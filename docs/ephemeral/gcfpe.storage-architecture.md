---
artifact_type: GCFPE_STORAGE_ARCHITECTURE_REQUIREMENT
artifact_version: "2.0"
created_date: 2026-09-17
last_revised: 2026-09-18
status: BINDING
authority: Product Owner decision, 2026-09-17
applies_to: GCFPE-20260914.1 / 091426.1 / 55 candidate prompts and supporting controls
governing_plan: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1, §4.5
repository: amthorn78/glow-hdengine-v2
runtime_artifact_root: docs/ephemeral
pfcanon_root: docs/pfcanon
graph_parts_root: docs/graph/parts
ecosystem_management_root: docs/prompt_ecosystem_management
baseline: main @ 3c0b1fa (PR #415)
---

# GCFPE storage architecture — repository-first

## The decision

Nathan moved Glow storage into the repository on 2026-09-17.

| Artifact | Destination | Access |
|---|---|---|
| Ephemeral, working, planning file; report, ledger, checkpoint, handoff record, run evidence | `docs/ephemeral/` | read and write, by pull request |
| Maintained machine-readable source — currently the GCFPE graph parts | `docs/graph/` | read and write, by pull request |
| Persistent ecosystem-management infrastructure — registry, decision record, architecture, authoritative-surface map | `docs/prompt_ecosystem_management/` | read and write, by pull request |
| PFCanon | `docs/pfcanon/` | **read only** |
| Prompt, plan, checklist, state, verdict | Notion | authored in place |
| Reusable behaviour | An installed skill | — |
| A file Nathan specifically directs to Drive | Google Drive | by local round trip |

The files of the former Drive folder `Glow / Ephemeral Planning Files` are in
`docs/ephemeral/`, including the current GCFPE record:
`gcfpe.plan.repair-checklist.md`, `gcfpe.batch-1.repair-report.md`,
`gcfpe.batch-1.validation-report.md`, the `gcfpe.batch-2.*` ledgers and report,
and `gcfpe.drainage-removal.repair-report.md`.

**Strengthened 2026-09-18: Google Drive is not a storage authority for this
ecosystem at all.** It is not a default destination and it is not a fallback.
Nathan keeps human reference copies there, including of PFCanon. **Those copies
carry no authority.** Never resolve canon from Drive, and never reconcile a
repository file against a Drive copy to decide which is current. A file goes to
Drive only where Nathan directs that specific file there.

**Derived output is never committed.** The assembled graph contract is built from
`docs/graph/parts/` on demand into the session scratchpad and represented
downstream by its proof token. The committed copy that previously sat at
`docs/ephemeral/gcfpe.r20260914-1.graph-contract.md` was removed on 2026-09-18:
it was a second copy that had drifted from its source and still carried the
retired drainage machinery — 28 references to the removed `NATHAN_MANUAL_PF10_DRAIN`
boundary node, the four-state drain enums, all 55 `pf10_addendum_role` tokens and
the superseded `CL-20` title. A session reading it would have rebuilt exactly what
the repair retired.

Every other path in the repository remains off limits without Nathan's explicit
instruction for that specific change. Nathan alone merges.

The `glow-artifact-storage`, `glow-write-boundary` and `glow-workspace-currency`
skills are updated to this, including the fourth open path
`docs/prompt_ecosystem_management/` and the stronger no-Drive-authority rule.

This document exists because the **prompts are not yet**, and a prompt that still
routes an artifact to Drive will send a runtime session to the wrong place.

**Remaining work as of the merged baseline**, measured against the live prompt
bodies: **44 of 55 prompts** still name `Glow / Ephemeral Planning Files` or a
direct Drive link as the artifact destination, and **39 of 55** still resolve
PFCanon by walking `Glow / Core Docs / PFCanon` in Drive rather than reading
`docs/pfcanon/`. Three carry both conventions. The 11 Batch 1 prompts are already
converted and are the wording to converge on — repository paths throughout, with
the single conditional Drive sentence retained. This is one controlled
cross-cutting pass, not batch-local work.

## Why the repository, specifically

The Drive connector has no content-write for an existing file ID. A replacement
must be created new and the old one trashed, and the body travels through a
tool-call parameter generated token by token. That path is reliable to roughly
20–30 KB, impossible much above 150 KB, and its characteristic failure is a
dropped trailing newline — which changes the hash, is invisible in any renderer,
and has happened twice independently from the same source file.

Git has none of that. It reads bytes off disk. The 583,125-byte rebuilt graph
that blocked Batch 1 as R2 is a non-event here.

## The defect class: `STORAGE_ARCHITECTURE`

The 55 candidate prompt bodies were written against the old architecture and
carry clauses that now contradict it. Repairing them is in scope for each
prompt's own batch, under the per-prompt checklist in §5 of the plan. It creates
no seventh batch and no new gate.

### What must change in a prompt

| Contradicting clause | Repaired to |
|---|---|
| `EPHEMERAL_DRIVE` as an artifact disposition | `docs/ephemeral/`, authored in place, landed by pull request |
| "save … in `Glow / Ephemeral Planning Files`" | "write … under `docs/ephemeral/`" |
| "fetch it back completely and retain the direct Drive link" | "commit and push it on the batch branch; reference it by repository path" |
| "referenced by direct Drive link" | "referenced by repository path" |
| canon resolved through `Glow / Core Docs / PFCanon` | canon read from `docs/pfcanon/`, read-only |
| "Markdown files in Drive `Glow / Core Docs / PFCanon`" | `docs/pfcanon/` |
| any implication that repository writes are forbidden outright | the three open paths above, everything else by explicit instruction |

### What must not change

- **The Markdown-only rule stands.** Google Docs, `.doc` and `.docx` PFCanon
  variants must still never be opened, inspected, compared, cited, or used as
  fallback. The source moved; the format rule did not.
- **Drive is not deleted from the prompts — it is narrowed.** A prompt may still
  name Drive, but only for the case where Nathan directs a specific file there,
  and it must say so conditionally.
- **Do not hardcode canon, skill-owned mechanics, or a release token into a
  prompt body.** Prompts name the destination class — `docs/ephemeral/`,
  `docs/pfcanon/` — and let the referenced canon and the installed skills own
  the rest. Drive naming, resolution and replacement mechanics belong in
  `glow-artifact-storage`, not restated in 55 places.
- **No re-authoring beyond the storage, source-resolution and reference
  clauses.** This is a bounded repair, not an excuse to rewrite a prompt.

## Per-batch obligation

Before repairing, each batch searches its own prompts for:

    Drive                      ← primary term, case-sensitive, bare word
    EPHEMERAL_DRIVE
    Ephemeral Planning Files
    Core Docs / PFCanon
    drive.google.com
    direct Drive link

**The bare `Drive` is the primary term and the other five are secondary.** A
phrase-only survey provably walks past real clauses: the graph's
`handoff_contract.required[3]` read *"direct Drive artifacts and repository/PR
references"* and matched none of the five phrases below it. Search the bare word
first, then the phrases to catch what a case-sensitive word search misses.

Every hit is recorded in the batch contract ledger under finding class
`STORAGE_ARCHITECTURE`, and closed or blocked explicitly. None may be silently
skipped. A prompt already repaired in an earlier batch that still carries one of
these returns to its owning batch ledger under §6.9 of the plan.

### Lineage is evidence, not routing — never "close" it

A `Drive` hit inside a **source binding** is not a storage defect and must not be
repaired, repointed, or closed. A source binding is any record of what a run
actually resolved and read: an entry carrying a hash, a `retrieved_at` stamp, or
an equivalent capture of a resolved identity at a point in time.

`docs/graph/parts/global.json` holds eleven such `drive.google.com` URLs under
`source_bindings`, nine of them stamped with `retrieved_at` and `sha256`. They
are a pinned historical capture. **Rewriting them destroys the evidence of what
was read and proves nothing about current storage.**

The distinction matches PF10, addendum *Specification format authority*: a
routing reference points a reader at current canon and carries no version; a
use or provenance record retains the exact resolved identity of what was
actually read. This survey repairs routing. It never edits provenance.

Record such a hit in the ledger as `STORAGE_ARCHITECTURE / LINEAGE_PRESERVED`
with no edit, so the survey is complete without the record being damaged.

## Known affected surfaces

Established by workspace search on 2026-09-17. This is a scope pointer, not an
exhaustive inventory — each batch runs its own survey.

**Candidate prompt bodies** under `GCFPE-20260914.1 — 091426.1`, in the
directories `HDE Change Flow`, `HDE IA`, `HDE TW`, `HDE QA`, `HDE PR` and
`Escalation`. Confirmed instances include `IA-60`, `UTIL-10`, `PR-50`,
`CF-C-10`, `CF-E-30` and `GCFPE-MGMT-10`; the clause pattern is boilerplate and
is expected in most of the 55.

**Supporting controls**, carried by §9 synchronization rather than by prompt
repair:

- Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1
- GCFPE Alpha Establishment and Change Management Checklist — 091426.1
- the family hub pages `HDE IA`, `HDE TW`, `HDE QA`, `Escalation`
- Glow Prompt Repair Execution-Surface and Artifact-Storage Policy — 20260902
- GCFPE — Epic Alpha Run Notes — HDE-EPIC040

Archived prompt versions under `04 Archived Prompt Versions` carry the same
clauses and are **not** repaired. They are history.

**Already corrected in this repository**, not left to a batch:
`GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0` and
`GCFPE-Per-Batch-Execution-Model-v1.0-20260916.md` still describe Drive routing
where they were imported unchanged; the execution-model document's chat-session
assumption is corrected here, its storage clauses are not. Treat both as
historical text except where this document or the plan says otherwise.

## Consequence for the two-pass execution model

Both passes run in Claude Code. Nathan does not use chat sessions, so the §6A
seam is a context budget rather than a capability boundary — Pass 1 is many
small targeted reads and writes against individual prompt pages in Notion, Pass
2 is whole-batch reconciliation, and running both in one session is what
exhausted Batch 2.

Pass 1 writes its own ledgers under `docs/ephemeral/`, opens the batch branch
and the pull request, and there is no ledger handoff between passes. Pass 2
commits onto the same branch and the same pull request. One branch, one PR, one
verdict per batch.

The graph is no longer a driver of the split either: it is held as parts in
`docs/graph/parts/` and rebuilt by script, so no pass loads a 570 KB file.

## Open items this closes

- **Batch 1, R2** — the rebuilt candidate graph exceeding the Drive connector
  ceiling. The graph parts are in `docs/graph/parts/` and the assembled graph is
  derived output that is never committed. There is nothing left to persist to
  Drive, so R2 no longer has a subject.

`R1` — the undeclared `SPECIFICATION_DELTA` schema — is unaffected by this
change and remains open.
