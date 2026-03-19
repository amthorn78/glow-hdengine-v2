## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC027   
Plan type: Live QA Plan / Runbook   
Execution venue: Codespaces   
Target environment: dev   
Plan revision: r6   
Date (UTC): 2026-03-15   
Operators (names-only): PO, QA agent

EVIDENCE\_ROOT: `audit/qa/hde-epic027`

For this runbook, `EVIDENCE_ROOT` is fixed to the canonical epic QA root above. Do not change it to a fresh run-specific path.

#### Canon precedence statement (required)

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set (explicit; stable references only)

Canon set (titles-only, names-only, no version numbers in prose):

* PF10 — HDE-Build Notes, §2.6) Audit Analysis HDE-EPIC027 Canon proof excerpt: “The only concrete canon delta supported by the allowlisted evidence is a PF14 mechanics correction for the dev writer conjunction endpoint method.” “No PF09 runnable-task delta is required from this audit pass.”  
    
* PF10 — HDE-Build Notes, §2.7) HDE-EPIC027 Implementation Report Canon proof excerpt: “HDE-EPIC027 was scoped as a Conjunction hardening/completion epic, not a contract-expansion epic” “the epic explicitly forbade new token names, new public contract surfaces, and embedded Live QA runbooks.”  
    
* PF27 — Canon Plan Templates, §1) Live QA Plan Canon proof excerpt: “PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.” “Live QA evidence MUST be organized only by check\_id under EPIC\_QA\_ROOT as current-state evidence.”  
    
* PF27 — Canon Plan Templates, §Step-log header schema expectations (minimum; required) Canon proof excerpt: “Header MUST include, at minimum:” “check\_id” “check\_name” “status”  
    
* PF19 — Canon-Glow-QA-Guide, §Workflow placement (Live QA runbooks; normative) Canon proof excerpt: “Live QA is a required Close Gate activity when an epic’s acceptance requires it.” “Functional Live QA is mandatory for functional changes”  
    
* PF19 — Canon-Glow-QA-Guide, §3.4.3 Evidence layout: current-state first (new posture) Canon proof excerpt: “The canonical current-state QA root is `audit/qa/<epic-id>/`.” “Per-run nesting is not canonical and must not be the required evidence surface.”  
    
* PF19 — Canon-Glow-QA-Guide, §3.4.6 Step-level Deliverables (no screen-only acceptance) Canon proof excerpt: “Every Live QA step must produce the deliverables declared for that step.” “Primary step evidence must be a path-addressable artifact, not a screen-only observation.”  
    
* PF19 — Canon-Glow-QA-Guide, §3.4.8 Rails posture for manual Live QA (EPIC017 example; generalized rule) Canon proof excerpt: “When manual Live QA requires runtime proof, open the minimum rails required for that proof and capture the exact rails state in the step evidence.” “Entrypoint existence must be preflighted before the operator treats a step as runnable.”  
    
* PF23 — Reality Audits, §Intent & scope \[Required-Now\] Canon proof excerpt: “Agents may read these audits as context when planning future work, but they do not schedule, trigger, or satisfy them.”  
    
* PF05 — HDE-CLI-API-Vendor-Ref, §0.2 Scope \[Required-Now\] Canon proof excerpt: “Endpoint Catalog (JSON success): proof surface (A7).” “A7 transport proofs must run on a §5.6 Endpoint Catalog (JSON success) route” “Internal-ops `/internal/version` is excluded”  
    
* PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required-Now\] Canon proof excerpt: “The Endpoint Catalog is the single machine-readable inventory of success routes.” “A7 proofs run only on cataloged JSON success routes.”  
    
* PF12 — HDE-Schemas-and-Artifacts, §Human Evidence Index (single home) Canon proof excerpt: “Path: docs/evidence/INDEX.json” “Must maintain 1:1 parity with the Machine Evidence Mirror”  
    
* PF12 — HDE-Schemas-and-Artifacts, §Machine Evidence Mirror (governed here) Canon proof excerpt: “Path: artifacts/evidence\_index.jsonl.” “Exactly one mirror file must exist at artifacts/evidence\_index.jsonl.”

### Scope statement

This plan evaluates the following in-scope surfaces / checks:

* D0 — Discovery, current-state evidence bootstrap, and manifest bootstrap  
* PO-001 — Dev harness surface and infra-wiring coherence  
* PO-002 — Internal compat identity proof discoverability  
* PO-003 — CLI deterministic shared-emitter posture  
* PO-004 — CLI installability, entrypoint, help, argument, and conformance proof  
* PO-005 — Reader success-route A7 proof family on cataloged JSON success routes  
* PO-006 — Writer-style behavior, readback parity, and non-A7 separation  
* PO-007 — Single-emitter, canonical-JSON, and evidence-ledger coherence  
* PO-008 — Acceptance-ledger and closeout truthfulness  
* PO-009 — No new public contract surface and no new acceptance vocabulary  
* PO-010 — Runtime functional proof posture across changed runtime surfaces

This plan explicitly excludes:

* Any new public contract surface  
* Any new acceptance token name  
* Any PF23 capture artifact or PF23 execution step  
* Any `HDE_BASE_URL` or prod-like runtime step, because scoped runtime wiring for that input is not audit-proven  
* Any use of `/internal/dev/sampler` as a cataloged A7 proof target  
* Any PF14 mechanics drain itself as a runnable implementation slice  
* Any per-run evidence root, timestamped run directory, or operator-selected fresh run folder

#### PF10 overrides / conflicts (if any)

* PF10 Addendum 2.6) Audit Analysis HDE-EPIC027 → the only live canon delta is the PF14 dev writer conjunction endpoint-method correction, and no new PF09 runnable-task delta is required → impacted references: PF10, PF27, PF19, PF05  
* PF10 Addendum 2.7) HDE-EPIC027 Implementation Report → this runbook must preserve hardening/completion scope only and must not introduce new public contract surfaces, new acceptance vocabulary, or an expanded QA scope → impacted references: PF10, PF27, PF19, PF05

---

### PF23 anchors

**Planning-time consult for Live QA planning (normative).**

* PF23 was consulted read-only for repo-reality framing of the Dev HTTP Harness, internal compat surface, CLI operator surface, Reader success-route proof family, writer surface family, and evidence-ledger topology.  
* No PF23 output is a required deliverable in this runbook.  
* No PF23 command is an execution step in this runbook.

### Environment and rails posture

#### Determinism pins (canonical pins only)

When producing governed bytes, use:

* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`

#### Rails posture (explicit)

Default rails for this runbook:

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `APP_ENV=dev`

If rails change by check:

* `po-005` → `HDE_WRITE_A7_PROOFS=1` → needed to emit the Reader A7 proof family while keeping closed rails  
* No `HDE_BASE_URL`\-driven step is allowed in this runbook  
* No implicit open-rails behavior is allowed anywhere in this runbook

### PO inputs needed

Required external inputs for this runbook:

* None

Optional execution inputs:

* None

If an operator tries to broaden this runbook to a prod-like or base-URL-driven verification path, that broadened path is out of scope for this document and the affected step is `TOOLING_BLOCKED`.

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Canonical epic QA root:

* `audit/qa/hde-epic027/`

This runbook uses the fixed current-state root above and does not use any per-run nesting.

#### Recommended canonical layout (default for new plans)

Use this layout for this run:

* `audit/qa/hde-epic027/00_meta/`  
* `audit/qa/hde-epic027/checks/d0_discovery/`  
* `audit/qa/hde-epic027/checks/po-001/`  
* `audit/qa/hde-epic027/checks/po-002/`  
* `audit/qa/hde-epic027/checks/po-003/`  
* `audit/qa/hde-epic027/checks/po-004/`  
* `audit/qa/hde-epic027/checks/po-005/`  
* `audit/qa/hde-epic027/checks/po-006/`  
* `audit/qa/hde-epic027/checks/po-007/`  
* `audit/qa/hde-epic027/checks/po-008/`  
* `audit/qa/hde-epic027/checks/po-009/`  
* `audit/qa/hde-epic027/checks/po-010/`

Required current-state artifacts for this runbook:

* `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`

These two files are QA-created outputs for this runbook. They are required by canon, but current audit evidence says they are not currently present or ledger-bound for EPIC027, so any check that depends on their existing index or mirror coverage is `TOOLING_BLOCKED` until that gap is resolved.

#### Step-log header schema expectations (minimum; required)

Every `primary.log` in this runbook must begin with a single-line JSON header containing at least:

* `schema_version`  
* `timestamp_utc`  
* `check_id`  
* `check_name`  
* `status`  
* `fail_status`  
* `command`  
* `command_provenance`  
* `evidence_artifacts`  
* `captured_env`  
* `pf_refs`  
* `intended_tokens`  
* `claimed_tokens`

For this runbook:

* `pf_refs` must use titles only  
* `captured_env` must include only canon-defined environment variable names  
* every step, including `TOOLING_BLOCKED`, must still produce `primary.log`  
* every executed step must have an entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json`

### Mandatory Step-0 artifacts

#### Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)

Required artifact for this run:

* `audit/qa/hde-epic027/00_meta/doc_deltas.md`

This file is QA-created in this runbook and records any observed canon-vs-repo or plan-vs-repo deltas from this run.

#### Step-0C — Prod handshake (identity-only) when target is prod-like

Not used in this runbook.

Reason: this runbook’s target environment is `dev`, and scoped `HDE_BASE_URL` runtime wiring is not audit-proven for EPIC027.

### Runbook Check Matrix

* d0\_discovery — discovery and evidence bootstrap — non-token evidence step — expected result: PASS  
* `po-001` — dev harness coherence — tokenless proof step — expected result: `PASS`  
* `po-002` — compat identity proof discoverability — tokenless proof step — expected result: `PASS`  
* `po-003` — CLI deterministic shared-emitter posture — intended tokens: `JSON_CANONICAL_CHECK_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK` — expected result: `PASS`  
* `po-004` — CLI installability and conformance proof — intended tokens: `CLI_READER_PARITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK` — expected result: `PASS`  
* `po-005` — Reader A7 proof family — intended tokens: `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`, `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK` — expected result: `PASS`  
* `po-006` — writer behavior and readback parity — intended tokens: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK` — expected result: `PASS`  
* `po-007` — single-emitter and evidence-ledger coherence — intended tokens: `JSON_CANONICAL_CHECK_OK`, `ENV_RAILS_POLICY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK` — expected result: `TOOLING_BLOCKED` unless the missing EPIC027 step-log manifest coverage gap is first resolved  
* `po-008` — closeout truthfulness — intended tokens: same as `po-007` where applicable — expected result: `TOOLING_BLOCKED` unless `po-007` reaches `PASS`  
* `po-009` — no new public surface and no new acceptance vocabulary — tokenless policy proof step — expected result: `PASS`  
* `po-010` — runtime functional proof posture — tokenless synthesis step — expected result: `PASS` if same-run runtime proofs exist across the changed runtime surfaces

#### Token coverage and evidence binding (required)

This runbook claims only canonical token names already staged in current EPIC027 closeout material and current canon. It does not claim any CLI-installability token names that are not explicitly canon-backed in the current accepted token set.

Every token-bearing check in this runbook must list its intended tokens in the step-log header and must list claimed tokens only after the step has actually produced the required governed evidence.

### Check Blocks

#### Embedded harness checks (pattern; use when no standalone script exists)

For this runbook, when no standalone script is audit-proven for a proof obligation, use one of these audit-proven patterns only:

* `python -m pytest -q <audit-proven test path>`  
* `rg -n <pattern> <audit-proven repo paths>`  
* `python <audit-proven repo script>`

Do not invent any helper script, alternate test path, wrapper module, or route alias.

#### Canon check clarifications (addenda-driven; locked)

* Treat `/internal/dev/sampler` catalog discoverability as unresolved. Do not use it as a PASS target in this runbook.  
* Do not use `HDE_BASE_URL` in this runbook. The current audit says that scoped runtime wiring for that variable is unproven for EPIC027.  
* For the dev writer conjunction surface, do not infer an HTTP method from stale mechanics prose. Prove behavior via audit-proven runtime tests and audit-proven evidence rows only.  
* `audit/qa/hde-epic027/qa_step_logs_manifest.json` and its sibling path proof are required QA-created current-state outputs for this runbook, but current EPIC027 mirror and index coverage for that manifest is audit-blocked.

  #### **CHECK d0\_discovery: d0 — Discovery, current-state evidence bootstrap, and manifest bootstrap**

Goal: establish the fixed current-state QA root, capture initial repo-visible proof posture for this run, and create the canonical EPIC027 step-log manifest required by the runbook.

Guide-derived obligation:

SOURCE EXCERPT (verbatim):  
 Proof obligation:  
 Epic-close verification includes runtime functional proof on the changed runtime surfaces; artifact-only close is not sufficient.

SOURCE EXCERPT (verbatim):  
 Notes:  
 This defines the close-proof posture only; it does not authorize embedding a runbook here.

Preconditions:

Codespaces terminal is at repo root

python is available

bash is available

PO actions:

Create the current-state EPIC027 QA directories.

Capture the current tree, env-pins checker behavior, and CLI top-level help into primary.log.

Create the EPIC027 step-log manifest and sibling path proof.

Create the run-level doc-delta ledger file.

SOURCE EXCERPT (verbatim):  
 Path:  
 ci/checks/check\_env\_pins.sh  
 Category:  
 Rails enforcement  
 Proof:  
 ci/checks/check\_env\_pins.sh: runs determinism env checker with \--check-log.

SOURCE EXCERPT (verbatim):  
 Path:  
 scripts/hdctl.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 if name \== "main":  
 sys.exit(main())

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/d0_discovery/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/d0_discovery/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/d0_discovery/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/d0_discovery/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

primary.log exists and contains a tree snapshot, env-pins checker output, and CLI help output

the manifest file exists at the canonical EPIC027 path

the sibling path-proof file exists

doc\_deltas.md exists under 00\_meta

Required deliverables:

audit/qa/hde-epic027/checks/d0\_discovery/primary.log

audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

audit/qa/hde-epic027/00\_meta/doc\_deltas.md

PASS criteria tied to deliverables:

all four deliverables exist

qa\_step\_logs\_manifest.json includes an entry for d0\_discovery

the path proof names the exact manifest path and its current SHA-256

FAIL criteria tied to deliverables plus what to capture:

* if any deliverable is missing, classify `FAIL_TOOLING` and capture the exact missing path in `primary.log`

  #### **CHECK po-001: PO-001**

Goal: prove that the dev-only conjunction harness remains the single non-public local and QA validation surface and that its remaining infra-wiring posture is coherent.

SOURCE EXCERPT (verbatim):  
 PO-001

Proof obligation:  
 The dev-only conjunction harness remains the single non-public local and QA validation surface, and its remaining infra-wiring posture is coherent.

SOURCE EXCERPT (verbatim):  
 Path:  
 adapter/http\_reader.py  
 Category:  
 Endpoint/surface  
 Proof:  
 @bp.route("/internal/dev/sampler", methods=\["POST"\], provide\_automatic\_options=False)  
 @bp.get("/dev/sampler/conjunction")  
 @bp.get("/dev/reader/conjunction")  
 @bp.get("/dev/writer/conjunction")

SOURCE EXCERPT (verbatim):  
 Path:  
 adapter/factory.py  
 Category:  
 Endpoint/surface  
 Proof:  
 app.register\_blueprint(bp, url\_prefix="")  
 app.register\_blueprint(compat\_blueprint)

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_dev\_conjunction\_http.py  
 Category:  
 Endpoint/surface  
 Proof:  
 assert payload\_one\["writer"\]\["writer\_route\_id"\] \== "dev.writer.conjunction.v1"

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_endpoint\_catalog.py  
 Category:  
 Endpoint/surface  
 Proof:  
 tests/http/test\_endpoint\_catalog.py

Preconditions:

* `d0_discovery` passed

* `audit/qa/hde-epic027/qa_step_logs_manifest.json` exists

PO actions:

1. Capture route and blueprint wiring for the conjunction dev surfaces.

2. Run the dev conjunction HTTP test.

3. Run the endpoint catalog test.

4. Write the result to `primary.log`.

5. Update the EPIC027 manifest entry for `po-001`.

SOURCE EXCERPT (verbatim):  
 Path:  
 engine/http/compat\_handler.py  
 Category:  
 Endpoint/surface  
 Proof:  
 compat\_blueprint \= Blueprint("compat", name, url\_prefix="/api/compat/v1")  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_dev\_conjunction\_http.py  
 Category:  
 Endpoint/surface  
 Proof:  
 assert payload\_one\["writer"\]\["writer\_route\_id"\] \== "dev.writer.conjunction.v1"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_endpoint\_catalog.py  
 Category:  
 Endpoint/surface  
 Proof:  
 tests/http/test\_endpoint\_catalog.py

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-001/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-001/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-001/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-001/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* the route inventory shows the conjunction dev trio under the adapter

* the route inventory shows the compat blueprint mount and app registration

* `tests/http/test_dev_conjunction_http.py` passes

* `tests/http/test_endpoint_catalog.py` passes

Required deliverables:

audit/qa/hde-epic027/checks/po-001/route\_inventory.txt

audit/qa/hde-epic027/checks/po-001/dev\_conjunction\_http.txt

audit/qa/hde-epic027/checks/po-001/endpoint\_catalog.txt

audit/qa/hde-epic027/checks/po-001/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* route inventory proves the dev conjunction trio

* both tests pass

FAIL criteria tied to deliverables plus what to capture:

* if route inventory is missing the conjunction dev trio, classify `FAIL_BEHAVIOR`

* if either test fails, classify `FAIL_BEHAVIOR`

* if a test cannot start, classify `FAIL_TOOLING`

  #### **CHECK po-002: PO-002**

Goal: prove that the internal conjunction compat surface has an explicit stable identity proof and that the proof is governed and discoverable.

SOURCE EXCERPT (verbatim):  
 PO-002

Proof obligation:  
 The internal conjunction compat surface produces an explicit stable identity proof and that proof is governed and discoverable.

SOURCE EXCERPT (verbatim):  
 engine/http/compat\_handler.py: compat blueprint is mounted at /api/compat/v1 and enforces prod POST refusal branch.

SOURCE EXCERPT (verbatim):  
 tools/evidence/update\_evidence\_index.py: contains EPIC027 token matrix and viability paths, plus conjunction identity/writer artifacts.

SOURCE EXCERPT (verbatim):  
 artifacts/evidence\_index.jsonl: contains artifact keys for compat.conjunction.identity\_hash, conjunction writer artifacts, A7 proof family, and EPIC027 token/viability entries with path proofs.

PO actions:

1. Capture compat surface wiring.

2. Capture identity-proof discoverability from the evidence updater and machine mirror.

3. Write the result to `primary.log`.

4. Update the EPIC027 manifest entry for `po-002`.

SOURCE EXCERPT (verbatim):  
 Path:  
 engine/http/compat\_handler.py  
 Category:  
 Endpoint/surface  
 Proof:  
 compat\_blueprint \= Blueprint("compat", name, url\_prefix="/api/compat/v1")  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tools/evidence/update\_evidence\_index.py  
 Category:  
 Script/runbook  
 Proof:  
 "discovered\_physical\_path": "audit/qa/hde-epic027/token\_evidence\_matrix.md",  
 Where found:  
 rg \-n "hde-epic027|token\_evidence\_matrix|acceptance\_map\_viability" tools/evidence/update\_evidence\_index.py

SOURCE EXCERPT (verbatim):  
 Evidence pointers

artifacts/evidence\_index.jsonl: contains artifact keys for compat.conjunction.identity\_hash, conjunction writer artifacts, A7 proof family, and EPIC027 token/viability entries with path proofs.

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-002/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-002/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-002/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-002/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* compat blueprint is mounted at `/api/compat/v1`

* machine-mirror or updater output exposes `compat.conjunction.identity_hash`

Required deliverables:

audit/qa/hde-epic027/checks/po-002/compat\_surface.txt

audit/qa/hde-epic027/checks/po-002/compat\_identity\_discovery.txt

audit/qa/hde-epic027/checks/po-002/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* compat surface is mounted

* identity-proof discoverability is explicit in the updater or mirror output

FAIL criteria tied to deliverables plus what to capture:

* if `/api/compat/v1` mount proof is absent, classify `FAIL_BEHAVIOR`

* if no identity-proof discoverability line is found, classify `FAIL_BEHAVIOR`

  #### **CHECK po-003: PO-003**

Goal: prove that the conjunction CLI remains deterministic and continues to emit through the shared public-emission path rather than ad-hoc serialization.

SOURCE EXCERPT (verbatim):  
 PO-003

Proof obligation:  
 The conjunction CLI surface remains deterministic and continues to use the shared public-emission path rather than ad-hoc serialization.

SOURCE EXCERPT (verbatim):  
 Path:  
 engine/cli/main.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 if not payload.endswith(b"\\n"):  
 raise CliError("STDOUT\_MISSING\_LF")  
 if b"\\r\\n" in payload:  
 raise CliError("STDOUT\_CRLF")  
 \_emit\_stdout\_bytes(emitter.emit\_public(conjunction\_payload))

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_showcompat\_parity\_and\_identity.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 def \_run\_showcompat(payload: dict\[str, object\], extra\_args: list\[str\] | None \= None, env: dict\[str, str\] | None \= None):

PO actions:

1. Capture the emitter and stdout guard proof from `engine/cli/main.py`.

2. Run the conjunction parity and identity CLI test.

3. Capture the `showcompat --help` surface.

4. Write the result to `primary.log`.

5. Update the EPIC027 manifest entry for `po-003`.

SOURCE EXCERPT (verbatim):  
 Path:  
 engine/cli/main.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 \_emit\_stdout\_bytes(emitter.emit\_public(conjunction\_payload))  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_showcompat\_parity\_and\_identity.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 def \_run\_showcompat(payload: dict\[str, object\], extra\_args: list\[str\] | None \= None, env: dict\[str, str\] | None \= None):  
 SOURCE EXCERPT (verbatim):  
 Path:  
 scripts/hdctl.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 if **name** \== "**main**":  
 sys.exit(main())

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-003/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-003/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-003/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-003/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* emitter proof shows shared `emit_public`

* parity and identity test passes

* `showcompat --help` runs successfully

Required deliverables:

audit/qa/hde-epic027/checks/po-003/cli\_emitter\_proof.txt

audit/qa/hde-epic027/checks/po-003/showcompat\_parity.txt

audit/qa/hde-epic027/checks/po-003/showcompat\_help.txt

audit/qa/hde-epic027/checks/po-003/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* emitter proof shows `emit_public`

* parity test passes

* help command returns successfully

FAIL criteria tied to deliverables plus what to capture:

* if emitter proof is absent, classify `FAIL_BEHAVIOR`

* if parity test fails, classify `FAIL_BEHAVIOR`

* if help invocation fails to start, classify `FAIL_TOOLING`

  #### **CHECK po-004: PO-004**

Goal: prove that the operator-facing CLI is explicitly covered for installability, entrypoint behavior, help and argument handling, deterministic pair behavior, and current contract conformance.

SOURCE EXCERPT (verbatim):  
 PO-004

Proof obligation:  
 The operator-facing CLI surface is explicitly covered for installability, entrypoint behavior, help and argument handling, deterministic pair behavior, and current contract conformance.

SOURCE EXCERPT (verbatim):  
 Path:  
 pyproject.toml  
 Category:  
 CLI entrypoint/help  
 Proof:  
 \[project.scripts\]  
 hdctl \= "engine.cli.main:cli"

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_cli\_install\_help.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 subprocess.run(\[sys.executable, "-m", "pip", "install", "-e", "."\], check=True, capture\_output=True)

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_bg\_resolve.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 tests/cli/test\_bg\_resolve.py

PO actions:

1. Prove the pyproject entrypoint binding.

2. Run the install-help test.

3. Run the bg-resolve test.

4. Capture `bg:resolve --help`.

5. Write the result to `primary.log`.

6. Update the EPIC027 manifest entry for `po-004`.

SOURCE EXCERPT (verbatim):  
 Path:  
 pyproject.toml  
 Category:  
 CLI entrypoint/help  
 Proof:  
 hdctl \= "engine.cli.main:cli"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_cli\_install\_help.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 subprocess.run(\[sys.executable, "-m", "pip", "install", "-e", "."\], check=True, capture\_output=True)  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_bg\_resolve.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 tests/cli/test\_bg\_resolve.py  
 SOURCE EXCERPT (verbatim):  
 Path:  
 scripts/hdctl.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 if **name** \== "**main**":  
 sys.exit(main())

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-004/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-004/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-004/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-004/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* pyproject entrypoint binding exists

* install-help test passes

* bg-resolve test passes

* `bg:resolve --help` runs successfully

Required deliverables:

audit/qa/hde-epic027/checks/po-004/entrypoint\_proof.txt

audit/qa/hde-epic027/checks/po-004/cli\_install\_help.txt

audit/qa/hde-epic027/checks/po-004/bg\_resolve\_test.txt

audit/qa/hde-epic027/checks/po-004/bg\_resolve\_help.txt

audit/qa/hde-epic027/checks/po-004/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* install-help and bg-resolve tests pass

* help invocation succeeds

* entrypoint binding is explicit in `pyproject.toml`

FAIL criteria tied to deliverables plus what to capture:

* if `pyproject.toml` entrypoint proof is absent, classify `FAIL_BEHAVIOR`

* if either test fails, classify `FAIL_BEHAVIOR`

* if help invocation cannot start, classify `FAIL_TOOLING`

  #### **CHECK po-005: PO-005**

Goal: prove that the Reader success-route validation remains bound to the cataloged JSON success-route family and demonstrates required transport and environment-gating behavior for that family.

SOURCE EXCERPT (verbatim):  
 PO-005

Proof obligation:  
 The Reader success-route proof remains bound to the cataloged JSON success-route family and demonstrates the required transport and environment-gating behavior for that family.

SOURCE EXCERPT (verbatim):  
 docs/ENDPOINTS\_CATALOG.json: includes /api/compat/v1, /reader, /internal/version, /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction with env gates and classifications.

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_reader\_a7\_transport.py  
 Category:  
 Rails enforcement  
 Proof:  
 write\_proofs \= os.environ.get("HDE\_WRITE\_A7\_PROOFS") \== "1"

PO actions:

1. Run the Reader A7 transport test under closed rails and deterministic pins, with proof writing enabled.

2. Capture cataloged success-route inventory from the endpoint catalogs.

3. Write the result to `primary.log`.

4. Update the EPIC027 manifest entry for `po-005`.

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_reader\_a7\_transport.py  
 Category:  
 Rails enforcement  
 Proof:  
 write\_proofs \= os.environ.get("HDE\_WRITE\_A7\_PROOFS") \== "1"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 docs/ENDPOINTS\_CATALOG.json  
 Category:  
 Ledger/index  
 Proof:  
 docs/ENDPOINTS\_CATALOG.json

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-005/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-005/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-005/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-005/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* Reader A7 transport test passes

* endpoint-catalog output includes `/reader`

* proof remains tied to cataloged JSON success routes only

Required deliverables:

audit/qa/hde-epic027/checks/po-005/reader\_a7\_transport.txt

audit/qa/hde-epic027/checks/po-005/catalog\_routes.txt

audit/qa/hde-epic027/checks/po-005/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* A7 transport test passes

* the catalog route inventory includes `/reader`

* no non-cataloged success-route proof target is treated as an A7 PASS target in this step

FAIL criteria tied to deliverables plus what to capture:

* if the transport test fails, classify `FAIL_BEHAVIOR`

* if `/reader` is absent from the catalog inventory, classify `FAIL_BEHAVIOR`

  #### **CHECK po-006: PO-006**

Goal: prove that the conjunction writer surface preserves writer-style behavior, demonstrates readback parity, and remains outside the A7 proof family.

SOURCE EXCERPT (verbatim):  
 PO-006

Proof obligation:  
 The conjunction writer surface preserves its writer-style behavior, demonstrates idempotent readback parity, and remains outside the A7 proof family.

SOURCE EXCERPT (verbatim):  
 Notes:  
 PF10 still records one mechanics-text mismatch for the dev writer conjunction endpoint method, but it treats that as a canon drain issue rather than as a new runnable implementation slice.

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_dev\_conjunction\_http.py  
 Category:  
 Endpoint/surface  
 Proof:  
 assert payload\_one\["writer"\]\["writer\_route\_id"\] \== "dev.writer.conjunction.v1"

SOURCE EXCERPT (verbatim):  
 artifacts/evidence\_index.jsonl: contains artifact keys for compat.conjunction.identity\_hash, conjunction writer artifacts, A7 proof family, and EPIC027 token/viability entries with path proofs.

PO actions:

1. Run the dev conjunction HTTP test to prove writer-route behavior and readback expectations.

2. Capture the machine-mirror rows for the writer artifact family.

3. Write the result to `primary.log`.

4. Update the EPIC027 manifest entry for `po-006`.

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_dev\_conjunction\_http.py  
 Category:  
 Endpoint/surface  
 Proof:  
 assert payload\_one\["writer"\]\["writer\_route\_id"\] \== "dev.writer.conjunction.v1"  
 SOURCE EXCERPT (verbatim):  
 Evidence pointers

artifacts/evidence\_index.jsonl: contains artifact keys for compat.conjunction.identity\_hash, conjunction writer artifacts, A7 proof family, and EPIC027 token/viability entries with path proofs.

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-006/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-006/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-006/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-006/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* dev conjunction HTTP test passes

* writer artifact rows are present in the machine mirror

* this step does not treat the writer family as an A7 proof family

Required deliverables:

audit/qa/hde-epic027/checks/po-006/dev\_conjunction\_http.txt

audit/qa/hde-epic027/checks/po-006/writer\_index\_rows.txt

audit/qa/hde-epic027/checks/po-006/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* the dev conjunction HTTP test passes

* writer artifact rows are discoverable in the mirror

FAIL criteria tied to deliverables plus what to capture:

* if the dev conjunction HTTP test fails, classify `FAIL_BEHAVIOR`

* if writer artifact rows are absent, classify `FAIL_BEHAVIOR`

  #### **CHECK po-007: PO-007**

Goal: prove that all conjunction-touched surfaces participate in the single-emitter, canonical-JSON, same-change evidence discipline and that the human and machine evidence ledgers remain coherent.

SOURCE EXCERPT (verbatim):  
 PO-007

Proof obligation:  
 All conjunction-touched surfaces participate in the single-emitter, canonical-JSON, same-change evidence discipline, and the human and machine evidence ledgers remain coherent.

SOURCE EXCERPT (verbatim):  
 EPIC027 step-log manifest files are unproven on disk (missing audit/qa/hde-epic027/qa\_step\_logs\_manifest.json and sibling path-proof), blocking deterministic manifest-binding steps

SOURCE EXCERPT (verbatim):  
 EPIC027 mirror/index artifact-key coverage for qa-step manifest is missing (no epic027.qa\_step\_logs\_manifest match in index/mirror/updater queries), blocking ledger-coherent plan output mapping

RERUN AUDIT REQUIRED for: `audit/qa/hde-epic027/qa_step_logs_manifest.json`

PO actions:

1. Run the canonical evidence-index, orientation, path-validation, LF, and mirror-schema checks.

2. Explicitly test whether EPIC027 manifest coverage is present in the updater, human index, and machine mirror.

3. If manifest coverage remains absent, classify the step `TOOLING_BLOCKED` and do not over-claim ledger coherence.

SOURCE EXCERPT (verbatim):  
 Path:  
 tools/evidence/update\_evidence\_index.py  
 Category:  
 Script/runbook  
 Proof:  
 "discovered\_physical\_path": "audit/qa/hde-epic027/token\_evidence\_matrix.md",

SOURCE EXCERPT (verbatim):  
 Path:  
 tools/evidence/orientation\_demo.py  
 Category:  
 Script/runbook  
 Proof:  
 ORIENTATION\_PATH \= ROOT / "audit" / "gates" / "topology" / "orientation\_demo.txt"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tools/evidence/validate\_evidence\_paths.py  
 Category:  
 Script/runbook  
 Proof:  
 ensure\_determinism\_env(apply=True)  
 SOURCE EXCERPT (verbatim):  
 Path:  
 tools/evidence/check\_lf\_endings.py  
 Category:  
 Script/runbook  
 Proof:  
 script \= ROOT / "ci" / "checks" / "check\_final\_lf.sh"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 ci/checks/check\_mirror\_schema.sh  
 Category:  
 Script/runbook  
 Proof:  
 index\_path \= Path("artifacts/evidence\_index.jsonl")  
 SOURCE EXCERPT (verbatim):  
 Negative-claim commands used: rg \-n "epic027.qa\_step\_logs\_manifest|qa\_step\_logs\_manifest" docs/evidence/INDEX.json artifacts/evidence\_index.jsonl tools/evidence/update\_evidence\_index.py

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-007/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-007/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-007/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-007/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* all canonical evidence-discipline jobs succeed

* the manifest lookup either proves EPIC027 qa-step manifest coverage or confirms the current audit gap

Required deliverables:

audit/qa/hde-epic027/checks/po-007/update\_evidence\_index\_write.txt

audit/qa/hde-epic027/checks/po-007/update\_evidence\_index\_check.txt

audit/qa/hde-epic027/checks/po-007/orientation\_demo\_write.txt

audit/qa/hde-epic027/checks/po-007/orientation\_demo\_check.txt

audit/qa/hde-epic027/checks/po-007/validate\_evidence\_paths.txt

audit/qa/hde-epic027/checks/po-007/check\_lf\_endings.txt

audit/qa/hde-epic027/checks/po-007/check\_mirror\_schema.txt

audit/qa/hde-epic027/checks/po-007/qa\_step\_manifest\_lookup.txt

audit/qa/hde-epic027/checks/po-007/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all evidence-discipline jobs pass

* `qa_step_manifest_lookup.txt` proves EPIC027 manifest coverage in the updater and ledgers

FAIL criteria tied to deliverables plus what to capture:

* if any evidence-discipline job fails, classify `FAIL_BEHAVIOR`

* if any job cannot start, classify `FAIL_TOOLING`

TOOLING\_BLOCKED criteria tied to deliverables plus what to capture:

* if all evidence-discipline jobs pass but `qa_step_manifest_lookup.txt` still shows no EPIC027 qa-step manifest coverage, classify `TOOLING_BLOCKED`

* record the two blocked excerpts above in `primary.log`

* do not claim ledger coherence for the EPIC027 qa-step manifest in this run

  #### **CHECK po-008: PO-008**

Goal: prove that the epic-close acceptance ledgers and closeout records explicitly bind canonical acceptance claims to actual proof and remain truthful to what was really executed.

SOURCE EXCERPT (verbatim):  
 PO-008

Proof obligation:  
 The epic-close acceptance ledgers and closeout records explicitly bind canonical acceptance claims to actual proof and remain truthful to what was really executed.

SOURCE EXCERPT (verbatim):  
 EPIC027 step-log manifest files are unproven on disk (missing audit/qa/hde-epic027/qa\_step\_logs\_manifest.json and sibling path-proof), blocking deterministic manifest-binding steps

SOURCE EXCERPT (verbatim):  
 EPIC027 mirror/index artifact-key coverage for qa-step manifest is missing (no epic027.qa\_step\_logs\_manifest match in index/mirror/updater queries), blocking ledger-coherent plan output mapping

RERUN AUDIT REQUIRED for: `audit/qa/hde-epic027/qa_step_logs_manifest.json`

PO actions:

1. Run the EPIC027 close-pack generator under closed rails and deterministic pins.

2. Capture whether the close report and manifest bind this run’s actual QA gate logs.

3. If `po-007` is blocked on missing manifest coverage, classify this step `TOOLING_BLOCKED` rather than over-claiming truthful closeout binding.

SOURCE EXCERPT (verbatim):  
 Path:  
 tools/qa/generate\_epic027\_close\_pack.py  
 Category:  
 Script/runbook  
 Proof:  
 EPIC\_ID \= "HDE-EPIC027"  
 SOURCE EXCERPT (verbatim):  
 Path:  
 audit/EPIC-027\_MANIFEST.json  
 Category:  
 Evidence root  
 Proof:  
 {"captured\_at\_utc":"2026-03-14T03:07:52Z","closeout\_dir":"audit/qa/hde-epic027","epic\_id":"HDE-EPIC027"...}  
 Where found:  
 rg \-n "hde-epic027" audit/EPIC-027\_MANIFEST.json

SOURCE EXCERPT (verbatim):  
 Path:  
 audit/EPIC-027\_close\_report.md  
 Category:  
 Evidence root  
 Proof:  
 audit/qa/hde-epic027/token\_evidence\_matrix.md  
 Where found:  
 rg \-n "hde-epic027|token\_evidence\_matrix" audit/EPIC-027\_close\_report.md  
 SOURCE EXCERPT (verbatim):  
 Negative-claim commands used: rg \-n "epic027.qa\_step\_logs\_manifest|qa\_step\_logs\_manifest" docs/evidence/INDEX.json artifacts/evidence\_index.jsonl tools/evidence/update\_evidence\_index.py

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-008/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-008/primary.log`

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-008/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-008/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* the close-pack generator runs

* close report and manifest bind to the EPIC027 QA root and canonical ledger files

* no truthfulness claim is made for a manifest family that remains unindexed or unmirrored

Required deliverables:

audit/qa/hde-epic027/checks/po-008/generate\_close\_pack.txt

audit/qa/hde-epic027/checks/po-008/close\_pack\_bindings.txt

audit/qa/hde-epic027/checks/po-008/qa\_step\_manifest\_lookup.txt

audit/qa/hde-epic027/checks/po-008/primary.log

refreshed audit/EPIC-027\_close\_report.md

conditional refreshed audit/EPIC-027\_MANIFEST.json

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* the close-pack generator runs

* close-pack bindings point to the EPIC027 QA root and current canonical ledger files

* the EPIC027 qa-step manifest is ledger-bound and not merely present on disk

FAIL criteria tied to deliverables plus what to capture:

* if the close-pack generator fails, classify `FAIL_BEHAVIOR`

* if close-pack bindings omit the canonical EPIC027 ledgers, classify `FAIL_BEHAVIOR`

TOOLING\_BLOCKED criteria tied to deliverables plus what to capture:

* if `po-007` remains blocked on qa-step manifest coverage, classify `TOOLING_BLOCKED`

* record the blocked excerpts above in `primary.log`

* do not claim truthful closeout binding for the qa-step manifest

  #### **CHECK po-009: PO-009**

Goal: prove that EPIC027 introduces no new public contract surface and no new acceptance vocabulary as part of completion proof.

SOURCE EXCERPT (verbatim):  
 PO-009

Proof obligation:  
 The epic introduces no new public contract surface and no new acceptance vocabulary as part of proving the conjunction work complete.

SOURCE EXCERPT (verbatim):

* HDE-EPIC027 is a conjunction hardening and completion pass, not a contract-expansion pass.

* The public Reader covenant remains unchanged: bands-only, numeric-free, and still routed through the shared public-emission posture.

PO actions:

1. Inventory the cataloged route family visible to this runbook.

2. Inventory the canonical token names already bound in the current EPIC027 close artifacts.

3. Write the result to `primary.log`.

4. Update the EPIC027 manifest entry for `po-009`.

SOURCE EXCERPT (verbatim):  
 docs/ENDPOINTS\_CATALOG.json: includes /api/compat/v1, /reader, /internal/version, /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction with env gates and classifications.  
 SOURCE EXCERPT (verbatim):  
 Path:  
 audit/qa/hde-epic027/token\_evidence\_matrix.md  
 Category:  
 Evidence root  
 Proof:  
 audit/qa/hde-epic027/token\_evidence\_matrix.md

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-009/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-009/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-009/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-009/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* route inventory remains within the known EPIC027 family

* token inventory uses only the current canonical EPIC027 token family

* no new cataloged public success surface appears

Required deliverables:

audit/qa/hde-epic027/checks/po-009/catalog\_surface\_inventory.txt

audit/qa/hde-epic027/checks/po-009/token\_inventory.txt

audit/qa/hde-epic027/checks/po-009/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* no unexpected public success surface appears in the catalog inventory

* no non-canonical token names are introduced in the token inventory

FAIL criteria tied to deliverables plus what to capture:

* if a new public success surface appears, classify `FAIL_BEHAVIOR`

* if a non-canonical token name appears, classify `FAIL_BEHAVIOR`

  #### **CHECK po-010: PO-010**

Goal: prove that same-run runtime functional proof exists on the changed runtime surfaces and that artifact-only close is not being substituted for runtime proof.

SOURCE EXCERPT (verbatim):  
 PO-010

Proof obligation:  
 Epic-close verification includes runtime functional proof on the changed runtime surfaces; artifact-only close is not sufficient.

SOURCE EXCERPT (verbatim):

* Functional Live QA is mandatory for functional changes: if a change alters runtime behavior (CLI, HTTP surface, vendor ingest, DB mutation or rejection posture), the Close Gate MUST include a runtime functional proof on that surface

PO actions:

1. Verify that same-run primary logs exist for the runtime proof steps already executed in this run.

2. Inventory the runtime proof surfaces represented by those logs.

3. Write the result to `primary.log`.

4. Update the EPIC027 manifest entry for `po-010`.

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_dev\_conjunction\_http.py  
 Category:  
 Endpoint/surface  
 Proof:  
 assert payload\_one\["writer"\]\["writer\_route\_id"\] \== "dev.writer.conjunction.v1"

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/http/test\_reader\_a7\_transport.py  
 Category:  
 Rails enforcement  
 Proof:  
 write\_proofs \= os.environ.get("HDE\_WRITE\_A7\_PROOFS") \== "1"

SOURCE EXCERPT (verbatim):  
 Path:  
 tests/cli/test\_showcompat\_parity\_and\_identity.py  
 Category:  
 CLI entrypoint/help  
 Proof:  
 def \_run\_showcompat(payload: dict\[str, object\], extra\_args: list\[str\] | None \= None, env: dict\[str, str\] | None \= None):

Execution note:

* Use only exact QA Audit-, PF10-, or canon-proven command strings for this check. If an exact command string is not proven verbatim, do not assert it here as a fixed runbook command.

* Create `audit/qa/hde-epic027/checks/po-010/primary.log` with the required governed first-line JSON header before any transcript bytes are appended.

* Record the exact runtime command lines actually used below that governed first-line JSON header in `primary.log`.

* Any refresh of `audit/qa/hde-epic027/qa_step_logs_manifest.json` and `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check must read the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-010/primary.log`.

Manifest pair creation and update instructions for this check:

* After `audit/qa/hde-epic027/checks/po-010/primary.log` exists for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json` for this check.

* If `audit/qa/hde-epic027/qa_step_logs_manifest.json` does not yet exist, create it at that exact path, creating parent directories if needed.

* The manifest update for this check must add or refresh this check’s entry in `audit/qa/hde-epic027/qa_step_logs_manifest.json` by reading the governed first-line JSON header in `audit/qa/hde-epic027/checks/po-010/primary.log`.

* After the manifest file is created or updated for this check, create or update `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt` for this check.

* The path-proof update for this check must point to the manifest file created or updated for this check.

What to look for:

* same-run runtime logs exist for CLI, dev harness or writer, and Reader A7 surfaces

* runtime proof inventory is based on this run’s primary logs, not on historical artifacts alone

Required deliverables:

audit/qa/hde-epic027/checks/po-010/runtime\_log\_presence.txt

audit/qa/hde-epic027/checks/po-010/runtime\_surface\_inventory.txt

audit/qa/hde-epic027/checks/po-010/primary.log

updated audit/qa/hde-epic027/qa\_step\_logs\_manifest.json

refreshed audit/qa/hde-epic027/qa\_step\_logs\_manifest.json.path\_proof.txt

PASS criteria tied to deliverables:

* all deliverables exist

* runtime-log presence shows no missing prerequisite runtime logs

* runtime-surface inventory proves that same-run runtime surfaces were actually executed in this run

FAIL criteria tied to deliverables plus what to capture:

* if prerequisite runtime logs are missing, classify `TOOLING_BLOCKED`

* if logs exist but show failing runtime tests, classify `FAIL_BEHAVIOR`

  ### **Close-out deliverables**

Unconditional current-state outputs for this runbook:

* `audit/qa/hde-epic027/00_meta/doc_deltas.md`

* `audit/qa/hde-epic027/qa_step_logs_manifest.json`

* `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`

* `audit/qa/hde-epic027/checks/d0_discovery/primary.log`

* `audit/qa/hde-epic027/checks/po-001/primary.log`

* `audit/qa/hde-epic027/checks/po-002/primary.log`

* `audit/qa/hde-epic027/checks/po-003/primary.log`

* `audit/qa/hde-epic027/checks/po-004/primary.log`

* `audit/qa/hde-epic027/checks/po-005/primary.log`

* `audit/qa/hde-epic027/checks/po-006/primary.log`

* `audit/qa/hde-epic027/checks/po-007/primary.log`

* `audit/qa/hde-epic027/checks/po-008/primary.log`

* `audit/qa/hde-epic027/checks/po-009/primary.log`

* `audit/qa/hde-epic027/checks/po-010/primary.log`

* `audit/EPIC-027_close_report.md`

Only the following close-pack refresh outputs are conditional, and only if `po-007` and `po-008` both reach `PASS`:

* refreshed `audit/EPIC-027_MANIFEST.json`

* refreshed `docs/evidence/INDEX.json`

* refreshed `docs/evidence/INDEX.sha256`

* refreshed `artifacts/evidence_index.jsonl`

* refreshed sibling path-proof and checksum companion files produced by canonical tooling

   **What “QA RCA & Doc Delta summary” means (explicit; non-drifting)**

For this runbook, the QA RCA & Doc Delta summary will live as a section of the unconditional `audit/EPIC-027_close_report.md`, and that summary must be produced regardless of whether `po-007` and `po-008` reach `PASS`.

That section must contain:

* what was run

* which checks ended `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, or `TOOLING_BLOCKED`

* the exact blocked condition for any blocked step

* whether any canon delta was observed in this run

* the rerun condition for any blocked step

* a plain statement of whether same-run runtime proof was achieved

## Review guardrails

### Hard blockers for plan approval/execution

* Any invented repo locus, script, test path, route, env var, or fixed output location  
* Any per-run evidence root or per-run nested directory posture  
* Any use of `HDE_BASE_URL` in this EPIC027 runbook  
* Any attempt to use `/internal/dev/sampler` as a cataloged A7 proof target  
* Any step that claims a token not listed in the current canonical EPIC027 token family used here  
* Any step that omits `primary.log`  
* Any executed step that is omitted from `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
* Any attempt to treat a blocked ledger-coherence step as PASS  
* Any attempt to infer the dev writer conjunction method from stale prose instead of proving behavior from audit-proven runtime surfaces

### QA planning QoS guardrails — templates, deferred steps, and prompt-family separation

* This runbook is objective-first. Commands are minimal and tied to concrete evidence.  
* `po-007` and `po-008` are intentionally kept in the runbook even though current audit evidence indicates a likely `TOOLING_BLOCKED` result.  
* If a blocked condition is resolved before execution, rerun the blocked step and refresh the same current-state check directory. Do not create a new run root.  
* Any further scope expansion requires a separate plan revision.

ASK OK?  
