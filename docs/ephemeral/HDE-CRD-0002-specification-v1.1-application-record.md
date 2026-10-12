---
artifact_type: CRD_SPECIFICATION_REDLINE_APPLICATION_RECORD
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION-V1.1-APPLICATION-RECORD
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
revision_mode: PREAPPROVAL_REVISION
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
reviewer: Thoth, CF-C-30 (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
prompt: CF-C-40 — Revise CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-12T19:33:53Z
repository_head_read: origin/main 6af9c765
denied_artifact: docs/ephemeral/HDE-CRD-0002-specification-v1.0.md (v1.0, blob fcdd116b, SPECIFICATION_PENDING)
review_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.0.md (INITIAL_DENY, 2026-10-12T19:24:01Z, #616)
revised_artifact: docs/ephemeral/HDE-CRD-0002-specification-v1.1.md (v1.1, SPECIFICATION_PENDING, "ASK OK?")
---

# HDE-CRD-0002 — Specification v1.1 application record

This record lists, item by item, how Specification v1.1 applies Thoth's review v1.0. It approves nothing. Specification v1.1 is pending with `ASK OK?` and returns to CF-C-30 for the same reviewer, Thoth. No PF10 addendum is created.

## 1. Required redlines

| # | Redline (review v1.0 §3) | Applied | Where in v1.1 | How |
| :- | :- | :- | :- | :- |
| R1.1 | Rewrite Exclusions bullet 5 so it does not exclude the bounded open-rails Live QA (including the synthetic-data live vendor call) or a Product Owner-authorized deployment or Ops task that places the QA candidate | Yes | Exclusions, bullet 5 | Restated as implementation-only: "As implementation work: no deployment, no production configuration change, and no live vendor call made by an implementation work unit." It then states that it excludes neither (a) the Live QA of Glow QA Guide §3.5.5 and Change Process Guide §1.1.5A, including the synthetic-data live vendor call, nor (b) a Product Owner-authorized deployment or Ops task placing the QA candidate. The `APP_ENV=prod` sentence is kept |
| R1.2 | Under QA requirement, state that the production-affecting Live QA minimum applies, and identify which requirements touch a production-functional surface, or say none with the basis | Yes | Canon, QA & Build Notes posture → new "Production-affecting Live QA minimum" bullet with a four-row classification table | States that the minimum applies, with the open-rails step and the synthetic-data live vendor call. Classifies every requirement: functional-feature scope (S14, S02, S10, S07, S08, and S15 where it removes a route), with surface and basis for each; production-affecting outside that scope (S01, with the exemption route if the deployed build does not install the distribution); S19 inheriting the class of the surface each fix changes; and not production-affecting (all others), with the basis. Consequential edits: Expected outcome names the Live QA minimum; Affected surfaces → operations names the QA-placement deployment or Ops task; a new **Live QA** constraint; the lineage line on Ops notes the same |
| R2.1 | Replace CD-3's "Not observed" with the verified fact | Yes | Compatibility dependencies, CD-3 | Re-read on `main` at `6af9c765`: `tools/evidence/update_evidence_index.py` lines 47 to 51 (`CRD_QA_ID`, `CRD_QA_ROOT_REL`, `CRD_QA_KEY` for HDE-CRD-0001, and the comment "another CRD needs its own explicit admission"); no other `.py` or `.sh` file under `tools/`, `ci/`, `engine/`, `adapter/` or `schemas/` names HDE-CRD-0001; `tools/qa/qa_harness.py` line 23 accepts any `HDE-CRD-[0-9]{4,}`. The source column cites HDE Schemas & Artifacts §8.17 "Change-container identity", Plan Templates §2A and `AGENTS.md` |
| R2.2 | Give CD-3 a treatment that guarantees admission before QA, preserving existing inputs: an in-scope requirement in a phase block, or a named lane and owner | Yes — in-scope requirement | New requirement S22; CD-3 treatment; Distillation block | S22: "Extend the canonical evidence-index updater's CRD admission to HDE-CRD-0002's QA root". Acceptance intent: before QA, the updater publishes and validates Index and Mirror entries for `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate. Placed in Distillation, with the dependency "S22 completes before HDE-CRD-0002 enters QA". Consequential edits: Observed need, warrant, Affected surfaces, Lead Developer finding (lane basis for S22), Bounded scope and Expected outcome now say S01 to S22; a **QA evidence admission** constraint; the QA requirement says QA evidence is published by the updater once S22 holds; the recommended ordering puts S22 before QA |
| R3 | Make S16's scope and acceptance intent state the same bound | Yes — the source-backed bound, `GEO_API_KEY` | Requirements, S16 | The acceptance intent is replaced with the reviewer's exact text: "`.env.example` has a `GEO_API_KEY` entry". The scope is unchanged. S16 is not widened |
| R4.1 | Exclusions bullet 2 becomes "No release re-cut beyond what the in-scope requirements require." | Yes, verbatim | Exclusions, bullet 2 | — |
| R4.2 | Replace the Release members constraint's first sentence with the verified fact; keep the convergence sentence | Yes | Constraints → Release members | Re-verified on `main` at `6af9c765`: `catalog/manifest.json` has 45 members. `engine/cli/main.py` (S07 line 79, S08 line 131, S14 line 138), `engine/bodygraph/resolver.py` (S14) and `adapter/http_reader.py` (S10 line 603) are members; `pyproject.toml` (S01) and `adapter/factory.py` (S02) are not. The text states that any requirement changing a member forces the re-cut and new admission pins, that the Implementation Audit establishes the actual set, and keeps the convergence sentence. Consequential edits: the Conjunction and Fermentation dependency cells name S07, S10, S08 and S14 by observed locus instead of S02 |

## 2. Non-gating notes

| # | Note (review v1.0 §4) | Applied | Where in v1.1 |
| :- | :- | :- | :- |
| N1 | Cite Change Process Guide §0.1A, not §0.1 | Yes | Format and register posture; U-7; Canon relied on |
| N2 | Add the affected requirements, alternatives and unresolved risk fields to the canon conflict register | Yes | Canon conflict register: each entry now has those three fields. The table became per-entry field lists so the added passages stay readable |
| N3 | Attribute 129 to PR05 | Yes | Why warranted ("129 test files ran in no CI lane at HDE-EPIC040 PR05 (O-11; not recounted, U-1)"); U-1 |
| N4 | State whether S21's evidence home lies inside an existing family or is admitted by S21's ADR | Yes | S21 acceptance intent ("inside an existing evidence family or in one S21's ADR admits"); Exclusions bullet 3 now excepts only that home, admitted by S21's ADR |
| N5 | Record the CLI/API/Vendor Ref §7.1.11e initiator limit | Yes | New **Override initiator** constraint; S14 acceptance intent adds "authorized initiator"; the Live QA classification refers to that constraint |
| N6 | The Notion board card is stale | Not applied — outside this artifact | Review v1.0 records it as record currency for its owner. This session writes no Notion row (CF-C-40 writes only under `docs/ephemeral/`) |

## 3. Canon conflict dispositions (review v1.0 §6)

| ID | Thoth's status | Reviewer's exact change | Applied in v1.1 |
| :- | :- | :- | :- |
| CR-1 | `APPROVED_AS_CHANGED` | Add Change Process Guide §0.1, §0.1A, §1.0 heading, §1.0.4 and §1.0.6 passages; Plan Templates §2A passages; PF30.1 §2 "Implementation MUST NOT begin before CRD Plan approval" | Yes: every listed passage is in the Conflicting sources field, quoted as the review lists it, and the drainage target names each aligned section. Status recorded as `APPROVED_AS_CHANGED`, confirmation against v1.1 pending |
| CR-2 | `APPROVED_AS_CHANGED` | Add Plan Templates §2A "Alchemical phase separation" | Yes, quoted; drainage target covers both passages. Status as above |
| CR-3 | `APPROVED_AS_CHANGED` | Add HDE Schemas & Artifacts §8.17 "Change-container identity"; HDE-SEPA005 note at line 1170 | Yes: §8.17 added to Conflicting sources, CD-2 and the drainage target; line 1170 recorded. Status as above |

Reviewer identity, decision time and the shared unresolved risk are carried from review v1.0 §6.

## 4. Preserved without change

Per CF-C-40 Execute step 1: change ID and class, author Isis and reviewer Thoth, the CRD primary-source warrant, and every requirement and exclusion the review did not reach. Unchanged: S01 to S13, S15, S17 to S20; Exclusions bullets 1, 4 and 6 to 11; the constraints other than Release members; CD-1; RD-1; record control (except the note on Last material update); continuity; phase purposes and completion boundaries (except the S22 additions); canon impact and drainage targets for S21 and S14; U-2 to U-6. Wording changes outside R1 to R4 and N1 to N5 are limited to the consequential edits named above, and to these:

- the Specification approval block names v1.1 and records the v1.0 denial;
- the lineage section records the decisions;
- a new "Pre-approval revision history" table;
- front-matter fields for the revision;
- the TypeSafe reading for the CF-C-30 re-review;
- Canon relied on.

## 5. Facts re-verified for this revision

On `main` at `6af9c765`:

- no file outside `docs/` changed between `2aed56f1` and `6af9c765`;
- the only `docs/pfcanon/` change between those heads is PF30.1 v0.9.1 (#614);
- R2: `tools/evidence/update_evidence_index.py` lines 40 to 60; a search of `tools/`, `ci/`, `engine/`, `adapter/` and `schemas/` for HDE-CRD-0001; `tools/qa/qa_harness.py` line 23;
- R3: `.env.example`; `engine/providers/vendor_http_hdapi.py` lines 55 to 75;
- R4: the `catalog/manifest.json` member list; `engine/cli/main.py` lines 79, 131 and 138; `adapter/http_reader.py` line 603;
- R1: `Procfile` (production app `adapter.factory:create_app()`); PF19 §3.5.5 and PF06 §1.1.5A; PF05 §7.1.11e.

## 6. Unresolved items and owners

- **S01 production-build path:** whether the deployed build installs the distribution is not observable in the repository. Owner: the Implementation Audit; the QA Plan applies the recorded exemption route only if it does not.
- **CR-1 to CR-3 canon drainage:** Product Owner.
- **N6 Notion board card:** its owner (Product Owner or Master Scrum).
- **S21 ADR:** not yet drafted. Product Owner-owned; an agent may draft it.
- **Specification approval:** Thoth at the CF-C-30 re-review.

## TypeSafe reading

Recorded in Specification v1.1, "TypeSafe reading for the receiving session (CF-C-30 re-review)".

## Canon relied on

As listed in Specification v1.1, "Canon relied on". Those re-read for this revision on `main` at `6af9c765`:

- PF06-Canon-Change-Process-Guide v2.5.4 §1.1.5A;
- PF19-Canon-Glow-QA-Guide v3.0.6 §3.5.5 "Production-affecting Live QA minimum";
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.17 "Change-container identity (normative)";
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11e.

In-flight documents: review v1.0 and Specification v1.0, both read in full. Prompt: CF-C-40 — Revise CRD Specification — 100926.1.
