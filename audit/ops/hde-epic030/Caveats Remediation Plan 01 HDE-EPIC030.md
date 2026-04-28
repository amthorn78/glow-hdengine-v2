Artifact Map

Remediation Plan Under Review: r2 Remediation Plan 01 HDE-EPIC030.md

Output: Remediation Plan Approval Review (Thoth)

Review Summary

* The Plan is canon-aligned on the core po-006 correction: public numeric-free proof, internal/admin compat compute proof, and vendor-backed no-user behavior proof are separated.
* DEV/PR and OPS readiness is acceptable: the executable remediation plan is now PR + OPS only, with QAP/DOC drainage explicitly outside execution scope.
* ADR posture is approval-ready: ADR-001 and ADR-002 are execution-critical and APPROVED for the Plan’s remediation sequence.
* Portability posture is acceptable: execution relies on embedded observed evidence and the Plan’s own PR/OPS instructions, not on opening non-PF attachments.
* OPS posture is bounded and safe: OPS work is PO-only, IA-facilitated, secret-redacted, PF07-gated where runtime target facts matter, and evidence-bound.
* Caveats are non-blocking because each has an owner, evidence trigger, safe default, and no canon contradiction or portability violation.
* Final decision: ASK OK WITH CAVEATS.

Review Ledger

1. RL-001 | Category: Canon

Plan anchor (verbatim 5–25 words): "Self-contained observed evidence in this Plan."

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan embeds the execution-relevant non-PF findings and does not require executors to open non-PF inputs outside the Plan.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: This satisfies portability and prevents hidden attachment dependencies.

Exact expected fix instruction: NA

PF support: PF27 — Canon Plan Templates, §Purpose & scope [Required−Now]

PF proof excerpt:

"A remediation guide MAY include a short “Evidence inventory reviewed (non-PF)” list for provenance, but it MUST NOT require the executor to open external files to execute the plan."

"If any non-PF fact is required to execute downstream steps ... the guide MUST embed that fact directly in the document inside “Observed Evidence Snapshot” as a short quote or precise paraphrase."

"Any Artifact Map (or equivalent) MUST explicitly label non-PF inputs as: `provenance only; not required to execute`."

2. RL-002 | Category: Canon

Plan anchor (verbatim 5–25 words): "The executable remediation task plan below contains only PR and OPS work items."

Plan anchor (secondary, if needed): "Documentation drainage does not substitute for PR or OPS remediation"

Item summary: The Plan correctly removes QA_PLAN_UPDATE and DOC_UPDATE from the executable remediation task plan and treats documentation drainage as non-execution follow-up.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Documentation drainage cannot be used as an implementation deliverable, acceptance condition, or closure blocker.

Exact expected fix instruction: NA

PF support: PF06 — Epic-Process-Guide, §0.2 Policy and principles

PF proof excerpt:

"Documentation drainage is never an execution or closeout gate."

"PF10 drain and any later drainage ... are never prerequisites, required deliverables, required checks, acceptance conditions, or blockers by themselves"

"Allowed blockers remain limited to real truth-and-proof failures"

3. RL-003 | Category: Canon

Plan anchor (verbatim 5–25 words): "Direct compute tests, public Reader output, and internal/admin compat output must remain separate proof classes."

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan correctly separates public numeric-free proof from internal/admin compatibility compute proof.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: po-006 cannot be remediated by treating an internal/admin numeric payload as public proof.

Exact expected fix instruction: NA

PF support: PF04 — HDE-Governance, §2.0.11 Catalog hygiene (where applicable)

PF proof excerpt:

"RESONANCE_PUBLIC_POSTURE_OK — Reader v1 and CLI **public** surfaces obey the **numeric-free, narrative-free public covenant**"

"This token covers CLI output only when the CLI is emitting the **Reader v1 success envelope**"

"This token does **not** govern `hdctl showcompat` stdout (the compatibility payload), which may include numeric scores/weights."

4. RL-004 | Category: Canon

Plan anchor (verbatim 5–25 words): "live compatibility behavior proof must not depend on app user IDs or DB-backed user BodyGraphs"

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan correctly treats vendor-backed birth/no-user behavior as the live proof class for the current pre-App environment.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Live no-user behavior proof must not be replaced by app-user IDs, DB-backed BodyGraphs, or synthetic `person_uid` injection.

Exact expected fix instruction: NA

PF support: PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode

PF proof excerpt:

"For live behavior tests in this environment (including PO Live QA and any D-goals that assert “live compat behavior in prod”), use `hdctl showcompat` with:"

"birth arguments only"

"an explicit vendor source flag, for example `showcompat --source=vendor`"

5. RL-005 | Category: Canon

Plan anchor (verbatim 5–25 words): "Governed evidence must remain under governed roots with coherent index/mirror/path-proof posture"

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan correctly preserves governed evidence root and index/mirror/path-proof discipline for promoted evidence.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: OPS or PR evidence cannot become acceptance-grade unless governed evidence bindings remain coherent.

Exact expected fix instruction: NA

PF support: PF12 — HDE Schemas & Artifacts, §Machine Evidence Mirror (governed here)

PF proof excerpt:

"Path: artifacts/evidence_index.jsonl"

"Each record MUST include fields sufficient for proof and reproducibility"

"Path-proofs are stored alongside each artifact; proof_anchor must point to the matching transcript."

6. RL-006 | Category: ADR

Plan anchor (verbatim 5–25 words): "Approve a corrected po-006 authority model: public numeric-free output proof"

Plan anchor (secondary, if needed): "Title: po-006 no-user compatibility proof authority and boundary"

Item summary: ADR-001 is approved because it establishes the required proof-authority split without widening public scope.

Status: Verified

Execution-critical (ADR only): Yes

Disposition (ADR only): APPROVE

Why it matters: PR-01 and PR-02 cannot execute canon-safely without a settled no-user compatibility boundary model.

Exact expected fix instruction: NA

PF support: PF04 — HDE-Governance, §2.0.11 Catalog hygiene (where applicable)

PF proof excerpt:

"RESONANCE_PUBLIC_POSTURE_OK — Reader v1 and CLI **public** surfaces obey the **numeric-free, narrative-free public covenant**"

"This token does **not** govern `hdctl showcompat` stdout (the compatibility payload), which may include numeric scores/weights."

"This token also does **not** govern admin-only surfaces"

7. RL-007 | Category: ADR

Plan anchor (verbatim 5–25 words): "Approve a controlled PO manual vendor-backed no-user smoke after command discovery and PR remediation."

Plan anchor (secondary, if needed): "Title: Controlled vendor-backed no-user smoke for po-006 remediation"

Item summary: ADR-002 is approved because it authorizes a bounded PO-only vendor smoke only after command discovery and PR remediation.

Status: Verified

Execution-critical (ADR only): Yes

Disposition (ADR only): APPROVE

Why it matters: The real-test requirement needs a controlled vendor-backed path, but only under explicit rails, no-user inputs, and secret-safe handling.

Exact expected fix instruction: NA

PF support: PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode

PF proof excerpt:

"Until local BodyGraph storage exists, vendor-backed `showcompat` Live QA MUST run with vendor rails open"

"In all cases, do not use `--user-a/--user-b` or `--source=db` in prod QA"

"These runs are the only compat runs that count as “live behavior tests” in the pre-App environment."

8. RL-008 | Category: Task

Plan anchor (verbatim 5–25 words): "The executable remediation task plan below contains only PR and OPS work items."

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan’s work item model is valid because it contains PR and OPS tasks only, with explicit DISCOVERY/CHANGE intent and stated dependencies.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Mixed task types or unclear task sequencing would make the Plan non-executable.

Exact expected fix instruction: NA

PF support: PF09.2 — HDE Build Checklist Dissolution, §0.2 Conventions

PF proof excerpt:

"Correct task model (DEV PRs only; OPS tasks only; explicit DISCOVERY vs CHANGE; no mixed tasks)."

"Correct sequencing and explicit cross-lane dependencies."

"Concrete deliverables (lowercase paths + filenames)."

9. RL-009 | Category: Task

Plan anchor (verbatim 5–25 words): "Discover exact vendor-backed no-user command and safe execution context"

Plan anchor (secondary, if needed): "No live vendor call is authorized in this work item unless ADR-002"

Item summary: OPS-01 is executable as PO-only discovery with IA facilitation, concrete evidence outputs, secret-safe handling, and a safe TOOLING_BLOCKED default.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Vendor command discovery is privileged operational work and must not be guessed or delegated to Codex.

Exact expected fix instruction: NA

PF support: PF06 — Epic-Process-Guide, §0.2 Policy and principles

PF proof excerpt:

"Ops tasks MUST be executed by the Product Owner (human operator) only."

"Automated agents (including CodEx-driven agents) MUST NOT attempt to perform Ops tasks"

"Every Ops task record MUST include:"

10. RL-010 | Category: Task

Plan anchor (verbatim 5–25 words): "Read-only repo boundary and source-skew discovery"

Plan anchor (secondary, if needed): "Read-only only: no file edits, no tests, no vendor calls."

Item summary: PR-01 is executable as bounded read-only discovery and does not cross into OPS, QA execution, or implementation change.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Source-skew and boundary facts must be established before PR-02 changes code or tests.

Exact expected fix instruction: NA

PF support: PF27 — Canon Plan Templates, §Purpose & scope [Required−Now]

PF proof excerpt:

"Validated references only. Plans MUST NOT include any repository path, module home, command, or uniqueness claim ... that cannot be confirmed via canon or repo inspection."

"Every asserted file path or “where this lives” claim in a plan MUST be validated"

"File minting is allowed. When a plan mints new files or new evidence outputs, it MUST name the exact repository paths and filenames"

11. RL-011 | Category: Task

Plan anchor (verbatim 5–25 words): "Remediate no-user compatibility boundary and po-006 proof tests"

Plan anchor (secondary, if needed): "PR-02 must still address whether tests prove no-user behavior"

Item summary: PR-02 is executable as a sequenced PR change after PR-01 and ADR-001, with OPS-01 inputs used only as inputs and not as Codex-executed OPS work.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: The repo may appear locally green while still failing the PO’s real no-user/vendor requirement unless PR-02 explicitly proves the right seam.

Exact expected fix instruction: NA

PF support: PF09.2 — HDE Build Checklist Dissolution, §0.2 Conventions

PF proof excerpt:

"Correct task model (DEV PRs only; OPS tasks only; explicit DISCOVERY vs CHANGE; no mixed tasks)."

"Correct sequencing and explicit cross-lane dependencies."

"Concrete deliverables (lowercase paths + filenames)."

12. RL-012 | Category: Task

Plan anchor (verbatim 5–25 words): "Execute controlled vendor-backed no-user implementation smoke when PF07 target facts are proven"

Plan anchor (secondary, if needed): "The Plan does not currently prove the PF07 target facts"

Item summary: OPS-02 is executable because it is PO-only, PF07-gated, secret-safe, evidence-bound, and stops as TOOLING_BLOCKED when target facts are missing.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Runtime target binding cannot rely on guessed hostnames, ports, URLs, or deployment state.

Exact expected fix instruction: NA

PF support: PF07 — Glow Infrastructure, §0 Front Matter

PF proof excerpt:

"A document that needs a PF07-owned fact MUST either cite the exact PF07 fact directly or identify the exact missing PF07 fact set"

"Placeholder ownership and guessed values are non-conforming"

"Specificity and review posture."

13. RL-013 | Category: Task

Plan anchor (verbatim 5–25 words): "No command may rely on an unproven path, host, port, URL, or service binding."

Plan anchor (secondary, if needed): "NONE"

Item summary: The Plan’s command and runtime binding posture prevents unsafe execution by guesswork.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: A vendor smoke is only safe when its command, target, and execution context are proven before execution.

Exact expected fix instruction: NA

PF support: PF07 — Glow Infrastructure, §0 Front Matter

PF proof excerpt:

"PF07 is the single canonical inventory for currently-owned, or intentionally-missing, infrastructure facts"

"Where PF07 is silent, plans MUST NOT invent or assume infrastructure facts."

"Missing PF07 facts are blockers for the affected claim or task until added or explicitly waived by the PO."

14. RL-014 | Category: Task

Plan anchor (verbatim 5–25 words): "Do not write secret values to command files, logs, summaries, stderr, stdout, JSON"

Plan anchor (secondary, if needed): "redacted_env_presence.json must contain only key names and presence booleans."

Item summary: The Plan’s secret-handling posture is safe for OPS-01 and OPS-02.

Status: Verified

Execution-critical (ADR only): NA

Disposition (ADR only): NA

Why it matters: Vendor-backed work can expose credentials unless logs, command captures, and env snapshots are presence-only.

Exact expected fix instruction: NA

PF support: PF05 — HDE-CLI-API-Vendor-Ref, §7.3.6 Observability (keys-only)

PF proof excerpt:

"Bounded labels; never log request/response bodies or secret header values; secrets redacted."

"Acceptance to flip rails"

"Pin a concrete policy ... prove refusal on closed rails; prove conformance on open rails"

Caveats

Caveat statement: RL-009 caveat — If `hdctl showcompat --help` is unavailable or does not prove exact no-user vendor flags and input shape, OPS-01 must record TOOLING_BLOCKED and no vendor call may run.

Owner: PO

Evidence trigger: `audit/ops/hde-epic030/ops-01/showcompat_help.stderr`, `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`, and `audit/ops/hde-epic030/ops-01/discovery_summary.md`

Risk if unresolved: PR remediation may pass local checks while the PO’s real no-user/vendor behavior requirement remains unproven.

Caveat statement: RL-011 caveat — If PR-01 proves the logged po-006 evidence is stale but current tests already pass, PR-02 must still prove no-user behavior rather than only full-argument compatibility with injected `person_uid`.

Owner: Lead Dev

Evidence trigger: PR-01 source-skew report and PR-02 targeted test report.

Risk if unresolved: The repo may appear green while the public/birth-facing no-user boundary remains unproven.

Caveat statement: RL-012 caveat — If exact command proof, vendor credentials, or PF07 target facts are missing, OPS-02 must record TOOLING_BLOCKED and must not run the vendor smoke.

Owner: PO

Evidence trigger: `audit/ops/hde-epic030/ops-02/vendor_command.txt`, `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`, `audit/ops/hde-epic030/ops-02/request_summary.txt`, `audit/ops/hde-epic030/ops-02/exit_code.txt`, and `audit/ops/hde-epic030/ops-02/result_summary.md`

Risk if unresolved: The implementation may remain locally repaired but not validated against the current no-user/vendor runtime posture.

Decision

Decision: ASK OK WITH CAVEATS
