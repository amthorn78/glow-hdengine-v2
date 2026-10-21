---
artifact_type: REDLINE_APPLICATION_REPORT
artifact_version: "1.1"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01-APPLICATION-REPORT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
reports_on: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (MATERIAL_PLAN_DELTA v1.1, PLAN_DELTA_PENDING)
predecessor: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.0-application-report.md (blob 04e1190dad43b2de529839e3eddfd37961e66c0d), carried below for P-1 to P-17
denial_redlines: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.0.md §4, D-1 to D-8 (IA-30 DELTA_DENY; blob 33f9dd4051ecd22be260b9a58860ede7a79d47d9)
redline: docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md §3, P-1 to P-17 (blob c4bfa53b6d45065946678bca05fc8ee1f7f9ba84)
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
governing_overlays: the no-ceiling addendum (PF10 v13.7.1 addendum 2.18); the Specification delta 01 addendum (record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md); the Product Owner's deployment direction of 2026-10-21 (docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.0.md §2)
author: the whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
repository_head_read: origin/main 4c306a1
created_at: 2026-10-21T20:39:22Z
---

# HDE-CRD-0002 — Plan delta 01 v1.1: redline application report (IA-40)

## 0. Revision v1.1: denial redlines D-1 to D-8

All eight are applied once each. Nothing else changed in substance from v1.0, which the review accepted in every other part (review v1.0 §3). §1 to §4 below are v1.0's report of P-1 to P-17, carried unchanged, except that P-9's content is now as D-1 to D-3 state.

| Item | Anchor (occurrences) | Applied as | Note |
| :- | :- | :- | :- |
| D-1 | Delta v1.0 §3 P-9 Intent, second sentence "The deployment facts the QA Plan needs, and the live start command (…), are recorded presence-only." (1) | Replaced with the required wording; first sentence unchanged | — |
| D-2 | Delta v1.0 §3 P-9 Success criteria (1) | Replaced with the required wording | Trigger, build command and start command no longer recorded |
| D-3 | Delta v1.0 §3 P-9 Constraints, the whole overlay including "Live start command" (1) | Replaced with the required wording, plus the author statement "When the candidate's identity does not appear" | B-1, B-2 |
| D-4 | Plan v1.1 §7 WU-OPS-01 PF07 posture, from "PF07-gap (discoverable by OPS): the service's deployment trigger" (1) to "it does not guess them." (1) | New item P-18, required wording | The PF07-derived sentence before it unchanged |
| D-5 | Plan v1.1 §7 WU-OPS-01 "Hosted-service operation (deployment or redeploy of the accepted commit; read of `/internal/version`; presence-only probe of the bindings)." (1) | New item P-19, required wording | "No vendor call, no database write." unchanged |
| D-6 | Plan v1.1 §11 R-9 row (1) | New item P-20, required wording | — |
| D-7 | Delta v1.0 §1 WU-OPS-01 bullet (1); §4 "Ops" row (1); §8 start-command row (1) | §1 and §4 restated as required; §8 row removed and the PF07 doc-delta row added; conflict row K-6 authored | B-3 |
| D-8 | Front matter; §8 return point; this report | `artifact_version: "1.1"`, predecessor v1.0, denial lineage review v1.0; this report adds §0 | A-7's reviewer note is answered by D-3: the build-command stop goes with the build-command discovery |

**Linked edits** that follow from D-1 to D-8 and change no content of their own:
- §1 gains a revision note, names D-1 to D-8 and the deploy direction among what it applies, and adds "Risk R-9 is removed" to its summary.
- §3's "Unchanged" list reads "every risk other than R-2, R-6, R-8 and R-9".
- §4 gains a "Risks" row naming P-13 and P-20.
- §5's first bullet reads "P-1 to P-20".
- The §8 review row reads "this revised delta".
- §9 holds a new TypeSafe reading for the re-review.
- The canon list adds Glow Infrastructure §2.4, §3.1, §3.3, §4.1 and §10, the review v1.0 and `engine/runtime/identity.py`, and restates the redaction bullet.
- The provenance row is updated.

**Author statements** within their stated bounds:
- **B-1, D-3.** If `/internal/version` does not report the candidate's `release_id` after the commit lands, the task reads again after the service has had time to deploy. If it still does not, the task records each read (time, HTTP status, the `release_id` reported or no answer), changes no production configuration and stops. It redeploys the previous commit only if the service did not answer at all, under the rollback intent. The Product Owner decides the next step. Within the bound: no configuration change, no discovery of the trigger or commands, the rollback intent as stated, no secret value or raw body.
- **B-2, D-3.** The task judges deployment by `release_id` alone, because `build_commit` is a fixed value written in the source (`engine/runtime/identity.py`, `_STATIC_IDENTITY`). This adds no work. It tells the executor not to rely on that field.
- **B-3, D-7.** K-6 records that the direction supersedes assessment v1.1 P-9's start-command parts and discharges the Specification delta 01 addendum's WU-OPS-01 obligation, as review v1.0 §2 states. C-6's stated limit stands.

**Reviewer notes**, not applied, since no redline covers them:
- **N-1.** Plan v1.1's WU-OPS-01 heading reads "Place the QA candidate and record the deployment facts". Under the direction, the unit records no deployment facts beyond the identity proof and the binding probe. The heading is not in D-1 to D-8 and is left as written.
- **N-2.** Plan v1.1 §13 says "Infrastructure facts the Plan names are PF07-derived or classified `discoverable by OPS` (WU-OPS-01)". The deploy source is now a Product Owner-provided fact (P-18). The sentence is not in D-1 to D-8 and is left as written.

## 1. Result (v1.0, carried)

All seventeen items are applied once each, at their anchors, and nothing outside them changed.

- **Applied exactly as written:** thirteen items (P-2, P-3, P-4, P-5, P-6, P-8, P-10, P-11, P-12, P-13, P-14, P-15, P-16).
- **Applied with an adjustment the redline or a governing overlay requires:** four items (P-1, P-7, P-9, P-17). Each adjustment is listed in §3:
  - where only the wording changes, the meaning is unchanged, as the redline permits;
  - P-7 also drops the ceiling under the no-ceiling addendum.
- **Returned unapplied:** none.

**Anchor check.** Every anchor was matched against the unchanged base blob `abffa2cc…` by exact string count. Each of the 25 anchor strings occurs exactly once, two to four of them for the multi-part items. No two items' target spans overlap. P-7 replaces the whole WU-PR-08 block, and no other item targets a line inside it (Plan Templates, "Redline bundle construction discipline": one-pass application from the base).

## 2. Item by item

| Item | Base anchor (occurrences) | Applied as | Note |
| :- | :- | :- | :- |
| P-1 | §2 row "Conflict register" (1); rows added after it | Three rows | A-2 |
| P-2 | §3 "member-changing work lands before the version-bumping release cut (S01 unit last among code units)" (1) | Replaced as written | — |
| P-3 | §3 "The single new release, `1.4.0` with new admission pins, is cut once, in WU-PR-08" (1), through the end of the bullet | Replaced as written | — |
| P-4 | §4 "admission constants change only in WU-PR-08" (1) | Replaced as written | — |
| P-5 | §5 "\| IF-8 \| Wheel layout \|" (1) | Shape cell replaced as written | — |
| P-6 | §6 "\| S01 \| WU-PR-08 \| Coagulation \|" (1); "\| Release re-cut \| … version bump `1.4.0` in WU-PR-08 \|" (1) | Both rows replaced as written | — |
| P-7 | §7 heading "### WU-PR-08 — Packaging, environment template, operator documentation, release 1.4.0 (PR; Coagulation)" (1), through "Nonclaims" | Block replaced | A-1 to A-5 |
| P-8 | §7 WU-DOC-01 "install into a dedicated environment; " (1); "HDE-EPIC040 current posture → release `1.4.0`" (1) | Deleted; replaced as written | — |
| P-9 | §7 WU-OPS-01: Intent "and the deployment facts the QA Plan and S01's exemption basis need" (1); Success "the `1.4.0` `release_id`" (1) and "the recorded deployment trigger and build command" (1); Constraints "(the QA Plan's S01 treatment depends on it)" (1) | Replaced; author statement added | A-2, A-6, A-7 |
| P-10 | §9 item 2 "The acceptance intents S01 to S22" (1); "the wheel-install admission test, " (1) | Replaced; deleted, as written | — |
| P-11 | §9 item 3 "S01's class-2 step or its recorded exemption basis from WU-OPS-01's discovery; " (1) | Deleted as written | — |
| P-12 | §10 heading (1); step 2 "`<V>`/`<T>` are the current constants for a refresh" (1) | Replaced as written | The step 2 sentence replaces its whole sentence, from the anchor to "set in `engine/config/registry_loader.py` first)." |
| P-13 | §11 "\| WU-PR-03/04/05/08 \|" (1, R-2); "\| R-6 \|" (1); R-8 risk text (1) | The three rows replaced as written | R-8's Unit and Treatment cells unchanged |
| P-14 | §12 "no release re-cut beyond the refreshes admission forces and the single `1.4.0` cut" (1) | Replaced as written | The §12 heading "(carried from the Specification; none added)" stays true: C-5 and C-6 are Specification exclusions |
| P-15 | §13 "No engineering decision remains open at Plan level; EC-1 to EC-12 are recorded in Audit §7.1 and applied here." (1) | Sentence appended as written | — |
| P-16 | §14 "; a reverted WU-PR-08 restores the `1.3.0` constants and manifest and re-converges" (1) | Deleted as written | — |
| P-17 | Header and state | The delta's front matter | A-8 |

## 3. Adjustments

- **A-1, P-7: no ceiling.** The no-ceiling addendum withdraws every ceiling clause. It names these passages of the assessment as not in force: P-7's "and the ceiling as the Product Owner sets it" and "The ceiling is the one the Product Owner sets in the recorded decision that §5 asks for", §5's ceiling question, the §6 row and §7's condition. It also takes the decision record's "Cost ceiling" row out of force. Applied as follows:
  - The heading "Business case and ceiling" becomes "Business case".
  - Both ceiling sentences are omitted.
  - The clause "The cost line is as corrected by this assessment §5" pointed at a correction to that row. The corrected fact itself stands (no-ceiling addendum, "Epic, task, and status effects": "WU-PR-08 changes the CI classifier, so its pull request runs all seven lanes"), so the block states the fact in place of the pointer.
- **A-2: addendum numbering, P-1, P-7, P-9 and P-17.** The redline cites "addendum 2.18" for the Specification delta 01 addendum. PF10 v13.7.1 gives 2.18 to the no-ceiling addendum. Each such citation therefore names "the Specification delta 01 addendum" with its record path, so it identifies the same addendum as the redline meant (delta §2 and K-4).
- **A-3, P-7 deliverable (3): the form stays the author's statement at PR-20.** The handoff asked that the form be stated from the repository. Plan Templates, "CI lane classification and automated budget-control discipline", says a plan must not invent a change-detection mechanism. The block therefore keeps the redline's text and adds "Repository facts for PR-20" (delta K-5):
  - the existing mechanisms: `_DOCUMENT_PATHS` and `_WORKFLOW_CONTROL_PATH_LANES`;
  - that nothing reads `.env.example`;
  - that no test enumerates `_DOCUMENT_PATHS`.

  PR-20 chooses.
- **A-4, P-7 dependencies.** The lane selection is "author states". It is stated from the classifier and from a throwaway-clone rehearsal: all seven lanes, 166 changed-test targets.
- **A-5, P-7 deliverable (4) and risks.**
  - Deliverable (4) applies "only if one enumerates the registry". None does on `main`, so for now it adds no test. PR-20 re-reads at its head.
  - The risks are authored, as "Author states" requires: misclassification, failures the full run exposes that are not this unit's, and document drift.
- **A-6, P-9 Intent: word order.** The literal substitution would read "the deployment facts the QA Plan and the live start command (…) need", which says the start command needs facts. The sentence is reordered so that it means what the redline states: the deployment facts the QA Plan needs, and the live start command, are recorded presence-only.
- **A-7, P-9 Constraints.** The redline says "remove the S01 dependency". It was applied literally: the parenthetical "(the QA Plan's S01 treatment depends on it)" is deleted, and "record it and stop" is kept.
  - **Reviewer note.** With S01 removed, the stop on a build-command difference has no stated reason left, because the engine runs from the checkout whatever the build installs (decision record §2). Whether to keep the stop is the reviewer's call, and the author did not infer one.
  - The added "Live start command" paragraph is the author statement P-9 requires. It is bounded by the stated limit (`MISSING_FILE`), and it keeps the existing rollback intent and the redaction rule from `AGENTS.md`.
- **A-8, P-17.**
  - The front matter lists the immutable base, the assessment v1.1 (with v1.0 and the return as history), Specification delta 01 with its review, both overlays and the decision record, with the state `PLAN_DELTA_PENDING`.
  - The fields IA-40 requires are §4 to §8 of the delta.
  - Plan v1.1's header, §16 and §17 are not edited, because the base is immutable. The delta's §8 serves as its checkpoint.

## 4. Preserved

- Everything in Plan v1.1 outside the seventeen anchors, including:
  - completed units WU-PR-01 to WU-PR-07, with R-5 and WU-PR-05's "precede the version bump";
  - §1 and §8;
  - §9 items 1, 4 and 5;
  - §10 steps 1 and 3 to 12;
  - §15;
  - AQ-1;
  - every interface but IF-8 and every risk but R-2, R-6 and R-8;
  - the unit order.
- The conflict register CR-1 to CR-3, carried.

## 5. TypeSafe reading for the receiving session (IA-30 re-review of v1.1)

The same single reading as delta v1.1 §9, recorded identically. It supersedes v1.0's reading below:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.21 (confidence 0.80); rung probabilities low 0.00, medium 0.05, high 0.71, extra high 0.23, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.99, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 0.99). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.050, Opus 5.5 at high 0.703, Opus 5.5 at extra high 0.228, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T20:38:58Z. Nathan picks the cell. Flags: none printed. Detail line not captured (delta v1.1 §9).
- **v1.0's reading, superseded:** Opus 5.5 at high, score 2.38, with the flag "boundary between extra high and high".
- **Nathan's pick:** not stated.
- **Surface advice:** as in delta §9.

## Canon relied on

As the delta v1.1's "Canon relied on" block, on `main` at `4c306a1`. In particular, for this report:
- IA-40 "Controlled sources and exact-redline boundary" ("Apply only the supplied IA-30 redlines … Preserve unaffected content") and its approved-base Execute step 3 (the application report);
- the no-ceiling addendum (PF10 v13.7.1 addendum 2.18), rule 1 and "Epic, task, and status effects" (A-1);
- Plan Templates, "Redline bundle construction discipline" (the anchor check) and "CI lane classification and automated budget-control discipline" (A-3);
- IA-30 delta review v1.0 §2 and §4 (D-1 to D-8), and Glow Infrastructure §2.4 ("PO-provided deployed environment facts MUST NOT be downgraded to `OPEN/TBD`"), for §0.
