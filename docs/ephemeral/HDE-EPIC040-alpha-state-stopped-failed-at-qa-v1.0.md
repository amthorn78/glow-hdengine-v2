---
artifact_type: ALPHA_STATE_RECORD
artifact_version: "1.0"
change_id: HDE-EPIC040
alpha_state: ALPHA_STOPPED_FAILED_AT_QA
resume_point: QA-70 — Review Whole-Change QA Plan
recorded_date: 2026-09-27
authority: Product Owner instruction, 2026-09-27
supersedes_state: ALPHA_RESUMED (decision D18, 2026-09-21)
---

# HDE-EPIC040 — Alpha state: ALPHA_STOPPED_FAILED_AT_QA

## Canon relied on

* Decision D18 and its 2026-09-23 successors in `docs/prompt_ecosystem_management/gcfpe.decision-record.md`: Alpha state is whatever the Epic's own artifacts under `docs/ephemeral/` record, landed by pull request. No Notion page holds it.
* `docs/prompt_ecosystem_management/authoritative-surfaces.md`, "Superseded for Alpha state".
* The QA stage failure record: `docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md`.

## State

**`ALPHA_STOPPED_FAILED_AT_QA`.** The GCFPE Epic Alpha for HDE-EPIC040 is halted: it failed at QA.

* **What failed:** QA-70 approved QA_PLAN v1.0, and that approval was wrong. The Plan's rails model contradicted canon: it mixed `SAFE_MODE=0` with `ALLOW_NETWORK=0`, set rails per command, and included live database checks that need users who do not exist before the App. The Product Owner rejected the approval on 2026-09-27. The execution of checks 1–10 under QA-100 (evidence commit `06b04a9`) inherited those defects.
* **Root cause:** the reviewer did not read the governing canon (RCA v1.1).

## Token

`ALPHA_STOPPED_FAILED_AT_QA` is minted here. The existing stop tokens, `ALPHA_STOPPED_PENDING_*`, each name a precondition to wait for. None names a failure at a flow stage. It follows D18's rule of recording a state under a name rather than in prose.

## Resumption

* **Resume point: QA-70.** QA-70 starts over against the current QA Plan. It applies the canon-first rule and produces a "Canon relied on" block that includes the rails sections of the QA Guide and PF10.
* **Not rerun:** everything before QA-70 stands. That covers the Specification v1.1, the Implementation Audit v2.0, the Implementation Plan v2.1, PR01 to PR07 as accepted, OPS01, DOC-20, QA-10, QA-20 and QA-50.
* **Not carried forward:** QA_PLAN_REVIEW v1.0 (rejected), the QA-90 task collection (#537) and the QA-100 checks 1–10 evidence (`06b04a9`). All of it derives from the rejected approval. It stays as historical record and grants no QA verdict.
* **Resuming requires the Product Owner's explicit decision.** Resuming does not authorize QA execution, merge, release promotion or Epic closure.

## Nonclaims

This record establishes no QA verdict, acceptance, OPS result, build-checklist status movement or Epic closure.
