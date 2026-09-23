---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
status: INTAKE
targets: []
gate_tier:
closure:
  upstream: []
  downstream: []
  state_sharers: []
readiness:
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted:
interaction_cost_actual:
items:
  - id: ITEM-01
    statement: "Each of the 40 of 55 091426.1 prompt bodies never yet read for a decorated governance line is checked with flowmaster-validate's PROMPT_BODY_GOVERNANCE_STATE, and anything found is repaired: a leftover line is removed, and a false positive is closed by narrowing the check, never by a looser strip."
    source: AF-004
    disposition: ""
  - id: ITEM-03
    statement: "The operational guidance, the workflow explanations and future handoffs all communicate the Notion read-only default consistently, so Notion is not crowded with routine lifecycle records."
    source: AF-006
    disposition: ""
  - id: ITEM-04
    statement: "A normal handoff carries only the persistent prompt to run, the target session or role where relevant, the exact input filenames each with a short label, and the minimum context for an exceptional condition, never restating history, architecture, decisions, scope, acceptance criteria, workflow rules or artifact contents that the named prompt, canon or files already hold."
    source: AF-008
    disposition: ""
  - id: ITEM-06
    statement: "Every handoff is visibly presented: the block is not buried inside a long report or surrounded by unnecessary explanation."
    source: AF-008
    disposition: ""
  - id: ITEM-07
    statement: "Every result a session produces, test results above all, is written to that session's output artifact, so a handoff may name the artifact but never carries the only copy of a fact; before handoffs shrink, every kind of fact the handoff rule now makes a handoff carry has a home in the producing prompt's output artifact."
    source: AF-008
    disposition: ""
  - id: ITEM-08
    statement: "A handoff carries no branch or commit; a versioned filename identifies the content, because an issued version is never edited and a correction is a new version."
    source: AF-008
    disposition: ""
  - id: ITEM-09
    statement: "PR implementation agents (the triggering case arose while PR-20 was planning) make the ordinary engineering and design decisions needed to accomplish the accepted work, including ones the plan did not anticipate, without a rescope: a correction that is obvious, necessary to make the approved scope work, and consistent with the Epic's accepted objective and controlling constraints is in scope, and the implementor decides it, implements it and tests it."
    source: AF-009
    disposition: ""
  - id: ITEM-10
    statement: "Formal rescoping is reserved for a genuine change to the Epic-level commitment (its outcome or objective, approved acceptance criteria, a protected architectural, security, data-model or external-contract boundary, a re-baseline across several planned work units, an accepted dependency or cross-team commitment, or budget, schedule or risk needing Product Owner direction), and a planned approach found incomplete, impractical or inferior is not by itself grounds."
    source: AF-009
    disposition: ""
  - id: ITEM-11
    statement: "Implementors have a simple decision tree or matrix they can apply during work to tell implementation latitude from formal rescope."
    source: AF-009 (AF-010 point 3, merged)
    disposition: ""
  - id: ITEM-12
    statement: "Implementation reports record every in-flight design decision: what changed, why it was necessary, and what was tested."
    source: AF-009 (AF-010 point 4, merged)
    disposition: ""
  - id: ITEM-14
    statement: "PR-30 builds the implementation, and PR-35 handles all code-review findings and CI fixes for that existing PR."
    source: AF-011
    disposition: ""
  - id: ITEM-15
    statement: "PR-35 is handed off to a separate dedicated session, because review handling, code-review corrections and CI fixes have different context and model-usage demands from implementation."
    source: AF-011
    disposition: ""
  - id: ITEM-17
    statement: "The PR-35 session subscribes to the existing PR it continues."
    source: AF-011
    disposition: ""
  - id: ITEM-18
    statement: "When PR-35 completes and its PR is merged, PR-35 automatically creates and dispatches a PR-40 handoff, a mechanism the workflow does not have today."
    source: AF-011
    disposition: ""
  - id: ITEM-19
    statement: "When a prompt ecosystem is modified, prompts that do not change only have their version number bumped, the version number alone tracking membership of the current iteration, and sibling bodies are created only for prompts that actually change, across all prompt ecosystems in the repository."
    source: AF-012
    disposition: ""
parts:
  - id: PART-01
    name: "Scan the 40 unread bodies for a decorated governance line, and repair what it finds"
    items: [ITEM-01]
    class:
    after: []
  - id: PART-02
    name: "Say the Notion read-only default the same way everywhere"
    items: [ITEM-03]
    class:
    after: []
  - id: PART-03
    name: "Every result lives in its output artifact"
    items: [ITEM-07]
    class:
    after: []
  - id: PART-04
    name: "A handoff carries only what the receiver cannot find elsewhere"
    items: [ITEM-04, ITEM-08]
    class:
    after: [PART-03]
  - id: PART-05
    name: "The handoff block is visible, not buried"
    items: [ITEM-06]
    class:
    after: []
  - id: PART-06
    name: "Implementation reports record in-flight decisions"
    items: [ITEM-12]
    class:
    after: []
  - id: PART-07
    name: "Implementation latitude and the rescope boundary"
    items: [ITEM-09, ITEM-10, ITEM-11]
    class:
    after: [PART-06]
  - id: PART-08
    name: "PR-35 alone handles review findings and CI"
    items: [ITEM-14]
    class:
    after: []
  - id: PART-09
    name: "PR-35 in its own session"
    items: [ITEM-15]
    class:
    after: [PART-08]
  - id: PART-10
    name: "The PR-35 session subscribes to its PR"
    items: [ITEM-17]
    class:
    after: []
  - id: PART-11
    name: "Automatic PR-40 dispatch after merge"
    items: [ITEM-18]
    class:
    after: []
  - id: PART-12
    name: "Version bump instead of a sibling for unchanged prompts"
    items: [ITEM-19]
    class:
    after: []
request: |
  Run the open Alpha Feedback items through triage: AF-004, AF-006, AF-008, AF-009 (it now includes AF-010's merged scope), AF-011, AF-012.
  They are on "GCFPE Alpha Feedback — Deferred Items — 091426.1", Notion page 3df4590a05eb8111a6a5f67cb82f96f6.
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20260923-alpha-feedback-open-entries

Carries the six open Alpha Feedback entries (AF-004, AF-006, AF-008, AF-009 with AF-010's merged
scope, AF-011 and AF-012) as one Modification: 15 new items in twelve parts, covering the
governance-line scan, the Notion read-only message, short handoffs backed by artifacts,
implementation latitude, the PR-35 phase and session, PR-40 dispatch, and version bumps in place of
siblings.

## Intake

Triage run 2026-09-23 under the D21 revision of *Modification Intake and Triage — PROPOSED (D20
redesign)* (Notion `3e34590a05eb81bfbf1ed0651e6b6ddf`), against `main` @ `a63bf80`. The six entries
split into **19 items: 15 NEW and 4 NOT_A_CHANGE** (already true). None is a duplicate, none is already
ruled, and no item's disposition waits on Nathan. **One question of intent, about ITEM-03 and
ITEM-04, is Nathan's to answer, at the latest when he approves `ANALYZE`** (see *Tensions*). Items are
numbered once across the run; the four that are not NEW keep their numbers and live only in this section.

**How the evidence was gathered.** Each record surface was read once for all 19 items: the graph
parts, the registry, the installed skills, the management documents and the Notion operational pages.
One prompt body, `PR-35`, was read in Notion for ITEM-17, and not copied to disk. Four independent
checkers then challenged the draft: one tried to overturn the already-true calls, one the NEW calls,
one audited the split and the parts, and one opened every cited line. Their corrections are applied
below. They overturned one disposition: ITEM-14 was drafted as already true, and is NEW. Nothing below
measures scope. Every **apparent surface** is unmeasured: it names what an item looks like it touches,
and `ANALYZE` computes the reach.

### The items

Citations: repository paths are from the repository root. `skill:<name>:N` is line N of the installed
skill's `SKILL.md`. `contract` is
`change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`; `flowmaster-validate`
bundles a byte-identical copy. `registry` is `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`.
`Notion: <page> § <heading>` is a Notion page section.

| id | source | requested outcome (short) | disposition | evidence | apparent surface (unmeasured) |
|---|---|---|---|---|---|
| ITEM-01 | AF-004 | the 40 unread bodies are checked for a decorated governance line, and anything found is repaired | **NEW** | Not done. Only 15 of 55 bodies are read; "The other 40 have never been looked at" (`docs/ephemeral/gcfpe.round30/REPORT-r30-CORRECTIONS.md:155-157`). No later record in the repository or on the Notion pages read shows a scan. The instrument is installed: `flowmaster-validate` 3.2.16 (`skill:flowmaster-validate:8`) emits `PROMPT_BODY_GOVERNANCE_STATE` (`flowmaster-validate/scripts/validate_gcfpe_20260914.py:2332-2333`, matcher `:1014-1043`) under `--bodies-stdin` only. The method is standing procedure (`docs/prompt_ecosystem_management/prompt-validation-procedure.md:20-25`). AF-004 names the narrow false-positive fix, "Not a looser strip". Owner at closure is "the next `GCFPE-MGMT-10` run", which `D20-B` replaces in place (`docs/prompt_ecosystem_management/gcfpe.decision-record.md:1029-1030`) | The 40 member bodies in Notion, read only. The matcher in `flowmaster-validate`, only on a false positive. A body and its registry `evidence_contract` hash, only on a leftover |
| ITEM-02 | AF-006 | lifecycle agents default to Notion read-only; a write only when the task or a destination rule requires it | **NOT_A_CHANGE** — already true | This is a Product Owner policy of 2026-09-22 (not a D-number): read-only absent task authorization or a destination rule, and no write inferred from a handoff, a completed task or an output (`docs/prompt_ecosystem_management/notion-write-boundary.md:34-47`, `:127-130`). The same rule stands in `session-working-rules.md:53`, `skill:glow-workspace-currency:141-144`, `skill:glow-write-boundary:64-66` and `skill:glow-artifact-storage:99-101`. The three skills were reviewed `SKILL_FIT_CONFIRMED` and installed on 2026-09-22 (`docs/ephemeral/pe36.task-01/INSTALL-VERIFICATION-pe36-task01.md:14-15`). The Hub states it too (Notion: Glow Operations Hub § Current GCFPE prompt and artifact categories — 091426.1). The source says so itself: "The relevant skills have already been updated". The behaviour matches: lifecycle sessions stopped writing the Flow Index (see ITEM-03) | — |
| ITEM-03 | AF-006 | operational guidance, workflow explanations and future handoffs say the default consistently | **NEW** | Partly there. The repository's operational documents say it (`docs/prompt_ecosystem_management/session-working-rules.md:53`, `:55`), and so does the Hub (§ Tracking is part of the work). `docs/prompt_ecosystem_management/README.md:60` gives the storage half: handoff and development-flow prompts are not Notion. Not consistent elsewhere. **`skill:session-relay-flowmaster:268`** reads "Notion is the preferred live control plane for current task, assignment, dependency, decision, and handoff state". `D18` makes the Flow Index's *Sole operative Alpha state* block "the single operative record" of Alpha state, and says the block governs if the others disagree (`gcfpe.decision-record.md:933-938`). The block carries a per-step PR04 log (`pr10_result`, `pr20_result`, `rs10_result`, …, `current_handoff_status`), and its § Maintenance protocol item 3 has every update record actor, output, status and next gate (Notion: Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1). Notion: HDE Change Flow Overview § CRD Alpha Test 1 still tells operators to "track actual work, prompt-use evidence, defects and retests" in a Notion checklist; that is a completed test's tracking block and not labelled historical. `glow-hde-pr-development` and `change-flow` never state the default. The policy's own record says the prompt bodies were never audited against it (`notion-write-boundary.md:7`, `:161-164`) | `session-relay-flowmaster`. The Flow Index's Alpha-state block and maintenance protocol. The Change Flow Overview. The workflow and handoff sections of the lifecycle prompt bodies. Possibly `glow-hde-pr-development` and `change-flow`. **Whether AF-006 reaches the per-step entries `D18`'s block carries is a policy question for `ANALYZE` and Nathan** |
| ITEM-04 | AF-008 | a handoff carries only prompt, target, labelled filenames and exceptional context | **NEW** | Two of the four elements are already required: the exact prompt and the receiving role and session (`docs/graph/parts/global.json:359-360`). What is new is "only". Today `handoff_contract.required` also makes every handoff carry "status, completed work, decisions, constraints, unresolved items, preserved authority" (`global.json:363`). It prohibits an "unlinked filename" (`:353`). `skill:glow-hde-pr-development:162` says "A metadata list, menu, blank form, filename-only reference, or instruction to reconstruct context is not runnable". Also `skill:change-flow:295`, `contract:17615` and the `PR-35` body's *Mandatory single-block handoff*. The source's example handoff block is 17,746 characters and 224 lines (`docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v2.0.md`) | `handoff_contract` in `docs/graph/parts/global.json`. `glow-hde-pr-development`. `change-flow` and the bundled contract. The handoff section of each member body. Whether AF-008 also reaches the Hub's 16-section maintenance-session standard (Notion: Glow Operations Hub § Prompt ecosystem worker output standard — canonical) is for `ANALYZE` |
| ITEM-05 | AF-008 | every handoff is one clearly labelled, paste-ready block | **NOT_A_CHANGE** — already true | Exactly one fenced `text` block, first line `NEXT_PROMPT_HANDOFF`, a complete paste-ready prompt, one per non-terminal result (`docs/graph/parts/global.json:343-346`). Every non-terminal branch in all 55 parts has a handoff count of 1. `skill:glow-hde-pr-development:162`. The registry audit contract requires the literal and a block count of 1 (`registry:5298-5300`). The Hub worker standard requires the same for maintenance sessions. **Condition:** the reviewer-prompt block has no label line (`docs/prompt_ecosystem_management/reviewer-prompt-template.md:17`, block opening at `:20`), and `skill:session-relay-flowmaster:279` describes a routed handoff in several parts. If `ANALYZE` finds AF-008 reaches those surfaces, this item is not fully true there | — |
| ITEM-06 | AF-008 | every handoff is visibly presented, not buried in a long report | **NEW** | Placement is half-governed, and visibility not at all. `skill:change-flow:295` puts the block last ("Every nonterminal result ends with exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block"). `skill:session-relay-flowmaster:279` puts it "in the final user-facing response itself". `skill:glow-hde-pr-development:162` says only "include", and the graph's `handoff_contract` covers the block's form and content only (`global.json:341-367`). Nothing limits the report above the block: the source's example opens its block at line 54, after 53 lines. A length rule already covers any message to Nathan (`skill:glow-po-reporting:52`; `session-working-rules.md:102-103`), but no lifecycle prompt applies it to its return | `change-flow`, `glow-hde-pr-development` and `session-relay-flowmaster` handoff rules. The return section of the lifecycle bodies |
| ITEM-07 | AF-008 | every result is in the output artifact; a handoff never holds the only copy | **NEW** | No rule forbids a fact living only in a handoff. The Hub's worker standard allows it: "If a fact matters, it goes in the correct numbered section of the handoff or the artifact" (§ Prompt ecosystem worker output standard — canonical › Every response is paste-ready). Handoff files are a sanctioned artifact class (`skill:glow-hde-pr-development:155`). `PR_IMPLEMENTATION_RESULT` is declared, but its content is not set (`docs/graph/parts/prompts/PR-30.json:162-163`). **The source's own example does not hold:** the result "14 failed, 1,207 passed" is also in `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md:101` and `…-rs20-checkpoint-v2.0.md:62`, which landed with the handoff in commit `a4490af`. The rule is still absent; that instance was not a gap | The output-artifact content of each producing prompt, `PR_IMPLEMENTATION_RESULT` above all. `glow-hde-pr-development`. The Hub worker standard |
| ITEM-08 | AF-008 | no branch or commit in a handoff; a versioned filename identifies content | **NEW** | Current handoffs must carry them: "exact workspace/worktree, branch, open PR and remote-head lineage" (`skill:glow-hde-pr-development:22`, `:82`). Also `skill:change-flow:313`, the `PR-35` body's handoff section ("repository/worktree/branch/PR/head references"), and the Hub's handoff § 6 "repository, branch, commit". Reviewer prompts carry them too (`docs/prompt_ecosystem_management/skill-packaging-and-delivery.md:51`, `reviewer-prompt-template.md:40`). Applied so far only to the triage handoff (`docs/ephemeral/pe36.mgmt-redesign/GCFPE-MGMT-REDESIGN-ANALYSIS-v1.0.md:796-797`). The premise already stands: a dated record is never corrected in place (`AUTH-001`, `notion-write-boundary.md:125`), and a successor takes `-v2` (Notion: Glow Operations Hub § Delivered artifacts must be identifiable from their filename — canonical). Two rules pull the other way: `skill:session-relay-flowmaster:259` forbids a "version-pinned filename as a locator substitute in prompt text", and `skill:glow-artifact-storage:145-148` says "Never put a version or a date in a live filename" (written for Drive) | The same surfaces as ITEM-04. `session-relay-flowmaster`. The reviewer-prompt template and the Hub standard, if `ANALYZE` finds AF-008 reaches them |
| ITEM-09 | AF-009 | ordinary engineering and design decisions, including unanticipated ones, are in scope for the implementor | **NEW** | Defect repair is already in scope; design latitude is not. An ordinary in-scope defect stays with the PR session: `skill:glow-hde-pr-development:65` ("Correct ordinary in-scope defects within the work unit") and `:135`, `skill:change-flow:453`, and PR-20's same-session repair of "a bounded planning defect" (`docs/graph/parts/prompts/PR-20.json:123`). No surface grants latitude for design or approach decisions. At planning, a design boundary routes to rescope, PR-20 → RS-10 when "the planning result substantiates a material scope, architecture, requirement, or design boundary" (`PR-20.json:157`). The PR skill's rescope trigger includes "architecture … or Plan authority" (`skill:glow-hde-pr-development:128`). RS-10 and RS-20 can call a finding in scope, but only after a handoff (`docs/graph/parts/prompts/RS-10.json:46`; `IN_SCOPE_REPAIR`, `skill:change-flow:323`). The triggering case was classed a rescope (`docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md:126`). PR04 ran under a one-unit Product Owner direction to the requested effect (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.2.md:668-670`); that is not a standing rule | `PR-20`, `PR-30` and `PR-35` bodies and graph parts. `RS-10`. `glow-hde-pr-development`. `change-flow` and the bundled contract |
| ITEM-10 | AF-009 | formal rescope only for a genuine Epic-level commitment change | **NEW** | The rescope lane today works at work-unit level, below the Epic threshold asked for. RS-20 approves a "complete bounded work-unit rescope within approved Specification intent" (`docs/graph/parts/global.json:430`; `skill:change-flow:313`). The planning-lane and OPS-30 entry predicates name "scope, architecture, requirement, or design" (`PR-10.json:157`, `PR-20.json:157`, `OPS-30.json:175`). The in-flight PR entries carry no threshold of their own (`PR-30.json:132`, `PR-35.json:135`). The implementor's threshold lives in `skill:glow-hde-pr-development:128` and `skill:change-flow:454`. The QA remediation lane has its own threshold, which counts a material change of "approach" (`skill:change-flow:488`); whether AF-009 reaches that lane is for `ANALYZE`. Related: `D4` ties formal rescope approval to the PF10 addendum (`gcfpe.decision-record.md:43-44`), so the threshold changes how often addenda arise | The rescope-entry predicates of the planning lane. `glow-hde-pr-development`. `change-flow`. `RS-10`, `RS-20`. Possibly the ESC remediation lane |
| ITEM-11 | AF-009 | a decision tree or matrix for the implementor | **NEW** | None exists. "decision tree", "decision matrix" and "latitude" have no hits in the graph, the registry, `change-flow` or `glow-hde-pr-development`. The only matrix is the RS-20 decider's (Notion: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1 § 7, row 3.06) and a historical plan's evidence checklist (`docs/ephemeral/GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md:287`). Neither is an implementor's tool | Where ITEM-09's rule lands |
| ITEM-12 | AF-009 | implementation reports record each in-flight decision: what, why, what was tested | **NEW** | Not required. The PR ledger has no design-decision field (`skill:glow-hde-pr-development:59`). "Decisions" are required in the handoff, not the result (`:162`). The registry defines `PR_IMPLEMENTATION_RESULT` by name and states only (`registry:3520-3525`). PR04's result did record its in-flight corrections, on a Product Owner direction (`docs/ephemeral/HDE-EPIC040-PR04-pr35-entry-checkpoint-v1.0.md:32`). Its §4 table records plan statement, repository fact and applied fix (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md:51`). Tests are recorded for some rows (`:78`, `:85`, `:89`) and in §8, not for every decision | `PR_IMPLEMENTATION_RESULT` content in the `PR-30` and `PR-35` bodies. `glow-hde-pr-development` |
| ITEM-13 | AF-011 | PR-20 and PR-30 may share a session that plans, then builds | **NOT_A_CHANGE** — already true | "One dedicated session per planned PR work unit; the same session performs both" (`skill:change-flow:365`). GCF-14 creates that session and GCF-15 has the Product Owner run Proceed "in that same session" (`:450-451`). PR-30 is "the same dedicated PR engineering session" (`docs/graph/parts/prompts/PR-30.json:177`; `registry:3425`, `:3513`). PR04 ran both in session `PR04-HDE-EPIC040-1` (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md:6`). It is mandatory rather than optional, with Nathan's Proceed between the phases. The machine contract does not enforce it: `pr_continuity_contract` omits PR-20 (`global.json:507-511`) | — |
| ITEM-14 | AF-011 | PR-30 builds; PR-35 handles all review findings and CI fixes on that PR | **NEW** | Mostly true, but not the "all". PR-30 builds and stops at `PR_CANDIDATE_PUBLISHED`. PR-35 owns "remote review retrieval, corrections, local retesting, coherent corrective publication, CI economy, current-head verification, and genuine merge readiness" (`skill:glow-hde-pr-development:53`; asserted at `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:33-34`; `docs/graph/parts/prompts/PR-35.json:174`; `contract:2987-2993`). CI fixes are already PR-35's alone. **Review correction is not.** PR-30's registry row allows it to "review-correct" (`registry:3531`). PR-30's section of the skill allows "An early draft PR" and says to "Bundle related implementation or review corrections into one locally verified push" (`skill:glow-hde-pr-development:77`, `:79`). Code review is Codex's, on the PR (`:86`). A PR-40 `REJECT` for "a precise in-scope implementation/review/corrected-code/PR-lineage defect" routes back to PR-30 (`docs/graph/parts/prompts/PR-40.json:165`; `contract:15734`). | PR-30's registry row. The PR-40 `REJECT` → PR-30 route in the graph part, the bundled contract and the PR-40 body. PR-30's section of `glow-hde-pr-development` |
| ITEM-15 | AF-011 | PR-35 in a separate dedicated session | **NEW** | The deliberate current contract is the opposite. `"session_class": "SAME_DEDICATED_PR_DEVELOPMENT_SESSION_AS_PR-30"` (`docs/graph/parts/prompts/PR-35.json:190`). "dedicated PR-development session" is one of the ten fields PR-30 and PR-35 share exactly once (`docs/graph/parts/global.json:513-516`), tied to R1 row GCF-17 (`:512`, `:528`). Also `registry:3604-3611`, with adding a session forbidden at `:3633`. `skill:glow-hde-pr-development:53` and `:55`, asserted at `scripts/validate_glow_hde_pr_development.py:32`. `skill:change-flow:307`. The register calls PR-35 "a same-session phase … not a new role, gate, session" (Notion: GCFPE Membership and Release Register § Current explicit membership — 091426.1). So do the Flow Index ("Normal PR lane: … same-session PR-35") and Notion: GCFPE PR Development Skill-Fit and Interoperability Decision — 20260914.1 § Interoperability rule. Precedent: PR04's PR-35 ran in a successor session by Product Owner exception (`docs/ephemeral/HDE-EPIC040-PR04-pr35-entry-checkpoint-v1.0.md:3`) | `pr_continuity_contract` in `global.json`, and the R1 oracle `flowmaster-validate` pins (`global.json:551-557`). `PR-30`, `PR-35` and `RS-40` parts and bodies. Registry rows. `glow-hde-pr-development`, its validator and behaviour cases. `change-flow` and the bundled contract. `session-relay-flowmaster:283`. The register and Flow Index wording |
| ITEM-16 | AF-011 | the PR-35 session continues the same PR, never a new or replacement one | **NOT_A_CHANGE** — already true | "The work unit keeps exactly one branch and one pull request … do not … open a second pull request" (`skill:glow-hde-pr-development:158`; reuse at `:77`). "pull request" is shared exactly once (`docs/graph/parts/global.json:519`). PR-35 resolves findings "on the existing pull request" (`registry:3626-3629`). It held when PR04's PR-35 ran in a successor session (`docs/ephemeral/HDE-EPIC040-PR04-pr-remote-action-ledger-v1.0.md:33`). Some surfaces already contemplate work units with several ordered PRs (`skill:session-relay-flowmaster:285`; `registry:3706`), and none says which phase opens a later one. **This has to stay true under PART-09** | — |
| ITEM-17 | AF-011 | the PR-35 session subscribes to its PR | **NEW** | No surface says so: "subscribe" has no hits in the graph, the registry, `glow-hde-pr-development`, `change-flow`, the bundled contract or the Notion operational pages. The `PR-35` body, read for this item, waits on remote results through a `REMOTE_EVIDENCE_PENDING` same-session re-entry handoff (also `skill:glow-hde-pr-development:112`), and forbids polling indefinitely. The skill polls "only when a pending remote result can change the next action" (`:121`). Precedent: PR04's successor PR-35 session subscribed to PR #467 when told to (`docs/ephemeral/HDE-EPIC040-PR04-pr-remote-action-ledger-v1.0.md:33`; `…-pr35-entry-checkpoint-v1.0.md:36`) | The `PR-35` body and graph part (`REMOTE_EVIDENCE_PENDING`). `glow-hde-pr-development` |
| ITEM-18 | AF-011 | after merge, PR-35 creates and dispatches a PR-40 handoff automatically | **NEW** | Creation half-exists; dispatch and merge observation are deliberately absent. PR-35 already returns a complete PR-40 handoff at `MERGE_PENDING`, conditional on Nathan's manual merge (`skill:glow-hde-pr-development:164`; `docs/graph/parts/prompts/PR-35.json:21`; the `PR-35` body's merge-readiness gate). No edge into PR-40 is automatic: `"direct_PR35_to_PR40_automatic_edge": false` (`global.json:449`). PR-40 is entered by Nathan's `MANUAL_PRODUCT_OWNER_INVOCATION` (`:33-43`), or by DOC-20's non-automatic handoff after Nathan asserts the merge (`docs/graph/parts/prompts/DOC-20.json:151`, `:169`). `skill:change-flow:366`: "no automatic dispatch or agent merge". PR-40's input is Nathan's invocation asserting the merge (`registry:3710`). **Watching for the merge is prohibited today:** the skill "never authorizes an agent to … keep polling for that manual action" (`skill:glow-hde-pr-development:110`), and PR-35 "returns control without polling for that action" (`skill:session-relay-flowmaster:283`, also `:285`). Nothing in the flow can launch or message another session (`skill:session-relay-flowmaster:713`; `docs/prompt_ecosystem_management/execution-and-delegation-model.md:137-139`). No D-number rules on dispatch. Merge stays Nathan's (`D18`, `gcfpe.decision-record.md:944`) | `post_merge_three_event_contract` and the manual-merge edge in `global.json`. `PR-35`, `PR-40` and `DOC-20` parts, bodies and registry inputs. `glow-hde-pr-development` (the no-polling rule). `change-flow` and the bundled contract. `session-relay-flowmaster:283-285` |
| ITEM-19 | AF-012 | unchanged prompts get a version bump, not a sibling | **NEW** | Today every member gets a sibling. The 091426.1 release moved all 54 predecessor member bodies to the archive (`D17`, `gcfpe.decision-record.md:878`; `docs/prompt_ecosystem_management/authoritative-surfaces.md:27`). The contract records `"versioned_sibling_successors": true` (`contract:3095`). The Alpha checklist requires "All 55 successor prompts are complete versioned siblings" (Notion: GCFPE Alpha Establishment and Change Management Checklist — 091426.1 § Governance repair checklist). The version sits inside every body: all 55 registry rows require `Prompt Version: 091426.1` (`registry:240`; `D11`, `gcfpe.decision-record.md:611`), so a bump edits the body. **A binding convention bears on it:** `prompt-body-content-policy.md:31` bars a body field "whose value changes because of a *release event*", while `:33-34` lists `Prompt version:` as legitimate. Precedent: 090726.2 kept 32 unchanged members at their old versions, with no sibling and no bump (Notion: Glow Operations Hub § Historical selection — GCFPE-20260907.2) | The release procedure. The register and complete-prompt-set catalogs. The in-body version line and its registry `required_regex`. `prompt-body-content-policy.md`. The bundled contracts' member registry. The repository's other prompt ecosystems, such as TW |

### Noticed while reading — not items

Nobody asked for these, so they are not in scope. They are recorded so the next session does not
rediscover them. The first may well be worth a ruling.

- **The single operative record of Alpha state is stale by four stages.** `D18` makes the Flow
  Index's *Sole operative Alpha state* block the record that governs (`gcfpe.decision-record.md:933-938`).
  The block was last edited 2026-09-22 07:35 and still reads `next_intended_stage: PR-20`,
  `implementation_authority: NONE`, and "PR04 implementation has not started". PR04 has since been
  implemented (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md`), merged as PR #467,
  and accepted by PR-40 (`docs/ephemeral/HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md:20`,
  `decision: ACCEPT`). The read-only default did what it says: lifecycle sessions stopped writing
  Notion. But nothing else writes the block now. That collision is ITEM-03's open question, playing out.
- **AF-008's evidence claim is wrong at `main`.** The entry says the full-validation result "exists
  only in the handoff". It is also in RS-20's own output artifact and checkpoint, which landed in
  the same commit (ITEM-07 above). The rule AF-008 asks for is still absent.
- **`notion-write-boundary.md:155-156` says a sweep of the other installed skills found "no fifth
  instance" of the Notion-write conflict.** That sweep looked for the Notion-write-default and
  prompts-in-Notion phrasings. It did not catch `session-relay-flowmaster:268`, which makes Notion
  the "preferred live control plane" for handoff state. The next line makes Google Drive "the
  preferred artifact plane", against `D7`.
- **`prompt-body-content-policy.md:78-84` is stale.** It says the governance-state check is
  built but not installed, at `flowmaster-validate` 3.2.15. 3.2.16 is installed. Its line 90 also
  describes the check more narrowly than the code implements it.
- **The Hub's current-selection paragraph is stale on AF-004's subject.** It says "one `Lifecycle:`
  line in each of the 55 bodies" (Notion: Glow Operations Hub § Current selection — GCFPE-20260914.1
  / 091426.1). Round 28 removed the header occurrence from all 55.
- **`change-flow` points at the wrong current contract.** `skill:change-flow:559` loads
  `gcfpe-current-direct-handoff-contract.json` as the current overlay. That file describes 091326.2,
  54 members, with no PR-35. `:278` still calls 091426.1 a reserved successor, although it was
  promoted on 2026-09-21 (`D17`).

### What was deduplicated against

- **Open Modifications:** none. On `main`, `docs/ephemeral/modifications/` holds only
  `MODIFICATION-20260922-af005-workspace-currency-hardening.md`, which is `ABANDONED`. The branch
  `docs/20260923-modification-intake-alpha-feedback-open-items` @ `85e7357` holds six drafts for these
  same entries. All six are `ABANDONED`, superseded by `D21` (`gcfpe.decision-record.md:1124-1125`).
  `docs/20260922-pe36-stage1-modification-format` holds no Modification.
- **Alpha Feedback, AF-001 to AF-012:** no other entry asks for any of these outcomes. AF-001,
  AF-002, AF-003 and AF-005 are WON'T DO. AF-007 is RESOLVED; it overlaps ITEM-02 on prompt storage
  only. AF-010 is merged into AF-009: points 3 and 4 are ITEM-11 and ITEM-12, and point 5 folds into
  AF-006 and AF-008.
- **`reconciliation-backlog.md`:** nothing. Every entry concerns retired drainage, Drive storage or
  stale status.
- **`gcfpe.decision-record.md`, D1–D21:** no ruling for or against any item. The nearest:
  - `D4`: ITEM-10
  - `D11` and `D17`: ITEM-19
  - `D13`, which restored the PR-30 → PR-35 edge: ITEM-14
  - `D14` and `D20-B`: ITEM-01
  - `D18`: merge is Nathan's (ITEM-18), and the Flow Index holds Alpha state (ITEM-03)
  - `D21-D`, a handoff only for a fresh session: governs the MGMT process only
- **Prior triage records:** `docs/ephemeral/pe36.mgmt-redesign/TRIAGE-COMPARISON-v1.0.md` and
  `TRIAGE-RERUN-COMPARISON-v1.0.md` were read as claims to re-verify, not as evidence. Every
  disposition above rests on its own citation. Two of their calls did not survive:
  - ITEM-14: they had it already true, and PR-30 still holds review correction.
  - AF-008's "only in the handoff" example: see *Noticed*.

### The parts

Twelve parts. Each lands whole or not at all. All land independently except three, each of which
waits for one other part: PART-04, PART-07 and PART-09.

| part | items | why these land together | order |
|---|---|---|---|
| PART-01 | ITEM-01 | One scan and its repair. What the repair is cannot be known until the scan runs. `ANALYZE` decides whether a repair rides in this part or becomes a Modification with `spawned_from` set | — |
| PART-02 | ITEM-03 | One message, said the same way across every surface that speaks to lifecycle sessions | — |
| PART-03 | ITEM-07 | One rule about output artifacts. It can land alone, and it makes nothing worse | — |
| PART-04 | ITEM-04, ITEM-08 | One rule: what a handoff carries. ITEM-08 names identifiers ITEM-04's "only" already leaves out. It is a separate item because its versioned-filename premise brings its own conflicts. Split, the same handoff rule would be applied twice, which is the `D12` error | **after PART-03.** AF-008 orders it: "before handoffs shrink, every kind of fact … needs a home in an artifact". Shrinking first would drop facts |
| PART-05 | ITEM-06 | A presentation rule: where the block sits in the response and whether it is visible. It removes no content, so it does not wait for PART-03 | — |
| PART-06 | ITEM-12 | Recording in-flight decisions. It is useful alone, and it comes before the latitude that relies on it | — |
| PART-07 | ITEM-09, ITEM-10, ITEM-11 | One boundary rule. The latitude (09) is only safe with its limit (10), and the decision tree (11) is the same rule in usable form | **after PART-06.** Latitude without the record loses the accountability AF-009 keeps: "These decisions must be recorded clearly in the implementation report" |
| PART-08 | ITEM-14 | The division of labour between the two phases. It holds in either session model | — |
| PART-09 | ITEM-15 | Reverses a deliberate contract tied to R1 row GCF-17 and to the R1 oracle `flowmaster-validate` pins | **after PART-08.** AF-011's reason for a separate session is that review and CI work differ from implementation. While review corrections still route to PR-30 (ITEM-14), a separate PR-35 session would not isolate that work |
| PART-10 | ITEM-17 | Useful in either session model: the current single session could subscribe too. So it does not wait for PART-09 | — |
| PART-11 | ITEM-18 | Separate from the session change. It needs a way to observe the merge, which is prohibited today, and a replacement for Nathan's merge assertion as PR-40's trigger | — |
| PART-12 | ITEM-19 | One release rule. It meets `prompt-body-content-policy.md:31` against `:33-34` (see ITEM-19) | — |

**They run together because they were handed in together** (`D21-A`). **Parts that touch the same
skill ship in one package, one review and one install** (template rule 7). By apparent surface:

- `glow-hde-pr-development`: PART-03, PART-04, PART-05, PART-06, PART-07, PART-08, PART-09, PART-10, PART-11, and perhaps PART-02
- `change-flow` and its bundled contract: PART-04, PART-05, PART-07, PART-08, PART-09, PART-11, PART-12, and perhaps PART-02
- `flowmaster-validate`, through its bundled contract, fixtures and pinned release: PART-04, PART-07, PART-08, PART-09, PART-11, PART-12, and PART-01 only on a false positive
- `session-relay-flowmaster`: PART-02, PART-04, PART-05, PART-09, PART-11
- the graph parts: PART-04, PART-07, PART-08, PART-09, PART-10, PART-11, PART-12

The two bundled contracts are byte-identical (SHA-256 `2b78f877e7a31efb…`), so a part touching one
touches both.

**Tensions between parts, for `ANALYZE`:**

- **PART-02 and PART-04 — Nathan's question.** AF-006 asks that future handoffs "communicate" the
  Notion read-only default. AF-008 says a handoff "must not restate … workflow rules" that the named
  prompt already holds. The entries do not say which governs. **Question for Nathan: must a
  future handoff state the Notion read-only default, or is it enough that no handoff ever directs a
  routine Notion write?**
- **PART-02 and `D18`.** The Flow Index Alpha-state block is a destination `D18` set, and it carries
  exactly the per-step record AF-006 does not want in Notion. It is already stale (see *Noticed*).
- **PART-04 and PART-09.** A separate PR-35 session has to find the existing PR. Today its entry
  package carries branch, worktree and remote head. After PART-04, only the PR reference or an
  artifact would locate it. In a unit with several ordered PRs, it would also have to be told which
  PR it continues. ITEM-16 must stay true through both.
- **PART-04 internally.** The versioned-filename premise meets `session-relay-flowmaster:259` and
  the `glow-artifact-storage` Drive naming rule.
- **PART-10 and PART-11.** AF-011 makes PR-35 the actor that dispatches after merge, so PR-35 must
  observe the merge. The PR subscription ITEM-17 asks for is the only PR-observing mechanism the
  request names. If `ANALYZE` uses it for that, PART-11 lands after PART-10.
- **PART-08, PART-09 and PART-11** all change PR-35's contract: its duties, its session and its
  exit. They land in that order where ordered, but the PR-35 body and the skill change once for
  all three, under rule 7.
- **PART-11 and merge authority.** Merge stays Nathan's (`D18`). Automatic dispatch can only follow
  his merge, never cause it. What then asserts the merge to PR-40 is open, given the rule never to
  infer merged state from a surface.
- **PART-12 and every other part.** Whether this Modification's own prompt edits land in place or
  as a new release decides whether PART-12 changes this run's cost. PART-12 is not ordered first,
  because the other parts can land under today's release mechanism.
- **PART-03 and PART-06** both change what `PR_IMPLEMENTATION_RESULT` carries: every result, and
  the in-flight decisions.
