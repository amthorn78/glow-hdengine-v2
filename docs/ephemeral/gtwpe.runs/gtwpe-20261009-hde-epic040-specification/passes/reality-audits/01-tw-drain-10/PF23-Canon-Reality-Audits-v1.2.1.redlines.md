# Redlines — Reality Audits (PF23)

## Header

- Run: `gtwpe-20261009-hde-epic040-specification`
- Prompt: `TW-DRAIN-10 — Prepare PF Document Redlines — 100726.1` (Notion `3f24590a05eb81fc872ad0003ac03086`)
- Target (directory + versionless name): `docs/pfcanon/` → `Reality Audits`
- Target file: `docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.1.md`
- Target base blob: `8552b26c62f4df4aef85d9d749c601a9db012dd3`
- Target baseline SHA-256: `d9e49c6fa3a7bc8195f5c1e824b57e7a5968402d3497154e475f805cfacdeb56`
- Preparation outcome: `READY`
- Save completeness: `COMPLETE_PACKAGE`

## Sources read whole

1. `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` — addendum `2.38 PF10-AINEUTRAL-001` (governing change source).
2. `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`.
3. `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`.
4. `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/triage/01-tw-triage-10/triage.md` (names the change that bears on this target).
5. `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` (editorial standard).

Canon read from `origin/main` at intake `0c4dddece401c457b2429ddc9cb8f2e819b4a943`; `docs/pfcanon/` verified unchanged from that commit. Working branch `docs/20261009-gtwpe-run-hde-epic040-specification`, HEAD `7ff4b1f3689ea18512f91345ace49846c868f0e5`.

## Scope

Exactly one change bears on this target: PF10 addendum `2.38 PF10-AINEUTRAL-001`, superseded-passages table row `Reality Audits §0` — the passage `Codex review passes run by the Product Owner` is read by function (no specific agent/product), per addendum rule 4. The closure decision and the specification contain no other reference to Reality Audits or PF23; the triage names no other change against Reality Audits.

---

## Redline R1

- Redline number: `R1`
- Findings or source items: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.38 PF10-AINEUTRAL-001`, superseded-passages table row `Reality Audits §0`.
- Change type: `CANON_UPDATE`
- Operation: `REPLACE`
- Target document: `PF23-Canon-Reality-Audits`
- Target-document evidence: `These audits are **Codex review passes run by the Product Owner at the closure of each epic** to compare what actually shipped (code, evidence, repo layout) with what PF-Canon and the epic plan said should exist. Their purpose is to:`
- Controlling basis: `PF10-HDE-Build-Notes-v13.5.md`, addendum `2.38 PF10-AINEUTRAL-001`, rule 4 ("Roles read by function") and superseded-passages table row `Reality Audits §0`.
- Rationale: Addendum 2.38 rule 4 attaches any governance role assigned through a named AI product to the function, whichever product performs it; the table maps `Codex review passes run by the Product Owner` to `review passes the Product Owner runs, whichever agent performs them`. The named product `Codex` is removed and the function-based reading is added.
- Section path: `# 0) Front Matter` → `Intent & scope [Required-Now]`
- Action: `REPLACE ONCE` — replace the unique old block below with the new block below, leaving the surrounding `**…**` bold markers unchanged.
- Uniqueness: `section-path matches=1 | old-block occurrence expected=1, observed=1`
- Expected occurrence: `1`
- Observed occurrence: `1`

### OLD (exact, one occurrence)

````markdown
Codex review passes run by the Product Owner at the closure of each epic
````

### NEW (complete replacement)

````markdown
review passes run by the Product Owner at the closure of each epic, whichever agent performs them
````

END OF REDLINES
