---
artifact_type: REDLINE_APPLICATION_REPORT
artifact_id: HDE-EPIC040-QA80-REDLINE-APPLICATION-REPORT
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-QA80-redline-application-report-v1.0.md (application of the QA-70 review v1.1 to Plan v1.0; preserved unchanged; SHA-256 6dc9c9fc7258ad78e3f8c25bc14a4eba6ad2eb20f6aed435ee89c648fae10a10)
state: PLAN_PENDING_REVISED
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
session_disposition: RETAIN_EXISTING
invocation_binding: EPIC / HDE-EPIC040 / QA-80 / QA_PLAN v1.1 revised to v1.2
prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
base_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.1.md (QA_PLAN v1.1, PLAN_PENDING_REVISED; 951 lines, 122,238 bytes; SHA-256 769e64e27685622e02996d1e19e4995c3893fe769f00a4fe0370b8fddc98e5a5; unchanged)
revised_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2, PLAN_PENDING_REVISED; 938 lines, 129,319 bytes; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010)
decision_source: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.3.md (QA_PLAN_REVIEW v1.3, DENY; SHA-256 108a21e2796ac70ffffdd1acbf88f9ea5b2e16759d2834281a75b7f811b05b03)
revocation_record: docs/ephemeral/HDE-EPIC040-QA70-approval-revocation-v1.0.md (SHA-256 9a22372807085375bf507f101100ee52a2159e9598999f6f414fafefc1286d3c)
decision_owner: Isis-52, QA Plan reviewer for HDE-EPIC040 (execution identity https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2), who replaced Isis-51 by Product Owner direction
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919)
observed_revision: e1ab8ba9931ff0a6de86fe16fc8e2ee9398be916 (origin/main); the review v1.3, the revocation record v1.0 and the Alpha feedback brief v1.0 were read from branch claude/nice-mayer-tf9l4c at b245b0ce57a6e361efd1b26eb8f03241cdd066e8, where they are recorded and not yet on main
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-80 (QA-80 is not an addendum producer)
---

# HDE-EPIC040 — QA-80 Redline Application Report v1.1

## 1. Result

`PLAN_PENDING_REVISED`. QA Plan v1.2 applies each of the eight redlines RL-01 to RL-08 of the QA-70 review v1.3 once. Every finding FND-101 to FND-107 and every other decision item of that review maps to an anchor in v1.2 (§3 to §5). No redline or decision item is unresolved. The entries removed from the collection and the renumbering are recorded here, and only here (§6), as the review directs. Every change outside the redline bundle is listed with its cause (§7). The Plan goes to Isis-52 at QA-70.

The collection is now the 12 checks that the review v1.3 §5 names, with the same `check_id` values in the same order (§9).

This report approves nothing. QA-80 selects no task, executes no QA, declares no PASS, edits no PF-Canon or PF10 text and produces no addendum.

## Canon relied on

The revised Plan's "Canon relied on" section is the complete record. For this revision, each read in full from `docs/pfcanon/` on `main` at `e1ab8ba`, which is identical to `bf6e8da` for `docs/pfcanon/`:

- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Unknowns, discovery, deferral, and open rails"; "Step-log header schema expectations (required; v2)"; "Runbook Check Matrix" and its matrix rules, including "Evidence coverage and optional legacy-token binding (required)"; "Check Blocks", from "Embedded harness checks" to "Close-out deliverables"; from "Review guardrails": "Source-bound review authority and exact-fix limits", "Hard blockers for plan approval/execution", "Live QA Plan approval materiality discipline", "Plan command, syntax, and example-literalness approval rule" and "Review stability and no-moving-target discipline".
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.3; §3.4.8; §3.4.9; §3.4.14; §3.5.1; §3.5.5 to §3.5.7; §4.3; §4.4.1 to §4.4.7; §9.2.15.5; §10.8; §11.1.
- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`): the whole document searched for the terms listed in the Plan's "Canon relied on", every hit read in context; addendum 2.28 §3; addendum 2.29. PF10 is silent on the shape of a QA Plan's check collection, the `PARKED` status, re-runs of closed-rails tests, collection tests, the recording of a PO-run check and the storage of QA evidence, so Plan Templates and the Glow QA Guide govern them.

In-flight documents read in full at this invocation: the QA-70 review v1.3; the approval revocation v1.0; the Alpha feedback brief v1.0; QA Plan v1.1; the redline application report v1.0; the QA-70 review v1.1; the QA Audit v1.0 loci L-40 to L-43. Not read and not relied on: the QA-70 review v1.2 and its QA-90 handoff, which the revocation record makes history only and void, and which the handoff to this invocation excludes as inputs. Repository observation, read-only, at `e1ab8ba`: `tools/qa/qa_harness.py`.

## 2. Identity verification (QA-80 Execute, step 1)

| Item | Verified value | How |
| --- | --- | --- |
| Pending Plan | `HDE-EPIC040-QA50-QA-PLAN` v1.1, state `PLAN_PENDING_REVISED`, not approved: the Product Owner revoked the QA-70 review v1.2 `APPROVE` on 2026-09-27 | Revocation record §1 and §3; review v1.3 front matter `predecessor` |
| Wrong-route check | Not an approved base: `WRONG_ROUTE_APPROVED_BASE` does not apply | Same sources |
| Denial and redlines | QA-70 review v1.3, `DENY`, FND-101 to FND-107, RL-01 to RL-08, for Plan v1.1 exactly: its `reviewed_plan` SHA-256 equals v1.1's | Review v1.3 §1, §3, §6 and front matter; `sha256sum` of v1.1 |
| Decision owner | Isis-52, `NEW_DEDICATED` by Product Owner direction, replacing Isis-51, who makes no further QA-70 decision on this Plan | Revocation record §3; review v1.3 front matter `session_disposition`, `replaced_reviewer` |
| Author | Kronos-23, the session that authored v1.0 and v1.1 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV) | Review v1.3 front matter `plan_author`; this session |
| Reviewer session | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 | Review v1.3 `role_session_ref` |
| Change and class | HDE-EPIC040, Epic | Plan v1.1 and review v1.3 front matter |
| PF10 | v13.4.2 at `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`, unchanged since v1.1 | `git diff` of `docs/pfcanon/` between `bf6e8da` and `e1ab8ba` is empty |
| Active addenda relied on | 2.2 to 2.29 as listed in Plan v1.2 §1 and §2.2; no addendum speaks to the topics of the v1.3 redlines | Plan v1.2 "Canon relied on" |
| Prior application report | v1.0, the application of the QA-70 review v1.1 to Plan v1.0, read in full; its §10 names no unresolved redline item | Report v1.0 |
| Unresolved items from the review v1.1 | None. Its redlines were applied in v1.1, and the review v1.3 changes only the regions its own redlines name | Report v1.0 §3; review v1.3 §6 |
| Excluded inputs | The QA-70 review v1.2 and its QA-90 handoff: revoked and void | Revocation record §3; the handoff to this invocation |
| Input hashes at this invocation | Review v1.3 108a21e2796ac70ffffdd1acbf88f9ea5b2e16759d2834281a75b7f811b05b03; revocation record v1.0 9a22372807085375bf507f101100ee52a2159e9598999f6f414fafefc1286d3c; Alpha feedback brief v1.0 6a1c5ec867f146a1642ed749bf745efe0bb0eabefee3a3f4be53f1331942bdfd; review v1.1 cc61419956c1232c0b7340915c39e03c6940acb25deb00272579faaa20f9ad79; Plan v1.1 769e64e27685622e02996d1e19e4995c3893fe769f00a4fe0370b8fddc98e5a5; report v1.0 6dc9c9fc7258ad78e3f8c25bc14a4eba6ad2eb20f6aed435ee89c648fae10a10; QA Audit v1.0 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df | `sha256sum` at this invocation |

## 3. Redline application

Each redline was applied once, to its base region of Plan v1.1. Anchors are line numbers of Plan v1.2 at the SHA-256 in the front matter.

| ID | Required outcome (review v1.3 §6) | Disposition | Resulting anchor in v1.2 | What was done |
| --- | --- | --- | --- | --- |
| RL-01 | Remove checks 12 and 14 from the collection, the matrix, the Check Blocks, the manifest expectations and the recording rules; no primary log or manifest entry; keep the deferral as a stated scope treatment with its reason, controlling source, decision reference, affected acceptance claim and reactivation condition | APPLIED | §2 lines 138 to 145; §10 lines 355 to 368; §12 common rules lines 438 to 459; check 12 predicates line 847; §11 line 421 | Both Check Blocks, both matrix rows and the §12 "`PARKED` records" rule removed. The close-out check's manifest predicate now expects exactly one entry for each of checks 1 to 11. §2 carries a "Deferred requirements" table that gives the five items for each requirement, and a sentence classing each as a valid deferral under Plan Templates "Unknowns, discovery, deferral, and open rails" |
| RL-02 | Remove every trace of check 13; its removal stays recorded in report v1.0 §3 (RL-08) and in the next application report | APPLIED | §2 lines 115 to 126; §10 lines 355 to 368; §11 line 421; §13 line 865; §14 line 888 | The D12 scope line, matrix row 13 and the CHECK 13 stub removed, as were the "number 13 is removed" notes of §11 and §13 and the §14 sentence "Check 13 is removed and maps to nothing". The removal is recorded in §6 here |
| RL-03 | Make the consequential regions consistent with RL-01 and RL-02: no text refers to a `PARKED` check, a removed check or its number; the deferrals stated once in §2 (five items), in §13 (not supported, not failures) and in §14 (their PF09 rows, kept in substance); §11 counts only executed checks | APPLIED | §2 lines 126, 138, 140 to 145; §2.1 line 156; §2.2 line 173; §5.2 lines 238 and 244; §6 line 263; §7.1 line 275; §10.1 line 376; §10.2 line 417; §11 lines 421 to 430; check 12 lines 847 and 855; §13 lines 865 and 868; §14 lines 888, 898 and 899 | D11 to D13 removed from the scope list, and the close-out D-goal renumbered (§6). §2.1, §2.2, §5.2 and §10.2 point to "§2, deferred requirements" in place of the parked checks. §6 and §7.1 no longer assign `PARKED` records. §10.1 lists class 2 as checks 3 to 10 and 12. §11 counts 12 checks and drops the two dependency rows. The close-out check expects checks 1 to 11 and path proofs for checks 1 to 12. §13 counts 12 checks, drops the `PARKED` marking category that existed only for the parked checks, and reports the two live parts as not supported under the §2 deferral. §14 keeps both PF09 rows in substance and maps the deferrals to no current proof |
| RL-04 | For each class 2 check that re-runs an owner test group or validator (checks 3, 4, 5, 7, 8, 9), state in one line what the local run proves that the bound CI and PR evidence of §10.2 does not, or remove the re-run | APPLIED | §10.1 line 377; §10.2 lines 406 to 415 | New table in §10.2, one line per check. Each line states the whole-surface run at the one tested source, which is true for all six under the §10.2 limit, plus the check-specific addition where one exists: check 3, the evidence graph as it stands at the tested source; check 4, the digests that bind the catalog bytes Kronos reads; check 5, the audit of the 45 release members at the tested source against the manifest whose digest Kronos binds to the OPS01 attestation; check 7, the readiness command's typed refusals through its real entrypoint; check 8, every skip with its reason; check 9, the production gating of the dev routes that check 10 does not probe. Every line is true, so no re-run was removed |
| RL-05 | Give the PO a recording path for check 11 that the PO can execute without composing a program; keep the v2 header, the manifest entry, `captured_env` with the values in force during the vendor runs and the `FAIL_TOOLING` route; stay within tracked entrypoints and Glow QA Guide §3.5.5; add no PO Live QA workload | APPLIED | §12 lines 450 to 455; check 11 command 0 line 796 and command 8 line 804 | The QA/infra executor makes both harness invocations, the recording preflight before the PO's commands and `record_check` after them, in its own shell in the same QA console checkout under the closed posture, with the tracked `record_check` that records every other check. The PO's part is to keep `body.txt` and `argv.txt` in `/tmp/hde-epic040-open-rails-showcompat-vendor/`, which v1.1 already required (item 2). `body.txt` is now appended by shell redirection. The two `python -c` programs the PO had to compose in v1.1 are gone. Kept: the v2 header and manifest entry (`record_check`), `captured_env` given explicitly from the values the body file records for commands 3 and 4, and the `FAIL_TOOLING` route (item 4). Added item 5: a secret value found by command 6 is quarantined by the PO, and the executor records `FAIL_TOOLING` from the files that scanned zero. Why this mechanism: `tools/qa/qa_harness.py` has no command-line entrypoint at `e1ab8ba`, so any PO-run recording would need a composed program. Glow QA Guide §3.5.5 makes the QA console the place where offline work runs. The executor already records every other check with this mechanism. A new recording script was not chosen, because Glow QA Guide §3.4.8 forbids newly invented runners |
| RL-06 | Make the §12 decisive-evaluation statement true: name the run-time writers of check 2 command 2, check 6 command 4 and check 15 command 2 as QA-created evidence-assembly writers, state that none evaluates a decisive predicate, and name the predicate that verifies each one's output; cite Glow QA Guide §3.4.8 and Plan Templates approval materiality | APPLIED | §12 line 444 | The false sentence ("this Plan embeds no helper program") is replaced. The three writers are named (the close-out check is check 12 in v1.2), with the verifying predicate for each: `test -s`, `cmp` ([E]) and the content predicates ([K]) for check 2; the [K] single-leaf predicate for check 6; `cmp` after the append ([E]) for check 12. The rule states that a defect in one is a QA evidence-assembly defect classified `FAIL_TOOLING` and correctable under §7.4, and that none is an execution-critical helper. It cites Glow QA Guide §3.4.8 and Plan Templates "Live QA Plan approval materiality discipline" |
| RL-07 | Before `d0-discovery` records its receipt, collection-test the complete selected selector set (the files of pytest groups A to G) at the tested source; add the predicate and map its failure to the existing status rules | APPLIED | Check 1 lines 478 to 481 and 489 to 497 | New step 7: one `python -m pytest --collect-only -q -p no:cacheprovider` invocation over the 70 files of groups A to G, as checks 3 to 9 list them, with exit code and collected count recorded. The final decisive command stays the admission command, now step 8. PASS requires rc 0 and a recorded count. rc 5 or a listed file not found is `TOOLING_BLOCKED`, as for the group checks. Any other non-zero code, for example rc 2 for a collection error, is `FAIL_TOOLING`, never `FAIL_BEHAVIOR`, because collection exercises no product behavior |
| RL-08 | State that the Plan confers no commit, push or PR authority and that evidence storage uses the separately authorized lane that the QA-90 task or the Product Owner names (Glow QA Guide §3.4.9); keep the bounded file list and the prohibitions as the limit on that lane | APPLIED | §7.2 lines 280 to 287 | Retitled "Evidence storage (separately authorized lane)". The section quotes Glow QA Guide §3.4.9, names the lane, and keeps the file list and every prohibition, now as the limit on what that lane may store |

## 4. Findings coverage

| Finding | Class | Resolved by | Where in v1.2 |
| --- | --- | --- | --- |
| FND-101: checks 12 and 14 run nothing and can only be `PARKED` | Blocker | RL-01, RL-03 | Checks and rows removed; §2 deferred requirements; §11, §13, §14 |
| FND-102: check 13 remains as a placeholder row and block | Blocker | RL-02, RL-03 | Removed everywhere; recorded in §6 here |
| FND-103: re-runs of CI-covered groups state no added value | Caveat | RL-04 | §10.1 line 377; §10.2 lines 406 to 415 |
| FND-104: the PO must compose two `python -c` programs to record check 11 | Caveat | RL-05 | §12 lines 450 to 455; check 11 commands 0 and 8 |
| FND-105: "this Plan embeds no helper program" is false | Caveat | RL-06 | §12 line 444 |
| FND-106: no collection test before the first governed receipt | Caveat | RL-07 | Check 1 step 7 and predicates |
| FND-107: §7.2 reads as granting commit and PR authority | Caveat | RL-08 | §7.2 |

## 5. Other decision items of the review v1.3

| Item | Review v1.3 decision | Disposition in v1.2 |
| --- | --- | --- |
| §2 canon tests T1 to T5 | T5 passes; T1 and T2 fail only for checks 12 to 14; T3 partial for checks 3, 4, 5, 7, 8, 9; T4 caveats for checks 1, 2, 6, 11, 15 | Addressed by RL-01 to RL-07; the resulting collection is the one the review §5 states (§9 here) |
| §4 rail postures and rails change only between checks | Keep | §5.2 unchanged except the RL-03 cell edits at lines 238 and 244. The QA/infra executor's recording invocations run in its own shell under the closed posture, outside the PO's commands, and make no network, vendor or database call (§12 line 450) |
| §4 executors by class; PO subset = check 11; class labels | Keep | Kept. §7.1 adds the executor's recording of check 11 (RL-05); the PO subset is unchanged |
| §4 check 11 posture, inputs, forbidden inputs, secret handling, evidence set, exercised-versus-inferred statement | Keep | Unchanged; only commands 0 and 8 changed (RL-05) |
| §4 check 10 under the closed posture, S-22 to S-25 retired | Keep | Unchanged |
| §4 [E] and [K] layers | Keep | Unchanged; RL-06 adds the writer statement to the same rule |
| §4 venue rule of check 3 | Keep | Unchanged |
| §4 rerun, Moon Loop, cleanup and recovery, `06b04a9` attempts | Keep | §7.3 to §7.5 unchanged |
| §4 deferral of the live part of AC040-07 and the live success path of AC040-09 | Correct as a deferral; only the form as checks is defective | Kept as a deferral, stated in §2 as a scope treatment (RL-01, RL-03) |
| §4 `CANON_CONFLICT_REGISTER` | Carried unchanged; no new conflict | §2.3 byte-identical to v1.1 (§9 here) |
| §4 review v1.2 note N-01 (secret on the `grep` argv in check 11 command 6) | Evidence only; available as an in-flight syntax normalization under §12; no redline | No change; check 11 command 6 is unchanged |
| §7 unresolved items and owners | Carried | §11 here |
| Decisions carried from the review v1.1 (C040-09 `APPROVED_AS_CHANGED`, QA50-S01, QA50-S02, check 11 posture, PF07 §2.4 binding) | Unchanged by the review v1.3 | Unchanged in v1.2, as report v1.0 §5 records them |
| Alpha feedback brief v1.0 | A request to GCFPE-MGMT-10 for prompt changes; not a Plan requirement | Not applied as a rule. v1.2 matches its item 3 in effect, because the review v1.3 redlines require the same outcome: checks that run nothing are dropped, and their IDs are recorded here, not as placeholders |

## 6. Removed entries and renumbering

Recorded here and not in the Plan (review v1.3 §6).

| v1.1 entry | v1.1 anchor | Disposition | Evidence identity |
| --- | --- | --- | --- |
| Check 12 `live-db-gate-readiness` (`PARKED`) | Matrix row line 354; CHECK 12 block lines 803 to 821; §11 row line 408; §2 D11 line 117 | Removed (RL-01). The requirement is the first deferred requirement of v1.2 §2 | Never executed. No primary log or manifest entry exists, and none is expected |
| Check 13 `live-db-reader-refusal` (removed placeholder) | Matrix row line 355; CHECK 13 stub lines 823 to 825; §2 D12 line 118 | Removed (RL-02). Its removal from the collection by the QA-70 review v1.1 RL-08 is recorded in report v1.0 §3 | Never executed |
| Check 14 `live-db-reader-success` (`PARKED`) | Matrix row line 356; CHECK 14 block lines 827 to 845; §11 row line 409; §2 D13 line 119 | Removed (RL-01). The requirement is the second deferred requirement of v1.2 §2 | Never executed |

| v1.1 | v1.2 | Identity |
| --- | --- | --- |
| Check 15 | Check 12 | `check_id` `qa-closeout-deliverables` unchanged; its evidence paths are keyed by `check_id` and unchanged |
| D-goal D14 | D-goal D11 | The close-out D-goal |
| Check 1 steps 7, 8 and 9 (admission, ignore rules, recording) | Steps 8, 9 and 10 | New step 7 is the collection test (RL-07). The final decisive command is still the admission command |

Checks 1 to 11 keep their numbers and `check_id` values. The checks 1 to 10 attempts in `06b04a9` keep their numbering (Plan §7.3).

## 7. Changes outside the redline bundle

Each change is required by the QA-80 contract, by the `AGENTS.md` canon-first rule, or because an applied redline would otherwise leave the Plan contradicting itself.

| ID | Region of v1.2 | Change | Cause |
| --- | --- | --- | --- |
| C-01 | Front matter lines 1 to 34; title line 36 | Version 1.2; predecessor v1.1 with its revocation and DENY; earlier version v1.0; author Kronos-23; invocation binding; redline source review v1.3; revocation record; earlier redline source review v1.1; this report; observed revision `e1ab8ba`; review route Isis-52 | QA-80 contract: state, lineage, PF10 version read, reviewer |
| C-02 | Lines 47 to 49 | Plan revision r3; date; operators line adds the executor's recording of check 11 | Versioning; RL-05 |
| C-03 | Line 57 | Revision record, including the rule that a redline cited without a review version is a redline of the review v1.1 | QA-80 lineage; both reviews number their redlines from RL-01 |
| C-04 | Lines 59 to 92 | "Canon relied on": this invocation's reads, the PF10 search, six new topic rows and this invocation's in-flight reads | `AGENTS.md` canon-first rule |
| C-05 | Lines 905 to 936 | New QA-80 `GCFPE_PROMPT_USES` entry; the v1.1 and QA-50 entries preserved; earlier uses updated with the QA-70 entries -03 and -04 | QA-80 contract |
| Q-01 | §6 line 263 | The delegation row covers D0 to D9, D11 and the recording preflight and recording of D10 | RL-01, RL-03 (no `PARKED` records); §6 renumbering; RL-05 |
| Q-02 | §7.1 line 274 | The PO bullet says the executor runs check 11's recording preflight and records it | RL-05 (line 274 is outside the RL-03 anchor list) |
| Q-03 | §7.1 line 275 | The executor bullet drops the `PARKED` records and adds the recording of check 11 | RL-03; RL-05 |
| Q-04 | §10 line 357 | Check 1 row adds "collection test" | RL-07 |
| Q-05 | §10 line 367 | Check 11 row adds "Q: recording preflight and recording (§12)" | RL-05 |
| Q-06 | §10 line 368; check heading line 825; D-goal line 827 | Close-out check numbered 12, D-goal D11 | §6 renumbering |
| Q-07 | §11 line 421 | Counts note that Q also runs the recording preflight and recording of check 11 | RL-05, inside the RL-03 region |
| Q-08 | Check 1 line 481 | "Final decisive command: step 8's admission command" | RL-07 renumbering |

No other region changed. The unified diff from v1.1 to v1.2 has 116 removed and 103 added lines, and every hunk lies in a region named in §3 or in this table.

## 8. Repository changes since v1.1's observed revision

Between `bf6e8da` and `e1ab8ba`, only the four QA-80 v1.1 files under `docs/ephemeral/` changed (amthorn78/glow-hdengine-v2#540). No file outside `docs/ephemeral/` changed, and `docs/pfcanon/` is identical. The review v1.3, the revocation record v1.0 and the Alpha feedback brief v1.0 are recorded on branch `claude/nice-mayer-tf9l4c` at `b245b0c`, with four other QA-70 records, and are not yet on `main`. Plan v1.2 cites them by path.

## 9. Verification performed at QA-80

- Plan v1.2 mechanical lint: no U+2026, no three consecutive periods, no fenced code block, no `run_id`, no `TBD`, `TODO`, `FIXME` or `???`, no CR byte; ends with `ASK OK?` and one LF.
- Render check with markdown-it-py 4.2.0 (CommonMark plus tables, in the session scratchpad): 16 tables, each with a consistent column count; 11 ordered lists with the intended start numbers; 45 headings.
- Collection: the `check_id` values of the §10 matrix, of the CHECK headings and of the review v1.3 §5 list are the same 12 values in the same order.
- References: no text refers to a `PARKED` check, a removed check or its number. The remaining `PARKED` mentions (lines 63, 65, 78, 313 and 316) name the canon status or its canon definition.
- Register: §2.3 of v1.2 is byte-identical to §2.3 of v1.1.
- Diff scope: every hunk of the v1.1 to v1.2 diff maps to §3 or §7 here.
- Repository facts newly relied on, read-only at `e1ab8ba`: `tools/qa/qa_harness.py` has no command-line entrypoint; `record_check` publishes one primary log and the flat manifest with rollback; the v2 header has fourteen keys, and `timestamp_utc` is the finalization time (Plan Templates "Step-log header schema expectations (required; v2)").
- Not performed: no QA check, no pytest run, no helper smoke validation, no network, vendor or database action.

## 10. CANON_CONFLICT_REGISTER

Carried in Plan v1.2 §2.3, the one register for this change, unchanged: C040-01 to C040-08 as in the QA Audit v1.0 §11, and C040-09 `APPROVED_AS_CHANGED` by the QA-70 review v1.1 §3. The review v1.3 found no new conflict and made no register decision, and QA-80 found none.

## 11. Unresolved items and owners

None from the review v1.3 bundle. Carried items keep their owners:

| Item | Owner |
| --- | --- |
| QA-100 attempts in `06b04a9` (checks 1 to 10 under Plan v1.0) | Kronos at QA-110, after an approved Plan (Plan §7.3) |
| Guide §4.3 and §5 defects (superseded by canon) | Isis, recorded; canon governs |
| Epic rails statement missing from the Implementation Plan v2.1 | Whole-change IA (carried, non-blocking) |
| Glow Infrastructure §2.8 wording (C040-09) | PF07 maintainer, documentation only |
| Deferred live Gate readiness and live Reader success | A future epic that introduces the App user model (Glow QA Guide §3.3); PF09 rows in Plan §14 |
| Prompt-level causes of the earlier approvals | GCFPE-MGMT-10, through the Alpha feedback brief |
| The QA-90 task naming the QA/infra executor and the evidence-storage lane | Product Owner delegation, recorded by Kronos at QA-90 after approval |

## Provenance

GCFPE_PROMPT_USES:

- usage_id: GCFPE-USE-HDE-EPIC040-QA-80-20260928-01 (shared with Plan v1.2)
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - prompt: QA-80 — Revise Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb813ba9a9dbd9a641d36c; page as of 2026-09-24T15:55:48.777Z; release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-80 (second revision, against the QA-70 review v1.3)
  - capture_time: 2026-09-28T00:05:56Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_PLAN v1.2 (`PLAN_PENDING_REVISED`) and this REDLINE_APPLICATION_REPORT v1.1, routed to QA-70 (Isis-52)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `e1ab8ba`)
- Earlier entry: GCFPE-USE-HDE-EPIC040-QA-80-20260927-01 (Plan v1.1 and report v1.0)
