---
artifact_type: CRD_SPECIFICATION
artifact_version: "1.1"
logical_id: HDE-CRD-0002-SPECIFICATION
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: SPECIFICATION_PENDING
approval_sentinel: "ASK OK?"
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
reviewer: Thoth, CF-C-30 — Review and Approve CRD Specification — 100926.1 (same reviewer as v1.0; session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
prompt: CF-C-40 — Revise CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a)
revision_mode: PREAPPROVAL_REVISION
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-12T19:31:15Z
repository_head_read: origin/main 6af9c765
supersedes: docs/ephemeral/HDE-CRD-0002-specification-v1.0.md (v1.0, SPECIFICATION_PENDING, denied)
review_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.0.md (INITIAL_DENY, R1–R4)
application_record_ref: docs/ephemeral/HDE-CRD-0002-specification-v1.1-application-record.md
format_owner: PF30.1-Canon-HDE-CRD-Records v0.9.1 — §4.1 Initial registration (Minimum CRD record contract) and §7 CRD record template
kickoff_ref: docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md
class_selection_ref: docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md
source_ref: docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md
---

# HDE-CRD-0002 — Specification

This is the pending CRD Specification for HDE-CRD-0002, version 1.1. It is the complete successor to v1.0, which Thoth denied at CF-C-30 (review v1.0, INITIAL_DENY). It applies required redlines R1 to R4 and non-gating notes N1 to N5; the application record lists each change. It sets intent, scope, constraints and outcomes at scope level. It does not prescribe PR or Ops work units, file edits or commands (HDE Governance §9.1.1); the change-wide Implementation Plan does that after this Specification is approved. It approves nothing and authorizes no implementation, QA, Ops, canon change, acceptance or closure.

## Format and register posture

- **Format.** Change Process Guide §0.1A ("Specification format authority") and Plan Templates §2A ("PF30-owned Specification format and record contract") name `PF30.1-Canon-HDE-CRD-Records`, **Minimum CRD record contract** and **CRD record template**, as the CRD Specification format. This record uses §4.1 and §7 of PF30.1 v0.9.1, the Product Owner's bounded correction of 2026-10-12 (amthorn78/glow-hdengine-v2#614), which removes planned work units from the Specification.
- **Content bound.** HDE Governance §9.1.1: a Specification stays at scope and outcome level and MUST NOT prescribe planned PR or Ops work units. The phase blocks below give purpose, scope, dependencies and completion boundaries only.
- **No PF30 entry.** HDE Governance §9.1.1 and Glow QA Guide "Change-lane QA applicability" treat PF30 as historical: no PF30 entry is created, updated or required. This record uses PF30.1's format and status vocabulary only. Change Process Guide §1.0.3 still requires a PF30 record before implementation; that conflict is CR-1 below.
- **"CRD Plan approval".** HDE Governance §9.1.1 retires the CRD Plan. The PF30.1 template block "CRD Plan approval" is recorded here as **Specification approval**, as the HDE-CRD-0001 record did (CR-1).

## `HDE-CRD-0002` — `Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer`

### Record control

- **CRD ID:** `HDE-CRD-0002`
- **Title:** Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer
- **CRD status:** `Registered` — the PF30.1 §3.3 value for an assigned ID whose approval is not yet recorded; no PF30 entry exists (Format and register posture)
- **Creation date:** `2026-10-12`
- **Last material update:** `None` — v1.1 is a pre-approval revision, not a material update of an approved record (see Pre-approval revision history)

### CRD continuity & volume continuation

- **Predecessor CRD:** `Not applicable`
- **Successor CRD:** `Not applicable`
- **Originating PF30.x volume:** `Not applicable — no PF30 entry (HDE Governance §9.1.1)`
- **Continuation PF30.x volume:** `Not applicable`
- **Reciprocal continuation reference:** `Not applicable`

### Intake, analysis & bounded scope

- **Observed need or requested change:** HDE-EPIC040 closed with defects and gaps that no work unit owns: packaging, HTTP 404 handling, CI coverage, attestation, CLI and dev surfaces, evidence tooling, an unimplemented canon CLI contract, an incomplete endpoint catalog and stale operator documents (item 5). Code merged by four HDE-EPIC040 PRs never had a code security review (item 6). Every PR session repeats the same pre-push checks by hand (item 7). The only governed close-pack writer cannot write the close report canon requires, so no change can pass the ordinary Close Gate (item 8). The canonical evidence-index updater admits only HDE-CRD-0001's QA root, so this CRD's QA evidence cannot be published until it is extended (CD-3).
- **Why warranted:** One defect is live on the public production surface (S02). One is a fail-open security default (S10). 129 test files ran in no CI lane at HDE-EPIC040 PR05 (O-11; not recounted, U-1), so their regressions are invisible to CI (S03). The next release attestation fails on Debian (S06). A Required-Now canon contract has no implementation (S14). Public routes merged without code security review (S19). HDE-EPIC040 needed exceptional closure because of item 8 (S21). HDE Schemas & Artifacts §8.17 requires the updater's CRD admission before this CRD enters QA (S22).
- **Affected surfaces:** `code: packaging metadata, the production HTTP adapter and its dev Reader route, the CI lane classifier and CI workflow, uncovered tests, the attestation builder and its closure probe, CLI help and Aux preview, the hdctl bg:resolve vendor path, evidence tests and Mirror provenance labels, the dev Reader harness, the close-pack writer and its schema, the canonical evidence-index updater's CRD admission; data: none; operations: release attestation, the production vendor override's audit trail, and any Product Owner-authorized deployment or Ops task that places the QA candidate for Live QA; documentation: docs/ADAPTER_009.md, ARCHITECTURE.md, .env.example, VERIFY.sh, docs/acceptance/reader_a7_crib.md, and AGENTS.md as affected; governance: none beyond S21's ADR; canon: S21 changes close-pack canon (ADR required); S14 implements existing canon`
- **Known constraints and risks:** see **Constraints** below.
- **Available intake evidence:** `docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md` (KICKOFF_READY); `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md` (CLASS_SELECTED); `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`; `docs/ephemeral/HDE-CRD-0002-specification-review-v1.0.md` (R2, for S22); and the records those name per item: `docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md` (RA-04, RA-05, RA-08, RA-12, RA-14), `docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md` (RA-09), `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` (O-11, O-22), `docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` §4, `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` (B-1, B-2), `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` (CC-1, CC-2), and HDE Phased Epics §2.26.7.
- **Lead Developer finding:** `valid: yes — each requirement below is an observed defect or gap with a cited source; not already satisfied: yes — no file outside docs/ changed on main between d86b8850 and 6af9c765 except AGENTS.md (2aed56f1 to 6af9c765 re-checked for this revision), and the Lead Developer re-checked DD-11, O-P07-04, .env.example, the endpoint catalog, the classifier, the CI paths-ignore list, the release-member list and the updater's CRD admission at or after d86b8850; CRD lane: yes for S01 to S22 — observed-change work originating outside PF09 planned work (HDE Governance §9.1); S22 is the compatibility work HDE Schemas & Artifacts §8.17 assigns to "the authorized change lane" before the first affected CRD enters QA; item 6(a) is not CRD lane and is routed (RD-1)`
- **Bounded scope:** S01 to S22 below. Each is a scope statement with its acceptance intent; the Implementation Plan decides how.
- **Exclusions:** see **Exclusions** below.
- **Expected outcome:** every acceptance intent S01 to S22 holds on `main`, verified by independent QA that includes the production-affecting Live QA minimum (Canon, QA & Build Notes posture); the ordinary Close Gate is available to HDE-CRD-0002 and later changes.
- **Current blockers and compatibility dependencies:** no blocker to Specification review. Compatibility dependencies CD-1 to CD-3 below; CD-3 is delivered by S22 before HDE-CRD-0002 enters QA. Routed dependency RD-1 below.

#### Requirements

Source key: the item and part in the briefs and kickoff, and the original observation ID.

Paths named below are existing files cited as observed defect locations. They come from the intake audit records named above and the Lead Developer's read-only checks at `2aed56f1` and `6af9c765`. They are evidence, not required implementation paths (Change Process Guide §0.5.1, "Plan path provenance"); the Implementation Audit establishes implementation loci.

| ID | Source | Scope | Acceptance intent (what must be true) |
| :---- | :---- | :---- | :---- |
| S01 | 5(a), O-12 | Package every release member with the distribution | A regular wheel install admits the complete release outside a source checkout |
| S02 | 5(b), O-P06a-22 | Unknown non-compat paths on the production app return the governed not-found envelope | Every 404 from the production app is the governed `ERR_NOT_FOUND` envelope with `no-store`, never Flask HTML |
| S03 | 5(c-1), O-11, RA-08, O-P06a-03 | Bring every test file into a CI lane or retire it with a recorded reason | No test file runs in no CI lane; each retirement has a recorded reason; recorded failures and collection errors are fixed or retired with their files |
| S04 | 5(c-2), O-22 | Unregistered `tools/qa/` sources get the same fail-closed treatment as `tools/bodygraph/` | An unregistered `tools/qa/` source, `.sh` and `.sql` included, cannot pass classification without an owner test |
| S05 | 5(c-3), RA-12 | Align the CI workflow's documentation skip list with the classifier's documentation prefixes | A PR touching only classifier documentation prefixes starts no CI run |
| S06 | 5(d), O-10 | Make the attestation builder's wheel stage work under Debian-patched setuptools | The release attestation builds under Debian-patched setuptools |
| S07 | 5(e), O-P07-01 | Correct the showcompat help summary | `hdctl --help` describes showcompat's actual `magic10_compat_result.v1` output |
| S08 | 5(e), O-P07-02 | Apply `aux-preview --band` when the band comes from the pair file | The band flag takes effect for pair-file input |
| S09 | 5(e), O-P07-03 | Repair or retire the dev Reader harness and the references to it | The harness imports and runs, or it is retired and `VERIFY.sh` and `docs/acceptance/reader_a7_crib.md` no longer reference it |
| S10 | 5(e), O-P07-04 | Gate dev `GET /reader` on an explicit environment | The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses |
| S11 | 5(e), O-P06a-23 | Make the engine-core evidence currency test check release identity | The test fails when `release_id` drifts |
| S12 | 5(e), O-P06b-17 | Correct provenance labels on current-release captures in the Machine Mirror | Current-release captures carry current-release labels |
| S13 | 5(e), O-OPS01-01 | Remove the closure admission probe's dependence on the ambient installed package | The probe's result depends only on the isolated closure's own sources |
| S14 | 5(f), DD-04, QA50-B01 | Implement the production vendor override as CLI/API/Vendor Ref §7.1.11a to §7.1.11f state it | `--allow-prod-vendor` behaves as §7.1.11 specifies, including environment classification, rails, evaluation order, error carrier, authorized initiator and audit; closed rails still refuse first, and public Reader or Aux traffic never reaches the vendor |
| S15 | 5(g), RA-14 | Reconcile the endpoint catalog with the routes the service registers | Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner |
| S16 | 5(h) | Add `GEO_API_KEY` to the environment template | `.env.example` has a `GEO_API_KEY` entry |
| S17 | 5(i), O-P07-05 | Correct the readiness and port statements in `docs/ADAPTER_009.md` | The readiness rules describe what `/internal/readyz` does, and the port statements are current |
| S18 | 5(i), DD-11, O-P07-06 | Correct `docs/ADAPTER_009.md`'s GET-with-body code and `ARCHITECTURE.md`'s stale statements | The documents say `invalid_json` for a compat GET with a body (observed by the Lead Developer in `engine/http/compat_handler.py` at `2aed56f1`) and state the current emitter return type and route mounts |
| S19 | 6(b), RA-09 | One code security review of what #467, #492, #501 and #508 merged, read on `main` | The review is recorded; each confirmed finding is fixed within this CRD or routed to an owner with a reason |
| S20 | 7 | One read-only pre-push and pre-plan check with its own test | One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository |
| S21 | 8, CC-1, CC-2 | A governed, feedback-free close-pack writer for Epic and CRD identities, and an admitted home for close-workflow run evidence | The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has a home, inside an existing evidence family or in one S21's ADR admits, that does not reopen an approved QA manifest; the accompanying ADR is approved |
| S22 | CD-3; review v1.0 R2; HDE Schemas & Artifacts §8.17 "Change-container identity" | Extend the canonical evidence-index updater's CRD admission to HDE-CRD-0002's QA root | Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate |

#### Exclusions

- No Reader contract or payload change, and no new public route.
- No release re-cut beyond what the in-scope requirements require.
- No new evidence family, acceptance token or token matrix, except a home for close-workflow run evidence that S21's ADR admits (S21).
- No canon change beyond S21's ADR-covered close-pack change. S14 implements existing canon and changes none.
- As implementation work: no deployment, no production configuration change, and no live vendor call made by an implementation work unit. This exclusion does not exclude, for this change, (a) the bounded open-rails Live QA that Glow QA Guide §3.5.5 and Change Process Guide §1.1.5A require, including the synthetic-data live vendor call, or (b) a Product Owner-authorized deployment or Ops task needed to place the QA candidate in the deployed or live target those steps exercise. Production `APP_ENV` is already `prod`, as reported by the Product Owner on 2026-10-12; S10 needs no production configuration change.
- No change to the code-review tooling (item 6).
- No retroactive close pack for HDE-EPIC040.
- No PF09 mapping of this work (Plan Templates §2A).
- No SessionStart hook (item 7).
- Item 6(a) is not delivered by this CRD (RD-1).
- Not reopened: O-P07-07 (covered by S09), O-P07-08 (moot), O-P07-09 (resolved), RA-11, RA-15, RA-16, final-check atomicity, O-OPS01-02, CC-3 to CC-6, and live Gate readiness and live Reader success (Build Checklist Coagulation HDE-COAG003.8 and HDE-COAG003.9). Reasons are in the briefs v1.2, "Reviewed and left out".

#### Constraints

- **Release members.** `catalog/manifest.json` lists 45 release members. The observed loci of S07, S08 and S14 (`engine/cli/main.py`: help text line 79, `aux-preview --band` line 131, `bg:resolve` parser line 138; and `engine/bodygraph/resolver.py`) and of S10 (`adapter/http_reader.py`, `APP_ENV` gate line 603) are release members. Those of S01 (`pyproject.toml`) and S02 (`adapter/factory.py`) are not. Any requirement whose implementation changes a release member forces a manifest re-cut and new admission pins; the Implementation Audit establishes the actual set. The change converges on one coherent re-cut after the member-changing work lands.
- **Uncovered tests.** S03 may expose real defects that enlarge the work. Running the uncovered files in the repository tree can rewrite tracked evidence (O-11), so any sweep runs in a throwaway copy.
- **Dev route.** S10 must not break dev, test or local use of `/reader`.
- **Vendor override.** S14 keeps generic SAFE rails first: the override never opens a closed rail and never lets public Reader or Aux traffic call the vendor (CLI/API/Vendor Ref §7.1.11).
- **Override initiator.** Any live invocation of `--allow-prod-vendor`, in QA or elsewhere, is initiated only by an authenticated human Product Owner or a human operations executor the Product Owner explicitly delegates in the referenced approved work item; an AI agent, CI job, application request or unauthenticated shell cannot self-authorize (CLI/API/Vendor Ref §7.1.11e).
- **Live QA.** Live QA steps are bounded, Product Owner-authorized, synthetic-data-only, secret-safe and subject to request limits and stop checks; they authorize no load, stress or volume testing (Glow QA Guide §3.5.5; Change Process Guide §1.1.5A).
- **QA evidence admission.** S22 completes before HDE-CRD-0002 enters QA, and preserves existing Epic and HDE-CRD-0001 inputs (HDE Schemas & Artifacts §8.17).
- **Governed artifacts.** The endpoint catalog mirror, Index, Mirror and path proofs are produced by their owning tools, never hand-edited.
- **Close-pack writer.** HDE-EPIC039 made the generic writer neutral on purpose; S21 reverses that choice and must weigh its rationale. S21 touches the release-sanity and close-validation lanes.
- **Security review.** S19 findings may enlarge the work; findings in code a later PR already changed are judged against `main`.
- **Duplication.** S20 duplicates CI logic and must track `ci.yml` changes.

#### Compatibility dependencies

| ID | Dependency | Source | Treatment |
| :---- | :---- | :---- | :---- |
| CD-1 | The governed close-pack schema accepts only Epic identities: its `epic_id` pattern is `^HDE-EPIC[0-9]{3}$` | Kickoff §4 item 8 [V]; HDE Schemas & Artifacts §1.2 "Change-container compatibility (normative)" requires every Epic-only close-pack schema, generator or validator to be updated through the authorized change lane before the first CRD close pack enters QA or closeout | Resolved by S21 |
| CD-2 | HDE Schemas & Artifacts §1.2 and §8.17 refer to "the stable CRD ID recorded in PF30", but no PF30 entry is created (HDE Governance §9.1.1) | HDE Schemas & Artifacts §1.2 and §8.17 "Change-container identity"; HDE Governance §9.1.1 | Interim: the CRD ID is the Product Owner-assigned ID in the class-selection record. Recorded as CR-3 |
| CD-3 | The canonical evidence-index updater admits only HDE-CRD-0001. Verified on `main` at `6af9c765`: `tools/evidence/update_evidence_index.py` lines 47 to 51 set `CRD_QA_ID = "HDE-CRD-0001"`, `CRD_QA_ROOT_REL = "audit/qa/hde-crd-0001"` and `CRD_QA_KEY = "audit.qa.hde_crd_0001"`, under the comment "another CRD needs its own explicit admission". No other `.py` or `.sh` file under `tools/`, `ci/`, `engine/`, `adapter/` or `schemas/` names HDE-CRD-0001; `tools/qa/qa_harness.py` line 23 already accepts any `HDE-CRD-[0-9]{4,}` | HDE Schemas & Artifacts §8.17 "Change-container identity" ("Before the first affected CRD enters QA, every schema, validator, generator, manifest producer, or helper that accepts only epic identity or `EPIC_QA_ROOT` MUST be identified and updated through the authorized change lane"); Plan Templates §2A "Existing-template reuse and substitution"; `AGENTS.md` (sole Index/Mirror writer) | Resolved by S22, an in-scope requirement in the Distillation block, completing before HDE-CRD-0002 enters QA |

The QA root itself is canon-defined for CRDs: `audit/qa/<crd-id>/`, in lower case (Glow QA Guide, "Change-lane QA applicability (normative)"; HDE Schemas & Artifacts §8.17). It is not a compatibility dependency.

#### Routed dependency

| ID | Item | Finding | Owner and route |
| :---- | :---- | :---- | :---- |
| RD-1 | 6(a): open code PRs only after the implementation is pushed | Not CRD lane: it is a prompt change with no development target. The selected prompt release GCFPE-20261009.1 already addresses its main case: PR-30 — PR Implementation Proceed — 100926.1 publishes "only after a coherent locally tested checkpoint", so a plan-only code PR is no longer the PR-30 path. What remains is security-review coverage of pushes after the first, which is review-tooling and process work | GCFPE-MGMT-10 and the Product Owner. Not a closure condition for HDE-CRD-0002 |

### Specification approval

Recorded in place of the PF30.1 template's "CRD Plan approval" block (Format and register posture).

- **Specification reference:** `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md`
- **Approval status:** `Pending` — v1.0 was denied (review v1.0, INITIAL_DENY, 2026-10-12T19:24:01Z)
- **Decision date:** `Pending`
- **Approver:** `Pending` — Thoth, through CF-C-30
- **Decision source:** `Pending`
- **Claim boundary:** approval would establish the planned baseline only; it does not establish implementation, QA, acceptance or closure.

**Implementation Plan approval:** `Pending` — the change-wide Implementation Plan follows Specification approval through the Implementation Audit and Plan lane; Isis reviews it.

### Phase blocks

Alchemical phases follow 7 Phases of Alchemical Engineering and the phase scopes in the HDE Build Checklist volumes. Each PR or Ops unit the Implementation Plan identifies belongs to exactly one block. No block is required to precede another except where Dependencies says so.

| Phase | Purpose and bounded scope | Planned work units | Dependencies | Completion boundary | Current phase-block status | Actual implementation or Ops references |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `Conjunction` | Integrate public, dev and CLI surfaces correctly: S02, S07, S09, S10, S15, S18 | `Pending — identified by the change-wide Implementation Plan` | Coordinates with the release re-cut where a requirement changes a release member (S07, S10 by observed locus). Where S19 findings touch these surfaces, the Plan orders them coherently | S02, S07, S09, S10, S15 and S18 hold on `main` | `Planned` | `Not completed` |
| `Fermentation` | Provider gate and Aux preview (Build Checklist Fermentation scope: SAFE rails and provider gate; CLI Aux preview): S08, S14 | `Pending — identified by the change-wide Implementation Plan` | Coordinates with the release re-cut (S08, S14 by observed locus) | S08 and S14 hold on `main` | `Planned` | `Not completed` |
| `Distillation` | Quality, reliability, security and automation: S03, S04, S05, S06, S11, S12, S13, S19, S20, S21, S22 | `Pending — identified by the change-wide Implementation Plan` | S04 and S05 travel with S03. S20 follows S03 to S05. S21's ADR is approved before S21's changed behavior is relied on. S22 completes before HDE-CRD-0002 enters QA. S21 completes before HDE-CRD-0002 enters its ordinary Close Gate | S03 to S06, S11 to S13 and S19 to S22 hold on `main`, and S21's ADR is approved | `Planned` | `Not completed` |
| `Coagulation` | Durable packaging and environment discipline: S01, S16, S17 | `Pending — identified by the change-wide Implementation Plan` | S01 converges with the release re-cut | S01, S16 and S17 hold on `main` | `Planned` | `Not completed` |

Recommended ordering, for the Implementation Plan to confirm: S03 to S05 early, so later changes in every block are visible to CI; the release re-cut after all member-changing work lands; S22 before QA; S21 before HDE-CRD-0002's closeout.

### Canon, QA & Build Notes posture

- **Canon impact:** S21 changes close-pack canon: which writer produces the close report, and where close-workflow run evidence lives. S14 implements CLI/API/Vendor Ref §7.1.11 without changing it. S22 implements the compatibility duty of HDE Schemas & Artifacts §8.17 without changing it. No other requirement changes canon.
- **Affected canon and intended drainage targets:**
  - S21 (ADR-covered): Change Process Guide §3.5.2 (close pack); HDE Schemas & Artifacts §1.2 "Close-pack artifacts"; Glow QA Guide "Close-pack truthfulness and same-run execution" and "Close report requirements".
  - S14 (status drainage after implementation): the "Required-Now implementation gap (DD-04; held)" paragraph of CLI/API/Vendor Ref §7.1.11 and the `--allow-prod-vendor` bullet of HDE Users Guide §16 become stale once S14 lands; their owners update them.
  - Operative documentation, not canon: `AGENTS.md` passages on the close-pack generator and CI-exempt paths, as S05 and S21 affect them.
- **Accompanying ADR reference and status:** required for S21 (Change Process Guide §1.0.5); not yet drafted. ADRs are Product Owner-owned; agents may draft them (HDE Governance §9.7.3). It must be approved before S21's changed behavior is relied on.
- **QA requirement:** full independent QA under Glow QA Guide, at the rigor Epic work receives (Change Process Guide §0.1A and §1.0.6; Glow QA Guide "Change-lane QA applicability"). CI success is not QA acceptance. QA evidence lives under `audit/qa/hde-crd-0002/`, as Glow QA Guide defines the CRD QA root, and is published by the canonical updater once S22 holds.
- **Production-affecting Live QA minimum:** applies to this change (Glow QA Guide §3.5.5 "Production-affecting Live QA minimum"; Change Process Guide §1.1.5A). The QA Plan includes at least one bounded open-rails live QA step in the deployed or live target, and a live vendor call under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`) with synthetic data only. Affected-surface identification, as those sections assign to the Specification:

  | Class | Requirements | Surface and basis |
  | :---- | :---- | :---- |
  | Touches a surface used to produce a production feature PF canon describes as functional; the live vendor call under open rails is mandatory | S14; S02; S10; S07; S08; S15 where it removes a registered route | S14 changes vendor ingest through `hdctl bg:resolve --source vendor`, the HumanDesignAPI BodyGraph acquisition path (CLI/API/Vendor Ref §7.1.11). S02, S10 and a route removal under S15 change the production app (`adapter.factory`, per the `Procfile`) that serves Reader v1 and v2. S07 and S08 change `engine/cli/main.py`, the operator CLI surface that carries showcompat and Aux preview. Classified inclusively: the QA Plan needs one live vendor call whatever the count, so inclusion adds no step and leaves no surface for the Implementation Audit to reinterpret. The QA Plan designs the call and the live steps that exercise each requirement's changed behavior |
  | Production-affecting, outside the functional-feature scope; at least one bounded open-rails live step, or an explicit authorized exemption recorded in the QA Plan | S01 | Packaging of the deployed service. The repository does not show whether the deployed build installs the distribution; the Implementation Audit establishes it, and the QA Plan exempts S01 with a recorded basis only if it does not |
  | Inherits the class of the surface its fix changes | S19 | A confirmed finding fixed within this CRD takes the class above of the surface the fix changes; the Implementation Plan names those fixes |
  | Not production-affecting | S03, S04, S05, S06, S09, S11, S12, S13, S15 (catalog entries only), S16, S17, S18, S20, S21, S22 | CI lanes and classifier, release attestation and its closure probe, evidence tests and labels, the dev-only Reader harness, documentation and the environment template, read-only repository tooling, close-pack tooling and evidence-index tooling. None changes deployed runtime behavior, vendor ingest, public behavior, operator CLI behavior or secret binding |

  Any live `--allow-prod-vendor` step is initiated as the **Override initiator** constraint states (CLI/API/Vendor Ref §7.1.11e). Deployment mechanics and Ops task identities belong to the Implementation Plan and QA Plan.
- **Independent QA Plan reference:** `Pending` — authored in the QA lane after implementation.
- **Material HDE Build Notes references:** `None recorded`. The current HDE Build Notes hold one addendum, on TypeSafe readings, which does not reach this scope.

### Canon conflict register

Thoth dispositioned CR-1 to CR-3 as `APPROVED_AS_CHANGED` in review v1.0 §6 (Thoth, session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum, 2026-10-12T19:24:01Z). This version carries the reviewer's exact changes. The dispositions apply to interim treatments and drainage routing only; no canon is changed, and drainage remains the Product Owner's. The CF-C-30 re-review confirms them against v1.1.

**CR-1**
- **Classification:** CANON_RECONCILIATION
- **Conflicting sources:** Change Process Guide §0.1 (CRD lane "accountable to PF30"); §0.1A (CRD lane "PF30 accountability"; lifecycle item 14 "PF09 or PF30 record completion"; "HDE CRD Records controls PF30 CRD registration and result tracking"); the §1.0 heading; §1.0.3 ("MUST receive … a concise initial record in PF30 before implementation begins"); §1.0.4 ("PF30 work mapping"); §1.0.6 ("update the existing PF30 CRD record"). Plan Templates §2A ("PF30 accountability"; "a concise initial record in the active PF30 volume"; "route CRD results and closure posture to the existing PF30 CRD record"; "Update the existing CRD record"). PF30.1 "CRD Plan" wording (§1, §2 including "Implementation MUST NOT begin before CRD Plan approval", §3.2, §4.1, §7). Against: HDE Governance §9.1.1 (no CRD Plan; PF30 historical; "The active workflow MUST NOT create, update or synchronize their entries") and Glow QA Guide "Change-lane QA applicability" (PF30 registration not a prerequisite).
- **Statement:** canon disagrees on whether a CRD needs a PF30 record and on the "CRD Plan" artifact.
- **Affected requirements:** none of S01 to S22; affects this record's registration posture and its Specification approval block.
- **Interim treatment:** follow HDE Governance §9.1.1, the owner of approval and authority boundaries (HDE Governance §9.1.2: follow the governing PF position immediately): no PF30 entry; "CRD Plan approval" recorded as Specification approval.
- **Alternatives considered:** create a PF30 entry under Change Process Guide §1.0.3 — rejected, HDE Governance §9.1.1 forbids it.
- **Recommended disposition and drainage target:** the Change Process Guide owner aligns §0.1, §0.1A, §1.0, §1.0.3, §1.0.4 and §1.0.6; the Plan Templates owner aligns §2A; the PF30 owner aligns the CRD Plan wording. Owner: Product Owner.
- **Unresolved risk:** until the owner drains them, readers of these passages meet contradictory text; HDE Governance §9.1.2 resolves each instance toward HDE Governance.
- **Status:** `APPROVED_AS_CHANGED` (review v1.0 §6); confirmation against v1.1 pending.

**CR-2**
- **Classification:** CANON_RECONCILIATION
- **Conflicting sources:** Plan Templates §2A intake prompt "Planned PR and Ops units" and §2A "Alchemical phase separation" ("For every phase block, identify its purpose, included PR and Ops units …"), against HDE Governance §9.1.1.
- **Statement:** both passages ask for planned units a Specification must not prescribe. The PF30.1 half of this conflict was corrected by the Product Owner on 2026-10-12 (v0.9.1, #614).
- **Affected requirements:** none of S01 to S22; affects the phase blocks' "Planned work units" column.
- **Interim treatment:** the Specification records no planned units (HDE Governance §9.1.1; PF30.1 §4.1, v0.9.1).
- **Alternatives considered:** list planned units per Plan Templates §2A — rejected, HDE Governance §9.1.1 forbids it.
- **Recommended disposition and drainage target:** the Plan Templates owner removes or rewords both passages. Owner: Product Owner.
- **Unresolved risk:** as CR-1.
- **Status:** `APPROVED_AS_CHANGED` (review v1.0 §6); confirmation against v1.1 pending.

**CR-3**
- **Classification:** CANON_RECONCILIATION
- **Conflicting sources:** Build Checklist Separation HDE-SEPA005 task notes ("that CRD's PF30 record, once entered, owns them", line 1170, introduced by the Lead Developer's 2026-10-11 PF09 redline); HDE Schemas & Artifacts §1.2 ("the stable CRD ID recorded in PF30"); HDE Schemas & Artifacts §8.17 "Change-container identity" ("the stable CRD ID recorded in PF30"). Against: HDE Governance §9.1.1 (no PF30 entries).
- **Statement:** three passages point to a PF30 record that will not exist.
- **Affected requirements:** S21 (CRD identity in the close pack; CD-1, CD-2) and S22 (CRD QA-root identity; CD-3).
- **Interim treatment:** this Specification is HDE-CRD-0002's governing record; the CRD ID is the Product Owner-assigned ID in the class-selection record.
- **Alternatives considered:** wait for a PF30 record — not possible under HDE Governance §9.1.1.
- **Recommended disposition and drainage target:** the PF09 owner rewords the HDE-SEPA005 note to name this Specification; the HDE Schemas & Artifacts owner rewords §1.2 and §8.17. Owner: Product Owner.
- **Unresolved risk:** as CR-1.
- **Status:** `APPROVED_AS_CHANGED` (review v1.0 §6); confirmation against v1.1 pending.

### Material-change history

`None recorded`

### Exact-source execution & decision lineage

- **Specification decisions:** v1.0 denied, review v1.0 (INITIAL_DENY, 2026-10-12T19:24:01Z, amthorn78/glow-hdengine-v2#616); v1.1 pending
- **Implementation PR, commit, merge, and SHA references:** `Not completed`
- **Ops task and completion references:** `Not completed` — no Ops work is identified at Specification level; the Implementation Plan and QA Plan determine whether any is needed, including any Product Owner-authorized deployment that places the QA candidate
- **QA execution reference:** `Not executed`
- **Remediation and QA re-execution references:** `Not completed`
- **Final QA verdict and exact candidate:** `Pending`
- **Acceptance decision:** `Pending`
- **Closure decision:** `Pending`

### Closure result

- **Actual outcome:** `Pending`
- **Approved deviations:** `None`
- **Superseded or rejected scope:** `None`
- **Deferred or residual work:** RD-1, routed to GCFPE-MGMT-10
- **ADR status:** S21 ADR not yet drafted
- **Canon-drain status:** not applicable until implementation; targets are listed under Canon, QA & Build Notes posture and in CR-1 to CR-3

## Pre-approval revision history

| Version | Prompt and mode | Basis | Change |
| :---- | :---- | :---- | :---- |
| 1.0 | CF-C-20 | Kickoff v1.0 | Initial pending Specification (#615) |
| 1.1 | CF-C-40, PREAPPROVAL_REVISION | Review v1.0 R1 to R4, N1 to N5, CR-1 to CR-3 dispositions | Applies every required redline and N1 to N5; adds S22; carries the reviewer's CR changes. Item by item: `docs/ephemeral/HDE-CRD-0002-specification-v1.1-application-record.md` |

## Kickoff open points resolved

| Point | Decision |
| :---- | :---- |
| U-1 Current count of test files in no CI lane | Not recounted here; the warrant cites the PR05 count of 129. S03 covers every such file whatever the count; the Implementation Audit establishes the current set on `main` |
| U-2 Production `APP_ENV=prod` is a report | Recorded as the Product Owner's report. S10's scope does not depend on it |
| U-3 Item 6(a) lane | Routed to GCFPE-MGMT-10 (RD-1) |
| U-4 Item 8 and CRD identities | In scope: S21 covers Epic and CRD identities (CD-1; HDE Schemas & Artifacts §1.2), and HDE-CRD-0002's own ordinary closure needs it |
| U-5 Phase structure | Four blocks; item 5(c) sits in Distillation and needs no block of its own |
| U-6 DD-11 code side | Verified by the Lead Developer at `2aed56f1`: a compat GET with a body returns `invalid_json` |
| U-7 Format | PF30.1 §4.1 and §7, v0.9.1, under Change Process Guide §0.1A and Plan Templates §2A, bounded by HDE Governance §9.1.1; conflicts CR-1 and CR-2 |

## TypeSafe reading for the receiving session (CF-C-30 re-review)

Action sent (v6): "Re-review, then approve or return with redlines, the second version of a 42 KB CRD Specification that the same reviewer denied once with four bounded required redlines (an exclusion that conflicted with a mandatory production Live QA rule, an unrouted QA evidence-index compatibility dependency, a requirement whose scope and acceptance intent disagreed, and a misstated release-member constraint), checking an item-by-item application record against the earlier review and confirming three canon-conflict dispositions. It is a read-only review against canon and a few repository files: no code and no live runs; implementation planning, a Plan review and independent QA follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.24 (confidence 0.79); rung probabilities low 0.00, medium 0.04, high 0.69, extra high 0.27, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.99 (confidence 0.98). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.04, Opus 5.5 at high 0.68, Opus 5.5 at extra high 0.27, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: none.
- **Detail:** v6 sent 2026-10-12T19:33:53Z; HTTP 200 in 0.65 s; 4238 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- **Superseded send:** an earlier send at 2026-10-12T19:31:15Z described the Specification as 31 KB; the artifact is 42 KB, so it was re-sent with the size corrected and only this reading is recorded.
- **Nathan's pick for CF-C-30:** not stated.
- **Nathan's pick for this CF-C-40 session:** not stated (reading recorded in review v1.0 §8).

**Surface advice:** run the CF-C-30 re-review as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the same Thoth review lineage. It reads this Specification, the application record, review v1.0 and `docs/pfcanon/` on `main`, and re-reads `tools/evidence/update_evidence_index.py`, `catalog/manifest.json` and `.env.example` on `main` for R2 to R4. It writes only its decision artifact under `docs/ephemeral/`. This Specification's PR should be merged to `main` first.

## Canon relied on

Read on `main` at `6af9c765` for this revision (sections re-read now are marked *); other entries were read for v1.0 at `2aed56f1` and are unchanged on `main`, since the only `docs/pfcanon/` change between the two heads is PF30.1 v0.9.1 (#614), which v1.0 read on its branch:
- PF06-Canon-Change-Process-Guide v2.5.4: §0.1A "Specification format authority" and lane rigor; §0.5.1 "Plan path provenance"; §0.6.9 Plans are pointers; §1.0.2 to §1.0.6; *§1.1.5A Production-affecting open-rails Live QA requirement, in full.
- PF27-Canon-Plan-Templates v2.0.5: "Artifact execution boundary"; §2A HDE-CRD-Specification Profile and PF30 Record Contract, all subsections, including "Existing-template reuse and substitution" and "Alchemical phase separation".
- PF30.1-Canon-HDE-CRD-Records v0.9.1: §1 to §7 in full, and the §8 HDE-CRD-0001 record as precedent.
- PF04-Canon-HDE-Governance v2.8.7: §9.1, change classes; §9.1.1 Change authority and exact-artifact lineage; §9.1.2; §9.7.3.
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability (normative)"; "QA evidence and work-product path grammar (normative)"; §4.3 Rules (evidence root); *§3.5.5 "Production-affecting Live QA minimum" (lines 1352 to 1372).
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)"; *§8.17 Live QA evidence layout, "Change-container identity (normative)".
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §7.1.11, §7.1.11a and §7.1.11b in full, and the §7.1.11c to §7.1.11f headings; *§7.1.11e Error carrier and authorized setter.
- PF29-Canon-HDE-Users-Guide v1.0.2: §16 Known limitations and nonclaims.
- PF20-Reference-HDE-Phased-Epics v1.9.6: §2.26.7.
- PF21-Reference-7 Phases of Alchemical Engineering: §4 to §7.
- PF09.1 to PF09.7 Build Checklist volumes: phase descriptions; PF09.3 HDE-SEPA005 note (CR-3).
- PF10-HDE-Build-Notes v13.5.2: read in full for v1.0; addendum 2.1 governs the TypeSafe reading above; nothing else applies.
- `AGENTS.md`: canon-first rule; canon read-only; release identity; sole Index/Mirror writer; dev routes gated to dev, test and local.

Repository files re-read on `main` at `6af9c765` for this revision: `tools/evidence/update_evidence_index.py` lines 40 to 60; `tools/qa/qa_harness.py` line 23; `.env.example`; `engine/providers/vendor_http_hdapi.py` lines 55 to 75; `catalog/manifest.json` member list; `Procfile`.

In-flight documents: review v1.0 (read in full), Specification v1.0 (read in full), and the kickoff, class-selection record and briefs v1.2 named in the front matter. Prompts read: CF-C-40 — Revise CRD Specification — 100926.1 (2026-10-12). Prompt release: GCFPE-20261009.1 / 100926.1.
