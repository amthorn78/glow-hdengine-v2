---
artifact_type: CHANGE_CLASS_SELECTION
artifact_version: "1.0"
logical_id: HDE-CRD-0002-CHANGE-CLASS-SELECTION
change_id: HDE-CRD-0002
change_class: CRD
state: CLASS_SELECTED
selected_by: Nathan / Product Owner
producer: Master Scrum
prompt: CF-PO-10 — Record Product Owner Change-Class Selection — 100926.1 (https://app.notion.com/p/3f44590a05eb81f9bf84f4585d9f7a2c)
entry_mode: EVIDENCED_SELECTION_RECORDING_OR_RECOVERY
recorded_at: 2026-10-12T18:48:00Z
repository_head_read: origin/main c2bb229
source_ref: docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md
next_prompt: CF-C-10
next_actor: Master Scrum
---

# HDE-CRD-0002 — Change-class selection record

## Result

| Field | Value |
| --- | --- |
| State | `CLASS_SELECTED` |
| Change | `HDE-CRD-0002` |
| Class | `CRD` |
| Selected by | Nathan / Product Owner |
| Mode | `EVIDENCED_SELECTION_RECORDING_OR_RECOVERY`: an existing explicit decision is recorded; Nathan was not asked to choose again |
| Source | `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`, read completely on `main` at `c2bb229` |
| Route | CF-C-10 — Prepare CRD Specification Kickoff Handoff — 100926.1 |

## Selection evidence (verbatim, Product Owner)

Recorded in the source's "Product Owner decisions" section:

- 2026-10-11: "Move all items to accepted for CRD drafting."
- 2026-10-11: "You can create a handoff for this to begin the process for HDE-CRD0002"
- 2026-10-11: "Yes, add all seven to HDE-CRD-0002."
- 2026-10-12: "Add the 7 items to the CRD"

Given to this invocation:

- 2026-10-12: "give me a handoff to begin the change dev process with this CRD in the master scrum process, using the current GCFPE."

The Product Owner wrote `HDE-CRD0002`; the source records the canonical form `HDE-CRD-0002` (PF30.1 §3.1). The source also records the 2026-10-12 report "APP_ENV in railway is set to prod" as Product Owner context, not as selection evidence.

## Identity and scope lineage

- Identity: `HDE-CRD-0002`, kept as given. This record does not allocate, require or use a PF30 number or a PF09 mapping.
- Proposed change: Candidate CRD Items List items 5, 6, 7 and 8 (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d), as one change, as stated in the source.
- Source lineage: briefs v1.0 → v1.1 → v1.2. v1.2 is the current version; v1.0 and v1.1 are superseded.

## Checks

| Check | Result |
| --- | --- |
| Existing `CHANGE_CLASS_SELECTION` record for HDE-CRD-0002 on `main` at `c2bb229` | None found (`docs/ephemeral/` listing) |
| Conflicting class claim in the source or Notion register | None found. The source and the Candidate CRD Items List both record CRD and HDE-CRD-0002 |
| Source read completely | Yes, all 21,054 bytes on `main` |

## Constraints and unresolved items

- This selection is not downstream approval (PF04 §9.1 role table, "Epic/CRD class selection"). It does not approve scope, draft a Specification, register PF30, create a PF10 addendum, or authorize implementation.
- Source finding carried for the Specification to decide (owner: Isis at CF-C-20): item 6(a) is "not naturally CRD lane"; its native route is GCFPE-MGMT-10.
- Item 8 needs a canon ADR, as the source states.

## TypeSafe reading for the receiving session (CF-C-10)

Action sent (v6): "Prepare a sanitized CRD Specification kickoff document from one existing, already reviewed 21 KB source brief covering four items with about twenty defect parts, accounting for every source unit; no code is written, no live provider run occurs, and an independent Specification author and Product Owner approval follow."

- TypeSafe cell: Opus 5.5 at high
- Rung probabilities: score 1.69, confidence 0.67: low 0.01, medium 0.39, high 0.51, extra high 0.09, max 0.00, ultracode 0.00; twelve cells (computed): Opus 5.5 at low 0.01, Opus 5.5 at medium 0.39, Opus 5.5 at high 0.50, Opus 5.5 at extra high 0.09, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between medium and high
- Model probabilities: Fable 5.1 0.01, Opus 5.5 0.99, confidence 0.98
- Detail: v6 sent 2026-10-12T18:47:50Z; HTTP 200 in 0.58 s; 4166 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between medium and high.
- Nathan's pick: not stated.

Surface advice: run CF-C-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. It needs repository read and write to `docs/ephemeral/` only, plus the installed TypeSafe scoring skill.

## Canon relied on

Read on `main`:
- PF04-Canon-HDE-Governance v2.8.7: §9.1 Single-home doctrine, the change-class paragraph and the role table row "Epic/CRD class selection".
- PF30.1-Canon-HDE-CRD-Records: §3.1 identifier syntax, as cited by the source (not re-read here).

In-flight documents: `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`; the Candidate CRD Items List (Notion), read 2026-10-11.
