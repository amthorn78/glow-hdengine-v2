# Findings and refutations

Scope: the 55-member GCFPE-20261009.1 candidate, its PE control, seven supplied packages and directly affected repository contracts. Source URLs are in [source-identities.md](source-identities.md). Current authority is repository main `1ea6a262032c3c4de19c38c549d737d72b03ec2f`, including D27. These findings identify analysis scope; they authorize no repair.

Required findings use D26's R1–R4 rubric. Listed observations are disclosed, not silently scheduled for repair. No finding is based solely on a historical fixture, a retained predecessor pointer, known provenance, an unselected candidate status, or an absent installation.

## F01 — GCFPE skill continuity has not adopted D27

**LISTED compatibility gap; S2; recovery path; likely when a handoff lacks a persistent platform identity.** The candidate's shared Role and artifact continuity rule says a persistent platform session ID or session-inspection API is not an intake/handoff prerequisite. `change-flow/SKILL.md` Runtime entry gate still requires “Stable identities for the continuing Master Scrum, Isis, Thoth, IA, and Kronos contexts.” Its RESUME instructions recover exact bound sessions; the embedded core requires `ListAgents` and stable session identity before actions. PR-development still specifies the recorded phase's own session and a same-session PR-35 re-entry rather than explicitly distinguishing role continuity from persistence.

**Consequence:** a candidate-compatible recovery may be rejected by its mandatory support skill or redirected to an unavailable platform session. The explicit candidate override resolves many legacy body phrases, but there is no equivalent complete D27 override in the supplied specialization.

The demonstrated impact is a recoverable compatibility stop; no silent wrong action was established, so D26 lists it rather than making its repair mandatory. **Potential correction scope, if opted in:** the GCFPE specialization, PR-development continuation instructions, affected validation expectations and their behavior cases. Preserve current-target verification before real side effects, known provenance, author/reviewer independence, original work/Proceed lineage, and separate PR-30/PR-35 phase sessions. No generic Primary-core change is established. Exact-target safety is not itself a defect. Related defect classes: FUNC-001, PAIR-001.

## F02 — QA executor restrictions survive the new latitude rule

**Required: R1/R3; S2; normal QA planning path; high likelihood whenever the conflicting step is followed.** [QA-50](https://app.notion.com/p/3f44590a05eb815d89d3e602973d83ad), Execute → Phase 2, step 3 still says: “Name the authorized environment executor. Kronos designs tasks and reviews evidence; another authorized operator executes them.” Its new preamble says Kronos is not categorically barred when the PO chooses it and no executor identity is required. D27 records Nathan's exact opposite ruling. The supplied change-flow contract/oracle expectations retain the older Kronos/non-Kronos execution division.

**Consequence:** otherwise authorized execution is assigned a compulsory named, different operator, or the task is returned unnecessarily. This is a direct imperative contradiction, not optional retention of known provenance.

**Correction scope:** QA-50's surviving instruction and the active GCFPE skill/validator contract. Keep Kronos authorship, actual task/evidence identity, bounded execution permission and independent acceptance. Preserve QA-100 → QA-110 for every result; the withdrawn AF-024 observation is not revived. Defect classes: FUNC-001, SCOPE-001, GUARD-001.

## F03 — Three qualifying delta approvals terminate where the graph requires a handoff

**Required: R1; S2; valid delta approval path; high likelihood on that branch.** CF-C-30 and CF-E-30 Required result and routing say “DELTA_APPROVE: terminal return to Nathan”. IA-30 Required results and routing says “Emit no runnable continuation block in this invocation.” Its storage rule also includes DELTA_APPROVE among terminal results.

The corresponding candidate graph branches `crd_specification_delta_return`, `epic_specification_delta_return` and `plan_delta_return` declare `terminal_for_invocation:false`, `next_prompt_handoff_count:1`, and the actual `ORIGINAL_NATIVE_STAGE`. D15 expressly corrected this qualifying-approval family to nonterminal behavior; change-flow says the qualifying approval itself permits exact-phase continuation.

**Consequence:** a lawful continuation is omitted and the operator has to reconstruct it. “Do not run the continuation” is correct but does not mean “omit the human-pasted handoff.” Missing-source and genuine-decision exceptions remain terminal.

**Correction scope:** all three bodies, their interfaces and guards as one behavior. Do not reinstate a PF10 drain or addendum-presence checkpoint. This review did not change their graph flags to conceal the disagreement. Defect classes: PAIR-001, DERIV-001.

## F04 — Support controls forbid a supported standalone Plan-delta loop

**Required: R1; S2; approved-base delta authoring/revision path; high likelihood when that mode is used.** [IA-30](https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c) routes `PLAN_DELTA_REDLINE` and `DELTA_DENY` to IA-40. IA-40's `APPROVED_BASE_PLAN_DELTA_AUTHORING` produces “a separate delta artifact, never a replacement Plan.” The candidate graph agrees.

The [PE successor](https://app.notion.com/p/3f44590a05eb81f98b76c83465dc1960), Candidate authoring contract, says approved-base denial returns to the overlay owner, “not IA-40 or QA-80.” `change-flow/SKILL.md`, QA execution and repeatable remediation, says “IA-40 remains only for a denied or pending preapproval Plan.”

**Consequence:** the separate-delta author can be rejected, misrouted, or removed during maintenance to satisfy stale support instructions. Immutable-base protection does not forbid a separate pending overlay.

**Correction scope:** PE's IA-40 prohibition, change-flow's active Plan-delta restrictions and matching checks. Preserve the prohibition on replacing an approved base and independent review. Do not assume the QA-80 analogue needs the same change: QA-70's delta denial uses the actual originating owner, and its native route must be assessed separately. Defect classes: PAIR-001, FUNC-001.

## F05 — Addendum numbering and format ownership conflict with current canon

**Required: R1; S2; qualifying-addendum creation path; high likelihood.** Current PF06 v2.5.4 §0.1A and PF27 v2.0.5, Canon precedence for template use, require the next continuous numbered H2, a descriptive title and H3-or-deeper children at creation. The result is self-contained canonical subject matter, without role-addressed handling instructions. PF10 v13.5.1 contains no active addendum superseding that rule.

RS-20's Exact qualifying addendum section instead says “RS-20 never edits PF10, allocates PF10 numbering, or claims canonical adoption.” `change-flow/SKILL.md` says the producer does not allocate canon numbering and the PO “pastes and numbers” the addendum. `glow-hde-pr-development/SKILL.md:147` repeats the PO-numbering assumption. Candidate global `pf10_addendum_contract.producer_allocates_pf10_number` is false and `format_home` points to Glow Operations Hub rather than the current owning canon.

**Consequence:** the producer can emit an unnumbered record that is not page-ready under current canon; stale graph and skill expectations can approve it or reject the correct format.

**Correction scope:** the six qualifying producers CF-C-30, CF-E-30, IA-30, QA-70, RS-20 and ESC-40; their shared graph/registry contract; change-flow, PR-development and validator expectations. Directly confirmed incompatible wording and the cohort's remaining format checks are distinguished in coverage. A nonproducer forbidding itself from assigning numbering is a permitted exception. Reserving PF-file edits/publication to the PO remains valid; resolving the next number for a standalone addendum is a different act. No new PF10 visibility or drainage gate is justified. Defect classes: AUTH-001, PAIR-001.

## F06 — Active validator expectations lag the candidate; passes do not cover it

**LISTED validation boundary; S2; candidate verification path; observed historical-profile limits.** The supplied scripts and profiles explicitly validate 091426.1-era contracts, including old execution-role/continuity expectations. Their positive fixture and source-free checks are useful tests of those packaged instruments. They are not checks of all 100926.1 bodies and D27 behavior. The targeted and complete suite attempts also fail on missing sibling sources; no replacement sources were fabricated.

**Consequence:** release readiness can be falsely inferred from a green zero-body/historical run, or a valid new rule can be rejected by an obsolete expectation. This record does neither. Actual flags, counts and gaps are in [checks.md](checks.md).

The scripts report their historical profile and coverage; a reader misusing that output is not itself a demonstrated silent validator pass on the new candidate. **Potential correction scope for future candidate qualification:** current candidate profile, contract, interface/registry expectations and behavioral regressions alongside F01–F05; preserve immutable historical R1 evidence. `glow-graph-contract`, which owns graph build/derivation, was not supplied, so full shipped candidate derivation is unavailable. Missing dependency is a limitation, not proof the absent package is defective. Defect classes: PAIR-001, GUARD-001, SCOPE-002.

## F07 — Blanket skill prohibition includes the human advice canon requires

**Required: R1; S2; downstream handoff preparation; likely if the supplied rule is applied literally.** PF04 v2.8.7 §9.1.3 requires task-specific human advice about surface, model and reasoning, without provider mandates or automatic switching. `change-flow/SKILL.md:301` says not to “create, require, recommend, or route through” a model/strength assessment or reasoning recommendation. Validation requirements retain that broad prohibition.

**Consequence:** useful mandatory operator advice is suppressed along with correctly retired assessment middleware. Restoring a mandatory Analyzer, scoring gate, session launcher or provider rule would be the wrong repair.

**Correction scope:** distinguish advisory output from routing/approval prerequisites in the specialization and checks. This does not establish TypeSafe as the right implementation or authorize a remote score call. Defect classes: FUNC-001, NAME-001.

## F08 — Remediation skill inputs and verdicts do not match native ESC contracts

**LISTED compatibility gap; S2; lawful remediation review path; high likelihood for an APPROVE_AS_CHANGED result or a stage without the asserted Plan.** `change-flow/SKILL.md`, QA execution and repeatable remediation, restricts ESC-40's current artifact to “exact APPROVE or DENY” and says the record supplies a decision “only when it identifies the immutable approved IMPLEMENTATION_PLAN_REF”. Candidate ESC-40 explicitly returns APPROVE, APPROVE_AS_CHANGED or DENY and requires the affected approved bases that actually exist at the originating stage. The skill also names REMEDIATION_PLAN/REMEDIATION_PLAN_ID where current ESC-30 produces REMEDIATION_PROPOSAL and ESC-25 accepts the actual proposal/task lineage.

**Consequence:** a valid native decision or earlier-stage remediation can be rejected or forced to fabricate an input. The verdict and unconditional prerequisite conflicts are substantive. Artifact-name differences alone would not be sufficient: an explicit source-semantic alias can preserve compatibility, but that does not admit the missing verdict or remove the invented prerequisite.

The established outcome is incompatibility or a loud stop, not a demonstrated silent review or wrong artifact. **Potential correction scope, if opted in:** current change-flow remediation interfaces and consuming validators, preserving native proposal/review authority, actual legacy equivalents, original delivery/verification owner and existing stage timing. Do not change the candidate's three-state review to make an old two-state checker pass. Defect classes: PAIR-001, FUNC-001.

## F09 — The graph omits RS-20's pre-Proceed return to PR-20

**Required: R1/R3; S2; normal approved pre-Proceed rescope path; high likelihood when graph routing is applied to that phase.** RS-20's native Rescope authorship, independent review and return section assigns proposal authorship to PR-20 before Proceed and says: “Before Proceed, return to the actual PR-20 planning context with future vehicle fields absent.” Its stage-aware intake expressly omits `PR_RETURN_PHASE` for that planning context.

The committed candidate `RS-20.json` has no edge to PR-20. Its `APPROVE` branches are `rescope_pr30_prepublication`, `rescope_open_pr` and `rescope_non_pr`; the dynamic native branch explicitly requires a non-PR origin. PR-20 is a PR origin, so none represents the lawful pre-Proceed return. The REJECT/IN_SCOPE_REPAIR dynamic branches have the same non-PR restriction.

**Consequence:** a graph-driven handoff can omit the lawful planning continuation or substitute an execution phase/vehicle that does not yet exist. This is a disagreement between the two current contracts on a supported success path, not a demand for another execution-phase enum. Refutation checked: PR-30_PREPUBLICATION is already proceeded implementation, not PR-20 planning; the non-PR branch cannot silently cover a PR author.

**Correction scope:** the stage-aware candidate RS-20 graph/interface and derived registry expectations, with a pre-Proceed return case that preserves absent future fields. Keep the three execution return-phase values unchanged and the native independent IA review. This was found while checking the flow diagram, after the workload review, and is recorded as a coordinator correction to coverage. Defect classes: PAIR-001, DERIV-001, GUARD-001.

## Listed observations and boundaries

| ID | Observation, path, likelihood and consequence | Disposition |
|---|---|---|
| L01 | Reused selected MGMT remains the six-input Batch method, including its retired Batch 6 skill-review timing. A caller following it encounters known D20 redesign debt. | Use the disclosed testing contract for this run. Completion/promotion of MGMT redesign is related existing work, not implicit runtime-candidate selection. |
| L02 | `glow-hde-pr-development` hardcodes Claude Code/`gh` and rejects connector fallback, although PF04 permits any verified capable surface. On another surface it can stop loudly. | Portability restriction listed; no claim that every connector can satisfy the complete PR lifecycle. |
| L03 | PR-10/20/30/35/40 retain some legacy required-session/disposition clauses under the explicit D27 interpretation. Nine mentions in five clause units remain after excluding known-provenance uses. | List as maintenance debt; the new body preamble is an operative override. Do not count all session references as defects. |
| L04 | OPS-10/20 transport text may expect revised proposal/report artifacts before RS-30 creates them. | Listed timing/clarity risk; preserve current lawful author and loud missing-input handling. |
| L05 | Initial IA-30 Plan approval names an executable PR, without a distinct Ops-first branch. A Plan beginning with Ops can require owner recovery. | Listed because executable/dependency guards prevent a lawful silent bypass. Do not extend the approved PR-40 progression repair by assumption. |
| L06 | Five closure bodies retain Candidate-prefixed destination headings/authoring boilerplate. The actual candidate URLs resolve. | Listed body-policy hygiene; no broken runtime locator shown. |
| L07 | Attribution validator accepts contradictory retention prose outside its checked lifecycle fields, despite the matrix's broader wording. Native skill still forbids persistence. | Listed coverage overstatement; no actual publication or authority bypass demonstrated. |
| L08 | A resealed LOCAL_GIT manifest with `untracked_paths=["ghost.txt"]` and unchanged empty-path hashes is accepted. Collector itself derives these consistently. | Listed altered-input consistency risk, not a normal collector failure. Any repair needs an explicitly included package/test scope. |
| L09 | Supplied TypeSafe scores effort/model, not demonstrated relay safety; excludes manager judgment while AF-013 asks for quantitative relay advice plus qualitative advice. Its OD source records and GCFPE binding are not established. | Keep domain-specific package unchanged. Recommend separating AF-013 integration pending its actual contract and sources; no invented score, mandatory model gate, or assumed automatic skill trigger. |
| L10 | Available installed governance-audit source is older than the supplied/canonical repair history and contains prompt snapshot/hash and retired drainage instructions. | It was consulted for comparison method only. D22/current repository controls govern this run. Recover the intended current source for any future full governance postflight; do not label this old environment copy the latest approved package. |
| L11 | Required graph builder and several full-suite siblings are outside the seven supplied packages. | Source packages are sufficient; installation is not necessary for analysis. Full integration scope remains unmeasured until exact sources are available. |

## Claims deliberately not made

No skill was installed, edited, packaged or approved. No runtime prompt was executed. No supplied TypeSafe service call or uses-table write occurred. No PF, selected graph/registry, prompt body, selection or historical approval was changed. No observed runtime success is inferred from fixtures, source review or Notion readback. No formal D24 verdict is issued for unchanged supplied packages.
