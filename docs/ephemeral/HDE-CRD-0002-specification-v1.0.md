---
artifact_type: CRD_SPECIFICATION
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: SPECIFICATION_PENDING
approval_sentinel: "ASK OK?"
author: Isis, Lead Developer (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
reviewer: Thoth, CF-C-30 — Review and Approve CRD Specification — 100926.1 (first review; no Thoth session yet bound to HDE-CRD-0002)
prompt: CF-C-20 — Create CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81a7a944f19bd9a2e3de)
created_at: 2026-10-12T19:05:58Z
repository_head_read: origin/main 2aed56f1
format_owner: PF30.1-Canon-HDE-CRD-Records v0.9.1 — §4.1 Initial registration (Minimum CRD record contract) and §7 CRD record template
kickoff_ref: docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md
class_selection_ref: docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md
source_ref: docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md
---

# HDE-CRD-0002 — Specification

This is the pending CRD Specification for HDE-CRD-0002. It sets intent, scope, constraints and outcomes at scope level. It does not prescribe PR or Ops work units, file edits or commands (HDE Governance §9.1.1); the change-wide Implementation Plan does that after this Specification is approved. It approves nothing and authorizes no implementation, QA, Ops, canon change, acceptance or closure.

## Format and register posture

- **Format.** Change Process Guide §0.1 ("Specification format authority") and Plan Templates §2A ("PF30-owned Specification format and record contract") name `PF30.1-Canon-HDE-CRD-Records`, **Minimum CRD record contract** and **CRD record template**, as the CRD Specification format. This record uses §4.1 and §7 of PF30.1 v0.9.1, the Product Owner's bounded correction of 2026-10-12 (amthorn78/glow-hdengine-v2#614), which removes planned work units from the Specification.
- **Content bound.** HDE Governance §9.1.1: a Specification stays at scope and outcome level and MUST NOT prescribe planned PR or Ops work units. The phase blocks below give purpose, scope, dependencies and completion boundaries only.
- **No PF30 entry.** HDE Governance §9.1.1 and Glow QA Guide "Change-lane QA applicability" treat PF30 as historical: no PF30 entry is created, updated or required. This record uses PF30.1's format and status vocabulary only. Change Process Guide §1.0.3 still requires a PF30 record before implementation; that conflict is CR-1 below.
- **"CRD Plan approval".** HDE Governance §9.1.1 retires the CRD Plan. The PF30.1 template block "CRD Plan approval" is recorded here as **Specification approval**, as the HDE-CRD-0001 record did (CR-1).

## `HDE-CRD-0002` — `Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer`

### Record control

- **CRD ID:** `HDE-CRD-0002`
- **Title:** Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer
- **CRD status:** `Registered` — the PF30.1 §3.3 value for an assigned ID whose approval is not yet recorded; no PF30 entry exists (Format and register posture)
- **Creation date:** `2026-10-12`
- **Last material update:** `None`

### CRD continuity & volume continuation

- **Predecessor CRD:** `Not applicable`
- **Successor CRD:** `Not applicable`
- **Originating PF30.x volume:** `Not applicable — no PF30 entry (HDE Governance §9.1.1)`
- **Continuation PF30.x volume:** `Not applicable`
- **Reciprocal continuation reference:** `Not applicable`

### Intake, analysis & bounded scope

- **Observed need or requested change:** HDE-EPIC040 closed with defects and gaps that no work unit owns: packaging, HTTP 404 handling, CI coverage, attestation, CLI and dev surfaces, evidence tooling, an unimplemented canon CLI contract, an incomplete endpoint catalog and stale operator documents (item 5). Code merged by four HDE-EPIC040 PRs never had a code security review (item 6). Every PR session repeats the same pre-push checks by hand (item 7). The only governed close-pack writer cannot write the close report canon requires, so no change can pass the ordinary Close Gate (item 8).
- **Why warranted:** One defect is live on the public production surface (S02). One is a fail-open security default (S10). Regressions in 129 test files are invisible to CI (S03). The next release attestation fails on Debian (S06). A Required-Now canon contract has no implementation (S14). Public routes merged without code security review (S19). HDE-EPIC040 needed exceptional closure because of item 8 (S21).
- **Affected surfaces:** `code: packaging metadata, the production HTTP adapter and its dev Reader route, the CI lane classifier and CI workflow, uncovered tests, the attestation builder and its closure probe, CLI help and Aux preview, the hdctl bg:resolve vendor path, evidence tests and Mirror provenance labels, the dev Reader harness, the close-pack writer and its schema; data: none; operations: release attestation, and the production vendor override's audit trail; documentation: docs/ADAPTER_009.md, ARCHITECTURE.md, .env.example, VERIFY.sh, docs/acceptance/reader_a7_crib.md, and AGENTS.md as affected; governance: none beyond S21's ADR; canon: S21 changes close-pack canon (ADR required); S14 implements existing canon`
- **Known constraints and risks:** see **Constraints** below.
- **Available intake evidence:** `docs/ephemeral/HDE-CRD-0002-specification-kickoff-v1.0.md` (KICKOFF_READY); `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md` (CLASS_SELECTED); `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`; and the records those name per item: `docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md` (RA-04, RA-05, RA-08, RA-12, RA-14), `docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md` (RA-09), `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` (O-11, O-22), `docs/ephemeral/HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` §4, `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` (B-1, B-2), `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` (CC-1, CC-2), and HDE Phased Epics §2.26.7.
- **Lead Developer finding:** `valid: yes — each requirement below is an observed defect or gap with a cited source; not already satisfied: yes — no file outside docs/ changed on main between d86b8850 and 2aed56f1 except AGENTS.md, and the Lead Developer re-checked DD-11, O-P07-04, .env.example, the endpoint catalog, the classifier and the CI paths-ignore list at or after d86b8850; CRD lane: yes for S01 to S21 — observed-change work originating outside PF09 planned work (HDE Governance §9.1); item 6(a) is not CRD lane and is routed (RD-1)`
- **Bounded scope:** S01 to S21 below. Each is a scope statement with its acceptance intent; the Implementation Plan decides how.
- **Exclusions:** see **Exclusions** below.
- **Expected outcome:** every acceptance intent S01 to S21 holds on `main`, verified by independent QA; the ordinary Close Gate is available to HDE-CRD-0002 and later changes.
- **Current blockers and compatibility dependencies:** no blocker to Specification review. Compatibility dependencies CD-1 to CD-3 below. Routed dependency RD-1 below.

#### Requirements

Source key: the item and part in the briefs and kickoff, and the original observation ID.

Paths named below are existing files cited as observed defect locations. They come from the intake audit records named above and the Lead Developer's read-only checks at `2aed56f1`. They are evidence, not required implementation paths (Change Process Guide §0.5.1, "Plan path provenance"); the Implementation Audit establishes implementation loci.

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
| S14 | 5(f), DD-04, QA50-B01 | Implement the production vendor override as CLI/API/Vendor Ref §7.1.11a to §7.1.11f state it | `--allow-prod-vendor` behaves as §7.1.11 specifies, including environment classification, rails, evaluation order, error carrier and audit; closed rails still refuse first, and public Reader or Aux traffic never reaches the vendor |
| S15 | 5(g), RA-14 | Reconcile the endpoint catalog with the routes the service registers | Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner |
| S16 | 5(h) | Add `GEO_API_KEY` to the environment template | `.env.example` names every environment key the service requires |
| S17 | 5(i), O-P07-05 | Correct the readiness and port statements in `docs/ADAPTER_009.md` | The readiness rules describe what `/internal/readyz` does, and the port statements are current |
| S18 | 5(i), DD-11, O-P07-06 | Correct `docs/ADAPTER_009.md`'s GET-with-body code and `ARCHITECTURE.md`'s stale statements | The documents say `invalid_json` for a compat GET with a body (observed by the Lead Developer in `engine/http/compat_handler.py` at `2aed56f1`) and state the current emitter return type and route mounts |
| S19 | 6(b), RA-09 | One code security review of what #467, #492, #501 and #508 merged, read on `main` | The review is recorded; each confirmed finding is fixed within this CRD or routed to an owner with a reason |
| S20 | 7 | One read-only pre-push and pre-plan check with its own test | One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository |
| S21 | 8, CC-1, CC-2 | A governed, feedback-free close-pack writer for Epic and CRD identities, and an admitted home for close-workflow run evidence | The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has an admitted home that does not reopen an approved QA manifest; the accompanying ADR is approved |

#### Exclusions

- No Reader contract or payload change, and no new public route.
- No release re-cut beyond what S01, S02, S07 or S14 requires.
- No new evidence family, acceptance token or token matrix.
- No canon change beyond S21's ADR-covered close-pack change. S14 implements existing canon and changes none.
- No deployment, production configuration change or live vendor call. Production `APP_ENV` is already `prod`, as reported by the Product Owner on 2026-10-12; S10 needs no production change.
- No change to the code-review tooling (item 6).
- No retroactive close pack for HDE-EPIC040.
- No PF09 mapping of this work (Plan Templates §2A).
- No SessionStart hook (item 7).
- Item 6(a) is not delivered by this CRD (RD-1).
- Not reopened: O-P07-07 (covered by S09), O-P07-08 (moot), O-P07-09 (resolved), RA-11, RA-15, RA-16, final-check atomicity, O-OPS01-02, CC-3 to CC-6, and live Gate readiness and live Reader success (Build Checklist Coagulation HDE-COAG003.8 and HDE-COAG003.9). Reasons are in the briefs v1.2, "Reviewed and left out".

#### Constraints

- **Release members.** S01, S02, S07 and possibly S14 change release members. Each forces a manifest re-cut and new admission pins; the change converges on one coherent re-cut after the member-changing work lands.
- **Uncovered tests.** S03 may expose real defects that enlarge the work. Running the uncovered files in the repository tree can rewrite tracked evidence (O-11), so any sweep runs in a throwaway copy.
- **Dev route.** S10 must not break dev, test or local use of `/reader`.
- **Vendor override.** S14 keeps generic SAFE rails first: the override never opens a closed rail and never lets public Reader or Aux traffic call the vendor (CLI/API/Vendor Ref §7.1.11).
- **Governed artifacts.** The endpoint catalog mirror, Index, Mirror and path proofs are produced by their owning tools, never hand-edited.
- **Close-pack writer.** HDE-EPIC039 made the generic writer neutral on purpose; S21 reverses that choice and must weigh its rationale. S21 touches the release-sanity and close-validation lanes.
- **Security review.** S19 findings may enlarge the work; findings in code a later PR already changed are judged against `main`.
- **Duplication.** S20 duplicates CI logic and must track `ci.yml` changes.

#### Compatibility dependencies

| ID | Dependency | Source | Treatment |
| :---- | :---- | :---- | :---- |
| CD-1 | The governed close-pack schema accepts only Epic identities: its `epic_id` pattern is `^HDE-EPIC[0-9]{3}$` | Kickoff §4 item 8 [V]; HDE Schemas & Artifacts §1.2 "Change-container compatibility (normative)" requires every Epic-only close-pack schema, generator or validator to be updated through the authorized change lane before the first CRD close pack enters QA or closeout | Resolved by S21 |
| CD-2 | HDE Schemas & Artifacts §1.2 refers to "the stable CRD ID recorded in PF30", but no PF30 entry is created (HDE Governance §9.1.1) | HDE Schemas & Artifacts §1.2; HDE Governance §9.1.1 | Interim: the CRD ID is the Product Owner-assigned ID in the class-selection record. Recorded as CR-3 |
| CD-3 | Whether the canonical evidence-index updater's per-change registration admits CRD QA-root artifacts | Not observed; the per-Epic registration pattern is recorded in `docs/ephemeral/HDE-EPIC040-lead-dev-close-gate-decisions-v1.0.md` §3 | The Implementation Audit establishes it before QA relies on it |

The QA root itself is canon-defined for CRDs: `audit/qa/<crd-id>/`, in lower case (Glow QA Guide, "Change-lane QA applicability (normative)"). It is not a compatibility dependency.

#### Routed dependency

| ID | Item | Finding | Owner and route |
| :---- | :---- | :---- | :---- |
| RD-1 | 6(a): open code PRs only after the implementation is pushed | Not CRD lane: it is a prompt change with no development target. The selected prompt release GCFPE-20261009.1 already addresses its main case: PR-30 — PR Implementation Proceed — 100926.1 publishes "only after a coherent locally tested checkpoint", so a plan-only code PR is no longer the PR-30 path. What remains is security-review coverage of pushes after the first, which is review-tooling and process work | GCFPE-MGMT-10 and the Product Owner. Not a closure condition for HDE-CRD-0002 |

### Specification approval

Recorded in place of the PF30.1 template's "CRD Plan approval" block (Format and register posture).

- **Specification reference:** `docs/ephemeral/HDE-CRD-0002-specification-v1.0.md`
- **Approval status:** `Pending`
- **Decision date:** `Pending`
- **Approver:** `Pending` — Thoth, through CF-C-30
- **Decision source:** `Pending`
- **Claim boundary:** approval would establish the planned baseline only; it does not establish implementation, QA, acceptance or closure.

**Implementation Plan approval:** `Pending` — the change-wide Implementation Plan follows Specification approval through the Implementation Audit and Plan lane; Isis reviews it.

### Phase blocks

Alchemical phases follow 7 Phases of Alchemical Engineering and the phase scopes in the HDE Build Checklist volumes. Each PR or Ops unit the Implementation Plan identifies belongs to exactly one block. No block is required to precede another except where Dependencies says so.

| Phase | Purpose and bounded scope | Planned work units | Dependencies | Completion boundary | Current phase-block status | Actual implementation or Ops references |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| `Conjunction` | Integrate public, dev and CLI surfaces correctly: S02, S07, S09, S10, S15, S18 | `Pending — identified by the change-wide Implementation Plan` | Coordinates with the release re-cut (S02, S07). Where S19 findings touch these surfaces, the Plan orders them coherently | S02, S07, S09, S10, S15 and S18 hold on `main` | `Planned` | `Not completed` |
| `Fermentation` | Provider gate and Aux preview (Build Checklist Fermentation scope: SAFE rails and provider gate; CLI Aux preview): S08, S14 | `Pending — identified by the change-wide Implementation Plan` | S14 coordinates with the release re-cut if it changes a release member | S08 and S14 hold on `main` | `Planned` | `Not completed` |
| `Distillation` | Quality, reliability, security and automation: S03, S04, S05, S06, S11, S12, S13, S19, S20, S21 | `Pending — identified by the change-wide Implementation Plan` | S04 and S05 travel with S03. S20 follows S03 to S05. S21's ADR is approved before S21's changed behavior is relied on. S21 completes before HDE-CRD-0002 enters its ordinary Close Gate | S03 to S06, S11 to S13 and S19 to S21 hold on `main`, and S21's ADR is approved | `Planned` | `Not completed` |
| `Coagulation` | Durable packaging and environment discipline: S01, S16, S17 | `Pending — identified by the change-wide Implementation Plan` | S01 converges with the release re-cut | S01, S16 and S17 hold on `main` | `Planned` | `Not completed` |

Recommended ordering, for the Implementation Plan to confirm: S03 to S05 early, so later changes in every block are visible to CI; the release re-cut after all member-changing work lands; S21 before HDE-CRD-0002's closeout.

### Canon, QA & Build Notes posture

- **Canon impact:** S21 changes close-pack canon: which writer produces the close report, and where close-workflow run evidence lives. S14 implements CLI/API/Vendor Ref §7.1.11 without changing it. No other requirement changes canon.
- **Affected canon and intended drainage targets:**
  - S21 (ADR-covered): Change Process Guide §3.5.2 (close pack); HDE Schemas & Artifacts §1.2 "Close-pack artifacts"; Glow QA Guide "Close-pack truthfulness and same-run execution" and "Close report requirements".
  - S14 (status drainage after implementation): the "Required-Now implementation gap (DD-04; held)" paragraph of CLI/API/Vendor Ref §7.1.11 and the `--allow-prod-vendor` bullet of HDE Users Guide §16 become stale once S14 lands; their owners update them.
  - Operative documentation, not canon: `AGENTS.md` passages on the close-pack generator and CI-exempt paths, as S05 and S21 affect them.
- **Accompanying ADR reference and status:** required for S21 (Change Process Guide §1.0.5); not yet drafted. ADRs are Product Owner-owned; agents may draft them (HDE Governance §9.7.3). It must be approved before S21's changed behavior is relied on.
- **QA requirement:** full independent QA under Glow QA Guide, at the rigor Epic work receives (Change Process Guide §1.0.6; Glow QA Guide "Change-lane QA applicability"). CI success is not QA acceptance. QA evidence lives under `audit/qa/hde-crd-0002/`, as Glow QA Guide defines the CRD QA root.
- **Independent QA Plan reference:** `Pending` — authored in the QA lane after implementation.
- **Material HDE Build Notes references:** `None recorded`. The current HDE Build Notes hold one addendum, on TypeSafe readings, which does not reach this scope.

### Canon conflict register

Entries are proposals for Thoth's disposition at CF-C-30. Review fields are not yet reviewed.

| ID | Classification | Conflicting sources | Statement | Interim treatment | Recommended disposition and drainage target | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| CR-1 | CANON_RECONCILIATION | Change Process Guide §1.0.3 ("MUST receive … a concise initial record in PF30 before implementation begins") and PF30.1 "CRD Plan" wording (§1, §2, §3.2, §4.1, §7), against HDE Governance §9.1.1 (no CRD Plan; PF30 historical; no PF30 entry at any stage) and Glow QA Guide "Change-lane QA applicability" (PF30 registration not a prerequisite) | Canon disagrees on whether a CRD needs a PF30 record and on the "CRD Plan" artifact | Follow HDE Governance §9.1.1, the owner of approval and authority boundaries: no PF30 entry; "CRD Plan approval" recorded as Specification approval | Change Process Guide owner aligns §1.0.3; the PF30 owner aligns the CRD Plan wording. Owner: Product Owner | PROPOSED; not yet reviewed |
| CR-2 | CANON_RECONCILIATION | Plan Templates §2A intake prompt "Planned PR and Ops units", against HDE Governance §9.1.1 | The intake prompt asks for planned units a Specification must not prescribe. The PF30.1 half of this conflict was corrected by the Product Owner on 2026-10-12 (v0.9.1, #614) | The Specification records no planned units | Plan Templates owner removes or rewords the prompt. Owner: Product Owner | PROPOSED; not yet reviewed |
| CR-3 | CANON_RECONCILIATION | Build Checklist Separation HDE-SEPA005 task notes ("that CRD's PF30 record, once entered, owns them", introduced by the Lead Developer's 2026-10-11 PF09 redline) and HDE Schemas & Artifacts §1.2 ("the stable CRD ID recorded in PF30"), against HDE Governance §9.1.1 (no PF30 entries) | Two passages point to a PF30 record that will not exist | This Specification is HDE-CRD-0002's governing record; the CRD ID is the one in the class-selection record | PF09 owner rewords the HDE-SEPA005 note to name this Specification; the HDE Schemas & Artifacts owner rewords §1.2. Owner: Product Owner | PROPOSED; not yet reviewed |

### Material-change history

`None recorded`

### Exact-source execution & decision lineage

- **Implementation PR, commit, merge, and SHA references:** `Not completed`
- **Ops task and completion references:** `Not completed` — no Ops work is identified at Specification level; the Implementation Plan determines whether any is needed
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
- **Canon-drain status:** not applicable until implementation; targets are listed under Canon, QA & Build Notes posture

## Kickoff open points resolved

| Point | Decision |
| :---- | :---- |
| U-1 Current count of test files in no CI lane | Not recounted here. S03 covers every such file whatever the count; the Implementation Audit establishes the current set on `main` |
| U-2 Production `APP_ENV=prod` is a report | Recorded as the Product Owner's report. S10's scope does not depend on it |
| U-3 Item 6(a) lane | Routed to GCFPE-MGMT-10 (RD-1) |
| U-4 Item 8 and CRD identities | In scope: S21 covers Epic and CRD identities (CD-1; HDE Schemas & Artifacts §1.2), and HDE-CRD-0002's own ordinary closure needs it |
| U-5 Phase structure | Four blocks; item 5(c) sits in Distillation and needs no block of its own |
| U-6 DD-11 code side | Verified by the Lead Developer at `2aed56f1`: a compat GET with a body returns `invalid_json` |
| U-7 Format | PF30.1 §4.1 and §7, v0.9.1, under Change Process Guide §0.1 and Plan Templates §2A, bounded by HDE Governance §9.1.1; conflicts CR-1 and CR-2 |

## TypeSafe reading for the receiving session (CF-C-30)

Action sent (v6): "Review, then approve or return with redlines, the first version of a new 28 KB CRD Specification covering 21 scope requirements across packaging, the HTTP adapter, CI coverage, CLI fixes, a canon vendor-override contract, a code security review and close-pack tooling, in four phase blocks, with one canon ADR requirement and three recorded canon conflicts to disposition. It is a read-only review against canon: no code and no live runs; implementation planning, a Plan review and independent QA follow."

- TypeSafe cell: Opus 5.5 at extra high
- Rung probabilities: score 3.33, confidence 0.55: low 0.00, medium 0.00, high 0.19, extra high 0.29, max 0.52, ultracode 0.00; twelve cells (computed): Opus 5.5 at low 0.00, Opus 5.5 at medium 0.00, Opus 5.5 at high 0.13, Opus 5.5 at extra high 0.21, Opus 5.5 at max 0.37, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.06, Fable 5.1 at extra high 0.08, Fable 5.1 at max 0.15, Fable 5.1 at ultracode 0.00. Flags: none
- Model probabilities: Fable 5.1 0.29, Opus 5.5 0.71, confidence 0.42
- Detail: v6 sent 2026-10-12T19:08:01Z; HTTP 200 in 0.83 s; 4214 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); the modal rung is max. Model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- Nathan's pick: not stated.

Surface advice: run CF-C-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. The review is read-only against `docs/pfcanon/` on `main` and writes only its decision artifact under `docs/ephemeral/`. PF30.1 v0.9.1 (#614) should be on `main` first, because this Specification cites it as the format owner.

## Canon relied on

Read on `main` at `2aed56f1`, except PF30.1 v0.9.1, read on its branch (#614):
- PF06-Canon-Change-Process-Guide v2.5.4: §0.1 "Specification format authority"; §0.5.1 Epic path normalization, "Plan path provenance" and "Plan locus validation labels"; §0.6.9 Plans are pointers; §1.0.2 Lead Developer analysis and CRD Specification; §1.0.3 PF30 registration and approval; §1.0.4 Phase separation and execution; §1.0.5 Canon changes; §1.0.6 QA, closeout, and PF30 result update.
- PF27-Canon-Plan-Templates v2.0.5: "Artifact execution boundary"; §2A HDE-CRD-Specification Profile and PF30 Record Contract, all subsections.
- PF30.1-Canon-HDE-CRD-Records v0.9 and v0.9.1: §1 to §7 in full, and the §8 HDE-CRD-0001 record as precedent.
- PF04-Canon-HDE-Governance v2.8.7: §9.1, change classes; §9.1.1 Change authority and exact-artifact lineage, including the role table and "Historical drainage"; §9.7.3 Identifier fidelity and optional legacy cross-references (Product Owner-owned ADR stubs).
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability (normative)"; "QA evidence and work-product path grammar (normative)"; §4.3 Rules (evidence root).
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: §1.2 Titles-only routing, "Close-pack artifacts" and "Change-container compatibility (normative)".
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §7.1.11 SAFE rails and production vendor override: the opening paragraphs, §7.1.11a and §7.1.11b in full, and the §7.1.11c to §7.1.11f headings.
- PF29-Canon-HDE-Users-Guide v1.0.2: §16 Known limitations and nonclaims.
- PF20-Reference-HDE-Phased-Epics v1.9.6: §2.26.7 Tracked Issues, Variances and Remaining Owners.
- PF21-Reference-7 Phases of Alchemical Engineering: definitions in §4 Conjunction, §5 Fermentation, §6 Distillation and §7 Coagulation.
- PF09.1 to PF09.7 Build Checklist volumes: phase descriptions; PF09.5 task list (HDE-FERM001, HDE-FERM005); PF09.1 change-scoped QA root criterion.
- PF10-HDE-Build-Notes v13.5.2: read in full; addendum 2.1 governs the TypeSafe reading above; nothing else applies.
- `AGENTS.md`: canon-first rule; canon read-only; CI-exempt documentation prefixes; dev routes gated to dev, test and local.

In-flight documents: the kickoff, class-selection record and briefs v1.2 named in the front matter. Prompt release: GCFPE-20261009.1 / 100926.1, read from the GCFPE Membership and Release Register on 2026-10-12.
