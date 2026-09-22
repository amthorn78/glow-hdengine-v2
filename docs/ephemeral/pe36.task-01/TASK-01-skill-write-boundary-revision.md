---
artifact_type: PE_SESSION_TASK_BRIEF
artifact_version: "1.0"
created_date: 2026-09-22
status: AUTHORIZED_NOT_STARTED
assigned_to: PE36
authorized_by: Product Owner, 2026-09-22 — "I do want a skill revision then. Pass that over to the new session as the first task"
authority_document: docs/prompt_ecosystem_management/notion-write-boundary.md
scope: three installed skills. No prompt body. No contract, graph or registry change.
---

# PE36 Task 01 — bring three skills into line with the Notion write boundary

**This is PE36's first task and it is authorized.** It supersedes the succession record's
statement that the queue is empty; that was true when written and stopped being true the same day.

## Why this exists

`notion-write-boundary.md` became binding on 2026-09-22. The operational documentation and the
Operations Hub were corrected the same day. **The skills were deliberately not touched**, because
the instruction that created the policy said not to touch them.

That leaves a gap with a sharp edge: **the documentation says the new thing and the skills say the
old thing, and skills are what actually load into a session.** Until this lands, a session will be
instructed to close out by writing to Notion no matter what the policy says.

## The three conflicts, quoted

### 1. `glow-workspace-currency` — the serious one

| where | text |
|---|---|
| description (**always in context**) | *"close every task by writing any state change back to Notion and reading it back before reporting it"* |
| The three obligations | *"**Record what changed.** Any state change goes to Notion in the session that produced it."* |
| §2 *Record — what counts as a state change* | *"Write to Notion, in the session that produced it, when any of these happen:"* followed by six triggers |

It is the serious one for two reasons. Its description is in context for **every** session, so it
reaches development-flow sessions that should be read-only. And §2's six triggers are exactly the
inferences the policy forbids — "a task stops early, is abandoned, or is handed to another session"
is a handoff, and a handoff is explicitly not an authorization.

### 2. `glow-artifact-storage`

Description: *"Prompts are authored and revised directly in Notion."* True of the durable,
Notion-managed members; stated without qualification it reads as true of every prompt, including
the five categories that do not belong there.

### 3. `glow-write-boundary`

Routing rule: *"**A prompt, plan, or state?** Notion."* One line, no category for a one-off,
handoff, correction, recovery or development-flow prompt.

## The design principle — do not gut the skill you are fixing

**`glow-workspace-currency` earned its existence.** It was written after stale state survived and
cost real cycles: 101 checklist boxes unchecked against 11 checked, a `status`/`gate` header twenty
rounds stale, and `D5` landing in round 21 without ever being written down, which made a later
session report a completed item to the Product Owner as a loose end.

So the correction is **not** "record less".

> **The obligation stays absolute. The destination becomes conditional.**
>
> Every state change is still recorded, in the session that produced it, and still read back before
> it is claimed. **Where** it is recorded depends on which kind of session you are.

| session | destination |
|---|---|
| **Maintaining the ecosystem** — a `GCFPE-MGMT-10` run, a prompt-repair round, a release transaction | Notion, on the surfaces that already name it: round-tracking page, release register, Alpha feedback list, release controls. Authorized **by rule**. Plus the repository. |
| **Executing the ecosystem flow** — planning, implementing, reviewing, QA-ing a work unit | `docs/ephemeral/`, landed by pull request. **Read-only toward Notion** unless that task's instruction directs a write. |

This is already the wording in `session-working-rules.md` and in the Hub's *Tracking is part of the
work*. **Match it.** Three surfaces saying the same thing in three different ways is how this
ecosystem generates defects.

A session that cannot tell which kind it is should treat itself as **executing**, not maintaining.
The read-only posture is the safe default, and the policy says so.

## What to change, and what not to

| do | do not |
|---|---|
| Scope the destination by session kind | Remove the record-what-changed obligation |
| Add the five excluded prompt categories to the routing rules | Weaken "verify before you claim" |
| State the read-only default explicitly | Rewrite §2's six triggers out of existence — they are correct about *what counts as a state change*, only wrong about *where it lands unconditionally* |
| Point at `notion-write-boundary.md` as the authority | Add a fourth restatement of the policy text; cite it |

**No prompt body. No contract, graph or registry change. No new skill.**

## The risk worth naming before you start

**Changing `glow-workspace-currency`'s description changes its triggering**, and `AF-003` records
that skill triggering is probabilistic, that `skill-creator`'s optimizer may measure slash-command
invocation rather than skill routing, and that four very different descriptions scored 1–2/10 —
i.e. possibly selecting on noise.

So: change the description **minimally**, preserve the trigger surface (the task words that make it
fire), and **do not chase a trigger-rate number**. The skill must still fire on exactly what it
fires on today; only what it then instructs should change. If a description edit is not strictly
required to fix the conflict, do not make one.

These three skills are load-bearing for every Glow session. **A botched revision is worse than the
conflict it fixes.**

## Procedure

`skill-packaging-and-delivery.md` and `skill-identity-and-freeze.md` govern. In brief:

1. **Never write to the synced skills directory.** Copy to scratch; run everything with
   `PYTHONDONTWRITEBYTECODE=1`.
2. Baseline first — `freeze.py` rooted at each **skill directory**, never the synced tree. Record
   the three baseline digests before changing a byte.
3. Revise. These are prose skills with no validator of their own, so the check is a careful read
   plus a diff, not a gate. Say so plainly rather than implying a gate ran.
4. **Advertised identity must be unspent.** Bump each skill's own version, and diff the advertised
   values against the previous package before packaging. A match is a defect. This rule has been
   broken three times, twice in the file that states it.
5. Package `.skill` files. Filename carries no version, so **lead the delivery caption with the
   sha256**, one package per line, and give file count and byte size.
6. **Independent §10 review is mandatory before install**, using `reviewer-prompt-template.md`.
   Fill every slot. Pin the reviewer to the **branch HEAD**, and say what to do if the branch has
   already merged and been deleted — that happened two rounds running.
7. Hand the files to Nathan. **Only Nathan installs, and only Nathan merges.** An install is
   complete when the installed tree measures the digest the verdict named — not when anything comes
   back green.

## Definition of done

- Three revised `.skill` packages delivered to Nathan with their digests.
- A filled reviewer prompt delivered in the same message.
- An independent §10 verdict of `SKILL_FIT_CONFIRMED` bound to those exact digests.
- The conflicts table in `notion-write-boundary.md` updated to record the disposition — it
  currently names all three as open.
- Nothing installed by PE36.

## Out of scope

`AF-001`–`AF-004`, the reconciliation backlog, `HDE-EPIC040`, the selected release's prompt bodies,
and any other skill. If a fourth skill turns out to conflict, **report it, do not fold it in.**
