---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_POLICY
artifact_version: "1.0"
created_date: 2026-09-22
status: BINDING
authority: Product Owner, 2026-09-22 — "Policy Update — Notion Storage and Write Boundaries"
scope: operational documentation and Ops Hub guidance. Prompt bodies and skills are explicitly out of scope for this amendment.
---

# Notion storage and write boundaries

**Not every prompt belongs in Notion, and executing a prompt does not produce a Notion write.**

This is a focused operational-policy amendment. It is not a prompt audit and not a documentation
overhaul.

## The policy, as issued

Recorded verbatim. Where this document elaborates, the elaboration is subordinate to the text
below.

> Notion is used for the prompts, records, and operational information that are intentionally
> maintained there. It is not a mandatory repository for every prompt created or used in the
> ecosystem.
>
> The following categories do **not** need to be stored in Notion:
>
> - one-off prompts created for a specific, bounded task;
> - session-to-session handoff prompts;
> - temporary correction, recovery, review, or clarification prompts;
> - development prompts used to run or continue the ecosystem flow;
> - other prompts that are not intended to become durable, reusable Notion-managed prompt assets.
>
> In particular, a development prompt that is executing the ecosystem flow may read the required
> Notion prompt pages and operational records, but it must not write anything to Notion unless the
> instruction for that specific task explicitly directs a Notion write.
>
> Do not infer a Notion-write requirement from any of the following:
>
> - the fact that a prompt was used;
> - the fact that a handoff occurred;
> - the fact that a development task completed;
> - the existence of an output, report, review, or decision;
> - a general preference for documentation.
>
> A Notion write requires explicit task-level authorization or an explicit established destination
> rule. Without that authorization, the correct posture is read-only with respect to Notion.

## The default is read-only

| | |
|---|---|
| **Reading Notion** | Unrestricted. Read the prompt pages, registers, indexes and records the task needs. |
| **Writing Notion** | Only on explicit task-level authorization, or an explicit established destination rule. |
| **Absent either** | Read-only. Not "write something small"; not "write it and flag it". Read-only. |

**A write you cannot point at an authorization for is not a cautious write. It is an unauthorized
one.** The authorization is either in the instruction for this specific task, or it is a
destination rule that already exists and names this artifact type and its page. Nothing else
qualifies.

## What is not an authorization

None of these creates one, alone or in combination:

- a prompt was used;
- a handoff occurred;
- a development task completed;
- an output, report, review or decision exists;
- documentation is generally preferable;
- the record "should" reflect what happened;
- a page exists that the artifact would fit on;
- a previous session wrote something similar.

The last two are the ones that actually bite. **A plausible destination is not a destination rule**,
and **precedent set by an unauthorized write does not retroactively authorize it.**

## Which prompts are Notion-managed, and which are not

| Notion-managed | Not Notion-managed |
|---|---|
| The selected release's prompt bodies — currently the 55 members of `GCFPE-20260914.1 / 091426.1` | one-off prompts for a specific, bounded task |
| The PE Metaprompt, the manager prompt, and the controls the register binds | session-to-session handoff prompts |
| Prompts a `GCFPE-MGMT-10` change deliberately creates as durable members | temporary correction, recovery, review or clarification prompts |
| | development prompts running or continuing the ecosystem flow |
| | anything not intended to become a durable, reusable Notion-managed prompt asset |

The distinguishing question is **not** "is this prompt important?" or "did it work?" It is: **is
this intended to become a durable, reusable Notion-managed prompt asset?** A prompt can be
load-bearing, carefully written, and reused across three sessions, and still belong nowhere near
Notion.

A handoff prompt is the clearest case. It is the vehicle that carries one task to the next session.
Its content is fully determined by the task it carries, it has no life after that task, and
preserving it in Notion adds a page that must thereafter be maintained, versioned, archived and
kept from contradicting the register. **A handoff prompt belongs in the handoff.** Where a durable
record of it is genuinely wanted, its home is `docs/ephemeral/` in the repository, landed by pull
request — not a Notion page.

## Where things do go

This policy removes a false obligation; it does not remove the real ones. Nothing here changes the
architecture in `README.md`:

| | |
|---|---|
| durable prompt behaviour | Notion, authored in place |
| procedure, convention, registry, decision record | `docs/prompt_ecosystem_management/` |
| run artifacts, reports, ledgers, verdicts, filled prompt instances, handoffs worth keeping | `docs/ephemeral/`, by pull request |
| operational status, navigation, plan state | Notion — where a destination rule already says so |

**"Not in Notion" does not mean "nowhere".** A development session that produces a report still
writes it to `docs/ephemeral/` and lands it by pull request. What it does not do is additionally
mint a Notion page because the work felt significant.

## What this does not change

- **The register remains the sole selection authority.** Reading it is how selection is resolved.
- **Ecosystem-maintenance work still records its state in Notion**, because that *is* its
  authorized destination — the round-tracking page, the release register, the Alpha feedback list
  and the release controls each have an established destination rule. A `GCFPE-MGMT-10` run or a
  prompt-repair round writing to those pages is authorized by that rule, not by inference.
- **Prompt bodies are still authored and revised in Notion in place**, for the members that are
  Notion-managed. See `prompt-corpus-policy.md`.
- **`AUTH-001` still holds.** A dated record is never corrected in place.

**The line runs between executing the flow and maintaining the ecosystem.** A session executing the
ecosystem flow — planning, implementing, reviewing, QA-ing a work unit — is read-only with respect
to Notion unless told otherwise. A session maintaining the ecosystem itself writes to the
maintenance surfaces that already name it. Neither one may borrow the other's authorization.

## Conflicts identified, not modified

Per the Product Owner's direction, prompts and skills are **not** modified by this amendment. The
following conflict with it and are recorded here for separate later review.

| artifact | the conflicting language | why it conflicts |
|---|---|---|
| **`glow-workspace-currency`** (skill) | *"close every task by writing any state change back to Notion and reading it back before reporting it"* · *"Any state change goes to Notion in the session that produced it"* | States a Notion write as the **default close-out of every task**, which is the exact inference this policy forbids. Its description is always in context, so it applies to every session including development-flow ones. **Highest priority.** |
| **`glow-artifact-storage`** (skill) | *"Prompts are authored and revised directly in Notion"* | True of Notion-managed members; stated without qualification it reads as true of every prompt. Needs the durable-asset carve-out. |
| **`glow-write-boundary`** (skill) | *"A prompt, plan, or state? Notion."* | A routing rule that sends every prompt to Notion, with no category for the five kinds that do not belong there. |

The machine-readable prompt contracts in `docs/graph/parts/` were searched and carry **no**
Notion-write instruction, so the prompt layer does not mandate writes at the contract level. What
any individual prompt body says was not audited, because this amendment is explicitly not a prompt
audit.

## The operational language corrected by this amendment

| document | was | now |
|---|---|---|
| `session-working-rules.md`, *Tracking is part of the work* | "**Every step is tracked in Notion.**" | Scoped to ecosystem-maintenance sessions, with the read-only default stated for development-flow sessions |
| `README.md`, *The architecture* | "Prompt behaviour → Notion, authored in place" | Qualified to durable Notion-managed prompt assets, pointing here |
