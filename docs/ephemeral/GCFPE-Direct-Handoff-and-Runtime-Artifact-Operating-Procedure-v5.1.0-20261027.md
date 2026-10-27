---
artifact_type: GCFPE_DIRECT_HANDOFF_AND_RUNTIME_ARTIFACT_OPERATING_PROCEDURE
artifact_version: "5.1.0"
title: "GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v5.1.0 — 20261027"
release: GCFPE-20261027.1
status: REGISTER_CONTROLLED
selection_rule: "Operative only while the release register's current selection binds it as the operating procedure. It does not assert its own binding."
supersedes: docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md
recorded_by: GCFPE-MGMT-10, MODIFICATION-20261027-gcfpe-backlog-open-items (PART-19, ITEM-03), 2026-10-27
---

# GCFPE Direct-Handoff and Runtime Artifact Operating Procedure

**This procedure restates no rule.** It exists so that the release register's *operating
procedure* binding resolves to a current file. Each rule it points to is held, and guarded, where
the table below names it. If this file and those sources ever disagree, they govern.

## Superseded

`docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md`
is superseded from the moment the release register binds this file, and is kept intact as historical
evidence (`AUTH-001`). It pointed to a dated 091426.1 report for which body carries which canonical
text, and it named the 091426.1 release and its graph proof token.

`docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v4.0.0-20260914.md`
was superseded on 2026-09-23 and is kept intact as historical evidence. **Do not execute either.** v4.0.0 was
written before GCFPE-20260914.1 was promoted (its own status reads `UNSELECTED_CANDIDATE_DRAFT`), and it
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
| What each prompt does, what it hands off and where the handoff sits | the selected prompt body in Notion, which carries the canonical texts its registry row requires (among them C-NOTION, C-ART, C-HANDOFF, C-PLACE, C-TOP, C-DEC, C-LAT, C-SESSION, C-SUB, C-DISPATCH, C-PROCEED, C-REPLAN, C-PR20-ENTRY and C-TYPESAFE); which body carries which is that body's row in `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`, whose `required_regex` and `forbidden_regex` assertions name each text's guard |
| The final wording of those canonical texts | the §P of the Modification that last applied each text, under `docs/ephemeral/modifications/`, beginning with `docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md` §3 and `gcfpe.decision-record.md` `D23`, *Successor — PR-40 is entered once per merge*, for C-DISPATCH's last sentence; the registry row's assertions guard each text as it now stands |
| Routes, result states and the handoff contract's fields | `docs/graph/parts/` (`D13`), rebuilt on demand and never committed assembled; its current proof token is recorded in `docs/prompt_ecosystem_management/authoritative-surfaces.md` (*Release baseline*) and in the register's current selection |
| Per-prompt contracts, and the guards that hold each canonical text | `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` |
| Rulings | `docs/prompt_ecosystem_management/gcfpe.decision-record.md` |
| PR, merge, abort and PF-document authority | the Prompt Flow Index, *Mandatory PR and PF-document authority boundaries — Product Owner* |
| Controlled sources (PFCanon read-only from `docs/pfcanon/`), runtime artifacts under `docs/ephemeral/` by pull request, and which artifacts a stage may require | the Prompt Flow Index, *Controlled-source and artifact rules* and *Artifact availability at the native stage* |
| Reading and storing prompt bodies | `docs/prompt_ecosystem_management/prompt-corpus-policy.md` (`D22`) |
| Notion writes | `docs/prompt_ecosystem_management/notion-write-boundary.md` |

## Why a pointer, not a rewrite

The installed `change-flow` skill resolves the operating procedure through the register's direct
binding and may not substitute a similarly named file. A binding left pointing at a superseded file
would stop that resolution. A rewritten procedure would be a second copy of rules that are already
held and guarded above, and two copies drift (`DERIV-001`). The graph
proof token is a pointer for the same reason: the release baseline records it, so this file does not
go stale when the graph is rebuilt.

## Canon relied on

- `PF04-Canon-HDE-Governance` v2.8.8 §9.1.3: the repository home of ongoing non-PF operating procedures
  remains undecided, so this successor stays in `docs/ephemeral/` beside its predecessor.
- `PF10-HDE-Build-Notes` v13.9: silent on this procedure (its one addendum, 2.1, is S19 vendor and
  security policy), so permanent canon governs.
