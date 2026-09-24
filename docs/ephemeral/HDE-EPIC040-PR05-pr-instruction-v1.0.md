---
artifact_type: PR_INSTRUCTION
artifact_id: HDE-EPIC040-PR05-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR05
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-24T17:57:11Z
next_stage: PR-20
---

# HDE-EPIC040-PR05 — PR Work-Unit Instruction v1.0

## 1. Identity and state

| Field | Value |
| --- | --- |
| Artifact type | `PR_INSTRUCTION` |
| Logical ID / version | `HDE-EPIC040-PR05-PR-INSTRUCTION` / `1.0` |
| State | `INSTRUCTION_READY` |
| Change | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| Work unit | `HDE-EPIC040-PR05` — Full golden comparison and read-only Gate readiness |
| `AUTHORING_CONTEXT` | `APPROVED_BASE_WITH_OVERLAYS` |
| Author / role | Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Architect |
| `session_disposition` / `role_session_ref` | `RETAIN_EXISTING` / the established whole-change IA session that authored the Audit v2.0, Plan v2.1, the PR01–PR04 instructions and the PR04 lineage review; no platform ID invented |
| `invocation_binding` | `HDE-EPIC040 / HDE-EPIC040-PR05 / PR-10` |
| `context_conflict` | `NONE` |
| Execution posture | `MANUAL_PROMPT_EXECUTION` |
| Capture time | `2026-09-24T17:57:11Z` |
| Path | `docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md` in `amthorn78/glow-hdengine-v2` |

This instruction defines exactly one approved work unit. It is not a detailed per-file plan, a Product Owner Proceed, implementation or merge authority, QA or Ops execution, a PF10 edit, release admission or activation, or Epic closure.

## 2. Approved lineage

All paths are under `docs/ephemeral/` on `main` unless stated.

| Role | Artifact | Identity |
| --- | --- | --- |
| `SPECIFICATION_REF` | `HDE-EPIC040-specification-v1.1-approved.md` | `SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, Thoth-17 `APPROVE` 2026-09-08T13:23:24Z; SHA-256 `43e1b182…e9df` |
| `IMPLEMENTATION_AUDIT_REF` | `HDE-EPIC040-implementation-audit-v2.0.md` | v2.0, `AUDIT_COMPLETE` |
| `IMPLEMENTATION_PLAN_REF` | `HDE-EPIC040-implementation-plan-v2.1.md` | v2.1, immutable approved base; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`. Its header reads `PLAN_PENDING_REVISED` (authoring state); the approval is the separate review below |
| `PLAN_REVIEW_REF` | `HDE-EPIC040-implementation-plan-review-v2.1.md` | v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, binding the exact Plan bytes |
| Approved overlay | `HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` | **`RESCOPE_REVIEW`** v2.0, Isis-50 `APPROVE`; its one addendum is `HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` (SHA-256 `86708f5c…82c1`), published as PF10 §2.15 |
| Accepted PR01 | `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md` | `ACCEPT` (#403). Use v1.1; v1.0 is the superseded `PENDING` predecessor |
| Accepted PR02 | `HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT` (#404) |
| Accepted PR03 | `HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` | `ACCEPTED_FINAL` (#405) |
| Required predecessor | `HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md` | `decision: ACCEPT`, `ACCEPTED_FINAL`, 2026-09-22T21:35:55Z; SHA-256 `08bff318…dba4`. PR04 landed as squash commit `cd6f9e6ca4541f448f77b206269f3882cb919f36` (#467), tree `72f0868de3635494916097b36656af302b914003` |
| Governing prompt | [PR-10 — Create PR Work-Unit Instructions — 091426.1](https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204) | Selected contract `GCFPE-20260914.1 / 091426.1 / 55` per the GCFPE Membership and Release Register, read 2026-09-24 |

**Overlay type, stated precisely.** The operator's handoff labelled the F01 review a `REMEDIATION_REVIEW_ID`. It is an RS-20 `RESCOPE_REVIEW` (bounded implementation rescope) with one PF10 addendum, not an ESC-40 `REMEDIATION_REVIEW`. It is carried here under its true type; no history is renamed.

No accepted PR, approved base or original Proceed is reauthored or rerun. PR01–PR04 are `ACCEPTED_FINAL`.

### 2.1 Current PF10 and applicable overlays

Current controlled PF10, resolved from `docs/pfcanon/` at authoring: **`docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md`**, 2,156 lines / 235,187 bytes, SHA-256 `d79e41102a88ded2cf9823787925c0ac243622cf2a3e59a3e5c1da28387e6f91`. It supersedes v13.2.9. Its Addendum Index now lists 2.1–2.19 and includes §2.14, so the earlier index/body gap (PR04 lineage review U-05) is closed.

| PF10 addendum | Effect on PR05 | Retained source artifact |
| --- | --- | --- |
| 2.2, 2.3, 2.4, 2.5 | C040-01–C040-06 decided guidance; the four-argument core is the only calculator; the 36-row taxonomy and 16-case conformance are the mechanics inputs | `HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md`, `…-C040-01-04-resolution-pf10-addendum-v1.0.md`, `…-C040-06-PF10-build-notes-addendum-v1.0.md` |
| 2.6, 2.7, 2.9, 2.10, 2.11 | Accepted PR01/PR02 behavior, consumed unchanged | as listed in the PR04 instruction §2.1 |
| 2.12 | The admission execution-provenance and executable-equivalence owner in `engine/config/registry_loader.py` stays the owning admission boundary. PR05 must not weaken, bypass or relocate it | `HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` |
| 2.13 | PR03 accepted; order `PR01 → … → PR05 → PR06 → PR07 → OPS01` fixed | `HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` |
| **2.15** | **F01: `RELEASE_NOT_ADMITTED` posture for the PR04-to-PR06 interval. PR05 is covered by it, needs no separate overlay and gets no new loci** (PF10 v13.3 line 1726). See §7 | `HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` |
| 2.16, 2.17, 2.18 | PR04 deferrals F03, F05, F07 to PR07 — context PR05 inherits and does not fix (§9) | `HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md`, `…-F05-…`, `…-F07-…` |
| 2.19 | PR04 lineage acceptance | `HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md` |

Effective baseline: **approved base + the overlays above.** None moves ownership into or out of PR05. §2.8 (PF10-FORM-001) and §2.14 are not applicable to PR05.

## 3. Repository and source baseline

### 3.1 Repository

- `main` head at authoring: `b0d1082ac663f4cd11237f12ebdf34415e2b5b56`, tree `bf394ae7a382535f6fd93148f6b7d329019b636d`, committed 2026-09-24T17:49:06Z.
- Since PR04 landed (`cd6f9e6`), the **only** changes outside `docs/` are `.github/pull_request_template.md` (new) and `AGENTS.md` (+6 lines, PR-description sections). **The executable baseline for PR05 is PR04's landed tree.** PR-20 must re-verify at its own time.
- No PR05 branch, commit, pull request, detailed plan, Proceed, implementation, review, CI result or merge exists.

### 3.2 Verified state of PR05's planned loci

| Locus | State | Consequence |
| --- | --- | --- |
| `tests/fixtures/magic10/v1/goldens.json` | **Absent**; `tests/fixtures/magic10/` does not exist | PR05 creates it. CI classifies it to `{product, release}` |
| `tools/bodygraph/check_magic10_gate_readiness.py` | **Absent**; `tools/bodygraph/` does not exist | PR05 creates it. **CI currently refuses this path**: `classify_paths` raises `CI_CHANGE_SURFACE_UNCLASSIFIED` for it — see §6.4 |
| `tools/config/artifacts.py` | Present (7,341 bytes). Public API is build/write only: `require_closed_rails`, `build_magic10_config`, `build_band_edges`, `write_magic10_config`, `write_band_edges`, plus private `_publish_prepared` | The comparison mode lives beside write helpers and must be structurally unable to reach them (§5.2) |
| `tools/config/generate_config_artifacts.py` | Present (14,456 bytes) | Existing CLI home; any new flag is a PR-20 proposal, not an existing command |
| Config/core/bodygraph test homes | `tests/config/` (14 modules incl. `test_config_artifacts.py`, `test_production_admission.py`, `test_magic10_contracts.py`); `tests/core/test_engine_core_{abba,determinism,purity}.py` | Existing homes for the comparator and readiness tests |
| G007/G008 application oracles | Already pinned by PR04 in `tests/compat/test_evaluate_pair_eligibility.py:45–48` and equal to PF01 §9.5 | PR05's fixture must agree with them; a disagreement is a finding, not something to edit away (§5.1) |

Seams PR05 consumes, all present on `main`:

- `engine.compat.compute.evaluate_pair(a, b, *, bundle_provider=None, cache=None, router=None)` — the one application evaluator, with an explicit bundle-provider seam.
- `engine.core.core.compute_core(member_a, member_b, mechanics_bundle, release_id)` — the one four-argument kernel (PR03, C040-05).
- `engine.config.registry_loader._load_active_mechanics_bundle_from_root(root)` — the private fixture seam. It still runs the complete PF10 §2.12 executable-equivalence check; only the root differs from public admission.
- `engine.config.registry_loader.load_active_mechanics_bundle()` — public admission. **It refuses on `main` with `INCOMPLETE_RELEASE_ROSTER`** (15-member manifest against the 44-member roster).
- `engine.bodygraph.gates.normalize_gates` — the shared Gate validator (PR02).
- `engine.db.adapter.DBAccess` — the DB abstraction; it exposes `readonly_tx`, `query`, `exec` and `tx`. `engine.bodygraph.mapped_cache.read_current_mapped_bodygraph(db, canonical_user_id)` reads one current row (PR04).

### 3.3 Controlled subject-matter sources

Resolve each as the unique current controlled Markdown in `docs/pfcanon/`. Resolved at authoring:

- **`PF01-Canon-HDE-Math-Spec-v1.3.7.md`** (SHA-256 `101576d0…`) — **§9.5, "Canonical Magic10 v1 goldens" (lines 1867–2018), is the sole authority for M10-G001–G008**: inputs, full metadata, synthetic UUIDs, exact expected outputs and hashes. §4.7 governs the eligible/ineligible emission rule.
- **`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`** (SHA-256 `d7b2e028…`) — names `tests/fixtures/magic10/v1/goldens.json` as the governed golden identity (line 4762): a deterministic verification input, **not** a second formula authority, a `config.magic10` payload, an Index/Mirror entry by implication, or a manifest member. Names `tools/bodygraph/check_magic10_gate_readiness.py` in the promoted "Gate persistence and resolution" class (line 1733). States that `tools/config/{artifacts,generate_config_artifacts}.py` **must fail closed** on an absent, invalid, ambiguous or hash-mismatched active mechanics configuration and **must not activate a candidate** (lines 4756–4760).
- **`PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`** — HDE-SEPA005.4 ("exact golden-output comparison, and an explicit guarantee that comparison cannot change the active production configuration") and HDE-SEPA005.5 ("read-only current-row Gate-readiness command"). Both `Not done`. PR05 contributes to them; it moves no PF09 status.
- `PF02-Canon-HDE-Architecture-v2.4.5.md` — pure-core and application separation. `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` — error tokens and CLI carriers if a CLI surface is added. `PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md` §6.7 with C040-05. `PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` for source fidelity.
- `PF10-HDE-Build-Notes-v13.3.md` per §2.1.

PF09.6 (Distillation, HDE-DIST008.x) and PF09.7 also list the golden path and readiness tool. They are **later-phase context, not PR05 authority**; PR05 claims no HDE-DIST008 completion.

Never use a Google Doc, `.doc`, `.docx`, export, archive, search hit, generated artifact or this instruction as authority where a source above owns the fact. There is no fallback.

## 4. Objective and completion boundary

**Objective (Plan §6.5).** Deliver the complete deterministic, non-mutating golden comparison capability and the current-row Gate-readiness tool.

**Completion (Plan §6.5).** The full non-mutating comparator and read-only readiness behavior are demonstrated in actual PR checks and CI. **No live current-row readiness verdict and no QA PASS.** PR06 later runs the comparator against the complete actual candidate.

**Not in this unit.** PR06 owns complete release admission, the 44-member manifest, promotion, and evidence convergence (including the sanity log's `NOT_ADMITTED → PASS` transition). PR07 owns DOC-10 documentation and F03, F05, F07. OPS01 owns final external verification. Also excluded: live DB or vendor operation, any write to a database, independent QA, Ops, deployment, PF10 edit, Canon drainage, PF09 movement, Epic closure.

## 5. Required behavior

### 5.1 Golden fixture — `tests/fixtures/magic10/v1/goldens.json`

- Exactly eight cases, **M10-G001 through M10-G008**, each transcribed from PF01 §9.5 with **full exact metadata and the synthetic UUIDs PF01 gives** — never the shortened highlights in Plan §5.9's table (Plan §5.9: "Use full exact metadata … not shortened substitutions from this table").
- Each case carries an explicit case type: **kernel** or **application**. G002, G003 and G006 are kernel cases built from injected vectors and are not claimed as physically realizable charts. G007 and G008 are application cases.
- Canonical JSON bytes per PF12 §4. The fixture is **input data only**: not a manifest member, not an Index/Mirror entry, not a formula.
- **Agreement check.** PR04 already pins G007/G008 values (`G007_READER_HASH`, `G008_FINGERPRINT`, `G008_PAIR_KEY`, `G008_READER_HASH`) and they equal PF01 §9.5. If transcribing PF01 into the fixture ever disagrees with those, or with the landed implementation's output for any case, that is a **finding**, not something to reconcile by editing either side. Route it per §10.

### 5.2 Comparator — in `tools/config/artifacts.py` / `generate_config_artifacts.py`

- **Inputs:** an explicit local candidate root and the complete golden collection. Validate both before anything runs.
- **Membership:** refuse a missing, duplicate or unknown case, and a wrong case type.
- **Execution:** each case runs through the canonical entrypoint for its type — kernel cases through PR03's canonical kernel functions, application cases through `evaluate_pair`. **Never a second formula**; the comparator orchestrates, it does not calculate (Plan §5.9).
- **Admission:** application cases obtain their bundle by loading the explicit candidate root through `_load_active_mechanics_bundle_from_root`, passed via `evaluate_pair`'s `bundle_provider` seam, so the full PF10 §2.12 executable-equivalence check still runs. A fixture candidate's success is **test-only** and is never release admission.
- **Comparison:** all fields, order, identities and bytes. Report **every** mismatch deterministically — not only the first.
- **Read-only, structurally.** The compare mode cannot call `write_magic10_config`, `write_band_edges`, `_publish_prepared` or any activation or generation helper, and **must not invoke generation as a side effect** (Plan §6.5). It never rewrites configuration, the manifest or fixtures, never replaces an expected value, never repairs a mismatch, and never activates a candidate (PF12 lines 4756–4760).
- **Refusal:** absent, invalid, ambiguous or hash-mismatched configuration, source/config/manifest mismatch, and refused admission all fail closed as mismatches or refusals — never as equality.
- **Invocation surface:** any new CLI spelling is a PR-level proposal requiring its own tests and docs (Plan §5.9). This instruction advertises no runnable command.

### 5.3 Readiness — `tools/bodygraph/check_magic10_gate_readiness.py`

- Selects **only** the selected current-row set, **read-only**, through the existing `DBAccess` abstraction, and applies the **shared** Gate predicate (`normalize_gates`) — no second validator.
- Validates row metadata and required Gates; collects bounded, aggregate, identity-safe diagnostics.
- **No `UPDATE`, `INSERT` or `DELETE`, no acquisition, no auto-repair, no backfill, no vendor call.** Use `readonly_tx`, never `exec` or `tx`.
- **An inaccessible or denied dataset yields unavailable or error, never all-ready.** An empty selection has explicitly defined semantics and is not silently "ready".
- **No payload leakage:** never dump birth tuples, Gate payloads, charts or person labels into output, logs or evidence.
- Prefer the tool's own read-only query through `DBAccess`, reusing `read_current_mapped_bodygraph` where it fits. A change to `engine/bodygraph/mapped_cache.py` is **not** pre-authorized; if PR-20 finds one necessary, apply §10.
- **Offline only in this unit.** Fake-DB tests prove behavior. Current production rows are unobserved; an actual live readiness claim requires separately authorized observation outside PR05 (Plan §5.9).

## 6. Bounded files and components

### 6.1 Owned loci (Plan §6.5)

`tests/fixtures/magic10/v1/goldens.json`; `tools/config/artifacts.py` and `tools/config/generate_config_artifacts.py` as the bounded comparison home; `tools/bodygraph/check_magic10_gate_readiness.py`; the existing config, core, bodygraph and application test homes. New helper and function names are chosen by PR-20.

### 6.2 Preserved surfaces

PR01 catalog/contract data; PR02 normalizer, immutable bundle and the §2.12 admission owner; PR03 kernel and intrinsic identity; PR04 application seams, `evaluate_pair`, eligibility, the F01 gate implementation and every PR04 test pin. All consumed unchanged.

### 6.3 Necessary dependent — CI path registration

`tools/bodygraph/check_magic10_gate_readiness.py` is **unclassified today**: `classify_paths` raises `CI_CHANGE_SURFACE_UNCLASSIFIED`, so a candidate adding it fails CI at classification. PR05 must register the new path (and any new test path the classifier rejects) in `ci/checks/classify_ci_changes.py`.

This is a **necessary dependent, not a rescope.** It is coherence registration — which lane a path selects — and changes no gate semantics or acceptance, which is exactly the line the approved F01 proposal drew between plan dependents and overlay files (proposal v1.1 §5). PR04 made the same kind of registration without one.

### 6.4 Consequence for CI lanes

`ci/checks/classify_ci_changes.py` is a member of `_FULL_VALIDATION_PATHS` (verified). Changing it makes the PR05 candidate run **full validation and all seven lanes, including the rails lane** — not only the release lane that the F01 review computed from Plan §6.5's loci alone. Coverage is unaffected: the F01 acceptance keys on the observed non-admitted state of the active release, not on the unit or the lane, so it covers every candidate in the interval. Carried so PR-20 plans for the rails lane rather than being surprised by it.

## 7. Inherited F01 condition — how PR05 lives with it

No admitted release exists until PR06. Therefore:

- Governed gates and the attestation on the PR05 candidate end `RELEASE_NOT_ADMITTED` (exit 3, explicit marker, never PASS), and ordinary CI accepts exactly that outcome — already implemented and landed by PR04.
- PR05 **must not** feed a synthetic or fixture release into any governed gate or the attestation, must not bypass or relocate admission, and must not emit `PR06R_B_FINAL_PASS`.
- **Inside pytest**, the comparator and readiness tests may use a validated synthetic complete-release candidate root through the existing fixture seam (§5.2). That is legitimate test evidence, not release admission.
- **Against the real repository root**, the comparator's application cases correctly **refuse** with `INCOMPLETE_RELEASE_ROSTER` until PR06. That refusal is the truthful result, not a PR05 defect, and must not be reported as a mismatch of golden values.

## 8. Acceptance, tests and evidence

### 8.1 Requirement coverage owned by PR05 (Plan §8)

`K040-REQ-010` (complete 8-case comparison through actual canonical code; read-only guarantee) and `K040-REQ-011` (read-only readiness capability) are PR05's principal obligations. PR05 also carries its portions of `K040-REQ-001` (ordered chain), `K040-REQ-008` (refusal matrix), `K040-REQ-012` (evidence) and `K040-REQ-013` (identities). Acceptance portions: **`AC040-06`** (complete golden and non-mutation), **`AC040-07`** (read-only readiness capability), `AC040-08` (evidence), **`AC040-09`** (read-only boundary). Obligations owned by PR06, PR07 or OPS01 are not claimed.

### 8.2 Comparator proof (Plan §6.5, §7.3)

- All eight cases pass against a validated fixture candidate, asserting the **complete** expected outputs, not only Plan §5.9's highlights.
- Altered field, order, byte or identity in any case yields a mismatch, and every mismatch is reported.
- Missing, duplicate or unknown case, and wrong case type, refuse.
- Source, configuration or manifest mismatch is not equality; refused admission is not equality.
- **Non-mutation:** snapshots of every candidate input and fixture are byte-identical after positive, negative **and exception** runs. Spies prove no write, activation or generation helper was called.

### 8.3 Readiness proof (Plan §6.5, §7.3)

Good, bad, missing, duplicate and malformed rows; empty-selection semantics; denied and unavailable DB; injected would-write and would-acquire/vendor spies proving none fired; **no false ready when unavailable**; observed selection reported precisely without birth or Gate payloads.

### 8.4 Evidence and CI

- **No governed primary evidence family is declared for the comparator or readiness tool** (PF12 checked). Their evidence is therefore **the actual PR test and CI record** with exact source commit and test identity (Plan §6.5, §7.2). Invent no epic-local canonical compare path, Machine Mirror key or acceptance token.
- The golden fixture is not automatically a manifest or Index member (PF12 line 4762).
- Any actually affected governed artifact is regenerated only by its owning writer, primary bytes first, from the same candidate root; never hand-edited.
- Local and CI proof is not live readiness, QA, acceptance or approval.

## 9. Inherited state PR05 does not own and must not fix

1. **F03** — `POST /api/reader?v=1` returns 404; the handler is served at `POST /reader` (blueprint at `url_prefix=""`). PR07, PF10 §2.16.
2. **F05** — the Reader emits `harmony`, which fails `schemas/reader.v1.schema.json` (only `*_leader` identities admitted). PR07, PF10 §2.17. **Interaction:** PF01 §4.7 and §9.5 define the Reader bytes behind G007/G008, including `harmony`. PR05 compares against PF01's oracle and must **not** "fix" the schema, the goldens under `goldens/reader/v1/`, or the emitter to make them agree.
3. **F07** — `tests/evidence/test_dev_conjunction_identity.py` fails 2 tests on `main`, outside every CI lane. PR07, PF10 §2.18. PR05 must not report it as a PR05 regression.
4. **Open by design:** O-12 (roster not packaged), O-20 and O-21 (capture generators and canonical harness; PR06), O-16 (`ERR_M10_GATES_MISSING` unreachable; PF01/PF05 maintainers), O-18 (narrative pack mount; PR06).
5. **Security review limitation** on PR04 (current-head security review absent). Product Owner's. Not PR05's to resolve.

**Route identity, stated from repository fact** (PR04 lineage review N-01): the served Reader POST route is `/reader`, not `/api/reader`. Do not repeat the Plan's conflation.

## 10. Rescope and owner boundaries

**Material** (PR-10 at 091426.1) means a change to the Epic-level commitment: its outcome or objective, approved acceptance criteria, a protected architectural, security, data-model or external-contract boundary, the scope of several planned work units, an accepted dependency or cross-team commitment, or budget, schedule or risk needing Product Owner direction. **A planned approach found incomplete, impractical or inferior is not by itself material.**

- A genuinely material finding: preserve all completed PR05 work and evidence, assign a stable `FINDING_REF` bound to `HDE-EPIC040-PR05`, and route through `RS-10` then `RS-20` (with `RS-30` only on an explicit `REVISION_REQUIRED`). An `APPROVE` emits exactly one PF10 addendum. Before publication there is no open PR and the approved delta returns to the same phase directly; after publication `RS-40` resumes the recorded phase.
- A non-material planning or implementation correction stays with its native owner and needs no rescope.
- A golden-value disagreement (§5.1) is evidence first: determine whether the fixture transcription, the landed implementation or PF01 is wrong before choosing a route. PF01 is Canon and is not edited here.
- A true product or Specification change returns terminally to Nathan and the Specification owners.
- No route rewrites the immutable Plan, mints a Proceed, reruns accepted work, merges, or invokes `PR-50` (Nathan only).

## 11. Merge, sessions, review and CI

- **Two dedicated sessions** (PR-10 at 091426.1): `PR-30` implements, tests locally, forms a coherent commit and publishes the initial candidate (`PR_CANDIDATE_PUBLISHED`), then hands off to **`PR-35` in its own dedicated session**, naming `PR_IMPLEMENTATION_RESULT` by repository path and the PR reference. PR-35 owns review correction, retesting, CI economy, current-head verification and `MERGE_PENDING`, without merging. No second Proceed.
- **Merge is Nathan's alone.** No agent merges, enables auto-merge, enqueues, schedules or offers a merge.
- Actual code review, security review of corrected code, findings and re-review, CI interpretation and any scoped waiver are PR-session obligations under this unit and `AGENTS.md`. No inherited CI exception or prior green run applies. PR descriptions follow the repository template at `.github/pull_request_template.md` and the `AGENTS.md` "PR descriptions" rules.
- `PR-40` runs only after the merge is observed as `MERGE_OBSERVED`, or, where no such result was returned for this merge, asserted by Nathan. It verifies merged state and landed attribution independently.

## 12. Migration, security and recovery

- **Migration:** none. No schema, data or loader migration; no manifest change.
- **Security:** synthetic fixtures and UUIDs only; never persist secrets, birth records or full Gate payloads in evidence. No remote schema resolution or uncontrolled filesystem traversal. Readiness stays read-only and never acquires vendor data.
- **Recovery:** on any error, configuration, fixtures and release selection stay unchanged and the exact mismatched case or source is reported. Restore tools, tests and fixtures together. **Never rewrite an expected value from failing actual output** (Plan §6.5).

## 13. Carried `CANON_CONFLICT_REGISTER`

Carried unchanged from Plan v2.1 §11.1, the PR04 instruction §13 and the PR04 lineage review §10. **No entry is reopened, relabeled, omitted or newly decided; PR05 opens none.**

| ID | Status | Effect carried into PR05 | Remaining owner |
| --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED`, Thoth-17 2026-09-08T13:23:24Z | `Done` exclusions and PF09.3 agreement preserved | Resolved |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED`, same | Use current controlled PF12 (repository v2.9.5) | PF12 version currency is ordinary maintenance |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED`, same | Current PF14 v3.5.7; C040-05 governs its core-test text | Resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED`, same | PR05 performs engineering checks, not QA | Resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED` alt. A, Isis-49 2026-09-09T03:57:16Z | **The comparator must call the one four-argument core; no second calculator** | PF14 §6.7 maintenance pending, non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED` alt. A, Isis-50 2026-09-09T11:48:08Z | Goldens exercise the 36-row taxonomy and 16-case conformance as delivered | PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |

The PF01 §4.5 versus PF05 §5.2.3 token-naming tension stays plan observation O-01 / PR04 result O-16 with the governed PF01/PF05 maintainers, decided by no one.

## 14. Ownership and current truth

- Instruction author and whole-change return owner: the retained whole-change HDE-EPIC040 Implementation Architect.
- `PR-20`: the dedicated PR05 PR-development session, assigned by the operator. This instruction neither creates it nor repurposes the IA session.
- `PR-30` and `PR-35`: two dedicated sessions, per §11.
- Merge: Nathan / Product Owner. `PR-40` reviewer after merge: this same whole-change IA in its read-only lineage-review role.

**Current truth.** Instruction `INSTRUCTION_READY`. Detailed PR05 plan `NOT PRODUCED`. PR-30 Proceed `NOT REQUESTED`, `NOT EXECUTED`. PR05 implementation, branch, commit, PR, review, CI and merge `NOT EXECUTED`. QA, Ops, release admission, PF09 movement and closure `NOT EXECUTED`.

## 15. Prompt-use provenance

`GCFPE_PROMPT_USES`:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-10-20260924-PR05-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`; `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1
- `work_unit_id`: `HDE-EPIC040-PR05`; `component`: golden comparison and read-only Gate readiness
- `requirements`: `K040-REQ-010`, `-011` principal; portions of `-001`, `-008`, `-012`, `-013`; `AC040-06`, `-07`, `-08`, `-09`
- `ecosystem_release`: `GCFPE-20260914.1` / `091426.1` / 55
- `prompt`: `PR-10 — Create PR Work-Unit Instructions — 091426.1`, `https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204`, fetched 2026-09-24T15:44:17Z. The page body differs from the 2026-09-21 read (two-session PR-30/PR-35 split, the "material" definition, artifact-first results and a lean handoff); this instruction follows the current body
- `role_stage`: retained whole-change IA / PR05 instruction creation
- `capture_time`: `2026-09-24T17:57:11Z`
- `result`: this `HDE-EPIC040-PR05-PR-INSTRUCTION v1.0`, `INSTRUCTION_READY`

Earlier entries are preserved in their own artifacts, including `GCFPE-USE-HDE-EPIC040-PR-40-20260922-PR04-01` in the PR04 lineage review §14. `docs/changes` holds no installed `GCFPE_PROMPT_PROVENANCE.md` procedure; repository persistence stays `PENDING / NON_GATING`.

## 16. Semantic readiness record

Compared clause by clause against the approved Specification, Plan v2.1 §§5.9, 6.5, 7.1–7.4 and 8, Plan Review v2.1, the F01 review and PF10 §2.15, the register, current repository evidence, and the current PR-20 contract at 091426.1 (re-read 2026-09-24; its only changes are the two-session split and artifact-first results).

| Source clause | Instruction meaning | Owner | Acceptance | Evidence stage |
| --- | --- | --- | --- | --- |
| Plan §5.9 / PF01 §9.5 goldens | §5.1: eight cases, full PF01 metadata and UUIDs, explicit case type, canonical bytes, input-only | PR05 | `AC040-06` | PR-30/PR-35 tests |
| Plan §5.9 comparator | §5.2: explicit root, canonical entrypoints, full comparison, every mismatch, no second formula | PR05 | `AC040-06` | PR-30/PR-35 tests |
| Plan §6.5 / PF12 4756–4760 read-only | §5.2: compare mode cannot reach write, activation or generation helpers; fails closed | PR05 | `AC040-06`, `-09` | Spies and byte snapshots |
| Plan §5.9 readiness | §5.3: read-only `DBAccess`, shared Gate predicate, no writes/acquisition, unavailable ≠ ready, no payload leakage | PR05 | `AC040-07`, `-09` | Fake-DB tests |
| Plan §6.5 evidence | §8.4: PR test/CI record; no invented family | PR05 | `AC040-08` | PR-30/PR-35 CI |
| PF10 §2.15 / F01 review §7 | §7: inherited posture; fixture root inside pytest only; real-root refusal is truthful | PR05 inherits; PR06 owns convergence | — | CI accepts `RELEASE_NOT_ADMITTED` |
| Classifier fact (new) | §6.3–§6.4: register the new path; all seven lanes will run | PR05 (coherence dependent) | — | CI classification |
| PR-10 "material" definition | §10 | Native owners | — | As arises |
| PR-20 contract | §§1–15 give bounded behavior, baseline, loci, exclusions, interfaces, dependencies, acceptance, evidence, migration, security, recovery and return owner; PF10 path and overlays in §2.1 | PR-20 | — | PR-20 |

Checked: numeric domains and sentinels are PF01's and not restated here; boolean exclusion in Gate input is `normalize_gates`'s; the fixture's closed schema is PR-20's to define against PF01; field and unit ownership are unambiguous; dependency order and evidence deadlines are unchanged. **No decisive comparison failed.** Every obligation outside PR-20's Inputs — detailed planning, implementation, security and code review, corrected-code coverage, findings and re-review, CI, manual-merge handling and completion evidence — is preserved in §§8, 11 and 12. `INSTRUCTION_READY` is set: a dedicated PR-20 session can plan PR05 from this instruction plus current repository and Canon evidence without reconstructing upstream intent.

No material scope, architecture, requirement or design boundary was found; no RS-10 route is opened. The two facts that differ from the Plan's framing — the unclassified readiness path and the resulting all-lane CI — are necessary-dependent coherence facts under §6.3, not boundaries.
