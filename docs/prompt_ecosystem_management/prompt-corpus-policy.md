---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.1"
created_date: 2026-09-21
revised_date: 2026-09-23 — D22, a transient tool file is part of a read
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Prompt Corpus Storage and Fidelity Policy — NON-NEGOTIABLE — 2026-09-21*
---

# Prompt Corpus Storage and Fidelity Policy

> **Amended 2026-09-23 by `D22`.** The directive below is preserved as issued. Where it reads as
> forbidding every byte of a body on disk, see *Amendment — transient files are part of a read*
> at the end of this document: a file the tooling makes in order to read a body is allowed
> under five conditions. Everything else the directive prohibits stays prohibited.

The Product Owner's policy, recorded verbatim, with what it invalidated on the day it was issued.
**It is permanent unless Nathan explicitly changes it.** Where any procedure, skill, validator or
plan conflicts with it, that element is defective.

Product Owner directive, 2026-09-21. **Permanent unless Nathan explicitly changes it.** Recorded verbatim; the commentary that follows is separate and subordinate.
> The prompt ecosystem is authored and maintained in Notion. It is not an application source repository and does not require repository-style byte fidelity.
>
> Do not create, propose, require, or normalize any procedure that transcribes, exports, mirrors, snapshots, caches, hashes, or otherwise copies the complete prompt corpus to local disk, a repository, or any parallel storage location.
>
> This prohibition includes, without limitation:
>
> - whole-corpus Markdown or JSON exports;
> - local prompt directories or mirrored trees;
> - byte-for-byte comparisons, hashes, or raw-file identity checks for prompt bodies;
> - corpus backup copies created for validation, review, testing, or audit;
> - suggestions that a complete local corpus is needed before work can proceed.
>
> The readable Notion content is the operative source for prompt analysis, review, validation, maintenance, and repair. If a task requires examining prompts, read the relevant Notion pages directly and use that available content as sufficient evidence.
>
> Validation should assess the things that actually matter for this ecosystem: prompt meaning, required structure, routing, dependencies, instructions, records, and operational behavior. It must not impose software-repository standards of raw-byte identity where those standards do not serve the work.
>
> An agent may retain only the minimum task-specific evidence needed for its immediate report or approved artifact. It must not turn that into a corpus mirror by accumulation.
>
> If an existing skill, prompt, validator, plan, or proposed repair conflicts with this policy, treat that element as defective. Do not work around the policy by creating a "temporary" or "read-only" corpus copy. Revise the procedure so it works from Notion directly, or clearly report the genuine limitation to Nathan before proceeding.
>
> This policy is permanent unless Nathan explicitly changes it.
## Reading is not restricted. Copying is.

**Product Owner, 2026-09-21:** *"you should not be forbidden to read them that is stupid. I just
don't want them copied to disk. How will you ever do any work if you cannot read them"*

The directive above already says this — *"read the relevant Notion pages directly and use that
available content as sufficient evidence"* — but it was misread once, so it is now stated
separately and in the plainest terms available:

| | |
|---|---|
| **Prohibited** | persisting, mirroring, exporting, hashing, byte-comparing, backing up, or accumulating prompt bodies anywhere outside Notion. A transient file made in order to read a body is part of the read, not persistence, under the five conditions in the amendment below (`D22`) |
| **Not restricted at all** | reading prompts. One, three, all fifty-five. As many as the work needs, as often as the work needs |

**There is no cap on how many prompts a session may read.** A whole-corpus read is a cost
decision, never a permission question. If a session needs to read every prompt to do the work,
it reads every prompt — into context, never into a store.

### The misreading this exists to prevent

A session conflated this policy with the separate **source-read minimalism** rule in
`session-working-rules.md` — an efficiency rule whose subject is *method*, about not routing bulk
through context when a *tool* needs the files — and concluded it was forbidden to read the corpus.
It then shipped a verification with a hole in it and told the Product Owner the policy required
the hole. The policy required no such thing.

**Keep the two apart:**

- **This policy governs storage.** Its one exception is the transient read file in the amendment
  below, and it says nothing about how much may be read.
- **Source-read minimalism governs method and cost.** It is subordinate to the work. It never
  forbids a read, and "this would be expensive" is never "this is not allowed."

When they appear to conflict over prompt bodies, this policy wins on storage and the work wins on
reading. Neither of them makes reading a prompt a thing that needs authorising.

## What this invalidates, named on the day it was issued
**`SF10-12`**** — the whole content of round 25 — is defective under this policy.** It pins a byte count and SHA-256 for each of the 55 bodies and compares them on every run. That is a raw-file identity check for prompt bodies, and the package is withdrawn rather than repaired. The two blocking findings `SFR-01` raised against it need no repair round; the thing they are findings about does not survive.
**The ****`--prompt-dir`**** mechanism predates round 25 and conflicts with the same clause.** The end-to-end gate and the 181-case body-fixture suite both require a complete local corpus of 55 `.md` files before they will run. That is a mirrored tree, and requiring it is a suggestion that a complete local corpus is needed before work can proceed. It is a Product Owner decision, not a session's, but it is the larger conflict and it should not be discovered again by a third reviewer.
**Two independent reviewers hit this wall before the policy existed.** `SFR-01` declined the 55-body gate in the round-24 review — *"that run would have produced a number, not evidence"* — and declined it again in round 25, *"rebuilding one means hand-transcribing 1.06 MB where a slip is indistinguishable from drift."* The policy is correcting a defect the machinery had already demonstrated twice, not overruling a working practice.
**The accumulation clause is not theoretical.** The session that received this policy was holding **8.37 MB of prompt-body copies across four scratch locations** — one deliberate 55-file corpus and three falsification trees that had each silently carried a full copy. All deleted on receipt. Nobody decided to build a corpus mirror; it arrived by copying a working tree three times.
## The standing test
Before proposing any check, ask what it would catch that matters. A byte-identity check on a Notion page catches a transcription slip in a copy that should not exist. **Prompt meaning, structure, routing, dependencies and operational behaviour are what the ecosystem runs on**, and every one of them is assessable by reading the page.

## Amendment — transient files are part of a read (`D22`, 2026-09-23)

**Product Owner, 2026-09-23:** *"allow save to disk, and re-write the rule where needed so it is
rationally conditional and not automatic."*

**The test is what a file is for, not where the bytes happen to sit.** The directive's target is
a parallel corpus, meaning something that can drift from Notion and then be believed. A file the
tooling makes because that is how it delivers or consumes the body is not that. For example, the
harness saves any tool result above roughly 30 KB to a session file, and thirteen bodies are over
that size. A scratch file can also feed `--bodies-stdin`.

**Allowed, when all five hold:**

1. **Outside the repository**, and outside any shared, synced or uploaded store.
2. **For the read or check in hand only.** It is never a source for later work; the next read
   goes back to Notion.
3. **Never an identity.** Not hashed, not byte-compared, not cited as the body.
4. **Deleted** when that read or check is done, and at the latest when the task ends.
5. **Disclosed** in the session's report: which bodies, and that the files were deleted.

**Still prohibited, without exception:** mirrors, exports, snapshots, backups, a cache reused
across tasks or sessions, a committed or uploaded body, accumulation into a corpus, body hashes
or byte comparison, and any procedure that requires a local corpus before work can proceed.

**What this does not change.** Reading remains unrestricted. Byte fidelity remains the wrong
standard for this ecosystem (*The standing test*, above). The validator keeps `--bodies-stdin` and
gains no path option, because a path option invites a standing directory.

