---
artifact_type: PF09_REDLINE
artifact_version: "1.0"
logical_id: HDE-EPIC040-PF09-REDLINE-LIVE-REQUIREMENTS
origin_change: HDE-EPIC040 (closed; CL-40 finding G-1 and F-2)
author: Isis, continuing Lead Developer for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
requested_by: 'Product Owner, 2026-10-11: "Ok, I want you to draft a standalone PF09 redline. Will do the update manually."'
applied_by: the Product Owner, as PF09 owner, by hand
base_commit: origin/main 1ea6a262
standing: Proposal only. Nothing in docs/pfcanon changes until the Product Owner applies it.
---

# PF09 redline: re-home HDE-EPIC040's two deferred live requirements

## 1. What this does

The HDE-EPIC040 CL-40 gap scan found two things about the live work that HDE-EPIC040 could not do because no user-bound rows exist yet:

- **G-1, a PF09 gap.** Live DB Reader v1/v2 success over live HTTP has no PF09 row. It is only a DEFERRED line pointing at "CL-40".
- **F-2, no gap.** Live read-only Gate readiness on current rows already has a home: PF09.7 HDE-COAG003.8. It just has not been moved there.

This redline:

1. **Closes G-1.** It adds PF09.7 **HDE-COAG003.9 — User-bound live Reader success verification**, status **Not done**, after HDE-COAG003.8. That completes the chain 003.6 cutover guard → 003.7 deploy, smoke and rollback → 003.8 Gate readiness → 003.9 live Reader success.
2. **Performs F-2.** It moves the live readiness observation into HDE-COAG003.8's notes, with a DEFERRED line.
3. **Moves two statuses.** HDE-SEPA005.5 goes **Partial → Done**, and so the HDE-SEPA005 parent goes **Partial → Done**. The re-homing was .5's only remaining condition (PF09.3 HDE-SEPA005.5 notes; QA-120 Report §14).
4. **Repoints every DEFERRED line** that said "CL-40" to the new rows, in PF09.3 and PF09.4.
5. **Fixes one stale cross-reference** in PF09.5 that the change would otherwise make wrong.
6. **Bumps the four headers.**

**The decision you make by applying it.** Applying this redline selects re-homing as the disposition of HDE-SEPA005.5's last condition. Canon has kept the alternative open: that the live observation lies outside .5's implementation text (PF09.3 HDE-SEPA005.5 notes; HDE Phased Epics C1; QA-120 Report §14). Both readings lead to .5 Done. If you prefer the other reading, reword the sentence in R3-8 that begins "Re-homing is the PF09 owner's disposition". Every other item still applies, because the live work needs a PF09 home under either reading (Change Process Guide §0.2: future work must be PF09-accounted).

**What it does not do.** No phase exit: PF09.3's phase master status stays **Not Done** because HDE-SEPA006 is open. No live result, epic, or ID other than HDE-COAG003.9. No evidence family or path home. No board movement. No PF10 addendum, because you chose a direct PF09 edit.

## 2. How to apply

1. **Start from the base below.** Every target is the exact text at `origin/main` `1ea6a262`. If a file's hash differs, stop and ask for a rebase of this redline.
2. **Apply all items in one pass.** Each target occurs exactly once in its file and no two targets overlap, so the order does not matter. REPLACE swaps the target for the replacement. A target can be part of a longer line; replace only the text shown. Some targets and replacements end in two spaces, which are Markdown line breaks; keep them.
3. **Rename the files** to the new versions with `git mv`, so history follows them.
4. **Effective date.** The headers say 2026-10-11. If you apply on another day, change that date in all four headers; the applied hashes in §5 then no longer match, which is expected.
5. **Merge order.** The headers cite `HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` (#602) and R3-6 relies on the HDE-CRD-0002 acceptance recorded with briefs v1.1 (#601). Merge #602 and #601 before, or in the same push as, the canon commit, so nothing on `main` cites a file that is not there.

| File at base | Base SHA-256 | New name |
| --- | --- | --- |
| `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.6.md` | `06c2b0208e211e31e2a6a68c5e169c9bcaa32adc03f4745efbefe5d99bcfe6eb` | `PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.7.md` |
| `docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.md` | `2c19e6b64931b4c0f2e313de3684f325a5e64c59a815013f5c2ad1922a4e82a5` | `PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md` |
| `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.md` | `6085affe26bc5cdbcc24086198d4c7fbae635358f6bde84fe7eba82d47e70292` | `PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md` |
| `docs/pfcanon/PF09.7-Canon-HDE-Build-Checklist-Coagulation-v1.1.6.md` | `360c9083476adeb62fdba064a93648404924a961b9b3e1e004c7c0e10118e97d` | `PF09.7-Canon-HDE-Build-Checklist-Coagulation-v1.1.7.md` |

## 3. Items

| ID | File | Op | Base line | Change |
| --- | --- | --- | --- | --- |
| R3-1 | PF09.3 | REPLACE | 7 | Front matter: version, effective date, update gate. |
| R3-2 | PF09.3 | REPLACE | 171 | Phase notes: SEPA005 status and re-homing. |
| R3-3 | PF09.3 | REPLACE | 1157 | HDE-SEPA005 parent status Partial to Done. |
| R3-4 | PF09.3 | REPLACE | 1163 | Parent notes: completion basis. |
| R3-5 | PF09.3 | REPLACE | 1167 | Parent notes: live requirements re-homed; PF09 gap G-1 closed by new row. |
| R3-6 | PF09.3 | REPLACE | 1170 | Parent notes: carried limitations now proposed under HDE-CRD-0002. |
| R3-7 | PF09.3 | REPLACE | 1264 | HDE-SEPA005.5 status Partial to Done. |
| R3-8 | PF09.3 | REPLACE | 1272 | HDE-SEPA005.5 notes: re-homing performed. |
| R4-1 | PF09.4 | REPLACE | 7 | Front matter: version, effective date, update gate. |
| R4-2 | PF09.4 | REPLACE | 2141 | HDE-CONJ010.4: name the successor row. |
| R4-3 | PF09.4 | REPLACE | 2179 | HDE-CONJ010.6: name the successor rows. |
| R5-1 | PF09.5 | REPLACE | 7 | Front matter: version, effective date, update gate. |
| R5-2 | PF09.5 | REPLACE | 2467 | Cross-reference: routing statement that the redline makes stale. |
| R7-1 | PF09.7 | REPLACE | 7 | Front matter: version, effective date, update gate. |
| R7-2 | PF09.7 | REPLACE | 1278 | HDE-COAG003.8: accept the re-homed readiness observation. |
| R7-3 | PF09.7 | REPLACE | 1280 | New subtask HDE-COAG003.9 before the HDE-COAG004 heading (closes PF09 gap G-1); the heading itself is unchanged. |

**Coverage.**
- G-1 (live DB Reader success has no row): R7-3 creates the row; R4-2, R4-3 and R3-5 point at it.
- F-2 (re-home live readiness to HDE-COAG003.8): R7-2 accepts it; R3-8, R3-4, R4-3 and R5-2 point at it.
- Status consequence: R3-7 (.5), R3-3 and R3-4 (parent), R3-2 (phase notes).
- HDE-CRD-0002 note on the carried limitations: R3-6.
- Headers: R3-1, R4-1, R5-1, R7-1.

## 4. Item text

### PF09.3 — `PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.6.md`

#### R3-1 — Front matter: version, effective date, update gate.

**REPLACE**, base line 7.

Target:

```text
**Version:** v1.1.6

**Status:** Canon

**Effective date:** 2026-10-09

**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-E-10-closure-decision-v1.0.md
```

Replacement:

```text
**Version:** v1.1.7

**Status:** Canon

**Effective date:** 2026-10-11

**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-E-10-closure-decision-v1.0.md; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md
```

#### R3-2 — Phase notes: SEPA005 status and re-homing.

**REPLACE**, base line 171.

Target:

```text
* HDE-SEPA005 remains **Partial**: HDE-SEPA005.1 through HDE-SEPA005.4 are **Done**, and HDE-SEPA005.5 is **Partial**. The deferred live current-row Gate-readiness observation still needs re-homing by the PF09 owner; QA50-F01 is resolved.  
```

Replacement:

```text
* HDE-SEPA005 is **Done**: HDE-SEPA005.1 through HDE-SEPA005.5 are **Done**. The two live observations that HDE-EPIC040 deferred as blocked by environment are re-homed to PF09.7-Canon-HDE-Build-Checklist-Coagulation: live current-row Gate readiness to HDE-COAG003.8 and live DB Reader success to HDE-COAG003.9. QA50-F01 is resolved.  
```

#### R3-3 — HDE-SEPA005 parent status Partial to Done.

**REPLACE**, base line 1157.

Target:

```text
**Task status:** **Partial**

**Epic or card:** **HDE-EPIC040 — Separation Pass 3**.
```

Replacement:

```text
**Task status:** **Done**

**Epic or card:** **HDE-EPIC040 — Separation Pass 3**.
```

#### R3-4 — Parent notes: completion basis.

**REPLACE**, base line 1163.

Target:

```text
* HDE-SEPA005.1 through HDE-SEPA005.4 are **Done** for their stated implementation and evidence scope. HDE-SEPA005.5 is **Partial**, so this parent remains **Partial** under this document's completion standard. QA50-F01 is resolved; the remaining .5 condition is the PF09 owner's re-homing of the deferred live current-row Gate-readiness observation. Neither epic closure nor the completed offline command makes that live observation complete.
```

Replacement:

```text
* HDE-SEPA005.1 through HDE-SEPA005.5 are **Done** for their stated implementation and evidence scope, so this parent is **Done** under this document's completion standard. QA50-F01 is resolved, and the deferred live current-row Gate-readiness observation is re-homed to HDE-COAG003.8 in PF09.7-Canon-HDE-Build-Checklist-Coagulation. Neither epic closure nor the completed offline command makes that live observation complete; it remains open in its new row.
```

#### R3-5 — Parent notes: live requirements re-homed; PF09 gap G-1 closed by new row.

**REPLACE**, base line 1167.

Target:

```text
* The two environment-blocked live requirements remain deferred: live, read-only Gate readiness against current rows is accounted under .5; live DB Reader v1/v2 success over live HTTP remains a PF09 gap noted at this parent. They require a future epic with the App user model, under its own approved Specification and QA Plan, through the HDE-EPIC040 CL-40 gap scan. No future task ID, epic, phase, or completed live result is assigned here. The `--allow-prod-vendor` gap remains with the PF05 and CLI owners through change control, outside HDE-EPIC040.
```

Replacement:

```text
* The two environment-blocked live requirements are re-homed, not completed: live, read-only Gate readiness against current rows is carried by HDE-COAG003.8, and live DB Reader v1/v2 success over live HTTP is carried by the new HDE-COAG003.9, both in PF09.7-Canon-HDE-Build-Checklist-Coagulation. Both require a future epic with the App user model, under its own approved Specification and QA Plan; no epic or completed live result is assigned here. The re-homing follows the HDE-EPIC040 CL-40 gap scan (`docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md`, findings G-1 and F-2). The `--allow-prod-vendor` gap remains with the PF05 and CLI owners through change control, outside HDE-EPIC040.
```

#### R3-6 — Parent notes: carried limitations now proposed under HDE-CRD-0002.

**REPLACE**, base line 1170.

Target:

```text
These limits do not reopen unrelated Done rows or become new tasks by this record.
```

Replacement:

```text
These limits do not reopen unrelated Done rows or become new tasks by this record. The Product Owner accepted them for CRD drafting as HDE-CRD-0002 on 2026-10-11; that CRD's PF30 record, once entered, owns them.
```

#### R3-7 — HDE-SEPA005.5 status Partial to Done.

**REPLACE**, base line 1264.

Target:

```text
**Subtask status:** **Partial**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis and remaining gap:**
```

Replacement:

```text
**Subtask status:** **Done**

**Epic or card:** HDE-EPIC040 — Separation Pass 3.

**Notes / completion basis:**
```

#### R3-8 — HDE-SEPA005.5 notes: re-homing performed.

**REPLACE**, base line 1272.

Target:

```text
* The live, read-only observation against current user-bound rows remains unproved and its PF09 re-homing remains unresolved. The App user model and persistent user-bound BodyGraphs were unavailable to this QA; no live command ran and no live proof is claimed. This row stays **Partial** until its actual PF09 owner resolves that remaining obligation through the separately authorized maintenance/gap route. The alternative reading that excludes the live observation from this row has not been selected.
* DEFERRED → HDE-EPIC040 CL-40 gap scan / future epic with the App user model — live current-row Gate readiness was blocked by the environment and must be planned under that future epic's approved Specification and QA Plan; not a close blocker for HDE-EPIC040. This reference allocates no new row or future epic ID and does not itself perform the re-homing.
```

Replacement:

```text
* The live, read-only observation against current user-bound rows remains unproved. It is re-homed to HDE-COAG003.8 in PF09.7-Canon-HDE-Build-Checklist-Coagulation, which owns the read-only current-row Gate-readiness inventory before Reader activation, and it is no longer a completion condition of this row. Re-homing is the PF09 owner's disposition of the remaining condition; the alternative reading, that the observation lies outside this row's implementation text, is not adopted. The App user model and persistent user-bound BodyGraphs were unavailable to HDE-EPIC040 QA; no live command ran and no live proof is claimed.
* DEFERRED → HDE-COAG003.8 / future epic with the App user model — live current-row Gate readiness was blocked by the environment and must be planned under that future epic's approved Specification and QA Plan; not a close blocker for HDE-EPIC040.
```

### PF09.4 — `PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.md`

#### R4-1 — Front matter: version, effective date, update gate.

**REPLACE**, base line 7.

Target:

```text
**Version:** v1.3

**Status:** Canon

**Effective date:** 2026-10-09

**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md
```

Replacement:

```text
**Version:** v1.3.1

**Status:** Canon

**Effective date:** 2026-10-11

**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md
```

#### R4-2 — HDE-CONJ010.4: name the successor row.

**REPLACE**, base line 2141.

Target:

```text
DEFERRED → CL-40 / future Epic with the App user model — live DB Reader success is blocked by environment; not a close blocker for HDE-EPIC040. No successor ID or completed live observation is recorded.
```

Replacement:

```text
DEFERRED → HDE-COAG003.9 in PF09.7-Canon-HDE-Build-Checklist-Coagulation / future Epic with the App user model — live DB Reader success is blocked by environment; not a close blocker for HDE-EPIC040. No completed live observation is recorded.
```

#### R4-3 — HDE-CONJ010.6: name the successor rows.

**REPLACE**, base line 2179.

Target:

```text
DEFERRED → CL-40 / future Epic with the App user model — live current-row Gate readiness and live DB Reader success remain environment-blocked; not close blockers for HDE-EPIC040. Their later owner/re-homing route is retained without allocating a new ID, inventing a live PASS, or changing the Separation inventory.
```

Replacement:

```text
DEFERRED → HDE-COAG003.8 and HDE-COAG003.9 in PF09.7-Canon-HDE-Build-Checklist-Coagulation / future Epic with the App user model — live current-row Gate readiness and live DB Reader success remain environment-blocked; not close blockers for HDE-EPIC040. No live PASS is recorded, and this row's Conjunction burden is unchanged by the re-homing.
```

### PF09.5 — `PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.md`

#### R5-1 — Front matter: version, effective date, update gate.

**REPLACE**, base line 7.

Target:

```text
**Version:** v1.6

**Status:** Canon

**Effective date:** 2026-10-09

**Last Update Gate:** BN 13.5; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md
```

Replacement:

```text
**Version:** v1.6.1

**Status:** Canon

**Effective date:** 2026-10-11

**Last Update Gate:** BN 13.5; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md
```

#### R5-2 — Cross-reference: routing statement that the redline makes stale.

**REPLACE**, base line 2467.

Target:

```text
HDE-SEPA005.5's remaining re-homing condition belongs to **PF09.3-Canon-HDE-Build-Checklist-Separation**.
```

Replacement:

```text
HDE-SEPA005.5's re-homing condition is resolved in **PF09.3-Canon-HDE-Build-Checklist-Separation**: the two live observations are carried by HDE-COAG003.8 and HDE-COAG003.9 in **PF09.7-Canon-HDE-Build-Checklist-Coagulation**.
```

### PF09.7 — `PF09.7-Canon-HDE-Build-Checklist-Coagulation-v1.1.6.md`

#### R7-1 — Front matter: version, effective date, update gate.

**REPLACE**, base line 7.

Target:

```text
**Version:** v1.1.6

**Status:** Canon

**Effective date:** 2026-10-09

**Last Update Gate:** BN 13.5
```

Replacement:

```text
**Version:** v1.1.7

**Status:** Canon

**Effective date:** 2026-10-11

**Last Update Gate:** BN 13.5; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md
```

#### R7-2 — HDE-COAG003.8: accept the re-homed readiness observation.

**REPLACE**, base line 1278.

Target:

```text
The inventory is read-only, value-minimized, deterministic, and fail-closed. Read-only inventory is PR/tooling work; any refresh is PO-only execution, IA-guided, and no request-time vendor or scorer fallback is permitted.
```

Replacement:

```text
The inventory is read-only, value-minimized, deterministic, and fail-closed. Read-only inventory is PR/tooling work; any refresh is PO-only execution, IA-guided, and no request-time vendor or scorer fallback is permitted.

This row also carries the live, read-only Gate-readiness observation against current user-bound rows that HDE-EPIC040 deferred, re-homed from HDE-SEPA005.5 in PF09.3-Canon-HDE-Build-Checklist-Separation. HDE-EPIC040 delivered the command and proved its refusals offline; the live observation is not proved.

DEFERRED → future epic with the App user model — persistent user-bound BodyGraph rows do not exist in pre-Glow production (HDE-COAG005), so the user-bound live observation cannot yet run; not a close blocker for HDE-EPIC040.
```

#### R7-3 — New subtask HDE-COAG003.9 before the HDE-COAG004 heading (closes PF09 gap G-1); the heading itself is unchanged.

**REPLACE**, base line 1280.

Target:

```text
## **Task HDE-COAG004— Stateless JSON QA mode (non-gating tracker)**
```

Replacement:

```text
### **Subtask HDE-COAG003.9 — User-bound live Reader success verification**

**Subtask name/label:** User-bound live Reader success verification

**Subtask description:**  
After an authorized Magic10 deployment (HDE-COAG003.7) and verified Gate-complete current rows (HDE-COAG003.8), verify Reader v1 and Reader v2 success over live HTTP on the deployed service for real user-bound current rows. Each success response must conform to its governed Reader schema, remain bands-only and numeric-free, carry the admitted release identity, and use no request-time vendor call, scorer fallback, or write.

**Subtask status:** **Not done**

**Dependencies / integration:** HDE-COAG003.7; HDE-COAG003.8; the App user model with persistent user-bound BodyGraph rows, which also ends the HDE-COAG005 interim no-user posture.

**Evidence / artifacts:**  
Secret-safe live request and response captures at the paths assigned by the owning future epic's approved QA Plan or Ops Task Record. This row creates no evidence family, schema, or path home.

**Notes:**

Origin: the AC040-09 live success path of HDE-EPIC040, deferred as blocked by environment and recorded as a PF09 gap by the HDE-EPIC040 CL-40 gap scan (G-1). HDE-EPIC040 QA proved Reader v1/v2 success in-process with injected rows and Reader refusal paths over loopback HTTP; it proved nothing about live DB success or the deployed service. Live execution is Product Owner-authorized, and Mechanics and QA must not create app-like user records in production (HDE-COAG005).

DEFERRED → future epic with the App user model — persistent user-bound BodyGraph rows do not yet exist; not a close blocker for HDE-EPIC040.

## **Task HDE-COAG004— Stateless JSON QA mode (non-gating tracker)**
```

## 5. Validation

A script held every item above as data and checked it against the four base files:

- every target occurs exactly once in its file;
- no two targets overlap;
- all items apply in one pass.

It printed no problems. A second script then parsed the fenced blocks of this document itself, re-applied them to the base files, and produced the same hashes, so the text here is what was checked. The applied files, with the 2026-10-11 date, hash as follows. These are the old file names with the new content; renaming does not change the hash.

| File | Items | Applied SHA-256 |
| --- | --- | --- |
| `PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.7.md` | R3-1, R3-2, R3-3, R3-4, R3-5, R3-6, R3-7, R3-8 | `3f1f7c429c8de9df5c87ea680adf899e5206affc058ced47664a42f328667266` |
| `PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md` | R4-1, R4-2, R4-3 | `65d4b9e2a1303638cc5c66a1d02f55c721509559d24ee8e42cb04a793750ac84` |
| `PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md` | R5-1, R5-2 | `0273d70c3afa49fa6408179a2049e4c06d15cb23fee94109d152c037a6d2c279` |
| `PF09.7-Canon-HDE-Build-Checklist-Coagulation-v1.1.7.md` | R7-1, R7-2, R7-3 | `49cca9569c3d45e5455178c5daaed0f02c504d2feef2ce495cc421512c0aac5c` |

To check by hand, `sha256sum` each applied file before committing. A mismatch with the date unchanged means an item was missed or mistyped.

## 6. Not in this redline

- **Dated records outside PF09.** HDE Mechanics Guide (§25.6 Gate-kernel comparison and current-row readiness), Glow QA Guide (HDE-EPIC040 history, "Later evidence landing and controlling closure") and HDE Phased Epics (HDE-EPIC040 C1 tables) describe the state at closure: .5 Partial and re-homing pending. They are records of that time and are not made false by a later PF09 update, so no change is proposed. Their owners may align them if they want.
- **PF09.4 HDE-EPIC040 Reader evidence note** ("live DB Reader success still environment-blocked") stays true and is unchanged.
- **The `--allow-prod-vendor` gap** stays with the PF05 and CLI owners. It is not touched.
- **HDE-CRD-0002** is not entered in PF30.1-Canon-HDE-CRD-Records by this redline. R3-6 says only that the PO accepted the items for CRD drafting.

## Canon relied on

Read on `main` at `1ea6a262`:
- PF06-Canon-Change-Process-Guide v2.5.4: §0.2 Policy and principles (PF09 gap; future work must be PF09-accounted); §0.6.10 Redline bundle construction discipline.
- PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.6: §0.3 Task, Status, and Deferral Conventions; §0.4 "Epic and CRD boundary"; §0.6 Completion Standard; Phase III notes; HDE-SEPA005 and HDE-SEPA005.5.
- PF09.4-Canon-HDE-Build-Checklist-Conjunction v1.3: HDE-CONJ010.4 and HDE-CONJ010.6 DEFERRED lines; the HDE-EPIC040 Reader evidence note.
- PF09.5-Canon-HDE-Build-Checklist-Fermentation v1.6: the HDE-EPIC040 QA-120 later record.
- PF09.7-Canon-HDE-Build-Checklist-Coagulation v1.1.6: HDE-COAG003 and its subtasks .5 to .8; HDE-COAG005 interim no-user posture.
- PF14-Canon-HDE-Mechanics-Guide v3.5.8, PF19-Canon-Glow-QA-Guide v3.0.6 and PF20-Reference-HDE-Phased-Epics v1.9.6: the HDE-EPIC040 passages listed in §6.
- PF21-Reference-7 Phases of Alchemical Engineering: §4 Conjunction (combine into a working whole); §7 Coagulation (solidify into a durable product and platform).
- PF30.1-Canon-HDE-CRD-Records v0.9: §3.1 CRD ID syntax (`HDE-CRD-<NNNN>`).
- PF10-HDE-Build-Notes v13.5.1: no rule on this re-homing found.
- `AGENTS.md`: canon is read-only unless the prompt directs a change, so this is a proposal for manual application.

In-flight documents:
- `docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` (#602, at its PR head): G-1 and F-2.
- `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.1.md` (#601, at its PR head).
- `docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md`: §7.2 and AC040-09 rows, §14.
- `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`.

Repository: `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json`, for `release_id` in success responses (R7-3).
