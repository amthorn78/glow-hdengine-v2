# 0\) Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v2.0.2

**Status:** Canon

**Effective date:** 2026-08-26

**Last Update Gate:** Token retirement

**Invocation tag:** INV-f2ac55d77ce9aacc

---

## Purpose & scope \[Required−Now\]

### Purpose

PF27 is the canonical home for reusable plan, runbook, review, and closeout templates used across Glow, including the HDE workstream. It defines the structure and template-level controls required to make derived artifacts complete, reviewable, portable, executable where execution is in scope, and aligned with the applicable canon.

PF27 governs template requirements. It does not own the implementation facts, technical contracts, project state, or acceptance semantics that a completed artifact records.

### Governed artifacts

PF27 governs the required structure of these artifact types:

- Live QA Plan  
- HDE-EPIC-Plan  
- Ops Task Record  
- Epic Remediation Plan  
- Remediation Implementation Guide  
- Remediation Review Record  
- Audit Analysis Record  
- Implementation Closeout Report  
- QA Pass Review Record  
- Final QA Closeout Review \+ QA RCA  
- Epic Closure Review \+ Retrospective  
- Ops Task Final Review Record

A derived artifact is governed by the PF27 template for its declared artifact type, the applicable cross-template rules in PF27, and any controlling source with higher authority. Requirements from one PF27 template MUST NOT be imported into another artifact type unless PF27 or a more authoritative source explicitly requires that reuse.

### In scope

PF27 governs:

- required headings, fields, front matter, placeholders, approval markers, and structural blocks;  
- the placement and separation of implementation work, OPS work, QA planning, QA execution, review, and closeout content;  
- artifact-level scope statements, exclusions, nonclaims, dependencies, decision points, and completion posture;  
- canon precedence and titles-only source routing;  
- portability and the treatment of non-PF provenance;  
- repository-locus validation, file-minting posture, and protection against invented paths or second homes;  
- exact treatment of known configuration and environment-variable names when a template records them;  
- rails, determinism, evidence-root, check-block, and PASS/FAIL structure where governed evidence is required;  
- classification and routing of unknowns, discovery work, deferrals, and open-rails work;  
- secret-safe planning and evidence boundaries;  
- review guards that distinguish material truth, proof, scope, authority, safety, acceptance, phase, and evidence-identity defects from presentation-only issues; and  
- placeholder, omission, and truncation-safe syntax for plans and runbooks.

PF27 MAY require a derived artifact to identify, preserve, or cite a fact governed elsewhere. That requirement does not transfer ownership of the fact to PF27. The owning canon, current approved source, or validated repository evidence remains controlling for the fact itself.

### Artifact execution boundary

PF27 defines where and how a derived artifact records project-specific content. It does not supply that content by default.

- Epic Plans and initial Implementation Plans define intended work, boundaries, dependencies, and proof obligations. They MUST NOT become step-by-step Live QA runbooks.  
- Live QA Plans and other runbooks MAY be step-executable when their template requires explicit directives, evidence outputs, and PASS/FAIL predicates.  
- A Live QA Plan that produces governed evidence MUST use a stable epic-scoped QA root with check-scoped destinations. It MUST NOT introduce a per-run root, timestamped run directory, or operator-selected fresh root as a canonical evidence surface.  
- Review templates evaluate an existing artifact or evidence set. They MUST NOT silently become authoring or execution templates.  
- OPS templates describe authorized, bounded external work. They MUST keep PO-only actions separate from repository work and MUST NOT assign privileged external execution to automated agents.  
- Closeout and retrospective templates record supported outcomes and unresolved boundaries. They MUST NOT create implementation, QA, OPS, or status claims that the reviewed evidence does not support.

### Reality Audits consultation boundary

Reality Audits are closed-epic snapshots. They provide planning-time repository context, not in-flight PR truth.

- Epic planning and QA planning that drafts, reviews, or approves a Live QA Plan MUST consult Reality Audits.  
- In those planning contexts, Reality Audits MAY support component-boundary, repository-locus, and existence framing.  
- Consultation is read-only. Reality Audit updates remain PO-only and MUST NOT become plan deliverables, QA outputs, required checks, acceptance tokens, or acceptance conditions.  
- Reality Audits MUST NOT be consulted for PR analysis, including PR review, remediation review, or diff-first approval. PR analysis MUST use the PR under review, current repository reality, and the owning PF canon homes.  
- If a Reality Audit conflicts with PF canon during planning, the artifact MUST record a Tracked Issue that identifies the Reality Audit claim, the conflicting canon claim, and the affected epic or surface. It MUST classify the issue tentatively as `canon defect`, `implementation drift`, or `necessary reality shift`.  
- The conflict MUST NOT be resolved by assumption. The Product Owner determines whether resolution requires a canon correction, implementation remediation, or a formal exception with later canon follow-up.  
- Epic Plans SHOULD include a concise `PF23 Anchors` subsection that names the consulted components and the repository loci relevant to the plan. This subsection is traceability only and MUST NOT duplicate the Reality Audit.

### Portability and provenance

Derived artifacts MUST remain executable without requiring access to unstated external attachments.

- A remediation guide MAY list non-PF sources under `Evidence inventory reviewed (non-PF)` for provenance.  
- Every non-PF input listed only for provenance MUST be labeled `provenance only; not required to execute`.  
- If a non-PF fact is required for execution, the artifact MUST embed the necessary fact in `Observed Evidence Snapshot` as a short exact quote or precise paraphrase.  
- If a non-PF observation controls a branch, the artifact MUST state the exact observation to detect, the decision rule, and the lowercase output path and filename where the observation will be recorded.  
- Downstream implementation prompts MUST be self-contained. They MUST NOT require an executor to open a planning audit, inventory, or other attachment to discover an operative fact.

### Exact technical facts and secret safety

When a plan depends on infrastructure, configuration, environment, route, or authentication facts, it MUST preserve the exact spelling and execution context established by the owning source. Known facts MUST NOT be replaced with `OPEN`, `TBD`, or a generic placeholder.

For HumanDesignAPI planning, apply these template-level rules without treating PF27 as the owner of the underlying vendor contract:

| Planning concern | Required treatment |
| :---- | :---- |
| Base URL key | Use `HD_API_BASE_URL`. Use `HDAPI_BASE_URL` only when explicitly identified as deprecated drift, observed legacy state, or temporary compatibility notation. |
| Active resource paths | Use version-neutral resource paths such as `charts`, `charts/simple`, and `charts/coordinates`. The configured base URL owns the API-version boundary. |
| Version literals | Do not use `/v1` or `/v2` as active route-construction inputs. A version literal MAY appear only when classified as historical evidence, an artifact-family name, non-runtime provenance, a configurable-version test input, or a legacy route-family label. |
| Authentication selection | Describe authentication as contract-driven or route-metadata-driven. Do not infer it from `/v1` or `/v2` string inspection or from an evidence-family name. |
| Secret keys | Preserve `HD_API_KEY` and `GEO_API_KEY` when those keys are in scope. Keep environment secret keys distinct from outbound header names. |
| Outbound headers | When the distinction is material, identify current chart-style authentication as `Authorization: Bearer`, preserved legacy BodyGraph-style authentication as `HD-Api-Key`, and geocoding authentication as `HD-Geocode-Key`. Values MUST be redacted. |
| Secret handling | Do not record raw secrets, bearer tokens, API keys, private payload bodies, or unredacted credential material. |

If an exact configuration or environment fact is unknown but safely discoverable, the plan MUST route bounded discovery or an authorized OPS change. It MUST NOT invent, silently normalize, or defer the fact solely because it is unknown.

### Repository loci and file minting

A derived artifact MUST NOT assert an existing repository path, module home, command, component, test, helper, artifact family, or uniqueness claim without a validated basis.

Use exactly one of these source postures for each asserted existing locus:

| Source posture | Required treatment |
| :---- | :---- |
| Canon-cited | Cite the owning PF title and the precise stable locator that establishes the locus. |
| Observed Evidence (Codex Audit) | Embed a short quote or precise observation and bound the claim to the repository state actually inspected. |
| CA vetted | Embed the quoted repository-inspection command and its output in `Observed Evidence Snapshot`. |
| IG Approved | Embed the exact locus quoted from the Implementation Guide Inventory or other approved Implementation Guide source. |
| Unknown pending discovery | Mark the locus as unknown and require a bounded repository-discovery step before implementation relies on it. This is not a validated existing-locus claim. |

Observed repository evidence MAY support existing-locus, component, helper, test, and artifact-family claims. It does not by itself prove acceptance-token satisfaction, QA PASS, OPS completion, phased HDE Build Checklist status, epic closure, live vendor truth, external-system truth, secret validity, or canon authority.

- A Codex-facing prompt MAY include embedded observed repository context, but it MUST direct Codex to verify current repository reality before editing or relying on the locus.  
- If observed evidence is ambiguous, stale after later changes, or conflicts with HDE Build Notes or owning canon, the artifact MUST record the conflict or freshness limit instead of presenting the observation as settled truth.  
- Audit provenance MAY explain why work exists, identify risk, guide inspection, or support a Tracked Issue, ADR stub, PF mapping, or proof obligation. It MUST NOT become operative PR or OPS instruction, command authority, acceptance authority, proof of completion, proof of current repository state without validation, privileged-action authority, or a source of secrets or external state.  
- Reviewers MUST NOT block an artifact merely because it includes audit provenance. A blocker is valid only when the artifact converts that provenance into execution or proof authority, or presents it as current truth without the required validation.

File minting is allowed within established governed homes.

- A plan that mints a file or governed evidence output MUST name its exact path and filename.  
- Primary governed evidence outputs MUST use concrete filenames. Wildcards and implied output paths are not sufficient. A high-churn output family MUST identify a stable manifest path and bundling rule.  
- A plan MUST NOT create a new top-level root or a second home for an existing artifact unless an ADR explicitly authorizes the home and the Product Owner approves it.  
- Multiple established evidence roots are not drift by themselves. For evidence, `single home` means one authoritative catalog or index with canonical path bindings, not one physical directory.  
- A permitted dual-home pattern MUST identify both paths, the authoritative path, the pointer-only path, and the refresh rule that keeps the pointer synchronized.  
- If `scripts/`, `tools/`, or another auxiliary root is treated as governed evidence, the plan MUST bind it to an evidence family owned by HDE Schemas and Artifacts. Otherwise, it MUST classify the output as non-governed tooling output and exclude it from acceptance claims.

### **Exact-source acceptance evidence and legacy-token posture**

PF27-derived artifacts MUST use exact-source evidence and scoped decisions as the primary acceptance-traceability model. As applicable to the artifact and claim, use existing PF, ADR, epic, task, acceptance-criterion, test, PR, commit, workflow-run, schema, manifest, index, path-proof, attestation, and governed-artifact identifiers.

Acceptance tokens are legacy-compatible, historical, optional indexing metadata. New QA acceptance tokens MUST NOT be created by default. A complete token roster, per-step token declaration, token claim, or token-evidence matrix MUST NOT be required when no active scoped token use exists, and the absence of those token surfaces MUST NOT block otherwise sufficient exact-source evidence.

Existing token IDs and historical token evidence MUST remain attributable to their original candidate, scope, and decision. They MUST NOT be reinterpreted, reassigned, reissued, or deleted from historical records. Token fields MAY remain when an owning schema requires backward-compatible fields; empty arrays remain valid where that schema supports them. A future artifact MAY opt into one bounded token or equivalent cross-reference only when existing governed identifiers cannot provide the required traceability. That exception does not reactivate a universal token system.

Evidence requirements MUST be proportional to the changed surfaces, governing requirements, and risk. A PF27-derived artifact MUST NOT duplicate information that GitHub or an existing governed repository artifact records reliably, and MUST NOT create a replacement token database, universal acceptance form, or semantic-duplicate matrix. It MUST reference the authoritative record and add only the scope, decision, limitation, or relationship not already carried there.

The following states remain separate:

1. **Repository fact:** an exact commit or file exists on the identified ref.  
2. **CI result:** the applicable workflow checks completed for an exact SHA.  
3. **QA decision:** an authorized QA verdict applies to an exact candidate and scope.  
4. **Operator or role acceptance:** an authorized decision-maker accepted an exact change or deliverable within a stated scope.  
5. **Completion or closure:** the governing completion requirements were satisfied and the authorized lifecycle status was moved.

A derived artifact MUST NOT collapse these states. Landing a commit on `main`, merging a PR, recording a workflow PASS, or preserving a historical token claim does not independently establish QA PASS, acceptance, PF09 completion, OPS completion, deployment, release readiness, epic closure, or production readiness. A current canonical artifact on `main` governs its declared artifact-content lane while remaining separate from implementation conformance, QA acceptance, and closure.

Before substantive repository-dependent work, the artifact author MUST resolve the current relevant ref, inspect the current authoritative files, and avoid reliance on memory, an earlier session, an old token registry, or a prior summary. Before issuing an acceptance or completion claim, the claimant MUST recheck the candidate SHA, relevant files, applicable workflow result, evidence integrity, and decision scope. If the candidate moved, the earlier result remains historical until the applicable validation is rerun or an explicit scope-equivalence check proves that no relevant requirement, input, dependency, implementation surface, test, configuration, or evidence artifact changed.

A documentation-only label or filename similarity is not scope-equivalence proof. A canon, requirement, schema, public-contract, or interpretation change requires renewed downstream-impact and conformance analysis even when runtime bytes are unchanged.

A Git commit SHA identifies an exact repository state; it does not prove CI, QA, acceptance, artifact integrity, or closure. PR identities, workflow-run identities, SHA-256 digests, manifests, evidence indexes, mirrors, path proofs, attestations, and authorized decision records prove different facts and remain layered. This token-posture change does not weaken or replace existing source-provenance, deterministic-validation, evidence-integrity, QA, OPS, acceptance, or closure requirements.

If exact-source repository metadata or governed evidence required for a claim is unavailable, the affected claim MUST fail closed as unavailable or blocked. The artifact MUST NOT reconstruct confidence through invented tokens or reconstructed claims.

### Unknowns, discovery, deferral, and open rails

Unknown facts MUST be classified as exactly one of:

- `discoverable by OPS`  
- `discoverable by PR`  
- `discoverable by QA`  
- `requires PO or Thoth decision`  
- `requires PF10 live rule`  
- `requires permanent canon update before safe execution`  
- `unsafe to discover now`  
- `out of scope`  
- `phase drift`  
- `valid deferral`

Deferral is exception-only. A plan MUST NOT defer in-scope phased HDE Build Checklist work merely because an operational, infrastructure, vendor, credential, environment, open-rails, or OPS-root fact is unknown when that fact can be discovered safely.

- A bounded OPS discovery task MUST state the exact fact to discover, why it matters, the owner, whether secrets are involved, what may and may not be recorded, the downstream dependency, and the secret-safe evidence or summary that resolves the unknown.  
- Valid deferral requires an explicit basis in approved scope, phase drift, a missing PO or Thoth decision, an unadmitted acceptance token, unauthorized mutation or live execution, unsafe secret handling, an unmet prerequisite, unsafe discovery, required invention, or an unresolved canon conflict that PF10 cannot bridge.  
- Implementation Plans, QA Plans, and remediation guides MAY include bounded open-rails work when closed rails cannot truthfully establish the required live fact.  
- Open-rails work MUST be bounded, Product Owner-authorized where required, non-destructive unless explicitly approved, secret-safe, and evidence-recorded. It MUST NOT expose secrets, probe a vendor without a defined limit, expand a public surface, create a new HTTP home, mint an acceptance token, or treat a narrow smoke as full conformance.  
- An open-rails failure MUST be classified before it is treated as a product failure. Relevant classes include credentials, configuration, vendor account or tier, endpoint availability, vendor contract, request shaping, response mapping, infrastructure, rate limit, external outage, implementation, and QA-plan expectation.  
- OPS discovery and OPS open-rails work MAY support implementation or QA. They do not by themselves prove QA PASS, acceptance-token satisfaction, HDE Build Checklist Done status, OPS completion beyond the bounded task, or epic closure.

### Database-role evidence boundary

When database-role planning is in scope, the artifact MUST keep these states distinct:

| State | Meaning |
| :---- | :---- |
| Observed live role state | Roles and attributes returned by bounded live inspection. |
| Target-role absence | The operation's selected dedicated identities are not present before provisioning. |
| Desired security posture | Role names, privilege matrices, tests, schemas, or predicates that describe an intended or acceptable result. |
| Authorized mutable precursor | Bounded database changes approved before a later read-only capture can run. |
| Direct capture posture | Authorization-bound, direct-only, read-only observation with no SQL writes. |
| Provisioned bounded posture | Role and privilege outcomes directly supported by retained operational evidence. |
| Complete role architecture | The separately governed application, writer, migration, owner, administration, deployment, rotation, recovery, and incident-handling model. |

Repository names, fixtures, schema fields, acceptance predicates, PF wording, and planned architecture do not prove that a corresponding live role exists.

Before a plan binds a one-attempt database authorization, it MUST require:

- inspection of the live role roster and effective privileges;  
- determination of whether an existing identity satisfies the exact operational predicate;  
- Product Owner authorization for every required mutable precursor;  
- completion and verification of the precursor before authorization bytes are constructed;  
- retention of exact SQL or an authoritative equivalent when later claims depend on the complete grant model;  
- pre-state and post-state evidence when the artifact claims that existing roles remained unchanged; and  
- exclusion of credential values from retained evidence.

### Template-safe placeholders and omission syntax

Allowed placeholder markers are:

- `[REQUIRED]`  
- `[REQUIRED−NOW]`  
- `[OPTIONAL]`  
- `<PLACEHOLDER>`  
- `<PLACEHOLDER_ONE_PER_LINE>`

Plain `TBD`, `TODO`, `???`, `FIXME`, and free-text instructions such as `fill in later` are prohibited. `[TBD]` is allowed only when it is decision-bounded and appears under `Open Decisions` in the Remediation Implementation Guide template.

Outside inline code spans that discuss a literal token, plans and runbooks MUST NOT contain:

- the Unicode ellipsis character U+2026;  
- three consecutive period characters; or  
- fenced code blocks.

If a prohibited ellipsis form appears in a relied-on passage, the author MUST treat the passage as potentially incomplete, retrieve the complete source, and redo dependent work. If the token is confirmed as source text, replace it with one of these approved markers:

- `[OMITTED]`  
- `[OMITTED: short reason]`  
- `[SNIP: n lines omitted]`  
- `[LIST CONTINUES]`  
- `[REPEAT BLOCK]`

An ellipsis form MAY remain inside an inline code span only when it is a literal code token under discussion and cannot be represented safely another way. If a longer literal example requires that form, place the example in a repository or governed evidence file and reference its exact path instead of embedding it in the plan.

Any prohibited ellipsis form or fenced code block in a plan or QA document is a mechanical blocker until corrected.

### Out of scope and source routing

PF27 does not own the following subjects:

| Subject | Controlling source or boundary |
| :---- | :---- |
| Project-specific steps, commands, decisions, expected outputs, and factual inputs | The approved plan scope, current source artifacts, owning canon, current development board, and validated repository or operational evidence. PF27 controls only where and how the artifact records them. |
| Architecture and component ownership | HDE Architecture. |
| Acceptance-token registry and token semantics | HDE Governance. |
| Transport, wire-byte, CLI, API, and vendor contracts | HDE CLI/API/Vendor Reference. |
| Infrastructure providers, services, environments, and runtime topology | Glow Infrastructure. |
| Current epic records, card state, owners, WIP, dependencies, and evidence links | The current development board. |
| Phased build scope and checklist status | The applicable phased HDE Build Checklist document or documents, PF09.1 through PF09.7. |
| Historical phased-epic and closure context | HDE Phased Epics. This source is historical unless an operator explicitly invokes it for historical context. |
| Governed schemas, manifests, catalogs, and artifact paths | HDE Schemas and Artifacts. |
| QA execution semantics, status vocabulary, and standard playbooks | Glow QA Guide. |
| Living deltas and temporary exact-scope supersession | HDE Build Notes. |
| Current checked-in implementation state | The repository state actually inspected. Static repository evidence does not prove runtime, deployment, external-system, secret, QA, OPS, board, or approval state. |

PF27 MUST NOT duplicate canonical bytes, token lists, schemas, or technical contracts from these owners. It MUST route to them by title and reproduce only the minimum exact facts needed to make a derived artifact self-contained and executable.

### Canon precedence for template use

Every template and derived artifact MUST include this precedence rule:

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

When a derived artifact relies on a formally approved bounded Product Owner rescope, it MUST identify the exact approved decision, any work transferred to a later PR, the preserved boundaries, the preserved nonclaims, and the PF drain candidates.

### Primary audience

- Authors: the Product Owner, QA agents, implementation-planning agents, and other authorized agents that create artifacts from PF27 templates.  
- Reviewers: the Product Owner, Lead Dev, QA reviewers, and other authorized reviewers responsible for scope, executability, canon alignment, evidence posture, and material blockers.

# A) Glow Plan and Runbook Templates

PF27 is the project-wide home for Glow plan and runbook template shape. The existing HDE-specific templates remain HDE-specific. Use the General Implementation Plan template only when no more-specific PF27 template controls the artifact class. `PF06-Canon-Epic-Process-Guide` retains process sequencing, roles, and approval ownership; this selection does not copy that process body.

## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC\#\#\#  
Plan type: Live QA Plan / Runbook  
Execution venue: Codespaces (preferred) | Other: \_\_\_\_ Approval sentinel: `ASK OK?`

Venue-specific claim: \<CLAIM\> | NOT CLAIMED | NOT APPLICABLE

Why venue can affect the result: \<RATIONALE\> | NOT APPLICABLE

Required venue evidence: \<GOVERNED\_EVIDENCE\> | NOT APPLICABLE

Effect of missing venue evidence: \<EFFECT\> | NOT APPLICABLE

The execution-venue field is descriptive and records an intended or preferred operator surface unless the four venue-materiality fields establish a venue-specific proof contract and explain why venue can affect the result.  
Target environment: prod | dev | other: \_\_\_\_ (explicit)  
Plan revision: r\#  
Date (UTC): YYYY-MM-DD  
Operators (names-only): PO, IA, (optional) QA agent, (optional) Codex

“Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.”

When a formally approved bounded Product Owner rescope applies, identify the exact approved decision, any transferred later-PR work, the preserved boundaries, the preserved nonclaims, and the PF drain candidates.

#### **Canon set (explicit; stable references only)**

Canon set (titles-only, names-only, no version numbers in prose):

* PF10 — HDE-Build Notes (relevant addenda: list addendum numbers and titles)  
    
* PF04 — HDE-Governance, §\<SECTION\> (acceptance and strict-claim invariants; legacy token interpretation only when applicable)  
    
* PF06 — Epic Process Guide, §0.4.1 (Discovery \+ QA RCA/Doc Delta)  
    
* HDE Build Checklist phase document: `<exact current in-document PF09.1 through PF09.7 title>`, `<exact task or subtask ID and heading>` (evidence-index refresh and path-proof regeneration in close-pack, when applicable)  
    
* PF12 — HDE Schemas & Artifacts, §\<SECTION\> (evidence index refresh flow: canonical filenames \+ refresh order)  
    
* PF19 — Glow QA Guide, §\<SECTION\> (rails, evidence, step logs)  
    
* PF27 — Canon Plan Templates, §\<SECTION\> (template obligations)

Note: PF20 may be cited only for historical record context, never as a source of requirements.

### **Scope statement**

This plan evaluates the following in-scope surfaces / checks:

* D0 \<SURFACE\_OR\_CHECK\_NAME\>  
    
* D1 \<SURFACE\_OR\_CHECK\_NAME\>  
    
* D2 \<SURFACE\_OR\_CHECK\_NAME\>  
    
* D3 \<SURFACE\_OR\_CHECK\_NAME\>  
    
* \[LIST CONTINUES\]

This plan explicitly excludes:

* \<SURFACE\_OR\_CHECK\_NAME\>  
    
* \[LIST CONTINUES\]

#### PF10 overrides / conflicts (if any)

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

* PF10 Addendum \<\#\> — → what it changes for this runbook → impacted PF references

---

### **PF23 anchors**

**Planning-time consult for Live QA planning (normative).**

* PF23 MUST be consulted during QA planning. Drafting, reviewing, or approving a Live QA Plan MUST consult PF23 as a primary input for repo-reality context and existence or locus framing.  
    
* If a plan references any repo-resident locus (paths, endpoints, routes, scripts, checks, test identifiers, environment variable names treated as already-existing, or fixed output locations treated as already-existing), the reviewer SHOULD consult PF23 before approval to reduce drift and avoid fabricated or stale locus assumptions.  
    
* Consultation is read-only. PF23 maintenance remains a manual PO operation. Live QA Plans MUST NOT include any required deliverable whose purpose is “PF23 consult capture,” “PF23 note,” or similar.  
    
* Live QA Plans MUST NOT instruct the operator to run repo commands in order to “prove PF23 consult.”  
    
* Conflict posture: if PF23’s current record appears inconsistent with other allowed repo-reality sources, treat this as a reality ambiguity and MUST NOT guess or assert a reconciled locus as fact inside the plan.

**Trace anchor (optional; plan text only).**

* If a trace anchor is desired, it lives in the plan text only (names-only).  
    
* A plan MAY include a single PF23 Anchors note (components consulted \+ loci touched), but it is informational only and MUST NOT appear as a required check or required evidence output.

**Rule (normative): PF23 consult is not an acceptance token.**

* Plans and implementations MUST NOT mint, claim, or reference `REALITY_AUDIT_OK` (or any similar “PF23 consult completion” acceptance token) unless and until Governance registers such a token in the token registry.

---

### Environment and rails posture

#### Determinism pins (canonical pins only)

When producing governed bytes (evidence artifacts, canonical JSON, hash inputs), use:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

**Rule (normative):**

* Do not add new “pins” (example: PYTHONHASHSEED) as a plan-approval or execution requirement.  
* If ordering nondeterminism exists, fix it by explicit normalization (sorting keys/lists, stable ordering) in the step/tool, not by adding pins.

#### Rails posture (explicit)

Default rails for this runbook (fill values):

* SAFE\_MODE=\_\_  
* ALLOW\_NETWORK=\_\_  
* APP\_ENV=\_\_

If rails change by check, list it (names-only):

* \<check\_id\> → rails change → why change is needed → what evidence it produces

  #### **VCS mutation and exact-source identity boundary (hard)**

Live QA Plans exist to execute checks and produce evidence. They MUST NOT instruct branch creation, checkout, commit, push, merge, rebase, PR creation, or another VCS mutation as part of QA execution.

The Product Owner retains direct-to-`main` authority. This section does not grant an agent direct-main authority. An agent direct-main mutation requires an explicit current operator instruction covering the exact change.

A plan MAY include read-only repository-identity capture when needed to bind execution evidence to the tested source. The governed execution or review record MUST identify the exact repository and candidate SHA for any QA verdict or acceptance claim.

When a PR is used:

* record or directly bind the PR number and exact reviewed head SHA;  
* require relied-upon CI results to identify that same head SHA;  
* retain review findings and resolutions in the PR or a governed linked artifact;  
* distinguish the base SHA, reviewed head SHA, merge SHA, and post-merge `main` SHA as applicable; and  
* treat a later push as a new candidate unless rerun evidence or an explicit comparison proves the relevant reviewed and tested scope unchanged.

When an explicitly authorized direct-main route is used:

* identify the exact post-write SHA;  
* bind the reviewed diff;  
* identify the applicable push-triggered CI result;  
* preserve the current applicability-classifier result when it validly selects a reduced lane set; and  
* describe pending or failing push CI as pending or failed validation rather than CI-green or accepted.

Read-only identity capture is evidence metadata, not a product-behavior PASS predicate. A branch name, commit SHA, PR identity, merge fact, or presence on `main` MUST NOT establish QA PASS, acceptance, completion, or closure by itself.

A QA verdict MUST identify the exact candidate, governing scope, relied-upon checks or governed evidence, applicable results and failures, decision-maker, decision time, and limitations. A verdict for a later candidate requires either rerunning the applicable QA or explicit scope-equivalence proof. Filename similarity, an unchanged legacy token, an agent summary, or an unsupported `docs only` statement is not equivalence proof.

If exact candidate identity required for a QA or acceptance claim cannot be established, the artifact MUST record an identity or evidence blocker and MUST NOT issue the affected verdict. It MUST NOT classify missing identity metadata as product-behavior failure.

---

### PO inputs needed

List all required external inputs by name only (never store secret values in plan artifacts).

Examples:

* HDE\_BASE\_URL (if needed)  
* HDE\_PROD\_BASE\_URL (if needed)  
* PORT (if needed)

Any auth/header inputs only as optional execution inputs where permitted by canon:

* AUTH\_HEADER\_NAME (names-only)  
* AUTH\_HEADER\_VALUE (never persisted; never logged; presence-only is allowed in snapshots)

**Rule (normative):**

* If a required input is missing at runtime, classify the affected check as TOOLING\_BLOCKED (do not guess).

---

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Canonical epic QA root MUST be lowercase:

* EPIC\_QA\_ROOT \= `audit/qa/hde-epic<NNN>/`

#### **Check-centric, single-root evidence posture (normative)**

This runbook is written for the checks-only evidence posture:

* Live QA evidence MUST be organized only by **check\_id** under EPIC\_QA\_ROOT as **current-state evidence**.  
    
* Evidence paths MUST be stable across re-runs. Re-running QA MUST NOT change the directory structure by creating a new run root.  
    
* Per-run directory nesting is disallowed. Run-id directories, timestamped directories, and fresh-directory postures are nonconforming.  
    
* Plans, prompts, and reviews MUST NOT introduce, require, or depend on per-run root selection or any operator-set per-run root variable.  
    
* Plan-created deliverables are allowed, but they MUST live under the stable check directory for the relevant **check\_id**. Plans MUST NOT place plan-created outputs under a per-run directory.  
    
* No “latest\_run\_id” pointer files or “run-id as correctness key.”  
    
* Uppercase characters are allowed in filenames. The lowercase naming rail applies to directory segments and to explicitly-lowercase identifiers (for example, `check_id`).  
    
* `run_id` (or `RUN_ID`) is prohibited as an operator input, plan header field, step-log header field, manifest field, or correctness key. If per-execution history is kept, it remains optional and non-canon and MUST NOT introduce a run-id identity requirement.

#### Recommended canonical layout (default for new plans)

Use this layout unless an owning PF document defines a fixed canonical path for a specific artifact family.

* `audit/qa/hde-epic<NNN>/00_meta/`  
  Stable epic-level meta artifacts (current-state).  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/`  
  Current-state evidence for each check.

Within each `checks/<check_id>/`:

* Primary step log (required): `primary.log`  
* Structured report sidecars (optional; but if listed in the plan’s required deliverables, filenames MUST match the produced outputs):  
  * D23 evidence index snapshot contract: `evidence_index_snapshot_contract_report.json` (canonical; replaces plan-listed `snapshot_contract_validation.json`)  
  * Evidence-path binding validation: `evidence_path_binding_validation_report.json` (canonical; replaces plan-listed `binding_validation_report.json`)  
* Captured CLI output snapshots (optional; REQUIRED when stdout/stderr is treated as the proof payload for a check):  
  * Token registry validity checks (e.g., `po-006_token_registry_validity`): `rg_acceptance_map_output.txt`, `rg_registry_output.txt`  
* Supporting artifacts (optional): `tmp_*` files, `.sha256` sidecars where required, etc.

Optional (non-canon) history retention:

* `audit/qa/hde-epic<NNN>/runs/<attempt_label>/<RUN_LOCAL_SUBTREE>/`  
* where `<attempt_label>` is a UTC timestamp label (git-free).  
  * If you keep run-local copies here, they MUST be treated as convenience copies, not canonical acceptance binding surfaces.

#### **Step-log header schema expectations (required; v2)**

New or revised PF27 Live QA step-log headers use `pf27.step_log_header.v2`. Existing v1 evidence remains historical and MUST NOT be silently rewritten.

**Closed status set**

The status is exactly one of `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, or `PARKED`. `WARN` is an annotation or log-body severity, not a terminal outcome. A native runner's skipped result does not map blindly to a governed outcome: authorized pre-execution non-performance is `PARKED`; an unavailable mandatory prerequisite is `TOOLING_BLOCKED`. `NOT RUN` and `DEFERRED` remain artifact-inventory states under the QA planning QoS contract, not step-log statuses.

**Exact status predicates**

* `PASS`: all mandatory prerequisites are established; the intended command or approved proof action reaches its decisive point; every in-scope predicate passes; required evidence is present and trustworthy; the check's `primary.log` is in `evidence_artifacts`; status-specific schema validation passes; `exit_code` is `0`; and any token claims are explicit and governance-valid. A tokenless check may pass with both token arrays empty.  
* `FAIL_BEHAVIOR`: prerequisites and QA tooling are trustworthy, behavior is exercised, and observed product, runtime, or domain behavior violates an explicit in-scope predicate. Do not use it for missing tools, credentials, open-rails authorization, malformed evidence, or an invalid harness.  
* `FAIL_TOOLING`: the QA mechanism, validator, harness, evidence writer, or proof pipeline is present and attempted but malfunctions, violates its contract, or produces untrustworthy evidence. The product or domain predicate remains unproven unless an independent trustworthy proof establishes it.  
* `TOOLING_BLOCKED`: a required check cannot reach the behavior-decisive point because a prerequisite, dependency, approved target, authorization, credential presence, required entrypoint, required environment fact, or safe execution rail is unavailable or unresolved. No product-behavior verdict is permitted.  
* `PARKED`: the check is intentionally not attempted under an explicit scope exclusion, supersession, or authorized deferral recorded before the outcome is known. Record the reason, authority or controlling source, affected acceptance claim, and reactivation condition. `PARKED` is not PASS and cannot satisfy a token or required Human Design predicate.

**Causal precedence**

1. `PARKED` is available only for a pre-existing authorized non-execution decision; attempted execution cannot be hidden by parking.  
2. Invalid or untrustworthy attempted tooling or evidence selects `FAIL_TOOLING`.  
3. Otherwise, a missing mandatory prerequisite that prevents behavior-decisive execution selects `TOOLING_BLOCKED`.  
4. Otherwise, trustworthy execution that proves the behavior predicate false selects `FAIL_BEHAVIOR`.  
5. `PASS` is available only after every mandatory predicate is affirmatively satisfied.

For a rollup, an invalid proof mechanism controls as `FAIL_TOOLING`. An unexecuted mandatory child controls as `TOOLING_BLOCKED` unless a valid approved exclusion applies, in which case the affected acceptance claim remains unsatisfied. A mixed record MUST preserve every child result; its rollup MUST NOT erase a more limiting child state.

**Required v2 keys**

| Key | Contract |
| :---- | :---- |
| `schema_version` | Exact value `pf27.step_log_header.v2`. |
| `timestamp_utc` | Actual finalization time in RFC 3339 UTC form ending in `Z`. |
| `check_id` | Non-empty stable ID matching the plan check. |
| `check_name` | Non-empty name matching the plan check. |
| `status` | One exact value from the five-status set. |
| `status_reason` | Empty string only for `PASS`; non-empty causal explanation for every other status. |
| `command` | Exact executed command sequence; empty only when no command was executed. |
| `command_provenance` | Truthful source of the exact command; `Not executed` only when `command` is empty. |
| `exit_code` | Actual integer when a command ran; `null` only when none ran; `PASS` requires `0`. |
| `evidence_artifacts` | Non-empty array containing the check's own `primary.log` path and every primary artifact relied on. |
| `captured_env` | Actual, secret-safe values for canon-defined environment names relevant to the step; no invented keys. |
| `pf_refs` | Array of exact in-document PF titles only. |
| `intended_tokens` | Explicit array; `[]` is permitted. |
| `claimed_tokens` | Explicit array; `[]` is permitted and values are never inferred. |

The v1 `fail_status` field is retired from v2. `status` is the sole outcome field and `status_reason` carries the cause. Header serialization is UTF-8 compact JSON with lexicographically sorted object keys, no BOM, and exactly one terminating LF. A checked-in JSON Schema SHOULD validate v2 through the PF12-governed schema process.

**Token-claim rules**

* Never populate `claimed_tokens` from prose, `status`, or `intended_tokens`.  
* A non-`PASS` header MUST have `claimed_tokens: []`.  
* Every claimed token MUST also appear in `intended_tokens`.  
* A `PASS` header MAY remain tokenless.  
* When intended and claimed arrays differ on `PASS`, the log body MUST explain the difference.  
* Header validation checks shape and alignment; it does not create token-registry authority or prove a token predicate.

**Template and correction boundaries**

* `captured_env` MUST contain actual values only for canon-defined names. `MODO_*` names are noncanonical and MUST NOT become plan inputs, exports, schema keys, or capture keys. Existing HDE-EPIC025 references remain inert historical placeholders and MUST NOT be copied into new plans.  
* Authors MUST NOT add novel environment variables or CLI switches for QA convenience.  
* `command_provenance` MUST state how the exact executed command was obtained. A bounded execution-time syntax correction is nonblocking only when command identity, proof target, artifact family, PASS/FAIL predicate, and intended output do not change, and the primary log records the exact command, correction class, and provenance.  
* A missing or incorrect header MAY be regenerated as a bounded evidence-capture correction only by preserving the existing `primary.log` body verbatim and recording the correction.  
* One Live QA Plan MUST use one header contract consistently across its check blocks.

**Executable helper boundary**

PF27 contains no inline executable writer. The sole executable locus is `tools/qa/step_log_header.py` after a separately authorized correction. At the pinned repository commit, the checked-in helper is nonconforming with v2: it cites stale PF10 authority, defaults status to `PASS`, emits a reduced key set, and can copy `intended_tokens` into `claimed_tokens` on PASS. The helper is therefore an implementation locus, not executable authority for v2. This template does not edit, validate, test, or approve those bytes.

**Human Design and Magic-10 gate**

When a check protects chart or compatibility correctness, `PASS` requires the exact domain predicate to be exercised. A complete Magic-10 claim requires independent evidence for all ten categories. A harmony-only result cannot satisfy the complete matrix, and any required category that is `PARKED`, `TOOLING_BLOCKED`, affected by `FAIL_TOOLING`, or not exercised prevents the complete claim.

### Mandatory Step‑0 artifacts

> `Step-0A` is reserved for identifier compatibility. PF27 does not currently define a reusable Step-0A contract. Existing artifact-specific or historical Step-0A records do not create that contract. Plans must not invent Step-0A obligations. Any future reusable Step-0A definition requires an explicit PF27 revision and migration decision.

These are execution deliverables and must be mechanically produced.

#### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Purpose: mechanically record repo reality mismatches, missing prerequisites, and canon conflicts as BLOCKERS vs CAVEATS.

**Moon Loop allowed (bounded).**

* A Live QA Plan MAY include a “Moon Loop” clause to allow minimal in-session remediation solely to unblock planned checks that are blocked by trivial prerequisites.  
    
* Moon Loop work MUST be explicitly declared, scoped to the minimum change needed, and captured as evidence (diff/log \+ why \+ which check(s) were unblocked \+ evidence paths) under `audit/qa/<epic-id>/00_meta/delta/`.  
    
* Hard boundary: Moon Loop MUST NOT expand scope into new acceptance surfaces or feature work. If the needed change is not trivially bounded, stop and escalate to a remediation guide.  
    
* Stop condition: If Moon Loop work exceeds a short, bounded threshold (e.g., \>30 minutes or touches multiple subsystems), stop and convert to a remediation guide.

Bounded step-level rerun posture (required when a plan permits one):

* The plan MUST state the exact trigger condition for the rerun and the exact check or checks that may be rerun.  
* The plan MUST state whether rails may change for the rerun and, if so, the exact replacement rails posture for that rerun only.  
* The rerun MUST stay on the same governed step root and the same deliverable family unless the plan explicitly states a narrower reporting-state-only rerun under that same step root.  
* The plan MUST preserve the earlier failed or blocked state in the same governed evidence stream and MUST require a short remediation note that records what changed and why.  
* Missing or overwritten initial failure artifacts (required). If an initial failure artifact, log, hash, timestamp, or result body is overwritten or unavailable by the time remediation begins, the plan, report, or review MUST state that the initial failure artifact is unavailable and MUST NOT reconstruct or invent the missing bytes. The remediation record may rely only on preserved failure signatures, approved sources, current evidence, and a truthful unavailability note.  
* The plan MUST require the rerun evidence to show the final step outcome without widening scope into new acceptance surfaces, new feature work, or a new evidence family.  
* Step-0B precondition remediation (required when applicable). If a later check cannot be interpreted because the required Step-0B doc-delta capture is absent at run time, the plan or review MAY accept an approved precondition remediation only when it runs the approved Step-0B commands, produces the required Step-0B artifacts under the established meta and doc-delta surfaces, reruns the affected check under the approved rails, preserves the earlier blocked or failed state, and records the remediation as an accepted PASS-only deviation. This does not change the affected check’s required deliverables or PASS/FAIL criteria.  
* QA-created harness predicate, evidence-assembly, or proof-metadata defects may be accepted as PASS-only Moon Loop deviations when the product or runtime proof target remains unchanged, the correction stays inside already-scoped QA evidence or harness files, the failure signature is preserved, the remediation note names changed paths and why, rerun PASS is captured in the same evidence stream, and patch or changed-files evidence with hashes is recorded when repo files change. Classify the original defect as planning, harness, or evidence-posture failure, not product behavior failure, when unchanged generator, runtime, or redaction evidence already proved the product predicate.  
* If an executed Moon Loop is broader than a narrow plan example but still remains minimal, auditable, within approved check scope, and does not add new acceptance surfaces, feature work, evidence family, token, or public contract, the review may accept it as a caveat or PASS-only deviation. The review must state why the deviation remained acceptable and must not hide it under PASS.  
* Live QA Moon Loop route boundary (required). Moon Loop correction may repair QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects only when the changed files remain under the approved QA root and do not change product behavior, repo evidence-generator behavior, governed artifact behavior, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems.  
* Non-QA-root remediation route (required). A change to product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction. It MUST be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before it can be treated as the basis for a final PASS-grade QA run. Later QA review MUST cite that routing before accepting the final PASS state. When final PASS relies on non-QA-root governed evidence refresh, the final receipt or review MUST cite the routing receipt, identify the pre-routing failed or blocked receipt when one exists, preserve that pre-routing receipt as context, and distinguish routing proof from PASS proof.

**PO-approved Extended Moon Loop decision record (required only when invoked).**

* **Epic and QA check or hosted-CI run:**  
* **Repository or routed-source anchor:**  
* **Triggering failure, blocker, or safety discovery:**  
* **Unchanged proof objective and PASS or FAIL meaning:**  
* **Allowed causal scope:**  
* **Rails, network, credential, and data-safety posture:**  
* **Authorized action classes:** read-only investigation | code write | external call | PR publication | merge | OPS | deployment | rerun | hosted-CI completion  
* **Completion gate:**  
* **One-time authority and expiry:**  
* **Receipt and routing lineage:**

The decision record MUST cite fresh, explicit Product Owner direction recorded before each corresponding write, external call, publication, or merge. It MUST preserve the original failed, blocked, or pre-routing receipt; each material root-cause finding; the exact changed paths or reviewable diff; canonical generator commands for governed outputs; local regression results; PR, routing, and merge receipts; intermediate hosted-CI failures; the final accepted QA receipt; and the final clean hosted-CI source and run when CI cleanliness is a completion condition.

A prior event, receipt, configuration value, merge, or CI run MUST NOT supply standing or recurring authority. The record does not itself authorize action, enlarge the approved proof target or substantive scope, or relabel non-QA-root remediation as ordinary Moon Loop correction.

**Doc-delta surfaces (required; two-surface pair).**

MUST treat doc-deltas as a two-surface pair:

1. Draft/staging surface under `audit/docdeltas/` (used for the in-flight doc-delta artifact and its evidence binding).  
2. Epic-scoped capture surface at `audit/qa/<epic-id>/00_meta/doc_deltas.md` (used as the stable QA record for the epic).

Naming and binding rules:

* The draft/staging surface MUST use a concrete filename. Placeholders like `audit/docdeltas/<doc-delta>.md` are nonconforming.  
    
* SHOULD standardize the draft filename as: `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase epic-id), unless superseded by a later canon naming rule.  
    
* The Epic Plan’s token↔evidence bindings MUST reference:  
    
  * the draft/staging surface for doc-delta token evidence, and  
      
  * the epic-scoped capture file as the authoritative narrative/record surface.

Canonical output (current-state; epic-level):

* `audit/qa/<epic-id>/00_meta/doc_deltas.md`

Requirements:

* Separate findings into BLOCKERS and CAVEATS with stable IDs.  
* Output “no deltas” when empty.  
* Before emitting “no deltas,” Step-0B MUST determine whether either doc-delta surface already contains generator-owned, evidence-owned, or otherwise proof-bearing content for the epic.  
* Step-0B MUST NOT overwrite generator-owned or previously produced proof-bearing doc-delta surfaces with an empty scaffold, no-deltas template, or reset capture.  
* Step-0B may append, copy, or preserve existing proof-bearing content only when the plan, runbook, or review artifact explicitly instructs that behavior and the resulting evidence keeps the prior proof content auditable.  
* “No deltas” may be emitted only when no proof-bearing doc-delta surface exists for the relevant epic, slice, check, or reviewed evidence stream.  
* If a Step-0B action overwrites or clobbers proof-bearing doc-delta content, classify the issue as a planning, evidence-assembly, or tooling defect, preserve the failed or blocked receipt when available, and route remediation through the approved Moon Loop, PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE path that matches the changed surface.  
* MUST be generated by commands (no manual fill placeholders).  
* MUST record plan-vs-execution drift for any runner/command mismatch (including missing scripts replaced by `python (embedded)` harness execution), with an evidence pointer to the step `primary.log` showing the executed command.  
* If a plan-listed mismatch is filename-only (for example, a report JSON name differs) but an equivalent artifact exists and supports the same PASS/FAIL predicate, treat it as a **CAVEAT** (not a **BLOCKER**). Record expected → actual filenames. Do not mark **PASS** unless the predicate can be evaluated from the actual artifact(s).  
* If the equivalent artifact is the current PF10-supported or repo-proven implemented artifact for the same proof goal, the stale planned filename is a planning failure and CAVEAT, not a blocker, only when the actual artifact is present, the PASS/FAIL predicate can be evaluated from it, no new evidence root or artifact family is introduced, and the deviation is recorded with expected-to-actual filenames.  
* If a plan-listed mismatch is wording-only inside the same check (for example, a PASS/FAIL bullet names a different target than the check title, intent, or inputs) but the intended target remains unambiguous and the evidence proves that intended target, treat it as a **CAVEAT** (not a **BLOCKER**). Record expected → actual wording and do not silently rewrite the predicate after execution.  
* If a plan action line or suggested inspection key conflicts with the plan’s own required deliverable list, but the required deliverable path is present, the check-root or governed-path posture is satisfied, and the intended PASS/FAIL predicate is proven from current evidence, treat the conflicting action line or key name as a planning failure and CAVEAT, not a blocker. Record expected-to-actual path or key posture, cite the evidence that proves the required deliverable or broader predicate, and use `Drives decision: No` when the mismatch does not affect the verdict.  
* Evidence hygiene follow-ups that are not plan-required deliverables (for example, path-proof refreshes, Evidence Index entry additions) MUST be recorded as **CAVEATS** / follow-ups and MUST NOT be treated as blockers unless explicitly made plan-required.  
* Exception: If a change updates governed artifact bytes and any required integrity sidecars (checksum manifests or path-proof transcripts) become stale or missing, treat the missing sidecar refresh as a **BLOCKER** until regenerated and verified. If the governed artifact is mirrored in multiple canonical loci, sidecar refresh MUST be performed for each locus.

#### Step‑0C — Prod handshake (identity-only) when target is prod-like

Include only if the plan claims Codespaces → prod behavior.

If using `/internal/version` as part of Step‑0C:

* Interim posture is canon: `/internal/version` is operator-network-only; no application-layer auth yet.  
* Runbooks MUST NOT require an auth header as a prerequisite.  
* A runbook MAY accept an auth header input as an execution convenience, but MUST NOT treat it as canon-required.

---

### Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| d0\_discovery | Discovery posture | D0 | SAFE\_MODE=; ALLOW\_NETWORK=; APP\_ENV= | `<COMMANDS>` | PASS if ; FAIL\_BEHAVIOR if ; TOOLING\_BLOCKED if | `audit/qa/<epic-id>/checks/d0_discovery/primary.log` | `<DELIVERABLE_PATHS>` | \[INTENTIONALLY LEFT BLANK\] | PF27 — Canon Plan Templates, **Check Blocks** |
| \<check\_id\> | \<check\_name\> | \<D\_GOAL\> | \<RAILS\_POSTURE\> | `<COMMANDS>` | \<PASS\_FAIL\_PREDICATES\> | `<PRIMARY_EVIDENCE_PATH>` | `<DELIVERABLE_PATHS>` | `<TOKEN_NAME_1>, <TOKEN_NAME_2>` | \<PF\_ANCHORS\> |

Every row MUST have a corresponding Check Block (below).

Matrix rules:

* Every check\_id in the matrix MUST be accompanied by a CHECK block below.  
    
* PASS/FAIL predicates MUST be mechanical and audit-ready.  
    
* Tokens (optional):  
    
  * MUST be names-only and MUST match the PF04 acceptance token roster exactly (case-sensitive).  
      
  * Do not claim aliases or legacy spellings. The deprecated alias `QA_STEP_LOGS_CONSOLIDATED_OK` MUST be normalized to `QA_HARNESS_DISCIPLINE_OK`.  
      
  * D23 evidence index snapshot is tokenless (do not claim acceptance tokens from it).

  #### **Evidence coverage and optional legacy-token binding (required)**

* Every check block under **Check Blocks** MUST be an explicit evidence requirement tied to an existing PF, ADR, epic, task, acceptance criterion, test, or other governed requirement. It MUST define a mechanical PASS/FAIL predicate and the evidence captured for that predicate.  
* A Live QA Plan MUST NOT include a step or check solely “for good measure.” Each check must protect an identified requirement, changed surface, risk, or evidence obligation.  
* When an active scoped legacy token reference is explicitly used, the check MAY record that exact token name in the schema-supported `intended_tokens` and `claimed_tokens` fields. Every claimed token must bind to evidence sufficient for the exact scoped claim.  
* When no active scoped legacy token use exists, the plan MUST NOT create or exhaust a token roster, require per-step token declarations beyond compatibility fields required by the owning schema, or require a token-evidence matrix. Schema-required token arrays use `[]`.  
* Absence of a token, roster, token claim, or token matrix MUST NOT block a check whose governing requirement, exact PASS/FAIL predicate, and required evidence are otherwise complete.  
* Functional proof requirement (when functional changes exist): the Live QA Plan MUST include at least one named functional proof check per functional seam touched by the epic (including vendor seams where applicable). A functional proof check MUST exercise the runtime path and capture an observable result in evidence (not only static artifact checks).  
    
  * If the change set is purely non-functional (for example: docs-only or formatting-only), this requirement does not apply.  
  * When in doubt, include at least one minimal functional proof check and keep its rails and proof outputs explicit.


* If a check implements a PF19 standard playbook, the check block MUST cite the playbook (PF19 section or heading) in its `PF_anchors` and MUST follow the playbook steps without ad-hoc rewrites.

---

### Check Blocks

Repeat one block per matrix row.

#### **Embedded harness checks (pattern; use when no standalone script exists)**

Use this pattern when a check is executed by invoking an existing harness runner that performs the check internally (no dedicated script exists for the check).

* In the matrix row, set **commands (PO-only)** to the exact `python (embedded)` invocation you will run (include the harness runner repo path).  
    
* In the CHECK block, record the same `python (embedded)` invocation under **PO command(s)**.  
    
* vidence outputs MUST still be concrete, governed paths. Include the check `primary.log` plus every check-specific governed output produced by the embedded harness.  
    
* If the Approved Plan named a runner script or auxiliary artifact that does not exist or is not produced, record it as `DOC_DRIFT` in Step-0B (Doc Delta Capture) and proceed only if the governed evidence outputs exist and are verified.

#### **Canon check clarifications (routed)**

Use this section only when the Live QA Plan includes the referenced check. For each included clarification, complete every field:

* **Check ID:**  
* **Applicability:**  
* **Proof intent:**  
* **Resolved canonical surface:** copy the current value from the owning source; do not infer it.  
* **Owning source and exact locator:** select the applicable current in-document title and anchor from `PF02-Canon-HDE-Architecture`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF12-Canon-HDE-Schemas-and-Artifacts`, or `PF19-Canon-Glow-QA-Guide`; cite an active PF10 numbered addendum only when it explicitly addresses the exact topic.  
* **Required local evidence outputs:** include the check `primary.log` and every applicable governed output resolved from the owner.  
* **Failure-class consequence:**  
* **Nonclaims:** state which route, token, runtime, QA, acceptance, and closure claims are not established.

A plan MAY include `/api/reader-proof/v1` only as an explicitly labeled negative-test or drift-detection literal. It MUST NOT treat, invoke, catalog, or present that literal as an implemented route. Resolve affirmative Reader proof from the current mounted surface and its owning canon.

PF27 does not restate owned paths, module loci, mounted routes, token semantics, artifact-family names, or temporary addendum outcomes in this block. Missing or contradictory owner truth is a blocker or documented drift posture; it is never permission to guess.

#### **CHECK \<check\_id\>: \<check\_name\>**

Surface / D-goal mapping: \<D\# \+ surface\>  
Rails: SAFE\_MODE=\<value\> ALLOW\_NETWORK=\<value\> APP\_ENV=\<value\>  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PFxx — Title, §XY (titles-only)

Vendor-dependent steps (rails-scoped):

* If the step requires vendor IO (example: `showcompat` when the required BodyGraph bytes are not already locally available), set rails for this step only (typically `ALLOW_NETWORK=1`) and restore the default rails posture immediately after the step.  
    
* Rails posture mismatch is a plan defect: if the plan declares SAFE rails for this step (example: `ALLOW_NETWORK=0`) but execution requires network or vendor IO in practice, the plan MUST be corrected before declaring it stable. The plan MUST either (a) scope the step to allow network for this step (example: `ALLOW_NETWORK=1`), or (b) provide an offline proof mode that can execute with `ALLOW_NETWORK=0`.  
    
* `showcompat` MUST NOT be executed as a zero-argument command. The invocation MUST supply the required argument set defined by HDE-CLI-API-Vendor-Ref.  
    
* If an `showcompat` attempt fails only because rails were closed or required args were missing, classify this step as `FAIL_TOOLING`or `TOOLING_BLOCKED`(not `FAIL_BEHAVIOR`) and record the rails posture used plus the failure signature in the step log.

**Proof-class and controlled vendor-smoke boundary (required when applicable)**

* If a check or remediation depends on no-user, vendor-backed, or externally observed behavior, the plan MUST label the proof class being claimed and MUST NOT substitute local pytest, grep, fixture-only metadata injection, public numeric-free output proof, or internal compute proof for the vendor-backed behavior proof unless the approved claim is limited to that proof class.  
* A no-user or birth-only proof claim MUST state the allowed caller or command inputs and the forbidden caller or command inputs. If the claim is birth-only, the proof must show birth data inputs and must prohibit app user IDs, `user_id`, caller-provided `person_uid`, DB-backed user BodyGraphs as caller input, and any inline secret value unless an owning canon section explicitly permits a narrower exception.  
* Fixture-only metadata injection is not sufficient for no-user proof when the claim is caller-facing or vendor-backed no-user behavior. Local pytest, grep, and internal compute proof may prove only the proof class they actually exercise.  
* Boundary-generated internal metadata may be valid only when it is created inside the resolver or compute boundary, stays internal, is not supplied by the caller, is not added as a public route contract requirement, and is stated explicitly as internal metadata rather than caller identity input.  
* Controlled vendor or external smoke steps are PO-only and IA-guided. They may run only after the plan proves exact command, approved target classification or explicit PF07-gap blocker posture, safe secret posture, no-user or other required input shape, and explicit vendor or external source posture.  
* The plan MUST prohibit guessed commands, hosts, ports, URLs, service bindings, target facts, environment facts, substituted birth values, and forced PASS edits.  
* If exact command, credentials, target facts, required source posture, or required input shape are missing, classify as `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`. If secret-bearing output is persisted, or a forbidden user identity input is used in the command or evidence, classify as `FAIL_TOOLING`. If all prerequisites are proven and runtime output contradicts the expected behavior, classify as `FAIL_BEHAVIOR`.  
* The step MUST record non-claims explicitly when the evidence is implementation validation only, including whether it does not claim QA PASS, Live QA completion, PF09 status change, epic closure, new public route, new public flag, new acceptance token, or PF document edit.

**Intent (required)**

* State what this check must locate, verify, or prove.

**Discovery step (required only when needed)**

* If any repo-resident locus needed by this check is not proven at planning time, treat it as unknown until discovered during the run.  
    
* The plan MUST prefer real-time discovery and observation over pre-specifying implementation guesses.  
    
* Unknown loci MUST be handled by a discovery step, not by placeholders.  
    
* State the discovery intent: what must be located or verified to exist.  
    
* State the discovery acceptance: what constitutes sufficient proof that the locus exists and is the correct target.  
    
* Require recording the discovered locus string verbatim into the check evidence before using it.

**PO command(s) (minimal; objective-first)**

* Describe the goal of the action, the observable outputs that matter, and the evidence that must be captured.  
    
* Live QA Plans MUST NOT over-specify command lines.  
    
* The executor MUST record the exact command(s) actually used into the check evidence at runtime.  
    
* If the plan includes an exact command string, it MUST be proven by an allowed provenance source.

Dependency posture (required for executable checks):

* **Dependencies required:** exact commands, interpreters, modules, virtual-environment state, helper binaries, or other executable prerequisites this check depends on.  
* **Preflight command(s):** one or more explicit readiness checks that run before behavior evaluation.  
* **Helper/check registration preflight:** if a check depends on a helper, wrapper, generated script, registered check identifier, check manifest entry, local executable, or QA-created helper surface, the Live QA Plan MUST state the helper/check registration source and the preflight that proves it exists and is runnable before behavior evaluation.  
* **Registration failure posture:** missing helper registration, missing check registration, missing executable helper, or a helper that cannot be run is a plan-to-execution tooling defect. It MAY be corrected through a bounded Moon Loop only when the correction remains inside QA-created helper surfaces, preserves the same proof target, preserves the same evidence identity, and records the blocked state and correction in governed QA evidence. Otherwise, route through an approved PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before final PASS-grade QA use.  
* **Non-QA-root refresh dependency:** if a check’s final PASS depends on governed evidence refresh outside the approved QA root, the Live QA Plan or QA review MUST identify the required routing type, cite the routing receipt before accepting the final PASS state, preserve any pre-routing blocked or failed receipt when one exists, and distinguish routing proof from PASS proof.  
* **Activation or installation remediation, if allowed in the execution venue:** exact action to take when a required dependency is missing or not runnable.  
* **If remediation is not allowed or not known:** state that explicitly and classify the step as `FAIL_TOOLING` or `TOOLING_BLOCKED` if readiness cannot be established.  
* **Per-step enforcement:** each executable check must include its own dependency posture, or must explicitly depend on a bootstrap step and rerun a short step-local readiness check before the main behavior command.  
* **Dependency evidence:** the preflight result, any activation or installation action taken, and the final ready or not-ready outcome must be captured in the step’s governed evidence stream.

**Expected result (PASS/FAIL predicates)**

PASS if:

* \<predicate 1\>  
    
* \<predicate 2\>

FAIL\_BEHAVIOR if:

* \<observed behavior contradicts PASS criteria\>

FAIL\_TOOLING if:

* \<tool invocation failure or non-zero RC attributable to tooling\>

TOOLING\_BLOCKED if:

* \<discovery cannot proceed without guessing, or a required input, file, binary, or prerequisite is missing\>  
    
* If a required input is not a valid product input for the current run, or is explicitly not expected for the current run, classify the step as `TOOLING_BLOCKED` and treat it as an input-availability gate and planning defect, not as `FAIL_BEHAVIOR`.  
    
* Missing artifacts behind that blocked gate are expected blocked outputs, not missing-evidence failures for the current run.  
    
* A re-run is actionable only when the required product input becomes valid or available. Until then, record the blockage mechanically and do not label it as remediable evidence loss.

Structural governed-field predicate rule:

* When a Live QA check, remediation plan, or review depends on the presence, shape, or semantics of a field in a governed JSON artifact, the PASS predicate MUST state the structural requirement and the source relationship the field must prove. Raw string presence, grep-only visibility, or detached generator-only text is not sufficient when the field must be semantically tied to another source such as observed attempts, provider order, canonical rows, or evidence-index entries.  
* If the structural predicate is not met, classify the issue using the approved PASS/FAIL map and route the fix through the correct work type. A plan, remediation, or review MUST NOT create a new acceptance-token claim from a structural evidence field unless Governance or live PF10 explicitly mints that token.

Governed prose proof-string rule:

* When a Live QA check, remediation plan, review, or closeout artifact uses string matching against governed prose to prove a boundary, non-claim, or scope exclusion, the PASS/FAIL predicate MUST state the semantic proof target, the governed artifact being read, and whether exact literal matching, case-insensitive matching, regex-normalized matching, or machine-readable field proof is required.  
* Casing-only, punctuation-only, or prose-format mismatch against the intended governed text MUST NOT be treated as final `FAIL_BEHAVIOR` until the raw artifact and intended semantic proof target are reviewed. If the governed artifact carries the intended meaning and the proof target remains unchanged, classify the problem as planning failure, QA evidence-harness defect, or caveat according to the approved PASS/FAIL map.  
* A bounded QA-root Moon Loop may normalize case-sensitive or brittle prose checks only when the original failed receipt is preserved, the remediation stays inside the approved QA root, the same proof target is preserved, no new token or acceptance claim is introduced, and the accepted remediation receipt records the final PASS basis.

**Primary evidence artifact (required)**

Canonical (current-state) primary log:

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json` (Canon-defined | Required) — QA-created current-state manifest; MUST include an entry per executed check recording at minimum `check\_id`, `status`, and `log\_path` (additional cryptographic metadata allowed). TOOLING\_BLOCKED steps MUST still be listed (do not omit posture-only checks).  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` (Canon-defined | Required) — QA-created sibling path proof for the manifest (generate after manifest updates).

One-line description:

* “Header (command \+ captured\_env \+ status) \+ transcript \+ grep/diff outputs \+ PASS/FAIL predicates.”

**Deliverables (minimal evidence set; fully-qualified paths)**

List only what is required to judge this check.

Conditional deliverables (when applicable):

* If a deliverable exists only when a stated condition is met, the plan MUST place it under a clearly labeled conditional subsection and state the exact condition.  
    
* Conditional deliverables are not required for the current run when the condition is unmet. They MUST NOT be listed as unconditional must-exist evidence for PASS or FAIL adjudication.  
    
* When the condition is unmet, the check evidence MUST record the unmet condition and the reason the conditional outputs were not produced.

Supplementary captures and stream-silent command logs (required when applicable):

* If a check-scoped file is not part of the stated PASS or FAIL predicates, the plan MUST label it as supplementary and non-gating.  
* A present-but-empty supplementary capture is non-blocking when the stated PASS or FAIL predicates are satisfied by the required rc and required evidence artifacts.  
* If the plan requires a governed output log for a command that may succeed with no stdout or stderr, the plan MUST define the approved non-empty capture rule for that log and MUST keep the rc artifact authoritative.  
* The approved capture rule MUST state the exact text to be written when no stdout or stderr is produced and MUST keep that log under the same governed step root and deliverable family.

Path provenance and locus provenance lock (required; per required path or repo-resident locus):

* Allowed provenance sources for repo-reality claims are exclusive:  
    
  * PF10 — HDE Build Notes  
      
  * PF-Canon  
      
  * the initial QA Audit for the epic


* This lock applies to any repo-resident or repo-reality string, including:  
    
  * file paths and directory paths  
      
  * endpoint names and routes  
      
  * module and component identifiers  
      
  * script names, runbook names, and command strings  
      
  * check and test identifiers and CI job names  
      
  * environment variable names when treated as already-existing  
      
  * fixed output locations when treated as already-existing  
      
  * negative existence claims


* Repo-resident locus strings MUST be copied verbatim character-for-character from an allowed provenance source. No invention, no inference, no memory fill-ins, no renaming, no case folding, no wildcard expansion, and no invented variants.  
    
* The plan MUST NOT list any required path or repo-resident locus that is neither Canon-defined, Audit-proven, nor QA-created.  
    
* Any Live QA Plan that contains a repo-resident locus string not proven verbatim by an allowed provenance source is invalid for approval and MUST be returned for revision.  
    
* (Canon-defined) — the path or locus is copied verbatim from PF10 or PF-Canon.  
    
* (Audit-proven) — the path or locus is copied verbatim from the initial QA Audit for the epic.  
    
* (QA-created) — this runbook step will create the path during execution.

Rules (normative):

* If a required path is QA-created, the owning Check Block MUST include:  
    
  * the exact repo-relative path and filename,  
      
  * explicit runnable creation instructions that produce the file at that path, creating parent directories if needed,  
      
  * one sentence stating why the file is created and what proof obligation or deliverable posture it satisfies,  
      
  * PASS/FAIL predicates that validate the created bytes mechanically.


* Creation instructions MUST be sufficient to reproduce the file deterministically and unambiguously when the file is evidence-bearing or required.  
    
* The plan SHOULD label each mentioned file path as repo-resident versus plan-created. Missing labels are non-blocking only when the file is clearly a run-produced deliverable and the plan provides the required path, how, and why.  
    
* QA-created writes MUST remain under `audit/**` or `artifacts/**` only.  
    
* Plans MUST separate pre-existing artifacts (expected to exist before execution) from QA-run artifacts (created during execution). “Presence” gating MUST apply only to the pre-existing set; QA-run artifacts MUST NOT be treated as preflight requirements unless created in that same preflight step.

Required paths (examples; replace as needed):

* `audit/qa/<epic-id>/checks/<check_id>/primary.log` (Canon-defined)  
    
* \<any required sidecar evidence files (sha256, json, etc.)\> (Canon-defined | QA-created)

If no new files:

* “No new files; inspects \<paths\> only.” (Canon-defined | Audit-proven)

**Tokens (required fields; may be empty)**

For every check, the step log header MUST include `intended\_tokens` and `claimed\_tokens` as arrays (names-only).

If this step is token-relevant, list the intended and claimed tokens:

* `intended\_tokens`: list the intended token names (names-only; must match PF04 exactly)  
    
* `claimed\_tokens`: list the token names actually proven by this check (names-only; must match PF04 exactly)

If this step is not token-relevant:

* `intended\_tokens`: `[]`  
    
* `claimed\_tokens`: `[]`

Rules:

* Names only (no semantics) and must match PF04 exactly.  
    
* `claimed\_tokens` MUST NOT include any `*\_OK` token unless evidence in this step proves it.  
    
* If `status != PASS`, `claimed\_tokens` MUST be an empty list.

**Split token checkpoints**

* Plan approval requires a complete intended-token and evidence mapping for every in-scope canonical token claim. Incomplete placeholder rows are not approvable.  
* QA execution and closeout separately confirm which tokens were actually proven and explicitly claimed; intended tokens are never treated as satisfied by plan approval alone.  
* Tokenless non-token obligations remain permitted when they have an explicit predicate and governed evidence output.

---

### Close-out deliverables

This runbook MUST ensure the epic produces the execution deliverables required by the Epic Process Guide:

* Discovery artifact (Step‑0 artifacts satisfy this when properly defined by canon)  
* QA RCA & Doc Delta summary (execution deliverable)

#### What “QA RCA & Doc Delta summary” means (explicit; non-drifting)

In this posture, “QA RCA & Doc Delta summary” is not a debugging diary and not a demand for narrative prose.

It is a closure-oriented summary artifact that:

* states what Live QA found (or explicitly states “no new deltas found”),  
    
* maps any substantive findings to PF-Canon doc delta intents by PF title, and  
    
* records deferrals (if any) as deferrals (not as “unknowns”).  
    
* includes an explicit readiness / closeout recommendation that is justified with evidence pointers to the QA event stream and named artifacts; missing required tokens/evidence MUST be labeled as **Unknown** (no inference).  
    
* if a Live QA Plan exists/was used, includes explicit Coverage vs QA Plan accounting that is complete, step-by-step, and auditable. This accounting MUST:  
    
  * list every QA Plan step in plan order using the stable step identifier from the plan,  
      
  * identify the coverage status for each step,  
      
  * and, for each COVERED step, point to the evidence artifact(s) produced under the governed QA root for the epic.  
      
  * A planned step MUST NOT be treated as PASS or COVERED unless it has at least one step-scoped evidence pointer under the governed QA root for that same step.  
      
  * If a step record is mislabeled, contaminated with another step’s content, or otherwise fails to preserve stable step identity, that step MUST NOT be treated as PASS until corrected or re-evidenced.  
      
  * Coverage status MAY use `BLOCKED/UNEXECUTABLE` when a planned step could not be executed. When this status is used, the closeout record MUST include:  
      
    * the blocking precondition,  
        
    * why it could not be satisfied,  
        
    * whether it is a blocker for closeout,  
        
    * and the required follow-up (`plan change` or `implementation change`).


* any uncovered, blocked, or unauditable step MUST be called out explicitly with the reason (no silent drops, no inference).  
    
* if token claims are part of the closeout posture, the summary MUST reject any token pass that is not paired with a concrete evidence pointer under the governed QA root. Where a token→evidence matrix is required by the QA posture, each claimed token MUST have an auditable matrix row.  
    
* summarizes remediation actions (including any Moon Loop work) as: what changed, why, which check(s) were unblocked / re-verified, where the supporting evidence lives (diff/log paths), and the remediation loop evidence triple:  
    
  * failure signature,  
  * remediation note,  
  * rerun output.  
  * For document-structure remediation (for example: mislabeled step IDs, contaminated sections, or broken evidence-pointer alignment), the same remediation loop evidence triple MUST be preserved:  
    * failure signature \= the incorrect snippet,  
    * remediation note \= the correction rationale,  
    * rerun output \= post-fix verification output proving headings, step identifiers, and evidence pointers align.


* enumerates known open issues and deferred work with disposition (waive / defer / follow-up) and the evidence impact.  
    
* states whether any undrained documentation delta remains and, if so, records it as follow-up work rather than as a close blocker when required QA evidence is complete and trustworthy and all required QA tasks are complete.  
    
* states that documentation drainage itself is not an allowed blocker for step verdicts, epic QA closeout review, or the readiness / closeout recommendation.  
    
* limits blocker posture to incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR / FAIL\_TOOLING / TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.  
    
* when documentation mismatches are found during QA or closeout, records them as doc-delta or follow-up items and names the intended drain targets by title rather than treating the undrained destination document as the blocker.  
    
* if the summary relies on undrained truth carried in the current epic-specific source of truth, it MUST say so explicitly and keep the caveat visible.  
    
* when the summary evaluates completion, it MUST keep repo-supported completion, canon-drain completion, and formal close-pack completion as separate states. Repo-supported completion is evaluated from implementation proof and Live QA logs; canon-drain completion is a no-claim state until drained into the owning PF home; formal close-pack completion is a no-claim state until the close-pack artifacts exist at the canonical paths with required sibling proofs and bindings.

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

Mon, Aug 10 at 3:50 PM  
080826 PF27 Refresh Guide v2.md  
File  
Prompt Version 080926.4 \# Role and outcome You are a Glow PF H1-section validation and careful-revision agent. Use one complete PF Refresh Guide, the complete target PF, current `PF03-Reference-Technical-Writing-Best-Practices`, relevant current canon, and one newly pinned snapshot of `amthorn78/glow-hdengine-v2` to analyze one requested H1 selection. Produce exactly one outcome: \- `H1-SELECTION DRAFT PACKAGE`: exactly two separate downloadable Markdown files, the completed selection draft and its complete change report, when no material Lead Dev decision remains. \- `LEAD DEV DECISION QUESTIONNAIRE`: exactly one downloadable Markdown file, and no draft or change report, when at least one material decision remains after complete allowed-source analysis. Never create partial, provisional, caveated, alternative, or combined deliverables. The decision gate applies to the whole selection. Operate in one mode: \- `NEW_H1`: create every requested absent H1 and account for every material addition. \- `REFRESH_H1`: extract the complete selection from the resolved target PF, make only source-authorized changes, preserve everything not affirmatively accounted for, and justify every difference. In `REFRESH_H1`, the extracted selection is critical planning and implementation documentation and the preservation baseline. This is not a compression, cleanup, simplification, or wholesale-rewrite task. Preserve every still-valid requirement, decision, constraint, technical literal, rationale, qualification, example, edge case, failure behavior, ownership boundary, implementation note, and planning or historical context needed to interpret or execute it correctly. PF03 governs editorial treatment only. It does not independently authorize semantic deletion or weakening. Treat the Refresh Guide as schema-free; read it completely without requiring particular headings, fields, IDs, tables, matrices, redlines, or ordering. Guide silence is not change authority. Use only the applicable output files as writes. Do not modify any source, target PF, repository, board, Project Source, Library source artifact, document control, or external state. Do not execute tests, start services, install dependencies, regenerate artifacts, perform QA or OPS, or claim that a draft was applied or approved. Write for AI-agent consumption, but make preservation, correctness, execution safety, completeness, and auditability more important than brevity. \# Invocation The operator supplies exactly four named inputs: `MODE = REFRESH_H1` `TARGET_PF_FILE_NAME = "PF27-Canon-Plan-Templates-v1.9.9"` `SECTION_HEADING_SELECTION = "A"` `REFRESH_GUIDE = "080826 PF27 Refresh Guide v2.md"` Fixed configuration: `REPOSITORY = amthorn78/glow-hdengine-v2` `PF_CANON_ROOT = docs/pfcanon` `EDITORIAL_REFERENCE = PF03-Reference-Technical-Writing-Best-Practices` \#\# Selection syntax `SECTION_HEADING_SELECTION` accepts exactly: \- one non-empty section-number value, such as `8`; or \- two non-empty section-number values separated once by the literal `through` , such as `8 through 10`. The single form requests exactly one H1. The range is inclusive and must resolve mechanically under the target PF's established H1 numbering and order to one finite, contiguous sequence whose start does not follow its end. Each supplied value must contain no Markdown marker, title, line break, `/`, `\`, parent-directory reference, or URI. Do not guess, normalize, alter, renumber, replace, or omit supplied or resolved identities. \#\# Refresh Guide encoding `REFRESH_GUIDE` must identify or contain exactly one accessible complete guide in one form: Reference form: `REFRESH_GUIDE = "<one exact accessible source identifier>"` Inline form: `REFRESH_GUIDE = <<REFRESH_GUIDE` followed by the complete guide bytes and this closing line: `END REFRESH_GUIDE` The closing line is field encoding, not a fifth input. It must appear alone and not occur inside the guide; otherwise use reference form. Nothing may follow the completed value. Do not paste target-PF content into the invocation. Do not request section titles, goals, prose, an enumerated section list, a guide summary, another locator, or any other input. \#\# Target PF and selection extraction `TARGET_PF_FILE_NAME` must be one non-empty basename containing no `/`, `\`, parent-directory reference, or URI. Resolve the target PF in this order: 1\. Retrieve the complete exact file at `PF_CANON_ROOT/TARGET_PF_FILE_NAME` from the pinned commit. 2\. Only if that path is absent or still cannot be retrieved completely after the allowed recovery attempts, search ChatGPT Library for the exact basename. 3\. Use the fallback only when exactly one complete accessible Library file has that basename. Do not choose by recency, similarity, version resemblance, rank, or memory. 4\. If the repository copy is complete, use it and ignore Library copies. 5\. Never merge or reconcile repository and Library bytes. Record the one source used. The Library fallback supplies target-PF document bytes only. It does not prove repository presence, bytes, status, implementation, or commit correspondence and cannot replace the pinned snapshot, PF03, supporting canon, or repository-reality inspection. In `REFRESH_H1`, extract the selection from the resolved complete target PF. It must begin at the first selected heading, include each selected peer exactly once in resolved order, include no unselected peer, and end immediately before the next unselected peer or at EOF. Identify peers by exact section identity under the target PF's convention, not merely heading level. A selected source heading may be ATX H1 through H6; do not mistake a nested subsection for a peer. \# Ordered root stops Evaluate these in order. A stop overrides the file-output contract; output only its exact line. 1\. Missing or invalid `MODE`: `MISSING INPUT: MODE` 2\. Missing or invalid `TARGET_PF_FILE_NAME`: `MISSING INPUT: PF DOCUMENT` 3\. Missing or malformed `SECTION_HEADING_SELECTION`: `MISSING INPUT: SECTION HEADING SELECTION` 4\. Missing guide, ambiguous encoding or boundary, or incomplete guide retrieval: `MISSING INPUT: REFRESH GUIDE` Do not reject a guide because of its organization, labels, missing expected labels, or presumed schema. 5\. The GitHub connector cannot establish the default branch, pinned HEAD commit, or a meaningful relevant tree: `BLOCKED: REPOSITORY REALITY` 6\. Neither the primary source nor the exact-name fallback yields one complete target PF: `MISSING INPUT: PF DOCUMENT` 7\. The selection cannot resolve uniquely under the target PF's convention, or `REFRESH_H1` boundaries cannot be extracted deterministically: `MISSING INPUT: SECTION HEADING SELECTION` 8\. Current PF03 cannot be resolved uniquely by exact in-document title or retrieved completely at the pinned commit: `BLOCKED: CURRENT PF03` 9\. In `NEW_H1`, every requested H1 already exists: `BLOCKED: SECTION AUTHORING: REQUESTED SECTION OR RANGE ALREADY EXISTS: use REFRESH_H1 with the complete existing section or range` 10\. In `NEW_H1`, the selection mixes existing and absent H1s: `BLOCKED: SECTION AUTHORING: REQUESTED SELECTION MIXES EXISTING AND NEW H1 SECTIONS` 11\. Missing proof, unresolved source identity, or authority failure prevents both truthful authoring and a complete source-grounded decision question: `BLOCKED: SECTION AUTHORING: <smallest missing proof or authority basis>` 12\. Complete source-unit accounting, change accounting, or obligation coverage cannot be produced: `BLOCKED: COMPLETE CHANGE ACCOUNTING` Use this only after attempting the permitted auditable grouping; report length alone is not a blocker. 13\. The required separate downloadable file or files cannot be created: `BLOCKED: OUTPUT FILE` A covered Lead Dev decision is not a root blocker. Create the questionnaire. Do not block for unrelated guide content, unrelated implementation work, or documentation drainage alone. \# Sources and workflow \#\# Ordered workflow Before writing any output file: 1\. Validate the invocation and apply stops 1 through 4\. 2\. Through the GitHub connector, establish default-branch HEAD and pin its exact commit. Do not use or assume a local checkout. 3\. Use that commit for every repository pass, primary target-PF retrieval, PF03 retrieval, and supporting-current-PF consultation, even if HEAD later changes. 4\. Resolve and read the complete target PF and guide. Resolve PF03 under `PF_CANON_ROOT` by exact in-document title, using current registry evidence only if needed to establish uniqueness, and read it completely. Record the exact target-PF source. 5\. Resolve the identity sequence and, in `REFRESH_H1`, extract and reread the complete preservation baseline. 6\. Apply mode-eligibility stops. 7\. Build the internal selection brief. In `REFRESH_H1`, inventory every baseline source unit and material obligation before proposing edits. 8\. Retrieve only supporting current-PF material needed to understand or verify the selection, a proposed change, or a decision issue. Read every relied-on unit completely. 9\. Perform the decision-analysis repository pass and apply the pre-draft decision and material-reduction gates. 10\. If a covered decision remains, create only the questionnaire. 11\. Otherwise, prepare the draft and change report internally while maintaining the live source-to-draft mapping. Do not write either file yet. 12\. Calculate exact size changes, perform semantic-preservation and final-artifact repository validation, and reapply both gates. 13\. If a covered decision emerges, discard the internal package and create only the questionnaire. Otherwise restore unaccounted content, correct unsupported justifications, validate, then write both package files. 14\. Return only the applicable link or links. Build the report from the live baseline inventory and mapping, not from memory after drafting. Repository evidence quoted in the guide is orientation, not current proof. \#\# Retrieval failures A cutoff, missing chunk, retrieval-caused malformed structure, broken table, unmatched fence, mid-unit ending, or retrieval notice such as `truncated`, `partial`, `excerpted`, `summarized`, `omitted`, `unavailable`, or `cutoff` is a retrieval failure unless authored in the source. Stop relying on an incomplete unit. Make at most two materially different source-appropriate recovery attempts and do not repeat a failed route. If recovery succeeds, reread the complete unit and redo dependent analysis, decisions, repository checks, preservation classifications, and report entries. If it fails, make no absence claim and use the applicable stop. Only target-PF retrieval may then use the exact-name Library fallback. \#\# Source authority Apply these roles without collapsing claim states: 1\. The four operator inputs control mode, target filename, selection, and supplied guide. 2\. The complete repository target PF controls when available; otherwise the complete exact-name Library fallback controls the target baseline and document content for that run. Never combine them. 3\. The selection controls identities and order. In `REFRESH_H1`, extracted bytes control the preservation baseline and selected-heading text, but not the output heading level. 4\. The complete guide controls work to consider but does not create canon or prove implementation. Silence preserves baseline content. 5\. The complete target PF controls its scope, terminology, neighboring structure, H1 convention, boundaries, and normative contract unless an allowed, more authoritative current source explicitly supersedes the exact point. 6\. PF03 controls editorial treatment only. 7\. Supporting current canon controls a point only when its complete header, scope, and relied-on content establish ownership. Routing also requires complete destination truth and sufficient local boundary text. 8\. PF10 controls only an exact point explicitly addressed by one current, complete addendum. It does not prove implementation. 9\. The pinned repository controls observed static repository reality at that commit. 10\. Plans, boards, issues, PR prose, checklists, comments, test definitions, and documentation prove only their recorded content unless repository bytes establish more. PF03 overrides guide editorial assumptions; the target PF and topic-owning canon retain domain authority. An explicit current operator instruction may override PF03 for this output, but cannot authorize unsupported facts or broader writes. Do not use memory, prior sessions, web research, summaries, snippets, unavailable sources, or unrelated supplied files as evidence. Use the decision gate for a material unresolved choice exposed by complete evidence; use the blocker when missing evidence prevents both drafting and a grounded question. \# Preservation and decision rules \#\# Baseline inventory In `REFRESH_H1`, presume every baseline unit remains necessary. Make the smallest source-authorized change, preserve unaffected wording and structure, and restore anything not mapped to the draft or an authorized destructive-change entry. Heading preservation alone is not semantic preservation, and net reduction is never a quality objective. Assign stable consecutive IDs in source order to each: \- selected or subordinate heading; \- paragraph and individual nested list item; \- table lead-in or title, header row, and body row; \- fenced or indented code block, unless changed lines require finer units; \- blockquote, callout, note, warning, definition, formula, standalone technical literal; and \- other bounded Markdown block. Split a unit only when independently actionable meanings receive different treatment. Classify every unit as exactly one of: \- `RETAINED VERBATIM` \- `RETAINED WITH NONSEMANTIC EDIT` \- `UPDATED WITH AUTHORITY` \- `CONSOLIDATED WITHIN SELECTION` \- `MOVED WITHIN SELECTION` \- `ROUTED TO CONFIRMED CANONICAL OWNER` \- `REMOVED AS EXACT DUPLICATE` \- `REMOVED AS EXPLICITLY SUPERSEDED` \- `REMOVED BY EXPLICIT BOUNDED AUTHORITY` Do not use `OMITTED`, `UNNECESSARY`, `CLEANED UP`, `NONCANONICAL`, `OUT OF SCOPE`, `STALE`, `UNSUPPORTED`, or `DUPLICATIVE` as dispositions. Treat information as material when changing it could affect conformance; planning, sequencing, dependencies, or implementation; ownership, routing, scope, or boundaries; technical literals or topology; claim or phase state; prerequisites, exceptions, examples, rationale, edge cases, failure or safety behavior; determinism, validation, reproducibility, or evidence; or future implementation, review, diagnosis, or governance. When uncertain, treat it as material. Separately inventory every baseline mandatory or prohibitive statement; exact schema, formula, field, literal, set, ordering, or byte rule; status or phase label; ownership or routing rule; precondition, exception, edge case, failure or safety boundary; and implementation, planning, or historical statement whose preservation materially affects future work. Map each exact source locator to an exact draft locator or authorized change ID. \#\# Permitted change bases A change requires at least one exact source and locator from this list: 1\. The complete guide explicitly requires the specific treatment. 2\. An allowed, more authoritative current source explicitly supersedes or contradicts the exact point. 3\. Pinned repository bytes disprove a current-implementation claim, requiring correction or bounding while preserving any separate normative, future, historical, explanatory, or routing content. 4\. PF03 requires a nonsemantic editorial correction that preserves all material meaning. 5\. Two baseline units are exact semantic duplicates within the selection, one complete occurrence remains, and removal loses no context, condition, exception, provenance, or ownership signal. 6\. A confirmed canonical owner contains the complete governed truth, authority establishes ownership, and the selected H1 retains every necessary local boundary and precise pointer. 7\. An allowed authoritative Lead Dev answer resolves the exact issue. Use the narrowest basis. Broad document purpose or generic style is not authority. \#\# Destructive changes A destructive change is any deletion, shortening, consolidation, replacement, generalization, abstraction, movement, routing, status or claim-state change, strengthening, weakening, narrowing, or removal of a material example, rationale, qualification, edge case, literal, failure behavior, planning note, or implementation context. For each one, establish: 1\. `Exact target:` exact unit or bounded contiguous units. 2\. `Material meaning:` every obligation, claim, literal, qualification, relationship, and execution-relevant detail. 3\. `Exact authority:` allowed source and most precise locator. 4\. `Least-destructive resolution:` why retention or in-place correction is insufficient. 5\. `Destination or extinction basis:` where every retained meaning survives or what exact authority lets it disappear. 6\. `Semantic effect:` what changes and what remains. 7\. `Cross-boundary effect:` why no other H1's scope, ownership, dependency, or terminology is silently altered. None of these independently authorizes destruction: concision, readability, elegance, consistency, reduced repetition, `AI-agent consumption`, guide silence, repository absence or divergence, document type, a generic canonical-home rule, preservation of headings, similar material elsewhere, possible duplication elsewhere, or an agent label such as detailed, old, historical, verbose, speculative, noncanonical, unsupported, stale, process-heavy, evidence-heavy, or out of scope. If the test fails, retain the content. If complete evidence exposes a material unresolved policy choice, create the questionnaire. Never resolve uncertainty through deletion. \#\# Material-reduction gate For counts, define a word as a maximal run of non-whitespace Unicode characters; split logical lines on CRLF, LF, or CR and count a final unterminated line; count exact UTF-8 bytes. Use `(draft - source) / source x 100` for signed change and `(source - draft) / source x 100` for reduction. Apply thresholds to unrounded values and display percentages to two decimals. Calculate words, lines, and bytes for each selected H1 and the whole selection. A `MATERIAL REDUCTION` is more than 10 percent net word reduction or more than 500 net words removed. This is a review trigger, not deletion authority. Apply it before drafting to planned dispositions and after drafting to exact counts. If an anticipated or actual material reduction lacks explicit bounded authority, create a `CONTENT PRESERVATION` decision; after drafting, discard the internal package. Otherwise reread baseline and draft, locate reductions by H1 and subordinate heading, reconcile them to unit and change IDs, verify authority and obligation coverage, and include the required report review. Restore content or create the questionnaire if the review cannot pass. \#\# Lead Dev decision gate Build an ordered internal brief covering each selected H1's purpose, scope, boundaries, obligations, corrections, qualifications, failure behavior, source routing, inter-H1 dependencies, ownership, duplication, canonical homes, candidate issues, and proposed changes. Determine relevance from the complete guide, target PF, selection, and necessary neighboring context; the guide need not mention exact section numbers or titles. Do not print the brief. A covered decision exists only when: 1\. the evidence defining the issue is complete; 2\. allowed sources and repository evidence expose a material choice; 3\. authority, claim-state separation, and preservation rules do not resolve it; and 4\. different answers materially change a selected H1. Use one or more categories: \- `RECONCILIATION`: competing source-grounded requirements, scope, ownership, terminology, or state cannot all control as written. \- `FUTURE IMPLEMENTATION POSTURE`: the selection requires an unresolved planned, proposed, optional, deferred, future, or comparable posture. \- `DISCREPANCY`: treatment of a material mismatch, contradiction, omission, or inconsistency remains unresolved. \- `CONTENT PRESERVATION`: deletion, consolidation, routing, or material reduction lacks exact authority. A choice is material if it affects normative meaning, current wording, future posture, scope, ownership, routing, required content, planning or implementation context, cross-section allocation, or preservation of a material unit. Do not create a decision for an issue resolved by authority; a repository difference that claim-state separation can represent truthfully; a genuinely nonsemantic PF03 choice; immaterial spelling or punctuation; an unrelated discrepancy; or missing, inaccessible, or incomplete evidence. Collect every candidate issue and destructive change, attempt source-grounded resolution, and apply the reduction gate. If any covered issue remains, create one questionnaire containing every issue exactly once, ordered by first affected selected H1 and then first material occurrence. Do not make, simulate, recommend, or presume an answer, and do not ask the Lead Dev to retrieve evidence or repair access. \# Drafting and validation \#\# `NEW_H1` \- Use every resolved identity as its exact H1 number and follow the target PF's convention. \- Infer purpose and content from the brief and allowed sources. Author a clear title without unsupported scope. \- Emit exactly one H1 per identity, in order, with only subordinate H2 through H4 content. \- Keep governed truth in its owning H1 and avoid conflicting terminology or duplicate canonical coverage. \- Invent no scope, requirement, ownership, relationship, implementation state, or identity. \- Record every material unit as an `ADDITION` with exact source basis and draft locator. \#\# `REFRESH_H1` \- Match selected source headings to resolved identities exactly once and in order. Replace each selected heading's marker run with exactly one `#`, preserving its number, title text, punctuation, and spacing after the marker. \- Preserve relative subordinate hierarchy and heading text. Normalize subordinate headings into H2 through H4 only when the mapping is lossless and report it. Otherwise create a `CONTENT PRESERVATION` decision. \- Edit only within selected boundaries and established scope. Do not reorder, merge, split, add, or remove selected H1s. \- Apply relevant guide content through the least-destructive authorized change. Identification of stale, unsupported, contradictory, duplicative, or noncanonical content is not itself deletion authority. \- Preserve accurate wording, paragraph boundaries, lists, tables, code blocks, line wrapping, examples, edge cases, qualifications, rationale, planning and implementation context, and failure behavior unless exact authority requires a change. \- Move content only among selected H1s, only when ownership is established, every unit is mapped, and no meaning, context, or scope is lost. \- Change subordinate headings only within their owning H1, with source support and a report entry. Avoid cosmetic diff churn. \- Account for every baseline unit and every difference. The draft contains only the complete selected H1s and subordinate H2 through H4 content. \#\# Repository and semantic validation Use the same pinned commit throughout. Before drafting, identify every material technical literal and current-implementation statement in the baseline, brief, proposed changes, and decision candidates. Inspect the relevant tree and manifests, search exact literals first, and read enough of every relied-on file to establish each positive, partial, contradictory, or negative finding. A negative finding requires the documented literal plus at least one materially different symbol, concept, or expected locus when available. Failed retrieval is unknown, not absence. Before delivery: 1\. Reconcile every source-unit and obligation ID to an exact draft destination or authorized change. 2\. Recheck obligations, literals, state labels, ownership, qualifications, examples, edge cases, safety constraints, and failure behavior independently of headings. 3\. Verify that moves, consolidations, and routing preserve every meaning and that routing has a confirmed owner, complete destination truth, and sufficient local boundary text. 4\. Restore unaccounted or incompletely preserved content and verify all counts. 5\. Rescan the final draft and report, or questionnaire, for technical literals and repository-dependent claims; recheck each against pinned evidence, repeating bounded negative searches when final wording depends on absence. In a questionnaire, recheck every discrepancy, position, posture, preservation impact, and draft effect; in a report, recheck every repository citation and repository-dependent justification. Static inspection proves checked-in bytes only. Definitions do not prove runtime success; routes do not prove reachability; tests do not prove passage; configuration does not prove deployment; generated artifacts do not prove generation or validation; and bounded absence supports only `not found in the inspected repository`. Do not run tests, services, or deployments or infer runtime state. Classify each material claim internally as: \- `CURRENT IMPLEMENTATION` \- `NORMATIVE REQUIREMENT` \- `PLAN OR PROPOSAL` \- `HISTORICAL` \- `EXAMPLE OR EXPLANATION` \- `ROUTING OR OWNERSHIP` Classify repository relevance as: \- `STATICALLY CONFIRMED` \- `PARTIALLY STATICALLY CONFIRMED` \- `REPO CONTRADICTED` \- `NOT FOUND IN INSPECTED REPOSITORY` \- `NOT REPO VERIFIABLE` \- `NOT APPLICABLE` State implementation only to the extent statically proved and preserve other claim states as their sources establish them. Do not recast requirements as plans, use future tense without source authority, infer future posture from absence, turn discrepancies into tasks without authority, or claim runtime, deployment, external-service, secret, approval, QA, board, or OPS state from static bytes. Keep volatile implementation commentary out of durable normative canon unless the target PF owns it or the brief requires it. Separate materially different states with labels, subordinate headings, or a compact table; do not create empty state headings or silently remove claims to solve state conflicts. \#\# Composition After preservation requirements: \- use direct declarative wording for changed or added text; \- use terms consistently without collapsing materially different contexts; \- put controlling rules before exceptions and examples only when restructuring is authorized; \- use paragraphs for meaning, bullets for discrete rules, and tables for repeated exact comparisons; \- keep content within its owning H1 and add no repetitive selection summary; \- invent no scene-setting, persuasion, transitions, facts, versions, dates, statuses, owners, tokens, paths, commands, examples, acceptance criteria, implementation details, identities, titles, or domain concepts; \- preserve exact identifier and technical-literal casing and spelling; \- do not replace exact contracts, sets, schemas, formulas, byte rules, failure behavior, safety boundaries, topology, or ownership rules with summaries; and \- exclude surrounding document-level material, but preserve such material when it occurs inside the baseline unless removal is independently authorized and accounted for. \# Questionnaire contract Define: \- `BASENAME`: `TARGET_PF_FILE_NAME` with one terminal `.md` removed, if present. \- `SELECTION_TAG`: the supplied number for a single selection, or `<START>-through-<END>` for a range. Name the file: `<BASENAME>-H1-<SELECTION_TAG>-Lead-Dev-Decision-Questionnaire.md` Begin exactly with `# Lead Dev Decision Questionnaire`, followed by `## Selection` and these bullets in order: \- `Target PF:` exact target filename \- `Target PF source:` `Pinned repository: <REPOSITORY>@<pinned commit>:<exact path>` or `ChatGPT Library fallback: <exact Library path and filename, with source version when available>` \- `Mode:` exact mode \- `Requested H1 selection:` exact supplied selection \- `Resolved H1 identities:` exact identities in order \- `Pinned repository commit:` exact commit \- `Draft status: Not created pending Lead Dev decisions.` \- `Change report status: Not created because no draft changes were made.` For each decision, use `## Decision <N>: <concise source-grounded title>` and these bullets in order: \- `Category:` one or more exact categories \- `Affected H1 section(s):` exact identities \- `Affected source unit(s):` exact ledger IDs and source locators when applicable \- `Decision required:` one resolving question \- `Why unresolved:` why authority does not determine the answer \- `Source-grounded positions:` each position with exact source identifier and precise anchor \- `Repository posture:` bounded static finding or `Not applicable` \- `Preservation impact:` content retained, changed, routed, consolidated, or removed under each answer \- `Answer options and draft effect:` mutually exclusive source-bounded options and effects \- `Lead Dev response:` Every labeled field begins with `-` . Nested bullets are allowed only under `Source-grounded positions:`, `Preservation impact:`, and `Answer options and draft effect:`. Use exact source titles when available and the most precise heading, locator, literal, or repository locus; quote only the minimum needed when no structural anchor exists. If bounded options would require invention, request the smallest free-form decision. Leave every response blank. Cover every decision once and distinguish requirements, repository reality, future posture, baseline preservation, and unresolved choice. Include no draft prose, replacement text, provisional resolution, recommendation, implementation plan or task, QA or OPS instruction, access request, or unrelated issue. Do not resume drafting in the same run. End with the final blank `- Lead Dev response:`. \# Change report contract Create this separate file whenever a draft is created. Name it: `<BASENAME>-H1-<SELECTION_TAG>-Change-Report.md` Begin exactly with `# H1 Selection Change Report` and use the following sections in order. \#\# `## Selection` Include these bullets in order: \- `Target PF:` exact target filename \- `Target PF source:` the same exact source format used above \- `Mode:` exact mode \- `Requested H1 selection:` exact supplied selection \- `Resolved H1 identities:` exact identities in order \- `Pinned repository commit:` exact commit \- `Draft file:` exact draft filename \- `Report scope:` `Every baseline source unit and every draft change.` for `REFRESH_H1`, or `Every material addition in the new H1 selection.` for `NEW_H1` \#\# `## Size comparison` For `REFRESH_H1`, include a table with each selected H1 and a total row showing source words, draft words, delta, and signed percentage; then a total-selection table showing source and draft lines and bytes with deltas and percentages. Use the defined counting rules and identify the method or tool without implying runtime PF validation. For `NEW_H1`, state `Not applicable: new section` for source counts and provide draft words, lines, and bytes. \#\# `## Preservation verdict` Include: \- `Source-unit coverage: COMPLETE` \- `Unaccounted baseline source units: 0` \- `Unauthorized destructive changes: 0` \- `Normative-obligation coverage: COMPLETE` \- `Material-reduction gate:` `NOT TRIGGERED` or `TRIGGERED AND PASSED` \- `Draft status: Review artifact only; not applied or approved.` If any verdict is unavailable, do not deliver the package. \#\# `## Source-unit disposition ledger` For `REFRESH_H1`, use: | Unit ID | Source H1 | Exact source locator | Unit type | Claim state | Disposition | Exact draft destination or change ID | Justification and authority | | \--- | \--- | \--- | \--- | \--- | \--- | \--- | \--- | Use stable IDs such as `SRC-0001` and identify each unit by heading path plus a minimal exact opening phrase, row key, list text, or literal. Group only contiguous units with identical disposition, destination, and justification, giving the inclusive ID range and exact endpoint locators. Do not group noncontiguous units or use vague locators or rationales. Every disposition except `RETAINED VERBATIM` cites detailed change IDs; every destructive disposition cites exact authority and passes its test. For `NEW_H1`, state `Not applicable: no prior selected H1 baseline.` \#\# `## Normative-obligation coverage matrix` For `REFRESH_H1`, use: | Obligation ID | Exact source locator | Obligation or critical context | Draft locator or authorized disposition | Related change ID | Verification | | \--- | \--- | \--- | \--- | \--- | \--- | Use stable IDs such as `OBL-0001`. Verification must describe the check, including exact-literal comparison where applicable; a heading match is insufficient. Identify the authorized change for any consolidation, move, routing, or removal. For `NEW_H1`, use the same structure as a source-provenance matrix for every new normative obligation and material context unit, replacing the source locator with its exact allowed source and locator. \#\# `## Detailed change register` Account for every baseline-to-draft difference in `REFRESH_H1` and every material addition in `NEW_H1`. Use one entry per atomic change: `### CHG-<four digits>: <concise factual label>` Include these bullets in order: \- `Affected H1:` exact identity \- `Change type:` `ADDITION`, `CORRECTION`, `NONSEMANTIC EDIT`, `STRUCTURAL EDIT`, `CONSOLIDATION`, `MOVE`, `ROUTING`, `STATUS CHANGE`, or `REMOVAL` \- `Source unit(s):` exact `SRC` IDs, or `Not applicable: new content` \- `Source locator:` exact heading path and anchor, or `Not applicable: new content` \- `Draft locator:` exact heading path and anchor \- `Before:` exact prior text, or `Not applicable: new content` \- `After:` exact replacement text or `Removed` \- `Justification:` why this exact change is required \- `Authority:` exact allowed source and precise locator \- `Repository evidence:` exact pinned locus or `Not applicable` \- `Semantic effect:` all meaning added, removed, narrowed, strengthened, weakened, reclassified, or relocated, or `None` for a proven nonsemantic edit \- `Preservation check:` how unaffected meaning survived \- `Less-destructive alternative:` why no smaller change satisfies authority, or `Not applicable` for an addition or nonsemantic edit For a `Before:` or `After:` block over 200 words, give its exact first and last sentences or lines, exact word count, and applicable unit range instead of the full block. Cover every changed word, meaning-affecting punctuation change, heading change, addition, deletion, consolidation, move, routing decision, and status change. Group identical mechanical changes only when all units and locators are enumerated. Do not group semantic changes as rewrite, cleanup, clarification, or simplification. Editorial preference is not authority; PF03 alone cannot authorize semantic change. Deletions require exact extinction authority, and consolidations or routing must show where every meaning survives. If `REFRESH_H1` has no changes, state: `No changes. The validated selection is reproduced unchanged except for required selected-heading H1 normalization, which is recorded above if applicable.` \#\# `## Destructive-change review` List every `CONSOLIDATION`, `MOVE`, `ROUTING`, `STATUS CHANGE`, and `REMOVAL` ID. For each, summarize all seven tests and identify the retained destination or extinction authority. If none, state `None.` \#\# `## Material-reduction review` If not triggered, state `Not triggered.` If triggered, include the exact trigger; reduction by H1 and subordinate heading; related unit and change IDs; bounded authority for each concentration; confirmation that concision, scope, or generic canonicalization did not authorize it; confirmation that all normative and execution-critical content remains or has an authorized disposition; and the conclusion `PASSED`. Otherwise restore content or create the questionnaire. \#\# `## Validation summary` Include: \- `Baseline reread after drafting: Yes` \- `Draft-to-baseline semantic comparison: Complete` \- `Exact technical-literal preservation check: Complete` \- `Repository-dependent claim recheck: Complete` \- `Source-unit ledger reconciled to draft: Yes` \- `Normative-obligation matrix reconciled to draft: Yes` \- `Every change has a specific justification and authority: Yes` \- `Open Lead Dev decisions: None` End exactly with: `- Change accounting status: COMPLETE` The report is an audit artifact, not approval, and must let a reviewer verify every change without guessing. \# Output contract Name the draft: `<BASENAME>-H1-<SELECTION_TAG>-Draft.md` The draft must begin with the first selected H1; contain each selected identity exactly once in order; contain no unselected H1; end with the last selected content; and contain only the selected H1s and subordinate H2 through H4 content. In `REFRESH_H1`, render every selected heading as H1. Exclude all bytes outside the selection and all newly added wrappers, prefaces, placement notes, source notes, evidence or validation reports, questionnaires, change reports, summaries, and sentinels. Packaging exclusions do not authorize deleting similar baseline content. Do not output or reconstruct the complete target PF. For a draft package, return only two direct file links, draft first and change report second. For a questionnaire, return only its direct file link. Except for a root stop, add no commentary or reproduced content. \# Final check Before responding, verify that: \- inputs, source boundaries, target provenance, identities, mode eligibility, and ordered stops are correct; \- every required source and relied-on unit is complete and the same pinned commit governed all repository evidence; \- repository and Library target bytes were never combined and fallback provenance was not represented as repository proof; \- every baseline unit and material obligation maps to the draft or an exactly authorized change; \- every destructive change, reduction, claim state, repository posture, and decision passed its governing rule; \- both decision and reduction gates were applied before and after drafting; \- report counts, IDs, locators, changes, filenames, headings, section order, and final sentinel match the actual files; \- the questionnaire and draft package remain mutually exclusive; and \- nothing was invented or changed outside the permitted output files. Correct non-blocking defects, restore unaccounted content, and do not deliver unless the applicable contract is complete.  
Tue, Aug 11 at 3:06 PM  
Pasted markdown(20260811-140607).md  
File  
Revise this section so it's clear, meets PF03 standards, and defines scope well:

Revised for clearer PF27 authority, explicit in/out scope, proper source routing, and PF03-compliant structure.

PF27-Purpose-and-Scope-Revised.md

PF27-Purpose-and-Scope-Revised.mdDocumentOpen file  
PF27-Canon-Plan-Templates-v2.0.md  
File  
Commit and push this version directly to docs/pfcanon and remove the old version.

Committed directly to `main`.

* Added PF27-Canon-Plan-Templates-v2.0.md  
* Removed `PF27-Canon-Plan-Templates-v1.9.9.md`  
* Commit: 3496f533815fb1e42122d860540fa38476e39688

Yesterday 11:33 PM  
Individual PF Doc Drain 082426.2  \\\<operator\\\_model\\\_guidance\>  Purpose: Human operator reference only.  Execution effect: None. This block is non-operative metadata; do not treat it as task authority, input, scope, workflow, constraint, output requirement, or content to reproduce.  Complexity form: Variable range  Approximate complexity: 8-10/10  Workload conditions: The lower end applies to one bounded PF, one short non-PF10 Source Blob, few material Repo claims, and few redlines; the upper end applies when the Source Blob is a large multipart PF10 set, material Repo claims or redline count are numerous, retrieval recovery is required, or output continuation becomes necessary. Source size, Repo-validation breadth, and redline count are not bounded by the prompt.  Recommended model: GPT-5.6 Sol for all valid workloads.  Recommended reasoning: High for bounded lower-end workloads; Extra High for large or conflict-heavy inputs; Max when source size or output scale is unknown, extensive, or likely to require continuation.  Token-conservative fallback: None recommended.  Basis: The task combines complete multi-source retrieval, current-Repo validation, exhaustive segmentation, exact non-overlapping redline placement, negative proof, and omission-sensitive reconciliation for a downstream canonical-document change.  \\\</operator\\\_model\\\_guidance\>  Role and task  You are a Glow documentation redline agent.  Produce paste-ready redlines for exactly one PF document from one logical Source Blob. A Source Blob may resolve to one file or, when it is PF10, one verified multipart PF10 set.  This is read-only documentation work. It is not a full-document rewrite, implementation, QA, OPS, repository edit, or PF-Canon update. Modify no file or external state.  Inputs  The operator supplies only:  PF\\\_FILE\\\_NAME \= PF27-Canon-Plan-Templates-v2.0 SOURCE\\\_BLOB\\\_FILE\\\_NAME \= PF10-HDE-Build-Notes-v12.8.9.md PF10\\\_ADDENDUM\\\_RANGE \= ""  Request no other input interactively.  A filename must be one non-empty basename containing no /, \\\\, parent reference, or URI.  PF10\\\_ADDENDUM\\\_RANGE may be empty. Otherwise, it must identify one exact PF10 addendum or one inclusive PF10 addendum range, such as:  Addendum 2.31 through Addendum 2.38  Fixed configuration:  \- Repository: amthorn78/glow-hdengine-v2  \- PF-Canon root: docs/pfcanon  Derive from complete source headers:  \- PF\\\_ID: the initial PF identifier.  \- PF\\\_EDIT\\\_TARGET: the complete PF title.  \- PF\\\_HEADER\\\_VERSION: the visible version line, or Unknown (not stated in PF).  \- READ\\\_SCOPE: the complete selected non-PF10 Source Blob file or complete verified PF10 set.  \- TRIGGER\\\_SCOPE: the portion of READ\\\_SCOPE permitted to trigger redlines, as defined below.  Use SOURCE\\\_BLOB\\\_SCOPE instead of SRC IDs only when unresolved Source Blob structure or boundaries prevent reliable IDs.  Ordered root stops  These outputs override every other output rule. Return only the first applicable line:  1\. PF\\\_FILE\\\_NAME is invalid, unresolved, ambiguous, non-PF, or cannot be retrieved completely after permitted resolution and recovery:  MISSING INPUT: PFXX  2\. SOURCE\\\_BLOB\\\_FILE\\\_NAME is invalid, unresolved, ambiguous, or cannot be retrieved completely after permitted resolution and recovery:  MISSING INPUT: SOURCE\\\_BLOB  3\. PF10\\\_ADDENDUM\\\_RANGE is non-empty and the resolved Source Blob is not PF10:  INVALID INPUT: PF10\\\_ADDENDUM\\\_RANGE  Repository failure is not a root stop when fallback resolves the affected source completely. Any material current-Repo claim still requires Repo validation or a Repo validation blocker.  Source resolution and baseline  Terminal versions  A terminal filename version is:  \- v;  \- followed by dot-separated integers;  \- followed optionally by an alphabetic suffix;  \- located immediately before .md;  \- and optionally preceded by a hyphen or space.  Independent resolution  Resolve the PF and Source Blob independently at the repository default-branch HEAD.  For each requested source:  4\. Enumerate matching regular files under docs/pfcanon.  5\. Honor one unique exact basename, including an exact older version.  6\. Otherwise, remove only the terminal version from the requested basename and candidate basenames and retain exact normalized-basename matches.  7\. Never use fuzzy identity.  8\. Read all candidate headers completely; header identity and version control resolution.  For a non-PF10 source:  \- Select the sole candidate; or  \- select the unique highest numeric header version only when every candidate header establishes one identity and document control names no different current version.  For PF10:  9\. Group candidates by numeric header version.  10\. Treat alphabetic suffixes as ordered parts only when complete headers or document control prove common identity, version, set membership, completeness, and order.  11\. Select the sole or unique highest verified complete set.  12\. Never infer set membership from filenames.  13\. Never select only the final part, combine numeric versions, or omit a verified part.  Retrieval channels  Retrieve every selected logical source completely from one channel.  Use this order independently for the PF and Source Blob:  14\. Repository at the pinned commit.  15\. After no more than two materially different failed Repository attempts for that source, Project Sources.  16\. If still unresolved, ChatGPT Library under the same identity, version, completeness, and PF10-set rules.  Stop at the first complete, unique resolution.  Do not:  \- replace complete Repository content with fallback content;  \- combine channels, fragments, versions, or unverified PF10 parts within one logical source;  \- rely on previews, summaries, caches, memory, similar files, or undeclared locations; or  \- represent fallback content as Repository evidence.  The PF and Source Blob may resolve through different channels, but each logical source must come completely from one channel.  Fallback establishes source content only. It proves no Repository state.  Fixed baseline  Before analysis, fix one baseline containing:  \- default branch and exact commit;  \- repository inventory used for resolution;  \- resolved PF and Source Blob identity;  \- selected PF10 membership and order, if applicable;  \- provenance and retrieval failures;  \- PF10\\\_ADDENDUM\\\_RANGE;  \- range boundaries;  \- READ\\\_SCOPE;  \- TRIGGER\\\_SCOPE; and  \- complete Source Blob structure.  Pin all Repository reads to the same commit even if HEAD changes.  Restart all dependent work after:  \- an unpinned Repository read;  \- a source-resolution change;  \- a fallback-channel change; or  \- later Repository recovery that replaces fallback content.  Authority and scope  Use only the resolved PF, resolved Source Blob, and pinned Repository.  Source roles are:  \- PF: sole edit target and authority for its original text, structure, terminology, and placement anchors.  \- TRIGGER\\\_SCOPE: sole change trigger.  \- Repository: validation authority only for material current-Repo facts.  \- Fallback channels: content retrieval only; they add no authority.  Repository inspection may prove current paths, files, commands, tests, artifacts, schemas, configurations, routes, modules, refs, and Git state.  Repository evidence cannot create canon, PF ownership, QA PASS, OPS completion, PF09 Done, acceptance, token satisfaction, or closeout.  Neither Repository findings nor PF10 content outside TRIGGER\\\_SCOPE may independently trigger a redline.  Read the PF end-to-end.  From the PF, derive:  \- header identity;  \- header version; and  \- the earliest complete scope passage containing two to six contiguous lines.  If no qualifying PF scope passage exists, use exactly:  Unknown (not stated in PF)  PF10 read and trigger scope  Read every file in READ\\\_SCOPE end-to-end before segmentation.  TRIGGER\\\_SCOPE is:  \- the complete Source Blob document for non-PF10;  \- the complete verified PF10 set when PF10\\\_ADDENDUM\\\_RANGE is empty;  \- the complete named addendum when the range names one exact addendum; or  \- every authored addendum from the named first addendum through the named last addendum, inclusive.  For a bounded PF10 range:  \- determine the start at the first exact requested same-level addendum heading;  \- determine the end immediately before the next same-level addendum heading following the last requested addendum, or at document-set end;  \- follow a different boundary rule only when the PF10 set explicitly defines one;  \- read and account for the entire verified set;  \- segment only the bounded range; and  \- use outside-range material only to clarify terms, IDs, references, dependencies, conflicts, supersession, order, or boundaries.  Report material effects of consulted outside-range context, but create no outside-range segment or disposition.  An absent, repeated, malformed, reversed, or non-unique requested boundary requires retrieval recovery. If still unresolved, create a Retrieval blocker using SOURCE\\\_BLOB\\\_SCOPE.  Retrieval integrity  A complete source or unit must be read in full.  Do not rely on snippets, previews, summaries, filenames, unopened links, partial OCR, prior-context remnants, ellipsized output, or memory.  Treat cutoffs, broken structure, broken tables, missing chunks, or text ending mid-unit as retrieval failure unless the source expressly contains an authored truncation marker.  For each incomplete source or unit:  17\. Stop relying on it.  18\. Make no more than two materially different source-appropriate recovery attempts.  19\. Do not repeat a failed route.  20\. After successful recovery, reread the complete unit and redo every dependent decision.  21\. Do not infer absence from failed retrieval.  Recovery limits apply independently to each source, source unit, and Repo claim.  An unresolved whole-source failure invokes the applicable root stop.  For any other unresolved retrieval dependency, record:  Retrieval blocker | source=\[source\] | unit=\[unit\] | required because=\[reason\] | incomplete because=\[failure\] | attempts=\[attempts/results\] | PO input=\[smallest need\] | SRC=\[SRC IDs or SOURCE\\\_BLOB\\\_SCOPE\] | SEG=\[SEG IDs or NONE ASSIGNED\]  Internal Source Coverage Ledger  Before segmentation, create one complete internal Source Coverage Ledger.  Source units  22\. Inventory every Markdown heading in file and source order.  23\. Treat pre-heading content as DOCUMENT START (front matter).  24\. Treat a headingless file as DOCUMENT WITHOUT AUTHORED HEADINGS.  25\. Define one unit as a heading plus all content through immediately before the next heading of any level.  26\. Keep tables, lists, quotations, fences, and blank lines in their containing unit.  27\. Assign every source line to exactly one non-overlapping unit.  28\. For bounded PF10 work, classify every unit as IN or OUT.  Treat document control, contents tables, separators, and empty parent headings as structural only. They receive no actionable ID or segment and do not prevent completion.  Source and segment IDs  Assign SRC-001 onward, in source order, only to:  \- substantive IN units;  \- materially consulted OUT units; and  \- incomplete blocked units.  During segmentation, assign SEG-001 onward in source order.  Each segment must map to exactly one primary SRC.  Each substantive in-scope SRC must map to at least one segment.  Keep the ledger internal. Output only:  \- reconciliation counts;  \- materially consulted outside-range headings;  \- dispositions;  \- retrieval blockers; and  \- Repo validation blockers.  Do not output unaffected outside units, processed-segment bookkeeping, or pagination cursors. Unprinted internal audit rows cannot require continuation or prevent END OF REDLINES.  Segmentation and dispositions  Segment only TRIGGER\\\_SCOPE.  A segment is the smallest independently decidable and placeable:  \- requirement;  \- correction;  \- canon delta;  \- material current-Repo claim; or  \- PF-relevant observation.  Split content requiring unrelated operations or placements. Combine segments only when one operation at one placement completely handles them.  Assign each segment exactly one disposition:  \- Redline  \- Already present  \- Out of scope  \- Retrieval blocker  \- Repo validation blocker  Already present  Use Already present only when the PF contains the complete effective Source Blob requirement or the complete Repo-corrected meaning and no change remains.  Similar terminology or partial coverage is insufficient.  Record the minimum verbatim PF line or lines needed to prove complete equivalence. When complete proof requires separated passages, use multiple concise proof records for the same segment.  Out of scope  Use Out of scope only when the exclusion is grounded in the PF title, structure, and verbatim scope passage.  Do not use Out of scope because:  \- a Repository premise is false;  \- placement is difficult; or  \- required proof is missing.  The Source Blob remains the change trigger when Repository inspection corrects a material premise.  Repository validation  Validate only material current-Repo claims that affect a disposition or paste-ready text.  Deduplicate claims, batch related inspections, and reuse proof.  Inspect the pinned baseline commit read-only and only as broadly as required.  Do not:  \- run QA or OPS;  \- edit;  \- install;  \- start services;  \- deploy;  \- migrate;  \- regenerate artifacts; or  \- call external services.  Assign each validated claim one posture:  \- Repo-confirmed  \- Repo-contradicted  \- Repo-partially-confirmed  \- Repo-not-found  \- Not repo-verifiable  Repository evidence controls conflicting current-Repo wording. Surface the conflict and redo dependent dispositions and redline text.  Use this positive proof format:  Repo validation | ref=\[branch/commit\] | path/method=\[value\] | result="\[verbatim line or short observation\]"  Use this negative proof format:  Repo search | commit=\[commit\] | query="\[pattern\]" | case=\[sensitive/insensitive\] | scope="\[roots\]" | method=\[search/tree/complete scan\] | result=\[0/N hits\]  Use Repo-contradicted or Repo-not-found only when supported by negative proof.  Before creating a Repo validation blocker, make no more than two materially different attempts using exact terms and the narrowest sufficient scope.  Record an unresolved material Repo dependency as:  Repo validation blocker | claim=\[claim\] | required because=\[reason\] | attempts=\[attempts/results\] | PO input=\[smallest need\] | SRC=\[SRC IDs\] | SEG=\[SEG IDs\]  Redline construction  Allowed change types:  \- NEW CANON  \- CANON UPDATE  \- CLARIFICATION  \- CONSISTENCY  \- DOC HYGIENE  \- DELETION  Allowed operations:  \- INSERT  \- REPLACE  \- DELETE  Each redline must contain only:  \- redline number;  \- SEG IDs;  \- change type and operation;  \- one to three contiguous verbatim Source Blob trigger lines;  \- Repo basis only when Repository evidence controls wording;  \- one rationale; and  \- one independently executable placement instruction against the complete original PF.  Each redline must be independently executable against the original PF without applying another redline first.  Redline targets and replacement or deletion ranges must not overlap.  Preserve PF terminology and style.  Do not invent any requirement, structure, Repository fact, status, owner, token, date, or version.  Include a Repository locus only when the Source Blob grounds it and Repository inspection validates it.  PF document control is read-only unless an in-scope segment explicitly requires its correction. Filename or header drift alone does not trigger a redline.  Placement requirements  Every placement instruction must include:  29\. The full authored Markdown heading path from the outermost heading through the target section, copied verbatim with heading markers.  30\. If the PF has no authored headings, Document region: ENTIRE ORIGINAL PF.  31\. A direct imperative stating exactly what to insert, replace, or delete.  32\. Whether each named boundary is retained or included in the operation.  33\. Only the exact original-PF boundary lines required for the operation.  34\. Exact uniqueness proof.  section-path matches is the count of exact paths in the parsed heading tree.  Each boundary count is its exact occurrence count within that section.  Every reported uniqueness count must equal 1\.  INSERT  Provide:  \- the complete verbatim line immediately before the gap; and  \- the complete verbatim line immediately after the gap.  Each boundary must occur exactly once within the identified section.  Direct the editor to insert between those lines and retain both unchanged.  Paste text must include every intended leading and trailing blank line.  When the required insertion is at the beginning or end of a document or section and two surrounding boundary lines do not exist, do not use INSERT. Use REPLACE over the smallest unique boundary range and preserve the original boundary text unchanged within the replacement.  REPLACE  Provide only:  \- the complete verbatim first line of the original range; and  \- the complete verbatim last line of the original range.  Each boundary must occur exactly once within the identified section.  Direct the editor to replace both boundary lines and everything between them, inclusively, exactly once with the complete replacement.  Do not reproduce the intervening original block outside the replacement text.  DELETE  Provide only:  \- the complete verbatim first line of the original range; and  \- the complete verbatim last line of the original range.  Each boundary must occur exactly once within the identified section.  Direct the editor to delete both boundary lines and everything between them, inclusively, exactly once.  Delete no text outside those boundaries.  Non-unique placement  If a heading path or boundary line is not unique:  35\. Do not use an occurrence ordinal, generic disambiguation excerpt, or full reproduced original block.  36\. Select the smallest wider range whose first and last lines are each unique within one uniquely identified section.  37\. When that wider range contains unchanged text, use REPLACE and preserve the unchanged text in the replacement.  38\. If independently executable unique boundaries still cannot be proved after recovery, create a Retrieval blocker and emit no ambiguous redline.  Never use \[SNIP: lines omitted\].  Output contract  Except for root stops, output only the redline document.  Do not add commentary, questions, code fences, unresolved placeholders, empty bullets, or sample labels.  Use Markdown headings only for individual redlines and Coverage Notes.  Begin exactly:  REDLINES FOR \[actual PF\\\_ID\]  PF: "\[verbatim header title\]"  Version: "\[verbatim version line or Unknown (not stated in PF)\]"  Scope (PF verbatim, 2 to 6 contiguous lines):  "\[verbatim lines or Unknown (not stated in PF)\]"  Number redlines consecutively beginning with Redline 001\.  For each redline, use the common fields followed by exactly one applicable operation form.  Redline 001  Segments: \[SEG IDs\]  Change: \[type\] | Operation: \[INSERT/REPLACE/DELETE\]  Source trigger (verbatim, 1 to 3 contiguous lines):  "\[lines\]"  \[Include only when Repository evidence controls wording:\]  Repo basis:  \[one proof record\]  Rationale: \[one or two source-grounded sentences\]  PLACEMENT INSTRUCTION  INSERT form  Section path (PF verbatim, outermost to target): "\[heading\]" \> "\[heading\]"  Action: Within the section identified above, insert TEXT TO INSERT immediately after PRECEDING BOUNDARY and immediately before FOLLOWING BOUNDARY. Keep both boundary lines unchanged. Apply this insertion once.  Uniqueness proof: section-path matches=1 | preceding-boundary matches within section=1 | following-boundary matches within section=1  PRECEDING BOUNDARY (PF verbatim; retained): "\[exact complete line immediately before the gap\]"  FOLLOWING BOUNDARY (PF verbatim; retained): "\[exact complete line immediately after the gap\]"  TEXT TO INSERT  \[exact insertion\]  END TEXT TO INSERT  REPLACE form  Section path (PF verbatim, outermost to target): "\[heading\]" \> "\[heading\]"  Action: Within the section identified above, replace from FIRST BOUNDARY LINE through LAST BOUNDARY LINE, inclusive, exactly once with REPLACEMENT TEXT. Replace no other text.  Uniqueness proof: section-path matches=1 | first-boundary-line matches within section=1 | last-boundary-line matches within section=1  FIRST BOUNDARY LINE (PF verbatim; unique within section; included): "\[exact first original line\]"  LAST BOUNDARY LINE (PF verbatim; unique within section; included): "\[exact last original line\]"  REPLACEMENT TEXT  \[complete replacement\]  END REPLACEMENT TEXT  DELETE form  Section path (PF verbatim, outermost to target): "\[heading\]" \> "\[heading\]"  Action: Within the section identified above, delete from FIRST BOUNDARY LINE through LAST BOUNDARY LINE, inclusive, exactly once. Delete no other text.  Uniqueness proof: section-path matches=1 | first-boundary-line matches within section=1 | last-boundary-line matches within section=1  FIRST BOUNDARY LINE (PF verbatim; unique within section; included): "\[exact first original line\]"  LAST BOUNDARY LINE (PF verbatim; unique within section; included): "\[exact last original line\]"  Use only the applicable operation form for each redline. Do not print the form headings INSERT form, REPLACE form, or DELETE form.  Coverage Notes  After all emitted redlines, output:  Coverage Notes  Resolution:  \- Repository: amthorn78/glow-hdengine-v2  \- Inspected ref: "\[default branch and commit, or Unavailable\]"  \- PF: requested="\[input\]" | resolved="\[Repo path at commit or fallback channel and file\]" | fallback="\[None or Repo failure\]"  \- Source Blob: requested="\[input\]" | resolved="\[Repo path or verified set at commit or fallback channel and identity\]" | fallback="\[None or Repo failure\]"  Scope:  \- PF10 range: "\[input or None\]"  \- Read scope: \[COMPLETE FILE or COMPLETE VERIFIED PF10 SET\]  \- Trigger mode: \[FULL\\\_DOCUMENT or PF10\\\_ADDENDUM\\\_RANGE\]  \- Boundaries: start="\[heading or document start\]" | end="\[next heading or document end\]"  Reconciliation:  files=\[N\] | headings=\[N\] | units=\[N\] | in scope=\[N\] | substantive in scope=\[N\] | structural only=\[N\] | outside range=\[N\] | consulted outside=\[N\] | unaccounted=\[N\]  segments=\[N\] | redline=\[N\] | already present=\[N\] | out of scope=\[N\] | retrieval blocked=\[N\] | repo blocked=\[N\] | unprocessed=\[N\]  redlines drafted=\[N\] | emitted=\[N\] | next=\[Redline \#\#\# or None\]  Outside-range context consulted:  \[heading or ID\] | affected=\[SEG IDs\] | effect=\[purpose\]  or:  None.  Already present:  SEG-\#\#\# | PF proof="\[minimum verbatim line or lines proving complete equivalence\]"  Use additional proof records for the same segment when separated PF passages are required.  If none:  None.  Out of scope:  SEG-\#\#\# | reason="\[PF-scope-grounded reason\]"  If none:  None.  Retrieval blockers:  \[records\]  or:  None.  Repo validation blockers:  \[records\]  or:  None.  Do not output:  \- the internal Source Coverage Ledger;  \- unaffected outside-range units;  \- a processed-segment ledger; or  \- bookkeeping cursors.  Every segment must appear exactly once as:  \- part of one emitted redline; or  \- one reported non-redline disposition; or  \- one reported blocker.  All counts must reconcile.  Final sentinel and completion  End with exactly one sentinel, using this precedence:  39\. Drafted redlines remain unprinted only because of response capacity:  CONTINUE REDLINE OUTPUT: Redline \#\#\#  40\. All drafted redlines are printed and both blocker classes remain:  BLOCKED: RETRIEVAL \[SRC IDs or SOURCE\\\_BLOB\\\_SCOPE\] | REPO VALIDATION \[SEG IDs\]  41\. All drafted redlines are printed and only Retrieval blockers remain:  BLOCKED: RETRIEVAL \[SRC IDs or SOURCE\\\_BLOB\\\_SCOPE\]  42\. All drafted redlines are printed and only Repo validation blockers remain:  BLOCKED: REPO VALIDATION \[SEG IDs\]  43\. Otherwise:  END OF REDLINES  END OF REDLINES is permitted only when:  \- all required logical sources were retrieved completely and coherently;  \- the PF and complete READ\\\_SCOPE were read;  \- every substantive in-scope SRC maps to at least one segment;  \- every segment maps to one primary SRC;  \- every segment has exactly one reported disposition;  \- every drafted redline was emitted;  \- every required Repo, placement, and proof gate passed;  \- unaccounted=0;  \- unprocessed=0; and  \- no Retrieval or Repo validation blocker remains.  Completion never depends on printing the internal ledger, unaffected outside-range units, empty headings, or internal audit rows.  For continuation:  \- preserve the complete baseline and cumulative counts;  \- preserve redline numbering;  \- repeat no redline;  \- output only the remaining redlines;  \- output cumulative Coverage Notes; and  \- end with the applicable sentinel.  Final internal check  Before responding:  44\. Apply the ordered root stops.  45\. Confirm exact source resolution, provenance, and complete coherent reads.  46\. Confirm the pinned Repository baseline and PF10 set order and boundaries.  47\. Reconcile every substantive in-scope source unit and segment.  48\. Confirm each segment has one primary source and one disposition.  49\. Confirm Repository validation is material, deduplicated, source-grounded, and pinned.  50\. Correct every Repo conflict in dependent decisions and paste-ready wording.  51\. For each redline, confirm:  \- section-path matches equal 1;  \- each boundary count equals 1;  \- the action matches the operation;  \- inclusive boundaries are identified correctly;  \- only necessary original boundary lines are reproduced outside replacement text;  \- insertion boundaries are retained;  \- replacement text preserves any intentionally unchanged widened content;  \- redlines do not overlap; and  \- no redline depends on another redline.  52\. Confirm PF document-control restrictions.  53\. Apply the single completion predicate and output the truthful sentinel.  Correct any non-blocking failure before responding. 

REDLINES FOR PF27

PF: "PF27-Canon-Plan-Templates"

Version: "v2.0"

Scope (PF verbatim, 2 to 6 contiguous lines):

"PF27 is the canonical home for reusable plan, runbook, review, and closeout templates used across Glow, including the HDE workstream. It defines the structure and template-level controls required to make derived artifacts complete, reviewable, portable, executable where execution is in scope, and aligned with the applicable canon.

PF27 governs template requirements. It does not own the implementation facts, technical contracts, project state, or acceptance semantics that a completed artifact records."

## **Redline 001**

Segments: SEG-012

Change: NEW CANON | Operation: REPLACE

Source trigger (verbatim, 1 to 3 contiguous lines):

"Source-bound reviewers must not create technical design merely to satisfy an output contract requiring exact fixes, complete decisions, or paste-ready wording. When the permitted sources do not establish an execution-critical identifier or design choice, the reviewer must report the missing decision or information through the task’s authorized failure disposition. The reviewer must not manufacture the missing design."

Rationale: PF10 requires source-bound reviewers to report missing decisions rather than invent execution-critical design. PF27’s reusable review guardrails need an explicit authority boundary and invalid-review recovery rule.

PLACEMENT INSTRUCTION

Section path (PF verbatim, outermost to target): "\# A) Glow Plan and Runbook Templates" \> "\#\# **Review guardrails**"

Action: Within the section identified above, replace from FIRST BOUNDARY LINE through LAST BOUNDARY LINE, inclusive, exactly once with REPLACEMENT TEXT. Replace no other text.

Uniqueness proof: section-path matches=1 | first-boundary-line matches within section=1 | last-boundary-line matches within section=1

FIRST BOUNDARY LINE (PF verbatim; unique within section; included): "\#\# **Review guardrails**"

LAST BOUNDARY LINE (PF verbatim; unique within section; included): "\#\#\# **Hard blockers for plan approval/execution**"

REPLACEMENT TEXT

## **Review guardrails**

### **Source-bound review authority and exact-fix limits**

A source-bound review does not authorize the reviewer to design new technical surfaces. An instruction to provide exact fixes, complete decisions, or paste-ready wording does not expand the permitted sources or the reviewer's authority.

A reviewer MUST NOT originate an execution-critical path, filename, directory or component home, command, script, module, tool, test, CLI option, environment variable, endpoint, route, provider, service, configuration key, token or alias, schema field, artifact-family or evidence identity, manifest binding, producer, validator, writer, check-mode interface, or acceptance predicate unless the item is established by the artifact under review, applicable live HDE Build Notes, controlling permanent canon, an approved Product Owner decision, or verified repository reality for an existing item.

Existing parent directories, neighboring artifacts, naming patterns, similar commands, reusable tools, or prior conventions prove only the inspected fact. They do not authorize a reviewer to mint a new identifier or interface. Similar spelling, a shared prefix, an acronym, filename resemblance, or semantic association does not prove equivalence.

If a safe correction requires an unestablished design choice, the review MUST use the task's authorized `NEEDS REVISION`, `Unverifiable`, Blocker, rejection, or missing-information disposition and identify the missing decision or source. The reviewer MUST NOT manufacture the design to complete the output.

Every execution-critical identifier in required fix text MUST map to an allowed source. Reviewer-created design is not an authority basis. A finding containing reviewer-invented technical design is invalid, as is any dependent required fix, ADR or Tracked Issue disposition, approval recommendation, or final decision. If the defect is systemic or affects the final posture, discard the review and rerun it from the unchanged inputs; do not repair unsupported text through post hoc justification.

### **Hard blockers for plan approval/execution**

* Live QA Plans and runbooks MUST NOT require equality to a preplanned Git commit as a readiness, behavior, routing, or PASS predicate. Source identity is execution provenance. The plan MUST require capture of actual execution-source identity in governed evidence, validation of the required current code posture, and preservation of routing provenance. This rule does not waive clean-source checks, authorization-bound source identity, routed-artifact provenance, OPS source binding, or exact-source release-attestation verification.  
    
* PF07-derived / PF07-gap infrastructure posture (required). Any plan, implementation guide, QA plan, review artifact, remediation guide, runbook, or epic document that includes an infrastructure fact or dependency MUST use exactly one posture:  
    
  * `PF07-derived`: cite the exact PF07 fact and locator for every required provider, project, service, repository, base URL or port, database instance or schema, config key, governed evidence root, start command, or other applicable infrastructure value.  
  * `PF07-gap`: identify the exact missing PF07 fact set, block the affected step or claim, and record the PF07 update as a drain or doc-delta target. Do not guess.


* Placeholder external-ownership language is non-conforming. Plans and related documents MUST NOT use phrases such as “infra to provide”, “ops to confirm”, “ask infra”, “await ops details”, guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or placeholder external ownership without a concrete PF07-backed value or an explicit PF07-gap statement.  
    
* QA plans and Live QA runbooks MUST NOT guess or redefine environment bindings that PF07 is meant to own. This includes, as applicable, active bindings such as `DEV_SAMPLER_URL`, `HDE_BASE_URL`, `DATABASE_URL`, production service base URLs, environment-specific host and port bindings, and canonical QA-root patterns. For HDE database access, `DATABASE_URL` is the sole active endpoint key and direct PostgreSQL through the Glow-owned psycopg provider is the sole active transport. Retired bridge names `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` may appear only as names-only historical evidence or configuration-drift inputs; plans and runbooks MUST NOT require, provision, restore, consume, or treat them as valid HDE runtime inputs, and MUST NOT treat their absence as an error, degraded state, discovery ambiguity, or acceptance failure. A Codespaces execution venue does not create a second database service, hostname, provider, transport, or evidence lane.  
    
* Default documented dev and QA access address (required). When a plan, implementation plan, QA plan, remediation guide, review, runbook, example command, or inline documentation needs to show a non-prod local-style client access address, it MUST use `127.0.0.1` as the default host, plus the correct port and endpoint path.  
    
* This default does not replace canonical config keys, infra wiring, or per-environment configuration. It is a documented client access convention only.  
    
* `127.0.0.1` in these templates is not a service identity claim and not a server bind requirement. Real provider, project, service, base URL, and config-key identity remain governed elsewhere, and services may still bind to `0.0.0.0`, `$PORT`, or another infra-owned target when that is the correct runtime posture.  
    
* When a QA console or runbook targets a real production service, that surface MUST be documented with the real production address even if the operator is in Codespaces, CI, or another remote shell.  
    
* Production and other prod-facing surfaces MUST keep the real hosted service URL or other real infrastructure address. Do not rewrite prod-facing targets to `127.0.0.1`.  
    
* `localhost` is not the preferred canonical example host for new or revised dev and QA documentation in these templates.  
    
* If a dev or QA surface cannot truly be reached at `127.0.0.1` from the intended operator context, the document MUST state an explicit exception and the real access route. Do not guess hostnames, forwarded URLs, ports, config keys, start commands, or endpoints.  
    
* Markdown-only wrapper differences in planning and review artifacts are non-blocking when the same required field name, content, ordering or adjacency, and meaning remain present, and no executable command, code, schema, JSON, token spelling, path string, endpoint string, or other machine-sensitive literal is altered. Reviewers may note those differences as optional cleanup only.  
    
* Markup that changes meaning, hides required text, or alters machine-sensitive content remains blocking.  
    
* Approval-submitted planning artifacts MUST include the literal approval sentinel `ASK OK?`. The sentinel is required and non-blocking by default, and reviewers MUST NOT classify it as stray text, formatting noise, or a blocker merely because it appears in the document. Missing the required sentinel remains blocking.  
    
* The plan sentinel `ASK OK?` is distinct from a reviewer final decision line such as `ASK OK`; do not conflate those surfaces.  
    
* Structural template completeness is gating. Missing required sections or required structural blocks (including required end markers and required gates) is blocking. Where a template requires canon pointers (for example PF09 or PF14 pointers), missing pointers are blocking. Invalid non-PF references and ungrounded existence claims are blocking.  
    
* Plans MAY consult PF documents during planning and review, and MAY note drain targets or doc-delta candidates as explicitly non-mandatory follow-up intents for PO, but PF10 drainage and any other PF-canon drainage are never execution conditions, approval conditions, completion conditions, required deliverables, required checks, acceptance criteria, or blockers for the current plan, review, QA step, OPS task, or closeout artifact. Reality Audits updates are PO-only.  
    
* PF09 task accountability for task-like items (required). Epic Plans, Implementation Plans, QA Plans, remediation plans, QA-readiness reviews, retrospectives, closure reviews, and future-work sections MUST NOT create free-floating task-like backlog. Every task-like item affecting implementation, QA, OPS, runtime, evidence, vendor behavior, architecture, product behavior, build improvements, adapter gaps, runtime gaps, QA-discovered gaps, OPS-discovered gaps, or post-epic recommendations MUST resolve to exactly one of: exact phased PF09 task/subtask mapping, PF09 gap, out of HDE phased build scope, or documentation/status drainage only.  
    
* Backlog, future work, deferred work, optional work, follow-up work, later, not now, and not in current epic are scheduling or disposition postures, not PF09 accountability substitutes. If a task-like item is moved out of the current epic, it still MUST carry the phased PF09 document, task ID, subtask ID where one exists, disposition, reason it is not included now, and whether a PF09 gap exists.  
    
* If a PF09 parent task exists and relevant subtasks exist, subtask-level mapping is required. Parent-task-only mapping is invalid unless no relevant subtask exists.  
    
* If the PF09 mapping cannot be proven, classify the item as PF09 gap rather than placing it into backlog, future work, later work, or recommendation text without mapping.  
    
* Documentation drainage, PF09 status drainage, board updates, closeout summaries, archive entries, and PF-canon reconciliation may be classified as documentation/status drainage only when they are not implementation, QA, OPS, runtime, evidence, vendor, product, or architecture work. If a doc delta describes future implementation, QA, OPS, runtime behavior, evidence behavior, vendor behavior, or product behavior, the underlying task-like item remains PF09-accountable.  
    
* PR-slice completion discipline (required). When a plan, remediation guide, or review record claims that a PR slice or remediation lane is complete or acceptable, it MUST account for every assigned HDE Build Checklist subtask. If one or more assigned subtasks are not complete, the document MUST identify each affected subtask ID, state exactly what was completed, state exactly what remains incomplete, describe the blocking condition or limiting constraint, explain why completion was not possible within the approved scope, and name the repo evidence, test result, or other concrete basis for that conclusion. Silent omission, partial completion without this explanation, or claiming completion while assigned subtasks remain unresolved is non-conforming.  
    
* Review and closure posture for mapped PF09 work (required). Current PF09 recorded status text is not a pre-drain acceptability gate, closure gate, QA-entry gate, or OPS acceptability gate. When a plan, remediation guide, QA-readiness review, closeout review, or approval artifact evaluates mapped PF09.x work, the controlling question is whether the mapped work is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review artifacts, plus PF10 live truth where PF10 explicitly speaks.  
    
* Combined-evidence supportability decisions (required). When live PF10 records that individually accepted PR or OPS slices intentionally did not move a mapped PF09.x row, a later plan, review, QA-readiness artifact, closeout artifact, or approval artifact may rely on a PF10-recorded combined-evidence supportability decision only if it identifies the exact slices combined, the mapped PF09.x row or subtask, the row’s substantive proof burden, the slice-local no-move conditions, what each slice proves, and the live PF10 conclusion. Prior slice-local no-status-move language must be preserved as slice-local truth, not treated as a prohibition against a later combined-evidence supportability decision.  
    
* Combined-evidence non-claim boundary (required). A combined-evidence supportability decision MUST state what it does not claim, including whether PF09.x has already been drained, QA has passed, the epic is closed, live vendor behavior has been proven, vendor-version runtime conformance has been completed, unregistered proof labels have become acceptance tokens, OPS evidence has become QA evidence, or any individual PR or OPS slice alone moves PF09.x status.  
    
* Exact mapping control (required). If a slice maps to an exact PF09.x subtask, that subtask is the controlling unit. If a slice claims to close more than one mapped PF09.x subtask, each claimed subtask must be complete in substance before acceptable-status language is allowed.  
    
* PF10 reopened-subtask planning rule (required). When current PF10 explicitly reopens, rebinds, or names active HDE Build Checklist subtasks for an epic, Epic Plans, QA Plans, remediation guides, and reviews MUST treat the exact subtask IDs as active scope unless a later PF10 addendum reverses that posture. Broader parent-task history-only wording MUST NOT suppress an exact subtask row that PF10 names as active.  
    
* Truth constraint for reopened scope (required). A reopened or rebound subtask is not automatically complete. Plans and reviews MUST preserve the current truth of its status and MUST NOT claim runtime facts are already true merely because the row is in scope. If active-scope and current-status text conflict, record the issue as a PF09.x doc-delta candidate or later-drain item rather than deferring the subtask by assumption.  
    
* Reused-history separation rule (required). When a plan or review distinguishes reused-history rows from active epic rows, it MUST list those categories separately, state whether any new implementation is being claimed for reused-history rows, and treat a false new-implementation claim as part of the evidence posture rather than as active-scope completion.  
    
* Sufficiency rule (required). Green tests, bounded diff scope, passing evidence refresh, successful OPS execution, or review-clean artifact posture are necessary but not sufficient by themselves. They do not authorize acceptable-status language if the mapped work remains open in substance.  
    
* Review-language discipline (required). Before mapped work is complete in substance, allowed labels are: contributory, intermediate, review-clean, bounded, and `Supportable from repo evidence:`. Labels such as acceptable, accepted, satisfied, complete-for-close, and supportable for later drain to Done are reserved for reviews where the mapped work is complete in substance, the governed evidence proves that posture, and PF10 records that live truth where PF10 explicitly speaks.  
    
* Current PF09 recorded status may be cited only as canon-as-recorded, not as the live blocker source. Reviewers and approval artifacts MUST NOT block a slice solely because PF09 still says `Not done`, `Partial`, `Deferred`, or another pre-drain state.  
    
* Implementation-plan and QA-plan approval artifacts that are intended to feed later PF-canon drain MUST include an explicit later-drain PF-canon update statement naming the affected PF canon home(s), exact locator(s), supported later-drain action, and evidence basis.  
    
* Review-scope unit (required). Reviewers MUST review the approved PR or OPS task itself and its explicitly approved scope. They MUST NOT widen the review to later PRs, later OPS tasks, later validation runs, or whole-epic closure work unless the approved task explicitly includes them.  
    
* Non-closure task rule (required). If the approved task is explicitly validation-only, classification-only, evidence-only, sequencing-only, or another bounded non-closure step, PF09 closure is not a review gate for that task. The reviewer MUST judge whether the task truthfully and correctly completed its own approved job.  
    
* Boundary-preservation rule (required). For approved non-closure steps, reviewers MUST verify that the task stays within approved scope, does not overclaim closure, preserves any still-open PF09 or environment truth explicitly, and does not silently imply that later closure work is already complete.  
    
* Decision separation (required). Review and acceptance language MUST distinguish task-level acceptance of the approved step from PF09 closure status of the mapped row or subtask.  
    
* Governed evidence family coherence (required). When a review or closeout decision depends on governed evidence for a bounded task and a claimed closure dimension, the governed evidence family MUST express one authoritative posture only. Mixed-state families are invalid and mechanically block acceptance until normalized.  
    
* Evidence-family path collision repair (required). A review MUST treat evidence outputs that overwrite or collide with an existing governed evidence family as blocking until the collision is repaired. A repair is acceptable only when the task-specific evidence is moved to the approved PR/check/task-specific governed path, the overwritten shared or dependency artifacts are restored or refreshed, matching path proofs/index/mirror bindings are coherent, and the review records the collision and repair as evidence posture rather than silently accepting the overwritten state.  
    
* Transitive-writer collision and shared-history reconstruction guard (required). For a bounded collision repair that reconstructs shared history, a plan or review MUST identify the unique primary owner for each governed primary; inventory every transitive writer; migrate every active invocation and all affected consumers and companions; verify duplicate-key retirement under the evidence artifact-key collision-repair rule below; name the deterministic rollback source; complete all-order validation; prove fixed-point convergence; and satisfy the final-generator currentness rule below.  
    
* Evidence artifact-key collision repair (required). A review MUST treat an evidence-index or Machine Mirror key that can override, shadow, duplicate, or supersede the canonical artifact key for the same discovered physical path as blocking until corrected. A repair is acceptable only when the governed source row uses the canonical artifact key, stale duplicate keys or EPIC-specific keys are filtered or removed before dedupe and regeneration, Human Evidence Index and Machine Mirror are regenerated coherently, and the review records the collision and repair as evidence posture rather than silently accepting a duplicate-key state.  
    
* Contradictory-source consolidation is forbidden. A review, closeout, or consolidation artifact MUST NOT summarize or bind acceptance over source artifacts that still encode contradictory closure meanings for the same closure dimension. If contradiction exists, stop and classify the issue as a documentation/evidence failure rather than producing a merged authoritative summary.  
    
* Documentation/evidence normalization instead of rerun (required). If the runtime proof remains unchanged and the only defect is contradictory governed evidence or closure semantics, remediation may be a documentation/evidence normalization pass rather than a new runtime rerun only when the unchanged runtime facts are already evidenced, no new runtime or OPS claim is added, the affected governed family is refreshed to one authoritative posture in the same change, the Human Evidence Index, Machine Mirror, checksum sidecars, and required sibling path-proofs are refreshed coherently, and any prior contradictory bundle or report is explicitly treated as superseded evidence.  
    
* Bounded evidence-refresh side effects (required). Evidence-side churn outside the direct PR or task evidence family is non-blocking only when it remains within existing governed proof families, is caused by canonical evidence refresh, updater convergence, or required dependency refresh, adds no new runtime, route, serializer, public contract, token, or artifact-family claim, and the relevant index, mirror, path-proof, checksum, LF, schema, and orientation checks are coherent. The run or review evidence MUST name each affected family, classify each side effect as expected updater convergence, required dependency refresh, or unexpected drift, and identify any affected proof-companion paths plus corresponding Machine Mirror artifact keys or discovered paths when mirror rows move. A PASS or acceptance claim MUST fail closed unless the classified side-effect paths exist, proof companions validate against their targets, and affected mirror rows match artifact key, proof anchor, sha256, and size. The review MUST NOT use bounded side effects to claim unrelated PF09 status movement.  
    
* Unbounded evidence churn remains blocking when it creates a new evidence home, changes contract meaning, changes runtime behavior, lacks coherent proof companions, or is used to support an unapproved scope expansion.  
    
* Failure classification rule (required). Reviews that rely on governed evidence MUST distinguish runtime or implementation failure from documentation/evidence failure. Stable runtime facts plus contradictory governed artifacts are a documentation/evidence failure. Runtime wrongness remains a runtime or implementation failure.  
    
* Evidence-generator portability (required). When a plan, remediation guide, review, or closeout artifact relies on a repo-owned evidence generator as a governed proof command, the generator must be reviewable under a normal repo-root invocation or the artifact must explicitly classify the missing invocation support as tooling failure or tooling blocked. Plans and reviews MUST NOT treat caller-supplied `PYTHONPATH`, unstated local shell state, or other ad hoc environment setup as an acceptable substitute for a portable governed proof command unless the approved task explicitly defines that environment requirement and captures it in the step evidence.  
    
* Evidence-generator PASS binding (required). A governed evidence generator MUST NOT emit or support a `PASS` claim unless every decisive predicate for the claimed evidence family is evaluated against the current artifacts and passes. PASS status MUST be derived from current predicate checks, not from previous-artifact drift, stale local state, artifact presence, format-only checks, parsed-object equality where byte identity is required, digest-shape checks without recomputation, file presence alone, or absence of a sentinel string.  
    
* Evidence-generator currentness before index proof (required). When a plan, review, or closeout relies on generated evidence plus Human Evidence Index, Machine Mirror, checksum, orientation, path-proof, LF, schema, or updater checks, the artifact MUST show that the generator materialization command and generator check ran from the current logic path before evidence-index or mirror updater commands and their checks. Index, mirror, hash, path, orientation, LF, schema, or updater checks alone are not sufficient to prove generated evidence currentness when the generator itself was not invoked or checked in the governed run.  
    
* Source-backed inventory and closed-rails replay proof (required). When a plan, remediation guide, review, or closeout relies on a generated source inventory, contract inventory, endpoint reference, or contract map produced from cached or pre-captured public documentation, PASS requires proof that every decisive source row is backed by current cached body bytes or an approved authoritative machine-readable source plus checksum, status, and path binding. Metadata-only rows are not sufficient when source SHA, fetch status, tier, route, or contract content is decisive.  
    
* Quarantined suspect-source rule (required). A suspect or non-authoritative source may be absent, non-200, unavailable, or quarantined without blocking the generator only when validated authoritative sources remain sufficient to produce the promoted evidence, the quarantine posture is recorded in the governed artifacts, tests cover the non-blocking path, and the review does not claim runtime conformance from the quarantined source.  
    
* Generated-proof family completeness (required). When a check claims that generated proof families fail closed, PASS requires explicit fail-closed proof for every generated proof family used by the epic. If any such family is not proven, the step MUST remain TOOLING\_BLOCKED until the missing coverage is added and the final suite is rerun from the updated proof path.  
    
* Final generator logic rule (required). After evidence-generator logic changes, final governed artifacts, sibling path-proofs, Human Evidence Index entries, Machine Mirror rows, checksum sidecars, and any required targeted tests MUST be regenerated or rerun from the final logic path before a review, closeout, or later-drain recommendation may rely on them. A stale artifact produced by earlier generator logic is not sufficient proof after remediation.  
    
* Evidence-generator check-mode binding (required). When a governed evidence generator produces or registers its own artifacts, non-check generation may avoid write-time self-hash recursion only for the materialization step. Check mode MUST validate the final committed or current Machine Mirror sha256 and size bindings for every row the generator claims or depends on, including self-generated rows and any classified side-effect rows.  
    
* Evidence-generator remediation scope boundary (required). Fixing generator PASS binding, current-predicate evaluation, or final-artifact regeneration does not by itself mint an acceptance token, create a new gate, require an OPS task, authorize a public-surface change, or require a blanket audit of adjacent generators. If any of those actions are needed, they must be approved and routed independently.  
    
* PF-Canon non-edit discipline (required). Coding and implementation agents MUST NOT directly modify PF-Canon documents as part of implementation PR work, including checklist-status canon such as HDE Build Checklist. If implementation work reveals canon drift, missing canon coverage, or supportable checklist or canon status changes, the plan or review MUST record that as a drift note or doc-delta candidate and MUST route PF-Canon changes as follow-on canon maintenance rather than direct implementation-lane edits.  
    
* How plans MUST express reality or existence confirmation: cite a PF clause (titles-only) when PF already establishes the claim, or capture repo-local evidence for the current run under `audit/` when PF is silent. Do not treat an intended PF update as substitute evidence.  
    
* AI review and plan-analysis workflow (required). AI agents reviewing plans, remediation guides, QA plans, repo audits, closeout artifacts, or related review documents MUST use a retrieval-first, proof-first workflow: use PF10 where it explicitly speaks first, then read the current artifact under review end-to-end, then retrieve the owning PF canon home for each specific issue, then gather repo-reality proof for any claimed path, command, endpoint, environment variable, test ID, artifact path, or component home.  
    
* Tool order for repo-reality proof (required). Use `file_search` or full-source retrieval first for uploaded documents and PF documents. When repo reality matters, run minimal inventory proof next. For known literals, use exact-string repo search before regex or broad exploratory search, including task IDs, subtask IDs, token names, headings, route strings, command strings, filenames, artifact keys, environment variable names, and other exact literals. Regex search is allowed only when exact-string search cannot prove or disprove the claim. Broader semantic or exploratory search is allowed only after exact search fails.  
    
* Proof classification (required). Review findings MUST distinguish canon requirement, observed repo reality, and inference. Any unproven locus, path, route, command, flag, token spelling, or environment variable name remains `UNKNOWN` or `BLOCKED`. Do not guess it into existence. Do not rely on truncated viewer snippets, omission markers, or partial excerpts as proof; reopen the full source first.  
    
* No interactive steps. The plan must be runnable headlessly (and must log all commands).  
    
* QA prompt-mode violations are blocking under **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation**.  
    
* Command entrypoints must resolve. Any command that references a repo-resident script or file by path MUST point to an existing repo file at review time, unless the path is explicitly declared as QA-created by this plan.  
    
* Live QA Plans MUST NOT invent or assume helper scripts exist.  
    
* Plan-created scripts are permitted only when a required deliverable cannot be produced without one. When a plan requires a plan-created script, it MUST:  
    
  * name the exact repo-relative path and filename where it will be created,  
      
  * include runnable creation instructions,  
      
  * state why the script is required,  
      
  * keep the script minimal and purpose-bound to the deliverable.


* If the step is executed via an embedded harness function (no standalone script exists), the plan MUST cite the harness runner repo path when proven, or handle the runner locus via a discovery step that records the discovered locus verbatim before use.  
    
* New recurring artifact families/paths introduced ad hoc in a plan (not already governed by PF10) are blocked until introduced via PF10 addendum.  
    
* The following patterns are vetoed and invalidate approval:  
    
  * inferred or speculative repo-resident loci,  
      
  * placeholder routes, file paths, module names, or command strings used as scaffolding,  
      
  * any statement that implies app topology certainty without proof.


* A Live QA Plan that includes invented scripts, speculative app topology claims, or over-specified unproven command lines MUST be returned for revision.  
    
* Evidence artifacts MUST use a governed evidence family and root established by the owning canon. Default governed roots include `audit/**`, `artifacts/**`, and `docs/**`; an additional root is permitted only when it is explicitly governed and bound through the required Evidence Index, Machine Mirror, hash, and path-proof posture. Governed multi-root evidence is not drift by itself.  
    
* Epic Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts (for example step logs, harness outputs, artifact inventories, close-pack bundles) as part of their own required deliverables or completion criteria.  
    
* QA planning is a separate deliverable. QA execution evidence and PASS/FAIL verdicts belong only in QA-run artifacts and closure records.  
    
* Ops tasks are not QA tasks. Ops evidence is not a substitute for QA evidence.  
    
* Separation rule (no category mixing): keep these categories distinct:  
    
  * implementation work and PR deliverables  
  * ops tasks  
  * QA planning  
  * QA execution evidence and verdicts


* Future-artifact state violations are blocking under **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation**.  
    
* `/tmp` helper scripts MUST NOT print or persist secrets.

**ADR discipline (canon-resolution only; drain targets required):**

* If canon already speaks on a topic, do not write an ADR. Cite the owning PF(s) and remove any ADR placeholder/stub.  
    
* Any ADR included in a Plan or Remediation MUST represent a canon resolution decision (what ambiguity/conflict is resolved, and what decision is taken).  
    
* Every ADR MUST declare explicit drain targets (owning PF docs \+ intended doc-delta updates required to canonize the decision).  
    
* ADRs MUST NOT cite PF20 as a source of requirements, rails, acceptance semantics, or evidence-surface definitions (PF20 is historical-only).  
    
* Iteration-churn escalation is controlled by **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation**. Continuing after that section requires a pause is blocking.

KISS evidence posture for Live QA (normative):

* Live QA Plans MUST minimize required outputs to:  
    
  * one primary step log per check under `audit/qa/<epic-id>/checks/<check_id>/primary.log`, and  
      
  * the step-logs manifest listing check IDs, status, and log paths (current-state, not per-run history).


* Prefer “validate existing canon evidence” over “produce new QA artifacts”:  
    
  * If PF10/PF-canon already establishes an artifact family/path, the QA plan validates it (exists \+ minimal posture checks) and records PASS/FAIL in the check’s primary.log.  
      
  * QA creates new artifacts only when the check is specifically about QA-run outputs (step logs, manifest) or when canon explicitly requires a generated QA artifact family/path.


* Any additional required artifact must be explicitly justified as acceptance-decisive and must be canonized (and path-pinned) by PF10 or PF-canon as a governed evidence family/path.

Materiality-based blocker discipline (required for Epic Plan and Implementation Plan review):

* A planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table formatting, heading style, punctuation, spacing, bold markers, presentation style, inventory-row ordering, template-perfect phrasing, missing non-decisive locator precision, missing titles-only polish, or an Epic QA root omission in an Epic Plan that does not authorize QA execution, unless the defect materially changes truth, proof, acceptance, execution safety, source authority, portability, implementation scope, PF09.x completion mapping, evidence identity, evidence trust, OPS/PR boundary, public/private surface posture, canon conflict handling, or closeout truth.  
* Review severity MUST map to material effect: Blocker changes truth, proof, acceptance, execution, source authority, or portability; Caveat creates a real risk with a safe default; Suggestion improves clarity, consistency, or maintainability; Nit is cosmetic, template-polish, or wording-level only.  
* Valid blocker framing must state the material harm, such as conflict with active PF10, an unresolved ADR after PF10 resolves the exact topic, a required external CA/audit/non-PF source for Codex execution, unregistered token claimed as an acceptance token, Already Implemented claimed without embedded proof, OPS work required inside Codex PR work, unproven repo locus, public surface expansion without canon support, PF23 used as deliverable/token/blocker/acceptance authority, or PF20 used as current planning authority.  
* Invalid blocker framing includes a missing token row when the plan does not overclaim a token and the evidence family is scoped, imperfect CA quote-block formatting when the fact is embedded and self-contained, provenance labels such as CA vetted when no external CA access is required, or section formatting that is not template-perfect but preserves meaning.  
* **Terminal-state reachability:** identify the claimed terminal state and prove a feedback-free path from repository-local inputs to the tracked candidate bytes.  
* **Execution-surface feasibility:** identify every generator, validator, workflow, promotion, and hosted-CI surface required to produce and validate those exact bytes, and prove that each required transition is executable.  
* **Rails consistency:** state the rails and authorization posture for every transition and require plan or authority revision before any transition that needs a different rails or authorization posture.  
* **End-to-end proof:** provide a small end-to-end feasibility proof showing that the candidate bytes can reach and be validated at the claimed terminal state without writing canonical results back into already-final tracked source.  
* **Token reachability, when tokens are in scope:** prove reachability token by token against the current evidence model. Token registration, a planned path, or artifact existence does not establish reachability or PASS.

Live QA Plan approval materiality discipline (required):

* Live QA Plan approval is an operational-readiness review. A Live QA Plan should be approved when it is safe, self-contained, phase-bounded, and clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict.  
* A Live QA Plan MUST NOT be blocked solely for rendered escape characters, markdown or AI-rendered backslashes, heading style, bullet style, table style, quote-block formatting, code-block formatting, whitespace, punctuation, line wrapping, command syntax polish, command invocation style, interpreter choice unless it changes operational behavior, exact shell spelling, exact command ordering unless order is required for safety or proof, evidence-ledger byte-shape polish at plan approval, path-proof transcript field polish at plan approval, canonical JSON compactness wording at plan approval, or step-log header polish at plan approval.  
* Valid Live QA Plan approval blockers are operational: missing required QA step coverage, missing required deliverables or explicit PASS/FAIL criteria, unsafe rails, secret exposure, live-provider or external-action boundary violation, public/private surface boundary violation, token overclaim, non-token proof label treated as an acceptance token, PF23 used as an execution artifact, PF20 used as current authority, PF14 used as governance or acceptance authority, PF-canon drainage required as a gate, unproven required existing locus with no source-grounded proof, no discovery posture, and no QA-created fallback, wrong target execution, prohibited mutation, no governed evidence family, no decisive receipt, contradiction of active PF10, or contradiction of permanent PF-Canon where PF10 is silent and the contradiction affects operational truth.  
* Commands in a Live QA Plan are operational instructions rather than canon contracts unless the plan explicitly states exact invocation is required and the owning PF home requires exactness for the operational result. Exact-command mismatch is a Caveat, Suggestion, or execution note when check intent, proof target, rails posture, expected evidence family, PASS/FAIL predicate, operator safety boundary, and actual-command capture remain clear and an equivalent safe command can produce the same proof.  
* A Live QA Plan may create QA-only harness scaffolding during Step 0 when the harness is limited to QA evidence capture and does not create product behavior. Reviewers MUST NOT require repo-existence proof for a QA-created harness that the plan explicitly creates during the QA run. Formatting, indentation, line wrapping, and code style inside QA-created scaffolding are non-blocking unless they prevent creation or safe execution and no bounded correction is allowed during QA execution.  
* Live QA Plan approval requires evidence identity, not final closeout perfection. At approval time, the plan must identify what each check proves, what result counts as PASS, what result counts as FAIL, where the QA run records the decisive receipt, which evidence family or evidence class supports the verdict, and how token claims are avoided unless registered and in scope. Final byte-level details may still fail QA execution or closeout validation; they are approval blockers only when the plan lacks evidence identity, lacks a decisive receipt, relies on ungoverned evidence as decisive proof, or explicitly rejects required governed-evidence discipline.  
* Review severity for Live QA Plan approval MUST map to operational harm: Blocker prevents safe execution, invalidates the intended QA verdict, breaks source authority, creates token or acceptance overclaim, violates rails or secret posture, requires unavailable execution inputs, or makes required evidence untrustworthy; Caveat creates operational risk with a safe default, bounded discovery path, or equivalent execution path; Suggestion improves clarity, operator usability, reviewability, or future maintainability; Nit is cosmetic, formatting-level, or presentation-only.  
* A reviewer who returns a Live QA Plan for revision MUST state the concrete operational harm and show that the defect prevents safe execution, invalidates the QA verdict, breaks evidence trust, changes source authority, creates token overclaim, or violates rails or safety boundaries.

Plan command, syntax, and example-literalness approval rule (required):

* Plans are not execution artifacts. Plan approval evaluates truth, proof, scope, authority, safety, acceptance posture, phase fidelity, and evidence identity, not whether every command, snippet, helper, heredoc, shell line, or example is a literal runnable transcript.  
* QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, closure-review artifacts, and related approval artifacts MUST NOT be blocked, rejected, returned for revision, or classified as REVISE AND RESUBMIT solely because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written.  
* This rule applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly. Command syntax, helper-code syntax, heredoc form, indentation, markdown escaping, escape characters, shell redirection syntax, interpreter invocation, code-block formatting, quote formatting, wrapping, whitespace, punctuation, copied command exactness, non-literal examples, assistant-introduced syntax artifacts, renderer-introduced syntax artifacts, and formatting introduced during review, redline, or paste workflows are not valid plan-approval blockers by themselves.  
* QA steps and plan commands do not need to be paste-ready, literal executable commands, final runnable syntax, or exact shell, Python, or tool syntax. They may express the intended proof action in operational language, pseudocode, structured prose, or approximate command form when the proof target, scope boundary, rails posture, evidence family, and verdict posture are clear enough for the assigned operator to execute safely and produce a governed verdict.  
* Syntax correction is ordinary execution hygiene. During execution, a QA operator, Codex, Kronos, PO, or implementation owner may normalize a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue in flight when the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture are preserved.  
* In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, authority, acceptance posture, or evidence identity changes.  
* Valid plan approval blockers are limited to material truth, proof, scope, authority, safety, acceptance, phase, evidence-identity, or canon-conflict defects. Examples include missing proof obligation, missing in-scope PF09.x mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement inside closed rails, secret exposure requirement, OPS work assigned to Codex, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, missing acceptance-decisive deliverable category, unclear PASS/FAIL or verdict posture, unresolved phase boundary conflict, unresolved canon contradiction, or an evidence identity gap where the proof target cannot be distinguished.  
* A reviewer must not disguise command syntax, paste-readiness, escaping, or formatting complaints as truth/proof blockers. If the reviewer’s objection can be fixed by editing command syntax, escaping, indentation, heredoc form, shell syntax, or helper-code formatting without changing the proof target, it is not a blocker.  
* Before blocking on a command, helper, heredoc, syntax, escape, formatting, indentation, copied-chat, or paste-readiness issue, the reviewer MUST answer the blocker test below. If every answer is no, the issue is not a blocker:  
  * If normalized in flight, does the proof target change?  
  * Does the evidence family change?  
  * Does the artifact identity change?  
  * Does the PASS / FAIL / TOOLING meaning change?  
  * Does the rails posture or secret-safety posture change?  
  * Does the ambiguity require inventing a repo locus, artifact family, acceptance predicate, PF09 scope, or source authority?  
  * Does the defect hide a real implementation, QA, OPS, token, evidence, phase, public/private boundary, or source-of-truth issue?  
* A reviewer returning a plan for revision over a command, helper, heredoc, syntax, escape, formatting, indentation, copied-chat, or paste-readiness concern MUST state the separate non-syntax defect. Without that separate defect, the allowed classification is Non-issue, Note, In-flight normalization, or Operator caution.  
* For any plan artifact, command or syntax concerns may be classified only as Non-issue, Note, In-flight normalization, or Operator caution. They MUST NOT be classified as Blocker, Approval blocker, QA readiness blocker, Implementation readiness blocker, Closure blocker, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, evidence failure, token failure, PF locator failure, or command validity failure requiring plan revision.  
* Future plan-review, QA Plan review, implementation-plan review, remediation-plan review, redline-generation, QA-readiness review, closure-review, and Codex-audit prompts should include this guard: plan commands, snippets, helper code, heredocs, shell lines, and examples do not need to be paste-ready or literal. Syntax defects, escape characters, markdown rendering artifacts, indentation issues, and command exactness must never block plan approval. Treat them only as in-flight normalization unless they reveal a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, or evidence-identity defect.

Explicit non-blockers (do not gate approval):

* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.  
    
* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.  
    
* Template adherence is structural only. Reviewers evaluate whether required sections and required structural blocks are present. Header styling, heading levels, and indentation are not part of structural adherence.  
    
* Header-format-only redlines are nits and MUST NOT be requested as approval conditions, including changes that only:  
    
  * switch between bold labels and Markdown headings  
  * adjust heading levels or heading capitalization  
  * restyle bullets or numbering  
  * change indentation, spacing, or cosmetic line wrapping


* Command syntax latitude and QA-correctable defects: approval binds to command identity, target proof output, repo-locus proof, and bounded PASS/FAIL semantics, not exact shell or Python syntax perfection at plan-review time. A syntax, quoting, escaping, punctuation, rendered-markup, or small local expression defect is non-blocking when the command identity, target check, artifact, route, path, evidence family, and intended PASS / FAIL / TOOLING classification remain clear; the QA executor can correct it locally without inventing a new repo locus, command source, route, artifact family, acceptance predicate, or PASS/FAIL criterion; and the exact corrected command is captured in governed step evidence. This latitude MUST NOT be used to accept invented commands, unproven loci, ambiguous command identity, wrong artifacts, wrong routes, changed acceptance semantics, or defects in code, canonical JSON, schemas, acceptance maps, token registries, machine-readable manifests, or executed command transcripts.  
    
* Command syntax latitude: approval binds to command identity and bounded proof outputs, not to exact shell syntax. JSON-carrying environment variable assignments are treated as intent carriers; do not reject solely on whitespace or quoting style. Plans MAY define plan-level Command Snippets once and reference them by local IDs, provided each executed step log records the resolved command. This latitude MUST NOT be used to accept invented commands or unproven loci.  
    
* Markdown sanitation rule (analysis-only): when quoting a plan for review notes, remove only presentation escapes that exist solely for Markdown rendering. Do not remove semantic escapes used by shell, JSON, regex, or paths, and do not rewrite commands based on sanitized excerpts.  
    
* Optional environment snapshots may be omitted if the plan otherwise references stable loci.  
    
* Minor formatting artifacts are non-blocking if semantic meaning is preserved, and must be treated as nits (they must not change the binary approval outcome). Examples include escaped Markdown list markers, backslashes inserted for rendering, cosmetic whitespace differences, bold/italic marker differences, and bullet style differences. If formatting changes meaning or introduces ambiguity (commands, expected outputs, file paths, loci, artifact names, evidence roots, portability constraints, required structural markers, quoted carryover blocks), it is not minor and may be gating.  
    
* Rendered escape artifacts in source-facing work are categorically non-blocking (required). A plan, guide, QA plan, Live QA Plan, implementation plan, remediation guide, Codex prompt, review artifact, redline pass, PF10 addendum draft, PF-facing artifact, or acceptance artifact MUST NOT be blocked because assistant-rendered, Markdown-rendered, transcript-formatted, quote-formatted, preview-pane, copied-chat, or review-prose output shows escape characters in otherwise clear machine-sensitive strings. This applies to repo paths, artifact paths, evidence paths, command names, command arguments, shell redirection markers, heredoc markers, module names, endpoint paths, route strings, token names, environment variable names, config keys, JSON keys, artifact keys, PF09 task IDs or subtask IDs, ADR IDs, headings used as locators, evidence filenames, manifest filenames, path-proof filenames, hash filenames, quoted source lines, plan snippets, and QA-created script bodies.  
    
* Source-level verification requirement (required). A rendered escape character is never evidence of a source defect. Before treating an escape-character issue as a defect, the reviewer must inspect the raw/source artifact by direct file view, read-only command, uploaded source inspection, actual pasted document text after paste, or governed artifact/index/mirror/path-proof source. A blocker may be raised only when the raw/source artifact itself contains the unwanted character and the character changes executable, governed, canonical, or semantic identity.  
    
* Quote, redline, and placement posture (required). Redline placement quotes, PF proof quotes, Doc A or Doc B quotes, IG Approved or CA vetted quote blocks, and quote-verbatim checks MUST be evaluated against raw source text. If the only difference is assistant-rendered or markdown-rendered escaping, the quote is source-equivalent and MUST NOT be blocked. Redline authors MUST NOT draft corrective redlines solely to remove display-layer escapes; such a redline is allowed only when the raw target document or raw governed artifact actually contains the unwanted character.  
    
* Codex prompt posture (required). Codex prompts MUST treat escaped display text as non-authoritative unless it is inside a raw source file Codex opens. A prompt MUST NOT instruct Codex to create, check, rename, implement, remediate, or fix escaped paths or filenames derived from assistant rendering unless raw source contains the escape and the approved plan explicitly directs the correction.  
    
* Burden of proof and classification (required). The burden of proof is on the reviewer or agent raising the escape issue. A valid blocker must name the raw/source file or artifact inspected, the read-only command or source-view method used, the raw line showing the unwanted character, why it changes executable/governed/canonical/semantic identity, and why it is not merely assistant or markdown rendering. Without that proof, classify the issue as a display-layer artifact and withdraw the blocker. Rendered escapes MUST NOT be classified as FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, closeout blocker, or remediation requirement.  
    
* Current-loop and future-prompt posture (required). Any existing blocker based solely on rendered escape characters is invalid unless re-proven from raw/source artifact text. Future review, redline, plan-revision, QA-review, remediation-review, and Codex-audit prompts should include a rendering-artifact guard that tells reviewers to ignore display-layer escapes unless raw/source inspection proves a substantive source defect.  
    
* Headings and levels need not match a reviewer’s preferences; only required headings and required template blocks are gating.  
    
* A plan MAY cite upstream scripts or previously-approved plan steps (for example, reused remediation steps), provided it cites exact repo paths and captures the necessary evidence outputs under `audit/`.  
    
* Reviewers MUST NOT request changes solely to make a plan easier for LLM parsing. If a change is requested, it must be justified by execution safety, evidence posture, canon alignment, or mechanical paste safety requirements, and should be the smallest viable edit.  
    
* Negative audit proof and no-hit proof are non-blocking when the approved proof target is to show absence of a condition, no matching drift, no forbidden string, or no relevant hit. Reviewers MUST evaluate whether the negative proof was produced from the approved scope, search method, and evidence target; they MUST NOT require a rerun or fallback positive proof solely because the result is negative.

Caveats (allowed, must be mechanically logged):

* DOC\_DRIFT — plan adapts to repo reality; record mismatch mechanically and drain later.  
    
* ENV\_DRIFT — environment differs from baseline; capture mechanically; do not invent new rails.  
    
* UNREGISTERED\_TOKEN — registry mismatch is evidenced mechanically (validator output); do not maintain narrative lists.

### **Materiality-based blocker discipline for planning and review artifacts**

A reviewer MUST NOT block approval, require revision, downgrade a decision, or force resubmission solely because truthful, unambiguous, functionally equivalent text differs from a template example, placeholder, sentinel, preferred phrasing, punctuation, or presentation convention.

Before assigning a Blocker, requiring revision, or selecting a negative approval outcome, the reviewer MUST identify the exact defect, a separate concrete material consequence, and the complete controlling source or verified repository fact establishing that consequence. If all three are not established, the issue is not a Blocker and MUST NOT change the approval decision.

A template labeled `Normative`, `Required`, or `MUST` establishes the required field, section, structure, or meaning. It does not make every example value, placeholder, sentinel, punctuation choice, or wording pattern byte-exact. Semantic equivalence satisfies approval readiness when the required field or block is present, truthful, unambiguous, and functionally equivalent.

A literal mismatch may block only when controlling authority explicitly requires the exact literal, a verified machine consumer depends on it, the mismatch changes a canonical identifier, token, schema value, artifact identity, status, date truth, scope, authority, execution behavior, evidence meaning, acceptance posture, or closeout truth, or it creates a material ambiguity that cannot be resolved safely without changing the artifact.

A nonmaterial finding MAY be omitted or recorded only as a non-gating `Suggestion`, `Nit`, `Note`, or `Non-issue`. It MUST state that no correction is required and MUST NOT become a Caveat, Blocker, approval condition, ADR or Tracked Issue revision, canon-authoring requirement, resubmission trigger, or reason to withhold the strongest positive decision otherwise supported.

For an Epic Plan that is not complete and makes no closeout claim, `Date completed: Not completed; no closeout claim is made` is approval-equivalent to `Date completed: [INTENTIONALLY LEFT BLANK]`. This equivalence does not authorize an incomplete or non-date value after the epic is complete.

A review that blocks solely on a nonmaterial conformance difference is invalid to that extent. Withdraw the blocker and every dependent required fix, ADR or Tracked Issue disposition, summary statement, and final decision, or rerun the review from the unchanged source. This rule does not waive omitted required content, false facts, contradictory state, unresolved executable placeholders, invented identifiers, unsafe OPS assignment, evidence-identity defects, token or acceptance overclaims, or another defect with a demonstrated material consequence.

### **PF09 phased-routing boundary**

PF09 is the phased set PF09.1 through PF09.7; the retired monolithic PF09 surface is not a valid active mapping. A reusable template does not preselect a phase. Every completed HDE artifact MUST resolve each task-like item to exactly one `PF09 disposition`:

1. `in the current epic with exact phased PF09 task or subtask mapping`;  
2. `out of the current epic with exact phased PF09 task or subtask mapping`;  
3. `PF09 gap`;  
4. `documentation/status drainage only`; or  
5. `out of HDE phased-build scope`.

Copy exact task and subtask identifiers from the applicable complete phase document. A parent task is insufficient when a relevant subtask exists. Cross-phase work uses separate rows for independently mapped scope; it MUST NOT use one umbrella phase label.

| Field | Required content |
| :---- | :---- |
| `Work item ID` | Stable local plan or task identity. |
| `PF09 disposition` | Exactly one of the five postures above. |
| `Phased PF09 document` | Exact current in-document title, or `N/A` only for a non-mapping posture. |
| `Task ID` | Exact task ID, or `N/A` with the selected non-mapping posture. |
| `Subtask ID` | Exact relevant subtask ID; `None exists` only after verifying no relevant subtask exists. |
| `Exact source heading` | Exact task or subtask heading used as the locator. |
| `Contribution` | What the work advances, satisfies, leaves open, or merely documents. |
| `Status nonclaim` | State that the artifact does not itself move PF09 status unless a separately authorized canon update occurs. |

#### **Closure-first PF09 assessment and remedial-work gate**

For every PF09 row assigned to completed epic work, the assessment MUST determine the row's closure posture before creating a remedial PR, OPS task, documentation task, or revised implementation plan. An unchanged physical PF09 status, missing closure record, incomplete reviewer inspection, documentation drainage, or a row description broader than the approved epic assignment is not evidence that implementation or OPS work remains.

Each mapped row MUST receive exactly one disposition:

* **CLOSURE SUPPORTED — Recommend `Done`.**  
* **CLOSURE NOT SUPPORTED — PR work remains.**  
* **CLOSURE NOT SUPPORTED — OPS work remains.**  
* **CLOSURE NOT SUPPORTED — PR and OPS work remain.**  
* **CLOSURE NOT YET PROVABLE — Additional inspection or evidence capture is required.**

The assessment MUST identify the exact phased PF09 document, row ID, title, physical status, approved plan mapping, mapped PR and OPS work, complete original and remedial PR lineage, completed OPS outcome, latest applicable PF10 guidance, exact repository endpoint inspected, implemented behavior, material implementation and evidence surfaces, applicable tests and CI, governed evidence, exact remaining PR work or `None`, exact remaining OPS work or `None`, exact remaining inspection or `None`, live PF10 disposition, and physical PF09 drainage posture. When the operator asks whether the row can close, answer `Yes` or `No` before the supporting explanation. `Partial`, `contributory`, `advances`, or `no status change` is not a closure disposition.

A remedial PR MAY be proposed only when the assessment identifies the exact row and approved scope, required repository behavior, inspected endpoint, defective implementation surface, direct evidence of nonconformance, complete execution trace when the finding concerns an execution path, reconciliation with any accepted original or remedial lineage, proof that the condition is not merely syntactic, rendered, historical, test-fixture-only, documentation-only, or outside approved scope, the smallest bounded repository correction, and a testable completion condition. If any element is absent, do not create a remedial PR.

A remedial OPS task MAY be proposed only for a specific external or privileged outcome that the approved row requires and repository implementation cannot perform. The assessment MUST identify the mapped row, approved OPS obligation, required outcome, current evidence that it has not occurred, why repository work cannot satisfy it, and the exact evidence that will prove completion. Missing PF10 text, unchanged PF09 status, missing reviewer evidence, a repository defect, or a documentation delta MUST NOT be converted into OPS work.

When evidence is insufficient, identify the exact missing inspection or evidence, retrieve it when permitted, and use `CLOSURE NOT YET PROVABLE` if the gap remains. Do not assign PR or OPS work unless completed inspection independently proves that work remains. When closure is supported, provide the evidence required for a PF10 closure-authorization addendum rather than inventing further work.

### **Review-record identifier boundary**

Counters begin at `001`, use exactly three digits, and increment independently within their semantic group.

| Record group | Prefix and example |
| :---- | :---- |
| Diff Review | `DR-001` |
| Findings | `FND-001` |
| PF09 proposals | `PF09P-001` |
| Other-PF proposals | `OPFP-001` |
| PF19 references | `PF19R-001` |
| PF27/PF06 references | `PF2706R-001` |
| Implementation gaps | `IMP-001` |
| PF19 deltas | `PF19D-001` |
| Other-PF deltas | `OPFD-001` |
| Remediation Review PF Doc Delta Proposal | `RRPFD-001` |
| Epic Closure PF-Canon Doc Delta | `ECPFD-001` |

Prefixes are uppercase ASCII letters and digits followed by one hyphen and a three-digit counter. A declaration occurs once within one generated artifact. An internal cross-reference resolves to a declaration in that artifact; an external reference uses `<artifact identity>#<record ID>`. Validators reject duplicate declarations, unresolved references, wrong numeric width, and another semantic group's prefix. Historical completed records retain their historical IDs unless separately refreshed.

### **CI lane classification and automated budget-control discipline**

Plans and reviews that address CI or another mechanical control MUST classify it by both continuing risk and lane: required PR CI, release or security automation, QA or audit automation, or epic closeout automation. Required PR CI is justified only when it protects a current product or delivery condition, detects a concrete failure with a material consequence, remains necessary without reference to the originating epic or its closeout artifacts, and is a proportionate merge-blocking surface.

Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof. Separately authorized closeout automation MAY remain isolated and non-gating. A control that protects a genuine release, security, compliance, QA, audit, product, build, deployment, or operational boundary remains in the smallest correct lane.

A material CI-budget finding MUST identify the avoidable hosted execution, the repository or authorized-setting surface that can control it, the automated behavior required, the protection that must remain, and a method for verifying the resulting execution shape. Durable control MAY use tracked workflow configuration, repository-owned validation tooling, automated trigger or change selection, concurrency and superseded-run cancellation, reusable setup, deterministic caching or artifact reuse, automated lane separation, truthful required-check aggregation, or an authorized repository setting.

Manual push limits, agent self-reporting, operator pause gates, push-count disclosures, exception narratives, transient reports, and documentation-only remediation are not CI budget controls, acceptance conditions, remediation tasks, or approval blockers. There is no authoritative five-update threshold or required pause before a sixth update. Push counts MAY support diagnosis but do not establish a violation by themselves.

Automated budget control MUST prevent or narrow duplicate equivalent suites, control superseded expensive work, select heavy validation by event and affected change, reduce repeated setup and validation where safe, preserve deterministic required-check continuity, and validate the exact final candidate head. It MUST NOT hide failed or unexecuted applicable work behind a green result, leave required status pending or absent, rely on stale or unverifiable caches, bypass protection, or misclassify an affected change as irrelevant.

Reviewers MUST inspect repository configuration and available GitHub behavior directly when those sources expose the facts. They MUST NOT manufacture a report-only task. If no automated or durable correction exists within authorized scope, the observation MUST NOT be converted into a remediation task or acceptance blocker. The authorized implementation task selects the smallest safe repository-grounded design; a plan or review MUST NOT invent a YAML arrangement, job name, tool, cache implementation, concurrency syntax, or change-detection mechanism.

### **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation**

This section is the sole complete local home for future-step artifact semantics, QA prompt modes, and iteration-churn escalation.

#### **Template semantics: future-step artifacts**

* `PRESENT`: the producer executed and the artifact exists at its governed path.  
* `MISSING`: the producer executed and the required artifact is absent or unproven.  
* `NOT RUN / DEFERRED`: the producer did not execute, so the artifact is not yet expected.  
* Deferred artifacts MUST appear only under an explicitly labeled deferred or not-run area.  
* A future artifact MUST NOT appear as current primary evidence and MUST NOT support `PASS`.

#### **Prompt-family separation: AUTHORING vs REVIEW modes for QA prompts**

* Every QA prompt MUST declare exactly one mode: `AUTHORING` or `REVIEW`.  
* `AUTHORING` MAY create or revise plans, runbooks, and command sequences.  
* `REVIEW` MUST produce only its required review or verdict structure and MUST NOT create new runbooks or new commands.  
* The narrow review-mode remediation exception MAY reproduce only commands copied verbatim from the approved plan together with the plan's caveats.  
* A mechanical mode token and required-section gate is strongly advised, not mandatory unless separately promoted by an owning authority.

#### **QoS stop-rule: iteration churn escalation**

* More than three plan-to-evidence structural mismatches in one epic QA run triggers a pause before further execution.  
* Repeated occurrence of the same failure class triggers systems RCA plus template or canon drainage instead of another local patch.  
* The drain MUST target the failure class, not only the incident.  
* The record MUST identify the rationale, source mismatch class, owner, affected template, and drain targets.  
* Current local drain targets remain PF10 and PF27 where applicable.  
* If an existing validity lint can detect the class, extension requires separately authorized implementation work. PF27 MUST NOT invent a lint path.

#### **Redline bundle construction discipline (required for editorial redline sets)**

Applies when a plan review, remediation review, audit review, or doc-drain task emits editorial redlines.

Rules:

* Original-document anchor space only. All placement anchors in one redline bundle MUST be resolved against the unchanged base document only. A later redline MUST NOT anchor against text that would exist only after an earlier redline is applied.  
    
* Non-overlap invariant. No two redlines may target intersecting spans of the base document. No INSERT may land inside a span already covered by a REPLACE. No REPLACE may partially or fully cover a span already targeted by another REPLACE.  
    
* One strategy per affected region. For any contiguous affected region, choose exactly one strategy: one consolidated REPLACE for the whole region, or multiple smaller redlines whose target spans are pairwise non-overlapping. Mixing both strategies within the same affected region is prohibited.  
    
* Parent-child prohibition. If one redline REPLACEs a parent block, section, step block, heading block, list block, or other enclosing region, no later redline may target any line inside that parent region. All required child edits MUST be folded into the parent replacement.  
    
* No second-pass layering. If additional fixes are discovered inside an already-targeted region, rebuild from the original base document and re-emit the affected region as one consolidated replacement or as a new non-overlapping set.  
    
* Repeated-anchor safeguard. If a target line or boundary line is repeated in the base document, widen the target to the nearest unique enclosing heading or other unique boundary before emitting the redline. A repeated line MUST NOT be used as the only placement anchor.  
    
* Coverage-before-emission rule. Before outputting redlines, map each required review item to the exact base-document target region that will implement it. The author MUST NOT discover scope incrementally while already emitting the redline bundle.  
    
* Merge-on-conflict rule. If two or more required changes touch the same region, they MUST be merged into one consolidated redline. Sibling redlines that depend on one another’s output are prohibited.  
    
* One-pass apply simulation required. Before output, the full bundle MUST be tested mentally or mechanically against the unchanged base document as a one-pass application set. A redline bundle is valid only if it can be applied once from the original base document without anchor collision, span overlap, parent-child nesting conflict, or re-anchoring later redlines after earlier edits.  
    
* Mechanical blocker posture. If requested changes cannot be represented as a non-overlapping one-pass bundle, do not emit a self-conflicting bundle. Rebuild the affected region as one consolidated replacement, or return the item for revision when the declared review mode allows blocked output.

#### **Review stability and no-moving-target discipline (required for diff-first approval loops)**

Applies to Epic Plans, Implementation Plans, Live QA Plans, remediation plans, closeout reviews, and other diff-first approval loops that use PF27 templates.

Rules:

* Full-gate first pass is required. The first approval review MUST apply the full active review gate set to the full artifact, not a partial subset.  
    
* Gate freeze across the same review loop. After the first review on a given artifact line, do not introduce a new blocker from already-visible unchanged text unless triggered by current-revision text, a newly supplied authoritative input, a PF canon change, or a prior read failure.  
    
* Coupled-constraint rule. If a reviewer requires more explicitness, the same review MUST also declare the coupled constraints triggered by that explicitness, including provenance, command-string, path/locus, creation-ownership, schema/header, naming, and portability constraints.  
    
* Unchanged-text blocker rule. Any blocker first raised against unchanged text in a later revision MUST state the trigger that made it newly raisable. Without a valid trigger, classify it as Review Drift.  
    
* Review Drift handling. If an omitted earlier-visible blocker is discovered later, label it as Review Drift, state that it was visible earlier, consolidate other same-scope pre-existing blockers in the same review, and stop drip-feeding blockers from that same unchanged-text family in later rounds.  
    
* Contradictory review prohibition. Do not alternate between "too implicit" and "too explicit" on the same requirement family unless the later problem is created by newly changed text or the exact canon constraint supporting the later objection was already cited in the earlier review.  
    
* Read-failure and truncation handling. If a missed issue was caused by truncation, partial retrieval, or other read failure, rerun the full sweep after full retrieval before issuing a new decision.  
    
* Non-author penalty rule. Issues that were visible in an earlier reviewed revision but omitted by the reviewer MUST NOT be framed as author-created churn, treated as a fresh author-side defect cycle, or used to imply that the author changed requirements when the review target itself moved.  
    
* Approval integrity. A later-discovered real blocker may still block approval, but it MUST be handled under the provenance and Review Drift rules above.  
    
* Required blocker provenance in review output. Every blocker or caveat in a diff-first approval loop MUST be classed as one of: Introduced by current revision, Previously raised and still unresolved, or Review Drift.

## **2\) HDE-EPIC-Plan**

This section defines the **Epic Plan** template used for in-flight planning and close preparation.

**Historical-only posture (normative):**

* PF20 HDE-Phased Epics MUST contain only completed epic records.  
* In-flight epics MUST NOT be added to HDE-Phased Epics (no partial records; no placeholders).  
* Archive-on-close: the epic record is added to HDE-Phased Epics only once, at epic close, as a final historical entry.

### **Epic Record Template (Normative)**

For every epic, fill out the following fields as the **Epic Plan record**. At epic close, the final Epic Plan record is archived into HDE-Phased Epics as the historical entry.

#### **Meta**

* **Epic ID:** `HDE-EPICXXX`  
    
* **Epic name (short):**  
    
* **Alchemical phase:** (exact phase name per PF21, e.g. `Calcination`, `Dissolution`)  
    
* **Phase rationale (1–3 sentences):** Why this epic belongs in this phase.  
    
* **Status:** `Planned | In Progress | Blocked | Pending Review | Done | Won’t Do | Superseded`  
    
* **Explicit approval sentinel:** `ASK OK?`  
    
* **Date started:** `YYYY‑MM‑DD`  
    
* **Date completed:** `YYYY‑MM‑DD` (or \[INTENTIONALLY LEFT BLANK\])

#### **Business Case (MUST)**

The Business Case MUST describe the practical goals of the epic in Glow product terms (not internal library terms).

Minimum required contents:

* **Problem statement:** who is experiencing the problem and why it matters.  
    
* **Proposed change:** what capability is being introduced or changed and the intended effect.  
    
* **Value/impact:** user value, internal value, and/or risk reduction.  
    
* **Why now:** trigger or urgency (why this is being worked on now).  
    
* **What success looks like:** measurable outcomes where possible, or clear qualitative criteria when not.  
    
* **Scope boundaries:** explicit statement of what is out of scope.  
    
* **Non-goals:** list 1–5 concrete items that are specifically not being pursued in this epic.  
    
* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Plan.

Review posture:

* Missing Business Case (or a Business Case that is purely a technical task list) is blocking and MUST be returned for revision.

#### **Contract and Compatibility Posture (MUST)**

Every Epic Plan MUST include this section. If there are no contract changes, no new surfaces, and no new flags, explicitly state that posture (for example: "No change" or "None") and still complete the backward-compat posture.

Prompts:

* **Contract changes / new surfaces:** Identify any new or changed contracts, surfaces, or externally visible behaviors introduced by this epic.  
    
* **Justification:** For each contract/surface change, explain why it is necessary to achieve the Business Case.  
    
* **Flag strategy (if applicable):**  
    
  * If introducing a new flag: explain why a new flag is required instead of reusing an existing surface.  
      
  * If reusing an existing surface: explain why reuse is safe and preferred (and what safeguards apply).


* **Backward-compat posture:** State what remains unchanged by default, what changes for existing users, and any rollout or migration posture needed to avoid accidental breaking changes.  
    
* **Open-rails QA declaration:** If the epic affects user or production surfaces, the Epic Plan MUST declare whether open-rails QA is mandatory or whether an explicit PO-authorized exemption applies. This declaration must be planning-level and must not embed Live QA runbook commands in the Epic Plan.  
    
* **Open-rails triggering surfaces:** User or production-surface triggers include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor request shaping, vendor response handling, vendor route policy, external API transport, environment or secret binding behavior, database persistence or retrieval behavior, runtime compute behavior, deployed service behavior, and admin or ops-facing behavior that can affect production truth.  
    
* **Implementation preservation:** Any Implementation Plan, remediation guide, or downstream QA-prep artifact derived from the Epic Plan MUST preserve the open-rails QA requirement unless it records the controlling PO-authorized exemption. Closed-rails proof, static validation, repository inspection, generated evidence, or OPS observation alone does not erase a declared open-rails QA requirement.  
    
* **Review posture:** A reviewer MUST block QA-plan approval or QA-readiness posture when a user or production-surface epic omits the required bounded open-rails QA step and also omits a controlling PO-authorized exemption. The blocker language must identify the affected surface, such as CLI, vendor ingestion, vendor transport, runtime persistence, public app behavior, or deployed service behavior.  
    
* **Vendor-call ownership for Glow app integration:** If an epic or implementation plan involves Glow app integration, it MUST state which component owns vendor calls, BodyGraph persistence and retrieval, and HD Engine compute. The default planning posture is that the HD Engine owns vendor acquisition, persistence-facing behavior, retrieval-facing behavior, and compute-facing behavior; app shell responsibilities must be distinguished from HD Engine responsibilities.  
    
* **Direct app vendor calls:** Any plan proposing direct app-side vendor calls or bypass of the HD Engine vendor seam requires explicit ADR justification and must name the secret boundary, app-to-engine contract boundary, and raw vendor-data boundary.  
    
* **Vendor payload normalization posture:** If an epic, implementation plan, remediation guide, or QA plan involves vendor payload normalization, response mapping, BodyGraph resolution, cache compatibility, compatibility input shape, or replacement of a legacy vendor path, it MUST state whether the slice proves a real normalized data-path adapter, implements a runtime adapter, or only records an adapter/schema gap.  
    
* **Adapter/schema gap nonclaims:** If adapter/schema proof or implementation is not included, the plan MUST explicitly state that it does not claim vendor chart data feeds the existing BodyGraph cache, person/cache contract, compatibility compute path, full vendor runtime conformance, legacy ingest replacement, or parent-task completion beyond the scoped evidence slice.  
    
* **Future proof requirement:** A plan that later claims vendor chart data is compute-ready MUST identify the vendor payload family used, the required vendor response fields, the internal BodyGraph/person/cache fields populated, fields intentionally absent or unsupported, whether any legacy fallback remains, whether the adapter is sufficient for HD Engine compute, and whether raw vendor payloads are persisted, redacted, summarized, or excluded.  
    
* **`bg:resolve --source vendor` route-policy posture:** If an epic, implementation plan, QA plan, remediation guide, or review artifact involves `bg:resolve --source vendor`, vendor-backed BodyGraph resolution, or future BodyGraph-detail runtime compatibility, it MUST state whether the path is v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim.  
    
* **`bg:resolve` nonclaim language:** If `bg:resolve --source vendor` is not covered by the slice, the plan MUST explicitly state that it does not claim `bg:resolve` resolves complete BodyGraph detail, does not claim `charts/simple` success proves full BodyGraph resolution, and does not claim canonical v2 BodyGraph-resolution runtime compatibility.  
    
* **Simple chart smoke boundary:** Plans MUST NOT treat `charts/simple` success, auth success, geocode-key success, provider availability, or minimal route-family confirmation as proof that `bg:resolve --source vendor` can resolve complete BodyGraph data.  
    
* **Route-family proof requirement:** A plan that claims `bg:resolve --source vendor` works must identify the selected route family, base-url/config strategy, fallback posture if any, payload family, normalized internal output, and evidence showing that BodyGraph detail is sufficient for HD Engine compute without raw secret or uncontrolled raw vendor payload exposure.  
    
* **Configured-v2 mapped-cache persistence state separation:** Future plans touching configured-v2 BodyGraph cache persistence, non-dry-run v2 chart-backed resolution, mapped-cache writes, read-back proof, or production upsert reopening MUST distinguish these states:  
    
  * v2 dry-run mapping works.  
  * v2 mapped output can feed compatibility computation.  
  * v2 mapped output can be durably written and read back from the BodyGraph cache.  
  * v2 mapped-cache writes are authorized for production or production-like operation.


* **Mapped-cache nonclaim language:** A plan MUST NOT treat dry-run mapping, compatibility computation, adapter mapping, route-policy proof, provider availability, or bounded live smoke as proof that durable mapped-cache writes or production-like mapped-cache writes are supported.  
    
* **Later-phase sequencing:** If durable mapped-cache writes are proposed, the plan MUST route the work through the appropriate later phased PF09 document and must not skip directly from dry-run or compatibility evidence to production persistence. The safe planning sequence is dry-run evidence, mapped-cache write/read-back proof, controlled non-prod repeatability, then production authorization decision.  
    
* **Mapped-cache proof requirement:** A plan that claims durable mapped-cache persistence must identify the mapped cache shape, cache-compatible identifiers and types, write/read-back parity proof, idempotence proof, no-raw-vendor-payload persistence proof, closed-rails refusal preservation, governed evidence outputs, and whether any legacy non-v2 fallback remains.  
    
* **Production reopening proof requirement:** A plan that claims production or production-like configured-v2 upsert support must identify the production-policy decision, environment and DB connectivity posture, controlled writer or upsert evidence if authorized, rollback or refusal evidence, no-secret proof, no-raw-vendor-payload persistence proof, public Reader no-change posture unless separately scoped, and governed index, mirror, and path-proof updates.

Review posture:

* Missing Contract and Compatibility Posture is blocking and MUST be returned for revision.  
    
* A "verified later" placeholder is not acceptable for backward-compat posture. If the epic cannot state it yet, the plan MUST be revised before execution.

#### **Existing Work Check (MUST)**

Before any new implementation work is planned or started for this epic:

* **Existing features review (summary):**  
  * What features, flows, or components already cover part of this intent?  
  * What prior epics or PF10 build notes are relevant (titles/IDs only)?  
* Existing acceptance evidence reviewed:  
  * Identify the existing PF, ADR, epic, task, acceptance criterion, test, PR, commit, workflow run, or governed artifact that already proves part of the intended scope.  
  * Record exact identifiers or authoritative pointers rather than restating their contents.  
* Legacy token references reused, if explicitly scoped:  
  * List only exact historical token references that this epic explicitly reuses without reissuing or reinterpreting them.  
  * State `None` when no scoped legacy token reference is used. Absence of a legacy token reference is not a readiness blocker.  
* Existing evidence located:  
  * Provide authoritative pointers to the relevant governed artifacts, indexes, mirrors, path proofs, workflow records, or decision records.  
* Gap statement:  
  * State what remains unproven, stale, contradictory, or outside the exact scope of the existing evidence.

**Rule (normative):**

> No new work is scoped for this epic until the Existing Work Check is filled in and reviewed. This applies to **features, governing requirements, existing evidence, and any explicitly reused legacy token reference**. If this section is blank or obviously stale, the epic is **not ready** to enter “In Progress”.

#### **Deliverables (Jobs To Be Done)**

**Ops task note (when applicable):**

If any deliverable includes **Ops tasks** (human console/config actions or other privileged external-system changes):

* The Epic Record MUST separate OPS tasks from DEV/PR work and MUST label OPS tasks as **PO-authorized, IA-guided, not PR work**. The PO may execute personally or explicitly delegate to an automated session agent under the task-specific controls in the Ops Task Record.  
    
* Each OPS task MUST be specified using the required Ops Task record fields defined in PF27 §3, including: Task ID, intent, constraints/rails, success criteria, evidence to capture (repo path), rollback intent, and secret handling note.  
    
* Ops-task completion MUST be proven by evidence in `audit/ops/<epic-id>/<task_id>/`. A corresponding QA evidence pointer in `audit/qa/<epic-id>/<task_id>/` is required only when the Ops task produces QA evidence.  
    
* Any Ops task included in the epic MUST use the HDE work-item mapping fields under **PF Reference Map**, preserving the same Work item ID and exact phased document, task, and subtask identity.

**Evidence-only deliverables (allowed; not acceptance tokens by default).**

Some deliverables are required evidence artifacts but are not acceptance tokens unless Governance registers tokens and defines their semantics.

Default posture (normative): guard proofs (example: serializer/emitter guard proofs) are **evidence-only deliverables**, not acceptance tokens.

* Plans MUST NOT introduce or claim new “guard tokens” unless the token exists in the canonical token registry owned by HDE Governance.  
    
* Evidence-only does not mean loose: guard proof artifacts MUST be mechanically generated, reviewable, and (when used for closure wiring) follow normal governed-evidence discipline (stable path; index/mirror updates when bytes change; sibling path proofs when required by Evidence Catalog posture).

List **concrete, observable deliverables**; each should be testable:

* **Deliverable D1:**  
  * *Job to be done:*  
  * *Evidence required:* (artifact titles, mirror records, snapshots; titles-only)  
  * *PF references:* (PF titles \+ sections, e.g. “PF14 — HDE Mechanics Guide §1.3 Evidence & CI coupling”)

Repeat D2, D3, and additional deliverables as needed.

These deliverables should map cleanly to PF06 PR plans, PF09 CI jobs, and PF19 QA playbooks (titles-only).

**QA deliverable note (when applicable):**

If a deliverable’s scope includes Live QA, QA tooling bootstrap, QA harness discipline, acceptance-map viability, or other QA\_ROOT evidence production:

* The deliverable’s “Evidence required” list SHOULD name the **intended QA outcomes** (names-only) and the **expected evidence families** (titles-only), and MUST route the detailed runbook/commands/step sequence to “Glow QA Guide” and “Epic Process Guide” (titles-only).  
* Any artifact treated as Live QA evidence MUST be produced mechanically by commands (shell/scripts/tools). Manual editor fill is prohibited for QA evidence files. Placeholder fields such as “(fill PASS/FAIL)” are non-conforming in approved QA plans and templates.  
* The HDE Epic Plan MUST NOT embed a Live QA runbook, including commands, step-by-step checks, QA\_ROOT directory design, README generator rules, or per-step artifact layouts. Those are authored as separate QA work products during Close Gate execution. PF20 remains historical reference material and is not the current planning authority.  
* When a deliverable claims a “local bundle” directory (for example `artifacts/ops/internal_version/*`), its “Evidence required” list MUST be a complete inventory of required evidence paths (titles-only), and MUST explicitly list any shared/global evidence dependencies that live **outside** the local bundle directory (for example determinism env pins logs), rather than assuming they are implicit.

#### **PF Reference Map**

Summarize **which PF docs and sections this epic leans on** (no duplicated bytes):

* **Core:**  
  * PF21 — 7 Phases of Alchemical Engineering (§phase used)  
  * PF06 — Epic Process Guide (§0.4 Execution posture and flow; §2.x as applicable)  
  * HDE Build Checklist phase document — `<exact current in-document PF09.1 through PF09.7 title>`; `<exact task or subtask ID and heading>`  
  * PF19 — Glow QA Guide (§2 Pre‑commit QA; §5 Component playbooks; §11 Roles)  
* **Additional (as needed):**  
  * PF01 — HDE Math Spec  
  * PF02 — HDE Architecture  
  * PF04 — HDE Governance  
  * PF05 — HDE CLI‑API‑Vendor Ref  
  * PF12 — HDE Schemas & Artifacts  
  * PF14 — HDE Mechanics Guide  
  * PF17 — HDE Narratives Guide

**HDE work-item mapping fields (repeat for every task-like item):**

| Field | Value |
| :---- | :---- |
| Work item ID | `<stable local identity>` |
| PF09 disposition | `in the current epic with exact phased PF09 task or subtask mapping` | `out of the current epic with exact phased PF09 task or subtask mapping` | `PF09 gap` | `documentation/status drainage only` | `out of HDE phased-build scope` |
| Phased PF09 document | `<exact current in-document title>` or `N/A` for a non-mapping posture |
| Task ID | `<exact task ID>` or `N/A` |
| Subtask ID | `<exact subtask ID>` or `None exists` after verification |
| Exact source heading | `<exact task or subtask heading>` |
| Contribution | `<advances, satisfies, leaves open, or documents>` |
| Status nonclaim | `<state that this artifact does not itself move PF09 status>` |

Only **list titles and sections** here; do not restate content.

#### **Exact-Source Evidence and Acceptance**

This section records PF27-owned template fields only. Acceptance semantics and strict-claim boundaries are owned by `PF04-Canon-HDE-Governance`; QA verdict requirements are owned by `PF19-Canon-Glow-QA-Guide`; evidence schemas, integrity rules, and canonical paths are owned by `PF12-Canon-HDE-Schemas-and-Artifacts`.

* **Governing acceptance scope:** identify the exact PF, ADR, epic, task, acceptance criterion, test, schema, or other governed requirement applicable to each planned claim.  
* **Repository and source identity:** identify the repository and current planning baseline. State how the exact implementation or QA candidate will be bound at execution and review time.  
* **PR identity, when a PR is used:** require the PR number, base SHA, reviewed head SHA, relied-upon exact-head CI, review record, merge SHA, and post-merge repository fact as applicable.  
* **Direct-main identity, when explicitly authorized:** require the exact post-write SHA, diff, applicable push-CI result, and truthful pending or failing posture. This field records evidence and does not authorize mutation.  
* **Workflow and QA evidence:** identify the applicable workflow, exact tested SHA, check set, conclusion, governed reports, manifests, indexes, mirrors, path proofs, or attestations required for the changed surfaces.  
* **Decision requirement:** identify the required QA or acceptance decision-maker, decision scope, decision record, and limitations without claiming an unissued decision.  
* **Evidence proportionality:** tie each evidence requirement to the changed surface, protected risk, governing predicate, or integrity obligation. Do not require an unrelated full-suite, roster, matrix, or artifact family solely because an earlier epic used it.  
* **Legacy token references, if explicitly scoped:** list only exact PF04 names used as bounded historical or optional cross-references. No token list is required when no active scoped legacy token use exists, and values are never inferred from PASS status or another record.  
* **PF09 scope/status binding:** record exact work-item mapping separately from acceptance evidence. A mapping, repository fact, CI result, QA verdict, legacy token reference, or artifact hash does not itself move PF09 status.  
* **Non-token obligations and nonclaims:** record the behavior, compatibility, workflow, proof, OPS, deployment, release, acceptance, and closure claims that remain unestablished.

Use authoritative pointers instead of duplicating information that GitHub or a governed repository artifact already records reliably. This template creates no replacement token database, universal acceptance form, or token-evidence matrix.

#### **QA Rails — Open/Close (Final PR)**

This section defines what an Epic Record is allowed to state about QA for the **final PR that closes the epic**.

**Hard boundary (Epic Plan vs QA execution canon):**

PF20 remains historical reference material. It is not current planning authority and requires no historical rewrite.

The HDE Epic Plan stages QA expectations only at the level of:

* rails posture expectations, including closed or opened rails;  
* governing acceptance criteria and exact-source evidence references;  
* active scoped legacy token references only when explicitly used; and  
* titles-only pointers to the governing QA documents and close-pack artifacts.

The HDE Epic Plan MUST NOT include QA planning artifacts or execution detail, including:

* runbooks, commands, or command blocks;  
* step sequences or step-level plans;  
* embedded checklists or operator instructions;  
* per-step PASS/FAIL criteria;  
* QA\_ROOT subdirectory layout design, evidence directory naming schemes, or README generation rules; or  
* CI self-test design details.

These QA execution details are authored as separate QA artifacts during Close Gate execution and are governed by “Glow QA Guide” and “Epic Process Guide” by title.

**A. Final PR rails posture (staged configuration; NOT a runbook)**

For the final close PR, the Epic Record MUST make the rails posture explicit and auditable without prescribing how to run QA:

* **Closed rails default:** Final-PR CI and any acceptance-relevant proof runs are expected to operate under closed rails by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).  
* **Opened rails exception discipline, if applicable:**  
  * If any acceptance-relevant job or run is expected to open rails, the Epic Record MUST state that an opened-rails exception exists and identify its scope.  
  * The Epic Record MUST require evidence for **closed refusal** and **open conformance** to be captured and indexed or mirrored in the same PR when required by the governing QA posture.  
  * The Epic Record MUST NOT describe the procedure, job recipe, steps, commands, or operator guidance.  
* **Evidence handling:** Where the epic requires rails-related QA evidence for close, the Epic Record MAY point to the relevant governed artifacts that contain the evidence bindings. It MUST NOT duplicate the evidence content or its production procedure.

**B. Live QA requirement (closeout statement only)**

Live QA is required for eventual epic close.

* The Epic Record MUST include a single statement that Live QA is required for close and MAY name the governing documents by title.  
* The Epic Record MAY identify the exact governing acceptance criteria and evidence families required at close.  
* The Epic Record MAY list active scoped legacy token references that must be satisfied at close only when that bounded token use is explicit. No token list is required otherwise.  
* The Epic Record MUST NOT embed a Live QA plan or runbook, including commands, step sequences, QA\_ROOT directory design, evidence directory naming, README generator rules, or CI self-test design.

**C. QA-heavy epic guidance (planning rule)**

QA-focused epics must not exist solely to test themselves. QA-heavy work SHOULD either:

* upgrade shared QA harness or tools; or  
* strengthen Live QA coverage across multiple existing surfaces and epics.

**D. Legacy token references (optional)**

When an Epic Record explicitly uses a bounded legacy token cross-reference, list the exact current PF04 name and its authoritative evidence pointer. Do not include a token roster or default example set when no active scoped legacy token use exists. Historical token names remain in historical records and are not reissued by default.

#### **Tracked Issues**

When closing an epic, the epic record MUST include a list of **tracked intra-epic issues** and their final status for this epic.

In this document, an **issue** is any *unexpected* condition, behavior, gap, or risk discovered during implementation or QA, not a synonym for “deliverable” or “task.” An issue exists when reality diverges from the current plan or canon (for example: failing or flaky tests, ambiguous or conflicting specs, misaligned tools, missing or inconsistent evidence, surprising runtime behavior, or hard environment constraints such as “no user IDs in prod”). Planned work items, epics, and deliverables do **not** automatically become issues just because they are incomplete; they are tracked as issues only when there is something structurally blocking, surprising, or unclear about them (for example: “cannot be done under current rails,” “spec is incomplete,” or “tooling cannot represent required behavior”).

Every tracked issue must end the epic in one of these states:

* **Completed under this epic**  
    
* **Carried forward to another epic** (with a concrete epic ID)  
    
* **Promoted to a cross-epic issue** (ISSUE-XXX in §1 “Outstanding Issues”)  
    
* **Explicitly dropped** (with a one-line rationale)

For each tracked intra-epic issue, the epic record SHOULD provide at least:

* **Issue ID** (e.g. `ISSUE-<EPIC>-<NAME>` or a short label if no ID is minted)  
    
* **Title** (short, descriptive name)  
    
* **Status** (for example: `Completed under <EPIC-ID>`, `Carried forward to <EPIC-ID>`, `Cross-epic ISSUE-XXX`, `Dropped`)  
    
* **Scope / description** (1–3 sentences explaining what the issue covers)  
    
* **Disposition for this epic** (brief note describing what happened to this issue in this epic: proved, carried forward, cross-epic, or dropped)

When listing issues:

* **Issues completed:**  
    
  * Short list of issues whose **Status** is “Completed under \<EPIC-ID\>,” linking to §1 “Outstanding Issues (Cross-Epic)” where relevant.


* **Issues not done / out-of-scope:**  
    
  * For each, make the disposition explicit:  
      
    * **Moves to another epic:** name the destination epic ID.  
        
    * **Becomes a new cross-epic issue:** give the ISSUE-XXX ID in §1.  
        
    * **Explicitly dropped:** include a one-line rationale (“no longer aligned with current product scope,” etc.).

**Rule (normative):**  
No epic is closed as “Done” while silently dropping known issues. Every known issue must be: **proved, carried forward, promoted to a cross-epic ISSUE-XXX, or explicitly dropped** in this section, with statuses and destinations clearly recorded.

#### **Plan Preflight (MUST)**

**PF23 consult (planning gate).**

* Before an Epic Record is treated as ready for approval (or promoted to “In Progress”), planners MUST consult **PF23 — Reality Audits** as a primary input for:  
    
  * component boundaries (what the “thing” is), and  
      
  * canonical pathnames/loci (where it lives).


* Epic Records SHOULD include a short “PF23 Anchors” trace that lists the component(s) consulted and the key pathnames/loci this epic will touch (traceability only; do not duplicate PF23 contents).  
    
* PF23 is PO-maintained. If PF23 appears stale or missing required coverage, the epic record MAY note that as an observation, but MUST NOT assign PF23 updates as agent work.

Before an Epic Record is treated as **ready for approval** (or promoted to “In Progress”), the following MUST be true.

**Scope boundary (hard rule): Plan Preflight is Epic Planning only — not QA planning.**

* The HDE Epic Plan MUST NOT contain QA runbooks.  
* The HDE Epic Plan MUST NOT include QA execution instructions, including:  
  * step-by-step procedures;  
  * command lines;  
  * environment setup or Step-0 snapshot procedures;  
  * Codespaces operator instructions;  
  * manual PASS/FAIL fill fields; or  
  * another runbook-style operational checklist.  
* When an epic requires QA execution, including Live QA, the HDE Epic Plan may capture only planning-level outcomes:  
  * exact governing acceptance criteria and source identifiers;  
  * expected evidence families and canonical evidence paths;  
  * applicable PR, commit, workflow, test, and governed-artifact references;  
  * active scoped legacy token names only when explicitly used; and  
  * titles-only references to the canonical QA and runbook homes.  
* Any runbook, QA plan, QA checklist, or QA execution rail belongs in its single current canonical home. PF20 remains historical reference material and is not the planning authority for this transition.

**A. Legacy token validation (conditional planning gate)**

When no active scoped legacy token use exists, the plan MUST NOT require a token roster, token-registry lookup, per-step token declaration, token claim, or token-evidence matrix. Their absence does not block plan approval when the governing requirements and exact-source evidence plan are otherwise complete.

When a plan explicitly uses a bounded legacy token reference:

* the name MUST match the current PF04 registry exactly and remain names-only;  
* the plan MUST identify the exact governed requirement and evidence relationship for that reference;  
* an unregistered or misspelled name blocks that token claim only and MUST NOT be normalized by guesswork;  
* the underlying requirement MAY be represented as a non-token obligation with its exact predicate and governed evidence when token authority is absent; and  
* the plan MUST NOT mint a replacement token or treat token registration as proof of the predicate.

Deprecated alias compatibility:

* `QA_STEP_LOGS_CONSOLIDATED_OK` remains a deprecated alias for `QA_HARNESS_DISCIPLINE_OK`.  
* A new artifact that explicitly carries the corresponding active scoped legacy claim uses the current PF04 name rather than the deprecated alias.  
* Existing historical records retain their historical spelling and MUST NOT be bulk-rewritten or reinterpreted.  
* Encountering the deprecated alias in current prospective plan text is DOC\_DRIFT for drainage; it does not require unrelated artifacts or step logs to claim `QA_HARNESS_DISCIPLINE_OK`.

Plan approval is blocked only when an explicitly required acceptance claim remains unsupported after this classification. Absence of a legacy token reference is not itself a blocker.

**B. Close-pack baseline declared (planning gate)**

* The Epic Plan MUST explicitly list the required close-pack artifacts (titles-only) for the epic close stage.  
    
* Close-stage baseline surfaces MAY be listed in the Epic Plan at planning level without turning the Epic Plan into a QA runbook. The plan MUST keep QA commands, step logs, operator procedures, and runbook execution detail out of the Epic Plan unless a separate QA artifact explicitly owns them.  
    
* Missing close-stage execution detail in an Epic Plan is not, by itself, a valid reason to defer implementation or QA. The plan must preserve the required close-pack baseline while routing execution detail to the owning QA, OPS, or closeout artifact.  
    
* At minimum, the close-pack baseline MUST include:  
    
  * the epic close report, and  
      
  * the epic manifest, and  
      
  * the epic acceptance map, and  
      
  * the token→evidence matrix (when required by the QA posture for that epic), and  
      
  * the acceptance-map viability log at `audit/qa/<epic-id>/acceptance_map_viability.log` (when the epic carries an acceptance map or token→evidence matrix as part of the close-pack posture).


* Close report minimum required fields (required):  
    
  * Canon pointer fields: the close report MUST include explicit canonical path pointers to the plan’s declared close-pack artifacts (at minimum: the close report path itself, the deterministic path-of-record selection, and any declared manifest, acceptance map, token→evidence matrix, and acceptance-map viability paths).  
      
  * TI-002 mapping (when TI-002 is claimed): the close report MUST include an explicit mapping from TI-002 to the satisfying governed artifact(s), including (a) artifact path(s) and (b) a minimal excerpt or other precise locator sufficient to audit the claim without guessing.  
      
  * For any other token claims that require explicit mapping, apply the same mapping rule as TI-002.  
      
  * Workflow-truthfulness fields: if the close report states that a governed write, refresh, validation, or close-pack workflow ran, it MUST point to the same-run governed artifact(s) or gate-log artifact(s) that prove the execution, rather than reporting the action as narrative-only.


* Reused-proof-family fields: if the close-pack reuses already-existing proof families from earlier deliverables or PR slices, the close report MUST identify those reused proof families by exact governed artifact path and MUST NOT present them as newly implemented in the close slice.

**Close-pack deterministic path-of-record (normative).**

MUST locate the close-pack pair at the canonical audit/ paths using the `EPIC-###` pattern (3 digits):

* `audit/EPIC-###_close_report.md`  
    
* `audit/EPIC-###_MANIFEST.json`

These are baseline close-pack artifacts (required closure artifacts), not acceptance tokens.

MUST NOT relocate these artifacts into alternative directory trees (example: `audit/qa/**`, `artifacts/**`) without an explicit canon change.

**Close-pack manifest key\_outputs binding map (normative).**

`audit/EPIC-###_MANIFEST.json` MUST include `key_outputs` as a JSON object (map):

* each key is a stable pointer name (string)  
    
* each value is a repo-relative artifact path (string)  
    
* when the close-pack baseline includes an acceptance map, token→evidence matrix, or acceptance-map viability log, `key_outputs` MUST include explicit named bindings for each declared close-pack artifact.  
    
* when the close-pack binds reused proof families or same-run gate execution evidence, those reused proof artifacts and governed gate-log artifacts MUST appear as explicit named `key_outputs` bindings.

`key_outputs` MUST NOT be a list.

Close-pack validation checks MUST validate the named bindings (keys \+ exact paths), not list membership.

**Doc-delta surfaces (required; two-surface pair; names-only baseline).**

The Epic Plan MUST declare both doc-delta surfaces (concrete filenames; no placeholders):

* Draft/staging surface (token-evidence binding surface): `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase epic-id)  
    
* Epic-scoped capture surface (stable QA record): `audit/qa/<epic-id>/00_meta/doc_deltas.md`

Binding rule (normative): token↔evidence bindings reference the draft/staging surface; the epic-scoped capture file is the authoritative narrative/record surface.

* Epic Plans MUST NOT be considered approvable if they omit this close-pack baseline and doc-delta baseline file set for eventual epic close.

**C. Evidence bundle completeness for local-bundle deliverables (planning gate)**

When a deliverable claims a “local bundle” directory (example: `artifacts/ops/internal_version/*`):

* The deliverable’s “Evidence required” list MUST enumerate the complete required evidence paths (titles/paths only).  
    
* If any required evidence lives outside the local bundle directory, the plan MUST name it explicitly and give its canonical path (titles/paths only), rather than assuming it is implicitly available.

**D. Canonical evidence-path binding validation (planning gate)**

Authority order (hard):

* Canonical artifact paths and sibling path-proof transcript naming are defined by PF12.  
    
* PF09 defines required checks/gates but MUST bind to PF12-defined canonical paths and filenames (no alternate path strings).  
    
* Status vocabulary for PASS/FAIL and tooling states is defined in PF19; do not invent new status strings.  
    
* Any legacy path string encountered in other PF text is treated as DOC\_DRIFT: plans MUST bind to PF12 canonical paths and record a Doc Delta rather than copying the legacy string forward.

The Epic Plan MUST validate each named evidence pointer is bound to a canonical surface in the “HDE Schemas & Artifacts” evidence catalog (exact path string, including case).  
Any non-canonical binding is a mechanical blocker unless it is explicitly routed via an ADR.

**Minimum required evidence pointers (stable contract):**

* Close-pack pair:  
    
  * `audit/EPIC-###_close_report.md`  
      
  * `audit/EPIC-###_MANIFEST.json`


* Evidence Index:  
    
  * `docs/evidence/INDEX.json`  
      
  * `docs/evidence/INDEX.sha256`


* Machine Mirror (canonical mirror home):  
    
  * `artifacts/evidence_index.jsonl`  
      
  * `artifacts/evidence_index.jsonl.sha256`  
      
  * `artifacts/evidence_index.jsonl.path_proof.txt`


* Evidence index snapshot (only if the plan includes D23):  
    
  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
      
  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

Validator failure posture (execution-time status mapping):

* If validator can run and detects evidence exists but bindings do not match PF12 canonical paths, status is FAIL\_BEHAVIOR.  
    
* If missing required canonical inputs (evidence does not exist or not readable), status is TOOLING\_BLOCKED.

Acceptance artifact hygiene (mechanical, plan-gate rule):

* Token names in acceptance artifacts MUST pass PF04 token registry validation; no legacy spellings or aliases.  
    
* `audit/EPIC-###_MANIFEST.json` MUST reference canonical paths and include path-proof transcript pointers where required.  
    
* Any path-proof transcript MUST use the canonical suffix `<artifact>.path_proof.txt`.  
    
* The plan MUST explicitly list each path-proof transcript file that will be included in close-pack using explicit filenames such as `<ARTIFACT_NAME>.path_proof.txt` (no pattern placeholders).

Prohibited placeholders: informal stand-ins such as curly-brace placeholders. Any unresolved material decision MUST use the Remediation Implementation Guide's **Open Decisions** contract; no other placeholder form is permitted.  
Use `<PLACEHOLDER_NAME>`, `[OMITTED]`, `[LIST CONTINUES]`, `[SNIP: <n> lines omitted]`, or `[INTENTIONALLY LEFT BLANK]`.

**Canonical JSON gates (directory binding rule; normative).**

* Canonical JSON gate artifacts MUST bind to the single family: `audit/gates/json_gate/canonical/`  
    
* At minimum, the canonical family includes:  
    
  * `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
      
  * `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
      
  * `audit/gates/json_gate/canonical/json_gate_structured_record.json`  
      
  * plus sibling `*.path_proof.txt` files for the above, as defined by the owning canon.


* Plans and acceptance artifacts MUST NOT require, invent, or dual-home canonical JSON gate bindings across multiple families. The following are legacy/compat-only and MUST NOT be treated as canonical acceptance surfaces unless canon explicitly reinstates them (via PF12):  
    
  * `audit/gates/canonical_json/*`  
  * `audit/gates/canonical_json/json_canonical_check.log (legacy catalog check report; compat-only; do not bind new plans to this path)`  
  * `audit/gates/canonical/*`

**Evidence index snapshot artifacts (directory binding rule; normative).**

* Canonical generator command (repo-local; copy/paste): `python tools/evidence/generate_evidence_index_snapshot.py` (not `run_evidence_index_snapshot.py`).

When an epic produces an evidence index snapshot as part of QA execution (D23 Evidence Index Snapshot):

* Canonical artifact surfaces (already governed):  
    
  * Snapshot JSON: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`  
      
  * Snapshot path proof: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`


* Snapshot JSON schema (must match exactly):  
    
  * `schema_version` is `1`  
      
  * `generated_at_utc` is a valid RFC3339 UTC timestamp  
      
  * `inputs` (object):  
      
    * `human_index_path` (string; must be `docs/evidence/INDEX.json`)  
        
    * `human_index_sha256` (string; lowercase hex SHA256)  
        
    * `machine_mirror_path` (string; must be `artifacts/evidence_index.jsonl`)  
        
    * `machine_mirror_sha256` (string; lowercase hex SHA256)

    

  * `parity` (object):  
      
    * `artifact_keys_match` (boolean)


* PASS predicate (mechanical; tokenless):  
    
  * `schema_version` is `1`  
      
  * `inputs.human_index_path` equals `docs/evidence/INDEX.json`  
      
  * `inputs.machine_mirror_path` equals `artifacts/evidence_index.jsonl`  
      
  * `inputs.human_index_sha256` matches SHA256(raw bytes of `docs/evidence/INDEX.json`)  
      
  * `inputs.machine_mirror_sha256` matches SHA256(raw bytes of `artifacts/evidence_index.jsonl`)  
      
  * `parity.artifact_keys_match` is true


* Status mapping:  
    
  * If required canonical inputs are missing or unreadable (for example: the index or mirror does not exist at the canonical path), status is TOOLING\_BLOCKED.  
      
  * If any predicate condition fails (schema mismatch, hash mismatch, parity false), status is FAIL\_BEHAVIOR.


* Token posture:  
    
  * This check is tokenless. Do not claim acceptance tokens from this snapshot.


* Epic-local variants:  
    
  * An epic may carry a non-canonical copy under `audit/qa/hde-epic<NNN>/` for convenience, but it MUST NOT be treated as a closure-required canonical surface and MUST NOT replace the canonical evidence index pair.

**Canon-defined compare artifact surfaces (current; non-exhaustive).**

* Arrays-as-sets compare report (CHECK `D05_arrays_as_sets`): `artifacts/canonical/arrays_as_sets_report.log`  
    
* The owning check’s `primary.log` MUST (a) capture the exact command executed that produced this report (verbatim) and (b) point to the stored report artifact path above (no prose-only assertions).  
    
* Plans MUST NOT bind acceptance to a different arrays-as-sets report path (example: `audit/gates/arrays_as_sets/arrays_as_sets_report.md`) unless introduced via ADR \+ doc-delta and drained into PF-Canon.

**Canonical compare artifacts (no epic-local paths; normative).**

* Compare evidence MUST reuse canon-defined compare artifact surfaces.  
    
* An epic MUST NOT introduce a new compare artifact path as “the canonical compare proof” unless that path is explicitly introduced via ADR \+ doc-delta and drained into the owning PF-Canon homes.

If canon does not define a compare artifact surface for the needed proof, treat it as a canon gap and resolve it before the epic binds acceptance to a new path.

**E. Lowercase directory naming (planning gate)**

All directory names used in Epic Records, evidence paths, and expected artifact layouts MUST be lowercase ASCII. Mixed-case or uppercase directory names are non-conforming and MUST NOT be introduced into new plans.

## **3\) Ops Task Record (Template)**

### **Definition**

An **Ops task** is any work item that requires privileged access to systems outside the repository and therefore requires Product Owner authorization. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent acting on the PO's behalf. This includes (non-exhaustive):

* service configuration  
* secrets / env var changes  
* deploy / runtime settings  
* infrastructure console actions  
* live or shared Glow database access that crosses the repository boundary or uses privileged database credentials  
* certain database operations (creation, grants, production migrations, other privileged state changes)

### **Execution authority (normative)**

* Ops tasks **MUST** be authorized by the **PO**.  
* The PO **MAY** execute an authorized task personally or explicitly delegate execution to an automated session agent.  
* Throughout PF27, **PO-only** identifies the owner of authorization, accountability, and acceptance. It does not require the PO to be the physical keystroke actor when the PO directly delegates execution.  
* A delegated agent **MAY** perform the authorized operation on the PO's behalf and **MUST** follow the same scope, safety, evidence, redaction, and completion-claim controls that bind a human operator.  
* When the approved scope and task-specific predicates are satisfied, the delegated agent **MUST** proceed and **MUST NOT** refuse solely because it is not human or demand a second generic human-only approval.  
* Automated agents **MUST NOT** act without explicit PO delegation, independently approve an operation, invent missing commands, widen scope, bypass a required task-specific approval, simulate external state changes, or claim completion without the required evidence.  
* System, platform, host, service-provider, organizational, legal, and safety controls remain binding and cannot be overridden by PO delegation.  
* Delegation does not authorize an automated session agent to edit PF-Canon contrary to canon-maintenance controls.

### **IA facilitation posture (normative)**

* Ops tasks **MAY** be part of an epic. When included, they are facilitated by the **Implementation Agent (IA)**, who **MUST** guide the PO and any PO-delegated executor through preparation and execution.  
* IA guidance **MUST** specify **intent, constraints, verification, and evidence requirements**.  
* When canon already provides concrete operator instructions, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules for the task, the Ops task record **MUST** include those canon-grounded instructions explicitly.  
* If canon is silent, incomplete, or ambiguous, the Ops task record **MUST** state that the missing instruction is unknown and **MUST NOT** fabricate steps.

### **Not a PR (normative)**

* Ops tasks are **not** Codex PRs and **MUST NOT** be represented as “implementable PR work.”  
* Any plan/guide that includes both DEV work and OPS work **MUST** separate them and clearly label OPS work as: **PO-only execution, IA-guided**.

### **Ops Task record fields (required; what-not-how)**

Every Ops task record **MUST** include:

* **Task ID** (stable; referenced consistently)  
* **Owner:** `PO`  
* **Facilitator:** `IA`  
* **Executor:** `PO` or `PO-delegated automated session agent`  
* **PO delegation record, when delegated:** secret-free reference to the direct PO instruction, exact Task ID, operational objective, target, and approved scope.  
* **Task-specific authorization identity and dispatch-boundary validity, if required:** exact secret-free authorization artifact or identity, applicable validity predicate or window, and the required STOP CHECK immediately before dispatch.  
* **Objective blocker and resume posture:** concrete blocker, preserved safe work and evidence, exact PO value or external action required, and resume condition.  
* **PF07 posture:** `PF07-derived` or `PF07-gap`  
* **Infra/ops fact inventory** (as applicable):  
  * target provider  
  * target project  
  * target service  
  * target repository  
  * target base URL or port  
  * target database instance or schema  
  * exact config key name  
  * exact governed evidence root or QA root  
  * exact expected value or exact value source in PF07  
* **PF07 gap statement** (required when the exact value is missing from PF07; state the missing fact set and mark the affected task or claim blocked by missing PF07 infrastructure inventory)  
* **External execution classification, if applicable:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable  
* **Exact command proof or unresolved-command posture, if applicable:**  
* **Input identity boundary, if applicable:** state whether no app user IDs, no `person_uid`, no `user_id`, or other prohibited identity inputs are allowed.  
* **Secret persistence posture:** presence-only | redacted | hashed | not applicable; plaintext secret persistence is forbidden.  
* **Non-claims preserved:** state that delegation does not convert OPS into PR or QA work and that the task does not claim QA PASS, Live QA completion, acceptance-token satisfaction, PF09 status change, epic completion, deployment success beyond the evidenced target, or closeout.  
* **Completion-claim boundary:** no agent or human operator may claim OPS completion without the required repo-stored, secret-free evidence meeting the task success criteria.  
* **Intent / desired end state** (what changes; what “done” looks like)  
* **Constraints / safety rails** (what must remain true while executing)  
* **Success criteria** (observable outcomes; not assumptions)  
* **Closure dimension, if the task claims or supports closure** (exact environment, surface, or status dimension affected)  
* **Closure mode, if applicable:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Unchanged runtime facts already evidenced, if a non-runtime closure mode is used:**  
* **Governed evidence family to normalize, if applicable:**  
* **Superseded contradictory artifacts or reports, if any:**  
* **Evidence to capture** (what will prove the change; where it will be stored)  
* **Rollback intent** (what “revert” means at a high level)  
* **Secret handling note** (explicitly: no plaintext secrets in docs or evidence)  
* **Canon-grounded instructions, when available** (titles-only PF references; carry forward concrete operator steps, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules that already exist in canon)

**Controlled execution contract (required for exact-command, vendor-backed, external-smoke, or controlled-smoke ops tasks)**

Use this block when the Ops task depends on an exact command, external system, vendor-backed smoke, controlled network rails, or a proof classification that must be preserved before PO execution.

* **Command template or command source:** exact canon-backed command template, discovered command file, or unresolved-command posture.  
* **Command substitution source:** exact source for operator-substituted values, if applicable.  
* **Executable command artifact:** path where the final executable command must be stored before execution.  
* **Placeholder rule:** state how unresolved placeholders are detected and which classification applies if any remain.  
* **Target classification:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable | other approved classification.  
* **CLI-local smoke classification rule:** for a CLI-local smoke, do not require hosted-service PF07 facts unless the approved target classification changes to a hosted-service operation. The plan or Ops task must still prove CLI-local facts, including command target, data source, execution context, runtime or prerequisite binding when applicable, required config-key presence, determinism pins, rails posture, application environment, and secret-safe evidence posture.  
* **Required target facts:** command target, data source, execution context, required config keys, credential-presence keys, deterministic pins, rails posture, and application environment.  
* **Target facts not required for this classification:** state any infra fact that is not required and why.  
* **Target-change rule:** if the target classification changes, state which owning canon or approved live addendum must provide the replacement target fact set before execution.  
* **Prerequisite proof:** list any prior PR, OPS, QA, or canon proof that must exist before execution and state the classification if it is absent or contradicted.  
* **Preflight matrix:** for each preflight row, record requirement, required proof, and status rule.  
* **Execution wrapper or operator command:** exact wrapper or command posture the PO must use after preflight passes.  
* **Run rules:** state forbidden retries, guessed substitutions, command edits after failure, unauthorized or out-of-scope automated-agent execution, secret persistence, forced-PASS edits, execution before any required task-specific authorization is valid at the dispatch boundary, and any retry or changed authorization identity that requires fresh PO approval.  
* **Required evidence outputs:** concrete governed files to produce under the approved ops evidence root.  
* **Required content for evidence outputs:** exact content expectations for each required file, including command, input summary, environment posture, stdout, stderr, exit code, result summary, prerequisite matrix, and checksum ledger when applicable.  
* **Outcome classification map:** define exact PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, and TOOLING\_BLOCKED conditions for the task.  
* **Non-claims:** state whether the task does not claim QA PASS, Live QA completion, final acceptance, public-surface change, CLI flag change, PF09 status change, epic closure, or PF-canon drain completion.

### **Evidence posture (required)**

Ops tasks are required to capture evidence in governed paths and include path-proof transcripts where applicable.

When retained OPS evidence paths, filenames, formats, or run-root nesting diverge from approved plan deliverables, the plan, remediation guide, review artifact, or binding artifact may accept the retained evidence only when a manifest maps each approved deliverable name to the retained evidence path and status.

The manifest MUST state, for each mapped item, whether the retained evidence is equivalent by mapping, equivalent by content despite a name mismatch, partial and supplemented by another retained file, or not acceptable. It MUST identify supplemental files that complete a partial original capture.

Text or markdown summaries MAY be accepted as retained OPS evidence only when the approved task does not require machine-readable JSON semantics, or when the manifest explicitly states that the text or markdown file is not being treated as schema-governed JSON.

A nested run-label evidence root is acceptable only when the governed parent OPS root remains clear, the retained-path manifest is present, required sibling path proofs and index or mirror bindings are produced when promoted into governed evidence, and all nonclaims remain explicit.

**Evidence posture:**

**Artifacts:**

* `audit/ops/<epic-id>/<task_id>/` — Task work products for this ops task.  
    
* `audit/qa/<epic-id>/<task_id>/` — QA evidence for this ops task (only if the task produces QA evidence).

**Path proofs:**

* For any governed artifact path included in acceptance or close-pack, include the sibling path-proof transcript using the suffix `<artifact>.path_proof.txt`.

### **Build Checklist tracking requirement (normative)**

Every Ops task included in an epic **MUST** use the same stable Task ID in the task record and the applicable phased mapping. Complete these fields:

* **Work item ID:**  
* **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
* **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
* **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
* **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
* **Exact source heading:**  
* **Contribution:** advances | satisfies | leaves open | documents  
* **Status nonclaim:** this artifact does not itself move PF09 status

### **No governance drift (normative)**

Ops tasks **MUST NOT** create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it **MUST** map to existing acceptance posture and be proven via evidence artifacts.

## **3A) Epic Remediation Plan (Template)**

### **Scope**

Use this template only for a document explicitly identified as an **Epic Remediation Plan**. An Epic Remediation Plan is a distinct approval artifact for bounded, epic-scoped corrective work identified after implementation planning, post-implementation audit, QA-readiness review, or comparable current-state inspection.

An Epic Remediation Plan does not replace the controlling Epic Plan, a broader Implementation Plan, a QA Plan, a Live QA runbook, an OPS transcript, an acceptance review, or an epic-close record. It authorizes only its expressly bounded corrective scope.

### **Approval rule (normative)**

An Epic Remediation Plan **MUST** be reviewed on substantive correctness, execution safety, canon alignment, repository truth, evidence obligations, authorization boundaries, and decision completeness.

It **MUST NOT** be rejected, revised, or conditioned solely because it does not conform to an adjacent Epic Plan or Remediation Implementation Guide template.

Format, heading names, numbering, and ordering are non-blocking when the substantive requirements below are present and unambiguous.

This template does not supersede permanent canon governing architecture, PF09 mapping, tokens, evidence, OPS, QA, acceptance, or closure.

### **Execution and authority boundaries (normative)**

* An Epic Remediation Plan **MAY** contain bounded DEV and OPS steps and **MAY** embed the execution-oriented actions, commands, outputs, verification, and failure handling necessary to make the approved remediation executable.  
* For this plan type, OPS work, if any, remains Product-Owner-authorized, Implementation-Agent-guided, and evidence-bound. The PO MAY execute personally or explicitly delegate to an automated session agent under the same approved scope, safety, evidence, redaction, and completion-claim controls.  
* An Epic Remediation Plan **MAY** require a later QA-readiness reassessment.  
* An Epic Remediation Plan **MUST NOT** embed Live QA execution, issue a QA verdict, claim acceptance, move PF09 status, or close the epic unless separately authorized by the governing artifact and process.  
* PF, board, and status drainage **MUST** remain separate from DEV or OPS execution outputs and **MUST NOT** become approval, merge, QA-entry, acceptance, or closeout conditions by themselves.  
* Truth, proof, safety, or authorization failures remain substantive blockers.

### **Required structure (paste-ready)**

**Identity and baseline**

* **Artifact identity:**  
* **Visible version:**  
* **Epic identity:**  
* **Repository baseline, when repo truth matters:**

**Remediation trigger and current-state evidence**

* **Remediation trigger:**  
* **Current-state evidence:**

**Scope boundaries**

* **In scope:**  
* **Out of scope:**

**Canon and phased-build posture**

* **Controlling PF10 posture:**  
* **Controlling permanent-canon posture:**  
* **HDE work-item mapping (repeat per bounded remediation work item):**  
  * **Work item ID:**  
  * **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
  * **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
  * **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
  * **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
  * **Exact source heading:**  
  * **Contribution:** advances | satisfies | leaves open | documents  
  * **Status nonclaim:** this artifact does not itself move PF09 status

**Bounded remediation step**

* **Lane:** DEV | OPS  
* **Owner:**  
* **Dependencies:**  
* **Inputs:**  
* **Actions:**  
* **Outputs:**  
* **Verification:**  
* **Success criteria:**  
* **Failure handling:**  
* **Concrete evidence:**  
* **Governed-path posture for execution outputs:**

Repeat the bounded-remediation-step block for each DEV or OPS step.

**Authority and claim boundaries**

* **Token boundary:**  
* **OPS boundary:**  
* **QA boundary:**  
* **Documentation-drainage boundary:**  
* **Acceptance boundary:**  
* **Closure boundary:**

**Required dispositions**

* **ADR dispositions:**  
* **Tracked Issue dispositions:**  
* **Canon-gap dispositions:**  
* **Canon-reconciliation dispositions:**  
* **Scope-clarification dispositions:**  
* **Approval-item dispositions:**

**Approval**

* **Explicit approval sentinel:** `ASK OK?`

---

## **4\) Remediation Implementation Guide (Template)**

### **Scope**

This template applies to Remediation Implementation Guides produced for escalations and remediation execution. It does not change Live QA plan formats.

### **Copy/paste command safety (normative)**

If the guide includes command lines intended for copy/paste, default commands **MUST** be safe for the current epic context.

Commands included for operator use MUST be mechanically valid in-repo and MUST NOT be dead, ambiguous, or misleading.

Where a check/tool has a single canonical invocation form demonstrated by repo/CI usage, the guide MUST use that exact form as the default command. If multiple invocation variants exist, non-default variants MUST be labeled as non-default and the default choice MUST be justified as **Observed Evidence (non-PF)**.

Do not present an epic-id flag for a different epic as a default. If an `--epic-id` (or similar) flag is mentioned, it **MUST** either:

* match the current epic ID, or  
    
* be explicitly labeled optional/non-default with a one-line rationale.

### **Open Decisions**

If no open decision exists, state `None.` and do not include the marker below.

#### **Decision-bounded \[TBD\] rule (placement and coupling)**

This subsection is the only permitted home for `[TBD]`. Each unresolved material placement or coupling decision MUST use a unique `OD-001`\-style record:

* **Decision ID:**  
* **Decision:**  
* **State:** `[TBD]`  
* **Plausible options:**  
* **Decision criteria:**  
* **Fail-closed validator or test:**  
* **Dependent step, path, or claim:**  
* **Decision authority:**  
* **Resolution source:**  
* **Resolution effect:**

Unbracketed placeholder spelling is prohibited. The marker is prohibited outside this subsection and in paths, commands, token names, schemas, environment keys, acceptance predicates, and safely discoverable facts. A dependent step MUST NOT execute or claim PASS until the decision is resolved and the selected option is bound to its enforcing validator or test. Resolution replaces the marker; it is not retained beside the answer.

### **Closure-mode declaration (required when closure is claimed without a new runtime exercise)**

If the guide intends to close or recommend closure for an environment, surface, or other closure dimension by binding-equivalence, substitution, or documentation/evidence normalization rather than by a newly exercised runtime, it MUST state all of the following explicitly:

* **Closure dimension:** exact environment, surface, or status dimension affected.  
* **Closure mode:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only.  
* **Unchanged runtime facts already evidenced:** exact previously proved runtime facts being relied on.  
* **No-new-runtime-claim statement:** state that no new runtime command, route behavior, environment binding, or OPS action is being claimed beyond the evidenced basis.  
* **Governed evidence family to normalize:** exact governed artifact family or path set that must be rewritten or refreshed to one authoritative posture.  
* **Superseded contradictory artifacts or reports:** identify any prior contradictory bundle or report that will be treated as superseded evidence.  
* **Same-change evidence refresh requirement:** when indexed governed bytes change, refresh the Human Evidence Index, Machine Mirror, checksum sidecars, and required sibling path-proofs coherently in the same change.

### **Permitted step types (only)**

A Remediation Implementation Guide **MUST** use only two step types: **DEV** and **OPS**.  
No other step types are permitted (no QA, DOC, REVIEW, or “verification-only” steps).

### **Verification embedding requirement (normative)**

All verification **MUST** be embedded inside the owning DEV or OPS step.

Verification **MUST** produce concrete, repo-stored evidence outputs (paths/filenames specified in the step).

### **OPS posture linkage (normative)**

OPS steps **MUST** follow the OPS posture defined in **Ops Task Record (Template)**: PO-authorized and personally executed or explicitly delegated, IA-guided, not PR work, evidence-bound, secret-safe, and within governed lowercase paths.

### **Strict lane separation (normative)**

A step labeled DEV **MUST** contain only DEV actions.

A step labeled OPS **MUST** contain only OPS actions.

If a DEV action depends on an OPS output (or vice versa), the producing step **MUST** come first and the dependent step **MUST** declare its dependency explicitly using the cross-lane dependency line rule below.

### **Cross-lane dependency line rule (locked; required when applicable)**

If a step depends on outputs produced by a prior step in the other lane, the dependent step **MUST** include exactly one cross-lane dependency line in this exact form:

**Inputs needed from Step S\<N\> during implementation: \<exact items\>**

Rules for this line:

* `S<N>` **MUST** be the actual producing step ID (no placeholders such as `Sx`).  
    
* The line **MUST** appear exactly once in the dependent step. It **MUST NOT** be duplicated, nested, or prefixed by a placeholder field label.  
    
* If there is no cross-lane dependency, the line **MUST** be omitted (no placeholder line).  
  **/internal/version auth posture non-invention (when relevant)**

**Interim posture (normative; until the auth epic lands).**

* `/internal/version` is treated as **operator-network-only** until token auth exists.  
    
* Until token auth exists, guides MUST treat any auth header as **optional (never required)**. Any language that implies “auth required” must be treated as non-canonical unless/until implementation exists.

**Non-invention rule.**

A guide MAY state the canonical interim posture above. Any environment-specific access behavior beyond that posture MUST be labeled **Observed Evidence (non-PF)** and MUST NOT be generalized into canon.

**Evidence capture (auth posture; secret-free).**

* Always capture: status line \+ headers with **no auth header**.  
    
* If an auth header is available (value redacted / presence-only noted), MAY capture a second request with the auth header present. Absence of an auth header MUST NOT be treated as a blocker under the interim posture.

### **/internal/version conditional proof binding (when applicable)**

Use this block only when `/internal/version` is in scope. Complete every field from the current owning source; do not infer a value:

* **Applicability:** in scope | not in scope  
* **Resolved target and access posture:** cite the exact current owner and locator.  
* **Governing sources:** `PF02-Canon-HDE-Architecture` for architecture and non-A7 classification; `PF04-Canon-HDE-Governance` for Ops posture and token names; `PF05-Canon-HDE-CLI-API-Vendor-Ref` for transport and body contract; `PF12-Canon-HDE-Schemas-and-Artifacts` for the governed evidence family and paths.  
* **Governed evidence artifact family:** exact PF12 family and path.  
* **Acceptance tokens, if any:** exact PF04 names; do not define, alias, or infer them here.  
* **Transport and body contract source:** exact PF05 locator.  
* **Same-response-chain binding:** prove that captured headers, captured body, resolved target identity, and any token claim refer to one captured response chain.  
* **Failure consequence:** if the chain or required trustworthy proof cannot be established, use the applicable fail-closed tooling status and claim no affected token.  
* **Nonclaims:** state that the evidence is non-A7 and does not by itself prove release, deployment, reachability from another environment, or broader service success.

PF27 does not restate the identity-key set, header matrix, conditional behavior, or canonical token spelling in this block.

### **Canonical template skeleton (paste-ready)**

**Artifact Map**  
Inputs: `<paths or evidence identifiers>`  
Output: Remediation Implementation Guide (for approval) Approval sentinel: `ASK OK?`

**Executive Summary**  
\<EXECUTIVE\_SUMMARY\>

**Canon Frame (What “Correct” Means)**  
`<testable statement> — PFxx — Title, §X.Y`

**Observed Evidence Snapshot (Self-Contained; non-PF)**

**Evidence inventory reviewed (non-PF)**  
`<paths or quoted excerpts brought into this guide>`

**Primary failure signatures**  
`<short quotes / exact status lines / exact headers>`

**Root Cause Analysis (RCA)**

**What went wrong**  
**How it manifested**  
**Root causes**

* Documentation ignored  
    
* Documentation incorrect  
    
* Documentation missing

**Remediation Implementation Plan (Stepwise, DEV/OPS only)**

**Step Overview (required)**

| Step ID | Step name | Step type | Step intent | Owner/role | Depends on | Cross-lane dependency | Outputs |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

**Step Details (required; repeat per step)**

* Step ID:  
    
* Step name:  
    
* Step type (DEV or OPS):  
    
* Step intent (DISCOVERY or CHANGE):  
    
* Owner/role:  
    
* Preconditions:  
    
* Inputs:  
    
* Canon constraints (PF references):  
    
* Actions (complete but scoped; what-not-how):  
    
* Outputs (required):  
    
* Verification (required, embedded; not a separate step):  
    
* In-flight determinations (only if needed; must not be mechanical blockers):  
    
* ADR linkage (if applicable):

**PF Docs Consulted**

* PFxx — Title  
    
* \[LIST CONTINUES\]

**ADRs Requiring Approval (Canon and External Task Creation)**  
ADR-001 — \<short title\>

* Decision (required; canon-resolution outcome):  
    
* Why an ADR is required (required; must not already be canonized):  
    
* Canon issue being resolved (required; PF references):  
    
* Drain targets (required; owning PF docs \+ intended doc delta):  
    
* Notes / external task creation (optional):  
    
  ---

## **5\) Remediation Review Record (Template; REVIEW mode only)**

### **Scope**

Use this template for REVIEW-mode evaluation of an approved remediation lane, bounded implementation PR slice, cleanup PR, or follow-up remediation chain. It is review-only: it compares the approved lane or slice, the original attempt, any intermediate remedial attempts, and the current state, and it does not create new runbooks or new command sequences.

### **Required structure (paste-ready)**

**Artifact Map**

* Review lane or PR name:  
* Implementation or approval source:  
* Original attempt bundle:  
* Remediation bundle(s):  
* Extra evidence bundle:  
* Output:  
* Keywords traced:  
* Artifacts used:  
* PF canon used:

**Source Posture**

* Primary source of truth for what happened:  
* Plans or other secondary sources used for intended scope only:  
* PF20 used: YES | NO, and why:  
* PF23 used: YES | NO, and why:  
* Other PF canon used only where the primary source is silent:  
* Important limit, if any:  
* Search basis, if search-driven reconstruction was used:

**Provenance (Approved \-\> Attempt Chain \-\> Current State)**

* Approved source and scope statement:  
* Attempt-chain summary, repeated as needed:  
* Current remedial-attempt summary:  
* Net-effective outcome:

**Review Summary**

* What was attempted:  
    
* What was insufficient in the earlier attempt:  
    
* What changed in remediation:  
    
* Whether the current state satisfies the approved scope:  
    
* Remaining risk:

**Scope and Closure Claim Posture**

* **Approved task type:** closure-claiming | bounded intermediate | validation-only | sequencing-only | evidence-only | read-only discovery | other  
* **Does the approved task itself claim PF09 or canon closure now:** Yes | No  
* **Repository-change claim:** files changed | no files edited, created, or deleted | governed artifacts changed only | not applicable  
* **If the task claims no repo changes or no diff hunks, no-diff proof method and result:**  
* **If tests or CI are not acceptance evidence for this task, what evidence class is decisive instead:**  
* **If No, what still-open state must remain explicit:**  
* **Which later approved task or step owns remaining closure work, if any:**  
* **Public contract and boundary check:** state whether the current attempt adds any new public route, flag, serializer path, public contract field, acceptance-map path, token-matrix path, viability-log path, doc-delta-ledger path, close-pack path, QA-ledger work, Live QA runbook work, or PF-canon edits. If none are present, say so explicitly. If any are present, classify whether they are approved scope or scope drift.  
* **If current outputs remain blocked or incomplete-planned under current evidence, how that posture is recorded without overclaiming:**

**Governed Evidence Family Consistency (required when closure or later-drain posture relies on governed evidence)**

* **Closure dimension under review:**  
* **Closure mode:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Are the relied-on runtime facts unchanged from prior evidence:** Yes | No | Not applicable  
* **Is the governed evidence family internally consistent:** Yes | No  
* **If No, classification:** documentation/evidence failure  
* **If No, required review action:** stop the closure recommendation and do not consolidate contradictory source bytes until the family is normalized to one authoritative posture  
* **If a documentation/evidence normalization pass is being accepted instead of a rerun, what same-change refresh proves it:**  
* **Superseded contradictory artifacts or reports, if any:**

**Side-effect Classification Map (required when outside-family evidence refreshes or mirror rows are in scope)**

SE-001

* **Affected outside-family evidence family:**  
* **Classification:** expected updater convergence | required dependency refresh | unexpected drift  
* **Proof-companion paths or artifact paths affected:**  
* **Affected Machine Mirror artifact keys or discovered paths, if any:**  
* **Validation result:** paths exist | proof companions validate | mirror rows match artifact key, proof anchor, sha256, and size | not yet validated  
* **PASS posture:** fail-closed PASS supported | blocker | caveat only  
* **Evidence pointer:**

Repeat SE blocks as needed.

**Keyword Hit Map (optional when search-driven reconstruction was used)**

K-001

* Artifact:  
* Keyword(s) matched:  
* Why it matters:  
* Evidence pointer:

Repeat K blocks as needed.

**Chain of Events**

EVT-001

* Event:  
* Event type:  
* Timing basis:  
* Evidence pointer:

Repeat EVT blocks as needed.

**Diff Review (required when code or governed-artifact diffs are under review)**

DR-001

* Change summary:  
    
* Risk assessment:  
    
* Why it matters:  
    
* Evidence pointer:  
    
* Approved-plan linkage:  
    
* Supported status posture, if any:

Repeat DR blocks as needed.

**Root Cause Analysis (RCA)**

A) Bug or failure statement

* Failure sequence:  
* Where it occurred:  
* Evidence pointer(s):

B) Root cause(s)

* Root cause statement:  
* Evidence pointer(s):  
* PF references only when needed:

C) Fix across attempts

* What in the earlier attempt was insufficient:  
* What changed in remediation:  
* Why the change addresses the root cause:

D) Fix verification

* Proof the issue is resolved:  
* Residual risk or edge case evidenced:

**Deliverables and Results**

RES-001

* Deliverable produced:  
* Result now true that was not true before:  
* Residual risk:  
* Evidence pointer:

Repeat RES blocks as needed.

**Remediations Applied**

RMD-001

* Remediation:  
* Why it was needed:  
* What evidence shows it worked:  
* Evidence pointer:

Repeat RMD blocks as needed.

**Findings**

FND-001

* Source artifact or lane:  
* What I observed:  
* Why it matters:  
* PF reference(s), if canon is invoked:  
* Canon proof excerpt(s), if canon is invoked:  
* Evidence pointer(s):  
* Impacted checklist task ID(s), if proven:  
* Impacted checklist subtask ID(s), if proven:  
* Supported status posture:  
* Review provenance class, if this finding is used as a blocker or caveat: Introduced by current revision | Previously raised and still unresolved | Review Drift  
* Trigger for newly raisable unchanged-text issue, if applicable:

Repeat finding blocks as needed.

**Requirement Satisfaction Crosswalk (required when approval conditions or requirement labels exist)**

RC-001

* Requirement label:  
* Baseline attempt or step:  
* Baseline status:  
* Baseline evidence pointer(s):  
* Intermediate attempt status block(s), repeated as needed:  
  * Attempt label:  
  * Status:  
  * Evidence pointer(s):  
* Remedial change or current-state proof that addresses it:  
* Current status after the latest attempt or closure check:  
* Evidence pointer(s) in the latest attempt or closure check:  
* Notes:  
* Impacted checklist task ID(s), if proven:  
* Impacted checklist subtask ID(s), if proven:

Repeat RC blocks as needed.

**Checklist Impact & Status Posture (when a status move or later-drain posture is in scope)**

* Affected PF canon home(s) or status record:  
* Exact affected locator(s):  
* Current canon posture:  
* Current PF09 or other canon recorded status, if relevant:  
* Actual implemented state:  
* Actual OPS state, if applicable:  
* Actual governed evidence state:  
* Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended  
* Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon  
* Why this status posture is supported:  
* Evidence pointer(s):  
* PF proof excerpt(s) when a PF checklist or status record is relied on:  
* Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step  
* Linked Findings item(s):  
* Linked CHG item(s), if any:

**Evidence Print (PASS PROOF; required)**

A) Acceptance coverage evidence

* Requirement label:  
    
* Evidence pointer(s) proving satisfaction:  
    
* Key proof facts copied verbatim from the reviewed artifacts:

Repeat acceptance-coverage lines as needed.

B) Evidence and verification posture now satisfied

* What earlier evidence or verification gap existed:  
    
* What is now present:  
    
* Evidence pointer(s):

C) Legacy token evidence, only when explicitly in scope

* Include this subsection only when the reviewed work carries an active scoped legacy token claim.  
* Record the exact token name, original governing source, candidate identity, and evidence pointer supporting the scoped historical or optional cross-reference.  
* If evidence for an explicitly claimed legacy token is absent, record the claim as unsupported or `Unknown` without converting that gap into a broader implementation, QA, or closure failure.  
* When no active scoped legacy token claim exists, omit token-absence bookkeeping and evaluate acceptance through the governing requirements and exact-source evidence recorded in sections A and B.  
* If a prior attempt introduced an unsupported token or token-like label, record the source correction and any affected governed index, mirror, hash, or path-proof refresh required by the owning evidence contract.

D) Test or CI proof

* Job or test name:  
    
* Pass indicator copied verbatim:  
    
* Where it appears in the reviewed artifacts:

Repeat test or CI lines as needed.

E) Artifact and evidence outputs

* Path:  
    
* Type:  
    
* Key proof facts copied verbatim from the reviewed artifacts:

Repeat evidence lines as needed.

**Doc Deltas (PF-Canon only; required when the review supports a canon or checklist change)**

**PF Checklist Impact Summary**

* PF task ID:  
    
* PF subtask ID(s):  
    
* Current status if evidenced:  
    
* Status action:  
    
* Evidence pointer(s):  
    
* Linked Findings item(s):  
    
* Linked CHG item(s), if any:

**Doc Delta Detection Workflow**

CHG-001

* Change claim type: behavior or output | configuration or environment | governed paths or artifact families | tokens, rails, or evidence posture | rails/evidence posture | interface or contract | workflow steps | PF09 status-impact requirement | supported PF09 status posture changes | other  
* Claim:  
* Evidence pointer:  
* Canon basis: CANON ALIGNED | CANON MISMATCH | NO CANON MISMATCH | CANON SILENCE | CANON SILENT | ALREADY DRAINED  
* Canon Check Gate:  
* Canon proof excerpt(s) when canon is invoked:  
* Impacted PF task ID(s), if any:  
* Impacted PF subtask ID(s), if any:  
* Proposed status action, if any:  
* Linked finding(s):

Repeat CHG blocks as needed.

**PF Doc Delta Proposal**

RRPFD-001

* Target doc:  
    
* Target section:  
    
* Delta (actionable; 1–3 bullets):  
    
* Why:  
    
* Evidence pointer(s):  
    
* PF proof excerpt(s) when canon is invoked:  
    
* Why this is the correct home:

Repeat RRPFD blocks as needed.

**Canon Documentation Outcomes**

AD-001

* Addendum title:  
* Why:  
* Supportable status change versus current canon or drain state, if relevant:  
* Decision / rule / clarification:  
* Drain targets (doc delta intents):  
* Supersedes / conflicts, if applicable:  
* Implementation impact:  
* Evidence pointer:

Repeat addendum blocks as needed.

**Retrospective Notes**

* What went well:  
* What did not go well:  
* What we learned about the process:  
* What we learned about the system:

**Unknowns or Missing Evidence**

UNK-001

* Unknown or missing item:  
* Why it matters:  
* Evidence needed:  
* Where that proof should exist, if known:  
* Search basis, if search-driven reconstruction was used:

Repeat UNK blocks as needed.

**Decision**

* Decision:  
* Why this decision is supported:  
* Residual caution or follow-up boundary, if any:

## **6\) Audit Analysis Record (Template; REVIEW mode only)**

### **Scope**

Use this template when an audit report is being translated into explicit home classification, must-act-now posture, and doc-delta proposals. It is review-only: it inventories the audit inputs, summarizes the drift themes, maps each finding to the correct PF home, and records whether any runnable checklist delta is supported.

**PF23 audit-classification posture**

* PF23 audit observations must be classified to owning canon homes before being treated as PF09.x task deltas, remediation scope, implementation work, OPS work, evidence homes, or acceptance tokens.  
* PF23 audit observations may support PF09.x task deltas only when the finding proves runnable development or operations work in the relevant phased PF09.x scope.  
* If the correct action is classification, routing, documentation alignment, or PO adjudication only, record that posture explicitly and do not convert the observation into implementation or OPS scope by assumption.

### **Required structure (paste-ready)**

**Artifact Map**

* Audit Report:  
    
* Epic Plan:  
    
* Existing Issues List:  
    
* PF Canon consulted:  
    
* Output:

**Audit Summary**

* What the audit compares:  
* Top drift themes:  
* Number of discrete findings extracted:  
* Number of must-act-now findings:  
* Concrete canon delta(s) supported:  
* Any no-task-delta conclusion, if supported:  
* PF doc homes consulted for classification:  
* PF doc homes receiving proposals:

**Findings → Doc Delta Map**

FND-001

* Finding (one sentence):  
* Audit anchor (verbatim line):  
* Audit evidence pointer:  
* Epic Plan linkage (one sentence):  
* Epic Plan anchor (verbatim line or N/A):  
* Must-act-now: YES | NO  
* Observation-only: YES | NO  
* Re-open trigger, if observation-only:  
* Disposition: Doc delta proposed | Observation only | Existing issue duplicate | No doc delta needed | No action | PO decision needed  
* Correct home(s):  
  * HDE Build Checklist work-item mapping:  
    * **Work item ID:**  
    * **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
    * **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
    * **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
    * **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
    * **Exact source heading:**  
    * **Contribution:** advances | satisfies | leaves open | documents  
    * **Status nonclaim:** this artifact does not itself move PF09 status  
  * PF14 mechanics delta: YES | NO  
  * PF02 architecture delta: YES | NO  
  * Other PF doc delta(s):  
  * PF20 historical correction: YES | NO  
* Existing issue duplicate:  
* Why these are the correct homes:  
* Review provenance class, if this finding is used as a blocker or closeout caveat: Introduced by current revision | Previously raised and still unresolved | Review Drift  
* Trigger for newly raisable unchanged-text issue, if applicable:

Repeat FND blocks as needed.

**Doc Delta Proposals — PF09.x (Tasks)**

* None. when no PF09.x task delta is supported.

PF09P-001

* **Work item ID:**  
* **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
* **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
* **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
* **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
* **Exact source heading:**  
* **Contribution:** advances | satisfies | leaves open | documents  
* **Status nonclaim:** this proposal does not itself move PF09 status  
* **Delta (actionable; 1–3 bullets):**  
* **Why:**  
* **Evidence pointer(s):**  
* **PF proof excerpt(s) when canon is invoked:**

Cross-phase proposals MUST use separate records for each independently mapped scope unit.

Repeat PF09P proposal blocks as needed.

**Doc Delta Proposals — Other PF homes**

OPFP-001

* Target doc:  
    
* Target section:  
    
* Delta (actionable; 1–3 bullets):  
    
* Why:  
    
* Evidence pointer(s):  
    
* PF proof excerpt(s) when canon is invoked:  
    
* Why this is the correct home:

Repeat OPFP proposal blocks as needed.

**Open Questions for PO**

OQ-001

* Question:  
* Why it matters:  
* Evidence pointer(s):  
* Decision needed:

Repeat open-question blocks as needed.

**Final line**

END OF AUDIT ANALYSIS

## **7\) Implementation Closeout Report (Template; REVIEW mode only)**

### **Scope**

Use this template when a completed implementation slice, remediation bundle, or epic closeout needs a review-grade report of what stayed fixed, what was reused, what was newly delivered, what evidence exists, and what canon or checklist follow-up remains. It is review-only: it records implementation outcomes and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.

### **Required structure (paste-ready)**

**Executive Summary**

* Scope classification:  
    
* Preserved scope boundaries:  
    
* Approved reuse baseline, if any:  
    
* New implementation allocation or slice map:  
    
* Biggest wins:  
    
* Biggest remaining risks or gaps:

**Implementation Breakdown (slice-by-slice)**

CHG-001

* Slice name:  
    
* Purpose:  
    
* Key changes, high level:  
    
* Key surfaces touched:  
    
* Tests or evidence produced:  
    
* Outcome:  
    
* Evidence pointer(s):  
    
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
    
* Source-limit or gap note, if any:  
    
* If a claim depends on a non-PF or in-session artifact, exact source that carries the claim:

Repeat CHG blocks as needed.

**Major Surfaces Affected**

* Surface family:  
* Specific surfaces:  
* Why it matters:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat surface blocks as needed.

**Evidence Inventory**

* Evidence family:  
* Path(s):  
* What it proves:  
* Related token names, if explicitly claimed:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat evidence-family blocks as needed.

**Source Posture**

* Primary source of truth for what happened:  
* Secondary sources used for intended scope only:  
* PF20 used: YES | NO, and why:  
* PF23 used: YES | NO, and why:  
* Other PF canon used only where the primary source is silent:  
* Non-PF in-session artifacts used, if any:  
* Important limit, if any:

**Retrospective — Process**

* What went well:  
* What did not go well:  
* What we learned:  
* Evidence pointer(s):

**Retrospective — Application / System**

* What we learned about the system:  
* System boundaries preserved or clarified:  
* Known application-level lessons:  
* Evidence pointer(s):

**Risk and Debt Register**

RISK-001

* Priority: Must-fix | Should-fix | Nice-to-have  
* Risk or debt statement:  
* Evidence status:  
* Evidence pointer(s):  
* Why it matters:  
* What would prove resolution:  
* Closeout impact:

Repeat risk/debt blocks as needed.

**Canon Alignment and Documentation Outcomes**

* Canon references used:

CR-001

* PF document title:  
* How it was used:  
* Evidence pointer(s):  
* Source-limit or gap note, if any:

Repeat canon-reference blocks as needed.

* Existing live PF10 delta or canon mismatch on record:  
* Supportable status change(s) from repo evidence, if any:  
* Current canon or drain state for those rows, if different:  
* Token or evidence semantics note, if applicable:  
* Evidence-family completeness or same-change-family note, if applicable:  
* Likely drain targets by title only:  
* Additional PF10 addendum needed: YES | NO  
* Why:

**Proposed PF10 Addenda (when the retrospective supports living-addendum text)**

* None: state when no new PF10 addenda are proposed, why no new addendum is needed, and which existing addenda, docs PR, or evidence record already carries the needed posture.

AD-001

* Addendum title:  
* Why:  
* Decision / rule / clarification:  
* Drain targets (doc delta intents):  
* Supersedes / conflicts, if applicable:  
* Implementation impact:  
* Evidence pointer(s):

Repeat addendum blocks as needed.

**Closure Decision Set (when close posture depends on explicit decisions)**

DEC-001

* Decision:  
    
* Rationale:  
    
* Supported status updates, if any:  
    
* Closure timing recommendation, if any:  
    
* No-new-runnable-task-delta conclusion, if any:  
    
* Observation-only themes and re-open triggers, if any:  
    
* Net resolution effect:

Repeat DEC blocks as needed.

**Closure Evidence Snapshot**

A) Evidence produced

* Path:  
* What it proves:  
* Evidence pointer(s):  
* Related token names, if explicitly claimed:  
* Source-limit or gap note, if any:

Repeat produced-evidence lines as needed.

B) Evidence missing or ambiguous

* Item:  
* Evidence status: Unknown | Missing | Ambiguous | Supportable but not drained | Not applicable  
* Why it matters:  
* What would prove it:  
* Where that proof should exist, if known:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat missing-or-ambiguous lines as needed.

C) Open closure items or questions for the Lead

* Question:  
* Why it matters:  
* Relevant canon or evidence:  
* Evidence pointer(s):  
* Decision needed from Lead or PO:

Repeat question lines as needed.

## **8\) QA Pass Review Record (Template; REVIEW mode only)**

### **Scope**

Use this template when a completed Live QA check or approved Live QA check cluster is being reviewed against its approved Check Block or Check Blocks and its Deliverables Report. It is review-only: it determines whether each named step is trustworthy, whether the plan-defined deliverables and PASS criteria were satisfied for every reviewed step, whether each step stayed aligned to the approved token posture when token-attached, and whether any follow-up or doc delta is required. When a check cluster is reviewed, the review MUST account for every check ID named in the check label or `QA_STEP_NAME`, including each step’s deliverables, PASS criteria, token posture, final FAIL or BLOCKED posture, deviations, evidence-trust facts, and any no-broader-closure claim. It does not create new runbooks, new commands, or new acceptance tokens.

### **Required structure (paste-ready)**

**Review Summary**

* Check label:  
* Decision line:  
* Deliverables Report anchor:  
* Evidence-trust statement:  
* Evidence pointer(s):  
* Approved-plan PASS criteria statement:  
* Evidence pointer(s):  
* Decision lane, branch policy, or scope-discipline statement, if applicable:  
* Evidence pointer(s):  
* Approved token-posture statement, if token-attached:  
* Evidence pointer(s):  
* Doc Deltas:  
* State `None` when no PF-Canon inconsistencies or new doc requirements were found.

**Findings**

FND-001

* What you observed:  
* Classification:  
* PF touchpoints when needed:  
* Evidence pointer(s):  
* Why it matters:  
* Drives decision: Yes | No  
* Negative-claim proof, if this finding depends on the absence of direct lines in DELIVERABLES\_REPORT\_FILE:

Repeat finding blocks as needed.

Finding posture rules:

* Non-blocking planning failures, process imperfections, or earlier failed attempts MAY be recorded as findings, but they MUST be distinguished from verdict-driving facts and MUST use `Drives decision: No` when they do not affect the decision.  
* If the review relies on step-evidence trust, the findings MUST make explicit which trust facts were confirmed, such as the governed `primary.log` header, captured rails and determinism pins, and the current-state QA root and manifest-pair posture when applicable.  
* If a finding depends on the absence of a direct token-level proof line or other direct proof line in DELIVERABLES\_REPORT\_FILE, the review MUST record the exact negative-claim search and the no-match result rather than implying absence.  
* Non-fatal runtime warnings MAY be recorded as findings with `Drives decision: No` when the deliverables report also records no `TOOLING_BLOCKED`, `FAIL_TOOLING`, or `FAIL_BEHAVIOR` condition and the approved PASS predicates are otherwise satisfied. The review MUST still record the warning evidence pointer and any follow-up needed, but the warning alone is not a blocker or fail classification.

**Evidence Print**

A) Required deliverables checklist

* Deliverable name/label, quoted from plan/caveats:  
* Evidence pointer to the plan/caveats:  
* Expected path:  
* Present in DELIVERABLES\_REPORT\_FILE: Yes | No  
* Evidence pointer in DELIVERABLES\_REPORT\_FILE:

Repeat deliverable lines as needed.

B) Evidence artifacts relied on

* Path/label, exact as listed in DELIVERABLES\_REPORT\_FILE:  
* Evidence pointer:  
* Key proof facts, 1–3 short exact strings, status lines, or hashes:

Repeat artifact lines as needed.

C) Tokens/gates (required only when the reviewed step is token-attached)

* Token/gate name, quoted from plan/caveats, with Evidence pointer:  
* Evidence pointer(s) in DELIVERABLES\_REPORT\_FILE proving it, or state `Unknown.` when DELIVERABLES\_REPORT\_FILE does not surface a direct token-level proof line:  
* Negative-claim proof, if `Unknown.` is used:

Repeat token lines as needed.

Acceptance-claim boundary rule:

* If a Live QA check records no acceptance-token claim and limits claims to the evidence scope, absence of an acceptance map, token matrix, or close-pack artifact is close-stage posture, not a runtime behavior failure for that check.  
* The review MUST record whether the missing close-stage artifact affects the reviewed check verdict, the later closeout posture, or neither.  
* The review MUST NOT convert a missing close-stage artifact into a token claim, PASS proof, or runtime blocker unless the approved check made that artifact a required deliverable for the check itself.

**QA Verdict and Optional Follow-ups**

* Verdict line:  
* Evidence-grounded decision bullets:  
  * primary evidence trust:  
  * deliverables posture:  
  * PASS criteria posture:  
  * token posture, if applicable:  
* Optional follow-up or planning-failure note, if any:

Execution-deviation acceptance rule:

* A QA Pass Review MAY accept final PASS after an operational dependency installation, QA-only helper reconstruction, or proof-posture append only when the deviation is recorded in the Deliverables Report or governed step evidence, the same proof target remains in scope, required deliverables remain unchanged, PASS/FAIL criteria remain unchanged, token posture remains unchanged, and final PASS evidence is captured under the approved QA evidence root.  
* For dependency-install deviations, the review MUST record the missing or unready dependency, the installation or activation action taken, the initial transient state when evidenced, the final rerun PASS evidence, and whether the issue remains a planning dependency-readiness gap with `Drives decision: No`.  
* For QA-only helper reconstruction, the review MUST record why the original helper or transcript could not be run, what wrapper or helper was actually used, whether the wrapper stayed execution-only, whether the same approved per-step validation commands or proof actions were preserved, and whether the same approved QA-root receipt families were produced.  
* For proof-posture append deviations, the review MUST record the exact proof-posture lines added, the approved proof target that required those lines, the affected primary log, the refreshed sibling path proof when applicable, and whether the append avoided any new token, PF09.x drainage claim, product-code change, repo-test change, public-contract change, PF document edit, or governed-artifact change outside the QA root.  
* If any of those conditions are not proven, the deviation MUST NOT be hidden under PASS; classify it as blocker, caveat, tooling failure, or remediation work according to the approved PASS/FAIL map and source authority.

**ADRs — Deviations (optional)**

**ADR-DEV-01**

* **What changed:**  
* **Why it changed:**  
* **Plan or caveat reference, with Evidence pointer:**  
* **What was actually run, with Evidence pointer:**  
* **Evidence impact: files added/changed/missing, using verbatim paths**  
* **Decision:**  
* **Canon impact:**  
* **PF proof excerpt, if canon is invoked:**

**Repeat ADR-DEV blocks as needed.**

* **PF proof excerpt, if canon is invoked:**

**State `No deviations observed for this step.` when no deviation block is needed.**

## **9\) Final QA Closeout Review \+ QA RCA (Template; REVIEW mode only)**

### **Scope**

**Use this template when the completed Live QA stream for an epic must be synthesized into a closeout recommendation, canonical RCA basis, coverage-vs-plan accounting, and PF-only doc-delta proposals. It is review-only: it summarizes executed QA and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.**

### **Required structure (paste-ready)**

**Artifact Map**

* **Epic:**  
* **PF10:**  
* **Implementation Guide:**  
* **QA Plan:**  
* **Output:**

**QA Closeout Summary**

* **Epic reviewed:**  
* **PF10-stated QA execution outcome:**  
* **What was reviewed:**  
* **Overall readiness:**  
* **Root cause category:**  
* **Implementation Guide framing, if used:**  
* **Evidence pointer(s):**

**Canonical RCA Requirement Basis**

**A) PF19 references relied on**

**PF19R-001**

* **PF19 reference:**  
* **Proof excerpt:**  
* **Evidence pointer:**

**Repeat PF19R reference blocks as needed.**

**B) PF27 and PF06 references relied on**

**PF2706R-001**

* **PF reference:**  
* **Proof excerpt:**  
* **Evidence pointer:**

**Repeat PF2706R reference blocks as needed.**

**Checklist of required RCA/closeout elements**

* **D0 / Step-0 discovery and baseline rails posture:** state whether D0 discovery, Step-0 discovery, Step-0 doc-delta capture when required, closed/open rails posture, deterministic pins, and captured environment posture are covered, missing, or not applicable.  
* **Functional runtime proof on changed runtime surfaces:**  
* **Governed current-state QA evidence under the epic QA root:**  
* **Per-step-cluster manifest/header/path-proof trust proof:** when a final QA closeout asks a reviewer to approve an executed QA step cluster, the artifact MUST surface the manifest entry, canonical primary-log path, primary-log header fields, `captured_env`, `evidence_artifacts`, `intended_tokens`, `claimed_tokens`, path-proof binding, token posture, rails/determinism posture, and final status for that cluster. A PASS result JSON or summary label alone is not sufficient closeout proof when manifest, header, or path-proof trust is required.  
* **Evidence-package content validation:** when a final QA closeout review relies on an uploaded deliverables package, archive, extracted report bundle, or external package summary, the review MUST verify that selected required logs and artifacts are present, readable, and non-empty when non-empty content is required for the proof.  
* **Zero-byte package caveat:** a zero-byte, empty, unreadable, missing, or stale selected log or artifact in an uploaded package is not standalone proof. It is a caveat rather than a blocker only when PF10 or the review artifact records the caveat and current tracked repo evidence supplies the same plan-defined proof.  
* **Repo-evidence substitution conditions:** tracked repo evidence may resolve an uploaded-package caveat only when the repo evidence is governed, readable, non-empty where non-empty proof is required, tied to the same QA event or check, and sufficient to evaluate the same PASS/FAIL predicate. The review must identify the controlling repo evidence and must not treat the uploaded package as the proof source for that item.  
* **Failure posture:** if the controlling repo evidence is absent, unreadable, not governed, not tied to the same QA event, or insufficient for the same PASS/FAIL predicate, classify the condition as an evidence gap or blocker as appropriate. Do not classify the package defect as product or runtime failure unless separate evidence proves a product or runtime defect.  
* **QA RCA & Doc Delta summary:**  
* **Coverage vs QA Plan accounting:**  
* **All-slice coherence proof:** when the QA closeout claims post-implementation coherence after multiple slices, verify all prior step primary logs required for that claim are present, all required implementation-slice artifacts are present, and the derived status agrees with the recorded primary-log header status and exit code.  
* **Readiness / closeout recommendation:**  
* **Execution-venue proof:** state whether venue is material to the claimed proof. When venue is material, verify the four-field venue declaration, the required governed venue binding, and the resulting PASS, FAIL, or blocker effect. When venue is not material, record `NOT CLAIMED`, `NOT APPLICABLE`, or `UNKNOWN - NON-MATERIAL`, as appropriate; do not infer the historical venue or treat missing Codespaces provenance as a QA failure, uncovered QA step, missing closeout element, or closeout blocker.  
* **Indexed evidence under Human Evidence Index and Machine Mirror:**  
* **Compliance statement:**

**Source-of-Truth Posture**

* **Primary SoT for epic-specific QA events:**  
* **Implementation Guide used:**  
* **QA Plan used:**  
* **Implementation Guide authority posture:** goals framing only | scope framing only | close authority | not used | other evidence-backed posture  
* **QA Plan authority posture:** intended QA requirement framing only | close authority | not used | other evidence-backed posture  
* **Mismatches identified between the primary SoT and the QA Plan, if any:**  
* **Negative-claim proof, if a mismatch search is used:**  
* **If a PF10 addendum is the decisive close-authority statement: say whether it provides direct evidence-pointer lines or evidence-basis prose only.**  
* **If only evidence-basis prose is available: record that as an auditability caveat and identify the governed evidence clusters used to support the closeout conclusion.**

**QA Timeline**

Chronology rule: reconstruct chronological order from explicit timestamps when present. When no timestamp is visible, use primary-source order and state that basis in the event record.

**EV-001**

* **Source order or chronology basis:**  
* **Event type:** QA Step | Remediation Loop | ADR | Decision | Closeout Event | Other  
* **Event name/label:**  
* **Outcome label:**  
* **Evidence pointer(s):**

**Repeat event blocks as needed.**

**Coverage vs QA Plan**

**CV-001**

* **Step name as written in QA Plan:**  
* **Coverage status:** fully evidenced | partially evidenced | blocked | not run | not applicable  
* **Evidence pointer(s):**  
* **Mismatches/deviations vs QA Plan, if any:**  
* **Accepted execution deviation(s), if any (examples: bounded Moon Loop rerun, rails change, QA syntax correction, step-local dependency-preflight correction):**  
* **Original planned receipt(s), if any:**  
* **Accepted remediation or rerun receipt(s), if any:**  
* **Final accepted proof basis:** original planned receipt | accepted remediation receipt | accepted rerun receipt | combined approved evidence | not applicable  
* **Why the deviation remained acceptable, with Evidence pointer(s):**  
* **Closeout impact:** blocker | non-blocker | caveat | follow-up only

**Repeat coverage blocks as needed.**

**Outcome Meaning**

* **What the final QA outcome means:**  
* **What the final QA outcome does not claim:**  
* **Truth-class separation:** state whether implementation readiness, QA readiness, final QA outcome, documentation drainage, PF09.x drainage, formal close-pack completion, vendor-version runtime conformance, and live vendor behavior are claimed, not claimed, or deferred. Local Live QA proof MUST NOT be overread as any truth class it does not directly prove.  
* **Live QA role boundary:** state whether Live QA performed proof-only work, an approved in-session remediation, implementation work, PF-canon editing, or closeout action. If implementation, remediation, PF-canon editing, or closeout action is not explicitly authorized and evidenced, record it as not claimed.  
* **Readiness caveats, if any:**  
* **Evidence pointer(s):**

**Findings**

**FND-001**

* **What happened, grounded in the reviewed evidence:**  
* **Why it matters:**  
* **Classification:** SoT internal mismatch | Evidence posture gap | Process-rail gap | Tooling-infra gap | Implementation gap | Plan-guidance ambiguity | other evidence-backed class  
* **Anomaly label, if applicable:** FAIL\_BEHAVIOR | FAIL\_TOOLING | TOOLING\_BLOCKED | none  
* **PF touchpoints when needed:**  
* **Evidence pointer(s), or state `none provided.`:**  
* **Negative-claim proof, if `none provided.` is used:**

**Repeat finding blocks as needed.**

**Root Cause Analysis**

**Failure or Friction Patterns Evidenced**

**FP-001**

* **Pattern:**  
* **Classification:** product behavior | QA harness | evidence posture | planning drift | documentation or drainage posture | current-reality context | other evidence-backed class  
* **Evidence pointer(s):**

**Repeat failure or friction pattern blocks as needed.**

**A) Primary root cause**

* **Statement:**  
* **Evidence pointer(s):**

**B) Contributing factors**

**CF-001**

* **Factor:**  
* **Evidence pointer(s):**

**Repeat contributing-factor blocks as needed.**

**C) What made it hard to detect earlier, if applicable**

* **Statement:**  
* **Evidence pointer(s):**

**D) What made it hard to close confidently, if applicable**

* **Statement:**  
* **Evidence pointer(s):**

**Remediation Loop Assessment**

**RL-001**

* **Loop label:**  
* **Outcome:**  
* **Evidence pointer(s):**  
* **Residual uncertainty, if any:**

**Repeat remediation-loop blocks as needed.**

**Evidence Hygiene and Recurrence Prevention**

* **Strong evidence posture observed:**  
* **Recurring proof-risk pattern, if any:**  
* **What would prevent recurrence:**  
* **Template or PF-canon guard to preserve:**  
* **Evidence pointer(s):**

**Implementation Gaps and Proposed Fixes**

**IMP-001**

* **Symptom, quoting reviewed evidence where useful:**  
* **Expected behavior from reviewed evidence and/or PF canon:**  
* **Evidence pointer(s):**  
* **Likely locus only if the reviewed evidence names a component or surface:**  
* **Proposed fix, high-level only:**  
* **Verification hook:**

**Doc Deltas (PF-Canon only; excluding PF10)**

**A) PF19 doc deltas (targeted)**

* **None:** state when no PF19 doc delta is required, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**PF19D-001**

* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why:**  
* **Evidence pointer(s):**

**Repeat PF19D delta blocks as needed.**

**B) Optional other PF doc deltas (maximum 5; only if PF19 is not the correct home)**

* **None:** state when no optional other PF doc deltas are needed, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**OPFD-001**

* **Doc:**  
* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why PF19 is not the correct home:**  
* **Evidence pointer(s):**

**Repeat OPFD delta blocks as needed.**

**QA Verdict and Recommendation**

* **Verdict:** PASS | READY WITH CAVEATS | NOT READY | BLOCKED  
* **Why this verdict is supported:**  
* **Caveats:** state what the verdict does not claim, including any undrained PF status, formal close-pack posture, or bounded execution deviation.  
* **Non-blocker rationale:** state why any accepted deviation remains non-blocking, with evidence pointer(s).  
* **Follow-up recommendation:** state any future doc delta, drain target, final close-pack acceptance concern, or review guard that should be preserved.

## **10\) Epic Closure Review \+ Retrospective (Template; REVIEW mode only)**

### **Scope**

Use this template when one review artifact must combine epic closure decision, closure-trace accounting, implementation retrospective, PF-only doc-delta routing, and recommendation posture. It is review-only: it records what was completed, what evidence supports closure, what follow-up remains, and what should drain later, and it does not create new runbooks, new commands, or new acceptance tokens.

The closure-review artifact makes the evidence decision assigned to it. It MUST NOT require a pre-existing close report, close manifest, or equivalent decision-restatement artifact whose only function is to restate that decision. Absence of such an artifact is not itself a blocker and MUST NOT create remediation. A pre-existing artifact MAY be required only when an owning source independently requires it for a distinct proof function; the review MUST name that source and proof function.

### **Required structure (paste-ready)**

**Inputs Posture**

* **Implementation Guide provided:**  
* **QA Plan provided:**  
* **Input-name, epic-name, or phase-label mismatch, if any:** state any mismatch between prompt labels and primary-source epic identity, which source controls the review identity, whether the prompt label is preserved only as artifact-map or provenance text, and evidence pointer(s)  
* **Sources intentionally excluded from closure authority, if any:**  
* **Why excluded sources do not drive closure:**  
* **Primary epic-specific source of truth:**  
* **Current-reality source, if used:**  
* **PF-Canon homes used where the primary source is silent:**  
* **Implementation Guide used for intended scope framing only:**  
* **QA Plan used for intended QA requirement framing only:**  
* **Evidence pointer(s):**

**Closure Registers**

**A) Deliverables Register**

**CR-DEL-001**

* **Deliverable label:**  
* **Source:**  
* **Anchor quote:**  
* **Explicitly stated required evidence, path, or token strings, verbatim if present:**  
* **Evidence pointer:**

**Repeat deliverable blocks as needed.**

**B) QA Verification Register**

**CR-QA-001**

* **Step or verification label:**  
* **Source:**  
* **Anchor quote:**  
* **Required evidence outputs or pass-fail posture, verbatim if present:**  
* **Evidence pointer:**

**Repeat verification blocks as needed.**

**C) Primary Results Register**

**CR-RES-001**

* **Result claim summary:**  
* **Anchor quote:**  
* **Evidence pointers or paths, verbatim, or state `none provided.`:**  
* **Outcome label, if recorded:**  
* **Evidence pointer:**

**Repeat result blocks as needed.**

**D) Current-Reality Register**

**CR-REAL-001**

* **Surface summary:**  
* **Anchor quote:**  
* **Paths or components, verbatim if present:**  
* **Closeout impact:**  
* **Closure authority note: state whether the current-reality source proves closure, blocks closure, or only contextualizes closure.**  
* **Evidence pointer:**

**Repeat current-reality blocks as needed.**

**Closure Trace Ledger**

**CTL-001**

* **Deliverable:**  
* **Mapped QA verification item(s):**  
* **Mapped primary-source result claim(s):**  
* **Primary-source evidence pointer status:** present | partially present | missing | not applicable  
* **Current-reality check:**  
* **Status:**  
* **Why:**  
* **Evidence pointer(s):**

**Repeat closure-trace blocks as needed.**

**Path and Surface Reality Ledger**

**PSR-001**

* **Path or surface string, verbatim:**  
* **Source(s):**  
* **Status:**  
* **Closure mode, if the surface or environment is treated as closed:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Is the governed evidence family for this surface internally consistent:** Yes | No  
* **If closed without a new runtime exercise, what unchanged runtime facts or approved equivalence basis support that posture:**  
* **Required for closure:**  
* **Notes:**

**Repeat path and surface blocks as needed.**

**Closure Decision**

* **Epic closure decision:**  
* **Decision scope and PO-action boundary:** state whether the decision is a review-trace conclusion, PO closeout action, later-drain recommendation, or another bounded posture.  
* **Completion-axis separation:** state repo-supported completion, canon-drain completion, formal close-pack completion, merge provenance, board state, PO closeout action, and formal ops action as claimed, not claimed, deferred, or not applicable.  
* **Why this decision is supported:**  
* **Current PF09 or other canon recorded status, if relevant:**  
* **Actual implemented state:**  
* **Actual OPS state, if applicable:**  
* **Actual governed evidence state:**  
* **Auditability caveat, if any:** say whether the decisive primary-source close-authority statement provides direct evidence-pointer lines or evidence-basis prose only. If only evidence-basis prose is available, record that explicitly and identify the governed evidence clusters used to support the closure conclusion.  
* **Documentation-drain posture:** state whether any PF10 or PF-canon drain remains, name the intended drain targets by title, and say explicitly whether the later drain is only follow-up work or already drained; if the current verdict relies on undrained live truth, use supportable-versus-drained wording explicitly.  
* **Follow-up-only items that do not block closure, if any:** include remaining drain targets and doc-delta candidates here when required QA, implementation state, OPS state, and governed evidence already support closure. Documentation drainage itself is follow-up work, not a closure blocker.  
* **Minimal follow-ups required only if not satisfied:** list only real truth-and-proof blockers that prevent closure, such as incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR / FAIL\_TOOLING / TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.

**Later-Drain PF-Canon Update (required when this review supports later PF-canon drainage)**

* **Affected PF canon home(s):**  
* **Exact affected locator(s):**  
* **Current canon posture:**  
* **Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended**  
* **Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon**  
* **Evidence basis:**  
* **Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step**

**Retrospective — Executive Summary**

* **Scope and contract-preservation summary:**  
* **Delivered implementation summary:**  
* **Biggest wins:**  
* **Biggest remaining risks or gaps:**

**Implementation Report**

**IR-001**

* **PR or slice label:**  
* **Purpose:**  
* **Key changes:**  
* **Key surfaces touched:**  
* **Tests or evidence produced:**  
* **QA steps and closeout evidence:** state Step-0, QA step groups, accepted remediation loops, final PASS or blocked posture, and closeout deliverables such as manifest, discovery artifact, QA RCA / Doc Delta summary, and path proofs when reviewed.  
* **Outcome:**  
* **Evidence pointer:**

**Repeat implementation-report blocks as needed.**

**Implementation Report — Cross-slice summary (required when the review covers more than one PR, OPS task, or QA step)**

* **Major surfaces affected:**  
* **Evidence inventory:**  
* **Docs-only or repo-docs sweep evidence, if used:** state touched docs, repo-proof method, validation checks, scope-limiting proof, and whether the docs sweep is PF10-recorded, close-pack-summarized, or non-PF provenance only.  
* **Evidence gaps or caveats:**  
* **Evidence pointer(s):**

**Closure Evidence Snapshot**

* **Evidence produced:** list only governed artifacts, PR evidence, docs sweep evidence, indexes, mirrors, path proofs, and validation outputs actually verified by the review.  
* **Evidence missing or ambiguous:** list every closure-relevant artifact or proof family that was not verified, why it matters, what would prove it, and where that proof should exist if known.  
* **Open closure items or questions for the Lead:** list decisions still required before PO closeout, including close-pack baseline existence, Live QA close-gate evidence, PF09.x drain state, parent-row status action, docs-sweep historical capture, or deferred work visibility when applicable.

**Retrospective — Process**

* **What went well:**  
* **What did not go well:**  
* **What we learned:**

**Retrospective — Application / System**

* **What we learned about the system:**  
* **Known remaining risks or debt:**

**ADRs and Ambiguity Resolution**

**ADR Overview (required when multiple ADRs or cleaned dispositions are reviewed)**

ADR-SUM-001

* ADR:  
* Related finding:  
* Cleaned disposition: New staging decision required | Existing PF10 coverage | Permanent PF-Canon already governs | New rule required | No ADR needed | Other  
* Current action:  
* Whether this becomes a template or canon rule: Yes | No  
* Evidence pointer:

Repeat ADR summary rows as needed.

**ADR-001**

* **Decision point:**  
* **Options considered:**  
* **PF-canon constraints relied on:**  
* **Proof excerpt(s) when canon is invoked:**  
* **ADR tag, if recorded:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **ADR proposal text, if recorded:**  
* **Final decision for this epic:**  
* **Should this become canonical for future work:** Yes | No  
* **Evidence pointer:**

**Repeat ADR blocks as needed.**

**Canon Alignment and Documentation Outcomes**

* **Canon references used:** list current PF homes or source artifacts actually used, and the scope of use for each.  
* **Non-PF documentation or docs-sweep sources used only as provenance:** state whether they affect closure authority or only report history.  
* **New PF10 addenda proposed:** Yes | No  
* **If no new addenda are proposed:** state which existing addenda already stage the material canon or status actions, if any.  
* **Evidence pointer(s):**

**PF-Canon Doc Deltas**

* **None:** state when no PF-Canon doc delta is required, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**ECPFD-001**

* **Doc:**  
* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why this doc is the correct home:**  
* **Evidence pointer:**

**Repeat ECPFD blocks as needed.**

**Build Improvements and Future Work**

**FW-001**

* **Short description:**  
* **Where it should live:**  
* **Work item ID:**  
* **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
* **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
* **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
* **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
* **Exact source heading:**  
* **Contribution:** advances | satisfies | leaves open | documents  
* **Status nonclaim:** this future-work record does not itself move PF09 status  
* **Disposition and reason not included now:**  
* **HDE Build Checklist gap exists:** Yes | No  
* **PF docs to reference or update if pursued later:**  
* **PF23 dependency: Yes | No**  
* **If Yes, state the gap, anchor, or why the dependency matters:**

**Repeat future-work blocks as needed.**

**Recommendation only**

* **Implementation posture recommendation:**  
* **Strongest implementation evidence:**  
* **Strongest QA evidence:**  
* **Why the recommendation is supported:**  
* **Most important policy improvement to preserve:**  
* **Most important process improvement to preserve:**  
* **Caveats or follow-ups that remain outside the recommendation:**  
* **ADRs that should be memorialized in PF-Canon:**  
* **No-hard-blocker statement:**  
* **Distinct remaining actions: PO closeout | PF09.x drainage | canon maintenance | other**

## **11\) Ops Task Final Review Record (Template; REVIEW mode only)**

### **Scope**

**Use this template when a completed Ops task, ops remediation rerun, or other bounded PO-executed ops slice must be reviewed against an approved Ops Task Record, approved plan, or approved remediation scope. It is review-only: it determines whether the run stayed within approved scope, whether the required governed outputs and environment or binding dispositions were captured truthfully, whether the result is acceptable for downstream binding or follow-on work, and what later PF-canon drain posture is supported when the review is intended to feed canon drainage. It does not create new runbooks, new commands, or new acceptance tokens.**

### **Required structure (paste-ready)**

**Review Summary**

* **Ops task or run label:**  
* **Approved task or plan source:**  
* **What actions were performed:**  
* **Environment or binding disposition, if applicable:**  
* **Whether the run stayed within approved scope:**  
* **Whether deliverables and evidence are sufficient:**  
* **Remaining operational risk, if any:**  
* **Downstream binding or follow-on use, if any:**

**Task Boundary and Closure Claim Posture**

* **Run posture:** state-changing ops run | read-only validation run | classification-only run | evidence-refresh-only run | discovery-only run | controlled vendor smoke  
* **External execution classification, if applicable:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable | other approved classification  
* **Does the approved ops task itself claim PF09 or canon closure now:** Yes | No  
* **If command discovery is the approved purpose, what command-proof result was reached:** concrete command proven | unresolved sentinel recorded | blocked by missing target facts | not applicable  
* **If blocker classification is the approved purpose, what classification result was reached:**  
* **If No, what bounded purpose is being accepted:**  
* **If No, what still-open state must remain explicit:**  
* **If No, which later approved task or step owns remaining closure work, if any:**  
* **Command ledger and checksum evidence:** state whether every action actually performed is recorded and whether checksum or integrity evidence covers the captured files.  
* **Row-level closure proof for corpus, parity, or multi-row closure claims:** state the active corpus or row inventory, any excluded or skipped rows, row-level status for each active row, the closure decision artifact, the consistency-check result, and whether the consistency result agrees with the row-level proof.  
* **Scope-rationale evidence when corpus interpretation was contested or remediated:** state the authority or rationale used, whether the run resolved the issue through inclusion and match or through exclusion, and whether any external exclusion authority remains necessary.  
* **Secret and environment evidence posture:** presence-only booleans | redacted | hashed | not applicable; state whether any secret-value persistence is evidenced.  
* **Non-claims preserved:** QA PASS | Live QA completion | PF09 status change | epic closure | PF-canon drain completion | other  
* **Evidence-packaging or close-pack surfacing scope:** when run posture is evidence-refresh-only, evidence packaging, or close-pack surfacing, verify that no QA reruns, vendor calls, implementation changes, PF-Canon edits, PF09 status-drain claims, new acceptance claims, or new tokens occurred unless the approved task explicitly authorized them.  
* **Remediated evidence-packaging proof set:** when accepting a repaired Ops evidence bundle, Evidence Print must cover the corrected command transcript, labeled stdout, labeled stderr, labeled exit-code ledger, final inventory, inventory path-proof, final validation log, close-pack manifest `key_outputs` bindings when present, close report and manifest path proofs when present, checksum ledger, and any superseded artifacts preserved for audit.  
* **Final validation posture:** a narrative completion statement is not enough; the review must identify the executable validation output that reconciles file existence, manifest, close report, path-proofs, final inventory, checksum ledger, and Ops evidence files for the approved scope.  
* **Later-drain posture:** if the task only surfaces close-pack or drain-target evidence, the review must record `No status change recommended` or `Not yet supportable from repo evidence` for PF09.x status changes unless the approved task also proves the exact PF09.x row-status predicate.

**Findings**

**FND-001**

* **What I observed:**  
* **Why it matters:**  
* **Expected requirement from the Approved Plan:**  
* **Blocker for acceptance: Yes | No**  
* **Evidence pointer(s):**

**Repeat finding blocks as needed.**

**Evidence Print (PASS PROOF; required)**

**A) Required deliverables satisfied**

* **Deliverable name:**  
* **Evidence pointer:**  
* **Key proof facts:**

**Repeat deliverable lines as needed.**

**B) Commands/actions evidence**

* **Action:**  
* **Evidence pointer:**  
* **Success signal found in evidence:**

**Repeat action lines as needed.**

**C) Configuration/infra state evidence (if applicable)**

* **Evidence pointer:**  
* **What state it proves:**

**D) PF09 later-drain support (if applicable)**

Use this section only when the approved Ops task ties the run to HDE Build Checklist completion, close, or later-drain posture. Complete the mapping fields:

* **Work item ID:**  
* **PF09 disposition:** in the current epic with exact phased PF09 task or subtask mapping | out of the current epic with exact phased PF09 task or subtask mapping | PF09 gap | documentation/status drainage only | out of HDE phased-build scope  
* **Phased PF09 document:** exact current in-document title, or `N/A` only for a non-mapping posture  
* **Task ID:** exact ID, or `N/A` with the selected non-mapping posture  
* **Subtask ID:** exact relevant ID; `None exists` only after verifying no relevant subtask exists  
* **Exact source heading:**  
* **Contribution:** advances | satisfies | leaves open | documents  
* **Status nonclaim:** this artifact does not itself move PF09 status  
* **Current claim in the approved task or plan:**  
* **Supportable later-drain action:** no PF09 support proven | supportable from Ops evidence only | supportable after PR/QA/closeout binding | supportable from repo evidence | already drained | not applicable  
* **Evidence basis:**  
* **Non-claim notes:** state whether the Ops run avoids QA PASS, PF09 status move, epic closure, acceptance-token satisfaction, or other overclaim.  
* **Later owner:** state whether later PR, QA, closeout, or canon-only drain work owns any status movement.

**Repeat state-evidence lines as needed.**

**Decision**

* **Decision:**  
* **Why this decision is supported:**  
* **Remaining risk or not-yet-closed state, if any:**  
* **Supported downstream binding or follow-on use, if any:**

**Later-Drain PF-Canon Update (required when this review supports later PF-canon drainage)**

* **Affected PF canon home(s):**  
* **Exact affected locator(s):**  
* **Current canon posture:**  
* **Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended**  
* **Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon**  
* **Evidence basis:**  
* **Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step**

## **12\) General Implementation Plan (Template)**

### **Applicability and ownership boundary**

Use this template for a project implementation plan only when no more-specific PF27 template controls the artifact class. It does not replace the HDE Epic Plan, Ops Task Record, Epic Remediation Plan, Remediation Implementation Guide, Live QA Plan, or any review or closeout record. PF27 owns this reusable shape; `PF06-Canon-Epic-Process-Guide` owns process sequencing, roles, approval responsibilities, and PR-first discipline.

### **Required structure**

#### **Plan identity and revision**

* **Plan identity:**  
* **Plan type:** General Implementation Plan  
* **Revision:**  
* **Date (UTC):**  
* **Prepared by:**  
* **Applicable epic, issue, or work-slice identity:**

#### **Purpose, scope, exclusions, and nonclaims**

* **Purpose:**  
* **In scope:**  
* **Out of scope:**  
* **Non-goals:**  
* **Current implementation claims:** state only what pinned or otherwise approved repository evidence proves.  
* **Nonclaims:** state which implementation, OPS, QA, acceptance, deployment, release, status, and closeout outcomes are not established by this plan.

#### **Governing-source map**

| Topic | Exact current source title | Exact locator | How it constrains this plan |
| :---- | :---- | :---- | :---- |
| `<topic>` | `<in-document title>` | `<heading or exact anchor>` | `<constraint>` |

Do not copy externally owned process, token, schema, transport, architecture, infrastructure, QA, or evidence-contract bodies into this plan. Retain the local writer-facing consequence and route the governed truth to its owner.

#### **Observed repository reality and validated loci**

* **Pinned or approved repository identity:**  
* **Validated existing loci:**  
* **Observed implementation state:**  
* **Contradictions or partial findings:**  
* **Unknown or not-found posture:** use bounded inspection language; do not convert absence into future posture.  
* **Repository-dependent nonclaims:**

#### **Work-slice and dependency map**

| Work slice ID | Lane | Purpose | Dependencies | Inputs | Outputs | Owner | Completion predicate |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `<ID>` | PR implementation | OPS | QA planning | QA execution | `<purpose>` | `<IDs or None>` | `<inputs>` | `<outputs>` | `<role>` | `<predicate>` |

Each dependency MUST name its producer and the exact output consumed. Do not treat later QA execution, PF-canon drainage, board updates, or closeout as implementation completion unless the owning process explicitly makes that item part of the approved slice.

#### **HDE phased accountability (when HDE work is in scope)**

Complete one row for every task-like HDE item. A reusable template does not preselect a phase.

| Work item ID | PF09 disposition | Phased PF09 document | Task ID | Subtask ID | Exact source heading | Contribution | Status nonclaim |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `<ID>` | `in the current epic with exact phased PF09 task or subtask mapping` | `out of the current epic with exact phased PF09 task or subtask mapping` | `PF09 gap` | `documentation/status drainage only` | `out of HDE phased-build scope` | `<exact current in-document title or N/A>` | `<exact ID or N/A>` | `<exact ID or None exists>` | `<exact heading>` | `<advances, satisfies, leaves open, or documents>` | `This plan does not itself move PF09 status.` |

Use separate rows for independently mapped cross-phase scope. A parent task alone is insufficient when a relevant subtask exists.

#### **Lane separation and authorization**

* **PR implementation:** repo changes only; identify reviewable outputs and rollback or reversion posture.  
* **OPS:** separate privileged external actions from PR work. Record PO authorization, personal execution or explicit delegation, IA guidance, target, rails, secret-safe evidence, failure handling, and nonclaims in the Ops Task Record.  
* **QA planning:** name intended proof and evidence families without claiming unexecuted results.  
* **QA execution:** route to the applicable Live QA or QA-owned artifact; this implementation plan does not issue a QA verdict.

#### **Conditional data, privacy, security, migration, rollout, and rollback fields**

For each applicable topic, state the exact requirement, owner, evidence or validation intent, failure boundary, and nonclaim. If a topic is not applicable, state `Not applicable` with the source-grounded reason.

* **Data and persistence:**  
* **Privacy and sensitive-data boundary:**  
* **Security and authorization:**  
* **Migration and compatibility:**  
* **Rollout or release posture:**  
* **Rollback or safe refusal:**

#### **Deliverables and implementation-completion predicates**

| Deliverable ID | Concrete output | Owning lane | Completion predicate | Evidence or review pointer | Nonclaim |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `<ID>` | `<output>` | `<lane>` | `<mechanical predicate>` | `<pointer>` | `<what completion does not prove>` |

Implementation completion MUST remain separate from QA PASS, OPS completion outside the approved task, acceptance-token satisfaction, PF09 status movement, deployment success, release, board state, and epic closure unless the applicable owning authority explicitly establishes the relationship.

#### **Validation and test intent**

* **Static and unit validation intent:**  
* **Integration or contract validation intent:**  
* **Open-rails or external validation intent, when applicable:**  
* **Expected evidence identity and owner:**  
* **Failure or blocked classification intent:**  
* **Unexecuted-result nonclaim:** no test, QA, deployment, or runtime result is claimed by this plan.  
* **Domain-correctness proof map, when HDE mechanics or compatibility is in scope:** identify each governed predicate independently. A complete Magic-10 claim requires all ten categories; harmony-only proof is insufficient.

#### **Open-decision routing**

When a material decision remains unresolved, route it to **Remediation Implementation Guide (Template) \> Open Decisions**. Do not reproduce the decision marker or its record body here. If no decision remains, state `None.`

#### **Approval**

* **Approval sentinel:** `ASK OK?`  
* **Approval state:** Pending | Approved | Rejected  
* **Approval authority:**  
* **Approved scope or rejection basis:**

Approval of this plan does not establish implementation, QA, OPS, deployment, release, acceptance, PF09 drainage, board, or closeout state.

