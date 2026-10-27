---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002/IMPLEMENTATION-PLAN-V1.1/DELTA-01-V1.1/IA-30-DELTA_APPROVE
approved_delta_digest: sha256 55e390a8848d02d6f4ffe9a26ff478afe34e97a79ee620285be9a017731d569e (file bytes of docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md; git blob 5103fe29d588631bba2e34dea65977c9b051305f)
producing_prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), MATERIAL_PLAN_DELTA_REVIEW; release GCFPE-20261009.1 / 100926.1
approval_decision: HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01-REVIEW v1.1, DELTA_APPROVE, docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md
immutable_base: HDE-CRD-0002 Implementation Plan v1.1, approved by IA-30 review v1.1 (INITIAL_APPROVE), docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
applicable_prior_addenda: the Specification delta 01 addendum (docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md); HDE Build Notes 2.18, the no-ceiling addendum (docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md; record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-no-cost-ceiling-v1.0.md); addenda 2.7 to 2.10 at their WU-PR-08 carried items; addendum 2.11
approved_delta: the overlay P-1 to P-20, reproduced in full below under "Approved delta, complete"
affected_surfaces: below, "Affected surfaces, dependencies and consequences"
exclusions: below, "Exclusions and nonclaims"
conflicts: below, "Conflicts"
unresolved_items: below, "Unresolved obligations and owners"
return_point: PR-10 — Create PR Work-Unit Instructions — 100926.1, for WU-PR-08
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (last addendum 2.18; this addendum takes the next number)
---

## 2.19 HDE-CRD-0002: Implementation Plan delta 01 is approved — no S01 or version cut, WU-PR-08 is S16 and S17 with one CI classifier registration, and WU-OPS-01 proves deployment by `release_id`

Timestamp: 102126 20:50 (UTC). Details: Records the IA-30 approval of the first material delta to the approved HDE-CRD-0002 Implementation Plan v1.1. The delta brings the Plan into line with Specification delta 01 and with two Product Owner directions of 2026-10-21. S01 and its packaging work leave the Plan. No release version cut is made; the release stays at `1.3.0`. WU-PR-08 covers S16 and S17 plus one classifier registration for `.env.example`, so its pull request runs all seven CI lanes. WU-OPS-01 proves the deployed candidate by `GET /internal/version` reporting its `release_id`, because deployments come from commits landing on `main`. The approved Plan v1.1 is unchanged; Plan v1.1 plus this delta is the current Plan.

### Source and approval

* Producing prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), mode MATERIAL\_PLAN\_DELTA\_REVIEW; release GCFPE-20261009.1 / 100926.1.
* Approval decision: DELTA\_APPROVE by Isis, continuing Lead Developer and whole-change Implementation Plan reviewer for HDE-CRD-0002, recorded in docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md, 2026-10-21.
* Approved delta: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md, logical ID HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01, version 1.1, authored by the whole-change Implementation Agent (session "HDE-CRD-0002-2") through IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1; file SHA-256 55e390a8848d02d6f4ffe9a26ff478afe34e97a79ee620285be9a017731d569e; landed by [\#683](https://github.com/amthorn78/glow-hdengine-v2/pull/683). Its application report is docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1-application-report.md.
* Lineage: change assessment v1.1 (PLAN\_DELTA\_REDLINE P-1 to P-17; docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md, [\#679](https://github.com/amthorn78/glow-hdengine-v2/pull/679)), which answered IA-40's REDLINE\_INCOMPLETE return on P-7 ([\#678](https://github.com/amthorn78/glow-hdengine-v2/pull/678)); delta v1.0 ([\#681](https://github.com/amthorn78/glow-hdengine-v2/pull/681)), denied by IA-30 review v1.0 (DELTA\_DENY, redlines D-1 to D-8; docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.0.md, [\#682](https://github.com/amthorn78/glow-hdengine-v2/pull/682)); delta v1.1 applies D-1 to D-8.
* Immutable base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (INITIAL\_APPROVE). The base file is not edited.
* Authorizing material change: Specification delta 01 (docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md, DELTA\_APPROVE by Thoth), recorded by the Specification delta 01 addendum, "HDE-CRD-0002: Specification delta 01 is approved — requirement S01 is removed and the release keeps its version, with a same-version manifest refresh for any member change" (record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md), and the Product Owner's OPTION 1 of 2026-10-21 (docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md).
* Product Owner directions applied: addendum 2.18, "Requirements and work units carry no cost ceiling; work continues until it is done"; and the deployment direction of 2026-10-21, "deploys come from github commits, this should already be well established", first recorded in IA-30 review v1.0 §2.

### Approved decision

The delta is approved as authored. It applies change assessment v1.1's redline P-1 to P-17 and review v1.0's redlines D-1 to D-8, which add items P-18 to P-20, and nothing else. It is material: it changes the scope of several planned work units (WU-PR-08, WU-DOC-01, WU-OPS-01), WU-PR-08's acceptance criteria, and the Plan's version-cut commitment. Unit, interface and risk identifiers are not renumbered.

Names used below: "the no-ceiling addendum" is addendum 2.18; "the Specification delta 01 addendum" is the addendum recorded at docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md.

### Approved delta, complete

Each item gives the Plan v1.1 anchor and the text in force from this approval. "This delta" means docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md.

#### P-1 — §2 "Lineage and sources": rows added after "Conflict register"

| Item | Exact identity |
| :---- | :---- |
| Specification delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, approved by `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; the Specification delta 01 addendum (`docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`) |
| Product Owner scope decision | `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` |
| This change assessment | `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md` (superseding v1.0 after IA-40's return, `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md`) |

#### P-2 — §3 opening paragraph

The clause "member-changing work lands before the version-bumping release cut (S01 unit last among code units)" reads:

> each member-changing unit carries its own same-version manifest refresh (no release version cut)

The rest of the paragraph is unchanged.

#### P-3 — §3 "Release-identity spine"

The sentences from "The single new release" to the end of the bullet read:

> No release version cut is made: the release stays at `1.3.0` and the admission constants do not change (Specification delta 01, C-5 and C-7). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member).

The bullet's first sentence is unchanged.

#### P-4 — §4 invariant 3

The clause "admission constants change only in WU-PR-08" reads:

> the admission constants (`ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC`, `ADMITTED_RELEASE_ROSTER`) do not change in this change

The rest of the invariant is unchanged.

#### P-5 — §5 IF-8 row

| ID | Interface | Shape |
| :---- | :---- | :---- |
| IF-8 | Wheel layout | Removed with S01 (Specification delta 01); not delivered |

#### P-6 — §6 traceability rows

| Requirement | Unit | Phase block | Live QA class |
| :---- | :---- | :---- | :---- |
| S01 | removed (Specification delta 01, C-1 and C-6); not delivered | — | — |
| Release re-cut | same-version refresh in each member-changing unit; no version cut (Specification delta 01) | — | — |

#### P-7 — §7 WU-PR-08 block (replaced from its heading through "Nonclaims")

##### WU-PR-08 — Environment template and operator documentation (PR; Coagulation)

- **Purpose.** S16 and S17 only: add the missing environment-template key, and correct the operator document's readiness and port statements. The classifier registration exists only so that S16's file change can pass CI. It adds no requirement.
- **Bounded scope.** S16, S17, and one classifier registration that makes `.env.example` a classified change surface. Nothing else.
- **Inputs.**
  - Audit §6 S16 and S17.
  - The items HDE Build Notes carries to the WU-PR-08 instruction:
    - the loopback bind statements (addenda 2.7, 2.8 and 2.9);
    - OBS-P4-5, O-19 and the production route exposure, contract F-3 (addenda 2.9 and 2.10).
  - **Not carried:** addendum 2.10's "cuts `1.4.0` from `release_id` `77204764…` (contract F-1)". The Specification delta 01 addendum approves no version cut and governs that overlapping scope (HDE Build Notes front matter §9, step 8: "apply only the highest-numbered applicable addendum to the overlapping scope"; noted in the IA-40 return record §4).
- **Deliverables.**
  1. `.env.example`: a `GEO_API_KEY` entry only.
  2. `docs/ADAPTER_009.md`: the readiness rules and port statements.
  3. `ci/checks/classify_ci_changes.py`: one registration that classifies `.env.example`. The author states its form at PR-20, choosing the smallest repository-grounded registration among the classifier's existing mechanisms.
  4. The registration's owner or pin test, only if one enumerates the registry the registration changes. The author states which, read from the repository.
  - **Repository facts for PR-20** (observed on `main` `7b763db`, identical to `a78b350` for these files; PR-20 re-reads them at its head and chooses):
    - The classifier's existing mechanism for a file that no code reads is the `_DOCUMENT_PATHS` set (`LICENSE`, `AcceptanceMap.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`). A path in it classifies as `documentation_only` with no lanes.
    - Nothing on `main` reads `.env.example`: no `.py`, `.sh`, `.yml`, `.toml`, `.json`, `requirements*.txt` or `Procfile` reference, and no dotenv loader. The one test hit is a literal in `tests/qa/test_generate_epic_close_pack.py` line 4338 (S16's acceptance text in a fixture). So `documentation_only` would not hide an affected change (Plan Templates, "CI lane classification and automated budget-control discipline").
    - No test enumerates `_DOCUMENT_PATHS` (searched `tests/`, `ci/` and `tools/`). The classifier's scenario table in `tests/evidence/test_rails_ci_workflow_integration.py` (`test_change_classifier_selects_expected_execution_scenarios`) pins example paths, not the set.
    - The other mechanism that fits is `_WORKFLOW_CONTROL_PATH_LANES`, a path-to-lanes map. It would select lanes for every future change to the template.
- **Dependencies and order.**
  - Eighth code unit, after WU-PR-07; the order is kept.
  - No release member changes, so there is no manifest refresh. `ci/checks/classify_ci_changes.py`, `.env.example` and `docs/ADAPTER_009.md` are not members of release `1.3.0` (45 members, `release_id` `77204764…`).
  - A change to the classifier is a full-validation path, so the PR runs all seven lanes.
  - **Lane selection, read from the classifier.** `ci/checks/classify_ci_changes.py` is in `_FULL_VALIDATION_PATHS`. In a throwaway clone of `a78b350`, one commit changed the three files: it registered `.env.example` in `_DOCUMENT_PATHS`, added `GEO_API_KEY` and corrected one port line. The classifier, called as `ci.yml` calls it with full SHAs, then exited 0 with `reason=selected_lanes` and all seven lanes (product, compat, db, rails, evidence, qa, release), and wrote 166 changed-test targets. With the registration, `.env.example` alone classified as `documentation_only`.
- **Acceptance and verification.**
  1. `.env.example` has a `GEO_API_KEY` entry and nothing else in it changed.
  2. The readiness section describes `/internal/readyz` as implemented and names the app that serves it. The port statements match the runner and Procfile bindings.
  3. Admission at the PR head reports `1.3.0`, 45 members and the base head's `release_id`, unchanged.
  4. At the PR head, the classifier run on `.env.example` alone returns a classification and no `CI_CHANGE_SURFACE_UNCLASSIFIED`.
  5. All seven lanes are green on the exact PR head, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Evidence obligations.** PR result record.
- **Risks and recovery.**
  - *Misclassification.* If a later change made code read `.env.example`, a `documentation_only` registration would skip its lanes. PR-20 re-checks the readers at its head, and the registration's form records why it is safe.
  - *The full run exposes failures that are not this unit's.* A classifier change runs every lane. A failure that is also red on the base is handled under PR-35's base-red rule, not by widening this unit.
  - *Document drift.* S17's statements are checked against `adapter/wsgi.py`, `adapter/factory.py`, `Procfile` and the canonical runner at the PR head. PR-40 checks the measure on the merged head.
  - R-2 and R-6 no longer apply. Recovery is as the common §7 terms state.
- **Nonclaims.** No release cut, no CI workflow change, no QA verdict.
- **Business case.** Carried by reference for PR-10 under addendum 2.11 rule 3, as the no-ceiling addendum narrows it: beneficiary, evidence, benefit and measure from `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` §2. No cost ceiling applies, and the decision record's "Cost ceiling" row is not in force (no-ceiling addendum, rule 1 and "Epic, task, and status effects"). The corrected fact the change assessment §5 records stands: the unit changes the classifier, so its PR runs all seven lanes.

#### P-8 — §7 WU-DOC-01, Bounded scope

The Bounded scope bullet reads:

> `README.md` (pre-push check usage; close-pack writer capability; test guidance); `CHANGELOG.md`; `AGENTS.md` operative passages (HDE-EPIC039 workflow posture → the extended close-pack capability and schema v2; HDE-EPIC040 current posture → release `1.3.0`, refreshed in place with no version cut, and its current `release_id`; the CI-exempt paths note verified against the workflow; pytest guidance); `docs/EVIDENCE_INDEX.md` (CRD admission, Mirror labels, close-run family); `docs/CLI_commands.md` final pass; `docs/server/reader_v1.md` (not-found limitation line removed). No canon, no generated evidence, no governed artifact by hand.

The rest of the block is unchanged.

#### P-9 — §7 WU-OPS-01: Intent, Success criteria, Constraints (revised by D-1 to D-3)

- **Intent.**

  > The Railway HD Engine production service runs the exact accepted candidate (the `main` head after WU-PR-08 and WU-DOC-01 merge) so that the QA Plan's bounded open-rails live steps (S02, S10 refusal in the deployed target; S14's live vendor call from the operator shell against the production rails) exercise that candidate. The candidate reaches the service when its commit lands on `main` (Product Owner direction of 2026-10-21, recorded in `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.0.md` §2).

- **Success criteria.**

  > `GET /internal/version` on the base URL reports the candidate's identity (the candidate's `release_id` at version `1.3.0`), which proves the candidate is deployed; the presence-only binding probe; all captured under `audit/ops/hde-crd-0002/wu-ops-01/` with path proofs (Plan Templates §3 evidence posture; lower-case directory names).

- **Constraints.**

  > No production configuration change by this task. The task does not discover or record the deployment trigger, build command or start command. Rollback intent: redeploy the previously deployed commit.
  >
  > **When the candidate's identity does not appear** (author statement, D-3). If `GET /internal/version` does not report the candidate's `release_id` once the candidate's commit has landed on `main`, the task reads it again after the service has had time to deploy. It does not inspect the deploy pipeline or the service settings.
  > - If a later read reports the candidate's `release_id`, the success criterion is met.
  > - Otherwise the task records each read: its time, its HTTP status, and either the `release_id` the endpoint reported or that the service did not answer. No secret value or raw body is recorded (Secret posture). The task changes no production configuration and stops.
  > - If the service did not answer at all, the task also redeploys the previously deployed commit under the rollback intent, and records that it did.
  > - The Product Owner decides any next step.
  >
  > The task judges deployment by `release_id` alone. `/internal/version`'s `build_commit` is a fixed value written in the source (`engine/runtime/identity.py`, `_STATIC_IDENTITY`, `"9479d28"`), so it does not identify the running commit.

The other WU-OPS-01 fields are unchanged.

#### P-10 — §9 item 2

The opening reads "The acceptance intents S02 to S22 (S01 removed by Specification delta 01) as the Specification states them, …". "the wheel-install admission test, " is deleted. The rest of the item is unchanged.

#### P-11 — §9 item 3

The clause "S01's class-2 step or its recorded exemption basis from WU-OPS-01's discovery; " is deleted. The rest of the item is unchanged.

#### P-12 — §10 heading and step 2

- **Heading:** "10. Release re-cut procedure (binding method for any unit that changes a release member: a same-version refresh)".
- **Step 2:** the sentence beginning "`<V>`/`<T>` are the current constants for a refresh" reads: "`<V>`/`<T>` are the current constants (`1.3.0` / `2026-08-24T18:04:49Z`); no version bump is made (Specification delta 01)."

The other steps are unchanged.

#### P-13 — §11 R-2, R-6 and R-8

| ID | Risk | Unit | Treatment |
| :---- | :---- | :---- | :---- |
| R-2 | Convergence run out of order or repeated with member changes in between. | WU-PR-03/04/05 | §10 restart rules; second-run byte stability. |
| R-6 | Removed with S01 (Specification delta 01). | — | — |
| R-8 | Three or four same-version manifest refreshes multiply convergence effort. | WU-PR-03/04/05 | Accepted: admission's byte binding leaves no alternative without rewriting the loader (a member); units are ordered to minimize refreshes. |

#### P-14 — §12 Exclusions

The clause "no release re-cut beyond the refreshes admission forces and the single `1.4.0` cut" reads:

> no release version cut: the release stays at `1.3.0`, with same-version refreshes only (Specification delta 01, C-5); S01 removed and not delivered (C-6)

The rest of §12 is unchanged.

#### P-15 — §13, the paragraph "No engineering decision remains open at Plan level; …"

This sentence is appended to the paragraph: "Specification delta 01 withdraws EC-11 (S01 packaging); EC-12 applies only as same-version refreshes."

#### P-16 — §14 Migration and rollback

The clause "; a reverted WU-PR-08 restores the `1.3.0` constants and manifest and re-converges" is deleted.

#### P-17 — Header and state

The front matter of this delta records:
- the approved base plus overlays: the immutable base, this assessment, Specification delta 01, the Specification delta 01 addendum and the no-ceiling addendum;
- the state, `PLAN_DELTA_PENDING`.

Plan v1.1's own header, §16 and §17 are not edited. §8 below takes the place of a new recovery envelope.

#### P-18 — §7 WU-OPS-01, PF07 posture (D-4)

The sentences from "PF07-gap (discoverable by OPS): the service's deployment trigger" to "it does not guess them." read:

> Deploy source: the candidate reaches the service when its commit lands on `main` of `amthorn78/glow-hdengine-v2` (Product Owner direction of 2026-10-21; a PO-provided deployed environment fact, which Glow Infrastructure §2.4 does not allow to be downgraded to `OPEN/TBD`). The build and start commands are not discovered or recorded; `GET /internal/version` reporting the candidate's `release_id` is the proof of deployment. The deploy-source fact is a Glow Infrastructure doc-delta candidate (§3.1, §4.1), owner the Product Owner.

The PF07-derived sentence before it is unchanged.

#### P-19 — §7 WU-OPS-01, External execution classification (D-5)

The sentence "Hosted-service operation (deployment or redeploy of the accepted commit; read of `/internal/version`; presence-only probe of the bindings)." reads:

> Hosted-service operation (read of `/internal/version`; presence-only probe of the bindings; a redeploy of the previously deployed commit only under the rollback intent). The candidate is deployed by its commit landing on `main`, not by this task.

"No vendor call, no database write." is unchanged.

#### P-20 — §11 R-9 row (D-6)

| ID | Risk | Unit | Treatment |
| :---- | :---- | :---- | :---- |
| R-9 | Removed: the deploy source is known; the candidate reaches the service when its commit lands on `main` (Product Owner direction of 2026-10-21). | — | — |

Unchanged by the delta: completed units WU-PR-01 to WU-PR-07 with their blocks and R-5 (executed history, including WU-PR-05's and R-5's "precede the version bump"); §1 and §8; §9 items 1, 4 and 5; §10 steps 1 and 3 to 12; §15; every interface other than IF-8; every risk other than R-2, R-6, R-8 and R-9; AQ-1; the unit order WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10; the conflict register CR-1 to CR-3; the WU-OPS-01 heading and Plan v1.1 §13's sentence on infrastructure facts, read with P-18 (the deploy source is a Product Owner-provided fact). The Implementation Audit is not revised; its S01, EC-11 and §7.3 version-bump text are superseded for planning by Specification delta 01 and this delta.

### Facts behind the decision

* The CI classifier refuses `.env.example`: `classify_paths(['.env.example'])` raises `CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`. `ci/checks/classify_ci_changes.py` is a full-validation path, so a pull request that registers `.env.example` runs all seven lanes (product, compat, db, rails, evidence, qa, release). `docs/ADAPTER_009.md` alone classifies as `documentation_only`. Measured on `main` at `bb263fc` and `397fca9`.
* No code reads `.env.example`. The other non-documentation files naming it are a fixture literal in `tests/qa/test_generate_epic_close_pack.py` and historical hash lists and notes that no code reads. No test names `_DOCUMENT_PATHS` outside the classifier.
* `.env.example`, `docs/ADAPTER_009.md` and `ci/checks/classify_ci_changes.py` are not members of release `1.3.0` (45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`), so WU-PR-08 makes no manifest refresh.
* `/internal/version` reports `release_id` derived from `catalog/manifest.json`; its `build_commit` is a fixed source value (`engine/runtime/identity.py`, `_STATIC_IDENTITY`, `"9479d28"`) and does not identify the running commit.
* No PF document states the HD Engine service's deploy source. Glow Infrastructure records the live start setting as unverified (§10) and the build artifact as TBD (§4.1), and states that PO-provided deployed environment facts must not be downgraded to `OPEN/TBD` (§2.4).

### Affected surfaces, dependencies and consequences

* Requirements: S01 leaves the Plan and is not delivered. S16 and S17 stay in WU-PR-08. No other requirement's unit, scope or acceptance changes.
* WU-PR-08: S16, S17 and one classifier registration for `.env.example`; its pull request runs all seven lanes; no manifest refresh; no CI workflow change. The registration's form is chosen at its PR-20 from the classifier's existing mechanisms. Its business case is the beneficiary, evidence, benefit and measure of the WU-PR-08 decision record §2, with no cost ceiling.
* WU-DOC-01: drops the dedicated-environment install note; states release `1.3.0`, refreshed in place with no version cut, and its current `release_id`.
* WU-OPS-01: the candidate reaches the service when its commit lands on `main`. `GET /internal/version` reporting the candidate's `release_id` at version `1.3.0` proves deployment. The unit records no deployment trigger, build command or start command, deploys nothing itself, and redeploys the previous commit only under its rollback intent.
* Release identity: version `1.3.0`, build time `2026-08-24T18:04:49Z`, 45 members, unchanged admission constants. `release_id` moves only by a same-version refresh in a unit that changes a member; no remaining unit is planned to.
* Tests: no wheel-install test and no pinned-identity rewrite to `1.4.0`.
* Risks: R-2 and R-8 cover WU-PR-03/04/05 only; R-6 and R-9 are removed; WU-PR-08 carries its own risks (misclassification, failures a full run exposes that are not the unit's, document drift).
* QA: the QA Plan needs no Live QA step or exemption for S01.

### Exclusions and nonclaims

* No unit added, removed or reordered; no interface added; no release version cut; no admission-constant change; no CI workflow change; no cost ceiling for any unit.
* Not delivered: a regular wheel install outside a source checkout still does not admit the release (Specification delta 01, C-6).
* This approval is not a PR Instruction, PR Proceed, Ops completion, deployment, QA verdict, acceptance or closure, and moves no PF09 or PF30 row.

### Conflicts

* Addendum 2.10 carries "WU-PR-08 (S17) cuts `1.4.0` … (contract F-1)"; addendum 2.6 states that WU-PR-08's version bump regenerates the engine-core purity report. The Specification delta 01 addendum approves no version cut and governs that overlapping scope. Neither statement applies to WU-PR-08; 2.10's other WU-PR-08 items (OBS-P4-5, O-19, F-3) and the loopback bind statements of 2.7 to 2.9 stay carried.
* Change assessment v1.1 and the WU-PR-08 decision record's "Cost ceiling" row carry a ceiling; addendum 2.18 takes them out of force.
* Change assessment v1.1 P-9 required WU-OPS-01 to record the live start command, and the Specification delta 01 addendum assigned "WU-OPS-01 records the deployment facts; Product Owner" as an unresolved obligation. The Product Owner's deployment direction supersedes P-9's start-command parts and discharges that obligation. The Specification text, including C-6's stated limit, is unchanged.
* The Specification delta 01 addendum's record and addendum 2.18 both carry the number 2.18. The delta and this addendum cite the former by title and record; no decision depends on its number.

### Unresolved obligations and owners

* Business cases for WU-DOC-01 and WU-OPS-01 (beneficiary, evidence, benefit, measure), due before DOC-10 and OPS-10: Product Owner.
* Glow Infrastructure doc-delta candidate: the HD Engine deploy source (commits landing on `main` of `amthorn78/glow-hdengine-v2`), §3.1 and §4.1: Product Owner.
* The PF10 number of the Specification delta 01 addendum, and the correction of addendum 2.11's internal cross-references: Product Owner.
* The registration's form: WU-PR-08's PR-20.

### Return phase

The continuation is PR-10 — Create PR Work-Unit Instructions — 100926.1, for WU-PR-08, from Plan v1.1 plus this delta.

### Relationship to existing HDE Build Notes guidance

This addendum applies the Specification delta 01 addendum and addendum 2.18 to the Implementation Plan, and records the Product Owner's deployment direction for HDE-CRD-0002. For WU-PR-08 it narrows the items addenda 2.6 and 2.10 carried, as stated under Conflicts. It supersedes no other addendum.
