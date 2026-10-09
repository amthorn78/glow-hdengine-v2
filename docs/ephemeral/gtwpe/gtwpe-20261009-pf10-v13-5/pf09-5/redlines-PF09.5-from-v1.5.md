# Redlines for PF09.5 from v1.5

Run: `gtwpe-20261009-pf10-v13-5/T-PF09-5`. Preparation revision: 1. Originating preparer: the Nathan-started Codex document session executing T-PF09-5 (runtime `/root`, workspace `/workspace/scratch/0aa6525fa090`); no separate author or reviewer session. Its conversation URL is not exposed by this runtime.

Prompt: TW-DRAIN-20 100926.1, https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862.

Original: `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.5.md`, native v1.5, at main `e7265a090ad0cc8de5f36de2f19481216aa3d073`. UTF-8 raw-byte SHA-256: `115655849b5550f7ce1be6a2a9725f9a72a75a2db395bee5f44dae212672a881`. Full original: 194,959 bytes, 2,912 LF-terminated lines; one phase file.

Selected change sources at `e7265a090ad0cc8de5f36de2f19481216aa3d073`: `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md`, complete A33 (3181–3238), A34 (3239–3306), A35 (3307–3444), A37 (3607–3847); complete C1, `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` (1–190). Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md`, pinned `f057d124176143b3e02ba7ad599880fd7e9991b1`, row T-PF09-5. PF03 and topic-owner reads are supporting controls, not change sources.

Preparation outcome: READY. Save completeness and validation receipts are in `redlines-PF09.5-from-v1.5.proof-log.md`; READY alone is not a final PF.

Each operation resolves independently against the unchanged original. The five-backtick fences contain exact UTF-8 payloads, including each final LF before the closing fence and meaningful trailing spaces. Heading paths below are verbatim original headings; field names locate native fields within them. Header document-control fields are reserved for Apply: native v1.5/date/Last Update Gate schema and source provenance are recorded in the proof log. No content operation overlaps those fields.

## Redline RL-001

Classification: Phase Master Update — QA qualification; no status transition

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`

Native field: `**Phase notes:**`

Operation: REPLACE
Expected occurrence count: 1

Basis: A33 Rule 1–5, Epic/task/status effects and Scope boundaries; A34 retained controls. The existing phase Done statement remains bounded to its recorded Fermentation work.

Exact OLD block:

`````markdown
* Non-dry-run mapped-cache writes remain guarded until a later mapped-cache persistence slice proves safe persistence. HDE-EPIC037 proves dry-run mapping and compat computation for the scoped chain; it does not prove durable configured-v2 mapped-cache write/read-back parity or production upsert reopening.
`````

Complete NEW block:

`````markdown
* Non-dry-run mapped-cache writes remain guarded until a later mapped-cache persistence slice proves safe persistence. HDE-EPIC037 proves dry-run mapping and compat computation for the scoped chain; it does not prove durable configured-v2 mapped-cache write/read-back parity or production upsert reopening.  
* Production-functional QA minimum: every QA plan for an epic touching a surface used to produce a production feature described as functional in PF-Canon must include a live vendor call under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, using synthetic data only. A plan without that test is not approval-ready. Closed-rails tests, replay, mocks, static or generated evidence, index or mirror work, review, an unrun procedure, and OPS discovery without a live vendor call cannot substitute; a deployed-service check or database read alone is also insufficient. Product Owner authorization, the defined request limit, secret-safe evidence, redaction, and failure classification remain required. OPS smoke remains OPS evidence unless the governing QA plan separately defines how it feeds QA evaluation. The requirement creates no load or volume authority and changes no phase or row status by itself. The controlling rule is in **PF10-HDE-Build-Notes**; QA procedure remains owned by **PF19-Canon-Glow-QA-Guide**.
`````

## Redline RL-002

Classification: Notes Update — execution ownership and environment configuration

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`
- `## **Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence**`

Native field: `Task notes:`

Operation: REPLACE
Expected occurrence count: 1

Basis: A34 Rule 1–7 and scope/nonclaims explicitly supersede the parent execution bar; A33 retains synthetic-only, bounded, secret-safe open rails. Environment-template correction and actual provisioning remain outside this documentation task.

Exact OLD block:

`````markdown
* This task includes OPS work because open-rails vendor calls require secrets and privileged runtime posture. Automated agents must not execute vendor calls or claim completion without PO-run evidence. The open-rails path is vendor-only for HumanDesignAPI; it must not include OpenAI, LLM, AI-agent, or other AI-provider calls.  
`````

Complete NEW block:

`````markdown
* This task includes OPS work because open-rails vendor calls require secrets and privileged runtime posture. "PO-only" identifies the Product Owner as the authorizing and accountable principal. For an identified task, a Product Owner-directed agent may execute the live vendor commands and produce evidence; it is not an independent approver. The executor must retain the exact commands, scope, rails, request limit, stop checks, synthetic inputs, secret scan and quarantine, redaction, and evidence contract. No completion is claimed without the required evidence. This creates no standing vendor-call authority. The open-rails path is vendor-only for HumanDesignAPI; it must not include OpenAI, LLM, AI-agent, or other AI-provider calls.  
* Vendor configuration comes from the execution environment: two API keys, `HD_API_KEY` and `GEO_API_KEY`, plus the base URL in `HD_API_BASE_URL`. The base URL is configuration, not an API key. `HDAPI_BASE_URL` is a compatibility fallback only when `HD_API_BASE_URL` is absent; differing values when both are set fail closed. Use the environment without asking the Product Owner to type, paste, or re-enter values, and do not remove the environment's only base URL merely to establish rails. Record presence only as `SET` or `UNSET`; keep values out of conversations, logs, stored evidence, commits, and process argument lists, and scan captured output before admitting it to evidence. Passing the environment to the product process is not handling plaintext secrets. If required configuration is absent, run no vendor call, record the missing names by presence only, and classify a begun step as `TOOLING_BLOCKED`; manual value entry is not a substitute. The controlling rule is in **PF10-HDE-Build-Notes**; CLI and configuration contracts remain owned by **PF05-Canon-HDE-CLI-API-Vendor-Ref** and **PF07-Canon-Glow-Infrastructure**.  
`````

## Redline RL-003

Classification: Evidence Update and Epic-information Update — separately attributed T11 and closure

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`
- `## **Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence**`

Native field: `Task notes:`

Operation: REPLACE
Expected occurrence count: 1

Basis: A35 Approval/source, Retained decisions, K-06 and nonclaims; A37 Q-2, environments/currentness, deferred live requirements and final QA verdict; C1 §§0–4, 6 and 8 supplies actual exceptional closure and supersedes A37’s then-open evidence landing/QA50-F01 state. It supplies no new Fermentation delivery assignment.

Exact OLD block:

`````markdown
* Epic or card: HDE-EPIC034, HDE-EPIC035, HDE-EPIC036, and HDE-EPIC037.
`````

Complete NEW block:

`````markdown
* Supporting vendor-behavior history from HDE-EPIC040, Separation Pass 3: QA Plan v1.2 check 11, T11 attempt 1, was executed on 2026-09-29 by the QA-100 session as the Product Owner's directed agent and accepted by QA-110 with per-task result PASS. At tested source `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`, two CLI invocations using synthetic birth tuples (AB and BA) under `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and `APP_ENV=dev` exercised live vendor-backed resolution, compatibility evaluation through the admitted release, canonical `magic10_compat_result.v1` stdout, and a numeric-free bands-only Reader v1 dump; the AB and BA captures were byte-identical. Original capture commit: `380cf46fda95686ccf71f256521e63ca0eb5c9e1` on `qa/hde-epic040-qa100-plan-v1.2-run-20260929`. The six check-scoped artifacts are `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`, `vendor_request.txt`, `vendor_run_ab.json`, `vendor_run_ba.json`, `reader_v1_ab.json`, and `reader_v1_ba.json`, with the latter five in that same directory. These are supplied historical QA facts recorded by **PF10-HDE-Build-Notes**.  
* T11 proves only its exercised CLI behavior. With empty stderr, the exact vendor resource path, auth-header family, and adapter status were inferred, not exercised. T11 did not exercise rate-limit or Retry-After handling, typed vendor error mapping, malformed responses, the v1 legacy guard, mapped-cache persistence, Reader v2 over HTTP, a deployed service, or live DB/current-row behavior. Three fixed-text capture lines still name the Product Owner as executor; the command provenance and execution deviation identify the directed QA-100 agent. The historical governed bytes remain unchanged. T11 alone establishes no whole-change QA verdict, broad vendor conformance, HDE-FERM008 completion, or Fermentation phase exit.  
* The later HDE-EPIC040 QA-120 report records PASS for all 12 approved Plan v1.2 checks at the same tested source; its final Run B evidence commit is `787bb97b58b638d6b307cad6d76484c883c58aec`. `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` records that #559 landed the QA evidence byte-identically and resolved QA50-F01 through Index and Mirror registration. It records Isis's `CLOSE` / `CHANGE_CLOSED` decision at 2026-09-29T19:53:33Z under the Product Owner's exceptional-closure authorization. Ordinary Close Gate completion, a close pack, token satisfaction, deployment, activation, board movement, and phase exit were not established. Live read-only Gate readiness against current rows and live DB Reader v1/v2 success over live HTTP remain blocked by the pre-App environment and await separately approved future user-bound scope; no fake production users, new Fermentation row, ID, or completion is inferred. HDE-SEPA005.5's remaining re-homing condition belongs to **PF09.3-Canon-HDE-Build-Checklist-Separation**. These later records preserve the existing bounded HDE-FERM008 Done posture and its HDE-EPIC034 through HDE-EPIC037 assignment.  
* Epic or card: HDE-EPIC034, HDE-EPIC035, HDE-EPIC036, and HDE-EPIC037.
`````

## Redline RL-004

Classification: Clarity Fix — directed execution in the existing smoke description

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`
- `## **Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence**`
- `### **Subtask HDE-FERM008.2 \- Execute PO-only open-rails v2 smoke**`

Native field: `Subtask description:`

Operation: REPLACE
Expected occurrence count: 1

Basis: A34 Rule 1–7 corrects the physical-executor restriction without changing the original evidence contract, Owner: PO, Facilitator: IA or recorded OPS-02 result; A33 preserves synthetic-only input.

Exact OLD block:

`````markdown
Run a controlled PO-executed open-rails vendor smoke against the v2 vendor path. The run must capture command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, and file checksums. It must not persist plaintext secrets or vendor payload bodies beyond the approved evidence shape.
`````

Complete NEW block:

`````markdown
Run a controlled Product Owner-authorized open-rails vendor smoke against the v2 vendor path, executed by the Product Owner or an agent directed for this identified task. Use the environment-held vendor configuration and retain the exact commands, scoped rails, request limit, stop checks, synthetic inputs, secret scan and quarantine, and redaction. The run must capture command transcript, stdout, stderr, exit code, redacted/presence-only secret posture, request summary, result summary, and file checksums. It must not persist plaintext secrets or vendor payload bodies beyond the approved evidence shape.
`````

## Redline RL-005

Classification: Notes Update — remove the directed-agent bar

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`
- `## **Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence**`
- `### **Subtask HDE-FERM008.2 \- Execute PO-only open-rails v2 smoke**`

Native field: `Notes:`

Operation: REPLACE
Expected occurrence count: 1

Basis: A34 Rule 2–3 and the explicit Fermentation .2 superseded-passage entry require removal of the execution ban, while the original approval, evidence and HDAPI-only boundaries remain.

Exact OLD block:

`````markdown
This subtask remains PO-only for live vendor execution. Development agents may specify intent, constraints, success criteria, evidence requirements, and rollback intent, but must not execute vendor calls or claim live-vendor completion without PO-run evidence. The executed smoke is HDAPI-only; no OpenAI or other AI-provider call is in scope.
`````

Complete NEW block:

`````markdown
This subtask remains PO-only for authorization and accountability, with IA facilitation. A Product Owner-directed agent may execute the live vendor commands for this identified task and produce the required evidence under the same controls as a human executor; it does not approve its own run or gain standing authority. "PO-run evidence" includes evidence from such a directed run. Development agents may specify intent, constraints, success criteria, evidence requirements, and rollback intent, and must not claim live-vendor completion without the required evidence. The executed smoke is HDAPI-only; no OpenAI or other AI-provider call is in scope.
`````

## Redline RL-006

Classification: Clarity Fix — conform the related existing runtime-smoke authority

Target document: PF09.5-Canon-HDE-Build-Checklist-Fermentation

Exact original heading path:

- `# **Phase V — Fermentation (Narratives & external bridges)**`
- `## **Task HDE-FERM008 \- HDAPI v2 live conformance, rails, and evidence**`
- `### **Subtask HDE-FERM008.11 \- Execute PO-only open-rails v2 BodyGraph-detail runtime smoke**`

Native field: `Notes:`

Operation: REPLACE
Expected occurrence count: 1

Basis: A34 Rule 1 applies to every HDE live vendor call, including this existing OPS smoke. The physical-executor-only wording would contradict that rule after the parent/.2 correction. No new subtask, rerun, approval or historical executor alteration is introduced; all remaining PR/OPS and scope nonclaims are preserved verbatim.

Exact OLD block:

`````markdown
This subtask is OPS work and remains PO-executed. PR work may bind the already-produced evidence but must not claim it executed the live smoke. This subtask does not claim QA PASS, OPS completion by PR work, PF09 status movement by PR work, HDE-FERM008 parent Done by itself, epic closeout, production deployment, broad HumanDesignAPI v2 platform conformance, public Reader expansion, new public route, app-side vendor credential ownership, raw vendor payload persistence, or AI scope.
`````

Complete NEW block:

`````markdown
This subtask is OPS work under Product Owner authorization and accountability. The Product Owner or an agent directed for this identified task executes its live vendor commands under the same controls and evidence contract. PR work may bind the already-produced evidence but must not claim it executed the live smoke. This subtask does not claim QA PASS, OPS completion by PR work, PF09 status movement by PR work, HDE-FERM008 parent Done by itself, epic closeout, production deployment, broad HumanDesignAPI v2 platform conformance, public Reader expansion, new public route, app-side vendor credential ownership, raw vendor payload persistence, or AI scope.
`````

END OF REDLINES
