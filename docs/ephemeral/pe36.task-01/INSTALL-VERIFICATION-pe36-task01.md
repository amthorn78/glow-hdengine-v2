---
artifact_type: SKILL_INSTALL_VERIFICATION_AND_DISPOSITION
artifact_version: "1.0"
created_date: 2026-09-22
session: PE36
task: docs/ephemeral/pe36.task-01/TASK-01-skill-write-boundary-revision.md
verdict_record: docs/ephemeral/pe36.task-01/SECTION-10-REVIEW-pe36-task01.md
successor_to: nothing corrected in place — this record is added beside the report and the verdict (AUTH-001)
status: INSTALLED_AND_VERIFIED
---

# PE36 Task 01 — install verified, and the two observations disposed of

**Task 01 is complete.** The §10 verdict returned `SKILL_FIT_CONFIRMED` for all three packages
with no findings, Nathan installed them, and the installed trees measure the digests the verdict
named.

## The install verification — the control this ecosystem exists to run

`skill-identity-and-freeze.md`: *"An install is complete when the installed tree measures the
digest the §10 verdict named. Not when the gates come back green."* Measured by PE36 after the
install, `freeze.py` rooted at each skill directory:

| skill | digest the verdict named | installed tree measures | |
|---|---|---|---|
| `glow-workspace-currency` | `3 5f2b4ae0d43f0609ae3c3b88409a2578791b008cf6908bd6516181688e06dd93` | same | **MATCH** |
| `glow-artifact-storage` | `1 502b4ecf11cea156702207ddb829b2d51064fe9eaa8678ac5db05c04375cba1c` | same | **MATCH** |
| `glow-write-boundary` | `1 662f9647ccfd996aa72e3d80ac70edc3d06a4310805ef14207b1340c69e93fc4` | same | **MATCH** |
| `change-flow` | `21 80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8` | same | **MATCH — unchanged** |
| `flowmaster-validate` | `29 b9ca212ac1275f16af12d34ad15d3df6e95fc71a95f2ce1ab56ee7245a3317af` | same | **MATCH — unchanged** |

Every skill the change touched **and every skill it deliberately did not.** The synced tree is
318 files, the same count the reviewer pinned before and after review.

The revised text is live, not merely the digest: `Only durable, Notion-managed prompts` in
`glow-artifact-storage`, `at the destination that holds it` and two occurrences of
`Where it lands` in `glow-workspace-currency`, and `A prompt that belongs` in its
`references/notion-operations.md`.

### The state claim that was stale, and how it was caught

The verdict record states *"Nothing was installed: the three installed digests at the end of
review are still the §3 baselines."* **That was true when the reviewer measured it and was not
true when PE36 next measured.** The install happened between the two measurements.

Nothing was wrong with the verdict; a dated record correctly recorded the state at its own
moment. It is noted here only because carrying that sentence forward into a report — instead of
re-measuring — is exactly the failure mode the succession record names: *a claim made before the
cheap measurement that would have checked it.* The measurement was one command.

## Verdict, recorded

`SKILL_FIT_CONFIRMED` ×3, author `SFR-PE36-T01`, bound to the three `.skill` sha256 values and
the three extracted-tree digests, **void for any other bytes**. No findings. Evidence read on
`main` @ `e8dc5e4` because PR #461 merged mid-review and its branch was deleted.

The reviewer contradicted none of the eight published measurements, and independently ran the
`Q2` sweep this round had deferred.

## Observation 1 — the asymmetric safe default. **Open, and it is Nathan's call.**

`A session that cannot tell which kind it is treats itself as executing.` fully prevents a
wrongful Notion write. It does not, by itself, prevent a maintenance session that misclassifies
itself from leaving a Notion maintenance surface stale — which is the failure class
`glow-workspace-currency` was written for. The reviewer confirmed the skill **does** close this,
through the unchanged Consult step, but across a section boundary.

**The reviewer's suggested correction, recorded verbatim so it need not be re-derived** — one
trailing clause on that sentence, in a body section and not the description, so it does not touch
the trigger surface:

> …and if the Consult step found a Notion surface that already names your item, that surface is a
> destination rule and the record belongs there too.

**PE36's recommendation: do not take it now; carry it.** Any byte change voids a clean
`SKILL_FIT_CONFIRMED` and costs a full independent review round for one clause that hardens a gap
already closed elsewhere in the same skill. `skill-packaging-and-delivery.md` is explicit:
*"batch small corrections into one change rather than shipping them one at a time. Three separate
one-line fixes cost three independent reviews; one change carrying all three costs one."*

This is **not** parked as "non-blocking" (`DISP-001`). It is a named item with recorded text, a
recommendation, and a trigger: **apply it in the next change that touches
`glow-workspace-currency` for any other reason.** If no such change arrives, it stays as recorded
here and in the succession record, and costs nothing.

## Observation 2 — the provenance nit. **Confirmed, and resolved here.**

The reviewer is right. `REVIEWER-PROMPT-pe36-task01.md` §5 reads *"The authority, quoted verbatim
from notion-write-boundary.md's record of the Product Owner's policy: … And, authorizing this
round: 'I do want a skill revision then. Pass that over to the new session as the first task'."*

The first quotation is verbatim in `notion-write-boundary.md`. **The second is not in that file.**
Verified by grep: it appears in exactly two places in the repository — that reviewer prompt, and
`TASK-01-skill-write-boundary-revision.md`'s `authorized_by` frontmatter, which is its real
source. The authority is genuine and correctly recorded; only the citation is wrong, and the
sentence structure attributes both quotations to one file.

**The reviewer prompt is not corrected in place.** It is a dated record and it is what the
reviewer actually worked from (`AUTH-001`). This entry is the successor beside it. A future
session using that prompt as the template's worked example should take the correction from here.

Affected nothing under review and does not touch the verdict.

## Q2 — closed

The round deferred a sweep for a fifth instance of the unqualified *"prompts are authored and
revised directly in Notion"* sentence. The reviewer ran it across the other 24 installed skills
rather than accepting the stated incompleteness: **no fifth instance**, and `change-flow` is
already aligned. Nothing remains open unless a sweep is wanted on a surface wider than the
installed skills, which nobody has asked for.

## What is now true

- The three skills are installed, verified by digest, and their revised behaviour is live.
- `notion-write-boundary.md`'s conflicts table is updated from *awaiting review* to installed.
- `D19` is recorded, with its consequence in `skill-identity-and-freeze.md`.
- No Notion write was made at any point in this task, by PE36 or by the reviewer. Searched again
  after the install: no Notion page records this task's state, so nothing there went stale. The
  policy's own routing table sends verdicts to `docs/ephemeral/`, and that is where they went.
