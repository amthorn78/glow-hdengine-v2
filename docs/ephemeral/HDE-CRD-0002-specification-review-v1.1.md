---
artifact_type: CRD_SPECIFICATION_REVIEW
artifact_version: "1.1"
logical_id: HDE-CRD-0002-SPECIFICATION-REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: INITIAL_SPECIFICATION_REVIEW (re-review after CF-C-40 PREAPPROVAL_REVISION)
decision: INITIAL_APPROVE
reviewed_artifact: docs/ephemeral/HDE-CRD-0002-specification-v1.1.md
reviewed_artifact_version: "1.1"
reviewed_artifact_blob: 8a3ef0a8930dcb6f610235ee84d68882bfaa80e1 (41,824 bytes; landed on main at fd47cab, amthorn78/glow-hdengine-v2#617)
application_record: docs/ephemeral/HDE-CRD-0002-specification-v1.1-application-record.md
approved_representation: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK.")
predecessor_review: docs/ephemeral/HDE-CRD-0002-specification-review-v1.0.md (INITIAL_DENY on v1.0)
reviewer: Thoth, CF-C-30 (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum; same reviewer as review v1.0)
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
prompt: CF-C-30 — Review and Approve CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-12T19:39:51Z
repository_head_read: origin/main fd47cab
pf10_addendum: none (initial approval; CF-C-30 step 2)
next_prompt: IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0)
next_mode: FIRST_ENTRY
next_actor: whole-change Implementation Agent (IA) for HDE-CRD-0002; session NOT_YET_ASSIGNED
---

# HDE-CRD-0002 — Specification review v1.1 (CF-C-30)

## 1. Decision

**INITIAL_APPROVE.** Thoth approves HDE-CRD-0002 Specification v1.1, authored by Isis, exactly as reviewed. That is the file at `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md`, blob `8a3ef0a8…`. It is the S01–S22 planned baseline. The approval ends the Specification with `ASK OK.`

v1.1 is an issued version and is not edited. The approved representation, `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, is v1.1 with the approval metadata filled in (§5). It is the artifact IA-10 consumes.

This decision creates no PF10 addendum. It authorizes the Implementation Audit and Implementation Plan preparation (HDE Governance §9.1.1). It authorizes no implementation, PR Proceed, Ops, QA, canon change, ADR approval, acceptance or closure.

## 2. Required redlines from review v1.0: applied

| # | Required correction | v1.1 | Finding |
| :- | :- | :- | :- |
| R1.1 | Exclusion must not exclude the bounded open-rails Live QA, the live vendor call, or a PO-authorized deployment or Ops task that places the QA candidate | Exclusions bullet 5 restated as implementation-only, with both carve-outs explicit | Applied. Consistent with Glow QA Guide §3.5.5 and Change Process Guide §1.1.5A |
| R1.2 | State that the production-affecting Live QA minimum applies, and identify the affected surfaces | New "Production-affecting Live QA minimum" bullet with a four-class surface table covering all of S01–S22 | Applied. The functional-feature class is drawn inclusively (S14, S02, S10, S07, S08, and S15 route removal). That is within the Specification's identification role, and it adds no QA step beyond the one mandatory live vendor call. The not-production-affecting class checks out against the §3.5.5 surface list |
| R2.1 | Replace CD-3's "Not observed" with the verified fact | CD-3 restated with `update_evidence_index.py` lines 47–51 and the `qa_harness.py` line 23 fact | Applied. Re-verified on main `fd47cab`: no `.py`, `.sh` or `.json` file under `tools/`, `ci/`, `engine/`, `adapter/` or `schemas/` except `tools/evidence/update_evidence_index.py` names HDE-CRD-0001 |
| R2.2 | A treatment that guarantees admission before QA, preserving existing inputs | New S22, in Distillation, with the dependency "S22 completes before HDE-CRD-0002 enters QA"; CD-3 resolved by S22; QA evidence admission constraint added | Applied. This is a canon-permitted treatment (Plan Templates §2A; HDE Schemas & Artifacts §8.17). The acceptance intent preserves Epic and HDE-CRD-0001 inputs. The lane basis for S22 is stated |
| R3 | S16's scope and acceptance intent state one bound | Acceptance intent is the review's exact text: "`.env.example` has a `GEO_API_KEY` entry" | Applied verbatim |
| R4.1 | Exclusion: "No release re-cut beyond what the in-scope requirements require." | Exclusions bullet 2 | Applied verbatim |
| R4.2 | Replace the Release-members first sentence with the verified fact | Constraint restated; phase-block dependency cells now name S07, S10, S08 and S14 by observed locus | Applied. Matches the verified member set on main |

## 3. Non-gating notes and other changes

- **N1–N5:** applied as the application record states. Each was checked in v1.1: the §0.1A citation; the register's added fields; "129 at PR05"; S21's evidence-home carve-out (now consistent with Exclusions bullet 3); and the Override initiator constraint.
- **N6:** correctly left outside the artifact, since CF-C-40 does not write to Notion. The Notion board card for HDE-CRD-0002 is still stale for its owner.
- **Unannounced changes:** none. A line diff of v1.0 against v1.1 shows only the changes the application record lists: the redline and note edits, their stated consequential edits, revision metadata, the revision history table, the TypeSafe reading and Canon relied on. No unaffected requirement, exclusion, constraint, CD-1, RD-1 or phase purpose changed.
- **Lead Developer facts:** re-verified on main `fd47cab`. Between `d86b8850` and `fd47cab`, the only file changed outside `docs/` is `AGENTS.md`.
- **New non-gating observations (no correction required):**
  - **M1.** The S01 row says the QA Plan may exempt S01 "with a recorded basis". Glow QA Guide §3.5.5 also requires that exemption to be authorized and to state the production claim not made and the follow-up. The QA Plan is bound by §3.5.5 as written, so nothing in the Specification needs to change.
  - **M2.** S07, the help-text change, is classified inclusively in the functional-feature class. This has no consequence, because one live vendor call satisfies the class.

## 4. Canon conflict register: confirmed against v1.1

| ID | Status | Confirmation |
| :- | :- | :- |
| CR-1 | `APPROVED_AS_CHANGED` (review v1.0 §6), confirmed | All passages the review listed are present in Conflicting sources, together with the original §1.0.3 and PF30.1 passages. The drainage target names each section. Interim treatment unchanged |
| CR-2 | `APPROVED_AS_CHANGED`, confirmed | The Plan Templates §2A "Alchemical phase separation" passage is present. Drainage covers both passages |
| CR-3 | `APPROVED_AS_CHANGED`, confirmed | HDE Schemas & Artifacts §8.17 is present in Conflicting sources, CD-2 and the drainage target. The HDE-SEPA005 note is recorded at line 1170. The affected requirements (S21, S22) are correct |

- **Reviewer:** Thoth, CF-C-30, session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum.
- **Reviewed artifact:** v1.1.
- **Decision time:** 2026-10-12T19:39:51Z.
- **Scope of the dispositions:** interim treatments and drainage routing only. Drainage stays with the Product Owner, and no canon is changed.
- **Carried state:** the register is carried in the approved representation for IA-10.

## 5. Approved representation

- **Path:** `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`.
- **Source:** v1.1 byte for byte, except the publication delta its front matter declares:
  - front-matter `state` becomes `SPECIFICATION_APPROVED` and `approval_sentinel` becomes `"ASK OK."`, with the approval fields added;
  - Record control: `CRD status` becomes `Plan Approved` (the PF30.1 §3.3 value, under the Specification's own "CRD Plan approval" mapping), and `Last material update` becomes `2026-10-12`;
  - the Specification approval block records `Approved`, the date, the approver and this decision as its source;
  - one Material-change history row (PF30.1 §3.3 and §4.2: a status change is material);
  - the "Specification decisions" lineage line;
  - the three CR status lines.
- **Diff check:** a line diff against v1.1 shows only those lines.
- **Unchanged:** Isis's text, including its pending-tense author wording, is preserved verbatim. Phase-block statuses stay `Planned`.

## 6. Next state and routing

- **Specification:** approved; v1.1 baseline; `ASK OK.`
- **Next:** IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1, `FIRST_ENTRY`.
  - Receiver: the whole-change Implementation Agent for HDE-CRD-0002.
  - IA session binding: `NOT_YET_ASSIGNED`; the Product Owner assigns it at launch.
  - Isis reviewer binding for IA-30: established. Isis authored this Specification in session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; IA-30's reviewer session may be assigned at that boundary.
  - IA-10 resolves its own current PF canon and PF10 sources.
- **PF10 addendum:** none.

## 7. TypeSafe reading for the receiving session (IA-10)

Action sent (v6): "Create, as the first Implementation Agent artifacts for a newly approved 42 KB CRD Specification of 22 scope requirements (packaging, the production HTTP adapter, CI coverage across about 129 uncovered test files, CLI fixes, a canon production vendor-override contract with audit, a code security review of four merged PRs, evidence-index admission and close-pack tooling with a canon ADR), a whole-change Implementation Audit that inspects the repository against every requirement, then a separate initial Implementation Plan with ordered PR and Ops work units across four phase blocks and one coordinated release re-cut. No code is written and no live run occurs; an independent reviewer approves or redlines the Plan before any implementation."

- **TypeSafe v6: Fable 5.1, max.** Effort score 3.94 (confidence 0.81); rung probabilities low 0.00, medium 0.00, high 0.04, extra high 0.09, max 0.75, ultracode 0.12. Model probabilities Fable 5.1 0.73, Opus 5.5 0.27 (confidence 0.46). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.00, Opus 5.5 at high 0.01, Opus 5.5 at extra high 0.02, Opus 5.5 at max 0.20, Opus 5.5 at ultracode 0.03, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.03, Fable 5.1 at extra high 0.07, Fable 5.1 at max 0.55, Fable 5.1 at ultracode 0.09. Sent 2026-10-12T19:39:51Z. Flags: none.
- **Nathan's pick for IA-10:** not stated.
- **Nathan's pick for this CF-C-30 re-review:** not stated (reading recorded in Specification v1.1).

**Surface advice:** run IA-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. It needs repository read access, including the test suite and CI classifier for S03–S05 and `catalog/manifest.json` with `engine/config/registry_loader.py` for the re-cut. It writes only the Audit and Plan under `docs/ephemeral/`. It makes no live vendor or production call.

## Canon relied on

Canon on `main` is unchanged since review v1.0. The last `docs/pfcanon/` commit is `df23bbf` (#614), and `git diff --stat df23bbf fd47cab -- docs/pfcanon` is empty. The sections read in full for review v1.0 therefore stand; they are listed in that review's "Canon relied on". For this decision, each topic maps to the following sections.

- **Approval authority, exact-artifact approval, and what approval authorizes:** PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (role table; "Approval applies to the exact artifact reviewed"; the approved Specification "authorizes the required Implementation Audit and Implementation Plan preparation, not implementation"); §9.1.2 (conflict precedence for CR-1 to CR-3).
- **R1 application:**
  - PF19-Canon-Glow-QA-Guide v3.0.6 §3.5.5 "Production-affecting Live QA minimum" (lines 1352–1370) and "Change-lane QA applicability (normative)";
  - PF06-Canon-Change-Process-Guide v2.5.4 §1.1.5A and §0.1A;
  - PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11e (Override initiator).
- **R2 application and S22:** PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.17 "Change-container identity" (lines 5266–5280); PF27-Canon-Plan-Templates v2.0.5 §2A "Existing-template reuse and substitution".
- **R3 and R4 application:** PF04 §9.1.1 (no IA expansion); `AGENTS.md` "Release identity" and the HDE-EPIC040 current posture (45 members; admission pins).
- **Format and the approved representation's status values:** PF30.1-Canon-HDE-CRD-Records v0.9.1 §3.3 (`Plan Approved`; a status change is material), §4.1, §4.2 (material-change row) and §7; PF06 §0.1A "Specification format authority".
- **Materiality of M1 and M2:** PF27 "Materiality-based blocker discipline".
- **PF10:** PF10-HDE-Build-Notes v13.5.2 is unchanged and holds addendum 2.1 only, which governs the TypeSafe reading in §7. PF10 is silent on this change's subject matter.

**In-flight documents read in full for this decision:**

- `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-v1.1-application-record.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-review-v1.0.md` (own predecessor);
- `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md`, compared by line diff.

**Prompts read:**

- CF-C-30 — Review and Approve CRD Specification — 100926.1;
- IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1, for its FIRST_ENTRY contract.

## 8. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / CF-C-30 / initial review 2 (re-review) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md`, v1.1 (approved) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | CF-C-30 — Review and Approve CRD Specification — 100926.1, https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8 |
| role/stage | Thoth / CF-C-30 initial Specification review, re-review |
| capture time | 2026-10-12T19:39:51Z |
| execution identity | https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| repository persistence | Pending: recorded here only, as in review v1.0 |
