---
artifact_type: PROMPT_ECOSYSTEM_OPERATING_PROCEDURE
artifact_version: "1.0"
created_date: 2026-09-27
status: CURRENT
authority: Product Owner instruction, 2026-09-27 (bring the Drive operating procedures into the repository and extract what is still live, carefully)
sources: archive/prompt-selection-and-session-delegation-protocol-v1.14.0.md; archive/general-prompt-flow-and-creation-guidelines-v1.12.1.md
---

# Operating rules carried forward from the Drive-era procedures

This page holds the rules from the two archived Drive procedures (see `archive/`) that are still valid and that no current authority states.

**It is subordinate to every current source.** Those are PF-Canon on `main` (with PF10, which governs where it speaks), the decision record, `AGENTS.md`, the graph contracts and the other procedures in this directory. If any of them conflicts with a rule here, it governs and the rule here is the defect to correct. Nothing here re-adopts content from the archived files beyond the rules listed.

## Canon relied on

* **PF-Canon on `main`:**
  * PF10 precedence rules and addendum 2.8 (PF10-FORM-001);
  * HDE Governance §9.1.5 and §9.1.6;
  * Glow QA Guide §9.2.15.5.
* **Decision record:** D1–D9 and D11–D26, including the D23 successors.
* **Graph contracts:** `docs/graph/parts/global.json` (`handoff_contract`, `canonical_source_contract`, `pf10_addendum_contract`, `terminal_contract`) and the 55 prompt parts.
* **This directory:** `README.md`, `authoritative-surfaces.md`, `execution-and-delegation-model.md`, `session-working-rules.md`, `prompt-body-content-policy.md`, `prompt-corpus-policy.md`, `notion-write-boundary.md`, `ecosystem-change-management.md`.
* **Also read:** `docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md` and `AGENTS.md`.

## How the rules were selected

Each archived document was read in full, rule by rule, by an independent reviewer: 544 lines and 789 lines. Every rule was checked against the sources above and classified as one of:
* superseded;
* covered elsewhere;
* specific to an old release;
* still live and uncovered;
* uncertain.

About 70% was superseded or specific to an old release. That includes the retired Analyzer (GCFPE-ASSESS-10), ChatGPT model and launch-line guidance, Drive and Library storage, and the 51- and 53-member rosters. A rule is carried here only if one reviewer found it live and uncovered and the other found no current source covering it. Rules the reviewers disagreed on, or could not settle without reading Notion prompt bodies, are listed as pending and are **not** adopted.

## Rules

### R1. Human Design mechanics research order

For a Human Design mechanics question, read PF08 and PF11 in `docs/pfcanon/` first. If they are inconclusive, retrieve the actual admitted original reference passages the claim needs. An index is not doctrinal evidence. If bounded external inquiry is needed, use only jovianarchive.com. An inaccessible original is an access limitation, not evidence that the doctrine is absent. If the question is still unresolved, give the Product Owner the exact question, the alternatives, the evidence inspected and the practical consequences.

*Source:* Protocol L41 and Guidelines L55; both reviewers classified it live. *Scope (Product Owner ruling, 2026-09-27):* the "HD Refs" originals remain authoritative in some contexts, but no development work needs them, so no repository home is created. The step "retrieve the original passages" applies outside development work only.

### R2. Engineering research order

For an engineering question, inspect current canon and the actual repository interfaces and files first. Only then use bounded primary technical sources.

*Source:* Protocol L42. The Analyzer hop in the original is dropped as superseded. The IA-60 research lane is unchanged.

### R3. One writer per output

Do not start a second writer for the same transaction, run identity or output namespace.

*Source:* Protocol L397. It is compatible with `execution-and-delegation-model.md` §5, which says parallel agents write nothing.

### R4. Corrections apply prospectively

A change to an operating rule applies to invocations started after it. Do not cancel or reissue work already running merely to retrofit a new rule, unless the Product Owner directs it.

*Source:* Protocol L403 and L330.

### R5. Rejected prompts

A prompt the Product Owner has rejected is not eligible for launch, reuse, repair or presentation as a current option. Do not revise or recreate it unless the Product Owner later instructs it. Retiring it follows the archive rule (D17: a move, never a copy or a deletion).

*Source:* Protocol L407 and L409, and Guidelines L606–L618. Both reviewers found no current statement of it.

## Pending — not adopted, needs a Product Owner ruling or a Notion body check

| # | Candidate | Why it is not adopted |
| :---- | :---- | :---- |
| P2 | Review standard: judge the artifact as a competent reader would act on it; no approval on an unsupported decisive claim | One reviewer found it uncovered; the other thought it may live in the CF-E-30, CF-C-30 and IA-30 prompt bodies |
| P3 | ADR disposition triad: APPROVED / APPROVED_AS_CHANGED / REJECTED; being included in a Plan is not approval | The vocabulary is in live use and D9 protects it, but it may already be in the prompt bodies |
| P4 | PR-10 semantic-readiness checks before INSTRUCTION_READY; session-reinitialization rules; IA-30 correction intake; CL-40 scan detail; ordered-PR merge dependency | Can only be settled by reading the Notion prompt bodies and graph parts |
| P6 | Who writes to the Notion Prompt and Session Control Error Log | No destination rule names it (`notion-write-boundary.md`) |
| P7 | Technical Writing (TW) flow rules | TW is outside the current ecosystem scope (D23 successor) |

## Product Owner rulings, 2026-09-27

These settle former pending items. They change no PF canon: the passages that disagree stay as written until the Product Owner directs a change to them.

| Former item | Ruling | Effect |
| :---- | :---- | :---- |
| P1, home for the "HD Refs" originals | They remain authoritative in some contexts, but nothing development-related needs them | No repository home is created; R1 is scoped accordingly |
| P5, monthly model-advice review of prompt headers | It does not survive; no header review is needed | The graph `handoff_contract` governs; the review in HDE Governance §9.1.6 is not performed. That passage is a candidate drain target |
| Who assigns PF10 addendum numbers | An agent that authors a PF10 addendum during a prompt-governed cycle assigns its number | PF10 addendum 2.8 stands. The graph `pf10_addendum_contract` rule that producers never assign numbers conflicts with it, and that contract is the candidate for correction |
| Whether addendum 2.28 needs a D4 update | Not a matter for agents to govern | No action |
