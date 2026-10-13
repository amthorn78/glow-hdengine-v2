---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-PR-01-PO-DISPOSITION-CR-4-CR-5
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
decision_owner: Nathan / Product Owner
decided_at: 2026-10-13, in the session that produced the lineage review below, after its report (recorded 2026-10-13T12:52:25Z)
recorded_by: the continuing whole-change HDE-CRD-0002 Implementation Agent, PR-40 role, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (recorder only; the decisions are the Product Owner's)
decides: CANON_CONFLICT_REGISTER entries CR-4 and CR-5 as proposed in docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v1.0.md §9 (v1.0, decision REJECT; blob 2cfbb5ec33d8d6ba06bc72a029f695d1630fd46a)
lineage_review_unchanged: yes (v1.0 is not edited; its REJECT and §10 bounded correction stand)
pf10_addendum_created: none
---

# HDE-CRD-0002 WU-PR-01 — Product Owner disposition of CR-4 and CR-5 (v1.0)

## 1. Product Owner's words (verbatim)

> "I accept your recommendation for CR-4. For CR-5 I will reserve the right to assign such things as I see fit."

## 2. CR-4 — PO-D4 versus the addendum 2.2 rescope-lane route

- **Decision: APPROVED.** The Product Owner accepts the recommended disposition, alternative (a). PO-D4 is confirmed as the Product Owner's own bounded decision for exactly R-14: the R-14 helper shape is recorded as a limit with no code change.
- **Effect.** For R-14 only, PO-D4 stands in place of the rescope-lane route in PF10 addendum 2.2 "Binding requirements". `AGENTS.md` and PF04-Canon-HDE-Governance §9.1.2 provide that a formally approved bounded Product Owner decision governs for the exact decision it adjudicates. This record is that formal approval. No other bypass shape is covered by it.
- **What does not change.**
  - The landed analyzer stands.
  - R-14 remains an analyzer limit owned by the whole-change IA (OBS-16).
  - Addendum 2.2's rescope-lane route still governs every other case.
  - The lineage review's REJECT and its bounded correction are unaffected; R-14 was already outside that correction.
- **Unresolved risk closed.** The lineage review recorded PO-D4's authority as agent-recorded only. That gap is closed by the Product Owner's words above.

## 3. CR-5 — canon replacement inside an implementation PR

- **Decision: APPROVED_AS_CHANGED.**
- **Original proposal (lineage review v1.0 §9):** "(a) for this case. For later units, state the preferred vehicle." Alternative (a): PF04 §9.1.2 exact Product Owner authority governs, and the landed change stands. Alternative (b): such replacements go in a separate PR or a direct-main change.
- **Product Owner's change:** "I will reserve the right to assign such things as I see fit."
- **Reading recorded:**
  - The Product Owner assigns the vehicle for a canon replacement case by case, under exact authority for the identified document and action.
  - No standing vehicle rule is set.
  - The PF10 v13.5.4 replacement in #627 was such an assignment (PO-D3), so the landed change stands.
- **What does not change.**
  - PF06-Canon-Change-Process-Guide §0.2 and PF04 §9.1.2 are not edited.
  - Drainage of their difference stays with the Product Owner.
  - Agents still edit PF canon only under the Product Owner's exact direction for the identified document and action (`AGENTS.md`).
- **Residual fact carried:** a revert of `7136040` would also remove PF10 v13.5.4 and addendum 2.3. Any such revert is the Product Owner's to direct.

## 4. Register state after this disposition

| ID | Status | Decision owner | Reviewed artifact |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED (unchanged) | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Nathan / Product Owner | lineage review v1.0 §9 |
| CR-5 | APPROVED_AS_CHANGED | Nathan / Product Owner | lineage review v1.0 §9 |

The register is carried forward by the corrective WU-PR-01 plan (PR-20) and its results.

## Canon relied on

- PF04-Canon-HDE-Governance v2.8.7 §9.1.2: canon precedence; exact Product Owner authority for canon edits; Product Owner dispositions govern within their scope.
- PF06-Canon-Change-Process-Guide v2.5.4 §0.2: implementation agents and PF-Canon edits.
- PF10-HDE-Build-Notes v13.5.4, addendum 2.2: Approved delta item 2 and Binding requirements.
- `AGENTS.md`: canon-first rule; a formally approved bounded Product Owner rescope; PF canon is read-only unless directed.
- All were read on `main` at `7136040` for the lineage review; `docs/pfcanon/` is unchanged since (`origin/main` is still `7136040`).

**In-flight documents read:**
- `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v1.0.md` (§6 LR-4 and LR-5, §8, §9);
- `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.9.md` §5 (PO-D3, PO-D4);
- `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.6.md` §4 (PO-D3 wording, as cited in the lineage review).
