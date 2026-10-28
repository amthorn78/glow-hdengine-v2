---
artifact_type: EPIC_SPECIFICATION_REDLINE_APPLICATION_RECORD
artifact_version: "1.0"
logical_id: HDE-EPIC041-EPIC-SPECIFICATION-V1.1-APPLICATION-RECORD
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
revision_mode: PREAPPROVAL_REVISION
author: Isis (Isis-56; https://claude.ai/code/session_01Q789u35D8uKpsTHJ67oMCz), the same continuing Isis author as v1.0 (Isis-55)
reviewer: Thoth (Thoth-20; https://claude.ai/code/session_01Q789u24G3yiuVFFZofiVfx), CF-E-30
prompt: CF-E-40 — Revise Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb8113a64dda1a380c1b96; page state 2026-10-27T13:17:15.163Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
created_at: 2026-10-28
repository_head_read: origin/main 0891314
denied_artifact: docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md (v1.0, 45,985 bytes, SPECIFICATION_PENDING; preserved unchanged)
review_ref: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md (INITIAL_DENY, redlines RL-1 to RL-7; merged as 0891314, #782)
revised_artifact: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1, SPECIFICATION_PENDING, "ASK OK?")
next_prompt: CF-E-30 — Review and Approve Epic Specification — 102726.1
next_actor: Thoth (same reviewer)
---

# HDE-EPIC041 — Epic Specification v1.1 application record

This record lists, item by item, how Specification v1.1 applies Thoth's review v1.0.

* It approves nothing.
* Specification v1.1 is `SPECIFICATION_PENDING` with `ASK OK?`. It returns to the same reviewer, Thoth, through CF-E-30.
* No PF10 addendum is created.
* v1.0 is preserved unchanged, as a complete replacement requires (HDE Governance §9.1.1).
* No redline was ambiguous, so none was returned to Thoth.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `0891314`. This branch changes nothing under `docs/pfcanon/`.

| Document (title) | Sections read in full | Used for |
| :- | :- | :- |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" | Same author and reviewer; complete replacement; prior artifact preserved |
| HDE Governance | §9.7.7 "Plan approval gate": "Business Case section required (Epic Specifications)"; "Business case for every requirement and work unit" | RL-1 to RL-3 |
| Plan Templates | §2 "Business Case (MUST)" and "Requirement and work-unit business case" | RL-1 to RL-3 |
| Plan Templates | "Canon precedence for template use" | RL-4, RL-5 |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`) | Searched by term: chart loader, `SEPA006`, `get_chart`, business case, application record, redline. No match | Build Notes is silent here, so permanent canon governs |
| Review v1.0 (in-flight) | Whole document | The redlines, and Rulings R-A to R-C |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Blocking redlines

| # | Redline (review v1.0 §3) | Applied | Where in v1.1 | How |
| :- | :- | :- | :- | :- |
| RL-1a | Replace the Problem-statement sentence naming the delivery team and the production operator | Yes, verbatim | §2.1 Problem statement | The replacement text is exact. The sentence after it ("Two defects are observed …") is kept unchanged, as the redline names only the one sentence |
| RL-1b | Insert an **If not done** bullet directly after **Why now** | Yes, verbatim | §2.1, new bullet between Why now and What success looks like | — |
| RL-2 | Replace the R-01 business-case row | Yes, verbatim | §2.4, R-01 row | Beneficiary is the delivery team. Evidence is E-1 and E-2 (E-4 locates the concerns). The Benefit and the Measure, including AC-05, are as written |
| RL-3.1 | §2.4: delete the R-05 row | Yes | §2.4 | — |
| RL-3.2 | §3 requirements table: delete the R-05 row | Yes | §3 | — |
| RL-3.3 | R-01 requirement text: append "No fallback data and no additional Engine I/O carve-out is introduced." | Yes, verbatim | §3, R-01 | A full stop was added to the end of the existing last sentence before the appended one |
| RL-3.4 | R-03 requirement text: append "The migration preserves governed caller output and failure behavior, and applicable CLI/API/Vendor and Mechanics behavior." | Yes, verbatim | §3, R-03 | Same full stop treatment as RL-3.3 |
| RL-3.5 | AC-05 **Binds**: `R-05` to `R-01, R-03, R-04` | Yes | §3, AC-05 | — |
| RL-3.6 | §3: delete the AC-06 row | Yes | §3 | — |
| RL-3.7 | §8 **Workflow and QA evidence**: append the governed-evidence obligation sentence | Yes, verbatim | §8 | — |
| RL-3.8 | §8: "AC-01 to AC-06" becomes "AC-01 to AC-05" in **Governing acceptance scope** and **Evidence proportionality** | Yes, both places | §8 | These were the only two occurrences |
| RL-3.9 | §6 D4 heading: "(HDE-SEPA006.3; R-04, R-05)" becomes "(HDE-SEPA006.3; R-04)" | Yes | §6 D4 | — |
| RL-3.10 | §4 **Backward-compat posture**: "Mechanics behavior (R-05)" becomes "Mechanics behavior (R-03)" | Yes | §4 | — |
| RL-3.11 | Consequential renumbering and references; R-01 to R-04 and AC-01 to AC-05 keep their numbers | Yes. Nothing else needed changing | Whole file | A search of v1.1 finds no remaining `R-05` or `AC-06`. These references were checked and still hold unchanged: AC-05 in the R-02 and R-04 measures; the §3 note on AC-05's "tracked files unchanged" limb; TI-04's disposition "then AC-05" |

## 2. Non-blocking redlines (applied in the replacement, as the review directs)

| # | Redline | Applied | Where in v1.1 | How |
| :- | :- | :- | :- | :- |
| RL-4 | Insert the canon precedence rule as a block quote directly after the "Canon searched and relied on" table | Yes, verbatim | §0, directly after that table | A row for review v1.0 was added as the table's last row (§3 below). The quote follows it directly |
| RL-5 | Three replacements of Build Notes citations by internal addendum number | Yes, all three, verbatim | §0 table, HDE Build Notes row; §5 Prior epics; TI-02 Scope | The §0 file identity "PF10, v13.9" is kept, as the review allows. A search of v1.1 finds no remaining "addendum 2.1" |
| RL-6 | Append the vendor route selection and production override scope sentence to TI-02's **Scope** | Yes, verbatim | §11, TI-02 Scope cell | — |
| RL-7 | Append the `.audit_src/` copies sentence to TI-03's **Scope** | Yes, verbatim | §11, TI-03 Scope cell | — |

## 3. Changes no redline states

These are revision lineage and record currency only. None changes a requirement, criterion, exclusion, posture or tracked-issue disposition.

* **Front matter:**
  * `artifact_version` is `1.1`;
  * `author` names both versions' sessions;
  * `reviewer` now names Thoth-20, as review v1.0 records. v1.0 recorded it as unknown;
  * `prompt` is CF-E-40, keeping the CF-E-20 lineage;
  * new fields: `revision_mode`, `supersedes`, `review_ref`, `application_record` and `repository_head_read`.
* **Opening paragraph:** names v1.1 as the complete replacement and points to this record.
* **§0 Lineage table:**
  * the head row adds `0891314`;
  * new Review and Superseded version rows;
  * the Author / reviewer row names Thoth-20.
* **§0 Canon table** (record of what this revision relied on):
  * the HDE Governance row adds §9.7.7 and the §9.1.1 complete-replacement sentence;
  * the Plan Templates row adds "Requirement and work-unit business case" and "Canon precedence for template use";
  * a review v1.0 row is added.
* **§13** is rewritten for v1.1:
  * the reviewer's identity;
  * Rulings R-A to R-C and the Status ruling, recorded as retained review context;
  * the question for the re-review;
  * a pre-approval revision history table;
  * the TypeSafe reading and surface advice for the CF-E-30 re-review, which replace v1.0's CF-E-30 reading (that reading stays in v1.0 §13);
  * Isis's verification for v1.0 and v1.1;
  * the nonclaims, which add that RL-3 drops no source obligation.

The TI-07 table row is kept as accepted in v1.0. Its disposition cell still reads "Thoth to confirm the reading". Ruling R-A has since confirmed the reading, and §13 records that ruling, so the row and §13 together give the current state. The row was not edited because no redline reaches it.

## 4. Preserved without change

Per CF-E-40 Execute step 1, these are unchanged:

* change ID and class, Epic name and phase;
* the same Isis author and Thoth reviewer;
* the decision lineage;
* the Epic PF09 planned-work identity: W-SEPA006 and W-SEPA006.1 to .3, with status nonclaims.

Every section and row that no redline reaches is also unchanged, apart from the record-currency changes in §3:

* §1 Meta;
* §2.1 apart from RL-1;
* §2.2 Exclusions;
* §2.3 E-1 to E-5;
* §2.4 rows R-02 to R-04;
* §3 rows R-02 and R-04, AC-01 to AC-04, the AC-05 criterion text, the AC-05 note, "Not evidence of any criterion", and D-1;
* §4 apart from RL-3.10;
* §5 apart from RL-5;
* §6 apart from RL-3.9;
* §7;
* §8 apart from RL-3.7 and RL-3.8;
* §9, §10 and §12;
* §11 TI-01 and TI-04 to TI-07.

## 5. Facts re-verified for this revision

On `main` at `0891314`:

* `git diff --stat db590ab 0891314` changes only `docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md` (#781) and `docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md` (#782). The repository observations E-1 to E-5, made at `db590ab`, therefore still hold.
* RL-7: `git ls-files .audit_src` and a `grep` for `engine.charts`, `charts.loader` and `load_chart` under `.audit_src/` confirm loader-importing copies under `scripts/`, `tests/loader/` (including the retired test), `tests/compat/` and `tests/provider/`.
* No test, script or provider call was run.

## 6. Observation for the reviewer (not applied)

The same `.audit_src/` search also matches some paths outside RL-7's four directories:

* `.audit_src/engine/charts/loader.py`, a copy of the loader itself;
* `.audit_src/adapter/http_reader.py`;
* `.audit_src/_archive/EPIC003_CLEAN_20251017_211719/server/app.py`;
* some Markdown and log captures.

RL-7 is exact and was applied as written. TI-03 already leaves the complete inventory to the Implementation Audit. Thoth decides whether TI-03 should name these paths too. v1.1 does not add them.

## 7. Unresolved items and owners

None of these blocks the re-review.

* **D-1 / TI-01** (repair, retirement or pure retention): the Product Owner.
* **TI-02 to TI-06:** the Implementation Audit, after approval.
* **TI-07** (whether tokenless Epics still need an acceptance map, a possible canon change): report to the Product Owner, per Ruling R-A. This CF-E-40 session reports it to Nathan in its closing message. No canon is edited.

## 8. TypeSafe reading and surface advice

Recorded in v1.1 §13: TypeSafe v8.2, Opus 5.5 at high, for the CF-E-30 re-review, with every probability and the 24 cells as printed. Nathan has stated no pick, so none is recorded.

## 9. Nonclaims

This record establishes none of the following:

* approval of any version;
* an Implementation Audit, Plan, PR, Proceed or merge authority;
* QA, Ops or acceptance;
* PF09 or board movement;
* a canon change, a PF10 addendum or closure.

Merging this file preserves the record and approves nothing (D21-C).
