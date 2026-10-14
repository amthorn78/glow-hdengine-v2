---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-03-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: APPROVE
approval_sentinel: "ASK OK."
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
items_decided: RP-1 (approved bounded implementation delta; canon governs the dev Reader start helper), RP-3 (approved bounded implementation delta; one roster line leaves the updater), RP-2 (confirmed in scope under the base; no delta); CR-6 APPROVED (alternative (a))
request_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-request-v1.0.md (v1.0, RESCOPE_REQUEST, RESCOPE_REQUEST_PENDING_REVIEW; blob 8fa8d85b62957b39b85c2d124338ecc621bfe3f9; SHA-256 c9ed18bc27e05504647e5966f5d05ecc91e942ae0cca0c08a8d2ba44f6b5482a; 24,885 bytes; read in full)
request_author: the dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (PR-20 pre-Proceed planning), session https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, this session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (PR-10 author of the WU-PR-03 instruction v1.0; PR-40 reviewer of WU-PR-02)
author_reviewer_independence: VERIFIED (distinct sessions and roles; this IA did not author the request, the suspended plan or the prototype). Disclosure: this IA authored the instruction v1.0 whose §5.5, §6 and §9 item 5 carry the EC-4 default that RP-1 corrects, and whose §5.7 (c) RP-3 corrects (§1)
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; retrieved revision last edited 2026-10-12T02:29:57.795Z); release GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
originating_stage: PR-20 pre-Proceed planning. No Proceed, workspace vehicle or code pull request exists. PR_RETURN_PHASE: not applicable
vehicle_state_relied_on: no open pull request on amthorn78/glow-hdengine-v2 at review time (GitHub pull-request listing, state open, zero results); origin/main 852370caf88e67c260a302447811244b5365f22a (tree 8b5c8d558c93; #640 merged, carrying the request, plan v1.0 and the prototype diff); docs/pfcanon/ unchanged since ad11821 (git diff ad11821 852370c -- docs/pfcanon is empty)
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, PENDING; blob 750c700cb325b05d3d0d921b982a2f15e2872399; 83,667 bytes; preserved; its successor is plan v1.1) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff (blob 35e118cd902ae5493683e0b7bdf460b080a3472c; 72,428 bytes; preserved)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0; blob 74e8f158b48d48a70ab0be1b175096c5388e5f4b; unchanged by this decision)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE by Isis; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; lineage; origin of EC-4)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0. None is rewritten by this decision
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md (v13.5.6, effective 2026.10.14; blob 9c5468fb69e4902daf30e9c484dd5803e4f4f8b5; SHA-256 8663ab94289adae036dbb07af8b302d1b7f3b1d2a1b57dfb7bbd664a5b98bec0; 69,689 bytes; read: front matter §§1–9, cross-references, template, index §1.1, addenda 2.2 and 2.5 in full, 2.1 and 2.3 headings and rules; silent on dev Reader start helpers, APP_ENV defaults and the IF-7 roster membership; next continuous addendum number 2.6)
applicable_prior_addenda: 2.2 (WU-PR-03 downstream item, ID-4), 2.3 (review chain), 2.5 (carried LR-O1 to LR-O3). None is superseded by this decision
addendum_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md (the one PF10_BUILD_NOTES_ADDENDUM this APPROVE creates; proposed number 2.6)
checkpoint_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0-checkpoint.md
handoff_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0-handoff.md
capture_time_utc: 2026-10-14T02:40:00Z
return_to: the PR-20 planning context of the dedicated WU-PR-03 PR engineering session (the request's author), which writes plan v1.1 as a complete successor under approved base + applicable overlays + addendum 2.6 and presents it at AWAITING_PO_PROCEED
canon_conflict_register: CR-1 to CR-5 carried unchanged; CR-6 APPROVED by this review (§12)
---

# HDE-CRD-0002 WU-PR-03 — Rescope Review v1.0

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Decision and authority

**decision: APPROVE.** This is one state for the one request, and the three items resolve as follows:
- **RP-1 is approved** as a bounded implementation delta, with the binding conditions in §7.1. The dev Reader start helper keeps propagating `APP_ENV` exactly. Approved Plan text that requires a default is overlaid for WU-PR-03 by addendum 2.6.
- **RP-3 is approved** as a bounded implementation delta, with the binding conditions in §7.2. The line `artifacts/core/purity/purity_report.json` leaves the updater's `CURRENT_RELEASE_CAPTURE_PATHS`.
- **RP-2 is confirmed in scope** under the base. Convergence step 3b corrects the order inside the method Plan v1.1 §10 already approves; no overlay is needed (§5).
- **CR-6 is `APPROVED`**, alternative (a): canon governs (§12).

Both deltas are represented by exactly one PF10 addendum overlay (§9).

**Authority.** RS-20 — Review Bounded Work-Unit Rescope — 100926.1: the continuing whole-change IA reviews the originating PR author's request independently and returns the decision to that author's phase. Rescope is owned by the PR author and the IA reviewer, with no Isis hop. This authority is limited to the native `RESCOPE_REVIEW` classification within approved Specification intent. It does not:
- decide Product Owner product intent;
- approve a replacement whole-change Plan;
- authorize implementation or merge;
- edit PF10;
- restart accepted work (WU-PR-01 and WU-PR-02 stay accepted-final);
- invoke PR-50.

**Author and reviewer independence: verified.** The request's front matter and its merged pull request (#640) record its author as the dedicated WU-PR-03 PR engineering session at PR-20 (session `session_01GC6jqu4Lczzk7PR7QGXSTJ`). This IA did not author the request, the suspended plan v1.0 or the prototype diff, and reviewed all three from their merged copies on `main`.

**Disclosure.** This IA authored the PR instruction v1.0 under PR-10.
- Its §5.5 states "EC-4's default is required". Its §6 row, its §8 contract E-6 and its §9 item 5 carry the default.
- Its §16 states that ID-2 applies HDE Architecture §3.8.1 "as written". That section's "Repo-side start-helper posture" bullet forbids the default, and the instruction did not detect it.
- Its §5.7 (c) routes a stale roster label to this IA "not a roster edit".

RP-1 and RP-3 therefore correct this IA's own instruction. The review applies canon and the request's evidence on their merits, and it does not shield the instruction. A correction to an issued instruction is made by overlay; the instruction is not re-issued.

**Reading of "material".** It is the same reading as the WU-PR-01 rescope review §1, cited as precedent only.
- `APPROVE` needs "a material bounded implementation delta within approved Specification intent". This review reads that as a substantive, evidenced change to the unit's bounded loci or approved clauses that the immutable base does not authorize.
- RS-20's Epic-level "Material" marks the line beyond which the matter leaves this IA (`SPECIFICATION_CHANGE_REQUIRED` or the Product Owner).
- RP-1 and RP-3 are the first kind and not the second (§3.4, §4.4).

**PF10 read.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`:
- read: front matter §§1–9, cross-references, template, index; addenda 2.2 and 2.5 in full; addenda 2.1 and 2.3, rules;
- it is silent on dev Reader start helpers, on `APP_ENV` defaults and on which captures belong on the IF-7 label roster;
- the next continuous number is 2.6;
- addenda 2.2, 2.3 and 2.5 stay applicable to WU-PR-03 unchanged.

## 2. Vehicle state and request completeness: verified

**Stage and vehicle.** Pre-Proceed planning:
- No Product Owner Proceed, workspace vehicle or code pull request exists for WU-PR-03.
- The GitHub pull-request listing for `amthorn78/glow-hdengine-v2` with state `open` returned zero results at review time. `PR_RETURN_PHASE` is not applicable and RS-40 does not apply.
- `origin/main` is `852370c` (#640). `docs/pfcanon/` is unchanged since `ad11821`.

**Baseline difference.** The request and plan measured at `20f16d0`; this review measured at `852370c`. `git diff 20f16d0 852370c` touches only `docs/ephemeral/` (#640's three files), so every code, tool and evidence fact holds.

**Completeness against RS-20's required inputs.** The input is exactly one `RESCOPE_REQUEST` from PR-20, identified by repository path and artifact type. It carries:
- the exact findings (§1, §2, §2A, §6);
- the approved Specification, the immutable base Plan and review, and PF10 with its active addenda (front matter);
- explicit proposed deltas (§3, §3A);
- the originating stage, owner and session (front matter);
- author and reviewer lineage (front matter, §1);
- completed valid work (§7);
- affected requirements, interfaces, files, tests, release, evidence, CI, Ops, QA, downstream work and canon (§4);
- evidence (§2.1–§2.3, §2A, §6);
- risks, exclusions and unresolved facts (§8);
- the conflict, as proposed register entry CR-6 (§5);
- no prior decision or application report (none exists).

The request is complete. Two details are incomplete, and neither affects the decision:
- **Affected instruction clauses.** The request names EC-4, IF-10's last clause, acceptance (2)'s last clause and E-6. It does not list every instruction clause that restates the default: §5.5 last sentence, the §6 rows for the script, the documents and the tests, §9 item 5 "defaulting `APP_ENV=dev`", §9 item 6's example and §10's S10 evidence row "the runner-default test". §7.1 B-2 of this review lists them all.
- **LR-O2.** The request applies LR-O2 to RP-3 (§3A item 3), but plan v1.0 §17 still says "LR-O2 not triggered". Plan v1.1 must carry the request's position (§7.2 B-9).

## 3. RP-1: the dev Reader start helper's `APP_ENV` default

### 3.1 Canon, read by this reviewer on `main`

Each passage the request quotes was re-read in its source on `main` at `852370c`. Every quotation is exact.

| Source and section | What it requires |
| :- | :- |
| HDE Architecture §3.8.1 "Dev/QA Reader availability", bullet "Repo-side start-helper posture (names-only)" | Dev Reader start helpers "MUST propagate `APP_ENV` exactly as supplied by the calling environment. They do not silently default `APP_ENV`." |
| HDE Mechanics Guide §5.6, paragraph "Dev Reader start helpers (APP_ENV propagation)" | Start helpers MUST propagate `APP_ENV` as-is "including when it is explicitly set to "dev", "test", "local", "prod", an empty string, or left unset" and "MUST NOT supply a default APP_ENV value (for example, forcing APP_ENV=dev when it is empty or unset)". They may set rails, locale and `PORT`, "but it must not override the caller's choice of APP_ENV". Live QA harnesses rely on this "to exercise and verify the full set of APP_ENV modes", so that "infra start helpers do not silently mask gating bugs" |
| HDE Mechanics Guide §34 "Dev HTTP Harness (single home)", "Required start and local examples" and "Current repository posture" | The required start command is `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`. The script "propagates `APP_ENV` only when the caller supplies it". "The Reader handler treats missing `APP_ENV` as dev; that behavior does not satisfy the explicit caller-supplied `APP_ENV=dev` requirement" |
| Glow Infrastructure §8.1, the `APP_ENV` note | Infra-owned start helpers, "including dev/QA Reader start commands, MUST" propagate `APP_ENV` from the caller and "MUST NOT silently force a default when `APP_ENV` is empty or unset". The same section binds `APP_ENV=dev` for the Dev and QA environments |
| HDE Build Checklist — Conjunction, Subtask HDE-CONJ001.4 evidence | `scripts/dev_start_reader.sh` "forwards `APP_ENV` from the caller without forcing a default, exporting `APP_ENV` only when it is present" and logs `APP_ENV_DISPLAY` |
| Glow QA Guide §13.9 | "For dev Reader start helpers, silent `APP_ENV` defaulting was non-conforming. The durable posture was to propagate `APP_ENV` exactly as supplied, including unset or empty states" |
| HDE Math Spec §12, "Dev Reader harness" bullet (supporting) | "A default that treats an unset environment as development is not fail-closed" |

No PF10 addendum addresses start helpers (§1). No Product Owner disposition adjudicates EC-4: the CR-4 and CR-5 record concerns other matters. Under `AGENTS.md` (canon-first rule), HDE Governance §9.1.2 ("Follow the governing PF position immediately") and Plan Templates "Canon precedence for template use", canon governs the in-flight Plan, its review and the instruction on this point.

### 3.2 Lineage of the conflicting text

- **Origin.** EC-4 originates in the Implementation Audit v1.0 §7.1, with the rationale "S10 must not break dev use; the runner would otherwise start a refusing `/reader`".
- **Isis's review.** Isis's IA-30 review v1.0 R1 narrowed IF-10 to explicit `dev`, with a verbatim replacement cell ending "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev`", and states "EC-4's dev-runner default (`APP_ENV=dev`) stands". Review v1.1 records R1.1 as applied. That review cites HDE-CLI-API-Vendor-Ref §5.6 and HDE Schemas & Artifacts "Reader surface routes and distinct contracts (normative)". It does not cite any start-helper passage of §3.1.
- **Instruction.** This IA's instruction v1.0 carried the default (§1, disclosure).
- **Search.** No HDE-CRD-0002 record names the start-helper passages. The request's search found nothing, and this review confirmed it for the review and audit files.
- **Effect on Isis's statement.** A review governs within its scope (HDE Governance §9.1.2), and PF-Canon governs where an in-flight document conflicts with it, unless PF10 or a formally approved bounded Product Owner rescope supersedes it (`AGENTS.md`). Neither does here. Isis's statement therefore yields to canon for this clause only. Everything else in R1 stands: the explicit-`dev` gate, the catalog `env_gate`, and the refusal set of acceptance (2).

### 3.3 Code and behavior, verified by this reviewer

- **On `main`.** `scripts/dev_start_reader.sh` (26 lines) conforms already:
  - it exports `APP_ENV` only when it is set (lines 13–18);
  - it prints `[dev-start] APP_ENV=<UNSET>` otherwise;
  - it runs `exec python -m adapter.http_reader`.

  `VERIFY.sh` line 4 is `export APP_ENV=${APP_ENV:-dev}`, the forbidden example of HDE Mechanics Guide §5.6.
- **Reproduction.** A detached worktree of `852370c` in this session's scratch clone; CPython 3.12 with CI's install; closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`); vendor and database keys unset. The prototype diff applied cleanly (20 files). After the §4.2 convergence:
  - `tests/scripts/test_dev_start_reader.py` gave **10 passed**;
  - `git diff -- scripts/dev_start_reader.sh` was empty: the script is byte-unchanged under the proposed design;
  - the test's cases are as the request §2.3 states. With `APP_ENV=dev` the runner serves `GET /reader?v=1` 200. Unset prints `<UNSET>` and refuses 403 `ERR_READER_FORBIDDEN`. `test`, `local`, `prod` and empty are kept and refused. `VERIFY.sh` with `APP_ENV=dev` exits 0 with every token `_OK`. Without an explicit `dev` it exits 2 with `VERIFY_APP_ENV_NOT_DEV` before starting a runner.
- **Not repeated.** This review did not re-run the request's approved-base prototype (EC-4 default → unset serves 200). That outcome follows from the default by construction, and the request records it.

### 3.4 Boundary and classification

- **The boundary is real.** EC-4, IF-10's last clause and acceptance (2)'s last clause are approved Plan text, and instruction v1.0 binds them (§4, §6, §9 item 5, §10). Implementing canon leaves acceptance (2)'s last clause literally unmet, and implementing the clause breaks canon. Changing an approved acceptance clause is outside what PR-20 may decide alone (PR-20 "Material"). Canon precedence settles which text governs. The immutable base still needs an overlay so that plan v1.1, PR-30, PR-35, PR-40 and QA verify against the corrected clause rather than the literal approved one.
- **It is within approved Specification intent; not `SPECIFICATION_CHANGE_REQUIRED`:**
  - S10's acceptance intent concerns the route: "served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses", narrowed by R1.1 to explicit `dev`. It is unchanged and met.
  - The constraint "Dev route. S10 must not break dev, test or local use of `/reader`" is met. Dev use as canon defines it supplies `APP_ENV=dev` (HDE Mechanics Guide §34 required command; Glow Infrastructure §8.1 binds `dev` for the Dev and QA environments), and that use keeps serving.
  - `test` and `local` were already refused on `main` (Isis R1).
  - A caller who omits `APP_ENV` gets a visible refusal (`APP_ENV=<UNSET>` banner, 403), which is the state canon requires to stay observable.
  - The Specification does not mention the default.
- **It is not Material** in RS-20's Epic-level sense. It changes no Specification outcome or acceptance criterion; no protected architecture, security, data-model or external-contract boundary; no other unit's scope; no accepted dependency; and no budget, schedule or risk needing Product Owner direction. It touches no release member, governed artifact, public route or production behavior. `scripts/dev_start_reader.sh` and `VERIFY.sh` are not members, and the script does not change.
- **Not `IN_SCOPE_REPAIR`.** The request offered `IN_SCOPE_REPAIR` "if the IA reads canon precedence as already authorizing it". Canon precedence decides which text governs, but the base itself expressly requires the default. HDE Governance §9.1.2 permits correcting lower-authority material "only when the edit is authorized"; otherwise it requires reporting and stopping. That is the request's posture, and an overlay is the authorized correction. The immutable base plus its overlays (2.2, 2.3, 2.5) does not already authorize it.

### 3.5 Alternatives

| Alternative | Disposition |
| :- | :- |
| (a) Canon governs. The script stays unchanged; IF-10, acceptance (2), E-6, the instruction clauses, the documents and the owner test state propagation; `VERIFY.sh` refuses unless `APP_ENV=dev` | **Approved**, with §7.1 |
| (b) Keep EC-4 under a formally approved bounded Product Owner decision superseding canon for this script (the CR-4 pattern), with drainage of six passages | Not taken. It is outside this IA's authority, and nothing recommends it. It would mask the unset mode that HDE Mechanics Guide §5.6 says QA harnesses rely on. The Product Owner may still raise it; this decision does not foreclose it |
| (c) As (a), but `VERIFY.sh` keeps `${APP_ENV:-dev}` because it is the caller | Rejected. `VERIFY.sh` starts the runner through the start helper, so its default is upstream of the helper and defeats the propagation contract. It is the literal example HDE Mechanics Guide §5.6 forbids. A loud refusal neither defaults nor overrides the caller's choice; `VERIFY.sh` declines to run its dev-only checks in any other mode |
| (d) `VERIFY.sh` propagates silently, with no refusal | Rejected. Without `APP_ENV=dev` every `VERIFY.sh` check would fail on 403s with no stated cause. The refusal is the same contract made explicit |

## 4. RP-3: the IF-7 label roster keeps a stale label on a byte-stable capture

### 4.1 Code and data, verified at `852370c`

- **The roster's own criterion.** `tools/evidence/update_evidence_index.py` lines 56–61 state the criterion: "Mirror rows for primaries whose bytes the admitted release determines carry a release label … a release change alone never relabels a capture". `CURRENT_RELEASE_CAPTURE_PATHS` (lines 62–86) lists 23 paths.
- **The purity report.** `artifacts/core/purity/purity_report.json` has the keys `behavioral_guard_exit_code`, `behavioral_guard_passed`, `env`, `fixture_kind`, `generated_at_utc`, `modules`, `schema` and `source_sha256`.
  - `generated_at_utc` is fixed at `2026-09-26T15:42:11Z`.
  - `source_sha256` binds exactly 12 sources: `catalog/magic10_mechanics_v1.json`, `engine/bodygraph/gates.py`, `engine/config/registry_loader.py`, `engine/core/__init__.py`, `engine/core/core.py`, `engine/magic10/{__init__,calculators,composite,signals}.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py` and `schemas/magic10_result_v1.schema.json`.
  - It contains no `release_id` and does not bind `catalog/manifest.json`.
  - The prototype diff touches none of the 12 sources.
- **The other roster captures.** Eight contain the current `release_id` literally (the catalog logs, three engine-core captures, the F07 writer pair, parity `ab`/`ba`). The rest are Reader or CLI bytes, digests of them, or gate logs that hash artifacts containing it. All of them are therefore bound to the release, directly or through the bytes they record. The purity report is the only roster member whose inputs are source files alone.
- **The tests.** `tests/evidence/test_evidence_index_missing_state.py`:
  - `test_current_release_capture_rows_are_labeled_and_frozen_rows_are_not` (line 1100) asserts that every Mirror row on the roster ends with the label of the current `catalog/manifest.json`;
  - `test_release_labels_follow_regenerated_captures_through_the_updater_alone` (line 1143) asserts the same through a copied repository;
  - `test_unlabeled_capture_rows_take_the_admitted_release_on_adoption` (line 1181) asserts that relabelling reproduces the Index byte for byte.

  These are WU-PR-02's accepted contract. A roster capture that does not change bytes when the release changes cannot satisfy them after any re-cut that leaves its inputs unchanged.

### 4.2 Reproduction by this reviewer

Same worktree and environment as §3.3, with the prototype diff applied but the updater restored to `main` (roster with the purity line). Steps:
1. **Cut.** `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` exit 0, then `scripts/release_id_recompute.py --check-manifest-only` exit 0. The manifest SHA-256 is `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f`, equal to the plan's rehearsal-3 value, so the prototype is reproducible.
2. **Engine-core owner, before step 3b.** `tools/evidence/generate_engine_core_evidence.py` rewrote `two_run/identity.json`, `abba/ab_ba_parity.json` and `json_compare/core_result_json_compare.json`; `purity/purity_report.json` was **byte-identical**. The owner then exited 1, because its internal updater run raised `ValueError: aux narrative catalog invalid`. This independently confirms F-2 and RP-2 (§5).
3. **Convergence.** Plan v1.0 §6.10 steps 3b to 8 in order, each exit 0:
   - A7 write and `--check`;
   - canonical JSON gate and `--check-only`;
   - updater and `--check`;
   - config `--publish-family` and updater `--check`;
   - A7 re-run, determinism gate proofs, open-rails ABBA in fixture mode (`SAFE_MODE=0 ALLOW_NETWORK=1`, keys absent) with `FROZEN_OPEN_ABBA_SHA256` set to the new digest, F07 writer, engine-core;
   - updater and `--check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`.
4. **Stale label.** The Mirror held 28 labelled rows. Exactly one carried a `release_id` other than `72fca4c3…`: `artifacts/core/purity/purity_report.json` with `52be4558…`.
5. **Tests with the line present.** The three tests of §4.1 gave **3 failed** (`-k` selection, 59 deselected).
6. **The fix.** Removing exactly that roster line (one deletion) and running the updater once gave exit 0. The Index and Mirror changed only on the purity row, whose `notes` field was dropped, and, in the Mirror, on the three self-record and sentinel rows that follow from it (`docs/evidence/INDEX.sha256`, `index.human_index`, `index.machine_mirror`). 620 Index rows before and after; one differing row.
7. **Validators after the fix,** each exit 0: `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh` and `check_final_lf.sh`.
8. **Tests after the fix.** `tests/evidence/test_evidence_index_missing_state.py` and `tests/evidence/test_engine_core_evidence.py` together gave **74 passed** (757 s).

**Not executed by this review:** a full `tests/` sweep. The request records one (4,747 passed, 3 skipped, 2 xfailed, 0 failed), and §7.2 B-9 binds PR-30 to run it.

### 4.3 The roster entry was a WU-PR-02 defect, and fixing it here restarts nothing

- **Origin.** The purity report fails the roster's own stated criterion, and WU-PR-02's own tests make that failure a CI blocker at the first same-version refresh. Lineage review v1.0 §7 LR-O3 (carried by addendum 2.5) recorded the general case: a stale label stays on a byte-stable capture. It did not examine roster membership path by path, and this IA's instruction §5.7 (c) routed the case here.
- **Accepted-final work stays final.** WU-PR-02 stays accepted. This is a prospective one-line change landed by a later unit, not a reopening, rerun or relabelling of WU-PR-02's delivery. Specification S12 ("Current-release captures carry current-release labels") and IF-7 ("Rows for captures the current release regenerates carry release-identifying fields") stay met. A capture that the release does not determine carries no release claim, which is the honest state. A stale claim is the S12 defect class.

### 4.4 Boundary and classification

- **The boundary is real.** Instruction v1.0 §6 says the updater is "expected to stay unchanged". §5.7 (c) says a stale label "is a finding to the IA … not a roster edit". §14 lists "a change needed outside §6 (in particular to … the updater …)" as a rescope trigger.
- **No lawful in-scope disposition exists:**
  - A hand edit of the Mirror row is forbidden (`AGENTS.md`, no manual edits to evidence indexes).
  - The engine-core owner cannot change the bytes without changing the schema.
  - Changing the tests would weaken WU-PR-02's accepted contract.
  - Red evidence-lane CI fails acceptance (7).
- **Classification: a bounded implementation delta, not Material.** One non-member tooling line. No Specification outcome, acceptance criterion, protected boundary, other unit's scope or dependency changes. No release member, public route or runtime behavior is touched. Specification S12 and S22 are "Not production-affecting".

### 4.5 Alternatives

| Alternative | Disposition |
| :- | :- |
| (a) Remove the one roster line; the updater itself unlabels the row; LR-O2 sweep | **Approved**, with §7.2 |
| (b) Add release identity to the purity report so that it regenerates at every release change | Rejected. It is larger: an `engine_core_purity_report.v1` schema change, changed tests, and a new meaning for an engine-core evidence family that binds sources by design. Not the smallest safe scope |
| (c) A separate IA pull request lands the line before WU-PR-03 | Rejected. The content is identical, but it adds a PR and a merge dependency. An IA landing code is also not this IA's lane (PR-10 issues instructions; the PR engineering session implements) |
| (d) Accept red evidence-lane CI | Rejected. Fails acceptance (7) and the drive-to-green obligations |

## 5. RP-2: convergence step 3b, confirmed in scope (no delta)

- **Evidence.** `update_evidence_index.py::_validate_epic038_pr02_semantics` calls the A7 owner's `validate_catalog` on the tracked catalog (request §6; plan F-2). With the unit's new validator, every updater run refuses until the A7 owner has rewritten the catalog. This review observed that refusal independently (§4.2 item 2: `ValueError: aux narrative catalog invalid` from the engine-core owner's internal updater call). With step 3b, every step 3b to 8 exited 0 (§4.2 item 3).
- **Classification: `IN_SCOPE_REPAIR`, recorded inside this single `APPROVE` state.**
  - Plan v1.1 §10 approves the method: the commands, the owners, regeneration before the updater and byte stability on a second run. Running the A7 owner once earlier uses the same command and owner and keeps step 7's run, which is then byte-stable. Instruction §6 already bounds the A7 owner and its regenerated family.
  - No acceptance intent, boundary, unit or dependency changes. It is a sequencing correction needed to deliver acceptance (7) within the approved method.
  - The restart point for an evidence-primary change becomes 3b, as plan v1.0 PD-15 states.
- **Not in the addendum.** The addendum records RP-2 as in scope under the base; it carries no delta for it.

## 6. Evidence against each excluded decision

| Excluded decision | RP-1 | RP-3 | Request as a whole |
| :- | :- | :- | :- |
| `REJECT` | Canon is unambiguous across six binding passages in five documents (§3.1). The script already conforms and is unchanged (§3.3). The change is safe (no member, governed artifact, public route or production behavior) and within this IA's authority (§3.4) | Reproduced (§4.2). It is the only lawful route to acceptance (7) (§4.4). One non-member line, safe (§4.2 items 6 to 8) | Not rejected |
| `REVISION_REQUIRED` | The evidence, the delta and the effects are precise. The two incompletenesses of §2 are closed by §7.1 B-2 and §7.2 B-9 without new evidence from the author | The fix is prototyped and independently reproduced, with its validators and tests | Not required |
| `SPECIFICATION_CHANGE_REQUIRED` | S10's acceptance intent and the "Dev route" constraint are unchanged and met (§3.4); the Specification does not mention the default | S12's criterion is unchanged and met (§4.3) | Not required |
| `IN_SCOPE_REPAIR` | The base expressly requires the default; correcting approved text needs an authorized overlay (§3.4) | The base excludes the updater (§4.4) | Not the whole request's state. RP-2 alone is in scope (§5) |

## 7. Binding conditions

These bind PR-20 plan v1.1, PR-30 and PR-35 for WU-PR-03. Instruction v1.0 stays as issued. Addendum 2.6 overlays the clauses named here and nothing else; everything else in the instruction holds, together with addenda 2.2, 2.3 and 2.5.

### 7.1 RP-1

- **B-1 Script.** `scripts/dev_start_reader.sh` is not changed. It leaves the hand-edited set. Its `git diff` from base to head is empty.
- **B-2 Overlaid clauses.** For WU-PR-03 the following read as stated, and every other word of each clause holds:
  - Plan v1.1 §5 IF-10, last clause, and instruction §4 IF-10 quotation: "`scripts/dev_start_reader.sh` propagates `APP_ENV` exactly as the caller supplies it, including unset and empty, and never defaults it; the canonical start command supplies `APP_ENV=dev`."
  - Audit EC-4 (instruction §4) is not implemented. Its documentation clause becomes: `docs/server/reader_v1.md` states the start command `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV`.
  - Plan v1.1 §7 WU-PR-03 acceptance (2), last clause, and instruction §10 acceptance (2): "`scripts/dev_start_reader.sh` with `APP_ENV=dev` starts a serving runner; with `APP_ENV` unset or empty it propagates that state and the runner refuses `GET /reader` (403 `ERR_READER_FORBIDDEN`)."
  - Plan v1.1 §7 WU-PR-03 "Deliverables", item "`scripts/dev_start_reader.sh` (default `APP_ENV=dev`)": withdrawn. The script is not a deliverable; its owner test is (B-4).
  - Instruction §5.5, last sentence: superseded by this decision. After S10, an unset `APP_ENV` starts a runner whose `/reader` refuses. Canon requires that, and the canonical start command supplies `APP_ENV=dev`.
  - Instruction §6:
    - the `scripts/dev_start_reader.sh` row becomes "unchanged (canon: propagate exactly)";
    - in the documents row, "S10 gate and runner default" becomes "S10 gate and the start command with `APP_ENV=dev`";
    - in the tests row, "the runner-default test" becomes "the runner propagation test".
  - Instruction §8 contract E-6: "`/reader` served only for `APP_ENV=dev`. The runner propagates `APP_ENV` exactly and the caller supplies `dev`. `VERIFY.sh` uses the canonical runner and requires `APP_ENV=dev`."
  - Instruction §9 item 5: "defaulting `APP_ENV=dev`" becomes "with the caller's `APP_ENV=dev`, refusing otherwise (B-3)". Item 6's example becomes a test that runs the script with `APP_ENV` unset and observes propagation and the refusal.
  - Instruction §10, S10 evidence row: "the runner-default test" becomes "the runner propagation test".
- **B-3 `VERIFY.sh`.** Line 4 `export APP_ENV=${APP_ENV:-dev}` is replaced as follows:
  - unless the caller supplies exactly `APP_ENV=dev`, it refuses before starting a runner, printing `VERIFY_APP_ENV_NOT_DEV` with the effective value (or `<UNSET>`), and exits 2;
  - otherwise it passes `APP_ENV` unchanged to the start helper;
  - no default is supplied anywhere in `VERIFY.sh`;
  - its other checks are as instruction §9 item 5 and plan v1.0 §6.4 state.
- **B-4 Owner test.** `tests/scripts/test_dev_start_reader.py` stays the ID-3 owner of `scripts/dev_start_reader.sh`; ID-3's four keys are unchanged. The test proves:
  - `APP_ENV=dev` serves;
  - unset prints `APP_ENV=<UNSET>` and refuses 403 `ERR_READER_FORBIDDEN`;
  - empty, `test`, `local` and `prod` are kept and refused;
  - `VERIFY.sh` with `APP_ENV=dev` exits 0 with every token `_OK`;
  - `VERIFY.sh` without an explicit `dev` (unset, empty, `test`) exits 2 with `VERIFY_APP_ENV_NOT_DEV` before any runner starts.

  It needs `bash` and `curl`; plan v1.1 records both as visible test dependencies.
- **B-5 Documents.** `docs/server/reader_v1.md` and `docs/acceptance/reader_a7_crib.md` state the start command `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV`. No other document changes for RP-1. `AGENTS.md` and `README.md` stay with WU-DOC-01 (plan OBS-P3-8).
- **B-6 Unchanged.** The `/reader` gate design (IF-10's first part), the catalog `env_gate` (`APP_ENV=dev`), acceptance (2)'s refusal set, IF-6, IF-11 and the members are unchanged.

### 7.2 RP-3

- **B-7 Locus.** `tools/evidence/update_evidence_index.py` joins the bounded files for exactly one change: delete the line `"artifacts/core/purity/purity_report.json",` from `CURRENT_RELEASE_CAPTURE_PATHS`. The roster then holds 22 paths. These do not change:
  - any other line, the roster comment, `_current_release_labels`, the label pattern or `_strip_current_release_label`;
  - `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` or any other refusal, the write paths, the schema, the admitted-CRD table or the catalog validation call.

  Instruction §5.7 (c) is overlaid for this path only. For any other roster capture, a stale label after a refresh stays a finding to this IA, never a roster edit.
- **B-8 Publication by the updater only.** The label is removed by the updater's own runs in the convergence: step 5, and step 8 thereafter. No governed artifact is hand-edited. After step 8:
  - the purity row of the Index and the Mirror has no `notes` field;
  - every other roster row carries the new release's label;
  - the step-11 sweep finds no purity-report hit.
- **B-9 LR-O2 applies.** The updater changes, so every test file that imports or runs it runs in the full-validation run: the full `tests/` sweep under closed rails with `ruby` on `PATH`, ending with a clean tree. Plan v1.1 replaces plan v1.0 §17's "LR-O2 not triggered" with this. The PR result record names each check with its counts.
- **B-10 Honest record.** The PR result record:
  - states the roster change, its reason (the capture binds engine-core sources, not the release) and the one row it unlabels;
  - carries the nonclaim that the purity report is not a release-bound capture;
  - cites this review;
  - does not represent the change as a modification of WU-PR-02's accepted delivery.

### 7.3 Common

- **B-11 Unchanged obligations.** Everything else in instruction v1.0 holds, as do the plan v1.0 work this decision preserves (§8) and addenda 2.2, 2.3 and 2.5:
  - acceptance (1) and (3) to (7);
  - contracts E-1 to E-5 and E-7 onward;
  - ID-1 to ID-4;
  - exclusions, nonclaims, evidence obligations and the PR-30/PR-35 split.
- **B-12 New boundary.** Any further change outside instruction §6 as extended here is a new finding to this IA through the rescope lane.

## 8. Effects and preserved work

| Surface | Effect |
| :- | :- |
| Requirements | S10 and S09 are met within their approved intent. S12 is met (§4.3). No other requirement is touched |
| Acceptance | WU-PR-03 (2)'s last clause as B-2. (1) and (3) to (7) unchanged |
| Interfaces and contracts | IF-10's last clause and E-6 as B-2. IF-6, IF-7's model, IF-11 and the other contracts unchanged |
| Files | `scripts/dev_start_reader.sh` leaves the changed set. `tools/evidence/update_evidence_index.py` joins it for one line. `VERIFY.sh`, the two documents and the owner test as B-3 to B-5 |
| Tests | No test assertion changes other than the owner test's content (B-4) |
| Release | No member change beyond the unit's own (`adapter/http_reader.py`, `engine/cli/main.py`). The refresh is unchanged. The updater and the scripts are not members |
| Evidence | One Index and Mirror row loses a stale label through the updater. The families regenerated are unchanged from plan v1.0 §6.10 |
| CI | The updater is an evidence-lane path. The PR already selects all seven lanes through the ID-3 classifier change. B-9 adds the full sweep the plan already runs |
| Ops and QA | QA-10's S10 Live QA step and WU-OPS-01 use the canonical start command with an explicit `APP_ENV`. The unset refusal stays observable through the runner (HDE Mechanics Guide §5.6) |
| Downstream | WU-PR-04 and WU-PR-05 refreshes no longer hit the purity label. WU-PR-08's version bump changes `engine/config/registry_loader.py`, so it regenerates the purity report unlabelled. WU-DOC-01 states the start command with `APP_ENV=dev` (OBS-P3-8) |
| Canon | None changes. Doc-delta candidates are in §10 |

**Preserved work.** The following stand, and plan v1.1 is a complete successor that changes only what this decision requires:
- plan v1.0's baseline re-verification (§4.1) and facts F-1 to F-14;
- the S02, S07, S09, S15 and S18 designs, ID-3 and ID-4, and PD-1 to PD-23;
- the three rehearsals and the final full sweep;
- the prototype diff, which already contains the approved RP-1 design and the RP-3 line.

## 9. PF10 overlay

One addendum, `docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md`, proposed as PF10 addendum 2.6, the next continuous number after 2.5 in v13.5.6.
- Applicable prior addenda: 2.2, 2.3 and 2.5. None is superseded.
- Its approved delta is RP-1 (§7.1) and RP-3 (§7.2). It records RP-2 as in scope under the base.
- Lineage: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0 → this review → the addendum.
- PF10 is not edited. Numbering and publication are the Product Owner's.
- From this decision onward, the effective baseline for WU-PR-03 is the approved base plus addenda 2.2, 2.3 and 2.5 plus this addendum.

## 10. Observations returned to the Product Owner, and obligations this IA carries

- **To the Product Owner: doc-delta candidates (canon; not edited here).**
  - HDE Mechanics Guide §34 "Current repository posture": after S10, its bullet "The Reader handler treats missing `APP_ENV` as dev" becomes stale.
  - HDE Architecture §3.8.1 "Current repository discrepancy" and the HDE Math Spec dev-harness bullet, already listed by instruction §15 (ID-2).

  These add to the candidates of instruction §15 and plan v1.0 §17.
- **To the Product Owner: CR-6 alternative (b).** It is not recommended and not foreclosed. If the Product Owner prefers the default, that is a Product Owner decision superseding canon, with drainage of the six passages. Otherwise CR-6 needs no drainage.
- **IA-carried, at PR-10 for later units:**
  - WU-PR-04, WU-PR-05 and WU-PR-08 apply the 22-path roster. LR-O3 (a stale label on any remaining roster capture is a finding) still applies.
  - OBS-P3-7 (step 3b whenever a unit changes the catalog validator).
  - OBS-P3-5 (WU-PR-06).
  - OBS-P3-1, OBS-P3-4 (WU-PR-05) and OBS-P3-8 (WU-DOC-01).
  - OBS-P3-2, OBS-P3-3 and OBS-P3-6 stay recorded with this IA as owner and are routed at the next applicable instruction or to the Product Owner. They block nothing here.
- **IA lesson, recorded.** Instruction §16 claimed coverage of HDE Architecture §3.8.1 "as written" while missing its start-helper bullet. Later instructions name the exact bullets read, not only section numbers.

## 11. Return

The decision returns to the PR-20 planning context of the dedicated WU-PR-03 PR engineering session, the request's author. That session writes plan v1.1 as the complete successor of the suspended plan v1.0, under the approved base plus addenda 2.2, 2.3, 2.5 and this addendum (`AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`). Plan v1.1:
- carries the `CANON_CONFLICT_REGISTER` with CR-6 as decided here;
- unblocks PD-7 and PD-24 and maps §7's conditions into its per-file table, implementation sequence, validation plan and acceptance evidence;
- is presented at `AWAITING_PO_PROCEED` when complete and executable.

This decision creates no Proceed, vehicle, branch or pull request for code, and grants no implementation or merge authority. The Product Owner merges the pull request carrying this review and the addendum to `main` before PR-20 resumes.

## 12. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried from the approved Specification, Plan, instruction and plan v1.0:

- **CR-1, CR-2, CR-3** (CANON_RECONCILIATION): `APPROVED_AS_CHANGED` (Thoth, Specification lineage). Not affected.
- **CR-4**: `APPROVED`, and **CR-5**: `APPROVED_AS_CHANGED` (Product Owner, `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 and §3). Not affected.
- **CR-6**, decided by this review:

| Field | Value |
| :- | :- |
| ID | CR-6 |
| Classification | CANON_RECONCILIATION (an approved in-flight Plan item contradicts current canon) |
| Sources and versions | Plan v1.1 §5 IF-10 (last clause) and §7 WU-PR-03 acceptance (2) (last clause); Audit v1.0 §7.1 EC-4; Plan review v1.0 R1 item 1 and its statement "EC-4's dev-runner default (`APP_ENV=dev`) stands"; instruction v1.0 §4, §5.5, §6, §8 E-6, §9 items 5 and 6, §10. Versus, on `main` at `852370c`: HDE Architecture v2.4.6 §3.8.1; HDE Mechanics Guide v3.5.8 §5.6 and §34; Glow Infrastructure v2.3.3 §8.1; HDE Build Checklist — Conjunction v1.3.1 HDE-CONJ001.4; Glow QA Guide v3.0.6 §13.9; HDE Math Spec v1.3.8 §12 (supporting) |
| Statement | The approved Plan requires the dev Reader start helper to default `APP_ENV=dev`; canon requires it to propagate `APP_ENV` exactly and never default it |
| Affected requirements | S10 (acceptance (2)'s runner clause); S09 (`VERIFY.sh` launches the runner) |
| Alternatives | (a) canon governs, with the bounded delta of §7.1; (b) a Product Owner decision superseding canon for this script, with drainage of six passages; (c) as (a), but `VERIFY.sh` keeps its own default |
| Recommended disposition | (a) |
| Decision | **`APPROVED`**, alternative (a) as bound by §7.1 (addendum 2.6). (b) and (c) are not taken (§3.5) |
| Interim treatment | until this review merges, plan v1.0's runner item stays BLOCKED; no implementation exists |
| Unresolved risk | none. An operator who omits `APP_ENV` gets a refusing runner, made visible by the banner and the documents |
| Permanent drainage | none: canon is unchanged. The Plan's conflicting clauses are overlaid for WU-PR-03 by addendum 2.6. The doc-delta candidates of §10 are separate |
| Reviewer and session | the continuing whole-change IA for HDE-CRD-0002 through RS-20; https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| Reviewed artifact | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-request-v1.0.md` v1.0 §5 (blob 8fa8d85b6295) |
| Decision time | 2026-10-14T02:40:00Z |
| Rationale | §3.1 to §3.4: canon is explicit and consistent; no PF10 rule or Product Owner rescope supersedes it; the Specification's intent and constraint are met; the overlay is the authorized correction |
| History | PROPOSED by the request v1.0 (2026-10-14T02:01:29Z); APPROVED by this review |

## 13. Working-state note and recovery

- **Attempt:** 1 of this RS-20 invocation. No prior RS-20 result exists for this request.
- **State:** the review, addendum, checkpoint and handoff were written under `docs/ephemeral/` on this session's working branch, committed, pushed and read back. One pull request is opened for the Product Owner to merge. No Notion write; no repository write outside `docs/ephemeral/`.
- **Reproducibility:** the §3.3 and §4.2 runs used a detached worktree of `852370c` in this session's scratch clone, CPython 3.12 with CI's install and closed rails. Commands are as listed there. Never run them in a working tree that must stay clean: the convergence rewrites governed files.
- **Interruption:** if the carrying pull request is not merged, the Product Owner merges it, and nothing is re-run. If re-entry is needed, the four artifacts on `main` are the complete state.

## 14. TypeSafe reading and surface advice for the receiving session (PR-20, WU-PR-03 plan v1.1)

Action sent (v6): "Revise, as the dedicated PR engineering session that authored it, an existing 84 KB detailed PR implementation plan, not yet reviewed, for the third unit of an approved CRD Implementation Plan (public, dev and CLI surfaces across about twenty hand-edited files plus about sixty owner-regenerated evidence files after a same-version release re-cut) into a complete successor that applies one approved bounded rescope: a dev start script keeps propagating its environment variable instead of defaulting it, with the related acceptance clause, verify script, two documents and an owner test restated; one line leaves an evidence updater's label roster; and an added convergence step is confirmed. The prior plan's design is already prototyped and its full test sweep passed, the review's binding conditions are the task list, and every changed clause must be carried exactly. No code is merged and no live provider call occurs; a Product Owner Proceed, implementation, and independent code and lineage reviews follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 1.97 (confidence 0.78).
  - Rung probabilities: low 0.00, medium 0.19, high 0.67, extra high 0.14, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.99 (confidence 0.98).
  - Twelve cells, computed from the two answers:
    - Opus 5.5 at low 0.00, Opus 5.5 at medium 0.19, Opus 5.5 at high 0.66, Opus 5.5 at extra high 0.14, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00;
    - Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00.
  - Sent 2026-10-14T02:24:46Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T02:24:46Z; HTTP 200 in 0.63 s; 4307 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- No Notion row was written. **Nathan's pick for PR-20 (plan v1.1):** not stated. **Nathan's pick for this RS-20 session:** not stated (the request's own reading for RS-20 stands as recorded in plan v1.0 §20).

**Surface advice:**
- Resume PR-20 in the dedicated WU-PR-03 PR engineering session's planning context, as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt. It writes plan v1.1 as a complete successor file and does not edit plan v1.0 or its prototype diff. It may write a successor diff if its design changes.
- What it re-checks before presenting `AWAITING_PO_PROCEED`: the prototype already contains the approved design. Plan v1.1 restates every clause of §7.1 B-2 exactly and states the B-9 full sweep. Re-running the rehearsal is optional. A re-run needs a Python 3.12 environment with CI's install, `ruby`, `bash` and `curl`, closed rails and a scratch worktree.
- What it needs: no live vendor, production or database access; the carrying pull request merged first.

## 15. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / RS-20 / WU-PR-03 / rescope review 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 |
| work unit | WU-PR-03; S09, S10 (RP-1); S12 contract (RP-3); convergence (RP-2) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; retrieved revision last edited 2026-10-12T02:29:57.795Z. Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (retrieved revision last edited 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA / RS-20 review of a PR-20 pre-Proceed request |
| capture time | 2026-10-14T02:40:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| earlier entries | instruction v1.0 (PR-10, this session); plan v1.0 and request v1.0 (PR-20, session_01GC6jqu4Lczzk7PR7QGXSTJ); each holds its own entry |
| repository persistence | PENDING / NON_GATING (no `docs/changes/GCFPE_PROMPT_PROVENANCE.md` on `main`); recorded here only; authorized owner: a repository writer under an installed procedure, when one exists |

## Canon relied on

Read on `main` at `852370c` (`docs/pfcanon/` unchanged since `ad11821`). Each decision topic is mapped to the sections read.

- **Rescope authority, decision matrix, materiality, addendum contract, routing (§1, §6, §9, §11):**
  - RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (Notion, read in full; the governing procedure).
  - PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion; the same revision read in full for the WU-PR-01 rescope review and re-fetched here; the receiver contract and "Material").
  - PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (detailed PR plan, hold label, Proceed per plan) and §9.1.2 "Canon precedence and persistent sources" (read in full: follow the governing PF position; correct lower-authority material only when authorized, otherwise report and stop; in-flight reviews govern within their scope).
  - PF06-Canon-Change-Process-Guide v2.5.4 §0.1A "Governing lanes, common lifecycle, and authority routing" (Build Notes recording).
  - PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" (the precedence rule; the addendum form: next continuous H2, H3-or-deeper children, page-ready, no role-addressed instructions; Build Notes cited by title only in PF prose).
  - `AGENTS.md` canon-first rule.
- **PF10 and addendum numbering (§1, §9):** PF10-HDE-Build-Notes v13.5.6. Read: front matter §§1–9, cross-references (titles only inside the file), the template, §1.1 index, addenda 2.2 and 2.5 in full, and addenda 2.1 and 2.3 (rules). Silent on both items; the next number is 2.6.
- **RP-1 subject matter (§3), read on `main`:**
  - PF02-Canon-HDE-Architecture v2.4.6 §3.8.1 in full;
  - PF14-Canon-HDE-Mechanics-Guide v3.5.8 §5.6 (the dev sampler gating and start-helper paragraphs) and §34 "Required start and local examples" and "Current repository posture";
  - PF07-Canon-Glow-Infrastructure v2.3.3 §8.1 `APP_ENV` entry and note;
  - PF09.4-Canon-HDE-Build-Checklist-Conjunction v1.3.1 HDE-CONJ001.4 evidence block;
  - PF19-Canon-Glow-QA-Guide v3.0.6 §13.9 learnings (the start-helper bullet and its neighbours);
  - PF01-Canon-HDE-Math-Spec v1.3.8 §12 "Dev Reader harness" bullet.

  HDE-CLI-API-Vendor-Ref §5.4 and §5.6 and HDE Schemas & Artifacts "Reader surface routes and distinct contracts (normative)" were not re-read here. They govern the gate itself, which this decision leaves unchanged, and are relied on only as recorded by Plan review v1.0 R1.
- **RP-3 subject matter (§4):** HDE Schemas & Artifacts §8.3 Mirror `notes` key, relied on as recorded by WU-PR-02 lineage review v1.0 and PF10 addendum 2.5; not re-read here; the label key set is unchanged. Repository code and tests read directly: the updater lines 50–90 (comment lines 56–61, roster lines 62–86); `tests/evidence/test_evidence_index_missing_state.py` lines 1085–1230. `AGENTS.md`: no manual edits to evidence indexes; the updater is the sole writer.
- **In-flight documents:**
  - Specification v1.1 (rows S09, S10, S12; constraint "Dev route"; classification table);
  - Implementation Audit v1.0 (S10 section; §7.1 EC-4);
  - Implementation Plan v1.1 (§5 IF-7 and IF-10; §7 WU-PR-02 deliverables; §7 WU-PR-03 deliverables and acceptance);
  - Plan review v1.0 R1 and review v1.1 (R1.1, R1.2 applied);
  - PR instruction v1.0 (§4, §5.5, §5.7, §6, §7, §8 E-6, §9 items 5 and 6, §10, §14, §15, §16);
  - PR implementation plan v1.0 (§1, §4, §5, §6.4, §6.7 to §6.10, §7, §8, §14 to §17) and its prototype diff (file list; applied in full for §4.2);
  - rescope request v1.0 (in full);
  - WU-PR-01 rescope review v1.0 and its addendum (precedent form only);
  - PO disposition CR-4/CR-5 (register only).
- **Silence and searches:**
  - `grep -n -i 'start helper\|start-helper' docs/pfcanon/*.md` finds the passages of §3.1, PF12 and PF14 evidence-list mentions of a historical HDE-EPIC029 helper snapshot, and a PF20 historical entry. None conflicts.
  - `grep -n -i -E 'dev_start_reader|start helper|purity_report|CURRENT_RELEASE_CAPTURE' docs/pfcanon/PF10-*.md` finds nothing.
  - No canon assigns the purity report to a release-label set. The roster is IF-7 implementation (Plan v1.1), so RP-3 is decided on the roster's own stated criterion and WU-PR-02's tests.

---

**Status:** `RESCOPE_REVIEW` v1.0, decision `APPROVE`, one request, three items: RP-1 an approved delta, RP-3 an approved delta, both in addendum 2.6; RP-2 in scope under the base. CR-6 `APPROVED`. Returns to the PR-20 planning context of the dedicated WU-PR-03 PR engineering session.

ASK OK.
