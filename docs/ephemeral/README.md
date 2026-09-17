# docs/ephemeral

The working store for Glow / GCFPE governance artifacts: reports, ledgers,
checkpoints, handoff records, run evidence and planning files.

Artifacts are authored here directly. The file on disk **is** the artifact —
no upload, no round trip, no size ceiling, no hash ritual. Git records exactly
what was written.

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

Files imported from the former Drive folder `Glow / Ephemeral Planning Files`
keep the names they arrived with. They are historical record. Do not rename them
to fit the convention — a rename breaks every reference that cites them.

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
