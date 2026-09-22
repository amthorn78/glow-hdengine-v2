---
artifact_type: RESCOPE_PROPOSAL
artifact_id: HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL
artifact_version: "1.1"
artifact_state: RESCOPE_PROPOSAL_PENDING_REVIEW
predecessor_version: "1.0"
predecessor_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md
correction_authority: RS-20 REVISION_REQUIRED, Isis-50, 2026-09-22T06:48:06Z
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-22T07:02:23Z
next_stage: RS-20
---

# HDE-EPIC040-PR04-F01 — Bounded Work-Unit Rescope Proposal v1.1

## 1. Identity, status and authority boundary

| Field | Value |
| --- | --- |
| Artifact type | `RESCOPE_PROPOSAL` — unchanged; this is a revision, not a type conversion |
| Logical ID | `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL` |
| Version | `1.1` — complete successor to v1.0, which is preserved unchanged at its path |
| Status | `RESCOPE_PROPOSAL_PENDING_REVIEW` |
| Correction authority | RS-20 `REVISION_REQUIRED`, Isis-50, `2026-09-22T06:48:06Z`, against this proposal at v1.0. Not a Product Owner correction. |
| Decision owner | Isis-50, the continuing independent Lead Developer reviewer; unchanged |
| `CHANGE_CLASS` / `CHANGE_ID` | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| `WORK_UNIT_ID` | `HDE-EPIC040-PR04` — Bounded application, identity and consumer integration |
| `FINDING_REF` | `HDE-EPIC040-PR04-F01` |
| Author / role | The same RS-10 proposal author: the retained whole-change HDE-EPIC040 Implementation Architect; no approval authority |
| `session_disposition` | `RETAIN_EXISTING` |
| `role_session_ref` | That same retained whole-change HDE-EPIC040 IA session; the dedicated PR-development session `PR04-HDE-EPIC040-1` is retained separately and is not replaced or addressed |
| `invocation_binding` | `HDE-EPIC040 / HDE-EPIC040-PR04 / RS-30` (`GCF-17.RESCOPE`) |
| `context_conflict` | `NONE` established |
| `AUTHORING_CONTEXT` | `APPROVED_BASE_WITH_OVERLAYS` |
| Capture time | `2026-09-22T07:02:23Z` |
| Output class / path | `REPOSITORY_CONTROLLED` / `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md` |

This proposal is evidence for a second RS-20 decision. It is not an approval, not a PF10 addendum, not implementation authority, not a Proceed, not a Specification change and not a merge instruction. RS-30 produces no addendum and decides nothing.

**What this revision changes.** Redlines R-1 through R-7 from RS-20's `RESCOPE_REVIEW` v1.0 §6, applied exactly once each. The per-item mapping is in the companion `docs/ephemeral/HDE-EPIC040-PR04-F01-rs30-redline-application-report-v1.0.md`. The settled classification (§5) and candidate D (§6.4) are carried forward as decided and are **not** re-derived or re-argued.

**What R-2 produced, beyond the redline.** The exhaustive trace RS-20 required (§6.3) found **one further omitted production file that neither v1.0 nor the review named — `tools/evidence/generate_determinism_gate_proofs.py` — and four test homes that pin the affected behavior and lie outside the instruction's owned test homes.** The corrected enumeration in §6.2 is therefore larger than the seven files R-1 called for. That is the point of deriving it exhaustively rather than by inspection, and it is stated plainly rather than folded in silently.

## 2. Applicable approved bases and overlay lineage

Bases applicable to the actual originating stage (PR-20 planning for PR04). All repository paths are in `amthorn78/glow-hdengine-v2`, branch `main`.

| Role | Artifact type / approval lineage | Repository path and SHA-256 |
| --- | --- | --- |
| `SPECIFICATION_ID` | `SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`; Thoth-17 `APPROVE` 2026-09-08T13:23:24Z | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`; recomputed `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` — matches RS-20's independent recomputation; U-03 is closed |
| `IMPLEMENTATION_AUDIT_ID` | `IMPLEMENTATION_AUDIT` v2.0, `AUDIT_COMPLETE` | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` |
| `IMPLEMENTATION_PLAN_ID` | `IMPLEMENTATION_PLAN` v2.1, immutable approved base | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`; `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| `PLAN_REVIEW_ID` | `IMPLEMENTATION_PLAN_REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z; redline `R040-IA30-02` | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| `PR_INSTRUCTION_ID` | `PR_INSTRUCTION` v1.0, `INSTRUCTION_READY` | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md`; `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf` |
| `PR_IMPLEMENTATION_PLAN` | `PR_IMPLEMENTATION_PLAN` v1.0, `DRAFT`, carrying F01 at its §14.1 | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md`; `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65` |
| Predecessor proposal | `RESCOPE_PROPOSAL` v1.0, superseded by this successor and preserved unchanged | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md`; recomputed `51eae27c2013722a3aebf22ca073587ad4d83c105176df87e970c37bc9f46bf6` — matches |
| Correction decision | `RESCOPE_REVIEW` v1.0, `REVISION_REQUIRED`, Isis-50, 2026-09-22T06:48:06Z; no addendum created | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` |
| Accepted dependencies | PR01 `ACCEPT` (#403); PR02 `ACCEPT` (#404); PR03 `ACCEPTED_FINAL` (#405, merged `9cda1b49a972da874021e8820997fab1ebaff153`) | `docs/ephemeral/HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md`, `…PR02-…-v1.0.md`, `…PR03-…-v1.0.md` |

**Current controlled PF10**, resolved and completely read from `docs/pfcanon/` at this authoring: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, recomputed SHA-256 `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f` — matches. Recorded as provenance of what was read; it gates nothing downstream.

**Applicable active addendum overlays**, by repository path, unchanged from v1.0 §2: §2.2 (PF10 body only); §2.3 `docs/ephemeral/HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md`; §2.4 `docs/ephemeral/HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md`; §2.5 `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md`; §2.6 `docs/ephemeral/PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md`; §2.7 `docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md` and `…-v2.0.md`; §2.8 PF10-FORM-001 (the page-ready canonical form governing any addendum RS-20 may emit; RS-30 emits none); §2.9 `docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md`; §2.10 `docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md`; §2.11 (PF10 body; review body `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md`); §2.12 `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md`; §2.13 `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md`. PF10 §2.14 exists in the body and is not applicable.

Load-bearing: **§2.12** places the executing-mechanics admission boundary in `engine/config/registry_loader.py`; **§2.13** fixes the order `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01` and independently records that the actual repository release remains the incomplete 15-member manifest with PR06 alone owning the 44-member materialization.

## 3. Repository baseline, re-verified

- Current `main` head at this authoring: **`332fa4c6b2c1ea65a52bee4fd40c227d2d49f4fc`**, tree `27f5a8a3986d8de3ac0d72c4973630485a126709`, committed 2026-09-22T07:58:55+01:00. Working tree clean.
- `git diff 6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612..main -- . ':(exclude)docs/'` is still **empty**. Every commit since the PR04 plan's verification point is documentation-only, so that verification and RS-20's remain exactly valid.
- Executable baseline is still precisely the accepted PR03 state `9cda1b49a972da874021e8820997fab1ebaff153`.
- No PR04 product branch, commit, pull request, Proceed, implementation result, review, CI result or merge exists. Nothing is fabricated here.
- PRs #452, #453, #457 and #462 have merged, so the instruction, the PR04 plan, proposal v1.0 and the RS-20 review are all on `main`.

## 4. Suspended boundary — proven

### 4.1 The approved obligation

PR04's approved completion condition (Plan §6.4, instruction §4, plan §4.2 condition 4) requires its integration paths and proofs to pass actual code review, security review **and CI**, with instruction §12 stating that no inherited CI exception or prior green run applies to this unit.

PR04's approved behavior requires removing every legacy success path — `compat_public` hash scoring, the `ts_v0` band and UID-only substitutes (instruction §10) — and consuming only the admitted mechanics bundle through the PF10 §2.12 admission owner, with instruction §10 stating that if a valid admitted release is unavailable, canonical integrated success refuses and there is no legacy fallback.

### 4.2 Executed evidence, at current head `332fa4c`

Both observations were re-run at this head with `LC_ALL=C LANG=C TZ=UTC`, a clean working tree, and produced no repository mutation.

**E-01 — the admission owner refuses today.** Under closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0`):

```
python -c "from engine.config.registry_loader import load_active_mechanics_bundle; load_active_mechanics_bundle()"
→ SchemaValidationError INCOMPLETE_RELEASE_ROSTER
  "release manifest does not yet contain the complete adopted roster"
```

`catalog/manifest.json` carries **15** entries in `files`; `ADMITTED_RELEASE_ROSTER` (`engine/config/registry_loader.py:400`) is pinned to **44** by the import-time invariant at line 447, and `_validate_admitted_manifest` (lines 1218–1226) raises `INCOMPLETE_RELEASE_ROSTER` on any strict subset. Complete admission is PR06's owned work (Plan §6.6), corroborated independently by PF10 §2.13.

**E-02 — a selected ordinary-CI gate is green today, and only because of the legacy path PR04 must delete.** Under the rails the job definition itself declares (`ci/jobs/rails_open_conformance.yml`: `SAFE_MODE=0 ALLOW_NETWORK=1`):

```
python tools/evidence/generate_open_rails_abba_proof.py --check-current
→ exit 0
  {"path":"audit/gates/determinism/open_rails_abba.json","result":"pass",
   "status":"OK","top_level_pass":true}
```

Its predicate map is all-true, including `abba_byte_identity`, `reader_cli_ab_identity` and `reader_cli_ba_identity`, which compare in-process Reader bytes against the bytes of a real `scripts/hdctl.py showcompat --dump-reader` **subprocess** (`generate_open_rails_abba_proof.py:421–422`, predicates at 490–492, `top_level_pass` at 521, `validate_current_fixture` at 543–547). The gate is green because `engine/runtime/public.py:29–32` still derives the band from `ts_v0`, bypassing the admission owner entirely. PR04 deletes exactly that path.

The finding is the collision: **E-02's gate requires live success on paths that, after PR04's approved change, must route through E-01's refusal.** RS-20 independently reproduced this by execution (review §2.3, observations V-05 through V-08) rather than by inference.

### 4.3 The three selected gate chains

| # | Gate | Chain, verified by reading the cited code | Why PR04 cannot satisfy it |
| --- | --- | --- | --- |
| 1 | Rails lane | `.github/workflows/ci.yml:164–172` → `ci/jobs/rails_open_conformance.yml:18` → `generate_open_rails_abba_proof.py --check-current`; the same lane also runs `pytest tests/evidence/test_rails_ci_workflow_integration.py` | Needs in-process **and subprocess** CLI success. A subprocess cannot receive a test-only bundle, and instruction §6.4 forbids a test-only bundle in a governed gate. |
| 2 | Release lane | `.github/workflows/ci.yml:228, 259` → `build_release_attestation.py --require-clean` → **`run_sanity_pipeline_gate.py`** (`build_release_attestation.py:669`) → `run_sanity_pipeline.py` stage 04 (`validate_current_reader_cli_determinism`, calling `generate_determinism_gate_proofs.build()` and `generate_open_rails_abba_proof.build_fixture_proof()`) and stage 05 (`validate_current_a7_transport`, calling `generate_a7_transport_proofs.build()`) → `AttestationBuildError("final_sanity_pass_missing")` at `build_release_attestation.py:766` | Same live success requirement, reached through two further byte-exact `PASS` pins (§4.4). The lane is selected for **every** PR04 code path: `_lanes_for_path` assigns `{"product","release"}` to any path under `_PRODUCT_PREFIXES`, which includes `engine/`, `adapter/`, `presenter/`. |
| 3 | Full-validation roster | `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` in `ci/checks/classify_ci_changes.py:40`; `tests/transport/test_a7_transport_proofs.py` calls the live A7 build; `tests/http/test_reader_a7_transport.py` asserts `GET /reader` 200 and `POST /reader` 405 | Convertible inside pytest, but only by changing `generate_a7_transport_proofs.py`, whose `capture()` hard-requires `post.status_code == 405` (line 75) and whose live `build()` **is** release-sanity stage 05. Item 3 cannot be separated from item 2. PR04's approved §6.5 implements Reader POST success, contradicting the pinned 405. |

### 4.4 Why no treatment inside PR04's approved loci is both truthful and permitted

| Treatment available inside instruction §7.1 | Why it fails |
| --- | --- |
| Retain any legacy success path | Prohibited by instruction §10 |
| Expand or activate the manifest | Excluded by instruction §9; PR06-owned; PF10 §2.13 fixes the order |
| Bypass, relocate or weaken admission | Prohibited by PF10 §2.12 |
| Feed a synthetic or test-only release into a governed gate or the attestation | Prohibited by instruction §6.4; a `PR06R_B_FINAL_PASS` produced that way is a fabricated passing result |
| Convert the gates to frozen-byte comparison while still emitting PASS | Weakens a release gate; instruction §6.6 forbids weakening a refusal to preserve an old fixture |
| Skip, disable or quarantine the gates or tests | Prohibited by `AGENTS.md` |

Every **truthful** treatment instead touches files outside instruction §7.1 and §7.2. **Corrected enumeration (R-1, extended by the R-2 trace): eight production and CI-configuration files and four test homes, listed with their individual justification in §6.2, derived by the method in §6.3.** v1.0 named six; RS-20 proved a seventh, `tools/evidence/run_sanity_pipeline_gate.py`, and the exhaustive trace adds an eighth production file, `tools/evidence/generate_determinism_gate_proofs.py`, plus the four test homes that pin the affected behavior.

## 5. Classification — settled, carried forward

**`HDE-EPIC040-PR04-F01` is a bounded implementation rescope.** Decided by RS-20 (review §3): not `IN_SCOPE_REPAIR`, not `SPECIFICATION_CHANGE_REQUIRED`, and not a defect in PR01–PR03. Carried forward here as decided and not reopened.

- **Not an in-scope correction.** Every truthful treatment lies outside the loci the PR04 engineering owner is authorized to change, so that owner cannot make any of them under unchanged authority. §4.4 enumerates the closed set of in-scope treatments and why each fails.

  **Qualification, as required by redline R-6.** "Outside the approved loci" does not by itself demand a rescope, and this proposal does not claim it does. PR04's plan §§6.2 and 6.5 already change several paths outside instruction §7.1 as *necessary dependents* without one — among them `ci/checks/classify_ci_changes.py`, `tools/evidence/run_canonical_json_gate.py` and `tools/cli/generate_showcompat_artifacts.py`. The distinguishing criterion this overlay rests on is **what the change does to a gate, not where the file sits**:

  | | Plan's necessary dependents | This overlay's files |
  | --- | --- | --- |
  | What changes | Coherence registration and frozen-byte validation — which lane a path selects, which frozen capture a validator compares against | **Gate semantics and acceptance** — what outcome a gate may emit, and what ordinary CI treats as a passing candidate |
  | Effect on the acceptance bar | None. The gate still demands exactly what it demanded before. | The gate gains a third outcome and CI accepts it under a stated condition. |
  | Who may authorize it | The PR author, as an unavoidable consequence of an already-approved change | A rescope reviewer, because it alters what CI certifies |

  That line is what bounds the precedent in risk R-01, and it is drawn explicitly here so the reviewer can test it rather than infer it. One file sits on the boundary and is called out in §6.2: `run_canonical_json_gate.py` is already a plan dependent for coherence reasons, and nothing in this overlay changes that treatment.

- **Not a Specification change.** No product intent, required behavior, exclusion or acceptance criterion moves. Specification v1.1 and Plan v2.1 §§5.7, 5.8, 6.4 are satisfied exactly as written; §8's requirement-to-unit mapping is unchanged in substance. What is missing is only a truthful way for the affected gates to express a state the approved plan itself creates — the interval between PR04's consumer switch and PR06's release admission — which is a consequence of the approved dependency order, not a departure from it.

- **Not a defect in PR01–PR03.** PR03 passed these gates lawfully because its consumers still used `ts_v0` (E-02). No accepted-final work is reopened or rerun.

## 6. The corrected bounded delta

### 6.1 The canon narrowing — confirmed, with one correction

v1.0 recorded that the truthful interim state is already expressible in current canon, so no PF12 decision is expected. RS-20 confirmed the narrowing. Restated with redline R-3 applied:

- `schemas/hde_release_attestation.v1.json` pins `validation_result` as `{"const": "PASS"}` and `release_admission` as `{"const": "PR06R_B_FINAL_PASS"}`. The success attestation is by construction emitted only on a complete pass, so **withholding it requires no schema change** — the builder already refuses.
- **Correction (R-3):** the same schema pins `pipeline_stop` as **`{"type": "null"}`**, not `const null`. v1.0 and its §10 E-13 said `const`. The distinction does not affect the narrowing — a type-pinned null is equally unable to carry a non-admitted state — but the statement was inaccurate and is corrected here and at §10 E-13.
- A **failure receipt contract already exists in canon**: `schemas/hde_release_attestation_failure.v1.json`, required fields `schema`, `code`, `stage`, `returncode`, `secret_values_recorded`. `build_release_attestation.py::_write_failure` (lines 498–507) already writes a canonical `failure.json` under `hde.release_attestation.failure.v1` on every `AttestationBuildError`, including today's `final_sanity_pass_missing`.
- That schema's `code` and `stage` are **open lowercase-token strings** (`"pattern": "^[a-z0-9_]+$"`), not enums. A distinct, truthful code such as `release_not_admitted` is therefore already expressible **with no PF12 schema or wire-value change**.

### 6.2 The enumerated file set, with per-file justification

Extend PR04's approved loci to exactly the files below, for one purpose only: to make the affected gates express a truthful, explicit non-admitted outcome instead of an ambiguous failure, and to let ordinary CI accept that one specific outcome until PR06 lands.

**Production and CI configuration — eight files.**

| # | File | Why it must change | Source of the requirement |
| --- | --- | --- | --- |
| 1 | `tools/evidence/generate_open_rails_abba_proof.py` | Reached twice: standalone by the rails lane (`--check-current`) and inside sanity stages 04 and 06. Because the rails lane invokes it directly, the non-admitted discrimination must live in this file; a caller cannot supply it. | v1.0; confirmed |
| 2 | `tools/evidence/generate_a7_transport_proofs.py` | `capture()` hard-requires `POST /reader` → 405 (line 75) and `GET /reader` → 200; its live `build()` is sanity stage 05 and is also called by `tests/transport/test_a7_transport_proofs.py`. | v1.0; confirmed |
| 3 | **`tools/evidence/generate_determinism_gate_proofs.py`** | **Newly identified by the §6.3 trace; named by neither v1.0 nor the review.** Stage 04's `validate_current_reader_cli_determinism` calls its `build()`, which calls `emit_reader_public_envelope` (line 25) and runs an `hdctl` subprocess (line 28) — a live Reader **and** CLI success path — and writes `audit/gates/parity/reader_cli/{ab,ba,summary}.json`, `audit/gates/determinism/abba.bytes` and `tworun_identity.sha256`. See §6.2.1 for why it is named rather than left to its caller. | R-2 trace |
| 4 | `tools/evidence/run_sanity_pipeline.py` | `_render_log` (`:222`) collapses every stage status to exactly `"OK"` or `"FAIL"`, and `:282` collapses the summary to `"PASS"` or `"FAIL"`. **No third token exists today.** Both binary collapses must admit a third state, and stage 04/05's in-process validators (`validate_current_reader_cli_determinism`, `validate_current_a7_transport`) live in this file. | R-1 chain; confirmed by reading |
| 5 | **`tools/evidence/run_sanity_pipeline_gate.py`** | **Added by redline R-1.** `build_release_attestation.py:669` invokes this wrapper, not the pipeline directly. `_expected_log()` builds a byte-exact log in which all fifteen stages read `:OK` with `first_failed_stage:NONE` and `summary:PASS`, and `_valid_log()` requires `data == _expected_log()` — byte equality. It is a second, independent `PASS` pin between the stages and the attestation, so a third state cannot reach the failure receipt without it. | RS-20 review §4.1 |
| 6 | `tools/evidence/build_release_attestation.py` | Fails closed at line 766 (`final_sanity_pass_missing`) and independently requires the log tail `check 15 Final-LF validation:OK\nfirst_failed_stage:NONE\nsummary:PASS\n` (lines 757–766). It must emit its existing canonical failure receipt with a distinct code instead of an ambiguous one. **Bounded strictly per R-7 — see below.** | v1.0; confirmed |
| 7 | `.github/workflows/ci.yml` | The rails and release lane steps must accept the one explicit outcome under the stated condition. | v1.0; confirmed |
| 8 | `ci/jobs/rails_open_conformance.yml` | The rails job definition's step and `proves` list must match the gate's corrected behavior. `ci/checks/run_rails_job_definitions.py` parses this shape natively, so the runner itself needs no change (§6.3, exclusion X-4). | v1.0; confirmed |

**Test homes that pin the above and lie outside instruction §7.1 and §7.2 — four files.**

| # | File | The pin it holds |
| --- | --- | --- |
| 9 | `tests/evidence/test_sanity_pipeline.py` | `test_sanity_gate_accepts_only_exact_generic_final_pass_log` (`:172`) asserts the wrapper accepts only the byte-exact all-`:OK`, `summary:PASS` log; `:48` and `:166` pin the rendered tokens. |
| 10 | `tests/evidence/test_open_rails_abba_proof.py` | `test_fixture_backed_open_rails_abba_positive_matrix` (`:160`) asserts `top_level_pass is True`; the negative matrix at `:182` pins the baseline the same way. |
| 11 | `tests/evidence/test_rails_ci_workflow_integration.py` | Pins `.github/workflows/ci.yml` content directly, including the rails-lane shape (`:39`) and — at `:153–157` — an equality assertion that the **exact set** of `tests/...` targets named anywhere in the workflow equals a fixed set. Any workflow edit that adds or renames a test target trips it. |
| 12 | `tests/transport/test_a7_transport_proofs.py` | Calls the live A7 `build()` in six tests. Unlike `tests/http/test_reader_a7_transport.py`, which is an existing HTTP/Reader home already owned under instruction §7.2, this one is not in an owned home. |

**Governed evidence regenerated through its owning writer — not a loci widening.** `run_sanity_pipeline.py` writes the tracked `audit/gates/sanity_pipeline/sanity_pipeline.log`, whose committed bytes today end `first_failed_stage:NONE` / `summary:PASS`, with a `.path_proof.txt` sibling. The release lane runs `git diff --exit-code` and a clean-tree assertion, so a changed render leaves a dirty tree unless the artifact is regenerated. The same applies to the parity and determinism artifacts written by file 3. These are regenerated **by their existing owning writers** under Plan §7.2 and `AGENTS.md`, never hand-edited, and they extend no loci.

**The three binding conditions, carried forward unchanged.** RS-20 confirmed these as correct and not open for revision:

1. The explicit outcome is **never** `PASS`, never `top_level_pass: true`, and never a frozen-byte substitute presented as a live result. Frozen captures stay frozen with their existing nonclaims.
2. The ordinary-CI acceptance keys on **that one explicit outcome only**, and on the observed non-admitted state of the active release — never on a generic failure, a lane name or a time window. This is risk R-02's mitigation and it is binding.
3. Because the acceptance is conditioned on a runtime-observable fact rather than a hardcoded window, it is **self-extinguishing by construction**: once PR06 admits the complete 44-member roster the branch is never taken, and its continued presence is truthful and inert. No later removal is owed, no unit is allocated scope for one, and no cleanup pull request is required. Removal is optional hygiene only.
4. No change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value is authorized. §6.1 establishes that none is expected. If implementation nonetheless requires one, that portion is a **separate PF12 canon decision** routed to the governed PF12 maintainer as a new finding, and is not pre-authorized by any disposition of this proposal.

**Ownership bound on file 6 (redline R-7).** PR04's touch on `tools/evidence/build_release_attestation.py` **transfers no attestation ownership from PR06.** Plan §4.2 maps complete release and external attestation to `scripts/cut_release_manifest.py`, `scripts/release_id_recompute.py` and `build_release_attestation.py`, and Plan §6.6 gives PR06 the owning attestation validator only where current contract gaps are evidenced. PR04's permitted touch is bounded to exactly two things: emitting the distinct non-admitted code on the existing failure-receipt path, and withholding the success attestation it already withholds. PR04 acquires no authority over the success attestation, the promoted roster, release identity, the manifest cut, or the attestation validator, and it may not change the success schema or wire value (condition 4 above). Every other aspect of attestation behavior remains PR06's.

### 6.2.1 The one judgement inside the set

File 3, `generate_determinism_gate_proofs.py`, is reached **only** through sanity stage 04, whose validator lives in `run_sanity_pipeline.py` (file 4). It is therefore technically possible to detect the non-admitted state at the caller — checking admission before invoking `build()` — and leave file 3 untouched. It is named in the set anyway, for two reasons: the caller-side check would have to duplicate admission logic that the builder's own failure already carries, and if implementation finds the builder is the honest place for the discrimination, an unnamed file would force a **second** rescope for the same finding — the precise outcome RS-20's `REVISION_REQUIRED` exists to prevent. Naming it costs nothing: it selects no additional CI lane (§6.4) and the overlay's purpose clause bounds what may be done to it as tightly as to every other file. Contrast file 1, where no such choice exists — the rails lane invokes it directly, so the discrimination must live in the file itself.

### 6.3 Derivation method and stopping condition (redline R-2)

RS-20 required the enumeration to be a testable claim rather than an inspection result. The method below is stated so the reviewer can re-run it.

**Definition.** A file is a **`PASS` pin** for this finding when all three hold: (a) it is reachable from the rails lane or from the release lane through `build_release_attestation.py` on a PR04 candidate; (b) when the active release is not admitted, it requires a positive `OK`/`PASS`/`True`-shaped value that a truthful non-admitted outcome cannot supply; and (c) that requirement cannot be satisfied truthfully without editing that file. A file failing any of the three is excluded, with its reason recorded.

**Procedure.**
1. **Seed.** Take the exact commands of the two lanes verbatim from `.github/workflows/ci.yml` — the rails lane at `:164–174` and the release lane at `:228–270` — plus the full-validation roster from `ci/checks/classify_ci_changes.py`, since PR04's candidate selects it.
2. **Expand.** For each command, read the module it runs and follow every call that can fail closed, recording each equality, predicate, `const` or byte-exact assertion on the path. Job-definition files expand to their `command` steps. The sanity pipeline expands to its fifteen `default_steps()` entries, each to its own subprocess or in-process validator.
3. **Test.** Apply (a)–(c) to every check found. Record the decision for each, including exclusions.
4. **Close.** Repeat until no newly reached file contains an untested check.
5. **Include the pinning tests.** For every file admitted by step 3, find the test that asserts its current behavior and admit that test unless it is already inside instruction §7.1 or §7.2.

**Stopping condition.** The trace is complete when every check reachable in step 2 has been tested in step 3 and each is either (i) independent of release admission, (ii) already owned by PR04 under instruction §7.1/§7.2 or already carried by the plan's necessary dependents, or (iii) in the enumerated set of §6.2. Reaching that state on all three chains is what makes §6.2 an exhaustive claim rather than an inspection.

**Exclusions found by the trace, with reasons.** These are reachable but excluded, and are listed so the claim is falsifiable:

| ID | Reached file or check | Why excluded |
| --- | --- | --- |
| X-1 | `ci/jobs/rails_closed_refusal.yml` → `tests/bodygraph/test_resolver_vendor.py` | Closed-rails vendor refusal. Exercises no compat or Reader success path; unaffected by admission state. |
| X-2 | `ci/jobs/logs_keys_only_redaction.yml` → `tools/evidence/generate_rails_gate_evidence.py --check` and vendor tests | Vendor transport policy, retry and redaction evidence built from `engine.bodygraph.vendor_client`. Prints `RAILS_GATE_EVIDENCE_OK` independent of release admission. |
| X-3 | `tests/bodygraph/test_vendor_client.py` (rails lane, step 1) | Vendor client policy only. |
| X-4 | `ci/checks/run_rails_job_definitions.py` | A strict closed-YAML parser plus a credential-declaration rejector. The corrected `rails_open_conformance.yml` uses only `command` and `proves`, which it already parses (`:92–99`), so the runner needs no change. |
| X-5 | `scripts/release_id_recompute.py --check-manifest-only` (release lane and sanity stage 02) | Validates the canonical bytes of `catalog/manifest.json` only. **Executed at this head: exit 0.** It passes on the incomplete 15-member manifest and is indifferent to admission. |
| X-6 | Sanity stages 01, 07, 08, 09, 10, 11, 12, 13, 14, 15 | Environment pins, direct-DB contract and posture, BodyGraph policy proofs, mapped-cache behavior, Index/Mirror refresh, evidence-path validation, mirror-schema and hash checks, orientation and final-LF. None produces a successful compat or Reader result; each validates static or independently materialized artifacts. |
| X-7 | Sanity stage 06 → `generate_rails_gate_evidence.py --check` | Same as X-2. Stage 06 also re-invokes `run_rails_job_definitions.py` over all three job files, which is a third reachable instance of file 1 — already in the set, so nothing new enters. |
| X-8 | Sanity stage 03 → `tools/evidence/run_canonical_json_gate.py --check-only` | Reachable and genuinely affected — it imports `compat_public` and `conjunction_public` from `engine.compat.compute` (`:42`) and `create_app` (`:31`). **Already carried by PR04's plan §6.2 as a necessary dependent**, so it is excluded from the overlay under stopping condition (ii). Flagged rather than hidden: if implementation finds that stage 03 must itself emit the third state, that is a gate-semantics change by the §5 criterion and belongs in the overlay. The reviewer may wish to admit it pre-emptively on the §6.2.1 reasoning. |
| X-9 | `tests/http/test_reader_a7_transport.py` | Asserts `GET /reader` 200 and `POST /reader` 405 and must change — but it is an existing HTTP/Reader test home already owned under instruction §7.2. Excluded under stopping condition (ii). |
| X-10 | `tests/evidence/test_release_attestation.py` | `test_v1_schema_preserves_the_pf12_wire_contract` (`:388`) pins the `PR06R_B_FINAL_PASS` const, which condition 4 forbids changing, so that test stays green and confirms the boundary holds. Its failure-receipt and declared-output-roster tests (`:302`, `:264`) are assertions about receipt shape, which this delta does not change — only the `code` value, which the schema leaves open. Excluded, and named so the reviewer can overrule if it judges the code value in scope for that test. |
| X-11 | `tests/runtime/test_identity.py`, `tests/evidence/test_release_manifest_content_binding.py` | Runtime identity and manifest content binding. Independent of the gate outcome. |

**Honest limit of this claim.** The trace is exhaustive over the three chains as they exist at head `332fa4c`, by the definition above. It is a static trace: it proves which checks *require* a positive value, not that an implementation confined to these twelve files will pass on the first attempt. X-8 and X-10 are the two places where a reasonable implementer could conclude a thirteenth or fourteenth file is needed, and both are named above rather than left to be discovered.

### 6.4 Candidate disposition — D, carried forward as settled

Candidate **D** — the delta of §6.2 executed inside PR04 under an overlay that names the files — remains the disposition, decided by RS-20 (review §5) and not reopened here. A, B and C are recorded with their costs for completeness only and are **not** re-argued.

| Candidate | Delta | Authority required | Cost |
| --- | --- | --- | --- |
| **D (settled)** | §6.2, inside PR04 under an overlay naming the files | Bounded implementation rescope; RS-20 `APPROVE` with one PF10 addendum overlay | Widens PR04's loci to **eight production and CI-configuration files plus four test homes** (§6.2), corrected from v1.0's six. **The CI-surface cost is nil (R-5):** PR04's candidate already runs full validation and all seven lanes, because plan §6.5 changes `ci/checks/classify_ci_changes.py`, a member of `_FULL_VALIDATION_PATHS`; RS-20 confirmed by executing the classifier that this path alone returns every lane `True` with `reason='selected_lanes'`, and `.github/workflows/ci.yml` independently maps to all seven. **Adding the workflow, job and evidence files selects no additional lane and enlarges no CI surface.** D's real cost is precedent and ownership, addressed by the §5 criterion and the R-7 ownership bound. |
| A | Same delta as its own unit of work | Same, plus a new unit in an immutable approved decomposition | Identical engineering; strictly larger for the same result. |
| B | Re-sequence so PR06's complete release admission lands before PR04's consumer switch | Whole-change Plan dependency-order change against PF10 §2.13; IA/Isis decision | Largest and least safe; PR06's admission work depends on PR04/PR05 outputs, so the re-sequence is not obviously coherent. |
| C | Land PR04 with rails and release lanes truthfully red under a scoped Product Owner CI waiver until PR06 | Product Owner decision; contradicts instruction §12 unless expressly granted | Leaves ordinary CI red across PR04 **and PR05** (§7), destroying the signal for every candidate in that window, and defers rather than resolves. Requires Nathan's express waiver, which no one has requested and which this proposal does not request. |

## 7. Effects

| Dimension | Effect |
| --- | --- |
| Requirements | None changes in substance. The affected obligations are `K040-REQ-012` and `AC040-08` (evidence coherence) and the CI clause of PR04's completion condition (plan §4.2 item 4). |
| **Dependencies (R-4 — proof, not assertion)** | **PR05 is covered by an overlay approved on the corrected delta, needs no separate overlay and receives no new loci.** Proven, per RS-20 review §7: (1) PR05's owned loci (Plan §6.5) are `tests/fixtures/magic10/v1/goldens.json`, `tools/config/artifacts.py`, `tools/config/generate_config_artifacts.py`, `tools/bodygraph/check_magic10_gate_readiness.py` and existing config/core/bodygraph/application test homes; (2) executing the classifier over exactly those paths yields the lane union `{evidence, product, release}`, so **the release lane is selected**; (3) the release lane is precisely where sanity stages 04 and 05 run, so PR05 hits the identical refusal — through the release lane only, not the rails lane, so it inherits via one chain rather than two; (4) PR05 owns **none** of the §6.2 files and can make no truthful treatment under its own authority; (5) PR05 runs before PR06 under the order PF10 §2.13 fixes. Because the condition keys on the non-admitted state of the active release rather than on PR04's candidate, it covers every candidate in the interval and extinguishes for all of them when PR06 lands. PR06 owns convergence under any disposition. |
| Tests | Plan §8 is unchanged: the six `R040-IA30-02` proof classes, the eligibility matrix, the Reader POST suite and the CLI/compat carriers all stand as designed. The four test homes in §6.2 change only to track the gates' corrected outcome vocabulary. |
| Ops | None. No Ops task, environment, deployment or vendor operation is created or required. |
| Documentation | None beyond this proposal, its application report and the RS-20 decision. No PF-Canon edit is proposed. On `APPROVE`, RS-20 — not this author — emits exactly one PF10 addendum overlay under PF10-FORM-001. |
| **Downstream (R-7)** | No effect on PR07, OPS01, independent QA, release promotion, PF09 movement or Epic closure. **PR04's bounded touch on `build_release_attestation.py` transfers no attestation ownership from PR06**, whose ownership of the complete release, promoted roster, release identity, manifest cut and owning attestation validator is unchanged; the bound is stated in full at §6.2. |
| Evidence integrity | Frozen historical captures stay frozen and unedited. Affected governed artifacts are regenerated through their existing owning writers under Plan §7.2, never hand-edited, and no new evidence family is created. |

## 8. Completed valid work preserved

Preserved intact and not reopened: PR04 plan §§5–8 in full (designed interfaces, invariants, contracts, the exact file and component plan, the requirement-to-change-and-test mapping and the complete test design); plan §9 checkpoints C1–C3, executable exactly as written; plan §§10–12 (local validation commands, review checklists, risk register). Only plan §9 item 15 and §4.2 condition 4 remain dependent on the disposition.

Also preserved: proposal v1.0 at its own path, complete and unmodified, superseded but not deleted or rewritten; the immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1; every active PF10 overlay in §2; accepted-final PR01, PR02 and PR03, which are historical evidence and are never rerun; the original authority of every existing owner; and the dedicated PR04 session `PR04-HDE-EPIC040-1`.

## 9. Originating stage, vehicle state and lawful return point

- **Originating stage:** PR-20 planning for `HDE-EPIC040-PR04`, in session `PR04-HDE-EPIC040-1`.
- **Vehicle state:** no Proceed, no workspace, no worktree, no branch, no open PR, no commit, no CI run. These are truthfully **not yet produced**, not missing prerequisites. **No `PR_RETURN_PHASE` applies** and none is asserted; RS-40 is ineligible and is not invoked.
- **Immediate return:** this revision returns to **Isis-50**, the same RS-20 reviewer session, for a second RS-20 decision on this v1.1.
- **After that decision:** `APPROVE` → RS-20 emits exactly one PF10 addendum overlay, and session `PR04-HDE-EPIC040-1` issues plan v1.1 as a complete successor carrying the overlay, in state `AWAITING_PO_PROCEED` for Nathan's `PR-30` invocation. `REJECT` → the decision and preserved evidence return to that session; the plan cannot truthfully reach `AWAITING_PO_PROCEED` without a Product Owner decision on candidate C. A further `REVISION_REQUIRED` → RS-30 again, to this same author. `SPECIFICATION_CHANGE_REQUIRED` → Nathan and the Specification owners.
- No route restarts IA-30 or IA-40, rewrites an approved base, mints a Proceed, reruns accepted-final work, merges, or invokes PR-50. Only Nathan may invoke PR-50 for an exact PR.

## 10. Evidence index

| ID | Claim | Exact source | Kind |
| --- | --- | --- | --- |
| E-01 | Admission refuses `INCOMPLETE_RELEASE_ROSTER` at current head | `load_active_mechanics_bundle()` executed under closed rails; `engine/config/registry_loader.py:400, 447, 1218–1226` | Executed + read |
| E-02 | Rails ABBA gate is green at current head, all predicates true | `generate_open_rails_abba_proof.py --check-current` executed under `SAFE_MODE=0 ALLOW_NETWORK=1`, exit 0 | Executed |
| E-03 | Manifest carries 15 members against a 44-member pinned roster | `catalog/manifest.json` `files` length; `ADMITTED_RELEASE_ROSTER` invariant | Read |
| E-04 | Gate compares live Reader bytes against a real `hdctl` subprocess | `generate_open_rails_abba_proof.py:421–422, 490–492, 521, 543–547` | Read |
| E-05 | Release lane is selected for every PR04 product path | `ci/checks/classify_ci_changes.py`: `_PRODUCT_PREFIXES` → `{"product","release"}` | Read |
| E-06 | Attestation fails closed on a sanity-stage failure | `tools/evidence/build_release_attestation.py:766`; log-tail requirement at `:757–766` | Read |
| E-07 | Sanity stages 04/05 invoke the determinism, ABBA and A7 builders live | `tools/evidence/run_sanity_pipeline.py:68, 122–155`; `default_steps()` at `:58–86` | Read |
| E-08 | A7 capture hard-requires `POST /reader` → 405 | `tools/evidence/generate_a7_transport_proofs.py:75` | Read |
| E-09 | `POST /api/reader` currently returns 405 `method_not_allowed` | `adapter/http_reader.py:459–462` | Read |
| E-10 | The legacy band path is still live, which is why E-02 is green | `engine/runtime/public.py:29–32` (`ts_v0`) | Read |
| E-11 | A canonical failure-receipt contract already exists and is already written | `schemas/hde_release_attestation_failure.v1.json`; `build_release_attestation.py:498–507` | Read |
| E-12 | The failure receipt's `code` and `stage` are open tokens, not enums | `schemas/hde_release_attestation_failure.v1.json` `"pattern": "^[a-z0-9_]+$"` | Read |
| **E-13** | **Corrected (R-3):** the success attestation pins `validation_result` and `release_admission` as `const`, and `pipeline_stop` as **`{"type": "null"}`** — a type pin, not a const | `schemas/hde_release_attestation.v1.json` | Read |
| E-14 | No non-documentation drift between the plan's verification head and current head | `git diff 6ecacafb..main -- . ':(exclude)docs/'` empty | Executed |
| **E-15** | **(R-1)** The gate wrapper is a second byte-exact `PASS` pin: `_expected_log()` builds all-`:OK` + `first_failed_stage:NONE` + `summary:PASS`, and `_valid_log()` requires byte equality | `tools/evidence/run_sanity_pipeline_gate.py`; invoked from `build_release_attestation.py:669` | Read |
| **E-16** | **(R-1)** No third status token exists today | `run_sanity_pipeline.py:222` (`"OK" if status == "OK" else "FAIL"`) and `:282` (`"PASS" if passed else "FAIL"`) | Read |
| **E-17** | **(R-2, new)** Stage 04's determinism builder runs a live Reader envelope and an `hdctl` subprocess | `tools/evidence/generate_determinism_gate_proofs.py:10, 25, 28`; called from `run_sanity_pipeline.py::validate_current_reader_cli_determinism` | Read |
| **E-18** | **(R-2, new)** `tests/evidence/test_rails_ci_workflow_integration.py:153–157` asserts equality between the exact set of `tests/...` targets in `ci.yml` and a fixed set | That file | Read |
| **E-19** | **(R-2, new)** `tests/evidence/test_sanity_pipeline.py:172` pins the gate wrapper's byte-exact PASS log; `:48`, `:166` pin the rendered tokens | That file | Read |
| **E-20** | **(R-2, new)** `tests/evidence/test_open_rails_abba_proof.py:160` asserts `top_level_pass is True` | That file | Read |
| **E-21** | **(R-2)** The sanity log is a tracked governed artifact ending `summary:PASS`, with a `.path_proof.txt` sibling, and the release lane asserts a clean tree | `git ls-files audit/gates/sanity_pipeline/`; log tail; `.github/workflows/ci.yml:243, 268–270` | Read |
| **E-22** | **(R-2)** `release_id_recompute.py --check-manifest-only` passes on the incomplete manifest | Executed at this head, exit 0 | Executed |
| **E-23** | **(R-5)** `ci/checks/classify_ci_changes.py` is a member of `_FULL_VALIDATION_PATHS`, so PR04's candidate already selects all seven lanes | `ci/checks/classify_ci_changes.py`; RS-20 review §5, which executed the classifier | Read + RS-20 execution |

**Execution environment for E-01, E-02, E-14 and E-22.** Python in the session container with `requirements.txt` and `requirements-dev.txt` installed; `LC_ALL=C LANG=C TZ=UTC`; clean working tree before and after; no repository mutation, no network vendor call, no write to any governed artifact. As recorded in v1.0: a first attempt at E-02 failed on the single predicate `canonical_gate_success` because `flask` was not yet installed in this container — a local environment gap, not a repository defect — and E-02 is the result after installing the declared requirements.

## 11. Risks, exclusions and unresolved facts

**Risks.** R-01: an overlay that widens a work unit's loci to CI and evidence files sets a precedent; it is bounded by naming the files exactly (§6.2), by the gate-semantics criterion that distinguishes them from ordinary necessary dependents (§5), by the exhaustive derivation that makes the list testable (§6.3), and by binding acceptance to the not-admitted condition so it expires at PR06. R-02: if the ordinary-CI acceptance is written loosely it could mask an unrelated genuine failure; condition 2 of §6.2 requires it to key on the one explicit outcome only, and that condition is binding. **R-03: answered — PR05 is covered, with proof at §7; PR05 requires no separate overlay and receives no new loci.**

**Exclusions.** This proposal does not approve anything, does not draft, number or imply a PF10 addendum, does not edit PF-Canon, does not request or imply a Proceed, does not create a branch or PR for PR04, does not implement, does not change the immutable Plan, does not rerun accepted-final work, and does not invoke or route to PR-50.

**Unresolved facts, all non-gating.**
- **U-01 — resolved.** The baseline advanced and PRs #452, #453, #457 and #462 merged; §3 records the current head and the empty non-documentation diff.
- **U-02 — carried.** Plan §14.2 decision D-03 (the valid self-pair exit-0 carrier) remains a deliberately unbundled potential second boundary. Not raised here.
- **U-03 — resolved.** Specification v1.1's SHA-256 was independently recomputed as `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` and matches. Closed at v1.1.
- **U-04 — carried.** The repository-resolved current PF12 is v2.9.5 while the approved Plan's register overlay records v2.9.6. Owner: the governed PF12 maintainer. It affects neither F01 nor §6.1, which cite the repository's actual schema files.
- **U-05 — carried.** PF10's §1.1 Addendum Index lists through 2.13 while the body carries §2.14. Observation for the PF10 drain owner.
- **U-06 — carried.** Repository prompt-provenance persistence remains `PENDING`: `docs/changes` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`, with no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination.
- **U-07 — new, non-gating.** X-8 and X-10 in §6.3 are the two exclusions a reasonable implementer could overturn. Both are named with their reasoning so RS-20 may admit either pre-emptively rather than leaving it to be discovered at implementation.

## 12. Carried `CANON_CONFLICT_REGISTER`

Carried unchanged from Plan v2.1 §11.1, PR04 instruction §13, proposal v1.0 §12 and RS-20 review §10. **No entry is reopened, relabeled, omitted, newly decided or resolved here, and `HDE-EPIC040-PR04-F01` is not a register entry.**

| ID | Classification / status | Decision lineage | Carried effect | Remaining owner / state |
| --- | --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED` exactly as proposed | Thoth-17, 2026-09-08T13:23:24Z, against Specification v1.0 represented by approved v1.1 | Preserve explicit `Done` exclusions and current PF09.3 agreement | Source correction resolved; no drainage pending |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use the current controlled PF12 Markdown; historical identity mismatch is history only | Resolved; PF12 version currency is ordinary maintenance (U-04) |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use current PF14 v3.5.7; C040-05 controls its contradictory core-test text | Historical mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | QA identity history preserved; PR04 performs engineering checks, not independent QA | Historical mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED`, alternative A exactly | Isis-49, 2026-09-09T03:57:16Z, against Plan v1.0 | The four-argument Gate core supersedes precomputed-score passages; no second calculator | Permanent PF14 §6.7 correction pending with its governed maintainer; non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED`, alternative A exactly | Isis-50, 2026-09-09T11:48:08Z, Review v2.0 against Plan v2.0 and ADR v1.0 | 36-row taxonomy and 16-case conformance as delivered through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage pending with governed maintainers; non-gating |

Review fields for **this version** remain explicitly **not yet reviewed**: the second RS-20 decision, its time and its rationale are Isis-50's to supply. The v1.0 decision history is preserved: `REVISION_REQUIRED`, Isis-50, 2026-09-22T06:48:06Z, no addendum created.

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES` — this entry, preserving the earlier ones by exact reference:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`
- `work_unit_id` / `finding_ref`: `HDE-EPIC040-PR04` / `HDE-EPIC040-PR04-F01`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204`
- `prompt_retrieved_revision`: page fetched, `page_last_edited_at` `2026-09-21T22:57:39.304Z`
- `role_stage`: retained whole-change HDE-EPIC040 IA session / RS-30 revision author, same author as the RS-10 proposal
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `capture_time`: `2026-09-22T07:02:23Z`
- `runtime_identity`: not asserted beyond the Product Owner-assigned role and session reference
- `result`: this `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1`, `RESCOPE_PROPOSAL_PENDING_REVIEW`, with its companion `REDLINE_APPLICATION_REPORT`
- `result_refs`: repository path in §1; branch, commit and pull-request identities populated only after they exist

Preserved earlier entries, by exact reference: `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01` (review §13), `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01` (proposal v1.0 §13), `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01` (plan §16) and `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (instruction §15).

Repository provenance persistence remains `PENDING / NON_GATING` (U-06). Nothing is invented, and this gap blocks no authorized work. Owner: the authorized repository writer, once an actual procedure is installed.

## 14. Decision requested

RS-20 is asked to decide the corrected bounded delta in §6.2, on the enumeration derived by the method in §6.3, with the classification (§5) and candidate D (§6.4) settled by its own prior review and carried forward unchanged. Redlines R-1 through R-7 are applied; the per-item mapping is in `docs/ephemeral/HDE-EPIC040-PR04-F01-rs30-redline-application-report-v1.0.md`.

Two items warrant the reviewer's explicit attention, both surfaced by the R-2 trace rather than by the redline: the **eighth production file** `tools/evidence/generate_determinism_gate_proofs.py` and its one judgement (§6.2.1), and the **four pinning test homes** in §6.2. U-07 names the two exclusions (X-8, X-10) the reviewer may wish to admit pre-emptively.

A qualifying `APPROVE` emits exactly one PF10 addendum overlay under PF10-FORM-001; that addendum is RS-20's to produce, not this author's.

ASK OK?
