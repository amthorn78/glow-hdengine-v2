---
artifact_type: RESCOPE_PROPOSAL
artifact_id: HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL
artifact_version: "1.0"
artifact_state: RESCOPE_PROPOSAL_PENDING_REVIEW
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-22T06:24:04Z
next_stage: RS-20
---

# HDE-EPIC040-PR04-F01 — Bounded Work-Unit Rescope Proposal v1.0

## 1. Identity, status and authority boundary

| Field | Value |
| --- | --- |
| Artifact type | `RESCOPE_PROPOSAL` |
| Logical ID | `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL` |
| Version | `1.0` |
| Status | `RESCOPE_PROPOSAL_PENDING_REVIEW` |
| `CHANGE_CLASS` / `CHANGE_ID` | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| `WORK_UNIT_ID` | `HDE-EPIC040-PR04` — Bounded application, identity and consumer integration |
| `FINDING_REF` | `HDE-EPIC040-PR04-F01` |
| Author / role | RS-10 finding author, acting in the retained whole-change HDE-EPIC040 Implementation Architect session; no approval authority |
| `session_disposition` | `RETAIN_EXISTING` |
| `role_session_ref` | The retained whole-change HDE-EPIC040 IA session recorded on the Flow Index; the dedicated PR-development session `PR04-HDE-EPIC040-1` is retained separately and is not replaced |
| `invocation_binding` | `HDE-EPIC040 / HDE-EPIC040-PR04 / RS-10` (`GCF-17.RESCOPE`) |
| `context_conflict` | `NONE` established |
| `AUTHORING_CONTEXT` | `APPROVED_BASE_WITH_OVERLAYS` |
| Capture time | `2026-09-22T06:24:04Z` |
| Output class / path | `REPOSITORY_CONTROLLED` / `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` |

This proposal is evidence for RS-20. It is not an approval, not a PF10 addendum, not implementation authority, not a Proceed, not a Specification change and not a merge instruction. RS-10 has no authority to approve scope, a Plan, remediation or Product Owner intent, and produces no addendum.

## 2. Applicable approved bases and overlay lineage

Bases applicable to the actual originating stage (PR-20 planning for PR04). All repository paths are in `amthorn78/glow-hdengine-v2`, branch `main`, and every SHA-256 below was independently recomputed by this author at the head named in §3.

| Role | Artifact type / approval lineage | Repository path and SHA-256 |
| --- | --- | --- |
| `SPECIFICATION_ID` | `SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`; Thoth-17 `APPROVE` 2026-09-08T13:23:24Z | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`; `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` (as supplied; not independently recomputed — see §11 U-03) |
| `IMPLEMENTATION_AUDIT_ID` | `IMPLEMENTATION_AUDIT` v2.0, `AUDIT_COMPLETE` | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` |
| `IMPLEMENTATION_PLAN_ID` | `IMPLEMENTATION_PLAN` v2.1, immutable approved base | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`; recomputed `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` — matches |
| `PLAN_REVIEW_ID` | `IMPLEMENTATION_PLAN_REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z; redline `R040-IA30-02` | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| `PR_INSTRUCTION_ID` | `PR_INSTRUCTION` v1.0, `INSTRUCTION_READY` | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md`; recomputed `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf` — matches |
| `PR_IMPLEMENTATION_PLAN` | `PR_IMPLEMENTATION_PLAN` v1.0, state `DRAFT`, carries F01 in its §14.1 | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md`; recomputed `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65`, 653 lines / 122,661 bytes — matches |
| Accepted dependencies | PR01 `ACCEPT` (PR #403); PR02 `ACCEPT` (PR #404); PR03 `ACCEPTED_FINAL` (PR #405, merged `9cda1b49a972da874021e8820997fab1ebaff153`) | `docs/ephemeral/HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md`, `…PR02-…-v1.0.md`, `…PR03-…-v1.0.md` |

**Current controlled PF10**, resolved and completely read from `docs/pfcanon/` at authoring time: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, recomputed SHA-256 `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f` — matches the supplied value. Recorded as provenance of what was read; it gates nothing downstream.

**Applicable active addendum overlays**, by repository path: §2.2 (PF10 body only); §2.3 `docs/ephemeral/HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md`; §2.4 `docs/ephemeral/HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md`; §2.5 `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md`; §2.6 `docs/ephemeral/PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md`; §2.7 `docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md` and `…-v2.0.md`; §2.8 PF10-FORM-001 (form rule for any addendum RS-20 may produce; RS-10 produces none); §2.9 `docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md`; §2.10 `docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md`; §2.11 (PF10 body; review body `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md`); §2.12 `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md`; §2.13 `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md`. PF10 §2.14 exists in the body and is not applicable to this finding.

Two overlays are load-bearing here: **§2.12** places the executing-mechanics admission boundary in `engine/config/registry_loader.py`, and **§2.13** fixes the dependency order `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01`.

## 3. Repository baseline, re-verified

- Current `main` head at authoring time: **`3e943ada3987720cf69c491c2cb7eb4bc9e1ae45`**, tree `61d11813065eb77974f63fc85dab29a24489f9f1`, committed 2026-09-22T07:17:33+01:00. Working tree clean.
- The handoff named head `6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612`. That commit is an ancestor of the current head. **`git diff 6ecacafb..main -- . ':(exclude)docs/'` is empty**: every commit since is documentation-only, so the plan's read-only verification at `6ecacafb` remains exactly valid at `3e943ad`. The finding is unaffected.
- Executable baseline is still precisely the accepted PR03 state `9cda1b49a972da874021e8820997fab1ebaff153`. The only post-PR03 commits touching `ci/` or `.github/` are `3c0b1fa` and `c683255`; both are ancestors of `6ecacafb` and were therefore already inside the plan's verification window.
- No PR04 product branch, commit, pull request, Proceed, implementation result, review, CI result or merge exists. Nothing is fabricated here.
- The plan artifact and the PR04 instruction are both present on `main`; their storage pull requests **#452 and #453 have merged** (see §11 U-01).

## 4. Suspended boundary — proven

### 4.1 The approved obligation

PR04's approved completion condition (Plan §6.4, instruction §4, plan §4.2 condition 4) requires its integration paths and proofs to pass actual code review, security review **and CI**, with instruction §12 stating that no inherited CI exception or prior green run applies to this unit.

PR04's approved behavior requires removing every legacy success path — `compat_public` hash scoring, the `ts_v0` band and UID-only substitutes (instruction §10) — and consuming only the admitted mechanics bundle through the PF10 §2.12 admission owner, with instruction §10 stating that if a valid admitted release is unavailable, canonical integrated success refuses and there is no legacy fallback.

### 4.2 Executed evidence, at current head `3e943ad`

Two executed observations, not readings, establish the collision. Both were run with `LC_ALL=C LANG=C TZ=UTC`, a clean working tree, and produced no repository mutation (`git status` clean afterwards).

**E-01 — the admission owner refuses today.** Under closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0`):

```
python -c "from engine.config.registry_loader import load_active_mechanics_bundle; load_active_mechanics_bundle()"
→ SchemaValidationError INCOMPLETE_RELEASE_ROSTER
  "release manifest does not yet contain the complete adopted roster"
```

Cause, read directly: `catalog/manifest.json` carries **15** entries in `files`; `ADMITTED_RELEASE_ROSTER` in `engine/config/registry_loader.py:400` is pinned to **44** members by the import-time invariant at line 447, and `_validate_admitted_manifest` (lines 1218–1226) raises `INCOMPLETE_RELEASE_ROSTER` whenever the manifest paths are a strict subset. Complete release admission is PR06's owned work (Plan §6.6). **Between PR04 and PR06 there is therefore no real admitted release, and so no real CLI, HTTP or evidence-generator success path.**

**E-02 — a selected ordinary-CI gate is green today, and is green only because of the legacy path PR04 must delete.** Under the rails the job definition itself declares (`ci/jobs/rails_open_conformance.yml`: `SAFE_MODE=0 ALLOW_NETWORK=1`):

```
python tools/evidence/generate_open_rails_abba_proof.py --check-current
→ exit 0
  {"path":"audit/gates/determinism/open_rails_abba.json","result":"pass",
   "status":"OK","top_level_pass":true}
```

Its predicate map is all-true, including `abba_byte_identity`, `reader_cli_ab_identity` and `reader_cli_ba_identity` — predicates that compare in-process Reader bytes against the bytes of a real `scripts/hdctl.py showcompat --dump-reader` **subprocess** (`tools/evidence/generate_open_rails_abba_proof.py:421–422`, predicates at 490–492, `top_level_pass` at 521, `validate_current_fixture` at 543–547). That gate is green because `engine/runtime/public.py:29–32` still derives the band from `ts_v0`, entirely bypassing the admission owner. PR04 deletes exactly that path.

The two observations are the finding: **E-02's gate requires live success on paths that, after PR04's approved change, must route through E-01's refusal.**

### 4.3 The three selected gates

| # | Gate | Chain, verified by reading the cited code | Why PR04 cannot satisfy it |
| --- | --- | --- | --- |
| 1 | Rails lane | `.github/workflows/ci.yml:164–172` ("Run rails policy and secret-safety lane") → `ci/jobs/rails_open_conformance.yml:18` → `generate_open_rails_abba_proof.py --check-current` | Needs in-process **and subprocess** CLI success. A subprocess cannot receive a test-only bundle, and instruction §6.4 forbids a test-only bundle in a governed gate ("local fixture candidates stay test-only"). |
| 2 | Release lane | `.github/workflows/ci.yml:228, 259` → `build_release_attestation.py --require-clean` → `run_sanity_pipeline.py` stage 04 (`generate_determinism_gate_proofs.build()`, `generate_open_rails_abba_proof.build_fixture_proof()`; lines 126–127) and stage 05 (`generate_a7_transport_proofs.build()`; line 149) → `AttestationBuildError("final_sanity_pass_missing")` at `build_release_attestation.py:766` | Same live success requirement. The lane is selected for **every** PR04 code path: `ci/checks/classify_ci_changes.py` assigns `{"product","release"}` to any path under `_PRODUCT_PREFIXES`, which includes `engine/`, `adapter/`, `presenter/`. |
| 3 | Full-validation roster | `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` in `ci/checks/classify_ci_changes.py:40` (includes `tests/cli/test_showcompat_sources.py`); `tests/transport/test_a7_transport_proofs.py` calls the live A7 build; `tests/http/test_reader_a7_transport.py` asserts `GET /reader` 200 and `POST /reader` 405 | Convertible inside pytest, but only by changing `tools/evidence/generate_a7_transport_proofs.py`, whose `capture()` hard-requires `post.status_code == 405` (line 75) — and whose live `build()` **is** release-sanity stage 05. So item 3 cannot be separated from item 2. PR04's approved §6.5 implements Reader POST success, which contradicts the pinned 405. |

### 4.4 Why no treatment inside PR04's approved loci is both truthful and permitted

| Treatment available inside instruction §7.1 | Why it fails |
| --- | --- |
| Retain any legacy success path | Prohibited by instruction §10 |
| Expand or activate the manifest | Excluded by instruction §9; PR06-owned; PF10 §2.13 fixes the order |
| Bypass, relocate or weaken admission | Prohibited by PF10 §2.12 |
| Feed a synthetic or test-only release into a governed gate or the attestation | Prohibited by instruction §6.4; a `PR06R_B_FINAL_PASS` produced that way is a fabricated passing result |
| Convert the gates to frozen-byte comparison while still emitting PASS | Weakens a release gate; instruction §6.6 forbids weakening a refusal to preserve an old fixture |
| Skip, disable or quarantine the gates or tests | Prohibited by `AGENTS.md` |

Every **truthful** treatment instead touches files outside instruction §7.1: `tools/evidence/run_sanity_pipeline.py`, `tools/evidence/build_release_attestation.py`, `.github/workflows/ci.yml`, `ci/jobs/rails_open_conformance.yml`, `tools/evidence/generate_a7_transport_proofs.py`, `tools/evidence/generate_open_rails_abba_proof.py`.

## 5. Classification

**This is a bounded implementation rescope.** It is not an ordinary in-scope correction and not a Specification change.

- **Not an in-scope correction.** An in-scope correction is one the existing owner can make under unchanged authority. Here every truthful treatment lies outside the work unit's approved loci, so the PR04 engineering owner cannot make any of them without exceeding its authorization. §4.4 enumerates the closed set.
- **Not a Specification change.** Nothing about the product's required behavior, intent, exclusions or acceptance moves. `HDE-EPIC040-SPECIFICATION` v1.1 and Plan v2.1 §§5.7, 5.8, 6.4 are satisfied exactly as written; §8's requirement-to-unit mapping is unchanged in substance. What is missing is only a truthful way for three CI gates to express a state the approved plan itself creates — the interval between PR04's consumer switch and PR06's release admission. That interval is a consequence of the approved dependency order, not a departure from it.
- **Not a defect in PR01–PR03.** PR03 passed these gates lawfully; its consumers still used `ts_v0` (E-02). No accepted-final work is reopened or rerun.

## 6. Smallest Specification-compatible overlay

### 6.1 A material narrowing found during this review

The plan's candidate A anticipated that a truthful interim posture might require a **PF12 canon decision**, because `build_release_attestation.py` emits the canon-owned wire value `PR06R_B_FINAL_PASS`. Inspection of the actual schemas shows that is very likely unnecessary:

- `schemas/hde_release_attestation.v1.json` pins `validation_result: const "PASS"`, `release_admission: const "PR06R_B_FINAL_PASS"` and `pipeline_stop: const null`. The success attestation is, by construction, emitted only on a complete pass. **Withholding it requires no schema change** — the builder already refuses.
- A **failure receipt contract already exists in canon**: `schemas/hde_release_attestation_failure.v1.json`, required fields `schema`, `code`, `stage`, `returncode`, `secret_values_recorded`. `build_release_attestation.py::_write_failure` (lines 498–507) already writes a canonical `failure.json` under `hde.release_attestation.failure.v1` on every `AttestationBuildError`, including today's `final_sanity_pass_missing`.
- That schema's `code` and `stage` are **open lowercase-token strings** (`"pattern": "^[a-z0-9_]+$"`), not enums. A distinct, truthful code such as `release_not_admitted` is therefore already expressible **without any PF12 schema or wire-value change**.

The truthful interim state is thus already representable in current canon. What is genuinely missing is only the three items in §6.2.

### 6.2 Proposed bounded delta

Extend PR04's approved loci to exactly the six files named in §4.4, for one purpose only: to make the affected gates express a truthful, explicit non-admitted outcome instead of an ambiguous failure, and to let ordinary CI accept that one specific outcome until PR06 lands.

1. **Explicit non-admitted outcome, never PASS.** When the active release is not admitted, `generate_open_rails_abba_proof.py --check-current`, sanity stages 04 and 05, and the A7 builder each record an explicit `RELEASE_NOT_ADMITTED` outcome. It is never `PASS`, never `top_level_pass: true`, and never a frozen-byte substitute presented as a live result. Frozen captures stay frozen and keep their existing nonclaims.
2. **Attestation withholds the success value.** `build_release_attestation.py` continues to refuse, emits no success attestation and no `PR06R_B_FINAL_PASS`, and writes its existing canonical failure receipt carrying a distinct code (proposed `release_not_admitted`) and its stage — under the existing `hde.release_attestation.failure.v1` contract, with no schema change.
3. **Bounded CI acceptance with an explicit end.** `.github/workflows/ci.yml` and `ci/jobs/rails_open_conformance.yml` accept that one explicit outcome as non-blocking **only while the active release is not admitted**. The condition is self-extinguishing: once PR06 admits the complete 44-member roster, the gates return to requiring PASS automatically, with no second decision and no cleanup PR required.

This is the plan's candidate **D** (candidate A executed inside PR04 under an overlay that names the files), narrowed by §6.1 so that no PF12 canon decision is expected.

**If, during implementation, the delta turns out to require a change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value, that portion is a PF12 canon decision and must be routed to the governed PF12 maintainer as a separate finding.** This proposal does not pre-authorize it, and §6.1 is the reason it is not expected to arise.

### 6.3 Alternatives considered, with costs

| Candidate | Delta | Authority required | Cost |
| --- | --- | --- | --- |
| **D (recommended)** | §6.2, inside PR04 under an overlay naming the six files | Bounded implementation rescope; RS-20 `APPROVE` with one PF10 addendum overlay | Widens PR04's loci to six CI/evidence files. Smallest truthful change; self-extinguishing at PR06; keeps the approved dependency order and every approved base intact. |
| A | Same delta, but as its own unit of work | Same, plus a new unit in an immutable Plan | Identical engineering, but adds a work unit to an approved decomposition — strictly larger than D for the same result. |
| B | Re-sequence so PR06's complete release admission lands before PR04's consumer switch | Whole-change Plan dependency-order change against PF10 §2.13; IA/Isis decision | Largest. Touches the immutable Plan's ordering, and PR06's own admission work depends on PR04/PR05 outputs, so the re-sequence is not obviously coherent. |
| C | Land PR04 with rails/release lanes truthfully red under a scoped Product Owner CI waiver until PR06 | Product Owner decision; contradicts instruction §12 unless expressly granted | Leaves ordinary CI red across PR04 and PR05, so every later candidate in that window loses its signal. Defers rather than resolves. |

**Recommended disposition: D.** It is the smallest change that makes CI tell the truth, needs no canon decision on current evidence, preserves the approved order and every approved base, and ends by itself when PR06 lands. C is the fallback if RS-20 judges that widening PR04's loci is not available to it; C then requires Nathan's express waiver, and this proposal does not request one.

## 7. Effects

| Dimension | Effect |
| --- | --- |
| Requirements | None changes in substance. The affected obligations are `K040-REQ-012` and `AC040-08` (evidence coherence) and the CI clause of PR04's completion condition (plan §4.2 item 4). |
| Dependencies | PR05 (golden comparison, read-only readiness) inherits the same interim gate condition while it too runs before PR06. PR06 owns convergence under any disposition. The dependency order itself is unchanged under D. |
| Tests | Plan §8 is unchanged. The six `R040-IA30-02` proof classes, the eligibility matrix, the Reader POST suite and the CLI/compat carriers all stand as designed. Only the three conversions coupled to item 3 of §4.3 depend on the disposition. |
| Ops | None. No Ops task, environment, deployment or vendor operation is created or required. |
| Documentation | None beyond this proposal and the RS-20 decision. No PF-Canon edit is proposed. If RS-20 approves, RS-20 (not this actor) emits exactly one PF10 addendum overlay under PF10-FORM-001. |
| Downstream | No effect on PR07, OPS01, independent QA, release promotion, PF09 movement or Epic closure. |
| Evidence integrity | Frozen historical captures stay frozen and unedited. No governed evidence is hand-edited, and no new evidence family is created. |

## 8. Completed valid work preserved

Preserved intact, and not reopened by this proposal: plan §§5–8 in full (designed interfaces, invariants, contracts, the exact file and component plan, the requirement-to-change-and-test mapping and the complete test design); plan §9 checkpoints C1–C3, which remain executable exactly as written; plan §§10–12 (local validation commands, review checklists, risk register). Only plan §9 item 15 and §4.2 condition 4 depend on this disposition.

Unchanged and untouched: the approved Specification, Audit, Plan v2.1 and Plan Review v2.1 as immutable bases; accepted-final PR01, PR02 and PR03, which are historical evidence and are never rerun; the original authority of every existing owner; the dedicated PR04 session `PR04-HDE-EPIC040-1`; the PF10 overlays in §2.

## 9. Originating stage, vehicle state and lawful return point

- **Originating stage:** PR-20 planning for `HDE-EPIC040-PR04`, in session `PR04-HDE-EPIC040-1`.
- **Vehicle state:** no Proceed, no workspace, no worktree, no branch, no open PR, no commit, no CI run. These are truthfully **not yet produced**, not missing prerequisites. **No `PR_RETURN_PHASE` field applies** and none is asserted; the PR-30/PR-35 execution return-phase vocabulary is not in play.
- **Lawful return point:** session `PR04-HDE-EPIC040-1`, plan v1.0 `DRAFT`.
- **After RS-20:** `APPROVE` → exactly one PF10 addendum overlay is emitted by RS-20, and that session issues plan v1.1 as a complete successor carrying the overlay, in state `AWAITING_PO_PROCEED` for Nathan's `PR-30` invocation. `REJECT` → the decision and preserved evidence return to that session; the plan cannot truthfully reach `AWAITING_PO_PROCEED` without a Product Owner decision on candidate C. `REVISION_REQUIRED` → RS-30, to this same proposal author. `SPECIFICATION_CHANGE_REQUIRED` → Nathan and the Specification owners.
- No route restarts IA-30 or IA-40, rewrites an approved base, mints a Proceed, reruns accepted-final work, merges, or invokes PR-50. Only Nathan may invoke PR-50 for an exact PR.

## 10. Evidence index

| ID | Claim | Exact source | Kind |
| --- | --- | --- | --- |
| E-01 | Admission refuses `INCOMPLETE_RELEASE_ROSTER` at current head | `load_active_mechanics_bundle()` executed under closed rails; `engine/config/registry_loader.py:400, 447, 1218–1226` | Executed + read |
| E-02 | Rails ABBA gate is green at current head, all predicates true | `tools/evidence/generate_open_rails_abba_proof.py --check-current` executed under `SAFE_MODE=0 ALLOW_NETWORK=1`, exit 0 | Executed |
| E-03 | Manifest carries 15 members against a 44-member pinned roster | `catalog/manifest.json` `files` length; `ADMITTED_RELEASE_ROSTER` invariant | Read |
| E-04 | Gate compares live Reader bytes against a real `hdctl` subprocess | `generate_open_rails_abba_proof.py:421–422, 490–492, 521, 543–547` | Read |
| E-05 | Release lane is selected for every PR04 product path | `ci/checks/classify_ci_changes.py`: `_PRODUCT_PREFIXES` → `{"product","release"}` | Read |
| E-06 | Attestation fails closed on a sanity-stage failure | `tools/evidence/build_release_attestation.py:766` | Read |
| E-07 | Sanity stages 04/05 invoke the determinism, ABBA and A7 builders live | `tools/evidence/run_sanity_pipeline.py:68, 126–127, 149` | Read |
| E-08 | A7 capture hard-requires `POST /reader` → 405 | `tools/evidence/generate_a7_transport_proofs.py:75` | Read |
| E-09 | `POST /api/reader` currently returns 405 `method_not_allowed` | `adapter/http_reader.py:459–462` | Read |
| E-10 | The legacy band path is still live, which is why E-02 is green | `engine/runtime/public.py:29–32` (`ts_v0`) | Read |
| E-11 | A canonical failure-receipt contract already exists and is already written | `schemas/hde_release_attestation_failure.v1.json`; `build_release_attestation.py:498–507` | Read |
| E-12 | The failure receipt's `code` and `stage` are open tokens, not enums | `schemas/hde_release_attestation_failure.v1.json` `"pattern": "^[a-z0-9_]+$"` | Read |
| E-13 | Success attestation pins `PASS` / `PR06R_B_FINAL_PASS` / `null` as consts | `schemas/hde_release_attestation.v1.json` | Read |
| E-14 | No non-documentation drift between the plan's verification head and current head | `git diff 6ecacafb..main -- . ':(exclude)docs/'` empty | Executed |

**Execution environment for E-01, E-02 and E-14.** Python in the session container, with `requirements.txt` and `requirements-dev.txt` installed at authoring time; `LC_ALL=C LANG=C TZ=UTC`; clean working tree before and after; no repository mutation, no network vendor call, no write to any governed artifact. A first attempt at E-02 failed on the single predicate `canonical_gate_success` because `flask` was not yet installed in this container; that was a local environment gap, not a repository defect, and E-02 above is the result after installing the declared requirements. That distinction is recorded rather than suppressed.

## 11. Risks, exclusions and unresolved facts

**Risks.** R-01: an overlay that widens a work unit's loci to CI and evidence files sets a precedent; it should be written to name the six files exactly and to bind the acceptance to the not-admitted condition, so it expires at PR06 rather than persisting. R-02: if the ordinary-CI acceptance in §6.2 item 3 is written loosely, it could mask an unrelated genuine failure in those lanes; it must key on the explicit `RELEASE_NOT_ADMITTED` outcome only. R-03: PR05 runs in the same interval and will inherit the condition; RS-20 should state whether the overlay covers PR05 or whether PR05 needs its own reference to it.

**Exclusions.** This proposal does not approve anything, does not draft or number a PF10 addendum, does not edit PF-Canon, does not request or imply a Proceed, does not create a branch or PR for PR04, does not implement, does not change the immutable Plan, does not rerun accepted-final work, and does not invoke or route to PR-50.

**Unresolved facts, all non-gating.**
- **U-01 (correction to the supplied handoff).** The handoff records `main` at `6ecacafb…` and the plan's storage PR #453 as open and unmerged. At authoring time `main` is `3e943ad…` and both #452 and #453 have merged, so the plan and instruction are on `main`. Every supplied SHA-256 was recomputed and matches. Nothing in F01 changes.
- **U-02.** Plan §14.2 records a potential second boundary (decision D-03, the valid self-pair exit-0 carrier). It is deliberately **not** bundled into F01 and is not raised here.
- **U-03.** The Specification SHA-256 in §2 is carried as supplied and was not independently recomputed in this invocation; the Specification's content is not load-bearing for F01, whose cause is entirely in repository code and CI configuration.
- **U-04.** The repository-resolved current PF12 is v2.9.5 while the approved Plan's register overlay records v2.9.6, as already recorded in the PR04 instruction §3.4. Owner: the governed PF12 maintainer. It does not affect F01 or §6.1, which cite the repository's actual schema files.

## 12. Carried `CANON_CONFLICT_REGISTER`

Carried unchanged from Plan v2.1 §11.1 and PR04 instruction §13. **No entry is reopened, relabeled, omitted, newly decided or resolved here, and `HDE-EPIC040-PR04-F01` is not a register entry.**

| ID | Classification / status | Decision lineage | Carried effect | Remaining owner / state |
| --- | --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED` exactly as proposed | Thoth-17, 2026-09-08T13:23:24Z, against Specification v1.0 represented by approved v1.1 | Preserve explicit `Done` exclusions and current PF09.3 agreement | Source correction resolved; no drainage pending |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use the current controlled PF12 Markdown; historical identity mismatch is history only | Resolved; PF12 version currency is ordinary maintenance (U-04) |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use current PF14 v3.5.7; C040-05 controls its contradictory core-test text | Historical mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | QA identity history preserved; PR04 performs engineering checks, not independent QA | Historical mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED`, alternative A exactly | Isis-49, 2026-09-09T03:57:16Z, against Plan v1.0 | The four-argument Gate core supersedes precomputed-score passages; no second calculator | Permanent PF14 §6.7 correction pending with its governed maintainer; non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED`, alternative A exactly | Isis-50, 2026-09-09T11:48:08Z, Review v2.0 against Plan v2.0 and ADR v1.0 | 36-row taxonomy and 16-case conformance as delivered through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage pending with governed maintainers; non-gating |

Review fields for this proposal itself remain explicitly **not yet reviewed**: reviewer, reviewed artifact version, decision, decision time and rationale are RS-20's to supply.

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES` — this entry, preserving the earlier ones by exact reference:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`
- `work_unit_id` / `finding_ref`: `HDE-EPIC040-PR04` / `HDE-EPIC040-PR04-F01`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `RS-10 — Create Bounded Work-Unit Rescope Proposal — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4?pvs=204`
- `prompt_retrieved_revision`: page fetched, `page_last_edited_at` `2026-09-21T22:57:33.281Z`
- `role_stage`: retained whole-change HDE-EPIC040 IA session / RS-10 finding author
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `capture_time`: `2026-09-22T06:24:04Z`
- `runtime_identity`: not asserted beyond the Product Owner-assigned role and session reference
- `result`: this `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0`, `RESCOPE_PROPOSAL_PENDING_REVIEW`
- `result_refs`: repository path in §1; branch, commit and pull-request identities populated only after they exist

Preserved earlier entries, by exact reference: `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01` (plan §16) and `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (instruction §15).

Repository provenance persistence remains `PENDING / NON_GATING`: `docs/changes` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`, with no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination. Nothing is invented, and this gap blocks no authorized work. Owner: the authorized repository writer, once an actual procedure is installed.

## 14. Decision requested

RS-20 is asked to classify `HDE-EPIC040-PR04-F01` and decide the bounded delta in §6.2, with §6.3's alternatives and §6.1's narrowing in evidence. The recommended disposition is **candidate D**. A qualifying `APPROVE` emits exactly one PF10 addendum overlay under PF10-FORM-001; that addendum is RS-20's to produce, not this author's.

ASK OK?
