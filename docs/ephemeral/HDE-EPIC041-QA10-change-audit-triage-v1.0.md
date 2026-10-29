---
artifact_type: CHANGE_AUDIT_TRIAGE
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA10-CHANGE-AUDIT-TRIAGE
CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-EPIC041-QA10-change-audit-triage-v1.0.md
state: COMPLETE
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
predecessor: none (first QA-10 triage for HDE-EPIC041)
audit_triaged: docs/ephemeral/HDE-EPIC041-QA10-reality-audit-v1.0.md (REALITY_AUDIT v1.0, COMPLETE; read end to end before this triage)
readiness_record: docs/ephemeral/HDE-EPIC041-QA10-qa-readiness-v1.0.md
producer: Isis, the continuing Lead Developer and whole-change readiness decision owner for HDE-EPIC041 (role continuity per D27; platform session identity not directly known)
prompt: QA-10 — Audit Implementation and Establish QA Readiness — 102726.1 (https://app.notion.com/p/4064590a05eb8161b170fbb23f7aeb28; page state 2026-10-27T13:07:31.843Z)
r1_row: GCF-20.TRIAGE
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head: 6a0f55f07607ddfea5590ed8ee080764e029b31a
approved_bases: Specification v1.1 (docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md; Thoth CF-E-30 INITIAL_APPROVE) → Implementation Plan v1.1 (docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md; Isis IA-30 INITIAL_APPROVE)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md (741 lines, sha256 6fa054b1e51cf76fd795e460cec039a51caf99cec16fe1521f0a00febff15f3c; read in full; provenance)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-10
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; CCR-5 (close-stage ordering) PROPOSED by this triage (finding #28, §6), not yet reviewed
triaged_at: 2026-10-29 (UTC)
GCFPE_PROMPT_USES: as the Reality Audit front matter (usage HDE-EPIC041-QA10-20261029)
---

# HDE-EPIC041 — Change Audit Triage v1.0 (QA-10)

This is the finding-by-finding triage of the Reality Audit v1.0. It records, for each finding, the observed behavior, the requirement or decision it is compared with, its implications and evidence limits, its owner and its existing native route. It is an analytical record. It is not PF10 insertion text, assigns no PF10 number and claims no canonical adoption. QA-10 produces no `PF10_BUILD_NOTES_ADDENDUM`; where a later native decision could need one, the finding names that decision's owner. The full evidence stays in the Reality Audit; this record links to it and never substitutes for it.

## 1. Summary

* **Audit summary.** The delivered HDE-EPIC041 boundary matches the approved Specification and Plan at `main` `6a0f55f0`: one Adapter-owned chart entry, one pure Engine chart module, the mixed loader removed with a guard, the callers migrated, outputs and failures preserved; no approved objective is shown to be unmet.
* **Drift theme:** "canon still describes the removed chart loader as current; governed QA evidence not yet produced".
* **Findings:** 18 audit observations (QA10-OBS-01 to -18), 78 PF23 comparison rows (Reality Audit §12.3) and one canon-to-canon conflict found while reconciling readiness (#28, CCR-5), in 28 coverage rows (§2). Prior-stage carried items are listed separately (§5).
* **Must-act-now:** 2 (QA10-OBS-12, for the named dependent passes QA-20 and QA-50; #28, for a Product Owner ruling before CL-05 runs).
* **Objective failures:** none evidenced. Readiness consequence: none of the findings blocks readiness (the readiness record decides).
* **PF homes consulted:** HDE Architecture; HDE Mechanics Guide; HDE Build Checklist — Separation; HDE Governance; Glow QA Guide; Change Process Guide; HDE State of the Repository (reference); HDE Build Notes.
* **PF homes receiving proposals:** HDE Architecture and HDE Mechanics Guide (existing DELTA-001 and DELTA-002, post-QA drainage); HDE State of the Repository (new candidate DELTA-003, reference document). Open question for the Product Owner: HDE Build Notes §2.2 R-3 against Change Process Guide §3.5.1, Glow QA Guide §3.1.3 and Plan Templates §3B (CCR-5).
* **PF09 task delta proposed:** none now. PF09 row-closure facts are preserved in §4 without originating a row-closure review.
* **PF-canon doc delta proposed:** DELTA-003 (candidate). DELTA-001 and DELTA-002 already exist and fully cover QA10-OBS-08 and -09. CCR-5 is an open question, not a proposed edit.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `6a0f55f0`. The Reality Audit's "Canon relied on" block lists every source, version and section read; this table maps each triage decision topic to its governing section.

| Decision topic | Governing source (title, section) | Proof excerpt (verbatim, short) |
| :- | :- | :- |
| Triage fields and doc-delta homes | Change Process Guide §2.2 "Findings → Doc Delta Map (required; single sink)"; "Classification-only audit posture" | "A finding MAY be Must-act-now while still requiring no PF09 task delta." |
| A drift observation is not a gate; objective failure is | HDE Governance §9.1.5 readiness table; Glow QA Guide §3.1.1 | "Historical discrepancy, debt or future improvement does not demonstrate objective failure" |
| PF23 observations route to owning homes, not to work | HDE Governance §2.0.18 "PF23 audit observation classification" | "MUST NOT be converted into a PF09.x task delta, implementation remediation, OPS task, Live QA task, or PF20 historical correction by assumption" |
| Drift stub and tentative bucket | HDE Governance §2.0.18 "Drift assessment protocol (stub)" | "Classify the drift into exactly one bucket (tentative): canon defect, implementation drift, or necessary reality shift." |
| Doc deltas drain only after QA | Change Process Guide §3.5.2.8 "Post-QA documentation drainage ordering (normative)" | "Drainage into canon, checklist rows, guides, or other document homes occurs only after all QA tasks for the epic are complete." |
| Canon wording on the loader | HDE Architecture §1.1 "Non-BodyGraph chart loader classification"; HDE Mechanics Guide §1.1 "BodyGraph and loader seam posture" | "The checked-in loader remains current repository reality until separately remediated"; "This is a required mechanics disposition, not a claim that relocation, caller migration or removal has occurred." |
| PF09 completion and governed evidence | HDE Build Checklist — Separation §0.6 "Completion Standard"; Task HDE-SEPA006 "Deliverables and required evidence"; Subtask .3 "Evidence / artifacts required" | "required governed evidence is complete and internally consistent"; "Required governed evidence is indexed through the existing authorized writer" |
| QA evidence indexing | Glow QA Guide §3.2 "Checklist" ("Same-PR parity (merge-blocking)"); §3.1.3 (close mutation set) | "`docs/evidence/INDEX.json` plus `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl` must be updated in the same PR as the captured evidence." |
| What may depend on planning records | HDE Build Notes 2.2 R-1, R-2 | "No code, test, tool, CI step, workflow, schema, governed evidence artifact, close pack, manifest, Index or Mirror row or path proof reads, binds, hashes, resolves or requires a path under docs/ephemeral/." |
| Deferred obligations of earlier units | HDE Build Notes 2.3 and 2.4 "Deferred obligations and unresolved work" | Reality Audit §12.2 maps each |
| Close-stage ordering (finding #28, CCR-5) | HDE Build Notes §2.2 R-3 "The close-pack writer runs only at close"; Change Process Guide v2.5.5 §3.5.1 "Requirement", paragraph "Close-mutation-set stage" (Entries, Exit, What it owns); Glow QA Guide v3.0.7 §3.1.3 "Permanent drainage and post-closure administration"; Plan Templates v2.0.6 §3B "Close Mutation Set Task Record (Template)", "Entries and exit (normative)" (each read in full); HDE Build Notes "Precedence, versioning, and scope" §1 "PF10 authority"; AGENTS.md "PF10's authority in the canon" | R-3: "after the authorized QA verdict and the closure decision exist"; Change Process Guide: "It sits between the final QA Report and the closure decision."; precedence: "that addendum … supersedes conflicting permanent PF canon until the guidance is formally reviewed and drained" |
| Approved scope, objectives, exclusions | Specification v1.1 §2 to §11; Specification review v1.1 §5 (CCR-1 to CCR-4); Plan v1.1 §2, §5, §6, §10 to §13; Plan review v1.0 N-4; Plan review v1.1 §3 (N-5) | Quoted per finding below |

HDE Build Notes 2.1 is not engaged: no finding touches vendor route selection, the production vendor override, the compat route, evidence-tool output roots or gate rows. Canon silence: none decisive. Scoped override: the integrated QA-10 actor and timing (HDE Governance §9.1.5) over Reality Audits' PO-at-closure intent, as the Reality Audit records.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Coverage map (one row per finding)

Repo check: the finding was re-verified directly against `6a0f55f0` for this triage (Confirmed) or rests on the stated evidence. Plan linkage: the approved objective or section. Primary action: objective repair · evidence recovery · later QA evidence · later development/documentation · fully covered duplicate · external follow-up · no action.

| # | Finding | Repo check | Plan linkage | Doc-delta disposition | Primary action | Owner | Must-act-now | Readiness impact |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| 1 | QA10-OBS-01 entry owns the R-01 concerns | Confirmed (E-018, E-019) | Spec R-01/AC-01; Plan §5.1, I-2, §5.3; WU-PR-01 | No doc delta needed: canon already states the required ownership (HDE Architecture §1.1) and DELTA-001 covers its stale sentence | No action; runtime verification carried to QA | Isis (QA-20 Guide) → Kronos (QA-50) | NO | None (achieved; QA owed) |
| 2 | QA10-OBS-02 pure module | Confirmed (E-013, E-014) | Spec R-02/AC-02; Plan I-1; WU-PR-01 | No doc delta needed (HDE Architecture §1.1 Purity rule already governs) | No action; QA owed | Isis → Kronos | NO | None |
| 3 | QA10-OBS-03 loader removed, callers migrated, guard | Confirmed (E-012, E-030, N-001, N-003) | Spec R-03/AC-03; Plan WU-PR-02; D-1 | No doc delta needed beyond DELTA-001/-002 | No action; QA owed | Isis → Kronos | NO | None |
| 4 | QA10-OBS-04 outputs and failures preserved | Confirmed (E-036, E-026, E-027, E-011) | Spec AC-05; Plan I-3 to I-5 | No doc delta needed | No action; QA owed | Isis → Kronos | NO | None |
| 5 | QA10-OBS-05 R-04 checks exist and passed exact-head CI; no QA yet | Confirmed (E-029, E-033); CI from recorded evidence (E-031) | Spec R-04/AC-04, §9 | No doc delta needed | Later QA evidence | Kronos (QA-50), QA executor | NO | None; independent QA owed |
| 6 | QA10-OBS-06 C-1 migrated; exit 2 preserved | Partially confirmed: import and code path read (E-030 static, N-006); exit 2 from recorded CI and PR-40 evidence on identical code (E-031, E-032); not reproducible here without installing requirements | Spec R-03; Plan I-4; Audit ED-07 | No doc delta needed | Later QA evidence (reproduce with CI's install) | Kronos | NO | None |
| 7 | QA10-OBS-07 open-rails binding conditions not met | Confirmed (N-004, E-018) | Spec §4 items 3 and 4, "Implementation preservation"; Plan §11 | No doc delta needed | No action; carry items 3 and 4 verbatim into the Guide and QA Plan | Isis (QA-20); Kronos (QA-50) | NO | None |
| 8 | QA10-OBS-08 HDE Architecture §1.1 calls the loader current | Confirmed (E-012) | Plan WU-PR-03 (DELTA-001 carried in #800) | Duplicate of existing issue: DELTA-001 (Implementation Audit v1.0 §9; HDE Build Notes 2.4), fully covering | Fully covered duplicate; drain after QA | Canon owner (Product Owner) | NO | None (drainage is not a gate, Change Process Guide §3.5.2.8) |
| 9 | QA10-OBS-09 HDE Mechanics Guide §1.1 likewise | Confirmed (E-012, E-018) | As #8 (DELTA-002) | Duplicate of existing issue: DELTA-002, fully covering | Fully covered duplicate; drain after QA | Canon owner (Product Owner) | NO | None |
| 10 | QA10-OBS-10 HDE State of the Repository §2.2 calls the loader current | Confirmed (E-012) | None (reference document outside the Plan's DELTA list) | Doc delta proposed: DELTA-003 (§3, finding 10) | Later documentation (post-QA) | Product Owner (reference-document owner) | NO | None |
| 11 | QA10-OBS-11 PF09.3 HDE-SEPA006 rows read Not done | Confirmed | Spec §2.2, §7 status nonclaims; Plan §7 | No doc delta needed now: the §0.6 predicates are not yet met; the post-closure PF09 update is the authorized owner's (§4) | No action now; PF09 row-closure facts preserved (§4) | Product Owner (post-closure PF09 update) | NO | None |
| 12 | QA10-OBS-12 no governed evidence for HDE-EPIC041 yet (review v1.0 N-4) | Confirmed (E-021) | Spec §8, §9, §10; Plan §10; PF09.3 §0.6, Task deliverables, Subtask .3 | No doc delta needed: canon already requires it | Later QA evidence: governed, indexed boundary and caller-regression evidence and doc-delta capture in QA; close mutation set at CL-05 | Isis (QA-20 carries it); Kronos (QA-50 plans it); CL-05 | **YES** (QA-20, QA-50) | None for readiness; a QA-planning dependency |
| 13 | QA10-OBS-13 `cline_skills/` unclassified by CI | Confirmed (E-008, E-035); hosted outcome Unknown | None (outside HDE-EPIC041) | No doc delta needed | External follow-up | Product Owner | NO | None (no HDE-EPIC041 surface involved) |
| 14 | QA10-OBS-14 register-bound operating procedure path absent on `main` | Confirmed (N-007) | None (GCFPE governance) | No doc delta needed | External follow-up (ecosystem defect report) | GCFPE management (GCFPE-MGMT-10) | NO | None (the register states the procedure restates no rule) |
| 15 | QA10-OBS-15 generator compat computation not restored (Audit FND-005) | Confirmed (N-006) | Plan §2 exclusion | Duplicate of existing issue: Audit FND-005, fully covering | Fully covered duplicate | CL-40 scan; Product Owner | NO | None (excluded scope) |
| 16 | QA10-OBS-16 `input_validators` CWD reads and TZ read (FND-006; OBS-1) | Confirmed (E-016) | Plan §2 exclusion | Duplicate: Audit FND-006 | Fully covered duplicate | CL-40 scan; Product Owner | NO | None |
| 17 | QA10-OBS-17 architecture snapshot stale (FND-007) | Confirmed (E-025) | Plan §2 exclusion; WU-PR-03 OBS-D1 | Duplicate: Audit FND-007 (and OBS-D1 for the close-time capture) | Fully covered duplicate | CL-40 scan; Product Owner; CL-05 for OBS-D1 | NO | None |
| 18 | QA10-OBS-18 repository documentation matches the code | Confirmed | Plan WU-PR-03; DOC-20 COMPLETE | No doc delta needed | No action | — | NO | None |
| 19 | H: RA-20261026-08 and FND-022 Resolved | Confirmed (same evidence as #3) | Spec R-01 to R-03 | No doc delta needed (PF23 records are dated; the PO's manual PF23 update may cite this audit) | No action | Product Owner (PF23 publication, non-gating) | NO | None |
| 20 | H: RA-20261026-06 and FND-018 Changed (hosted CI) | Confirmed for recorded runs; the current head's run Unknown | None | Duplicate of #13 for the current head; otherwise no doc delta | No action beyond #13 | Product Owner | NO | None |
| 21 | H: RA-08 Changed (test counts) | Confirmed (E-009) | None | No doc delta needed (informational) | No action | Product Owner (PF23) | NO | None |
| 22 | H: RA-18 Changed (C040 drainage) | Confirmed (PF10 0 hits; AGENTS.md:140) | None | No doc delta needed | No action | Product Owner (PF23) | NO | None |
| 23 | H: FND-009 Changed (root counts) | Confirmed (E-004) | None | No doc delta needed | No action | Product Owner (PF23) | NO | None |
| 24 | H: RA-09 Unverifiable | Not checked because no new evidence exists for those earlier units | None | No doc delta needed | No action | Product Owner (PF23) | NO | None |
| 25 | H: RA-10 Unverifiable | Not checked because no DB probe is permitted (HDE-COAG003.8 owns it) | None | No doc delta needed | No action | PF09.7 HDE-COAG003.8 owner | NO | None |
| 26 | H: 69 Persistent rows (membership: Reality Audit §12.3, 16 re-checked, 53 carried) | Confirmed for the 16; carried by byte identity for the 53 | None of them touches HDE-EPIC041's surfaces | No doc delta needed from this change (historical) | No action | Product Owner (PF23 publication, non-gating) | NO | None |
| 27 | Bounded, not re-compared: PF23 §12.1.B canon-claim rows and §12.4 item rows | Not checked because those comparisons were made against replaced canon versions and outside this change's scope | None | No doc delta needed from this change | No action | Product Owner (PF23) | NO | None |
| 28 | Canon-to-canon conflict on when the close pack is written relative to the closure decision (found while reconciling readiness; not a repository observation) | Not repo-verifiable (canon text); each clause read in full and quoted (§3, #28) | Specification §10, §6 D5; Plan v1.1 DL-04 ("CL-05 (GCF-24.CLOSE), after a QA PASS") | Open question for PO | External follow-up: canon decision; recorded as CCR-5, PROPOSED (§6) | Product Owner (canon owner and author of HDE Build Notes §2.2) | **YES** (Product Owner ruling before CL-05 runs; meanwhile R-3 governs as written) | None (bears on CL-05, not on readiness or QA) |

## 3. Finding records

Each record states observed behavior, requirement or decision, implications, evidence limits, owner and native route. Evidence ids are the Reality Audit's.

**1. QA10-OBS-01 — Adapter-owned orchestration (R-01).**
* Observed: `adapter/chart_orchestration.py::load_chart` reads `SAFE_MODE` for the log field, both clocks and the correlation id, reads the two pinned lists anchored at the repository root, returns the normalized fixture chart and emits exactly one keys-only line per call to the injected sink or the module logger; no route, no file write (E-018, E-019, N-004, N-005).
* Requirement: Specification R-01 ("…belong to one supported Adapter-owned orchestration entry…"), AC-01; Plan v1.1 §5.1 and §5.3; PF09.3 Task "Implementation / integration boundary". The resolver/ingest clause is vacuous: no acquisition exists on the supported path (Audit §4 R-01 "Feasibility").
* Implications: achieved at the implementation level. Independent runtime verification of AC-01 under closed rails is owed to QA.
* Limits: local probes are not QA or CI.
* Owner and route: QA-20 Guide (continuing Isis) records it as delivered behavior to verify; Kronos plans it at QA-50.

**2. QA10-OBS-02 — Pure Engine computation (R-02).**
* Observed: `engine/charts/pure.py` imports only `re`, `unicodedata`, `typing`; the delivered AST deny-list and fresh-interpreter harness pass, and their three negative self-tests fail planted violations (E-013, E-014).
* Requirement: Specification R-02, AC-02 ("…with none of the listed side effects, including at import"); HDE Architecture §1.1 "Purity rule (normative)…no import-time side effects"; Plan I-1, as corrected for later stages by AUD-CORR-1 (HDE Build Notes 2.3).
* Implications: achieved; QA verifies independently.
* Limits: the harness patches the entry points it lists; an effect through an unlisted entry point is outside its proof (stated limit of the delivered check, not an observed effect).
* Owner and route: as #1.

**3. QA10-OBS-03 — Caller migration and retirement (R-03).**
* Observed: `engine/charts/` holds only `pure.py`; the guard's scan of 518 files finds no importer or `_call_legacy`; 69 inventory files (25 live, 44 historical) each have a disposition; legacy shapes raise `TypeError` (E-012, E-019, E-030, N-001, N-003; Reality Audit §12.4).
* Requirement: Specification R-03, AC-03; Product Owner decision D-1 ("Retire it"; Audit §8.1); Plan WU-PR-02 Scope ("No shim is kept"); PF09.3 Subtask .2 ("Do not treat an import-path rename as complete migration").
* Implications: achieved; TI-06 is moot (no compatibility surface retained). The guard does not recognize a module name assembled at run time or reached through a parent-package attribute; the WU-PR-02 lineage review recorded that limit, and such a form would fail at import because the module is absent.
* Limits: none decisive.
* Owner and route: as #1.

**4. QA10-OBS-04 — Preserved outputs and failures; no fallback; clean tree (AC-05).**
* Observed: 13 of 13 shapes equal between the removed loader and today's entry; compat bytes, the tracked log and release membership unchanged; fallback gone; no tracked change after the probes (E-036, E-011, E-026, E-027, N-002, N-010).
* Requirement: Specification AC-05; Plan I-3, I-4 (the legacy-routed `TypeError` is the one intended change), I-5; HDE Mechanics Guide §1.1 remediation ("preserve existing canonical outputs").
* Implications: achieved; the one intended failure change is documented (CHANGELOG, QA10-OBS-18).
* Limits: the C-1 part rests on recorded evidence (#6).
* Owner and route: as #1.

**5. QA10-OBS-05 — Boundary checks (R-04).**
* Observed: five new or migrated test files plus the two loader tests exist and are owner-registered; each work unit's exact-head hosted CI passed (E-029, E-031, E-033). No HDE-EPIC041 QA has run (E-021).
* Requirement: Specification R-04, AC-04; §9 "Live QA is required for eventual close of this Epic"; PF09.3 Subtask .3 ("independent QA and acceptance retain their applicable owners").
* Implications: the implementation part of R-04 is delivered. AC-04's "all pass, with … recorded" is met in the PR records; its independent verification is QA's.
* Limits: hosted CI read through the lineage reviews, not directly (no API access).
* Owner and route: Kronos, QA-50 → QA-70 → execution under the Product Owner's chosen arrangement.

**6. QA10-OBS-06 — The compat-determinism generator (C-1).**
* Observed: line 9 imports the entry; `main()` exits 2 with `compat_public not implemented` before any chart call (static read; N-006). The exit-2 run is evidenced by the generator test in the exact-head CI of #796 and by the WU-PR-02 reviewer's local run at `9843934f`; the script and `engine/compat/compute.py` are byte-identical since then (E-031, E-032). A local run here exits 1 on a missing `jsonschema` (E-030).
* Requirement: Specification R-03 ("…including the active compatibility-determinism artifact generator…preserves governed caller output and failure behavior"); Plan I-4; Audit ED-07.
* Implications: achieved on attributable evidence for identical code. QA reproduces it with CI's install (WU-PR-03 plan OBS-10: the test needs the repository's requirements).
* Limits: no local reproduction in this audit, by the no-install boundary.
* Owner and route: Kronos (QA-50).

**7. QA10-OBS-07 — Open-rails binding conditions.**
* Observed: no production entry point, CLI path or vendor path reaches the entry or the pure module; the boundary acquires nothing from a vendor or DB (N-004, E-018).
* Requirement: Specification §4 items 3 and 4 and "Implementation preservation" ("Any Plan, guide or QA-prep artifact derived from this Specification must preserve items 3 and 4"); Plan §11 (both quoted verbatim); Audit §6.
* Implications: neither condition is met at this head, so the mandatory bounded live vendor test does not attach on this evidence, and no open-rails step or exemption is required by item 4. The Guide and QA Plan must still carry both items verbatim; if QA finds new reach, they re-attach. Specification §9's separate statement that live QA is required for close stands.
* Limits: static search plus imports read; not a deployed-environment observation.
* Owner and route: Isis (QA-20), Kronos (QA-50).

**8. QA10-OBS-08 — HDE Architecture §1.1 wording (DELTA-001).**
* Observed: the canon sentence "The checked-in loader remains current repository reality until separately remediated" describes a removed module (E-012).
* Requirement: HDE Architecture §1.1 anticipates this ("this classification does not claim that relocation, caller migration, or removal has occurred"); AGENTS.md "HDE-EPIC041 current posture" tells agents the code state is current and to report the drift.
* Implications: drift of the necessary-reality-shift kind (tentative bucket). It misleads a reader who does not read AGENTS.md; QA-20 should name it so QA does not treat the canon sentence as a contract. It is not a conflict with an approved base and not a readiness gate.
* Doc delta: duplicate of DELTA-001 (Implementation Audit v1.0 §9: "after delivery and acceptance, replace 'remains current repository reality until separately remediated' with the delivered boundary"), carried in #800's description, HDE Build Notes 2.4. Drain after QA (Change Process Guide §3.5.2.8).
* Owner and route: canon owner (Product Owner), post-QA drainage.

**9. QA10-OBS-09 — HDE Mechanics Guide §1.1 wording (DELTA-002).** As #8, for "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift"; duplicate of DELTA-002, fully covering. HDE Mechanics Guide line 5697 (the HDE-EPIC030 review record) names the loader as "current-reality context" of that review; it is a dated record and needs no delta.

**10. QA10-OBS-10 — HDE State of the Repository §2.2 (new candidate DELTA-003).**
* Observed: §2.2 "Complete the separate chart-loader boundary correction" says the loader "still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging"; the module is removed (E-012).
* Requirement: none binding; HDE State of the Repository is a reference document (title class "Reference"), compared as context by Reality Audits.
* Implications: a reader of that reference would plan against a removed module. Not a gate.
* Doc delta proposed (candidate, targets only): **DELTA-003.** Target: HDE State of the Repository, §2.2. Delta: after QA, record that HDE-SEPA006's boundary correction is delivered (the Adapter entry, the pure module, the removal and its guard), or retire §2.2 as a forward-looking item. Why: §2.2 describes a module that no longer exists. Evidence: Reality Audit E-012, N-003; #796. PF proof excerpt: "The non-BodyGraph loader under `engine/charts/loader.py` still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging."
* Owner and route: Product Owner, post-QA documentation drainage.

**11. QA10-OBS-11 — PF09.3 HDE-SEPA006 status rows.**
* Observed: Task HDE-SEPA006 and Subtasks .1 to .3 read **Not done**; the Task notes describe the loader defect as current.
* Requirement: PF09.3 §0.6 lists the Done predicates; Specification §7 and §8 make no PF09 movement claim.
* Implications: the row status is accurate for now: QA, governed evidence, acceptance and closure are pending (§4). No delta is proposed before those exist.
* Owner and route: Product Owner, by an authorized post-closure PF09 update.

**12. QA10-OBS-12 — Governed evidence for HDE-EPIC041 (resolves review v1.0 N-4 for readiness).**
* Observed: no Index or Mirror row, no `audit/qa/hde-epic041/`, no doc-delta file and no close pack exist for HDE-EPIC041 (E-021).
* Requirement: PF09.3 Task HDE-SEPA006 "Required governed evidence is indexed through the existing authorized writer under HDE-Schemas and Artifacts and HDE-Mechanics Guide"; Subtask .3 "required indexing through the existing governed writer"; §0.6 "required governed evidence is complete and internally consistent"; Specification §8 ("This is a governed-evidence obligation, not a requirement"), §9 (evidence families expected at close) and §10 (close-pack and doc-delta paths); Plan §10 ("None of DL-01 to DL-03 is planned to create or change a governed evidence family"); Glow QA Guide §3.2 same-PR Index/Mirror parity; QA-20's "Required QA evidence indexing".
* Answer to N-4: the approved Plan did not require the PR units to produce a governed family, and none of their changed paths is an Index member; that is consistent with the approved base, so its absence now is not an objective failure. The governed-evidence obligation of PF09.3 lands in the QA lane (QA step logs and their indexing through `tools/evidence/update_evidence_index.py`, Step-0B doc-delta capture at the Specification §10 surfaces) and in the close mutation set (CL-05).
* Implications: Must-act-now **YES** for the dependent passes: the QA-20 Guide must name the boundary and caller-regression evidence QA has to capture and index, and QA-50 must plan it, because no earlier artifact plans it.
* Limits: none.
* Owner and route: Isis (QA-20), Kronos (QA-50), CL-05 at close.

**13. QA10-OBS-13 — `cline_skills/` and CI classification.**
* Observed: the direct commit `6a0f55f0` adds nine ZIP archives under a new root `cline_skills/`; the classifier, run as `ci.yml` runs it for that push, exits 2 with `CI_CHANGE_SURFACE_UNCLASSIFIED:cline_skills/change-flow.skill` (E-008, E-035).
* Requirement: the classifier fails closed on any path it cannot classify (`classify_ci_changes.py:1934`).
* Implications: the hosted push run on `6a0f55f0` is expected to fail at classification (not read). A pull request's classifier diffs its base and head, so a later pull request based on `6a0f55f0` or after does not carry these paths unless it changes them; the effect is bounded to that push run and any change touching `cline_skills/`. No HDE-EPIC041 surface is involved. QA should not read a red `main` push run at this head as an HDE-EPIC041 result (Plan RK-06).
* Owner and route: Product Owner (classify the prefix, relocate the files, or accept the red run).

**14. QA10-OBS-14 — GCFPE operating procedure path.**
* Observed: the register's "operating procedure" binding names `docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.1.0-20261027.md`, which `de27c356` deleted from `main` (N-007).
* Requirement: the register: "a pointer that restates no rule; the sources it names govern".
* Implications: non-decisive for this change; a reader following the binding finds no file.
* Owner and route: GCFPE management, reported for GCFPE-MGMT-10 with this prompt identity (QA-10 102726.1); no prompt or register edited here.

**15 to 17. QA10-OBS-15, -16, -17 — Audit FND-005, FND-006, FND-007 at this head.** Each persists unchanged and stays outside HDE-EPIC041 (Plan §2). Dispositions are the Audit's: CL-40 scan candidates and Product Owner decisions; FND-005 also names HDE Governance GATE:CORE-DET, D.1 and D.3 as a candidate home; FND-007 names HDE Schemas and Artifacts. OBS-D1 (the close-time architecture capture and close-PR docs sweep) stays with CL-05.

**18. QA10-OBS-18 — Repository documentation.** Matches the code on every statement checked (DOC-20 COMPLETE re-confirmed on the points in the Reality Audit). No action.

**19 to 27. Historical comparison rows.** PF23 records are dated snapshots (HDE Governance §2.0.18). The two Resolved rows are resolved by this change; the Changed, Unverifiable and Persistent rows touch no HDE-EPIC041 surface. None creates work (HDE Governance §2.0.18, "PF23 audit observation classification"). The complete fresh audit is suitable for the Product Owner's manual PF23 update, which is not a readiness gate (Glow QA Guide §3.1.1).

**28. Close-stage ordering: HDE Build Notes §2.2 R-3 against three permanent canon documents (CCR-5).**
* Observed (canon text, each read in full): HDE Build Notes §2.2 R-3 says "The close-pack writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist." Change Process Guide §3.5.1 says the close-mutation-set stage "sits between the final QA Report and the closure decision", starts from "the final QA Report with verdict `PASS`, or from a closure decision of `DO_NOT_CLOSE` whose return work is the close mutation set", and "exits to the closure decision after the Product Owner merges the close PR"; it owns "the close pack". Glow QA Guide §3.1.3: "The close mutation set is a closure prerequisite and precedes the closure decision". Plan Templates §3B states the same entries and exit for CL-05. The permanent-canon text was added on 2026-10-27 (`2d99bffc`, #762); §2.2 on 2026-10-28 (#792).
* Conflict: on the ordinary path (final QA Report PASS → CL-05), no closure decision exists yet, so R-3's "and the closure decision exist" forbids the write that the three permanent documents place before the closure decision. They agree only on the `DO_NOT_CLOSE` re-entry.
* Governing rule today: R-3. HDE Build Notes "Precedence, versioning, and scope", §1 "PF10 authority": "For any topic explicitly addressed by an applicable, active PF10 addendum, that addendum is the current authoritative source of truth and supersedes conflicting permanent PF canon until the guidance is formally reviewed and drained"; AGENTS.md "PF10's authority in the canon" says the same. R-3 explicitly addresses when the writer runs, so it governs that topic as written. QA-10 records this determination and changes nothing.
* Why it is still an entry: applied as written, R-3 reverses the CL-05 entries and exit that three permanent documents state and leaves the closure decision without the prerequisite Glow QA Guide §3.1.3 names. The 2.2 decision text records the Product Owner's direction as "the close-pack generator runs only at the end of a full work-unit cycle", without mention of the closure decision, so whether R-3's closure-decision clause states the intended order is a question only the Product Owner can answer.
* Requirement affected: Specification §10 and §6 D5 (close baseline); Plan v1.1 DL-04 (CL-05 after a QA PASS). Not R-01 to R-04 or AC-01 to AC-05.
* Implications: none for readiness, QA-20 or QA-50 (QA writes no close pack). CL-05 for HDE-EPIC041 applies R-3 as written unless the Product Owner rules otherwise first.
* Limits: QA-10 decides no canon question.
* Owner and route: Product Owner (canon owner; the 2.2 direction is his), before CL-05. Recorded as CCR-5 (§6).

## 4. PF09 row-closure facts (preserved; no row-closure review originated)

| Row | Predicate (PF09.3 §0.6 and the row text) | Targeted scope | Recorded status | Facts at `6a0f55f0` | Remaining obligations | Determination |
| :- | :- | :- | :- | :- | :- | :- |
| HDE-SEPA006 | Behavior implemented; dependencies met; tests pass on the identified state; required governed evidence complete; QA, Ops, acceptance decisions confirmed; limits disclosed; authorized PF09 update | Separate orchestration from pure Engine computation; migrate callers; retire the mixed boundary | Not done | Behavior delivered and accepted per unit (#791, #796, #800); exact-head CI passed; no governed evidence; no QA; no Ops (none planned); no acceptance or closure decision | QA verdict; governed evidence indexed; Isis closure; authorized post-closure PF09 update | Not made here |
| HDE-SEPA006.1 | As above, for Adapter-owned acquisition and pure normalization | `adapter/chart_orchestration.py`, `engine/charts/pure.py` | Not done | QA10-OBS-01, -02 | As above | Not made here |
| HDE-SEPA006.2 | As above, for supported-caller migration | C-1 to C-3; legacy retirement | Not done | QA10-OBS-03, -06 | As above | Not made here |
| HDE-SEPA006.3 | As above, plus "required indexing through the existing governed writer" | Boundary and behavior verification | Not done | QA10-OBS-05, -12 | As above, with the indexing obligation of #12 | Not made here |

## 5. Carried prior-stage items (owners unchanged)

| Item | Source | State | Owner |
| :- | :- | :- | :- |
| TI-07 / CCR-1 (acceptance map for tokenless work) | Specification §11; review v1.1 §5 | Open; a close-pack matter | CL-05; Product Owner (possible canon change) |
| TI-02; Candidate CRD Items List items 9 and 10 | Specification §11 | Open, advisory; not engaged | Product Owner |
| OBS-9 (pre-push message about `documentation_only`) | WU-PR-03 plan §16 | Open | Product Owner / CI tooling owner |
| PR35-LINK (a handoff linked the CL-30 page for PR-35) | WU-PR-03 result v1.1 | Reported | GCFPE management |
| OBS-D1 (close-PR docs sweep; architecture capture) | WU-PR-03 instruction §12 | Open; close-time | CL-05 |
| OBS-6, OBS-7, OBS-8 (`scripts/scratch.py`; classifier error order; `ruby` path) | WU-PR-02 plan §16 | Unchanged | Product Owner; record; later sessions' surface advice |
| OBS-2, OBS-5, OBS-10 (environment: `env -i`; shallow clones; the generator test needs `requirements.txt`) | Earlier plans | Unchanged | Later sessions' surface advice (QA-20 records it) |
| Review v1.1 N-5 (nit in the approved Plan) | IA-30 review v1.1 §3 | No effect | None |
| Review v1.0 N-4 (governed evidence) | IA-30 review v1.0 | Answered for readiness by #12; obligation carried to QA | Isis (QA-20); Kronos (QA-50) |
| Prompt-use repository persistence | Every record's provenance | PENDING | GCFPE management (non-gating) |

## 6. CANON_CONFLICT_REGISTER (CCR-1 to CCR-4 carried unchanged; CCR-5 proposed)

CCR-1 APPROVED (Thoth, CF-E-30 review v1.1, Ruling R-A; confirmed by Isis IA-30 v1.1): a close-pack matter for CL-05. CCR-2 APPROVED (Thoth): no effect. CCR-3 APPROVED as conditional (Thoth): not triggered (#7). CCR-4 APPROVED (Thoth): no effect. #8 to #11 are drift that canon anticipated, not a conflict with an approved base; #13 and #14 are repository and governance facts.

One new entry, proposed by this triage:

| Field | CCR-5 |
| :- | :- |
| Classification | CANON_RECONCILIATION |
| Conflicting sources, versions and clauses | HDE Build Notes v13.9.3 §2.2 R-3, first bullet ("…after the authorized QA verdict and the closure decision exist"); Change Process Guide v2.5.5 §3.5.1 "Close-mutation-set stage" ("sits between the final QA Report and the closure decision"; Entries; Exit; What it owns); Glow QA Guide v3.0.7 §3.1.3 ("The close mutation set is a closure prerequisite and precedes the closure decision"); Plan Templates v2.0.6 §3B "Entries and exit (normative)" |
| Evidence | The quoted clauses (#28); HDE Build Notes "Precedence, versioning, and scope" §1; dates: the permanent stage text landed 2026-10-27 (`2d99bffc`, #762), §2.2 on 2026-10-28 (#792) |
| Conflict statement | On the ordinary path, R-3 requires a closure decision before the close-pack writer runs; the three permanent documents place the close mutation set, which includes the close pack, before the closure decision |
| Governing rule meanwhile | R-3, as written: HDE Build Notes "Precedence, versioning, and scope" §1 (an addendum supersedes conflicting permanent canon for any topic it explicitly addresses, until drained); AGENTS.md "PF10's authority in the canon" |
| Affected requirements | Specification §10 and §6 D5; Plan v1.1 DL-04; the CL-05 stage for HDE-EPIC041. No R-01 to R-04 or AC-01 to AC-05 |
| Alternatives | (A) R-3 stands: for this change the closure decision precedes the close-pack write, and the three permanent documents are drained to match. (B) The Product Owner corrects R-3 in a later HDE Build Notes addendum so that the writer runs after the final QA Report records PASS, or after a `DO_NOT_CLOSE` decision whose return work is the set, restoring the CL-05 entries and exit |
| Recommended disposition | An explicit Product Owner ruling between (A) and (B) before CL-05 runs for HDE-EPIC041. The recorded direction ("at the end of a full work-unit cycle") and the three permanent documents read most naturally as (B); until a ruling exists, R-3 governs as written. QA-10 decides neither |
| Interim treatment | R-3 governs as written. QA-20, QA-50 and QA execution are unaffected. CL-05 applies R-3 unless the ruling exists first |
| Unresolved risk | CL-05 and the closure decision follow an order that one set of canon text forbids; a closure decision made without the close mutation set Glow QA Guide §3.1.3 calls its prerequisite |
| Permanent drainage target and owner | HDE Build Notes (a correcting addendum) under (B), or Change Process Guide §3.5.1, Glow QA Guide §3.1.3 and Plan Templates §3B under (A); Product Owner |
| Status | PROPOSED |
| Proposed by | Isis, QA-10, in this triage v1.0 |
| Reviewer and session | Not yet reviewed |
| Reviewed artifact identity and version | Not yet reviewed |
| Decision time | Not yet reviewed |
| Decision rationale | Not yet reviewed |

## 7. Nonclaims

This triage proposes and routes; it approves nothing. It is not PF10 text, a PF10 addendum, a PF23 publication, a canon change, an implementation, a QA verdict, readiness, acceptance, PF09 or board movement or closure. DELTA-003 is a candidate for its owner, and CCR-5 is a proposal awaiting the Product Owner's decision. Merging this file preserves the record and approves nothing (D21-C).
