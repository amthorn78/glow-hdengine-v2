> **SUPERSEDED — HISTORICAL RECORD, NOT BINDING.** General Prompt Flow and Creation Guidelines v1.12.1 (2026-09-09), imported from Google Drive `Glow / Ops` (file ID `1lFtlm1kVcrgDyxZV7E7KYuOwKiZ1rWR-`) on 2026-09-27. It predates the current release, decision D7 and the drainage removal. Do not apply it. Current rules are in PF-Canon, PF10, the decision record and the procedures in `docs/prompt_ecosystem_management/`, including `operating-procedures/`. Everything below the separator line is the original file, byte for byte (135,590 bytes, SHA-256 `dee7b76e2179a40c60f6882da6987683f59d4c25b3e1cebd686b4b23c5320497`).

---

# NON-CANONICAL — General Prompt Flow and Creation Guidelines

Version: 1.12.1
Updated: 2026-09-09
Status: non-canonical effective successor guidance; selection is determined by the Notion register.

## Prompt creation, internal subagents and model recommendations — Product Owner clarification, 2026-09-09

The rule **do not delegate prompt creation** applies to responsibility for authoring the requested prompt. The assigned author must complete that prompt rather than hand the task onward by producing another prompt or appointing a replacement prompt-author session. This rule does **not** prohibit internal subagents. Do not reinterpret it as a blanket delegation ban or a reason to exclude Ultra.

Internal subagents may perform bounded research, retrieval, analysis, implementation or checking within the actual authorized assignment when necessary or materially useful. No additional generic permission is required solely because the assigned agent uses internal subagents. The responsible agent defines bounded work, integrates and verifies the results, preserves source fidelity and remains accountable for the complete output. For prompt-creation tasks, that agent retains complete prompt authorship; helpers can examine sources, requirements, contradictions or the completed draft without replacing the author or creating a recursive prompt-writing handoff.

Internal assistance does not replace a named workflow actor, satisfy a separately required independent approval, transfer decision authority, authorize another workflow invocation or expand write permissions. Preserve actual author/reviewer separation, sole-writer controls where required, task scope and external-action permissions. A sole writer is compatible with internal read-only analysis. An explicit restriction that genuinely addresses subagent use must be interpreted within its stated scope; do not manufacture one from prompt-creation, session-identity or approval-owner language. Identify any real capability or controlling-instruction limit precisely instead of attributing it to a generic model prohibition.

Recommend the supported surface, model and reasoning mode that best fit the **complete actual workload**, its quality target and expected total completion cost. No model or reasoning mode may be excluded merely because it uses internal subagents, is stronger or costlier, is absent from a fixed task table, or has not been observed in the user's account picker. Consider all currently supported candidates that meet the actual task requirements. Necessary subagent work must not be blocked by a misapplied prompt-creation rule, and Ultra must remain a candidate when meaningful independent work benefits the task. Permission to use it does not make it the default: justify the selected configuration from the work, not volume or an automatic maximum.

Give one exact primary recommendation, with a task-specific reason and a clearly conditional fallback when useful. Separate published support, observed configuration and genuine launch limitations. An unavailable account-picker inspection method alone does not prevent concrete advice supported by current official guidance; never invent actual availability or configure the session merely because a model was recommended. The human retains launch selection.

This explicit Product Owner clarification controls contrary broad wording in this guide. Preserve the narrow prohibition on delegating prompt creation, actual workflow actor/approval boundaries and historical observations. It adds no new approval stage and does not activate workflow automation.

## GCFPE Epic re-engineering effective contract

Apply the separately bound `epic-reengineering-correction.json` after the unchanged epic-alpha predecessor and immutable R1 layers. Target GCFPE-20260909.1 / 090926.1 has 53 prompt members, one Analyzer, 50 effective logical rows: 48 preserved predecessor rows plus conditional GCF-R01 / IA-50 and GCF-R02 / IA-60. Historical R1 still has 46 rows. Target metadata never establishes live selection; the owning Notion register does. Automation remains held. No active role session is contacted by maintenance.

The sole GCFPE-ASSESS-10 wraps every separate substantive invocation, including research, answer seeding, same-author recovery and correction intake; ordinary clarification and internal Audit/Plan phases do not add rows. IA-50 — IA Answer Seeder and IA-60 — Thoth Planning Research are both in Notion AI Prompts / HDE IA. Human answers are returned data. IA retains whole-change architecture ownership, Isis independent review and dedicated PR actors detailed engineering. Thoth's research lane accepts preapproval inquiries; ESC-30's remediation native inputs and returns remain unchanged.

Correction intake: an actual engineering answer or Canon conflict materially changing an approved Plan without changing objectives/exclusions first goes to existing same-Isis IA-30 with exact approved base/review/Specification and evidenced delta when no real correction instruction exists. Its actual PLAN_REVIEW_ID permits IA-40 and IA-30 return. Never invent a denial, Canon conflict, rescope or review ID. Actual rescope prerequisites apply only to actual scope changes; qualified ESC-40 equivalent Plan review retains every existing exact-Plan/reviewer/coverage predicate and does not require duplicate IA-30 approval.

Recovery contract:

| Paused state | Native continuation after IA-50 and the Analyzer |
| --- | --- |
| IA-10 Audit incomplete | Same IA-10; approved SPECIFICATION_ID plus exact incomplete phase checkpoint/envelope |
| Audit complete, initial Plan incomplete | Same IA-20; SPECIFICATION_ID and complete IMPLEMENTATION_AUDIT_ID plus Plan/checkpoint/envelope |
| Real IA-40 correction paused | Same IA-40; actual IMPLEMENTATION_PLAN_ID and PLAN_REVIEW_ID, remaining corrections, envelope; preserve ordinary IA-30 or remediation ESC-40 return |
| Approved Plan materially affected, no correction instruction | Existing same-Isis IA-30 correction intake first; real base/review/Specification and evidenced delta |

The envelope carries exact change, paused prompt/version/phase, author/session/reviewer, base/checkpoint identity/version/state/coverage, stable complete question, examined evidence/alternatives/unresolved fields/affected requirements/sections/ADRs/files, actual answer/finding with source/authority/limits, remaining work, return and real prerequisites. Partial answers affect only answered fields. A valid partial answer permits SEED_READY for bounded same-IA continuation when its native prerequisites are present; an unanswered decisive question still blocks later Plan submission, not that limited continuation. Applied duplicates reuse actual successor lineage. Stale/contradictory answers return the exact conflict to its owner. Scope changes use existing authority. No restart except explicit Product Owner instruction. IA authors complete successor artifacts; seeder/research do not approve or edit the Plan. A missing answer means an exact human question and recoverable pause, never a placeholder runnable handoff.

## First substantive operation — PFCanon header inventory

**Native duty owner: CF-E-10 kickoff worker only.** The following requirements describe that worker’s output and permitted actions. A controller routes and verifies this contract; flowmaster-validate and governance-audit only inspect it. They do not author, revise, approve, decide, publish or execute the worker’s task.
After Analyzer entry and before any kickoff source interpretation (including the Epic Strategy Card), verify Glow / Core Docs / PFCanon ancestry and inventory its complete direct-child header-pair scope. No inaccessible-directory broad-search fallback is allowed. Pair by stable PF identity and verified directory membership, retaining exact file IDs, MIME types and current-representation selection evidence in runtime provenance. Inventory Markdown, DOCX and native Google Docs as their actual stored forms; do not report a DOCX comparison when only a Google Doc exists. Exports retain native source identity and representation lineage.
Compare title/document identity, version, status and corresponding date/update-gate fields when present across the controlled Markdown and each actual document counterpart. Retain raw compared values. Normalize harmless whitespace only, preserving case, punctuation, numbers and meaning. Record MATCH, MISMATCH, INCOMPLETE, UNPAIRED, UNREADABLE or AMBIGUOUS_SOURCE; duplicate competing candidates never silently select the highest version. Header parity proves only header parity. Missing required identity/version/status fields are INCOMPLETE; a missing counterpart is UNPAIRED, not MATCH.
For each discrepancy record affected source use and correction/routing/explicit acceptance owner. Scoped acceptance names the exact allowed representation/version, scope and reason; retain the original unequal status and raw values. Block dependent source use where required, not unrelated kickoff work or whole-library repair. This comparison does not replace the existing controlled Markdown authority predicate or extend a live-Drive gate to authorized QA/OPS execution copies. Include the full inventory/provenance and dependency dispositions in the kickoff evidence and carry the material result in the sole kickoff handoff.
The installed Change Flow header helper may extract synthetic/local Markdown and DOCX and compare a faithfully exported native document header record using standard-library tools; it does not discover authority, establish ancestry, choose a canonical body or repair sources. If a real header cannot be extracted faithfully, report the limitation and inspect the actual representation with available tools.

## Whole-change architecture and readiness

**Native duty owner: IA-10, IA-20 and IA-40 authors only.** The following requirements describe that worker’s output and permitted actions. A controller routes and verifies this contract; flowmaster-validate and governance-audit only inspect it. They do not author, revise, approve, decide, publish or execute the worker’s task.
Own a viable whole-change implementation architecture before requesting Plan approval: component ownership, interfaces and exact important data shapes, invariants, cross-component dependencies, sequencing, failure/recovery behavior, acceptance allocation and decisive source feasibility. Use useful examples and diagrams where they make design reviewable. Dedicated PR authors retain detailed per-file planning; architecture, source-defined domain meaning and feasible evidence collection cannot be deferred as PR detail.
Trace each requirement to the actual source clause, design decision, owned work unit, acceptance meaning and evidence deadline. An approved Plan governs its bounded change and approved decisions; it does not silently override unrelated Canon. Correct clear author transcription errors; classify genuine conflicts under the carried ADR contract. Resolve architecture/feasibility-determining questions before claiming submission readiness. Carry routine execution checks only to their legitimate stage, with exact owner/deadline; never weaken an upstream deadline. A complete Audit may contain explicit blocked dispositions, but that does not make an unresolved architecture ready for Plan approval. Save a truthful checkpoint and exact question when decisive evidence is absent.

Record decisive questions in the existing Audit/Plan, not a parallel approval system. Each entry carries stable question identity, complete question text, exact requirement and row/field, inspected source passages and provenance, known facts, remaining unknown subset, competing interpretations, proposed decision or exact unresolved exception, affected sections/ADRs/files, actual owner and required stage deadline. Extract conclusive facts even when other fields remain unresolved. No generic all-evidence-pending debt or assumed small unresolved subset is acceptable.
For mechanics development questions inspect current controlled PF08 and PF11 first. If inconclusive, verify Glow's direct HD Refs directory, read its Human Design Reference Index and retrieve the actual admitted source passages needed by the claim. The index alone is not doctrinal evidence. Use an available original PDF without requiring Markdown conversion. If bounded external inquiry is necessary, use only jovianarchive.com. An inaccessible original proves an access limitation, not absence of doctrine. If still unresolved, give the Product Owner the exact question, alternatives, inspected evidence, affected fields and practical consequences.
For engineering, inspect relevant current Canon and actual repository interfaces/files first; then use bounded primary technical sources. An advanced unresolved inquiry goes through the single Analyzer to IA-60 — Thoth Planning Research in AI Prompts / HDE IA. Prepare exact files/interfaces, constraints, alternatives, failure modes, decision criteria and requested finding. No approved Plan is required for this preapproval route. Preserve ESC-30's separate remediation intake and authority.

## Independent substantive review and ADR decisions

**Native duty owner: Existing native Thoth/Isis reviewers only; standalone approved-Plan addenda belong only to IA-30 or qualified ESC-40.** The following requirements describe that worker’s output and permitted actions. A controller routes and verifies this contract; flowmaster-validate and governance-audit only inspect it. They do not author, revise, approve, decide, publish or execute the worker’s task.
Independently compare the author's stated intent with the behavior a competent reader would infer from the actual complete artifact. Inspect canonical truth, Human Design fidelity where relevant, engineering quality, feasibility, coherence, source sufficiency and final handoff completeness. Apply PF13 and PF21 to outcome, coherent surface, boundaries, stewardship and applicable phase intent without symbolic stages or mandatory scores. A polished checklist or generic approval is insufficient when a decisive source or architecture claim is unsupported.
Review each stable ADR against exact affected clauses, competing alternatives, rationale and implementation effects. Require NEW_CANON or CANON_RECONCILIATION, or a different class only with an already approved definition. Give every ADR an explicit APPROVED, APPROVED_AS_CHANGED with exact changed text, or REJECTED with reason disposition. Inclusion in a Plan is not approval. Preserve rejected proposals and original/changed text. Material new design returns to its author for a complete reviewable successor before approval.
For approved Plan decisions, preserve the existing standalone PF10 build-note addendum contract alongside exact approved Plan and proof: include every approved ADR's ID/class, exact decision, scope, lineage, drainage owner/target and authority boundaries. A coherent mixed approval batch may contain approved and approved-as-changed items only; retain rejected items in review evidence. All rejected means no empty addendum. Reuse a valid exact batch without duplication. Apply the same appropriate existing reviewer/addendum boundary to late findings; no new approver is introduced. Keep proposal, review decision, source-resolution, addendum preparation, Product Owner publication and permanent drainage states separate. Informational publication pending alone is not an extra gate; a decisive governing conflict remains evaluated on its actual resolution and scope. Never mutate PF10 or choose final numbering.

## Semantic readiness before INSTRUCTION_READY

**Native duty owner: PR-10 instruction author only.** The following requirements describe that worker’s output and permitted actions. A controller routes and verifies this contract; flowmaster-validate and governance-audit only inspect it. They do not author, revise, approve, decide, publish or execute the worker’s task.
Compare the complete instruction, clause by clause, against the exact approved Specification, Implementation Plan and review, applicable classified/decided Canon ADRs, decisive current Canon/repository evidence and the full selected PR-20 contract. Keep a compact comparison record of source clause, intended meaning, instruction meaning, owned unit, acceptance and required evidence stage. Check numeric domains and zero/sentinel meaning, boolean exclusion where the integer domain excludes booleans, exact nested/closed object schemas, field ownership, separate PR ownership, acceptance-criterion meaning, dependency order and evidence deadlines. Do not copy historical example constants into this reusable contract.
The instruction must carry enough meaning and decisive source feasibility to plan the approved unit without reconstructing upstream intent. Preserve every obligation outside PR-20's Inputs heading: complete detailed engineering planning, implementation, security/code review, corrected-code coverage, findings and re-review, CI with scoped waiver conditions, manual-merge dependency handling and completion evidence. PR-20 may return its native AWAITING_PO_PROCEED only for a complete executable scoped plan; do not substitute an upstream PLAN_PENDING state or imply Proceed. The sole downstream native input remains PR_INSTRUCTION_ID and transport preserves its exact identity and complete source package.
Do not mark INSTRUCTION_READY while a decisive comparison fails. Correct author transcription/instruction errors here without a fake Canon ADR. Return a genuine architecture/design/Canon conflict to the actual IA/reviewer or existing remediation/rescope owner with exact evidence and native inputs through the Analyzer. Missing source feasibility is an exact owned question before its source-required deadline, not an automatic postponement until mutation. The Analyzer only assesses the unchanged package and cannot repair this instruction or approval.

## Actual final-response contract

**Native duty owner: Each invoked native producer; Analyzer has its own worker-recommendation output.** The following requirements describe that worker’s output and permitted actions. A controller routes and verifies this contract; flowmaster-validate and governance-audit only inspect it. They do not author, revise, approve, decide, publish or execute the worker’s task.
Before sending the final response, inspect the actual final text against the actual result branch. State the result and usable artifact identities first, then the exact immediate next prompt name/directory, actor and retained or initial session, surface/model/reasoning and task-specific rationale, followed by the complete populated invocation. Advice here is for the Analyzer run; its own MODEL_HANDOFF advises the worker. A saved attachment containing the block does not satisfy final delivery. Unknown picker observations do not prevent concrete advice based on current applicable official support; disclose unobserved configuration separately. Do not guess inaccessible capabilities. A blocked branch gives the exact missing question/input/owner and recoverable saved state, without a fake runnable block. A real terminal branch returns to its native owner without an invented Analyzer. A human answer not yet received is a prerequisite, never a placeholder runnable seeder package. This check covers success, denial, revision, remediation, rescope, partial/manual-action, recovery and terminal results, including CRD paths. It is an output check within this invocation, not another stage.
Producer and Analyzer schema include actual release and resolved source/destination runtime versions (truthful no predecessor version for OPERATOR_DIRECT_RECOVERY), native inputs, exact actor/session, artifact/approval/source lineage, real gates, full QA membership and per-task attempts/results/reviewers when applicable, capabilities, risks, package status and immediate-next recommendation. Predecessor recommends the Analyzer, Analyzer reads the entire worker contract/decisive sources and returns MODEL_HANDOFF plus unchanged worker invocation. Unknown picker does not prevent supported concrete advice. Official guidance remains dynamically appraised; no fixed worker table or measured-cost claim is added.

## Verification and preservation

Validate complete affected bodies and all-member dispositions, graph closure, exact native phase inputs, actual final outputs, both ADR classes and approve/change/reject batches, late addenda, source feasibility and historical semantic counterexamples. Static string presence is insufficient. Preserve actual QA membership/attempt rules, manual merge and Proceed, CRD compatibility, PF20/PF30 section-only outputs, PF09 substantive build-note addenda, bounded direct CRD candidate records and CL-40 terminal ownership. Header parity is Epic-only and not a new QA/OPS execution-copy gate. Permanent source drainage and pending informational PF10 publication are distinct from unresolved governing decisions.

Use complete pinned snapshots and meaningful positive/negative fixtures; distinguish deterministic, isolated prompt-output and live evidence. Do not relabel historical counts or unresolved stalls as observed success. Require independent meaning/feasibility/role-boundary review before selecting published, fully read-back compatible candidates. Preserve old selected lineage until compatibility, archive original pages intact and verify guide pointers, installed persisted skills and selected identities. No Technical Writing or protected Primary-core change is authorized.

## Current successor target metadata

GCFPE_RELEASE_CONTRACT
```json
{"analyzer_ids": ["GCFPE-ASSESS-10"], "automation_hold": true, "logical_rows": 50, "positions": ["ENTRY", "TRANSITION"], "preserved_predecessor_rows": 48, "release": "GCFPE-20260909.1", "runtime_version": "090926.1", "selected_prompt_ids": ["CF-C-10", "CF-C-20", "CF-C-30", "CF-C-40", "CF-E-10", "CF-E-20", "CF-E-30", "CF-E-40", "CF-PO-10", "CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40", "GCFPE-ASSESS-10", "GCFPE-MGMT-10", "IA-10", "IA-20", "IA-30", "IA-40", "IA-50", "IA-60", "MGR-10", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30", "UTIL-10"]}
```

## Preserved procedures and dated lineage


## Preserved GCFPE Epic-alpha predecessor contract, 2026-09-08

Authorized target release GCFPE-20260908.2 has 51 selected prompt members, exactly one reusable GCFPE-ASSESS-10 and 48 substantive logical rows. Actual selection is owned by the live GCFPE Membership and Release Register. This guide does not select a release or activate automation. The correction supersedes the prior first-invocation exception and broad automation-hold wording only for GCFPE; earlier dated events remain historical. All separately owned Technical Writing contracts remain unchanged.

Topology: Product Owner cycle entry → GCFPE-ASSESS-10 [ENTRY] → first substantive prompt → GCFPE-ASSESS-10 [TRANSITION] → eligible next substantive prompt; after the final appraised CL-40 completion, return directly to the Product Owner. Ordinary clarification and the combined IA-10/QA-50 Audit-then-Plan phases stay within their invocation.

Every actual later substantive handoff retains the existing middleware duties: the predecessor selects the exact native eligible destination, prepares the complete actual package, and recommends the Analyzer's configuration; the Analyzer reads the complete selected destination and decisive sources, returns full MODEL_HANDOFF, and only when eligible emits the complete unchanged native invocation in the final response. READY/READY_WITH_LIMITS is strength appraisal, never approval, dispatch or substantive execution. Incomplete input preserves all valid state and names the exact missing fact, recovery owner and smallest safe action. Action-time approvals, manual PR controls, one-way sends, QA membership/attempts and native source requirements remain intact. No ordinary direct substantive handoff bypasses the Analyzer.

For both ENTRY and TRANSITION: The Analyzer reads the complete current governed destination, complete actual package and every decisive source needed to appraise the whole destination operation. It assesses source breadth and coupling; tools and environment; reasoning, novelty and ambiguity; output and verification; consequence and action risk; context-transfer pressure; sequential/asynchronous burden; and session stability. MODEL_HANDOFF states the exact eligible surface, available model and supported reasoning level, required capabilities, reasons, cheaper eligible alternative or NONE ESTABLISHED, posture, evidence/limits and reassessment triggers. READY and READY_WITH_LIMITS concern strength appraisal only. When ready, the final response includes the complete unchanged destination-native invocation. Incomplete, contradictory or ineligible input returns ASSESSMENT_INCOMPLETE, preserving valid state and naming the precise recovery fact/authority, owner and smallest safe action; no runnable destination is fabricated.

## Managed entry, execution posture and continuing identity
Carry one execution-posture field, EXECUTION_POSTURE, with exactly MANUAL_PROMPT_EXECUTION or AUTOMATED_ORCHESTRATION. An explicit Product Owner manual alpha invocation uses MANUAL_PROMPT_EXECUTION. The active automation hold blocks AUTOMATED_ORCHESTRATION, hidden dispatch, scheduled execution and cross-session automation; it does not block that manual Analyzer or substantive invocation. This distinction supplies no action authority beyond the native task. Publication, validation or release selection never activates automation.
The single GCFPE-ASSESS-10 supports ANALYZER_POSITION: ENTRY | TRANSITION. At Product Owner cycle entry it is the first managed prompt: ENTRY precedes CF-PO-10 for unresolved classification, CF-E-10 for a valid Product Owner EPIC selection, or CF-C-10 for a valid CRD selection. The Analyzer records rather than invents the selection; CF-PO-10 obtains a missing Product Owner classification. No predecessor or preceding Analyzer exists for ENTRY. Every later concrete substantive handoff uses TRANSITION with actual lineage. An explicitly operator-invoked native direct/recovery task uses that same assessment profile with truthful source OPERATOR_DIRECT_RECOVERY, its complete actual native intake and available lineage, without inventing a predecessor prompt. This does not repair or bypass a known incomplete upstream decision/output; recover that actual output where required. Preserve native QA-90 direct-entry clarification when task selection is absent. Pure ecosystem maintenance is not an unresolved Epic/CRD classification: its existing standalone manager intake remains outside development-cycle ENTRY routing, with a direct/recovery assessment package naming the actual maintenance case as required assessment middleware before the actual standalone maintenance invocation; no invented development ID or CF-PO-10 route. Internal clarification and combined Audit/Plan phases remain inside their invocation. No Analyzer follows a true terminal result; CL-40 COMPLETE remains terminal.
Separate persistent role identity from invocation binding. Carry session_disposition, role_session_ref, invocation_binding (exact change, artifact, stage and task), and context_conflict (NONE or the exact unresolved conflict). For an explicitly Product Owner-selected continuing named session use session_disposition: RETAIN_EXISTING and the exact supplied reference. A user-assigned reference suffices; do not invent a platform ID. Clarify only missing/contradictory identity, wrong role, inaccessible required continuity, an actual incompatible active binding, or explicit Product Owner replacement. Age, a completed prior change, a new change, new model advice, slow work or an unproven stall do not require reinitialization. Missing artifact/stage facts remain explicitly unresolved until the native task establishes them.
Dedicated IA and PR boundaries remain distinct: one whole-change IA session per change and one PR session per planned PR work unit. Resume a correctly bound existing dedicated session; do not repurpose an unrelated one. For a native first dedicated assignment, session_disposition: INITIAL_DEDICATED_ASSIGNMENT records the exact required role and change/work-unit binding. role_session_ref may truthfully state NOT_YET_ASSIGNED with the Product Owner/operator assignment owner when the native handoff permits assignment at launch; it never fabricates a session ID. A missing continuing named-session identity still requires clarification. These fields record identity; they do not authorize this actor to create, restart, message or replace sessions.
## Canonical PF source predicate and PF10 boundary
When selecting an authoritative PF source in Drive, prove every step: resolve Glow; resolve its direct child Core Docs; resolve that folder's direct child PFCanon; list that PFCanon folder's direct children; select only the controlled Markdown lane for the stable PF identity; verify the selected file's direct parent ID equals that PFCanon folder; require one unique current controlled match. If any step fails, stop the affected source-dependent operation with SOURCE_RESOLUTION_ERROR naming the failed predicate, source, evidence needed and recovery owner. Do not select by title, search rank, modified time, archive/export/download result or highest-looking version. A broad search may locate a candidate folder but supplies no authority. Keep actual IDs, versions and parent evidence only in runtime provenance.
Preserve the separately approved bounded QA/OPS operator-prepared repository execution-copy access rule when the native task expressly permits it. Such a supplied execution copy is not a newly selected current canonical Drive source and must not be claimed to satisfy this predicate without proof. Do not impose a new live-Drive, parity or freshness gate on that authorized execution-copy route; a missing or conflicting requirement still goes to its owning authority. This exception cannot be used to select an archived search result as current Canon.
Epic or CRD execution may create standalone, paste-ready PF10 build-note addendum Markdown artifacts within its explicit authority. It may not edit, append, replace, upload, publish, or otherwise mutate PF10. PF10 insertion and publication remain separate Product Owner-controlled work. Do not choose final PF10 numbering or read PF10 solely for numbering. Preparation, approval and pending informational publication are distinct; pending informational publication is not a Plan, readiness, QA or closure gate. Preserve actual required Product Owner scope/rescope disposition and its existing manual prerequisite separately.
## Carried Canon-conflict register
Preserve one CANON_CONFLICT_REGISTER in existing applicable substantive artifact metadata/content and handoffs. This is carried state, not a new approval artifact, prompt, role or stage. Assessment-only and read-only actors validate/carry it in their permitted output; they gain no substantive authoring, review or Canon authority. Record an evidenced conflict when the current actor's native artifact permits findings; otherwise carry the exact finding to its existing owner. An empty register is valid only when actual source coverage supports no identified conflict; unknown coverage is not an empty finding.
Each entry retains: stable conflict/ADR ID within the change; classification NEW_CANON, CANON_RECONCILIATION or another already approved category; exact conflicting sources, resolved versions, clauses and evidence; conflict statement; affected requirements; alternatives; recommended disposition; interim treatment; unresolved risk; permanent drainage target and owner; status PROPOSED, APPROVED, APPROVED_AS_CHANGED or REJECTED; reviewer/session; reviewed artifact identity/version; decision time; decision rationale. Before review, review fields explicitly remain not yet reviewed rather than invented. Preserve the original proposal, decision history and the reviewer's exact change for APPROVED_AS_CHANGED. Rejected entries remain with rationale. Merely including an item in a Plan is not approval; no silent resolution, omission or Canon edit is permitted.
Use the next applicable existing review boundary. Specification conflicts receive explicit Thoth disposition in CF-E-30 or CF-C-30. Conflicts first introduced in the Implementation Audit/Plan receive explicit Isis disposition in IA-30. Ordinary late material changes use IA-40 preparation/revision then IA-30 review when a real correction instruction exists; otherwise current IA-30 bounded correction intake comes first as defined in the effective successor contract. Preserve the already integrated remediation exception: its pending complete IA-authored successor goes through IA-40 to the same Isis ESC-40 combined review, which satisfies the existing Plan-review contract only with its exact required predicates; do not add a second IA-30 approval of the identical design. Its equivalent Plan decision carries the same register/disposition/addendum duties. This preserves the prior graph and one review, not a new downstream Canon authority. Non-plan-affecting post-closure architectural records retain the explicitly assigned CL-30 lane; CL-30 does not approve its own proposals. Permanent Canon drainage retains its existing owner.
Do not reinterpret accepted history or fabricate an approval, rejection, reviewer or drainage owner. Materially changed scope/requirements use the existing actual author/reviewer correction path; unaffected decided items remain decided. Carry exact register lineage, publication evidence and unresolved facts through all next/recovery packages.


### GCFPE release provenance — target, not selection authority

This source-bound metadata describes this coordinated correction. Actual selected state comes only from the Membership and Release Register.



### Reusable human ENTRY launch block

Provisional, current, nonbinding Analyzer launch guidance: ChatGPT Work / GPT-6 Astra / High for bounded intake appraisal, subject to actual supported availability and the current official appraisal. The human chooses configuration. Refresh official OpenAI documentation when catalog/surface coverage is stale, eligibility is uncertain, Max or Ultra is considered, the choice is non-obvious, or a material capability/stall anomaly requires reassessment. Reuse applicable current evidence for ordinary adjacent handoffs. Published guidance, tool exposure, account access, recommendation and observed configuration are distinct. No inferred WU, context-window, runtime-configuration or model-causality claim is permitted.

Populate the following template from actual intake before using it. Placeholders are template notation, not runnable values. For an unresolved class, preserve available intake and exact unknowns; target CF-PO-10 to obtain the Product Owner classification. A missing assigned development ID is not invented. Read the complete selected Analyzer and intended native destination first.

```plain text
run @Notion prompt GCFPE-ASSESS-10 — Assess the Next GCFPE Workload

Inputs
Prompt directory: AI Prompts / HDE Change Flow
ANALYZER_INPUT
ANALYZER_POSITION: ENTRY
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
Entry source: PRODUCT_OWNER_CYCLE_ENTRY
Product Owner/operator: <actual supplied identity>
Change class and identity: <actual PO EPIC/CRD selection and assigned identity, or UNRESOLVED with exact known intake>
Intended substantive destination: <CF-PO-10, CF-E-10 or CF-C-10, exact versionless name and verified directory>
Destination actor/session: <native actor; exact supplied role_session_ref; session_disposition; invocation_binding; context_conflict>
Actual first task: <complete actual operation and available intake>
Native destination inputs: <complete actual native values; exact unresolved facts where the native intake obtains them>
Source/artifact lineage: <complete actual identities, versions, statuses and relationships; no fabricated predecessor>
CANON_CONFLICT_REGISTER: <actual complete carried state or supported no-conflict state>
Applicable gates/manual prerequisites: <actual satisfied, pending or not-applicable state, evidence, owner and action>
QA selection and attempts: <actual complete state or explicitly not applicable>
Capabilities: <required and available tools/stores/environment and actual limits>
Risks/anomalies: <actual facts and unknowns>
Package status: <complete, conditionally eligible or blocked, with exact reason and missing facts>
Analyzer run recommendation: <current provisional or freshly appraised human launch configuration and evidence limits>
```

There is no fabricated source prompt, no Analyzer before this ENTRY invocation, and no destination invocation when required source/decision/native intake is incomplete. A routing header alone from CF-E-30 lacks the full Thoth output and branch: return ASSESSMENT_INCOMPLETE, name that missing output and emit neither guessed IA-10 nor CF-E-40. A complete approval preserves IA-10; complete denial preserves CF-E-40.

### Plan review and standalone approved-decision addenda

At final complete Plan approval, output one or more standalone Markdown PF10_BUILD_NOTES_ADDENDUM artifacts for every APPROVED or APPROVED_AS_CHANGED ADR carried by that Plan, using a coherent approval batch when appropriate. State approved decisions directly, not as proposals. Include change, exact Plan and review identity/version and approval lineage; each ADR ID/classification, source conflict, approved decision, interim treatment, affected scope, permanent drainage target/owner, and implementation/authority boundaries. State insertion/publication is a separate Product Owner-controlled action. Preserve exact original proposal and review changes in the register/proof. Store the standalone files alongside the approved Plan and proof package under the native artifact storage contract.
Create no addendum when all entries are REJECTED; retain every rejection and rationale in the register and review proof. Reuse a complete valid prior addendum for the same exact disposition batch. When verified carried evidence establishes an already published matching disposition, record that existing disposition and do not recreate or duplicate it. Do not read PF10 solely to number an addendum or claim publication from preparation. Never assign a final PF10 addendum number, insert, append, edit, replace, upload or publish PF10. Pending informational insertion does not block the approved Plan. Any required artifact-save failure is reported truthfully under native evidence rules, not converted into a PF10-publication gate.


The addendum duty belongs to final IA-30 Plan approval, or the already qualified same-Isis ESC-40 integrated exact-Plan review under its existing predicates. Thoth Specification review records proposals in existing Section 12 and decisions in existing Section 1 metadata; Sections 2–13 remain verbatim on approval. A substantive APPROVED_AS_CHANGED requirement change therefore uses DENY → same Isis revision → same Thoth review. Ordinary late Plan conflicts with a real correction instruction return through IA-40 → IA-30; without one, current IA-30 correction intake comes first; the postapproval correction is carried under existing PLAN_REVIEW_ID, not a new artifact or key. CL-30 retains its assigned ADR_CANDIDATE authoring lane and gains no selfapproval or new approver. Actual RS-20 rescope disposition remains a prerequisite distinct from informational PF10 publication.

Carry existing approved or rejected history without redeciding it. Verified matching published addenda are reused as existing dispositions, never duplicated. Runtime IDs, exact resolved versions, hashes and publication evidence belong in provenance, not reusable source locators. This maintenance performs no live ADR decision or PF10 write.

QA-90 retains Product Owner selection, asks for absent/ambiguous direct-entry selection and never assumes ALL or a ready subset. Ordinary incoming QA-90 packages obtain that missing selection before becoming runnable. QA-110 preserves attempts, exactly one native valid-plan ordinary retry and waiting already-authored task reuse through QA-100. QA-10 still saves all three native artifacts, including substantive paste-ready build-note triage or supported NO_ADDENDUM_NEEDED with retained triage identity. CL-40 frames supported PF09 gaps as standalone PF10 build-note addenda; only eligible non-launch-blocking application CRD candidates receive the existing bounded direct candidate-list update. Prompt-maintenance findings stay in operational tracking. CL-40 completion remains terminal.

Publish and archive complete coherent successors, preserve all replaced Notion pages intact, verify every body/title/parent/version and archive hash, update all four raw Markdown guides in place, Git-sync each changed skill separately, and complete independent postflight before selecting. The new predecessor-bound Epic-alpha overlay follows unchanged R1, integrated QA/remediation, final scan, alpha feedback and Strength Analyzer layers; the marked Primary core remains byte-identical. Preserve open lifecycle/automation holds and historical records. Static validation and publication prove contract consistency only. PF04 Astra Max stall remains an unresolved reported anomaly with no established cause or prevention claim. General Guidelines retain model appraisal and the concise GCFPE learning observation; existing monthly review is unchanged.

Source and authority: Product Owner-authorized GCFPE Epic Phase Alpha Repair One-Off Implementation Prompt and complete Feedback Assessment, resolved under Glow HDE 3.0, plus current selected Notion controls, all51 complete prompt bodies, current guides, installed immutable layers and verified read-only canonical-source evidence. Exact one-off identities and hashes are held in the implementation evidence; this contract uses stable resource names and verified directory paths.


## In-flight model and surface learning — 2026-09-07

Nathan authorized incremental improvement using the pilots already running. Maintain the existing quality and acceptance requirements, then choose an eligible surface/model/effort with the best supported total cost of completion. Include retrieval, reasoning, tools, retries, verification, handoff and human correction effort. A cheap initial attempt or a stronger model name does not establish the lowest cost per accepted result.

### Make the recommendation useful

1. Establish the actual assignment, source scope, required capabilities and acceptance conditions. Separate volume from ambiguity, coupled reasoning and consequence. Missing access or an unclear brief is not solved by increasing effort.
2. Consider Chat or Work from the exact required operations, source access, output form and observed capabilities. Then select the model and its supported reasoning level separately. Respect explicit surface choices and existing role/session controls. Do not translate Chat GPT-6 Pro into Astra or apply Work effort labels to Chat.
3. Choose one exact task-specific recommendation. Where useful, identify a cheaper eligible alternative and the unresolved condition that would justify escalation. Label the basis as official guidance, task judgment or comparable observed outcomes. A provisional recommendation is not a measured optimum, and an unknown account option remains unknown.
4. Use the lowest effort reasonably supported to meet the existing quality target. Do not make Medium, Max or any named model a permanent workflow default. A long input alone does not justify Max; Ultra requires useful independent work with clear integration and output ownership. Internal subagents are permitted when necessary or materially useful within the assigned task; the prompt-creation restriction does not prohibit them. Diagnose failures before changing configuration: distinguish source, access, prompt, tool and reasoning defects.
5. Carry this short recommendation in the existing handoff for the actual next unit. A session doing straightforward recording can need a different configuration from a session reconciling conflicting architecture. The human chooses; no advice authorizes self-switching or replacing an active session.

### Learn from current work

Use [Model Routing and In-Flight Learning](https://app.notion.com/p/3d44590a05eb817c8e55fbaad7283bce) under Glow Operations Hub. Add a concise observation at a useful ordinary completion/handoff or a material routing failure, within the writer's actual authority. Otherwise return it through the existing handoff for an authorized maintainer. Do not add a record for every routine turn or retrofit mandatory outputs into frozen prompts.

Record task/input scope, recommended configuration and rationale, actual configuration and evidence or UNKNOWN, acceptance/corrections, elapsed time or human effort when observed, usage with its original unit and source, and the lesson/uncertainty/next trigger. Link existing evidence. Missing usage is neither zero nor a blocker; no invented WU estimate, telemetry, session identity or model attribution. Session-wide usage is not task-specific when concurrent activity prevents attribution. Do not convert credits, tokens or WUs without a verified applicable basis.

Treat these as observational results, not controlled comparisons. Preserve task differences, sample counts and uncertainty. A single failure does not establish model causality. Prefer a cheaper route when comparable evidence supports acceptance, and retain a stronger route where failure/review cost warrants it. Do not rerun live work just to benchmark configurations or start competing writers. The separate deferred model-run-data infrastructure remains deferred; this lightweight record does not install it.

### Keep the guidance current without repeated research

This guide remains the sole selection-method and model-appraisal owner; Notion records outcomes and links. Reuse a current applicable appraisal. A verified release/retirement, changed capability or pricing, stale basis, or consequential result triggers a bounded refresh for the relevant surface and workload. Preserve the existing read-only monthly review; no new automation is created. Refresh affects prospective advice, not already running assignments or accepted artifact identities. New models are candidates for appraisal, not automatic replacements.

Official model and usage guidance was consulted on 2026-09-07: [Models](https://learn.chatgpt.com/docs/models), [Pricing](https://learn.chatgpt.com/docs/pricing). Model/effort availability and usage treatment remain surface- and account-specific; public pricing is not an observed cost for Nathan's task. The current role/effort guidance below is a starting appraisal, not a local efficiency benchmark.

An advisory skill remains a possible later implementation. No new skill, gateway, delegation, cross-ecosystem responsibility or workflow approval stage is introduced by this revision.


## Current Glow TW follow-up — 2026-09-08

Current selection: **TW-ALPHA-20260908.1**, authorized by Nathan's approved Alpha Test Follow-Up Brief and “Proceed with implementation” (GLOW-TW-ALPHA-FOLLOWUP-090826.1). [TW hub](https://app.notion.com/p/3d44590a05eb8171ab6ff4dab33b00ef) and [Alpha control](https://app.notion.com/p/3d44590a05eb81fe991ff0114cb43029) hold the exact eight-member catalog. Revised TW-ASSESS-10 and TW-MGMT-10 are 090826.2; TW-DRAIN-10, TW-DRAIN-20 and TW-APPLY-10 are 090826.1; triage and both section-only record prompts remain 090726.2. All predecessors remain intact.

Before substantive redline creation, run [TW-ASSESS-10](https://app.notion.com/p/3d54590a05eb81c395f4f2d92e9cccc5) against the actual preparation task. After a complete READY package, run a separate assessment of that actual original/package and output/verification burden before [TW-APPLY-10](https://app.notion.com/p/3d54590a05eb81f99ce6e7908a2a5a60). Creation advice cannot substitute for that second checkpoint. Reuse matching verified assessments on unchanged continuation; keep exact scope, baseline, package and session identities. Configuration/launches stay with Nathan or a separately authorized controller. No automatic switch, resend, new session or universal gateway is authorized.

Both drains verify assigned scope, complete selected task coverage, applicable outputs and actual need. Complete supported zero-edit work returns exactly `no redlines`: no artifact, handoff, application or version bump. Missing evidence is not no work. Changed preparation delivers complete redlines/report artifacts and a populated final-response pre-Apply assessment handoff. Analyzer final-response handoffs provide source prompt/files, scope, model/effort, package status, gates, risks/anomalies and actual next invocation. Triage remains list-only and exempt.

PF09 independently checks all six dimensions, without blocking on absent development-board data. New tasks use the actual phase's native format and available source context; mark reasonable descriptive inference. Never fabricate IDs, phase, completion, approval or evidence. A genuine unresolved schema/ID/authority question is a specific blocker.

The creator validates the whole original-bound package before READY. RL-045's single-occurrence FIND_AND_REPLACE is invalid; correct it explicitly at the producer and revalidate the complete package. Apply repeats validation and rejects an invalid batch atomically: zero edits, unchanged original, verified diagnostic back to the actual preparer. No silent conversion or valid-subset application. Corrected packages require full validation and package-specific reassessment.

A successfully changed downloadable PF receives one native version increment, actual application date and Last Update Gate containing exact deduplicated upstream source filenames used to create the redlines. Derive these narrow metadata edits before application and include them in conflict/preservation checks. Invalid/failed/no-change outputs get no revised PF or metadata bump. Only a separately requested report-only no-change result may use verified terminal/coverage evidence, without a fabricated package or assessment.

PF20/PF30 remain complete paste-ready sections only, no compulsory Apply bridge. Workers read current Drive PFCanon and PF03; no Drive write, PF publication, repository mirror change or product QA. Downloads are not canon. Reusable prompt bodies remain solely in Notion. Reports use the established authorized destination. Save/readback, partial-state and uncertain-write recovery controls are unchanged.

TW Flowmaster 1.1.6 supports this selected-catalog profile without changing its embedded Primary core, legacy selections or unrelated ecosystems. Flowmaster validator 2.5.2 updates the matching compatibility assertions; the suite passes. No runtime automation was activated. Twenty-nine isolated reference-contract checks and independent read-only scenario review passed; neither proves live model execution.

The preceding Alpha was generally successful per Nathan. PF04 reportedly hung on Astra Max; cause and actual tool/session/usage details remain unknown. Dated maintenance recommendation: Work / GPT-6 Astra / Extra High; Max only for justified added depth, not as a stall remedy. Use the OpenAI documentation skill for current capability/reasoning appraisal when needed, retain dated applicable evidence and separate recommendation from actual configuration. Record real observations without invented WUs/cost savings.

The dated TW block below is retained solely as historical evidence; this current section controls subsequent selected-profile work.

## Historical Glow TW alpha — 2026-09-07

The [Glow Technical Writing Ecosystem](https://app.notion.com/p/3d44590a05eb8171ab6ff4dab33b00ef) selects **TW-ALPHA-20260907.3**: seven operational/assessment prompts at 090726.2 and [TW-MGMT-10 — Manage the Glow TW Ecosystem — 090726.3](https://app.notion.com/p/3d44590a05eb81418640d9764d2ca4d0). The entry is [TW-ASSESS-10 — Assess Session Strength — 090726.2](https://app.notion.com/p/3d44590a05eb8103a89be82383bb1882). Nathan authorized coded names following GCFPE and internal-reference/relationship updates under GLOW-TW-NAMING-090726.1. [Alpha 1](https://app.notion.com/p/3d44590a05eb81fe991ff0114cb43029) records the exact eight-member catalog, prior lineage and actual verification. Earlier prompt pages remain intact.

For original release TW-ALPHA-20260907.1, static whole-set/handoff review, complete publication readback and 19 isolated executable fixture checks passed for their declared scope. No independent or live manual TW trial was performed. The prompt set is ready for Nathan's manual alpha; runtime results remain unproven. That original implementation invocation reused approval for design GLOW-TW-ALPHA-DESIGN-090726.1 without adding architecture, shared ownership, a gateway, Flowmaster, automation or skill dependency.

Nathan launches each document session and successor. The six operational roles remain distinct and directly invocable; triage is optional PF10-only list routing based on documented ownership, including eligible Reference documents. Every document-work turn has concise preflight; reuse applicable predecessor task advice and current cost/capability appraisal. Workers read current PF Markdown in Drive `Glow / Core Docs / PFCanon` and PF03 as the common writing standard, with no Drive writes or authoritative PF mutation.

Whole incoming source is the default; all Nathan-selected agendas/sections in any supported source are read fully without a compulsory unselected inventory. Drains read the complete target, account all selected changes and outside dependencies, and deliver redlines/report pairs with truthful preparation/save state. PF09 independently covers subtasks, tasks, phase statuses, new rows, evidence and Epic information. PF20/PF30 accept the correct approved specifications and actual required approval/history, keep planned and actual outcomes separate, and end with paste-ready sections only. TW-APPLY-10 requires complete successful preparation, exact original/scope and a valid non-overlapping literal batch; invalidity returns a Markdown diagnostic to the actual preparer through Nathan. No-change does not fabricate a PF version.

TW-MGMT-10 manages later TW prompt changes and selection through PE; it does not run before ordinary document turns. Handoffs carry real retrievable artifacts and actual selection/run identities; uncertain/partial saves are inspected and reconciled before retry. Implementation maintenance permission is separate from these runtime read-only contracts. Preserve GCFPE selection, adjacent utilities, unrelated consumers and in-flight identities.

For a first TW assessment, Nathan invokes TW-ASSESS-10 in an already-open session with the exact intended worker prompt, complete assigned target PF and incoming source blob, plus any selected sections and required supporting artifacts. The analyzer reads the complete intended prompt/target and whole or selected incoming scope, accounts for full reading/output/verification demands, and returns one supported surface/model/effort recommendation with task reasons, a cheaper eligible alternative when supported, dated evidence/limits and reassessment triggers. It stops before document work. Nathan chooses the available configuration and invokes the worker. Decisive missing input yields an incomplete assessment; account-picker unknowns alone do not create a new execution gate. Existing valid predecessor advice may be reused. Each worker still checks advice applicability and can reuse verified same-session source reading under its existing rules; successors establish their own access/coverage. The analyzer does not run on every turn, change models, launch sessions or add advice to TW-TRIAGE-10. It applies the current shared selection method without owning a second model catalog.

Codes use `TW-<FUNCTION>-<NUMBER>` with a descriptive action title. Ten-step slots identify related roles; they do not impose an execution order. Exact versions and immutable-source lineage stay in the selected catalog. TW-MGMT-10 retains its already coded identity. Document session names remain `TW-PFxx-x`; approved in-flight prompt/artifact identities are preserved.

TW-ASSESS-10 returns advice or an incomplete-assessment explanation to Nathan and stops. TW-TRIAGE-10 returns only PF targets to Nathan. Nathan directly invokes TW-DRAIN-10 for general PF preparation or TW-DRAIN-20 for PF09. A complete READY redline/report package names TW-APPLY-10; BLOCKED preparation stays with its originating preparer for correction, and NO_CHANGE ends without compulsory application. Application success returns the revised PF/report; invalidity returns a diagnostic through Nathan only to the actual preparer. TW-RECORD-10 and TW-RECORD-20 terminate with sections and have no required application bridge. TW-MGMT-10 maintains all eight roles through PE and does not run before ordinary work.

All eight full Notion publications passed title, exact parent, identity and complete-body readback. Static review covered eight relationships and all 18 established alpha cases, supported by a complete diff proving preservation outside the documented identity/name changes and relationship addition. Prior 19 executable fixture checks remain dated original-release evidence; no fixture rerun, model execution, independent review or live trial occurred in this naming change.

## Current Alpha 1 feedback correction

**2026-09-07 — Product Owner-authorized implementation after Alpha Test 1 completion.** This prospective correction supersedes the separate ordinary IA-10 → IA-20 and QA-50 → QA-60 authoring handoffs, including PF10 §2.13’s QA-60 producer clause, only in their invocation/producer mapping. Distinct Audit/Plan substance and Isis review remain. This procedural record does not edit the historical PF source or claim canonical publication. Current selected release is resolved from the GCFPE Membership and Release Register. Historical status and release entries below remain event-time evidence; this section controls the corrected behavior.

QA-10 delivers a substantive paste-ready PF10 build notes addendum: observations, governing obligations, repository-wide impact, necessary action and material limitations. Keep publication administration and proposal framing out of the insert. The complete finding/disposition/evidence map remains in REALITY_AUDIT, linked by QA_READINESS; downstream actors read both full evidence and addendum. With no new entry, save the required CHANGE_AUDIT_TRIAGE as NO_ADDENDUM_NEEDED with supported reason and Audit reference, preserving its downstream identity without inventing insertion text. Publication remains manual and does not create an extra readiness gate.

Selection belongs to the Product Owner. Accept explicit QA step IDs/names, an unambiguous natural-language selection, a complete selection source, or ALL for every step in the exact approved QA Plan. Preserve an already supplied selection. If absent or ambiguous, show available IDs and short names and ask which tasks to run; never assume ALL or choose a ready subset. Author every selected valid task, including dependency-waiting members. Dependency readiness controls execution order, never assignment membership. Preserve blocked/defective entries explicitly. Reuse already-authored instructions as dependencies become ready; QA-110 returns them to QA-100, using QA-90 only for genuinely unissued selected instructions or the exact permitted retry. Never execute an unselected prerequisite or reset attempts.

### One invocation per Audit and Plan authoring phase

IA-10 performs GCF-09 Implementation Audit and then GCF-10 whole-change Implementation Plan in one ordinary invocation in the dedicated IA session. QA-50 performs the independent Kronos QA Audit and QA Plan phases of GCF-21 in one ordinary invocation. Preserve distinct complete Audit and Plan identities, mandatory audit-before-plan order, all source-native content, and existing concise supporting proofs. Neither author approves its own Plan. Success supplies the complete Analyzer handoff for Isis IA-30 or QA-70. Exact-redline denial retains IA-40 or QA-80 as the substantive destination, reached through a separate Analyzer invocation. No Analyzer is inserted between the Audit and Plan phases inside the same IA-10 or QA-50 invocation.

IA-20 and QA-60 remain selected same-author plan-only continuations for a completed valid Audit, including interrupted and legacy work. They are not mandatory extra invocations. On interruption preserve finished phases and resume the first incomplete phase; a substantive source/scope blocker names the actual owner without fabricating approval. Historical logical rows and approvals remain; invocation consolidation adds no stage or permission.


CL-40 delivers each supported PF09 gap as a standalone PF10 build notes addendum, stating required work directly. Include complete task/subtask substance, phase placement, blocking dependency and evidence needs without fabricated allocations. PF10 insertion and PF09 application remain manual/governed. Eligible Glow development implementation CRD candidates are added or updated in the existing list with reread/readback and preserved dispositions. Prompt-ecosystem maintenance belongs in its existing Notion operational case, not that development candidate list. Candidate recording is not authorization to implement that candidate.

Maintain one accurate current-state summary from exact later evidence and explicit Product Owner decisions; preserve older checkpoints as dated history. Alpha Test 1 is complete by the Product Owner's decision. The saved CL-40 result's unavailable-current-board limit remains a separate recorded source limitation; do not invent its resolution. Neither this maintenance nor trial completion activates automation or certifies unexercised paths.


## Final managed PF09 and CRD discovery — Product Owner direction, 2026-09-07

The final-scan extension introduced **CL-40 — Scan for PF09 Gaps and CRD Candidates** as one shared final managed prompt for both Epic and CRD cycles. The same continuing Isis runs it after positive closure, CL-20, and completion or valid disposition of every actually selected post-closure managed author/reviewer branch. Do not add optional maintenance simply to reach the scan. Pending manual PF publication, memo delivery and board administration remain explicit but are not scan prerequisites. Include complete prepared but unpublished material as context. The change remains closed while the final scan is pending or incomplete.

The scan reads complete current PF10, all active parts where applicable, all seven current PF09 phase inventories, the existing CRD candidate list and relevant available change, delivery, QA, RCA, remediation, closure, board, incident, feedback and conversation evidence. Record actual coverage and inaccessible material. Relevant repository inspection is read-only and distinguishes current evidence from the tested historical baseline; the scan does not execute QA or production operations.

Apply the Product Owner's distinction by demonstrated effect, regardless of the originating change class:

- **PF09 row candidates:** gaps in the PF09 records that block successful application development. Explain the concrete development or launch dependency, verify it is absent across the current phase inventories, and supply standalone paste-ready PF10 build notes addenda stating the required PF09 task/subtask content and actual target phase directly, without proposal framing. PF09 publication and product decisions retain their existing manual/governed owners.
- **CRD candidates:** non-launch-blocking gaps, quality improvements or defects with a concrete Glow HD Engine application, repository or development-service implementation target and intended implemented outcome. Nonblocking status alone is insufficient; exclude work already fully owned by PF09/PF10, an active approved change or another implementation record. Prompt/TW/orchestration/handoff/audit/tuning/procedure-only work remains in existing Notion operational tracking. Ambiguous ownership is recorded there as Ambiguous — PO Decision Required. Record their value and evidenced nonblocking basis in the existing `Candidate-CRD-Items-List` in Drive `Glow / Ops / Assessments & Decisions`. Invocation authorizes this bounded noncanonical list update, preserving current IDs, entries, decisions and deferrals; it does not approve or launch a CRD. Do not assign an official CRD ID.

Deduplicate against all PF09 phases, the candidate list and known in-flight, completed or explicitly disposed work. Existing unfinished work is not a missing row. Preserve unresolved impact as unresolved and request only the decisive missing fact; absence of blocking evidence does not establish nonblocking status. A contradiction of accepted closure evidence is reported to the actual closure owner, not hidden as optional work or used to silently rewrite the historical decision.

Save one substantive change-scoped `CYCLE_GAP_SCAN` report in Library, with coverage, findings, dispositions, PF10 build notes addenda for PF09 gaps, actual candidate-list writes and precise incomplete items. Keep audit/proposal commentary outside paste-ready addenda. Re-read the list before modifying it and verify the exact bounded update; uncertain writes are inspected before retry, and repeated scans are idempotent. A supported no-candidate result needs no list write. A missing decisive source, unresolved classification or failed required persistence prevents a COMPLETE claim, without invalidating prior closure.

CL-20, CL-30 and accepted Epic maintenance/revalidation routes provide complete Analyzer handoffs for CL-40 only after their applicable managed work. CL-40 is appraised before invocation and returns terminally without another Analyzer. CL-E-20 still goes through CL-E-30; denial stays with its actual author. MGR-10 tracks managed-cycle completion separately from change closure. CL-40 is terminal to the Product Owner: no next-change selection, kickoff, automatic dispatch or new approval gate. The existing QA task-selection contract, QA attempts, PR/merge controls and automation hold are preserved. The separately reported QA-10 prose and QA-90 selection feedback is not implemented by this change.

GCFPE-20260908.1 has 51 prompts: complete successors for GCFPE-20260907.2's 50 members, plus one GCFPE-ASSESS-10. The Notion register owns actual selection, exact versions and archive evidence. R1 retains 46 historical rows, integrated QA/remediation retains 47, and final-scan/Alpha feedback retains 48 effective rows. The subsequent middleware layer retains 48 logical rows. Preserve Primary core, earlier layers and automation hold. Static review/publication does not establish runtime execution.

## Integrated QA-10 and remediation handoffs — Product Owner correction, 2026-09-06

Apply the approved [in-flight alpha implementation plan](https://app.notion.com/p/3d34590a05eb81c0be47d9d3b0912b71) through the compatible selection in the [Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1). The approved target introduces no new prompt IDs and consolidates four launch entries: QA-15 into QA-10; ESC-20 and ESC-50 into ESC-30; ESC-60 routing into ESC-40. The 53-member baseline therefore has a 49-member successor target, including GCFPE-MGMT-10. Preserve retired and superseded originals intact; the register records actual publication and selection, not this target statement.

Continuing Isis owns QA-10's complete fresh implementation audit, historical PF23 comparison, finding-by-finding triage and readiness. Return separate complete audit and PF10-addendum triage Markdown plus QA_READINESS. A first assessment needs no earlier READY, Guide, QA Plan or Kronos test attempt. Evidenced failure to achieve an applicable approved plan objective yields NOT_READY and a complete Analyzer handoff whose substantive destination is continuing Thoth through ESC-30. Decisive missing evidence yields a precise incomplete assessment and evidence-recovery owner, not a fabricated product failure. Historical discrepancies or future improvements alone do not block; runtime verification properly reserved for QA remains an explicit future obligation. READY supplies the complete Analyzer handoff for same-Isis QA-20 Live QA Guide creation. Independent Kronos Audit then Plan authoring remains one QA-50 invocation, followed through the Analyzer by separate Isis QA Plan review.

Thoth uses ESC-30 to diagnose, select bounded ESC-25 discovery when needed, propose and revise the remedy. Discovery returns to Thoth. When decomposition or Implementation Plan changes are needed, continuing IA prepares the complete pending successor through IA-40 **before** Isis approval. Continuing Isis uses ESC-40 to review the concrete remedy and any exact incorporated IA-authored Plan, return exact redlines to the actual author, or supply approved normal-lane handoffs. A review that expressly satisfies both full contracts can serve as PLAN_REVIEW_ID; a generic remedy approval cannot. Do not duplicate the same completed Plan approval through IA-30. Preserve ordinary initial Plan review, necessary PR/QA Plan/Ops approvals, and actual authors and continuing reviewers. Kronos retains ESC-10 for later actual QA escalation.

Return accepted repair evidence to the originating owner and stage. Ordinary corrections inside approved work retain authority; material changes require revised proposal/necessary Plan preparation and Isis review. Product-objective or exclusion changes retain rescope and PO/Specification approval. There is no fixed remediation-cycle cap, but unexplained repeated failure requires diagnosis; the existing bounded QA retry rule and attempts cannot be reset by relabeling a repair cycle. Preserve uncapped finite QA collections and complete member outcomes.

PF10/PF23 publication remains manual, and standalone addendum preparation does not authorize live PF10 inspection. Pending recording of informational proposals is not an added QA-readiness or QA-progression gate; actual scope decisions and required approvals remain. Exact original prompt/version evidence, PO PR Proceed, complete code review and direct-specific-only agent merge authority are unchanged. Advice follows the actual next workload, including planning and recovery, without fixed PR-30 model/effort or session reconfiguration.

After the corrected release is published, **continuing Isis-49 must rerun revised QA-10 for HDE-CRD-0001 before QA-20**. Preserve the earlier READY, accepted delivery and cancelled QA-15 history. Produce a new complete audit, triage and readiness decision; the earlier decision cannot substitute. This directed rerun is a bounded exception to prospective-only preservation, not authority to cancel other running work or recreate accepted delivery. The operating procedure details the complete boundaries and return rules. Publication and static validation do not prove the rerun occurred or activate automation.

## Product Owner PR merges — controlling correction, 2026-09-05

PR merges are Product Owner manual actions throughout the ordinary flow. No agent may execute a merge unless the Product Owner directly and specifically instructs that agent to merge the identified PR. Proceed, completed work, approved plans/reviews, CI success, deployment authority and general workflow automation never supply that instruction. Do not routinely offer or ask to merge, enable auto-merge, enqueue/schedule a merge or delegate it. A one-PR exception confers no standing automation or authority for other PRs.

PR-30 retains its full engineering review, correction and check responsibilities. At engineering completion it saves MERGE_PENDING, reports the PR ready for Product Owner manual merge and returns control, with a complete populated GCFPE-ASSESS-10 invocation for PR-40, conditional on verified actual merge. It does not remain polling for the manual merge. Missing review/findings/checks remain engineering work, with truthful pending states and same-session recovery.

If later approved engineering in an ordered PR unit depends on an earlier Product Owner merge, preserve the unit as PR_OPEN with that manual dependency, earlier-PR readiness and unfinished later steps. Return a complete populated GCFPE-ASSESS-10 invocation for the same PR-30 session's resume after verified actual merge, retaining Proceed for the unchanged Plan. Do not declare the whole unit complete/MERGE_PENDING, poll for the manual action or send an unfinished unit to PR-40. Planning identifies this dependency. In ordinary user output, PR-30 simply says "Ready to merge" for the ready PR; PR-40 reports its review result. Mention merge evidence or dependencies only when material; do not recite policy or ask merge questions.

The Product Owner's invocation of PR-40 for the supplied lineage is sufficient merge approval. Do not ask for a separate merge confirmation or approval object. Invocation does not merge anything, authorize an agent to merge, establish actual merged state or supply the reviewer's ACCEPT verdict. PR-40 stays read-only, checks native merge evidence, and reports an open/closed-unmerged PR or unavailable evidence as pending for the actual action/evidence. A historically accurate MERGE_PENDING implementation result need not be replaced just to reflect a later PO merge. Keep every PR's actual ordered lineage and unfinished engineering evidence visible.

This direct Product Owner correction governs the overlapping workflow wording; it does not claim to edit PF Canon or change an immutable R1 source. PR-30 has no fixed model/effort; its exact-task destination advice comes from GCFPE-ASSESS-10 and remains human configuration guidance. A manual merge requires no invented agent/model task. Coordinators and relays preserve the manual boundary even where other dispatch is authorized.

## PR completion, assessment delivery and early rescope — 2026-09-05

Apply the current GCFPE shared assessment to the entire destination operation: independent challenge of plans/assumptions, coupled contracts and adverse boundaries, asynchronous review/results, ordinary repairs, evidence and final delivery. A small diff, detailed plan or many passing tests does not remove that work. First identify actual applicable repository/environment model constraints; distinguish difficulty judgment from the human selection that satisfies those constraints. Compare eligible choices using evidence. Do not infer actual configuration or model causality from an incident, automatically maximize all tasks, or prescribe a fixed PR-30 model. PR-20 owns the complete actual PR-30 workload package, including full engineering review and correction ownership, and recommends the Analyzer run. GCFPE-ASSESS-10 owns the destination configuration recommendation after reading that exact completed-plan package.

Every concrete next-agent handoff belongs in the final user-facing response itself. A substantive predecessor returns the complete populated Analyzer invocation, including the complete intended destination-native package, exact attachments, actor/session continuity and Analyzer-run advice. A ready Analyzer returns its destination appraisal and the complete populated destination-native invocation. A block only in a saved artifact is insufficient. Preserve actual prerequisite decisions and dependency state inside the block. PR-20 preserves the Product Owner's exact-plan decision and the same continuing engineering session. Preserve AWAITING_PO_PROCEED. The Analyzer may appraise the complete PR-30 package before the reserved action-time Product Owner invocation; the Product Owner then invokes the returned native PR-30 block to supply the original exact-Plan Proceed. Invent no separate approval object or approval step. Any genuinely separate pending prerequisite must still be satisfied and evidenced. Analyzer appraisal supplies no substantive approval. Missing or invalid package content cannot be bypassed by invoking the worker directly. Manual-only actions remain human prerequisites and do not require an invented prompt.

PR-30 owns applicable code/security review through substantive result consumption and finding disposition, correction and review coverage of changed published code. Read complete relevant reviews, threads and summary comments; Completed/COMMENTED or a reaction alone does not prove success, and formal APPROVED is not universally required. PR_OPEN is intermediate. MERGE_PENDING requires engineering review completion, dispositioned findings and required checks passed or an actual scoped authorized waiver. Preserve failed CI and waiver scope; CI waiver never waives code/security review. Continue authorized work or report a precise interruption with the same owner's resume route. Later PR-40 lineage review cannot substitute for unfinished engineering review. Keep merging with the Product Owner under the controlling merge-action correction above; avoid a global SHA-only rerun gate.

RS-10 accepts a substantiated PR boundary finding during detailed planning, implementation or engineering review. Carry the affected instruction and approved upstream lineage; detailed Plan, result and PR references are included only when they exist, with drafts and not-yet-produced artifacts identified truthfully. Reuse a matching proposal's actual state. The assigned PR finding author gains no IA approval authority. Ordinary in-scope defects and complexity alone stay in the existing work. Approved bounded rescope retains same-IA review, Product Owner manual PF10 disposition, any changed whole-Plan Isis review, revised instructions and changed detailed-plan PO Proceed; changed Specification intent retains its proper formation owners. If approved whole-change Plan content changes without an existing exact Isis correction, RS-20 routes the approved base/rescope and actual manual disposition to the same Isis through IA-30; its exact correction goes to the same IA through IA-40 and the complete pending successor returns to IA-30 for normal review. Reuse a valid existing correction; omit this loop when that Plan content is unchanged. Other lanes retain their native escalation routes. For a remediation-origin Plan successor under the 2026-09-06 integrated QA-10 correction, use the explicit IA-40 pre-approval preparation intake and the same-Isis ESC-40 combined review when it satisfies the full exact Implementation Plan review contract. Do not add the older IA-30 instruction/approval loop merely to reapprove that same completed design. Actual rescope and Product Owner scope decisions remain required where applicable.

GCFPE-MGMT-10 verifies the actual prompt version and checkpoint, separates reported facts from observed evidence and later state, and tests review-result consumption, final-response delivery, policy-constrained advice and pre-implementation rescope/re-entry. Preserve the incident until its stated observed-behavior condition is met. This maintenance guidance grants no underlying PR, PF, production, review-message, merge or automation authority.


## Mandatory PR and PF-document authority boundaries — Product Owner, 2026-09-05

**Outside an authorized Glow development cycle, agents are expressly forbidden to open a pull request or directly edit any PF document unless the Product Owner explicitly instructs that exact action.** This applies to all PF documents, not only PF10, and to draft PRs as well as ready-for-review PRs.

Within an authorized development cycle, the assigned actor must still have authority for the exact action, document, artifact and write scope under the existing flow. Merely working on Glow, performing maintenance, repairing prompts, auditing skills, documenting requirements or executing an establishment checklist is not a development invocation. Do not relabel maintenance as development or infer permission from tool availability, draft status, successful checks, model recommendations or a broad “proceed.”

PF-document protection covers direct edits, append operations, replacement, renumbering, version changes and publication of native documents, Markdown counterparts and repository mirrors. Permission for one PF document or surface does not authorize another. General permission to update operational documentation does not include PF documents. Where no development authority applies, the Product Owner's explicit instruction must identify the PF document and requested direct mutation.

**PF10 addenda are delivered only as standalone documents for the Product Owner to insert manually.** A request to prepare an addendum does not authorize opening or inspecting the live PF10, appending it, choosing its final number, editing the canonical document, replacing its Markdown counterpart or publishing a repository mirror. The Product Owner handles numbering/insertion and canonical adoption. Respect any separately explicit instruction for an exact PF action; do not infer one from the addendum request.

These are controlling operational boundaries, not permission to perform a PR or PF mutation. Preserve already granted authority within its exact scope; no new approval-token system or repeated approval request is required. If authority for a proposed action is absent, complete the permitted draft/report work and report the blocked action. Record an actual violation in the existing Error Log.

Incident 017 records the unauthorized PR and PF10 publication. PR #398 is closed unmerged. Its former CI/integration instruction is withdrawn; no reopen, replacement PR, retry, merge or further PF edit is authorized by this correction. The earlier PR/PF edits were unauthorized when performed. The Product Owner has now directed use of the PF10 content already present and canceled the separate draft; retain the existing content without further editing. This subsequent disposition does not retroactively authorize the violation. Use the [Error Log](https://app.notion.com/p/3d14590a05eb81458dadf3fabd021b97) and current [establishment checklist](https://app.notion.com/p/3d24590a05eb81059255fa60ed15ee7b) for disposition. Alpha continues.

## Workflow-only canon, QA collections and predecessor assessment — 2026-09-05

The Product Owner requires reusable GCFPE prompts to embed workflow canon only. Roles, sequencing, action boundaries, input/output structure, decisions, lineage, recovery and handoffs may be baked in. Subject-matter policy and meanings must be read and applied from their current authoritative sources during execution. Classify clauses by their function, including within mixed workflow/technical documents. Preserve approved runtime artifact versions. A subject-matter canon update should not force a prompt-policy rewrite; a workflow-contract change may legitimately do so. Lifecycle and trial eligibility are resolved from their owning register/checklist rather than copied as permanent prompt facts.

Every concrete substantive transition requires GCFPE-ASSESS-10, including planning, review, revision, recovery and continuing-session work. The predecessor determines the eligible destination, prepares complete actual native inputs and recommends the Analyzer run. The Analyzer reads the complete destination and decisive package sources before recommending the destination's human configuration. Preserve exact destination, source/input/plan versions or collection membership, approvals, prerequisites, actors, attempts, capabilities and unresolved facts. Assess all eight workload dimensions in the middleware contract above; distinguish volume from difficulty without fixed destination tables or automatic maximums.

The Analyzer's actual-work destination appraisal takes precedence over provisional entry guidance. PR-30 has no fixed model or reasoning recommendation. PR-10 and DOC-10 prepare complete PR-20 planning packages and recommend the Analyzer; PR-20 prepares the completed PR-30 package and recommends the Analyzer, which accounts for applicable repository policy. Material package, authority, scope, capability or appraisal changes require reassessment. Preserve the exact package and assessment without substituting headers. Unknown options remain explicit. Unknown account-picker details alone do not invalidate supported dated advice; missing essential capability or an incomplete, contradictory or ineligible package prevents a runnable destination. The human selects configuration; no self-switch, restart, hidden dispatch or session replacement follows.

QA-90, QA-100 and QA-110 accept arbitrary finite caller-selected collections in one invocation through their plural fields or complete retrievable collection sources, preserving singular aliases. There is no artificial QA-task count cap or one-user-invocation-per-ID requirement. Every member retains approved scope, Plan/review, step/task, environment, evidence, attempts, reviewer and return. Dependency-ready authorized work may proceed while blocked/deferred members remain explicit. Keep complete membership and task/result/review mappings through internal chunks or resumable partial results; do not truncate, merge identities, reset retries or infer a whole-run PASS. Scope, execution concurrency, retry limits and evidence-file packaging rules remain separate from task cardinality.

Repository provenance requires actual installed procedure/schema/writer discovery. A named path or historical candidate does not prove installation. If unavailable, preserve full usage and task/result/attempt mappings in permitted outputs, identify persistence as pending and its authorized owner, and continue otherwise authorized work under the existing non-gating fallback. Do not invent fields, successful tooling, extra actual invocations or observed model values. Physical installation remains a separate authorized repository task; this guidance does not close that establishment item.

GCFPE-MGMT-10 applies PE Analyze's substantive quality discipline to the whole ecosystem: clarity, efficiency, ambiguity and effectiveness; material risk-to-mechanism-to-fix reasoning; complete directive/change/preservation traceability; minimal usable inputs; full-source coverage; actual-work variability; and meaningful success/failure/return checks. Consequential shared-contract changes receive a real separate qualified check of complete candidates and affected integrations. Source review, static walkthrough, executable checks, live execution and user confirmation remain distinct evidence. Historical PE Analyze model bands, arbitrary risk quotas, registry IDs and obsolete prompt mirrors are not adopted. The current selected manager in the register governs execution of this procedure.

These are current Product Owner directions. Earlier dated events and version notes remain historical evidence. Existing approvals, canonical writers, preservation and PR/PF authority boundaries continue to apply.

## GCFPE establishment and source-reference history — 2026-09-05

The Product Owner authorized implementation of the GCFPE Alpha Establishment Checklist and then required immediate correction of static file locators throughout the complete prompt set. GCFPE remains alpha; the checklist precedes Product Owner-initiated CRD testing. Its current work status and selected release are recorded in the [Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1) and [Flow Index](https://app.notion.com/p/3cc4590a05eb8101b5ded32c12616eb6). Earlier static-readiness statements describe their dated assessment, not compliance with this newly identified source-resolution defect.

**Prompt source locators are versionless names plus verified directory paths only.** Static file links are strictly forbidden within complete prompt bodies and their human model headers. This includes raw URLs, Markdown/rich-text hyperlinks, Notion page/file mentions, bookmarks/embeds and opaque provider IDs used as locator substitutes. Do not hardcode a referenced source's version or date suffix. The prompt's own version, stable ID, schema/contract identifiers and exact human model labels remain metadata; an actual directory name is preserved even if it contains a historical number.

These names are logical search identities; existing stored files may retain version suffixes. At execution, find the named resource in its directory, inspect the complete source and establish its current controlled selection. Search ordering or modification time alone is insufficient. Preserve the accepted R1 authority, and preserve exact approved/in-flight artifact lineage supplied separately as runtime data. Dynamic discovery is not permission to replace approved inputs. If an authoritative match is absent or ambiguous, resolve that concrete issue without guessing a provider ID or inventing a path.

Actual resolved versions, source identities and returned links belong in runtime evidence, usage records, operational catalogs or reports outside reusable prompt text. They must not be copied back into source-locator instructions. These procedural documents may retain navigational/evidence links; they must not contain competing complete prompt bodies.

Verified directories: PF Canon/reference resources in Drive `Glow / Core Docs / PFCanon`; general/model guidance in Drive `Glow / Ops`; manager delegation guidance in Drive `Glow / Prompts`; Authority Register and Contract Matrix in Library `/Glow HDE 3.0`; development prompt families in Notion `AI Prompts / HDE Change Flow`, `HDE IA`, `HDE QA`, `Escalation` and `HDE TW`. The register gives the exact current membership and directory mapping. Prompt navigation inside a body uses stable prompt name and directory; exact page links remain in the external catalog.

The adjacent GCFPE-MGMT-10 management prompt, resolved through the [current selection register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1), executes one request from intake through investigation, whole-ecosystem impact review, coordinated repair, proportionate quality control, supported publication/readback, documentation and resume. Review every development member and managed auxiliary for each member change or addition, record affected/unaffected reasons, and update related contracts together. Check locators throughout every changed complete body and header. Do not publish isolated incompatible counterparts or recreate the repeated global-preflight loop. Canonical/independent decision boundaries remain intact.

Repository prompt-use provenance captures the exact versions actually used for a spec/component/work unit, retaining multiple uses and explicit unknowns. Read-only roles carry this metadata in permitted existing outputs; only an already authorized repository writer persists it under the repository procedure. This creates no new approval token, extra Specification section, or post-closure prerequisite. Keep records in the repository, complete reusable development/management prompts in Notion, temporary repair prompts in Library, and lasting noncanonical procedures/authorized reference reports in Drive. An actual Notion removal moves the original intact into the existing appropriate archive; no delete, trash, clear or copy-then-delete substitute.

GCFPE headers are provisional fallbacks; actual-work predecessor advice is primary, and PR-30 has no fixed model or reasoning recommendation. The receiving agent does not self-reconfigure. The existing monthly model review remains read-only at its existing schedule; findings enter this management process, with no duplicate automation. A text fix, static walkthrough, metadata example or successful save is not proof of runtime behavior. Incidents retain their actual closure conditions.

This current policy controls over earlier conflicting procedural wording. The complete [establishment checklist](https://app.notion.com/p/3d24590a05eb81059255fa60ed15ee7b) and [Error Log](https://app.notion.com/p/3d14590a05eb81458dadf3fabd021b97) record actual completion and incident 015. No activation or CRD testing is authorized by this publication.

## Product Owner clarification — prompt categories, 2026-09-05

**Flow prompts being repaired:** The reusable prompts that form the Glow development flow belong in Notion. Their published complete bodies and model headers must not be published to Drive.

**Temporary repair-process prompts:** One-off review, validation, repair and handoff prompts used to carry out this repair project may be stored in ChatGPT Library. They are not part of the reusable development flow and do not require Notion publication merely because they are prompts. This includes the temporary Astra validation/optimization assignment.

**Reports and reference guidelines:** Continue to use Drive for these documents, with appropriate Notion links.

This clarification narrows the earlier blanket Notion-only wording to the flow prompts being repaired. It does not prohibit Library storage for temporary repair-process prompts. The previous overbroad interpretation and relocation of the temporary handoff were unnecessary to satisfy this distinction. This note records the clarification only: do not move, restore, republish or rewrite existing prompt bodies as a consequence. Existing locations, history, lifecycle and execution state remain unchanged. The requirement to move any removed Notion item intact into its existing archive remains in force.


## Controlling prompt-storage policy — Product Owner correction, 2026-09-05

**Notion is the sole persistent publication home and editable source of truth for complete prompt bodies, including their human operator model headers. Do not publish, mirror, back up or maintain prompt bodies in Google Drive.** Reports, assessments and noncanonical reference guidelines remain Markdown documents in Drive, linked from Notion. They may describe or link prompts, but must not become alternate prompt-body repositories.

Temporary local authoring is permitted. Existing Library drafts are unpublished historical/staging evidence, not published prompts and not a substitute for Notion publication. Do not create a new persistent Library prompt collection or treat a downloadable file as publication. Publish the complete body in the appropriate existing Notion prompt hierarchy and point the Flow Index to that page. Keep drafts clearly labeled as drafts; publication alone does not establish approval, activation or runtime success.

This explicit prompt-body exception overrides earlier general DURABLE_DRIVE, EPHEMERAL_LIBRARY and CONTROL_NOTION wording wherever that wording routes prompt bodies elsewhere or limits Notion to pointers only. It does not migrate historical files automatically. Preserve prior evidence. Any Notion item removed from active use must move intact into the already existing appropriate Notion archive, never be deleted, trashed or cleared.


Version: 1.11.0

Status: Active noncanonical operational reference

Owner: Product Owner; maintained by the Managing Prompt Engineer

Effective: 2026-09-08 UTC

Model appraisal reviewed: 2026-09-05 UTC against official Work guidance and current runtime exposure; operator-header boundary corrected by the Product Owner.

Editable source: This raw UTF-8 Markdown file in Glow / Ops is the sole current editable source. The prior native Doc is historical evidence preserved in Docs Archive.

Scope: Any session that creates, repairs, reviews, or hands off a prompt for another execution session.

Authority boundary: This guide supplements controlling canon, project prompt contracts, and exact Product Owner directives. It cannot amend or override them.

## Purpose

This guide supports usable prompts: assign a clear task to the right actor, provide the needed sources, perform proportional checks, deliver the complete prompt with its model recommendation, and improve it through actual use.

For Glow HDE Prompt Repair, [Revised Delivery Strategy](https://drive.google.com/file/d/1FFRtkj1NozqgXy2KiTOMOMhpiVscMh1E/view) and the Product Owner's 2026-09-05 correction require every in-scope prompt to be reviewed, every required prompt to be repaired, and both complete flows to be reconciled before any trial. Development approvals, PF Canon permissions and genuine role independence remain.

## Glow complete-flow readiness requirement

The complete Epic and CRD process is the release unit, including formation, IA/Plan, PR/Ops, QA, escalation, revision/return paths, closure, post-closure work and required utilities. Review/dispose of every existing inventory entry and repair all required bodies and interfaces. Internal drafting groups are not trial releases.

No individual prompt is Ready for trial while the whole-flow review/repair is incomplete. This includes offline, synthetic and role-bound trials. Use Draft — whole-flow repair incomplete — not ready for trial. Static authoring checks and persistence verification may continue; prompt execution waits for the complete version set and one integrated compatibility review. The rejected CF-C-30 trial handoff is withdrawn.

This requirement adds complete coverage, not repeated audit ceremony. Retain proportional checks, accepted evidence, direct authorized repairs and the simple defect loop. After whole-flow readiness is established, observed defects are corrected and retested with their affected interfaces. No model recommendation overrides this readiness condition.

## Authority and source boundary

Apply sources in this order:

1. The Product Owner’s exact current directive.

2. Applicable PF Canon and active project prompt or workflow contracts.

3. Prompt Selection and Session Delegation Protocol, current active version, for launch and session handoff.

4. This noncanonical reference for general method and quality control.

Apply an explicit later Product Owner directive within its stated scope and record which earlier operational rule it supersedes. Escalate only a material unresolved conflict to the actual decision owner; do not request the same adopted policy decision again.

### Historical PF10 research finding

The original guide's repository source [PF10-HDE-Build-Notes-v12.9.5.md](https://github.com/amthorn78/glow-hdengine-v2/blob/0f8ff03960dace54b0faae835fdcc51111b4ec3e/docs/pfcanon/PF10-HDE-Build-Notes-v12.9.5.md) at commit 0f8ff03960dace54b0faae835fdcc51111b4ec3e was checked directly. Addendum 2.2, section 5, Living prompt-flow map control, requires a human-readable Notion map with runtime sequence, prompt identity, actor, inputs and outputs, decision ownership, approval semantics, lifecycle state, conflicts, and controlling-artifact links. Section 5.3 requires updates when a prompt is proposed, contracted, authored, reviewed, repaired, published, activated, held, superseded, retired, or replaced.

The inspected PF10 source did not establish the exact model-header wording. The current explicit Product Owner clarification and Selection Protocol require predecessor assessment of actual next work, applicable provisional fallback headers and PR-30's no-fixed-recommendation exception. Do not attribute this wording to PF10 or turn it into receiving-agent model control.

## Operator model guidance and the PR-30 exception

For GCFPE, the substantive predecessor recommends the Analyzer and carries complete actual destination-native inputs. The Analyzer supplies the primary human destination configuration recommendation. Reusable headers retain only minimum legitimate first/direct/recovery-entry guidance. PR-30 has no fixed model or reasoning recommendation: PR-20 packages its actual completed Plan for the Analyzer. Never copy runtime facts into reusable headers.

Keep advice portable with the existing handoff and exact artifact lineage. An adjacent launch line reflects the applicable actual-task assessment, which may differ from the fallback; it must not falsely claim to match or replace that fallback. A legitimate first, direct or recovery entry without a predecessor may use clearly provisional launch guidance from available evidence. Missing advice in an ordinary transition does not permit bypassing the Analyzer. If model options cannot be verified, name that advisory limitation and the needed capabilities without inventing a label or a new execution prerequisite.

The human chooses the available configuration. Advice does not instruct the receiving agent to inspect, switch, restart or reconfigure itself, reassign a workflow actor, or replace a continuing session. Internal subagent assistance follows the task-specific rule above and needs no separate generic approval merely because it is internal assistance. Actual tools, authority and observed configuration remain separate. Refresh a current appraisal only for a meaningful capability or evidence change; materially revised work needs a revised task assessment.

Outside GCFPE, retain an applicable native prompt's human header policy unless its owner changes it. This GCFPE correction does not silently revise other ecosystems.
## Model-availability evidence boundary — 2026-09-05

Published Work support, the tools/models exposed in the authoring runtime, and another account's actual model picker are different evidence. A ready recommendation names the exact surface, model, effort, task rationale, appraisal date and official source, and states any account-specific uncertainty. Use available evidence; do not demand an unexposed picker-inspection operation or invent account availability. An unknown account-specific picker alone is not a prompt-authoring or publication blocker. A genuinely unavailable essential task capability or an actual operator launch choice is handled at that specific action. The receiving agent neither inspects nor reconfigures itself because of the header. Reuse a still-current appraisal; do not repeat research for each prompt or add a release gate.

## Complete prompt handoff

Every ready-to-send prompt or prompt link must be delivered as a pair:

1. A substantive predecessor's complete populated Analyzer invocation carries the entire actual destination-native package and Analyzer-run recommendation. The ready Analyzer returns its appraisal and complete destination-native invocation. True entries use provisional advice with PR-30's exception; true terminals return to the Product Owner.

2. The complete executable prompt or its direct durable link.

Use this exact launch-line form:

Launch with: [actual supported session surface] — [exact model] — [thinking level]

The substantive predecessor owns the eligible destination, complete actual package and Analyzer-run recommendation. The Analyzer owns the destination appraisal. The reusable-prompt author owns only applicable provisional entry guidance. It must replace every placeholder with an exact task-fit recommendation supported by current intended-surface evidence, with account-specific uncertainty stated under the evidence boundary above. The Product Owner decides whether to accept the recommendation and launches the session.

- Bind each recommendation to its own operation: predecessor advice for the Analyzer, Analyzer advice for the substantive destination. Preserve exact package lineage and keep provisional entry guidance separate.

- An adjacent launch line carries the applicable actual-task advice; state when it supersedes the provisional fallback.

- Do not use relative labels such as latest, best, strongest, automatic, default, or whatever is available.

- Include exact model/effort and appraisal basis in available task-specific advice; retain applicable provisional fallback headers, with no fixed recommendation in PR-30. Report genuine uncertainty rather than inventing an option.

- Disclose an unverified account-specific option and research a suitable available alternative when needed. Do not invent availability or require the receiving agent to inspect/reconfigure itself. An indispensable missing task capability or actual launch decision blocks execution; all substantive input, eligibility, authority and mandatory middleware requirements remain binding.

## Launch-configuration research

### Required research before recommendation

1. Verify published support for the intended ChatGPT surface and record the relevant runtime exposure actually observable. State any unobserved account-picker boundary; do not require an unavailable inspection mechanism.

2. Reuse the current documented appraisal when it still applies. Check current official OpenAI guidance when a release, retirement, availability change, consequential result, stale evidence, or a non-obvious choice requires fresh appraisal. Each delivery requires a valid recommendation, not a new model research project.

3. Classify the task by accuracy requirement, complexity, connected-app or computer-use needs, context volume, coding or research load, latency and cost sensitivity, and whether independent decomposition is both useful and permitted.

4. Optimize for accuracy first. After quality is demonstrated, choose a faster or less costly model only when it still satisfies the task.

5. Record exact display name, effort, actual-work rationale and appraisal date/source in the existing handoff, with its input lineage. Use applicable provisional headers only as fallbacks.

### Current model-role guide

This is a dated appraisal, refreshed at delivery. Model choice is distinct from surface access, tools, reasoning effort, and authority to reassign or dispatch workflow actors. Internal subagents may support the authorized task under the clarification above.

| Model | Current selection role |
|---|---|
| GPT-6 Astra (`gpt-6-astra`; picker may display Astra) | First candidate for the hardest tasks spanning code, apps, and research. |
| GPT-5.6 Sol | Complex analysis and polished output where it meets the quality target. |
| GPT-5.6 Terra | Everyday reasoning and tool work. |
| GPT-5.6 Luna | Clear, repeatable extraction, transformation, and structured summaries. |

Roles are grounded in [ChatGPT Work model guidance](https://learn.chatgpt.com/docs/models), checked 2026-09-05. Sol is the strongest GPT-5.6 option; it is no longer the overall flagship in this appraisal.

**Glow selection policy:** Establish the actual task’s quality and capability requirements first. Include Astra in the candidate comparison for the hardest governance, architecture, recovery, prompt/skill design and multi-system work. Compare eligible less costly configurations where they can meet the same requirements. This is task-fit judgment, not a Glow-specific benchmark; a task category alone does not assign a model or reasoning level.

**Availability evidence:** The Product Owner reported Astra released, and this Work runtime advertises `gpt-6-astra`. That establishes current-session runtime exposure. It does not establish every model/effort pairing in another session, client, plan, or API account. Record the actual evidence source and any remaining uncertainty for the intended launch surface.

**Evaluation discipline:** Define acceptance before comparison. Use identical frozen, non-mutating cases and score completeness, source identity, instruction adherence, finding classification, payload portability, recovery correctness, and unnecessary approval pauses. A model switch grants no authority and does not replace an independent reviewer. Never test models as competing live writers.

[OpenAI's selection method](https://developers.openai.com/api/docs/guides/model-selection) prioritizes an explicit accuracy target before comparing faster or less costly choices. For Glow, record elapsed time, usage when exposed, retries, and human repair per accepted result. Do not claim Astra is cheaper or faster for this workflow from release claims or per-token pricing alone.

### Astra-specific authoring appraisal

The [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model) describes stronger instruction following, sensitivity to conflicting instructions, more clarification, and possible over-testing. Apply these operational controls when preparing work:

- State the outcome and existing authorization. Complete permitted work before requesting a decision; reserve stops for material missing input, authority, or capability.
- Identify instruction conflicts precisely. Name the controlling source when it changes the action; do not invent approval requirements.
- Distinguish prompt-creation ownership, internal subagent assistance and workflow-actor delegation. Use necessary or materially useful internal subagents within the authorized task, with defined output ownership and verification. Choosing a model does not expand task scope or transfer approval authority.
- Define proportional verification and completion so testing ends when required evidence is sufficient.
- Specify the output form and plain-language style.
- Keep operative task controls distinct from the internal operator model header. The header recommends a launch choice to the human; the receiving agent must not try to change its own model.

These controls guide future authoring. They do not revise a frozen prompt, approved changeset, accepted audit, or running session.

### Thinking-level guide

Select an exact effort exposed for the chosen model and surface. Work uses Light where CLI uses Low; Medium supports ordinary depth; High or Extra High supports harder reasoning. Max is a deeper single-task option where exposed. Ultra delegates to subagents. Combinations vary by account and rollout. See [current Work controls](https://learn.chatgpt.com/docs/models).

- Select the least effort that reliably meets acceptance criteria. Never deliver `default`, `automatic`, or a relative label.
- A sole-writer requirement does not imply single-agent analysis or fix the model/effort. Evaluate the actual preflight or other task; internal read-only checks can support one responsible author and writer.
- Use Max only when available and the unresolved problem justifies more depth and usage. Do not automatically select the maximum.
- Recommend Ultra when meaningful independent work benefits the complete task and the responsible agent can integrate and verify it while preserving output ownership. Necessary or materially useful internal subagents are permitted within the assignment; do not require another generic permission or infer a ban from the prohibition on delegating prompt creation. If a genuine task-specific or capability limit prevents that work, state the exact limit and recommend the best supported alternative.
- Use the user-facing `Extra High` label in the handoff, rather than the runtime identifier `xhigh`.
- Do not infer that a Work model or effort is available in ordinary Chat from API or runtime exposure.

### Surface guide

- Use Work when the complete assignment needs capabilities, state management, execution or artifact handling established for Work and not established for the intended Chat route. Sustained multistep implementation and verification are typical candidates.

- Consider Chat for bounded analysis, drafting, research or connected-app operations when that exact route has the required source access, tools and deliverable capability. An app connection alone does not require Work or prove Chat can complete the task. Verify the whole operation and preserve explicitly retired routes; the Operations Hub records the separate Chat Pro 6 observations and PF10 Condense disposition.

- Use local CLI only under the separate local-client eligibility and authority controls. Never silently substitute CLI for Chat or Work, and still identify the exact model or profile and effort in the launch instruction.

Work terminal execution is an eligible environment for authorized Glow HDE development, DevOps and QA when the task’s required capabilities are available. Resolve the current glow-hde-devops skill, Preflight in Notion AI Prompts / DevOps, and NON-CANONICAL-HDE-Workstation-Readiness-and-Operations in Drive Glow / Ops / Access & Infrastructure. Keep changing machine details and credentials out of reusable prompt headers. State the execution environment separately from model advice, and carry material gaps and recovery through the existing handoff. Apply the Operating Procedure’s bounded maintenance rules when setup changes leave workflow contracts unchanged. This does not promise unrestricted platform parity or authorize otherwise unassigned production effects.

## General prompt-creation flow

1. Identify the outcome, permitted actor, necessary inputs, affected handoff, and authority for any writes. Execute current-session work directly when authorized; use another session only for an actual role, workload or independence need.
2. Reuse accepted sources and prompt bodies. For an initial workflow repair, review every in-scope prompt and every required transition; record retained/repaired/superseded dispositions in the existing Index. For later individual defects, read the affected prompt, contract and neighboring handoff. Expand source retrieval only for a concrete question.
3. Draft the complete executable prompt. State its task, inputs, outputs, role boundaries, consequential stop conditions and resume/return instruction. Do not substitute a prompt that asks for another prompt.
4. Check the actual operations required. Confirm the target and callable capability. Where read-only permission inspection is unavailable, record permission as an execution condition; do not make impossible advance certification a prerequisite for finishing the task.
5. Review correct actor/inputs, output/handoff, authority and operability. For Glow Prompt Repair, finish the complete prompt set and one integrated interface review before any representative execution. Then run integrated cases in the appropriate roles and check corrected failure/return paths. Additional checks must resolve a concrete defect or material risk.
6. For GCFPE, verify mandatory Analyzer handoffs at every concrete substantive transition, including planning and same-session returns. The predecessor carries the complete native package and recommends the Analyzer; the Analyzer recommends and returns the destination invocation. Retain only legitimate provisional entry guidance and PR-30's no-fixed-recommendation exception.
7. Record truthful status: Draft — whole-flow repair incomplete; Ready for integrated trial only after the complete-flow gate; Used successfully only for executed behavior; or Blocked/Rejected. A saved file or isolated static review does not establish trial readiness. Preserve versions and use the existing Index and Error Log.
8. During use, repair the smallest observed cause, return the complete corrected prompt and resume point, and retest the failed case. Check adjacent prompts only when their contract changes.

For ordinary Glow Prompt Repair edits, separate audit, inactive-publication and publication-postflight sessions are no longer default prerequisites. Required development reviewers and genuinely consequential authority decisions remain in their proper sessions. A representative test failure returns to the existing maker, not automatically to a new audit cycle.

## Minimum executable prompt anatomy

- Role and exact session identity, when governed.

- One direct objective that assigns the real task rather than asking the receiver to write another prompt.

- Authoritative source inputs located by versionless names and verified directory paths; preserve actual resolved identities and approved artifact versions separately in runtime input/evidence records.

- Scope, mutation boundary, output identity, concurrency ownership, and prohibited actions.

- Required procedure and decision rules, including how to handle contradictions and unknowns.

- Deliverables, evidence, validation, readback, and rollback or compensation requirements.

- Genuine stop conditions and a precise return contract.

- Applicable provisional true-entry guidance or PR-30's explicit exception, and the responsibility-appropriate final response: complete Analyzer invocation from the predecessor, complete native invocation from the ready Analyzer, or true terminal return to the Product Owner.

## Launch-blocking readiness gate

A prompt is ready only when every applicable item passes:

- The prompt assigns the executable task, not prompt-creation recursion.

- The correct actor and session boundaries are explicit.

- Inputs needed for this task are accessible and identified. Retrieve changing target state when the operation needs it; unrelated source freshness is not a launch gate.

- Authority, writes, prohibited actions, outputs, and stop conditions are unambiguous.

- Required operations are supported, targets are identified, and consequential failures have a realistic handling path. Unavailable read-only permission inspection is explicitly an execution condition, not an assumed permission denial or an impossible advance-proof gate.

- No unresolved placeholder, invented identity, stale relative label, or ambient-context dependency remains.

- The proportional review has passed. For Glow Prompt Repair, every in-scope prompt has been reviewed/disposed, every required body repaired, and the complete Epic/CRD flows reconciled before any trial readiness claim. State separately what has actually executed.

- The status distinguishes Draft — whole-flow repair incomplete, Ready for integrated trial, Used successfully, Blocked or Rejected. A subgroup is not eligible for independent trial release; runtime success remains a separate evidence claim.

Configuration advice supplies no substantive approval. Mandatory GCFPE middleware, complete native packages, exact actor/session continuity, manual prerequisites and truthful status are required contracts. Unknown account-picker details alone are not a publication blocker when supported dated advice and limits remain. Missing essential capability or incomplete, contradictory or ineligible input prevents a runnable destination. PR-30's absence of fixed advice is compliant. Missing middleware is drift requiring repair before compatible selection.

## Lifecycle and archival control

Prompt lifecycle states may include proposed, contracted, authored, reviewed, repaired, published, activated, held, superseded, retired, rejected, or replaced. Preserve exact identities and lineage at every transition.

A lifecycle decision to retire, supersede, or reject a prompt does not itself authorize destructive disposition.

- Any Notion page or database removed from an active location must be moved intact to an existing scope-appropriate Notion archive. Deletion, trash, content erasure, workspace-root relocation, or an improvised new archive is not an archival substitute.

- For Glow HDE Prompt Repair prompt pages, use [04 Archived Prompt Versions](https://app.notion.com/p/3c94590a05eb811cb145cd010e3b3fcf), page 3c94590a-05eb-811c-b145-cd010e3b3fcf, unless the Product Owner explicitly selects another existing scope-appropriate archive.

- Preserve stable identity, title, content, and relevant lineage. Verify absence from the former active parent, presence under the archive, and integrity by fetching the moved item.

- Identify the existing destination and available move/readback operations before an authorized move. If read-only permission inspection is unavailable, the authorized operation and readback establish its result. A definite denial stops that action; an uncertain outcome requires inspection before retry. Preserve the item and report an exact manual step if needed. Never delete or improvise another archive.

- Rejected prompts are not launchable, repairable, or reusable unless the Product Owner later issues an exact instruction.

## Failure handling and escalation

- Missing or unsupported advice: complete useful appraisal and state limits. Repair missing GCFPE Analyzer transport without changing the substantive destination or package. Missing decisive inputs, eligibility or essential capabilities require ASSESSMENT_INCOMPLETE with exact recovery owner/action and no fabricated invocation. Unknown account-picker details alone do not defeat supported dated advice.

- Recommended model unavailable: research a verified suitable alternative for the operator, update the actual-task handoff and applicable fallback if its general basis changed, and explain the change. Do not claim or instruct agent self-switching.

- A required operation that is actually unavailable blocks that operation. Complete other authorized work and provide the exact supported/manual alternative where possible. Unobservable advance permission is an execution condition, not proof of missing capability. Do not promise guaranteed rollback.

- A material unresolved authority or source conflict goes to its decision owner. Apply explicit adopted operational revisions within their scope without asking for the same authorization again.

- Prompt rejected by the Product Owner: mark rejected, remove it from active presentation through authorized nondestructive disposition, and preserve evidence.

## Illustrative launch recommendations

These are dated Work examples. Verify the actual pairing before delivery.

| Task | Example operator-header selection |
|---|---|
| Difficult governed preflight or recovery design with one writer | Launch with: Work — GPT-6 Astra — Extra High |
| Complex analysis already shown adequate on Sol | Launch with: Work — GPT-5.6 Sol — Medium |
| Routine bounded tool work | Launch with: Work — GPT-5.6 Terra — Light |

For Luna, Max, Ultra, ordinary Chat, or another surface, select an exact exposed combination after appraisal; do not extrapolate a Work example.

Historical example only: the earlier U1 corrective-preflight Astra recommendation is retained in prior versions. It is not a current task or launch instruction. Current next work comes from the Repair Plan and its complete-flow readiness requirement.

## Maintenance

- Review immediately after a verified release, retirement, availability change, or consequential evaluation failure; do not wait for the monthly review.
- Keep the established monthly review read-only. Resolve current Markdown sources through the Glow Operations Hub, compare current official guidance, and report proposed corrections.
- Record review date, model/runtime identity, surface, availability evidence, exact effort, task rationale, evaluation status and next review trigger. Use source names and directories in prompt headers; actual source links and resolved versions belong in the separate appraisal evidence. Refresh unlaunched handoffs prospectively and preserve running work.

- Review this guide when the OpenAI model catalog, Work capabilities, Prompt Selection and Session Delegation Protocol, PF10 prompt-flow controls, or relevant workspace governance changes.

- Review it after any omitted or incorrect launch recommendation, wrong-surface launch, hidden-session failure, prompt-recursion failure, or destructive archival attempt.

- Update the version, effective date, source notes, and change log for every substantive revision.

- Because this is noncanonical, route any desired PF10 or other PF Canon change through a separately authorized canonical change.

## Source references

Current operational protocol: [Prompt Selection and Session Delegation Protocol](https://drive.google.com/file/d/10EKsqzg27jtXiKDzmKaZtZvgl_LgNgjP/view?usp=drivesdk) (resolve the currently selected version through the Operations Hub)

- [PF10-HDE-Build-Notes-v12.9.5.md](https://github.com/amthorn78/glow-hdengine-v2/blob/0f8ff03960dace54b0faae835fdcc51111b4ec3e/docs/pfcanon/PF10-HDE-Build-Notes-v12.9.5.md) at repository commit 0f8ff03960dace54b0faae835fdcc51111b4ec3e

- [OpenAI model selection guidance](https://developers.openai.com/api/docs/guides/model-selection)

- [OpenAI prompting guidance](https://developers.openai.com/api/docs/guides/prompting)

- [ChatGPT Work model guide](https://learn.chatgpt.com/docs/models)

- [ChatGPT Work prompting guide](https://learn.chatgpt.com/docs/prompting)

- [Glow Operations Hub](https://app.notion.com/p/3ce4590a05eb814f8892f88ff8539308)

- [Prompt and Session Control Error Log](https://app.notion.com/p/3d14590a05eb81458dadf3fabd021b97)

## Change log

Version 1.12.1 — 2026-09-09 — Applied the Product Owner clarification that the prohibition concerns delegating prompt creation, not internal subagents. Permitted necessary or materially useful internal assistance within assigned scope; required task-fit recommendations without blanket model/mode exclusions; removed the explicit-permission obstacle and sole-writer fixed-effort wording. Preserved actual workflow ownership, approvals, human launch control and historical records.

Version 1.3.2 — 2026-09-05 — Whole-set 090526.3 review corrected contradictory account-picker inspection language, preserved exact internal human model headers and prospective appraisal, and refreshed affected current-reference labels. Published support, runtime exposure and account availability remain distinct; monthly review and prior history retained.

Version 1.3.1 — 2026-09-05 — Corrected mandatory internal human operator model headers, Astra-aware task appraisal and no receiving-agent self-reconfiguration. Historical outside-only statements below are superseded.

Version 1.3.0 — 2026-09-05 — Incorporated the Product Owner’s complete-flow-before-any-trial correction; withdrew subgroup readiness; preserved proportional verification, model guidance and archive controls.

Version 1.2.0 — 2026-09-04 — Implemented the adopted Prompt Repair strategy: bounded review and trials, observed-defect repair, realistic permission handling, reuse of current model appraisal, and continuing ownership. Preserved external launch recommendations and move-to-existing-archive controls.


- **1.1.0 — 2026-09-04:** Appraised GPT-6 Astra; made it the first candidate for the hardest governed tasks; retained task-based Sol/Terra/Luna selection; separated capability from workspace availability; clarified Max, Ultra, and proportional verification; revised prospective examples; migrated to raw Markdown while preserving native history.

- Versions 1.0.0–1.0.1 — 2026-09-04 — Initial release established the general prompt-flow control; version 1.0.1 corrected Work’s user-facing reasoning label from XHigh to Extra High after verification against current official OpenAI documentation.

## Source and representation history

- Previous editable source: [native guide v1.0.1](https://docs.google.com/document/d/11uEXGyf_esVJ1RZlhHXg_law26TE6iCQl5i4kujfuus/edit), structurally read with one tab, headings, lists, links, and no native media or comments requiring additional preservation.
- Storage requirement: [Glow Drive Markdown-First Storage and Editing Workflow v1.0.0](https://drive.google.com/file/d/190P6BI29hsQMJzg8vvzWylJaHcrHhfAR/view).
- Native history: [Docs Archive](https://drive.google.com/drive/folders/1T5tktjk6x0fdl-dKceyHMT7cOeRF6a4L). Historical sources remain valid evidence for earlier pinned runs and are not parallel current masters.
- No independent Glow model-comparison benchmark was run for this update. No numerical performance or price advantage is asserted.








## Historical change record

2026-09-05 — GCFPE establishment, complete-set change management, component prompt-use provenance, and incident 015 source-locator correction. Exact operational links remain outside prompt bodies; human model headers remain required. Historical sections are retained as history where superseded above.


## Authority correction — 1.4.1 — 2026-09-05

Recorded the Product Owner's express prohibition on PR creation and direct edits to every PF document outside authorized development unless explicitly instructed. Preserved development actor/scope boundaries and standalone-only PF10 addendum delivery for manual insertion. Incident 017 supersedes any earlier inference that establishment work authorized PR #398 or direct PF10 publication. This procedural correction performs no PF edit, PR creation, development execution or alpha exit.


## Revision 1.5.0 — 2026-09-05

Applied the Product Owner's workflow-only canon boundary, uncapped finite QA collections, predecessor assessment default, PR-20 completed-plan advice and PR-30 exception. Restored PE Analyze quality criteria in the ecosystem manager, aligned integration discovery and preserved all historical incidents and authority boundaries.


## Revision 1.5.1 — 2026-09-05

Prospective GCFPE PR completion, full-operation policy-constrained assessment, final-response handoff and stage-aware rescope repair. Prior source and incident history retained.


## Revision 1.5.2 — 2026-09-05

Enforced Product Owner manual PR merges, the direct-specific agent exception, PR-30 completion without a merge offer, and PR-40 merge-approval interpretation with read-only actual-state verification. Preserved earlier evidence and unrelated controls.

## Revision 1.6.0 — 2026-09-06

Implemented the approved integrated QA-10 audit, historical comparison, triage and readiness workflow; Thoth proposal and Isis decision ownership; pre-approval IA Plan preparation and explicit combined review; return-by-origin and uncapped bounded remediation cycles; informational PF publication without an extra progression gate; and the required post-publication Isis-49 QA-10 rerun. Preserved prior version/event history, ordinary approval boundaries, manual merges, workflow-only canon, complete source locators and task-specific model advice. The selected register and actual execution evidence determine publication and runtime status.



## Revision 1.6.1 — 2026-09-07

Align HDE capability preparation and environment evidence with the Product Owner’s practical Codespaces requirement. Preserve current model appraisals, advice ownership, human configuration choice and role/approval boundaries. This operational clarification adds no workflow stage or launch token.



## Revision 1.7.0 — 2026-09-07

Added the final shared CL-40 discovery contract and coordinated terminal routing. Preserved the complete prior document, including the 2026-09-07 workstation-preparation additions, historical decisions and QA/remediation rules.



## TW alpha setup revision — 1.9.0 — 2026-09-07

Added the scoped manual TW alpha requirements and actual implementation recommendation where applicable; linked the dedicated ecosystem space and implementation record. Earlier event-time records and unrelated workflow instructions remain intact. No PF source, reusable prompt body, repository, skill or runtime state is changed by this revision.


## In-flight routing revision — 1.9.1 — 2026-09-07

Implemented Nathan’s request to learn during existing pilots: task-specific cost/quality recommendations, observed-result capture, capability-specific Chat/Work routing and prospective appraisal refresh. Linked the Notion learning record. Preserved existing workflow authority, running work, original source identities and prior event-time history. No model benchmark or usage saving is claimed.


## TW alpha implementation revision — 1.9.2 — 2026-09-07

Recorded the verified TW-ALPHA-20260907.1 selection, bounded TW-MGMT-10 identity, source/worker boundaries, completed static/fixture/publication evidence and manual-runtime limitation. Preserved predecessor/source identities, dated setup and concurrent in-flight model-learning content, existing file ID/parent and unrelated workflow instructions. The detailed report is the evidence owner; this reference contains no reusable prompt body. No PF, repository, skill or live TW mutation is authorized by this revision.

## TW strength analyzer revision — 1.9.3 — 2026-09-07

Added the Nathan-authorized assessment-only entry and selected TW-ALPHA-20260907.2 with the six workers unchanged, analyzer 090726.1 and maintenance 090726.2. Fourteen affected cases were checked statically and both complete Notion publications read back. No live analyzer/worker trial or independent review was performed. Updated only this document's TW section, version and appended revision note; preserved other content, stable file ID and history. See the [change report](https://drive.google.com/file/d/1o2YGZxRvbqpENrHBASuxSjiZKR8CvUE5/view).


## TW coded naming revision — 1.9.4 — 2026-09-07

Recorded Nathan's GLOW-TW-NAMING-090726.1 request and verified eight-member TW-ALPHA-20260907.3 selection. Applied functional TW prefixes, action titles, internal references and explicit relationships. Existing roles, outputs, model guidance, PF/Drive runtime boundaries and previous event-time records remain. All eight publications, eight relationship checks and 18 established-case static preservation checks passed; no live or independent validation. This revision preserves the existing file ID, parent and all content outside the enumerated TW edits, version field and this note. Detailed receipt: [Alpha 1](https://app.notion.com/p/3d44590a05eb81fe991ff0114cb43029).


## TW Alpha follow-up revision — 1.9.5 — 2026-09-08

Implements the approved scope/coverage exit, two task-bound assessment checkpoints, formatted handoffs, optional-board PF09 inference, strict producer/Apply validation and narrow output-header provenance. Selected five revised roles: ASSESS/MGMT at 090826.2 and both drains/Apply at 090826.1; triage and section-only record roles unchanged. TW skill 1.1.6 and validator compatibility 2.5.2 synchronized. Earlier sections are historical where explicitly marked. No PF canon, other ecosystem or runtime session was changed. PF04 incident remains unresolved; live follow-up acceptance is pending.


## GCFPE middleware revision — 1.10.0 — 2026-09-08

Implemented the Product Owner-approved mandatory GCFPE middleware contract for the compatible GCFPE-20260908.1 successor: one Analyzer,51 selected prompts,48 effective logical rows. Preserved native authority, QA selection/attempts, manual controls, continuing sessions, first-entry exceptions and terminal CL-40. Prior assessment conclusions, all TW-owned blocks/history, earlier corrections, Primary core and automation holds remain unchanged. The owning register and maintenance record hold selection/readback/postflight evidence; this text does not prove runtime behavior or savings.


## GCFPE Epic-alpha repair revision — 1.11.0 — 2026-09-08

Effective prospectively upon governed successor selection. Replaced the current GCFPE middleware guidance with ENTRY and TRANSITION, precise manual/automation posture, retained role identity and dedicated bindings, carried Canon decisions and standalone addenda, strict PF source predicate, and no-PF10-mutation boundaries. Preserved native workflow contracts, prior dated history and all TW text. Existing Drive identity and verified parent retained.


