---
artifact_type: RESCOPE_DECISION
artifact_id: HDE-EPIC040-PR07-F01-RESCOPE-DECISION
artifact_version: "1.0"
artifact_state: DECIDED
decision: APPROVE — option 1, add code unit HDE-EPIC040-PR06a
change_class: EPIC
change_id: HDE-EPIC040
finding_ref: HDE-EPIC040-PR07-F01
finding_title: Code and public-contract work deferred to PR07 does not fit the documentation-only PR07 of Plan v2.1 §6.7
decision_owner: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING
invocation: Product Owner direct instruction, 2026-09-26 — "Ok, decide on this. If we do it, create a PF10 build notes addendum and create parameters for this new code unit, PR06a."
route: GCF-17.RESCOPE
decision_time_utc: 2026-09-26T02:55:39Z
addendum_created: docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.3.md
---

# HDE-EPIC040-PR07-F01 — Rescope Decision v1.0: Add PR06a

## 1. Decision

**Option 1.** A bounded code unit, **HDE-EPIC040-PR06a**, is added between PR06 and PR07. It delivers full Magic-10 exposure as **Reader v2**, and also the three findings deferred from PR04: F03, the production route; F05, Reader v1 schema conformance; and F07, the dev conjunction evidence capture. It then re-cuts the release once. PR07 stays documentation-only.

The complete unit parameters, the canon decision `C040-07` and the dependency change are in the one PF10 addendum overlay: `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`.

This supplies no implementation authority, Proceed, merge permission, QA verdict, PF09 movement or closure.

## 2. What was decided, and by whom

| Decision | Owner | Basis |
| --- | --- | --- |
| The public Reader exposes the full Magic-10 set | **Nathan / Product Owner**, 2026-09-26 | "we don't want to just emit harmony. This means PF01 needs a canon update"; "we need full magic 10" |
| Route: add PR06a (option 1), not widen PR07 (option 2) or defer beyond the Epic (option 3) | Isis-50, on the Product Owner's delegation | §3 |
| Mechanism: full Magic-10 ships as a versioned Reader v2; Reader v1 stays unchanged | Isis-50, as the direct consequence of the Product Owner decision under current canon | §4 |
| F07: the dev conjunction route carries the real admitted identity, not a dev stamp | Isis-50 | PF10 §2.12 and accepted PR04 behavior leave no other admissible answer |

**The full-Magic-10 decision is the Product Owner's, not this reviewer's.** The approved Specification v1.1 explicitly excludes it: "No public ten-category expansion or numeric public result". That puts it outside what a rescope decision may change on its own authority. The addendum records it as the Product Owner's decision, superseding the ten-category clause for HDE-EPIC040 and leaving the numeric clause intact.

## 3. Why option 1

- **Option 2 is excluded by the approved Plan's own text.** Plan v2.1 §6.7 says of PR07: "No source behavior or contract changes hidden as docs," and a newly found material code defect "returns to the same IA under existing change control, not silently fixed by DOC-10." Widening PR07 would override the immutable base in the one unit designed to describe the result rather than produce it.
- **Option 3 ships a known public-contract defect.** After PR06's admission, the production Reader is served at a route that PF05 does not name. Its success bytes fail the repository's own published schema, and full Magic-10 would not exist at all.
- **Option 1 isolates the public contract change** into one reviewable unit with its own instruction, plan and Proceed, and re-cuts the release once before OPS01. Its cost is one extra PR cycle. PR06's lineage review already records that any F03 or F05 fix forces a manifest re-cut and a new `release_id`, so the cycle carries no cost that the deferred work did not already carry.

## 4. Why Reader v2, and not a wider Reader v1

Canon prescribes the mechanism consistently, in four places:

| Source | Statement |
| --- | --- |
| PF01 §2.2 | "Exposure of the full Magic-10 set is a future, versioned change." |
| PF01 §5.1 | "Public exposure of all ten categories remains a future, versioned change." |
| PF01 §5.4.7 | Reader v1 remains harmony-only "unless a separately authorized public-contract version change widens it." |
| PF04 §15.2 `OI-001` | "Draft a versioned `reader.v2` public schema … **Keep Reader v1 unchanged.** Reader v2 may expose the canonical complete ten-item intrinsic Magic-10 result … Update PF01, PF05, PF12, tests, and Evidence Index entries." |

Delivering full Magic-10 as Reader v2 therefore **adds** canon and contradicts none. Every existing Reader v1 statement across PF01, PF04, PF05, PF09.4 and PF14 stays true. Widening v1 in place would instead rewrite roughly forty harmony-only statements across seven canon documents, and would change the meaning of a published contract under its existing version.

The Reader v2 contract in the addendum follows `OI-001`'s own terms: exactly ten items in canonical governed order, no omission, duplication, default fill, harmony-only substitution or viewer-preference mutation.

**F05 resolves in both directions.** The emitted `harmony` identity is correct for Reader v1: it comes from the admitted Magic-10 order, and PF01 §2.1 already records the `*_leader` schema as the non-conforming side. The retired scorer's `*_leader` identities therefore leave the published v1 schema, and Reader v2 carries all ten.

## 5. Evidence read

| Source | Identity | Load-bearing content |
| --- | --- | --- |
| PF10 current | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.3.md`, `6337d600…` | Latest active base per its §6 current-version rule. Addenda run through §2.22. §§2.16–2.18 are the F03/F05/F07 deferrals with return point PR07 |
| PF01 | `…PF01-Canon-HDE-Math-Spec-v1.3.7.md`, `101576d0…` | §§2.1, 2.2, 4.7, 5.1 as quoted |
| PF04 | `…PF04-Canon-HDE-Governance-v2.8.6.md`, `e8234398…` | §8.1.2 v1 exposure rule; §15.2 `OI-001` |
| PF05 | `…PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`, `a1257496…` | Production route `POST /api/reader?v=1`; `v=2` currently refused |
| PF12 | `…PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`, `d7b2e028…` | Reader schemas are release members |
| Specification v1.1 | `43e1b182…` | Line 265 exclusion |
| Plan v2.1 | `10732f93…` | §6.7 PR07 boundary; §6.8 OPS01 "all seven PR units" |
| F03 / F05 / F07 deferrals | `3f592509…` / `2cc921e2…` / `78d32798…` | Required work and manifest impact |
| PR06 lineage review | `27d49898…` | 44 members, version `1.1.0`, `release_id` `988ed2a7…`, `ADMITTED`; F03/F05/F07 carried to PR07 |
| Repository | `main` `4382690`, tree `ec30ccb6…` | `adapter/http_reader.py`, `schemas/reader.v1.schema.json`, `presenter/reader_v1/emitter.py` and `engine/runtime/public.py` are manifest members; the roster invariant is pinned at 44 in `engine/config/registry_loader.py`; `schemas/reader.v2.schema.json` does not exist |

No PF source was resolved from anywhere but `docs/pfcanon/`, which was read only. No code was executed for this decision: it rests on canon and recorded findings, not on a new behavioral claim.

## 6. Excluded options, with the evidence against each

| Option | Why not |
| --- | --- |
| 2 — widen PR07 | Contradicts Plan v2.1 §6.7 verbatim and mixes a public contract change into the final documentation step. |
| 3 — defer beyond the Epic | Leaves the production route, the v1 schema and the Product Owner's full-Magic-10 decision all undelivered. |
| Full Magic-10 by widening Reader v1 | Contradicts PF04 `OI-001` ("Keep Reader v1 unchanged") and PF01's versioned-change statements, and rewrites a published contract under its existing version. |
| Reader v1 adopts the four `*_leader` identities | These are the retired scorer's identities. The admitted Magic-10 core cannot produce them, and PF01 §2.1 records the schema that carries them as non-conforming. |

## 7. Return

- **Next native stage:** `PR-10 — Create PR Work-Unit Instructions — 091426.1` for HDE-EPIC040-PR06a, by the retained whole-change Implementation Architect. The paste-ready handoff is `docs/ephemeral/HDE-EPIC040-PR06a-PR10-handoff-v1.0.md`.
- **Then:** `PR-20` in a dedicated PR06a session, which produces a detailed plan in `AWAITING_PO_PROCEED` for Nathan's `PR-30`. PR07's `PR-10` waits until PR06a is `ACCEPTED_FINAL`.
- **No `PR_RETURN_PHASE`** applies, and RS-40 is ineligible: no PR06a Proceed, branch or pull request exists.
- **Notion:** none written. Under `docs/prompt_ecosystem_management/notion-write-boundary.md`, a development-flow decision is read-only with respect to Notion unless the task directs a write, and this one does not.
