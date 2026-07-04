# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref

**Version:** v2.4.1

**Status:** Canon

**Effective date:** 2026-07-03

**Last Update Gate:**  BN 11.9.9

**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **0.2 Scope \[Required-Now\]**

* **Supersession (PF10 addenda).** PF10 is living; when multiple **numbered** addenda exist, the later number supersedes earlier guidance. PF05 integrates the latest addenda and routes **by title only** to single homes (no version numbers). Build Notes reference posture: when citing PF10, reference by **addendum number \+ addendum title**; do not use PF10 version strings or PF10 section numbers as durable anchors.

* **Ownership.** This document owns the **bytes** for CLI, Reader transport, and Vendor ingest (HDAPI): payload shapes, validators, headers & conditional delivery, typed error mapping, and exit-code/stream rules. It is authoritative for CLI and Reader wire bytes. **Appendix A** transport matrices are kept in lockstep with **HDE-Governance §10** (titles only). Writers/errors posture is policy-owned in Governance; PF05 references it by title.

* **Public resonance posture (v1).** Public surface is **bands-only** and **numeric-free**; resonance is **SR-only** (`alpha=1.0`). `hysteresis=1` is armed for future XR and not exposed. Any XR diagnostics, if used, are **CLI-admin-guarded** and never emitted on Reader 200\.

* **Canonical JSON and locale.** All public bytes are UTF-8 (no BOM), ASCII-sorted keys, compact, with exactly **one trailing LF**. Arrays used as sets are deduped and ASCII-sorted. All byte checks and comparisons run with `LC_ALL=C`, `LANG=C`, and `TZ=UTC` (see **HDE-Schemas & Artifacts**).

* **Endpoint Catalog (JSON success): proof surface (A7).** The Catalog is **internal-only** and **env-gated** per entry; entries not gated for prod are **unreachable in production**. A7 transport proofs **must** run on a **§5.6 Endpoint Catalog (JSON success)** route (titles only; path-agnostic). Internal-ops `/internal/version` is **excluded** and governed by **HDE-Governance §10.5**. A7 **byte rules** are owned in **§5.3** of this document.

* **Single homes.** PF05 is the bytes/contract home for its CLI \+ transport surfaces; it does not own global token semantics or the canonical token roster (those are single-homed in **HDE-Governance**). PF05 may **reference** token names only where needed to pin acceptance claims for PF05 surfaces. PF05 also does not own the global Evidence Index: **HDE-Schemas & Artifacts (PF12)** is the single home; PF05 may list surface-specific artifact paths only when a byte-level contract or proof anchor requires an explicit file reference.

* **Evidence discipline (PF12 single home).** Evidence indexing (titles/paths only), the human Evidence Index and its hash sentinel, and the machine JSONL mirror are governed in **PF12** and must update **in the same PR** as artifact changes. CI enforces: 1:1 join equality (human↔machine), unknown-key rejection, ASCII field order, sort-before-write, **single mirror file**, and required `proof_anchor` path-proofs, per PF12.

  ## **0.3 Tagging convention**

* **\[Implemented\]** — Verified in the repository and exercised by surfaces/tests.  
* **\[Required-Now\]** — Required for current build goals; if missing in code, it is a gap to close.  
* **\[Speculative\]** — Accepted future design; preserved here but not yet wired.

  ## **0.4 Change policy**

* **Single homes; no duplication.** Do not restate Architecture/Math rules; keep CLI/Reader/Vendor **bytes here** and reference other documents **by title only**.

* **Governed paths only.** Evidence and acceptance artifacts must live under governed repo roots: `docs/**`, `artifacts/**`, and `audit/**`. For Live QA runs executed in Codespaces, mechanical evidence is check-scoped under the stable epic root `audit/qa/<epic-id>/checks/<check-id>/`; per-run nesting is disallowed. Transient generator paths (scratch/temp) are disallowed. Root sprawl is drift: any new top-level directory is nonconforming unless explicitly authorized by an ADR; enforce via lint or CI guard (fail the PR).

* **Lowercase directories (ASCII) only.** Don’t create mixed-case directories.

* **Deterministic CLI results.** Any CLI command results used in QA MUST satisfy determinism (AB↔BA) and be reproducible as described in §9. *(Token names live in Governance.)*  
* **Evidence anchoring.** Any evidence pointer emitted by the CLI must use governed repo roots and must be path-proven in the evidence index (see **Glow QA Guide** and **HDE-Governance §9** by title).  
* **Mirror schema check invocation (operator note).** `ci/checks/check_mirror_schema.sh` is a Python entrypoint. Invoke it as `python ci/checks/check_mirror_schema.sh` (or direct exec only if the executable bit is guaranteed). Do **not** run it via `bash ci/checks/check_mirror_schema.sh`; that invocation is invalid and is a known source of drift.  
* **Live QA Plan command-invocation materiality and rendered-escape review.** PF05 may preserve preferred command invocations for execution and evidence reproducibility. Command examples and vendor request examples in plans are not canonical invocation contracts unless PF05 or another owning PF explicitly makes command bytes the proof target. Distinguish normative protocol bytes from illustrative invocation syntax: vendor header names, route families, endpoint families, payload shape, auth posture, environment-variable identity, rails posture, and secret safety are substantive; shell wrapper form, heredoc formatting, indentation, rendered escapes, copied-chat damage, local invocation style, and paste-readiness are not blockers by themselves. A mismatch from preferred command spelling, path spelling, shell syntax, heredoc form, escaped option, interpreter choice, helper-code syntax, indentation, or pasted command form is a Live QA Plan approval blocker only when raw source changes execution, proves the wrong target, opens unsafe rails, exposes secrets, mutates prohibited state, prevents the check from running, makes PASS/FAIL unverdictable, or damages governed evidence trust. PF05 reviewers MUST judge raw command identity and raw artifact identity from source artifacts, governed records, canonical bindings, raw repo files, or execution transcripts, not assistant-rendered output, markdown previews, copied chat text, or review prose. A blocker based on escaping, syntax, command exactness, or shell-wrapper form requires raw/source proof of a separate executable, governed, canonical, safety, scope, evidence-identity, or semantic defect; otherwise the issue belongs in caveats, suggestions, execution notes, in-flight normalization, or the captured QA evidence command transcript.  
* **Process ownership.** Use the evidence-only PR template and follow the “update in same PR” workflow defined in **Epic-Process-Guide** (titles only). **Build Notes** are WIP only; drained guidance must land in canon.  
* **Documentation drainage is never a blocker.** PF10 drain and any later documentation drainage are never prerequisites, required deliverables, required checks, acceptance conditions, or readiness blockers for PF05-owned CLI, Reader, or Vendor work. Allowed blockers remain limited to truth and proof failures, such as missing required QA artifacts, untrusted evidence, or unresolved fail states that affect acceptance.  
* **PF10 carries live truth until later drain.** When an undrained canon delta affects PF05-owned surfaces, PF10 remains the temporary live-truth home until drainage occurs. Plans, reviews, QA artifacts, acceptance maps, step logs, and closeout materials may record later drain targets or doc-delta candidates, but they must not require PF document updates as execution or closeout conditions, and they must distinguish supportable-from-repo-evidence posture from already drained posture.  
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

* **Legacy BodyGraph request shaping — Implemented; HumanDesignAPI v2 pending.** Current PF05 request shaping is legacy BodyGraph-oriented and MUST NOT be treated as HumanDesignAPI v2 conformance. Until HDE-FERM006 through HDE-FERM008 close, v2 endpoint bytes, v2 auth names, request-body rules, response envelope mapping, and v1 legacy fallback policy remain pending and MUST be derived from the governed contract inventory rather than guessed. See §7.1.10 and §7.2.  
* **HumanDesignAPI v2 pending route set — Required-Now.** The pending v2 conformance work must reconcile `POST /v2/charts`, `POST /v2/charts/simple`, and `POST /v2/charts/coordinates` as the recommended v2 chart routes, and `POST /v1/bodygraphs` and `POST /v1/bodygraphs/simple` as legacy v1 routes. The suspect `api-reference/openapi.json` artifact MUST be quarantined until domain, title, server, and path-family validation prove it is a HumanDesignAPI artifact.  
* **Base-URL, API-version, and credential posture — Required-Now.** `HD_API_BASE_URL` is the canonical HumanDesignAPI base URL key and owns the vendor API-version boundary. Runtime request construction appends only version-neutral resource paths to the configured base URL, preserves any configured version path, and MUST NOT infer route behavior or auth-header family from hardcoded `/v1` or `/v2` path strings. `HDAPI_BASE_URL` is deprecated compatibility only, and conflicting `HD_API_BASE_URL` / `HDAPI_BASE_URL` values fail closed. `HD_API_KEY` is the canonical vendor credential key; v2 chart routes project it as `Authorization: Bearer`, and legacy v1 BodyGraph routes project it as `HD-Api-Key`. `GEO_API_KEY` is preserved where geocoding behavior requires `HD-Geocode-Key`.  
* **Live HTTP gated by SAFE rails — Required-Now.** Vendor calls are permitted only when rails are explicitly open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); default posture for dev/CI is closed. Closed-rails refusal behavior, admin override, and rails evidence live in §7.1. HumanDesignAPI v2 open-rails smoke, when required, remains PO-only and evidence-backed.  
* **Adapter data-source policy — Required-Now.** In prod, the adapter reads from DB on the hot path, using vendor only on explicit triggers (birth-data change, scheduled refresh, operator). In dev, direct vendor calls are allowed but must upsert into DB for repeatability. HumanDesignAPI v2 conformance MUST route through one sanctioned vendor seam and MUST NOT create a second HTTP home, bypass adapter guards, or bypass the presenter boundary. See §7.4.  
* **No-AI vendor boundary — Required-Now.** HumanDesignAPI v2 conformance is deterministic vendor-contract work only. PF05 MUST NOT add OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, AI acceptance-token, or AI-enablement bytes, flags, headers, config keys, routes, error mappings, or runtime obligations for this work.  
* **Production calls — Speculative.** Concrete timeout, retry, backoff, and observability profiles are defined in §7.3 and must be pinned before enabling production vendor traffic. Documentation consolidation alone does not prove live vendor conformance.

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

  # **3\) CLI Overview & Conventions \[Required-Now\]**

**QA status note (informative).** EPIC027 closed the CLI installability, help/version, argument-policing, showcompat parity/conformance, and deterministic sampler evidence slices. Governed CLI conformance evidence includes `artifacts/cli/help/hdctl_help.txt`, `artifacts/cli/help/showcompat_help.txt`, `artifacts/cli/help/reject_nonjson.txt`, `artifacts/cli/install/entrypoints.txt`, `artifacts/cli/install/installability_summary.json`, `artifacts/cli/ab.json`, `artifacts/cli/ba.json`, and `artifacts/cli/summary.json`. The current CLI evidence snapshot supports `CLI_PYPROJECT_ENTRYPOINT_OK`, `CLI_MODULE_RUN_OK`, `CLI_INSTALL_OK`, `CLI_HELP_EXIT_0_OK`, `CLI_HELP_STDOUT_OK`, `CLI_READER_PARITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, and `TWO_RUN_IDENTITY_OK`. All success output must come from the single canonical emitter, be UTF-8 with ASCII-sorted keys and exactly one trailing LF, and be validated under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

## **3.1 Global flags & process contract**

* **Packaging & entrypoints (normative).** Single home in **pyproject**:  
   `[project.scripts]` defines `hdctl = "engine.cli.main:cli"`.  
   **Module-runner parity:** `python -m engine.cli --help` ≡ `hdctl --help` (exit 0).  
   **QA status:** expected PASS for `CLI_PYPROJECT_ENTRYPOINT_OK`, `CLI_INSTALL_OK`, `CLI_MODULE_RUN_OK`, `CLI_HELP_EXIT_0_OK`, `CLI_HELP_STDOUT_OK`.  
* **Governed installability proof (normative).** `CLI_INSTALL_OK` evidence for the shipped console entrypoint MUST be positive and MUST NOT rely on skipped console checks. Governed installability artifacts are `artifacts/cli/install/entrypoints.txt` and `artifacts/cli/install/installability_summary.json`. The proof run MUST use a deterministic editable-install path (`PIP_NO_INDEX=1`, `--no-deps`, `--no-build-isolation`), require `console_entrypoint_available=true`, and keep module and console help/version facts single-sourced and internally coherent across the installability artifacts.  
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
* **Typed input error on failure.** Missing/unreadable file, non-JSON, schema failure, or canonicalization failure → **typed input error** (stderr code string token; no JSON envelope; see §3.4) on **stderr**; **stdout empty**.  
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

## 3.3 Streams discipline (stdout / stderr) \[Required‑Now\]

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
* **Typed errors (non-zero; command-specific).** Print a single stderr code string token (no JSON envelope), LF-terminated; `stdout` empty. Each command must pin its non-usage failure exit code(s) and emitted stderr code strings in its command contract (see §3.4, for example §4.1.4 for `showcompat`).  
* API error JSON (`error_v1`) must use the same canonical JSON rules and single emitter as success payloads. CLI error code strings are not JSON; they MUST be deterministic, LF-terminated, and free of timestamps, UUIDs, or environment-dependent content.

### **No mixed streams**

* Do **not** interleave diagnostics with public bytes.

* Logs/diagnostics go to `stderr` or files; **never** into stdout payloads.

* No secrets/PII in logs; redact if referenced.

  ### **Determinism pins**

* For the same inputs and flags, outputs (payload bytes, error bytes, and exit code) must be **stable** (**two-run identity**).

* All JSON emitted must follow §6.1 canonicalization.

* Locale/encoding pins: run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; UTF-8 only; single LF terminator; no BOM/ANSI.

### **Validation (binary)**

1. **Success (0):** `stdout ==` the command’s **canonical success payload** (byte‑for‑byte); `stderr` empty.

   * For Reader‑envelope commands, the canonical success payload is the six‑key Reader v1 body (§5.1).

   * For `hdctl showcompat`, the canonical success payload is compat JSON stdout (§4.1/§5.1).

2. **Error/usage:** `stderr` is LF‑terminated (JSON or synopsis); `stdout` empty.

3. **No ANSI / no extra lines:** grep‑guards block escape sequences; exactly one trailing LF.

4. 4\. **Canonical compare:** re-serialize JSON payloads and byte-compare (must match); checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

5. **Reader parity:** for any surface that emits Reader v1 bytes (Reader HTTP \+ CLI reader‑dump surfaces), those bytes are **byte‑identical** across Reader and CLI for identical inputs/environment.

6. **Determinism:** two‑run identity holds for both success and error paths.

**Routing (titles‑only).** Canonical JSON rules and chart schemas live in **HDE‑Schemas & Artifacts**; governance tokens and A7 posture live in **HDE‑Governance**.

## **3.4 Exit codes taxonomy \[Required−Now\]**

Exit codes are exhaustive for the public surface. Non-zero exits must not print partial payloads on stdout. JSON emitted on stdout uses the single presenter/emitter (§6.2) and canonical JSON (§6.1).

#### **Codes**

* `0` — Success. `stdout` is a single canonical JSON value (object or array), LF-terminated; `stderr` empty.

* `64` — Usage. `stderr` is a short human synopsis; `stdout` empty.

* Other non-zero exit codes are command-specific. On failure, `stderr` contains exactly one line: a single code string token, LF-terminated (no JSON envelope); `stdout` empty.

#### **Global rules**

1. **No mixed streams:** stdout is reserved for success payloads only; all failures write only to stderr.

2. **No ANSI/no control bytes:** `stderr` MUST be plain UTF-8 text; do not emit colors, cursor codes, or progress spinners.

3. **Exactly one trailing LF:** `stdout` success payloads and `stderr` error code strings must each end with exactly one LF.

4. **No partial payloads:** if an error occurs after emitting some bytes, the command MUST treat that as failure and MUST NOT leave partial JSON on stdout.

#### **Validation (binary)**

1. **Success:** If `exit=0`, assert `stdout` parses as JSON and round-trips byte-identically under `serializer_v1` after canonicalization and single-LF normalization; assert `stderr` empty.

2. **Usage:** If `exit=64`, assert `stderr` is human text and ends with one LF; assert `stdout` empty.

3. **Failure:** If `exit!=0` and `exit!=64`, assert `stdout` empty; assert `stderr` is exactly one non-empty LF-terminated line containing a single code string token.

4. **Token correctness:** For failures, assert the stderr code string token is stable, numeric-free, and listed in the command contract. If the failure maps to an HTTP `error_v1`, assert the token matches the transport `error_v1.code`.

5. **Determinism:** two-run identity and AB↔BA parity hold for error paths as well as success.

**Routing (titles-only).** Canonical JSON rules: HDE-Schemas & Artifacts. A7 transport rules and SAFE rails: HDE-Governance and §5.3 of this document.

---

## **3.5 Single-emitter parity with Reader**

* **One entrypoint.** CLI public bytes MUST be emitted via the byte-authoritative presenter/emitter entrypoint defined in §6.2. Wrapper envelope builders MAY exist (for example Reader v1 envelope emission), but they MUST delegate byte emission to the byte-authoritative entrypoint and MUST NOT serialize public bytes outside it. Output is UTF-8, ASCII-sorted keys, compact separators, exactly **one LF**.  
* **No ad-hoc serialization.** Forbid `json.dumps(`, `jsonify(`, templating, or any local “mini-emitters” on public paths.  
* **Symbol allow-list and CI guard.** Pin the allow-listed presenter/emitter emission symbol(s) as the only permitted public serializer entrypoint. CI must fail if public paths reference non-allow-listed serializer symbols or contain disallowed patterns (grep-guard). Tests must assert that CLI and Reader public bytes are emitted via the byte-authoritative entrypoint, and that any wrapper envelope builders delegate without introducing alternate serialization.  
* **Preimage recipe.** Build the preimage as defined in **PF01** (do not restate fields here), compute `idempotence_hash`, then re-emit the final six-key body.  
* **Determinism & parity.** A single byte-authoritative emitter ensures Reader↔CLI byte equality, **AB↔BA parity**, and **two-run identity** for identical inputs/environment.  
* **Evidence.** Provide (1) grep-guard report, (2) import graph/reflection proof that CLI and Reader call only allow-listed emission symbols and that wrappers delegate byte emission to the byte-authoritative entrypoint, and (3) byte-compare fixtures showing CLI stdout equals Reader body. **Evidence is indexed in PF12** (records-only; titles-only).

  ## **3.6 Determinism expectations for stdout**

* **AB↔BA parity.** For identical inputs differing only by pair order, stdout bytes are identical (including the single trailing LF).  
* **Two-run identity.** Running the same command twice with the same inputs/environment produces byte-identical stdout.  
* **Schema & shape gates.** The printed stdout payload must validate the **owning contract for that command’s stdout**:  
  * For Reader-envelope-on-stdout surfaces (if any exist), stdout must satisfy the six-key Reader v1 covenant in §5.1.  
  * For `hdctl showcompat`, stdout must satisfy the compat JSON contract in §4.1/§5.1 and must **not** be required to match the Reader v1 six-key covenant (Reader v1 bytes are produced via the reader-dump path).  
  *  Any contract or canonicalization violation results in a single stderr code string token (no JSON envelope) with an exit code pinned by the command contract (see §3.4); stdout must be empty on failure.    
* **Locale/TZ pins.** All CLI tests and byte comparisons run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

## **3.7 Interim “no-user” QA mode (pre-Glow prod)**

**Status.** Informative for HDE-EPIC017 Live QA. CLI bytes and flag semantics in this document remain canonical; this subsection constrains **how** those commands are used in the current production environment until a Glow App user model exists.

**Environment premise.**

* No app-level user model is integrated with the HD Engine.

* No persistent user-bound BodyGraph records exist in production.

* We must not create app-like user records in prod ahead of Glow App integration.

**Compat & Reader (`hdctl showcompat`).**

* For pre-Glow prod QA, use `hdctl showcompat` with **birth arguments only** as the primary public or birth-facing compat harness:  
  * `--birthdate-a/-b`, `--birthtime-a/-b`, `--location-a/-b`.  
* In this environment, **set `--source vendor` explicitly** for birth-based compat runs. The default source selection may follow DB/auto paths that are blocked or misconfigured when there is no user model.  
* For po-006 remediation and equivalent pre-App no-user compat review, keep these proof classes separate:  
  * public numeric-free output proof,  
  * internal/admin compatibility compute proof,  
  * vendor-backed no-user behavior proof.  
* The public or birth-facing compatibility path MUST NOT require caller-provided `person_uid`, caller-provided `user_id`, app user IDs, DB-backed user BodyGraphs as caller input, or user-bound DB records.  
* Existing direct compatibility tests that use full-argument UID-backed inputs do not prove no-user behavior. Source-skewed failure logs, grep-only numeric-free checks, and fixture-only `person_uid` injection MUST NOT be treated as sufficient proof for live or birth-facing no-user behavior.  
* Strict compatibility compute MAY remain internal/admin only if a sanctioned no-user boundary supplies deterministic internal metadata before compute. Boundary-generated internal metadata may be used only inside that sanctioned resolver or adapter boundary and does not create a caller requirement, public route, public flag, or public contract.  
* UID-coupled ordering or pair identity metadata required by internal compute MUST be derived only inside the sanctioned no-user resolver or adapter boundary. It MUST NOT become caller-supplied `person_uid`, caller-supplied `user_id`, app user ID, DB-backed user BodyGraph input, route flag, public contract, or proof requirement for public or birth-facing no-user compatibility.  
* The accepted PR-02 local boundary proof class is birth-only caller input: `birthdate`, `birthtime`, and `location`, with neither caller-provided `person_uid` nor caller-provided `user_id`. That local proof does not replace the separate vendor-backed no-user behavior proof.  
* Local pytest and grep checks MAY prove public numeric-free posture, canonicalization, serializer/math properties, or internal compute properties only when labeled as such. They MUST NOT substitute for vendor-backed no-user behavior proof when the claim is live behavior in the current pre-App/no-user environment.  
* Until the product implements a facility to store and replay BodyGraph data locally for QA, Live QA cannot rely on precomputed BodyGraph inputs being available for showcompat runs. Functional birth-based compat runs therefore require vendor acquisition under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`) for the showcompat step. If rails are closed, treat the outcome as an expected blocker or typed refusal for that step, not a product behavior failure. Rails changes must be explicit and step-scoped; restore the default rails posture after the showcompat step.  
* A controlled vendor-backed no-user smoke, when used as PF05 `showcompat` implementation-validation evidence, MUST be PO-only and IA-guided. Automated agents MUST NOT run the vendor call, and no command may be modified by guesswork to force a PASS.  
* For an OPS-02 style controlled vendor smoke, “no-user” means the external command and caller-facing proof use birth data only.  
* Allowed caller or command inputs are limited to:  
  * `--source vendor`,  
  * `--birthdate-a`,  
  * `--birthtime-a`,  
  * `--location-a`,  
  * `--birthdate-b`,  
  * `--birthtime-b`,  
  * `--location-b`.  
* Forbidden caller or command inputs include:  
  * `--user-a`,  
  * `--user-b`,  
  * `--a-user`,  
  * `--b-user`,  
  * app user IDs,  
  * `user_id`,  
  * `person_uid`,  
  * DB-backed user BodyGraphs as caller input,  
  * `--source db`,  
  * any inline secret value.  
* The executable command recorded for the controlled smoke MUST be an `hdctl showcompat --source vendor` command with the six birth flags for A and B. Birth values MUST come from `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json` when that file exists, and the recorded command MUST contain no unresolved placeholders before execution.  
* For this CLI vendor smoke, the target is the HD Engine CLI running in the PO-controlled execution context. Required target facts are `hdctl showcompat`, `--source vendor`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when required by the command path, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and `APP_ENV=dev`.  
* `HDE_BASE_URL` is not required for this exact CLI vendor smoke unless the command changes to call an HD Engine HTTP service. If the target changes from CLI vendor execution to an HD Engine HTTP service call, a new infrastructure-backed target fact set is required before execution.  
* OPS-02 style controlled smoke execution MUST NOT run unless these conditions are proven before execution: exact command, complete birth-only input values, no user identity in the command, no inline secrets, explicit vendor source, open rails for the vendor step only, determinism pins, required vendor environment presence, safe secret posture, accepted PR-02 birth-only proof, and PO proceed authorization.  
* If required command proof, birth input, rails, vendor environment presence, PR-02 accepted proof, or PO proceed authorization is missing, record `TOOLING_BLOCKED`. If a user identity input, inline secret, guessed command change, missing evidence file after an attempted run, or secret-bearing artifact appears, record `FAIL_TOOLING`. If prerequisites are proven and runtime behavior contradicts expected birth-only no-user vendor behavior, record `FAIL_BEHAVIOR`.  
* A `PASS` classification is allowed only when the exact command runs with exit code `0`, uses `--source vendor`, uses birth-only flags, supplies no app user ID, no `user_id`, and no caller-provided `person_uid`, persists no secret values, emits non-empty parseable JSON on stdout unless the documented success output differs, and records that the smoke is implementation-validation evidence only.  
* The controlled vendor smoke is implementation validation only. It is not a QA rerun, not a Live QA plan, not a closure decision, not a PF09 status change, not PF-canon drain completion, and not a substitute for final po-006 QA.  
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

## 4.1 hdctl showcompat \[Implemented; Required‑Now\]

### 4.1.1 Purpose and posture (normative)

`hdctl showcompat` is the canonical compat harness for:

* Computing the full Magic‑10 compat result (scores, bands, narrative keys) for a pair of BodyGraphs; and

* Producing both:

  * **Compat JSON** on stdout for admin/QA (full compat detail: all categories, bands, scores, narrative keys); and

  * An optional **Reader v1 success envelope** (six‑key, numeric‑free) via its **reader‑dump** path, byte‑identical to the Reader API.

It is an admin/QA tool, not a public API. It is **implemented** in the CLI but remains **merge‑blocking** until determinism and Reader↔CLI parity tokens are proven green.

*Single emitter.* All JSON surfaces (stdout compat JSON, reader‑dump envelope, admin sidecars) must use the single canonical presenter/emitter shared with Reader (§6).

### 4.1.2 Inputs — flags and normalization (normative)

`showcompat`supports three input families for the *pair* of BodyGraphs; flags below are as reported by the Codex CLI audit and are now normative.

**Input requirement (normative).** `hdctl showcompat` MUST be invoked with explicit inputs for the pair. A zero-argument invocation is a usage error (exit 64\) and cannot be treated as a functional proof.

**Help-surface compatibility aliases (informative).**

* CLI help may expose `--user-a-id` and `--user-b-id` as long-form aliases for the DB-backed user input family. Canonical PF05 prose continues to use `--user-a` / `--a-user` and `--user-b` / `--b-user`.

* CLI help may expose `--format {json}` as a JSON-only compat-output selector. This does not widen the byte contract beyond canonical JSON.

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

**Conjunction mode (`--conjunction`).**

* Mode: `--conjunction`.

* When `--conjunction` is used, both parties (A and B) are required. Missing either MUST produce a usage error.

* When `--conjunction` is used, the input sources are:

  * Two user IDs (A and B) from either `db` or `vendor` (via `--a-user` \+ `--b-user`).

  * File-based BodyGraph fixtures (does not require user IDs), via either:

    * `--pair-file <path>` (legacy alias: `--file <path>`).

    * `--a-file <path>` \+ `--b-file <path>`.

  * Stdin-based BodyGraph fixtures (does not require user IDs), via `--stdin` (payload MUST include both `left` and `right`).

* `--conjunction` is a read-only computation and MUST NOT mutate state.

* `--conjunction` emits a public conjunction payload under stable top-level key `conjunction`.

* When `--conjunction` is used, `--viewer-prefs` is ignored. (Conjunction output does not use viewer prefs.)

* When `--conjunction` is used, `--compat-format` is ignored. (Conjunction output is not a compat report.)

* When `--conjunction` is used, dump and sidecar flags are disallowed. This includes `--dump-reader`, `--dump-admin-dir`, and `--admin-sidecar` (or equivalent aliases). Invalid conjunction flag combinations follow the usage-error rules in §4.1.4.

* `--conjunction` does not change `--source` legality: `--source` remains limited to `db`, `vendor`, or `auto`.

**Normalization (AB↔BA).**

Before invoking compat math, `showcompat` **must normalize the pair** into a canonical order (AB↔BA neutral). The compat engine sees a canonical `(a,b)` regardless of flag order or input ordering.

**Rails interaction.**

* For `--source=db`, `showcompat` must **never** perform vendor I/O.

* For `--source=vendor` or `auto` paths that require a vendor call:

  * Vendor I/O is allowed **only** when `SAFE_MODE=0` and `ALLOW_NETWORK=1`.

  * With rails closed (default in dev/CI), a vendor‑required run must **fail closed** with a typed refusal (no network).

* Rails resolution uses the same `_resolver_env()` mechanism as `bg:resolve` (SAFE rails and env policy are titles‑only in Governance/Mechanics).

### 4.1.3 Output surfaces and shapes (normative)

`showcompat` has **two** primary byte surfaces and optional admin sidecars:

1. **Compat JSON to stdout (admin/test surface)** — **primary** CLI output.

2. **Reader v1 success envelope via reader-dump** — **secondary parity surface**.

3. **Admin sidecars** — optional, file-backed diagnostics.

All JSON surfaces:

* Emit exactly one final line feed (`\n`) at end-of-stream and no other framing lines.

* Line endings MUST be LF-only. CRLF (`\r\n`) is forbidden anywhere in the emitted bytes.

* Double-blank-line separators are forbidden (do not emit `\n\n` patterns in the emitted bytes).

* Encoding is UTF-8 without BOM.

* Keys sorted lexicographically (ASCII, stable).

* Treat arrays that represent sets as deduped and ASCII-sorted.  
  ---

**1\) Compat JSON — stdout (primary)**

On success, and **in the absence of explicit reader-dump overrides**, `showcompat` **MUST** write a single LF-terminated compat JSON object to **stdout**, and **MUST NOT** print the Reader v1 envelope directly to stdout.

**Envelope (informative outline).**  
 Compat JSON is a single object, canonically emitted, whose high-level shape is:

`{`

  `"a": { … },`

  `"b": { … },`

  `"viewer_prefs": { … },`

  `"compat": {`

    `"categories": [ … ],`

    `"meta": { … }`

  `}`

`}`

*The exact internal schema (fields for scores, bands, narrative keys per category, and identity fields) is owned by this document (later sections) and the HDE-Mechanics Guide (titles-only), and is **not** the Reader v1 envelope.*

**Semantics.**

* `a` / `b` describe the pair participants and resolved BodyGraphs for this compat run.  
* `viewer_prefs` captures viewer-preference inputs where applicable (for example `top_category` and weights across the Magic-10 set). In pre-App QA contexts it is expected to be present but neutral (equal weights) unless the test explicitly varies it.  
* `viewer_prefs` MUST be validated and normalized before compat computation. Normalization preserves Magic-10 weight semantics and exposes the normalized weight for a candidate top category to the sampler/ranker handoff; the sampler/ranker remains the behavior owner for excluding candidates whose top category has viewer weight 0\.  
* Compat computation MUST NOT create a second zero-weight exclusion home in the CLI or presenter, and this normalization/handoff rule does not create a new route or public contract.  
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

### **4.1.4 Errors and exit codes (normative)**

Exit codes follow §3.4. The mapping for `showcompat`:

* `0`: Success; stdout is canonical JSON (plus exactly one trailing LF); stderr empty.  
* `64`: Usage; stderr is a short human synopsis; stdout empty.  
* If a `--format` selector is supplied with a non-JSON value (for example `--format yaml`), the invocation MUST fail as a usage error with exit code `64`, empty stdout, and parser rejection text on stderr. This includes conjunction-mode invocations.  
* `1`: Failure; stdout empty. `stderr` contains exactly one line: a single code string token, LF-terminated (no JSON envelope).  
  * For CLI stdout invariants, the stderr code string MUST be one of:  
    * `STDOUT_MISSING_LF` indicates missing final LF on emitted stdout bytes.  
    * `STDOUT_CRLF` indicates CRLF was detected in emitted stdout bytes.  
    * `STDOUT_NOT_CANONICAL_V1` indicates stdout parses as JSON but is not canonical under `serializer_v1` (does not round-trip through canonicalization).  
  * For engine/internal/vendor failures, the stderr code string MUST match the canonical `error_v1.code` that would appear for the same failure on HTTP surfaces.  
  * Conjunction closed-rail data refusal: if `--conjunction` is set and a required local BodyGraph is missing while the needed access path is unavailable due to rails being closed, `stderr` MUST be `PROVIDER_REFUSED` and `stdout` MUST be empty.  
* Other non-zero codes are reserved; in all cases stdout remains empty.

Streams follow §3.3/§3.4. HTTP error envelopes follow §5.2.

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

Determinism caveat: `hdctl showcompat` currently depends on vendor-backed computation when exercised against the vendor-backed engine (OPEN rails). Deterministic QA is therefore bounded; a fully deterministic, offline `showcompat` path requires either a local compute path or a cached or seeded deterministic vendor stub that can run under SAFE rails.

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

* `COMPOSITE_ABBA_IDENTITY_OK` — AB↔BA identity for stdout compat JSON and reader-dump envelope in the chosen environment.

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

## 4.2 hdctl read singlebg \[Speculative\]

*(Unchanged in spirit; shown here only for completeness with minor wording aligned to Option B. No new semantics were invented.)*

**Purpose (normative, draft).**  
 Emit a single‑chart diagnostic to stdout using the same canonical emitter as Reader/CLI success bodies (UTF‑8, sorted keys, compact, exactly one LF). This command is for testing & debugging chart ingestion/normalization; it is not a product surface. It does **not** change the Reader v1 public envelope.

**Inputs, stdout schema, errors, and acceptance** remain as in the existing PF05 text (single‑chart file input, optional tz override, schema gate, canonical JSON, two‑run identity, stderr‑only errors). No dependency on compat JSON or narratives.

Implementation status (audit v1): **Not implemented**; see existing PF05 language for details.

---

## 4.3 hdctl list people \[Speculative\]

Needs development.

---

## 4.4 Fetch commands (person/batch) \[Speculative\]

Needs development.

---

## 4.5 CLI Admin Preview (narrative) \[Required‑Now\]

`hdctl aux-preview` remains the admin preview surface for Aux narrative text and IDs, reading compat JSON from `--pair-file` and calling the Aux emitter. It must **not** change Reader 200 bytes; it is admin‑only and LF‑only. Needs further development.

---

## 4.6 hdctl bg:resolve \[Required-Now\]

`hdctl bg:resolve` is the operator command for resolving a single BodyGraph for a given key and data source.

**Inputs and sources (normative).**

* `--user <id>` — engine user key. In the long run it is expected to align with a Glow App user ID; in pre-Glow prod QA it is used as an **ephemeral QA key** and not as a durable app user identifier.

* `--source {db|vendor|auto}` selects the data source:

  * `db` — resolve from DB only (no vendor I/O).  
  * `vendor` — resolve from vendor only; vendor HTTP calls are allowed **only** when SAFE rails are open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`). Shaping and error mapping follow §7.1/§7.2/§7.3 and the policies in **HDE-Governance** and the **HDE-Mechanics Guide** (titles-only).  
  * `g:resolve --source vendor` route-policy boundary — configured v2 bases MUST select `unsupported_runtime_nonclaim` and fail closed with `PROVIDER_ROUTE_UNSUPPORTED` before legacy `bodygraphs` request construction. Non-v2 configured bases MAY preserve the legacy BodyGraph route only as explicit legacy fallback. `v2_chart_backed_bodygraph_resolution` and `dual_route_policy` are not implemented and MUST NOT be inferred from `charts/simple` or other v2 chart evidence without a future adapter/schema proof or ADR-backed canon update. This route policy preserves HD Engine ownership of vendor acquisition and BodyGraph resolution, keeps secrets and raw payloads out of evidence, and preserves nonclaims for full HumanDesignAPI v2 runtime conformance, public Reader changes, public routes, public payload changes, new HTTP homes, app-side vendor credential ownership, raw payload persistence, and AI scope.  
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

  * When `APP_ENV` is unset, empty, or set to any other value (including `prod`), the handler **MUST** return a **403 Forbidden** response using the typed error envelope from §5.2 with `code: "ERR_WRITER_FORBIDDEN"`, and **MUST NOT** call the sampler core. The body is a numeric-free error object; `Cache-Control: no-store`; no `ETag`.

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

# 5\. Reader Transport (public bytes) \[Required‑Now\]

## 5.1 Success envelope \[Required‑Now\]

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

All byte checks run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC` (where relevant), as described in PF01/PF12 (titles-only).

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

1. **Typed, numeric-free error\_v1 envelope.** All governed HTTP error surfaces (Reader errors, diagnostic writer errors, and internal health/ready/not-found error responses) **MUST** emit the **error\_v1** JSON envelope, serialized by the single canonical emitter (§6.1/§6.2) and LF-terminated. The **minimum** shape is:

    `{"schema": "v1", "ok": false, "code": "<ERR_*>", "error": "<non-PII message>"}`

   1. `schema` — fixed string `"v1"` for this error envelope.

   2. `ok` — boolean, always `false` for error\_v1.

   3. `code` — canonical **UPPER\_SNAKE** error token from the governed **error token map** (see below).

   4. `error` — human-readable, non-PII, non-secret message.

2. Optional fields are defined in the schema owned by **HDE-Schemas & Artifacts** (titles-only). Today this includes:

   1. `retry_after_ms` — integer ≥ 0, **only** when the transport policy explicitly permits it (e.g. deterministic 429 handling for vendor rate limits).

   2. `details` — optional object for additional structured context; the allowed fields and structure are governed by the error\_v1 schema and must remain numeric-free on public surfaces.

3. No other fields may appear in the public error\_v1 envelope.

4. **Canonical error token map (`ERR_*`) and aliases.**

   1. Canonical error tokens are defined in a governed **error token map** (for example `ERROR_TOKEN_MAP` in the engine) and are emitted as **UPPER\_SNAKE** strings in the `code` field, such as:

      1. `ERR_COMPAT_INVALID_JSON`

      2. `ERR_INVALID_VIEWER_PREFS`

      3. `ERR_MISSING_NARRATIVE_KEY`

      4. `ERR_READER_INVALID_VERSION`, `ERR_READER_FORBIDDEN`, `ERR_READER_MISSING_PARAM`, `ERR_READER_INVALID_CHART`, `ERR_READER_INVALID_PATH`, `ERR_READER_MISSING_TZ_A`, `ERR_READER_MISSING_TZ_B`

      5. `ERR_WRITER_INVALID_CONTENT_TYPE`, `ERR_WRITER_INVALID_JSON`, `ERR_WRITER_INVALID_INPUT`, `ERR_WRITER_UNKNOWN_KEY`, `ERR_WRITER_REQUEST_TOO_LARGE`, `ERR_WRITER_UNAUTHORIZED`, `ERR_WRITER_FORBIDDEN`

      6. `ERR_NOT_FOUND` for canonical 404/405 mappings.

   2. Legacy lowercase strings such as `"invalid_json"`, `"invalid_prefs"`, `"missing_narrative_key"`, and `"forbidden"` are retained as **input aliases** inside the engine code (for example for older tests or call sites). Public surfaces **MUST** emit canonical `ERR_*` codes in the `code` field; dev-only compat probe behavior may explicitly allow legacy codes (see §5.5).

   3. Any new error condition added in future work **must** be represented by a canonical `ERR_*` token in the map first, and only then wired into Reader, writer, and CLI surfaces.

5. **Headers (normative).**  
    `Content-Type: application/json; charset=utf-8` · `Cache-Control: no-store` · **no `ETag`** on error and writer responses. A7 conditional rules for success responses live in §5.3.

6. **Streams.** CLI failures emit a single LF-terminated stderr code string token (no JSON envelope); stdout remains empty on failure. HTTP consumers receive error\_v1 in the response body. Public JSON bytes are canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

7. **Determinism & parity.** Given the same inputs/environment, HTTP error bodies are **byte-identical**; **AB vs BA** does not change the error. If the same error condition is surfaced on both CLI and HTTP, the CLI stderr code string token MUST equal the HTTP error\_v1 `code` value for that condition (token-level parity); envelopes are not required to be byte-identical across surfaces.

8. **Refusal vs 429 (policy note).** **Refusal** (rails closed) is an **ops surface**, **not** an A7 proof surface. Transport invariants on refusal: `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, **no `ETag`**, **no `Vary`**, **no `Content-Encoding`**. **429** is an A7 transport outcome and **may** include `retry_after_ms`. Keys-only log allow-lists and error token semantics are owned in **HDE-Governance** (titles-only).

   ### **Validation (binary)**

1. **Schema gate:** Ensure JSON matches the error\_v1 schema (HDE-Schemas & Artifacts).

2. **Fields gate:** Ensure no numeric fields appear, and only schema-allowed optional fields appear.

3. **Token map:** For public surfaces, emitted `code` values are canonical `ERR_*` tokens; lowercase legacy aliases are not emitted. For dev-only compat probe behavior, allow only the explicitly documented legacy code cases.

4. **Parity:** If the same failure is surfaced on the CLI (`hdctl`) and on a transport route, the CLI stderr code string token MUST equal the transport error\_v1 `code` value for that failure.

5. **A7 checks:** All error bodies must be canonical JSON and must not violate A7 conditional/header policy (see §5.3).

**Routing (titles-only).** The error\_v1 schema and error token map are owned by **HDE-Schemas & Artifacts** and **HDE-Governance** (titles-only). Canonical JSON rules live in **HDE-Schemas & Artifacts (§4)**. Governance tokens covering error behavior live in **HDE-Governance (§2.0 Acceptance Tokens)**.

---

## **5.3 Conditional delivery (A7) \[Required-Now\]**

These transport bytes are owned here; PF05 owns **Reader bytes only** and keeps matrices in lockstep with HDE-Governance (writers live in Governance; titles only). Bodies use the canonical serializer (§6.1). **A7 proofs run only on a PF05 Endpoint Catalog (JSON success) route** (titles only; the route entry must be marked `a7_eligible: true`). Internal-ops `/internal/version` is excluded.

* **ETag identity & conditional sequence.** On 200 success, emit a **strong, quoted ETag** over the **LF-terminated canonical body** (pre-compression). A **304 Not Modified** may be returned **only after** a prior 200-with-body for the same identity. **HEAD** mirrors 200 validators and never has a body.  
* **304 entity headers (tightened).** **Omit both** `Content-Type` **and** `Content-Length` on 304\. Body is empty. Suppress any automatic framework emission of `Content-Length` on 304 responses.  
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

* **Canonical Reader route.** The Reader HTTP surface is defined as `GET /reader` and is the canonical Reader route for the v1 dev/proof surface.

* **Version selection.** Reader v1 is selected via query parameter `v=1` on the Reader route, without changing the route path.

* **API-mount alias posture.** When the Reader blueprint is mounted under an `/api` prefix in a runtime configuration, `/api/reader` (and `/api/reader?v=1`) is an alias of the same Reader surface as `/reader` (and `/reader?v=1`). It is not a distinct contract or a separate proof surface.

* **Aux narrative surface.** The auxiliary narrative surface is served at `/aux/narrative`. This route is a narrative surface and exists in the same adapter HTTP surface family.

* **Forbidden invented route.** There is no `/api/reader-proof/v1` route. Plans and docs must not reference it.

* **Proof-surface selection posture.** Any QA proof that depends on a Reader success route must reference the actual reachable Reader route for the target environment. When an Endpoint Catalog is used, the proof route must be selected from the catalog entries that correspond to the real mounted routes. Do not invent alternate proof routes.

* **Scope note.** This note records the canonical state of Reader surfaces for planning and QA. It does not introduce new routes, change public contract semantics, or mint new acceptance obligations.

* **Gate.** The route **must** be gated by `APP_ENV=dev` and bound only to a local interface (for example, `127.0.0.1`), or disabled entirely. It must not be mounted in production builds or non-dev deploys.  
* **Documented local-style access (clarification).** Where PF05 shows a dev or QA example address for a non-prod local-style surface, it MUST use `127.0.0.1` as the default documented client host, plus the effective port and endpoint path. This is a client-access convention only; it does not redefine service identity or server bind address. Prod-facing targets keep their real hosted addresses. If a surface cannot be reached at `127.0.0.1` from the intended operator context, PF05 must state an explicit exception and the real access route. `localhost` is not the preferred canonical example host.

* **Rails closed.** Harness runs with rails closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); it never opens vendor rails.

### **Emitter and parity (must)**

* **Single emitter.** All harness success and error bodies are emitted by the **same shared presenter/emitter** as Reader and CLI (§6.2).  
* **Reader↔CLI parity.** For identical inputs and environment, harness responses are **byte-identical** to `hdctl showcompat` stdout (six keys, LF).  
* **Determinism.** **AB↔BA** parity and **two-run identity** must hold at the byte level.

### **Serialization (canonical)**

* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF. Arrays used as sets are deduped & ASCII-sorted (§6.1). All comparisons run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
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

* **Path.** `POST /api/compat/v1` (dev only).  
* **Method posture.**  
  * `POST` performs evaluation and returns the pair (dev/internal only).  
  * `GET /api/compat/v1` is probe-only (health): it MUST NOT compute compat and MUST NOT accept a request body.  
  * If a request body is present on `GET`, return typed error\_v1 with `code=ERR_COMPAT_INVALID_JSON`.  
  * `GET /api/compat/v1` returns a fixed probe payload: `{"schema":"v1","ok":true}` (canonical bytes).  
* **Request body (POST).** JSON object: `{"a_id":"<uid>","b_id":"<uid>","viewer_prefs":{}}` where:  
  * `a_id`, `b_id` are opaque user ids (strictly `UID_RE` and non-empty).  
  * `viewer_prefs` is the viewer-preference object for the compat run. It MUST be validated and normalized before compat evaluation. Missing, non-integer, incomplete, out-of-range, or unknown-category preference inputs remain typed `ERR_INVALID_VIEWER_PREFS` failures.  
  * The normalized viewer-preference object MUST preserve weight 0 semantics for downstream sampler/ranker exclusion and MUST follow the same normalization posture used by `hdctl showcompat`.  
* **Validation and environment gating.**  
  * Reject invalid or empty `a_id`/`b_id` before any person resolution; do not allow empty strings to propagate into server errors.  
  * In `APP_ENV=prod`, `POST /api/compat/v1` MUST return 404 with error\_v1 `code=ERR_NOT_FOUND` (internal surface must not be exposed).  
* **Success body (dev/internal).** Returns the §7A pair contract and bytes for the public Reader v1 payload.

**Error body.** Typed, numeric-free **error\_v1** envelope as defined in §5.2: `{"schema":"v1","ok":false,"code":"<ERR_*>", "error":"<message>", ...}`. For this route, the canonical codes include:

* `ERR_COMPAT_INVALID_JSON` for malformed or mixed `a`/`b` payloads (for example mixing `*_id` and full person payload for the same party),

* `ERR_INVALID_VIEWER_PREFS` for missing/non-integer or incomplete viewer preference weights,

* `ERR_MISSING_NARRATIVE_KEY` when a required narrative key is absent or unresolvable for a compat category.

Legacy lowercase strings such as `"invalid_json"`, `"invalid_prefs"`, and `"missing_narrative_key"` remain accepted **aliases** internally, but are resolved via the error token map into their canonical `ERR_*` equivalents before error\_v1 is emitted. The public `code` field on this route **MUST** carry the canonical `ERR_*` tokens, not the aliases.

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

* **Proof posture (compat route).** Governed parity proof for this dev-only compat surface MUST exercise the in-repo app-client surface on `POST /api/compat/v1` under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`). Vendor-backed `hdctl showcompat --source vendor` is not the governing proof surface for this route.  
* **Compat-route proof bytes:** `artifacts/compat/AB.json`, `artifacts/compat/BA.json`, `artifacts/compat/identity_hash.txt`.  
* **CLI parity (public):** `artifacts/cli/reader_cli_parity.bytes`.  
* **Harness headers:** `artifacts/cli/transport/post_nonconditional_proof.log`, `artifacts/cli/transport/no_secrets_error_headers.log`.  
* **Serializer guards:** `artifacts/cli/guards/serializer_grep_guard.log`, `artifacts/cli/guards/emitter_symbol_proof.txt`.  
* **Guard regression and index coverage:** `tests/cli/test_serializer_guards.py`, `tests/ops/test_evidence_index.py`.  
* **(If sidecar enabled)** internal-contract parity bytes for compat v1 (file path per Doc-Delta).  
   **Indexing discipline:** update **PF12** human `docs/evidence/INDEX.json`, **hash sentinel**, and machine `artifacts/evidence_index.jsonl` **in the same PR**.

**Routing (titles-only).** §7A contract lives in **HDE-Mechanics Guide**. A7 transport policy lives in **HDE-Governance** (A7) and §5.3 / Appendix A here. Canonical JSON rules: **HDE-Schemas & Artifacts** §4. Tokens: **HDE-Governance** §2.0.

## **5.6 Endpoint Catalog (JSON success) \[Required−Now\]**

**Purpose and scope.** This section defines the governed Endpoint Catalog used to (a) declare internal Reader and dev/admin HTTP surfaces that exist for this Epic, (b) classify them for proof selection and exposure control, and (c) anchor A7 proof execution. This Catalog is **internal-only** and **not a client contract**.

**Rules (normative).**

* The Catalog is the governed inventory of endpoints for this Epic. It may include literal `path` strings because they are proof anchors (see §0.2 public resonance posture).

* For each catalog entry, declare at minimum:

  * `path` (literal HTTP path)

  * `allowed_methods` (explicit allow-list)

  * `internal` (boolean)

  * `class` (surface class; at minimum `dev_harness` and `internal_admin`)

  * `env_gate` (non-empty for any non-public surface; must prevent accidental production exposure)

  * `a7_eligible` (boolean; true only for Reader success surfaces where A7 proofs must run)

**Terminology disambiguation (normative).**

* In PF05, "Endpoint Catalog" refers to the governed `docs/ENDPOINTS_CATALOG.json` artifact (and its machine mirrors listed in Appendix D).

* This catalog is distinct from OpenAPI-like public contracts: it is an internal proof anchor and exposure-control surface map.

**A7 transport invariants applicability.**

* §5.3 A7 invariants apply only to routes whose catalog entry has `a7_eligible: true`.

**Population policy (normative).**

* Entries must be env-gated unless they are public client surfaces.

* Internal-ops `/internal/version` is excluded.

* The Catalog must include dev-harness Reader success routes used by A7 proofs.

* Internal admin/dev-only routes (example: compat admin) must be declared POST-only when applicable and must not be `a7_eligible`.

### **Catalog entries (normative; minimal)**

* **Reader success route (governed proof surface; dev-harness class):** `/reader`  
  * path: `/reader`  
  * allowed\_methods: \[`GET`, `HEAD`\]  
  * internal: true  
  * class: `dev_harness`  
  * env\_gate: `{"APP_ENV":"dev"}`  
  * a7\_eligible: true  
  * For the current closure scope, this route is the governed Reader success-proof surface.  
  * Endpoint Catalog audit classification: if `/reader` is cataloged as `class: dev_harness` or `classification:"dev_harness"` with `env_gate` constrained to `APP_ENV=dev`, that state is dev-gated proof/catalog posture only and MUST NOT be treated as production public Reader enablement.  
  * Production public Reader enablement requires a separate explicit contract/runtime state change.  
  * Public Reader output and internal/admin compatibility output are distinct proof classes. Do not treat `/api/compat/v1` proof as public `/reader` proof, and do not treat `/reader` proof-surface status as internal/admin compat enablement.  
  * This note creates no new public route, no new token, and no new flag.  
  * The governed machine-readable inventory for this surface remains `docs/ENDPOINTS_CATALOG.json`; do not create a second inventory or designation carrier.  
  * This designation does not authorize a new route, a new flag, a new proof-surface carrier, or any writer-surface widening.  
* **Dev sampler conjunction (dev-only):** `/dev/sampler/conjunction`  
  * path: `/dev/sampler/conjunction`  
  * allowed\_methods: \[`GET`\]  
  * internal: true  
  * class: `dev_harness`  
  * env\_gate: `{"APP_ENV":["dev","test","local"]}`  
  * a7\_eligible: false  
* **Internal dev sampler harness (dev-only):** `/internal/dev/sampler`  
  * `path: /internal/dev/sampler`  
  * `allowed_methods: [POST]`  
  * `internal: true`  
  * `class: dev_harness`  
  * `env_gate: {"APP_ENV":["dev","test","local"]}`  
  * `a7_eligible: false`  
  * `GET /internal/dev/sampler MUST remain invalid and return 405.`  
  * `Success output remains internal/dev evidence only: canonical JSON, IDs-only plus seed metadata, and two-run identity proof. This entry does not create a public route, public contract, Reader payload change, or A7 proof surface.`  
* **Dev reader conjunction (dev-only):** `/dev/reader/conjunction`  
  * path: `/dev/reader/conjunction`  
  * allowed\_methods: \[`GET`\]  
  * internal: true  
  * class: `dev_harness`  
  * env\_gate: `{"APP_ENV":["dev","test","local"]}`  
  * a7\_eligible: false  
* **`Dev writer conjunction (dev-only):`** `/dev/writer/conjunction`  
  * Any governed writer-evidence run that exercises `GET /dev/writer/conjunction` MUST require explicit caller-provided open rails and MUST NOT silently force `SAFE_MODE=0` or `ALLOW_NETWORK=1` on behalf of the caller.  
  * Such writer-evidence runs do not widen the route contract and do not move this endpoint into the A7 proof family.  
  * **Output canon (normative).**  
    * Any success payload emitted by these routes MUST be serialized by the canonical public emitter, producing deterministic JSON bytes with ASCII-sorted keys and exactly one trailing LF.  
    * AB↔BA parity MUST hold for conjunction evaluation: swapping A and B MUST NOT change emitted bytes after canonical emission.  
  * Endpoints (dev-only).  
    * GET /dev/sampler/conjunction  
      * Dev-only conjunction preview route for sampler evaluation.  
    * GET /dev/reader/conjunction  
      * Dev-only conjunction preview route for Reader-style response emission and VendorError mapping.  
    * GET /dev/writer/conjunction  
      * Dev-only conjunction preview route returning an idempotent writer-style envelope (not the public Reader v1 envelope).  
      * The Endpoint Catalog route id for this endpoint is `dev.writer.conjunction.v1`.  
* **Compat v1 (internal admin, dev-only):** `/api/compat/v1`  
  * path: `/api/compat/v1`  
  * allowed\_methods: \[`POST`\]  
  * internal: true  
  * class: `internal_admin`  
  * env\_gate: non-empty (must gate out production)  
  * a7\_eligible: false  
* Compat evidence proof posture (internal/admin only).  
  * EPIC030 compat evidence and indexing MAY reuse the existing compat families for `/api/compat/v1` and `hdctl showcompat`.  
  * Compat evidence MUST NOT create a new route, public surface, Reader payload redesign, public contract, public flag, public serializer path, or second public threshold home.  
  * Compat parity proof MUST compare emitted canonical bytes. Parsed-object equality alone is insufficient because it can hide byte drift.  
  * Compat identity proof MUST bind the current AB and BA emitted bytes to the claimed identity hash. Regex-only, stale, or previous-artifact-drift-only evidence is insufficient.  
  * Band-threshold and tuning evidence MAY bind internal/admin compat threshold sources, compact diffs, and identity-hash artifacts as proof for compat/admin JSON. This does not authorize public Reader scores, public Reader threshold bytes, public category expansion, or public numeric output.  
  * Category-order and category-framework proof MAY bind Magic-10 order, per-channel mechanics, canonical compare, Human Index binding, Machine Mirror binding, and narrative key-table linkage as internal/admin evidence. This does not authorize public category-order expansion or public Reader numeric output.  
  * Top-level PASS claims for governed compat evidence MUST derive from the decisive predicates for that evidence family, including current AB↔BA identity where claimed and canonical-compare status where claimed. Stale artifacts produced before final generator logic are insufficient.

### **Evidence artifacts**

* `artifacts/reader/endpoints_snapshot.json` — machine snapshot of catalog entries used during the proof run.  
* `artifacts/proofs/endpoints_env_gate_proof.log` — A7 proof that env-gated endpoints are not accessible in `APP_ENV=prod`.  
* *(Optional, informative)* `docs/ENDPOINTS_CATALOG.json` — governed Endpoint Catalog; internal proof anchor (checksum and path-proof sidecars listed in Appendix D).  
* *(Optional, informative)* `docs/ENDPOINTS_CATALOG.json.sha256` — checksum sidecar; MUST reference `docs/ENDPOINTS_CATALOG.json` for `sha256sum -c` verification from the repository root.

### **Acceptance tokens**

The token roster lives in **HDE-Governance §2.0**. PF05 asserts the following acceptance claims (title-only):

* `ENDPOINTS_CATALOG_OK` — Catalog exists and is non-empty for the Epic’s proof surfaces.

* `ENDPOINTS_CATALOG_POST_ONLY_OK` — POST-only internal routes are declared as POST-only (no implicit GET surface).

* `ENDPOINTS_CATALOG_INTERNAL_OK` — internal routes are marked internal and not treated as client contract.

* `ENDPOINTS_CATALOG_ENV_GATE_OK` — env gate fields are present and prevent production exposure.

* `A7_TRANSPORT_PROOF_OK` — all cataloged `a7_eligible` routes satisfy §5.3 invariants.

  ### **Routing**

* Token names live in `HDE-Governance §2.0`.

* Transport validators live in §5.3 and Appendix A.

* Evidence artifacts and snapshots are listed in **Appendix D: Evidence Index**.

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
3. 3\. **Determinism:** AB↔BA and two-run identity hold for identical inputs/env; outputs are stable under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

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

  ## **5.12 Dev conjunction endpoints \[Implemented (dev-only)\]**

* **Purpose.** Provide dev-only HTTP routes for conjunction preview and harness evaluation without coupling to the internal sampler harness.  
* **Environment gating (normative).**  
  * These routes MUST be gated by `APP_ENV` in `{dev, test, local}` and MUST NOT be available in production.  
  * If env-gating fails, requests to these routes MUST be forbidden using the Writer-style error envelope in §5.2 with `code: "ERR_WRITER_FORBIDDEN"` (not a raw HTTP 403 payload).  
  * These routes are not eligible for A7 proof selection; they MUST be registered with `a7_eligible=false` in the Endpoint Catalog.  
* **Input contract (normative).**  
  * Inputs are supplied as query-string keys in the `a_*` and `b_*` namespace.  
  * At minimum, `a_id` and `b_id` MUST be accepted as pair identifiers.  
  * Request validation MUST fail closed for missing or malformed required identifiers, and MUST use canonical typed error mapping (no ad-hoc string errors).  
* Resolver acquisition and SAFE rails posture (normative).  
  * Provider acquisition MUST be performed through resolver acquisition (not raw cache reads), so cache hits are normalized into a resolved shape and resolved detection remains correct even when a cached record is vendor-shaped.  
  * SAFE rails posture is closed by default. When an explicit environment configuration enables open-rails acquisition, acquisition MAY open rails only long enough to acquire missing data and MUST close back before compute and emission.  
  * Any governed writer-evidence run that exercises `GET /dev/writer/conjunction` MUST require explicit caller-provided open rails and MUST NOT silently force `SAFE_MODE=0` or `ALLOW_NETWORK=1` on behalf of the caller.  
  * Such writer-evidence runs do not widen the route contract and do not move this endpoint into the A7 proof family.  
* Output canon (normative).  
  * Any success payload emitted by these routes MUST be serialized by the canonical public emitter, producing deterministic JSON bytes with ASCII-sorted keys and exactly one trailing LF.  
  * AB↔BA parity MUST hold for conjunction evaluation: swapping A and B MUST NOT change emitted bytes after canonical emission.  
  * `GET /dev/writer/conjunction` MUST emit typed, numeric-free writer-style success and error envelopes.  
  * The success envelope type MUST be `dev.writer.conjunction.success.v1`.  
  * The error envelope type MUST be `dev.writer.conjunction.error.v1`.  
  * Writer-style success and error outcomes on `GET /dev/writer/conjunction` MUST remain `Cache-Control: no-store`, MUST NOT emit `ETag`, and MUST be treated as non-conditional.  
* Endpoints (dev-only).  
  * GET /dev/sampler/conjunction  
    * Dev-only conjunction preview route for sampler evaluation.  
  * GET /dev/reader/conjunction  
    * Dev-only conjunction preview route for Reader-style response emission and VendorError mapping.  
  * GET /dev/writer/conjunction  
    * Dev-only conjunction preview route returning an idempotent writer-style envelope (not the public Reader v1 envelope).  
    * The Endpoint Catalog route id for this endpoint is `dev.writer.conjunction.v1`.  
    * The `/dev/*/conjunction` family notation is bounded to the currently canonized conjunction-family surfaces listed in this subsection.  
    * It does **not** create a reusable wildcard or standing rule that any future dev route matched by a `/dev/*/` pattern is automatically valid, dev-harness, or outside the formal proof family.  
    * Any future non-conjunction dev route requires explicit canon classification before it is treated as valid, dev-harness, or outside the formal proof family.

  ---

# 6\. Serializer Canon & Single Emitter \[Required-Now\]

## 6.1 Canonical JSON (UTF-8, sorted keys, compact, one LF) \[Implemented\]

* **Encoding & termination.** Emit UTF-8 JSON, BOM/ANSI-free, with **exactly one** trailing LF (`\n`).  
* **Ordering & separators.** Serialize with **sorted keys (ASCII lexicographic)** and **compact separators** (`,` and `:`; no spaces).  
* **Arrays-as-sets.** Any array that functions as a set **MUST** be deduplicated and ASCII-sorted by its identity rule (see **HDE-Schemas & Artifacts §4**).  
* **Locale determinism.** All canonicalization and byte comparisons run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**No pretty-print; no alternates.** Pretty/indented output and alternate serializers are **not permitted** on public paths. Grep-guards **MUST** block ad-hoc `json.dumps(...)` or any non-presenter emitter.

**Validation (binary)**

* **Canonical compare:** re-serialize with the rules above and byte-compare against the produced bytes (**must match exactly**).  
* **LF/encoding check:** UTF-8 only, no BOM/ANSI, **exactly one LF** at end of file.

**Routing (titles-only).** Canonical JSON rules are owned by **HDE-Schemas & Artifacts (§4)**. Governance tokens for these checks live in **HDE-Governance (§2.0 Acceptance Tokens)**.

## **6.2 Unify entrypoint (single presenter/emitter) Required−NowRequired-NowRequired−Now**

* **One entrypoint for public bytes.** All public JSON bytes MUST be emitted by the byte-authoritative presenter/emitter entrypoint (both success and typed errors). Reader and CLI MAY call wrapper envelope builders, but wrappers MUST delegate byte emission to the byte-authoritative entrypoint and MUST NOT serialize public bytes outside it.

* **Forbid ad-hoc serialization.** Any `json.dumps` / `jsonify` / template rendering on public paths is disallowed. No alternate serializers.

* **Symbol allow-list (single source).** The byte-authoritative entrypoint is pinned in code and CI allow-lists (owned in code/CI; titles-only here). Wrapper envelope builder symbols may be allow-listed only when they delegate byte emission to the byte-authoritative entrypoint and do not introduce alternate serialization.

* **CI grep-guard.** In CI, grep-guard must fail on any forbidden serializer usage or emitter drift (see §3.5, §6.3).

* **Test parity (symbol-level).** Tests MUST prove that CLI and Reader call only allow-listed emission symbols for public bytes, and that any wrapper envelope builders delegate byte emission to the byte-authoritative entrypoint (import-graph or reflection proof).

* **Canonicalization coupling.** The byte-authoritative entrypoint MUST enforce canonical JSON (sorted keys, compact separators, stable newline) and shared error tokenization rules for both Reader and CLI.

* **Determinism & parity.** A single byte-authoritative emitter ensures Reader↔CLI **byte equality**, **AB↔BA parity**, and **two-run identity** for identical inputs and environment.

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
* **Canonicalize & hash (one emitter, one recipe).** Serialize the five-key object with the **single presenter/emitter** and **canonical JSON rules** (§6.1: UTF-8 no BOM, sorted keys, compact, exactly one LF; arrays-as-sets deduped & ASCII-sorted; run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`) to obtain `preimage_bytes`. Compute `idempotence_hash = sha256(preimage_bytes)` as lowercase 64-hex.

* **Finalize.** Add the computed `idempotence_hash` to the object (becoming the **sixth top-level key**) and **re-serialize** with the same emitter to produce the public bytes (LF-terminated).

* **Parity & determinism.** The `preimage_bytes` and final public bytes produced by Reader and CLI **MUST** be **byte-identical** for identical inputs/environment. Preimage and final bytes **MUST** also be identical for **AB vs BA** normalized inputs, and across **two runs** with the same inputs.

**Validation gates (binary)**

1. **Recheck:** Remove `idempotence_hash`, re-serialize the five-key preimage canonically, and verify `sha256(preimage_bytes) == published idempotence_hash` for Reader and CLI.  
2. **Pattern checks:** `idempotence_hash` and `release_id` each match `^[0-9a-f]{64}$`.  
3. **AB↔BA:** Preimage and final bytes for `(A,B)` vs `(B,A)` are **byte-identical**.  
4. **Two-run identity:** Two serializations over the same inputs produce **byte-identical** preimage and final bytes.  
5. **Emitter proof:** Tests/reflection show both surfaces delegate byte emission to the byte-authoritative entrypoint (see §6.2).

**Evidence (titles/paths only)**

* **Parity harness outputs** for Reader vs CLI and AB vs BA (see **PF12 Appendix C**).  
* **Recompute logs/scripts** for `idempotence_hash`.  
* **Indexing in PF12:** update human `docs/evidence/INDEX.json` \+ hash sentinel and the machine `artifacts/evidence_index.jsonl` in the **same PR** as artifacts.

**Routing (titles-only).** Canonical JSON rules: **HDE-Schemas & Artifacts (§4)**. Governance tokens: **HDE-Governance (§2.0 Acceptance Tokens)**.

---

# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**

## **7.1 Rails & Environment \[Required-Now\]**

### **7.1.1 Rails defaults (env inventory; titles-only)**

* **Dev / Codex and QA / Codespaces:** rails **CLOSED** in the current deployed records unless explicitly opened for a bounded, PO-authorized task.

  * `SAFE_MODE = 1`

  * `ALLOW_NETWORK = 0`

* **Prod / Railway:** rails **OPEN** only where the deployed environment inventory records the explicit PO-owned production binding.

  * `SAFE_MODE = 0`

  * `ALLOW_NETWORK = 1`  
* **CI:** rails **CLOSED** by default.  
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

* `HD_API_BASE_URL`  
* `HD_API_KEY`  
* `GEO_API_KEY` (when needed)

`HDAPI_BASE_URL` is deprecated legacy spelling. PF05 may mention it only as an observed drift key or temporary compatibility alias during migration. Resolution MUST be canonical-first: read `HD_API_BASE_URL`; if absent, a compatibility implementation MAY read `HDAPI_BASE_URL`; if both exist with different values, fail closed with a typed configuration ambiguity.

Missing or empty env values **MUST** produce a typed failure **without** I/O.

### **7.1.5 Determinism and shaping (closed rails)**

* With rails closed:

  * Providers **may shape** the request (URL, headers, body schema) **deterministically**:

    * Order-neutral.

    * No time/locale/random dependence.

  * Providers **must not send** the request; the output is the typed refusal.

* All checks run under:

  * `LC_ALL = C`  
  * `LANG = C`  
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

#### 7.1.8a OPS discovery, open-rails testing, and repo-reality observations (vendor ingest)

PF05 vendor work MUST NOT be deferred merely because a vendor route, auth header, credential binding, config key, base URL posture, endpoint-family availability, account or tier posture, request shape, response shape, error envelope, rate-limit behavior, or open-rails precondition is unknown.

If the missing fact is safely discoverable, the work MUST route through a bounded OPS discovery task or bounded OPS open-rails task instead of guessing, silently deferring, or treating the unknown as out of scope. OPS discovery and open-rails execution remain PO-only, IA-guided, secret-safe, and evidence-recorded. Automated agents MUST NOT perform live external vendor actions, expose secret values, simulate external state changes, or claim OPS completion.

Open-rails testing is allowed when it is necessary to prove or discover live vendor reachability, endpoint availability, auth posture, credential-binding correctness, base URL posture, request/response compatibility, account or tier behavior, rate-limit or retry behavior, error-envelope behavior, or integration viability. A bounded live vendor smoke proves only the narrow interaction it was designed to prove. It MUST NOT be treated as full HumanDesignAPI runtime conformance, public Reader expansion, public payload expansion, new route creation, or acceptance-token satisfaction unless the owning governance source explicitly supports that stronger claim.

Codex Audit or other supplied read-only repo-reality observations may support PF05 planning-time claims about existing vendor seams, route helpers, adapter loci, CLI loci, evidence tools, tests, or artifact families. Such observations do not create canon, do not prove live vendor truth, do not satisfy acceptance tokens, do not prove QA PASS, do not complete OPS work, and do not move PF09 status by themselves.

### **7.1.9 Routing (titles-only)**

* Env inventory: **Glow-Infrastructure**.

* Transport matrices and refusal/error policy: **HDE-Governance**.

* Evidence index and mirror: **HDE-Schemas & Artifacts**.

---

### **7.1.10 Endpoint policy (legacy BodyGraph vendor HTTP; HumanDesignAPI v2 pending)**

**Current legacy BodyGraph endpoint posture:**

The current implemented vendor-ingest contract remains legacy BodyGraph-oriented and MUST NOT be cited as HumanDesignAPI v2 conformance.

The current legacy request-shaping block uses:

POST /bodygraphs

with the three-key JSON body:

{"birthdate":"...","birthtime":"...","location":"..."}

**HumanDesignAPI v2 endpoint posture pending:**

HumanDesignAPI v2 conformance is pending governed contract inventory and implementation evidence. The pending v2 route map MUST distinguish at least these recommended v2 chart routes:

* `POST /v2/charts`  
* `POST /v2/charts/simple`  
* `POST /v2/charts/coordinates`

PF05 MUST NOT collapse those v2 routes into the legacy BodyGraph endpoint, and MUST NOT claim v2 runtime conformance until HDE-FERM006 through HDE-FERM008 close with governed evidence.

**Legacy v1 isolation pending:**

The pending contract inventory MUST distinguish legacy v1 routes, including:

* `POST /v1/bodygraphs`  
* `POST /v1/bodygraphs/simple`

Whether v1 BodyGraph routes remain supported as explicit legacy fallback or are retired after v2 migration is a PO decision. Until that decision is drained, v1 behavior MUST be labeled legacy or pending and MUST NOT be silently deleted, silently promoted, or treated as the recommended v2 path.

**Privacy / payload constraints:**

* Vendor HTTP MUST NOT receive internal user ids or other internal identifiers.  
* Public Reader output remains bands-only and numeric-free.  
* This pending v2 endpoint posture creates no new public Reader route and no public Reader contract change.

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

### **7.2.0 HumanDesignAPI v2 request and response contract pending**

HumanDesignAPI v2 full live/runtime conformance remains pending. Current governed evidence records source-selection, deterministic request-shaping proof, proof-level response-envelope mapping, adapter/presenter boundary proof, closed-rails refusal, and a bounded OPS-02 open-rails smoke for `charts/coordinates` bound by PR-06 for HDE-FERM008.2 only. These proof slices do not claim full HumanDesignAPI v2 runtime conformance, normalized data-path completion, HDE-FERM008 parent completion, HDE-FERM008.3/.4/.5 completion, public Reader changes, public route or payload changes, new HTTP homes, or AI scope.

Pending v2 contract work MUST follow this source precedence:

* validated `v2-routes.yaml` and `v1-routes.yaml` first,  
* rendered endpoint pages second,  
* high-level guide pages third,  
* suspect artifacts quarantined until validated.

The advertised `api-reference/openapi.json` artifact MUST NOT define PF05 bytes unless validation proves it belongs to HumanDesignAPI by domain, title, server, and path-family.

The v2 request contract, when drained, MUST define:

* the byte-authoritative request contracts for `POST /v2/charts`, `POST /v2/charts/simple`, and `POST /v2/charts/coordinates`,  
* v2 auth headers, including `Authorization: Bearer` and `HD-Geocode-Key` conditions for location-based calls,  
* exact v2 base URL posture and credential/config key names,  
* request-body shape, including whether ISO-style birthdate values are required,  
* response envelope mapping for `timestamp`, `success`, `message`, `errorCode`, `type`, and `data`,  
* typed error mapping,  
* retry and rate-limit handling,  
* v1 legacy isolation or retirement posture.

PF05 pins `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key, `HD_API_KEY` as the canonical vendor credential key, and `GEO_API_KEY` as the geocoding key where required. `HDAPI_BASE_URL` is deprecated legacy spelling and may be supported only as a temporary compatibility alias when `HD_API_BASE_URL` is absent; conflicting values MUST fail closed as configuration ambiguity. The configured `HD_API_BASE_URL` owns the vendor API-version path and may include a vendor version segment without changing runtime route constants. PF05 MUST NOT restate current deployed base URL values as runtime-contract text; deployed values belong to infrastructure inventory and OPS evidence. Legacy BodyGraph resource paths under a configured v2 base remain live-behavior-unproven and MUST NOT be claimed as live vendor conformance from route-version remediation alone.

PF05 MUST preserve the distinction between v2 chart smoke, v2 full chart payload, legacy BodyGraph payload, response-envelope proof, and normalized HD Engine BodyGraph/person/cache contract. `ChartSimpleResult` MUST NOT be presumed sufficient for full BodyGraph detail. `ChartResult` and `ChartSimpleResult` MUST NOT be claimed to feed existing BodyGraph cache, person/bodygraph compute inputs, compatibility inputs, or legacy BodyGraph replacement until a bounded adapter/schema proof or implementation maps the vendor payload family into the existing internal contract. Recording an exact schema/adapter gap is valid evidence posture for a scoped gap-recording slice, but it is not future runtime compatibility proof.

No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider config key, AI credential, AI runtime rail, AI evidence family, or AI QA obligation is introduced by this v2 request and response contract work.

### **7.2.1 Endpoints, method, base URL**

* **Primary endpoint:** `POST /bodygraphs` (JSON).

  * This is the **only** vendor BodyGraph endpoint HDE uses. No alternate vendor endpoint is defined here; see §7.1.10 for the explicit statement that `POST /bodygraphs/simple` is unsupported for this engine.

* **Endpoint and resource-path posture.**

  * egacy v1 BodyGraph source documentation remains `POST /v1/bodygraphs` and `POST /v1/bodygraphs/simple`.  
  * Recommended v2 chart source documentation remains `POST /v2/charts`, `POST /v2/charts/simple`, and `POST /v2/charts/coordinates`.  
  * Runtime request construction MUST use version-neutral resource paths joined to the configured `HD_API_BASE_URL`. The governed resource paths are `bodygraphs`, `bodygraphs/simple`, `charts`, `charts/simple`, and `charts/coordinates`.  
  * Runtime request construction MUST preserve any API-version path already present in `HD_API_BASE_URL`; it MUST NOT hardcode active `/v1` or `/v2` route prefixes into runtime route constants.  
* **Base-URL resolution.**  
  * Resolve canonically from `HD_API_BASE_URL`.  
  * If `HD_API_BASE_URL` is absent, a temporary compatibility implementation MAY read deprecated `HDAPI_BASE_URL`.  
  * If both keys exist and values differ, fail closed with a typed configuration ambiguity.  
  * If no usable base URL exists, fail closed with a typed error before I/O; do not default to any literal URL.  
* **Method rules.**

  * `POST` is normative for JSON BodyGraph requests.

  * `GET` **MUST NOT** carry a request body; if ever used, it is only for dev-harness health probes and not for BodyGraph computation.

### **7.2.2 Canonical headers (dash-case, exact on wire)**

Send these verbatim on wire. Do not add other headers unless explicitly pinned.

* `Accept: application/json`  
* `Content-Type: application/json; charset=utf-8`  
* `Legacy v1 BodyGraph routes: HD-Api-Key: <secret>`  
* `HumanDesignAPI v2 chart routes: Authorization: Bearer <secret>`  
* `Routes requiring geocoding: HD-Geocode-Key: <secret>`  
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

* **Locale-neutral.** No locale or formatting beyond the pinned rules. Strings are ASCII/UTF-8 as stated. Jobs run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

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

4. 4\. Determinism. Shaping output is identical for AB vs BA. No locale, time, or random dependence. Checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

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

Rails open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); env ready (`HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when needed); shaping fixed per §7.2. Deprecated `HDAPI_BASE_URL` may be used only as an explicitly labeled temporary compatibility alias when `HD_API_BASE_URL` is absent; conflicting values fail closed.

### **7.3.2 Timeouts (closed integers)**

Domains (ms):

* `connect_timeout_ms ∈ {1000,2000,5000}`

* `read_timeout_ms ∈ {2000,5000,10000}`

* `total_timeout_ms ∈ {5000,10000,15000,30000}`

One `timeout_profile ∈ {small, default, long}` pins the triple.

### **7.3.3 Retries, status classification, and redirects (deterministic classes)**

`max_attempts ∈ {0,1,2,3}` (includes the initial try).

Retryable classes are exactly `{network_error, 5xx}`.

Do not retry `429`, other `4xx`, `3xx`, or other non-200 statuses outside `4xx` and `5xx`.

Non-200 HTTP statuses outside `4xx` and `5xx` MUST be classified as `http_status_other`, mapped to typed error code `PROVIDER_ERROR`, and emitted with `retried:false` in governed proof artifacts when that fact is captured.

The default vendor request path MUST NOT follow redirects. If the provider returns a redirect status such as `302` with a `Location` header, PF05 requires the original status, response body, and response headers to be surfaced for classification rather than following the redirect.

HTTP error responses captured by the default request path MUST be converted into status, body, and header tuples before classification. This allows the same typed mapping rules to apply to injected and default request paths.

### **7.3.4 Backoff policy (deterministic; no jitter)**

`backoff ∈ {none, fixed, exponential}` with closed integer params.

Schedule respects `total_timeout_ms`; no random jitter.

### **7.3.5 Rate limits & Retry-After (429)**

Map **429** to a typed `PROVIDER_RATE_LIMITED` error.

If `Retry-After` parses, surface `retry_after_ms` as an integer greater than or equal to 0; otherwise omit it.

EPIC011 does not auto-recover on 429; any success-path retry belongs to a later epic.

### **7.3.6 Observability (keys-only)**

Vendor SAFE-rails observability MUST be keys-only, bounded, and secret-safe.

Vendor logs and persisted vendor log samples MUST NOT contain request bodies, response bodies, plaintext secrets, raw secret header values, vendor payload bytes, unbounded labels, or user identifiers.

Allowed vendor observability is limited to bounded keys and labels such as route class, rails state, timeout profile, retry/backoff profile, outcome class, status class, and deterministic success or failure class.

Failure classes for governed vendor-log proof MAY include `429`, `4xx`, `5xx`, and `network_error`; other non-200 status handling is classified separately as `http_status_other` when captured by the provider-gate proof.

Log timestamps or ordering markers used for deterministic proof MUST be controlled so they do not create nondeterministic public or acceptance bytes.

PR-specific vendor log samples MUST remain under the PR-specific governed audit path when a shared artifact family would otherwise be overwritten.

### **7.3.7 Failure posture (typed, numeric-free)**

Refusal on closed rails requires no I/O; deterministic mapping follows §7.2.

* timeouts/exhaustion → `PROVIDER_UNAVAILABLE`  
* malformed vendor JSON → `PROVIDER_BAD_RESPONSE`  
* non-200 statuses outside `4xx` and `5xx` → `PROVIDER_ERROR` with internal class `http_status_other`

### **7.3.8 Acceptance to flip rails**

Pin a concrete policy (from the domains above); prove refusal on closed rails; prove conformance on open rails; maintain CLI↔Reader parity; update indices in the same PR.

Acceptance impact.  
 Moves 429 out of retryable set for EPIC011; no token additions (PF04 owns tokens).

### **7.3.9 HumanDesignAPI v2 live conformance pending**

HumanDesignAPI v2 full live/runtime conformance remains pending. HDE-EPIC035 evidence records provider-outcome and rate-limit mapping for HDE-FERM008.3, exact response-normalization schema/adapter gap posture for HDE-FERM008.4, retained OPS-01 live-vendor observations, and PR-03 governed evidence-loop binding for HDE-FERM008.5. HDE-EPIC036 evidence records explicit `bg:resolve --source vendor` route-policy classification and evidence-loop binding for HDE-FERM008.6: configured v2 bases select `unsupported_runtime_nonclaim`, no legacy `bodygraphs` request is built for configured v2 bases, non-v2 bases preserve explicit legacy fallback, and HDE-FERM008.6 is supportable for later PF09 status drainage from repo evidence. These proof slices do not claim HDE-FERM008 parent completion, PF09 status movement, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader changes, public route or payload changes, new HTTP homes, app-side vendor credential ownership, raw payload persistence, or AI scope.

Closed-rails v2 proof MUST show deterministic refusal with no DNS, socket, HTTP, or other external I/O. Any JSON emitted for refusal MUST be canonical, numeric-free where public, LF-terminated, and secret-free.

Open-rails v2 smoke, when required, is an OPS or QA action according to the approved plan and must remain PO-authorized, secret-safe, bounded, and stored under governed evidence when promoted as proof. PF05-owned CLI and vendor-ingest surfaces are production-relevant surfaces. Any epic that alters, proves, routes, classifies, or constrains CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor transport, vendor route policy, HumanDesignAPI request shaping, HumanDesignAPI auth/header behavior, BodyGraph vendor ingest, vendor response normalization, vendor error/retry/rate-limit behavior, provider transport behavior, configured base URL behavior, or environment-key binding behavior MUST include at least one bounded open-rails QA step unless an explicit PO-authorized or controlling-canon exemption is recorded before QA approval. Closed-rails refusal proof remains valuable but is not sufficient by itself for these affected open-rails runtime surfaces. The open-rails evidence MUST distinguish actual exercised route behavior from inferred route behavior and MUST preserve nonclaims for any route, payload, environment, production deployment, BodyGraph-detail sufficiency, or full runtime-conformance behavior not exercised.

The v2 live-conformance evidence family MUST cover, as applicable:

* rate-limit posture,  
* `Retry-After` handling,  
* v2 typed error mapping,  
* malformed-response handling,  
* response normalization,  
* v1 legacy guard behavior,  
* evidence-index coherence.

No vendor-v2-specific acceptance token may be claimed unless HDE-Governance registers it or Build Notes mints it pending drainage. Existing PF05 vendor error, refusal, canonical JSON, rails, and evidence-index tokens remain titles-only references.

The open-rails path is HumanDesignAPI-only. It MUST NOT include OpenAI, LLM, AI-agent, chatbot, prompt, embedding, model-call, or other AI-provider calls.

---

## **7.4 Adapter data-source policy (PF10-AA) \[Required-Now\]**

**Purpose.** Pin where the adapter reads BodyGraph data in each environment without changing public transport bytes.

**Glow app integration boundary.** HumanDesignAPI request shaping, vendor auth/header behavior, vendor evidence posture, BodyGraph persistence/retrieval, and HD computation remain HD Engine responsibilities. The Glow app is the product shell and consumer of HD Engine outputs. PF05 MUST NOT authorize duplicate vendor-client implementation in the Glow app, direct app-to-vendor request shaping, app-layer vendor secret handling, or bypass of the HD Engine vendor seam without a future ADR and canon update.

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

# **8\. Error Model & Exit Codes \[Required-Now\]**

## 8.1 Typed public error object (numeric-free) \[Required−Now\]

**Primary home:** §5.2 “Errors” (tagged **Required−NowRequired-NowRequired−Now**). This section is a short cross-surface summary; if any drift occurs, §5.2 wins.

**Shape (minimum).** HTTP typed errors use the **error\_v1** envelope, serialized by the single emitter (UTF-8, sorted keys, compact, one LF):

`{"schema":"v1","ok":false,"code":"<ERR_*>","error":"<non-PII message>"}`

* `schema:"v1"` (string, required)

* `ok:false` (boolean, required)

* `code` (canonical `ERR_*` token, UPPER\_SNAKE; closed vocabulary; legacy lowercase aliases may be accepted as internal inputs but are not emitted)

* `error` (human-readable, non-PII, non-secret)

Optional fields are schema-owned and must remain numeric-free (for example `retry_after_ms` integer ≥ 0 when transport policy explicitly permits it, and optional `details` object when permitted by the error\_v1 schema).

**CLI note.** CLI typed failures do **not** emit `error_v1` on stderr. CLI failures emit a single LF-terminated code string token; when the same failure maps to an HTTP surface, that token MUST equal the HTTP `error_v1.code` value for the same condition.

**No other fields.** HTTP error envelopes must not echo payloads, secrets, stack traces, or vendor bodies. Always LF-terminate canonical public JSON with exactly one trailing `\n`.

**Routing (titles-only).** Schema constraints live in **HDE-Schemas & Artifacts**. Token naming/semantics live in **HDE-Governance**.

## **8.2 Streams discipline \[Required−Now\]**

**Primary home:** §3.3 “Streams discipline (stdout / stderr)” (tagged Required-Now). This section is a cross-surface summary.

* **Success (exit 0\) → stdout.** Print the command’s canonical success payload (LF-terminated) to `stdout`; `stderr` empty.

  * For Reader success surfaces, the success payload is the Reader v1 body (§5.1).

  * For `hdctl showcompat`, the success payload is compat JSON (§4.1). Reader v1 bytes, when needed for parity, are produced via the command’s reader-dump parity path (not by replacing stdout).

* **Usage (exit 64\) → stderr.** Print a short synopsis to `stderr`; `stdout` empty.

* **Typed failures and internal failures (non-zero; command-specific) → stderr.** Print a single LF-terminated code string token to `stderr`; `stdout` empty. Where the same failure maps to an HTTP `error_v1`, the CLI token MUST equal the HTTP `error_v1.code` value. The exact non-usage failure exit code is pinned by the command contract (see §3.4 and the command section).

* **No mixed streams.** Never interleave diagnostics with public bytes.

## **8.3 Exit codes (taxonomy) \[Required−Now\]**

**Primary home:** §3.4 “Exit codes taxonomy Required−NowRequired-NowRequired−Now”. This section is a short summary.

* `0` — Success. Canonical success payload on stdout (LF-terminated); stderr empty.

* `64` — Usage/config/input error. Synopsis on stderr; stdout empty.

* Other non-zero exit codes — command-specific. The exact non-usage failure exit code(s) are pinned by the command contract (see §3.4 and the command section, for example §4.1.4 for `showcompat`). For all such failures, stderr contains a single LF-terminated code string token and stdout remains empty.

These codes are exhaustive for the CLI public surface in the sense that success is `0` and usage is `64`, while all other outcomes are non-zero failures that must follow the stderr-only, single-token discipline.

## **8.4 Determinism & hygiene gates \[Required−Now\]**

* Canonical emitter. Success stdout and HTTP `error_v1` bodies follow the single-emitter rules (UTF-8, sorted keys, compact, one LF).

* CLI stderr discipline. CLI stderr code strings and usage synopses are plain UTF-8 text, LF-terminated, and must not be wrapped in JSON envelopes.

* No ad-hoc dumps. Forbid `json.dumps` and alternate serializers on public paths.

* Idempotence posture. Typed errors are not part of the success preimage; success preimage/idempotence checks remain unchanged.

* Parity expectations. CLI error token serialization must be stable across runs (two-run identity) and deterministic across AB/BA inputs where applicable. When the same failure maps to an HTTP surface, the CLI token MUST equal the HTTP `error_v1.code` value for that failure.

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
* **Same-change evidence-family completeness (MUST).** When a PF05-scoped proof or gate run changes any governed artifact in an evidence family, refreshing only a subset of related companions is non-conforming. All changed primary artifacts, sibling `*.path_proof.txt` transcripts, and affected human-index and machine-mirror companion files for that family MUST be regenerated to current same-change chronology in the same run or change.  
* **Bounded evidence-family refresh (MUST).** When a PF05-scoped PR, remediation slice, or proof refresh is explicitly bounded to a named PF05 evidence family, governed updates MUST be limited to that family and to directly required shared index, mirror, topology, and sibling `*.path_proof.txt` companions. Unrelated governed artifact churn outside the approved family is non-conforming unless the changed artifact is directly required by the same proof flow.  
* **Canonical JSON gate dual-family closeout (MUST).** If both `audit/gates/json_gate/canonical/` and `audit/gates/canonical_json/` are still produced by the same generation flow, closeout MUST refresh both families and their sibling `*.path_proof.txt` transcripts in the same run. Refreshing only one family is insufficient, and closure claims MUST use whole-family same-change validation rather than subset freshness.  
* **Index (human).** **`docs/evidence/INDEX.json`** (PF12 §8.6) lists artifacts and scripts (**titles/paths only; no payload bytes**). A **hash sentinel** **`docs/evidence/INDEX.sha256`** gates merges and is **not mirrored**.  
* **Machine mirror (single home).** The records-only JSONL mirror lives at **`artifacts/evidence_index.jsonl`** (PF12 §8.3). Human↔machine entries **must be 1:1**; a non one-to-one join is a failure. Each mirror record includes `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` (transcript reference plus on-disk stat). The mirror is **ASCII field-ordered** and **sort-before-write** with **unknown-key rejection**; a **single** mirror file is permitted.  
* **Repo docs tokens (PR checklist).** Include `EVIDENCE_INDEX_UPDATED_OK`, **`EVIDENCE_INDEX_HASH_OK`**, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Repo docs tokens (PR checklist).** Include `EVIDENCE_INDEX_UPDATED_OK`, **`EVIDENCE_INDEX_HASH_OK`**, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, and `CI_CHECK_FINAL_LF_OK`.  
* **Close-pack execution truthfulness (MUST).** If a PF05-scoped acceptance map, token-evidence matrix, close report, or manifest claims Human Index refresh, hash-sentinel refresh, machine-mirror refresh, mirror-schema validation, LF validation, orientation-demo refresh, acceptance-map viability generation, or related evidence-workflow execution, that claim MUST be backed by same-run governed QA log anchors under `audit/qa/<epic-id>/checks/<check-id>/`.  
* **Epic-close runtime proof sufficiency (MUST).** A PF05-scoped epic-close recommendation MUST NOT rely on artifact-only close-pack files. When changed PF05 runtime surfaces are part of the close recommendation, same-run governed QA proof MUST show that prerequisite runtime logs are present and that the changed runtime proof families actually executed in that run.

* **Runtime-proof synthesis deliverables (MUST).** The governed synthesis step MUST capture `runtime_log_presence.txt`, `runtime_surface_inventory.txt`, and the corresponding `primary.log` under `audit/qa/<epic-id>/checks/<check-id>/`.  
* **Update discipline (MUST).** When any golden, artifact, or script path changes, update **`docs/evidence/INDEX.json`**, **`docs/evidence/INDEX.sha256`**, and **`artifacts/evidence_index.jsonl`** in the **same commit/PR**, and add a matching entry in **§11 Change Management: Doc-Delta Hooks**.  
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
* The **human↔machine join is exactly 1:1** (no extras/misses); CI enforces join parity and path proofs under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Sentinel** is recomputed when the human Index changed and is noted in the Change Log entry.  
* Freeze-pack changes (if any) produce a new `release_id` and are logged.

Otherwise, it is **Rejected** (no partial merges).

### **11.2.3 Guardrails (do not regress)**

* **Single emitter.** Reader and CLI must produce public bytes via the same presenter emitter; forbid ad-hoc `json.dumps`.  
* **Numeric-free public.** Reader v1 success remains `{id, band}` only; no numerics on the public surface.  
* **No duplicated bytes.** Architecture/Math are referenced by title only; transport and vendor bytes live here.  
* **Determinism first.** Never introduce jitter or locale/time dependencies; AB↔BA and two-run identity remain required. CI byte comparisons run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`; JSON is UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF.  
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

**HumanDesignAPI v2 conformance note.** The example below is the current legacy BodyGraph-oriented request example. It is not a HumanDesignAPI v2 request example and MUST NOT be cited as proof that PF05 is v2-conformant. HumanDesignAPI v2 request examples, including route selection, auth headers, birthdate format, geocode-key conditions, response envelope mapping, and typed errors, remain pending until derived from the governed contract inventory and drained through the PF05 v2 contract update.

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

  #### **D.0b EPIC027 acceptance ledgers and close-pack**

* `docs/acceptance_map_epic027.json`

* `docs/acceptance_map_epic027.json.path_proof.txt`

* `audit/qa/hde-epic027/token_evidence_matrix.md`

* `audit/qa/hde-epic027/token_evidence_matrix.md.path_proof.txt`

* `audit/qa/hde-epic027/acceptance_map_viability.log`

* `audit/EPIC-027_close_report.md`

* `audit/EPIC-027_MANIFEST.json`

* `audit/EPIC-027_close_report.md.path_proof.txt`

* `audit/EPIC-027_MANIFEST.json.path_proof.txt`

  #### **D.0c EPIC027 close-pack same-run QA gate logs**

* `audit/qa/hde-epic027/checks/gate_update_evidence_index_write/primary.log`

* `audit/qa/hde-epic027/checks/gate_update_evidence_index_check/primary.log`

* `audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log`

* `audit/qa/hde-epic027/checks/gate_evidence_paths_validation/primary.log`

* `audit/qa/hde-epic027/checks/gate_lf_endings/primary.log`

* `audit/qa/hde-epic027/checks/gate_orientation_demo_write/primary.log`

* `audit/qa/hde-epic027/checks/gate_orientation_demo_check/primary.log`

#### **D.0d EPIC028 acceptance ledgers**

* `docs/acceptance_map_epic028.json`  
* `audit/qa/hde-epic028/token_evidence_matrix.md`  
* `audit/qa/hde-epic028/acceptance_map_viability.log`

#### **D.0e EPIC028 formal close-pack baseline**

* `audit/EPIC-028_close_report.md`  
* `audit/EPIC-028_MANIFEST.json`  
* `audit/EPIC-028_close_report.md.path_proof.txt`  
* `audit/EPIC-028_MANIFEST.json.path_proof.txt`

#### **D.0f EPIC028 Codespaces venue provenance**

* `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md`  
* `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md.path_proof.txt`

#### **D.0g EPIC029 acceptance ledgers**

* `docs/acceptance_map_epic029.json` *(acceptance-map ledger binding `HDE-CONJ009.1` and `HDE-CONJ008.1` as supportable from repo evidence for later drain to Done at epic close)*  
* `docs/acceptance_map_epic029.json.path_proof.txt` *(governed path-proof for the EPIC029 acceptance map)*  
* `audit/qa/hde-epic029/token_evidence_matrix.md` *(token-to-evidence ledger supporting the EPIC029 closeout bindings for the controlling Conjunction rows)*  
* `audit/qa/hde-epic029/token_evidence_matrix.md.path_proof.txt` *(governed path-proof for the EPIC029 token-to-evidence ledger)*  
* `audit/qa/hde-epic029/acceptance_map_viability.log` *(viability log for the EPIC029 acceptance bindings used by the closeout review)*  
* `audit/qa/hde-epic029/acceptance_map_viability.log.path_proof.txt` *(governed path-proof for the EPIC029 acceptance-map viability log)*  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json` *(qa-step log ledger confirming governed step coverage for the EPIC029 closeout review)*  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the EPIC029 qa-step log ledger)*

#### **D.0h EPIC029 formal close-pack baseline**

* `audit/EPIC-029_close_report.md` *(formal EPIC029 close report binding `HDE-CONJ009.1` and `HDE-CONJ008.1` as supportable from repo evidence for Done at epic close)*  
* `audit/EPIC-029_MANIFEST.json` *(formal EPIC029 close manifest binding the close-pack outputs and the later-drain actions for those controlling Conjunction rows)*  
* `audit/EPIC-029_close_report.md.path_proof.txt` *(governed path-proof for the formal EPIC029 close report)*  
* `audit/EPIC-029_MANIFEST.json.path_proof.txt` *(governed path-proof for the formal EPIC029 close manifest)*  
* *For the EPIC029 close decision, read this formal close-pack baseline together with the bounded dev-harness proof anchors and OPS-01 bundle listed later in **D.11c** and **D.11d**; those companion artifacts carry the HDE-CONJ001.4 closure posture, including the bounded local\_dev binding-equivalence path that the epic close review treated as supportable from repo evidence for later drain to Done at epic close.*

#### **D.0i EPIC029 shared evidence sentinel and mirror artifacts**

* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`

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

**Env-gating proof.** Writer error posture and env-gate refusal proof. See also §5.3 and HDE-Governance §10. Env-gate refusals are explicit (Forbidden) and must not emit Reader cache validators.

**A7 proof snapshots**

* `artifacts/reader/endpoints_snapshot.json` — snapshot of endpoints and env gates used for the proof run.  
* `artifacts/proofs/endpoints_env_gate_proof.log` — proof log showing env-gated endpoints refuse production access (no-store posture).  
* `artifacts/proofs/a7_transport_proof.log` — transport invariant proof summary for A7 routes.  
* `artifacts/proofs/success_get.txt` — raw GET success snapshot used by A7 transport proofs.  
* `artifacts/proofs/success_head.txt` — raw HEAD success snapshot used by A7 transport parity proofs.  
* `artifacts/proofs/success_304.txt` — raw 304 snapshot used by conditional delivery proofs.  
* `artifacts/proofs/success_writers_errors.txt` — raw writer/error snapshot used by no-store and no-ETag posture proofs.  
* `artifacts/proofs/success_encoding_invariance.txt` — encoding invariance proof snapshot.  
* `artifacts/proofs/success_encoding_invariance.txt.path_proof.txt` — governed path-proof for the encoding invariance proof snapshot.  
* `tests/http/test_endpoint_catalog.py` *(Reader Endpoint Catalog coverage proof anchor)*  
* `tests/http/test_reader_a7_transport.py` *(Reader A7 transport proof anchor)*

**Proof emission gating**

* Proof artifact emission is gated by `HDE_WRITE_A7_PROOFS`. When unset, default proof runs MUST NOT write proof artifacts.

**Endpoint Catalog artifacts**

* `docs/ENDPOINTS_CATALOG.json` — governed Endpoint Catalog (entry metadata including `path`, `allowed_methods`, `internal`, `class`, `env_gate`, `a7_eligible`).  
* `docs/ENDPOINTS_CATALOG.json.path_proof.txt` — path-proof sidecar for the governed catalog.  
* `docs/ENDPOINTS_CATALOG.json.sha256`  
* `artifacts/audit/ENDPOINTS_CATALOG.json` — audit mirror of the Endpoint Catalog used by epic proof review.

### **D.5 Error headers and writer posture**

* Error response headers (UTF-8): `tests/transport/headers/error_headers_utf8.snap`  
* No-store and no-ETag posture (writers/errors): `tests/transport/headers/no_store_writers_errors.snap`

### **D.6 Single-emitter guard (serializer path)**

* `Grep-guard: ci/grep-guards/no_json_dumps_public.regex`  
* `Allowlist for canonical emitter: ci/grep-guards/canonical_emitter.allowlist`  
* `Governed serializer grep artifact: artifacts/cli/guards/serializer_grep_guard.log`  
* `Governed emitter symbol proof: artifacts/cli/guards/emitter_symbol_proof.txt`  
* `Guard regression coverage: tests/cli/test_serializer_guards.py`  
* `Evidence-index target coverage: tests/ops/test_evidence_index.py`

### **D.7 Canonical JSON checks (public bytes)**

* *`audit/gates/canonical_json/canonical_json.gate.json` (supplemental canonical JSON gate summary)*  
* *`audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt` (governed path-proof for the supplemental canonical JSON gate summary)*  
* *`audit/gates/canonical_json/json_canonical_check.log`*  
* *`audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`*  
* *`audit/gates/canonical_json/json_canon_compare.log`*  
* *`audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`*  
* *`audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (authoritative canonical JSON gate check log for the bounded conjunction route-probe set `/reader`, `/dev/writer/conjunction`, `/dev/reader/conjunction`, `/dev/sampler/conjunction`, and `/internal/dev/sampler`)*  
* *`audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` (governed path-proof for the authoritative canonical JSON gate check log)*  
* *`audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` (authoritative canonical JSON gate compare log for the bounded conjunction route-probe set and the corrected expected-status evaluation on `/internal/dev/sampler`)*  
* *`audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt` (governed path-proof for the authoritative canonical JSON gate compare log)*  
* *`audit/gates/json_gate/canonical/json_gate_structured_record.json` (authoritative canonical JSON gate structured record, including the corrected `/internal/dev/sampler` result `expected_http_status: 200`, `http_status: 200`, and `status: "pass"`)*  
* *`audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt` (governed path-proof for the authoritative canonical JSON gate structured record)*

  ### D.8 showcompat seam (non-empty canonical JSON \+ parity)

* `artifacts/cli/showcompat/stdout.json` *(LF-terminated, non-empty)*  
* `artifacts/cli/showcompat/stdout.json.sha256` *(sha256 of stdout.json bytes; canonical)*  
* `artifacts/cli/showcompat/stdout.sha256` *(legacy alias; same bytes as stdout.json.sha256)*  
* `artifacts/cli/showcompat/args.json` *(deterministic capture context; test fixture only, not a release identity proof)*  
* `artifacts/cli/showcompat/two_run_identity.log`  
* `artifacts/cli/showcompat/abba.diff` *(expected empty)*  
* `artifacts/cli/showcompat/reader_cli_parity.diff` *(expected empty)*  
* `tests/cli/test_cli_canonical_bytes.py` *(showcompat stdout canonical-bytes validation)*  
* `tests/cli/test_cli_usage_and_errors.py` *(showcompat usage/errors validation)*

#### D.8a showcompat conjunction fixtures (AB / BA \+ sidecar)

* Pair fixtures (direct `a` / `b` ordering):

  * `artifacts/cli/pair.json` (AB)

  * `artifacts/cli/pair_ba.json` (BA)

* showcompat output fixtures (success, AB / BA):

  * `artifacts/cli/showcompat_ab.json` (AB)

  * `artifacts/cli/showcompat_ba.json` (BA)

* `--conjunction` output fixtures (success, AB / BA) and sidecar:

  * `artifacts/cli/out.json` (AB)

  * `artifacts/cli/out_ba.json` (BA)

  * `artifacts/cli/abba_sidecar.json` (sidecar)

  #### **D.8b compat conjunction identity capture (internal compat route)**

* `artifacts/compat/identity_hash.txt` *(explicit conjunction compat identity capture)*

* `artifacts/compat/identity_hash.txt.path_proof.txt` *(governed path-proof for the explicit conjunction compat identity capture)*

* `artifacts/compat/AB.json` *(canonical AB compat bytes referenced by the identity-hash proof)*

* `tests/http/test_compat_endpoint_contract.py` *(compat contract coverage for the conjunction identity-hash artifact)*

#### **D.8c CLI installability and conformance**

* `artifacts/cli/install/entrypoints.txt` *(positive console-entrypoint installability proof)*

* `artifacts/cli/install/installability_summary.json` *(installability summary with module and console help/version proof)*

* `artifacts/cli/help/hdctl_help.txt` *(top-level CLI help capture)*

* `artifacts/cli/help/showcompat_help.txt` *(showcompat help capture)*

* `artifacts/cli/help/reject_nonjson.txt` *(argument-policing capture for non-JSON rejection)*

* `artifacts/cli/summary.json` *(CLI conformance summary including deterministic sampler semantics)*

#### **D.8d Dev writer conjunction readback parity and A7 exclusion**

* `artifacts/writer/conjunction_write_readback.log` *(writer idempotence and write/readback parity log)*

* `artifacts/writer/conjunction_write_readback.log.path_proof.txt` *(governed path-proof for the write/readback log)*

* `artifacts/writer/conjunction_writer_summary.json` *(writer summary artifact)*

* `artifacts/writer/conjunction_writer_summary.json.path_proof.txt` *(governed path-proof for the writer summary artifact)*

* `tests/http/test_dev_conjunction_http.py` *(writer behavior and readback parity proof)*

* `tests/http/test_endpoint_catalog.py` *(A7-exclusion confirmation; no writer contract widening)*

### **D.9 Vendor rails (closed refusal and open conformance)**

* Closed-rails refusal proof (single-file canonical; headers → blank line → body): `artifacts/proofs/ops_refusal_proof.txt`  
* Shaping correctness (closed rails): `ci/jobs/logs_keys_only_redaction.yml`  
* Open-rails conformance (timeouts/retries/backoff): `ci/jobs/rails_open_conformance.yml`

#### D.9a HumanDesignAPI v2 conformance candidate proof anchors

These anchors are PF05 surface-proof candidates only. Final evidence schema, Human Evidence Index binding, Machine Mirror binding, hash sentinels, and path-proof naming are owned by HDE-Schemas & Artifacts. Until PF12 binds them, they MUST NOT be treated as final acceptance anchors.

* **Contract inventory and source precedence**  
  * `artifacts/vendor/hdapi_v2/source_inventory.json`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log`  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* **Request shaping, source selection, and legacy guard**  
  * `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`  
* **Response mapping and adapter boundary**  
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  * `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
* **Closed-rails refusal, typed errors, and rate limits**  
  * `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt`  
  * `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
* **Index and mirror coherence**  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * Sibling path-proof transcripts for each indexed HDAPI v2 artifact.  
* **PO-only open-rails smoke**  
  * Open-rails vendor-smoke evidence MUST live under the lowercase epic-specific OPS root assigned by the PO and MUST be bound into the governed evidence model before acceptance claims depend on it.  
  * PF05 MUST NOT bind a literal OPS path until the HDE epic or card ID is assigned.  
  * Open-rails smoke artifacts MUST remain secret-free, presence-only or redacted where needed, and HumanDesignAPI-only.

#### **D.9b HDE-EPIC033 PR-01 HumanDesignAPI v2 contract-inventory proof anchors**

These anchors bind the HDE-EPIC033 PR-01 contract-inventory slice only. They support HDE-FERM006 inventory and source-precedence evidence, not HumanDesignAPI v2 runtime request shaping, source selection execution, live conformance, public Reader changes, open-rails vendor smoke, new HTTP homes, or AI scope.

* **Contract inventory primary artifacts**  
  * `artifacts/vendor/hdapi_v2/source_inventory.json` *(canonical JSON inventory of public same-origin HumanDesignAPI documentation sources; source mode is closed-rails source cache)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt` *(governed path-proof for the canonical source inventory)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.md` *(human-readable source inventory summary; AI and LLM-oriented documentation such as `llms.txt` and `llms-full.txt` is documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt` *(governed path-proof for the source inventory summary)*  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log` *(validation log for `v2-routes.yaml`, `v1-routes.yaml`, quarantined or suspect OpenAPI artifacts, and route-spec gate status)*  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt` *(governed path-proof for the OpenAPI validation log)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md` *(anomaly ledger carrying the quarantined suspect `api-reference/openapi.json` posture)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt` *(governed path-proof for the anomaly ledger)*  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv` *(endpoint reference for v2 and v1 route families, including recommended `POST /v2/charts` and legacy `POST /v1/bodygraphs` entries)*  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt` *(governed path-proof for the endpoint reference)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(canonical JSON contract map binding validated vendor sources to v2 and legacy v1 route families; includes the explicit non-conformance claim for runtime request shaping, source selection, live conformance, public Reader change, and open-rails smoke)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt` *(governed path-proof for the contract map)*  
* **Closed-rails source-cache inputs**  
  * `artifacts/vendor/hdapi_v2/source_cache/api-reference.openapi.json`  
  * `artifacts/vendor/hdapi_v2/source_cache/authentication.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/coordinates_guide.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/migration_v1_to_v2.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/rate_limiting.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/response_format.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/robots_preflight.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`  
  * `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/v1_overview.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2_coordinates_chart_page.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2_full_chart_page.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2_overview.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2_simple_chart_page.body`  
* **Generator, tests, and validation proof anchors**  
  * `tools/evidence/generate_hdapi_v2_contract_inventory.py` *(governed contract-inventory generator; default mode is closed rails and consumes pre-captured public documentation)*  
  * `tests/evidence/test_hdapi_v2_contract_inventory.py` *(targeted HDAPI v2 contract-inventory regression suite)*  
  * `tests/evidence` *(full evidence test proof family relied on by PR-01 validation)*  
  * `tools/evidence/update_evidence_index.py` *(single-writer Evidence Index and Machine Mirror binding flow for the HDE-EPIC033 primary artifacts)*  
  * `tools/evidence/orientation_demo.py` *(orientation check proof command for the refreshed evidence skeleton)*  
  * `tools/evidence/validate_evidence_paths.py` *(path validation proof command for the PR-01 governed evidence family)*  
  * `tools/evidence/check_lf_endings.py` *(LF-ending proof command for the PR-01 governed evidence family)*  
  * `ci/checks/check_mirror_schema.sh` *(Machine Mirror schema proof command for the PR-01 governed evidence family)*  
  * `ci/checks/check_evidence_index_hash.sh` *(Human Evidence Index hash proof command for the PR-01 governed evidence family)*  
  * `ci/checks/check_final_lf.sh` *(final LF proof command for the PR-01 governed evidence family)*  
* **Acceptance baseline and evidence-ledger anchors**  
  * `docs/acceptance_map_epic033.json` *(acceptance map recording the inventory-only HDE-FERM006 scope completed by this PR and preserving HDE-FERM007 and HDE-FERM008 as not completed by this PR)*  
  * `docs/acceptance_map_epic033.json.path_proof.txt` *(governed path-proof for the EPIC033 acceptance map)*  
  * `audit/qa/hde-epic033/token_evidence_matrix.md` *(token evidence matrix using existing registry-valid tokens only and minting no vendor-v2-specific token)*  
  * `audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt` *(governed path-proof for the token evidence matrix)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log` *(viability log recording `status=PASS`, no vendor-v2-specific token, no runtime v2 conformance claim, no public Reader surface change, and no AI scope)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt` *(governed path-proof for the acceptance-map viability log)*  
  * `audit/docdeltas/hde-epic033_doc_deltas.md` *(repo-root doc-delta baseline for the PR-01 contract-inventory evidence binding)*  
  * `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt` *(governed path-proof for the repo-root doc-delta baseline)*  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md` *(QA meta doc-delta baseline for the PR-01 contract-inventory evidence binding)*  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt` *(governed path-proof for the QA meta doc-delta baseline)*  
* **Index, mirror, and collateral-refresh posture**  
  * `docs/evidence/INDEX.json` *(Human Evidence Index carrying HDE-EPIC033 PR-01 evidence rows)*  
  * `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the HDE-EPIC033 Human Evidence Index update)*  
  * `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
  * `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel update)*  
  * `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying HDE-EPIC033 PR-01 evidence rows)*  
  * `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the HDE-EPIC033 Machine Evidence Mirror update)*  
  * `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel update)*  
  * Collateral path-proof and orientation refreshes outside the HDAPI v2 family are evidence-tooling convergence only. They do not alter product behavior, create feature scope, create contract scope, create public Reader changes, or create new HTTP homes.  
* **Boundary and non-claim posture**  
  * This PR-01 proof family completes the inventory-only HDE-FERM006 evidence slice. It does not claim HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader change, new HTTP home, runtime v2 conformance, AI product scope, AI runtime, AI evidence family, AI token, AI credential, AI rail, AI QA obligation, prompt, embedding, chatbot, model-call, or AI provider scope.

#### **D.9c HDE-EPIC033 Live QA proof anchors for Step-0B through PO-009**

* **Step-0B doc-delta capture**  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log` *(canonical step receipt for Step-0B PASS evidence, exit code 0, closed rails, determinism pins, and `DOC_DELTA_PRESENT_OK`)*  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt` *(governed sibling path-proof for the Step-0B primary log)*  
  * `audit/docdeltas/hde-epic033_doc_deltas.md` *(repo-root doc-delta surface for the PR-01 contract-inventory evidence binding)*  
  * `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt` *(governed path-proof for the repo-root doc-delta surface)*  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md` *(QA-root doc-delta surface for the PR-01 contract-inventory evidence binding)*  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt` *(governed path-proof for the QA-root doc-delta surface)*  
  * Step-0B makes no broader HDE-EPIC033 closure claim.  
* **PO-001 source inventory and source-cache proof**  
  * `audit/qa/hde-epic033/checks/po-001/primary.log` *(canonical step receipt for PO-001 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-001/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-001 primary log)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.json` *(source inventory artifact relied on by PO-001; full PR-01 contract-inventory anchor is listed in D.9b)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.md` *(human-readable source inventory artifact relied on by PO-001; full PR-01 contract-inventory anchor is listed in D.9b)*  
  * `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml` *(closed-rails source-cache route input relied on by PO-001)*  
  * `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml` *(closed-rails source-cache route input relied on by PO-001)*  
  * `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json` *(closed-rails source-cache metadata input relied on by PO-001)*  
* **PO-002 AI and LLM boundary proof**  
  * `audit/qa/hde-epic033/checks/po-002/primary.log` *(canonical step receipt for PO-002 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-002/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-002 primary log)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.md` *(source inventory summary relied on by PO-002 for documentation-discovery-only AI and LLM boundary posture)*  
  * `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body` *(closed-rails source-cache input relied on by PO-002 as documentation-discovery-only context)*  
  * `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt` *(closed-rails source-cache input relied on by PO-002 as documentation-discovery-only context)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md` *(anomaly posture artifact relied on by PO-002; full PR-01 contract-inventory anchor is listed in D.9b)*  
  * PO-002 does not create AI product scope, AI runtime scope, AI evidence scope, AI token scope, AI credential scope, AI rails scope, prompt scope, embedding scope, chatbot scope, model-call scope, or AI provider scope.  
* **PO-003 route validation proof**  
  * `audit/qa/hde-epic033/checks/po-003/primary.log` *(canonical step receipt for PO-003 PASS evidence after the accepted operational Ruby dependency deviation)*  
  * `audit/qa/hde-epic033/checks/po-003/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-003 primary log)*  
  * `tests/evidence/test_hdapi_v2_contract_inventory.py` *(route-validation test proof relied on by PO-003)*  
  * The PO-003 Ruby installation deviation is an operational dependency deviation only. It does not change required deliverables, PASS/FAIL criteria, public Reader surface, runtime v2 conformance, open-rails posture, new HTTP homes, or AI scope.  
* **PO-004 OpenAPI quarantine proof**  
  * `audit/qa/hde-epic033/checks/po-004/primary.log` *(canonical step receipt for PO-004 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-004/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-004 primary log)*  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log` *(OpenAPI validation and quarantine proof relied on by PO-004; full PR-01 contract-inventory anchor is listed in D.9b)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md` *(known-anomalies proof relied on by PO-004; full PR-01 contract-inventory anchor is listed in D.9b)*  
* **PO-005 endpoint-reference proof**  
  * `audit/qa/hde-epic033/checks/po-005/primary.log` *(canonical step receipt for PO-005 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-005/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-005 primary log)*  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv` *(endpoint reference proof relied on by PO-005; full PR-01 contract-inventory anchor is listed in D.9b)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(contract-map proof relied on by PO-005; full PR-01 contract-inventory anchor is listed in D.9b)*  
* **PO-006 contract-map non-claim proof**  
  * `audit/qa/hde-epic033/checks/po-006/primary.log` *(initial PO-006 primary receipt before bounded QA-harness remediation)*  
  * `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt` *(governed sibling path-proof for the initial PO-006 primary log)*  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log` *(accepted final PO-006 Moon Loop remediation R3 receipt for the QA-harness phrase-match defect)*  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log.path_proof.txt` *(governed sibling path-proof for the accepted final PO-006 remediation receipt)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(contract-map proof relied on by PO-006 for no runtime v2 conformance, no runtime request shaping, no source-selection execution, no open-rails vendor smoke, no public Reader surface, no new HTTP home, and no AI scope)*  
  * The PO-006 Moon Loop deviation is QA evidence-harness remediation inside `audit/qa/hde-epic033/checks/` only. It does not create product bytes, new PF05 runtime behavior, public Reader expansion, new HTTP homes, open-rails vendor behavior, or epic closure.  
* **PO-007 evidence index and mirror update proof**  
  * `audit/qa/hde-epic033/checks/po-007/primary.log` *(canonical step receipt for PO-007 PASS evidence under closed rails and deterministic pins, claiming evidence-index and path-proof tokens)*  
  * `audit/qa/hde-epic033/checks/po-007/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-007 primary log)*  
  * `docs/evidence/INDEX.json` *(Human Evidence Index proof anchor relied on by PO-007; full PR-01 index anchor is listed in D.9b)*  
  * `docs/evidence/INDEX.sha256` *(Human Evidence Index hash sentinel relied on by PO-007)*  
  * `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
  * `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel)*  
  * `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror proof anchor relied on by PO-007; full PR-01 mirror anchor is listed in D.9b)*  
  * `artifacts/evidence_index.jsonl.sha256` *(Machine Evidence Mirror hash sentinel relied on by PO-007)*  
  * `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel)*  
  * `tools/evidence/update_evidence_index.py` *(evidence updater check relied on by PO-007)*  
  * `tools/evidence/validate_evidence_paths.py` *(evidence path validation check relied on by PO-007)*  
  * `tools/evidence/check_lf_endings.py` *(LF-ending check relied on by PO-007)*  
  * `ci/checks/check_mirror_schema.sh` *(Machine Mirror schema check relied on by PO-007)*  
  * `ci/checks/check_evidence_index_hash.sh` *(Human Evidence Index hash check relied on by PO-007)*  
  * `ci/checks/check_final_lf.sh` *(final LF check relied on by PO-007)*  
* **PO-008 token posture proof**  
  * `audit/qa/hde-epic033/checks/po-008/primary.log` *(canonical step receipt for PO-008 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-008/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-008 primary log)*  
  * `audit/qa/hde-epic033/token_evidence_matrix.md` *(baseline existing-token matrix proving no vendor-v2-specific token minting)*  
  * PO-008 proves baseline existing-token posture only. It does not mint a vendor-v2-specific acceptance token.  
* **PO-009 HDE-FERM006 supportability and no-drainage proof**  
  * `audit/qa/hde-epic033/checks/po-009/primary.log` *(canonical step receipt for final PO-009 PASS evidence, including explicit repo-evidence-only supportability and no PF09.5 drainage claim lines)*  
  * `audit/qa/hde-epic033/checks/po-009/primary.log.path_proof.txt` *(governed sibling path-proof for the final PO-009 primary log)*  
  * `docs/acceptance_map_epic033.json` *(acceptance map relied on by PO-009 to bind HDE-FERM006.1 through HDE-FERM006.4 and preserve HDE-FERM007 and HDE-FERM008 as not completed by this PR)*  
  * `audit/qa/hde-epic033/token_evidence_matrix.md` *(token evidence matrix relied on by PO-009 for existing-token posture)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log` *(viability log relied on by PO-009 for no vendor-v2-specific token, no runtime conformance claim, no public Reader surface change, and no AI scope)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(contract map relied on by PO-009 to preserve inventory-only HDE-FERM006 supportability and non-completion of runtime v2 behavior)*  
  * The PO-009 reconstructed helper wrapper and explicit proof-posture append are accepted execution deviations for this step because final evidence contains the required repo-evidence-only supportability and no PF09.5 drainage claim lines. The deviation does not change required deliverables, public Reader bytes, runtime v2 conformance, source-selection execution, open-rails vendor behavior, new HTTP homes, AI scope, PF09.5 drainage, or epic closure.  
* **HDE-EPIC033 Live QA non-claim posture through PO-009**  
  * Step-0B and PO-001 through PO-009 are step-level Live QA evidence only unless a later closeout artifact says otherwise.  
  * These checks do not claim broader HDE-EPIC033 closure, runtime HumanDesignAPI v2 conformance, runtime request shaping, source-selection execution, open-rails vendor smoke, public Reader change, new HTTP home, or AI scope.  
  * PF09.5 drainage remains unproven by PO-009 unless separately proven by PF09.5.

  #### **D.9d HDE-EPIC033 Live QA proof anchors for PO-010 to PO-012**

* **PO-010 later-runtime-scope non-claim proof**  
  * `audit/qa/hde-epic033/checks/po-010/primary.log` *(original planned PO-010 receipt retained as initial `FAIL_BEHAVIOR` evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt` *(governed sibling path-proof for the original PO-010 primary log)*  
  * `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log` *(accepted final PO-010 remediation receipt with final remediation status `PASS` and exit code 0\)*  
  * `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt` *(governed sibling path-proof for the accepted PO-010 remediation receipt)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md` *(anomaly ledger relied on by PO-010 for runtime request-shaping non-claim posture)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(contract-map proof relied on by PO-010 for later adapter architecture, runtime request shaping, live vendor smoke, and runtime v2 conformance non-claim posture)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log` *(acceptance-map viability proof relied on by PO-010)*  
  * The PO-010 remediation is accepted as QA evidence-harness remediation only. It preserves the original proof target and does not claim later adapter architecture, runtime request shaping, live vendor smoke, runtime v2 conformance, public Reader change, new HTTP home, AI scope, PF09.5 drainage, or epic closure.  
* **PO-011 inventory-only runtime-conformance non-claim proof**  
  * `audit/qa/hde-epic033/checks/po-011/primary.log` *(canonical step receipt for PO-011 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-011 primary log)*  
  * `artifacts/vendor/hdapi_v2/source_inventory.md` *(source inventory proof relied on by PO-011 for inventory-only posture)*  
  * `artifacts/vendor/hdapi_v2/contract_map.json` *(contract-map proof relied on by PO-011 for runtime vendor-conformance non-claim posture)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log` *(acceptance-map viability proof relied on by PO-011)*  
  * PO-011 does not require a remediation receipt and does not claim runtime vendor conformance, runtime request shaping, source-selection execution, open-rails vendor smoke, public Reader change, new HTTP home, AI scope, PF09.5 drainage, or epic closure.  
* **PO-012 no-expansion boundary proof**  
  * `audit/qa/hde-epic033/checks/po-012/primary.log` *(original planned PO-012 receipt retained as initial `FAIL_BEHAVIOR` evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt` *(governed sibling path-proof for the original PO-012 primary log)*  
  * `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log` *(accepted final PO-012 remediation receipt with final remediation status `PASS` and exit code 0\)*  
  * `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt` *(governed sibling path-proof for the accepted PO-012 remediation receipt)*  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md` *(anomaly ledger relied on by PO-012 for live vendor smoke, public Reader change, new HTTP home, and AI runtime or evidence-scope non-claim posture)*  
  * `docs/acceptance_map_epic033.json` *(acceptance map relied on by PO-012)*  
  * `audit/qa/hde-epic033/acceptance_map_viability.log` *(acceptance-map viability proof relied on by PO-012)*  
  * The PO-012 remediation is accepted as QA evidence-harness remediation only. It preserves the original proof target and does not claim live vendor smoke, public Reader change, new HTTP home, AI runtime or evidence scope, PF09.5 drainage, or epic closure.  
* **Shared PO-010 to PO-012 remediation posture**  
  * PO-010 and PO-012 initial failures are retained as failure context, not final proof basis.  
  * PO-010 and PO-012 accepted remediation receipts are final proof basis for those steps.  
  * The shared remediation pattern was a QA evidence-harness phrase-match correction inside the QA root. It did not change product code, repo tests, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multi-subsystem implementation surfaces.

  #### **D.9e HDE-EPIC033 Live QA proof anchors for PO-013, PO-014, and qa-16 closeout deliverables**

* **PO-013 routed final proof**  
  * `audit/qa/hde-epic033/checks/po-013/primary.log` *(original planned PO-013 receipt retained as initial `FAIL_BEHAVIOR`, exit code 1, and `ORIENTATION_MISMATCH` evidence)*  
  * `audit/qa/hde-epic033/checks/po-013/primary.log.path_proof.txt` *(governed sibling path-proof for the original PO-013 primary log)*  
  * `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log` *(QA\_PLAN\_UPDATE routing receipt proving routing before final PASS-grade proof)*  
  * `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-013 routing receipt)*  
  * `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log` *(accepted final PO-013 R3 proof receipt with `PASS`, exit code 0, routing proof, `message_count=0`, evidence path validation, LF checks, orientation, mirror schema, evidence-index hash, final LF, and viability boundaries)*  
  * `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log.path_proof.txt` *(governed sibling path-proof for the accepted final PO-013 R3 proof receipt)*  
  * PO-013 is accepted only through the R3 proof after QA\_PLAN\_UPDATE routing. The original planned receipt remains failure evidence and is not the accepted final proof basis.  
  * PO-013 final proof does not claim runtime v2 conformance, public Reader surface change, new HTTP home, AI scope, broader HDE-EPIC033 closure, PF09.5 drainage, or PO closeout.  
* **PO-014 non-claim and stable-root proof**  
  * `audit/qa/hde-epic033/checks/po-014/primary.log` *(canonical step receipt for PO-014 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic033/checks/po-014/primary.log.path_proof.txt` *(governed sibling path-proof for the PO-014 primary log)*  
  * PO-014 proves non-claim and stable-QA-root posture only. It does not claim implementation work, PF document edit, runtime vendor conformance, public Reader change, new HTTP home, AI scope, epic closure, PF09.5 drainage, or acceptance-token satisfaction.  
* **qa-16 closeout deliverables proof**  
  * `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log` *(canonical step receipt for qa-16 closeout-deliverables PASS evidence)*  
  * `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt` *(governed sibling path-proof for the qa-16 primary log)*  
  * `audit/qa/hde-epic033/qa_step_logs_manifest.json` *(QA step-log manifest listing Step-0B through PO-014 and qa-16 receipts)*  
  * `audit/qa/hde-epic033/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the QA step-log manifest)*  
  * `audit/qa/hde-epic033/00_meta/discovery_artifact.md` *(D0 discovery artifact created for qa-16 closeout deliverables)*  
  * `audit/qa/hde-epic033/00_meta/discovery_artifact.md.path_proof.txt` *(governed path-proof for the D0 discovery artifact)*  
  * `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md` *(QA RCA and Doc Delta summary created for qa-16 closeout deliverables)*  
  * `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt` *(governed path-proof for the QA RCA and Doc Delta summary)*  
  * `docs/evidence/INDEX.json` *(Human Evidence Index proof anchor relied on by qa-16 closeout deliverables)*  
  * `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror proof anchor relied on by qa-16 closeout deliverables)*  
  * `audit/gates/topology/orientation_demo.txt` *(orientation evidence proof anchor relied on by qa-16 closeout deliverables)*  
  * qa-16 satisfies closeout deliverable criteria only. It does not claim broader HDE-EPIC033 closure, PO closeout, PF09.5 drainage, runtime v2 conformance, public Reader surface change, new HTTP home, AI scope, or merge provenance.  
* **HDE-EPIC033 Live QA and closeout non-claim posture through qa-16**  
  * Step-0B through PO-014 and qa-16 have PF10-supported PASS evidence or accepted remediation evidence.  
  * Ready-with-caveats closeout posture is not formal closure by itself.  
  * Lead closure decision, board update, merge provenance, formal close-pack completion, and PF09.5 canon drainage remain separate from PF05 evidence-anchor listing unless later source evidence explicitly binds them.  
  * HDE-FERM007 and HDE-FERM008 remain out of scope and not evidenced by this proof set. Do not treat this evidence as runtime v2 adapter conformance, live vendor conformance, public Reader change, new HTTP home, AI scope, or docs PR execution proof.  
* **HDE-EPIC033 Lead retrospective closure-trace context.** The HDE-EPIC033 Lead Dev Epic Retrospective may be used to interpret **D.9b** through **D.9e** only as repo-supported closure-trace context for the HDE-FERM006 inventory-only contract slice. It does not create new PF05 runtime bytes, runtime request shaping, source-selection execution, open-rails vendor smoke, public Reader changes, new HTTP homes, AI scope, PF09.5 drainage, formal close-pack completion, merge provenance, board state, PO closeout, or proof that HDE-FERM007 or HDE-FERM008 is done.

#### **D.9f HDE-EPIC034 HumanDesignAPI v2 source-selection, request-shaping, response-mapping, boundary, and closed-rails proof anchors**

These anchors bind HDE-EPIC034 vendor-seam proof families only. They do not claim full HumanDesignAPI v2 live/runtime conformance, normalized data-path completion, open-rails vendor success, public Reader expansion, public payload expansion, new HTTP homes, AI scope, PF09 drainage, OPS completion, QA PASS, or epic closure unless a later source explicitly binds those stronger claims.

* **OPS discovery and environment fact summary**  
  * `audit/ops/hde-epic034/ops-01/fact_summary.json` *(secret-safe operational fact summary for canonical `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, deprecated `HDAPI_BASE_URL` compatibility posture, endpoint-family availability, and non-claim boundaries)*  
* **Source selection and legacy isolation**  
  * `artifacts/vendor/hdapi_v2/source_selection.snapshot.json` *(governed source-selection snapshot distinguishing recommended v2 chart routes from legacy v1 BodyGraph routes)*  
  * `artifacts/vendor/hdapi_v2/v1_legacy_guard.log` *(legacy guard proving v1 BodyGraph behavior is explicit legacy behavior and not silently collapsed into recommended v2 chart behavior)*  
* **Request shaping**  
  * `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json` *(governed request-shaping snapshot for canonical `HD_API_BASE_URL`, deprecated alias posture, version-neutral resource paths, v2 Bearer auth, v1 legacy `HD-Api-Key`, geocode posture, and no live-conformance claim)*  
  * `audit/qa/hde-epic034/pr-02/request_shaping_check.log` *(PR-02 request-shaping check log)*  
* **Response-envelope mapping**  
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` *(proof-level StandardResponse envelope mapping for response type, success posture, error-code posture, data identity posture, route variant, schema-gap status, and no vendor-payload-body emission)*  
  * `audit/qa/hde-epic034/pr-03/response_mapping_check.log` *(PR-03 response-mapping check log)*  
* **Adapter and presenter boundary**  
  * `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log` *(adapter/presenter boundary proof family after W-001 through W-005 remediation, including conservative fail-closed boundary classification and route-drift repair posture)*  
  * `audit/qa/hde-epic034/pr-04/boundary_check.log` *(PR-04 boundary check log, if present in the governed evidence family)*  
* **Closed-rails refusal**  
  * `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt` *(PR-05 closed-rails refusal proof for implemented current chart resource paths and legacy resource paths, no DNS/socket/HTTP external I/O, canonical base URL key, v1/v2 auth posture, no live vendor call, no open-rails smoke, no runtime v2 conformance, no public Reader change, and no AI scope)*  
  * `audit/qa/hde-epic034/pr-05/closed_rails_check.log` *(PR-05 closed-rails validation log)*  
* **Index and mirror coherence**  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * Sibling `*.path_proof.txt` transcripts for each indexed HDE-EPIC034 governed artifact.

#### **D.9g HDE-EPIC034 OPS-02, PR-06, and Live QA proof anchors**

These anchors bind the bounded open-rails HumanDesignAPI v2 smoke and its governed evidence binding only. They support HDE-FERM008.2 evidence posture only and do not claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, HDE-FERM008.3/.4/.5 completion, public Reader change, public route, public flag, public payload change, new HTTP home, public transport change, AI scope, PO closeout, board update, merge provenance, or PF-canon drainage.

* **OPS-02 open-rails smoke evidence bundle**  
  * `audit/ops/hde-epic034/ops-02/commands.txt` *(PASS-producing command transcript for the bounded open-rails smoke; records open rails, deterministic pins, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` posture, and `charts/coordinates`)*  
  * `audit/ops/hde-epic034/ops-02/env_presence_redacted.json` *(secret-safe environment presence snapshot)*  
  * `audit/ops/hde-epic034/ops-02/exit_codes.txt` *(OPS wrapper exit-code capture)*  
  * `audit/ops/hde-epic034/ops-02/files_sha256.txt` *(checksum listing for the OPS-02 evidence bundle)*  
  * `audit/ops/hde-epic034/ops-02/moon_loop_rerun_transcript.txt` *(rerun transcript proving command-to-output provenance)*  
  * `audit/ops/hde-epic034/ops-02/ops02_full_action_log_and_evidence_output.md` *(full action log and evidence output)*  
  * `audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py` *(repo-resident secret-safe procedure used for the PASS-producing smoke)*  
  * `audit/ops/hde-epic034/ops-02/request_summary.json` *(redacted request summary; v2 chart auth posture, version-neutral `charts/coordinates`, no legacy v2 `HD-Api-Key`)*  
  * `audit/ops/hde-epic034/ops-02/result_summary.json` *(OPS-02 result summary; classification PASS, vendor attempted, raw secrets not persisted, full vendor payload not persisted, HDE-FERM008.2 evidence ready)*  
  * `audit/ops/hde-epic034/ops-02/stderr.log`  
  * `audit/ops/hde-epic034/ops-02/stdout.log`  
* **PR-06 OPS evidence binding**  
  * `audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log` *(governed binding log; PR-06 does not rerun the live vendor call, binds OPS-02 evidence, and records HDE-FERM008.2-only support)*  
  * `docs/acceptance_map_epic034.json` *(acceptance map; baseline existing tokens only, no vendor-v2-specific acceptance token, HDE-FERM008.2 supported, HDE-FERM008 parent and HDE-FERM008.3/.4/.5 not completed)*  
  * `audit/docdeltas/hde-epic034_doc_deltas.md`  
  * `audit/qa/hde-epic034/00_meta/doc_deltas.md`  
* **Live QA and closeout proof anchors**  
  * `audit/qa/hde-epic034/qa_step_logs_manifest.json` *(manifest listing Step-0B and PO-001 through PO-018 check logs as PASS)*  
  * `audit/qa/hde-epic034/00_meta/discovery_artifact.md` *(records PO-012 as the bounded PO-authorized open-rails Live QA step and preserves nonclaim boundaries)*  
  * `audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md` *(QA RCA / Doc Delta summary; closeout assembly evidence only, not PO closeout, board update, merge, or canon drain)*  
* **Index, mirror, and path-proof posture**  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * Sibling `*.path_proof.txt` transcripts for the OPS-02, PR-06, acceptance-map, Live QA, index, mirror, and hash artifacts listed above.

#### **D.9h HDE-EPIC035 HumanDesignAPI v2 provider-outcome, response-normalization, OPS, and evidence-loop proof anchors**

These anchors bind HDE-EPIC035 vendor-seam evidence only. They do not claim QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, AI scope, board update, merge provenance, or PF-canon drainage.

* **PR-01 provider-outcome and rate-limit evidence**  
  * `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` *(HDE-FERM008.3 provider-outcome mapping; closed-rails only; maps provider HTTP statuses, malformed response posture, network-error posture, retryability, route/auth posture, and no-claim boundaries)*  
  * `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` *(HDE-FERM008.3 rate-limit and Retry-After evidence; closed-rails only)*  
  * `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`  
  * `tools/evidence/generate_hdapi_v2_live_conformance.py` *(closed-rails evidence generator; generator certification must enforce closed deterministic rails before writing or checking provider-outcome evidence)*  
  * `tests/evidence/test_hdapi_v2_live_conformance.py` *(targeted regression coverage for provider-outcome evidence, non-backdated proofs, and non-closed-rails refusal)*  
* **PR-02 response-normalization and release binding**  
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` *(HDE-FERM008.4 exact schema/adapter gap evidence; records that v2 ChartResult and ChartSimpleResult are not proven to feed existing BodyGraph cache, person/bodygraph compute inputs, or compatibility inputs without adapter proof)*  
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` *(binds PR-01 HDE-FERM008.3 provider-outcome evidence to PR-02 HDE-FERM008.4 exact schema/adapter gap evidence without claiming full runtime conformance or HDE-FERM008.5 closure)*  
  * `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`  
  * `tools/evidence/generate_hdapi_v2_response_normalization.py`  
  * `tests/evidence/test_hdapi_v2_response_normalization.py`  
* **OPS-01 retained open-rails observations**  
  * `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt`  
  * `audit/ops/hde-epic035/ops-01/files_sha256.txt`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt` *(records `bg:resolve --source vendor` as a legacy BodyGraph ingest-path observation against configured v2 base, v2 `charts/simple` success, geokey proof for `charts/simple`, and no full runtime-conformance claim)*  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json`  
  * `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json`  
* **PR-03 evidence-loop and acceptance-boundary artifacts**  
  * `docs/acceptance_map_epic035.json` *(baseline existing tokens only; records HDE-FERM008.5 evidence-loop closure candidate posture and no parent completion)*  
  * `docs/acceptance_map_epic035.json.path_proof.txt`  
  * `audit/qa/hde-epic035/token_evidence_matrix.md`  
  * `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`  
  * `audit/qa/hde-epic035/acceptance_map_viability.log`  
  * `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`  
  * `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` *(binds retained OPS-01 evidence without rerunning OPS or claiming OPS completion)*  
  * `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`  
  * `audit/docdeltas/hde-epic035_doc_deltas.md`  
  * `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`  
  * `audit/qa/hde-epic035/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`  
  * `tests/evidence/test_hde_epic035_pr03_evidence_loop.py`  
* **Index, mirror, and path-proof posture**  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `docs/evidence/INDEX.json.path_proof.txt`  
  * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
  * Sibling `*.path_proof.txt` transcripts for each indexed HDE-EPIC035 governed artifact.

#### **D.9i HDE-EPIC036 `bg:resolve --source vendor` route-policy and evidence-loop proof anchors**

These anchors bind HDE-EPIC036 route-policy and evidence-loop proof surfaces only. They do not claim QA PASS beyond the cited QA step result, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, AI scope, board update, merge provenance, or PF-canon drainage.

* **PR-01 route-policy classification and closed-rails proof**  
  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json` *(HDE-FERM008.6 route-policy snapshot; configured v2 base selects `unsupported_runtime_nonclaim`; non-v2 configured base preserves explicit legacy fallback; v2 chart-backed BodyGraph resolution and dual-route policy are not claimed)*  
  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json` *(records BodyGraph-detail sufficiency as unsupported runtime nonclaim and records no complete v2 ChartResult or ChartSimpleResult to BodyGraph/person/cache adapter in inspected loci)*  
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`  
  * `audit/qa/hde-epic036/route_policy_decision.log` *(records selected route policy, no configured-v2 `bodygraphs` request, preserved non-v2 explicit legacy fallback, no public expansion, no raw payload persistence, no AI scope, and no full v2 runtime conformance)*  
  * `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`  
  * `tests/bodygraph/test_bg_resolve_route_policy.py`  
  * `tests/bodygraph/test_resolver_vendor.py`  
  * `tests/cli/test_bg_resolve.py`  
  * `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`  
* **PR-02 evidence-loop and acceptance-boundary artifacts**  
  * `docs/acceptance_map_epic036.json` *(HDE-FERM008.6 governed evidence-loop closure for HDE-EPIC036 PR-02; approved PR-02 token roster only; route-policy classification and evidence-loop binding only)*  
  * `docs/acceptance_map_epic036.json.path_proof.txt`  
  * `audit/qa/hde-epic036/token_evidence_matrix.md`  
  * `audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt`  
  * `audit/qa/hde-epic036/acceptance_map_viability.log`  
  * `audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt`  
  * `audit/docdeltas/hde-epic036_doc_deltas.md`  
  * `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`  
  * `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`  
  * `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`  
* **QA open-rails and closeout evidence anchors**  
  * `audit/qa/hde-epic036/checks/po-010/primary.log` *(PO-010 primary log for bounded open-rails route-policy behavior proof)*  
  * `audit/qa/hde-epic036/checks/po-010/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic036/checks/po-010/live_route_policy.log` *(records open rails, redacted base posture, `PROVIDER_ROUTE_UNSUPPORTED`, `unsupported_runtime_nonclaim`, legacy BodyGraph route family, `bodygraphs` resource path, and redacted route auth posture)*  
  * `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`  
  * `audit/qa/hde-epic036/qa_step_logs_manifest.json` *(Step-0B through PO-012 and `qa-13-governed-evidence-gates` check log manifest)*  
  * `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt`  
  * `audit/qa/hde-epic036/checks/po-011/primary.log`  
  * `audit/qa/hde-epic036/checks/po-011/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic036/checks/po-012/primary.log`  
  * `audit/qa/hde-epic036/checks/po-012/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log`  
  * `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic036/00_meta/discovery_artifact.md`  
  * `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`  
  * `audit/qa/hde-epic036/00_meta/hde_epic036_po011_po012_qa13_qa14_action_report.md`  
  * `audit/qa/hde-epic036/00_meta/hde_epic036_po011_po012_qa13_qa14_remediation_evidence_addendum.md`  
* **Index, mirror, and path-proof posture**  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `docs/evidence/INDEX.json.path_proof.txt`  
  * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
  * Sibling `*.path_proof.txt` transcripts for each indexed HDE-EPIC036 governed artifact.

### **D.10 Runtime posture & env-resolver envelopes**

* Env snapshot (DB posture): `artifacts/runtime/env_matrix.snapshot.json`  
* Failure envelope (guarded selection-only bytes): `artifacts/runtime/env_matrix.failure.json`  
* **Dev resolver snapshot (rails evidence):** `artifacts/runtime/env_connectivity.snapshot.json`

### **D.11 QA artifacts namespace (transient captures)**

* **Live QA root (write-scope):** `audit/qa/<epic-id>/` (mechanical artifacts only; runbook rails and “gitless/no git-status gating” live in Glow QA Guide and Epic-Process-Guide by title)  
* **Checks-only evidence layout.** Live QA evidence MUST be organized only by `check_id` under stable check directories: `audit/qa/<epic-id>/checks/<check-id>/`. Re-running QA MUST reuse the same epic-scoped root and stable check directories.  
* **Per-run nesting is disallowed.** Do not create run-id directories, timestamped run directories, or other per-run subroots under the Live QA root.  
* **Per-run root variables are vetoed.** Plans and reviews MUST NOT require operator-selected “fresh directory for this run” postures; evidence writes to the stable check directories.  
* **Plan-created deliverables under checks.** When Live QA requires plan-created deliverables, they MUST be written under the stable check directory, not under per-run directories or ad-hoc run roots.  
* **Transient captures (test-only; non-gating):** `artifacts/qa/` (allowed for local/test captures; not the Live QA run root)  
* **Filename case posture.** Uppercase letters in filenames are allowed. The lowercase ASCII naming rail applies to directory names (and to identifier classes explicitly defined as lowercase-only, such as check IDs). Reviewers and lint MUST NOT treat uppercase filename segments as a lowercase-rule violation.  
* **No run\_id correctness key.** Live QA plans and governed evidence artifacts MUST NOT require `run_id` (or `RUN_ID`) as an operator input, step-log header field, manifest field, or correctness key; acceptance is check-centric and stable across reruns.  
* **History retention is non-gating.** Optional per-execution history nesting or labeling MUST remain non-canonical and non-gating; acceptance binds only to canonical check-centric evidence surfaces, not to per-execution identifiers.

#### D.11a EPIC027 Live QA proof anchors for PF05 surfaces

* **po-001 dev conjunction and catalog coherence**

  * `audit/qa/hde-epic027/checks/po-001/route_inventory.txt` *(dev conjunction trio and compat blueprint route inventory proof)*

  * `audit/qa/hde-epic027/checks/po-001/dev_conjunction_http.txt` *(dev conjunction HTTP PASS capture)*

  * `audit/qa/hde-epic027/checks/po-001/endpoint_catalog.txt` *(Endpoint Catalog proof capture for the passing po-001 run)*

  * `audit/qa/hde-epic027/checks/po-001/primary.log` *(governed step log for po-001)*

* **po-002 compat surface and identity discoverability**

  * `audit/qa/hde-epic027/checks/po-002/compat_surface.txt` *(compat surface mount, GET probe, POST compute, and prod APP\_ENV gate proof)*

  * `audit/qa/hde-epic027/checks/po-002/compat_identity_discovery.txt` *(discoverability proof via updater and mirror references to `compat.conjunction.identity_hash`)*

  * `audit/qa/hde-epic027/checks/po-002/primary.log` *(governed step log for po-002)*

* **po-003 shared emitter and showcompat proofs**

  * `audit/qa/hde-epic027/checks/po-003/cli_emitter_proof.txt` *(LF guard and shared `emit_public` proof)*

  * `audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt` *(showcompat parity and identity proof capture)*

  * `audit/qa/hde-epic027/checks/po-003/showcompat_help.txt` *(showcompat help-surface proof capture)*

  * `audit/qa/hde-epic027/checks/po-003/primary.log` *(governed step log for po-003)*  
* **po-004 CLI installability, conformance, and `bg:resolve` help proof**  
  * `audit/qa/hde-epic027/checks/po-004/entrypoint_proof.txt` (explicit pyproject console-binding proof)

  * `audit/qa/hde-epic027/checks/po-004/cli_install_help.txt` (CLI install-help test PASS capture)

  * `audit/qa/hde-epic027/checks/po-004/bg_resolve_test.txt` (bg:resolve CLI test PASS capture)

  * `audit/qa/hde-epic027/checks/po-004/bg_resolve_help.txt` (bg:resolve help-surface proof capture)

  * `audit/qa/hde-epic027/checks/po-004/primary.log` (governed step log for po-004)  
* **po-005 Reader A7 proof family and catalog-target discipline**  
  * *`audit/qa/hde-epic027/checks/po-005/reader_a7_transport.txt` (Reader A7 transport PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-005/catalog_routes.txt` (catalog inventory proof that `/reader` is A7-eligible and `/internal/version` is excluded)*

  * *`audit/qa/hde-epic027/checks/po-005/primary.log` (governed step log for po-005)*  
* **po-006 writer behavior, mirror discoverability, and A7 exclusion**  
  * *`audit/qa/hde-epic027/checks/po-006/dev_conjunction_http.txt` (dev conjunction HTTP PASS capture for writer behavior)*

  * *`audit/qa/hde-epic027/checks/po-006/writer_index_rows.txt` (machine-mirror discoverability proof for writer artifacts)*

  * *`audit/qa/hde-epic027/checks/po-006/primary.log` (governed step log for po-006)*  
* **po-007 evidence-discipline and qa-step-manifest ledger coverage**  
  * *`audit/qa/hde-epic027/checks/po-007/update_evidence_index_write.txt` (evidence-index write PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/update_evidence_index_check.txt` (evidence-index check PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/orientation_demo_write.txt` (orientation-demo write PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/orientation_demo_check.txt` (orientation-demo check PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/validate_evidence_paths.txt` (evidence-path validation PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/check_lf_endings.txt` (final-LF validation PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/check_mirror_schema.txt` (mirror-schema PASS capture)*

  * *`audit/qa/hde-epic027/checks/po-007/qa_step_manifest_lookup.txt` (EPIC027 qa-step-manifest coverage proof in updater and governed ledgers)*

  * *`audit/qa/hde-epic027/checks/po-007/primary.log` (governed step log for po-007; claimed tokens are recorded in the step header)*  
* **po-008 close-pack generator, bindings, and ledger truthfulness**  
  * *`audit/qa/hde-epic027/checks/po-008/generate_close_pack.txt` (close-pack generator run capture)*  
  * *`audit/qa/hde-epic027/checks/po-008/close_pack_bindings.txt` (binding proof that close-pack paths point to the EPIC027 QA root and canonical ledger files)*  
  * *`audit/qa/hde-epic027/checks/po-008/qa_step_manifest_lookup.txt` (proof that the EPIC027 qa-step manifest is ledger-bound rather than merely present on disk)*  
  * *`audit/qa/hde-epic027/checks/po-008/primary.log` (governed step log for po-008)*  
* **po-009 catalog surface and token inventory guard**  
  * *`audit/qa/hde-epic027/checks/po-009/catalog_surface_inventory.txt` (catalog inventory proof that no unexpected public success surface appears in the EPIC027 surface family)*

  * *`audit/qa/hde-epic027/checks/po-009/token_inventory.txt` (token inventory proof that no non-canonical token names are introduced)*

  * *`audit/qa/hde-epic027/checks/po-009/primary.log` (governed step log for po-009)*  
* **po-010 runtime functional proof posture**  
  * *`audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt` (same-run prerequisite runtime-log presence proof)*

  * *`audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt` (same-run runtime-surface inventory proof across the changed PF05 proof families)*

  * *`audit/qa/hde-epic027/checks/po-010/primary.log` (governed step log for po-010)*

* **EPIC027 QA manifest pair**

  * `audit/qa/hde-epic027/qa_step_logs_manifest.json`

  * `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`

#### **D.11b EPIC028 Live QA proof anchors for PF05 surfaces**

* **d0 discovery and evidence bootstrap**  
  * `audit/qa/hde-epic028/checks/d0/primary.log` *(governed step log for d0)*  
  * `audit/qa/hde-epic028/checks/d0/runtime_context.txt` *(rails and runtime context capture for the EPIC028 QA root)*  
  * `audit/qa/hde-epic028/checks/d0/cli_health.txt` *(CLI help baseline capture)*  
  * `audit/qa/hde-epic028/checks/d0/services_surfaces.txt` *(surface baseline for `/api/compat/v1`, `/reader`, and `/internal/version`)*  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json` *(EPIC028 QA step manifest)*  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the EPIC028 QA step manifest)*  
* **po-001 internal compatibility canonical, order-neutral, shared governed emission path**  
  * `audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt` *(normalize\_pair and pair\_key proof capture)*  
  * `audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt` *(compat\_public ordering and pair-key proof capture)*  
  * `audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt` *(emit\_public delegation to the canonical serializer)*  
  * `audit/qa/hde-epic028/checks/po-001/primary.log` *(governed step log for po-001)*  
* **po-002 one governed emission path across CLI, Reader, and internal compatibility**  
  * `audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt` *(Reader-side governed emitter snapshot)*  
  * `audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt` *(runtime public envelope routing snapshot)*  
  * `audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt` *(governed emitter allow-list proof snapshot)*  
  * `audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt` *(CLI serializer grep-guard snapshot)*  
  * `audit/qa/hde-epic028/checks/po-002/primary.log` *(governed step log for po-002)*  
* **po-003 CLI compatibility surface presence and deterministic proof-surface verification**  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.txt` *(CLI help capture)*  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt` *(CLI help stderr capture)*  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt` *(CLI help return-code capture)*  
  * `audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt` *(showcompat help-surface presence proof)*  
  * `audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt` *(governed emitter allow-list proof snapshot)*  
  * `audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt` *(CLI serializer grep-guard snapshot)*  
  * `audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt` *(non-zero Reader↔CLI parity artifact probe)*  
  * `audit/qa/hde-epic028/checks/po-003/primary.log` *(governed step log for po-003)*  
* **po-004 public six-part Reader success envelope remains numeric-free**  
  * `audit/qa/hde-epic028/checks/po-004/pytest_stdout.log` *(Reader transport test stdout capture)*  
  * `audit/qa/hde-epic028/checks/po-004/pytest_stderr.log` *(Reader transport test stderr capture)*  
  * `audit/qa/hde-epic028/checks/po-004/pytest_rc.txt` *(Reader transport test return-code capture)*  
  * `audit/qa/hde-epic028/checks/po-004/success_encoding_invariance_snapshot.txt` *(encoding-invariance proof snapshot)*  
  * `audit/qa/hde-epic028/checks/po-004/primary.log` *(governed step log for po-004)*  
* **po-005 governed Reader proof-surface designation**  
  * `audit/qa/hde-epic028/checks/po-006/primary.log (governed step log for po-006)`  
  * `audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt (copied PO-005 PASS lookup proving /reader was resolved before transport proof)`  
  * `audit/qa/hde-epic028/checks/po-006/context_note_pre_po010_moonloop.txt (preserved PO-006 resolved-branch context after bounded Moon Loop remediation)`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stdout.log (Reader transport proof stdout capture)`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stderr.log (Reader transport proof stderr capture)`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_rc.txt (Reader transport proof return-code capture; PASS lane requires 0)`  
* **po-006 governed public success surface transport posture**  
  * `audit/qa/hde-epic028/checks/po-006/primary.log` *(governed step log for po-006)*  
  * `audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt` *(copied PO-005 PASS lookup proving `/reader` was resolved before transport proof)*  
  * `audit/qa/hde-epic028/checks/po-006/blocked_note.txt` *(resolved-branch note artifact for po-006)*  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stdout.log` *(Reader transport proof stdout capture)*  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stderr.log` *(Reader transport proof stderr capture)*  
  * `audit/qa/hde-epic028/checks/po-006/pytest_rc.txt` *(Reader transport proof return-code capture; PASS lane requires `0`)*  
* **po-007 one coherent current-epic acceptance binding**  
  * `audit/qa/hde-epic028/checks/po-007/primary.log` *(governed step log for po-007)*  
  * `audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json` *(current-epic acceptance-map home snapshot)*  
  * `audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt` *(current-epic token-matrix home snapshot)*  
  * `audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt` *(current-epic viability-log home snapshot)*  
  * `audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl` *(machine-mirror binding rows proving the current-epic acceptance binding remains single-home and mirrored)*  
* **po-008 same-change coherence across changed governed evidence families**  
  * `audit/qa/hde-epic028/checks/po-008/primary.log` *(governed step log for po-008)*  
  * `audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt` *(before-snapshot of the authoritative `audit/gates/json_gate/canonical` family)*  
  * `audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt` *(before-snapshot of the legacy-but-governed `audit/gates/canonical_json` family)*  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log` *(canonical gate-writer stdout capture)*  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log` *(canonical gate-writer stderr capture)*  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt` *(canonical gate-writer return-code capture; PASS lane requires `0`)*  
  * `audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt` *(after-snapshot of the authoritative `audit/gates/json_gate/canonical` family)*  
  * `audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt` *(after-snapshot of the legacy-but-governed `audit/gates/canonical_json` family)*  
* **po-009 human ledger, machine ledger, and companion proof refresh coherence**  
  * `audit/qa/hde-epic028/checks/po-009/primary.log` *(governed step log for po-009)*  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stdout.log` *(evidence-index updater stdout capture)*  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stderr.log` *(evidence-index updater stderr capture)*  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.rc.txt` *(evidence-index updater return-code capture; PASS lane requires `0`)*  
  * `audit/qa/hde-epic028/checks/po-009/index_snapshot.json` *(human Evidence Index snapshot used for the coherence check)*  
  * `audit/qa/hde-epic028/checks/po-009/index_sha_snapshot.txt` *(human Evidence Index hash-sentinel snapshot)*  
  * `audit/qa/hde-epic028/checks/po-009/mirror_path_proof_snapshot.txt` *(machine-mirror path-proof snapshot)*  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json` *(current-run step manifest; records `check_id`, `status`, and `log_path` for each executed check)*  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt` *(current-run step-manifest path-proof used by the po-009 coherence check)*  
  * `audit/qa/hde-epic028/checks/po-009/manifest_updater_lookup.txt` *(updater-source lookup proving current-run step-manifest discoverability)*  
  * `audit/qa/hde-epic028/checks/po-009/manifest_human_index_lookup.txt` *(human-index lookup proving current-run step-manifest discoverability)*  
  * `audit/qa/hde-epic028/checks/po-009/manifest_mirror_lookup.txt` *(machine-mirror lookup proving current-run step-manifest discoverability)*  
* **step-0B bounded Moon Loop delta capture**  
  * `audit/qa/hde-epic028/00_meta/delta/patch.diff` *(bounded Moon Loop patch capture used by the po-010 rerun review)*  
  * `audit/qa/hde-epic028/00_meta/delta/changed_files.txt` *(bounded Moon Loop changed-files capture used by the po-010 rerun review)*  
* **po-010 acceptance reporting and repo-supported completion summary**  
  * `audit/qa/hde-epic028/checks/po-010/primary.log` *(governed step log for po-010)*  
  * `audit/qa/hde-epic028/checks/po-010/final_summary.txt` *(repo-supported completion summary with explicit no-claim posture for canon drain and formal close-pack completion)*

  #### **D.11c EPIC029 bounded conjunction and dev-harness proof anchors**

* *`audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md (explicit bounded conjunction route inventory for /reader, /dev/writer/conjunction, /dev/reader/conjunction, /dev/sampler/conjunction, and /internal/dev/sampler)`*  
* *`audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt (governed path-proof for the bounded conjunction JSON surface inventory)`*  
* *`audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md (EPIC029 dev-harness binding coverage artifact for the W-004 closure review, including Codespaces direct-runtime proof and local_dev binding-equivalence for DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler)`*  
* *`audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md.path_proof.txt (governed path-proof for the dev-harness binding coverage artifact)`*  
* *`tests/adapter/test_dev_sampler_http.py (dev sampler APP_ENV gate and ERR_WRITER_FORBIDDEN proof anchor for /internal/dev/sampler)`*

#### **D.11d EPIC029 OPS-01 and epic-close QA proof anchors**

* `audit/ops/hde-epic029/ops-01/commands.txt` *(OPS-01 command transcript for the W-004 dev-harness closure normalization pass)*  
* `audit/ops/hde-epic029/ops-01/stdout.log` *(OPS-01 runtime transcript including the Codespaces direct-runtime proof and the binding-equivalence normalization inputs)*  
* `audit/ops/hde-epic029/ops-01/stderr.log` *(OPS-01 stderr transcript)*  
* `audit/ops/hde-epic029/ops-01/exit_codes.txt` *(OPS-01 exit-code and final normalized disposition summary)*  
* `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md` *(Codespaces closure artifact for the dev sampler harness, closed by direct runtime validation)*  
* `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md` *(local-dev closure artifact for the same dev sampler harness, closed by binding-equivalence with no separate local-dev runtime in this evidence pass)*  
* `audit/ops/hde-epic029/ops-01/binding_disposition.md` *(authoritative environment-by-environment closure record with no mixed-state `not yet closed` posture remaining in OPS-01)*  
* `audit/ops/hde-epic029/ops-01/created_files_sha256.txt` *(OPS-01 checksum ledger for the normalized bounded evidence family)*  
* `audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log` *(canonical epic-close Live QA log bound as PASS evidence for the final in-epic closure review)*  
* `audit/qa/hde-epic029/checks/po-precommit/primary.log` *(canonical precommit QA log bound as PASS evidence)*  
* `audit/qa/hde-epic029/checks/po-postcommit/primary.log` *(canonical postcommit QA log bound as PASS evidence)*

#### **D.11e EPIC029 W-001 blocker-classification proof anchors**

* `audit/ops/hde-epic029/ops-02/W-001_action_log_and_evidence_output_run2.md` *(read-only validation bundle for W-001 classification of the remaining blockers for `HDE-CONJ009.1` and `HDE-CONJ008.1`)*  
* `audit/ops/hde-epic029/ops-02/W-001_classification_run2.md` *(classification artifact for the remaining EPIC029 conjunction blockers)*  
* `audit/ops/hde-epic029/ops-02/commands_w001_run2.txt` *(inspection-command ledger for the W-001 validation run)*  
* `audit/ops/hde-epic029/ops-02/exit_codes_w001_run2.txt` *(exit-code ledger for the W-001 validation run)*  
* `audit/ops/hde-epic029/ops-02/stdout_w001_run2.log` *(stdout capture preserving the inspected evidence excerpts for the W-001 validation run)*  
* `audit/ops/hde-epic029/ops-02/stderr_w001_run2.log` *(stderr capture for the W-001 validation run)*

#### **D.11f EPIC029 Live QA proof anchors for po-001 to po-005**

* **po-001 bounded Conjunction closeout slice / no new public surface**  
  * `audit/qa/hde-epic029/checks/po-001/primary.log` *(canonical step receipt for the bounded Conjunction closeout slice)*  
  * `audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md` *(bounded conjunction inventory snapshot for the approved in-scope surface family)*  
  * `audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json` *(Endpoint Catalog compatibility snapshot anchoring `/reader` and `/dev/writer/conjunction`)*  
  * `audit/qa/hde-epic029/checks/po-001/route_snapshot.txt` *(route-slice snapshot for the bounded conjunction family)*  
* **po-002 canonical JSON discipline across the bounded Conjunction slice**  
  * `audit/qa/hde-epic029/checks/po-002/primary.log` *(canonical step receipt for the bounded canonical-JSON check)*  
  * `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.output.log` *(supplementary canonical-gate output capture)*  
  * `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.rc.txt` *(canonical-gate return-code capture)*  
  * `audit/qa/hde-epic029/checks/po-002/json_gate_structured_record.snapshot.json` *(authoritative canonical JSON gate structured-record snapshot)*  
  * `audit/qa/hde-epic029/checks/po-002/json_canonical_check.snapshot.log` *(legacy canonical-family snapshot log)*  
* **po-003 existing dev writer posture remains typed, numeric-free, and outside formal transport proofs**  
  * `audit/qa/hde-epic029/checks/po-003/primary.log` *(canonical step receipt for the dev writer posture check)*  
  * `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.output.log` *(writer-evidence generator output capture)*  
  * `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.rc.txt` *(writer-evidence generator return-code capture)*  
  * `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.output.log` *(dev writer HTTP proof output capture)*  
  * `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.rc.txt` *(dev writer HTTP proof return-code capture)*  
  * `audit/qa/hde-epic029/checks/po-003/conjunction_write_readback.snapshot.log` *(writer readback snapshot for the dev writer conjunction surface)*  
  * `audit/qa/hde-epic029/checks/po-003/conjunction_writer_summary.snapshot.json` *(writer summary snapshot for the typed dev writer envelope posture)*  
* **po-004 internal sampler harness remains dev/admin-only and refuses prod or misconfigured use**  
  * `audit/qa/hde-epic029/checks/po-004/primary.log` *(canonical step receipt for the internal sampler harness check)*  
  * `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.output.log` *(internal sampler HTTP test output capture)*  
  * `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.rc.txt` *(internal sampler HTTP test return-code capture)*  
  * `audit/qa/hde-epic029/checks/po-004/dev_start_reader.snapshot.sh` *(dev reader harness start snapshot used by the sampler check)*  
  * `audit/qa/hde-epic029/checks/po-004/dev_sampler_healthcheck.snapshot.py` *(dev sampler healthcheck snapshot used by the sampler check)*  
* **po-005 dev harness binding closure for `HDE-CONJ001.4`**  
  * `audit/qa/hde-epic029/checks/po-005/primary.log` *(canonical step receipt for the dev-harness binding closure check)*  
  * `audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt` *(OPS-01 commands snapshot for the binding-closure review)*  
  * `audit/qa/hde-epic029/checks/po-005/exit_codes.snapshot.txt` *(OPS-01 exit-codes snapshot for the binding-closure review)*  
  * `audit/qa/hde-epic029/checks/po-005/codespaces_dev_sampler_url.snapshot.md` *(Codespaces URL snapshot for the published dev sampler binding)*  
  * `audit/qa/hde-epic029/checks/po-005/local_dev_sampler_url.snapshot.md` *(local-dev URL snapshot for the same published dev sampler binding)*  
  * `audit/qa/hde-epic029/checks/po-005/binding_disposition.snapshot.md` *(binding-disposition snapshot for direct runtime closure in Codespaces and binding-equivalence closure in local\_dev)*

#### **D.11g EPIC029 Live QA proof anchors for po-006 to po-008**

* **po-006 formal transport proof surface remains the cataloged Reader success surface**  
  * `audit/qa/hde-epic029/checks/po-006/primary.log` *(canonical step receipt for the Endpoint Catalog proof-boundary check)*  
  * `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.output.log` *(endpoint-catalog test output capture for the formal A7-surface check)*  
  * `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.rc.txt` *(endpoint-catalog test return-code capture for the formal A7-surface check)*  
  * `audit/qa/hde-epic029/checks/po-006/endpoints_catalog.snapshot.json` *(Endpoint Catalog snapshot proving `/reader` remains the formal A7 surface and that dev/internal surfaces are not promoted into the formal transport-proof family)*  
* **po-007 real functional harness proof exists and passes**  
  * `audit/qa/hde-epic029/checks/po-007/primary.log` *(canonical step receipt for the combined functional harness proof)*  
  * `audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log` *(combined functional bundle output capture, including the accepted dependency-preflight line recorded for the pytest-backed step)*  
  * `audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt` *(combined functional bundle return-code capture)*  
* **po-008 final bounded acceptance surface closeout**  
  * `audit/qa/hde-epic029/checks/po-008/primary.log` *(canonical step receipt for the bounded acceptance-surface closeout check)*  
  * `audit/qa/hde-epic029/checks/po-008/acceptance_map.snapshot.json` *(acceptance-map snapshot proving `ready_for_close_binding` for the EPIC029 closeout slice)*  
  * `audit/qa/hde-epic029/checks/po-008/token_evidence_matrix.snapshot.md` *(token-to-evidence snapshot for the bounded EPIC029 closeout surface)*  
  * `audit/qa/hde-epic029/checks/po-008/acceptance_map_viability.snapshot.log` *(viability snapshot proving `COVERED=9 PLANNED=0 MISSING=0` for the EPIC029 acceptance bindings)*  
  * `audit/qa/hde-epic029/checks/po-008/qa_step_logs_manifest.snapshot.json` *(qa-step log manifest snapshot for the EPIC029 closeout review)*  
  * `audit/qa/hde-epic029/checks/po-008/close_report.snapshot.md` *(close-report snapshot for the bounded EPIC029 closeout surface)*  
  * `audit/qa/hde-epic029/checks/po-008/close_manifest.snapshot.json` *(close-manifest snapshot for the bounded EPIC029 closeout surface)*  
  * `audit/qa/hde-epic029/checks/po-008/po_epic_close_live_qa.snapshot.log` *(canonical epic-close Live QA bridge-log snapshot supporting `TESTS_PASS_OK`)*  
  * `audit/qa/hde-epic029/checks/po-008/po_precommit.snapshot.log` *(precommit QA bridge-log snapshot supporting `QA_PRECOMMIT_CHECKLIST_OK`)*  
  * `audit/qa/hde-epic029/checks/po-008/po_postcommit.snapshot.log` *(postcommit QA bridge-log snapshot supporting `QA_POSTCOMMIT_CHECKLIST_OK`)*

#### **D.11h EPIC030 PR-01 normalization and compat proof anchors**

* `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log` *(invalid viewer-preference failure proof for the PR-01 normalization slice)*  
* `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log.path_proof.txt` *(governed path-proof for the invalid viewer-preference proof)*  
* `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log` *(canonicalization compare proof for the PR-01 normalization slice)*  
* `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log.path_proof.txt` *(governed path-proof for the normalization canonicalization proof)*  
* `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json` *(zero-weight handoff proof for the repo-owned normalization-side handoff into sampler/ranker exclusion)*  
* `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json.path_proof.txt` *(governed path-proof for the zero-weight handoff proof)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC030 PR-01 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC030 PR-01 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11i EPIC030 PR-02 dev sampler proof anchors**

* `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt` *(headers proof for the existing `/internal/dev/sampler` dev-only POST surface)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt.path_proof.txt` *(governed path-proof for the dev sampler headers proof)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json` *(canonical JSON body proof for the dev sampler surface)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json.path_proof.txt` *(governed path-proof for the dev sampler body proof)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json` *(IDs-only plus seed metadata proof for the dev sampler surface)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json.path_proof.txt` *(governed path-proof for the seed-only proof)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json` *(two-run identity proof for the dev sampler surface)*  
* `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json.path_proof.txt` *(governed path-proof for the two-run identity proof)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC030 PR-02 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC030 PR-02 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11j EPIC030 PR-03 compat evidence proof anchors**

* `tools/evidence/generate_epic030_pr03_compat_evidence.py` *(governed generator for the EPIC030 PR-03 compat evidence family)*  
* `audit/qa/hde-epic030/pr-03/compat_parity_binding.log` *(byte-level AB↔BA compat parity binding proof)*  
* `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt` *(governed path-proof for the compat parity binding proof)*  
* `audit/qa/hde-epic030/pr-03/compat_identity_binding.log` *(current emitted-byte compat identity-hash binding proof)*  
* `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt` *(governed path-proof for the compat identity binding proof)*  
* `audit/qa/hde-epic030/pr-03/category_order_binding.log` *(Magic-10 category-order and narrative key-table linkage proof)*  
* `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt` *(governed path-proof for the category-order binding proof)*  
* `artifacts/narratives/key_table_10x2.snapshot.json` *(compat narrative key-table snapshot linkage proof)*  
* `artifacts/narratives/key_table_10x2.snapshot.json.path_proof.txt` *(governed path-proof for the narrative key-table snapshot)*  
* `tests/compat/test_compat_public_ab_ba_identity.py` *(targeted compat public AB↔BA identity regression test)*  
* `tests/compat/test_abba_parity.py` *(targeted AB↔BA parity regression test)*  
* `tests/http/test_compat_endpoint_contract.py` *(compat endpoint contract regression test)*  
* `tests/ops/test_evidence_index.py` *(evidence index regression test covering governed bindings)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC030 PR-03 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC030 PR-03 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11k EPIC030 PR-04 band-threshold proof anchors**

* `tools/evidence/generate_epic030_pr04_band_thresholds_evidence.py` *(governed generator for the EPIC030 PR-04 band-threshold evidence family)*  
* `audit/qa/hde-epic030/pr-04/band_edges_binding.log` *(constants-pack band-edge binding proof for compat/admin thresholds)*  
* `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt` *(governed path-proof for the band-edge binding proof)*  
* `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json` *(compact threshold-diff proof for the compat/admin tuning slice)*  
* `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt` *(governed path-proof for the compact threshold-diff proof)*  
* `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt` *(LF-terminated AB↔BA compat identity-hash proof for the threshold/tuning slice)*  
* `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt` *(governed path-proof for the threshold identity-hash proof)*  
* `tests/compat/test_thresholds_constants_pack.py` *(compat threshold constants-pack regression proof)*  
* `tests/evidence/test_epic030_pr04_band_thresholds_evidence.py` *(evidence-generator regression proof that AB↔BA mismatch fails the identity artifact)*  
* `tests/http/test_compat_endpoint_contract.py` *(compat endpoint contract regression proof preserving the public/admin split)*  
* `tests/ops/test_evidence_index.py` *(evidence index regression proof covering governed bindings)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC030 PR-04 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC030 PR-04 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11l EPIC030 PR-05 category-framework proof anchors**

* `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` *(governed generator for the EPIC030 PR-05 category-framework evidence family)*  
* `audit/qa/hde-epic030/pr-05/category_framework_binding.log` *(top-level category-framework binding proof for per-channel mechanics, canonical compare, index binding, mirror binding, and public Reader posture)*  
* `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt` *(governed path-proof for the category-framework binding proof)*  
* `audit/qa/hde-epic030/pr-05/category_canonical_compare.log` *(canonical JSON compare proof for the category-framework evidence family)*  
* `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt` *(governed path-proof for the category canonical-compare proof)*  
* `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json` *(per-channel mechanics snapshot for the category-framework evidence family)*  
* `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt` *(governed path-proof for the per-channel mechanics snapshot)*  
* `tests/evidence/test_epic030_pr05_category_framework_evidence.py` *(category-framework evidence regression proof)*  
* `tests/http/test_compat_endpoint_contract.py` *(compat endpoint contract proof for the existing internal/admin surface)*  
* `tests/http/test_reader_a7_transport.py` *(Reader A7 transport proof anchor preserving the public Reader posture)*  
* `tests/compat/test_compat_public_ab_ba_identity.py` *(compat public AB↔BA identity regression proof)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC030 PR-05 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC030 PR-05 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11m EPIC030 Live QA proof anchors for po-001 to po-005**

* **po-001 surface inventory and no-public-widening proof**  
  * `audit/qa/hde-epic030/checks/po-001/primary.log` *(canonical step receipt for the po-001 surface-inventory PASS evidence)*  
  * `audit/qa/hde-epic030/checks/po-001/surface_inventory.txt` *(surface inventory proving `/api/compat/v1`, `/internal/dev/sampler`, and `/reader` remain seeded route families with no public widening found)*  
  * `audit/qa/hde-epic030/checks/po-001/exit_code.txt` *(exit-code proof for the po-001 PASS mapping)*  
* **po-002 zero-weight handoff through normalization into sampler exclusion**  
  * `audit/qa/hde-epic030/checks/po-002/primary.log` *(canonical step receipt for the po-002 zero-weight handoff PASS evidence)*  
  * `audit/qa/hde-epic030/checks/po-002/pytest_stdout.log` *(pytest transcript for viewer-preference normalization and sampler-core tests)*  
  * `audit/qa/hde-epic030/checks/po-002/generator_stdout.log` *(generator stdout capture for the PR-01 normalization evidence generator)*  
  * `audit/qa/hde-epic030/checks/po-002/pytest_rc.txt` *(pytest return-code proof for po-002)*  
  * `audit/qa/hde-epic030/checks/po-002/generator_rc.txt` *(generator return-code proof for po-002)*  
  * `audit/qa/hde-epic030/checks/po-002/exit_code.txt` *(step exit-code proof for po-002)*  
  * `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json` *(PR-01 proof artifact relied on by po-002; full PR-01 anchor is listed in D.11h)*  
* **po-003 invalid viewer preferences and normalization canonical compare**  
  * `audit/qa/hde-epic030/checks/po-003/primary.log` *(canonical step receipt for the po-003 normalization PASS evidence)*  
  * `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log` *(invalid viewer-preference rejection proof relied on by po-003; full PR-01 anchor is listed in D.11h)*  
  * `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log` *(normalization canonical-compare proof relied on by po-003; full PR-01 anchor is listed in D.11h)*  
* **po-004 dev sampler harness remains non-public, environment-bounded, deterministic, and diagnostic-only**  
  * `audit/qa/hde-epic030/checks/po-004/primary.log` *(canonical step receipt for the po-004 dev sampler harness PASS evidence)*  
  * `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json` *(two-run identity proof relied on by po-004; full PR-02 anchor is listed in D.11i)*  
  * `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt` *(headers and dev/internal bounded-route proof relied on by po-004; full PR-02 anchor is listed in D.11i)*  
* **po-005 compat identity and parity proof**  
  * `audit/qa/hde-epic030/checks/po-005/primary.log` *(canonical step receipt for the po-005 compat identity and parity PASS evidence)*  
  * `audit/qa/hde-epic030/pr-03/compat_identity_binding.log` *(current emitted-byte compat identity binding proof relied on by po-005; full PR-03 anchor is listed in D.11j)*  
  * `audit/qa/hde-epic030/pr-03/compat_parity_binding.log` *(byte-level AB↔BA compat parity binding proof relied on by po-005; full PR-03 anchor is listed in D.11j)*

#### **D.11n EPIC030 po-006 no-user vendor-smoke remediation proof anchors**

* **PR-01 read-only boundary and source-skew discovery**  
  * `PR-01 Remediation HDE-EPIC030.md` *(read-only boundary/source-skew discovery report; source artifact reports no files edited, no tests run, no vendor call, no public route creation, no public Reader widening, no new flag, no serializer-path change, and no PF09 status change recommendation)*  
  * PR-01 no-user discovery facts *(compat boundary report proving current `compat_public` signature and callers, `normalize_pair` caller identity dependency, stale failure-source skew, distinct public Reader versus internal/admin compat proof classes, and the no-user compatibility gap)*  
* **PR-02 birth-only local boundary proof**  
  * `engine/compat/compute.py` *(runtime boundary change allowing sanctioned deterministic internal metadata derivation from complete birth tuples when caller input supplies neither `person_uid` nor `user_id`)*  
  * `tests/compat/test_conjunction_no_user_boundary.py` *(birth-only no-user boundary regression proof)*  
  * `test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable` *(accepted PR-02 local proof name for caller birth-only input, no caller-provided `person_uid`, no caller-provided `user_id`, and AB↔BA stability)*  
  * `tests/compat/test_compat_public_lf_bom.py` *(compat LF and no-BOM regression proof included in the PR-02 broader boundary bundle)*  
  * `tests/compat/test_compat_public_ab_ba_identity.py` *(compat AB↔BA identity regression proof included in the PR-02 broader boundary bundle)*  
  * `tests/http/test_compat_endpoint_contract.py` *(compat endpoint contract proof preserving the existing internal/admin surface)*  
  * `tests/http/test_endpoint_catalog.py` *(Endpoint Catalog proof included in the PR-02 broader boundary bundle)*  
  * `tests/adapter/test_compat_http_parity.py` *(adapter compat HTTP parity proof included in the PR-02 broader boundary bundle)*  
  * `tests/adapter/test_compat_http_dev.py` *(adapter compat dev proof included in the PR-02 broader boundary bundle)*  
  * `tests/adapter/test_compat_writer_transport.py` *(compat writer transport proof included in the PR-02 broader boundary bundle)*  
  * PR-02 vendor-smoke non-run proof *(PR-02 report states no vendor command was run by Codex and that controlled vendor-backed smoke remains PO-only)*  
* **OPS-01 discovery and blocker-classification anchors**  
  * `audit/ops/hde-epic030/ops-01/commands.txt` *(OPS-01 command ledger for discovery commands and remediation edit actions)*  
  * `audit/ops/hde-epic030/ops-01/python_version.txt` *(Python preflight capture for OPS-01 discovery)*  
  * `audit/ops/hde-epic030/ops-01/python_version.stderr` *(stderr capture for the Python preflight)*  
  * `audit/ops/hde-epic030/ops-01/pytest_version.txt` *(pytest preflight capture for OPS-01 discovery)*  
  * `audit/ops/hde-epic030/ops-01/pytest_version.stderr` *(stderr capture for the pytest preflight)*  
  * `audit/ops/hde-epic030/ops-01/grep_path.txt` *(grep path preflight capture for OPS-01 discovery)*  
  * `audit/ops/hde-epic030/ops-01/grep_path.stderr` *(stderr capture for the grep path preflight)*  
  * `audit/ops/hde-epic030/ops-01/hdctl_path.txt` *(hdctl availability capture for OPS-01 discovery)*  
  * `audit/ops/hde-epic030/ops-01/hdctl_path.stderr` *(stderr capture for hdctl availability)*  
  * `audit/ops/hde-epic030/ops-01/hdctl_help.txt` *(hdctl help capture for OPS-01 discovery)*  
  * `audit/ops/hde-epic030/ops-01/hdctl_help.stderr` *(stderr capture for hdctl help)*  
  * `audit/ops/hde-epic030/ops-01/showcompat_help.txt` *(showcompat help capture for the controlled vendor smoke command-discovery boundary)*  
  * `audit/ops/hde-epic030/ops-01/showcompat_help.stderr` *(stderr capture for showcompat help)*  
  * `audit/ops/hde-epic030/ops-01/env_presence.json` *(presence-only boolean environment snapshot for OPS-01; secret values are not persisted)*  
  * `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt` *(OPS-01 command-candidate proof for the controlled vendor-backed no-user smoke; unresolved sentinel means OPS-02 remains `TOOLING_BLOCKED`)*  
  * `audit/ops/hde-epic030/ops-01/discovery_summary.md` *(OPS-01 discovery posture and blocker-classification proof)*  
  * `audit/ops/hde-epic030/ops-01/files_sha256.txt` *(checksum ledger for OPS-01 captured files)*  
* **OPS-02 controlled vendor-backed no-user smoke anchors**  
  * `audit/ops/hde-epic030/ops-02/vendor_command.txt` *(exact executable `hdctl showcompat --source vendor` birth-only command used for the controlled smoke)*  
  * `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json` *(birth values substituted into the controlled smoke command, with no app user IDs, no `person_uid`, no `user_id`, and vendor execution true)*  
  * `audit/ops/hde-epic030/ops-02/redacted_env_presence.json` *(presence-only boolean environment capture for vendor and rails inputs; secret values are not persisted)*  
  * `audit/ops/hde-epic030/ops-02/target_disposition.md` *(target classification proof for `CLI_LOCAL_VENDOR_SMOKE`; hosted-service PF07 facts are not required for this local CLI vendor-source smoke)*  
  * `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md` *(runtime binding proof that OPS-02 exercised a runtime containing the PR-02 birth-only no-user remediation)*  
  * `audit/ops/hde-epic030/ops-02/request_summary.txt` *(OPS-02 controlled-smoke request summary proving explicit vendor source, birth-only input shape, no `person_uid`, no `user_id`, no app user ID, target posture, safe secret posture, command source, and PO proceed authorization)*  
  * `audit/ops/hde-epic030/ops-02/stdout.json` *(non-empty parseable stdout capture for the controlled vendor-backed no-user smoke)*  
  * `audit/ops/hde-epic030/ops-02/stderr.log` *(stderr capture for the controlled vendor-backed no-user smoke; empty stderr is allowed when recorded)*  
  * `audit/ops/hde-epic030/ops-02/exit_code.txt` *(runtime exit-code proof for the controlled vendor-backed no-user smoke)*  
  * `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md` *(parseability proof for `stdout.json`)*  
  * `audit/ops/hde-epic030/ops-02/stdout.json.sha256` *(sha256 sidecar for the OPS-02 stdout capture)*  
  * `audit/ops/hde-epic030/ops-02/execution_classification.md` *(execution classification proof for the controlled vendor-backed no-user smoke)*  
  * `audit/ops/hde-epic030/ops-02/result_summary.md` *(runtime result summary classifying OPS-02 as `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, or `TOOLING_BLOCKED`, and preserving the implementation-validation-only non-claim posture)*  
  * `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md` *(OPS-02 prerequisite-to-canon completion matrix)*  
  * `audit/ops/hde-epic030/ops-02/files_sha256.txt` *(checksum ledger for OPS-02 evidence files, including the accepted deterministic self-reference row required by the po-006 validator)*  
  * `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md` *(consolidated OPS-02 action log and evidence report used by po-006)*  
  * Absence of caller-provided `person_uid`, caller-provided `user_id`, app user IDs, and DB-backed user BodyGraphs from the public or birth-facing no-user proof *(proof obligation for the PF05 no-user boundary; exact evidence path is owned by the po-006 QA plan block)*  
  * OPS-02 remains implementation-validation evidence only; it is not QA PASS, not Live QA completion, not a PF09 status change, and not epic closure.

#### **D.11o EPIC030 Live QA proof anchors for po-006 to po-011**

* **po-006 public numeric-free compatibility and OPS-02 validation proof**  
  * `audit/qa/hde-epic030/checks/po-006/primary.log` *(canonical step receipt for the po-006 PASS evidence under closed deterministic QA rails)*  
  * `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt` *(public Reader bands-only and numeric-free proof for the user-facing compatibility posture)*  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json` *(OPS-02 evidence validator proof with status `PASS`)*  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.stderr` *(stderr capture for the OPS-02 evidence validator; empty stderr is allowed when recorded)*  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation_rc.txt` *(return-code proof for the OPS-02 evidence validator)*  
  * `audit/qa/hde-epic030/checks/po-006/pytest_rc.txt` *(pytest return-code proof for the public compatibility checks)*  
  * `audit/qa/hde-epic030/checks/po-006/grep_rc.txt` *(grep return-code proof for the numeric-free marker)*  
  * `audit/qa/hde-epic030/checks/po-006/exit_code.txt` *(step exit-code proof for po-006)*  
  * `audit/qa/hde-epic030/pr-05/category_framework_binding.log` *(PR-05 binding log relied on by po-006 for the public numeric-free marker)*  
  * `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md` *(consolidated OPS-02 report relied on by po-006)*  
  * `audit/ops/hde-epic030/ops-02/files_sha256.txt` *(Moon Loop-remediated checksum ledger relied on by the po-006 OPS-02 validator)*  
* **po-007 threshold ownership and band-edge proof**  
  * `audit/qa/hde-epic030/checks/po-007/primary.log` *(canonical step receipt for the po-007 PASS evidence)*  
  * `audit/qa/hde-epic030/checks/po-007/threshold_ownership.txt` *(threshold ownership proof naming the existing threshold source files and showing no duplicate threshold home)*  
  * `audit/qa/hde-epic030/checks/po-007/generator_rc.txt` *(generator return-code proof for po-007)*  
  * `audit/qa/hde-epic030/checks/po-007/preflight.log` *(preflight proof for required repo loci)*  
  * `audit/qa/hde-epic030/checks/po-007/exit_code.txt` *(step exit-code proof for po-007)*  
  * `audit/qa/hde-epic030/checks/po-007/generator_stdout.log` *(generator stdout capture for po-007)*  
  * `audit/qa/hde-epic030/checks/po-007/generator_stderr.log` *(generator stderr capture for po-007)*  
  * `audit/qa/hde-epic030/pr-04/band_edges_binding.log` *(band-edge binding proof showing `engine.compat.thresholds.THRESHOLDS_V1`, edges `24,49,74,100`, and `status: PASS`)*  
* **po-008 band-threshold comparison and identity proof**  
  * `audit/qa/hde-epic030/checks/po-008/primary.log` *(canonical step receipt for the po-008 PASS evidence)*  
  * `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json` *(threshold-diff proof relied on by po-008)*  
  * `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt` *(implemented identity-hash proof relied on by po-008)*  
  * The stale plan filename `audit/qa/hde-epic030/pr-04/band_thresholds_identity.log` is not a final PF05 proof anchor; use `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt` for the PR-04 identity proof.  
* **po-009 category-framework binding, canonical compare, and per-channel mechanics proof**  
  * `audit/qa/hde-epic030/checks/po-009/primary.log` *(canonical step receipt for the po-009 PASS evidence)*  
  * `audit/qa/hde-epic030/checks/po-009/exit_code.txt` *(step exit-code proof for po-009)*  
  * `audit/qa/hde-epic030/checks/po-009/generator_rc.txt` *(generator return-code proof for po-009)*  
  * `audit/qa/hde-epic030/checks/po-009/pytest_rc.txt` *(pytest return-code proof for po-009)*  
  * `audit/qa/hde-epic030/checks/po-009/pytest_stdout.log` *(pytest stdout proof for po-009)*  
  * `audit/qa/hde-epic030/pr-05/category_framework_binding.log` *(category-framework binding proof with public numeric-free posture, index binding, mirror binding, per-channel mechanics status, canonical compare status, and overall PASS)*  
  * `audit/qa/hde-epic030/pr-05/category_canonical_compare.log` *(category canonical-compare proof relied on by po-009)*  
  * `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json` *(per-channel mechanics proof relied on by po-009)*  
* **po-010 generated-proof fail-closed coverage**  
  * `audit/qa/hde-epic030/checks/po-010/primary.log` *(canonical step receipt for the final po-010 PASS evidence after remediation)*  
  * `audit/qa/hde-epic030/checks/po-010/exit_code.txt` *(step exit-code proof for po-010)*  
  * `audit/qa/hde-epic030/checks/po-010/fail_closed_visibility.txt` *(visibility proof that PR-01 through PR-03, PR-04, and PR-05 generated proof families are proven for fail-closed behavior)*  
  * `audit/qa/hde-epic030/checks/po-010/pytest_rc.txt` *(pytest return-code proof for po-010)*  
  * `audit/qa/hde-epic030/checks/po-010/pytest_stdout.log` *(pytest stdout proof for the po-010 fail-closed suite)*  
  * `tests/evidence/test_epic030_pr01_pr03_fail_closed_evidence.py` *(remediation test file proving PR-01 through PR-03 fail-closed evidence behavior)*  
  * `tests/evidence/test_epic030_pr04_band_thresholds_evidence.py` *(PR-04 fail-closed evidence regression proof)*  
  * `tests/evidence/test_epic030_pr05_category_framework_evidence.py` *(PR-05 fail-closed evidence regression proof)*  
* **po-011 PR-slice traceability proof**  
  * `audit/qa/hde-epic030/checks/po-011/primary.log` *(canonical step receipt for the po-011 traceability PASS evidence)*  
  * `audit/qa/hde-epic030/checks/po-011/traceability_summary.json` *(traceability proof that required PR-slice artifacts are present, indexed, and mirrored)*  
  * `audit/qa/hde-epic030/checks/po-011/exit_code.txt` *(step exit-code proof for po-011)*

#### **D.11p EPIC030 Live QA proof anchors for po-012 to po-017 and final QA closeout**

* **po-012 reused-history and active-scope classification**  
  * `audit/qa/hde-epic030/checks/po-012/primary.log` *(canonical step receipt for the po-012 PASS evidence after Step-0B precondition remediation)*  
  * `audit/qa/hde-epic030/00_meta/doc_deltas.md` *(Step-0B precondition artifact confirming doc-delta surfaces before final po-012 execution)*  
* **po-013 source-of-truth posture and drainage separation**  
  * `audit/qa/hde-epic030/checks/po-013/primary.log` *(canonical step receipt for the po-013 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic030/checks/po-013/source_of_truth_posture.txt` *(fixed-schema source-of-truth posture proof separating repo-supported completion, canon-drain completion, and formal close-pack completion)*  
* **po-014 all-slice coherence**  
  * `audit/qa/hde-epic030/checks/po-014/primary.log` *(canonical step receipt for the po-014 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic030/checks/po-014/all_slice_coherence.json` *(all-slice coherence proof confirming prior po-001 through po-013 primary logs and required PR-01 through PR-05 artifacts are present and coherent)*  
  * `audit/qa/hde-epic030/checks/po-014/exit_code.txt` *(step exit-code proof for po-014)*  
* **po-015 baseline discovery and execution context**  
  * `audit/qa/hde-epic030/checks/po-015/primary.log` *(canonical step receipt for the po-015 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic030/checks/po-015/discovery.json` *(baseline discovery/context artifact proving rails, paths, and surfaces are structurally present and typed)*  
  * `audit/qa/hde-epic030/checks/po-015/discovery_validation.txt` *(parseability and structure-validation proof for the po-015 discovery artifact)*  
* **po-016 final QA interpretation and QA RCA**  
  * `audit/qa/hde-epic030/checks/po-016/primary.log` *(canonical step receipt for the po-016 PASS evidence under closed deterministic rails)*  
  * `audit/EPIC-030_QA_RCA.md` *(QA RCA and interpretation artifact containing Coverage vs QA Plan, Findings classification, Outcome meaning, evidence support, canon follow-up, and closeout-readiness recommendation without formal close-pack overclaim)*  
* **po-017 documentation-drainage non-blocker posture**  
  * `audit/qa/hde-epic030/checks/po-017/primary.log` *(canonical step receipt for the po-017 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic030/checks/po-017/documentation_drainage_posture.txt` *(documentation-drainage posture proof recording `drainage_blocker: False`, `pf09_2_drainage_required_before_otherwise_proven_QA_pass: False`, and explicit real truth-and-proof blocker categories)*  
* **Final QA closeout review and caveat posture**  
  * `audit/EPIC-030_QA_RCA.md` *(final QA closeout source for root-cause analysis, remediation-loop assessment, implementation-gap summary, and READY WITH CAVEATS recommendation)*  
  * The EPIC030 final QA closeout posture remains a QA closeout-readiness recommendation. It is not a claim that PF09.2 drainage is complete, and it is not a claim that formal close-pack completion is proven beyond the surfaced close-pack artifacts and separate OPS review.

#### **D.11q EPIC030 OPS-03 close-pack evidence-packaging proof anchors**

* **OPS-03 scope and execution posture**  
  * `audit/ops/hde-epic030/ops-03/commands.txt` *(corrected, labeled, replayable OPS-03 command transcript using executable `python - <<'PY'` heredoc task blocks)*  
  * `audit/ops/hde-epic030/ops-03/commands_prev_invalid.txt` *(audit-trail preservation of the prior invalid command transcript)*  
  * `audit/ops/hde-epic030/ops-03/stdout.log` *(labeled stdout capture for manifest validation, close-report validation, path-proof generation and validation, inventory generation, checksum generation, and final comprehensive validation)*  
  * `audit/ops/hde-epic030/ops-03/stderr.log` *(stderr capture for OPS-03; empty stderr is allowed when represented by the empty-file SHA-256)*  
  * `audit/ops/hde-epic030/ops-03/exit_codes.txt` *(labeled exit-code ledger mapping critical OPS-03 task labels to exit code 0\)*  
  * `audit/ops/hde-epic030/ops-03/created_files_sha256.txt` *(checksum ledger for created and refreshed OPS-03 files)*  
* **OPS-03 validation and inventory**  
  * `audit/ops/hde-epic030/ops-03/final_validation.log` *(final comprehensive validation proof for file existence, manifest validation, close report validation, path-proof validation, final inventory validation, and OPS-03 evidence-bundle validation)*  
  * `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md` *(three-column final evidence inventory proving 18 governed artifacts present and 0 missing)*  
  * `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md.path_proof.txt` *(governed path-proof for the final evidence inventory)*  
* **Canonical close-pack pair and supporting bindings**  
  * `audit/EPIC-030_close_report.md` *(canonical EPIC030 close report surfaced by OPS-03 with explicit closure-state separation)*  
  * `audit/EPIC-030_close_report.md.path_proof.txt` *(governed path-proof for the EPIC030 close report)*  
  * `audit/EPIC-030_MANIFEST.json` *(canonical EPIC030 close manifest with named `key_outputs` bindings for close report, manifest, acceptance map, QA RCA, QA step manifest, token matrix, doc deltas, drain targets, final inventory, and checksum ledger)*  
  * `audit/EPIC-030_MANIFEST.json.path_proof.txt` *(governed path-proof for the EPIC030 close manifest)*  
  * `docs/acceptance_map_epic030.json` *(acceptance-map binding included in the surfaced close-pack evidence family)*  
  * `audit/qa/hde-epic030/token_evidence_matrix.md` *(token-to-evidence matrix included in the surfaced close-pack evidence family)*  
  * `audit/qa/hde-epic030/qa_step_logs_manifest.json` *(QA step manifest included in the surfaced close-pack evidence family)*  
  * `audit/docdeltas/hde-epic030_doc_deltas.md` *(doc-delta ledger surfaced by OPS-03)*  
  * `audit/docdeltas/hde-epic030_drain_targets.md` *(drain-targets ledger surfaced by OPS-03)*  
* **OPS-03 non-overclaim posture**  
  * OPS-03 is evidence packaging and close-pack surfacing only. It does not rerun QA, execute vendor calls, modify implementation, edit PF-Canon, claim PF09.2 drainage, create new acceptance claims, or authorize an immediate PF09.2 status change by itself.

#### **D.11r EPIC031 PR-01 SAFE rails provider-gate proof anchors**

* `artifacts/vendor/policies_pinned.md` *(provider policy evidence for pinned timeouts, bounded attempts, deterministic backoff, and non-retry classification for non-200 statuses outside `4xx` and `5xx`)*  
* `artifacts/vendor/policies_pinned.md.path_proof.txt` *(governed path-proof for the pinned provider policy evidence)*  
* `artifacts/vendor/retry_after_parse.log` *(deterministic `Retry-After` parsing proof for delta-seconds, HTTP-date, invalid, unsupported, and overflow values)*  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json` *(governed PR-01 proof for open-rails provider-gate policy, no-live-vendor posture, non-retry `http_status_other` handling, and classified side-effect families)*  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json.path_proof.txt` *(governed path-proof for the PR-01 open-rails policy proof)*  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json` *(governed PR-01 proof for retry, backoff, 429 handling, `Retry-After`, and non-4xx non-5xx `PROVIDER_ERROR` mapping)*  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json.path_proof.txt` *(governed path-proof for the retry/backoff proof)*  
* `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json` *(governed PR-01 proof that local mocked or fixture-backed provider results are the only allowed open exception in the no-live-call proof lane)*  
* `tools/evidence/generate_epic031_pr01_provider_gate.py` *(governed evidence generator for the PR-01 provider-gate proof family)*  
* `tests/bodygraph/test_vendor_client.py` *(vendor-client regression proof for retry classes, 429 behavior, non-redirect handling, default request-path classification, and keys-only logging where applicable)*  
* `tests/bodygraph/test_resolver_vendor.py` *(resolver-vendor regression proof for the PR-01 provider-gate slice)*

#### **D.11s EPIC031 PR-02 SAFE rails observability proof anchors**

* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json` *(governed PR-02 evidence proving bounded labels, route observability, timeout-profile observability, and observed failure classes)*  
* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json.path_proof.txt` *(governed path-proof for the bounded-label observability proof)*  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json` *(governed PR-02 evidence proving keys-only logs, no payload body, no plaintext secret, no raw secret header, no forbidden hits, and no key violations)*  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json.path_proof.txt` *(governed path-proof for the keys-only log-redaction proof)*  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log` *(governed deterministic redaction scan for PR-02 vendor log posture)*  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log.path_proof.txt` *(governed path-proof for the redaction scan)*  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl` *(PR-specific governed vendor keys-only JSONL sample; do not overwrite shared DB-bridge log evidence with this vendor sample)*  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl.path_proof.txt` *(governed path-proof for the PR-specific vendor keys-only sample)*  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt` *(PR-specific governed vendor rails-scope artifact proving closed deterministic rails, no live vendor calls, and detected vendor-route scope for PR-02)*  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt.path_proof.txt` *(governed path-proof for the PR-specific vendor rails-scope artifact)*  
* `ci/jobs/logs_keys_only_redaction.yml` *(local CI job definition for keys-only log-redaction proof under closed rails)*  
* `tools/evidence/generate_epic031_pr02_log_posture.py` *(governed evidence generator for the PR-02 bounded-label, redaction, scan, vendor-sample, and vendor-scope evidence family)*  
* `tools/evidence/update_evidence_index.py` *(single-writer evidence-index tooling binding the PR-02 evidence rows to the Human Evidence Index and Machine Evidence Mirror)*  
* `tests/evidence/test_evidence_skeleton.py` *(evidence skeleton regression proof preserving non-EPIC020 mirror schema validation while scoping the EPIC020 token-roster assertion to EPIC020 records)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the EPIC031 PR-01 and PR-02 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the Human Evidence Index update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the EPIC031 PR-01 and PR-02 evidence rows)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the Machine Evidence Mirror update)*

#### **D.11t EPIC031 Live QA proof anchors for Step-0A through po-006**

* **Step-0A discovery and harness setup**  
  * `audit/qa/hde-epic031/00_meta/live_qa_harness.py` *(Live QA harness used by EPIC031 check execution)*  
  * `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log` *(canonical step receipt for Step-0A PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json` *(check-root discovery sidecar for rails, surfaces, and seed-path presence)*  
  * The conflicting plan action reference to `audit/qa/hde-epic031/00_meta/discovery.json` is not a PF05 proof anchor for Step-0A; use the check-root discovery path above.  
* **Step-0B doc-delta capture**  
  * `audit/docdeltas/hde-epic031_doc_deltas.md` *(repo-root doc-delta surface for EPIC031)*  
  * `audit/qa/hde-epic031/00_meta/doc_deltas.md` *(QA-root doc-delta surface for EPIC031, including later PO-006 remediation notes where applicable)*  
  * `audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log` *(canonical step receipt for Step-0B PASS evidence)*  
* **po-001 Fermentation first-slice scope boundary**  
  * `audit/qa/hde-epic031/checks/po-001/primary.log` *(canonical step receipt for po-001 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-001/result.json` *(scope-boundary proof that no EPIC031 public surface was added and that later vendor-version, database, router, public-surface, close-pack, and acceptance expansion remain excluded for this slice)*  
  * `audit/qa/hde-epic031/pr-03/evidence_family_map.json` *(scope-guardrail companion relied on by po-001 for acceptance-token and follow-up-scope non-expansion facts)*  
  * `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json` *(scope-guardrail companion relied on by po-001 for HDAPI v2 runtime, live-vendor, and PO-only smoke non-execution facts)*  
* **po-002 closed-by-default provider access and bounded opening**  
  * `audit/qa/hde-epic031/checks/po-002/primary.log` *(canonical step receipt for po-002 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-002/result.json` *(closed-default refusal, bounded opening, provider-test, and no-live-vendor proof for po-002)*  
  * `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt` *(local deterministic vendor-scope proof relied on by po-002)*  
* **po-003 deterministic typed provider refusal before unsafe input or ingest**  
  * `audit/qa/hde-epic031/checks/po-003/primary.log` *(canonical step receipt for po-003 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-003/result.json` *(typed provider-refusal proof for closed SAFE rails before unsafe provider input or ingest)*  
  * `engine/bodygraph/resolver.py` *(resolver control-flow evidence relied on by po-003 for refusal before vendor input resolution)*  
  * `tests/bodygraph/test_resolver_vendor.py` *(regression proof relied on by po-003 for closed SAFE rails refusal before input or ingest)*  
* **po-004 pinned policy, non-success classification, and retry/backoff proof**  
  * `audit/qa/hde-epic031/checks/po-004/primary.log` *(canonical step receipt for po-004 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-004/result.json` *(non-success classification, pinned-attempts, and retry/backoff artifact-presence proof for po-004)*  
* **po-005 Retry-After, typed 429, and rate-limit proof**  
  * `audit/qa/hde-epic031/checks/po-005/primary.log` *(canonical step receipt for po-005 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-005/result.json` *(Retry-After delta parsing, 429 source mapping, and typed 429 evidence proof for po-005)*  
* **po-006 keys-only observability and Moon Loop remediation**  
  * `audit/qa/hde-epic031/checks/po-006/primary.log` *(canonical step receipt for final po-006 PASS evidence after Moon Loop remediation)*  
  * `audit/qa/hde-epic031/checks/po-006/result.json` *(allowed-keys, payload-body-absence, plaintext-secret-absence, and raw-secret-header-absence proof for po-006)*  
  * `audit/qa/hde-epic031/remediation/moon_loop/patch.diff` *(Moon Loop remediation patch proving the QA-created harness predicate was aligned to canonical redaction schema fields)*  
  * `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt` *(Moon Loop changed-files proof with sha256 values for the changed harness and po-006 current-state evidence)*  
  * The po-006 Moon Loop remediation is accepted only as QA-harness correction evidence. It does not create new PF05 bytes, new public routes, new acceptance tokens, new vendor runtime behavior, or a substitute for the PR-02 governed keys-only proof family listed in **D.11s**.

#### **D.11u EPIC031 Live QA proof anchors for po-007 to po-009**

* **po-007 sensitive provider data absence from QA-visible diagnostics**  
  * `audit/qa/hde-epic031/checks/po-007/primary.log` *(canonical step receipt for po-007 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-007/result.json` *(redaction-scan and no-live-vendor-scope proof for po-007, including `scan_present: true`, `scope_live_forbidden: true`, and `status: PASS`)*  
* **po-008 governed human and machine evidence coherence**  
  * `audit/qa/hde-epic031/checks/po-008/primary.log` *(canonical step receipt for final po-008 PASS evidence after Moon Loop remediation)*  
  * `audit/qa/hde-epic031/checks/po-008/result.json` *(evidence-coherence proof for po-008, including `all_commands_green: true`, `coherence_status: PASS`, and `status: PASS`)*  
  * `audit/qa/hde-epic031/remediation/moon_loop/patch.diff` *(po-008 Moon Loop patch capture for governed coherence/index remediation)*  
  * `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt` *(po-008 Moon Loop changed-files proof for refreshed coherence/index artifacts, hash sentinels, Machine Mirror artifacts, path proofs, and compat AB/BA filesystem mtime normalization with bytes unchanged)*  
* **po-009 machine mirror and family-map alignment**  
  * `audit/qa/hde-epic031/checks/po-009/primary.log` *(canonical step receipt for po-009 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-009/result.json` *(machine-mirror and family-map alignment proof for po-009, including `family_map_present: true`, `machine_mirror_present: true`, `mirror_mentions_epic031: true`, and `status: PASS`)*

#### **D.11v EPIC031 Live QA proof anchors for po-010 to po-012**

* **po-010 generated-proof fail-closed posture**  
  * `audit/qa/hde-epic031/checks/po-010/primary.log` *(canonical step receipt for po-010 PASS evidence after the prior PR-01 check-mode blocker was resolved)*  
  * `audit/qa/hde-epic031/checks/po-010/result.json` *(generated-proof fail-closed proof for po-010, including `pr01_generator_check_mode_present: true`, PR-02 generator check success, PR-03 coherence check success, and `status: PASS`)*  
  * `tools/evidence/generate_epic031_pr01_provider_gate.py` *(PR-01 provider-gate generator check-mode proof relied on by po-010)*  
* **po-011 acceptance-claim boundary**  
  * `audit/qa/hde-epic031/checks/po-011/primary.log` *(canonical step receipt for po-011 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-011/result.json` *(acceptance-claim boundary proof for po-011, including no claimed tokens, `claims_limited_to_evidence_scope: true`, and the note that missing acceptance map or token matrix remains close-stage posture rather than runtime behavior failure)*  
* **po-012 active Fermentation subtask supportability without PF09.5 drainage claim**  
  * `audit/qa/hde-epic031/checks/po-012/primary.log` *(canonical step receipt for po-012 PASS evidence)*  
  * `audit/qa/hde-epic031/checks/po-012/result.json` *(supportability proof for HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4 from current evidence, with `pf09_5_drain_claimed: false` and `status: PASS`)*

#### **D.11w EPIC031 Live QA proof anchors for po-013 to po-015**

* **po-013 reused foundation remains history-only**  
  * `audit/qa/hde-epic031/checks/po-013/primary.log` *(canonical step receipt for po-013 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-013/result.json` *(reused-foundation proof for po-013, including active-slice-only posture, `new_implementation_claim_for_reused_foundation: false`, `reused_foundation_classification: history_only`, and `status: PASS`)*  
* **po-014 implementation readiness is not final QA outcome**  
  * `audit/qa/hde-epic031/checks/po-014/primary.log` *(canonical step receipt for po-014 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-014/result.json` *(prior-log and readiness-separation proof for po-014, including `all_prior_logs_present: true`, `implementation_readiness_is_final_qa_outcome: false`, and `status: PASS`)*  
* **po-015 truth-class and drainage separation**  
  * `audit/qa/hde-epic031/checks/po-015/primary.log` *(canonical step receipt for po-015 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-015/result.json` *(truth-class separation proof for po-015, including implementation readiness, QA readiness, final QA outcome, and documentation drainage as separate, with `pf09_5_drainage_required_before_qa_pass: false`)*

#### **D.11x EPIC031 Live QA proof anchors for po-016 to po-018**

* **po-016 vendor-version runtime conformance is not completed by this epic**  
  * `audit/qa/hde-epic031/checks/po-016/primary.log` *(canonical step receipt for po-016 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-016/result.json` *(vendor-version runtime non-claim proof for po-016, including `vendor_version_runtime_conformance_claimed: false`, `no_live_vendor_policy: true`, and `status: PASS`)*  
* **po-017 live vendor behavior is not claimed from local proof**  
  * `audit/qa/hde-epic031/checks/po-017/primary.log` *(canonical step receipt for po-017 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-017/result.json` *(live-vendor-behavior non-claim proof for po-017, including `live_vendor_behavior_claimed: false`, `live_vendor_calls_forbidden_recorded: true`, and `status: PASS`)*  
* **po-018 Live QA stays QA, not implementation, remediation, or closeout action**  
  * `audit/qa/hde-epic031/checks/po-018/primary.log` *(canonical step receipt for po-018 PASS evidence under closed deterministic rails)*  
  * `audit/qa/hde-epic031/checks/po-018/result.json` *(Live QA proof-only boundary proof for po-018, including `implementation_performed_by_live_qa: false`, `remediation_performed_by_live_qa: false`, `closeout_action_performed_by_live_qa: false`, and `live_qa_role: prove_current_results_only`)*

#### **D.11y EPIC032 PR-01 narrative-router parity and evidence-indexing proof anchors**

* `tools/evidence/generate_epic032_pr01_router_evidence.py` *(governed generator for HDE-EPIC032 PR-01 router coverage, AB↔BA and two-run identity, and CLI/HTTP parity proof)*  
* `audit/gates/narratives/keys_10x4.table.json` *(router coverage snapshot proving the 10 category by 4 band key table, canonical JSON, and missing-key cases)*  
* `audit/gates/narratives/keys_10x4.table.json.path_proof.txt` *(governed path-proof for the router coverage snapshot)*  
* `artifacts/narratives/router/parity_abba.log` *(AB↔BA and two-run identity log for router outputs; keys-only and no-prose evidence)*  
* `artifacts/narratives/router/parity_abba.log.path_proof.txt` *(governed path-proof for the AB↔BA and two-run identity log)*  
* `artifacts/narratives/router/cli_http_parity.log` *(CLI/HTTP parity log for router responses where parity is defined, including 120 passing parity rows)*  
* `artifacts/narratives/router/cli_http_parity.log.path_proof.txt` *(governed path-proof for the CLI/HTTP parity log)*  
* `tests/unit/test_narratives_router.py` *(router matrix, supported tuple behavior, missing-key fail-closed behavior, two-run identity, and AB↔BA coherence proof anchor)*  
* `tests/cli/test_aux_preview.py` *(CLI narrative preview proof anchor for the PR-01 validation roster)*  
* `tests/transport/test_aux_narrative.py` *(transport narrative proof anchor for the PR-01 validation roster)*  
* `tools/evidence/update_evidence_index.py` *(single-writer evidence-index tooling that carries the corrected HDE-EPIC032 PR-01 token posture)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the HDE-EPIC032 PR-01 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-01 Human Evidence Index update)*  
* `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
* `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the HDE-EPIC032 PR-01 evidence rows; the router key-table row carries only `JSON_CANONICAL_CHECK_OK`, while parity rows retain `CLI_READER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`, and `COMPOSITE_ABBA_IDENTITY_OK`)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-01 Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel update)*  
* The unsupported `NARR_REGISTRY_CLOSURE_OK` claim is not a PF05 acceptance anchor for this PR-01 evidence family; the corrected key-table posture is `JSON_CANONICAL_CHECK_OK` only.  
* This PR-01 proof family does not create a new public Reader route, public Reader flag, public payload field, public numeric output, or public narrative text contract.

#### **D.11z EPIC032 PR-02 narrative registry diff, pack identity, and evidence-indexing proof anchors**

* `tools/evidence/generate_narrative_registry_diff.py` *(governed generator for HDE-EPIC032 PR-02 narrative registry diff, pack identity, and fail-closed manifest and key-grid validation)*  
* `tools/evidence/run_sanity_pipeline.py` *(sanity-pipeline proof anchor that runs narrative registry generation and generator check before evidence updater operations)*  
* `tests/unit/test_narratives_loader.py` *(narrative loader and generator proof anchor for canonical rendering, keys-only posture, pack identity, supported category and band validation, full tuple-grid validation, duplicate rejection, and fail-closed negative cases)*  
* `tests/evidence/test_sanity_pipeline.py` *(pipeline-ordering proof anchor that prevents stale registry diff or pack identity evidence from being accepted by index checks alone)*  
* `audit/gates/narratives/registry.diff.json` *(canonical PR-02 registry diff artifact for manifest changes, keys-only registry counts, no-prior-baseline diff state, and HDE-FERM003.2 scope)*  
* `audit/gates/narratives/registry.diff.json.path_proof.txt` *(governed path-proof for the PR-02 registry diff artifact)*  
* `audit/gates/narratives/pack_identity.txt` *(pack identity proof with canonical manifest SHA, manifest path, canonical size, two-run hashes, and two-run match)*  
* `audit/gates/narratives/pack_identity.txt.path_proof.txt` *(governed path-proof for the PR-02 pack identity proof)*  
* `audit/docdeltas/hde-epic032_doc_deltas.md` *(Doc-Delta posture artifact for PR-02, including the no-PF-Canon-edit posture reported by PR Artifacts)*  
* `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt` *(governed path-proof for the PR-02 Doc-Delta posture artifact)*  
* `audit/gates/topology/orientation_demo.txt` *(orientation evidence refreshed from `total_artifacts: 342` to `total_artifacts: 345` after the three PR-02 indexed artifacts were added)*  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` *(governed path-proof for the refreshed orientation evidence)*  
* `tools/evidence/update_evidence_index.py` *(single-writer evidence-index tooling that loads `epic032.pr02.doc_deltas`, `epic032.pr02.pack_identity`, and `epic032.pr02.registry_diff` into Human Index and Machine Mirror generation)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the HDE-EPIC032 PR-02 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-02 Human Evidence Index update)*  
* `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
* `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying the HDE-EPIC032 PR-02 evidence rows for Doc-Delta, pack identity, and registry diff)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-02 Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel update)*  
* PR-02 uses only approved PR-02 token names in new rows and does not introduce `NARR_REGISTRY_CLOSURE_OK` or any new PF05 acceptance token.  
* This PR-02 proof family does not create a new public Reader route, public Reader flag, public payload field, public numeric output, public narrative text contract, or PF05 transport contract change.

#### **D.11aa EPIC032 PR-03 DB bridge fallback, provider parity, and evidence-indexing proof anchors**

* `tools/evidence/generate_db_bridge_parity.py` *(governed generator for HDE-EPIC032 PR-03 adapter selection, dev bridge fallback, bridge capability, deterministic provider parity, env connectivity, redaction posture, fail-closed check mode, and closed-rails live-unavailable posture)*  
* `artifacts/db_bridge/adapter_selection.snapshot.json` *(adapter selection snapshot proving deterministic dev fallback from direct `psycopg` selection to bridge selection, with no raw DSN recorded)*  
* `artifacts/db_bridge/adapter_selection.snapshot.json` MUST carry structural `selection_order` evidence derived from observed `attempts[*].provider`. Raw string presence, detached generator-only data, missing source binding, non-array shape, or mismatched order is insufficient and MUST fail generator write or check mode. This selection-order proof does not create a new acceptance-token claim.  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt` *(governed path-proof for the adapter selection snapshot)*  
* `artifacts/db_bridge/provider_parity.proof.json` *(provider parity and bridge capability proof with deterministic direct-vs-bridge harness cases, live provider parity marked unavailable under closed rails, and non-token proof labels for DB provider parity and bridge capability)*  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt` *(governed path-proof for the provider parity and bridge capability proof)*  
* `artifacts/runtime/env_connectivity.snapshot.json` *(runtime env connectivity snapshot proving secret-free dev bridge fallback through `DBAccess`, redacted presence for `DATABASE_URL` and `DB_BRIDGE_URL`, and fallback from psycopg error to bridge success)*  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt` *(governed path-proof for the runtime env connectivity snapshot)*  
* `ci/checks/check_bridge_consistency.py` *(bridge consistency guard proof anchor; rejects false-PASS provider-parity conditions when direct rows are missing, skipped, unavailable, or errored)*  
* `engine/db/adapter.py` *(adapter-selection implementation proof anchor for `PROD_ENV_ALIASES = {"prod", "production", "live"}` and production-like bridge guard behavior for `APP_ENV=live`)*  
* `tests/db/test_adapter_selection.py` *(adapter-selection regression proof for non-production fallback and `APP_ENV=live` production-like guard behavior)*  
* `tests/db/test_adapter_contract.py` *(adapter contract proof that bridge provider exposes provider contract methods expected by `DBAccess`)*  
* `tests/unit/test_check_bridge_consistency.py` *(bridge consistency regression proof for false-PASS rejection and truth-preserving skip acceptance)*  
* `tests/evidence` *(evidence regression proof family for PR-03 DB bridge fallback and provider parity evidence generation)*  
* `tests/ops/test_evidence_index.py` *(evidence-index regression proof for canonical adapter-selection key binding and stale duplicate key filtering)*  
* `tools/evidence/update_evidence_index.py` *(single-writer evidence-index tooling that binds PR-03 artifacts into the Human Evidence Index and Machine Evidence Mirror, uses canonical key `db_bridge.adapter_selection.snapshot`, and filters stale `epic032.pr03.adapter_selection`)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying the canonical adapter-selection row with HDE-EPIC032 PR-03 metadata and `DB_CONN_ENV_OK`)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-03 Human Evidence Index update)*  
* `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
* `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying PR-03 rows for canonical adapter selection, env connectivity, and provider parity; adapter-selection uses `DB_CONN_ENV_OK`, env-connectivity uses `DEV_DB_BRIDGE_FALLBACK_OK` and `DB_CONN_ENV_OK`, and provider-parity uses `JSON_CANONICAL_CHECK_OK`)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-03 Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel update)*  
* `audit/gates/topology/orientation_demo.txt` *(orientation evidence reporting a coherent evidence skeleton with 347 artifacts after duplicate adapter-selection row removal)*  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` *(governed path-proof for the refreshed orientation evidence)*  
* Shared path-proof refreshes for already-governed PR-01, PR-02, EPIC030, writer, topology, Human Index, and Machine Mirror companion files are evidence-tool refresh behavior only. They do not reopen earlier PR behavior, introduce a new public Reader route, create a new PF05 transport contract, or change public Reader bytes.  
* Live provider parity remains truthfully unavailable under closed rails and MUST NOT be reported as pass. Provider parity evidence MAY proceed as governed proof-label evidence without claiming those proof labels as acceptance tokens.

#### **D.11ab EPIC032 OPS-01 DB provider parity closure proof anchors**

* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` *(primary OPS-01 closure decision artifact; records `provider_parity_closure_status: closed`, active corpus closure, provider availability, presence-only secret posture, and no active parity row with `parity=diff`)*  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt` *(governed path-proof for the OPS-01 closure decision artifact)*  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity.proof.json` *(provider parity proof showing active rows `grants`, `search_path`, `select_one`, and `ddl_fingerprint` are non-skipped and match)*  
* `audit/ops/hde-epic032/db-provider-parity/bridge_consistency_result.txt` *(bridge consistency proof recording command, exit code 0, result `PASS`, active corpus, and all row parity values as match)*  
* `audit/ops/hde-epic032/db-provider-parity/parity_scope_rationale.txt` *(parity scope rationale proving Path A closure by all active corpus rows matching, not by excluding `ddl_fingerprint`)*  
* `audit/ops/hde-epic032/db-provider-parity/non_claims.txt` *(non-claim posture proof that OPS-01 does not claim QA PASS, PF09 status move, epic closure, or acceptance-token satisfaction for DB proof labels)*  
* `audit/ops/hde-epic032/db-provider-parity/ops01_final_report.txt` *(human-readable final OPS evidence summary for provider parity closure-candidate posture)*  
* `audit/ops/hde-epic032/db-provider-parity/created_files_sha256.txt` *(checksum ledger covering the closure decision, provider parity proof, bridge consistency result, non-claims, and support files)*  
* `audit/ops/hde-epic032/db-provider-parity/commands.txt` *(execution command transcript for DB posture and provider parity capture)*  
* `audit/ops/hde-epic032/db-provider-parity/stdout.log` *(stdout capture; empty stdout supports clean execution and secret-safe posture)*  
* `audit/ops/hde-epic032/db-provider-parity/stderr.log` *(stderr capture; empty stderr supports clean execution and secret-safe posture)*  
* `audit/ops/hde-epic032/db-provider-parity/exit_codes.txt` *(exit-code capture for OPS-01 provider parity execution)*  
* `audit/ops/hde-epic032/db-provider-parity/redacted_env_presence.txt` *(target environment and presence-only `DATABASE_URL` and `DB_BRIDGE_URL` posture; no secret values)*  
* `audit/ops/hde-epic032/db-provider-parity/adapter_selection.snapshot.json` *(provider availability and selection posture evidence carried by the OPS-01 closure packet)*  
* `audit/ops/hde-epic032/db-provider-parity/env_connectivity.snapshot.json` *(environment connectivity and selection-order evidence carried by the OPS-01 closure packet)*  
* OPS-01 provider parity closure is acceptable as OPS evidence only. It does not by itself claim QA PASS, PF09 status movement, HDE-FERM004.2 status movement, epic closure, DB proof-label acceptance-token satisfaction, or public Reader behavior.

#### **D.11ac EPIC032 PR-04 non-dev typed DB failure and evidence-coherence proof anchors**

* `artifacts/runtime/env_connectivity.nondev_failure.json` *(canonical JSON non-dev total-failure proof for `APP_ENV=stage`, no proactive probes, numeric-free public failure posture, secret-free posture, observed selection order `["psycopg","bridge"]`, and typed `BridgeUnavailable` / `missing_bridge_url` failure)*  
* `artifacts/runtime/env_connectivity.nondev_failure.json.path_proof.txt` *(governed path-proof for the non-dev total-failure proof)*  
* `artifacts/runtime/env_connectivity.snapshot.json` *(existing runtime env connectivity snapshot carried forward in the PR-04 DB posture evidence family)*  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt` *(governed path-proof for the runtime env connectivity snapshot)*  
* `artifacts/db_bridge/adapter_selection.snapshot.json` *(adapter selection snapshot carried forward from prior DBAccess provider-selection evidence)*  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt` *(governed path-proof for the adapter selection snapshot)*  
* `artifacts/db_bridge/provider_parity.proof.json` *(provider parity and bridge evidence row carried forward with `JSON_CANONICAL_CHECK_OK` and proof-label notes, not unsupported acceptance tokens)*  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt` *(governed path-proof for the provider parity proof)*  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` *(OPS-01 provider parity closure evidence indexed as OPS evidence only)*  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt` *(governed path-proof for the OPS-01 provider parity closure evidence)*  
* `tools/evidence/generate_db_bridge_parity.py` *(governed generator for PR-04 non-dev total-failure evidence, including fail-closed behavior when success, typed error class or code, snapshot, or attempt-order expectations deviate)*  
* `tests/evidence/test_generate_db_bridge_parity_nondev.py` *(evidence regression proof for non-dev stage posture, observed attempt order, and typed `BridgeUnavailable` / `missing_bridge_url`)*  
* `tests/db/test_adapter_selection.py` *(adapter-selection regression proof for stage missing-config and prod guard total-failure behavior with typed errors)*  
* `tools/evidence/update_evidence_index.py` *(single-writer evidence-index tooling that loads PR-04 primary artifact rows, including non-dev failure and OPS-01 closure-decision rows, into the Human Evidence Index and Machine Evidence Mirror entry set)*  
* `docs/evidence/INDEX.json` *(Human Evidence Index carrying HDE-EPIC032 PR-04 evidence rows)*  
* `docs/evidence/INDEX.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-04 Human Evidence Index update)*  
* `docs/evidence/INDEX.json.path_proof.txt` *(governed path-proof for the Human Evidence Index update)*  
* `docs/evidence/INDEX.sha256.path_proof.txt` *(governed path-proof for the Human Evidence Index hash sentinel update)*  
* `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror carrying PR-04 non-dev failure and OPS-01 closure-decision records)*  
* `artifacts/evidence_index.jsonl.sha256` *(hash sentinel refreshed for the HDE-EPIC032 PR-04 Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror update)*  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` *(governed path-proof for the Machine Evidence Mirror hash sentinel update)*  
* PR-04 evidence binds OPS-01 provider parity closure as OPS evidence only. It does not convert OPS-01 into QA evidence, PF09 status movement, epic closure, or unregistered DB provider or bridge proof-label token satisfaction.  
* PR-04 non-dev typed DB failure evidence does not create a new public Reader route, public Reader field, public transport contract, or Vendor ingest endpoint.  
* For PF05 evidence-anchor reading, **D.11aa**, **D.11ab**, and **D.11ac** form the combined proof chain for `HDE-FERM004.2`: PR-03 supplies DB bridge fallback, bridge capability proof, deterministic provider-parity harnessing, false-PASS parity guards, evidence-index binding, and CI remediation; OPS-01 supplies provider-parity closure as OPS evidence; PR-04 supplies non-dev typed DB failure behavior, evidence coherence, and OPS-01 binding. This combined proof-chain note does not edit PF09.5 status, claim QA PASS, claim epic closure, claim live vendor behavior, or convert DB proof labels into acceptance tokens.  
* DB provider and bridge proof-label posture for PF05 evidence anchors: `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token proof labels unless HDE-Governance admits them or Build Notes mints them pending drainage. `DEV_DB_BRIDGE_FALLBACK_OK` remains canonical only for scoped dev fallback. PF05 evidence rows MUST NOT treat those DB provider or bridge proof labels as acceptance tokens by inference, Machine Mirror row membership, OPS-01 closure, QA PASS, or PF09.5 supportability language.

#### **D.11ad EPIC032 Live QA proof anchors for Step-0A and Step-0B**

* **Step-0A discovery posture and Live QA harness setup**  
  * `audit/qa/hde-epic032/00_meta/live_qa_harness.py` *(QA-created harness used for HDE-EPIC032 Live QA Step-0A and Step-0B execution)*  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log` *(canonical step receipt for Step-0A PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log.path_proof.txt` *(governed path-proof for the Step-0A primary log)*  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/result.json` *(Step-0A result sidecar proving QA root creation, listed repo loci discovery, status PASS, and exit code 0\)*  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/remediation_provenance.md` *(same-stream remediation provenance for the bounded Step-0A harness correction)*  
  * `audit/qa/hde-epic032/00_meta/delta/changed_files.txt` *(bounded Moon Loop changed-files capture for the Step-0A harness correction)*  
  * `audit/qa/hde-epic032/00_meta/delta/changed_files.sha256` *(hash capture for the bounded Step-0A harness correction)*  
  * `audit/qa/hde-epic032/00_meta/delta/remediation_note.txt` *(remediation note recording the corrected `live_qa_harness.py` placeholder body and why it changed)*  
  * `audit/qa/hde-epic032/00_meta/delta/failure_signature.txt` *(failure-signature capture for the Step-0A placeholder-body syntax failure)*  
* **Step-0B doc-delta capture**  
  * `audit/docdeltas/hde-epic032_doc_deltas.md` *(repo-root doc-delta surface containing BLOCKERS and CAVEATS headings and the Step-0A correction note)*  
  * `audit/qa/hde-epic032/00_meta/doc_deltas.md` *(QA-root doc-delta surface containing BLOCKERS and CAVEATS headings and the Step-0A correction note)*  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log` *(canonical step receipt for Step-0B PASS evidence)*  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log.path_proof.txt` *(governed path-proof for the Step-0B primary log)*  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json` *(Step-0B result sidecar proving draft and capture surfaces exist and required headings are present)*  
* **Step manifest**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state QA step manifest recording Step-0A and Step-0B PASS entries and log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the HDE-EPIC032 QA step manifest)*  
* Step-0A and Step-0B remain tokenless Live QA evidence. Their primary headers record `intended_tokens: []` and `claimed_tokens: []`. The bounded Moon Loop correction is QA-harness correction evidence only and does not create PF05 product bytes, public Reader expansion, acceptance-token satisfaction, PF09 drainage, or epic closeout.

#### **D.11ae EPIC032 Live QA proof anchors for PO-001 to PO-003**

* **PO-001 Fermentation Pass 3 scope boundary**  
  * `audit/qa/hde-epic032/checks/po-001/primary.log` *(canonical step receipt for PO-001 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-001/primary.log.path_proof.txt` *(governed path-proof for the PO-001 primary log)*  
  * `audit/qa/hde-epic032/checks/po-001/result.json` *(PO-001 result sidecar proving Reader and dev Reader catalog surfaces visible, OPS evidence not treated as QA PASS by itself, and DB proof labels not treated as acceptance tokens)*  
* **PO-002 router determinism and identity**  
  * `audit/qa/hde-epic032/checks/po-002/primary.log` *(canonical step receipt for PO-002 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-002/primary.log.path_proof.txt` *(governed path-proof for the PO-002 primary log)*  
  * `audit/qa/hde-epic032/checks/po-002/result.json` *(PO-002 result sidecar proving router tests return exit code 0, key-table evidence exists, and AB↔BA parity evidence exists)*  
* **PO-003 keys-only and Reader non-expansion**  
  * `audit/qa/hde-epic032/checks/po-003/primary.log` *(canonical step receipt for PO-003 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-003/primary.log.path_proof.txt` *(governed path-proof for the PO-003 primary log)*  
  * `audit/qa/hde-epic032/checks/po-003/result.json` *(PO-003 result sidecar proving router key-table evidence remains keys-only, Reader route posture is visible and not expanded into a new proof route, and APP\_ENV gating is visible for internal/dev surfaces)*  
* **Manifest and primary-header trust proof**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-001, PO-002, and PO-003 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-001 through PO-003)*  
* PO-001, PO-002, and PO-003 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves.

#### **D.11af EPIC032 Live QA proof anchors for PO-004 to PO-006**

* **PO-004 narrative-router identity**  
  * `audit/qa/hde-epic032/checks/po-004/primary.log` *(canonical step receipt for PO-004 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-004/primary.log.path_proof.txt` *(governed path-proof for the PO-004 primary log)*  
  * `audit/qa/hde-epic032/checks/po-004/result.json` *(PO-004 result sidecar proving router pytest exit code 0, AB↔BA or identity marker evidence exists, and six router tests passed)*  
  * `artifacts/narratives/router/parity_abba.log` *(router identity evidence relied on by PO-004; full PR-01 anchor is listed in D.11y)*  
* **PO-005 registry diff and pack identity**  
  * `audit/qa/hde-epic032/checks/po-005/primary.log` *(canonical step receipt for PO-005 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-005/primary.log.path_proof.txt` *(governed path-proof for the PO-005 primary log)*  
  * `audit/qa/hde-epic032/checks/po-005/result.json` *(PO-005 result sidecar proving registry generator check returns exit code 0, registry diff is bound to HDE-EPIC032, and pack identity posture is recorded)*  
  * `audit/gates/narratives/registry.diff.json` *(registry diff evidence relied on by PO-005; full PR-02 anchor is listed in D.11z)*  
  * `audit/gates/narratives/pack_identity.txt` *(pack identity evidence relied on by PO-005; full PR-02 anchor is listed in D.11z)*  
* **PO-006 registry non-overclaim**  
  * `audit/qa/hde-epic032/checks/po-006/primary.log` *(canonical step receipt for PO-006 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-006/primary.log.path_proof.txt` *(governed path-proof for the PO-006 primary log)*  
  * `audit/qa/hde-epic032/checks/po-006/result.json` *(PO-006 result sidecar proving unsupported registry token claims were not seen, required missing items are empty, and behavior failures are empty)*  
  * `audit/gates/narratives/keys_10x4.table.json` *(keys-only roster evidence relied on by PO-006; full PR-01 anchor is listed in D.11y)*  
* **Manifest and token-header trust proof**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-004, PO-005, and PO-006 PASS entries with check-scoped primary-log paths and path-proof references)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-004 through PO-006)*  
* PO-004, PO-005, and PO-006 remain tokenless Live QA evidence. Their primary headers record `intended_tokens: []` and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves. The registry evidence does not claim unsupported acceptance semantics, and the router key-table evidence does not overclaim `NARR_REGISTRY_CLOSURE_OK`.

#### **D.11ag EPIC032 Live QA proof anchors for PO-007 to PO-009**

* **PO-007 registry and doc-delta identity**  
  * `audit/qa/hde-epic032/checks/po-007/primary.log` *(canonical step receipt for PO-007 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-007/primary.log.path_proof.txt` *(governed path-proof for the PO-007 primary log)*  
  * `audit/qa/hde-epic032/checks/po-007/result.json` *(PO-007 result sidecar proving registry diff binding, doc-delta surface availability, and PASS status)*  
  * `audit/gates/narratives/registry.diff.json` *(registry diff evidence relied on by PO-007; full PR-02 anchor is listed in D.11z)*  
  * `audit/docdeltas/hde-epic032_doc_deltas.md` *(doc-delta surface relied on by PO-007; full PR-02 anchor is listed in D.11z)*  
* **PO-008 DB bridge and provider parity proof-chain**  
  * `audit/qa/hde-epic032/checks/po-008/primary.log` *(canonical step receipt for PO-008 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-008/primary.log.path_proof.txt` *(governed path-proof for the PO-008 primary log)*  
  * `audit/qa/hde-epic032/checks/po-008/result.json` *(PO-008 result sidecar proving generator check return code 0, OPS closure status visibility, and PASS status)*  
  * `tools/evidence/generate_db_bridge_parity.py` *(DB bridge/provider parity generator relied on by PO-008; full PR-03 and PR-04 anchors are listed in D.11aa and D.11ac)*  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` *(OPS provider-parity closure evidence relied on by PO-008; full OPS-01 anchor is listed in D.11ab)*  
* **PO-009 OPS evidence non-claim posture**  
  * `audit/qa/hde-epic032/checks/po-009/primary.log` *(canonical step receipt for PO-009 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-009/primary.log.path_proof.txt` *(governed path-proof for the PO-009 primary log)*  
  * `audit/qa/hde-epic032/checks/po-009/result.json` *(PO-009 result sidecar proving OPS status visibility, OPS QA PASS non-claim posture, and PASS status)*  
  * OPS provider parity evidence remains support evidence only for PO-009. It does not become QA success, checklist completion, PF09.5 drainage, acceptance-token satisfaction, or epic closure by itself.  
* **Manifest, header, and tokenless posture for PO-007 to PO-009**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-007, PO-008, and PO-009 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-007 through PO-009)*  
  * PO-007, PO-008, and PO-009 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves.

#### **D.11ah EPIC032 Live QA proof anchors for PO-010 to PO-012**

* **PO-010 structural selection-order proof**  
  * `audit/qa/hde-epic032/checks/po-010/primary.log` *(canonical step receipt for final PO-010 PASS evidence after PR-routed selection-order remediation)*  
  * `audit/qa/hde-epic032/checks/po-010/primary.log.path_proof.txt` *(governed path-proof for the PO-010 primary log)*  
  * `audit/qa/hde-epic032/checks/po-010/result.json` *(PO-010 result sidecar proving PASS status, no required-missing entries, no behavior failures, and tokenless primary-header posture)*  
  * `artifacts/db_bridge/adapter_selection.snapshot.json` *(structural `selection_order` evidence relied on by PO-010; `selection_order` must match observed attempt providers)*  
  * `artifacts/db_bridge/provider_parity.proof.json` *(provider-parity proof-label posture relied on by PO-010; DB proof labels remain non-token proof labels)*  
  * `tools/evidence/generate_db_bridge_parity.py` *(PR-routed generator remediation relied on by PO-010 to stabilize structural selection-order evidence)*  
* **PO-011 current-state PASS proof**  
  * `audit/qa/hde-epic032/checks/po-011/primary.log` *(canonical step receipt for PO-011 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-011/primary.log.path_proof.txt` *(governed path-proof for the PO-011 primary log)*  
  * `audit/qa/hde-epic032/checks/po-011/result.json` *(PO-011 result sidecar proving PASS status, no required-missing entries, no behavior failures, and tokenless primary-header posture)*  
* **PO-012 regenerated DB bridge evidence proof**  
  * `audit/qa/hde-epic032/checks/po-012/primary.log` *(canonical step receipt for final PO-012 PASS evidence after governed DB bridge evidence regeneration)*  
  * `audit/qa/hde-epic032/checks/po-012/primary.log.path_proof.txt` *(governed path-proof for the PO-012 primary log)*  
  * `audit/qa/hde-epic032/checks/po-012/result.json` *(PO-012 result sidecar proving final PASS status, no required-missing entries, no behavior failures, and tokenless primary-header posture)*  
  * A brief PO-012 `TOOLING_BLOCKED` state caused by missing `artifacts/db_bridge/adapter_selection.snapshot.json` during refresh is non-blocking only after governed regeneration via `tools/evidence/generate_db_bridge_parity.py` restores the final current-state PASS result.  
* **PR-routed remediation and tokenless posture for PO-010 to PO-012**  
  * `audit/qa/hde-epic032/remediation/moon_loop/patch.diff` *(remediation package artifact recorded for the PO-010 through PO-012 review)*  
  * `audit/qa/hde-epic032/remediation/moon_loop/boundary_classification.md` *(boundary-classification artifact recording that non-QA-root generator remediation is PR-routed remediation, not bounded Moon Loop-only correction)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-010, PO-011, and PO-012 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-010 through PO-012)*  
  * PO-010, PO-011, and PO-012 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves.

#### **D.11ai EPIC032 Live QA proof anchors for PO-013 to PO-015**

* **PO-013 evidence-index coherence**  
  * `audit/qa/hde-epic032/checks/po-013/primary.log` *(canonical step receipt for PO-013 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt` *(governed path-proof for the PO-013 primary log)*  
  * `audit/qa/hde-epic032/checks/po-013/result.json` *(PO-013 result sidecar proving PASS status, required-missing empty, Human Index present, Machine Mirror present, and command checks returning 0\)*  
  * `docs/evidence/INDEX.json` *(Human Evidence Index proof anchor relied on by PO-013)*  
  * `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror proof anchor relied on by PO-013)*  
* **PO-014 Human Index and Machine Mirror alignment**  
  * `audit/qa/hde-epic032/checks/po-014/primary.log` *(canonical step receipt for PO-014 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt` *(governed path-proof for the PO-014 primary log)*  
  * `audit/qa/hde-epic032/checks/po-014/result.json` *(PO-014 result sidecar proving PASS status, required-missing empty, Human and Machine evidence loci present, and command checks returning 0\)*  
  * `docs/evidence/INDEX.json` *(Human Evidence Index proof anchor relied on by PO-014)*  
  * `artifacts/evidence_index.jsonl` *(Machine Evidence Mirror proof anchor relied on by PO-014)*  
* **PO-015 generated-proof fail-closed checks**  
  * `audit/qa/hde-epic032/checks/po-015/primary.log` *(canonical step receipt for PO-015 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt` *(governed path-proof for the PO-015 primary log)*  
  * `audit/qa/hde-epic032/checks/po-015/result.json` *(PO-015 result sidecar proving PASS status, required-missing empty, all commands green, and command checks returning 0\)*  
  * `tools/evidence/generate_narrative_registry_diff.py` *(generated-proof fail-closed command target relied on by PO-015)*  
  * `tools/evidence/generate_db_bridge_parity.py` *(generated-proof fail-closed command target relied on by PO-015)*  
* **Manifest and tokenless posture for PO-013 to PO-015**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-013, PO-014, and PO-015 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-013 through PO-015)*  
  * PO-013, PO-014, and PO-015 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves.

#### **D.11aj EPIC032 Live QA proof anchors for PO-016 to PO-018**

* **PO-016 DB proof-label non-token posture**  
  * `audit/qa/hde-epic032/checks/po-016/primary.log` *(canonical step receipt for PO-016 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-016/primary.log.path_proof.txt` *(governed path-proof for the PO-016 primary log)*  
  * `audit/qa/hde-epic032/checks/po-016/result.json` *(PO-016 result sidecar proving PASS status, DB proof-label token overclaim not detected, no required-missing entries, and no behavior failures)*  
  * `artifacts/db_bridge/provider_parity.proof.json` *(DB provider parity proof anchor relied on by PO-016; DB proof labels remain non-token proof labels unless Governance registers them)*  
* **PO-017 dev bridge fallback scope**  
  * `audit/qa/hde-epic032/checks/po-017/primary.log` *(canonical step receipt for PO-017 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-017/primary.log.path_proof.txt` *(governed path-proof for the PO-017 primary log)*  
  * `audit/qa/hde-epic032/checks/po-017/result.json` *(PO-017 result sidecar proving PASS status, fallback-scope checking, no required-missing entries, and no behavior failures)*  
  * `artifacts/db_bridge/adapter_selection.snapshot.json` *(DB bridge fallback and adapter-selection proof anchor relied on by PO-017)*  
* **PO-018 active evidence families and PF09 drainage non-claim**  
  * `audit/qa/hde-epic032/checks/po-018/primary.log` *(canonical step receipt for PO-018 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-018/primary.log.path_proof.txt` *(governed path-proof for the PO-018 primary log)*  
  * `audit/qa/hde-epic032/checks/po-018/result.json` *(PO-018 result sidecar proving PASS status, active evidence families present, PF09 drainage not claimed, no required-missing entries, and no behavior failures)*  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` *(OPS support evidence locus relied on by PO-018; OPS evidence does not by itself claim PF09.5 drainage or epic closure)*  
* **Manifest, path-proof, and tokenless posture for PO-016 to PO-018**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-016, PO-017, and PO-018 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-016 through PO-018)*  
  * PO-016, PO-017, and PO-018 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by themselves.

#### **D.11ak EPIC032 Live QA proof anchors for PO-019 to PO-021**

* **PO-019 reused-foundation posture**  
  * `audit/qa/hde-epic032/checks/po-019/primary.log` *(canonical step receipt for PO-019 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-019/primary.log.path_proof.txt` *(governed path-proof for the PO-019 primary log)*  
  * `audit/qa/hde-epic032/checks/po-019/result.json` *(PO-019 result sidecar proving reused foundation checked from repo docs, no required-missing entries, no behavior failures, and PASS status)*  
* **PO-020 truth-class separation**  
  * `audit/qa/hde-epic032/checks/po-020/primary.log` *(canonical step receipt for PO-020 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-020/primary.log.path_proof.txt` *(governed path-proof for the PO-020 primary log)*  
  * `audit/qa/hde-epic032/checks/po-020/result.json` *(PO-020 result sidecar proving OPS evidence, QA result, PF09.5 drainage, and final closeout remain separate truth classes)*  
* **PO-021 vendor-version runtime conformance non-claim**  
  * `audit/qa/hde-epic032/checks/po-021/primary.log` *(canonical step receipt for PO-021 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-021/primary.log.path_proof.txt` *(governed path-proof for the PO-021 primary log)*  
  * `audit/qa/hde-epic032/checks/po-021/result.json` *(PO-021 result sidecar proving vendor-version runtime conformance is not claimed and PASS status is limited to the reviewed proof lane)*  
* **Manifest, path-proof, and tokenless posture for PO-019 to PO-021**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-019, PO-020, and PO-021 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-019 through PO-021)*  
  * PO-019, PO-020, and PO-021 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, vendor-version runtime conformance, or epic closeout by themselves.

#### **D.11al EPIC032 Live QA proof anchors for PO-022 to PO-024**

* **PO-022 live-provider behavior non-claim**  
  * `audit/qa/hde-epic032/checks/po-022/primary.log` *(canonical step receipt for PO-022 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-022/primary.log.path_proof.txt` *(governed path-proof for the PO-022 primary log)*  
  * `audit/qa/hde-epic032/checks/po-022/result.json` *(PO-022 result sidecar proving live provider behavior is not claimed, no required-missing entries, no behavior failures, and PASS status)*  
* **PO-023 public Reader non-expansion**  
  * `audit/qa/hde-epic032/checks/po-023/primary.log` *(canonical step receipt for PO-023 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-023/primary.log.path_proof.txt` *(governed path-proof for the PO-023 primary log)*  
  * `audit/qa/hde-epic032/checks/po-023/result.json` *(PO-023 result sidecar proving `/reader` remains visible, the invented proof route is absent, no required-missing entries exist, and public Reader non-expansion posture holds)*  
* **PO-024 proof-only Live QA role**  
  * `audit/qa/hde-epic032/checks/po-024/primary.log` *(canonical step receipt for PO-024 PASS evidence under closed rails and deterministic pins)*  
  * `audit/qa/hde-epic032/checks/po-024/primary.log.path_proof.txt` *(governed path-proof for the PO-024 primary log)*  
  * `audit/qa/hde-epic032/checks/po-024/result.json` *(PO-024 result sidecar proving Live QA planning or execution did not perform implementation, PF edits, closeout action, route edits, Reader adapter edits, public payload edits, public flag edits, or evidence-index/token-map edits)*  
* **Manifest, path-proof, tokenless posture, and non-expansion posture for PO-022 to PO-024**  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json` *(current-state manifest proving PO-022, PO-023, and PO-024 entries with PASS status and check-scoped primary-log paths)*  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` *(governed path-proof for the manifest used by PO-022 through PO-024)*  
  * PO-022, PO-023, and PO-024 remain tokenless Live QA evidence. Their primary headers record `captured_env`, `evidence_artifacts`, `intended_tokens: []`, and `claimed_tokens: []`. These checks do not claim acceptance-token satisfaction, final QA outcome, PF09.5 drainage, live-provider behavior, public Reader route expansion, public Reader flag expansion, public payload expansion, PF edits, or epic closeout by themselves.

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

### **D.13 Internal ops: `/internal/version` bundle (ops-only; not A7)**

* `artifacts/ops/internal_version/body_get.json`

* `artifacts/ops/internal_version/body_get.sha256`

* `artifacts/ops/internal_version/headers_get.txt`

* `artifacts/ops/internal_version/headers_head.txt`

* `artifacts/ops/internal_version/headers_cond_if_none_match.txt`

* `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`

* `artifacts/ops/internal_version/request_chain_manifest.json`

* `artifacts/ops/internal_version/two_run_identity.log`

* `artifacts/ops/internal_version/*.path_proof.txt`

**Capture note (raw headers).** `headers_get.txt` and `headers_head.txt` are raw capture files. If capture tooling emits non-header warning lines, validators should ignore non–`key: value` lines while still requiring the HTTP status line and the required header fields.

**Filenames rule (canonical \+ permitted aliases only).** The filenames listed above are the canonical internal\_version evidence bundle filenames. If an epic acceptance binding requires legacy alias filenames, emit alias copies mechanically sourced from these canonical files, and continue to index the canonical filenames. Permitted legacy aliases include `cond_if_none_match_headers.txt` and `cond_if_modified_since_headers.txt` (legacy), which are aliases for the canonical `headers_cond_if_*` captures. Do not introduce ad-hoc filename variants outside the canonical set plus explicitly defined aliases.

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

