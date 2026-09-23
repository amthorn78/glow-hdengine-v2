---
artifact_type: GCFPE_DIRECT_HANDOFF_AND_RUNTIME_ARTIFACT_OPERATING_PROCEDURE
artifact_version: "5.0.0"
title: "GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v5.0.0 — 20260923"
release: GCFPE-20260914.1
status: REGISTER_BOUND
supersedes: docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v4.0.0-20260914.md
recorded_by: GCFPE-MGMT-10, closing MODIFICATION-20260923-alpha-feedback-open-entries (D23), 2026-09-23
---

# GCFPE Direct-Handoff and Runtime Artifact Operating Procedure

**This procedure restates no rule.** It exists so that the release register's *operating
procedure* binding resolves to a current file. Each rule it points to is held, and guarded, where
the table below names it. If this file and those sources ever disagree, they govern.

## Superseded

`docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v4.0.0-20260914.md`
is superseded on 2026-09-23 and kept intact as historical evidence. **Do not execute it.** It was
written before this release was promoted (its own status reads `UNSELECTED_CANDIDATE_DRAFT`), and it
states rules that have since been retired:

- Drive storage and Drive links for runtime artifacts (`D7`);
- the PF10 addendum drainage lifecycle (`D6`, `D8`);
- `glow-hde-devops` as a support skill (`D16`);
- the pre-promotion selection and Alpha boundary (`D17`, `D18`);
- the complete, self-contained handoff carrying status and decisions; PR-30 and PR-35 in one
  session; Nathan's merge assertion as the only way into PR-40; and one Proceed per work unit
  (`D23`).

## Where each rule lives

| subject | authority |
|---|---|
| Selection, membership, and each member's current version | the **GCFPE Membership and Release Register** in Notion, and the complete-prompt-set catalog's `current_version` column (C-VERSION, `D23-G`) |
| What each prompt does, what it hands off and where the handoff sits | the selected prompt body in Notion. Each body carries the canonical texts for its role: C-NOTION, C-ART, C-HANDOFF, C-PLACE and C-TOP; in the PR lane also C-DEC, C-LAT, C-SESSION, C-SUB, C-DISPATCH, C-PROCEED and C-REPLAN |
| The wording of those canonical texts | `docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md`, §P *Canonical wording* and Amendment 1; `docs/ephemeral/modifications/MODIFICATION-20260923-pr40-reject-replans.md`, §P *Canonical wording* |
| Routes, result states and the handoff contract's fields | `docs/graph/parts/` (`D13`), rebuilt on demand and never committed assembled; proof token `55 nodes · 229 edges · 55 state_routes · 575,074 bytes · sha256 ae2bd159…` |
| Per-prompt contracts, and the guards that hold each canonical text | `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` |
| Rulings | `docs/prompt_ecosystem_management/gcfpe.decision-record.md` |
| PR, merge, abort and PF-document authority | the Prompt Flow Index, *Mandatory PR and PF-document authority boundaries* |
| Controlled sources (PFCanon read-only from `docs/pfcanon/`), runtime artifacts under `docs/ephemeral/` by pull request, and which artifacts a stage may require | the Prompt Flow Index, *Controlled-source and artifact rules* and *Artifact availability at the native stage* |
| Reading and storing prompt bodies | `docs/prompt_ecosystem_management/prompt-corpus-policy.md` (`D22`) |
| Notion writes | `docs/prompt_ecosystem_management/notion-write-boundary.md` |

## Why a pointer, not a rewrite

The installed `change-flow` skill resolves the operating procedure through the register's direct
binding and may not substitute a similarly named file. A binding left pointing at a superseded file
would stop that resolution. A rewritten procedure would be a second copy of rules that are already
held and guarded above, and two copies drift (`DERIV-001`).
