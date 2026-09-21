---
artifact_type: PROMPT_ECOSYSTEM_FREEZE_SNAPSHOT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
subject: The frozen state of the candidate release, measured — and what a freeze means once the corpus mirror is gone
---

# Freeze — GCFPE-20260914.1 / 091426.1 / 55

Every value below was measured in this session against the installed tree and the committed
repository, not transcribed from a report.

## Installed skills

| skill | files | digest — `freeze.py` rooted at the skill directory |
|---|---|---|
| `change-flow` | 21 | `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` |
| `flowmaster-validate` | 29 | `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` |

| declared identity | value |
|---|---|
| `CHANGE_FLOW_SPECIALIZATION_REVISION` | 3.2.8 |
| `FLOWMASTER_VALIDATE_REVISION` | 3.2.14 |
| `validator_revision` | 3.2.12 |
| `SKILL_TREE_SHA256` | `6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93` |

`flowmaster-validate` equals the digest its §10 verdict named. Zero `.pyc` in the synced directory,
which was never written to.

## Candidate contract

`1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` / **610549 bytes**,
**byte-identical in both bundled copies** — `change-flow/references/` and
`flowmaster-validate/references/`.

## Graph — rebuilt, not quoted

Built from the **56 committed parts** in `docs/graph/parts/` with the canonical builder:

```
build: 55 nodes, 227 edges, 55 state_routes
       embedded JSON 569902 bytes  sha256 1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7
       validation PASS
```

This reproduces the proof token in `authoritative-surfaces.md` **exactly**. The assembled graph was
built to a scratchpad and is not committed, per `D7`.

## Repository controls

| control | sha256 | bytes |
|---|---|---|
| `project-prompt-contract-registry.md` | `907e565eabe10bfe…` | 203972 |
| `gcfpe.decision-record.md` | `3076cbf693f762fb…` | 51830 |
| `authoritative-surfaces.md` | `b7cb6078c05430e8…` | 6422 |
| `ecosystem-change-management.md` | `0dede2030149bc76…` | 19614 |

## What this freeze deliberately does **not** contain

**The 55 prompt bodies.** Under the **Prompt Corpus Storage and Fidelity Policy** the corpus is
authored and maintained in Notion and must not be transcribed, exported, mirrored, snapshotted,
cached or hashed to disk. A freeze that captured them would be the prohibited artifact, produced at
the moment of promotion.

**The prompts' identity in this release is the release itself** — `GCFPE-20260914.1 / 091426.1 /
55` — together with the 55 `member_registry` entries in the contract above, which bind every prompt
to its exact Notion page id. That binding is frozen, and it is checkable at any time by resolving a
page id. What is not frozen, and must not be, is a copy of what those pages said today.

This is a change in what a freeze means, not a gap in this one. The plan's §13 line was written
when the freeze was expected to cover *"prompt/control snapshot"*; the prompt half is now carried
by identity rather than by content, and the control half is above in full.

## Standing

The candidate release is frozen at the values above. The selected production release
`GCFPE-20260913.1 / 091326.2 / 54` is untouched. Nothing here promotes anything: promotion remains
a Product Owner decision after independent post-flight.
