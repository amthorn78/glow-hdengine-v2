---
artifact_type: CHANGE_AUDIT_TRIAGE
artifact_version: "1.0"
logical_id: HDE-CRD-0002-QA10-CHANGE-AUDIT-TRIAGE
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
predecessor: none
reality_audit: docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.0.md
readiness_record: docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md
producer: Isis, continuing Lead Developer and readiness decision owner (this session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
prompt: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_head_inspected: origin/main 39122b77b7f8e548e005e8bc82fabc2c6e33708b
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-10
created_at: 2026-10-23T14:30:00Z
---

# HDE-CRD-0002 — Change Audit Triage v1.0 (QA-10)

This record accounts for every finding of the Reality Audit (§12 observations RA2-01 to RA2-33, the historical comparison, and the obligations HDE Build Notes carries to QA-10 or to QA).
- **What each finding records.** Its evidence, the approved requirement or decision it relates to, its implication, the action or retained obligation, its owner and native route, and its documentation disposition.
- **What it is not.** It is not PF10 insertion text, and it makes no canon, Plan, scope or remedy decision.

## 1. Summary

| Count | Class |
| :- | :- |
| 1 | Objective failure (blocks readiness): FND-001, S22 |
| 4 | Reserved for runtime QA: FND-004 (S02), FND-007 (S06), FND-011 (S14 initiator), FND-032 (deployed-candidate re-read) |
| 3 | Carried to QA-20 and QA-50 as obligations: FND-030 (LR7-O4 close formats), FND-031 (Ops evidence path proof), FND-033 (validator install prerequisite) |
| 2 | Product Owner decisions due or carried: FND-028 (option A stop rule), FND-029 (S19-R01 to R07 dispositions) |
| 5 | Documentation deltas proposed: FND-017, FND-018, FND-019, FND-020, FND-021 |
| 6 | Later-change candidates already routed (duplicates of existing records): FND-012, FND-022, FND-023, FND-024, FND-025, FND-034 |
| 15 | Aligned or no action, with the reason: FND-002, FND-003, FND-005, FND-006, FND-008, FND-009, FND-010, FND-013, FND-014, FND-015, FND-016, FND-026, FND-027, FND-035, FND-036 |

There are 36 findings. Each has exactly one row in §2. The Reality Audit's observation IDs map to finding IDs in the table's second column.

## 2. Coverage map

Abbreviations:
- **Primary action:** OR objective repair; ER evidence recovery; LD later development or documentation; DUP fully covered duplicate; NA no action, with reason; QA reserved for runtime QA.
- **Doc disposition:** DDP doc delta proposed; NDD no doc delta needed; DUP duplicate of an existing issue; OQ open question for the Product Owner.
- **Must act now:** YES only with a current dependency.

| FND | Audit ID | Observed behaviour | Requirement or decision | Primary action | Owner and route | Doc | Must act now |
| :- | :- | :- | :- | :- | :- | :- | :- |
| FND-001 | RA2-22 | The updater admits `audit/qa/hde-crd-0002` (fixture-tested). `tests/evidence/test_evidence_index_missing_state.py::test_absent_admitted_crd_root_publishes_nothing` (:977-983), run by the evidence lane (`ci.yml:221-240`), asserts that the real root does not exist, that the loader has no current row for it, and that the Index has none. The first publication of HDE-CRD-0002 QA evidence selects the evidence lane (E-005) and fails this test | Spec S22, as §3 FND-001 quotes it | OR | Thoth through ESC-30, then ESC-40 (Isis) and a lawful delivery owner (§3) | NDD | YES |
| FND-002 | RA2-01 | Release 1.3.0, 45 members; roster equals the manifest; `release_id` 77204764… is the one production reported | Specification delta 01 C-5, C-7; Plan delta 01 P-3, P-4 | NA: aligned | — | NDD | NO |
| FND-003 | RA2-02 (unknown paths) | `adapter.factory` 404 and 405 are the governed envelope with no-store, for every path | S02 | NA: aligned; QA verifies live | Kronos (QA-50) | NDD | NO |
| FND-004 | RA2-02 (person) | `POST /api/reader` with an unknown person returns `ERR_M10_PERSON_UNRESOLVED` 404, a canon-defined envelope (HDE CLI/API/Vendor Ref §5.2.3) | S02's scope is "Unknown non-compat paths"; its acceptance intent reads "every 404" | QA: the QA Plan states which 404s S02's live step exercises | Isis (QA-20 Guide), Kronos (QA-50) | NDD | NO |
| FND-005 | RA2-03 | 0 uncovered test files; 66 recorded retirements; O-P06a-03 retired | S03 | NA: aligned. Note: 166 of 215 files run through full-validation targets, not on every PR, which is the binding definition | — | NDD | NO |
| FND-006 | RA2-04, RA2-05 | `tools/qa` owner refusal for .py/.sh/.sql; the workflow filter equals the classifier prefixes over all 8194 paths | S04, S05 | NA: aligned | — | NDD | NO |
| FND-007 | RA2-06 | The Debian setuptools compatibility shim and its five tests (E-315, E-316). The Debian build is evidenced by the WU-PR-02 local rehearsal (E-318: exit 1 before, 0 after); hosted CI uses setup-python (E-317) | S06; WU-PR-02 lineage review v2.0 ACCEPT | QA: the QA Plan decides whether to re-run the Debian reproduction | Kronos (QA-50) | NDD | NO |
| FND-008 | RA2-07 to RA2-09 | showcompat help, aux-preview `--band`, harness retirement | S07, S08, S09 | NA: aligned; S07 and S08 are functional-feature surfaces for Live QA | Kronos (QA-50) | NDD | NO |
| FND-009 | RA2-10 | Dev `GET /reader` is served only for `APP_ENV` exactly `dev` | S10 ("dev, test or local"; constraint "must not break dev, test or local use") narrowed by Plan v1.1 §15 and addenda 2.6 and 2.7 (CR-6, CR-8 APPROVED, alternative (a)) | NA: aligned with the approved Plan and canon (HDE CLI/API/Vendor Ref §5.4, §5.6; HDE Schemas & Artifacts §8.8). The Specification text is not amended; the register entries carry the decision | — | NDD | NO |
| FND-010 | RA2-11 to RA2-13 | S11 drift test (E-319, E-320); S12 labels on 27 rows over 22 paths, none stray (E-321 to E-323); S13 root-bound probe with three tests (E-324, E-325) | S11, S12, S13 | NA: aligned | — | NDD | NO |
| FND-011 | RA2-14 | `--allow-prod-vendor` follows §7.1.11a to f in code and tests. The audit actor is the effective-UID account; code cannot tell a human Product Owner from an agent | S14; Specification "Override initiator"; HDE CLI/API/Vendor Ref §7.1.11e; addendum 2.9 LR4-O2 | QA: the QA Plan's live vendor call is initiated by the authenticated human Product Owner or a delegated human executor | Kronos (QA-50); Product Owner initiates | NDD | NO |
| FND-012 | RA2-27 | showcompat/conjunction vendor acquisition (`_acquire_dry_run`) has no production-override gate | S19-R01 routed to the Product Owner with a reason (S19 review §4); §7.1.11 scopes the flag to bg:resolve | DUP of S19-R01 | Product Owner | DUP | NO |
| FND-013 | RA2-15 | 18 catalog rows; 53 served pairs fully accounted for; retired `/ops/*` routes stay registered and answer as unknown paths in a prod posture | S15 under addendum 2.7 AD-1 | NA: aligned | — | NDD | NO |
| FND-014 | RA2-16, RA2-17 | `GEO_API_KEY` present; readiness and port statements match the code | S16, S17 | NA: aligned | — | NDD | NO |
| FND-015 | RA2-18 | `invalid_json`, `-> bytes` and the mounts are stated correctly | S18 | NA: aligned | — | NDD | NO |
| FND-016 | RA2-19 | S19 record: 9 fixed (each fix present on `main`, E-341), 7 routed | S19 | NA for the record (see FND-029 for the routed items) | — | NDD | NO |
| FND-017 | RA2-23 | `docs/ADAPTER_009.md` stale lines :49, :189-193, :223, :209 | Operative documentation; WU-DOC-01's purpose (Plan v1.1 §7) is "Bring the operative repository documents to the delivered state". These lines predate HDE-CRD-0002 and are outside WU-DOC-01's listed statements | LD | Product Owner, as a later documentation change | DDP: `docs/ADAPTER_009.md` (six-key body; remove "New"; override in every environment) | NO |
| FND-018 | RA2-24 | `ARCHITECTURE.md` :10, :25 (`dumps` alias), :35 (compat GET "ids-only"), no mention of the S19 production posture | Operative documentation | LD | Product Owner, as a later documentation change | DDP: `ARCHITECTURE.md` | NO |
| FND-019 | RA2-25 | `docs/contracts/reader_v2_public_bytes.md:8` and AGENTS.md "HDE-EPIC040 current posture" ("PF10 records them") are stale against current canon | Operative documentation; AGENTS.md needs the Product Owner's explicit instruction | LD | Product Owner | DDP: `docs/contracts/reader_v2_public_bytes.md`; `AGENTS.md` (Product Owner instruction required) | NO |
| FND-020 | RA2-21 | The ADR's "Stated limits" still carry "and `SATISFIED` needs every recorded status to be `PASS`" | Addendum 2.17 Resolution A and its drainage table ("when the ADR is next revised") | LD | Product Owner (the ADR owner), at the next revision | DDP: `docs/adr/hde/close_pack_writer_adr.md` | NO |
| FND-021 | (historical RA-18) | C040-06/07/08 content is in PF04, PF05 and PF12; PF10 carries none; PF01 has no C040 hit; completeness not established | Canon drainage (HDE-EPIC040) | LD | Product Owner, canon maintenance | OQ: whether C040 drainage into PF01 §§6.1–6.2 is complete | NO |
| FND-022 | RA2-26 | `adapter.http_reader.create_app` after_request never fires | Addendum 2.7 AD-4 item 4 (routed to S19; not taken up) | DUP: carried later-change candidate | Product Owner | DUP | NO |
| FND-023 | RA2-28 | The env guard sees `app.config` | Addendum 2.21 LR8-F1 | DUP | Product Owner | DUP | NO |
| FND-024 | RA2-29 | `test_prepush_check.py` raced git auto-maintenance once on hosted CI (proposed untested patch `-c maintenance.auto=false`) | Addendum 2.21 PR35-C1 | DUP: later-change candidate. QA risk: an intermittent red changed-tests step on a QA evidence PR that changes no prepush file. Recorded here so the QA Plan's CI expectations name it | Product Owner | DUP | NO |
| FND-025 | RA2-30 | Two read-only validators need Flask (the runtime install) | AGENTS.md validation lists; PF19 harness prerequisites | DUP of FND-033's obligation | Isis (QA-20), Kronos (QA-50) | NDD | NO |
| FND-026 | RA2-32 | Packaging covers 29 of 45 release members | Specification delta 01 C-6 (stated limit; README.md:138) | NA: stated limit | — | NDD | NO |
| FND-027 | RA2-33 and historical RA-16, RA-13, FND-012 | Root hygiene, " (1)" skill file names, em-dash path, pytest.ini scope, Python `.sh` validator | Not in HDE-CRD-0002's scope (Spec "Not reopened": RA-16 and others) | NA: outside scope; persistent | Product Owner, if ever | NDD | NO |
| FND-028 | — | Option A stop rule (WU-PR-07 decision record §3; addendum 2.16): no PR-40 review of WU-PR-07, WU-PR-08 or WU-DOC-01 recorded a hosted CI failure a local replay would have caught. WU-PR-07: none (addendum 2.16). WU-PR-08: the one failure (E-007, PR35-C1) was an intermittent race on code that passed on two other runs, not recorded as replay-catchable. WU-DOC-01 v1.0, v2.0, v3.0: no hosted failure | Stop rule: "If none is recorded by HDE-CRD-0002's QA-10 readiness stage, the replay report is removed in a later change"; addendum 2.16: "that is the Product Owner's decision at QA-10" | The record is complete here. The removal is a later change, and the decision is the Product Owner's | Product Owner | OQ: confirm removal of the replay report in a later change | NO |
| FND-029 | RA2-19 | S19-R01 to R07 are routed to the Product Owner with reasons; no Product Owner disposition of them was found | S19 ("routed to an owner with a reason" is met) | NA for S19. Open Product Owner items | Product Owner | OQ | NO |
| FND-030 | RA2-21 | No close pack exists. Addendum 2.16 LR7-O4: at T1 the close needs the QA plan as `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v<N>.<N>.md` with `### CHECK <n>` headings and `Surface / D-goal mapping:` lines naming all 22 S-IDs, and the QA report as `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v<N>.<N>.md` with `artifact_type: QA_REPORT`, `change_id` and `verdict: PASS`. Spec delta 01 removed S01, so 21 S-IDs remain in scope; how the mapping names S01 is a QA-50 design point | Addendum 2.16 "LR7-O4 carried to QA-10 readiness" | Obligation carried to QA-20 and QA-50 | Isis (QA-20), Kronos (QA-50) | NDD | NO |
| FND-031 | RA2-31 | WU-OPS-01 evidence carries a SHA-256 ledger only; CR-9 PROPOSED | Glow QA Guide §11.1 (the consuming QA check carries the path proof); CR-9 | Obligation carried to QA-50; CR-9 disposition at its native boundary | Kronos (QA-50) for the consuming check; Isis for CR-9 | NDD | NO |
| FND-032 | — | Production reported `release_id` 77204764… at 2026-10-23T13:30:06Z (one read) | Plan v1.1 §9 item 3; Glow QA Guide §3.5.5 | QA: the live steps re-read `/internal/version` | Kronos (QA-50) | NDD | NO |
| FND-033 | RA2-30 | QA execution of read-only validators needs CI's full install | AGENTS.md "Pytest readiness rule" | Obligation carried to QA-20 | Isis (QA-20) | NDD | NO |
| FND-034 | — | The closeout-validation job's first hosted run is due at HDE-CRD-0002's T7 | Addendum 2.13 "Unresolved, with owners" | DUP: carried to the close | HDE-CRD-0002 close mutation set; the Product Owner dispatches | DUP | NO |
| FND-035 | historical RA-17, FND-017, FND-019, FND-024, FND-025, RA-05, RA-07, RA-08, RA-12, RA-14 | Resolved since `39b9cdf` | PF23 comparison | NA: resolved | — | NDD | NO |
| FND-036 | historical RA-01 to RA-04, RA-06, RA-09 to RA-11, RA-15, RA-18, FND-001 to FND-016, FND-018, FND-020 to FND-023 | Persistent, changed or not re-checked, as the audit table states | PF23 comparison | NA: no HDE-CRD-0002 obligation; RA-10, RA-11 and RA-15 are listed as not reopened in the Specification | — | NDD | NO |

## 3. FND-001 in detail (the readiness blocker)

**What the approved sources require:**
- **Specification v1.1, S22 acceptance intent:** "Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate".
- **Constraints, "QA evidence admission":** "S22 completes before HDE-CRD-0002 enters QA".
- **Canon, QA & Build Notes posture, "QA requirement":** "QA evidence lives under `audit/qa/hde-crd-0002/` … and is published by the canonical updater once S22 holds".
- **Plan v1.1 §7 WU-PR-02, Purpose:** "admit HDE-CRD-0002's QA root to the canonical evidence graph before QA".

**Expected outcome.** QA evidence for HDE-CRD-0002 can be published by the canonical updater under `audit/qa/hde-crd-0002/`, and the published state validates, including under the repository's evidence-lane validation.

**Observed evidence:**
- **E-326:** the updater's `ADMITTED_CRD_QA` admits the root. **E-327:** a fixture test publishes it beside HDE-CRD-0001 and validates both.
- **E-328:** the same test file holds `test_absent_admitted_crd_root_publishes_nothing`. With no condition, it asserts:
  - `not (ROOT / "audit/qa/hde-crd-0002").exists()`;
  - no `_load_crd_qa_entries([])` current row containing `hde-crd-0002`;
  - no Index row under `audit/qa/hde-crd-0002`.
- **E-005:** the evidence lane runs that file (`ci.yml:221-240`). A change adding `audit/qa/hde-crd-0002/` files and their Index rows selects the evidence lane.
- **E-006:** the test implements Plan v1.1 WU-PR-02 acceptance (5), "the absent real root publishes nothing", which held when WU-PR-02 delivered it. No record addresses its behaviour once QA creates the root (N-002).

**Exact shortfall.** On `main`, the publication of HDE-CRD-0002 QA evidence produces a repository state that the repository's own evidence-integrity lane rejects. The objective that QA evidence is "published by the canonical updater" and "validates" under that root is therefore not achieved for the real root. This holds deterministically: the first assertion fails the moment the directory exists.

**Why it is a failure and not a drift observation:**
- The input is real: the QA evidence of this change (HDE Build Notes addendum 2.11 rule 4(a) and (b); the hosted CI runner).
- The failure blocks a named dependency: QA-50's evidence publication and Kronos's QA checks, and later the close-run family under `audit/qa/hde-crd-0002/close/`, which also lies under the root.

**Affected dependency.** Every QA evidence publication for HDE-CRD-0002 (QA-50 onward), and the close-run family (S21, T-stage close).

**Required resolution evidence:**
- **(1) The updated test on `main`.** A change on `main` in which the evidence-lane tests no longer require the real root to be absent, while still proving what acceptance (5) protected: that an absent admitted root publishes nothing, for example in a fixture repository. The remedy's form is ESC-30's to propose; this record does not design it.
- **(2) Hosted evidence of the fix.** CI on that change: the evidence lane green with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **(3) A demonstration with the root present.** A test or rehearsal showing the evidence lane passes with an `audit/qa/hde-crd-0002/` family present, in a fixture or throwaway clone, with no real QA evidence fabricated.

**Owner and route:**
- **Diagnosis and proposal:** continuing Thoth, ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1.
- **Remedy review:** Isis, ESC-40.
- **Delivery:** a lawful prospective PR owner. WU-PR-02 is accepted-final and is not reopened.
- **Return:** the same Isis QA-10 for reassessment of S22 and its dependants.

**Not affected:**
- The other 20 in-scope requirements.
- WU-PR-02's other deliverables (S06, S11, S12, S13).
- The updater's admission logic itself.

## 4. Requirement reconciliation

| Req | Unit | Status | Evidence | Reserved for QA |
| :- | :- | :- | :- | :- |
| S01 | — | Removed by Specification delta 01 (C-1, C-6); not delivered; stated limit FND-026 | E-436 | — |
| S02 | WU-PR-03 | Achieved | E-216 to E-219; tests in `tests/http/test_endpoint_catalog.py` | Live step (FND-003, FND-004) |
| S03 | WU-PR-01 | Achieved | E-126 to E-130 | — |
| S04 | WU-PR-01 | Achieved | E-124, E-131, E-132 | — |
| S05 | WU-PR-01 | Achieved | E-119, E-133, E-134 | — |
| S06 | WU-PR-02 | Achieved (recorded Debian rehearsal; hosted non-Debian success) | E-315 to E-318, E-003 | Optional re-run (FND-007) |
| S07 | WU-PR-03 | Achieved | E-256 | Live step (functional-feature class) |
| S08 | WU-PR-04 | Achieved | E-266 | Live step |
| S09 | WU-PR-03 | Achieved (retired) | E-104, E-294, E-295 | — |
| S10 | WU-PR-03 | Achieved as approved (explicit `dev`) | E-226, E-227 | Live step (refusal in the deployed target) |
| S11 | WU-PR-02 | Achieved | E-319, E-320 | — |
| S12 | WU-PR-02 | Achieved | E-321 to E-323 | — |
| S13 | WU-PR-02 | Achieved | E-324, E-325 | — |
| S14 | WU-PR-04 | Achieved in code and tests; initiator reserved | E-261 to E-263, E-275 to E-288 | Mandatory live vendor call (FND-011) |
| S15 | WU-PR-03 | Achieved under AD-1 | E-246, E-247 | Catalog entries only |
| S16 | WU-PR-08 | Achieved | E-401, E-402 | — |
| S17 | WU-PR-08 | Achieved | E-403 to E-417 | — |
| S18 | WU-PR-03 | Achieved | E-418 to E-423 | — |
| S19 | WU-PR-05 | Achieved as a record; fixes present | E-340, E-341 | Fixed surfaces inherit their class |
| S20 | WU-PR-06 | Achieved | E-135 to E-140 | — |
| S21 | WU-PR-07 | Achieved in code, tests and ADR approval; no close run yet | E-329 to E-339 | Close formats (FND-030) |
| S22 | WU-PR-02 | **Shortfall (FND-001)** | E-326 to E-328, E-005, E-006 | — |

## Canon relied on

| Decision topic | Governing sections |
| :- | :- |
| Triage form, dispositions, routing | QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, "Execute" §3 and §4, "Task-specific conflict and output duties", read in full; PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.1 (triage purpose and assessment states). The prompt's rule that the triage is never PF10 insertion text governs over PF19's "PF10-addendum-ready" description for this record |
| FND-001 objective | Specification v1.1-approved S22 row, "Constraints: QA evidence admission", "Canon, QA & Build Notes posture: QA requirement"; Plan v1.1 §7 WU-PR-02 (Purpose; Acceptance (5)) |
| Real inputs | PF10-HDE-Build-Notes v13.7.5 addendum 2.11 rule 4 (read in full) |
| S10 narrowing | PF10 addenda 2.6 and 2.7 (CR-6, CR-8); Plan v1.1 §15 |
| S15 catalog posture | PF10 addendum 2.7 AD-1 |
| S14 clauses and the initiator | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11a–f; PF10 addendum 2.9 (LR4-O2) |
| Routed items | PF10 addenda 2.7 (AD-4), 2.10 (S19-R01 to R07), 2.13, 2.16 (LR7-O4; option A), 2.21 (PR35-C1, LR8-F1, LR8-F2, LR8-O1), 2.22 (CR-9; FND-001 to FND-004 of the receipt) |
| Ops evidence path proofs | PF19-Canon-Glow-QA-Guide v3.0.6 §11.1, as quoted in the CR-9 entry (`docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13) |
| Stated limit (packaging) | Specification delta 01 C-6; PF10 addendum 2.20 |
| Historical comparison | PF23-Canon-Reality-Audits v1.2.2, read in full |
