---
artifact_type: IA_40_TERMINAL_RETURN
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01-REDLINE-RETURN
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
result: REDLINE_INCOMPLETE (terminal for this IA-40 invocation; no MATERIAL_PLAN_DELTA authored)
AUTHORING_MODE: APPROVED_BASE_PLAN_DELTA_AUTHORING
redline_returned: docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.0.md (IA-30 PLAN_DELTA_REDLINE P-1 to P-17; blob 52c204abd092; landed by #677 as 96ced7f)
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd44), approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (INITIAL_APPROVE; blob 0cc0276524b2). Unchanged
material_change: docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE), recorded by docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md (addendum 2.18)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Product Owner OPTION 1; blob efc220928f7c)
return_owner: Isis, Plan reviewer, IA-30 (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
author: the whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), continuing the Plan author lineage (sessions 012nUipT8gpdYtjzA5UQk5ah and 01CCKsYD2yX5WgU3biWKb59j)
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16; page state as of 2026-10-12T02:29:25.413Z, fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_head_read: origin/main 96ced7f36be1445c5be83c6d862d419b580c65f7
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.9.md (blob c9e598d65dd1; sha256 4d821147c95624c80d0615bc99ba76f45a44e69c86765762c8cdf6eba0cd8fff). Front matter §8 and §9; addenda 2.9 and 2.10 at their WU-PR-08 carried items; 2.11 in full; 2.16 and 2.17 headings and their WU-PR-08 passages. Addendum 2.18 read from its docs/ephemeral record
created_at: 2026-10-21T18:52:00Z
---

# HDE-CRD-0002 — Plan delta 01: redline returned to the reviewer (IA-40, REDLINE_INCOMPLETE)

## 1. Result

**REDLINE_INCOMPLETE.** IA-40 applies only the supplied redline. One item, P-7, cannot be applied as bounded, because a repository fact contradicts it:

- **P-7 fixes WU-PR-08's deliverables** to `.env.example` and `docs/ADAPTER_009.md`.
- **The CI classifier refuses `.env.example`.** It is not registered as any change surface, so any pull request that changes it fails CI's classification step, and the run fails.

The fix is a registration in `ci/checks/classify_ci_changes.py`. That file lies outside P-7's fixed bound, and changing it makes CI run every lane. Adding it would be a design change to the bound, which IA-40 does not infer. The redline returns to its reviewer.

No `MATERIAL_PLAN_DELTA` was authored, and the approved Plan is unchanged.

## 2. The finding

| Item | Fact (measured on `main` `96ced7f`, closed rails, CPython 3.12.3) |
| :- | :- |
| CI's classification step | `.github/workflows/ci.yml` step `classify` runs `python3 ci/checks/classify_ci_changes.py --base "$BASE_SHA" --head "$HEAD_SHA" --event-name … --github-output … --changed-tests-output …` under `set -euo pipefail`. The final step fails the run when the classification outcome is not `success` |
| A WU-PR-08 change, reproduced | In a throwaway clone, one commit on `96ced7f` that appends `GEO_API_KEY=changeme` to `.env.example` and corrects one port line in `docs/ADAPTER_009.md`. The classifier, called as CI calls it with full SHAs, prints `CI_CHANGE_CLASSIFIER_ERROR:CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example` and **exits 2** |
| Why | `_lanes_for_path` returns no lane set for `.env.example`. It is not in `_DOCUMENT_PATHS` (`LICENSE`, `AcceptanceMap.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`), has no document suffix (`.adoc`, `.md`, `.rst`) and matches no product or test prefix. `classify_paths` then raises `CI_CHANGE_SURFACE_UNCLASSIFIED` (`ci/checks/classify_ci_changes.py` around lines 1838 and 1898) |
| `docs/ADAPTER_009.md` alone | `prepush_check.py --path docs/ADAPTER_009.md lanes`: `reason=documentation_only`, no lane, 0 changed-test targets |
| A classifier change | `prepush_check.py --path ci/checks/classify_ci_changes.py lanes`: all seven lanes, 166 changed-test targets |
| Release membership | `.env.example` and `docs/ADAPTER_009.md`: not members of release `1.3.0` (45 members, `release_id` `77204764…`). The decision record's "no manifest refresh" holds |

**Effect on P-7:**
- Its acceptance item (4), "the selected lanes are green", cannot be met: CI fails before it selects any lane.
- The business case's cost line is inaccurate (decision record §2, "Cost ceiling": "Neither change touches a release member, so there is no manifest refresh and no full-validation CI run"). A classifier registration runs all seven lanes on the WU-PR-08 pull request.

This is a real input under addendum 2.11 rule 4(b): the hosted CI run of WU-PR-08's own pull request.

## 3. What the reviewer decides

These are the options as the author sees them. The reviewer decides the bound (Plan Templates, "Source-bound review authority and exact-fix limits").

| Option | Change to P-7 | Consequence |
| :- | :- | :- |
| A. Register `.env.example` in the classifier | Deliverables gain `ci/checks/classify_ci_changes.py` (one registration for `.env.example`), and its pinned test if one enumerates the changed registry. The author states the registration form at PR-20 | Every lane runs on the WU-PR-08 PR. The decision record's cost line changes. Whether the ceiling of 1 PR, 2 sessions and 1 day still holds is the Product Owner's call (addendum 2.11 rule 3). A full hosted run takes about 20 minutes, and the local full replay about 25 to 33 minutes |
| B. A different registration home | Only if the reviewer finds one outside the classifier that CI reads. The author found none: the classifier is CI's only surface map | — |

The author recommends A. It is the smallest change that lets S16's file change pass CI.

## 4. The other sixteen items

Each was checked against Plan v1.1 on `main` and found applicable as written. Each anchor is present exactly once at the quoted location:
- P-1: §2 table.
- P-2: §3 opening paragraph.
- P-3: §3 "Release-identity spine".
- P-4: §4 invariant 3.
- P-5: §5 IF-8.
- P-6: §6, the S01 and "Release re-cut" rows.
- P-8: §7 WU-DOC-01 "Bounded scope".
- P-9: §7 WU-OPS-01 Intent, Success criteria and Constraints.
- P-10, P-11: §9 items 2 and 3.
- P-12: §10 heading and step 2.
- P-13: §11 R-2, R-6 and R-8.
- P-14: §12.
- P-15: §13.
- P-16: §14.
- P-17: header.

They will be applied unchanged when the redline returns with P-7 resolved.

**One note for the reviewer, not a defect of the redline.** Addendum 2.10 carries to the WU-PR-08 instruction "WU-PR-08 (S17) cuts `1.4.0` from `release_id` `77204764…` (contract F-1)". Addendum 2.18 approves no version cut. Their scopes overlap on the version cut, so PF10's operational rule applies: front matter §9 step 8, the highest-numbered applicable addendum governs the overlapping scope. Addendum 2.18 therefore governs, and the delta's "Inputs" line for WU-PR-08 would carry 2.9's and 2.10's other items (OBS-P4-5, O-19, F-3, the loopback bind) without the cut.

## 5. Unresolved items and owners

| Item | Owner |
| :- | :- |
| P-7's bound: how `.env.example` reaches green CI (§3) | Isis (IA-30), as a revised change assessment |
| The decision record's cost line, and whether the ceiling still holds with all seven lanes running | Isis records the correction. The Product Owner decides the ceiling (addendum 2.11 rule 3) |
| The Plan delta itself | This Implementation Agent (IA-40), on the revised redline |

## 6. Return point

Terminal for this invocation. The redline returns to Isis: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), in the same approved-base change-assessment lineage.

When a corrected `PLAN_DELTA_REDLINE` exists, IA-40 `APPROVED_BASE_PLAN_DELTA_AUTHORING` resumes with this Implementation Agent.

No continuation handoff is emitted (IA-40, "Results and routing").

## 7. TypeSafe reading

TypeSafe: not read. The result is terminal and has no receiving session to score.

Nathan's pick for this IA-40 session: not stated. The reading for it is in the change assessment §7.

## Canon relied on

Read on `main` at `96ced7f`.

- **IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1**, read in full: `APPROVED_BASE_PLAN_DELTA_AUTHORING` inputs; "Apply only the supplied IA-30 redlines … Ambiguous, contradictory, or unsupported redlines return to the same Isis reviewer without inference"; `REDLINE_INCOMPLETE` routing.
- **PF10-HDE-Build-Notes v13.6.9:**
  - front matter §8 "Silence rule" and §9 "Operational rule for agents" (step 8);
  - addendum 2.11 in full (rule 3, the ceiling; rule 4, real inputs);
  - addenda 2.9 and 2.10 at their WU-PR-08 carried items;
  - addendum 2.18 from its record.
- **PF27-Canon-Plan-Templates v2.0.5**, "Source-bound review authority and exact-fix limits", as the change assessment cites it (the reviewer decides the bound; the author states design inside it).
- **`AGENTS.md`:** "HDE-EPIC039 current workflow posture" (the one `test` job; seven change-aware lanes; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and "Release identity".
- **In-flight documents, read in full:**
  - the change assessment;
  - Implementation Plan v1.1;
  - Specification delta 01;
  - the decision record §1 to §3;
  - the addendum 2.18 record's "Affected surfaces", "Conflicts" and "Unresolved" sections.
- **Repository facts:**
  - `.github/workflows/ci.yml`: triggers and the `classify` step;
  - `ci/checks/classify_ci_changes.py`: `_DOCUMENT_SUFFIXES`, `_DOCUMENT_PATHS`, `_lanes_for_path`'s fall-through and `classify_paths`;
  - the reproduction in §2.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-40 / approved-base Plan delta authoring 1 (terminal return) |
| change | CRD HDE-CRD-0002 |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | whole-change Implementation Agent / IA-40 APPROVED_BASE_PLAN_DELTA_AUTHORING |
| capture time | 2026-10-21T18:52:00Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
