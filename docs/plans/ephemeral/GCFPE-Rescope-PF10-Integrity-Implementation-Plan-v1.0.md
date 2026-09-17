---
artifact_type: GCFPE_IMPLEMENTATION_PLAN
logical_id: GCFPE-RESCOPE-PF10-INTEGRITY-IMPLEMENTATION-PLAN
artifact_version: "1.0"
status: READY_FOR_PRODUCT_OWNER_REVIEW
created_date: 2026-09-13
execution_authority: NONE
source_release: GCFPE-20260912.2
source_prompt_version: 091226.3
candidate_release: TO_BE_ALLOCATED_DURING_IMPLEMENTATION
alpha_state: ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION
pfcanon_content_read_policy: MARKDOWN_ONLY
pfcanon_gdoc_docx_content_policy: PROHIBITED
runtime_artifact_root: Glow / Ephemeral Planning Files
runtime_artifact_root_url: https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc
plan_scope: GCFPE prompt ecosystem, active workflow controls, specialized PR-development skill, validation, promotion, and archive lineage
---

# GCFPE Rescope, PF10, and PR-Development Integrity Implementation Plan v1.0

## 1. Purpose

Create and validate a complete successor GCFPE release that repairs the Alpha rescope-loop failure without rewriting approved implementation plans, rerunning accepted PR work, discarding valid in-flight work, or expanding Product Owner responsibilities.

The repaired ecosystem must establish a controlled PR-to-IA-to-PF10-to-PR loop, add a dedicated approved-rescope continuation, add a Product Owner-only manual `Abort PR and Escalate` entry point, enforce PFCanon Markdown-only source access, preserve smart PR publication behavior, and prevent the metaprompt, skills, policies, or validators from regenerating the rejected architecture.

This plan does not authorize prompt publication, skill mutation, PF10 drainage, repository work, PR merge, candidate promotion, or Alpha resumption.

## 2. Controlling requirements

### 2.1 PF10 and approved-artifact lifecycle

1. The buck stops at PF10 for in-flight changes to approved plans, guides, specifications, scope, and escalation decisions.
2. An approved implementation plan remains the authoritative base plan.
3. An applicable active PF10 addendum overlays the base plan only for the scope it explicitly addresses.
4. An in-flight approved change must not automatically create a replacement whole-change Plan, replacement detailed PR Plan, replacement PR Instruction, another Plan approval, or another Product Owner Proceed.
5. An accepted PR must never be rerun, re-authored, reopened, or re-planned to prove its already accepted scope.
6. Existing valid work in an open PR, branch, commit, workspace, or artifact remains preserved and is reused after an approved addendum becomes active.
7. Any prompt that approves a rescope, escalation, remediation, or material change to an approved plan must emit a separate standalone `PF10_BUILD_NOTES_ADDENDUM` Markdown artifact.
8. Addendum authoring does not edit PF10 or make the addendum canonical. Nathan, as Product Owner, manually drains or inserts the approved addendum into PF10.
9. Once the approved addendum is actually inserted into PF10, it becomes the authoritative in-flight overlay and may support resumption through the dedicated continuation prompt.
10. Normal rescope approval must not add a second Product Owner merits decision called “manual PF10 disposition.” The Product Owner action is publication/drainage and prompt relay.

### 2.2 Rescope loop

The successor graph must implement this semantic route:

1. PR implementation identifies a substantiated material boundary.
2. The PR session preserves all valid work and emits one formal rescope request through the selected request-authoring boundary.
3. The same whole-change IA approves, denies, or redlines the bounded request.
4. Approval emits a standalone PF10 Build Notes addendum for Product Owner manual drainage.
5. After actual PF10 insertion, a dedicated “approved rescope, proceed with implementation” prompt returns the addendum to the same PR-development session.
6. The same PR workspace, branch, open PR, accepted dependencies, approved base Plan, detailed PR Plan, PR Instruction, and original Proceed remain in force except where the active addendum explicitly modifies the scope.
7. A denial or redline may enter a bounded revision loop. It must not silently create an endless retry loop or a whole-plan restart.

The implementation must establish exactly one formal rescope-request authoring boundary. It may retain RS-10 for this function or place the complete request directly in PR-30, but it must not create two redundant mandatory request stages.

### 2.3 Product Owner-only abort entry

1. Create a dedicated manual prompt with the working title `Abort PR and Escalate`.
2. Only Nathan, as Product Owner, may invoke it.
3. No PR, RS, IA, QA, ESC, management prompt, skill, validator, or automated workflow may invoke it, select it, or route into it automatically.
4. A worker session may preserve evidence and return control to the Product Owner when rescope cannot rescue the PR. It must not characterize that return as an abort decision.
5. The manual invocation itself starts the abort/escalation process for the exact PR and work unit named by the Product Owner.
6. The prompt must preserve the repository workspace, branch, commits, PR, review evidence, CI evidence, rescope attempts, and approved unaffected work. It must not delete, reset, merge, or discard them.
7. The prompt must create a complete abort/escalation evidence package and route it to the correct substantive escalation owner under the selected workflow.
8. If the abort/escalation process approves a scope, plan, guide, specification, or escalation decision, the approving prompt emits the required standalone PF10 addendum.
9. The final stable prompt ID and family placement must be allocated during the controlled candidate inventory. The working title is not publication evidence.

### 2.4 PFCanon Markdown-only access

1. Agents may read only the canonical Markdown versions of PFCanon files.
2. Agents must never open, fetch, inspect, cite as authority, or use a Google Docs, DOC, or DOCX version of a PFCanon file.
3. There is no Google Docs or DOCX fallback. A missing or inaccessible Markdown source is a source blocker.
4. Active prompts, skills, procedures, handoffs, hubs, catalogs, validators, and examples must reference PFCanon Markdown sources only.
5. PFCanon handoff references must use the actual Drive link for the Markdown file, never an opaque Library ID.
6. Source discovery must be constrained to Markdown candidates before content retrieval. A non-Markdown PFCanon candidate must not be opened to determine whether it is equivalent.
7. Every PFCanon read must record the Markdown filename, direct Drive link, observed version or identity, and content digest when available.
8. Historical records containing obsolete Google Docs or DOCX references remain historical evidence only. They must not be executed as runtime source routes, and the active control layer must explicitly direct agents to the current Markdown source instead.

### 2.5 PR-development behavior

1. `glow-hde-pr-development` remains the primary PR-30 skill.
2. `glow-hde-devops` remains support-only for bounded environment, Railway, vendor, database, deployment, or operational capabilities.
3. A fresh or recovered PR session must inspect existing workspaces, worktrees, branches, commits, PRs, and Drive artifacts before creating work.
4. It must reuse the most advanced consistent existing state and must not invent a session-inspection endpoint or unsupported platform limitation.
5. Local testing precedes meaningful commits and pushes.
6. Commits and pushes must be purposeful and reviewable: neither no publication nor constant micro-commits and pushes.
7. An early draft PR is allowed after a coherent, locally tested checkpoint.
8. Open substantive review findings take priority over paid CI. The session must not wait for or retrigger CI on a revision already known to require correction.
9. When supported and authorized, stale CI for a known-defective revision may be cancelled. Otherwise it is marked stale while local remediation continues.
10. The corrected candidate is locally tested, committed coherently, and pushed deliberately before fresh review and current-head CI.
11. PR-30 continues until required review findings are resolved, required current-head CI passes or an actual scoped waiver exists, mergeability is verified, and the PR is genuinely ready for Product Owner manual merge.
12. PR-30 never merges without a direct, PR-specific Product Owner instruction.

### 2.6 Direct handoffs and artifact storage

1. All runtime planning files and off-repository artifacts are efficient, machine-readable Markdown under `Glow / Ephemeral Planning Files`.
2. The producer uploads the complete file, reads it back, and returns the actual Drive link.
3. Opaque ChatGPT Library identifiers are prohibited as runtime artifact references.
4. Every nonterminal continuation contains exactly one fenced, plain-text, copy-paste-ready prompt.
5. The handoff names the exact selected destination prompt, version, and direct Notion link; receiving role/session; change and work-unit identifiers; required Drive artifacts; current status; decisions; constraints; unresolved items; next action; and expected output.
6. A metadata list, blank template, title-only destination, or saved-artifact-only reference is not an acceptable handoff.

## 3. Protected state and non-goals

The implementation must preserve these boundaries throughout candidate development:

- The current selected GCFPE release remains active until a complete successor passes validation and is explicitly promoted.
- HDE-EPIC040 remains `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION`.
- PR #403 / PR01 remains accepted and must never be rerun or re-authored.
- PR #404 / PR02 remains open, draft, unmerged, and preserved at its current verified lineage until separate Alpha resumption authority exists.
- The rejected RS-20 review and rejected PF10 addendum remain non-operative historical evidence.
- No repository mutation, PR merge, CI run, PFCanon edit, PF10 insertion, or Alpha resumption is part of this GCFPE candidate implementation.
- The immutable R1 baseline and Flowmaster Primary core are not rewritten by default.
- Model, strength, reasoning-level, eligibility, suitability, account-availability, capability-assessment, or Analyzer routing must not be reintroduced.

## 4. Target workflow graph

| From | Condition | Required destination or result | Prohibited destination or result |
| --- | --- | --- | --- |
| PR-30 | Material boundary proved | Formal bounded rescope request with preserved work and one pasteable handoff | Whole-plan rewrite, new PR, discarded workspace, automatic abort |
| Rescope request | Complete and bounded | Same whole-change IA rescope decision | Product Owner analysis, generic QA escalation |
| IA rescope decision | APPROVE | Rescope decision plus standalone PF10 addendum | IA-30/IA-40 whole-plan restart, new Proceed |
| IA rescope decision | DENY or REDLINE | Bounded revision or Product Owner return when no safe revision remains | Infinite retry, automatic abort |
| Product Owner | Manually drains approved addendum | PF10 Markdown contains the active addendum | Agent PF10 edit, second merits decision |
| Approved-rescope continuation | Active addendum verified in PF10 Markdown | Same PR session and preserved implementation vehicle | Replacement Plan, Instruction, Proceed, PR, or session |
| Product Owner | Manually invokes `Abort PR and Escalate` | Abort/escalation process begins for exact PR/work unit | Invocation or routing by any agent or automation |

## 5. Component impact inventory

### 5.1 Confirmed prompt targets

| Component | Required change |
| --- | --- |
| RS-10 | Retain only if it is the single formal rescope-request author; require complete evidence, preserved PR lineage, PF10 Markdown references, and direct IA handoff. |
| RS-20 | Remove the rejected manual-disposition gate and IA-30/IA-40 restart. Make the same IA the bounded approve/deny/redline authority. On approval, emit the standalone PF10 addendum and return to the Product Owner for manual drainage. |
| RS-30 | Preserve bounded redline revision. Add a defined Product Owner return when the request cannot be responsibly repaired; never auto-invoke abort. |
| New approved-rescope continuation | Create a dedicated prompt that verifies actual insertion in PF10 Markdown and resumes the same PR session against the approved base plus active addendum. Working function: `Approved Rescope — Resume PR Implementation`. |
| New PO-only manual abort prompt | Create `Abort PR and Escalate` as a manual-only entry point. Prevent every automated or agent-originated invocation. |
| PR-30 | Replace normal Plan/instruction re-entry and new-Proceed language with the PF10 rescope loop. Preserve recovery, local testing, smart publication, review-first CI, merge readiness, and manual merge boundaries. |
| PR-20 | Cross-reference the detailed PR Plan against applicable PF10 Markdown addenda; distinguish approved base content from active overlays. |
| IA-10 and IA-20 | Cross-reference plan creation against applicable PF10 Markdown sources and record the plan-time applicability snapshot. Do not weave later in-flight addenda into an untracked base rewrite. |
| IA-30 and IA-40 | Guard initial Plan review/revision from in-flight PF10 rescope. An approved base plus applicable active addendum must not automatically enter a successor Plan loop. |
| QA-50, QA-60, and QA-80 | Apply PF10-first plan/overlay discipline and prevent approved-plan re-authoring during QA or remediation. |
| QA-70, RS-20, ESC-40, and every other qualifying approval prompt | Apply the semantic PF10-addendum producer rule. Do not rely only on a static producer-name allow-list. |
| ESC-30 and ESC-40 | Accept correctly authorized PR-originated escalation evidence without treating QA-only ESC-10 as the PR entry. Preserve PF10 addendum production for approved material changes. |
| GCFPE-MGMT-10 | Replace the generic late material Plan-rewrite route with PF10-first lifecycle rules, the dedicated resume function, and the PO-only abort boundary. |
| PE Metaprompt | Add non-reintroduction rules for approved-artifact immutability, PF10 overlays, Markdown-only PFCanon access, PO-only abort, direct handoffs, and specialized PR-skill ownership. |

### 5.2 Required complete catalog scan

Do not limit the repair to the confirmed pages above. From the complete selected catalog, identify every prompt whose inputs, outputs, examples, fallback logic, handoffs, or cross-references involve any of these concepts:

- implementation Plan, detailed PR Plan, QA Plan, remediation Plan, guide, or specification creation or revision;
- PF10 read, addendum authoring, publication, drainage, status, or precedence;
- rescope, escalation, abort, plan correction, post-approval correction, or re-entry;
- PR workspace recovery, commit, push, review, CI, merge readiness, or manual merge;
- PFCanon source retrieval or file-format selection;
- Library IDs, Google Docs links, DOC/DOCX references, or conversation reconstruction;
- handoff creation, terminal completion, or Product Owner return.

Record each matched prompt, the exact defect or confirmed no-change result, required correction, new version, direct Notion link, and validation result. Preserve prompts that already comply.

## 6. Skill and enforced-control workstream

### 6.1 `glow-hde-pr-development`

Revise the specialization and its behavior cases together.

Required skill changes:

- Replace the current post-rescope language that follows unspecified downstream prerequisites with the explicit PF10 Markdown verification and same-PR continuation contract.
- Add an `Approved rescope continuation` behavior case covering workspace recovery, active PF10 Markdown addendum verification, preservation of the original Proceed, and return to the same PR lifecycle.
- Add a `Rescope cannot rescue PR` behavior case that returns evidence and control to Nathan without invoking or routing to `Abort PR and Escalate`.
- Add a `Product Owner manually invoked abort` behavior case that executes only after direct manual invocation and preserves all evidence and repository state.
- Add a negative case proving that an agent-authored abort handoff, automatic abort transition, or QA-only escalation substitution fails validation.
- Add PFCanon Markdown-only positive and Google Docs/DOCX negative cases.
- Preserve existing recovery, local-test-first, coherent commit/push, review-before-stale-CI, current-head CI, merge-readiness, and no-merge behavior.
- Keep `glow-hde-devops` support-only.

Validation command after modification:

```text
python3 scripts/validate_glow_hde_pr_development.py
```

### 6.2 `change-flow`

Revise only the Change-specific specialization and current overlay unless evidence proves a separately authorized Primary or R1 change is unavoidable.

Required changes:

- Replace GCF-17.RESCOPE wording with the explicit IA approval → standalone PF10 addendum → Product Owner manual drainage → dedicated same-PR continuation loop.
- Remove the statement that every material plan change invalidates Proceed and returns through normal planning. Replace it with a distinction between initial/unapproved Plan revision and an approved in-flight change governed through PF10.
- Add the Product Owner-only manual abort entry and prohibit automatic inbound edges.
- Require Markdown-only PFCanon reads everywhere the specialization resolves PF10 or another PFCanon source.
- Replace the static PF10 producer assumption with a semantic qualifying-approval rule plus an enumerated current candidate producer map.
- Preserve the Primary core byte-for-byte and preserve the immutable R1 baseline unless a separate explicit authority decision changes either.
- Update `references/gcfpe-current-direct-handoff-contract.json` to the successor release and repaired graph only after prompt membership is complete.

If the new current overlay cannot validate without changing the immutable R1 oracle, stop and report the exact semantic conflict. Do not silently revise the oracle or Primary core.

### 6.3 `flowmaster-validate`

Revise the GCFPE current-release validation boundary, current direct-handoff checks, and fixtures so that passing historical declarations cannot bless the old route.

Add deterministic rules for:

- no RS-20 approval edge to IA-30 or IA-40 for an approved in-flight PF10 change;
- exactly one selected approved-rescope continuation with a resolvable Notion destination;
- continuation to the same PR session, workspace, branch, PR, approved base, and original Proceed;
- no automatic edge to `Abort PR and Escalate`;
- successful abort entry only when the input explicitly records direct Product Owner manual invocation;
- semantic PF10 addendum production on every qualifying approval outcome;
- plan/guide/specification PF10 cross-reference and base-plus-overlay representation;
- PFCanon Markdown-only sources and negative rejection of active Google Docs, DOC, and DOCX routes;
- Drive Markdown artifact storage and no Library IDs;
- preservation of specialized PR-skill ownership and remote-action-cost controls;
- archived predecessors preserved intact after promotion;
- HDE-EPIC040 Alpha hold preserved until explicit resumption.

The validator remains read-only and must not run Alpha or mutate live controls.

## 7. Operating controls and release surfaces

Create versioned successors for every affected active control. At minimum:

- GCFPE Direct-Handoff and Runtime Artifact Operating Procedure;
- selected catalog;
- membership and release register;
- Glow HDE Prompt Flow Index;
- relevant HDE Change Flow, IA, QA, Escalation, and Technical Writing hubs;
- GCFPE Alpha Establishment and Change Management Checklist;
- GCFPE-MGMT-10;
- PE Metaprompt;
- current direct-handoff contract in the installed Change Flow specialization;
- specialized PR-development skill and behavior cases;
- Flowmaster/GCFPE validators and fixtures;
- HDE-EPIC040 Alpha record.

Required operating-procedure changes:

1. Separate approval, addendum authoring, Product Owner drainage, and post-drain continuation as distinct facts.
2. Define the addendum as noncanonical until manual drainage and authoritative once present in PF10 Markdown.
3. Remove the obsolete “manual PF10 disposition” merits gate.
4. Define the PO-only abort invocation and forbid automatic routing.
5. Enforce PFCanon Markdown-only retrieval with no fallback.
6. Replace fixed producer counts with semantic qualifying-outcome validation while still enumerating the candidate release’s expected producers.
7. Preserve direct handoffs, Drive Markdown artifacts, no Library IDs, no Analyzer/model assessment, and archive-not-delete behavior.

Required Alpha-log correction:

- preserve the current stop record;
- mark the older `READY FOR MANUAL RS-20 INVOCATION` instruction as superseded historical evidence;
- record that no current RS-20 output authorizes resumption;
- identify the successor GCFPE promotion and explicit Product Owner Alpha-resumption instruction as separate prerequisites;
- preserve PR #403 finality and PR #404’s open/draft work;
- identify obsolete Google Docs/DOCX PFCanon references as non-operative historical references and route current work only to PFCanon Markdown.

## 8. Implementation phases

### Phase 0 — Freeze, snapshot, and source preflight

**Goal:** Establish the exact current selected state without modifying it.

Tasks:

1. Resolve the selected release, catalog, register, manager, metaprompt, procedures, hubs, current skills, validators, and Alpha record.
2. Export or capture complete read-only bodies and content hashes for comparison.
3. Resolve every required PFCanon source by its canonical Markdown file only.
4. Build a source register containing exact Markdown filenames, Drive links, versions/identities, and digests.
5. Fail closed if any required PFCanon Markdown source is missing, ambiguous, or inaccessible. Do not inspect a Google Docs or DOCX alternative.
6. Record the immutable predecessor set and archive destination.

**Exit criteria:** Complete source register, complete component inventory, no production mutation, and all decisive PFCanon inputs proven Markdown.

### Phase 1 — Effective contract and graph specification

**Goal:** Freeze the intended successor semantics before prompt authoring.

Tasks:

1. Write a machine-readable graph contract for the repaired rescope loop.
2. Define the single formal rescope-request authoring boundary.
3. Allocate the stable ID for the approved-rescope continuation.
4. Allocate the stable ID for the PO-only `Abort PR and Escalate` prompt.
5. Define the PF10 addendum qualifying-outcome predicate and required artifact fields.
6. Define the PFCanon Markdown-only source predicate.
7. Define initial Plan revision versus approved in-flight PF10 overlay behavior.
8. Define Product Owner returns and terminal states so no workflow route can manufacture an abort decision.

**Exit criteria:** Closed graph with no orphan outputs, duplicate producers, automatic abort edges, whole-plan restart edges, or unproduced required inputs.

### Phase 2 — Prompt candidate authoring

**Goal:** Create complete sibling prompt candidates without changing the selected release.

Tasks:

1. Author the repaired RS, PR, IA, QA, ESC, management, and metaprompt pages identified in §5.
2. Author the new approved-rescope continuation prompt.
3. Author the new PO-only `Abort PR and Escalate` prompt.
4. Apply PF10-first cross-references to every matched Plan, guide, and specification creator or reviser.
5. Apply the semantic PF10 addendum output contract to every qualifying approval outcome.
6. Replace every affected handoff with one fully populated copy-paste-ready block.
7. Remove active PFCanon Google Docs/DOCX references, Library IDs, Analyzer/model assessment language, obsolete restarts, and invented platform endpoints.
8. Record each candidate as a sibling with explicit predecessor identity. Do not overwrite or archive the selected predecessor yet.

**Exit criteria:** Complete candidate prompt set, complete change register, all internal destinations resolvable inside the candidate set, and predecessor pages untouched.

### Phase 3 — Skill and contract implementation

**Goal:** Align the execution layer with the candidate prompt graph.

Tasks:

1. Revise `glow-hde-pr-development`, its behavior cases, and its validator.
2. Revise the Change-specific `change-flow` specialization and direct-handoff contract.
3. Revise `flowmaster-validate` current-release checks and GCFPE fixtures.
4. Preserve Primary core byte identity and record `PRIMARY_CHANGE_REQUIRED = false` if proven.
5. Commit skill changes through the governed skill-update workflow only after local validators pass.

**Exit criteria:** Skills and candidate prompts express the same actors, states, artifacts, edges, manual controls, storage rules, and prohibitions.

### Phase 4 — Procedure, hub, register, and Alpha-control candidates

**Goal:** Remove external active controls that could restore the rejected route.

Tasks:

1. Create the operating-procedure successor.
2. Update candidate catalog, register entry, flow index, hubs, and checklist.
3. Update the Alpha record with explicit supersession of the stale RS-20 invocation while preserving historical evidence.
4. Bind candidate release identity consistently across Notion controls and installed contract metadata.
5. Keep the candidate unselected and production predecessor selected.

**Exit criteria:** No active candidate control points to the old restart, non-Markdown PFCanon source, automatic abort path, generic DevOps ownership, or metadata-only handoff.

### Phase 5 — Deterministic validation

**Goal:** Prove structural and semantic consistency before live promotion review.

Run at minimum:

```text
python3 scripts/validate_glow_hde_pr_development.py
python3 scripts/validate_flowmaster.py --strict-warnings
python3 scripts/validate_flowmaster.py --target change-flow --target flowmaster-validate
python3 scripts/run_change_flow_fixtures.py
python3 scripts/validate_gcfpe_current.py
python3 scripts/run_gcfpe_current_fixtures.py
```

Add candidate fixtures before expecting these commands to pass. A historical pass does not validate the successor.

**Exit criteria:** Full suite pass; 46/46 immutable Change rows where still applicable; zero errors, warnings, or advisories; all new positive and negative fixtures behave as expected; Primary byte identity proven unchanged or separately authorized.

### Phase 6 — Live candidate readback and graph audit

**Goal:** Validate what is actually staged, not merely local declarations.

Tasks:

1. Read back every complete candidate prompt and control page.
2. Verify exact title, version, stable ID, Notion URL, predecessor, and lifecycle state.
3. Verify every handoff destination resolves to the intended candidate prompt.
4. Verify all required Drive Markdown artifacts and PFCanon Markdown references resolve.
5. Verify no active candidate body instructs an agent to open PFCanon Google Docs/DOCX content.
6. Verify no active candidate route requires Library IDs or conversation reconstruction.
7. Replay the HDE-EPIC040 PR02 rescope case as a non-mutating fixture against the preserved facts.
8. Test the PO-only abort entry separately; prove the ordinary graph cannot reach it.
9. Confirm the selected production release and Alpha state remain unchanged during validation.

**Exit criteria:** Complete live readback pass, closed candidate graph, and explicit validation report with every finding resolved.

### Phase 7 — Product Owner promotion decision and archival

**Goal:** Promote only the complete validated successor.

Tasks after explicit Product Owner approval:

1. Select the complete successor release atomically across register, catalog, manager, index, hubs, procedure, skills, and validation contract.
2. Read back every changed selection binding.
3. Archive superseded prompt and control versions intact in the existing archive locations.
4. Never delete, overwrite, or rewrite historical pages or evidence.
5. Record exact archive receipts and successor/predecessor lineage.
6. Run post-promotion deterministic and live readback validation again.

**Exit criteria:** One selected complete successor; all selected components agree; predecessor versions archived intact; post-promotion validation passes.

### Phase 8 — Alpha readiness handoff

**Goal:** Prepare, but do not execute, the safe return to HDE-EPIC040 Alpha.

Tasks:

1. Produce a concise promotion report and explicit Alpha-readiness result.
2. Produce the exact manual PF10 drainage package required for the approved PR02 rescope only after the repaired IA route produces a valid new addendum.
3. After Nathan drains the addendum into PF10 Markdown, produce the complete manual invocation for the approved-rescope continuation.
4. Verify the continuation targets the same PR02 session/workspace, PR #404, approved base artifacts, original Proceed, current repository lineage, and active PF10 Markdown addendum.
5. Do not resume Alpha until Nathan explicitly invokes the continuation.

**Exit criteria:** `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`; no Alpha work executed.

## 9. Required fixture matrix

| Fixture ID | Scenario | Required result |
| --- | --- | --- |
| RS-POS-01 | PR proves material boundary | Complete formal rescope request; valid work preserved; no automatic abort. |
| RS-POS-02 | IA approves bounded rescope | Standalone PF10 addendum emitted; return to PO drainage; no IA-30/IA-40 restart. |
| RS-POS-03 | PF10 Markdown contains drained addendum | Dedicated continuation resumes same PR session and original Proceed. |
| RS-POS-04 | IA redlines repairable rescope | Bounded revision returns to same IA. |
| RS-NEG-01 | Approved rescope attempts new Plan or Proceed | Validation failure. |
| RS-NEG-02 | Accepted PR is included in rerun scope | Validation failure. |
| ABORT-POS-01 | Nathan directly invokes exact abort prompt | Abort/escalation process begins with preserved evidence. |
| ABORT-NEG-01 | PR or RS prompt routes automatically to abort | Validation failure. |
| ABORT-NEG-02 | Agent claims abort decision without PO invocation | Validation failure. |
| PF10-POS-01 | Qualifying approval outcome | Separate Drive Markdown addendum with complete approved delta and manual-drain status. |
| PF10-NEG-01 | Proposal, denial, pending, or unchanged outcome | No empty or fabricated addendum. |
| PFCANON-POS-01 | Exact canonical Markdown source available | Content read allowed and provenance recorded. |
| PFCANON-NEG-01 | Only Google Docs/DOCX alternative found | Stop as source blocker; do not open fallback. |
| PFCANON-NEG-02 | Active handoff contains PFCanon Docs/DOCX route | Validation failure. |
| PR-POS-01 | Interrupted session has existing workspace | Recover and continue verified matching work. |
| PR-POS-02 | Open reviews and active CI | Fix reviews locally before spending another CI run. |
| PR-POS-03 | Coherent locally tested checkpoint | Purposeful commit/push and optional early draft PR accepted. |
| PR-NEG-01 | Micro-push or speculative CI loop | Validation failure. |
| PR-NEG-02 | Implementation stops before commit/PR/review/CI despite in-scope authority | Validation failure. |
| HANDOFF-POS-01 | Any nonterminal branch | One exact pasteable prompt with Notion and Drive links plus full continuity. |
| HANDOFF-NEG-01 | Metadata list or Library ID | Validation failure. |
| META-NEG-01 | Metaprompt regenerates old restart, non-Markdown PFCanon route, auto-abort, or Analyzer | Validation failure. |

## 10. Acceptance criteria

The iteration is ready for promotion only when all of the following are proven:

1. The selected candidate defines one closed PR → IA → PF10 addendum → Product Owner drainage → same-PR continuation loop.
2. RS-20 no longer routes an approved in-flight change through IA-30/IA-40 whole-plan re-authoring.
3. No in-flight PF10 change automatically requires a replacement Plan, Instruction, detailed Plan, Proceed, PR, session, or accepted-PR rerun.
4. The dedicated approved-rescope continuation exists, is selected, has a direct Notion URL, and preserves the original implementation vehicle.
5. `Abort PR and Escalate` exists as a Product Owner-only manual invocation and has no automatic inbound workflow edge.
6. Every qualifying approval emits one standalone PF10 Build Notes addendum; nonqualifying outcomes do not.
7. Every Plan, guide, and specification creator or reviser cross-references applicable PF10 Markdown and preserves base-plus-overlay lineage.
8. No active prompt, skill, control, example, fixture, or handoff opens or relies on PFCanon Google Docs, DOC, or DOCX content.
9. Missing PFCanon Markdown fails closed without fallback.
10. `glow-hde-pr-development` is the verified PR-30 primary skill; `glow-hde-devops` is support-only.
11. PR recovery, local-test-first publication, purposeful commit/push behavior, review-before-stale-CI behavior, current-head CI, merge readiness, and manual merge boundaries pass validation.
12. All runtime artifacts are machine-readable Markdown in `Glow / Ephemeral Planning Files` and are handed off by direct Drive link.
13. Every nonterminal handoff is one complete copy-paste-ready prompt with the correct selected destination.
14. No active model/strength/reasoning assessment, Analyzer, or configuration-based workflow gate is reintroduced.
15. The PE Metaprompt cannot regenerate any repaired defect.
16. The predecessor release remains active until promotion and is archived intact only after successful successor selection.
17. Deterministic validation, complete live readback, graph resolution, and post-promotion validation all pass with no unresolved mandatory finding.
18. HDE-EPIC040 remains stopped until a separate explicit Product Owner resumption invocation.

## 11. Product Owner control points

The implementation must preserve these actions as Nathan-only manual controls:

- approve or reject this implementation plan;
- authorize implementation of the GCFPE candidate;
- approve production promotion;
- manually drain approved PF10 addenda;
- manually invoke `Abort PR and Escalate`;
- manually invoke the approved-rescope continuation after PF10 Markdown contains the addendum;
- manually merge an identified PR;
- explicitly resume HDE-EPIC040 Alpha.

Agents perform source resolution, analysis, candidate authoring, validation, addendum authoring, artifact storage, handoff creation, and ordinary authorized workflow work. They must not inflate Product Owner work beyond the manual controls above.

## 12. Deliverables

The completed iteration must produce:

1. successor GCFPE prompt catalog and complete member register;
2. repaired RS, PR, IA, QA, ESC, management, and metaprompt candidates;
3. one dedicated approved-rescope continuation prompt;
4. one Product Owner-only manual `Abort PR and Escalate` prompt;
5. revised `glow-hde-pr-development` skill, behavior cases, and validator;
6. revised Change-specific `change-flow` specialization and current direct-handoff contract;
7. revised `flowmaster-validate` current-release checks and GCFPE fixtures;
8. revised operating procedure, hubs, Flow Index, checklist, and Alpha record;
9. PFCanon Markdown-only source register and validation results;
10. prompt-by-prompt finding and correction register;
11. deterministic validation report;
12. live readback and handoff-resolution report;
13. promotion report and archive receipts;
14. post-promotion validation report;
15. Product Owner Alpha-readiness handoff without Alpha execution.

## 13. Source register

| Source | Use in this plan |
| --- | --- |
| `HDE-EPIC040-alpha-rs20-escalation-planning-failure-rca-v1.0.md` | Primary failure evidence and preserved Alpha state. |
| Current selected GCFPE catalog | Source release membership and exact active prompt identities. |
| GCFPE Membership and Release Register | Selected-release and predecessor/successor authority. |
| GCFPE-MGMT-10 | Current management behavior and repair target. |
| PE Metaprompt | Prompt-generation non-reintroduction boundary. |
| GCFPE Direct-Handoff and Runtime Artifact Operating Procedure | Active artifact, handoff, PF10, and archive policy target. |
| `change-flow` specialization | Active workflow overlay and actor/session boundary target. |
| `glow-hde-pr-development` | Specialized PR-30 execution and recovery target. |
| `flowmaster-validate` | Deterministic validation and fixture target. |
| PFCanon Markdown files in `Glow / Core Docs / PFCanon` | Exclusive canonical content sources. Google Docs and DOCX versions are prohibited. |

## 14. Final plan status

`READY_FOR_PRODUCT_OWNER_REVIEW`

No implementation, publication, promotion, archive move, PF10 drainage, repository action, or Alpha resumption has been performed by this plan.
