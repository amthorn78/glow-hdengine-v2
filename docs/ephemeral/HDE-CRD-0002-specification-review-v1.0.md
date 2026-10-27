---
artifact_type: CRD_SPECIFICATION_REVIEW
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION-REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: INITIAL_SPECIFICATION_REVIEW
decision: INITIAL_DENY
reviewed_artifact: docs/ephemeral/HDE-CRD-0002-specification-v1.0.md
reviewed_artifact_version: "1.0"
reviewed_artifact_blob: fcdd116b5253fb00a15caf1176ab9ad3487bf3b9 (29,614 bytes; landed on main at 9f710bb, amthorn78/glow-hdengine-v2#615)
reviewed_artifact_state_after_review: SPECIFICATION_PENDING (unchanged; sentinel remains "ASK OK?")
kickoff_ref: docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md
reviewer: Thoth, CF-C-30 (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
author: Isis, Lead Developer (author of the reviewed Specification)
prompt: CF-C-30 — Review and Approve CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-12T19:24:01Z
repository_head_read: origin/main 9f710bb
pf10_addendum: none (initial review; CF-C-30 step 2)
next_prompt: CF-C-40 — Revise CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a)
next_mode: PREAPPROVAL_REVISION
next_actor: Isis
---

# HDE-CRD-0002 — Specification review v1.0 (CF-C-30)

## 1. Decision

**INITIAL_DENY.** HDE-CRD-0002 Specification v1.0 is not approved. It stays `SPECIFICATION_PENDING` with `ASK OK?`. It returns to the same author, Isis, through CF-C-40 in `PREAPPROVAL_REVISION` mode, with the four required redlines in §2 and §3.

The Specification is close to approvable. Its PF30.1 record structure, scope-level discipline, phase blocks, Lead Developer finding, RD-1 routing and canon-conflict interim treatments are sound (§5). Each of the four defects is a contradiction or omission that the Implementation Audit would otherwise have to resolve by silently expanding or reinterpreting the Specification. HDE Governance §9.1.1 forbids that: "An incomplete, contradictory or insufficient approved Specification returns to its own revision cycle with evidence; IA MUST NOT expand or reinterpret it silently."

This decision creates no PF10 addendum, approves no delta, and authorizes no implementation, planning, QA, Ops, canon change, acceptance or closure.

## 2. Required redlines (summary)

| # | Location in v1.0 | Defect | Consequence if unchanged |
| :- | :- | :- | :- |
| R1 | Exclusions, bullet 5; Canon, QA & Build Notes posture → QA requirement | Excludes "deployment … or live vendor call" for the whole change, and the QA posture omits the production-affecting Live QA minimum and the affected-surface identification canon assigns to the Specification | The QA Plan cannot both obey the Specification and be approval-ready, so HDE-CRD-0002 cannot reach QA acceptance |
| R2 | Compatibility dependencies, CD-3 | Records the evidence-index updater's CRD admission as "Not observed", with no treatment that delivers it. Verified: the updater admits only `HDE-CRD-0001` | HDE-CRD-0002 QA evidence cannot be published by the sole Index/Mirror writer, and no requirement in S01–S21 lets the Implementation Audit fix it |
| R3 | Requirements, S16 | Scope adds `GEO_API_KEY`; acceptance intent requires every key the service requires. Verified: `.env.example` lacks several keys the service reads | Implementing the scope fails the acceptance intent; meeting the acceptance intent needs scope the Specification does not state |
| R4 | Constraints → Release members; Exclusions, bullet 2 | Names S01, S02, S07 and "possibly S14" as member-changing. Verified: S08's, S10's and S14's observed loci are release members; S01's and S02's are not. The exclusion forbids a re-cut that S08 or S10 would require | Contradictory scope: an in-scope fix may require a re-cut the Specification excludes |

## 3. Required redlines (detail)

### R1 — The deployment and live-vendor-call exclusion contradicts mandatory QA, and the QA posture omits the affected surfaces

- **Defect.** Exclusions bullet 5 reads: "No deployment, production configuration change or live vendor call." Nothing limits it to implementation work, so it binds the whole change, QA included. The QA requirement line says "full independent QA under Glow QA Guide, at the rigor Epic work receives". It does not state that the production-affecting Live QA minimum applies. It also does not identify which requirements touch a production-functional surface.
- **Controlling source.**
  - Glow QA Guide "Change-lane QA applicability (normative)" applies the same QA rigor to CRDs.
  - Glow QA Guide §3.5.5, "Production-affecting Live QA minimum": a change that can affect real production functionality, deployed runtime behavior, vendor ingest, CLI behavior, operator-facing CLI surfaces or public behavior needs "at least one bounded open-rails live QA step that proves a real production-relevant behavior in the deployed or live environment". Where the change touches a surface used to produce a production feature PF canon describes as functional, the QA Plan "MUST include a live vendor call under open rails … A plan without that test is not approval-ready". It also says: "The approved Specification and plans identify the affected surfaces."
  - Change Process Guide §1.1.5A (same rule), §0.1A (equal rigor across lanes) and §1.0.4 (a CRD follows the downstream Epic process).
- **Material consequence.** In-scope requirements change production-affecting behavior:
  - S02: 404s from the production app (`adapter.factory`, per the `Procfile`);
  - S10: a dev route the production factory mounts;
  - S14: the `hdctl bg:resolve --source vendor` production override (CLI/API/Vendor Ref §7.1.11);
  - S07 and S08: operator-facing CLI behavior.

  A QA Plan written within the exclusion cannot include the required live step or the live vendor call, so it is not approval-ready. A QA Plan that includes them contradicts the approved Specification. Either way, the Expected outcome "verified by independent QA" is unreachable. S02's own warrant ("live on the public production surface") also cannot be proven while deployment is excluded.
- **Required correction.**
  1. Rewrite Exclusions bullet 5 so it does not exclude, for this change, either of these:
     - the bounded open-rails Live QA required by Glow QA Guide §3.5.5 and Change Process Guide §1.1.5A, including the synthetic-data live vendor call where that rule applies;
     - a Product Owner-authorized deployment or Ops task needed to place the QA candidate in the deployed or live target those steps exercise.

     Exclusions the author intends only for implementation work may stay, if they are stated as implementation-only. Examples: no production configuration change as implementation work, and no live vendor call made by an implementation work unit.
  2. Under **Canon, QA & Build Notes posture → QA requirement**, state that the production-affecting Live QA minimum applies. Identify which in-scope requirements touch a surface used to produce a production feature that PF canon describes as functional. If none do, say so with the basis.
- **Left to the author.** Which surfaces qualify, and how each is worded. This review does not identify them (Plan Templates, "Source-bound review authority and exact-fix limits"). Deployment mechanics and Ops task identities belong to the Implementation Plan and QA Plan, not the Specification.

### R2 — CD-3 is observable now: the canonical evidence-index updater admits only HDE-CRD-0001

- **Defect.** CD-3 says it is "Not observed" whether the canonical evidence-index updater's per-change registration admits CRD QA-root artifacts. Its treatment is "The Implementation Audit establishes it before QA relies on it." It names no requirement or route that would deliver the admission.
- **Verified repository fact (main 9f710bb).**
  - `tools/evidence/update_evidence_index.py` lines 47–51: `CRD_QA_ID = "HDE-CRD-0001"`, `CRD_QA_ROOT_REL = "audit/qa/hde-crd-0001"`, `CRD_QA_KEY = "audit.qa.hde_crd_0001"`, under the comment "Source-owned admission for this approved CRD. This is not a check roster or directory discovery rule; another CRD needs its own explicit admission."
  - A search of `tools/` and `ci/` (`*.py`, `*.sh`) for `HDE-CRD-0001` / `hde-crd-0001` finds only this file.
  - `tools/qa/qa_harness.py` line 23 already accepts any `HDE-CRD-[0-9]{4,}`, so the updater is the only single-CRD admission found.
- **Controlling source.**
  - HDE Schemas & Artifacts §8.17, "Change-container identity": "Before the first affected CRD enters QA, every schema, validator, generator, manifest producer, or helper that accepts only epic identity or `EPIC_QA_ROOT` MUST be identified and updated through the authorized change lane."
  - Plan Templates §2A, "Existing-template reuse and substitution": the CRD Specification "MUST record that compatibility dependency and route it to the owning canon or change lane before the affected CRD relies on it."
  - `AGENTS.md` makes `tools/evidence/update_evidence_index.py` the sole active writer of the Index, Mirror and their companions.
  - HDE Governance §9.1.1: IA must not expand the Specification.
- **Material consequence.** HDE-CRD-0002 QA evidence under `audit/qa/hde-crd-0002/` cannot be published by its sole writer. No requirement S01–S21 covers the admission, so the Implementation Audit cannot plan it without silently expanding scope. QA would block.
- **Required correction.**
  1. Replace CD-3's "Not observed" with the verified fact above.
  2. Give CD-3 a treatment that guarantees the canonical updater admits HDE-CRD-0002's QA-root artifacts before HDE-CRD-0002 enters QA, preserving existing Epic and HDE-CRD-0001 inputs. Use one of:
     - an in-scope requirement with its own acceptance intent, placed in a phase block; or
     - a named authorized change lane and owner that delivers it before QA, recorded as a dependency of the Expected outcome.
- **Left to the author.** Which of the two treatments (Plan Templates §2A permits either), and the requirement's wording.

### R3 — S16's scope and acceptance intent state different bounds

- **Defect.** S16 scope: "Add `GEO_API_KEY` to the environment template". S16 acceptance intent: "`.env.example` names every environment key the service requires".
- **Verified repository fact (main 9f710bb).**
  - `.env.example` names only `HD_API_BASE_URL`, `HD_API_KEY` and `HD_API_SECRET`.
  - The service also reads, among others, `APP_ENV`, `SAFE_MODE` and `ALLOW_NETWORK` (`os.environ` reads in `engine/` and `adapter/`).
  - `engine/providers/vendor_http_hdapi.py` line 67 requires `HD_API_KEY` and `GEO_API_KEY`.
  - `AGENTS.md` names `DATABASE_URL` as the only active DB transport configuration surface.
- **Controlling source.** HDE Governance §9.1.1 (a contradictory Specification returns to revision; IA must not reinterpret it). Plan Templates, "Materiality-based blocker discipline": contradictory state is not waived.
- **Material consequence.** A candidate that implements the stated scope fails the stated acceptance intent. A candidate that meets the acceptance intent implements keys the scope does not name, which IA may not add.
- **Required correction.** Make S16's scope and acceptance intent state the same bound. The source-backed bound is `GEO_API_KEY` (kickoff §4, item 5(h)). For that bound, replace the acceptance-intent cell with: "`.env.example` has a `GEO_API_KEY` entry". If the author widens S16 instead, the scope cell must enumerate each key with its source, and the acceptance intent must name the same keys.

### R4 — The release-member constraint misstates which requirements change members, and the re-cut exclusion forbids required work

- **Defect.**
  - Constraints → Release members: "S01, S02, S07 and possibly S14 change release members. Each forces a manifest re-cut and new admission pins".
  - Exclusions bullet 2: "No release re-cut beyond what S01, S02, S07 or S14 requires."
  - The source exclusion carried by the kickoff (§4, item 5, Exclusions [S]) is broader: "No release re-cut beyond what (a), (b), (e) or (f) requires". Item 5(e) covers all seven carried defects, S07 to S13. The Specification narrowed (e) to S07.
- **Verified repository fact (main 9f710bb).** `catalog/manifest.json` lists 45 release members.

  | Member? | File | Observed locus of |
  | :- | :- | :- |
  | Yes | `engine/cli/main.py` | S07 (help text, line 79), S08 (`aux-preview --band`, line 131), S14 (`bg:resolve` parser, line 138) |
  | Yes | `adapter/http_reader.py` | S10 (`APP_ENV` gate, line 603) |
  | Yes | `engine/bodygraph/resolver.py` | S14 (vendor resolver) |
  | No | `pyproject.toml` | S01 |
  | No | `adapter/factory.py` | S02 (production app per the `Procfile`) |
- **Controlling source.** `AGENTS.md`, "Release identity": `release_id` derives from `catalog/manifest.json`, and intentional cuts change only that file. HDE Governance §9.1.1, as above.
- **Material consequence.** If S08's or S10's fix changes its observed locus, the change requires the re-cut and new admission pins the exclusion forbids. The Implementation Audit then faces a contradiction it may not resolve. The constraint also tells it the wrong requirements drive the re-cut.
- **Required correction.**
  1. Exclusions bullet 2 becomes: "No release re-cut beyond what the in-scope requirements require."
  2. In Constraints → Release members, replace the first sentence with the verified fact: the observed loci of S07, S08, S10 and S14 are release members; those of S01 and S02 are not; any requirement whose implementation changes a release member forces the re-cut; the Implementation Audit establishes the actual set. Keep the existing sentence on converging to one coherent re-cut.

## 4. Non-gating notes (no correction required)

- **N1.** The "Specification format authority" paragraph sits in Change Process Guide **§0.1A**, not §0.1. The Specification cites "§0.1" in Format and register posture, U-7 and Canon relied on. The cited format owner, PF30.1 §4.1 and §7, is correct. The revision may fix the citation.
- **N2.** The canon conflict register omits some conflicting passages, and its entries lack three fields of the carried `CANON_CONFLICT_REGISTER` contract: affected requirements, alternatives and unresolved risk. The dispositions in §6 add the omitted passages. The revision may add the three fields.
- **N3.** The warrant says "Regressions in 129 test files are invisible to CI (S03)" as a current fact. 129 is the PR05 count, and U-1 says it was not recounted. Attributing it ("129 at PR05") would keep the claim exact.
- **N4.** Exclusions say "No new evidence family". S21 requires "an admitted home for close-workflow run evidence". Stating whether that home lies inside an existing family or is admitted by S21's ADR would remove a possible reading conflict for the Implementation Audit.
- **N5.** Any live S14 step is subject to CLI/API/Vendor Ref §7.1.11e. The authorized initiator is an authenticated human Product Owner, or a human operations executor the Product Owner delegates. An AI agent, CI job or unauthenticated shell cannot self-authorize. This bears on R1's surface identification and on QA planning.
- **N6 (record currency, not a Specification defect).** The Notion board card "HDE-CRD-0002 — Candidate CRD Items 5–8 …" (Board Cards, last edited 2026-10-11T20:08Z) still cites briefs v1.1 in an open #601, says the CF-PO-10 artifact is not recorded, and says "Not started: Specification". On `main`:
  - the class selection is `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md` (#612);
  - the kickoff is #613;
  - the pending Specification is #615.

  This session executes the flow and is read-only toward Notion, so the card is left for its owner.

## 5. Reviewed and found sound

| Area | Finding | Basis |
| :- | :- | :- |
| Record format | Every PF30.1 §4.1 minimum field is present, in §7 template order. "Specification approval" replaces "CRD Plan approval" with a stated reason, matching the HDE-CRD-0001 record (PF30.1 §8). `Registered` and `Planned` are valid §3.3 values | PF30.1 §3.3, §4.1, §4.3, §7, §8; Change Process Guide §0.1A |
| Scope-level content | No planned PR or Ops units; work units recorded as `Pending — identified by the change-wide Implementation Plan`; paths stated as evidence, not required implementation paths | HDE Governance §9.1.1; PF30.1 §4.1 (v0.9.1); Change Process Guide §0.5.1 "Plan path provenance" |
| Lead Developer finding and lane | Valid, not already satisfied, and in the CRD lane for S01–S21; item 6(a) found not CRD lane | PF30.1 §3.2; Change Process Guide §1.0.2; HDE Governance §9.1 "Epic and CRD change lanes" |
| RD-1 routing of item 6(a) | The factual basis holds: PR-30 — PR Implementation Proceed — 100926.1 publishes "only after a coherent locally tested checkpoint" (Execute step 3). The kickoff assigned this decision to the Specification (U-3) | PR-30 prompt (read 2026-10-12); kickoff §2, §7 |
| Phase blocks | Purpose, scope, dependencies and completion boundaries are explicit; assignments are consistent with phase meanings | Change Process Guide §1.0.4; PF30.1 §4.3; 7 Phases of Alchemical Engineering §4–§7 |
| S21 and its ADR | Canon impact, drainage targets and the ADR requirement are recorded; the ADR is approved before S21's behavior is relied on | Change Process Guide §1.0.5; HDE Governance §9.7.3; PF30.1 §4.1 |
| CD-1, CD-2 | Correctly stated and routed | HDE Schemas & Artifacts §1.2 "Change-container compatibility"; Plan Templates §2A |
| QA root | `audit/qa/hde-crd-0002/` is canon-defined | Glow QA Guide "Change-lane QA applicability (normative)" |
| Facts checked on main 9f710bb | S05: `ci.yml` `paths-ignore` lists 4 prefixes, `_DOCUMENTATION_PREFIXES` lists 8. S10: `adapter/http_reader.py:603` defaults `APP_ENV` to `dev`. S15: 0 catalog entries for `/api/aux/narrative`, `/internal/healthz`, `/internal/readyz`, `/ops/probe/env`; `/reader` present. S18: `engine/http/compat_handler.py:125` returns `invalid_json` for a GET with a body, and `docs/ADAPTER_009.md:174` says `body_not_allowed`. S14: CLI/API/Vendor Ref §7.1.11 marks the override a held Required-Now gap; HDE Users Guide line 979 says the flag is absent | Repository read |

## 6. Canon conflict register — Thoth dispositions

Fields follow the carried `CANON_CONFLICT_REGISTER` contract. These dispositions apply to the interim treatments and drainage routing only; no canon is changed, and drainage remains the Product Owner's. The revised Specification carries them, and the next CF-C-30 review confirms them against v1.1.

| ID | Status | Disposition and rationale | Reviewer's exact change |
| :- | :- | :- | :- |
| CR-1 | `APPROVED_AS_CHANGED` | The interim treatment follows the governing source. HDE Governance owns approval and authority boundaries (Change Process Guide §0.1A routing; HDE Governance §9.1.1: "The active workflow MUST NOT create, update or synchronize their entries"), and §9.1.2 says to follow the governing PF position immediately. Glow QA Guide "Change-lane QA applicability" agrees. No PF30 entry; "Specification approval" in place of "CRD Plan approval" | Add the passages that carry the same conflict: Change Process Guide §0.1, §0.1A, the §1.0 heading, §1.0.4 and §1.0.6 (see list below); Plan Templates §2A (see list below); PF30.1 §2 "Implementation MUST NOT begin before CRD Plan approval". Drainage target and owner unchanged |
| CR-2 | `APPROVED_AS_CHANGED` | Interim treatment correct: the Specification records no planned units, per HDE Governance §9.1.1 and PF30.1 §4.1 (v0.9.1) | Add Plan Templates §2A "Alchemical phase separation" ("For every phase block, identify its purpose, included PR and Ops units …"), which carries the same conflict as the intake prompt |
| CR-3 | `APPROVED_AS_CHANGED` | Interim treatment correct: the CRD ID is the Product Owner-assigned ID in the class-selection record; HDE Governance §9.1.1 forbids a PF30 entry | Add HDE Schemas & Artifacts §8.17 "Change-container identity" ("the stable CRD ID recorded in PF30"). HDE Build Checklist Separation HDE-SEPA005 note verified at line 1170 |

Passages to add under CR-1:

- **Change Process Guide:**
  - §0.1: CRD lane "accountable to PF30".
  - §0.1A: CRD lane "PF30 accountability"; lifecycle item 14 "PF09 or PF30 record completion"; "HDE CRD Records controls PF30 CRD registration and result tracking".
  - §1.0 heading.
  - §1.0.4: "PF30 work mapping".
  - §1.0.6: "update the existing PF30 CRD record".
- **Plan Templates §2A:**
  - "PF30 accountability".
  - "a concise initial record in the active PF30 volume".
  - "route CRD results and closure posture to the existing PF30 CRD record".
  - "Update the existing CRD record".

- **Reviewer:** Thoth, CF-C-30, session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum.
- **Reviewed artifact:** `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md`, v1.0.
- **Decision time:** 2026-10-12T19:24:01Z.
- **Unresolved risk (all three):** until the owner drains them, readers of these passages meet contradictory text. HDE Governance §9.1.2 resolves each instance toward HDE Governance.

## 7. Next state and routing

- **Specification v1.0:** `SPECIFICATION_PENDING`, `ASK OK?`. It is not approved and is not edited by this review.
- **Next:** CF-C-40 — Revise CRD Specification — 100926.1, `PREAPPROVAL_REVISION`, Isis. Isis produces a complete successor `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md` (pending) with an item-by-item application record for R1–R4, then returns it to CF-C-30 with Thoth as the same reviewer.
- **PF10 addendum:** none.

## 8. TypeSafe reading for the receiving session (CF-C-40)

Action sent (v6): "Revise a 28 KB CRD Specification that has already been reviewed once, producing a complete successor version in response to an independent reviewer's denial that carries four bounded required redlines (one exclusion that conflicts with a mandatory production Live QA rule, one unrouted QA evidence-index compatibility dependency, one requirement whose scope and acceptance intent disagree, and one misstated release-member constraint) plus non-gating notes. No code is written and no live run occurs; the same independent reviewer reviews the revision again before any planning."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.19 (confidence 0.79); rung probabilities low 0.00, medium 0.07, high 0.68, extra high 0.25, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.97 (confidence 0.94). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.07, Opus 5.5 at high 0.66, Opus 5.5 at extra high 0.24, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: none.
- **Detail:** v6 sent 2026-10-12T19:23:10Z; HTTP 200 in 0.77 s; 4213 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- **Nathan's pick for CF-C-40:** not stated.
- **Nathan's pick for this CF-C-30 session:** not stated (reading recorded in the Specification v1.0, "TypeSafe reading for the receiving session (CF-C-30)").

**Surface advice:** run CF-C-40 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. It reads the Specification v1.0, this review and `docs/pfcanon/` on `main`. It writes only the successor Specification and its application record under `docs/ephemeral/`. R2 and R4 cite repository files the session should re-read on `main` before restating them.

## Canon relied on

Read from `docs/pfcanon/` on `main` at 9f710bb. Each entry gives the PF title and version, the sections read, and the decision topics the sections govern.

**PF04-Canon-HDE-Governance v2.8.7.** Read: the line-196 routing paragraph; §9.1, including Ops tasks and "Epic and CRD change lanes"; §9.1.1 in full, including the role table and "Historical drainage"; §9.1.2 in full; §9.7.3. Governs:

- review authority and mode (Thoth reviews; denial returns redlines to Isis);
- scope-level Specification content;
- the IA non-expansion rule underpinning R1–R4;
- conflict precedence for CR-1 to CR-3;
- ADR ownership.

**PF06-Canon-Change-Process-Guide v2.5.4.** Read: §0.1 and §0.1A in full; §0.5.1, "Plan path provenance" paragraph; §1.0 to §1.0.6 in full; §1.1.5 and §1.1.5A in full. Governs:

- format authority (N1);
- lane rigor and the downstream process (R1);
- the production-affecting Live QA requirement (R1);
- phase separation;
- the ADR requirement;
- the CR-1 passages.

**PF27-Canon-Plan-Templates v2.0.5.** Read: "Artifact execution boundary"; "Canon precedence for template use"; §2A in full; "Source-bound review authority and exact-fix limits"; "Materiality-based blocker discipline". Governs:

- the compatibility-dependency duty (R2);
- the CR-1 and CR-2 passages;
- the reviewer's limits;
- the materiality test applied to every finding, which separates R1–R4 (gating) from N1–N6 (non-gating).

**PF30.1-Canon-HDE-CRD-Records v0.9.1.** Read: §0 to §8 in full, including the HDE-CRD-0001 record. Governs the record format, status vocabularies, phase-block tracking, the HDE-CRD-0001 precedent, and the PF30.1 §2 passage under CR-1.

**PF19-Canon-Glow-QA-Guide v3.0.6.** Read: "Change-lane QA applicability (normative)" (lines 18–30); §3.5.5 from "Codespaces MAY temporarily act as a vendor client" through "Production-affecting Live QA minimum" (lines 1352–1370). Governs R1, CRD QA rigor and the QA root.

**PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6.** Read: §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)" (lines 583–640); §8.17 "Change-container identity" (lines 5266–5280). Governs R2, CD-1 and CR-3.

**PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3.** Read: §7.1.11 and §7.1.11a to §7.1.11f in full. Governs S14's surface (R1 and N5) and its consistency with the S10 environment rule.

**PF21-Reference-7 Phases of Alchemical Engineering.** Read: §4 to §7. Governs the phase-block assignments (no finding).

**PF10-HDE-Build-Notes v13.5.2.** Read in full. Addendum 2.1 governs only the TypeSafe reading (§8). PF10 is silent on this CRD's subject matter, so permanent canon governs (PF10 "Silence rule").

**Other passages.** Read: PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.7, the HDE-SEPA005 note (line 1170), for CR-3. PF29-Canon-HDE-Users-Guide v1.0.2, the `--allow-prod-vendor` limitation (line 979), for S14.

**Not read; no decision here rests on them:**

- PF20-Reference-HDE-Phased-Epics §2.26.7 (located at line 11398);
- `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`;
- `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md`.

The kickoff carries their content as source-stated [S].

**In-flight documents read in full:**

- `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md` (reviewed artifact);
- `docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md`.

**Prompts read:**

- CF-C-30 — Review and Approve CRD Specification — 100926.1;
- CF-C-40 — Revise CRD Specification — 100926.1;
- PR-30 — PR Implementation Proceed — 100926.1 (RD-1 basis; carried register contract).

**Operative documentation:** `AGENTS.md` (release identity; sole Index/Mirror writer; direct-only DB surface).

## 9. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / CF-C-30 / initial review 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md`, v1.0 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | CF-C-30 — Review and Approve CRD Specification — 100926.1, https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8, read 2026-10-12 |
| role/stage | Thoth / CF-C-30 initial Specification review |
| capture time | 2026-10-12T19:24:01Z |
| execution identity | https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| repository persistence | Pending: no installed `GCFPE_PROMPT_PROVENANCE.md` writer was checked by this session; recorded here only |
