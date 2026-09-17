# GCFPE Batch 1 Repair Report

```yaml
artifact_type: GCFPE_BATCH_1_REPAIR_REPORT
artifact_version: "2.0"
report_date: 2026-09-17
supersedes_in_place: "v1.0 of the same path, 2026-09-17 (verdict BATCH_1_BLOCKED)"
authority: "Nathan / Product Owner, Batch 1 repair re-run authorization, 2026-09-17"
repairs_validation: docs/ephemeral/gcfpe.batch-1.validation-report.md
storage_requirement: docs/ephemeral/gcfpe.storage-architecture.md
contract_ledger: docs/ephemeral/gcfpe.batch-1.contract-ledger.md
copy_repair_ledger: docs/ephemeral/gcfpe.batch-1.copy-repair-ledger.md
verdict: BATCH_1_REPAIRED
blockers: 0
scope: BATCH_1_ONLY
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
selected_release_mutated: false
pf10_edited_or_drained: false
prompt_bodies_changed: 11
graph_parts_changed: 2
defects_fully_closed: 8
storage_architecture_hits_closed: 52
criteria_met: 6
criteria_not_met: 0
open_items_for_product_owner: 1
```

## 1. Verdict

**`BATCH_1_REPAIRED`.** All eight recorded defects are now fully closed, the
`STORAGE_ARCHITECTURE` defect class is closed across all eleven prompts and the
graph, both prior blockers are retired, and all six Batch 1 completion criteria
are met.

| Prior blocker | Outcome |
|---|---|
| **R1** — `SPECIFICATION_DELTA` has no declared `schema_version` | **Retired by closing D4.** The delta's format is governed by referenced canon, resolved and cited at run time through each prompt's existing PFCanon source contract. No identifier was minted and none was reused. §3. |
| **R2** — rebuilt graph exceeds the Drive connector ceiling | **Retired: no subject.** The graph is held as parts in `docs/graph/parts/` and the assembled graph is derived output that is never persisted. There is nothing to write to Drive. Confirmed, not re-litigated. |

One item is raised **for Nathan's decision**, and it is not a blocker: it does
not prevent Batch 1 closing and nothing downstream waits on it. §7.

## 2. Per-prompt disposition, against the bodies as they now stand

All eleven were fetched fresh immediately before editing and read back
completely afterwards. All eleven changed, because the storage boilerplate was
in every body. Clause-level findings are in the contract ledger.

| # | Prompt | Disposition | Closed here | Clause that now satisfies it |
|---|---|---|---|---|
| 1.01 | GCFPE-MGMT-10 | **REPAIRED** | 3 × `STORAGE_ARCHITECTURE` | Report is "written under `docs/ephemeral/`, committed and pushed on the batch branch … referenced by its repository path"; canon "from `docs/pfcanon/`" |
| 1.02 | MGR-10 | **REPAIRED** | 3 × `STORAGE_ARCHITECTURE` | Handoff carries artifacts "by … its repository path, or its direct Notion URL"; boundaries paragraph repointed |
| 1.03 | CF-PO-10 | **REPAIRED** | 4 × `STORAGE_ARCHITECTURE` | `CHANGE_CLASS_SELECTION` written under `docs/ephemeral/` and referenced by repository path |
| 1.04 | CF-C-10 | **REPAIRED** | 4 × `STORAGE_ARCHITECTURE` | "KICKOFF_HANDOFF_ID, the complete artifact's repository path under `docs/ephemeral/`" |
| 1.05 | CF-C-20 | **REPAIRED** | 4 × `STORAGE_ARCHITECTURE` | "Include the artifact's repository path under `docs/ephemeral/`" |
| 1.06 | CF-C-30 | **REPAIRED** | 9 × `STORAGE_ARCHITECTURE` | Addendum "written under `docs/ephemeral/` … read back completely"; approval-decision and immutable-base carried by repository path |
| 1.07 | CF-C-40 | **REPAIRED** | 3 × `STORAGE_ARCHITECTURE`, **D4 completed** | "The `SPECIFICATION_DELTA` format … is governed by the canon referenced for this change, resolved and cited at run time through this prompt's PFCanon source contract below." |
| 1.08 | CF-E-10 | **REPAIRED** | 4 × `STORAGE_ARCHITECTURE` | Mirrors CF-C-10 exactly |
| 1.09 | CF-E-20 | **REPAIRED** | 4 × `STORAGE_ARCHITECTURE` | Mirrors CF-C-20 exactly |
| 1.10 | CF-E-30 | **REPAIRED** | 9 × `STORAGE_ARCHITECTURE` | Mirrors CF-C-30 exactly |
| 1.11 | CF-E-40 | **REPAIRED** | 3 × `STORAGE_ARCHITECTURE`, **D4 completed** | Same delta-format clause as CF-C-40, in the EPIC variant |

The 2026-09-17 repair's own edits — MGMT-10's Entry contract, CF-C-10's
reciprocal branch and Required-list terminator, the two `-40` output contracts,
CF-E-30's and CF-E-40's casing — are intact and were not revisited.

## 3. D4 completed — the `SPECIFICATION_DELTA` format

`artifact_type: SPECIFICATION_DELTA` and `state: SPECIFICATION_PENDING` were
settled from the ledger by the prior run and are unchanged. The third field was
the open part, and the answer is that it was never a field.

The prior run framed the choice as `glow-specification/3.0` (asserts a
conformance the delta's field set does not hold) versus a minted
`glow-specification-delta/3.0` (nothing defines or validates it). Both are
wrong, and so is picking one, because a `schema_version` token written into a
prompt body is a hardcoded canon reference — which §4.5 of the plan forbids
directly: *"Do not hardcode canon, skill-owned mechanics, or a release token
into a prompt body. Prompts name the destination class … and let the referenced
canon and the installed skills own the rest."* The `glow-graph-contract` skill
names the same symptom: *"When a field seems to want a `schema_version` that no
source defines, that is usually a sign the format belongs to canon."*

Both `-40` bodies now carry, identically:

> The `SPECIFICATION_DELTA` format — its section and field structure — is
> governed by the canon referenced for this change, resolved and cited at run
> time through this prompt's PFCanon source contract below. Record the exact
> canon resolved and cited in the produced delta; do not reuse the base
> Specification's schema token for it, and do not mint a new one. If that canon
> cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR` with the failed
> predicate and recovery owner rather than authoring against an assumed format.

The failure mode is an existing, defined state rather than silent authoring
against a guess, and the delta resolves its format the way every other
canon-governed artifact in the flow does. **D4 is fully closed and R1 is
retired.** No identifier was minted.

## 4. The other seven defects and the open items

D1, D2, D3, D5, D6, D7, D8 were fully closed by the 2026-09-17 repair and are
not re-derived here; v1.0 of this file, in this path's git history, holds that
reasoning. O1 was closed from source, O2 settled as deliberate, O3 left to
Batch 2.

Two of those closures had, however, **never reached a store.** The prior run
recorded `repository_writes: 0` because no repository path was open to it, and
handed its changed graph parts over with the report instead. Measured on `main`
before this run: **235** edges, no `CF-C-10 → CF-E-10` edge, no
`role_vocabulary`. So the graph still asserted a CRD/Epic asymmetry the bodies
do not have, and the two `pf10_addendum_role` vocabularies were still unjoined.

Both were landed here, as a separate commit, applying an already-decided repair
rather than authoring a new one. Without this, criterion 2 would have been false
against the live artifact. Recorded as `B1-GBR-01` and `B1-GBR-02`.

## 5. Completion criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | All 11 have complete review rows and final dispositions | **MET** | §2 here, plus a clause-level row per finding in the contract ledger and a per-prompt readback row in the copy/repair ledger |
| 2 | CRD and Epic parallel where intended, explicitly different where required | **MET** | Measured from the rebuilt graph: `CF-C-10 → [CF-C-10, CF-C-20, CF-E-10, CF-PO-10, NATHAN_TERMINAL_RETURN]`, `CF-E-10 → [CF-C-10, CF-E-10, CF-E-20, CF-PO-10, NATHAN_TERMINAL_RETURN]`, symmetric `True`. The storage repairs were applied as exact mirrors: 4/4, 4/4, 9/9, 3/3 clauses across the `-10`/`-20`/`-30`/`-40` pairs. The one genuine lane difference, the Epic PF09 requirement, remains stated in CF-E-10 and correctly absent from CF-C-10 |
| 3 | Initial approvals not misclassified as PF10 addendum events | **MET** | Re-verified after edit: `INITIAL_APPROVE … emits no PF10 addendum` in both `-30` bodies; graph `never_for` contains `INITIAL_APPROVAL` |
| 4 | Material in-flight change produces exactly one standalone addendum | **MET** | `exactly_one_per_qualifying_approval: true`; producer set unchanged at `[CF-C-30, CF-E-30, ESC-40, IA-30, QA-70, RS-20]` after rebuild; the addendum field list is intact, with two storage references repointed and nothing added or dropped |
| 5 | Specification outputs give complete lawful intake to Batch 2 | **MET** | The only Batch 1 surface Batch 2 consumes is the `-30` `INITIAL_APPROVE` package. Its content is unchanged; the Specification and decision are now carried by repository path instead of Drive link. IA-10 independently resolves its own PFCanon/PF10 sources, which this handoff still does not fabricate |
| 6 | Manager/coordinator do not absorb other actors' authority | **MET** | MGMT-10 and MGR-10 changed only storage and reference clauses. Their input sets, prohibition lists, result vocabularies and prepare-only handoffs are untouched. The added open-path sentence removes an authority the old text implied rather than granting one |

## 6. Supersession of the five historical Batch 1 artifacts

Unchanged from v1.0 and restated for continuity. All five are preserved in
place; none was edited, renamed, replaced or trashed. The Drive IDs below are
**lineage** — they identify which historical artifact is superseded on which
point — and are correct as written.

| Artifact | Drive ID | Superseded on |
|---|---|---|
| Batch 1 Repair Report v1.0 (2026-09-15) | `1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-` | Its per-prompt ledger and its completion claim. §2 here replaces its disposition table |
| Batch 1 Contract Ledger v1.0 | `1Ej9MIKgejK69j-BorauRM14AE7mQffVX` | **Nothing.** Not superseded. It is the pre-edit review record and the authority that settled D3, D4's two declared fields, O1 and O2 |
| Batch 1 Copy/Repair Ledger v1.0 | `1bzRCUEBgmw0j-TAer_72xAATZBTH1q9r` | Its pending status only |
| Pre-Edit Closure Ledger v1.0 | `13K0F7S-eDTSYB54Bxo2dMDBQfm4dKC8h` | **Nothing.** Not superseded |
| Corrective Repair and Author Self-Assessment v1.0 | `1M7Ni7TGrZfIgHpCW1xlvPnKS9js0LazE` | Its scope limitation only |

The two ledgers written by **this** run — `gcfpe.batch-1.contract-ledger.md` and
`gcfpe.batch-1.copy-repair-ledger.md` — are new files under the current naming
convention. They do not replace the 2026-09-15 ledgers above, which remain the
pre-edit review record.

## 7. Open for Nathan — a decision, not a blocker

**Hardcoded canon tokens in the kickoff and Specification prompts.** Closing R1
established that a `schema_version` token in a prompt body is a hardcoded canon
reference under §4.5. Four Batch 1 prompts still carry one:

| Prompt | Token |
|---|---|
| CF-C-10, CF-E-10 | `schema_version: glow-kickoff/3.0` |
| CF-C-20, CF-E-20 | `schema_version: glow-specification/3.0` |

These were not repaired. No recorded defect covers them, and the authorization
forbids re-authoring beyond what a recorded defect supports. They also differ
from the delta case in one way that matters: these tokens are *defined* and a
consumer can validate against them, so they are not false conformance — they are
only hardcoded.

The question is whether §4.5's "do not hardcode canon" rule is meant to reach
existing defined tokens, or only to prevent inventing new ones. That is a
Product Owner call, not a derivation. If it reaches them, the same clause used
for the delta applies, and the change touches most of the 55 prompts rather than
these four — which makes it its own authorized pass, not a Batch 1 amendment.

Batch 1 does not wait on this and nothing downstream is blocked by it.

## 8. Graph

Rebuilt from parts with the `glow-graph-contract` builder. No file was
hand-edited and no hash was computed by hand.

```
python3 graph_parts.py build docs/graph/parts <scratchpad>
  WARNING  state_routes[RS-40]: declared route(s) with no backing edge: drain_verified
  build: 55 nodes, 236 edges, 55 state_routes
         embedded JSON 582287 bytes  sha256 5c45e58347c9e04f57105fc5d96a44d14ea2ee80003a5aa0a873d8ab440a1b70
         validation PASS
```

**Proof token — `edges 236 · embedded JSON 582287 B · sha256 5c45e583…`**

| | |
|---|---|
| Nodes | 55, unchanged |
| Edges | 235 on `main` → **236** (`CF-C-10 → CF-E-10`, `wrong_class_epic`) |
| state_routes | 55, derived from edges on build |
| Warnings | **One, and it is the expected one.** `RS-40.drain_verified`, the known Batch 3 orphan. No new warning |
| Built artifact | Written to the session scratchpad. **Not committed.** It is derived output |

Parts changed: `global.json` and `prompts/CF-C-10.json`. **53 prompt parts
untouched**, which is what makes the scope provable rather than asserted.

`predecessor_union_destinations` for CF-C-10 was deliberately left at
`['CF-C-20']`: it records the selected predecessor's destinations, and
`091326.2` did not have this branch.

### The `canonical_source_contract` decision

**Decided: add the location.** `pfcanon_root: docs/pfcanon` and
`pfcanon_access: READ_ONLY` were added. `pfcanon_authority` is unchanged at
`CONTROLLED_MARKDOWN_ONLY`.

Reason. The field was not wrong, but it was silent on where canon is, and after
this repair it would have been the only control still silent — all eleven bodies
now name `docs/pfcanon/` explicitly, and §9 requires supporting controls to be
synchronized to the repaired prompts. Naming a destination class is also exactly
what §4.5 asks for rather than what it forbids: the rule is against hardcoding
*canon* and *version tokens*, and it says in terms that prompts should "name the
destination class — `docs/ephemeral/`, `docs/pfcanon/`". `pfcanon_access` was
added with it because read-only is half the repair mapping for canon and a
location without it invites a write.

## 9. Prohibited-action confirmation

No write outside `docs/ephemeral/` and `docs/graph/`. `docs/pfcanon/` was not
written. The assembled graph was built to the scratchpad and is not committed.
No prompt outside the eleven was read for modification or modified. The selected
release `GCFPE-20260913.1 / 091326.2 / 54` was not mutated; no selected
predecessor was edited. PF10 was not read, edited or drained. The release
register, Alpha state, catalog, Flow Index and PR/CI state were untouched. No
historical Batch 1 artifact was edited, renamed or deleted. Batches 2–6 were not
executed and no Batch 2 handoff was prepared. No ChatGPT Library artifact or
Library ID was used. O3 was left alone as out of scope. Nothing was merged.
