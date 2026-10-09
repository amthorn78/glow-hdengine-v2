# PF09.3 from v1.1.5 — exact redlines

Run identity: `GTWPE-20261009-PF10-v13.5-T-PF09-3`. Assigned ledger row: `T-PF09-3`.

Preparation outcome: `READY`. Save completeness is recorded in the separate proof log after complete saved-pair readback.

Originating preparer: Codex `/root`, this Nathan-started document session in `/workspace/scratch/d3c88a3f81ed`; no platform conversation ID is exposed. Correction returns to this same preparer and run, under TW-DRAIN-20 100926.1.

Prompt: TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862.

Original: `amthorn78/glow-hdengine-v2` / `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`, native UTF-8 Git blob at `e7265a090ad0cc8de5f36de2f19481216aa3d073`, v1.1.5; 71,280 bytes; SHA-256 `0e3415e62e92f9d18c0d6ac1e513c1d8999efcacf2f71f4e1bda495fdbadec65`; Git blob `593c06bb6ae889ebb39f1f5c1f32231838d71eec`.

Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md` at `f057d124176143b3e02ba7ad599880fd7e9991b1`. Destination: `docs/20261009-gtwpe-pf10-v13-5`, shared draft PR #596 while open. The predeclared documents continuation applies only if #596 has merged.

Source order for Apply: `PF10-HDE-Build-Notes-v13.5.md` (v13.5, selected A units); `HDE-EPIC040-specification-v1.1-approved.md` (v1.1, complete S01–S13); `HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` (C1, complete controlling); `HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` (C0, complete reading, retained history only where C1 preserves it). All repository inputs are bound to `e7265a090ad0cc8de5f36de2f19481216aa3d073`. Exact selections, roles, holds, and per-operation basis are in `redlines-PF09.3-from-v1.1.5.proof-log.md`.

The native header is reserved for TW-APPLY-10: Version v1.1.5, Status Canon, Effective date 2026-09-09, Last Update Gate PF10 13.0.9; title and invocation tag stay unchanged. No native change/revision log requires a content entry. All three edits below resolve independently against this unchanged original; offsets are evidence in the proof log, never locators. Literal payloads include every LF before their closing fence.

## Redline RL001

**Classification:** Status Update; Notes Update; Phase Master accounting

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**`

**Original location:** The HDE-SEPA005 bullet in the phase Notes, before Task HDE-SEPA001.

**Expected occurrence:** 1 exact old block in the stated original section; 1 in the whole original.

**Old text:**
``````text
* HDE-SEPA005 remains **Partial**: HDE-SEPA005.1 and HDE-SEPA005.2 remain **Partial**, and HDE-SEPA005.3 through HDE-SEPA005.5 remain **Not done**.  
``````

**Replacement text:**
``````text
* HDE-SEPA005 remains **Partial**: HDE-SEPA005.1 through HDE-SEPA005.4 are **Done**, and HDE-SEPA005.5 is **Partial**. The deferred live current-row Gate-readiness observation still needs re-homing by the PF09 owner; QA50-F01 is resolved.  
``````

**Basis:** Conform the phase summary to independently assessed subtask states: .1–.4 Done, .5 and parent Partial. QA50-F01 is resolved; live-readiness re-homing is not. Keep the phase master status Not Done and all unrelated work untouched. Source-ledger references: A02, A04, A37; S02, S06, S11; C1 §§0–4, 6; C0 §15 as retained by C1.

## Redline RL002

**Classification:** Status Update; Notes Update; Evidence Update; Epic-information Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA005 — Production Magic10 mechanics configuration contract**`

**Original location:** The complete Task HDE-SEPA005 section, including all five nested subtasks and its trailing separator, ending immediately before Task HDE-SEPA006.

**Expected occurrence:** 1 exact old block in the stated original section; 1 in the whole original.

**Old text:**
``````text
## **Task HDE-SEPA005 — Production Magic10 mechanics configuration contract**

**Task ID:** HDE-SEPA005

**Task name/label:** Production Magic10 mechanics configuration contract

**Task description:**  
Implement the exact Separation code, configuration, tooling, tests, and evidence required to produce the corrected Channel catalog, strict adopted mechanics configuration, fail-closed loader, deterministic configuration identity and comparison tooling, and governed implementation proofs.

**Task status:** **Partial**

### **Subtask HDE-SEPA005.1 — Corrected canonical 36-Channel catalog**

**Subtask ID:** HDE-SEPA005.1

**Subtask name/label:** Corrected canonical 36-Channel catalog

**Subtask description:**  
Correct all circuit/substream rows, ascending Gate pairs, Center-set projection, schema, and row order while preserving non-scoring Product metadata and existing FE/BE bundle compatibility.

**Subtask status:** **Partial**

### **Subtask HDE-SEPA005.2 — Magic10 mechanics schema and default configuration**

**Subtask ID:** HDE-SEPA005.2

**Subtask name/label:** Magic10 mechanics schema and default configuration

**Subtask description:**  
Implement the complete twenty-signal map, response profiles, Balance operations, caps closure, source hashes, result schemas, and strict configuration schema.

**Subtask status:** **Partial**

### **Subtask HDE-SEPA005.3 — Fail-closed mechanics configuration loader**

**Subtask ID:** HDE-SEPA005.3

**Subtask name/label:** Fail-closed mechanics configuration loader

**Subtask description:**  
Implement one immutable typed bundle loaded outside Engine Core, exact source/hash closure, Gate normalization, result-schema validation, and one active configuration per release.

**Subtask status:** **Not done**

### **Subtask HDE-SEPA005.4 — Mechanics configuration identity and deterministic comparison**

**Subtask ID:** HDE-SEPA005.4

**Subtask name/label:** Mechanics configuration identity and deterministic comparison

**Subtask description:**  
Implement canonical configuration and source-bundle hashes, exact golden-output comparison, and an explicit guarantee that comparison cannot change the active production configuration.

**Subtask status:** **Not done**

### **Subtask HDE-SEPA005.5 — Separation implementation tests and governed artifacts**

**Subtask ID:** HDE-SEPA005.5

**Subtask name/label:** Separation implementation tests and governed artifacts

**Subtask description:**  
Implement the schema mutation matrix, Gate-ingress rejection, canonical-byte checks, catalog/caps/threshold closure, read-only current-row Gate-readiness command, and indexed evidence.

**Subtask status:** **Not done**

---

``````

**Replacement text:**
``````text
## **Task HDE-SEPA005 — Production Magic10 mechanics configuration contract**

**Task ID:** HDE-SEPA005

**Task name/label:** Production Magic10 mechanics configuration contract

**Task description:**  
Implement the exact Separation code, configuration, tooling, tests, and evidence required to produce the corrected Channel catalog, strict adopted mechanics configuration, fail-closed loader, deterministic configuration identity and comparison tooling, and governed implementation proofs.

**Task status:** **Partial**

**Epic or card:** **HDE-EPIC040 — Separation Pass 3**. The selected scope is this parent and HDE-SEPA005.1 through HDE-SEPA005.5. HDE-SEPA001 through HDE-SEPA004 and their subtasks remain the twenty-nine excluded Done/context units. C040-01 is resolved; the old Notes inconsistency does not reopen them. HDE-SEPA006 is separate planned Separation work and is outside HDE-EPIC040.

**Task notes:**

* HDE-SEPA005.1 through HDE-SEPA005.4 are **Done** for their stated implementation and evidence scope. HDE-SEPA005.5 is **Partial**, so this parent remains **Partial** under this document's completion standard. QA50-F01 is resolved; the remaining .5 condition is the PF09 owner's re-homing of the deferred live current-row Gate-readiness observation. Neither epic closure nor the completed offline command makes that live observation complete.
* The approved Specification v1.1 remains the scope baseline, with the adopted decisions recorded in HDE Build Notes. C040-06 supplies the corrected Channel taxonomy and existing-state conformance, without a new scoring formula. C040-05 preserves the pure four-argument Core boundary. C040-07's approved Reader v2 delivery supersedes the original public ten-category exclusion only for that surface; Reader v1 remains supported and public results remain bands-only and numeric-free. C040-08 aligns the Reader v1 error schema with the emitted governed four-key envelope without changing response bytes. These decisions do not create a second configuration, calculator, presenter, schema authority, or evidence index.
* HDE-EPIC040 reached `CLOSE / CHANGE_CLOSED` by Product Owner-authorized exceptional closure at 2026-09-29T19:53:33Z. The controlling record is `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`. All nine implementation/documentation PR units were accepted and merged: PR01 #403, PR02 #404, PR03 #405, PR04 #467, PR05 #492, PR06 #501, PR06a #508, PR06b #513, and PR07 #518. OPS01 has a separate PASS result and ACCEPT receipt; DOC-20 is COMPLETE. PR07's documentation-only CI is not behavior proof.
* Whole-change QA is **PASS** for the approved QA Plan v1.2 run: twelve checks executed and accepted at tested source `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`. The recorded admitted release is `1.3.0`, with 45 members and `release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`. The release identity, implementation acceptance, OPS result, QA verdict, evidence registration, and exceptional closure retain their separate proof functions.
* The two environment-blocked live requirements remain deferred: live, read-only Gate readiness against current rows is accounted under .5; live DB Reader v1/v2 success over live HTTP remains a PF09 gap noted at this parent. They require a future epic with the App user model, under its own approved Specification and QA Plan, through the HDE-EPIC040 CL-40 gap scan. No future task ID, epic, phase, or completed live result is assigned here. The `--allow-prod-vendor` gap remains with the PF05 and CLI owners through change control, outside HDE-EPIC040.
* QA planning for this production-functional scope must include the live vendor call required by HDE Build Notes, using synthetic data under open rails; closed fixtures, a database read, or an exemption do not substitute. The recorded T11 proof consists of two Product Owner-directed, vendor-backed CLI invocations (AB and BA), with configuration from the execution environment: `HD_API_KEY`, `GEO_API_KEY`, and `HD_API_BASE_URL`, or the supported `HDAPI_BASE_URL` alias subject to conflict rejection. This records that bounded proof and its authority; it grants no new vendor execution. T11 proves release-bound Magic10 output and a bands-only Reader v1 dump, not live DB readiness, Reader v2 HTTP success, a deployed service, rate-limit handling, or full vendor conformance.
* Exceptional closure does not establish ordinary Close Gate completion. The close report, close manifest, close-pack path proofs, drain-targets ledger, governed close-pack placement of the QA RCA summary, and same-run close-workflow evidence were absent and excepted within that closure's stated scope. No close-report SATISFIED posture, token satisfaction, board movement, phase exit, deployment, or release activation follows. This task's remaining work does not reopen HDE-EPIC040.
* Carried packaging, HTTP, CLI, evidence-owner, and repository limitations retain their recorded owners. In particular, wheel installs omit required release members; HTML 404 remains on the recorded non-compat factory paths; the CLI proof test and out-of-lane failures remain baseline; engine-core currency testing and Mirror origin labels remain evidence-owner work. The bounded security QA checks do not supply the missing implementation-delta code security review. Stronger atomicity and capture re-identification promises were not adopted. These limits do not reopen unrelated Done rows or become new tasks by this record.

**Evidence / artifacts:**

* `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` supplies the approved six-unit scope and the preserved exclusions. HDE Build Notes supplies the adopted decisions, accepted PR lineage, bounded OPS and QA records, and the later-drain recommendations. `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` retains the delivery, retrospective, Strategy Card, conflict-register, and row recommendation history only where the controlling v1.2 record preserves it.
* `docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md` and the separate `docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md` identify the approved run, criteria, attempts, and limits. The evidence of record is Run B at `787bb97b58b638d6b307cad6d76484c883c58aec`. PR #559 landed its QA root on main as `74f6cc96`, with tree `b7c72a364fd8b6ce8cf2a92c1068b6ded12ff2c8`, byte-identical to that stream. The 39-file QA root and the 41 stored paths under `audit/` are different counts: the latter also includes `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof outside the QA root.
* QA50-F01 is **resolved** by #559: fourteen files are registered through the existing evidence updater, Human Evidence Index, and Machine Mirror—the manifest, twelve primary logs, and `audit/docdeltas/hde-epic040_doc_deltas.md`. Index and Mirror grew from 606 to 620 records. The supplementary QA files and `00_meta/doc_deltas.md` landed but were not registered. The manifest ledger-coverage lookup now holds; registration is evidence-owner work, not another QA execution.
* The canonical QA manifest is `audit/qa/hde-epic040/qa_step_logs_manifest.json`. Its twelve primary logs are under `audit/qa/hde-epic040/checks/`, with the manifest, logs, doc-delta surfaces, and their recorded path proofs reconciled by T12. Run A at `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c` remains a preserved, non-canonical execution record and must not be merged as the QA root. Its untraced T03 outcome and missing T10 receipt remain unknown; no reconstruction or rerun is claimed.

### **Subtask HDE-SEPA005.1 — Corrected canonical 36-Channel catalog**

**Subtask ID:** HDE-SEPA005.1

**Subtask name/label:** Corrected canonical 36-Channel catalog

**Subtask description:**  
Correct all circuit/substream rows, ascending Gate pairs, Center-set projection, schema, and row order while preserving non-scoring Product metadata and existing FE/BE bundle compatibility.

**Subtask status:** **Done**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis:**  
C040-06's adopted 36-row catalog and 16-case existing-state conformance were delivered through accepted PR01 and the dependent configuration/core work. All Gate pairs are ascending and unique; circuit/substream and Center projection follow the adopted single-home contracts; non-scoring metadata and FE/BE bundle compatibility are preserved. QA check T04 (`ac040-02-03-catalog-config`) passed group A (304 tests) and its 36-row K1 predicate. T03 revalidated the owner-generated catalog evidence, including `catalog.catalog_schema_validation` and `catalog.domain_closure_report`. The completion basis combines those tests and governed artifacts with the separate acceptance and closure records above; it is not an external-consumer test or a new catalog authority.

**Evidence / artifacts:**  
`catalog/channels_v1.json`; the owner-generated catalog, registry, and bundle evidence; `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`; and `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log`, in the registered Run B stream. No remaining row-specific completion gap is recorded.

### **Subtask HDE-SEPA005.2 — Magic10 mechanics schema and default configuration**

**Subtask ID:** HDE-SEPA005.2

**Subtask name/label:** Magic10 mechanics schema and default configuration

**Subtask description:**  
Implement the complete twenty-signal map, response profiles, Balance operations, caps closure, source hashes, result schemas, and strict configuration schema.

**Subtask status:** **Done**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis:**  
Accepted PR01 and its dependent Core/consumer deliveries implement the strict adopted default `m10-channel-state-v1.0.0`: twenty signals, the activation/coherence/expression response profiles, ten category weights, eighteen weighted-state operations, and the two Balance operations `twice_min_owner_mass_v1` and `companionship_em_mass_v1`. QA T04's K2 predicate and group A establish configuration structure; the group tests and PR evidence establish caps closure, source/hash closure, and strict configuration/result-schema validation. T11's vendor-backed result independently carries the same configuration ID, twenty signals, and ten categories. No preset, retuning, hidden selector, or alternative formula is adopted, and a structural K2 check alone is not the whole completion proof.

**Evidence / artifacts:**  
`catalog/magic10_mechanics_v1.json`; its strict configuration and result-schema evidence through the owning writers; `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`; and `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`. No remaining row-specific completion gap is recorded.

### **Subtask HDE-SEPA005.3 — Fail-closed mechanics configuration loader**

**Subtask ID:** HDE-SEPA005.3

**Subtask name/label:** Fail-closed mechanics configuration loader

**Subtask description:**  
Implement one immutable typed bundle loaded outside Engine Core, exact source/hash closure, Gate normalization, result-schema validation, and one active configuration per release.

**Subtask status:** **Done**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis:**  
Accepted PR02, PR03, PR04, and PR06 deliver the deeply immutable admitted bundle, schema-bound Gate ingress and normalization, exact release-member/hash closure, result validation, and fail-closed refusal behavior. Source execution coherence covers the eight selected loader/serializer/support/Core/calculator modules through the adopted captured-compilation comparison; it is not a historical raw-byte or arbitrary tamper-proof guarantee. Engine Core remains pure and receives its bundle and release identity as explicit arguments, with loading and file access outside Core. QA T05 (`ac040-04-05-admission-identity`, 371 tests), T07, and T08 support the required boundary; T01 records admission of the complete pinned release and T09 exercises the admission refusal. The earlier release-not-admitted interval ended with PR06 and is retained only as delivery history. No stronger multi-file crash-atomicity, cross-process admission, or wheel-distribution promise is inferred.

**Evidence / artifacts:**  
`engine/config/registry_loader.py`; `catalog/manifest.json`; the owning loader, Core, release-admission, execution-coherence, and result-schema evidence; and Run B primary logs for `ac040-04-05-admission-identity`, `ac040-07-gate-ingress-offline`, `ac040-04-09-compat-cli-offline`, and `ac040-09-reader-http-in-process`. No remaining row-specific completion gap is recorded for the supported source-tree release.

### **Subtask HDE-SEPA005.4 — Mechanics configuration identity and deterministic comparison**

**Subtask ID:** HDE-SEPA005.4

**Subtask name/label:** Mechanics configuration identity and deterministic comparison

**Subtask description:**  
Implement canonical configuration and source-bundle hashes, exact golden-output comparison, and an explicit guarantee that comparison cannot change the active production configuration.

**Subtask status:** **Done**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis:**  
Accepted PR02, PR03, PR05, and PR06 deliver canonical configuration/source identity and the exact, read-only comparison. QA T05 binds the 45-member manifest and release identity. T06 (`ac040-06-golden-comparison`, group C, 153 tests) records all eight cases M10-G001 through M10-G008 matching at the repository root, byte-identical repeat reports, a one-leaf altered fixture reported only as M10-G001 mismatches, and an unchanged tree digest. Comparison neither selects nor mutates active production configuration. AB/BA identity is corroborated by the applicable Core/CLI groups and T11. OPS01's accepted attestation and adverse refusals are separate corroboration; QA did not rebuild the attestation. Frozen historical captures are not current release identity, and no comparison at an untested candidate root is claimed.

**Evidence / artifacts:**  
`catalog/manifest.json`; the owning configuration and source-hash artifacts; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log` and its match/mismatch captures; `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log`; and the separately accepted evidence under `audit/ops/hde-epic040/ops01/`. No remaining row-specific completion gap is recorded.

### **Subtask HDE-SEPA005.5 — Separation implementation tests and governed artifacts**

**Subtask ID:** HDE-SEPA005.5

**Subtask name/label:** Separation implementation tests and governed artifacts

**Subtask description:**  
Implement the schema mutation matrix, Gate-ingress rejection, canonical-byte checks, catalog/caps/threshold closure, read-only current-row Gate-readiness command, and indexed evidence.

**Subtask status:** **Partial**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis and remaining gap:**

* The schema mutation matrix, Gate-ingress rejection, canonical bytes, catalog/caps/threshold closure, and read-only readiness command are implemented and proven by the selected PR and QA records. T03's nine read-only evidence validators and group G (587 tests), T04, T06, and T07 cover the relevant proof burden. T07 (`ac040-07-gate-ingress-offline`, 191 tests) proves the command's real-entrypoint refusals: `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, and `READINESS_UNAVAILABLE`, each exit 5 with empty stdout. Unavailable input is never reported ready; the command makes no SQL write. Synthetic fixtures prove fixture behavior only.
* The indexed-evidence condition is established: QA50-F01 landed through #559, including the QA manifest's registration and ledger-coverage lookup. The older QA-120 and closure v1.0 references to missing Index/Mirror registration and evidence absent from main are superseded by the controlling closure v1.2 record. Indexing is no longer a .5 completion gap.
* The live, read-only observation against current user-bound rows remains unproved and its PF09 re-homing remains unresolved. The App user model and persistent user-bound BodyGraphs were unavailable to this QA; no live command ran and no live proof is claimed. This row stays **Partial** until its actual PF09 owner resolves that remaining obligation through the separately authorized maintenance/gap route. The alternative reading that excludes the live observation from this row has not been selected.
* DEFERRED → HDE-EPIC040 CL-40 gap scan / future epic with the App user model — live current-row Gate readiness was blocked by the environment and must be planned under that future epic's approved Specification and QA Plan; not a close blocker for HDE-EPIC040. This reference allocates no new row or future epic ID and does not itself perform the re-homing.

**Evidence / artifacts:**  
The registered `audit/qa/hde-epic040/qa_step_logs_manifest.json`, twelve primary logs, and `audit/docdeltas/hde-epic040_doc_deltas.md`; the corresponding existing Index/Mirror registration; Run B primary logs for `ac040-08-evidence-validators`, `ac040-02-03-catalog-config`, `ac040-06-golden-comparison`, `ac040-07-gate-ingress-offline`, and `qa-closeout-deliverables`; and the controlling closure v1.2 record. These artifacts establish the stated offline behavior and evidence integrity, not a live current-row observation.

---

``````

**Basis:** Use the actual PF09.3 §0.3/§0.6 completion standard for every selected row. Combine delivered scope, accepted PR lineage, distinct OPS/QA records, and C1’s resolved evidence registration. Record .1–.4 Done with row-specific proof, .5 Partial with its sole remaining live-readiness re-homing condition, parent Partial with the separate live Reader gap. Add exact Epic information and evidence limits without changing the six-unit scope, creating rows, or promoting held proposals. Source-ledger references: A02–A07, A09–A13, A15–A28, A32–A37; S01–S13; C1 complete (controlling); C0 §§3–7, 10–15 only as retained and updated by C1.

## Redline RL003

**Classification:** Clarity Fix; citation-only Notes Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction**`

**Original location:** The first Task notes bullet naming HDE-Build Notes Addendum 2.17.

**Expected occurrence:** 1 exact old block in the stated original section; 1 in the whole original.

**Old text:**
``````text
* HDE-Build Notes Addendum 2.17, Non-BodyGraph chart-loader boundary and PF09 work coverage, records the September 7, 2026 gap scan's loader/caller finding and selected Separation home. HDE-Architecture §1.1 already classifies the boundary as Required-Now drift.  
``````

**Replacement text:**
``````text
* HDE Build Notes records the September 7, 2026 gap scan's loader/caller finding and selected Separation home. HDE-Architecture §1.1 already classifies the boundary as Required-Now drift.  
``````

**Basis:** Apply the active title-only Build Notes citation rule to this current PF passage. Preserve the September 7 finding, architecture requirement, every SEPA006 obligation/status, and its exclusion from EPIC040. The older addendum-number citation is not resolved against current numbering. Source-ledger references: A30; ledger H4/H5 and T-PF09-3 scope boundaries.

END OF REDLINES
