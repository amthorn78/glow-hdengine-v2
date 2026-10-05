---
artifact_type: PROMPT_ECOSYSTEM_DECISION_RECORD
artifact_version: "1.0"
created_date: 2026-10-05
status: BINDING
authority: Product Owner rulings for the GTWPE, from 2026-10-05
applies_to: the GTWPE (Glow Technical Writing Prompt Ecosystem) — every prompt it maintains or builds, through every revision, consolidation and handoff
---

# GTWPE decision record

Product Owner rulings that govern the GTWPE, with what follows from each. They are kept here, not in
`docs/ephemeral/`, because they outlive any one change or release. Entries carry the `GTWPE-` prefix so
they are not confused with the GCFPE decision record's `D` numbers or the GTWPE design's `D-` numbers.

## GTWPE-D1 — Every artifact has its own proof log

Nathan, 2026-10-05, verbatim:

> For the GTWPE, I want to make sure one critical requirement is preserved: every prompt that produces one of the defined GTWPE artifacts must also produce a separate proof log documenting how that artifact was created.
>
> For this requirement, there are only two possible artifact types:
>
> * The redlines Markdown file
> * The final updated PF Markdown file
>
> If a prompt produces either one of these, that output counts as an artifact and requires its own separate proof log. If a prompt produces both, then each artifact must have its own corresponding proof log, unless the prompt explicitly defines a single combined proof log that clearly covers both outputs.
>
> Ordinary conversational responses, status updates, recommendations, analysis, or other inline text do not count as artifacts for this requirement.
>
> Each proof log must, at minimum, record:
>
> * The artifact produced
> * The source files and inputs used
> * The substantive changes made
> * The basis for those changes
> * Any important constraints, assumptions, or interpretations applied
> * Any validation or verification performed
> * Any unresolved issues, limitations, or deviations
> * Enough identifying information to associate the proof log unambiguously with the correct redlines file or final PF file
>
> The proof log should provide enough evidence for another session or reviewer to understand what changed, what those changes were based on, how the artifact was produced, and what was verified.
>
> This requirement must remain intact throughout the GTWPE system. It must not be omitted, weakened, or lost during prompt revisions, consolidation, or handoffs.

What follows from it:

- **Which prompts it binds is decided by what they write, not by their names.** Any GTWPE prompt that
  writes a redlines Markdown file or a final updated PF Markdown file is bound, now and in every later
  version.
- **Every change keeps it whole.** A change to such a prompt, made through GTWPE-MGMT-10, leaves the
  requirement in full: the separate proof log, every minimum item, and the link to its artifact. A
  revision, consolidation or handoff that would drop or weaken any of these does not meet this record.
- **"Proof log" here is not the repository's governed evidence.** Canon and `AGENTS.md` use "proof"
  for evidence about the engine itself, much of it governed and written only by the canonical tools:
  path proofs, and proof logs such as the two-run identity proof log. A GTWPE proof log is the record a
  prompt writes beside its own artifact. This ruling does not make it governed evidence.
- **Canon is silent, so this ruling governs.** PF canon on `main` at `f29d778` was searched for "proof
  log", "processing report", "application report", "redline report" and "apply report". Only "proof
  log" matched. In HDE Governance, the Change Process Guide, the HDE Build Checklist (Separation), HDE
  Schemas and Artifacts, the HDE Mechanics Guide and HDE Phased Epics, each hit is an evidence log for
  the engine's own checks, such as the coupling proof log and the release-ID recompute proof log. The
  Glow QA Guide's one hit is the phrase "proof logic". HDE Build Notes has none. No PF document sets a
  rule for proof logs of technical-writing artifacts.
