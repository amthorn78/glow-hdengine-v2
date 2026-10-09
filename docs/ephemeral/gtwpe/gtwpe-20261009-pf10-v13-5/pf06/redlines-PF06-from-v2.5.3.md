# T-PF06 — Exact redlines from PF06 v2.5.3

Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff
Run: `gtwpe-20261009-pf10-v13-5/T-PF06/preparation-1`. Originating preparer: `/root`, this user-invoked T-PF06 document session. No separate conversation identifier is exposed; no replacement author/session is invented.
Original: `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; SHA-256 `ee51f4cc9e78709f7fbf5868c2891ad3a109c0ed9d87b367250738dc3d55d7e0`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md` at `f057d124176143b3e02ba7ad599880fd7e9991b1`; task `T-PF06`.
Preparation outcome: `READY`. Save completeness is recorded only in the separate proof log after complete readback.
Incoming scope: A01, A08, A14, A29–A30, A33–A34, A38; S01, S13. Sources in header-provenance order: `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` (v13.5), `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` (approved v1.1). PF03 and format-owner sections are support only.
Apply reserves document-control metadata: native Version v2.5.3; Effective date 2026-08-27; Status Canon; existing Last Update Gate is the old redlines identity. The target has no change-history entry requirement for this revision. Apply derives v2.5.4, actual application date and `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md`. Title and invocation tag are preserved.
Every operation consumes its exact old block once within the unchanged original heading path. UTF-8 byte spans and original line numbers are supplemental verification only. Fenced payloads include their final LF; no label or closing fence is part of a payload. No whole-document rewrite, fuzzy match, dependent locator or repeated-replacement operation occurs.

## Redline RL-001

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.1 Purpose and scope**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [315, 1123); starting original line: 17.

OLD TEXT:

``````text
This guide defines the common change-delivery process for a human \+ pair-programming \+ CodEx workflow across two governed lanes: the Epic lane for product-development work originating in or formally mapped to PF09, and the CRD lane for observed features, defects, operational needs, governance needs, and system changes originating outside PF09 and accountable to PF30. It supplies paste-ready headers, checklists, and prompts. It requires an Audit and a Sandbox Build/Test for each epic or CRD. The normal route for code-bearing epic or CRD work is PR-based, while an explicit current Product Owner instruction may authorize a bounded direct-to-`main` route. Close requires the applicable exact-source evidence, close-pack material, and authorized decisions; a PASS acceptance-token list is not required.
``````

REPLACEMENT TEXT:

``````text
This guide defines the common change-delivery process for a human \+ pair-programming workflow with an executing agent across two governed lanes: the Epic lane for product-development work originating in or formally mapped to PF09, and the CRD lane for observed features, defects, operational needs, governance needs, and system changes originating outside PF09 and accountable to PF30. It supplies paste-ready headers, checklists, and prompts. It requires an Audit and a Sandbox Build/Test for each epic or CRD. The normal route for code-bearing epic or CRD work is PR-based, while an explicit current Product Owner instruction may authorize a bounded direct-to-`main` route. Close requires the applicable exact-source evidence, close-pack material, and authorized decisions; a PASS acceptance-token list is not required.
``````

## Redline RL-002

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.1A Governing lanes, common lifecycle, and authority routing**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [2287, 2313); starting original line: 34.

OLD TEXT:

``````text
3. Lead Developer plan.  
``````

REPLACEMENT TEXT:

``````text
3. Lead Developer Specification.  
``````

## Redline RL-003

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.1A Governing lanes, common lifecycle, and authority routing**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [3915, 4155); starting original line: 60.

OLD TEXT:

``````text
PF06 coordinates those authorities but does not replace them. Historical records retain the document names and identities that applied when they were created and are not rewritten solely to adopt the current PF06 title or lane terminology.
``````

REPLACEMENT TEXT:

``````text
PF06 coordinates those authorities but does not replace them. Historical records retain the document names and identities that applied when they were created and are not rewritten solely to adopt the current PF06 title or lane terminology.

Specification format authority. The permanent governed record is a Specification. CRD Specifications use the current CRD record contract and template in HDE CRD Records; Epic Specifications use the current Epic Record Template (Normative) in Plan Templates. A delta Specification uses the applicable governing base format. Kickoff packages are transient, and Implementation Plans are working implementation direction whose producing prompt may shape them. Prompts resolve the owning canon at runtime instead of hardcoding the PF27/PF30 document titles or restating their templates. Each produced Specification cites the exact owning canon title and section used. Retired glow-specification, glow-kickoff and glow-kind/version tokens, the retired thirteen-section GCFPE shape and a permanent-record `schema_version` are not Specification-format authority. If the owning format cannot be resolved, report `SOURCE_RESOLUTION_ERROR` with the failed predicate and recovery owner; do not guess a format. Historical approvals and preserved source representations retain their original format and provenance.

Agent-authored HDE Build Notes addenda are self-contained canonical records at creation, including QA, Ops and closure classes. Resolve the current continuous addendum number and format before authoring. Each addendum has one H2 with the next number and a descriptive title, unique metadata when needed, and only H3 or lower subordinate headings. It records supported decisions, status, durable requirements, exceptions, scope, nonclaims, evidence, dependencies and unresolved obligations in declarative language; it does not carry role-addressed publication, routing or record-maintenance instructions. Technical Writing Best Practices owns the writing guidance.
``````

## Redline RL-004

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [4219, 4521); starting original line: 66.

OLD TEXT:

``````text
The normal code-bearing epic-slice route is PR-first via CodEx. The Product Owner MAY instead authorize direct mutation of `main` through an explicit current instruction covering the exact change. An agent MUST NOT infer direct-main authority from PF06, repository access, or an earlier authorization.
``````

REPLACEMENT TEXT:

``````text
The normal code-bearing epic-slice route is PR-first via the executing agent. The Product Owner MAY instead authorize direct mutation of `main` through an explicit current instruction covering the exact change. An agent MUST NOT infer direct-main authority from PF06, repository access, or an earlier authorization.
``````

## Redline RL-005

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [4522, 4856); starting original line: 68.

OLD TEXT:

``````text
For the PR route, CodEx MUST open a PR for the exact slice and include code changes, Doc-Delta updates, and each evidence-index, mirror, hash, or path-proof companion required by changed governed artifacts and current canon. For the direct-main route, the exact operator authorization and the post-write exact-source evidence govern.
``````

REPLACEMENT TEXT:

``````text
For the PR route, the executing agent MUST open a PR for the exact slice and include code changes, Doc-Delta updates, and each evidence-index, mirror, hash, or path-proof companion required by changed governed artifacts and current canon. For the direct-main route, the exact operator authorization and the post-write exact-source evidence govern.
``````

## Redline RL-006

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [12768, 12952); starting original line: 115.

OLD TEXT:

``````text
* PF-canon drainage applies stable documentation updates to the permanent PF homes. PF10 can stage live truth before drainage, but the drain itself is a separate documentation action.
``````

REPLACEMENT TEXT:

``````text
* PF-canon drainage applies stable documentation updates to the permanent PF homes. PF10 can stage live truth before drainage, but the drain itself is a separate documentation action.

The operational development board is the Notion HDE development board: https://app.notion.com/p/3d54590a05eb819dacccfcfbfee8666b?pvs=204. Board Cards carry current operational Epic/CRD state; Board History is the related imported event ledger. Imported JSON is a migration snapshot. Historical PF16/PF20/PF30 pointer pages provide stable role-based navigation and provenance; resolve current PF source bytes by document identity and title in the repository, rather than freezing a versioned filename from a pointer. An event without a source card does not establish a role. Board lanes, card DONE and historical pointers do not decide canon authority, Specification approval, QA, acceptance or closure.
``````

## Redline RL-007

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [13314, 13543); starting original line: 119.

OLD TEXT:

``````text
Every task-like item in an Epic Plan, Implementation Plan, QA Plan, remediation plan, QA-readiness review, retrospective, closure review, Scrum handoff, PO planning handoff, or board-prep artifact MUST resolve to exactly one of:
``````

REPLACEMENT TEXT:

``````text
Every task-like item in an Epic Specification, Implementation Plan, QA Plan, remediation plan, QA-readiness review, retrospective, closure review, Scrum handoff, PO planning handoff, or board-prep artifact MUST resolve to exactly one of:
``````

## Redline RL-008

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [15426, 16122); starting original line: 137.

OLD TEXT:

``````text
For every PF09 row that an approved Epic Plan or Implementation Plan assigns to completed PR, OPS, or combined epic work for closure, the reviewer MUST identify the exact phased PF09 document, row ID, title, physical status, approved plan scope, mapped PR and OPS lineage, and current evidence before creating remedial work. The approved plan together with applicable active PF10 defines the bounded row scope. A broader PF09 description, later-phase work, historical cleanup, future expansion, unrelated stale artifacts, physical PF09 drainage, permanent-canon drainage, QA PASS, acceptance, deployment, closeout, or an explicitly excluded requirement MUST NOT retroactively enlarge that scope.
``````

REPLACEMENT TEXT:

``````text
For every PF09 row that an approved Epic Specification or Implementation Plan assigns to completed PR, OPS, or combined epic work for closure, the reviewer MUST identify the exact phased PF09 document, row ID, title, physical status, approved plan scope, mapped PR and OPS lineage, and current evidence before creating remedial work. The approved plan together with applicable active PF10 defines the bounded row scope. A broader PF09 description, later-phase work, historical cleanup, future expansion, unrelated stale artifacts, physical PF09 drainage, permanent-canon drainage, QA PASS, acceptance, deployment, closeout, or an explicitly excluded requirement MUST NOT retroactively enlarge that scope.
``````

## Redline RL-009

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [23194, 23288); starting original line: 175.

OLD TEXT:

``````text
Implementation Agents and other non-CodEx process roles do not run git and do not create PRs.
``````

REPLACEMENT TEXT:

``````text
Implementation Agents and process roles other than executing agent do not run git and do not create PRs.
``````

## Redline RL-010

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [32048, 32847); starting original line: 280.

OLD TEXT:

``````text
Build Notes reference posture (living addenda).

When referencing Build Notes in reviews, plans, or Doc Delta notes:

* Do not reference Build Notes by version strings.  
* Prefer referencing by addendum number \+ addendum title.  
* Do not treat Build Notes section numbers as durable anchors for external enforcement.

When PF10 or a closeout artifact records more than one QA pass, QA review, final review, or pass-like addendum for the same epic, each entry MUST be distinguishable by addendum number and addendum title or by another stable source-order label. Reviews and closeout summaries MUST NOT rely on repeated labels such as “QA Pass 2” alone when that label appears more than once for the same epic. If duplicate labels exist, cite source order and state the chronology explicitly.
``````

REPLACEMENT TEXT:

``````text
Build Notes reference posture (living addenda).

In current PF prose, reviews, Specifications, plans and Doc Delta notes, reference HDE Build Notes by title only. Do not include a Build Notes version, section number, addendum number or addendum title as a citation or enforcement locator. Search the current document by subject and read the governing material; an earlier number or a stale snippet does not resolve current authority.

When more than one QA pass, review or pass-like record concerns the same Epic, distinguish the chronology by stable source order and exact evidence or decision identities and times. Repeated labels such as “QA Pass 2” alone are insufficient. This preserves distinct source events without an internal Build Notes locator in current PF prose. Historical source snapshots and provenance retain their original identifiers unchanged.
``````

## Redline RL-011

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [35551, 35655); starting original line: 335.

OLD TEXT:

``````text
Ops tasks (PO-authorized execution; PO-executed or explicitly delegated; IA-guided; not CodEx PR work).
``````

REPLACEMENT TEXT:

``````text
Ops tasks (PO-authorized execution; PO-executed or explicitly delegated; IA-guided; not PR work assigned to the executing agent).
``````

## Redline RL-012

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [36126, 36728); starting original line: 339.

OLD TEXT:

``````text
Execution authority. Ops tasks MUST be authorized by the Product Owner. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent. The delegated agent MAY perform the authorized operation on the PO's behalf and MUST follow the same scope, safety, evidence, redaction, and completion-claim controls that bind a human operator. “PO-only” identifies the owner of authorization, accountability, and acceptance; it does not require the PO to be the physical keystroke actor. A delegated agent is an authorized executor, not an independent approver.
``````

REPLACEMENT TEXT:

``````text
Execution authority. Ops tasks MUST be authorized by the Product Owner. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent. The delegated agent MAY perform the authorized operation on the PO's behalf and MUST follow the same scope, safety, evidence, redaction, and completion-claim controls that bind a human operator. “PO-only” identifies the owner of authorization, accountability, and acceptance; it does not require the PO to be the physical keystroke actor. A delegated agent is an authorized executor, not an independent approver.

Live vendor execution interface. For an identified HD Engine vendor task directed by the Product Owner, the directed automated session agent executes the vendor call and produces its evidence. It follows the task’s exact commands, scope, rails, request limit, stop checks, synthetic-input rules, secret scan and quarantine, redaction and evidence contract. It is not an independent approver. The same interface applies to QA, Ops, controlled vendor-backed no-user smoke and implementation validation; the evidence retains its actual class. There is no standing vendor-call authority without the task direction.

Vendor configuration comes from the execution environment: `HD_API_KEY` and `GEO_API_KEY` are the two API keys; `HD_API_BASE_URL` is base-URL configuration. `HDAPI_BASE_URL` is a deprecated compatibility alias used only when `HD_API_BASE_URL` is absent; differing configured values fail closed. Use the environment configuration without asking the Product Owner to type, paste or re-enter values, and do not discard an environment-held base URL merely because of rails posture. Record only `SET` or `UNSET` presence. Keep values out of process arguments, conversation, logs and stored evidence; scan captured output before admitting it to evidence. Missing required configuration prevents the call and makes a begun step `TOOLING_BLOCKED`; manual entry is not a substitute. Environment setup remains Product Owner-owned.
``````

## Redline RL-013

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.2 Policy and principles**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [41115, 41367); starting original line: 368.

OLD TEXT:

``````text
Not a PR. Ops tasks are not CodEx PR work. They MUST NOT be represented as “implementable PR work.” Any implementation/remediation document MUST separate Ops tasks from PR work and label Ops tasks explicitly as: PO-authorized execution, IA-guided.
``````

REPLACEMENT TEXT:

``````text
Not a PR. Ops tasks are not PR work assigned to the executing agent. They MUST NOT be represented as “implementable PR work.” Any implementation/remediation document MUST separate Ops tasks from PR work and label Ops tasks explicitly as: PO-authorized execution, IA-guided.
``````

## Redline RL-014

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.3 Participants and responsibilities**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [53797, 54180); starting original line: 491.

OLD TEXT:

``````text
* Implementation Agent (ChatGPT). Runs each approved epic or CRD end to end, prepares the applicable planning and execution drafts, sets up CodEx asks (what, not how), verifies proofs and artifacts, ensures Doc-Delta and every applicable governed evidence companion land in the authorized mutation set, and escalates blockers to the Lead Developer. Does not run git or create PRs.  
``````

REPLACEMENT TEXT:

``````text
* Implementation Agent (IA). Runs each approved epic or CRD end to end, prepares the applicable planning and execution drafts, sets up requests for the executing agent (what, not how), verifies proofs and artifacts, ensures Doc-Delta and every applicable governed evidence companion land in the authorized mutation set, and escalates blockers to the Lead Developer. Does not run git or create PRs.  
``````

## Redline RL-015

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.3 Participants and responsibilities**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [54180, 54498); starting original line: 492.

OLD TEXT:

``````text
* Lead Developer (AI). Defines intent and bounded scope, performs the required current-state and existing-work analysis, produces or governs the applicable Epic Plan or CRD Plan, approves the Implementation Plan once, performs the gate review when a PR route is used, and otherwise steps out during CodEx execution.  
``````

REPLACEMENT TEXT:

``````text
* Lead Developer (AI). Defines intent and bounded scope, performs the required current-state and existing-work analysis, produces or governs the applicable Epic Specification or CRD Specification, approves the Implementation Plan once, performs the gate review when a PR route is used, and otherwise steps out during execution by the executing agent.  
``````

## Redline RL-016

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.3 Participants and responsibilities**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [54498, 55073); starting original line: 493.

OLD TEXT:

``````text
* CodEx. Executes in a sandbox, runs Audit and Build/Test, and follows the mutation route expressly authorized for the change. For a PR route, CodEx opens or amends the PR and supplies the applicable close material. For direct-main mutation, CodEx requires an explicit current operator instruction covering the exact change and records the post-write SHA, diff, and applicable push-CI state. CodEx can read PF docs. Even so, the IA SHOULD paste execution-critical material verbatim during build sessions to keep a stable, unambiguous in-session reference and reduce drift.  
``````

REPLACEMENT TEXT:

``````text
* The executing agent. Executes in a sandbox, runs Audit and Build/Test, and follows the mutation route expressly authorized for the change. For a PR route, the executing agent opens or amends the PR and supplies the applicable close material. For direct-main mutation, the executing agent requires an explicit current operator instruction covering the exact change and records the post-write SHA, diff, and applicable push-CI state. The issued Implementation Guide MUST establish the actual executing agent’s ability to read PF documents and required inputs. Even so, the IA SHOULD paste execution-critical material verbatim during build sessions to keep a stable, unambiguous in-session reference and reduce drift.  
``````

## Redline RL-017

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.3 Participants and responsibilities**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [55644, 55746); starting original line: 497.

OLD TEXT:

``````text
* Communication rule. AIs do not contact one another directly. The Product Owner routes all messages.
``````

REPLACEMENT TEXT:

``````text
* Communication rule. AIs do not contact one another directly. The Product Owner routes all messages.

These process functions do not require a particular AI provider, product, model or reasoning-effort setting. Preserve role separation, session continuity, approvals, mutation routes and readback duties. Literal product-bearing vocabulary and field names, including `CA vetted`, `Codex Audit observed evidence`, `Observed Evidence (Codex Audit)`, `Observed repo reality (Codex Audit)`, `Codex prompt`, `CodEx Prompt`, `codex`, `codex_inputs` and `codex_can_see_pf_docs`, retain their exact spellings and denote the corresponding audit, prompt or execution function. A label is not a provider mandate. Capability descriptions of a particular product remain qualified descriptions; each Implementation Guide establishes the capabilities of its actual executing agent.
``````

## Redline RL-018

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [55884, 55998); starting original line: 502.

OLD TEXT:

``````text
* IA sends CodEx an audit request with explicit report formats and any verbatim components or schemas required.  
``````

REPLACEMENT TEXT:

``````text
* IA sends the executing agent an audit request with explicit report formats and any verbatim components or schemas required.  
``````

## Redline RL-019

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [55998, 56135); starting original line: 503.

OLD TEXT:

``````text
* CodEx resolves the current ref and returns an audit report covering observed repository facts, gaps, risks, proposals, and unknowns.  
``````

REPLACEMENT TEXT:

``````text
* The executing agent resolves the current ref and returns an audit report covering observed repository facts, gaps, risks, proposals, and unknowns.  
``````

## Redline RL-020

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [56265, 56467); starting original line: 505.

OLD TEXT:

``````text
* IA sends CodEx build instructions plus verbatim execution-critical material. CodEx may adapt within scope, MUST report all changes, and returns a detailed change report plus artifacts and evidence.  
``````

REPLACEMENT TEXT:

``````text
* IA sends the executing agent build instructions plus verbatim execution-critical material. The executing agent may adapt within scope, MUST report all changes, and returns a detailed change report plus artifacts and evidence.  
``````

## Redline RL-021

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [56536, 56668); starting original line: 507.

OLD TEXT:

``````text
* For a PR route, CodEx opens or amends the exact-slice PR and includes code, Doc-Delta, and every applicable evidence companion.  
``````

REPLACEMENT TEXT:

``````text
* For a PR route, the executing agent opens or amends the exact-slice PR and includes code, Doc-Delta, and every applicable evidence companion.  
``````

## Redline RL-022

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [56668, 56873); starting original line: 508.

OLD TEXT:

``````text
* For a direct-main route, CodEx acts only under an explicit current operator instruction covering the exact mutation and records the exact post-write SHA, diff, and applicable push-triggered CI result.  
``````

REPLACEMENT TEXT:

``````text
* For a direct-main route, the executing agent acts only under an explicit current operator instruction covering the exact mutation and records the exact post-write SHA, diff, and applicable push-triggered CI result.  
``````

## Redline RL-023

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [57767, 57971); starting original line: 510.

OLD TEXT:

``````text
* If a required execution-time capability or authorization is unavailable, the workflow is blocked. CodEx MUST NOT claim an action occurred, silently substitute another actor, or omit required content.  
``````

REPLACEMENT TEXT:

``````text
* If a required execution-time capability or authorization is unavailable, the workflow is blocked. The executing agent MUST NOT claim an action occurred, silently substitute another actor, or omit required content.  
``````

## Redline RL-024

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.4 4 Execution posture and flow (route-aware)**
### **0.4.1 Live QA discovery and RCA (execution requirements)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [59756, 59995); starting original line: 522.

OLD TEXT:

``````text
These requirements are execution and Close Gate deliverables. They MUST NOT be treated as prerequisites for Epic Plan or CRD Plan approval and MUST NOT force a detailed Live QA runbook into Epic Plan, CRD Plan, or Implementation planning.
``````

REPLACEMENT TEXT:

``````text
These requirements are execution and Close Gate deliverables. They MUST NOT be treated as prerequisites for Epic Specification or CRD Specification approval and MUST NOT force a detailed Live QA runbook into Epic Specification, CRD Specification, or Implementation planning.
``````

## Redline RL-025

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [85087, 85278); starting original line: 811.

OLD TEXT:

``````text
Route the applicable Epic Plan or CRD Plan through the Lead Developer process. Keep process artifacts (Epic Plan/CRD Plan/Doc-Delta) titles-only and route to single homes for bytes/evidence.
``````

REPLACEMENT TEXT:

``````text
Route the applicable Epic Specification or CRD Specification through the Lead Developer process. Keep process artifacts (Epic Specification/CRD Specification/Doc-Delta) titles-only and route to single homes for bytes/evidence.
``````

## Redline RL-026

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [88226, 88341); starting original line: 846.

OLD TEXT:

``````text
An Epic Plan, CRD Plan, or QA Plan MUST NOT reference a file path as required unless one of the following is true:
``````

REPLACEMENT TEXT:

``````text
An Epic Specification, CRD Specification, or QA Plan MUST NOT reference a file path as required unless one of the following is true:
``````

## Redline RL-027

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [89177, 89381); starting original line: 857.

OLD TEXT:

``````text
* Codex Audit observed evidence: identify the supplied Codex Audit and embed the observed repo-reality fact as a short quote or precise paraphrase. This label may prove planning-time repo reality only.  
``````

REPLACEMENT TEXT:

``````text
* Codex Audit observed evidence: identify the supplied read-only repository audit and embed the observed repo-reality fact as a short quote or precise paraphrase. This label may prove planning-time repo reality only.  
``````

## Redline RL-028

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [90475, 90571); starting original line: 866.

OLD TEXT:

``````text
* CodEx must still verify repo reality during execution before editing or relying on the locus.
``````

REPLACEMENT TEXT:

``````text
* The executing agent must still verify repo reality during execution before editing or relying on the locus.
``````

## Redline RL-029

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [90572, 91051); starting original line: 868.

OLD TEXT:

``````text
Audit provenance in planning artifacts. Audit provenance is allowed in Epic Plans, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives when it is used as planning context, risk context, discovery context, source-trace context, rationale for inspection, rationale for a Tracked Issue, rationale for an ADR stub, rationale for a planned workstream, rationale for a QA proof obligation, rationale for repo validation, or rationale for PF-canon drainage.
``````

REPLACEMENT TEXT:

``````text
Audit provenance in planning artifacts. Audit provenance is allowed in Epic Specifications, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives when it is used as planning context, risk context, discovery context, source-trace context, rationale for inspection, rationale for a Tracked Issue, rationale for an ADR stub, rationale for a planned workstream, rationale for a QA proof obligation, rationale for repo validation, or rationale for PF-canon drainage.
``````

## Redline RL-030

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [91052, 91533); starting original line: 870.

OLD TEXT:

``````text
Audit provenance MUST NOT be treated as PR instruction, OPS instruction, step-by-step execution procedure, CodEx command source, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth without repo validation, source of invented file/path/module/test existence, source of required deliverables unless adopted by the plan or PF source, source of privileged live action, or source of secrets or external state.
``````

REPLACEMENT TEXT:

``````text
Audit provenance MUST NOT be treated as PR instruction, OPS instruction, step-by-step execution procedure, source of commands for the executing agent, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth without repo validation, source of invented file/path/module/test existence, source of required deliverables unless adopted by the plan or PF source, source of privileged live action, or source of secrets or external state.
``````

## Redline RL-031

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.5 Routing and evidence discipline**
### **0.5.1 Epic path normalization (close-pack \+ QA root)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [93177, 93243); starting original line: 888.

OLD TEXT:

``````text
* a supplied Codex Audit for the epic, task, or review artifact  
``````

REPLACEMENT TEXT:

``````text
* a supplied read-only repository audit for the epic, task, or review artifact  
``````

## Redline RL-032

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.1 Canon-first planning**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [104368, 104467); starting original line: 1027.

OLD TEXT:

``````text
Implementation Agents MUST treat PF-Canon as the primary source of facts for epic planning and QA.
``````

REPLACEMENT TEXT:

``````text
Implementation Agents MUST treat PF-Canon as the primary source of facts for epic planning and QA.

At each task start and each subject change, search the repository canon and the current change-ID’s in-flight documents for relevant terms, surfaces, environments and headings before planning, authoring, reviewing, deciding or asking the Product Owner. Read all governing sections found; search does not require loading all canon. Record the exact document titles and sections actually used. Ask the Product Owner only where the searched canon is silent or unresolved, naming the sections checked.

Current `main` Markdown under `docs/pfcanon/` is the sole PF source home. Each document retains its declared Canon, Build Notes or Reference class; mirrors, Notion pages, Drive files and historical Reality Audits do not gain canon authority. Change-process documents, including intake, kickoff, Specifications, working plans, audits, readiness material, guides, reviews, reports, remediation, handoffs, redlines and Product Owner decisions, use exact repository paths under `docs/ephemeral/`. Governed code, tests, configuration and evidence retain their owning homes and writers. Persistent prompt-ecosystem management uses `docs/prompt_ecosystem_management/`; live GCFPE prompt bodies retain their single Notion home. ChatGPT Library and Google Drive are neither current source nor destination, except an explicit file-specific Product Owner Drive instruction as a nonauthoritative exception. Historical files are not bulk-moved or rewritten. This does not decide an unresolved home for ongoing operating procedures or selection guidance.

The approved Specification governs change scope. Approved Implementation Plans provide working direction; required reviews and Product Owner decisions govern their own bounded actions. Apply the canon precedence rule in Plan Templates, “Canon precedence for template use”; storage, provenance and artifact presence do not confer approval or execution authority.
``````

## Redline RL-033

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.1 Canon-first planning**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [107982, 108112); starting original line: 1054.

OLD TEXT:

``````text
  * PF10-live posture: cite the current PF10 addendum by addendum number and title when PF10 explicitly supplies the live fact.  
``````

REPLACEMENT TEXT:

``````text
  * PF10-live posture: cite HDE Build Notes by title only when it supplies the governing live fact; locate and read that fact by subject search.  
``````

## Redline RL-034

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.4 PO Live QA vendor-first scope**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [118338, 118538); starting original line: 1162.

OLD TEXT:

``````text
Purpose: PO Live QA is a vendor-first activity. Its primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.
``````

REPLACEMENT TEXT:

``````text
Purpose: PO Live QA is a vendor-first activity. Its primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.

Product Owner-run sessions remain one execution form. When the Product Owner directs an identified vendor task, a directed agent executes its commands unchanged using environment-held configuration under §0.2. This preserves authorization, safety, evidence class and independent QA review; it does not require human keystrokes or manual vendor-value entry.
``````

## Redline RL-035

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.9 Plans are pointers; QA planning is post-implementation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [129935, 130133); starting original line: 1306.

OLD TEXT:

``````text
Core rule: Epic Plans and CRD Plans are pointers to canon and governed artifacts. They are not the place to restate or rebuild canon (token definitions, schemas, CLI semantics, env matrices, etc.).
``````

REPLACEMENT TEXT:

``````text
Core rule: Epic Specifications and CRD Specifications are pointers to canon and governed artifacts. They are not the place to restate or rebuild canon (token definitions, schemas, CLI semantics, env matrices, etc.).
``````

## Redline RL-036

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.9 Plans are pointers; QA planning is post-implementation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [130134, 130444); starting original line: 1308.

OLD TEXT:

``````text
Do not rebuild canon inside an Epic Plan or CRD Plan. Either plan may reference canonical documents by title only and point to canonical artifact paths. If review needs more definition than canon provides, the correction is a doc-delta or a governed artifact, not duplicated canonical content inside the plan.
``````

REPLACEMENT TEXT:

``````text
Do not rebuild canon inside an Epic Specification or CRD Specification. Either Specification may reference canonical documents by title only and point to canonical artifact paths. If review needs more definition than canon provides, the correction is a doc-delta or a governed artifact, not duplicated canonical content inside the Specification.
``````

## Redline RL-037

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.9 Plans are pointers; QA planning is post-implementation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [130445, 130692); starting original line: 1310.

OLD TEXT:

``````text
QA planning happens after implementation (and after D0 discovery). A step-by-step QA plan (Live QA step lists, per-step Deliverables blocks, copy/paste command blocks, harness invocation details, etc.) is not an Epic Plan or CRD Plan deliverable.
``````

REPLACEMENT TEXT:

``````text
QA planning happens after implementation (and after D0 discovery). A step-by-step QA plan (Live QA step lists, per-step Deliverables blocks, copy/paste command blocks, harness invocation details, etc.) is not an Epic Specification or CRD Specification deliverable.
``````

## Redline RL-038

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.9 Plans are pointers; QA planning is post-implementation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [130693, 130739); starting original line: 1312.

OLD TEXT:

``````text
An Epic Plan or CRD Plan SHOULD provide only:
``````

REPLACEMENT TEXT:

``````text
An Epic Specification or CRD Specification SHOULD provide only:
``````

## Redline RL-039

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **0\. Front Matter**
## **0.6 Discipline**
### **0.6.9 Plans are pointers; QA planning is post-implementation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [131053, 131166); starting original line: 1320.

OLD TEXT:

``````text
Approval posture: avoid planning stalls. Reviewers SHOULD NOT block Epic Plan or CRD Plan approval by demanding:
``````

REPLACEMENT TEXT:

``````text
Approval posture: avoid planning stalls. Reviewers SHOULD NOT block Epic Specification or CRD Specification approval by demanding:
``````

## Redline RL-040

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.0 CRD lane intake, plan, and PF30 registration**
### **1.0.2 Lead Developer analysis and CRD Plan**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [142968, 143019); starting original line: 1429.

OLD TEXT:

``````text
### **1.0.2 Lead Developer analysis and CRD Plan**
``````

REPLACEMENT TEXT:

``````text
### **1.0.2 Lead Developer analysis and CRD Specification**
``````

## Redline RL-041

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.0 CRD lane intake, plan, and PF30 registration**
### **1.0.2 Lead Developer analysis and CRD Plan**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [143499, 143527); starting original line: 1443.

OLD TEXT:

``````text
The result is the CRD Plan.
``````

REPLACEMENT TEXT:

``````text
The result is the CRD Specification, using the current CRD record contract and template in HDE CRD Records under §0.1A.
``````

## Redline RL-042

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.0 CRD lane intake, plan, and PF30 registration**
### **1.0.3 PF30 registration and approval**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [143574, 143902); starting original line: 1447.

OLD TEXT:

``````text
The CRD MUST receive a stable CRD ID and a concise initial record in PF30 before implementation begins. The CRD Plan MUST receive the approval required by current governance. If the required PF30 record cannot be established, implementation is blocked; do not substitute PF09 accountability or claim that registration occurred.
``````

REPLACEMENT TEXT:

``````text
The CRD MUST receive a stable CRD ID and a concise initial record in PF30 before implementation begins. The CRD Specification MUST receive the approval required by current governance. If the required PF30 record cannot be established, implementation is blocked; do not substitute PF09 accountability or claim that registration occurred.
``````

## Redline RL-043

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.0 CRD lane intake, plan, and PF30 registration**
### **1.0.5 Canon changes**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [144833, 145229); starting original line: 1457.

OLD TEXT:

``````text
A CRD that changes a canonical rule, contract, schema, process, interpretation, permanent policy, or governed-artifact meaning MUST have an accompanying approved ADR. The ADR MUST identify affected canon and drainage consequences. Material CRD activity and decisions enter HDE Build Notes and then drain to the appropriate permanent owner. A CRD Plan alone does not authorize canon supersession.
``````

REPLACEMENT TEXT:

``````text
A CRD that changes a canonical rule, contract, schema, process, interpretation, permanent policy, or governed-artifact meaning MUST have an accompanying approved ADR. The ADR MUST identify affected canon and drainage consequences. Material CRD activity and decisions enter HDE Build Notes and then drain to the appropriate permanent owner. A CRD Specification alone does not authorize canon supersession.
``````

## Redline RL-044

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [146739, 146935); starting original line: 1476.

OLD TEXT:

``````text
* Treat Reality Audits as optional historical context only; they are not a required Epic Plan, implementation, or QA input and do not replace current repository inspection or controlling canon.  
``````

REPLACEMENT TEXT:

``````text
* Treat Reality Audits as optional historical context only; they are not a required Epic Specification, implementation, or QA input and do not replace current repository inspection or controlling canon.  
``````

## Redline RL-045

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [147201, 147275); starting original line: 1479.

OLD TEXT:

``````text
* Draft the Epic Plan only after the current-state inventory is complete.
``````

REPLACEMENT TEXT:

``````text
* Draft the Epic Specification only after the current-state inventory is complete.
``````

## Redline RL-046

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [147276, 147445); starting original line: 1481.

OLD TEXT:

``````text
Epic Plan record: Draft the current **Epic Record Template (Normative)** in PF27-Canon-Plan-Templates. PF06 does not define a separate Epic Plan machine-header grammar.
``````

REPLACEMENT TEXT:

``````text
Epic Specification record: Draft the current **Epic Record Template (Normative)** in Plan Templates, resolved at runtime under §0.1A. PF06 does not define a separate Epic Specification machine-header grammar.
``````

## Redline RL-047

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [147446, 147751); starting original line: 1483.

OLD TEXT:

``````text
Approved epic scope: After the required review and approval, preserve the approved scope, stable governing and acceptance-criterion identities, and applicable evidence obligations in the Epic Plan and its approval record. A separate epic-internal CRD is not used. A complete token roster is not required.
``````

REPLACEMENT TEXT:

``````text
Approved epic scope: After the required review and approval, preserve the approved scope, stable governing and acceptance-criterion identities, and applicable evidence obligations in the Epic Specification and its approval record. A separate epic-internal CRD is not used. A complete token roster is not required.

Specification approval and implementation handoff remain distinct. On denial, the same Specification author revises against the exact review findings and returns to the same bound reviewer. On approval, the exact approved representation is the native input to the Product Owner-selected dedicated whole-change Implementation Agent session. That session performs the mandatory whole-change Implementation Audit before authoring the separate complete change-wide Implementation Plan. Independent Plan review, per-PR Proceed, authorized execution, independent QA, acceptance and closure remain separate duties. A Specification, audit, plan or saved proof does not substitute for any later required decision.

The whole-change audit is separate from the executing agent’s repository audit for a PR or implementation slice in §2.2. Retain that later audit, the Guide/IP sequence and all applicable execution and approval boundaries. No extra token, PF20/PF30 record, synthetic approval object or creation proof is added as a native handoff input.
``````

## Redline RL-048

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [148071, 148287); starting original line: 1489.

OLD TEXT:

``````text
CodEx execution: CodEx MUST run Audit \+ Sandbox Build/Test and verify that its working base remains current. If `main` advanced, CodEx MUST compare and reconcile the movement or prove it immaterial before mutation.
``````

REPLACEMENT TEXT:

``````text
Execution by the executing agent: The executing agent MUST run Audit \+ Sandbox Build/Test and verify that its working base remains current. If `main` advanced, the executing agent MUST compare and reconcile the movement or prove it immaterial before mutation.
``````

## Redline RL-049

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [148288, 148409); starting original line: 1491.

OLD TEXT:

``````text
For a PR route, CodEx opens or amends the exact-slice PR when the required authenticated capability exists and includes:
``````

REPLACEMENT TEXT:

``````text
For a PR route, the executing agent opens or amends the exact-slice PR when the required authenticated capability exists and includes:
``````

## Redline RL-050

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.1 Standard epic flow**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [148579, 148840); starting original line: 1498.

OLD TEXT:

``````text
For an authorized direct-main route, CodEx records the exact post-write SHA, diff, and applicable push-triggered CI result. It MUST describe pending or failed validation truthfully and MUST NOT claim QA, acceptance, or closure merely because the change landed.
``````

REPLACEMENT TEXT:

``````text
For an authorized direct-main route, the executing agent records the exact post-write SHA, diff, and applicable push-triggered CI result. It MUST describe pending or failed validation truthfully and MUST NOT claim QA, acceptance, or closure merely because the change landed.
``````

## Redline RL-051

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [149965, 150030); starting original line: 1514.

OLD TEXT:

``````text
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

REPLACEMENT TEXT:

``````text
### **1.1.3 “Prod via Codespaces” requirements (Epic Specification)**
``````

## Redline RL-052

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [151609, 151725); starting original line: 1535.

OLD TEXT:

``````text
Name prod surfaces by title. The Epic Plan MUST name (by title, routing to Glow Infrastructure as the single home):
``````

REPLACEMENT TEXT:

``````text
Name prod surfaces by title. The Epic Specification MUST name (by title, routing to Glow Infrastructure as the single home):
``````

## Redline RL-053

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [151852, 151914); starting original line: 1542.

OLD TEXT:

``````text
Clarify Codespaces role. The Epic Plan MUST state explicitly:
``````

REPLACEMENT TEXT:

``````text
Clarify Codespaces role. The Epic Specification MUST state explicitly:
``````

## Redline RL-054

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [152077, 152191); starting original line: 1547.

OLD TEXT:

``````text
Describe the prod handshake and artifact location (identity-only). The Epic Plan MUST describe (at a high level):
``````

REPLACEMENT TEXT:

``````text
Describe the prod handshake and artifact location (identity-only). The Epic Specification MUST describe (at a high level):
``````

## Redline RL-055

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [152952, 153128); starting original line: 1561.

OLD TEXT:

``````text
Epic Plan entries that refer to “prod via Codespaces” without these clarifications are incomplete and MUST be updated before the epic moves into implementation or Live QA.
``````

REPLACEMENT TEXT:

``````text
Epic Specification entries that refer to “prod via Codespaces” without these clarifications are incomplete and MUST be updated before the epic moves into implementation or Live QA.
``````

## Redline RL-056

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [153129, 153342); starting original line: 1563.

OLD TEXT:

``````text
Vendor-first Live QA using “prod via Codespaces”. For epics that intend to run vendor-first Live QA (per §0.6.4 and §1.1.6) using the “prod via Codespaces” pattern above, the Epic Plan MUST ALSO ensure:
``````

REPLACEMENT TEXT:

``````text
Vendor-first Live QA using “prod via Codespaces”. For epics that intend to run vendor-first Live QA (per §0.6.4 and §1.1.6) using the “prod via Codespaces” pattern above, the Epic Specification MUST ALSO ensure:
``````

## Redline RL-057

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [153343, 153595); starting original line: 1565.

OLD TEXT:

``````text
* The current Epic Plan acceptance criteria and evidence requirements explicitly declare this posture by title (for example: “Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under audit/qa/\\/\\”).  
``````

REPLACEMENT TEXT:

``````text
* The current Epic Specification acceptance criteria and evidence requirements explicitly declare this posture by title (for example: “Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under audit/qa/\\/\\”).  
``````

## Redline RL-058

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.3 “Prod via Codespaces” requirements (Epic Plan)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [154085, 154424); starting original line: 1570.

OLD TEXT:

``````text
This identity \+ vendor step does not change the identity-only semantics of /internal/version: the handshake remains a pre-flight proof of “which engine is live,” while the vendor-backed flow is what satisfies the vendor behavior portion of the D-goals and is recorded in the current Epic Plan acceptance criteria and evidence record.
``````

REPLACEMENT TEXT:

``````text
This identity \+ vendor step does not change the identity-only semantics of /internal/version: the handshake remains a pre-flight proof of “which engine is live,” while the vendor-backed flow is what satisfies the vendor behavior portion of the D-goals and is recorded in the current Epic Specification acceptance criteria and evidence record.
``````

## Redline RL-059

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.4 Live QA mechanical evidence expectations**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [154481, 154667); starting original line: 1574.

OLD TEXT:

``````text
For Live QA epics, mechanical, step-explicit QA is still required — but it belongs in the QA Plan and QA execution artifacts, not embedded inside the Epic Plan or Implementation Plan.
``````

REPLACEMENT TEXT:

``````text
For Live QA epics, mechanical, step-explicit QA is still required — but it belongs in the QA Plan and QA execution artifacts, not embedded inside the Epic Specification or Implementation Plan.
``````

## Redline RL-060

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.4 Live QA mechanical evidence expectations**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [155156, 155184); starting original line: 1578.

OLD TEXT:

``````text
The Epic Plan MUST provide:
``````

REPLACEMENT TEXT:

``````text
The Epic Specification MUST provide:
``````

## Redline RL-061

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [178944, 179246); starting original line: 1814.

OLD TEXT:

``````text
For any epic that can affect real production functionality, QA readiness and closeout review MUST account for at least one bounded open-rails Live QA step that proves relevant production-facing behavior in the deployed or PO-approved live target, unless an explicit exemption is approved and recorded.
``````

REPLACEMENT TEXT:

``````text
For any epic that can affect real production functionality, QA readiness and closeout review MUST account for at least one bounded open-rails Live QA step that proves relevant production-facing behavior in the deployed or PO-approved live target, unless an explicit exemption is approved and recorded.

Mandatory vendor minimum for production-functional surfaces. The QA Plan of every Epic touching any surface used to produce a production feature described as functional in PF canon MUST include a live vendor call under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`), using synthetic data only. A Plan without that test is not approval-ready, including an earlier approved Plan that omits it. Identify the affected surfaces from the Epic’s Specification and plans; this guide does not invent a universal surface roster. No real person, user or production data is used.

For this scope, closed-rails fixtures, replay, mocks, fake services, static analysis, generated or governed evidence, path proofs, Index/Mirror refreshes, repository audits, review approval, an unrun smoke procedure and Ops discovery without the live vendor call do not satisfy the requirement. A live service check or database read alone is also insufficient. Existing Product Owner authorization, defined request limits, step-scoped rails, stop checks, secret-safe capture, redaction and failure classification still apply. The rule authorizes no load, stress or volume testing, public route, flag, payload change or production Reader change. Ops smoke evidence remains Ops evidence. The test proves only what it exercises, without implying full vendor conformance, QA PASS, acceptance, work-item status movement, deployment or closure.

This minimum supersedes the exemption alternatives and non-vendor substitution below only for that scope. No retained exemption ground for an in-scope Plan has been determined by the Product Owner; this guide does not resolve that open question. Outside that scope, the broader production-affecting rule and its existing bounded exemption procedure remain operative.
``````

## Redline RL-062

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [180613, 181148); starting original line: 1841.

OLD TEXT:

``````text
A valid open-rails Live QA step may include, when scoped and authorized: live deployed service check, live vendor smoke, live API call against a deployed target, live DB bridge read/write check, live persistence and retrieval check, live request-shaping check with redacted proof, live response-shape check with redacted proof, live authentication or credential-binding confirmation, live environment-variable binding confirmation, live app-to-engine integration check, or live CLI/API behavior check against a real configured target.
``````

REPLACEMENT TEXT:

``````text
Outside the mandatory production-functional vendor scope above, a valid open-rails Live QA step may include, when scoped and authorized: live deployed service check, live vendor smoke, live API call against a deployed target, live DB bridge read/write check, live persistence and retrieval check, live request-shaping check with redacted proof, live response-shape check with redacted proof, live authentication or credential-binding confirmation, live environment-variable binding confirmation, live app-to-engine integration check, or live CLI/API behavior check against a real configured target.
``````

## Redline RL-063

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [181149, 181649); starting original line: 1843.

OLD TEXT:

``````text
The following do not satisfy the required open-rails Live QA step by themselves: unit tests, integration tests against fake services, closed-rails fixture replay, static analysis, generated evidence artifacts, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, Codex audit, PF10 supportability note, implementation review approval, QA Plan approval, smoke procedure written but not run, or OPS discovery without live behavior proof.
``````

REPLACEMENT TEXT:

``````text
The following do not satisfy the required open-rails Live QA step by themselves: unit tests, integration tests against fake services, closed-rails fixture replay, static analysis, generated evidence artifacts, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, read-only repository audit, PF10 supportability note, implementation review approval, QA Plan approval, smoke procedure written but not run, or OPS discovery without live behavior proof.
``````

## Redline RL-064

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [182690, 183446); starting original line: 1849.

OLD TEXT:

``````text
Exemption is allowed only with explicit justification. A Live QA Plan may omit open-rails Live QA only when at least one of the following is true: the epic has no production, runtime, compute, vendor, persistence, deployed, integration, public, or external-service effect; the live step would be unsafe; the live step would expose secrets or private data and no redacted safe alternative exists; the PO explicitly withholds authorization; the required deployed target is unavailable and cannot be safely reached; the work is documentation-only and does not affect production behavior; the work is planning-only and does not claim implementation readiness; or the work is a closed-rails-only proof slice and no production functionality claim is being made.
``````

REPLACEMENT TEXT:

``````text
Outside that mandatory scope, exemption is allowed only with explicit justification. A Live QA Plan may omit open-rails Live QA only when at least one of the following is true: the epic has no production, runtime, compute, vendor, persistence, deployed, integration, public, or external-service effect; the live step would be unsafe; the live step would expose secrets or private data and no redacted safe alternative exists; the PO explicitly withholds authorization; the required deployed target is unavailable and cannot be safely reached; the work is documentation-only and does not affect production behavior; the work is planning-only and does not claim implementation readiness; or the work is a closed-rails-only proof slice and no production functionality claim is being made.
``````

## Redline RL-065

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [183447, 183715); starting original line: 1851.

OLD TEXT:

``````text
If an exemption is used, the Live QA Plan MUST state why open-rails Live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release. Default posture: no exemption.
``````

REPLACEMENT TEXT:

``````text
For that outside-scope exemption procedure, if an exemption is used, the Live QA Plan MUST state why open-rails Live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release. Default posture: no exemption.
``````

## Redline RL-066

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [183716, 184067); starting original line: 1853.

OLD TEXT:

``````text
A Live QA Plan for a production-affecting epic is not approval-ready unless it includes at least one open-rails Live QA step or a clear, authorized exemption. Reviewers MUST NOT accept a closed-rails-only Live QA Plan for a production-affecting epic without explicit exemption language. This is a truth/proof requirement, not a formatting preference.
``````

REPLACEMENT TEXT:

``````text
Outside the mandatory production-functional vendor scope above, a Live QA Plan for a production-affecting epic is not approval-ready unless it includes at least one open-rails Live QA step or a clear, authorized exemption. Reviewers MUST NOT accept a closed-rails-only Live QA Plan for a production-affecting epic without explicit exemption language. This is a truth/proof requirement, not a formatting preference.
``````

## Redline RL-067

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.5 Live QA behavior vs artifact pattern**
#### **1.1.5A Production-affecting open-rails Live QA requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [184068, 184918); starting original line: 1855.

OLD TEXT:

``````text
PR, OPS, and QA sequencing MUST support bounded live proof when required. Open-rails Live QA may be PO-run or PO-authorized where secrets, external services, or deployed environments are involved. CodEx and implementation agents may prepare repo-local code, fixtures, validators, redaction helpers, harnesses, documentation, and evidence-processing logic. When a required live external action is an otherwise-permitted Ops task, it MAY be performed personally by the PO or by an explicitly delegated automated session agent under the applicable Ops authorization, scope, safety, stop-check, redaction, evidence, and completion-claim controls. Delegation does not convert Ops evidence into QA evidence. Secret values MUST remain out of commands, logs, chat output, and repo evidence unless an external system securely injects them without disclosure.
``````

REPLACEMENT TEXT:

``````text
PR, OPS, and QA sequencing MUST support bounded live proof when required. Open-rails Live QA may be PO-run or PO-authorized where secrets, external services, or deployed environments are involved. The executing agent and implementation agents may prepare repo-local code, fixtures, validators, redaction helpers, harnesses, documentation, and evidence-processing logic. When a required live external action is an otherwise-permitted Ops task, it MAY be performed personally by the PO or by an explicitly delegated automated session agent under the applicable Ops authorization, scope, safety, stop-check, redaction, evidence, and completion-claim controls. Delegation does not convert Ops evidence into QA evidence. Secret values MUST remain out of commands, logs, chat output, and repo evidence unless an external system securely injects them without disclosure.
``````

## Redline RL-068

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.6 PO Live QA vendor-first scope**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [184964, 185055); starting original line: 1859.

OLD TEXT:

``````text
When an Epic Plan describes PO Live QA (a Live QA session that requires PO time), it MUST:
``````

REPLACEMENT TEXT:

``````text
When an Epic Specification describes PO Live QA (a Live QA session that requires PO time), it MUST:
``````

## Redline RL-069

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.6 PO Live QA vendor-first scope**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [186767, 187089); starting original line: 1872.

OLD TEXT:

``````text
  * Ensure that artifacts for vendor steps are clearly identifiable as vendor evidence (for example via a vendor-specific subdirectory or filename convention) so that they can be bound to the applicable stable acceptance criteria, tests, and evidence requirements in the current Epic Plan and Glow QA Guide (titles-only).
``````

REPLACEMENT TEXT:

``````text
  * Ensure that artifacts for vendor steps are clearly identifiable as vendor evidence (for example via a vendor-specific subdirectory or filename convention) so that they can be bound to the applicable stable acceptance criteria, tests, and evidence requirements in the current Epic Specification and Glow QA Guide (titles-only).
``````

## Redline RL-070

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [189609, 189695); starting original line: 1909.

OLD TEXT:

``````text
* a CodEx audit snippet that lists the CLI shape as discovered behavior for this repo
``````

REPLACEMENT TEXT:

``````text
* a read-only repository audit snippet that lists the CLI shape as discovered behavior for this repo
``````

## Redline RL-071

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [189987, 190163); starting original line: 1917.

OLD TEXT:

``````text
* use command shapes that are explicitly documented as supported (for example a shell-level presence check or a help/usage invocation taken from the CLI spec or CodEx audit)  
``````

REPLACEMENT TEXT:

``````text
* use command shapes that are explicitly documented as supported (for example a shell-level presence check or a help/usage invocation taken from the CLI spec or read-only repository audit)  
``````

## Redline RL-072

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [190813, 190850); starting original line: 1928.

OLD TEXT:

``````text
* a CodEx audit report for this repo
``````

REPLACEMENT TEXT:

``````text
* a read-only repository audit report for this repo
``````

## Redline RL-073

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [191327, 191444); starting original line: 1939.

OLD TEXT:

``````text
During Epic Plan review for epics that include CLI steps (especially Live QA epics), Lead Dev and QA reviewers MUST:
``````

REPLACEMENT TEXT:

``````text
During Epic Specification review for epics that include CLI steps (especially Live QA epics), Lead Dev and QA reviewers MUST:
``````

## Redline RL-074

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [191445, 191546); starting original line: 1941.

OLD TEXT:

``````text
* spot-check CLI commands in the Plan against HDE-CLI-API-Vendor-Ref, tests, or CodEx audit output  
``````

REPLACEMENT TEXT:

``````text
* spot-check CLI commands in the Plan against HDE-CLI-API-Vendor-Ref, tests, or read-only repository audit output  
``````

## Redline RL-075

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [191880, 192091); starting original line: 1949.

OLD TEXT:

``````text
Interaction with other sections: This section refines §0.6.1 “Canon-first planning” for CLI usage: CLI behavior in QA Plans must come from the CLI spec, tests, or CodEx audit, not from generic assumptions.
``````

REPLACEMENT TEXT:

``````text
Interaction with other sections: This section refines §0.6.1 “Canon-first planning” for CLI usage: CLI behavior in QA Plans must come from the CLI spec, tests, or read-only repository audit, not from generic assumptions.
``````

## Redline RL-076

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [192363, 192465); starting original line: 1956.

OLD TEXT:

``````text
Plans are non-conforming and MUST be revised before Epic Plan approval or Live QA scheduling if they:
``````

REPLACEMENT TEXT:

``````text
Plans are non-conforming and MUST be revised before Epic Specification approval or Live QA scheduling if they:
``````

## Redline RL-077

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.8 CLI commands in QA Plans (canon-backed only)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [192466, 192576); starting original line: 1958.

OLD TEXT:

``````text
* rely on CLI commands or flags that are not present in any PF-Canon CLI spec, test harness, or CodEx audit  
``````

REPLACEMENT TEXT:

``````text
* rely on CLI commands or flags that are not present in any PF-Canon CLI spec, test harness, or read-only repository audit  
``````

## Redline RL-078

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.10 PLAN submission preflight (mechanical gate: exact sources \+ evidence paths)**
#### **1.1.10.2 Exact-source and acceptance-evidence validation**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [195328, 195392); starting original line: 1993.

OLD TEXT:

``````text
Before finalizing Epic Plan acceptance claims, the author MUST:
``````

REPLACEMENT TEXT:

``````text
Before finalizing Epic Specification acceptance claims, the author MUST:
``````

## Redline RL-079

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.10 PLAN submission preflight (mechanical gate: exact sources \+ evidence paths)**
#### **1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [197961, 198149); starting original line: 2028.

OLD TEXT:

``````text
Every acceptance token to artifact binding that appears in an Epic Plan and in the token/evidence matrix MUST be validated against the canonical evidence catalog before approval or merge.
``````

REPLACEMENT TEXT:

``````text
Every acceptance token to artifact binding that appears in an Epic Specification and in the token/evidence matrix MUST be validated against the canonical evidence catalog before approval or merge.
``````

## Redline RL-080

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.10 PLAN submission preflight (mechanical gate: exact sources \+ evidence paths)**
#### **1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [206350, 206405); starting original line: 2139.

OLD TEXT:

``````text
* Epic Plan required evidence list (per deliverable)  
``````

REPLACEMENT TEXT:

``````text
* Epic Specification required evidence list (per deliverable)  
``````

## Redline RL-081

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [215968, 216148); starting original line: 2237.

OLD TEXT:

``````text
Review stability and no-moving-target discipline applies to diff-first approval loops for Epic Plans, Implementation Plans, Live QA Plans, remediation plans, and closeout reviews.
``````

REPLACEMENT TEXT:

``````text
Review stability and no-moving-target discipline applies to diff-first approval loops for Epic Specifications, Implementation Plans, Live QA Plans, remediation plans, and closeout reviews.
``````

## Redline RL-082

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [222153, 222439); starting original line: 2275.

OLD TEXT:

``````text
Epic Plans are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Plan review MUST NOT demand QA-runbook-level precision, close-pack-level evidence completeness, or template inventory polish unless current planning truth depends on it.
``````

REPLACEMENT TEXT:

``````text
Epic Specifications are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Specification review MUST NOT demand QA-runbook-level precision, close-pack-level evidence completeness, or template inventory polish unless current planning truth depends on it.
``````

## Redline RL-083

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [222440, 222697); starting original line: 2277.

OLD TEXT:

``````text
Implementation Plans must be concrete enough for CodEx and OPS separation. A plan may be blocked for an independent non-syntax defect only when that defect remains after faithful syntax normalization and is proven without relying on malformed presentation.
``````

REPLACEMENT TEXT:

``````text
Implementation Plans must be concrete enough for the executing agent and OPS separation. A plan may be blocked for an independent non-syntax defect only when that defect remains after faithful syntax normalization and is proven without relying on malformed presentation.
``````

## Redline RL-084

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [222733, 223047); starting original line: 2281.

OLD TEXT:

``````text
Plans, review prompts, redline prompts, plan redlines, Codex prompts, remediation plans, QA Plans, Live QA Plans, Implementation Plans, Epic Plans, implementation-readiness reviews, QA closeout reviews, epic closure reviews, and closure-review artifacts are planning and review artifacts, not execution artifacts.
``````

REPLACEMENT TEXT:

``````text
Plans, review prompts, redline prompts, plan redlines, executing-agent prompts, remediation plans, QA Plans, Live QA Plans, Implementation Plans, Epic Specifications, implementation-readiness reviews, QA closeout reviews, epic closure reviews, and closure-review artifacts are planning and review artifacts, not execution artifacts.
``````

## Redline RL-085

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [228234, 228597); starting original line: 2328.

OLD TEXT:

``````text
During execution, the assigned operator, QA executor, CodEx, Kronos, Product Owner, implementation owner, or other authorized executor may normalize syntax without requiring plan revision when the normalization preserves the plan’s semantic contract. The exact command actually executed, its exit code, and its captured output belong in the execution evidence.
``````

REPLACEMENT TEXT:

``````text
During execution, the assigned operator, QA executor, the executing agent, Kronos, Product Owner, implementation owner, or other authorized executor may normalize syntax without requiring plan revision when the normalization preserves the plan’s semantic contract. The exact command actually executed, its exit code, and its captured output belong in the execution evidence.
``````

## Redline RL-086

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [234969, 235275); starting original line: 2373.

OLD TEXT:

``````text
* Business Case is missing or not product-oriented: every Epic Plan MUST include a clearly labeled Business Case section that explains the product goal, the user problem, and the value (what changes for the user and what success looks like). If missing or purely technical, return the plan for revision.  
``````

REPLACEMENT TEXT:

``````text
* Business Case is missing or not product-oriented: every Epic Specification MUST include a clearly labeled Business Case section that explains the product goal, the user problem, and the value (what changes for the user and what success looks like). If missing or purely technical, return the plan for revision.  
``````

## Redline RL-087

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [235275, 235581); starting original line: 2374.

OLD TEXT:

``````text
* Contract Change Justification is missing: the Epic Plan MUST include a clearly labeled Contract Change Justification section that explains any new or modified contract surfaces (CLI flags or modes, endpoint routes, output shapes) and why a new surface is necessary rather than reusing an existing one.  
``````

REPLACEMENT TEXT:

``````text
* Contract Change Justification is missing: the Epic Specification MUST include a clearly labeled Contract Change Justification section that explains any new or modified contract surfaces (CLI flags or modes, endpoint routes, output shapes) and why a new surface is necessary rather than reusing an existing one.  
``````

## Redline RL-088

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.1 Epic-lane workflow at a glance**
### **1.1.11 Plan review rules (content-first; blockers vs caveats)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [235581, 235841); starting original line: 2375.

OLD TEXT:

``````text
* Backward compatibility posture is missing: the Epic Plan MUST include a clearly labeled Backward Compatibility posture section that states what remains unchanged by default, what changes (if anything), and the rollback plan if the change must be reverted.  
``````

REPLACEMENT TEXT:

``````text
* Backward compatibility posture is missing: the Epic Specification MUST include a clearly labeled Backward Compatibility posture section that states what remains unchanged by default, what changes (if anything), and the rollback plan if the change must be reverted.  
``````

## Redline RL-089

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.2 PLAN: Machine header (paste and fill, then post)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [249345, 249405); starting original line: 2487.

OLD TEXT:

``````text
## **1.2 PLAN: Machine header (paste and fill, then post)**
``````

REPLACEMENT TEXT:

``````text
## **1.2 SPECIFICATION: Resolve and use the current owning format**
``````

## Redline RL-090

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.2 PLAN: Machine header (paste and fill, then post)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [249406, 249741); starting original line: 2489.

OLD TEXT:

``````text
Use the current **Epic Record Template (Normative)** in PF27-Canon-Plan-Templates. That template is the canonical home for the complete Epic Plan shape, required and conditional fields, contract and compatibility posture, stable requirement and acceptance-criterion identities, evidence pointers, review guards, and close preparation.
``````

REPLACEMENT TEXT:

``````text
Use the current **Epic Record Template (Normative)** in PF27-Canon-Plan-Templates. That template is the canonical home for the complete Epic Specification shape, required and conditional fields, contract and compatibility posture, stable requirement and acceptance-criterion identities, evidence pointers, review guards, and close preparation.
``````

## Redline RL-091

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.2 PLAN: Machine header (paste and fill, then post)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [249742, 250197); starting original line: 2491.

OLD TEXT:

``````text
PF06 retains the process boundaries in this H1: complete the current-state canon and repository inventory before drafting; preserve scope, dependencies, public-interface posture, outcomes, acceptance intent, evidence obligations, risks, open decisions, canon anchors, and applicable context-header requirements; exchange proposed code capsules before Implementation Plan approval; and satisfy the Epic Plan approval workflow and adjacent pre-start gates.
``````

REPLACEMENT TEXT:

``````text
PF06 retains the process boundaries in this H1: complete the current-state canon and repository inventory before drafting; preserve scope, dependencies, public-interface posture, outcomes, acceptance intent, evidence obligations, risks, open decisions, canon anchors, and applicable context-header requirements; exchange proposed code capsules before Implementation Plan approval; and satisfy the Epic Specification approval workflow and adjacent pre-start gates.
``````

## Redline RL-092

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.3 Epic approval record**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [250236, 250547); starting original line: 2497.

OLD TEXT:

``````text
The approved Epic Plan and its required approval establish the Epic lane’s bounded scope, governing and acceptance-criterion identities, and applicable evidence obligations. Plan Templates owns the reusable Epic Plan and approval-record structure. PF06 does not use CRD as an epic-internal approval artifact.
``````

REPLACEMENT TEXT:

``````text
The approved Epic Specification and its required approval establish the Epic lane’s bounded scope, governing and acceptance-criterion identities, and applicable evidence obligations. Plan Templates owns the reusable Epic Specification and approval-record structure. PF06 does not use CRD as an epic-internal approval artifact.
``````

## Redline RL-093

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**
## **1.5 Code capsules (Epic Plan samples)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [250952, 250997); starting original line: 2505.

OLD TEXT:

``````text
## **1.5 Code capsules (Epic Plan samples)**
``````

REPLACEMENT TEXT:

``````text
## **1.5 Code capsules (Epic Specification samples)**
``````

## Redline RL-094

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [251956, 252055); starting original line: 2529.

OLD TEXT:

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
``````

REPLACEMENT TEXT:

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Specification or CRD Specification approval)**
``````

## Redline RL-095

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [252056, 252493); starting original line: 2531.

OLD TEXT:

``````text
Define how work proceeds after the applicable Epic Plan or CRD Plan approval in a way CodEx can execute with minimal inference. Lead Dev approves once and later performs the PR gate only when the authorized route uses a PR. Each issued guide MUST identify the exact repository baseline and selected mutation route, resolve whether CodEx can read PF documents, and include all execution-critical material required by that access posture.
``````

REPLACEMENT TEXT:

``````text
Define how work proceeds after the applicable Epic Specification or CRD Specification approval in a way the executing agent can execute with minimal inference. Lead Dev approves once and later performs the PR gate only when the authorized route uses a PR. Each issued guide MUST identify the exact repository baseline and selected mutation route, establish the actual executing agent’s ability to read PF documents and other required inputs, and include all execution-critical material required by that access posture.
``````

## Redline RL-096

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [252494, 253016); starting original line: 2533.

OLD TEXT:

``````text
PF06 owns the approved-plan-to-guide-to-implementation-plan sequence, role handoffs, mutation-route decision, gate timing, and PO-only merge consequence when a PR is used. The normal code-bearing route assigns CodEx to open or amend a PR. Agent direct-main mutation requires an explicit current operator instruction covering the exact change. Repo docs and applicable evidence-index, hash, mirror, and path-proof companions MUST change in the same authorized mutation set whenever their owning requirements are triggered.
``````

REPLACEMENT TEXT:

``````text
PF06 owns the approved-Specification-to-guide-to-implementation-plan sequence, role handoffs, mutation-route decision, gate timing, and PO-only merge consequence when a PR is used. The normal code-bearing route assigns the executing agent to open or amend a PR. Agent direct-main mutation requires an explicit current operator instruction covering the exact change. Repo docs and applicable evidence-index, hash, mirror, and path-proof companions MUST change in the same authorized mutation set whenever their owning requirements are triggered.
``````

## Redline RL-097

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [255718, 255864); starting original line: 2575.

OLD TEXT:

``````text
"The Implementation Agent sends CodEx an audit request with the explicit formats and execution-critical material required by the approved scope."
``````

REPLACEMENT TEXT:

``````text
"The Implementation Agent sends the executing agent an audit request with the explicit formats and execution-critical material required by the approved scope."
``````

## Redline RL-098

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [255864, 256013); starting original line: 2576.

OLD TEXT:

``````text
"CodEx resolves and records the current repository ref and returns an audit report separating observed facts, gaps, risks, proposals, and unknowns."
``````

REPLACEMENT TEXT:

``````text
"The executing agent resolves and records the current repository ref and returns an audit report separating observed facts, gaps, risks, proposals, and unknowns."
``````

## Redline RL-099

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [256169, 256269); starting original line: 2578.

OLD TEXT:

``````text
"The Implementation Agent sends CodEx build instructions and verbatim execution-critical material."
``````

REPLACEMENT TEXT:

``````text
"The Implementation Agent sends the executing agent build instructions and verbatim execution-critical material."
``````

## Redline RL-100

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [256269, 256437); starting original line: 2579.

OLD TEXT:

``````text
"CodEx verifies that its base remains current, builds and verifies only the approved scope, and returns the detailed change report and produced artifacts or evidence."
``````

REPLACEMENT TEXT:

``````text
"The executing agent verifies that its base remains current, builds and verifies only the approved scope, and returns the detailed change report and produced artifacts or evidence."
``````

## Redline RL-101

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [256542, 256731); starting original line: 2581.

OLD TEXT:

``````text
"CodEx performs the expressly authorized mutation route: PR for the normal code-bearing path, or direct-main only under an explicit current operator instruction covering the exact change."
``````

REPLACEMENT TEXT:

``````text
"The executing agent performs the expressly authorized mutation route: PR for the normal code-bearing path, or direct-main only under an explicit current operator instruction covering the exact change."
``````

## Redline RL-102

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [256731, 256889); starting original line: 2582.

OLD TEXT:

``````text
"For a PR, CodEx records the exact PR and candidate identities. For direct-main, CodEx records the exact post-write SHA, diff, and applicable push-CI state."
``````

REPLACEMENT TEXT:

``````text
"For a PR, the executing agent records the exact PR and candidate identities. For direct-main, the executing agent records the exact post-write SHA, diff, and applicable push-CI state."
``````

## Redline RL-103

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [257011, 258841); starting original line: 2584.

OLD TEXT:

``````text
"The Product Owner alone performs any authorized merge and separately records any acceptance or closure decision." roles: lead_dev: "Approves the Implementation Plan once; then acts as PR gate when a PR is used and checks applicable acceptance and evidence requirements." implementation_agent: "Coordinates with CodEx, supplies explicit formats and execution-critical material, reviews the change report, and prepares supported closure material without claiming unproved state." codex: "Performs the audit and authorized build or verification work, follows only the expressly authorized mutation route, adapts only within scope, and reports every change and limitation." po: "Routes communications, retains direct-main authority, performs any authorized merge, and records scoped decisions without collapsing repository presence, QA, acceptance, or closure." evidence_routing: interim: "Audit, build, verification, and result observations return to the Implementation Agent with their actual claim state and exact source identity." pr: "A PR carries the exact slice, repo-doc changes, and every applicable governed evidence companion; close-pack artifacts are close-only." direct_main: "A direct-main mutation records the current authorization, exact post-write SHA, diff, and applicable push-triggered CI result." repo_docs: "Applicable repo-doc and evidence-companion changes land in the same authorized mutation set." final: "After repository adoption, QA, acceptance, closure, and board or planning updates proceed separately through their owning authorized processes." determinism_pins: lc_all: "C" tz: "UTC" capsules_scope: "Capsules finalized by an approved Implementation Plan remain immutable; scoped adaptation is allowed only when reported and otherwise authorized." codex_can_see_pf_docs: "unassessed"
``````

REPLACEMENT TEXT:

``````text
"The Product Owner alone performs any authorized merge and separately records any acceptance or closure decision." roles: lead_dev: "Approves the Implementation Plan once; then acts as PR gate when a PR is used and checks applicable acceptance and evidence requirements." implementation_agent: "Coordinates with the executing agent, supplies explicit formats and execution-critical material, reviews the change report, and prepares supported closure material without claiming unproved state." codex: "Performs the audit and authorized build or verification work, follows only the expressly authorized mutation route, adapts only within scope, and reports every change and limitation." po: "Routes communications, retains direct-main authority, performs any authorized merge, and records scoped decisions without collapsing repository presence, QA, acceptance, or closure." evidence_routing: interim: "Audit, build, verification, and result observations return to the Implementation Agent with their actual claim state and exact source identity." pr: "A PR carries the exact slice, repo-doc changes, and every applicable governed evidence companion; close-pack artifacts are close-only." direct_main: "A direct-main mutation records the current authorization, exact post-write SHA, diff, and applicable push-triggered CI result." repo_docs: "Applicable repo-doc and evidence-companion changes land in the same authorized mutation set." final: "After repository adoption, QA, acceptance, closure, and board or planning updates proceed separately through their owning authorized processes." determinism_pins: lc_all: "C" tz: "UTC" capsules_scope: "Capsules finalized by an approved Implementation Plan remain immutable; scoped adaptation is allowed only when reported and otherwise authorized." codex_can_see_pf_docs: "unassessed"
``````

## Redline RL-104

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [259742, 259767); starting original line: 2591.

OLD TEXT:

``````text
## **2.2 Audit (CodEx)**
``````

REPLACEMENT TEXT:

``````text
## **2.2 Audit (the executing agent)**
``````

## Redline RL-105

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [259768, 260074); starting original line: 2593.

OLD TEXT:

``````text
Goal. Establish that the codebase can host the change without violating canon, and surface any gaps or risks before Build/Test. CodEx responds in prose and fills the output fields; the Implementation Agent (IA) provides the audit template and any verbatim snippets or schema fragments required for checks.
``````

REPLACEMENT TEXT:

``````text
Goal. Establish that the codebase can host the change without violating canon, and surface any gaps or risks before Build/Test. The executing agent responds in prose and fills the output fields; the Implementation Agent (IA) provides the audit template and any verbatim snippets or schema fragments required for checks.
``````

## Redline RL-106

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [264155, 264408); starting original line: 2616.

OLD TEXT:

``````text
* Gaps & proposals. List missing components/schemas; propose minimal fixes or scoped improvements; call out any risks that would block CodEx from using the expressly authorized mutation route and satisfying the applicable governing acceptance criteria.
``````

REPLACEMENT TEXT:

``````text
* Gaps & proposals. List missing components/schemas; propose minimal fixes or scoped improvements; call out any risks that would block the executing agent from using the expressly authorized mutation route and satisfying the applicable governing acceptance criteria.
``````

## Redline RL-107

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [264409, 264466); starting original line: 2618.

OLD TEXT:

``````text
Output fields (CodEx fills; IA provides this structure):
``````

REPLACEMENT TEXT:

``````text
Output fields (the executing agent fills; IA provides this structure):
``````

## Redline RL-108

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
### **Findings → Doc Delta Map (required; single sink)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [265493, 265716); starting original line: 2659.

OLD TEXT:

``````text
In addition to the structured output fields above, CodEx MUST provide a short narrative audit report that is directly drainable into Doc-Delta and PO adjudication when canon ambiguity or implementation drift is discovered.
``````

REPLACEMENT TEXT:

``````text
In addition to the structured output fields above, the executing agent MUST provide a short narrative audit report that is directly drainable into Doc-Delta and PO adjudication when canon ambiguity or implementation drift is discovered.
``````

## Redline RL-109

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
### **Findings → Doc Delta Map (required; single sink)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [267748, 267886); starting original line: 2704.

OLD TEXT:

``````text
Epic Plan linkage (one sentence): state how the finding maps to epic scope, or state that it does not create new planned runnable work.  
``````

REPLACEMENT TEXT:

``````text
Epic Specification linkage (one sentence): state how the finding maps to epic scope, or state that it does not create new planned runnable work.  
``````

## Redline RL-110

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.2 Audit (CodEx)**
### **Findings → Doc Delta Map (required; single sink)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [267886, 267951); starting original line: 2705.

OLD TEXT:

``````text
Epic Plan anchor: quote the governing plan line, or write N/A.  
``````

REPLACEMENT TEXT:

``````text
Epic Specification anchor: quote the governing plan line, or write N/A.  
``````

## Redline RL-111

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.3 Code Review (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [270104, 270135); starting original line: 2767.

OLD TEXT:

``````text
## **2.3 Code Review (CodEx)**
``````

REPLACEMENT TEXT:

``````text
## **2.3 Code Review (the executing agent)**
``````

## Redline RL-112

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after Epic Plan or CRD Plan approval)**
## **2.4 Sandbox Build/Test (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [271477, 271515); starting original line: 2789.

OLD TEXT:

``````text
## **2.4 Sandbox Build/Test (CodEx)**
``````

REPLACEMENT TEXT:

``````text
## **2.4 Sandbox Build/Test (the executing agent)**
``````

## Redline RL-113

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [273634, 273800); starting original line: 2832.

OLD TEXT:

``````text
"verbatim\_payloads": \["\\", "\\", "\\"\], // CodEx can read PF docs; still paste execution-critical material verbatim to keep an unambiguous in-session reference  
``````

REPLACEMENT TEXT:

``````text
"verbatim\_payloads": \["\\", "\\", "\\"\], // Assess actual executing-agent PF/input access; still paste execution-critical material verbatim to keep an unambiguous in-session reference  
``````

## Redline RL-114

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [273824, 273920); starting original line: 2834.

OLD TEXT:

``````text
"freedom\_within\_scope": "CodEx may adapt/fix within scope; must report all changes at end",  
``````

REPLACEMENT TEXT:

``````text
"freedom\_within\_scope": "The executing agent may adapt/fix within scope; must report all changes at end",  
``````

## Redline RL-115

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [274905, 274964); starting original line: 2856.

OLD TEXT:

``````text
CodEx portability rule (Implementation Plan codex\_inputs)
``````

REPLACEMENT TEXT:

``````text
Execution prompt portability rule (Implementation Plan codex\_inputs)
``````

## Redline RL-116

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.1 Machine header**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [274965, 275415); starting original line: 2858.

OLD TEXT:

``````text
The final implementation prompt given to CodEx MUST be self-contained. Do not reference planning-time CodEx audit artifacts or “CA vetted” notes as external context. If a planning artifact uses CA vetted or IG Approved quotes for validation, convert them into canon citations and explicit repo paths before handing off to CodEx. Paste any execution-critical schemas, formats, or commands inline, because CodEx cannot access external attachments.
``````

REPLACEMENT TEXT:

``````text
The final implementation prompt given to the executing agent MUST be self-contained. Do not reference planning-time read-only repository audit artifacts or “CA vetted” notes as external context. If a planning artifact uses CA vetted or IG Approved quotes for validation, convert them into canon citations and explicit repo paths before execution handoff. Paste execution-critical schemas, formats and commands inline. Establish the actual agent’s input-access limits in the Implementation Guide and use the Asset Draft Pack route in Appendix A whenever required material cannot be supplied reliably inline or through accessible repository contents.
``````

## Redline RL-117

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.4 Approval**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [275900, 276053); starting original line: 2887.

OLD TEXT:

``````text
From this point, CodEx and IA proceed per the approved IP. Lead Dev returns for the PR gate only when the expressly authorized mutation route uses a PR.
``````

REPLACEMENT TEXT:

``````text
From this point, the executing agent and IA proceed per the approved IP. Lead Dev returns for the PR gate only when the expressly authorized mutation route uses a PR.
``````

## Redline RL-118

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.1 Requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [276118, 276315); starting original line: 2893.

OLD TEXT:

``````text
The normal code-bearing epic route is PR-first via Codex. The Product Owner MAY explicitly authorize direct-to-`main` mutation for the exact change. An agent MUST NOT infer direct-main permission.
``````

REPLACEMENT TEXT:

``````text
The normal code-bearing epic route is PR-first via the executing agent. The Product Owner MAY explicitly authorize direct-to-`main` mutation for the exact change. An agent MUST NOT infer direct-main permission.
``````

## Redline RL-119

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.1 Requirement**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [276316, 276567); starting original line: 2895.

OLD TEXT:

``````text
For a PR route, Codex opens PRs for the authorized epic slices and pushes code, Doc-Delta, and applicable evidence in the same PR. A multi-PR epic MAY use up to 10 PRs, and each PR MUST be self-contained and follow the PR-route parity rules in §0.2.
``````

REPLACEMENT TEXT:

``````text
For a PR route, the executing agent opens PRs for the authorized epic slices and pushes code, Doc-Delta, and applicable evidence in the same PR. A multi-PR epic MAY use up to 10 PRs, and each PR MUST be self-contained and follow the PR-route parity rules in §0.2.
``````

## Redline RL-120

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [295048, 295450); starting original line: 3125.

OLD TEXT:

``````text
Workflow placement (Close Gate work product). The detailed Live QA plan or runbook (commands, step checks, QA root structure, and evidence landing mechanics) is authored as a separate QA artifact during the Close Gate stage. It MUST NOT be treated as an Epic Plan prerequisite and MUST NOT be embedded into Epic Plan or Implementation planning. See §0.4.1 for required Live QA execution deliverables.
``````

REPLACEMENT TEXT:

``````text
Workflow placement (Close Gate work product). The detailed Live QA plan or runbook (commands, step checks, QA root structure, and evidence landing mechanics) is authored as a separate QA artifact during the Close Gate stage. It MUST NOT be treated as an Epic Specification prerequisite and MUST NOT be embedded into Epic Specification or Implementation planning. See §0.4.1 for required Live QA execution deliverables.
``````

## Redline RL-121

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [296067, 296308); starting original line: 3133.

OLD TEXT:

``````text
* If the epic touches the vendor seam, the plan MUST include at least one vendor-focused PO step that hits the seam and records observable outputs (request signature, response shape, and any user-visible outputs), without leaking secrets.  
``````

REPLACEMENT TEXT:

``````text
* If the epic touches the vendor seam, the plan MUST include at least one vendor-focused Product Owner-authorized step that hits the seam and records observable outputs (request signature, response shape, and any user-visible outputs), without leaking secrets. A directed agent executes the identified task under §0.2.  
``````

## Redline RL-122

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [296308, 296536); starting original line: 3134.

OLD TEXT:

``````text
* If strict closed-rails posture blocks functional proof, the plan MAY open rails explicitly as a bounded exception. The plan MUST name the rails opening, justify it, keep it minimal, and capture it in the evidence artifacts.  
``````

REPLACEMENT TEXT:

``````text
* If strict closed-rails posture blocks functional proof, the plan MAY open rails explicitly as a bounded exception. For the mandatory production-functional vendor scope in §1.1.5A, the live vendor step MUST use open rails. The plan MUST name the rails opening, justify it, keep it minimal, and capture it in the evidence artifacts.  
``````

## Redline RL-123

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [296883, 297133); starting original line: 3141.

OLD TEXT:

``````text
* Exemption boundary: truly non-functional-only epics (docs, refactors with no behavior changes, schema-only updates with no runtime behavior changes) MAY omit functional proof, but the exemption MUST be explicitly justified and validated by the IG.
``````

REPLACEMENT TEXT:

``````text
* Exemption boundary: truly non-functional-only epics (docs, refactors with no behavior changes, schema-only updates with no runtime behavior changes) MAY omit functional proof, but the exemption MUST be explicitly justified and validated by the IG. This does not exempt an Epic within the mandatory production-functional vendor scope in §1.1.5A.
``````

## Redline RL-124

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [297299, 297335); starting original line: 3146.

OLD TEXT:

``````text
* closed-rails posture (env pins)  
``````

REPLACEMENT TEXT:

``````text
* closed-rails default posture (env pins), with the bounded open-rails live vendor step required for the scope in §1.1.5A  
``````

## Redline RL-125

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.2 Close PR contents**
#### **3.5.2.8 Live QA via harness (required for epic closeout)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [302722, 303033); starting original line: 3205.

OLD TEXT:

``````text
No QA-only epics that only test themselves. QA-heavy epics must deliver shared value. If an epic’s QA work does not upgrade shared QA tools or harnesses and does not strengthen Live QA coverage across multiple existing surfaces, the Epic Plan MUST be returned as non-conforming and re-scoped before approval.
``````

REPLACEMENT TEXT:

``````text
No QA-only epics that only test themselves. QA-heavy epics must deliver shared value. If an epic’s QA work does not upgrade shared QA tools or harnesses and does not strengthen Live QA coverage across multiple existing surfaces, the Epic Specification MUST be returned as non-conforming and re-scoped before approval.
``````

## Redline RL-126

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**
## **3.5 Close Gate (route-aware)**
### **3.5.5 Remediation PR pattern (separate from Live QA)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [315486, 315839); starting original line: 3353.

OLD TEXT:

``````text
Ops tasks are not remediation PRs. If any remediation requires privileged external actions (service config, secrets/env changes, infrastructure console actions, privileged DB operations), those steps are Ops tasks and MUST be handled as PO-only execution, IA-guided with secret-free, repo-stored evidence. They MUST NOT be represented as CodEx PR work.
``````

REPLACEMENT TEXT:

``````text
Ops tasks are not remediation PRs. If any remediation requires privileged external actions (service config, secrets/env changes, infrastructure console actions, privileged DB operations), those steps are Ops tasks and MUST be handled as PO-only execution, IA-guided with secret-free, repo-stored evidence. They MUST NOT be represented as PR work assigned to the executing agent.
``````

## Redline RL-127

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [316062, 316126); starting original line: 3359.

OLD TEXT:

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
``````

REPLACEMENT TEXT:

``````text
# **4\) PR & COMMIT PLAN (PR-first via the executing agent; Lead Dev gates)**
``````

## Redline RL-128

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
## **4.2 Required pre-merge evidence (titles-only; CodEx supplies artifacts)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [326636, 326715); starting original line: 3564.

OLD TEXT:

``````text
## **4.2 Required pre-merge evidence (titles-only; CodEx supplies artifacts)**
``````

REPLACEMENT TEXT:

``````text
## **4.2 Required pre-merge evidence (titles-only; the executing agent supplies artifacts)**
``````

## Redline RL-129

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
## **4.3 Guidance for PO (CodEx UI)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [327780, 327818); starting original line: 3572.

OLD TEXT:

``````text
## **4.3 Guidance for PO (CodEx UI)**
``````

REPLACEMENT TEXT:

``````text
## **4.3 Guidance for PO (executing-agent PR interface)**
``````

## Redline RL-130

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
## **4.3 Guidance for PO (CodEx UI)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [327819, 328055); starting original line: 3574.

OLD TEXT:

``````text
If an applicable governed file, required companion, or current registry-valid evidence binding is missing, do not merge. Ask the IA to have CodEx amend the current PR so the applicable material lands in the same PR before squash-merge.
``````

REPLACEMENT TEXT:

``````text
If an applicable governed file, required companion, or current registry-valid evidence binding is missing, do not merge. Ask the IA to have the executing agent amend the current PR so the applicable material lands in the same PR before squash-merge.
``````

## Redline RL-131

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
## **4.3 Guidance for PO (CodEx UI)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [328056, 328386); starting original line: 3576.

OLD TEXT:

``````text
PF23 consult is not a PR-review input. Do not consult PF23 or treat it as a blocker during PR analysis. If a PF23 statement appears to conflict with PF canon or the approved Epic Plan or CRD Plan, record a drift item and route it to the Product Owner for adjudication; do not block merge solely on an unadjudicated PF23 conflict.
``````

REPLACEMENT TEXT:

``````text
PF23 consult is not a PR-review input. Do not consult PF23 or treat it as a blocker during PR analysis. If a PF23 statement appears to conflict with PF canon or the approved Epic Specification or CRD Specification, record a drift item and route it to the Product Owner for adjudication; do not block merge solely on an unadjudicated PF23 conflict.
``````

## Redline RL-132

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**
## **4.5 PR template — evidence-only QA**
### **Artifacts included (titles and repo-relative paths only)**
#### **CLI / Reader parity & determinism**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [334449, 334540); starting original line: 3672.

OLD TEXT:

``````text
* Dev connectivity snapshot (PF10-A) — artifacts/runtime/env\_connectivity.snapshot.json
``````

REPLACEMENT TEXT:

``````text
* Dev connectivity snapshot (HDE Build Notes) — artifacts/runtime/env\_connectivity.snapshot.json
``````

## Redline RL-133

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **5\) Quick reference: where code exchange is allowed**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [369473, 369527); starting original line: 4103.

OLD TEXT:

``````text
Epic Plan and CRD Plan. Propose/refine code-capsules.
``````

REPLACEMENT TEXT:

``````text
Epic Specification and CRD Specification. Propose/refine code-capsules.
``````

## Redline RL-134

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **5\) Quick reference: where code exchange is allowed**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [369528, 369763); starting original line: 4105.

OLD TEXT:

``````text
Implementation Plan (IP). Finalize the capsule list; package verbatim components/schemas for CodEx. After IP approval, capsules become immutable. CodEx may apply scoped fixes but must record every change in the Detailed Change Report.
``````

REPLACEMENT TEXT:

``````text
Implementation Plan (IP). Finalize the capsule list; package verbatim components/schemas for the executing agent. After IP approval, capsules become immutable. The executing agent may apply scoped fixes but must record every change in the Detailed Change Report.
``````

## Redline RL-135

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **5\) Quick reference: where code exchange is allowed**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [369764, 370002); starting original line: 4107.

OLD TEXT:

``````text
Build. IA provides instructions \+ verbatim materials. CodEx can read PF docs. Even so, paste execution-critical formats, schemas, stable requirement IDs, commands, and artifact paths verbatim to keep an unambiguous in-session reference.
``````

REPLACEMENT TEXT:

``````text
Build. IA provides instructions \+ verbatim materials. The Implementation Guide establishes actual executing-agent PF/input access. Even so, paste execution-critical formats, schemas, stable requirement IDs, commands, and artifact paths verbatim to keep an unambiguous in-session reference.
``````

## Redline RL-136

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **5\) Quick reference: where code exchange is allowed**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [370003, 370278); starting original line: 4109.

OLD TEXT:

``````text
Mutation. The normal code-bearing route is a CodEx-opened PR. The Product Owner MAY explicitly authorize direct-to-`main` mutation for the exact change. Agent direct-main permission MUST NOT be inferred. Record the exact candidate and repository identities for either route.
``````

REPLACEMENT TEXT:

``````text
Mutation. The normal code-bearing route is a PR opened by the executing agent. The Product Owner MAY explicitly authorize direct-to-`main` mutation for the exact change. Agent direct-main permission MUST NOT be inferred. Record the exact candidate and repository identities for either route.
``````

## Redline RL-137

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **5\) Quick reference: where code exchange is allowed**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [370538, 370706); starting original line: 4113.

OLD TEXT:

``````text
Escalation. PO may direct CodEx to inspect code or processes at any time. IA keeps docs and applicable evidence companions synchronized in the authorized mutation set.
``````

REPLACEMENT TEXT:

``````text
Escalation. PO may direct the executing agent to inspect code or processes at any time. IA keeps docs and applicable evidence companions synchronized in the authorized mutation set.
``````

## Redline RL-138

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [399641, 399705); starting original line: 4374.

OLD TEXT:

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
``````

REPLACEMENT TEXT:

``````text
# **Appendix A — Large Schemas & Assets (executing-agent capabilities)**
``````

## Redline RL-139

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Purpose**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [399722, 399991); starting original line: 4378.

OLD TEXT:

``````text
Define how to include large schemas or assets when content is too large to paste inline or when the workflow cannot rely on file attachments. This appendix preserves ownership, auditability, and single-home discipline while keeping execution mechanical and repeatable.
``````

REPLACEMENT TEXT:

``````text
Define how to include large schemas or assets when content is too large to paste inline or when the workflow cannot rely on file attachments. This appendix preserves ownership, auditability, and single-home discipline while keeping execution mechanical and repeatable.

The Implementation Guide establishes the actual executing agent’s repository, PF and attachment capabilities. The CodEx descriptions below are product-specific capability context, not a provider mandate or a universal limit. Self-contained execution-critical inline material and the Asset Draft Pack route remain required whenever the actual agent cannot reliably receive the required material.
``````

## Redline RL-140

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Constraints (facts)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [400568, 400661); starting original line: 4385.

OLD TEXT:

``````text
* CodEx may adapt within scope but must report every change in the Detailed Change Report.  
``````

REPLACEMENT TEXT:

``````text
* The executing agent may adapt within scope but must report every change in the Detailed Change Report.  
``````

## Redline RL-141

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Constraints (facts)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [400833, 401140); starting original line: 4387.

OLD TEXT:

``````text
* Single-PR parity. When assets are introduced or moved, update all `PF12-Canon-HDE-Schemas-and-Artifacts`\-required evidence ledgers, hash sentinels, mirrors, and path-proofs in the same PR. If the CodEx UI cannot include doc edits, the IA provides verbatim text in the same PR body for CodEx to commit.  
``````

REPLACEMENT TEXT:

``````text
* Single-PR parity. When assets are introduced or moved, update all `PF12-Canon-HDE-Schemas-and-Artifacts`\-required evidence ledgers, hash sentinels, mirrors, and path-proofs in the same PR. If the CodEx UI cannot include doc edits, the IA provides verbatim text in the same PR body for the executing agent to commit.  
``````

## Redline RL-142

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Roles & responsibilities**
### **Lead Dev / IA**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [401565, 401706); starting original line: 4396.

OLD TEXT:

``````text
* Ensure the CodEx-opened PR captures Evidence Index, hash sentinel, mirror updates, and single-home pointers. Avoid separate docs-only PRs.
``````

REPLACEMENT TEXT:

``````text
* Ensure the PR opened by the executing agent captures Evidence Index, hash sentinel, mirror updates, and single-home pointers. Avoid separate docs-only PRs.
``````

## Redline RL-143

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Roles & responsibilities**
### **Product Owner**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [401730, 401817); starting original line: 4400.

OLD TEXT:

``````text
* Load the Asset Draft Pack files into the CodEx PR branch at the specified targets.  
``````

REPLACEMENT TEXT:

``````text
* Load the Asset Draft Pack files into the PR branch used by the executing agent at the specified targets.  
``````

## Redline RL-144

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Roles & responsibilities**
### **Product Owner**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [401817, 401894); starting original line: 4401.

OLD TEXT:

``````text
* Confirm the CodEx-opened PR and, after Lead Dev gate passes, squash-merge.
``````

REPLACEMENT TEXT:

``````text
* Confirm the PR opened by the executing agent and, after Lead Dev gate passes, squash-merge.
``````

## Redline RL-145

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Roles & responsibilities**
### **CodEx**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [401895, 401909); starting original line: 4403.

OLD TEXT:

``````text
### **CodEx**
``````

REPLACEMENT TEXT:

``````text
### **Executing agent**
``````

## Redline RL-146

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **When to use an Asset Draft Pack**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [402342, 402486); starting original line: 4411.

OLD TEXT:

``````text
Use a pack when any required artifact cannot reasonably be pasted inline for CodEx (e.g., large JSON or YAML schemas, binaries, long fixtures).
``````

REPLACEMENT TEXT:

``````text
Use a pack when any required artifact cannot reasonably be pasted inline for the executing agent (e.g., large JSON or YAML schemas, binaries, long fixtures).
``````

## Redline RL-147

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Asset Draft Pack — minimal fields**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [402960, 403027); starting original line: 4428.

OLD TEXT:

``````text
notes: "Consumed by component X; CodEx will assume this location."
``````

REPLACEMENT TEXT:

``````text
notes: "Consumed by component X; the executing agent will assume this location."
``````

## Redline RL-148

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Flow (high level)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [403531, 403608); starting original line: 4440.

OLD TEXT:

``````text
* IA → CodEx: send inline materials; name target paths for large assets.  
``````

REPLACEMENT TEXT:

``````text
* IA → the executing agent: send inline materials; name target paths for large assets.  
``````

## Redline RL-149

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Flow (high level)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [403608, 403680); starting original line: 4441.

OLD TEXT:

``````text
* PO: load the Asset Pack at the target paths in the CodEx PR branch.  
``````

REPLACEMENT TEXT:

``````text
* PO: load the Asset Pack at the target paths in the PR branch used by the executing agent.  
``````

## Redline RL-150

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Flow (high level)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [403680, 403800); starting original line: 4442.

OLD TEXT:

``````text
* CodEx: build & test; if something is missing, switch to planning mode and note stubs in the Detailed Change Report.  
``````

REPLACEMENT TEXT:

``````text
* The executing agent: build & test; if something is missing, switch to planning mode and note stubs in the Detailed Change Report.  
``````

## Redline RL-151

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Flow (high level)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [403866, 403953); starting original line: 4444.

OLD TEXT:

``````text
* PO: confirm the CodEx-opened PR, then squash-merge after the Lead Dev gate passes.  
``````

REPLACEMENT TEXT:

``````text
* PO: confirm the PR opened by the executing agent, then squash-merge after the Lead Dev gate passes.  
``````

## Redline RL-152

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Planning mode (CodEx)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [404094, 404123); starting original line: 4447.

OLD TEXT:

``````text
## **Planning mode (CodEx)**
``````

REPLACEMENT TEXT:

``````text
## **Planning mode (the executing agent)**
``````

## Redline RL-153

Operation: REPLACE

Original heading path (each line is an exact authored heading):

``````text
# **Appendix A — Large Schemas & Assets (CodEx constraints)**
## **Acceptance and drift guards (exact-source; legacy tokens optional)**
``````

Expected literal occurrence: 1. Original UTF-8 byte span: [405228, 405337); starting original line: 4456.

OLD TEXT:

``````text
* No surprises: if an asset was not present at build time, CodEx records a stub; IA reconciles before close.
``````

REPLACEMENT TEXT:

``````text
* No surprises: if an asset was not present at build time, the executing agent records a stub; IA reconciles before close.
``````

END OF REDLINES
