# Redlines: PF09.4-Canon-HDE-Build-Checklist-Conjunction, from v1.3.1

## Package identity

| Field | Value |
| :- | :- |
| Artifact | Exact redlines for one PF09 phase document (TW-DRAIN-20) |
| Target | `PF09.4-Canon-HDE-Build-Checklist-Conjunction` v1.3.1, `docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md` |
| Original baseline | `origin/main` at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; blob `3abe7fc79d6987006590b65d39ab9e1f60da9538`; 111,181 bytes; 2,185 lines, LF endings, final LF; SHA-256 `65d4b9e2a1303638cc5c66a1d02f55c721509559d24ee8e42cb04a793750ac84` over the raw bytes. Unchanged since the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a` |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` (HDE Build Notes v13.8.8), blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`: addendum 2.8 (lines 890–1002) and addendum 2.35 (lines 3725–3955), read in full |
| Supporting cross-reference | X04, `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` §18 (lines 753–792), blob `1d6a92a483e2` |
| Routing record | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` (blob `74944b261c0e`, equal at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` and on `main`), task T-PF09.4, rows A35 (relation R-2) and A08 with X04 (OBS-P3-16) |
| Prompt | TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862 (fetched live 2026-10-26) |
| Preparer | Claude Code cloud session https://claude.ai/code/session_01TJJV6QvnTufZxMtDS6LUip, started by Nathan for T-PF09.4 |
| Run identity | `T-PF09.4-PREP-20261026-01` (first preparation run; no earlier run exists for this target and source version) |
| Preparation outcome | `READY` |
| Save completeness | Recorded in the proof log after read-back |
| Proof log | `redlines-PF09.4-from-v1.3.1.proof-log.md`, beside this file |

## How to read a redline

- Every redline is a `REPLACE` of one exact, nonempty OLD block that occurs exactly once in the whole original baseline. There is no `INSERT`, `DELETE` or `FIND_AND_REPLACE` in this batch.
- Each OLD and NEW literal is the exact text between its opening fence line (````text) and its closing fence line (````), without the line break that precedes the closing fence. No literal contains a fence. Neither literal includes the line break that ends its last line, so every line break around a replaced block stays as it is.
- The heading path names the original's exact heading lines, outermost first; each heading occurs once, and each nested heading falls inside the section of the one before it. The original line numbers are informative only; the OLD literal and its count of one are the locator.
- All OLD spans are resolved against the same unchanged original. No two spans intersect or share a boundary.
- Document-control fields (Version, Effective date, Last Update Gate) are not redlined here. TW-APPLY-10 derives them. The proof log supplies their baseline values and the source identity for the gate.

## RL-01

- Operation: `REPLACE`
- Row: HDE-CONJ001
- Classification: Clarity Fix; Notes Update (task)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ001 — Dev HTTP Harness (single home)`
- Field: **Task notes:** → the "Defaults:" list
- Original lines (informative): 210–212
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A08 with X04 (OBS-P3-16)

OLD:

````text
Defaults:

`Cache-Control: no-store` on all harness responses.
````

NEW:

````text
Defaults:

`Cache-Control: no-store` on harness responses, except the dev Reader `/reader` success family, which keeps the A7 posture that PF05-Canon-HDE-CLI-API-Vendor-Ref §5.4 applies to the harness (HDE-CONJ001.1).
````

## RL-02

- Operation: `REPLACE`
- Row: HDE-CONJ001.1
- Classification: Clarity Fix (subtask description)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ001 — Dev HTTP Harness (single home)` > `### **Subtask HDE-CONJ001.1 — Harness behavior & non-production posture**`
- Field: **Subtask description:** → "**Response and payload posture.**"
- Original lines (informative): 249
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A08 with X04 (OBS-P3-16)

OLD:

````text
Uses `Cache-Control: no-store` on all harness responses.
````

NEW:

````text
Uses `Cache-Control: no-store` on harness responses, except the dev Reader `/reader` success family (`GET` `200`, `HEAD` `200` and `304`), which keeps the A7 posture that PF05-Canon-HDE-CLI-API-Vendor-Ref §5.4 applies to the harness instead of `no-store`. Harness errors always carry `no-store` and no `ETag`.
````

## RL-03

- Operation: `REPLACE`
- Row: HDE-CONJ005
- Classification: Notes Update; Evidence Update (task)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ005 — Reader Surface (API)`
- Field: **Task notes:** → the paragraph beginning "Done retains this row's"
- Original lines (informative): 1112
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2

OLD:

````text
Done retains this row's implemented surface and bounded tested-evidence scope. It does not assert deployed reachability or live current-row DB success. The carried HTML-404 transport observation, wheel-distribution decision, legacy CLI proof failure, and evidence-owner currency/provenance observations remain with their recorded owners; they are not resolved by these notes.
````

NEW:

````text
Done retains this row's implemented surface and bounded tested-evidence scope. It does not assert deployed reachability or live current-row DB success. The observations these notes carried are no longer open. HDE-CRD-0002, closed on 2026-10-26, delivered three of them under its approved Specification: the HTML-404 transport observation (O-P06a-22) by S02, so every 404 from the production app is the governed `ERR_NOT_FOUND` envelope with `no-store`; the legacy CLI proof failure (O-P06a-03) by S03, which retired `tests/reader_v1/test_cli_proof.py` with a recorded reason; and the evidence-owner currency and provenance observations (O-P06a-23 and O-P06b-17) by S11 and S12. Its final QA Report records checks 17, 2 and 8, which cover them, as PASS. The fourth, the wheel-distribution decision (O-12), is made: the Product Owner removed S01 on 2026-10-21, so a regular wheel install outside a source checkout still does not admit the release.
````

## RL-04

- Operation: `REPLACE`
- Row: HDE-CONJ005.4
- Classification: Evidence Update; Notes Update (subtask)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ005 — Reader Surface (API)` > `### Subtask HDE-CONJ005.4 — Reader A7 evidence indexing`
- Field: the paragraph "**Accepted HDE-EPIC040 evidence and current requirement:**"
- Original lines (informative): 1371
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2 (S12, O-P06b-17)

OLD:

````text
**Accepted HDE-EPIC040 evidence and current requirement:** PR06a records owner-regenerated Reader schema/golden and route evidence, with canonical gate and Evidence Index checks passing at its landed tree. PR06b records the later `1.3.0` cut, owner-regenerated dependents, and passing canonical gate and Index checks. Maintain applicable same-change Index/Mirror/hash/path-proof coherence through the existing owning writers; these records do not replace the whole-family requirement above. PR #559 separately landed and registered the QA evidence of record, resolving QA50-F01. Preserve capture-time identity and provenance; O-P06b-17's origin-family mirror labels remain with the evidence/updater owner.
````

NEW:

````text
**Accepted HDE-EPIC040 evidence and current requirement:** PR06a records owner-regenerated Reader schema/golden and route evidence, with canonical gate and Evidence Index checks passing at its landed tree. PR06b records the later `1.3.0` cut, owner-regenerated dependents, and passing canonical gate and Index checks. Maintain applicable same-change Index/Mirror/hash/path-proof coherence through the existing owning writers; these records do not replace the whole-family requirement above. PR #559 separately landed and registered the QA evidence of record, resolving QA50-F01. Preserve capture-time identity and provenance. HDE-CRD-0002's S12 has since corrected O-P06b-17's origin-family Machine Mirror labels, so current-release captures carry current-release labels; its final QA Report records check 8 as PASS.
````

## RL-05

- Operation: `REPLACE`
- Row: HDE-CONJ008.3
- Classification: Evidence Update; Notes Update (subtask)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ008 — Writer Surfaces (API)` > `### Subtask HDE-CONJ008.3 — Writer evidence presence & indexing`
- Field: the paragraph "**HDE-EPIC040 owner and registration consequence:**"
- Original lines (informative): 1811
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2 (S12, O-P06b-17)

OLD:

````text
**HDE-EPIC040 owner and registration consequence:** PR06a registers `tools/evidence/generate_conjunction_writer_evidence.py` with `_EVIDENCE_GENERATOR_TEST_OWNERS` so `tests/evidence/test_dev_conjunction_identity.py` is a changed-test target, and records owner-regenerated writer artifacts. The restored proof has no live-vendor dependency and uses real admission without a fabricated release. Keep its artifact and CI-owner registration coherent through those existing owners. The A7 exclusion and caller-controlled rails remain unchanged; the separate O-P06b-17 provenance-label observation is still owned by the evidence/updater lane.
````

NEW:

````text
**HDE-EPIC040 owner and registration consequence:** PR06a registers `tools/evidence/generate_conjunction_writer_evidence.py` with `_EVIDENCE_GENERATOR_TEST_OWNERS` so `tests/evidence/test_dev_conjunction_identity.py` is a changed-test target, and records owner-regenerated writer artifacts. The restored proof has no live-vendor dependency and uses real admission without a fabricated release. Keep its artifact and CI-owner registration coherent through those existing owners. The A7 exclusion and caller-controlled rails remain unchanged. HDE-CRD-0002's S12 has since resolved the separate O-P06b-17 provenance-label observation; its final QA Report records check 8 as PASS.
````

## RL-06

- Operation: `REPLACE`
- Row: HDE-CONJ009.2
- Classification: Evidence Update; Notes Update (subtask)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)` > `### Subtask HDE-CONJ009.2 — Global Index/Mirror discipline`
- Field: the paragraph "**Later HDE-EPIC040 evidence:**"
- Original lines (informative): 1994
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2 (S12, O-P06b-17)

OLD:

````text
**Later HDE-EPIC040 evidence:** PR06a and PR06b record owner-regenerated release dependents with passing canonical gate and Index checks. The exceptional closure records PR #559's separate landing and Index/Mirror registration of the QA evidence of record, resolving QA50-F01; that landing is not a new QA run. Maintain the existing same-change evidence discipline, preserve frozen capture-time identities, and retain O-P06b-17 with its evidence/updater owner. None of these facts creates an acceptance map, token matrix, close pack, or Conjunction phase exit.
````

NEW:

````text
**Later HDE-EPIC040 evidence:** PR06a and PR06b record owner-regenerated release dependents with passing canonical gate and Index checks. The exceptional closure records PR #559's separate landing and Index/Mirror registration of the QA evidence of record, resolving QA50-F01; that landing is not a new QA run. Maintain the existing same-change evidence discipline and preserve frozen capture-time identities. None of these facts creates an acceptance map, token matrix, close pack, or Conjunction phase exit. HDE-CRD-0002's S12 has since resolved O-P06b-17; its final QA Report records check 8 as PASS.
````

## RL-07

- Operation: `REPLACE`
- Row: HDE-CONJ010
- Classification: Notes Update (task)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration**`
- Field: **Task notes:** → the paragraph beginning "No new Epic, successor identifier"
- Original lines (informative): 2089
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2

OLD:

````text
No new Epic, successor identifier, implementation unit, acceptance token, or documentation-only task is allocated. HDE-SEPA006's Adapter/Engine chart-loader and caller migration remains separately owned in Separation. The known legacy CLI proof failure, wheel-distribution decision, and evidence currency/provenance observations retain their existing owners.
````

NEW:

````text
No new Epic, successor identifier, implementation unit, acceptance token, or documentation-only task is allocated. HDE-SEPA006's Adapter/Engine chart-loader and caller migration remains separately owned in Separation. HDE-CRD-0002 has since resolved the legacy CLI proof failure (S03) and the evidence currency and provenance observations (S11 and S12), and the wheel-distribution decision is made (S01 removed); HDE-CONJ010.4 and HDE-CONJ010.6 record the details. None of this changes this task's Partial status or its remaining population.
````

## RL-08

- Operation: `REPLACE`
- Row: HDE-CONJ010.4
- Classification: Notes Update; Evidence Update (subtask)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration**` > `### **Subtask HDE-CONJ010.4 — Engine Core and pre-admin surface integration**`
- Field: **Subtask notes:** → "**Remaining Partial burden:**"
- Original lines (informative): 2139
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2

OLD:

````text
**Remaining Partial burden:** Establish the complete supported pre-admin consumer migration required by this row, including the narrative, presenter, and current-generator obligations, with the row's no-legacy boundary and scoped evidence. The selected sources do not establish that complete population. PR06a/PR06b retain the pre-existing `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure with its recorded owner; the wheel-distribution decision and evidence currency/provenance observations are also carried, not waived. Do not represent the corrected production route as deployed/live current-row DB success.
````

NEW:

````text
**Remaining Partial burden:** Establish the complete supported pre-admin consumer migration required by this row, including the narrative, presenter, and current-generator obligations, with the row's no-legacy boundary and scoped evidence. The selected sources do not establish that complete population. The pre-existing `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure that PR06a/PR06b retained is resolved: HDE-CRD-0002's S03 retired that test with a recorded reason (O-P06a-03), because the legacy `scripts/hd_cli.py` stub is neither a Reader surface nor proof. Its S11 and S12 resolved the evidence currency and provenance observations, and the wheel-distribution decision is made: the Product Owner removed S01, so a regular wheel install outside a source checkout still does not admit the release. None of this completes the consumer migration above. Do not represent the corrected production route as deployed/live current-row DB success.
````

## RL-09

- Operation: `REPLACE`
- Row: HDE-CONJ010.6
- Classification: Notes Update; Evidence Update (subtask)
- Heading path: `# **Phase IV — Conjunction (Surfaces and tools meet the core)**` > `## **Task HDE-CONJ010 — Full Magic10 deterministic scoring integration**` > `### **Subtask HDE-CONJ010.6 — Integration goldens and parity**`
- Field: **Subtask notes:** → "**Remaining Partial burden:**"
- Original lines (informative): 2177
- Expected occurrences of OLD in the whole original: 1
- Ledger rows: A35 R-2 (S03, S12)

OLD:

````text
**Remaining Partial burden:** Reconcile and prove this row's full matrix, pair/cache identity, UID-independence, result schema, Reader projection, failure-token, and internal-parity population, with exact tested-state attribution and disclosed baseline failures. The selected consumer/golden proof does not independently establish the entire Conjunction population. Reader-to-CLI dump parity remains a v1 family, and the legacy CLI proof failure remains with its recorded owner. Preserve capture-time identity for frozen evidence; no current service identity substitutes for it, and O-P06b-17's origin-family mirror labels remain an evidence-owner question.
````

NEW:

````text
**Remaining Partial burden:** Reconcile and prove this row's full matrix, pair/cache identity, UID-independence, result schema, Reader projection, failure-token, and internal-parity population, with exact tested-state attribution and disclosed baseline failures. The selected consumer/golden proof does not independently establish the entire Conjunction population. Reader-to-CLI dump parity remains a v1 family. HDE-CRD-0002's S03 retired the legacy CLI proof test with a recorded reason, and its S12 corrected O-P06b-17's origin-family Machine Mirror labels; neither establishes this row's remaining population. Preserve capture-time identity for frozen evidence; no current service identity substitutes for it.
````

END OF REDLINES
