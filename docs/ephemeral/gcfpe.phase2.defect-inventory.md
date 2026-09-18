---
artifact_type: GCFPE_PHASE2_DEFECT_INVENTORY
artifact_version: "1.0"
created_date: 2026-09-17
status: COMPLETE_FOR_ITS_PURPOSE
authority: Product Owner direction, 2026-09-17
governing_plan: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1, §6B Phase 3
scope: Batches 2-6, 44 prompts
instrument_version: "1.1"
canon_resolved: PF10-HDE-Build-Notes, addendum Specification format authority, read 2026-09-17
base_commit: c8f7eb5c12e3ef5cc343377db71054a726e1d925
findings: 174
coverage_rows: 308
decisions_for_product_owner: 6
batches_authorized: NONE
---

# GCFPE Phase 2 defect inventory — Batches 2–6

> ### ⚠️ Read as a dated record, not as current status
>
> Written before the cross-cutting drainage removal merged (2026-09-18, PR #415). Where
> this document reports something as *open, standing, deferred to a later batch, or the
> current contract*, check it against the merged baseline first. Specifically:
>
> - the **interim one-check replacement** (`pf10_reference_visibility_check`,
>   `PF10_REFERENCE_VISIBILITY`) was **struck** — no post-addendum check survives, and
>   neither token exists in `docs/graph/parts/global.json`;
> - the `RS-40.drain_verified` **orphan route is closed** and the builder emits no
>   warning;
> - the current graph proof token is **55 nodes · 227 edges · 55 state_routes**; any
>   235/236/240-edge token here is a dated measurement;
> - **Batch 2's blocker is dead** (decision record D10);
> - work deferred here "to Batches 2–5" for the drainage lifecycle was completed outside
>   the batch sequence by the cross-cutting repair.
>
> Current authority: `docs/prompt_ecosystem_management/gcfpe.decision-record.md`,
> `docs/prompt_ecosystem_management/authoritative-surfaces.md`, and
> `docs/ephemeral/gcfpe.drainage-removal.repair-report.md`.


What the parallel survey found across the 44 prompts Batch 1 does not own. This is
the Phase 3 input: total scope in one place, and the decisions that are the Product
Owner's rather than a batch's.

**No batch is authorized by this document.** Each still requires its own execution
authorization, as §6 requires.

## 1. What was measured

| | |
|---|---|
| Prompts surveyed | 44 of 44 |
| Coverage rows | 308 — every prompt × every check class |
| `NOT_CHECKED` rows | 0 |
| Raw mechanical hits handed to the agents | 1,646 |
| Findings returned | 174 |
| Quote-verification failures | 0 |

Discovery was precomputed mechanically by the coordinator and the agents classified
it, so coverage is arithmetic rather than trust: every hit is accounted for by a
coverage row or a finding.

## 2. Findings by class

| Class | Count |
|---|---|
| `STORAGE_ARCHITECTURE` | 102 |
| `PF10_ADDENDUM_POSTURE` | 46 |
| `LINEAGE_PRESERVED` | 13 |
| `GRAPH_BODY_RECONCILIATION` | 5 |
| `IMPLEMENTATION_PLAN_FORMAT` | 4 |
| `SPECIFICATION_FORMAT_AUTHORITY` | 4 |
| `TERMINOLOGY` | 1 |

Dispositions: 147 `REPAIR`, 13 `ESCALATE_SHARED_CONTRACT`, 13 `LINEAGE_PRESERVED`,
1 `BLOCKED`. Confidence: 160 HIGH, 13 MEDIUM, 1 LOW.

**The bulk is mechanical.** 102 of 174 are storage-architecture clauses — Drive-bound
canon resolution, saves routed to the former Drive folder, artifacts referenced by
Drive link. These are bounded edits against now-settled rules, not governance work.

## 3. Findings by batch

| Batch | Prompts | Findings | Heaviest prompts |
|---|---|---|---|
| 2 | 7 | 26 | IA-10 (8) |
| 3 | 10 | 52 | PR-10, PR-20, PR-40, RS-20, RS-40 (6 each) |
| 4 | 10 | 26 | QA-70 (5) |
| 5 | 9 | 29 | ESC-40 (7) |
| 6 | 8 | 41 | CL-20 (8), CL-40 (6) |

## 4. The six decisions for the Product Owner

Thirteen escalations reduce to six questions. None is a batch's to answer, and each
must land identically everywhere it reaches.

**D1 — The PF10 addendum storage and reference contract.**
The `PF10_BUILD_NOTES_ADDENDUM` record contract prescribes a direct Drive URL as the
reference form a future run must write. It is a machine-readable record contract, not
prose, and it is restated across roughly 27 prompts in four batches. One decision,
applied once.
*Raised by:* `B2-15` (IA-30), `B5-SA-20/21/22` (OPS-10/20/30), `B5-PA-01` (ESC-40).

**D2 — `pf10_addendum_contract.drain_owner` contradicts itself.**
The shared contract carries `drain_owner` as a value while listing `"drain_owner"` in
its own `forbidden_fields`. Carried forward unresolved from Batch 1. Binds CF-C-30,
CF-E-30, IA-30, RS-20, QA-70, ESC-40 — five batches.
*Raised by:* `B3-PAP-RS20-06` (RS-20).

**D3 — Does 2.14's Implementation Plan binding reach the detailed per-PR plan?**
2.14 routes "Epic or CRD Implementation Plan" structure to PF27 §12. PF04 §9.1.1 names
the concrete types as `EPIC_IMPLEMENTATION_PLAN` and `CRD_IMPLEMENTATION_PLAN`; the
detailed per-PR plan is a distinct artifact created later. Whether PR-20's ~25-field
list is a defect turns entirely on this.
*Raised by:* `B3-IPF-PR20-06` (PR-20).

**D4 — Producer role-vocabulary mismatch.**
`global.json` declares a qualifying producer's body token as
`QUALIFYING_DELTA_APPROVAL_PRODUCER`. **Four of the six declared producers disagree
with it, using three different values:** IA-30 says `QUALIFYING_PRODUCER`; RS-20, QA-70
and ESC-40 say `PRODUCER`. Only CF-C-30 and CF-E-30 — the two Batch 1 repaired — comply.
All non-producers are consistent at `NONPRODUCER`.

> **Corrected 2026-09-17.** This entry originally described a QA-70-only mismatch,
> raised by `B4-GBR-02`. Measured across all six producers it is four of six. The
> original scope was understated.
*Raised by:* `B4-GBR-02` (QA-70); scope corrected by direct measurement.

**D5 — Does PF27 govern Ops Task Record and Remediation Review Record structure?**
OPS-10/20/30 resolve PF27 by name for their artifact and then state their own field
lists; PF27 §3 carries "Ops Task record fields (required)". ESC-40 never names PF27
while PF27 §5 carries a Remediation Review Record template. If those sections govern,
four prompts both fail to resolve structure authority and restate structure.
*Raised by:* `B5-SF-01/02/03/04` (OPS-10/20/30, ESC-40).

**D6 — Should a declared non-producer restate the producer addendum contract?**
CL-20 is `NONPRODUCER` in its header and `NON_PRODUCER` in its graph part, yet restates
the full producer addendum contract including retired drainage-state fields. OPS-10/20/30
do the same for the storage route.
*Raised by:* `B6-PAP-04` (CL-20), and D1's OPS findings.

## 5. Verification status — stated plainly

Adversarial verification was run to completion for **Batch 2 only** and then stopped by
Product Owner direction, as disproportionate at the inventory stage. It belongs in
Phase 4, immediately before anything is edited.

| Batch | Findings | Verified | Confirmed | Refuted |
|---|---|---|---|---|
| 2 | 26 | 24 | 22 | 2 |
| 3 | 52 | 4 | 3 | 1 |
| 4, 5, 6 | 96 | 0 | — | — |

**Batch 2's rate is the only evidence of precision available: 22 of 24, about 92%.**
Applied to 174 findings that suggests roughly 160 are genuine, but that is an estimate
from one batch and is recorded as an estimate, not a measurement. The 146 unverified
findings are **unverified, not refuted** — the two are different and this inventory does
not conflate them.

Per-batch adversarial verification in Phase 4 remains required before any prompt is edited.

## 6. What this does not contain

- No prompt, graph part or canon file was changed by the survey. Phase 2 was read-only.
- The five completeness critiques did not run. Their absence is why §5 states an estimate
  rather than a coverage claim.
- Batch 1 is not re-surveyed here; it is closed at `BATCH_1_REPAIRED_WITH_CORRECTIONS`.

## 6A. Decisions taken

D1–D6 were ruled by the Product Owner on 2026-09-17. The rulings and their
consequences are recorded at
`docs/prompt_ecosystem_management/gcfpe.decision-record.md`, which supersedes §4 of
this inventory as the statement of what was decided. §4 remains the record of what
was *found*.

The largest consequence: **drainage is removed from prompt behaviour entirely**, as
one cross-cutting repair outside the six-batch sequence.

## 7. Recommended sequence

1. Product Owner rules on D1–D6. D1 and D2 reach the most prompts and should go first.
2. Apply the shared-contract decisions centrally, coordinator-owned, in one change.
3. Then batches in waves, each with its own authorization, its own adversarial
   verification pass, and its own pull request.

Batch 2 is the natural first implementation target: fully verified, 26 findings, and its
IA-10 carries the heaviest single concentration of Drive-bound routing in the survey.
