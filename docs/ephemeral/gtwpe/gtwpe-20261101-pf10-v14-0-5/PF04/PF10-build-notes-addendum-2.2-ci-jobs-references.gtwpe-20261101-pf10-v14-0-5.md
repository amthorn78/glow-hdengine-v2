---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: CI-JOBS-REFERENCES-1
artifact_version: "1.0"
proposed_pf10_number: "2.2, as the Product Owner placed it: in the next PF10 base version after HDE Build Notes v14.0.5 drains, following the draft addendum 2.1 in docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-isis-review.gtwpe-20261101-pf10-v14-0-5.md §7. HDE Build Notes v14.0.5 on main has its own, unrelated 2.2; this number is not for that version"
authority: "Nathan / Product Owner, 2026-11-02, in the T-16 document session, answering \"should the ci/jobs/*.yml pointers become their own canon change across those seven documents, or stay as they are for now? I recommend a separate canon change rather than another T-01 follow-up.\" with: \"Just create a PF10 build notes addendum for that. Make it 2.2\""
producing_session: https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR (branch claude/gtwpe-triage-authoring-j94ewf-documents)
origin: T-01 follow-up drain-4 of ledger gtwpe-20261101-pf10-v14-0-5, which reported the ci/jobs references and did not change them (PF04/PF04-Canon-HDE-Governance-v2.8.12.proof-log.md §7)
repository_head_read: origin/main b9edf2bca74d003925a8539b4ae7b88fc6ae0eeb. docs/pfcanon/ is unchanged from 84d6d1cad95c67788336d174dc4b8922d9bb0cb2
pf10_read: HDE Build Notes v14.0.5 on main, the front matter rules 1 to 9, the template, the addendum index, and the addendum "GATE:CORE-DET evidence is the real compat path" in full; draft addendum 2.1 and its placement section (§6) in full
capture_time_utc: 2026-11-02T03:42:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The front matter and the "Canon relied on" block above the H2 are record-only and are not page text
incorporated_into: not yet
---

**Canon relied on** (read on `main` at `b9edf2b`; each section read in full):

* HDE Build Notes v14.0.5: "Precedence, versioning, and scope" rules 1 to 9 (rule 4, continuous addendum sequence; rule 6, current-version rule, under which a new base version does not read the old one); "Cross-references" (titles only); the template; and the addendum "GATE:CORE-DET evidence is the real compat path" (FND-005), whose R-2 retired three of the job files this addendum covers.
* Change Process Guide v2.5.5, §0.1A, the paragraph on agent-authored HDE Build Notes addenda (one H2, H3 subordinates, declarative, no role-addressed publication, routing or record-maintenance instructions).
* HDE Governance v2.8.8: §4.3 "CI hygiene"; §7.3 "Narratives persistence logging (admin-only)"; §12.2 "Evidence links"; §15.2 "Open issues list", OI-004 and OI-005; Appendix B.1 to B.6; Appendix C.1 to C.7; Appendix D.2, D.4, D.5 and D.10. Also T-01's unpublished revision v2.8.12 (`docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.12.md`), §12.2 and Appendix B.2, which already state the GATE:CORE-DET job retirement.
* HDE Build Checklist — Fermentation v1.6.1, Subtask HDE-FERM001.4.
* HDE Build Checklist — Distillation v1.1.9, Subtasks HDE-DIST001.3 and HDE-DIST004.3, and the T-16 revision v1.1.10 of the same rows.
* HDE Schemas & Artifacts v2.9.7, §8.6.3.4, "Rails proofs (ops)".
* HDE Mechanics Guide v3.5.9, §1.1 "Capabilities the repo must provide".
* HD Engine Epics Map v2.3.8, HDE-EPIC012, "Evidence (titles/paths only)".
* HDE Phased Epics v1.9.6, §2.16 HDE-EPIC031, D2.
* Draft addendum 2.1 (`docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-isis-review.gtwpe-20261101-pf10-v14-0-5.md`, v1.1), §6 "Placement and the GTWPE drafts" and §7: the placement of the next base version's addenda and their stand-alone form.
* Ledger `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, §7 "Execution destination".
* Code and records read at `b9edf2b`: `.github/workflows/ci.yml`; `ci/checks/run_rails_job_definitions.py`; `ci/checks/classify_ci_changes.py`; `tools/evidence/run_sanity_pipeline.py`; `tools/evidence/generate_rails_gate_evidence.py`; `tests/evidence/test_rails_ci_workflow_integration.py`; the three files in `ci/jobs/`; and the complete path history of `main` (1,444 commits).
* Editorial standard: Technical Writing Best Practices v1.8.8.

## 2.2 CI job references in canon: `ci/jobs/` holds the three rails job definitions, nineteen job files that never existed are retired as CI evidence, and the three bench jobs remain planned work

Timestamp: 110226 03:42 (UTC). Details:

* What this records. The Product Owner's decision of 2026-11-02 that the `ci/jobs/*.yml` references in PF canon become their own canon change. No code, test, workflow or evidence changes.
* What this decides.
  * What `ci/jobs/` holds, and which canon references to it are current (R-1).
  * Nineteen referenced job files that never existed are retired as CI evidence (R-2).
  * How canon names a CI check (R-3).
  * The bench job names and two open issues stay as planned work (R-4).

### Decision and approval status

* Decision. The Product Owner directed on 2026-11-02 that the `ci/jobs/*.yml` references become their own canon change, recorded as this addendum and numbered 2.2. Rules R-1 to R-4 state that change.
* Status. Proposed. The rules take effect as canon when this addendum is published in HDE Build Notes.
* Relation to other canon.
  * Every gate's binary checklist and pass conditions in HDE Governance are unchanged.
  * The three rails job definitions, and every canon reference to them, are unchanged.
  * This addendum supersedes only the following:
    * the `ci/jobs/*.yml` entries that R-2 lists, in HDE Governance Appendix B.1, B.2, B.3, B.4, B.6, D.2, D.4 and D.10;
    * any reading of HDE Governance Appendix C.6 "Jobs" as naming existing CI (R-4).
  * Every other entry in those sections still governs.

### The facts that prompted it

All read on main at `b9edf2b`.

* `ci/jobs/` holds three files, and has never held more.
  * They are `ci/jobs/rails_closed_refusal.yml`, `ci/jobs/rails_open_conformance.yml` and `ci/jobs/logs_keys_only_redaction.yml`. HDE-EPIC031 added them on 2026-05-10; the last change was HDE-EPIC040 PR-04 (`cd6f9e6`, 2026-09-22).
  * Each is a rails job definition: a small YAML file in the closed schema that `ci/checks/run_rails_job_definitions.py` reads. The runner accepts exactly these three identities and refuses any other as "unknown job identity".
  * CI runs them in the one `test` job of `.github/workflows/ci.yml`, in the step "Run rails policy and secret-safety lane". The CI classifier sends a change under `ci/jobs/` to the rails and release lanes. Release-sanity stage 06, "CI rails", runs them too. `tests/evidence/test_rails_ci_workflow_integration.py` pins the three.
* PF canon names 25 distinct `ci/jobs/*.yml` files: the three above and 22 others.
* None of the 22 others has ever existed. No path in the history of `main` (1,444 commits, 11,636 distinct paths) has any of their names. The only CI configuration files `main` has ever held are `.github/workflows/ci.yml`, `.github/workflows/epic-closeout-validation.yml` and the three rails job definitions.
* Where the 22 appear.
  * HDE Governance lists 19 of them as CI jobs or CI guards of its gates, in Appendix B.1, B.2, B.3, B.4, B.6, D.2, D.4 and D.10.
  * The other three are bench jobs: `ci/jobs/bench_math_transport.yml`, `ci/jobs/bench_vendor_open.yml` and `ci/jobs/slo_verify.yml`. They appear in HDE Governance Appendix C.6 "CI hooks"; in HDE Build Checklist — Distillation, Subtask HDE-DIST004.3 "Bench CI jobs", whose status is Not done; and in HD Engine Epics Map, HDE-EPIC012, an Epic recorded as won't do.
  * HDE Governance §15.2 already records two of the 19 as absent: OI-004 says `ci/jobs/canonical_emitter_symbol_check.yml` "was not found in the complete tree", and OI-005's next step is to add `ci/jobs/transport_head_parity.yml` "or record approved replacement paths". Both issues are OPEN.
* The earlier HDE Build Notes addendum of 2026-11-01, "GATE:CORE-DET evidence is the real compat path" (FND-005), already retired three of the 19, the HDE Governance Appendix B.2 entries, because they never existed.
* HDE Build Checklist — Fermentation, HDE Schemas & Artifacts, HDE Mechanics Guide and HDE Phased Epics name only the three rails job definitions. So does HDE Build Checklist — Distillation outside HDE-DIST004.3. Those references are accurate.

### R-1 — What `ci/jobs/` holds

* `ci/jobs/` holds rails job definitions only. A rails job definition is a file in the closed schema that `ci/checks/run_rails_job_definitions.py` reads, with one of the identities the runner accepts.
* The current definitions are `ci/jobs/rails_closed_refusal.yml`, `ci/jobs/rails_open_conformance.yml` and `ci/jobs/logs_keys_only_redaction.yml`. They are current CI. CI runs them in the rails lane of the `test` job, and release-sanity stage 06 runs them.
* These canon references to them are current and stay as written:
  * HDE Governance §7.3, Appendix B.5 and Appendix D.5;
  * HDE Build Checklist — Fermentation, Subtask HDE-FERM001.4;
  * HDE Build Checklist — Distillation, Subtask HDE-DIST001.3;
  * HDE Schemas & Artifacts §8.6.3.4, "Rails proofs (ops)";
  * HDE Mechanics Guide §1.1;
  * HDE Phased Epics, HDE-EPIC031, D2.

### R-2 — Retired job references

These job files never existed. They are not CI jobs, and no record may cite them as current CI evidence, as proof that a check runs, or as an input to a gate result.

* HDE Governance Appendix B.1: `ci/jobs/canonical_emitter_symbol_check.yml`, `ci/jobs/no_json_dumps_public_guard.yml` and `ci/jobs/lf_and_encoding_check.yml`. The last is also in Appendix D.2, "CI guards".
* HDE Governance Appendix B.2: `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml` and `ci/jobs/two_run_identity_bytecompare.yml`. This restates the retirement in the addendum of 2026-11-01 and changes nothing about it.
* HDE Governance Appendix B.3: `ci/jobs/schema_shape_success.yml`, `ci/jobs/schema_shape_error.yml` and `ci/jobs/reader_cli_parity.yml`.
* HDE Governance Appendix B.4 and D.4: `ci/jobs/transport_etag_200.yml`, `ci/jobs/transport_conditional_304.yml`, `ci/jobs/transport_head_parity.yml` and `ci/jobs/transport_no_store_writers_errors.yml`.
* HDE Governance Appendix B.6: `ci/jobs/validation_viewer_prefs.yml`, `ci/jobs/fixed_point_rounding_and_clamp.yml`, `ci/jobs/band_thresholds_inclusive.yml` and `ci/jobs/public_numeric_ban_guard.yml`.
* HDE Governance Appendix D.10: `ci/jobs/bands_edges_snapshot.yml` and `ci/jobs/bands_edges_diff.yml`.

What retirement means:

* It removes references to files that never existed. It removes no requirement. Each gate's binary checklist still states what must hold.
* Where a retired reference was the only CI evidence a section named for a check, that section names no CI evidence for the check. It names one when the tracked test or tool that performs the check is identified (R-3).
* A retired reference is not a specification for a new file. Creating a file under `ci/jobs/` with a retired name would run nothing: the runner refuses any identity outside R-1.

### R-3 — How canon names a CI check

* Canon names a `ci/jobs/<name>.yml` file only for a rails job definition that is tracked on `main`.
* Canon names any other CI check by the tracked test or tool that performs it. Where the lane matters, it also names the step of the `test` job in `.github/workflows/ci.yml` that runs it.
* A test that CI runs only when the CI classifier selects it is cited as run "as CI selects it". `ci/checks/classify_ci_changes.py` decides that selection.
* A "titles-only" list of CI jobs or CI guards names existing files only.
* Planned work may name a file that does not exist yet: a build-checklist subtask that is not done, an Epic record, or an open issue's next step. Such a name records planned work. No record may cite it as an existing CI job.

### R-4 — Planned and open entries that stay

* The bench jobs `ci/jobs/bench_math_transport.yml`, `ci/jobs/bench_vendor_open.yml` and `ci/jobs/slo_verify.yml` are planned work, not CI. They are not retired.
  * HDE Build Checklist — Distillation, Subtask HDE-DIST004.3, keeps them as written, with status Not done.
  * HD Engine Epics Map, HDE-EPIC012, keeps them as written, as part of that Epic's record.
  * HDE Governance Appendix C.6 "Jobs" names the planned bench orchestration of HDE-DIST004.3. It names no existing file.
  * Delivering them as `ci/jobs/` files would need the runner and the workflow changed first, because the runner accepts only the identities in R-1.
* HDE Governance §15.2 OI-004 and OI-005 stay OPEN as written. R-2 neither closes nor satisfies them.

### Known nonconforming items

Each item was found by the search behind this addendum. None is changed here. Each needs its owner's decision.

* HDE Governance §7.3 names `ci/jobs/logs_keys_only_redaction.yml` as the required CI evidence locus for narrative-persistence logs. It says the job "MUST prove that logs contain no narrative text and only the allowed keys". The job runs `tools/evidence/generate_rails_gate_evidence.py --check` and two vendor-client test files. None of them mentions narratives. Whether any CI check proves the §7.3 requirement is not established.
* HDE Governance names four files under `ci/grep-guards/`: `canonical_emitter.allowlist` and `no_json_dumps_public.regex` (§12.2, GATE:CORE-CANON), `public_numeric_ban.regex` (§12.2, GATE:CORE-MATCH) and `no_ansi_no_bom.regex` (Appendix D.2). No path under `ci/grep-guards/` exists on `main` or in its history. They are outside this addendum's scope.

### Scope, exclusions and nonclaims

* Scope: references to `ci/jobs/*.yml` in PF canon; what `ci/jobs/` holds; how canon names a CI check.
* Excluded:
  * any code, test, workflow, CI or evidence change;
  * any gate's checklist or pass conditions;
  * which tracked test or tool performs each check whose job reference R-2 retires;
  * `ci/grep-guards/` and any other untracked CI path;
  * the delivery of the bench jobs.
* Nonclaims. This record makes no QA verdict, acceptance, Ops result, deployment or build-checklist movement, and drains no canon. It does not say whether any gate passes. The facts it cites are static reads of the repository; no test or CI run was made for it.

### Dependencies and unresolved obligations

* Drainage into permanent canon has not been done. The targets are:
  * HDE Governance Appendix B.1, B.2, B.3, B.4, B.6, D.2, D.4 and D.10 (R-2);
  * HDE Governance Appendix C.6 (R-4);
  * HDE Governance §4.3 "CI hygiene" (R-1 and R-3).
* The tracked test or tool that performs each check whose job reference R-2 retires is not identified. Until it is, the affected sections name no CI evidence for those checks.
* The two known nonconforming items are open.

### Evidence

* `ci/` on `main` at `b9edf2b`: `ci/checks/` (11 files) and `ci/jobs/` (3 files).
* History of the three rails job definitions: added in `9012b4d` and `28e3c0f` (2026-05-10), changed in `472ba83` and `76a331a` (2026-07-14), `f48226f` (2026-07-23) and `cd6f9e6` (2026-09-22).
* The complete path history of `main` at `b9edf2b` (1,444 commits): no path has the name of any of the 22 other job files, and no path is under `ci/grep-guards/`.
* Runner and CI wiring:
  * `ci/checks/run_rails_job_definitions.py` (`REQUIRED_IDENTITIES`; "unknown job identity"; "required identities mismatch");
  * `.github/workflows/ci.yml` (step "Run rails policy and secret-safety lane");
  * `ci/checks/classify_ci_changes.py` (a change under `ci/jobs/` selects the rails and release lanes);
  * `tools/evidence/run_sanity_pipeline.py` (stage "06 CI rails");
  * `tests/evidence/test_rails_ci_workflow_integration.py`.
* The redaction job's commands: `ci/jobs/logs_keys_only_redaction.yml`; `tools/evidence/generate_rails_gate_evidence.py`; `tests/bodygraph/test_vendor_client.py`; `tests/bodygraph/test_resolver_vendor.py`.
