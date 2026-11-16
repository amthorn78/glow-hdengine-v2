# HDE-EPIC042 drain targets

Drain-targets ledger of HDE-EPIC042's close mutation set (CL-05). Each deferral and tracked issue below is named by its ID with its owner and drain target or route. None is a closure prerequisite, and none is drained by this close.

## Build checklist register

- HDE-DISS005: Task HDE-DISS005 and Subtask HDE-DISS005.3 in HDE Build Checklist Dissolution, recorded Partial; the delivered change supports Done (acceptance criterion AC-07). The authorized post-closure PF09 update. Owner: Product Owner.
- HDE-SEPA007: Task HDE-SEPA007 and Subtasks HDE-SEPA007.1 to HDE-SEPA007.5 in HDE Build Checklist Separation, recorded Not done; the delivered change supports Done under decision D-3, with the Required-When-Landed tag kept until the cutover (C-08). The authorized post-closure PF09 update. Owner: Product Owner.

## Doc-Delta record of the Magic10 v2 paths (C-09; DELTA-005)

HDE Schemas and Artifacts section 2.9 asks the implementing change to record the paths of the v2 configuration and of its schemas and catalogs through its Doc-Delta. The doc-deltas ledger of this close is byte-identical to the Step-0B capture `audit/qa/hde-epic042/00_meta/doc_deltas.md`, which this close does not overwrite (HDE Schemas and Artifacts section 1.2; CCR-E042-01), so the record of the paths is carried here. Delivered at the tested commit of the QA run, as the closure decision section 9 lists them:

- DELTA-005: `catalog/centers_v1.json`, the centers catalog (335 bytes).
- DELTA-005: `catalog/type_pairing_v1.json`, the Type-pairing catalog (1,146 bytes).
- DELTA-005: `schemas/centers_v1.schema.json`, the centers catalog schema (1,436 bytes).
- DELTA-005: `schemas/type_pairing_v1.schema.json`, the Type-pairing catalog schema (1,895 bytes).
- DELTA-005: `schemas/magic10_mechanics_v2.schema.json`, the v2 mechanics configuration schema (11,941 bytes).
- DELTA-005: `schemas/thresholds_v2.schema.json`, the v2 thresholds schema (1,937 bytes).
- DELTA-005: `schemas/magic10_result_v2.schema.json`, the v2 result schema (1,632 bytes).
- DELTA-005: `schemas/magic10_compat_result_v2.schema.json`, the v2 compat result schema (1,871 bytes).
- DELTA-005: `engine/config/magic10_v2_loader.py`, the fail-closed v2 loader (21,409 bytes).
- DELTA-005: no governed v2 configuration file and no version-2 `math/thresholds.json` exist; they are written at the release cut (HDE-DIST008.2). The labelled non-canon fixtures that stand in for them are `tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json`, `tests/fixtures/magic10_v2/thresholds_v2.fixture.json` and `tests/fixtures/magic10_v2/LABEL.txt`.
- DELTA-005 drain target: HDE Schemas and Artifacts section 2.9. Owner: Product Owner, through canon maintenance.

## Canon and repository drainage

- DELTA-001: `README.md` line 115, the POST-only wording for `/api/compat/v1` against the endpoint catalog's four methods. Owner: Product Owner. Non-mandatory.
- DELTA-002: `AGENTS.md` still names `docs/pfcanon`. Owner: Product Owner. Non-mandatory.
- DELTA-003: the pre-push tool's `documentation_only` note (triage finding A-18; Question 3). Owner: Product Owner to assign. Non-mandatory.
- DELTA-004: HDE Build Notes text points: triage finding A-19, the offsets' "Implementation status: Not started" line, and the two points on addendum 2.8 (QA Report section 9). Owner: Product Owner. Non-mandatory.
- DELTA-006: resolved by amthorn78/glow-hdengine-v2#857, which registered the QA evidence in the evidence index. Nothing drains.
- CCR-E042-01: who writes the epic-scoped doc-delta capture, disposition (A), APPROVED; the HDE Build Notes wording is the Product Owner's. Owner: Product Owner.
- HDE Build Notes 2.1 and 2.2: retire or keep 2.1 at closure; drain 2.1 and the offsets of 2.2 (drain targets D-1 to D-13). Owner: Product Owner (ISSUE-EPIC042-TI-04, ISSUE-EPIC042-TI-08).
- HDE Build Notes 2.3 to 2.11 for this change: each addendum's own drain targets. Owner: Product Owner, through canon maintenance.

## Tracked issues

- ISSUE-EPIC042-TI-01: proved under this epic (fixture-only home, Implementation Audit Q-01 alternative A).
- ISSUE-EPIC042-TI-02: proved under this epic (WU-PR-01 generator).
- ISSUE-EPIC042-TI-03: proved under this epic (labelled non-canon fixtures; C-07 held).
- ISSUE-EPIC042-TI-04: carried forward; permanent canon still reads "offsets not set"; drained through HDE Build Notes 2.2 (D-1 to D-13). Owner: Product Owner.
- ISSUE-EPIC042-TI-05: proved; no tool-input refresh was a deliverable. The tool-input copies of PF09.2 and PF09.3 lag once the PF09 moves are applied. Owner of that refresh: Product Owner.
- ISSUE-EPIC042-TI-06: proved (Specification review v1.1).
- ISSUE-EPIC042-TI-07: carried forward; the acceptance-map canon question for tokenless work stays the Product Owner's. This close writes the acceptance map and its viability log through the close-pack writer. Owner: Product Owner.
- ISSUE-EPIC042-TI-08: carried forward; records after closure (HDE Build Notes 2.1 retire or keep; drain 2.1 and 2.2; PF09 updates; Board Card). Owner: Product Owner.

## Routed items and proof limits

- A-07: `engine/config/bundles.py` line 78, a v1-edges consumer missing from the cutover list; its cutover-row assignment and the "Magic-10 v2 bundles" statement's implementing row (Implementation Plan Q-02; triage Question 2). Owner: Product Owner.
- O-1: the INV-4 guard fails by design at the cut and is retired then; the contract-evidence generator is re-run at the cut. Owner: HDE-DIST008.2.
- O-5: the vendored HDE Build Notes copy lags canon; also the PF23 Reality Audits update. Owner: Product Owner, by ordinary pull request and manual update.
- MB-096: a step that a PASS verdict needs belongs in the QA Plan (QA RCA RC-1). Owner: GCFPE-MGMT-10.
- QA proof limits, carried: qa-09's band binding covers only the Cool region; single-pair coverage in qa-05 and qa-09; vendor request counts are not observable (QA Report section 10).
