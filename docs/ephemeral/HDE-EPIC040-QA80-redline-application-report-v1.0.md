---
artifact_type: REDLINE_APPLICATION_REPORT
artifact_id: HDE-EPIC040-QA80-REDLINE-APPLICATION-REPORT
artifact_version: "1.0"
predecessor: none (first application report for this Plan line)
state: PLAN_PENDING_REVISED
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos, continuing QA authority for HDE-EPIC040 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
session_disposition: RETAIN_EXISTING
invocation_binding: EPIC / HDE-EPIC040 / QA-80 / QA_PLAN v1.0 revised to v1.1
prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; read in full at QA-80)
ecosystem_release: GCFPE-20260914.1 (091426.1)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
base_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; 836 lines, 86,864 bytes; SHA-256 f3500c4952d4ee4f2080c2eaeb7b50c3b9fd77bb404d4287fd8806ec048403f3; unchanged)
revised_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.1.md (QA_PLAN v1.1, PLAN_PENDING_REVISED; 951 lines, 122,238 bytes; SHA-256 769e64e27685622e02996d1e19e4995c3893fe769f00a4fe0370b8fddc98e5a5)
decision_source: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md (QA_PLAN_REVIEW v1.1, DENY; SHA-256 cc61419956c1232c0b7340915c39e03c6940acb25deb00272579faaa20f9ad79)
decision_owner: Isis, continuing QA Plan reviewer (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq)
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919)
observed_revision: bf6e8dab4a12cba6cbbe252f38fc2ba0580e5f80 (origin/main)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-80 (QA-80 is not an addendum producer)
---

# HDE-EPIC040 — QA-80 Redline Application Report v1.0

## 1. Result

`PLAN_PENDING_REVISED`. QA Plan v1.1 applies each of the thirteen redlines RL-01 to RL-13 of the QA-70 review v1.1 once. Every finding FND-001 to FND-009 and every other decision item of that review maps to an anchor in v1.1 (§3 to §5). No redline or decision item is unresolved. Every change outside the redline bundle is listed with its cause (§6). The Plan returns to the same continuing Isis at QA-70.

This report approves nothing. QA-80 selects no task, executes no QA, declares no PASS, edits no PF-Canon or PF10 text and produces no addendum.

## Canon relied on

The revised Plan's "Canon relied on" section is the complete record of the canon read for this revision. In summary, each read in full from `docs/pfcanon/` on `main` at `bf6e8da`:

- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`): v13.3.9 read in full at QA-50 in this session (SHA-256 54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d); a QA-80 line diff shows v13.4.2 changes only its version line and index and adds addenda 2.29 to 2.31, read in full at QA-80.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §2.2.6; §2.3; §3.1.1 to §3.3; all of §3.4; §3.5.1 to §3.5.7; §4.4; §11.1 to §11.3; §14.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Unknowns, discovery, deferral, and open rails"; "Database-role evidence boundary"; "Template-safe placeholders and omission syntax"; "Canon precedence for template use"; §A.1 Live QA Plan in full; "Review guardrails" in full; §2 "QA Rails — Open/Close (Final PR)".
- **Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §0; §2.1, §2.2, §2.4, §2.6 to §2.8; §10.
- **HDE CLI/API Vendor Ref** (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`): §7.3.9; §7.4.
- **HDE Build Checklist — Separation** (`docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`): Task HDE-SEPA005 and its subtasks.

In-flight documents read at QA-80: the QA-70 review v1.1 and the QA Plan v1.0 in full; the PO disposition v1.0 and the planning-failure RCA v1.1 in full; the QA Audit v1.0 §4 and §10 to §12; the Implementation Plan v2.1 §8 acceptance table; the PR07 work-unit lineage review v1.0 §1 to §4; the QA-70 review v1.0 §4 and §5; the Alpha state record v1.0; the QA-70 handoff to QA-80.

## 2. Identity verification (QA-80 Execute, step 1)

| Item | Verified value | How |
| --- | --- | --- |
| Pending Plan | `HDE-EPIC040-QA50-QA-PLAN` v1.0, state `PLAN_PENDING`, never approved (review v1.0 APPROVE was rejected by the Product Owner and is history only) | Plan v1.0 front matter; review v1.1 front matter `predecessor`; Alpha state record |
| Wrong-route check | Not an approved base: `WRONG_ROUTE_APPROVED_BASE` does not apply | Same sources |
| Denial and redlines | QA-70 review v1.1, `DENY`, FND-001 to FND-009, RL-01 to RL-13, for Plan v1.0 exactly | Review v1.1 §1, §3, §5; `reviewed_plan` field |
| Decision owner | Isis, the continuing QA Plan reviewer | Review v1.1 front matter; Glow QA Guide §11.1 |
| Author | Kronos, the same session that authored v1.0 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV) | Plan v1.0 front matter; this session |
| Reviewer session | https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq | Review v1.1 `role_session_ref` |
| Change and class | HDE-EPIC040, Epic | Plan v1.0 and review v1.1 front matter |
| PF10 | v13.4.2 at `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`, the only PF10 file in `docs/pfcanon/` | Directory listing and SHA-256 at `bf6e8da` |
| Active addenda relied on | 2.2 to 2.29 as listed in Plan v1.1 §1 and §2.2; 2.29 added for canon location | Plan v1.1 "Canon relied on" |
| Prior application report | None exists for this Plan line | Search of `docs/ephemeral/` for `HDE-EPIC040-QA80` |
| Input artifact hashes at QA-80 | QA Audit v1.0 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df; Live QA Guide v1.0 5a61d77b8301dcee750eedb2916ecae1ec231d540b85028c022fa6d7883a9818; QA readiness v1.0 cc513834b5274d6b5778347a5e0486ec82962f828e993231439e51ebcdf58185; PO disposition v1.0 713e8c1f8c913ec13a59d18a17bb5a697b7cc4fc7ab3ff7635783012da204682; RCA v1.1 a3f76e8c0ef3d1a50e2e30c68e30193237a1b9cb6f08f88cd89f1b9d03bd0381 | `sha256sum` at QA-80 |

## 3. Redline application

Each redline was applied once, to its base region of Plan v1.0. Anchors are line numbers of Plan v1.1 at the SHA-256 above.

| ID | Required outcome (review v1.1 §5) | Disposition | Resulting anchor in v1.1 | What was done |
| --- | --- | --- | --- | --- |
| RL-01 | State the target truthfully; give the four venue-materiality fields for any check the filesystem can affect, or show why venue cannot affect it | APPLIED | Front matter lines 37 to 43; check 3 "Venue evidence" line 513 and its `TOOLING_BLOCKED` venue rule | Target: a local QA console under the closed posture, the CLI-local vendor posture for the vendor step, HumanDesignAPI through `HD_API_BASE_URL`; no deployed service or database. Four venue fields: claim NOT CLAIMED; venue can affect only group G's `tests/evidence/test_evidence_index_missing_state.py` (checkout file modes versus the updater's 644); required evidence `umask` and `stat` of `docs/evidence/INDEX.sha256`; effect: a mode-only failure is `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`, and AC040-08 relies on exact-head CI for that test. The other checks are shown venue-independent |
| RL-02 | Re-scope D9 and D12; mark D11 and D13 blocked by environment and deferred under Glow QA Guide §3.3, with the reactivation condition | APPLIED | §2 lines 115 to 119 | D9 re-scoped to loopback HTTP under the closed posture with `APP_ENV=dev`. D12 removed (RL-08). D11 and D13 marked blocked by environment, deferred, `PARKED`, with the reactivation condition "a future epic defines user-bound QA surfaces once the App user model exists" |
| RL-03 | Replace the four ENV classes with the review's §2 postures; no `APP_ENV=prod` with a local process; rails change only between checks; remove the per-command `SAFE_MODE=0` paragraph; keep the unset lists | APPLIED | §5.2 lines 214 to 234 | Postures Closed, CLI-local vendor and Production (not used), with their canon. Rule "Rails change only between checks, never inside one". Paragraph removed. Unset lists kept: the closed list is the former ENV-C list; the CLI-local vendor list is the former ENV-V list. PF27 "Rails change by check" line added for the vendor check |
| RL-04 | Remove the readiness selection file input; keep `DATABASE_URL` only if RL-08 retains a DB-reading check | APPLIED | §6 lines 244 to 252 | Selection-file row removed. `DATABASE_URL` row removed, because RL-08 was applied by removal and no check reads a database. A sentence records that no database input is requested |
| RL-05 | Class 2 checks to QA/infra (a named delegated executor) outside PO Live QA time; the PO runs class 3 and any class 1 pre-flight the Plan assigns | APPLIED | §7.1 lines 256 to 264 | Named executor: the QA/infra executor, one authorized execution operator/session (Glow QA Guide §11.1) in the repository QA/Verifier role, delegated by the PO and identified in the QA-90 task, runs every class 1 and class 2 check and the `PARKED` records. The PO runs only check 11. No class 1 pre-flight is assigned to the PO. If no QA/infra executor is recorded, class 1 and class 2 checks are not run and the PO does not run them |
| RL-06 | Check 10 under the closed posture with `APP_ENV=dev`, or remove; retitle without "live production"; keep the probes the production route answers identically under dev; for S-22 to S-25 choose option (a) or (b) | APPLIED, option (b) | Check 10, lines 701 to 759; check 9 intent line 693 | Closed posture, `APP_ENV=dev`, retitled "Reader route security over loopback HTTP (closed posture)"; `check_id` kept for identity. Kept S-01 to S-21 and S-26: QA-80 inspection shows the production Reader route, `/internal/version` and the factory 404 read no `APP_ENV`. S-22 to S-25 dropped; their production gating is cited as in-process class 2 coverage in group F (`tests/http/test_reader_post_v1.py`, `tests/http/test_dev_conjunction_http.py`). Option (a) was not chosen: it would add a production-facing, PO-authorized step whose deployed identity is not attributable to the tested source, and HDE-EPIC040 makes no deployment claim |
| RL-07 | Remove check 7 command 1 | APPLIED | Check 7, lines 650 to 659 | Open-pin command removed; remaining commands renumbered 1 to 4; PASS updated to commands 1 to 3; a sentence cites group D's unit test and FND-002 |
| RL-08 | Remove check 13, or re-posture it closed and relabel it | APPLIED, removal | Check 13 stub, lines 823 to 825; §2 D12 line 118; §10 row 13 | Removed from the collection, the manifest and the evidence set. Re-posturing was not chosen: the check would need the shared-database DSN in the console, which the class 1 and class 2 executor does not handle, and it would support no AC040-09 live claim. Q-1 stays covered by checks 9 and 10. The number 13 is kept for traceability |
| RL-09 | Record checks 12 and 14 `PARKED` before execution under Glow QA Guide §3.3, with affected claim and reactivation condition; no commands, inputs or probes | APPLIED | Check 12 lines 803 to 821; check 14 lines 827 to 845; §12 `PARKED` records rule line 435 | Both blocks now carry only the `PARKED` record: reason, controlling source (Glow QA Guide §3.3; review FND-003, RL-09), affected claim (AC040-07 live part; AC040-09 live success), reactivation condition. Commands, inputs, probes, predicates and deliverables removed. The QA/infra executor writes the `PARKED` receipt with `record_check` |
| RL-10 | Add the §3.5.6 class per check and mark the PO subset; label every class 2 check "local/offline (no vendor)"; name existing exact-head CI or PR evidence per closed-rails criterion; update dependencies | APPLIED | §10 lines 337 to 357; §10.1 lines 359 to 366; §10.2 lines 368 to 395; §11 lines 397 to 414 | Class and PO Live QA columns; PO subset is check 11 only. Class 2 checks labeled "local/offline (no vendor)", "Pre-flight / internal", "Handled by QA/infra outside PO's Live QA time". §10.2 names the exact-head CI run of every delivering PR (PR01 to PR06b) and OPS01 from the HDE Build Notes lineage addenda, mapped per criterion from the Implementation Plan v2.1 §8, with the change-aware-lane limit stated. Dependencies updated: checks 12 and 14 `PARKED` with no dependency; check 13 removed |
| RL-11 | Add how a hand operator produces the v2 header and manifest entry, with a step-local preflight; add that no decisive evaluator is composed at run time | APPLIED | §12 lines 418 to 439 | Rule: each decisive predicate is [E] (tracked entrypoint or named baseline command, literal expected value) or [K] (Kronos at QA-110 from captured artifacts); no evaluator or helper program is composed or embedded, so no preapproval smoke validation is needed. Two result layers defined (execution receipt; QA-110 per-task result). Hand-operator mechanism: recording preflight, body and argv capture, one `record_check` invocation with explicit `captured_env`, transactional publication and the `FAIL_TOOLING` route. Pytest runs directly because `run_pytest_check` does not admit `-rs` |
| RL-12 | Check 8: record each skip with its reason; skips contribute no proof; vendor-backed behavior is carried by check 11 | APPLIED | Check 8, line 682 | Skip lines copied with reasons into the PREDICATES section; no proof from skips; the three open-rails skips named from FND-007; vendor behavior carried by check 11 alone |
| RL-13 | §14 mapping consistent with RL-08 and RL-09: parked checks map to no current proof | APPLIED | §14, line 910 | Check 12 removed from HDE-SEPA005.5's current mapping; checks 12 and 14 map to no current proof; check 13 maps to nothing; checks 9 to 11 keep the parent mapping with the PF09 gap |

The review's note "Checks 6 and 11 need no block redline beyond RL-11. Their evaluator steps follow the RL-11 rule" was applied: check 6's evaluator became a `cmp` byte-identity step with [E] and [K] predicates (lines 598 to 639), and check 11's evaluator became byte-identity, secret-scan and parse steps with [E] and [K] predicates and the hand-operator recording (lines 761 to 801).

## 4. Findings coverage

| Finding | Class | Resolved by | Where |
| --- | --- | --- | --- |
| FND-001 local server at `APP_ENV=prod`; production claims without production | Blocker | RL-01, RL-02, RL-03, RL-06, RL-08 | Front matter target; §5.2 (no production posture for a local process); check 10 closed `APP_ENV=dev`; check 13 removed |
| FND-002 mixed `SAFE_MODE=0 ALLOW_NETWORK=0` per command; duplicate of a unit test | Blocker | RL-03, RL-07 | §5.2 rule and removed paragraph; check 7 command 1 removed |
| FND-003 user rows and a PO UUID list | Blocker | RL-02, RL-04, RL-09 | §2 D11 and D13; §6 rows removed; checks 12 and 14 `PARKED` |
| FND-004 DB-backed live Reader refusal counted as AC040-09 | Blocker | RL-02, RL-08 | Check 13 removed; D12 removed |
| FND-005 no class labels; PO executes all; closed-rails suites mapped as acceptance | Blocker | RL-05, RL-10 | §7.1; §10 class and PO columns; §10.1; §10.2 |
| FND-006 decisive evaluators composed at run time | Blocker | RL-11 | §12 decisive-evaluation rule; checks 2, 4, 5, 6, 10, 11 and 15 conformed |
| FND-007 check 8 skips read as vendor coverage | Caveat | RL-12 | Check 8 skips paragraph |
| FND-008 venue premise contradicted by a file-mode failure | Caveat | RL-01 | Front matter venue fields; check 3 venue evidence and rule |
| FND-009 hand operator without a header or manifest mechanism; one refused connection | Caveat | RL-11 | §12 hand-operator recording; check 10 [E] readiness predicate ("no probe is sent before the first HTTP 200") |

Note on FND-008: the `06b04a9` log (`ac040-08-evidence-validators/primary.log` L174 to L177) shows the regenerated mode 420 on the left of the assertion and the checkout mode 438 on the right. The review words it as "420 expected, 438 observed". The Plan states the log's facts: checkout mode 438 (666), regenerated mode 420 (644). The finding and its remedy are unchanged.

## 5. Other decision items of the review

| Item | Review v1.1 decision | Disposition in v1.1 |
| --- | --- | --- |
| C040-09 | `APPROVED_AS_CHANGED`: covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; not newly written decisive evaluators; drainage PF07 §2.8 wording | Carried into the single register, §2.3, with its full history; applied in §2.2 and §12; DD-02 status updated |
| QA50-S01 | Confirmed; synthetic tuples recorded verbatim; default L-51 | Already satisfied by v1.0 §6 birth-tuple row and check 11 deliverables; unchanged |
| QA50-S02 | Moot under FND-003 | Satisfied by RL-04 (no selection input) and RL-09 |
| Check 11 posture | Conforms; only its evaluator is affected | Posture, inputs, forbidden inputs, secret handling, evidence set and exercised-versus-inferred statement kept; evaluator replaced under RL-11 |
| PF07 §2.4 QA binding without `SAFE_MODE` | Not a gap for this Plan (Glow QA Guide §14.5.1) | Already satisfied: the closed posture sets `SAFE_MODE=1` (§5.2) |
| Guide §4.3 and §5 defects | Recorded for Isis; canon governs | The Plan follows canon; §2.1 rows state the supersession. No QA-80 action |
| Epic rails statement missing from Implementation Plan v2.1 | Whole-change IA | No QA-80 action; not a Plan dependency (review v1.1 §3) |
| Coverage after correction (review §4) | AC040-07 live part and AC040-09 live success are not claimable and are reported as not supported for that reason | §2 D11 and D13; checks 12 and 14; §13 new bullet; §14 new accountability rows |
| QA-100 attempts in `06b04a9` | Kronos at QA-110, after the revised Plan | §7.3 "Earlier attempts" bullet: neither counted nor discarded; QA-110 dispositions them |
| Deferred live readiness and live Reader success | Future epic that introduces the App user model | §14 rows with exact PF09 accountability |

## 6. Changes outside the redline bundle

Each change is required either by the QA-80 contract, by a newly supplied authoritative input, or because an applied redline would otherwise leave the Plan contradicting itself.

| ID | Region of v1.1 | Change | Cause |
| --- | --- | --- | --- |
| C-01 | Front matter; title | Version 1.1; predecessor; `PLAN_PENDING_REVISED`; QA-80 prompt; redline source; this report; RCA; PF10 v13.4.2; observed revision; same Isis session; no addendum | QA-80 contract: state, lineage, PF10 version read |
| C-02 | Line 44 | "Plan revision: r2 (artifact v1.1)" | Versioning |
| C-03 | Line 54 | Revision record paragraph | QA-80 lineage |
| C-04 | Lines 56 to 83 | "Canon relied on" section | `AGENTS.md` canon-first rule; HDE Build Notes addendum 2.29 |
| C-05 | §2.2 line 170; §2.3 lines 172 to 188 | Single `CANON_CONFLICT_REGISTER` carried into the Plan: C040-01 to C040-08 byte-identical to the QA Audit §11 rows (verified), C040-09 with its decision and full history | QA-80 contract: preserve one register in the substantive artifact; review v1.1 C040-09 decision |
| C-06 | Provenance, lines 927 to 949 | QA-80 `GCFPE_PROMPT_USES` entry added; QA-50 entry preserved; earlier uses referenced; fenced block removed | QA-80 contract; Plan Templates: a fenced code block in a plan is a mechanical blocker |
| U-01 | §1, PF10 line | v13.4.2 path, numbering note, addendum 2.29 | Newly supplied input: PF10 v13.4.2 |
| U-02 | §1, PF19 and PF07 lines | Sections the redlines rely on added; PF07 §0 added | The redlines' canon (review v1.1 §2) |
| U-03 | §2.2 line 168 | PF10 Addendum 2.29 bullet | Newly supplied input |
| U-04 | §9.1 DD-02, DD-03, DD-05 | C040-09 status; PF10 2.29 supersession and `AGENTS.md` resolution; DD-05 resolved | C040-09 decision; PF10 2.29; `AGENTS.md` at `bf6e8da` |
| Q-01 | Line 46 | Operators by class | RL-05 |
| Q-02 | §2.1 rows §4.2, §4.3, §5, §6 `APP_ENV` asymmetry | Rows point to the revised checks | RL-02, RL-03, RL-06, RL-08, RL-09 |
| Q-03 | §2.2 line 159 | PF10 2.20 bullet: live observation `PARKED` | RL-02, RL-09 |
| Q-04 | §6 `PORT` and delegation rows; line 252 | D9 only; delegation to the QA/infra executor; no database input | RL-04, RL-05, RL-08, RL-09 |
| Q-05 | §7.3 line 281 | "Earlier attempts" bullet | QA-80 contract: preserve attempt identity; review v1.1 §6 |
| Q-06 | §7.4 line 285 | "evaluator code" removed from Moon Loop scope | RL-11 |
| Q-07 | §7.5 lines 289 to 293 | Cleanup matches one server check, the vendor posture and no database | RL-03, RL-04, RL-08, RL-09, RL-11 |
| Q-08 | §8 line 301 | Pytest runs directly; `run_pytest_check` not used | RL-11, RL-12 |
| Q-09 | Checks 1 to 9 and 15: rails and class lines | ENV classes replaced by postures; class labels | RL-03, RL-10 |
| Q-10 | Check 1 command 2 | "apply the closed posture" | RL-03 |
| Q-11 | Check 2 predicates | [E] and [K] split | RL-11 |
| Q-12 | Check 3 | Venue evidence, venue rule, §14.1 anchor | RL-01 |
| Q-13 | Check 4 | Structural probe replaced by digests; structure [K] | RL-11 |
| Q-14 | Check 5 | Binding probe replaced by [K] evaluation | RL-11 |
| Q-15 | Check 6 | Evaluator replaced by `cmp` and [E]/[K] predicates | RL-11 (review: "Their evaluator steps follow the RL-11 rule") |
| Q-16 | Checks 8 and 9 commands | "run directly (§12)" | RL-11, RL-12 |
| Q-17 | Check 9 intent | In-process dev-route gating sentence | RL-06 option (b) |
| Q-18 | Check 11 | Rails line; class; readiness and recording preflight; `cmp`; secret scan also covers the body file (the Plan's §3 requires a scan over all evidence files); parse check; recording; restore at check end; [E]/[K] predicates; failure rules | RL-03, RL-10, RL-11 |
| Q-19 | Check 15 | Manifest verification becomes [K] with digest capture; scope wording follows the removed check 13 | RL-08, RL-11 |
| Q-20 | §13 | 14 checks; `PARKED` state; QA-110 per-task results; §10.2 evidence; proof-class list; deferred claims reported as not supported | RL-02, RL-08, RL-09, RL-11; review v1.1 §4 |
| Q-21 | §14 lines 920 and 921 | Accountability rows for the two deferrals | RL-02, RL-09, under Plan Templates PF09 task accountability (no free-floating deferred work) |

No other region changed. §3, §4, §5.1, §5.3, §7.2, §9 (except DD-02, DD-03, DD-05), §15, the rest of §2 and §8, and the remaining text of every check block are byte-identical to v1.0. The unified diff has 252 removed and 367 added lines.

## 7. Repository changes since the planning basis

`git diff --stat a6002d2 bf6e8da`, excluding `docs/ephemeral/` and `docs/pfcanon/`: 12 files. `.claude/hooks/check_canon_relied_on.py` and `.claude/settings.json` (new agent hooks); `.github/workflows/ci.yml` (a step running `ci/checks/check_agents_md_citations.py`, and its unit test in the product lane); `AGENTS.md`; `ci/checks/check_agents_md_citations.py` (new); `ci/checks/classify_ci_changes.py`; four files under `docs/prompt_ecosystem_management/operating-procedures/`; `tests/evidence/test_rails_ci_workflow_integration.py` (two parametrized cases added; a group G file); `tests/unit/test_check_agents_md_citations.py` (new; outside the HDE-EPIC040 surface). No product code, catalog, schema, manifest or HDE-EPIC040 tool changed. Group G's test count at the tested source may therefore differ from the Audit's count; the Plan's §11 rule records and explains a count difference without failing it.

## 8. Verification performed at QA-80

- Plan v1.1 mechanical lint: no U+2026, no three consecutive periods, no fenced code block, no `run_id`, no `TBD`, `TODO`, `FIXME` or `???`, no CR byte; ends with `ASK OK?` and one LF.
- Render check with markdown-it-py 4.2.0 (CommonMark plus tables, installed in the session scratchpad): 14 tables, each with a consistent column count; 11 ordered lists with the intended start numbers; 48 headings.
- The eight carried register rows C040-01 to C040-08 compared with the QA Audit §11 rows: byte-identical.
- Repository facts newly relied on, inspected read-only at `bf6e8da`: the `APP_ENV` reads of `adapter/http_reader.py`, `adapter/factory.py`, `engine/db/adapter.py` and `engine/http/compat_handler.py`; the dev-route gating tests in `tests/http/test_reader_post_v1.py` and `tests/http/test_dev_conjunction_http.py`; the file-mode handling of `tools/evidence/update_evidence_index.py` and the assertion in `tests/evidence/test_evidence_index_missing_state.py`; the argument grammar, publication rollback and manifest preflight of `tools/qa/qa_harness.py`; the 0600 mode set by `engine/cli/_admin_dump.py`; commit `06b04a9` (read-only fetch).
- Not performed: no QA check, no pytest run, no helper smoke validation (the Plan embeds no helper), no network, vendor or database action.

## 9. CANON_CONFLICT_REGISTER

Carried in Plan v1.1 §2.3, the one register for this change: C040-01 to C040-08 unchanged from the QA Audit v1.0 §11; C040-09 `APPROVED_AS_CHANGED` by Isis in the QA-70 review v1.1 §3 (2026-09-27), with original proposal and decision history. No new conflict was found at QA-80.

## 10. Unresolved items and owners

None from the redline bundle. Carried items keep their owners: Guide §4.3 and §5 (Isis); the epic rails statement of the Implementation Plan v2.1 (whole-change IA); the `06b04a9` attempts (Kronos at QA-110); PF07 §2.8 wording (PF07 maintainer); deferred live readiness and live Reader success (a future epic with the App user model); the QA-90 task that names the QA/infra executor (Product Owner delegation, recorded by Kronos at QA-90 after approval).

## Provenance

GCFPE_PROMPT_USES:

- usage_id: GCFPE-USE-HDE-EPIC040-QA-80-20260927-01 (shared with Plan v1.1)
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; release GCFPE-20260914.1
  - role_stage: continuing Kronos, QA-80
  - capture_time: 2026-09-27T21:37:48Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_PLAN v1.1 (`PLAN_PENDING_REVISED`) and this REDLINE_APPLICATION_REPORT v1.0, routed to QA-70 (the same continuing Isis)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md`)
