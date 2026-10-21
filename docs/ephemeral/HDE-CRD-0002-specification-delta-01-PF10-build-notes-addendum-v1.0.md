## 2.18 HDE-CRD-0002: Specification delta 01 is approved — requirement S01 is removed and the release keeps its version, with a same-version manifest refresh for any member change

Timestamp: 102126 18:36 (UTC). Details: Records the CF-C-30 approval of the first Specification delta to the approved HDE-CRD-0002 CRD Specification. The delta removes requirement S01 (every release member packaged with the distribution), drops any release version cut so the release stays at `1.3.0`, and replaces the Specification's "manifest re-cut and new admission pins" constraint with a same-version manifest refresh. S16 and S17 are kept. The approved base is unchanged; the base plus this delta is the current Specification.

### Source and approval

* Producing prompt: CF-C-30 — Review and Approve CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8), mode APPROVED\_BASE\_DELTA\_REVIEW; release GCFPE-20261009.1 / 100926.1.
* Approval decision: DELTA\_APPROVE by Thoth, the HDE-CRD-0002 Specification reviewer (session https://claude.ai/code/session\_01QDA4Gim8zTtX2KqAEWnaum), recorded in docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md, 2026-10-21T18:36:00Z.
* Approved delta: docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md, logical ID HDE-CRD-0002-SPECIFICATION-DELTA-01, authored by Isis, Lead Developer, through CF-C-40 — Revise CRD Specification — 100926.1 (APPROVED\_BASE\_FIRST\_DELTA\_AUTHORING); file SHA-256 59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636; landed by [\#675](https://github.com/amthorn78/glow-hdengine-v2/pull/675).
* Immutable base: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION\_APPROVED, "ASK OK."), the approved representation of docs/ephemeral/HDE-CRD-0002-specification-v1.1.md, approved by docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md (INITIAL\_APPROVE, 2026-10-12T19:39:51Z). The base file is not edited.
* Authorizing decision: the Product Owner's OPTION 1 of 2026-10-21, docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md ([\#673](https://github.com/amthorn78/glow-hdengine-v2/pull/673)): remove S01; drop the `1.4.0` version cut and keep the release at `1.3.0`; keep S16 and S17; a member change forces a manifest refresh at the current version, not new admission pins.
* Warranting assessment: docs/ephemeral/HDE-CRD-0002-specification-correction-assessment-v1.0.md (CF-C-30 CORRECTION\_REDLINE, changes C-1 to C-14; [\#674](https://github.com/amthorn78/glow-hdengine-v2/pull/674)).
* Applicable prior addenda, in order: none overlays this Specification. The decision rests on addendum 2.11 (rule 4, real inputs; rule 5, constructed inputs; its "Epic, task, and status effects" leaving S01 open on rule 3) and on addenda 2.12 (decision 4) and 2.16 (the decisions returned to the Product Owner before WU-PR-08's PR-10).

### Approved decision

The delta is approved as authored. It applies exactly the fourteen changes of the correction redline and nothing else. It is a material change under HDE CRD Records §4.2: it changes approved scope and exclusions, phase structure and completion boundaries, dependency order, QA posture and the expected outcome.

### Approved delta, complete

Requirement IDs are not renumbered. The "Current text" column gives the wording in force from this approval.

| # | Location in the Specification | Base text replaced | Current text |
| :- | :- | :- | :- |
| C-1 | Requirements table, S01 row | Scope "Package every release member with the distribution"; acceptance intent "A regular wheel install admits the complete release outside a source checkout" | Scope "Removed by the Product Owner's decision of 2026-10-21 (docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md)"; acceptance intent "None — not delivered". Source "5(a), O-12" kept |
| C-2 | Intake → Bounded scope | "S01 to S22 below." | "S02 to S22 below; S01 is removed (Exclusions)." The second sentence is unchanged |
| C-3 | Intake → Expected outcome | "every acceptance intent S01 to S22 holds on `main`" | "every acceptance intent S02 to S22 holds on `main`"; the rest of the field is unchanged |
| C-4 | Intake → Affected surfaces | "code: packaging metadata, the production HTTP adapter …" | "code: the production HTTP adapter …"; nothing else changes |
| C-5 | Exclusions, bullet 2 | "No release re-cut beyond what the in-scope requirements require." | "No release version cut: the release stays at its current version, `1.3.0`, and no new admission version or build time is set (Product Owner decision of 2026-10-21)." |
| C-6 | Exclusions, new bullet after bullet 2 | — | "S01 (5(a), O-12), every release member packaged with the distribution, is removed by the Product Owner's decision of 2026-10-21. Basis: production starts the engine from the checkout (`Procfile`: `python -m gunicorn 'adapter.factory:create_app()'`) and CI installs in editable mode, so S01 rests on no real input (HDE Build Notes, real-input rule). Not delivered: a regular wheel install outside a source checkout still does not admit the release." |
| C-7 | Constraints → Release members, from "Those of S01" to the end of the bullet | "Those of S01 (`pyproject.toml`) and S02 (`adapter/factory.py`) are not. Any requirement whose implementation changes a release member forces a manifest re-cut and new admission pins; the Implementation Audit establishes the actual set. The change converges on one coherent re-cut after the member-changing work lands." | "That of S02 (`adapter/factory.py`) is not. Any requirement whose implementation changes a release member forces a manifest refresh at the current version, not new admission pins; the Implementation Audit establishes the actual set." The bullet's first two sentences are unchanged |
| C-8 | Phase blocks, Conjunction, Dependencies | "Coordinates with the release re-cut where a requirement changes a release member (S07, S10 by observed locus)." | "Coordinates with a same-version manifest refresh where a requirement changes a release member (S07, S10 by observed locus)." The S19 sentence is unchanged |
| C-9 | Phase blocks, Fermentation, Dependencies | "Coordinates with the release re-cut (S08, S14 by observed locus)" | "Coordinates with a same-version manifest refresh (S08, S14 by observed locus)" |
| C-10 | Phase blocks, Coagulation | Purpose "Durable packaging and environment discipline: S01, S16, S17"; Dependencies "S01 converges with the release re-cut"; Completion boundary "S01, S16 and S17 hold on `main`" | Purpose "Durable environment discipline: S16, S17"; Dependencies "None; S16 and S17 change no release member"; Completion boundary "S16 and S17 hold on `main`". Other columns unchanged |
| C-11 | "Recommended ordering" line | "…; the release re-cut after all member-changing work lands; …" | Clause deleted: "S03 to S05 early, so later changes in every block are visible to CI; S22 before QA; S21 before HDE-CRD-0002's closeout." |
| C-12 | Canon, QA & Build Notes posture → Production-affecting Live QA minimum table | The row "Production-affecting, outside the functional-feature scope; …", requirement S01, "Packaging of the deployed service. …" | Row deleted. The functional-feature, inherits and not-production-affecting rows are unchanged |
| C-13 | Closure result → Superseded or rejected scope | `None` | "S01, removed by the Product Owner's decision of 2026-10-21 (docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md)" |
| C-14 | Material-change history | One row (2026-10-12, Specification approval) | One row appended; the existing row is unchanged (HDE CRD Records §4.2). Date: 2026-10-21. Affected fields: approved scope (S01); Bounded scope; Expected outcome; Affected surfaces; Exclusions (bullet 2 replaced; S01 bullet added); Constraints → Release members; phase structure and dependencies (Conjunction, Fermentation, Coagulation, Recommended ordering); Live QA classification (S01 row removed); Superseded or rejected scope. Change: S01 removed; no release version cut, the release staying at `1.3.0` with a same-version manifest refresh for any member change; S16 and S17 kept as the Coagulation block. Decision source: the Product Owner decision record above; the correction assessment above; the delta approval above. Build Notes reference: this addendum. Record control's "Last material update" is 2026-10-21 |

Unchanged by the delta: the Observed need, Why warranted and Lead Developer finding fields (records of intake); every requirement other than S01; every exclusion other than bullet 2; every constraint other than the last two sentences of Release members; CD-1 to CD-3; RD-1; the canon-conflict register as carried; the kickoff open points; Record control, Specification approval and decision lineage except as this approval records them.

### Facts behind the decision

* Production starts the engine from the checkout: `Procfile` reads `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …`, and `-m` places the working directory first on the import path. The live Railway start setting is unverified (Glow Infrastructure §10); if production ran without the checkout, admission would refuse to start (`MISSING_FILE`).
* Same-version refreshes are established practice in this change: at the merges of WU-PR-03, its corrective cycle, WU-PR-04 and WU-PR-05 (`c98d41f`, `2f3db0a`, `5892538`, `822ce15`), `catalog/manifest.json` kept version `1.3.0`, build time `2026-08-24T18:04:49Z` and 45 members while `release_id` moved `52be4558…` → `72fca4c3…` → `d84d99e1…` → `2f18a5eb…` → `77204764…`; the `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER` constants in `engine/config/registry_loader.py` did not change.
* S16 (`.env.example`) and S17 (`docs/ADAPTER_009.md`) change no release member, and no HDE-CRD-0002 unit has changed `pyproject.toml`.

### Affected surfaces, dependencies and consequences

* Implementation Plan v1.1 (docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md) no longer matches the Specification where it plans S01 or a `1.4.0` version cut: §3 "Release-identity spine"; §6 (the S01 row and "version bump `1.4.0` in WU-PR-08"); §7 WU-PR-08 (title, scope, deliverables, acceptance) and WU-OPS-01's success criterion ("the `1.4.0` `release_id`"); §10; §11 R-2 and R-6; §12; WU-DOC-01's AGENTS.md "release `1.4.0`" line. Those passages are not in force against this Specification; the Plan's own approved-base change route resolves them.
* WU-PR-08 covers S16 and S17 only. It changes no release member, so it requires no manifest refresh. Its business case and cost ceiling are in the Product Owner decision record §2 (addendum 2.11 rule 1).
* The QA Plan needs no Live QA step or exemption for S01.
* Release identity is unchanged: `release_id` is manifest-derived, and version `1.3.0` with its build time remains the admitted release.
* No test, Ops task or document is required by the delta itself.

### Exclusions and nonclaims

* No new requirement; no change to any other requirement's scope or acceptance intent; no canon change; no change to the release-identity rule.
* Not delivered: a regular wheel install outside a source checkout still does not admit the release.
* This approval is not an Implementation Plan change, PR Proceed, Ops completion, QA verdict, acceptance or closure, and moves no PF09 or PF30 row.

### Conflicts

None. No PF canon requires a release version cut; the decision is consistent with addendum 2.11 rules 4 and 5; the carried canon-conflict register is unaffected.

### Unresolved obligations and owners

* The live Railway start setting: WU-OPS-01 records the deployment facts; Product Owner. A stated limit, not a blocker.
* The Implementation Plan v1.1 approved-base change for the passages above: Isis as Plan reviewer (IA-30), then the whole-change Implementation Agent (IA-40).

### Return phase

The affected continuation is IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), APPROVED\_BASE\_CHANGE\_ASSESSMENT, with this approved delta and the Product Owner decision as the authorized material-change request against the immutable Implementation Plan v1.1 and its review v1.1. WU-PR-08's PR-10 follows the Plan change.

### Relationship to existing HDE Build Notes guidance

This addendum applies addendum 2.11 to requirement S01 and answers the WU-PR-08 business-case and S01 real-input decisions that addenda 2.12 and 2.16 returned to the Product Owner. It changes no other addendum and supersedes none.
