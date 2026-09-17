---
artifact_type: RECOVERY_VALIDATION_PROMPT
logical_id: GCFPE-CHANGE-FLOW-REPAIR-RECOVERY-VALIDATION
version: "1.0"
date: 2026-09-14
mode: TARGETED_READ_ONLY_RECOVERY_AUDIT
mutation_authority: REPORT_ARTIFACTS_ONLY
output_location: "Google Drive / Glow / Ephemeral Planning Files"
---

# Validate and Recover Partial GCFPE Repair Work

Run **`amthor-workspace-governance-audit` in TARGETED analysis mode** as the primary skill for this task.

Do **not** run `change-flow`, `glow-hde-devops`, `glow-hde-pr-development`, or `skill-creator` as the controlling skill. This is not an implementation, repair, release, DevOps, or skill-editing session. If a complete recovered Flowmaster candidate needs deterministic verification, `flowmaster-validate` may be used read-only against that candidate only.

## Role

Act as an independent recovery auditor. A previous dedicated implementation session was stopped after it drifted away from the authorized GCFPE repair. Its narrative claims and completion statements are untrusted unless corroborated by durable evidence.

Your only purpose is to determine:

1. what durable work the failed session actually created or changed;
2. which work, if any, is complete and trustworthy enough to reuse;
3. which work is partial, conflicting, unsafe, or unverifiable;
4. whether any protected operational state was changed;
5. the earliest exact point from which a later authorized repair session could safely resume.

Do not continue the repair. Do not complete missing work. Do not clean up the failed session's effects.

## Cost and focus constraint

Minimize paid actions and redundant reads. Batch compatible read operations. Do not run CI, build pipelines, deployments, full test suites, or broad exploratory searches. Begin with the named authoritative sources and follow only links or repository evidence needed to prove or disprove a specific recovery claim.

If decisive evidence cannot be accessed, classify the result as `INDETERMINATE`; do not compensate with speculation or wider tangents.

## Absolute mutation boundary

This is a read-only audit except for creating the two required recovery deliverables in `Glow / Ephemeral Planning Files`.

You must not:

- edit, create, replace, select, promote, publish, or supersede any GCFPE prompt, catalog entry, release-register entry, skill, canon file, plan, or Alpha record;
- edit, drain, append to, or otherwise mutate PF10;
- archive, move, delete, restore, rename, or reorganize any page, file, prompt, candidate, or release;
- create a competing GCFPE release candidate;
- commit, push, open or modify a pull request, trigger or wait for CI, deploy, or perform any GitHub write;
- contact, resume, or depend on the failed session;
- resume the EPIC040 Alpha or begin PR04 planning;
- issue an RS-20 handoff or any other implementation handoff;
- treat this prompt, the failed implementation prompt, a transcript, or a completion claim as proof that work exists.

If you discover a harmful or unauthorized mutation, report it precisely and leave it untouched.

## Canon and file-format boundary

- Read PFCanon sources **only in Markdown form**.
- Never open, inspect, index, compare, or rely on Google Docs, `.doc`, or `.docx` versions of PFCanon files.
- Do not use ChatGPT Library or Library IDs for source retrieval or output storage.
- Use exact Notion pages, exact Google Drive links, and local installed-skill Git evidence.
- Do not invent or depend on a session-inspection endpoint.

## Authoritative instruction sources

These define what the failed session was supposed to implement; they are not evidence that it did so:

- Approved repair plan: [GCFPE Change Flow Repair Plan v2.0](https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk)
- Failed-session implementation prompt: [GCFPE Change Flow Repair Implementation Prompt v1.0](https://drive.google.com/file/d/1NhVE0jZLS0UIfZWsokymRiglsYv1Z4Lc/view?usp=drivesdk)

Use their work-package definitions and acceptance criteria as the recovery comparison baseline. Record their exact fetched identity, metadata, and content digest before comparison.

## Known baseline to verify, not assume

The last known pre-repair baseline was reported as:

- selected release: `GCFPE-20260913.1`;
- MGMT prompt: `GCFPE-MGMT-10 — Manage an Ecosystem Change — 091326.2`;
- selected ecosystem size: 54 members;
- Alpha stopping point: PR03 accepted-final;
- next intended Alpha action: PR04 planning, not yet started.

Treat every item above as a claim requiring live verification. If durable evidence now differs, report the current state and the evidence supporting it.

## Primary live sources

Inspect the current contents and metadata of these exact records first:

- [GCFPE prompt catalog](https://app.notion.com/p/3da4590a05eb81bcbc5deb2d2cec4f1f?pvs=204)
- [GCFPE release register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204)
- [GCFPE-MGMT-10](https://app.notion.com/p/3da4590a05eb81ac80e6d886a25aa026?pvs=204)
- [EPIC040 Alpha notes](https://app.notion.com/p/3d64590a05eb81e1a645e0ca209b45c0?pvs=204)
- [GCFPE operating procedure](https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk)
- [PR-development skill-fit decision](https://app.notion.com/p/3d94590a05eb81f6824ff4bf507d474c?pvs=204)
- [Glow / Ephemeral Planning Files](https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc)

From those records, follow only the exact linked Flow Index, prompt hubs, candidate/release pages, and evidence artifacts relevant to changes made by the failed session.

## Installed-skill and repository scope

Read-only inspect the installed sources and Git history/status/diffs for:

- `amthor-workspace-governance-audit`;
- `flowmaster-validate`;
- `change-flow`;
- `glow-hde-pr-development`;
- `glow-hde-devops`;
- `glow-merged-change-attribution-lock`.

Determine whether the failed session modified any installed skill, created uncommitted files, created commits, or left multiple workspaces/worktrees. Search for existing workspaces before concluding that work is missing. Do not modify, stash, reset, checkout, clean, commit, or push anything.

## Recovery procedure

### 1. Pin the observed baseline

Record for every decisive source:

- stable ID or exact URL;
- title or skill identity;
- parent/container;
- lifecycle or selection state;
- version/revision when exposed;
- retrieval time;
- content digest or Git object identity;
- whether the representation is complete.

If a source changes after pinning, record `SRC-002` and do not silently refresh the audit basis.

### 2. Inventory durable effects

Identify all artifacts and mutations plausibly attributable to the failed implementation session, including:

- new or edited Notion prompt pages, hubs, catalog rows, release rows, or Alpha records;
- new or edited Markdown files in `Glow / Ephemeral Planning Files`;
- modified installed-skill files, uncommitted changes, commits, branches, worktrees, or generated validation evidence;
- candidate manifests, topology maps, inventories, comparison matrices, validation reports, readback evidence, or migration records;
- changes to selected/current release state;
- any archive, move, deletion, restoration, or duplication event visible in durable metadata.

Use timestamps only as discovery clues, never as sole attribution proof. Establish attribution from identity, content, lineage, parentage, diffs, and references.

### 3. Compare against the approved repair

Map every discovered artifact to the exact repair-plan work package and acceptance criterion it purports to satisfy. Determine the actual state of each planned work package, including the work concerning:

- PF10 addendum governance and rescope/escalation control;
- a distinct second implementation/continuation prompt where required;
- PR-session skill evaluation and the specialized `glow-hde-pr-development` skill;
- smart local-test-first commit/push behavior and review-before-CI economics;
- existing-workspace recovery;
- Google Drive Markdown artifact routing;
- Markdown-only PFCanon access;
- GCFPE graph, catalog, release, validation, and Alpha-resumption changes.

Do not infer completion from the presence of a filename, page shell, checklist, or self-authored status statement. Inspect complete content and its consumers.

### 4. Classify each item

Assign exactly one recovery classification:

- `RECOVERABLE_CONFIRMED`: complete, internally consistent, correctly located, attributable, and independently validated against its governing requirements;
- `RECOVERABLE_WITH_REVALIDATION`: apparently complete and attributable, but missing final deterministic validation or readback proof;
- `PARTIAL_RECOVERABLE`: contains useful work, but is incomplete; identify the exact usable portion and every missing dependency;
- `CONFLICTING_OR_UNSAFE`: conflicts with authoritative state, exceeds authority, introduces ambiguous identity, or cannot safely become a base;
- `UNVERIFIED`: evidence is insufficient to establish content, lineage, completeness, or attribution;
- `NOT_FOUND`: required work has no durable evidence after bounded source inspection.

Also assign one observed lifecycle state:

- `NOT_STARTED`
- `EVIDENCE_ONLY`
- `DRAFT_CANDIDATE`
- `COMPLETE_UNSELECTED_CANDIDATE`
- `VALIDATED_UNSELECTED_CANDIDATE`
- `SELECTED_UNVERIFIED`
- `SELECTED_VALIDATED`

Never upgrade lifecycle or recovery classification merely because the previous session said an item was complete.

### 5. Reconcile maker and readers

For every recovered producer artifact, identify its required readers/consumers and verify they agree on:

- identity and version;
- input/output schema;
- authority and approval boundary;
- parent/container and handoff target;
- stop condition and continuation behavior.

Use the governance-audit rule IDs where applicable, including `SRC-*`, `INV-*`, `CTR-*`, `TOP-*`, `AUT-*`, `ART-*`, `MUT-*`, `SES-*`, `SKL-*`, `PUB-*`, and `COL-*`.

### 6. Determine the safe recovery point

State:

- the verified current selected release and ecosystem size;
- whether the selected catalog/register or any authoritative prompt was changed;
- whether any unauthorized mutation occurred;
- which exact artifacts may be reused unchanged;
- which exact artifacts require revalidation before reuse;
- which fragments are useful but must not be treated as completed work;
- which artifacts must not be reused;
- the earliest unmet dependency in the approved repair plan;
- the safest exact restart point for a future, separately authorized repair session.

The restart point is a finding, not an authorization. Do not generate a restart or implementation prompt.

## Required deliverables

Create exactly these two new, machine-readable Markdown files in `Glow / Ephemeral Planning Files`:

1. `GCFPE-Repair-Recovery-Validation-Report-v1.0-20260914.md`
2. `GCFPE-Repair-Recovery-Evidence-Manifest-v1.0-20260914.md`

Do not create a proposed changeset, PF10 addendum, repair candidate, replacement prompt, release artifact, or Alpha handoff.

### Report requirements

The validation report must contain:

1. executive recovery verdict;
2. scope and mutation attestation;
3. pinned-source table;
4. verified current baseline;
5. durable-effect inventory;
6. work-package recovery matrix;
7. artifact-by-artifact classification and rationale;
8. governance findings with rule IDs and evidence references;
9. authoritative-state mutation check;
10. safe-to-reuse list;
11. revalidation-required list;
12. do-not-reuse list;
13. exact earliest unmet dependency;
14. exact safest restart point;
15. unresolved evidence gaps;
16. final manual-review gate.

### Evidence-manifest requirements

The evidence manifest must use compact Markdown tables and fenced YAML for machine-readable records. Give each evidence item a stable ID and include:

- source ID/URL/path;
- source type;
- complete/incomplete status;
- revision/digest/Git object;
- retrieval time;
- relevant work package;
- finding IDs supported;
- recovery classification;
- lifecycle state;
- attribution basis;
- notes on uncertainty.

## Final verdict

Emit exactly one recovery verdict:

- `RECOVERY_CONFIRMED`
- `PARTIAL_RECOVERY_AVAILABLE`
- `NO_RECOVERABLE_WORK_FOUND`
- `RECOVERY_INDETERMINATE`
- `UNSAFE_STATE_DETECTED`

Also emit the governance-audit verdict required by the primary skill: `PASS`, `PASS WITH WARNINGS`, `FAIL`, or `INDETERMINATE`.

Use `RECOVERY_CONFIRMED` only when all claimed completed repair work is durably present, attributable, internally consistent, and independently validated. Use `UNSAFE_STATE_DETECTED` if selected/current authority, PF10, Alpha state, archives, or installed skills were mutated outside the approved boundary.

## Required final response

Return only a concise Product Owner summary containing:

- recovery verdict and governance-audit verdict;
- verified selected release and Alpha stopping point;
- counts by recovery classification;
- whether protected state was changed;
- exact safest restart point;
- links to the two Drive deliverables;
- the statement: `No repair, release, PF10, archive, GitHub, CI, or Alpha-resumption action was performed.`

Stop for Product Owner review. Do not suggest or begin the next action.
