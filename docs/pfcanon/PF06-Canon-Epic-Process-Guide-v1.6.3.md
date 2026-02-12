# **0\. Front Matter**

**Title:** PF06-Canon-Epic-Process-Guide 

**Version:** v1.6.3

**Status:** Canon

**Effective date**: 2026-02-09  
**Last Update Gate:**  BN 9.8.2 Drain A49-51

**Invocation tag:** INV-f2ac55d77ce9aacc

## 0.1 Purpose and scope

This guide defines the epic delivery process for a human \+ pair-programming \+ CodEx workflow. It supplies paste-ready headers, checklists, and prompts. It requires an Audit and a Sandbox Build/Test in each epoch. It sets Close to be PR-first. CodEx automatically opens the pull request and attaches the close pack and the acceptance tokens (PASS) list.

This is process guidance only. It does not constrain execution environments, repository tooling, or any transport or payload bytes (those remain in their canonical homes).

## 0.2 Policy and principles

PR-first via CodEx.

CodEx opens PRs automatically for each epic slice and pushes:

* Code changes

* Doc-Delta updates (repo docs)

* Both evidence indices:

  * Human: docs/evidence/INDEX.json

  * Machine: artifacts/evidence\_index.jsonl

Implementation Agent analyzes PR bundles and produces PF-canon Doc Deltas.

An epic MAY be delivered in a series of PRs (up to 10 PRs per epic), each PR carrying a coherent slice of work with its own code \+ evidence parity.

The Lead Developer gates; the Product Owner is the sole merger and uses squash on PASS.

Agents do not run git and do not create PRs.

The main branch is protected with required checks; squash is the only merge mode.

Re-run proofs only on qualifying drift (green-freeze).

Evidence parity in the same PR.

Whenever proofs or artifacts change, update in the same PR:

* The human Evidence Index (docs/evidence/INDEX.json)

* The hash sentinel

* The machine JSONL mirror (artifacts/evidence\_index.jsonl)

The machine mirror is:

* Records-only

* Canonical JSONL (UTF-8, sorted keys, compact, exactly one trailing LF)

* Strict: rejects unknown keys

Each mirror record includes:

* artifact\_key

* role

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor (to a co-located path-proof)

Repo-doc and docs-only changes must be evidence-backed.

Any claim about CLI behavior, output bytes, tokens, governed artifacts, or system mechanics MUST be supported by at least one of:

* a canon pointer (title-only) to the relevant rule.

* a targeted test run output referenced in the PR summary.

* an existing governed evidence artifact path already committed under governed roots.

Additional docs-only constraints:

* Treat "contract changes" (even docs-only ones) as requiring a tight evidence posture. Tests, proofs, and artifacts should be captured in the same PR bundle whenever possible.

* If a docs-only PR is approved without captured CI/test output, the PR summary or review pack MUST (1) state that verification was diff-only, (2) cite the best available canon pointer or governed evidence path for each non-obvious claim, and (3) record any search method used to look for missing proof.

Copy/paste command safety (docs-only and discovery PRs).

Interactive-terminal safety (no shell-closing blocks).

When a plan, runbook, or repo doc includes a command block intended for an operator to paste into an interactive terminal:

* The block MUST NOT terminate the operator shell session (for example by using exit as part of enforcement).

* If strict enforcement requires exit semantics, the enforcement MUST run in an isolated subshell and report PASS/FAIL (and exit code) without closing the parent shell.

* If a shell-terminating block is genuinely required (rare), it MUST be explicitly labeled as non-interactive and an interactive-safe alternative MUST be provided.

When repo docs include commands intended for copy/paste use:

Commands MUST be truthy and CI-traceable:

* If a command is intended to run a CI check or governed script, document the CI-style invocation as the default.

* Do not present multiple conflicting invocations as co-equal. Any compatibility alternative MUST be explicitly labeled optional and must state when/why it is needed.

* Example (mirror schema validation): default to ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl (CI-style direct invocation). python ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl is an optional compatibility fallback (the script has a Python shebang).

The default command shown MUST be safe and non-epic-specific.

* Do not include unrelated epic IDs, unrelated flags, or “example” values in the default command.

* Any epic-specific selector (for example an \--epic-id flag) MUST be explicitly labeled optional and MUST NOT be presented as the default.

* If a command is conditional on local repo state, environment, or path existence, the doc MUST state the condition and the safe fallback.

Decision-bounded placement (no invented “fits at” paths).

When a doc references a future artifact placement or a not-yet-decided path:

* It MUST be labeled TBD and constrained to the smallest set of plausible options.

* It MUST NOT be presented as a single fixed “would fit at \<x\>” path unless the placement is already governed by an existing canonical rule or governed artifact family.

Review source-retrieval guard (no excerpt-based claims).

Reviewers MUST NOT assert canon violations or contradictions about:

* token rosters (missing/wrong tokens, token semantics mismatch), or

* Live QA rails posture / evidence posture, or

* transport bytes / CLI contract expectations,

unless they have fully retrieved the governing canonical passages being referenced (the relevant roster section(s) and the relevant registry / rails / contract entries).

Build Notes reference posture (living addenda).

When referencing Build Notes in reviews, plans, or Doc Delta notes:

* Do not reference Build Notes by version strings.

* Prefer referencing by addendum number \+ addendum title.

* Do not treat Build Notes section numbers as durable anchors for external enforcement.

Canon mismatch posture (docs-only PRs).

If a docs-only PR documents current repo behavior that appears to diverge from a canonical PF home (for example CLI exit codes vs HDE-CLI-API-Vendor-Ref), the PR MUST:

* state plainly that the text reflects repo-tested behavior (citing the test/evidence used), and

* state that the PF doc remains the single home for the normative contract (titles only), and

* include a Doc-Delta note routing the reconciliation into the canonical home (update canon or update code) rather than implying “canon is satisfied.”

Docs-only PRs MUST NOT claim “conforms to PF-Canon” when the PR’s own evidence indicates an implementation-vs-canon mismatch.

Docs-only PRs MUST NOT introduce unverified assumptions (for example inventing unsupported CLI flags or asserting output formats not proven by canon/tests/evidence). If the evidence is missing, treat it as a spec gap and fix the spec or add the proof, rather than “fixing docs by habit.”

A7 proof surface (when applicable).

* Run HTTP success-path proofs only on a cataloged JSON success route from the Endpoint Catalog.

* The /internal/version endpoint is ops-only and not A7-eligible.

Single homes.

* Public transport & CLI/Reader bytes → HDE-CLI-API-Vendor-Ref.

* Governance & token semantics → HDE-Governance.

* Deterministic serializer/idempotence → HDE-Math-Spec.

* Architecture & single-emitter rules → HDE Architecture.

* Evidence index & mirror schema → HDE-Schemas & Artifacts.

* Infra and environment names → Glow Infrastructure.

PF14 scope guard (doc roles).

HDE-Mechanics Guide (PF14) is a components and operational-surface reference. It MUST NOT define, rename, alias, or curate acceptance tokens, and it MUST NOT be used as a planning authority for acceptance language. Token registry, naming, semantics, and enforcement remain governed by their single homes (titles only).

For HD Engine epics:

* “Prod” is the production HD Engine service and its production database as defined in Glow Infrastructure.

* PF06 does not redefine environment semantics and treats those names as the single home.

When epic docs or QA plans talk about “prod via Codespaces”:

* They must treat Codespaces as a QA console that talks to that production service and DB, not as a prod environment in its own right.

In this guide, “prod via Codespaces” means:

* “Run commands from Codespaces that talk to the production HD Engine service/DB and store QA artifacts in the repo,” consistent with PF10’s “Prod on Railway, QA via Codespaces” addendum.

Baseline PR tokens (titles-only).

* PR\_OPENED\_OK

* TESTS\_PASS\_OK

* DOC\_DELTA\_PRESENT\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* EVIDENCE\_INDEX\_HASH\_OK

* MACHINE\_MIRROR\_UPDATED\_OK

Ops tasks (PO-only execution; IA-guided; not CodEx PR work).

Definition. An Ops task is any work item that requires privileged access to systems outside the repository and therefore cannot be performed by automated agents. This includes (non-exhaustive): service configuration, secrets and env var changes, deploy/runtime settings, infrastructure console actions, and privileged database operations (creation, grants, production migrations, and other privileged state changes). A DevOps task is treated as an Ops task whenever it requires any of the above human-only access.

Execution authority. Ops tasks MUST be executed by the Product Owner (human operator) only. Automated agents (including CodEx-driven agents) MUST NOT attempt to perform Ops tasks, MUST NOT claim completion, and MUST NOT simulate external state changes.

IA facilitation posture. Ops tasks MAY be part of an epic. When included, they are facilitated by the Implementation Agent (IA), who MUST guide the PO through execution. The IA’s job is to specify intent, constraints, verification, and evidence requirements in a what-not-how manner, then work directly with the PO during execution.

Not a PR. Ops tasks are not CodEx PR work. They MUST NOT be represented as “implementable PR work.” Any implementation/remediation document MUST separate Ops tasks from PR work and label Ops tasks explicitly as: PO-only execution, IA-guided.

Ops task record format (required fields). Every Ops task record MUST include:

* Task ID (stable; referenced consistently)

* Owner: PO

* Facilitator: IA

* Target system/service (name only; no secrets)

* Intent / desired end state (what changes; what “done” looks like)

* Constraints / safety rails (what must remain true while executing)

* Success criteria (observable outcomes; not assumptions)

* Evidence to capture (what artifact(s) prove the change; where stored)

* Rollback intent (what “revert” means at a high level)

* Secret handling note (explicitly: no plaintext secrets in docs or evidence)

Evidence posture (required). Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase audit path such as:

* audit/ops/\<epic-id\>/ for Ops execution evidence, or

* audit/qa/\<epic-id\>/ when the evidence is part of QA execution.

Evidence MUST NOT include secrets. If a setting/value is sensitive, evidence must be presence-only, redacted, or hashed, while still being sufficient to verify that the intended state was reached.

Ops evidence provenance minima (required).

Every Ops task evidence bundle MUST include, at minimum:

* Command transcript: the exact command(s) run, recorded verbatim (including any env var names set). Secret values MUST be redacted or presence-only noted.

* Outputs and exit status: stdout, stderr, and the exit code (or equivalent) captured as files.

* Verification outputs are captured, not asserted: if a task claims “checksum OK”, “schema validated”, or similar, the evidence MUST include the tool output that shows the check result (not just a narrative statement).

* Sanitized embedded excerpts: if file contents are embedded in a report, the excerpt MUST be sanitized to remove terminal control sequences. If sanitization would risk altering meaning, embed only a minimal safe excerpt and rely on the on-disk file path as the authoritative content.

Build Checklist tracking requirement. Any Ops task included in an epic MUST be represented as a subtask in the module specific build checklist so it can be tracked and reused. The checklist entry MUST use the same Task ID and carry the same required fields listed above.

No governance drift. Ops tasks MUST NOT create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it MUST map to existing governance-defined acceptance posture and be proven via evidence artifacts.

Clarification. If a change is fully achievable as code (including tests and deterministic artifacts), it is PR work. If any step requires human console/config action, that step is an Ops task (even if adjacent code changes exist). Ops tasks can be prerequisites for epic completion, but they are proven by evidence artifacts, not by agent execution claims.

## 0.3 Participants and responsibilities

* Implementation Agent (ChatGPT). Runs each epic end to end, prepares CRD-ready drafts, sets up CodEx asks (what, not how), verifies proofs and artifacts, ensures Doc-Delta and both indices are updated in the same PR, and escalates blockers to the Lead Developer. Does not run git or create PRs.

* Lead Developer (AI). Defines intent and scope, approves the CRD and Implementation Plan once, performs the gate review on the PR, and otherwise steps out during CodEx execution.

* CodEx. Executes in a sandbox, runs Audit and Build/Test, opens the PR automatically using the template, and attaches the close pack and the PASS list. Adapts within scope and reports all changes. CodEx can read PF docs. Even so, the IA SHOULD paste execution-critical material verbatim during build sessions (formats, schemas, exact token names, commands, and artifact paths) to keep a stable, unambiguous in-session reference and to reduce drift.

* Thoth (CRD authority). Owns CRD standards and architecture fit, confirms acceptance tokens and capsule homes by title.

* Product Owner (human). Sole merger using squash; signs acceptance on PASS; informs the Scrum Master after merge. Owns Tracked Issues and ADR stubs for planning artifacts; adjudicates drift items and approves token minting decisions.

* Scrum Master (AI). Informed after merge; records the close; updates boards and the sprint report.

* Communication rule. AIs do not contact one another directly. The Product Owner routes all messages.

## 0.4 Execution posture and flow (PR-first)

* Lead Dev publishes the Implementation Guide to the Implementation Agent (IA).  
* IA sends Codex an audit request with explicit report formats and any verbatim components/schemas required.  
* Codex returns an audit report covering capabilities, gaps, and risks.  
* IA drafts the Implementation Plan. Lead Dev approves once, then acts only as the PR gate.  
* IA sends Codex build instructions plus verbatim components/schemas. Codex may adapt within scope, must report all changes, and returns a detailed change report plus artifacts and evidence.  
* IA either requests changes or approves.  
* Codex opens the PR epic/-, pushes code, Doc-Delta (repo docs), the human Evidence Index, the machine JSONL mirror, and the close-pack (audit/EPIC-\_close\_report.md, audit/EPIC-\_MANIFEST.json).  
* Machine mirror requirements: records-only canonical JSONL, exactly one LF per line, unknown keys rejected, each record includes a proof\_anchor.  
* Lead Dev gate review:  
  * verify PASS tokens  
  * verify A7 proof surface on the cataloged JSON success route (not /internal/version)  
  * verify env-gate proof and encoding invariance  
  * verify same-PR evidence parity  
  * verify Endpoint Catalog single home present (docs/ENDPOINTS\_CATALOG.json \+ .sha256)  
  * verify Reader A7 proof JSON is captured and indexed (human \+ machine, same PR)  
* PO merges: perform squash merge on PASS and notify the Scrum Master.  
* Closure: IA files the Closure Report; boards and sprint reports updated; suites green-freeze until a qualifying change lands.  
* Determinism pins for determinism-sensitive capture and CI checks: set LC\_ALL=C, LANG=C, TZ=UTC to keep bytes stable. Do not add non-canonical “extra pins” as requirements.

### 0.4.1 Live QA discovery and RCA (execution requirements)  

Live QA via a QA harness is a required Close Gate stage for every epic. See §3.5.2.8 for the harness-run and evidence-landing requirements.

These requirements are execution and Close Gate deliverables. They MUST NOT be treated as prerequisites for Epic Plan approval and MUST NOT force a detailed Live QA runbook into PLAN/CRD or Implementation planning.

0.4.1.1 Mandatory D0 Discovery artifact  
Before running any Live QA steps that exercise behavior or vendor flows, the epic MUST produce at least one Discovery artifact that captures the baseline execution context and rails posture for the Live QA session.

At minimum, this Discovery artifact MUST:

* Record the effective rails posture and runtime context (for example SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, locale/timezone pins, and any other env variables materially affecting Live QA behavior).  
* Summarize which services and surfaces are expected to be reachable for Live QA (for example “CLI only”, “Reader HTTP routes”, “production endpoints”) and any known constraints.  
* Capture initial tool health for key entrypoints (for example CLI help, harness availability) so later failures can be distinguished from simple environment misconfiguration.

Evidence posture (normative)

* The Discovery artifact is a governed, mechanical file under the epic’s QA root (audit/qa//). It is evidence that the session ran under known, documented conditions.  
* Run-id discipline is not a correctness mechanism. Per-run directory nesting MAY exist for convenience/history, but is optional and non-canon. The canonical Discovery artifact is epic-level current-state evidence.  
* The Discovery artifact MUST be generated by commands and MUST NOT be hand-edited. (Titles-only; concrete schemas/paths are owned by the QA template and artifacts specifications.)

### 0.4.1.2 Mandatory QA RCA & Doc Delta summary

Every Live QA epic MUST produce a QA RCA & Doc Delta summary as part of execution deliverables, regardless of whether large gaps are observed.

Definition (normative; prevents drift)  
The QA RCA & Doc Delta summary is not a new plan and not a second epic review. It is a short, evidence-linked explanation of:

* what was run,  
* what the outcomes mean (PASS vs FAIL\_BEHAVIOR vs FAIL\_TOOLING vs TOOLING\_BLOCKED),  
* what evidence proves those outcomes, and  
* whether canon updates are required (or explicitly none).

It exists to prevent re-litigating failures caused by environment/tooling (wrong base URL, missing inputs, network blocked) versus actual behavior regressions.

The summary MUST NOT:

* introduce new acceptance criteria,  
* expand QA scope beyond the epic,  
* propose new QA plans/runbooks beyond what Close Gate requires.

Minimum required contents  
At minimum, the summary MUST:

* State the key Live QA findings in reader-usable language (not just raw logs).  
* If no substantial gaps are found, it MUST say so explicitly (example: “No new PF-Canon deltas identified for this epic”).  
* For each substantive failure or anomaly, classify it as one of: FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED, and include a one-line reason.  
* Provide minimal evidence pointers for each substantive finding (step log(s), artifact(s), validator outputs). (Titles-only here; concrete paths are owned by the QA plan template.)  
* Map each substantive finding that implies a change in behavior, infrastructure, or process to explicit PF-Canon doc deltas by title (examples: HDE Phased Epics, HDE-Build Checklist, Glow QA Guide, HDE-Mechanics Guide, Glow Infrastructure, HDE-Schemas & Artifacts).  
* Identify follow-on epics/cards expected to carry those PF updates when they are deferred.

Location (normative)  
The QA RCA & Doc Delta summary MAY live as a section of the epic close report, or as a separate governed artifact referenced from the close report.

If the QA RCA & Doc Delta summary is maintained as a separate governed artifact, it MUST use the canonical filename `audit/EPIC-<NNN>_QA_RCA.md`. The epic close report MUST reference this artifact by path.

The level of detail is proportional to the findings (brief when no deltas, more extensive when multiple PF docs are impacted). When the run is clean, this summary may be only a few lines.

### 0.4.1.3 Execution gate

For Live QA epics, the Close Gate (§3.5) MUST confirm:

* a D0 Discovery artifact exists for the Live QA session(s), and  
* a QA RCA & Doc Delta summary exists and, where substantial gaps were found, points to concrete PF-Canon updates (or explicitly states none).

If either the Discovery artifact or the QA RCA & Doc Delta summary is missing, the epic MUST NOT be treated as fully accepted, even if code/tests/CI tokens are green.

1. DELTA NOTES  
* Expanded the governed artifacts list to include the machine mirror checksum companion and its proof transcript.  
* Reformatted the governed artifacts list into a consistent inline-code bullet list.  
* Replaced an ellipsis-based close-pack example with an explicit subpath placeholder.  
2. REVISED EXCERPT

## 0.5 Routing and evidence discipline

Single homes (titles-only)

* Transport bytes and CLI/Reader flows → HDE-CLI-API-Vendor-Ref.  
* Token semantics and ops policy (A7, refusal, writers) → HDE-Governance.  
* Canonical JSON, pack/manifest, Human Evidence Index, and machine mirror → HDE-Schemas & Artifacts.  
* Architecture boundaries and single-emitter rules → HDE Architecture.  
* Do not restate bytes, schemas, or token tables here.

Governed locations only

* Evidence artifacts and persisted logs must live under governed paths (audit/**, artifacts/**, and docs/\*\*).  
* Transient/generator paths are disallowed for governed evidence (for example ./outputs, ./runs, ./tmp, /tmp, \~/.cache, .venv).

Live QA execution convenience (/tmp helpers)  
During Live QA execution, QA agents MAY create ephemeral helper scripts under /tmp for execution-only purposes (parsing, formatting, extracting proof facts). These scripts and any /tmp outputs:

* MUST NOT be treated as deliverables or evidence, and  
* MUST NOT be indexed, mirrored, or referenced as acceptance binding surfaces.

Evidence posture is unchanged:

* Any evidence artifact used to decide PASS/FAIL MUST be written under a concrete lowercase path under audit/\*\* (preferred) or artifacts/\*\*.  
* Ephemeral helper scripts MUST NOT print or persist secrets. If they handle sensitive env vars, logs MUST remain presence-only or redacted.  
* Proof files must live under governed paths (audit/**, artifacts/**, and docs/\*\*).

Live QA Moon Loop: minimal in-session remediation is allowed to unblock QA  
Live QA may include a small remediation loop when a check fails due to a small, execution-blocking issue (wrong predicate target, missing guard, etc.) and the smallest correction is required to produce a PASS-grade proof for the already-approved epic scope.

Hard boundary: no scope expansion. In-session remediation MUST NOT:

* add new features or acceptance criteria  
* introduce new evidence families  
* turn QA into a second remediation plan

The only goal is to unblock the existing QA check(s) and prove the already-scoped behavior.

Allowed remediation actions (minimum set)

* Create small helper scripts under /tmp for parsing/glue (ephemeral; never treated as governed evidence).  
* Adjust the QA check procedure to key on the canonical emitted evidence surfaces already required by canon and implementation.  
* Apply the smallest change required for the failing check(s) to execute and validate the intended behavior.  
* Re-run the affected check(s) and capture the PASS-grade evidence artifacts.

Evidence posture for in-session remediation (mandatory)  
If remediation occurs inside a QA session, the existing primary log artifacts MUST make it auditable without additional documents:

* The failing check’s primary.log MUST include the failure signature (short excerpt).  
* The same log (or the session transcript) MUST include a one–two sentence remediation note that names exactly what changed (file paths) and why.  
* The rerun output showing PASS MUST be captured in the same evidence stream.  
* If any repo files were changed, capture a minimal delta artifact under a lowercase governed path, for example:  
  * audit/qa//remediation/moon\_loop/patch.diff (or equivalent)  
  * audit/qa//remediation/moon\_loop/changed\_files.txt (paths \+ sha256)  
  * This delta capture MUST NOT discuss branches, commits, or PR workflow.

Stop condition

Plan-compliant PASS is required for Moon Loop reruns (mandatory). If a Moon Loop rerun records PASS but later fails a plan-defined content predicate (for example missing PF refs in doc-delta content, or a non-plan-compliant primary.log header), treat the step as still non-PASS and continue remediation until a final rerun satisfies all plan predicates.

If the remediation required is not “minimal” (multiple files, structural changes, or unclear scope), stop the Moon Loop and escalate to a normal remediation plan.

Same-PR parity (mandatory)  
When proofs or artifacts change, update all three in the same PR that carries the change:

* the human Evidence Index docs/evidence/INDEX.json,  
* the hash sentinel docs/evidence/INDEX.sha256 (merge-gating), and  
* the machine mirror artifacts/evidence\_index.jsonl.

CI enforces 1:1 join (human↔machine), and blocks on missing/mis-indexed items.

Human Evidence Index and sentinel are governed artifacts (path-proofs required)  
The following files are governed artifacts and MUST each have a co-located path-proof transcript that matches their on-disk bytes:

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Whenever either INDEX.json or INDEX.sha256 changes, their corresponding \*.path\_proof.txt files MUST be refreshed in the same PR. The canonical evidence updater is expected to refresh these proofs during normal runs and to fail in check mode if they are stale.

Mirror hygiene (PF12 schema)  
The mirror is records-only canonical JSONL (UTF-8, compact, exactly one LF), unknown-keys rejected, ASCII field order, sort-before-write, single mirror file.

Each record must include:

* artifact\_key  
* role  
* sha256  
* size\_bytes  
* produced\_at\_utc  
* discovered\_physical\_path  
* proof\_anchor (transcript anchor \+ co-located path-proof)

Governed evidence drift remediation (hard stop)  
If any governed evidence artifact’s recorded metadata (sha256 or size) does not match the physical bytes on disk (for example a \*.path\_proof.txt transcript or a machine mirror record disagrees with the artifact), treat it as a hard stop:

* Do not hand-edit governed artifacts (Index, mirror, path-proofs) to “make checks pass.”  
* Remediate by regenerating using the canonical evidence tooling (single writer) so that:  
  * artifact bytes,  
  * co-located path-proof transcripts, and  
  * machine mirror metadata  
    are coherent.

After regeneration, run the relevant check modes under canonical determinism pins (LC\_ALL=C, LANG=C, TZ=UTC) and any required read-only routing to confirm the drift class is resolved before merge. For evidence skeleton surfaces, this typically includes:

* python tools/evidence/update\_evidence\_index.py \--check  
* python tools/evidence/orientation\_demo.py \--check  
* Mirror schema validation: ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl (CI-style direct invocation).  
* python ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl is an optional compatibility fallback (the script has a Python shebang).

Evidence validation special cases (self-record \+ validator dependencies)

Canonical machine mirror path (single home)  
The only canonical machine mirror file is artifacts/evidence\_index.jsonl. Plans/PRs MUST NOT introduce alternate “mirror” files under docs/evidence/\*\* (for example docs/evidence/INDEX.machine\_mirror.jsonl). If such a path appears in tools/CI output, treat it as drift or a tooling bug and resolve it before close.

Self-record proof semantics (high-risk)  
The Evidence Index and the machine mirror are themselves governed artifacts that may be indexed and path-proofed. When a PR changes evidence tooling or changes how index/mirror/path-proofs are generated or validated, the PR MUST include an explicit self-record regression check (for example a dedicated test that validates mirror self-record proof SHA semantics) and must capture diagnostics that clearly show expected vs found digests when failures occur.

Validator dependency policy (CI stability)  
Any evidence validator (scripts or tests) that depends on non-core packages MUST have an explicit dependency posture:

* Either the dependency is required and installed in CI, or  
* the validator must skip cleanly with an explicit message (no import-time hard failure).

This prevents CI-only failures that block merges without changing product behavior.

Validator run proof (CI-safe)  
When a PR relies on a validator (script or test) as merge evidence (e.g., to enforce acceptance-map / token-matrix invariants), the PR Packet MUST capture:

* the exact invocation used to run the validator  
* PASS output (or failing diagnostics if requesting review)  
* the rails/pins used for the run (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) unless the validator is explicitly documented as pin-insensitive

Ops rails refusal proof (closed-rails)  
Capture a single-file refusal proof at artifacts/proofs/ops\_refusal\_proof.txt containing: required headers, one blank line, and an LF-terminated numeric-free JSON body. This artifact is governed by HDE-Governance (refusal/writers policy; tokens by title) and indexed per HDE-Schemas & Artifacts (mirror/proof\_anchor, records-only JSONL, one LF, unknown-key reject).

Merge gate (path-proofs required)  
Every indexed artifact must have a co-located path-proof referenced by proof\_anchor; CI blocks the merge if any path-proof is missing or mis-indexed. Same-PR parity (human index \+ hash sentinel \+ machine mirror) remains mandatory.

Proof surface routing (A7)  
Success-path proofs run only on a cataloged JSON success route (Endpoint Catalog). The /internal/version ops surface is excluded from A7 and governed by policy in Governance. Capture GET, HEAD, 304 (304 omits both Content-Type and Content-Length), required Vary: Authorization, Accept-Encoding, and encoding-invariance. Env-gate headers proof is required. (Titles-only pointers; bytes live in PF05; evidence lives in PF12.)

Endpoint Catalog single home (titles-only)  
The only authoritative Catalog path is docs/ENDPOINTS\_CATALOG.json (canonical JSON; one LF) with docs/ENDPOINTS\_CATALOG.json.sha256. The Catalog lists JSON success routes only, each with an env-gate; all /internal/\* routes are excluded. A7 proofs must run on a Catalog success route, and an env-gate headers proof is required.

Reader A7 proof JSON (machine-checkable)  
Epics that ship Reader A7 must produce a single proof JSON (records-only, canonical) containing: route\_path, env\_gate, GET/HEAD/after-304 header captures, ETag, vary\_has\_auth, vary\_has\_accept\_encoding, and encoding\_invariance\_ok. Proof JSON and indices update occur in the same PR.

CRD routing  
Thoth receives the CRD only. Keep process artifacts (PLAN/CRD/Doc-Delta) titles-only and route to single homes for bytes/evidence.

Cross-doc references  
Use titles only for all external references; do not duplicate transport bytes, schemas, or acceptance rosters in this guide.

Evidence skeleton coherence (Index/Mirror \+ topology orientation)  
When a PR adds or changes governed evidence and therefore updates the Evidence Index and/or the Machine Mirror, it MUST also refresh the topology orientation demo artifact and its co-located path-proof:

* audit/gates/topology/orientation\_demo.txt  
* audit/gates/topology/orientation\_demo.txt.path\_proof.txt

Determinism predicate surfaces (D16–D18; locked)  
Determinism remediation predicates for D16–D18 MUST validate the canonical emitted evidence surfaces (and required sibling path-proofs) below, and MUST NOT require wrapper bundles or extra non-canon marker-line conventions beyond those canonical surfaces:

* D16 — audit/gates/topology/orientation\_demo.txt \+ audit/gates/topology/orientation\_demo.txt.path\_proof.txt  
* D17 — audit/gates/determinism/env\_pins.log \+ audit/gates/determinism/env\_pins.log.path\_proof.txt  
  * D17 — audit/gates/determinism/env\_pins.log \+ audit/gates/determinism/env\_pins.log.path\_proof.txt  
  * It MUST include a rails object and MUST record the determinism pins LC\_ALL, LANG, TZ.  
  * Under closed rails, the expected pins are SAFE\_MODE:"1", ALLOW\_NETWORK:"0", LC\_ALL:"C", LANG:"C", TZ:"UTC".  
  * Validators MUST treat this schema+pins record as acceptance-decisive and MUST NOT require any additional wrapper bundle beyond the log \+ sibling path-proof.  
* D18 — audit/gates/sanity\_pipeline/sanity\_pipeline.log \+ audit/gates/sanity\_pipeline/sanity\_pipeline.log.path\_proof.txt  
  * sanity\_pipeline.log MUST exist, be non-empty, and MUST contain the decisive identifying lines run:sanity-pipeline, env\_pins: audit/gates/determinism/env\_pins.log, and summary:PASS.  
  * Prerequisite: the sanity pipeline gate requires pytest to be available in the execution environment. Missing pytest is a TOOLING\_BLOCKED failure mode and must be remediated before rerun.  
  * Validators MUST require these minimum lines and MUST NOT require additional non-canon marker conventions beyond them.

Path-proof naming is locked for these canonical surfaces (for example: env\_pins.log.path\_proof.txt — not env\_pins.path\_proof.txt).

HDE-Phased Epics MUST NOT be cited to define evidence surface paths, validator predicate targets, or path-proof naming. Cite the owning canon homes (this guide, Build Checklist, HDE-Schemas & Artifacts, Glow QA Guide, Governance) for those requirements.

If the orientation demo is not refreshed to match the current Evidence Index and Mirror skeleton, the standard check fails with ORIENTATION\_DRIFT.

### **0.5.1 Epic path normalization (close-pack \+ QA root)**

This guide uses normalized epic identifiers for file paths. Plans, QA ledgers, Evidence Index entries, and machine mirror records MUST use these canonical patterns and MUST NOT introduce alternate spellings.

Plan path provenance (no fabricated required paths)  
 A PLAN, CRD, or QA Plan MUST NOT reference a file path as required unless one of the following is true:

* Canon-defined — the path (or path pattern) is explicitly defined by PF canon, or

* Audit-proven — the path’s existence is already proven by an existing, canon-recognized audit artifact family, or

* QA-created — the plan includes inline, explicit creation instructions and validation for the path.

If a path is not canon-defined and not audit-proven, it MUST either be created under QA with explicit instructions and justification, or it MUST NOT appear in the plan.

Plan locus validation labels (required for asserted repo loci)  
 When a planning artifact asserts an implementation locus (repo path, directory root, module home, or “where this lives”), the statement MUST be validated using exactly one of the following labels:

* Canon-cited (preferred): cite the governing PF canon home(s) that define the locus.

* CA vetted: include a verbatim quote from the planning CodEx audit output that proves the locus.

* IG Approved: include a verbatim quote from the approved Implementation Guide that proves the locus.

* QA-created: include explicit creation instructions plus an explicit verification step that proves the locus exists and meets criteria; capture the proof in governed evidence output.

Rules for CA vetted and IG Approved:

* The quote MUST be verbatim. Paraphrase is not permitted for these labels.

* The quote MUST be sufficient to prove the asserted locus. If it does not prove the locus, the plan must not assert it.

File and directory minting posture (do not invent a home)  
 Plans MAY require minting new files and directories only under an already validated, canon-defined home, or under governed QA roots (`audit/**`, `artifacts/**`) when the creation occurs during QA. Plans MUST NOT introduce a new top-level root, a second home for an existing surface, or a guessed repo layout. If a new root or new home is required, treat it as an architecture change and route it via ADR and Doc-Delta before it appears as a required path in a plan.

Review gate  
 Any required locus that lacks a valid label above is a mechanical blocker until corrected.

Environment variable name governance (no QA-time minting)

Environment variable names referenced in QA plans, step logs, and QA evidence schemas are governed interface surfaces, not free text. A QA plan MUST NOT add a new environment variable name “because it would be useful,” and MUST NOT carry forward an unapproved variable name merely because it appeared in a prior iteration.

No QA-time env var minting. Live QA (including Moon Loop execution) MUST NOT introduce new environment variable names as runtime requirements, rails pins, or required evidence keys. If a workflow would require a new environment variable name to function, treat that as development work under PO approval: the variable name MUST be explicitly defined and documented in canon before any QA plan relies on it.

MODO\_\* variables are forbidden. Any environment variable name beginning with MODO\_ is non-canonical for Glow/HDE QA planning and QA execution. QA plans, QA runbooks, and QA evidence schemas MUST NOT introduce, require, or depend on MODO\_\* variables for PASS/FAIL or as required evidence structure (including required header fields, manifests, or required schema fields).

Legacy handling (non-binding only). If an already-approved plan or previously captured QA artifact includes MODO\_\* keys, treat them as diagnostic-only inert placeholders: they MUST NOT be required for PASS/FAIL, MUST NOT be treated as required evidence keys, and MUST NOT be used as proof of rails posture or execution configuration. Remove them in the next plan revision and do not replicate the pattern.

Review posture: any required reliance on an unapproved environment variable name, including any MODO\_\* name, is a mechanical blocker until removed or canon-defined.

If QA must create a file that has no prior canonical existence, the relevant step MUST include:

* exact mkdir \-p and write instructions (no placeholders),

* a one-line purpose (what the file proves and why it exists),

* explicit PASS and FAIL predicates tied to the file’s contents.

QA may create folders/files only under audit/\*\* or artifacts/**. Any instruction that implies creating or writing outside audit/** or artifacts/\*\* is nonconforming.

Plans MUST separate pre-existing artifacts (expected to exist before the QA run) from QA-run artifacts (created during execution). Preflight “presence” checks MUST only gate on pre-existing artifacts.

Review-only posture (fixed artifacts). If a plan states “Commands: None required” and lists fixed-path artifacts as required deliverables, those artifacts MUST be pre-existing (canon-defined or audit-proven) before the step begins. If generation is required, the plan MUST include explicit creation commands and MUST classify the outputs as QA-run artifacts.

Repo-path correctness (code deliverables). When a plan lists a repo code path as a required deliverable (for example, for an existence check), the path MUST resolve in-repo as written. If an architectural alias is used, the plan MUST record an explicit mapping note (alias path to repo path) and the check MUST validate the repo path.

Helper scripts (non-substitutive). Helper scripts created to collect or format evidence MAY be added, but they MUST NOT substitute for required deliverables and MUST NOT change PASS/FAIL predicates unless the plan is revised.

Epic number (\<NNN\>)  
 is the zero-padded 3-digit epic number (example: 022). When an epic ID is HDE-EPIC022, then \<NNN\> is 022\.

Close-pack filenames (canonical)  
 Epic close-pack artifacts MUST use:

* audit/EPIC-\<NNN\>\_close\_report.md

* audit/EPIC-\<NNN\>\_MANIFEST.json

Close-pack path-proof siblings (required)  
 The close report and manifest are governed artifacts and MUST each have a co-located path-proof transcript:

* audit/EPIC-\<NNN\>\_close\_report.md.path\_proof.txt

* audit/EPIC-\<NNN\>\_MANIFEST.json.path\_proof.txt

Close-pack validation checks MUST verify that the path-proof transcripts exist and match the on-disk bytes of their parent artifacts.

Do not create parallel close-pack artifacts under alternate spellings (examples of disallowed alternates: EPIC022, EPIC\_022, `audit/epic-022/<SUBPATH>`).

Close-pack manifest key\_outputs is a named binding map (object).  
 audit/EPIC-\<NNN\>\_MANIFEST.json MUST include key\_outputs as a JSON object (map) where:

* each key is a stable pointer name (string), and

* each value is a repo-relative artifact path (string).

key\_outputs MUST NOT be a list.

Close-pack validation checks MUST validate the named bindings (keys \+ exact paths), not list membership.

Epic QA root (canonical)  
 Epic QA root directories MUST be lower-case and MUST use:

* audit/qa/hde-epic\<NNN\>/ (example: audit/qa/hde-epic022/)

When this guide uses audit/qa//, it means the epic QA root audit/qa/hde-epic\<NNN\>/.

Plans and implementations MUST NOT introduce parallel alternate spellings for the same epic (examples of disallowed alternates: audit/QA/, audit/qa/HDE-EPIC022/, audit/qa/hde-epic022-v2/).

Doc-Delta surfaces (draft \+ epic-scoped capture)  
 Doc-deltas use a two-surface pair. In the Plan and PR, both surfaces MUST use concrete filenames (no placeholders).

1. Draft / staging surface (token binding surface).  
    A doc-delta draft MUST live under:  
    audit/docdeltas/hde-epic\<NNN\>\_doc\_deltas.md  
    Where hde-epic\<NNN\> is the canonical lowercase epic QA slug (for example hde-epic022). This draft surface is the primary surface for doc-delta evidence binding when a doc-delta deliverable is claimed.

2. Epic-scoped capture surface (stable QA record).  
    The epic MUST also capture an epic-scoped doc-delta record under:  
    audit/qa/hde-epic\<NNN\>/00\_meta/doc\_deltas.md

This capture file is the stable record surface for the epic’s QA and closeout narrative. It MUST NOT be replaced by a placeholder reference.

The approved plan’s Doc Delta Capture step (Step-0B or equivalent) MUST confirm these two fixed-path artifacts exist.

The plan’s evidence bindings must clearly distinguish these two surfaces: draft (binding) vs epic-scoped capture (record).

Doc-Delta capture integrity (mandatory). At close, the draft and epic-scoped capture doc-delta files MUST be byte-identical. If they differ, the Doc-Delta capture step MUST remediate and rerun until `diff` returns exit code 0\.

Doc-Delta content completeness (mandatory). Doc-Delta content MUST include PF refs per entry, sufficient to trace each change back to PF-canon drains. PF refs MUST follow the titles-only rule used elsewhere in this document.

Legacy artifacts  
 If legacy artifacts exist under non-canonical names, treat them as deprecated. Do not create new artifacts under deprecated patterns.

## **0.6 Discipline**

### **0.6.1 Canon-first planning**

Implementation Agents MUST treat PF-Canon as the primary source of facts for epic planning and QA.

Before drafting any QA Plan or Implementation Plan for a Live QA epic, they MUST:

* Read Glow Infrastructure, HDE-Build Notes, Glow QA Guide, and HDE Phased Epics (by title) to collect:  
  * environment and infrastructure facts  
  * QA tokens  
  * epic D-goals and exclusions  
* Use canonical infra/env values (for example, production service name, base URL, and DB instance/schema) from those documents directly, instead of treating them as unknowns.  
* Consult Reality Audits (PF23) for any epic touching: ingestion vendors, admin bundle behavior surfaces, live QA in prod, schema migrations.  
* When PF23 consult is required, planning artifacts MUST include a short “PF23 Anchors” note that lists:  
  * the PF23 components consulted (by title)  
  * the key pathnames/loci from Reality Audits that this epic will touch  
* This note is traceability-only. It MUST NOT duplicate PF23 content, and it MUST NOT be presented as a required Live QA deliverable or a required acceptance token.  
* PF23 consult is non-token closure evidence. It is not a gateable token and MUST NOT be represented as a token (for example: no REALITY\_AUDIT\_OK, no PF23\_OK) on a closure pack acceptance roster.  
* PF23 consult scope: PF23 consult may be used to inform epic planning, implementation planning, and QA planning. It MUST NOT be used for PR analysis, PR review, or post-hoc “blockers” in a merge decision.  
* Drift handling (protocol stub): If any PF23 Reality Audit statement appears to contradict PF canon, record a drift item (cite the PF canon requirement and the PF23 statement, explain the contradiction, and propose the minimum safe posture). Route the drift item to the Product Owner for adjudication. Do not resolve by ad-hoc interpretation inside the plan.  
* PF23 is a post-epic audit input: it reflects the latest closed-epic snapshot, not an in-flight PR truth source.  
* PF23 is a post-epic audit input: it reflects the latest closed-epic snapshot, not an in-flight PR truth source.  
* Classify the drift item into exactly one bucket (tentative): canon defect, implementation drift, or necessary reality shift.  
* Do not fix by assumption. No plan, review, or QA artifact may treat the contradiction as resolved unless the Product Owner adjudicates.  
* Resolution routing is PO-owned: canon update, implementation remediation, or formalized exception with canon follow-up.  
* No execution-time PF23 consult artifacts. Live QA plans, runbooks, and step logs MUST NOT introduce required deliverables whose purpose is PF23 consult capture (for example pf23\_consult.md, “PF23 capture” steps, or operator commands intended only to produce PF23 trace artifacts). If a trace anchor is desired beyond the “PF23 Anchors” note above, it MUST remain in plan text only and MUST be informational-only (non-gating).  
* PF23 consult is non-token closure evidence (no REALITY\_AUDIT\_OK). Plans and implementations MUST NOT mint, claim, or reference REALITY\_AUDIT\_OK (or any similar “PF23 consult completion” acceptance token) unless and until Governance registers such a token.  
* PF23 consult scope MUST be represented as a consult requirement and closure evidence, not as an acceptance token. When PF23 consult is required, the work MUST capture a short consult record that includes:  
  * the PF23 Anchors list (components used and loci/pathnames pulled)  
  * a brief “what changed / what did not” summary scoped to the epic or plan  
* This consult record MUST live in existing closure surfaces (for example, the epic-scoped meta record under audit/qa//00\_meta/ and/or the epic close report). It MUST NOT appear in the acceptance token roster.  
* Implementation Agents MUST NOT treat canonical infra/env details that PF-Canon already defines as PO inputs unless PF-Canon explicitly marks them OPEN/TBD.  
* Any QA Plan or Implementation Plan that asks the PO to “provide” such a value without citing an OPEN/TBD gap in PF-Canon is non-conforming and must be corrected before use.  
* Post-Audit ADRs (decision capture). When an audit or plan reveals recurring ambiguity that cannot be resolved by retrieving the governing PF-Canon passages, the Implementation Agent SHOULD capture the ambiguity as a Post-Audit ADR and route it to the Product Owner for adjudication.  
* ADRs are clarification artifacts, not acceptance criteria. They MUST NOT introduce new acceptance tokens, new QA obligations, or new gates.  
* ADR minimum sections (paste-ready headings; fill all fields; keep each section brief):  
  * ADR-\<EPIC\>-\<DOMAIN\>-\<NNN\> — \<title\>  
  * Date: \<YYYY-MM-DD\>  
  * Status: Proposed | Accepted  
  * Decision owner: Product Owner (final), Lead Dev or Implementation Agent (draft)  
  * Context (include audit pointer(s) and plan pointer(s))  
  * Decision (numbered D1, D2)  
  * Alternatives considered  
  * Consequences (positive, negative, tradeoffs)  
  * Canon impact (doc-delta targets by title only)  
  * Non-goals (explicitly list what this   
  * ADR does not change)  
* Doc deltas that drain ADR decisions into canon MUST be paste-ready. Each doc delta entry MUST include:  
  * Target doc (title only) and target section  
  * Current proof excerpt (verbatim; 1–5 lines)  
  * Replacement block (exact replacement text for the excerpt scope)  
  * Why (one sentence; KISS)  
  * Evidence pointer(s) (audit, plan, PR diff, or runtime proofs)

### **0.6.2 Rails and environments (closed-rails vs open-rails QA)**

QA Plans MUST distinguish between:

* Closed-rails determinism checks that run locally with rails closed (for example, serializer and bundle determinism jobs)  
* Open-rails production checks that run from a console (for example, Codespaces) against the production HD Engine service and DB as defined in Glow Infrastructure and clarified in HDE-Build Notes (titles only)

Deterministic parity scenario requirement (acceptance). Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor attempt scenarios) MUST be reproducible under determinism pins \+ closed rails, without reliance on external network or a live database.

Non-canonical env pins are forbidden as Live QA requirements. Live QA steps that produce governed bytes/evidence MUST use only the canonical determinism pins (LC\_ALL, LANG, TZ) and the rails posture as applicable. Plans MUST NOT introduce non-canonical pins (for example PYTHONHASHSEED) as approval or execution requirements.

Determinism is achieved by ordering, not interpreter knobs. If a step or tool is nondeterministic due to hash-order dependence, it MUST normalize ordering explicitly (sort keys, sort lists, avoid unordered set iteration) rather than relying on QA-only rails or interpreter settings.

Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts.

Allowed fallback: if real-codepath deterministic triggering is not feasible, use a deterministic stub layer only to the extent required to produce the canon error envelope and parity artifacts (no live I/O).

Acceptance proof MUST consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and must be indexable under governed evidence surfaces (human index \+ machine mirror in the same PR).

Determinism pins (for example locale/time settings) apply to determinism-sensitive jobs.

When a step is explicitly described as “prod via Codespaces,” the plan MUST:

* assume an open-rails posture sufficient to reach prod  
* prove determinism via repeatable runs and evidence, not by pretending that rails are closed

### **0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)**

For Live QA epics, prod behavior runs in a prod-facing environment.

Any D-goal that is about behavior (for example compat math, narrative generation, vendor ingest, “full product payload” for a pair) MUST define a primary exercise context that can reach the production HD Engine service and DB as defined in Glow Infrastructure.

Examples include:

* a terminal with hdctl configured to call the production base URL  
* an admin GUI in a browser hitting a Railway route

Codespaces is a console and artifact sink, not the prod executor.

Codespaces MAY:

* run offline tools against a checkout of the same code/commit as prod  
* receive and store artifacts (logs, JSON, headers, transcripts) under audit/qa// run offline validation (for example python \-m json.tool, cmp, sha256sum) against those artifacts

Codespaces MUST NOT be treated as “where prod runs” unless the step explicitly:

* describes how the commands in Codespaces are reaching the production service over the network  
* uses that connection as the exercise context

Codespaces environment provenance capture (optional; non-gating). A Live QA plan MAY include a Step-0 “Codespaces snapshot” when execution occurs from Codespaces, but it MUST be explicitly labeled optional and MUST NOT be required for plan approval, execution, or acceptance review.

Reviewers MUST NOT use the presence, absence, or contents of any “Codespaces snapshot” artifact to decide PASS vs REMEDIATION NEEDED.

This guide does not define Codespaces config checklists or snapshot schemas. Consult Glow QA Guide (titles-only) for Codespaces configuration guidance.

Behavior vs artifact phases. Live QA steps that refer to behavior MUST separate:

* a behavior run phase (where the behavior is exercised in a prod-facing environment)  
* an artifact capture & analysis phase (where artifacts from that run are copied or uploaded into the Codespace under audit/qa// and analyzed offline)

The QA Plan MUST be clear about both phases for each such step.

Codespaces-only runs are local smoke checks. Steps that run hdctl or other logic purely inside Codespaces (for example under closed rails with no network) MAY be included as local smoke checks but MUST NOT be used to satisfy prod behavior tokens.

When a token is about prod behavior, its satisfaction MUST be tied to a prod-facing behavior run as described above, with artifacts captured under audit/qa//.

### **0.6.4 PO Live QA vendor-first scope**

For epics that include PO-run Live QA sessions:

Purpose: PO Live QA is a vendor-first activity. Its primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.

What belongs in PO Live QA: Steps in a PO Live QA session MUST be scoped to vendor flows, including (as applicable to the epic):

* vendor-backed BodyGraph resolution (for example bg:resolve \--source=vendor in dry-run or controlled modes)  
* vendor-backed compat calculations (for example compat via vendor-backed inputs or the Admin bundle path once defined by other PF docs)  
* vendor error conditions and edge cases (for example malformed input, missing data, timeouts) that the epic chooses to exercise

What does not belong in PO Live QA: Steps whose only purpose is:

* proving connectivity (for example /internal/version identity pings)  
* re-running determinism, serializer/guard, or sanity checks that are already covered by CI/QA/infra

These checks MUST NOT be treated as part of the PO’s Live QA workload. These checks remain CI/QA/infra responsibilities and may be referenced as pre-work or prerequisites, but they are not, by themselves, a reason to convene a PO Live QA session.

Codespaces rails in PO Live QA: In the context of PO Live QA:

* Codespaces is, by default, an artifact sink and offline analysis console (see §0.6.3).  
* Codespaces MAY temporarily open rails (for example setting SAFE\_MODE=0, ALLOW\_NETWORK=1, base URL pointing to production) only when:  
  * the goal of that step is to exercise a live vendor flow as described above  
  * the rail-opening is documented (env vars set, commands logged, and artifacts captured under audit/qa//logs/)

Showcompat vendor rails posture (Live QA)  
 Until local BodyGraph storage exists, functional showcompat computation requires open vendor rails. When a Live QA step calls showcompat for real computation, open vendor rails for that step only and record the rails settings in the step log header.

Closed rails behavior: attempting functional showcompat under closed rails is expected to fail and MUST be classified as a tooling/environment failure (closed rails), not a behavior failure. Record the rails profile and failure signature in the step log.

Showcompat invocation contract: showcompat requires arguments. A zero-argument invocation is a usage error. Live QA plans and execution steps that call showcompat MUST specify the required arguments per HDE-CLI-API-Vendor-Ref (title only).

Post-step restore: after the vendor step completes, restore default rails posture (SAFE\_MODE=1, ALLOW\_NETWORK=0) for subsequent non-vendor checks.

For non-vendor behavior (serializer determinism, guard proofs, sanity pipeline), Codespaces MUST NOT be used as a surrogate “prod” environment in PO Live QA; those checks belong to CI/QA/infra.

Plans or runs that:

* assign non-vendor checks to the PO’s Live QA workload  
* treat vendor-neutral smoke checks as PO Live QA

are non-conforming and must be corrected by moving those checks into CI/QA and keeping the PO session focused on vendor behavior.

### **0.6.5 Fail-closed to spec gap**

If, during planning, PF-Canon appears ambiguous or incomplete:

* Implementation Agents MUST treat the affected check as blocked by a spec gap  
* capture enough evidence to describe the gap  
* route it into Build Notes and/or HDE Phased Epics as a documented issue  
* instead of improvising new rails, redefining environment semantics, or asking the PO to guess

### **0.6.6 Filesystem naming (directories)**

Rule (global). All directories in the repository and application codebase MUST use lowercase ASCII names.

Scope note. This rule governs directory names only. Filenames with uppercase characters are allowed unless separately forbidden by canon.

Verification posture. Enforcement scans for this rule MUST scan directory names (for example with find \-type d). Scanning file paths (-type f) is over-broad because it includes filenames and can produce false failures under this directory-only rule.

Introducing any mixed-case or uppercase directory name is non-conforming.

Under governed roots (for example audit/**, docs/**, artifacts/\*\*), mixed-case directories are a QA failure, not cosmetic drift.

Remediation posture (when drift exists). If mixed-case directories exist, they are treated as legacy drift and MUST be normalized to lowercase, not copied forward into new work.

Evidence discipline for renames. Any renames that affect governed artifact paths MUST be accompanied by the required index and mirror updates (Human Evidence Index, Machine Mirror, and path-proofs) in the same PR, per the evidence discipline.

### **0.6.7 Mechanical evidence (Live QA)**

When the process says “QA verifies X,” “QA proves Y,” “QA runs Z,” etc., the relevant plan segment must indicate what evidence will be produced to demonstrate that the verification happened and what the result was.

If a step is a PO action (for example, approving a plan, providing a prod URL, or approving a QA slice), the PO action must leave behind at least one inspectable artifact, not just a chat comment.

Acceptable evidence includes step logs, filesystem captures, CLI outputs, tool screenshots, etc. (Evidence MUST be secret-free; scrub tokens, credentials, PII, and private URLs.)

Per-step evidence expectations are defined below. KISS minimum outputs (required) are mandatory.

Each Live QA check/step MUST produce exactly one primary step log for that check (the default evidence artifact for the check), at:

* audit/qa//checks/\<check\_id\>/primary.log

Each Live QA run MUST produce a step-logs manifest, at:

* audit/qa//qa\_step\_logs\_manifest.json

The manifest MUST enumerate, at minimum: check\_id, status, and the primary.log path for each check.

The step-logs manifest is a JSON object, not JSONL; do not emit or require a JSONL variant (for example `qa_step_logs_manifest.jsonl`).

The step-logs manifest is a governed artifact and MUST have a sibling path-proof transcript, at:

* audit/qa//qa\_step\_logs\_manifest.json.path\_proof.txt

Posture-only steps (no validation logic executed). If a check is posture-only and records TOOLING\_BLOCKED, the step MUST still:

* Write the per-check primary.log with status: "TOOLING\_BLOCKED" and include a one-line posture note beginning with UNPROVEN/TOOLING\_BLOCKED: (what is missing / why unproven).  
* Upsert a manifest entry with status: "TOOLING\_BLOCKED" and log\_path pointing to the per-check primary.log (and refresh the manifest path-proof in the same step).  
* MUST NOT claim any \*\_OK tokens.

Each QA step MUST explicitly name the expected artifacts (paths and filenames) it will produce under the canonical QA root audit/qa//. Naming the per-check primary.log satisfies this requirement by default.

If a step claims it updated qa\_step\_logs\_manifest.json, the step’s primary.log SHOULD include a minimal filedump excerpt of the new/updated manifest entry (for example: check\_id, status, log\_path) to prevent ambiguous “done vs next steps” ledger state.

Steps that are “validate existing canon evidence” SHOULD prefer referencing existing governed artifacts in the primary.log (paths-only) over generating duplicate snapshots. Do not create extra artifacts that do not change PASS vs REMEDIATION NEEDED.

Additional required artifacts (files beyond the per-check primary.log \+ manifest) are allowed only when they are acceptance-decisive and already canonized as a governed evidence family/path. If an artifact is diagnostic-only (does not change PASS vs REMEDIATION NEEDED), it MUST NOT be required for plan approval or Live QA execution; it may be included only as optional diagnostics.

Each QA step MUST explicitly name which repo files it will touch/edit. Plans and implementations MUST NOT introduce parallel alternate QA roots or ad-hoc epic slugs.

For PO actions that are used as QA inputs (for example: providing production service/DB identifiers, approving a QA slice), the action MUST be recorded in an inspectable artifact under the canonical QA root—typically in the primary.log of the step that consumed the PO input. It is not sufficient to “say it happened” without leaving inspectable evidence.

### **0.6.8 Operational guardrails**

Live QA plans/runbooks MUST NOT include VCS workflow content (branches, commits, PRs, cherry-pick guidance) and MUST NOT instruct or discuss branch/commit/PR operations.

Live QA plans/runbooks MUST NOT gate PASS/FAIL on VCS state (for example “working tree clean,” “on correct branch,” “commit matches expected,” or any similar VCS-derived condition).

Limited, read-only git commands MAY be included only as optional, non-gating repo-root sanity checks (“this is a repo” / “repo root exists”). They MUST be non-mutating and MUST NOT print or rely on branch names, commit SHAs, or PR identifiers. If a git sanity check fails, the check outcome is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR), and execution MUST proceed via non-git verification paths.

If any git information is captured at all, it is traceability-only and MUST NOT block execution or acceptance decisions.

### **0.6.9 Plans are pointers; QA planning is post-implementation**

Core rule: An Epic PLAN and CRD are pointers to canon and governed artifacts. They are not the place to restate or rebuild canon (token definitions, schemas, CLI semantics, env matrices, etc.).

Do not rebuild canon inside an Epic PLAN/CRD. The PLAN/CRD may reference canonical docs by title only and point to canonical artifact paths. If review “needs” more definition than canon provides, the correction is a doc-delta (update canon) or a governed artifact — not duplicating canonical content inside the PLAN/CRD.

QA planning happens after implementation (and after D0 discovery). A step-by-step QA plan (Live QA step lists, per-step Deliverables blocks, copy/paste command blocks, harness invocation details, etc.) is not an Epic Planning deliverable.

The PLAN/CRD SHOULD provide only:

* titles-only acceptance intent (what must be true)  
* the QA posture (e.g., “Live QA required”)  
* pointers to where QA artifacts will live

The detailed QA Plan is authored/updated during implementation and QA work, and must satisfy the mechanical evidence requirements in §0.6.7 and §1.1.4–§1.1.8.

Approval posture: avoid planning stalls. Reviewers SHOULD NOT block PLAN/CRD approval by demanding:

* a full token/evidence matrix embedded in the PLAN/CRD  
* a fully specified Live QA step list before implementation exists

If a token name/semantics is unclear at planning time, treat it as Deferred (out of scope) and capture the dispute as an ADR/doc-delta rather than debating inside the PLAN.

Live QA plan review outcome discipline (Blockers vs Caveats). Reviewers SHOULD keep Live QA plan approval and execution capture separate: the approval gate is about clarity, scope, and evidence routing — not about pre-creating execution artifacts.

Schema authority (templates \+ step-log headers \+ status vocabulary). The Live QA plan template shape, step-log header schema, and status vocabulary are governed by Plan Templates (titles-only). This guide does not restate or extend that schema; any additional header fields beyond the Plan Templates minimum are optional and MUST NOT be required as a plan-approval condition unless Plan Templates is updated to require them.

Header field omissions are format gaps (capture as caveats). If a plan/template expects specific step-log header fields (for example pf\_refs, intended\_tokens, claimed\_tokens) but the tool-emitted primary.log header omits them, record the omission as a formatting caveat in the QA RCA/doc-delta record. Do not reinterpret PASS/FAIL solely on that omission unless the missing field prevents confident verification of acceptance-decisive proof facts.

Token claims in step logs (claims-only semantics). If a step log includes any \*\_OK token names, they are treated as claims:

* Token lists are optional in runbooks; plans must not be approved/rejected based on token-list completeness.  
* On PASS, the step log may claim one or more \*\_OK tokens that the step actually verified.  
* On any non-PASS status, the step log MUST NOT claim any \*\_OK tokens.  
* If a step needs to record intended tokens without claiming them, list them under a distinct label (for example “intended tokens”) rather than using the claim token list.  
* This is intentionally schematic; see the canonical token registry and per-check token semantics for details.

For each step log MUST:

* Include a stable check ID that is consistent across runs.  
* Include a rails snapshot (at minimum: SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, APP\_ENV). Additional env vars may be recorded if helpful. If present, they are diagnostic only and must not be treated as required pins (for example: PYTHONHASHSEED=0).  
* Include the exact command(s) executed (copy/paste-ready).  
* Capture exit codes (where applicable).  
* End with an explicit step outcome classification (tooling vs behavior), consistent with the status vocabulary in Plan Templates.

Step-log header writer input exports (per-check requirement)  
 If a check generates the primary.log JSON header via a step-log header writer, the plan MUST explicitly export the header writer inputs per check immediately before invoking the writer. Do not rely on inherited values from prior checks. The step-log header schema and status vocabulary remain defined by Plan Templates; this rule governs how plans supply the writer inputs deterministically.

Required per-check exports (names are fixed):

* CHECK\_ID

* CHECK\_NAME

* PASS\_FAIL

* COMMANDS\_JSON

* ARTIFACTS\_JSON

* PF\_REFS\_JSON

Review posture: missing any required export is a mechanical blocker for plan approval and MUST be corrected before execution.

Moon Loop remediation (allowed; evidence-capture only): if execution already occurred but the header is missing or incorrect due to missing exports, it is allowed to export the required variables, regenerate only the JSON header, and rebuild primary.log by prepending the corrected header line while preserving the existing body bytes verbatim. Record the remediation in the step log notes and do not re-run behavioral steps solely to fix header formatting.

Anti-drift: plans MUST NOT mix patterns where some checks export these variables and other checks omit them while still calling the same header writer.

Live QA plan approval, review findings MUST be separated into exactly two sets:

* BLOCKERS — issues that prevent the PO from executing the plan, or prevent reviewers from determining pass/fail for in-scope behavior with confidence. Examples: commands not runnable, missing pass/fail criteria, evidence capture not specified, evidence output location cannot be deterministically found (for example wildcard-only output paths instead of a single primary file or manifest pointer), plan depends on manual-fill placeholders for outputs/evidence, unvalidated or fabricated repo loci (paths, module homes, env var names), prohibited characters outside explicit code spans (Unicode ellipsis character U+2026; three consecutive full stop characters), plan requires production code changes.  
* CAVEATS — issues that do not prevent execution or confident verification. Examples: partial token lists, token registry drift discovered during planning, documentation drift that can be captured via doc delta, presentation-only formatting variance (including markdown heading depth, list marker choice, and whitespace), template/formatting imperfections that do not obstruct execution (including omission of fenced code blocks when commands remain copy/paste-ready and no markup that breaks copy/paste in plain-text venues), omission of optional diagnostic artifacts (for example a “Codespaces snapshot”).

Token/evidence matrix is a QA ledger artifact. When a token/evidence matrix is required for an epic, it is maintained as a governed QA ledger under the epic’s QA root (see §1.1.9). The PLAN may contain a one-line pointer; it must not embed the matrix. The QA root will be filled in during implementation.

## **0.7 QA branches posture**

Purpose: verify evidence and transport posture without touching production code.

Scope: evidence-only.

Allowed changes are limited to governed artifacts: indices and sentinels (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`); Endpoint Catalog single home (`docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`); A7 headers-only proofs (`artifacts/proofs/success_get.txt`, `success_head.txt`, `success_304.txt`, `success_writers_errors.txt`, `success_encoding_invariance.txt`, `endpoints_env_gate_proof.log`); ops rails-closed refusal proof (`artifacts/proofs/ops_refusal_proof.txt`, headers → blank line → LF-terminated numeric-free JSON body); CLI parity (`artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`); DB posture (dev acceptable) (`artifacts/runtime/env_matrix.snapshot.json`, `artifacts/runtime/env_connectivity.snapshot.json`, `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`); BodyGraph evidence (`artifacts/bodygraph/source_selection.snapshot.json`, `artifacts/bodygraph/source_invariance/{ab.json,ba.json,summary.json}`, `artifacts/bodygraph/refresh_policy.snapshot.json`, `artifacts/bodygraph/metrics.snapshot.json`, `artifacts/bodygraph/keys_only.logs.sample`).

Forbidden: any changes under app/service code, migrations/DDL writers, runtime configs, vendor rails, or endpoint behavior.

Path normalization: transient/generator paths (e.g., `codex/out/**`) are forbidden as sources for governed proofs; relocate outputs into `artifacts/**` or `docs/**` before indexing.

Branch/PR: use branch `qa/<epic-id>-<slug>` and open an evidence-only QA PR using §4.5 PR template. Keep evidence and indices in the same PR (parity rule).

Determinism pins: run determinism-sensitive capture and CI with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

CI posture (diff-scoped): CI validates only governed files changed in the QA branch. Minimum checks: mirror schema (records-only JSONL, sorted keys, one LF, unknown keys rejected); final-LF on governed text artifacts; Appendix-D ↔ mirror 1:1 parity with `proof_anchor` path-proof linkage; A7 headers proofs on a cataloged JSON success route (not `/internal/version`) covering GET/HEAD/304, `Vary: Authorization, Accept-Encoding`, and encoding invariance; writers/errors posture headers (`no-store`, JSON errors, no ETag).

Prod handshake requirement (when claimed): if the QA branch/plan claims it exercised prod via Codespaces for an HDE epic, include at least one simple handshake proving commands talk to the canonical production HD Engine service and DB (per Glow Infrastructure). Typical handshake: `curl` the production base URL `/internal/version` from Codespaces and capture the full response under `audit/qa/<epic-id>/logs/`. If omitted, QA is underspecified until the handshake artifact is added.

Rails default: CI/test harness runs CLOSED by default; any job that opens rails must pin policy and attach evidence in the same PR.

Acceptance (titles only)  
 `QA_EVIDENCE_ONLY_OK` — branch contains evidence updates only (no production code).  
 `QA_CI_DIFF_SCOPED_OK` — CI restricted to changed governed files passed.

---

# 1\) EPIC PLAN → CRD (Lead Dev) 

## **1.1 Workflow at a glance**

### **1.1.1 Standard epic flow**

Before applying the steps below, every epic MUST perform a canon inventory:

* Read, by title, the current Glow Infrastructure, HDE-Build Notes, Glow QA Guide, and Reality Audits (PF23) entries that apply to this epic.

* Consult HDE Phased Epics as a historical-only archive of completed epic records (for prior context and precedent). Do not add in-flight epic entries there. The epic record is archived there once, at epic close.

* Record, in the PLAN context header or adjacent notes:

  * key environment and infra facts from Glow Infrastructure (use canonical values; do not treat as PO inputs unless explicitly marked OPEN/TBD in canon)

  * relevant QA tokens and acceptance semantics from Glow QA Guide / PF-Canon (cite the owning canon doc)

  * the epic’s D-goals and exclusions from the epic CRD/PLAN; HDE Phased Epics may be consulted only as historical precedent for the D-goal roster and prior close artifacts (it MUST NOT be cited to define evidence surfaces, acceptance tokens, rails, or status semantics)

* Add a short PF23 Anchors subsection (or adjacent notes) listing:

  * the component(s) used from Reality Audits

  * the key pathnames/loci from that audit that this epic will touch

* This is traceability only. Do not duplicate PF23 contents. Do not assign PF23 updates as tasks (PO-owned).

* If any required fact appears missing or ambiguous, mark it as a spec gap per §0.6.5 (blocked-by-spec) instead of treating it as a PO input or improvising rails.

* Only after this canon inventory is complete should the PLAN header and CRD be drafted.

PLAN header (machine-ready): Draft the PLAN machine header as a single post.

CRD with approved scope: After one review, issue the CRD with the approved scope and acceptance tokens by title only (for example A3, A4, A7); do not list bytes or payload shapes in the CRD.

Code capsules before IP: Finalize code-capsules before IP approval; capsules freeze at IP.

CodEx PR creation: CodEx runs Audit \+ Sandbox Build/Test, then opens the PR automatically using the standard template. In that PR, CodEx pushes, in a single slice:

* Code

* Doc-Delta (repo docs)

* Human Evidence Index (docs/evidence/INDEX.json)

* Machine JSONL mirror (artifacts/evidence\_index.jsonl)

CodEx also attaches:

* The close pack

* The PASS token list

Lead Developer gate: Lead Dev gates the PR by verifying, as applicable:

* PASS token list is consistent and complete

* A7 proof surface is correct (cataloged JSON success route only)

* Env-gates and encoding invariance are respected for A7 proofs

* 1:1 Evidence Index ↔ machine mirror parity with path-proofs

PO merge and green-freeze: The Product Owner is the sole merger and uses squash-merge on PASS. After merge:

* Scrum Master is informed

* Suites are green-freeze unless a qualifying change lands

### **1.1.2 Multi-PR epics**

For some epics (for example EPIC017 and similar Calcination/Separation passes):

* The work may be split into a series of PRs (up to 10 PRs per epic).

* Each PR must carry a self-contained slice with code \+ Doc-Delta \+ evidence.

* The PR-first pattern and same-PR parity (code \+ docs \+ Evidence Index \+ machine mirror) apply to each PR.

* Epic-level acceptance (as recorded in HDE Phased Epics) occurs only after all required PRs for that epic have merged.

### **1.1.3 “Prod via Codespaces” requirements (PLAN/CRD)**

/internal/version auth posture is not canon (non-invention). This guide treats /internal/version as an identity handshake artifact, but it does not canonize:

* its access-control semantics (public vs operator-network gated vs auth-header required)

* the expected failure mode when access is missing/invalid

Until that auth posture is canonized:

* Plans, remediation guides, and operational tooling MUST NOT state /internal/version auth requirements as canon.

* Any statement about auth posture MUST be explicitly labeled Observed Evidence (non-PF) and MUST be secret-free (presence-only, redacted, or hashed).

Evidence required to canonize auth posture (secret-free). To support an eventual canon decision, capture and store (under a lowercase audit path) the status line and headers for the production deployment context(s) under both conditions:

* with no auth header

* with an auth header only if one is explicitly sourced for this run (value redacted or presence-only noted)

Auth headers are optional until canonized. Plans and runbooks MUST NOT require an auth header/token for /internal/version unless the plan also specifies its sourcing explicitly (for example, as an Ops task output owned by the PO). If no auth header exists or no sourcing chain exists, record that fact as Observed Evidence (non-PF) and proceed with the unauthenticated capture. Do not treat “missing auth token” as proof that the endpoint is inaccessible or “ops not implemented.”

This evidence is required input for the canon decision and MUST NOT be replaced by assumptions.

Name prod surfaces by title. The PLAN/CRD MUST name (by title, routing to Glow Infrastructure as the single home):

* the production HD Engine service and base URL

* the production DB instance/schema

Do not invent new environment labels.

Clarify Codespaces role. The PLAN/CRD MUST state explicitly:

* Codespaces is a QA console that runs CLI/HTTP commands against the production service and DB.

* Codespaces is not a production environment in its own right.

Describe the prod handshake and artifact location (identity-only). The PLAN/CRD MUST describe (at a high level):

* an identity/pre-flight handshake step

* where its artifact will live

Example: Step 0: curl the production /internal/version endpoint from Codespaces and store the output under audit/qa/\<epic-id\>/logs/ before running deeper QA.

This handshake is identity-only:

* It proves the QA console can reach the production HD Engine.

* It records which engine\_tag, release\_id, commit, and invocation\_tag were live at the time of QA.

Live QA plans MUST NOT use /internal/version to satisfy any behavior D-goals (for example compat math, narratives, vendor ingest, admin bundle). Those goals require separate behavior steps that exercise prod-facing behavior surfaces and produce their own artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>.

PLAN/CRD entries that refer to “prod via Codespaces” without these clarifications are incomplete and MUST be updated before the epic moves into implementation or Live QA.

Vendor-first Live QA using “prod via Codespaces”. For epics that intend to run vendor-first Live QA (per §0.6.4 and §1.1.6) using the “prod via Codespaces” pattern above, the PLAN/CRD MUST ALSO ensure:

* The epic’s acceptance roster in HDE Phased Epics explicitly declares this posture by title (for example: “Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>”).

* The Live QA plan includes at least one vendor-focused step that:

  * uses or references the prod identity handshake artifact (for example the /internal/version capture under audit/qa/\<epic-id\>/logs/) to anchor which engine instance is under test

  * demonstrates a vendor-backed end-to-end flow (for example vendor-backed resolve or compat) executed against the production HD Engine service, with its own mechanical artifacts captured under audit/qa/\<epic-id\>/\<SUBPATH\> as required by §1.1.4–§1.1.6.

This identity \+ vendor step does not change the identity-only semantics of /internal/version: the handshake remains a pre-flight proof of “which engine is live,” while the vendor-backed flow is what satisfies the vendor behavior portion of the D-goals and is recorded in the PF20 acceptance roster.

### **1.1.4 Live QA mechanical evidence expectations**

For Live QA epics, mechanical, step-explicit QA is still required — but it belongs in the QA Plan (and, where relevant, the Implementation Plan), not embedded inside the Epic PLAN/CRD.

PLAN/CRD posture (planning-time). The Epic PLAN/CRD SHOULD NOT embed the Live QA step list or command blocks.

The Epic PLAN/CRD MUST provide:

* titles-only acceptance intent

* the QA posture (e.g., “Live QA required”)

* a pointer to the QA Plan (titles-only reference) and the epic QA root (audit/qa/\<epic-id\>/)

QA Plan posture (execution-time). For each Live QA step, the QA Plan MUST specify:

* Command(s) to run (copy/paste runnable; no guessing).

* Pass/fail checks (what is asserted, and what constitutes failure).

* Deliverables: exact file artifacts to be produced/updated, with paths under audit/qa/\<epic-id\>/\<SUBPATH\>.

* Any required context (env assumptions, flags discovered in D0, required fixtures), expressed as concrete preconditions.

Live QA plan validity lint (approval gate). A Live QA plan is non-approvable unless all items below are satisfied.

QA planning QoS guardrails (iteration pressure). When Live QA plan iteration count is high, apply the guardrails below to prevent REVIEW-mode drift and to stop non-convergent plan rewrites.

Prompt-family separation (AUTHORING vs REVIEW). Every QA prompt used in this process MUST declare its mode in its header as one of:

* AUTHORING — allowed to draft or restructure plan text, step definitions, deliverables blocks, scripts, and runbooks.

* REVIEW — allowed to evaluate evidence and plan coherence, quote existing plan text, and request plan changes. REVIEW mode MUST NOT invent new commands, runbooks, or evidence pointers.

REVIEW-mode remediation exception (verbatim-only). If remediation requires quoting commands, the REVIEW-mode prompt MAY include only command snippets copied verbatim from the approved plan text (including caveats). The prompt MUST label the snippet as verbatim and MUST NOT introduce new flags, paths, or steps.

QoS stop-rule (iteration churn escalation). If the Live QA plan requires repeated structural remediation for the same failure mode across revisions (suggest threshold: 2), treat the issue as a systems-level prompt/template defect. Escalate to a systems RCA and a canonical drain that targets the class of failure, not the incident.

Step list coherence (no undefined steps). If a Live QA plan includes a step matrix, checklist, or run sequence, every step ID listed MUST have a corresponding step definition in the plan’s Step Details (or the plan MUST explicitly state that the step is out of scope and must not be executed).

Plans MUST NOT list steps that are not defined as executable steps in the plan body. An undefined step ID in the matrix is a mechanical blocker.

Evidence pointers must be concrete (no manifest-only references). Paths, filenames, and evidence routing MUST be explicit in the plan (not “see manifest”).

If the plan references a proof/log file, it must be stored at a governed path and retrievable by reviewers using repo lookup alone.

Any referenced log/proof that is required evidence for an executed, in-scope step MUST be present and retrievable as part of the evidence bundle used for plan approval or final review.

Template semantics for deferred steps (NOT RUN / DEFERRED). If a plan template or closure/rollup step enumerates step-scoped evidence paths for steps that have not executed, it MUST explicitly label those entries as NOT RUN (or DEFERRED). NOT RUN / DEFERRED MUST NOT be treated as a missing-evidence failure and MUST be excluded from missing-evidence counts.

Closure/rollup steps that roll up evidence-path existence MUST separate these states:

* PRESENT — the artifact exists at the referenced path.

* MISSING — the producing step is executed and the artifact should exist, but does not.

* NOT RUN / DEFERRED — the producing step has not executed; no artifact is expected yet.

No dangling links rule for deferred steps. A plan or close-pack rollup MUST NOT present absent future-step file paths as evidence pointers in a way that implies file existence. If listing future-step paths at all, list them only as NOT RUN / DEFERRED entries until the producing step has executed.

A plan MUST NOT list a file path as a required prerequisite unless it is canon-defined or audit-proven. If it is neither, the plan MUST include the exact create/write step(s) under audit/\*\* or artifacts/\*\* (no placeholders) and treat the artifact as QA-run-produced evidence (not a preflight prerequisite).

Directly executable (copy/paste discipline). All operator-run steps MUST be copy/paste runnable in Codespaces. If a step includes script content, it MUST be provided so execution results in a syntactically valid file.

Gitless runbook. Live QA runbooks are gitless in the sense that they MUST NOT describe or enforce VCS workflow (branches/commits/PRs). A runbook must contain only verification steps; no branching, merging, resetting, committing, etc.

Read-only git commands MAY be included only as optional, non-gating repo-root sanity checks (“this is a repo” / “repo root exists”). They MUST be non-mutating and MUST NOT print or rely on branch names, commit SHAs, or PR identifiers. If such a sanity check fails, the check outcome is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR), and the run MUST proceed using non-git verification paths.

If git information is recorded, it must be purely traceability metadata; it must not block the run.

Mechanical-only evidence. Any file treated as QA evidence (including close artifacts) MUST be mechanically produced from commands and MUST NOT contain manual-fill placeholders. If a result is “no deltas,” the produced artifact MUST state that explicitly.

Doc Delta Capture (when Codespaces is used). When Live QA execution uses Codespaces, the plan MUST include a Step-0 Doc Delta Capture step that records any missing prerequisites or doc ambiguity discovered during planning. If no deltas are found, the step must explicitly say “no deltas.” (Step-0 artifacts and requirements are governed by Plan Templates (titles-only).)

A Step-0 “Codespaces snapshot” MAY be captured as an optional diagnostic convenience record, but it MUST be explicitly labeled non-gating and MUST NOT be required for plan approval or execution.

No manual-result placeholders (hard rule). Live QA plans and runbooks MUST NOT include instructions that require the operator to manually fill results (for example “Result: (fill PASS/FAIL/SKIPPED)” or equivalent). Step outcomes must be determined mechanically from the step’s commands and the resulting artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>.

If a plan cannot express a step outcome as commands \+ checks \+ deliverables, that step is non-conforming and must be rewritten or removed.

If a QA Plan step cannot be expressed mechanically (commands \+ deliverables \+ checks), it is not a valid Live QA step in this process.

Execution tolerance for operational doc drift (Live QA). For Live QA execution details (paths, filenames, exact script locations, exact CI job names), if an acceptance roster or plan reference conflicts with repo reality, QA MUST use the repo-real invocation/paths to run the checks and capture evidence.

Source-of-truth posture (Live QA). The plan and rosters define intended steps and checks. The governed Live QA evidence stream (step receipts, manifests, and close-pack artifacts) is the source of truth for what executed and what can be claimed. Plan text is not evidence and MUST NOT be used to infer outcomes, token satisfaction, or coverage.

Coverage vs plan-step accounting (required). The close-pack MUST include a Live QA plan-step coverage ledger for in-scope plan steps, marking each step as Fully evidenced, Partially evidenced, Not evidenced, or Unknown. Any step marked Not evidenced or Unknown MUST be treated as an explicit closeout gap: either a blocker that prevents closeout, or a closure-override waiver that enumerates the gap and its rationale.

Record the mismatch as a CAVEAT: DOC\_DRIFT for later drain.

Do not block execution unless the mismatch prevents knowing what to run or how to verify.

Evidence posture remains non-negotiable: evidence must still be captured under the canonical QA root and governed locations.

Non-blocking DOC\_DRIFT example (common): A step overview lists a specific report JSON filename, but the repo-real run emits the report artifact under a different filename and the plan’s embedded verification predicates do not hinge on the specific report JSON filename. Record DOC\_DRIFT and proceed without retrofitting acceptance to the report filename.

No non-canonical QA scripts or wrappers in Live QA plans (baseline commands only). Live QA plans MUST NOT depend on helper or wrapper scripts unless the tool is explicitly canon-named by path in PF-Canon (template compliance does not imply permission to invent entrypoints).

If a step needs “tooling,” it MUST be either:

* a canon-named entrypoint by explicit path (for example a repo script or CI check that is already established as a governed surface)

* an inline tool whose full source is embedded in the plan step and written into the run-local QA tools directory for that run (no hidden dependencies)

Any plan that references a non-canon script path as a “required surface” is non-conforming and must be revised to validate the governed artifact surface directly using baseline commands.

“Baseline commands” means explicit shell/Python one-liners, direct invocation of canon tools, tee for logs, and explicit file writes, with no reliance on opaque runners.

Command/Entrypoint provenance (no invented executable entrypoints). Plans and runbooks MUST NOT require an executable entrypoint (for example: python \-m \<module\>, bash \<script.sh\>, ./\<tool\>) unless one of the following is true:

* Repo-proven — the entrypoint is a real, versioned repo surface and its existence is confirmed at the specified path / module name at execution time, or

* Canon-defined — the entrypoint is explicitly defined by PF canon as a required tool surface, or

* Explicitly created — the plan includes explicit creation instructions (for example: an OPS step that creates an ephemeral helper under /tmp).

Evidence roots are not code roots. audit/\*\* and artifacts/\*\* are evidence roots. A plan MUST NOT invoke scripts from those roots unless the plan explicitly creates them in-step. (Writing governed evidence outputs under audit/\*\* or artifacts/\*\* is expected.)

QA vs remediation separation. Remediation plans MAY include code changes that modify or add entrypoints only when DEV scope explicitly introduces those entrypoints as versioned repo code.

Preflight existence checks (mandatory). Any OPS step that invokes a repo script, binary, or module MUST include a check that proves it exists before attempting the run. Examples:

* For Python modules: python \-c "import \<module\>; print('OK')"

* For scripts: test \-f \<path\> && test \-x \<path\> || (echo "MISSING"; exit 2\)

If the entrypoint does not exist, the run is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR). The operator MUST stop and capture the transcript as evidence.

### **1.1.5 Live QA behavior vs artifact pattern**

For Live QA work, runtime behavior and governed evidence artifacts are not the same thing. The QA Plan MUST describe them as two distinct phases where applicable.

Behavior execution phase: Run the system/endpoint/harness step that exercises the behavior being tested. Treat this phase as producing signals (responses, logs, outputs) that inform what evidence must be captured, but do not treat “it worked when I ran it” as the evidence artifact.

Artifact capture \+ analysis phase: Capture governed evidence artifacts under audit/qa/\<epic-id\>/\<SUBPATH\> (and related required closeout artifacts). Perform analysis offline (e.g., in Codespace), producing the required summaries, diffs, and verification notes as governed artifacts.

Rule: A Live QA step is not complete unless the artifact phase produces the specified deliverables in the QA root (or other governed locations referenced by Evidence Index/Machine Mirror), even if the behavior phase “looked correct” during execution.

### **1.1.6 PO Live QA vendor-first scope**

When a PLAN or CRD describes PO Live QA (a Live QA session that requires PO time), it MUST:

* Declare PO Live QA as vendor-first. Clearly state that PO Live QA for this epic is a short, focused session whose primary goal is to exercise live vendor behavior against the production HD Engine and capture mechanical evidence of that behavior.

* Label vendor vs non-vendor steps. For all Live QA steps, classify them into:

  * Vendor-focused (class 3): steps that exercise vendor-backed flows (for example vendor-backed BodyGraph resolution, compat, vendor error behavior).

  * Ops/identity (class 1): connectivity and identity checks (for example /internal/version).

  * Internal functional/determinism (class 2): serializer/guard/sanity/determinism checks that can run under CI/QA without involving the PO.

* Identify the PO workload explicitly. Identify the subset of Live QA steps that the PO is expected to run in a Live QA session:

  * This subset MUST consist only of vendor-focused steps.

  * Ops/identity and internal functional/determinism steps MUST be marked as preconditions or CI/QA responsibilities, not PO Live QA workload. They may be referenced as “pre-flight / internal” work but not scheduled into PO’s Live QA time.

* Tie vendor steps to mechanical vendor evidence. For each vendor-focused PO step:

  * Specify the behavior run context (prod-facing environment), per §1.1.5.

  * Specify the artifact capture & analysis commands in Codespaces, including the paths and filenames under audit/qa/\<epic-id\>/\<SUBPATH\> where vendor-related artifacts will be stored (for example JSON bodies, logs, error responses).

  * Ensure that artifacts for vendor steps are clearly identifiable as vendor evidence (for example via a vendor-specific subdirectory or filename convention) so that they can be referenced from epic acceptance in HDE Phased Epics and from QA tokens in Glow QA Guide (titles-only).

Plans that:

* describe PO Live QA without labeling vendor vs non-vendor steps

* assign ops/identity or internal determinism steps to the PO’s Live QA workload

* omit mechanical vendor evidence expectations for PO-run vendor steps under audit/qa/\<epic-id\>/\<SUBPATH\>

are incomplete and must be corrected before PO Live QA is scheduled.

### **1.1.7 D3 CLI guard runs — CI vs open-rails Live QA**

Live QA planning MUST explicitly distinguish between these contexts:

* CI / closed-rails D3 guard runs (authoritative).

  * D3 CLI guard tokens (for example the serializer and emitter guard tokens defined by title in the HDE-Build Checklist and HDE-Mechanics Guide) are authoritatively satisfied by CI and closed-rails runs.

  * The canonical D3 acceptance condition is: guard tools run under the closed determinism rails (for example LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0 as defined by other PF docs) and exit successfully, with their evidence captured and indexed according to those documents.

  * Live QA Plans MUST NOT assume that an open-rails Live QA environment is responsible for re-satisfying these D3 guard tokens; instead, they MUST point to the CI/closed-rails evidence when claiming D3 acceptance.

* Open-rails Live QA guard runs (optional, env-enforcement only).

  * In an intentionally open-rails Live QA environment (for example, a Codespace used for prod-facing behavior tests and artifact capture per §0.6.3–§0.6.4), running the CLI guard tools is optional and is treated as an env-enforcement check only.

  * In this context, a guard run that fails solely due to env mismatch (for example, exit code 1 because the environment is open rails instead of the closed determinism rails expected by CI) MUST NOT be treated as:

    * a wiring bug

    * a failure to satisfy D3 guard tokens

  * Live QA Plans MUST:

    * state explicitly when a guard step is being run in an open-rails environment “for information only” (to confirm that guards enforce env pins)

    * tie D3 guard tokens back to the CI/closed-rails runs, not to these open-rails checks

Effect on PO Live QA: For PO-run Live QA sessions in open-rails environments:

* Guard runs, if present, MAY be used to demonstrate that env pins are enforced.

* Guard failures due solely to env mismatch MUST NOT block PO Live QA or be interpreted as D3 token failures.

* The Live QA Plan MUST refer back to the CI/closed-rails guard evidence as the source of truth for D3 acceptance.

Plans are non-conforming and MUST be corrected if they:

* treat open-rails guard failures as D3 token failures

* omit the CI vs open-rails distinction for guard steps

These plans MUST be corrected so that D3 acceptance is clearly anchored in CI/closed-rails runs, with open-rails guard runs documented as optional env-enforcement checks only.

### **1.1.8 CLI commands in QA Plans (canon-backed only)**

Live QA Plans frequently use hdctl or other CLI commands as entrypoints (for example D0 “CLI presence” checks, D1 error-stream checks, or vendor-facing steps). To keep those steps aligned with PF-Canon and avoid inventing new CLI requirements, the following rules apply.

CLI bytes live in the CLI spec.

All CLI commands, flags, and subcommands used in QA Plans MUST be traceable to at least one of:

* HDE-CLI-API-Vendor-Ref (the single home for CLI/Reader bytes)

* a governed CLI test harness or script in the repo

* a CodEx audit snippet that lists the CLI shape as discovered behavior for this repo

QA Plans MUST NOT introduce new CLI spellings or flags “by habit” (for example a generic \--version check) that are not present in those sources.

D0 CLI presence checks must be minimal and spec-backed.

When D0 includes a “CLI presence” or “CLI baseline” step, that step MUST:

* use command shapes that are explicitly documented as supported (for example a shell-level presence check or a help/usage invocation taken from the CLI spec or CodEx audit)

* phrase the Expected Outcome in terms of what PF-Canon actually requires (for example “CLI is installed and runnable under the pinned rails for later steps”), not in terms of extra behavior that is not a canonical requirement

D0 steps MUST NOT assert stronger expectations (for example “must print a version string” or a particular banner) unless those behaviors are explicitly tied to PF-Canon requirements or epic acceptance tokens by title.

Plan authors MUST copy, not invent, CLI shapes.

Implementation Agents and QA Plan authors MUST derive every CLI command used in a QA Plan from:

* the CLI spec

* an existing test or harness

* a CodEx audit report for this repo

Implementation Agents and QA Plan authors MUST copy those shapes exactly (command name, flags, argument structure), adjusting only concrete values like file paths or epic IDs.

Any time a Plan adds a new CLI usage that is not already present in those sources, the Plan MUST treat that as a spec gap and do one of:

* update the CLI spec first

* remove or replace the command with a canon-backed equivalent

Plan reviewers MUST treat non-traceable CLI commands as blocking.

During PLAN/CRD review for epics that include CLI steps (especially Live QA epics), Lead Dev and QA reviewers MUST:

* spot-check CLI commands in the Plan against HDE-CLI-API-Vendor-Ref, tests, or CodEx audit output

* treat any CLI command or flag that cannot be traced to one of those sources as a blocking issue

Plans with non-traceable CLI commands MUST be corrected before approval by doing one of:

* replace the command with a canon-backed usage

* first add the missing behavior to the CLI spec and tests, and then update the Plan to match

Interaction with other sections: This section refines §0.6.1 “Canon-first planning” for CLI usage: CLI behavior in QA Plans must come from the CLI spec, tests, or CodEx audit, not from generic assumptions.

It complements §1.1.5–§1.1.7 by ensuring that:

* CLI steps used for behavior runs and artifact capture follow documented command shapes

* D3 CLI guard runs in Live QA (when present) still respect the CI vs open-rails distinction while using canon-backed commands

Plans are non-conforming and MUST be revised before PLAN/CRD approval or Live QA scheduling if they:

* rely on CLI commands or flags that are not present in any PF-Canon CLI spec, test harness, or CodEx audit

* assert Expected Outcomes that go beyond PF-Canon requirements without naming the corresponding tokens or docs by title

### **1.1.9 Token fidelity rails for QA tokens and evidence**

This section defines planning \+ review \+ closeout rails for epics that introduce or consume QA Acceptance Tokens.

#### **1.1.9.1 Two axes reminder: PF23 audit scope vs PF19 token semantics**

PF23 audits govern whether particular audit steps are required and how they are executed.

QA Acceptance Tokens remain governed by their canonical registry (names \+ semantics). Waiving, narrowing, or skipping PF23 audits does not waive token fidelity requirements.

#### **1.1.9.2 Token scope discipline (prevent planning stall)**

Every Epic PLAN/CRD or Implementation Plan that references QA Acceptance Tokens MUST classify referenced tokens into exactly one of these sets:

* In-scope tokens: Tokens this epic will claim (i.e., tokens that appear as acceptance proofs / closeout claims).

* Deferred tokens: Tokens identified during planning/discovery, but explicitly out of scope for this epic. Deferred tokens must not be claimed as acceptance proofs for this epic.

* Informative tokens: Tokens mentioned only for context (e.g., “related existing token exists”), but not claimed and not evidence-wired for this epic.

Planning-time rule (no invention): If a token’s canonical name/semantics cannot be identified via canon or an explicit epic-specific approval, it MUST be treated as Deferred (or removed). Do not invent local aliases/synonyms.

Reviewer rule (anti-stall): Token naming disputes should not stall PLAN/CRD approval; classify the token as Deferred and capture the dispute as ADR/doc-delta rather than debating inside the PLAN.

#### **1.1.9.3 Split the checkpoints: Plan approval vs QA ledger completion**

This process separates two checkpoints, but token fidelity is enforced at both.

Stage A is PLAN/CRD approval (planning-time). A PLAN/CRD may be approved only if:

* It includes a titles-only acceptance roster (what must be true).

* It includes a Token Scope block with stable names for in-scope tokens.

* For any epic that introduces or consumes QA Acceptance Tokens, reviewers MUST construct (explicitly or as a checked artifact) a token/evidence matrix for all in-scope tokens.

Stage A token/evidence matrix rule (hard): No in-scope token may have any cell in the token/evidence matrix marked as “e.g.”, “TBD”, or left implicit at approval time.

If a token row cannot be completed without guessing, that token MUST be removed from in-scope and treated as Deferred.

A PLAN/CRD MUST NOT be marked approved (ASK OK) for that token while any row is incomplete or uses placeholders.

Stage A may still defer detailed Live QA runbooks into QA execution artifacts per §1.1.4–§1.1.6, but token naming and token→evidence wiring (by titles/paths/keys) must be explicit.

Stage B is Closeout readiness / Live QA completion (execution-time). Before an epic is considered closeout-ready, the QA ledger must be complete for all in-scope tokens, and the token/evidence matrix must match reality:

* the planned tests/CI jobs/Live QA steps exist and were executed as applicable

* the governed evidence artifacts exist under governed roots

* the Evidence Index \+ Machine Mirror entries referenced by the matrix exist and are coherent

Stage B is verification of the Stage A matrix against produced evidence; it is not a second chance to “finish naming” or “decide token spellings.”

#### **1.1.9.4 Token/evidence matrix is a QA ledger artifact (not embedded in the PLAN)**

The token/evidence matrix is the governed QA ledger that binds each in-scope QA Acceptance Token to:

* tests (unit/integration)

* CI enforcement under closed rails

* Live QA steps (if applicable)

* governed evidence artifacts (paths)

* Evidence Index \+ Machine Mirror entries (keys and proof anchors)

The matrix MUST NOT be embedded inside the Epic PLAN/CRD. The PLAN may include a pointer line to the matrix location (typically under the epic QA root).

Matrix completeness rule (applies at Stage A for in-scope tokens): For every token that is in scope for the epic at PLAN/CRD approval time, the token/evidence matrix MUST have a complete row. No “e.g.”, “TBD”, “??”, or implicit cells are permitted for in-scope tokens at approval time.

Row schema (minimum required fields). Each in-scope token row MUST include:

* PF19 registry name: the canonical QA token name (no aliases).

* Acceptance map / manifest token name: MUST exactly match the PF19 registry name (no epic-local synonyms).

* Tests: the unit/integration tests that exercise the behavior (by identifier or path).

* CI jobs: the CI job(s) that enforce the behavior under closed rails (by job name).

* Live QA steps: step identifiers that demonstrate the token (if applicable), pointing to the epic QA root.

* Evidence artifacts (paths): governed repo-relative artifact paths produced by those tests/steps.

* Evidence Index \+ Machine Mirror entries: the artifact\_key(s) and the expected proof anchoring posture for each artifact:

  * artifact\_key

  * epic\_id

  * tokens (the PF19 token name)

  * proof\_anchor (to the co-located path-proof)

If any in-scope token cannot satisfy this schema without guessing, the token MUST be removed from in-scope (Deferred) before approval.

Uniqueness requirement (always): The token/evidence matrix MUST contain exactly one row per in-scope token. Duplicate rows for the same token are mechanical blockers and must be removed before approval.

Draft scaffolds (not approvable): Draft matrices may exist during plan drafting, but a PLAN/CRD cannot be marked approved (ASK OK) for any token while its row contains placeholders or missing fields.

#### **1.1.9.5 Acceptance token single homes: PF04 registry vs PF19 QA operational library (no local synonyms)**

Acceptance token names and semantics are defined once in the canonical governance registry.

Rules:

* PF04 is the single source of truth for acceptance token names and semantics. Epic plans, acceptance maps, manifests, and step logs MUST reference token names exactly as registered there (no aliases, no near-matches).

* PF19 is the canonical home for QA operational guidance about tokens. PF19 may carry execution guidance (metadata, wiring notes, runbook mapping, evidence expectations), but it MUST reference token names exactly as defined in PF04 and MUST NOT introduce new token names or divergent meanings.

* PF20 acceptance rosters are names-only consumers. Epic acceptance rosters consume token names and MUST validate spelling against the PF04 registry before tokens are treated as claimable acceptance.

* No local synonyms. Epic-local token names, aliases, and “equivalent” spellings are prohibited. If a token name cannot be identified without guessing, it must be treated as out of scope and recorded as a doc delta rather than invented.

Tool-exported token registries and derived token sets (for example `S1_TokenRegistry` output) are observational only and may lag the PF04 registry; they MUST NOT be treated as acceptance authority or used as the source of record for token spelling in plans, close packs, or PR PASS rosters.

If a tool emits `QA_STEP_LOGS_CONSOLIDATED_OK`, treat it as a deprecated alias for `QA_HARNESS_DISCIPLINE_OK` and record the canonical token name in acceptance artifacts.

#### **1.1.9.6 No silent downgrades**

Once a reviewer has identified token naming or token→evidence wiring as a blocking issue (for example missing PF19 entry for a used token, placeholder “e.g./TBD” cells in the token/evidence matrix, or incomplete token→artifact bindings), that blocker MUST NOT be downgraded to “non-blocking” in a later review unless:

* the plan/acceptance artifacts have been updated to resolve the issue, or

* PF-Canon has been explicitly updated to resolve the issue (for example PF19 registry update)

Any downgrade MUST reference the specific resolving change (plan diff and/or PF-Canon change). A change in reviewer interpretation or scope alone is not sufficient.

#### **1.1.9.7 Scope waivers must be explicit and non-transitive**

If the Product Owner or governance chooses to waive or narrow a canon requirement for a particular plan (for example, “PF23 audits are out of scope for this plan”), reviewers MUST:

* record the waiver as a local scope directive in the PLAN/CRD

* state explicitly that other rails remain fully in force, including:

  * PF19 QA token naming/semantics (Glow QA Guide)

  * PF12 evidence/index/mirror rules (HDE-Schemas & Artifacts)

  * PF20 D-goals and token rosters (HDE-Phased Epics)

  * PF09 CI/QA rails (HDE-Build Checklist)

Such waivers MUST NOT be interpreted as permission to relax token naming, acceptance mapping, evidence wiring, or index/mirror discipline.

#### **1.1.9.8 Re-ground before asserting “no canonical token name exists”**

Before any reviewer asserts “no canonical token name exists yet” for a QA behavior, they MUST:

* re-check the PF19 QA Acceptance Tokens registry for an existing token that covers the behavior

* re-read any epic-specific approvals or remediation guides that may already have selected a token name and semantics for this behavior

If an epic-specific approval defines a token name (even if PF19 has not yet been updated):

* plans, acceptance maps, and token/evidence matrices MUST treat that name as canonical for the epic (no alternate spellings)

* PF19 becomes the drainage target (doc-delta) to register/standardize the token; PF19 is not a license to invent new names in the meantime

If neither PF19 nor an epic-specific approval provides a token name that can be used without guessing, the token MUST be deferred out of scope rather than invented.

#### **1.1.9.9 Token value rubric \+ token budget (reduce token sprawl)**

Guard proofs are evidence-only unless Governance registers tokens (normative).

Default posture: serializer/emitter/guard proofs are evidence-only deliverables, not acceptance tokens. They MUST exist, be mechanically produced, and be reviewable, but they do not create new token obligations unless Governance has registered a token name and semantics for that guard.

No token invention: A plan MUST NOT introduce or claim new “guard tokens” unless the token exists in the canonical token registry owned by HDE Governance.

Evidence quality (still strict): Evidence-only does not mean loose. Guard proof artifacts MUST:

* be mechanically generated (no hand edits)

* have a single primary log/artifact per guard check

* include a clear PASS or FAIL classification in the primary artifact

* be stored under governed roots when used as closure evidence

* follow normal index/mirror/path-proof discipline when promoted to governed evidence

Promotion rule: If a guard proof is referenced by acceptance wiring (for example a token/evidence matrix row, acceptance map, or close-pack narrative), it MUST be treated like other governed evidence (stable path, indexed, mirrored, with required path proofs).

Do not admit noise tokens. A QA Acceptance Token should represent an acceptance invariant that can be mechanically evidenced. Do not create tokens for workflow facts (e.g., “docs were read”, “PR was opened”, “a human checked something”).

Default token budget: 0 new tokens per epic.

Exception: up to ≤ 3 new tokens may be introduced only with explicit justification and an ownership plan (doc-delta path). More than 3 requires an explicit governance decision.

#### **1.1.9.10 AB/BA composite identity token name (canonical)**

The only canonical acceptance token name for AB/BA composite identity is:

* COMPOSITE\_ABBA\_IDENTITY\_OK

Any alternate spellings or legacy variants are non-canonical and MUST NOT appear as acceptance tokens in:

* Epic Plans

* acceptance maps

* token/evidence matrices

If an epic inherits legacy wording from a document, the PLAN may include a one-line clarification (example: “legacy name → canonical COMPOSITE\_ABBA\_IDENTITY\_OK”), but the claimed token name remains canonical.

### **1.1.10 PLAN submission preflight (mechanical gate: tokens \+ evidence paths)**

This section defines a mandatory preflight that must pass before an Epic PLAN is considered approvable. It is designed to prevent plan churn caused by missing close-pack items, unregistered tokens, and misbound evidence paths.

#### **1.1.10.1 Close-pack completeness (plan-authoring gate)**

A PLAN is non-conforming unless it explicitly includes the close-pack baseline:

* the complete close-pack file set (by path, titles-only)

* the required close-pack acceptance marker (titles-only)

This is a plan submission gate, not a later Close Gate reminder.

#### **1.1.10.2 Token registry validation (no unregistered acceptance tokens)**

Token load reduction posture (planning). Default posture for Live QA plan approval:

* No per-step token claims are required.

* No full token roster is required in the plan body.

* Tokens remain an optional indexing layer unless token validity is required to interpret pass/fail for a specific test or check.

If a plan lists tokens:

* Token names MUST be exact and registry-valid for anything claimed as acceptance.

* If a token name is encountered in epic rosters or QA materials but is absent from the registry:

  * Do not invent substitute token names.

  * Record as a CAVEAT: UNREGISTERED\_TOKEN (and capture it in Doc Delta Capture), and continue executing tests and capturing evidence normally unless the missing token prevents determining pass/fail with confidence.

Acceptance tokens referenced in an Epic PLAN are governance-controlled names and MUST match the canonical token roster.

Validation gate (mechanical). Every token name listed in:

* the PLAN acceptance roster (Stage A)

* the token/evidence matrix (Stage B, when used)

MUST be validated against the canonical token roster before a plan can be approved.

Unregistered token names are mechanical blockers. They are not style issues and must not be interpreted.

Token Inventory (required before plan finalization)  
 Before finalizing PLAN/CRD acceptance claims, the author MUST:

* List every token the plan intends to claim (including tokens referenced by acceptance maps and token/evidence matrices when used).

* For each token, confirm it exists in an accepted canonical home (HDE Governance, or HDE-Build Notes when newly minted).

* If any needed token does not exist in a canonical home, raise an ADR. If the ADR is approved, mint the token in HDE-Build Notes during planning and include a Doc-Delta task to register it into the Governance token registry. Until minted, the token MUST NOT be claimed.

Acceptance claim posture (tokens only; obligations allowed)

* Acceptance claims MUST be written as canonical token names. Do not use freeform acceptance sentences as substitutes for token claims.

* If a requirement is epic-local and does not warrant a new token, express it as an obligation (non-token requirement) with explicit proof wiring (commands, evidence artifact path(s), and a pass predicate). Obligations must not be formatted to look like token names.

Keyset posture (no new token by default)

* Do not mint a new token solely to express an internal compatibility posture (for example, a keyset contract). Prove the posture as evidence under existing canonical tokens or as an obligation.

Canonical token string hygiene (common invalid variants). Token strings are contract surfaces. Plans, acceptance maps, token/evidence matrices, and step logs MUST use registry-canonical spellings (no aliases, no near-matches).

Observed invalid variants must be corrected as follows:

* CANON\_JSON\_OK → JSON\_CANONICAL\_CHECK\_OK

* DOC\_DELTA\_CAPTURED\_OK → DOC\_DELTA\_PRESENT\_OK  
* COMPOSITE\_AB\_BA\_IDENTITY\_OK → COMPOSITE\_ABBA\_IDENTITY\_OK

* CLI\_READER\_EMITTER\_PARITY\_OK → CLI\_READER\_PARITY\_OK

* CATEGORY\_FRAMEWORK\_OK → (non-canonical and ambiguous; replace with the correct canonical token for the intended claim: MAGIC10\_DOMAIN\_CLOSED\_OK for domain closure, or PREFS\_KEYSET\_10\_OK for prefs keyset contract)  
* 

Close-pack presence is baseline artifacts, not a token by default. Do not include CLOSE\_PACK\_FILES\_PRESENT\_OK in acceptance rosters or plan token lists unless and until Governance explicitly registers and canonizes it as a token. Close-pack presence is verified by the existence of the canonical close-pack artifacts and their evidence bindings.

No ad-hoc new tokens during revise/resubmit. During a revise/resubmit planning loop, the plan MUST NOT introduce new acceptance tokens unless:

* explicitly requested by Lead review

* required due to a clearly identified canon gap

Default posture when a behavior must be enforced and no token exists: state it as a non-token mechanical requirement under the deliverable and prove it via tests/evidence, rather than tokenizing it.

If (and only if) a new token is genuinely required, it must be routed, not invented. A plan may propose a new token only when all of the following are true:

* ADR present in the plan. The ADR explicitly states:

  * proposed token name

  * one-sentence semantics

  * intended evidence surface(s) (paths/titles only)

  * drain targets (titles only)

* Conflict/synonym check performed. The plan records that the proposed token name does not duplicate or alias an existing canonical token.

* Doc-Delta required. The token is registered via Doc-Delta in the canonical token home before it can be required as an acceptance claim.

Until registered, the token may be tracked as a proposed ADR item, but it MUST NOT appear as a required acceptance claim in PLAN/CRD, acceptance maps, or token/evidence matrices.

#### **1.1.10.3 Evidence bundle completeness for local-bundle deliverables**

When a deliverable claims a local bundle of governed artifacts under a directory (example: artifacts/ops/internal\_version/\*), the PLAN MUST explicitly state:

* the complete required bundle paths (titles-only, full paths, no byte restatement), sourced from the canonical bundle definition

* any shared or global governed artifacts required for acceptance that live outside the local bundle root, including canonical paths

If the plan references a canonical bundle definition section by title instead of listing all paths, it must still list:

* any overrides, exclusions, or additions

* any shared/global evidence outside the local bundle root

#### **1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)**

Path-proofs are required, but not primary token evidence. Co-located \*.path\_proof.txt transcripts are mandatory for indexed artifacts and are referenced via proof\_anchor.

However:

* Token/evidence bindings (token/evidence matrices, acceptance maps, and PLAN required evidence lists) MUST bind tokens to the primary artifact(s) and the validator tests.

* Token/evidence bindings MUST NOT list \*.path\_proof.txt files as the primary evidence surface for a token. Path-proofs may be referenced only as the proof\_anchor for a bound primary artifact.

Every acceptance token to artifact binding that appears in an Epic Plan and in the token/evidence matrix MUST be validated against the canonical evidence catalog before approval or merge.

If the evidence catalog defines a fixed canonical path for a token’s evidence surface, the plan and matrix MUST bind to that exact path.

Evidence-path authority order (normative). When determining the authoritative path-of-record or token → artifact binding for governed evidence, resolve conflicts using this authority order (highest wins):

* repo manifests

* audit manifests

* rendered reports

* QA plan text (intent only; never acceptance authority)

Path-proof constraint (no fallback acceptance). This authority order does not relax path-proof requirements. If the highest-authority binding cannot be proven (missing artifact, missing path proof, or hash mismatch), treat it as a tooling or process failure and remediate the binding or regenerate the evidence before claiming acceptance.

Determinism env pins is a single canonical evidence surface.

When DETERMINISM\_ENV\_PINS\_OK is claimed, the only valid evidence surface is:

* audit/gates/determinism/env\_pins.log

* audit/gates/determinism/env\_pins.log.path\_proof.txt

DETERMINISM\_ENV\_PINS\_OK MUST NOT be bound to artifacts/proofs/env\_pins.txt (or any other similarly named file).

When DETERMINISM\_ENV\_PINS\_OK is claimed, all acceptance ledgers and indices MUST bind to the canonical log path, and parity MUST be consistent across:

* token/evidence matrix row

* docs/evidence/INDEX.json

* artifacts/evidence\_index.jsonl

* the proof\_anchor path-proof

Any deviation is a mechanical blocker: fix the binding, do not reinterpret.

Evidence index snapshot artifact family is a single canonical surface (no EPIC-local variant for closure).

Tool entrypoint naming (repo-proven): When a PLAN, runbook, or Implementation Guide references the evidence index snapshot generator, use `python tools/evidence/generate_evidence_index_snapshot.py` and do not reference `python tools/evidence/run_evidence_index_snapshot.py`.

Tool entrypoint naming (repo-proven): When a PLAN references the determinism env pins gate runner, use `python tools/evidence/run_env_pins_gate.py`.

Tool entrypoint naming (repo-proven): When a PLAN references the showcompat artifacts runner, use `python tools/evidence/run_showcompat_artifacts.py`.

Canonical path (normative): Evidence index snapshot artifacts MUST use the gate-family path:

* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json

* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt

EPIC-local posture:

* The EPIC-local variant under audit/qa/\<epic-id\>/\<SUBPATH\>/evidence\_index\_snapshot.json is non-authoritative; it MAY exist for compatibility or run-local context, but it MUST NOT be treated as canonical closure evidence.

* Implementation Plans, QA plans, acceptance maps, and close-pack manifests MUST bind to the gate-family path above (not the EPIC-local variant).

Canonical JSON gate directory is a single canonical evidence family (no dual-home binding).

Canonical directory (normative): Canonical JSON gate artifacts MUST live under: audit/gates/json\_gate/canonical/

Canonical JSON gate artifact surfaces (normative; D19/D20 validate-existing steps):

* audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson

* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

* audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json

Naming posture (normative): Do not accept wrapper bundles or alternate filenames for canonical JSON gate artifacts. Use the canon-defined filenames above.

Path proof posture (normative): Each artifact above MUST be accompanied by its corresponding path proof(s) as defined by the owning canon (titles only).

Validation posture:

* Each \*.ndjson log MUST parse as JSON-per-line.

* Each \*.ndjson log must include at least one record with status="pass" (i.e. the gate log is required to exist and the check must have executed; it cannot be a pure non-execution stub).

* The structured record (json\_gate\_structured\_record.json) MUST parse as JSON; schema and required fields are owned by the canonical artifacts/specification doc (titles only).

Legacy directory posture:

* audit/gates/canonical\_json/ (including audit/gates/canonical\_json/json\_canonical\_check.log) is legacy/non-authoritative naming; do not treat it as the canonical JSON gate evidence family, and MUST NOT require it in Implementation Plans unless the owning canon explicitly reinstates it.

* audit/gates/canonical/ is legacy/compat-only; do not treat it as the canonical JSON gate evidence family.

If tooling emits only to a legacy path, treat as a tooling defect; do not bind to it.

No dual-home acceptance binding:

* Acceptance maps, token/evidence matrices, and close-pack manifests MUST bind to the same canonical JSON gate family. Bind to audit/gates/json\_gate/canonical/ only.

* Any deviation is a mechanical blocker: fix the binding, do not reinterpret.

Canonical compare artifacts: reuse canon surfaces (no epic-local compare paths). Default posture: compare proofs MUST bind to canon-defined compare artifact surfaces. An epic MUST NOT introduce a new compare artifact path as the canonical compare proof unless that surface has been introduced through the canon change pathway and drained into the owning canonical homes.

Any binding to a non-canonical path is a mechanical blocker and must be corrected before approval. If a non-canonical path is truly required, it must be routed via ADR and drained into the correct canonical home.

When a token is claimed as satisfied, the following artifacts MUST agree (paths and keys must match):

* Epic Plan required evidence list (per deliverable)

* token/evidence matrix row for the token

* docs/evidence/INDEX.json entry for the bound artifact

* artifacts/evidence\_index.jsonl mirror record for the same artifact\_key and discovered\_physical\_path

* the path-proof file referenced by proof\_anchor

This validation is enforced as a human review checklist line (pass/fail). An automated validator may be added, but the rule does not depend on automation.

#### **1.1.10.5 PF09 subtask closeout (evidence-binding first)**

When an epic claims closure of a PF09 task or subtask that is described as captured elsewhere or piecemeal, the default closure method is:

* bind existing governed evidence (tests \+ artifacts) into the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix)

* rather than creating new evidence families

Creating a new evidence family for closeout is allowed only if:

* the PLAN includes an explicit gap statement (what is missing from existing evidence)

* the new evidence aligns to governed artifact conventions (titles-only routing to the evidence catalog)

Closure is not considered complete unless the acceptance artifacts explicitly map the PF09 task/subtask to concrete evidence (no implicit it exists somewhere else posture).

### 1.1.11 Plan review rules (content-first; blockers vs caveats)

Scope  
 Plan review evaluates execution feasibility, deterministic pass/fail, and evidence wiring. Plan review MUST NOT gate on presentation-only formatting.

Non-reviewable formatting (do not block)

* Markdown heading depth (H2 vs H3 vs H4) is non-reviewable.

* List marker choice (`-` vs `*`), whitespace, indentation, and text wrapping are non-reviewable. Whitespace-only issues MUST NOT block plan approval, including when embedded snippets have whitespace sensitivity (indentation-sensitive code, shell heredocs, YAML). Capture as a nit and resolve via bounded in-flight remediation during execution, with the executed bytes captured in evidence.

* Copy/paste perfection MUST NOT be an approval gate. Plans and reviews MUST NOT block approval on the expectation that multi-line command blocks will copy and run without any operator adjustment. The approval standard is that the commands and steps are semantically valid and executable with ordinary operator care.

* Command syntax latitude is allowed when command identity and intent are clear. Syntax-only issues (quoting style, line breaks, JSON formatting in shell assignments) MUST NOT block plan approval if the plan makes the intended command identity reviewable and the execution evidence records the exact command used.

* Presentation-only Markdown escapes are non-reviewable. Reviewers may normalize punctuation-escape backslashes for readability when the backslash is escaping Markdown punctuation (for example: \_ used to render \_). Reviewers MUST NOT silently change semantic escapes inside shell strings, JSON env vars, regexes, or file contents.

* Boldface, italics, and line-break differences are non-reviewable unless they obscure required semantics.

Mechanical blockers (planning artifacts)

* Any plan fact that asserts a repo path, module home, env var name/value, CLI shape, script/module/check/test name, endpoint route, or other executable entrypoint MUST be validated (Canon-cited, CA vetted, IG Approved, or QA-created). Unvalidated or fabricated loci are mechanical blockers. Missing tooling is a repo gap to be addressed by PR work, not by QA-time script creation. (See §0.5.1.)

* Plans MUST NOT use placeholders that shift responsibility to reviewers (for example: “PO will fill”, “TBD”, “???”, “e.g.”). If a value is unknown, the plan MUST cite a gap in PF canon and record it as a Tracked Issue with an owner and disposition.

* Prohibited characters are mechanical blockers outside explicit code spans: Unicode ellipsis character (U+2026), and a sequence of three consecutive full stop characters (U+002E repeated three times). Use the approved omission markers below instead.

* Fenced code blocks are prohibited in planning documents, reviews, and plan-derived excerpts. Commands and snippets must be presented as plain text lines with surrounding context and clear labeling rather than fencing.

* Plans, QA plans, endpoint catalogs, and runbooks MUST NOT invent “proof-only” routes. Route references MUST be to canonical registered routes (as defined in the Endpoint Catalog) and to routes that actually exist in the target runtime mount. In particular:

  * Reader surface: GET /reader (canonical). Reader v1 is selected via query param v=1 (for example: GET /reader?v=1).

  * If the API is mounted under /api, /api/reader is an alias of the same Reader surface (not a separate contract).

  * Plans and runbooks MUST NOT reference /api/reader-proof/v1.

  * Aux narrative surface: POST /aux/narrative (canonical).

* Plans and plan-derived artifacts MUST NOT introduce or require run\_id (or similar per-run identifiers) as an operator input, step-log header field, manifest field, or correctness key. Optional per-execution history nesting MAY exist for convenience, but MUST remain non-canonical and non-gating.

Approved omission markers (portable)

* OMITTED

* OMITTED:shortreason

* SNIP:\\\<n linesomitted

* LISTCONTINUES

* REPEATBLOCK

Portable formatting note (inline code-like values)

* For inline code-like values, use double quotes or a CODE: prefix. Do not rely on markdown rendering for meaning.

Reviewer safety posture (no guesswork)

* If a plan view is truncated, garbled, or otherwise unreadable, treat it as a read failure and request a clean re-open of the source text. Do not infer missing content. If an ellipsis token appears in any relied-on passage, treat it as a truncation/read-failure signal until the full source is re-opened and verified; redo any dependent review conclusions after full retrieval.

* Reviewers MUST NOT propose or accept invented repo paths, command invocations, route paths, or token names as “probably right.” Require validation or mark as a blocker.

* When quoting or redlining plan content, do not silently change escapes that affect execution semantics. If you normalize presentation-only escapes for readability, do it explicitly and ensure the quoted or pasted text preserves semantic meaning.

Simplified QA planning posture (planning-time expectations)

* Epic planning does not require a step-by-step QA playbook. Reviewers MUST NOT block on the absence of a full step list at PLAN time.

* If a plan does specify QA steps, each step MUST define a concrete pass predicate and point to a governed evidence output (single primary file or manifest) so that acceptance is deterministic. Steps MUST reference real repo entrypoints and registered routes; missing tooling is resolved by PR work, not by QA-time script creation.

Deferrals and Tracked Issues (no silent drops)

* Any deferred scope item MUST be recorded as a Tracked Issue with explicit disposition and a destination epic ID.

* Deferred items MUST NOT be claimed as accepted or satisfied in the current epic.

Non-goals (for review)

* This section does not require exhaustive QA runbooks during epic planning.

* This section does not change token semantics; it clarifies review gates for plan portability and determinism.  
* 

## **1.2 PLAN: Machine header (paste and fill, then post)**

type: PLAN  
 epic:  
 id: "EPIC-?.?"  
 title: ""  
 goal\_one\_line: ""  
 non\_goals: \["", "", ""\]  
 context\_header: "D=\_\_ W=\_\_ IFC=\_\_ CU=\_\_ POC=\_\_ IC=\_\_ ESC=\_\_ APPLY\_STEPS=\_\_ VERIFY\_CHECKS=\_\_ Ambiguities=\_\_"

dependencies:  
 must\_have: \[""\]

blocks: \[""\]

interfaces\_public: \[""\]

outcomes\_vertical\_cuts:

* ""

* ""

/\# ≤5; titles only (no bytes)  
 acceptance\_proofs:

* "DET\_SERIALIZER\_OK"

* "CLI\_READER\_PARITY\_OK"

* "EVIDENCE\_INDEX\_UPDATED\_OK"

* "EPIC\_IS\_GATE\_OK"

* "A7\_GET\_QUOTED\_ETAG\_OK" \# if the epic delivers a JSON success route

/\# Also include by title, as applicable (no version numbers in prose):  
 also\_include:  
 pr\_baseline\_tokens:  
 \- "PR\_OPENED\_OK"  
 \- "TESTS\_PASS\_OK"  
 \- "DOC\_DELTA\_PRESENT\_OK"

`# Index/mirror (same PR)`  
`- "EVIDENCE_INDEX_UPDATED_OK"`  
`- "EVIDENCE_INDEX_HASH_OK"`  
`- "MACHINE_MIRROR_UPDATED_OK"`

\# Close-pack presence is a baseline artifact requirement (non-token); verified via canonical close-pack filenames.

a7\_detail\_tokens:  
 \- "A7\_HEAD\_PARITY\_OK"  
 \- "A7\_304\_OMITS\_CT\_CL\_OK"  
 \- "A7\_VARY\_AUTH\_AE\_OK"  
 \- "A7\_ENCODING\_INVARIANCE\_OK"  
 \- "A7\_TRANSPORT\_PROOF\_OK"  
 \- "ENDPOINTS\_CATALOG\_INTERNAL\_OK"  
 \- "ENDPOINTS\_CATALOG\_OK"  
 \- "ENDPOINTS\_CATALOG\_ENV\_GATE\_OK"

cli\_detail\_tokens:  
 \- "CLI\_INSTALL\_OK"  
 \- "CLI\_HELP\_OK"  
 \- "CLI\_SHOWCOMPAT\_PRESENT"  
 \- "CLI\_SHOWCOMPAT\_CANON\_OK"  
 \- "CLI\_AB\_BA\_PARITY\_OK"  
 \- "CLI\_TWO\_RUN\_IDENTITY\_OK"  
 \- "CLI\_READER\_EMITTER\_PARITY\_OK"

db\_posture\_tokens:  
 \- "DB\_RUNTIME\_SEARCH\_PATH\_OK"  
 \- "DB\_ROLE\_OK"  
 \- "DB\_SCHEMA\_FINGERPRINT\_OK"  
 \- "DB\_CONN\_ENV\_OK"

risks: \["\<1–2 concise risks\>"\]  
 open\_decisions: \["\<≤3; must resolve before IP\>"\]  
 hd\_engine\_canon\_anchors: \["\<reader|aux|logs|meta|cache|sdk\>"\]

\# exchanged now (or in CRD); not after IP

code\_capsules\_proposed:

* id: "canon\_serializer\_v1"  
   status: "proposed"

* id: "strong\_etag\_v1"  
   status: "proposed"

notes: |  
 PR-first via CodEx. CodEx opens the PR automatically after sandbox build/test.  
 Do not instruct humans to run git or create PRs.  
 Update Doc-Delta \+ human Evidence Index \+ hash sentinel \+ machine JSONL mirror in the same PR when artifacts/proofs change.  
 A7 proofs (if any) must run on a cataloged JSON success route; /internal/version is not A7-eligible.  
 Capture env-gate proof and prove encoding invariance (identity and effective length).  
 Governed locations only: artifacts/\*\* and docs/\*\*; no transient/generator paths.

---

## **1.3 CRD: Machine header (copy/paste)**

epic\_id: "HDE-EPIC0XX"  
 crd\_id: "HDE-CRD0XX"  
 type: CRD  
 scope\_mode: FULL | PATCH | VERIFY  
 acceptance\_proofs:

\#"A7\_PROOF\_PRESENT" etc (titles only)

* "\<ACCEPTANCE\_TOKEN\_1\>"

evidence\_minima:

\#Reader A7 proofs (required when any A7 proof token is claimed)

* "Endpoint Catalog present under audit/qa/\<epic-id\>/endpoint\_catalog.json (or equivalent) and referenced in Evidence Index"

\#CLI parity artifacts (required when CLI parity is in scope)

* "CLI parity evidence: a CLI output capture \+ a REST response capture (paired) for each in-scope endpoint"

\#DB posture

* "DB posture tokens evidenced (titles-only): DB\_RUNTIME\_SEARCH\_PATH\_OK, DB\_ROLE\_OK, DB\_SCHEMA\_FINGERPRINT\_OK, DB\_CONN\_ENV\_OK, DB\_BOUNDARY\_VIEW\_OK, DB\_WRITERS\_ISOLATED\_OK"

\#BodyGraph ingest (required when BG ingestion is in scope)

* "BodyGraph ingest evidence: ingestion logs, payload snapshots (redacted), and verification artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>"

ops\_endpoints:

* "\<OPS\_ENDPOINT\_1\>"

notes\_for\_coder:

* "Short list: routing references, required harness notes, and any non-obvious constraints"

## **1.4 Adjacent pre-start gates (titles-only)**

Purpose. Some epics depend on deliverables from adjacent roles/streams (e.g., EPIC-010 narrative copy gates).

Rule. Pre-start gates must: (a) name the deliverable by title only, (b) register acceptance tokens in Governance, and (c) require evidence entries (human \+ mirror) in the same PR that unblocks the epic. (See Build Notes — Adjacent Subtask gate for EPIC-010.)

## **1.5 Code capsules (PLAN/CRD samples)**

### **canon\_serializer\_v1 (py)**

import json  
 def canon\_dumps(obj):  
 return json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",",":")) \+ "\\n"  
 contracts: CANON\_SERIALIZER\_LF, STABLE\_KEY\_ORDER  
 anchors: IDENTITY\_OK, PREIMAGE\_OK  
 notes: One import path repo-wide; replaces any ad-hoc dumps.

### **strong\_etag\_v1 (py)**

import hashlib  
 def strong\_etag(body\_bytes\_lf: bytes) \-\> str:  
 return '"' \+ hashlib.sha256(body\_bytes\_lf).hexdigest() \+ '"'  
 contracts: STRONG\_QUOTED, SHA256\_BODY\_LF  
 anchors: HEADERS\_OK  
 notes: Never emit ETag for writers/errors.

### **serializer\_ts\_v1 (ts)**

export function canonDumps(obj: Record\<string, unknown\>): string {  
 const keys \= Object.keys(obj).sorted();  
 const ordered: Record\<string, unknown\> \= {};  
 for (const k of keys) ordered\[k\] \= (obj as any)\[k\];  
 return JSON.stringify(ordered) \+ "\\n";  
 }  
 // contracts: CANON\_SERIALIZER\_LF, STABLE\_KEY\_ORDER  
 // anchors: IDENTITY\_OK  
 // notes: SDKs must reproduce service bytes exactly.

# 2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after CRD)

Define how the work proceeds after CRD approval in a way CodEx can execute with minimal inference. Lead Dev approves once, then steps out except for the PR gate review. CodEx can read PF docs. Even so, the Implementation Agent (IA) SHOULD paste execution-critical material verbatim during build sessions (explicit formats, schemas, exact token names, commands, and artifact paths) so the session has an unambiguous reference and avoids drift. CodEx may adapt within approved scope and MUST deliver a detailed change report at the end. PR-first via CodEx: CodEx opens the PR automatically and attaches the close pack and PASS list; the PO is the sole merger (squash on PASS). Repo-docs (Doc-Delta) and the evidence index/mirror trio MUST be updated in the same PR whenever proofs or governed artifacts change.

## **2.1 Machine header**

type: IMPLEMENTATION\_GUIDE  
 epic\_id: "EPIC-?.?"

execution\_flow:

* "Lead Dev publishes this Implementation Guide to the Implementation Agent (IA)."

* "IA → CodEx: AUDIT REQUEST (explicit formats; attach any verbatim components/schemas required)."

* "CodEx → IA: AUDIT REPORT (capabilities, gaps, risks)."

* "IA drafts IMPLEMENTATION PLAN; Lead Dev approves once, then steps out (gate only)."

* "IA → CodEx: BUILD INSTRUCTIONS \+ VERBATIM COMPONENTS/SCHEMAS (CodEx may adapt within scope; must report all changes)."

* "CodEx: BUILD & TEST → returns DETAILED CHANGE REPORT \+ ARTIFACTS/EVIDENCE to IA."

* "IA: requests changes or APPROVES."

* "PR-first via CodEx: CodEx opens PR epic/\<epic-id\>-\<slug\> and pushes code \+ Doc-Delta (repo docs) \+ Evidence Index (human JSON) \+ Evidence Index hash sentinel \+ machine JSONL mirror (records-only, canonical, one LF, unknown keys rejected, ASCII field order, sort-before-write, single mirror file; each record has discovered\_physical\_path and a proof\_anchor to a path-proof file) \+ close-pack files (audit/EPIC-\<ID\>\_close\_report.md, audit/EPIC-\<ID\>\_MANIFEST.json)."

* "When A7 is in scope, the PR also carries: Endpoint Catalog file (docs/ENDPOINTS\_CATALOG.json \+ .sha256), env-gate headers proof, and the composite success proof JSON (artifacts/proofs/reader\_success\_get\_head\_304.json) validated against the PF12 schema."

* "Lead Dev: performs PR gate review; verifies PASS tokens (incl. CLI\_READER\_PARITY\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, CLOSE\_PACK\_FILES\_PRESENT\_OK), and—when applicable—A7 tokens (A7\_HEAD\_PARITY\_OK, A7\_304\_OMITS\_CT\_CL\_OK, A7\_VARY\_AUTH\_AE\_OK, A7\_ENCODING\_INVARIANCE\_OK, A7\_TRANSPORT\_PROOF\_OK, ENDPOINTS\_CATALOG\_INTERNAL\_OK). Confirms Catalog-only proof surface, /internal/version exclusion, env-gate proof, governed locations only."

* "PO: sole merger; squash-merge on PASS; informs Scrum Master after merge."

roles:  
 lead\_dev: "Approves the Implementation Plan once; then acts as PR gate; ensures acceptance tokens and evidence requirements are met."  
 implementation\_agent: "Coordinates with CodEx; supplies explicit formats and verbatim components/schemas; reviews change report; produces Closure Report; ensures Doc-Delta and indices are included in the same PR."  
 codex: "Performs Audit and Build/Test; opens PR automatically per execution\_flow; adapts within scope; returns detailed change report \+ artifacts; can read PF docs, but relies on IA-pasted verbatim formats/snippets for execution-critical material to avoid ambiguity."  
 po: "Routes comms; reviews and performs the squash-merge on PASS; not responsible for opening PRs."

evidence\_routing:  
 interim: "Audit/Build/Test logs and observations returned by CodEx to IA."  
 pr: "Close-pack in PR (report, manifest, proofs) with PASS token list visible; Human Index and hash sentinel updated; machine mirror updated in the same PR; each mirror record includes sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, and a proof\_anchor to a path-proof file; governed locations only (artifacts/**, docs/**)."  
 repo\_docs: "Doc-Delta (titles-only) is committed in the same PR as code and evidence; no separate docs-only PRs."  
 final: "Merge on PASS; IA files Closure Report; Scrum Master updated; boards moved."

determinism\_pins:  
 lc\_all: "C"  
 tz: "UTC"

capsules\_scope: "All capsules finalized at IP approval; immutable thereafter. CodEx may propose scoped improvements but must record them in the change report."  
 codex\_can\_see\_pf\_docs: true

## **2.2 Audit (CodEx)**

Goal. Establish that the codebase can host the change without violating canon, and surface any gaps or risks before Build/Test. CodEx responds in prose and fills the output fields; the Implementation Agent (IA) provides the audit template and any verbatim snippets or schema fragments required for checks.

Checklist (titles only for references; IA supplies exact formats/snippets as needed):

* Serializer posture. One single import path for the canonical serializer (equivalent to canon\_serializer\_v1); flag duplicates or ad-hoc JSON dumps. (HDE-Math-Spec; HDE Architecture — single-emitter rule)

* Idempotence posture. Preimage \+ newline stance match HDE-Math-Spec (fields & ordering; trailing LF) and hashing stance matches SHA-256 over the LF-terminated canonical body.

* Public transport (success path, A7). Satisfiable only on a cataloged JSON success route (Endpoint Catalog by title); not on /internal/version. Confirm feasibility of:

  * Strong, quoted ETag over LF-terminated body

  * HEAD 200 mirroring validators, Content-Type \== GET, Content-Length \== len(identity 200 body)

  * 304 only after prior 200, omitting both Content-Type and Content-Length

  * Vary: Authorization, Accept-Encoding supported

  * Encoding invariance feasible (ETag and effective Content-Length stable across accepted encodings). (HDE-Governance — A7; CLI/API Vendor Ref — transport bytes)

* Endpoint Catalog posture (if A7 in scope). Catalog is internal-only and env-gated per entry; non-prod entries unreachable in prod. Confirm a practical strategy for headers-only env-gate proof. (Governance; CLI/API Vendor Ref; Schemas & Artifacts — index path)

* Composite success proof JSON. Plan to emit a records-only composite proof (reader\_success\_get\_head\_304.json) and validate it against the PF12 composite proof schema (titles-only pointer). (Schemas & Artifacts)

* Writers/Errors transport. Writers are no-store, never 304; error responses carry Content-Type: application/json; charset=utf-8 and no ETag. (Governance — writers)

* Rails closed refusal. On closed rails, refusal is typed numeric-free JSON, no-store, no ETag/Vary/Content-Encoding; confirm plan for the single-file refusal proof shape (headers block → blank line → one-line canonical JSON body). (Governance; Schemas & Artifacts)

* Logs & security. Keys-only logging (no payload bodies, no secrets); redaction & validation posture aligns with Governance; CI grep-guards exist.

* Aux narrative (if in scope). A7-equivalent success path feasible (deterministic text, strong ETag on LF-text); suppression \= 200 with no body and no ETag; policy header supported. (Narratives Guide; Governance)

* Dev DB bridge fallback (PF10-A). In dev, if DATABASE\_URL present but unusable, fall back to DB\_BRIDGE\_URL; refuse if neither is usable. Plan to capture artifacts/runtime/env\_connectivity.snapshot.json; diagnostics keys-only, no secrets. (Governance; Schemas & Artifacts)

* Evidence parity & PR readiness (PF12 single home). Human Evidence Index (docs/evidence/INDEX.json), hash sentinel (docs/evidence/INDEX.sha256), and machine mirror (artifacts/evidence\_index.jsonl) exist or can be emitted in the same PR; mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, one LF), unknown-keys rejected, ASCII field order, sort-before-write, single mirror file, and supports a proof\_anchor pointing to a co-located path-proof file. CI has—or will add—parity/unknown-key checks. (Schemas & Artifacts; Build Notes)

* Governed locations only. All evidence under artifacts/\*\* and docs/\*\*; no transient/generator paths. (Schemas & Artifacts)

* Gaps & proposals. List missing components/schemas; propose minimal fixes or scoped improvements; call out any risks that would block CodEx from opening a PR and satisfying tokens.

Output fields (CodEx fills; IA provides this structure):

audit:  
 serializer\_path: "\<module.path\>"  
 duplicates: \["\<offending.symbol\>", "\<another.symbol\>"\]  
 det\_serializer\_ok: true|false

idempotence\_ok: true|false

a7\_proof\_surface\_exists: true|false  
 a7\_vary\_auth\_ae\_ok: true|false  
 a7\_head\_parity\_ok: true|false  
 a7\_304\_omits\_ct\_cl\_ok: true|false  
 a7\_encoding\_invariance\_ok: true|false

endpoints\_catalog\_file\_ready: true|false  
 composite\_proof\_json\_ready: true|false  
 env\_gate\_proof\_ready: true|false

writers\_errors\_semantics\_ok: true|false

refusal\_proof\_ready: true|false

logs\_keys\_only\_ok: true|false  
 governed\_locations\_ok: true|false

dev\_db\_bridge\_fallback\_ready: true|false  
 dev\_connectivity\_snapshot\_ready: true|false

human\_index\_wired: true|false  
 human\_index\_hash\_ready: true|false  
 machine\_mirror\_wired: true|false  
 mirror\_schema\_ok: true|false  
 path\_proofs\_ok: true|false

missing\_components: \["\<title\>", "\<another.title\>"\]  
 proposed\_fixes: \["\<short\_fix\>", "\<another\_fix\>"\]  
 blockers: \["\<risk\_1\>", "\<risk\_2\>"\]

### **Findings → Doc Delta Map (required; single sink)**

In addition to the structured output fields above, CodEx MUST provide a short narrative audit report that is directly drainable into Doc-Delta and PO adjudication when canon ambiguity or implementation drift is discovered.

Use the exact labels below (fill every field; use N/A when a field does not apply).

Audit Summary

\<one sentence\>

Drift theme: "\<theme\>"

Count of findings: \<N\>  
 Count of Must-act-now findings: \<N\>

Findings → Doc Delta Map (required; single sink)

FND-001 —

Finding (one sentence): \<one sentence\>  
 Audit anchor: \<verbatim observed line\>  
 Audit evidence pointer: \<repo path or artifact pointer\>  
 Epic Plan linkage (one sentence): \<one sentence\>  
 Epic Plan anchor: \<verbatim plan line or N/A\>  
 Must-act-now: YES|NO  
 Doc deltas required (bullets; at least one; targets only):

* PF09 task delta: YES (required)

* PF14 mechanics delta: YES|NO

* PF02 architecture delta: YES|NO

* Other PF canon delta(s): \<titles-only list or None\>

Repeat FND blocks until all findings are captured. Use sequential IDs (FND-001, FND-002, FND-003, and so on).

Doc Delta Proposals — PF09 (Tasks) (required)

PF09-TSK-001 —

Task ID: \<PF09\_TASK\_ID\_PLACEHOLDER\>  
 Status: Not done | Optional | Done  
 Task title: \<short title\>  
 Type: Canon update | Clarify | Debt/confirm  
 Must-act-now: YES|NO  
 Source finding: FND-\<NNN\>  
 Evidence pointer(s):

* \<pointer\>  
   Notes (optional; 1 line): \<note\>

Repeat PF09-TSK blocks until all required tasks are captured.

Doc Delta Proposals — PF canon (include only if any delta is YES)

DELTA-001 —

Target doc: \<PF doc title\>  
 Target section: \<heading text or §X.Y\>  
 Delta (actionable; 1–3 bullets):

* \<delta bullet\>  
   Why (one sentence): \<one sentence\>  
   Evidence pointer(s):

* \<pointer\>  
   PF proof excerpt (required if a section is cited; verbatim lines):  
   \<1–5 verbatim PF lines\>

Doc-delta proposals are targets-only. Do not restate transport bytes, schemas, or token tables in audit output.

## **2.3 Code Review (CodEx)**

Goal. Review proposed change style and safety against canon, given IA-supplied formats/snippets.

Checklist:

* No numerics in public payload/narrative.

* Writers/Errors responses follow Governance semantics (by title).

* No RNG/time sources in deterministic paths.

* No additional public interfaces beyond interfaces\_public in the plan.

Output:

code\_review:  
 public\_numeric\_free: true  
 writers\_errors\_semantics\_ok: true  
 deterministic\_paths\_ok: true  
 interfaces\_within\_limit: true  
 red\_flags: \[\]

## **2.4 Sandbox Build/Test (CodEx)**

Describe, at a high level, what was built and what was verified. Include a Detailed Change Report that IA can audit and file.

Output:

sandbox:  
 build\_summary: "\<what was built and why\>"  
 tests:  
 ab\_ba\_identity\_ok: true  
 two\_run\_identity\_ok: true  
 transport\_parity\_simulated: true  
 artifacts\_recorded: \["build.log", "test.log"\]  
 detailed\_change\_report:  
 files\_added: \["\<file\_path\_1\>"\]  
 files\_modified: \["\<file\_path\_1\>"\]  
 files\_removed: \["\<file\_path\_1\>"\]  
 deviations\_from\_instructions: \["\<deviation\_1\>"\]  
 improvements\_made\_within\_scope: \["\<improvement\_1\>"\]  
 known\_limitations: \["\<limitation\_1\>"\]  
 followups\_suggested: \["\<followup\_1\>"\]

# 3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)

## **3.1 Machine header**

{  
 "type": "IMPLEMENTATION\_PLAN",  
 "epic\_id": "EPIC-?.?",  
 "crd\_link": "\<pointer\>",  
 "digest": "\<≤1 page: how tasks satisfy proofs and surface/contract constraints\>",  
 "assumptions": \["\<assumption\_1\>"\],  
 "context\_header": "D=\_\_ W=\_\_ IFC=\_\_ CU=\_\_ POC=\_\_ IC=\_\_ ESC=\_\_ APPLY\_STEPS=\_\_ VERIFY\_CHECKS=\_\_ Ambiguities=\_\_",  
 "code\_capsules\_finalized": \[  
 {"id": "canon\_serializer\_v1", "status": "approved"},  
 {"id": "strong\_etag\_v1", "status": "approved"},  
 {"id": "serializer\_ts\_v1", "status": "approved"}  
 \],  
 "codex\_inputs": {  
 "verbatim\_payloads": \["\<components\>", "\<schemas\>", "\<formats/snippets\>"\], // CodEx can read PF docs; still paste execution-critical material verbatim to keep an unambiguous in-session reference  
 "instructions": "\<clear WHAT, scope limits, and acceptance expectations\>",  
 "freedom\_within\_scope": "CodEx may adapt/fix within scope; must report all changes at end",  
 "reporting\_requirements": "Return detailed\_change\_report \+ artifacts/evidence"  
 },  
 "pr\_expectations": {  
 "template\_required": true,  
 "acceptance\_tokens": \[  
 "DET\_SERIALIZER\_OK",  
 "TRANSPORT\_A7\_OK",  
 "CLI\_READER\_PARITY\_OK",  
 "INTVER\_NO\_STORE\_NO\_ETAG\_OK",  
 "EVIDENCE\_INDEX\_UPDATED\_OK"  
 \],  
 "close\_pack\_files": \[  
 "audit/EPIC-\<ID\>\_close\_report.md",  
 "audit/EPIC-\<ID\>\_MANIFEST.json"  
 \]  
 }  
 }

CodEx portability rule (Implementation Plan codex\_inputs)

The final implementation prompt given to CodEx MUST be self-contained. Do not reference planning-time CodEx audit artifacts or “CA vetted” notes as external context. If a planning artifact uses CA vetted or IG Approved quotes for validation, convert them into canon citations and explicit repo paths before handing off to CodEx. Paste any execution-critical schemas, formats, or commands inline, because CodEx cannot access external attachments.

## **3.2 Tasks (repeat per task; keep atomic)**

task:  
 name: "\<atomic task name\>"  
 description: "\<what changes conceptually\>"  
 inputs: \["\<docs or modules\>"\]  
 dependencies: \["\<tasks\>"\]  
 expected\_observables:  
 \- "\<what will be true if task succeeds\>"  
 proof\_coverage: \["DET\_SERIALIZER\_OK", "TRANSPORT\_A7\_OK"\]  
 validation\_text: "\<how success will be reasoned and later reported\>"  
 capsules\_used: \["canon\_serializer\_v1", "strong\_etag\_v1"\]

## **3.3 Blockers and resolutions**

blockers:

* item: "\<description\>"  
   resolution: "\<resolve|waive|defer\>"

## **3.4 Approval**

ip\_approval:  
 lead\_dev\_decision: "APPROVED"  
 notes: "\<optional\>"  
 lead\_dev\_steps\_out: true

From this point, CodEx and IA proceed per the approved IP. Lead Dev returns only to gate the PR.

## **3.5 Close Gate (PR-first)**

### **3.5.1 Requirement**

For every epic, work is delivered PR-first via Codex.

Codex opens PRs automatically for each epic slice and pushes code \+ Doc-Delta \+ evidence in the same PR.

An epic MAY use up to 10 PRs to deliver its full scope; each PR MUST be self-contained and follow the PR-first and parity rules in §0.2.

The Product Owner (PO) is the sole merger (squash on PASS).

Epic-level acceptance (as recorded in HDE Phased Epics) occurs only after:

* all required PRs for that epic have merged

* the Close Gate has been satisfied

HDE Phased Epics is historical-only: the epic record is added there once, at epic close, as the final archived entry. In-flight epics MUST NOT be recorded there.

The Close Gate applies to the PR that carries the epic close-out (close PR).

All earlier PRs in the series must still be PR-first and parity-clean.

Only the close PR is required to carry the full close-pack and final PASS roster described below.

### **3.5.2 Close PR contents**

#### **3.5.2.1 Close-pack files**

The close PR MUST include the epic close-pack (canonical filenames):

* audit/EPIC-\<NNN\>\_close\_report.md

* audit/EPIC-\<NNN\>\_MANIFEST.json

Where \<NNN\> is the zero-padded 3-digit epic number (see §0.5.1).

The close PR MUST also include:

* a PASS tokens section (final status; titles only; see §0.2 Baseline PR tokens (titles-only) and the PLAN/CRD machine headers)  
* PASS roster token validity (registry-bound): the PASS tokens section MUST list only canonical acceptance token names that exist in the acceptance token registry. Any unregistered token reference MUST be marked Unknown and MUST NOT be recorded as PASS until registered (or explicitly waived via closure override).

* an explicit verification statement that the close-pack baseline artifacts exist at the canonical filenames listed above

Close-pack presence is a baseline artifact requirement, not a token by default. Convenience copies elsewhere MAY exist for human convenience, but MUST NOT be used for acceptance binding.

#### **3.5.2.2 Core determinism and parity tokens**

The close PR MUST demonstrate core determinism and parity via (titles only):

* DET\_SERIALIZER\_OK

* CLI\_READER\_PARITY\_OK

* TWO\_RUN\_IDENTITY\_OK

#### **3.5.2.3 Index and mirror trio (same PR)**

The close PR MUST update the Evidence Index and machine mirror in the same PR, satisfying:

* EVIDENCE\_INDEX\_UPDATED\_OK

* EVIDENCE\_INDEX\_HASH\_OK

* MACHINE\_MIRROR\_UPDATED\_OK

#### **3.5.2.4 Repo-docs and evidence updates (same PR)**

The close PR MUST update, in the same PR:

* Human Evidence Index: docs/evidence/INDEX.json

* Index hash sentinel: docs/evidence/INDEX.sha256 (hash MUST match bytes of INDEX.json)

* Machine mirror: artifacts/evidence\_index.jsonl

Machine mirror requirements (titles-only; enforceable):

* records-only canonical JSONL

* exactly one trailing LF

* unknown keys rejected

* ASCII field order

* sort-before-write

* single mirror file

* each record has discovered\_physical\_path \+ proof\_anchor to a co-located path-proof

Also required in the close PR (titles-only; as applicable):

* Repo index and acceptance crib notes

* Doc-Delta note (if applicable)

#### **3.5.2.5 A7 tokens (when A7 is in scope — Catalog success route)**

When A7 is in scope for the epic, the close PR MUST satisfy the relevant A7 tokens (titles only), including:

* A7\_GET\_QUOTED\_ETAG\_OK

* A7\_HEAD\_PARITY\_OK

* A7\_304\_OMITS\_CT\_CL\_OK

* A7\_VARY\_AUTH\_AE\_OK

* A7\_ENCODING\_INVARIANCE\_OK

* ENDPOINTS\_CATALOG\_INTERNAL\_OK

* A7\_TRANSPORT\_PROOF\_OK

#### **3.5.2.6 /internal/version tokens (when in scope — ops surface)**

When /internal/version is in scope, the close PR MUST satisfy:

* INTVER\_200\_CTYPE\_JSON\_UTF8\_OK

* INTVER\_HEAD\_PARITY\_OK

* INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK

* INTVER\_200\_NO\_ETAG\_OK

The /internal/version proof surface requires an explicit invariant checklist before emitting any \_OK tokens.

Any remediation guide, QA step, or probe tool that produces governed /internal/version evidence MUST explicitly enumerate and verify the invariants below. It is not acceptable to imply these checks by referencing PF sections only.

Canon-critical invariants (minimum set) are listed below.

* A) Transport

  * GET MUST return 200\.

  * HEAD MUST return 200 and satisfy parity expectations.

  * Conditional requests (If-None-Match, If-Modified-Since) MUST NOT yield 304; they MUST return 200\.

  * Canonical token name for this invariant: INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK.

  * Alias names (for example INTERNAL\_VERSION\_COND\_200\_NO\_304\_OK) are non-canon and MUST NOT be used.

* B) Headers

  * Cache-Control: no-store MUST be present.

  * Content-Type: application/json; charset=utf-8 MUST be present.

  * ETag MUST be absent.

  * Last-Modified MUST be absent.

  * Header capture parsing note (non-blocking diagnostics). Raw header capture files may include non-header diagnostic lines (for example curl warnings). Any parser or reviewer MUST ignore lines that are not the HTTP status line or a Key: value header line. Presence of diagnostic lines is non-blocking as long as the required status line and required header predicates are satisfied.

* C) Body (identity payload)

  * Body MUST be fixed-schema JSON with exactly these keys (no extras): engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id.

  * Body bytes MUST satisfy the canon identity-bytes posture where applicable to the proof surface (canonical bytes, including LF termination).

Token emission gating (no false OK) is listed below.

* A tool MUST NOT emit any \*\_OK token unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run.

* If the run status is FAIL\_TOOLING (or equivalent), the tool MUST NOT emit \*\_OK tokens for invariants that did not pass.

* The tool MUST NOT emit integrity success tokens (for example two-run identity success) unless those checks demonstrably passed on the produced artifacts.

Coupling requirement (anti-mixed-target and anti-redirect drift) is listed below.

* For each probe run, the emitted tokens, captured headers, captured body, and any two-run identity digest MUST refer to the same resolved target/response chain.

* If coupling cannot be established, the run MUST fail and MUST NOT emit \*\_OK tokens.

* When a coupling \+ two-run identity proof log is produced for /internal/version, it MUST be a governed artifact (single log) and must be index and mirror bound in the same PR.

#### **3.5.2.7 A7 artifacts (when A7 is in scope; titles only)**

When A7 is in scope, the close PR MUST include the governed A7 artifacts (titles only):

* Endpoint Catalog file \+ checksum:

  * docs/ENDPOINTS\_CATALOG.json

  * docs/ENDPOINTS\_CATALOG.json.sha256

* Env-gate headers-only proof:

  * artifacts/proofs/endpoints\_env\_gate\_proof.log

* Composite success proof JSON (records-only; PF12 schema-validated):

  * artifacts/proofs/reader\_success\_get\_head\_304.json

Covers:

* success headers for GET / HEAD / 304

* writers and errors posture

* encoding-invariance capture

#### **3.5.2.8 Live QA via harness (required for epic closeout)**

Every epic MUST complete a Live QA stage via a QA harness before it can be considered closeout-ready.

This section is process guidance only. It does not define harness implementation details; those are owned by the Glow QA Guide and the HDE-Mechanics Guide (titles only).

Workflow placement (Close Gate work product). The detailed Live QA plan or runbook (commands, step checks, QA root structure, and evidence landing mechanics) is authored as a separate QA artifact during the Close Gate stage. It MUST NOT be treated as an Epic Plan prerequisite and MUST NOT be embedded into PLAN/CRD or Implementation planning. See §0.4.1 for required Live QA execution deliverables.

Minimum requirements (all epics) are listed below.

Functional proof requirement (functional changes)  
 If an epic changes a functional feature (runtime behavior, user-visible outputs, integration seams, or data flow), the Live QA plan MUST include at least one functional proof step that exercises the changed behavior in the harness and produces governed evidence. Static artifacts alone (schemas, diffs, logs without a proof step) are not sufficient.

* This includes functional changes to CLI surfaces, adapter-to-engine behavior, engine-to-vendor calls, vendor-to-engine handling, and engine-to-user outputs.

* If the epic touches the vendor seam, the plan MUST include at least one vendor-focused PO step that hits the seam and records observable outputs (request signature, response shape, and any user-visible outputs), without leaking secrets.

* If strict closed-rails posture blocks functional proof, the plan MAY open rails explicitly as a bounded exception. The plan MUST name the rails opening, justify it, keep it minimal, and capture it in the evidence artifacts.

* Evidence requirements for the proof step:

  * What was exercised (titles-only description of the functional path)

  * The command or endpoint identity used (and where it is defined)

  * The explicit PASS/FAIL predicate

  * Pointers to the primary evidence file(s)

  * Rails posture (names-only) and any pins required for determinism

* Exemption boundary: truly non-functional-only epics (docs, refactors with no behavior changes, schema-only updates with no runtime behavior changes) MAY omit functional proof, but the exemption MUST be explicitly justified and validated by the IG.

Live QA plan exists (titles-only). The epic MUST have a Live QA plan (runbook) that specifies:

* the QA harness invocation (for example \--epic \<id\> or equivalent)

* closed-rails posture (env pins)

* expected evidence under audit/qa/\<epic-id\>/\<SUBPATH\> (epic-level current-state evidence; per-run nesting is optional and non-canon)

If the epic claims QA Acceptance Tokens, the plan must name the QA ledger artifacts by path. This includes the token/evidence matrix location (titles-only semantics) and any other governed ledgers required for close.

Acceptance-map viability is a Close Gate input. If the Live QA harness produces an acceptance-map viability check, that check MUST be meaningful (not default-PASS) and MUST block epic closeout readiness when it fails; the harness run MUST surface that failure (including influencing the harness exit status) so Close Gate work does not proceed on a false PASS.

Mandatory D0 Discovery artifact and QA RCA summary are present. The epic MUST satisfy the Live QA execution deliverables in §0.4.1:

* a governed D0 Discovery artifact under the epic’s QA tree

* a QA RCA and Doc Delta summary (as part of the close report or as a governed artifact referenced by it)

At least one harness run executed in Codespaces. Before epic closeout, the plan’s harness entrypoint MUST be executed at least once in a GitHub Codespace attached to the canonical repo, producing governed evidence under audit/qa/\<epic-id\>/\<SUBPATH\> (epic-level current-state; optional per-run copies permitted).

Live QA evidence landing is PR-first and parity-clean. Live QA evidence MUST land under governed roots and follow the same-change-set evidence parity rule:

* Live QA artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>

* the index and mirror trio updates (Human Evidence Index, hash sentinel, Machine Mirror) in the same PR

Live QA evidence may land either:

* inside the epic close PR

* in an evidence-only QA PR (see §0.7 and §4.5) that merges before the close PR

Entrypoint regression test exists in CI (no governed evidence writing). Every entrypoint command documented in the Live QA plan MUST have a corresponding CI test that:

* runs the entrypoint (or a logically equivalent variant) under the canonical env pins

* asserts that the expected QA root layout and outputs are created and non-empty

* fails if harness behavior regresses

CI tests MUST NOT be treated as a source of governed evidence and MUST NOT require committing audit/qa/\<epic-id\>/\<SUBPATH\> outputs to the repo.

No QA-only epics that only test themselves. QA-heavy epics must deliver shared value. If an epic’s QA work does not upgrade shared QA tools or harnesses and does not strengthen Live QA coverage across multiple existing surfaces, the PLAN/CRD MUST be returned as non-conforming and re-scoped before approval.

Close Gate check. The close PR MUST confirm that Live QA evidence exists under governed roots and is indexed (Human Evidence Index \+ hash sentinel \+ Machine Mirror), and it must ensure the epic’s close-pack references the existence of this Live QA evidence by title and path (no URLs required).

### **3.5.3 Repo docs sweep (major epics)**

For major epics (for example, HDE-EPIC018), the close PR MUST also include a final repo docs sweep that aligns non-canonical repo docs.

Brings top-level, non-canonical repo docs into alignment. This includes:

* README.md

* CHANGELOG.md

* AGENTS.md

* non-pfcanon files under docs/\*\*

Any operator-facing command blocks in the swept docs MUST follow Copy/paste command safety (0.2 Policy and principles) and MUST be verified and truthy (no dead or misleading commands; default invocation matches CI for check scripts).

If the sweep edits acceptance artifacts or governed evidence wiring, re-run the relevant CI-safe validators and checks and include the pass proof in the close PR packet.

Brings older, epic-specific guidance into line with the current epic’s rails and acceptance outcomes, or clearly retires it. Examples include:

* EPIC011 and EPIC017-only notes

* Alpha and A7-only descriptions

* outdated evidence practices

Does not modify PF-Canon itself. The repo docs sweep MUST NOT modify any PF-Canon docs (for example files under docs/pfcanon/\*\*). PF-Canon remains the single home for normative rules; the repo docs sweep is strictly an implementation-level alignment.

Lives in the close PR. This repo docs sweep is part of the close-out tasks for such epics and is performed in the same close PR that carries:

* the close-pack

* the index and mirror trio

* other close-out evidence

### **3.5.4 ADR block in the close-pack (all epics)**

The close PR MUST ensure that the epic’s close-pack includes a brief ADR block summarizing the key architectural and behavioral decisions made during the epic.

ADR scope constraints (anti-duplication) apply.

* The ADR block MUST NOT restate or attempt to override existing PF-Canon (rails, acceptance tokens, evidence surfaces, or status semantics). If the topic is already governed, cite the governing PF-Canon doc instead.

* If execution is blocked because PF-Canon is missing, ambiguous, or wrong, capture a Doc Delta requirement; ADR content is permitted only to document any temporary local stopgap decision pending canon update.

At minimum, this ADR block MUST:

* use neutral, titles-only references back to PF-Canon, for example:

  * Glow Infrastructure

  * HDE-CLI-API-Vendor-Ref

  * Glow QA Guide

  * HDE Phased Epics

* list each decision as a short item with:

  * a decision label (for example ADR — QA evidence root and directory casing)

  * a one–two sentence statement of the decision

  * the PF documents that should receive the corresponding Doc Deltas (by title only)

Closure override (rare; explicit). If closure is approved by explicit decision override while accepting known QA proof gaps, the ADR block MUST explicitly label the override decision and MUST enumerate each accepted gap (non-blocking) along with the evidence basis for closure and the drain targets (PF documents by title) required to remove the drift for future epics.

No posture-only PASS. Posture-only / TOOLING\_BLOCKED checks MUST NOT be recorded or represented as PASS closure gates. If closure proceeds while a check remains posture-only / TOOLING\_BLOCKED, that exception MUST be handled via the explicit closure override entry above and MUST be scoped to the epic (not reused as default posture for future epics).

Location. The ADR block lives in the close report:

* audit/EPIC-\<ID\>\_close\_report.md

This ADR block is part of the epic’s permanent record. Follow-on epics and doc-only work can then use it to drive PF-Canon deltas.

### **3.5.5 Remediation PR pattern (separate from Live QA)**

Structural remediations that do not change engine behavior MUST be handled as explicit remediation PRs, not buried inside Live QA runs. Examples include:

* directory casing normalization

* path refactors

* relocation of evidence files into governed roots

Separate remediation PRs. Each remediation PR should:

* be tracked by its own card or Build Notes addendum

* be scoped narrowly to the remediation at hand  
* include a minimal evidence pointer block (paths only) that points to:  
  * the remediation delta artifact(s) (patch diff, changed-files list, or equivalent)  
  * the post-remediation validation rerun output or receipt

Live QA may depend on, but not perform, remediation. Live QA plans may depend on such remediation PRs (for example EPIC017 QA evidence is consolidated under audit/qa/hde-epic017/logs/), but Live QA steps themselves MUST NOT perform large-scale structural migrations as part of a PO session.

Close Gate responsibility. The Close Gate for the epic MUST confirm that:

* any required remediation PRs have merged

* the close-pack and Evidence Index and mirror reflect the post-remediation state

Close-pack regeneration rule (no stale close-pack cuts). If any remediation run or remediation PR changes:

* a step status (FAIL\_\* → PASS or similar)

* any governed evidence that the close-pack summarizes or references

then the close-pack artifacts MUST be regenerated after the remediation is complete so they represent the final closure cut.

The Close Gate MUST NOT treat an earlier pre-remediation close-pack as final.

If the close-pack generator depends on a QA ledger or manifest, that input MUST be unambiguous for the closure cut (no duplicate entries for the same logical run or step identity). If the ledger is ambiguous, treat it as a tooling failure and resolve it before generating or accepting the close-pack.

Live QA evidence artifacts should assume those canonical paths, not improvise new ones.

Ops tasks are not remediation PRs. If any remediation requires privileged external actions (service config, secrets/env changes, infrastructure console actions, privileged DB operations), those steps are Ops tasks and MUST be handled as PO-only execution, IA-guided with secret-free, repo-stored evidence. They MUST NOT be represented as CodEx PR work.

Using a distinct remediation PR pattern keeps Live QA focused on behavior and evidence capture, while structural cleanups are performed once, auditable, and referenced by title from HDE Phased Epics and Build Notes.

---

# 4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)

## **4.1 Machine header**

type: PR\_COMMIT\_PLAN  
 epic\_id: "EPIC-?.?"  
 one\_line\_outcome: ""

precommit\_prereqs:  
 reader\_json\_success\_route\_registered: true \# Endpoint Catalog entry exists (internal-only, env-gated)  
 reader\_a7\_matrix:  
 \- "200+STRONG\_ETAG"  
 \- "HEAD\_200\_PARITY"  
 \- "304\_OMIT\_CT\_CL"  
 a7\_vary\_auth\_ae\_ready: true \# Vary: Authorization, Accept-Encoding supported  
 a7\_encoding\_invariance\_ready: true \# ETag & effective Content-Length stable across encodings  
 env\_gate\_proof\_ready: true \# Plan to capture headers proving non-prod endpoints are unreachable in prod  
 writers\_errors\_no\_store\_no\_etag: true  
 ab\_ba\_identity\_ok: true  
 two\_run\_identity\_ok: true  
 narrative\_policy\_ok: "\<if Aux in scope (200/no body/no ETag on suppression)\>"  
 logs\_keys\_only: true  
 indices\_ready\_same\_pr: true \# Human INDEX.json and machine evidence\_index.jsonl updated in same PR; mirror canonical JSONL (UTF-8, sorted keys, compact, one LF), unknown keys rejected; each record includes proof\_anchor to a path-proof file  
 single\_finalization\_scope: "\<precisely what is finalized by this PR (one coherent slice)\>"  
 revert\_concept: "\<simple revert path: single squash commit rollback; no data loss; how to disable feature flag if applicable\>"

## **4.2 Required pre-merge evidence (titles-only; CodEx supplies artifacts)**

premerge\_evidence\_required:

* name: "PR\_OPENED\_OK" \# PR opened by CodEx using epic template; PASS tokens listed in body

* name: "DOC\_DELTA\_PRESENT\_OK" \# Repo docs (indexes/cribs) updated in this PR

* "audit/EPIC-\<ID\>\_close\_report.md" \# Close-pack baseline artifact (required; non-token)

* "audit/EPIC-\<ID\>\_MANIFEST.json" \# Close-pack baseline artifact (required; non-token)

* name: "EVIDENCE\_INDEX\_UPDATED\_OK" \# docs/evidence/INDEX.json updated (titles/paths only)

* name: "MACHINE\_MIRROR\_UPDATED\_OK" \# artifacts/evidence\_index.jsonl present; canonical JSONL (one LF), unknown keys rejected; each record has proof\_anchor to a path-proof file

* name: "EVIDENCE\_INDEX\_HASH\_OK" \# docs/evidence/INDEX.sha256 updated; hash matches INDEX.json bytes

* name: "CLI\_READER\_PARITY\_OK" \# Reader 200 body equals hdctl/glowctl showcompat stdout (LF-terminated)

* name: "TWO\_RUN\_IDENTITY\_OK" \# Two independent runs produce byte-identical bodies and ETag

* name: "A7\_GET\_QUOTED\_ETAG\_OK" \# GET 200 returns strong quoted ETag over LF-terminated canonical body

* name: "A7\_HEAD\_PARITY\_OK" \# HEAD 200 mirrors GET validators; Content-Type \== GET; no body; Content-Length \== length(identity 200 body)

* name: "A7\_304\_OMITS\_CT\_CL\_OK" \# 304 only after prior 200; no body; omits both Content-Type and Content-Length; validators mirror cached GET

* name: "A7\_VARY\_AUTH\_AE\_OK" \# Vary: Authorization, Accept-Encoding present

* name: "A7\_ENCODING\_INVARIANCE\_OK" \# ETag and effective Content-Length stable across accepted encodings

* name: "ENDPOINTS\_CATALOG\_INTERNAL\_OK" \# Catalog internal-only; entries env-gated; non-prod entries unreachable in prod (headers-only env-gate proof)

* name: "WRITERS\_ERRORS\_NOSTORE\_NOETAG\_OK" \# Writers no-store; errors have Content-Type: application/json; charset=utf-8; no ETag

## **4.3 Guidance for PO (CodEx UI)**

If any required governed file or index/mirror update is missing, do not merge. Ask the IA to have CodEx amend the current PR so the missing items land in the same PR before squash-merge.

PF23 consult is not a PR-review input. Do not consult PF23 or treat it as a blocker during PR analysis. If a PF23 statement appears to conflict with PF canon or the approved PLAN/CRD, record a drift item and route it to the Product Owner for adjudication; do not block merge solely on an unadjudicated PF23 conflict.

Verify this PR contains, as required:

* Doc-Delta (repo docs)

* Human Evidence Index update (docs/evidence/INDEX.json)

* Evidence Index hash sentinel (docs/evidence/INDEX.sha256)

* Machine JSONL mirror update (artifacts/evidence\_index.jsonl)

Wait for the Lead Dev gate review (PASS).

On PASS, perform a squash merge, then notify the Scrum Master.

## **4.4 PO approval and commit record**

po\_approval:  
 decision: "APPROVED"  
 notes: ""

commit\_record:  
 pr\_id: ""  
 commit\_id: ""  
 closeout\_evidence\_pointer: "\<pointer to close pack / proof bundle in PR\>"

## **4.5 PR template — evidence-only QA**

For PRs whose sole purpose is to verify evidence and transport posture without changing production code. Use titles only for cross-doc references. Keep the human Evidence Index \+ hash sentinel \+ machine mirror in the same PR.

Paste this as the PR body and fill in:

### Evidence-only QA — \<short scope\> (EPIC-\<ID\> QA)

### Summary

* Purpose: \<one paragraph describing what is being verified and why\>

* Scope: evidence-only; no production code changes

* Determinism pins set for all determinism-sensitive captures and CI: LC\_ALL=C, LANG=C, TZ=UTC

  ### Artifacts included (titles and repo-relative paths only)

  #### Indexes (must update in the same PR)

* Evidence Index (human) — docs/evidence/INDEX.json

* Evidence Index hash sentinel — docs/evidence/INDEX.sha256

* Machine Evidence Index (JSONL) — artifacts/evidence\_index.jsonl (+ artifacts/evidence\_index.jsonl.sha256)

  #### Endpoint Catalog (A7 proof surface; Catalog-only)

* Catalog file (records-only) — docs/ENDPOINTS\_CATALOG.json

* Catalog checksum — docs/ENDPOINTS\_CATALOG.json.sha256  
  * Note: The docs/ENDPOINTS\_CATALOG.json.sha256 sidecar MUST reference docs/ENDPOINTS\_CATALOG.json (repo-relative) so `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256` can be run from repo root.

* Endpoint Catalog snapshot (titles-only) — artifacts/reader/endpoints\_snapshot.json

* Env-gate proof (headers-only) — artifacts/proofs/endpoints\_env\_gate\_proof.log

  #### A7 proofs on a cataloged JSON success route (headers-only)

Note: If these proof artifacts are generated by tests, artifact emission MUST be gated behind an explicit flag (for example HDE\_WRITE\_A7\_PROOFS) so default test runs do not write files.

* GET (200) — artifacts/proofs/success\_get.txt

* HEAD (200) — artifacts/proofs/success\_head.txt

* 304 — artifacts/proofs/success\_304.txt

* Writers/errors posture — artifacts/proofs/success\_writers\_errors.txt

* Encoding-invariance — artifacts/proofs/encoding\_invariance.txt

* Composite success proof JSON — artifacts/proofs/reader\_success\_get\_head\_304.json  
   (records-only; validated against PF12 composite proof schema)

  #### Ops — rails refusal proof (closed-rails)

* Refusal probe capture — artifacts/proofs/ops\_refusal\_proof.txt

  #### Ops — /internal/version coupling proof (if in scope)

* /internal/version two-run identity \+ coupling proof — artifacts/ops/internal\_version/two\_run\_identity.log

Note: single governed log artifact; bound under existing /internal/version token set; indexed \+ mirrored in the same PR when produced/updated.

Note: headers → blank line → LF-terminated numeric-free JSON body; titles-only routing to HDE-Governance for policy/tokens and HDE-Schemas & Artifacts for indexing/mirror rules.

#### CLI / Reader parity & determinism

* CLI parity set (AB/BA/summary) — artifacts/cli/ab.json; artifacts/cli/ba.json; artifacts/cli/summary.json

* Reader vs CLI parity diff (expected empty) — artifacts/cli/showcompat/reader\_vs\_cli.diff

* CLI showcompat stdout (LF-terminated; non-empty) — artifacts/cli/showcompat/stdout.json

* CLI two-run identity log — artifacts/cli/showcompat/two\_run\_identity.log

* Preimage recompute log — artifacts/cli/showcompat/preimage\_recompute.log

  #### DB evidence (if in scope)

* DDL fingerprint — artifacts/db/ddl\_fingerprint.json

* Grants snapshot — artifacts/db/grants.txt

* Schema/search\_path echo — artifacts/db/check\_schema.txt

* Connection env selection proof — artifacts/db/conn\_env\_selection.log

* Dev connectivity snapshot (PF10-A) — artifacts/runtime/env\_connectivity.snapshot.json

  ### PASS tokens (check what applies)

  #### Index/mirror gates (same PR)

* PR\_OPENED\_OK

* DOC\_DELTA\_PRESENT\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* EVIDENCE\_INDEX\_HASH\_OK

* MACHINE\_MIRROR\_UPDATED\_OK

  #### Determinism & parity

* CLI\_READER\_PARITY\_OK

* TWO\_RUN\_IDENTITY\_OK

  #### A7 (Catalog-only)

* ENDPOINTS\_CATALOG\_OK

* ENDPOINTS\_CATALOG\_INTERNAL\_OK

* A7\_GET\_QUOTED\_ETAG\_OK

* A7\_HEAD\_PARITY\_OK

* A7\_304\_OMITS\_CT\_CL\_OK

* A7\_VARY\_AUTH\_AE\_OK

* A7\_ENCODING\_INVARIANCE\_OK

* A7\_TRANSPORT\_PROOF\_OK

  #### Writers/errors posture

* WRITERS\_ERRORS\_NOSTORE\_NOETAG\_OK

  #### QA process (branches)

* QA\_EVIDENCE\_ONLY\_OK

* QA\_CI\_DIFF\_SCOPED\_OK

  #### Close-pack (use N/A for QA if not an epic close)

* Close-pack baseline present (non-token) — audit/EPIC-\<ID\>\_close\_report.md; audit/EPIC-\<ID\>\_MANIFEST.json

  ### Human↔Machine parity checks

* 1:1 parity between Appendix D entries and mirror records

* Mirror JSONL is canonical: UTF-8, compact, exactly one LF; ASCII field order; sort-before-write; single mirror file

* Unknown keys rejected in mirror schema

* Each record has discovered\_physical\_path and proof\_anchor to a path-proof stored with the artifact

* All listed paths exist and are repo-relative; governed locations only (artifacts/**, docs/**)

  #### Diff-scoped CI status at time of landing

catalog\_schema: pass|fail  
 domain\_closure: pass|fail  
 topology: pass|fail  
 arrays\_as\_sets: pass|fail  
 canonical\_json: pass|fail  
 mirror\_schema: pass|fail \# CI\_CHECK\_MIRROR\_SCHEMA\_OK  
 final\_lf: pass|fail \# CI\_CHECK\_FINAL\_LF\_OK  
 env\_pins: pass|fail \# LC\_ALL=C, LANG=C, TZ=UTC

#### Reviewer checklist

* A7 proofs run only on a cataloged JSON success route (not /internal/version)

* Catalog file \+ .sha256 present; env-gate proof captured

* GET, HEAD, and 304 captured; 304 omits both Content-Type and Content-Length

* Vary: Authorization, Accept-Encoding present on success route

* Encoding-invariance of identity (ETag) and effective length proven

* Composite success proof JSON present and schema-validated (PF12)

* Writers are no-store; error responses have Content-Type: application/json; charset=utf-8 and no ETag

* Reader and CLI share a single emitter and produce byte-equal bodies for identical inputs

* Two-run identity holds for body and ETag

* Evidence Index and hash sentinel updated in this same PR

* Machine mirror updated in this same PR and passes schema checks (records-only, unknown-key reject, ASCII order, sort-before-write, single file)

  #### Notes

Cross-doc references (titles only):

* Governance and A7 policy — HDE-Governance

* Evidence mirror and artifacts — HDE-Schemas & Artifacts

* CLI and Reader contract — HDE-CLI-API-Vendor-Ref

* Math and serializer rules — HDE-Math-Spec

## **4.6 PR review pack template — provenance, diff review, RCA, and pass proof**

Use this template for PRs that require reviewer-facing analysis (remediation sequences, non-trivial diffs, or any PR that produced CI failures or bugs). This is a review artifact and does not replace the close pack.

Rules:

* Titles-only cross-doc references (no version numbers in prose).

* Repo-relative paths only.

* For each non-obvious claim, include:

  * Source: \<where the claim originates\>

  * Evidence pointer: \<where the supporting evidence can be found\>

* If the PR has multiple attempts or remediations, Provenance, RCA, and Requirement Satisfaction Crosswalk are REQUIRED.

* Doc Deltas is ALWAYS INCLUDED (PF-Canon only).

* Evidence Print is REQUIRED.

### **PR Review Pack — \<PR ID\> (EPIC-\<ID\>)**

Fill the sections below. Use DR-\#\#\#, F-\#\#\#, and RCA-\#\#\# numbering as needed.

### **Review Summary**

* Purpose: \<what this PR changes and why\>

* Scope: \<what is in scope and what is explicitly out of scope\>

* Current state: \<PASS | Non-passing | Remediation required\>

* Scope drift check: \<call out any cross-epic or tooling changes and justify them\>

* Key risks: \<list residual risks that remain after this PR\>

### **Provenance (REQUIRED for remediation sequences)**

* Provenance lineage: \<Original → Remediation 1 → Remediation 2 → Remediation 3\>

* Attempt record (repeat per attempt):

  * Attempt label: \<Attempt 0 | Remediation 1 | Remediation 2 | Remediation 3\>

  * Change summary: \<what changed in this attempt\>

  * CI status summary: \<PASS/FAIL, and what failed if not PASS\>

  * Tests run summary: \<what was run and why it is the right suite\>

  * Evidence artifacts changed: \<what artifacts were created or updated\>

  * Source: \<Implementation Plan section or other governing input\>

  * Evidence pointer: \<PR comment, commit, diff hunk, artifact path\>

### **Diff Review (REQUIRED; primary technical review)**

DR-001

* Change summary: \<one change\>

* Risk assessment: \<Low | Medium | High\>

* Why it matters: \<why a reviewer should care\>

* Evidence pointer: \<diff path and hunk; preserve \+ and \- markers if quoting a diff\>

* Approved Plan linkage: \<approved plan section heading or acceptance token names\>

Repeat DR-\#\#\# as needed.

### **Findings**

F-001

* Observed: \<what was observed\>

* Why it matters: \<why it matters\>

* Source: \<where the observation originates\>

* Evidence pointer: \<diff hunk, log, test output, artifact path\>

Repeat F-\#\#\# as needed.

### **RCA (REQUIRED when any CI failure or bug occurred)**

RCA-001

* A) Failure statement: \<quote the failure as it appeared\>

* B) Where it occurred: \<attempt number and context\>

* C) Root cause: \<what actually caused it\>

* D) Fix progression: \<what changed across attempts to resolve it\>

* E) Fix verification: \<how the fix was proven\>

* Residual risk: \<what remains, and why it is acceptable or what follow-up is needed\>

Common RCA checks:

* If the PR introduces or modifies an evidence-path validator (any code that loads `artifacts/evidence_index.jsonl` or interprets `discovered_physical_path`), verify it rejects absolute paths, traversal segments like `..`, and any resolved out-of-root path. It MUST also enforce that each JSONL line parses to a JSON object (dict) and that the resulting `discovered_physical_path` exists under repo root.

* If your tests emit governed artifacts, artifact emission MUST be gated behind an explicit flag (no default emission on normal runs).

* If a PR updates evidence/INDEX.jsonl, it MUST also update evidence/INDEX.sha256 and preserve canonical JSONL formatting and stable ordering.

* If a .sha256 sidecar is updated, verify it references the correct repo-relative target path and that `sha256sum -c <sidecar>` works from repo root.

### **Requirement Satisfaction Crosswalk (REQUIRED for remediation sequences)**

* Requirement: \<requirement label and short statement\>

* Status by attempt: \<Attempt 0: FAIL | Remediation 1: PARTIAL | Remediation 2: PASS\>

* Evidence pointer: \<where the requirement is proven\>

Repeat per requirement.

### **Doc Deltas (PF-Canon only; ALWAYS INCLUDED)**

* Doc: \<PF doc title\>

* Section: \<section heading\>

* Delta summary: \<what should change\>

* Rationale: \<why the doc needs this change\>

* Evidence pointer: \<where the supporting evidence can be found\>

Repeat per delta.

### **Evidence Print (REQUIRED; PASS PROOF)**

A) Tokens satisfied (names-only; do not invent)

* \<TOKEN\_NAME\_1\>

* \<TOKEN\_NAME\_2\>

If no PASS tokens are claimed by name in this PR artifact, state: No PASS tokens claimed by name in this PR artifact.

B) Evidence artifacts produced or updated (repo-relative paths)

* Path: \<path\>

* Type: \<what the artifact is\>

* Key proof facts: \<what the artifact proves\>

* sha256: \<sha256 if applicable\>

* Evidence pointer: \<where to find the artifact in the PR\>

Repeat per artifact.

C) Test and CI proof

* Command: \<exact command\>

* Pass indicator: \<what “PASS” looked like\>

* Evidence pointer: \<where the output is recorded\>

Evidence hygiene: if you cite multiple runs, keep pass counts and durations consistent, or label them explicitly as distinct runs.

D) PR analysis routing (titles only)

When adjudicating PR correctness, route claims to the owning PF homes (titles only) and do not use PF23 as a PR-review input:

* Governance and tokens — HDE-Governance

* QA posture and acceptance — Glow QA Guide

* CLI and Reader contract — HDE-CLI-API-Vendor-Ref

* Schema and artifact rules — HDE-Schemas & Artifacts

* Build workflow and checks — HDE-Build Checklist

* Mechanics and semantics — HDE-Mechanics Guide

* Architecture and system boundaries — HDE-Architecture

* Infra and environments — Glow Infrastructure

* Math and serializer rules — HDE-Math-Spec

* Epic delivery process — Epic Process Guide

## **4.7 PR review pack template — docs-only PR (Lead Dev gate)**

Use this variant when a PR changes repo docs only (no runtime code changes). This is a review-pack format (lead gate), not a PR body template.

Rules:

* Docs-only does not mean evidence-free. If the docs assert contract or behavior (CLI semantics, tokens, governed artifacts, evidence routes), the review pack MUST cite the evidence basis (canon pointer, governed artifact, or new test/proof output).

* If no CI or test proof is present in the PR bundle, the review pack MUST state that verification was diff-only and record the search method used to look for pass indicators.

Template:

### **Review Summary (required)**

* Scope: \<what docs changed, and why\>

* Claim surfaces impacted: \<CLI behavior, tokens, governed artifacts, evidence index or mirror semantics, QA harness behavior\>

* Risk assessment: \<Low | Medium | High\> (docs-correctness drift is the default risk)

* Verification posture:

  * Evidence-backed via canon pointer: \<title-only pointer(s)\>

  * Evidence-backed via governed artifact: \<repo-relative path(s)\>

  * Evidence-backed via new proof in this PR: \<what was run, and where the output is recorded\>

  * Diff-only: \<explicitly state that no CI/test output was captured in the PR bundle\>

### **Diff Review (required)**

DR-001

Change summary: \<what changed\>

Risk assessment: \<Low | Medium | High\>

Why it matters: \<what could be wrong if this is wrong\>

Evidence pointer: \<diff hunk or file path; cite existing governed evidence if available\>

Approved Plan linkage: \<if applicable\>

\[Repeat DR-00N as needed\]

### **Findings (required)**

* \<List doc correctness risks, contradictions, missing evidence links, and any required follow-ups\>

### **Evidence Print (PASS PROOF; required)**

A) Tokens satisfied (names-only; do not invent):

* \<None explicitly claimed as satisfied in PR artifacts\> or \<TokenName\_1\>, \<TokenName\_2\>

B) Evidence artifacts produced or updated:

* Docs changed (repo-relative): \<list paths\>

* Canon pointers used (title-only): \<list\>

* Governed evidence paths cited: \<list\>

Key proof facts:

* \<Bullet the facts that are actually supported by the cited evidence\>

C) Test and CI proof:

* If present, list the concrete CI or test outputs captured in the PR bundle (or governed evidence paths).

* If not present, record the verification limit:

  * Verification posture: Diff-only (no captured CI/test output in PR bundle)

  * Search method (example format):

    * Searched PR artifacts for pass-indicator strings: "passed", "exit 0"

    * Result: \<0 hits | N hits\> (include the string set and scope you searched)

Decision:

* PASS | PASS WITH CAVEATS | FAIL / BLOCKERS

# 5\) Quick reference: where code exchange is allowed

Plan and CRD. Propose/refine code-capsules.

Implementation Plan (IP). Finalize the capsule list; package verbatim components/schemas for CodEx. After IP approval, capsules become immutable. CodEx may apply scoped fixes but must record every change in the Detailed Change Report.

Build. IA provides instructions \+ verbatim materials. CodEx can read PF docs. Even so, paste execution-critical material verbatim to keep an unambiguous in-session reference (formats, schemas, exact token names, commands, and artifact paths).

PR & Commit. CodEx opens the PR automatically; no new code exchange beyond what CodEx built. PO performs squash merge after Lead Dev gate passes.

Escalation. PO may direct CodEx to inspect code/processes at any time. IA keeps docs synchronized (Doc-Delta \+ indices).

# 6\) PHASE EXIT DISCIPLINE (ALCHEMICAL PHASES)

This section defines how the Product Owner and Lead Developer decide that an alchemical phase is ready to exit for planning purposes.

It does not redefine what the phases are; that remains in Glow Development Philosophy and 7 Phases of Alchemical Engineering (titles only). It does not move epic records, issues, or task status out of HDE Phased Epics or HDE-Build Checklist; those remain the single homes for phase and epic data.

## **6.1 When this section applies**

Use this section whenever the PO and Lead Dev are asking:

* “Are we done enough with this phase to move the next epics into the next phase?”

* “Can we stop opening new epics tagged with this phase and carry the remaining work forward as debt?”

If the checks below cannot be evaluated from PF-Canon and governed evidence, the phase exit decision is blocked-by-spec, per §0.6.5. Do not treat gut feel or informal summaries as sufficient.

## **6.2 Phase exit is canon-first and evidence-backed**

Before declaring a phase exit-ready, the PO and Lead Dev MUST perform a canon inventory, exactly as in §1.1.1, with explicit attention to:

* HDE Phased Epics: phase, epics, D-goals, exclusions, tracked issues, and cross-epic issues.

* HDE-Build Checklist: phase tasks and statuses (Done / Partial / Consolidation pending / Not done / Won’t Do).

* HDE-Schemas & Artifacts and HDE-Build Checklist: Evidence Index, machine mirror, close packs, and governed roots only.

If any of the later checks (close-out epic, foundations, Partial/Consolidation rows, tracked issues) cannot be evaluated from this canon inventory, the phase MUST NOT be treated as exit-ready.

## **6.3 Close-out epic required**

Each phase MUST have at least one close-out epic in that phase that satisfies all of the following:

* The epic is Status: Done in HDE Phased Epics for that phase, with D-goals and exclusions clearly recorded.

* Its tokens and evidence roster for D-goals is complete in HDE Phased Epics and is consistent with the epic’s acceptance map and manifest.

* The epic’s close pack:

  * lives under governed roots (for example audit/EPIC-\<ID\>\_close\_report.md and audit/EPIC-\<ID\>\_MANIFEST.json)

  * is indexed in both:

    * the human Evidence Index docs/evidence/INDEX.json

    * the machine mirror artifacts/evidence\_index.jsonl

  * is consistent with HDE-Schemas & Artifacts and HDE-Build Checklist (titles only).

If no epic in the phase meets these conditions, the phase MUST NOT be considered exit-ready.

## **6.4 Foundation tasks: Not done vs explicit decisions**

HDE-Build Checklist is the single home for phase tasks.

For the phase under review, all foundation tasks defined for that phase in HDE-Build Checklist MUST be:

* marked Done, or

* explicitly re-scoped or dropped, as below.

Any Not done rows for that phase MUST be resolved one of two ways:

* Re-scoped: the work is moved into a later phase by recording it explicitly in one or more future epics in HDE Phased Epics (new scope).

* Won’t Do: the work is not going to be done and is recorded as Won’t Do in HDE Phased Epics with a short rationale and reflected in HDE-Build Checklist.

A phase MUST NOT be treated as exit-ready if there are foundation rows that are still Not done in HDE-Build Checklist without a matching re-scope or Won’t Do decision in HDE Phased Epics.

## **6.5 Partial / Consolidation pending rows as controlled debt**

For the phase under review, Partial and Consolidation pending rows in HDE-Build Checklist are treated as debt, not blockers, only if:

* The notes for those rows show that the remaining work is enhancement, tuning, or consolidation, not missing foundational behavior.

* Each such row is explicitly carried by one of:

  * a cross-epic Outstanding Issue or similar issue entry in HDE Phased Epics for that phase, or

  * a future epic record in HDE Phased Epics that names the work as Existing work / Debt to absorb in its scope.

If a Partial or Consolidation pending row has no such carrier, treat it like a missing foundation task: resolve it or re-scope it before calling the phase exit-ready.

## **6.6 Tracked issues must be disposed of, not dropped**

Before treating a phase as exit-ready:

* Every Done epic in that phase in HDE Phased Epics MUST list its tracked issues.

* Every tracked issue for those epics MUST record one of:

  * Completed under \<EPIC\>: resolved within that epic.

  * Carried forward to \<EPIC\>: moved into a later epic’s scope.

  * Promoted to ISSUE-XXX: promoted to a cross-epic or cross-phase issue with its own identifier.

  * Explicitly dropped (with rationale): intentionally not carried forward, with a short explanation.

If a Done epic has real, unresolved issues that are not covered by one of these dispositions, phase exit is not allowed. Treat that as a spec gap and resolve it before re-evaluating.

## **6.7 Phase exit as a planning decision**

When §6.3–§6.6 are satisfied, phase exit is treated as a planning decision only:

* It says the core aim of this phase has been achieved and its remaining work is tracked as debt.

* It does not say all work tagged with this phase is finished forever.

Any remaining work that properly belongs to this phase MUST be handled as:

* cross-epic or cross-phase issues recorded in HDE Phased Epics, or

* explicit inputs to the next phase’s epics (for example carry sampler tuning from Dissolution into Separation error-envelope work).

Once a phase is declared exit-ready under this section:

* New epics MUST be opened in the next phase, not the old phase.

* Those new epics MUST name the carried-forward work in their scope, so that acceptance and evidence for that work live entirely in the new phase.

This follows the instruction in Glow Development Philosophy to avoid over-tuning and silent drift and the expectation in 7 Phases of Alchemical Engineering that phases do not mix: once a phase’s core aim is achieved and its debt is explicit, planning moves forward, and that phase stops accumulating new epics.

## **6.8 Epic retrospective and closure evidence snapshot (recommended)**

Purpose: After the epic is functionally complete (and before final phase-exit decisions), produce a short retrospective and a closure evidence snapshot that makes evidence posture and remaining gaps explicit for the Lead.

This is not a replacement for the epic close report. Use it as an input to the close report, or attach it as a referenced artifact in the PR bundle.

Template:

### **Implementation Report (what happened in the repo)**

* PR or step breakdown: \<PR01, PR02, PR03, PR04, or equivalent steps; 1 to 3 bullets each\>

* Major surfaces affected: \<CLI | API | DB | evidence | QA harness | docs | other\>

* Evidence inventory (what exists): \<list the concrete governed artifacts and where they live\>

### **Evidence gaps (if any; label Unknown if you cannot verify)**

For each gap, record:

* Gap: \<what is missing or not verified\>

* Status: \<Unknown | Missing | Ambiguous\>

* What would prove it: \<the minimal test, proof, or artifact that would close the gap\>

### **Retrospective (Process)**

* What went well: \<process wins\>

* What did not go well: \<process gaps, including evidence posture gaps\>

* What we learned (Process): \<actionable changes to make next time\>

### **Retrospective (Application/System) (optional)**

* What we learned about the system: \<technical insights\>

* Known remaining risks or debt: \<explicit list\>

### **Closure Evidence Snapshot (for Lead decision)**

6.1 Evidence produced:

* \<List the evidence artifacts that exist and are ready for audit\>

6.2 Evidence missing or ambiguous:

* \<List missing or ambiguous evidence, and the impact\>

6.3 Open closure items or Lead questions:

* \<What must be decided, accepted, or scheduled before closure\>

# Appendices

## **Appendix A — Large Schemas & Assets (CodEx constraints)**

### **Purpose**

Define how to include large schemas or assets when content is too large to paste inline or when the workflow cannot rely on file attachments. This appendix preserves ownership, auditability, and single-home discipline while keeping execution mechanical and repeatable.

### **Constraints (facts)**

* CodEx can read PF docs, but may not have reliable access to large external assets via attachment workflows. Execution-critical formats and small schemas should still be pasted inline by the IA to keep an unambiguous in-session reference.

* CodEx cannot accept file uploads as part of the build interaction; only IA-provided inline text or snippets and repo contents are used during build.

* Only the Product Owner (PO) may load large files into the repo or PR branch when needed. Agents do not run git and do not create PRs.

* CodEx may adapt within scope but must report every change in the Detailed Change Report.

* Governed locations only. Assets and evidence must live under artifacts/\*\* and docs/\*\*. Transient or generator paths are disallowed.

* Single-PR parity. Repo docs (Doc-Delta), the human Evidence Index (docs/evidence/INDEX.json), the Evidence Index hash sentinel (docs/evidence/INDEX.sha256), and the machine mirror (artifacts/evidence\_index.jsonl) must be updated in the same PR when assets are introduced or moved. If the CodEx UI cannot include doc edits, the IA provides verbatim text in the same PR body for CodEx to commit.

* Mirror hygiene (PF12). The mirror is records-only canonical JSONL (UTF-8, compact, exactly one LF), unknown-keys rejected, ASCII field order, sort-before-write, single mirror file; each record includes artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, and a proof\_anchor pointing to a co-located path-proof.

### **Roles & responsibilities**

#### **Lead Dev / IA**

* Prepare inline materials (formats, small schemas, snippets).

* When assets are too large for inline use, create an Asset Draft Pack (fields below) for the PO to load.

* Ensure the CodEx-opened PR captures Evidence Index, hash sentinel, mirror updates, and single-home pointers. Avoid separate docs-only PRs.

#### **Product Owner**

* Load the Asset Draft Pack files into the CodEx PR branch at the specified targets.

* Confirm the CodEx-opened PR and, after Lead Dev gate passes, squash-merge.

#### **CodEx**

* Can read PF docs, but the IA SHOULD still paste execution-critical formats and small schemas or snippets inline to keep an unambiguous in-session reference and reduce drift.

* Uses IA-provided inline materials and repo contents during build.

* Proposes scoped adjustments; lists every change in the Detailed Change Report (files added, modified, removed; deviations and improvements).

### **When to use an Asset Draft Pack**

Use a pack when any required artifact cannot reasonably be pasted inline for CodEx (e.g., large JSON or YAML schemas, binaries, long fixtures).

### **Asset Draft Pack — minimal fields**

Paste verbatim to the PO and attach in the PR body; the PO loads these files to the PR branch.

asset\_pack:  
 epic\_id: "EPIC-?.?"  
 owner: "IA or Lead Dev"  
 assets:  
 \- asset\_id: "schema\_user\_profile\_v3"  
 title: "User Profile Schema v3"  
 repo\_target\_location: "\<path/inside/repo\>"  
 size\_bytes: 123456  
 sha256: "\<64-hex\>"  
 license\_note: "\<source/license or 'internal'\>"  
 single\_home\_category: "Architecture" \# route by category title only  
 notes: "Consumed by component X; CodEx will assume this location."

### **Guardrails**

* No secrets or PII. Include license and source.

* Exactly one single home per concept; route by category title only, not by version numbers.

* Keep paths repo-relative and stable; list titles and paths in the human Evidence Index.

* For governed assets, add a mirror record (records-only JSONL) with a proof\_anchor to a path-proof stored alongside the asset.

### **Flow (high level)**

* Lead Dev → IA: approve scope; decide inline versus Asset Pack.

* IA → CodEx: send inline materials; name target paths for large assets.

* PO: load the Asset Pack at the target paths in the CodEx PR branch.

* CodEx: build & test; if something is missing, switch to planning mode and note stubs in the Detailed Change Report.

* IA: review the change report; request adjustments or approve.

* PO: confirm the CodEx-opened PR, then squash-merge after the Lead Dev gate passes.

* Docs & evidence: IA ensures Doc-Delta, human Evidence Index \+ hash sentinel, and machine mirror reflect the final assets in the same PR.

### **Planning mode (CodEx)**

Use to propose file trees, stub schemas, and integration points; surface gaps early. IA decides what to paste inline versus pack; planning output is advisory.

### **Acceptance and drift guards (titles only; tokens live in Governance)**

* Evidence parity (same PR): EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK.

* PR posture: PR\_OPENED\_OK, DOC\_DELTA\_PRESENT\_OK.

* Report completeness: the Detailed Change Report lists every file added/modified/removed and every deviation from IA instructions.

* No surprises: if an asset was not present at build time, CodEx records a stub; IA reconciles before close.

## **Appendix B — Remediation Implementation Guides (DEV/OPS only)**

### **Purpose**

Define the canonical structure and step schema for Remediation Implementation Guides used for escalations and remediation execution.

### **Scope**

This appendix applies to Remediation Implementation Guides only. It does not change Live QA plan formats.

### **Allowed step types (only)**

A Remediation Implementation Guide MUST use only two step types:

* DEV

* OPS

No other step types are permitted (no QA, DOC, REVIEW, or verification-only steps).

### **Verification embedding requirement**

All verification MUST be embedded inside the owning DEV or OPS step.

Verification MUST produce concrete, repo-stored evidence outputs (paths and filenames specified in the step).

Verification MUST NOT be separated into a standalone verification step.

### **OPS posture linkage**

OPS steps in remediation guides MUST comply with the Ops task policy in §0.2 (PO-executed, IA-guided, not CodEx PR work, secret-free evidence, lowercase audit paths).

### **Strict lane separation**

A step labeled DEV MUST contain only DEV actions.

A step labeled OPS MUST contain only OPS actions.

If a DEV action depends on an OPS output (or vice versa), the producing step MUST come first and the dependent step MUST declare its dependency explicitly (see Dependency-line rule below).

### **Dependency-line rule (locked)**

If a step depends on outputs produced by a prior step in the other lane, the dependent step MUST include exactly one cross-lane dependency line in this exact form:

Inputs needed from Step S\<N\> during implementation: \<exact items\>

Rules for this line:

* S\<N\> MUST be the actual producing step ID (no placeholders such as Sx).

* The line MUST appear exactly once in the dependent step.

* The line MUST NOT be duplicated, nested, or prefixed by an alternate label.

* If there is no cross-lane dependency, the line MUST be omitted (do not include placeholders).

## **Appendix C — Remediation Task Plans (DEV PRs \+ OPS tasks)**

### **Purpose**

Define the canonical structure and approval gates for Remediation Task Plans that combine DEV PR work and OPS procedures.

### **Scope**

This appendix applies to remediation task plans submitted for approval. It does not change Live QA plan formats.

### **Task model (locked)**

A remediation task plan MUST contain only two task types:

* DEV tasks are PRs only and MUST be enumerated as PR-01, PR-02, PR-03 (continue as needed) (no mixed-task steps).

* OPS tasks are PO-run procedures only and MUST be enumerated as OPS-01, OPS-02, OPS-03 (continue as needed) (no mixed-task steps).

Each task MUST declare its intent as exactly one of:

* DISCOVERY

* CHANGE

Cross-lane dependencies (locked line). If a task depends on outputs produced by a prior task in the other lane, the dependent task MUST include exactly one dependency line in this exact form:

Inputs needed from Task \<ID\> during implementation: \<exact items\>

Placeholders (for example TBD, to be determined, Sx) in this line are a mechanical blocker.

### **Execution-ready gate (normative)**

A remediation task plan submitted for approval MUST be execution-ready:

* every task is runnable as written by its assigned actor (PO for OPS; CodEx for DEV PRs)

* there are no missing inputs, no missing outputs, and no ambiguous success criteria

### **Approval gate scope (tight)**

For remediation task plans, approval MUST focus on:

* correct task model (OPS vs DEV; DISCOVERY vs CHANGE; no mixed tasks)

* correct sequencing and explicit cross-lane dependencies

* concrete deliverables (lowercase paths \+ filenames)

* concrete verification success criteria (what done means)

Not approval blockers: Detailed command lines and step-by-step failure handling are not required as plan-approval conditions.

### **Evidence posture remains non-negotiable (in-flight detail allowed)**

In-flight operational detail is allowed during execution (OPS command selection, exact CLI flags, procedural failure handling), as long as evidence posture remains intact.

Even when commands and failure handling are developed in flight, OPS execution MUST still capture (as repo-stored artifacts under lowercase audit paths):

* the exact commands actually run (verbatim)

* stdout/stderr \+ exit code (or equivalent output)

* the produced artifacts at the declared output paths

* deviation notes explaining why a different command/flag was used

In-flight flexibility MUST NOT permit:

* changing governed artifact locations or filenames

* introducing new governed files without explicitly stating indexing/mirror intent

* indexing remediation-only diagnostics into governed indices/mirror

### **Mechanical blockers (auto-reject if present anywhere in the plan)**

* Any PR-xx task missing a paste-ready CodEx Prompt embedded inside that task.

* Any task that mixes DEV \+ OPS work in a single task.

* Any task output specified only as a directory. Deliverables MUST be concrete file paths including filenames (for example audit/qa/\<epic-id\>/\<task-id\>/\<filename\>), and directory names MUST be lowercase ASCII.

* Any cross-lane dependency missing the exact dependency line, or using non-concrete exact items.

* Any task missing explicit verification success criteria (what done means and how it is recognized from produced artifacts).

### **Exact filenames rule (Evidence Index \+ mirror \+ path-proofs)**

Any remediation task plan that includes tasks touching governed evidence indices/mirrors MUST explicitly name the exact index \+ path-proof filenames as task outputs and as embedded verification checks (inside the owning DEV/OPS task; not as standalone verification-only tasks).

### **Canonical quick reference (use verbatim when applicable)**

Evidence index (human-readable):

* docs/evidence/INDEX.json

* docs/evidence/INDEX.sha256

* docs/evidence/INDEX.json.path\_proof.txt

* docs/evidence/INDEX.sha256.path\_proof.txt

Evidence index mirror (machine-readable):

* `artifacts/evidence_index.jsonl`

* `artifacts/evidence_index.jsonl.path_proof.txt`

* `artifacts/evidence_index.jsonl.sha256`

* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Path-proof artifacts are co-located siblings: \<file\>.path\_proof.txt sits next to \<file\>. Plans MUST NOT relocate path-proofs into alternate directories.

If a plan proposes a new file under governed surfaces, it MUST state whether it is intended to appear in the indices/mirror. Absence of that statement is a blocker.

### **Portability vs provenance (non-PF evidence)**

Remediation task plans may include a short Evidence inventory reviewed (non-PF) list for provenance, but MUST NOT require the reader/executor to open external files to execute the plan.

If a remediation plan depends on any non-PF fact (command outputs, headers, error strings, observed file paths, status lines), the plan MUST embed that fact directly in the document as a short quote or precise paraphrase inside an Observed Evidence Snapshot section.

If an Artifact Map is included, it MUST explicitly label non-PF inputs as provenance only; not required to execute. Otherwise the non-PF input is treated as an execution dependency and becomes a portability blocker.

When a non-PF observation drives a branching decision, the plan MUST include:

* the observation to look for (exact string/status/shape)

* the decision rule

* the output artifact path where the observation is captured (file path including filename; lowercase directory names)

### **Canonical Remediation Task Plan Template (paste-ready)**

#### **Artifact Map**

* Inputs (non-PF): provenance only; not required to execute

* Output: Remediation Task Plan (for approval)

#### **Observed Evidence Snapshot (self-contained; non-PF)**

* Evidence excerpts required for execution (quotes or precise paraphrases only)

#### **Task Overview**

* Task ID

* Task name

* Task type (DEV/OPS)

* Task intent (DISCOVERY/CHANGE)

* Owner/role

* Depends on

* Cross-lane dependency

* Outputs

#### **Task Details (repeat per task)**

Task ID:

* Task name:

* Task type (DEV or OPS):

* Task intent (DISCOVERY or CHANGE):

* Owner/role:

* Preconditions:

* Inputs:

* Actions (what-not-how; execution detail may be developed in flight for OPS):

* Outputs (required; concrete paths \+ filenames; lowercase directory names):

* Verification (required; success criteria and what artifacts prove done):

* Evidence capture (required for OPS): where commands/output/deviations are recorded (paths \+ filenames; lowercase directory names):

Include the dependency-line rule exactly once when cross-lane dependency exists.

