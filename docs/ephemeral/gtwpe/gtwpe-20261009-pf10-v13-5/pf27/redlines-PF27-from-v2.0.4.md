# PF27 exact redlines from v2.0.4

Preparation outcome: READY  
Save outcome: COMPLETE_PACKAGE  
Prompt: TW-DRAIN-10 — 100926.1  
Run identity: T-PF27-20261009-pf10-v13-5-r1  
Originating preparer: /root, this Nathan-started T-PF27 ChatGPT Work document session  
Repository: amthorn78/glow-hdengine-v2  
Original: docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md at e7265a090ad0cc8de5f36de2f19481216aa3d073  
Original SHA-256 (exact UTF-8 Git blob bytes): aa4ac7201e83beb46d43be80999049edcb43a2d24798a8b51ca6c2cce67b5248  
Prepared content version: baseline v2.0.4; Apply derives v2.0.5  
Source justifying changes: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md  
Ledger: docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md at f057d124176143b3e02ba7ad599880fd7e9991b1; assigned row T-PF27

The separate preparation proof log records the complete selected-source boundaries, protected lineage, dispositions and validation. All operations resolve independently against the unchanged original. Document-control fields are reserved for TW-APPLY-10. Every OLD and NEW payload below includes its displayed final LF; closing fences are delimiters, not payload. Exact source backslashes and meaningful whitespace are literal. Byte spans are half-open UTF-8 offsets and corroborate the exact locators; they are not line-number-only instructions.

## RL-001

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [972, 990); original lines 32–32  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Governed artifacts**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* HDE-EPIC-Plan  
````

NEW:

````text
* HDE-EPIC-Specification  
````

## RL-002

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [990, 1040); original lines 33–33  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Governed artifacts**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* HDE-CRD-Plan Profile and PF30 Record Contract  
````

NEW:

````text
* HDE-CRD-Specification Profile and PF30 Record Contract  
````

## RL-003

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [3201, 3325); original lines 68–68  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Artifact execution boundary**
````

Reason: State permanence-based format ownership without changing protected historical Specifications or creating a schema.

OLD:

````text
PF27 defines where and how a derived artifact records project-specific content. It does not supply that content by default.
````

NEW:

````text
PF27 defines where and how a derived artifact records project-specific content. It does not supply that content by default.

Epic and CRD Specifications are permanent governed records. The normative HDE Epic record template in this document owns Epic Specification format; the CRD record contract and record template in the active HDE-CRD-Records volume own CRD Specification format. A Specification delta follows the canon governing its base Specification. A kickoff is transient scaffolding and an Implementation Plan is working direction; their producing prompts may state their shape. Neither a prompt-defined thirteen-section Specification nor a retired `glow-specification`, `glow-kickoff`, or other `glow-<kind>/<version>` artifact-schema identifier supplies a permanent Specification format.
````

## RL-004

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [3326, 3497); original lines 70–70  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Artifact execution boundary**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Epic Plans and initial Implementation Plans define intended work, boundaries, dependencies, and proof obligations. They MUST NOT become step-by-step Live QA runbooks.  
````

NEW:

````text
* Epic Specifications and initial Implementation Plans define intended work, boundaries, dependencies, and proof obligations. They MUST NOT become step-by-step Live QA runbooks.  
````

## RL-005

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [4034, 4228); original lines 74–74  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Artifact execution boundary**
````

Reason: Remove the blanket agent bar only for task-specific directed vendor execution; preserve the principal, lane and evidence boundaries.

OLD:

````text
* OPS templates describe authorized, bounded external work. They MUST keep PO-only actions separate from repository work and MUST NOT assign privileged external execution to automated agents.  
````

NEW:

````text
* OPS templates describe authorized, bounded external work. They MUST keep privileged external work separate from repository work. For an identified live vendor task, the Product Owner is the authorizing and accountable principal and may direct an automated session agent to execute and produce evidence under the same task controls. The agent is not an independent approver; this creates no standing vendor authority. Other privileged actions retain their applicable authorization boundaries.  
````

## RL-006

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [6966, 7142); original lines 107–107  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Exact technical facts and secret safety**
````

Reason: Make canonical/compatibility selection and conflict refusal explicit without requiring migration or inventing environment values.

OLD:

````text
| Base URL key | Use `HD_API_BASE_URL`. Use `HDAPI_BASE_URL` only when explicitly identified as deprecated drift, observed legacy state, or temporary compatibility notation. |
````

NEW:

````text
| Base URL key | The product reads `HD_API_BASE_URL`, or the compatibility alias `HDAPI_BASE_URL` only when `HD_API_BASE_URL` is absent. Conflicting values fail closed. The base URL is configuration, not an API key. Do not remove the environment's only base URL as part of a rails change. |
````

## RL-007

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [7784, 7938); original lines 111–111  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Exact technical facts and secret safety**
````

Reason: Carry the two-key requirement into the reusable configuration fields.

OLD:

````text
| Secret keys | Preserve `HD_API_KEY` and `GEO_API_KEY` when those keys are in scope. Keep environment secret keys distinct from outbound header names. |
````

NEW:

````text
| Secret keys | A live HD Engine vendor call requires both `HD_API_KEY` and `GEO_API_KEY` in the execution environment, in addition to the base URL. Keep environment secret keys distinct from outbound header names. |
````

## RL-008

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [8207, 8340); original lines 113–113  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Exact technical facts and secret safety**
````

Reason: Distinguish environment inheritance from secret disclosure and manual secret entry.

OLD:

````text
| Secret handling | Do not record raw secrets, bearer tokens, API keys, private payload bodies, or unredacted credential material. |
````

NEW:

````text
| Secret handling | Use environment-held vendor configuration in the product process. Record presence only (`SET` or `UNSET`); do not print, log, store, commit, transmit, or put values on process argument lists. Do not require the Product Owner to type, paste, or re-enter vendor values. Scan captured output before it enters evidence. Raw secrets, bearer tokens, API keys, private payload bodies, and unredacted credential material remain forbidden. |
````

## RL-009

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [8341, 8578); original lines 115–115  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Exact technical facts and secret safety**
````

Reason: Retain discovery routing while making the vendor missing-configuration stop and classification explicit.

OLD:

````text
If an exact configuration or environment fact is unknown but safely discoverable, the plan MUST route bounded discovery or an authorized OPS change. It MUST NOT invent, silently normalize, or defer the fact solely because it is unknown.
````

NEW:

````text
If an exact configuration or environment fact is unknown but safely discoverable, the plan MUST route bounded discovery or an authorized OPS change. It MUST NOT invent, silently normalize, or defer the fact solely because it is unknown.

When required vendor configuration is absent, no vendor call runs. Record only the missing variable names and their `UNSET` presence posture; an affected step that has begun is `TOOLING_BLOCKED`. Do not substitute manual vendor-value entry or guess a value.
````

## RL-010

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CLARIFY  
Original UTF-8 span: [9033, 9178); original lines 126–126  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Repository loci and file minting**
````

Reason: Preserve the exact vocabulary value while giving its functional, provider-neutral meaning.

OLD:

````text
| Observed Evidence (Codex Audit) | Embed a short quote or precise observation and bound the claim to the repository state actually inspected. |
````

NEW:

````text
| Observed Evidence (Codex Audit) | Embed a short quote or precise observation from the read-only repository audit, whichever agent produced it, and bound the claim to the repository state actually inspected. |
````

## RL-011

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [9935, 10113); original lines 133–133  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Repository loci and file minting**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* A Codex-facing prompt MAY include embedded observed repository context, but it MUST direct Codex to verify current repository reality before editing or relying on the locus.  
````

NEW:

````text
* A prompt for the executing agent MAY include embedded observed repository context, but it MUST direct the executing agent to verify current repository reality before editing or relying on the locus.  
````

## RL-012

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [24264, 24335); original lines 278–278  
Basis / selected source ledger: A29, A30

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Canon precedence for template use**
````

Reason: Provide repository authority, bounded consultation and derived storage/citation posture without new evidence homes or a non-PF operating-procedure destination.

OLD:

````text
Every template and derived artifact MUST include this precedence rule:
````

NEW:

````text
Current authoritative PF Markdown is the repository's `docs/pfcanon/` on `main`. Before authoring a derived artifact, search PF-Canon for the subject, identify and read the owning current sources, and consult applicable in-flight approved Specifications, Implementation Plans, reviews and Product Owner dispositions. Record the actual repository source state used; do not treat a version-looking filename or an old attachment as current authority.

Change-process documents derived from these templates belong under `docs/ephemeral/` and its established subdirectories. Notion is navigation and board context, and Google Drive and ChatGPT Library are not PF authority or change-process document destinations. This storage rule does not relocate governed QA, Ops, audit or evidence families, alter their writers, or migrate historical records. Placement of non-PF operating procedures remains separately undecided.

Cite HDE Build Notes by title alone in current PF prose and derived references, without an internal addendum number, heading, section or file-version locator. Other PF references use their current title and applicable section. Preserve actual file identities and historical citations in source-use inventories and evidence provenance.

Every template and derived artifact MUST include this precedence rule:
````

## RL-013

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [24613, 24860); original lines 282–282  
Basis / selected source ledger: A08

Location — complete authored original heading path:

````text
# **0\) Document Control**
## **Purpose & scope \[Required−Now\]**
### **Canon precedence for template use**
````

Reason: Carry the established addendum form into template use; create no addendum, publishing duty or gate.

OLD:

````text
When a derived artifact relies on a formally approved bounded Product Owner rescope, it MUST identify the exact approved decision, any work transferred to a later PR, the preserved boundaries, the preserved nonclaims, and the PF drain candidates.
````

NEW:

````text
When a derived artifact relies on a formally approved bounded Product Owner rescope, it MUST identify the exact approved decision, any work transferred to a later PR, the preserved boundaries, the preserved nonclaims, and the PF drain candidates.

When a derived artifact includes an agent-authored HDE Build Notes addendum, the addendum uses the next continuous numbered H2 heading with a descriptive title and H3-or-deeper children. It is page-ready, self-contained canonical subject matter: decisions, status, evidence, scope, nonclaims, dependencies and consequences. Completed work, future work, recommendations and unproven facts remain distinct; role-addressed handling, publication, routing and record-maintenance instructions do not belong in the addendum.
````

## RL-014

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [26387, 26457); original lines 313–313  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Front matter**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) Codex
````

NEW:

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) executing agent
````

## RL-015

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [27075, 27157); original lines 323–323  
Basis / selected source ledger: A30

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Front matter**
#### **Canon set (explicit; stable references only)**
````

Reason: Remove the requirement for internal addendum numbers and titles in the Canon set.

OLD:

````text
* PF10 — HDE-Build Notes (relevant addenda: list addendum numbers and titles)  
````

NEW:

````text
* HDE Build Notes  
````

## RL-016

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [28169, 30522); original lines 350–376  
Basis / selected source ledger: A33, A34, A30, A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Open-Rails Live QA Requirement for production-affecting epics**
````

Reason: Conform the named superseded exemption/step alternatives only for A33 production-functional scope; retain broader outside-scope controls, directed executor fields and title-only citations.

OLD:

````text
### **Open-Rails Live QA Requirement for production-affecting epics**

A Live QA Plan for a production-affecting epic MUST include at least one bounded open-rails live QA step, or an explicit authorized exemption.

Production-affecting scope includes work that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence, database retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret-binding behavior, request shaping, response mapping, authentication or authorization behavior, public Reader behavior, CLI/API behavior used in production, queues, workers, jobs, schedulers, runtime services, or any path that must work outside isolated closed-rails fixtures.

The required open-rails live QA step MUST identify:

* the production-relevant behavior being proved,  
* the live target or PO-approved live target,  
* the rails posture,  
* the secret-safety posture,  
* the evidence to capture,  
* what the live step proves,  
* what the live step does not prove.

Closed-rails tests, fixture replay, static analysis, generated evidence, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, Codex audit, PF10 supportability notes, implementation review approval, QA Plan approval, unrun smoke procedures, and OPS discovery without live behavior proof do not satisfy this requirement by themselves.

The open-rails live QA step must be bounded, non-destructive unless explicitly approved, PO-authorized where secrets, external services, or deployed environments are involved, secret-safe, evidence-recorded, scoped to the epic’s actual production risk, and explicit about proof limits.

A Live QA Plan may omit open-rails live QA only with explicit exemption language. The exemption MUST state why open-rails live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release.

A reviewer MUST NOT approve a closed-rails-only Live QA Plan for a production-affecting epic unless the plan includes explicit authorized exemption language.

List each as:

* PF10 Addendum \\\<\#\> — → what it changes for this runbook → impacted PF references
````

NEW:

````text
### **Open-Rails Live QA Requirement for production-affecting epics**

Every QA Plan for an epic touching any surface used to produce a production feature described as functional in PF-Canon MUST include a bounded open-rails test that is a live vendor call using synthetic data only. The test uses `SAFE_MODE=0` and `ALLOW_NETWORK=1`. A plan within this production-functional scope without that test is not approval-ready; no exemption is established for that scope.

Production-affecting scope includes work that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence, database retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret-binding behavior, request shaping, response mapping, authentication or authorization behavior, public Reader behavior, CLI/API behavior used in production, queues, workers, jobs, schedulers, runtime services, or any path that must work outside isolated closed-rails fixtures. The epic's Specification and plans identify which affected surfaces produce a feature stated as functional in PF-Canon.

The required live vendor test MUST identify:

* the production-functional surface and behavior being proved,  
* the live vendor target and task-specific Product Owner direction or authorization,  
* the executing operator or directed agent; the Product Owner remains the authorizing and accountable principal,  
* synthetic inputs only; no real person, user or production data,  
* the step-scoped rails pair `SAFE_MODE=0`, `ALLOW_NETWORK=1` and restoration of the default rails immediately afterward,  
* the required environment-held vendor configuration and presence-only, secret-safe preflight,  
* the existing request limit, stop checks, redaction, secret scan and quarantine controls,  
* the evidence to capture under the existing evidence contract,  
* what the live test proves and what it does not prove.

Closed-rails tests, fixture replay, mocks or fake services, static analysis, generated or governed evidence, path-proof validation, Index or Mirror refresh, acceptance-map refresh, repository inspection, read-only repository audit, supportability notes, review approval, an unrun smoke procedure, and OPS discovery without a live vendor call do not satisfy this requirement. A non-vendor live step, including a deployed-service check or database read, does not satisfy it by itself.

The test is bounded, non-destructive unless explicitly approved, secret-safe, evidence-recorded and scoped to the epic's actual production risk. It does not authorize load, stress or volume testing or raise a request limit. A passing test establishes only the exercised behavior, not full vendor conformance, whole-change QA PASS, acceptance, PF09 status movement, deployment or epic closure. Open-rails Ops evidence remains Ops evidence; this template does not convert it into QA evidence.

For a production-affecting epic outside the production-functional scope above, the existing requirement for a bounded open-rails live QA step or an explicit authorized exemption remains. Any such exemption records why the step is omitted, who authorized the omission, the production claim not made, and whether a later step is required before closeout or release. It cannot substitute for the mandatory live vendor test within the production-functional scope. A reviewer MUST NOT approve a closed-rails-only plan within that scope on exemption language.

List each applicable live-truth override or conflict as:

* HDE Build Notes → what it changes for this runbook → impacted PF references
````

## RL-017

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CLARIFY  
Original UTF-8 span: [32519, 32770); original lines 423–423  
Basis / selected source ledger: A32 / C040-09

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Environment and rails posture**
#### **Rails posture (explicit)**
````

Reason: State the approved read-only attribution meaning; preserve independently owned exact-source evidence obligations.

OLD:

````text
A plan MAY include read-only repository-identity capture when needed to bind execution evidence to the tested source. The governed execution or review record MUST identify the exact repository and candidate SHA for any QA verdict or acceptance claim.
````

NEW:

````text
A plan MAY include read-only `git` observations for tested-source attribution. They do not authorize a VCS mutation and are never a product-behavior PASS gate. The governed execution or review record MUST identify the exact repository and candidate SHA for any QA verdict or acceptance claim under the applicable evidence contract.
````

## RL-018

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [34618, 34712); original lines 451–451  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **PO inputs needed**
````

Reason: Make the existing PO-input field environment-based for vendor calls without changing unrelated external inputs.

OLD:

````text
List all required external inputs by name only (never store secret values in plan artifacts).
````

NEW:

````text
List all required external inputs by name only (never store secret values in plan artifacts). For HD Engine vendor calls, use `HD_API_KEY`, `GEO_API_KEY` and the base URL already held in the execution environment: `HD_API_BASE_URL`, or `HDAPI_BASE_URL` only when the canonical key is absent, with conflicts rejected. Record `SET` or `UNSET` presence only. Do not request manual entry of vendor values.
````

## RL-019

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [58449, 58608); original lines 688–688  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Runbook Check Matrix**
````

Reason: Conform the matrix executor column with directed vendor execution.

OLD:

````text
| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
````

NEW:

````text
| check\_id | check\_name | D-goal | rails posture | commands (authorized executor) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
````

## RL-020

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [61826, 62717); original lines 720–727  
Basis / selected source ledger: A32 / C040-09, A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Check Blocks**
#### **Embedded harness checks (pattern; use when no standalone script exists)**
````

Reason: Keep the changed approval narrower than the rejected historical proposal: tracked tested API invocation and attribution only, no runtime evaluator minting.

OLD:

````text
#### **Embedded harness checks (pattern; use when no standalone script exists)**

Use this pattern when a check is executed by invoking an existing harness runner that performs the check internally (no dedicated script exists for the check).

* In the matrix row, set **commands (PO-only)** to the exact `python (embedded)` invocation you will run (include the harness runner repo path).  
* In the CHECK block, record the same `python (embedded)` invocation under **PO command(s)**.  
* vidence outputs MUST still be concrete, governed paths. Include the check `primary.log` plus every check-specific governed output produced by the embedded harness.  
* If the Approved Plan named a runner script or auxiliary artifact that does not exist or is not produced, record it as `DOC_DRIFT` in Step-0B (Doc Delta Capture) and proceed only if the governed evidence outputs exist and are verified.
````

NEW:

````text
#### **Embedded harness checks (pattern; use when no standalone script exists)**

Use this pattern only to invoke an existing tracked, reviewed, tested repository harness entrypoint that performs the check internally. The bounded `python -c` use of tracked harness APIs, such as `tools.qa.qa_harness` and its `_refresh_path_proof` API in the approved harness lineage, creates no script file and no new decisive evaluator at run time. Resolve the actual entrypoint and invocation from the repository before use; the example is not command discovery or proof of current runnability.

* In the matrix row, record the exact tracked harness invocation under **commands (authorized executor)**.  
* In the CHECK block, record the same invocation under **Executor command(s) (PO-authorized)**.  
* Evidence outputs MUST still be concrete, governed paths. Include the check `primary.log` plus every check-specific governed output produced by the harness.  
* If the Approved Plan named a runner script or auxiliary artifact that does not exist or is not produced, record it as `DOC_DRIFT` in Step-0B (Doc Delta Capture) and proceed only if the governed evidence outputs exist and are verified.  
* This pattern does not authorize a newly written decisive evaluator, invented runner or substitute repository tooling. Those remain governed by Glow QA Guide, **Rails posture for manual Live QA**, including its tracked-entrypoint and remediation boundaries. QA-only evidence assembly or ephemeral glue does not gain decisive-evaluator authority from this pattern.
````

## RL-021

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [63058, 63420); original lines 737–737  
Basis / selected source ledger: A30

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Check Blocks**
#### **Canon check clarifications (routed)**
````

Reason: Remove the conflicting numbered-addendum citation instruction.

OLD:

````text
* **Owning source and exact locator:** select the applicable current in-document title and anchor from `PF02-Canon-HDE-Architecture`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF12-Canon-HDE-Schemas-and-Artifacts`, or `PF19-Canon-Glow-QA-Guide`; cite an active PF10 numbered addendum only when it explicitly addresses the exact topic.  
````

NEW:

````text
* **Owning source and exact locator:** select the applicable current in-document title and anchor from `PF02-Canon-HDE-Architecture`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF12-Canon-HDE-Schemas-and-Artifacts`, or `PF19-Canon-Glow-QA-Guide`; cite HDE Build Notes by title alone only when it explicitly addresses the exact topic.  
````

## RL-022

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [64469, 65580); original lines 753–758  
Basis / selected source ledger: A33, A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Check Blocks**
#### **CHECK \\: \\**
````

Reason: Record both open rails and environment preflight; remove offline substitution for the mandatory vendor test while retaining offline proof classes.

OLD:

````text
Vendor-dependent steps (rails-scoped):

* If the step requires vendor IO (example: `showcompat` when the required BodyGraph bytes are not already locally available), set rails for this step only (typically `ALLOW_NETWORK=1`) and restore the default rails posture immediately after the step.  
* Rails posture mismatch is a plan defect: if the plan declares SAFE rails for this step (example: `ALLOW_NETWORK=0`) but execution requires network or vendor IO in practice, the plan MUST be corrected before declaring it stable. The plan MUST either (a) scope the step to allow network for this step (example: `ALLOW_NETWORK=1`), or (b) provide an offline proof mode that can execute with `ALLOW_NETWORK=0`.  
* `showcompat` MUST NOT be executed as a zero-argument command. The invocation MUST supply the required argument set defined by HDE-CLI-API-Vendor-Ref.  
* If an `showcompat` attempt fails only because rails were closed or required args were missing, classify this step as `FAIL_TOOLING`or `TOOLING_BLOCKED`(not `FAIL_BEHAVIOR`) and record the rails posture used plus the failure signature in the step log.
````

NEW:

````text
Vendor-dependent steps (rails-scoped):

* A live vendor call uses `SAFE_MODE=0` and `ALLOW_NETWORK=1` for that step only, and restores the default rails posture immediately afterward. Do not remove the only environment-held base URL while setting rails.  
* Preflight the required environment configuration by presence only: `HD_API_KEY`, `GEO_API_KEY` and a base URL resolved from `HD_API_BASE_URL`, or `HDAPI_BASE_URL` only when the canonical key is absent. Conflicting base URLs fail closed. Use configuration from the environment; no manual re-entry or secret-bearing arguments. Missing required configuration means no vendor call and `TOOLING_BLOCKED` for a begun step.  
* Rails mismatch is a plan defect. Correct the vendor step's rails before execution. An offline proof mode may prove only its stated offline claim; it cannot replace the mandatory live vendor test for a production-functional surface.  
* `showcompat` MUST NOT be executed as a zero-argument command. The invocation MUST supply the required argument set defined by HDE-CLI-API-Vendor-Ref.  
* If a `showcompat` attempt fails only because rails were closed or required args were missing, classify this step as `FAIL_TOOLING` or `TOOLING_BLOCKED` (not `FAIL_BEHAVIOR`) and record the rails posture used plus the failure signature in the step log.
````

## RL-023

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [66997, 67302); original lines 766–766  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Check Blocks**
#### **CHECK \\: \\**
````

Reason: Conform the named PO-only vendor-smoke passage without extending permission to other external work.

OLD:

````text
* Controlled vendor or external smoke steps are PO-only and IA-guided. They may run only after the plan proves exact command, approved target classification or explicit PF07-gap blocker posture, safe secret posture, no-user or other required input shape, and explicit vendor or external source posture.  
````

NEW:

````text
* Controlled live vendor smoke steps are PO-authorized and IA-guided. A task-specific directed agent may execute unchanged proven commands and produce evidence; the PO remains the authorizing and accountable principal. Other external smoke steps retain their applicable authorization boundaries. Execution may begin only after the plan proves exact command, approved target classification or explicit PF07-gap blocker posture, safe secret posture, no-user or other required input shape, and explicit vendor or external source posture.  
````

## RL-024

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [68896, 68941); original lines 784–784  
Basis / selected source ledger: A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **1\) Live QA Plan**
### **Check Blocks**
#### **CHECK \\: \\**
````

Reason: Separate executor from accountable PO in the command field.

OLD:

````text
**PO command(s) (minimal; objective-first)**
````

NEW:

````text
**Executor command(s) (PO-authorized; minimal; objective-first)**
````

## RL-025

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [93969, 94616); original lines 1023–1023  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* PF09 task accountability for task-like items (required). Epic Plans, Implementation Plans, QA Plans, remediation plans, QA-readiness reviews, retrospectives, closure reviews, and future-work sections MUST NOT create free-floating task-like backlog. Every task-like item affecting implementation, QA, OPS, runtime, evidence, vendor behavior, architecture, product behavior, build improvements, adapter gaps, runtime gaps, QA-discovered gaps, OPS-discovered gaps, or post-epic recommendations MUST resolve to exactly one of: exact phased PF09 task/subtask mapping, PF09 gap, out of HDE phased build scope, or documentation/status drainage only.  
````

NEW:

````text
* PF09 task accountability for task-like items (required). Epic Specifications, Implementation Plans, QA Plans, remediation plans, QA-readiness reviews, retrospectives, closure reviews, and future-work sections MUST NOT create free-floating task-like backlog. Every task-like item affecting implementation, QA, OPS, runtime, evidence, vendor behavior, architecture, product behavior, build improvements, adapter gaps, runtime gaps, QA-discovered gaps, OPS-discovered gaps, or post-epic recommendations MUST resolve to exactly one of: exact phased PF09 task/subtask mapping, PF09 gap, out of HDE phased build scope, or documentation/status drainage only.  
````

## RL-026

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [98619, 99038); original lines 1033–1033  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* PF10 reopened-subtask planning rule (required). When current PF10 explicitly reopens, rebinds, or names active HDE Build Checklist subtasks for an epic, Epic Plans, QA Plans, remediation guides, and reviews MUST treat the exact subtask IDs as active scope unless a later PF10 addendum reverses that posture. Broader parent-task history-only wording MUST NOT suppress an exact subtask row that PF10 names as active.  
````

NEW:

````text
* PF10 reopened-subtask planning rule (required). When current PF10 explicitly reopens, rebinds, or names active HDE Build Checklist subtasks for an epic, Epic Specifications, QA Plans, remediation guides, and reviews MUST treat the exact subtask IDs as active scope unless a later PF10 addendum reverses that posture. Broader parent-task history-only wording MUST NOT suppress an exact subtask row that PF10 names as active.  
````

## RL-027

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [118765, 118859); original lines 1113–1113  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
Materiality-based blocker discipline (required for Epic Plan and Implementation Plan review):
````

NEW:

````text
Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review):
````

## RL-028

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [118860, 119594); original lines 1115–1115  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* A planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table formatting, heading style, punctuation, spacing, bold markers, presentation style, inventory-row ordering, template-perfect phrasing, missing non-decisive locator precision, missing titles-only polish, or an Epic QA root omission in an Epic Plan that does not authorize QA execution, unless the defect materially changes truth, proof, acceptance, execution safety, source authority, portability, implementation scope, PF09.x completion mapping, evidence identity, evidence trust, OPS/PR boundary, public/private surface posture, canon conflict handling, or closeout truth.  
````

NEW:

````text
* A planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table formatting, heading style, punctuation, spacing, bold markers, presentation style, inventory-row ordering, template-perfect phrasing, missing non-decisive locator precision, missing titles-only polish, or an Epic QA root omission in an Epic Specification that does not authorize QA execution, unless the defect materially changes truth, proof, acceptance, execution safety, source authority, portability, implementation scope, PF09.x completion mapping, evidence identity, evidence trust, OPS/PR boundary, public/private surface posture, canon conflict handling, or closeout truth.  
````

## RL-029

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [119897, 120424); original lines 1117–1117  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Valid blocker framing must state the material harm, such as conflict with active PF10, an unresolved ADR after PF10 resolves the exact topic, a required external CA/audit/non-PF source for Codex execution, unregistered token claimed as an acceptance token, Already Implemented claimed without embedded proof, OPS work required inside Codex PR work, unproven repo locus, public surface expansion without canon support, PF23 used as deliverable/token/blocker/acceptance authority, or PF20 used as current planning authority.  
````

NEW:

````text
* Valid blocker framing must state the material harm, such as conflict with active PF10, an unresolved ADR after PF10 resolves the exact topic, a required external CA/audit/non-PF source for execution by the agent, unregistered token claimed as an acceptance token, Already Implemented claimed without embedded proof, OPS work required inside repository PR work, unproven repo locus, public surface expansion without canon support, PF23 used as deliverable/token/blocker/acceptance authority, or PF20 used as current planning authority.  
````

## RL-030

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [126530, 127033); original lines 1139–1139  
Basis / selected source ledger: A14, A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes. Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, closure-review artifacts, and related approval artifacts MUST NOT be blocked, rejected, returned for revision, or classified as REVISE AND RESUBMIT solely because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written.  
````

NEW:

````text
* QA Plans, Epic Specifications, Implementation Plans, remediation plans, review prompts, redline prompts, prompts for the executing agent, closure-review artifacts, and related approval artifacts MUST NOT be blocked, rejected, returned for revision, or classified as REVISE AND RESUBMIT solely because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written.  
````

## RL-031

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [128125, 128625); original lines 1142–1142  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Syntax correction is ordinary execution hygiene. During execution, a QA operator, Codex, Kronos, PO, or implementation owner may normalize a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue in flight when the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture are preserved.  
````

NEW:

````text
* Syntax correction is ordinary execution hygiene. During execution, a QA operator, the executing agent, Kronos, PO, or implementation owner may normalize a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue in flight when the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture are preserved.  
````

## RL-032

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [128857, 129715); original lines 1144–1144  
Basis / selected source ledger: A38, A34

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Valid plan approval blockers are limited to material truth, proof, scope, authority, safety, acceptance, phase, evidence-identity, or canon-conflict defects. Examples include missing proof obligation, missing in-scope PF09.x mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement inside closed rails, secret exposure requirement, OPS work assigned to Codex, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, missing acceptance-decisive deliverable category, unclear PASS/FAIL or verdict posture, unresolved phase boundary conflict, unresolved canon contradiction, or an evidence identity gap where the proof target cannot be distinguished.  
````

NEW:

````text
* Valid plan approval blockers are limited to material truth, proof, scope, authority, safety, acceptance, phase, evidence-identity, or canon-conflict defects. Examples include missing proof obligation, missing in-scope PF09.x mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement inside closed rails, secret exposure requirement, OPS work assigned to an executing agent without task-specific PO authorization, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, missing acceptance-decisive deliverable category, unclear PASS/FAIL or verdict posture, unresolved phase boundary conflict, unresolved canon contradiction, or an evidence identity gap where the proof target cannot be distinguished.  
````

## RL-033

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [131588, 132214); original lines 1156–1156  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Future plan-review, QA Plan review, implementation-plan review, remediation-plan review, redline-generation, QA-readiness review, closure-review, and Codex-audit prompts should include this guard: plan commands, snippets, helper code, heredocs, shell lines, and examples do not need to be paste-ready or literal. Syntax defects, escape characters, markdown rendering artifacts, indentation issues, and command exactness must never block plan approval. Treat them only as in-flight normalization unless they reveal a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, or evidence-identity defect.
````

NEW:

````text
* Future plan-review, QA Plan review, implementation-plan review, remediation-plan review, redline-generation, QA-readiness review, closure-review, and prompts for read-only repository audits should include this guard: plan commands, snippets, helper code, heredocs, shell lines, and examples do not need to be paste-ready or literal. Syntax defects, escape characters, markdown rendering artifacts, indentation issues, and command exactness must never block plan approval. Treat them only as in-flight normalization unless they reveal a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, or evidence-identity defect.
````

## RL-034

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [135688, 136669); original lines 1173–1173  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Rendered escape artifacts in source-facing work are categorically non-blocking (required). A plan, guide, QA plan, Live QA Plan, implementation plan, remediation guide, Codex prompt, review artifact, redline pass, PF10 addendum draft, PF-facing artifact, or acceptance artifact MUST NOT be blocked because assistant-rendered, Markdown-rendered, transcript-formatted, quote-formatted, preview-pane, copied-chat, or review-prose output shows escape characters in otherwise clear machine-sensitive strings. This applies to repo paths, artifact paths, evidence paths, command names, command arguments, shell redirection markers, heredoc markers, module names, endpoint paths, route strings, token names, environment variable names, config keys, JSON keys, artifact keys, PF09 task IDs or subtask IDs, ADR IDs, headings used as locators, evidence filenames, manifest filenames, path-proof filenames, hash filenames, quoted source lines, plan snippets, and QA-created script bodies.  
````

NEW:

````text
* Rendered escape artifacts in source-facing work are categorically non-blocking (required). A plan, guide, QA plan, Live QA Plan, implementation plan, remediation guide, prompt for the executing agent, review artifact, redline pass, PF10 addendum draft, PF-facing artifact, or acceptance artifact MUST NOT be blocked because assistant-rendered, Markdown-rendered, transcript-formatted, quote-formatted, preview-pane, copied-chat, or review-prose output shows escape characters in otherwise clear machine-sensitive strings. This applies to repo paths, artifact paths, evidence paths, command names, command arguments, shell redirection markers, heredoc markers, module names, endpoint paths, route strings, token names, environment variable names, config keys, JSON keys, artifact keys, PF09 task IDs or subtask IDs, ADR IDs, headings used as locators, evidence filenames, manifest filenames, path-proof filenames, hash filenames, quoted source lines, plan snippets, and QA-created script bodies.  
````

## RL-035

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [137812, 138210); original lines 1176–1176  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Codex prompt posture (required). Codex prompts MUST treat escaped display text as non-authoritative unless it is inside a raw source file Codex opens. A prompt MUST NOT instruct Codex to create, check, rename, implement, remediate, or fix escaped paths or filenames derived from assistant rendering unless raw source contains the escape and the approved plan explicitly directs the correction.  
````

NEW:

````text
* Prompt posture for the executing agent (required). Prompts for the executing agent MUST treat escaped display text as non-authoritative unless it is inside a raw source file the executing agent opens. A prompt MUST NOT instruct the executing agent to create, check, rename, implement, remediate, or fix escaped paths or filenames derived from assistant rendering unless raw source contains the escape and the approved plan explicitly directs the correction.  
````

## RL-036

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [139008, 139440); original lines 1178–1178  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Hard blockers for plan approval/execution**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Current-loop and future-prompt posture (required). Any existing blocker based solely on rendered escape characters is invalid unless re-proven from raw/source artifact text. Future review, redline, plan-revision, QA-review, remediation-review, and Codex-audit prompts should include a rendering-artifact guard that tells reviewers to ignore display-layer escapes unless raw/source inspection proves a substantive source defect.  
````

NEW:

````text
* Current-loop and future-prompt posture (required). Any existing blocker based solely on rendered escape characters is invalid unless re-proven from raw/source artifact text. Future review, redline, plan-revision, QA-review, remediation-review, and prompts for read-only repository audits should include a rendering-artifact guard that tells reviewers to ignore display-layer escapes unless raw/source inspection proves a substantive source defect.  
````

## RL-037

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [142756, 143050); original lines 1202–1202  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **Materiality-based blocker discipline for planning and review artifacts**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
For an Epic Plan that is not complete and makes no closeout claim, `Date completed: Not completed; no closeout claim is made` is approval-equivalent to `Date completed: [INTENTIONALLY LEFT BLANK]`. This equivalence does not authorize an incomplete or non-date value after the epic is complete.
````

NEW:

````text
For an Epic Specification that is not complete and makes no closeout claim, `Date completed: Not completed; no closeout claim is made` is approval-equivalent to `Date completed: [INTENTIONALLY LEFT BLANK]`. This equivalence does not authorize an incomplete or non-date value after the epic is complete.
````

## RL-038

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [157818, 157976); original lines 1331–1331  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **Review guardrails**
### **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation**
#### **Review stability and no-moving-target discipline (required for diff-first approval loops)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
Applies to Epic Plans, Implementation Plans, Live QA Plans, remediation plans, closeout reviews, and other diff-first approval loops that use PF27 templates.
````

NEW:

````text
Applies to Epic Specifications, Implementation Plans, Live QA Plans, remediation plans, closeout reviews, and other diff-first approval loops that use PF27 templates.
````

## RL-039

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [160373, 160398); original lines 1346–1346  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
## **2\) HDE-EPIC-Plan**
````

NEW:

````text
## **2\) HDE-EPIC-Specification**
````

## RL-040

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [160399, 160498); original lines 1348–1348  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
````

Reason: Name the permanent record and preserve the separate implementation/QA artifact classes.

OLD:

````text
This section defines the **Epic Plan** template used for in-flight planning and close preparation.
````

NEW:

````text
This section defines the **Epic Specification** as the permanent governed Epic record, using the normative template below. It captures intended scope and proof obligations for in-flight work and supported outcomes for close preparation. An Implementation Plan remains separate working direction; the Specification is not a Plan or a Live QA runbook.
````

## RL-041

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [160869, 161045); original lines 1358–1358  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
For every epic, fill out the following fields as the **Epic Plan record**. At epic close, the final Epic Plan record is archived into HDE-Phased Epics as the historical entry.
````

NEW:

````text
For every epic, fill out the following fields as the **Epic Specification record**. At epic close, the final Epic Specification record is archived into HDE-Phased Epics as the historical entry.
````

## RL-042

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [162321, 162481); original lines 1384–1384  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Business Case (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Plan.
````

NEW:

````text
* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Specification.
````

## RL-043

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [162681, 162908); original lines 1392–1392  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Contract and Compatibility Posture (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
Every Epic Plan MUST include this section. If there are no contract changes, no new surfaces, and no new flags, explicitly state that posture (for example: "No change" or "None") and still complete the backward-compat posture.
````

NEW:

````text
Every Epic Specification MUST include this section. If there are no contract changes, no new surfaces, and no new flags, explicitly state that posture (for example: "No change" or "None") and still complete the backward-compat posture.
````

## RL-044

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [163624, 165251); original lines 1402–1405  
Basis / selected source ledger: A33, A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Contract and Compatibility Posture (MUST)**
````

Reason: Keep Specification-level vendor declarations and downstream preservation aligned with the exact mandatory scope; do not add a QA execution stage to the Specification.

OLD:

````text
* **Open-rails QA declaration:** If the epic affects user or production surfaces, the Epic Plan MUST declare whether open-rails QA is mandatory or whether an explicit PO-authorized exemption applies. This declaration must be planning-level and must not embed Live QA runbook commands in the Epic Plan.  
* **Open-rails triggering surfaces:** User or production-surface triggers include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor request shaping, vendor response handling, vendor route policy, external API transport, environment or secret binding behavior, database persistence or retrieval behavior, runtime compute behavior, deployed service behavior, and admin or ops-facing behavior that can affect production truth.  
* **Implementation preservation:** Any Implementation Plan, remediation guide, or downstream QA-prep artifact derived from the Epic Plan MUST preserve the open-rails QA requirement unless it records the controlling PO-authorized exemption. Closed-rails proof, static validation, repository inspection, generated evidence, or OPS observation alone does not erase a declared open-rails QA requirement.  
* **Review posture:** A reviewer MUST block QA-plan approval or QA-readiness posture when a user or production-surface epic omits the required bounded open-rails QA step and also omits a controlling PO-authorized exemption. The blocker language must identify the affected surface, such as CLI, vendor ingestion, vendor transport, runtime persistence, public app behavior, or deployed service behavior.  
````

NEW:

````text
* **Open-rails QA declaration:** Identify whether the epic touches a surface used to produce a production feature stated as functional in PF-Canon. For that scope, declare the mandatory bounded live vendor test with synthetic data only and `SAFE_MODE=0`, `ALLOW_NETWORK=1`; no exemption or non-vendor substitute is established. Outside that scope, retain the applicable broader production-affecting open-rails requirement and any already authorized exemption. Keep the declaration planning-level; do not embed Live QA commands in the Epic Specification.  
* **Open-rails triggering surfaces:** User or production-surface triggers include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor request shaping, vendor response handling, vendor route policy, external API transport, environment or secret binding behavior, database persistence or retrieval behavior, runtime compute behavior, deployed service behavior, and admin or ops-facing behavior that can affect production truth.  
* **Implementation preservation:** Any Implementation Plan, remediation guide or downstream QA-prep artifact derived from the Epic Specification MUST preserve the mandatory live vendor test for production-functional scope. Closed-rails proof, static validation, repository inspection, generated evidence, a database or deployed-service probe, OPS observation or exemption language does not erase it. Preserve any separately applicable broader open-rails obligation outside that scope.  
* **Review posture:** A QA Plan within production-functional scope is not approval-ready without the bounded synthetic live vendor test. Identify the affected feature and surface; do not approve a closed-rails-only plan on an exemption or a non-vendor live-step substitute. Outside that scope, apply the existing broader production-affecting requirement and its controlling authorization.  
````

## RL-045

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [175668, 176009); original lines 1489–1489  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Deliverables (Jobs To Be Done)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* The HDE Epic Plan MUST NOT embed a Live QA runbook, including commands, step-by-step checks, QA\_ROOT directory design, README generator rules, or per-step artifact layouts. Those are authored as separate QA work products during Close Gate execution. PF20 remains historical reference material and is not the current planning authority.  
````

NEW:

````text
* The HDE Epic Specification MUST NOT embed a Live QA runbook, including commands, step-by-step checks, QA\_ROOT directory design, README generator rules, or per-step artifact layouts. Those are authored as separate QA work products during Close Gate execution. PF20 remains historical reference material and is not the current planning authority.  
````

## RL-046

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [181128, 181181); original lines 1546–1546  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **QA Rails — Open/Close (Final PR)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
**Hard boundary (Epic Plan vs QA execution canon):**
````

NEW:

````text
**Hard boundary (Epic Specification vs QA execution canon):**
````

## RL-047

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [181300, 181363); original lines 1550–1550  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **QA Rails — Open/Close (Final PR)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
The HDE Epic Plan stages QA expectations only at the level of:
````

NEW:

````text
The HDE Epic Specification stages QA expectations only at the level of:
````

## RL-048

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [181655, 181744); original lines 1557–1557  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **QA Rails — Open/Close (Final PR)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
The HDE Epic Plan MUST NOT include QA planning artifacts or execution detail, including:
````

NEW:

````text
The HDE Epic Specification MUST NOT include QA planning artifacts or execution detail, including:
````

## RL-049

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [187370, 187401); original lines 1633–1633  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
#### **Plan Preflight (MUST)**
````

NEW:

````text
#### **Specification Preflight (MUST)**
````

## RL-050

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [188172, 188262); original lines 1646–1646  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
**Scope boundary (hard rule): Plan Preflight is Epic Planning only — not QA planning.**
````

NEW:

````text
**Scope boundary (hard rule): Specification Preflight is Epic Planning only — not QA planning.**
````

## RL-051

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [188263, 188315); original lines 1648–1648  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* The HDE Epic Plan MUST NOT contain QA runbooks.  
````

NEW:

````text
* The HDE Epic Specification MUST NOT contain QA runbooks.  
````

## RL-052

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [188315, 188392); original lines 1649–1649  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* The HDE Epic Plan MUST NOT include QA execution instructions, including:  
````

NEW:

````text
* The HDE Epic Specification MUST NOT include QA execution instructions, including:  
````

## RL-053

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [188629, 188748); original lines 1656–1656  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* When an epic requires QA execution, including Live QA, the HDE Epic Plan may capture only planning-level outcomes:  
````

NEW:

````text
* When an epic requires QA execution, including Live QA, the HDE Epic Specification may capture only planning-level outcomes:  
````

## RL-054

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [191100, 191213); original lines 1687–1687  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* The Epic Plan MUST explicitly list the required close-pack artifacts (titles-only) for the epic close stage.  
````

NEW:

````text
* The Epic Specification MUST explicitly list the required close-pack artifacts (titles-only) for the epic close stage.  
````

## RL-055

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [191213, 191511); original lines 1688–1688  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Close-stage baseline surfaces MAY be listed in the Epic Plan at planning level without turning the Epic Plan into a QA runbook. The plan MUST keep QA commands, step logs, operator procedures, and runbook execution detail out of the Epic Plan unless a separate QA artifact explicitly owns them.  
````

NEW:

````text
* Close-stage baseline surfaces MAY be listed in the Epic Specification at planning level without turning the Epic Specification into a QA runbook. The plan MUST keep QA commands, step logs, operator procedures, and runbook execution detail out of the Epic Specification unless a separate QA artifact explicitly owns them.  
````

## RL-056

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [191511, 191765); original lines 1689–1689  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Missing close-stage execution detail in an Epic Plan is not, by itself, a valid reason to defer implementation or QA. The plan must preserve the required close-pack baseline while routing execution detail to the owning QA, OPS, or closeout artifact.  
````

NEW:

````text
* Missing close-stage execution detail in an Epic Specification is not, by itself, a valid reason to defer implementation or QA. The plan must preserve the required close-pack baseline while routing execution detail to the owning QA, OPS, or closeout artifact.  
````

## RL-057

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [194886, 194976); original lines 1729–1729  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
The Epic Plan MUST declare both doc-delta surfaces (concrete filenames; no placeholders):
````

NEW:

````text
The Epic Specification MUST declare both doc-delta surfaces (concrete filenames; no placeholders):
````

## RL-058

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [195581, 195723); original lines 1736–1736  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Epic Plans MUST NOT be considered approvable if they omit this close-pack baseline and doc-delta baseline file set for eventual epic close.
````

NEW:

````text
* Epic Specifications MUST NOT be considered approvable if they omit this close-pack baseline and doc-delta baseline file set for eventual epic close.
````

## RL-059

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [196850, 197031); original lines 1754–1754  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2\) HDE-EPIC-Plan**
### **Epic Record Template (Normative)**
#### **Plan Preflight (MUST)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
The Epic Plan MUST validate each named evidence pointer is bound to a canonical surface in the “HDE Schemas & Artifacts” evidence catalog (exact path string, including case).  
````

NEW:

````text
The Epic Specification MUST validate each named evidence pointer is bound to a canonical surface in the “HDE Schemas & Artifacts” evidence catalog (exact path string, including case).  
````

## RL-060

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [203530, 203587); original lines 1852–1852  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
````

NEW:

````text
## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**
````

## RL-061

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [203847, 204149); original lines 1858–1858  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **Applicability and process routing**
````

Reason: Route CRD permanent format to its actual register owner while retaining reusable downstream templates.

OLD:

````text
The Change Process Guide governs the shared lifecycle. The CRD uses CRD identity and PF30 accountability where an epic uses Epic identity and PF09 accountability. The change lanes differ by origin, identity, and controlling work register, not by implementation, QA, evidence, review, or closure rigor.
````

NEW:

````text
The Change Process Guide governs the shared lifecycle. The CRD uses CRD identity and PF30 accountability where an epic uses Epic identity and PF09 accountability. The change lanes differ by origin, identity, and controlling work register, not by implementation, QA, evidence, review, or closure rigor.

The permanent CRD Specification uses the CRD record contract and record template in the active HDE-CRD-Records volume. This PF27 profile supplies applicability and reuse guidance; its intake prompts do not define an alternative permanent Specification structure.
````

## RL-062

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [204150, 204319); original lines 1860–1860  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **Applicability and process routing**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
A CRD MAY contain one or more PR units, Ops tasks, or both. A CRD Plan does not authorize implementation, QA, Ops, canon supersession, acceptance, or closure by itself.
````

NEW:

````text
A CRD MAY contain one or more PR units, Ops tasks, or both. A CRD Specification does not authorize implementation, QA, Ops, canon supersession, acceptance, or closure by itself.
````

## RL-063

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CLARIFY  
Original UTF-8 span: [204368, 204396); original lines 1864–1864  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **CRD intake and Lead Developer analysis**
````

Reason: Keep analysis prompts as guidance rather than a competing permanent Specification field contract.

OLD:

````text
Every CRD Plan MUST record:
````

NEW:

````text
Use the following prompts for CRD intake and Lead Developer analysis; record the permanent CRD Specification in the active PF30 owner's required format:
````

## RL-064

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [206752, 207116); original lines 1904–1904  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **Existing-template reuse and substitution**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
Where an owning schema, governed path, manifest, evidence root, validator, or artifact contract currently accepts only Epic identity, the CRD Plan MUST record that compatibility dependency and route it to the owning canon or change lane before the affected CRD relies on it. PF27 MUST NOT invent a CRD path, schema field, validator behavior, or artifact identity.
````

NEW:

````text
Where an owning schema, governed path, manifest, evidence root, validator, or artifact contract currently accepts only Epic identity, the CRD Specification MUST record that compatibility dependency and route it to the owning canon or change lane before the affected CRD relies on it. PF27 MUST NOT invent a CRD path, schema field, validator behavior, or artifact identity.
````

## RL-065

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [207161, 207423); original lines 1908–1908  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **Canon, QA, and closeout boundaries**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
A canon-changing CRD requires an accompanying approved ADR. The ADR MUST identify the affected canon and drainage consequences. Material CRD canon activity and decisions enter HDE Build Notes before permanent drainage. A CRD Plan alone does not supersede canon.
````

NEW:

````text
A canon-changing CRD requires an accompanying approved ADR. The ADR MUST identify the affected canon and drainage consequences. Material CRD canon activity and decisions enter HDE Build Notes before permanent drainage. A CRD Specification alone does not supersede canon.
````

## RL-066

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CANON_UPDATE  
Original UTF-8 span: [208084, 209292); original lines 1923–1948  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **2A) HDE-CRD-Plan Profile and PF30 Record Contract**
### **Compact PF30 record contract**
````

Reason: Remove the competing compact field contract and route the permanent format to the read current PF30 owner without changing its fields or historical entries.

OLD:

````text
### **Compact PF30 record contract**

PF30 is the concise CRD accountability register, not the implementation log, QA archive, evidence store, runbook, or retrospective. Update the existing CRD record when material scope, status, authority, or final outcome changes.

The initial PF30 record contains:

* CRD ID and title;  
* status and creation date;  
* observed need or requested change;  
* Lead Developer disposition and bounded scope;  
* alchemical phase block or blocks;  
* planned PR and Ops units with dependencies;  
* canon impact and approved ADR reference, when applicable;  
* QA requirement; and  
* CRD Plan and material HDE Build Notes references.

The PF30 closure update contains:

* final status and closure date;  
* implemented PR, commit, merge, and Ops references;  
* QA verdict and exact candidate identity;  
* material deviations or deferred work;  
* ADR and canon-drain status; and  
* final authorized outcome.

PF30 records reference detailed governed sources. They MUST NOT reproduce full plans, commands, logs, evidence payloads, QA runbooks, or retrospectives. No PF27-derived artifact creates a new PF30 volume; volume rollover remains controlled by the PF30 register.
````

NEW:

````text
### **PF30-owned Specification format and record contract**

PF30 is the concise CRD accountability register, not the implementation log, QA archive, evidence store, runbook or retrospective. Resolve its current active volume and use its **Minimum CRD record contract** and **CRD record template** for the permanent CRD Specification, including initial registration, material-change history, phase tracking and closure fields. The current format owner is `PF30.1-Canon-HDE-CRD-Records`, **Minimum CRD record contract** and **CRD record template**; this profile does not replace or compress that contract.

Update the existing CRD record when material scope, status, authority or final outcome changes. Preserve its actual historical approval and lineage wording; current Specification terminology does not retrospectively rewrite records.

PF30 records reference detailed governed sources. They MUST NOT reproduce full Implementation Plans, commands, logs, evidence payloads, QA runbooks or retrospectives. No PF27-derived artifact creates a new PF30 volume; volume rollover remains controlled by the PF30 register.
````

## RL-067

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [212205, 212305); original lines 1983–1983  
Basis / selected source ledger: A38

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **3\) Ops Task Record (Template)**
### **Not a PR (normative)**
````

Reason: Express the governing actor, auditor or prompt recipient by function; preserve vocabulary and machine labels and existing task authority.

OLD:

````text
* Ops tasks are **not** Codex PRs and **MUST NOT** be represented as “implementable PR work.”  
````

NEW:

````text
* Ops tasks are **not** repository PRs and **MUST NOT** be represented as “implementable PR work.”  
````

## RL-068

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [222693, 222948); original lines 2096–2096  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **3A) Epic Remediation Plan (Template)**
### **Scope**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
An Epic Remediation Plan does not replace the controlling Epic Plan, a broader Implementation Plan, a QA Plan, a Live QA runbook, an OPS transcript, an acceptance review, or an epic-close record. It authorizes only its expressly bounded corrective scope.
````

NEW:

````text
An Epic Remediation Plan does not replace the controlling Epic Specification, a broader Implementation Plan, a QA Plan, a Live QA runbook, an OPS transcript, an acceptance review, or an epic-close record. It authorizes only its expressly bounded corrective scope.
````

## RL-069

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [223187, 223346); original lines 2102–2102  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **3A) Epic Remediation Plan (Template)**
### **Approval rule (normative)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
It **MUST NOT** be rejected, revised, or conditioned solely because it does not conform to an adjacent Epic Plan or Remediation Implementation Guide template.
````

NEW:

````text
It **MUST NOT** be rejected, revised, or conditioned solely because it does not conform to an adjacent Epic Specification or Remediation Implementation Guide template.
````

## RL-070

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [249615, 249630); original lines 2738–2738  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **6\) Audit Analysis Record (Template; REVIEW mode only)**
### **Required structure (paste-ready)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Epic Plan:  
````

NEW:

````text
* Epic Specification:  
````

## RL-071

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [250143, 250181); original lines 2761–2761  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **6\) Audit Analysis Record (Template; REVIEW mode only)**
### **Required structure (paste-ready)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Epic Plan linkage (one sentence):  
````

NEW:

````text
* Epic Specification linkage (one sentence):  
````

## RL-072

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [250181, 250226); original lines 2762–2762  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **6\) Audit Analysis Record (Template; REVIEW mode only)**
### **Required structure (paste-ready)**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
* Epic Plan anchor (verbatim line or N/A):  
````

NEW:

````text
* Epic Specification anchor (verbatim line or N/A):  
````

## RL-073

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [297719, 298151); original lines 3757–3757  
Basis / selected source ledger: A14

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **12\) General Implementation Plan (Template)**
### **Applicability and ownership boundary**
````

Reason: Adopt Specification naming for the corresponding permanent record; preserve Implementation, QA and Remediation Plan classes.

OLD:

````text
Use this template for a project implementation plan only when no more-specific PF27 template controls the artifact class. It does not replace the HDE Epic Plan, Ops Task Record, Epic Remediation Plan, Remediation Implementation Guide, Live QA Plan, or any review or closeout record. PF27 owns this reusable shape; `PF06-Canon-Change-Process-Guide` owns process sequencing, roles, approval responsibilities, and PR-first discipline.
````

NEW:

````text
Use this template for a project implementation plan only when no more-specific PF27 template controls the artifact class. It does not replace the HDE Epic Specification, Ops Task Record, Epic Remediation Plan, Remediation Implementation Guide, Live QA Plan, or any review or closeout record. PF27 owns this reusable shape; `PF06-Canon-Change-Process-Guide` owns process sequencing, roles, approval responsibilities, and PR-first discipline.
````

## RL-074

Operation: REPLACE  
Expected occurrence count: 1  
Change type: CONSISTENCY  
Original UTF-8 span: [299029, 299257); original lines 3785–3785  
Basis / selected source ledger: A30

Location — complete authored original heading path:

````text
# **A) Glow Plan and Runbook Templates**
## **12\) General Implementation Plan (Template)**
### **Required structure**
#### **Governing-source map**
````

Reason: Keep the general governing-source map from requiring internal Build Notes locators.

OLD:

````text
Do not copy externally owned process, token, schema, transport, architecture, infrastructure, QA, or evidence-contract bodies into this plan. Retain the local writer-facing consequence and route the governed truth to its owner.
````

NEW:

````text
Do not copy externally owned process, token, schema, transport, architecture, infrastructure, QA, or evidence-contract bodies into this plan. Retain the local writer-facing consequence and route the governed truth to its owner. HDE Build Notes is the title-only exception to the locator column: do not supply an internal addendum, heading, section or file-version locator. Source-use inventories retain actual retrieved file identity and historical provenance.
````

END OF REDLINES
