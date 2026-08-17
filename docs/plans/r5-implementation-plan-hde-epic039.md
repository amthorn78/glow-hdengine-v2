# Artifact Map

Document revision: r5

Implementation Guide: r6-epic-plan-hde-epic039.md

Caveats: None provided

Codex Planning Audit: implementation-audit-epic039.md

Repository: amthorn78/glow-hdengine-v2

Repository access mode: Connector

Default branch: main

Planning baseline commit: c20c788baa46312f2d88691b7264caec29d313a0

Canon root: docs/pfcanon

PF10 source set: PF10-HDE-Build-Notes

PF27 template source: PF27-Canon-Plan-Templates §12 General Implementation Plan (Template)

Canon validation: Complete

Repository validation: Complete at pinned planning baseline

Output: Implementation Plan (PRs \+ OPS tasks \+ PF09 Completion Scope \+ Crosswalk \+ Codex Prompts)

# Brief recap of scope

HDE-EPIC039 completes five ordered Calcination workstreams: canonical JSON and schema-declared set consolidation; evidence-ledger convergence; reusable QA-harness hardening; removal and reclassification of HDE-EPIC038 closeout and CI machinery; and an epic-agnostic, feedback-free closeout-candidate lifecycle.

The implementation uses five PR tasks and no OPS tasks. PR-04 requires a bounded execution-ref classification of every current CI control before edits, and PR-05 depends on PR-04. No PF09 item is already complete and reused: all nine mapped subtasks remain open as Consolidation pending, Partial, or Not done. This plan makes no QA PASS, acceptance, token-satisfaction, PF09-status, OPS-completion, or closeout claim.

# Canon Applicability Snapshot

PF01-Canon-HDE-Math-Spec \- Not applicable

PF02-Canon-HDE-Architecture \- Applied \- Effect: Preserves component single homes, repository tooling boundaries, and offline evidence-plane separation.

PF03-Reference-Technical-Writing-Best-Practices \- Applied \- Effect: Requires source-grounded, portable implementation instructions and accurate claim posture.

PF04-Canon-HDE-Governance \- Applied \- Effect: Owns acceptance-token identities, canonical-gate governance, evidence parity, and nonclaim posture.

PF05-Canon-HDE-CLI-API-Vendor-Ref \- Applied \- Effect: Owns supported interpreter posture for the legacy-named Python mirror checker.

PF06-Canon-Epic-Process-Guide \- Applied \- Effect: Requires PR-first delivery, assigned PF09 completeness, lane separation, and feedback-free terminal reachability.

PF07-Canon-Glow-Infrastructure \- Not applicable

THE HUMAN DESIGN SYSTEM \- Not applicable

PF09.1-Canon-HDE-Build-Checklist-Calcination \- Applied \- Effect: Supplies all nine task identities, source statuses, ordering, and completion scope.

PF09.2-Canon-HDE-Build-Checklist-Dissolution \- Not applicable

PF09.3-Canon-HDE-Build-Checklist \- Not applicable

PF09.4-Canon-HDE-Build-Checklist-Conjunction \- Not applicable

PF09.5-Canon-HDE-Build-Checklist-Fermentation \- Not applicable

PF09.6-Canon-HDE-Build-Checklist-Distillation \- Not applicable

PF09.7-Canon-HDE-Build-Checklist-Coagulation \- Not applicable

PF10-HDE-Build-Notes - Applied - Effect: Addendum 2.3 controls continuing-risk justification, CI lane placement, HDE-EPIC039 CI remediation, and source-writeback prohibition; Addendum 2.4 controls local-first validation, coherent remote-update batching, the five-update circuit breaker, exact-final-head validation, and CI-triggering update reporting for autonomous agents; Addendum 2.5 makes budget-efficient structural CI remediation a mandatory HDE-EPIC039 execution requirement and completion condition, including duplicate and superseded execution control, change-aware and event-aware heavy work, required-check continuity, repeated-setup justification, before-and-after execution-shape proof, and the required validation matrix.

RAVE I CHING \- Not applicable

PF12-Canon-HDE-Schemas-and-Artifacts \- Applied \- Effect: Owns canonical bytes, set identity rules, close-pack paths, ledger/proof coherence, and acyclic attestation behavior.

PF13-Reference-Glow Development Philosophy v1 \- Reference-only

PF14-Canon-HDE-Mechanics-Guide \- Applied \- Effect: Owns canonicalization, evidence tooling, QA harnesses, and release/provenance mechanics.

Glow Tonality Guide v1.1: Writing for Human Connection \- Not applicable

PF16‑Canon — HD Engine Epics Map \- Historical-only

PF17-Canon-HDE-Narratives-Guide \- Not applicable

PF18‑Reference‑HDE‑Narrative Deliverables \- Not applicable

PF19-Canon-Glow-QA-Guide \- Applied \- Effect: Owns current-state QA evidence, the five-status vocabulary, tooling-versus-behavior classification, and empty-output failure rules.

PF20-Reference-HDE-Phased Epics \- Historical-only

7 Phases of Alchemical Engineering \- Applied \- Effect: Confirms Calcination as the removal-and-consolidation phase.

PF23-Canon-Reality-Audits \- Reference-only

PF27-Canon-Plan-Templates \- Applied \- Effect: Owns this Implementation Plan structure, QA status routing, and terminal-reachability proof posture.

PF29-Canon-HDE-Users-Guide \- Not applicable

# PF09 Completion Scope

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC002 PF09 subtask ID: HDE-CALC002.2 PF09 source status: Consolidation pending Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-01 Implementation Guide item(s): D1 Caveat ID(s): None Proof pointer: Observed repo reality: tools/evidence/run\_canonical\_json\_gate.py and tests/evidence/test\_canonical\_json\_gate\_check\_outputs.py. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: PR-01 must complete the full canonical-byte requirement; repository presence and passing-looking historical artifacts do not move PF09 status.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC002 PF09 subtask ID: HDE-CALC002.3 PF09 source status: Consolidation pending Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-01 Implementation Guide item(s): D1 Caveat ID(s): None Proof pointer: Observed repo reality: engine/mech/helpers.py, tools/evidence/generate\_arrays\_as\_sets\_report.py, schemas/channels\_v1.schema.json, and tests/compare/test\_arrays\_as\_sets.py. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: Existing string-only `sorted(set(...))` behavior does not prove schema-driven object identity, conflicting-identity refusal, or complete target coverage.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.10 PF09 source status: Partial Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-02 Implementation Guide item(s): D2 Caveat ID(s): None Proof pointer: Observed repo reality: tools/evidence/update\_evidence\_index.py, ci/checks/check\_mirror\_schema.sh, and .github/workflows/ci.yml. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: Existing fixed-point and transaction foundations are retained, but final-byte, ownership, and CI-lane behavior must be completed.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.11 PF09 source status: Partial Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-02 Implementation Guide item(s): D2 Caveat ID(s): None Proof pointer: Observed repo reality: tools/evidence/update\_evidence\_index.py, tools/evidence/orientation\_demo.py, tests/evidence/test\_machine\_mirror\_self\_proof.py, and tests/evidence/test\_orientation\_demo.py. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: PR-02 must establish one authorized write followed only by non-writing final-state checks.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.13 PF09 source status: Partial Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-03 Implementation Guide item(s): D3 Caveat ID(s): None Proof pointer: Observed repo reality: .github/workflows/ci.yml and tools/qa/epic021\_qa.py. Support: pinned connector inspection found active `python -m pytest` calls but retained run-identity harness behavior at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: Historical transcripts remain immutable; only active executable tooling and tests are changed.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.14 PF09 source status: Partial Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-03 Implementation Guide item(s): D3 Caveat ID(s): None Proof pointer: Observed repo reality: tools/qa/qa\_harness.py, tools/qa/epic021\_qa.py, tools/qa/generate\_epic027\_close\_pack.py, and tools/qa/generate\_epic029\_close\_pack.py. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: Current paths, timestamps, run IDs, and unconstrained status strings require replacement with stable check-centric behavior.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.15 PF09 source status: Partial Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-03 Implementation Guide item(s): D3 Caveat ID(s): None Proof pointer: Observed repo reality: tools/qa/qa\_harness.py and tests/qa/test\_generic\_qa\_harness.py. Support: pinned connector inspection found uncaught missing-input paths and insufficient reference validation at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: PR-03 implements reusable viability mechanics only; it does not run Live QA or produce a QA verdict.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.21 PF09 source status: Not done Plan disposition: Complete in this epic Repository posture: Existing implementation observed; completion not claimed Implementing task ID(s): PR-04 Implementation Guide item(s): D4 Caveat ID(s): None Proof pointer: Observed repo reality: tools/evidence/generate\_hde\_epic038\_closeout.py, tools/evidence/check\_hde\_epic038\_qa\_current\_state.py, their focused tests, tools/evidence/update\_evidence\_index.py, and .github/workflows/ci.yml. Support: pinned connector exact-file and complete-workflow inspection at c20c788baa46312f2d88691b7264caec29d313a0. ADR ID: None PF07 prerequisite: None Notes: Removal is conditional on a complete execution-ref consumer and PF10 Addendum 2.3 classification; history and formal nonclaims remain intact.

PF09 document: PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID: HDE-CALC003 PF09 subtask ID: HDE-CALC003.22 PF09 source status: Not done Plan disposition: Complete in this epic Repository posture: Planned output Implementing task ID(s): PR-05 Implementation Guide item(s): D5 Caveat ID(s): None Proof pointer: NA \- the complete pinned tree contains no tools/qa/generate\_epic\_close\_pack.py; PR-05 creates the approved epic-agnostic capability after PR-04. ADR ID: None PF07 prerequisite: None Notes: The lifecycle supplies generation and validation mechanics only; it cannot close an epic, satisfy tokens, establish QA PASS, or perform Product Owner closeout.

# Crosswalk: IG items \-\> Plan tasks

| Implementation Guide work item | Caveats applied | PF09 document(s) | PF09 task ID(s) | PF09 subtask ID(s) | Primary disposition | Implementation task(s) | Evidence pointer | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| D1 — Canonical serialization and set-array consolidation | None | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC002 | HDE-CALC002.2; HDE-CALC002.3 | Planned in PR task(s) | PR-01 | Observed repo reality: canonical-gate and arrays-as-sets loci; planned refresh of their existing governed output families | Planned |
| D2 — Evidence-ledger parity and touch discipline | None | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.10; HDE-CALC003.11 | Planned in PR task(s) | PR-02 | Observed repo reality: Human Index, sentinel, Machine Mirror, orientation, proof, and mirror-checker loci | Planned |
| D3 — Reusable QA invocation and viability hardening | None | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.13; HDE-CALC003.14; HDE-CALC003.15 | Planned in PR task(s) | PR-03 | Observed repo reality: generic harness, active wrappers, and generic-harness tests | Planned |
| D4 — HDE-EPIC038 closeout subsystem removal | None | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.21 | Planned in PR task(s) | PR-04 | Observed repo reality: active HDE-EPIC038 generator, validators, tests, updater bindings, receipt flow, and CI workflow | Planned |
| D5 — Feedback-free generic closeout lifecycle | None | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.22 | Planned in PR task(s) | PR-05 | Proposed path: tools/qa/generate\_epic\_close\_pack.py | Planned |

# Blocking questions

NO BLOCKING QUESTIONS.

# Execution plan

1. Task ID: PR-01 Intent: Consolidate canonical governed JSON and schema-declared set-array behavior. Depends on: None Implementation Guide item(s): D1 Caveat ID(s): None PF09 document(s): PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID(s): HDE-CALC002 PF09 subtask ID(s): HDE-CALC002.2; HDE-CALC002.3 PF09 completion role: Completes PF09 item in this epic Bounded prerequisite: None Continuation rule: Continue only after the execution-ref drift check confirms the canonical-gate, schemas, catalogs, tests, and controlling canon differ only by expected predecessor-independent changes.  
     
2. Task ID: PR-02 Intent: Make the evidence skeleton atomic, convergent, and final-byte checkable. Depends on: PR-01 Implementation Guide item(s): D2 Caveat ID(s): None PF09 document(s): PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID(s): HDE-CALC003 PF09 subtask ID(s): HDE-CALC003.10; HDE-CALC003.11 PF09 completion role: Completes PF09 item in this epic Bounded prerequisite: None Continuation rule: Account for the approved PR-01 diff, classify every D2 CI control under PF10 Addendum 2.3, and stop without partial edits if a safe final-state write/check sequence cannot be established.  
     
3. Task ID: PR-03 Intent: Replace run-oriented and phantom-pass harness behavior with stable current-state QA mechanics. Depends on: PR-02 Implementation Guide item(s): D3 Caveat ID(s): None PF09 document(s): PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID(s): HDE-CALC003 PF09 subtask ID(s): HDE-CALC003.13; HDE-CALC003.14; HDE-CALC003.15 PF09 completion role: Completes PF09 item in this epic Bounded prerequisite: None Continuation rule: Account for PR-01 and PR-02, preserve historical evidence bytes, and stop if active callers cannot be migrated without changing Live QA or acceptance scope.  
     
4. Task ID: PR-04 Intent: Classify the complete current CI graph, make hosted CI materially more budget-efficient, and remove the withdrawn HDE-EPIC038 closeout subsystem while preserving independently justified protection. Depends on: PR-03 Implementation Guide item(s): D4 Caveat ID(s): None PF09 document(s): PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID(s): HDE-CALC003 PF09 subtask ID(s): HDE-CALC003.21 PF09 completion role: Completes PF09 item in this epic Bounded prerequisite: None Continuation rule: Before edits, classify every execution-ref trigger, job, step, matrix, condition, permission, `needs` edge, artifact transfer, repeated setup or validation, and direct or indirect writer against all ten PF10 Addendum 2.3 questions and establish the execution-ref cost shape required by PF10 Addendum 2.5. Implement and validate the smallest safe changes that eliminate duplicate equivalent full-suite eligibility, avoidable superseded work, irrelevant heavy execution, and unjustified repeated setup while preserving required-check continuity, truthful success, rapid feedback, exact-final-head assurance, and every independently justified protection. Complete the PF10 Addendum 2.5 validation matrix and before-and-after event-to-job execution shape in the implementation report, and apply PF10 Addendum 2.4 remote-update discipline. If any disposition, required-check dependency, repository-setting dependency, or material reduction cannot be safely established, fail closed and do not start PR-05.
     
5. Task ID: PR-05 Intent: Implement an epic-agnostic, feedback-free closeout-candidate writer/checker and isolated hosted validation lane. Depends on: PR-04 Implementation Guide item(s): D5 Caveat ID(s): None PF09 document(s): PF09.1-Canon-HDE-Build-Checklist-Calcination PF09 task ID(s): HDE-CALC003 PF09 subtask ID(s): HDE-CALC003.22 PF09 completion role: Completes PF09 item in this epic Bounded prerequisite: None Continuation rule: Continue only after PR-04 proves the obsolete receipt-feedback path is absent and the retained evidence/release controls have stable, non-writing ownership.

# PR series

## PR-01 \- Consolidate canonical JSON and schema-declared sets

Title: Consolidate canonical JSON and schema-declared sets

Intent: Establish one current Calcination implementation for canonical governed JSON and set arrays without changing Human Design meaning or ordered-array semantics.

Implementation Guide source items: D1

Approved requirement:

* Enforce UTF-8 without BOM, recursively ASCII-sorted object keys, compact separators, schema-valid values, and exactly one trailing LF.  
* Treat an array as a set only when its owning schema or PF12-owned binding declares set semantics and an identity.  
* Collapse byte-identical duplicates, reject conflicting values with the same identity, and order identities by strict ASCII without locale transformation.  
* Replace omission-prone gate coverage with a deterministic inventory of every governed target in D1’s Calcination scope.  
* Keep the authoritative `audit/gates/json_gate/canonical/` family coherent with every still-produced supplemental output under `audit/gates/canonical_json/`.  
* Make the arrays-as-sets report deterministic, mechanically generated, checkable, and covered by positive and fail-closed tests.  
* Preserve Gate, Channel, Line, Profile, Authority, BodyGraph, score, band, narrative, and ordered-array meaning.

Caveats applied: None

PF09 document(s), task IDs, and proof excerpts:

PF09.1-Canon-HDE-Build-Checklist-Calcination, HDE-CALC002:

> ## **Task HDE-CALC002 — Canonical Serialization Package**

> **Task name/label:** Canonical Serialization Package  
>   
> **Task status:** **Partial**

PF09 subtask IDs and proof excerpts:

HDE-CALC002.2:

> **Subtask name/label:** Canonical JSON rules for public bytes  
>   
> **Subtask description:** Enforce canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, consistent float serialization, no extra whitespace, and exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted.  
>   
> **Subtask status: Consolidation pending**

HDE-CALC002.3:

> **Subtask name/label:** Arrays-as-sets discipline  
>   
> **Subtask description:** Deduplicate and ASCII-sort arrays that function as sets before hashing or comparison.  
>   
> **Subtask status: Consolidation pending**

PF09 completion role: Completes PF09 item in this epic

PF14 or owning-canon pointers and proof excerpts:

PF14-Canon-HDE-Mechanics-Guide §4:

> Canonical JSON. UTF-8 (no BOM); ASCII-sorted keys; compact separators (, and : only); exactly one trailing LF (\\n). Arrays that function as sets are deduplicated and ASCII-sorted by identity.  
>   
> Single source of bytes. The same canonical serializer is used for Reader responses, CLI stdout on parity surfaces, and machine-generated evidence artifacts.  
>   
> Determinism. AB↔BA parity and two-run identity MUST hold for identical inputs/environment. Run all canonicalization and byte-compares with LC\_ALL=C, LANG=C, TZ=UTC.

PF14-Canon-HDE-Mechanics-Guide §5.1:

> Locale-free, bytewise order. All string ordering is ASCII byte order (code-point ascending), case-sensitive, under LC\_ALL=C. No locale collation; no Unicode normalization.  
>   
> Stable total order. Comparators are antisymmetric, transitive, and total (every pair comparable). Equal inputs are stable (no reordering of equals).  
>   
> Arrays-as-sets discipline. When an array is used as a set: dedupe by identity, then ASCII-sort with the appropriate comparator; never rely on map/set iteration order.

PF12-Canon-HDE-Schemas-and-Artifacts §4.2:

> This discipline applies only when the owning schema defines an array as a set. An ordered array retains its schema-declared order.  
>   
> The schema MUST define an identity rule:  
> 

> * A scalar's identity is its value.  
> 1. Project each element to its canonical identity without trimming, case conversion, locale transformation, or other value change.  
> 2. If one identity repeats with byte-identical elements, retain one element.  
> 3. If one identity repeats with different element values, fail closed and identify the first divergent field.  
> 4. Sort the remaining elements in strict ASCII ascending identity order.

>   
> Producers MUST write the normalized order; validators reject duplicates, conflicts, and out-of-order sets.

PF07 facts, prerequisites, or reconciliation posture: PF07-Canon-Glow-Infrastructure is not applicable. No infrastructure value or operational dependency is introduced.

Dependencies: None

Observed repo reality:

* Observed repo reality: tools/evidence/run\_canonical\_json\_gate.py contains a fixed 13-entry `TARGETS` tuple and produces both current gate families. Support: pinned connector exact-file inspection at c20c788baa46312f2d88691b7264caec29d313a0.  
* Observed repo reality: engine/mech/helpers.py implements string-only `dedupe_sort` as `sorted(set(seq))`. Support: pinned connector exact-file inspection at the planning baseline.  
* Observed repo reality: schemas/channels\_v1.schema.json declares `uniqueItems` for `domains` and `flags`, but not `centers`, and lacks the PF12-required `$id`. Support: pinned connector exact-file inspection.  
* Observed repo reality: catalog/gates\_v1.json and catalog/channels\_v1.json lack final LF. Support: pinned connector byte inspection.  
* Observed repo reality: catalog/manifest.json currently records `version` as `1.0.0` and `built_at_utc` as `2025-12-26T00:00:00Z`. Support: pinned connector exact-file inspection.

Observed audit provenance: Non-current blockers RB-001, RB-002, and RB-003 reported incomplete target inventory, missing object identity/conflict tests, and no encoded authoritative/supplemental designation. These observations direct reinspection only.

Discovery:

* Compare every touched locus and PF04 §2.0.6, PF12 §§4 and 8.2, and PF14 §§4–5 against the planning baseline.  
* Accept only expected execution-ref changes; there are no predecessor PRs for PR-01.  
* Re-enumerate current D1 target and schema bindings before editing.  
* Stop with a concise drift report if the owning contract, gate-family authority, schema set declaration, or release-manifest metadata materially differs.

Implementation requirements:

* Extend the gate’s machine-readable target bindings so each current D1 target has an exact path, validator or schema binding, and set-field identity rules where applicable.  
* Cover the existing 13 generated target paths, the PF12-owned manifest and catalog JSON surfaces, and the current gates/channels schemas without importing later-phase evidence families.  
* Encode the complete sorted inventory in the existing structured gate record and fail if a declared target is missing, unbound, omitted, non-schema-valid, or noncanonical.  
* Use schema-declared `uniqueItems` plus PF12 identity bindings; never infer set semantics from list appearance.  
* Add the PF12-required schema IDs to gates and channels schemas and declare `centers` uniqueness without changing its allowed values.  
* Preserve ordered arrays. Normalize only object key order and declared set-array order.  
* Normalize the four PF12-recorded noncanonical catalog files. Reconcile `catalog/manifest.json` to PF12 §5.1 Frozen-input completeness by preserving every legitimate current entry and adding the required existing inputs `catalog/channels_v1.json`, `catalog/gates_v1.json`, `catalog/narratives/keys.json`, `catalog/narratives/manifest.json`, `catalog/narratives/palettes.json`, `catalog/narratives/suppression_map.json`, and `catalog/narratives/templates.json`. Run `scripts/cut_release_manifest.py` with `version=1.0.0` and `built_at_utc=2025-12-26T00:00:00Z`, regenerate the PF12 §6.4 release-identity surfaces through `scripts/release_id_recompute.py` in its required `HDE_ISOLATED_RELEASE_BUILD=1` isolated release-build mode, and require `python ci/checks/check_release_identity.sh` to pass against the final committed bytes. Do not change release metadata.  
* Refresh both still-produced canonical-gate families in one change. The authoritative family remains `audit/gates/json_gate/canonical/`; supplemental output cannot replace it.  
* Expand the existing arrays-as-sets producer and tests to cover scalar identity, object identity, byte-identical duplicates, conflicting identities, ASCII ordering, check-mode drift, omitted targets, and deterministic two-run output.  
* Promote the arrays report only after the check exists; bind its required proof companion and evidence-ledger entries through the existing canonical updater.  
* Do not edit PF documents, public contracts, Human Design meanings, or historical artifacts.

Concrete anchors:

* Observed repo reality: tools/evidence/run\_canonical\_json\_gate.py  
* Observed repo reality: tools/evidence/generate\_arrays\_as\_sets\_report.py  
* Observed repo reality: engine/mech/helpers.py  
* Observed repo reality: schemas/gates\_v1.schema.json  
* Observed repo reality: schemas/channels\_v1.schema.json  
* Observed repo reality: catalog/gates\_v1.json  
* Observed repo reality: catalog/channels\_v1.json  
* Observed repo reality: catalog/magic10\_caps.json  
* Observed repo reality: catalog/magic10\_seeds.json  
* Observed repo reality: catalog/manifest.json  
* Observed repo reality: scripts/cut\_release\_manifest.py  
* Observed repo reality: scripts/release\_id\_recompute.py  
* Observed repo reality: ci/checks/check\_release\_identity.sh  
* Observed repo reality: artifacts/math/freeze\_pack\_manifest.json  
* Observed repo reality: artifacts/math/release\_id\_recompute.log  
* Observed repo reality: artifacts/math/release\_id.txt  
* Observed repo reality: artifacts/math/checksums\_audit.log  
* Observed repo reality: artifacts/math/manifest\_snapshot.json  
* Observed repo reality: artifacts/proofs/env\_pins.txt  
* Observed repo reality: tests/compare/test\_arrays\_as\_sets.py  
* Observed repo reality: tests/evidence/test\_canonical\_json\_gate\_check\_outputs.py  
* Planned output: artifacts/canonical/arrays\_as\_sets\_report.log.path\_proof.txt

Evidence outputs:

* PR implementation evidence produced by tools/evidence/run\_canonical\_json\_gate.py:  
    
  * Observed repo reality: audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson  
  * Observed repo reality: audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson  
  * Observed repo reality: audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json  
  * Observed repo reality: audit/gates/canonical\_json/json\_canonical\_check.log  
  * Observed repo reality: audit/gates/canonical\_json/json\_canon\_compare.log  
  * Observed repo reality: audit/gates/canonical\_json/canonical\_json.gate.json


* PR implementation evidence produced by tools/evidence/generate\_arrays\_as\_sets\_report.py:  
    
  * Observed repo reality: artifacts/canonical/arrays\_as\_sets\_report.log


* PR release-identity evidence regenerated through `scripts/release_id_recompute.py` in isolated release-build mode: `artifacts/math/freeze_pack_manifest.json`; `artifacts/math/release_id_recompute.log`; `artifacts/math/release_id.txt`; `artifacts/math/checksums_audit.log`; `artifacts/math/manifest_snapshot.json`; `artifacts/proofs/env_pins.txt`; and their required existing family-owned companions.  
    
* Existing or planned sibling proof companions and ledger bindings must match final bytes. Their presence does not establish QA PASS, token satisfaction, acceptance, or closeout. Same-PR Doc-Delta requirement: PR-01 must create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md`; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Acceptance tokens: CANONICAL\_JSON\_GATE\_UPDATED\_OK; CANONICAL\_JSON\_GATE\_PASSED\_OK; JSON\_CANONICAL\_CHECK\_OK. These are intended implementation tokens only and are not claimed by this plan or PR.

Rails posture: Closed rails: SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC. No external I/O.

Basic QA check: Planned command: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/compare/test_arrays_as_sets.py tests/evidence/test_canonical_json_gate_check_outputs.py && SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python ci/checks/check_release_identity.sh`

Pass condition: The bounded suites prove complete target enumeration, canonical bytes, authoritative/supplemental coherence, deterministic report generation, duplicate collapse, conflict refusal, ASCII ordering, and check-mode failure on drift.

Fail condition: Any omission, missing validator binding, schema violation, noncanonical byte, ordered-array mutation, divergent gate family, nondeterminism, or false-success path fails the check.

PO inputs: None

Codex Prompt:

```
Implement PR-01 only: consolidate canonical governed JSON and schema-declared set arrays in amthorn78/glow-hdengine-v2.

Repository baseline:
- Default branch: main
- Planning baseline: c20c788baa46312f2d88691b7264caec29d313a0

Before editing, compare the execution ref with the baseline for every listed locus and for these controlling units:
- PF09.1-Canon-HDE-Build-Checklist-Calcination: HDE-CALC002.2 and HDE-CALC002.3
- PF04-Canon-HDE-Governance §2.0.6

* PF10-HDE-Build-Notes Addendum 2.4
- PF12-Canon-HDE-Schemas-and-Artifacts §§4, 5, and 8.2
- PF14-Canon-HDE-Mechanics-Guide §§4–5

There are no predecessor PR diffs to account for. If any material scope, authority, schema, target-family, or manifest-metadata drift exists, stop before editing and return a concise drift report with exact paths and changed contracts. Do not reinterpret canon.

PF09 completion role: complete HDE-CALC002.2 and HDE-CALC002.3 in this epic without editing PF09 or claiming its status changed.

Exact touched loci:
- Observed repo reality: tools/evidence/run_canonical_json_gate.py
- Observed repo reality: tools/evidence/generate_arrays_as_sets_report.py
- Observed repo reality: engine/mech/helpers.py
- Observed repo reality: schemas/gates_v1.schema.json
- Observed repo reality: schemas/channels_v1.schema.json
- Observed repo reality: catalog/gates_v1.json
- Observed repo reality: catalog/channels_v1.json
- Observed repo reality: catalog/magic10_caps.json
- Observed repo reality: catalog/magic10_seeds.json
* Observed repo reality: catalog/manifest.json
* Observed repo reality: scripts/cut_release_manifest.py
* Observed repo reality: scripts/release_id_recompute.py
* Observed repo reality: ci/checks/check_release_identity.sh
* Observed repo reality: artifacts/math/freeze_pack_manifest.json
* Observed repo reality: artifacts/math/release_id_recompute.log
* Observed repo reality: artifacts/math/release_id.txt
* Observed repo reality: artifacts/math/checksums_audit.log
* Observed repo reality: artifacts/math/manifest_snapshot.json
* Observed repo reality: artifacts/proofs/env_pins.txt
* Observed repo reality: tests/compare/test_arrays_as_sets.py
- Observed repo reality: tests/evidence/test_canonical_json_gate_check_outputs.py
- Existing governed gate outputs under audit/gates/json_gate/canonical/ and audit/gates/canonical_json/
- Observed repo reality: artifacts/canonical/arrays_as_sets_report.log
- Planned output: artifacts/canonical/arrays_as_sets_report.log.path_proof.txt
- Existing Human Index, sentinel, Machine Mirror, orientation, and directly affected proof companions

Implement these requirements:
1. Governed JSON must be UTF-8 without BOM, recursively ASCII-key-sorted, compact, schema-valid, and terminated by exactly one LF.
2. Preserve ordered arrays. Apply set handling only where the owning schema or PF12 binding declares it and supplies an identity.
3. Collapse byte-identical duplicate members. Reject different members sharing one identity and identify the first divergent field. Sort remaining identities by strict ASCII without locale or value transformation.
4. Replace omission-prone coverage with deterministic machine-readable target bindings. Cover the existing 13 generated targets and the current PF12-owned manifest, catalog, and topology-schema surfaces in D1 scope. Every target requires an exact validator or schema binding. Missing, omitted, unbound, schema-invalid, or noncanonical targets must fail.
5. Record the sorted target and set-rule inventory in the existing structured gate record. Do not create another gate family.
6. Keep audit/gates/json_gate/canonical/ authoritative. Refresh every still-produced supplemental output under audit/gates/canonical_json/ in the same change.
7. Add the PF12-required schema IDs and declare Channel centers uniqueness without changing the allowed values.
8. Normalize the four current catalog files recorded as noncanonical. Preserve all Human Design values and ordered-array meaning.
9. Reconcile catalog/manifest.json to PF12 §5.1 Frozen-input completeness: preserve every legitimate current entry and add catalog/channels_v1.json, catalog/gates_v1.json, catalog/narratives/keys.json, catalog/narratives/manifest.json, catalog/narratives/palettes.json, catalog/narratives/suppression_map.json, and catalog/narratives/templates.json. Run scripts/cut_release_manifest.py with --version 1.0.0 and --built-at-utc 2025-12-26T00:00:00Z. In an isolated release-build workspace, run SAFE_MODE=1 ALLOW_NETWORK=0 LANG=C LC_ALL=C TZ=UTC HDE_ISOLATED_RELEASE_BUILD=1 python scripts/release_id_recompute.py, carry the generated PF12 §6.4 release-identity surfaces into the PR, and require SAFE_MODE=1 ALLOW_NETWORK=0 LANG=C LC_ALL=C TZ=UTC python ci/checks/check_release_identity.sh to pass against the final committed bytes. Do not change version or built_at_utc. Stop if execution-ref metadata or PF12's required frozen-input set differs from the planning baseline.
10. Make the arrays report deterministic and checkable. Add positive and fail-closed coverage for scalar identity, object identity, identical duplicates, conflicting identities, ASCII order, omissions, family disappearance, and two-run identity.
11. Bind changed governed outputs, their required proof companions, and ledger records to final bytes using current canonical evidence tooling. Do not hand-edit generated evidence.
12. Do not change public routes, payload contracts, Human Design calculations or meanings, PF documents, historical evidence, OPS state, or later-phase domain scope.
Same-PR Doc-Delta requirement: Create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md` in PR-01. Preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Basic QA:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/compare/test_arrays_as_sets.py tests/evidence/test_canonical_json_gate_check_outputs.py && SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python ci/checks/check_release_identity.sh

Pass means the bounded tests establish complete inventory, canonical bytes, family coherence, declared set semantics, deterministic output, and decisive failure behavior. Fail on any omission, ambiguity, false success, or semantic change.

The relevant intended token names are CANONICAL_JSON_GATE_UPDATED_OK, CANONICAL_JSON_GATE_PASSED_OK, and JSON_CANONICAL_CHECK_OK. Do not claim them.

Remote-update discipline: Keep iterative commits, targeted tests, and debugging local. Before each ordinary update to the open pull request head, collect the complete current CI and review feedback set, include all safely combinable known fixes in one coherent correction batch, run the smallest relevant checks and complete applicable local validation, and inspect the final diff and repository status. Do not update the pull request head with an incomplete or knowingly superseded intermediate state. Treat remote-only validation as a bounded exception and record why it could not be established non-remotely. If this assignment has already made five CI-triggering branch updates, pause before a sixth and report the update count, causes, current CI and review state, unresolved work, validation performed, and consolidation plan; do not update the branch again without explicit authorization. Require every applicable check on the final exact head. In the implementation report, state the number of CI-triggering branch updates and identify any remote-only validation or urgent-safety exception used.

Do not execute OPS, Live QA, external calls, acceptance, closeout, or unrelated work. Return a concise change and proof summary without private chain-of-thought.
```

## PR-02 \- Make evidence-ledger updates atomic and convergent

Title: Make evidence-ledger updates atomic and convergent

Intent: Establish one final-byte write transaction for the Human Index, sentinel, Machine Mirror, proofs, and orientation, followed only by non-writing validation.

Implementation Guide source items: D2

Approved requirement:

* Keep the canonical evidence updater as sole writer for the Human Index, sentinel, Machine Mirror, and required proof bindings.  
* Converge in one authorized write invocation and validate final bytes without repair.  
* Generate orientation only from the final evidence skeleton, then run non-writing updater and orientation checks.  
* Prove Machine Mirror self-record correctness and atomic add/remove behavior.  
* Preserve historical records and avoid later-phase evidence expansion.  
* Classify each D2 CI control under PF10 Addendum 2.3; retain required PR CI only when continuing product or delivery risk justifies it.  

* Apply PF10 Addendum 2.5 to each D2 CI control: record its contribution to the execution-ref cost shape, avoid duplicate equivalent full-suite eligibility and avoidable superseded or irrelevant hosted work, preserve required-check continuity and truthful failure, justify repeated setup and validation, and carry the resulting before-and-after control shape into PR-04’s complete workflow validation matrix.
* Use the current Python invocation for `ci/checks/check_mirror_schema.sh` and remove obsolete operand assumptions.

Caveats applied: None

PF09 document(s), task IDs, and proof excerpts:

PF09.1-Canon-HDE-Build-Checklist-Calcination, HDE-CALC003:

> ## Task HDE-CALC003 — Repository & Tooling Skeleton

> **Task name/label:** Repository & Tooling Skeleton  
>   
> **Task status:** **Partial**

PF09 subtask IDs and proof excerpts:

HDE-CALC003.10:

> **Subtask name/label:** Indexing & parity CI gates  
>   
> **Subtask description:** Update the Human Evidence Index and Machine Mirror in the same PR (records-only; with path-proofs); ensure governed locations only (`artifacts/**`, `audit/**`, `docs/evidence/**`); reject ungoverned `codex/out/**`; and fail CI if Index/Mirror miss entries, violate canonical JSONL, have unknown keys, missing path-proofs, wrong field order, or are unsorted.  
>   
> **Subtask status:** **Partial**

HDE-CALC003.11:

> **Subtask name/label:** Evidence Index/Mirror touch discipline  
>   
> **Subtask description:** For any change that touches the Human Index, its sentinel, or the Machine Mirror, enforce a standard tool chain under closed rails in the same PR so that the Index, Mirror, and path-proofs stay in lockstep:

PF09 completion role: Completes PF09 item in this epic

PF14 or owning-canon pointers and proof excerpts:

PF14-Canon-HDE-Mechanics-Guide §1.3.1:

> tools/evidence/update\_evidence\_index.py is the single writer for:  
> 

> * docs/evidence/INDEX.json (Human Index, titles/paths only),  
> * docs/evidence/INDEX.sha256 (hash sentinel),  
> * artifacts/evidence\_index.jsonl (Machine Mirror), and  
> * governed \*.path\_proof.txt transcripts for artifacts listed in this guide.

>   
> Updater fixed-point convergence (normative). `tools/evidence/update_evidence_index.py` MUST converge to a deterministic fixed point from a clean checkout in CI-like order. The updater MUST centralize Human Index, hash sentinel, Machine Mirror, and governed path-proof writes inside one bounded convergence loop and MUST NOT require a second manual rerun to settle stale in-memory or pre-write proof metadata.  
>   
> Check-mode equivalence (normative). `python tools/evidence/update_evidence_index.py --check` MUST validate the same ordered write model used by normal generation. A `--check` failure caused by updater self-instability, rather than by true artifact drift, is a mechanics defect.

PF04-Canon-HDE-Governance §2.0.6:

> * **CI\_CHECK\_MIRROR\_SCHEMA\_OK** — Mirror records pass schema/role/field-order checks (unknown-key rejection). The retained validator path is `ci/checks/check_mirror_schema.sh`; the file is Python, and the `.sh` suffix is legacy path identity, not an interpreter declaration. The validator reads fixed input `artifacts/evidence_index.jsonl`, accepts no caller-selected mirror path, and MUST be run from the repository root.  
  >   
> * Supported invocations are `python ci/checks/check_mirror_schema.sh` and direct execution as `ci/checks/check_mirror_schema.sh` when Git executable mode and shebang handling are guaranteed.

PF10-HDE-Build-Notes, Addendum 2.3:

> 1. **Required PR CI** provides fast, reliable, deterministic feedback about whether a proposed change preserves current product and delivery integrity. It may block merge when the protected risk and failure consequence justify that power.  
> 2. **Release or security automation** builds, packages, signs, attests, scans, or validates an actual release or security boundary. It may gate release or deployment when the output is consumed by that process or satisfies a real security, legal, contractual, or compliance obligation.  
> 3. **QA or audit automation** performs deeper validation, captures governed results, or supports a bounded review. It may be automated without becoming an ordinary merge gate.  
> 4. **Epic closeout automation** prepares or validates administrative closeout material. It may reduce manual work, but it must remain outside required PR CI unless a specific part independently qualifies for another lane.

PF07 facts, prerequisites, or reconciliation posture: PF07-Canon-Glow-Infrastructure is not applicable. Repository-setting state is neither required nor claimed.

Dependencies: PR-01

Observed repo reality:

* Observed repo reality: tools/evidence/update\_evidence\_index.py contains `_WriteTransaction`, `_render_mirror`, a deterministic self-record calculation, and a bounded fixed-point loop. Support: pinned connector exact-file inspection.  
* Observed repo reality: .github/workflows/ci.yml contains write sequences that invoke updater, orientation, and updater again before checks. Support: pinned connector exact-file inspection.  
* Observed repo reality: tools/evidence/orientation\_demo.py currently writes its report separately.  
* Observed repo reality: ci/checks/check\_mirror\_schema.sh is Python and reads the fixed Machine Mirror path.  
* Observed repo reality: tests/evidence/test\_machine\_mirror\_self\_proof.py and tests/evidence/test\_orientation\_demo.py exist.

Observed audit provenance: Non-current blocker RB-004 reported unresolved complete writer ownership and insufficient final-byte, self-record, and add/remove atomicity proof. Revalidate at the execution ref.

Discovery:

* Compare PR-02 loci and PF04, PF10, PF12 §8.3, and PF14 §1.3 against the planning baseline.  
* Account only for the approved PR-01 diff.  
* Enumerate all active updater, orientation, mirror-schema, evidence-path, hash, and LF invocations.  
* Apply all ten PF10 Addendum 2.3 questions to each D2 control.  
* Stop without partial edits if a safe ownership or lane disposition cannot be established.

Implementation requirements:

* Make `tools/evidence/update_evidence_index.py` the single public write entrypoint for the complete evidence skeleton.  
* Coordinate orientation rendering within the updater’s bounded transaction or through a pure renderer so there is no post-orientation repair write.  
* Preserve `tools/evidence/orientation_demo.py --check` as a non-writing validator; any compatibility write mode must delegate to the canonical updater and cannot directly mutate ledger companions.  
* Compute the Human Index, sentinel, Machine Mirror, complete self-record, orientation, and proof bindings from one final model before atomic publication.  
* Roll back the entire write set on any convergence, validation, add/remove, proof, or self-record failure.  
* After authorized write completion, the sequence must be updater `--check`, orientation `--check`, mirror-schema check, evidence-path check, hash check, and final-LF check, all non-writing.  
* Remove every active updater-write/orientation-write/updater-write sequence.  
* Use `python ci/checks/check_mirror_schema.sh` or direct execution without a mirror operand. Reject unsupported operand assumptions in active callers and focused tests.  
* Prove atomic addition and removal across the Human Index, sentinel, Mirror, Mirror checksum, affected path proofs, and orientation.  
* Preserve frozen historical bytes and current historical roles.  
* Classify D2 hosted controls. Retain them as required PR CI only when their continuing-risk answers satisfy PF10; otherwise narrow, remove, or isolate them without creating a new evidence family.

Concrete anchors:

* Observed repo reality: tools/evidence/update\_evidence\_index.py  
* Observed repo reality: tools/evidence/orientation\_demo.py  
* Observed repo reality: ci/checks/check\_mirror\_schema.sh  
* Observed repo reality: .github/workflows/ci.yml  
* Observed repo reality: tests/evidence/test\_machine\_mirror\_self\_proof.py  
* Observed repo reality: tests/evidence/test\_orientation\_demo.py  
* Observed repo reality: docs/evidence/INDEX.json  
* Observed repo reality: docs/evidence/INDEX.sha256  
* Observed repo reality: artifacts/evidence\_index.jsonl  
* Observed repo reality: artifacts/evidence\_index.jsonl.sha256  
* Observed repo reality: audit/gates/topology/orientation\_demo.txt

Evidence outputs:

* PR implementation evidence produced by the canonical updater:  
    
  * Observed repo reality: docs/evidence/INDEX.json  
  * Observed repo reality: docs/evidence/INDEX.json.path\_proof.txt  
  * Observed repo reality: docs/evidence/INDEX.sha256  
  * Observed repo reality: docs/evidence/INDEX.sha256.path\_proof.txt  
  * Observed repo reality: artifacts/evidence\_index.jsonl  
  * Observed repo reality: artifacts/evidence\_index.jsonl.path\_proof.txt  
  * Observed repo reality: artifacts/evidence\_index.jsonl.sha256  
  * Observed repo reality: artifacts/evidence\_index.jsonl.sha256.path\_proof.txt  
  * Observed repo reality: audit/gates/topology/orientation\_demo.txt  
  * Observed repo reality: audit/gates/topology/orientation\_demo.txt.path\_proof.txt


* These outputs demonstrate implementation mechanics only. Same-PR Doc-Delta requirement: PR-02 must create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md`; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Acceptance tokens: EVIDENCE\_INDEX\_UPDATED\_OK; EVIDENCE\_INDEX\_MIRROR\_OK; EVIDENCE\_INDEX\_HASH\_OK; MACHINE\_MIRROR\_UPDATED\_OK; EVIDENCE\_PATHS\_VALIDATED\_OK; EVIDENCE\_PATH\_PROOFS\_OK; CI\_CHECK\_MIRROR\_SCHEMA\_OK; CI\_CHECK\_FINAL\_LF\_OK. No token is claimed.

Rails posture: Closed rails and non-writing hosted validation. No network, external service, runtime, database, or OPS behavior.

Basic QA check: Planned command: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/evidence/test_machine_mirror_self_proof.py tests/evidence/test_orientation_demo.py`

Pass condition: The bounded suites prove one transaction, complete self-record bytes, atomic additions/removals, deterministic convergence, orientation against final state, rollback on failure, and read-only check equivalence.

Fail condition: Partial writes, a required second write, stale self-record or proof, historical-byte refresh, unsupported mirror invocation, nondeterminism, or a writing check mode fails PR-02.

PO inputs: None

Codex Prompt:

```
Implement PR-02 only: make the evidence skeleton atomic, convergent, and checkable without repair in amthorn78/glow-hdengine-v2.

Repository baseline:
- Default branch: main
- Planning baseline: c20c788baa46312f2d88691b7264caec29d313a0
- Approved predecessor: PR-01

Before editing, compare the execution ref with the baseline for the exact loci below and these current canon units:
- PF09.1-Canon-HDE-Build-Checklist-Calcination: HDE-CALC003.10 and HDE-CALC003.11
- PF04-Canon-HDE-Governance §2.0.6
- PF05-Canon-HDE-CLI-API-Vendor-Ref §0.2

* PF10-HDE-Build-Notes Addenda 2.3, 2.4, and 2.5
- PF12-Canon-HDE-Schemas-and-Artifacts §8.3
- PF14-Canon-HDE-Mechanics-Guide §§1.3, 1.3.1, and 1.3.2

Account only for the approved PR-01 diff. Stop before editing and return a concise path-and-contract drift report if any other material change affects ownership, output bytes, caller inventory, or CI disposition.

PF09 completion role: complete HDE-CALC003.10 and HDE-CALC003.11 without editing PF09 or claiming its status changed.

Exact touched loci:
- Observed repo reality: tools/evidence/update_evidence_index.py
- Observed repo reality: tools/evidence/orientation_demo.py
- Observed repo reality: ci/checks/check_mirror_schema.sh
- Observed repo reality: .github/workflows/ci.yml
- Observed repo reality: tests/evidence/test_machine_mirror_self_proof.py
- Observed repo reality: tests/evidence/test_orientation_demo.py
- Observed repo reality: docs/evidence/INDEX.json
- Observed repo reality: docs/evidence/INDEX.sha256
- Observed repo reality: artifacts/evidence_index.jsonl
- Observed repo reality: artifacts/evidence_index.jsonl.sha256
- Observed repo reality: audit/gates/topology/orientation_demo.txt
- Exact directly affected sibling proof companions

First enumerate every active call to the updater, orientation tool, mirror-schema checker, evidence-path validator, index-hash checker, and final-LF checker. For every D2 hosted control, answer all ten PF10 Addendum 2.3 questions and assign exactly one lane. If any current control cannot be safely classified, stop before partial edits.

Implement these requirements:
1. tools/evidence/update_evidence_index.py is the single public writer for the Human Index, sentinel, Machine Mirror, Mirror checksum, and required proof bindings.
2. Coordinate orientation from the final evidence model in the same bounded transaction. No active sequence may run updater write, orientation write, and updater write again.
3. Compute final Index, sentinel, Mirror, complete Mirror self-record, orientation bytes, and affected proof bindings before atomic publication. Roll back all additions, removals, file updates, and directories on failure.
4. Preserve tools/evidence/orientation_demo.py --check as read-only. Any retained compatibility write entrypoint must delegate to the canonical updater and cannot repair companions independently.
5. A completed authorized write must be immediately stable under updater --check, orientation --check, mirror-schema validation, evidence-path validation, hash validation, and final-LF validation, with no byte change.
6. The Mirror self-record must bind the complete final Mirror bytes according to current PF04/PF12 semantics.
7. Add focused tests for atomic add, atomic remove, rollback, final-byte self-record, one-invocation convergence, orientation finality, and check-mode nonmutation.
8. The retained mirror-schema checker is Python. Active callers must use python ci/checks/check_mirror_schema.sh or direct execution, from repository root, with no mirror operand. Do not invoke it through bash or sh.
9. Preserve frozen historical artifacts and roles. Do not refresh history as current proof or import later-phase evidence work.
10. Required PR CI may retain only independently justified continuing-risk controls. Narrow, remove, or isolate other D2 controls according to PF10 without adding a replacement administrative gate.
Same-PR Doc-Delta requirement: Create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md` in PR-02. Preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Basic QA:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/evidence/test_machine_mirror_self_proof.py tests/evidence/test_orientation_demo.py

Pass requires atomic convergence, final-byte self-record correctness, final orientation, complete add/remove parity, rollback, and non-writing checks. Any repair rerun, partial state, stale proof, historical churn, or unsupported invocation fails.

The relevant intended token names are EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_INDEX_HASH_OK, MACHINE_MIRROR_UPDATED_OK, EVIDENCE_PATHS_VALIDATED_OK, EVIDENCE_PATH_PROOFS_OK, CI_CHECK_MIRROR_SCHEMA_OK, and CI_CHECK_FINAL_LF_OK. Do not claim them.

CI-budget discipline for D2: Apply PF10-HDE-Build-Notes Addendum 2.5 to every D2 CI-control change. Record each control’s execution-ref event, job, step, dependency, repeated setup, artifact transfer, and required-check conclusion; do not create duplicate equivalent full-suite eligibility, avoidable superseded work, unrelated heavy execution, missing required-check continuity, unjustified repeated setup, or false-green behavior; and return the D2 before-and-after control shape for PR-04’s complete workflow validation matrix.

Remote-update discipline: Keep iterative commits, targeted tests, and debugging local. Before each ordinary update to the open pull request head, collect the complete current CI and review feedback set, include all safely combinable known fixes in one coherent correction batch, run the smallest relevant checks and complete applicable local validation, and inspect the final diff and repository status. Do not update the pull request head with an incomplete or knowingly superseded intermediate state. Treat remote-only validation as a bounded exception and record why it could not be established non-remotely. If this assignment has already made five CI-triggering branch updates, pause before a sixth and report the update count, causes, current CI and review state, unresolved work, validation performed, and consolidation plan; do not update the branch again without explicit authorization. Require every applicable check on the final exact head. In the implementation report, state the number of CI-triggering branch updates and identify any remote-only validation or urgent-safety exception used.

Do not execute OPS, Live QA, external calls, acceptance, closeout, or unrelated work. Return the D2 control classification, concise change summary, and check proof without private chain-of-thought.
```

## PR-03 \- Harden the reusable current-state QA harness

Title: Harden the reusable current-state QA harness

Intent: Replace run-oriented, timestamp-sensitive, loosely classified QA mechanics with stable epic/check identities and deterministic viability behavior.

Implementation Guide source items: D3

Approved requirement:

* Keep active pytest invocation on the active Python interpreter.  
* Remove `run_id`, timestamped correctness paths, per-run nesting, and operator-selected QA roots from current-state correctness.  
* Enforce exactly PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, or PARKED.  
* Treat missing dependencies and required inputs as tooling or prerequisite failures.  
* Resolve token identity from acceptance-map `tokens[].name` and validate it against current Governance.  
* Return deterministic TOOLING\_BLOCKED instead of uncaught missing-token-material exceptions.  
* Prevent invalid or broken references from producing PASS.  
* Require successful viability to resolve required references and load/evaluate the map.  
* Fail on empty, absent, or partial required outputs.  
* Preserve historical records and avoid Live QA execution.

Caveats applied: None

PF09 document(s), task IDs, and proof excerpts:

PF09.1-Canon-HDE-Build-Checklist-Calcination, HDE-CALC003:

> ## Task HDE-CALC003 — Repository & Tooling Skeleton

> **Task name/label:** Repository & Tooling Skeleton  
>   
> **Task status:** **Partial**

PF09 subtask IDs and proof excerpts:

HDE-CALC003.13:

> **Subtask status:** **Partial** **Owner:** Unassigned **Epic or card:** HDE-EPIC019, HDE-EPIC025  
>   
> **Intent:** Ensure all QA plans and CI jobs invoke pytest using `python -m pytest` (not `pytest`) to guarantee module resolution and consistent plugin discovery.

HDE-CALC003.14:

> **Subtask name / label:** QA harness discipline (tooling vs behavior, commands, emptiness)  
>   
> **Subtask status:** **Partial**  
>   
> **Epic provenance:** EPIC019 (live QA harness baseline)

HDE-CALC003.15:

> **Subtask name / label:** acceptance map & QA harness viability check  
>   
> **Subtask description:** Verify that a given epic has a viable acceptance map and that the QA harness can load it.  
>   
> **Subtask status:** **Partial**

PF09 completion role: Completes PF09 item in this epic

PF14 or owning-canon pointers and proof excerpts:

PF14-Canon-HDE-Mechanics-Guide §1.6.3:

> Within an epic, check IDs are the stable handle. There is no additional “run identity” dimension in mechanics.  
>   
> A per-epic “step logs manifest” (see §1.6.3) MAY be emitted to map check IDs to the current canonical log filenames. This is a convenience index for reviewers; it is not required for correctness and MUST be current-state only, not per-run history.  
>   
> run\_id is prohibited: Live QA plans and artifacts MUST NOT introduce or require run\_id (or RUN\_ID) as an operator input, step-log header field, manifest field, or correctness key.  
> 

> * Enforce status vocabulary as gating (names-only): PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED.  
> * Prohibit ad-hoc statuses for core execution state; if status is outside this set, normalization MAY set it only when the transcript unambiguously indicates the correct status (for example, contains a single definitive PASS: line and no FAIL\_ lines). Otherwise status remains Unclear and the step is not acceptable.

>   
> Fail closed on missing outputs: If the harness completes without producing at least one non-empty per-check primary.log under audit/qa/hde-epic/checks/ or without updating the per-epic step logs manifest, it MUST exit non-zero and record the reason as a tooling/harness failure.  
>   
> Be reusable across epics: Epic-specific harness entrypoints may exist as thin wrappers for convenience, but they MUST delegate to the generic harness entrypoint and must not re-implement logging, QA\_ROOT layout, or manifest updates in bespoke per-epic code.  
>   
> CI self-test (normative): The repo MUST include a CI test that executes the epic QA harness entrypoint under closed rails and asserts, at minimum:

PF19-Canon-Glow-QA-Guide §4.4.5:

> Status vocabulary (normative): status MUST be one of PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED. Non-conforming status values MUST be normalized (or the step is not audit-usable).  
>   
> Each per-check primary log MUST begin with a machine-readable header block on the first line, followed by the human-readable body.  
>   
> Routing (normative): Live QA runbook template structure, the minimum step-log header schema, and the status vocabulary are owned by PF27 — Plan Templates. This guide does not define alternate header schemas.

PF19-Canon-Glow-QA-Guide §4.4.5:

> * Missing declared prerequisites or missing required inputs/artifacts implies TOOLING\_BLOCKED (not FAIL\_BEHAVIOR).  
> * Tool/harness failure that prevents running or evaluating the check implies FAIL\_TOOLING.  
> * The check ran, but behavior contradicted the expected result implies FAIL\_BEHAVIOR.

PF07 facts, prerequisites, or reconciliation posture: PF07-Canon-Glow-Infrastructure is not applicable. The implementation uses repository-local files and temporary test roots only.

Dependencies: PR-02

Observed repo reality:

* Observed repo reality: tools/qa/qa\_harness.py accepts caller-selected `qa_root`, acceptance-map, and matrix paths; writes run directories; records `run_id`; and uses wall-clock timestamps.  
* Observed repo reality: `CheckResult` accepts arbitrary status strings and `summarize_checks` recognizes only strings beginning with `FAIL`.  
* Observed repo reality: missing viability inputs can raise directly.  
* Observed repo reality: tools/qa/epic021\_qa.py derives a run ID from an environment value, git SHA, or fallback and emits placeholder-success steps.  
* Observed repo reality: .github/workflows/ci.yml sets `EPIC021_QA_RUN_ID`.  
* Observed repo reality: tools/qa/generate\_epic027\_close\_pack.py and tools/qa/generate\_epic029\_close\_pack.py pass `RUN_ID` into the generic viability helper.  
* Observed repo reality: tests/qa/test\_epic021\_harness\_entrypoint.py asserts run-directory behavior and writes beneath the source-tree QA root.

Observed audit provenance: Non-current blocker RB-005 reported run IDs, timestamps, caller-selected roots, arbitrary statuses, unresolved references, and missing deterministic tooling-blocked behavior.

Discovery:

* Compare exact harness, wrapper, self-test, and CI loci with the baseline and approved PR-01/PR-02 diffs.  
* Inspect all active imports and calls of `HarnessConfig`, `CheckResult`, manifest/log writers, and viability functions.  
* Preserve archived QA and audit bytes.  
* Stop if an active caller requires a public, OPS, or Live-QA behavior change outside D3.

Implementation requirements:

* Derive the canonical QA root and acceptance-map path from validated epic identity; do not accept an operator-selected correctness root.  
* Store current results only under stable epic and check identities. Remove run IDs, per-run paths, timestamp fields, git-derived identity, and placeholder-success checks.  
* Make status a closed enum with exactly the five current values. Reject or deterministically classify every other value.  
* Invoke pytest through the active Python interpreter; active wrappers must use `sys.executable -m pytest` or an equivalent in-process invocation that cannot select a different interpreter.  
* Resolve acceptance tokens only from `tokens[].name`.  
* Resolve the current Governance token roster from the single current repository-resident PF04 source and fail TOOLING\_BLOCKED when that source or required token material cannot be uniquely loaded.  
* Resolve evidence references deterministically. Accept an exact repository-relative path or one unambiguous legacy title containing a single repository-relative path. Multiple, malformed, traversal, absent, empty, or partial references cannot PASS.  
* Distinguish TOOLING\_BLOCKED prerequisites, FAIL\_TOOLING harness failures, and FAIL\_BEHAVIOR evaluated contradictions.  
* A successful viability result requires a parseable map, valid epic identity, registered token names, resolvable non-empty references, and a non-empty current-state primary log plus manifest entry.  
* Convert active epic-specific callers to thin wrappers over the generic implementation.  
* Rewrite self-tests to use temporary repository fixtures and leave the source tree unchanged.  
* Preserve historical evidence and do not regenerate it.  
* Do not create HDE-EPIC039 Live QA evidence, execute Live QA, or claim QA PASS. The PF06-required same-PR Doc-Delta pair remains mandatory PR parity evidence and is not a QA verdict.

Concrete anchors:

* Observed repo reality: tools/qa/qa\_harness.py  
* Observed repo reality: tools/qa/epic021\_qa.py  
* Observed repo reality: tools/qa/generate\_epic027\_close\_pack.py  
* Observed repo reality: tools/qa/generate\_epic029\_close\_pack.py  
* Observed repo reality: tests/qa/test\_generic\_qa\_harness.py  
* Observed repo reality: tests/qa/test\_epic021\_harness\_entrypoint.py  
* Observed repo reality: .github/workflows/ci.yml  
* Observed repo reality: tools/evidence/check\_po\_006\_token\_registry\_validity.py  
* Observed repo reality: tools/evidence/check\_epic024\_acceptance\_map\_viability.py

Evidence outputs: PR-03 must create or update the PF06-required same-PR Doc-Delta pair at `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md`; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Acceptance tokens: QA\_HARNESS\_DISCIPLINE\_OK; QA\_HARNESS\_ENTRYPOINT\_SELFTEST\_OK. QA\_BOOTSTRAP\_OK and QA\_LIVE\_QA\_RUN\_OK remain later QA-readiness or closeout tokens and are not PR claims.

Rails posture: Closed, repository-local, current-state tooling. Basic tests use temporary directories and perform no external I/O.

Basic QA check: Planned command: `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/qa/test_generic_qa_harness.py tests/qa/test_epic021_harness_entrypoint.py`

Pass condition: The suites prove stable paths, no run identity, the five statuses, active-interpreter pytest, deterministic prerequisite classification, valid-reference success, broken-reference failure, non-empty outputs, manifest idempotence, and no source-tree writes.

Fail condition: Any run ID, timestamp correctness key, caller-selected QA root, arbitrary status, phantom PASS, uncaught missing input, empty required output, broken reference success, or historical rewrite fails PR-03.

PO inputs: None

Codex Prompt:

```
Implement PR-03 only: harden the reusable current-state QA harness in amthorn78/glow-hdengine-v2.

Repository baseline:
- Default branch: main
- Planning baseline: c20c788baa46312f2d88691b7264caec29d313a0
- Approved predecessors: PR-01 and PR-02

Before editing, compare the execution ref with the baseline for every listed locus and for:
- PF09.1-Canon-HDE-Build-Checklist-Calcination: HDE-CALC003.13, HDE-CALC003.14, and HDE-CALC003.15
- PF04-Canon-HDE-Governance §2.0 acceptance-token roster

* PF10-HDE-Build-Notes Addendum 2.4
- PF14-Canon-HDE-Mechanics-Guide §§1.6.1–1.6.3
- PF19-Canon-Glow-QA-Guide §§2.2.5 and 4.4
- PF27-Canon-Plan-Templates current status semantics

Account only for approved PR-01 and PR-02 diffs. Stop before editing and return an exact drift report if another change alters active caller scope, QA identity, status semantics, or token ownership.

PF09 completion role: complete HDE-CALC003.13, HDE-CALC003.14, and HDE-CALC003.15 without editing PF09 or claiming status movement.

Exact touched loci:
- Observed repo reality: tools/qa/qa_harness.py
- Observed repo reality: tools/qa/epic021_qa.py
- Observed repo reality: tools/qa/generate_epic027_close_pack.py
- Observed repo reality: tools/qa/generate_epic029_close_pack.py
- Observed repo reality: tests/qa/test_generic_qa_harness.py
- Observed repo reality: tests/qa/test_epic021_harness_entrypoint.py
- Observed repo reality: .github/workflows/ci.yml
- Inspect-only context: tools/evidence/check_po_006_token_registry_validity.py and tools/evidence/check_epic024_acceptance_map_viability.py

First enumerate every active import and invocation of HarnessConfig, CheckResult, the generic log/manifest writers, and acceptance-map viability. Historical transcripts and audit artifacts are read-only.

Implement these requirements:
1. Validate the epic identity and derive the canonical epic QA root and acceptance-map path. Do not accept an operator-selected correctness root.
2. Use stable epic and check identities only. Remove run_id, RUN_ID, EPIC021_QA_RUN_ID, git-derived run identity, wall-clock correctness fields, per-run directories, and per-run manifest entries.
3. Use exactly PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, or PARKED. Reject or deterministically classify every other core status.
4. Run pytest through the active Python interpreter. Active wrappers must use sys.executable with -m pytest or an equivalent same-interpreter mechanism; never call a bare pytest wrapper.
5. Token identity comes only from acceptance-map tokens[].name. Resolve the one current repository-resident PF04 Governance source and its §2.0 roster. Missing or ambiguous governance/token material is TOOLING_BLOCKED, not an exception or behavior verdict.
6. Resolve required evidence references before PASS. Accept exact repository-relative paths and one unambiguous legacy title containing a single repository-relative path. Reject traversal, ambiguity, malformed values, absent files, empty files, and partially written JSON. Broken references cannot PASS.
7. Missing declared inputs and prerequisites are TOOLING_BLOCKED. Harness/import/execution failure is FAIL_TOOLING. An evaluated contradiction is FAIL_BEHAVIOR.
8. A successful viability result must prove that the map loads, epic identity matches, token names are registered, required references resolve and are non-empty, and the generic harness writes a non-empty current-state primary log and unique manifest entry.
9. Convert active epic-specific callers to thin wrappers. Do not preserve duplicate logging or manifest logic.
10. Remove placeholder-success steps. Unexecuted work may be PARKED but cannot be PASS.
11. Rewrite entrypoint tests to use temporary repository fixtures and prove the source tree remains unchanged.
12. Preserve every historical QA artifact byte. Do not create HDE-EPIC039 Live QA evidence, execute Live QA, or claim QA PASS. Create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md` in PR-03; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.

Basic QA:
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python -m pytest -q tests/qa/test_generic_qa_harness.py tests/qa/test_epic021_harness_entrypoint.py

Pass requires stable current-state paths, closed statuses, same-interpreter pytest, decisive prerequisite and behavior classifications, valid-reference success, broken-reference refusal, non-empty outputs, idempotent manifest replacement by check ID, and zero source-tree test writes.

The relevant intended token names are QA_HARNESS_DISCIPLINE_OK and QA_HARNESS_ENTRYPOINT_SELFTEST_OK. Do not claim them. QA_BOOTSTRAP_OK and QA_LIVE_QA_RUN_OK are outside this PR’s claim posture.

Remote-update discipline: Keep iterative commits, targeted tests, and debugging local. Before each ordinary update to the open pull request head, collect the complete current CI and review feedback set, include all safely combinable known fixes in one coherent correction batch, run the smallest relevant checks and complete applicable local validation, and inspect the final diff and repository status. Do not update the pull request head with an incomplete or knowingly superseded intermediate state. Treat remote-only validation as a bounded exception and record why it could not be established non-remotely. If this assignment has already made five CI-triggering branch updates, pause before a sixth and report the update count, causes, current CI and review state, unresolved work, validation performed, and consolidation plan; do not update the branch again without explicit authorization. Require every applicable check on the final exact head. In the implementation report, state the number of CI-triggering branch updates and identify any remote-only validation or urgent-safety exception used.

Do not execute OPS, Live QA, external calls, acceptance, closeout, or unrelated work. Return a concise change and proof summary without private chain-of-thought.
```

## PR-04 \- Remove withdrawn closeout machinery and repair CI lanes

Title: Remove withdrawn closeout machinery and repair CI lanes

Intent: Classify the entire execution-ref CI graph under PF10 Addendum 2.3, remove the withdrawn HDE-EPIC038 closeout subsystem, and preserve or narrow only independently justified product and delivery protection.

Implementation Guide source items: D4

Approved requirement:

* Before editing, classify every current trigger, job, step, job condition, permission, `needs` edge, artifact transfer, and direct or indirect source-writing behavior.  
* Answer all ten PF10 Addendum 2.3 questions for each control.  
* Remove the HDE-EPIC038 DEV-01/DEV-02 generator, validators, focused tests, private-receipt production, authenticated receipt consumption, network-enabled generation, updater bindings, and CI bindings created only for the withdrawn lifecycle.  
* Evaluate the release-attestation builder, sanity gate, and sanity pipeline against actual continuing consumers.  
* Retain or narrow only independently justified controls, remove historical epic identity from retained permanent controls, repair triggers and dependencies, and leave no source writeback or closeout-only merge gate.  
* Preserve HDE-EPIC038 implementation history, QA history, failure evidence, and formal nonclaims.  

* Fail closed and block PR-05 if safe classification is incomplete.

* Treat budget-efficient CI as a mandatory PR-04 completion condition, not an optional follow-up or repository-settings suggestion.

* Record the execution-ref cost shape before editing, covering event overlap, jobs, steps, matrices, dependencies, repeated setup and validation, artifact transfers, superseded-run behavior, and required-check conclusions for each material event class.

* Implement the smallest safe repository-grounded changes that prevent duplicate equivalent full-suite eligibility for one exact candidate head, cancel or short-circuit avoidable expensive work on superseded heads, prevent unrelated heavy work, preserve deterministic required-check continuity, preserve rapid feedback and exact-final-head assurance, and keep every independently justified protection in its smallest correct lane.

* Inspect repeated installation, checkout, environment construction, test collection, validators, matrix fan-out, and artifact transfers; reduce or retain each with a concrete continuing-risk justification without weakening deterministic exact-source validation.

* Complete the PF10 Addendum 2.5 validation matrix and record the before-and-after event-to-job execution shape in the implementation report. Prefer static workflow validation, local tests, existing run metadata, and the ordinary final-head CI cycle; identify and justify any bounded remote-only validation cycle.

* If a source change affects a required check name, workflow identity, or reporting surface, identify the exact observed repository-setting dependency and route it to the authorized owner without assuming completion.

Caveats applied: None

PF09 document(s), task IDs, and proof excerpts:

PF09.1-Canon-HDE-Build-Checklist-Calcination, HDE-CALC003:

> ## Task HDE-CALC003 — Repository & Tooling Skeleton

> **Task name/label:** Repository & Tooling Skeleton  
>   
> **Task status:** **Partial**

PF09 subtask IDs and proof excerpts:

HDE-CALC003.21:

> **Subtask name/label:** HDE-EPIC038 closeout subsystem removal and CI-cost cleanup  
>   
> **Subtask description:** Remove the HDE-EPIC038-specific DEV-01/DEV-02 closeout generator, validators, focused tests, private-receipt handling, authenticated receipt-consumption path, network-enabled generation lane, and CI bindings created only for the withdrawn r5 lifecycle. Before deleting a path, prove whether it has any active consumer outside HDE-EPIC038. Preserve genuinely shared generic primitives under their existing owners and remove only the obsolete epic-specific layer.  
>   
> Product Owner disposition: **remove**.  
>   
> Preserve immutable repository and PF10 history, PR \#385 failure evidence, the substantive HDE-EPIC038 implementation and QA record, and every formal-closeout nonclaim. Do not reopen r5 or delete historical evidence to make the current tree appear cleaner.  
>   
> `HDE-CALC003.21` precedes `HDE-CALC003.22`.

PF09 completion role: Completes PF09 item in this epic

PF14 or owning-canon pointers and proof excerpts:

PF10-HDE-Build-Notes, Addendum 2.3:

> 16. HDE-EPIC039 is the implementation home for the current CI remediation. HDE-EPIC039 must inspect the complete current CI workflow at its execution ref and classify every trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior under this addendum. It must:  
> * remove the HDE-EPIC038 doc-delta, token-matrix, private-receipt, authenticated receipt-consumption, and other administrative closeout bindings from required CI;  
> * remove or relocate other epic-specific evidence and closeout controls that fail the continuing-risk test;  
> * preserve or narrow tests that independently protect current product, build, compatibility, security, database, runtime, ordering, rails, release, or deployment behavior;  
> * evaluate release-attestation and sanity-pipeline behavior against actual release, security, or deployment consumers rather than preserving or deleting it by name;  
> * remove historical epic identity and administrative assertions from any retained permanent CI control where the underlying product regression remains valuable;  
> * correct triggers and job conditions so irrelevant documentation, audit, evidence, or historical-only changes do not incur unrelated product CI while required-check semantics remain sound;  
> * repair the job-dependency graph after removals or separations; and  
> * leave no tracked-source writeback, hosted-receipt feedback loop, or closeout-only merge gate.

PF14-Canon-HDE-Mechanics-Guide §27.4:

> * is not a current runtime identity input;  
> * is not regenerated for each later release;  
> * retains its historical producer and capture meaning;  
> * MUST NOT be relabeled as a current external release attestation;  
> * MUST NOT be refreshed merely because the manifest or release ID changes; and  
> * remains subject to historical integrity, secret-safety, and canonical-byte checks.

PF14-Canon-HDE-Mechanics-Guide §27.5:

> * run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, and `ALLOW_NETWORK=0`;  
> * stop on the first failed stage;  
> * make no vendor, database, bridge, deployment, migration, or other external call;  
> * never rerun OPS-02 or OPS-03;  
> * preserve separate current-direct and historical-bridge meanings;  
> * validate canonical JSON, deterministic outputs, rails, direct selection, direct posture, BodyGraph policy, mapped-cache evidence, updater fixed point, portable paths, Mirror/Index hashes, topology, and final LF;

PF07 facts, prerequisites, or reconciliation posture: PF07-Canon-Glow-Infrastructure is not applicable. Branch-protection and required-check settings are not asserted or changed.

Dependencies: PR-03

Observed repo reality:

* Observed repo reality: .github/workflows/ci.yml has `push` and `pull_request` triggers and seven jobs: `test`, `compat-conj-pr01-closure`, `epic020`, `compat-http-epic020`, `epic020-evidence-bundles`, `rails-policy-gates`, and `sanity-pipeline`.  
* Observed repo reality: `test` depends on all six other jobs.  
* Observed repo reality: the workflow actively invokes HDE-EPIC038 focused tests, generation, QA-current-state checks, private-receipt production and upload, authenticated consumption, network-enabled generation, and updater/orientation write sequences.  
* Observed repo reality: tools/evidence/update\_evidence\_index.py retains HDE-EPIC038 QA and closeout constants, loaders, validators, receipt handling, and check-mode bindings.  
* Observed repo reality: tools/evidence/build\_release\_attestation.py invokes tools/evidence/run\_sanity\_pipeline\_gate.py, which invokes tools/evidence/run\_sanity\_pipeline.py.  
* Observed repo reality: tools/evidence/run\_sanity\_pipeline.py identifies the current chain as `HDE-EPIC038-PR06-release-sanity`.

Observed audit provenance: Non-current blockers RB-006 through RB-008 reported incomplete CI classification, active HDE-EPIC038 bindings, and an unclassified builder-to-gate-to-pipeline chain.

Discovery:

* Account for approved PR-01 through PR-03 changes before comparing with the planning baseline.  
* Retrieve and classify the complete execution-ref workflow and every directly invoked script.  
* Record exact control identity, consumer, lane, all ten PF10 answers, disposition, and affected graph edges.  
* Do not edit until the classification is complete.  
* If any control lacks a safe disposition, stop with the classification record, leave the tree unchanged, and block PR-05.

Implementation requirements:

* Delete the active HDE-EPIC038 closeout generator, QA-current-state validator, and focused tests created only for DEV-01/DEV-02.  
* Remove active updater constants and functions owned only by that lifecycle, including all HDE-EPIC038 closeout-family and private-receipt bindings.  
* Remove workflow steps for doc-delta and administrative closeout checks, focused tests, generation, token presentation, receipt production/upload, authenticated receipt consumption, network-enabled regeneration, and receipt-fixed-point confirmation.  
* Remove active dependencies on `GH_TOKEN`, `_HDE_EPIC038_PRIVATE_CI_ROOT`, `_HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID`, `_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST`, and the private-receipt configuration keys used only by the withdrawn flow.  
* Evaluate release-attestation, sanity-gate, and sanity-pipeline scripts against actual consumers. Retain or narrow only independently justified behavior.  
* If retained, remove HDE-EPIC038 identity and administrative closeout assertions from permanent release/sanity mechanics and migrate generic tests to existing generic test homes.  
* If no continuing consumer exists, remove the workflow control without deleting frozen historical evidence.  
* Rebuild workflow triggers, job conditions, permissions, and `needs` edges so every retained edge resolves and irrelevant documentation, audit, evidence, or history-only changes do not incur unrelated product CI.  
* Do not alter repository settings, public behavior, runtime routes, OPS, databases, release identity, or historical evidence.  
* Preserve all files under historical audit and PF-canon roots, HDE-EPIC038 implementation/QA/failure records, and every formal nonclaim.  
* Do not represent removal as HDE-EPIC038 completion.

Concrete anchors:

* Observed repo reality: .github/workflows/ci.yml  
* Observed repo reality: tools/evidence/generate\_hde\_epic038\_closeout.py  
* Observed repo reality: tools/evidence/check\_hde\_epic038\_qa\_current\_state.py  
* Observed repo reality: tests/evidence/test\_hde\_epic038\_closeout.py  
* Observed repo reality: tests/evidence/test\_hde\_epic038\_qa\_current\_state.py  
* Observed repo reality: tests/evidence/test\_hde\_epic038\_release\_sanity.py  
* Observed repo reality: tools/evidence/update\_evidence\_index.py  
* Observed repo reality: tools/evidence/build\_release\_attestation.py  
* Observed repo reality: tools/evidence/run\_sanity\_pipeline\_gate.py  
* Observed repo reality: tools/evidence/run\_sanity\_pipeline.py  
* Observed repo reality: tests/evidence/test\_release\_attestation.py  
* Observed repo reality: tests/evidence/test\_sanity\_pipeline.py  
* Observed repo reality: audit/qa/hde-epic038/

Evidence outputs: PR-04 must create or update the PF06-required same-PR Doc-Delta pair at `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md`; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content. The execution-ref CI classification is returned in Codex’s implementation report and is not a new governed artifact family.

Acceptance tokens: None established as applicable by current PF04 and approved scope.

Rails posture: Closed rails. The network-enabled HDE-EPIC038 generation lane and receipt feedback are removed. Retained hosted validation must be non-writing and justified in its correct PF10 lane.

Basic QA check: Validation predicate: one bounded, budget-efficient post-change validation must combine static workflow inspection, local tests, existing run metadata, and the ordinary final-head CI cycle to prove complete classification of every workflow control; zero active HDE-EPIC038 closeout, receipt, network, or source-writeback bindings; a valid retained job graph; deterministic required-check continuity; and the complete PF10 Addendum 2.5 validation matrix and before-and-after execution shape.

Pass condition: Every current control has all ten PF10 Addendum 2.3 answers and one safe disposition; one ordinary open-pull-request update cannot launch duplicate equivalent full required suites for the same exact head; safely superseded heads do not continue avoidable expensive work; irrelevant changes do not run unrelated heavy jobs; every required check reaches a truthful deterministic conclusion; the exact final candidate receives every applicable protection; repeated setup, validators, matrix expansion, and artifact transfer are reduced or concretely justified; the before-and-after event-to-job shape shows a material reduction in avoidable hosted work; prohibited active names and bindings have zero matches; all retained `needs` targets exist; and historical evidence remains present.

Fail condition: An unclassified control, unresolved consumer, duplicate equivalent full suite, avoidable superseded execution, unrelated heavy execution, missing or false-green required-check conclusion, unvalidated final head, unjustified repeated setup or transfer, inability to show material before-and-after reduction, active prohibited binding, dangling dependency, source-writeback path, unverified repository-setting assumption, historical deletion, or retroactive completion assertion fails PR-04 and blocks PR-05.

PO inputs: None

Codex Prompt:

```
Implement PR-04 only: classify the complete current CI graph, remove the withdrawn HDE-EPIC038 closeout subsystem, and repair lane placement in amthorn78/glow-hdengine-v2.

Repository baseline:
- Default branch: main
- Planning baseline: c20c788baa46312f2d88691b7264caec29d313a0
- Approved predecessors: PR-01, PR-02, and PR-03

Before editing, compare the execution ref with the planning baseline and account only for approved predecessor diffs. Revalidate:
- PF09.1-Canon-HDE-Build-Checklist-Calcination HDE-CALC003.21

* PF10-HDE-Build-Notes Addenda 2.3, 2.4, and 2.5 in full
- PF06-Canon-Epic-Process-Guide PR-first and terminal-lifecycle rules
- PF12-Canon-HDE-Schemas-and-Artifacts §§6.2.2 and 8
- PF14-Canon-HDE-Mechanics-Guide §§1.3.1, 27.4, and 27.5

If another material change affects the workflow, active consumers, historical boundary, or release/sanity ownership, stop before editing and return a concise drift report.

PF09 completion role: complete HDE-CALC003.21 without editing PF09 or claiming status movement.

Primary touched loci:
- Observed repo reality: .github/workflows/ci.yml
- Observed repo reality: tools/evidence/generate_hde_epic038_closeout.py
- Observed repo reality: tools/evidence/check_hde_epic038_qa_current_state.py
- Observed repo reality: tests/evidence/test_hde_epic038_closeout.py
- Observed repo reality: tests/evidence/test_hde_epic038_qa_current_state.py
- Observed repo reality: tests/evidence/test_hde_epic038_release_sanity.py
- Observed repo reality: tools/evidence/update_evidence_index.py
- Observed repo reality: tools/evidence/build_release_attestation.py
- Observed repo reality: tools/evidence/run_sanity_pipeline_gate.py
- Observed repo reality: tools/evidence/run_sanity_pipeline.py
- Observed repo reality: tests/evidence/test_release_attestation.py
- Observed repo reality: tests/evidence/test_sanity_pipeline.py
- Historical audit/QA/HDE-EPIC038 paths are preserve-only.

Do not edit immediately. First produce a complete execution-ref classification covering every workflow trigger, job, step, job condition, permission, needs edge, artifact upload/download/transfer, and directly or indirectly invoked source-writing behavior. For each control, answer exactly:
1. What current product behavior or delivery condition does it protect?
2. What concrete defect or failure does it detect?
3. What material harm does it prevent?
4. Would it remain needed without the originating epic and closeout package?
5. Which lane is correct?
6. Why must it block merge, release, or deployment instead of reporting non-blockingly?
7. Can a smaller or existing mechanism protect the same risk?
8. Does it produce ephemeral engineering output, a release artifact, or tracked administrative evidence?
9. Does it require CI output, run identity, or a later receipt to mutate tracked source?
10. Is failure deterministic, actionable, and owned?

Assign each control one disposition: retain, narrow, remove, or isolate in its correct existing lane. If any disposition is unsafe or ambiguous, stop with the classification report, make no partial edits, and state that PR-05 is blocked.

When classification is complete:
- Remove the HDE-EPIC038 DEV-01/DEV-02 generator, QA-current-state validator, and focused tests that exist only for the withdrawn lifecycle.
- Remove active updater bindings and functions owned only by that lifecycle, including EPIC038_QA_PRIMARY_ARTIFACTS, EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS, EPIC038_CLOSEOUT_KEY_OUTPUTS, EPIC038_CLOSEOUT_FAMILY_KEYS, EPIC038_CLOSEOUT_FAMILY_PATHS, closeout loaders/validators, and private-receipt helpers.
- Remove active CI doc-delta, administrative closeout, focused-test, token-presentation, private-receipt, authenticated-consumption, network-enabled generation, and receipt-fixed-point steps.
- Remove active closeout dependencies on GH_TOKEN and every _HDE_EPIC038 private receipt variable or private-receipt configuration key.
- Inspect the complete build_release_attestation.py to run_sanity_pipeline_gate.py to run_sanity_pipeline.py chain. Preserve or narrow it only if a concrete current release, security, deployment, product, or delivery consumer justifies it.
- If the underlying release/sanity behavior is retained, remove HDE-EPIC038 identity and administrative assertions and preserve equivalent generic coverage in the existing generic test homes.
- Repair triggers, conditions, permissions, and needs edges after removals.
- Leave no hosted source-writeback, receipt feedback, network-enabled closeout generation, or closeout-only merge gate.
- Do not change repository settings.
- Preserve all historical HDE-EPIC038 implementation evidence, QA evidence, failure evidence, PF10 history, and formal-closeout nonclaims. Do not edit or delete historical audit artifacts.
- Do not claim HDE-EPIC038 completion, token satisfaction, QA PASS, acceptance, or closeout.

Same-PR Doc-Delta requirement: Create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md` in PR-04. Preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content.
Basic QA is one bounded post-change static inspection. It must show:
- every workflow control has a completed PF10 classification;
- active code and workflows have zero HDE-EPIC038 closeout/receipt/network bindings;
- every retained needs edge resolves;
- no hosted validation writes tracked source;
- historical evidence paths remain present.

Any unclassified control, unresolved consumer, active prohibited binding, dangling edge, source-writeback path, historical deletion, or retroactive completion assertion fails PR-04 and blocks PR-05.

CI-budget remediation:

1. Before editing, record the execution-ref cost shape for every material event class: events, event overlap, jobs, steps, matrices, conditions, dependencies, repeated setup and validation, artifact transfers, superseded-run behavior, and required-check conclusions.
2. Implement the smallest safe repository-grounded changes so one ordinary open-pull-request update cannot launch duplicate equivalent full required suites for the same exact head; safely superseded heads do not continue avoidable expensive work; irrelevant changes do not run unrelated heavy jobs; every required check reaches a truthful deterministic conclusion; the exact final candidate receives every applicable protection; and every independently justified control remains in its smallest correct lane.
3. Inspect repeated dependency installation, repository checkout, environment construction, test collection, generated-file validation, matrix fan-out, artifact upload and download, and repeated validator execution. Reduce each redundant unit through a safe deterministic mechanism or retain it with a concrete continuing-risk justification.
4. Complete the PF10 Addendum 2.5 validation matrix for an ordinary code update to an open pull request; a second update superseding an in-progress older head; a documentation-only change; an audit-only, evidence-only, or historical-record-only change; a product, build, compatibility, security, release, deployment, or operational change; the exact final pull-request candidate; a default-branch update after merge; and each applicable separate release, security, QA, audit, or closeout event.
5. For each applicable matrix row, state the starting event, required-check conclusion, expensive jobs that run, expensive jobs that do not run and why they are inapplicable, older-run cancellation or short-circuit behavior, equivalent-suite eligibility through another event, and validation proving truthful protection.
6. Record the before-and-after event-to-job execution shape and demonstrate a material reduction in avoidable hosted work without inventing a currency target.
7. Prefer static workflow validation, local tests, existing run metadata, and the ordinary final-head CI cycle. Use an additional hosted cycle only for a genuinely remote-only defect and record the reason.
8. If a source change affects a required check name, workflow identity, or reporting surface, identify the exact observed repository-setting dependency and route it to the authorized owner without fabricating or assuming completion.

Remote-update discipline: Keep iterative commits, targeted tests, and debugging local. Before each ordinary update to the open pull request head, collect the complete current CI and review feedback set, include all safely combinable known fixes in one coherent correction batch, run the smallest relevant checks and complete applicable local validation, and inspect the final diff and repository status. Do not update the pull request head with an incomplete or knowingly superseded intermediate state. Treat remote-only validation as a bounded exception and record why it could not be established non-remotely. If this assignment has already made five CI-triggering branch updates, pause before a sixth and report the update count, causes, current CI and review state, unresolved work, validation performed, and consolidation plan; do not update the branch again without explicit authorization. Require every applicable check on the final exact head. In the implementation report, state the number of CI-triggering branch updates and identify any remote-only validation or urgent-safety exception used.

Do not execute OPS, Live QA, external calls, acceptance, closeout, or unrelated work. Return the complete classification plus concise change and proof summaries without private chain-of-thought.
```

## PR-05 \- Implement a feedback-free generic closeout lifecycle

Title: Implement a feedback-free generic closeout lifecycle

Intent: Provide one epic-agnostic candidate writer/checker and an isolated, non-required hosted validation lane whose terminal state requires no receipt or source feedback.

Implementation Guide source items: D5

Approved requirement:

* Use repository-local tracked inputs to determine all tracked candidate bytes before hosted validation.  
* Provide one authorized candidate writer and a separate non-writing check mode.  
* Keep evidence-ledger and path-proof ownership with the canonical updater.  
* Keep current release attestation external to the source it attests.  
* Require clean-tree, exact-head, deterministic-generation, path, proof, and ledger validation to fail closed.  
* Prove terminal reachability without a later hosted receipt, run identifier, mutable attestation, or later source commit.  
* Keep the lifecycle epic-agnostic and free of HDE-EPIC038 semantics.  
* Keep closeout automation outside required PR CI.  

* Apply PF10 Addendum 2.5 to the proposed hosted validation lane and the final HDE-EPIC039 workflow state. The lane must not become an ordinary open-pull-request full-suite trigger or create duplicate equivalent, avoidable superseded, irrelevant heavy, or false-green execution; the implementation report must update the required validation-matrix closeout row and final before-and-after event-to-job shape after this workflow lands.
* Do not close HDE-EPIC039, establish QA PASS, satisfy tokens, or perform PO closeout.

Caveats applied: None

PF09 document(s), task IDs, and proof excerpts:

PF09.1-Canon-HDE-Build-Checklist-Calcination, HDE-CALC003:

> ## Task HDE-CALC003 — Repository & Tooling Skeleton

> **Task name/label:** Repository & Tooling Skeleton  
>   
> **Task status:** **Partial**

PF09 subtask IDs and proof excerpts:

HDE-CALC003.22:

> **Subtask name/label:** Feedback-free closeout lifecycle reachability  
>   
> **Subtask description:** Implement and prove an epic-agnostic closeout lifecycle in which repository-local inputs determine all tracked candidate bytes before hosted validation, and hosted CI validates those exact bytes without writing canonical results back into tracked source. Require a bounded end-to-end reachability proof for the terminal state before the lifecycle is adopted. Fail closed when any result depends on later receipt-driven source mutation, and preserve deterministic generation, single-writer evidence, path-proof, exact-head validation, and clean-tree responsibilities.  
>   
> PF06, PF12, and PF27 must define the final lifecycle contract before implementation.  
>   
> `HDE-CALC003.21` is a dependency and must be completed first. This subtask must not reuse the removed HDE-EPIC038 receipt-feedback semantics or retroactively complete HDE-EPIC038.  
>   
> Calcination is the single implementation home. Downstream release and phase-exit rows consume this capability and do not become a second implementation home.

PF09 completion role: Completes PF09 item in this epic

PF14 or owning-canon pointers and proof excerpts:

PF06-Canon-Epic-Process-Guide §3.5.1:

> Feedback-free terminal lifecycle.  
>   
> An ordinary Close Gate lifecycle MUST be terminally reachable. All tracked candidate bytes required for the final close state MUST be complete before hosted validation, and hosted CI MUST validate those exact candidate bytes without requiring canonical results to be written back into source.  
>   
> A Close Gate lifecycle MUST NOT require hosted CI to mutate the tracked candidate after validation, require a later source commit to absorb the result needed to validate the earlier candidate, or otherwise create a source-to-CI-to-source causal back-edge.

PF12-Canon-HDE-Schemas-and-Artifacts §6.2.2:

> ### **6.2.2 Acyclic release-attestation and close-pack lifecycle**

> Any future PF12-governed close-pack lifecycle that binds `release_id` or current release provenance MUST preserve the acyclic dependency direction in §6.2.1. All tracked candidate close-pack bytes MUST be complete from tracked repository inputs before hosted CI validates those exact bytes. The lifecycle MUST NOT require a hosted-CI fact that becomes available only after the exact candidate source state is committed to be written back into, or used to derive, the tracked source it attests.  
>   
> Current external attestation MUST remain external to the tracked source it attests. Frozen historical checked-in release evidence MUST NOT be refreshed, relabeled, or used as current-equality evidence to satisfy a future close-pack predicate.

PF14-Canon-HDE-Mechanics-Guide §27:

> The required dependency direction is:  
>   
> `tracked source -> canonical manifest -> release ID -> external attestation`  
>   
> No generated attestation or release derivative may point back into tracked source as an identity input.

PF27-Canon-Plan-Templates:

> * **Terminal-state reachability:** identify the claimed terminal state and prove a feedback-free path from repository-local inputs to the tracked candidate bytes.  
> * **Execution-surface feasibility:** identify every generator, validator, workflow, promotion, and hosted-CI surface required to produce and validate those exact bytes, and prove that each required transition is executable.  
> * **Rails consistency:** state the rails and authorization posture for every transition and require plan or authority revision before any transition that needs a different rails or authorization posture.  
> * **End-to-end proof:** provide a small end-to-end feasibility proof showing that the candidate bytes can reach and be validated at the claimed terminal state without writing canonical results back into already-final tracked source.

PF07 facts, prerequisites, or reconciliation posture: PF07-Canon-Glow-Infrastructure is not applicable. The hosted workflow uses repository source and read-only GitHub Actions permissions only; no repository-setting change is authorized.

Dependencies: PR-04

Observed repo reality:

* Observed repo reality: the complete pinned tree contains no tools/qa/generate\_epic\_close\_pack.py.  
* Observed repo reality: tools/qa/ contains epic-specific generators for EPIC-025 through EPIC-029.  
* Observed repo reality: the current closeout implementation is HDE-EPIC038-specific and uses hosted receipt feedback; PR-04 removes it.  
* Observed repo reality: tools/evidence/update\_evidence\_index.py, tools/evidence/orientation\_demo.py, evidence-path validation, mirror-schema validation, and final-LF validation provide the retained evidence-skeleton check surfaces.  
* Observed repo reality: .github/workflows/ci.yml is the only current workflow file at the planning baseline.

Observed audit provenance: Non-current blockers RB-009 and RB-010 reported no generic lifecycle and no HDE-EPIC039 candidate surfaces. The latter absence is expected at implementation-planning time and does not authorize closeout artifact creation in PR-05.

Discovery:

* Compare the proposed component boundary and controlling PF06/PF12/PF14/PF27 units to the baseline plus approved PR-01 through PR-04 changes.  
* Confirm PR-04 removed the receipt-feedback lifecycle and established stable retained evidence/release ownership.  
* Inspect existing epic-specific generators only for reusable pure mechanics; do not import their epic identities or historical assertions.  
* Stop if PR-04 is incomplete or a current generic writer already exists with materially different ownership.

Implementation requirements:

* Create one generic candidate writer/checker at the approved path.  
* Add a closed, canonical JSON input schema for repository-local candidate-source data. The source contains stable epic identity, tracked plan and evidence-input paths, deterministic report sections, output bindings, and explicit nonclaims. It cannot contain run IDs, hosted receipts, mutable attestation inputs, or a later commit dependency.  
* Require an exact tracked repository-relative source path and exactly one explicit mode: authorized write or non-writing check.  
* Derive canonical close-report and manifest paths from the validated epic ID. Caller-selected output roots are prohibited.  
* In write mode, render all candidate output bytes in memory, validate every input and output path, then publish atomically. Do not write evidence ledgers or external attestations.  
* In check mode, compute expected bytes and compare them with committed candidate bytes. Do not create, repair, touch, or normalize files.  
* Require the canonical evidence updater to bind path proofs and ledgers after local generation and before commit. Hosted validation runs updater and orientation checks only.  
* Add an isolated manual closeout-validation workflow with `contents: read`, no write permission, no artifact receipt, no network-enabled application behavior, and no required-PR-CI posture.  
* The hosted workflow checks out the selected exact ref, requires a clean tree, validates the tracked candidate-source path, runs generic check mode and retained read-only ledger/proof checks, and proves the tree remains clean afterward.  
* Do not store a commit hash inside candidate source as a self-referential identity. Exact-head proof comes from the checked-out clean ref and tracked bytes.  
* Add a bounded temporary-repository test proving: write from tracked local inputs; commit; exact-head clean check; byte-identical second render; no diff; rejection of later receipt, run identity, mutable attestation, later-commit dependency, dirty tree, missing input, path escape, nondeterminism, and attempted check-mode write.  
* Do not generate an HDE-EPIC039 close report, close manifest, acceptance map, token-evidence matrix, QA log, or close candidate in PR-05. The PF06-required same-PR Doc-Delta pair remains mandatory PR parity evidence and does not constitute candidate generation, acceptance, or closeout.  
* Do not create tokens, perform QA, make acceptance decisions, or perform Product Owner closeout.

Concrete anchors:

* Proposed path: tools/qa/generate\_epic\_close\_pack.py  
* Proposed path: schemas/epic\_close\_candidate\_source.v1.json  
* Proposed path: tests/qa/test\_generate\_epic\_close\_pack.py  
* Proposed path: .github/workflows/epic-closeout-validation.yml  
* Observed repo reality: tools/evidence/update\_evidence\_index.py  
* Observed repo reality: tools/evidence/orientation\_demo.py  
* Observed repo reality: ci/checks/check\_mirror\_schema.sh  
* Observed repo reality: tools/evidence/validate\_evidence\_paths.py  
* Observed repo reality: ci/checks/check\_final\_lf.sh

Evidence outputs: PR-05 must create or update the PF06-required same-PR Doc-Delta pair at `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md`; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content. PR-05 implements capability and feasibility proof; it does not produce a real epic close candidate.

Acceptance tokens: None established as applicable by current PF04 and approved scope.

Rails posture: Local generation is authorized, deterministic, repository-local, and closed-rails. Hosted validation is manual, non-required, read-only, receipt-free, and clean-tree enforcing.

Basic QA check: Validation predicate: tests/qa/test_generate_epic_close_pack.py must prove the complete temporary-repository writer-to-commit-to-hosted-check state machine and every prohibited feedback dependency without touching the real repository’s governed artifacts; bounded static workflow validation must also prove that the proposed hosted lane remains manual, non-required, read-only, outside ordinary pull-request CI, and represented in the final PF10 Addendum 2.5 validation matrix and before-and-after execution shape.

Pass condition: A candidate generated entirely from tracked local inputs reaches a clean exact-head read-only validation state with identical expected bytes and no later source mutation; the hosted lane cannot create duplicate equivalent full-suite eligibility, avoidable superseded work, unrelated heavy execution, a missing or false-green required-check conclusion, or unjustified repeated setup; and the final combined HDE-EPIC039 execution shape retains the material reduction established by PR-04.

Fail condition: A receipt, run ID, mutable attestation, later commit, caller-selected output root, dirty tree, missing input, path escape, nondeterministic render, check-mode write, second ledger, HDE-EPIC038 identity, ordinary pull-request full-suite trigger, duplicate equivalent execution, avoidable superseded work, unrelated heavy execution, false-green conclusion, unjustified repeated setup, or regression of the final before-and-after execution shape fails PR-05.

PO inputs: None

Codex Prompt:

```
Implement PR-05 only: create an epic-agnostic, feedback-free closeout-candidate lifecycle in amthorn78/glow-hdengine-v2.

Repository baseline:
- Default branch: main
- Planning baseline: c20c788baa46312f2d88691b7264caec29d313a0
- Approved predecessors: PR-01 through PR-04
- Hard dependency: PR-04 must have removed the HDE-EPIC038 receipt-feedback lifecycle and completed the CI classification.

Before editing, compare the execution ref with the baseline plus approved predecessor diffs. Revalidate:
- PF09.1-Canon-HDE-Build-Checklist-Calcination HDE-CALC003.22
- PF06-Canon-Epic-Process-Guide feedback-free terminal lifecycle

* PF10-HDE-Build-Notes Addenda 2.3, 2.4, and 2.5 lane, committed-source validation, autonomous-update discipline, and budget-efficiency rules
- PF12-Canon-HDE-Schemas-and-Artifacts §§6.2.2 and close-pack baseline contract
- PF14-Canon-HDE-Mechanics-Guide §27
- PF27-Canon-Plan-Templates terminal-reachability rules

Stop before editing if PR-04 is incomplete, an active receipt-feedback path remains, or a materially different generic writer already owns this component. Return a concise drift report; do not reinterpret canon.

PF09 completion role: complete HDE-CALC003.22 without editing PF09 or claiming status movement.

Exact planned loci:
- Proposed path: tools/qa/generate_epic_close_pack.py
- Proposed path: schemas/epic_close_candidate_source.v1.json
- Proposed path: tests/qa/test_generate_epic_close_pack.py
- Proposed path: .github/workflows/epic-closeout-validation.yml

Retained integration loci:
- Observed repo reality: tools/evidence/update_evidence_index.py
- Observed repo reality: tools/evidence/orientation_demo.py
- Observed repo reality: ci/checks/check_mirror_schema.sh
- Observed repo reality: tools/evidence/validate_evidence_paths.py
- Observed repo reality: ci/checks/check_final_lf.sh

Inspect existing epic-specific generators only for reusable pure functions and repository conventions. Do not copy epic identity, historical assertions, receipt behavior, network behavior, or acceptance claims.

Implement these requirements:
1. Create tools/qa/generate_epic_close_pack.py as the sole generic candidate-output writer.
2. Create schemas/epic_close_candidate_source.v1.json as a closed canonical-JSON input contract. It must carry stable epic identity, tracked plan and evidence-input paths, deterministic report sections, key-output bindings, and explicit nonclaims. The owning schema MUST include $schema with the exact value https://json-schema.org/draft/2020-12/schema and $id with the stable repository-path identity schemas/epic_close_candidate_source.v1.json.
3. The input schema must reject unknown keys and any run ID, hosted receipt, mutable attestation, later-commit result, caller-selected output root, or other feedback dependency.
4. Require one tracked repository-relative candidate-source path and exactly one mode: authorized write or read-only check.
5. Derive the canonical close report and close manifest paths from the validated three-digit epic identity. Do not accept output-root overrides.
6. Write mode must load only tracked repository-local inputs, render every candidate output in memory, validate path containment and deterministic bytes, and publish atomically. It must not update the Human Index, Machine Mirror, path proofs, release identity, or external attestation.
7. Check mode must render expected bytes and byte-compare the committed candidate. It must not create, modify, normalize, repair, chmod, or timestamp anything.
8. After local write mode, the existing canonical evidence updater remains the sole ledger/proof writer. Hosted validation uses only updater --check, orientation --check, mirror-schema, evidence-path, hash, and LF checks.
9. Create .github/workflows/epic-closeout-validation.yml as isolated manual epic-closeout automation. Use contents: read, exact-ref checkout, clean-tree precheck, generic check mode, retained read-only evidence checks, and clean-tree postcheck.
10. The workflow must not be required PR CI, upload or consume a receipt, write tracked source, enable application network behavior, mutate repository state, or use a hosted result as a later source input.
11. Do not embed a source commit hash in candidate bytes. Exact-head identity is proven by the checked-out clean ref and byte comparisons.
12. Add one bounded temporary-repository test module that proves:
   - tracked local inputs to authorized writer;
   - atomic candidate production;
   - commit of the complete candidate;
   - clean exact-head read-only validation;
   - deterministic second rendering and zero diff;
   - failure on missing, empty, partial, untracked, escaping, or ambiguous inputs;
   - failure on run IDs, receipts, mutable attestations, later commits, dirty trees, nondeterminism, and check-mode writes.
13. The component must be epic-agnostic and contain no HDE-EPIC038 identity or semantics.
14. Do not generate an HDE-EPIC039 close report, close manifest, acceptance map, token-evidence matrix, QA log, or close candidate in this PR. Create or update `audit/docdeltas/hde-epic039_doc_deltas.md` and `audit/qa/hde-epic039/00_meta/doc_deltas.md` as the PF06-required same-PR Doc-Delta pair; preserve existing proof-bearing content; keep the two files byte-identical; include PF references per entry; and maintain same-PR code, docs, Human Evidence Index, Machine Mirror, and path-proof parity. Emit “no deltas” only when neither surface contains generated, proof-bearing, remediation, drain-target, or closeout-relevant content. This pair does not constitute candidate generation, acceptance, or closeout.
15. Do not create or claim tokens, QA PASS, acceptance, PF09 movement, OPS completion, Product Owner closeout, or epic closure.

Basic QA is the new temporary-repository lifecycle test. Pass requires a terminal candidate state reached entirely from tracked inputs and validated at clean exact HEAD without any source-to-hosted-validation-to-source feedback. Any prohibited dependency or mutation fails.

No acceptance token is established for this PR. Do not invent one.

CI-budget requirements: Treat the proposed `.github/workflows/epic-closeout-validation.yml` as part of the final HDE-EPIC039 execution shape. Keep it manual, non-required, read-only, and outside ordinary pull-request CI. Prove that it cannot create duplicate equivalent full-suite eligibility, avoidable superseded work, unrelated heavy execution, a missing or false-green required-check conclusion, or unjustified repeated setup. Complete the applicable closeout-event row of the PF10 Addendum 2.5 validation matrix and update the final before-and-after event-to-job execution shape after the workflow lands. Fail closed if the new lane regresses the material reduction established by PR-04 or relies on an unverified repository-setting assumption.

Remote-update discipline: Keep iterative commits, targeted tests, and debugging local. Before each ordinary update to the open pull request head, collect the complete current CI and review feedback set, include all safely combinable known fixes in one coherent correction batch, run the smallest relevant checks and complete applicable local validation, and inspect the final diff and repository status. Do not update the pull request head with an incomplete or knowingly superseded intermediate state. Treat remote-only validation as a bounded exception and record why it could not be established non-remotely. If this assignment has already made five CI-triggering branch updates, pause before a sixth and report the update count, causes, current CI and review state, unresolved work, validation performed, and consolidation plan; do not update the branch again without explicit authorization. Require every applicable check on the final exact head. In the implementation report, state the number of CI-triggering branch updates and identify any remote-only validation or urgent-safety exception used.

Do not execute OPS, Live QA, external calls, acceptance, closeout, or unrelated work. Return a concise state-transition proof and change summary without private chain-of-thought.
```

# Ops tasks

NO OPS TASKS.

# PO Inputs Summary

None.

# ADRs

NO ADRS.

# Canon Creation / Reconciliation Requirements

NO CANON CREATION OR RECONCILIATION REQUIRED.

ASK OK?  
