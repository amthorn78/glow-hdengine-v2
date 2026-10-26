# PF09.3 from v1.1.7 — exact redlines

Run identity: `GTWPE-20261026-PF10-v13.8.8-T-PF09.3`. Assigned ledger task: `T-PF09.3`, rows S-CR3, A35 (relations R-1 and R-2) and A02 (RP-2).

Preparation outcome: `READY`. Save completeness is recorded in the separate proof log after complete saved-pair readback.

Originating preparer: the Nathan-started T-PF09.3 document session, a Claude Code cloud session (https://claude.ai/code/session_01YSdc7bi4Jf3eEwEQmcbqCc), acting under TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862). A returned Apply diagnostic comes back to this preparer and run.

Original: `amthorn78/glow-hdengine-v2` / `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.7.md` on `main`, read at `9dda63dd3f05f496c3ff67e95da78550d3950c5a` and unchanged at `0838ba08254eaefc888019df49a06aa2ae99cc6c`. Git blob `1e8fb350a7ab46cec1c4894798db1f1b1f0a1d94`; v1.1.7; 86,650 bytes; 1,378 LF line ends; SHA-256 `3f1f7c429c8de9df5c87ea680adf899e5206affc058ced47664a42f328667266`; UTF-8, no BOM, no CR.

Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, identical on `main` at `0838ba08`). Destination: branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, the ledger's predeclared continuation, because the ledger PR #760 merged on 2026-10-26T21:18:51Z.

Selected incoming sources, in source order:

1. `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, v13.8.8, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`: front matter lines 1–223 (application rules), addendum 2.2 lines 258–337 and addendum 2.35 lines 3725–3955.
2. `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1, blob `c4802a5a7fa3`, SHA-256 `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df`: CR-3, lines 221–230.
3. `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, delta 01, blob `9408d6ed091b`, SHA-256 `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636`, approved (DELTA_APPROVE, Thoth, 2026-10-21T18:36:00Z), as the overlay of the base: C-6 (line 59) for S01.

Document-control header, reserved for TW-APPLY-10. Baseline schema and values: `**Title:**` PF09.3-Canon-HDE-Build-Checklist-Separation; `**Version:**` v1.1.7 (a `v`-prefixed three-component dotted numeric version); `**Status:**` Canon; `**Effective date:**` 2026-10-11 (`YYYY-MM-DD`); `**Last Update Gate:**` BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-E-10-closure-decision-v1.0.md; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md; `**Invocation tag:**` INV-f2ac55d77ce9aacc. The sources that justified this update, in source order, are: the PF10 file `PF10-HDE-Build-Notes-v13.8.8.md` (version 13.8.8); `HDE-CRD-0002-specification-v1.1-approved.md`; `HDE-CRD-0002-specification-delta-v1.0.md`. The closure decision, QA Report, close report and `tests/retired_tests.md` are cited inside payloads as evidence, not as change sources. No payload below touches the header. The target has no change log, revision history or Doc-Delta section, so no history-entry redline is needed. The full-target scan found no `Draft` status language, placeholder, TODO or unresolved drafting note to remove. Title, Status and Invocation tag stay unchanged.

Literal convention. Each fenced literal is exactly the bytes between the newline that ends its opening fence line and the newline that begins its closing fence line. A literal that starts or ends with an LF therefore shows an empty first or last line inside the fence. Trailing spaces are significant. The fences are six backticks; no payload contains a fence.

All seven operations resolve independently against the unchanged original. Their original spans and gap do not overlap or touch, and none is at the header.

## Redline RL001

**Classification:** Phase Master Update; Notes Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**`

**Original location:** Phase **Notes:** list: the HDE-SEPA006 bullet and the phase-master bullet that follows it (the third and fourth bullets), before Task HDE-SEPA001. The old block is original lines 172 to 173, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
* HDE-SEPA006 records the separate non-BodyGraph chart-loader boundary correction, supported-caller migration, operational-path retirement, and meaningful boundary verification. The new task and its three subtasks are **Not done**.  
* The phase master status remains **Not Done**. Open Separation implementation and verification obligations are not merely status-reconciliation or later-phase closure bookkeeping. HDE-CRD-0001's closure and accepted QA do not discharge these separate obligations.
``````

**Replacement text:**
``````text
* HDE-SEPA006 records the separate non-BodyGraph chart-loader boundary correction, supported-caller migration, operational-path retirement, and meaningful boundary verification. The new task and its three subtasks are **Not done**. It also owns the legacy chart-loader defect that HDE-CRD-0002 exposed and did not fix.  
* The phase master status remains **Not Done**. Open Separation implementation and verification obligations are not merely status-reconciliation or later-phase closure bookkeeping. The closures and accepted QA of HDE-CRD-0001 and HDE-CRD-0002 do not discharge these separate obligations.
``````

**Source-ledger rows:** A35 R-1, A02 RP-2 (phase statement of HDE-SEPA006 and its open obligations)

**Basis:** HDE Build Notes 2.2 RP-2 routes the legacy chart-loader defect to the Product Owner as decision owner for Task HDE-SEPA006 and records that it is not fixed in HDE-CRD-0002; 2.35 R-1 records HDE-SEPA006 as its owning row, not targeted for closure. HDE-CRD-0002 is closed (CL-C-10 v1.2), so the phase statement that a CRD closure does not discharge Separation obligations now names both closed CRDs. The phase master status stays Not Done because HDE-SEPA006 and its three subtasks remain Not done (PF09.3 0.6 completion standard).

## Redline RL002

**Classification:** Notes Update; Evidence Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA005 — Production Magic10 mechanics configuration contract**`

**Original location:** **Task notes:** of Task HDE-SEPA005, the bullet beginning "The two environment-blocked live requirements are re-homed" (original line 1167). The old block is original line 1167, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
* The two environment-blocked live requirements are re-homed, not completed: live, read-only Gate readiness against current rows is carried by HDE-COAG003.8, and live DB Reader v1/v2 success over live HTTP is carried by the new HDE-COAG003.9, both in PF09.7-Canon-HDE-Build-Checklist-Coagulation. Both require a future epic with the App user model, under its own approved Specification and QA Plan; no epic or completed live result is assigned here. The re-homing follows the HDE-EPIC040 CL-40 gap scan (`docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md`, findings G-1 and F-2). The `--allow-prod-vendor` gap remains with the PF05 and CLI owners through change control, outside HDE-EPIC040.
``````

**Replacement text:**
``````text
* The two environment-blocked live requirements are re-homed, not completed: live, read-only Gate readiness against current rows is carried by HDE-COAG003.8, and live DB Reader v1/v2 success over live HTTP is carried by the new HDE-COAG003.9, both in PF09.7-Canon-HDE-Build-Checklist-Coagulation. Both require a future epic with the App user model, under its own approved Specification and QA Plan; no epic or completed live result is assigned here. The re-homing follows the HDE-EPIC040 CL-40 gap scan (`docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md`, findings G-1 and F-2). The `--allow-prod-vendor` gap, carried outside HDE-EPIC040 through change control, was delivered by HDE-CRD-0002 requirement S14; its proven scope is recorded in `audit/HDE-CRD-0002_close_report.md`.
``````

**Source-ledger rows:** A35 R-2 (line 1167)

**Basis:** HDE Build Notes 2.35 R-2: the note says the `--allow-prod-vendor` gap "remains with the PF05 and CLI owners"; HDE-CRD-0002 has since delivered `--allow-prod-vendor` (S14). The close report records S14 as MET with its proven scope (local matrix, check 9; one bounded live vendor call, check 20). Only the last sentence changes; the re-homing of the live requirements to HDE-COAG003.8 and HDE-COAG003.9 is unchanged (2.35 R-5).

## Redline RL003

**Classification:** Notes Update; Evidence Update; Epic-information Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA005 — Production Magic10 mechanics configuration contract**`

**Original location:** **Task notes:** of Task HDE-SEPA005, the last bullet, beginning "Carried packaging, HTTP, CLI, evidence-owner, and repository limitations" (original line 1170). The old block is original line 1170, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
* Carried packaging, HTTP, CLI, evidence-owner, and repository limitations retain their recorded owners. In particular, wheel installs omit required release members; HTML 404 remains on the recorded non-compat factory paths; the CLI proof test and out-of-lane failures remain baseline; engine-core currency testing and Mirror origin labels remain evidence-owner work. The bounded security QA checks do not supply the missing implementation-delta code security review. Stronger atomicity and capture re-identification promises were not adopted. These limits do not reopen unrelated Done rows or become new tasks by this record. The Product Owner accepted them for CRD drafting as HDE-CRD-0002 on 2026-10-11; that CRD's PF30 record, once entered, owns them.
``````

**Replacement text:**
``````text
* The Product Owner accepted the carried packaging, HTTP, CLI, evidence-owner, and repository limitations for CRD drafting as HDE-CRD-0002 on 2026-10-11. HDE-CRD-0002's governing record is its approved Specification, `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, as overlaid by its approved delta 01, `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`. HDE-CRD-0002 reached `CLOSE / CHANGE_CLOSED` at 2026-10-26T16:40:00Z (`docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md`), after its final QA Report recorded PASS (`docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md`). It delivered these corrections: the production app returns the governed not-found envelope, not HTML, for unknown non-compat paths (S02); every test file runs in a CI lane or is retired with a recorded reason, and the recorded failures, including the CLI proof test's, are fixed or retired with their files (S03); the engine-core currency test checks release identity (S11), and current-release Mirror captures carry current-release labels (S12); and the missing code security review of what HDE-EPIC040's #467, #492, #501, and #508 merged is recorded, with findings F01 to F09 fixed and the findings it routed to the Product Owner awaiting disposition (S19). Each delivery's proven scope is recorded in `audit/HDE-CRD-0002_close_report.md`. Wheel installs were not delivered: Specification delta 01 removed the packaging requirement (S01) by Product Owner decision, so a regular wheel install outside a source checkout still does not admit the release. Stronger atomicity and capture re-identification promises were not adopted. These limits do not reopen unrelated Done rows or become new tasks by this record.
``````

**Source-ledger rows:** S-CR3 (line 1170); A35 R-2 (line 1170)

**Basis:** Specification v1.1 CR-3 directs the PF09 owner to reword this note to name the Specification in place of "that CRD's PF30 record, once entered", which will not exist (HDE Governance 9.1.1; CR-1). HDE Build Notes 2.35 R-2 records that HDE-CRD-0002 delivered HTML 404 (S02), the CLI proof test and out-of-lane failures (S03), engine-core currency and Mirror labels (S11, S12) and the code security review (S19), and removed wheel installs (S01) by Product Owner decision, so the "remain baseline" posture is stale. Delta 01 C-6 states the S01 limit. Closure, QA and per-requirement scope are cited to their records. Atomicity and re-identification stay not adopted (Specification Exclusions, "Not reopened").

## Redline RL004

**Classification:** Notes Update; Epic-information Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction**`

**Original location:** The **Owner / execution lane:** field of Task HDE-SEPA006 (original line 1293). The old block is original line 1293, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
**Owner / execution lane:** Implementation Agent (IA) for implementation planning and delivery coordination; the dedicated PR implementation lane delivers the authorized code, tooling, tests, and evidence. No individual session is assigned by this row.
``````

**Replacement text:**
``````text
**Owner / execution lane:** Implementation Agent (IA) for implementation planning and delivery coordination; the dedicated PR implementation lane delivers the authorized code, tooling, tests, and evidence. The Product Owner is this task's decision owner, including for the legacy chart-loader defect recorded in the task notes. No individual session is assigned by this row.
``````

**Source-ledger rows:** A02 RP-2; A35 R-1

**Basis:** HDE Build Notes 2.2 RP-2 routes the defect "to the Product Owner as the decision owner for Task HDE-SEPA006"; 2.35 R-1: "the PF09 owner's planning, with the Product Owner as HDE-SEPA006 decision owner". The IA and PR lanes are unchanged.

## Redline RL005

**Classification:** Epic-information Update

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction**`

**Original location:** The **Epic or card:** field of Task HDE-SEPA006 (original line 1297). The old block is original line 1297, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
**Epic or card:** Not selected. This is separate planned product work, not an addition to the closed HDE-CRD-0001 scope.
``````

**Replacement text:**
``````text
**Epic or card:** Not selected. This is separate planned product work, not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope.
``````

**Source-ledger rows:** A35 R-1; A02 RP-2

**Basis:** HDE-CRD-0002 touched this task's surface (it retired a loader test and routed the defect) but did not take the task into its scope: its Specification excludes PF09 mapping of its work, 2.2 RP-2 records the defect as not fixed and not deferred to a unit of HDE-CRD-0002, and 2.35 R-1 records no closure target. The task stays unselected for any Epic or CRD.

## Redline RL006

**Classification:** Notes Update; Evidence Update; Clarity Fix

**Operation:** REPLACE

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction**`

**Original location:** The three bullets of Task HDE-SEPA006's **Task notes:** (original lines 1314 to 1316), after the "**Task notes:**" label and its blank line. The old block is original lines 1314 to 1316, from its first byte through its last visible character; the LF after it is not consumed.

**Expected occurrence:** 1 exact old block in the stated section path; 1 in the whole original.

**Old text:**
``````text
* HDE Build Notes records the September 7, 2026 gap scan's loader/caller finding and selected Separation home. HDE-Architecture §1.1 already classifies the boundary as Required-Now drift.  
* This task introduces no scoring algorithm, full Magic10 delivery, new provider contract, fallback data, broader Engine I/O exemption, production operation, or provenance helper.  
* HDE-CRD-0001 retains its existing CLOSE / CHANGE\_CLOSED decision and exact accepted evidence. That evidence is not acceptance of this separate migration. No implementation, QA, or completion is claimed for this task.
``````

**Replacement text:**
``````text
* HDE Build Notes recorded the September 7, 2026 gap scan's loader/caller finding and selected Separation home. HDE-Architecture §1.1 already classifies the boundary as Required-Now drift.  
* This task introduces no scoring algorithm, full Magic10 delivery, new provider contract, fallback data, broader Engine I/O exemption, production operation, or provenance helper.  
* HDE Build Notes records a legacy chart-loader defect that HDE-CRD-0002's CI-coverage work exposed, and routes it to this task with the Product Owner as decision owner: in the legacy signature of `engine/charts/loader.py`, `_call_legacy` calls `get_chart` on a `FixturesProvider`, which has no such method, and the call fails with `AttributeError` at `engine/charts/loader.py:81`. HDE Build Notes dates the defect to `6c6f4b2a` (2025-09-28) and records that only tests called the legacy signature, that the loader is not a release member, and that it is not reached at runtime. HDE-CRD-0002 retired `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` under its requirement S03 and recorded the reason in `tests/retired_tests.md`. A run of that test appended to the tracked `artifacts/logs/loader_call.jsonl` through the loader's own call log; HDE-CRD-0002 left that file unchanged. Retained coverage for the test's passing case is `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`. HDE-CRD-0002 did not fix the defect, and no repair of `engine/charts/loader.py` was approved; its close report, `audit/HDE-CRD-0002_close_report.md`, defers the defect to the Product Owner as decision owner. This evidence records the defect for this task; it is not implementation, QA, or completion of any part of it.  
* HDE-CRD-0001 and HDE-CRD-0002 each retain their existing CLOSE / CHANGE\_CLOSED decision and exact accepted evidence. That evidence is not acceptance of this separate migration. No implementation, QA, or completion is claimed for this task.
``````

**Source-ledger rows:** A35 R-1 with A02 RP-2 (HDE-SEPA006 evidence: the legacy chart-loader defect and the retired test)

**Basis:** 2.35 R-1 returns the defect evidence to the PF09 owner: `_call_legacy` calls `get_chart` on a `FixturesProvider` that has none (AttributeError at engine/charts/loader.py:81), the retired test appended to the tracked loader_call.jsonl, and no repair was approved. 2.2 RP-2 supplies the retirement under S03, its recorded reason, the 2025-09-28 origin, the not-a-release-member and not-reached-at-runtime facts and the replacing coverage. The first bullet keeps its history in the past tense, because the current HDE Build Notes holds no September 7, 2026 gap-scan record. The second bullet is unchanged. The last bullet adds HDE-CRD-0002's closure beside HDE-CRD-0001's.

## Redline RL007

**Classification:** Evidence Update; Notes Update (subtask)

**Operation:** INSERT

**Original heading path:** `# **Phase III — Separation (Public shape, identity, guardrails)**` / `## **Task HDE-SEPA006 — Non-BodyGraph chart-loader boundary correction**` / `### **Subtask HDE-SEPA006.2 — Supported caller migration**`

**Original location:** End of Subtask HDE-SEPA006.2, between its **Evidence / artifacts required:** paragraph and the blank line before the Subtask HDE-SEPA006.3 heading. The gap is at original line 1355, column 1, immediately after the LF that ends original line 1354.

**Expected occurrence:** 1 gap. The BEFORE literal followed immediately by the AFTER literal occurs once in the whole original and once in the stated section path; the gap is their shared boundary. Neither anchor is deleted.

**Before anchor:**
``````text
Supported-caller inventory with exact source attribution and a disposition for every member; migration/retirement diff; focused runtime, tooling, and loader/provider caller-regression results. Any retained compatibility surface must have both an owning-contract basis and evidence of actual purity.

``````

**After anchor:**
``````text

### **Subtask HDE-SEPA006.3 — Boundary and behavior verification**
``````

**Inserted text:**
``````text

**Notes:**  
HDE-CRD-0002 retired `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py`, a test caller of the legacy loader signature, under its requirement S03, with the reason recorded in `tests/retired_tests.md`. That retirement is not caller migration: it neither migrates nor removes the legacy signature, and the loader defect recorded in Task HDE-SEPA006's notes remains unfixed.

``````

**Source-ledger rows:** A35 R-1 (HDE-SEPA006.2 covers the retired test)

**Basis:** 2.35 R-1: HDE-SEPA006.2's caller migration includes "relevant loader/provider tests", covering the retired test. The note records that test's retirement as evidence for this subtask and states its limit: retiring a test caller is not migration, so the legacy signature and the defect stay in scope. It adds no requirement; status stays Not done.

END OF REDLINES
