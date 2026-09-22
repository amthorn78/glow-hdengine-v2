---
artifact_type: REDLINE_APPLICATION_REPORT
artifact_id: HDE-EPIC040-PR04-F01-RS30-REDLINE-APPLICATION-REPORT
artifact_version: "1.0"
artifact_state: COMPLETE
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
revised_artifact: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md
base_artifact: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md
correction_authority: RS-20 REVISION_REQUIRED, Isis-50, 2026-09-22T06:48:06Z
capture_time_utc: 2026-09-22T07:02:23Z
---

# HDE-EPIC040-PR04-F01 — RS-30 Redline Application Report v1.0

## 1. Scope and authority

| Field | Value |
| --- | --- |
| Correction authority | **RS-20 `REVISION_REQUIRED`**, Isis-50, `2026-09-22T06:48:06Z`, recorded in `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md`. **Not** a Product Owner correction, so the route returns to RS-20 and not terminally to Nathan. |
| Base artifact | `RESCOPE_PROPOSAL` v1.0, `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md`, SHA-256 `51eae27c2013722a3aebf22ca073587ad4d83c105176df87e970c37bc9f46bf6` — recomputed at this authoring and matched. Preserved unchanged at its path. |
| Revised artifact | `RESCOPE_PROPOSAL` v1.1, `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md`, state `RESCOPE_PROPOSAL_PENDING_REVIEW`, ending `ASK OK?` |
| Artifact type | `RESCOPE_PROPOSAL` in both versions. No type conversion occurred; the public state is a compatibility state, not a type change. |
| Author | The same RS-10 proposal author: the retained whole-change HDE-EPIC040 Implementation Architect session. `session_disposition: RETAIN_EXISTING`. |
| Decision owner | Isis-50, unchanged. This report decides nothing and creates no addendum. |
| Repository baseline | `main` head `332fa4c6b2c1ea65a52bee4fd40c227d2d49f4fc`, tree `27f5a8a3986d8de3ac0d72c4973630485a126709`, clean tree. `git diff 6ecacafb..main -- . ':(exclude)docs/'` empty. |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, SHA-256 `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f`, recomputed and matched. Recorded as provenance only. |

Every redline item below is applied **exactly once**. No item is silently omitted and no resolution is fabricated.

## 2. Redline application map

| Item | Required change | Disposition | Resulting anchors in v1.1 | Evidence carried |
| --- | --- | --- | --- | --- |
| **R-1** *(blocking)* | Add `tools/evidence/run_sanity_pipeline_gate.py` to §4.4, §6.2, §6.3 candidate D and §10; correct §4.4's closing sentence and the §6.3 cost cell to the corrected count | **APPLIED** | §6.2 row 5 (with its own justification); §4.3 row 2 names the wrapper in the release chain; §4.4 closing sentence gives the corrected enumeration; §6.4 candidate D cost cell gives the corrected count; §10 E-15 and E-16 | `build_release_attestation.py:669` invokes the wrapper; `_expected_log()` / `_valid_log()` require byte equality with an all-`:OK`, `first_failed_stage:NONE`, `summary:PASS` log; `run_sanity_pipeline.py:222` and `:282` collapse to two tokens each; `build_release_attestation.py:757–766` independently requires the same tail. All re-read at this head. |
| **R-2** *(blocking)* | State the derivation **method** and its stopping condition — a reproducible trace of every `PASS` pin reachable from the rails lane and from the release lane through `build_release_attestation.py` | **APPLIED** | New §6.3 "Derivation method and stopping condition": a three-clause definition of a `PASS` pin, a five-step procedure, an explicit stopping condition, an eleven-row exclusion table with reasons, and a stated honest limit | Seeded from the verbatim lane commands at `.github/workflows/ci.yml:164–174` and `:228–270` plus `_FULL_VALIDATION_SUPPLEMENTAL_TESTS`; expanded through `default_steps()`' fifteen stages and each job definition; exclusions X-1 … X-11 each carry their reason, including the executed X-5 (`release_id_recompute.py --check-manifest-only`, exit 0) |
| **R-3** | `pipeline_stop` is `{"type": "null"}`, not `const null`; `validation_result` and `release_admission` are `const` | **APPLIED** | §6.1 second bullet, flagged explicitly as a correction to v1.0; §10 E-13 rewritten | `schemas/hde_release_attestation.v1.json` re-read: `pipeline_stop => {"type": "null"}` |
| **R-4** | Replace the assertion that PR05 inherits the condition with its proof | **APPLIED** | §7 "Dependencies" row carries the five-step proof; §11 R-03 marked answered | RS-20 review §7, carried with its classifier execution: PR05's Plan §6.5 loci yield the lane union `{evidence, product, release}`; the release lane is where stages 04 and 05 run; PR05 owns none of the affected files; PR05 precedes PR06 under PF10 §2.13 |
| **R-5** | Record that widening PR04's loci selects no additional CI lane | **APPLIED** | §6.4 candidate D cost cell; §10 E-23 | `ci/checks/classify_ci_changes.py` is a member of `_FULL_VALIDATION_PATHS`; PR04 plan §6.5 already changes it, so the candidate already runs full validation and all seven lanes. RS-20 executed the classifier and observed every lane `True` with `reason='selected_lanes'`; that execution is attributed to RS-20, not re-claimed as this author's |
| **R-6** | Qualify "every truthful treatment lies outside the approved loci"; state the distinguishing criterion | **APPLIED** | §5 second bullet, with a three-row comparison table and an explicit boundary case | PR04 plan §§6.2 and 6.5 already change `ci/checks/classify_ci_changes.py`, `tools/evidence/run_canonical_json_gate.py` and `tools/cli/generate_showcompat_artifacts.py` as necessary dependents without a rescope. Criterion stated as **gate semantics and acceptance** versus **coherence registration and frozen-byte validation**, with `run_canonical_json_gate.py` named as the boundary case and cross-referenced at §6.3 X-8 |
| **R-7** | State that PR04's touch on `build_release_attestation.py` transfers no attestation ownership from PR06 | **APPLIED** | §6.2 "Ownership bound on file 6"; §7 "Downstream" row | Plan §4.2 maps complete release and external attestation to `cut_release_manifest.py`, `release_id_recompute.py` and `build_release_attestation.py`; Plan §6.6 gives PR06 the owning attestation validator only where contract gaps are evidenced. PR04's touch is bounded to the non-admitted code on the existing failure-receipt path and the withholding it already performs |

## 3. Conditions carried forward unchanged

RS-20 confirmed four conditions as correct and closed to revision. All four are carried verbatim in substance at v1.1 §6.2, and none was altered, softened or re-argued:

1. The explicit outcome is never `PASS`, never `top_level_pass: true`, and never a frozen-byte substitute presented as a live result; frozen captures stay frozen with their nonclaims.
2. The ordinary-CI acceptance keys on that one explicit outcome only and on the observed non-admitted state of the active release — never on a generic failure, a lane name or a time window.
3. The acceptance is self-extinguishing by construction; no later removal is owed and no cleanup pull request is required.
4. No change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value is authorized; any such need is a separate PF12 canon decision, not pre-authorized.

Also carried forward as settled, per review §§3 and 5, and **not** re-derived: the classification as a bounded implementation rescope, and candidate **D** as the disposition. A, B and C appear at v1.1 §6.4 for completeness only.

## 4. Findings produced by the R-2 trace, beyond the redline

The trace R-2 required was not a formality. Applying the method in v1.1 §6.3 surfaced material the redline did not ask for and the review did not have. It is reported here rather than folded silently into the file list.

| # | Finding | Why it matters |
| --- | --- | --- |
| 1 | **`tools/evidence/generate_determinism_gate_proofs.py` is a further omitted production file.** Sanity stage 04's `validate_current_reader_cli_determinism` calls its `build()`, which calls `emit_reader_public_envelope` (`:25`) and runs an `hdctl` subprocess (`:28`) — a live Reader **and** CLI success path — and writes the parity and determinism governed artifacts. | Neither v1.0's six nor R-1's seventh named it. The corrected production set is **eight**. |
| 2 | **Four test homes pin the affected behavior and lie outside instruction §7.1 and §7.2**: `tests/evidence/test_sanity_pipeline.py` (`:172` pins the wrapper's byte-exact PASS log), `tests/evidence/test_open_rails_abba_proof.py` (`:160` asserts `top_level_pass is True`), `tests/evidence/test_rails_ci_workflow_integration.py` (`:153–157` asserts equality between the exact set of `tests/...` targets in `ci.yml` and a fixed set), and `tests/transport/test_a7_transport_proofs.py` (calls the live A7 build). | A file set naming only production files would block again at implementation the moment the pinning tests ran. |
| 3 | **The tracked sanity log is a clean-tree pin.** `audit/gates/sanity_pipeline/sanity_pipeline.log` is committed, ends `first_failed_stage:NONE` / `summary:PASS`, and has a `.path_proof.txt` sibling; the release lane asserts `git diff --exit-code` and a clean tree. | Named as a regeneration obligation through the existing owning writer under Plan §7.2 — **not** a loci widening, and never hand-edited. |
| 4 | **One judgement inside the set, stated rather than buried.** File 3 is reached only through the pipeline, so the non-admitted discrimination could be made at the stage-04 caller instead. It is named anyway, because an unnamed file would force a second rescope for the same finding. | v1.1 §6.2.1 states the reasoning and contrasts it with file 1, where no such choice exists. |
| 5 | **Two exclusions a reasonable implementer could overturn**, named so the reviewer can admit either pre-emptively: X-8 (`run_canonical_json_gate.py`, already a plan dependent but genuinely affected) and X-10 (`tests/evidence/test_release_attestation.py`, whose receipt-shape tests this delta does not change). | Recorded as unresolved fact U-07 and flagged at v1.1 §14. |

## 5. What was preserved

- **Proposal v1.0** is unmodified at its own path; v1.1 is a complete successor, not an overwrite.
- **Unaffected content** carried forward: the identity and authority boundary, the approved-base and overlay lineage, the proven boundary and its executed evidence, the closed set of in-scope treatments, the canon narrowing, the three binding conditions, the effects table's unchanged rows, the preserved-work section, the originating stage and lawful return point, the risks and exclusions, the carried `CANON_CONFLICT_REGISTER` and the prompt-use lineage.
- **Approved-base references** unchanged: Specification v1.1, Audit v2.0, Plan v2.1, Plan Review v2.1, and every active PF10 overlay.
- **Vehicle state** unchanged and truthfully not yet produced: no Proceed, workspace, worktree, branch, open PR, commit or CI run; no `PR_RETURN_PHASE` asserted; RS-40 ineligible and not invoked.
- **Completed valid work** unchanged: PR04 plan §§5–8, §9 checkpoints C1–C3, §§10–12.
- **Register** unchanged: C040-01 … C040-06 carried with no entry reopened, relabeled, omitted or newly decided. `HDE-EPIC040-PR04-F01` is not a register entry.
- **Unresolved facts** updated truthfully: U-01 and U-03 resolved with their evidence; U-02, U-04, U-05 and U-06 carried; U-07 added by the R-2 trace.

## 6. What this report does not do

It decides nothing, approves nothing, and drafts, numbers or implies no PF10 addendum. It requests no Proceed, creates no branch or pull request for PR04, implements nothing, changes no immutable base, reruns no accepted-final work, and neither invokes nor routes to PR-50. `docs/pfcanon/` was read only.

## 7. Return

The revised proposal returns to **Isis-50**, the same RS-20 reviewer session, at `RS-20 — Review Bounded Work-Unit Rescope — 091426.1`, for a second decision on v1.1. The expected result is a `RESCOPE_REVIEW`.
