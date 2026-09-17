# GCFPE Batch 1 Repair Report

```yaml
artifact_type: GCFPE_BATCH_1_REPAIR_REPORT
artifact_version: "1.0"
report_date: 2026-09-17
authority: "Nathan / Product Owner, Batch 1 repair authorization, 2026-09-17"
repairs_validation: gcfpe.batch-1.validation-report.md
validation_drive_id: 1GXIatst9X17zKHnicwOMr4fXR3Q-eVlH
validation_sha256: 564aff9ec4b3e6fc823b840f2bbe2c48451682c21beb57906120fc1a4bc5027c
verdict: BATCH_1_BLOCKED
blockers: 2
scope: BATCH_1_ONLY
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
selected_release_mutated: false
repository_writes: 0
pf10_edited_or_drained: false
prompt_bodies_changed: 5
defects_fully_closed: 7
defects_partially_closed: 1
open_items_closed: 2
open_items_out_of_scope: 1
criteria_met: 6
criteria_not_met: 0
supersedes: 5
```

## 1. Verdict

**`BATCH_1_BLOCKED`.** Seven of the eight recorded defects are fully closed, the
eighth is partially closed, both in-scope open items are settled from source,
and all six Batch 1 completion criteria are now met. Two things could not be
completed from source and are returned rather than approximated:

- **R1 — D4's `schema_version`.** No source in the workspace declares a schema
  identifier for `SPECIFICATION_DELTA`. Two defensible values exist and they are
  not equivalent. Declaring one would be a schema-design decision, not a
  derivation.
- **R2 — the rebuilt graph cannot be persisted to Drive.** It is 583,125 bytes
  against a connector ceiling of roughly 150,000. This is the same measured
  limit already recorded against Batch 2, not a new finding.

Neither blocker is in the prompt bodies. All five edited prompts are persisted
and read back, and the graph rebuilds clean with no new warnings.

## 2. Per-prompt disposition, against the bodies as they now stand

| # | Prompt | Disposition | Defects closed | Clause that now satisfies it |
|---|---|---|---|---|
| 1.01 | GCFPE-MGMT-10 | **REPAIRED** | O1 | Entry contract rewritten as six annotated inputs, each carrying producer, owning authority and native availability point; "The relevant controls" now closed by the case |
| 1.02 | MGR-10 | **CONFIRMED_NO_CHANGE** | — | No recorded defect; body untouched |
| 1.03 | CF-PO-10 | **CONFIRMED_NO_CHANGE** | — | No recorded defect; body untouched |
| 1.04 | CF-C-10 | **REPAIRED** | D3, D6 | "A BLOCKED wrong-class result whose recorded selection is EPIC goes directly to **CF-E-10 — Prepare Epic Specification Kickoff Handoff — 091426.1**"; Required list now ends "…observed-problem source." |
| 1.05 | CF-C-20 | **CONFIRMED_NO_CHANGE** | — | No recorded defect; body untouched |
| 1.06 | CF-C-30 | **CONFIRMED_NO_CHANGE** | D5 (closed in global.json, not in the body) | Body token `QUALIFYING_DELTA_APPROVAL_PRODUCER` now declared and bound in `pf10_addendum_contract.role_vocabulary` |
| 1.07 | CF-C-40 | **REPAIRED_WITH_RESIDUAL** | D7, D4 (part) | "author one complete pending `artifact_type: SPECIFICATION_DELTA` with `state: SPECIFICATION_PENDING`"; new output-contract paragraph opening Required result and routing; "the complete denied pending CRD_SPECIFICATION_REF". **`schema_version` not declared — R1.** |
| 1.08 | CF-E-10 | **CONFIRMED_NO_CHANGE** | — | No recorded defect; body untouched. Its existing `wrong_class_crd` branch is the pattern D3 mirrored |
| 1.09 | CF-E-20 | **CONFIRMED_NO_CHANGE** | — | No recorded defect; body untouched |
| 1.10 | CF-E-30 | **REPAIRED** | D8 | All three `Epic_SPECIFICATION_REF` occurrences now `EPIC_SPECIFICATION_REF` |
| 1.11 | CF-E-40 | **REPAIRED_WITH_RESIDUAL** | D7, D8, D4 (part) | Same two D4 clauses as CF-C-40 in the EPIC variant; "the complete denied pending EPIC_SPECIFICATION_REF"; both `immutable approved EPIC_SPECIFICATION_REF` bullets. **`schema_version` not declared — R1.** |

Five bodies changed: GCFPE-MGMT-10, CF-C-10, CF-C-40, CF-E-30, CF-E-40. Six
unchanged. Every changed body was fetched fresh immediately before editing and
read back completely afterwards; in each readback the target clause is present
and no other section moved.

## 3. Defect closure

### D1 / D2 — the record defects. CLOSED by this report.
No single document assigned a disposition to each of the eleven prompts against
their current bodies. This report is that document: §2 carries a row per prompt
against the post-repair body, and §6 supersedes the five historical artifacts
by name. The plan page's Batch 1 line is updated to point here.

### D3 — CRD/Epic wrong-class asymmetry. CLOSED. Repair (a), symmetry.
**The decision gate was settled from source, not chosen.** Three independent
pieces of evidence in the Batch 1 Contract Ledger show the asymmetry was never
deliberate:

1. CF-C-10's own `supported_repair_contract` reads: *"BLOCKED only routes to a
   real recoverable same-owner/classification/**other-class** intake when
   complete; otherwise terminal Nathan."* The ledger **required** CF-C-10 to
   carry an other-class route. Its CF-E-10 counterpart is the same sentence.
2. `B1-C10-C2` and `B1-E10-C2` are word-for-word identical, both naming
   *"Self-recovery and **class redirection**"*. The finding was raised against
   both lanes equally.
3. At review time the ledger recorded CF-E-10's `downstream_dependencies` as
   including `CF-C-10`, and CF-C-10's as not including `CF-E-10` — the
   asymmetry was an *observed* state the repair contract then required to be
   fixed. The 2026-09-15 pass applied it to the Epic lane only.

So the sources settle it: the lanes were specified symmetric. Repair (b),
documenting a difference, would have documented a defect as if it were intent.

CF-C-10 now carries the reciprocal branch, mirroring CF-E-10's wording,
placement and link form exactly. The graph part carries the matching
`wrong_class_epic` edge to `CF-E-10`, in the mirrored `state_route_order`
position. Measured after rebuild:

```
CF-C-10 destinations: CF-C-10, CF-C-20, CF-E-10, CF-PO-10, NATHAN_TERMINAL_RETURN
CF-E-10 destinations: CF-C-10, CF-E-10, CF-E-20, CF-PO-10, NATHAN_TERMINAL_RETURN
lanes symmetric: True
```

### D4 — undeclared SPECIFICATION_DELTA. PARTIALLY CLOSED. See R1.
Two of the three fields are settled by source and are now declared in both
bodies:

- **`artifact_type: SPECIFICATION_DELTA`** — Contract Ledger, CF-C-40 and
  CF-E-40 `supported_repair_contract`: *"Both SPECIFICATION_PENDING;
  **artifact_type distinguishes modes**."* Copy/Repair Ledger `B1-C40-T1` and
  `B1-E40-T1`: *"Generic result and next-step text obscures **two artifact
  types** under SPECIFICATION_PENDING."*
- **`state: SPECIFICATION_PENDING`** — same clause, *"**Both**
  SPECIFICATION_PENDING"*. This confirms the validation's judgment that the
  graph's `result_states = ['SPECIFICATION_PENDING']` was the intended value and
  the prompts were at fault for not stating it. The graph value is now
  supported by a stated token rather than by inference.

Both bodies now open Required result and routing with an explicit output
contract naming both artifact types, their shared state, and `artifact_type` as
the sole discriminator.

**`schema_version` is not declared, and was not invented.** Searched for a
delta schema identifier across the live graph, the Contract Ledger, the
Copy/Repair Ledger, the Pre-Edit Closure Ledger, the Corrective report, the
current bodies and the selected predecessor `CF-C-40 — 091326.2`. The entire
schema vocabulary in the workspace is two tokens, `glow-specification@3.0` and
`glow-kickoff@3.0`. Neither denotes a delta. The predecessor describes the
artifact as *"a standalone `SPECIFICATION_DELTA`, not a successor
Specification"* and assigns it no schema either. Returned as R1.

### D5 — undeclared `pf10_addendum_role` vocabulary. CLOSED.
The field had no controlled vocabulary in `global.json`, so neither the graph's
`NON_PRODUCER` / `QUALIFYING_PRODUCER` nor the bodies'
`NONPRODUCER` / `QUALIFYING_DELTA_APPROVAL_PRODUCER` was authoritative and the
two could not be joined. `pf10_addendum_contract.role_vocabulary` now declares
both values, their meanings, and the `prompt_body_token` each binds to.

Neither representation was rewritten. Changing the graph's 55 node tokens or the
bodies' tokens would have reached 44 prompts outside this authorization; binding
them closes the defect within scope. The producer set is untouched and verified
unchanged after rebuild: `[CF-C-30, CF-E-30, ESC-40, IA-30, QA-70, RS-20]`.

### D6 — CF-C-10 dangling conjunction. CLOSED.
`"…observed-problem source; and"` → `"…observed-problem source."`

### D7 — doubled class token. CLOSED.
`"the complete denied pending CRD CRD_SPECIFICATION_REF"` → `"…pending
CRD_SPECIFICATION_REF"`. `"the complete denied pending Epic
Epic_SPECIFICATION_REF"` → `"…pending EPIC_SPECIFICATION_REF"`.

### D8 — inconsistent identifier casing. CLOSED.
All `Epic_SPECIFICATION_REF` occurrences are now `EPIC_SPECIFICATION_REF`: three
in CF-E-30, three in CF-E-40. The Epic lane now matches the CRD lane's
SCREAMING snake case throughout.

## 4. Open items

### O1 — MGMT-10 entry inputs. CLOSED, from source.
The Contract Ledger's `input_inventory` for GCFPE-MGMT-10 supplies a producer,
authority, native availability point and absence behaviour for every input. The
Entry contract is rewritten as six annotated bullets carrying those values.

"The relevant controls" is now closed rather than open-ended, using the ledger's
own phrase *"affected source/control/receiver contracts"* together with the
enumeration already present in MGMT-10's Batch method step 1: *"the candidate,
its selected predecessor, the governing plan, the catalog, the Flow Index, and
any further control whose repaired external identity, input/output contract,
handoff or graph binding the case actually changes. Nothing outside that set is
in scope."* No value was invented; each traces to the ledger or to the prompt's
own step 1.

### O2 — MGMT-10 batch mode has no graph representation. SETTLED: deliberate. No graph change.
Three sources agree the graph is intentionally silent on the governance mode:

1. MGMT-10's `supported_repair_contract`: *"**Approved plan controls exact batch
   scope and result/report vocabulary.**"* The batch vocabulary lives in the
   plan, by design, not in the reusable graph.
2. The ledger records `observed_result_states` for MGMT-10 as exactly the four
   reusable states, as the complete observed set, while separately requiring
   *"One next-batch repair handoff only when plan predicates are met"* — the
   handoff is a case-scoped output, not a graph state.
3. The Corrective report's Defect C verification says it directly: *"No manager
   graph state change was needed because the persisted graph already contained
   no fixed Batch 1 state."* A prior pass considered this exact question and
   decided against adding batch states.

The validation could not settle this from the body and the graph alone and was
right not to guess. With the ledger and the corrective report added, it settles.
**No part was changed and no edge was added for MGMT-10.**

### O3 — 4-byte builder delta. OUT OF SCOPE, not pursued.
Belongs to Batch 2 by the authorization. Recorded, untouched.

## 5. Completion criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | All 11 have complete review rows and final dispositions | **MET** | §2 of this report: a disposition row per prompt against the post-repair body, with the exact clause satisfying each closed defect. §6 supersedes the five prior artifacts by name |
| 2 | CRD and Epic parallel where intended, explicitly different where required | **MET** | D3 closed by symmetry, settled from CF-C-10's own `supported_repair_contract`. Measured after rebuild: both lanes carry the reciprocal wrong-class edge. The one genuine lane difference, the Epic PF09 requirement, remains explicitly stated in CF-E-10 and correctly absent from CF-C-10 |
| 3 | Initial approvals not misclassified as PF10 addendum events | **MET** | Unchanged by this repair and re-verified: `INITIAL_APPROVE … emits no PF10 addendum` in both -30 bodies; IA-10 agrees; graph routes `initial_approve` to IA-10 and only `delta_approve` to `NATHAN_MANUAL_PF10_DRAIN`; `never_for` contains `INITIAL_APPROVAL` |
| 4 | Material in-flight change produces exactly one standalone addendum | **MET** | Unchanged and re-verified: `exactly_one_per_qualifying_approval = true`; producer set confirmed unchanged after the D5 rebuild; the 20 required fields still match the bodies field for field |
| 5 | Specification outputs give complete lawful intake to Batch 2 | **MET** | Re-run against IA-10 `FIRST_ENTRY` after the repair. The only Batch 1 surface Batch 2 consumes is the -30 `INITIAL_APPROVE` package, which this repair did not touch. D4's new clauses are confined to the -40 prompts, which route to -30, not to IA-10 |
| 6 | Manager/coordinator do not absorb other actors' authority | **MET** | MGMT-10's Entry contract was annotated, not widened. The six inputs, the prohibition list, the reusable result vocabulary and the prepare-only PR-10 handoff are unchanged. The added text assigns authority to Nathan, the catalog and the controlled source owners — it grants none to this prompt |

## 6. Supersession of the five historical Batch 1 artifacts

All five are preserved in place. None was edited, replaced, re-ID'd or trashed.
Each is superseded only on the points named.

| Artifact | Drive ID | Superseded on |
|---|---|---|
| Batch 1 Repair Report v1.0 | `1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-` | **Its per-prompt ledger and its completion claim.** It describes pre-corrective bodies: its CF-C-20/CF-E-20 rows assert delta-authoring the current bodies forbid, and its claim that the graph lists `SPECIFICATION_DELTA` for C/E-20 is false against the live artifact. §2 of this report replaces its disposition table. Its record of the 2026-09-15 edits remains historical evidence |
| Batch 1 Contract Ledger v1.0 | `1Ej9MIKgejK69j-BorauRM14AE7mQffVX` | **Nothing.** Not superseded. It is the pre-edit review record and it is the authority that settled D3, D4's two declared fields, O1 and O2 in this pass. Its `repair_disposition: NOT_YET_APPLIED` rows are now answered by §2 |
| Batch 1 Copy/Repair Ledger v1.0 | `1bzRCUEBgmw0j-TAer_72xAATZBTH1q9r` | **Its pending status only.** Its `disposition: PENDING` and `complete_readback: PENDING` rows for the five changed prompts are answered by §2. Its copy findings stand and were used as evidence for D4 |
| Pre-Edit Closure Ledger v1.0 | `13K0F7S-eDTSYB54Bxo2dMDBQfm4dKC8h` | **Nothing.** Not superseded. Defects A, B and C remain correctly recorded and correctly closed by the corrective pass |
| Corrective Repair and Author Self-Assessment v1.0 | `1M7Ni7TGrZfIgHpCW1xlvPnKS9js0LazE` | **Its scope limitation only.** Its `batch_1_completion_claim: SUPPORTED_ONLY_WITHIN_STATED_LIMITED_AUTHOR_SELF_REVIEW_SCOPE` and `independent_verification: false` are now answered: an independent validation ran on 2026-09-17 and this repair closed its findings. Its Defect A/B/C record stands and settled O2 |

The two ledgers and the Pre-Edit Closure Ledger are **not** superseded in
substance. They were right. What was missing was a current document tying them
to the bodies as they now stand.

## 7. Graph rebuild

Built from parts with `graph_parts.py build`. No file was hand-edited and no
hash was computed by hand; the builder stamps the header over the byte range it
describes.

```
python3 graph_parts.py build <parts> <out>
  WARNING  state_routes[RS-40]: declared route(s) with no backing edge: drain_verified
  build: 55 nodes, 236 edges, 55 state_routes
         embedded JSON 582526 bytes  sha256 45e8aa3f…
         validation PASS
```

| | |
|---|---|
| Nodes | 55, unchanged |
| Edges | 235 → **236** (+1: `CF-C-10 → CF-E-10`, `wrong_class_epic`) |
| state_routes | 55, derived from edges on build |
| Embedded JSON | 582,526 bytes · `45e8aa3f2121afe3a3162a8be9114e3d19ff11b1a79cbf6e1b3594fd2d8556db` |
| Whole file | 583,125 bytes · `25694ff1dca910877828d27d69c0ff32e72c30fdb9d26b1ce1935b539c84309d` |
| Warnings | **One, and it is the expected one.** `RS-40 drain_verified`, the known Batch 3 orphan. **No new warning appeared** |

Parts changed: `prompts/CF-C-10.json` (one edge added, one `state_route_order`
entry) and `global.json` (`role_vocabulary` added). 53 prompt parts untouched,
which is what makes the scope provable rather than asserted.

`predecessor_union_destinations` for CF-C-10 was deliberately **not** changed.
It records the selected predecessor's destinations, and the predecessor did not
have this branch; editing it would have made a false claim about `091326.2`.

## 8. Blockers returned to Nathan

### R1 — `SPECIFICATION_DELTA` has no `schema_version`, and no source supplies one
Both candidate values are defensible and they are not interchangeable:

- **`glow-specification/3.0`**, the same token the base Specification carries.
  *For:* the ledger says `artifact_type` is what distinguishes the modes, which
  implies the other identity fields are shared; both artifacts are reviewed by
  the same reviewer in the same lineage. *Against:* that token denotes the
  "unchanged thirteen-section schema", and the delta's field set is different —
  immutable base, bounded overlay, affected surfaces, exclusions, evidence,
  conflicts, unresolved items, return phase. The label would assert a conformance
  that does not hold.
- **A new token, e.g. `glow-specification-delta/3.0`.** *For:* follows the
  `glow-<kind>/<version>` convention exactly and describes the actual shape.
  *Against:* nothing defines it. Minting it creates a schema identifier that no
  consumer can validate against, and CF-C-30 / CF-E-30 currently accept "one
  pending SPECIFICATION_DELTA" with no schema check.

**What is needed:** your decision on which, and if the second, whether the delta
field list in CF-C-40/CF-E-40 step 3 becomes that schema's definition. Once
decided this is a two-line edit to each -40 body and closes D4 completely.

### R2 — the rebuilt graph cannot be persisted to Drive
583,125 bytes against a reliable `create_file` ceiling of roughly 150,000. This
is the connector's measured capability, already recorded against Batch 2, not a
new discovery and not a method problem: `update_file` has no content parameter
at all, so there is no content-write for the existing ID
`1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp`.

**Consequence, stated plainly:** the live Drive graph is now stale against the
repaired prompts. It holds 235 edges, no `CF-C-10 → CF-E-10` edge and no
`role_vocabulary`. Graph/prompt agreement for CF-C-10 is broken until the
rebuilt graph is persisted. Everything needed to persist it exists and is
reproducible — the changed parts, the builder, and the stamped hash above.

**What is needed:** the storage decision the plan already records as open for
Batch 2. The rebuilt graph and both changed parts are handed over with this
report rather than written anywhere unauthorized.

## 9. Prohibited-action confirmation

No repository write, commit, branch, tag or PR. No file written inside any
cloned repository. The candidate graph was never hand-edited; every change went
through a part and the builder. No prompt outside the eleven was read for
modification or modified. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not mutated; no selected predecessor was
edited. PF10 was not read, edited or drained. The release register, Alpha state,
catalog and Flow Index were untouched. No historical Batch 1 artifact was
edited, replaced or trashed. Batches 2–6 were not executed and no Batch 2
handoff was prepared. No ChatGPT Library artifact or Library ID was used. O3 was
left alone as out of scope.
