---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Prompt Corpus Storage and Fidelity Policy — NON-NEGOTIABLE — 2026-09-21*
---

# Prompt Corpus Storage and Fidelity Policy

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
## What this invalidates, named on the day it was issued
**`SF10-12`**** — the whole content of round 25 — is defective under this policy.** It pins a byte count and SHA-256 for each of the 55 bodies and compares them on every run. That is a raw-file identity check for prompt bodies, and the package is withdrawn rather than repaired. The two blocking findings `SFR-01` raised against it need no repair round; the thing they are findings about does not survive.
**The ****`--prompt-dir`**** mechanism predates round 25 and conflicts with the same clause.** The end-to-end gate and the 181-case body-fixture suite both require a complete local corpus of 55 `.md` files before they will run. That is a mirrored tree, and requiring it is a suggestion that a complete local corpus is needed before work can proceed. It is a Product Owner decision, not a session's, but it is the larger conflict and it should not be discovered again by a third reviewer.
**Two independent reviewers hit this wall before the policy existed.** `SFR-01` declined the 55-body gate in the round-24 review — *"that run would have produced a number, not evidence"* — and declined it again in round 25, *"rebuilding one means hand-transcribing 1.06 MB where a slip is indistinguishable from drift."* The policy is correcting a defect the machinery had already demonstrated twice, not overruling a working practice.
**The accumulation clause is not theoretical.** The session that received this policy was holding **8.37 MB of prompt-body copies across four scratch locations** — one deliberate 55-file corpus and three falsification trees that had each silently carried a full copy. All deleted on receipt. Nobody decided to build a corpus mirror; it arrived by copying a working tree three times.
## The standing test
Before proposing any check, ask what it would catch that matters. A byte-identity check on a Notion page catches a transcription slip in a copy that should not exist. **Prompt meaning, structure, routing, dependencies and operational behaviour are what the ecosystem runs on**, and every one of them is assessable by reading the page.
