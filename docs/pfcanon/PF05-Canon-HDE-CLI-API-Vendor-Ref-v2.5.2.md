# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref  
**Version:** v2.5.2  
**Status:** Canon  
**Effective date:** 2026-08-25  
**Last Update Gate:** BN 12.8.9   
**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **0.2 Scope \[Required-Now\]**

* **Supersession (PF10 addenda).** Consult the complete latest active PF10 base version, whether it is one unlettered document or a complete verified lettered set, and treat every document in a lettered set as an equally authoritative container of independently scoped addenda. Apply every applicable, active, non-superseded addendum to its own scope. A later document letter supersedes nothing by itself; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and lower-numbered guidance remains authoritative for distinct scope. PF10 governs PF05 only where such an addendum explicitly addresses a PF05-owned topic; when the complete active PF10 version is silent on that topic, PF05 governs. PF05 integrates applicable PF10 guidance and routes **by title only** to single homes (no version numbers). Build Notes reference posture: cite PF10 by **addendum number \+ addendum title**; do not use PF10 version strings, document letters, or PF10 section numbers as durable anchors.  
    
* **Ownership.** This document owns the **bytes** for CLI, Reader transport, and Vendor ingest (HDAPI): payload shapes, validators, headers & conditional delivery, typed error mapping, and exit-code/stream rules. It is authoritative for CLI and Reader wire bytes. **Appendix A** transport matrices are kept in lockstep with **HDE-Governance §10** (titles only). Writers/errors posture is policy-owned in Governance; PF05 references it by title.  
    
* **Public resonance posture (v1).** Public surface is **bands-only** and **numeric-free**; resonance is **SR-only** (`alpha=1.0`). `hysteresis=1` is armed for future XR and not exposed. Any XR diagnostics, if used, are **CLI-admin-guarded** and never emitted on Reader 200\.  
    
* **Success carriers, canonical JSON, and locale.** On exit 0, each CLI mode emits exactly one declared success carrier and leaves stderr empty. The closed carrier set is canonical JSON, help text, version text, Aux narrative text, and governed Aux-suppressed empty output. Canonical JSON is mandatory for every ordinary machine success and every file-only receipt; those JSON bytes are UTF-8 (no BOM), ASCII-sorted by key, compact, and terminated by exactly one LF, with arrays used as sets deduped and ASCII-sorted. Nonempty text carriers are UTF-8, LF-only, and terminated by exactly one LF. All byte checks and comparisons run with `LC_ALL=C`, `LANG=C`, and `TZ=UTC` (see **HDE-Schemas & Artifacts**).  
    
* **Endpoint Catalog (JSON success): proof surface (A7).** The Catalog is **internal-only** and **env-gated** per entry; entries not gated for prod are **unreachable in production**. A7 transport proofs **must** run on a **§5.6 Endpoint Catalog (JSON success)** route (titles only; path-agnostic). Internal-ops `/internal/version` is **excluded** and governed by **HDE-Governance §10.5**. A7 **byte rules** are owned in **§5.3** of this document.  
    
* **Single homes.** PF05 is the bytes/contract home for its CLI \+ transport surfaces; it does not own global token semantics or the canonical token roster (those are single-homed in **HDE-Governance**). PF05 may **reference** token names only where needed to pin acceptance claims for PF05 surfaces. PF05 also does not own the global Evidence Index: **HDE-Schemas & Artifacts (PF12)** is the single home; PF05 may list surface-specific artifact paths only when a byte-level contract or proof anchor requires an explicit file reference.  
    
* **Evidence discipline (PF12 single home).** Evidence indexing (titles/paths only), the human Evidence Index and its hash sentinel, and the machine JSONL mirror are governed in **PF12** and must update **in the same PR** as artifact changes. CI enforces: 1:1 join equality (human↔machine), unknown-key rejection, ASCII field order, sort-before-write, **single mirror file**, and required `proof_anchor` path-proofs, per PF12.

  ## **0.3 Tagging convention**

* **\[Implemented\]** — Verified in the repository and exercised by surfaces/tests.  
    
* **\[Required-Now\]** — Required for current build goals; if missing in code, it is a gap to close.  
    
* **\[Speculative\]** — Accepted future design; preserved here but not yet wired.

  ## **0.4 Change policy**

* **Single homes; no duplication.** Do not restate Architecture/Math rules; keep CLI/Reader/Vendor **bytes here** and reference other documents **by title only**.  
    
* **Governed evidence roots.** Governed-root identities, artifact-family paths, admissibility, and top-level-directory authorization are single-homed in **HDE-Schemas & Artifacts**. PF05 may name an explicit PF05 proof path only where required to define or verify a PF05-owned byte contract; it MUST NOT maintain a closed global root roster. Live-QA check scoping and transient-path refusal remain subject to the owning evidence and QA contracts.  
    
* **Lowercase directories (ASCII) only.** Don’t create mixed-case directories.  
    
* **Deterministic CLI results.** Any CLI command results used in QA MUST satisfy two-run determinism; pair-sensitive data outputs MUST also satisfy AB↔BA identity as described in §9. Help and version have no party order, and Aux narrative parity follows its owning narrative and perspective contract. *(Token names live in Governance.)*  
    
* **Evidence anchoring.** Any evidence pointer emitted by the CLI must use governed repo roots and must be path-proven in the evidence index (see **Glow QA Guide** and **HDE-Governance §9** by title).  
    
* **Mirror schema check invocation (operator note).**  
    
  * **Path and interpreter.** `ci/checks/check_mirror_schema.sh` is the retained stable path for a Python entrypoint. Its `.sh` suffix is legacy path identity and does not declare the current interpreter.  
  * **Supported invocation.** Run the gate from the repository root. The preferred form is `python ci/checks/check_mirror_schema.sh`, where `python` resolves to the supported Python 3 interpreter. Direct execution as `ci/checks/check_mirror_schema.sh` is supported only when Git executable mode and shebang handling are guaranteed. A Python harness SHOULD invoke `[sys.executable, "ci/checks/check_mirror_schema.sh"]`.  
  * **Fixed input.** The validator reads the repository Machine Mirror at `artifacts/evidence_index.jsonl` and does not support a caller-selected mirror path. New plans, operator instructions, and harnesses SHOULD omit appended operands; the current program ignores such an operand, and its presence does not prove custom-path support.  
  * **Failure classification.** `bash ci/checks/check_mirror_schema.sh` and `sh ci/checks/check_mirror_schema.sh` are invalid. Shell-parser output from either form is an invocation or tooling defect, not a Machine Mirror schema finding. A missing-mirror result obtained outside the repository root is a locus defect until the supported invocation is rerun from the repository root. Only the supported invocation’s exit status and validator output may support a Mirror-schema PASS or FAIL claim, and evidence MUST preserve the command actually executed.  
  * **Retention and migration.** Retaining the legacy path is accepted. Any future migration to a `.py` path MUST intentionally introduce and validate the new entrypoint; inventory and update active CI, sanity, QA, test, operator-documentation, and canon callers; preserve historical evidence and command transcripts unchanged; preserve direct and explicit-Python invocation of the legacy path during transition; rerun the owning closed-rails Mirror, Evidence Index, path, hash, and final-LF gates; and define an explicit deprecation and removal point. Because explicit-Python callers would parse a Bash wrapper as Python, the legacy path MUST remain Python-compatible until those callers are drained. No incidental rename, suffix-only cleanup, or partial caller migration is authorized.


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
    
* **Repository-state note.** The four current-state rows below are pinned to `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`; they are not branch-head or runtime-PASS claims.  
    
* **`hdctl aux-preview` — Present; Required-Now (admin-only).** The parser surface exists; the narrative/admin byte contract remains governed by §4.5.  
    
* **`hdctl bg:resolve` — Partially implemented; Required-Now.** The parser and configured-v2 vendor path exist, but DB/auto resolution remains a stub and failure-stream behavior does not conform to §§3.3-3.4; see §4.6.  
    
* **`hdctl bg:export-json` — Speculative; explicit gap.** No command is present; the future stateless BodyGraph export contract is recorded in §4.8.  
    
* **`hdctl admin-bundle` — Required-Now; not implemented.** No command was found at the pinned commit. Exact invocable and remote-request bytes remain OPEN pending the Doc-Delta required by §4.9.  
    
* **`hdctl dev:sampler` — Implemented (dev/admin-only).** Dev/admin sampler harness; runs only when `APP_ENV ∈ {dev, test, local}` under closed rails, reads a JSON candidates file, calls the sampler core, and emits canonical JSON for deterministic QA replay. Full contract (inputs, seed semantics, determinism, and streams) lives in §4.10.  
    
  ---

  ## **Reader transport**

* **Endpoint Catalog (JSON success) — Required-Now.** Internal-only, env-gated per entry, and the **single A7 proof surface** for Reader success routes (not `/internal/version`). A7 header matrix, conditional behavior, and proof artifacts are specified in §5.3, §5.6, and Appendix A; PF12 owns the Evidence Index and mirror schema.  
    
* **Dev harness — Implemented (dev-only).** `/reader?v=1` is the canonical dev Reader surface for schema/LF checks, AB↔BA and two-run identity, and Reader↔CLI reader-dump parity. `/api/reader?v=1` is an alias only when the Reader blueprint is actually mounted under `/api`. Rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); harness proofs are supplemental and do not replace Endpoint Catalog A7 proofs. See §5.4.  
    
* **`/internal/version` (ops endpoint) — Required-Now.** Ops-only identity surface (JSON, no cache, no ETag) used for engine identity and rails snapshots. Header and refusal posture are governed by HDE-Governance §10.5; bytes live in the internal-ops section of Reader transport.  
    
* **Production Reader surface — Required-Now.** `POST /api/reader?v=1` is the adopted production application route. It accepts only the closed two-UUID request in §5.1, resolves BodyGraphs read-only, and projects either the one-band eligible Reader v1 success or the empty ineligible self-pair success. The existing file-path GET Reader remains development-only and non-authoritative.  
    
  ---

  ## **Serializer and emitter**

* **Single canonical emitter shared by CLI and Reader — Required-Now.** All public JSON (success and typed errors) is emitted by a single presenter/emitter entrypoint with canonical JSON rules (UTF-8, sorted keys, compact, one LF). No ad-hoc `json.dumps` or alternate serializers on public paths. Full rules and grep-guards live in §6.  
    
  ---

  ## **Vendor ingest (HDAPI)**

* **Legacy BodyGraph fallback and bounded HumanDesignAPI v2 chart path — implemented with remaining PF05 gaps.** **HDE Build Checklist — Fermentation** records HDE-FERM006 through HDE-FERM008 Done for the bounded HDE BodyGraph-detail scope. At `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, configured v2 bases use the version-neutral `charts` resource, Bearer auth, and the deterministic `ChartResult` adapter; non-v2 bases retain an explicit legacy `bodygraphs` fallback. This does not claim broad HumanDesignAPI v2 platform conformance, public Reader expansion, production deployment, production DB-hot-path completion, or complete conformance to every §7.2/§7.3 byte requirement. See §§7.1.10, 7.2, and 7.4.  
    
* **HumanDesignAPI v2 pending route set — Required-Now.** The pending v2 conformance work must reconcile `POST /v2/charts`, `POST /v2/charts/simple`, and `POST /v2/charts/coordinates` as the recommended v2 chart routes, and `POST /v1/bodygraphs` and `POST /v1/bodygraphs/simple` as legacy v1 routes. The suspect `api-reference/openapi.json` artifact MUST be quarantined until domain, title, server, and path-family validation prove it is a HumanDesignAPI artifact.  
    
* **Base-URL, API-version, and credential posture — Required-Now.** `HD_API_BASE_URL` is the canonical HumanDesignAPI base URL key and owns the vendor API-version boundary. Runtime request construction appends only version-neutral resource paths to the configured base URL, preserves any configured version path, and MUST NOT infer route behavior or auth-header family from hardcoded `/v1` or `/v2` path strings. `HDAPI_BASE_URL` is deprecated compatibility only, and conflicting `HD_API_BASE_URL` / `HDAPI_BASE_URL` values fail closed. `HD_API_KEY` is the canonical vendor credential key; v2 chart routes project it as `Authorization: Bearer`, and legacy v1 BodyGraph routes project it as `HD-Api-Key`. `GEO_API_KEY` is preserved where geocoding behavior requires `HD-Geocode-Key`.  
    
* **Live HTTP gated by SAFE rails — Required-Now.** Vendor calls are permitted only when rails are explicitly open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); default posture for dev/CI is closed. Closed-rails refusal behavior, admin override, and rails evidence live in §7.1. HumanDesignAPI v2 open-rails smoke, when required, remains PO-only and evidence-backed.  
    
* **Adapter data-source policy — Required-Now.** In prod, the adapter reads from DB on the hot path, using vendor only on explicit triggers (birth-data change, scheduled refresh, operator). In dev, direct vendor calls are allowed but must upsert into DB for repeatability. HumanDesignAPI v2 conformance MUST route through one sanctioned vendor seam and MUST NOT create a second HTTP home, bypass adapter guards, or bypass the presenter boundary. See §7.4.  
    
* **No-AI vendor boundary — Required-Now.** HumanDesignAPI v2 conformance is deterministic vendor-contract work only. PF05 MUST NOT add OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, AI acceptance-token, or AI-enablement bytes, flags, headers, config keys, routes, error mappings, or runtime obligations for this work.  
    
* **Production calls — Speculative.** Concrete timeout, retry, backoff, and observability profiles are defined in §7.3 and must be pinned before enabling production vendor traffic. Documentation consolidation alone does not prove live vendor conformance.  
    
  ---

  ## **Evidence discipline: indices and parity**

* **Evidence index & mirror — Required-Now.** **HDE-Schemas & Artifacts** is the single home for the Evidence Catalog, Human Evidence Index, hash sentinel, Machine Evidence Mirror, governed artifact identities and paths, record schemas, parity, checksums, and path-proofs. PF05 may name an explicit PF05 proof anchor only where required to define or verify a PF05-owned byte contract; it does not maintain a parallel Evidence Catalog.  
    
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

**Repository evidence note (informative).** Checked-in CLI help, installability, argument-policing, parity/identity, and sampler records are named in the owning evidence sections. Those files record claims about prior runs; their presence does not by itself prove that commands ran successfully at `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, tests passed, acceptance tokens are currently green, or an epic closed. Those conclusions require governed execution and acceptance records. All governed JSON success bytes MUST come from the single canonical emitter, be UTF-8 with ASCII-sorted keys and exactly one trailing LF, and be validated under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

## **3.1 Global flags & process contract**

* **Packaging & entrypoints (normative).** Single home in **pyproject**:  
  `[project.scripts]` defines `hdctl = "engine.cli.main:cli"`.  
  **Module-runner parity:** `python -m engine.cli --help` ≡ `hdctl --help` (exit 0).  
  **QA status:** expected PASS for `CLI_PYPROJECT_ENTRYPOINT_OK`, `CLI_INSTALL_OK`, `CLI_MODULE_RUN_OK`, `CLI_HELP_EXIT_0_OK`, `CLI_HELP_STDOUT_OK`.  
* **Governed installability proof (normative).** `CLI_INSTALL_OK` evidence for the shipped console entrypoint MUST be positive and MUST NOT rely on skipped console checks. Governed installability artifacts are `artifacts/cli/install/entrypoints.txt` and `artifacts/cli/install/installability_summary.json`. The proof run MUST use a deterministic editable-install path (`PIP_NO_INDEX=1`, `--no-deps`, `--no-build-isolation`), require `console_entrypoint_available=true`, and keep module and console help/version facts single-sourced and internally coherent across the installability artifacts.  
* **`--help` / `-h`** — for the root or a registered subcommand, print deterministic, nonempty UTF-8 usage/help text to stdout, LF-only and ending in one LF; leave stderr empty and exit 0\.  
* **`--version`** — in the valid root invocation form, print exactly one deterministic, nonempty UTF-8 version/build line ending in one LF to stdout; leave stderr empty and exit 0\. An invalid `--version` plus command combination remains a usage error.  
* **Environment gate** — the CLI must **not** alter SAFE rails or emit bytes outside the declared carrier contract. All governed JSON output comes from the **single presenter/emitter** (see §6); help, version, and Aux narrative text use their owning deterministic text paths.  
* **Input normalization** — the CLI prepares normalized inputs (**order-neutral AB↔BA**) before invoking the engine.

### **3.1.1 Closed exit-0 success carriers**

On exit 0, every CLI mode MUST emit exactly one carrier declared by its command contract and MUST leave stderr empty. This set is exhaustive; a new carrier requires an explicit PF05 contract change.

| Carrier ID | Exact permitted surface | Stdout contract |
| :---- | :---- | :---- |
| `canonical_json` | Every ordinary machine-readable success surface, including compat, Reader-on-stdout where defined, BodyGraph, sampler, conjunction, admin JSON, and file-write receipts | Exactly one canonical JSON object or array: UTF-8, compact, ASCII-sorted keys, and exactly one trailing LF |
| `help_text` | Root and registered-subcommand `-h` or `--help` | Deterministic, nonempty human-readable UTF-8 usage/help text; LF-only; final LF required; multiline allowed |
| `version_text` | Root `--version` in the valid version invocation form | Exactly one deterministic, nonempty human-readable UTF-8 version/build line ending in one LF |
| `aux_narrative_text` | `hdctl aux-preview` narrative-output mode only | Exact governed Aux narrative transport bytes; UTF-8, LF-only, no ANSI; when nonempty, exactly one final LF |
| `aux_suppressed_empty` | `hdctl aux-preview` narrative-output mode only, and only for the governed suppressed result | Zero stdout bytes |

For every carrier, exit status is 0, stderr is empty, diagnostics are excluded from stdout, terminal-control bytes are forbidden, output is deterministic under the command's build, pack, input, and environment pins, and no secret or unowned PII is emitted.

**File-output rules.** A command that already emits primary canonical JSON and also writes a sidecar retains the primary JSON without adding a receipt. A command whose only successful product is one or more files emits one command-owned canonical JSON receipt after every required write succeeds. Aux narrative remains the sole stdout carrier when an admin sidecar is requested; no receipt is appended. A failed or partial write is nonzero with empty stdout. Human file-success synopses, generic empty stdout, and every undeclared non-JSON carrier are forbidden. The exact receipt schema remains in the command contract and its schema home.

**Aux suppression boundary.** Empty stdout is allowed only when the governed Aux result is suppressed. It MUST NOT represent a missing output selection, unimplemented branch, skipped write, swallowed exception, or no-op invocation. An Aux form selecting neither narrative stdout nor valid file output fails as usage.

**Repository posture at `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a` (informative).** Static inspection confirms successful argparse help text, a one-line root version path, raw Aux narrative output, governed Aux-suppressed empty output, and canonical-JSON paths for ordinary machine success. It also finds an additional Aux pair-file path that can exit 0 without stdout and no closed, carrier-specific enforcement across all modes. The repository therefore does not yet conform to the exhaustive carrier contract; this statement does not claim runtime behavior or test passage.

## **3.2 Input forms (files vs inline) \[Required-Now\]**

Input methods for commands that compare or display charts. Titles-only pointers; no transport bytes restated here.

### **Files (Required-Now)**

* **File arguments.** Commands accept file paths to **canonical chart JSON** (e.g., `--a <path>`, `--b <path>`).  
    
* **Schema gate.** Each file must validate against its owning chart JSON Schema (titles-only pointer; schema lives in **HDE-Schemas & Artifacts**).  
    
* **Canonical JSON gate.** Files must be UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays-as-sets deduped & ASCII-sorted (see **HDE-Schemas & Artifacts** §4).  
    
* **Typed input error on failure.** Missing/unreadable file, non-JSON, schema failure, or canonicalization failure → **typed input error** (stderr code string token; no JSON envelope; see §3.4) on **stderr**; **stdout empty**.  
    
* **Locale.** Parsing/validation and byte checks run under `LC_ALL=C`.

  ### **Time-zone overrides (when allowed)**

**Status.** Required-Now implementation gap. The contract below is normative; it does not claim that the selected flags, resolution algorithm, provenance, or refusal codes are implemented at the pinned commit.

* **No default birth timezone.** PF05 MUST NOT use UTC, process `TZ`, server or container local time, a viewer or device zone, an IP-derived zone, a fixed offset, or an abbreviation as a person's birth timezone.  
* **Qualifying sources and precedence.** Resolve each raw birth tuple independently using `explicit override > stored birth-event IANA timezone > deterministic location-derived IANA timezone`. A qualifying explicit override is a valid `--a-tz` or `--b-tz` value on a command path that recalculates from raw birth data and can honor it. A stored zone must belong to the same canonical birth event. A derived zone must come from the normalized birth location or coordinates through a sanctioned resolver with pinned data provenance.  
* **Invalid higher-priority source.** An invalid explicit or stored zone MUST fail; it MUST NOT fall through to a lower-priority source. Approved IANA link aliases MAY normalize only through an exact mapping in the pinned timezone data. Case-folding, spelling correction, substring matching, and implicit alias invention are forbidden.  
* **Stored/derived conflict.** Without an explicit override, canonical stored and derived zones that differ MUST fail with `ERR_TIMEZONE_CONFLICT`, even when their UTC offsets happen to match at the supplied instant. A valid explicit override resolves this conflict and its use is recorded in calculation provenance.

#### **Resolution algorithm**

1. Validate the calendar date and wall-clock time.  
2. Select and validate a qualifying timezone source under the precedence above; when neither override nor stored zone exists, require exactly one place and one derived canonical IANA zone.  
3. Resolve the local date, local time, and selected zone under pinned timezone data.  
4. Require exactly one real UTC instant. A fold MUST fail with `ERR_LOCAL_TIME_AMBIGUOUS`; a gap MUST fail with `ERR_LOCAL_TIME_NONEXISTENT`; malformed or impossible calendar or wall-clock input MUST fail with `ERR_LOCAL_TIME_INVALID`. The implementation MUST NOT select a default fold, assume standard or daylight time, or shift across a gap.  
5. Bind the selected IANA zone, source class, resolved UTC offset, resolved UTC instant, and timezone-data version to calculation provenance. Exact schema fields and placement remain in the owning schema home.  
6. Only then may chart calculation, or a vendor path demonstrably preserving the same resolved semantics, proceed.

#### **Typed refusal codes**

| Code | Exact condition |
| :---- | :---- |
| `ERR_TIMEZONE_REQUIRED` | No explicit override, no stored birth-event timezone, and no birth location is available for derivation |
| `ERR_TIMEZONE_INVALID` | A supplied explicit or stored identifier is invalid under the pinned IANA identifier and alias contract |
| `ERR_LOCATION_AMBIGUOUS` | The birth location does not resolve uniquely enough to select one timezone |
| `ERR_TIMEZONE_UNRESOLVED` | A unique normalized location is available but the sanctioned resolver returns no canonical IANA zone |
| `ERR_TIMEZONE_CONFLICT` | Stored birth-event timezone and deterministic location-derived timezone disagree, with no explicit override |
| `ERR_LOCAL_TIME_AMBIGUOUS` | Local date/time and zone map to two real UTC instants |
| `ERR_LOCAL_TIME_NONEXISTENT` | Local date/time and zone map to no real UTC instant |
| `ERR_LOCAL_TIME_INVALID` | Calendar date or wall-clock time is malformed, out of range, or impossible |
| `ERR_TIMEZONE_OVERRIDE_UNSUPPORTED` | The command, source path, or precomputed input cannot actually apply the override |

* **Missing and unavailable resolution.** Missing location produces `ERR_TIMEZONE_REQUIRED`; ambiguous location produces `ERR_LOCATION_AMBIGUOUS`; a unique location with no resolved zone produces `ERR_TIMEZONE_UNRESOLVED`. Operational resolver-data or service failure uses the owning internal/provider error boundary and MUST NOT be mislabeled as user input or defaulted to UTC.  
    
* **Precomputed and vendor boundaries.** `--a-tz` and `--b-tz` apply only to qualifying raw-birth recalculation paths. A full precomputed chart on a non-recalculation path, or a vendor path that cannot demonstrably honor the selected zone or exact instant, MUST refuse the override with `ERR_TIMEZONE_OVERRIDE_UNSUPPORTED`; it MUST NOT accept and ignore the flag or relabel computed mechanics.  
    
* **Governance dependency.** These exact order-neutral strings are selected for the PF05 contract, but the global error-token roster remains owned by **HDE-Governance**. Before implementation emits them or conformance evidence claims them, Governance MUST register them through its authorized maintenance path. Once registered and implemented, a code is emitted as exactly one LF-terminated stderr line on the command's owned nonzero failure exit, with stdout empty.  
    
* **Repository posture at `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a` (informative).** No `--a-tz` or `--b-tz` parser option, end-to-end source precedence, UTC-instant resolution, fold/gap handling, timezone-data version, or selected refusal code was found in the inspected repository. The checked-in timezone list is an unversioned five-entry identifier array, and a legacy vendor path explicitly ignores `tz`. The checked-in error map contains `ERR_READER_MISSING_TZ_A` and `ERR_READER_MISSING_TZ_B`; those implementation facts do not replace the selected order-neutral PF05 codes, and any retention, aliasing, migration, or removal remains Governance-owned. These bounded static findings establish an implementation gap, not runtime behavior.

  ### **Inline JSON (Speculative)**

* Not defined in this version. If added later, must use the **same schema/canonicalization gates** as file inputs and follow the same **typed-error** posture. Track as **\[OPEN\]**.

  ### **Aliases policy (inputs)**

* **\[OPEN\] decision.** If input-only aliases are accepted, they must normalize via declared alias ledgers (titles-only to **HDE-Schemas & Artifacts** A1/A4/A5) and outputs remain canonical.  
    
* **v1 default (current):** unknown IDs **hard-fail** with a typed input error; no implicit aliases unless an explicit allow-list is adopted.

  ### **Validation (binary)**

1. **Exists/reads OK:** file present and readable.  
2. **JSON/Schema OK:** parses as JSON and passes the owning chart schema.  
3. **Canonical JSON OK:** UTF-8, no BOM, sorted keys, compact, one LF; arrays-as-sets deduped & ASCII.  
4. **Timezone resolution:** for every qualifying raw-birth recalculation, validate source precedence, IANA identity, stored/derived agreement, unique place and zone, fold/gap behavior, and one resolved UTC instant; bind the selected zone, source, offset, instant, and timezone-data version to provenance. Any selected typed refusal emits one LF-terminated stderr code and leaves stdout empty.  
5. **Streams:** on any input error, stderr carries the typed error; stdout empty.

**Routing (titles-only).** Canonical JSON rules & chart schemas: **HDE-Schemas & Artifacts**. Governance tokens: **HDE-Governance** (§2.0).

## 3.3 Streams discipline (stdout / stderr) \[Required‑Now\]

**Rules for command output streams.** Transport acceptance (A7) lives in HDE‑Governance; do not restate it here. Serialization rules are in §6.1/§6.2.

### **Success → stdout**

* On **exit 0**, each command mode emits exactly the success carrier declared by its contract to `stdout` and leaves `stderr` empty. The exhaustive carrier set is in §3.1.1.  
    
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

1. **Success (0):** `stdout ==` the command mode's declared §3.1.1 carrier bytes (byte-for-byte); `stderr` empty.  
     
   * For Reader‑envelope commands, the canonical success payload is the six‑key Reader v1 body (§5.1).  
       
   * For `hdctl showcompat`, the canonical success payload is compat JSON stdout (§4.1/§5.1).

   

2. **Error/usage:** a typed failure emits exactly one LF-terminated canonical code token on `stderr`; a usage failure emits one LF-terminated synopsis; `stdout` is empty in both cases.  
     
3. **No ANSI / no extra lines:** grep-guards block escape sequences; every nonempty carrier ends in exactly one LF, while governed Aux-suppressed output is exactly zero bytes.  
     
4. **Canonical compare:** re-serialize `canonical_json` payloads and byte-compare them (must match); validate each non-JSON carrier against its declared byte contract. Checks run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
     
5. **Reader parity:** for any surface that emits Reader v1 bytes (Reader HTTP \+ CLI reader‑dump surfaces), those bytes are **byte‑identical** across Reader and CLI for identical inputs/environment.  
     
6. **Determinism:** two‑run identity holds for both success and error paths.

**Routing (titles‑only).** Canonical JSON rules and chart schemas live in **HDE‑Schemas & Artifacts**; governance tokens and A7 posture live in **HDE‑Governance**.

## **3.4 Exit codes taxonomy \[Required−Now\]**

Exit codes are exhaustive for the public surface. Non-zero exits must not print partial payloads on stdout. JSON emitted on stdout uses the single presenter/emitter (§6.2) and canonical JSON (§6.1).

#### **Codes**

* `0` — Success. `stdout` is exactly the mode's declared §3.1.1 carrier; `stderr` is empty. Ordinary machine success and file-only receipts use one LF-terminated canonical JSON value.  
    
* `64` — Usage. `stderr` is a short human synopsis; `stdout` empty.  
    
* Other non-zero exit codes are command-specific. On failure, `stderr` contains exactly one line: a single code string token, LF-terminated (no JSON envelope); `stdout` empty.

#### **Global rules**

1. **No mixed streams:** stdout is reserved for success payloads only; all failures write only to stderr.  
     
2. **No ANSI/no control bytes:** `stderr` MUST be plain UTF-8 text; do not emit colors, cursor codes, or progress spinners.  
     
3. **Exactly one trailing LF:** every nonempty stdout carrier and every stderr usage synopsis or error code string must end with exactly one LF. Governed Aux-suppressed output is exactly zero bytes.  
     
4. **No partial carriers:** if an error occurs after emitting any stdout bytes or before required file writes complete, the command MUST treat that as failure and MUST leave stdout empty; it MUST NOT leave partial JSON, text, or a premature file receipt.

#### **Validation (binary)**

1. **Success:** If `exit=0`, assert that exactly one declared §3.1.1 carrier is present and `stderr` is empty. For `canonical_json`, parse and round-trip byte-identically under the owned canonical serializer. Validate help, version, Aux narrative, and governed Aux suppression against their carrier-specific byte contracts.  
     
2. **Usage:** If `exit=64`, assert `stderr` is human text and ends with one LF; assert `stdout` empty.  
     
3. **Failure:** If `exit!=0` and `exit!=64`, assert `stdout` empty; assert `stderr` is exactly one non-empty LF-terminated line containing a single code string token.  
     
4. **Token correctness:** For failures, assert the stderr code string token is stable, numeric-free, and listed in the command contract. If the failure maps to an HTTP `error_v1`, assert the token matches the transport `error_v1.code`.  
     
5. **Determinism:** two-run identity holds for every success and error path. AB↔BA identity applies to pair-sensitive data outputs and order-neutral error codes; help and version have no party order, and Aux narrative parity follows its owning narrative and perspective contract.

**Routing (titles-only).** Canonical JSON rules: HDE-Schemas & Artifacts. A7 transport rules and SAFE rails: HDE-Governance and §5.3 of this document.

---

## **3.5 Single-emitter parity with Reader**

* **One JSON entrypoint.** Governed CLI and Reader JSON bytes MUST be emitted via the byte-authoritative presenter/emitter entrypoint defined in §6.2. Wrapper envelope builders MAY exist (for example Reader v1 envelope emission), but they MUST delegate JSON byte emission to the byte-authoritative entrypoint and MUST NOT serialize governed JSON outside it. Canonical JSON output is UTF-8, ASCII-sorted by key, compact, and terminated by exactly **one LF**. Help, version, and Aux narrative text follow their §3.1.1 carrier contracts and are not forced through JSON serialization.  
    
* **No ad-hoc JSON serialization.** Forbid `json.dumps(`, `jsonify(`, templating, or any local “mini-emitters” on governed JSON paths.  
    
* **Symbol allow-list and CI guard.** Pin the allow-listed presenter/emitter emission symbol(s) as the only permitted governed JSON serializer entrypoint. CI must fail if governed JSON paths reference non-allow-listed serializer symbols or contain disallowed patterns (grep-guard). Validation must assert that CLI and Reader governed JSON bytes are emitted via the byte-authoritative entrypoint, that wrappers delegate without alternate JSON serialization, and that the declared text carriers use only their owning byte paths.  
    
* **Preimage recipe.** Build the preimage as defined in **PF01** (do not restate fields here), compute `idempotence_hash`, then re-emit the final six-key body.  
    
* **Determinism & parity.** The single byte-authoritative JSON emitter ensures Reader↔CLI byte equality for Reader-v1 bytes, AB↔BA identity for pair-sensitive JSON, and two-run identity for identical inputs and environment. Every non-JSON carrier independently satisfies its owning §3.1.1 determinism and parity contract.  
    
* **Evidence.** Provide (1) a grep-guard report, (2) import-graph or reflection proof that every governed CLI and Reader handler calls only allow-listed emission symbols and that wrappers delegate byte emission to the byte-authoritative entrypoint, and (3) byte-compare fixtures showing that Reader-v1 bytes written by `hdctl showcompat --dump-reader <path>` equal the Reader response body. Evidence identities and paths are indexed through **HDE-Schemas & Artifacts**.

  ## **3.6 Determinism expectations for stdout**

* **AB↔BA parity.** For pair-sensitive data outputs with identical inputs differing only by pair order, stdout bytes are identical, including the single trailing LF. Help and version have no party order; Aux narrative parity follows its owning narrative and perspective contract.  
    
* **Two-run identity.** Running the same command twice with the same inputs/environment produces byte-identical stdout.  
    
* **Carrier, schema & shape gates.** Stdout must validate the **owning carrier and command contract**:  
    
  * For Reader-envelope-on-stdout surfaces (if any exist), stdout must satisfy the six-key Reader v1 covenant in §5.1.  
  * For `hdctl showcompat`, stdout must satisfy the compat JSON contract in §4.1/§5.1 and must **not** be required to match the Reader v1 six-key covenant (Reader v1 bytes are produced via the reader-dump path).  
  * Any contract or canonicalization violation results in a single stderr code string token (no JSON envelope) with an exit code pinned by the command contract (see §3.4); stdout must be empty on failure.


* **Locale/TZ pins.** All CLI byte comparisons run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`. The process `TZ=UTC` pin controls environment determinism only and MUST NOT be used as a person's birth timezone.

### **Dependent reconciliation outside this selection**

The §3.1.1 carrier set controls globally, but the unselected `bg:export-json` wording in §4.8 still permits empty stdout or a human synopsis for file success, and the unselected `admin-bundle` wording in §4.9 still permits a human file-success synopsis. Those command sections remain unchanged in this selection and require later in-owner reconciliation: each file-only success MUST emit a command-owned canonical JSON receipt after all required writes complete.

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

---

## 4.1 hdctl showcompat \[Partially Implemented; Required‑Now\]

### 4.1.1 Purpose and posture (normative)

`hdctl showcompat` is the canonical compat harness for:

* Computing the full Magic‑10 compat result (scores, bands, narrative keys) for a pair of BodyGraphs; and  
    
* Producing both:  
    
  * **Compat JSON** on stdout for admin/QA (full compat detail: all categories, bands, scores, narrative keys); and  
      
  * An optional **Reader v1 success envelope** (six‑key, numeric‑free) via its **reader‑dump** path, byte‑identical to the Reader API.

It is an admin/QA tool, not a public API. It is **registered but materially partial** in the CLI and remains **merge‑blocking** until determinism and Reader↔CLI parity tokens are proven green.

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
      
  * `auto` — DB-only; vendor fallback is prohibited. Birth-based vendor resolution requires explicit `--source vendor`. This is the same source-selection policy as `bg:resolve` (§4.6).


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

* ## Treat arrays that represent sets as deduped and ASCII-sorted.

**1\) Compat JSON — stdout (primary)**

On success, and **in the absence of explicit reader-dump overrides**, `showcompat` **MUST** write a single LF-terminated compat JSON object to **stdout**, and **MUST NOT** print the Reader v1 envelope directly to stdout.

**Closed governed result contracts (normative).**

`magic10_result.v1` exists only for an eligible distinct-person pair. Its top-level object has `additionalProperties: false` and exactly `schema`, `config_id`, `release_id`, `pair_key`, `signals`, and `categories`. `schema` is `magic10_result.v1`; `release_id` and `pair_key` are lowercase 64-hex; `signals` has exactly twenty rows in flattened caps-input order; and `categories` has exactly ten rows in `catalog/magic10.json` order.

Each signal row has exactly `signal_id` and `q`, with integer `q` in `0..200`. Each pure category row has exactly `category_id`, integer `score` in `0..100`, and `band` in `{Cool, Open, Warm, Glow}`. The pure result contains no names, UIDs, timestamps, viewer preferences, copy, personal keys, shared keys, request metadata, or mutable configuration handles.

`magic10_compat_result.v1` is the symmetric complete internal/admin result and also exists only for an eligible pair. It has the same top-level identity fields and signal array, with `schema` fixed to `magic10_compat_result.v1`. Each category row has exactly `category_id`, `score`, `band`, required nonempty `shared_key`, required nonempty `personal_lo_to_hi_key`, and required nonempty `personal_hi_to_lo_key`.

The narrative router augments, but does not rescore or otherwise change, the pure result. It orders parties by `(gate_mask, canonical_person_id)`; for distinct equal-mask parties, ASCII canonical UUID order decides `lo` and `hi`. The normalized `a_to_b` key is `personal_lo_to_hi_key`, the normalized `b_to_a` key is `personal_hi_to_lo_key`, and both calls must return the same `shared_key` or augmentation fails closed. A caller-specific projection selects its personal key by comparing its canonical UUID with the transient normalized orientation and may not rewrite the symmetric stored result. The router does not change `q`, score, band, order, `config_id`, `release_id`, or `pair_key`. Reversing request order produces byte-identical complete-result bytes. The augmented result is assembled per eligible evaluation and must not be cached or retrieved solely by the identity-free intrinsic `pair_key`. A valid self-pair has no `magic10_result.v1` or `magic10_compat_result.v1`.

**CLI full-matrix diagnostic.**

For an eligible pair, ordinary `hdctl showcompat` stdout is one canonical `magic10_compat_result.v1` document. It has no enclosing `a`, `b`, `viewer_prefs`, `compat`, or CLI-identity `meta` wrapper. This numeric full-matrix result is restricted to internal/admin CLI use and must never be substituted for Reader v1 public bytes.

Existing viewer-preference validation and normalization remain input-side handoffs for sampler/ranker workflows, including preservation of weight-0 semantics; viewer preferences do not enter intrinsic scoring, add fields to either governed result, or create a second CLI/presenter zero-weight exclusion home. CLI-local identity context, when needed for evidence tagging, remains separate from the complete-result bytes and does not establish remote production identity.

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
* `"reader_version": "v1",`  
* `"eligible": <ELIGIBILITY_VALUE>,`  
* `"categories": [ { "id": "harmony", "band": "Cool|Open|Warm|Glow" } or [] ],`  
* `"meta": { "engine_tag": "<ENGINE_TAG>", "invocation_tag": "<INVOCATION_TAG>" },`  
* `"release_id": "<hex64>",`  
* `"idempotence_hash": "<hex64>"`  
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

* **Implementation status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c`:** Registered but partially implemented.  
* **Statically confirmed:** the packaged `hdctl` entrypoint and `showcompat` parser exist; compat stdout, Reader dump, and admin-dump paths are wired; compat stdout and Reader dump use the canonical presenter.  
* **Required gaps:** category scores are derived from a stable pair/category hash rather than full BodyGraph mechanics; file/stdin mode does not retain full BodyGraph topology; stdout `a`/`b` are not resolved BodyGraphs; the adopted explicit stdin/user flag spellings, file canonical-byte/schema gates, and stdin schema/shape validation are absent; `auto` can select vendor from birth inputs; conjunction passes viewer preferences despite the ignore rule; admin sidecars bypass the presenter; and help describes Reader bytes rather than compat stdout.  
* **Evidence posture:** checked-in tests and artifacts record intended canonical/parity behavior, but their presence is not a runtime PASS or acceptance-token attestation.

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
    
* Emit, under governed repo paths (for example `artifacts/hdctl/<RUN_ID>` or `artifacts/qa/<RUN_ID>` — exact locations and schemas are owned by **HDE-Schemas & Artifacts**):  
    
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

**Contract status (informative).** No detailed invocable contract is adopted in this version. Exact flags, chart schema, stdout shape, typed error tokens/exit codes, and acceptance evidence remain OPEN for the future Doc-Delta that promotes this command from Speculative. Any future contract MUST use the shared presenter and the global canonical-byte/stream rules.

Implementation status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c` (informative): **Not found in the inspected packaged parser**; absence is not a current defect while the command remains Speculative.

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
  * `bg:resolve --source vendor` configured-v2 route-policy boundary — configured v2 bases use the version-neutral `charts` resource path, route-metadata `Authorization: Bearer` auth posture, geocode posture, and deterministic v2 `ChartResult` adapter. `--dry-run` performs no DB write. Non-dry-run configured-v2 mapped-cache persistence requires explicit `--upsert`, open rails, non-production posture in both the requested and process environments, an available sanctioned `DBAccess` target, and a successful adapter mapping. Missing upsert intent or production-like posture fails closed with `PROVIDER_WRITE_UNSUPPORTED`. The bounded write stores only adapter-mapped HDE BodyGraph/cache data, verifies canonical write/read-back parity, one-row identity, and idempotence, and never persists raw vendor envelopes or secret-bearing material. Generic legacy BodyGraph ingest is guarded from v2 chart routing and MUST NOT compose legacy `bodygraphs` resource paths against a configured v2 base. Non-v2 configured bases MAY preserve the legacy BodyGraph route only as explicit legacy fallback. This route policy preserves HD Engine ownership of vendor acquisition and BodyGraph resolution, keeps secrets and raw payloads out of evidence, and preserves nonclaims for broad HumanDesignAPI v2 platform conformance, public Reader changes, public routes, public payload changes, new HTTP homes, app-side vendor credential ownership, raw payload persistence, and AI scope.  
  * `auto` — DB-only; vendor fallback is prohibited. Current repository behavior treats `auto` as the no-I/O DB stub. When the DB path performs direct PostgreSQL access, an absent, invalid, unavailable, or unauthorized direct endpoint MUST fail closed without vendor or alternate-transport selection, and retired bridge keys MUST fail before provider construction or I/O (HDE-Mechanics Guide; titles-only).


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

| Command/surface | Status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c` | Contract note |
| :---- | :---- | :---- |
| `hdctl showcompat` | Registered; materially partial | See §4.1.6 for semantic, input, source, presenter, and help gaps. |
| `hdctl aux-preview` | Registered | Required-Now admin preview surface; no broader PASS claim is made here. |
| `hdctl bg:resolve` | Registered; materially partial | DB/auto is a no-I/O stub; failure streams diverge. |
| `hdctl dev:sampler` | Registered; materially partial | Deterministic core exists; presenter, input-gate, and error-mapping gaps remain. |
| `hdctl admin-bundle` | Required-Now; not found | The complete command contract is in §4.9; no implementation or conformance claim is made. |
| `POST /internal/admin/bundle/v1` | Required-Now; not found | The complete transport contract is in §4.9; no route, runtime, or deployment claim is made. |
| `hdctl bg:export-json` | Speculative; not found | Absence is not a current implementation defect. |
| `hdctl read singlebg` | Speculative; not found | No detailed invocable contract is adopted. |
| `hdctl list people` | Speculative; not found | No implementation is required by current status. |
| Fetch person/batch | Speculative/disabled; not found | No implementation is required by current status. |

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
    
* Write a **single BodyGraph export JSON file** under a governed path (for example `artifacts/hdctl/bg_export/<RUN_ID>` or `artifacts/qa/<RUN_ID>`; exact path and schema are owned by **HDE-Schemas & Artifacts**), containing:  
    
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

* On success: after the export file is written successfully, `stdout` MUST contain one canonical JSON receipt with exactly one trailing LF and `stderr` is empty. The command-owned receipt schema remains OPEN for the future Doc-Delta that pins the invocable command contract.  
    
* On typed failure: exit 2; `stderr` contains exactly one LF-terminated canonical code token (no JSON envelope), and `stdout` is empty. Usage errors follow the exit-64 synopsis rules in §§3.3-3.4.

### **4.8.3 QA usage and evidence (titles-only)**

**QA harness role.**

* `hdctl bg:export-json` is the **first leg** of the stateless QA pipeline:  
    
  * birth (or vendor BodyGraph) → `bg:export-json` → BodyGraph export JSON → `showcompat` stateless compat export (§4.1.7) → compat JSON \+ Reader v1 envelope files.


* QA plans defined in **Glow QA Guide** and epic records in **HDE-Phased Epics** will use this pipeline to test BodyGraph, compat, and narratives **without DB**.

**Evidence & schemas.**

* Schemas for BodyGraph export JSON and any “run bundle” composite artifacts are owned by **HDE-Schemas & Artifacts**; PF05 **must not** define those schemas.  
    
* Evidence index entries (for example “BodyGraph export JSON golden”, “stateless run bundle”) live in **PF12**; this section simply requires that the CLI surfaces exist and honour canonical JSON and no-DB semantics.

### **4.8.4 Implementation status (gap record)**

* **Current status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c`:** Not found in the inspected packaged parser; no `bg:export-json` subcommand is registered in `engine/cli/main.py`. This bounded static finding does not claim runtime state or establish the absence of every possible ad hoc artifact.  
    
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
      
  * three narrative composition results for the match, each expressed as a PF12-owned `Text` or `Suppressed` result  
      
  * a closed meta block with engine identity, invocation identity, content identity, build identity, bundle source, and rails context


* Emit that composition as a single canonical JSON object (the admin bundle) for admin, QA, and internal product use.

Posture:

* Admin-only surface. The admin bundle is explicitly not a public Reader response and is not subject to the public numeric-free covenant. It may contain numeric scores and narrative text.  
    
* Pre-Glow product requirement. A build that cannot produce admin bundles via hdctl admin-bundle against Railway prod is considered unusable pre-Glow, regardless of any Admin GUI.  
    
* Not an A7 surface. Admin bundle transport is not part of the A7 proof surface; A7 proofs remain on cataloged Reader JSON success routes only.

The mechanical implementation of the admin bundle builder (pure function or module inside the engine) is owned by the HDE-Mechanics Guide. This section defines the CLI contract that uses that builder.

**Implementation status at `main@932aebf48c6e0de518d3c452f5ffa451475d0f2c` (informative).** Required-Now and not found in the inspected repository: the packaged parser in `engine/cli/main.py` does not register `admin-bundle`; `adapter/http_reader.py` does not define `/internal/admin/bundle/v1`; the five exact PF12 schema paths selected below return absent; and `errors/token_map/token_map.json` does not register the new admin-bundle token set. These bounded static findings do not claim runtime behavior, deployment, test passage, QA, acceptance, or token satisfaction.

### **4.9.2 Selected architecture**

There is one v1 computation path:

1. `hdctl admin-bundle` is a thin authenticated HTTP client.  
2. It always calls `POST /internal/admin/bundle/v1` on the configured HDE service.  
3. The HTTP adapter authenticates and validates, resolves the two raw birth inputs to canonical BodyGraphs, then invokes the one pure `admin_bundle_v1` builder.  
4. The builder receives canonical resolved values and stable release context. It performs no HTTP, filesystem, database, environment, clock, random, logging, or audit I/O.  
5. The existing canonical presenter/emitter serializes the builder result exactly once.  
6. HTTP returns those bytes. The CLI validates and copies the HTTP entity-body bytes verbatim; it never reconstructs or reserializes a successful bundle.

There is no local CLI fallback, direct CLI vendor path, composition of multiple CLI commands, alternate emitter, or source-dependent builder. A remote failure is a typed failure, not permission to calculate a substitute locally. This choice is what makes authentication universal and CLI/HTTP bundle parity mechanically provable.

Resolver/vendor I/O belongs outside the pure builder. PF14 must clarify its currently contradictory wording that the builder both “uses resolvers” and “does not perform I/O”: the adapter/orchestrator may resolve; the builder receives resolved canonical BodyGraphs.

### **4.9.3 Exact CLI grammar**

The only v1 invocation forms are:

```
hdctl admin-bundle \
  --births-file PATH \
  --viewer-prefs-file PATH \
  [--a-tz IANA_ZONE] [--b-tz IANA_ZONE] \
  [--out PATH [--force]]
```

or:

```
hdctl admin-bundle \
  --birthdate-a YYYY-MM-DD --birthtime-a HH:MM --location-a LOCATION \
  --birthdate-b YYYY-MM-DD --birthtime-b HH:MM --location-b LOCATION \
  --viewer-prefs-file PATH \
  [--a-tz IANA_ZONE] [--b-tz IANA_ZONE] \
  [--out PATH [--force]]
```

These spellings are exact. V1 defines no aliases.

#### 4.9.3.1 Mutual exclusion and precedence

| Rule | Decision |
| :---- | :---- |
| Pair input | Exactly one family is required: `--births-file`, or all six inline birth flags. |
| Partial inline input | Usage error, exit `64`. All six inline flags form one indivisible group. |
| Mixed file/inline input | Usage error, exit `64`. `--births-file` excludes every inline birth flag. |
| Viewer preferences | `--viewer-prefs-file` is always required. There is no neutral or equal-weight default. |
| Time-zone override | `--a-tz` and `--b-tz` may accompany either input family. Each becomes that party’s `timezone_override`; it does not mutate a stored `timezone` value. |
| Time-zone precedence | Exact existing PF05 rule: explicit override \> stored birth-event IANA timezone \> deterministic location-derived IANA timezone. A valid override resolves a stored/derived conflict. |
| Output | Without `--out`, the bundle entity body is stdout. With `--out`, the bundle goes only to that file and stdout is only the receipt. |
| Overwrite | Existing destinations are refused by default. `--force` is legal only with `--out`. |
| Standard streams as paths | `PATH` cannot be `-`; stdin/stdout pseudo-paths are not aliases. |
| Source selection | No `--source`, `--local`, `--vendor`, `--base-url`, `--token`, user-ID, BodyGraph-file, fixture, or debug flag exists in v1. |
| Future user model | User-ID inputs require a new versioned contract; they cannot be added silently to `admin_bundle_request_v1`. |

Argument-grammar violations are usage errors: exit `64`, empty stdout, and one short LF-terminated stderr synopsis. The synopsis may name an offending option but MUST NOT echo a birthdate, birthtime, location, timezone, token, or file content.

All non-usage failures use exit `2`, empty stdout, and exactly one canonical `ERR_*` token plus one LF on stderr. This preserves the currently selected command-specific exit code while reconciling the old JSON-on-stderr prose to PF05’s controlling single-token carrier.

### **4.9.4 Exact input schemas and normalization**

All new schemas are JSON Schema Draft 2020-12, closed with `additionalProperties: false`, and reject duplicate object keys. Their PF12 artifact homes are:

- `schemas/admin_bundle.births.v1.json`  
- `schemas/admin_bundle.request.v1.json`  
- `schemas/admin_bundle.response.v1.json`  
- `schemas/admin_bundle.receipt.v1.json`  
- `schemas/admin_bundle.audit.v1.json`

PF12 must register these artifacts before implementation can claim schema conformance. The selected shapes are not open decisions; artifact publication is a dependent documentation/implementation action.

#### 4.9.4.1 `admin_bundle_births_v1` file

The births file contains exactly:

```json
{
  "a": {
    "birthdate": "1990-01-02",
    "birthtime": "03:04",
    "location": "Rabat, Morocco",
    "timezone": "Africa/Casablanca"
  },
  "b": {
    "birthdate": "1991-05-06",
    "birthtime": "07:08",
    "location": "Lisbon, Portugal"
  },
  "schema": "admin_bundle_births_v1"
}
```

`a`, `b`, and `schema` are required. Each party requires exactly `birthdate`, `birthtime`, and `location`; `timezone` is the sole optional property. `timezone_override` is forbidden in this file because CLI `--a-tz`/`--b-tz` is the explicit override carrier.

#### 4.9.4.2 Viewer-preference file

The viewer-preference file is the existing PF12 object, with exactly these two keys:

```json
{
  "top_category": "harmony",
  "weights": {
    "alignment": 50,
    "balance": 50,
    "comfort": 50,
    "communication": 50,
    "consistency": 50,
    "creativity": 50,
    "drive": 50,
    "expansion": 50,
    "harmony": 50,
    "heat": 50
  }
}
```

`top_category` is one exact Magic-10 ID. `weights` contains every and only the ten IDs. Each weight is a JSON integer `0..100`; booleans are invalid. Zero is preserved and never promoted to a default.

The frozen semantic category order is:

1. `harmony`  
2. `heat`  
3. `communication`  
4. `alignment`  
5. `comfort`  
6. `consistency`  
7. `expansion`  
8. `creativity`  
9. `drive`  
10. `balance`

Object keys still serialize in ASCII order. The order above controls schema-declared category arrays and is not replaced by ASCII sorting.

#### 4.9.4.3 HTTP `admin_bundle_request_v1`

The CLI produces, and the HTTP route accepts, exactly:

```json
{
  "a": {
    "birthdate": "1990-01-02",
    "birthtime": "03:04",
    "location": "Rabat, Morocco",
    "timezone": "Africa/Casablanca",
    "timezone_override": "Africa/Casablanca"
  },
  "b": {
    "birthdate": "1991-05-06",
    "birthtime": "07:08",
    "location": "Lisbon, Portugal"
  },
  "schema": "admin_bundle_request_v1",
  "viewer_prefs": {
    "top_category": "harmony",
    "weights": {
      "alignment": 50,
      "balance": 50,
      "comfort": 50,
      "communication": 50,
      "consistency": 50,
      "creativity": 50,
      "drive": 50,
      "expansion": 50,
      "harmony": 50,
      "heat": 50
    }
  }
}
```

Top-level required keys are exactly `a`, `b`, `schema`, and `viewer_prefs`. Each party requires `birthdate`, `birthtime`, and `location`, and may contain `timezone` and/or `timezone_override`. No user ID, `person_uid`, precomputed chart, provider selector, source label, correlation value, or auth value is a body field.

Field rules:

- `birthdate`: exactly `YYYY-MM-DD`; a real date in the proleptic Gregorian calendar; no locale parsing, two-digit years, or auto-correction.  
- `birthtime`: exactly `HH:MM`, `00:00..23:59`; no seconds, offset, abbreviation, AM/PM, or silent rounding in v1.  
- `location`: UTF-8 text normalized to Unicode NFC, outer whitespace removed, no CR/LF/NUL/control character, and `1..256` UTF-8 bytes after normalization. Case, diacritics, and meaningful punctuation are preserved. No fuzzy spelling correction is permitted.  
- `timezone` and `timezone_override`: exact IANA identifiers or an alias explicitly present in the pinned timezone-data alias map. No case-folding, abbreviation, fixed-offset substitute, or guessed alias.

The route accepts semantically valid JSON with arbitrary insignificant whitespace/key order; canonical request bytes are not required from non-CLI clients. It parses with duplicate-key detection, applies the same normalization once, validates the normalized object, and passes only normalized typed data onward. The CLI itself emits its request through the canonical serializer.

The request limit is `32,768` bytes of encoded entity body. UTF-8 BOM, invalid UTF-8, empty body, duplicate key, trailing non-whitespace data, NaN/Infinity, or multiple JSON values is `ERR_ADMIN_BUNDLE_INVALID_JSON`. Unknown keys are not silently removed.

Input files must be regular readable files, UTF-8 without BOM, strict JSON, and no larger than the request limit. The output destination MUST NOT identify either input file.

### **4.9.5 `HDE_BASE_URL` resolution**

`HDE_BASE_URL` is the only base-URL source. Resolution is exact:

1. Read the process environment variable `HDE_BASE_URL` once at command start.  
2. Missing, empty, leading/trailing whitespace, or malformed values fail with `ERR_ADMIN_BUNDLE_CONFIG_INVALID`.  
3. The value must be an HTTPS origin: scheme `https`, nonempty host, optional port, and path either empty or exactly `/`.  
4. Userinfo, query, fragment, other path prefixes, backslashes, and embedded credentials are forbidden.  
5. Normalize the sole optional trailing `/` away, then append exactly `/internal/admin/bundle/v1`.  
6. Do not read a repository endpoints file, `.env`, PF07 prose, vendor base URL, Codespaces URL, localhost, or hard-coded Railway URL as a fallback.

For production, the operator sets `HDE_BASE_URL=https://glow-hdengine-v2-production.up.railway.app`, as currently named by PF07. The CLI does not assume production when configuration is absent.

TLS certificate and hostname verification are mandatory. There is no insecure switch. Redirect following is disabled so an admin bearer credential cannot be forwarded to a different origin. The CLI makes one attempt, with a `5` second connect timeout and `60` second total response timeout; it does not automatically retry a POST whose server-side execution is unknown.

### **4.9.6 Authentication and authorization**

#### 4.9.6.1 Client credential

`HDE_ADMIN_TOKEN` is the only CLI credential source. It is never accepted as an option, URL parameter, cookie, request-body field, or config-file fallback.

The raw value is:

```
<key-id>.<secret>
```

- `key-id`: `[A-Za-z0-9][A-Za-z0-9_-]{0,31}`.  
- `secret`: exactly 32 cryptographically random bytes encoded as 43 unpadded base64url characters.  
- The full token is ASCII and contains no whitespace.

Missing or malformed client credentials fail locally as `ERR_ADMIN_AUTH_REQUIRED` without making a request.

The CLI sends exactly one credential carrier:

```
Authorization: Bearer <HDE_ADMIN_TOKEN>
```

It also sends `Accept: application/json`, `Accept-Encoding: identity`, `Content-Type: application/json; charset=utf-8`, `User-Agent: hdctl/<package-version>`, and one canonical lowercase UUIDv4 `X-Correlation-ID`. It sends no cookies. Authorization scheme comparison follows HTTP’s case-insensitive scheme rule; the CLI emits `Bearer` exactly.

#### 4.9.6.2 Server registries

PF07’s open variables are closed as strict JSON objects:

```
HDE_ADMIN_TOKENS = {
  "ops-01": {
    "client": "hdctl",
    "digest": "sha256:<64-lowercase-hex>"
  }
}

HDE_ADMIN_SCOPES = {
  "ops-01": ["admin:bundle:read"]
}
```

The shown values are structural notation, not literal environment bytes.

- `HDE_ADMIN_TOKENS` maps each key ID to exactly `client` and `digest`.  
- `client` is exactly one of `hdctl`, `admin_gui`, or `automation`.  
- `digest` is SHA-256 of the complete ASCII bearer token, including key ID and dot.  
- `HDE_ADMIN_SCOPES` maps the same key IDs to sorted, duplicate-free registered scope strings.  
- The two key sets must be identical. Duplicate JSON keys, malformed entries, unknown client values, unregistered scopes, or mismatched sets are configuration failures.  
- This route requires exact scope `admin:bundle:read`.

Production must fail readiness/startup if either registry is missing or invalid; it must not register an open or degraded route. Verification uses a constant-time digest comparison, including a dummy digest path for unknown key IDs. Shared credentials are prohibited: each operator/service account and each client class receives a distinct key ID.

Rotation needs no code change: add a new key, distribute it, then remove the prior key through the managed secret configuration. Revocation takes effect when the new configuration is atomically applied; removed key IDs no longer authenticate. Raw tokens and Authorization values are never logged.

Missing, malformed, unknown, revoked, or wrong-secret tokens all return the same `401` body and `WWW-Authenticate: Bearer realm="hde-admin"`. A valid credential lacking the route scope returns `403` and `WWW-Authenticate: Bearer realm="hde-admin", error="insufficient_scope", scope="admin:bundle:read"`. This avoids a credential-validity oracle while preserving the HTTP distinction between authentication and authorization.

The Admin GUI must call this route from a confidential backend. A browser bundle must never receive or retain `HDE_ADMIN_TOKEN`; the HDE route sets no CORS allow headers and accepts no cookie authentication.

### **4.9.7 Exact HTTP contract**

- Method: `POST`  
- Path: `/internal/admin/bundle/v1`  
- Audit route identity: `internal.admin.bundle.v1`  
- Aliases: none  
- Success status: `200`

Request media type is `application/json` with either no charset parameter or `charset=utf-8`; other media types/parameters are rejected. `Content-Encoding` must be absent or `identity`. If `Accept` is present, it must permit `application/json`; absent and `*/*` are acceptable.

Failure precedence for a request containing multiple defects is fixed:

1. path/method routing;  
2. request framing, size, content encoding, media type, and acceptability;  
3. authentication and authorization;  
4. JSON parsing and closed-schema validation;  
5. timezone/domain resolution, dependencies, bundle construction, and required success-audit commit.

Authentication occurs before JSON parsing or mechanics work. The size/framing gate may terminate an oversized request without reading or authenticating its full body.

Every body-bearing response has:

```
Content-Type: application/json; charset=utf-8
Cache-Control: no-store
X-Content-Type-Options: nosniff
X-Correlation-ID: <server-selected-canonical-uuidv4>
Content-Length: <exact LF-terminated entity-body length>
```

It has no `ETag`, `Vary`, `Content-Encoding`, or CORS allow header. The server emits identity bytes even if a caller offers compression. `X-Correlation-ID` is transport/audit data and is never part of the bundle. A valid canonical inbound correlation ID may be retained; an absent, duplicate, or invalid one is discarded without logging its value and replaced by a server-generated UUIDv4.

Only `POST` is allowed. Other methods return `405`, `Allow: POST`, and `ERR_NOT_FOUND`. In accordance with HTTP `HEAD` semantics, `HEAD` returns the same `405` status but no body, `Content-Length: 0`, no `Content-Type`, `Cache-Control: no-store`, no ETag, and `Allow: POST`. Unsupported paths return `404`/`ERR_NOT_FOUND` through the shared error presenter.

### **4.9.8 Resolution, pure builder, and pair normalization**

The adapter performs these operations in order after auth and request validation:

1. Resolve each party independently under PF05’s selected timezone algorithm. Never default to UTC, process/container `TZ`, server locale, device/viewer zone, IP-derived zone, abbreviation, fixed offset, or a guessed location.  
2. Resolve the local date/time to exactly one UTC instant using pinned timezone data. Folds, gaps, invalid higher-priority sources, ambiguous locations, unresolved locations, and unhonored overrides fail with the existing exact timezone tokens.  
3. Obtain and validate each complete canonical BodyGraph. The canonical BodyGraph schema and calculation provenance remain single-homed in PF12/PF01/PF14 and are referenced, not copied, by `admin_bundle.response.v1`.  
4. Validate top-level/nested person identity coherence. Canonical `person_uid` is internal resolver output; it is never a caller requirement in this pre-user-model contract.  
5. Normalize the pair by ASCII byte order of canonical `person_uid`. If the IDs are equal, the canonical BodyGraph bytes must also be equal and the existing self-pair representation applies; equal IDs with unequal BodyGraphs are an internal invariant failure.  
6. The first normalized party is bundle A and the second is bundle B. Compute compatibility and all directional narratives only after this normalization.  
7. Invoke the pure builder with normalized BodyGraphs, normalized viewer preferences, the immutable validated narrative pack view, and stable release/rails context.

Consequences:

- Swapping raw request A/B produces the same normalized A/B, the same compat result, and the same bundle bytes.  
- `a_to_b` and `b_to_a` are defined relative to returned normalized A/B, not request position.  
- Shared narrative evaluation remains symmetric; directional prose is swap-covariant, not forced equal.  
- A source-neutral canonical BodyGraph is required. Raw vendor envelopes, provider request/response metadata, DB rows, placeholder/hash charts, seed-only charts, partial charts, and ad-hoc source labels cannot enter the bundle.

### **4.9.9 Closed `admin_bundle_v1` response schema**

The exact top-level keys are:

```json
{
  "a_bodygraph": {},
  "b_bodygraph": {},
  "compat": {
    "categories": [],
    "meta": {}
  },
  "meta": {},
  "narratives": [],
  "schema": "admin_bundle_v1",
  "viewer_prefs": {}
}
```

The braces/arrays above are structural notation. A real response contains no ellipses, placeholders, or extra keys.

#### 4.9.9.1 BodyGraphs

`a_bodygraph` and `b_bodygraph` each validate against the one active canonical, source-neutral BodyGraph schema, including its required person/`person_uid` coherence and calculation provenance. The admin-bundle schema uses a schema reference to that owner; it does not fork the field set.

The returned BodyGraphs must be complete enough to render the canonical nine-center BodyGraph and to support the existing mechanics: Personality calculation at the resolved birth instant/place and Design calculation by the exact 88-degree solar-arc rule in the owning Human Design mechanics, not a fixed “88 days” approximation. This paragraph is a conformance guard, not a second math implementation.

#### 4.9.9.2 `viewer_prefs`

This is the normalized, exact PF12 preference object supplied to computation. It is included once at bundle top level. No viewer ID is added.

#### 4.9.9.3 `compat`

`compat` has exactly `categories` and `meta`.

- `categories` contains exactly ten entries in the frozen Magic-10 semantic order.  
- Each entry has exactly:  
  - `id`: the category ID matching its position;  
  - `score`: JSON integer `0..100`, boolean invalid;  
  - `band`: exactly `Cool`, `Open`, `Warm`, or `Glow`;  
  - `personal_key`: nonempty governed compatibility selection key;  
  - `shared_key`: nonempty governed compatibility selection key.  
- `meta` has exactly `engine_tag` and `release_id`, and both equal the same fields in bundle `meta`.

This is the existing inner compat result, not a second math schema. The current `showcompat` outer participant shells are not nested again: canonical BodyGraphs live in `a_bodygraph`/`b_bodygraph`, and preferences live in `viewer_prefs`.

`personal_key` must not be interpreted as the retired stored narrative perspective `personal`. Narrative composition always receives an explicit `shared`, `a_to_b`, or `b_to_a` perspective. If existing ledgers cannot preserve this distinction, construction fails; it must not collapse the two private directions.

#### 4.9.9.4 `narratives`

`narratives` is an ordered list, not a set. It contains exactly three entries in this order:

1. `shared`  
2. `a_to_b`  
3. `b_to_a`

Each entry has exactly:

```json
{
  "band": "Warm",
  "category": "harmony",
  "perspective": "shared",
  "result": {}
}
```

- `category` equals `viewer_prefs.top_category`.  
- `band` equals the band of that category in `compat.categories`.  
- `perspective` equals the fixed slot’s perspective.  
- `result` is exactly one PF17/PF12 composer response:

Text:

```json
{
  "composition_id": "<8..128-char-id>",
  "fragment_ids": ["<id>"],
  "pack_sha": "<64-lowercase-hex>",
  "text": "<validated whole paragraph>"
}
```

or Suppressed:

```json
{
  "composition_id": "<8..128-char-id>",
  "pack_sha": "<64-lowercase-hex>",
  "policy_reason": "conflict",
  "suppressed": true
}
```

The union is closed and mutually exclusive. A valid suppressed result occupies its perspective slot and is a successful, truthful full-bundle outcome; it never fabricates fallback prose. `fragment_ids` retains composer slot/selection order and is not sorted as a set. Every result `pack_sha` equals bundle `meta.pack_sha`. Invalid narrative identity fails the whole bundle before this union and echoes no narrative provenance in the error.

Admin authorization permits the bundle to carry both private directions. It does not change PF17’s end-user privacy rule: non-admin consumers must never receive the other party’s private paragraph.

#### 4.9.9.5 `meta`

`meta` has exactly:

```json
{
  "build_commit": "<40-lowercase-hex>",
  "bundle_source": "admin_bundle_builder_v1",
  "emitter_sha256": "<64-lowercase-hex>",
  "engine_tag": "<stable-engine-tag>",
  "input_kind": "birth_match",
  "invocation_sha256": "<64-lowercase-hex>",
  "invocation_tag": "<stable-invocation-tag>",
  "pack_sha": "<64-lowercase-hex>",
  "rails": {
    "allow_network": true,
    "safe_mode": false
  },
  "release_id": "<64-lowercase-hex>"
}
```

`bundle_source` and `input_kind` are the shown constants. Runtime identity fields are release/process identity fixed for the active packaged engine; they cannot be request UUIDs or wall-clock values. `rails` has exactly the two booleans shown as fields; their values report the effective server rails for the computation.

The bundle contains no caller/client ID, credential ID, correlation ID, timestamp, request order, base URL, route, HTTP header, CLI version, output path, hostname, remote address, raw location, raw vendor payload, DB/provider source label, audit status, or per-request timing. Timezone/calculation provenance remains inside its owning canonical BodyGraph/provenance contract, not duplicated here.

### **4.9.10 Canonical bytes and the exact parity boundary**

All successful bundle and receipt JSON uses the existing canonical serializer/presenter:

- UTF-8, no BOM;  
- `ensure_ascii=false` semantics: non-ASCII values are emitted as UTF-8 rather than gratuitous `\u` escapes;  
- ASCII key order (all governed field names are ASCII);  
- compact separators and no insignificant whitespace;  
- exactly one final LF and no CR;  
- finite schema-authorized integers only; no floats, NaN, or Infinity in the admin wrapper/compat/meta/receipt;  
- schema-declared sets are deduplicated and sorted by their owning comparator;  
- schema-declared ordered arrays—including Magic-10 categories, narrative perspectives, and `fragment_ids`—retain their mandated order and are never set-sorted.

The parity subject is the LF-terminated `admin_bundle_v1` HTTP entity body. It excludes HTTP framing/headers, CLI file receipt, audit record, and filesystem metadata.

For a fixed normalized request and fixed engine configuration/release:

- direct HTTP body \= CLI stdout body \= CLI `--out` file bytes;  
- SHA-256 over each is equal;  
- two runs are byte-identical;  
- raw AB and BA request orderings are byte-identical after normalization.

The route serializes once. The CLI buffers up to `8,388,608` response bytes, requires status/body/header/schema/canonical conformance, verifies that parsing and canonical reserialization reproduce the received bytes, and then copies the original bytes. A body above the limit or any protocol/canonical mismatch is `ERR_ADMIN_BUNDLE_PROTOCOL`; the CLI never repairs it.

### **4.9.11 Output-file behavior and receipt**

#### 4.9.11.1 No `--out`

On `200`, stdout is the exact HTTP entity body and stderr is empty. No synopsis, correlation ID, headers, or receipt is appended.

#### 4.9.11.2 With `--out PATH`

The CLI validates the complete response before the first destination mutation. It then:

1. requires an existing directory parent;  
2. refuses symlink/device/directory destinations and refuses any destination identifying an input file;  
3. creates a mode `0600` temporary regular file in the destination directory;  
4. writes the exact received entity bytes;  
5. flushes and fsyncs the file;  
6. atomically installs it without clobber, or atomically replaces an existing regular file only when `--force` is present;  
7. fsyncs the containing directory where the platform supports it;  
8. removes its temporary file on failure and preserves the prior destination.

Only after all required writes succeed does stdout receive one canonical receipt:

```json
{
  "path": "/absolute/normalized/admin_bundle.json",
  "schema": "admin_bundle_receipt_v1",
  "sha256": "<sha256-of-exact-file-bytes>",
  "size_bytes": 12345
}
```

The receipt has exactly these four keys. `path` is the absolute normalized final destination. `size_bytes` includes the one final LF. There is no timestamp or correlation ID, so a repeated forced write of identical bytes to the same path produces the same receipt.

If the destination exists without `--force`, fail with `ERR_ADMIN_BUNDLE_OUTPUT_EXISTS`. Any other output failure is `ERR_ADMIN_BUNDLE_OUTPUT_WRITE`. Failure emits no receipt and leaves stdout empty. `--out` does not itself update an Evidence Index/Machine Mirror or confer governed-evidence status on a file.

### **4.9.12 Closed error and status contract**

Every body-bearing HTTP error is exactly the four-key `error_v1` object, canonically serialized with one LF:

```json
{"code":"<ERR_*>","error":"<exact message>","ok":false,"schema":"v1"}
```

No optional `details`, birth value, location, timezone, token clue, stack trace, vendor body, bundle fragment, composition/pack identity, or retry number appears in this route’s error body.

| HTTP | Code | Exact `error` message | Condition |
| ----: | :---- | :---- | :---- |
| 400 | `ERR_ADMIN_BUNDLE_INVALID_JSON` | `admin bundle request is not valid JSON` | Invalid UTF-8/BOM, empty/multiple JSON, duplicate keys, malformed JSON, trailing data, NaN/Infinity. |
| 401 | `ERR_ADMIN_AUTH_REQUIRED` | `admin authorization required` | Missing, duplicate, malformed, unknown, revoked, or invalid bearer credential. |
| 403 | `ERR_ADMIN_BUNDLE_FORBIDDEN` | `admin bundle scope required` | Valid credential lacks `admin:bundle:read`. |
| 404 | `ERR_NOT_FOUND` | `not found` | Unsupported path. |
| 405 | `ERR_NOT_FOUND` | `not found` | Unsupported method on exact path; include `Allow: POST`. |
| 406 | `ERR_ADMIN_BUNDLE_NOT_ACCEPTABLE` | `application/json response is required` | `Accept` excludes JSON. |
| 413 | `ERR_ADMIN_BUNDLE_REQUEST_TOO_LARGE` | `admin bundle request is too large` | Entity body exceeds 32,768 bytes. |
| 415 | `ERR_ADMIN_BUNDLE_INVALID_CONTENT_TYPE` | `content type must be application/json` | Missing/wrong media type, non-UTF-8 charset, or unsupported content encoding. |
| 422 | `ERR_ADMIN_BUNDLE_UNKNOWN_KEY` | `admin bundle request contains an unknown key` | Any unknown object property at any request depth. |
| 422 | `ERR_ADMIN_BUNDLE_INVALID_INPUT` | `admin bundle request validation failed` | Wrong schema discriminator/type/cardinality/format or invalid birth/location value not covered below. |
| 422 | `ERR_INVALID_VIEWER_PREFS` | `viewer preferences are invalid` | Incomplete/unknown Magic-10 set, bad top category, bool/non-integer/out-of-range weight. |
| 422 | `ERR_TIMEZONE_REQUIRED` | `birth timezone is required` | Existing PF05 exact condition. |
| 422 | `ERR_TIMEZONE_INVALID` | `birth timezone is invalid` | Existing PF05 exact condition. |
| 422 | `ERR_LOCATION_AMBIGUOUS` | `birth location is ambiguous` | Existing PF05 exact condition. |
| 422 | `ERR_TIMEZONE_UNRESOLVED` | `birth timezone could not be resolved` | Existing PF05 exact condition. |
| 422 | `ERR_TIMEZONE_CONFLICT` | `birth timezone sources conflict` | Existing PF05 exact condition. |
| 422 | `ERR_LOCAL_TIME_AMBIGUOUS` | `local birth time is ambiguous` | Existing PF05 exact condition. |
| 422 | `ERR_LOCAL_TIME_NONEXISTENT` | `local birth time does not exist` | Existing PF05 exact condition. |
| 422 | `ERR_LOCAL_TIME_INVALID` | `local birth date or time is invalid` | Existing PF05 exact condition. |
| 422 | `ERR_TIMEZONE_OVERRIDE_UNSUPPORTED` | `birth timezone override is unsupported` | Existing PF05 exact condition. |
| 429 | `ERR_ADMIN_BUNDLE_RATE_LIMITED` | `admin bundle request rate exceeded` | Governed admin-route limiter refuses the caller. `Retry-After`, when emitted, is a decimal-seconds header only. |
| 500 | `ERR_ADMIN_BUNDLE_INTERNAL` | `admin bundle generation failed` | Invariant, schema, identity, canonicalization, or other unclassified internal failure. |
| 503 | `ERR_MISSING_NARRATIVE_KEY` | `required narrative key is unavailable` | Required compat selection key is absent/unresolvable; distinct from a valid composer suppression. |
| 503 | `ERR_NARRATIVE_IDENTITY_INVALID` | `narrative identity is missing, malformed, or not bound to the active release` | PF17 pre-composition identity failure. |
| 503 | `ERR_ADMIN_BUNDLE_DEPENDENCY_UNAVAILABLE` | `admin bundle dependency is unavailable` | Resolver/provider/pack service unavailable, SAFE rails prevent required resolution, or provider semantics cannot be preserved. |
| 503 | `ERR_ADMIN_BUNDLE_AUDIT_UNAVAILABLE` | `admin bundle audit is unavailable` | A required success audit cannot be committed; no bundle is returned. |

The application route emits no other status. A reverse proxy’s synthetic response is not an alternate route contract; the CLI classifies an unrecognized/nonconforming response as local `ERR_ADMIN_BUNDLE_PROTOCOL`.

The route performs specific internal logging/classification but collapses ungoverned provider errors to `ERR_ADMIN_BUNDLE_DEPENDENCY_UNAVAILABLE`; it does not expose raw vendor status/body. A valid composer Suppressed result is `200`, never `503`.

#### 4.9.12.1 CLI-local mapping

All tabled HTTP errors produce their exact `code` token on CLI stderr and exit `2`. Local failures are:

| Token | Exact local condition |
| :---- | :---- |
| `ERR_ADMIN_BUNDLE_CONFIG_INVALID` | Invalid/missing `HDE_BASE_URL` or other non-auth client configuration. |
| `ERR_ADMIN_AUTH_REQUIRED` | Missing/malformed `HDE_ADMIN_TOKEN`; same token as HTTP auth refusal. |
| `ERR_ADMIN_BUNDLE_INPUT_FILE` | Input path is unreadable, non-regular, oversized, BOM-bearing, or otherwise cannot be loaded. |
| `ERR_ADMIN_BUNDLE_OUTPUT_EXISTS` | Destination exists and `--force` is absent. |
| `ERR_ADMIN_BUNDLE_OUTPUT_WRITE` | Safe/atomic destination write or durability step fails. |
| `ERR_ADMIN_BUNDLE_TRANSPORT` | DNS, connect, TLS, timeout, connection, or response-read failure before a conforming HTTP response is available. |
| `ERR_ADMIN_BUNDLE_PROTOCOL` | Redirect, unrecognized status, wrong/missing headers, compressed/oversized body, malformed error envelope, schema mismatch, or noncanonical success body. |

Locally parsed schema failures use the same route token they would have produced (`ERR_ADMIN_BUNDLE_INVALID_JSON`, `ERR_ADMIN_BUNDLE_UNKNOWN_KEY`, `ERR_ADMIN_BUNDLE_INVALID_INPUT`, `ERR_INVALID_VIEWER_PREFS`, or the size token). There is no raw exception text or provider detail on stderr.

Every newly selected token—including the already-selected but not-yet-registered timezone and narrative identity tokens—must enter PF04’s governed error-token registry before implementation emits it or QA claims conformance. Registration is a blocking dependency, not an unresolved PF05 design choice.

### **4.9.13 Audit contract**

The route’s exact audit identity is `internal.admin.bundle.v1`.

The server selects one canonical UUIDv4 correlation ID before authentication. Every successful response requires exactly one durable audit record committed before response bytes are released. The record has exactly:

```json
{
  "at": "2026-08-11T12:34:56.789Z",
  "caller": "ops-01",
  "client": "hdctl",
  "correlation_id": "00000000-0000-4000-8000-000000000000",
  "input_kind": "birth_match",
  "outcome": "success",
  "release_id": "<64-lowercase-hex>",
  "route": "internal.admin.bundle.v1"
}
```

- `at` is UTC RFC 3339 with exactly millisecond precision and `Z`.  
- `caller` is the authenticated key ID, which must be an opaque non-email account/service label.  
- `client` comes from the trusted token registry, not User-Agent or an untrusted request field.  
- `input_kind` is `birth_match` for a valid v1 request, otherwise `unknown` on a failure record.  
- `outcome` is one of `success`, `auth_required`, `forbidden`, `invalid_request`, `rate_limited`, `dependency_failure`, or `internal_failure`.

Auth failures and security-relevant refusals are also audited best-effort. For an unauthenticated request, `caller` and `client` are `unknown`; attacker-supplied key IDs are not copied into logs. A failure to write a failure-audit record must not recursively mask the original refusal. A failure to commit a success-audit record does mask the success and returns the selected `503` audit error.

Audit/log records MUST NOT contain raw birthdate/time, location, timezone, BodyGraph, `person_uid`, viewer weights, narrative text, composition/fragment IDs, request/response body, token, digest, Authorization/cookie/header values, raw key ID from a failed token, output path, vendor payload, or remote IP. Infrastructure access logs are a separate governed surface and do not change this schema.

Audit time, caller, client, correlation, and outcome are deliberately excluded from `admin_bundle_v1`; otherwise two-run identity would be impossible.

### **4.9.14 Human Design and narrative fidelity guards**

The transport contract introduces no new Human Design math. Conformance requires all of the following:

- Birth calculation uses the exact resolved local instant and place. No UTC/process-zone fallback, fuzzy timezone repair, default fold, DST-gap shift, or fixed-offset shortcut.  
- The canonical BodyGraph is complete and source-neutral. Provider response presence is not proof of chart correctness; schema, identity, provenance, and existing mechanics validation must pass.  
- Personality mechanics use the resolved birth instant. Design mechanics follow the owning exact solar-arc rule; “approximately three months” is explanatory language, not a fixed-day algorithm.  
- Compatibility contains every Magic-10 category exactly once in the frozen order. `harmony` cannot proxy for the other nine. Scores/bands/selection keys come only from the governed compatibility engine.  
- Narrative `families_fired`, category, band, and direction come from mechanics. The composer cannot infer a Gate, Channel, family, score, band, or relationship claim from prose.  
- All three admin perspective slots are explicit. Shared symmetry and directional swap covariance remain intact.  
- Valid suppression is preserved honestly. Missing/blocked content never triggers filler, generic advice, fate language, medical/diagnostic claims, or an LLM/model call.  
- Narrative pack and release identity must be valid before any prose or provenance is returned.

### **4.9.15 Industry-practice rationale**

The choices above apply current standards without replacing Glow canon:

- The Authorization header, TLS-only transport, certificate verification, no URL token, scoped credential, and uniform auth refusal follow [RFC 6750](https://www.rfc-editor.org/info/rfc6750/). The static registry is explicitly a bounded pre-Glow mechanism; the later app-admin identity model should replace it through a versioned migration rather than weaken it.  
- `Cache-Control: no-store` is selected instead of the draft’s `private, max-age=0, must-revalidate` because `private` still permits private-cache storage; [RFC 9111](https://www.rfc-editor.org/info/rfc9111/) defines `no-store` for both private and shared caches.  
- Deterministic property sorting and invariant bytes align with the rationale in [RFC 8785](https://www.rfc-editor.org/info/rfc8785/). Glow’s existing serializer remains authoritative; this decision does not silently adopt JCS number/string rules or remove Glow’s required final LF.  
- Strong authentication for an Internet-reachable management endpoint, generic external errors, sanitized security logging, and `no-store` align with the [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). A confidential GUI backend, request limits, no redirects, no browser token, no CORS/cookies, least privilege, and atomic output reduce avoidable exposure.

### **4.9.16 Alchemical and development-philosophy fidelity**

This decision keeps phases distinct:

- **Calcination:** removes the comforting but false alternatives—conceptual flags, local fallback, example route, optional auth carrier, and source-dependent meta.  
- **Separation:** selects one versioned command/route/schema and separates semantic bundle data from transport, audit, credentials, and clocks.  
- **Conjunction:** makes every client meet one authenticated HTTP adapter, one pure builder, and one emitter.  
- **Distillation:** reduces successful bytes to a closed, canonical, repeatable object and a hash-verifiable file receipt.  
- **Coagulation:** is not claimed here; it occurs only after implementation, governed schemas/tokens, tests, live evidence, and acceptance are real.

In PF13’s elemental terms: Fire is the falsifiable full-payload outcome; Water is the one calm builder/emitter surface; Air is the explicit versioned contract/configuration; Earth is fail-closed auth, audit, privacy, and recoverable atomic writes. Alchemical language guides the engineering mode; it does not become a payload field, scoring rule, or substitute for Human Design mechanics.

### **4.9.17 Required dependent changes before conformance**

This decision authorizes future implementation posture only. A conforming implementation requires coordinated changes in the owning homes:

1. **PF05:** replace the example/alternative/open wording in §§4.9.2–4.9.6 and §§5.10.2–5.10.6 with this contract; retain the global success/failure carriers.  
2. **PF04:** register every selected `ERR_*` token and exact semantics; retain the three existing admin-bundle acceptance tokens and audit/privacy rules.  
3. **PF07:** register `HDE_ADMIN_TOKEN`, and close `HDE_ADMIN_TOKENS`/`HDE_ADMIN_SCOPES` with the shapes, secret ownership, startup validation, and rotation/revocation behavior above.  
4. **PF12:** publish the five closed Draft 2020-12 schemas and bind the response to the active canonical BodyGraph and composer-response schemas without copying their ownership.  
5. **PF14:** split resolver orchestration from the pure builder; normalize the resolved pair once; use the existing compat/narrative mechanics and canonical presenter.  
6. **PF17/PF18:** ensure the three direction-aware composer results and valid suppression union are the referenced runtime schema; do not revive stored `personal` perspective.  
7. **PF19/PF09.7:** add executable proof for full payload, auth, audit hygiene, CLI/HTTP raw-body parity, AB/BA identity, two-run identity, file receipt/atomicity, and governed evidence binding.

The implementation must not be described as complete merely because documentation or schema files land.

### **4.9.18 Minimum acceptance matrix**

No admin-bundle acceptance token may be claimed until governed evidence proves at least:

- exact CLI help surface and every mutual-exclusion/usage case;  
- no base-URL or credential fallback and no secret-bearing CLI flag;  
- HTTPS verification, redirect refusal, timeout behavior, and single-attempt transport;  
- missing/invalid/revoked token `401`, insufficient scope `403`, and credential rotation/revocation;  
- strict JSON, duplicate-key, unknown-key, size, media-type, and viewer-preference negatives;  
- every timezone source/precedence/fold/gap/conflict refusal and provenance binding;  
- two complete canonical BodyGraphs with identity/provenance validation;  
- all ten compat entries in the frozen order with scores, bands, and keys;  
- exactly three ordered perspective slots, including Text and valid Suppressed cases;  
- narrative identity failure and no-fallback/no-fabrication behavior;  
- exact closed meta and exclusion of source/caller/time/correlation/PII;  
- HTTP raw body \= CLI stdout \= CLI output-file bytes;  
- AB/BA and two-run byte identity;  
- no compression/ETag/cache storage and exact success/error headers;  
- safe no-clobber, `--force`, mode `0600`, atomic failure, exact receipt hash/size/path;  
- success audit before response, security-failure audits, audit-outage refusal, and redaction scans;  
- at least synthetic end-to-end evidence and any authorized real-pair evidence under a restricted governed privacy posture; raw real-person birth/bundle data must not be placed in an unrestricted artifact or log.

The existing required tokens remain:

- `ADMIN_BUNDLE_FULL_PAYLOAD_OK`  
- `CLI_ADMIN_BUNDLE_PARITY_OK`  
- `ADMIN_AUTH_REQUIRED_OK`

They are necessary, not sufficient substitutes for their full registered predicates and supporting canonical/evidence gates.

### **4.9.19 Explicit non-claims and rejected alternatives**

This decision does not:

- create or modify GitHub code, schemas, docs, infrastructure, secrets, routes, or acceptance records;  
- claim the production service currently exposes the route;  
- claim current placeholder/hash compat or current vendor mapping is Human Design conformant;  
- add a public Reader/App surface, widen A7, or make numeric/narrative admin content public;  
- authorize direct browser possession of an HDE admin token;  
- authorize user-ID inputs, DB writes, automatic vendor fallback, or local CLI calculation;  
- put transport/audit identity into deterministic bundle bytes;  
- treat documentation, repository presence, a provider response, or a generated artifact as QA PASS.

Rejected v1 alternatives are: `/admin/bundle`; route aliases; local CLI composition; source-dependent `bundle_source=CLI|GUI`; token/base URL flags; cookies/query tokens; permissive/unknown JSON fields; default viewer preferences; UTC/process timezone defaults; response reserialization in the CLI; `private` cacheability; ETags/compression; timestamps/correlation IDs in the bundle; human success synopses; JSON CLI errors; partial or filler narratives; and silent fallback after any identity, timezone, provider, audit, or schema failure.

- Future user-ID inputs and any post-Glow alignment with the wider app identity/auth model remain reserved for a later Doc-Delta; neither is part of `admin_bundle_v1`.

## **4.10 hdctl dev:sampler Partially Implemented; dev/admin-only**

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
      
  * When `APP_ENV` is unset, empty, or outside `{dev,test,local}`, the handler MUST NOT call the sampler core. It exits 2, writes `ERR_WRITER_FORBIDDEN\n` to `stderr`, and leaves `stdout` empty. The corresponding HTTP harness maps the same canonical code through its governed HTTP error envelope and status.


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

All validation and error behavior follows the global CLI input and stream rules in §§3.2-3.4: on typed input failure, `stderr` contains exactly one LF-terminated canonical code token; on usage failure it contains one LF-terminated synopsis; `stdout` remains empty and the exit code is nonzero.

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
      
  * On typed validation failure, exit code is 2, `stderr` contains exactly one LF-terminated canonical code token (no JSON envelope), and `stdout` remains empty.

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

### **5.1.0 Production POST request and resolution (normative)**

`POST /api/reader?v=1` accepts one JSON object with exactly `a_id` and `b_id`. Each value must be an exact lowercase canonical hyphenated RFC 4122 UUID. Unknown keys and inline charts, Gates, weights, profiles, bands, configuration IDs, and viewer preferences are prohibited.

The application resolves each UUID read-only through `public.hde_body_graphs_current` with `user_id` equal to the canonical UUID and `vendor = 'hdapi'`, selecting the current `user_id`, `vendor`, `vendor_version`, `input_fingerprint`, and `payload`. Reader resolution performs no write, request-time vendor call, arbitrary-string UUID5 conversion, or silent fallback. A resolved Gate array must be present, nonempty, unique, canonical, and within `1..64` before Engine Core is called.

Eligibility is decided after both complete projections resolve and before Engine Core, narrative routing, or intrinsic cache access. The same canonical UUID with byte-identical normalized projections is a valid ineligible self-pair. The same canonical UUID with unequal complete normalized projections fails closed. For distinct parties, directional narrative order is `(gate_mask, canonical_person_id)`; ASCII canonical UUID order is used only to break an equal Gate-mask tie. Request order never controls narrative orientation.

### 5.1.1 CLI and admin compatibility surfaces (normative)

* The Reader v1 success envelope above is the **only** public compat payload exposed by the Reader API. It remains six‑key and numeric‑free.  
    
* The compat engine produces the pure `magic10_result.v1` and the symmetric complete `magic10_compat_result.v1` defined in §4.1.3. Neither is the Reader v1 envelope.

**hdctl showcompat (CLI admin harness).**

In v1, `hdctl showcompat`:

* resolves and normalizes the pair inputs under §4.1;  
* invokes the governed result path without using viewer preferences or person identity as intrinsic score inputs;  
* emits the complete `magic10_compat_result.v1` to stdout for an eligible pair as one LF-terminated canonical JSON document; and  
* emits no `a`/`b`/`viewer_prefs` wrapper or public Reader payload on ordinary stdout.

The complete result is an internal/admin surface only. When `--dump-reader <path>` is provided, `showcompat` also writes the six-key Reader v1 success envelope to `<path>` through the Reader presenter. Those bytes remain governed by §5.1.2 and §6.1 and are distinct from the complete internal result.

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
      
  * In v1:  
      
    * if `eligible == true`: emit exactly one item `{"id": "harmony", "band": …}`;  
        
    * if `eligible == false`: `categories` MUST be `[]`. Engine Core, the intrinsic cache, and the narrative router are not called; no `pair_key`, intrinsic result, or narrative key exists.


* Be byte-identical across Reader and CLI for the same underlying compat result and environment when CLI produces the envelope via `--dump-reader`.

Richer compat JSON (including numeric scores and narrative selection keys) is restricted to **admin/test artifacts** (for example, `hdctl showcompat` compat JSON on stdout, admin sidecars, and Aux preview inputs). These admin surfaces **must not** extend or change the Reader v1 public envelope; the six‑key envelope remains numeric‑free and field‑closed.

### 5.1.3 Emission algorithm (success case; titles‑only)

The Reader v1 success emission algorithm is:

1. **Build the five-key public preimage.** After eligibility and category projection, build an object with exactly `reader_version`, `eligible`, `categories`, `meta`, and `release_id`. It excludes `idempotence_hash` and `pair_key`; never copy `pair_key` into the public hash.  
     
2. **Canonicalize & hash.** Serialize the preimage with the single shared emitter and canonical JSON rules (§6.1) to obtain `preimage_bytes`. Compute `idempotence_hash = sha256(preimage_bytes)` as lowercase 64-hex.  
     
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

   

2. No other fields may appear in the public error\_v1 envelope.

3. **Magic10 Reader and internal failure contract (normative).**

   1. For Reader v1, the standard error envelope has exactly `schema`, `ok`, `code`, and `error`; `schema` is `v1`, `ok` is `false`, and `code` and `error` are the governed pair below. Public Reader invokes `engine.compat.errors.error_envelope()` without `details`. No stack, path, UUID, Gate list, configuration contents, database detail, or internal diagnostic detail appears.

| Condition | Canonical token | HTTP status | Public-envelope rule |
| ----- | ----- | ----- | ----- |
| Invalid JSON, unknown request key, missing `a_id` or `b_id`, or an identifier that is not an exact lowercase hyphenated UUID | `ERR_READER_INVALID_INPUT` | 422 | Standard error envelope; no details |
| The same canonical identity is supplied with unequal complete normalized chart projections on an internal or future resolver path | `ERR_READER_INVALID_CHART` | 422 | Standard error envelope; no success, score, cache access, or narrative routing |
| Person identifier cannot resolve to a complete BodyGraph | `ERR_M10_PERSON_UNRESOLVED` | 404 | Standard error envelope; do not reveal which identifier failed |
| Reader DB resolution is unavailable, ambiguous, or violates the current-view row contract | `ERR_M10_RESOLVER_UNAVAILABLE` | 503 | `Cache-Control: no-store`; no row or DB details |
| Reader resolves a stored BodyGraph whose Gate array is missing, empty, duplicate, malformed, noncanonical, or outside `1..64` | `ERR_M10_BODYGRAPH_INCOMPLETE` | 503 | `Cache-Control: no-store`; no partial score and no request-time vendor fallback |
| An internal or CLI complete-chart input has no Gate array or an empty Gate array | `ERR_M10_GATES_MISSING` | 422 | Standard internal error envelope; no partial score |
| An internal or CLI Gate value is duplicate, malformed, noncanonical, or outside `1..64` | `ERR_M10_GATES_INVALID` | 422 | Standard internal error envelope; no partial score |
| Legacy ID-only internal call reaches scoring without sanctioned chart resolution | `ERR_M10_LEGACY_INPUT_UNSUPPORTED` | 422 | Standard error envelope; no UID-hash fallback |
| Loaded mechanics config or source hash disagrees with the selected config | `ERR_M10_CONFIG_MISMATCH` | 503 | `Cache-Control: no-store`; no result body |
| Manifest membership, checksum, or release identity disagrees | `ERR_M10_MANIFEST_MISMATCH` | 503 | `Cache-Control: no-store`; no result body |
| Result schema identity or bytes disagree with the active release | `ERR_M10_RESULT_SCHEMA_MISMATCH` | 503 | `Cache-Control: no-store`; no result body |
| Cached result identity is stale and valid Gate inputs are unavailable for recomputation | `ERR_M10_STALE_RESULT` | 503 | `Cache-Control: no-store`; no legacy result |

   2. The exact governed `error` messages are:

| Token | Exact message |
| ----- | ----- |
| `ERR_READER_INVALID_INPUT` | `invalid Reader request` |
| `ERR_READER_INVALID_CHART` | `invalid Reader chart` |
| `ERR_M10_PERSON_UNRESOLVED` | `BodyGraph not found` |
| `ERR_M10_RESOLVER_UNAVAILABLE` | `BodyGraph resolver unavailable` |
| `ERR_M10_BODYGRAPH_INCOMPLETE` | `BodyGraph is incomplete` |
| `ERR_M10_GATES_MISSING` | `Gate data is required` |
| `ERR_M10_GATES_INVALID` | `Gate data is invalid` |
| `ERR_M10_LEGACY_INPUT_UNSUPPORTED` | `legacy scoring input is unsupported` |
| `ERR_M10_CONFIG_MISMATCH` | `Magic10 configuration mismatch` |
| `ERR_M10_MANIFEST_MISMATCH` | `Magic10 release manifest mismatch` |
| `ERR_M10_RESULT_SCHEMA_MISMATCH` | `Magic10 result schema mismatch` |
| `ERR_M10_STALE_RESULT` | `Magic10 cached result is stale` |

   3. The error branch of `schemas/reader.v1.schema.json` MUST enforce this exact closed topology and the governed token/message pairs. Every new token MUST be registered in `engine/compat/error_tokens.py` and regenerated into `errors/token_map/token_map.json` through `tools/errors/generate_error_artifacts.py`. `adapter/schemas/error_v1.schema.json` remains unchanged unless its parity check proves a mismatch.

   

   

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

   

2. **Headers (normative).**  
   `Content-Type: application/json; charset=utf-8` · `Cache-Control: no-store` · **no `ETag`** on error and writer responses. A7 conditional rules for success responses live in §5.3.  
     
3. **Streams.** CLI failures emit a single LF-terminated stderr code string token (no JSON envelope); stdout remains empty on failure. HTTP consumers receive error\_v1 in the response body. Public JSON bytes are canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
     
4. **Determinism & parity.** Given the same inputs/environment, HTTP error bodies are **byte-identical**; **AB vs BA** does not change the error. If the same error condition is surfaced on both CLI and HTTP, the CLI stderr code string token MUST equal the HTTP error\_v1 `code` value for that condition (token-level parity); envelopes are not required to be byte-identical across surfaces.  
     
5. **Refusal vs 429 (policy note).** **Refusal** (rails closed) is an **ops surface**, **not** an A7 proof surface. Transport invariants on refusal: `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, **no `ETag`**, **no `Vary`**, **no `Content-Encoding`**. **429** is an A7 transport outcome and **may** include `retry_after_ms`. Keys-only log allow-lists and error token semantics are owned in **HDE-Governance** (titles-only).

   ### **Validation (binary)**

6. **Schema gate:** Ensure JSON matches the error\_v1 schema (HDE-Schemas & Artifacts).  
     
7. **Fields gate:** Ensure no numeric fields appear, and only schema-allowed optional fields appear.  
     
8. **Token map:** For public surfaces, emitted `code` values are canonical `ERR_*` tokens; lowercase legacy aliases are not emitted. For dev-only compat probe behavior, allow only the explicitly documented legacy code cases.  
     
9. **Parity:** If the same failure is surfaced on the CLI (`hdctl`) and on a transport route, the CLI stderr code string token MUST equal the transport error\_v1 `code` value for that failure.  
     
10. **A7 checks:** All error bodies must be canonical JSON and must not violate A7 conditional/header policy (see §5.3).

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
* **Reader↔CLI parity.** For identical inputs and environment, harness responses are byte-identical to the Reader-v1 bytes written by `hdctl showcompat --dump-reader <path>` (six keys, one LF).  
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
  **Indexing discipline.** Governed evidence identities and paths, Human Index and sentinel behavior, Machine Mirror schema, parity, checksums, and path-proofs are single-homed in **HDE-Schemas & Artifacts** and must be updated coherently when that contract requires it.

**Routing (titles-only).** A7 transport rules: **HDE-Governance** §10 and this document §5.3 / Appendix A. Canonical JSON and capture normalization: **HDE-Schemas & Artifacts** §4. Token names live in **HDE-Governance** §2.0.

---

## **5.5 Compat v1 (dev-only) route & parity harness \[PartiallyImplemented; Required−Now\]**

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
  * The compatibility namespace is exactly `/api/compat/v1` and its descendants and MUST NOT match unrelated prefixes such as `/api/compat/v10`. Resolve production posture by trimming and case-folding a nonempty `APP_ENV` first and otherwise `ENGINE_ENV`; `prod`, `production`, and `live` resolve to production-like posture. In any resolved production-like posture, every method on the exact namespace or any descendant MUST fail closed with status `404`, presenter-backed `error_v1` `code=ERR_NOT_FOUND`, and `Cache-Control: no-store`; `HEAD` carries no body. This guard applies before compatibility computation so the internal surface remains hidden.  
* **Success body (dev/internal; authenticated).** After the production-excluding environment gate and internal authentication, `POST /api/compat/v1` returns the canonical `magic10_compat_result.v1` defined in §4.1.3 for an eligible pair. It does not return or wrap Reader v1 bytes. Full signals, scores, and narrative keys remain internal/admin-only. A valid self-pair has no complete result, and this route must not fabricate a matrix.

**Error body.** Typed, numeric-free **error\_v1** envelope as defined in §5.2: `{"schema":"v1","ok":false,"code":"<ERR_*>", "error":"<message>", ...}`. For this route, the canonical codes include:

* `ERR_COMPAT_INVALID_JSON` for malformed or mixed `a`/`b` payloads (for example mixing `*_id` and full person payload for the same party),  
    
* `ERR_INVALID_VIEWER_PREFS` for missing/non-integer or incomplete viewer preference weights,  
    
* `ERR_MISSING_NARRATIVE_KEY` when a required narrative key is absent or unresolvable for a compat category.

Legacy lowercase strings such as `"invalid_json"`, `"invalid_prefs"`, and `"missing_narrative_key"` remain accepted **aliases** internally, but are resolved via the error token map into their canonical `ERR_*` equivalents before error\_v1 is emitted. The public `code` field on this route **MUST** carry the canonical `ERR_*` tokens, not the aliases.

### **Headers & conditionals (normative)**

* **Success (200).** `Content-Type: application/json; charset=utf-8`; `Cache-Control: no-store`; no `ETag`. POST is non-conditional and never returns `304`.  
* **Errors.** Except for the explicit bodyless non-production `HEAD` response above, all error responses use `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, and no `ETag`. Compatibility `404` and `405` responses use the shared presenter/emitter to emit canonical error\_v1 with `code=ERR_NOT_FOUND` while preserving the routing status; HTTP `HEAD` semantics suppress the production `404` body. The selected factory converts compatibility-scoped HTML `404` and `405` responses to this envelope and preserves Flask’s `Allow` header on a converted `405`.  
* **Method and subpath handling.** In non-production posture, `HEAD /api/compat/v1` returns `405` with no body, `Content-Length: 0`, no `Content-Type`, `Cache-Control: no-store`, and `Allow: POST, OPTIONS`; `OPTIONS /api/compat/v1` returns `204` with no body, `Content-Length: 0`, no `Content-Type`, `Cache-Control: no-store`, and `Allow: POST, OPTIONS`. Other unsupported methods at the exact namespace return presenter-backed `405` error\_v1, and unsupported descendant paths return presenter-backed `404` error\_v1. Compat GET does not use the optional A7 HEAD/304 flow.

### **Serialization & determinism (dev)**

* **Single emitter.** Responses **MUST** be emitted by the same presenter/emitter the CLI uses (§6.2).  
* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; arrays-as-sets deduped & ASCII-sorted (§6.1).  
* **Determinism.** For a fixed request, **two runs** produce byte-identical LF-terminated bytes; **AB↔BA parity** holds when swapping `a/b`. Tests run under `LC_ALL=C`.

### **Parity (clarified)**

* **Public parity lives in §5.4** (`/reader?v=1` ↔ Reader-v1 bytes written by `hdctl showcompat --dump-reader <path>`). Ordinary `showcompat` stdout is the distinct compat envelope.  
* **Compat v1 parity (normative).** For the same eligible normalized inputs, active configuration, and release, `hdctl showcompat` stdout and authenticated `POST /api/compat/v1` MUST emit byte-identical canonical `magic10_compat_result.v1` bytes. Both surfaces consume the same complete result and neither may calculate, weight, round, band, augment, or rescore independently.

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

**Purpose and ownership.** PF05 owns the transport facts and A7 behavior for its routes. The authoritative Endpoint Catalog schema, per-method record model, record fields, canonical path, checksum, path-proof, population policy, and validation are single-homed in **HDE-Schemas & Artifacts**. PF05 MUST NOT redefine that schema or maintain a second endpoint inventory.

**PF05 transport facts to project through the owned Catalog schema.**

| Route | Methods defined by PF05/runtime | Transport posture | A7 |
| :---- | :---- | :---- | :---- |
| `/reader` | `GET`, `HEAD` | internal dev-harness; explicit `APP_ENV=dev`; production public enablement is a separate change | eligible |
| `/api/reader` | `POST` | production application Reader v1; closed two-UUID request; read-only current-`hdapi` BodyGraph resolution | not eligible |
| `/api/compat/v1` | `GET`, `POST`, `HEAD`, `OPTIONS` | internal admin; production-excluding environment gate; writer `no-store`, no `ETag` | not eligible |
| `/aux/narrative` | `GET` | canonical public narrative surface; `classification:"public_aux"`; `internal:false`; `env_gate:"not_applicable_public"` | not eligible |
| `/api/aux/narrative` | `GET` | conditional `/api` alias of `/aux/narrative`, represented by the canonical record's `aliases` array | not eligible |
| `/internal/admin/bundle/v1` | `POST` | internal admin; authenticated and scope-gated; writer `no-store`, no `ETag`; no aliases | not eligible |
| `/internal/dev/sampler` | `POST` | internal dev-harness; `APP_ENV ∈ {dev,test,local}`; writer `no-store`, no `ETag` | not eligible |
| `/dev/sampler/conjunction` | `GET` | internal dev-harness; `APP_ENV ∈ {dev,test,local}` | not eligible |
| `/dev/reader/conjunction` | `GET` | internal dev-harness; `APP_ENV ∈ {dev,test,local}` | not eligible |
| `/dev/writer/conjunction` | `GET` | internal dev-harness/writer; route identity `dev.writer.conjunction.v1`; explicit caller-provided rails | not eligible |
| `/internal/version` | `GET`, `HEAD` | internal ops identity; may remain cataloged | excluded from `success_endpoints` and A7 selection |

PF12 represents the configured Aux spellings as one canonical per-method record:

```json
{
  "a7_eligible": false,
  "aliases": ["/api/aux/narrative"],
  "blueprint_module": "adapter.http_reader",
  "classification": "public_aux",
  "env_gate": "not_applicable_public",
  "internal": false,
  "method": "GET",
  "path": "/aux/narrative",
  "rails_profile": "public-read-only; vendor-network-disabled"
}
```

`path` is the canonical route; `aliases` contains reachable spellings of the same contract, not independent surfaces. Query selectors are not stored in either field. PF12 MUST register `public_aux`, the optional `aliases` mechanism and its validation, the public `env_gate` sentinel, and this record before Catalog conformance may be claimed. If a future configured mount does not expose `/api/aux/narrative`, the authoritative record MUST omit that alias.

Only routes designated A7-eligible through the authoritative Catalog are selected for §5.3 success proofs. Catalog membership never by itself proves reachability, implementation, PASS, production exposure, or acceptance. Token semantics remain in **HDE-Governance**; catalog artifacts and companions remain in **HDE-Schemas & Artifacts**.

**PF05-owned proof constraints.** Compat proof compares canonical emitted bytes; parsed-object equality is insufficient. Current AB/BA emitted bytes MUST bind to the claimed identity hash; stale or regex-only evidence is insufficient. Compat threshold/category proof remains internal/admin and MUST NOT widen public Reader routes, payloads, or numerics. Transport-validator behavior remains governed by §5.3 and Appendix A.

**Implementation and acceptance state (informative).** At pinned authoring inspection `main@aa58e93ddedb9738af33de20e42c39a38b7c1e08`, `docs/ENDPOINTS_CATALOG.json` used PF12's current per-method model but did not yet contain the Aux or admin-bundle records, `public_aux`, or `aliases`. This Required-Now projection is a dependent contract requirement, not a claim that the checked-in Catalog, deployment, QA, OPS, or acceptance state already conforms.

---

## **5.7 Aux Narrative (public bytes)**

**Route (canonical \+ conditional alias; byte identity required).**

* Canonical: `GET /aux/narrative?v=1`.  
* Conditional `/api` alias when configured: `GET /api/aux/narrative?v=1`.  
* **Alias parity (merge-blocking):** canonical and alias MUST produce byte-identical status, governed headers, and body for the same query tuple. **Acceptance:** `AUX_CANON_ALIAS_PARITY_OK`. Policy and token semantics live in HDE-Governance.  
* PF12 represents the configured pair as the one canonical `GET` record in §5.6, with `classification:"public_aux"` and `aliases:["/api/aux/narrative"]`. Aux is not an A7 JSON-success surface.

---

**Query parameters (closed public grammar).**

The public Aux routes accept exactly these case-sensitive query names:

* `v` — required exactly once; after ordinary URL decoding its value MUST be exactly the one-character ASCII string `1`.  
* `category` — Magic-10 id (closed set).  
* `band` — one of `{Cool, Open, Warm, Glow}`.  
* `perspective` — one of `{shared, a_to_b, b_to_a}`.

`v` is not trimmed, numerically parsed, case-folded, defaulted, or normalized. Missing `v`, empty `v=`, unsupported values such as `v=01`, `v=1%20`, or `v=2`, and every duplicate occurrence return the version refusal below, even when every duplicate value is `1`.

`slot`, `viewer_top`, `flags`, `flag`, `families_fired`, `release_id`, `pack_sha`, case variants, and every other query name are not public. Any occurrence, including an empty occurrence, is refused before composition. `flags` is not split or normalized, `flag` is not an alias, and public-route authorization does not unlock hidden query semantics. A QA or admin override requires a separately governed non-public carrier.

The server obtains `families_fired`, `release_id`, `pack_sha`, and the validated pack view from governed internal mechanics and identity state. These values are not caller preferences.

**Deterministic query-validation precedence.**

1. Preserve ordinary path and method routing.  
2. Reject any query name outside the exact four-name allow-list.  
3. Validate `v` cardinality.  
4. Validate the sole decoded `v` value.  
5. Apply the existing `category`, `band`, and `perspective` contract.  
6. Obtain the governed internal mechanics, release, and pack state before composition.

An unsupported query name wins over an invalid `v`. Several unsupported names still produce the same generic refusal.

**Typed query refusals.**

| Condition | Status | Code | Exact message |
| :---- | ----: | :---- | :---- |
| Any unsupported or unknown query-name occurrence | `400` | `ERR_AUX_UNSUPPORTED_QUERY_PARAMETER` | `unsupported Aux query parameter` |
| Missing, empty, unsupported, or duplicate `v` | `400` | `ERR_AUX_INVALID_VERSION` | `invalid or unsupported Aux version selector` |

The exact unsupported-name body is:

```json
{"code":"ERR_AUX_UNSUPPORTED_QUERY_PARAMETER","error":"unsupported Aux query parameter","ok":false,"schema":"v1"}
```

The exact version body is:

```json
{"code":"ERR_AUX_INVALID_VERSION","error":"invalid or unsupported Aux version selector","ok":false,"schema":"v1"}
```

Each body is canonical JSON with exactly one final LF. Both refusals use `Content-Type: application/json; charset=utf-8` and `Cache-Control: no-store`; omit `ETag`, `Vary`, and `Content-Encoding`; and MUST NOT echo a parameter name or value, the request query, identity state, narrative input, or PII. Canonical and alias routes return byte-identical refusal status, governed headers, and body. The version gate runs before identity preflight, narrative routing, suppression, or prose composition.

`ERR_AUX_UNSUPPORTED_QUERY_PARAMETER` and `ERR_AUX_INVALID_VERSION` MUST enter the governed error token map and `error_v1` schema surface before implementation emits either token or conformance is claimed.

**Implementation and acceptance state (informative).** At pinned authoring inspection `main@aa58e93ddedb9738af33de20e42c39a38b7c1e08`, `adapter/http_reader.py` registered both route spellings but did not enforce `v`, read the six rejected parameters, and forwarded them or used them as overrides. The checked-in error-token map contained neither selected Aux token. These are repository contradictions to the Required-Now contract, not permission to widen the public grammar and not evidence of runtime, deployment, QA, or acceptance state.

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

* ## Aux **HEAD/304 are out of scope** for EPIC-010. (Policy: HDE-Governance.)

**Snapshot normalization (routing).**

* Stored header snapshots use **lower-case header names**; values verbatim.

* ## Normalization is governed in HDE-Schemas & Artifacts; **acceptance:** `SNAPSHOT_HEADER_LOWERCASE_OK`.

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

**Implementation and acceptance state:** Repository inspection at `main@aa58e93ddedb9738af33de20e42c39a38b7c1e08` did not find this Required-Now HTTP route in the inspected adapter/factory or an exact route search. Until IG-022 lands or governance recanonizes its status, §5.9 cannot support an implementation or acceptance claim.

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

**Architecture and route.**

* Method: `POST`.  
* Canonical path: `/internal/admin/bundle/v1`.  
* Audit route identity: `internal.admin.bundle.v1`.  
* Aliases: none.  
* Success status: `200`.

`hdctl admin-bundle` is a thin authenticated HTTP client for this one route. The HTTP adapter authenticates and validates, resolves both raw birth inputs to canonical BodyGraphs, and invokes one pure `admin_bundle_v1` builder with normalized values and stable release context. Resolver, vendor, database, environment, logging, and audit I/O remain outside the builder. The existing canonical presenter/emitter serializes the result once; the route returns those bytes, and the CLI validates and copies the entity body without reconstructing it. There is no local CLI fallback, alternate emitter, source-dependent builder, or substitute calculation after a remote failure.

**Request body.** The route accepts exactly the closed `admin_bundle_request_v1` object:

```json
{
  "a": {
    "birthdate": "1990-01-02",
    "birthtime": "03:04",
    "location": "Rabat, Morocco",
    "timezone": "Africa/Casablanca",
    "timezone_override": "Africa/Casablanca"
  },
  "b": {
    "birthdate": "1991-05-06",
    "birthtime": "07:08",
    "location": "Lisbon, Portugal"
  },
  "schema": "admin_bundle_request_v1",
  "viewer_prefs": {
    "top_category": "harmony",
    "weights": {
      "alignment": 50,
      "balance": 50,
      "comfort": 50,
      "communication": 50,
      "consistency": 50,
      "creativity": 50,
      "drive": 50,
      "expansion": 50,
      "harmony": 50,
      "heat": 50
    }
  }
}
```

Top-level required keys are exactly `a`, `b`, `schema`, and `viewer_prefs`. Each party requires exactly `birthdate`, `birthtime`, and `location`, and may include `timezone` and/or `timezone_override`. No user ID, `person_uid`, precomputed chart, provider selector, source label, correlation value, or authentication value is a body field. `viewer_prefs` is the exact normalized PF12 object: one Magic-10 `top_category` and every and only the ten integer weights `0..100`; booleans are invalid and zero is preserved.

`birthdate` is a real proleptic-Gregorian date in exact `YYYY-MM-DD`; `birthtime` is exact `HH:MM` in `00:00..23:59`; `location` is NFC-normalized UTF-8, outer-trimmed, control-free, and `1..256` UTF-8 bytes while preserving meaningful case, diacritics, and punctuation. Timezone values are exact IANA identifiers or aliases present in the pinned timezone-data alias map. No case folding, abbreviation, fixed-offset substitute, guessed alias, fuzzy location correction, silent rounding, or UTC/process-zone fallback is permitted.

The request entity limit is `32,768` bytes. The parser accepts semantically valid JSON with arbitrary insignificant whitespace and key order, detects duplicate keys, normalizes once, validates the closed schema, and passes only normalized typed data onward. UTF-8 BOM, invalid UTF-8, empty body, duplicate key, trailing non-whitespace data, NaN/Infinity, or multiple JSON values is invalid JSON; unknown properties are not removed.

Request media type is `application/json` with no charset or `charset=utf-8`. `Content-Encoding` is absent or `identity`. If `Accept` is present it permits `application/json`; absent and `*/*` are accepted.

Failure precedence is fixed:

1. path and method routing;  
2. request framing, size, content encoding, media type, and acceptability;  
3. authentication and authorization;  
4. JSON parsing and closed-schema validation;  
5. timezone/domain resolution, dependencies, bundle construction, and required success-audit commit.

Authentication precedes JSON parsing or mechanics work. The size/framing gate may terminate an oversized request without reading or authenticating its full body.

The adapter resolves each party under PF05's selected timezone algorithm, validates each complete source-neutral canonical BodyGraph and identity/provenance coherence, then normalizes the pair by ASCII byte order of canonical `person_uid`. Equal IDs require equal canonical BodyGraph bytes. Returned A/B and `a_to_b`/`b_to_a` are relative to that normalized order. Raw AB and BA requests therefore produce identical bundle bytes; shared narrative evaluation remains symmetric and directional prose remains swap-covariant.

### **5.10.3 Response body and headers (normative)**

**Success body.** The exact top-level keys are:

```json
{
  "a_bodygraph": {},
  "b_bodygraph": {},
  "compat": {
    "categories": [],
    "meta": {}
  },
  "meta": {},
  "narratives": [],
  "schema": "admin_bundle_v1",
  "viewer_prefs": {}
}
```

The braces and arrays are structural notation; a response contains no placeholders or extra keys.

* `a_bodygraph` and `b_bodygraph` validate against the one active canonical, source-neutral BodyGraph schema, including person/`person_uid` coherence and calculation provenance. They are complete enough for the canonical nine-center BodyGraph and the owning Personality and exact 88-degree Design mechanics.  
* `viewer_prefs` is the normalized exact PF12 preference object supplied to computation and is included once. No viewer ID is added.  
* `compat` has exactly `categories` and `meta`. `categories` has exactly ten entries in frozen semantic order `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. Each entry has exactly `id`, integer `score` in `0..100`, `band` in `{Cool,Open,Warm,Glow}`, nonempty `personal_key`, and nonempty `shared_key`. `compat.meta` has exactly `engine_tag` and `release_id`, equal to the same bundle-meta fields. `personal_key` is a compatibility selection key, not the retired stored narrative perspective `personal`.  
* `narratives` is an ordered list of exactly three entries: `shared`, `a_to_b`, then `b_to_a`. Each entry has exactly `band`, `category`, `perspective`, and `result`. `category` equals `viewer_prefs.top_category`; `band` equals that category's compat band; and `perspective` equals the fixed slot.

Each `result` is exactly one closed PF17/PF12 composer response. Text is:

```json
{
  "composition_id": "<8..128-char-id>",
  "fragment_ids": ["<id>"],
  "pack_sha": "<64-lowercase-hex>",
  "text": "<validated whole paragraph>"
}
```

Suppressed is:

```json
{
  "composition_id": "<8..128-char-id>",
  "pack_sha": "<64-lowercase-hex>",
  "policy_reason": "conflict",
  "suppressed": true
}
```

The union is closed and mutually exclusive. A valid suppression occupies its slot and remains a successful full bundle; it never fabricates fallback prose. `fragment_ids` preserves composer slot/selection order and is not set-sorted. Every result `pack_sha` equals bundle `meta.pack_sha`. Invalid narrative identity fails the whole bundle without provenance echo. Admin authorization permits both private directions but does not weaken PF17's end-user privacy boundary.

`meta` has exactly:

```json
{
  "build_commit": "<40-lowercase-hex>",
  "bundle_source": "admin_bundle_builder_v1",
  "emitter_sha256": "<64-lowercase-hex>",
  "engine_tag": "<stable-engine-tag>",
  "input_kind": "birth_match",
  "invocation_sha256": "<64-lowercase-hex>",
  "invocation_tag": "<stable-invocation-tag>",
  "pack_sha": "<64-lowercase-hex>",
  "rails": {
    "allow_network": true,
    "safe_mode": false
  },
  "release_id": "<64-lowercase-hex>"
}
```

`bundle_source` and `input_kind` are the shown constants. Runtime identity fields are stable active-release/process identity, not request UUIDs or wall-clock values. `rails` reports the effective computation rails through exactly its two booleans. The bundle excludes caller/client or credential identity, correlation ID, timestamp, request order, base URL, route, HTTP headers, CLI version, output path, hostname, remote address, raw location, raw vendor payload, DB/provider source label, audit status, and per-request timing.

Successful bytes use the one canonical serializer: UTF-8 without BOM or CR; non-ASCII values emitted as UTF-8; ASCII-sorted object keys; compact separators; exactly one final LF; finite schema-authorized integers only; schema-declared sets deduplicated and sorted by their owner; and ordered arrays kept in their mandated semantic order.

**Headers.** Every body-bearing success or error response uses:

```
Content-Type: application/json; charset=utf-8
Cache-Control: no-store
X-Content-Type-Options: nosniff
X-Correlation-ID: <server-selected-canonical-uuidv4>
Content-Length: <exact LF-terminated entity-body length>
```

The response omits `ETag`, `Vary`, `Content-Encoding`, and CORS allow headers and emits identity bytes even when compression is offered. A valid canonical inbound correlation ID may be retained; an absent, duplicate, or invalid value is replaced without logging its value. Correlation is transport/audit data and never enters the bundle.

Only `POST` is allowed. Other methods return `405`, `Allow: POST`, and `ERR_NOT_FOUND`. `HEAD` returns the same `405` with no body, `Content-Length: 0`, no `Content-Type`, `Cache-Control: no-store`, no `ETag`, and `Allow: POST`. Unsupported paths return `404` and `ERR_NOT_FOUND` through the shared presenter.

**Closed error contract.** Every body-bearing error is exactly the four-key canonical `error_v1` object with one LF and no optional details or sensitive echo.

| HTTP | Code | Exact `error` message | Condition |
| ----: | :---- | :---- | :---- |
| `400` | `ERR_ADMIN_BUNDLE_INVALID_JSON` | `admin bundle request is not valid JSON` | Invalid UTF-8/BOM, empty or multiple JSON, duplicate keys, malformed JSON, trailing data, or NaN/Infinity. |
| `401` | `ERR_ADMIN_AUTH_REQUIRED` | `admin authorization required` | Missing, duplicate, malformed, unknown, revoked, or invalid bearer credential. |
| `403` | `ERR_ADMIN_BUNDLE_FORBIDDEN` | `admin bundle scope required` | Valid credential lacks `admin:bundle:read`. |
| `404` | `ERR_NOT_FOUND` | `not found` | Unsupported path. |
| `405` | `ERR_NOT_FOUND` | `not found` | Unsupported method on the exact path; include `Allow: POST`. |
| `406` | `ERR_ADMIN_BUNDLE_NOT_ACCEPTABLE` | `application/json response is required` | `Accept` excludes JSON. |
| `413` | `ERR_ADMIN_BUNDLE_REQUEST_TOO_LARGE` | `admin bundle request is too large` | Entity body exceeds 32,768 bytes. |
| `415` | `ERR_ADMIN_BUNDLE_INVALID_CONTENT_TYPE` | `content type must be application/json` | Missing or wrong media type, non-UTF-8 charset, or unsupported content encoding. |
| `422` | `ERR_ADMIN_BUNDLE_UNKNOWN_KEY` | `admin bundle request contains an unknown key` | Unknown object property at any request depth. |
| `422` | `ERR_ADMIN_BUNDLE_INVALID_INPUT` | `admin bundle request validation failed` | Wrong discriminator, type, cardinality, format, or uncovered birth/location value. |
| `422` | `ERR_INVALID_VIEWER_PREFS` | `viewer preferences are invalid` | Incomplete/unknown Magic-10 set, bad top category, or boolean/non-integer/out-of-range weight. |
| `422` | `ERR_TIMEZONE_REQUIRED` | `birth timezone is required` | Existing PF05 exact condition. |
| `422` | `ERR_TIMEZONE_INVALID` | `birth timezone is invalid` | Existing PF05 exact condition. |
| `422` | `ERR_LOCATION_AMBIGUOUS` | `birth location is ambiguous` | Existing PF05 exact condition. |
| `422` | `ERR_TIMEZONE_UNRESOLVED` | `birth timezone could not be resolved` | Existing PF05 exact condition. |
| `422` | `ERR_TIMEZONE_CONFLICT` | `birth timezone sources conflict` | Existing PF05 exact condition. |
| `422` | `ERR_LOCAL_TIME_AMBIGUOUS` | `local birth time is ambiguous` | Existing PF05 exact condition. |
| `422` | `ERR_LOCAL_TIME_NONEXISTENT` | `local birth time does not exist` | Existing PF05 exact condition. |
| `422` | `ERR_LOCAL_TIME_INVALID` | `local birth date or time is invalid` | Existing PF05 exact condition. |
| `422` | `ERR_TIMEZONE_OVERRIDE_UNSUPPORTED` | `birth timezone override is unsupported` | Existing PF05 exact condition. |
| `429` | `ERR_ADMIN_BUNDLE_RATE_LIMITED` | `admin bundle request rate exceeded` | Governed admin-route limiter refuses the caller. |
| `500` | `ERR_ADMIN_BUNDLE_INTERNAL` | `admin bundle generation failed` | Invariant, schema, identity, canonicalization, or other unclassified internal failure. |
| `503` | `ERR_MISSING_NARRATIVE_KEY` | `required narrative key is unavailable` | Required compat selection key is absent or unresolvable. |
| `503` | `ERR_NARRATIVE_IDENTITY_INVALID` | `narrative identity is missing, malformed, or not bound to the active release` | PF17 pre-composition identity failure. |
| `503` | `ERR_ADMIN_BUNDLE_DEPENDENCY_UNAVAILABLE` | `admin bundle dependency is unavailable` | Resolver/provider/pack unavailable, SAFE rails prevent required resolution, or provider semantics cannot be preserved. |
| `503` | `ERR_ADMIN_BUNDLE_AUDIT_UNAVAILABLE` | `admin bundle audit is unavailable` | Required success audit cannot be committed; no bundle is returned. |

A valid composer Suppressed result is `200`, never `503`. `Retry-After`, when emitted for `429`, is a decimal-seconds header only. Provider details collapse to the governed dependency error and are never returned. The application route emits no other status; a nonconforming proxy response is a CLI-local `ERR_ADMIN_BUNDLE_PROTOCOL`.

### **5.10.4 Authentication, authorization, and admin-only gating (normative)**

`HDE_ADMIN_TOKEN` is the CLI's only credential source and has exact form `<key-id>.<secret>`, where `key-id` matches `[A-Za-z0-9][A-Za-z0-9_-]{0,31}` and `secret` is exactly 32 random bytes encoded as 43 unpadded base64url characters. It is not accepted as an option, URL/query value, cookie, body field, or config-file fallback. The client sends exactly `Authorization: Bearer <HDE_ADMIN_TOKEN>`; a missing or malformed client credential fails locally as `ERR_ADMIN_AUTH_REQUIRED` without a request.

The server uses strict `HDE_ADMIN_TOKENS` and `HDE_ADMIN_SCOPES` JSON registries with identical key-ID sets. Each token entry has exactly trusted `client` in `{hdctl,admin_gui,automation}` and `digest` as SHA-256 of the complete ASCII bearer token. Each scope entry is a sorted, duplicate-free registered-scope array. This route requires exact scope `admin:bundle:read`. Missing or invalid production registries fail readiness/startup; the route MUST NOT register open or degraded. Digest verification is constant-time, including a dummy path for unknown IDs. Each operator/service account and client class has a distinct key ID; raw tokens and Authorization values are never logged.

Missing, malformed, unknown, revoked, or wrong-secret credentials all return the same `401` error and `WWW-Authenticate: Bearer realm="hde-admin"`. A valid credential without the route scope returns `403` and `WWW-Authenticate: Bearer realm="hde-admin", error="insufficient_scope", scope="admin:bundle:read"`. The Admin GUI calls from a confidential backend. Browser bundles never receive or retain the token; the HDE route accepts no cookie authentication and emits no CORS allow headers.

### **5.10.5 Logging and audit (normative)**

The server selects one canonical UUIDv4 correlation ID before authentication. Every successful response requires one durable audit record committed before response bytes are released. The record has exactly:

```json
{
  "at": "2026-08-11T12:34:56.789Z",
  "caller": "ops-01",
  "client": "hdctl",
  "correlation_id": "00000000-0000-4000-8000-000000000000",
  "input_kind": "birth_match",
  "outcome": "success",
  "release_id": "<64-lowercase-hex>",
  "route": "internal.admin.bundle.v1"
}
```

`at` is UTC RFC 3339 with exactly millisecond precision and `Z`; `caller` is the authenticated opaque key ID; `client` comes from the trusted registry; `input_kind` is `birth_match` for a valid v1 request and `unknown` for a failure record; `outcome` is exactly one of `success`, `auth_required`, `forbidden`, `invalid_request`, `rate_limited`, `dependency_failure`, or `internal_failure`.

Authentication failures and security-relevant refusals are audited best-effort. Unauthenticated failures use `caller:"unknown"` and `client:"unknown"` without copying attacker-supplied key IDs. Failure-audit outage does not mask the original refusal. Success-audit commit failure masks success and returns `ERR_ADMIN_BUNDLE_AUDIT_UNAVAILABLE`.

Audit and operation logs contain no raw birthdate/time, location, timezone, BodyGraph, `person_uid`, viewer weights, narrative text, composition/fragment IDs, request/response body, token or digest, Authorization/cookie/header values, raw failed key ID, output path, vendor payload, or remote IP. Audit time, caller, client, correlation, and outcome stay outside `admin_bundle_v1` so deterministic bytes remain possible.

### **5.10.6 Parity with CLI admin bundle (normative)**

The parity subject is the LF-terminated `admin_bundle_v1` HTTP entity body; it excludes HTTP framing and headers, CLI receipt, audit record, and filesystem metadata. For one normalized request and fixed engine configuration/release:

* direct HTTP body \= CLI stdout body \= CLI `--out` file bytes;  
* SHA-256 over each is equal;  
* two runs are byte-identical; and  
* raw AB and BA request orderings are byte-identical after normalization.

The route serializes once. The CLI accepts at most `8,388,608` response bytes, requires conforming status, headers, schema, and canonical bytes, proves canonical reserialization reproduces the received body, and then copies the original bytes. It never repairs or reserializes a successful response. Oversize or protocol/canonical mismatch is `ERR_ADMIN_BUNDLE_PROTOCOL`.

The exact response/request/audit schemas and every newly selected error token are dependent registrations in PF12 and PF04; auth registry variables and startup semantics are dependent PF07 work; resolver/builder separation is dependent PF14 work; and direction-aware composer results remain PF17/PF12-owned. The existing acceptance tokens `ADMIN_BUNDLE_FULL_PAYLOAD_OK`, `CLI_ADMIN_BUNDLE_PARITY_OK`, and `ADMIN_AUTH_REQUIRED_OK` remain necessary but cannot be claimed until their complete governed evidence predicates pass.

**Implementation and acceptance state (informative).** Pinned inspection at `main@aa58e93ddedb9738af33de20e42c39a38b7c1e08` found no `admin-bundle` parser in `engine/cli/main.py` and no `/internal/admin/bundle/v1` route in the inspected HTTP adapter/factory or exact repository searches. This Required-Now contract is a plan/requirement, not a claim of implementation, schema publication, QA, OPS, deployment, or acceptance.

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
    
* **Cataloged; not A7.** The route is represented in the authoritative internal Endpoint Catalog and excluded from `success_endpoints`, A7 proof selection, and public contracts, as specified in §5.11.6.  
    
* **Writer-style errors.** The route uses the standard typed error envelope and headers from §5.2/§8; gating failures and validation errors are treated as writer-style/ops outcomes (`Cache-Control: no-store`, no `ETag`), not as public Reader errors.

  ### **5.11.2 Route, method, and APP\_ENV gate (normative)**

Route and method:

* Method: `POST`.  
    
* Path: `/internal/dev/sampler`.  
    
* Bound to the existing reader blueprint, but with **dev/admin-only** gating and HTTP posture as defined here.

APP\_ENV gate:

* The handler **MUST** enforce `APP_ENV ∈ {dev, test, local}`:  
    
  * When `APP_ENV` is exactly one of `dev`, `test`, or `local`, the handler may proceed to validate input and call the sampler core.  
      
  * When `APP_ENV` is unset, empty, or outside `{dev,test,local}`, the handler MUST return status `403` with the canonical `error_v1` envelope carrying `code:"ERR_WRITER_FORBIDDEN"`; it MUST NOT call the sampler core. The response uses `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, and no `ETag`.

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
      
  * `Cache-Control: no-store`.  
      
  * No `ETag`; this route is not an A7 surface.


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

* `POST /internal/dev/sampler` is a **dev/admin-only internal harness** included in the internal Endpoint Catalog as `dev_harness`, `internal:true`, and `a7_eligible:false`. It remains excluded from `success_endpoints`, A7 proof selection, and public contracts. `GET /internal/dev/sampler` remains unsupported.  
    
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

## **6.2 Unify entrypoint (single presenter/emitter) \[Required-Now\]**

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

### **7.1.10 Endpoint policy (explicit version-gated dual lineage)**

**Normative route selection.**

`bg:resolve --source vendor` selects one full-detail route from the validated terminal API-version segment of the configured base:

* A terminal, case-sensitive `v2` segment selects the version-neutral resource `charts`.  
* A terminal, case-sensitive `v1` segment selects the intentionally retained legacy resource `bodygraphs`.  
* An unversioned base, unsupported version, nonterminal version marker, multiple conflicting version markers, or otherwise ambiguous base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or any external I/O.  
* Route selection is immutable for the invocation. A v2 request failure never triggers a v1 request, and a v1 request failure never triggers v2.

The low-level provider contract retains `charts`, `charts/simple`, `charts/coordinates`, `bodygraphs`, and `bodygraphs/simple`. Only full `charts` and full `bodygraphs` are resolver-selectable. The other three resources remain contracted inventory for request-building and conformance work; they are not retired, do not establish live provider availability, and cannot satisfy the full resolver contract merely because their request shape is known.

**Configured-base boundary.**

`HD_API_BASE_URL` is canonical. `HDAPI_BASE_URL` is a deprecated compatibility alias during the existing migration window only. Normalize a candidate by trimming surrounding ASCII whitespace and trailing `/` characters for comparison and joining; preserve every other configured path prefix. The URL must be absolute HTTPS, contain a host, contain no userinfo, query, or fragment, and end in exactly `v1` or `v2`.

If both environment names are present, both normalized URLs must be byte-equal. A conflict produces `PROVIDER_CONFIG_INVALID` before I/O. If the canonical name is absent, the compatibility alias may supply the value. If both are absent, return `PROVIDER_CONFIG_MISSING`. Append exactly one `/` and the version-neutral resource; never append another version segment and never follow redirects.

**Legacy and claim boundary.**

The explicit v1 `bodygraphs` path is retained legacy selection, not fallback. No legacy route is retired by repository nonselection. Retirement requires a separately versioned decision with consumer, migration, evidence, and rollback review.

The bounded Fermentation work and repository request builders do not establish broad HumanDesignAPI v2 platform conformance, live route availability, public Reader change, production mapped-cache persistence, or QA acceptance. A complete full-route response may enter only the existing governed HDE normalization boundary; simple results cannot be promoted to complete BodyGraph detail.

**Privacy / payload constraints:**

* Vendor HTTP MUST NOT receive internal user ids or other internal identifiers.  
* Public Reader output remains bands-only and numeric-free.  
* This pending v2 endpoint posture creates no new public Reader route and no public Reader contract change.

---

### **7.1.11 SAFE rails and production vendor override**

Vendor HTTP remains subject to the generic SAFE rails in **HDE-Governance**. Closed SAFE or network rails refuse before every vendor decision and perform no credential loading, DNS, socket, or HTTP activity. The production override is an additional admin gate; it never opens either generic rail and never permits public Reader or Aux traffic to call the vendor.

#### **7.1.11a Exact CLI flag**

The only production authorization flag in this selection is:

```
--allow-prod-vendor <AUTHORIZATION_REF>
```

It is one value-bearing flag accepted only by `hdctl bg:resolve --source vendor`. It has no short spelling, compatibility alias, negated form, environment-variable form, or implicit default.

`AUTHORIZATION_REF` is an audit reference, not a credential. It must contain 1–128 ASCII characters and match:

```
^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$
```

An empty value, control character, whitespace, character outside the allow-list, missing value, or duplicate occurrence is invalid. The reference identifies the approved Product Owner work item or recorded Product Owner delegation and must never contain a token or secret.

#### **7.1.11b Environment classification**

`APP_ENV` is canonical. `ENGINE_ENV` is a compatibility alias for this CLI gate only when `APP_ENV` is absent or blank.

* Normalize by trimming ASCII whitespace and lowercasing.  
* Production-like values are exactly `prod`, `production`, and `live`.  
* Recognized non-production values are exactly `dev`, `test`, `local`, `stage`, and `staging`.  
* Treat an unset or all-whitespace value as absent.  
* If both names are nonblank, their normalized values must be equal; a conflict is `PROVIDER_CONFIG_INVALID`.  
* Use nonblank `APP_ENV`; otherwise use nonblank `ENGINE_ENV`.  
* If neither is nonblank, or the effective value is outside both allow-lists, return `PROVIDER_CONFIG_INVALID` before I/O. Never treat an unknown label as non-production.

The flag never changes environment classification.

#### **7.1.11c Rail and flag matrix**

| Effective environment | Generic rails | Override flag | Result |
| :---- | :---- | :---- | :---- |
| any recognized value | `SAFE_MODE` closed | any | existing `PROVIDER_REFUSED`; zero vendor I/O |
| any recognized value | network not allowed | any | existing `PROVIDER_NETWORK_BLOCKED`; zero vendor I/O |
| `prod`, `production`, or `live` | both rails open | absent | `PROVIDER_PROD_OVERRIDE_REQUIRED`; zero vendor I/O |
| `prod`, `production`, or `live` | both rails open | malformed or duplicated | CLI usage error; zero vendor I/O |
| `prod`, `production`, or `live` | both rails open | valid, but actor identity or audit sink unavailable | `PROVIDER_AUDIT_UNAVAILABLE`; zero vendor I/O |
| `prod`, `production`, or `live` | both rails open | valid and auditable | vendor read/resolve may proceed, subject to every route, credential, retry, and write guard |
| recognized non-production | both rails open | absent | normal non-production vendor policy |
| recognized non-production | both rails open | present | `PROVIDER_PROD_OVERRIDE_INVALID`; zero vendor I/O |

The familiar open representation is `SAFE_MODE=0` and `ALLOW_NETWORK=1`. The production flag substitutes for neither value.

#### **7.1.11d Evaluation order and scope**

Evaluate the gates in this order before client construction, secret loading, DNS, sockets, or HTTP:

1. Parse the command and reject malformed, duplicated, or inapplicable flags.  
2. Confirm `--source vendor`; using the flag with `--source db` or `--source auto` is a CLI usage error.  
3. Apply the generic SAFE and network rails.  
4. Resolve and validate the effective environment.  
5. Apply the production/non-production flag matrix.  
6. Resolve authenticated actor identity and durably write the pre-I/O audit event.  
7. Apply base-URL, route, credential-presence, request, retry, and any separate persistence gates.

The flag authorizes only one bounded admin vendor HTTP opportunity. It does not authorize public Reader/Aux vendor traffic, production `--upsert`, any production database write, bypass of `PROVIDER_WRITE_UNSUPPORTED`, a route or version, credentials, expanded retries, or a no-network dry run. A production dry run that contacts the vendor still requires the flag.

#### **7.1.11e Error carrier and authorized setter**

A missing value, duplicate flag, invalid syntax, or use with a non-vendor source uses the canonical CLI usage carrier and exits `64`. Runtime policy refusals use the canonical `status="error"` resolver envelope with one stable typed code and a non-sensitive message and exit `1`. Every refusal has outbound-attempt count `0`.

The authorized initiator is an authenticated human Product Owner or a human operations executor explicitly delegated by the Product Owner in the referenced approved work item. An AI agent, CI job, application request, or unauthenticated shell cannot self-authorize by supplying the flag. Actor identity comes from the authenticated execution environment or control plane, never a free-form `--operator` value. If a stable authenticated actor identity is unavailable, refuse the operation. The authorization reference records the decision basis; it is not authentication and grants no privilege by itself.

#### **7.1.11f Audit contract**

Every production-like invocation that reaches semantic override evaluation, including an absent, invalid, refused, or allowed authorization reference, creates one append-only, locally durable, keys-only event before I/O. A syntax failure that prevents parsing, including a duplicate flag or missing value, remains observable through the trusted process/control-plane audit rather than an application event assembled from unparsed arguments.

| Field | Rule |
| :---- | :---- |
| `schema_version` | fixed audit schema version |
| `event` | exactly `vendor_prod_override` |
| `occurred_at` | UTC timestamp from the governed clock boundary |
| `correlation_id` | generated by the trusted runtime; not supplied as birth or user data |
| `actor_principal` | authenticated OS/control-plane principal |
| `authorization_ref` | validated flag value, or `null` when absent |
| `command` | exactly `bg:resolve` |
| `source` | exactly `vendor` |
| `environment` | normalized production alias |
| `safe_mode_open` | boolean result only |
| `network_open` | boolean result only |
| `route_family` / `resource_path` | allow-listed label if route classification was reached; otherwise `null` |
| `outcome` | one of `refused`, `allowed`, `failed`, `completed` |
| `error_code` | stable typed code or `null` |
| `outbound_attempted` | boolean; never a raw request count with subject data |

Do not record `--user`, birth date, birth time, location, coordinates, request or response bodies, configured URL, header values, tokens, API keys, geocode keys, database identifiers, or raw provider messages. Sanitize audit fields against CR/LF and delimiter injection. The flag value, actor, and policy state never appear in an exception string or raw diagnostic outside the governed audit record.

Failure to persist the pre-I/O event is `PROVIDER_AUDIT_UNAVAILABLE` and blocks the call. A post-I/O completion event may update the same correlation record or append a second state event under the audit schema, with the same exclusions.

---

## **7.2 Request Shaping (owned here) \[Required-Now\]**

**Purpose.** Define the exact route-scoped HDAPI request and response contract used by vendor resolution: base-URL validation, resource selection, method, headers, request object, serialization, response-family validation, and provider-to-HDE typed mapping. Rails and enablement live in §7.1.

### **7.2.0 Contract and implementation posture**

The contract in this section is Required-Now. Static inspection of the pinned repository confirms low-level request builders for all five inventoried resources and current resolver selection of v2 `charts` or legacy `bodygraphs`; it also shows material gaps against this contract: broad non-v2 legacy selection, no production-vendor override flag or audit gate, and retry configuration outside the five approved tuples. Repository definitions do not establish runtime success, deployment, live-provider availability, or QA acceptance.

Existing governed evidence records source selection, deterministic request-shaping proof, proof-level response-envelope mapping, adapter/presenter boundary proof, closed-rails refusal, a bounded `charts/coordinates` open-rails smoke, field-sufficiency proof, deterministic `ChartResult` adapter mapping, configured-v2 dry-run route wiring, mapped v2-to-compat proof, bounded open-rails runtime smoke evidence, and parent evidence binding. Those bounded proof slices do not claim broad HumanDesignAPI v2 platform conformance, normalized-data-path completeness beyond their stated scope, production deployment, production upsert, public Reader changes, new HTTP homes, app-side vendor ownership, raw payload persistence, QA PASS, OPS completion by documentation, or AI scope.

Contract interpretation retains the validated source precedence: validated `v2-routes.yaml` and `v1-routes.yaml`, rendered endpoint pages, then high-level guide pages. A suspect API-description artifact does not define PF05 bytes until its domain, title, server, and route family are validated.

PF05 preserves the distinction between v2 full chart, v2 simple chart, coordinate-route chart, legacy full BodyGraph, legacy simple BodyGraph, raw payload-family sufficiency, deterministic adapter mapping, mapped cache posture, mapped-cache persistence, and the normalized HDE BodyGraph/person/cache contract. `ChartSimpleResult` and `SimpleBodygraphResponse` are not sufficient for full resolver success.

HumanDesignAPI vendor acquisition, request shaping, credential handling, response normalization, BodyGraph persistence/retrieval, and HDE computation remain inside the HD Engine boundary. This contract introduces no OpenAI, LLM, agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, or AI QA obligation.

### **7.2.1 Endpoints, method, and base URL**

**Base resolution.**

* `HD_API_BASE_URL` is canonical; deprecated `HDAPI_BASE_URL` may supply the value only when the canonical name is absent.  
* Trim surrounding ASCII whitespace and trailing `/` characters for comparison and joining; preserve every other path prefix.  
* Require absolute HTTPS, a host, no userinfo, no query, no fragment, and final non-empty path segment exactly `v1` or `v2`.  
* If both names are present, require normalized byte equality. A conflict is `PROVIDER_CONFIG_INVALID`; both absent is `PROVIDER_CONFIG_MISSING`.  
* Append exactly one `/` and the version-neutral resource path. Do not hardcode another version segment.  
* Use `POST` with no query. Do not follow redirects; any `3xx` is classified without replaying credentials.

**Resource support and exact request contract.**

| Resource | Configured lineage | `bg:resolve` status | Exact request object | Authentication | Geocode header | Success family |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `charts` | terminal `v2` | **SUPPORTED; selected full route** | `birthdate`, `birthtime`, `location` only | `Authorization: Bearer <HD_API_KEY>` | required: `HD-Geocode-Key: <GEO_API_KEY>` | v2 `StandardResponse`, `type="ChartResult"` |
| `charts/simple` | terminal `v2` | **CONTRACTED INVENTORY; not resolver-selectable** | `birthdate`, `birthtime`, `location` only | `Authorization: Bearer <HD_API_KEY>` | required: `HD-Geocode-Key: <GEO_API_KEY>` | v2 `StandardResponse`, `type="ChartSimpleResult"` |
| `charts/coordinates` | terminal `v2` | **CONTRACTED INVENTORY; not resolver-selectable** | `birthdate`, `birthtime`, `lat`, `lng` only | `Authorization: Bearer <HD_API_KEY>` | forbidden | v2 `StandardResponse`, `type="ChartResult"` |
| `bodygraphs` | terminal `v1` | **SUPPORTED; selected legacy full route** | `birthdate`, `birthtime`, `location` only | `HD-Api-Key: <HD_API_KEY>` | required: `HD-Geocode-Key: <GEO_API_KEY>` | flat v1 `BodygraphResponse` |
| `bodygraphs/simple` | terminal `v1` | **CONTRACTED LEGACY INVENTORY; not resolver-selectable** | `birthdate`, `birthtime`, `location` only | `HD-Api-Key: <HD_API_KEY>` | required: `HD-Geocode-Key: <GEO_API_KEY>` | flat v1 `SimpleBodygraphResponse` |

Contracted inventory permits the low-level request builder and conformance tests to describe and validate a route. It does not make the route resolver-selectable, prove that a live account supports it, or make a simple payload sufficient for the normalized full-detail contract.

### **7.2.2 Canonical headers (dash-case, exact on wire)**

Every request sends:

* `Accept: application/json`  
* `Content-Type: application/json; charset=utf-8`  
* exactly one route-appropriate authentication header  
* `HD-Geocode-Key: <GEO_API_KEY>` only where §7.2.1 requires it  
* `User-Agent: GlowHDEngine/<release_id>`, where `release_id` is lowercase 64-hex

Never send both authentication families. Never send a geocode secret on `charts/coordinates`. Do not add another header unless a later governed PF05 contract pins it.

API and geocode keys are secrets. Never echo their values in logs, errors, or evidence. Persisted header captures follow the canonical normalization rules in **HDE-Schemas & Artifacts**; on-wire casing remains exact as shown.

### **7.2.3 Route-scoped request objects**

**v2 location routes: `charts` and `charts/simple`.**

```json
{"birthdate":"YYYY-MM-DD","birthtime":"HH:MM","location":"<location>"}
```

* `birthdate` is the supplied local civil birth date in valid, zero-padded Gregorian `YYYY-MM-DD` form.  
* `birthtime` is the supplied local civil birth time in zero-padded 24-hour `HH:MM` form from `00:00` through `23:59`; seconds and a timezone suffix are forbidden.  
* `location` is one JSON string, not a structured object. Trim outer whitespace; require 4–200 Unicode scalar values; preserve spelling and diacritics without transliteration, case-folding, or inferred replacement.

**v2 coordinate route: `charts/coordinates`.**

```json
{"birthdate":"YYYY-MM-DD","birthtime":"HH:MM","lat":0,"lng":0}
```

The date and time rules match v2 location routes. `lat` and `lng` are finite JSON numbers, not strings or booleans. Latitude is within `[-90, 90]`; longitude is within `[-180, 180]`. `NaN` and infinities are invalid. The object contains no `location`, and the request sends no geocode header. The current CLI has no governed coordinate-input surface, so this route is not resolver-selectable.

**v1 routes: `bodygraphs` and `bodygraphs/simple`.**

```json
{"birthdate":"DD-MMM-YYYY","birthtime":"HH:MM","location":"<location>"}
```

Convert a validated input date mechanically to zero-padded `DD-MMM-YYYY` with the fixed English month set `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`. Preserve the same `HH:MM` and one-string location rules. The four-scalar minimum is a provider-source rule; the 200-scalar maximum is a Glow safety limit, not a provider-support claim.

No request contains `tz`. The vendor derives timezone from the governed route input. PF05 does not manufacture, infer, or repair timezone data at this boundary.

Every route request object uses unique names, lexicographically sorted keys, no insignificant whitespace, minimum required JSON escapes, UTF-8 encoding, no BOM, and exactly one terminal LF. Request construction has no AI transformation, heuristic location correction, timezone guess, or fallback body.

**Route-scoped response acceptance.**

A successful v2 response is a JSON object with required `StandardResponse` members `timestamp`, `success`, `message`, `errorCode`, `type`, and `data`. `success` must be JSON `true`; `errorCode` must be a string empty after trimming; `type` must exactly match the route family; and `data` must be a conforming JSON object. Missing members, wrong types, duplicate object names, malformed JSON, a route-family mismatch, or non-object `data` produce `PROVIDER_BAD_RESPONSE`. A well-formed provider-declared failure produces `PROVIDER_ERROR`. Its public carrier may contain only a bounded, allow-listed provider-code label and never echoes `message`, raw bytes, request values, or secrets. Unknown extra provider members may be ignored only at the adapter boundary and are never logged, persisted, or promoted into the normalized HDE contract.

Full `ChartResult` requires: `activations`, `authority`, `birthDateUtc`, `centers`, `channelsLong`, `channelsShort`, `circuitries`, `cognition`, `definition`, `determination`, `distraction`, `environment`, `gates`, `incarnationCross`, `motivation`, `notSelfTheme`, `perspective`, `profile`, `signature`, `strategy`, `transference`, `type`, and `variables`. Mapping may use only governed normalized fields and never synthesizes a missing field. `ChartSimpleResult` remains insufficient for full resolver success.

A v1 `bodygraphs` response must be the validated flat `BodygraphResponse`; `bodygraphs/simple` must be the flat `SimpleBodygraphResponse`. A v2 wrapper on a v1 route, a flat v1 response on a v2 route, or a simple response presented as full detail is `PROVIDER_BAD_RESPONSE`.

Configuration absence or conflict maps to `PROVIDER_CONFIG_MISSING` or `PROVIDER_CONFIG_INVALID`. An unsupported or ambiguous base maps to `PROVIDER_ROUTE_UNSUPPORTED`. Any redirect or otherwise unmapped status maps to `PROVIDER_ERROR`. None is retryable. §7.2.5 retains the HTTP status mapping; §7.3 owns the exact retry budget and profiles.

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
     
4. Determinism. Shaping output is identical for AB vs BA. No locale, time, or random dependence. Checks run under `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
     
5. Error mapping. Each provider outcome maps to the typed error above. `retry_after_ms` is integer, non-negative, and omitted on invalid formats.  
     
6. Hygiene. All emitted JSON is canonical (UTF-8 no BOM, sorted keys, compact, one LF).

Evidence (records-only; titles-only; indexed via PF12).

* `vendor/shaping_example` — canonical headers, body, and URL (no secrets).  
    
* `rails/closed_refusal` — typed refusal proof (no I/O).  
    
* `rails/open_conformance` — header redaction and policy proof (if rails opened in an integration profile).

Indexing discipline: governed evidence identities and paths, Human Index and sentinel behavior, Machine Mirror schema, parity, checksums, and path-proofs are single-homed in **HDE-Schemas & Artifacts** and must be updated coherently when that contract requires it.

Routing (titles-only).  
Rails and enablement: §7.1. Live HTTP policies: §7.3. Canonical JSON and capture normalization: HDE-Schemas & Artifacts §4. Governance tokens and keys-only allow-lists: HDE-Governance §2.0.

---

## **7.3 Live HTTP Call Behavior \[Required-Now\]**

### **7.3.1 Scope and prerequisites**

Rails open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); env ready (`HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when needed); shaping fixed per §7.2. Deprecated `HDAPI_BASE_URL` may be used only as an explicitly labeled temporary compatibility alias when `HD_API_BASE_URL` is absent; conflicting values fail closed.

### **7.3.2 Timeouts (closed integers)**

Domains (ms):

* `connect_timeout_ms ∈ {1000,2000,5000}`  
    
* `read_timeout_ms ∈ {2000,5000,10000}`  
    
* `total_timeout_ms ∈ {5000,10000,15000,30000}`

One `timeout_profile ∈ {small, default, long}` pins the triple.

### **7.3.3 Retries, status classification, and redirects (deterministic classes)**

`max_attempts` counts the initial HTTP request. Its exact domain is the integer set `{1,2,3}`. JSON booleans, floats, numeric strings, zero, negatives, and values above three are invalid and produce `PROVIDER_CONFIG_INVALID` before request construction or I/O.

`max_retries = max_attempts - 1`

Automatic retry classes are exactly `network_error` and HTTP `5xx`. Input or configuration errors, unsupported routes, authentication failures, `404`, `429`, redirects, provider-declared v2 failures, type mismatches, malformed payloads, other `4xx`, and other statuses are not retryable.

Non-`4xx`/`5xx` non-`200` statuses are classified as `http_status_other`, mapped to `PROVIDER_ERROR`, and recorded with `retried:false` when governed proof captures that fact.

The default vendor path never follows redirects. A redirect status, including `302`, is surfaced with its response body and headers for bounded classification; credentials are never replayed to `Location`. HTTP error responses from the default path are converted into status, body, and header tuples before classification so injected and default paths use the same typed mapping.

### **7.3.4 Backoff profiles (exact tuples; no jitter)**

Only these complete tuples are valid:

| `max_attempts` | `backoff_kind` | `base_ms` | `ceiling_ms` | Schedule |
| ----: | :---- | ----: | ----: | :---- |
| 1 | `none` | 0 | 0 | one initial attempt; no retry |
| 2 | `fixed` | 250 | 250 | at most one retry after 250 ms |
| 2 | `fixed` | 500 | 500 | at most one retry after 500 ms |
| 3 | `exponential` | 250 | 500 | retry after 250 ms, then 500 ms |
| 3 | `exponential` | 500 | 2000 | retry after 500 ms, then 1000 ms; **default** |

The default tuple is exactly `(3, "exponential", 500, 2000)`. Profile fields are not independently mixable; every other Cartesian combination is invalid.

Attempt 1 has no preceding delay. A fixed profile uses `base_ms` for every retry and requires `base_ms == ceiling_ms`. For an exponential profile, the delay before retry ordinal `r` is `min(base_ms × 2^(r-1), ceiling_ms)`, where `r=1` precedes attempt 2\.

There is no jitter, random seed, wall-clock-dependent selection, provider-body-dependent selection, hidden retry, or `Retry-After` rescheduling. The selected total operation budget remains a hard ceiling across connection, response, and backoff. If the remaining budget cannot contain the next scheduled attempt, stop with the most specific safe typed failure without exceeding the budget.

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

HumanDesignAPI v2 broad platform conformance remains bounded and must not be overclaimed. HDE-EPIC035 evidence records provider-outcome and rate-limit mapping for HDE-FERM008.3, exact response-normalization schema/adapter gap posture for HDE-FERM008.4, retained OPS-01 live-vendor observations, and PR-03 governed evidence-loop binding for HDE-FERM008.5. HDE-EPIC036 evidence records explicit `bg:resolve --source vendor` route-policy classification and evidence-loop binding for HDE-FERM008.6. HDE-EPIC037 evidence records field-sufficiency proof for HDE-FERM008.7, deterministic v2 ChartResult adapter mapping for HDE-FERM008.8, configured-v2 `bg:resolve --source vendor --dry-run` charts-route wiring for HDE-FERM008.9, mapped v2-to-compat proof for HDE-FERM008.10, PO-produced bounded open-rails runtime smoke evidence for HDE-FERM008.11, and parent evidence binding for HDE-FERM008.12. The HDE-EPIC037 parent posture is supportable to Done for later PF09 drainage only. These proof slices do not themselves claim QA PASS, OPS completion by PR work, PF09 status movement, PO closeout, board update, merge action, PF-canon edit, epic closeout, production deployment, broad HumanDesignAPI v2 platform conformance beyond the bounded HDE-FERM008.7 through HDE-FERM008.11 evidence chain, public Reader changes, public route or payload changes, new HTTP homes, app-side vendor ownership, raw payload persistence, or AI scope.

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

**Configured-v2 mapped-cache write boundary.** For configured v2 bases, current `bg:resolve --source vendor` uses the version-neutral `charts` route and deterministic v2 `ChartResult` adapter. `--dry-run` performs no DB write. A non-dry-run mapped-cache write is permitted only with explicit `--upsert`, open rails, non-production posture in both requested and process `APP_ENV`/`ENGINE_ENV`, an available sanctioned `DBAccess` target, and successful adapter mapping. The write stores adapter-mapped HDE BodyGraph/cache data only, never a raw HumanDesignAPI v2 envelope, and MUST preserve canonical write/read-back parity, one-row identity, idempotence, no raw secret/request/response/vendor-payload persistence, and closed-rails zero-I/O refusal. Missing upsert intent or production-like posture fails closed with `PROVIDER_WRITE_UNSUPPORTED`. Production or production-like user-bound upsert remains closed until a later authorized epic explicitly reopens that scope.

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

* **Reader↔CLI byte-equality.** For identical inputs and environment, Reader response bytes and Reader-v1 bytes written by `hdctl showcompat --dump-reader <path>` MUST be byte-identical, including the single trailing LF. Ordinary `showcompat` stdout remains the distinct compat JSON envelope.  
* **AB↔BA identity.** Swapping pair order produces **bit-for-bit identical** bytes (pair normalization in effect).

* ## **Two-run identity.** Two serializations under identical inputs produce **byte-identical** output.

## 9.2 Idempotence (binary)

* **Preimage re-check.** Remove `idempotence_hash`, canonicalize the five-key preimage with the single emitter, compute `sha256(preimage_bytes)`, and verify it equals the published `idempotence_hash`.

* ## **Scope.** Check holds for **both** Reader **and** CLI outputs.

## 9.3 Transport (A7) invariants (binary)

* **ETag / 304 / HEAD.** Emit **strong, quoted ETag** on `200`; return `304` **only after** a prior `200`\-with-body for that identity; `HEAD` **mirrors `200` validators** and has **no body**.  
* **304 entity headers (tightened).** **Omit both** `Content-Type` **and** `Content-Length` on `304`; body is empty.  
* **POST is non-conditional.** `POST` never carries validators and never returns `304`.  
* **Cache semantics.** `200`/`HEAD`: `Cache-Control: private, max-age=0, must-revalidate`. Writers/errors: `Cache-Control: no-store`.  
* **Content-Type on 200\.** `Content-Type: application/json; charset=utf-8`.  
* **Vary (required).** `Vary: Authorization, Accept-Encoding` present.

* ## **Encoding invariance.** For the same canonical body, the **identity ETag** and **HEAD identity length** (LF-terminated, pre-compression) are stable across accepted `Accept-Encoding` selections (`identity`, `gzip`, `br`).

## 9.4 Vendor rails acceptance (binary)

* **Refusal posture (rails closed).** With rails closed (any of `SAFE_MODE!=0` **or** `ALLOW_NETWORK!=1`), vendor calls **MUST NOT** perform network I/O and **MUST** return a typed refusal (numeric-free), with secrets redacted.  
* **Shaping correctness (closed).** Request shaping (endpoint, headers, body) remains **deterministic** and **order-neutral** without sending the request.

* ## **Conformance when opened.** With rails open and env present, live calls obey pinned **timeouts/retries/backoff**; typed error mapping is deterministic; **no payload/secret logging**; parity/identity remain unaffected.

## 9.5 Evidence posture (titles-only; PF12 single home)

* **PF05 proof families.** Maintain current, truthful evidence for Reader↔CLI, AB↔BA and two-run parity; idempotence recomputation; Reader transport; canonical emission; and vendor-rails refusal/open-conformance where an authorized open-rails run exists.  
* **No status inference.** A path, file, test, mirror record, checklist row, or stored token does not by itself prove generation, execution, PASS, acceptance, closure, deployment, or production readiness.  
* **Single home.** Evidence-family identities and paths, Human Evidence Index, hash sentinel, Machine Evidence Mirror, complete record schemas, parity, checksums, path-proofs, same-change requirements, and regeneration rules are owned by **HDE-Schemas & Artifacts**. PF05 does not restate those contracts.  
* **Process and tokens.** Merge workflow lives in **Epic-Process-Guide** and token semantics live in **HDE-Governance**. PF05 names neither a parallel token roster nor a parallel path list.

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
* v2.4.6 — Clarify PF10 addendum precedence and pin the supported invocation, fixed input, failure classification, and migration boundary for `ci/checks/check_mirror_schema.sh` in §§0.2 and 0.4. Sentinel updated: NO.  
* v2.4.7 — Define the closed CLI success-carrier set and fail-closed birth-time timezone-source precedence, ambiguity, fold/gap, provenance, and typed-refusal contract in §§0.2 and 3\. Sentinel updated: NO.  
* v2.4.8 — Define the Required-Now `admin_bundle_v1` CLI and `POST /internal/admin/bundle/v1` contracts, including authentication, request/response bytes, audit identity, file receipt, and parity in §4.9. Sentinel updated: NO.  
* v2.4.9 — Define the PF12-owned `public_aux` Catalog alias model, reject undocumented Aux query controls, require exactly one `v=1`, and normalize the §6.2 status tag in §§5–6. Sentinel updated: NO.  
* **Where to put links.** Governed artifact identities and paths are indexed through the Evidence Catalog in **HDE-Schemas & Artifacts**; do not paste payload or transport bytes here. If the Human Evidence Index changes, record “Sentinel updated: YES” only after recomputing `docs/evidence/INDEX.sha256`; the sentinel is the SHA-256 digest of the canonical bytes of `docs/evidence/INDEX.json` and is not mirrored.

## **11.2 Doc-Delta Hooks (how we propose, review, and land changes)**

**Purpose.** Provide a uniform, auditable record for a normative PF05 change without duplicating evidence schemas, paths, token semantics, or process rules owned elsewhere.

### **11.2.1 Doc-Delta template**

* **Doc-Delta ID / date / author:** stable identifier and accountable owner.  
* **Scope:** affected PF05-owned CLI, Reader-transport, serializer/emitter, vendor-ingest, or acceptance behavior.  
* **Targets:** PF05-local section anchors only.  
* **Normative delta:** at most five concrete action bullets, including exact byte/behavior changes.  
* **Acceptance impact:** name the affected parity, idempotence, transport, vendor-rails, security, or compatibility proof families; do not assert PASS.  
* **Evidence impact:** name affected governed evidence families and route all identities, paths, record schemas, checksums, and path-proofs to **HDE-Schemas & Artifacts**.  
* **Sentinel impact:** `Yes/No`. If Yes, recompute `docs/evidence/INDEX.sha256` from canonical `docs/evidence/INDEX.json` bytes and note “Sentinel updated: YES” in the Change Log.  
* **Freeze-pack impact:** `Yes/No`; if Yes, record the newly governed release identity through its owning contract.  
* **Rollout and rollback:** implementation order, verification hooks, failure posture, and rollback boundary.

### **11.2.2 Acceptance to land**

A Doc-Delta is accepted only when the owning binary gates have governed execution evidence; affected evidence families and required companions are coherent under **HDE-Schemas & Artifacts**; the Human/Machine join and sentinel are current when applicable; and any freeze-pack identity change is governed. A stored artifact, test definition, checklist status, or token name is not a substitute for that execution evidence. Otherwise the Doc-Delta is rejected; no partial normative merge is implied.

### **11.2.3 Guardrails**

* Reader and CLI public bytes use the same byte-authoritative presenter; no local public emitter.  
* Reader v1 remains numeric-free and field-closed.  
* PF05 owns its transport/CLI/vendor bytes and routes other contracts by canonical title.  
* Locale, clock, random, ordering, and trailing-LF behavior remain deterministic.  
* Workflow lives in **Epic-Process-Guide**; evidence schema/path ownership lives in **HDE-Schemas & Artifacts**; token semantics live in **HDE-Governance**.

---

# **Appendix A — Transport Matrices (headers, conditional rules, examples) \[Required-Now\]**

**Purpose.** Pin the Reader transport behavior the CLI must emit or parity-check. These matrices are normative for CLI/Reader and are kept in lockstep with HDE-Governance §10 (titles only). They cover at minimum: 200 strong quoted ETag; 304-after-200 with no body and omitted Content-Type and Content-Length; HEAD parity (no body; Content-Length equals identity 200 body; Content-Type \== GET); writers/errors no-store with no ETag; and encoding-invariance of identity across Accept-Encoding. Architecture and Math are referenced by title only.

**Proof surface.** Proofs run on a cataloged JSON success route listed in §5.6 (not on `/internal/version`). Byte rules are owned here; examples live in tests and PF12 evidence artifacts (titles only).

## **A.1 Success (200) — required headers**

* Content-Type: `application/json; charset=utf-8`  
* ETag: `"<strong, quoted>"` (identity over the final LF-terminated body; MUST be present on 200; identity is computed over pre-compression bytes)  
* Vary: `Authorization, Accept-Encoding`  
* Cache-Control: `private, max-age=0, must-revalidate`

## **A.2 304 Not Modified (conditional GET)**

**Preconditions.** A prior 200 success with a strong, quoted ETag exists, and the request presents a matching `If-None-Match`.

**Body.** None.

**Headers.**

* ETag present (matches the cached 200\)  
* Mirror 200 validators (Cache-Control, Vary)  
* Omit Content-Type  
* Omit Content-Length

## **A.3 Writers and errors**

* Cache-Control: `no-store` (MUST)  
* No ETag (MUST)  
* Errors: `Content-Type: application/json; charset=utf-8` and LF-terminated body

## **A.4 HEAD parity**

* **Status.** 200  
* **Body.** None  
* **Validators.** Headers equal the 200 success validators for the same resource (including Content-Type)  
* **Length.** `Content-Length == len(identity 200 body)` (pre-compression)  
* **Type.** `Content-Type` on HEAD equals GET

## **A.5 POST semantics**

* **Non-conditional.** Requests do not send validators; responses never return `304`.  
* **POST responses.** Successful POST responses do not carry validators. Writer-style POSTs remain `no-store` with no `ETag`.

## **A.6 Encoding invariance (accepted Accept-Encoding: identity, gzip, br)**

* **Identity stability.** For the same canonical body, the ETag identity is unchanged across accepted encodings.  
* **Length stability.** The effective Content-Length of the identity body is invariant across accepted encodings.  
* **Evidence.** Capture on a cataloged JSON success route; artifacts are listed and indexed in PF12 (human `INDEX.json` \+ hash sentinel \+ machine mirror, same-PR rule).

## **A.7 Aux Narrative (excerpt, Aux Narrative)**

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

# **Appendix B — Vendor Request/Response Examples (typed mapping tables; redact secrets) \[Speculative\]**

**Purpose.** Provide **redacted** examples for HDAPI interactions to aid integration tests. These are **illustrative**, follow §7.2 request shaping, and obey §7.3 policies when rails are open. **Never** include real keys or payload bodies in logs.

## **B.1 Request (redacted example; rails open)**

The validated configured base owns the version segment. Each request uses a version-neutral resource and exactly the route-specific object and headers below.

| Resource | Resolver-selectable | Body members | Auth | Geocode |
| :---- | :---- | :---- | :---- | :---- |
| `charts` | terminal v2 full route | `birthdate`, `birthtime`, `location` | `Authorization: Bearer <redacted>` | `HD-Geocode-Key: <redacted>` |
| `charts/simple` | no; contracted inventory | `birthdate`, `birthtime`, `location` | `Authorization: Bearer <redacted>` | `HD-Geocode-Key: <redacted>` |
| `charts/coordinates` | no; contracted inventory | `birthdate`, `birthtime`, `lat`, `lng` | `Authorization: Bearer <redacted>` | forbidden |
| `bodygraphs` | terminal v1 legacy full route | `birthdate`, `birthtime`, `location` | `HD-Api-Key: <redacted>` | `HD-Geocode-Key: <redacted>` |
| `bodygraphs/simple` | no; contracted legacy inventory | `birthdate`, `birthtime`, `location` | `HD-Api-Key: <redacted>` | `HD-Geocode-Key: <redacted>` |

**v2 full location request.**

```
POST /v2/charts
Accept: application/json
Authorization: Bearer <redacted>
Content-Type: application/json; charset=utf-8
HD-Geocode-Key: <redacted>
User-Agent: GlowHDEngine/<release_id>

{"birthdate":"YYYY-MM-DD","birthtime":"HH:MM","location":"<location>"}
```

**v2 coordinate-inventory request.**

```
POST /v2/charts/coordinates
Accept: application/json
Authorization: Bearer <redacted>
Content-Type: application/json; charset=utf-8
User-Agent: GlowHDEngine/<release_id>

{"birthdate":"YYYY-MM-DD","birthtime":"HH:MM","lat":0,"lng":0}
```

**v1 retained-legacy full request.**

```
POST /v1/bodygraphs
Accept: application/json
Content-Type: application/json; charset=utf-8
HD-Api-Key: <redacted>
HD-Geocode-Key: <redacted>
User-Agent: GlowHDEngine/<release_id>

{"birthdate":"DD-MMM-YYYY","birthtime":"HH:MM","location":"<location>"}
```

The displayed paths illustrate a configured base ending in `/v2` or `/v1` joined to the version-neutral resource. Runtime route constants contain no version segment. The serialized JSON request object has sorted unique keys, no insignificant whitespace, UTF-8 encoding, no BOM, and one LF. The placeholder `<release_id>` is the governed lowercase 64-hex value; no example authorizes a literal placeholder on wire.

Simple and coordinate resources remain low-level contracted inventory, not `bg:resolve` choices. A simple response cannot satisfy full BodyGraph resolution. A route or payload example never authorizes public Reader vendor traffic, production persistence, or cross-lineage fallback.

## **B.2 Response → typed error mapping (deterministic)**

A v2 success uses `StandardResponse` and a route-matching `type`: `ChartResult` for `charts` and `charts/coordinates`, or `ChartSimpleResult` for `charts/simple`. A v1 success is the matching flat `BodygraphResponse` or `SimpleBodygraphResponse`. Cross-family wrappers, wrong route types, incomplete full-detail results, malformed JSON, and duplicate object names are `PROVIDER_BAD_RESPONSE`.

| Condition | Canonical code | Retry |
| :---- | :---- | :---- |
| missing or conflicting configuration | `PROVIDER_CONFIG_MISSING` or `PROVIDER_CONFIG_INVALID` | no |
| unsupported or ambiguous route base | `PROVIDER_ROUTE_UNSUPPORTED` | no |
| `401` | `PROVIDER_UNAUTHORIZED` | no |
| `403` | `PROVIDER_FORBIDDEN` | no |
| `404` | `PROVIDER_NOT_FOUND` | no |
| `429` | `PROVIDER_RATE_LIMITED` | no |
| `500`–`599` | `PROVIDER_UNAVAILABLE` after the attempt budget | yes |
| network error | `PROVIDER_UNAVAILABLE` after the attempt budget | yes |
| malformed or mismatched response | `PROVIDER_BAD_RESPONSE` | no |
| provider-declared v2 failure or any other status, including `3xx` | `PROVIDER_ERROR` | no |

A valid `Retry-After` may project nonnegative integer `retry_after_ms` but never schedules an automatic retry. No vendor body is echoed and secrets remain redacted. The CLI projects the canonical provider code as its single LF-terminated `stderr` token; governed HTTP projects the same code through its canonical `error_v1` envelope.

## **B.3 Profiles/placeholders**

* **Timeout profile:** `default|small|long` (see §7.3.2)

| `max_attempts` | `backoff_kind` | `base_ms` | `ceiling_ms` | Schedule |
| ----: | :---- | ----: | ----: | :---- |
| 1 | `none` | 0 | 0 | one initial attempt; no retry |
| 2 | `fixed` | 250 | 250 | one retry after 250 ms |
| 2 | `fixed` | 500 | 500 | one retry after 500 ms |
| 3 | `exponential` | 250 | 500 | retries after 250 ms and 500 ms |
| 3 | `exponential` | 500 | 2000 | retries after 500 ms and 1000 ms; **default** |

`max_attempts` counts the initial request and accepts only integers `1`, `2`, or `3`. Zero and every unlisted tuple fail before I/O with `PROVIDER_CONFIG_INVALID`. No profile uses jitter. Only `network_error` and `5xx` retry, and the total operation budget is a hard ceiling.

---

# **Appendix C — CLI Parity Harness (usage recipes for AB↔BA, two-run) \[Required-Now\]**

**Purpose.** Repeatable recipes to prove **Reader↔CLI byte parity**, **AB↔BA identity**, and **two-run identity**, without exposing vendor calls. The harness is **dev-only** (`APP_ENV=dev`).

## **C.1 Reader↔CLI parity (success)**

1. **Run Reader (dev harness)** with fixture inputs; capture the **LF-terminated** body.  
     
2. **Run CLI.** Run `hdctl showcompat --dump-reader <path>` for the same inputs; capture the LF-terminated bytes written to `<path>`. Ordinary stdout remains compat JSON and is not a Reader-envelope parity input.  
     
3. **Hygiene pre-checks.** Validate both Reader bodies as UTF-8, BOM/ANSI-free, exactly one LF, six top-level keys, and `{id,band}` category items only.  
     
4. **Byte-compare.** The Reader response body and CLI reader-dump bytes MUST be identical, including `idempotence_hash` and the single LF.  
     
5. **Preimage re-check:** remove `idempotence_hash`, re-serialize the five-key preimage canonically, and confirm `sha256(preimage_bytes)` equals the published digest.

## **C.2 AB↔BA identity**

* Repeat **C.1** for **(A,B)** and **(B,A)**; the two outputs **MUST** match **bit-for-bit** (pair normalization in effect).

## **C.3 Two-run identity**

* Repeat the **same** command twice with identical inputs/environment; outputs **MUST** be **byte-identical** (including the single LF).

## **C.4 Hygiene**

* Use the **single presenter emitter** on both surfaces; **forbid** ad-hoc `json.dumps` or local “mini-emitters”.  
    
* Enforce schema & LF gates on every run; fail fast on any deviation.

# Appendix D — Evidence Routing (records-only) \[Required-Now\]

This appendix is a records-only locator and does not maintain an independent artifact inventory.

The Evidence Catalog, Human Evidence Index at `docs/evidence/INDEX.json`, its hash sentinel, Machine Evidence Mirror at `artifacts/evidence_index.jsonl`, governed artifact identities and paths, record schema, parity, checksums, and path-proof rules are single-homed in **HDE-Schemas & Artifacts**. PF05 may name an explicit PF05 proof anchor in its owning section only when required to define or verify a PF05-owned byte contract.

A path reference does not prove that an artifact exists, was generated, passed validation, or supports QA, OPS, checklist, closeout, or acceptance status.

---

# Appendix E — Channel Label Glossary (informative; non-contract)

**Purpose.** A copy/UX aid mapping the **36 canonical channel IDs** to conventional lineage **labels**. This appendix **does not** change payload bytes or schemas. **IDs are authoritative; labels are non-normative.** If channel identifiers ever appear publicly in a future version, they **must** be normalized per PF-Schemas §2.1 to **min→max, zero-padded `NN-NN`** before emission.

**Routing (titles-only):**  
Public payload contract → PF-Canon-HDE-CLI-API-Vendor-Ref main text; machine catalogs & identity rules → PF-Canon-HDE-Schemas and Artifacts; math/semantics → PF-Canon-HDE-Math-Spec.

---

### E.1 Canonical IDs → conventional labels

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

### E.2 Usage notes (copy discipline)

* Use labels for **UX copy only**; never substitute them for IDs in code, schemas, or evidence.  
* When referencing channels in QA or examples, include the **canonical ID** (e.g., “`10-20` Awakening”).  
* Circuit or tone references are **channel-scoped**, not gate-scoped (see PF-Math/PF-Mechanics).

### E.3 Evidence hooks (titles/paths only)

* `audit/gates/topology/orientation_demo.txt` — before/after normalization samples (`high-low` → `min-max` `NN-NN`).  
* (Optional) `fixtures/reference/channel_labels.snapshot.txt` — human-readable dump of the table above (non-contract).

---

