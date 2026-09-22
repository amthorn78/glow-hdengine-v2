---
artifact_type: LINEAGE_MIGRATION_TRANSITION_REFERENCE
artifact_id: HDE-EPIC040-LINEAGE-MIGRATION-TRANSITION-REFERENCE
artifact_version: "1.0"
artifact_state: COMPLETE
change_class: EPIC
change_id: HDE-EPIC040
scope: The seven PR-10 lineage inputs listed below, and nothing else
created_date_utc: 2026-09-21
authority: Product Owner instruction, 2026-09-21
verdict: PR-10 MAY PROCEED using these migrated artifacts as its lineage inputs
---

# HDE-EPIC040 — lineage migration transition reference

**PR-10 may proceed.** All seven required lineage inputs are present at their exact filenames, and
each one's readable contents identify it as the claimed artifact. No material ambiguity, missing
file or conflicting identity was found within this scope.

## What happened to these artifacts

`HDE-EPIC040` was implemented through the prior ChatGPT-based prompt ecosystem, with its artifacts
stored in Google Drive. PR01, PR02 and PR03 completed under that system. Those artifacts have been
transferred into this repository's ephemeral artifact location, `docs/ephemeral/`.

**The contents and filenames were preserved. Platform-specific metadata was not, and was not meant
to be.** Google Drive file IDs and links, ChatGPT Library `libfile_` identifiers, folder paths,
created and modified timestamps, and ownership details all belong to the storage layer that was
left behind. **Changed storage metadata here is the expected result of the migration, not evidence
of broken lineage.**

## The continuity mechanism

**The stable filename plus the readable artifact body.** Each artifact states its own
`artifact_type`, logical identity, version and state in its own text. That self-declared identity
travelled with the file and is what a receiving agent resolves against.

It is not the only thing that travelled. Several artifacts carry **SHA-256 values for their own
inputs**, recorded at authoring time — content identity that is independent of any storage system.
Where such a pin exists it can be checked directly, and one was.

## Bounded inspection — the seven required inputs

Present, and identified by their own readable contents:

| Prompt input | Exact filename | Declared identity in the body | Bytes |
|---|---|---|---|
| Required predecessor acceptance | `HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` | `PR_WORK_UNIT_LINEAGE_REVIEW` · `HDE-EPIC040-PR03-PR-WORK-UNIT-LINEAGE-REVIEW` v1.0 · `COMPLETE` · **`decision: ACCEPT`** | 15,112 |
| Approved Specification base | `HDE-EPIC040-specification-v1.1-approved.md` | `SPECIFICATION` · `HDE-EPIC040-SPECIFICATION` v1.1 · **`SPECIFICATION_APPROVED`** | 64,553 |
| Implementation Audit base | `HDE-EPIC040-implementation-audit-v2.0.md` | `IMPLEMENTATION_AUDIT` · `HDE-EPIC040-IMPLEMENTATION-AUDIT` v2.0 · **`AUDIT_COMPLETE`** | 33,103 |
| Immutable whole-change Plan | `HDE-EPIC040-implementation-plan-v2.1.md` | `IMPLEMENTATION_PLAN` · `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1 · `PLAN_PENDING_REVISED` — **see note 1** | 146,624 |
| Approving Plan Review | `HDE-EPIC040-implementation-plan-review-v2.1.md` | `IMPLEMENTATION_PLAN_REVIEW` · `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1 · **`decision: APPROVE`** | 32,843 |
| Accepted dependency lineage: PR01 | `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md` | `PR_WORK_UNIT_LINEAGE_REVIEW` · `HDE-EPIC040-PR01-PR-WORK-UNIT-LINEAGE-REVIEW` v1.1 · **`Decision: ACCEPT`** | 15,755 |
| Accepted dependency lineage: PR02 | `HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` | `PR_WORK_UNIT_LINEAGE_REVIEW` · `HDE-EPIC040-PR02-PR-WORK-UNIT-LINEAGE-REVIEW` v1.0 · `COMPLETE` · **`decision: ACCEPT`** | 13,195 |

**7 of 7 present. 7 of 7 self-identify as the claimed artifact.**

### One input is provable, not merely identifiable

The approving Plan Review declares the exact bytes it approved:

> `Exact approved bytes | 146,624 bytes; 985 LF-terminated lines; SHA-256 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`

The migrated Plan file measures **146,624 bytes, 985 LF-terminated lines, SHA-256
`10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`** — an exact match on all three.

**The immutable whole-change Plan is therefore the same artifact that was approved, proven from
inside the migrated set, with no reference to any storage system.** That is the most load-bearing
input in the chain. The other six rest on readable identity, which is the agreed mechanism and is
sufficient; only this one could be checked more strongly, because only this one is pinned by a
sibling in the set.

## Notes for the receiving agent

**1. The Plan's own header says `PLAN_PENDING_REVISED`. That is correct and is not a problem.**
An artifact records its state at authoring, before review. The approval lives in the separate
`HDE-EPIC040-implementation-plan-review-v2.1.md`, which is `decision: APPROVE` and binds the exact
bytes above. **Read the pair.** The Plan alone will look unapproved; it is not.

**2. The PR03 handoff names PR-10 at prompt version `091326.2`. That version is archived.**
`GCFPE-20260913.1 / 091326.2` was superseded on 2026-09-21 by `GCFPE-20260914.1 / 091426.1 / 55`,
and its prompt pages were moved to *04 Archived Prompt Versions*. **Resolve `PR-10 — Create PR
Work-Unit Instructions` at `091426.1` from the GCFPE Membership and Release Register**, which is
the sole selection authority. The embedded `091326.2` reference is preserved historical lineage,
not a routing instruction. This is a stale *prompt* pointer, not a defect in the *artifact*
lineage.

**3. Dead prior-platform pointers inside the bodies are provenance, not inputs.** Across the seven
artifacts there are roughly **105 `libfile_…` ChatGPT Library identifiers** and **37
`drive.google.com` links**. None of them resolve. None of them needs to: every one names an
artifact that either is in the list above or is historical evidence outside PR-10's inputs.
**Do not attempt to resolve, reconstruct or repair them, and do not treat one as a blocker.**

**4. Two near-neighbour files exist that must not be cited instead.**

| present in the directory | why it is not the input |
|---|---|
| `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.0.md` | the **v1.0** predecessor, which the v1.1 body records as truthfully `PENDING` and preserved as historical evidence. The required input is **v1.1** |
| `HDE-EPIC040-implementation-plan-review-v2.1 (1).md` | a migration-duplicate filename. **Verified byte-identical** to the canonical file, so it carries no conflicting identity — but cite the canonical name |

The same byte-identical duplicate exists for `…-implementation-plan-review-v2.0`, which is outside
this input set in any case. No duplicate was found that *differs* from its canonical file.

## What was not done

No prompt-ecosystem audit, corpus validation, semantic screen or broad provenance exercise. No
Drive metadata was reconstructed. No byte-level fidelity check was run beyond the single
self-contained one the artifacts themselves made available. **No listed source artifact was
modified.** PR-10 was not started.

## Verdict

**The filenames and readable document identities are sufficient for the PR-10 agent to identify
and use the correct lineage artifacts.** This page is the continuity record for that migration.

The three notes above are identification guidance, not unresolved facts. Nothing in this scope
requires an additional reference or clarification.

---

## Paste-ready note for the PR-10 kickoff

> **Lineage-migration context — read before resolving inputs.**
>
> Your seven lineage inputs were produced under the prior ChatGPT/Google Drive workflow and have
> been migrated into `docs/ephemeral/` in `amthorn78/glow-hdengine-v2`. Contents and filenames are
> preserved; **storage metadata is not, deliberately.** Google Drive IDs and links, `libfile_…`
> ChatGPT Library identifiers, paths, timestamps and ownership all belong to the system that was
> left behind. **Changed storage metadata is the expected result of the migration. Do not treat it
> as broken lineage, and do not try to reconstruct it.**
>
> Resolve each input by its **exact filename and the identity its own body declares**. All seven
> were confirmed present and self-identifying on 2026-09-21; see
> `docs/ephemeral/HDE-EPIC040-lineage-migration-transition-reference-v1.0.md`.
>
> Three things to know:
> 1. `HDE-EPIC040-implementation-plan-v2.1.md` states `PLAN_PENDING_REVISED` in its own header.
>    That is its authoring state. The approval is in `HDE-EPIC040-implementation-plan-review-v2.1.md`
>    (`decision: APPROVE`), which pins the Plan's exact bytes — and the migrated file reproduces
>    them exactly. **Read the pair; the Plan is approved.**
> 2. The PR03 acceptance hands off to `PR-10` at prompt version **`091326.2`, which is archived**.
>    Resolve `PR-10 — Create PR Work-Unit Instructions` at **`091426.1`** from the GCFPE Membership
>    and Release Register, the sole selection authority.
> 3. Use `HDE-EPIC040-PR01-pr-work-unit-lineage-review-**v1.1**.md`. A `v1.0` is also present and
>    is the superseded `PENDING` predecessor, preserved as historical evidence.
>
> `HDE-EPIC040-PR03` is `ACCEPTED_FINAL`. PR04 is the next planned unit and its PR-10
> instruction-authoring stage may begin. This carries no Proceed, merge, PF10 or implementation
> authority.
