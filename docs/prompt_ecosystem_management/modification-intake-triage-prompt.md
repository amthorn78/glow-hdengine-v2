---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-22
status: BINDING
authority: Product Owner decision D20, 2026-09-22
release_membership: NONE — deliberately outside GCFPE-20260914.1
governed_by: its output only; stubs are checked by modification_validate.py
---

# Modification Intake and Triage

The required entrypoint. Feedback arrives as a prose dump containing several changes; nothing
downstream can split that, so nothing downstream can start.

**This prompt is deliberately outside the release.** No graph part, no registry row, no §10
review, not a member of `GCFPE-20260914.1`. Changing it is an ordinary edit rather than a Class A
change, because it will be tuned often. It needs no contract of its own: its only output is
Modification stubs, and `modification_validate.py` already checks those. A bad triage emits stubs
that fail validation or that `ANALYZE` rejects at entry — the check is downstream and mechanical.

**Not a skill.** It is invoked explicitly when you have a dump. `AF-003` records that skill
triggering is probabilistic; a prompt you paste beats a skill that might not load.

## The boundary that keeps this from becoming a second ANALYZE

| | answers |
|---|---|
| **Triage** | *Is this one change or three, and is it new?* |
| **`ANALYZE`** | *What does this one change actually reach?* |

Triage does **identification-level research only** — enough to name what an item appears to touch
and to check it against the record. It never measures scope, never computes closure, never
classifies A–E, never plans. **If triage emits a scope measurement, that is the defect**, and it
is greppable.

---

## The prompt

Paste everything in the block, then the dump.

```plain text
You are performing Modification intake and triage for Nathan's Glow prompt ecosystem. You split
and deduplicate a dump of feedback into Modification stubs. You do not analyze, plan, or change
anything.

=== WHAT YOU DO ===

1. SPLIT the input into atomic candidate items. One item = one requested outcome. If two
   sentences ask for the same outcome, that is one item. If one sentence asks for two, that is
   two items.

2. STATE each item as a single sentence of requested outcome, in the requester's intent, not
   your interpretation of the fix.

3. DEDUPE each item against the record. Read, do not assume:
     - open Modifications in docs/ephemeral/modifications/ (any status but COMPLETE or ABANDONED)
     - GCFPE Alpha Feedback — Deferred Items — 091426.1 in Notion (AF-001 onward)
     - docs/prompt_ecosystem_management/reconciliation-backlog.md
     - docs/prompt_ecosystem_management/gcfpe.decision-record.md (D1 onward)

4. DISPOSE each item as exactly one of:
     NEW                     not found in the record
     DUPLICATE_OF <id>       the same outcome is already requested; name the id
     ALREADY_RULED <D-nn>    the Product Owner has decided this; name the D-number
     NOT_A_CHANGE            a question, or already true; say which, and answer it if it is a question
     NEEDS_YOU               the intent is genuinely ambiguous; state the ambiguity as a question

5. NAME THE APPARENT SURFACE for each item in one line — which prompt, skill, rule or document it
   looks like it touches. Mark it explicitly as unmeasured. You are not computing closure.

6. GROUP the NEW items into proposed Modifications. Items belong together when they share a rule,
   a verification, or one package/review/install cycle. Give each group a coupling:
     ATOMIC        one rule applied across surfaces; a failure in one invalidates the rest
     INDEPENDENT   items that merely share a cycle; one can block without stopping the others
   Rule-shaped work must be ONE group. Splitting it is the D12 error. A group has one coupling;
   if you need both, that is two groups.

=== WHAT YOU DO NOT DO ===

Do not measure scope. Do not run or emulate closure.py. Do not assign a gate tier. Do not assign
a modification_class. Do not plan. Do not decide a policy question. Do not edit any prompt, skill,
document, graph part or registry row. Do not write to Notion. Do not open a branch or a PR.

Your grouping is a PROPOSAL. Nathan approves it, and ANALYZE may revise it once before approval
freezes it.

=== WHAT YOU RETURN ===

A. A table, one row per item: item, one-sentence statement, disposition, apparent surface.
   Include EVERY item, including duplicates and already-ruled ones. An item Nathan raised deserves
   a visible record even when the answer is "we already decided this" — otherwise he raises it
   again in a month and nobody knows he asked.

B. The proposed grouping: which items form which Modification, each with its coupling and the
   reason those items belong together.

C. One Modification stub per proposed group, written to
   docs/ephemeral/modifications/MODIFICATION-<yyyymmdd>-<slug>.md using the template at
   docs/prompt_ecosystem_management/modification-template.md, with:
     status: INTAKE
     items:  the grouped items, each with an id and a statement, disposition empty
     request: the relevant part of the dump, verbatim
   and nothing else filled in. Everything past INTAKE belongs to ANALYZE.

D. The validator's output, run and pasted, not described:
     PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/modification_validate.py \
         docs/ephemeral/modifications/

=== HOW TO REPORT ===

Answer first. If an item is ALREADY_RULED or NOT_A_CHANGE, say so plainly rather than softening
it — telling Nathan a thing is already decided is the useful answer, not a failure to help.
Close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

---

## What good triage looks like

Twelve feedback points becoming three Modifications — one `ATOMIC` group of six that are one rule
across surfaces, one `INDEPENDENT` basket of four small skill edits sharing a package and review,
one standalone — plus two items disposed as `ALREADY_RULED` and never entering the pipeline at
all. Three passes instead of twelve, and two avoided entirely.
