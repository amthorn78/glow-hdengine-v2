# HDE-EPIC040-PR03 — PR Implementation Result v1.3

```yaml
artifact_type: PR_IMPLEMENTATION_RESULT
PR_IMPLEMENTATION_RESULT_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-RESULT
version: v1.3
predecessor: https://drive.google.com/file/d/14sNRNIhMFfLJvdOSNAgkcy3attWdVFjk/view?usp=drivesdk
state: MERGE_PENDING
readiness: READY_TO_MERGE
capture_utc: 2026-09-14T12:18:15Z
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR03
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: dedicated PR engineering session for HDE-EPIC040-PR03
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / RS-40 / PR03-R02
context_conflict: NONE
lifecycle: EXISTING_OPEN_PR_IMPLEMENTATION
originating_stage: PR-30
original_PO_PROCEED: PRESERVED
PR_IMPLEMENTATION_PLAN_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN
plan_version: v1.0
rescope_review: HDE-EPIC040-PR03-RESCOPE-REVIEW-01 v1.0 APPROVE
manual_drain: CONFIRMED_AND_SUBSTANTIVE_EQUALITY_VERIFIED
current_PF10: PF10-HDE-Build-Notes-v13.2.5.md section 2.12
source_correction_applied: true
local_validation_complete: true
corrected_source_code_review: COMPLETED_NATIVE_NO_FINDINGS_SIGNAL
corrected_source_security_review: COMPLETED_NO_SECURITY_ISSUES
repository: amthorn78/glow-hdengine-v2
target: main
worktree: /workspace/scratch/808bf6c1dac3/pr03
branch: hde-epic040-pr03-pure-gate-core
local_implemented_head: 2badc3c5b87e40ddcc984865420e91a2f9695cd1
local_implemented_tree: cbc6f35834253dcee3907bf4669bc7cdd1e396a2
local_candidate_clean: true
correction_commit_object_published: true
remote_PR_branch_updated: true
remote_PR_head: 2badc3c5b87e40ddcc984865420e91a2f9695cd1
remote_PR_tree: cbc6f35834253dcee3907bf4669bc7cdd1e396a2
baseline_head: 5b2fb8d70924a6710b6261fc0c93d3869fed6380
baseline_tree: e43c2063599e7bc449f20d4ab045d32d95581bf4
PR_REF: https://github.com/amthorn78/glow-hdengine-v2/pull/405
PR_state: OPEN_NON_DRAFT_UNMERGED
hosted_CI_runs_for_correction: 1
final_exact_head_CI: SUCCESS
final_CI_run: https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34841280306
PO_publication_order_exception: EXPLICIT_SINGLE_PUSH_AUTOMATIC_CI_BEFORE_CORRECTED_SOURCE_REVIEW
review_or_CI_waiver: NONE
unresolved_engineering_review_threads: 0
CI_suppression_or_workflow_controls_changed: false
PF10_edited_by_engineer: false
merge_or_PR40_executed: false
independent_QA_Ops_deployment_release_activation_Epic_closure: NOT_EXECUTED
output_classification: EPHEMERAL_DRIVE
output_destination: Glow / Ephemeral Planning Files
output_parent_id: 1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc
native_return_owner: Nathan / Product Owner
continuation_handoff: CONDITIONAL_PR40_AFTER_NATHAN_MANUAL_MERGE
conditional_PR40_receiver: retained whole-change HDE-EPIC040 Implementation Architect in its established read-only lineage-review role
```

## Outcome

**MERGE_PENDING — Ready to merge [PR #405](https://github.com/amthorn78/glow-hdengine-v2/pull/405).**

The approved correction is implemented, committed, pushed, locally validated, reviewed and passed all seven selected hosted CI lanes on exact head `2badc3c5b87e40ddcc984865420e91a2f9695cd1`, tree `cbc6f35834253dcee3907bf4669bc7cdd1e396a2`. All engineering review threads are resolved. The original release-misattribution reproducer now refuses before an incorrect result can be produced.

Nathan's explicit “yes” authorized the single already-tested correction push, accepting that automatic CI would start before corrected-source review. The engineer performed exactly that push. The ordering exception is recorded separately from actual passing tests, completed reviews and CI; nothing was waived, no CI controls were changed, and there is no agent merge authority.

This complete successor supersedes v1.2's publication-decision blocker and v1.1's unimplemented-rescope state while preserving both records as history. Actual manual merge and independent PR-40 acceptance remain future actions.

## Authority, manual drain and source lineage

The prior erroneous missing-drain return is not repeated. Nathan's assertion that the content is present and the renewed RS-40 invocation were carried forward. The engineer independently resolved the current controlled PF10 and compared its complete §2.12 with the approved page-ready addendum. The substantive bodies match; differences are Markdown bolding, escaping, bullet formatting, whitespace and PF10's trailing EOF marker.

The controlled-source path was verified through Glow → Core Docs → PFCanon, with direct parent IDs:
`0ANCzbmSbmO_HUk9PVA → 1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3 → 18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu → 1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`.
The unique current controlled PF10 Markdown is v13.2.5, not the handoff's explicitly pre-drain v13.2.4. No Google Doc twin or stale attachment was substituted.

| Source | Exact identity | Direct reference |
| --- | --- | --- |
| Current PF10 | v13.2.5, §2.12; fetched text 159,862 UTF-8 bytes, SHA-256 `e12a5f699078fc43d44be72f96ea586ab14116d75988e6e2a19d53aa0ab16ebf` | [PF10](https://drive.google.com/file/d/1evxWB8tdxeFstNtMzT-MD0kjuRGtaILq/view?usp=drivesdk) |
| Approved addendum | HDE-EPIC040-PR03-R02-PF10-BUILD-NOTES-ADDENDUM v1.0; 10,629 bytes, SHA-256 `a44659a7754c5f6e10f0bf4a1397d6815aae32ef75a2626a866055a801ba1998` | [Addendum](https://drive.google.com/file/d/1AKBfTpnV3C6jALe18COqDFadk2DplVb7/view?usp=drivesdk) |
| Native approval | HDE-EPIC040-PR03-RESCOPE-REVIEW-01 v1.0, APPROVE; 33,251 bytes, SHA-256 `eb7259a6477b62129bd12b266d3a12a92ec24925ebd9f73c9f518c12be18dde1` | [Review](https://drive.google.com/file/d/1QygaPftN2OnucTvZgMPtpKn5eCemXUyE/view?usp=drivesdk) |
| Rescope request | HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0; SHA-256 `1f5a1df21a4be089809b9ac642ca047d3205669a39cf3e2c8ce301bda5dd41e1` | [Request](https://drive.google.com/file/d/1Cg6LglLhgqPVrHr6uL374kkdiP2Zqzu6/view?usp=drivesdk) |
| Immutable PR instruction | v1.0, INSTRUCTION_READY; SHA-256 `4f45fff6ecd79b85f7b0d97f57056d1bd8e896eaff53fce81567ee0d08446895` | [Instruction](https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk) |
| Immutable detailed PR plan | v1.0; SHA-256 `d6fb097d009c81d71b28f97bf09ba5d71bb8429f7d458dcda5f667d0c5a6e8a9`; original Proceed preserved | [Plan](https://drive.google.com/file/d/1wPpcIQkDLVNwdvK2ujfDpkssUh4KwAoO/view?usp=drivesdk) |
| Specification | v1.1, Thoth-17 APPROVE | [Specification](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk) |
| Implementation Audit | v2.0, AUDIT_COMPLETE | [Audit](https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk) |
| Whole-change Plan | v2.1, immutable | [Whole-change Plan](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk) |
| Plan review | v2.1, Isis-50 APPROVE | [Plan review](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk) |
| Accepted PR01 | Lineage review v1.1, ACCEPT, #403 final | [PR01 lineage](https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk) |
| Accepted PR02 | Lineage review v1.0, ACCEPT, #404 final | [PR02 lineage](https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk) |
| Earlier result | v1.1, historical RESCOPE_PENDING | [Result v1.1](https://drive.google.com/file/d/1UZZYqgpVrbraGMGrlOFnPwGqFCUp4ZmF/view?usp=drivesdk) |
| Immediate predecessor | v1.2, historical PRODUCT_OWNER_DECISION_REQUIRED; its publication blocker is superseded by Nathan's explicit authorization and the completed push/reviews/CI | [Result v1.2](https://drive.google.com/file/d/14sNRNIhMFfLJvdOSNAgkcy3attWdVFjk/view?usp=drivesdk) |
| Session/CI RCA | v1.1, historical incident record | [RCA](https://drive.google.com/file/d/1EOOqIiuaVxPv42Oh9sf3kxNF0WhmC2NK/view?usp=drivesdk) |
| PF10-resolution RCA | v1.0, previously saved as separately requested | [Resolution RCA](https://drive.google.com/file/d/1rdQnB-u6HyGB5sWxq5-uYlU_kFKz6tKI/view?usp=drivesdk) |

The standalone addendum's original READY_FOR_MANUAL_DRAIN / NON_CANONICAL_PENDING_MANUAL_DRAIN metadata remains historical source text. Its effective scope here derives from Nathan's completed drain and the independently verified current PF10 section. The engineer did not edit that metadata, number PF10, perform the drain, rewrite an approved base or ask for a replacement Proceed.

## Implemented correction and preserved delivery

The existing admission owner now covers exactly eight modules: the accepted loader, serializer wrapper, stable serializer and category registry, plus core, composite, signals and calculators. Each newly covered pure module passively retains its executing top-level code object, name, file, origin, optimization level and interpreter cache tag after its definitions complete. Capture failure leaves unavailable provenance; it does not break candidate imports into a successful admission bypass.

The loader resolves the mechanics modules at admission, after its own types exist, avoiding core/type import cycles. It checks partial initialization, retained/live origin agreement, one safe common absolute source root, compatible compilation semantics and the existing manifest-bound capture. Its existing comparator passively compiles exact captured bytes with `dont_inherit=True` and the checked optimization level, then compares the result to retained actual top-level execution code. Typed refusals remain internal. No captured source is executed and no module is reloaded.

Production changes are confined to:

- `engine/config/registry_loader.py`;
- `engine/core/core.py`;
- `engine/magic10/composite.py`;
- `engine/magic10/signals.py`;
- `engine/magic10/calculators.py`.

Tests changed only in `tests/config/test_production_admission.py` and `tests/core/test_engine_core_purity.py`. The synthetic helper and evidence writer did not require source edits during this correction. No new loader, serializer, calculator, schema, selector, bundle field or public field was added.

The original PR03 delivery remains intact: exact four-required-argument `compute_core(member_a, member_b, mechanics_bundle, release_id)`; accepted NormalizedGates and injected immutable AdmittedMechanicsBundle; one five-state classifier over the accepted 36-row taxonomy; 20 ordered signals; ten ordered category scores/bands; intrinsic chart fingerprints and numerically ordered pair identity; immutable six-field magic10_result.v1 closure; refusal of malformed/incoherent inputs; removal of the precomputed-score/CoreConfig/three-argument success path. Configuration and source loading remain outside computation.

No mathematical operation changed. The fixed G004 q oracle remains `[25,63,0,38,40,20,0,25,50,38,50,0,0,0,50,20,0,60,0,33]`; categories remain `[22,10,15,6,22,13,0,18,15,8]`, all Cool. Existing rounding, inclusive 24/49/74 bands, caps, Integration exceptions, schema, fingerprint/pair preimages and serializer ownership are unchanged.

## Before/after proof and requirement mapping

The unchanged retained reproducer is `/workspace/scratch/808bf6c1dac3/pr03-r02-repro.py`. Before production edits, it again admitted a coherently rehashed temporary signals source changed from addition to subtraction, changed the release ID, and produced unchanged signals/categories labeled with the altered release. Executing-source SHA-256 was `c1d3829c21934452ed1a34b7ba32d8f84664033730f1ec0ebdea354d24f2c690`; altered temporary-source SHA-256 was `fa51ef85f2cc711fee24a58139214945214bc3a6630ed14d648279808cae232c`.

Four new per-module regression cases were run before repair: all four failed because the expected refusal did not occur. After the correction they pass. Running the original unchanged reproducer through the bounded verification wrapper now reports:

```json
{"preserved_reproducer":"REFUSED_BEFORE_ALTERED_RESULT","refusal":"EXECUTING_SOURCE_MISMATCH","finding":"CORRECTED_LOCALLY"}
```

| Obligation | Current decisive tests/evidence |
| --- | --- |
| K040-REQ-006/007/008/009; AC040-03/04/05/09 | Rehashed syntax-valid non-equivalent code in each new owner refuses; exact eight-owner roster preserves the accepted four |
| K040-REQ-011; AC040-08 | Missing/short/nonmodule provenance, partial initialization, wrong optimization/cache tag, retained/live origin mismatch and different installation origin fail closed |
| Captured-byte discipline | Omitted captured sources refuse UNBOUND_SOURCE; parseable but uncompilable module sources refuse EXECUTION_COMPILATION_FAILED; changes after capture refuse SOURCE_CHANGED |
| Supported startup/execution equivalence | Fresh loader-first/core-first imports at optimization 0/1/2; each new owner's timestamp-valid stale bytecode refuses while fresh changed source admits |
| Equivalent source is not historical raw-byte identity | Per-module trailing-comment changes admit, preserve signals/categories/config, change release/pair identity and retain AB/BA canonical-byte parity |
| Purity and no reload/execute | Genuinely fresh pure imports under side-effect guards record exactly four passive captures; computation also blocks compile/exec/eval/import/frame inspection/reload and external effects |
| Existing behavior and predecessors | All fixed oracles, classifiers, signals, reducers, identity, immutability, malformed-input, threshold and production-admission regressions pass; accepted PR01/PR02 lifecycle work is not reopened |
| K040-REQ-012/013 | Existing core writer/companions, exact candidate/source inventory, local logs, actual corrected-source review dispositions and final exact-head hosted CI |

The former two-root test replaced signals with a placeholder and expected admission. It was adapted to append a nonexecuting comment instead, retaining its original distinct-source identity and no-cross-read assertions under the newly approved equivalence boundary. The symlink test now restores original signals bytes between its leaf and ancestor cases. These are bounded fixture adaptations, not weakened assertions.

There are 71 additional collected admission regression cases. Counts below overlap; do not sum them.

## Local validation on the correction

The retained Python 3.12 environment `/workspace/scratch/808bf6c1dac3/pr03-venv` was reused, requirements-dev.txt, requirements.txt and the editable project were installed, pytest 8.4.2 readiness verified, and environment pins checked. Validation used `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. No live vendor/database access occurred.

| Validation | Actual result |
| --- | --- |
| Expanded focused plan suite, including accepted execution-coherence regression | 730 passed |
| Configured default suite | 1,893 passed; 3 existing closed-rails vendor skips |
| Exact classifier-selected tests in clean isolated worktree | 1,970 passed |
| Product lane and ordering check | 20 passed; check PASS |
| Compatibility lane/help/serializer/emitter checks | 62 passed, 3 skips, 2 existing xfails; checks PASS |
| DB/runtime-contract lane | 249 passed; direct-only contract PASS |
| Rails definitions/workflow integration | Definition runner PASS; 124 workflow-integration tests passed |
| Evidence lane | 111 passed |
| Generic QA subsystem regression in clean worktree | 488 passed |
| Release regression in clean worktree | 52 passed |
| Actual manifest-only check | PASS; unchanged 15-member manifest |
| External exact-source attestation build and verify | PASS with --require-clean |
| Candidate diff/clean checks | PASS |

The classifier selected all seven lanes and affected tests for the full main-to-candidate difference: 40 paths. The QA/release rows are engineering regression checks, not independent QA, Ops, release activation or Epic acceptance.

Exact command logs and JUnit records are preserved at:

- `/workspace/scratch/7dd3a4c5f4d6/rs40-validation`: per-group command/start/elapsed/exit records, logs and XML;
- `/workspace/scratch/7dd3a4c5f4d6/rs40-clean-lanes`: classification, changed-tests manifest, isolated suite results, manifest check and attestation;
- transient drivers `rs40_validate.py`, `rs40_clean_lanes.py`, `verify_preserved_pr03_r02.py` in the same current scratch workspace.

Focused tests were run before default regression. The first broader narrow run found only the now-adapted two-root placeholder case; 245 other tests passed. Subsequent runs passed, including 299 provenance/determinism tests before the final additions and 246 final admission/purity/determinism tests. Those developmental runs are not substituted for the complete final suites.

External attestation binds source commit `2badc3c5b87e40ddcc984865420e91a2f9695cd1`, source-tree digest `c540ce4f282cf1f735dce8e78087e97c94329923047c5a9f5b3c6ceb36997f4d`, and manifest identity `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`. Attestation JSON SHA-256: `39cf08331a4ddb40c48e069193919f990a0854911e7d974dd08dcf547537cb8b`. The existing safety filter omitted 14 retained-history entries/companions; its prior bounded behavior was preserved. The external attestation bundle is retained. Temporary clean test worktrees were removed only after clean checks; all logs and the principal PR03 worktree remain.

## Governed evidence

The existing `tools/evidence/generate_engine_core_evidence.py --skip-index` regenerated only its four affected primaries:
`artifacts/core/purity/purity_report.json`,
`artifacts/core/two_run/identity.json`,
`artifacts/core/abba/ab_ba_parity.json`,
`artifacts/core/json_compare/core_result_json_compare.json`.

The canonical updater alone regenerated four primary path proofs and four mirror/checksum companions. The correction therefore changes twelve governed evidence paths, without changing the writer, schemas, Human Index or orientation data. Synthetic evidence remains explicitly bounded to the effective 44-member fixture, never the actual incomplete release.

The updater and all companion checks passed: updater --check, orientation --check, step-log manifest --check, mirror hash, path validation, mirror schema, final LF and canonical JSON --check-only. No generated companion was hand-edited.

## Publication, corrected-source reviews and finding dispositions

The correction is one descendant commit of preserved b33c4172. Its 19-path delta is 383 insertions and 28 deletions. Full main-to-candidate scope is 40 paths, 2,325 insertions and 1,047 deletions. Local and remote object identities match. The completed local validation and all 40 inventory hashes were preserved across publication; no source change or history rewrite accompanied the final push.

The earlier local restore preparation failure, prematurely attempted clean-lane check, off-ref reviewer Unknown error and 401/403 access failure remain recorded in [Result v1.2](https://drive.google.com/file/d/14sNRNIhMFfLJvdOSNAgkcy3attWdVFjk/view?usp=drivesdk). None was a successful review or validation result. Their underlying platform causes are not invented.

Nathan answered “yes” to the exact request to authorize one correction push to the existing PR knowing automatic CI would start before corrected-source review. The engineer made that single non-forced fast-forward to 2badc3c5 and read back the same head on PR #405. This narrowly superseded the review-before-CI order for this publication; it did not waive substantive review or CI, authorize a second push, modify workflow controls, create a new Proceed, change implementation scope or authorize merge. No CI suppression directive was introduced.

The repository automatically started code review on the published head. The engineer did not duplicate that request. One exact native [security-review request](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5663587839) started the separate corrected-head security review.

| Evidence | Actual outcome |
| --- | --- |
| Code review on 2badc3c5 | Began 2026-09-14T12:02:49Z; completed 12:11:56Z in the [current-head review summary](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661172743); the review bot emitted its documented clean/no-findings thumbs-up at 12:11:59Z, reaction ID 504597325; no new inline finding |
| Security review on 2badc3c5 | [Comment 5663646174](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5663646174), posted 2026-09-14T12:09:04Z, explicitly says no security issues found and names reviewed commit 2badc3c5b8 |
| PR03-R02, original P1 | Corrected by the approved implementation and adverse reproducer proof; [resolution record 4004992259](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4004992259) binds the completed corrected-source code/security results; thread resolved |
| Prior source-access finding | The exact object is now the published PR head and both reviews cover it; [resolution record 4004992466](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4004992466) preserves the historical 401/403 limitation; thread resolved |
| PR03-R01 threshold finding | Historical not-applicable resolution preserved; not reopened |
| Unresolved engineering review threads | Zero on readback |

The code-review conclusion uses the integration's native no-findings signal combined with the exact-head review summary, absence of new findings, implemented adverse-case proof and actual thread dispositions. It is not an invented formal APPROVED submission, a generic Completed label by itself, an engineer-authored independent review, a historical source review, or PR-40 acceptance. The security result is the explicit corrected-head review content, not the earlier misrouted off-ref attempt. No source correction was needed after these reviews.

## Final exact-head hosted CI

[CI #3570](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34841280306), run ID 34841280306, was the sole hosted run for the correction. It ran once on exact head `2badc3c5b87e40ddcc984865420e91a2f9695cd1`. The [test job/check](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34841280306/job/103966602586), ID 103966602586, concluded SUCCESS. Run started 2026-09-14T12:02:42Z; check completed 12:15:15Z; workflow final update 12:15:16Z.

| Hosted step / lane | Actual result |
| --- | --- |
| Exact checkout and classification | SUCCESS; exact correction SHA; 40 changed paths; all seven lanes selected |
| Dependencies, pytest and closed environment | SUCCESS; one setup sequence and closed deterministic pins |
| Isolated affected behavioral tests | SUCCESS; 1,970 passed in 137.84 seconds |
| product | SUCCESS; ordering check and 20 passed |
| compat | SUCCESS; CLI/serializer/emitter checks; 62 passed, 3 skipped, 2 xfailed |
| db | SUCCESS; direct runtime contract; 249 passed, 5 warnings |
| rails | SUCCESS; three definition groups 4 / 108 / 39 passed; 124 workflow-integration tests passed |
| evidence | SUCCESS; all governed integrity checks; 111 passed in 400.61 seconds |
| qa | SUCCESS; 488 generic subsystem regression tests passed in isolated source |
| release | SUCCESS; 52 passed; manifest check and exact-source attestation build/verify with --require-clean |
| Final applicability and clean candidate | SUCCESS; actual CI_APPLICABILITY_AND_EXACT_HEAD_OK at 2026-09-14T12:15:12.1986256Z |

The three compatibility skips and two xfails are the existing closed-rails vendor and untouched-scope cases, matching local validation. Counts overlap and are not added. No selected lane or PR03 requirement was waived. The QA/release lanes are engineering regression and attestation checks, not independent QA, Ops, release materialization or promotion.

The complete hosted job log and final structured run/check/review/PR snapshot are retained at `/workspace/scratch/7dd3a4c5f4d6/rs40-final-hosted-ci.log` and `/workspace/scratch/7dd3a4c5f4d6/rs40-final-ci-snapshot.json`. GitHub run/job/comment links remain the externally retrievable evidence. The exact checkout, lane selection, per-lane conclusions, attestation commands and final clean-tree marker were inspected. Earlier [CI #3568](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34824825198) and [CI #3569](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34830070689) remain historical and are not substituted for correction validation.

Code/security review finished before this run concluded. Its start before review completion was the exact ordering exception Nathan approved. No extra push, rerun, CI-suppression directive, workflow change or cancellation was used.

## Complete candidate inventory

SHA-256 values below identify all 40 main-to-candidate changed files at tree `cbc6f35834253dcee3907bf4669bc7cdd1e396a2`. Earlier unchanged PR03 files remain included for complete lineage.

| Repository-relative path | SHA-256 |
| --- | --- |
| `artifacts/core/abba/ab_ba_parity.json` | `a3b88605ff3aa03ffcc643fb8ac0e35c89211320249544ee5f2a0e6a0bad829b` |
| `artifacts/core/abba/ab_ba_parity.json.path_proof.txt` | `bb4bcc29655cfbe51b667df66fa9e9adb05d844210cfba501416aff9263552b7` |
| `artifacts/core/json_compare/core_result_json_compare.json` | `824b962d760a3e6f49f30ffba44da1acec15101d388f65144e0428e68f30a868` |
| `artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` | `a73dc0c26622025503bf7706bb31023ad8d467adbed6901be313a8b4748cfca2` |
| `artifacts/core/purity/purity_report.json` | `62ff57b78b412ce6f8ebab1ab2184116b6e98363f244dc0cf63bf3c53d0551ae` |
| `artifacts/core/purity/purity_report.json.path_proof.txt` | `0d7f721756d6c37337359b3efb2c5cc322ef0a5c4ce81ae012015d649574508b` |
| `artifacts/core/two_run/identity.json` | `cf90a4fe0fa360999f40bdb436b0c29907e1992c292bbd8b993d9d71807c74fa` |
| `artifacts/core/two_run/identity.json.path_proof.txt` | `78f657333d9e6c16b9c3d3042eb73c771236fd0b617f96cbc08c3a244d424ea1` |
| `artifacts/evidence_index.jsonl` | `3cf2bc90a550775b19e9b9e62c8e1c618ed43527629e48597a3973df587c23e3` |
| `artifacts/evidence_index.jsonl.path_proof.txt` | `43691d05a2fe5bc43642026c7912ea3b64a3c211dad14b6833f7afef8d042159` |
| `artifacts/evidence_index.jsonl.sha256` | `175ff7c5fd5bc6accb64ea5cb04d82915bd3a56e84c2c5697392eb1c258cd128` |
| `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | `18093806373dd1060a049e4f49d5f5ab5accce05c6e599ba73cd950826f3222c` |
| `ci/checks/classify_ci_changes.py` | `6e4e610bfe33456adb5c1afdd14cf6272fe3594afdec921e58794b345458e4f6` |
| `docs/schemas/core/engine_core_abba_logs.schema.json` | `f021843dfb6a284f60835150344b7145d9cd44a1a438707ed5c7e2ea1d9f93b4` |
| `docs/schemas/core/engine_core_abba_logs.schema.json.path_proof.txt` | `4a22885f03a485d4b1df2b87c72b71a35ad327646baa9aabdbbe3385259c2271` |
| `docs/schemas/core/engine_core_json_compare_logs.schema.json` | `025faef8d810339409de5e85c1ab9694fcfd4aa106d7da9fae35ac0b2427533e` |
| `docs/schemas/core/engine_core_json_compare_logs.schema.json.path_proof.txt` | `27ecc1ca767e2429673115d8d4bf92b7085a62ad52a9356665211501b086aee3` |
| `docs/schemas/core/engine_core_purity_report.schema.json` | `9017ce9a2a1ae044d361536cbdf23f0e45d58cfff84f1f23d70a5765d60c2db3` |
| `docs/schemas/core/engine_core_purity_report.schema.json.path_proof.txt` | `e8497f4aab5c82f5e63dad4c167d67de1b6dba17ae035ced29bb425c4e891fd6` |
| `docs/schemas/core/engine_core_two_run_logs.schema.json` | `6a11ee9b93f21c7d3491cfeeec6f358f7aabdb34cf22b6148c3e2aa4bbe2ac2b` |
| `docs/schemas/core/engine_core_two_run_logs.schema.json.path_proof.txt` | `792484a66de73338f382ca5e1ec6e8078666ef7df522722e9038b05747a9b058` |
| `engine/config/registry_loader.py` | `5e3146832115003137f6448e25228b83574948d565120697d20ed4254e22135c` |
| `engine/core/__init__.py` | `c86ee4c120f6aeea098ea6cccd80375426a7b6b3b20ed9981014d1c9bb496929` |
| `engine/core/core.py` | `cd07b071b0e3f9056ec6775aa0b717780165f7fe2a2bd2685a934a0363381766` |
| `engine/magic10/__init__.py` | `5363b7dde23ce8a8737b9ba09b06ebcfaa56ca8ce351bb105d65bfa76f06f772` |
| `engine/magic10/calculators.py` | `3f39e63e8b6f7b4b74c3929b04dbd2010524d0ae736c9d412606c64deb894c5a` |
| `engine/magic10/composite.py` | `73c6476405318934192d7f09937c7ee0bdcb79a17de5093d2ff89bb74d48cc8f` |
| `engine/magic10/signals.py` | `d45068a992eb2f40fb3343a825683c4283a6427a26fefe6b2c5d79479a05458e` |
| `tests/config/helpers.py` | `ab12b3d123927f5207acaa32ea6a6b8b7879fa56d76624787a4734bb963982e4` |
| `tests/config/test_production_admission.py` | `8bd41a993f0abb4a8fe3c4822cb69b632ef3578f7d6f612eed41ed96723baf35` |
| `tests/core/test_engine_core_abba.py` | `142843f168f1115b06a7b6e1b5125569396884aeb85a039c82161e3135b261e9` |
| `tests/core/test_engine_core_determinism.py` | `b815e2d4f3e10796a51d6edd167dece949acad3405c9a1b70825780e74cbb0e7` |
| `tests/core/test_engine_core_purity.py` | `e1a230d48a01bb5a34d8507f85359773b33f956d395774cdfd3b3f115d37023c` |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` | `1fbee1ba99552154938c9513cdf7cfb4ceb21bc1117913f84de147e84e67f801` |
| `tests/evidence/test_engine_core_evidence.py` | `b8409a0ac042136a95e79c394e066c24900f4158b49de9cba8ddfae4278451ec` |
| `tests/evidence/test_rails_ci_workflow_integration.py` | `1d878dc455cf1a1589c4628e3484571ea655d885e465413edce77c707178ae92` |
| `tests/m10/test_defs_order.py` | `f9e1a53f347749858290d4bcb70bb11ee455474e109f229c975ee688351f1bb3` |
| `tests/m10/test_m10_symmetry_identity.py` | `4802d857ca4e14b77ca031e52d5cc512ade7bc3aeb23e1424cdd8fded32abc27` |
| `tests/m10/test_thresholds_rounding.py` | `6d5a8286bf68b768e8637754e3c71c52a6675d73a0b1792ace83ef860f7431e4` |
| `tools/evidence/generate_engine_core_evidence.py` | `6cba625cc348497d28adc0f65b595e56d4567b7533777b000237371f53464caa` |

## Preserved conflicts, exclusions and limitations

C040-01 through C040-04 remain approved historical Canon reconciliations by Thoth-17, with their original source/evidence/rationale lineage preserved in the immutable Specification and plan records. C040-05 remains Isis-49 APPROVED alternative A: removal of the legacy precomputed-score/CoreConfig/three-argument success path, preserving separate HDE-DIST008.1 scope. C040-06 remains Isis-50 APPROVED alternative A: accepted 36-row taxonomy, exact Integration exceptions and 16-case conformance without weight/formula changes. Permanent Canon drainage retains its governed maintainers and is non-gating. No register entry is reopened, reclassified or newly decided.

PR02 F01/F02/F03 overlays apply only to accepted PR02. The sole new PR03 authority is the exact approved R02 overlay now drained in PF10 §2.12. PR01/#403 and PR02/#404 remain accepted-final; their tests were used as integration regressions, not their lifecycle work rerun or revised.

The actual release remains the original 15-member manifest, SHA-256 `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`. No release materialization/promotion occurred. Exclude PR04–PR07, OPS01, independent QA/Ops, deployment, live vendor/database access, PF10 edits, Canon drainage, release activation and Epic closure. Preserve all public fields, schemas, identities, mathematics and ownership seams.

The proof is bounded executable equivalence for the eight named owners, not historical raw-source identity, arbitrary in-process tamper resistance, a new deployment protocol or stronger atomicity. Changed comments can preserve executable equality while changing release identity. Unavailable/incompatible import provenance fails closed. Local passing tests and attestation remain distinct from the completed corrected-source reviews and successful exact-head hosted gate. All are now evidenced for this candidate.

## Final recovery point, risks and manual handoff

PR #405 is open, non-draft, unmerged, mergeable, and has `mergeable_state=clean` and `auto_merge=null`. Its three ordered commits are:

1. `dd52ba0dc1224abd629a31d5618104dc5a605832` — original PR03 mechanics and identity implementation.
2. `b33c41721ad2320f71c2cdaf00616e27d36945da` — preserved commit-message correction checkpoint.
3. `2badc3c5b87e40ddcc984865420e91a2f9695cd1` — approved PR03-R02 execution-provenance correction.

The final local and remote head/tree match. The retained worktree is clean at `/workspace/scratch/808bf6c1dac3/pr03` on `hde-epic040-pr03-pure-gate-core`; target main remains `5b2fb8d70924a6710b6261fc0c93d3869fed6380`, tree `e43c2063599e7bc449f20d4ab045d32d95581bf4`. Original archived pre-message-correction commits, reproducer, prior results, approvals, reviews and CI history remain preserved. No source changed after completed local validation, publication or reviews. Current PR commit messages contain no CI-suppression directive.

No unresolved in-scope implementation, engineering review or CI finding remains. Bounded limitations remain: actual incomplete 15-member release; future PR04–PR07/OPS01 obligations; no arbitrary in-process tamper-resistance claim; preserved permanent Canon drainage owners; non-gating prompt-use repository persistence. These are not claimed as completed by PR03. No new approved base, branch, PR, Proceed or PF10 addendum was created.

Nathan / Product Owner performs the manual merge of [PR #405](https://github.com/amthorn78/glow-hdengine-v2/pull/405). The engineer has not merged, enabled auto-merge, scheduled a merge, or started PR-40 and will not poll for the manual action.

After actual manual merge, the exact next native receiver is the **retained whole-change HDE-EPIC040 Implementation Architect in its established read-only lineage-review role**, as immutable instruction §14 specifies. It is not the PR03 engineer or Isis-50. Use [PR-40 — Review PR Work-Unit Lineage — 091326.2](https://app.notion.com/p/3da4590a05eb813c8b47e77f94ff1def?pvs=204), preserving that existing role/session rather than creating or repurposing one.

The conditional invocation carries this result v1.3, instruction v1.0, detailed plan v1.0, current PF10 and the approved/drained R02 decision package, complete approved/accepted lineage, single ordered PR reference #405 and its three commit identities, actual engineering review/CI evidence, PO ordering exception and full unchanged conflict-register lineage. PR-40 independently verifies actual merge and attributable delivered scope, then saves and reads back exactly one PR_WORK_UNIT_LINEAGE_REVIEW with ACCEPT, REJECT or PENDING and its native return. Until actual merge, that review remains conditional. No later merge or acceptance fact is invented here, and this historical MERGE_PENDING result must not be rewritten to fabricate one.

## Prompt-use provenance

Preserve prior PR-10, PR-20, PR-30 and RS-40 usage from the immutable instruction, detailed plan and results v1.1/v1.2. Current continuation remains `GCFPE-USE-HDE-EPIC040-RS-40-20260914-PR03-R02-01`, ecosystem `GCFPE-20260913.1`, Specification v1.1, work unit PR03, same dedicated PR engineer and manual execution.

[RS-40 — Approved Rescope — Resume PR Implementation — 091326.2](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204) and [PR-30 — PR Implementation Proceed — 091326.2](https://app.notion.com/p/3da4590a05eb81c0aee0d0862b242e09?pvs=204) govern the native implementation lifecycle. Primary skill glow-hde-pr-development revision 1.2.0 preserved the existing candidate, prevented unauthorized publication while review access was blocked, and resumed through exact-head reviews and CI after Nathan's narrow ordering authorization. The Notion reference skill was used only to verify the conditional PR-40 source and receiver; it did not execute a review or create a Notion page. Google Drive was used for this complete successor and required readback.

The selected PR-40 page was fetched in full; returned page revision is `2026-09-13T11:35:46.151Z`. It was read solely for conditional handoff preparation, not executed. Repository prompt-provenance persistence remains non-gating for an actually authorized installed writer; no new procedure, schema or path was invented.

NEXT_PROMPT_HANDOFF: conditional PR-40 only after Nathan's actual manual merge; the final operator return supplies this artifact's actual Drive link after successful upload and exact-text readback.
