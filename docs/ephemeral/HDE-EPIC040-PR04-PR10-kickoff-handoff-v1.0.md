---
artifact_type: PR10_KICKOFF_HANDOFF
artifact_id: HDE-EPIC040-PR04-PR10-KICKOFF-HANDOFF
artifact_version: "1.0"
artifact_state: COMPLETE
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
destination_prompt: PR-10 — Create PR Work-Unit Instructions — 091426.1
created_date_utc: 2026-09-21
authority: Product Owner instruction, 2026-09-21 — Alpha unblocked; PR04 PR-10 instruction authoring may begin
grants: PR-10 instruction authoring only. No Proceed. No implementation. No merge.
---

# HDE-EPIC040-PR04 — PR-10 kickoff handoff

Paste the fenced block below to the retained whole-change `HDE-EPIC040` Implementation Architect.

**Why PR-10 and not IA-10.** The whole-change Implementation Audit (`v2.0`, `AUDIT_COMPLETE`) and
Implementation Plan (`v2.1`, approved by Review `v2.1`) already exist and are immutable. `IA-10`
would author a fresh Audit and Plan and would therefore re-open an approved base. `PR-10 — Create
PR Work-Unit Instructions` is the stage the PR03 acceptance names, and it is authored *by* the
same whole-change IA — the actor is the IA, the prompt is PR-10.

---

```plain text
NEXT_PROMPT_HANDOFF

Run PR-10 — Create PR Work-Unit Instructions — 091426.1
https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204

Resolve that prompt at version 091426.1 from the GCFPE Membership and Release Register
(https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1), which is the sole selection
authority. GCFPE-20260914.1 / 091426.1 / 55 was selected on 2026-09-21. Earlier records in this
Epic's lineage route to PR-10 at 091326.2; that version is archived and is historical lineage, not
a routing instruction.

=== RECEIVING ROLE AND SESSION ===
Actor: the Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Architect.
session_disposition: RETAIN_EXISTING. role_session_ref: the established whole-change IA session
that authored the Audit v2.0, the Plan v2.1 and the PR01-PR03 instruction set. Do not create,
restart or replace a session. If that session is unavailable, say so and stop; do not substitute
a new one.

=== CHANGE AND WORK UNIT ===
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040 — Separation Pass 3
WORK_UNIT_ID: HDE-EPIC040-PR04
Work unit scope, per the immutable Plan: application eligibility, identity and consumer
integration. PR05 owns golden comparison and read-only readiness; PR06, PR07 and OPS01 retain
their planned work. Do not widen PR04 into their scope.

=== ARTIFACT MIGRATION CONTEXT — READ BEFORE RESOLVING INPUTS ===
Every input below was produced under the prior ChatGPT / Google Drive workflow and has been
migrated into docs/ephemeral/ in amthorn78/glow-hdengine-v2. Contents and filenames are preserved.
Storage metadata is not, deliberately.

Inside these artifact bodies you will find roughly 105 `libfile_...` ChatGPT Library identifiers
and 37 drive.google.com links. NONE of them resolve. That is the expected result of the migration
and is NOT broken lineage. Do not attempt to resolve, fetch, reconstruct or repair them; do not
treat one as a missing input, a source-resolution error or a blocker; do not return
SOURCE_RESOLUTION_ERROR on account of one. They are prior-platform provenance. Every artifact they
name is either listed below by repository path or is historical evidence outside your inputs.

Resolve each input by its exact repository path and the identity its own body declares. The
continuity record for this migration, including the confirmation that all seven inputs are present
and self-identifying, is:
  docs/ephemeral/HDE-EPIC040-lineage-migration-transition-reference-v1.0.md
Read it first. It is short and it answers the questions the dead links will otherwise raise.

=== REQUIRED INPUT ARTIFACTS, BY REPOSITORY PATH ===
All under docs/ephemeral/ in amthorn78/glow-hdengine-v2, branch main.

Required predecessor acceptance:
  HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md
  PR_WORK_UNIT_LINEAGE_REVIEW v1.0, COMPLETE, decision ACCEPT. HDE-EPIC040-PR03 is ACCEPTED_FINAL.

Approved Specification base:
  HDE-EPIC040-specification-v1.1-approved.md
  SPECIFICATION v1.1, SPECIFICATION_APPROVED. Immutable.

Implementation Audit base:
  HDE-EPIC040-implementation-audit-v2.0.md
  IMPLEMENTATION_AUDIT v2.0, AUDIT_COMPLETE.

Immutable whole-change Plan:
  HDE-EPIC040-implementation-plan-v2.1.md
  IMPLEMENTATION_PLAN v2.1. Its own header reads PLAN_PENDING_REVISED — that is its authoring
  state, not its current state. It is APPROVED, by the separate review below. Read the pair.

Approving Plan Review:
  HDE-EPIC040-implementation-plan-review-v2.1.md
  IMPLEMENTATION_PLAN_REVIEW v2.1, decision APPROVE, Isis-50, 2026-09-09T13:36:43Z. It declares
  the exact approved bytes: 146,624 bytes, 985 LF-terminated lines, SHA-256
  10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be. The migrated Plan file
  reproduces all three exactly, so the approved artifact is identified without reference to any
  storage system.

Accepted dependency lineage, PR01:
  HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md
  PR_WORK_UNIT_LINEAGE_REVIEW v1.1, decision ACCEPT. Use v1.1. A v1.0 is also present in the same
  directory and is the superseded PENDING predecessor, preserved as historical evidence.

Accepted dependency lineage, PR02:
  HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md
  PR_WORK_UNIT_LINEAGE_REVIEW v1.0, COMPLETE, decision ACCEPT.

Migration continuity record:
  HDE-EPIC040-lineage-migration-transition-reference-v1.0.md

=== CURRENT STATUS AND DECISIONS ALREADY MADE ===
PR01, PR02 and PR03 are ACCEPTED_FINAL and are not rerun. PR03 landed as merged commit
9cda1b49a972da874021e8820997fab1ebaff153, "HDE-EPIC040-PR03: Pure Gate mechanics and intrinsic
identity (#405)", 2026-09-14T12:33:13Z.
Alpha was unblocked by the Product Owner on 2026-09-21. The stop reason
ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR is discharged: the Change Flow prompt ecosystem was
repaired and GCFPE-20260914.1 / 091426.1 / 55 was selected the same day.
The approved Specification, Audit and Plan are immutable and are not re-opened by this stage.

=== CONSTRAINTS AND AUTHORITY BOUNDARY ===
This handoff authorises PR-10 instruction authoring for HDE-EPIC040-PR04 and NOTHING ELSE.
It is not a Proceed. PR04 implementation requires the Product Owner's separate exact invocation of
PR-30 against the detailed PR04 Plan, after PR-20 produces it.
Do not implement, create a branch, open a pull request, merge, enable auto-merge, edit PF10,
allocate a PF10 number, drain an addendum, execute QA or Ops, or invoke PR-50. Merge and abort
remain Product Owner-only actions.
Write every artifact you produce as complete machine-readable Markdown at a path under
docs/ephemeral/, commit and push it on a working branch, read it back completely, and reference it
by repository path. Repository paths outside docs/ephemeral/ and docs/graph/ are not written.
docs/pfcanon/ is read-only. Nathan alone merges; an open pull request is a complete outcome.
Resolve current PF10 afresh from docs/pfcanon/ as controlled Markdown, and record the version you
actually read as provenance. Google Drive is not a source, a store or an authority for this work.

=== UNRESOLVED ITEMS AND THEIR OWNERS ===
None blocking this stage. For completeness: the PR04 detailed Plan does not yet exist and is
PR-20's output, not an input you require; the Product Owner's PR-30 Proceed for PR04 does not
exist and must not be assumed, requested as a precondition, or fabricated.

=== MANUAL PREREQUISITE ===
None. Alpha is unblocked and this stage may begin on receipt.

=== NEXT ACTION AND EXPECTED OUTPUT ===
Author one complete PR_INSTRUCTION for HDE-EPIC040-PR04 from the immutable approved Plan v2.1,
bounded to PR04's planned scope, in the format PR-10 requires. State its repository path, its
state, and the exact next stage and actor — PR-20, the dedicated PR04 PR-development session — in
one complete direct native handoff. Do not author the detailed PR Plan yourself and do not request
a Proceed in the same breath.
```
