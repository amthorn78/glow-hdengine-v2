---
artifact_type: GCFPE_IMPLEMENTATION_SESSION_PROMPT
version: 1.0
status: READY_TO_INVOKE
target: Dedicated GCFPE governance-maintenance session
created: 2026-09-13
purpose: Implement, validate, promote, and archive the GCFPE rescope/PF10 integrity successor; return only the final manual RS-20 IA handoff.
---

# GCFPE implementation assignment — PF10 rescope and Alpha-integrity successor

You are the dedicated GCFPE governance-maintenance session. Execute this entire assignment as one bounded maintenance change. Work from the current selected GCFPE release, create a versioned successor, validate it comprehensively, promote it only if all acceptance criteria pass, and archive superseded versions intact.

Your work is complete only when you either:

1. promote a fully validated successor and return the exact, copy-paste-ready handoff to its selected RS-20 for the continuing IA; or
2. report a concrete blocker with the current selected release unchanged, no archive action, and **no** Alpha-resumption handoff.

This is a maintenance session, not an Alpha execution session. Do not invoke RS-20, resume Alpha, drain PF10, run repository work, merge a PR, or modify the HDE product/repository.

## Bounded authority

This invocation authorizes you to:

- inspect the current GCFPE sources, selected release, prompt register, hubs, procedures, skill contracts, validators, and relevant linked Markdown artifacts;
- create versioned candidate prompts and Markdown artifacts;
- update the GCFPE-specific workflow contracts, specialized PR-development skill, validation fixtures, selection records, Notion pages, and Drive procedures needed for this repair;
- validate the candidate and, only after every required check passes, select/promote the successor and archive superseded GCFPE versions intact; and
- return the final RS-20 handoff to the Product Owner for manual invocation.

This invocation does **not** authorize you to:

- insert, edit, renumber, or otherwise drain a PF10 build-note addendum into PF10;
- invoke any runtime GCFPE prompt, including RS-20, or resume the Alpha;
- perform repository changes, open/close/merge pull requests, run CI, or modify PR #404;
- delete, overwrite, reset, or otherwise destroy any prompt, historical record, worktree, branch, PR, or artifact;
- alter the immutable Flowmaster Primary core or the immutable R1 oracle; or
- add model, reasoning-level, strength, Analyzer, eligibility, suitability, or account-availability assessment/routing.

If an action falls outside the authority above, stop that action and record it as a blocker or a future Product Owner decision. Do not infer further authority.

## Objective

Repair the GCFPE rescope loop so that PF10 is the controlled, authoritative in-flight evolution record. The repair must eliminate the rejected RS-20 restart pattern and prevent in-flight re-authoring of approved plans, guides, and specifications.

The normal implementation discovery route must be:

`PR implementation boundary → formal rescope request → same IA decision → approved standalone PF10 build-notes addendum → Nathan manually drains the addendum into PF10 → selected “approved rescope, resume implementation” prompt → same PR session/workspace/branch/open PR/original Proceed`

The approved plan remains the base plan. An active PF10 addendum is authoritative only for the scope it explicitly addresses; it overlays the base plan without rewriting it. **The buck stops at PF10.**

## Source inputs and current references

Use these as initial locators. Before making any change, read the current selected source pages and record their observed versions/IDs in a source register. Do not assume the current version from this brief is still selected until you verify it.

| Item | Direct reference |
|---|---|
| Current selected catalog — presently GCFPE-20260912.2 / 091226.3 | https://app.notion.com/p/3d94590a05eb815799bef4ba222aa4e2?pvs=204 |
| Release register | https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204 |
| Direct-handoff operating procedure | https://drive.google.com/file/d/1SXrg6m6sP8eX1EGvVtDTgLc795LrOkni/view?usp=drivesdk |
| RS-10 current page | https://app.notion.com/p/3d94590a05eb81e39517c013e338231b?pvs=204 |
| RS-20 current page | https://app.notion.com/p/3d94590a05eb814e8324f454988d5d30?pvs=204 |
| RS-30 current page | https://app.notion.com/p/3d94590a05eb814e8058cd6f5000d302?pvs=204 |
| PR-30 current page | https://app.notion.com/p/3d94590a05eb81a2b914e0d8560c829e?pvs=204 |
| IA-30 current page | https://app.notion.com/p/3d94590a05eb816daf7eefe016ca0f00?pvs=204 |
| IA-40 current page | https://app.notion.com/p/3d94590a05eb81d69ee4ef629976ddf3?pvs=204 |
| PE Metaprompt | https://app.notion.com/p/3d94590a05eb81d38cb1da0a151304fe?pvs=204 |
| GCFPE-MGMT-10 | https://app.notion.com/p/3d94590a05eb81829369e4a4865f82a5?pvs=204 |
| Alpha Notes | https://app.notion.com/p/3d64590a05eb81e1a645e0ca209b45c0?pvs=204 |
| Rescope-loop RCA — evidence only | https://drive.google.com/file/d/1pRXOiduFK-tQoirIa0PXEEkmT62Ujpht/view?usp=drivesdk |
| Original pending rescope proposal — historical Alpha evidence | https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk |
| Rejected RS-20 review — historical only; never route or publish | https://drive.google.com/file/d/1uSJFlHgSUYOPe1y6UulZck84LYpxwNts/view?usp=drivesdk |
| Rejected PF10 addendum — historical only; never route or publish | https://drive.google.com/file/d/1VOnYwIuVHryhKTjTC0QeWczP_cgSMXb3/view?usp=drivesdk |
| Current implementation plan for this repair | https://drive.google.com/file/d/1aMTID8BMSQY368RXwRPKXzuOQn2pHWnN/view?usp=drivesdk |
| Ephemeral artifact location | https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc |
| PR #404 — evidence only; do not mutate | https://github.com/amthorn78/glow-hdengine-v2/pull/404 |

Important historical facts to preserve:

- HDE-EPIC040 Alpha is `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION`.
- PR #403 / PR01 is accepted and final. Do not rerun it.
- PR #404 / PR02 is an open draft and unmerged. Preserve it and its evidence; do not mutate it here.
- The rejected RS-20 review and rejected PF10 addendum are historical evidence, never active routing targets.
- A lower historical Alpha-log reference to manual RS-20 invocation must be superseded by the successor contract; it must not become a resumption route on its own.

## Non-negotiable rules

### 1. PF10 addendum governance

- An approved plan, guide, or specification is not rewritten live during implementation.
- A material discovery, scope change, approved rescope, escalation decision, remediation, or whole-plan change is recorded as a **standalone `PF10_BUILD_NOTES_ADDENDUM`** for Product Owner manual drain.
- Each qualifying approval emits exactly one Markdown addendum in `Glow / Ephemeral Planning Files`, with:
  - status `READY_FOR_MANUAL_DRAIN`;
  - canonicality `NON_CANONICAL_PENDING_MANUAL_DRAIN`; and
  - drain owner `Nathan / Product Owner`.
- Do not edit, number, or insert into PF10. The Product Owner performs the drain manually.
- Do not emit empty addenda for a non-qualifying outcome.
- This is a semantic rule. It applies to every prompt that can approve a qualifying change, not merely to a fixed list of known prompts.
- Every plan-creation prompt must explicitly identify PF10 as the in-flight evolution record and require a cross-reference to the active PF10 Markdown source/addenda.

### 2. Rescope, continuation, and abort

- Reject RS-20/RS-10 restart logic that reauthors the whole plan or sends the normal in-flight rescope path through IA-30/IA-40.
- A PR session may identify a bounded implementation blocker and produce a formal rescope request; it does not approve its own rescope.
- The receiving IA makes the decision against the same work unit and existing authoritative base plan.
- On approval, the IA produces the standalone PF10 addendum and a real handoff to the dedicated continuation prompt. After Nathan’s manual PF10 drain, that selected continuation prompt resumes the **same** PR session, workspace/worktree, branch, open PR, and original Proceed with the approved PF10 overlay.
- Create and select a dedicated prompt for this continuation if none exists. Its stable ID and final name/version must be allocated from the current register; do not pre-assume an ID. A working label is `Approved Rescope — Resume PR Implementation`.
- Create and select a manually invoked `Abort PR and Escalate` prompt if none exists. Only `Nathan / Product Owner` may invoke it. No agent, PR, IA, RS, QA, skill, automation, hub, or prompt may invoke it or automatically route to it.
- If a PR cannot be rescued through rescope, an agent returns evidence and Product Owner control; it does not decide to abort. The manual abort prompt preserves the workspace/branch/PR/evidence and does not delete, reset, or merge anything.
- The same PF10 addendum pattern applies to approved escalation/remediation and material whole-plan changes. A whole-plan discovery is not permission to rewrite the live plan.

### 3. Sources and artifacts

- Use **only Markdown versions of PFCanon files** as canonical sources. Never open, fetch, inspect, cite as authority, or use a Google Doc, DOC, or DOCX version of any PFCanon file. There is no fallback: if the authoritative Markdown source is not available, record a source blocker.
- You may read the RCA as evidence, but must not follow or rely on any Google Docs PF10 link embedded in it. Resolve the current PF10 Markdown source separately.
- Store every off-repository planning artifact in `Glow / Ephemeral Planning Files` as efficient, machine-readable Markdown. Upload and read it back before citing it.
- Handoffs must use exact Drive links and explicit filename/version information, never ChatGPT Library IDs or conversation reconstruction.

### 4. Direct handoffs

- Every non-terminal prompt has exactly one fenced plain-text `NEXT_PROMPT_HANDOFF` block that is an actual copy-paste-ready invocation, not a field list or template.
- It must contain the exact selected receiving prompt name, version, and direct Notion URL; the receiving role/session; change/work identifiers; direct Drive artifact links; current state; decisions; constraints; unresolved items; next action; and expected output.
- Terminal prompts state terminal completion and must not emit a continuation handoff.
- Every route must resolve to a selected in-set prompt and be valid for its current status/authority.

### 5. Specialized PR development and action economy

- Re-evaluate and correct the skills used by PR-development sessions. `glow-hde-pr-development` is the primary skill for PR-30 implementation and interrupted-PR recovery. `glow-hde-devops` is support-only and must not control PR workflow policy.
- Update and validate the specialized PR-development skill as part of this successor. Preserve its established scope, but repair recovery, rescope, review, CI, and escalation behavior.
- Before starting fresh implementation after interruption, the PR session must recover the matching existing workspace/worktree, branch, open PR, and Drive artifacts when they exist. It must not invent a session-inspection dependency or force rework merely because a former conversation ended.
- Local testing occurs before any meaningful commit or push. Use coherent, locally tested checkpoints: do not make constant commits/pushes, and do not make none. An early draft PR is allowed only after a locally tested coherent point.
- Remote actions cost money. Open review findings take priority over CI. Do not wait for, retrigger, or consume a stale CI run while material review issues remain. Fix review findings locally, test them, create one coherent push, then obtain review/current-head CI. Cancel stale CI only when supported and authorized.
- A PR-development session works through review correction and current-head CI to genuine merge readiness, but does not merge without independent authority.

### 6. Prohibited regressions

- Do not introduce model/strength assessment, strength analyzer execution/routing, model or reasoning-level recommendations, eligibility/suitability/account checks, or workflow gates based on model or reasoning level.
- Do not use the ChatGPT Library for runtime artifacts.
- Do not alter the immutable Flowmaster Primary core or R1 oracle. If the generic `change-flow` specialization needs a GCFPE correction, implement it as a versioned GCFPE-specific overlay/contract and validate that the protected core remains byte-identical.

## Required execution sequence

### Phase 0 — freeze, source register, and impact inventory

1. Read the release register and selected catalog. Pin the actual selected predecessor release, its members, their versions, and the prompt/skill/hub/procedure controls that select or constrain them.
2. Create a Markdown source register in `Glow / Ephemeral Planning Files`. It must identify each authoritative source by name, version, direct URL, content role, source class, and observed status. Include an explicit PFCanon Markdown-only compliance column.
3. Build an impact matrix covering at least RS-10, RS-20, RS-30, the new continuation prompt, the new manual abort prompt, PR-20, PR-30, IA-10/20/30/40, QA-50/60/70/80, ESC-30/40, the PE metaprompt, management prompt, all plan/guide/spec-writing prompts found in the selected catalog, selection hubs, direct-handoff procedure, Alpha notes/log, `glow-hde-pr-development`, `glow-hde-devops`, change-flow GCFPE overlay/contract, and validators/fixtures.
4. Preserve the existing selected release as active during all candidate work.

### Phase 1 — define the effective successor contract before editing

1. Allocate a single successor release identity and exact member/version scheme only after the preflight inventory. Do not create competing sibling releases.
2. Write a successor graph contract covering normal PR flow, bounded rescope, rejected rescope, approved rescope continuation, manual abort/escalation, and terminal closure.
3. Explicitly remove the old RS-20 restart route from active status/routing. Keep historical records intact and labeled historical.
4. Define all state transitions and authority boundaries. In particular, prove that only the Product Owner manually invokes the abort prompt and that the final selected RS-20 is not invoked by this maintenance session.

### Phase 2 — repair prompts and handoffs

1. Create the selected successor copies of every impacted prompt; preserve substantive existing behavior outside this repair.
2. Add the dedicated approved-rescope continuation prompt and the Product-Owner-only abort-and-escalate prompt.
3. Repair PR-30 so it creates a bounded formal rescope request when appropriate, preserves the recoverable context, and returns a real IA handoff rather than attempting plan reauthoring or abort.
4. Repair RS/IA prompt behavior so an IA approval creates a standalone PF10 addendum and the next handoff reaches the continuation prompt, not an IA-30/IA-40 restart.
5. Update plan-creation prompts to cross-reference the authoritative PF10 Markdown source and active addenda.
6. Replace every affected generic handoff template/field list with one actual, populated `NEXT_PROMPT_HANDOFF` block per non-terminal execution outcome.
7. Ensure every approved rescope, escalation, remediation, or material plan change produces the required PF10 addendum only after approval; the handoff must carry its exact Drive link and the Product Owner manual-drain constraint.

### Phase 3 — repair skills, contracts, procedures, and hubs

1. Update `glow-hde-pr-development` through the skill-maintenance workflow. Its behavior cases and validation must cover workspace recovery, smart commit/push behavior, review-before-CI priority, formal rescope request, approved rescope continuation, and Product-Owner-only abort boundary.
2. Make `glow-hde-devops` support-only in the PR workflow. Do not use it as a primary PR-development controller.
3. Repair the GCFPE-specific `change-flow` overlay/contract and validation fixtures so its active contract no longer requires a restart/reauthoring path. Do not modify the protected generic core.
4. Update management controls, selection hubs, flow/index documents, direct-handoff procedure, and Alpha notes/log to select the successor graph and to mark the predecessor logic historical only after promotion.
5. Update the PE metaprompt so it cannot regenerate the retired restart, reauthoring, Library-ID, non-Markdown PFCanon, or prohibited assessment patterns.

### Phase 4 — deterministic validation

Create and run a successor validation suite. It must include machine-checkable or auditable checks for all of the following:

- selected-catalog completeness and exact successor membership count;
- one valid populated handoff per non-terminal prompt and no handoff on terminal prompts;
- all named Notion destinations resolve to selected in-set prompts with correct versions;
- no active route uses RS-20 as a restart/whole-plan-reauthoring mechanism;
- PR → IA → PF10 addendum → same-PR continuation graph closure;
- abort path is manual-only and unreachable from agent routes;
- semantic PF10 addendum coverage across every qualifying approval prompt;
- plan-creation cross-reference to PF10;
- no in-flight plan/guide/spec rewrite instruction outside the addendum process;
- Markdown-only PFCanon source rule and absence of Google Docs/DOC/DOCX fallback;
- all runtime planning artifacts/handoffs use Drive Markdown links rather than Library IDs;
- PR skill selection and action-economy rules;
- protected Flowmaster Primary core/R1 identity remains unchanged;
- no prohibited model/strength/Analyzer/reasoning-assessment language or routing in active sources; and
- old selected release remains active until all post-repair validation passes.

Test at least these scenarios end-to-end on the candidate graph:

1. PR discovery leads to a bounded request, IA rejection, and safe return without plan reauthoring.
2. PR discovery leads to IA approval, one PF10 addendum, Product Owner manual-drain boundary, then same-PR continuation.
3. A qualifying escalation/remediation/whole-plan discovery yields an approved PF10 addendum without live rewriting the base plan.
4. Repeated PR failure can surface evidence, but only Product Owner manual abort can initiate abort/escalation.
5. An interrupted PR session recovers existing workspace/branch/PR/artifacts without a false endpoint claim or reconstruction requirement.
6. Review findings are addressed locally before a new CI-triggering push.

### Phase 5 — promotion and archival

1. Produce a full validation and promotion report in `Glow / Ephemeral Planning Files`; upload and read it back.
2. If any acceptance check fails, do not select/promote the candidate and do not archive the predecessor. Return the failure report, exact blockers, and a safe repair handoff if one is valid. Do **not** return an Alpha-resumption RS-20 block.
3. If every acceptance check passes, update the release register, catalog, affected hubs/procedures, and active contracts to select the exact successor.
4. Read back all activated pages/artifacts and rerun the independent validation against the selected successor.
5. Archive all superseded GCFPE versions intact only after the successful post-promotion audit. Archive means retain them with accurate historical/superseded status; never delete or overwrite them.

## Promotion acceptance criteria

You may promote only when every item below is true:

- the selected successor has a defined and validated PR → IA → PF10 addendum → same-PR continuation loop;
- RS-20 restart/whole-plan reauthoring is absent from active routing;
- the continuation prompt and the manual-only abort prompt exist, are selected, and have exact working handoffs;
- all qualifying approval outcomes emit standalone Drive Markdown PF10 addenda with the required manual-drain status and ownership;
- all plan-creation prompts cross-reference the current PF10 Markdown source/addenda;
- no active prompt rewrites approved plans/guides/specifications in flight;
- PFCanon Markdown-only rule passes with no GDoc/DOC/DOCX source fallback;
- the specialized PR-development skill is validated as primary and DevOps is support-only;
- every required non-terminal handoff is exact and pasteable;
- current selected routes, versions, Notion references, and Drive links resolve correctly;
- no prohibited assessment/analyzer logic is active;
- immutable primary-core/R1 checks pass;
- predecessor remains preserved until promotion, then archived intact; and
- Alpha remains stopped pending Nathan’s manual use of the final handoff.

## Required artifacts

Create, upload, read back, and cite direct Drive links for at least:

1. source register and impact matrix;
2. effective successor graph/contract;
3. validation matrix and execution results;
4. PF10 addendum schema/example fixture (clearly non-canonical and not drained);
5. promotion and archival report; and
6. any candidate-specific handoff/skill/contract verification evidence.

Use concise, machine-readable Markdown with front matter, stable headings, exact IDs/versions, source links, decisions, validation status, and unresolved-items fields.

## Required final response

Return a concise implementation report first, containing:

- predecessor and promoted successor release IDs/versions and exact member count;
- created/updated prompt names, versions, and direct Notion links;
- selected primary/support skill decisions and validation results;
- exact direct Drive links to required artifacts;
- promotion and archival results; and
- the final statement `READY_FOR_MANUAL_ALPHA_RESUMPTION` only if promotion succeeded.

Then, **only after successful promotion**, end your response with exactly one fenced plain-text block headed `NEXT_PROMPT_HANDOFF`. This final block is for Nathan to paste manually into the continuing IA session. It is the sole Alpha-resumption trigger. Do not invoke it yourself.

Populate every value from the promoted sources. Placeholders, guessed IDs/versions, bare Library IDs, incomplete context, and a field-list instead of an invocation are invalid. The block must direct the receiver to run the exact newly selected RS-20 by its exact name, version, and direct Notion URL. It must identify the continuing IA session/role, HDE-EPIC040 and PR02/PR #404, the original rescope request and base plan, the exact current PF10 **Markdown** source and applicable addenda, the promotion report, status, decisions, constraints, unresolved items, the next IA action, and expected output.

Its opening should be operationally equivalent to:

```text
Run the Notion prompt **<exact selected RS-20 name> — <exact version>**.
Notion prompt: <exact direct Notion URL>
```

It must also state that the Alpha was previously stopped, this handoff is being manually invoked by Nathan after GCFPE promotion, and the receiver must follow the newly selected PF10-addendum rescope contract rather than any retired restart/reauthoring route.

If promotion does not succeed, do not provide this block. State `NOT_READY_FOR_MANUAL_ALPHA_RESUMPTION`, retain the predecessor selection, and list exact blockers and evidence.
