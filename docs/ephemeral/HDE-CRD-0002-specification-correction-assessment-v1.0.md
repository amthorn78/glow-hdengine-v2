---
artifact_type: CRD_SPECIFICATION_CORRECTION_ASSESSMENT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION-CORRECTION-ASSESSMENT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: APPROVED_BASE_CORRECTION_ASSESSMENT
decision: CORRECTION_REDLINE
immutable_base: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480; approved by docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md, INITIAL_APPROVE, 2026-10-12T19:39:51Z)
base_state_after_assessment: unchanged; still SPECIFICATION_APPROVED
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Nathan / Product Owner, 2026-10-21, OPTION 1; blob efc220928f7c; landed by amthorn78/glow-hdengine-v2#673 as bc361f4)
pending_delta: none (this mode decides that one should be authored)
reviewer: Thoth, CF-C-30 (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum; reviewer of Specification v1.0 and v1.1)
author_return: Isis, Lead Developer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2), CF-C-40 APPROVED_BASE_FIRST_DELTA_AUTHORING
prompt: CF-C-30 — Review and Approve CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-21T18:27:29Z
repository_head_read: origin/main bc361f4
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.9.md (searched in full; addenda 2.11, 2.12 and 2.16 read in the passages that govern this decision)
pf10_addendum: none (assessment mode creates none)
next_prompt: CF-C-40 — Revise CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a)
next_mode: APPROVED_BASE_FIRST_DELTA_AUTHORING
---

# HDE-CRD-0002 — Specification correction assessment v1.0 (CF-C-30)

## 1. Decision

**CORRECTION_REDLINE.** The Product Owner's scope decision of 2026-10-21 (OPTION 1) is an actual authorized product and scope decision. It justifies one bounded correction to the approved Specification, and no product or scope choice remains open.

The decision has four parts:
- remove S01;
- drop the `1.4.0` version cut, so the release stays at `1.3.0`;
- keep S16 and S17;
- replace the constraint that a member change forces new admission pins with a same-version manifest refresh.

The approved Specification stays exactly as it is, and still `SPECIFICATION_APPROVED`. Isis authors one pending `SPECIFICATION_DELTA` in CF-C-40 from the redline in §3, and the delta returns to this reviewer under `APPROVED_BASE_DELTA_REVIEW`.

This assessment approves no delta and creates no PF10 addendum. It authorizes no Implementation Plan change, PR work, Ops, QA, canon change, acceptance or closure.

## 2. Assessment

### 2.1 Authority

- The decision record quotes the Product Owner verbatim ("approve option 1, give me the handoff") and states OPTION 1 in full in its §2. It was recorded by Isis, the continuing Lead Developer, as recorder only.
- Removing a requirement and fixing the release version are scope choices. They belong to the Product Owner (CF-C-30, *APPROVED_BASE_CORRECTION_ASSESSMENT*: "an actual authorized Product Owner product/scope decision").
- The decision answers exactly what the WU-PR-07 lineage review returned to the Product Owner before WU-PR-08's PR-10: WU-PR-08's business case and the S01 real-input fact (HDE Build Notes addendum 2.16, "Decisions returned to the Product Owner" (1); addendum 2.12, decision 4).
- No part needs a further Product Owner choice. S16 and S17 keep their approved scope and acceptance intents.

### 2.2 Basis, checked on `main` at `bc361f4`

The reviewer does not re-decide a Product Owner scope choice. The basis was checked so the redline states no false fact.

| Claim in the decision | Checked | Result |
| :- | :- | :- |
| Production runs the engine from the checkout | `Procfile`: `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …` | Holds. `-m` puts the working directory first on the import path. The record states its own limit: the live Railway start setting is unverified (Glow Infrastructure §10) |
| S01 has no real input | HDE Build Notes addendum 2.11 rule 4 (real inputs); its "Epic, task, and status effects" left S01 "open … on rule 3" until the fact was established | Consistent. The record supplies the fact, and rule 5 bars work justified only by an input outside the real set |
| A member change can refresh the manifest at the current version without new admission pins | `catalog/manifest.json` at the four HDE-CRD-0002 merges `c98d41f`, `2f3db0a`, `5892538` and `822ce15` | Holds. Version `1.3.0`, build time `2026-08-24T18:04:49Z` and 45 members are unchanged throughout. `release_id` went `52be4558…` → `72fca4c3…` → `d84d99e1…` → `2f18a5eb…` → `77204764…`. The `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER` lines in `engine/config/registry_loader.py` did not change across those merges |
| S16 and S17 change no release member | The member list of `catalog/manifest.json` (45 paths) | Holds. Neither `.env.example` nor `docs/ADAPTER_009.md` is a member |
| "Packaging metadata" in Affected surfaces is S01's alone | `git log c98d41f^..bc361f4 -- pyproject.toml` | Holds. No HDE-CRD-0002 unit changed `pyproject.toml`. S06's locus is the attestation builder, which Affected surfaces lists separately |

### 2.3 Fit with canon

- **Material change.** Removing S01 changes approved scope, exclusions, phase structure and dependency order. That is a material change under HDE CRD Records §4.2, so it takes the delta route: an immutable base, a pending delta, Thoth's delta review, and on approval one HDE Build Notes addendum (CF-C-30 Execute steps 3 to 5). It never edits the approved record in place (HDE Governance §9.1.1).
- **Format.** The delta uses the base Specification's canon format (Change Process Guide §0.1A: "A delta Specification uses the applicable governing base format"), which is HDE CRD Records §4.2 and §7.
- **Business case.** The delta adds no requirement, so HDE Build Notes addendum 2.11 rule 3's Specification gate ("blocks a requirement without a business case") has nothing new to test. The business case for the reduced WU-PR-08 (S16, S17) is in the decision record §2, for the unit's PR-10 under the same rule.
- **Release identity.** This stays manifest-derived (`AGENTS.md`, "Release identity"). The redline changes only what the Specification requires of a member change; it changes no identity rule.

## 3. Bounded correction redline

The delta applies exactly these changes, as an overlay on the immutable base. Text quoted below is the base's current text. "Replace with" text is the required wording; the author may adjust phrasing only where the meaning is unchanged. Requirement IDs are not renumbered.

| # | Base location | Base text (quoted or exact anchor) | Required change |
| :- | :- | :- | :- |
| C-1 | Requirements table, S01 row | Scope "Package every release member with the distribution"; acceptance intent "A regular wheel install admits the complete release outside a source checkout" | Keep the ID and the Source cell (`5(a), O-12`). Scope becomes: "Removed by the Product Owner's decision of 2026-10-21 (`docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`)". Acceptance intent becomes: "None — not delivered" |
| C-2 | Intake → Bounded scope | "S01 to S22 below." | "S02 to S22 below; S01 is removed (Exclusions)." |
| C-3 | Intake → Expected outcome | "every acceptance intent S01 to S22 holds on `main`" | "every acceptance intent S02 to S22 holds on `main`" |
| C-4 | Intake → Affected surfaces | "code: packaging metadata, the production HTTP adapter …" | Delete "packaging metadata, ". Nothing else in the field changes |
| C-5 | Exclusions, bullet 2 | "No release re-cut beyond what the in-scope requirements require." | "No release version cut: the release stays at its current version, `1.3.0`, and no new admission version or build time is set (Product Owner decision of 2026-10-21)." |
| C-6 | Exclusions (new bullet, placed after bullet 2) | — | "S01 (5(a), O-12), every release member packaged with the distribution, is removed by the Product Owner's decision of 2026-10-21. Basis: production starts the engine from the checkout (`Procfile`: `python -m gunicorn 'adapter.factory:create_app()'`) and CI installs in editable mode, so S01 rests on no real input (HDE Build Notes, real-input rule). Not delivered: a regular wheel install outside a source checkout still does not admit the release." Cite HDE Build Notes by title alone, as Plan Templates "Canon precedence for template use" requires of derived references |
| C-7 | Constraints → Release members | From "Those of S01 (`pyproject.toml`) and S02 (`adapter/factory.py`) are not." to the end of the bullet ("… one coherent re-cut after the member-changing work lands.") | Replace with: "That of S02 (`adapter/factory.py`) is not. Any requirement whose implementation changes a release member forces a manifest refresh at the current version, not new admission pins; the Implementation Audit establishes the actual set." Keep the bullet's first two sentences (45 members; the S07, S08, S10 and S14 loci) unchanged |
| C-8 | Phase blocks, Conjunction row, Dependencies cell | "Coordinates with the release re-cut where a requirement changes a release member (S07, S10 by observed locus)." | "Coordinates with a same-version manifest refresh where a requirement changes a release member (S07, S10 by observed locus)." The S19 sentence stays |
| C-9 | Phase blocks, Fermentation row, Dependencies cell | "Coordinates with the release re-cut (S08, S14 by observed locus)" | "Coordinates with a same-version manifest refresh (S08, S14 by observed locus)" |
| C-10 | Phase blocks, Coagulation row | Purpose "Durable packaging and environment discipline: S01, S16, S17"; Dependencies "S01 converges with the release re-cut"; Completion boundary "S01, S16 and S17 hold on `main`" | Purpose: "Durable environment discipline: S16, S17". Dependencies: "None; S16 and S17 change no release member". Completion boundary: "S16 and S17 hold on `main`". Status and the other columns are unchanged |
| C-11 | The "Recommended ordering" line below the phase blocks | "…; the release re-cut after all member-changing work lands; …" | Delete that clause. The rest of the line is unchanged ("S03 to S05 early …; S22 before QA; S21 before HDE-CRD-0002's closeout") |
| C-12 | Canon, QA & Build Notes posture → Production-affecting Live QA minimum table | The row "Production-affecting, outside the functional-feature scope; … \| S01 \| Packaging of the deployed service. …" | Delete the row. No remaining requirement is in that class. The other three rows are unchanged |
| C-13 | Closure result → Superseded or rejected scope | `None` | "S01, removed by the Product Owner's decision of 2026-10-21 (`docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`)" |
| C-14 | Material-change history | One row (2026-10-12, Specification approval) | The delta states the row its approval adds, without overwriting the existing row (HDE CRD Records §4.2). Affected fields: approved scope (S01), exclusions, Release-members constraint, phase structure and dependencies (Conjunction, Fermentation, Coagulation, ordering), Live QA classification, superseded scope. Decision source: the Product Owner decision record and the CF-C-30 delta approval. Build Notes reference: the addendum that approval creates |

### 3.1 Passages that stay unchanged, with the reason

- **Intake → Observed need or requested change** ("… packaging, …"). It records what was observed at intake. The removal is recorded where HDE CRD Records puts it: Exclusions (C-6) and Superseded or rejected scope (C-13).
- **Intake → Why warranted.** It names no S01 content.
- **Intake → Lead Developer finding** ("CRD lane: yes for S01 to S22"). The finding stands as made. S01 is removed by a Product Owner scope decision, not by a negative finding.
- **Kickoff open points, U-1 to U-7.** None names S01.
- **The canon conflict register as carried, and every other requirement, exclusion, constraint, compatibility dependency (CD-1 to CD-3) and RD-1.**
- **Record control, Specification approval and Exact-source execution & decision lineage.** These change only as the delta-approval route records them; the delta itself does not rewrite the base's approval.

### 3.2 What the delta must state besides the overlay

As CF-C-40 Execute step 3 requires:
- the immutable base by repository path and approval lineage;
- the authorizing Product Owner decision;
- the affected requirements: S01 removed, and S16 and S17 regrouped;
- the preserved exclusions;
- this assessment as its evidence;
- conflicts: none (§5);
- the canon cited for its format (HDE CRD Records §4.2 and §7, under Change Process Guide §0.1A);
- the unresolved items in §4;
- the return phase in §3.3.

### 3.3 Return phase for the delta

After DELTA_APPROVE, the affected native receiver is IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), in `APPROVED_BASE_CHANGE_ASSESSMENT` mode.
- The receiver is Isis, as Plan reviewer.
- The request is the approved delta with the Product Owner decision, as the authorized material-change request against the immutable Implementation Plan v1.1 and its review.
- The Plan passages the decision record lists in §3 "Later route" are the affected anchors.
- WU-PR-08's PR-10 follows the Plan change, not the Specification delta directly.

## 4. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The live Railway start setting is unverified (Glow Infrastructure §10). If production ever ran without the checkout, admission would refuse to start (`MISSING_FILE`). This is recorded in the decision as a stated limit, not a blocker | WU-OPS-01, which records the deployment facts; Product Owner |
| The Implementation Plan v1.1 change (WU-PR-08 scope, the `1.4.0` passages, WU-OPS-01's success criterion, R-2, R-6, WU-DOC-01's AGENTS.md line) | Isis through IA-30, then the Implementation Agent through IA-40, after the delta is approved |
| The HDE Build Notes addendum recording the approved delta | Thoth at DELTA_APPROVE; publication into PF10 by the Product Owner |

## 5. Conflicts

None.
- The decision conflicts with no PF canon: the Specification and Plan never cited a canon requirement for a version cut.
- Release identity stays manifest-derived.
- HDE Build Notes addendum 2.11 supports the removal (rules 4 and 5).
- The carried canon conflict register is unaffected.

## 6. TypeSafe reading for the receiving session (CF-C-40)

Action sent (v8.2): "Author the first pending Specification delta against an already approved 22-requirement CRD Specification, applying an independent reviewer's exact correction redline of about a dozen bounded passages: remove one packaging requirement under a Product Owner scope decision, and change the release-member constraint and four related phase-block and exclusion passages so the change keeps its current release version. The delta is one Markdown record in the base Specification's canon format; no code is written and no live run occurs, and the same reviewer reviews the delta before an approval addendum is issued."

- **TypeSafe v8.2: Opus 5.5 at medium.** Effort score 1.45 (confidence 0.69); rung probabilities low 0.01, medium 0.57, high 0.39, extra high 0.03, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.66, Sonnet 5.5 0.33, Haiku 5.5 0.01 (confidence 0.55). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.007, Opus 5.5 at medium 0.376, Opus 5.5 at high 0.257, Opus 5.5 at extra high 0.020, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.003, Sonnet 5.5 at medium 0.188, Sonnet 5.5 at high 0.129, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.006, Haiku 5.5 at high 0.004, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and medium. Sent 2026-10-21T18:27:29Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T18:27:29Z; HTTP 200 in 0.62 s; 5448 input and 71 output tokens; jev-1.13.0. Rung by rule: medium (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and medium.
- **Nathan's pick for CF-C-40:** not stated.
- **Nathan's pick for this CF-C-30 session:** not stated (reading recorded in the decision record §5).
- **Notion row:** not written (CF-C-30 handoff rule).

**Surface advice:** run CF-C-40 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access.
- It reads from `main`: the approved Specification, this assessment, the Product Owner decision record, and HDE CRD Records §4.2 and §7 in `docs/pfcanon/`.
- It writes only the pending delta under `docs/ephemeral/`.
- It needs no live vendor, production or database access, and runs no tests.

## Canon relied on

Read on `main` at `bc361f4`. Each entry gives the source, the sections read, and the decision topics they govern.

**CF-C-30 — Review and Approve CRD Specification — 100926.1.** Read in full; page state 2026-10-12, unchanged since review v1.1. Governs:
- the mode's inputs;
- Execute step 3 (CORRECTION_REDLINE; the base remains unchanged);
- routing to CF-C-40;
- no addendum in this mode.

**CF-C-40 — Revise CRD Specification — 100926.1.** Read on 2026-10-12, for its `APPROVED_BASE_FIRST_DELTA_AUTHORING` contract. Governs what the delta states (§3.2).

**IA-30 — Review Whole-Change Implementation Plan — 100926.1.** Read in full for this assessment. Governs the `APPROVED_BASE_CHANGE_ASSESSMENT` mode named as the delta's return phase (§3.3).

**PF10-HDE-Build-Notes v13.6.9.** The whole file was searched for "S01", "1.4.0", "admission pin", "re-cut", "WU-PR-08" and "real input". Read:
- addendum 2.11 in full (rules 1, 3, 4 and 5; "Epic, task, and status effects" on WU-PR-08 and S01);
- addendum 2.12, "Epic, task, and status effects" and "Deferred obligations" (decision 4);
- addendum 2.16, "Approval and source record" and "Epic, task, and status effects" (the decisions returned to the Product Owner).

Addendum 2.17 was searched and makes no decision on S01, `1.4.0` or WU-PR-08. Addendum 2.1 governs the TypeSafe reading.

**Read for review v1.0 and v1.1; unchanged on `main`:**
- **PF04-Canon-HDE-Governance v2.8.7** §9.1.1 (approval applies to the exact artifact; an approved base is not patched) and §9.1.2 (Product Owner dispositions govern within their scope).
- **PF06-Canon-Change-Process-Guide v2.5.4** §0.1A ("Specification format authority": a delta uses the governing base format).
- **PF27-Canon-Plan-Templates v2.0.5**, "Canon precedence for template use" (HDE Build Notes cited by title alone in derived references, for C-6).
- **PF30.1-Canon-HDE-CRD-Records v0.9.1** §4.2 (material update and append-only history, for C-14), §3.3, and §7 (the "Superseded or rejected scope" field, for C-13).
- **PF07-Canon-Glow-Infrastructure v2.3.3** §10, cited through the decision record for the unverified start setting; not re-read here.

**`AGENTS.md`:** "Release identity" and the HDE-EPIC040 current posture (manifest-derived `release_id`; admission pins in `engine/config/registry_loader.py`; 45 members).

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (the passages in §3; the whole file was read at approval);
- `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md` (own decision).

**Repository facts read on `main` at `bc361f4`:**
- `Procfile`;
- `catalog/manifest.json` at five commits;
- the `ADMITTED_RELEASE_*` lines of `engine/config/registry_loader.py` and their history;
- the `pyproject.toml` history since `c98d41f^`.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / CF-C-30 / approved-base correction assessment 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Thoth / CF-C-30 APPROVED_BASE_CORRECTION_ASSESSMENT |
| capture time | 2026-10-21T18:27:29Z |
| execution identity | https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| repository persistence | recorded here only |
