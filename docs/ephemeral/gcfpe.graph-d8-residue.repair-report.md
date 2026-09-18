---
artifact_type: GCFPE_GRAPH_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-18
release: GCFPE-20260914.1 / 091426.1 / 55
authority: Product Owner authorization, 2026-09-18
scope: docs/graph/parts/ — three defects found by the workflow-skill repair
---

# Graph repair — D8 residue, predecessor scope, stale protected identity

Three defects in `docs/graph/parts/`, each found by a validator that had never previously
been able to run. All three were surfaced by the workflow-skill repair (rounds 4 and 5) and
fixed here under Product Owner authorization.

## What was wrong

| # | Where | Defect |
|---|---|---|
| 1 | `global.json` `terminal_contract.invocation_terminal_recoverable` | Listed **`PF10_REFERENCE_NOT_VISIBLE`**, a result state of the PF10 reference-visibility check that **D8** retired along with `pf10_reference_visibility_check` and the `PF10_REFERENCE_VISIBILITY` vocabulary. The rebuilt handoff contract had already dropped it; the graph had not. |
| 2 | `prompts/CL-20.json` `predecessor.title` | Carried the **candidate** name, *"CL-20 — Prepare Closure Memo and Post-Closure Record — 091326.2"*. The `predecessor` block records the **selected** release's page, which is still titled *"CL-20 — Prepare Post-Closure Drainage and Closure Memo"*. The rename was over-applied into selected-release provenance — `SCOPE-002`. |
| 3 | `global.json` `protected_identities.flowmaster_primary_core_sha256` | Pinned `495c2ca6…` against a measured `4d8bb9bf…`. |

## How each was established, not assumed

- **Defect 1** — the retired token is named in D8 and in the succession record's list of
  markers to treat as defects on sight. The rebuilt contract does not contain it.
- **Defect 2** — resolved against the **live Notion page** `3da4590a05eb81a2a0c9c98f719350a1`,
  whose title is *"CL-20 — Prepare Post-Closure Drainage and Closure Memo — 091326.2"*. The
  candidate node's own title and `output_artifacts` correctly keep the new name and
  `POST_CLOSURE_RECORD`; only the predecessor block was wrong.
- **Defect 3** — recomputed from the installed `flowmaster-primary/SKILL.md` using
  `validate_flowmaster.marked_block`, giving `4d8bb9bf1c9c85ae…`, which matches the validation
  profile and the passing Flowmaster suite. The graph's value matches no measured artifact.

## The proof token moved

Rebuilt with `scripts/graph_parts.py build docs/graph/parts`, which ships with the
`glow-graph-contract` skill. Node, edge and state_route counts are unchanged; only three
field values moved.

| | |
|---|---|
| Before | `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…` |
| After | `55 nodes · 227 edges · 55 state_routes · 571,479 bytes · sha256 021058dd…` |

Validation `PASS`, no orphan-route warning. The assembled graph is derived output and is not
committed; this repair changes only the parts.

## Documents updated in this change

| Path | Change |
|---|---|
| `authoritative-surfaces.md` | Proof token and the recorded build output |
| `ecosystem-change-management.md` | Proof token in the standing-instruments table |
| `gcfpe.decision-record.md` | Forward note under D15; D15's own before/after is left intact as history |

`pe-succession/pe30-to-pe31.md` still cites `d7832c73…`. It is a **dated succession record**
and is history, not instruction, so it was deliberately not rewritten. The forward note under
D15 states the supersession. `pe-succession/pe31-to-pe32.md` carries the same citation and is
on the unmerged branch `docs/20260918-pe32-succession`.

## Skills

The four installed skills bundle the candidate graph and pin its digest. They were rebuilt
against the new graph and repackaged for installation: the bundled graph replaced in
`flowmaster-validate` and `change-flow`, and every pin naming it updated **field by field** —
the validation profile's `frozen_graph`, `EXPECTED_FROZEN_GRAPH_SHA256` / `_BYTES`,
`change-flow`'s `EXPECTED_GRAPH_SHA`, and the handoff contract's own
`source_snapshot.frozen_candidate_graph` pin in both copies, followed by re-pinning the
contract's own digest and byte count.

## Verification, from the rebuilt tree

| Gate | Result |
|---|---|
| Graph rebuild and validation | `PASS`, 55 / 227 / 55, no orphan routes |
| Candidate validator | **0 errors** (23 before the workflow-skill repair began) |
| Flowmaster full validation suite | `FLOWMASTER_SUITE_PASS`, 0 findings, 0 warnings |
| Candidate fixture runner | 33 / 33 fixtures, 28 / 28 variants |
| `change-flow` own validator | PASS |
| `glow-hde-pr-development` structural validator | PASS |
| Governance audit fixture suite | 29 tests, OK |
| Candidate contract | byte-identical across both skills |
