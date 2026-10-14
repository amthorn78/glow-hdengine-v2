---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-03-RESCOPE-1
proposed_pf10_number: "2.6 (next continuous number after addendum 2.5 of the current controlled PF10; allocation and publication are the Product Owner's)"
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (RS-20; selected version 100926.1, release GCFPE-20261009.1; https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c)
approval_decision: HDE-CRD-0002-WU-PR-03-RESCOPE-REVIEW v1.0, decision APPROVE, docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md
immutable_base: HDE-CRD-0002-SPECIFICATION v1.1 (SPECIFICATION_APPROVED, Thoth CF-C-30; docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md) → HDE-CRD-0002 Implementation Plan v1.1 (approved by IA-30 review v1.1, Isis; docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md and docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md) → HDE-CRD-0002 WU-PR-03 PR instruction v1.0 (IA, PR-10; docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md)
applicable_prior_addenda: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md §2.2 (WU-PR-03 downstream item); §2.3 (review chain); §2.5 (carried LR-O1 to LR-O3). None is superseded
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md (v13.5.6; blob 9c5468fb69e4902daf30e9c484dd5803e4f4f8b5; front matter, index and addenda 2.2 and 2.5 read in full at creation; provenance, not a gate)
originating_request: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-request-v1.0.md (RESCOPE_REQUEST v1.0, items RP-1, RP-3 and RP-2, from the dedicated WU-PR-03 PR engineering session at PR-20 pre-Proceed planning)
return_phase: PR-20 planning context of the dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (pre-Proceed; no Proceed, vehicle or pull request for code exists; PR_RETURN_PHASE not applicable)
capture_time_utc: 2026-10-14T02:40:00Z
normalized_approved_delta_digest: not computed (no governed normalization procedure exists; none is invented)
---

## 2.6 HDE-CRD-0002 WU-PR-03: the dev Reader start helper keeps propagating APP_ENV exactly, as canon requires, and the engine-core purity report leaves the current-release label roster

Timestamp: 101426 02:40 (UTC) Details: Records the whole-change Implementation Agent's approval, through Review Bounded Work-Unit Rescope, of one bounded implementation rescope of work unit WU-PR-03 (public, dev and CLI surfaces; requirements S02, S07, S09, S10, S15, S18 and the same-version release refresh) of the approved HDE-CRD-0002 Implementation Plan v1.1.
- Origin: the WU-PR-03 rescope request v1.0 (items RP-1, RP-3 and RP-2) from the dedicated PR engineering session during pre-Proceed planning.
- Evidence: the review's reading of the canon passages on the dev Reader start helper, and its own reproduction at `main` `852370c` of the release refresh, the stale label and its correction.

### Decision and approval status

The continuing whole-change Implementation Agent for HDE-CRD-0002 decided `APPROVE` on the WU-PR-03 rescope request v1.0, as one state for the one request. The decision record is `docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md`.

The approval is a bounded implementation rescope within the approved Specification's intent. It does not change the Epic-level commitment, any Specification acceptance criterion, any protected boundary, any other work unit, any accepted dependency or any Product Owner matter. The immutable base is not rewritten.

This addendum is the one overlay the approval creates. The effective baseline for WU-PR-03 is the approved base plus addenda 2.2, 2.3 and 2.5 plus this addendum.

The canon-conflict register entry CR-6 is `APPROVED` with alternative (a): canon governs.

### Base

The base is not changed. Its relevant clauses are:
- **Specification v1.1:**
  - requirement S10 ("The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses"), narrowed by the approved Plan to explicit `dev`;
  - the constraint "S10 must not break dev, test or local use of `/reader`";
  - requirement S09;
  - requirement S12 ("Current-release captures carry current-release labels").
- **Implementation Audit v1.0, engineering choice EC-4:** "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev` when unset; `docs/server/reader_v1.md` states it".
- **Implementation Plan v1.1:**
  - interface IF-7 (release labels on rows for captures the current release regenerates);
  - interface IF-10, whose last clause is "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev`";
  - work unit WU-PR-03 "Deliverables" and acceptance (2), whose last clause is "`scripts/dev_start_reader.sh` without `APP_ENV` starts a serving runner".
- **Plan review v1.0, redline R1:** the explicit-`dev` gate, applied in review v1.1. R1 kept EC-4's default.
- **WU-PR-03 PR instruction v1.0:**
  - §4, §5.5, §6, §8 contract E-6, §9 items 5 and 6, and §10 carry the default;
  - §5.7 (c) states that a roster capture left byte-stable across a `release_id` change keeps its earlier label and "is a finding to the IA … not a roster edit";
  - §6 keeps `tools/evidence/update_evidence_index.py` unchanged.

### Approved delta (RP-1): canon governs the dev Reader start helper

Six binding canon passages, in five documents, require dev Reader start helpers to propagate `APP_ENV` exactly as the caller supplies it, including unset and empty, and never to default it:
- HDE Architecture §3.8.1, "Repo-side start-helper posture";
- HDE Mechanics Guide §5.6, "Dev Reader start helpers (APP_ENV propagation)", and §34, the required start command `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`;
- Glow Infrastructure §8.1, the `APP_ENV` note;
- HDE Build Checklist — Conjunction, HDE-CONJ001.4;
- Glow QA Guide §13.9.

HDE Math Spec §12 supports them ("A default that treats an unset environment as development is not fail-closed").

No HDE Build Notes addendum and no Product Owner rescope supersedes these passages, so canon governs the in-flight Plan, its review and the instruction on this point. For WU-PR-03:

1. `scripts/dev_start_reader.sh` is not changed; it already exports `APP_ENV` only when the caller supplies it and displays `<UNSET>` otherwise. EC-4 is not implemented, and the script is not a deliverable of the unit.
2. IF-10's last clause reads: "`scripts/dev_start_reader.sh` propagates `APP_ENV` exactly as the caller supplies it, including unset and empty, and never defaults it; the canonical start command supplies `APP_ENV=dev`."
3. Acceptance (2)'s last clause reads: "`scripts/dev_start_reader.sh` with `APP_ENV=dev` starts a serving runner; with `APP_ENV` unset or empty it propagates that state and the runner refuses `GET /reader` (403 `ERR_READER_FORBIDDEN`)."
4. Contract E-6 reads: "`/reader` served only for `APP_ENV=dev`. The runner propagates `APP_ENV` exactly and the caller supplies `dev`. `VERIFY.sh` uses the canonical runner and requires `APP_ENV=dev`."
5. The other instruction clauses that state the default follow items 1 to 4:
   - in §6, "S10 gate and runner default" becomes "S10 gate and the start command with `APP_ENV=dev`";
   - "the runner-default test" becomes "the runner propagation test" in §6 and §10;
   - §9 item 5 starts the runner with the caller's `APP_ENV=dev`;
   - §5.5's conclusion that the default is required no longer holds.
6. `VERIFY.sh` supplies no default. Unless the caller supplies exactly `APP_ENV=dev`, it refuses before starting a runner, prints `VERIFY_APP_ENV_NOT_DEV` with the effective value and exits 2. Otherwise it passes `APP_ENV` unchanged to the start helper.
7. `docs/server/reader_v1.md` and `docs/acceptance/reader_a7_crib.md` state the start command `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV`.
8. `tests/scripts/test_dev_start_reader.py` stays the registered owner test of `scripts/dev_start_reader.sh` (the four classifier keys of the instruction's ID-3 are unchanged). It proves:
   - `APP_ENV=dev` serves;
   - unset prints `APP_ENV=<UNSET>` and refuses 403 `ERR_READER_FORBIDDEN`;
   - empty, `test`, `local` and `prod` are kept and refused;
   - `VERIFY.sh` with `APP_ENV=dev` exits 0 with every token `_OK`;
   - `VERIFY.sh` without an explicit `dev` exits 2 with `VERIFY_APP_ENV_NOT_DEV` before any runner starts.

   It requires `bash` and `curl`.

### Approved delta (RP-3): one line leaves the current-release label roster

`tools/evidence/update_evidence_index.py` joins WU-PR-03's bounded files for exactly one change: the line `"artifacts/core/purity/purity_report.json",` is removed from `CURRENT_RELEASE_CAPTURE_PATHS`, leaving 22 paths.

The engine-core purity report binds the SHA-256 of 12 engine-core, serializer, mechanics-catalog and schema sources. It carries no `release_id` and does not bind `catalog/manifest.json`, so a same-version refresh that leaves those sources unchanged leaves it byte-stable. It therefore fails the roster's own stated criterion ("primaries whose bytes the admitted release determines"), and under the label rule it keeps a superseded release label.

These do not change:
- any other line of the updater, the roster comment, the label rule and pattern, the label strip, `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` and every other refusal, the write paths, the schema, the admitted-CRD table and the catalog validation call;
- `tools/evidence/generate_engine_core_evidence.py` and the purity report's schema.

The updater's own runs in the convergence remove the row's label; no governed artifact is hand-edited. For every other roster capture, a stale label after a refresh remains a finding to the Implementation Agent, never a roster edit.

### RP-2: in scope under the base; no delta

The updater validates the tracked endpoint catalog through the transport-proof owner's catalog validator. With WU-PR-03's validator, every updater run therefore refuses (`aux narrative catalog invalid`) until that owner has rewritten the catalog. The convergence runs the transport-proof owner's write and `--check` after admission and before the canonical JSON gate and the first updater run (step 3b). The later run of that owner stays and is byte-stable. The restart point for an evidence-primary change is step 3b.

This is a sequencing correction inside the method the approved Plan already sets: the same commands and owners, regeneration before the updater, and byte stability on a second run. No acceptance intent, boundary, unit or dependency changes.

### Binding requirements

- `git diff` from base to head is empty for `scripts/dev_start_reader.sh`. For `tools/evidence/update_evidence_index.py` it is exactly the one deleted roster line.
- After the convergence's last updater run:
  - the purity report's Index and Mirror rows carry no `notes` field;
  - every other roster row carries the new release's label;
  - the stale-binding sweep finds no purity-report hit.
- The updater changes, so every test file that imports or runs it runs. The full `tests/` sweep under closed rails, with `ruby`, `bash` and `curl` available, ends with a clean tree. The unit's result record names each check with its counts.
- The unit's result record states the roster change, its reason and the one row it unlabels. It carries the nonclaim that the purity report is not a release-bound capture. It does not represent the change as a modification of WU-PR-02's accepted delivery.
- WU-PR-03's acceptance (1) and (3) to (7), ID-1 to ID-4, the other contracts, the exclusions, the nonclaims, the evidence obligations and the PR-30/PR-35 split are unchanged. So are the `/reader` gate design (served only for explicit `APP_ENV=dev`), the catalog `env_gate` and acceptance (2)'s refusal set.
- Any further change outside the bounded files as extended here is a new finding to the Implementation Agent through the rescope lane.

### Scope, exclusions and nonclaims

- No release member changes beyond the unit's own two (`adapter/http_reader.py`, `engine/cli/main.py`); the same-version refresh is unchanged. `scripts/dev_start_reader.sh`, `VERIFY.sh` and the updater are not members.
- No public route, public payload, public flag, transport or production behavior changes from this rescope.
- No canon changes. The six start-helper passages stand as written, and no canon drainage follows from CR-6.
- Keeping the start helper's default under a Product Owner decision superseding canon was not decided. It remains a Product Owner option, not recommended, and would require drainage of the six passages.
- Adding release identity to the purity report was not approved.
- No live vendor, production or database call; closed rails throughout.
- No QA artifact, QA verdict, acceptance, PF09 or PF30 status movement, deployment, canon edit, Product Owner Proceed, merge authority or epic or CRD closure follows from this addendum.
- WU-PR-01 and WU-PR-02 remain accepted-final; nothing in them is reopened or rerun.

### Affected surfaces

- **Requirements.** S10 and S09 are met within their approved intent: dev use supplies `APP_ENV=dev`, as the canonical start command and the Dev and QA environment bindings do. S12 stays met; a capture the release does not determine carries no release claim. No other requirement is touched.
- **Dependencies.** None upstream. WU-PR-04 and WU-PR-05 refresh against the 22-path roster. WU-PR-08's version bump changes an engine-core source, so it regenerates the purity report, which stays unlabelled.
- **Tests.** The owner test proves propagation and the `VERIFY.sh` refusal instead of a default. No other test assertion changes. The updater's consumers run in the full sweep.
- **Ops and QA.** The S10 Live QA step and the Ops task that places the QA candidate use the canonical start command with an explicit `APP_ENV`. The unset refusal stays observable through the runner, which canon says QA harnesses rely on.
- **Documentation.** Two repository documents state the start command with `APP_ENV=dev`. `AGENTS.md` and `README.md` follow in the documentation unit.
- **Doc-delta candidates (canon, not edited).** After S10, HDE Mechanics Guide §34's "Current repository posture" statement that the Reader handler treats missing `APP_ENV` as dev becomes stale. This adds to the candidates already recorded for this unit.
- **Downstream work.** The updater-consumer, label-timing and stale-label rules carried by addendum 2.5 apply to the 22-path roster. The step-3b order applies to any later unit that changes the catalog validator.

### Evidence

- **Canon.** On `main` `852370c`, each of the six start-helper passages and the supporting HDE Math Spec bullet was read in its source; the quotations in the request are exact. On `main`, `scripts/dev_start_reader.sh` exports `APP_ENV` only when it is set. `VERIFY.sh` line 4 is `export APP_ENV=${APP_ENV:-dev}`.
- **Reproduction setup.** A detached worktree of `852370c` with the planning prototype applied, CPython 3.12 with the CI install, and closed rails.
- **Cut.** The same-version cut gave manifest SHA-256 `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f`, equal to the plan's rehearsal. The recompute check exited 0.
- **Engine-core owner.** It rewrote three captures and left the purity report byte-identical. Its internal updater run then refused with `aux narrative catalog invalid`, which is the RP-2 condition.
- **Convergence.** The order with step 3b exited 0 at every step through the updater, orientation, path, Mirror-schema and hash checks.
- **Stale label.** Exactly one of 28 labelled Mirror rows kept the superseded `release_id` `52be4558…`: the purity report. The three label tests of `tests/evidence/test_evidence_index_missing_state.py` failed.
- **Correction.** After the one-line roster removal and one updater run:
  - only that row's label was removed in the Index (620 rows before and after);
  - every validator exited 0, including the final-LF and step-log manifest checks;
  - `tests/evidence/test_evidence_index_missing_state.py` with `tests/evidence/test_engine_core_evidence.py` gave 74 passed.
- **Start-helper test.** `tests/scripts/test_dev_start_reader.py` gave 10 passed with the script byte-unchanged.
- **Recorded by the requesting session, not re-run by the review:** the full sweep on the final prototype, 4,747 passed, 3 skipped, 2 xfailed, 0 failed.

### Conflicts

CR-6, CANON_RECONCILIATION: the approved Plan required the dev Reader start helper to default `APP_ENV=dev`, and canon requires exact propagation. It is decided `APPROVED` with alternative (a), canon governs, through the deltas above. No canon drainage is required.

CR-1 to CR-5 of HDE-CRD-0002 are carried unchanged.

### Unresolved obligations and owners

- PF10 numbering and publication: the Product Owner.
- The documentation updates in `AGENTS.md` and `README.md` for the start command: the HDE-CRD-0002 documentation unit.
- The canon doc-delta candidate above: the Product Owner.
- The full sweep on the real branch, the convergence with its second-run byte stability, and the result record: the dedicated WU-PR-03 PR engineering session in implementation, after the Product Owner's Proceed.

### Status and consequences

- **Completed:** the review decision, CR-6's decision and this overlay.
- **Not yet done:**
  - plan v1.1;
  - the Product Owner's Proceed;
  - implementation, reviews and merge of WU-PR-03;
  - the later instructions that apply the 22-path roster and the step-3b order.
- **Unproven:** the full sweep on the real branch.
- **Consequence:** when WU-PR-03 lands under this overlay:
  - the dev Reader start helper conforms to canon and leaves every `APP_ENV` mode observable;
  - the dev route serves only for an explicit `APP_ENV=dev`;
  - `VERIFY.sh` refuses loudly instead of defaulting;
  - the release refresh converges with green evidence-lane tests and no stale release claim on a capture the release does not determine.
