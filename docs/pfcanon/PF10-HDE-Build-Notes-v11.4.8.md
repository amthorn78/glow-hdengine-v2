# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.4.8  
Effective Date: 2026.06.16

**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

## Precedence and versioning

**PF10 IS CANONICAL.** For any topic explicitly covered in this scratchpad, PF10 is the current authoritative source of truth and **supersedes all other PF canon** until that item is formally reviewed and drained into the relevant permanent PF document.

**No competing canon may be used against an active PF10 entry.** While an item remains live in this scratchpad, agents must follow PF10 for that topic and must not prefer, merge, reinterpret, or reconcile conflicting language from older PF canon.

**Later addendum wins.** If multiple addenda address the same or overlapping scope, the **highest-numbered / latest addendum is the only authoritative one**. Earlier addenda on that scope are superseded and must not be used in parallel.

**Only the latest PF10 file matters.** Older scratchpad files are **fully drained, obsolete, or both**. Agents must **not** read them, reuse them, compare them, reconcile them, or carry forward language from them once a newer PF10 exists.

**This file contains only live items.** Drained items are removed from the scratchpad. Therefore, the current version of PF10 contains only active, not-yet-merged guidance.

**Silence means canon reverts to the permanent PF home.** If a topic does **not** appear in the latest PF10, then PF10 has nothing to say about it, and the source of truth is the relevant permanent PF-Canon document.

**Operational rule for agents:** use the latest PF10 first; obey it wherever it speaks; ignore older scratchpads entirely; fall back to permanent PF-Canon only where the latest PF10 is silent.

## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\> (autofill from system info)  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## 1.1 Addendum Index:

2.1 ) Deferral Is Exception-Only; OPS Discovery Is First-Class Work  
2.2 ) Open-Rails Testing Is Allowed When Needed for Implementation or QA  
2.3) HDE-EPIC034 Planning ADR Decisions: Do Not Defer Discoverable Vendor and Infrastructure Work  
2.4) Codex Audit Observed Evidence Is Valid Planning-Time Repo-Reality Evidence  
2.5) Mission-Critical Environment Variable Inventory Must Be Preserved in PF07  
2.6) HD API Base URL Environment Variable Name Decision  
2.7) HumanDesignAPI v2 Uses Authorization Bearer; v1 Uses HD-Api-Key Header

# 2\) Numbered Addenda

---

## **2.1 ) Deferral Is Exception-Only; OPS Discovery Is First-Class Work**

Timestamp: 061626

Details: HDE planning has repeatedly deferred in-scope PF09 work because infrastructure, vendor, environment, credential-binding, OPS-root, or open-rails facts were not already pinned before planning. That posture is rejected.

The project has OPS tasks, PF10 live-rule authority, documented environment-variable patterns, PO-owned operational execution, and governed evidence practices so that unknown operational facts can be discovered and recorded without guessing.

Deferral is exception-only.

Unknown but discoverable is not a deferral reason.

### **Decision / rule / clarification**

In-scope PF09.x work MUST NOT be deferred merely because operational facts are unknown.

If a missing fact can be safely discovered, confirmed, or recorded by the PO through a bounded OPS task, the plan must route an OPS discovery task instead of deferring the PF09.x work.

OPS discovery tasks are valid work items in Epic Plans, Implementation Plans, QA-readiness action plans, remediation guides, and QA Plans when QA needs PO-run operational support.

OPS discovery may be used to discover or confirm:

* environment variable names  
* documented environment-variable bindings  
* credential-binding names  
* config-key names  
* secret-binding names  
* base URL posture  
* vendor account posture  
* vendor tier posture  
* endpoint availability  
* route-family availability  
* open-rails permission posture  
* vendor smoke preconditions  
* OPS evidence root requirements  
* external console or admin facts  
* deployment/runtime facts  
* whether a dependent PR can proceed safely  
* whether a QA proof can be designed honestly

OPS discovery must record the fact needed for execution or QA without exposing secret values.

### **Deferral standard**

Deferral is allowed only with strong, explicit justification.

A plan may defer in-scope work only when at least one of the following is true:

* The work is explicitly outside the approved epic scope.  
* The work belongs to a later alchemical phase and pulling it forward would create real phase drift.  
* The work requires a PO or Thoth decision that has not been made and cannot be safely staged through PF10.  
* The work requires a new acceptance token that Governance or PF10 has not admitted.  
* The work would mutate production or external systems without PO authorization.  
* The work would expose secrets or require unsafe handling of secrets.  
* The work requires live external execution that the PO has not authorized.  
* The work depends on a prior in-scope PR or OPS result that must happen first.  
* The missing fact cannot be safely discovered through bounded OPS discovery.  
* The work would require inventing facts, paths, credentials, evidence roots, vendor behavior, infrastructure state, or canon authority.  
* The work is blocked by a real canon contradiction that PF10 cannot safely bridge as live temporary authority.

If none of those conditions applies, deferral is not justified.

### **Invalid deferral reasons**

The following are not valid deferral reasons by themselves:

* “The environment variable is unknown.”  
* “The credential-binding name is unknown.”  
* “The config key is unknown.”  
* “The base URL is unknown.”  
* “The secret-binding name is unknown.”  
* “The vendor account posture is unknown.”  
* “The endpoint availability is unknown.”  
* “The OPS evidence root is unknown.”  
* “The PO must confirm it.”  
* “Codex cannot discover it.”  
* “Open rails are involved.”  
* “The work requires OPS.”  
* “PF07 has not drained the fact yet.”  
* “PF12 has not named the evidence root yet.”

Those are OPS discovery candidates.

They are not automatic deferral grounds.

### **OPS discovery task requirements**

A valid OPS discovery task must state:

* the exact fact to discover  
* why the fact matters  
* who owns discovery  
* whether secrets are involved  
* what may be recorded  
* what must not be recorded  
* what downstream PR, QA, OPS, or planning item depends on it  
* what safe evidence or summary resolves the unknown

OPS discovery must not silently become implementation, QA execution, acceptance proof, closure proof, or uncontrolled external action.

OPS discovery may unblock implementation or QA, but the discovered fact must still be routed into the relevant PR, QA Plan, Implementation Plan, or closeout proof before it is relied on.

### **Planning rule**

Plans must classify unknowns as exactly one of:

* discoverable by OPS  
* discoverable by PR  
* discoverable by QA  
* requires PO/Thoth decision  
* requires PF10 live rule  
* requires permanent canon update before safe execution  
* unsafe to discover now  
* out of scope  
* phase drift  
* valid deferral

“Unknown” alone is not a classification.

“OPS required” alone is not a deferral reason.

“Open rails required” alone is not a deferral reason.

### **Immediate operating rule**

Until drained, this PF10 addendum is the live rule:

Do not defer in-scope PF09.x work merely because operational, infrastructure, vendor, credential, environment, open-rails, or OPS-root facts are unknown.

Create bounded OPS discovery tasks when those facts can be safely discovered by the PO.

Deferral requires strong justification.

Unknown but discoverable is not deferred.

### **Drain targets**

Drain this addendum into:

* PF27 — Canon Plan Templates: add template rules requiring explicit deferral justification and OPS discovery routing for discoverable operational unknowns.  
* PF06 — Epic Process Guide: add OPS discovery as a first-class planning/execution work type and distinguish discoverable unknowns from valid deferral.  
* PF07 — Glow Infrastructure: add guidance that missing infrastructure, credential-binding, config-key, base URL, secret-binding, and environment facts should route to OPS discovery where safe.  
* PF05 — HDE CLI-API-Vendor Ref: add vendor-integration guidance that unknown route, account, tier, auth, endpoint, and request/response facts are OPS discovery candidates.  
* PF12 — HDE Schemas and Artifacts: add OPS discovery evidence posture for safe operational fact capture and evidence-root binding.  
* PF19 — Glow QA Guide: add QA planning guidance that discoverable operational facts may be routed through OPS discovery and do not automatically defer QA or implementation.  
* PF09.5 — HDE Build Checklist Fermentation: add phase-checklist posture that Fermentation subtasks should not be deferred for discoverable OPS facts.  
* PF04 — HDE Governance: add governance posture that acceptance-token issues may block, but operational discovery does not require new token creation.  
* PF14 — HDE Mechanics Guide: add mechanics guidance distinguishing discoverable operational facts from real mechanics/design gaps.

## **2.2 ) Open-Rails Testing Is Allowed When Needed for Implementation or QA**

Timestamp: 061626

Details: HDE planning has treated open-rails testing as something to avoid or defer by default. That posture is too restrictive. Some vendor, runtime, integration, credential-binding, account-tier, and QA acceptance facts cannot be proven honestly through closed-rails inspection alone.

Open-rails testing is allowed when needed.

Open-rails testing must be bounded, PO-authorized, secret-safe, and evidence-recorded. Those controls are not deferral triggers. They are the normal execution posture for live operational work.

### **Decision / rule / clarification**

Open-rails testing may be included in implementation and QA plans when it is necessary to prove or discover:

* live vendor reachability  
* vendor endpoint availability  
* auth posture  
* credential-binding correctness  
* config-key correctness  
* base URL posture  
* request/response compatibility  
* vendor account tier or permission behavior  
* rate-limit or retry behavior  
* vendor error-envelope behavior  
* integration viability  
* QA acceptance posture that cannot be proven closed-rails only

Open-rails testing is not automatically deferred.

Open-rails testing is not automatically out of scope.

Open-rails testing is not automatically a blocker.

Open-rails testing is not automatically a later epic.

If open-rails testing is needed and the work is otherwise in scope, the plan must route a bounded OPS open-rails task rather than deferring by default.

### **Allowed use in implementation**

Implementation Plans may include OPS open-rails tasks when live operational information is needed to unblock implementation or validate a vendor-facing implementation assumption.

Implementation open-rails tasks may support:

* PR discovery  
* PR implementation  
* request shaping  
* response mapping  
* credential binding  
* endpoint availability checks  
* vendor account/tier confirmation  
* runtime integration proof  
* bounded smoke testing

Codex may prepare repo-local code, fixtures, validators, redaction helpers, harnesses, docs, and evidence-processing logic, but Codex must not perform PO-only live external actions or handle secret values directly.

The PO may run the live open-rails action and return a bounded, redacted evidence summary.

### **Allowed use in QA**

QA Plans may include OPS open-rails tasks when live operational verification is necessary for the QA proof.

QA open-rails tasks may support:

* live vendor smoke  
* credential-binding confirmation  
* endpoint-family confirmation  
* account/tier confirmation  
* error-envelope confirmation  
* open-rails versus closed-rails contrast  
* acceptance evidence that cannot honestly be proven closed-rails only

A QA Plan may require a PO-run open-rails evidence summary without becoming an OPS plan or implementation plan.

### **Open-rails safety posture**

Open-rails work must preserve these boundaries:

* No secret values in logs, prompts, commits, artifacts, or chat.  
* No uncontrolled production mutation.  
* No destructive external action unless explicitly authorized by the PO.  
* No open-ended vendor probing.  
* No broad exploratory live testing when a bounded smoke answers the question.  
* No public Reader expansion unless explicitly scoped.  
* No new HTTP home unless explicitly scoped.  
* No new acceptance token unless Governance or PF10 admits it.  
* No treating vendor smoke success as broader conformance than it proves.  
* No treating vendor smoke failure as product failure until credential, environment, vendor, account, and endpoint posture are distinguished.

These boundaries are not excuses for deferral.

They are the rules for doing open-rails work safely.

### **Open-rails evidence posture**

Open-rails evidence may record:

* task ID  
* operator or owner role  
* date/time if available  
* environment label  
* vendor family or endpoint family  
* credential-binding name, not secret value  
* request class, not secret payload  
* high-level result  
* status code or vendor error class when safe  
* redacted response excerpt when safe  
* whether behavior matched expectation  
* whether follow-up PR, OPS, QA update, or canon update is needed

Open-rails evidence must not record:

* raw API keys  
* raw bearer tokens  
* raw secrets  
* sensitive account details  
* unnecessary personally identifying information  
* uncontrolled production data  
* full private payloads unless explicitly approved and safe

### **Open-rails failure interpretation**

An open-rails failure is not automatically a product failure.

Classify the failure before acting.

Open-rails failure may indicate:

* credential issue  
* config issue  
* vendor account/tier limitation  
* endpoint unavailability  
* vendor contract mismatch  
* request-shaping defect  
* response-mapping defect  
* infrastructure gap  
* rate-limit or retry posture  
* external outage  
* product implementation defect  
* QA plan expectation mismatch

Do not collapse these categories.

The purpose of open-rails testing is to discover truth, not to force premature deferral.

### **Immediate operating rule**

Until drained, this PF10 addendum is the live rule:

Open-rails testing is allowed in implementation and QA when needed.

If open-rails proof is necessary and the work is in scope, create a bounded OPS open-rails task.

Do not defer merely because open rails, live vendor access, credentials, or PO-run operational execution are involved.

### **Drain targets**

Drain this addendum into:

* PF27 — Canon Plan Templates: add template support for OPS open-rails tasks in Implementation Plans, QA Plans, and remediation guides.  
* PF19 — Glow QA Guide: add QA open-rails support posture, evidence summary requirements, and failure classification rules.  
* PF06 — Epic Process Guide: add process guidance for sequencing PR, OPS discovery, OPS open-rails testing, and QA.  
* PF07 — Glow Infrastructure: add infrastructure rules for safe live config, credential-binding, base URL, and environment posture discovery.  
* PF05 — HDE CLI-API-Vendor Ref: add vendor testing posture for live route, auth, error, rate-limit, and account/tier facts.  
* PF12 — HDE Schemas and Artifacts: add open-rails evidence summary and redaction posture where live vendor evidence becomes governed.  
* PF04 — HDE Governance: add governance posture that open-rails testing does not mint acceptance tokens or expand acceptance scope by itself.  
* PF09.5 — HDE Build Checklist Fermentation: add Fermentation guidance that live vendor or open-rails needs may be routed through OPS tasks rather than deferred by default.

## **2.3) HDE-EPIC034 Planning ADR Decisions: Do Not Defer Discoverable Vendor and Infrastructure Work**

Timestamp: 061626

Details: HDE-EPIC034 planning included ADRs that treated request-shaping, deterministic shaping, and open-rails smoke as deferred because PF05/PF07/PF12 facts were not pinned. This addendum decides those ADRs for planning purposes under the new deferral and open-rails posture.

The decision is to keep the work in scope where safe and route discoverable facts through OPS tasks.

### **ADR-001 — HDE-FERM007.2 request-shaping execution**

Decision: Do not defer HDE-FERM007.2 solely because v2 request-shaping infrastructure or credential facts are unknown.

HDE-FERM007.2 may remain in the epic plan as in-scope work if the plan includes OPS discovery tasks to confirm the required operational facts.

OPS discovery may confirm:

* v2 base URL posture  
* v2 auth header names  
* credential/config key names  
* secret-binding names  
* documented environment-variable bindings  
* legacy-to-v2 mapping facts  
* endpoint-family availability  
* account/tier posture

PR work may proceed after the required OPS facts are discovered and recorded in a safe form.

The plan must not guess these values.

The plan must not defer HDE-FERM007.2 merely because the values are not already in PF05 or PF07.

Deferral remains valid only if PO authorization is not available, discovery is unsafe, a real canon contradiction exists, or the work is explicitly removed from epic scope by PO/Thoth.

Planning disposition: HDE-FERM007.2 should be routed as OPS discovery plus dependent PR work, not deferred by default.

### **ADR-002 — HDE-FERM007.5 closed-rails deterministic shaping proof**

Decision: Do not defer HDE-FERM007.5 solely because deterministic shaping proof depends on discoverable request-shaping or infrastructure facts.

HDE-FERM007.5 may remain in scope if the plan sequences:

* OPS discovery for operational/config facts;  
* PR implementation or proof work for deterministic source selection and shaping;  
* closed-rails proof using discovered bindings without live calls;  
* optional OPS open-rails contrast if live vendor behavior is needed to confirm the boundary.

Closed-rails deterministic proof must not invent values. It may use discovered operational facts once safely recorded.

If the proof requires live vendor behavior, that live behavior may be tested through a bounded OPS open-rails task.

Deferral remains valid only if request-shaping remains unresolved after OPS discovery, if PO authorization is absent, if live testing is unsafe, or if Thoth/PO explicitly reclassifies HDE-FERM007.5 out of this epic.

Planning disposition: HDE-FERM007.5 should be treated as in-scope after the necessary OPS discovery and PR prerequisites, not deferred by default.

### **ADR-003 — HDE-FERM008.2 PO-only open-rails smoke**

Decision: Do not defer HDE-FERM008.2 solely because it requires PO-only open-rails testing.

Open-rails testing is allowed as an OPS task.

HDE-FERM008.2 may be planned as a bounded PO-run OPS open-rails task if the epic scope includes it and the PO authorizes execution.

The task may discover and record:

* live vendor reachability  
* credential-binding correctness  
* endpoint availability  
* account/tier posture  
* vendor error class  
* redacted response shape  
* safe status outcome  
* whether follow-up PR or QA work is needed

The task must not expose secret values.

The task must not overclaim full runtime conformance from a narrow smoke.

Deferral remains valid only if PO does not authorize live execution, if the task would be unsafe, if the required secret posture cannot be handled safely, or if Thoth/PO explicitly excludes HDE-FERM008.2 from the epic.

Planning disposition: HDE-FERM008.2 should be routed as a PO-run OPS open-rails task when in scope, not deferred by default.

### **ADR-004 — PF27 close-stage path posture**

Decision: PF27-required close-stage baseline surfaces may be listed in plans without turning the plan into a QA runbook.

This ADR remains approved.

Close-stage path posture is not a reason to defer implementation or QA.

Plans may list close-stage baseline surfaces at the planning level while keeping QA commands, step logs, and runbook procedures out of the Epic Plan.

Planning disposition: preserve PF27/PF12 close-stage baseline posture; do not use it as a deferral reason.

### **HDE-EPIC034 planning impact**

The next HDE-EPIC034 plan revision should not default HDE-FERM007.2, HDE-FERM007.5, or HDE-FERM008.2 to Deferred with rationale solely because OPS, open rails, credentials, environment variables, or infrastructure facts are involved.

Instead, it should classify each as:

* OPS discovery;  
* OPS open-rails testing;  
* dependent PR work;  
* QA-supported OPS work;  
* valid deferral only if the deferral standard is met.

The plan should use OPS tasks to discover and record necessary operational facts.

The plan should use PF10 as live temporary authority where permanent PF canon has not yet drained.

### **Drain targets**

Drain these ADR decisions into:

* PF09.5 — HDE Build Checklist Fermentation: clarify HDE-FERM007/HDE-FERM008 planning posture so discoverable OPS/open-rails facts do not force deferral.  
* PF05 — HDE CLI-API-Vendor Ref: clarify HDAPI v2 request-shaping and vendor-smoke unknowns as OPS discovery/open-rails candidates.  
* PF07 — Glow Infrastructure: clarify v2 environment, credential-binding, base URL, and secret-binding discovery posture.  
* PF12 — HDE Schemas and Artifacts: clarify OPS evidence summary and open-rails evidence binding.  
* PF19 — Glow QA Guide: clarify QA-supported OPS open-rails tasks and failure classification.  
* PF27 — Canon Plan Templates: clarify that OPS tasks can be first-class plan items for discovery and open-rails testing.  
* PF06 — Epic Process Guide: clarify PR/OPS/QA sequencing for discoverable operational facts.

## **2.4) Codex Audit Observed Evidence Is Valid Planning-Time Repo-Reality Evidence**

Timestamp: 061626

Details: HDE-EPIC034 implementation-plan review exposed a false-blocker pattern: plan review rejected “Observed Evidence (non-PF)” when the observed evidence came from a Codex Audit that was explicitly supplied as a planning input. That posture is too restrictive.

Codex Audits exist to provide read-only repo-reality observations for planning, implementation scoping, existing-locus checks, drift detection, and Codex prompt portability. When a Codex Audit is in scope for a plan or review, its repo observations may be used as observed evidence.

This addendum clarifies that Codex Audit observed evidence is valid planning-time repo-reality evidence when properly labeled and bounded.

### **Decision / rule / clarification**

A Codex Audit is an authorized planning-time source for observed repo reality when it is explicitly supplied for the plan, review, implementation guide, remediation guide, or QA-prep artifact.

Observed evidence from a Codex Audit may be used to support:

* existing repo-locus claims  
* existing file/path claims  
* existing module/component claims  
* existing test/harness/helper claims  
* current repo-reality framing  
* implementation scoping  
* Codex prompt portability  
* “Already implemented and reused” planning posture  
* discovery-first or reuse-first implementation posture  
* gap identification  
* drift identification  
* PR task inputs  
* OPS task dependencies  
* QA-prep context

The phrase “Observed Evidence (non-PF)” is valid when the evidence is sourced from a supplied Codex Audit and the plan makes that provenance clear.

The preferred labels are:

* Observed Evidence (Codex Audit)  
* Observed repo reality (Codex Audit)  
* CA Observed Evidence  
* CA repo-reality observation

“Observed Evidence (non-PF)” remains acceptable if the artifact map or surrounding text identifies the Codex Audit as the source.

### **What Codex Audit observed evidence can prove**

Codex Audit observed evidence can prove planning-time repo reality, including:

* a repo path was observed  
* a file was observed  
* a module was observed  
* a test was observed  
* a helper/tool was observed  
* a component surface was observed  
* a current implementation seam was observed  
* a current artifact family was observed  
* a path or locus was not observed, if the audit states what it searched  
* a mismatch exists between canon/planning expectations and repo reality  
* a PR task may reuse or inspect an existing locus  
* a Codex prompt may safely name a repo locus as observed

This is exactly what Codex Audits are for.

### **What Codex Audit observed evidence does not prove by itself**

Codex Audit observed evidence does not by itself prove:

* acceptance-token satisfaction  
* QA PASS  
* epic closure  
* PF09 status movement  
* PO closeout  
* Live QA execution  
* OPS completion  
* governed evidence freshness after later changes  
* production truth  
* external vendor truth  
* open-rails truth  
* secret validity  
* runtime conformance beyond what the repo itself proves  
* canon authority  
* new normative rules

Those claims still require the correct owning source: PF10, PF-Canon, governed QA evidence, OPS evidence, PO confirmation, or later closeout evidence as applicable.

### **Planning use rule**

If a plan uses Codex Audit observed evidence for repo reality, it does not need to convert that evidence into a PF citation or an “IG Approved” quote.

A plan may write:

* Observed Evidence (Codex Audit): path found.  
* Observed Evidence (Codex Audit): helper found.  
* Observed Evidence (Codex Audit): component surface found.  
* Observed Evidence (Codex Audit): path not found.  
* Observed Evidence (Codex Audit): current repo seam appears in a named surface.

This is sufficient for planning-time repo-locus support, provided the Codex Audit was supplied as an input and the claim does not overstate acceptance, QA, OPS, closure, or canon truth.

### **Codex prompt portability rule**

A Codex-facing prompt may include Codex Audit observed evidence as embedded context.

The prompt must not require Codex to open the Codex Audit unless the audit is separately supplied to Codex.

The prompt may say, for example:

* Observed repo reality from planning audit: this path was found.  
* Observed repo reality from planning audit: this module was found.  
* Observed repo reality from planning audit: this evidence helper was found.

That is portable when the observation itself is embedded in the prompt.

Codex must still verify repo reality during execution before editing or relying on the locus.

### **Existing-locus claim rule**

A plan may label a path or component as Existing based on Codex Audit observed evidence.

Acceptable form:

* Existing: (Observed Evidence — Codex Audit)

or:

* Existing: \<component/surface\> (Observed Evidence — Codex Audit)

A reviewer must not block this merely because the support is non-PF.

PF canon is not the only valid source for repo reality. PF canon governs authority. Codex Audit observes repo reality.

### **Already implemented and reused rule**

A plan may support “Already implemented and reused” posture with Codex Audit observed evidence when the claim is limited to repo presence, reuse posture, or planning-time implementation reality.

The plan must not overclaim that the item is accepted, QA-passed, closed, or PF09-drained unless PF10, PF09.x, governed evidence, or another owning source supports that stronger claim.

Valid:

* Already implemented and reused — supported by Observed Evidence (Codex Audit) showing the existing repo surface and by the approved plan’s reuse posture.

Invalid:

* Already implemented and Done in PF09 — if PF09.x does not say Done and PF10 does not support it.

### **Review blocker rule**

Reviewers MUST NOT issue REVISE AND RESUBMIT solely because a plan uses “Observed Evidence (non-PF)” for existing-locus or repo-reality support when that observed evidence comes from a supplied Codex Audit.

This is not a blocker.

It may be a blocker only if one of the following is true:

* the plan uses Codex Audit evidence as acceptance proof  
* the plan uses Codex Audit evidence as QA PASS proof  
* the plan uses Codex Audit evidence as closure proof  
* the plan uses Codex Audit evidence as PF09 status movement proof  
* the plan uses Codex Audit evidence as canon authority  
* the plan uses Codex Audit evidence as OPS completion proof  
* the plan uses Codex Audit evidence as live vendor truth  
* the plan fails to identify that the observed evidence came from the Codex Audit  
* the observed evidence is materially ambiguous or contradicts PF10/PF-Canon  
* the plan claims a path exists but the Codex Audit only says it was not found or was unverified  
* the plan relies on an audit observation after later repo changes make freshness unclear and no current check is planned

Otherwise, Codex Audit observed evidence is valid planning input.

### **HDE-EPIC034 application**

For HDE-EPIC034:

* The Implementation Plan may use Observed Evidence from the supplied Codex Audit to support existing repo-locus claims.  
* Existing HDE-EPIC034 repo surfaces observed by the Codex Audit may be labeled as Existing with Observed Evidence (Codex Audit).  
* Already implemented/reused posture may cite Codex Audit observed evidence for repo reality where PF10 or PF09.x does not need to be the proof source.  
* PR tasks may embed Codex Audit observed evidence as planning context.  
* Codex prompts may include Codex Audit observed loci as starting points, while still instructing Codex to verify before editing.  
* This does not claim QA PASS, PF09 drainage, acceptance-token satisfaction, or closure.  
* This does not replace PF10 where PF10 explicitly speaks.  
* This does not replace PF-Canon for authority, tokens, evidence rules, rails, or phase governance.

Any current blocker against HDE-EPIC034 based solely on “Observed Evidence (non-PF)” being used for Codex Audit repo-reality observations is withdrawn by this addendum.

### **Immediate operating rule**

Until drained, this PF10 addendum is the live rule:

Codex Audit observed evidence is valid planning-time repo-reality evidence.

Plans may use it for existing-locus claims, reuse posture, implementation scoping, and Codex prompt context when the Codex Audit is supplied and the claim is bounded to repo reality.

Do not block a plan merely because the repo-reality proof is “Observed Evidence (non-PF)” rather than PF canon, IG Approved, or CA-vetted quote format.

PF canon governs authority. Codex Audit observes repo reality.

### **Drain targets**

#### **PF27 — Canon Plan Templates**

Drain into Epic Plan, Implementation Plan, remediation guide, and review template rules.

Required drain content:

* Codex Audit observed evidence is valid planning-time repo-reality evidence.  
* Plans may use Codex Audit observations to support existing path, component, helper, test, and repo-locus claims.  
* Existing-locus claims may be labeled “Existing: (Observed Evidence — Codex Audit).”  
* Plan reviewers must not require PF canon proof for repo-reality facts when a supplied Codex Audit provides observed evidence.  
* Reviewers must distinguish repo-reality support from acceptance, QA, OPS, closure, PF09, and canon authority.

#### **PF06 — Epic Process Guide**

Drain into planning, implementation-review, remediation-review, and closeout-review posture.

Required drain content:

* Codex Audits are valid planning-time repo-reality inputs.  
* Codex Audit observations may guide PR task scoping and reuse-first planning.  
* Codex Audit evidence can support “existing locus” and “already implemented/reused” planning posture.  
* Codex Audit evidence does not by itself prove closure, QA pass, OPS completion, or PF09 drainage.

#### **PF23 — Reality Audits**

Drain into the relationship between formal Reality Audits and Codex Audits.

Required drain content:

* PF23 remains canon-scoped repo-reality context.  
* Codex Audits may provide task-specific read-only repo-reality observations.  
* A plan may use task-specific Codex Audit observations for current implementation planning when PF23 is too broad, older, or silent.  
* If PF23 and a Codex Audit conflict, record drift and resolve through repo inspection or PF10/PO decision.

#### **PF12 — HDE Schemas and Artifacts**

Drain into evidence and path-proof planning posture.

Required drain content:

* Codex Audit observations may identify existing governed artifacts, evidence helpers, index/mirror files, and path-proof surfaces for planning.  
* Codex Audit observations do not replace governed evidence records at QA or closeout.  
* Plans may use Codex Audit observations to name existing evidence loci when scoping PR or OPS work.

#### **PF19 — Glow QA Guide**

Drain into QA-prep and QA plan review posture.

Required drain content:

* Codex Audit observed evidence may support QA planning context and pre-QA repo-reality framing.  
* Codex Audit evidence may identify expected existing loci for QA to verify.  
* Codex Audit evidence does not substitute for Live QA evidence or PASS proof.  
* QA plan reviewers must not reject a plan merely because repo-reality context came from a supplied Codex Audit.

#### **PF04 — HDE Governance**

Drain into token/evidence authority distinctions.

Required drain content:

* Codex Audit observed evidence may support repo-reality facts.  
* Codex Audit observed evidence does not mint or satisfy acceptance tokens.  
* Governance review should block only if Codex Audit evidence is overclaimed as token, acceptance, or closure proof.

#### **PF05 — HDE CLI-API-Vendor Ref**

Drain into vendor implementation planning posture.

Required drain content:

* Codex Audit observations may support existing vendor seam, route-helper, adapter, CLI, or evidence-tool locus claims.  
* Vendor runtime or live external truth still requires the appropriate OPS/open-rails evidence.  
* Codex Audit repo-reality evidence may seed PR planning but does not prove live vendor conformance.

#### **PF07 — Glow Infrastructure**

Drain into infrastructure planning posture.

Required drain content:

* Codex Audit observations may identify existing config, environment, helper, or repo-bound infrastructure surfaces.  
* Infrastructure-owned live facts still require PF07, PO confirmation, OPS discovery, or open-rails evidence.  
* Do not reject a plan for using Codex Audit observed evidence to identify current repo infrastructure loci.

#### **PF09.5 — HDE Build Checklist Fermentation**

Drain into Fermentation planning/status support posture.

Required drain content:

* Codex Audit observed evidence may support planning-time reuse and existing implementation posture for Fermentation rows.  
* It may support “Already implemented and reused” planning statements when bounded to repo reality.  
* It does not by itself mark a PF09.5 row Done.  
* PF09.5 status movement still requires PF09.5 update, PF10 supportability, or governed closeout posture.

#### **PF14 — HDE Mechanics Guide**

Drain into mechanics/component planning posture.

Required drain content:

* Codex Audit observed evidence may identify current mechanics/component surfaces for planning.  
* PF14 remains mechanics authority; Codex Audit remains repo-reality observation.  
* Plans may combine PF14 mechanics authority with Codex Audit repo observations to scope implementation tasks.

### **Final authority**

Until drained, PF10 is the live source of truth for this topic.

Codex Audit observed evidence is valid.

Do not block plans merely because repo-reality facts are labeled Observed Evidence from a Codex Audit.

Block only when the evidence is overclaimed beyond repo reality, is ambiguous, conflicts with higher authority, or is used as acceptance, QA, OPS, PF09-drainage, closure, canon, or live-vendor proof without the owning source.

Confirmed.

Current PF07 was not completely wiped of vendor variables, but it is **not preserving the full deployed environment-variable matrix you just provided**, and it appears to have drift around the base-url key spelling.

What PF07 currently still has:

* `HDAPI_BASE_URL`  
* `HD_API_KEY`  
* `GEO_API_KEY`  
* `DEV_SAMPLER_URL`  
* `ALLOW_NETWORK`, `APP_ENV`, `LANG`, `LC_ALL`, `SAFE_MODE`, `TZ`  
* the Codespaces `DEV_SAMPLER_URL` binding  
* some Railway production resource names

PF07 currently records the vendor-ingest key as `HDAPI_BASE_URL`, and it separately says HumanDesignAPI v2 base URL and credential/secret-binding names are still open. It also records `DEV_SAMPLER_URL` for Codespaces as `http://127.0.0.1:8000/internal/dev/sampler`. PF05 likewise treats `HDAPI_BASE_URL` as the legacy BodyGraph base-url key in the current request-shaping section.

But your deployed Railway screenshot and environment matrix show **Prod and Dev using `HD_API_BASE_URL`**, while QA uses **`HDAPI_BASE_URL`**. That is mission-critical drift if PF07 does not preserve the exact per-environment key names and values-as-redacted. It also means any plan that assumes only `HDAPI_BASE_URL` exists is unsafe until the spelling difference is explicitly reconciled.

Below is the PF10 addendum to pin this immediately.

## **2.5) Mission-Critical Environment Variable Inventory Must Be Preserved in PF07**

Timestamp: 061626

Details: PO review identified major infrastructure documentation drift around deployed environment variables for `glow-hdengine-v2`.

Current PF07 partially records HD Engine infrastructure keys, including vendor-ingest names and the Codespaces `DEV_SAMPLER_URL` binding, but it does not preserve the full current deployed environment-variable matrix across Prod, Dev, and QA. It also records `HDAPI_BASE_URL` as the vendor base-url key, while the current deployed Railway Prod and Dev environments use `HD_API_BASE_URL`. QA currently uses `HDAPI_BASE_URL`.

This is mission-critical infrastructure documentation. These variables must never be lost, normalized silently, renamed casually, or treated as unknown when the PO has provided the deployed configuration.

### **Decision / rule / clarification**

The following environment-variable inventory is live PF10 truth until drained into PF07.

PF07 must be corrected to preserve the deployed environment-variable matrix exactly, with secret values redacted and key spellings preserved exactly as deployed.

This addendum does not expose secret values.

This addendum does not claim HumanDesignAPI v2 runtime conformance.

This addendum does not decide whether `HD_API_BASE_URL` or `HDAPI_BASE_URL` is the final canonical long-term key.

This addendum does decide that the currently deployed key names and environment bindings are mission-critical facts and must be preserved.

### **Current deployed environment variables**

#### **Prod — Railway**

`ALLOW_NETWORK=1`  
`APP_ENV=prod`  
`DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
`GEO_API_KEY={redacted}`  
`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`  
`HD_API_KEY={redacted}`  
`LANG=C`  
`LC_ALL=C`  
`SAFE_MODE=0`  
`TZ=UTC`

#### **Dev — Codex**

`ALLOW_NETWORK=0`  
`APP_ENV=dev`  
`DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
`GEO_API_KEY={redacted}`  
`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`  
`HD_API_KEY={redacted}`  
`LANG=C`  
`LC_ALL=C`  
`SAFE_MODE=1`  
`TZ=UTC`  
`PORT=8000`  
`DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`  
`DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

#### **QA — Codespaces**

`ALLOW_NETWORK=0`  
`APP_ENV=dev`  
`DATABASE_URL=postgresql://postgres:REDACTED@metro.proxy.rlwy.net:52353/railway`  
`DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`  
`DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`  
`GEO_API_KEY=REDACTED`  
`HDAPI_BASE_URL=https://api.humandesignapi.nl/v1`  
`HD_API_KEY=REDACTED`  
`LANG=C`  
`LC_ALL=C`  
`TZ=UTC`

### **Key-spelling drift finding**

The deployed environments currently show a base-url key spelling split:

* Prod and Dev: `HD_API_BASE_URL`  
* QA: `HDAPI_BASE_URL`  
* Current PF07/PF05 legacy documentation: `HDAPI_BASE_URL`

This is a documentation and possibly implementation-significant drift.

Until explicitly reconciled, plans, implementation prompts, QA plans, OPS tasks, and reviews must preserve the exact key spelling per environment.

No agent may silently normalize:

* `HD_API_BASE_URL` into `HDAPI_BASE_URL`  
* `HDAPI_BASE_URL` into `HD_API_BASE_URL`

Any implementation, QA, or OPS task that depends on the vendor base URL must state which key is being read in which environment, or must explicitly discover and record the binding.

### **Mission-critical preservation rule**

PF07 is the permanent home for infrastructure-owned environment facts.

PF07 must preserve:

* environment name  
* provider/context  
* key name  
* redacted value or value pattern  
* whether the key is required  
* whether the key is secret-bearing  
* whether the key is rails-related  
* whether the key is vendor-related  
* whether the key is DB-related  
* whether the key is dev-harness-related  
* whether the key is prod-only, dev-only, QA-only, or shared  
* any known spelling differences between environments

PF07 must not collapse this into names-only notes when a deployed environment matrix is known.

PF07 must not replace the matrix with `OPEN/TBD` for facts that the PO has supplied.

PF07 must not record a single canonical key spelling if the deployed environments currently differ.

### **Secret-handling rule**

Secret values must remain redacted.

Docs may record:

* key names  
* redacted value markers  
* URL hostnames and ports when provided by PO  
* non-secret base URLs  
* redacted database URL forms  
* environment/provider names  
* requiredness and ownership

Docs must not record:

* raw API keys  
* raw database passwords  
* raw bearer tokens  
* unredacted secrets  
* private payload values not required for infrastructure identity

### **Execution and review rule**

Plans and reviews must treat these environment variables as current deployed infrastructure facts until PF07 drains and supersedes them.

A plan or review must not claim any of the above variables are unknown merely because PF07 has not yet been drained.

A plan or review must not defer work merely because PF07 still says a value is `OPEN/TBD` when this PF10 addendum explicitly provides the current deployed binding.

A plan or review must not block on the key-spelling split by guessing a correction. The split must be handled explicitly as either:

* a compatibility requirement,  
* an OPS discovery fact,  
* an implementation migration,  
* a PF07 doc correction,  
* or a PO/Thoth decision.

### **HDE-EPIC034 application**

For HDE-EPIC034 and HumanDesignAPI vendor work:

* `HD_API_KEY` is the current deployed vendor credential key across Prod, Dev, and QA.  
* `GEO_API_KEY` is currently deployed where vendor/geocoding behavior may need it.  
* `HD_API_BASE_URL` is currently deployed in Prod and Dev.  
* `HDAPI_BASE_URL` is currently deployed in QA.  
* Both base-url key spellings must be preserved until deliberately reconciled.  
* Open-rails vendor testing may use the deployed Prod key set only when PO-authorized and secret-safe.  
* Closed-rails Dev and QA work must preserve `ALLOW_NETWORK`, `SAFE_MODE`, `APP_ENV`, `LANG`, `LC_ALL`, and `TZ` exactly as deployed.  
* `DB_BRIDGE_URL` and `DEV_SAMPLER_URL` are known current non-prod/dev-harness bridge bindings and must not be treated as unknown for Dev/QA planning.

### **Corrective action posture**

This PF10 addendum immediately corrects the live truth gap.

Permanent drainage is still required into PF07, but PF07 drainage is not a blocker to using these facts now.

Any current plan, review, implementation prompt, QA plan, OPS task, or Codex prompt that depends on these variables should treat this PF10 addendum as the current source of truth until PF07 is corrected.

### **Required PF07 drain target**

Drain into PF07 — Glow Infrastructure.

Required section targets:

* HD Engine environment variables  
* Production Railway environment  
* Dev/Codex environment  
* QA/Codespaces environment  
* Vendor-ingest keys  
* DB bridge keys  
* Dev sampler harness keys  
* Rails/determinism keys  
* HumanDesignAPI legacy v1 base-url posture  
* HumanDesignAPI v2 pending mapping posture

Required PF07 content:

* full Prod matrix above  
* full Dev matrix above  
* full QA matrix above  
* exact spelling distinction between `HD_API_BASE_URL` and `HDAPI_BASE_URL`  
* redacted secret handling rules  
* explicit statement that current v1 deployed base URL is `https://api.humandesignapi.nl/v1`  
* explicit statement that current deployed vendor credential key is `HD_API_KEY`  
* explicit statement that `GEO_API_KEY` is deployed and must be preserved  
* explicit statement that `DB_BRIDGE_URL` and `DEV_SAMPLER_URL` are deployed non-prod/QA support bindings  
* explicit statement that PF07 must not downgrade supplied deployed facts to `OPEN/TBD`

### **Additional drain targets**

#### **PF05 — HDE CLI-API-Vendor Ref**

Drain target intent:

* Reconcile legacy vendor base-url key usage between `HDAPI_BASE_URL` and `HD_API_BASE_URL`.  
* State whether both spellings are supported, whether one is canonical, or whether a migration is required.  
* Preserve current deployed reality while deciding request-shaping byte behavior.  
* Do not guess the long-term key spelling.

#### **PF04 — HDE Governance**

Drain target intent:

* Preserve rails and environment-key posture for `ALLOW_NETWORK`, `SAFE_MODE`, and `APP_ENV`.  
* Clarify that environment-variable documentation drift is a governance-relevant operational risk when it affects rails, secrets, public/private posture, or acceptance evidence.

#### **PF19 — Glow QA Guide**

Drain target intent:

* Require Live QA and QA planning to capture or reference the exact environment-variable key names used in the executing environment.  
* Treat mismatched expected key spelling as infrastructure/tooling ambiguity, not as behavior failure, until resolved.

#### **PF27 — Canon Plan Templates**

Drain target intent:

* Require plans that depend on infrastructure variables to preserve exact key spelling and environment context.  
* Prevent templates from collapsing deployed environment matrices into vague `OPEN/TBD` placeholders when PO-supplied facts exist.

#### **PF12 — HDE Schemas and Artifacts**

Drain target intent:

* Define safe redacted environment snapshot posture for governed evidence.  
* Preserve key names, redacted values, provider/environment labels, and hash/path-proof posture where environment evidence is captured.

#### **PF06 — Epic Process Guide**

Drain target intent:

* Treat environment-variable preservation as an OPS/documentation truth responsibility.  
* Require PO-provided deployed environment facts to be routed into PF10/PF07 rather than repeatedly rediscovered.

#### **PF23 — Reality Audits**

Drain target intent:

* Future reality audits should check PF07 environment-variable documentation against observed repo/devcontainer/Railway/Codespaces state where available.  
* Drift between PF07 and deployed variables should be reported as infrastructure reality drift.

### **Immediate operating rule**

Until drained, this PF10 addendum is the live rule:

The environment-variable matrix in this addendum is the current known deployed truth for HDE environment planning.

Do not lose it.

Do not normalize it.

Do not replace it with `OPEN/TBD`.

Do not treat these variables as unknown.

Do not silently change `HD_API_BASE_URL` to `HDAPI_BASE_URL` or vice versa.

Use the exact key name for the exact environment until PF07 and PF05 explicitly reconcile the key-spelling split.

### **Final authority**

This addendum is live PF10 truth until drained.

PF07 remains the permanent home for this information, but the current deployed environment-variable matrix is now protected in PF10 and must not be dropped from future planning, implementation, QA, OPS, review, or documentation-drainage work.

## **2.6) HD API Base URL Environment Variable Name Decision**

Timestamp: 061626

Details: The prior PF10 environment-variable preservation addendum recorded a live key-name split:

* Prod and Dev currently use `HD_API_BASE_URL`  
* QA currently uses `HDAPI_BASE_URL`  
* PF07/PF05 had historically documented `HDAPI_BASE_URL`

That split is now decided.

### **Decision**

The canonical environment variable name for the HumanDesignAPI base URL is:

`HD_API_BASE_URL`

This is the required canonical name going forward.

The spelling `HDAPI_BASE_URL` is deprecated and must be treated as legacy drift.

### **Canonical vendor environment-variable names**

The canonical vendor-related environment variable names are:

`HD_API_BASE_URL`

`HD_API_KEY`

`GEO_API_KEY`

These names must be preserved exactly.

Do not normalize them.

Do not collapse them.

Do not rename them without an explicit PF10 or PF-canon decision.

### **Current deployed-state interpretation**

The current deployed-state record is interpreted as follows:

#### **Prod — Railway**

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

Status: canonical and correct.

#### **Dev — Codex**

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

Status: canonical and correct.

#### **QA — Codespaces**

`HDAPI_BASE_URL=https://api.humandesignapi.nl/v1`

Status: legacy drift; must be migrated to `HD_API_BASE_URL`.

### **QA/Codespaces migration decision**

QA/Codespaces should be updated to use:

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

The legacy key:

`HDAPI_BASE_URL`

should be removed after the canonical key is confirmed present and working.

If immediate removal is risky, `HDAPI_BASE_URL` may remain temporarily as a compatibility alias, but it must be documented as deprecated drift and not treated as the canonical key.

### **Runtime / implementation compatibility posture**

Implementation may support a temporary compatibility fallback from `HDAPI_BASE_URL` to `HD_API_BASE_URL` only to avoid breaking existing QA/Codespaces execution while the environment is migrated.

The allowed resolution order is:

1. Read `HD_API_BASE_URL`  
2. If absent, read deprecated alias `HDAPI_BASE_URL`  
3. If both exist and values match, use `HD_API_BASE_URL`  
4. If both exist and values differ, fail closed with a configuration ambiguity

No code, plan, QA run, OPS task, or review may silently prefer the deprecated alias over the canonical key.

No code, plan, QA run, OPS task, or review may silently use two different values.

### **Documentation posture**

PF07 must document `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL variable.

PF07 may document `HDAPI_BASE_URL` only as a deprecated legacy alias observed in QA/Codespaces before migration.

PF05 must use `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL variable for vendor request-shaping and vendor-client posture.

PF05 may mention `HDAPI_BASE_URL` only as deprecated legacy spelling, if compatibility behavior exists or is needed during migration.

### **Updated mission-critical environment-variable inventory**

The protected vendor and supporting variables are:

#### **Prod — Railway**

`ALLOW_NETWORK=1`

`APP_ENV=prod`

`DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`

`GEO_API_KEY={redacted}`

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

`HD_API_KEY={redacted}`

`LANG=C`

`LC_ALL=C`

`SAFE_MODE=0`

`TZ=UTC`

#### **Dev — Codex**

`ALLOW_NETWORK=0`

`APP_ENV=dev`

`DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`

`GEO_API_KEY={redacted}`

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

`HD_API_KEY={redacted}`

`LANG=C`

`LC_ALL=C`

`SAFE_MODE=1`

`TZ=UTC`

`PORT=8000`

`DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`

`DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

#### **QA — Codespaces, target canonical state**

`ALLOW_NETWORK=0`

`APP_ENV=dev`

`DATABASE_URL=postgresql://postgres:REDACTED@metro.proxy.rlwy.net:52353/railway`

`DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`

`DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

`GEO_API_KEY=REDACTED`

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

`HD_API_KEY=REDACTED`

`LANG=C`

`LC_ALL=C`

`TZ=UTC`

### **Deprecated QA legacy key**

The following key is known legacy drift in QA/Codespaces:

`HDAPI_BASE_URL=https://api.humandesignapi.nl/v1`

Disposition:

Deprecated alias.

Migration target:

`HD_API_BASE_URL=https://api.humandesignapi.nl/v1`

Do not use `HDAPI_BASE_URL` in new plans, implementation prompts, QA plans, OPS tasks, or PF documentation except to identify and remove or temporarily bridge legacy drift.

### **Planning and review rule**

Plans, implementation prompts, QA plans, OPS tasks, and reviews must use:

`HD_API_BASE_URL`

They must not use:

`HDAPI_BASE_URL`

unless the text is explicitly discussing deprecated legacy drift, temporary compatibility fallback, or QA/Codespaces migration.

If a plan or review sees `HDAPI_BASE_URL`, it must classify it as one of:

* deprecated alias observed  
* compatibility fallback  
* migration target  
* drift requiring OPS/doc update

It must not classify `HDAPI_BASE_URL` as the canonical key.

### **OPS discovery / migration rule**

An OPS task may be created to confirm or update environment-variable bindings.

For this specific drift, a bounded OPS task may confirm:

* whether QA/Codespaces currently has `HD_API_BASE_URL`  
* whether QA/Codespaces still has `HDAPI_BASE_URL`  
* whether both keys exist  
* whether the values match  
* whether `HDAPI_BASE_URL` can be removed safely  
* whether implementation currently reads one or both names  
* whether docs, plans, or QA artifacts still reference the deprecated name

The OPS task must not expose secret values.

The OPS task may report redacted status only.

### **HDE-EPIC034 application**

For HDE-EPIC034:

* Use `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key.  
* Use `HD_API_KEY` as the canonical HumanDesignAPI credential key.  
* Use `GEO_API_KEY` when geocoding/vendor route behavior requires it.  
* Treat `HDAPI_BASE_URL` as QA/Codespaces legacy drift.  
* Do not defer request-shaping, vendor-seam, open-rails, or OPS discovery work merely because this key-name drift exists.  
* Route the key-name check or migration through OPS discovery or OPS change if needed.  
* If implementation needs temporary compatibility, use canonical-first fallback and fail closed if both keys exist with different values.

### **Update to prior PF10 addendum**

This addendum updates and supersedes the unresolved “key-spelling drift finding” language in the prior environment-variable preservation addendum.

The prior language said the deployed environments showed a base-url key spelling split and that the final canonical key had not yet been decided.

The updated decision is:

`HD_API_BASE_URL` is canonical.

`HDAPI_BASE_URL` is deprecated legacy drift.

QA/Codespaces must migrate to `HD_API_BASE_URL`.

### **Required PF07 drain target**

Drain into PF07 — Glow Infrastructure.

Required PF07 updates:

* Record `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key.  
* Record `HD_API_KEY` as the canonical HumanDesignAPI credential key.  
* Record `GEO_API_KEY` as the canonical geocoding/vendor-support key when needed.  
* Preserve the full Prod, Dev, and QA environment matrices from this PF10 addendum.  
* Update QA/Codespaces target state to `HD_API_BASE_URL`.  
* Record `HDAPI_BASE_URL` only as deprecated legacy QA/Codespaces drift.  
* Document canonical-first fallback behavior only if implementation supports it.  
* State that both keys with different values is a configuration ambiguity and must fail closed.  
* State that secret values must remain redacted.  
* State that PO-provided deployed environment facts must not be downgraded to `OPEN/TBD`.

### **Required PF05 drain target**

Drain into PF05 — HDE CLI-API-Vendor Ref.

Required PF05 updates:

* Replace canonical vendor base-url references using `HDAPI_BASE_URL` with `HD_API_BASE_URL`.  
* Preserve `HDAPI_BASE_URL` only as deprecated alias / legacy drift if compatibility behavior is documented.  
* State that HumanDesignAPI request shaping must read canonical `HD_API_BASE_URL`.  
* State that `HD_API_KEY` is the canonical vendor credential key.  
* State that `GEO_API_KEY` is preserved where geocoding behavior requires it.  
* State that `HD_API_BASE_URL` currently points to `https://api.humandesignapi.nl/v1` for the current deployed legacy vendor base URL.  
* Do not silently treat the v1 base URL as v2 conformance.

### **Required PF14 drain target**

Drain into PF14 — HDE Mechanics Guide.

Required PF14 updates:

* Use `HD_API_BASE_URL` as the canonical mechanics-facing HumanDesignAPI base URL key.  
* Record that `HDAPI_BASE_URL` is deprecated drift, not canonical mechanics language.  
* Clarify any fallback resolution mechanics if implemented.  
* Preserve fail-closed behavior if canonical and deprecated values conflict.

### **Required PF27 drain target**

Drain into PF27 — Canon Plan Templates.

Required PF27 updates:

* Plans must preserve exact environment-variable key spelling.  
* Plans must use canonical `HD_API_BASE_URL`.  
* Plans must not introduce `HDAPI_BASE_URL` except as deprecated drift or temporary compatibility notation.  
* Plans must route environment key-name uncertainty through OPS discovery rather than deferral.

### **Required PF19 drain target**

Drain into PF19 — Glow QA Guide.

Required PF19 updates:

* QA plans must use `HD_API_BASE_URL` as canonical.  
* QA may check for deprecated `HDAPI_BASE_URL` only as drift/migration evidence.  
* QA must not treat a deprecated alias as canonical.  
* QA must classify conflicting values between canonical and deprecated keys as configuration ambiguity, not product behavior failure.

### **Required PF12 drain target**

Drain into PF12 — HDE Schemas and Artifacts.

Required PF12 updates:

* Environment snapshots and governed evidence summaries must preserve exact key names.  
* Redacted environment evidence should record canonical `HD_API_BASE_URL`.  
* Deprecated `HDAPI_BASE_URL` may appear only as observed drift or alias evidence.  
* Secret values remain redacted.

### **Required PF06 drain target**

Drain into PF06 — Epic Process Guide.

Required PF06 updates:

* Environment-variable key-name drift should be handled through OPS discovery or OPS change, not deferral.  
* PO-provided deployed environment facts should be routed into PF10 and PF07.  
* Review and closeout should distinguish canonical key migration from implementation behavior failure.

### **Required PF04 drain target**

Drain into PF04 — HDE Governance.

Required PF04 updates:

* `ALLOW_NETWORK`, `SAFE_MODE`, and `APP_ENV` remain rails-governance keys.  
* `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` are infrastructure/vendor configuration keys, not acceptance tokens.  
* Key-name drift can be governance-relevant when it affects rails, secrets, or acceptance evidence.

### **Immediate operating rule**

Until drained, this PF10 addendum is the live rule:

Use `HD_API_BASE_URL`.

Do not use `HDAPI_BASE_URL` except as deprecated legacy drift or temporary compatibility alias.

Prod and Dev are already canonical.

QA/Codespaces must migrate from `HDAPI_BASE_URL` to `HD_API_BASE_URL`.

Do not silently normalize key names.

Do not treat `HD_API_BASE_URL` as unknown.

Do not defer work because of this key-name drift.

Route discovery, confirmation, or migration through OPS.

If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist and differ, fail closed and record configuration ambiguity.

### **Final authority**

PF10 is the live source of truth for this decision until drained.

The canonical HumanDesignAPI base URL environment variable is:

`HD_API_BASE_URL`

Validated.

The live HumanDesignAPI docs show that **v2 uses the API key as a Bearer token in the `Authorization` header**. The v2 full-chart example sends `Authorization: Bearer <token>` and the Authorizations section says the API key is used as a Bearer token in the Authorization header. It also shows `HD-Geocode-Key` as a separate required header for that location-based chart request. ([Human Design API](https://docs.humandesignapi.nl/api-reference/charts/generate-a-full-chart))

The v1 legacy BodyGraph docs show the old header form: `HD-Api-Key: <api-key>` plus `HD-Geocode-Key: <api-key>`. The v1 Authorizations section names `HD-Api-Key` as the required Human Design API key header. ([Human Design API](https://docs.humandesignapi.nl/api-reference/bodygraph/generate-a-complete-bodygraph))

Current PF05 already partially records this direction: it says the current legacy BodyGraph example is **not** a v2 request example, and that HumanDesignAPI v2 request examples, including auth headers, remain pending until derived from the governed contract inventory and drained through the PF05 v2 contract update. PF05 also states that the future v2 request contract must define “v2 auth headers, including `Authorization: Bearer` and `HD-Geocode-Key` conditions.”

So: **the change is validated, but it should be pinned in PF10 now** so it cannot be lost or blurred during HDE-EPIC034 request-shaping work.

## **2.7) HumanDesignAPI v2 Uses Authorization Bearer; v1 Uses HD-Api-Key Header**

Timestamp: 061626

Details: PO review validated a mission-critical HumanDesignAPI contract difference between legacy v1 and recommended v2 routes.

HumanDesignAPI v2 chart routes use the API key as a Bearer token in the `Authorization` header.

HumanDesignAPI v1 BodyGraph routes use the legacy `HD-Api-Key` request header.

This difference must be preserved in planning, implementation, OPS discovery, open-rails testing, QA, PF05 drainage, PF07 drainage, and PF12 evidence semantics.

### **Decision / rule / clarification**

The canonical secret environment variable remains:

`HD_API_KEY`

That environment secret is projected differently by vendor API version:

* v1 legacy BodyGraph request header: `HD-Api-Key: <redacted>`  
* v2 chart request header: `Authorization: Bearer <redacted>`

The geocoding key remains:

`GEO_API_KEY`

When the route requires geocoding, it is projected as:

`HD-Geocode-Key: <redacted>`

Do not confuse the environment variable name with the outbound vendor header name.

Do not use `HD-Api-Key` as the v2 auth header.

Do not use `Authorization: Bearer` as the v1 legacy BodyGraph auth header unless vendor docs later change and PF10 or PF05 records that change.

### **Validated vendor-doc basis**

Validated current vendor-doc facts:

* v2 full chart route: `POST /v2/charts`  
* v2 auth header: `Authorization: Bearer <token>`  
* v2 geocode header when required: `HD-Geocode-Key: <api-key>`  
* v2 docs describe `Authorization` as required and as “API key used as Bearer token in the Authorization header.”  
* v1 complete BodyGraph route: `POST /v1/bodygraphs`  
* v1 auth header: `HD-Api-Key: <api-key>`  
* v1 geocode header: `HD-Geocode-Key: <api-key>`  
* v1 docs describe `HD-Api-Key` as required and as the Human Design API key header.

### **Header mapping table**

| Vendor API family | Route family | Credential environment variable | Outbound vendor auth header | Geocode environment variable | Outbound geocode header |
| ----- | ----- | ----- | ----- | ----- | ----- |
| HumanDesignAPI v1 legacy BodyGraph | `/v1/bodygraphs` and legacy v1 BodyGraph family | `HD_API_KEY` | `HD-Api-Key: <redacted>` | `GEO_API_KEY` when required | `HD-Geocode-Key: <redacted>` |
| HumanDesignAPI v2 chart routes | `/v2/charts`, `/v2/charts/simple`, `/v2/charts/coordinates` | `HD_API_KEY` | `Authorization: Bearer <redacted>` | `GEO_API_KEY` when required | `HD-Geocode-Key: <redacted>` |

### **Implementation rule**

Any HDE v2 request-shaping implementation must construct the v2 auth header as:

`Authorization: Bearer <HD_API_KEY value>`

It must not construct v2 auth as:

`HD-Api-Key: <HD_API_KEY value>`

Any legacy v1 request-shaping implementation must preserve legacy auth as:

`HD-Api-Key: <HD_API_KEY value>`

It must not silently migrate legacy v1 to Bearer auth unless PF10 or PF05 later records vendor-doc support for that change.

### **Secret handling**

Docs, logs, evidence, QA plans, implementation plans, OPS reports, Codex prompts, and closeout records may name header names and environment-variable names.

They must not record raw secret values.

Allowed:

* `HD_API_KEY`  
* `GEO_API_KEY`  
* `Authorization: Bearer <redacted>`  
* `HD-Api-Key: <redacted>`  
* `HD-Geocode-Key: <redacted>`

Forbidden:

* raw API key values  
* raw Bearer token values  
* raw geocode key values  
* full unredacted request headers  
* vendor request or response payload dumps outside an explicitly approved governed evidence shape

### **QA and OPS rule**

QA and OPS may verify header posture only in secret-safe form.

QA and OPS may record:

* v1 used `HD-Api-Key` header name  
* v2 used `Authorization` Bearer header name  
* `HD-Geocode-Key` was present when required  
* secret presence was confirmed  
* raw values were redacted  
* open-rails smoke result status or vendor error class, when safe

QA and OPS must not record raw header values.

### **Open-rails testing impact**

Open-rails v2 smoke must use:

`Authorization: Bearer <redacted>`

for the vendor API key.

It must not use:

`HD-Api-Key: <redacted>`

for v2.

A v2 open-rails failure caused by sending `HD-Api-Key` instead of `Authorization: Bearer` must be classified as a request-shaping/auth-header defect or OPS setup defect, not as vendor unavailability.

A v1 legacy BodyGraph open-rails failure caused by sending Bearer auth instead of `HD-Api-Key` must be classified as a legacy request-shaping/auth-header defect or OPS setup defect, not as vendor unavailability.

### **HDE-EPIC034 application**

For HDE-EPIC034:

* HDE-FERM007.2 request shaping must include the v1/v2 auth-header distinction.  
* HDE-FERM007.5 deterministic shaping proof must verify that v2 shaping uses Bearer auth and v1 shaping uses legacy `HD-Api-Key`.  
* HDE-FERM008.2 PO-only open-rails smoke must use Bearer auth for v2 chart routes.  
* HDE-FERM008.3 error/retry/rate-limit mapping must not blur authentication-header defects with vendor runtime failures.  
* HDE-FERM008.5 evidence-loop closure must preserve header-family identity in secret-safe evidence if live conformance depends on it.

### **Interaction with HD API base URL key decision**

This addendum does not change the environment-variable decision that `HD_API_BASE_URL` is the canonical base URL key.

The canonical vendor environment keys remain:

`HD_API_BASE_URL`

`HD_API_KEY`

`GEO_API_KEY`

This addendum clarifies only outbound request header projection:

* `HD_API_KEY` becomes `HD-Api-Key` for v1 legacy BodyGraph requests.  
* `HD_API_KEY` becomes `Authorization: Bearer` for v2 chart requests.  
* `GEO_API_KEY` becomes `HD-Geocode-Key` when geocoding is required.

### **Review and planning rule**

Any plan, implementation prompt, QA guide, QA plan, OPS task, or Codex prompt that discusses HumanDesignAPI v2 request shaping must explicitly preserve the v2 Bearer auth posture.

Any plan, implementation prompt, QA guide, QA plan, OPS task, or Codex prompt that discusses legacy v1 BodyGraph request shaping must explicitly preserve the v1 `HD-Api-Key` posture.

Do not write generic “HD API key header” language where v1/v2 distinction matters.

Use exact header names.

### **Required drain targets**

#### **PF05 — HDE CLI-API-Vendor Ref**

Drain target intent:

* Record the v1/v2 auth-header distinction in the vendor request-shaping section.  
* v1 legacy BodyGraph: `HD-Api-Key`.  
* v2 chart routes: `Authorization: Bearer`.  
* Shared geocode header where required: `HD-Geocode-Key`.  
* State that `HD_API_KEY` is the environment secret projected into either header depending on API family.  
* State that v2 must not use `HD-Api-Key`.  
* State that v1 must not be silently migrated to Bearer auth without vendor-doc proof and PF10/PF05 update.  
* Preserve the current PF05 distinction between contract inventory, request shaping, runtime conformance, and live conformance.

#### **PF07 — Glow Infrastructure**

Drain target intent:

* Preserve `HD_API_KEY` as the canonical vendor API key environment variable.  
* Preserve `GEO_API_KEY` as the geocoding key.  
* Preserve `HD_API_BASE_URL` as the canonical vendor base URL environment variable.  
* Clarify that environment variable names are not necessarily outbound vendor header names.  
* Add secret-safe notation for v1 and v2 header projection.  
* Ensure deployed environment matrices do not imply `HD_API_KEY` is sent under the same header for v1 and v2.

#### **PF12 — HDE Schemas and Artifacts**

Drain target intent:

* Add or update HDAPI v2 evidence-family semantics so request-shaping evidence can prove auth-header family without exposing secret values.  
* Evidence may record `Authorization: Bearer <redacted>` as header shape.  
* Evidence may record `HD-Api-Key: <redacted>` for legacy v1 only.  
* Evidence may record `HD-Geocode-Key: <redacted>` where geocode is required.  
* Raw header values remain forbidden.

#### **PF19 — Glow QA Guide**

Drain target intent:

* QA proof for v2 request shaping or open-rails smoke must distinguish auth-header family.  
* QA should classify wrong auth-header family as request-shaping/auth setup failure.  
* QA must not log or persist raw header values.  
* QA plans may require secret-presence confirmation and redacted header-shape confirmation.

#### **PF27 — Canon Plan Templates**

Drain target intent:

* Plans involving vendor request shaping must include version-specific auth-header posture when relevant.  
* Do not allow generic vendor-auth wording to hide v1/v2 differences.  
* Require exact header names in planning text when the distinction affects implementation or QA.

#### **PF04 — HDE Governance**

Drain target intent:

* Reinforce that header names may be recorded, but header values must not be logged.  
* Treat auth-header family mismatch as a governance-relevant request-shaping and secret-safety issue when it affects live vendor behavior.  
* Clarify that `HD_API_KEY`, `GEO_API_KEY`, and `HD_API_BASE_URL` are infrastructure/vendor config keys, not acceptance tokens.

#### **PF14 — HDE Mechanics Guide**

Drain target intent:

* Reflect that v2 request-shaping mechanics project `HD_API_KEY` into `Authorization: Bearer`.  
* Reflect that v1 legacy mechanics project `HD_API_KEY` into `HD-Api-Key`.  
* Preserve shared geocode-key mechanics where required.  
* Ensure response-mapping and source-selection mechanics do not collapse v1 and v2 auth behavior.

#### **PF09.5 — HDE Build Checklist Fermentation**

Drain target intent:

* HDE-FERM007.2 request shaping should explicitly require the v1/v2 auth-header distinction.  
* HDE-FERM007.5 deterministic shaping proof should preserve auth-header family.  
* HDE-FERM008.2 open-rails smoke should use v2 Bearer auth for v2 routes.  
* HDE-FERM008.3 should distinguish auth-header mismatch from vendor availability or rate-limit failures.

### **Immediate operating rule**

Until drained, this PF10 addendum is live truth:

HumanDesignAPI v2 chart routes use:

`Authorization: Bearer <redacted>`

HumanDesignAPI v1 legacy BodyGraph routes use:

`HD-Api-Key: <redacted>`

Routes requiring geocoding use:

`HD-Geocode-Key: <redacted>`

The same `HD_API_KEY` secret environment variable supplies the vendor API key, but the outbound header differs by API version.

Do not blur v1 and v2 auth headers.

Do not log raw values.

Do not defer implementation or QA because this fact was not previously drained; this addendum records the decision now.

\<eof\>