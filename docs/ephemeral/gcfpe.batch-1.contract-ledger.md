# GCFPE Batch 1 Contract Ledger — repository-first re-run

```yaml
artifact_type: GCFPE_BATCH_1_CONTRACT_LEDGER
artifact_version: "1.0"
ledger_date: 2026-09-17
authority: "Nathan / Product Owner, Batch 1 repair re-run authorization, 2026-09-17"
scope: BATCH_1_ONLY
finding_classes: [STORAGE_ARCHITECTURE, SPECIFICATION_DELTA_FORMAT, GRAPH_BODY_RECONCILIATION]
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
selected_release_mutated: false
storage_architecture_hits_total: 52
storage_architecture_closed: 52
storage_architecture_blocked: 0
prompt_bodies_changed: 11
graph_parts_changed: 2
open_findings: 0
```

This ledger records the findings this re-run raised and closed. It does not
restate the eight defects closed by the 2026-09-17 repair; those stand and
their record is `gcfpe.batch-1.repair-report.md`.

## 1. Survey method

Each of the eleven bodies was fetched fresh from Notion immediately before
editing and read back completely afterwards. Each was searched
case-sensitively for the bare term `Drive` first, then for
`Ephemeral Planning Files`, `Core Docs`, `EPHEMERAL_DRIVE`,
`drive.google.com` and `Google Doc`.

The bare `Drive` term is what makes the survey sound. A phrase-only survey
misses real clauses — the graph's `handoff_contract.required[3]`,
`"direct Drive artifacts and repository/PR references"`, matches none of the
five phrases named in §4.5 of the plan and is a genuine defect.

## 2. Classification rule applied

A clause is a `STORAGE_ARCHITECTURE` defect only when it tells a **future
runtime session where to put or fetch something**. A Drive URL that records
**where something came from at a past moment** — a retrieval receipt, a pinned
capture, a `source_id`, a superseded-document pointer — is lineage and stays
exactly as written.

Applied to this batch: **no lineage clause exists in any of the eleven bodies.**
The single `drive.google.com` URL each body carried was the
`Glow / Ephemeral Planning Files` folder, a destination for future writes, not a
provenance record. Every hit below is therefore a routing clause. In the graph,
the classification does bite: 11 `drive.google.com` URLs live in
`source_bindings` and are lineage; 2 clauses elsewhere are routing.

Two things the repair deliberately did not do:

- **The Markdown-only rule is unchanged.** Every body still prohibits opening,
  comparing, citing or falling back to Google Docs, `.doc` or `.docx` PFCanon
  variants. The source moved; the format rule did not.
- **Drive is narrowed, not deleted.** Every repaired body now carries
  "Google Drive is used only where Nathan directs a specific file there" —
  conditional, never a default.

## 3. `STORAGE_ARCHITECTURE` findings — prompt bodies

Clause counts are per distinct contradicting clause, not per edit. All closed.

| ID | Prompt | Section | Clause as found | Repaired to | Status |
|---|---|---|---|---|---|
| `B1-SA-01` | GCFPE-MGMT-10 | Required result | "Save/read back the report, record its direct Drive link" | write under `docs/ephemeral/`, commit and push on the batch branch, reference by repository path | CLOSED |
| `B1-SA-02` | GCFPE-MGMT-10 | Artifact and source boundaries | "saved in `Glow / Ephemeral Planning Files` … carried by its observed direct Drive link" | written under `docs/ephemeral/`, pushed on the branch, referenced by repository path | CLOSED |
| `B1-SA-03` | GCFPE-MGMT-10 | Artifact and source boundaries | canon resolved "through `Glow / Core Docs / PFCanon`" | read from `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-04` | MGR-10 | Handoff rule | handoff carries artifacts "by exact identity/version and direct Drive link" | by repository path, or direct Notion URL for a Notion-resident artifact | CLOSED |
| `B1-SA-05` | MGR-10 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-06` | MGR-10 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-07` | CF-PO-10 | Required result and routing | "Save/read back the artifact and retain its direct Drive link" | write under `docs/ephemeral/`, push on the branch, reference by repository path | CLOSED |
| `B1-SA-08` | CF-PO-10 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-09` | CF-PO-10 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-10` | CF-PO-10 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-11` | CF-C-10 | Required result and routing | "KICKOFF_HANDOFF_ID, the complete artifact's observed direct Drive link" | the complete artifact's repository path under `docs/ephemeral/` | CLOSED |
| `B1-SA-12` | CF-C-10 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-13` | CF-C-10 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-14` | CF-C-10 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-15` | CF-C-20 | Required result | "Include the observed direct Drive link" | include the artifact's repository path under `docs/ephemeral/` | CLOSED |
| `B1-SA-16` | CF-C-20 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-17` | CF-C-20 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-18` | CF-C-20 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-19` | CF-C-30 | Execute 5 | addendum "approval-decision ID/version/direct Drive link" | approval-decision ID/version/repository path | CLOSED |
| `B1-SA-20` | CF-C-30 | Execute 5 | addendum "immutable-base ID/version/approval lineage/direct Drive link" | …/repository path | CLOSED |
| `B1-SA-21` | CF-C-30 | Execute 5 | "Save/read back the addendum in `Glow / Ephemeral Planning Files`" | write under `docs/ephemeral/`, push on the branch, read back completely | CLOSED |
| `B1-SA-22` | CF-C-30 | Required result | decision returned with "its direct Drive link" | its repository path | CLOSED |
| `B1-SA-23` | CF-C-30 | Required result and routing | INITIAL_APPROVE package carries Specification and decision "by direct Drive link" | by repository path | CLOSED |
| `B1-SA-24` | CF-C-30 | Required result and routing | DELTA_APPROVE returns "single read-back addendum link" | single read-back addendum repository path | CLOSED |
| `B1-SA-25` | CF-C-30 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-26` | CF-C-30 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-27` | CF-C-30 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-28` | CF-C-40 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-29` | CF-C-40 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-30` | CF-C-40 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-31` | CF-E-10 | Required result and routing | KICKOFF_HANDOFF_ID "observed direct Drive link" | repository path under `docs/ephemeral/` | CLOSED |
| `B1-SA-32` | CF-E-10 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-33` | CF-E-10 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-34` | CF-E-10 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-35` | CF-E-20 | Required result | "Include the observed direct Drive link" | include the artifact's repository path | CLOSED |
| `B1-SA-36` | CF-E-20 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-37` | CF-E-20 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-38` | CF-E-20 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-39` | CF-E-30 | Execute 5 | addendum "approval-decision ID/version/direct Drive link" | …/repository path | CLOSED |
| `B1-SA-40` | CF-E-30 | Execute 5 | addendum "immutable-base ID/version/approval lineage/direct Drive link" | …/repository path | CLOSED |
| `B1-SA-41` | CF-E-30 | Execute 5 | "Save/read back the addendum in `Glow / Ephemeral Planning Files`" | write under `docs/ephemeral/`, push, read back completely | CLOSED |
| `B1-SA-42` | CF-E-30 | Required result | decision returned with "its direct Drive link" | its repository path | CLOSED |
| `B1-SA-43` | CF-E-30 | Required result and routing | INITIAL_APPROVE package "by direct Drive link" | by repository path | CLOSED |
| `B1-SA-44` | CF-E-30 | Required result and routing | DELTA_APPROVE "single read-back addendum link" | single read-back addendum repository path | CLOSED |
| `B1-SA-45` | CF-E-30 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-46` | CF-E-30 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-47` | CF-E-30 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |
| `B1-SA-48` | CF-E-40 | Handoff rule | direct Drive link | repository path / Notion URL | CLOSED |
| `B1-SA-49` | CF-E-40 | Artifact and source boundaries | `Ephemeral Planning Files` + direct Drive link | `docs/ephemeral/`, repository path | CLOSED |
| `B1-SA-50` | CF-E-40 | Artifact and source boundaries | `Glow / Core Docs / PFCanon` | `docs/pfcanon/`, read-only | CLOSED |

## 4. `STORAGE_ARCHITECTURE` findings — graph parts

| ID | Location | Clause as found | Repaired to | Status |
|---|---|---|---|---|
| `B1-SA-51` | `global.json` `alpha_resumption_contract.preparation_prerequisites[7]` | "handoff saved and completely read back in `Glow / Ephemeral Planning Files`" | "handoff written under `docs/ephemeral/`, committed and pushed on the working branch, and completely read back" | CLOSED |
| `B1-SA-52` | `global.json` `handoff_contract.required[3]` | "direct Drive artifacts and repository/PR references" | "artifact repository paths, direct Notion URLs where the artifact is Notion-resident, and repository/PR references" | CLOSED |

**Zero per-prompt parts carried a storage clause.** Confirmed by re-running the
survey across all 56 part files after repair:

```
[Drive] 0 · [Ephemeral Planning Files] 0 · [Core Docs] 0
[EPHEMERAL_DRIVE] 0 · [Google Doc] 0 · [drive.google.com] 11
drive.google.com outside source_bindings: 0
bare "Drive" outside source_bindings:     0
```

`source_bindings` is untouched. Its 11 Drive URLs carry `sha256`,
`retrieved_at`, `provider_size_bytes` and
`binding_scope: REPAIR_BASELINE_EVIDENCE_ONLY_NOT_A_RUNTIME_CURRENT_PF10_ALIAS`,
and its own `runtime_rule` already states these pins never replace a fresh
lookup. That is lineage by every test in §2.

## 5. `SPECIFICATION_DELTA_FORMAT` — R1

| ID | Prompts | Finding | Resolution | Status |
|---|---|---|---|---|
| `B1-SDF-01` | CF-C-40, CF-E-40 | `SPECIFICATION_DELTA` is declared with `artifact_type` and `state` but no format authority. The prior run correctly refused to invent one. | The format is governed by referenced canon, resolved and cited at run time through each prompt's existing PFCanon source contract. No version token is embedded. | CLOSED |

The clause added to both bodies, identical in each:

> The `SPECIFICATION_DELTA` format — its section and field structure — is
> governed by the canon referenced for this change, resolved and cited at run
> time through this prompt's PFCanon source contract below. Record the exact
> canon resolved and cited in the produced delta; do not reuse the base
> Specification's schema token for it, and do not mint a new one. If that canon
> cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR` with the failed
> predicate and recovery owner rather than authoring against an assumed format.

Why this closes D4 rather than deferring it. The prior run framed R1 as a
choice between reusing `glow-specification/3.0` (false conformance) and minting
`glow-specification-delta/3.0` (nothing validates it). Both are wrong because
the question was misframed: a `schema_version` token in a prompt body is a
hardcoded canon reference, which §4.5 of the plan forbids outright — *"Do not
hardcode canon, skill-owned mechanics, or a release token into a prompt body.
Prompts name the destination class … and let the referenced canon and the
installed skills own the rest."* The `glow-graph-contract` skill states the same
rule for exactly this symptom: *"When a field seems to want a `schema_version`
that no source defines, that is usually a sign the format belongs to canon."*

So no identifier was needed and none was minted. The delta now resolves its
format the same way every other canon-governed artifact in the flow does, and
the failure mode is a named, already-defined state rather than silent authoring
against a guess.

**The base Specification's own `schema_version: glow-specification/3.0` in
CF-C-20 and CF-E-20 was deliberately left alone.** R1's scope is the delta.
Changing the base token is not supported by any recorded defect and would reach
beyond this authorization. It is recorded as an observation in §7.

## 6. `GRAPH_BODY_RECONCILIATION` — found by this run, not previously landed

| ID | Finding | Evidence | Status |
|---|---|---|---|
| `B1-GBR-01` | The graph part for CF-C-10 carried no `CF-C-10 → CF-E-10` edge, while CF-C-10's persisted body carries the reciprocal wrong-class branch. The graph asserted a CRD/Epic asymmetry the bodies do not have. | Rebuild before repair: **235** edges, `CF-C-10` destinations `[CF-C-10, CF-C-20, CF-PO-10, NATHAN_TERMINAL_RETURN]`. The prior report records this edge as added and the rebuild as 236. | CLOSED |
| `B1-GBR-02` | `pf10_addendum_contract.role_vocabulary` was absent, so the graph's `NON_PRODUCER` / `QUALIFYING_PRODUCER` and the bodies' `NONPRODUCER` / `QUALIFYING_DELTA_APPROVAL_PRODUCER` could not be joined. | `role_vocabulary present: False` on `main`. The prior report records it as declared. | CLOSED |

**Cause, stated plainly.** Neither is a new defect and neither is a
contradiction of the prior run's work. The 2026-09-17 repair closed D3 and D5
correctly and described both changes precisely, but it recorded
`repository_writes: 0` because no repository path was open to it at the time;
its §8 states the changed parts were "handed over with this report rather than
written anywhere unauthorized." They were never persisted. Under
repository-first storage there is now somewhere to put them, so this run landed
them — as a separate commit, applying an already-decided repair rather than
authoring a new one.

Had they been left, Batch 1 completion criterion 2 would have been false against
the live artifact: the bodies symmetric, the graph not.

## 7. Observations recorded, not repaired

| Observation | Why not repaired here |
|---|---|
| CF-C-10, CF-E-10 hardcode `schema_version: glow-kickoff/3.0`; CF-C-20, CF-E-20 hardcode `schema_version: glow-specification/3.0`. Under §4.5's "do not hardcode canon" rule these are the same shape of defect R1 just closed for the delta. | No recorded defect covers them, and the authorization forbids re-authoring beyond what a recorded defect supports. Closing them is a Product Owner decision about whether §4.5's rule reaches existing, defined, validating tokens — not a derivation. Raised for Nathan; affects at least 4 Batch 1 prompts and probably most of the 55. |
| `state_routes[RS-40].drain_verified` declares a route with no backing edge. | Batch 3 lane. Known, expected, and the only build warning. |
| O3, the 4-byte builder delta. | Batch 2 scope by the authorization. Untouched. |

## 8. Producer/consumer reconciliation

Re-run across the CRD and Epic branches after all eleven bodies were persisted.

- **Lane symmetry, measured from the rebuilt graph:** `CF-C-10 → [CF-C-10,
  CF-C-20, CF-E-10, CF-PO-10, NATHAN_TERMINAL_RETURN]`, `CF-E-10 → [CF-C-10,
  CF-E-10, CF-E-20, CF-PO-10, NATHAN_TERMINAL_RETURN]`, symmetric `True`.
- **Handoff reference form now agrees graph-to-body.** `handoff_contract.required[3]`
  and the eleven repaired Handoff-rule clauses both say repository path plus
  direct Notion URL. Before this run the graph said "direct Drive artifacts"
  and the bodies said "direct Drive link"; they agreed, but on the wrong thing.
- **The `-10 → -20` interface is consistent.** CF-C-10/CF-E-10 emit
  `KICKOFF_HANDOFF_ID` as a repository path; CF-C-20/CF-E-20 consume
  `KICKOFF_HANDOFF_ID` and now report the produced Specification by repository
  path.
- **The `-30` addendum contract is consistent.** Both `-30` bodies write the
  addendum under `docs/ephemeral/` and return its repository path; the graph's
  `pf10_addendum_contract` producer set is unchanged at `[CF-C-30, CF-E-30,
  ESC-40, IA-30, QA-70, RS-20]` and `exactly_one_per_qualifying_approval`
  remains `true`.
- **The `-40 → -30` delta interface is consistent.** Both `-40` bodies emit
  `artifact_type: SPECIFICATION_DELTA` / `state: SPECIFICATION_PENDING` with
  canon-governed format; both `-30` bodies accept "one pending
  SPECIFICATION_DELTA" without a schema check, which is now correct rather than
  accidental — there is no token to check, and the format authority is named.
- **`never_for` still contains `INITIAL_APPROVAL`**, and both `-30` bodies still
  state `INITIAL_APPROVE … emits no PF10 addendum`. Unchanged by this run and
  re-verified.

## 9. Prohibited-action confirmation

No write outside `docs/ephemeral/` and `docs/graph/`. `docs/pfcanon/` was not
written. The assembled graph was built to the session scratchpad and is not
committed. No prompt outside the eleven was modified. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not mutated and no selected predecessor
was edited. PF10 was not read, edited or drained. The release register, Alpha
state, catalog, Flow Index and PR/CI state were untouched. No historical Batch 1
artifact was edited, renamed or deleted. Batches 2–6 were not executed. Nothing
was merged.
