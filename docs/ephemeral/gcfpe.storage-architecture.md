---
artifact_type: GCFPE_STORAGE_ARCHITECTURE_REQUIREMENT
artifact_version: "1.0"
created_date: 2026-09-17
status: BINDING
authority: Product Owner decision, 2026-09-17
applies_to: GCFPE-20260914.1 / 091426.1 / 55 candidate prompts and supporting controls
governing_plan: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1, §4.5
repository: amthorn78/glow-hdengine-v2
runtime_artifact_root: docs/ephemeral
pfcanon_root: docs/pfcanon
graph_parts_root: docs/graph/parts
---

# GCFPE storage architecture — repository-first

## The decision

Nathan moved Glow storage into the repository on 2026-09-17.

| Artifact | Destination | Access |
|---|---|---|
| Ephemeral, working, planning file; report, ledger, checkpoint, handoff record, run evidence | `docs/ephemeral/` | read and write, by pull request |
| Maintained machine-readable source — currently the GCFPE graph parts | `docs/graph/` | read and write, by pull request |
| PFCanon | `docs/pfcanon/` | **read only** |
| Prompt, plan, checklist, state, verdict | Notion | authored in place |
| Reusable behaviour | An installed skill | — |
| A file Nathan specifically directs to Drive | Google Drive | by local round trip |

Google Drive is no longer a default destination for anything. Nathan keeps human
reference copies there, including of PFCanon. **Those copies carry no authority.**
Never resolve canon from Drive, and never reconcile a repository file against a
Drive copy to decide which is current.

Every other path in the repository remains off limits without Nathan's explicit
instruction for that specific change. Nathan alone merges.

The `glow-artifact-storage`, `glow-write-boundary` and `glow-workspace-currency`
skills are already updated to this. This document exists because the **prompts
and the supporting controls are not**, and a prompt that still routes an artifact
to Drive will send a runtime session to the wrong place.

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

    EPHEMERAL_DRIVE
    Ephemeral Planning Files
    Core Docs / PFCanon
    drive.google.com
    direct Drive link

Every hit is recorded in the batch contract ledger under finding class
`STORAGE_ARCHITECTURE`, and closed or blocked explicitly. None may be silently
skipped. A prompt already repaired in an earlier batch that still carries one of
these returns to its owning batch ledger under §6.9 of the plan.

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

## Unresolved: two ephemeral directories

The skills name `docs/ephemeral/` as the working store and the only ephemeral
path a session may write. Commit `f9c9eda` (2026-09-17 02:28 UTC) imported the
155 files from Drive `Glow / Ephemeral Planning Files` into
`docs/plans/ephemeral/` instead, including the current GCFPE record:
`gcfpe.plan.repair-checklist.md`, `gcfpe.batch-1.repair-report.md`,
`gcfpe.batch-1.validation-report.md`, `gcfpe.batch-2.*` and
`gcfpe.r20260914-1.graph-contract.md`.

The authorized write path and the actual store are therefore different
directories. Nathan resolves this, by moving the import or by repointing the
skills. Until then: **read** the historical record from
`docs/plans/ephemeral/`, **write** new artifacts to `docs/ephemeral/`, and move
nothing.

A prompt repaired under this requirement should cite `docs/ephemeral/` as the
destination class, since that is what the skills authorize. If Nathan settles on
`docs/plans/ephemeral/`, one search-and-replace across the repaired prompts
closes it — which is why the prompts name a destination class and nothing more.

## Consequence for the two-pass execution model

The batch ledgers now live in `docs/ephemeral/`, which a chat session cannot
write. Pass 1 therefore drafts both ledgers and hands them to Pass 2, which
commits them in the batch's single pull request; if Pass 1 itself runs in Claude
Code it commits them directly. This is a mechanical consequence of the storage
change, not an authority change, and Nathan may direct otherwise.

## Open items this closes

- **Batch 1, R2** — the rebuilt candidate graph exceeding the Drive connector
  ceiling. The graph parts are in `docs/graph/parts/` and the assembled graph is
  derived output that is never committed. There is nothing left to persist to
  Drive, so R2 no longer has a subject.

`R1` — the undeclared `SPECIFICATION_DELTA` schema — is unaffected by this
change and remains open.
