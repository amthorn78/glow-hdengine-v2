---
artifact_type: PROMPT_ECOSYSTEM_DECISION_RECORD
artifact_version: "1.0"
created_date: 2026-09-17
status: BINDING
authority: Product Owner rulings, 2026-09-17
applies_to: GCFPE-20260914.1 / 091426.1 / 55 and the prompt-management ecosystem generally
---

# Prompt ecosystem decision record

Product Owner rulings that govern the prompt ecosystem, with the consequences that
follow from each. Recorded here rather than in a pull request discussion because
these decisions outlive the change that produced them.

## D1 — No Drive URL in the PF10 addendum contract

PF10 is referenced by **canonical name and its canonical location in `docs/pfcanon`**.
No separately carried direct URL to PF10 or to any addendum. PF10 is the canonical
location; that is where agents go to find it.

Applied as one canonical decision everywhere it appears, not reinterpreted per prompt.

## D2 — No drain owner

`drain_owner` is not specified anywhere: not as a contract value, not as an artifact
field, not as something a later prompt tracks or reports. The contradiction between
`drain_owner` as a required value and `drain_owner` in `forbidden_fields` is resolved
by **deleting the requirement**, not by reconciling the two.

## D3 — The detailed per-PR Implementation Plan is left alone

Evidence: PF10 2.14 binds "Epic or CRD Implementation Plan"; PF04 §9.1.1 names the
concrete types as `EPIC_IMPLEMENTATION_PLAN` and `CRD_IMPLEMENTATION_PLAN` and
distinguishes the detailed per-PR plan from them throughout; PF27 does not list the
per-PR plan among its governed artifacts and contains no occurrence of "per-PR".

No canonical home is created for it. PR-10 and PR-20 are not refactored to remove
duplication. Repair only on an actual contradiction or functional defect.

## D4 — The addendum-role token is removed

**The behavioural rule, which is what matters:** only a prompt that approves a
qualifying material change to an already-approved Specification or Plan may create a
`PF10_BUILD_NOTES_ADDENDUM`, and only on that approval. The addendum records the
approved change without rewriting the immutable approved base. Every other outcome
and every other prompt creates none.

The `PF10 addendum role` token is **removed** from prompt bodies and from
`global.json`'s `role_vocabulary`. Evidence for removal:

- nothing reads it — it appears in the graph only as `.node.pf10_addendum_role`, a
  leaf attribute, in zero edges, conditions, predicates or routes;
- no prompt body references any other prompt's role;
- four of the six declared producers used three different values for the same
  concept, because nothing authoritative defined it;
- the Project Prompt Contract Registry already carries the same fact in a better
  form — `outputs[].artifact` names the artifact rather than asserting a role, so it
  is derivable and checkable against the body.

Metadata is kept only where it provides concrete operational benefit. A second
encoding of a fact the registry already holds is not that.

## D5 — PF27 governs Ops Task Record and Remediation Review Record

PF27 explicitly claims both in its governed-artifacts list and contains their
templates (§3, §5), so PF27 is the structural authority.

**The general rule:** if Canon already provides the template for an artifact, use the
canonical template. If Canon does not, the required structure may remain in the
producing prompt.

This does not license rewriting every prompt that happens to share field names.
Repair only actual conflicts, incorrect bindings, or places where a prompt would
cause an artifact to diverge from the PF27 template.

## D6 — Drainage is removed from prompt behaviour entirely

**No prompt knows that drainage exists.** Prompt logic contains no manual drain,
drain owner, drain status, `MANUAL_DRAIN_REQUIRED`, `DRAIN_VERIFIED`,
`MANUAL_DRAIN_MISMATCH`, `READY_FOR_MANUAL_DRAIN`,
`NON_CANONICAL_PENDING_MANUAL_DRAIN`, pre-drain or post-drain state, waiting for
anyone to drain, blocking until a drain occurs, verifying that one occurred, or
reconciling drain evidence — **and no renamed equivalent.**

### The lifecycle, from every prompt's view

A qualifying approval creates the addendum. After that turn, the addendum is part of
PF10. On the immediately following turn the receiving prompt reads PF10 and confirms
the expected update is visible. **That is all.**

It is not a drain check, canonicalization check, synchronization check, ownership
check, content verification, byte comparison, reconciliation procedure, new status
machine, or new artifact requirement. After that turn the transition is over, and
later prompts simply read current PF10 and work from current Canon.

### Why

Historical evidence must never gate current execution. The originating failure was a
prompt refusing to continue after the PF10 update had already happened, because it
was still looking for an intermediate condition that no longer mattered. A
conversational override is available and is exactly what this removes — these
workflows are intended to become increasingly automated.

### Consequences

- `POST_CLOSURE_DRAINAGE_STATUS` is **removed, not renamed**. CL-20 keeps its closure
  memo and loses the producer roster, the storage contract, the addendum links, the
  drain evidence and the drain-state inputs. What it needs, it reads from current PF10.
- `PF10_REFERENCE_ROLE` is **deleted as a field**. What is retained is the factual
  provenance — the PF10 version or equivalent identity actually read at that point.
  **Record what was read; do not assign it a workflow state.** A field with allowed
  values invites later logic to branch on it; a recorded fact cannot become a gate.
- RS-40 loses its `DRAIN_VERIFIED` gate and keeps its resumption and routing
  responsibility. If current Canon says implementation may resume, it resumes.

### What must survive

Removal is scoped to drainage machinery, not to functionality sharing a paragraph
with it:

- **approved-base immutability** — independent, and one of the reasons the addendum
  mechanism exists at all;
- legitimate routing and resumption behaviour;
- historical and provenance facts;
- current PF10 as execution authority;
- any unrelated functional requirement in the same clause.

## Execution decisions

**Drainage removal is one cross-cutting repair**, outside the six-batch sequence,
because it is one global rule and splitting it across six authorizations creates six
chances to apply it six different ways. This is an exception for this shared rule
only; it is not a licence to collapse the batch structure, and batch-local review of
unrelated changes still happens in its batch.

**Drainage findings are not adversarially verified before repair.** D6 resolves the
substantive question, so occurrence-by-occurrence litigation buys nothing. This is
not a licence for blind string deletion — see *What must survive*. Verification is
retained where a false positive would cause a wrong functional edit, including the
storage-architecture and specification-format findings.

**The Project Prompt Contract Registry is re-pointed to the current release before
approval**, not approved stale and updated afterward.
