# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.5.7  
Effective Date: 2026.06.19

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
2.8) PR-01 HDE-EPIC034  
2.9) OPS-01 HDE-EPIC034  
2.10) PR-02 HDE-EPIC034  
2.11) PR-03 HDE-EPIC034  
2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation  
2.13) ADR — HD Engine Owns Vendor Acquisition, BodyGraph Persistence, Retrieval, and Compute for Future Glow App Integration  
2.14) W-001 Remediation PR-04 HDE-EPIC034  
2.15) W-002 Remediation PR-04 HDE-EPIC034  
2.16) W-003 Remediation PR-04 HDE-EPIC034

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

## 2.8) PR-01 HDE-EPIC034

Review Summary

* The PR implements HDE-EPIC034 PR-01 source-selection evidence generation from the governed HDAPI contract map, with explicit v2 chart variants and v1 BodyGraph legacy route groups.  
* The PR aligns with the Approved Plan for PR-01: it targets HDE-FERM007.1 only and does not implement request shaping, response mapping, adapter/presenter boundary proof, open-rails vendor smoke, public Reader changes, new HTTP homes, or AI scope.  
* The PR adds source-selection, v1 legacy guard, source-selection check-log, current-epic doc-delta, human index, machine mirror, hash, and path-proof evidence.  
* The PR includes remediation for prior bugs and CI drift: auth/geocode preservation, public-docs refresh posture, PF12 canonical artifact-key binding, stale EPIC034-specific key filtering, mixed-auth rejection, source-authority validation, geocode requirement validation, path-proof chronology, removal of an unsupported `TESTS_PASS_OK` token from a generated check log, and `ORIENTATION_DRIFT`.  
* Final PR Artifacts record the relevant validation commands as passed, including generator refresh, evidence index refresh/check, orientation demo refresh/check, targeted pytest, canonical JSON check, evidence path validation, mirror schema, evidence-index hash, and LF checks.  
* Diff review covers all 58 final git patch hunks through 40 DR items.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.1.  
* The review supports a PF09 subtask status action of change to Done for HDE-FERM007.1 only; no parent HDE-FERM007 status change is recommended.  
* RCA is included because PR Artifacts explicitly include bug, regression, and CI-failure remediation history.

Diff Review

1. DR-001  
   Change summary: Updates `artifacts/evidence_index.jsonl`, including refreshed historical rows and new HDE-EPIC034 source-selection, doc-delta, and index/mirror rows.  
   Risk assessment: Medium  
   Why it matters: This is the central machine mirror update, and it must preserve canonical PF12 evidence binding without duplicate stale EPIC034-specific keys.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → Diff → `@@ -62,51 +62,51 @@`; PR Artifacts → Diff → `@@ -123,91 +123,91 @@`; PR Artifacts → Diff → `@@ -235,94 +235,99 @@`; PR Artifacts → Diff → `@@ -331,30 +336,30 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
2. DR-002  
   Change summary: Updates `artifacts/evidence_index.jsonl.path_proof.txt` for the refreshed machine mirror.  
   Risk assessment: Low  
   Why it matters: The machine mirror path proof must match the updated mirror bytes and self-record semantics.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → Diff → `@@ -1,6 +1,6 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
3. DR-003  
   Change summary: Updates `artifacts/evidence_index.jsonl.sha256`.  
   Risk assessment: Low  
   Why it matters: The machine mirror checksum sidecar must track the updated machine mirror.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
4. DR-004  
   Change summary: Updates `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.  
   Risk assessment: Low  
   Why it matters: The checksum sidecar path proof must stay coherent with the updated sidecar bytes.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
5. DR-005  
   Change summary: Refreshes `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`.  
   Risk assessment: Medium  
   Why it matters: This is unrelated historical evidence churn, acceptable only because the evidence index and path-proof checks passed.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
6. DR-006  
   Change summary: Refreshes `artifacts/narratives/router/parity_abba.log.path_proof.txt`.  
   Risk assessment: Medium  
   Why it matters: This is unrelated historical evidence churn, acceptable only because the evidence index and path-proof checks passed.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
7. DR-007  
   Change summary: Adds `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`.  
   Risk assessment: Low  
   Why it matters: This is the primary HDE-FERM007.1 source-selection snapshot required by the Approved Plan.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; PR Artifacts → Diff → `@@ -0,0 +1 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
8. DR-008  
   Change summary: Adds `artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`.  
   Risk assessment: Low  
   Why it matters: The source-selection snapshot must be path-proven for governed evidence acceptance.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
9. DR-009  
   Change summary: Adds `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`.  
   Risk assessment: Low  
   Why it matters: This is the required guard proving v1 BodyGraph routes remain explicit legacy behavior.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; PR Artifacts → Diff → `@@ -0,0 +1,14 @@`  
   Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
10. DR-010  
    Change summary: Adds `artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The v1 legacy guard log must be path-proven for governed evidence acceptance.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
11. DR-011  
    Change summary: Refreshes `artifacts/writer/conjunction_write_readback.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated path-proof refresh increases evidence churn but is covered by validation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
12. DR-012  
    Change summary: Refreshes `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated path-proof refresh increases evidence churn but is covered by validation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
13. DR-013  
    Change summary: Refreshes `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This is unrelated historical doc-delta path-proof churn; current-epic doc-delta evidence is added separately.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
14. DR-014  
    Change summary: Adds `audit/docdeltas/hde-epic034_doc_deltas.md`.  
    Risk assessment: Low  
    Why it matters: This supplies the current-epic draft/staging doc-delta surface required for `DOC_DELTA_PRESENT_OK`.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md b/audit/docdeltas/hde-epic034_doc_deltas.md`; PR Artifacts → Diff → `@@ -0,0 +1,29 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Acceptance tokens  
15. DR-015  
    Change summary: Adds `audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The draft/staging doc-delta surface must be path-proven.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Acceptance tokens  
16. DR-016  
    Change summary: Refreshes `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated path-proof churn is acceptable only because validation passed.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
17. DR-017  
    Change summary: Refreshes `audit/gates/narratives/pack_identity.txt.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated path-proof churn is acceptable only because validation passed.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
18. DR-018  
    Change summary: Refreshes `audit/gates/narratives/registry.diff.json.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated path-proof churn is acceptable only because validation passed.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
19. DR-019  
    Change summary: Updates `audit/gates/topology/orientation_demo.txt`.  
    Risk assessment: Low  
    Why it matters: This remediates orientation evidence drift after adding governed artifacts.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt b/audit/gates/topology/orientation_demo.txt`; PR Artifacts → Diff → `@@ -1,4 +1,4 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Basic QA check  
20. DR-020  
    Change summary: Updates `audit/gates/topology/orientation_demo.txt.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The refreshed orientation artifact must have coherent path-proof data.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Basic QA check  
21. DR-021  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
22. DR-022  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
23. DR-023  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
24. DR-024  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
25. DR-025  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
26. DR-026  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
27. DR-027  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
28. DR-028  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
29. DR-029  
    Change summary: Refreshes `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`.  
    Risk assessment: Medium  
    Why it matters: This unrelated historical path-proof refresh is covered by validation and does not expand PR-01 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
30. DR-030  
    Change summary: Adds `audit/qa/hde-epic034/00_meta/doc_deltas.md`.  
    Risk assessment: Low  
    Why it matters: This supplies the epic-scoped QA meta doc-delta capture surface required for `DOC_DELTA_PRESENT_OK`.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md b/audit/qa/hde-epic034/00_meta/doc_deltas.md`; PR Artifacts → Diff → `@@ -0,0 +1,29 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Acceptance tokens  
31. DR-031  
    Change summary: Adds `audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The epic-scoped QA meta doc-delta capture surface must be path-proven.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Acceptance tokens  
32. DR-032  
    Change summary: Adds `audit/qa/hde-epic034/pr-01/source_selection_check.log`.  
    Risk assessment: Low  
    Why it matters: The PR-scoped check log proves route-family, auth-family, geocode, source-authority, and no-live-vendor posture.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log b/audit/qa/hde-epic034/pr-01/source_selection_check.log`; PR Artifacts → Diff → `@@ -0,0 +1,19 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
33. DR-033  
    Change summary: Adds `audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The PR-scoped check log must be path-proven.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
34. DR-034  
    Change summary: Updates `docs/evidence/INDEX.json`.  
    Risk assessment: Medium  
    Why it matters: This is the human evidence index binding for all new PR-01 governed artifacts.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → Diff → `@@ -1 +1 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
35. DR-035  
    Change summary: Updates `docs/evidence/INDEX.json.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The human index path proof must match updated index bytes.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
36. DR-036  
    Change summary: Updates `docs/evidence/INDEX.sha256`.  
    Risk assessment: Low  
    Why it matters: The human index hash sentinel must match updated index bytes.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
37. DR-037  
    Change summary: Updates `docs/evidence/INDEX.sha256.path_proof.txt`.  
    Risk assessment: Low  
    Why it matters: The human index hash sentinel path proof must match the updated checksum sidecar.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs  
38. DR-038  
    Change summary: Adds tests for source-selection snapshot derivation, route distinction, v1 guard, check-log output, missing-route fail-closed behavior, public-docs refresh posture, mixed auth rejection, source-authority drift, non-coordinate geocode drift, and geocode auth drift.  
    Risk assessment: Low  
    Why it matters: The test additions cover the planned source-selection behavior and all recorded remediation bugs.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -240,25 +240,205 @@ def test_unavailable_suspect_openapi_does_not_block_contract_generation() -> Non`  
    Approved Plan linkage: Approved Plan → PR-01 — Basic QA check  
39. DR-039  
    Change summary: Updates `tools/evidence/generate_hdapi_v2_contract_inventory.py` to emit EPIC034 PR-01 source-selection artifacts and fail closed on missing routes, auth-family drift, geocode drift, source-authority drift, and false network-posture logging.  
    Risk assessment: Medium  
    Why it matters: This is the primary implementation logic for HDE-FERM007.1 and must remain evidence-generation only, not runtime request shaping.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -11,80 +11,93 @@ from __future__ import annotations`; PR Artifacts → Diff → `@@ -534,50 +547,232 @@ def build_contract_map(produced: str, fetched: dict[str, dict[str, Any]], rows:`; PR Artifacts → Diff → `@@ -679,50 +874,57 @@ def write_baseline_pointer_artifacts(produced: str, acceptance: dict[str, Any])`  
    Approved Plan linkage: Approved Plan → PR-01 — Implementation requirements  
40. DR-040  
    Change summary: Updates `tools/evidence/update_evidence_index.py` to register canonical HDE-EPIC034 PR-01 evidence rows, filter superseded keys, include doc-delta surfaces, refresh path proofs, and load the new entries into the human index.  
    Risk assessment: Medium  
    Why it matters: This is the primary evidence-index binding change and must maintain canonical row identity, path-proof chronology, and parity.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py`; PR Artifacts → Diff → `@@ -483,50 +483,55 @@ EPIC032_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → Diff → `@@ -651,50 +656,118 @@ EPIC033_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → Diff → `@@ -730,50 +803,52 @@ CONJUNCTION_WRITER_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → Diff → `@@ -843,50 +918,56 @@ def _write_path_proof(`; PR Artifacts → Diff → `@@ -966,71 +1047,74 @@ def _normalize_index_entry(entry: Mapping[str, object]):`  
    Approved Plan linkage: Approved Plan → PR-01 — Evidence outputs

RCA

A) Bug/Failure statement

PR Artifacts record repeated review and remediation cycles, including `We have 4 bugs and CI failure here. Analyze and fix.`, `Another bug.`, `3 new bugs introduced:`, and `3 more bugs found:`. The explicit CI failure was `ORIENTATION_DRIFT`.

B) Root cause(s)

1. The source-selection snapshot initially dropped auth/geocode fields that were needed to preserve the v1/v2 auth distinction.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `The snapshot drops those fields here, so source-selection evidence can still pass even if later wiring selects a route with the wrong header family; include the relevant contract-map auth/geocode fields or add a guard over them.`  
2. The PR check log initially hard-coded closed-rails posture even when public-document refresh mode was used.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `When this generator is run with` \--refresh-public-docs`, it fetches public documentation under open rails, but the EPIC034 check log still hard-codes` network\_posture=closed-rails-source-cache`.`  
3. The evidence index initially used EPIC034-specific keys for canonical PF12 artifact bindings and later kept stale EPIC034-specific duplicates.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Registering this governed path under an EPIC034-specific key means evidence consumers that resolve the canonical HDAPI v2 source-selection artifact will not find the new row even though the artifact exists; please use the PF12 key while keeping the EPIC034 metadata on the row.`  
   Evidence pointer(s): PR Artifacts → Actions Taken → `the current generated INDEX and mirror now contain both` epic034.pr01.source\_selection\_snapshot`/`epic034.pr01.v1\_legacy\_guard`and the canonical`hdapi\_v2.source\_selection`/`hdapi\_v2.v1\_legacy\_guard `rows for the same physical files`  
4. Auth validation initially accepted mixed auth-family strings because it only checked for the expected family substring.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `these guards only require the expected header-family substring, so a v1 route with` HD-Api-Key header plus Authorization Bearer token`(or a v2 route also carrying`HD-Api-Key`) still generates a PASS snapshot/check log.`  
5. Source-authority, non-coordinate geocode, geocode-header, and path-proof chronology checks were initially incomplete.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `please fail closed when these source-authority fields do not match the expected route family.`  
   Evidence pointer(s): PR Artifacts → Actions Taken → `please also assert` required `for the non-coordinate routes before certifying the snapshot.`  
   Evidence pointer(s): PR Artifacts → Actions Taken → `require` HD-Geocode-Key header`whenever`expected\_geocode \== "required" `and reject it for the coordinates route.`  
   Evidence pointer(s): PR Artifacts → Actions Taken → `That makes the governed path proof claim the file was modified hours before it was generated, so evidence consumers relying on proof chronology get false provenance`  
6. `TESTS_PASS_OK` was initially bound to a generated check log that did not prove pytest or QA execution.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `This registers the generated source-selection check log as evidence for` TESTS\_PASS\_OK`, but that log is produced by` generate\_hdapi\_v2\_contract\_inventory.py `and contains no pytest command, exit code, or QA receipt.`

C) Fix in this PR

* Added auth/geocode preservation and fail-closed guards to source-selection snapshot generation.  
* Updated source-selection check-log generation to report active generation posture and avoid false closed-rails claims for public-doc refresh mode.  
* Registered source-selection and v1 legacy-guard evidence under PF12 canonical artifact keys.  
* Filtered superseded EPIC034-specific evidence keys before appending canonical entries.  
* Rejected mixed v1/v2 auth families.  
* Added source-authority validation for expected validated YAML source specs and rank-1 source precedence.  
* Added non-coordinate geocode requirement checks and geocode-auth-header checks.  
* Added current-epic doc-delta evidence pair and registered it in the evidence updater.  
* Removed unsupported `TESTS_PASS_OK` token binding from the generated source-selection check-log evidence row.  
* Refreshed governed evidence ledgers, hashes, path proofs, and orientation evidence.

D) Fix verification

* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`.

Findings

1. F-001 (DR-001): Machine mirror updates include HDE-EPIC034 canonical source-selection and doc-delta rows while preserving index/mirror validation.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.source_selection","discovered_physical_path":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory","produced_at_utc":"2026-06-16T21:45:57Z","proof_anchor":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt","record_type":"epic034_pr01_source_selection","role":"snapshot","schema_version":"1.0","sha256":"d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2","size_bytes":2609,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Why it matters: This confirms canonical source-selection evidence is mirror-bound.  
2. F-002 (DR-002): Machine mirror path proof is refreshed with coherent size, hash, mirror-body hash, mtime, and produced time.  
   Evidence pointer: PR Artifacts → Diff → `+mirror_body_sha256: 9d45b5c2c4cf9911ca97c2e78775db46a40a2c9dba9e9f6b2394cef939bcf799`  
   Why it matters: The machine mirror proof supports updated mirror trust.  
3. F-003 (DR-003): Machine mirror checksum sidecar is updated.  
   Evidence pointer: PR Artifacts → Diff → `+d73d0ab045ede2c1c779be90e64a2811bdb715860a91d189933fc3fddaf428ee artifacts/evidence_index.jsonl`  
   Why it matters: The checksum sidecar tracks the updated mirror file.  
4. F-004 (DR-004): Machine mirror checksum path proof is refreshed.  
   Evidence pointer: PR Artifacts → Diff → `+sha256: d0b96aa22934d2c585ad47a814cf08d5584ce2a4cd6f5771839e529f1f6f5b8d`  
   Why it matters: The checksum sidecar proof remains coherent.  
5. F-005 (DR-005): Narrative router CLI/HTTP parity path-proof refresh is unrelated but covered by validation.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`  
   Why it matters: Unrelated evidence churn is not a blocker when validation passes.  
6. F-006 (DR-006): Narrative router ABBA parity path-proof refresh is unrelated but covered by validation.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`  
   Why it matters: Unrelated evidence churn is not a blocker when validation passes.  
7. F-007 (DR-007): Source-selection snapshot preserves route-family classification, source authority, auth model, geocode posture, and no-claim boundaries.  
   Evidence pointer: PR Artifacts → Diff → `+"ai_scope_claim":"NONE","generated_at_utc":"2026-06-16T21:45:57Z","open_rails_vendor_smoke_claim":"NONE","public_reader_change_claim":"NONE","request_shaping_claim":"NONE"`  
   Why it matters: This directly supports HDE-FERM007.1 and Approved Plan boundaries.  
8. F-008 (DR-008): Source-selection snapshot path proof is present and current.  
   Evidence pointer: PR Artifacts → Diff → `+sha256: d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2`  
   Why it matters: The primary source-selection evidence is path-proven.  
9. F-009 (DR-009): V1 legacy guard log proves explicit legacy status and non-collapse.  
   Evidence pointer: PR Artifacts → Diff → `+[/v1/bodygraphs] legacy_v1_bodygraph_explicit=PASS`  
   Why it matters: This directly satisfies the v1 legacy isolation requirement.  
10. F-010 (DR-010): V1 legacy guard path proof is present and current.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: e1d4b619946ba81869c07bb3be1de5e9c3f04813737d9bd069e05359399d10b2`  
    Why it matters: The v1 legacy guard evidence is path-proven.  
11. F-011 (DR-011): Writer readback path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
12. F-012 (DR-012): Writer summary path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
13. F-013 (DR-013): EPIC032 doc-delta path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`  
    Why it matters: Current-epic HDE-EPIC034 doc-delta evidence is provided separately.  
14. F-014 (DR-014): Current-epic draft/staging doc-delta surface is present and says no PF-Canon document edits are required by PR-01.  
    Evidence pointer: PR Artifacts → Diff → `+No PF-Canon document edits are required by PR-01. The PR proves source-selection policy and v1 legacy BodyGraph isolation using repo-governed evidence without changing PF-Canon text.`  
    Why it matters: This satisfies the doc-delta evidence posture without inventing canon edits.  
15. F-015 (DR-015): Current-epic draft/staging doc-delta path proof is present.  
    Evidence pointer: PR Artifacts → Diff → `+path: audit/docdeltas/hde-epic034_doc_deltas.md`  
    Why it matters: The current-epic draft/staging doc-delta surface is path-proven.  
16. F-016 (DR-016): Narrative keys path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
17. F-017 (DR-017): Narrative pack identity path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
18. F-018 (DR-018): Narrative registry diff path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
19. F-019 (DR-019): Orientation demo now records the updated artifact count.  
    Evidence pointer: PR Artifacts → Diff → `+total_artifacts: 365`  
    Why it matters: This addresses orientation evidence drift after adding new governed artifacts.  
20. F-020 (DR-020): Orientation demo path proof is refreshed.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: cf357b25063135db2a1d0aeb785e01cc1252a225e506e8e45d88d3c99e537eaa`  
    Why it matters: The orientation evidence remains path-proven.  
21. F-021 (DR-021): EPIC030 category-order path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
22. F-022 (DR-022): EPIC030 compat identity path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
23. F-023 (DR-023): EPIC030 compat parity path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
24. F-024 (DR-024): EPIC030 band-edges path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
25. F-025 (DR-025): EPIC030 band-threshold diff path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
26. F-026 (DR-026): EPIC030 band-threshold identity hash path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
27. F-027 (DR-027): EPIC030 category canonical compare path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
28. F-028 (DR-028): EPIC030 category framework path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
29. F-029 (DR-029): EPIC030 per-channel mechanics path-proof refresh is unrelated evidence churn.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`  
    Why it matters: It does not expand PR-01 behavior and is covered by validation.  
30. F-030 (DR-030): Current-epic QA meta doc-delta capture surface is present.  
    Evidence pointer: PR Artifacts → Diff → `+This current-epic doc-delta draft/staging surface binds HDE-EPIC034 PR-01 to PF09.5 HDE-FERM007.1 source-selection evidence only.`  
    Why it matters: This completes the second surface for `DOC_DELTA_PRESENT_OK`.  
31. F-031 (DR-031): Current-epic QA meta doc-delta capture path proof is present.  
    Evidence pointer: PR Artifacts → Diff → `+path: audit/qa/hde-epic034/00_meta/doc_deltas.md`  
    Why it matters: The epic-scoped capture surface is path-proven.  
32. F-032 (DR-032): Source-selection check log records all required checks as PASS.  
    Evidence pointer: PR Artifacts → Diff → `+[source_authority_validated_yaml_rank1] status=PASS`  
    Why it matters: This proves the PR-01 check log now covers route family, auth family, geocode, source authority, and no-live-vendor posture.  
33. F-033 (DR-033): Source-selection check log path proof is present.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: 36b1ccf493ecea2129d773fb2c272d4736187dd462ebd81e0bb417da3e72d12e`  
    Why it matters: The PR-scoped check log is path-proven.  
34. F-034 (DR-034): Human evidence index is updated with current-epic doc-delta and source-selection entries.  
    Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
    Why it matters: This proves current-epic doc-delta token evidence is indexed.  
35. F-035 (DR-035): Human evidence index path proof is refreshed.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: 293be49324caf3780cf19c75c468dd4672d40d4f3d2e23a121cff9c9f8b600f2`  
    Why it matters: The human evidence index proof matches updated index bytes.  
36. F-036 (DR-036): Human evidence index hash sentinel is updated.  
    Evidence pointer: PR Artifacts → Diff → `+293be49324caf3780cf19c75c468dd4672d40d4f3d2e23a121cff9c9f8b600f2 docs/evidence/INDEX.json`  
    Why it matters: The index hash sentinel matches the updated human index.  
37. F-037 (DR-037): Human evidence index hash sentinel path proof is refreshed.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: 83413db6a9e06937dcb2ab3883b3ab7dbafcce1c25e6044f8e554885c9b9c895`  
    Why it matters: The hash sentinel proof is coherent.  
38. F-038 (DR-038): Tests cover the planned behavior and every recorded bug class.  
    Evidence pointer: PR Artifacts → Diff → `+def test_epic034_source_selection_fails_when_geocode_auth_header_drifts() -> None:`  
    Why it matters: Regression coverage is sufficient for the observed source-selection evidence risks.  
39. F-039 (DR-039): Generator changes remain evidence-generation scoped and include fail-closed checks.  
    Evidence pointer: PR Artifacts → Diff → `+ raise ValueError(f"SOURCE_SELECTION_SOURCE_AUTHORITY_MISMATCH:{method} {path}")`  
    Why it matters: The generator now fails closed on non-authoritative sources rather than certifying weak evidence.  
40. F-040 (DR-040): Evidence updater changes register current EPIC034 evidence and avoid stale duplicate keys.  
    Evidence pointer: PR Artifacts → Diff → `+ ("epic034.pr01.source_selection_snapshot", "artifacts/vendor/hdapi_v2/source_selection.snapshot.json"),`  
    Why it matters: This prevents duplicate canonical/EPIC034-specific evidence rows and supports canonical consumer lookup.  
41. F-041: No request shaping, response mapping, public Reader change, open-rails smoke, live conformance, new HTTP home, or AI scope is claimed by the new doc-delta surfaces.  
    Evidence pointer: PR Artifacts → Diff → `+- No request shaping is implemented or claimed.`  
    Why it matters: This confirms scope containment against the Approved Plan.  
42. F-042: Final validation commands are recorded as passed.  
    Evidence pointer: PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py`  
    Why it matters: This supports the required PR-01 basic QA and remediation closure.

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.1  
   Current PF09 status: Task status: Not done; Subtask status: Not done  
   Status recommendation: change to Done  
   Why this status posture is supported: PR Artifacts provide canonical source-selection evidence, v1 legacy guard evidence, check-log PASS evidence, current-epic doc-delta evidence, path proofs, human index updates, machine mirror updates, hash proof, and targeted test proof for HDE-FERM007.1. The recommendation applies only to HDE-FERM007.1; no parent HDE-FERM007 status change is recommended because later HDE-FERM007 subtasks remain outside PR-01.  
   Evidence pointer(s): PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.source_selection","discovered_physical_path":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory","produced_at_utc":"2026-06-16T21:45:57Z","proof_anchor":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt","record_type":"epic034_pr01_source_selection","role":"snapshot","schema_version":"1.0","sha256":"d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2","size_bytes":2609,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Evidence pointer(s): PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   PF proof excerpt(s) when PF09 is relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
   "Task ID: HDE-FERM007"  
   "Task status: Not done"  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.1 \- Pin v2 source-selection policy  
   "Define and implement source-selection behavior so v2 chart endpoints are the recommended vendor path. v1 BodyGraph endpoints may be retained only as explicitly named legacy behavior. The policy must distinguish full chart, simple chart, and coordinates chart routes rather than treating all vendor calls as one legacy BodyGraph endpoint."  
   "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `JSON_CANONICAL_CHECK_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.source_selection","discovered_physical_path":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory","produced_at_utc":"2026-06-16T21:45:57Z","proof_anchor":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt","record_type":"epic034_pr01_source_selection","role":"snapshot","schema_version":"1.0","sha256":"d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2","size_bytes":2609,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python - <<'PY' ... PY canonical JSON check for artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
* `EVIDENCE_INDEX_UPDATED_OK`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
* `MACHINE_MIRROR_UPDATED_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"index.machine_mirror","discovered_physical_path":"artifacts/evidence_index.jsonl","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"artifacts/evidence_index.jsonl.path_proof.txt","role":"self_record","sha256":"9d45b5c2c4cf9911ca97c2e78775db46a40a2c9dba9e9f6b2394cef939bcf799","size_bytes":148549}`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 epic-scoped QA meta doc-delta capture for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
* `TESTS_PASS_OK`  
  * PR Artifacts → Testing → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 epic-scoped QA meta doc-delta capture for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
  Type: Canonical JSON snapshot  
  Key proof facts copied verbatim from PR Artifacts: `"runtime_conformance_claim":"NONE"`; `"request_shaping_claim":"NONE"`; `"open_rails_vendor_smoke_claim":"NONE"`; `"public_reader_change_claim":"NONE"`; `"ai_scope_claim":"NONE"`  
  sha256: `d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2`  
* Path: `artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts: `path: artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; `size_bytes: 2609`; `produced_at_utc: 2026-06-16T21:45:57Z`  
  sha256: `d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2`  
* Path: `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`  
  Type: LF-terminated log  
  Key proof facts copied verbatim from PR Artifacts: `[/v1/bodygraphs] legacy_v1_bodygraph_explicit=PASS`; `[/v1/bodygraphs] collapsed_to_recommended_v2_chart=FAIL`; `status=PASS`  
  sha256: `e1d4b619946ba81869c07bb3be1de5e9c3f04813737d9bd069e05359399d10b2`  
* Path: `artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts: `path: artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; `size_bytes: 590`; `produced_at_utc: 2026-06-16T21:45:57Z`  
  sha256: `e1d4b619946ba81869c07bb3be1de5e9c3f04813737d9bd069e05359399d10b2`  
* Path: `audit/qa/hde-epic034/pr-01/source_selection_check.log`  
  Type: LF-terminated check log  
  Key proof facts copied verbatim from PR Artifacts: `[v2_variants_distinguished] status=PASS`; `[v1_not_collapsed_to_v2] status=PASS`; `[source_authority_validated_yaml_rank1] status=PASS`; `status=PASS`  
  sha256: `36b1ccf493ecea2129d773fb2c272d4736187dd462ebd81e0bb417da3e72d12e`  
* Path: `audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts: `path: audit/qa/hde-epic034/pr-01/source_selection_check.log`; `size_bytes: 821`; `produced_at_utc: 2026-06-16T21:45:57Z`  
  sha256: `36b1ccf493ecea2129d773fb2c272d4736187dd462ebd81e0bb417da3e72d12e`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
  Type: Current-epic doc-delta draft/staging surface  
  Key proof facts copied verbatim from PR Artifacts: `No PF-Canon document edits are required by PR-01. The PR proves source-selection policy and v1 legacy BodyGraph isolation using repo-governed evidence without changing PF-Canon text.`  
  sha256: `6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf`  
* Path: `audit/qa/hde-epic034/00_meta/doc_deltas.md`  
  Type: Current-epic QA meta doc-delta capture  
  Key proof facts copied verbatim from PR Artifacts: `HDE-FERM007.1 remains unchanged in PF09.5 by this PR until final review confirms the evidence posture.`  
  sha256: `6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf`  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts copied verbatim from PR Artifacts: `"artifact_key":"index.human_index"`; `"discovered_physical_path":"docs/evidence/INDEX.json"`  
  sha256: `293be49324caf3780cf19c75c468dd4672d40d4f3d2e23a121cff9c9f8b600f2`  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Evidence Mirror  
  Key proof facts copied verbatim from PR Artifacts: `"artifact_key":"index.machine_mirror"`; `"discovered_physical_path":"artifacts/evidence_index.jsonl"`; `"role":"self_record"`  
  sha256: `9d45b5c2c4cf9911ca97c2e78775db46a40a2c9dba9e9f6b2394cef939bcf799`

C) Test/CI proof

* Job or test name: `python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `canonical JSON check for artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python - <<'PY' ... PY canonical JSON check for artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

PF09 Impact Summary

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.1  
   Current status if evidenced: Task status: Not done; Subtask status: Not done  
   Status action: change to Done  
   Evidence pointer(s): PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.source_selection","discovered_physical_path":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory","produced_at_utc":"2026-06-16T21:45:57Z","proof_anchor":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt","record_type":"epic034_pr01_source_selection","role":"snapshot","schema_version":"1.0","sha256":"d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2","size_bytes":2609,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Linked Findings item(s): F-007; F-009; F-014; F-030; F-032; F-034; F-038; F-039; F-040  
   Linked CHG item(s), if any: CHG-006

Doc Delta Detection Workflow

CHG-001  
Change claim type: behavior or output  
Change claim: PR-01 produces a source-selection snapshot that classifies v2 chart routes as recommended and v1 BodyGraph routes as legacy, while preserving no-claim posture.  
Evidence pointer: PR Artifacts → Diff → `+"source_selection_policy":{"classification_source":"governed contract inventory","legacy_v1_bodygraph_route_family":"legacy_v1_bodygraph","recommended_internal_vendor_route_family":"recommended_v2_chart","selection_scope":"HDE-EPIC034 PR-01 HDE-FERM007.1 route-family source selection only"}`  
Canon basis: CANON ALIGNED

CHG-002  
Change claim type: behavior or output  
Change claim: PR-01 produces a v1 legacy guard log proving v1 routes are explicit legacy behavior and not silently collapsed into v2 chart behavior.  
Evidence pointer: PR Artifacts → Diff → `+[/v1/bodygraphs] collapsed_to_recommended_v2_chart=FAIL`  
Canon basis: CANON ALIGNED

CHG-003  
Change claim type: behavior or output  
Change claim: PR-01 adds fail-closed checks for auth-family drift, geocode drift, source-authority drift, and missing required route families.  
Evidence pointer: PR Artifacts → Diff → `+ raise ValueError(f"SOURCE_SELECTION_AUTH_FAMILY_MISMATCH:{method} {path}")`  
Canon basis: CANON ALIGNED

CHG-004  
Change claim type: governed paths or artifact families  
Change claim: PR-01 registers canonical evidence rows for source-selection, v1 legacy guard, PR-01 check log, and current-epic doc-delta surfaces.  
Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG-005  
Change claim type: tokens, rails, or evidence posture  
Change claim: PR-01 adds the two-surface current-epic doc-delta evidence pair for `DOC_DELTA_PRESENT_OK`.  
Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"epic034.pr01.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 epic-scoped QA meta doc-delta capture for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-16T21:45:59Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG-006  
Change claim type: PF09 status-impact requirement  
Change claim: PR-01 evidence supports changing PF09.5 HDE-FERM007.1 from Not done to Done, while leaving parent HDE-FERM007 unchanged.  
Evidence pointer: PR Artifacts → Diff → `+HDE-FERM007.1 remains unchanged in PF09.5 by this PR until final review confirms the evidence posture.`  
Canon basis: CANON ALIGNED

CHG: CHG-006

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM007.1 \- Pin v2 source-selection policy

Canon basis: CANON ALIGNED

Impacted PF09 task ID(s): HDE-FERM007

Impacted PF09 subtask ID(s): HDE-FERM007.1

PF09 status action: change to Done

Delta: Update HDE-FERM007.1 subtask status from Not done to Done, and preserve parent HDE-FERM007 as Not done until later subtasks are reviewed.

Why: PR Artifacts provide source-selection, v1 legacy guard, doc-delta, evidence index, machine mirror, path-proof, and test evidence for the exact HDE-FERM007.1 slice.

Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.source_selection","discovered_physical_path":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 canonical source-selection snapshot for HDE-FERM007.1 derived from governed HDAPI v2 contract inventory","produced_at_utc":"2026-06-16T21:45:57Z","proof_anchor":"artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt","record_type":"epic034_pr01_source_selection","role":"snapshot","schema_version":"1.0","sha256":"d01d991bfaca8b1eb0be70b711ebda5498bb573b19f85ea942ea841a448c93b2","size_bytes":2609,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`

Canon proof excerpt:  
"Task ID: HDE-FERM007"  
"Task status: Not done"  
"Define and implement source-selection behavior so v2 chart endpoints are the recommended vendor path. v1 BodyGraph endpoints may be retained only as explicitly named legacy behavior. The policy must distinguish full chart, simple chart, and coordinates chart routes rather than treating all vendor calls as one legacy BodyGraph endpoint."  
"Subtask status: Not done"

## 2.9) OPS-01 HDE-EPIC034

Review Summary

* Ops Evidence shows OPS-01 produced the required evidence bundle files: `fact_summary.json`, `fact_summary.json.path_proof.txt`, `commands.txt`, `stdout.log`, `stderr.log`, `exit_codes.txt`, and `files_sha256.txt`.  
* Ops Evidence aligns with the Approved Plan’s OPS-01 scope: bounded PO discovery, secret-safe operational fact capture, no PR work, no QA pass claim, no open-rails execution, and no PF09 status move claim.  
* Ops Evidence records the PF10-decided facts that were missing in the prior OPS review: `Authorization: Bearer <redacted>`, `HD-Api-Key: <redacted>`, and `HD-Geocode-Key: <redacted>`.  
* Ops Evidence records deployment presence, deprecated alias posture, secret-binding presence, documented environment bindings, endpoint-family availability, account/tier posture, and proceed classifications for PR-02, PR-05, and OPS-02.  
* Evidence provenance is sufficient for this OPS task: the bundle includes a command/action ledger, JSON validation output, path-proof creation output, exit-code ledger, and checksum ledger.  
* No destructive action, open-rails test, live vendor success claim, PR work claim, QA pass claim, or PF09 status move claim is asserted.  
* PF09.x support: OPS-01 supports the Approved Plan’s evidence-only/unblock posture for HDE-FERM007.2 and HDE-FERM007.5; it does not itself support changing either subtask to Done.

Findings

1. What you observed: Ops Evidence maps OPS-01 to the correct PF09 task and subtasks, and states that OPS-01 contributes evidence only.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""pf09\_impact":{"affected\_subtasks":\["HDE-FERM007.2","HDE-FERM007.5"\],"task\_id":"HDE-FERM007"" | ""summary":"OPS-01 contributes secret-safe operational evidence only; it does not complete HDE-FERM007.2 or HDE-FERM007.5""  
   Expected requirement from the Approved Plan: OPS-01 affects HDE-FERM007.2 and HDE-FERM007.5 and has PF09 completion role `Contributes evidence only`.  
   Why it matters: The OPS evidence does not overclaim PF09 status and supports the intended downstream PR/OPS sequencing.  
   Blocker for acceptance: No  
   PF support, only if relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.5 \- Prove v2 adapter determinism under closed rails  
   Canon proof excerpt, only if PF support is used:  
   "\#\#\# **Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints**"  
   "\#\#\# **Subtask HDE-FERM007.5 \- Prove v2 adapter determinism under closed rails**"  
2. What you observed: Required OPS-01 deliverables are present and checksum-bound.  
   Evidence pointer: Ops Evidence | ops-01/files\_sha256.txt | "ed0da5fa3f5610000db9f715dc5f236509d6904a8f81d7cfdfb8a8d813026bb6 audit/ops/hde-epic034/ops-01/commands.txt" | "7d9df2d26a910a386b149420fe220fff3a9a851ee3b12081f390f3fbdeb0889c audit/ops/hde-epic034/ops-01/fact\_summary.json" | "de9f2d98c7156a5b9facc60948081d16727f378d16fdcc4cf0e78da5b21bad20 audit/ops/hde-epic034/ops-01/stdout.log"  
   Expected requirement from the Approved Plan: OPS-01 must produce `fact_summary.json`, `fact_summary.json.path_proof.txt`, `commands.txt`, `stdout.log`, `stderr.log`, `exit_codes.txt`, and `files_sha256.txt`.  
   Why it matters: The expected OPS evidence bundle exists as repo-stored text evidence.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
3. What you observed: The main fact summary has a sibling path-proof transcript with matching path, size, sha256, mtime, and produced-at data.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json.path\_proof.txt | "path: audit/ops/hde-epic034/ops-01/fact\_summary.json" | "size\_bytes: 5738" | "sha256: 7d9df2d26a910a386b149420fe220fff3a9a851ee3b12081f390f3fbdeb0889c"  
   Expected requirement from the Approved Plan: OPS-01 must produce `audit/ops/hde-epic034/ops-01/fact_summary.json.path_proof.txt`.  
   Why it matters: The primary OPS fact summary is path-proven and reviewable.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
4. What you observed: Validation and checksum steps are recorded as passing.  
   Evidence pointer: Ops Evidence | ops-01/stdout.log | "json\_validation=PASS" | "path\_proof\_created=audit/ops/hde-epic034/ops-01/fact\_summary.json.path\_proof.txt" | "sha256sum\_check=PASS"  
   Expected requirement from the Approved Plan: Success requires the fact summary and supporting evidence outputs to be present and checkable.  
   Why it matters: The evidence bundle’s own validation signals support trust in the created deliverables.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
5. What you observed: OPS-01 records PO authorization, PR-01 sequencing, and the target environment set.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""po\_authorization":"authorized\_bounded\_ops01\_discovery\_repo\_bundle\_only"" | ""pr01\_sequencing\_state":"merged"" | ""target\_set":\["Prod \- Railway","Dev \- Codex","QA \- Codespaces"\]"  
   Expected requirement from the Approved Plan: OPS-01 requires PR-01 as the source-selection baseline, PO authorization, and PO access to relevant runtime, vendor, deployment, and secret-binding surfaces.  
   Why it matters: The evidence supports bounded execution authority and correct sequencing.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
6. What you observed: OPS-01 records the PF10-decided canonical base URL key, vendor API key, geocode key, deprecated legacy alias, and all required header-family shapes.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""canonical\_base\_url\_key":"HD\_API\_BASE\_URL"" | ""v2\_chart\_route\_auth\_header\_shape":"Authorization: Bearer "" | ""v1\_legacy\_bodygraph\_auth\_header\_shape":"HD-Api-Key: ""  
   Expected requirement from the Approved Plan: OPS-01 must record PF10-decided facts without treating them as discovery questions.  
   Why it matters: These facts are required to unblock later request-shaping and deterministic proof design without confusing environment-variable names with outbound vendor header names.  
   Blocker for acceptance: No  
   PF support, only if relied on:  
   PF10 — HDE Build Notes, §2.7) HumanDesignAPI v2 Uses Authorization Bearer; v1 Uses HD-Api-Key Header  
   Canon proof excerpt, only if PF support is used:  
   "HumanDesignAPI v2 chart routes use the API key as a Bearer token in the `Authorization` header."  
   "HumanDesignAPI v1 BodyGraph routes use the legacy `HD-Api-Key` request header."  
   "When the route requires geocoding, it is projected as:"  
   "`HD-Geocode-Key: <redacted>`"  
7. What you observed: OPS-01 records the geocode header shape when required.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""canonical\_geocode\_key":"GEO\_API\_KEY"" | ""geocode\_header\_when\_required":"HD-Geocode-Key: "" | ""header\_family\_notes":"PF10-decided header-family facts are recorded as non-secret shapes only; OPS-01 does not record raw header values or execute a vendor call.""  
   Expected requirement from the Approved Plan: OPS-01 must record `GEO_API_KEY` and `HD-Geocode-Key: <redacted>` where geocoding is required.  
   Why it matters: Later v2 request shaping and closed-rails proof need the geocode-key posture separated from vendor API-key posture.  
   Blocker for acceptance: No  
   PF support, only if relied on:  
   PF10 — HDE Build Notes, §2.7) HumanDesignAPI v2 Uses Authorization Bearer; v1 Uses HD-Api-Key Header  
   Canon proof excerpt, only if PF support is used:  
   "The geocoding key remains:"  
   "`GEO_API_KEY`"  
   "When the route requires geocoding, it is projected as:"  
   "`HD-Geocode-Key: <redacted>`"  
8. What you observed: OPS-01 records environment-variable posture for Prod, Dev, and QA, including canonical-only base URL posture for Prod/Dev and a matching temporary compatibility alias in QA.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""prod\_railway":{"base\_url\_dual\_key\_status":"canonical\_only","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"absent","HD\_API\_BASE\_URL":"present:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)"" | ""dev\_codex":{"base\_url\_dual\_key\_status":"canonical\_only","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"absent","HD\_API\_BASE\_URL":"present:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)"" | ""qa\_codespaces":{"base\_url\_dual\_key\_status":"match","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"present\_as\_temporary\_compatibility\_alias:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_BASE\_URL\\":\\"present:https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_BASE_URL%5C%22:%5C%22present:https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)""  
   Expected requirement from the Approved Plan: OPS-01 must discover whether `HD_API_BASE_URL` is present in each target environment, whether `HDAPI_BASE_URL` is absent or present as temporary compatibility alias or legacy drift, and whether simultaneous values match or conflict.  
   Why it matters: PR-02 needs this posture to avoid guessing or silently preferring deprecated configuration names.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
9. What you observed: OPS-01 records documented environment bindings for Prod, Dev, and QA without secret values.  
   Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""prod\_railway":\["HD\_API\_BASE\_URL","HD\_API\_KEY","GEO\_API\_KEY","SAFE\_MODE","ALLOW\_NETWORK","APP\_ENV","LC\_ALL","LANG","TZ"\]" | ""dev\_codex":\["HD\_API\_BASE\_URL","HD\_API\_KEY","GEO\_API\_KEY","SAFE\_MODE","ALLOW\_NETWORK","APP\_ENV","LC\_ALL","LANG","TZ","PORT","DB\_BRIDGE\_URL","DEV\_SAMPLER\_URL"\]" | ""qa\_codespaces":\["HD\_API\_BASE\_URL","HDAPI\_BASE\_URL temporary compatibility alias","HD\_API\_KEY","GEO\_API\_KEY","SAFE\_MODE","ALLOW\_NETWORK","APP\_ENV","LC\_ALL","LANG","TZ"\]"  
   Expected requirement from the Approved Plan: OPS-01 must record documented environment-variable bindings.  
   Why it matters: These bindings are the concrete non-secret environment facts needed by downstream implementation and proof work.  
   Blocker for acceptance: No  
   PF support, only if relied on: N/A  
   Canon proof excerpt, only if PF support is used: N/A  
10. What you observed: OPS-01 records endpoint-family availability and account/tier posture while explicitly stating v2 has not yet been live-tested.  
    Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""endpoint\_family\_availability":{"dev\_codex":"repo-governed source inventory documents v2 chart families and legacy v1 BodyGraph families; v1 has worked previously in the app; v2 has not yet been live-tested; OPS-01 performed no live vendor call"" | ""account\_tier\_posture":{"dev\_codex":"account/tier supports previously demonstrated legacy v1 BodyGraph usage; v2 account/tier access has not yet been tested; no sensitive account details recorded"" | ""open\_rails\_test\_executed":false"  
    Expected requirement from the Approved Plan: OPS-01 must record endpoint-family availability, account/tier posture, and must not perform open-rails vendor smoke.  
    Why it matters: The evidence truthfully distinguishes source-inventory readiness from live v2 conformance.  
    Blocker for acceptance: No  
    PF support, only if relied on: N/A  
    Canon proof excerpt, only if PF support is used: N/A  
11. What you observed: OPS-01 records downstream proceed classifications for PR-02, PR-05, and OPS-02.  
    Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""pr02\_can\_proceed\_safely":"proceed\_with\_caveat: PR-02 may proceed for request-shaping implementation/design using repo-governed v2 contract inventory, confirmed secret-binding posture, and PF10-decided header-family facts, but must not claim live v2 vendor success because v2 account/tier access is untested" | ""pr05\_can\_be\_designed\_honestly":"proceed\_with\_requirement: PR-05 closed-rails deterministic proof can be designed from repo-governed source-selection/contract evidence, confirmed environment binding posture, and PF10-decided header-family facts." | ""ops02\_can\_proceed\_safely":"proceed\_with\_requirement: OPS-02 may proceed after the required PR prerequisites establish v2 request shaping, environment-variable reconfiguration, and a PO-approved open-rails v2 test plan"  
    Expected requirement from the Approved Plan: OPS-01 fact summary must include clear proceed or blocked classification for PR-02, PR-05, and OPS-02.  
    Why it matters: These classifications satisfy the OPS-01 handoff requirement while preserving caveats and prerequisites.  
    Blocker for acceptance: No  
    PF support, only if relied on: N/A  
    Canon proof excerpt, only if PF support is used: N/A  
12. What you observed: OPS-01 records secret-handling rules and non-claims.  
    Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""redaction\_rule":"No raw API keys, raw bearer tokens, raw geocode keys, raw secret values, sensitive account details, unnecessary personally identifying information, uncontrolled production data, or full private payloads may be recorded." | ""live\_v2\_vendor\_success\_claimed":false" | ""pf09\_status\_move\_claimed":false"  
    Expected requirement from the Approved Plan: OPS-01 must not record raw API keys, bearer tokens, geocode keys, secret values, sensitive account details, unnecessary PII, uncontrolled production data, or full private payloads; it must not claim implementation, QA, live conformance, or PF09 status movement.  
    Why it matters: The evidence remains secret-safe and truthfully scoped.  
    Blocker for acceptance: No  
    PF support, only if relied on: N/A  
    Canon proof excerpt, only if PF support is used: N/A

Evidence Print (PASS PROOF; required)

A) Required deliverables satisfied

* Deliverable name: `audit/ops/hde-epic034/ops-01/fact_summary.json`  
  Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""schema":"ops01\_hde\_epic034\_operational\_fact\_summary.v1"" | ""ops\_task":"OPS-01"" | ""path":"audit/ops/hde-epic034/ops-01/fact\_summary.json""  
  Key proof facts:  
  * Records the OPS task, epic, path, schema, created-at, and updated-at metadata.  
  * Records PF10-decided facts and operational discovery results.  
  * Records proceed classifications for PR-02, PR-05, and OPS-02.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/fact_summary.json.path_proof.txt`  
  Evidence pointer: Ops Evidence | ops-01/fact\_summary.json.path\_proof.txt | "path: audit/ops/hde-epic034/ops-01/fact\_summary.json" | "size\_bytes: 5738" | "sha256: 7d9df2d26a910a386b149420fe220fff3a9a851ee3b12081f390f3fbdeb0889c"  
  Key proof facts:  
  * Provides the sibling path-proof transcript for the main fact summary.  
  * Records path, size, sha256, mtime, and produced-at data.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/commands.txt`  
  Evidence pointer: Ops Evidence | ops-01/commands.txt | "EDIT\_ACTION audit/ops/hde-epic034/ops-01/fact\_summary.json \-\> remediated missing PF10-decided header-family facts: Authorization: Bearer , HD-Api-Key: , HD-Geocode-Key: " | "python \-m json.tool audit/ops/hde-epic034/ops-01/fact\_summary.json \> /tmp/hde\_epic034\_ops01\_fact\_summary.pretty.json" | "sha256sum \-c audit/ops/hde-epic034/ops-01/files\_sha256.txt"  
  Key proof facts:  
  * Records the fact-summary creation and remediation actions.  
  * Records validation, path-proof, grep, and checksum command patterns.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/stdout.log`  
  Evidence pointer: Ops Evidence | ops-01/stdout.log | "json\_validation=PASS" | "header\_family\_fact\_remediation=PASS" | "sha256sum\_check=PASS"  
  Key proof facts:  
  * Records successful JSON validation.  
  * Records header-family remediation and grep success.  
  * Records checksum validation success.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/stderr.log`  
  Evidence pointer: Ops Evidence | ops-01/files\_sha256.txt | "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b audit/ops/hde-epic034/ops-01/stderr.log"  
  Key proof facts:  
  * Included in checksum ledger.  
  * File exists as a required deliverable.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/exit_codes.txt`  
  Evidence pointer: Ops Evidence | ops-01/exit\_codes.txt | "0" | "0" | "0"  
  Key proof facts:  
  * Records zero exit codes for the validation/check steps.  
  * Included in checksum ledger.  
* Deliverable name: `audit/ops/hde-epic034/ops-01/files_sha256.txt`  
  Evidence pointer: Ops Evidence | ops-01/files\_sha256.txt | "ed0da5fa3f5610000db9f715dc5f236509d6904a8f81d7cfdfb8a8d813026bb6 audit/ops/hde-epic034/ops-01/commands.txt" | "7d9df2d26a910a386b149420fe220fff3a9a851ee3b12081f390f3fbdeb0889c audit/ops/hde-epic034/ops-01/fact\_summary.json" | "de9f2d98c7156a5b9facc60948081d16727f378d16fdcc4cf0e78da5b21bad20 audit/ops/hde-epic034/ops-01/stdout.log"  
  Key proof facts:  
  * Records sha256 entries for the OPS evidence files.  
  * Supports bundle integrity review.

B) Commands/actions evidence

* Evidence pointer: Ops Evidence | ops-01/commands.txt | "EDIT\_ACTION audit/ops/hde-epic034/ops-01/fact\_summary.json \-\> created secret-safe OPS-01 fact summary from PO-provided answers and repo/PF reality"  
  Success signal found in evidence: Fact summary exists and is checksum-bound.  
* Evidence pointer: Ops Evidence | ops-01/commands.txt | "EDIT\_ACTION audit/ops/hde-epic034/ops-01/fact\_summary.json \-\> expanded target environment set from QA-only to Prod \- Railway, Dev \- Codex, and QA \- Codespaces from PO-provided answers"  
  Success signal found in evidence: Fact summary records `target_set` as `Prod - Railway`, `Dev - Codex`, and `QA - Codespaces`.  
* Evidence pointer: Ops Evidence | ops-01/commands.txt | "EDIT\_ACTION audit/ops/hde-epic034/ops-01/fact\_summary.json \-\> remediated missing PF10-decided header-family facts: Authorization: Bearer , HD-Api-Key: , HD-Geocode-Key: "  
  Success signal found in evidence: Fact summary includes `v2_chart_route_auth_header_shape`, `v1_legacy_bodygraph_auth_header_shape`, and `geocode_header_when_required`.  
* Evidence pointer: Ops Evidence | ops-01/commands.txt | "python \-m json.tool audit/ops/hde-epic034/ops-01/fact\_summary.json \> /tmp/hde\_epic034\_ops01\_fact\_summary.pretty.json"  
  Success signal found in evidence: Ops Evidence | ops-01/stdout.log | "json\_validation=PASS"  
* Evidence pointer: Ops Evidence | ops-01/commands.txt | "rg \-n "Authorization: Bearer |HD-Api-Key: |HD-Geocode-Key: " audit/ops/hde-epic034/ops-01/fact\_summary.json"  
  Success signal found in evidence: Ops Evidence | ops-01/stdout.log | "header\_family\_grep=PASS"  
* Evidence pointer: Ops Evidence | ops-01/commands.txt | "sha256sum \-c audit/ops/hde-epic034/ops-01/files\_sha256.txt"  
  Success signal found in evidence: Ops Evidence | ops-01/stdout.log | "sha256sum\_check=PASS"

C) Configuration/infra state evidence, if applicable

* Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""prod\_railway":{"base\_url\_dual\_key\_status":"canonical\_only","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"absent","HD\_API\_BASE\_URL":"present:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)""  
  What state it proves: Prod records canonical `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` posture, with deprecated `HDAPI_BASE_URL` absent.  
* Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""dev\_codex":{"base\_url\_dual\_key\_status":"canonical\_only","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"absent","HD\_API\_BASE\_URL":"present:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)""  
  What state it proves: Dev records canonical `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` posture, with deprecated `HDAPI_BASE_URL` absent.  
* Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""qa\_codespaces":{"base\_url\_dual\_key\_status":"match","GEO\_API\_KEY":"present:redacted/SET","HDAPI\_BASE\_URL":"present\_as\_temporary\_compatibility\_alias:[https://api.humandesignapi.nl/v1\\",\\"HD\_API\_BASE\_URL\\":\\"present:https://api.humandesignapi.nl/v1\\",\\"HD\_API\_KEY\\":\\"present:redacted/SET\\](https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_BASE_URL%5C%22:%5C%22present:https://api.humandesignapi.nl/v1%5C%22,%5C%22HD_API_KEY%5C%22:%5C%22present:redacted/SET%5C)""  
  What state it proves: QA records both canonical `HD_API_BASE_URL` and temporary compatibility alias `HDAPI_BASE_URL`, with matching values and secret-bearing values redacted.  
* Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""inspection\_surfaces":{"dev\_codex":"Codex workspace environment inspection with values redacted","prod\_railway":"Railway project environment variables UI for production service","qa\_codespaces":"Codespaces shell environment inspection with secret values redacted""  
  What state it proves: The fact summary identifies the inspection surfaces used for Dev, Prod, and QA.  
* Evidence pointer: Ops Evidence | ops-01/fact\_summary.json | ""endpoint\_family\_availability":{"dev\_codex":"repo-governed source inventory documents v2 chart families and legacy v1 BodyGraph families; v1 has worked previously in the app; v2 has not yet been live-tested; OPS-01 performed no live vendor call""  
  What state it proves: Endpoint-family availability is source-inventory backed, with live v2 vendor success explicitly not claimed.

D) PF09.x later-drain support, only if the Approved Plan ties this OPS task to PF09.x completion, close, or later-drain posture

* PF09.x document: PF09.5 — HDE Build Checklist Fermentation  
  PF09.x task ID: HDE-FERM007  
  PF09.x subtask ID, if any: HDE-FERM007.2  
  Current claim in the Approved Plan: OPS-01 contributes evidence only and unblocks later v2 request-shaping implementation.  
  Supportable later-drain action: no PF09.x support proven  
  Evidence basis: Ops Evidence proves secret-safe deployment, credential-binding, deprecated alias, endpoint-family, account/tier, PF10-decided header-family, and proceed-classification facts for downstream PR-02.  
  Notes: OPS-01 does not itself implement request shaping and does not support changing HDE-FERM007.2 to Done.  
* PF09.x document: PF09.5 — HDE Build Checklist Fermentation  
  PF09.x task ID: HDE-FERM007  
  PF09.x subtask ID, if any: HDE-FERM007.5  
  Current claim in the Approved Plan: OPS-01 contributes evidence only and unblocks later closed-rails deterministic shaping proof.  
  Supportable later-drain action: no PF09.x support proven  
  Evidence basis: Ops Evidence proves secret-safe environment posture and PF10-decided key/header facts needed to design PR-05 honestly.  
  Notes: OPS-01 does not itself perform closed-rails deterministic shaping proof and does not support changing HDE-FERM007.5 to Done.

## 2.10)  PR-02 HDE-EPIC034

Review Summary

* The PR implements HDE-EPIC034 PR-02 request shaping for HumanDesignAPI v2 chart routes and preserves legacy v1 BodyGraph shaping posture.  
* The PR aligns with the Approved Plan’s PR-02 scope: HDE-FERM007.2 only, closed rails, no live vendor call, no public Reader change, no new HTTP home, no open-rails claim, and no AI scope.  
* The PR uses the accepted OPS-01 fact posture and PF10-decided key/header posture: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, v2 `Authorization: Bearer`, v1 legacy `HD-Api-Key`, and `HD-Geocode-Key`.  
* The PR adds and indexes governed request-shaping evidence: `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`, its path proof, `audit/qa/hde-epic034/pr-02/request_shaping_check.log`, and its path proof.  
* The PR includes follow-up remediation commits for validation defects, route-contract drift, geocode conditionals, safe route logging, misleading test-token wording, and final evidence proof refresh.  
* Final PR Artifacts record the full final validation suite after the last remediation commit, including targeted pytest, evidence index update/check, orientation update/check, evidence-path validation, mirror schema, hash check, LF check, and `git diff --check`.  
* Diff review covers all diff hunks across `PR-02a HDE-EPIC034.md`, `PR-02b HDE-EPIC034.md`, and `PR-02c HDE-EPIC034.md`.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.2. Review supports change to Done for HDE-FERM007.2 only; no parent HDE-FERM007 status change is supported.  
* RCA is included because PR Artifacts explicitly include bug, defect, regression, and remediation history.

Diff Review

1. DR-001  
   Change summary: PR-02a adds and refreshes the machine mirror rows for request-shaping evidence and related governed artifacts.  
   Risk assessment: Medium  
   Why it matters: Machine mirror rows are acceptance-bearing evidence pointers; they must bind the new request-shaping snapshot and check log without stale or misleading rows.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -62,51 +62,51 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -123,91 +123,91 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -235,99 +235,101 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -336,30 +338,30 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — v2 request shaping after OPS discovery  
2. DR-002  
   Change summary: PR-02a updates machine mirror hash and path-proof sidecars.  
   Risk assessment: Low  
   Why it matters: Mirror byte changes require coherent sidecars.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,6 +1,6 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
3. DR-003  
   Change summary: PR-02a refreshes historical path-proof artifacts outside the direct request-shaping slice.  
   Risk assessment: Medium  
   Why it matters: Broad evidence churn is acceptable only because later final validation re-proves evidence index, mirror, hash, and path-proof coherence.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
4. DR-004  
   Change summary: PR-02a refreshes doc-delta, topology, prior-epic QA, and EPIC033 baseline proof artifacts.  
   Risk assessment: Medium  
   Why it matters: These are not the main PR-02 behavior, but they are part of the governed evidence refresh surface.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic023_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic023_doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/gates/topology/orientation_demo.txt b/audit/gates/topology/orientation_demo.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,4 +1,4 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Acceptance tokens  
5. DR-005  
   Change summary: PR-02a refreshes HDAPI v2 contract inventory, source inventory, source-selection, and legacy guard artifacts that PR-02 consumes.  
   Risk assessment: Medium  
   Why it matters: PR-02 request shaping depends on validated contract-map fields and the accepted PR-01 source-selection baseline.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json b/artifacts/vendor/hdapi_v2/source_inventory.json`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,14 +1,14 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Discovery  
6. DR-006  
   Change summary: PR-02a updates HDAPI v2 inventory support artifacts and path proofs.  
   Risk assessment: Low  
   Why it matters: These artifacts support route-contract and source-authority posture for request shaping.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md b/artifacts/vendor/hdapi_v2/known_anomalies.md`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,15 +1,15 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log b/artifacts/vendor/hdapi_v2/openapi_validation.log`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,26 +1,26 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md b/artifacts/vendor/hdapi_v2/source_inventory.md`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,28 +1,28 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Discovery  
7. DR-007  
   Change summary: PR-02a adds the canonical request-shaping snapshot and its path proof.  
   Risk assessment: Low  
   Why it matters: This is the primary planned HDE-FERM007.2 evidence artifact.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -0,0 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -0,0 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
8. DR-008  
   Change summary: PR-02a adds the PR-scoped request-shaping check log and its path proof.  
   Risk assessment: Low  
   Why it matters: The check log proves closed-rails posture, v2 Bearer posture, v1 legacy header posture, geocode posture, base URL posture, deprecated alias posture, and secret-safety posture.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log b/audit/qa/hde-epic034/pr-02/request_shaping_check.log`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -0,0 +1,14 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -0,0 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
9. DR-009  
   Change summary: PR-02a updates human evidence index, hash sentinel, and related proof artifacts.  
   Risk assessment: Medium  
   Why it matters: The Approved Plan requires governed evidence index and mirror updates for evidence outputs.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
10. DR-010  
    Change summary: PR-02a modifies `engine/bodygraph/vendor_client.py` to implement request shaping, env-key resolution, route contracts, auth/geocode posture, and fail-closed validation.  
    Risk assessment: High  
    Why it matters: This is runtime-adjacent vendor-seam logic; incorrect handling could leak secrets, shape invalid requests, or confuse v1/v2 auth posture.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/engine/bodygraph/vendor_client.py b/engine/bodygraph/vendor_client.py`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,28 +1,29 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -61,380 +62,502 @@ PINNED_BACKOFF_PROFILES = frozenset(`  
    Approved Plan linkage: Approved Plan → PR-02 — Implementation requirements  
11. DR-011  
    Change summary: PR-02a expands `tests/bodygraph/test_vendor_client.py` for request-shaping behavior and failure modes.  
    Risk assessment: Low  
    Why it matters: Request-shaping behavior needs direct tests for auth, geocode, base URL fallback, route contracts, and fail-closed handling.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/tests/bodygraph/test_vendor_client.py b/tests/bodygraph/test_vendor_client.py`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -316,25 +316,276 @@ def test_vendor_safe_rails_failure_classes_are_observable(tmp_path: Path) -> Non`  
    Approved Plan linkage: Approved Plan → PR-02 — Basic QA check  
12. DR-012  
    Change summary: PR-02a expands `tests/evidence/test_hdapi_v2_contract_inventory.py` for canonical request-shaping evidence generation.  
    Risk assessment: Low  
    Why it matters: Generated evidence must be deterministic, contract-derived, secret-safe, and correctly indexed.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1,35 +1,36 @@`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -420,25 +421,145 @@ def test_epic034_source_selection_fails_when_source_authority_drifts() -> None:`  
    Approved Plan linkage: Approved Plan → PR-02 — Basic QA check  
13. DR-013  
    Change summary: PR-02a extends `tools/evidence/generate_hdapi_v2_contract_inventory.py` to generate request-shaping evidence and enforce evidence-gate logic.  
    Risk assessment: Medium  
    Why it matters: Evidence generation must not produce false PASS logs, stale artifacts, or open-rails claims.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -12,94 +12,127 @@ from __future__ import annotations`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -729,50 +762,179 @@ def build_source_selection_check_log(produced: str, snapshot: dict[str, Any], *`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -842,93 +1004,111 @@ def write_baseline_pointer_artifacts(produced: str, acceptance: dict[str, Any])`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
14. DR-014  
    Change summary: PR-02a updates `tools/evidence/update_evidence_index.py` to add PR-02 request-shaping rows and remove stale rows when outputs are absent.  
    Risk assessment: Medium  
    Why it matters: Evidence index rows must truthfully reflect generated artifacts and avoid stale or misleading acceptance posture.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -488,50 +488,55 @@ EPIC032_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -724,50 +729,93 @@ EPIC034_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → PR-02a HDE-EPIC034.md → `@@ -1049,72 +1097,75 @@ def _normalize_index_entry(entry: Mapping[str, object]) -> dict[str, object]:`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
15. DR-015  
    Change summary: PR-02b updates the final machine mirror after route-logging and test-evidence remediation.  
    Risk assessment: Medium  
    Why it matters: This becomes the intermediate post-remediation mirror state before PR-02c final validation refresh.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -62,51 +62,51 @@`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -123,91 +123,91 @@`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -235,101 +235,101 @@`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -338,30 +338,30 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
16. DR-016  
    Change summary: PR-02b updates mirror sidecars, historical path proofs, and human evidence index sidecars.  
    Risk assessment: Medium  
    Why it matters: These broad proof refreshes must be followed by final validation, which PR-02c supplies.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -1,6 +1,6 @@`; PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
17. DR-017  
    Change summary: PR-02b hardens `engine/bodygraph/vendor_client.py` against unsafe route logging and legacy simple route-contract drift.  
    Risk assessment: High  
    Why it matters: Vendor logs must remain keys-only and bounded; legacy route support must remain explicit and contract-backed.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/engine/bodygraph/vendor_client.py b/engine/bodygraph/vendor_client.py`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -64,54 +64,58 @@ _RETRY_AFTER_MAX_MS = 2_147_483_647`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -418,88 +422,88 @@ class HdApiClient:`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -507,57 +511,65 @@ class HdApiClient:`  
    Approved Plan linkage: Approved Plan → PR-02 — Rails posture  
18. DR-018  
    Change summary: PR-02b adds route-logging, legacy-simple shaping, and evidence-token regression tests.  
    Risk assessment: Low  
    Why it matters: These tests prevent reintroduction of route leaks and unsupported generated-log `TESTS_PASS_OK` claims.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/tests/bodygraph/test_vendor_client.py b/tests/bodygraph/test_vendor_client.py`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -279,50 +279,92 @@ def test_vendor_safe_rails_logs_are_keys_only_bounded_and_secret_free(tmp_path:`; PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -541,25 +541,35 @@ def test_epic034_request_shaping_closed_rails_generation_requires_env_pins(monke`  
    Approved Plan linkage: Approved Plan → PR-02 — Basic QA check  
19. DR-019  
    Change summary: PR-02b updates `tools/evidence/update_evidence_index.py` to remove misleading PR-02 pytest evidence wording/token posture.  
    Risk assessment: Medium  
    Why it matters: Generated posture logs must not claim `TESTS_PASS_OK` or imply separately indexed pytest evidence without a concrete test transcript.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py`; PR Artifacts → PR-02b HDE-EPIC034.md → `@@ -745,52 +745,52 @@ def _load_epic034_pr01_entries() -> list[dict[str, object]]:`  
    Approved Plan linkage: Approved Plan → PR-02 — Acceptance tokens  
20. DR-020  
    Change summary: PR-02c refreshes the final machine mirror after the complete validation suite.  
    Risk assessment: Low  
    Why it matters: PR-02c is the final diff state and revalidates the evidence posture after prior remediation.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -62,51 +62,51 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -123,91 +123,91 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -235,101 +235,101 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -338,30 +338,30 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
21. DR-021  
    Change summary: PR-02c refreshes final mirror hash and path-proof sidecars.  
    Risk assessment: Low  
    Why it matters: The last mirror refresh must leave hash and proof sidecars coherent.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,6 +1,6 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
22. DR-022  
    Change summary: PR-02c refreshes final historical path-proof timestamps for artifacts affected by the evidence pass.  
    Risk assessment: Low  
    Why it matters: These proof-only changes are acceptable because PR-02c records the full validation suite after the refresh.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
23. DR-023  
    Change summary: PR-02c refreshes prior-epic QA path proofs and EPIC034 doc-delta proof surfaces.  
    Risk assessment: Low  
    Why it matters: The final validation suite confirms path and index coherence for the refreshed proof set.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
24. DR-024  
    Change summary: PR-02c refreshes final human evidence index path proofs.  
    Risk assessment: Low  
    Why it matters: Human index path proofs must be current after index and mirror refreshes.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → PR-02c HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-02 — Evidence outputs  
25. DR-025  
    Change summary: PR-02c records the final full validation suite after the last evidence proof refresh.  
    Risk assessment: Low  
    Why it matters: This closes the previous review blocker: the final artifact state has a complete post-change validation record.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`; PR Artifacts → PR-02c HDE-EPIC034.md → `✅ git diff --check`  
    Approved Plan linkage: Approved Plan → PR-02 — Basic QA check

RCA

A) Bug/Failure statement

PR Artifacts show multiple remediation rounds for PR-02, including `Bugs found, analyze and fix:`, `More bugs:`, and `Bug found:`. The final remediation states it “Re-ran the full EPIC034 PR-02 final validation suite under closed rails and refreshed the governed evidence index/mirror/path-proof state produced by canonical tools.”

B) Root cause(s)

1. Initial request-shaping validation was too weak for required field types and whitespace.  
   Evidence pointer(s): PR Artifacts → PR-02a HDE-EPIC034.md → `For required string fields this only treats` None`and the exact empty string as missing, whereas the previous v1 builder rejected values whose`.strip() `was empty.`  
2. Initial v2 shaping drifted from vendor route contract bytes and serialization requirements.  
   Evidence pointer(s): PR Artifacts → PR-02a HDE-EPIC034.md → `When` path`is`/v2/charts\*`, this still rewrites` birthdate='1990-01-15'`to`15-Jan-1990 `and leaves coordinate inputs as strings if supplied that way`  
3. Initial evidence generation risked false PASS posture or stale generated artifacts.  
   Evidence pointer(s): PR Artifacts → PR-02a HDE-EPIC034.md → `If this generator is run without a successful` update\_evidence\_index.py`/path-proof refresh afterward, the PR-02 check log still reports` evidence\_index\_and\_path\_proof\_posture`as PASS because this check is hard-coded to`True`.`  
4. Vendor route logging initially trusted caller-supplied route strings.  
   Evidence pointer(s): PR Artifacts → PR-02b HDE-EPIC034.md → `When a caller constructs` VendorRequest`directly, any non-empty`route`value is written verbatim to the retry log here, bypassing the path-only`\_route\_label\_from\_url() `fallback.`  
5. Evidence index wording initially implied unsupported pytest token evidence.  
   Evidence pointer(s): PR Artifacts → PR-02b HDE-EPIC034.md → `This can make the evidence index report tests passed for PR-02 even when the targeted tests were not run, so point this token at an actual test transcript or remove it from this generated log row.`

C) Fix in this PR

* Restored stricter validation for string required fields, type handling, v2 date posture, coordinate serialization, route-field tuples, and geocode posture.  
* Added route-conditional `GEO_API_KEY` handling and fail-closed route-contract validation.  
* Hardened route logging so arbitrary `VendorRequest.route` values are not trusted unless they match the known route-label surface.  
* Added `/v1/bodygraphs/simple` contract coverage where legacy simple BodyGraph shaping was required.  
* Removed misleading `TESTS_PASS_OK` posture from the generated request-shaping check-log evidence row.  
* Refreshed governed evidence ledgers, hash sentinels, path proofs, and orientation evidence.  
* Re-ran the full validation suite after the final evidence refresh.

D) Fix verification

* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`.  
* PR Artifacts record `✅ git diff --check`.

Findings

1. F-001 (DR-001): The machine mirror includes the canonical PR-02 request-shaping row.  
   Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   why it matters: This binds the primary PR-02 evidence artifact under the canonical HDAPI v2 artifact key.  
   PF references only when needed: N/A  
2. F-002 (DR-002): Machine mirror sidecars are refreshed.  
   Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`  
   why it matters: The mirror hash sidecar tracks the final mirror bytes.  
   PF references only when needed: N/A  
3. F-003 (DR-003): Broad historical path-proof churn is present but validated after the final refresh.  
   Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   why it matters: Final path validation reduces risk from the broad proof refresh surface.  
   PF references only when needed: N/A  
4. F-004 (DR-004): Current-epic doc-delta path-proof posture remains present and refreshed.  
   Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`  
   why it matters: This preserves the current-epic doc-delta evidence surface used for `DOC_DELTA_PRESENT_OK`.  
   PF references only when needed: N/A  
5. F-005 (DR-005): The PR consumes and refreshes governed HDAPI contract inventory and source-selection baseline artifacts.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`  
   why it matters: HDE-FERM007.2 requires request shaping to use validated contract-map fields.  
   PF references only when needed: N/A  
6. F-006 (DR-006): Contract-inventory support artifacts are refreshed but remain support artifacts, not live conformance proof.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log b/artifacts/vendor/hdapi_v2/openapi_validation.log`  
   why it matters: The PR does not claim live HumanDesignAPI v2 conformance.  
   PF references only when needed: N/A  
7. F-007 (DR-007): The request-shaping snapshot records closed-scope no-claim posture and PF10/OPS-derived input references.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `"live_vendor_call_claim":"NONE","open_rails_vendor_smoke_claim":"NONE","public_reader_change_claim":"NONE"`  
   why it matters: This preserves the Approved Plan boundary.  
   PF references only when needed: N/A  
8. F-008 (DR-008): The request-shaping check log records the required PASS posture.  
   Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `+[v2_bearer_auth_posture] status=PASS`; PR Artifacts → PR-02a HDE-EPIC034.md → `+[v1_legacy_hd_api_key_posture] status=PASS`; PR Artifacts → PR-02a HDE-EPIC034.md → `+[no_secret_values_emitted] status=PASS`  
   why it matters: It proves the core request-shaping posture without claiming live vendor success.  
   PF references only when needed:  
   PF10 — HDE Build Notes, §2.7) HumanDesignAPI v2 Uses Authorization Bearer; v1 Uses HD-Api-Key Header  
   "HumanDesignAPI v2 chart routes use the API key as a Bearer token in the `Authorization` header."  
   "HumanDesignAPI v1 BodyGraph routes use the legacy `HD-Api-Key` request header."  
9. F-009 (DR-009): The human evidence index and hash sentinels are updated and later revalidated.  
   Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
   why it matters: Hash proof is part of the acceptance posture for governed evidence.  
   PF references only when needed: N/A  
10. F-010 (DR-010): `engine/bodygraph/vendor_client.py` is the main runtime-adjacent change and is covered by direct tests.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `diff --git a/engine/bodygraph/vendor_client.py b/engine/bodygraph/vendor_client.py`  
    why it matters: Request-shaping safety depends on this seam remaining bounded and secret-safe.  
    PF references only when needed: N/A  
11. F-011 (DR-011): Vendor-client tests were expanded and later re-run successfully.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
    why it matters: This proves the runtime-adjacent request-shaping behavior is covered by tests.  
    PF references only when needed: N/A  
12. F-012 (DR-012): Evidence-generator tests cover canonical, secret-safe request-shaping artifact generation.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `+def test_epic034_request_shaping_snapshot_is_canonical_secret_safe_and_contract_derived() -> None:`  
    why it matters: This targets the primary governed evidence artifact.  
    PF references only when needed: N/A  
13. F-013 (DR-013): The evidence generator builds request-shaping snapshots from contract and OPS evidence inputs.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `+def build_request_shaping_snapshot(produced: str, contract: dict[str, Any], source_selection: dict[str, Any], ops_summary: dict[str, Any]) -> dict[str, Any]:`  
    why it matters: This implements the planned proof generator.  
    PF references only when needed: N/A  
14. F-014 (DR-014): The evidence updater binds PR-02 request-shaping artifacts into governed ledgers.  
    Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `+ "discovered_physical_path": "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json",`  
    why it matters: This supports `EVIDENCE_INDEX_UPDATED_OK` and mirror update posture.  
    PF references only when needed: N/A  
15. F-015 (DR-015): PR-02b removed misleading generated-log test-evidence wording.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `Removed the EPIC034 PR-02 request_shaping_check note claiming targeted pytest evidence is indexed separately`  
    why it matters: This prevents generated posture logs from overclaiming `TESTS_PASS_OK`.  
    PF references only when needed: N/A  
16. F-016 (DR-016): PR-02b proof refreshes are superseded by PR-02c’s final validation pass.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `Re-ran the full EPIC034 PR-02 final validation suite under closed rails and refreshed the governed evidence index/mirror/path-proof state produced by canonical tools.`  
    why it matters: The final review can rely on the last bundle state, not the incomplete PR-02b validation block.  
    PF references only when needed: N/A  
17. F-017 (DR-017): Route logging is hardened to prevent arbitrary untrusted route values from leaking into logs.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `Hardened vendor retry logging so arbitrary VendorRequest.route values are only used if they match a known whitelist`  
    why it matters: This maintains keys-only and bounded logging posture.  
    PF references only when needed: N/A  
18. F-018 (DR-018): Regression coverage guards route logging and unsupported token evidence.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `Added regression coverage for untrusted route leakage, legacy /v1/bodygraphs/simple request shaping, and the corrected PR-02 token row.`  
    why it matters: This addresses specific defects found during review.  
    PF references only when needed: N/A  
19. F-019 (DR-019): The PR prevents generated check logs from claiming `TESTS_PASS_OK`.  
    Evidence pointer: PR Artifacts → PR-02b HDE-EPIC034.md → `Strengthened the regression test so this evidence row cannot reintroduce either TESTS_PASS_OK or wording that implies separately indexed pytest evidence.`  
    why it matters: Acceptance-token satisfaction must come from real test proof, not generated posture logs.  
    PF references only when needed: N/A  
20. F-020 (DR-020): PR-02c confirms the final remediated request-shaping check row remains limited to `EVIDENCE_PATH_PROOFS_OK`.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `Preserved the corrected PR-02 request-shaping evidence posture: the epic034.pr02.request_shaping_check row remains scoped to EVIDENCE_PATH_PROOFS_OK and does not claim TESTS_PASS_OK.`  
    why it matters: This closes the prior unsupported token-satisfaction issue.  
    PF references only when needed: N/A  
21. F-021 (DR-021): Final mirror sidecars are refreshed after the full validation run.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `Refreshed the machine mirror path proof, including the final mirror body hash and produced timestamp.`  
    why it matters: This confirms final proof freshness after the last change.  
    PF references only when needed: N/A  
22. F-022 (DR-022): Final historical proof refreshes do not create scope drift because they are proof-only and validated.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `Refreshed human evidence index path proofs and orientation proof timestamps after the final validation run.`  
    why it matters: Proof refreshes are bounded by the final validation suite.  
    PF references only when needed: N/A  
23. F-023 (DR-023): Current-epic doc-delta proof surfaces remain in the final mirror.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-17T23:40:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
    why it matters: The Approved Plan includes `DOC_DELTA_PRESENT_OK`.  
    PF references only when needed: N/A  
24. F-024 (DR-024): Final human evidence index path proofs are refreshed.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`  
    why it matters: Index path-proof freshness is part of governed evidence integrity.  
    PF references only when needed: N/A  
25. F-025 (DR-025): The final validation suite is complete after the final evidence refresh.  
    Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`; PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`; PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
    why it matters: This removes the previous blocker and supports PR acceptability.  
    PF references only when needed: N/A

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.2  
   Current PF09 status: Task status: Not done; Subtask status: Not done  
   Status recommendation: change to Done  
   Why this status posture is supported: PR Artifacts prove request shaping is implemented and evidenced for HDE-FERM007.2 with governed contract-map input, OPS-01 fact-summary input, canonical request-shaping snapshot, request-shaping check log, path proofs, evidence index/mirror updates, targeted tests, and full final validation after remediation. The recommendation applies only to HDE-FERM007.2; parent HDE-FERM007 remains Not done because later subtasks remain outside PR-02.  
   Evidence pointer(s): PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Evidence pointer(s): PR Artifacts → PR-02a HDE-EPIC034.md → `+[v2_bearer_auth_posture] status=PASS`  
   Evidence pointer(s): PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
   PF proof excerpt(s) when PF09 is relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
   "Task ID: HDE-FERM007"  
   "Task status: Not done"  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints  
   "Replace or gate legacy vendor request shaping with v2-aware shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates. Request shaping must use validated contract-map fields, canonical body construction where governed artifacts are emitted, and the v2 auth model. Exact secret/config key names must be pinned in PF05 and PF07 before execution."  
   "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `JSON_CANONICAL_CHECK_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
* `EVIDENCE_INDEX_UPDATED_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
* `MACHINE_MIRROR_UPDATED_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"index.machine_mirror","discovered_physical_path":"artifacts/evidence_index.jsonl","produced_at_utc":"2026-06-17T23:40:59Z","proof_anchor":"artifacts/evidence_index.jsonl.path_proof.txt","role":"self_record","sha256":"42b40525bff8613d6b937ef5028d0841ea9f89c676fd987ae4ef6439abae20df","size_bytes":149875}`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → PR-02a HDE-EPIC034.md → `+path: artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
  * PR Artifacts → PR-02a HDE-EPIC034.md → `+path: audit/qa/hde-epic034/pr-02/request_shaping_check.log`  
* `TESTS_PASS_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"epic034.pr01.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 current-epic draft/staging doc-delta surface for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-17T23:40:59Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"epic034.pr01.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-01 epic-scoped QA meta doc-delta capture for HDE-FERM007.1 source-selection evidence","produced_at_utc":"2026-06-17T23:40:59Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr01_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf","size_bytes":1337,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
  Type: Canonical JSON snapshot  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"base_url_env_var":"HD_API_BASE_URL"`  
  * `"v2_auth_header_posture":"Authorization: Bearer <redacted>"`  
  * `"v1_legacy_auth_header_posture":"HD-Api-Key: <redacted>"`  
  * `"live_vendor_call_claim":"NONE"`  
    sha256: `db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45`  
* Path: `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
  * `size_bytes: 4325`  
  * `produced_at_utc: 2026-06-17T08:20:37Z`  
    sha256: `db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45`  
* Path: `audit/qa/hde-epic034/pr-02/request_shaping_check.log`  
  Type: LF-terminated check log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `[closed_rails_generation] status=PASS`  
  * `[v2_bearer_auth_posture] status=PASS`  
  * `[v1_legacy_hd_api_key_posture] status=PASS`  
  * `status=PASS`  
    sha256: `ae7273b7b235c2d66861392f062ea1175a2b1f8c19d5537d7000c5c125a30699`  
* Path: `audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: audit/qa/hde-epic034/pr-02/request_shaping_check.log`  
  * `size_bytes: 647`  
  * `produced_at_utc: 2026-06-17T08:20:37Z`  
    sha256: `ae7273b7b235c2d66861392f062ea1175a2b1f8c19d5537d7000c5c125a30699`  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.human_index"`  
  * `"discovered_physical_path":"docs/evidence/INDEX.json"`  
    sha256: `c2187c42cd4fefcd89872377f748b22d6f4c4e146d2798d510cb7ffd6b789362`  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Evidence Mirror  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.machine_mirror"`  
  * `"discovered_physical_path":"artifacts/evidence_index.jsonl"`  
  * `"role":"self_record"`  
    sha256: `42b40525bff8613d6b937ef5028d0841ea9f89c676fd987ae4ef6439abae20df`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
  Type: Current-epic doc-delta draft/staging surface  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf`  
* Path: `audit/qa/hde-epic034/00_meta/doc_deltas.md`  
  Type: Current-epic QA meta doc-delta capture  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `6d38510d2ceec560c6bbf53bbe79d38fff606dd9f8478081024512d27efeb3cf`

C) Test/CI proof

* Job or test name: `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing  
* Job or test name: `git diff --check`  
  Pass indicator copied verbatim: `✅ git diff --check`  
  Where it appears in PR Artifacts: PR Artifacts → PR-02c HDE-EPIC034.md → Testing

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

PF09 Impact Summary

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.2  
   Current status if evidenced: Task status: Not done; Subtask status: Not done  
   Status action: change to Done  
   Evidence pointer(s): PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Linked Findings item(s): F-001; F-007; F-008; F-010; F-011; F-013; F-014; F-025  
   Linked CHG item(s), if any: CHG-006

Doc Delta Detection Workflow

CHG-001  
Change claim type: behavior or output  
Change claim: PR-02 implements v2-aware request shaping for the governed HumanDesignAPI v2 chart route family while preserving legacy v1 BodyGraph header posture.  
Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `"v2_auth_header_posture":"Authorization: Bearer <redacted>"`  
Canon basis: CANON ALIGNED

CHG-002  
Change claim type: configuration or environment  
Change claim: PR-02 uses `HD_API_BASE_URL` as canonical and treats `HDAPI_BASE_URL` as a temporary compatibility alias only.  
Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `"base_url_env_var":"HD_API_BASE_URL"`  
Canon basis: CANON ALIGNED

CHG-003  
Change claim type: schemas or data model  
Change claim: PR-02 emits a canonical request-shaping JSON snapshot derived from governed contract inventory and OPS-01 fact summary.  
Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG-004  
Change claim type: governed paths or artifact families  
Change claim: PR-02 binds request-shaping artifacts to the human evidence index and machine mirror with path proofs.  
Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"epic034.pr02.request_shaping_check","discovered_physical_path":"audit/qa/hde-epic034/pr-02/request_shaping_check.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 LF-terminated request-shaping posture check log for v2 Bearer, v1 HD-Api-Key, geocode, base URL alias, and secret-safety posture","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"log","schema_version":"1.0","sha256":"ae7273b7b235c2d66861392f062ea1175a2b1f8c19d5537d7000c5c125a30699","size_bytes":647,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG-005  
Change claim type: tokens, rails, or evidence posture  
Change claim: PR-02 keeps closed rails, no live vendor call, no public Reader change, no open-rails smoke claim, and no runtime conformance claim.  
Evidence pointer: PR Artifacts → PR-02a HDE-EPIC034.md → `"live_vendor_call_claim":"NONE","open_rails_vendor_smoke_claim":"NONE","public_reader_change_claim":"NONE"`  
Canon basis: CANON ALIGNED

CHG-006  
Change claim type: PF09 status-impact requirement  
Change claim: PR-02 evidence supports changing PF09.5 HDE-FERM007.2 from Not done to Done, while leaving parent HDE-FERM007 unchanged.  
Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG: CHG-006

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM007.2 \- Update request shaping for v2 endpoints

Canon basis: CANON ALIGNED

Impacted PF09 task ID(s): HDE-FERM007

Impacted PF09 subtask ID(s): HDE-FERM007.2

PF09 status action: change to Done

Delta: Update HDE-FERM007.2 subtask status from Not done to Done, and preserve parent HDE-FERM007 as Not done until later HDE-FERM007 subtasks are reviewed.

Why: PR Artifacts provide request-shaping implementation evidence, canonical request-shaping snapshot, check log, path proofs, governed index/mirror updates, targeted tests, and final validation for the exact HDE-FERM007.2 slice.

Evidence pointer: PR Artifacts → PR-02c HDE-EPIC034.md → `{"artifact_key":"hdapi_v2.request_shaping","discovered_physical_path":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-02 canonical request-shaping snapshot for HDE-FERM007.2 derived from governed HDAPI v2 contract inventory and OPS-01 fact summary","produced_at_utc":"2026-06-17T08:20:37Z","proof_anchor":"artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt","record_type":"epic034_pr02_request_shaping","role":"snapshot","schema_version":"1.0","sha256":"db21ab37760dd94b2d16187a72ba929d792853a3a22cde41dc374629b07ada45","size_bytes":4325,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`

Canon proof excerpt:  
"Task ID: HDE-FERM007"  
"Task status: Not done"  
"Replace or gate legacy vendor request shaping with v2-aware shaping for POST /v2/charts, POST /v2/charts/simple, and POST /v2/charts/coordinates. Request shaping must use validated contract-map fields, canonical body construction where governed artifacts are emitted, and the v2 auth model. Exact secret/config key names must be pinned in PF05 and PF07 before execution."  
"Subtask status: Not done"

## 2.11) PR-03 HDE-EPIC034

Artifact Map

PR Name: PR-03

PR Artifacts Bundle: PR-03 HDE-EPIC034.md

Approved Plan: r4 Implementation Plan HDE-EPIC034.md

Output: PR Final Review

Review Summary

* The PR implements HDE-EPIC034 PR-03 response-envelope mapping proof generation for v2 `StandardResponse` semantics, preserving response type, success status, `errorCode`, data payload identity posture, and route variant.  
* The PR aligns with the Approved Plan’s PR-03 scope: HDE-FERM007.3 only, closed rails, no live vendor calls, no public Reader output change, no HDE-FERM008.4 normalized data path proof, no open-rails smoke claim, and no AI transformation scope.  
* The PR adds governed response-mapping evidence: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`, its path proof, `audit/qa/hde-epic034/pr-03/response_mapping_check.log`, and its path proof.  
* The PR includes remediation for discovered bugs: PR-03 doc-delta mislabeling, route-specific schema drift, stale public-doc refresh output, missing `StandardResponse` field validation, hard-coded internal-locus inspection claims, and stale PR-03 index rows after output cleanup.  
* Final PR Artifacts record the required validation suite as passed, including generator refresh, evidence index update/check, targeted pytest, orientation update/check, path validation, mirror schema check, evidence-index hash check, LF check, and `git diff --check`.  
* Diff review covers all 79 diff hunks across 67 file patches.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.3.  
* The review supports change to Done for HDE-FERM007.3 only; no parent HDE-FERM007 status change is supported.  
* RCA is included because PR Artifacts explicitly include bug and remediation history.

Diff Review

1. DR-001  
   Change summary: Updates `artifacts/evidence_index.jsonl`, including PR-03 response-mapping, doc-delta, and final governed evidence rows.  
   Risk assessment: Medium  
   Why it matters: The machine mirror is acceptance-bearing evidence; PR-03 rows must be correctly scoped and stale rows must be removed.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → Diff → `@@ -62,51 +62,51 @@`; PR Artifacts → Diff → `@@ -123,91 +123,91 @@`; PR Artifacts → Diff → `@@ -235,101 +235,103 @@`; PR Artifacts → Diff → `@@ -338,30 +340,30 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — v2 response-envelope mapping into HDE internal inputs  
2. DR-002  
   Change summary: Updates machine mirror path proof, hash sentinel, and hash sentinel path proof.  
   Risk assessment: Low  
   Why it matters: Mirror byte changes require coherent sidecars and path proofs.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → Diff → `@@ -1,6 +1,6 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
3. DR-003  
   Change summary: Refreshes narrative router parity path proofs.  
   Risk assessment: Medium  
   Why it matters: These are historical proof-refresh hunks outside direct PR-03 behavior, so final validation must prove global evidence-path coherence.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
4. DR-004  
   Change summary: Refreshes HDAPI v2 contract inventory, endpoint reference, anomaly, OpenAPI validation, and related path-proof artifacts.  
   Risk assessment: Medium  
   Why it matters: PR-03 response mapping depends on contract-map and source-inventory evidence; drift here could invalidate envelope mapping if not tested.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt b/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/endpoint_reference.csv b/artifacts/vendor/hdapi_v2/endpoint_reference.csv`; PR Artifacts → Diff → `@@ -1,6 +1,6 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt b/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md b/artifacts/vendor/hdapi_v2/known_anomalies.md`; PR Artifacts → Diff → `@@ -1,15 +1,15 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt b/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log b/artifacts/vendor/hdapi_v2/openapi_validation.log`; PR Artifacts → Diff → `@@ -1,26 +1,26 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt b/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Discovery  
5. DR-005  
   Change summary: Refreshes accepted PR-02 request-shaping snapshot and path proof.  
   Risk assessment: Medium  
   Why it matters: PR-03 consumes PR-02 request-shaping as a dependency; refreshes must preserve baseline semantics and proof integrity.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Discovery  
6. DR-006  
   Change summary: Adds the canonical response-mapping snapshot and its path proof.  
   Risk assessment: Low  
   Why it matters: This is the primary planned evidence output for HDE-FERM007.3.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`; PR Artifacts → Diff → `@@ -0,0 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
7. DR-007  
   Change summary: Refreshes source inventory, source-selection, and v1 legacy guard dependency artifacts.  
   Risk assessment: Medium  
   Why it matters: Response mapping must reuse accepted PR-01/PR-02 baseline evidence rather than duplicate or reinterpret it.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json b/artifacts/vendor/hdapi_v2/source_inventory.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md b/artifacts/vendor/hdapi_v2/source_inventory.md`; PR Artifacts → Diff → `@@ -1,28 +1,28 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; PR Artifacts → Diff → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Discovery  
8. DR-008  
   Change summary: Refreshes writer path-proof artifacts.  
   Risk assessment: Medium  
   Why it matters: These are proof-refresh hunks outside direct response mapping; acceptance depends on final evidence validation.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
9. DR-009  
   Change summary: Refreshes doc-delta surfaces and path proofs, including current EPIC034 doc-delta content.  
   Risk assessment: Medium  
   Why it matters: PR-03 fixes prior doc-delta mislabeling and must bind current doc-delta surfaces to HDE-FERM007.3, not PR-01.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md b/audit/docdeltas/hde-epic034_doc_deltas.md`; PR Artifacts → Diff → `@@ -1,29 +1,32 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → PR-03 — Acceptance tokens  
10. DR-010  
    Change summary: Refreshes narrative-gate and topology evidence path proofs.  
    Risk assessment: Medium  
    Why it matters: Orientation and evidence skeleton updates are broad governed proof churn; final validation must confirm coherence.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt b/audit/gates/topology/orientation_demo.txt`; PR Artifacts → Diff → `@@ -1,4 +1,4 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Basic QA check  
11. DR-011  
    Change summary: Refreshes EPIC030 QA evidence path proofs.  
    Risk assessment: Medium  
    Why it matters: Historical proof-only churn must remain governed by final path and mirror validation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
12. DR-012  
    Change summary: Refreshes EPIC033 QA metadata, acceptance-map viability, and token-evidence path proofs.  
    Risk assessment: Medium  
    Why it matters: These historical proof refreshes are outside PR-03 behavior but affect governed evidence validation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log b/audit/qa/hde-epic033/acceptance_map_viability.log`; PR Artifacts → Diff → `@@ -1,8 +1,8 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt b/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt b/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
13. DR-013  
    Change summary: Updates EPIC034 QA meta doc-delta surface and path proof for PR-03 response mapping.  
    Risk assessment: Low  
    Why it matters: This binds current-epic doc-delta posture to PR-03/HDE-FERM007.3.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md b/audit/qa/hde-epic034/00_meta/doc_deltas.md`; PR Artifacts → Diff → `@@ -1,29 +1,32 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Acceptance tokens  
14. DR-014  
    Change summary: Refreshes PR-01 source-selection and PR-02 request-shaping check logs and path proofs.  
    Risk assessment: Medium  
    Why it matters: PR-03 depends on prior accepted slices, but must not overwrite their semantics or mis-scope their rows.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log b/audit/qa/hde-epic034/pr-01/source_selection_check.log`; PR Artifacts → Diff → `@@ -1,19 +1,19 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log b/audit/qa/hde-epic034/pr-02/request_shaping_check.log`; PR Artifacts → Diff → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Discovery  
15. DR-015  
    Change summary: Adds the PR-03 response-mapping check log and path proof.  
    Risk assessment: Low  
    Why it matters: The check log is the planned LF-terminated posture proof for response-envelope mapping.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log b/audit/qa/hde-epic034/pr-03/response_mapping_check.log`; PR Artifacts → Diff → `@@ -0,0 +1,19 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -0,0 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
16. DR-016  
    Change summary: Refreshes EPIC033 acceptance map and path proof.  
    Risk assessment: Medium  
    Why it matters: Historical acceptance-map proof churn is acceptable only with final evidence validation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/acceptance_map_epic033.json b/docs/acceptance_map_epic033.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/acceptance_map_epic033.json.path_proof.txt b/docs/acceptance_map_epic033.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
17. DR-017  
    Change summary: Updates the human Evidence Index, hash sentinel, and path proofs.  
    Risk assessment: Medium  
    Why it matters: Acceptance tokens rely on same-PR human index, hash, mirror, and proof updates.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
18. DR-018  
    Change summary: Expands `tests/evidence/test_hdapi_v2_contract_inventory.py` for response-mapping generation, route/envelope preservation, schema-gap posture, stale-output cleanup, token coverage, schema drift, and internal-locus checks.  
    Risk assessment: Low  
    Why it matters: Tests directly cover the planned PR-03 behavior and the review-found bugs.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -522,54 +522,242 @@ def test_epic034_request_shaping_rejects_ops01_blocker_wording() -> None:`  
    Approved Plan linkage: Approved Plan → PR-03 — Basic QA check  
19. DR-019  
    Change summary: Updates `tools/evidence/generate_hdapi_v2_contract_inventory.py` imports/constants and derived-output cleanup sets for PR-03.  
    Risk assessment: Medium  
    Why it matters: Public-doc refresh cleanup must not leave stale PR-03 closed-rails derived outputs behind.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -13,120 +13,137 @@ import argparse`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
20. DR-020  
    Change summary: Adds route-specific `StandardResponse` parsing and validation.  
    Risk assessment: Medium  
    Why it matters: Response-envelope proof must fail closed when `success`, `errorCode`, `type`, or `data` are missing or drift by route.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -306,50 +323,71 @@ def success_envelope(method: dict[str, Any], *, version: str) -> str:`  
    Approved Plan linkage: Approved Plan → PR-03 — Implementation requirements  
21. DR-021  
    Change summary: Updates route-tier parsing, OpenAPI validation, and anomaly text handling around contract inputs.  
    Risk assessment: Medium  
    Why it matters: Contract-input validation feeds the response-mapping proof and must not allow unsupported schema drift to pass as valid evidence.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -397,50 +435,51 @@ def parse_tier_map(llms_full: str) -> dict[str, str:`; PR Artifacts → Diff → `@@ -457,61 +496,63 @@ def validate_suspect_openapi(body: bytes, source_row: dict[str, Any]) -> tuple[b`; PR Artifacts → Diff → `@@ -544,50 +585,55 @@ def build_anomaly_text(produced: str, suspect_ok: bool, suspect_info: dict[str,`  
    Approved Plan linkage: Approved Plan → PR-03 — Discovery  
22. DR-022  
    Change summary: Adds response-mapping snapshot and check-log generation, including internal-locus inspection, schema-gap recording, no-compatibility-by-inference posture, and non-claims.  
    Risk assessment: Medium  
    Why it matters: This is the core PR-03 evidence logic and must remain proof-level without claiming full normalized data path proof.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -891,97 +937,277 @@ def build_request_shaping_check_log(produced: str, snapshot: dict[str, Any], *`  
    Approved Plan linkage: Approved Plan → PR-03 — Implementation requirements  
23. DR-023  
    Change summary: Wires response-mapping outputs into render output generation.  
    Risk assessment: Low  
    Why it matters: The generator must produce the planned response-mapping snapshot and PR-scoped log under closed rails.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -1055,53 +1281,56 @@ def render_outputs(produced: str, fetched: dict[str, dict[str, Any]], bodies: di`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
24. DR-024  
    Change summary: Updates `tools/evidence/update_evidence_index.py` to add PR-03 response-mapping rows, doc-delta rows, approved tokens, and stale-key filtering.  
    Risk assessment: Medium  
    Why it matters: Evidence index registration must scope PR-03 rows correctly and remove stale PR-01/PR-03 rows when outputs are absent.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py`; PR Artifacts → Diff → `@@ -486,57 +486,66 @@ EPIC032_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → Diff → `@@ -689,68 +698,50 @@ EPIC034_PR01_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`; PR Artifacts → Diff → `@@ -773,50 +764,112 @@ EPIC034_PR02_PRIMARY_ARTIFACTS: list[dict[str, object]] = [`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs  
25. DR-025  
    Change summary: Wires PR-03 rows into the human index loader and prunes superseded PR-03 keys.  
    Risk assessment: Low  
    Why it matters: Final evidence generation must not keep stale PR-03 response-mapping rows after public-doc refresh deletes derived outputs.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/update_evidence_index.py b/tools/evidence/update_evidence_index.py`; PR Artifacts → Diff → `@@ -1099,73 +1152,76 @@ def _normalize_index_entry(entry: Mapping[str, object]) -> dict[str, object]:`  
    Approved Plan linkage: Approved Plan → PR-03 — Evidence outputs

RCA

A) Bug/Failure statement

PR Artifacts record multiple bug rounds after the initial PR-03 implementation. The first bug round says the current EPIC034 doc-delta path was still loaded as PR-01 evidence, route-specific schema expectations were not enforced during generation, and public-doc refresh could leave stale PR-03 response-mapping outputs. A later bug round says `StandardResponse` field drift, hard-coded internal-locus inspection, and stale PR-03 index rows after derived-output deletion still needed remediation.

B) Root cause(s)

1. The initial doc-delta registration reused current EPIC034 doc-delta surfaces under PR-01 artifact rows instead of PR-03/HDE-FERM007.3 rows.  
   Evidence pointer(s): PR Artifacts → Actions taken → `This path is still loaded by` EPIC034\_PR01\_PRIMARY\_ARTIFACTS`in`tools/evidence/update\_evidence\_index.py `as the PR-01/HDE-FERM007.1 doc-delta evidence, but the file now declares PR-03/HDE-FERM007.3 response-mapping evidence.`  
2. Route-specific response schema expectations were initially asserted only against checked-in artifacts, not enforced during generation.  
   Evidence pointer(s): PR Artifacts → Actions taken → `If the source-cache contract drifts but still uses an allowed schema name, for example` /v2/charts/simple`reporting`ChartResult`instead of`ChartSimpleResult`, this check accepts it and the generated PR-03 check log still reports PASS because it only checks membership in the same allowed set.`  
3. Public-doc refresh cleanup initially omitted PR-03 closed-rails derived response-mapping outputs.  
   Evidence pointer(s): PR Artifacts → Actions taken → `Because the response-mapping snapshot/check log are not included in that cleanup set, a public-docs refresh can leave stale` response\_mapping.snapshot.json`and`response\_mapping\_check.log `on disk`  
4. The response-envelope proof initially hard-coded `success` and `errorCode` posture instead of validating the `StandardResponse` fields.  
   Evidence pointer(s): PR Artifacts → Actions taken → `For a source-cache refresh where the v2` StandardResponse`schema still wraps`ChartResult`but drops or renames`success`or`errorCode`, this code still emits PASS evidence saying those fields are preserved`  
5. Internal-locus inspection was initially hard-coded, which could leave PASS evidence claiming inspection of missing files.  
   Evidence pointer(s): PR Artifacts → Actions taken → `When any of the cited BodyGraph files are moved or removed, the generator still emits governed evidence saying those loci were inspected and records a schema-gap posture, because this block is hard-coded instead of derived from existence/content checks.`  
6. PR-03 stale index rows were not pruned when public-doc refresh removed PR-03 derived outputs.  
   Evidence pointer(s): PR Artifacts → Actions taken → `_load_human_index()` does not filter existing `epic034.pr03.*`/`hdapi_v2.response_mapping` rows the way it filters PR-02 superseded keys.\`

C) Fix in this PR

* Registered current EPIC034 doc-delta surfaces as PR-03/HDE-FERM007.3 evidence and superseded stale PR-01 doc-delta rows.  
* Added route-specific expected response type/data schema pairs for response-envelope generation.  
* Grouped PR-02 request-shaping and PR-03 response-mapping outputs into a closed-rails derived output cleanup set for public-doc refresh.  
* Added `StandardResponse` field validation for `success`, `errorCode`, `type`, and `data`.  
* Carried response-envelope fields into the response-mapping proof and check logic.  
* Added fail-closed path+hash inspection for cited internal BodyGraph/compat loci.  
* Added PR-03 superseded-key filtering for response-mapping and doc-delta rows.  
* Added regression tests for stale-output cleanup, route-specific schema drift, approved-token coverage, stale PR-03 index row cleanup, `StandardResponse` field drift, and missing internal loci.

D) Fix verification

* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`.  
* PR Artifacts record `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`.  
* PR Artifacts record `✅ git diff --check`.

Findings

1. F-001 (DR-001): The machine mirror includes canonical PR-03 response-mapping and check-log rows.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   why it matters: This binds the primary PR-03 artifact to the governed evidence mirror.  
   PF references only when needed: N/A  
2. F-002 (DR-002): Machine mirror hash and path-proof sidecars are updated for the final mirror.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"index.machine_mirror","discovered_physical_path":"artifacts/evidence_index.jsonl","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"artifacts/evidence_index.jsonl.path_proof.txt","role":"self_record","sha256":"9d74c1eddc8ba5f0a2262860f172589dc9aa63b43e69038dfcdf8a981509bfe0","size_bytes":151202}`  
   why it matters: The mirror self-record proves final machine mirror identity.  
   PF references only when needed: N/A  
3. F-003 (DR-003): Narrative router proof-only refreshes are present and covered by final path validation.  
   Evidence pointer: PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   why it matters: Broad path-proof churn needs final proof validation.  
   PF references only when needed: N/A  
4. F-004 (DR-004): HDAPI contract-map and source-validation artifacts are refreshed and support PR-03 contract-derived response mapping.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`  
   why it matters: PR-03 response-envelope proof depends on the governed contract map.  
   PF references only when needed: N/A  
5. F-005 (DR-005): Request-shaping snapshot remains present as a dependency artifact.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
   why it matters: PR-03 consumes PR-02 request-shaping proof rather than reimplementing it.  
   PF references only when needed: N/A  
6. F-006 (DR-006): The response-mapping snapshot preserves envelope fields, route variants, schema-gap posture, and explicit non-claims.  
   Evidence pointer: PR Artifacts → Diff → `+"ai_scope_claim":"NONE","data_payload_body_emitted":false,"data_payload_identity_posture":"identity is proven only as an envelope data-field preservation posture; no vendor payload body is serialized"`  
   why it matters: This satisfies the Approved Plan’s proof-level mapping scope while avoiding live-conformance overclaim.  
   PF references only when needed: N/A  
7. F-007 (DR-007): Source-selection and v1 legacy baseline artifacts remain in the dependency set.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
   why it matters: PR-03 depends on accepted PR-01 route-family baseline evidence.  
   PF references only when needed: N/A  
8. F-008 (DR-008): Writer proof-only refreshes do not expand PR-03 scope.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`  
   why it matters: These are governed evidence refreshes, not response-mapping behavior changes.  
   PF references only when needed: N/A  
9. F-009 (DR-009): Current EPIC034 doc-delta rows are now scoped to PR-03/HDE-FERM007.3.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"epic034.pr03.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 current-epic draft/staging doc-delta surface for HDE-FERM007.3 response-mapping evidence","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr03_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f","size_bytes":1879,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   why it matters: This remediates the earlier misbinding of PR-03 doc-delta evidence as PR-01 evidence.  
   PF references only when needed: N/A  
10. F-010 (DR-010): Orientation and narrative proof refreshes are validated after regeneration.  
    Evidence pointer: PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
    why it matters: Orientation drift is a recurring evidence integrity risk.  
    PF references only when needed: N/A  
11. F-011 (DR-011): EPIC030 path-proof churn is proof-only and validated.  
    Evidence pointer: PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
    why it matters: Historical evidence refreshes do not block when path validation passes.  
    PF references only when needed: N/A  
12. F-012 (DR-012): EPIC033 QA proof refreshes are historical evidence refreshes, not PR-03 scope drift.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log b/audit/qa/hde-epic033/acceptance_map_viability.log`  
    why it matters: They do not introduce new PR-03 implementation behavior.  
    PF references only when needed: N/A  
13. F-013 (DR-013): QA meta doc-delta surface is also scoped to PR-03/HDE-FERM007.3.  
    Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"epic034.pr03.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 epic-scoped QA meta doc-delta capture for HDE-FERM007.3 response-mapping evidence","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr03_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f","size_bytes":1879,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
    why it matters: This completes the current-epic doc-delta evidence pair for the PR-03 slice.  
    PF references only when needed: N/A  
14. F-014 (DR-014): Prior PR-01 and PR-02 evidence surfaces remain refreshed and indexed as dependencies, not re-scoped as PR-03 behavior.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log b/audit/qa/hde-epic034/pr-02/request_shaping_check.log`  
    why it matters: PR-03 depends on request-shaping evidence but does not redo request shaping.  
    PF references only when needed: N/A  
15. F-015 (DR-015): The PR-03 check log records all required response-mapping posture checks as PASS.  
    Evidence pointer: PR Artifacts → Diff → `+[response_type_preservation] status=PASS`; PR Artifacts → Diff → `+[success_status_handling] status=PASS`; PR Artifacts → Diff → `+[no_normalized_data_path_proof_claimed] status=PASS`  
    why it matters: This is the PR-scoped evidence that response mapping stays proof-level and does not claim HDE-FERM008.4.  
    PF references only when needed: N/A  
16. F-016 (DR-016): EPIC033 acceptance-map refresh remains historical and does not alter PR-03 scope.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/acceptance_map_epic033.json b/docs/acceptance_map_epic033.json`  
    why it matters: Historical refreshes are not PR-03 acceptance sources except through global evidence validation.  
    PF references only when needed: N/A  
17. F-017 (DR-017): Human Evidence Index, hash sentinel, and proofs are updated after PR-03 row changes.  
    Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"index.human_index","discovered_physical_path":"docs/evidence/INDEX.json","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"docs/evidence/INDEX.json.path_proof.txt","role":"snapshot","sha256":"c7833d2378df7179b8105f036c0d44326acd68857bffe66bfbe0c0c4bb5d9015","size_bytes":73664}`  
    why it matters: The human index is part of the governed acceptance evidence set.  
    PF references only when needed: N/A  
18. F-018 (DR-018): Targeted tests cover response-mapping canonical generation, route/envelope preservation, schema-gap posture, stale cleanup, schema drift, and missing internal loci.  
    Evidence pointer: PR Artifacts → Diff → `+def test_epic034_response_mapping_snapshot_is_canonical_secret_safe_and_contract_derived() -> None:`  
    why it matters: The new tests directly cover the planned behavior and the review-found defects.  
    PF references only when needed: N/A  
19. F-019 (DR-019): Closed-rails derived output cleanup now includes PR-03 response-mapping outputs.  
    Evidence pointer: PR Artifacts → Actions taken → `Fixed stale public-doc refresh cleanup by grouping PR-02 request-shaping and PR-03 response-mapping outputs into one closed-rails derived output set`  
    why it matters: Public-doc refresh must not leave stale closed-rails PR-03 evidence on disk.  
    PF references only when needed: N/A  
20. F-020 (DR-020): `StandardResponse` field validation was added.  
    Evidence pointer: PR Artifacts → Actions taken → `Added StandardResponse field validation so v2 contract inventory and response-mapping evidence now fail closed unless success, errorCode, type, and data are present in both required fields and schema properties.`  
    why it matters: Response field preservation must be proven from contract data, not hard-coded posture.  
    PF references only when needed: N/A  
21. F-021 (DR-021): Contract parsing and validation logic was strengthened around source inputs.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`  
    why it matters: The response-mapping artifact depends on validated contract-map facts.  
    PF references only when needed: N/A  
22. F-022 (DR-022): The generator records inspected internal loci with path and hash evidence, schema-gap status, and no-compatibility-by-inference posture.  
    Evidence pointer: PR Artifacts → Diff → `+"inspected_internal_loci":[{"path":"engine/bodygraph/vendor_client.py","sha256":"41502528b831da35939bd283162c19327b9a79ea980123a0f43537b19cbd0b5f"}`  
    why it matters: The Approved Plan required discovery-first inspection before claiming internal-target posture.  
    PF references only when needed: N/A  
23. F-023 (DR-023): The generator emits the response-mapping snapshot and PR-03 check log.  
    Evidence pointer: PR Artifacts → Diff → `+ response_snapshot = build_response_mapping_snapshot(produced, contract, snapshot, request_snapshot, ops_summary)`  
    why it matters: Planned evidence artifacts are produced by the canonical generator path.  
    PF references only when needed: N/A  
24. F-024 (DR-024): The evidence updater registers PR-03 response-mapping and doc-delta rows with approved tokens.  
    Evidence pointer: PR Artifacts → Diff → `+ "artifact_key": "hdapi_v2.response_mapping",`  
    why it matters: Acceptance evidence must be indexed under governed artifact keys and not under stale PR-01 rows.  
    PF references only when needed: N/A  
25. F-025 (DR-025): The human index loader filters superseded PR-03 rows and loads current PR-03 rows.  
    Evidence pointer: PR Artifacts → Diff → `+ not in EPIC034_PR03_SUPERSEDED_INDEX_KEYS`  
    why it matters: This resolves stale PR-03 rows after public-doc refresh removes derived response-mapping outputs.  
    PF references only when needed: N/A  
26. F-026: Final validation suite is complete and recorded after the latest remediation.  
    Evidence pointer: PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
    why it matters: This proves the final PR state, not just an earlier intermediate state.  
    PF references only when needed: N/A

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.3  
   Current PF09 status: Task status: Not done; Subtask status: Not done  
   Status recommendation: change to Done  
   Why this status posture is supported: PR Artifacts prove HDE-FERM007.3 response-envelope mapping at the proof level with canonical response-mapping snapshot, PR-scoped response-mapping check log, schema-gap posture, internal-locus inspection, no compatibility-by-inference posture, no normalized-data-path proof claim, no live-conformance claim, evidence index/mirror binding, path proofs, targeted tests, and full validation. The recommendation applies only to HDE-FERM007.3; parent HDE-FERM007 remains Not done because later subtasks remain outside PR-03.  
   Evidence pointer(s): PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Evidence pointer(s): PR Artifacts → Diff → `+[internal_target_posture_or_schema_gap_recorded] status=PASS`  
   Evidence pointer(s): PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
   PF proof excerpt(s) when PF09 is relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
   "Task ID: HDE-FERM007"  
   "Task status: Not done"  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.3 \- Normalize v2 response envelopes into HDE BodyGraph and chart inputs  
   "Map the v2 response envelope into the HDE internal data model used by BodyGraph cache, compatibility, sampler, and admin surfaces. The mapping must preserve response type, success status, errorCode, data payload identity, and route variant. It must avoid logging payload bodies or secrets and must keep public Reader output numeric-free."  
   "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `JSON_CANONICAL_CHECK_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
* `EVIDENCE_INDEX_UPDATED_OK`  
  * PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  * PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
* `MACHINE_MIRROR_UPDATED_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"index.machine_mirror","discovered_physical_path":"artifacts/evidence_index.jsonl","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"artifacts/evidence_index.jsonl.path_proof.txt","role":"self_record","sha256":"9d74c1eddc8ba5f0a2262860f172589dc9aa63b43e69038dfcdf8a981509bfe0","size_bytes":151202}`  
  * PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
  * PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → Diff → `+path: artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
  * PR Artifacts → Diff → `+path: audit/qa/hde-epic034/pr-03/response_mapping_check.log`  
* `TESTS_PASS_OK`  
  * PR Artifacts → Actions taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr03.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 current-epic draft/staging doc-delta surface for HDE-FERM007.3 response-mapping evidence","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr03_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f","size_bytes":1879,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr03.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 epic-scoped QA meta doc-delta capture for HDE-FERM007.3 response-mapping evidence","produced_at_utc":"2026-06-18T02:44:06Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr03_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f","size_bytes":1879,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
  Type: Canonical JSON snapshot  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"response_envelope_mapping_scope":"HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only"`  
  * `"schema_gap_status":"GAP_RECORDED"`  
  * `"normalized_data_path_proof_claim":"NONE"`  
  * `"live_vendor_call_claim":"NONE"`  
    sha256: `0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9`  
* Path: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
  * `size_bytes: 6538`  
  * `produced_at_utc: 2026-06-18T02:44:04Z`  
    sha256: `0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9`  
* Path: `audit/qa/hde-epic034/pr-03/response_mapping_check.log`  
  Type: LF-terminated check log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `[closed_rails_generation] status=PASS`  
  * `[response_type_preservation] status=PASS`  
  * `[internal_target_posture_or_schema_gap_recorded] status=PASS`  
  * `status=PASS`  
    sha256: `d32f4b937d7c0b20aa3002dcad3d051500069893d2dd5d42cdbf0987347808c3`  
* Path: `audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: audit/qa/hde-epic034/pr-03/response_mapping_check.log`  
  * `size_bytes: 899`  
  * `sha256: d32f4b937d7c0b20aa3002dcad3d051500069893d2dd5d42cdbf0987347808c3`  
    sha256: `d32f4b937d7c0b20aa3002dcad3d051500069893d2dd5d42cdbf0987347808c3`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
  Type: Current-epic doc-delta draft/staging surface  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr03.doc_deltas"`  
  * `"record_type":"epic034_pr03_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f`  
* Path: `audit/qa/hde-epic034/00_meta/doc_deltas.md`  
  Type: Current-epic QA meta doc-delta capture  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr03.qa_meta_doc_deltas"`  
  * `"record_type":"epic034_pr03_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `47c757679fad235079bc9e2e6eb20128cc0f554f3a628f43f8caa5b874acc52f`  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.human_index"`  
  * `"discovered_physical_path":"docs/evidence/INDEX.json"`  
    sha256: `c7833d2378df7179b8105f036c0d44326acd68857bffe66bfbe0c0c4bb5d9015`  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Evidence Mirror  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.machine_mirror"`  
  * `"discovered_physical_path":"artifacts/evidence_index.jsonl"`  
  * `"role":"self_record"`  
    sha256: `9d74c1eddc8ba5f0a2262860f172589dc9aa63b43e69038dfcdf8a981509bfe0`

C) Test/CI proof

* Job or test name: `python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing  
* Job or test name: `git diff --check`  
  Pass indicator copied verbatim: `✅ git diff --check`  
  Where it appears in PR Artifacts: PR Artifacts → Actions taken → Testing

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

PF09 Impact Summary

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.3  
   Current status if evidenced: Task status: Not done; Subtask status: Not done  
   Status action: change to Done  
   Evidence pointer(s): PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
   Linked Findings item(s): F-006; F-009; F-013; F-015; F-018; F-020; F-022; F-024; F-025; F-026  
   Linked CHG item(s), if any: CHG-006

Doc Delta Detection Workflow

CHG-001  
Change claim type: behavior or output  
Change claim: PR-03 implements proof-level v2 `StandardResponse` response-envelope mapping into HDE internal input semantics.  
Evidence pointer: PR Artifacts → Diff → `+"response_envelope_mapping_scope":"HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only"`  
Canon basis: CANON ALIGNED

CHG-002  
Change claim type: behavior or output  
Change claim: PR-03 records schema-gap posture and does not claim compatibility by inference.  
Evidence pointer: PR Artifacts → Diff → `+"schema_gap_status":"GAP_RECORDED"`  
Canon basis: CANON ALIGNED

CHG-003  
Change claim type: behavior or output  
Change claim: PR-03 preserves response type, success status, `errorCode`, data payload identity posture, and route variant.  
Evidence pointer: PR Artifacts → Diff → `+[response_type_preservation] status=PASS`  
Canon basis: CANON ALIGNED

CHG-004  
Change claim type: governed paths or artifact families  
Change claim: PR-03 adds and indexes governed response-mapping snapshot and check-log evidence under `artifacts/` and `audit/`.  
Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG-005  
Change claim type: tokens, rails, or evidence posture  
Change claim: PR-03 preserves no live vendor call, no open-rails smoke, no public Reader change, no AI transformation, and no normalized-data-path proof posture.  
Evidence pointer: PR Artifacts → Diff → `+[no_normalized_data_path_proof_claimed] status=PASS`  
Canon basis: CANON ALIGNED

CHG-006  
Change claim type: PF09 status-impact requirement  
Change claim: PR-03 evidence supports changing PF09.5 HDE-FERM007.3 from Not done to Done, while leaving parent HDE-FERM007 unchanged.  
Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
Canon basis: CANON ALIGNED

CHG: CHG-006

Doc: PF09.5 — HDE Build Checklist Fermentation

Section: §Subtask HDE-FERM007.3 \- Normalize v2 response envelopes into HDE BodyGraph and chart inputs

Canon basis: CANON ALIGNED

Impacted PF09 task ID(s): HDE-FERM007

Impacted PF09 subtask ID(s): HDE-FERM007.3

PF09 status action: change to Done

Delta: Update HDE-FERM007.3 subtask status from Not done to Done, and preserve parent HDE-FERM007 as Not done until later HDE-FERM007 subtasks are reviewed.

Why: PR Artifacts provide response-envelope mapping implementation evidence, canonical response-mapping snapshot, response-mapping check log, schema-gap posture, no-compatibility-by-inference proof, governed index/mirror updates, path proofs, targeted tests, and final validation for the exact HDE-FERM007.3 slice.

Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.response_mapping","discovered_physical_path":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-03 canonical response-envelope mapping snapshot for HDE-FERM007.3 with schema-gap posture and no live vendor conformance claim","produced_at_utc":"2026-06-18T02:44:04Z","proof_anchor":"artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt","record_type":"epic034_pr03_response_mapping","role":"snapshot","schema_version":"1.0","sha256":"0ff5ca1d2f16ed6c365c9f517566cef8a59e82cb8e92813b8c828d2a3efd03f9","size_bytes":6538,"tokens":["JSON_CANONICAL_CHECK_OK","EVIDENCE_PATH_PROOFS_OK"]}`

Canon proof excerpt:  
"Task ID: HDE-FERM007"  
"Task status: Not done"  
"Map the v2 response envelope into the HDE internal data model used by BodyGraph cache, compatibility, sampler, and admin surfaces. The mapping must preserve response type, success status, errorCode, data payload identity, and route variant. It must avoid logging payload bodies or secrets and must keep public Reader output numeric-free."  
"Subtask status: Not done"

Commit Message

Accept EPIC034 PR-03 response-envelope mapping proof

Commit Description

* Implements HDE-EPIC034 PR-03 response-envelope mapping proof generation for v2 `StandardResponse` semantics.  
* Adds canonical `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and PR-scoped `audit/qa/hde-epic034/pr-03/response_mapping_check.log` with sibling path proofs.  
* Preserves response type, success status, `errorCode`, data payload identity posture, and route variant while recording schema-gap posture for existing BodyGraph/cache/compatibility targets.  
* Keeps closed rails and explicit non-claims for live vendor conformance, open-rails smoke, public Reader changes, HDE-FERM008.4 normalized data path proof, vendor payload bodies, secrets, and AI transformation.  
* Updates governed human Evidence Index, machine Evidence Mirror, hash sentinels, path proofs, and current EPIC034 doc-delta evidence rows.  
* Adds regression tests for canonical response mapping, route-specific schema drift, missing `StandardResponse` fields, stale public-doc refresh cleanup, missing internal inspection loci, stale PR-03 index row cleanup, and approved token coverage.  
* RCA covered doc-delta misbinding, route-specific schema drift, stale public-doc refresh outputs, hard-coded envelope field posture, hard-coded internal-locus inspection, and stale PR-03 index rows.  
* Final validation passed generator refresh, evidence index update/check, targeted pytest, orientation update/check, evidence path validation, mirror schema, evidence-index hash, LF checks, and `git diff --check`.  
* Impacted PF09 item: HDE-FERM007 / HDE-FERM007.3; review supports change to Done for HDE-FERM007.3 only, with no parent HDE-FERM007 status change.

DECISION: PR ACCEPTABLE

Paste this into the PF10 Addendum Index:

2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation

Paste this under `# 2) Numbered Addenda`:

---

## **2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation**

Timestamp: 061826 18:55

Details: HDE-EPIC034 PR-04 attempted to complete HDE-FERM007.4 by proving adapter and presenter boundary preservation for the HumanDesignAPI v2 vendor seam.

The approved PR-04 intent was a structural boundary proof, not a runtime v2 conformance claim. The proof target was that the HumanDesignAPI v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, does not bypass the presenter boundary, does not introduce ad-hoc serialization, and does not authorize external I/O inside pure compute modules.

PR-04 failed as a proof model. The failure is not currently evidenced as a live vendor runtime failure. It is evidenced as a validation/proof failure cluster: the boundary proof could report PASS while missing adapter bypasses, presenter bypasses, public route drift, ad-hoc serialization, pure-compute external I/O, stale evidence rows, and vendor guard weaknesses.

### **Observed failure**

The PR-04 failure loop produced repeated false-PASS risks. The failed proof mechanism could miss at least the following classes while still reporting success:

* adapter bypass  
* presenter bypass  
* public route drift  
* ad-hoc serialization  
* pure-compute external I/O  
* stale evidence rows  
* vendor guard weaknesses

The latest visible failure class was a fail-open public-route drift check: newly discovered public routes could be reduced to an empty comparison set exactly when route drift needed to be detected.

### **Root cause**

The primary root cause is that PR-04 used an open-ended blacklist-style static analysis posture rather than a conservative positive boundary contract.

The proof attempted to prove absence of arbitrary Python and Flask behavior by accumulating specific forbidden syntax patterns. That approach is not stable enough for PR-04 acceptance because every new route-registration form, response-producing form, HTTP-client form, aliasing pattern, helper chain, serializer form, or guard shape can create another missed case.

Secondary root causes:

* presenter-boundary proof drifted into partial Flask/Python route semantics instead of a stable architecture-level invariant  
* the evidence generator became responsible for too many concerns: source inventory, contract mapping, request shaping, response mapping, artifact rendering, path proofs, and architecture-boundary analysis  
* tests became one-bug/one-fixture regression checks rather than a table-driven invariant suite  
* route-drift detection remained incomplete and could disable itself when inspected adapter loci differed from a hard-coded baseline  
* vendor guard proof could conflate “guard symbols exist somewhere” with proof that each external-I/O path is guarded

### **Escalation decision**

The PR-04 escalation to Lead Dev identified that the failed PR evidence supports a proof/acceptance failure more strongly than a live runtime failure.

Isis prepared a remediation plan for Thoth approval. The recommended remediation path is a combined approach:

1. replace the permissive blacklist proof with a conservative positive boundary contract  
2. split boundary analysis from evidence rendering  
3. replace one-off bug fixtures with a table-driven boundary taxonomy and invariant suite  
4. repair the active public-route drift false-PASS hole as part of the positive boundary model  
5. revalidate PR-04 against HDE-FERM007.4 only after the proof model is corrected

### **Live rule for HDE-EPIC034 PR-04 remediation**

Until drained into the owning PF homes, PR-04 remediation MUST use a conservative fail-closed boundary-proof posture.

A remediated PR-04 proof MUST fail closed on unknown current boundary categories. Unknown public route, response-producing path, serializer path, external-I/O path, guard provenance, presenter provenance, adapter route registration, or evidence-binding posture MUST NOT be silently treated as PASS.

A remediated PR-04 proof MUST distinguish these categories explicitly:

* allowed  
* forbidden  
* unknown / fail-closed  
* out of scope

The proof MUST be based on discovered current repo surfaces and must report the actual adapter, presenter, engine, vendor-seam, and evidence-tool loci it inspected. It MUST NOT assume these loci from earlier planning text or from hard-coded expected path lists without verification.

### **Analyzer and renderer separation**

Boundary analysis MUST be separated from evidence rendering.

The analyzer should return explicit findings, unknowns, public route deltas, responder provenance, serializer findings, external-I/O findings, guard provenance, evidence-family bindings, and verdict status.

The evidence generator should render analyzer output into governed evidence artifacts, path proofs, and evidence-index rows. It should not independently decide architecture-boundary truth.

### **Boundary taxonomy requirement**

PR-04 remediation MUST replace one-off bug fixtures with a table-driven taxonomy and invariant suite covering at least:

* route registration surfaces  
* public route signatures  
* response-producing paths  
* presenter-valid paths  
* presenter-bypass paths  
* serializer families  
* external-I/O families  
* import and alias forms  
* cross-file helper chains  
* vendor guard provenance  
* pure-compute forbidden operations  
* public/internal route classification  
* evidence-family binding for PR-01 through PR-04

The taxonomy should make missing categories visible. It does not by itself prove all possible Python behavior; it must be paired with the fail-closed analyzer posture.

### **Scope boundary**

This addendum does not expand PR-04 scope.

PR-04 remediation remains HDE-FERM007.4 only.

PR-04 remediation MUST NOT claim:

* HDE-FERM007.5  
* HDE-FERM008  
* runtime v2 conformance  
* live vendor conformance  
* open-rails smoke  
* public Reader change  
* public transport behavior change  
* new public route  
* new public flag  
* new public payload  
* new HTTP home  
* AI runtime scope  
* AI evidence scope

HDE-FERM007.4 may move to Done only after a remediated proof demonstrates the corrected conservative boundary model, produces current governed evidence, and passes the relevant validation checks.

### **Drain targets**

Drain the durable rule to the owning PF homes after Thoth approval and successful remediation:

* HDE Architecture — owns adapter, presenter, engine, and boundary architecture rules  
* HDE Mechanics Guide — owns the boundary-proof mechanics, analyzer/renderer split, and required evidence mechanics  
* HDE Schemas and Artifacts — owns governed evidence/index/mirror/path-proof posture  
* HDE Build Checklist Fermentation — owns HDE-FERM007.4 status posture and any checklist language needed after remediation  
* Glow QA Guide — owns review posture for proof-model failure versus live-runtime failure, if a general QA rule is needed

Source basis: PF10’s current template/index ends at addendum 2.11 and defines the addendum format. The approved plan defines PR-04’s required boundary proof outputs, success/failure posture, and HDE-FERM007.4 scope. The PR-04 remediation material records the false-PASS loop, the root proof-model failure, and Isis’s recommended combined remediation path.

## **2.13) ADR — HD Engine Owns Vendor Acquisition, BodyGraph Persistence, Retrieval, and Compute for Future Glow App Integration**

Timestamp: 061626

Status: Proposed for PF10 live adoption

Decision owner: Thoth / PO

Scope: Future Glow app integration with HD Engine

### **Decision**

When the Glow app is integrated with the HD Engine, the HD Engine will remain responsible for:

* the initial HumanDesignAPI vendor call;  
* request shaping and auth/header handling for vendor calls;  
* receiving and normalizing vendor BodyGraph/chart response data;  
* storing BodyGraph data in the database;  
* retrieving stored BodyGraph data from the database;  
* running HD Engine computation against stored or freshly acquired BodyGraph data;  
* maintaining governed evidence and proof posture for vendor acquisition and BodyGraph persistence behavior.

The Glow app will not become the owner of the HumanDesignAPI vendor-call process.

The Glow app will not independently reimplement vendor request shaping, vendor auth/header handling, BodyGraph normalization, or BodyGraph persistence logic.

The Glow app is expected to function as the application shell, UX/product layer, dating/matching interface, account/session/product orchestration layer, and consumer of HD Engine outputs.

### **Change from prior architectural assumption**

This ADR supersedes the prior integration assumption that the Glow app would perform the initial vendor call and pass BodyGraph data into the HD Engine for processing only.

The new decision is:

The HD Engine owns both acquisition and processing.

That means the HD Engine owns the complete BodyGraph lifecycle from vendor call through storage, retrieval, and computation.

### **Rationale**

The HD Engine has already invested substantial design and hardening effort into the vendor-call path, including:

* HumanDesignAPI v1/v2 contract inventory;  
* vendor route-family distinction;  
* environment-variable and credential posture;  
* v1/v2 auth-header posture;  
* closed-rails and open-rails policy;  
* OPS discovery and open-rails testing policy;  
* request-shaping planning;  
* response-mapping planning;  
* adapter/presenter boundary proof;  
* DB bridge and persistence posture;  
* evidence-index and Machine Mirror discipline;  
* no-secret and governed-evidence posture.

Repeating this work inside the Glow app would create duplicated logic, duplicated risk, duplicated credential handling, duplicated evidence burden, and likely drift between the app and the engine.

The safer architecture is to keep vendor integration and HD computation in one hardened component: the HD Engine.

### **Architectural boundary**

The Glow app may request or trigger HD Engine behavior, but the HD Engine owns the vendor and compute boundary.

The Glow app may provide user/product context needed to initiate a chart acquisition flow, but it should not directly call HumanDesignAPI unless a future ADR explicitly creates a narrow exception.

The HD Engine should expose a controlled integration surface to the Glow app for operations such as:

* request chart acquisition;  
* check acquisition status;  
* retrieve computed HD profile outputs;  
* retrieve stored BodyGraph-derived results;  
* trigger recomputation where authorized;  
* surface errors or retry state in an app-safe form.

The exact endpoint, queue, service, or SDK shape is not decided by this ADR.

### **Security and secret posture**

HumanDesignAPI credentials should remain owned by the HD Engine infrastructure boundary.

The Glow app should not need direct access to:

* `HD_API_KEY`;  
* `GEO_API_KEY`;  
* raw HumanDesignAPI auth headers;  
* raw vendor request payloads;  
* raw vendor response payloads unless a future data contract explicitly authorizes that exposure.

The Glow app may receive normalized, app-safe outputs from the HD Engine.

The HD Engine must preserve secret-safe logging, redaction, and evidence posture.

### **Data ownership posture**

The HD Engine is the owner of BodyGraph acquisition and BodyGraph persistence mechanics.

The database remains the persistence layer for stored BodyGraph data and related HD Engine runtime state.

Future integration work must distinguish:

* user/app identity owned by Glow app;  
* vendor acquisition owned by HD Engine;  
* BodyGraph persistence owned by HD Engine;  
* HD computation owned by HD Engine;  
* app presentation, matching, onboarding, and user experience owned by Glow app.

### **Vendor-call ownership rule**

All HumanDesignAPI vendor calls should route through the HD Engine unless a future PF10 addendum or permanent PF canon explicitly approves an exception.

The Glow app must not introduce a parallel HumanDesignAPI client, parallel credential path, parallel vendor request-shaping layer, or parallel BodyGraph normalization layer without a new ADR.

### **Persistence and retrieval rule**

The HD Engine is responsible for storing the acquired BodyGraph data and retrieving it later for computation.

The Glow app may request stored results or computed outputs, but it should not become the canonical storage owner for raw vendor BodyGraph data unless future architecture explicitly changes this decision.

### **Evidence and QA posture**

Future implementation and QA planning must prove that:

* the Glow app does not bypass the HD Engine for HumanDesignAPI vendor calls;  
* vendor credentials remain under the HD Engine infrastructure boundary;  
* BodyGraph storage and retrieval remain governed by the HD Engine persistence path;  
* HD computation continues to run in the HD Engine;  
* public/app-facing surfaces receive normalized, app-safe outputs rather than raw ungoverned vendor data;  
* no new public route, app endpoint, or integration surface expands access to raw vendor secrets or ungoverned BodyGraph payloads without explicit scope and proof.

### **Impact on HDE-EPIC034 and later Fermentation work**

This ADR supports the current HDE-EPIC034 direction by making adapter/presenter boundary proof more important, not less important.

If the HD Engine owns future vendor acquisition for the Glow app, then HDE-EPIC034 must continue to protect:

* no new uncontrolled HTTP home;  
* no adapter bypass;  
* no presenter boundary bypass;  
* no ad-hoc serialization;  
* no pure-compute external I/O;  
* no vendor credential leakage;  
* no public Reader or app-facing contract drift.

Future HDE-FERM007 and HDE-FERM008 work should treat the HD Engine vendor seam as the durable integration point for the Glow app.

### **Impact on future Glow app architecture**

Future Glow app architecture should assume:

* the Glow app is not the HumanDesignAPI vendor client;  
* the Glow app is not the canonical BodyGraph normalization layer;  
* the Glow app is not the owner of raw vendor credential handling;  
* the Glow app is not the owner of HD computation;  
* the Glow app consumes HD Engine outputs through a controlled integration contract.

The Glow app can still own:

* onboarding UX;  
* user consent and product flow;  
* dating/matching experience;  
* account and profile UX;  
* display orchestration;  
* app-specific caching of app-safe outputs, if later approved;  
* user-facing error presentation;  
* app analytics or matching workflows, if later scoped.

### **Non-goals**

This ADR does not decide:

* the final Glow app to HD Engine integration transport;  
* whether integration uses HTTP, internal service call, queue, SDK, or another mechanism;  
* the final app-facing API contract;  
* user-account identity mapping;  
* matching algorithm scope;  
* app-side caching policy;  
* production deployment topology;  
* public pricing or product UX;  
* final open-rails QA procedure;  
* final HDE-FERM008 live conformance closure.

Those remain future architecture and implementation decisions.

### **Invalid future assumptions**

Future plans must not assume:

* the Glow app will call HumanDesignAPI directly;  
* the Glow app will store raw BodyGraph vendor data as the canonical owner;  
* the HD Engine only processes data supplied by the app;  
* vendor hardening work should be duplicated in the app;  
* HumanDesignAPI credentials belong in the app layer;  
* app integration requires bypassing the HD Engine vendor seam.

### **Required planning posture**

Future Epic Plans, Implementation Plans, QA Plans, and remediation plans involving Glow app integration must preserve this decision unless explicitly superseded.

Any plan proposing direct Glow app vendor calls must include a new ADR explaining why the HD Engine ownership model is being changed.

Any plan proposing raw BodyGraph persistence outside the HD Engine must include a new ADR explaining the ownership, security, evidence, and data-contract implications.

### **Drain targets**

#### **PF02 — HDE Architecture**

Drain this ADR into architecture ownership boundaries.

Required drain content:

* HD Engine owns HumanDesignAPI vendor acquisition.  
* HD Engine owns BodyGraph storage and retrieval.  
* HD Engine owns HD computation.  
* Glow app is a product/app shell and consumer of HD Engine outputs.  
* Direct Glow app vendor calls require a future ADR.

#### **PF05 — HDE CLI-API-Vendor Ref**

Drain this ADR into vendor-call ownership and request-shaping posture.

Required drain content:

* HumanDesignAPI request shaping belongs to HD Engine.  
* Glow app must not duplicate vendor-client behavior.  
* v1/v2 auth-header and base-url posture remain HD Engine vendor responsibilities.  
* App integration should call HD Engine integration surfaces, not HumanDesignAPI directly.

#### **PF07 — Glow Infrastructure**

Drain this ADR into secret/config ownership.

Required drain content:

* `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` belong to the HD Engine infrastructure boundary.  
* Glow app should not require direct vendor API credentials.  
* Any future cross-service invocation must preserve secret isolation.

#### **PF12 — HDE Schemas and Artifacts**

Drain this ADR into artifact/data ownership.

Required drain content:

* BodyGraph acquisition and persistence evidence belongs to HD Engine evidence families.  
* Raw vendor BodyGraph data ownership must remain HD Engine unless future canon changes it.  
* App-facing outputs should be normalized and governed.

#### **PF14 — HDE Mechanics Guide**

Drain this ADR into mechanics ownership.

Required drain content:

* Vendor acquisition, BodyGraph persistence, BodyGraph retrieval, and computation remain HD Engine mechanics.  
* Glow app integration consumes HD Engine outputs.  
* Do not duplicate vendor normalization mechanics in the app layer.

#### **PF19 — Glow QA Guide**

Drain this ADR into QA proof posture for app integration.

Required drain content:

* QA for Glow app integration must prove the app does not bypass the HD Engine for vendor calls.  
* QA must preserve secret boundary, app/engine contract boundary, and raw vendor-data boundary.  
* App integration QA must not treat app-side UI success as proof of HD Engine vendor acquisition unless HD Engine evidence supports it.

#### **PF27 — Canon Plan Templates**

Drain this ADR into future integration-plan templates.

Required drain content:

* Plans involving Glow app integration must state vendor-call ownership.  
* Plans must distinguish app shell responsibilities from HD Engine acquisition/compute responsibilities.  
* Plans proposing direct app vendor calls require ADR justification.

#### **PF09.5 — HDE Build Checklist Fermentation**

Drain this ADR where relevant to HDE-FERM007 and HDE-FERM008.

Required drain content:

* HumanDesignAPI v2 adapter architecture work supports HD Engine-owned vendor acquisition for later Glow app integration.  
* Live conformance and open-rails vendor proof should assume HD Engine ownership of vendor calls unless explicitly superseded.

### **Decision summary**

The HD Engine is the canonical owner of HumanDesignAPI vendor acquisition, BodyGraph persistence, BodyGraph retrieval, and HD computation.

The Glow app is the product shell and consumer of HD Engine outputs.

This is the preferred architecture because it preserves the hardened vendor-call path and avoids duplicating high-risk vendor, credential, evidence, and compute logic in the app layer.

## 2.14) W-001 Remediation PR-04 HDE-EPIC034

Review Summary

* The PR implements W-001 for HDE-EPIC034 PR-04 remediation: a conservative positive boundary contract with explicit `allowed`, `forbidden`, `unknown / fail-closed`, and `out of scope` classifications.  
* The PR aligns with the Approved Plan’s W-001 scope: it targets HDE-FERM007.4 boundary proof remediation and does not claim HDE-FERM007.5, HDE-FERM008, runtime v2 conformance, live vendor conformance, open-rails smoke, public Reader changes, new public routes, or AI scope.  
* The PR updates the adapter/presenter boundary proof so it reports discovered adapter, presenter, engine, vendor-seam, and evidence-tool loci before classification, and it records unknown current categories as fail-closed rather than PASS-capable.  
* The PR includes multiple bug-fix rounds addressing guard provenance, route drift, closed-rails vendor gating, per-route presenter provenance, aliasing, after-request mutation, empty-response handling, helper pass-through handling, installed hook discovery, and route-scope filtering.  
* Tests and evidence posture are sufficient for W-001: final artifacts record targeted pytest plus generator, evidence-index, orientation, evidence-path, mirror-schema, hash, LF, and `git diff --check` validation as passed.  
* Diff review covers all 100 diff hunks across 80 file patches by grouping related evidence, code, test, and generated-proof hunks.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.4.  
* Status recommendation: No status change recommended. W-001 is an accepted remediation slice, but the Approved Plan reserves HDE-FERM007.4 Done posture for successful remediation and validation of the broader PR-04 proof obligation.  
* RCA is included because PR Artifacts explicitly record repeated bug/fix rounds and stabilization work.

Diff Review

1. DR-001  
    Change summary: Updates the Machine Evidence Mirror rows, including PR-04 boundary proof, boundary check, doc-delta, and self-record rows.  
    Risk assessment: Medium  
    Why it matters: W-001 acceptance depends on governed evidence rows accurately reflecting the remediated boundary proof and not carrying stale PR-04 posture.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -62,51 +62,51 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -123,91 +123,91 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -235,105 +235,105 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -342,30 +342,30 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
2. DR-002  
    Change summary: Updates Machine Evidence Mirror path-proof and checksum sidecars.  
    Risk assessment: Low  
    Why it matters: Mirror byte changes require matching path-proof and hash sidecars.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,6 +1,6 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
3. DR-003  
    Change summary: Refreshes narrative router parity path proofs.  
    Risk assessment: Medium  
    Why it matters: These are historical proof refreshes outside W-001’s core behavior, so final validation must confirm evidence-path coherence.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
4. DR-004  
    Change summary: Replaces the PR-04 adapter-boundary proof log with W-001 conservative-boundary evidence and updates its path proof.  
    Risk assessment: Low  
    Why it matters: This is the primary proof artifact for the W-001 remediation.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,33 +1,67 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
5. DR-005  
    Change summary: Refreshes HDAPI v2 contract-map, endpoint-reference, anomaly, and OpenAPI validation artifacts and path proofs.  
    Risk assessment: Medium  
    Why it matters: PR-04 boundary proof depends on the governed HDAPI evidence family remaining coherent while boundary evidence is regenerated.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt b/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt b/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md b/artifacts/vendor/hdapi_v2/known_anomalies.md`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,15 +1,15 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt b/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log b/artifacts/vendor/hdapi_v2/openapi_validation.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,26 +1,26 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt b/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
6. DR-006  
    Change summary: Refreshes accepted source-selection, request-shaping, response-mapping, source-inventory, and v1 legacy dependency artifacts and path proofs.  
    Risk assessment: Medium  
    Why it matters: W-001 must reuse prior accepted evidence families rather than reimplementing them; refreshed dependency artifacts must remain bound and validated.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json b/artifacts/vendor/hdapi_v2/source_inventory.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md b/artifacts/vendor/hdapi_v2/source_inventory.md`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,28 +1,28 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
7. DR-007  
    Change summary: Refreshes writer, doc-delta, narrative-gate, and topology path proofs.  
    Risk assessment: Medium  
    Why it matters: These are proof refreshes outside the W-001 code path; final evidence-path and mirror checks must cover them.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
8. DR-008  
    Change summary: Refreshes EPIC030 historical QA path proofs.  
    Risk assessment: Medium  
    Why it matters: Historical proof refreshes are acceptable only when governed path and mirror validation remain green.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
9. DR-009  
    Change summary: Refreshes EPIC031 log/posture evidence artifacts and path proofs.  
    Risk assessment: Medium  
    Why it matters: These rows are outside W-001 but show global evidence refresh side effects that must be covered by validation.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/bounded_label_observability.json b/audit/qa/hde-epic031/pr-02/bounded_label_observability.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/bounded_label_observability.json.path_proof.txt b/audit/qa/hde-epic031/pr-02/bounded_label_observability.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json b/audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json.path_proof.txt b/audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/secret_redaction_scan.log b/audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,9 +1,9 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/secret_redaction_scan.log.path_proof.txt b/audit/qa/hde-epic031/pr-02/secret_redaction_scan.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl b/audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,6 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl.path_proof.txt b/audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt b/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,19 +1,20 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt.path_proof.txt b/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-001  
10. DR-010  
     Change summary: Refreshes EPIC033 and EPIC034 metadata and prior PR-01/PR-02/PR-03 check logs and path proofs.  
     Risk assessment: Medium  
     Why it matters: W-001 must preserve prior accepted evidence families while rebinding PR-04 proof evidence.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log b/audit/qa/hde-epic033/acceptance_map_viability.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,8 +1,8 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt b/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt b/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log b/audit/qa/hde-epic034/pr-01/source_selection_check.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,19 +1,19 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log b/audit/qa/hde-epic034/pr-02/request_shaping_check.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log b/audit/qa/hde-epic034/pr-03/response_mapping_check.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,19 +1,19 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
11. DR-011  
     Change summary: Updates the PR-04 boundary check log and path proof for the W-001 conservative boundary contract.  
     Risk assessment: Low  
     Why it matters: This is the primary PR-scoped QA evidence surface for W-001.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log b/audit/qa/hde-epic034/pr-04/boundary_check.log`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,18 +1,37 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
12. DR-012  
     Change summary: Refreshes EPIC033 acceptance-map proof surfaces and HDE evidence index/hash sidecars.  
     Risk assessment: Medium  
     Why it matters: These artifacts participate in governed evidence posture after PR-04 evidence regeneration.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/acceptance_map_epic033.json b/docs/acceptance_map_epic033.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/acceptance_map_epic033.json.path_proof.txt b/docs/acceptance_map_epic033.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1 +1 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,5 +1,5 @@`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
13. DR-013  
     Change summary: Hardens `engine/bodygraph/vendor_client.py` closed-rails refusal and retry-log classification.  
     Risk assessment: High  
     Why it matters: The sanctioned vendor seam must refuse unless open rails are explicit and must log refusals with bounded error classification.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/engine/bodygraph/vendor_client.py b/engine/bodygraph/vendor_client.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -59,65 +59,72 @@ PINNED_BACKOFF_PROFILES = frozenset(`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -261,51 +268,51 @@ class HdApiClient:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -428,152 +435,163 @@ class HdApiClient:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -631,36 +649,40 @@ class HdApiClient:`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
14. DR-014  
     Change summary: Adds vendor-client tests for explicit open-rails gating and refusal classification.  
     Risk assessment: Low  
     Why it matters: The W-001 boundary proof relies on the low-level vendor helper being directly guarded, not merely guarded by upstream entrypoints.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tests/bodygraph/test_vendor_client.py b/tests/bodygraph/test_vendor_client.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -100,90 +100,149 @@ def test_fetch_does_not_retry_other_4xx_statuses() -> None:`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
15. DR-015  
     Change summary: Expands evidence tests for W-001 conservative classifications, route drift, presenter provenance, guard provenance, aliasing, hooks, helpers, and fail-closed behavior.  
     Risk assessment: Low  
     Why it matters: These tests directly target the false-PASS bug classes identified in the remediation plan.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -184,52 +184,50 @@ def test_generator_refresh_requires_explicit_open_rails(monkeypatch: pytest.Monk`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -801,51 +799,50 @@ def test_epic034_boundary_check_log_exists_and_binds_prior_families() -> None:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1975,50 +1972,51 @@ app.add_url_rule('/bad', view_func=Bad.as_view('bad'))`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -2066,135 +2064,204 @@ def test_epic034_presenter_bypass_keeps_methodview_methods_qualified(monkeypatch`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -2248,25 +2315,912 @@ def test_epic034_presenter_bypass_detects_imported_adapter_helper(monkeypatch: p`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
16. DR-016  
     Change summary: Updates EPIC031 log-posture generator for closed-rails/vendor refusal posture.  
     Risk assessment: Medium  
     Why it matters: This touches vendor/logging posture adjacent to the W-001 low-level vendor guard changes.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tools/evidence/generate_epic031_pr02_log_posture.py b/tools/evidence/generate_epic031_pr02_log_posture.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -19,51 +19,51 @@ from tools.evidence import update_evidence_index # noqa: E402`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -109,71 +109,72 @@ def _client(log_path: Path, request: Callable[[urlrequest.Request, float], tuple`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
17. DR-017  
     Change summary: Updates `generate_hdapi_v2_contract_inventory.py` for W-001 boundary evidence rendering, path-proof handling, vendor guard checks, and unsupported-scope posture.  
     Risk assessment: Medium  
     Why it matters: This generator renders the W-001 proof outputs and must not convert analyzer failures or unknowns into PASS.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -96,90 +96,79 @@ SOURCES = [`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1333,51 +1322,51 @@ def _adapter_external_io_calls(loci: tuple[str, ...]) -> list[str]:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1758,54 +1747,56 @@ def _vendor_external_io_functions(loci: tuple[str, ...]) -> list[str]:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1834,175 +1825,356 @@ def _unsupported_scope_claims(*payloads: dict[str, Any]) -> list[str]:`  
     Approved Plan linkage: Approved Plan → Work Item W-001  
18. DR-018  
     Change summary: Updates `hdapi_v2_boundary_analyzer.py` to implement the conservative positive boundary analysis, route discovery, presenter provenance, external-I/O, guard-provenance, and fail-closed logic.  
     Risk assessment: High  
     Why it matters: This is the core implementation of W-001’s proof-model correction.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -1,39 +1,43 @@`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -149,112 +153,112 @@ def _adapter_external_io_calls(loci: tuple[str, ...]) -> list[str]:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -272,156 +276,207 @@ def _route_methods(deco_name: str, deco: ast.AST) -> str:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -537,57 +592,69 @@ def _adapter_presenter_bypass_routes(loci: tuple[str, ...]) -> list[str]:`; PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `@@ -603,50 +670,554 @@ def _adapter_presenter_bypass_routes(loci: tuple[str, ...]) -> list[str]:`  
     Approved Plan linkage: Approved Plan → Work Item W-001

RCA

A) Bug/Failure statement

PR Artifacts show W-001 was a remedial PR for a false-PASS boundary proof loop and then underwent several bug-fix rounds. The initial remediation summary says it implemented the conservative contract, followed by review comments such as “3 bugs found, analyze carefully and fix,” “More bugs found,” “5 bugs found,” and “more bugs,” before the final review result said no new blocking issues were found.

B) Root cause(s)

1. The previous boundary proof treated vendor guard provenance too broadly.  
    Evidence pointer(s): PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `When the only external I/O is in` engine/bodygraph/vendor\_client.py:\_default\_request`, this branch marks it as guarded whenever any guarded entrypoint exists anywhere in the vendor loci, without checking that all call paths into` \_default\_request `go through those guarded entrypoints.`  
2. Route drift could still be disabled by changed adapter loci.  
    Evidence pointer(s): PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `When the adapter locus list is expanded or repointed to cover a new public route file, this condition makes` route\_baseline\_reconciled`true solely because the list differs from`ADAPTER\_BOUNDARY\_CANONICAL\_ADAPTER\_LOCI`, even if` public\_reader\_route\_drift `is non-empty.`  
3. The vendor seam initially did not require both open-rails flags explicitly before network access.  
    Evidence pointer(s): PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `Fresh evidence in this revision: the new low-level guard treats a missing` SAFE\_MODE`as`False`, so a process that sets` ALLOW\_NETWORK=1`but omits`SAFE\_MODE=0`proceeds to`opener.open `even though the repo rails require both open-rails flags before vendor/network access.`  
4. Presenter provenance initially still had per-route and return-path false-PASS gaps.  
    Evidence pointer(s): PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `When one adapter route calls` emit\_public`but another route returns a non-JSON/plain response without going through the presenter, this global`adapter\_presenter\_calls and not presenter\_bypass `check still marks every response-producing path as allowed because the bypass scanner only catches JSON-ish serializers.`  
5. The analyzer initially missed hook, alias, helper, mutation, empty-response, abort/raise, and local-shadowing variants.  
    Evidence pointer(s): PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `When a Flask` after\_request`/`after\_app\_request`hook replaces the response with a raw string or`Response`,` \_adapter\_public\_route\_signatures`records the hook but this new presenter-provenance scanner never adds it to`route\_functions`.`

C) Fix in this PR

* Implemented explicit allowed/forbidden/unknown-fail-closed/out-of-scope classifications and rendered them into PR-04 boundary evidence.  
* Added low-level closed-rails refusal directly to `HdApiClient._default_request`, requiring explicit open rails.  
* Tightened guard provenance to bind relevant vendor external-I/O paths to guarded entrypoints and later to guard dominance.  
* Fixed public-route drift posture so changed adapter loci do not silently disable drift checks.  
* Reworked presenter provenance to per-route and per-return proof, including nested handlers, hooks, helper pass-throughs, aliases, empty responses, response mutations, abort/raise exits, and shadowing cases.  
* Regenerated governed boundary evidence, evidence indices, mirror, hashes, and path proofs under closed rails.

D) Fix verification

* PR Artifacts record final targeted pytest as passed: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
* PR Artifacts record final evidence-index validation as passed: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
* PR Artifacts record final mirror, hash, LF, and diff validation as passed: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
* Residual risk: W-001 is only the first remediation work item. The Approved Plan still lists W-002 analyzer/rendering separation, W-003 taxonomy replacement, W-004 route-drift remediation, and W-005 final PR-04 validation as additional remediation work items.

Findings

1. F-001 (DR-001): The Machine Evidence Mirror now contains W-001/PR-04 boundary-proof and boundary-check rows with updated timestamps, hashes, and path-proof anchors.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T04:10:43Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"83b9e08dffb16218900725381c5bb6010582db6c74a3c216c4664219de496910","size_bytes":10557,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
    Why it matters: This proves the primary W-001 boundary proof is mirrored and path-proofed.  
2. F-002 (DR-002): Machine mirror sidecars were updated after the W-001 proof refresh.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`  
    Why it matters: Sidecars must track the final mirror bytes.  
3. F-003 (DR-003): Historical narrative router path-proof refreshes are present but covered by final validation.  
    Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
    Why it matters: Broad proof churn is not a blocker when path validation passes.  
4. F-004 (DR-004): The boundary proof now states W-001 scope, classification categories, fail-closed unknown posture, and actual discovered loci.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+work_item=W-001`  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+classification_categories_used=allowed,forbidden,unknown / fail-closed,out of scope`  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+unknown_current_categories_fail_closed=true`  
    Why it matters: This directly satisfies the W-001 proof-model correction.  
    PF references only when needed:  
    PF10 — HDE Build Notes, §2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation  
    "A remediated PR-04 proof MUST fail closed on unknown current boundary categories."  
    "A remediated PR-04 proof MUST distinguish these categories explicitly:"  
5. F-005 (DR-005): Contract-support artifact refreshes remain supporting evidence and do not expand W-001 scope.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`  
    Why it matters: W-001 consumes existing HDAPI evidence context but does not re-scope contract inventory work.  
6. F-006 (DR-006): Prior source-selection, request-shaping, response-mapping, source-inventory, and v1 legacy evidence families remain refreshed and bound.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
    Why it matters: W-001 depends on prior PR evidence families and must preserve them.  
7. F-007 (DR-007): Proof refreshes outside W-001 are validation-covered and do not create observed scope drift.  
    Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
    Why it matters: This supports trust in broad path-proof refreshes.  
8. F-008 (DR-008): EPIC030 path-proof churn is historical evidence refresh only.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`  
    Why it matters: It does not alter W-001 behavior and is covered by final validation.  
9. F-009 (DR-009): EPIC031 log-posture evidence refresh is present and adjacent to vendor/logging posture.  
    Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt b/audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`  
    Why it matters: W-001 hardens vendor closed-rails posture and related evidence must remain coherent.  
10. F-010 (DR-010): Prior PR-01, PR-02, and PR-03 check logs remain present as dependency-family evidence.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log b/audit/qa/hde-epic034/pr-03/response_mapping_check.log`  
     Why it matters: W-001 must preserve earlier accepted evidence families.  
11. F-011 (DR-011): The PR-04 boundary check log explicitly proves closed rails, conservative positive contract application, fail-closed unknown posture, discovered loci, route drift, presenter provenance, external I/O, guard provenance, and evidence/path-proof posture.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+[conservative_positive_boundary_contract_applied] status=PASS`  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+[unknown_current_categories_fail_closed] status=PASS`  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+[guard_provenance_checked_per_relevant_path] status=PASS`  
     Why it matters: This is the PR-scoped PASS proof for the W-001 boundary model.  
12. F-012 (DR-012): Human Evidence Index and hash sidecars were updated and validated.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"index.human_index","discovered_physical_path":"docs/evidence/INDEX.json","produced_at_utc":"2026-06-19T04:10:45Z","proof_anchor":"docs/evidence/INDEX.json.path_proof.txt","role":"snapshot","sha256":"f77d18ae5e125c3ecc51f2fecb6fff5afd8eb5806e3c8816a03c14cd872c77f9","size_bytes":74591}`  
     Why it matters: Evidence-index parity and path-proof discipline are part of acceptance evidence.  
13. F-013 (DR-013): The vendor client now refuses unless open rails are explicit and classifies provider refusal.  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `Tightened the sanctioned vendor seam so _default_request refuses unless SAFE_MODE=0 and ALLOW_NETWORK=1 are both explicitly set, including the missing-SAFE_MODE / ALLOW_NETWORK=1 case.`  
     Why it matters: This closes a live-I/O risk inside the sanctioned vendor seam while staying within closed-rails boundary-proof remediation.  
14. F-014 (DR-014): Vendor-client regression tests cover direct low-level closed-rails refusal.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+def test_default_request_refuses_unless_both_open_rails_flags_are_set(monkeypatch: pytest.MonkeyPatch) -> None:`  
     Why it matters: The sanctioned seam must not rely only on upstream guards.  
15. F-015 (DR-015): Evidence tests cover the fail-closed boundary categories and the previously observed false-PASS cases.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+def test_epic034_adapter_boundary_reports_positive_contract_classifications() -> None:`  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+def test_epic034_boundary_unknown_category_is_fail_closed() -> None:`  
     Why it matters: The PR adds direct regression proof for W-001’s central acceptance posture.  
16. F-016 (DR-016): EPIC031 log-posture generator changes are adjacent but not scope-expanding.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tools/evidence/generate_epic031_pr02_log_posture.py b/tools/evidence/generate_epic031_pr02_log_posture.py`  
     Why it matters: They relate to vendor/logging proof refresh and are covered by final tests.  
17. F-017 (DR-017): The HDAPI evidence generator now renders explicit boundary findings and verdicts rather than a permissive PASS-only posture.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+def _boundary_finding(category: str, classification: str, verdict: str, inspected: list[str], reason: str, details: list[str] | None = None) -> dict[str, Any]:`  
     Why it matters: Rendering explicit findings is necessary so failures and unknowns cannot be hidden.  
18. F-018 (DR-018): The boundary analyzer received the core conservative proof-model changes.  
     Evidence pointer: PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`  
     Why it matters: This file is the core W-001 analyzer implementation.  
19. F-019: Final validation evidence is complete and current after the last bug-fix round.  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ git diff --check`  
     Why it matters: The final state is tested after repeated remediation.  
20. F-020: PR Artifacts include a final code-review statement with no new blocking issues.  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `Review Result`  
     Evidence pointer: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `I reviewed the latest commit (f98275b) and found no new blocking issues in the changed W-001 / HDE-FERM007.4 boundary-proof logic.`  
     Why it matters: This is not accepted as a substitute for this review, but it supports that Codex’s final pass did not identify further blockers.

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
    PF09 subtask ID(s): HDE-FERM007.4  
    Current PF09 status: Task status: Not done; Subtask status: Not done  
    Status recommendation: No status change recommended  
    Why this status posture is supported: W-001 implements and proves the first remediation slice: conservative positive boundary contract and fail-closed unknown-category posture. The Approved Plan still lists W-002, W-003, W-004, and W-005 as additional remediation work/validation before HDE-FERM007.4 can safely move to Done.  
    Evidence pointer(s): Approved Plan → Work Item W-001 → `* Intent: Replace the current PR-04 proof model with a conservative positive boundary contract that fails closed on unknown route, responder, serializer, external-I/O, guard, or public-surface categories.`  
    Evidence pointer(s): Approved Plan → Work Item W-005 → `* Dependencies: W-001 through W-004 complete.`  
    Evidence pointer(s): PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+[unknown_current_categories_fail_closed] status=PASS`  
    PF proof excerpt(s) when PF09 is relied on:  
    PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
    "Task ID: HDE-FERM007"  
    "Task status: Not done"  
    PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.4 \- Preserve adapter and presenter boundaries  
    "Ensure the v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, and does not introduce ad-hoc serialization. Adapter remains the HTTP home; presenter remains the byte-authoritative emitter; deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam."  
    "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T04:10:43Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"83b9e08dffb16218900725381c5bb6010582db6c74a3c216c4664219de496910","size_bytes":10557,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"epic034.pr04.boundary_check","discovered_physical_path":"audit/qa/hde-epic034/pr-04/boundary_check.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 boundary check log for adapter HTTP home, presenter boundary, serializer, pure-compute, and prior-family binding posture","produced_at_utc":"2026-06-19T04:10:43Z","proof_anchor":"audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"5fc914e14ed527d76e2e3f7f0cd46bac89926d14c23967cd871419098769c85b","size_bytes":1907,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"epic034.pr04.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 current-epic doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof","produced_at_utc":"2026-06-19T04:10:45Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr04_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d","size_bytes":2003,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"epic034.pr04.qa_meta_doc_deltas","discovered_physical_path":"audit/qa/hde-epic034/00_meta/doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 QA meta doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof","produced_at_utc":"2026-06-19T04:10:45Z","proof_anchor":"audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt","record_type":"epic034_pr04_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d","size_bytes":2003,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
* `TESTS_PASS_OK`  
  * PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
* `EVIDENCE_INDEX_UPDATED_OK`  
  * PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  * PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
* `MACHINE_MIRROR_UPDATED_OK`  
  * PR Artifacts → Diff \- W-001 Remediation PR-04 HDE-EPIC034.md → `+{"artifact_key":"index.machine_mirror","discovered_physical_path":"artifacts/evidence_index.jsonl","produced_at_utc":"2026-06-19T04:10:45Z","proof_anchor":"artifacts/evidence_index.jsonl.path_proof.txt","role":"self_record","sha256":"84cf00d6367b43c4ae3346e5055675ccd2b6150910d4651766ff01649f334eb9","size_bytes":152507}`  
  * PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
  * PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
   Type: LF-terminated adapter/presenter boundary proof log  
   Key proof facts copied verbatim from PR Artifacts:  
  * `work_item=W-001`  
  * `classification_categories_used=allowed,forbidden,unknown / fail-closed,out of scope`  
  * `unknown_current_categories_fail_closed=true`  
     sha256: `83b9e08dffb16218900725381c5bb6010582db6c74a3c216c4664219de496910`  
* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`  
   Type: Path proof  
   Key proof facts copied verbatim from PR Artifacts:  
  * `path: artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  * `size_bytes: 10557`  
  * `produced_at_utc: 2026-06-19T04:10:43Z`  
     sha256: `83b9e08dffb16218900725381c5bb6010582db6c74a3c216c4664219de496910`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log`  
   Type: LF-terminated PR-scoped boundary check log  
   Key proof facts copied verbatim from PR Artifacts:  
  * `scope=HDE-EPIC034 PR-04 boundary check for W-001 / HDE-FERM007.4`  
  * `conservative_positive_boundary_contract_applied=true`  
  * `unknown_current_categories_fail_closed=true`  
     sha256: `5fc914e14ed527d76e2e3f7f0cd46bac89926d14c23967cd871419098769c85b`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`  
   Type: Path proof  
   Key proof facts copied verbatim from PR Artifacts:  
  * `path: audit/qa/hde-epic034/pr-04/boundary_check.log`  
  * `size_bytes: 1907`  
  * `produced_at_utc: 2026-06-19T04:10:43Z`  
     sha256: `5fc914e14ed527d76e2e3f7f0cd46bac89926d14c23967cd871419098769c85b`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
   Type: Current-epic doc-delta surface  
   Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr04.doc_deltas"`  
  * `"record_type":"epic034_pr04_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
     sha256: `6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d`  
* Path: `audit/qa/hde-epic034/00_meta/doc_deltas.md`  
   Type: Current-epic QA meta doc-delta surface  
   Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr04.qa_meta_doc_deltas"`  
  * `"record_type":"epic034_pr04_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
     sha256: `6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d`  
* Path: `docs/evidence/INDEX.json`  
   Type: Human Evidence Index  
   Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.human_index"`  
  * `"discovered_physical_path":"docs/evidence/INDEX.json"`  
  * `"role":"snapshot"`  
     sha256: `f77d18ae5e125c3ecc51f2fecb6fff5afd8eb5806e3c8816a03c14cd872c77f9`  
* Path: `artifacts/evidence_index.jsonl`  
   Type: Machine Evidence Mirror  
   Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.machine_mirror"`  
  * `"discovered_physical_path":"artifacts/evidence_index.jsonl"`  
  * `"role":"self_record"`  
     sha256: `84cf00d6367b43c4ae3346e5055675ccd2b6150910d4651766ff01649f334eb9`

C) Test/CI proof

* Job or test name: `python -m pip install -r requirements-dev.txt`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pip install -r requirements-dev.txt`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python -m pytest --version`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest --version`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
   Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing  
* Job or test name: `git diff --check`  
   Pass indicator copied verbatim: `✅ git diff --check`  
   Where it appears in PR Artifacts: PR Artifacts → Actions \- W-001 Remediation PR-04 HDE-EPIC034.md → Testing

## 2.15) W-002 Remediation PR-04 HDE-EPIC034 

Review Summary

* The PR implements W-002 for HDE-EPIC034 PR-04 remediation by splitting boundary analysis from evidence rendering.  
* The PR aligns with the Approved Plan’s W-002 scope: the analyzer now owns findings, unknowns, public route deltas, guard provenance, presenter provenance, serializer findings, external-I/O findings, evidence-family bindings, unsupported-scope claims, checks, and final verdict status.  
* The PR preserves W-001’s conservative positive boundary contract and adds a renderer guard so non-PASS analyzer verdicts cannot render PASS evidence.  
* Tests and evidence posture are sufficient for W-002: PR Artifacts record targeted renderer/analyzer tests, full targeted pytest, evidence generation, evidence index update/check, canonical JSON gate, orientation update/check, evidence path validation, mirror schema, evidence-index hash, LF checks, and `git diff --check` as passed.  
* Diff review found no scope drift into HDE-FERM007.5, HDE-FERM008, runtime v2 conformance, live vendor conformance, open-rails smoke, public Reader change, new HTTP home, or AI scope.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.4.  
* Status recommendation: No status change recommended. W-002 is an accepted remediation slice, but the Approved Plan still keeps W-003, W-004, and W-005 outstanding before HDE-FERM007.4 can support Done.  
* RCA is included because PR Artifacts explicitly record a reported P2 bug and its fix.

Diff Review

1. DR-001  
   Change summary: Updates the Machine Evidence Mirror rows for W-002 PR-04 boundary proof, boundary check, canonical JSON gates, doc-deltas, human index, and mirror self-records.  
   Risk assessment: Medium  
   Why it matters: W-002 acceptance depends on governed evidence rows reflecting the final analyzer/rendering split and the later P2 non-PASS verdict guard.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → Diff → `@@ -59,155 +59,155 @@`; PR Artifacts → Diff → `@@ -235,105 +235,105 @@`; PR Artifacts → Diff → `@@ -342,30 +342,30 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
2. DR-002  
   Change summary: Updates Machine Evidence Mirror path-proof and checksum sidecars.  
   Risk assessment: Low  
   Why it matters: Mirror byte changes require coherent path-proof and hash sidecars.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → Diff → `@@ -1,6 +1,6 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
3. DR-003  
   Change summary: Refreshes narrative router proof path-proofs.  
   Risk assessment: Medium  
   Why it matters: These are broad proof-refresh side effects outside W-002’s main behavior; final path validation must cover them.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: N/A  
4. DR-004  
   Change summary: Updates `adapter_boundary_proof.log` and its path proof to W-002 analyzer-owned / renderer-only posture.  
   Risk assessment: Low  
   Why it matters: This is the primary W-002 governed proof output.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`; PR Artifacts → Diff → `@@ -1,53 +1,58 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
5. DR-005  
   Change summary: Refreshes HDAPI v2 supporting contract inventory artifacts and path proofs.  
   Risk assessment: Medium  
   Why it matters: W-002 must preserve prior vendor evidence-family coherence while changing boundary-proof ownership.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt b/artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt b/artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md b/artifacts/vendor/hdapi_v2/known_anomalies.md`; PR Artifacts → Diff → `@@ -1,15 +1,15 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt b/artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log b/artifacts/vendor/hdapi_v2/openapi_validation.log`; PR Artifacts → Diff → `@@ -1,26 +1,26 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt b/artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
6. DR-006  
   Change summary: Refreshes source-selection, request-shaping, response-mapping, source-inventory, and v1 legacy dependency evidence and path proofs.  
   Risk assessment: Medium  
   Why it matters: W-002 must preserve prior dependency evidence families and not reimplement PR-01 through PR-03.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json b/artifacts/vendor/hdapi_v2/source_inventory.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md b/artifacts/vendor/hdapi_v2/source_inventory.md`; PR Artifacts → Diff → `@@ -1,28 +1,28 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt b/artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt b/artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log`; PR Artifacts → Diff → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt b/artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
7. DR-007  
   Change summary: Refreshes writer and doc-delta path proofs.  
   Risk assessment: Medium  
   Why it matters: These are proof-refresh side effects, so they require final path/mirror validation.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: N/A  
8. DR-008  
   Change summary: Refreshes canonical JSON gate artifacts and path proofs.  
   Risk assessment: Low  
   Why it matters: W-002 final testing includes the canonical JSON gate and updates corresponding governed evidence.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/canonical_json.gate.json b/audit/gates/canonical_json/canonical_json.gate.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt b/audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canon_compare.log b/audit/gates/canonical_json/json_canon_compare.log`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt b/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canonical_check.log b/audit/gates/canonical_json/json_canonical_check.log`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt b/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_structured_record.json b/audit/gates/json_gate/canonical/json_gate_structured_record.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-002  
9. DR-009  
   Change summary: Refreshes narrative, topology, EPIC030, EPIC033, and prior EPIC034 QA path proofs and check logs.  
   Risk assessment: Medium  
   Why it matters: These broad proof refreshes are outside W-002 behavior but covered by the final evidence validation commands.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log b/audit/qa/hde-epic033/acceptance_map_viability.log`; PR Artifacts → Diff → `@@ -1,8 +1,8 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt b/audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt b/audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log b/audit/qa/hde-epic034/pr-01/source_selection_check.log`; PR Artifacts → Diff → `@@ -1,19 +1,19 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-01/source_selection_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log b/audit/qa/hde-epic034/pr-02/request_shaping_check.log`; PR Artifacts → Diff → `@@ -1,14 +1,14 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-02/request_shaping_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log b/audit/qa/hde-epic034/pr-03/response_mapping_check.log`; PR Artifacts → Diff → `@@ -1,19 +1,19 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-03/response_mapping_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: N/A  
10. DR-010  
    Change summary: Updates the W-002 PR-04 boundary check log and its path proof.  
    Risk assessment: Low  
    Why it matters: The check log is the PR-scoped PASS proof for analyzer/rendering separation.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log b/audit/qa/hde-epic034/pr-04/boundary_check.log`; PR Artifacts → Diff → `@@ -1,37 +1,49 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-002  
11. DR-011  
    Change summary: Refreshes acceptance-map and human Evidence Index/hash files with path proofs.  
    Risk assessment: Medium  
    Why it matters: W-002 evidence changes require same-PR human index and hash sentinel refresh.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/acceptance_map_epic033.json b/docs/acceptance_map_epic033.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/acceptance_map_epic033.json.path_proof.txt b/docs/acceptance_map_epic033.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
    Approved Plan linkage: Approved Plan → Work Item W-002  
12. DR-012  
    Change summary: Adds targeted W-002 tests for analyzer output consumption, renderer non-PASS rejection, UNKNOWN/FORBIDDEN refusal, finding preservation, and no-claim posture.  
    Risk assessment: Low  
    Why it matters: These tests directly cover the W-002 renderer/analyzer split and the recorded P2 bug.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -1,31 +1,32 @@`; PR Artifacts → Diff → `@@ -3179,48 +3180,145 @@ from flask import Flask`  
    Approved Plan linkage: Approved Plan → Work Item W-002  
13. DR-013  
    Change summary: Refactors `generate_hdapi_v2_contract_inventory.py` so the generator renders analyzer-owned output, rejects UNKNOWN/FORBIDDEN PASS states, rejects non-PASS analyzer verdicts, and updates the boundary check renderer.  
    Risk assessment: High  
    Why it matters: This is the critical boundary between analysis and evidence rendering; a bug here can recreate false PASS evidence.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -1862,318 +1862,207 @@ def _boundary_finding(category: str, classification: str, verdict: str, inspecte`  
    Approved Plan linkage: Approved Plan → Work Item W-002  
14. DR-014  
    Change summary: Updates `hdapi_v2_boundary_analyzer.py` with structured analyzer-owned result output and W-002 work-item metadata.  
    Risk assessment: High  
    Why it matters: The analyzer result is now the source of truth for findings, unknowns, deltas, provenance, bindings, checks, and verdict status.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`; PR Artifacts → Diff → `@@ -1219,52 +1219,59 @@ def _pure_compute_external_io(loci: tuple[str, ...]) -> list[str]`; PR Artifacts → Diff → `@@ -1567,25 +1574,181 @@ def _unsupported_scope_claims(*payloads: dict[str, Any]) -> list[str]`  
    Approved Plan linkage: Approved Plan → Work Item W-002

RCA

A) Bug/Failure statement

PR Artifacts record a reported P2 bug after the initial W-002 implementation: “A bug was found, referenced here:” and the final summary says the renderer previously could accept an analyzer result whose `verdict_status` was not PASS when the legacy checks map was otherwise true. PR Artifacts then state: “Fixed the reported P2 bug by making the renderer reject analyzer results whose authoritative verdict\_status is not PASS, even when the legacy checks map is otherwise all true.”

B) Root cause(s)

1. The renderer still trusted the legacy checks map more than the analyzer’s authoritative verdict.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Fixed the reported P2 bug by making the renderer reject analyzer results whose authoritative verdict_status is not PASS, even when the legacy checks map is otherwise all true.`  
2. The PR-04 check log did not initially include a direct gate requiring the analyzer-owned verdict to be PASS.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Added a boundary-check-log gate requiring analyzer_owned_verdict_status=PASS, so the PR-04 check log cannot pass if a proof somehow reports a non-PASS analyzer-owned verdict.`

C) Fix in this PR

* The renderer now rejects analyzer results whose `verdict_status` is not PASS.  
* The boundary check log now includes `[analyzer_owned_verdict_pass] status=PASS`.  
* Regression coverage now requires synthetic analyzer results with all checks true but verdict status UNKNOWN or FAIL to be rejected.  
* Governed PR-04 W-002 evidence was regenerated after the fix.

D) Fix verification

* PR Artifacts record the targeted regression command as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w002_renderer_refuses_non_pass_analyzer_verdict_even_when_checks_pass tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w002_renderer_refuses_unknown_or_forbidden_pass tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w002_analyzer_findings_survive_rendering_and_no_claims_remain -q`  
* PR Artifacts record full targeted pytest as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
* PR Artifacts record final evidence-index, path, mirror, hash, LF, and diff checks as passed.

Findings

1. F-001 (DR-001): The Machine Evidence Mirror now includes updated W-002 boundary proof and boundary check records.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T06:56:49Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"aee8d984efd3182553042a6d1dd16e663346a2c230517747437ffb63101b98ac","size_bytes":10953,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
   Why it matters: This binds the main W-002 proof artifact to the governed mirror.  
2. F-002 (DR-002): Mirror hash and path-proof sidecars were refreshed.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`  
   Why it matters: Mirror sidecars must match final mirror bytes.  
3. F-003 (DR-003): Narrative router proof path refreshes are validation-covered.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Why it matters: Broad proof refreshes are acceptable only with final path validation.  
4. F-004 (DR-004): The primary boundary proof now states analyzer/rendering separation and renderer-only posture.  
   Evidence pointer: PR Artifacts → Diff → `+analyzer_rendering_separation=analyzer owns findings, unknowns, deltas, provenance, bindings, and verdicts; renderer only emits analyzer output`  
   Evidence pointer: PR Artifacts → Diff → `+renderer_only_posture=evidence generator does not rediscover route, guard, presenter, serializer, external-I/O, or boundary truth`  
   Why it matters: This implements W-002’s intended split.  
   PF references only when needed:  
   PF10 — HDE Build Notes, §2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation  
   Canon proof excerpt:  
   "Boundary analysis MUST be separated from evidence rendering."  
   "The analyzer should return explicit findings, unknowns, public route deltas, responder provenance, serializer findings, external-I/O findings, guard provenance, evidence-family bindings, and verdict status."  
5. F-005 (DR-005): HDAPI v2 supporting contract evidence was regenerated but remains dependency context, not W-002 scope expansion.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/contract_map.json b/artifacts/vendor/hdapi_v2/contract_map.json`  
   Why it matters: W-002 consumes prior vendor evidence context while preserving the boundary-proof scope.  
6. F-006 (DR-006): Prior source-selection, request-shaping, response-mapping, and legacy guard evidence families remain refreshed and bound.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json b/artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
   Why it matters: W-002 must not duplicate or weaken prior accepted slices.  
7. F-007 (DR-007): Writer and doc-delta path-proof refreshes are proof-only and validation-covered.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Why it matters: These broad side effects are not blockers because final path validation passed.  
8. F-008 (DR-008): Canonical JSON gate artifacts were refreshed and the canonical JSON gate was run.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`  
   Why it matters: W-002 evidence changes include governed JSON surfaces and canonicality must remain proven.  
9. F-009 (DR-009): Historical QA and prior PR proof refreshes are present and validation-covered.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Why it matters: Broad proof churn is acceptable only when governed evidence validation passes.  
10. F-010 (DR-010): The boundary check log proves analyzer/rendering separation, renderer-only posture, analyzer verdict gate, and carried findings.  
    Evidence pointer: PR Artifacts → Diff → `+[analyzer_rendering_separation_applied] status=PASS`  
    Evidence pointer: PR Artifacts → Diff → `+[generator_rendered_analyzer_output_only] status=PASS`  
    Evidence pointer: PR Artifacts → Diff → `+[analyzer_owned_verdict_pass] status=PASS`  
    Why it matters: This is the PR-scoped W-002 PASS proof.  
11. F-011 (DR-011): Human Evidence Index and hash sentinel are updated for the regenerated evidence.  
    Evidence pointer: PR Artifacts → Diff → `+sha256: fa43de1f35bc8a2b4bc5fe51ce9d216882c0b689a40d47c31210e168f74eed09`  
    Evidence pointer: PR Artifacts → Diff → `+fa43de1f35bc8a2b4bc5fe51ce9d216882c0b689a40d47c31210e168f74eed09 docs/evidence/INDEX.json`  
    Why it matters: Evidence parity and hash freshness are required for governed proof trust.  
12. F-012 (DR-012): Tests cover analyzer output consumption and renderer refusal of non-PASS analyzer verdicts.  
    Evidence pointer: PR Artifacts → Diff → `+def test_epic034_w002_generator_consumes_analyzer_output_without_recomputing(monkeypatch: pytest.MonkeyPatch) -> None:`  
    Evidence pointer: PR Artifacts → Diff → `+def test_epic034_w002_renderer_refuses_non_pass_analyzer_verdict_even_when_checks_pass() -> None:`  
    Why it matters: These tests directly cover the W-002 objective and the P2 bug.  
13. F-013 (DR-013): The generator now has a renderer guard that refuses UNKNOWN/FORBIDDEN PASS and non-PASS analyzer verdicts.  
    Evidence pointer: PR Artifacts → Diff → `+ if result.get("verdict_status") != "PASS":`  
    Evidence pointer: PR Artifacts → Diff → `+ raise ValueError(f"ADAPTER_BOUNDARY_ANALYZER_VERDICT_NON_PASS:{result.get('verdict_status', 'MISSING')}")`  
    Why it matters: This closes the final reported false-PASS path in the renderer.  
14. F-014 (DR-014): The analyzer now returns a structured W-002 result with inspected loci, findings, unknowns, public route deltas, provenance objects, checks, and verdict status.  
    Evidence pointer: PR Artifacts → Diff → `+ "work_item": "W-002",`  
    Evidence pointer: PR Artifacts → Diff → `+ "checks": checks,`  
    Evidence pointer: PR Artifacts → Diff → `+ "verdict_status": verdict_status,`  
    Why it matters: The analyzer is now the owner of boundary truth for W-002.  
15. F-015: Final validation is complete after the P2 bug fix.  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ git diff --check`  
    Why it matters: The accepted state is the post-bug-fix state, not the initial W-002 implementation.

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.4  
   Current PF09 status: Task status: Not done; Subtask status: Not done  
   Status recommendation: No status change recommended  
   Why this status posture is supported: W-002 implements analyzer/rendering separation for the PR-04 proof model, but the Approved Plan still lists W-003 taxonomy replacement, W-004 route-drift proof repair, and W-005 final validation before HDE-FERM007.4 can support Done.  
   Evidence pointer(s): Approved Plan → Work Item W-002 → `* Intent: Split boundary analysis from evidence rendering so the analyzer returns explicit findings, unknowns, deltas, guard provenance, and verdicts, while the evidence generator only renders those results.`  
   Evidence pointer(s): Approved Plan → Work Item W-005 → `* Dependencies: W-001 through W-004 complete.`  
   Evidence pointer(s): PR Artifacts → Diff → `+analyzer_owned_verdict_status=PASS`  
   PF proof excerpt(s) when PF09 is relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
   "Task ID: HDE-FERM007"  
   "Task status: Not done"  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.4 \- Preserve adapter and presenter boundaries  
   "Ensure the v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, and does not introduce ad-hoc serialization. Adapter remains the HTTP home; presenter remains the byte-authoritative emitter; deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam."  
   "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T06:56:49Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"aee8d984efd3182553042a6d1dd16e663346a2c230517747437ffb63101b98ac","size_bytes":10953,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr04.boundary_check","discovered_physical_path":"audit/qa/hde-epic034/pr-04/boundary_check.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 boundary check log for adapter HTTP home, presenter boundary, serializer, pure-compute, and prior-family binding posture","produced_at_utc":"2026-06-19T06:56:49Z","proof_anchor":"audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"804404f45980389de1b8f2e16ca33370448651f1d467a311d8a2c9073975e72a","size_bytes":2732,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr04.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 current-epic doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof","produced_at_utc":"2026-06-19T06:33:42Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr04_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d","size_bytes":2003,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
* `JSON_CANONICAL_CHECK_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"canonical_json.check_log","discovered_physical_path":"audit/gates/canonical_json/json_canonical_check.log","produced_at_utc":"2026-06-19T06:40:55Z","proof_anchor":"audit/gates/canonical_json/json_canonical_check.log.path_proof.txt","record_type":"canonical_json_gate_log","role":"log","schema_version":"1.0","sha256":"39816887268ba549e3495be7f838f3bb4a9dd9bc81472e47ff5392a9d17e0a67","size_bytes":7268,"tokens":["JSON_CANONICAL_CHECK_OK"]}`  
  * PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  Type: LF-terminated adapter/presenter boundary proof log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `work_item=W-002`  
  * `analyzer_owned_verdict_status=PASS`  
  * `renderer_only_posture=evidence generator does not rediscover route, guard, presenter, serializer, external-I/O, or boundary truth`  
    sha256: `aee8d984efd3182553042a6d1dd16e663346a2c230517747437ffb63101b98ac`  
* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  * `size_bytes: 10953`  
  * `produced_at_utc: 2026-06-19T06:56:49Z`  
    sha256: `aee8d984efd3182553042a6d1dd16e663346a2c230517747437ffb63101b98ac`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log`  
  Type: LF-terminated PR-scoped boundary check log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `scope=HDE-EPIC034 PR-04 boundary check for W-002 / HDE-FERM007.4`  
  * `[analyzer_rendering_separation_applied] status=PASS`  
  * `[analyzer_owned_verdict_pass] status=PASS`  
    sha256: `804404f45980389de1b8f2e16ca33370448651f1d467a311d8a2c9073975e72a`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: audit/qa/hde-epic034/pr-04/boundary_check.log`  
  * `size_bytes: 2732`  
  * `produced_at_utc: 2026-06-19T06:56:49Z`  
    sha256: `804404f45980389de1b8f2e16ca33370448651f1d467a311d8a2c9073975e72a`  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.human_index"`  
  * `"discovered_physical_path":"docs/evidence/INDEX.json"`  
  * `"role":"snapshot"`  
    sha256: `fa43de1f35bc8a2b4bc5fe51ce9d216882c0b689a40d47c31210e168f74eed09`  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Evidence Mirror  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.machine_mirror"`  
  * `"discovered_physical_path":"artifacts/evidence_index.jsonl"`  
  * `"role":"self_record"`  
    sha256: `574603258819f322daa670216d0575334d729fbed6d3887c517ec6a26f08b882`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
  Type: Current-epic doc-delta surface  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr04.doc_deltas"`  
  * `"record_type":"epic034_pr04_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d`

C) Test/CI proof

* Job or test name: `python -m pip install -r requirements-dev.txt`  
  Pass indicator copied verbatim: `✅ python -m pip install -r requirements-dev.txt`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest --version`  
  Pass indicator copied verbatim: `✅ python -m pytest --version`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/run_canonical_json_gate.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `git diff --check`  
  Pass indicator copied verbatim: `✅ git diff --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

Doc Deltas: None (no PF-Canon inconsistencies or new doc requirements found)

PF09 Impact Summary

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.4  
   Current status if evidenced: Task status: Not done; Subtask status: Not done  
   Status action: No status change recommended  
   Evidence pointer(s): PR Artifacts → Diff → `+analyzer_owned_verdict_status=PASS`  
   Linked Findings item(s): F-004; F-010; F-012; F-013; F-014; F-015  
   Linked CHG item(s), if any: CHG-001; CHG-002; CHG-003; CHG-004; CHG-005

Doc Delta Detection Workflow

CHG-001  
Change claim type: workflow steps  
Change claim: Boundary analysis is split from evidence rendering; analyzer owns findings, unknowns, deltas, provenance, bindings, and verdicts, while the renderer only emits analyzer output.  
Evidence pointer: PR Artifacts → Diff → `+analyzer_rendering_separation=analyzer owns findings, unknowns, deltas, provenance, bindings, and verdicts; renderer only emits analyzer output`  
Canon basis: CANON ALIGNED

CHG-002  
Change claim type: evidence posture  
Change claim: Renderer-only posture is now explicit and the evidence generator does not rediscover route, guard, presenter, serializer, external-I/O, or boundary truth.  
Evidence pointer: PR Artifacts → Diff → `+renderer_only_posture=evidence generator does not rediscover route, guard, presenter, serializer, external-I/O, or boundary truth`  
Canon basis: CANON ALIGNED

CHG-003  
Change claim type: behavior or output  
Change claim: Renderer rejects non-PASS analyzer verdicts even if legacy checks are true.  
Evidence pointer: PR Artifacts → Diff → `+ raise ValueError(f"ADAPTER_BOUNDARY_ANALYZER_VERDICT_NON_PASS:{result.get('verdict_status', 'MISSING')}")`  
Canon basis: CANON ALIGNED

CHG-004  
Change claim type: governed paths or artifact families  
Change claim: W-002 boundary proof and boundary check evidence are regenerated under existing governed artifact paths with path proofs and mirror/index updates.  
Evidence pointer: PR Artifacts → Diff → `+work_item=W-002`  
Canon basis: CANON ALIGNED

CHG-005  
Change claim type: PF09 status-impact requirement  
Change claim: W-002 contributes to HDE-FERM007.4 remediation but does not support a PF09 status change yet.  
Evidence pointer: Approved Plan → Work Item W-005 → `* Dependencies: W-001 through W-004 complete.`  
Canon basis: CANON ALIGNED

## 2.16) W-003 Remediation PR-04 HDE-EPIC034

Artifact Map

PR Name: W-003

PR Artifacts Bundle: W-003 Remediation PR-04 HDE-EPIC034.md

Approved Plan: r1 Remediation PR-04 HDE-EPIC034.md

Output: PR Final Review

Review Summary

* The PR implements W-003 for HDE-EPIC034 PR-04 remediation by adding analyzer-owned W-003 boundary taxonomy metadata and a table-driven invariant suite for the required boundary categories.  
* The PR aligns with the Approved Plan’s W-003 scope: it targets HDE-FERM007.4 only and replaces narrow one-off fixtures with taxonomy coverage across allowed, forbidden, unknown / fail-closed, and out-of-scope cases.  
* The PR preserves accepted W-001 and W-002 posture: conservative fail-closed boundary classification remains in force, and analyzer-owned findings remain separate from renderer-only evidence output.  
* The PR includes bug-fix rounds for taxonomy semantics, negative-category rendering, raw public response bypass detection, fake/import-alias emitter paths, unsupported-scope taxonomy coverage, and declared-vs-covered taxonomy reporting.  
* Tests and evidence posture look sufficient for W-003: PR Artifacts record targeted taxonomy tests, full targeted pytest, evidence index update/check, path validation, mirror schema, evidence-index hash, LF checks, canonical JSON gate, orientation check, and `git diff --check` as passed.  
* Diff review covers all 53 diff hunks across 47 file patches by grouping related evidence, proof, index, test, generator, and analyzer hunks.  
* Exact impacted PF09 item: PF09.5 — HDE Build Checklist Fermentation, task HDE-FERM007, subtask HDE-FERM007.4.  
* Status recommendation: No status change recommended. W-003 is an accepted remediation slice, but the Approved Plan still keeps W-004 and W-005 outstanding before HDE-FERM007.4 can support Done.  
* RCA is included because PR Artifacts explicitly record two bug reports and their fixes.

Diff Review

1. DR-001  
   Change summary: Updates the Machine Evidence Mirror rows for W-003 PR-04 boundary proof, boundary check, doc-deltas, canonical JSON gates, human index, and machine mirror self-records.  
   Risk assessment: Medium  
   Why it matters: W-003 acceptance depends on governed evidence rows reflecting the final taxonomy proof and bug-fix state.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl b/artifacts/evidence_index.jsonl`; PR Artifacts → Diff → `@@ -59,155 +59,155 @@`; PR Artifacts → Diff → `@@ -235,105 +235,105 @@`; PR Artifacts → Diff → `@@ -342,30 +342,30 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
2. DR-002  
   Change summary: Updates Machine Evidence Mirror path-proof and checksum sidecars.  
   Risk assessment: Low  
   Why it matters: Mirror byte changes require matching path-proof and hash sidecars.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.path_proof.txt b/artifacts/evidence_index.jsonl.path_proof.txt`; PR Artifacts → Diff → `@@ -1,6 +1,6 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256.path_proof.txt b/artifacts/evidence_index.jsonl.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
3. DR-003  
   Change summary: Refreshes narrative router path proofs, writer path proofs, and doc-delta path proofs.  
   Risk assessment: Medium  
   Why it matters: These are broad governed proof-refresh side effects, so final path validation must cover them.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/cli_http_parity.log.path_proof.txt b/artifacts/narratives/router/cli_http_parity.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/narratives/router/parity_abba.log.path_proof.txt b/artifacts/narratives/router/parity_abba.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_write_readback.log.path_proof.txt b/artifacts/writer/conjunction_write_readback.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/artifacts/writer/conjunction_writer_summary.json.path_proof.txt b/artifacts/writer/conjunction_writer_summary.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt b/audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: N/A  
4. DR-004  
   Change summary: Updates `adapter_boundary_proof.log` and its path proof for W-003 table-driven taxonomy coverage.  
   Risk assessment: Low  
   Why it matters: This is the primary W-003 governed proof artifact.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`; PR Artifacts → Diff → `@@ -1,72 +1,107 @@`; PR Artifacts → Diff → `diff --git a/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt b/artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
5. DR-005  
   Change summary: Refreshes canonical JSON gate artifacts and path proofs.  
   Risk assessment: Low  
   Why it matters: W-003 evidence changes include governed JSON surfaces, so canonical JSON proof must remain current.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/canonical_json.gate.json b/audit/gates/canonical_json/canonical_json.gate.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt b/audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canon_compare.log b/audit/gates/canonical_json/json_canon_compare.log`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt b/audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canonical_check.log b/audit/gates/canonical_json/json_canonical_check.log`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt b/audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`; PR Artifacts → Diff → `@@ -1,18 +1,18 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_structured_record.json b/audit/gates/json_gate/canonical/json_gate_structured_record.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt b/audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
6. DR-006  
   Change summary: Refreshes narrative, topology, and EPIC030 path proofs.  
   Risk assessment: Medium  
   Why it matters: These broad proof refreshes are outside W-003’s main behavior but are acceptable when governed evidence validation passes.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/gates/narratives/keys_10x4.table.json.path_proof.txt b/audit/gates/narratives/keys_10x4.table.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/pack_identity.txt.path_proof.txt b/audit/gates/narratives/pack_identity.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/narratives/registry.diff.json.path_proof.txt b/audit/gates/narratives/registry.diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/gates/topology/orientation_demo.txt.path_proof.txt b/audit/gates/topology/orientation_demo.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt b/audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt b/audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt b/audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: N/A  
7. DR-007  
   Change summary: Updates EPIC034 QA meta doc-delta path proof, W-003 PR-04 boundary check log, and boundary-check path proof.  
   Risk assessment: Low  
   Why it matters: The boundary check log is the PR-scoped proof surface that W-003 taxonomy gates are applied.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt b/audit/qa/hde-epic034/00_meta/doc_deltas.md.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log b/audit/qa/hde-epic034/pr-04/boundary_check.log`; PR Artifacts → Diff → `@@ -1,49 +1,55 @@`; PR Artifacts → Diff → `diff --git a/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt b/audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
8. DR-008  
   Change summary: Updates Human Evidence Index, hash sentinel, and path proofs.  
   Risk assessment: Medium  
   Why it matters: PR-04 evidence changes require same-PR human index, machine mirror, and hash sentinel parity.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json b/docs/evidence/INDEX.json`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.json.path_proof.txt b/docs/evidence/INDEX.json.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256 b/docs/evidence/INDEX.sha256`; PR Artifacts → Diff → `@@ -1 +1 @@`; PR Artifacts → Diff → `diff --git a/docs/evidence/INDEX.sha256.path_proof.txt b/docs/evidence/INDEX.sha256.path_proof.txt`; PR Artifacts → Diff → `@@ -1,5 +1,5 @@`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
9. DR-009  
   Change summary: Adds the table-driven W-003 invariant suite and adjusts the existing presenter-bypass taxonomy regression area.  
   Risk assessment: Low  
   Why it matters: W-003’s central requirement is to replace one-off bug fixtures with taxonomy-driven invariant coverage.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/tests/evidence/test_hdapi_v2_contract_inventory.py b/tests/evidence/test_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -823,50 +823,335 @@ def test_epic034_adapter_boundary_builder_fails_closed_on_missing_locus(monkeypa`; PR Artifacts → Diff → `@@ -3180,51 +3465,51 @@ from flask import Flask`  
   Approved Plan linkage: Approved Plan → Work Item W-003  
10. DR-010  
    Change summary: Updates the boundary proof renderer to emit W-003 taxonomy scope, required/covered groups, missing-category posture, and taxonomy verdict summaries.  
    Risk assessment: Medium  
    Why it matters: The renderer must expose taxonomy coverage without turning taxonomy coverage itself into misleading current-repo boundary PASS claims.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/generate_hdapi_v2_contract_inventory.py b/tools/evidence/generate_hdapi_v2_contract_inventory.py`; PR Artifacts → Diff → `@@ -1880,89 +1880,123 @@ def _vendor_guard_provenance_findings(loci: tuple[str, ...]) -> tuple[list[str],`; PR Artifacts → Diff → `@@ -1975,83 +2009,89 @@ def build_adapter_boundary_proof(produced: str, source_selection: dict[str, Any]`  
    Approved Plan linkage: Approved Plan → Work Item W-003  
11. DR-011  
    Change summary: Hardens presenter-bypass analysis for raw strings/bytes, `Response(...)`, `make_response(...)`, and assigned unpresented payloads.  
    Risk assessment: Medium  
    Why it matters: The bug-fix evidence says these raw public-response paths were previously falling through to unresolved/unknown provenance rather than forbidden presenter-bypass findings.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`; PR Artifacts → Diff → `@@ -522,70 +522,95 @@ def _adapter_presenter_bypass_routes(loci: tuple[str, ...]) -> list[str]:`  
    Approved Plan linkage: Approved Plan → Work Item W-003  
12. DR-012  
    Change summary: Extends unsupported-scope detection and W-003 taxonomy group declarations/classification requirements.  
    Risk assessment: Medium  
    Why it matters: W-003 taxonomy coverage must include explicit unsupported-scope/no-claim posture and all required groups must be visible.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`; PR Artifacts → Diff → `@@ -1581,50 +1606,83 @@ def _unsupported_scope_claims(*payloads: dict[str, Any]) -> list[str]:`  
    Approved Plan linkage: Approved Plan → Work Item W-003  
13. DR-013  
    Change summary: Updates `analyze_adapter_boundary(...)` to include W-003 taxonomy rows, required taxonomy group reporting, missing taxonomy groups, taxonomy checks, and rendered current-classification/current-verdict split.  
    Risk assessment: High  
    Why it matters: This is the core analyzer-owned taxonomy implementation and the main place where false PASS risk must remain controlled.  
    Evidence pointer: PR Artifacts → Diff → `diff --git a/tools/evidence/hdapi_v2_boundary_analyzer.py b/tools/evidence/hdapi_v2_boundary_analyzer.py`; PR Artifacts → Diff → `@@ -1687,68 +1745,85 @@ def analyze_adapter_boundary(`  
    Approved Plan linkage: Approved Plan → Work Item W-003

RCA

A) Bug/Failure statement

PR Artifacts record two bug-fix rounds after the initial W-003 implementation. The first bug report caused a fix where “taxonomy coverage is no longer conflated with current repo boundary findings,” and the second caused presenter-bypass hardening for “raw string/bytes payloads, Response(...)/make\_response(...) payloads, and assigned unpresented payloads.”

B) Root cause(s)

1. Taxonomy coverage rows initially conflated invariant coverage with current repo findings.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Fixed the W-003 taxonomy semantics so taxonomy coverage is no longer conflated with current repo boundary findings.`  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Updated boundary proof rendering so negative-coverage groups such as presenter_bypass_paths and pure_compute_forbidden_operations are rendered as covered invariant categories with explicit required case classifications, rather than as misleading classification=allowed verdict=PASS taxonomy rows.`  
2. Presenter-bypass analysis initially let raw public response forms fall through to unresolved/unknown provenance.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Hardened presenter-bypass analysis so raw string/bytes payloads, Response(...)/make_response(...) payloads, and assigned unpresented payloads are classified as presenter-bypass findings instead of falling through to unresolved/unknown provenance.`  
3. The unsupported-scope/no-claim posture needed explicit taxonomy coverage.  
   Evidence pointer(s): PR Artifacts → Actions Taken → `Expanded W-003 taxonomy coverage to include explicit unsupported-scope/no-claim posture and to require forbidden import/alias cases where local shadowing or fake emitters produce raw responses.`

C) Fix in this PR

* The analyzer now records required case classifications per taxonomy group separately from current analyzer classification and current verdict.  
* Boundary proof rendering now distinguishes declared taxonomy groups, actually covered groups, required case classifications, current classification, current verdict, and coverage status.  
* Presenter-bypass analysis now classifies raw public response payloads and assigned unpresented payloads as forbidden presenter-bypass findings.  
* W-003 tests now cover required case classifications, four classification classes, unsupported-scope coverage, fake/import-alias emitter paths, and the prior negative-group relabeling bug.

D) Fix verification

* PR Artifacts record the initial W-003 taxonomy suite as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
* PR Artifacts record post-bug-fix targeted taxonomy regression tests as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rows_are_analyzer_owned tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rendering_does_not_relabel_negative_groups_as_current_pass -q`  
* PR Artifacts record final broad targeted pytest as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
* PR Artifacts record final evidence checks as passed: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`, `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`, `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`, `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`, and `✅ git diff --check`.

Findings

1. F-001 (DR-001): The Machine Evidence Mirror now binds W-003 PR-04 boundary proof and boundary check artifacts.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T07:51:20Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"55a55a37eda1697b3250c42dbd9612980608afaa639798dc6e89656de25b28a9","size_bytes":17991,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
   Why it matters: This is the governed machine binding for the primary W-003 proof artifact.  
2. F-002 (DR-002): Mirror sidecars were refreshed after evidence changes.  
   Evidence pointer: PR Artifacts → Diff → `diff --git a/artifacts/evidence_index.jsonl.sha256 b/artifacts/evidence_index.jsonl.sha256`  
   Why it matters: Hash and path-proof sidecars must track the final mirror bytes.  
3. F-003 (DR-003): Narrative, writer, and doc-delta path-proof refreshes are present and validation-covered.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Why it matters: Broad path-proof churn is acceptable only when path validation remains green.  
4. F-004 (DR-004): The adapter boundary proof now records W-003 scope, taxonomy application, required/covered taxonomy groups, missing-category posture, classification categories, and taxonomy verdict summaries.  
   Evidence pointer: PR Artifacts → Diff → `+work_item=W-003`  
   Evidence pointer: PR Artifacts → Diff → `+table_driven_boundary_taxonomy=applied to analyzer-owned categories for W-003`  
   Evidence pointer: PR Artifacts → Diff → `+taxonomy_missing_category_posture=none`  
   Why it matters: This is the direct proof that W-003’s taxonomy posture is present.  
   PF references only when needed:  
   PF10 — HDE Build Notes, §2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation  
   Canon proof excerpt:  
   "PR-04 remediation MUST replace one-off bug fixtures with a table-driven taxonomy and invariant suite covering at least:"  
   "The taxonomy should make missing categories visible. It does not by itself prove all possible Python behavior; it must be paired with the fail-closed analyzer posture."  
5. F-005 (DR-005): Canonical JSON proof artifacts were refreshed and canonical JSON validation is recorded as passed.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`  
   Why it matters: W-003 regenerated governed evidence surfaces that require canonical JSON discipline.  
6. F-006 (DR-006): Narrative/topology/EPIC030 path-proof refreshes are covered by final validation.  
   Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
   Why it matters: Evidence refreshes outside W-003’s core code path do not block acceptance when governed path validation passes.  
7. F-007 (DR-007): The boundary check log proves table-driven taxonomy application, visible required groups, no silent skips, fail-closed posture, and analyzer/rendering separation.  
   Evidence pointer: PR Artifacts → Diff → `+[table_driven_boundary_taxonomy_applied] status=PASS`  
   Evidence pointer: PR Artifacts → Diff → `+[required_taxonomy_groups_covered_or_visibly_marked] status=PASS`  
   Evidence pointer: PR Artifacts → Diff → `+[no_required_taxonomy_group_silently_skipped] status=PASS`  
   Why it matters: This is the PR-scoped W-003 PASS proof.  
8. F-008 (DR-008): Human Evidence Index and hash sentinel were updated for the W-003 evidence refresh.  
   Evidence pointer: PR Artifacts → Diff → `+{"artifact_key":"index.human_index","discovered_physical_path":"docs/evidence/INDEX.json","produced_at_utc":"2026-06-19T16:54:48Z","proof_anchor":"docs/evidence/INDEX.json.path_proof.txt","role":"snapshot","sha256":"148a371f9e19f5ddaf54e62fb010e30785ede304c887025466ca1d1973afa52b","size_bytes":74591}`  
   Why it matters: Same-PR evidence index parity is required for governed proof trust.  
9. F-009 (DR-009): The W-003 test suite now contains taxonomy-owned cases and regression assertions.  
   Evidence pointer: PR Artifacts → Diff → `+def test_epic034_w003_boundary_taxonomy_covers_required_groups() -> None:`  
   Evidence pointer: PR Artifacts → Diff → `+def test_epic034_w003_taxonomy_rows_are_analyzer_owned() -> None:`  
   Evidence pointer: PR Artifacts → Diff → `+def test_epic034_w003_taxonomy_rendering_does_not_relabel_negative_groups_as_current_pass() -> None:`  
   Why it matters: These tests implement the approved table-driven invariant posture.  
10. F-010 (DR-010): The renderer now emits required case classifications, current classification, current verdict, and coverage status instead of bare taxonomy PASS labels.  
    Evidence pointer: PR Artifacts → Diff → `+ "required_case_classifications=" + json.dumps(row["required_case_classifications"], sort_keys=True, separators=(",", ":")) + " "`  
    Evidence pointer: PR Artifacts → Diff → `+ f"current_classification={row['current_classification']} "`  
    Evidence pointer: PR Artifacts → Diff → `+ f"coverage_status={row['coverage_status']} "`  
    Why it matters: This addresses the documented bug where taxonomy coverage could be confused with current repo boundary findings.  
11. F-011 (DR-011): Presenter-bypass analysis was hardened for raw public response forms.  
    Evidence pointer: PR Artifacts → Actions Taken → `Hardened presenter-bypass analysis so raw string/bytes payloads, Response(...)/make_response(...) payloads, and assigned unpresented payloads are classified as presenter-bypass findings instead of falling through to unresolved/unknown provenance.`  
    Why it matters: This reduces false-PASS risk for public response-producing paths.  
12. F-012 (DR-012): Unsupported-scope/no-claim posture is included in taxonomy groups and classification requirements.  
    Evidence pointer: PR Artifacts → Diff → `+ "unsupported_scope_no_claims": "hde_ferm007_5_runtime_v2_live_open_rails_ai_scope",`  
    Evidence pointer: PR Artifacts → Diff → `+ "unsupported_scope_no_claims": (BOUNDARY_OUT_OF_SCOPE,),`  
    Why it matters: W-003 must preserve the PR-04 scope boundary and make out-of-scope posture visible.  
13. F-013 (DR-013): The analyzer now returns W-003 taxonomy rows, missing groups, required groups, and taxonomy checks.  
    Evidence pointer: PR Artifacts → Diff → `+ "boundary_taxonomy": taxonomy_group_verdicts,`  
    Evidence pointer: PR Artifacts → Diff → `+ "missing_taxonomy_groups": missing_taxonomy_groups,`  
    Evidence pointer: PR Artifacts → Diff → `+ "required_taxonomy_groups": list(REQUIRED_BOUNDARY_TAXONOMY_GROUPS),`  
    Why it matters: The analyzer remains the source of boundary truth while W-003 adds invariant taxonomy coverage.  
14. F-014: Final test and evidence validation are sufficient for W-003.  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
    Evidence pointer: PR Artifacts → Actions Taken → `✅ git diff --check`  
    Why it matters: The accepted review state is the state after W-003 bug fixes and evidence refresh.

PF09 Impact & Status Posture

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.4  
   Current PF09 status: Task status: Not done; Subtask status: Not done  
   Status recommendation: No status change recommended  
   Why this status posture is supported: W-003 implements table-driven boundary taxonomy and invariant coverage, but the Approved Plan still lists W-004 route-drift repair and W-005 final validation before HDE-FERM007.4 can support Done.  
   Evidence pointer(s): Approved Plan → Work Item W-003 → `* Intent: Replace narrow one-off bug fixtures with a table-driven boundary taxonomy and invariant suite covering allowed, forbidden, unknown/fail-closed, and out-of-scope cases.`  
   Evidence pointer(s): Approved Plan → Work Item W-005 → `* Dependencies: W-001 through W-004 complete.`  
   Evidence pointer(s): PR Artifacts → Diff → `+[table_driven_boundary_taxonomy_applied] status=PASS`  
   PF proof excerpt(s) when PF09 is relied on:  
   PF09.5 — HDE Build Checklist Fermentation, §Task HDE-FERM007 \- HDAPI v2 vendor adapter architecture  
   "Task ID: HDE-FERM007"  
   "Task status: Not done"  
   PF09.5 — HDE Build Checklist Fermentation, §Subtask HDE-FERM007.4 \- Preserve adapter and presenter boundaries  
   "Ensure the v2 vendor seam does not create a new HTTP home, does not bypass adapter guards, and does not introduce ad-hoc serialization. Adapter remains the HTTP home; presenter remains the byte-authoritative emitter; deterministic compute remains pure except for the sanctioned BodyGraph/vendor seam."  
   "Subtask status: Not done"

Evidence Print (PASS PROOF; required)

A) Tokens satisfied

* `EVIDENCE_PATH_PROOFS_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"hdapi_v2.adapter_boundary_proof","discovered_physical_path":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 LF-terminated adapter/presenter boundary proof for HDE-FERM007.4 with no live vendor, open-rails, public Reader, HDE-FERM007.5, HDE-FERM008, or AI scope claim","produced_at_utc":"2026-06-19T07:51:20Z","proof_anchor":"artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"55a55a37eda1697b3250c42dbd9612980608afaa639798dc6e89656de25b28a9","size_bytes":17991,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr04.boundary_check","discovered_physical_path":"audit/qa/hde-epic034/pr-04/boundary_check.log","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 boundary check log for adapter HTTP home, presenter boundary, serializer, pure-compute, and prior-family binding posture","produced_at_utc":"2026-06-19T07:51:20Z","proof_anchor":"audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt","record_type":"epic034_pr04_adapter_boundary","role":"log","schema_version":"1.0","sha256":"d8974d5fc1c49e0e71d0d0f2cbef75bd9a2c64d862e753aa74e44836d0143ebc","size_bytes":3069,"tokens":["EVIDENCE_PATH_PROOFS_OK"]}`  
* `DOC_DELTA_PRESENT_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"epic034.pr04.doc_deltas","discovered_physical_path":"audit/docdeltas/hde-epic034_doc_deltas.md","epic_id":"HDE-EPIC034","notes":"EPIC034 PR-04 current-epic doc-delta surface records no PF-Canon edit for HDE-FERM007.4 boundary proof","produced_at_utc":"2026-06-19T16:54:48Z","proof_anchor":"audit/docdeltas/hde-epic034_doc_deltas.md.path_proof.txt","record_type":"epic034_pr04_doc_delta","role":"snapshot","schema_version":"1.0","sha256":"6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d","size_bytes":2003,"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]}`  
* `JSON_CANONICAL_CHECK_OK`  
  * PR Artifacts → Diff → `+{"artifact_key":"canonical_json.check_log","discovered_physical_path":"audit/gates/canonical_json/json_canonical_check.log","produced_at_utc":"2026-06-19T16:58:17Z","proof_anchor":"audit/gates/canonical_json/json_canonical_check.log.path_proof.txt","record_type":"canonical_json_gate_log","role":"log","schema_version":"1.0","sha256":"9293633f62966e292930f6f1c25f9f29668b0d1d11a98d530961d2157cd9144a","size_bytes":7268,"tokens":["JSON_CANONICAL_CHECK_OK"]}`  
  * PR Artifacts → Actions Taken → `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`

B) Evidence artifacts produced or updated

* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  Type: LF-terminated adapter/presenter boundary proof log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `work_item=W-003`  
  * `table_driven_boundary_taxonomy=applied to analyzer-owned categories for W-003`  
  * `taxonomy_missing_category_posture=none`  
    sha256: `55a55a37eda1697b3250c42dbd9612980608afaa639798dc6e89656de25b28a9`  
* Path: `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
  * `size_bytes: 17991`  
  * `produced_at_utc: 2026-06-19T07:51:20Z`  
    sha256: `55a55a37eda1697b3250c42dbd9612980608afaa639798dc6e89656de25b28a9`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log`  
  Type: LF-terminated PR-scoped boundary check log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `scope=HDE-EPIC034 PR-04 boundary check for W-003 / HDE-FERM007.4`  
  * `[table_driven_boundary_taxonomy_applied] status=PASS`  
  * `[no_required_taxonomy_group_silently_skipped] status=PASS`  
    sha256: `d8974d5fc1c49e0e71d0d0f2cbef75bd9a2c64d862e753aa74e44836d0143ebc`  
* Path: `audit/qa/hde-epic034/pr-04/boundary_check.log.path_proof.txt`  
  Type: Path proof  
  Key proof facts copied verbatim from PR Artifacts:  
  * `path: audit/qa/hde-epic034/pr-04/boundary_check.log`  
  * `size_bytes: 3069`  
  * `produced_at_utc: 2026-06-19T07:51:20Z`  
    sha256: `d8974d5fc1c49e0e71d0d0f2cbef75bd9a2c64d862e753aa74e44836d0143ebc`  
* Path: `docs/evidence/INDEX.json`  
  Type: Human Evidence Index  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.human_index"`  
  * `"discovered_physical_path":"docs/evidence/INDEX.json"`  
  * `"role":"snapshot"`  
    sha256: `148a371f9e19f5ddaf54e62fb010e30785ede304c887025466ca1d1973afa52b`  
* Path: `artifacts/evidence_index.jsonl`  
  Type: Machine Evidence Mirror  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"index.machine_mirror"`  
  * `"discovered_physical_path":"artifacts/evidence_index.jsonl"`  
  * `"role":"self_record"`  
    sha256: `85c777e6e125b034d3483b4409b3742f747d91d336dd81d4a202df91c9422d20`  
* Path: `audit/docdeltas/hde-epic034_doc_deltas.md`  
  Type: Current-epic doc-delta surface  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"epic034.pr04.doc_deltas"`  
  * `"record_type":"epic034_pr04_doc_delta"`  
  * `"tokens":["DOC_DELTA_PRESENT_OK","EVIDENCE_PATH_PROOFS_OK"]`  
    sha256: `6e411bd697f1bfbe6baf70747be07b09d86d316647a92b2c269ee921aa22f34d`  
* Path: `audit/gates/canonical_json/json_canonical_check.log`  
  Type: Canonical JSON check log  
  Key proof facts copied verbatim from PR Artifacts:  
  * `"artifact_key":"canonical_json.check_log"`  
  * `"record_type":"canonical_json_gate_log"`  
  * `"tokens":["JSON_CANONICAL_CHECK_OK"]`  
    sha256: `9293633f62966e292930f6f1c25f9f29668b0d1d11a98d530961d2157cd9144a`

C) Test/CI proof

* Job or test name: `python -m pip install -r requirements-dev.txt`  
  Pass indicator copied verbatim: `✅ python -m pip install -r requirements-dev.txt`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest --version`  
  Pass indicator copied verbatim: `✅ python -m pytest --version`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py -q`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rows_are_analyzer_owned tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rendering_does_not_relabel_negative_groups_as_current_pass -q`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rows_are_analyzer_owned tests/evidence/test_hdapi_v2_contract_inventory.py::test_epic034_w003_taxonomy_rendering_does_not_relabel_negative_groups_as_current_pass -q`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_hdapi_v2_contract_inventory.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/update_evidence_index.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/validate_evidence_paths.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_mirror_schema.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `ci/checks/check_evidence_index_hash.sh`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/check_lf_endings.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/run_canonical_json_gate.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/run_canonical_json_gate.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `python tools/evidence/orientation_demo.py --check`  
  Pass indicator copied verbatim: `✅ SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing  
* Job or test name: `git diff --check`  
  Pass indicator copied verbatim: `✅ git diff --check`  
  Where it appears in PR Artifacts: PR Artifacts → Testing

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

Doc Deltas: None (no PF-Canon inconsistencies or new doc requirements found)

PF09 Impact Summary

1. PF09 task ID: HDE-FERM007  
   PF09 subtask ID(s): HDE-FERM007.4  
   Current status if evidenced: Task status: Not done; Subtask status: Not done  
   Status action: No status change recommended  
   Evidence pointer(s): PR Artifacts → Diff → `+[table_driven_boundary_taxonomy_applied] status=PASS`  
   Linked Findings item(s): F-004; F-007; F-009; F-010; F-011; F-012; F-013; F-014  
   Linked CHG item(s), if any: CHG-001; CHG-002; CHG-003; CHG-004; CHG-005

Doc Delta Detection Workflow

CHG-001  
Change claim type: workflow steps  
Change claim: W-003 adds table-driven boundary taxonomy and invariant coverage for the required HDE-FERM007.4 boundary categories.  
Evidence pointer: PR Artifacts → Diff → `+table_driven_boundary_taxonomy=applied to analyzer-owned categories for W-003`  
Canon basis: CANON ALIGNED

CHG-002  
Change claim type: evidence posture  
Change claim: Taxonomy rows now distinguish required case classifications from current analyzer classification and current verdict.  
Evidence pointer: PR Artifacts → Diff → `+boundary_taxonomy group=presenter_bypass_paths finding_category=presenter_provenance required_case_classifications=["forbidden","unknown / fail-closed"] current_classification=allowed current_verdict=PASS coverage_status=covered_by_w003_invariant_suite scope=in_scope`  
Canon basis: CANON ALIGNED

CHG-003  
Change claim type: behavior or output  
Change claim: Presenter-bypass analysis now classifies raw public response payloads, `Response(...)`, `make_response(...)`, and assigned unpresented payloads as presenter-bypass findings.  
Evidence pointer: PR Artifacts → Actions Taken → `Hardened presenter-bypass analysis so raw string/bytes payloads, Response(...)/make_response(...) payloads, and assigned unpresented payloads are classified as presenter-bypass findings instead of falling through to unresolved/unknown provenance.`  
Canon basis: CANON ALIGNED

CHG-004  
Change claim type: governed paths or artifact families  
Change claim: W-003 regenerates the existing PR-04 boundary proof and boundary check evidence under existing governed artifact paths with path proofs and index/mirror updates.  
Evidence pointer: PR Artifacts → Diff → `+work_item=W-003`  
Canon basis: CANON ALIGNED

CHG-005  
Change claim type: PF09 status-impact requirement  
Change claim: W-003 contributes to HDE-FERM007.4 remediation but does not support a PF09 status change yet because W-004 and W-005 remain.  
Evidence pointer: Approved Plan → Work Item W-005 → `* Dependencies: W-001 through W-004 complete.`  
Canon basis: CANON ALIGNED

\<eof\>