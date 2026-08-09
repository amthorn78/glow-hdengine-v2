# 0\. Front Matter

**Title:** PF06-Canon-Epic-Process-Guide   
**Version:** v2.4  
**Status:** Canon  
**Effective date:** 2026-08-09  
**Last Update Gate:**  0808 Refresh 1  
**Invocation tag:** INV-f2ac55d77ce9aacc

## 0.1 Purpose and scope

This guide defines the epic delivery process for a human, Implementation Agent, Lead Developer, and CodEx workflow. It requires an Audit and a Sandbox Build/Test for each epic and makes closeout PR-first. In this process, CodEx is responsible for opening the pull request and including the close pack and any supported acceptance-token claims. Actual product capability, repository authorization, and external configuration are execution preconditions and are not proven by this guide.

This is process guidance only. It does not constrain execution environments, repository tooling, transport bytes, or payload bytes. Those remain in their canonical homes.

## 0.2 Policy and principles

PR-first via CodEx.

For each epic slice, CodEx MUST open the PR and include:

- Code changes  
    
- Doc-Delta updates (repo docs)  
    
- Both evidence indices:  
    
  - Human: docs/evidence/INDEX.json  
      
  - Machine: artifacts/evidence\_index.jsonl

Implementation Agent analyzes PR bundles and produces PF-canon Doc Deltas.

Coding agents and Implementation Agents MAY NOT directly modify PF-Canon documents as part of implementation PR work.

If implementation work reveals canon drift, missing canon coverage, or a needed canon change, the agent MUST record that explicitly as a drift note or Doc Delta candidate with evidence pointers rather than editing the PF-Canon file directly.

A PR review or remediation report MAY support a future PF-Canon status update, but the canon edit itself remains separate documentation work. This applies to HDE-Build Checklist rows and any other PF-Canon status tables.

Documentation drainage is never an execution or closeout gate.

Drainage from an exact applicable HDE-Build Notes addendum, and later drainage into permanent canon, checklist, guide, or summary homes, are never prerequisites, required deliverables, required checks, acceptance conditions, or blockers by themselves for plans, reviews, QA artifacts, OPS tasks, acceptance maps, token-to-evidence matrices, PR summaries, or closeout artifacts.

Allowed blockers remain limited to real truth-and-proof failures, such as incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR or FAIL\_TOOLING or TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.

When a canon or checklist delta is known but not yet drained, only the exact current applicable HDE-Build Notes addendum may act as temporary live truth for the topic it explicitly covers. Artifacts MUST identify that addendum by number and title, record the drift and later drain target, use supportable-from-repository-evidence wording when the permanent home is not yet updated, and MUST NOT require drainage to approve execution, recommend merge, or support epic readiness or closeout.

Product Owner-approved bounded revision. An expressly approved, bounded Product Owner scope, architecture, or ADR revision MAY supersede conflicting PF-Canon only for the exact decision it adjudicates. The approval record MUST include a causal map, name the superseded language, preserve later-slice boundaries, state explicit nonclaims, and identify controlled later drainage. It MUST NOT be treated as a general waiver, unrestricted informal scope expansion, or authority outside the recorded decision. Permanent PF-Canon drainage remains required, but it is separate documentation work and MUST NOT be made a prerequisite for applying the approved bounded revision.

Closure axes remain separate. QA evidence, phased-checklist status drainage, PO closeout, board state, merge provenance, and PF-canon drainage are separate closure axes and MUST NOT be collapsed.

- QA evidence proves QA-plan coverage and QA proof posture. It does not by itself perform PO closeout, board update, merge action, phased-checklist drainage, or PF-canon drainage.  
- Phased-checklist status drainage updates an exact task or subtask in the applicable phased HDE-Build Checklist. It may be supported by an exact current applicable HDE-Build Notes addendum and repository evidence, but it remains a documentation/status-drain action, not implementation work.  
- PO closeout is a PO-owned process action. A Lead report or QA evidence package may support PO closeout, but does not perform it.  
- Board state is a Scrum or board-state action. Board updates must be handled in the board source of truth and MUST NOT be inferred solely from QA evidence, an HDE-Build Notes addendum, or review approval.  
- Merge provenance is a repo/history axis. It must be evidenced by repo, PR, or commit state where relevant and MUST NOT be inferred from planning approval or QA approval alone.  
- Canon drainage applies stable documentation updates to the permanent owner. An exact current applicable HDE-Build Notes addendum can stage live truth only for its explicit topic, but the drain itself is a separate documentation action.

Phased-checklist accountability for task-like work. The applicable phased HDE-Build Checklist remains the completion backbone for HDE implementation, QA, OPS, runtime, evidence, vendor, architecture, and product-behavior work. A task-like item may be outside the current epic, deferred, optional, future-scoped, backlog-scoped, non-gating, or follow-up work, but it may not escape phased-checklist accountability.

Every task-like item in an Epic Plan, Implementation Plan, QA Plan, remediation plan, QA-readiness review, retrospective, closure review, Scrum handoff, PO planning handoff, or board-prep artifact MUST resolve to exactly one of:

- in current epic with the exact applicable phased HDE-Build Checklist task or subtask mapping;  
- out of current epic with the exact applicable phased HDE-Build Checklist task or subtask mapping;  
- phased-checklist gap, when the work is legitimate HDE phased-build work but no current task or subtask in the applicable phased HDE-Build Checklist accounts for it;  
- documentation/status drainage only, when the item is only a document, board, archive, or status reconciliation action and not implementation, QA, OPS, runtime, evidence, vendor, architecture, or product-behavior work;  
- out of HDE phased build scope, when the item truly does not belong to the HDE phased build checklist.

Backlog is a scheduling state, not scope authority. If work is moved to backlog, the handoff MUST preserve the exact applicable phased HDE-Build Checklist title, task ID, subtask ID where one exists, disposition, reason it is not included now, and whether a phased-checklist gap exists. If the mapping cannot be proven, the item MUST be marked as a phased-checklist gap rather than placed into backlog without mapping.

Future work must be phased-checklist-accounted. Future runtime claims, future QA claims, future OPS work, future adapter work, future vendor work, future evidence work, future app-integration work, future build improvements, and future remediation work MUST state the exact applicable phased HDE-Build Checklist task or subtask they will satisfy or advance, or be marked as a phased-checklist gap or out of HDE phased build scope.

Subtask-level mapping is required when a relevant subtask exists. Parent-task-only mapping is invalid unless no relevant subtask exists. A parent checklist row may not be treated as closed or supportable for Done merely because one child row or one evidence dimension is mapped.

Reviewers MUST reject plans, retrospectives, closeout reviews, remediation guides, QA-readiness reports, and Scrum/PO handoffs that create unaccounted task-like backlog. This is a scope-accountability requirement, not a documentation-drainage requirement.

Runtime-conformance sequencing for multi-slice epics. When an epic is trying to move a runtime or vendor surface from unsupported, insufficient, or nonclaim posture into bounded support, the plan SHOULD sequence proof from narrowest truth to broadest binding: first prove schema, field, or adapter insufficiency; then implement the pure mapping or adapter layer; then wire the runtime path; then prove internal compatibility; then run any required PO-only open-rails smoke; then bind parent or aggregate evidence. A parent-level evidence binding PR should be last when it depends on earlier PR slices and OPS evidence.

Parent binding does not rerun OPS. A parent-binding or aggregate-evidence PR may consume PO-produced OPS evidence, but it MUST NOT claim to have executed OPS, completed OPS, made live vendor calls, moved phased-checklist status, produced QA PASS, or performed closeout unless those actions happened as separate authorized actions with their own evidence. The parent-binding artifact MUST state whether it binds existing OPS evidence, reruns nothing, and preserves the relevant nonclaims.

Boundary repetition is protective. For runtime-conformance chains, each decisive evidence artifact SHOULD repeat the nonclaims that prevent evidence-to-product overclaim, including no public Reader change, no new public route, no new HTTP home, no app-side vendor ownership, no raw secret or uncontrolled payload persistence, no AI scope, no QA PASS, no OPS completion by PR work, no phased-checklist status movement by PR work, and no closeout unless those claims are explicitly in scope and proven.

An epic MAY be delivered in a series of PRs (up to 10 PRs per epic), each PR carrying a coherent slice of work with its own code \+ evidence parity.

The Lead Developer gates; the Product Owner is the sole merger and uses squash on PASS.

Implementation Agents do not run git and do not create PRs.

Repository administration MUST protect the main branch with the required checks and permit the Product Owner to merge only by squash. This is a process precondition; the pinned repository tree does not prove the live settings.

Re-run proofs only on qualifying drift (green-freeze).

Evidence parity in the same PR.

Whenever proofs or governed artifacts change, update the Human Evidence Index, its hash sentinel, the Machine Mirror, and required path-proof companions in the same PR through the canonical single-writer workflow. Exact paths, schemas, field order, byte rules, and self-record semantics remain single-homed in HDE-Schemas & Artifacts and MUST NOT be duplicated here.

Repo-doc and docs-only changes must be evidence-backed.

Any claim about CLI behavior, output bytes, tokens, governed artifacts, or system mechanics MUST be supported by at least one of:

- a canon pointer (title-only) to the relevant rule.  
    
- a targeted test run output referenced in the PR summary.  
    
- an existing governed evidence artifact path already committed under governed roots.

Additional docs-only constraints:

- Treat "contract changes" (even docs-only ones) as requiring a tight evidence posture. Tests, proofs, and artifacts should be captured in the same PR bundle whenever possible.  
    
- If a docs-only PR is approved without captured CI/test output, the PR summary or review pack MUST (1) state that verification was diff-only, (2) cite the best available canon pointer or governed evidence path for each non-obvious claim, and (3) record any search method used to look for missing proof.

Copy/paste command safety (docs-only and discovery PRs).

Interactive-terminal safety (no shell-closing blocks).

When a plan, runbook, or repo doc includes a command block intended for an operator to paste into an interactive terminal:

- The block MUST NOT terminate the operator shell session (for example by using exit as part of enforcement).  
    
- If strict enforcement requires exit semantics, the enforcement MUST run in an isolated subshell and report PASS/FAIL (and exit code) without closing the parent shell.  
    
- If a shell-terminating block is genuinely required (rare), it MUST be explicitly labeled as non-interactive and an interactive-safe alternative MUST be provided.

When repo docs include commands intended for copy/paste use:

Commands MUST be truthy and CI-traceable:

- If a command is intended to run a CI check or governed script, document the CI-style invocation as the default.  
    
- Do not present multiple conflicting invocations as co-equal. Any compatibility alternative MUST be explicitly labeled optional and must state when/why it is needed.  
    
- Example (mirror schema validation): default to ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl (CI-style direct invocation). python ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl is an optional compatibility fallback (the script has a Python shebang).

The default command shown MUST be safe and non-epic-specific.

- Do not include unrelated epic IDs, unrelated flags, or “example” values in the default command.  
    
- Any epic-specific selector (for example an \--epic-id flag) MUST be explicitly labeled optional and MUST NOT be presented as the default.  
    
- If a command is conditional on local repo state, environment, or path existence, the doc MUST state the condition and the safe fallback.

Decision-bounded placement (no invented “fits at” paths).

When a doc references a future artifact placement or a not-yet-decided path:

- It MUST be labeled TBD and constrained to the smallest set of plausible options.  
    
- It MUST NOT be presented as a single fixed “would fit at \<x\>” path unless the placement is already governed by an existing canonical rule or governed artifact family.

Review source-retrieval guard (no excerpt-based claims).

Reviewers MUST NOT assert canon violations or contradictions about:

- token rosters (missing/wrong tokens, token semantics mismatch), or  
    
- Live QA rails posture / evidence posture, or  
    
- transport bytes / CLI contract expectations,

unless they have fully retrieved the governing canonical passages being referenced (the relevant roster section(s) and the relevant registry / rails / contract entries).

AI review retrieval and proof order.

- Reviewers and AI agents evaluating plans, remediation guides, QA plans, repo audits, closeout artifacts, or related review documents MUST use retrieval-first, proof-first review.  
- When an HDE-Build Notes addendum explicitly addresses the exact topic, identify it by addendum number and title and use the latest applicable, non-superseded addendum before older canon on that point. Then read the current artifact end to end, retrieve the permanent owner for each issue, and prove repository-reality claims with concrete repository evidence.  
- For known literals, exact-string lookup comes before regex or broad search. This applies to task IDs, subtask IDs, token names, headings, route strings, command strings, filenames, artifact keys, environment variable names, and other exact literals.  
- Do not rely on memory, truncated viewer snippets, ellipsized passages, partial excerpts, or broad semantic search as proof when exact retrieval is available.  
- If a locus, path, route, command, flag, token spelling, heading, ID, artifact key, or environment variable cannot be proven, classify it as UNKNOWN or BLOCKED and do not invent or near-match it.  
- Review findings MUST distinguish canon requirement, observed repo reality, and inference.

Build Notes reference posture (living addenda).

When referencing HDE-Build Notes in reviews, plans, or Doc Delta notes:

- Do not reference HDE-Build Notes by version string or by the document title alone.  
    
- Identify the exact applicable addendum by number and title and verify that a later addendum has not superseded it.  
    
- Do not treat an addendum as authority outside its stated scope.

When exact applicable HDE-Build Notes addenda or a closeout artifact record more than one QA pass, QA review, final review, or pass-like event for the same epic, each entry MUST be distinguishable by addendum number and title or another stable source-order label. Reviews and closeout summaries MUST NOT rely on repeated labels such as “QA Pass 2” alone. If duplicate labels exist, cite source order and state the chronology explicitly.

Canon mismatch posture (docs-only PRs).

If a docs-only PR documents current repo behavior that appears to diverge from a canonical PF home (for example CLI exit codes vs HDE-CLI-API-Vendor-Ref), the PR MUST:

- state plainly that the text reflects repo-tested behavior (citing the test/evidence used), and  
    
- state that the PF doc remains the single home for the normative contract (titles only), and  
    
- include a Doc-Delta note routing the reconciliation into the canonical home (update canon or update code) rather than implying “canon is satisfied.”

Docs-only PRs MUST NOT claim “conforms to PF-Canon” when the PR’s own evidence indicates an implementation-vs-canon mismatch.

Docs-only PRs MUST NOT introduce unverified assumptions (for example inventing unsupported CLI flags or asserting output formats not proven by canon/tests/evidence). If the evidence is missing, treat it as a spec gap and fix the spec or add the proof, rather than “fixing docs by habit.”

A7 proof surface (when applicable).

- Run HTTP success-path proofs only on a cataloged JSON success route from the Endpoint Catalog.  
    
- The /internal/version endpoint is ops-only and not A7-eligible.

Single homes.

- Public transport & CLI/Reader bytes → HDE-CLI-API-Vendor-Ref.  
    
- Governance & token semantics → HDE-Governance.  
    
- Deterministic serializer/idempotence → HDE-Math-Spec.  
    
- Architecture & single-emitter rules → HDE Architecture.  
    
- Evidence index & mirror schema → HDE-Schemas & Artifacts.  
    
- Infra and environment names → Glow Infrastructure.

HDE-Mechanics Guide scope guard (doc roles).

HDE-Mechanics Guide is a components and operational-surface reference. It MUST NOT define, rename, alias, or curate acceptance tokens, and it MUST NOT be used as a planning authority for acceptance language. Token registry, naming, semantics, and enforcement remain governed by their single homes (titles only).

For HD Engine epics:

- “Prod” is the production HD Engine service and its production database as defined in Glow Infrastructure.  
    
- Glow Infrastructure is the single home for infrastructure and environment names; PF06 does not redefine their semantics.

When epic docs or QA plans talk about “prod via Codespaces”:

- They must treat Codespaces as a QA console that talks to that production service and DB, not as a prod environment in its own right.

In this guide, “prod via Codespaces” means:

- “Run commands from Codespaces that talk to the production HD Engine service or database and store QA artifacts in the repository.” Codespaces-specific proof is required only when the venue is material under HDE-Build Notes Addendum 2.35, “Live QA Execution Environments: Replace the Universal Codespaces Requirement with a Materiality-Based Evidence Contract.”

Baseline PR acceptance token names and semantics are defined by HDE-Governance. This guide does not reproduce that roster.

Ops tasks (PO-authorized execution; PO-executed or explicitly delegated; IA-guided; not CodEx PR work).

Definition. An Ops task is any work item that requires privileged access to systems outside the repository. This includes (non-exhaustive): service configuration, secrets and env var changes, deploy/runtime settings, infrastructure console actions, and privileged database operations (creation, grants, production migrations, and other privileged state changes). A DevOps task is treated as an Ops task whenever it requires any of the above privileged external access.

Execution authority. Ops tasks MUST be authorized by the Product Owner. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent. The delegated agent MAY perform the authorized operation on the PO's behalf and MUST follow the same scope, safety, evidence, redaction, and completion-claim controls that bind a human operator. “PO-only” identifies the owner of authorization, accountability, and acceptance; it does not require the PO to be the physical keystroke actor. A delegated agent is an authorized executor, not an independent approver.

Delegation contract. A direct PO command to execute an identified Ops task constitutes project-level authorization to act as the PO's delegated executor only when:

- The task identity, operational objective, and target are concrete in the PO instruction or an applicable approved Ops instruction.  
- The requested action remains inside the task's approved scope.  
- Every action-specific or phase-specific authorization required by the Ops contract exists in its required form and is valid at the dispatch boundary.  
- The agent has the required tool capability, access, and credential presence without exposing credential values.  
- Required preconditions, stop checks, rollback controls where applicable, and evidence-capture paths are concrete.  
- The operation is permitted by system, platform, host, service-provider, organizational, legal, and safety controls external to PF-Canon.

When these predicates are satisfied, the delegated agent MUST proceed with the authorized operation and MUST NOT demand a second generic human-only approval solely because the action is operational, privileged, live, mutating, deploy-related, configuration-related, secret-backed, or externally visible. Any additional task-specific or platform-required confirmation remains required. A broad directive is sufficient only when the approved Ops instruction supplies the concrete commands, targets, stop checks, and evidence contract; it is not authority to invent missing commands, widen scope, bypass required approval, or perform unrelated work.

Permitted stops and required blocker response. A delegated agent MUST stop only when an objective blocker prevents valid execution, including a prohibiting higher-priority rule; unavailable tools, network, access, credentials, or capability; an absent or invalid mandatory target, command, authorization artifact, byte identity, hash, stop check, rollback control, or evidence path; material ambiguity that could affect unintended state; changed state that invalidates authorization or safety boundaries; or an operation outside delegated scope. When stopped, the agent MUST identify the concrete blocker, preserve completed safe work and evidence, state exactly what PO value or external action resolves it, and resume once resolved. It MUST NOT substitute a generic actor-type refusal for a specific blocker.

Product Owner authorization is final within the Glow project-governance lane, but it cannot override higher-priority system or platform policy, manufacture unavailable capability or credentials, validate nonexistent run-specific artifacts, or make an unsafe or ambiguous command concrete.

Mutating, privileged, deployment, configuration, database, and secret-backed operations are eligible for explicit PO delegation when otherwise permitted. Before dispatch, the exact target and authorized effect MUST be concrete; any task-required rollback or recovery action MUST be concrete when feasible; and any required STOP CHECK MUST occur immediately before the irreversible or externally mutating boundary. Secret values MUST remain out of commands, logs, chat output, and repo evidence unless an external system securely injects them without disclosure. Completion MUST be supported by the required secret-free Ops evidence.

IA facilitation posture. Ops tasks MAY be part of an epic. When included, they are facilitated by the Implementation Agent (IA). The IA’s job remains to specify intent, constraints, verification, and evidence requirements in a what-not-how manner, then work directly with the PO and any delegated executor. IA facilitation does not create approval authority or widen the delegated scope.

Canon-grounded OPS instructions are required when available. If the relevant PF canon already provides concrete operator steps, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules for an Ops task, the task plan MUST include those instructions explicitly.

The what-not-how posture still applies where canon is silent or incomplete, but it MUST NOT be used to suppress canon-grounded instructions that already exist.

If canon is silent, incomplete, or ambiguous for a required Ops step, the task MUST state that the missing instruction is unknown and MUST NOT fabricate procedure.

Any PF references used for these instructions MUST remain titles-only.

Not a PR. Ops tasks are not CodEx PR work. They MUST NOT be represented as “implementable PR work.” Any implementation/remediation document MUST separate Ops tasks from PR work and label Ops tasks explicitly as: PO-authorized execution, IA-guided.

Ops tasks are not QA tasks. They are implementation work that changes runtime state outside the repo and may be executed personally by the PO or by an explicitly delegated automated session agent acting on the PO's behalf. Delegation does not convert Ops into PR work or QA work.

Ops evidence is not a substitute for QA evidence. Ops completion evidence may be a prerequisite for QA, but QA verification still requires functional proof and the required QA evidence outputs defined in QA planning.

Separation rule (no category mixing). Planning artifacts MUST keep these categories distinct and explicitly labeled:

- Implementation work and deliverables (code and implementation changes)  
    
- Ops tasks (environment changes)  
    
- QA planning (verification plan and evidence posture)  
    
- QA execution (functional runs and governed QA evidence)

Ops task record format (required fields). Every Ops task record MUST include:

- Task ID (stable; referenced consistently)  
    
- Owner: PO  
    
- Facilitator: IA  
    
- Target system/service (name only; no secrets)  
    
- Intent / desired end state (what changes; what “done” looks like)  
    
- Constraints / safety rails (what must remain true while executing)  
    
- Success criteria (observable outcomes; not assumptions)  
    
- Evidence to capture (what artifact(s) prove the change; where stored)  
    
- Rollback intent (what “revert” means at a high level)  
    
- Secret handling note (explicitly: no plaintext secrets in docs or evidence)

Evidence posture (required). Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase audit path such as:

- audit/ops/hde-epic\<NNN\>/ for Ops execution evidence, or  
    
- audit/qa/hde-epic\<NNN\>/ when the evidence is part of QA execution.

Evidence MUST NOT include secrets. If a setting/value is sensitive, evidence must be presence-only, redacted, or hashed, while still being sufficient to verify that the intended state was reached.

Ops evidence provenance minima (required).

Every Ops task evidence bundle MUST include, at minimum:

- Command transcript: the exact command(s) run, recorded verbatim (including any env var names set). Secret values MUST be redacted or presence-only noted. Outputs and exit status: stdout, stderr, and the exit code (or equivalent) captured as files.  
- Verification outputs are captured, not asserted: if a task claims “checksum OK”, “schema validated”, or similar, the evidence MUST include the tool output that shows the check result (not just a narrative statement).  
- Sanitized embedded excerpts: if file contents are embedded in a report, the excerpt MUST be sanitized to remove terminal control sequences. If sanitization would risk altering meaning, embed only a minimal safe excerpt and rely on the on-disk file path as the authoritative content.  
- Retained-path manifest when evidence paths diverge: if a PO-authorized OPS task or later OPS review retains evidence under paths, names, formats, or nested run roots that differ from approved deliverable names, the OPS evidence bundle MUST include a manifest mapping each approved deliverable name to the retained evidence path and the equivalence status. The manifest MUST preserve the approved deliverable identity, the retained repo-relative path, any known format mismatch, any nested evidence-root convention used, and the remaining non-claim posture. It MUST NOT move, rename, or rewrite already-produced OPS evidence merely to make the paths match the plan unless the approved task explicitly requires that remediation.

Build Checklist tracking requirement. Any Ops task included in an epic MUST be represented as a subtask in the module specific build checklist so it can be tracked and reused. The checklist entry MUST use the same Task ID and carry the same required fields listed above.

No governance drift. Ops tasks MUST NOT create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it MUST map to existing governance-defined acceptance posture and be proven via evidence artifacts.

Clarification. If a change is fully achievable as code, including tests and deterministic artifacts, it is PR work. If any step requires privileged access to systems outside the repository, that step is an Ops task even if adjacent code changes exist. Ops tasks can be prerequisites for epic completion, but completion is proven by the required evidence artifacts, not by unsupported claims from either a human or delegated executor.

Bounded Ops discovery and validation runs. An Ops task approved as DISCOVERY, command-discovery, validation-only, sequencing-correction, blocker-classification, or implementation-validation MUST be reviewed only for that bounded approved purpose. If exact command proof, target facts, required credentials, prerequisite proof, or safe execution context remain unproven, the task MUST record the unresolved posture and MUST NOT convert that state into FAIL\_BEHAVIOR.

OPS discovery is first-class work, not a deferral substitute. When an in-scope implementation, QA, remediation, or OPS item depends on an operational, infrastructure, credential, environment, vendor, endpoint, open-rails, or evidence-root fact that can be safely discovered under Product Owner authorization through a bounded OPS task, the plan MUST route bounded OPS discovery instead of deferring the item merely because the fact is not already pinned.

Unknown classification. Plans MUST classify each operational unknown as one of: discoverable by OPS, discoverable by PR, discoverable by QA, requires PO or Thoth decision, requires an exact applicable HDE-Build Notes addendum, requires permanent canon update before safe execution, unsafe to discover now, out of scope, phase drift, or valid deferral. “Unknown,” “OPS required,” and “open rails required” are not complete classifications by themselves.

OPS discovery task minimums. A bounded OPS discovery task MUST state the exact fact to discover, why the fact matters, who owns discovery, whether secrets are involved, what may be recorded, what must not be recorded, what downstream PR, QA, OPS, or planning item depends on it, and what safe evidence or summary resolves the unknown. The discovery result may unblock later PR, OPS, or QA work only after the discovered fact is routed into the relevant plan, QA artifact, implementation artifact, or closeout proof.

Dependent Ops execution guard. A downstream Ops execution task MUST NOT proceed from unresolved command proof or unresolved target facts. When the safe execution basis is not proven, classify the downstream task as TOOLING\_BLOCKED and record what proof would unblock it.

Ops evidence overclaim guard. Bounded Ops discovery, validation, and implementation-validation evidence MUST NOT by itself claim QA PASS, Live QA completion, phased-checklist status change, acceptance-token satisfaction, PF-canon drain completion, or epic closure. It may support a later-drain posture only when the approved task claimed that posture and the governed evidence proves it.

Closed-task OPS revalidation reviews. An OPS evidence review MAY revalidate an already-closed or already-recorded phased-checklist task or subtask when the approved task is bounded to revalidation, evidence inspection, or current-state confirmation. The review MUST preserve the distinction between OPS revalidation evidence, QA evidence, phased-checklist status drainage, acceptance-token claims, PF-canon drainage, and epic closeout.

OPS revalidation evidence may support the current recorded applicable phased HDE-Build Checklist posture or support a later-drain note only when the reviewed evidence proves that bounded posture. It does not replace QA evidence, does not perform QA execution, does not perform applicable phased HDE-Build Checklist drainage, does not create a new acceptance token claim, does not imply implementation change, and does not perform PO closeout.

When older governed evidence has a historical shape caveat, the revalidation review MUST classify the caveat precisely. A historical evidence-shape caveat is not by itself a reason to downgrade a closed applicable phased HDE-Build Checklist task when the governing evidence requirement is still satisfied by coherent current evidence, mirror records, and path-proof linkage. If a later PO-governed migration or current PF-Canon rule requires richer evidence shape, record that as a separate migration or drain item rather than silently changing the closed-task posture.

Ops closeout packaging run (OPS-01). When an epic uses an Ops task to surface already-produced close-pack artifacts and closure evidence, the run MUST remain packaging and evidence only:

- no reopened implementation work  
- no QA verdict changes  
- no canon-drain claim  
- no merge-provenance claim

The OPS-01 execution bundle MUST include, at minimum, commands.txt, stdout.log, stderr.log, exit\_codes.txt, and created\_files\_sha256.txt under the stable ops root for the epic.

OPS-01 MAY surface the canonical close-pack baseline artifacts and their sibling path-proofs, but it MUST bind those artifacts to the existing governed acceptance or QA evidence family rather than inventing a replacement proof surface.

A later OPS provenance run is optional unless the approved plan explicitly makes it mandatory.

An OPS-01 validation bundle may be accepted for its bounded validation purpose even when one or more intended environments remain `not yet closed`, provided the bundle truthfully records the unresolved state, the reason, and the governed evidence that supports that state.

For each intended environment, the bundle MUST either show a validated run or record an explicit disposition that says `not yet closed` with a concrete reason grounded in the run evidence.

Missing infra-owned bindings MUST be preserved as `not yet closed` or deferred states. They MUST NOT be guessed, reconstructed, or silently treated as closed.

Accepting a truthful OPS-01 validation bundle does not by itself support a phased-checklist status move or a claim that the underlying environment task is complete. It only proves the bounded validation outcome the run was approved to capture.

Ops task-level close-candidate posture. An Ops evidence bundle MAY record `CLOSE CANDIDATE`, `closed`, or equivalent task-level status for a bounded evidence dimension when the approved OPS task proves that dimension and preserves the higher-level non-claim posture.

When this posture is used, the bundle MUST state:

- the bounded dimension being evaluated  
- the active proof scope or corpus, including any included or excluded rows when the proof depends on a scoped corpus  
- the decisive evidence and checksum or path-proof posture used for the task-level status  
- the secret-safety posture, including presence-only treatment for sensitive environment values  
- the higher-level non-claims that still apply, including QA PASS, phased-checklist status movement, acceptance-token satisfaction, PF-canon drain completion, and epic closure when those are not proven

A task-level close candidate or closed proof dimension does not by itself move a phased-checklist row to Done, satisfy an acceptance token, prove Live QA, or close an epic. Those stronger claims require separately approved scope and separately governed evidence.

Ops evidence-packaging remediation runs. When an Ops task is approved as evidence packaging, close-pack surfacing, or provenance repair, it MUST remain within the approved evidence boundary.

A packaging-only Ops remediation MUST NOT:

- rerun QA  
- make vendor calls  
- modify implementation files  
- edit PF-Canon  
- claim phased-checklist status drainage  
- create new acceptance claims

If the remediation repairs a prior Ops evidence defect, the repaired bundle MUST make the repair auditable by recording:

- the defect class or blocker that was repaired  
- the corrected command transcript or evidence artifact  
- labeled stdout, stderr, and exit-code evidence mapped to the corrected actions  
- validation output for each claimed check result  
- the prior invalid or superseded artifact when preservation is needed for audit trail  
- the final bounded outcome and any non-claim posture that remains

A packaging-only Ops remediation may support close-pack surfacing or evidence-provenance closure only for the bounded task it was approved to perform. It MUST NOT be used to imply new implementation completion, QA rerun completion, phased-checklist status change, PF-canon drain completion, or epic closure unless those claims are separately approved and proven.

## 0.3 Participants and responsibilities

- Implementation Agent (ChatGPT). Runs each epic end to end, prepares CRD-ready drafts, sets up CodEx asks (what, not how), verifies proofs and artifacts, ensures Doc-Delta and both indices are updated in the same PR, and escalates blockers to the Lead Developer. Does not run git or create PRs.  
    
- Lead Developer (AI). Defines intent and scope, approves the CRD and Implementation Plan once, performs the gate review on the PR, and otherwise steps out during CodEx execution.  
    
- CodEx. Executes the authorized repository work in a sandbox, runs Audit and Build/Test, and is responsible for opening the PR under the approved plan and this guide’s PR process. It includes the close pack and supported acceptance claims, adapts only within scope, and reports all material changes. Repository access, PR authorization, and source availability remain execution preconditions rather than guaranteed current capability claims.  
    
- Thoth (CRD authority). Owns CRD standards and architecture fit, confirms acceptance tokens and capsule homes by title.  
    
- Product Owner (human). Sole merger using squash; signs acceptance on PASS; informs the Scrum Master after merge. Owns Tracked Issues and ADR stubs for planning artifacts; adjudicates drift items and approves token minting decisions.  
    
- Scrum Master (AI). Informed after merge; records the close; updates boards and the sprint report.  
    
- Communication rule. AIs do not contact one another directly. The Product Owner routes all messages.

## 0.4 Execution posture and flow (PR-first)

- Lead Dev publishes the Implementation Guide to the Implementation Agent (IA).  
- IA sends CodEx an audit request with explicit report formats and any verbatim components or schemas required.  
- CodEx returns an audit report covering capabilities, gaps, and risks.  
- IA drafts the Implementation Plan. Lead Dev approves once, then acts only as the PR gate.  
- IA sends CodEx build instructions plus verbatim components or schemas. CodEx may adapt within scope, must report all changes, and returns a detailed change report plus artifacts and evidence.  
- IA either requests changes or approves.  
- CodEx opens the PR and includes the approved code, Doc-Delta updates to repository documentation, the Human Evidence Index, the Machine Mirror, and the canonical close-pack files `audit/EPIC-<NNN>_close_report.md` and `audit/EPIC-<NNN>_MANIFEST.json` with the companions defined in §0.5.1.  
- Machine Mirror schema and byte requirements remain single-homed in HDE-Schemas & Artifacts.  
- Lead Dev gate review:  
  - verify only acceptance-token claims admitted under §1.1.9  
  - verify A7 proof surface on the cataloged JSON success route (not /internal/version)  
  - verify env-gate proof and encoding invariance  
  - verify same-PR evidence parity  
  - verify Endpoint Catalog single home present (docs/ENDPOINTS\_CATALOG.json \+ .sha256)  
  - verify Reader A7 proof JSON is captured and indexed (human \+ machine, same PR)  
- PO merges: perform squash merge on PASS and notify the Scrum Master.  
- Closure: IA files the Closure Report; boards and sprint reports updated; suites green-freeze until a qualifying change lands.  
- Determinism pins for determinism-sensitive capture and CI checks: set LC\_ALL=C, LANG=C, TZ=UTC to keep bytes stable. Do not add non-canonical “extra pins” as requirements.

### 0.4.1 Live QA discovery and RCA (execution requirements)

Live QA via a QA harness is a required Close Gate stage for every epic. See §3.5.2.8 for the harness-run and evidence-landing requirements.

These requirements are execution and Close Gate deliverables. They MUST NOT be treated as prerequisites for Epic Plan approval and MUST NOT force a detailed Live QA runbook into PLAN/CRD or Implementation planning.

#### 0.4.1.1 Mandatory D0 Discovery artifact

Before running any Live QA steps that exercise behavior or vendor flows, the epic MUST produce at least one Discovery artifact that captures the baseline execution context and rails posture for the Live QA session.

At minimum, this Discovery artifact MUST:

- Record the effective rails posture and runtime context (for example SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, locale/timezone pins, and any other env variables materially affecting Live QA behavior).  
- Summarize which services and surfaces are expected to be reachable for Live QA (for example “CLI only”, “Reader HTTP routes”, “production endpoints”) and any known constraints.  
- Capture initial tool health for key entrypoints (for example CLI help, harness availability) so later failures can be distinguished from simple environment misconfiguration.

Evidence posture (normative)

- The Discovery artifact is a governed, mechanical file under the epic’s QA root (audit/qa/hde-epic\<NNN\>/). It is evidence that the session ran under known, documented conditions.  
- Per-run nesting is disallowed for Live QA current-state evidence. Discovery artifacts MUST live under the stable epic-scoped QA root and MUST NOT use run-id, timestamped, or fresh-run directories as correctness surfaces.  
- When the Discovery artifact is step-scoped, it MUST land under the stable check directory for that step. Re-runs refresh the same governed location rather than creating a new run root.  
- The Discovery artifact MUST be generated by commands and MUST NOT be hand-edited. Its plan structure is governed by PF27-Canon-Plan-Templates, and its artifact schema and path rules are governed by HDE-Schemas & Artifacts.

#### 0.4.1.2 Mandatory QA RCA & Doc Delta summary

Every Live QA epic MUST produce a QA RCA & Doc Delta summary as part of execution deliverables, regardless of whether large gaps are observed.

Definition (normative; prevents drift) The QA RCA & Doc Delta summary is not a new plan and not a second epic review. It is a short, evidence-linked explanation of:

- what was run,  
- what the outcomes mean (PASS vs FAIL\_BEHAVIOR vs FAIL\_TOOLING vs TOOLING\_BLOCKED),  
- what evidence proves those outcomes, and  
- whether canon updates are required (or explicitly none).

It exists to prevent re-litigating failures caused by environment/tooling (wrong base URL, missing inputs, network blocked) versus actual behavior regressions.

The summary MUST NOT:

- introduce new acceptance criteria,  
- expand QA scope beyond the epic,  
- propose new QA plans/runbooks beyond what Close Gate requires.

Minimum required contents At minimum, the summary MUST:

- State the key Live QA findings in reader-usable language (not just raw logs).  
    
- If no substantial gaps are found, it MUST say so explicitly (example: “No new PF-Canon deltas identified for this epic”).  
    
- For each substantive failure or anomaly, classify it as one of: FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED, and include a one-line reason.  
    
- When a step is blocked because the approved plan depends on unavailable or non-product inputs, the summary MUST classify the outcome as TOOLING\_BLOCKED with a planning-defect or input-availability reason, not as FAIL\_BEHAVIOR.  
    
- In that case the summary MUST name which expected artifacts were not produced because the blocking precondition was not met, and it MUST state that those artifacts were not expected for that run.  
    
- The summary MUST record the precise rerun condition for the blocked step, for example that rerun is deferred until valid product inputs become available.  
    
- When a check includes more than one attempt in the same governed step directory, the summary MUST distinguish attempt history from the final governing outcome.  
    
- If an earlier attempt failed but a later rerun under the required rails and determinism posture produced the complete governed evidence set and satisfied the approved PASS criteria, the later rerun MAY govern the step outcome.  
    
- In that case the summary MUST name the superseded earlier attempt, classify why it failed, and state plainly which later attempt produced the final accepted evidence.  
    
- The earlier failed attempt remains part of the record and MUST NOT be hidden, but it is not a close blocker by itself once the later rerun is clearly evidenced and the approved criteria are met.  
    
- Provide minimal evidence pointers for each substantive finding (step log(s), artifact(s), validator outputs). Use the applicable plan structure from PF27-Canon-Plan-Templates and exact governed paths from HDE-Schemas & Artifacts.  
    
- Map each substantive finding that implies a change in behavior, infrastructure, or process to the permanent owning PF-Canon document by exact title (for example, the applicable phased HDE-Build Checklist, Glow QA Guide, HDE-Mechanics Guide, Glow Infrastructure, or HDE-Schemas & Artifacts). HDE Phased Epics may receive only a historical record correction after close, not in-flight planning or task scope.  
    
- Identify follow-on epics/cards expected to carry those PF updates when they are deferred.  
    
- When the QA RCA & Doc Delta summary is used to support epic-close readiness, it MUST state the source-of-truth posture for the review. The summary MUST name the primary epic-specific execution source, the canon homes used for closeout interpretation, and any Implementation Guide or QA Plan inputs that were used only for framing.  
    
- When a Live QA Plan exists, the summary MUST include explicit Coverage vs QA Plan accounting in plan order using stable step identifiers. For each planned step, it MUST record whether the step is Fully evidenced, Partially evidenced, or Not evidenced, whether governed evidence pointers exist, any material mismatch between the planned step and the recorded step, and the closeout impact.  
    
- When the primary epic-specific execution source is an exact applicable HDE-Build Notes addendum, identified by number and title, or another guidance record, the summary MUST state whether that source carries direct evidence-pointer lines or only evidence-basis prose.  
    
- If the decisive source is evidence-light, the summary MUST label it as evidence-light guidance and SHOULD pair it with the governing evidence-backed lines that make the closeout reasoning auditable.  
    
- Coverage vs QA Plan MUST separately surface any accepted plan-execution deviation, even when the step is Fully evidenced and PASS. Examples include bounded Moon Loop reruns, rails changes, and step-local dependency-preflight corrections. Coverage status alone is not sufficient when accepted execution materially diverged from the approved plan.  
    
- When closeout depends on runtime functional proof, the summary MUST state whether same-run runtime proof exists across the changed runtime surfaces required by the approved plan, and it MUST name the governed artifacts that prove presence or absence of those runtime surfaces.  
    
- The summary MUST include an explicit closeout-readiness recommendation. This recommendation is a closure-oriented review result and MUST remain distinct from the final SATISFIED or NOT SATISFIED decision recorded in the close report.  
    
- When a QA closeout or acceptance-reporting summary is limited to repo-supported completion, it MUST say so explicitly.  
    
- It MUST distinguish, as separate states, repo-supported completion, canon-drain completion, and formal close-pack completion.  
    
- If canon-drain completion or formal close-pack completion is not proven, the summary MUST mark those states as no-claim or equivalent explicit non-claim wording rather than implying completion.  
    
- A repo-supported completion summary MUST distinguish blocked steps from recorded or completed steps in the current run and MUST NOT be phrased as though formal merge or close is already proven unless that stronger proof is actually present.

Location (normative) The QA RCA & Doc Delta summary MAY live as a section of the epic close report, or as a separate governed artifact referenced from the close report.

If the QA RCA & Doc Delta summary is maintained as a separate governed artifact, it MUST use the canonical filename `audit/EPIC-<NNN>_QA_RCA.md`. The epic close report MUST reference this artifact by path.

The level of detail is proportional to the findings (brief when no deltas, more extensive when multiple PF docs are impacted). When the run is clean, this summary may be only a few lines.

#### 0.4.1.3 Execution gate

For Live QA epics, the Close Gate (§3.5) MUST confirm:

- a D0 Discovery artifact exists for the Live QA session(s), and  
- a QA RCA & Doc Delta summary exists and, where substantial gaps were found, points to concrete PF-Canon updates (or explicitly states none).

If either the Discovery artifact or the QA RCA & Doc Delta summary is missing, the epic MUST NOT be treated as fully accepted, even if code/tests/CI tokens are green.

## 0.5 Routing and evidence discipline

Single homes (titles-only)

- Transport bytes and CLI/Reader flows → HDE-CLI-API-Vendor-Ref.  
- Token semantics and ops policy (A7, refusal, writers) → HDE-Governance.  
- Canonical JSON, pack/manifest, Human Evidence Index, and machine mirror → HDE-Schemas & Artifacts.  
- Architecture boundaries and single-emitter rules → HDE Architecture.  
- Do not restate bytes, schemas, or token tables here.

Governed locations only

- Evidence artifacts and persisted logs must live under governed paths (audit/**, artifacts/**, and docs/\*\*).  
- Transient/generator paths are disallowed for governed evidence (for example ./outputs, ./runs, ./tmp, /tmp, \~/.cache, .venv).

Live QA execution convenience (/tmp helpers) During Live QA execution, QA agents MAY create ephemeral helper scripts under /tmp for execution-only purposes (parsing, formatting, extracting proof facts). These scripts and any /tmp outputs:

- MUST NOT be treated as deliverables or evidence, and  
- MUST NOT be indexed, mirrored, or referenced as acceptance binding surfaces.

Evidence posture is unchanged:

- Any evidence artifact used to decide PASS/FAIL MUST be written under a concrete lowercase path under audit/\*\* (preferred) or artifacts/\*\*.  
- Ephemeral helper scripts MUST NOT print or persist secrets. If they handle sensitive env vars, logs MUST remain presence-only or redacted.  
- Proof files must live under governed paths (audit/**, artifacts/**, and docs/\*\*).

Live QA Moon Loop: minimal in-session remediation is allowed to unblock QA Live QA may include a small remediation loop when a check fails due to a small, execution-blocking issue (wrong predicate target, missing guard, etc.) and the smallest correction is required to produce a PASS-grade proof for the already-approved epic scope.

Hard boundary: no scope expansion. In-session remediation MUST NOT:

- add new features or acceptance criteria  
- introduce new evidence families  
- turn QA into a second remediation plan

The only goal is to unblock the existing QA check(s) and prove the already-scoped behavior.

Allowed remediation actions (minimum set)

- Create small helper scripts under /tmp for parsing/glue (ephemeral; never treated as governed evidence).  
- Adjust the QA check procedure to key on the canonical emitted evidence surfaces already required by canon and implementation.  
- When a Live QA check fails because a proof command depends on exact-case or exact-string matching against governed prose, reviewers MUST verify the raw artifact and the intended semantic proof target before treating the failure as final FAIL\_BEHAVIOR.  
- If the raw artifact preserves the intended semantic posture and the defect is only a brittle prose-match, casing, punctuation, or equivalent phrase-match issue, the failure MAY be treated as a QA evidence-harness defect eligible for bounded Moon Loop correction under the approved QA root.  
- The corrected check MUST preserve the original proof target, PASS or FAIL predicate, rails posture, evidence family, and non-claim boundaries, and the governed evidence stream MUST preserve the original failed proof and the accepted rerun proof.  
- Apply the smallest change required for the failing check(s) to execute and validate the intended behavior.  
- A PO-approved Moon Loop MAY repair an existing governed evidence-integrity ledger, checksum companion, or self-reference row when the only failing predicate is ledger completeness or binding coherence and the underlying behavior proof already satisfies the approved predicates. The correction MUST stay inside the existing evidence family and governed step root, MUST NOT run a new behavior command, vendor call, or network-opening step, MUST NOT introduce a new evidence root or evidence family, and MUST be followed by a rerun or validator output that proves the original PASS criteria.  
- Re-run the affected check(s) and capture the PASS-grade evidence artifacts.  
- A bounded Moon Loop may correct only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under the approved QA root.  
- A change to product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction.  
- Non-QA-root remediation MUST be routed through an approved work item type: PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE.  
- A final PASS proof that relies on non-QA-root governed evidence refresh MUST cite the approved routing receipt before the refresh-derived gate or validation output.  
- Valid routing types include PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE as approved for the affected work item.  
- The review record MUST preserve the failed pre-routing or pre-refresh receipt as context, identify the final accepted receipt, and state that final PASS relies on routed refresh rather than unapproved Moon Loop correction.  
- If the routing receipt is missing or the final receipt cannot prove the routing before the refresh-dependent checks, the step remains non-PASS until routed evidence is available.  
- If an initial failing artifact is overwritten or unavailable by the time remediation begins, the remediation record MUST state that the initial failure artifact is unavailable and MUST NOT reconstruct missing logs, hashes, timestamps, result bodies, or proof bytes.

Evidence posture for in-session remediation (mandatory) If remediation occurs inside a QA session, the existing primary log artifacts MUST make it auditable without additional documents:

- The failing check’s primary.log MUST include the failure signature (short excerpt).  
- The same log (or the session transcript) MUST include a one–two sentence remediation note that names exactly what changed (file paths) and why.  
- The rerun output showing PASS MUST be captured in the same evidence stream.  
- If any repo files were changed, capture a minimal delta artifact under a lowercase governed path, for example:  
  - audit/qa/hde-epic\<NNN\>/remediation/moon\_loop/patch.diff (or equivalent)  
  - audit/qa/hde-epic\<NNN\>/remediation/moon\_loop/changed\_files.txt (paths \+ sha256)  
  - This delta capture MUST NOT discuss branches, commits, or PR workflow.  
- If a Moon Loop changes evidence packaging, transcript repair, validation provenance, or classification after an initial failure, the governed evidence stream MUST record the approved scope boundary, the exact command or command family used, material stdout, stderr, exit-code, or validator output, any superseded artifact posture, and any remaining non-claim boundaries.

A PO-approved Moon Loop MAY temporarily open rails on one already-approved Live QA step even when the approved plan defaulted that step to closed rails, but only as a bounded deviation for that step.

This is allowed only when all of the following are true:

- the deviation is explicitly approved by the Product Owner and recorded in governed step evidence  
- the step keeps the same approved step ID, the same deliverable family, and the same PASS or FAIL criteria  
- the rerun remains under the same governed step root  
- the rerun does not introduce new acceptance surfaces, new evidence families, or widened feature scope

When those conditions are met, treat the issue as a non-blocking planning failure or deviation note, not as an automatic trust failure, provided the governed evidence remains complete, non-empty where required, any required determinism pins for produced bytes remain captured, and the rerun satisfies the approved PASS criteria.

The review record MUST state:

- the original closed-rails expectation  
- the actual rails used  
- why closed rails were insufficient for that step  
- where the PO approval was recorded  
- why the rerun remained within the already-approved step scope

If these conditions are not met, stop the Moon Loop and escalate to a normal remediation plan.

For reporting or classification steps, a bounded Moon Loop MAY correct a false blocked state when the blocked result was triggered by the presence of a trigger file rather than by a hard blocking condition in the file content.

If this pattern is used:

- preserve the original contextual note by copying it to an immutable context artifact under the same governed step root  
- remove or rename only the trigger filename or trigger filenames that caused the false blocked classification  
- capture the Step-0B or equivalent delta pair for the change  
- rerun only the already-approved reporting step under the same deliverable family

This is acceptable only when the rerun changes reporting state, not behavior state, and when the preserved context artifact plus the rerun evidence make the transition auditable without inventing a new evidence surface.

Stop condition

Plan-compliant PASS is required for Moon Loop reruns (mandatory). If a Moon Loop rerun records PASS but later fails a plan-defined content predicate (for example missing PF refs in doc-delta content, or a non-plan-compliant primary.log header), treat the step as still non-PASS and continue remediation until a final rerun satisfies all plan predicates.

If the remediation required is not “minimal” (multiple files, structural changes, or unclear scope), stop the Moon Loop and escalate to a normal remediation plan.

Same-PR parity (mandatory) When proofs or governed artifacts change, refresh the Human Evidence Index, hash sentinel, Machine Mirror, and every required path-proof companion in the same PR through the canonical evidence writer. CI MUST enforce the owner-defined Human-to-Machine parity and block missing, stale, or mis-indexed bindings. Exact paths, schemas, record fields, ordering, byte rules, self-record rules, and path-proof content are owned by HDE-Schemas & Artifacts and are not reproduced here.

Governed evidence drift remediation (hard stop) If a governed artifact, its path proof, the Human Evidence Index, the hash sentinel, or the Machine Mirror disagrees with the physical bytes, stop. Do not hand-edit governed evidence to force a check to pass. Regenerate through the canonical single writer and run the exact current check procedures and determinism pins defined by HDE-Schemas & Artifacts. Merge remains blocked until the owner-defined checks establish coherence.

Evidence validation special cases (self-record \+ validator dependencies)

Canonical machine mirror path (single home) Use only the Machine Mirror home defined by HDE-Schemas & Artifacts. Plans and PRs MUST NOT introduce an alternate mirror. Treat any alternate path emitted by tooling or CI as drift and resolve it before close.

Self-record proof semantics (high-risk) The Human Evidence Index and Machine Mirror are governed artifacts. A PR that changes their generation or validation MUST run the owner-defined self-record regression checks and capture decisive diagnostics for any mismatch.

Validator dependency policy (CI stability) Any evidence validator (scripts or tests) that depends on non-core packages MUST have an explicit dependency posture:

- Either the dependency is required and installed in CI, or  
- the validator must skip cleanly with an explicit message (no import-time hard failure).

This prevents CI-only failures that block merges without changing product behavior.

Validator run proof (CI-safe) When a PR relies on a validator (script or test) as merge evidence (e.g., to enforce acceptance-map / token-matrix invariants), the PR Packet MUST capture:

- the exact invocation used to run the validator  
- PASS output (or failing diagnostics if requesting review)  
- the exact owner-defined rails and determinism pins used for the run, unless the validator is explicitly documented as pin-insensitive

Ops rails refusal proof (closed-rails) When closed-rails refusal proof is in scope, capture it at the owner-defined governed path and apply the refusal, writer, indexing, and path-proof contracts from HDE-Governance and HDE-Schemas & Artifacts. This guide does not reproduce those bytes or schemas.

Merge gate (path-proofs required) Every indexed artifact MUST satisfy the owner-defined path-proof binding. Missing or incoherent binding blocks merge. Same-PR parity among the Human Evidence Index, hash sentinel, and Machine Mirror remains mandatory.

Proof surface routing (A7) Success-path A7 proofs run only on an eligible cataloged JSON success route. The `/internal/version` ops surface is excluded. Apply the exact current transport predicates from HDE-CLI-API-Vendor-Ref, the policy from HDE-Governance, and the evidence contract from HDE-Schemas & Artifacts rather than reproducing header or proof bytes here.

Endpoint Catalog single home (titles-only) The only authoritative Catalog path is `docs/ENDPOINTS_CATALOG.json`, with checksum companion `docs/ENDPOINTS_CATALOG.json.sha256`. The Catalog records endpoint metadata, including non-A7 internal routes. Its `success_endpoints` list identifies JSON success routes; `/internal/*` routes are excluded from A7 eligibility. A7 proofs must run on a cataloged success route, and an env-gate headers proof is required.

Reader A7 proof JSON (machine-checkable) When Reader A7 is in scope, produce the owner-defined machine-checkable proof artifact and update its governed index and mirror bindings in the same PR. Its schema and byte contract remain in the owning canon.

CRD routing Thoth receives the CRD only. Keep process artifacts (PLAN/CRD/Doc-Delta) titles-only and route to single homes for bytes/evidence.

Cross-doc references Use titles only for all external references; do not duplicate transport bytes, schemas, or acceptance rosters in this guide.

Evidence skeleton coherence (Index/Mirror \+ topology orientation) When a PR adds or changes governed evidence, it MUST refresh the owner-defined topology orientation artifact and required path-proof companion in the same PR as the Human Evidence Index and Machine Mirror.

Determinism predicate surfaces (D16–D18; locked) For D16–D18, validate only the canonical evidence surfaces and sibling path proofs defined by their owning canon. Do not require wrapper bundles, alternate path spellings, or extra marker conventions. Apply the exact owner-defined determinism pins and decisive predicates. A missing required validator dependency is `TOOLING_BLOCKED` and must be corrected before rerun; it is not behavior PASS or FAIL.

HDE Phased Epics MUST NOT be cited to define evidence-surface paths, validator predicate targets, or path-proof naming. Cite the exact owning canon title, including the applicable phased HDE-Build Checklist, HDE-Schemas & Artifacts, Glow QA Guide, or HDE-Governance, for those requirements.

If the orientation demo is not refreshed to match the current Evidence Index and Mirror skeleton, the standard check fails with ORIENTATION\_DRIFT.

### 0.5.1 Epic path normalization (close-pack \+ QA root)

This guide uses normalized epic identifiers for file paths. Plans, QA ledgers, Evidence Index entries, and machine mirror records MUST use these canonical patterns and MUST NOT introduce alternate spellings.

Plan path provenance (no fabricated required paths) A PLAN, CRD, or QA Plan MUST NOT reference a file path as required unless one of the following is true:

- Canon-defined — the path (or path pattern) is explicitly defined by PF canon, or  
    
- Audit-proven — the path’s existence is already proven by an existing, canon-recognized audit artifact family, or  
    
- QA-created — the plan includes inline, explicit creation instructions and validation for the path.

If a path is not canon-defined and not audit-proven, it MUST either be created under QA with explicit instructions and justification, or it MUST NOT appear in the plan.

Plan locus validation labels (required for asserted repo loci) When a planning artifact asserts an implementation locus (repo path, directory root, module home, or “where this lives”), the statement MUST be validated using exactly one of the following labels:

- Canon-cited (preferred): cite the governing PF canon home(s) that define the locus.  
- Codex Audit observed evidence: identify the supplied Codex Audit and embed the observed repo-reality fact as a short quote or precise paraphrase. This label may prove planning-time repo reality only.  
- IG Approved: include a verbatim quote from the approved Implementation Guide that proves the locus.  
- QA-created: include explicit creation instructions plus an explicit verification step that proves the locus exists and meets criteria; capture the proof in governed evidence output.

Rules for Codex Audit observed evidence and IG Approved:

- The embedded observation MUST be sufficient to prove the asserted planning-time locus. If it does not prove the locus, the plan must not assert it.  
- Codex Audit observed evidence may support existing-locus claims, reuse-first planning, implementation scoping, PR task inputs, OPS task dependencies, QA-prep context, and gap identification.  
- Codex Audit observed evidence does not by itself prove acceptance-token satisfaction, QA PASS, epic closure, phased-checklist status movement, PO closeout, Live QA execution, OPS completion, governed evidence freshness after later changes, production truth, external vendor truth, open-rails truth, secret validity, runtime conformance beyond the observed repo fact, canon authority, or new normative rules.  
- CodEx must still verify repo reality during execution before editing or relying on the locus.

Audit provenance in planning artifacts. Audit provenance is allowed in Epic Plans, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives when it is used as planning context, risk context, discovery context, source-trace context, rationale for inspection, rationale for a Tracked Issue, rationale for an ADR stub, rationale for a planned workstream, rationale for a QA proof obligation, rationale for repo validation, or rationale for PF-canon drainage.

Audit provenance MUST NOT be treated as PR instruction, OPS instruction, step-by-step execution procedure, CodEx command source, acceptance authority, token authority, QA PASS proof, OPS completion proof, applicable phased HDE-Build Checklist Done proof, closeout proof, current repo truth without repo validation, source of invented file/path/module/test existence, source of required deliverables unless adopted by the plan or PF source, source of privileged live action, or source of secrets or external state.

A reviewer MUST NOT block a plan solely because it includes audit provenance. A blocker is valid only when the plan turns audit provenance into execution authority or proof authority. Allowed review classifications for context-only audit provenance include No issue, Note, Context accepted, Planning provenance accepted, Repo validation required before execution, and Keep out of PR or OPS instruction text.

When audit provenance appears in PR or OPS planning, convert it into neutral work language before operative execution text. Examples of neutral work language include inspect the current repo state, validate the current route policy, prove the current behavior, update governed evidence, preserve the nonclaim, or bind the evidence under the governed root.

File and directory minting posture (do not invent a home) Plans MAY require minting new files and directories only under an already validated, canon-defined home, or under governed QA roots (`audit/**`, `artifacts/**`) when the creation occurs during QA. Plans MUST NOT introduce a new top-level root, a second home for an existing surface, or a guessed repo layout. If a new root or new home is required, treat it as an architecture change and route it via ADR and Doc-Delta before it appears as a required path in a plan.

Review gate Any required locus that lacks a valid label above is a mechanical blocker until corrected.

QA-planning locus provenance lock (repo-resident loci)

In QA planning artifacts (Live QA Plans, QA Guides, QA reviews, QA prompts, and QA checklists), the allowed sources for repo-reality claims are:

- an exact applicable HDE-Build Notes addendum, identified by number and title  
- PF-Canon  
- a supplied Codex Audit for the epic, task, or review artifact  
- the initial QA Audit for the epic

This lock applies to repo-resident and repo-reality strings, including:

- file and directory paths  
- endpoint names and routes  
- module and component identifiers  
- script names, runbook names, and command strings  
- check and test identifiers, CI job names  
- environment variable names when treated as already-existing  
- fixed output locations when treated as already-existing  
- negative existence claims

No invention, no inference, no memory. If the exact locus string is not supported by an allowed provenance source, it MUST NOT appear as a repo-resident claim in the plan.

Verbatim-only requirement for exact locus strings. When a repo-resident locus string is used, it MUST be copied character-for-character from the allowed provenance source. No renaming, case folding, equivalent substitutions, wildcard expansions, or invented variants.

Blocking posture. Any QA plan that contains a repo-resident locus string not proven by an allowed provenance source is invalid for approval and MUST be returned for revision.

Non-goal. This lock governs repo-reality claims and does not govern higher-level QA intent that does not assert repo-resident loci.

Environment variable name governance (no QA-time minting or silent normalization)

Environment variable names referenced in QA plans, step logs, OPS tasks, implementation prompts, review packs, and QA evidence schemas are governed interface surfaces, not free text. A QA plan MUST NOT add a new environment variable name “because it would be useful,” and MUST NOT carry forward an unapproved variable name merely because it appeared in a prior iteration.

No QA-time env var minting. Live QA (including Moon Loop execution) MUST NOT introduce new environment variable names as runtime requirements, rails pins, or required evidence keys. If a workflow would require a new environment variable name to function, treat that as development work under PO approval: the variable name MUST be explicitly defined and documented in canon before any QA plan relies on it.

Mission-critical environment-variable preservation. When the PO provides deployed environment facts, plans and reviews MUST preserve exact key spelling, environment context, provider context, redacted value posture, requiredness, and secret-bearing status until the facts are routed into an exact applicable HDE-Build Notes addendum, identified by number and title, and the permanent infrastructure home. Do not normalize, collapse, rename, or replace supplied deployed facts with OPEN/TBD while they remain live.

Key-name drift and migration. Environment-variable key-name drift MUST be handled through OPS discovery, OPS change, an exact applicable HDE-Build Notes addendum, or permanent canon update, not by deferral or silent correction. A deprecated or alias key may be discussed only when labeled as deprecated drift, compatibility fallback, migration target, observed evidence, or configuration ambiguity. Review and closeout artifacts MUST distinguish canonical key migration or configuration ambiguity from implementation behavior failure.

MODO\_\* variables are forbidden. Any environment variable name beginning with MODO\_ is non-canonical for Glow/HDE QA planning and QA execution. QA plans, QA runbooks, and QA evidence schemas MUST NOT introduce, require, or depend on MODO\_\* variables for PASS/FAIL or as required evidence structure (including required header fields, manifests, or required schema fields).

Legacy handling (non-binding only). If an already-approved plan or previously captured QA artifact includes MODO\_\* keys, treat them as diagnostic-only inert placeholders: they MUST NOT be required for PASS/FAIL, MUST NOT be treated as required evidence keys, and MUST NOT be used as proof of rails posture or execution configuration. Remove them in the next plan revision and do not replicate the pattern.

Review posture: any required reliance on an unapproved environment variable name, including any MODO\_\* name, is a mechanical blocker until removed, canon-defined, classified as OPS-discoverable, or explicitly labeled as deprecated drift or compatibility evidence.

If QA must create a file that has no prior canonical existence, the relevant step MUST include:

- exact mkdir \-p and write instructions (no placeholders),  
    
- a one-line purpose (what the file proves and why it exists),  
    
- explicit PASS and FAIL predicates tied to the file’s contents.

QA may create folders/files only under audit/\*\* or artifacts/**. Any instruction that implies creating or writing outside audit/** or artifacts/\*\* is nonconforming.

Plans MUST separate pre-existing artifacts (expected to exist before the QA run) from QA-run artifacts (created during execution). Preflight “presence” checks MUST only gate on pre-existing artifacts.

Plan-created outputs (explicit creation rule)

If a QA plan requires creating a file, it MUST name the exact repo-relative path and filename that will be created as a plan-created output.

Required creation clarity:

- How — explicit, runnable creation instructions that produce the file at that path and create parent directories when needed  
    
- Why — one sentence stating the proof obligation, deliverable posture, or required outcome the file satisfies

Evidence-bearing created files MUST be reproducible. The plan MUST include enough creation detail to reproduce the file deterministically and unambiguously, including required inputs and the stable structure or content it must contain.

Provenance labeling posture. The plan SHOULD label each mentioned file path as repo-resident or plan-created. Missing labels are non-blocking only when the file is clearly a run-produced deliverable and the plan still provides the required how, why, and exact creation path.

Review-only posture (fixed artifacts). If a plan states “Commands: None required” and lists fixed-path artifacts as required deliverables, those artifacts MUST be pre-existing (canon-defined or audit-proven) before the step begins. If generation is required, the plan MUST include explicit creation commands and MUST classify the outputs as QA-run artifacts.

Repo-path correctness (code deliverables). When a plan lists a repo code path as a required deliverable (for example, for an existence check), the path MUST resolve in-repo as written. If an architectural alias is used, the plan MUST record an explicit mapping note (alias path to repo path) and the check MUST validate the repo path.

Helper scripts (non-substitutive). Helper scripts created to collect or format evidence MAY be added, but they MUST NOT substitute for required deliverables and MUST NOT change PASS/FAIL predicates unless the plan is revised.

Epic number (\<NNN\>) is the zero-padded 3-digit epic number (example: 022). When an epic ID is HDE-EPIC022, then \<NNN\> is 022\.

Close-pack filenames (canonical) Epic close-pack artifacts MUST use:

- audit/EPIC-\<NNN\>\_close\_report.md  
    
- audit/EPIC-\<NNN\>\_MANIFEST.json

Close-pack path-proof siblings (required) The close report and manifest are governed artifacts and MUST each have a co-located path-proof transcript:

- audit/EPIC-\<NNN\>\_close\_report.md.path\_proof.txt  
    
- audit/EPIC-\<NNN\>\_MANIFEST.json.path\_proof.txt

Close-pack validation checks MUST verify that the path-proof transcripts exist and match the on-disk bytes of their parent artifacts.

Do not create parallel close-pack artifacts under alternate spellings (examples of disallowed alternates: EPIC022, EPIC\_022, `audit/epic-022/<SUBPATH>`).

Close-pack manifest key\_outputs is a named binding map (object). audit/EPIC-\<NNN\>\_MANIFEST.json MUST include key\_outputs as a JSON object (map) where:

- each key is a stable pointer name (string), and  
    
- each value is a repo-relative artifact path (string).

key\_outputs MUST NOT be a list.

Close-pack validation checks MUST validate the named bindings (keys \+ exact paths), not list membership.

Epic QA root (canonical) Epic QA root directories MUST be lower-case and MUST use:

- audit/qa/hde-epic\<NNN\>/ (example: audit/qa/hde-epic022/)

When this guide uses audit/qa/hde-epic\<NNN\>/, it means the epic QA root audit/qa/hde-epic\<NNN\>/.

Plans and implementations MUST NOT introduce parallel alternate spellings for the same epic (examples of disallowed alternates: audit/QA/, audit/qa/HDE-EPIC022/, audit/qa/hde-epic022-v2/).

Doc-Delta surfaces (draft \+ epic-scoped capture) Doc-deltas use a two-surface pair. In the Plan and PR, both surfaces MUST use concrete filenames (no placeholders).

1. Draft / staging surface (token binding surface). A doc-delta draft MUST live under: audit/docdeltas/hde-epic\<NNN\>\_doc\_deltas.md Where hde-epic\<NNN\> is the canonical lowercase epic QA slug (for example hde-epic022). This draft surface is the primary surface for doc-delta evidence binding when a doc-delta deliverable is claimed.  
     
2. Epic-scoped capture surface (stable QA record). The epic MUST also capture an epic-scoped doc-delta record under: audit/qa/hde-epic\<NNN\>/00\_meta/doc\_deltas.md

This capture file is the stable record surface for the epic’s QA and closeout narrative. It MUST NOT be replaced by a placeholder reference.

The approved plan’s Doc Delta Capture step (Step-0B or equivalent) MUST confirm these two fixed-path artifacts exist.

Step-0B preservation rule. The Doc Delta Capture step is additive verification by default. It MUST NOT overwrite, truncate, replace, or template-over existing generator-owned, previously produced, or proof-bearing doc-delta surfaces with “no deltas,” empty placeholder content, or generic no-delta scaffolding.

The Doc Delta Capture step may emit “no deltas” only when no proof-bearing doc-delta content exists for the epic. If either fixed doc-delta surface already contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content, Step-0B MUST preserve that content and confirm, append, or copy only as explicitly required by the approved plan.

If Step-0B overwrites proof-bearing doc-delta content, classify the issue as an evidence assembly or tooling failure, not product behavior failure. The remediation record MUST preserve the original failed receipt when available, restore the proof-bearing content from current governed source or approved remediation input, and rerun the affected approved check until the final evidence stream is auditable.

The plan’s evidence bindings must clearly distinguish these two surfaces: draft (binding) vs epic-scoped capture (record).

Doc-Delta capture integrity (mandatory). At close, the draft and epic-scoped capture doc-delta files MUST be byte-identical. If they differ, the Doc-Delta capture step MUST remediate and rerun until `diff` returns exit code 0\.

Doc-Delta content completeness (mandatory). Doc-Delta content MUST include PF refs per entry, sufficient to trace each change back to PF-canon drains. PF refs MUST follow the titles-only rule used elsewhere in this document.

Legacy artifacts If legacy artifacts exist under non-canonical names, treat them as deprecated. Do not create new artifacts under deprecated patterns.

## 0.6 Discipline

### 0.6.1 Canon-first planning

Implementation Agents MUST treat PF-Canon as the primary source of facts for epic planning and QA.

Plans MAY check PF documents during planning and review. Planning artifacts MAY instruct the reviewer or planner to consult PF documents (including Reality Audits) to confirm what PF currently states.

Plans MUST NOT mandate PF document updates. Planning artifacts MUST NOT require updates to any PF documents as part of the plan’s PR or OPS deliverables, acceptance posture, tracked issues, confirming artifacts, or completion criteria.

Reality Audits updates are PO-only. Updates to Reality Audits are a manual PO operation only. PR scope MUST NOT include Reality Audits edits, and plans MUST NOT mandate or schedule Reality Audits updates inside PR or OPS work.

Allowed documentation posture inside plans (informational only). Plans MAY include a “Doc deltas capture” or “Doc delta candidates” note, but these notes MUST be explicitly non-mandatory and MUST NOT be expressed as a required PR or OPS task. Any PF doc maintenance implied by those notes is PO-owned and out of plan scope.

How plans MUST express reality and existence confirmation. If a plan requires confirming whether a component, route, contract, or locus exists, the plan MUST express confirmation in one of these allowed forms:

- PF check (allowed): “Check Reality Audits for the current recorded existence/locus statement.” This is a read-only check and MUST NOT imply an update.  
    
- Repo-local evidence (required when PF is silent or insufficient): capture confirmation as repo-local evidence (for example: deterministic command output recorded into an audit artifact, a governed gate log, a QA step-log entry, or a test/probe result). The plan MUST NOT require turning that result into a PF update.

Review posture (blocking condition). Any plan that mandates a PF document update (including Reality Audits) as part of PR or OPS deliverables MUST be treated as non-portable and returned for revision.

Before drafting any QA Plan or Implementation Plan for a Live QA epic, they MUST:

- Read Glow Infrastructure, Glow QA Guide, each exact applicable HDE-Build Notes addendum by number and title, and the applicable phased HDE-Build Checklist to collect current planning facts. Consult HDE Phased Epics only as a historical archive of completed epic records.  
  - environment and infrastructure facts  
  - QA tokens  
  - epic D-goals and exclusions  
- Use canonical infra/env values (for example, production service name, base URL, and DB instance/schema) from those documents directly, instead of treating them as unknowns.  
- Reality Audits consultation is required during QA planning whenever a Live QA Plan is drafted, reviewed, or approved.  
- If a QA plan names any repo-resident locus, the reviewer SHOULD consult Reality Audits before approval to reduce fabricated or stale locus assumptions.  
- This consultation is planning-time and read-only. QA plans MUST NOT mandate Reality Audits edits, and QA execution MUST NOT include Reality Audits updates as a required output.  
- If Reality Audits appears inconsistent with another allowed repo-reality source, treat it as a reality ambiguity. Do not assert a reconciled locus as fact inside the plan.  
- Consult Reality Audits for any epic touching: ingestion vendors, admin bundle behavior surfaces, live QA in prod, schema migrations.  
- When Reality Audits consult is required, planning artifacts MUST include a short “Reality Audits Anchors” note that lists:  
  - the Reality Audits components consulted (by title)  
  - the key pathnames/loci from Reality Audits that this epic will touch  
- This note is traceability-only. It MUST NOT duplicate Reality Audits content, and it MUST NOT be presented as a required Live QA deliverable or a required acceptance token.  
- Reality Audits consult is non-token closure evidence. It is not a gateable token and MUST NOT be represented as a token (for example: no REALITY\_AUDIT\_OK, no Reality Audits\_OK) on a closure pack acceptance roster.  
- Reality Audits consult scope: Reality Audits consult may be used to inform epic planning, implementation planning, and QA planning. It MUST NOT be used for PR analysis, PR review, or post-hoc “blockers” in a merge decision.  
- In closeout review, Reality Audits current-reality context may support surface framing, repo-root context, or contradiction detection, but it does not by itself prove closure, satisfy acceptance, or block closure. If Reality Audits context appears to contradict an exact applicable HDE-Build Notes addendum, governed QA evidence, approved implementation evidence, or close-pack proof, record the contradiction as drift or an adjudication item and route it rather than treating Reality Audits as final closure authority.  
- Reality Audits audit observations MUST route to their owning canon homes by title and MUST NOT be converted into phased-checklist task deltas, remediation scope, implementation deltas, evidence homes, or acceptance tokens by assumption. If an audit observation appears to imply new work, record the classification and routing question for Product Owner or owning-canon adjudication before treating it as executable scope.  
- Drift handling (protocol stub): If any Reality Audits statement appears to contradict PF canon, record a drift item (cite the PF canon requirement and the Reality Audits statement, explain the contradiction, and propose the minimum safe posture). Route the drift item to the Product Owner for adjudication. Do not resolve by ad-hoc interpretation inside the plan.  
- Reality Audits are post-epic audit inputs: they reflect the latest closed-epic snapshot, not an in-flight PR truth source.  
- Classify the drift item into exactly one bucket (tentative): canon defect, implementation drift, or necessary reality shift.  
- Do not fix by assumption. No plan, review, or QA artifact may treat the contradiction as resolved unless the Product Owner adjudicates.  
- Resolution routing is PO-owned: canon update, implementation remediation, or formalized exception with canon follow-up.  
- No execution-time Reality Audits consult artifacts. Live QA plans, runbooks, and step logs MUST NOT introduce required deliverables whose purpose is Reality Audits consult capture (for example pf23\_consult.md, “Reality Audits capture” steps, or operator commands intended only to produce Reality Audits trace artifacts). If a trace anchor is desired beyond the “Reality Audits Anchors” note above, it MUST remain in plan text only and MUST be informational-only (non-gating).  
- Reality Audits consult is non-token closure evidence (no REALITY\_AUDIT\_OK). Plans and implementations MUST NOT mint, claim, or reference REALITY\_AUDIT\_OK (or any similar “Reality Audits consult completion” acceptance token) unless and until Governance registers such a token.  
- Reality Audits consult scope MUST be represented as a consult requirement and closure evidence, not as an acceptance token. When Reality Audits consult is required, the work MUST capture a short consult record that includes:  
  - the Reality Audits Anchors list (components used and loci/pathnames pulled)  
  - a brief “what changed / what did not” summary scoped to the epic or plan  
- This consult record MUST live in existing closure surfaces (for example, the epic-scoped meta record under audit/qa/hde-epic\<NNN\>/00\_meta/ and/or the epic close report). It MUST NOT appear in the acceptance token roster.  
- Implementation Agents MUST NOT treat canonical infra/env details that PF-Canon or an exact applicable HDE-Build Notes addendum explicitly defines as PO inputs unless the source explicitly marks them OPEN/TBD.  
- When a plan, review artifact, remediation guide, or epic document includes an infra or ops dependency, it MUST bind each required value in exactly one of these postures:  
  - Glow Infrastructure-derived posture: cite the exact Glow Infrastructure fact directly.  
  - HDE-Build Notes-addendum posture: cite the exact applicable addendum by number and title when that addendum explicitly supplies the live fact.  
  - OPS-discoverable posture: define the bounded OPS discovery task that will safely confirm or record the fact without exposing secrets.  
  - Glow Infrastructure-gap posture: identify the exact missing Glow Infrastructure fact and mark the affected task or claim blocked by missing Glow Infrastructure infrastructure inventory only when no exact applicable HDE-Build Notes addendum supplies the fact and safe OPS discovery cannot resolve it before execution.  
- The artifact MUST NOT rely on placeholder ownership or vague sourcing such as infra to provide, ops to confirm, ask infra, await ops details, infra-owned without a concrete Glow Infrastructure-backed value or an exact applicable HDE-Build Notes addendum fact, or guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or guessed governed evidence roots.  
- Any infra or ops task named in a plan MUST, where applicable, state the target provider, target project, target service, target repository, target base URL or port, target database instance or schema, exact config key name, exact governed evidence root or QA root, and the exact expected value or exact Glow Infrastructure, exact applicable HDE-Build Notes addendum, or OPS-discovery value source.  
- QA and Live QA plans MUST NOT guess or redefine Glow Infrastructure-owned environment bindings or service facts. If Glow Infrastructure is silent but an exact applicable HDE-Build Notes addendum explicitly speaks, use the addendum posture. If both are silent and the fact can be safely discovered, use OPS-discoverable posture. If neither applies, stop at the explicit Glow Infrastructure-gap blocker or valid deferral classification and record the intended Glow Infrastructure update as a doc-delta or drain target for PO action.  
- Any QA Plan or Implementation Plan that asks the PO to “provide” such a value without classifying the source as Glow Infrastructure-derived, exact-applicable-addendum-derived, OPS-discoverable, or Glow Infrastructure-gap is non-conforming and must be corrected before use.  
- When a plan, QA plan, remediation guide, review pack, or OPS guide documents a non-prod local-style access address, the default documented client access host MUST be `127.0.0.1` with the correct port and endpoint path.  
- This is a client access convention only. It MUST NOT be used to rename or obscure the real Glow Infrastructure service identity, the real prod-facing address, or the server bind address.  
- Production and prod-facing surfaces MUST keep the real hosted address recorded in canon, even when the operator is working from Codespaces, CI, or another remote shell.  
- If a dev or QA surface cannot actually be reached at `127.0.0.1` from the intended operator context, the document MUST state an explicit exception and the real access route. `localhost`, guessed hostnames, guessed forwarded URLs, or placeholder wording MUST NOT be used as the default documented address.  
- Post-Audit ADRs (decision capture). When an audit or plan reveals recurring ambiguity that cannot be resolved by retrieving the governing PF-Canon passages, the Implementation Agent SHOULD capture the ambiguity as a Post-Audit ADR and route it to the Product Owner for adjudication.  
- ADRs are clarification artifacts, not acceptance criteria. They MUST NOT introduce new acceptance tokens, new QA obligations, or new gates.  
- ADR minimum sections (paste-ready headings; fill all fields; keep each section brief):  
  - ADR-\<EPIC\>-\<DOMAIN\>-\<NNN\> — \<title\>  
  - Date: \<YYYY-MM-DD\>  
  - Status: Proposed | Accepted  
  - Decision owner: Product Owner (final), Lead Dev or Implementation Agent (draft)  
  - Context (include audit pointer(s) and plan pointer(s))  
  - Decision (numbered D1, D2)  
  - Alternatives considered  
  - Consequences (positive, negative, tradeoffs)  
  - Canon impact (doc-delta targets by title only)  
  - Non-goals (explicitly list what this ADR does not change)  
- Doc deltas that drain ADR decisions into canon MUST be paste-ready. Each doc delta entry MUST include:  
  - Target doc (title only) and target section  
  - Current proof excerpt (verbatim; 1–5 lines)  
  - Replacement block (exact replacement text for the excerpt scope)  
  - Why (one sentence; KISS)  
  - Evidence pointer(s) (audit, plan, PR diff, or runtime proofs)

### 0.6.2 Rails and environments (closed-rails vs open-rails QA)

QA Plans MUST distinguish between:

- Closed-rails determinism checks that run locally with rails closed (for example, serializer and bundle determinism jobs)  
- Open-rails production checks that run from a permitted console against the production HD Engine service and database as defined in Glow Infrastructure and, only for an explicitly covered point, an exact applicable HDE-Build Notes addendum identified by number and title

Open-rails testing may be included in implementation or QA planning when live operational information is necessary and the work is otherwise in scope. The plan MUST bound the task, identify PO authorization, preserve secret safety, state what may be recorded, state what must not be recorded, and avoid treating vendor smoke success as broader conformance than it proves.

If open-rails proof or discovery is required, the plan MUST sequence the work explicitly as PR preparation or harness work, bounded PO-authorized OPS discovery or OPS open-rails execution, then QA verification or evidence binding as applicable. Open rails, live vendor access, credentials, or PO-authorized execution are not deferral reasons by themselves; they are OPS/QA sequencing facts unless the task is unsafe, unauthorized, out of scope, phase drift, or blocked by a real unresolved dependency.

Open-rails failure classification. A failed open-rails run MUST be classified before it is treated as product behavior failure. Possible classes include credential issue, config issue, vendor account or tier limitation, endpoint unavailability, vendor contract mismatch, request-shaping defect, response-mapping defect, infrastructure gap, rate-limit or retry posture, external outage, product implementation defect, or QA plan expectation mismatch.

Deterministic parity scenario requirement (acceptance). Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor attempt scenarios) MUST be reproducible under determinism pins \+ closed rails, without reliance on external network or a live database.

Non-canonical env pins are forbidden as Live QA requirements. Live QA steps that produce governed bytes/evidence MUST use only the canonical determinism pins (LC\_ALL, LANG, TZ) and the rails posture as applicable. Plans MUST NOT introduce non-canonical pins (for example PYTHONHASHSEED) as approval or execution requirements.

Determinism is achieved by ordering, not interpreter knobs. If a step or tool is nondeterministic due to hash-order dependence, it MUST normalize ordering explicitly (sort keys, sort lists, avoid unordered set iteration) rather than relying on QA-only rails or interpreter settings.

Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts.

Allowed fallback: if real-codepath deterministic triggering is not feasible, use a deterministic stub layer only to the extent required to produce the canon error envelope and parity artifacts (no live I/O).

Acceptance proof MUST consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and must be indexable under governed evidence surfaces (human index \+ machine mirror in the same PR).

Determinism pins (for example locale/time settings) apply to determinism-sensitive jobs.

When a step is explicitly described as “prod via Codespaces,” the plan MUST:

- assume an open-rails posture sufficient to reach prod  
- prove determinism via repeatable runs and evidence, not by pretending that rails are closed

### 0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)

For Live QA epics, prod behavior runs in a prod-facing environment.

Any D-goal that is about behavior (for example compat math, narrative generation, vendor ingest, “full product payload” for a pair) MUST define a primary exercise context that can reach the production HD Engine service and DB as defined in Glow Infrastructure.

Examples include:

- a terminal with hdctl configured to call the production base URL  
- an admin GUI in a browser hitting a Railway route

Codespaces is a console and artifact sink, not the prod executor.

Codespaces MAY:

- run offline tools against a checkout of the same code/commit as prod  
- receive and store artifacts (logs, JSON, headers, transcripts) under `audit/qa/hde-epic<NNN>/`  
- run offline validation against those artifacts using source-grounded commands permitted by the owning QA plan

Codespaces MUST NOT be treated as “where prod runs” unless the step explicitly:

- describes how the commands in Codespaces are reaching the production service over the network  
- uses that connection as the exercise context

Codespaces environment provenance capture (optional; non-gating). A Live QA plan MAY include a Step-0 “Codespaces snapshot” when execution occurs from Codespaces, but it MUST be explicitly labeled optional and MUST NOT be required for plan approval, execution, or acceptance review.

Reviewers MUST NOT use the presence, absence, or contents of any “Codespaces snapshot” artifact to decide PASS vs REMEDIATION NEEDED.

This guide does not define Codespaces config checklists or snapshot schemas. Consult Glow QA Guide (titles-only) for Codespaces configuration guidance.

Behavior vs artifact phases. Live QA steps that refer to behavior MUST separate:

- a behavior run phase (where the behavior is exercised in a prod-facing environment)  
- an artifact capture & analysis phase (where artifacts from that run are copied or uploaded into the Codespace under audit/qa/hde-epic\<NNN\>/ and analyzed offline)

The QA Plan MUST be clear about both phases for each such step.

Codespaces-only runs are local smoke checks. Steps that run hdctl or other logic purely inside Codespaces (for example under closed rails with no network) MAY be included as local smoke checks but MUST NOT be used to satisfy prod behavior tokens.

When a token is about prod behavior, its satisfaction MUST be tied to a prod-facing behavior run as described above, with artifacts captured under audit/qa/hde-epic\<NNN\>/.

### 0.6.4 PO Live QA vendor-first scope

For epics that include PO-run Live QA sessions:

Purpose: PO Live QA is a vendor-first activity. Its primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.

What belongs in PO Live QA: Steps in a PO Live QA session MUST be scoped to vendor flows, including (as applicable to the epic):

- vendor-backed BodyGraph resolution (for example bg:resolve \--source=vendor in dry-run or controlled modes)  
- vendor-backed compat calculations (for example compat via vendor-backed inputs or the Admin bundle path once defined by other PF docs)  
- vendor error conditions and edge cases (for example malformed input, missing data, timeouts) that the epic chooses to exercise

What does not belong in PO Live QA: Steps whose only purpose is:

- proving connectivity (for example /internal/version identity pings)  
- re-running determinism, serializer/guard, or sanity checks that are already covered by CI/QA/infra

These checks MUST NOT be treated as part of the PO’s Live QA workload. These checks remain CI/QA/infra responsibilities and may be referenced as pre-work or prerequisites, but they are not, by themselves, a reason to convene a PO Live QA session.

Codespaces rails in PO Live QA: In the context of PO Live QA:

- Codespaces is, by default, an artifact sink and offline analysis console (see §0.6.3).  
- Codespaces MAY temporarily open rails (for example setting SAFE\_MODE=0, ALLOW\_NETWORK=1, base URL pointing to production) only when:  
  - the goal of that step is to exercise a live vendor flow as described above  
  - the rail-opening is documented (env vars set, commands logged, and artifacts captured under audit/qa/hde-epic\<NNN\>/logs/)

Showcompat source and rails posture (Live QA)

Live QA plans that invoke `showcompat` MUST identify the selected input and source mode and apply the corresponding rails and preconditions defined by HDE-CLI-API-Vendor-Ref. Vendor-sourced runs require the applicable vendor rails. The implemented command also supports database and file or standard-input paths, so vendor rails and CLI argument count MUST NOT be treated as universal `showcompat` predicates.

Post-step restore: after the vendor step completes, restore default rails posture (SAFE\_MODE=1, ALLOW\_NETWORK=0) for subsequent non-vendor checks.

For non-vendor behavior (serializer determinism, guard proofs, sanity pipeline), Codespaces MUST NOT be used as a surrogate “prod” environment in PO Live QA; those checks belong to CI/QA/infra.

Plans or runs that:

- assign non-vendor checks to the PO’s Live QA workload  
- treat vendor-neutral smoke checks as PO Live QA

are non-conforming and must be corrected by moving those checks into CI/QA and keeping the PO session focused on vendor behavior.

### 0.6.5 Fail-closed to spec gap

If, during planning, PF-Canon appears ambiguous or incomplete:

- Implementation Agents MUST treat the affected check as blocked by a spec gap  
- capture enough evidence to describe the gap  
- route it to the permanent owning canon or, when one exact current addendum explicitly owns the temporary point, to that HDE-Build Notes addendum by number and title; do not route in-flight scope to HDE Phased Epics  
- instead of improvising new rails, redefining environment semantics, or asking the PO to guess

### 0.6.6 Filesystem naming (directories)

Rule (global). All directories in the repository and application codebase MUST use lowercase ASCII names.

Scope note. This rule governs directory names only. Filenames with uppercase characters are allowed unless separately forbidden by canon.

Verification posture. Enforcement scans for this rule MUST scan directory names (for example with find \-type d). Scanning file paths (-type f) is over-broad because it includes filenames and can produce false failures under this directory-only rule.

Introducing any mixed-case or uppercase directory name is non-conforming.

Under governed roots (for example audit/**, docs/**, artifacts/\*\*), mixed-case directories are a QA failure, not cosmetic drift.

Remediation posture (when drift exists). If mixed-case directories exist, they are treated as legacy drift and MUST be normalized to lowercase, not copied forward into new work.

Evidence discipline for renames. Any renames that affect governed artifact paths MUST be accompanied by the required index and mirror updates (Human Evidence Index, Machine Mirror, and path-proofs) in the same PR, per the evidence discipline.

### 0.6.7 Mechanical evidence (Live QA)

When the process says “QA verifies X,” “QA proves Y,” “QA runs Z,” etc., the relevant plan segment must indicate what evidence will be produced to demonstrate that the verification happened and what the result was.

If a step is a PO action (for example, approving a plan, providing a prod URL, or approving a QA slice), the PO action must leave behind at least one inspectable artifact, not just a chat comment.

Acceptable evidence includes step logs, filesystem captures, CLI outputs, tool screenshots, etc. (Evidence MUST be secret-free; scrub tokens, credentials, PII, and private URLs.)

Per-step evidence expectations are defined below. KISS minimum outputs (required) are mandatory.

Each Live QA check/step MUST produce exactly one primary step log for that check (the default evidence artifact for the check), at:

- audit/qa/hde-epic\<NNN\>/checks/\<check\_id\>/primary.log

Each Live QA run MUST produce a step-logs manifest, at:

- audit/qa/hde-epic\<NNN\>/qa\_step\_logs\_manifest.json

The manifest MUST enumerate, at minimum: check\_id, status, and the primary.log path for each check.

The step-logs manifest is a JSON object, not JSONL; do not emit or require a JSONL variant (for example `qa_step_logs_manifest.jsonl`).

The step-logs manifest is a governed artifact and MUST have a sibling path-proof transcript, at:

- audit/qa/hde-epic\<NNN\>/qa\_step\_logs\_manifest.json.path\_proof.txt

For ledger-refresh or evidence-discoverability checks, the step MAY treat the current-run step-logs manifest pair as a decisive deliverable. When it does, the approved PASS criteria MUST name:

- the required updater or refresher exit-status artifact  
- the current-run step-logs manifest and its sibling path-proof transcript  
- any required discoverability lookup artifacts and the exact found=True condition they must record

For such a step, the manifest content requirement is not just file existence. The manifest MUST record check\_id, status, and log\_path for the current executed checks captured by that run.

If a step executes multiple commands to refresh or verify this ledger state, the primary.log command field MUST preserve execution order as one explicit pipeline or one explicit ;-joined sequence, not as an ambiguous paraphrase.

When these criteria are used, a Moon Loop rerun may re-run the updater, rebuild the current-run manifest pair from the governed check headers, regenerate the named lookup artifacts, and rewrite primary.log from the concrete refreshed artifacts without being treated as scope expansion, provided the approved deliverables and PASS criteria do not change.

Posture-only steps (no validation logic executed). If a check is posture-only and records TOOLING\_BLOCKED, the step MUST still:

- Write the per-check primary.log with status: "TOOLING\_BLOCKED" and include a one-line posture note beginning with UNPROVEN/TOOLING\_BLOCKED: (what is missing / why unproven).  
- Upsert a manifest entry with status: "TOOLING\_BLOCKED" and log\_path pointing to the per-check primary.log (and refresh the manifest path-proof in the same step).  
- MUST NOT claim any \*\_OK tokens.

Each QA step MUST explicitly name the expected artifacts (paths and filenames) it will produce under the canonical QA root audit/qa/hde-epic\<NNN\>/. Naming the per-check primary.log satisfies this requirement by default.

If a step claims it updated qa\_step\_logs\_manifest.json, the step’s primary.log SHOULD include a minimal filedump excerpt of the new/updated manifest entry (for example: check\_id, status, log\_path) to prevent ambiguous “done vs next steps” ledger state.

Steps that are “validate existing canon evidence” SHOULD prefer referencing existing governed artifacts in the primary.log (paths-only) over generating duplicate snapshots. Do not create extra artifacts that do not change PASS vs REMEDIATION NEEDED.

Additional required artifacts (files beyond the per-check primary.log \+ manifest) are allowed only when they are acceptance-decisive and already canonized as a governed evidence family/path. If an artifact is diagnostic-only (does not change PASS vs REMEDIATION NEEDED), it MUST NOT be required for plan approval or Live QA execution; it may be included only as optional diagnostics.

When a Live QA step validates same-change coherence across more than one existing governed evidence family, the plan MUST name the full coherence set and treat it as one acceptance-decisive unit.

For such a step, PASS criteria MUST state both:

- that each named family remains present before and after the writer or generator run  
- that the writer or generator exit status for the same run is successful

If one named family disappears, is omitted from the before/after capture, or the writer or generator exits non-zero, the step MUST fail exactly as the approved plan defines.

A QA step that is claimed as complete, PASS-ready, or sufficient to satisfy a gating condition MUST prove governed pass-state in its primary.log. File existence, non-empty output, or the absence of the literal text `MISSING` are not sufficient by themselves.

Unless the approved plan explicitly defines a different decisive signal, the primary.log for a passed step MUST record an explicit command outcome that shows success, and QA completeness MUST require `[exit_code] 0` or an equivalent canonical success marker grounded in the executed command output.

When a generator, close-pack rule, or acceptance-binding rule depends on Live QA completeness, it MUST bind to this governed pass-state requirement rather than to file presence alone.

This kind of step is verification only. It does not reclassify legacy versus canonical homes by itself, and it does not authorize new binding targets.

Each QA step MUST explicitly name which repo files it will touch/edit. Plans and implementations MUST NOT introduce parallel alternate QA roots or ad-hoc epic slugs.

For PO actions that are used as QA inputs (for example: providing production service/DB identifiers, approving a QA slice), the action MUST be recorded in an inspectable artifact under the canonical QA root—typically in the primary.log of the step that consumed the PO input. It is not sufficient to “say it happened” without leaving inspectable evidence.

### 0.6.8 Operational guardrails

Live QA plans/runbooks MUST NOT include VCS workflow content (branches, commits, PRs, cherry-pick guidance) and MUST NOT instruct or discuss branch/commit/PR operations.

Live QA plans/runbooks MUST NOT gate PASS/FAIL on VCS state (for example “working tree clean,” “on correct branch,” “commit matches expected,” or any similar VCS-derived condition).

Limited, read-only git commands MAY be included only as optional, non-gating repo-root sanity checks (“this is a repo” / “repo root exists”). They MUST be non-mutating and MUST NOT print or rely on branch names, commit SHAs, or PR identifiers. If a git sanity check fails, the check outcome is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR), and execution MUST proceed via non-git verification paths.

If any git information is captured at all, it is traceability-only and MUST NOT block execution or acceptance decisions.

### 0.6.9 Plans are pointers; QA planning is post-implementation

Core rule: An Epic PLAN and CRD are pointers to canon and governed artifacts. They are not the place to restate or rebuild canon (token definitions, schemas, CLI semantics, env matrices, etc.).

Do not rebuild canon inside an Epic PLAN/CRD. The PLAN/CRD may reference canonical docs by title only and point to canonical artifact paths. If review “needs” more definition than canon provides, the correction is a doc-delta (update canon) or a governed artifact — not duplicating canonical content inside the PLAN/CRD.

QA planning happens after implementation (and after D0 discovery). A step-by-step QA plan (Live QA step lists, per-step Deliverables blocks, copy/paste command blocks, harness invocation details, etc.) is not an Epic Planning deliverable.

The PLAN/CRD SHOULD provide only:

- titles-only acceptance intent (what must be true)  
- the QA posture (e.g., “Live QA required”)  
- pointers to where QA artifacts will live

The detailed QA Plan is authored/updated during implementation and QA work, and must satisfy the mechanical evidence requirements in §0.6.7 and §1.1.4–§1.1.8.

Approval posture: avoid planning stalls. Reviewers SHOULD NOT block PLAN/CRD approval by demanding:

- a full token/evidence matrix embedded in the PLAN/CRD  
- a fully specified Live QA step list before implementation exists

If a token name/semantics is unclear at planning time, treat it as Deferred (out of scope) and capture the dispute as an ADR/doc-delta rather than debating inside the PLAN.

Live QA plan review outcome discipline (Blockers vs Caveats). Reviewers SHOULD keep Live QA plan approval and execution capture separate: the approval gate is about clarity, scope, and evidence routing — not about pre-creating execution artifacts.

Live QA Plan approval is an operational-readiness review. Approve when the plan is safe, self-contained, phase-bounded, and clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict.

Do not return a Live QA Plan for revision solely for exact-command mismatch, command invocation preference, rendered escape characters, formatting, code-block or quote-block style, step-log header polish, path-proof field polish, canonical JSON compactness wording, or evidence-ledger byte-shape polish.

A Live QA Plan approval blocker is valid only when the issue creates concrete operational harm to safe execution, required QA step coverage, required deliverable existence, explicit PASS or FAIL verdictability, rails posture, secret handling, live-provider or external-action boundary, public/private surface boundary, token truth, acceptance overclaim, source authority, self-contained execution, evidence trust, proof target identity, repo-locus truth where an existing locus is required, OPS/QA/implementation category separation, phase scope, or closeout truth.

At plan approval, the plan must identify what each check proves, what counts as PASS, what counts as FAIL, where the decisive receipt lands, which governed evidence family or evidence class supports the verdict, and how token claims are avoided unless admitted under §1.1.9 and in scope. Final byte-level details of canonical JSON compactness, field ordering, path-proof transcript shape, step-log header shape, mirror-record shape, or evidence-index refresh mechanics are closeout or execution validation issues unless their absence prevents evidence identity, decisive receipt, governed proof, or verdictability.

Commands in a Live QA Plan are operational instructions, not canon contracts, unless the plan states that an exact invocation is required and the owning PF home requires exactness for the operational result. If an equivalent safe command can produce the same proof target under the same rails, evidence family, and PASS or FAIL predicate, exact-command mismatch is a Caveat, Suggestion, or execution note rather than a Blocker. The exact command actually used must be captured in governed QA evidence.

A Live QA Plan MAY create QA-only harness scaffolding during Step 0 when the harness is limited to QA evidence capture and does not create product behavior. Reviewers MUST NOT require repo-existence proof for a QA-created harness that the plan explicitly creates during the QA run. A QA-created harness issue is a Blocker only when creation is not executable, unsafe, out of scope, changes implementation behavior, proves the wrong target, cannot emit a verdict, or cannot produce or point to required governed evidence.

A Live QA plan, execution report, or closeout review may define a check as proof-only only when its purpose is to prove current state and not to perform implementation, PF edit, OPS action, evidence-index edit, token-map edit, route or public payload expansion, or closeout action.

When a check is proof-only, the plan or result evidence MUST state the non-action boundaries and verify that no prohibited action occurred.

A proof-only PASS proves only the named proof target and governed evidence posture. It MUST NOT imply implementation completion, PF edits, OPS completion, final closeout, live-provider behavior, public surface expansion, or applicable phased HDE-Build Checklist drainage unless those stronger claims are separately approved and proven.

A reviewer who blocks Live QA Plan approval MUST state the operational harm. If no operational harm is shown, classify the issue as Caveat, Suggestion, Nit, or no issue.

Schema authority (templates \+ step-log headers \+ status vocabulary). The Live QA plan template shape, step-log header schema, and status vocabulary are governed by PF27-Canon-Plan-Templates (titles-only). This guide does not restate or extend that schema; any additional header fields beyond the PF27-Canon-Plan-Templates minimum are optional and MUST NOT be required as a plan-approval condition unless PF27-Canon-Plan-Templates is updated to require them.

Header field omissions are format gaps (capture as caveats). If a plan/template expects specific step-log header fields (for example pf\_refs, intended\_tokens, claimed\_tokens) but the tool-emitted primary.log header omits them, record the omission as a formatting caveat in the QA RCA/doc-delta record. Do not reinterpret PASS/FAIL solely on that omission unless the missing field prevents confident verification of acceptance-decisive proof facts.

Token claims in step logs (claims-only semantics). If a step log includes any \*\_OK token names, they are treated as claims:

- Token lists are optional in runbooks; plans must not be approved/rejected based on token-list completeness.  
- On PASS, the step log may claim one or more \*\_OK tokens that the step actually verified.  
- On any non-PASS status, the step log MUST NOT claim any \*\_OK tokens.  
- If a step needs to record intended tokens without claiming them, list them under a distinct label (for example “intended tokens”) rather than using the claim token list.  
- When a PASS-grade step log records both intended tokens and claimed tokens, reviewers MUST compare those sets as part of token-fidelity review.  
- If the intended-token set and claimed-token set match in the governed step evidence, the step MAY be treated as token-aligned for those tokens.  
- If the claimed-token set is narrower or wider than the intended-token set, the QA review MUST say so explicitly rather than implying exact alignment.  
- A narrative QA review does not need to restate every matching token proof line when that alignment is already explicit in the governed step evidence and the step’s approved PASS criteria are otherwise satisfied.  
- When a Live QA plan includes intended tokens in a matrix or rollup view, but the step’s approved Deliverables and PASS/FAIL blocks are deliverable-based, the step block is the decisive contract for the step.  
- If the step’s required deliverables are present and the approved step-level PASS criteria are satisfied, absence of token-by-token proof lines in the narrative review or deliverables report is a reporting caveat, not an automatic blocker, unless token alignment itself is explicitly required by the step block or by governed step evidence.  
- If a QA review states that token-level proof lines were not surfaced, the review MUST record the exact search basis used to reach that conclusion, including the searched token names, searched fields, or searched report sections.  
- Matrix-only intended tokens remain planning metadata unless the step block or the governed step evidence makes token alignment acceptance-decisive for that step.  
- This is intentionally schematic; see the canonical token registry and per-check token semantics for details.

Each step log MUST:

- Include a stable check ID that is consistent across runs.  
- Include a rails snapshot (at minimum: SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, APP\_ENV). Additional env vars may be recorded if helpful. If present, they are diagnostic only and must not be treated as required pins (for example: PYTHONHASHSEED=0).  
- Include the exact command(s) executed (copy/paste-ready).  
- Capture exit codes (where applicable).  
- End with an explicit step outcome classification consistent with the status vocabulary in PF27-Canon-Plan-Templates.

Step-log header writer input exports (per-check requirement)

If a check generates the `primary.log` header through a step-log header writer, the plan MUST supply the required inputs for that check immediately before invoking the writer. It MUST use the exact current writer contract in PF27-Canon-Plan-Templates and MUST NOT rely on values inherited from an earlier check.

Any writer input required by PF27-Canon-Plan-Templates that is missing is a mechanical blocker for plan approval and MUST be corrected before execution.

Moon Loop remediation (allowed; evidence-capture only): if execution already occurred but the header is missing or incorrect due to missing exports, it is allowed to export the required variables, regenerate only the JSON header, and rebuild primary.log by prepending the corrected header line while preserving the existing body bytes verbatim. Record the remediation in the step log notes and do not re-run behavioral steps solely to fix header formatting.

Anti-drift: plans MUST NOT mix patterns where some checks export these variables and other checks omit them while still calling the same header writer.

For Live QA plan approval, review findings MUST be separated into exactly two sets:

- BLOCKERS — independently proven issues that prevent safe faithful execution or prevent reviewers from determining pass/fail for in-scope behavior with confidence. Examples include missing pass/fail criteria, unspecified evidence capture, an indeterminate output location, manual-fill placeholders for semantic outputs or evidence, unvalidated or fabricated repository loci, unsafe or ambiguous commands, commands that cannot be faithfully normalized, or a plan requirement to change production code.  
- CAVEATS — issues that do not prevent safe execution or confident verification, such as harmless presentation defects, partial non-decisive token context, documentation drift that can be captured through a doc delta, or omission of optional diagnostic artifacts.

Token/evidence matrix is a QA ledger artifact. When a token/evidence matrix is required for an epic, it is maintained as a governed QA ledger under the epic’s QA root (see §1.1.9). The PLAN may contain a one-line pointer; it must not embed the matrix. The QA root will be filled in during implementation.

### 0.6.10 Redline bundle construction discipline

Redline bundles for plans, QA plans, and review artifacts MUST be built as one-pass, non-overlapping edits against the unchanged base document.

- Original-document anchor space only. Resolve all placement anchors against the unchanged base document only. Do not anchor later edits against text that would exist only after an earlier edit is applied.  
- Non-overlap invariant. No two redlines in the same bundle may target intersecting base-document spans. No INSERT may land inside a span already covered by a REPLACE, and no REPLACE may partially or fully cover a span already targeted by another REPLACE.  
- One strategy per affected region. For any contiguous affected region, choose exactly one strategy: one consolidated REPLACE for the whole region, or multiple smaller redlines whose target spans are pairwise non-overlapping.  
- Parent-child prohibition. If one redline replaces a parent block, no later redline may target any line inside that parent region. Fold all child edits into the parent replacement.  
- No second-pass layering. Do not emit a broad structural redline and then follow it with repair redlines inside the same replaced region. Rebuild the affected region as one consolidated replacement or as a new non-overlapping set.  
- Repeated-anchor safeguard. If a target line or boundary line repeats in the base document, widen the target to the nearest unique enclosing heading or other unique boundary before emitting the redline.  
- Coverage-before-emission rule. Before outputting redlines, map each required review item to the exact base-document target region that will implement it.  
- Merge-on-conflict rule. If two or more required changes touch the same region, merge them into one consolidated redline.  
- One-pass apply simulation required. A redline bundle is valid only if it can be applied once from the original base document without anchor collision, span overlap, parent-child nesting conflict, or re-anchoring later redlines after earlier edits.  
- Mechanical blocker posture. If the requested changes cannot be represented as a non-overlapping one-pass bundle, do not emit a self-conflicting redline set. Rebuild the region as one consolidated replacement.  
- Bundle validity gate. A redline bundle is mechanically valid only if every required item is mapped to at least one redline, no target spans overlap, no parent-child targeting conflict exists, every placement anchor is unique after disambiguation, and the bundle can be applied once from the original base document without reinterpretation.  
- Failure classification. Any violation of this discipline is a mechanical redline-construction failure and MUST be treated as Revise and Resubmit.

## 0.7 QA branches posture

Purpose: verify evidence and transport posture without touching production code.

Scope: evidence-only.

Allowed changes are limited to in-scope governed evidence and the required Human Evidence Index, hash sentinel, Machine Mirror, and path-proof companions. Evidence families may include Endpoint Catalog, A7 transport, closed-rails refusal, CLI parity, direct PostgreSQL, or BodyGraph evidence only when the approved scope and owning canon require them. Use the exact current paths and schemas from their canonical owners; do not copy an artifact roster into this guide or reuse retired bridge-era DB evidence as current posture.

Forbidden: any changes under app/service code, migrations/DDL writers, runtime configs, vendor rails, or endpoint behavior.

Path normalization: transient or generator paths are forbidden as sources for governed proofs. Relocate outputs into an approved governed home under `audit/**`, `artifacts/**`, or `docs/**` before indexing.

Branch/PR: use branch `qa/hde-epic<NNN>-<slug>`, where `<NNN>` is the zero-padded epic number and `<slug>` is a lowercase ASCII hyphenated label. Open an evidence-only QA PR under the applicable PR process. Keep evidence and indices in the same PR.

Determinism pins: run determinism-sensitive capture and CI with the exact current pins defined by the owning canon.

CI posture (required): Evidence-only QA branches MUST have a diff-scoped validation lane that validates the governed files changed in the branch. Broader repository CI jobs may also run. The diff-scoped lane must cover the required mirror schema and governed-text checks, Human Evidence Index-to-Machine Mirror parity with `proof_anchor` linkage, and any in-scope transport or writer/error predicates defined by the owning canon.

Prod handshake requirement (when claimed): if the QA branch/plan claims it exercised prod via Codespaces for an HDE epic, include at least one simple handshake proving commands talk to the canonical production HD Engine service and DB (per Glow Infrastructure). Typical handshake: `curl` the production base URL `/internal/version` from Codespaces and capture the full response under `audit/qa/hde-epic<NNN>/logs/`. If omitted, QA is underspecified until the handshake artifact is added.

Rails default: CI/test harness runs CLOSED by default; any job that opens rails must pin policy and attach evidence in the same PR.

Acceptance (titles only)

Evidence-only QA branch acceptance token names and semantics must be admitted under §1.1.9. This section does not reproduce the roster.

---

# 1\) EPIC PLAN → CRD (Lead Dev)

## 1.1 Workflow at a glance

### 1.1.1 Standard epic flow

Before applying the steps below, every epic MUST perform a canon inventory:

- Read, by title, the current Glow Infrastructure, Glow QA Guide, and Reality Audits entries that apply to this epic, plus every exact applicable HDE-Build Notes addendum by number and title.  
    
- Consult HDE Phased Epics as a historical-only archive of completed epic records (for prior context and precedent). Do not add in-flight epic entries there. The epic record is archived there once, at epic close.  
    
- Record, in the PLAN context header or adjacent notes:  
    
  - key environment and infra facts from Glow Infrastructure (use canonical values; do not treat as PO inputs unless explicitly marked OPEN/TBD in canon)  
      
  - relevant QA operational mappings from Glow QA Guide and acceptance-token names and semantics admitted under §1.1.9  
      
  - the epic’s D-goals and exclusions from the epic CRD/PLAN; HDE Phased Epics may be consulted only as historical precedent for the D-goal roster and prior close artifacts (it MUST NOT be cited to define evidence surfaces, acceptance tokens, rails, or status semantics)


- Add a short Reality Audits Anchors subsection (or adjacent notes) listing:  
    
  - the component(s) used from Reality Audits  
      
  - the key pathnames/loci from that audit that this epic will touch


- This is traceability only. Do not duplicate Reality Audits contents. Do not assign Reality Audits updates as tasks (PO-owned).  
    
- If any required fact appears missing or ambiguous, mark it as a spec gap per §0.6.5 (blocked-by-spec) instead of treating it as a PO input or improvising rails.  
    
- Only after this canon inventory is complete should the PLAN header and CRD be drafted.

PLAN header (machine-ready): Draft the PLAN machine header as a single post.

CRD with approved scope: After one review, issue the CRD with the approved scope and acceptance tokens by title only (for example A3, A4, A7); do not list bytes or payload shapes in the CRD.

Code capsules before IP: Finalize code-capsules before IP approval; capsules freeze at IP.

CodEx PR responsibility: After Audit and Sandbox Build/Test, CodEx MUST open the PR under the approved plan and this guide’s PR process. In that PR, CodEx includes, in one slice:

- Code  
    
- Doc-Delta (repo docs)  
    
- Human Evidence Index (docs/evidence/INDEX.json)  
    
- Machine JSONL mirror (artifacts/evidence\_index.jsonl)

CodEx also attaches:

- The close pack  
    
- The PASS token list

Lead Developer gate: Lead Dev gates the PR by verifying, as applicable:

- PASS token list is consistent and complete  
    
- A7 proof surface is correct (cataloged JSON success route only)  
    
- Env-gates and encoding invariance are respected for A7 proofs  
    
- 1:1 Evidence Index ↔ machine mirror parity with path-proofs

PO merge and green-freeze: The Product Owner is the sole merger and uses squash-merge on PASS. After merge:

- Scrum Master is informed  
    
- Suites are green-freeze unless a qualifying change lands

### 1.1.2 Multi-PR epics

For some epics (for example EPIC017 and similar Calcination/Separation passes):

- The work may be split into a series of PRs (up to 10 PRs per epic).  
    
- Each PR must carry a self-contained slice with code \+ Doc-Delta \+ evidence.  
    
- The PR-first pattern and same-PR parity (code \+ docs \+ Evidence Index \+ machine mirror) apply to each PR.  
    
- Epic-level acceptance is defined and tracked in the current PLAN and CRD and occurs only after all required PRs for that epic have merged. The completed epic record may be archived in HDE Phased Epics after close.

### 1.1.3 “Prod via Codespaces” requirements (PLAN/CRD)

/internal/version auth posture is not canon (non-invention). This guide treats /internal/version as an identity handshake artifact, but it does not canonize:

- its access-control semantics (public vs operator-network gated vs auth-header required)  
    
- the expected failure mode when access is missing/invalid

Until that auth posture is canonized:

- Plans, remediation guides, and operational tooling MUST NOT state /internal/version auth requirements as canon.  
    
- Any statement about auth posture MUST be explicitly labeled Observed Evidence (non-PF) and MUST be secret-free (presence-only, redacted, or hashed).

Evidence required to canonize auth posture (secret-free). To support an eventual canon decision, capture and store (under a lowercase audit path) the status line and headers for the production deployment context(s) under both conditions:

- with no auth header  
    
- with an auth header only if one is explicitly sourced for this run (value redacted or presence-only noted)

Auth headers are optional until canonized. Plans and runbooks MUST NOT require an auth header/token for /internal/version unless the plan also specifies its sourcing explicitly (for example, as an Ops task output owned by the PO). If no auth header exists or no sourcing chain exists, record that fact as Observed Evidence (non-PF) and proceed with the unauthenticated capture. Do not treat “missing auth token” as proof that the endpoint is inaccessible or “ops not implemented.”

This evidence is required input for the canon decision and MUST NOT be replaced by assumptions.

Name prod surfaces by title. The PLAN/CRD MUST name (by title, routing to Glow Infrastructure as the single home):

- the production HD Engine service and base URL  
    
- the production DB instance/schema

Do not invent new environment labels.

Clarify Codespaces role. The PLAN/CRD MUST state explicitly:

- Codespaces is a QA console that runs CLI/HTTP commands against the production service and DB.  
    
- Codespaces is not a production environment in its own right.

Describe the prod handshake and artifact location (identity-only). The PLAN/CRD MUST describe (at a high level):

- an identity/pre-flight handshake step  
    
- where its artifact will live

Example: Step 0: curl the production /internal/version endpoint from Codespaces and store the output under audit/qa/hde-epic\<NNN\>/logs/ before running deeper QA.

This handshake is identity-only:

- It proves the QA console can reach the production HD Engine.  
    
- It records which `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, and `release_id` were live at the time of QA.

Live QA plans MUST NOT use /internal/version to satisfy any behavior D-goals (for example compat math, narratives, vendor ingest, admin bundle). Those goals require separate behavior steps that exercise prod-facing behavior surfaces and produce their own artifacts under audit/qa/hde-epic\<NNN\>/\<SUBPATH\>.

PLAN/CRD entries that refer to “prod via Codespaces” without these clarifications are incomplete and MUST be updated before the epic moves into implementation or Live QA.

Vendor-first Live QA using “prod via Codespaces”. For epics that intend to run vendor-first Live QA (per §0.6.4 and §1.1.6) using the “prod via Codespaces” pattern above, the PLAN/CRD MUST ALSO ensure:

- The current PLAN and CRD acceptance posture explicitly declares the required vendor-backed behavior, permitted execution venue, and governed evidence location. Codespaces is named only when it is material under HDE-Build Notes Addendum 2.35, “Live QA Execution Environments: Replace the Universal Codespaces Requirement with a Materiality-Based Evidence Contract.”  
    
- The Live QA plan includes at least one vendor-focused step that:  
    
  - uses or references the prod identity handshake artifact (for example the /internal/version capture under audit/qa/hde-epic\<NNN\>/logs/) to anchor which engine instance is under test  
      
  - demonstrates a vendor-backed end-to-end flow (for example vendor-backed resolve or compat) executed against the production HD Engine service, with its own mechanical artifacts captured under audit/qa/hde-epic\<NNN\>/\<SUBPATH\> as required by §1.1.4–§1.1.6.

This identity \+ vendor step does not change the identity-only semantics of /internal/version: the handshake remains a pre-flight proof of “which engine is live,” while the vendor-backed flow is what satisfies the vendor behavior portion of the D-goals and is recorded in the current PLAN and CRD acceptance posture.

### 1.1.4 Live QA mechanical evidence expectations

For Live QA epics, mechanical, step-explicit QA is still required — but it belongs in the QA Plan and QA execution artifacts, not embedded inside the Epic PLAN/CRD or Implementation Plan.

QA planning is a separate deliverable. Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts and MUST NOT embed a full QA runbook (step intents, command blocks, or evidence-generation steps). These planning artifacts MAY state QA objectives and closeout proof obligations, but the QA Plan is where step intents, evidence expectations, and PASS/FAIL posture are specified and where governed QA evidence is produced and indexed.

The Epic PLAN/CRD MUST provide:

- titles-only acceptance intent  
    
- the QA posture (e.g., “Live QA required”)  
    
- a pointer to the QA Plan (titles-only reference) and the epic QA root (audit/qa/hde-epic\<NNN\>/)

QA Plan posture (execution-time). For each Live QA step, the QA Plan MUST specify:

- Command(s) to run (copy/paste runnable; no guessing).  
- Pass/fail checks (what is asserted, and what constitutes failure).  
- Deliverables: exact file artifacts to be produced or updated, with stable step-scoped paths under audit/qa/hde-epic\<NNN\>/checks/\<check\_id\>/.  
- Re-runs MUST refresh the same check directory and MUST NOT create per-run directories or fresh-run roots.  
- Any required context (env assumptions, flags discovered in D0, required fixtures), expressed as concrete preconditions.  
- If a Live QA step depends on product-managed IDs, fixtures, or other runtime inputs that may be unavailable, the plan MUST state how availability is proven before execution and MUST define BLOCKED as the outcome when those inputs are absent or are not valid product inputs.  
- Any deliverable that is only expected when such a precondition is met MUST be labeled conditional in the plan. When the condition is not met, the plan MUST require a governed blocked-note or equivalent artifact and MUST treat the omitted conditional outputs as not expected for that run rather than as missing evidence.  
- If a step is expected to be TOOLING\_BLOCKED unless a named evidence-ledger or manifest-coverage gap is first resolved, the plan MUST name the exact lookup or proof artifact that decides that branch and MUST name the exact loci that artifact must confirm.  
- If the same run later proves that the required coverage is present in all of those plan-named loci, the step MAY be evaluated for PASS using its approved PASS criteria and MUST NOT remain blocked by the superseded gap alone.  
- File existence is not sufficient when the plan requires coverage in specific updater sources, ledgers, or indexes. The deciding lookup artifact MUST show the required mapping or binding in each named locus.  
- If a Live QA check, remedial QA step, or remediation guide depends on a governed JSON field, structural field, adapter-selection field, or equivalent shape predicate, the plan or guide MUST define the structural predicate that proves field presence and semantic binding to the intended source.  
- Raw string presence, substring search, or detached generator-only wording is insufficient when the proof target is a governed structured artifact. The predicate MUST state how the field is tied to the source, such as observed attempts or provider order, updater mapping, or canonical row binding.  
- A check MUST NOT pass by locating a field name if the value shape, source binding, or semantic relationship is missing, malformed, or detached from the governed source.  
- When PASS is taken under this resolved-gap branch, the review MUST name the deciding lookup artifact and MUST state plainly that the blocked branch did not trigger because the required coverage was confirmed.  
- If the lookup does not prove all required loci, the step MUST remain TOOLING\_BLOCKED or FAIL\_TOOLING exactly as the approved plan defines, and the review MUST NOT over-claim ledger coherence.  
- A plan MUST NOT define PASS criteria that become structurally unreachable when the required inputs are outside the current product surface. If that dependency exists, the plan MUST label it as a planning defect or deferred input-availability gate and must state the rerun condition.

Discovery-first posture (mandatory)

Live QA Plans MUST assume any repo detail not proven at planning time is unknown until discovered during the run. The plan MUST prefer real-time discovery and observation over guessed implementation detail.

Repo-resident loci may be named only when proven by allowed provenance sources under the QA-planning locus provenance lock above.

Unknown loci must be handled by a discovery step, not by placeholders. When a check depends on an unproven repo-resident locus, the step MUST:

- state the discovery intent  
    
- state the discovery acceptance criterion  
    
- require recording the discovered locus string verbatim into the step evidence before using it  
    
- define PASS, FAIL, and BLOCKED outcomes for discovery itself

Vetoed patterns. Live QA Plans MUST NOT use placeholder or example routes, file paths, module names, test IDs, or command strings as scaffolding for unknown repo reality.

Command-line minimalism (required)

The plan SHOULD describe:

- the goal of the action  
    
- the observable outputs that matter  
    
- the evidence that must be captured

The executor MUST record the exact commands actually used into the step evidence at runtime. If the plan includes an exact command string, that string MUST be provenance-proven under the QA-planning locus provenance lock above.

Live QA plan validity lint (approval gate). A Live QA plan is non-approvable unless all items below are satisfied.

QA planning QoS guardrails (iteration pressure). When Live QA plan iteration count is high, apply the guardrails below to prevent REVIEW-mode drift and to stop non-convergent plan rewrites.

Prompt-family separation (AUTHORING vs REVIEW). Every QA prompt used in this process MUST declare its mode in its header as one of:

- AUTHORING — allowed to draft or restructure plan text, step definitions, deliverables blocks, scripts, and runbooks.  
    
- REVIEW — allowed to evaluate evidence and plan coherence, quote existing plan text, and request plan changes. REVIEW mode MUST NOT invent new commands, runbooks, or evidence pointers.

REVIEW-mode remediation exception (verbatim-only). If remediation requires quoting commands, the REVIEW-mode prompt MAY include only command snippets copied verbatim from the approved plan text (including caveats). The prompt MUST label the snippet as verbatim and MUST NOT introduce new flags, paths, or steps.

Temporary addendum clarification during review (step-preserving posture). If an exact applicable HDE-Build Notes addendum explicitly resolves a documentation, inventory, or classification ambiguity for an already-approved QA step, the review MUST treat the issue as canon-alignment drift rather than as a new runtime defect unless the governed evidence shows a real runtime failure.

For that exact ambiguity while the addendum remains live, the reviewer MUST apply the exact addendum clarification first and the older ambiguous canon wording second.

Under this posture, the existing approved step MAY be rerun or evaluated using its existing step ID, existing PASS/FAIL posture, and existing approved evidence family.

REVIEW mode MUST NOT use the clarification as a reason to invent a new route, a new flag, a new proof-surface carrier, a new QA step, a new evidence family, or a new acceptance token.

The review record MUST state the temporary clarified designation, identify the existing approved evidence family used for the decision, and list the downstream canon-drain targets required for permanent alignment.

Downstream drainage MUST preserve the existing single-home inventory posture and the existing proof-surface separation. Do not create a second designation mechanism or alternate inventory home as part of the temporary clarification.

If an exact applicable HDE-Build Notes addendum resolves a previously blocked branch for an already-approved step, stale blocked-lane command text that remains in the approved plan is a planning defect, not an automatic blocker, when all of the following are true:

- the actual rerun uses the existing approved step ID  
- the actual rerun stays within the existing approved deliverable family  
- the deciding lookup artifact comes from the already-approved evidence family  
- the governed rerun evidence proves the approved PASS criteria

In that case, the review MUST state which stale blocked-lane command or lookup path was superseded, which governed artifact actually drove the successful branch, and that no extra governed paths were introduced.

A rerun that changes only the deciding lookup source within the existing deliverable family remains execution-preserving. It does not create a new evidence family, a new proof-surface carrier, or a scope expansion.

This temporary clarification posture is execution-preserving only. It does not remove the downstream drain obligation, and it MUST NOT widen into new dev or ops remediation work unless governed evidence proves such work is actually required.

QoS stop-rule (iteration churn escalation). If the Live QA plan requires repeated structural remediation for the same failure mode across revisions (suggest threshold: 2), treat the issue as a systems-level prompt/template defect. Escalate to a systems RCA and a canonical drain that targets the class of failure, not the incident.

Step list coherence (no undefined steps). If a Live QA plan includes a step matrix, checklist, or run sequence, every step ID listed MUST have a corresponding step definition in the plan’s Step Details (or the plan MUST explicitly state that the step is out of scope and must not be executed).

Plans MUST NOT list steps that are not defined as executable steps in the plan body. An undefined step ID in the matrix is a mechanical blocker.

Minor target-label mismatches inside a step are plan defects, not automatic step failures, when all of the following are true:

- the step title or intent identifies one concrete target,  
    
- the Inputs section names that same concrete target, and  
    
- the captured evidence proves that same target.

When those conditions are met, the reviewer MUST record the mismatch as a wording caveat or doc-delta item and MUST NOT fail the step on that mismatch alone.

If the step title, inputs, PASS/FAIL text, and captured evidence do not converge on one target, the step is non-conforming and must be corrected before it can be trusted.

Evidence pointers must be concrete (no manifest-only references). Paths, filenames, and evidence routing MUST be explicit in the plan (not “see manifest”).

If the plan references a proof/log file, it must be stored at a governed path and retrievable by reviewers using repo lookup alone.

Any referenced log/proof that is required evidence for an executed, in-scope step MUST be present and retrievable as part of the evidence bundle used for plan approval or final review.

If a plan’s SOURCE EXCERPT or runnable command block writes additional check-scoped files beyond the Deliverables list, each such file MUST be classified in the plan as one of:

- required deliverable — counted for missing-evidence review and eligible to affect PASS or FAIL.  
    
- auxiliary capture — retained in the step evidence stream but explicitly non-gating.

Auxiliary captures MUST NOT expand the step’s required-deliverables set or its PASS criteria unless the plan also names them in the Deliverables block or the PASS/FAIL block.

Support captures such as stderr logs, support-script rc files, or verifier side outputs are informational only unless the plan states a specific content or exit-code predicate for them. If the plan requires only file existence or some other decisive predicate, empty stderr or unused support captures are non-blocking.

Non-fatal runtime warnings recorded in a governed report are caveats, not blockers, when the report also records no TOOLING\_BLOCKED, FAIL\_TOOLING, or FAIL\_BEHAVIOR condition for the step and the warning does not alter the approved PASS predicate, evidence identity, rails posture, or proof target.

If a warning affects command success, output bytes, required deliverables, evidence trust, runtime behavior, or a plan-defined predicate, reviewers must classify the actual affected condition rather than treating the warning label alone as decisive.

This includes files referenced in verbatim source excerpts. If the plan shows a redirected output path for such a file, the plan MUST either list it as a required deliverable or label it auxiliary and non-gating in the same step definition.

Template semantics for deferred steps (NOT RUN / DEFERRED). If a plan template or closure/rollup step enumerates step-scoped evidence paths for steps that have not executed, it MUST explicitly label those entries as NOT RUN (or DEFERRED). NOT RUN / DEFERRED MUST NOT be treated as a missing-evidence failure and MUST be excluded from missing-evidence counts.

Closure/rollup steps that roll up evidence-path existence MUST separate these states:

- PRESENT — the artifact exists at the referenced path.  
    
- MISSING — the producing step is executed and the artifact should exist, but does not.  
    
- NOT RUN / DEFERRED — the producing step has not executed; no artifact is expected yet.

No dangling links rule for deferred steps. A plan or close-pack rollup MUST NOT present absent future-step file paths as evidence pointers in a way that implies file existence. If listing future-step paths at all, list them only as NOT RUN / DEFERRED entries until the producing step has executed.

A plan MUST NOT list a file path as a required prerequisite unless it is canon-defined or audit-proven. If it is neither, the plan MUST include the exact create/write step(s) under audit/\*\* or artifacts/\*\* (no placeholders) and treat the artifact as QA-run-produced evidence (not a preflight prerequisite).

Directly executable (copy/paste discipline). All operator-run steps MUST be copy/paste runnable in the execution environment permitted by the owning Live QA Plan. If a step includes script content, it MUST be complete enough to create a syntactically valid file.

Inline-command consolidation via step-local script is allowed when controlled. If an approved step is written as inline commands but the actual run consolidates those commands into a step-local script, that execution form is allowed when:

- the script is created under the same governed step root and is itself captured as a step artifact or embedded verbatim in primary.log  
- primary.log records the exact executed command sequence or exact script content with command\_provenance set to Explicitly created  
- the plan-defined deliverables, governed output paths, and PASS/FAIL predicates remain unchanged  
- the script does not introduce hidden dependencies or widen scope beyond the approved step

When these conditions are met, reviewers MUST treat the script as a provenance or execution-form improvement, not as a blocker. It becomes blocking only if it changes the required deliverables, the required proof posture, or the meaning of the step.

Gitless runbook. Live QA runbooks are gitless in the sense that they MUST NOT describe or enforce VCS workflow (branches/commits/PRs). A runbook must contain only verification steps; no branching, merging, resetting, committing, etc.

Read-only git commands MAY be included only as optional, non-gating repo-root sanity checks (“this is a repo” / “repo root exists”). They MUST be non-mutating and MUST NOT print or rely on branch names, commit SHAs, or PR identifiers. If such a sanity check fails, the check outcome is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR), and the run MUST proceed using non-git verification paths.

If git information is recorded, it must be purely traceability metadata; it must not block the run.

Mechanical-only evidence. Any file treated as QA evidence (including close artifacts) MUST be mechanically produced from commands and MUST NOT contain manual-fill placeholders. If a result is “no deltas,” the produced artifact MUST state that explicitly.

Doc Delta Capture (mandatory for Live QA). Every Live QA plan MUST include the Step-0 Doc Delta Capture artifacts defined by PF27-Canon-Plan-Templates. They record missing prerequisites and documentation ambiguity discovered during planning. If no deltas are found, the produced artifacts MUST state “no deltas.” Codespaces-specific venue evidence remains conditional on venue materiality.

A Step-0 “Codespaces snapshot” MAY be captured as an optional diagnostic convenience record, but it MUST be explicitly labeled non-gating and MUST NOT be required for plan approval or execution.

No manual-result placeholders (hard rule). Live QA plans and runbooks MUST NOT include instructions that require the operator to manually fill results (for example “Result: (fill PASS/FAIL/SKIPPED)” or equivalent). Step outcomes must be determined mechanically from the step’s commands and the resulting artifacts under audit/qa/hde-epic\<NNN\>/\<SUBPATH\>.

If a plan cannot express a step outcome as commands \+ checks \+ deliverables, that step is non-conforming and must be rewritten or removed.

If a QA Plan step cannot be expressed mechanically (commands \+ deliverables \+ checks), it is not a valid Live QA step in this process.

Execution tolerance for operational doc drift (Live QA). For Live QA execution details (paths, filenames, exact script locations, exact CI job names), if an acceptance roster or plan reference conflicts with repo reality, QA MUST use the repo-real invocation/paths to run the checks and capture evidence.

Source-of-truth posture (Live QA). The plan and rosters define intended steps and checks. The governed Live QA evidence stream (step receipts, manifests, and close-pack artifacts) is the source of truth for what executed and what can be claimed. Plan text is not evidence and MUST NOT be used to infer outcomes, token satisfaction, or coverage.

Coverage vs plan-step accounting (required). The close-pack MUST include a Live QA plan-step coverage ledger for in-scope plan steps, marking each step as Fully evidenced, Partially evidenced, Not evidenced, or Unknown. Any step marked Not evidenced or Unknown MUST be treated as an explicit closeout gap: either a blocker that prevents closeout, or a closure-override waiver that enumerates the gap and its rationale.

A step MUST NOT be marked Fully evidenced, nor treated as closure-satisfying PASS by implication, unless the coverage ledger cites at least one step-scoped governed evidence pointer for that exact step under the canonical QA root.

A heading label, summary sentence, or cross-step evidence pointer is not sufficient. If the step record is mislabeled, duplicated, or contaminated with another step’s content, the step MUST be treated as Not evidenced, Unknown, or BLOCKED/UNEXECUTABLE until the identity and evidence pointers are corrected, or handled via an explicit closure override.

In addition to the four evidence-coverage labels above, the coverage ledger MUST use BLOCKED/UNEXECUTABLE when a planned step could not execute because a required precondition or product input was unavailable.

Any BLOCKED/UNEXECUTABLE entry MUST state: the blocking precondition, why it could not be satisfied, whether it blocks closeout, and the required follow-up.

Record the mismatch as a CAVEAT: DOC\_DRIFT for later drain.

Do not block execution unless the mismatch prevents knowing what to run or how to verify.

Evidence posture remains non-negotiable: evidence must still be captured under the canonical QA root and governed locations.

Non-blocking DOC\_DRIFT example (common): A step overview lists a specific report JSON filename, but the repo-real run emits the report artifact under a different filename and the plan’s embedded verification predicates do not hinge on the specific report JSON filename. Record DOC\_DRIFT and proceed without retrofitting acceptance to the report filename.

No non-canonical QA scripts or wrappers in Live QA plans (baseline commands only). Live QA plans MUST NOT depend on helper or wrapper scripts unless the tool is explicitly canon-named by path in PF-Canon (template compliance does not imply permission to invent entrypoints).

If a step needs “tooling,” it MUST be either:

- a canon-named entrypoint by explicit path (for example a repo script or CI check that is already established as a governed surface)  
    
- an inline tool whose full source is embedded in the plan step and written into the run-local QA tools directory for that run (no hidden dependencies)

Any plan that references a non-canon script path as a “required surface” is non-conforming and must be revised to validate the governed artifact surface directly using baseline commands.

A Live QA step does not require a dedicated per-check helper or wrapper when the governed result can be produced and reviewed through baseline commands plus an already-governed workflow.

When a step reuses the same governed header or manifest workflow already used by earlier checks, the plan or report MUST make that reuse explicit enough to verify:

- the exact commands or writer path used for the update  
    
- the specific governed artifacts refreshed for that step  
    
- that the step’s manifest entry and sibling path-proof were refreshed for that step

Absence of a dedicated helper is a planning or convenience gap, not an automatic blocker, when the approved PASS or FAIL predicates and the governed artifact updates can still be confirmed directly from the recorded workflow.

“Baseline commands” means explicit shell/Python one-liners, direct invocation of canon tools, tee for logs, and explicit file writes, with no reliance on opaque runners.

Command/Entrypoint provenance (no invented executable entrypoints). Plans and runbooks MUST NOT require an executable entrypoint (for example: python \-m \<module\>, bash \<script.sh\>, ./\<tool\>) unless one of the following is true:

- Repo-proven — the entrypoint is a real, versioned repo surface and its existence is confirmed at the specified path / module name at execution time, or  
    
- Canon-defined — the entrypoint is explicitly defined by PF canon as a required tool surface, or  
    
- Explicitly created — the plan includes explicit creation instructions (for example: an OPS step that creates an ephemeral helper under /tmp).

Evidence roots are not code roots. audit/\*\* and artifacts/\*\* are evidence roots. A plan MUST NOT invoke scripts from those roots unless the plan explicitly creates them in-step. (Writing governed evidence outputs under audit/\*\* or artifacts/\*\* is expected.)

QA vs remediation separation. Remediation plans MAY include code changes that modify or add entrypoints only when DEV scope explicitly introduces those entrypoints as versioned repo code.

Preflight existence checks (mandatory). Any OPS step that invokes a repo script, binary, or module MUST include a check that proves it exists before attempting the run. Examples:

- For Python modules: python \-c "import \<module\>; print('OK')"  
    
- For scripts: test \-f \<path\> && test \-x \<path\> || (echo "MISSING"; exit 2\)

If the entrypoint does not exist, the run is TOOLING\_BLOCKED (not FAIL\_BEHAVIOR). The operator MUST stop and capture the transcript as evidence.

### 1.1.5 Live QA behavior vs artifact pattern

For Live QA work, runtime behavior and governed evidence artifacts are not the same thing. The QA Plan MUST describe them as two distinct phases where applicable.

Behavior execution phase: Run the system/endpoint/harness step that exercises the behavior being tested. Treat this phase as producing signals (responses, logs, outputs) that inform what evidence must be captured, but do not treat “it worked when I ran it” as the evidence artifact.

Artifact capture \+ analysis phase: Capture governed evidence artifacts under audit/qa/hde-epic\<NNN\>/\<SUBPATH\> (and related required closeout artifacts). Perform analysis offline (e.g., in Codespace), producing the required summaries, diffs, and verification notes as governed artifacts.

Rule: A Live QA step is not complete unless the artifact phase produces the specified deliverables in the QA root (or other governed locations referenced by Evidence Index/Machine Mirror), even if the behavior phase “looked correct” during execution.

#### 1.1.5A Production-affecting open-rails Live QA requirement

For any epic that can affect real production functionality, QA readiness and closeout review MUST account for at least one bounded open-rails Live QA step that proves relevant production-facing behavior in the deployed or PO-approved live target, unless an explicit exemption is approved and recorded.

This applies when the epic can affect any of the following:

- production surfaces  
- public or app-facing behavior  
- runtime compute  
- vendor ingest  
- HumanDesignAPI calls  
- external API integrations  
- database persistence  
- database retrieval  
- DB bridge behavior  
- deployed service behavior  
- environment-variable or secret-binding behavior  
- request shaping  
- response mapping  
- authentication or authorization behavior  
- public Reader behavior  
- CLI/API behavior used in production  
- queues, workers, jobs, schedulers, or runtime services  
- any path that must work outside isolated closed-rails fixtures

Closed-rails proof remains important, but closed-rails proof alone is not enough for production-affecting work. This applies even when closed-rails tests, repo tests, evidence refreshes, static checks, and generated proof artifacts are all green.

The required open-rails Live QA step must be bounded, non-destructive unless explicitly approved, PO-authorized where secrets, external services, or deployed environments are involved, secret-safe, evidence-recorded, scoped to the epic’s actual production risk, clear about what it proves, and clear about what it does not prove. One open-rails Live QA step is the minimum. More are required when one live step cannot honestly prove the affected production functionality.

A valid open-rails Live QA step may include, when scoped and authorized: live deployed service check, live vendor smoke, live API call against a deployed target, live DB bridge read/write check, live persistence and retrieval check, live request-shaping check with redacted proof, live response-shape check with redacted proof, live authentication or credential-binding confirmation, live environment-variable binding confirmation, live app-to-engine integration check, or live CLI/API behavior check against a real configured target.

The following do not satisfy the required open-rails Live QA step by themselves: unit tests, integration tests against fake services, closed-rails fixture replay, static analysis, generated evidence artifacts, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, Codex Audit, exact-addendum supportability note, implementation review approval, QA Plan approval, smoke procedure written but not run, or OPS discovery without live behavior proof.

Open-rails Live QA evidence may record key names, redacted values, header names, redacted header-shape posture, environment label, endpoint family, status class, redacted response excerpt when safe, whether behavior matched expectation, and whether the live step proves only a narrow smoke or broader behavior. It MUST NOT record raw API keys, raw bearer tokens, raw database passwords, raw request secrets, raw private payloads, unredacted vendor response bodies unless explicitly approved and governed, or uncontrolled production data.

Open-rails Live QA proves only what it actually exercises. A live vendor smoke does not prove full vendor conformance unless it covers the full conformance claim. A single DB bridge read does not prove all persistence behavior. A single deployed endpoint check does not prove all public app behavior. A successful response does not prove all error, retry, or rate-limit behavior. A live smoke does not automatically move unrelated phased-checklist rows to Done. The QA Plan MUST state the bounded proof meaning.

Exemption is allowed only with explicit justification. A Live QA Plan may omit open-rails Live QA only when at least one of the following is true: the epic has no production, runtime, compute, vendor, persistence, deployed, integration, public, or external-service effect; the live step would be unsafe; the live step would expose secrets or private data and no redacted safe alternative exists; the PO explicitly withholds authorization; the required deployed target is unavailable and cannot be safely reached; the work is documentation-only and does not affect production behavior; the work is planning-only and does not claim implementation readiness; or the work is a closed-rails-only proof slice and no production functionality claim is being made.

If an exemption is used, the Live QA Plan MUST state why open-rails Live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release. Default posture: no exemption.

A Live QA Plan for a production-affecting epic is not approval-ready unless it includes at least one open-rails Live QA step or a clear, authorized exemption. Reviewers MUST NOT accept a closed-rails-only Live QA Plan for a production-affecting epic without explicit exemption language. This is a truth/proof requirement, not a formatting preference.

PR, OPS, and QA sequencing MUST support bounded live proof when required. Open-rails Live QA may be PO-run or PO-authorized where secrets, external services, or deployed environments are involved. CodEx and implementation agents may prepare repo-local code, fixtures, validators, redaction helpers, harnesses, documentation, and evidence-processing logic. When a required live external action is an otherwise-permitted Ops task, it MAY be performed personally by the PO or by an explicitly delegated automated session agent under the applicable Ops authorization, scope, safety, stop-check, redaction, evidence, and completion-claim controls. Delegation does not convert Ops evidence into QA evidence. Secret values MUST remain out of commands, logs, chat output, and repo evidence unless an external system securely injects them without disclosure.

### 1.1.6 PO Live QA vendor-first scope

When a PLAN or CRD describes PO Live QA (a Live QA session that requires PO time), it MUST:

- Declare PO Live QA as vendor-first. Clearly state that PO Live QA for this epic is a short, focused session whose primary goal is to exercise live vendor behavior against the production HD Engine and capture mechanical evidence of that behavior.  
    
- Label vendor vs non-vendor steps. For all Live QA steps, classify them into:  
    
  - Vendor-focused (class 3): steps that exercise vendor-backed flows (for example vendor-backed BodyGraph resolution, compat, vendor error behavior).  
      
  - Ops/identity (class 1): connectivity and identity checks (for example /internal/version).  
      
  - Internal functional/determinism (class 2): serializer/guard/sanity/determinism checks that can run under CI/QA without involving the PO.


- Identify the PO workload explicitly. Identify the subset of Live QA steps that the PO is expected to run in a Live QA session:  
    
  - This subset MUST consist only of vendor-focused steps.  
      
  - Ops/identity and internal functional/determinism steps MUST be marked as preconditions or CI/QA responsibilities, not PO Live QA workload. They may be referenced as “pre-flight / internal” work but not scheduled into PO’s Live QA time.


- Tie vendor steps to mechanical vendor evidence. For each vendor-focused PO step:  
    
  - Specify the behavior run context (prod-facing environment), per §1.1.5.  
      
  - Require the owning Live QA Plan to specify the artifact-capture and analysis commands and exact governed output paths. Codespaces-specific commands and venue provenance are required only when Codespaces is material to the approved proof under HDE-Build Notes Addendum 2.35, “Live QA Execution Environments: Replace the Universal Codespaces Requirement with a Materiality-Based Evidence Contract.”  
      
  - Ensure that artifacts for vendor steps are clearly identifiable as vendor evidence so they can be referenced from the current PLAN and CRD acceptance posture and from the owning QA evidence surfaces in Glow QA Guide.

Plans that:

- describe PO Live QA without labeling vendor vs non-vendor steps  
    
- assign ops/identity or internal determinism steps to the PO’s Live QA workload  
    
- omit mechanical vendor evidence expectations for PO-run vendor steps under audit/qa/hde-epic\<NNN\>/\<SUBPATH\>

are incomplete and must be corrected before PO Live QA is scheduled.

### 1.1.7 D3 CLI guard runs — CI vs open-rails Live QA

Live QA planning MUST explicitly distinguish between these contexts:

- CI / closed-rails D3 guard runs (authoritative).  
    
  - Claimable D3 CLI guard tokens are admitted only under §1.1.9. The applicable phased HDE-Build Checklist, HDE-Mechanics Guide, and Glow QA Guide govern the related guard requirements, implementation surfaces, and QA evidence mechanics within their respective scopes; none independently creates a claimable token.  
      
  - The canonical D3 acceptance condition is: guard tools run under the closed determinism rails (for example LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0 as defined by other PF docs) and exit successfully, with their evidence captured and indexed according to those documents.  
      
  - Live QA Plans MUST NOT assume that an open-rails Live QA environment is responsible for re-satisfying these D3 guard tokens; instead, they MUST point to the CI/closed-rails evidence when claiming D3 acceptance.


- Open-rails Live QA guard runs (optional, env-enforcement only).  
    
  - In an intentionally open-rails Live QA environment (for example, a Codespace used for prod-facing behavior tests and artifact capture per §0.6.3–§0.6.4), running the CLI guard tools is optional and is treated as an env-enforcement check only.  
      
  - In this context, a guard run that fails solely due to env mismatch (for example, exit code 1 because the environment is open rails instead of the closed determinism rails expected by CI) MUST NOT be treated as:  
      
    - a wiring bug  
        
    - a failure to satisfy D3 guard tokens

    

  - Live QA Plans MUST:  
      
    - state explicitly when a guard step is being run in an open-rails environment “for information only” (to confirm that guards enforce env pins)  
        
    - tie D3 guard tokens back to the CI/closed-rails runs, not to these open-rails checks

Effect on PO Live QA: For PO-run Live QA sessions in open-rails environments:

- Guard runs, if present, MAY be used to demonstrate that env pins are enforced.  
    
- Guard failures due solely to env mismatch MUST NOT block PO Live QA or be interpreted as D3 token failures.  
    
- The Live QA Plan MUST refer back to the CI/closed-rails guard evidence as the source of truth for D3 acceptance.

Plans are non-conforming and MUST be corrected if they:

- treat open-rails guard failures as D3 token failures  
    
- omit the CI vs open-rails distinction for guard steps

These plans MUST be corrected so that D3 acceptance is clearly anchored in CI/closed-rails runs, with open-rails guard runs documented as optional env-enforcement checks only.

### 1.1.8 CLI commands in QA Plans (canon-backed only)

Live QA Plans frequently use hdctl or other CLI commands as entrypoints (for example D0 “CLI presence” checks, D1 error-stream checks, or vendor-facing steps). To keep those steps aligned with PF-Canon and avoid inventing new CLI requirements, the following rules apply.

CLI bytes live in the CLI spec.

All CLI commands, flags, and subcommands used in QA Plans MUST be traceable to at least one of:

- HDE-CLI-API-Vendor-Ref (the single home for CLI/Reader bytes)  
    
- a governed CLI test harness or script in the repo  
    
- a CodEx audit snippet that lists the CLI shape as discovered behavior for this repo

QA Plans MUST NOT introduce new CLI spellings or flags “by habit” (for example a generic \--version check) that are not present in those sources.

D0 CLI presence checks must be minimal and spec-backed.

When D0 includes a “CLI presence” or “CLI baseline” step, that step MUST:

- use command shapes that are explicitly documented as supported (for example a shell-level presence check or a help/usage invocation taken from the CLI spec or CodEx audit)  
    
- phrase the Expected Outcome in terms of what PF-Canon actually requires (for example “CLI is installed and runnable under the pinned rails for later steps”), not in terms of extra behavior that is not a canonical requirement

D0 steps MUST NOT assert stronger expectations (for example “must print a version string” or a particular banner) unless those behaviors are explicitly tied to PF-Canon requirements or epic acceptance tokens by title.

Plan authors MUST copy, not invent, CLI shapes.

Implementation Agents and QA Plan authors MUST derive every CLI command used in a QA Plan from:

- the CLI spec  
    
- an existing test or harness  
    
- a CodEx audit report for this repo

Implementation Agents and QA Plan authors MUST copy those shapes exactly (command name, flags, argument structure), adjusting only concrete values like file paths or epic IDs.

Any time a Plan adds a new CLI usage that is not already present in those sources, the Plan MUST treat that as a spec gap and do one of:

- update the CLI spec first  
    
- remove or replace the command with a canon-backed equivalent

Plan reviewers MUST treat non-traceable CLI commands as blocking.

During PLAN/CRD review for epics that include CLI steps (especially Live QA epics), Lead Dev and QA reviewers MUST:

- spot-check CLI commands in the Plan against HDE-CLI-API-Vendor-Ref, tests, or CodEx audit output  
    
- treat any CLI command or flag that cannot be traced to one of those sources as a blocking issue

Plans with non-traceable CLI commands MUST be corrected before approval by doing one of:

- replace the command with a canon-backed usage  
    
- first add the missing behavior to the CLI spec and tests, and then update the Plan to match

Interaction with other sections: This section refines §0.6.1 “Canon-first planning” for CLI usage: CLI behavior in QA Plans must come from the CLI spec, tests, or CodEx audit, not from generic assumptions.

It complements §1.1.5–§1.1.7 by ensuring that:

- CLI steps used for behavior runs and artifact capture follow documented command shapes  
    
- D3 CLI guard runs in Live QA (when present) still respect the CI vs open-rails distinction while using canon-backed commands

Plans are non-conforming and MUST be revised before PLAN/CRD approval or Live QA scheduling if they:

- rely on CLI commands or flags that are not present in any PF-Canon CLI spec, test harness, or CodEx audit  
    
- assert Expected Outcomes that go beyond PF-Canon requirements without naming the corresponding tokens or docs by title

### 1.1.9 Token fidelity rails for QA tokens and evidence

HDE-Governance is the permanent canonical home for acceptance-token names, semantics, and admission. A token is claimable only when its exact name is registered there or is explicitly minted by one exact applicable numbered HDE-Build Notes addendum pending drainage into HDE-Governance. An epic approval, Glow QA Guide entry, checklist row, tool export, evidence artifact, or local plan cannot mint a claimable token.

Plans and reviews MUST:

- classify every referenced token as in scope, deferred, or informative;  
- use the exact spelling from HDE-Governance or, during a bounded drainage window, the exact applicable numbered HDE-Build Notes addendum that minted the token;  
- treat a token-like label absent from both permitted sources as a non-token proof obligation or proposal, never as claimed acceptance;  
- route any proposed token and its semantics through the HDE-Governance admission process before it becomes an acceptance predicate;  
- defer or remove a token when its admitted name or semantics cannot be established without guessing; and  
- keep explicit evidence wiring for every in-scope token without duplicating the governing roster or semantics in PF06.

PF27-Canon-Plan-Templates owns the Epic PLAN structure. This guide owns the CRD process obligations in §1.3 but does not create a CRD machine schema; any CRD field governed by PF27-Canon-Plan-Templates follows that owner. Glow QA Guide owns QA operational guidance and the governed token-to-evidence ledger. The PLAN or CRD may point to that ledger but MUST NOT embed a second schema or roster. At approval, every in-scope token must have complete, non-placeholder evidence wiring. At closeout, the ledger must match the produced governed evidence, Human Evidence Index, and Machine Mirror.

HDE Phased Epics is historical-only. It may preserve a completed epic record after close but does not define an in-flight token roster or acceptance semantics. Any bounded scope waiver must be explicit and non-transitive and cannot alter HDE-Governance token authority or evidence-integrity requirements. A prior token-fidelity blocker may be downgraded only when the governing source or affected artifact has changed and the resolving change is identified.

### 1.1.10 PLAN submission preflight (mechanical gate: tokens \+ evidence paths)

This section defines a mandatory preflight that must pass before an Epic PLAN is considered approvable. It is designed to prevent plan churn caused by missing close-pack items, unregistered tokens, and misbound evidence paths.

#### 1.1.10.1 Close-pack completeness (plan-authoring gate)

A PLAN is non-conforming unless it explicitly includes the close-pack baseline:

- the complete close-pack file set by full path as defined in §0.5.1

This is a plan submission gate, not a later Close Gate reminder.

#### 1.1.10.2 Token registry validation (no unregistered acceptance tokens)

Before PLAN or CRD approval, validate every claimed acceptance-token name against HDE-Governance or one exact applicable numbered HDE-Build Notes addendum that explicitly minted the token pending drainage. A claimed roster containing a name admitted by neither source is a mechanical blocker to approval or acceptance. Do not infer an alias, near-match, or replacement.

During execution, record an encountered unregistered token-like name as `CAVEAT: UNREGISTERED_TOKEN` and continue non-token evidence capture unless the missing registered predicate prevents a confident pass/fail determination. Evidence capture does not make the name claimable. If the behavior must be enforced without a registered token, state it as a non-token obligation with explicit proof wiring.

A plan may propose a new token only through an ADR that states the proposed name, semantics, intended evidence surfaces, conflict check, and Governance routing. The proposal MUST remain non-token and MUST NOT appear in a claimed acceptance roster until HDE-Governance registers it or one exact applicable numbered HDE-Build Notes addendum explicitly mints it pending drainage. PF06 does not define token aliases, token budgets, canonical token strings, or local admission exceptions.

Close-pack presence is a baseline artifact obligation, not an acceptance token. Verify close-pack files and evidence bindings separately from the claimed-token roster.

#### 1.1.10.3 Evidence bundle completeness for local-bundle deliverables

When a deliverable claims a local bundle of governed artifacts under a directory (example: artifacts/ops/internal\_version/\*), the PLAN MUST explicitly state:

- the complete required bundle paths, with no byte restatement, sourced from the canonical bundle definition  
    
- any shared or global governed artifacts required for acceptance that live outside the local bundle root, including canonical paths

If the plan references a canonical bundle definition section by title instead of listing all paths, it must still list:

- any overrides, exclusions, or additions  
    
- any shared/global evidence outside the local bundle root

#### 1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)

Path-proofs are required, but not primary token evidence. Co-located \*.path\_proof.txt transcripts are mandatory for indexed artifacts and are referenced via proof\_anchor.

However:

- Token/evidence bindings (token/evidence matrices, acceptance maps, and PLAN required evidence lists) MUST bind tokens to the primary artifact(s) and the validator tests.  
    
- Token/evidence bindings MUST NOT list \*.path\_proof.txt files as the primary evidence surface for a token. Path-proofs may be referenced only as the proof\_anchor for a bound primary artifact.

Every acceptance token to artifact binding that appears in an Epic Plan and in the token/evidence matrix MUST be validated against HDE-Schemas & Artifacts before approval or merge.

If HDE-Schemas & Artifacts defines a fixed canonical path for a token’s evidence surface, the plan and matrix MUST bind to that exact path.

If a PR or remediation produces evidence for a PR-specific, check-specific, vendor-specific, or slice-specific behavior, it MUST NOT overwrite shared or global governed evidence artifacts unless the approved task explicitly requires refreshing those shared artifacts.

If an attempted evidence output collides with an existing shared or global evidence family, the final review MUST show that the collision was repaired by restoring the shared artifact, relocating the slice-specific evidence under a governed slice-specific root, refreshing required companion proof, index, mirror, and checksum artifacts, and classifying any shared or global companion churn.

A collision repair is acceptable only when it preserves the approved behavior, does not drop required evidence, does not create an alternate evidence home, and does not use the repaired collision to claim unrelated applicable phased HDE-Build Checklist closure, route work, public-contract change, or new acceptance scope.

Governed evidence key collision repair. If one governed artifact path is associated with multiple artifact keys, labels, or rows, or if an epic-specific key can override a canonical repo key for the same discovered physical path, the final review MUST treat this as an evidence-key collision.

The repair MUST restore the canonical key-of-record, remove or filter the stale duplicate key at the source that generates the index or mirror row, regenerate the Human Evidence Index, Machine Mirror, hash sentinels, and path-proof transcripts as applicable, and prove that the stale key is no longer claimable in governed evidence surfaces.

A PR may not be accepted on a duplicate-key collision by changing downstream display only. The source of generated rows must be corrected, or the stale row must be explicitly marked as a non-claim and excluded from acceptance binding.

Evidence-path authority order (normative). When determining the authoritative path-of-record or token → artifact binding for governed evidence, resolve conflicts using this authority order (highest wins):

- repo manifests  
    
- audit manifests  
    
- rendered reports  
    
- QA plan text (intent only; never acceptance authority)

Path-proof constraint (no fallback acceptance). This authority order does not relax path-proof requirements. If the highest-authority binding cannot be proven (missing artifact, missing path proof, or hash mismatch), treat it as a tooling or process failure and remediate the binding or regenerate the evidence before claiming acceptance.

Determinism env pins is a single canonical evidence surface.

When DETERMINISM\_ENV\_PINS\_OK is claimed, the only valid evidence surface is:

- audit/gates/determinism/env\_pins.log  
    
- audit/gates/determinism/env\_pins.log.path\_proof.txt

DETERMINISM\_ENV\_PINS\_OK MUST NOT be bound to artifacts/proofs/env\_pins.txt (or any other similarly named file).

When DETERMINISM\_ENV\_PINS\_OK is claimed, all acceptance ledgers and indices MUST bind to the canonical log path, and parity MUST be consistent across:

- token/evidence matrix row  
    
- docs/evidence/INDEX.json  
    
- artifacts/evidence\_index.jsonl  
    
- the proof\_anchor path-proof

Any deviation is a mechanical blocker: fix the binding, do not reinterpret.

Evidence index snapshot artifact family is a single canonical surface (no EPIC-local variant for closure).

Tool entrypoint naming (repo-proven): When a PLAN, runbook, or Implementation Guide references the evidence index snapshot generator, use `python tools/evidence/generate_evidence_index_snapshot.py` and do not reference `python tools/evidence/run_evidence_index_snapshot.py`.

Tool entrypoint naming (repo-proven): When a PLAN references the determinism env pins gate runner, use `python tools/evidence/run_env_pins_gate.py`.

Tool entrypoint naming (repo-proven): When a PLAN references the showcompat artifacts runner, use `python tools/evidence/run_showcompat_artifacts.py`.

Canonical path (normative): Evidence index snapshot artifacts MUST use the gate-family path:

- audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json  
    
- audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt

EPIC-local posture:

- The EPIC-local variant under audit/qa/hde-epic\<NNN\>/\<SUBPATH\>/evidence\_index\_snapshot.json is non-authoritative; it MAY exist for compatibility or run-local context, but it MUST NOT be treated as canonical closure evidence.  
    
- Implementation Plans, QA plans, acceptance maps, and close-pack manifests MUST bind to the gate-family path above (not the EPIC-local variant).

Canonical JSON gate directory is a single canonical evidence family (no dual-home binding).

Canonical directory (normative): Canonical JSON gate artifacts MUST live under: audit/gates/json\_gate/canonical/

Canonical JSON gate artifact surfaces (normative; D19/D20 validate-existing steps):

- audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson  
    
- audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson  
    
- audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json

Naming posture (normative): Do not accept wrapper bundles or alternate filenames for canonical JSON gate artifacts. Use the canon-defined filenames above.

Path proof posture (normative): Each artifact above MUST be accompanied by its corresponding path proof(s) as defined by the owning canon (titles only).

Validation posture:

- Each \*.ndjson log MUST parse as JSON-per-line.  
    
- Each \*.ndjson log must include at least one record with status="pass" (i.e. the gate log is required to exist and the check must have executed; it cannot be a pure non-execution stub).  
    
- The structured record (json\_gate\_structured\_record.json) MUST parse as JSON; its schema and required fields are owned by HDE-Schemas & Artifacts.

Legacy directory posture:

- audit/gates/canonical\_json/ (including audit/gates/canonical\_json/json\_canonical\_check.log) is legacy/non-authoritative naming; do not treat it as the canonical JSON gate evidence family, and MUST NOT require it in Implementation Plans unless the owning canon explicitly reinstates it.  
    
- audit/gates/canonical/ is legacy/compat-only; do not treat it as the canonical JSON gate evidence family.

If tooling emits only to a legacy path, treat as a tooling defect; do not bind to it.

No dual-home acceptance binding:

- Acceptance maps, token/evidence matrices, and close-pack manifests MUST bind to the same canonical JSON gate family. Bind to audit/gates/json\_gate/canonical/ only.  
    
- Any deviation is a mechanical blocker: fix the binding, do not reinterpret.

Snapshot-and-verify acceptance-binding checks are allowed when the step is verifying an already-existing current-epic binding rather than regenerating it.

For such a step, PASS requires governed evidence that shows all of the following:

- the expected current-epic homes are named explicitly  
- the machine mirror contains matching rows for each of those same homes  
- no alternate acceptance-map home is detected for the current epic

When those conditions are met, the step MAY pass on a snapshot-and-verify basis without regenerating ledgers, relocating artifacts, or inventing alternate homes.

If any expected home is missing, any matching mirror row is absent, or an alternate acceptance-map home is detected, the step MUST NOT pass as a single-home acceptance-binding check.

Canonical compare artifacts: reuse canon surfaces (no epic-local compare paths). Default posture: compare proofs MUST bind to canon-defined compare artifact surfaces. An epic MUST NOT introduce a new compare artifact path as the canonical compare proof unless that surface has been introduced through the canon change pathway and drained into the owning canonical homes.

Any binding to a non-canonical path is a mechanical blocker and must be corrected before approval. If a non-canonical path is truly required, it must be routed via ADR and drained into the correct canonical home.

When a token is claimed as satisfied, the following artifacts MUST agree (paths and keys must match):

- Epic Plan required evidence list (per deliverable)  
    
- token/evidence matrix row for the token  
    
- docs/evidence/INDEX.json entry for the bound artifact  
    
- artifacts/evidence\_index.jsonl mirror record for the same artifact\_key and discovered\_physical\_path  
    
- the path-proof file referenced by proof\_anchor

This validation is enforced as a human review checklist line (pass/fail). An automated validator may be added, but the rule does not depend on automation.

#### 1.1.10.5 Phased-checklist subtask closeout (evidence-binding first)

When an epic claims closure of a phased-checklist task or subtask that is described as captured elsewhere or piecemeal, the default closure method is:

- bind existing governed evidence (tests \+ artifacts) into the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix)  
    
- rather than creating new evidence families

Creating a new evidence family for closeout is allowed only if:

- the PLAN includes an explicit gap statement (what is missing from existing evidence)  
    
- the new evidence aligns with the governed artifact conventions in HDE-Schemas & Artifacts

Closure is not considered complete unless the acceptance artifacts explicitly map the phased-checklist task/subtask to concrete evidence (no implicit it exists somewhere else posture).

When a plan, remediation guide, review artifact, or closeout artifact cites phased-checklist status or authority, it MUST reference each relevant current phased HDE-Build Checklist by exact title rather than a retired generic or single-document home.

This rule applies across all seven phased HDE-Build Checklists. If the cited work spans more than one phase, the artifact MUST name each relevant checklist explicitly.

If the correct phase home is unclear, the artifact MUST record that ambiguity as a drift item or doc-delta candidate rather than citing a generic retired checklist surface.

Exact-addendum live truth versus phased-checklist pre-drain status. When an exact applicable HDE-Build Notes addendum explicitly covers the mapped work, that addendum is the live in-flight authority for whether the work is complete in substance and supportable for later drain. The applicable phased HDE-Build Checklist remains the checklist mapping and later-drain record.

The current applicable phased HDE-Build Checklist status text is not a pre-drain gate for PR acceptability, OPS acceptability, QA readiness, or epic closure. It may be cited to show canon as currently drained, but it MUST NOT be used by itself as proof that the mapped work remains incomplete.

The controlling question is whether the exact mapped phased-checklist task or subtask is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review artifacts. When an exact phased-checklist subtask exists, that subtask is the controlling unit.

Combined-evidence supportability decisions.

When an earlier PR, OPS task, or remediation slice correctly preserved non-move or non-claim posture for its own bounded scope, that earlier non-move language does not by itself prohibit a later combined-evidence supportability decision.

A later review or ADR MAY support a mapped phased-checklist task or subtask to Done for QA-readiness or later-drain purposes when the combined evidence chain proves the full substantive burden for that row from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review artifacts.

The combined-evidence decision MUST name each contributing slice, state what each slice proved, explain why each earlier non-move condition was slice-local, and preserve non-claim boundaries for phased-checklist drainage, QA PASS, epic closure, admitted-token satisfaction, and OPS-as-QA substitution unless those stronger claims are separately proven.

Green tests, bounded diff scope, review-clean artifact posture, successful OPS execution, or refreshed evidence are necessary but not sufficient by themselves. They do not justify acceptable-status language unless the mapped work is actually complete in substance and the live record supports the later-drain posture.

If a slice is only contributory or intermediate toward a later phased-checklist close, approval and review artifacts MAY call it contributory, intermediate, review-clean, bounded, or supportable from repo evidence. They MUST NOT call it acceptable, accepted, satisfied, or complete-for-close.

Approval, review, retrospective, and closeout artifacts MUST keep these states separate:

- current applicable phased HDE-Build Checklist recorded status  
- supported later-drain status  
- actual implemented state  
- actual OPS state, when applicable  
- actual governed evidence state

They MUST NOT say that a slice is blocked only because the applicable checklist still says Not done or Partial, and they MUST NOT phrase a supportable status move as though that checklist has already been updated.

Parent-task drainage after partial subtask completion.

When evidence supports completion of one or more subtasks under a broader phased-checklist parent task, but not every child row or acceptance dimension under that parent is proven complete, review and closeout artifacts MUST keep the parent-task posture separate from the subtask posture.

A subtask may be recorded as supportable to Done while the parent task remains Partial, Consolidation pending, or another non-Done posture if unproven child rows, deferred dimensions, close-pack gaps, or drain-only caveats remain.

A parent phased-checklist row may be recommended for Done only when the review names every child row or acceptance dimension that must close that parent and proves that each one is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review artifacts.

If the parent-task decision is intentionally deferred to a later close or drain step, the artifact MUST say so explicitly and MUST NOT imply that subtask completion automatically closes the parent.

When a PR or OPS task is approved as a bounded non-closure step, review MUST be limited to the approved task in question and its explicitly approved scope.

A phased-checklist closure gate applies only when the approved task explicitly claims one or more of the following:

- it brings a mapped phased-checklist task or subtask to Done  
- it supports a Done recommendation now  
- it performs final closure, final binding, final acceptance promotion, or other explicitly closure-claiming work

If the approved task explicitly states that it does not itself close the mapped rows, contributes evidence only, is sequencing correction only, is validation-only, is blocker-classification only, or uses equivalent non-closure language, the reviewer MUST honor that boundary and MUST NOT require row closure in that review.

A bounded approved task may be accepted for truthful completion of its own approved purpose even when the mapped phased-checklist row remains open, provided the task stays within approved scope, does not overclaim closure, preserves any still-open phased-checklist row as open, contributory, intermediate, validation-only, deferred, or equivalent approved posture, and does not silently imply later closure work is already complete.

Review and acceptance language MUST distinguish task-level acceptance of the approved step from phased-checklist closure status of the mapped row.

A governed evidence family used to support review, remediation, closeout, or later-drain phased-checklist posture MUST express exactly one authoritative posture for each bounded task and each claimed closure dimension.

If one governed artifact in the same family says `closed` while another says `not yet closed`, `deferred`, `partial`, or other contradictory meaning for that same closure dimension, the family is mechanically non-acceptable until normalized. A consolidation artifact MUST NOT summarize contradictory governed bytes as if they form a valid single posture.

When runtime facts are unchanged and only the closure interpretation, approval posture, or documentation posture changes, remediation MAY be a documentation or evidence normalization pass rather than a new runtime rerun, but only if:

- no new runtime command, route behavior, environment binding, or OPS action is being claimed  
- every governed artifact in the affected family is refreshed to the same authoritative posture  
- the Human Evidence Index, hash sentinel, Machine Mirror, and required path-proofs are refreshed coherently in the same change  
- any earlier contradictory bundle is explicitly treated as superseded evidence rather than as a parallel truth surface

When closure is claimed by equivalence or substitution rather than by an independently exercised runtime, the approving plan, review artifact, or closeout artifact MUST state the exact closure mode explicitly, for example `Closure mode: binding-equivalence`, and MUST describe the limited basis for that equivalence.

Review and closeout classification MUST distinguish runtime or implementation failure from documentation or evidence failure. Reviewers MUST NOT demand a new runtime rerun unless runtime facts are actually missing, changed, or contradicted.

### 1.1.11 Plan review rules (content-first; blockers vs caveats)

Scope Plan review evaluates execution feasibility, deterministic pass/fail, and evidence wiring. Plan review MUST NOT gate on presentation-only formatting.

Template adherence is structural only. When a planning artifact uses a PF template, reviewers MUST evaluate template adherence only for structural completeness: required sections present, required gates present, required end marker present.

Header styling is not part of structural adherence. Reviewers MUST NOT request revisions solely to change heading levels, heading bold/italics, or other presentation-only formatting. If noted, record as a Nit (suggestion only) and do not block approval.

Review stability and no-moving-target discipline applies to diff-first approval loops for Epic Plans, Implementation Plans, Live QA Plans, remediation plans, and closeout reviews.

- Full-gate first pass is required. Before issuing the first approval decision on an artifact, apply the full active review gate set to the full artifact, not a partial subset.  
    
- Gate freeze across the same review loop. After the first review on a given artifact line, do not introduce a new blocker from already-visible unchanged text unless the later blocker is caused by newly added or materially changed text, a newly supplied authoritative input changes the review basis, PF canon changed after the prior review, or a prior tooling or read failure prevented the text from being fully visible.  
    
- Coupled-constraint rule. If a reviewer requires more explicitness, the same review MUST also declare the coupled constraints that the added explicitness triggers, including provenance, command-string, path and locus, creation-ownership, schema or header, lowercase or naming, and portability constraints.  
    
- Unchanged-text blocker rule. Any blocker first raised against unchanged text in a later revision MUST state the trigger that makes it newly raisable. If no valid trigger exists, classify the issue as Review Drift.  
    
- Review Drift handling. When a blocker was already visible in an earlier reviewed revision, label it Review Drift, state plainly that it was visible earlier, and consolidate any other same-scope pre-existing blockers in that same review.  
    
- Contradictory review prohibition. Do not alternate between too implicit and too explicit on the same requirement family unless the supporting canon constraint was already cited earlier or the later problem was created by newly changed text.  
    
- Read-failure and truncation handling. If an issue was missed because of truncation, partial retrieval, or other read failure, treat it as reviewer-side or tooling-side failure. Re-run the full sweep after full retrieval before issuing a new decision.  
    
- Non-author penalty rule. Do not frame omitted earlier blockers from unchanged text as author-created churn or as a fresh author-side defect cycle.  
    
- Approval integrity. This discipline does not require approving a real blocker. It requires that review be stable, complete, and non-contradictory, and that any later-discovered blocker be handled under the rules above.

This does not relax structural requirements. Missing required sections, missing required end markers, missing required gates, missing required pointers to HDE-Build Checklist or HDE-Mechanics Guide when required by this guide or the template, invalid/non-PF references, and ungrounded existence claims remain valid blockers.

Review-loop severity discipline.

A planning artifact MUST NOT be returned as REVISE AND RESUBMIT solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table order, heading style, punctuation, spacing, bold markers, missing titles-only polish, or similar presentation defects.

A blocker requires material harm to truth, proof, acceptance, execution, source authority, portability, implementation scope, applicable phased HDE-Build Checklist completion mapping, evidence identity, evidence trust, OPS or PR boundary, public or private surface posture, canon conflict handling, or closeout truth.

If no material harm exists, classify the issue as Nit, Suggestion, or Caveat.

Reviewers who block must state the material harm.

CA-vetted or audit-vetted fact labels are not blockers when the plan embeds the needed fact and the downstream actor can proceed without external CA, audit files, attachments, chat history, or implementation guides. They become blockers only when the artifact requires that external source or uses provenance wording to smuggle in unproven requirements.

Epic Plans are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Plan review MUST NOT demand QA-runbook-level precision, close-pack-level evidence completeness, or template inventory polish unless current planning truth depends on it.

Implementation Plans must be concrete enough for CodEx and OPS separation. A plan may be blocked for an independent non-syntax defect only when that defect remains after faithful syntax normalization and is proven without relying on malformed presentation.

Plan-execution artifact boundary.

Plans, review prompts, redline prompts, plan redlines, CodEx prompts, remediation plans, QA Plans, Live QA Plans, Implementation Plans, Epic Plans, implementation-readiness reviews, QA closeout reviews, epic closure reviews, and closure-review artifacts are planning and review artifacts, not execution artifacts.

Syntax and executability classification.

Presentation-only formatting defects are non-blocking only when a faithful normalization preserves the intended objective, command identity, inputs, outputs, authorization, rails, safety controls, evidence target, and pass or fail predicate. Reviewers may normalize harmless quoting, escaping, indentation, wrapping, Markdown rendering, or wrapper form when those semantics remain unambiguous.

A command or snippet is a material blocker when it cannot be normalized faithfully, is unsafe or ambiguous, changes semantic command identity or behavior, omits a required dependency or output, cannot execute in the permitted environment, or prevents the required verdict or evidence. The reviewer MUST state the surviving substantive defect and its material effect. A mixed finding must separate harmless presentation from the substantive defect.

Execution evidence MUST record the exact command actually executed, its exit status, captured output, produced artifacts, and final classification. A formatting correction during execution MUST NOT alter the acceptance target or hide an initial failed attempt. Actual repository code, canonical JSON, schemas, registries, governed machine-readable artifacts, and executed transcripts are evaluated under their owning contracts, not as presentation-only plan text.

Authored omission markers are source content and may be acceptable when they do not conceal required semantics. A retrieval-generated ellipsis, cutoff, omitted passage, or malformed source unit is a retrieval failure and MUST be reopened before reliance. Missing required evidence remains blocking even when an earlier syntax or presentation defect was harmless.

Documentation drainage and presentation polish MUST NOT delay readiness when truth, proof, scope, authority, safety, acceptance posture, phase fit, executability, and evidence identity are otherwise sufficient.

Approval-submission sentinel.

- Approval-submitted planning artifacts MUST include `ASK OK?` as the approval-submission sentinel when their purpose is to request approval before execution.  
- The presence of `ASK OK?` is intentional and MUST NOT be treated as stray text, formatting noise, or a blocker by itself.  
- Missing `ASK OK?` remains a valid blocker for approval-submitted plans.  
- The in-plan `ASK OK?` sentinel is distinct from the reviewer final verdict format, such as `ASK OK` or `REVISE AND RESUBMIT`; reviewers MUST NOT conflate the two surfaces.

Non-reviewable formatting (do not block)

Markdown heading depth, list-marker choice, whitespace, wrapping, boldface, italics, and equivalent presentation details are non-reviewable when required semantics remain clear. Harmless rendering escapes and wrappers may be normalized only under the syntax and executability classification above. They become material when faithful normalization cannot establish the required executable identity, safety, evidence, or result.

Review proof MUST distinguish authored source text, rendered output, copied quotation changes, and retrieval artifacts. If source-byte truth for a relied-on technical literal is unavailable, do not claim that the source contains it; retrieve the complete source or classify the fact as unknown.

Mechanical blockers (planning artifacts)

- Business Case is missing or not product-oriented: every Epic Plan MUST include a clearly labeled Business Case section that explains the product goal, the user problem, and the value (what changes for the user and what success looks like). If missing or purely technical, return the plan for revision.  
- Contract Change Justification is missing: the Epic Plan MUST include a clearly labeled Contract Change Justification section that explains any new or modified contract surfaces (CLI flags or modes, endpoint routes, output shapes) and why a new surface is necessary rather than reusing an existing one.  
- Backward compatibility posture is missing: the Epic Plan MUST include a clearly labeled Backward Compatibility posture section that states what remains unchanged by default, what changes (if anything), and the rollback plan if the change must be reverted.  
- Any plan fact that asserts a repo path, module home, env var name/value, CLI shape, script/module/check/test name, endpoint route, or other executable entrypoint MUST be validated (Canon-cited, CA vetted, IG Approved, or QA-created). Unvalidated or fabricated loci are mechanical blockers. Missing tooling is a repo gap to be addressed by PR work, not by QA-time script creation. (See §0.5.1.)  
* Plans MUST NOT use placeholders that shift responsibility to reviewers (for example: “PO will fill”, “TBD”, “???”, “e.g.”). If a value is unknown, the plan MUST cite a gap in PF canon and record it as a Tracked Issue with an owner and disposition.  
* Preferred omission-character hygiene: use the approved authored omission markers below instead of the Unicode ellipsis character (U+2026) or three consecutive full stops. An authored marker is acceptable only when it does not conceal required semantics; a retrieval-generated omission is a read failure.  
* Commands and snippets should be presented as plain text lines with surrounding context and clear labeling. Code-block formatting may be normalized only when the command identity and complete semantic contract remain unchanged.  
* Plans, QA plans, endpoint catalogs, and runbooks MUST NOT invent “proof-only” routes. A7 JSON-success proof routes MUST be registered in the Endpoint Catalog and must exist in the target runtime mount. Other route references MUST be defined by the owning transport canon and must exist in the target runtime mount. In particular:  
  - Reader surface: GET /reader (canonical). Reader v1 is selected via query param v=1 (for example: GET /reader?v=1).  
  - If the API is mounted under /api, /api/reader is an alias of the same Reader surface (not a separate contract).  
  - Plans and runbooks MUST NOT reference /api/reader-proof/v1.  
  - Aux narrative surface: `GET /api/aux/narrative?v=1` is canonical; `GET /aux/narrative?v=1` is its alias, as defined by HDE-CLI-API-Vendor-Ref.  
* Plans, QA prompts, and QA reviews MUST NOT introduce, require, or depend on run\_id, timestamped run directories, fresh-run roots, or any per-run directory nesting as operator input, step-log header field, manifest field, or correctness key.  
* Live QA evidence layout is checks-only under a stable epic-scoped QA root. Re-runs MUST refresh the same check directories and MUST NOT create new run roots for correctness purposes.

Approved omission markers (portable)

- OMITTED  
    
- OMITTED:shortreason  
    
- SNIP:\\\<n linesomitted  
    
- LISTCONTINUES  
    
- REPEATBLOCK

Portable formatting note (inline code-like values)

- For inline code-like values, use double quotes or a CODE: prefix. Do not rely on markdown rendering for meaning.

Reviewer safety posture (no guesswork)

- If a plan view is truncated, garbled, or otherwise unreadable, treat it as a read failure and retrieve the complete source text. Do not infer missing content. Distinguish an authored omission marker from a retrieval-generated ellipsis or cutoff; any retrieval-generated omission requires a complete reread and revalidation of dependent conclusions.  
    
- Reviewers MUST NOT propose or accept invented repo paths, command invocations, route paths, or token names as “probably right.” Require validation or mark as a blocker.  
    
- When quoting or redlining plan content, do not silently change escapes that affect execution semantics. If you normalize presentation-only escapes for readability, do it explicitly and ensure the quoted or pasted text preserves semantic meaning.

Simplified QA planning posture (planning-time expectations)

- Epic planning does not require a step-by-step QA playbook. Reviewers MUST NOT block on the absence of a full step list at PLAN time.  
    
- If a plan does specify QA steps, each step MUST define a concrete pass predicate and point to a governed evidence output (single primary file or manifest) so that acceptance is deterministic. Steps MUST reference real repo entrypoints and registered routes; missing tooling is resolved by PR work, not by QA-time script creation.

A QA plan is not approval-ready if any executable step depends on undeclared or unchecked tooling.

Helper and selected-check registration preflight. If a Live QA Plan, QA Guide, QA helper, runbook, or QA prompt names a helper script, helper module, QA check ID, QA step selector, runbook-local command entrypoint, or generated check registry as executable, the plan MUST include a preflight proving that the helper exists and that every selected check is registered or otherwise accepted by the helper before behavior execution begins.

Missing helper registration is a plan-to-execution tooling defect, not a product behavior failure. If selected-check registration cannot be proven before execution, classify the step as TOOLING\_BLOCKED or FAIL\_TOOLING as appropriate. Do not classify it as FAIL\_BEHAVIOR unless prerequisites are proven and the observed product behavior itself fails.

A bounded Moon Loop may repair helper or selected-check registration only when the correction remains inside QA-created helper surfaces or the approved QA evidence stream, preserves the original proof target, PASS or FAIL predicate, scope boundary, rails posture, secret posture, evidence identity, nonclaim boundaries, and no-new-token posture, and captures both the original failure and accepted rerun proof.

PO-approved Extended Moon Loop remediation.

A PO-approved Extended Moon Loop remediation is an event-bound, repository-anchored, routed continuation of one identified QA or hosted-CI failure, blocker, or evidenced safety defect after the ordinary Moon Loop boundary has been exceeded. It does not relabel product code, repo tests, repo generators, governed artifacts outside the QA root, or other routed remediation as ordinary Moon Loop correction.

An Extended Moon Loop exists only after fresh, explicit Product Owner direction recorded before the corresponding action. The direction MUST identify or make unambiguous:

- the epic and affected QA check or hosted-CI run  
- the repository or routed-source anchor  
- the triggering failure, blocker, or safety discovery  
- the unchanged proof objective and PASS or FAIL meaning  
- the permitted causal scope  
- the rails, network, credential, and data-safety posture  
- whether code change, external action, PR publication, merge, or CI completion is authorized  
- the completion gate  
- any one-time authority that expires separately

Each action class must be expressly authorized before use. Investigation authority does not imply write, external-call, publication, merge, OPS, deployment, or rerun authority. Required authority must exist before the action; later documentation may bind the authority record but cannot create authority retroactively.

A newly exposed defect remains inside the same Extended Moon Loop only when it is produced by, blocks, or invalidates the original correction or a required downstream gate; its relationship to the original proof chain is recorded; correction does not change the proof objective, acceptance surface, public contract, endpoint family, evidence family, or epic scope; and the affected surface follows its normal routing. An independent or opportunistic defect requires separate Product Owner disposition.

When those conditions remain satisfied, execution may continue within the recorded causal lineage without serial plan revisions. Replanning is required when the desired proof, product behavior, acceptance criteria, public boundary, endpoint family, evidence family, or substantive epic scope changes.

The record MUST preserve the original failed, blocked, or pre-routing receipt; each material root-cause finding; the exact changed paths or reviewable diff; canonical generator commands for governed outputs; local regression results; PR, routing, and merge receipts; intermediate hosted-CI failures; the final accepted QA receipt; and the final clean hosted-CI source and run when CI cleanliness is a completion condition. Earlier failures MUST NOT be converted into PASS.

An Extended Moon Loop does not by itself authorize another external interaction, OPS action, deployment, migration, service start, feature, route, public contract, acceptance criterion, token, evidence family, phased-checklist status change, board movement, acceptance claim, or epic closeout. It does not bypass PR routing, canonical evidence ownership, review, or hosted CI.

The Extended Moon Loop completes only when the original approved proof satisfies its final predicates, every required routed correction is present in the validation workspace, canonical evidence companions are coherent, required local regression gates pass, required hosted CI passes on the routed or merged source, and the complete receipt lineage is preserved. Extended authority expires at completion. One-time external, OPS, merge, or deployment authority expires under its own narrower terms and is never renewed implicitly.

For each executable step that depends on a command-line tool, interpreter, importable module, virtual environment, helper binary, or equivalent runtime dependency, the plan MUST define all of the following:

- the exact dependency or dependency set  
- the exact preflight check that proves the dependency is present and runnable  
- the exact activation or installation action to take if the dependency is missing, when such remediation is allowed in the execution venue  
- the failure classification to use if dependency readiness cannot be established

If the plan cannot truthfully specify the activation or installation action, it MUST say so explicitly and MUST treat a failed dependency preflight as unresolved dependency posture rather than inventing procedure.

A shared bootstrap step may exist, but each later executable step remains responsible for step-local readiness. Each later step MUST either include its own dependency preflight and remediation logic inline or explicitly depend on the bootstrap step and rerun a short step-local readiness check before the main behavior command.

If a dependency preflight fails and readiness is not restored by the plan-defined activation or installation action, the step MUST be classified as FAIL\_TOOLING or TOOLING\_BLOCKED as appropriate. It MUST NOT be classified as FAIL\_BEHAVIOR.

The dependency preflight result, any install or activation action taken, and the final ready or not-ready outcome MUST be captured in the step’s governed evidence stream.

Post-approval dependency discovery during Live QA.

If an executable dependency that was not fully listed in the approved plan is discovered during approved Live QA execution, the QA executor MAY restore dependency readiness and continue only when all of the following are true:

- the activation or installation action is allowed in the execution venue  
- the action does not change the proof target, PASS or FAIL predicate, scope boundary, rails posture, secret posture, product code, repo tests, public contract, PF document, acceptance token posture, or governed artifact outside the approved QA evidence stream  
- the same approved check is rerun to governed PASS after readiness is restored  
- the governed evidence records the initial failure or dependency event, the exact activation or installation action, the final rerun, and the final PASS or non-PASS classification

When those conditions are met, classify the event as an accepted plan-execution deviation or dependency-readiness doc-delta candidate, not as FAIL\_BEHAVIOR. If those conditions are not met, classify the step as TOOLING\_BLOCKED or FAIL\_TOOLING according to the observed state and the approved plan.

Deferrals and Tracked Issues (no silent drops)

- Any deferred scope item or Tracked Issue MUST record the owner-defined disposition and its required destination, identifier, or rationale. A future-epic deferral uses a destination epic ID or a permitted backlog stub. A Tracked Issue uses a current-epic completion record, carried-forward epic ID, cross-epic issue identifier, or explicit drop rationale, as applicable.  
    
- Deferred items MUST NOT be claimed as accepted or satisfied in the current epic.

Non-goals (for review)

- This section does not require exhaustive QA runbooks during epic planning.  
    
- This section does not change token semantics; it clarifies review gates for plan portability and determinism.

## 1.2 PLAN: Machine header (paste and fill, then post)

PF27-Canon-Plan-Templates is the sole canonical home for PLAN template structure, required and conditional fields, and status values. Use its current normative structured template. This heading does not establish a PF06 machine serialization; do not reproduce or extend a machine schema here.

The completed PLAN MUST preserve the process requirements in this section, including:

- a product-oriented Business Case;  
- Contract Change Justification for every new or changed contract surface;  
- Backward Compatibility and rollback posture;  
- exact phased HDE-Build Checklist mapping for task-like work;  
- explicit in-scope, deferred, and informative token posture using only names registered in HDE-Governance or explicitly minted by one exact applicable numbered HDE-Build Notes addendum pending drainage;  
- required versus conditional evidence and QA posture;  
- approved public-interface boundaries, dependencies, risks, and decisions;  
- the canonical close-pack baseline as a non-token artifact requirement; and  
- titles-only routing to the owning canon for technical contracts and acceptance semantics.

Applicability-specific fields MUST be completed only when the corresponding scope is present. The PLAN MUST NOT prefill A7, Reader, CLI, database, vendor, OPS, Live QA, close-pack, or acceptance results as universally applicable or already satisfied.

## 1.3 CRD: Machine header (copy/paste)

Apply the current PF27-Canon-Plan-Templates rules to every CRD field and structure that document governs. This heading does not establish a PF06 machine-readable CRD grammar. Do not invent or reproduce a local machine schema.

The CRD MUST state the approved scope, public-interface boundary, titles-only acceptance intent, conditional QA and OPS posture, and the governing evidence families. When Endpoint Catalog evidence is applicable, route to the canonical Catalog and checksum under `docs/**`; do not create an epic-local Catalog or an unspecified equivalent. Evidence minima MUST remain conditional on the approved scope and must not reproduce canonical token rosters or transport-byte contracts.

## 1.4 Adjacent pre-start gates (titles-only)

Some epics depend on deliverables owned by an adjacent role or workstream. A pre-start gate MUST name the deliverable and owner by title, map any task-like work to the exact applicable phased HDE-Build Checklist task or subtask, use only acceptance names registered in HDE-Governance or explicitly minted by one exact applicable numbered HDE-Build Notes addendum pending drainage, and require the applicable governed evidence update in the PR that unblocks the epic. An adjacent gate does not create a new acceptance token, evidence home, or execution authority.

## 1.5 Code capsules (PLAN/CRD samples)

Code capsules freeze at Implementation Plan approval. PF06 does not reproduce serializer, ETag, transport, or other implementation algorithms. Each capsule MUST point by exact title to its canonical owner and identify only the approved implementation boundary needed by the plan.

Canonical serialization and idempotence are owned by HDE-Math-Spec. Transport and CLI/Reader bytes are owned by HDE-CLI-API-Vendor-Ref. Architecture and single-emitter boundaries are owned by HDE Architecture. If the owning canon does not define an executable algorithm or contract completely, record a canon gap; do not supply a local approximation.

# 2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after CRD)

Define how work proceeds after CRD approval with enough precision for CodEx to execute without inventing scope, repository loci, commands, evidence paths, or acceptance claims. Lead Dev approves the Implementation Plan once and then participates only at the PR gate. The Product Owner remains the sole merger.

The workflow requires a CodEx-capable session that can inspect the repository, execute the authorized repository work, and open the required PR. Those capabilities are execution preconditions, not claims proven by this guide or by repository bytes.

## 2.1 Machine header

PF27-Canon-Plan-Templates is the sole canonical home for plan and runbook template structure, required and conditional fields, and status values. Use its structured Remediation Implementation Guide template only when that template applies. This heading does not establish a PF06 machine serialization; do not reproduce or extend a local machine schema.

The completed Implementation Guide MUST preserve this process:

1. Lead Dev publishes the approved Implementation Guide to the Implementation Agent.  
2. The Implementation Agent sends CodEx an audit request containing the approved scope, exact source pointers, required output contract, and any execution-critical source material permitted by the owning canon.  
3. CodEx returns an audit report that separates observed repository reality, risks, gaps, and unknowns.  
4. The Implementation Agent drafts the Implementation Plan using PF27-Canon-Plan-Templates. Lead Dev approves it once.  
5. The Implementation Agent sends CodEx the approved build instructions. CodEx may adapt within scope but MUST report every material deviation or improvement.  
6. CodEx returns a detailed change report and the available repository evidence. The Implementation Agent either requests bounded corrections or approves the result for PR gating.  
7. CodEx opens the PR and includes the approved code and repository-document changes. When governed evidence changes, the same PR MUST update the Human Evidence Index, its hash sentinel, the Machine Mirror, and required path-proof companions.  
8. Lead Dev reviews the PR against the approved scope and verifies only acceptance claims admitted by HDE-Governance or one exact applicable numbered HDE-Build Notes addendum pending drainage. Canonical close-pack files are verified separately as non-token baseline artifacts.  
9. When A7 is in scope, Lead Dev verifies the applicable A7 posture through the owning canon and the cataloged success-route proof surface. `/internal/version` is not an A7 proof route.  
10. The Product Owner performs the squash merge only after the applicable gate is satisfied and then informs the Scrum Master.

All evidence referenced by the Implementation Guide MUST use governed roots under `audit/**`, `artifacts/**`, or `docs/**`. Transient and generator paths are not acceptance surfaces. The guide MUST distinguish requirements from observed repository state and MUST NOT prefill PASS, completion, merge, QA, OPS, or closeout results.

## 2.2 Audit (CodEx)

The audit establishes whether the current repository can host the approved change without violating the owning canon. It is static repository analysis unless a separately authorized task expressly permits more. It does not execute QA or OPS, prove runtime behavior, or create acceptance claims.

The Implementation Agent supplies the approved scope, exact source identifiers, and the applicable Audit Analysis Record requirements from PF27-Canon-Plan-Templates. CodEx MUST report confirmed, partial, contradictory, not-found, and non-repository-verifiable states separately.

The audit MUST cover every applicable item below:

- Canonical serialization and idempotence: identify the single current implementation locus and report duplicate or ad hoc emitters without reproducing the governing algorithm from HDE-Math-Spec or HDE Architecture.  
- Public transport: when A7 is in scope, determine whether the cataloged JSON success-route surface can satisfy the applicable GET, HEAD, conditional, `Vary`, encoding, writer, and error requirements owned by HDE-Governance and HDE-CLI-API-Vendor-Ref.  
- Endpoint Catalog: inspect the canonical Catalog and checksum at their documented single home. Distinguish its endpoint inventory from `success_endpoints` and do not infer A7 eligibility from route presence alone.  
- Composite proof: when applicable, identify the current canonical proof family and schema through HDE-Schemas & Artifacts. Do not mint an alternate proof home.  
- Closed-rails refusal, logging, and security: verify only the statically inspectable keys-only, redaction, refusal, and guard surfaces. Do not treat checked-in definitions as runtime PASS.  
- Aux narrative: when in scope, use canonical `GET /api/aux/narrative?v=1`, with alias `GET /aux/narrative?v=1`, as defined by HDE-CLI-API-Vendor-Ref. Do not reproduce its transport-byte contract here.  
- Database transport: apply HDE-Build Notes Addendum 2.12, “pg-bridge and DB\_BRIDGE\_URL Deprecation and Retirement \- Direct PostgreSQL Is the Sole Active HDE Database Transport.” `DATABASE_URL` is the sole active database endpoint, direct PostgreSQL through the Glow-owned psycopg provider is the only selectable transport, retired bridge keys fail before provider selection without logging values, and unavailable direct access fails closed without alternate transport. Any new evidence path must be canon-defined, audit-proven, or explicitly created under an approved governed root.  
- Evidence parity and PR readiness: inspect the Human Evidence Index, hash sentinel, Machine Mirror, and applicable path-proof companions at their canonical homes. Confirm only what the pinned bytes support.  
- Governed locations: reject proposed acceptance bindings outside `audit/**`, `artifacts/**`, and `docs/**`.  
- Negative findings: record the exact search scope, searched literals or predicates, source, and result. A failed or incomplete retrieval is unknown, not absence.  
- Gaps and proposals: identify the minimum source-grounded correction and its owner. Do not convert a documentation gap into implementation, QA, OPS, or phased-checklist scope by assumption.

The audit report MUST apply the current Audit Analysis Record requirements in PF27-Canon-Plan-Templates. It MUST include an audit summary and a complete finding-to-delta map when findings exist. Each finding must state the observed fact, source anchor, repository evidence pointer when applicable, relationship to the approved epic scope, urgency, and correct owner.

Task-like implementation, QA, OPS, runtime, evidence, vendor, architecture, or product-behavior work MUST map to the exact applicable phased HDE-Build Checklist task or subtask. When no current row accounts for legitimate phased-build work, classify it as a phased-checklist gap. Documentation or status drainage alone is not a runnable task. HDE Phased Epics is historical-only and MUST NOT receive in-flight planning or task scope.

When current canon already classifies an observation, the audit MAY mark it classification-only. It MUST cite the owning title, state that no new delta is needed, and avoid inventing runnable work. Open questions are permitted only for a material unresolved owner, routing, or scope choice after the governing sources have been retrieved completely.

## 2.3 Code Review (CodEx)

Record Code Review in structured Markdown under this heading and apply any relevant review-record rules in PF27-Canon-Plan-Templates. Before review, every result field MUST remain unassessed rather than defaulting to success. This guide does not assert a separate PF27 generic Code Review template.

The review MUST determine, within the approved scope:

- whether public payload and narrative surfaces comply with their owning content rules;  
- whether writer and error behavior follows HDE-Governance;  
- whether deterministic paths avoid uncontrolled randomness and time;  
- whether the change adds a public interface outside the approved interface set; and  
- whether any material red flag, deviation, limitation, or unsupported claim remains.

Static review does not prove runtime success, test PASS, deployment state, or external configuration.

## 2.4 Sandbox Build/Test (CodEx)

Record Sandbox Build/Test in structured Markdown under this heading. Before execution, test and verification result fields MUST remain unassessed. Populate them only from evidence produced by the authorized build or test work. This guide does not assert a PF27 generic Sandbox Build/Test template.

The result MUST describe what was built, what was verified, the exact files added, modified, or removed, every deviation from the approved instructions, scoped improvements, known limitations, and suggested follow-up. It MUST distinguish executed results from proposed work and must not claim QA, OPS, merge, phased-checklist drainage, or epic closure unless those separately authorized actions occurred and are proven by their owning evidence.

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

Assigned HDE-Build Checklist scope is binding for each PR. When the approved Implementation Plan, remediation plan, or review scope assigns specific HDE-Build Checklist tasks or subtasks to a PR, that PR MUST either complete every assigned subtask or explain each unresolved assigned subtask in detail before the PR can be treated as complete.

The explanation MUST identify each affected task ID and subtask ID, state exactly what was completed, state exactly what remains incomplete, describe the blocking condition or limiting constraint, explain why completion was not possible within the approved PR scope, and cite the repo evidence, test result, or other concrete basis for that conclusion.

Silent omission, partial completion without this explanation, or a completeness claim that ignores unresolved assigned subtasks is non-conforming.

The Product Owner (PO) is the sole merger (squash on PASS).

Epic-level acceptance (as recorded in HDE Phased Epics) occurs only after:

* all required PRs for that epic have merged

* the Close Gate has been satisfied

HDE Phased Epics is historical-only: the epic record is added there once, at epic close, as the final archived entry. In-flight epics MUST NOT be recorded there.

The Close Gate applies to the PR that carries the epic close-out (close PR).

All earlier PRs in the series must still be PR-first and parity-clean.

Only the close PR is required to carry the full close-pack and final PASS roster described below.

Feedback-free terminal lifecycle.

An ordinary Close Gate lifecycle MUST be terminally reachable. All tracked candidate bytes required for the final close state MUST be complete before hosted validation, and hosted CI MUST validate those exact candidate bytes without requiring canonical results to be written back into source.

A Close Gate lifecycle MUST NOT require hosted CI to mutate the tracked candidate after validation, require a later source commit to absorb the result needed to validate the earlier candidate, or otherwise create a source-to-CI-to-source causal back-edge. If the terminal transition cannot be produced and validated without that feedback cycle, the lifecycle is not eligible to establish ordinary Close Gate completion and must be stopped and separately dispositioned.

Exceptional closure record.

Failure or withdrawal of an ordinary Close Gate lifecycle does not establish closure and does not itself authorize an exception. Only an explicit Product Owner decision may authorize closure of one identified epic outside ordinary Close Gate completion.

The exceptional-closure record MUST:

* identify the epic, the Product Owner authority, the exception scope, and the accepted delivered business outcome  
* identify the failed, stopped, or withdrawn closeout lineage and the current merge posture of any related PR or candidate artifacts  
* state every ordinary Close Gate element that was not achieved or is not claimed, including applicable Gate results, token satisfaction, `SATISFIED` posture, close report, close manifest, acceptance map, close-pack completion, and merged close PR  
* preserve the current evidence-supported QA, implementation, OPS, and repository facts without allowing one proof class to imply another  
* state whether PF09 status movement, board movement, PF-Canon drainage, or phase exit occurred; absent separate proof or authority, each remains expressly unclaimed  
* identify unresolved closeout architecture, token, canon, evidence-lifecycle, or subsystem debt and route it to separately authorized future work  
* state that the exception is epic-specific, does not establish ordinary Close Gate completion, and does not create a reusable default for another epic

An exceptional closure record MUST NOT relabel a failed or absent ordinary close pack as complete, infer unproven tokens or gates, merge an unmerged candidate by declaration, establish phase exit, or authorize the carried future work.

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
* a tracked-issue closeout mapping in the close report for any TI-\* items cited by the epic (example: TI-002): each TI item MUST map to either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets so closure is unambiguous.  
* an explicit binary closure decision in the close report: SATISFIED or NOT SATISFIED.  
* if the decision is NOT SATISFIED, the close report MUST list the minimal follow-ups required to make closure defensible and canon-aligned.  
* if the decision is SATISFIED after an earlier interim readiness or closeout artifact recorded a different verdict, the close report MUST identify the superseded artifact and state the governed evidence change that justifies the final decision.  
* interim readiness or QA closeout artifacts MAY exist during remediation, but only the final close report decision governs epic close.

Close-pack presence is a baseline artifact requirement, not a token by default. Convenience copies elsewhere MAY exist for human convenience, but MUST NOT be used for acceptance binding.

A Live QA step that validates close-pack generation or close-pack completeness MAY stage check-scoped copies of the canonical close-pack artifacts under the stable step root as QA-run-produced deliverables.

Those copied artifacts are validation surfaces only. The step MAY use generator exit status and the existence of the copied artifacts as its PASS predicate when that predicate is stated explicitly in the approved plan.

Such copies MUST NOT replace, rename, or redefine the canonical close-pack baseline files. Final close-pack acceptance remains bound to the canonical filenames listed above.

Ops closeout provenance run (OPS-02). When existing closeout evidence is not enough to prove venue or execution provenance, an Ops task MAY perform a provenance-only run after the close-pack baseline is surfaced.

OPS-02 MUST remain bounded:

* no full QA rerun  
* no invented QA outcome  
* no canon-drain claim  
* no merge-provenance claim

OPS-02 SHOULD prefer binding existing evidence. It MAY use a minimal rerun of one governed QA step or one governed artifact family only when that is the smallest truthful way to create the provenance binding.

The OPS-02 execution bundle MUST include, at minimum, commands.txt, repo\_root.txt, repo\_head.txt, python\_version.txt, stdout.log, stderr.log, exit\_codes.txt, and one primary provenance artifact. If the primary provenance artifact is treated as governed closeout evidence, it MUST also have a sibling path-proof transcript.

The primary provenance artifact MUST state the governed artifact path being bound, the in-session command family, the venue or Codespaces context used, the repo root and commit linkage, and the non-claim boundaries for the run.

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

If the close PR includes generated acceptance-ledger artifacts or generated close-pack artifacts, reviewability requires more than path presence. The close PR MUST make all of the following explicit and auditable in the same PR:

* whether the acceptance map, token-evidence matrix, and viability log bind the full intended proof-family roster for the slice or only a reduced subset

* whether any reused proof families are explicitly named as reused bindings rather than implied by narrative summary

* whether the close report and manifest describe only work that was actually executed in that run

If a close report, manifest, or generated review artifact claims that the Human Evidence Index, hash sentinel, Machine Mirror, path-proofs, or validator or gate outputs were refreshed or re-validated, that claim MUST be backed by same-run governed execution evidence in the PR. Narrative assertions of execution are non-conforming unless the executed workflow evidence is present.

When changed governed artifacts require checksum, index, mirror, or path-proof companions, those companions MUST be refreshed coherently in the same PR and MUST carry chronology that is current for that refresh. Stale or backdated companion chronology is a close-blocking evidence defect until regenerated with canonical tooling.

When the close-pack slice reuses previously completed proof families rather than re-implementing those slices, the close-pack bindings MUST identify that reuse explicitly and MUST point to the same-run gate or QA-log anchors used to prove the close workflow actually ran.

Generated close-pack artifacts MUST separate canonical acceptance tokens from PF09 scope bindings. Acceptance maps, token-evidence matrices, viability logs, close reports, and manifests MUST NOT mint epic-local acceptance token names to stand in for PF09 tasks, subtasks, or slice-completion claims.

The close report and manifest MUST state the full approved PF09 scope for the close slice, even when only part of that scope is directly tied to acceptance tokens or QA bridge evidence.

A temporary or bridge token may be promoted from `Planned`, `token_incomplete`, or equivalent incomplete posture to `Implemented`, `COVERED`, or `PASS` only when the governing QA logs exist at the canonical governed paths and those logs show the required success result.

Narrative assertions, anticipated future runs, or missing-path placeholders are not sufficient for this promotion. The generated close-pack artifacts MUST bind directly to the actual QA log paths and their governed manifest or index anchors.

If accepted OPS evidence states that an environment remains `not yet closed`, the close-pack MUST preserve that status explicitly. It MUST NOT rewrite the environment to closed or imply that the mapped PF09 subtask is complete merely to tidy the final package.

When a generated close-pack or acceptance-ledger slice is a sequencing, anti-overclaim, or other non-closure step, it MUST remain blocked, incomplete-planned, deferred, or equivalent non-closure posture until the approved closure preconditions are truthfully met. Successful regeneration of the artifacts is not sufficient by itself to justify close-binding or PASS promotion.

If a generator or close-binding rule is intended to support later PF09 closure, it MUST depend on explicit proof markers for each mapped PF09.x task or subtask that the slice claims to close, together with any required environment-closure conditions for mapped OPS or harness rows. Generic readiness flags, narrative assertions, or artifact existence alone are not sufficient for this promotion.

When the current evidence does not yet satisfy those explicit proof markers or required environment closures, the regenerated outputs MUST preserve the blocked or incomplete-planned posture and MUST NOT imply that later work is already complete.

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

* expected evidence under audit/qa/\<epic-id\>/checks/\<check\_id\>/ (stable check-scoped evidence; no per-run nesting, no run-id directories, and no operator-selected fresh-run root)

If the epic claims QA Acceptance Tokens, the plan must name the QA ledger artifacts by path. This includes the token/evidence matrix location (titles-only semantics) and any other governed ledgers required for close.

Acceptance-map viability is a Close Gate input. If the Live QA harness produces an acceptance-map viability check, that check MUST be meaningful (not default-PASS) and MUST block epic closeout readiness when it fails; the harness run MUST surface that failure (including influencing the harness exit status) so Close Gate work does not proceed on a false PASS.

Mandatory D0 Discovery artifact and QA RCA summary are present. The epic MUST satisfy the Live QA execution deliverables in §0.4.1:

* a governed D0 Discovery artifact under the epic’s QA tree

* a QA RCA and Doc Delta summary (as part of the close report or as a governed artifact referenced by it)

Execution environment and venue materiality. Every governed Live QA execution MUST use an environment permitted by the governing Live QA Plan or applicable QA authority, execute the required governed harness, and produce governed, reproducible evidence under audit/qa/\<epic-id\>/checks/\<check\_id\>/ using the stable check-scoped layout.

GitHub Codespaces remains the canonical and preferred shared HDE QA console. Canonical and preferred do not mean exclusive or mandatory for every epic.

Codespaces execution and governed Codespaces provenance are mandatory only when Codespaces is materially part of the approved proof scope. Venue is material when the approved claim concerns a Codespaces-specific repository configuration, bootstrap, image, tool, secret-injection behavior, provisioning behavior, network behavior, forwarded port, mount, filesystem behavior, provider identity, operator-support promise, provider-sensitive defect, or another condition reasonably capable of changing the result in Codespaces.

A Live QA Plan that makes venue mandatory MUST state:

* `Venue-specific claim`  
* `Why venue can affect the result`  
* `Required venue evidence`  
* `Effect of missing venue evidence`

Without those four statements, an execution-venue field records the intended or preferred operator surface and does not create a separate acceptance criterion or closeout blocker.

When venue is not material:

* absence of Codespaces provenance is not a QA failure or closeout blocker  
* an otherwise supported behavior result MUST NOT be downgraded solely because the execution venue is unknown  
* reviewers MUST NOT infer where execution occurred  
* the venue posture MUST be recorded as `NOT CLAIMED`, `NOT APPLICABLE`, or `UNKNOWN - NON-MATERIAL`, as appropriate

Regardless of venue, the governed execution evidence MUST capture every material fact needed to interpret the result, including the stable check identity, execution-source identity, governed entrypoint or command family, repository locus, relevant runtime and dependency readiness, deterministic pins, rails and network posture, external target identity when applicable, secret-binding posture without secret values, PASS or FAIL predicate, exit status and result output, governed evidence paths and bindings, and any accepted material execution deviation.

When venue is material, at least one governed artifact MUST bind the exact check or artifact, the Codespaces venue, canonical repository association, execution-source identity, command or command family, the specific Codespaces property being proven, and sufficient chronology to connect the execution to its resulting evidence.

A venue substitution is material only when venue is a proof axis, the substitution changes a material dependency, target, rails, network, secret, or runtime condition, or the governing plan forbids substitution for a supported reason. Otherwise, substitution is acceptable when the environment contract and every check predicate remain satisfied and the actual posture is recorded truthfully.

Live QA evidence landing is PR-first and parity-clean. Live QA evidence MUST land under governed roots and follow the same-change-set evidence parity rule:

* Live QA step artifacts under audit/qa/\<epic-id\>/checks/\<check\_id\>  
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

Post-QA documentation drainage ordering (normative).

* All required QA tasks, remediation loops, runtime-proof checks, and close-gate QA reviews MUST be completed before documentation drainage begins.

* If a canon delta, checklist delta, guide delta, summary correction, or other documentation correction is known but not yet drained, PF10 is the controlling temporary source of truth for that item until drainage occurs.

* Undrained documentation changes MUST NOT be used as blockers for finishing QA execution, issuing step verdicts, issuing epic QA closeout review, or deciding epic close posture, provided PF10 explicitly records the truth of what happened and the required QA proof is otherwise complete.

* Allowed close blockers remain limited to QA truth and proof failures, including incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.

* When a documentation mismatch or canon delta is found during QA or closeout, it MUST be recorded in PF10 as a follow-up, implementation gap, ADR note, or doc-delta item. It MUST NOT be converted into a pre-drain closure blocker solely because the destination PF document has not yet been updated.

* Post-QA drain ordering is mandatory. Drainage into canon, checklist rows, guides, or other document homes occurs only after all QA tasks for the epic are complete.

* This rule changes timing, not honesty requirements. PF10 MUST still state open doc deltas, remaining follow-ups, and any caveats plainly and explicitly.

* Reviewers and closeout authors MUST NOT treat an undrained documentation delta by itself as proof that the epic is not ready. A not-ready posture is justified only when the undrained item also reveals a real QA truth or proof failure.

* If QA evidence is complete and trustworthy and all required QA tasks are complete, the epic MAY be recommended as ready for closeout even when undrained documentation deltas remain. Undrained documentation deltas alone do not justify a not-ready verdict.

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

Repo docs sweeps MUST distinguish implementation-slice evidence, close-pack evidence, Live QA evidence, formal PF-Canon drainage, and historical evidence. They MUST NOT present PR-slice artifacts, repo-doc validation, or historical evidence families as close-pack artifacts, Live QA proof, PF-Canon drainage, or final closure evidence unless those exact artifacts or results are directly proven.

Repo docs sweeps MUST prove non-obvious claims before documenting them. Before a sweep adds or updates claims about commands, flags, workflows, file paths, module paths, service names, endpoints, config keys, environment variables, artifact paths, token names, validation references, evidence roots, or PF terminology, the sweep MUST ground those claims in repo reality, PF10, or PF-Canon.

The sweep artifact or review record MUST preserve the proof posture for those claims, such as repo-proof notes, PF10 anchors, PF-canon anchors, or an explicit Unknown or Not verified statement.

Docs-only scope validation MUST also prove that code, tests, schemas, generated evidence, governed evidence indices, and PF-Canon files were not changed unless those changes were separately approved.

If a docs PR or repo-docs sweep states that repo-proof checks were performed, but the final closeout review did not inspect repo state directly after that docs PR, the review MUST mark final repo path existence and docs-only scope validation as Unknown or Not verified for that review.

The review SHOULD record a future repo-only audit, closeout audit checklist item, or PO adjudication item for final path-existence confirmation. This follow-up is not a closure blocker by itself unless the approved closeout gate required direct repo-state proof in the current review.

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
  * the decision point or ambiguity being resolved  
  * the materially different options considered, when more than one real option was on the table  
  * the PF-canon constraints or governing passages that bounded the choice  
  * the final decision for this epic  
  * whether the decision should become canonical for future work, or remain epic-specific only  
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

PO-approved Extended Moon Loop lineage. After fresh, event-specific Product Owner approval establishes an Extended Moon Loop, one recorded causal lineage MAY span multiple focused commits, remediation PRs, merge cycles, hosted-CI reruns, and mechanically necessary canonical companion refreshes without repeated remediation-plan issuance, provided that:

* the original proof objective, acceptance surface, substantive scope, rails posture, evidence identity, and nonclaims remain unchanged  
* every later defect is causally produced by, blocks, or invalidates the original correction or a required downstream gate  
* the relationship of each later defect to the original proof chain is recorded  
* each changed file or system follows its applicable PR, OPS, QA-plan-update, or documentation-update routing  
* the complete failure, correction, routing, merge, rerun, and final-validation receipt lineage is preserved  
* every action class was expressly authorized before that action occurred

A separate plan or Product Owner disposition is required when a new defect is independent or opportunistic, or when the desired proof, product behavior, acceptance criteria, public boundary, endpoint family, evidence family, or substantive epic scope changes. Prior one-time approval never supplies recurring authority for a later event.

Close Gate responsibility. The Close Gate for the epic MUST confirm that:

* any required remediation PRs have merged

* the close-pack and Evidence Index and mirror reflect the post-remediation state

Close-pack regeneration rule (no stale close-pack cuts). If any remediation run or remediation PR changes:

* a step status (FAIL\_\* → PASS or similar)

* any governed evidence that the close-pack summarizes or references

then the close-pack artifacts MUST be regenerated after the remediation is complete so they represent the final closure cut.

The Close Gate MUST NOT treat an earlier pre-remediation close-pack as final.

If the close-pack generator depends on a QA ledger or manifest, that input MUST be unambiguous for the closure cut (no duplicate entries for the same logical run or step identity). If the ledger is ambiguous, treat it as a tooling failure and resolve it before generating or accepting the close-pack.

If the close-pack generator uses qa\_step\_logs\_manifest.json or any equivalent QA ledger as a closure input, the final closure cut MUST expose one authoritative executed-check ledger that records, for each executed or posture-only step, at least the check\_id, status, and the path to the primary.log or equivalent governed evidence file.

An empty checks list, omitted executed steps, duplicate step identities, or a ledger that does not make its authoritative executed-check field explicit MUST be treated as a tooling failure for closeout.

If a different canonical field or artifact is used instead of a checks list, the close report MUST name it explicitly so Coverage vs plan-step accounting can be reconstructed without manual detective work.

Any step-identity mismatch between a closure ledger entry, a check heading, and the referenced evidence pointer MUST be treated as the same tooling failure until corrected.

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
  * Note: If docs/ENDPOINTS\_CATALOG.json bytes change, regenerate the checksum and path-proof sidecars in the same PR.  
* Catalog path-proof transcript — docs/ENDPOINTS\_CATALOG.json.path\_proof.txt  
* Catalog checksum path-proof transcript — docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt  
* Audit mirror (records-only) — artifacts/audit/ENDPOINTS\_CATALOG.json  
* Audit mirror checksum — artifacts/audit/ENDPOINTS\_CATALOG.json.sha256  
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
* Full-gate first pass is required. Before issuing the first approval decision on the artifact, apply the full active review gate set to the full artifact, not a partial subset.

* After the first review on a given artifact line, do not introduce a new blocker from unchanged text unless the later blocker is caused by newly added or materially changed text, a newly supplied authoritative input changes the review basis, PF canon changed after the prior review, or a prior read failure or truncation prevented full visibility.

* Any blocker or caveat raised against unchanged text MUST state the trigger that makes it newly raisable.

For close-pack or acceptance-ledger remediation sequences, the review MUST distinguish all of the following separately:

* canonical file existence

* content completeness of the acceptance ledger

* truthfulness of any claimed write or check workflow

* chronology freshness of changed governed companions

An acceptance-ledger slice is not satisfied merely because the acceptance map, token-evidence matrix, or viability log exists. If the reviewed outcome binds only a reduced global subset when the approved slice depends on reused proof families, the review MUST mark that requirement as not yet satisfied until the binding model is expanded or the missing families are explicitly handled as non-claims.

If the final recommendation depends on a combined Original plus Remedial outcome, the review MUST state what earlier drift or blocker was reversed, what net-effective shipped state remains after remediation, and why that final combined outcome supports the status recommendation.

When the review supports a PF09 task or subtask status move, the review SHOULD state the exact impacted PF09 row or rows, the current PF09 status posture, the recommended status move, and the specific final evidence basis for that recommendation.

When a review uses Codex Audit observed evidence, the review MUST label it as planning-time or review-time repo-reality support and MUST NOT overclaim it as acceptance proof, QA PASS, OPS completion, PF09 status movement, PF-canon drain completion, epic closure, production truth, external vendor truth, open-rails truth, or canon authority.

If a review identifies a remaining canon delta whose correct home is another PF document, the review pack MUST route that delta to the correct home and MUST NOT silently convert it into a PF06 process delta.

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
  * Net-effective shipped state (required for remediation sequences): after listing attempts, add a short block that states what remains in the final combined outcome after the last remediation. If the review depends on a combined Original plus Remedial result, say so explicitly.  
  * Reversed or canceled drift: if an earlier attempt introduced risky or out-of-scope changes that were later undone, name them and state plainly that they do not remain in the final shipped change-set.  
  * Final approval basis: state which requirements were already satisfied before remediation, which blocker or blockers were resolved later, and why the final review is based on the combined outcome rather than on any single intermediate attempt.  
  * Read-only closure-proof attempt: when the remaining blocker is proof of final net branch truth or scope cleanliness rather than a new code or evidence change, a remediation sequence MAY end with a read-only closure-proof attempt instead of another write-producing attempt.  
  * Read-only proof requirements: the review MUST state that no repo edits or governed-artifact regenerations were made, MUST identify the latest write-producing attempt whose green validations remain the operative functional evidence, and MUST explain why a no-edit proof pass is sufficient.  
  * Branch-truth proof posture: the read-only proof MUST establish the final shipped state against the named comparison target by recording the current comparison posture and the net-diff status for any previously disputed files or artifact families.  
  * Closure effect: a read-only closure-proof attempt may resolve a provenance or scope-cleanliness blocker without reopening implementation only when it proves that no further repo edits remain and that the final combined outcome is the shipped state under review.  
  * Read-only discovery or source-skew proof attempt: when the approved PR purpose is discovery-only, no-edit, no-diff, source-skew, or boundary-classification proof, the review MAY accept the artifact without diff hunks, tests, or committed governed artifacts only when the review states that no repo edits or governed-artifact regenerations were made, identifies the discovery questions answered, names the read-only command ledger or inspected source basis, and preserves any mapped PF09.x row as No status change recommended unless the approved task claimed closure and produced governed evidence for that closure.

### **Diff Review (REQUIRED; primary technical review)**

DR-001

* Change summary: \<one change\>

* Risk assessment: \<Low | Medium | High\>

* Why it matters: \<why a reviewer should care\>

* Evidence pointer: \<diff path and hunk; preserve \+ and \- markers if quoting a diff\>

* Canon basis: \<CANON | CANON SILENCE\>

* Approved Plan linkage: \<approved plan section heading or acceptance token names\>

Repeat DR-\#\#\# as needed.

Common DR checks (Lead Dev gate):

* File-list integrity: if the PR review pack includes a "File list:" section, every listed repo path MUST appear as a changed path in the PR diff, unless it is explicitly labeled as non-diff evidence (CI log URL) or as a runtime-generated artifact that is not committed.

* Duplicate patch blocks: if the PR diff contains duplicate `diff --git` blocks for the same path, treat this as a packaging or review artifact error and resolve it before approval.  
* Intermediate vs final posture: when a review bundle contains an early risky hunk and a later corrective hunk for the same logical area, reviewers MUST call out both and MUST state which hunk reflects the final shipped posture.  
* Scoped proof lane guard: a PR may introduce a narrow closure lane or scoped assertion set only if the main lane retains the broader fail-closed safeguards it previously carried. Dropping those safeguards without an explicit approved scope change is a blocker.  
* Duplicate diff distinction: duplicate `diff --git` blocks in the actual PR diff remain a packaging error and must be resolved before approval. Duplicate diff excerpts inside the review bundle, when they refer to the same already-reviewed patch and do not correspond to extra changed paths, are a reviewability caveat and MUST NOT be counted as additional shipped behavior.  
* Output-claim integrity: if the PR review pack enumerates expected outputs, verify that committed outputs have corresponding diffs and that runtime-only outputs are labeled as such.  
* Positive installability proof: when a PR claims shipped installability, entrypoint readiness, or console or module availability, the review MUST prefer positive proof of the shipped entrypoint or module path. Skipped or negative placeholder artifacts do not satisfy that claim unless the approved plan explicitly allows a non-installability posture.  
* Fail-closed entrypoint posture: if the claimed shipped entrypoint is missing during proof generation, the proof MUST fail closed or report the missing entrypoint as a blocker. It MUST NOT silently downgrade the artifact to a pseudo-pass.  
* Ambient environment guard: installability or conformance proof MUST NOT depend on ambient host PATH or other unstated shell state. The generator or captured commands MUST pin or derive the environment they rely on, and the review pack MUST state what path or env basis the proof used.  
* Single-source proof metadata: when a PR emits installability, help, version, or entrypoint metadata in more than one artifact, the review MUST verify those artifacts agree or identify which artifact is authoritative. Duplicate or conflicting proof metadata is a blocker until reconciled.

### **Findings**

F-001

* Observed: state what was observed.

* Why it matters: state why it matters.

* Source: state where the observation originates.

* Evidence pointer: state the diff hunk, log, test output, or artifact path.

* Review provenance: state exactly one of Introduced by current revision, Previously raised and still unresolved, or Review Drift.

* Trigger if based on unchanged text: state the trigger that makes the issue newly raisable, or state Not applicable.

* Impacted PF09 task ID(s), if proven: list only task IDs directly supported by this finding, or state No proven PF09 impact.

* Impacted PF09 subtask ID(s), if proven: list only subtasks directly supported by this finding, or state No proven PF09 impact.

* Supported PF09 status posture: when the finding supports a PF09 status move, state the exact posture supported by this finding. Otherwise state No proven PF09 impact.

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
* If a remediation review identifies more than one distinct cause, record each root cause separately with its own evidence pointer rather than collapsing them into one narrative.  
* If a PR adds or regenerates governed artifacts, reviewers MUST verify that changed artifacts, path-proofs, index rows, mirror rows, and checksum sidecars carry current and internally coherent chronology for the changed bytes. Stale or backdated produced\_at\_utc or mtime\_utc evidence is a blocker until the evidence family is regenerated with canonical tooling.  
* Evidence generators and proof harnesses MUST derive top-level PASS from the current decisive predicate checks for the evidence family. Format-only validation, regex-only digest validation, parsed-object equality when byte identity is the claim, or stale local state MUST NOT satisfy a PASS claim.  
* Evidence generators and proof harnesses MUST NOT serialize unexpected or unclassified behavior as PASS-grade evidence. If observed behavior deviates from expected success, expected failure, or an approved typed-error posture, the generator MUST fail closed or emit an approved non-PASS posture.  
* When generated evidence or acceptance-boundary artifacts rely on governance metadata, review MUST verify that the metadata is mechanically checked where practical. This includes epic ID, PF09 task or subtask ID, artifact kind, record type, token roster or allowed-token boundary, claim or nonclaim posture, source artifact identity, and any release or binding identity that controls the review conclusion.  
* Nonclaims that prevent overclaiming QA PASS, OPS completion, PF09 status movement, acceptance-token satisfaction, runtime conformance, public-surface expansion, or epic closeout SHOULD be asserted by tests, validators, generators, or acceptance-boundary artifacts when those nonclaims are decisive to the review. If machine checking is not practical, the review MUST state the limitation and preserve the nonclaim explicitly in the reviewed artifact.  
* Evidence claims MUST be scoped to exactly what the artifact proves. A nonclaim snapshot, field-sufficiency snapshot, contract snapshot, or parent-binding summary MUST NOT claim log/privacy/no-payload, runtime conformance, QA PASS, OPS completion, PF09 status movement, or closeout tokens unless the artifact family actually produces the required proof. If an artifact type cannot prove a token or claim, the generator, registration source, acceptance map, matrix, mirror row, and review text must preserve the nonclaim instead of letting the claim survive through names, labels, or inherited token arrays.  
* If a generated evidence family declares artifact roles, mirror roles, or equivalent role metadata, review MUST verify that the declared roles survive generation, registration, Human Evidence Index or Machine Mirror update, and path-proof refresh. Dropped, defaulted, or silently changed roles are evidence-identity defects when the role controls interpretation of the evidence family.  
* When an evidence update uses a fixed-point loop across generated artifacts, Human Evidence Index, Machine Mirror, hash sentinels, path proofs, aggregate evidence, or orientation evidence, the review MUST verify that the loop is bounded, rerunnable, and converged from the final generator logic. A fixed-point loop is not accepted merely because a downstream file exists; the final evidence pass must show coherent generated bytes, hashes, sizes, proof anchors, and companion proof surfaces.  
* When generated evidence asserts environment-specific behavior, attempt ordering, selection order, typed errors, provider posture, adapter posture, or comparable runtime facts, the generator MUST derive those facts from the actual observed run, snapshot, command output, or governed input for the intended environment. It MUST NOT substitute another environment posture, hardcode observed-order claims, or synthesize proof facts that were not produced by the governed run.  
* If a PR adds or modifies generated evidence that is later indexed, mirrored, aggregated, counted, or summarized, the review MUST verify that the generator and generator check ran before downstream updater, index, mirror, hash, path-proof, aggregate, or orientation checks that depend on those generated bytes.  
* Downstream index, mirror, hash, path-proof, aggregate, or orientation checks do not by themselves prove generated-evidence freshness when the generating command did not run in the final governed proof path.  
* If adding, removing, or changing indexed artifacts changes aggregate counts, orientation summaries, topology summaries, roster totals, or other derived inventory evidence, those derived artifacts and their companion proof surfaces MUST be refreshed in the same final evidence pass. Stale derived aggregate evidence is a blocker until the generated artifact, derived artifact, and governed companion proof surfaces are current and coherent.  
* When a PR or remediation discovers an unsupported token claim in governed evidence, review MUST verify that the unsupported token was removed at the source that generates the governed row, not merely hidden in a downstream report.  
* The review MUST also verify regenerated Human Evidence Index, Machine Mirror, hash sentinels, and path-proof transcripts as applicable, and must record the search or validation method used to confirm the unsupported token is absent from the source and generated evidence surfaces.  
* A PR may not be treated as remediated while the unsupported token remains claimable in any governed acceptance, index, mirror, manifest, QA log, OPS evidence, or closeout artifact.  
* When a QA check, proof harness, or generated acceptance artifact evaluates a roster of generated proof families, PASS requires explicit fail-closed visibility for every generated family in the claimed roster. If any generated family lacks explicit proof coverage, the result MUST remain TOOLING\_BLOCKED or another approved non-PASS posture until coverage is added, the family is explicitly handled as a non-claim, or the approved roster is changed.  
* When generator or proof-harness logic changes, any governed artifacts used to prove that logic MUST be regenerated from the final logic path before the review may treat them as acceptance evidence. Stale artifacts from earlier generator logic are not sufficient proof after remediation.  
* When remediation fixes a false-PASS evidence generator or proof harness, the review MUST state whether the fix includes a regression test or equivalent mechanically repeatable negative check for the old false-positive path. If no such check exists, record the gap as residual risk rather than silently treating the generator defect as hardened.  
* If a proof generator or evidence harness needs open rails, it MUST require explicit caller-provided open rails and MUST NOT silently force SAFE\_MODE=0, ALLOW\_NETWORK=1, or equivalent. The invocation used for the proof must make the rails posture explicit.  
* If emitted or summarized bytes depend on specific env fields beyond the standard deterministic pins, the generator or harness MUST pin or otherwise prove those env inputs explicitly. Missing byte-affecting env pins leave the proof nondeterministic and non-accepting.  
* When a remediation changes only evidence tooling, generators, or governed artifacts, the review MUST state explicitly whether any public contract, route family, or A7 scope changed. If none changed, say so plainly.  
* Existing governed evidence refreshed outside the direct PR slice MAY be treated as bounded evidence churn only when the review proves all of the following: the refresh was produced by the canonical updater or generator, the refreshed items remain in existing governed homes, companion index, mirror, checksum, and path-proof artifacts are coherent, and the review does not use that churn to claim unrelated PF09 closure, route work, writer work, public-contract change, or new acceptance scope.  
* When run evidence classifies outside-family proof-companion churn, the classification MUST name each refreshed family and, where Machine Mirror rows change, the affected artifact key and discovered physical path or other canonical row locator.  
* A PASS claim for bounded side-effect classification MUST fail closed if any classified side-effect path is missing, any proof companion does not validate against its target artifact, or any affected Machine Mirror row fails to match artifact key, proof anchor, sha256, or size\_bytes.  
* If a remediation is scoped as evidence-family closeout and the review shows that the underlying runtime, route, or transport slice was already correct, the review MUST say so explicitly and MUST NOT widen the remediation claim to reopened runtime, route, or writer work unless a real defect is shown.  
* The review MUST name the preserved slice and the exact evidence-family gap that remained open.  
* Same-change evidence-family closure is family-complete, not primary-family-only. If the remediation or canonical generator changes supplemental, legacy, or compatibility outputs that are still produced by the same governed flow, their companion path-proofs, mirror rows, and checksum or index companions MUST also be current in that same run.  
* A remediation MUST NOT be recommended as complete on the basis of a rerun claim while any changed still-produced governed companion remains stale. Subset freshness is insufficient; every changed governed output family that still participates in the slice must close as one coherent same-change whole.

### **Requirement Satisfaction Crosswalk (REQUIRED for remediation sequences)**

* Requirement: \<requirement label and short statement\>

* Status by attempt: \<Attempt 0: FAIL | Remediation 1: PARTIAL | Remediation 2: PASS\>

* Evidence pointer: \<where the requirement is proven\>

Repeat per requirement.

For remediation sequences, each requirement row SHOULD also record:

* Original or earlier blocking state: summarize the state before the successful remediation.

* Remediation change that addresses it: identify the later change that resolves the blocker.

* Current status after remediation: state whether the requirement is Satisfied, Not satisfied, or still mixed after the final attempt.

* Notes: record any earlier drift or intermediate change that was reversed and therefore does not remain in the final shipped state.

### **PF09 Impact & Status Posture (include when the PR review is used to support PF09 closeout)**

* PF09 task ID: record the exact task ID supported by the review.  
* PF09 subtask ID(s): record the exact subtask IDs supported by the review.  
* Affected PF canon home(s): name the exact PF document title or titles that a later drain would update.  
* Exact affected locator(s): record the exact row ID, subtask ID, section heading, anchor, or status-table row that the later drain would touch.  
* Current PF09 recorded status: quote the current task and subtask status lines from PF09.  
* Actual implemented state: state whether the mapped work is complete in substance, contributory only, or still incomplete.  
* Actual OPS state, if applicable: state whether required OPS work is complete in substance, contributory only, or still incomplete.  
* Actual governed evidence state: state whether governed evidence is sufficient, partial, or missing for the later-drain posture.  
* Supported later-drain action: state exactly one of change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended.  
* Drain readiness classification: state exactly one of Already drained into PF-Canon | Supportable from repo evidence only | Not yet supportable from repo evidence.  
* Epic-close expectation: state exactly one of drain at epic close | after an additional PR or OPS slice | after a separate canon-only drain step.  
* If the review supports a PF09 status move but the current PF09 row still shows the older state, quote that older state separately and keep it distinct from the supported later-drain action.  
* Review, retrospective, implementation, and closeout artifacts MUST NOT phrase a supportable status move as though the canon row has already been updated.  
* Why this status posture is supported: tie the supported later-drain action to the approved plan, the final remediated evidence, and the blocker or blockers that were resolved or remain open.  
* Evidence pointer(s): point to the governing plan and the final review evidence.  
* PF proof excerpt(s) when PF09 is relied on: quote the exact PF09 task and subtask status lines used for the posture.

### **Doc Deltas (PF-Canon only; ALWAYS INCLUDED)**

* Doc: \<PF doc title\>

* Section: \<section heading\>

* Delta summary: \<what should change\>

* Rationale: \<why the doc needs this change\>

* Evidence pointer: \<where the supporting evidence can be found\>

Repeat per delta.

Doc Delta Detection Workflow (required when PR review supports PF-canon change claims)

For each substantive doc delta or PF09 status action, include a CHG item with:

* change claim type: behavior or output | governed paths or artifact families | tokens, rails, or evidence posture | workflow steps | PF09 status-impact requirement | other  
* claim: one sentence describing the change or supported status posture  
* evidence pointer: where the supporting evidence can be found  
* canon basis: CANON ALIGNED | CANON SILENCE | CANON GAP | CANON CONFLICT | NOT ASSESSED  
* canon check gate: owning PF document title and exact section heading, row ID, or status-table locator checked  
* canon proof excerpt: short verbatim excerpt from the owning PF source used to decide the basis

If the CHG item supports a PF09 status action, include exact phased PF09 document title, task ID, subtask ID, current status line, supported status action, impacted PF09 task ID(s), impacted PF09 subtask ID(s), and linked finding IDs.

If canon basis is CANON GAP or CANON CONFLICT, do not silently convert the issue into implementation scope. Route it as a Doc Delta or PO adjudication item unless the approved task explicitly includes that work.

### **Evidence Print (REQUIRED; PASS PROOF)**

Doc Delta Detection Workflow (required when PR review supports PF-canon change claims)

For each substantive doc delta or PF09 status action, include a CHG item with:

* change claim type: behavior or output | governed paths or artifact families | tokens, rails, or evidence posture | workflow steps | PF09 status-impact requirement | other  
* claim: one sentence describing the change or supported status posture  
* evidence pointer: where the supporting evidence can be found  
* canon basis: CANON ALIGNED | CANON SILENCE | CANON GAP | CANON CONFLICT | NOT ASSESSED  
* canon check gate: owning PF document title and exact section heading, row ID, or status-table locator checked  
* canon proof excerpt: short verbatim excerpt from the owning PF source used to decide the basis

If the CHG item supports a PF09 status action, include exact phased PF09 document title, task ID, subtask ID, current status line, supported status action, impacted PF09 task ID(s), impacted PF09 subtask ID(s), and linked finding IDs.

If canon basis is CANON GAP or CANON CONFLICT, do not silently convert the issue into implementation scope. Route it as a Doc Delta or PO adjudication item unless the approved task explicitly includes that work.

A) Tokens satisfied (names-only; do not invent)

* \<TOKEN\_NAME\_1\>

* \<TOKEN\_NAME\_2\>

If no PASS tokens are claimed by name in this PR artifact, state: No PASS tokens claimed by name in this PR artifact.

When no PASS tokens are claimed by name, the review pack MUST:

* record the search method used to confirm that no token names are claimed in the PR artifact

* state that the PR is proved through concrete tests/checks and governed artifact evidence rather than through named token claims

* add an Acceptance coverage evidence subsection that groups the core requirement labels, the evidence pointers that prove satisfaction, and the key proof facts for the whole PR outcome

A1) Acceptance coverage evidence (required for remediation sequences; recommended whenever the review supports PF09 closeout even if tokens are claimed)

* Requirement label: state the core requirement or closure claim being proved.

* Evidence pointer(s): point to the exact diff, artifact, test, or review line that proves the requirement.

* Key proof facts: quote the minimal facts that show the requirement is satisfied in the final reviewed outcome.

* Final posture: state whether the requirement is Satisfied, Not satisfied, or Mixed in the final combined outcome.

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
  If no CI or test proof is present in the PR bundle, the review pack MUST state that verification was diff-only and record the search method used to look for pass indicators.  
* "Verified locally" statements MUST be paired with an evidence pointer to captured output (CI log URL or committed evidence artifact). For CLI help checks (example: `hdctl showcompat --help`), include an excerpt and pointer in the Evidence Print.

* Docs-only PRs that change docs MUST include a recorded docs-lint or markdown validation proof (CI log URL or committed evidence artifact). If such tooling does not exist, record the gap as a repo issue and treat it as a blocker or as an explicit closure override (with rationale).  
* Full-gate first pass is required. Before issuing the first approval decision on the artifact, apply the full active review gate set to the full artifact, not a partial subset.  
* After the first review on a given artifact line, do not introduce a new blocker from unchanged text unless the later blocker is caused by newly added or materially changed text, a newly supplied authoritative input changes the review basis, PF canon changed after the prior review, or a prior read failure or truncation prevented full visibility.  
* Any blocker or caveat raised against unchanged text MUST state the trigger that makes it newly raisable.

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

* List doc correctness risks, contradictions, missing evidence links, and any required follow-ups.  
* For each blocker or caveat, state review provenance using exactly one of Introduced by current revision, Previously raised and still unresolved, or Review Drift.  
* If a blocker or caveat is raised against unchanged text, state the trigger that makes it newly raisable. Otherwise state Not applicable.

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

### **Executive Summary**

* Scope statement: state whether the epic is hardening and completion work, contract expansion, or another posture, and name the boundaries that remained unchanged.

* Biggest wins: summarize the most important completed slices or proof improvements.

* Biggest remaining risks or gaps: list only the risks or gaps that still matter for closure or follow-up drainage.

  ### **Implementation Report (what happened in the repo)**

* If the epic reuses already-implemented scope, record that reuse explicitly as Step 0 or Approved reuse baseline and state that it is inherited scope rather than new implementation.

* For each PR or step, record:

  * Purpose

  * Key changes, high level

  * Key surfaces touched

  * Tests or evidence produced

  * Outcome

* Major surfaces affected: list the runtime, tooling, evidence, and documentation surfaces materially touched by the epic.

* Evidence inventory (what exists): list the concrete governed artifacts and where they live.

  ### **Evidence gaps (if any; label Unknown if you cannot verify)**

For each gap, record:

* Gap: state what is missing or not verified.  
* Status: use Unknown, Missing, or Ambiguous.  
* What would prove it: state the minimal test, proof, or artifact that would close the gap.  
* Where that proof should exist, if known: name the expected canon or governed artifact home.  
* If implementation PR evidence exists but close-pack, Live QA, PF-Canon drainage, or final aggregate validation is not directly proven, the snapshot MUST mark each missing proof as Missing, Unknown, Ambiguous, or No claim. PR-slice evidence MUST NOT imply formal close-pack proof, Live QA completion, PF-Canon drainage, or final aggregate validation unless those exact artifacts or results are directly proven.  
* Intended decomposition versus historical execution: a plan states intended decomposition only. Use PF10, PR metadata, and git or commit history to attribute what actually occurred; do not use plan text as historical execution proof.  
* Historical CI fact: before using review-success text as historical CI fact, reconcile it with run-level Actions data, including reruns. If the complete run or rerun history is unavailable or conflicts with the narrative record, label the result Unknown or Ambiguous and state the minimal evidence needed to resolve it.

  ### **Retrospective (Process)**

* What went well: process wins.

* What did not go well: process gaps, including evidence posture gaps.

* What we learned (Process): actionable changes to make next time.

  ### **Retrospective (Application/System) (optional)**

* What we learned about the system: technical insights.

* Known remaining risks or debt: explicit list.

  ### **Canon Alignment and Documentation Outcomes**

* Canon references used: list only the canon homes that materially informed the closeout analysis.  
* Source posture and inputs used: name the primary source of truth for what happened, state which plans or other artifacts were used only for intended scope or framing, and state explicitly whether PF20, PF23, or any non-PF artifacts were used.  
* When PF10 provides the primary epic-specific account of what happened but does not restate the original epic business case or the single consolidated PR or OPS sequence, the report MAY use the Epic Plan or Implementation Plan for those specific gaps only.  
* The report MUST say explicitly which facts are taken from PF10 and which facts are taken from plan artifacts as gap-filling inputs.  
* Plans used in this way are framing inputs only and MUST NOT override a live PF10 addendum on the same point.  
* When PF10 is silent on a docs-only repo-docs sweep, a retrospective or closeout artifact MAY use the docs PR artifact only for documentation-step history, docs file list, validation posture, repo-proof notes, and scope-boundary facts.  
* The artifact MUST label PF10 silence and MUST NOT use the docs PR artifact to prove implementation behavior, QA completion, close-pack completion, PF-canon drainage, acceptance-token satisfaction, or epic closure unless those stronger proofs are separately present.  
* Important limits: state any material limits in the current session or evidence set, especially when merged-PR proof, close-pack proof, or other closure-defining artifacts are missing.  
* Repo-proven versus formally closed posture: if the retrospective can support completion or status moves from repo evidence but cannot prove formal merge or close, say that distinction plainly rather than blurring it.  
* Later-drain PF-canon updates: when the artifact is intended to support a later PF-canon drain, name the exact affected PF canon home or homes, the exact affected locator or locators, the supported later-drain action, the drain readiness classification, the evidence basis, and whether the drain is expected at epic close, after an additional PR or OPS slice, or after a separate canon-only drain step.  
* Proposed addenda or live deltas: record any still-live canon deltas, their intended drain homes, and whether they are implementation work, documentation work, or unresolved analysis.  
* Uncertain drain targets: state None when there are none. Otherwise record the uncertainty explicitly.  
* Token and evidence semantics, if applicable: distinguish registry or semantics drift from binding or completeness drift, and state whether the issue is resolved, unresolved, or observational only.

### **Final QA Closeout Review \+ QA RCA (recommended)**

Use this review when closeout depends on synthesizing step-level QA outcomes, remediation history, and canon-alignment posture. It may live inside the close report or as a governed artifact referenced by it.

Minimum structure

* Artifact Map. Name the epic reviewed, the primary epic-specific source of truth, the canon homes used for closeout interpretation, and any framing inputs such as the Implementation Guide or QA Plan.

* Source-of-Truth Posture. State which artifact is primary for epic-specific events, which sources are framing only, and any internal mismatch that affects trust or traceability.  
* If a prompt label, artifact-map label, or non-PF input name conflicts with PF10, PF23, the Implementation Guide, the QA Plan, or another governing source used for closeout interpretation, the review MUST record the mismatch explicitly. The review MUST evaluate the epic under the governing source-of-truth identity and may preserve the supplied label only as provenance in the Artifact Map.  
* Closure Registers. When the review is used as a closure-oriented decision aid, include compact registers that separate:  
  * Deliverables register. Record each closure-critical deliverable, its source, the anchor quote or governing claim, and any exact evidence, path, or token strings that matter.

  * QA verification register. Record each QA step or verification item, its source, and the required evidence outputs or pass/fail posture.

  * Execution results register. Record the governing execution or remediation claims the review relies on and the outcome labels those claims carry.

  * Current-reality register. Record any repo-reality or surface-existence confirmations used to support closure, the relevant path or surface strings when they matter, and whether each confirmation supports, contradicts, or does not address closure.  
* Closure Trace Ledger. For each closure-critical deliverable or slice, map the deliverable to the QA verification item or items that validate it, the governing execution result or results that claim completion, whether current-reality confirmation was used, a status line (Satisfied | Not satisfied | Caveat), and a short why statement grounded in those inputs.

* Path and Surface Reality Ledger. When closure depends on named routes, entrypoints, governed ledgers, or close-pack files, list each required path or surface string verbatim, its source or sources, whether it is proven in current reality or only by execution record, whether it is required for closure, and a short note explaining its closure role.  
* Proof-Class Separation. When a closure claim relies on more than one proof class, the review MUST name each proof class and state which artifacts prove each class. Do not let public output proof, internal/admin compute proof, vendor-backed behavior proof, QA proof, OPS proof, PF09 drain proof, or close-pack proof imply another proof class unless the review names and proves the bridge.

* QA Closeout Summary. State the step-level QA outcome, the overall readiness recommendation, the main blocker or non-blocker themes, and the highest-impact closure risks or gaps that remain.  
* Closure-decision wording discipline. When a final QA closeout review, retrospective, closure evidence snapshot, ADR, or Lead decision aid uses SATISFIED, Satisfied, READY WITH CAVEATS, supportable to Done, or equivalent closure-oriented wording, it MUST state the exact decision axis covered by that wording.  
* Unless directly proven in the reviewed evidence, the artifact MUST mark the following as not performed, no claim, or not proven: PO closeout action, board update, merge provenance, formal OPS action, formal close-pack completion, PF-canon drainage, and final PF09 status update.  
* A closure-trace SATISFIED statement, readiness recommendation, or supportable-status statement is not by itself a PO closeout action, board update, merge provenance assertion, formal OPS completion, formal close-pack completion, or canon-drain completion.  
* Canonical RCA Requirement Basis. List the canon sections that justify the review method.  
* For each canonical basis item, include the PF document title and either a short proof excerpt or a precise evidence pointer showing why that source governs the review method.  
* Required elements checklist. Confirm the presence or absence of the D0 Discovery artifact, runtime functional proof when required, governed current-state QA evidence under the epic QA root, the QA RCA summary, Coverage vs QA Plan accounting, a readiness recommendation, indexed evidence, and the applicable venue posture.  
  * When the approved proof includes a venue-specific claim, confirm the required governed venue binding and treat absent, ambiguous, or contradictory venue proof according to the plan’s stated effect.  
  * When venue is not material, record `NOT CLAIMED`, `NOT APPLICABLE`, or `UNKNOWN - NON-MATERIAL`, as appropriate, and do not treat absent Codespaces provenance as an uncovered QA step or missing closeout element.  
  * Do not infer the execution venue from a provider name, repository path, current console session, devcontainer configuration, or artifact location.  
* The required elements checklist MUST end with a compliance statement that states Complete, Complete with caveats, Incomplete, or Not assessed. It MUST NOT say Complete when any required element is absent, ambiguous, or unsupported by governed evidence.  
* Step-cluster approval proof. When a final QA closeout review asks the reviewer to approve an executed Live QA step cluster, governed current-state QA evidence MUST be surfaced at cluster level, not only as a result summary. For every executed step cluster under review, the review MUST identify the manifest entry or entries, the manifest path-proof posture, the primary log or logs, primary-log path-proof binding, captured\_env posture, evidence\_artifacts posture, intended\_tokens posture, claimed\_tokens posture, and the result sidecar or other plan-defined decisive receipt.  
* A result JSON, PASS label, or summary sentence is not sufficient by itself for final closeout review when the step cluster is being used as current-state Live QA evidence. The closeout review must show the manifest, header, tokenless or token-claim posture, and path-proof surfaces that make the PASS auditable.  
* QA Timeline. Summarize the major remediation loops, ADR or audit events, and QA step outcomes in a stable chronology. If the governing source is append-only, the review MAY use source order as the canonical chronology and MUST say so explicitly.

* Coverage vs QA Plan. List every planned QA step in plan order, record whether it is Fully evidenced, Partially evidenced, or Not evidenced, note any material mismatch, and state the closeout impact for each step.  
* Coverage vs QA Plan MUST separately call out any accepted plan-execution deviation, even when the step is Fully evidenced and PASS. Examples include bounded Moon Loop reruns, rails changes, and step-local dependency-preflight corrections. Coverage status alone is not sufficient when accepted execution materially diverged from the approved plan.

* For each remediated step, Coverage vs QA Plan accounting MUST distinguish original planned receipts from accepted remediation receipts and identify the final accepted receipt or evidence basis. Failed or superseded receipts remain part of the record and MUST NOT be hidden, but they MUST NOT be treated as the governing PASS basis once an accepted remediation receipt is proven.  
* Findings. Record each substantive finding with what happened, why it matters, classification, PF touchpoints when needed, and evidence-pointer posture.

* Root Cause Analysis. State the primary root cause, contributing factors, what made the issue hard to detect or hard to close, and the role of any remediation loops in reducing or preserving uncertainty.  
* Remediation Loop Assessment. For each major remediation loop, rerun sequence, or ADR-backed correction path used in closeout, state whether it reduced uncertainty, corrected evidence or closure-posture drift, or only preserved a caveat, and explain why. Distinguish productive bounded remediation from churn  
* Evidence Hygiene Assessment. State which evidence families were strong, which remained risky, and whether each decisive proof depended on step logs, path-proof surfaces, validators, checksums, close-pack binding, or other governed evidence discipline. When a risk could recur in future epics, state the canon, planning, QA, or evidence-posture change that would prevent recurrence.

* Implementation Gaps and Proposed Fixes. For each remaining gap, state the symptom, the expected behavior, the likely locus, a high-level fix, and a verification hook.

* Doc Deltas. State whether PF06 has any delta from the review. If the correct home is another PF document, route the delta there and say why PF06 is not the correct home.

Guidance on evidence-light decision records

* If a guidance record, ADR set, or other closeout decision note is used but does not carry explicit evidence-pointer lines, the review MUST label it as evidence-light guidance.

* Evidence-light guidance MAY inform decision framing, but it MUST NOT be treated as stronger than the evidence-backed implementation, QA-pass, or close-pack records around it.

* When possible, the review SHOULD pair each evidence-light guidance item with the governing evidence-backed lines that make the decision auditable.

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

* OPS tasks are PO-authorized procedures. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent. OPS tasks MUST be enumerated as OPS-01, OPS-02, OPS-03 (continue as needed) (no mixed-task steps).

Each task MUST also declare its closure posture as exactly one of:

* CLOSURE-CLAIMING  
* NON-CLOSURE

A CLOSURE-CLAIMING task is one whose approved job is to bring one or more mapped PF09.x rows to Done, support a Done recommendation now, or perform final closure, final binding, final acceptance promotion, or equivalent closure work.

A NON-CLOSURE task is one whose approved job is bounded validation, blocker classification, sequencing correction, evidence-only work, repo-side wiring, contributory work, or another approved intermediate step that does not itself claim PF09 closure.

Approval and review of a NON-CLOSURE task MUST judge only the truthful completion of that approved task purpose. PF09 row closure is not a task-level approval gate for a NON-CLOSURE task.

Each task MUST declare its intent as exactly one of:

* DISCOVERY

* CHANGE

Cross-lane dependencies (locked line). If a task depends on outputs produced by a prior task in the other lane, the dependent task MUST include exactly one dependency line in this exact form:

Inputs needed from Task \<ID\> during implementation: \<exact items\>

Placeholders (for example TBD, to be determined, Sx) in this line are a mechanical blocker.

### **Execution-ready gate (normative)**

A remediation task plan submitted for approval MUST be execution-ready:

* every task has a syntax-normalized semantic contract that is executable by its assigned authorized actor; literal paste-and-run syntax is not a plan-approval test

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

OPS execution preflight and classification. Before any OPS task executes external, vendor-backed, privileged, or open-rails behavior, the producing plan or in-flight OPS evidence MUST prove the execution preflight that applies to that task: executable command, target facts, input shape, secret posture, rails posture, deterministic pins, prerequisite proof, PO authorization, and required env or credential presence where applicable. Missing command proof, unresolved placeholders, missing target facts, missing prerequisite proof, absent PO authorization, or uncaptured required env posture is TOOLING\_BLOCKED unless the approved task defines a narrower non-execution outcome.

OPS outcome labels. Use PASS only when the task preflight passes, the approved command or action runs, the captured outputs satisfy the task success criteria, no secret or identity contamination occurs, and the result summary preserves any non-claims that apply. Use FAIL\_BEHAVIOR only when prerequisites are proven and the observed behavior fails. Use FAIL\_TOOLING when the run or evidence is contaminated, unsafe, secret-bearing, identity-bearing when forbidden, guessed, missing required outputs after an attempted run, or otherwise invalid as a tool run. Use TOOLING\_BLOCKED when the task cannot safely run.

Post-failure command discipline. OPS commands, flags, targets, credentials, hostnames, ports, birth or user inputs, or evidence locations MUST NOT be changed after a failed run merely to force PASS. Any retry-changing fact MUST be canon-backed or approved in the task context, recorded in the result summary, and reflected in the produced evidence.

In-flight flexibility MUST NOT permit:

* changing governed artifact locations or filenames

* introducing new governed files without explicitly stating indexing/mirror intent

* indexing remediation-only diagnostics into governed indices/mirror

### **Mechanical blockers (auto-reject if present anywhere in the plan)**

* Any PR-xx task missing an embedded CodEx Prompt. A present prompt’s syntax-origin or paste-readiness defect is non-blocking and may be normalized during execution when the semantic contract is preserved.

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
* Task closure posture (CLOSURE-CLAIMING or NON-CLOSURE)  
* Owner/role  
* Depends on  
* Cross-lane dependency  
* Outputs

#### **Task Details (repeat per task)**

Task ID:

* Task name:  
* Task type (DEV or OPS):  
* Task intent (DISCOVERY or CHANGE):  
* Task closure posture (CLOSURE-CLAIMING or NON-CLOSURE):  
* Owner/role:  
* Preconditions:  
* Inputs:  
* Actions (what-not-how; execution detail may be developed in flight for OPS):  
* Outputs (required; concrete paths \+ filenames; lowercase directory names):  
* Verification (required; success criteria and what artifacts prove done):  
* Evidence capture (required for OPS): where commands/output/deviations are recorded (paths \+ filenames; lowercase directory names):

Include the dependency-line rule exactly once when cross-lane dependency exists.

