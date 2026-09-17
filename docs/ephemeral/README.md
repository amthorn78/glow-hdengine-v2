# docs/ephemeral

The working store for Glow / GCFPE governance artifacts: reports, ledgers,
checkpoints, handoff records, run evidence and planning files.

Artifacts are authored here directly. The file on disk **is** the artifact —
no upload, no round trip, no size ceiling, no hash ritual. Git records exactly
what was written.

> ## Unresolved: two ephemeral directories
>
> The `glow-write-boundary` and `glow-artifact-storage` skills name
> **`docs/ephemeral/`** as the working store and the only ephemeral path a
> session may write.
>
> On 2026-09-17 at 02:28 UTC, commit `f9c9eda` imported the 155 files from the
> Drive folder `Glow / Ephemeral Planning Files` into **`docs/plans/ephemeral/`**
> instead — including the current GCFPE record: `gcfpe.plan.repair-checklist.md`,
> `gcfpe.batch-1.repair-report.md`, `gcfpe.batch-1.validation-report.md`,
> `gcfpe.batch-2.*` and `gcfpe.r20260914-1.graph-contract.md`.
>
> So the authorized write path and the actual store are different directories.
> This file is in the authorized one because a session may not write to
> `docs/plans/ephemeral/`.
>
> **Nathan resolves this**, either by moving the import here or by pointing the
> skills at `docs/plans/ephemeral/`. Until he does: **read** the historical
> record from `docs/plans/ephemeral/`, and **write** new artifacts here. Do not
> move, copy, duplicate or tidy either directory on your own initiative.

## How work lands here

1. Author or edit the file at its path under `docs/ephemeral/`.
2. Commit it on a `docs/<yyyymmdd>-<short-slug>` branch.
3. Push and open one pull request for the session's work.
4. Report the branch, the PR, and the paths written.

An artifact is stored once it is committed and pushed. **Nathan merges.** An open
pull request is a complete outcome; it is not unfinished work needing another
push, and it is never merged by a session to make it look finished.

## Naming

    <system>.<scope>.<artifact>.md

Lowercase. Dots separate segments, hyphens join words inside one —
`gcfpe.batch-2.repair-report.md`. No version or date in a live filename; those
belong in the artifact's YAML header. A name that changes is not an address.

## Boundaries

- This directory is pruned manually by Nathan. Never delete or tidy it on your
  own initiative.
- `docs/pfcanon/` is authoritative PFCanon and is **read-only**. Never write it.
- `docs/graph/` holds maintained machine-readable source and is not scratch.
  Never move working files into it, and never move its contents here.
- Derived output rebuilt from source is not committed anywhere. Build it to the
  scratchpad and represent it by a proof token.
- Prompts and state live in Notion, not here.
- Every other path in the repository is off limits without Nathan's explicit
  instruction for that specific change.

See the `glow-write-boundary` and `glow-artifact-storage` skills.
