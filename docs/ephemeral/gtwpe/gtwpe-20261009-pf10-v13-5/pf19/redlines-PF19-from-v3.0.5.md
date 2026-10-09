# Redlines — PF19 from v3.0.5

Task: `T-PF19`; run: `T-PF19-20261009-root-01`; package revision: `2`.
Originating preparer: this Work/Codex conversation, primary agent `/root`, workspace `/workspace/scratch/4b56edd45caf`; no separate provider-session URL is available.
Prompt: TW-DRAIN-10 — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Original: `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; raw UTF-8 SHA-256 `2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0`, 657,008 bytes.
Preparation outcome: READY; package availability is established separately in the companion proof log after actual saved-file readback.
Every operation resolves independently against this unchanged original. Literal payloads include all intended whitespace/newlines; the one newline immediately before a closing fence is the payload delimiter, not an extra payload byte. INSERT anchors are retained and adjacent in the original.
Document-control version/date/Last Update Gate fields are reserved to TW-APPLY-10. Baseline native fields: v3.0.5; effective date 2026-09-08; Last Update Gate PF10 13.0.9. Apply derives v3.0.6, its actual execution date and gate sources in this order: PF10-HDE-Build-Notes-v13.5.md; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md. Status Canon and invocation tag are unchanged.

## Redline RL-01

**Operation:** REPLACE

**Original-bound heading path:** # **0\. Front Matter** → ## **0.2 Purpose & scope**

**Location within that path:** 0.2 Purpose & scope / authored work products

**Expected occurrence:** 1

**OLD**

````text
Authored off-repository QA work products use ChatGPT Library under §0.4.3. Existing repository plans such as `docs/qa/<crd-id>-live-qa-plan.md` retain their recorded role; their existence is not a universal QA prerequisite. This does not re-home repository-controlled execution evidence or authorize migration of historical files.
````

**NEW**

````text
New authored QA work products are stored in `docs/ephemeral/` and referenced by repository path under §0.4.3. Existing repository plans such as `docs/qa/<crd-id>-live-qa-plan.md` retain their recorded role; their existence is not a universal QA prerequisite. This does not re-home repository-controlled execution evidence or authorize migration of historical files.
````

## Redline RL-02

**Operation:** REPLACE

**Original-bound heading path:** # **0\. Front Matter** → ## **0.4 Principles & Single Homes (routing only)** → ### **0.4.3 Core principles (names-only).**

**Location within that path:** 0.4.3 Source and work-product posture / storage paragraph

**Expected occurrence:** 1

**OLD**

````text
Off-repository change-process artifacts, including QA readiness, audit, triage, Guide, Plan, task, review, final Report, separate RCA and remediation work products, are saved in ChatGPT Library. Scratch is transient preparation space. File size, a large attachment or an export does not create a Drive fallback; Notion may carry concise status and usable links, not a second artifact body. Repository-controlled code, tests and governed mechanical evidence remain at their approved repository paths. Existing historical artifacts are not migrated automatically. Product Owner publication of PF10, PF23 or historical change records remains separately authorized administration.
````

**NEW**

````text
Change-process artifacts, including QA readiness, audit, triage, Guide, Plan, task, review, final Report, separate RCA and remediation work products, are stored in `docs/ephemeral/` and referenced by repository path. A document whose class is uncertain is stored there too. Scratch is transient preparation space. ChatGPT Library and Google Drive are neither destinations nor authorities for these documents; a specific Product Owner-directed Drive file remains non-authoritative. Notion may carry concise status and usable links, not a second artifact body; prompt bodies retain their single home in Notion. Repository-controlled code, tests, configuration and governed mechanical evidence remain at their established repository paths and writers. Existing historical artifacts and their provenance are not migrated automatically. Product Owner publication of PF10, PF23 or historical change records remains separately authorized administration.
````

## Redline RL-03

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.3 Environment constraints — pre-App, no-user QA mode**

**Location within that path:** 3.3 No-user QA mode / controlled vendor-backed no-user smoke

**Expected occurrence:** 1

**OLD**

````text
* Controlled vendor-backed no-user smoke execution is PO-only and IA-guided. It must use explicit open rails only for the vendor step, capture determinism pins, store no secret values, capture only presence-safe secret posture, and avoid guessed commands, hosts, ports, URLs, service bindings, targets, credentials, birth values, or environment facts.  
````

**NEW**

````text
* Controlled vendor-backed no-user smoke execution is Product Owner-authorized and IA-guided. An automated session agent executes the identified vendor task when the Product Owner directs it, under §3.5.7. The Product Owner remains the authorizing and accountable principal; the directed agent is the executor and evidence producer, not an independent approver. The step must use explicit open rails only for the vendor call, capture determinism pins, use synthetic inputs only, store no secret values, capture only presence-safe secret posture, and avoid guessed commands, hosts, ports, URLs, service bindings, targets, credentials, birth values, or environment facts.  
````

## Redline RL-04

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.3 Environment constraints — pre-App, no-user QA mode**

**Location within that path:** 3.3 No-user QA mode / execution boundary

**Expected occurrence:** 1

**OLD**

````text
* The controlled vendor-backed no-user implementation smoke above retains its stated PO-only boundary. Other bounded QA or Ops tasks may be assigned to an authorized repository-capable execution agent when their actual task, role, scope, rails, credential, evidence and approval requirements are satisfied. Capability or repository access alone grants no execution authority. No command may be modified by guesswork to force PASS; documentation drainage does not perform PR, Ops, QA or closure work.  
````

**NEW**

````text
* The controlled vendor-backed no-user implementation smoke above retains its Product Owner authorization boundary and permits the directed execution defined in §3.5.7. Other bounded QA or Ops tasks may be assigned to an authorized repository-capable execution agent when their actual task, role, scope, rails, credential, evidence and approval requirements are satisfied. Capability or repository access alone grants no execution authority. No command may be modified by guesswork to force PASS; documentation drainage does not perform PR, Ops, QA or closure work.  
````

## Redline RL-05

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)** → ### **3.4.3 Evidence layout: current-state first (new posture)** → #### **QA evidence and work-product path grammar (normative)**

**Location within that path:** 3.4.3 / QA evidence and work-product path grammar / Authored Live QA plan or runbook row

**Expected occurrence:** 1

**OLD**

````text
| Authored Live QA plan or runbook | ChatGPT Library for off-repository authored process artifacts | Preserve exact change, version and approval identity with a usable retrieval reference. It is not execution evidence, a manifest entry or proof that QA ran. Repository-controlled evidence and existing historical plan files retain their separate roles; no automatic migration or new repository-plan publication prerequisite. |
````

**NEW**

````text
| Authored Live QA plan or runbook | `docs/ephemeral/`, referenced by repository path | Preserve exact change, version and approval identity with a usable retrieval reference. It is not execution evidence, a manifest entry or proof that QA ran. Repository-controlled evidence and existing historical plan files retain their separate roles; no automatic migration or new repository-plan publication prerequisite. |
````

## Redline RL-06

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)** → ### **3.4.8 Rails posture for manual Live QA (EPIC017 example; generalized rule)**

**Location within that path:** 3.4.8 QA execution/remediation / tracked entrypoints paragraph

**Expected occurrence:** 1

**OLD**

````text
QA plans MUST invoke tracked, reviewed, tested repository entrypoints. A plan MUST NOT embed compressed source, base64 executable payloads, large inline programs, newly invented runners, or substitute repository tooling. A missing required entrypoint is an implementation-readiness gap that MUST route through the normal PR, test, and CI path before Live QA planning.
````

**NEW**

````text
QA plans MUST invoke tracked, reviewed, tested repository entrypoints. A plan MUST NOT embed compressed source, base64 executable payloads, large inline programs, newly invented runners, or substitute repository tooling. A missing required entrypoint is an implementation-readiness gap that MUST route through the normal PR, test, and CI path before Live QA planning.

Where the approved task permits it, invoking tracked, tested QA harness or proof-refresh APIs through `python -c` is invocation of the repository entrypoint, not a newly written decisive evaluator. Read-only git observations establish attribution under §3.4.9 and never a PASS predicate. An approved task’s narrower no-script condition still applies; execution-only wrappers do not acquire authority to evaluate new decisive predicates.
````

## Redline RL-07

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)** → ### **3.4.10 Plan validity lint (blockers-only; deterministic)**

**Location within that path:** 3.4.10 / Plans are not execution artifacts bullet

**Expected occurrence:** 1

**OLD**

````text
Codex prompts
````

**NEW**

````text
prompts given to the executing agent
````

## Redline RL-08

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)** → ### **3.4.10 Plan validity lint (blockers-only; deterministic)**

**Location within that path:** 3.4.10 / Syntax correction is ordinary execution hygiene bullet

**Expected occurrence:** 1

**OLD**

````text
A QA operator, Codex, Kronos, PO, or implementation owner
````

**NEW**

````text
A QA operator, executing agent, Kronos, PO, or implementation owner
````

## Redline RL-09

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.5 PO Live QA sessions (vendor-first rails)**

**Location within that path:** 3.5.5 PO Live QA sessions / Definition and scope

**Expected occurrence:** 1

**OLD**

````text
Definition and scope are as follows: a PO-run Live QA session is a short, focused session whose primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.
````

**NEW**

````text
Definition and scope are as follows: a Product Owner-authorized Live QA session is a short, focused session whose primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior. The Product Owner may direct an automated session agent to execute the identified vendor task under §3.5.7. A CLI-local vendor smoke has its own target and proof limits; it must not be described as deployed-service validation merely because the vendor is live.
````

## Redline RL-10

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.5 PO Live QA sessions (vendor-first rails)**

**Location within that path:** 3.5.5 / Roles of each class / ops and identity steps

**Expected occurrence:** 1

**OLD**

````text
are designed and executed by QA/infra (or CodEx)
````

**NEW**

````text
are designed and executed by QA/infra (or the executing agent)
````

## Redline RL-11

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.5 PO Live QA sessions (vendor-first rails)**

**Location within that path:** 3.5.5 / Production-affecting Live QA minimum

**Expected occurrence:** 1

**OLD**

````text
Production-affecting Live QA minimum is as follows.

For any epic that can affect real production functionality, deployed runtime behavior, external integrations, vendor ingest, vendor route policy, external API transport, DB persistence or retrieval, public or app-facing behavior, CLI behavior, operator-facing CLI surfaces, runtime request or response behavior, compute used by production, admin or ops-facing behavior that can affect production, or secret or environment binding, the Live QA Plan MUST include at least one bounded open-rails live QA step that proves a real production-relevant behavior in the deployed or live environment.

Closed-rails proof remains required where applicable, but closed-rails proof alone is not sufficient for a production-affecting epic unless the plan records an explicit authorized exemption. A valid exemption must state why open-rails live QA is not safe or not applicable, what closed-rails proof remains available, what production claim is not being made, and what follow-up is required before the omitted production-facing claim can be made.

The open-rails live QA step must be scoped, PO-authorized, secret-safe, mechanically evidenced, and clear about what it proves and does not prove. It must not rely only on mocked fixtures, closed-rails replay, static analysis, generated artifacts, documentation review, repo-local inspection, PF09 supportability language, or a written but unexecuted smoke procedure.


````

**NEW**

````text
Production-affecting Live QA minimum is as follows.

For any epic that can affect real production functionality, deployed runtime behavior, external integrations, vendor ingest, vendor route policy, external API transport, DB persistence or retrieval, public or app-facing behavior, CLI behavior, operator-facing CLI surfaces, runtime request or response behavior, compute used by production, admin or ops-facing behavior that can affect production, or secret or environment binding, the Live QA Plan MUST include at least one bounded open-rails live QA step that proves a real production-relevant behavior in the deployed or live environment.

Whenever the epic touches a surface used to produce a production feature that PF-Canon describes as functional, its QA Plan MUST include a live vendor call under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`), using synthetic data only and no real person, user or production data. A plan without that test is not approval-ready; an earlier approval without it does not satisfy this requirement. The approved Specification and plans identify the affected surfaces. An exemption, a closed-rails substitution or a live non-vendor step does not satisfy this functional-feature scope.

For production-affecting work outside that functional-feature scope, the existing exemption alternative remains bounded: closed-rails proof alone is not sufficient unless the plan records an explicit authorized exemption stating why open-rails live QA is not safe or not applicable, what closed-rails proof remains available, what production claim is not made, and what follow-up is required before that omitted claim can be made. This alternative does not exempt the mandatory live vendor test above.

Closed-rails tests, fixture replay, mocks or fake services, static analysis, generated or governed artifacts, path-proof validation, Index or Mirror refresh, repository inspection, review approval, an unrun smoke procedure and OPS discovery without a live vendor call do not satisfy the mandatory vendor test. A deployed-service check or database read alone does not satisfy it either.

The test remains bounded, Product Owner-authorized, secret-safe, mechanically evidenced, subject to its defined request limit and stop checks, and clear about its exercised behavior and nonclaims. It authorizes no load, stress or volume testing and raises no request limit. Open-rails Ops evidence retains its Ops class and feeds QA only as the governing QA Plan defines. A passing test proves only what it exercises; it establishes no full vendor conformance, whole-change QA PASS, acceptance, PF09 movement, deployment or closure.


````

## Redline RL-12

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / minimum vendor-step captures / request description

**Expected occurrence:** 1

**OLD**

````text
* a request description file (schematic example: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_request.txt`) that names the command or GUI action, the environment used, and the inputs (birth tuples, synthetic IDs, or, once in scope, user IDs)  
````

**NEW**

````text
* a request description file (schematic example: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_request.txt`) that names the command or GUI action, the environment used, and the synthetic inputs; live vendor calls use no real person, user or production data  
````

## Redline RL-13

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / HDAPI v2 distinct proof classes

**Expected occurrence:** 1

**OLD**

````text
PO-only open-rails vendor-smoke proof
````

**NEW**

````text
PO-authorized open-rails vendor-smoke proof
````

## Redline RL-14

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / canonical vendor configuration bullet

**Expected occurrence:** 1

**OLD**

````text
* HDAPI vendor QA plans MUST use `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key. QA may check for `HDAPI_BASE_URL` only as deprecated alias, compatibility fallback, migration evidence, or drift evidence. QA MUST NOT treat `HDAPI_BASE_URL` as canonical. If `HD_API_BASE_URL` and `HDAPI_BASE_URL` both exist with conflicting values, QA must classify the result as configuration ambiguity, not product behavior failure.  
````

**NEW**

````text
* HDAPI vendor QA plans use vendor configuration from the execution environment: two API keys, `HD_API_KEY` and `GEO_API_KEY`, and a base URL. The base URL is configuration, not an API key. `HD_API_BASE_URL` is canonical; `HDAPI_BASE_URL` is a compatibility fallback only when the canonical key is absent. Conflicting values fail closed as configuration ambiguity, not product behavior failure. Plans, tasks and agents MUST NOT ask the Product Owner to type, paste or re-enter vendor values, and a rails posture MUST NOT remove the only base URL the environment holds. Passing the environment to the product process is permitted; record only `SET` or `UNSET`, keep values off process argument lists and out of conversations, logs, files and commits, and scan captured output before it enters evidence. If a required variable is missing, no vendor call runs; record missing names by presence only and classify an already-begun step as `TOOLING_BLOCKED`. Manual value entry is not a substitute.  
````

## Redline RL-15

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / open-rails vendor executor bullet

**Expected occurrence:** 1

**OLD**

````text
* Open-rails HDAPI v2 vendor smoke is PO-only execution, IA-guided. Automated agents may define intent, safety rails, success criteria, evidence requirements, and rollback intent, but MUST NOT execute the vendor call, handle plaintext secrets, or claim completion without PO-run evidence.  
````

**NEW**

````text
* Open-rails HDAPI v2 vendor smoke is Product Owner-authorized and IA-guided. An automated session agent executes the identified task when the Product Owner directs it. The Product Owner is the authorizing and accountable principal; the agent is the executor and evidence producer, not an independent approver. The task’s scope, exact commands, rails, request limit, stop checks, synthetic inputs, secret scan and quarantine, redaction and evidence contract bind every executor equally. No command is changed by guesswork and no completion is claimed without the required evidence. This creates no standing authority for vendor calls or other privileged actions. Existing plans that name the Product Owner as physical executor retain their historical standing; directed execution uses their unchanged commands and environment-held configuration.  
````

## Redline RL-16

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / bounded live smoke proof bullet

**Expected occurrence:** 1

**OLD**

````text
A bounded PO-produced open-rails smoke may prove
````

**NEW**

````text
A bounded PO-authorized open-rails smoke may prove
````

## Redline RL-17

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.5 Live QA via Codespaces → Railway (cross-epic crib)** → ### **3.5.7 Evidence expectations for vendor-focused PO steps**

**Location within that path:** 3.5.7 / allowed bounded operational verification bullet

**Expected occurrence:** 1

**OLD**

````text
A QA Plan may include a bounded PO-run OPS open-rails task
````

**NEW**

````text
A QA Plan may include a bounded PO-authorized OPS open-rails task, including execution by the directed agent under this section,
````

## Redline RL-18

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.6 Repo introspection before Live QA plan (d0 planning artifacts)**

**Location within that path:** 3.6 Repo introspection / opening paragraph

**Expected occurrence:** 1

**OLD**

````text
Before finalizing the Live QA Plan, Kronos must establish the current tools, paths and prerequisites through its independent QA Audit and required mechanical repository introspection. Reuse relevant current evidence without repeating completed analysis merely to create another artifact. This does not add a readiness gate after Isis’s integrated QA-10. Authored audits and Plans use ChatGPT Library; mechanically produced D0 evidence uses its approved governed QA paths and actual authorized execution owner.
````

**NEW**

````text
Before finalizing the Live QA Plan, Kronos must establish the current tools, paths and prerequisites through its independent QA Audit and required mechanical repository introspection. Reuse relevant current evidence without repeating completed analysis merely to create another artifact. This does not add a readiness gate after Isis’s integrated QA-10. Authored audits and Plans are stored in `docs/ephemeral/` and referenced by repository path; mechanically produced D0 evidence uses its approved governed QA paths and actual authorized execution owner.
````

## Redline RL-19

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.6 Repo introspection before Live QA plan (d0 planning artifacts)**

**Location within that path:** 3.6 / audit observed evidence block

**Expected occurrence:** 1

**OLD**

````text
**Codex Audit observed evidence (planning-time only)**

A supplied Codex Audit may support QA planning context and pre-QA repo-reality framing for existing paths, components, tests, helpers, evidence helpers, governed artifacts, index or mirror files, and expected loci that QA should later verify. Acceptable labels include “Observed Evidence (Codex Audit)” and “Observed repo reality (Codex Audit).”

Codex Audit observed evidence does not by itself prove QA PASS, acceptance-token satisfaction, Live QA execution, OPS completion, PF09 status movement, epic closure, live vendor truth, production truth, secret validity, runtime conformance beyond observed repo reality, or canon authority. Those claims still require the owning PF source, governed QA evidence, OPS evidence, PO confirmation, or later closeout evidence as applicable.

QA plan reviewers MUST NOT reject a plan solely because repo-reality context came from a supplied Codex Audit. Reviewers must block only when the observation is overclaimed beyond repo reality, materially ambiguous, stale without a planned current check, contradictory to PF10 or PF-Canon, or used as acceptance, QA, OPS, closure, PF09-drainage, canon, or live-vendor proof without the owning source.


````

**NEW**

````text
**Read-only repository audit observed evidence (planning-time only)**

A supplied read-only repository audit may support QA planning context and pre-QA repo-reality framing for existing paths, components, tests, helpers, evidence helpers, governed artifacts, index or mirror files, and expected loci that QA should later verify. The vocabulary labels “Observed Evidence (Codex Audit)” and “Observed repo reality (Codex Audit)” keep their exact spelling and denote this audit function, whichever agent produced it.

Read-only repository audit observed evidence does not by itself prove QA PASS, acceptance-token satisfaction, Live QA execution, OPS completion, PF09 status movement, epic closure, live vendor truth, production truth, secret validity, runtime conformance beyond observed repo reality, or canon authority. Those claims still require the owning PF source, governed QA evidence, OPS evidence, PO confirmation, or later closeout evidence as applicable.

QA plan reviewers MUST NOT reject a plan solely because repo-reality context came from a supplied read-only repository audit. Reviewers must block only when the observation is overclaimed beyond repo reality, materially ambiguous, stale without a planned current check, contradictory to PF10 or PF-Canon, or used as acceptance, QA, OPS, closure, PF09-drainage, canon, or live-vendor proof without the owning source.


````

## Redline RL-20

**Operation:** REPLACE

**Original-bound heading path:** # **3\. Post-commit QA (staging/prod)** → ## **3.6 Repo introspection before Live QA plan (d0 planning artifacts)**

**Location within that path:** 3.6 / D0 checklist / gitignore attribution bullet

**Expected occurrence:** 1

**OLD**

````text
including in the Codex prompt that produces the plan
````

**NEW**

````text
including in the prompt given to the executing agent that produces the plan
````

## Redline RL-21

**Operation:** REPLACE

**Original-bound heading path:** # **4\. Evidence & indexing (how to prove; titles-only for schemas)** → ## **4.6 Derived AI-readable evidence for HTTP response bodies**

**Location within that path:** 4.6 Derived evidence / privacy and complete-result paragraph

**Expected occurrence:** 1

**OLD**

````text
The derived artifact MUST remain privacy-preserving and MUST NOT calculate, reinterpret, or correct Human Design output. When the proof target is a complete internal Magic-10 result, it must preserve the exact ten-category identity and order, with every category exactly once and no extras, omissions, duplicates, defaults, or harmony-only substitution. A public Reader v1 review must preserve its narrower numeric-free public projection. The derived layer must not blur those surfaces.
````

**NEW**

````text
The derived artifact MUST remain privacy-preserving and MUST NOT calculate, reinterpret, or correct Human Design output. When the proof target is a complete internal Magic-10 result, it must preserve the exact ten-category identity and order, with every category exactly once and no extras, omissions, duplicates, defaults, or harmony-only substitution. A public Reader v1 review must preserve its narrower numeric-free public projection. A public Reader v2 review preserves the approved full ten-category bands-only, numeric-free projection; internal scores, signals and narrative keys do not become public values. The derived layer must not blur these distinct surfaces.
````

## Redline RL-22

**Operation:** REPLACE

**Original-bound heading path:** # **5\. Component playbooks (how to run QA per surface)** → ## **5.6 CLI/API & SDKs** → ### **5.6.1 Steps**

**Location within that path:** 5.6.1 / Establish a test pair and environment / post-App test IDs

**Expected occurrence:** 1

**OLD**

````text
* In environments where the app user model is live and user-bound BodyGraphs exist, test IDs may include real user IDs only where those surfaces are explicitly authorized by the approved change Specification and applicable owning product/QA contracts.  
````

**NEW**

````text
* In environments where the app user model is live and user-bound BodyGraphs exist, test IDs may include real user IDs only where those surfaces are explicitly authorized by the approved change Specification and applicable owning product/QA contracts. This does not permit real person, user or production data in a live vendor call; the synthetic-input rule in §3.5.7 applies.  
````

## Redline RL-23

**Operation:** INSERT

**Original-bound heading path:** # **5\. Component playbooks (how to run QA per surface)** → ## **5.8 Admin bundle surfaces (CLI & HTTP, HDE-only)** → ### **Failures to watch**

**Location within that path:** 5 / new 5.9 after complete 5.8, immediately before H1 6

**Expected occurrence:** 1

**BEFORE**

````text
ces return a full admin bundle when an invalid or revoked credential is used.  
* Operations logs are missing, lack correlation IDs, or contain raw birth data, secrets, or unnecessary PII.  
* Admin-bundle evidence artifacts are created or updated without corresponding Human Index and Machine Mirror updates in the same PR, or without path-proofs.


````

**AFTER**

````text
# **6\. Catalog/A7 proofs (collected rules; HDE-specific bytes live elsewhere)**

````

**INSERT**

````text
## **5.9 Gate-based mechanics, admission and Reader proof boundaries**

This playbook applies to the Gate-based mechanics contract owned by HDE-Math-Spec, HDE-Architecture, HDE-Schemas & Artifacts, HDE-Mechanics Guide and HDE-CLI-API-Vendor-Ref. Exact mathematics, schemas, release membership, error bytes and writers stay at those homes. HDE-Build Notes supplies applicable approved overrides; a Specification supplies selected scope, not a current execution result.

QA binds each claim to its actual proof class:

| Claim | Decisive proof and rejection boundary | What it does not establish |
| :---- | :---- | :---- |
| Catalog and mechanics closure | Complete owner-governed catalog/configuration/schema execution, cross-source closure and positive/negative cases; count-only checks, snapshots substituted for active configuration, missing/extra members or invalid ordering are insufficient. | Complete release admission, runtime integration or live behavior. |
| Immutable loading and pure compute | Actual executable-schema, member/hash/release and deep-immutability checks outside the pure four-argument Engine Core; no swallowed refusal, hidden configuration selection, fallback scoring or partial successful result. | Admission from a synthetic fixture, live database readiness or independent QA acceptance. |
| Complete release admission and identity | The admission owner accepts only the complete pinned roster and owner-governed manifest/member/schema bindings. Configuration/source and release digests are distinct from repository commit IDs and index records. | Release activation, deployment or an external attestation merely from loader success. |
| Exact golden comparison | The complete governed goldens pass through canonical behavior; mismatch/invalid-input cases and before/after non-mutation evidence establish exact read-only comparison, with AB/BA and repeated-input identity where applicable. | A copied expected result, legacy calculator, synthetic-root success substituted for the actual candidate or configuration activation. |
| Gate ingress and readiness | Invalid, missing, empty, duplicate, noncanonical or out-of-domain input refuses; current-row readiness is a bounded read-only observation of the actual selected rows, with typed refusal when unavailable. | A live observation from fake-DB tests, vendor acquisition, row repair, backfill or fabricated readiness. |
| Reader and integration | Separate internal/admin complete results, Reader v1 harmony-only or ineligible-empty public projection, and approved Reader v2 ten-in-order bands-only public projection. Both public versions remain numeric-free; projections do not rescore or change mechanics identity. | Public numbers or narrative keys, a second calculator, deployed success from in-process tests or Reader v2 HTTP success from a v1 CLI dump. |
| Evidence and decisions | Owning writers produce coherent applicable manifest, Index, Mirror, hash and path-proof bindings; exact outcomes retain failed/unexecuted work, tested-source identity and limitations. | QA from evidence presence, acceptance from CI, PF09 mutation from supportability or closure from a QA verdict. |

Production application Reader tests address `POST /api/reader` with explicit `v=1` or `v=2`; the development `GET /reader` surface is distinct. Route/method/environment reachability, public schema conformance, eligibility, typed refusals, transport and secret-safe failure posture are evaluated against their owning contracts. A7 success-proof eligibility is a separate catalog/transport class; a production POST, dev preview or ops identity ping is not interchangeable A7 proof. The retained §6 collection remains subject to §5.1’s non-authority rule where it conflicts with the current owners.

An incomplete active release is never PASS, a success attestation or a frozen-byte substitute for live behavior. The approved PR04-to-PR06 interval treatment accepted only the explicit non-admitted outcome and independently observed incomplete roster; it accepted no unrelated failure, skipped test or synthetic release. It self-extinguished when complete admission landed. The recorded progression was the incomplete 15-member release, then PR06’s admitted 44-member `1.1.0`, PR06a’s 45-member `1.2.0`, and PR06b’s 45-member `1.3.0`. This is release lineage, not authority to create a partial-release exception or reactivate the interval on an admitted candidate.

Frozen captures retain their digest-verified capture-time identity. Their capture identities must agree; the canonical JSON gate does not re-identify them from current service identity. The current identity family and external release attestation retain their separate owners and actual release/source bindings. A supplemental adverse attestation check proves its refusal cases only; neither it nor offline readiness proves vendor, deployed-service or live-database behavior. §§3.3, 3.5.5–3.5.7 and 10.8 control environment limits, vendor authority and substantive currentness.


````

## Redline RL-24

**Operation:** REPLACE

**Original-bound heading path:** # **9\. Legacy QA acceptance-token compatibility** → ## **9.2 Legacy QA Acceptance Token Library (optional compatibility)** → ### **9.2.14 Optional legacy token/evidence cross-reference and review rails** → #### **9.2.14.5 Legacy token-governance addendum alignment (conditional)**

**Location within that path:** 9.2.14.5 Legacy token-governance addendum alignment / citation bullet

**Expected occurrence:** 1

**OLD**

````text
* Cite the governing addendum by addendum number and title for the affected retained token.  
````

**NEW**

````text
* Name HDE-Build Notes by title only in PF19; resolve the applicable current override by its topic and scope. Retained historical metadata keeps its original source attribution.  
````

## Redline RL-25

**Operation:** REPLACE

**Original-bound heading path:** # **10\. QA checklists, harnesses, and review rules** → ## **10.8 QA source attribution and substantive currentness** → ### **Canonical authority and bounded execution sources**

**Location within that path:** 10.8 / Canonical authority and bounded execution sources

**Expected occurrence:** 1

**OLD**

````text
### **Canonical authority and bounded execution sources**

Google Drive `Glow / Core Docs / PFCanon` remains the canonical source for readiness, QA planning, Plan review and task preparation. Resolve the current authoritative Markdown for reading; repository PF copies are publication/execution copies, not an independent PF editing authority.

An authorized bounded QA or Ops executor may use the PF copies actually available under `docs/pfcanon` in its repository-capable environment, including a local execution client with repository-only access. Missing Drive access does not require a fresh Drive comparison, synchronization certificate or another planning gate. Record the PF sources actually used, their available versions and material known limitations. This exception does not extend to planning/governance work or authorize PF mutation.


````

**NEW**

````text
### **Canonical authority and actual execution sources**

The current PF Markdown in `docs/pfcanon/` on `main` is authoritative for readiness, QA planning, governance, Plan review, task preparation and QA/Ops execution. Each document keeps its declared standing. Native Google Docs, exports, Drive folders, Notion pages and PF-named files elsewhere confer no PF authority. Repository canon remains read-only for agents except under the Product Owner’s exact authority for the identified document and action.

Record the PF sources actually used, their available versions and material known limitations. An executor records the source actually accessible in its execution environment; material divergence affecting the claim is reconciled under this section, without a Drive comparison, synchronization certificate or another planning gate. Canon location grants no tool, credential, network, rails, mutation or privileged-action permission. Authored change-process documents use §0.4.3; governed evidence retains its established homes and writers.


````

## Redline RL-26

**Operation:** REPLACE

**Original-bound heading path:** # **11\. Roles & RACI (QA)** → ## **11.3 Canon-first QA preparation**

**Location within that path:** 11.3 Canon-first QA preparation / opening paragraph

**Expected occurrence:** 1

**OLD**

````text
Isis’s Guide and Kronos’s independent QA Audit/Plan use current authoritative sources for the actual approved change. Implementation actors retain the same no-invention discipline in their own work. Apply §10.8’s narrower repository-PF exception only to authorized bounded QA/Ops execution, not to planning or governance.
````

**NEW**

````text
Isis’s Guide and Kronos’s independent QA Audit/Plan use current authoritative sources for the actual approved change. Implementation actors retain the same no-invention discipline in their own work. Resolve current PF Markdown in `docs/pfcanon/` on `main` under §10.8 for planning, governance and execution; repository access does not confer PF editing or privileged-action authority.
````

## Redline RL-27

**Operation:** REPLACE

**Original-bound heading path:** # **11\. Roles & RACI (QA)** → ## **11.3 Canon-first QA preparation**

**Location within that path:** 11.3 / Validated reference requirement / planning-audit bullet

**Expected occurrence:** 1

**OLD**

````text
must never appear in Codex or IA implementation prompts
````

**NEW**

````text
must never appear in prompts given to the executing agent or IA implementation prompts
````

## Redline RL-28

**Operation:** REPLACE

**Original-bound heading path:** # **12\. Change control** → ## **12.2 Supersession rule (PF10 addenda)**

**Location within that path:** 12.2 Supersession rule / current citation instruction

**Expected occurrence:** 1

**OLD**

````text
* When referencing PF10 guidance in PF19 or in a Live QA plan, cite PF10 by addendum number plus addendum title (stable unit), not by brittle subsection/paragraph anchors.  
````

**NEW**

````text
* In PF19, name HDE-Build Notes by title only, without its addendum number, section, heading, paragraph, version or other internal locator. Search its current content by topic and applicable scope rather than resolving a historical locator by number. Historical records retain their original wording and provenance.  
````

## Redline RL-29

**Operation:** INSERT

**Original-bound heading path:** # **13\. Change QA History** → ## **13.19 HDE-CRD-0001 — Accepted QA and closed-change record**

**Location within that path:** 13 Change QA History / new 13.20 after complete 13.19, immediately before H1 14

**Expected occurrence:** 1

**BEFORE**

````text
r atomicity or all-metadata guarantees. Historical readiness v1.0, the cancelled QA-15 attempt and later integrated readiness v1.1 retain their own identities; cancellation did not consume a QA retry. Current obligations are owned by §§3.1, 4.4.5, 9.2.15.5–9.2.15.8, 10.6 and 10.8, with technical mechanics and schemas routed to their single homes.


````

**AFTER**

````text
# **14\. Codespaces QA environments (environment details)**

````

**INSERT**

````text
## **13.20 HDE-EPIC040 — Gate-based mechanics, actual QA lineage and exceptional closure**

**H — Supplied historical evidence.** HDE-Build Notes, the approved `HDE-EPIC040-specification-v1.1-approved.md` and complete `HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` supply this event record. It attributes their actual decisions and proof limits; it is no new QA run, code/security review, deployment observation, PF09 action or closure decision. The Specification selected HDE-SEPA005 and its five subtasks; the other twenty-nine units remained Done/context exclusions. C040-04’s historical PF19 filename/body discrepancy is resolved and is not reopened.

### **Implementation, admission and external proof**

The recorded delivered chain comprises nine accepted, merged PR units: PR01 #403, PR02 #404, PR03 #405, PR04 #467, PR05 #492, PR06 #501, PR06a #508, PR06b #513 and documentation-only PR07 #518. OPS01 is separately PASS/ACCEPT and DOC-20 COMPLETE. These records do not substitute for independent QA or transfer a past CI result to another candidate.

PR04’s qualified acceptance preserved F03 (unserved production route), F05 (v1 schema mismatch), F07 (two evidence-test failures) and the security-review limitation. The explicit non-admitted CI outcome was never PASS or an attestation success. PR05’s real-root golden comparison refused the incomplete roster; its positive comparator and readiness tests used labelled synthetic/offline inputs. PR06 ended the interval by admitting 44 members as `1.1.0` and comparing all eight goldens against the actual candidate. PR06a delivered Reader v2, the production POST route, v1 harmony identities and dev-conjunction capture in the 45-member `1.2.0` release. PR06b aligned the v1 error schema to the unchanged emitted four-key envelope and re-cut 45-member `1.3.0`, release ID `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.

The frozen canonical-JSON captures retained digest-verified capture-time identity; current service identity and release attestation were separate. OPS01’s external attestation bound source `6f53d828a30101bb7cd6638f3695eb82c2b10979`. Supplemental candidate `6e4b3a109c0fe270cbbf51c033e63aa460792002` exercised adverse A-5, A-6 and A-7 and refused each as required; it made no vendor or database call. Those are distinct source and proof identities, not a fresh attestation or QA rerun.

### **QA Plan and execution of record**

The rejected/revoked approvals and Plan v1.0/v1.1 remain history. The resumed immutable QA Plan v1.2 was approved by review v1.4; collection v1.0 and its `06b04a9` evidence were not carried forward. Collection v1.1 supplied T01–T10, v1.3 supplied T11 (v1.2 was never executed), and v1.4 supplied T12. Execution results v1.1 superseded v1.0 for T01–T10; T11 and T12 each retained their own v1.0 result and review. Every final member was ACCEPT with per-task PASS; the later QA-120 Report v1.0 issued whole-change PASS with a separate RCA v1.0.

The actually tested source was `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`. Run B stored T01–T10 at `345148b7fce2482349828f897abbc0d7d12fe7fa`, T11 at `380cf46fda95686ccf71f256521e63ca0eb5c9e1`, and the completed stream at `787bb97b58b638d6b307cad6d76484c883c58aec`, on `qa/hde-epic040-qa100-plan-v1.2-run-20260929`. It used the Product Owner-controlled Linux shell, Python 3.12.3, one checkout, QA root and manifest; venue-specific claim was NOT CLAIMED. All checks except T11 used closed rails; T11 alone used `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev` and synthetic birth tuples, then restored closed posture. Determinism pins were `LC_ALL=C`, `LANG=C`, `TZ=UTC` throughout.

| Task / check | Accepted result and proof class | Material limits |
| :---- | :---- | :---- |
| T01 `d0-discovery` | PASS; collected 2,092 tests, explained the two-case difference, admitted the recorded 45-member `1.3.0` bundle and captured identity. | Discovery/identity, not an additional full test run or deployment proof. |
| T02 `step-0b-doc-delta-capture` | PASS; identical doc-delta surfaces with DD-01–DD-12, no blockers and explicit caveats. | Documentation capture, not performed permanent drainage. |
| T03 `ac040-08-evidence-validators` | PASS; nine read-only validators, group G 587 passed, governed-graph digest unchanged. | Run A left no T03 trace; its outcome and T03’s attempt label remain unknown. |
| T04 `ac040-02-03-catalog-config` | PASS; group A 304 passed, complete 36-row catalog and 20-signal/10-category configuration structure. | Local/offline proof; structural review and tests have separate coverage. |
| T05 `ac040-04-05-admission-identity` | PASS; group B 371 passed, manifest/release recompute and accepted OPS01 corroboration. | QA did not rebuild the external attestation. |
| T06 `ac040-06-golden-comparison` | PASS; group C 153 passed, eight matches, byte-identical repeated comparison, deliberate one-leaf mismatch reported, tree unchanged. | Actual repository root only; no other candidate root certified. |
| T07 `ac040-07-gate-ingress-offline` | PASS; group D 191 passed, empty/invalid/unavailable readiness refusals through the real entrypoint. | Offline/fake-DB capability; no live current-row observation. |
| T08 `ac040-04-09-compat-cli-offline` | PASS; group E 144 passed and three closed-rails vendor skips. | Skips supply no vendor coverage. |
| T09 `ac040-09-reader-http-in-process` | PASS; group F 339 passed, injected-row Reader v1/v2 success, eligibility, refusal, transport, schemas and dev-route production gating. | In-process success, not live DB or deployed-service success. |
| T10 `sec-reader-http-live` | PASS; 22 loopback HTTP probes, governed refusals/method guards, bounded request read, no secret/stack/Gate/numeric leakage and server shutdown. | No successful live DB Reader response. The known HTML 404 was observed; behavior-level security QA is not code security review. |
| T11 `open-rails-showcompat-vendor` | PASS; two live vendor CLI invocations, AB/BA byte identity of complete internal results and numeric-free harmony-only Reader v1 dumps, bound to the admitted release. | Exact vendor resource path, auth-header family and adapter status were inferred, not exercised in captured stderr. No retry/rate-limit/error-map, persistence, Reader v2 HTTP or deployed-service proof. |
| T12 `qa-closeout-deliverables` | PASS; final 12-entry manifest, logs/supplementary integrity, DD-13 append, 15 path proofs, governed checks and complete coverage accounting. | No product-behavior claim, close pack or Index/Mirror registration by this check. |

LR-01 retained both stored executions. Run A at `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c` was the earlier Codespaces record; it had eight primary logs, T10 probes without a receipt/manifest entry, no T03 trace, four logs without OUTPUT, and no QA execution result. Run B was the evidence of record for all ten checks because it was the later complete single stream, independently of outcome; recorded results agreed. T01, T02 and T04–T10 had two executions, with Run A first. Run B’s second executions lacked the required QA-110 attempt-2 decision and consumed the ordinary rerun allowance as a process deviation. T03 had one recorded execution and an unknown attempt label; a discovered non-PASS Run A T03 would require focused review. Run A remains preserved and non-canonical, never merged as the current QA root. T11/T12 were attempt 1. No Moon Loop or authorized QA rerun was reported.

C040-09 adopted attribution-only read-only git observation and tracked/tested harness APIs through `python -c`, not a newly written decisive evaluator; the earlier proposal/review was rejected and remained history. T12’s intermediate runner was an accepted recording deviation (K-07): actual commands and predicates were unchanged, its path/role were not recorded, and no proof was reconstructed. C040-10 recorded the Product Owner’s directed-agent authority for T11 and environment-held two-key/base-URL configuration. Accurate executor provenance and the accepted deviation remained distinct from three historical fixed-text lines that named the Product Owner. Neither interface granted new approval or general external-call authority.

### **Later evidence landing and controlling closure**

At the QA-120 capture the evidence was on Run B, absent from main and unregistered (QA50-F01); those dated observations are not the final state. Closure v1.2 records #559 landing 39 QA-root files byte-identical to `787bb97` and registering 14 files—the manifest, 12 primary logs and doc-delta file—through the evidence owner. Index/Mirror rows rose from 606 to 620, the manifest lookup held, and QA50-F01 plus evidence-not-on-main were resolved. Supplementary files and the QA-root doc-delta copy landed without registration. #559’s exact-head CI passed at `95ab9bf`, with tree identity to landed `74f6cc96`. That index work was not another QA run; later storage/merge commits were not the source tested by the QA Plan.

The controlling decision is Isis’s `CLOSE / CHANGE_CLOSED` at `2026-09-29T19:53:33Z`, closure decision v1.2, superseding v1.1 DO_NOT_CLOSE and the earlier v1.0 decision/void handoff. The Product Owner authorized exceptional closure under Change Process Guide; ordinary Close Gate completion was not established. CLOSE01 stopped on a close-report writer capability gap and no admitted post-verdict evidence home. No close report, close manifest, close-pack path proofs, drain-targets ledger, governed RCA placement, close-report SATISFIED decision or same-run close-workflow evidence was produced. Acceptance map/token matrix were neither present nor required. This exception applied only to EPIC040; it created no reusable default and authorized no future work.

Two live parts remained unsupported because the pre-App environment lacked actual user-bound data: read-only Gate readiness on current rows and successful Reader v1/v2 HTTP against live DB rows. They were deferred requirements, not failed or passing executed checks. No deployed service, live database, production posture, activation or deployment was proven. Q-1’s bounded behavior security checks and Q-2’s live synthetic vendor check were satisfied; PR04/PR05/PR06/PR06a code-security coverage limits were not retrospectively filled. Wheel admission, HTML 404, baseline out-of-lane CLI/test failures, help/ignored-flag and APP_ENV asymmetry, evidence-origin labels, `--allow-prod-vendor`, `.env.example` missing `GEO_API_KEY` and actual environment configuration remained with their recorded owners.

The later-drain recommendation supported .1–.4 as Done and .5 as Partial, with the parent remaining Partial; no PF09 status moved. After #559, .5 retained one stated condition: the live current-row observation still needed re-homing by the PF09 owner; the alternative reading remained that owner’s decision. DD-03 identified the superseded Library/Drive source/storage wording addressed in §§0.2, 0.4.3, 3.4.3, 3.6, 10.8 and 11.3. Other DD items, board/memo administration, canon drainage and ordinary close-pack completion were separate acts, not facts established by this history.

**L — Reusable learning, not new MUSTs.** The actual planning failures concerned unread governing canon and a rereview limited to redlines instead of the whole Plan. K-01–K-07 concern real recorder argv, command presentation, duplicate-execution guards, real-command dry runs, base URL versus keys, executor identity and intermediate-file disclosure. Recorded operator corrections did not change proof identity; Run A’s missing T03/T10 causes retain their unknown/inferred limits. PF19D-001–004, OPFD-001/002 and closure CC-1/2/3/5/6 remained proposals or unresolved maintenance decisions, not approvals. This entry creates no new mandatory guard, captured-identity field, evidence home, close-workflow writer, rails interpretation, QA task or acceptance predicate from those lessons. Current rules remain at their existing owners; product and code/security proof limits remain visible.


````

## Redline RL-30

**Operation:** REPLACE

**Original-bound heading path:** # **5\. Component playbooks (how to run QA per surface)** → ## **5.4 App Frontend**

**Location within that path:** 5.4 App Frontend / opening paragraph

**Expected occurrence:** 1

**OLD**

````text
App-specific; this playbook is a names-only placeholder. The FE team fills in concrete tools, routes, and thresholds.
````

**NEW**

````text
App-specific; this names-only playbook leaves concrete tools, routes and thresholds to the owning FE change. PF19 does not establish their implementation or availability.
````

END OF REDLINES
