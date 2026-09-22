---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
artifact_id: HDE-EPIC040-PR04-F01-PF10-BUILD-NOTES-ADDENDUM
artifact_version: "1.0"
addendum_id: HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
page_ready_heading_number: NOT_ALLOCATED_BY_RS20
observed_last_addendum_in_pf10_body_at_authoring: "2.14"
observed_last_addendum_in_pf10_index_at_authoring: "2.13"
producing_prompt:
  id: RS-20
  name: RS-20 — Review Bounded Work-Unit Rescope — 091426.1
  selected_version: "091426.1"
  ecosystem_release: GCFPE-20260914.1
  notion_url: https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204
  retrieved_revision: "2026-09-21T22:57:36.541Z"
approval_decision:
  id: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW
  version: "2.0"
  decision: APPROVE
  reviewer: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
  decision_time_utc: 2026-09-22T07:27:55Z
  repository_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md
  reviewed_artifact: HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1
  reviewed_artifact_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md
  reviewed_artifact_sha256: 6bef3daf72eb4b547f43fa9efb49a548f68e97bbb8113c27f7ba13c4dec3756b
immutable_base:
  id: HDE-EPIC040-IMPLEMENTATION-PLAN
  version: "2.1"
  sha256: 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be
  repository_path: docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md
  approval_lineage: HDE-EPIC040 Implementation Plan Review v2.1, Isis-50 APPROVE 2026-09-09T13:36:43Z, redline R040-IA30-02 — docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md
  specification: HDE-EPIC040-SPECIFICATION v1.1, SPECIFICATION_APPROVED, Thoth-17 APPROVE 2026-09-08T13:23:24Z — docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md
  audit: HDE-EPIC040 Implementation Audit v2.0, AUDIT_COMPLETE — docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md
  work_unit_instruction: HDE-EPIC040-PR04-PR-INSTRUCTION v1.0, INSTRUCTION_READY — docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md
applicable_prior_addenda:
  - docs/ephemeral/HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md
  - docs/ephemeral/PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md
  - docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v2.0.md
  - docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md
  - docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md
  - docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md
pf10_read_at_authoring:
  path: docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md
  sha256: 1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f
repository_baseline:
  main_head: 0f47079f24834424c4a4cfaba6a8d44d94286ad2
  tree: 0865ef1814d238910b7da1e935d04124980aba34
  executable_baseline: 9cda1b49a972da874021e8820997fab1ebaff153
return_phase:
  pr_return_phase: NOT_APPLICABLE
  native_return_stage: PR-20 — Create Detailed PR Implementation Plan — 091426.1
  native_return_session: PR04-HDE-EPIC040-1
  resulting_state: AWAITING_PO_PROCEED
  rs40_eligible: false
conflicts: NONE
transport_metadata_excluded_from_pf10_body: true
---

## 2.x HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval

### Status and authority

`HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v2.0` approves a bounded implementation overlay for finding `PR04-F01` against the immutable HDE-EPIC040 Specification v1.1, Implementation Plan v2.1, approving Plan Review v2.1, and PR04 Instruction v1.0.

The approved bases remain immutable and valid. The overlay does not replace or revise an approved base, create a Product Owner Proceed, reopen accepted PR01, PR02 or PR03, change the whole-change dependency order, or authorize implementation beyond the stated delta. The overlays effective in PF10 §§2.7, 2.9, 2.10, 2.12 and 2.13 remain approved within their exact scopes and are not reopened; §2.10 in particular remains scoped to HDE-EPIC040-PR02 alone.

No Product Owner Proceed exists for HDE-EPIC040-PR04. The overlay confers none, and confers no merge, PF09, QA, acceptance or closure authority.

### Evidence-supported boundary

PR04's approved completion condition requires its integration paths and proofs to pass actual code review, security review and ordinary CI, with no inherited CI exception. PR04's approved behavior requires deleting every legacy success path — `compat_public` hash scoring, the `ts_v0` band and UID-only substitutes — and consuming only the admitted mechanics bundle through the admission owner in `engine/config/registry_loader.py` established by PF10 §2.12.

The actual repository release is the incomplete fifteen-member `catalog/manifest.json`, against the forty-four-member `ADMITTED_RELEASE_ROSTER` pinned by the import-time invariant in `engine/config/registry_loader.py`. `load_active_mechanics_bundle()` refuses with `SchemaValidationError INCOMPLETE_RELEASE_ROSTER`, and `_validate_admitted_manifest` raises on any strict subset. Complete release admission is HDE-EPIC040-PR06's owned work, as PF10 §2.13 independently records. Between PR04's consumer switch and PR06's admission there is therefore no real CLI, HTTP or evidence-generator success path.

Three ordinary-CI chains execute exactly such live success paths and are selected for every PR04 candidate: the rails lane through `ci/jobs/rails_open_conformance.yml`; the release lane through `tools/evidence/build_release_attestation.py`, its gate wrapper `tools/evidence/run_sanity_pipeline_gate.py`, and release-sanity stages 04 and 05; and the full-validation supplemental roster, which a PR04 candidate selects because its plan changes `ci/checks/classify_ci_changes.py`.

A PR04-shaped change confined to PR04's own approved loci — `engine/runtime/public.py` banding through the admission owner instead of `ts_v0`, and `adapter/http_reader.py` implementing the contracted Reader `POST` success path at its existing declared route — turns all three chains red. Every failure observed falls inside the enumerated set below or inside loci PR04 already owns.

This is a bounded mismatch between an approved completion condition and approved loci. It is not a defect in PR01 through PR03, which passed these gates lawfully while their consumers still used `ts_v0`. It changes no product objective, requirement text, exclusion, mathematics, taxonomy, public contract, identity formula, work-unit order or Product Owner scope.

### Approved bounded overlay

PR04's approved loci extend to the files enumerated below, for one purpose only: the affected gates express a truthful, explicit non-admitted outcome instead of an ambiguous failure, and ordinary CI accepts that one outcome while the active release is not admitted.

1. **Explicit non-admitted outcome, never a pass.** When the active release is not admitted, the affected gates and release-sanity stages each record an explicit `RELEASE_NOT_ADMITTED` outcome. That outcome is never `PASS`, never `top_level_pass: true`, and never a frozen-byte substitute presented as a live result. Frozen captures remain frozen and retain their existing nonclaims.

2. **The attestation withholds its success value.** `tools/evidence/build_release_attestation.py` continues to refuse, emits no success attestation and no `PR06R_B_FINAL_PASS`, and writes its existing canonical failure receipt under `hde.release_attestation.failure.v1` carrying a distinct code — `release_not_admitted` — and its stage. The receipt's `code` and `stage` are open lowercase-token strings, so this requires no PF12 schema or wire-value change.

3. **Bounded ordinary-CI acceptance with an explicit end.** `.github/workflows/ci.yml` and `ci/jobs/rails_open_conformance.yml` accept that one explicit outcome as non-blocking, keyed on the outcome itself and on the observed non-admitted state of the active release, and on nothing else. The acceptance is conditioned on a runtime-observable fact rather than a fixed window, so it self-extinguishes: once PR06 admits the complete forty-four-member roster the branch is never taken.

### Bounded implementation and test loci

Production and CI configuration, nine files:

* `tools/evidence/generate_open_rails_abba_proof.py` — the rails lane invokes it directly, so the discrimination lives in this file; it is also reached inside release-sanity stages 04 and 06.
* `tools/evidence/generate_a7_transport_proofs.py` — its `capture()` hard-requires `POST /reader` → 405 and `GET /reader` → 200, and its live `build()` is release-sanity stage 05.
* `tools/evidence/generate_determinism_gate_proofs.py` — release-sanity stage 04 calls its `build()`, which emits a live Reader envelope and runs a real CLI `showcompat --dump-reader` subprocess.
* `tools/evidence/run_sanity_pipeline.py` — its log renderer collapses every stage status to `OK` or `FAIL` and the summary to `PASS` or `FAIL`; both binary collapses admit the third state, and stages 04 and 05's in-process validators live here.
* `tools/evidence/run_sanity_pipeline_gate.py` — `build_release_attestation.py` invokes this wrapper rather than the pipeline directly, and it requires byte equality with a log in which all fifteen stages read `:OK` with `first_failed_stage:NONE` and `summary:PASS`. It is a second, independent pass pin between the stages and the attestation.
* `tools/evidence/build_release_attestation.py` — bounded by the ownership limit below.
* `tools/evidence/run_canonical_json_gate.py` — its `--check-only` result is a direct predicate input to the rails-lane gate through `canonical_gate()` and the `canonical_gate_success` predicate, and it is likewise invoked by the determinism builder. Its existing treatment as a PR04 necessary dependent, validating against the frozen generated hashes, is unchanged and unaffected; this overlay adds only the permission to express the non-admitted outcome in this file where implementation establishes it must live there.
* `.github/workflows/ci.yml` — the rails and release lane steps accept the one explicit outcome under the stated condition.
* `ci/jobs/rails_open_conformance.yml` — the job definition's step and `proves` list match the gate's corrected behavior. The job-definition runner parses this shape natively and needs no change.

Test homes that pin the above and lie outside the work unit's owned test homes, four files:

* `tests/evidence/test_sanity_pipeline.py` — pins the gate wrapper's byte-exact pass log and the rendered status tokens.
* `tests/evidence/test_open_rails_abba_proof.py` — asserts `top_level_pass is True` in its positive matrix.
* `tests/evidence/test_rails_ci_workflow_integration.py` — pins the workflow's rails-lane shape and asserts equality between the exact set of test targets named in the workflow and a fixed set.
* `tests/transport/test_a7_transport_proofs.py` — calls the live A7 build.

Governed evidence affected by the corrected renders is regenerated by its existing owning writers and is never hand-edited. This includes the tracked `audit/gates/sanity_pipeline/sanity_pipeline.log` with its path-proof companion, and the six outputs of the determinism builder: `audit/gates/parity/reader_cli/ab.json`, `audit/gates/parity/reader_cli/ba.json`, `audit/gates/parity/reader_cli/summary.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256` and `artifacts/cards/a3/IDENTITY_OK.txt`. Regeneration through an owning writer is an evidence obligation and extends no loci. The release lane's clean-tree assertions remain in force.

### Binding conditions

The overlay is valid only as bounded by all four of the following.

1. The explicit outcome is never a pass in any surface: never `PASS`, never `top_level_pass: true`, never a frozen-byte substitute presented as a live result.
2. The ordinary-CI acceptance keys on that one explicit outcome and on the observed non-admitted state of the active release. It never keys on a generic failure, a lane name, a job name or a time window, and it never accepts an unrelated failure in those lanes.
3. The acceptance is self-extinguishing by construction, conditioned on a runtime-observable fact. No later removal is owed, no unit receives scope for one, and no cleanup work unit or pull request is created.
4. No change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value is authorized. Any such need is a separate PF12 canon decision for the governed PF12 maintainer and is not pre-authorized.

Beyond these, no legacy success path is retained, the manifest is neither expanded nor activated, admission is neither bypassed, relocated nor weakened, no synthetic or test-only release is fed to a governed gate or to the attestation, no gate is converted to frozen-byte comparison while still emitting a pass, and no test is skipped, disabled or quarantined.

### Ownership limits

PR04's touch on `tools/evidence/build_release_attestation.py` transfers no attestation ownership from HDE-EPIC040-PR06. That touch is bounded to emitting the distinct non-admitted code on the existing failure-receipt path and to the withholding the builder already performs. Authority over the success attestation, the promoted roster, release identity, the manifest cut and the owning attestation validator remains PR06's.

The distinction that bounds this overlay is what a change does to a gate, not where a file sits. Changes that alter gate semantics and what ordinary CI certifies as a passing candidate require this overlay. Changes that alter coherence registration — which lane a path selects — or that validate against an existing frozen capture do not, and remain ordinary necessary dependents of the approved work unit.

### Requirements and acceptance effects

The overlay rewrites no requirement and no acceptance criterion. It makes the existing completion condition satisfiable rather than altering it.

| Requirement or criterion | Effect |
| --- | --- |
| `K040-REQ-012` | The affected gates and the attestation express the actual admission state through their existing owning writers, with no new evidence family and no fabricated passing snapshot. |
| `AC040-08` | Evidence coherence holds across the interval: a non-admitted release yields an explicit non-admitted outcome and a canonical failure receipt, not an ambiguous failure or a false pass. |
| PR04 completion, CI clause | Satisfiable on a truthful candidate. The requirement that all selected lanes pass on the exact candidate head is unchanged; no inherited CI exception applies and none is created. |

All other approved requirement and criterion text, allocation and completion burden are unchanged. The overlay satisfies no later unit in advance.

### Work-unit, dependency and status effects

The dependency order `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01` is unchanged.

HDE-EPIC040-PR05 is covered by this overlay and requires no separate overlay and no new loci. PR05's owned loci classify to the lane union `evidence`, `product` and `release`; the release lane is where sanity stages 04 and 05 run; PR05 owns none of the enumerated files; and PR05 precedes PR06. PR05 inherits the condition through the release lane alone. Because the acceptance keys on the non-admitted state of the active release rather than on a particular candidate, it covers every candidate in the interval and extinguishes for all of them when PR06 lands.

HDE-EPIC040-PR06 owns convergence: complete release admission, the forty-four-member materialization, identity recomputation and promotion. Adding the enumerated files to PR04's loci selects no additional CI lane, because a PR04 candidate already selects full validation and all seven lanes through its change to `ci/checks/classify_ci_changes.py`.

There is no effect on HDE-EPIC040-PR07, OPS01, independent QA, release promotion, PF09 status movement or Epic closure. No Ops task, environment, deployment, vendor or database operation is created or required. No PF-Canon document is edited.

### Preserved exclusions and nonclaims

The overlay creates no public route, public flag, public payload field or transport change; no new evidence family, schema, writer, loader, serializer or calculator; no new persistent infrastructure; and no release promotion, activation or deployment.

It establishes no QA verdict, no acceptance, no PF09 status movement, no Product Owner closeout and no Epic closure. It does not claim that PR04 is implemented, reviewed, merged or complete. Local and CI proof is not live vendor smoke, production readiness, independent QA or approval.

Accepted-final HDE-EPIC040-PR01, PR02 and PR03 remain final and are not rerun, reopened, revised or reaccepted. Proposal v1.0 of this finding and the RS-20 decision v1.0 that returned it are preserved unchanged as decision history.

### Separate boundary recorded and not decided

`adapter/http_reader.py` is simultaneously an approved PR04 locus that PR04 is required to change and one of the fifteen committed members of `catalog/manifest.json`. The release lane's manifest content binding asserts that every committed manifest entry's hash and size equal the repository bytes, and it fails on a PR04-shaped change, while PR04 may not refresh the manifest.

This is the class PF10 §2.10 addressed for HDE-EPIC040-PR02 and `engine/serializer/canon.py`, under an overlay scoped to that work unit alone and reserving complete member refresh and final identity recomputation to PR06. It is independent of release admission and would occur with a fully admitted release, so it lies outside this finding and outside this overlay.

It is recorded as the candidate finding `HDE-EPIC040-PR04-F02` for the PR04 work unit, and is neither decided, scoped nor pre-approved here. It does not gate this overlay, which is complete on its own terms.

### Unresolved items and owners

| Item | Owner | State |
| --- | --- | --- |
| `HDE-EPIC040-PR04-F02` — manifest binding refresh for `adapter/http_reader.py` | Session `PR04-HDE-EPIC040-1`, through its ordinary rescope route | Candidate finding; undecided |
| PR04 plan decision D-03 — the valid self-pair exit-0 carrier | Session `PR04-HDE-EPIC040-1` | Deliberately unbundled; not raised |
| PF12 version currency, repository-resolved v2.9.5 against the register's v2.9.6 | The governed PF12 maintainer | Ordinary maintenance; non-gating |
| Permanent PF14 §6.7 correction carried by `C040-05` | Its governed maintainer | Pending; non-gating |
| Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage carried by `C040-06` | Their governed maintainers | Pending; non-gating |
| PF10 Addendum Index currency — the index lists through `2.13` while the body carries `2.14` | The PF10 drain owner | Observation; non-gating |
| Repository prompt-provenance persistence | The authorized repository writer, once a procedure is installed | `PENDING`; non-gating |

### Canon-conflict continuity

`CANON_CONFLICT_REGISTER` entries `C040-01` through `C040-06` are carried unchanged with their existing classifications, decision lineage, carried effects and remaining owners. No entry is reopened, relabeled, omitted, newly decided or resolved. Neither `HDE-EPIC040-PR04-F01` nor the `HDE-EPIC040-PR04-F02` candidate is a register entry.

### Resulting state

`HDE-EPIC040-PR04-F01` is an approved bounded implementation rescope. The approved delta returns to the PR-20 planning stage in the dedicated PR04 session, which issues PR04 detailed Implementation Plan v1.1 as a complete successor carrying this overlay, in state `AWAITING_PO_PROCEED`.

No `PR_RETURN_PHASE` applies: the finding arose before any Proceed, workspace, worktree, branch, commit, open pull request or CI run, and RS-40 is ineligible. PR04 implementation awaits the Product Owner's separate exact `PR-30` invocation, which this overlay does not supply.
