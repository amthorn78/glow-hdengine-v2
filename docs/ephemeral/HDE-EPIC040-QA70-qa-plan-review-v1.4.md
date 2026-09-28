---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-EPIC040-QA70-QA-PLAN-REVIEW
artifact_version: "1.4"
predecessor: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.3.md (DENY of Plan v1.1; SHA-256 108a21e2796ac70ffffdd1acbf88f9ea5b2e16759d2834281a75b7f811b05b03)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
decision: APPROVE
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
reviewer: Isis-52, QA Plan reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING (the continuing Isis-52 session, re-entered by the Product Owner's pasted QA-80 handoff)
role_session_ref: Isis-52 (execution identity https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
invocation_binding: EPIC / HDE-EPIC040 / QA-70 / QA_PLAN v1.2
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-70 — Review Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb8143bf26d1459fbbcad7; page as of 2026-09-24T15:55:17.352Z; re-read in full at this invocation, unchanged)
ecosystem_release: GCFPE-20260914.1 (091426.1)
reviewed_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2, PLAN_PENDING_REVISED; 938 lines, 129,319 bytes; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; read in full)
plan_author: Kronos-23 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
redline_application_report: docs/ephemeral/HDE-EPIC040-QA80-redline-application-report-v1.1.md (SHA-256 f05fc1fed20245c2281482013e70a42ee1c17d667923d3475bb32baf9a78dcc2; read in full)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df; read in full)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919; parts read under Canon relied on)
observed_revision: 8eb4ce0 (origin/main). No file outside `docs/ephemeral/` changed since `bf6e8da`, so the code, tests, evidence and canon under review are those the Plan observed
decision_time_utc: 2026-09-28T00:26:24Z
PF10_ADDENDUM_OUTPUT: NONE (initial-mode APPROVE produces no addendum)
---

# HDE-EPIC040 — QA Plan Review v1.4 (QA-70, Isis-52)

## 1. Decision

**`APPROVE`.** QA Plan v1.2 is coherent, complete, bounded and executable. It is the approved whole-change QA Plan for HDE-EPIC040.

- Every one of its 12 checks runs at least one command whose result decides the check's status. No placeholder, removed entry or record-only entry remains.
- The two requirements that cannot run before the Glow App are stated once, as deferrals under Glow QA Guide §3.3, and are not checks.
- This review judged the whole Plan again as a first review would, not only whether the redlines were applied. §3 records the canon tests for each check.

Approval is not task selection, execution, QA PASS, acceptance, merge or closure. No PF10 addendum is produced. The next stage is QA-90, in the continuing Kronos-23 session.

## Canon relied on

Read from `docs/pfcanon/` on `main` (`8eb4ce0`; `docs/pfcanon/` unchanged since `3be23de`). Each section listed was read in full in this session.

**Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Unknowns, discovery, deferral, and open rails"; "Step-log header schema expectations (required; v2)"; "Runbook Check Matrix" and its matrix rules, including "Evidence coverage and optional legacy-token binding (required)"; "Check Blocks", from "Embedded harness checks" to "Split token checkpoints", including the dependency posture and "Path provenance and locus provenance lock"; "Close-out deliverables"; from "Review guardrails": "Source-bound review authority and exact-fix limits", "Hard blockers for plan approval/execution", "Live QA Plan approval materiality discipline", "Plan command, syntax, and example-literalness approval rule" and "Review stability and no-moving-target discipline".

**Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.3; §3.4.8; §3.4.9; §3.4.14; §3.5.1; §3.5.5; §3.5.6; §3.5.7; §4.3; §4.4.1 to §4.4.7; §9.2.15.5; §9.2.15.6; §10.8; §11.1.

**HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`):

- Read in full: "Precedence, versioning, and scope" (1 to 9) and addendum 2.20 "HDE-EPIC040-PR05 — PR Work-Unit Lineage Review v1.0". Addendum 2.20 §5 records readiness as "Delivered offline. There are fake-DB tests only and no live readiness observation, as the Plan requires", and sets no live QA requirement.
- Addendum 2.28 §3 "QA planning obligations" and §5.
- The whole document was searched for `PARKED`, `live qa plan`, `qa plan`, `check block`, `for good measure`, `closed-rails` and `collection-test`, and every hit was read in context. No addendum sets a rule for the form of a check collection, for deferrals, for re-runs of closed-rails tests, for collection tests or for recording a PO-run check. PF10 is silent on these (Precedence §8), so Plan Templates and the Glow QA Guide govern.
- Addenda 2.2 to 2.27 and 2.29 are relied on as the Plan (§1, §2.2) and review v1.1 record them. This review changes nothing about them.

**In-flight documents**, each read in full at this invocation:

- QA Plan v1.2 and redline application report v1.1, plus the unified diff from Plan v1.1 to v1.2.
- QA-80 checkpoint v1.1 and the QA-80 handoff to QA-70 v1.1.
- QA Audit v1.0; Live QA Guide v1.0; QA readiness v1.0; Change Audit Triage v1.0; Reality Audit v1.0; PO disposition v1.0.
- Alpha state record v1.0 "Resumption".
- RCA v1.1 §6.

Read in full earlier in this session and unchanged since: review v1.1, review v1.3, the approval revocation v1.0 and the Alpha feedback brief v1.0. From the Specification v1.1: the AC040-01 to AC040-09 table.

## 2. Redline verification (review v1.3 §6)

| ID | Required outcome | Result | Plan v1.2 anchor |
| --- | --- | --- | --- |
| RL-01 | Checks 12 and 14 out of the collection; deferral kept as a scope treatment with its five items | Applied | §2 "Deferred requirements" table (L140 to L145); no Check Block, matrix row or `PARKED` recording rule remains |
| RL-02 | Every trace of check 13 removed; removal recorded outside the Plan | Applied | Removal recorded in report v1.1 §6 and report v1.0 §3 |
| RL-03 | Consequential regions consistent; §11 counts executed checks only | Applied | §2, §2.1, §2.2, §5.2, §6, §7.1, §10.1, §10.2, §11 (12 checks), check 12 L847 and L855, §13 L865 and L868, §14 L888, L898 and L899 |
| RL-04 | Each re-run of an owner group states what it adds, or is removed | Applied | §10.1 L377; §10.2 table L406 to L415, one true line for each of checks 3, 4, 5, 7, 8 and 9 |
| RL-05 | PO recording path with no composed program; header, manifest, `captured_env` and `FAIL_TOOLING` route kept | Applied | §12 L450 to L455; check 11 commands 0 and 8 (L796, L804). The QA/infra executor records with the tracked `record_check` |
| RL-06 | The decisive-evaluation statement made true | Applied | §12 L444 names the three run-time writers and each one's verifying predicate |
| RL-07 | Collection test of groups A to G before the first receipt | Applied | Check 1 step 7 (L478) and predicates (L489, L495, L497) |
| RL-08 | No commit, push or PR authority; separately authorized storage lane | Applied | §7.2 (L280 to L287) |

Diff scope: the Plan v1.1 to v1.2 diff has 49 hunks. Each lies in a region named by review v1.3 §6, or in a change row of report v1.1 §7 (front matter, revision record, "Canon relied on", provenance, renumbering, and the executor's role in recording check 11). A search of v1.2 finds no reference to a `PARKED` check, a removed check, check 13, check 14, check 15 or D-goals D12 to D14. The remaining `PARKED` mentions (L63, L65, L78, L313, L316) name the canon status only. The `CANON_CONFLICT_REGISTER` in §2.3 is byte-identical to v1.1: both sections hash to SHA-256 08a8aabc22bfd4fd06c69d5e6e5e272544c20f83622da6783d86bb0fa584aca5.

## 3. Whole-plan canon tests

These are the tests of review v1.3 §2:

- **T1.** Every listed check has a mechanical PASS/FAIL predicate, and it runs a command whose result decides its status (Plan Templates matrix rules, "Evidence coverage").
- **T2.** No listed check is a placeholder, a removed entry or a record-only entry, and deferrals appear in scope text (Plan Templates "Evidence coverage"; Glow QA Guide §3.3).
- **T3.** Each check protects something that bound CI or PR evidence does not already prove (Glow QA Guide §3.4.14, §3.4.8).
- **T4.** The assigned operator can execute the check as written (Plan Templates approval materiality).
- **T5.** Every criterion is covered by a step or by a canon-grounded deferral (Glow QA Guide §3.4.14).

| # | check_id | Executor | Command whose result decides the status | T1 | T2 | T3: what the check proves that bound evidence does not | T4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Q | Admission probe; collection test of the 70 files; install, harness and help | Pass | Pass | Preconditions and admission of the tested source. The collection test is Glow QA Guide §3.4.8's pre-receipt requirement | Pass |
| 2 | `step-0b-doc-delta-capture` | Q | `test -s` and `cmp` of the two surfaces | Pass | Pass | The Plan Templates Step-0B obligation | Pass. Its writer is named QA-created scaffolding, verified by [E] and [K] predicates |
| 3 | `ac040-08-evidence-validators` | Q | Nine validators; group G | Pass | Pass | §10.2 row: validators and group G at the tested source, with the evidence graph as it stands there | Pass |
| 4 | `ac040-02-03-catalog-config` | Q | Group A; catalog digests | Pass | Pass | §10.2 row: group A at the tested source; digests bind the bytes Kronos reads | Pass |
| 5 | `ac040-04-05-admission-identity` | Q | `--check-manifest-only`; OPS01 `sha256sum -c`; group B | Pass | Pass | §10.2 row: the 45 members at the tested source against the attested manifest | Pass |
| 6 | `ac040-06-golden-comparison` | Q | Two match runs, one mismatch run, `cmp`, tree digests; group C | Pass | Pass | Byte identity, deliberate mismatch and non-mutation at the tested source | Pass |
| 7 | `ac040-07-gate-ingress-offline` | Q | Three typed refusals; group D | Pass | Pass | §10.2 row: refusals through the real entrypoint | Pass |
| 8 | `ac040-04-09-compat-cli-offline` | Q | Group E | Pass | Pass | §10.2 row: group E at the tested source, with every skip recorded | Pass |
| 9 | `ac040-09-reader-http-in-process` | Q | Group F | Pass | Pass | §10.2 row: group F at the tested source, including dev-route production gating | Pass |
| 10 | `sec-reader-http-live` | Q | Server readiness; 22 probes; `wc -l` of the captures | Pass | Pass | PO Q-1 over loopback HTTP, which no CI run exercises | Pass |
| 11 | `open-rails-showcompat-vendor` | P runs; Q records | Two vendor runs; `cmp`; secret scan; `json.tool` | Pass | Pass | PO Q-2; HDE CLI/API Vendor Ref §7.3.9; HDE Build Notes 2.28 RA-10 | Pass. The PO composes no program; the executor records with the tracked `record_check` |
| 12 | `qa-closeout-deliverables` | Q | Path-proof check mode; updater and path validators | Pass | Pass | Integrity of the QA run's own evidence; coverage accounting | Pass |

T5 passes:

| Criterion or obligation | Covered by |
| --- | --- |
| AC040-01 | Check 12 and the QA-120 Report |
| AC040-02 and AC040-03 | Check 4 |
| AC040-04 and AC040-05 | Checks 1, 5 and 8 |
| AC040-06 | Check 6 |
| AC040-07, offline part | Check 7 |
| AC040-08 | Checks 3 and 12 |
| AC040-09, closed-rails and vendor parts | Checks 8 to 11 |
| AC040-07 live part; AC040-09 live success path | Deferred under Glow QA Guide §3.3 (§2 table). The Specification's AC040-07 already states that "unavailable live facts remain unavailable" |
| HDE Build Notes 2.28 RA-10 ("include the bounded open-rails step, or record the PO/Canon exemption before QA approval") | Check 11 is the open-rails step. The live readiness observation is recorded as a canon deferral before this approval |
| RA-09 | Checks 9 and 10 |
| RA-08 | §2 exclusions and groups A to G |
| PO Q-1 and Q-2 | Checks 9 and 10 (Q-1); check 11 (Q-2) |

## 4. Other review points (QA-70 step 1)

| Point | Result |
| --- | --- |
| Environments and rails | §5.2 uses only the three canon postures of review v1.1 §2, and rails change only between checks. The executor's two recording invocations for check 11 run in its own shell under the closed posture: one before the PO applies the CLI-local vendor posture (command 0), one after the PO restores the closed posture (command 9) |
| Dependencies | §11 is consistent: `d0-discovery` gates every executed check; check 10 needs check 9; check 11 needs check 8; check 12 runs last. A dependency that is not PASS makes the dependent check `TOOLING_BLOCKED`, and it is still recorded |
| Evidence | One primary log per check at its concrete path; manifest and path proofs by the tracked writers; supplementary files bound by SHA-256; no token claims. This matches Glow QA Guide §4.3 and §4.4 |
| PASS/FAIL predicates | Every block states PASS, FAIL_TOOLING and TOOLING_BLOCKED, and states FAIL_BEHAVIOR or says it is not applicable. All follow the Plan Templates status predicates and causal precedence. The [E] and [K] layers are unchanged from v1.1 |
| Recovery, rerun, escalation | §7.3 to §7.5 are unchanged, with one bounded rerun, Moon Loop limits and ESC-10 through QA-110 |
| Report and RCA | §13 matches Plan Templates "Close-out deliverables": `BLOCKED/UNEXECUTABLE` is permitted, deferrals are recorded as deferrals, and the completion states are kept separate. It also matches Glow QA Guide §9.2.15.5 |
| Deferral | The §2 table meets Plan Templates "valid deferral" (an unmet prerequisite that QA may not create) and Glow QA Guide §3.3 ("explicitly called out in epic-level QA plans and deferred"). Each row gives its reason, controlling source, decision reference, affected claim and reactivation condition, and §14 carries its PF09 accountability |
| Evidence storage | §7.2 confers no commit, push or PR authority, as Glow QA Guide §3.4.9 requires |
| Locus provenance | The revision adds no repository locus. The recording files are under `/tmp`, outside the repository, and are not acceptance surfaces (Glow QA Guide §3.4.8). Their content enters the governed primary log through `record_check` |
| PF10 | No contradiction found with the parts read (Precedence; 2.20; 2.28 §3 and §5) or in the whole-document search. The other addenda in Plan §2.2 are relied on as the Plan and review v1.1 record them |

## 5. Repository facts verified (read-only, at `8eb4ce0`)

| Fact the revised text relies on | Result | How |
| --- | --- | --- |
| `tools/qa/qa_harness.py` has no command-line entrypoint | Holds: no `__main__`, `argparse` or `main()`, and no `pyproject.toml` script | `grep` |
| `record_check` publishes the primary log and the manifest together, verifies both, and rolls back on error | Holds: `record_check` → `record_check_family` → `_publish_with_rollback` | Read |
| An explicit `captured_env` is used when given; admitted keys are `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV` | Holds (`_captured_env`, `ADMITTED_ENV_KEYS`, `DETERMINISM_ENV_PINS`) | Read |
| PASS requires exit code 0 and an empty reason; any other status requires a reason; `command_provenance` is `Not executed` exactly when no command ran | Holds (`CheckResult.__post_init__`, `_primary_log_content`). The recording preflight's `CheckResult` is valid as described | Read |
| All 12 `check_id` values fit the harness pattern `[a-z0-9][a-z0-9._-]*` | Holds | Read |
| The 70 collection-test files exist and have unique basenames | Holds: 70 of 70 present, no duplicate basename | `git cat-file`; basename comparison |
| One collection of those 70 files succeeds | QA Audit §4.4: 2,090 tests, rc 0 at `a6002d2`. Since then only `tests/evidence/test_rails_ci_workflow_integration.py` changed among them (report v1.0 §7) | Audit |
| Release `1.3.0`, `2026-08-24T18:04:49Z`, 45 members, and the admission pins | Holds (`engine/config/registry_loader.py` L398 to L399) | Manifest parse; read |
| OPS01 ledger | 7 of 7 OK, rc 0 | `sha256sum -c SHA256SUMS`, read-only |
| Attestation binding | `release_id` = `manifest_sha256` = `sha256sum catalog/manifest.json` = `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; `validation_result` PASS; `release_admission` `PR06R_B_FINAL_PASS` | JSON parse |
| Readiness refusal tokens and `GOLDEN_COMPARISON_MISMATCH` | Present in their tools | `grep` |

Not done: no pytest collection or test run (this container has Python 3.11 and no test dependencies; the Plan requires 3.12), no QA check, and no network, vendor or database action.

## 6. Findings

No blocker, and no caveat that needs a Plan revision. The notes below are for the QA-90 task author. None changes a proof target, rails posture, evidence identity or predicate. Plan Templates classes them as operator caution, in-flight normalization or nit.

| ID | Class | Provenance | Note | For QA-90 |
| --- | --- | --- | --- | --- |
| N-101 | Operator caution | Introduced by current revision (§12 item 1, L451) | The executor creates `/tmp/hde-epic040-open-rails-showcompat-vendor/` with `mkdir -p`, and the preflight appends to `body.txt`. A `body.txt` or `argv.txt` left from an earlier attempt would mix two attempts in one primary log | The check 11 task requires both files to be absent before the recording preflight. A rerun starts from an empty directory |
| N-102 | In-flight normalization | Unchanged text (check 11 command 6, L802); first noted as review v1.2 N-01 (evidence only) | `grep -c -F "$HD_API_KEY"` puts the secret on a process argv while `grep` runs. The Plan now has a second operator session working in the same console (§7.1, §12) | The check 11 task gives the standard-input form, for example `printf '%s\n' "$HD_API_KEY" \| grep -c -F -f - <file>` |
| N-103 | Operator caution | Introduced by current revision (§7.1, §12) | The QA/infra executor must work in the PO's QA console: it reads the PO's `/tmp` files and records into the same checkout | The delegation record names the executor and states that it runs in the PO's QA console |
| N-104 | Note | Unchanged text (§7.3) | §7.3 defines attempt 1 as the QA-90 task's first execution, and neither counts nor discards the `06b04a9` attempts. The Alpha state record v1.0 ("Resumption") records those attempts as not carried forward. Their disposition is Kronos's (Glow QA Guide §11.1) | Each task states its attempt number and how the `06b04a9` attempts are treated |
| N-105 | Nit | Introduced by current revision (§10.2 L406) | "Six class 2 checks re-run an owner test group": check 6 also runs group C, and its added proof is stated in its own block | None |

## 7. Carried decisions

- `CANON_CONFLICT_REGISTER`: carried in Plan v1.2 §2.3, the one register for this change. C040-01 to C040-08 are unchanged; C040-09 is `APPROVED_AS_CHANGED` (review v1.1 §3). No new conflict was found, and this review makes no register decision.
- QA50-S01 (synthetic birth tuples recorded verbatim) and the check 11 posture: as decided in review v1.1, and unchanged. Check 11 satisfies the Glow QA Guide §3.5.5 production-affecting open-rails minimum and PO Q-2.
- Review v1.2's approval is revoked, and its QA-90 handoff is void (revocation record §3). The QA-90 task collection v1.0 and the `06b04a9` evidence are not carried forward (Alpha state record v1.0).

## 8. Unresolved items and owners

| Item | Owner |
| --- | --- |
| QA-90 tasks: task selection, the delegation record naming the QA/infra executor, and the evidence-storage lane (Plan §6, §7.2) | Kronos-23 at QA-90. Selection and delegation are the Product Owner's |
| Execution notes N-101 to N-104 | Kronos-23 at QA-90 |
| Disposition of the `06b04a9` attempts | Kronos (Plan §7.3) |
| Guide §4.3 and §5 defects | Isis (recorded; canon governs) |
| Epic rails statement missing from Implementation Plan v2.1 | Whole-change IA (carried, non-blocking) |
| Glow Infrastructure §2.8 wording (C040-09) | PF07 maintainer (documentation only) |
| Deferred live Gate readiness and live Reader success | A future epic with the App user model (Glow QA Guide §3.3); PF09 rows in Plan §14 |
| Prompt-level causes of the earlier approvals | GCFPE-MGMT-10, through the Alpha feedback brief |
| QA-70 records not yet on `main`: reviews v1.2, v1.3 and v1.4, the approval revocation, the Alpha feedback brief and their handoffs, all on branch `claude/nice-mayer-tf9l4c` | Product Owner (merge) |

## Nonclaims

This review selects no task, executes no QA, declares no PASS, and grants no vendor, database, commit or merge authority. It edits no PF-Canon, PF10 text or prompt, and produces no PF10 addendum. The QA Plan approval is this review's decision, not a merge. Merging preserves the record and approves nothing (D21-C).

## Provenance

GCFPE_PROMPT_USES:

- usage_id: GCFPE-USE-HDE-EPIC040-QA-70-20260928-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - components: HDE-SEPA005, HDE-SEPA005.1 to HDE-SEPA005.5; AC040-01 to AC040-09
  - prompt: QA-70 — Review Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb8143bf26d1459fbbcad7; page as of 2026-09-24T15:55:17.352Z; release GCFPE-20260914.1
  - role_stage: Isis-52, QA-70 (review of revised pending Plan v1.2)
  - capture_time: 2026-09-28T00:26:24Z
  - execution_identity: https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2
  - result: QA_PLAN_REVIEW v1.4, APPROVE, routed to QA-90 (Kronos-23)
  - task_and_attempt_mapping: none (QA-70 creates no task)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md`; owner: the authorized repository writer under that procedure once installed)
- Earlier entries, each in its own artifact: GCFPE-USE-HDE-EPIC040-QA-70-20260927-01 (review v1.0, rejected), -02 (review v1.1, DENY), -03 (review v1.2, APPROVE revoked), -04 (review v1.3, DENY)
