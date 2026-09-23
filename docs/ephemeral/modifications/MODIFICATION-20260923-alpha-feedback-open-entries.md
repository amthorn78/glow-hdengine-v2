---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
status: PLANNED
targets: [prompt, skill, rule, graph, registry, notion_control]
gate_tier: 2
closure:
  upstream: [DOC-10, DOC-20, ESC-40, GCFPE-MGMT-10, IA-30, MGR-10, OPS-20, PR-10, PR-20, PR-30, PR-35, PR-40, QA-20, RS-10, RS-20, RS-30, RS-40]
  downstream: [DOC-10, ESC-25, ESC-30, OPS-10, PR-10, PR-20, PR-30, PR-35, QA-10, QA-20, RS-10, RS-20, RS-30, RS-40]
  state_sharers: "closure.py over PR-10 PR-20 PR-30 PR-35 PR-40 RS-10 RS-20 DOC-20 OPS-30 QA-10, pasted in §A; the Tier 2 parts take the release-wide gate instead"
readiness: NEEDS_RULING
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 9
item_count_at_approval: 16
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
  - id: ITEM-20
    statement: "The flowmaster-validate skill states the prompt-corpus rule as D22 now has it: a transient file the tooling makes in order to read a body is part of the read, and only a standing copy is prohibited."
    source: "Product Owner, 2026-09-23, added at ANALYZE (D22)"
    disposition: ""
parts:
  - id: PART-01
    name: "Scan the 40 unread bodies for a decorated governance line, and repair what it finds"
    items: [ITEM-01]
    class: B
    after: []
  - id: PART-02
    name: "Say the Notion read-only default the same way everywhere"
    items: [ITEM-03]
    class: B
    after: []
  - id: PART-03
    name: "Every result lives in its output artifact"
    items: [ITEM-07]
    class: A
    after: []
  - id: PART-04
    name: "A handoff carries only what the receiver cannot find elsewhere"
    items: [ITEM-04, ITEM-08]
    class: A
    after: [PART-03]
  - id: PART-05
    name: "The handoff block is visible, not buried"
    items: [ITEM-06]
    class: A
    after: []
  - id: PART-06
    name: "Implementation reports record in-flight decisions"
    items: [ITEM-12]
    class: A
    after: []
  - id: PART-07
    name: "Implementation latitude and the rescope boundary"
    items: [ITEM-09, ITEM-10, ITEM-11]
    class: A
    after: [PART-06]
  - id: PART-08
    name: "PR-35 alone handles review findings and CI"
    items: [ITEM-14]
    class: B
    after: []
  - id: PART-09
    name: "PR-35 in its own session"
    items: [ITEM-15]
    class: A
    after: [PART-08]
  - id: PART-10
    name: "The PR-35 session subscribes to its PR"
    items: [ITEM-17]
    class: A
    after: []
  - id: PART-11
    name: "Automatic PR-40 dispatch after merge"
    items: [ITEM-18]
    class: A
    after: [PART-10]
  - id: PART-12
    name: "Version bump instead of a sibling for unchanged prompts"
    items: [ITEM-19]
    class: A
    after: []
  - id: PART-13
    name: "flowmaster-validate states the D22 corpus rule"
    items: [ITEM-20]
    class: B
    after: []
request: |
  Run the open Alpha Feedback items through triage: AF-004, AF-006, AF-008, AF-009 (it now includes AF-010's merged scope), AF-011, AF-012.
  They are on "GCFPE Alpha Feedback — Deferred Items — 091426.1", Notion page 3df4590a05eb8111a6a5f67cb82f96f6.
requested_by: Nathan
analyze_approved_by: Nathan
analyze_approved_date: 2026-09-23
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: [MODIFICATION-20260923-pr40-reject-replans]
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

## §A — Analysis

Written 2026-09-23 by `MODE = ANALYZE`, running the proposed `GCFPE-MGMT-10` body (Notion
`3e34590a05eb811b93d2da9b4ef8106d`) in the same session as triage, against `main` @ `a63bf80`.

**What changed after intake, in this mode.** Four things:

- **ITEM-20 / PART-13 were added** on Nathan's instruction. `flowmaster-validate` still states the old
  corpus rule, and `D22` changed it.
- **Two of the intake tensions are settled by Nathan:**
  - A future handoff does **not** restate the Notion read-only default. It is enough that no handoff
    directs a routine Notion write (PART-02 against PART-04).
  - The stale Flow Index Alpha-state record is out of this run.
- **`D22` was ruled mid-analysis** (PR #475). Without it, 13 bodies over the harness's ~30 KB
  save threshold could not be read.
- **Two harness behaviours were found:**
  - The harness saves any large fetch to a session file.
  - It refuses a session's `rm` on that file.

### Scope, and how it was measured

**Method: broad match minus permitted exceptions, over every body, never over a phrase list.**

**Who read the bodies.** All 55 `091426.1` bodies were read from Notion:
- 42 small bodies by four workers, 11 bodies each, all read inline;
- 13 large bodies by two workers under `D22`.

**What each worker did.**
- It applied one broad probe per part to every line. For example, every line containing "Notion", and
  every line containing "rescope|RS-10|RS-20|material|in-scope|boundary".
- It subtracted the stated exceptions: read and navigation lines, and verbatim boilerplate counted
  separately.
- It returned the survivors with excerpts, and any in-scope line its instructions did not cover.

The skills, graph parts, registry and the bundled contract were measured by `grep` in this session.

**One limit.** `QA-10` was read in one pass, with lines cut at 400 characters. Its figures are lower
bounds, and three long lines of its handoff and result sections were seen only in part.

| part | measured reach | method note |
|---|---|---|
| PART-01 | **40 bodies**, named: the 55 minus the 15 read in rounds 28–30 (`REPORT-r30-CORRECTIONS.md:155-157`). 11 of the 40 are over the save threshold | exact set, not a probe |
| PART-02 | **Bodies:** 8 with a live Notion-as-state line — "Concise authorized operational state and pointers remain `CONTROL_NOTION`" in `PR-10`, `PR-20`, `PR-30`, `PR-40`, `OPS-10`, `OPS-20`, `OPS-30`, plus `QA-10` "Notion and repository persistence" (6 lines). 10 more (`CF-*`×8, `CF-PO-10`, `MGR-10`) allow "a direct Notion URL for a Notion-resident artifact" in their handoff rule. **Skill:** `session-relay-flowmaster:268` and its `CONTROL_PLANE: NOTION` field (`:353`). **Notion:** the Change Flow Overview's Alpha Test 1 tracking block. **0 bodies** tell a session to create a Notion page, status, log or handoff record | "Notion" lines minus identity, URL, navigation and "prompt bodies live in Notion" |
| PART-03 | **53 bodies**, every nonterminal one, and each hands facts forward in its handoff. Test results must land in the artifact in only 3 bodies (`QA-100`, `QA-120`, `RS-40`). `PR-30`'s `PR_IMPLEMENTATION_RESULT` names "local tests" but not their outcome. The Hub worker standard allows "the handoff or the artifact" | output-artifact and result sections, per body |
| PART-04 | **53 handoff field lists, in about seven wording variants**, plus `handoff_contract.required` (`docs/graph/parts/global.json:358-365`), `contract:17615`, `glow-hde-pr-development:22`, `:82`, `:162`, `change-flow:295`, `:313`, and the Hub 16-section maintenance standard. **Branch or commit** is required in 2 bodies (`PR-35`: worktree, branch, PR, head; `PR-30`, step 6) and conditional in 2 (`IA-10`, `IA-20`). It is otherwise absent from bodies and present in the skill and reviewer surfaces. `GCFPE-MGMT-10` (live) has no handoff rule; `D20` replaces it | handoff-rule section, per body |
| PART-05 | **55 bodies** have no rule on how much text surrounds the block. **16** say "contain" rather than "end with" (`CF-*`×8, `CF-PO-10`, `MGR-10`, `PR-35`, `CL-20`, `CL-30`, `CL-40`, `CL-C-10`, `CL-E-10`). **4** also require the result to "end `ASK OK?`" (`QA-60`, `QA-80`, `RS-10`, `RS-30`), so the final position contradicts itself | placement and length wording |
| PART-06 | `PR-30`, `PR-35`, `RS-40` (`PR_IMPLEMENTATION_RESULT`), and `glow-hde-pr-development:59`. No body requires in-flight design decisions in a result | result-content sections |
| PART-07 | **About 20 bodies** carry a rescope or escalation threshold, and **"material" is defined in none of the 55.** Graph predicates: `PR-10.json:157`, `PR-20.json:157`, `OPS-30.json:175`. Skills: `glow-hde-pr-development:65`, `:128`, `:135`; `change-flow:313`, `:323`, `:453`, `:454`. PR-20 enters RS-10 before Proceed, and PR-30 goes straight to RS-20 after Proceed. That asymmetry is deliberate (`global.json:487-505`) | rescope and boundary lines minus routing-only mechanics |
| PART-08 | `registry:3531` (PR-30 "review-correct"); `glow-hde-pr-development:74-79`; `PR-40`'s `REJECT` → PR-30 route (body, `PR-40.json:165`, `contract:15734`). **`PR-30`'s own body already agrees with AF-011**: "PR-35—not PR-30—owns review retrieval and correction" | review-assignment lines in `PR-30` and `PR-40` |
| PART-09 | **About 17 bodies** state PR-30 and PR-35 as one dedicated session (the shared continuity list, plus the `CL`×5 merge block). Also: `pr_continuity_contract` (`global.json:472-526`); `PR-35.json:190`; registry `:3604-3611`, `:3633`, `:5108`; `glow-hde-pr-development` description, `:53`, `:55`, validator and behaviour cases; `change-flow:301-307`, `:365`; `session-relay-flowmaster:283`; the register and Flow Index wording; and **the R1 oracle row GCF-17**, which pins "Exactly the GCF-14 planning session" | "same session", "dedicated", "PR-35" lines |
| PART-10 | `PR-35`, `RS-40` (the PR-35 phase), `glow-hde-pr-development:112`, `:121`. "subscribe" has **0** hits across all 55 bodies and every skill | exact term |
| PART-11 | `global.json:33-43`, `:299-307`, `:447-471`; `PR-35.json:21`; `RS-40`'s `MERGE_PENDING` route; `DOC-20.json:151`, `:169`; registry `:3710`; `glow-hde-pr-development:110`, `:164`; `change-flow:331`, `:366`; `session-relay-flowmaster:283-285`; the bundled contract. **No merge-observing mechanism exists, and polling for the merge is prohibited** | edges into `PR-40` and no-polling rules |
| PART-12 | **55 bodies × 5 header lines** (title, `Prompt Version:`, `Set:`, `Ecosystem release:`, URL title); registry `required_regex` on 55 rows (`registry:240`); `candidate_version` in 55 graph parts; `contract:3095`; the Alpha checklist; the register and catalog. **Not measured:** the TW prompt ecosystem and the PE Metaprompt, both named by the item's "across all prompt ecosystems". The `CL-*` "complete sibling" save rules concern artifact successors, not prompt siblings (`NAME-001`), and are excluded | header lines; `sibling` 0 hits in bodies |
| PART-13 | `flowmaster-validate/SKILL.md:55-60`, `:231-232` ("a file persists, and a persisted corpus is what the policy forbids") | exact term |

### Per part: closure, tier, class and targets

Closure is `closure.py` over the graph parts. **It counts prompt-to-prompt edges only.** Two
consequences for this Modification:
- `PR-35 → PR-40` is a boundary edge (`NATHAN_MANUAL_MERGE_ASSERTION`), so `PR-40` shows one
  upstream, `DOC-20`. PART-11 would turn that boundary into a prompt edge and grow both radii.
- A skill target has no graph part, so its closure is undefined rather than empty.

```
PR-10   upstream 3  GCFPE-MGMT-10, IA-30, PR-40      downstream 3  PR-10, PR-20, RS-10              sharers 19  radius 24
PR-20   upstream 2  DOC-10, PR-10                    downstream 2  PR-20, RS-10                     sharers 19  radius 21
PR-30   upstream 4  ESC-40, PR-40, RS-20, RS-40      downstream 3  PR-30, PR-35, RS-20              sharers 3   radius 7
PR-35   upstream 4  ESC-40, PR-30, RS-20, RS-40      downstream 2  PR-35, RS-20                     sharers 3   radius 6
PR-40   upstream 1  DOC-20                           downstream 3  PR-10, PR-30, RS-10              sharers 6   radius 9
RS-10   upstream 8  DOC-10 DOC-20 OPS-10 OPS-20 OPS-30 PR-10 PR-20 PR-40   downstream 1  RS-20       sharers 1   radius 10
RS-20   upstream 5  PR-30, PR-35, RS-10, RS-30, RS-40  downstream 4  PR-30, PR-35, RS-30, RS-40     sharers 4   radius 9
DOC-20  upstream 0                                   downstream 4  DOC-10, PR-40, QA-10, RS-10      sharers 23  radius 25
OPS-30  upstream 1  OPS-20                           downstream 3  ESC-25, OPS-10, RS-10            sharers 4   radius 8
QA-10   upstream 3  DOC-20, MGR-10, QA-20            downstream 2  ESC-30, QA-20                    sharers 0   radius 4
```

| part | class | tier | targets | why |
|---|---|---|---|---|
| PART-01 | **B** — applies `prompt-body-content-policy.md` | 0 for the scan | prompt (read), skill only on a false positive | a scan changes nothing; a repair is discovered scope (below) |
| PART-02 | **B** — applies the 2026-09-22 Notion policy | 2 | skill, prompt (18 bodies), Notion control | one rule over many prompts; changes what agents do with state, not routing |
| PART-03 | **A** — a new rule: no fact lives only in a handoff | 2 | prompt (53), skill, rule, Notion control (Hub standard) | changes what prompts produce |
| PART-04 | **A** — reverses the "complete, self-contained handoff" rule | 2 | graph (`handoff_contract`), prompt (53), skill, registry, rule | the graph part moves; one rule over the corpus |
| PART-05 | **A or B — genuinely ambiguous.** B if it only extends the existing length rule (`glow-po-reporting:52`) to lifecycle returns; A if it sets a new placement rule. I recommend treating it as A, because the 4 `ASK OK?` contradictions need a ruling on which comes last | 2 | prompt (~20), skill | reaches many prompts |
| PART-06 | **A** — new required content in `PR_IMPLEMENTATION_RESULT` | 1 | prompt (3), skill | changes what 3 prompts produce |
| PART-07 | **A** — reverses the work-unit rescope threshold | 2 | graph (3 predicates), prompt (~20), skill, rule | reaches many prompts; graph parts move |
| PART-08 | **B** — `PR-30`'s body, `D13` and the skill (`:53`) already give review to PR-35; three surfaces lag | 1 | registry, skill, graph (`PR-40` route), prompt (`PR-40`) | the `PR-40` part moves; radius 9 |
| PART-09 | **A** — reverses a deliberate contract and an R1 row | 2 | graph, prompt (~17), registry, skill (+ validator, R1 oracle), Notion control (register/Flow Index wording), rule | corpus-wide, and protected identity |
| PART-10 | **A** — new behaviour | 1 | prompt (`PR-35`, `RS-40`), skill | may change `REMOTE_EVIDENCE_PENDING` routing |
| PART-11 | **A** — reverses `direct_PR35_to_PR40_automatic_edge: false` | 1 | graph, prompt (`PR-35`, `RS-40`, `PR-40`, `DOC-20`), registry, skill | a boundary becomes an edge; the radius is the union of `PR-35` and `PR-40` |
| PART-12 | **A** — changes the release procedure and a binding convention | 2 | prompt (55), registry (55 rows), graph (55), Notion control (register, catalog, checklist), rule | every member |
| PART-13 | **B** — applies `D22` | 0 | skill | no graph part |

**Modification tier: 2.** Parts 02, 03, 04, 05, 07, 09 and 12 are corpus-wide, so this run takes the
release-wide gate once. It must not be paid per part.

### Contradictions and risks

- **The PR-lane parts collide in one skill.** PART-03, 04, 05, 06, 07, 08, 09, 10 and 11 all change
  `glow-hde-pr-development`, and PART-09 changes its **description**, which is the trigger surface
  (`AF-003`). One package, one review and one install, under rule 7. A review that rejects one part's
  edit blocks that part only.
- **PART-09 touches a protected identity.** R1 row GCF-17 is pinned by `flowmaster-validate`'s R1
  oracle (`global.json:551-557`). Separating PR-35 fails the suite until the oracle is re-pinned.
- **PART-11 has no mechanism to build on.** Watching for the merge is prohibited
  (`glow-hde-pr-development:110`; `session-relay-flowmaster:283`, `:285`). Nothing in the flow can
  launch or message a session without the operator (`session-relay-flowmaster:713`;
  `execution-and-delegation-model.md:137-139`). The subscription PART-10 adds is the only PR-observing
  mechanism named, so PART-11 depends on PART-10 if it uses it.
- **PART-04 and PART-09 together** leave a separate PR-35 session locating its PR by the PR reference
  or an artifact alone. `ITEM-16` must survive that.
- **"material" is undefined in all 55 bodies.** PART-07 is where it gets defined. Every other threshold
  keeps the undefined word until then.
- **`D22` has no guard** (`GUARD-001`), and its own entry says so.
- **Defect classes matched:**
  - `DERIV-001`: a handoff restating what the named artifact holds (PART-03, 04).
  - `FUNC-001` risk: PART-09 retires "same session" by function, so the sweep must test what an agent
    is told to do, not the phrase.
  - `NAME-001`: artifact "siblings" in `CL-*` are not prompt siblings (PART-12).
  - `SCOPE-001`: avoided above.
- **Noticed, outside this Modification's scope** — each is a candidate for a separate Modification,
  not for widening this one:
  - `QA-10` calls itself read-only and also saves three artifacts;
  - `CL-40` updates a "Candidate CRD Items List" in place without naming its store;
  - `CL-20` directs a board update with no destination;
  - `OPS-10` and `OPS-20` forbid page mentions yet carry and require them;
  - four `CL-*` bodies cite a "PR-40 merge-approval effect … defined above" that is not defined;
  - `change-flow:559` loads the 091326.2 contract as current.

### Open questions for the Product Owner

Three. Each blocks only its own part.

1. **PART-09 — re-pin R1 row GCF-17?** A separate PR-35 session changes an immutable R1 row and its
   pinned oracle. **Recommend yes.** The re-pin rides in the same `flowmaster-validate` package.
2. **PART-11 — what starts PR-40, and what stands in for your merge assertion?** Today your paste of
   the conditional PR-40 block is both the trigger and the assertion. **Recommend:**
   - the PR-35 session, subscribed under PART-10, observes the merge event on its PR and emits the
     PR-40 handoff itself;
   - PR-40 keeps its independent merge verification (event 3), so the observed event replaces the
     assertion and nothing is inferred;
   - dispatch stays a paste, or a session launch where the surface supports one.

   This makes PART-11 **after PART-10**.
3. **PART-12 — where does the version live, and how far does it reach?** **Recommend:**
   - the register and catalog carry membership and version, and bodies drop the release-bound
     header lines (`prompt-body-content-policy.md:113-114`: governance state belongs to its governing
     artifact);
   - `D11`'s `required_regex` moves to the register;
   - PART-12 is limited to GCFPE in this run, because the TW ecosystem and the PE Metaprompt are
     unmeasured.

Settled by approving this analysis, as recommended:
- PART-02 leaves `D18`'s Flow Index block alone. It is a maintenance destination, and AF-006 governs
  lifecycle sessions.
- PART-07 is the PR lane, and the ESC remediation lane keeps its own threshold.
- PART-04 reaches the Hub's maintenance-session handoff standard but not the skill-reviewer prompt,
  which `skill-packaging-and-delivery.md` governs.
- The Class A parts are recorded as one `D23` before execution.

### Readiness and interaction cost

**`NEEDS_RULING`**, with two splits recommended. Readiness is advice and never refuses.

- **Sequential discovery — PART-01's repair.** Whether any repair exists is unknown until the scan
  runs. PART-01 executes the scan here. A leftover or false positive becomes a new Modification with
  `spawned_from` set.
- **Unmeasured scope — PART-12 outside GCFPE.** TW and the PE Metaprompt were not measured. Narrow
  PART-12 to GCFPE, or measure them before PLAN.

```
interaction_cost = open rulings 3 + 2 + review cycles 1 + installs 1 + merges 2  =  9
```

- **Review cycles and installs:** one package set, one §10 review and one install for
  `glow-hde-pr-development`, `change-flow`, `flowmaster-validate` and `session-relay-flowmaster`.
- **Merges:** #474, which holds this record, and the execution PR. #475 (`D22`) is separate and
  already open.
- **What a split would cost.** Moving PART-09, 11 and 12 to a separate run removes the three rulings
  from this run's path. But PART-09 and PART-11 change the same skill as six other parts, so a second
  run would pay its own review, install and merge: **+3**, to save nothing that parts do not already
  isolate. **Keep them together.** A part waiting on a ruling does not hold the others, and PLAN can
  start on the ten that need none.

## §P — Plan

Written 2026-09-23 by `MODE = PLAN`. The analysis was approved by Nathan on 2026-09-23 ("approve,
all agreed"), which settles every recommendation in §A.

### Rulings received with the approval

| question | ruling |
|---|---|
| PART-09: re-pin R1 row GCF-17 | **Yes.** The re-pin ships in the `flowmaster-validate` and `change-flow` packages |
| PART-11: what starts PR-40 | **The subscribed PR-35 session observes the merge event and emits the PR-40 handoff itself.** PR-40 keeps its independent merge verification. Dispatch is a paste, or a session launch where the surface provides one. **PART-11 lands after PART-10** |
| PART-12: where the version lives | **In the register and complete-prompt-set catalog.** Bodies drop their release-bound header lines, and `D11`'s `required_regex` moves to the register. **GCFPE only in this run** |
| Recommended splits | PART-01 scans; any repair becomes a new Modification with `spawned_from` set. PART-12 is narrowed to GCFPE |
| Settled with the analysis | PART-02 leaves `D18`'s Flow Index block alone. PART-07 is the PR lane only. PART-04 reaches the Hub maintenance-session handoff standard, not the skill-reviewer prompt. The Class A parts are recorded as one `D23` before execution |

**Consequence for the parts:** PART-11 now lands after PART-10.

### Canonical wording

Every edit below converges on these texts. They are written once here and never re-authored per
prompt (`ecosystem-change-management.md` §2 Step 3). A worker who finds a prompt where the text
cannot be placed reports it, and does not improvise.

- **C-NOTION** (PART-02):
  > Concise operational state, results and pointers live in the repository under `docs/ephemeral/`.
  > Notion holds the published prompt bodies and the maintenance surfaces a destination rule names;
  > this prompt reads Notion and writes to it only where its task instruction directs a write.
- **C-ART** (PART-03):
  > Before emitting any handoff, write every result this prompt produces — verdict or state,
  > decisions, test and validation results with their outcomes, constraints, unresolved items and
  > owners — into its output artifact, and read it back. The handoff names that artifact; it never
  > carries the only copy of a fact.
- **C-HANDOFF** (PART-04; replaces each body's handoff field list):
  > The block names the exact destination prompt by full name, version and direct Notion URL; the
  > receiving role and session; each input artifact by repository path, with a one-line label; the
  > pull request reference when the receiver continues an existing PR; and, only for a condition
  > those artifacts do not already record, the minimum context it needs. It carries no branch and no
  > commit: an artifact is identified by its versioned filename, and an issued version is never
  > edited. It does not restate history, architecture, decisions, scope, acceptance criteria,
  > workflow rules or artifact contents that the named prompt, canon or files hold. No placeholders,
  > menus, alternate destinations, "above", prior-chat reconstruction or unlinked filenames.
- **C-PLACE** (PART-05):
  > The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a
  > few lines naming what was produced and where; the artifact holds the rest.

  In the four bodies that also "end `ASK OK?`", `ASK OK?` moves to the line immediately before the
  block.
- **C-DEC** (PART-06, added to `PR_IMPLEMENTATION_RESULT`):
  > An *In-flight decisions* section, one row per decision taken without a rescope: what changed,
  > why it was necessary to deliver the approved scope, and what was tested, by test identity and
  > outcome. `NONE` when there were none.
- **C-LAT** (PART-07):
  > **Material** means a change to the Epic-level commitment: its outcome or objective; approved
  > acceptance criteria; a protected architectural, security, data-model or external-contract
  > boundary; the scope of several planned work units; an accepted dependency or cross-team
  > commitment; or budget, schedule or risk needing Product Owner direction. A planned approach
  > found incomplete, impractical or inferior is not by itself material.
  >
  > **Decide it during work:**
  > 1. Is it material, as above? Then take the formal rescope route.
  > 2. Otherwise, is it obvious, necessary to deliver the approved scope, and consistent with the
  >    Epic's objective and controlling constraints? Then decide it, implement it, test it, and
  >    record it under *In-flight decisions*. That holds even if the plan did not anticipate it.
  > 3. Otherwise, do not do it. Record it as a candidate for its owner.
- **C-SESSION** (PART-09):
  > `PR-30` and `PR-35` are two phases of one work unit, run in two dedicated sessions. PR-30's
  > session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from
  > PR-30's handoff, and continues the same pull request. The phases share one `WORK_UNIT_ID`,
  > original Proceed, workspace/worktree, branch, pull request, PR instruction, detailed plan, primary
  > skill authority and recovery lineage; they do not share a session.
- **C-SUB** (PART-10):
  > At entry, subscribe to the pull request's activity where the surface provides it, and act on
  > review, comment and check events as they arrive. Where no subscription is available,
  > `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. Subscribing is not polling.
- **C-DISPATCH** (PART-11):
  > At `MERGE_PENDING`, stay subscribed and return control; do not poll. When the subscription
  > delivers the merge of the identified PR — a merge Nathan performs — emit the `PR-40` handoff:
  > paste-ready, or launched as a new session where the surface provides one. The observed merge
  > event is the trigger, and `PR-40` still verifies the merged state and landed lineage
  > independently. No agent merges.
- **C-VERSION** (PART-12, the release rule):
  > A release's membership and each member's current version live in the register and the
  > complete-prompt-set catalog. A member whose body changes gets a successor page at the new version;
  > a member whose body does not change keeps its page, and the register records it in the new
  > release. Bodies carry no release-bound header line.
- **C-D22** (PART-13): the `D22` wording of `prompt-corpus-policy.md`, *Amendment*.

### Steps

Conventions:
- **Body edits** are made in Notion in place with `notion-update-page` `update_content`, one exact
  `old_str` per edit, and read back after each page.
- **Large bodies** are read under `D22`.
- **Graph parts** are edited by a scripted JSON transform, never by hand, then rebuilt to the
  scratchpad with `glow-graph-contract/scripts/graph_parts.py build`; the proof token is recorded.
- **Skill edits** are made to copies in the scratchpad, packaged once per skill with `skill-creator`,
  and reviewed once (§10) for all four skills together.
- **Registry guards** are each proved by an injected regression that must fail (`D14`).

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| 0 | all | `gcfpe.decision-record.md` | Add **`D23`**, recording the Class A rulings of this Modification: C-ART, C-HANDOFF, C-PLACE, C-DEC, C-LAT, C-SESSION (with the R1 re-pin), C-SUB, C-DISPATCH, C-VERSION | this approval; rule target | `D23` present before any step below runs; `grep -c '^## D23'` = 1 | revert the commit |
| 1 | PART-01 | the 40 bodies named in §A | Read each body; pipe `{id: text}` to `flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract <bundled 091426.1 contract> --bodies-stdin`; read `prompt_bodies_validated` and the `PROMPT_BODY_GOVERNANCE_STATE` errors | Class B; `prompt-validation-procedure.md` | `prompt_bodies_validated` lists all 40 ids. Each `PROMPT_BODY_GOVERNANCE_STATE` hit is quoted with its clause. Result table written to `docs/ephemeral/modifications/evidence/PART-01-scan.md` | nothing written to bodies |
| 1a | PART-01 | — | If step 1 finds any leftover or false positive: open a new Modification with `spawned_from` set to this one and stop PART-01 | §A split | the new file validates | — |
| 2 | PART-02 | `session-relay-flowmaster/SKILL.md:268` | Replace the line with C-NOTION, adapted to the relay's list form ("Notion holds the published prompt bodies and the maintenance surfaces a destination rule names; live task, handoff and decision state lives in the repository under `docs/ephemeral/`"). `:269` (Drive as artifact plane, against `D7`) is out of scope and noted, not edited | Class B | `grep -c "preferred live control plane"` = 0; package review | restore the scratch copy |
| 3 | PART-02 | 7 bodies: `PR-10`, `PR-20`, `PR-30`, `PR-40`, `OPS-10`, `OPS-20`, `OPS-30` | Replace "Concise authorized operational state and pointers remain `CONTROL_NOTION`." with C-NOTION | Class B | readback: `CONTROL_NOTION` absent from all 7 | re-apply the old sentence |
| 4 | PART-02 | `QA-10` | Replace "Notion and repository persistence" (6 occurrences) with "repository persistence, Notion read-only unless a destination rule names the page" | Class B | readback: 0 occurrences of the old phrase | re-apply |
| 5 | PART-02 | 10 bodies: `CF-C-10..40`, `CF-E-10..40`, `CF-PO-10`, `MGR-10` | In the handoff rule, delete ", or its direct Notion URL for a Notion-resident artifact". PART-04 later replaces the paragraph | Class B | readback: phrase absent from all 10 | re-apply |
| 6 | PART-02 | Notion: HDE Change Flow Overview § *CRD Alpha Test 1 — manual run tracking* | Prefix the section with "Historical — Alpha Test 1 is complete (2026-09-07). Not current guidance." | task authorization by this approval | readback | remove the prefix |
| 7 | PART-02 | registry, all 55 rows | Add `forbidden_regex: 'CONTROL_NOTION'` | `D14` guard | governance audit: 0 hits on the edited corpus; injected regression (the old sentence restored in one body) fails | remove the assertion |
| 8 | PART-03 | 53 nonterminal bodies | Insert C-ART as the first sentence of each body's result or output section (the section naming its output artifact) | `D23` | readback: C-ART present in 53 bodies | remove the sentence |
| 9 | PART-03 | Notion: Hub § *Prompt ecosystem worker output standard* | Replace "it goes in the correct numbered section of the handoff or the artifact" with "it goes in the artifact, and the handoff names the artifact" | `D23` | readback | re-apply |
| 10 | PART-03 | `glow-hde-pr-development:155` | Append C-ART | `D23` | package review | scratch copy |
| 11 | PART-03 | registry, 53 nonterminal rows | `required_regex: 'never carries the only copy'` | `D14` | audit passes; injected removal fails | remove |
| 12 | PART-04 | `docs/graph/parts/global.json` `handoff_contract` | `required` becomes: prompt full name/version/URL; receiving role and session; artifact repository paths with labels; PR reference when continuing a PR; exceptional context only. Add `branch`, `commit` and "restated artifact content" to `prohibited`. `complete_paste_ready_prompt` stays true | `D23` | `graph_parts.py build` passes; new proof token recorded; `closure.py` unchanged for all prompts (Tier 2 gate) | revert the part |
| 13 | PART-04 | 53 nonterminal bodies | Replace each body's handoff field-list paragraph (anchored on the sentence containing `NEXT_PROMPT_HANDOFF` and the list that follows) with C-HANDOFF. `PR-30` step 6 and `PR-35`'s *Required inputs* drop branch, worktree, commit and head as handoff content; they stay as entry-recovery checks | `D23` | readback per body: C-HANDOFF present, old list absent. Count 53 | re-apply the old paragraph |
| 14 | PART-04 | `glow-hde-pr-development:22`, `:82`, `:162`; `change-flow:295`, `:313`; `session-relay-flowmaster:259` (runtime handoffs may name versioned files; reusable prompt text stays versionless) | Converge on C-HANDOFF | `D23` | package review; `validate_glow_hde_pr_development.py` literals updated and passing | scratch copies |
| 15 | PART-04 | bundled contract, `transition_contract` (`contract:17594-17618`), in both skills | Regenerate from the graph parts; never hand-edit | `D13`, `D23` | both copies byte-identical to each other; `flowmaster-validate` suite passes | previous contract |
| 16 | PART-04 | Notion: Hub § *Handoff format — required structure* | Replace the 16-section list with C-HANDOFF plus "sections the artifact already holds are named, not repeated" | `D23` | readback | re-apply |
| 17 | PART-04 | registry, 53 rows | `forbidden_regex` on "branch, worktree, commit" inside the handoff paragraph (bounded by `NEXT_PROMPT_HANDOFF`) | `D14` | audit passes; injected regression fails | remove |
| 18 | PART-05 | 55 bodies (block present), and the 4 `ASK OK?` bodies (`QA-60`, `QA-80`, `RS-10`, `RS-30`) | Insert C-PLACE after the handoff rule; in the 4, move `ASK OK?` per C-PLACE. The 16 "contain" bodies now say "ends with" | `D23` | readback: C-PLACE present in the 53 nonterminal bodies; the 4 ordered correctly | re-apply |
| 19 | PART-05 | `glow-hde-pr-development:162`, `change-flow:295`, `session-relay-flowmaster:279` | Converge on C-PLACE | `D23` | package review | scratch copies |
| 20 | PART-06 | `PR-30`, `PR-35`, `RS-40` result sections; `glow-hde-pr-development:59` | Add C-DEC to `PR_IMPLEMENTATION_RESULT` | `D23` | readback; package review | remove |
| 21 | PART-06 | registry: `PR-30`, `PR-35`, `RS-40` | `required_regex: 'In-flight decisions'` | `D14` | audit passes; injected removal fails | remove |
| 22 | PART-07 | bodies with a rescope threshold: `PR-10`, `PR-20`, `PR-30`, `PR-35`, `PR-40`, `RS-10`, `RS-20`, `DOC-10`, `DOC-20`, `IA-30` | Insert C-LAT once, in the section that sends findings to RS; replace "material boundary" in those routing sentences with "material change (as defined above)". `OPS-*`, `QA-*`, `CL-*` and `ESC-*` are out of scope (PR lane only, per the approval) | `D23` | readback: C-LAT present in all 10 | re-apply |
| 23 | PART-07 | graph: `PR-10.json:157`, `PR-20.json:157` edge conditions | "a material change to the Epic-level commitment, as C-LAT defines it" | `D23` | build passes; the two parts moved; closure over the radii of `PR-10` (24) and `PR-20` (21) passes | revert the parts |
| 24 | PART-07 | `glow-hde-pr-development:65`, `:128`, `:135`; `change-flow:313`, `:323`, `:453-454` | Converge on C-LAT, and add the three-step decision tree | `D23` | package review | scratch copies |
| 25 | PART-07 | registry: the 10 rows | `required_regex: 'Decide it during work'` | `D14` | audit passes; injected removal fails | remove |
| 26 | PART-08 | registry `:3531` | "Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35" | Class B | `grep -c review-correct registry` = 0 | revert |
| 27 | PART-08 | `glow-hde-pr-development:79` | "Bundle related implementation changes into one locally verified push when practical." | Class B | package review | scratch copy |
| 28 | PART-08 | `PR-40` `REJECT` → PR-30 route | **No change here.** The route runs after merge, when no open PR exists, so it is not PR-35's review work. Nathan ruled on 2026-09-23 that it re-plans through PR-20 in a new session. That change is `MODIFICATION-20260923-pr40-reject-replans`, which shares this package. EXECUTE records `NOT_APPLICABLE` here, with that pointer | Class B | EXECUTE records the disposition | — |
| 29 | PART-09 | graph `global.json` `pr_continuity_contract` | Remove "dedicated PR-development session" from `shared_exactly_one`; set `added_boundaries.session` = 1 for the PR-30 → PR-35 edge; `PR-35_same_r1_row_as_PR-30` stays true (same R1 row, new session) | `D23` | build passes; new proof token; Tier 2 gate | revert the part |
| 30 | PART-09 | graph `PR-35.json` | `session_class` = `DEDICATED_PR_REVIEW_SESSION`; `receiving_role` = "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request."; `adds_session` = true | `D23` | build passes | revert |
| 31 | PART-09 | graph `PR-30.json` (edge to PR-35), `RS-40.json` (PR-35 phase) | The PR-30 → PR-35 handoff targets the PR-35 session; RS-40's `PR_RETURN_PHASE: PR-35` resumes in the PR-35 session | `D23` | build passes; closure over `PR-30` (7) and `PR-35` (6) | revert |
| 32 | PART-09 | ~17 bodies stating one shared session (the continuity-list paragraph) | Replace with C-SESSION | `D23` | readback: "dedicated PR-development session" absent from every continuity list | re-apply |
| 33 | PART-09 | registry `PR-35` `:3604-3611`, `:3633`; `RS-40` `:5108` | `session_class` → `DEDICATED_PR_REVIEW_SESSION`; input "`session_disposition: NEW_DEDICATED`"; remove "session" from forbidden additions | `D23` | audit passes | revert |
| 34 | PART-09 | R1 oracle row GCF-17 (`flowmaster-validate` and `change-flow` references) | Re-pin: GCF-17's `session` gains "PR-35 runs in its own dedicated session for the same work unit". Recompute the row's `source_row_sha256` and the oracle SHA-256; replace `52807e58…` everywhere it is pinned (`flowmaster-validate` SKILL.md `:149`, `validate_gcfpe_20260914.py` ×3, `validate_gcfpe_current.py`, `global.json` `protected_identities`) | Nathan's ruling | `grep -rc 52807e58` = 0 across both skills and the graph parts; `flowmaster-validate` full suite passes; injected regression (old row text with the new pin) fails | restore the old oracle and pins |
| 35 | PART-09 | `glow-hde-pr-development` description (`:3`), `:53`, `:55`, `:82`, `:164`; validator literals `:32-34`; `behavior-cases.md`; `change-flow:301`, `:303`, `:307`, `:365`; `session-relay-flowmaster:283` | Converge on C-SESSION. The description changes: it is the trigger surface | `D23` | package review; validator passes with updated literals; injected old literal fails | scratch copies |
| 36 | PART-09 | Notion: register § *Current explicit membership* and Flow Index § *Native flow changes* | "same-session PR-35" → "PR-35 in its own dedicated session" | maintenance destination rule | readback | re-apply |
| 37 | PART-10 | `PR-35` body, `RS-40` (PR-35 phase), `glow-hde-pr-development:112`, `:121` | Insert C-SUB | `D23` | readback; package review | remove |
| 38 | PART-11 | graph `global.json` `post_merge_three_event_contract`, `_other_edges` and `boundary_transitions` (`:33-43`, `:299-307`, `:447-471`), `PR-35.json:21`, `RS-40` `MERGE_PENDING` | `event_2` becomes "merge of the identified PR observed by the subscribed PR-35 session (Nathan merges)"; `direct_PR35_to_PR40_automatic_edge` = true; the boundary `NATHAN_MANUAL_MERGE_ASSERTION` becomes a prompt edge PR-35 → PR-40, condition "merge event observed", transport `COMPLETE_NEXT_PROMPT_HANDOFF` | `D23` | build passes; `closure.py PR-40` now shows `PR-35` upstream; closure over the new radius | revert the parts |
| 39 | PART-11 | `PR-35`, `RS-40`, `PR-40`, `DOC-20` bodies; registry `PR-40` inputs `:3710` | Insert C-DISPATCH in PR-35 and RS-40. PR-40's input becomes "the observed merge event, or Nathan's assertion where no subscription existed" | `D23` | readback; audit passes | re-apply |
| 40 | PART-11 | `glow-hde-pr-development:110`, `:164`; `change-flow:331`, `:366`; `session-relay-flowmaster:283-285` | Converge on C-DISPATCH; keep every no-merge and no-polling sentence | `D23` | package review | scratch copies |
| 41 | PART-12 | `prompt-body-content-policy.md` `:33-34` | Remove `Prompt version:` and `Ecosystem release:` from the legitimate list; add C-VERSION | `D23` | the policy reads consistently; `grep` shows no conflicting line | revert |
| 42 | PART-12 | 55 bodies | Delete the header lines `Prompt Version:`/`Prompt version:`, `Set:` and `Ecosystem release:`. Titles are unchanged | `D23` | readback: 0 such lines in 55 bodies | re-apply from the register's values |
| 43 | PART-12 | registry, 55 rows | Remove `required_regex` `Prompt [Vv]ersion: 091426.1` and `Ecosystem release`; add `forbidden_regex` for those header keys | `D23`, `D14` | audit passes; injected header line fails | restore |
| 44 | PART-12 | Notion: register and complete-prompt-set catalog; Alpha checklist line "All 55 successor prompts are complete versioned siblings" | Add a per-member `current_version` column (all `091426.1` now), plus C-VERSION as the release rule. The checklist line is marked superseded by `D23` | maintenance destination rule | readback | revert |
| 45 | PART-13 | `flowmaster-validate/SKILL.md:55-60`, `:231-232` | Replace "a file persists, and a persisted corpus is what the policy forbids" with the C-D22 reason: "a path option invites a standing directory; a transient read file is allowed under `D22`" | Class B | package review | scratch copy |
| 46 | gate | release-wide | One gate for the Tier 2 run, run once: graph rebuilt against its new proof token; `closure.py` over every changed prompt; `flowmaster-validate` full suite; governance audit (`amthor-workspace-governance-audit`) over all 55 bodies, with every new guard's injected regression failing; `modification_validate.py` | Tier 2 | all pass, counts recorded in §E | fix within the failing part, or block it |
| 47 | skills | `glow-hde-pr-development`, `change-flow`, `flowmaster-validate`, `session-relay-flowmaster` | Package once each; one filled `reviewer-prompt-template.md`; one independent §10 review for all four | rule 7 | verdict `SKILL_FIT_CONFIRMED` bound to the four digests | fix and re-review, or ship without the rejected part (Nathan's choice) |
| 48 | record | this Modification, §E; Alpha Feedback page (AF-004, 006, 008, 009, 011, 012 dispositions) | Record the dispositions | Alpha feedback list is a maintenance destination | readback | — |

**Order.** 0 first. Then the parts in any order, except:
- PART-04 (12–17) after PART-03 (8–11);
- PART-07 (22–25) after PART-06 (20–21);
- PART-09 (29–36) after PART-08 (26–28);
- PART-11 (38–40) after PART-10 (37).

Step 46 runs once, after every body, graph and registry step. Step 47 follows step 46.

### Product Owner actions

- **Merge** the execution PR (repository: decision record, policy, graph parts, registry, evidence).
  Verified by the merge commit on `main`.
- **Install** the four `.skill` packages after the §10 verdict. Verified by comparing each installed
  tree's freeze digest (`freeze.py`) to the packaged digest.
- **Merge #474** (this record) and **#475** (`D22`) whenever you want them preserved.

### Explicitly not in scope

- The Flow Index Alpha-state block (`D18`).
- PART-07 outside the PR lane: `OPS-*`, `QA-*`, `CL-*`, `ESC-*`.
- The TW ecosystem and the PE Metaprompt, for PART-12.
- Any repair PART-01 finds: that becomes a new Modification.
- The six out-of-scope defects noted in §A.
- `session-relay-flowmaster:269` (Drive as artifact plane).
- Renaming prompt pages.
