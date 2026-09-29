---
artifact_type: QA_EVIDENCE_REVIEW
artifact_id: HDE-EPIC040-QA110-QA-EVIDENCE-REVIEW
artifact_version: "1.0"
state: ALL_MEMBERS_ACCEPT_RUN_INCOMPLETE
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-110 / QA task collection v1.1 tasks T01 to T10 against QA-100 execution results v1.1
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-110 — Review QA Evidence and Route the Next Action — 091426.1 (Notion 3db4590a05eb816984d1d34da0e08f40; page as of 2026-09-24T15:52:32.947Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (APPROVE by Isis-52; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df)
task_collection: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md (SHA-256 4d498d91382a16df3a73653172fa00d427402a9c12ad85e6d2589d699415f836)
execution_results: docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.1.md (SHA-256 afcb8df263c1e2295caa63e0fb213a3f1c48da8a8dca6ea0470eb1199944e041; supersedes v1.0)
evidence_of_record: branch qa/hde-epic040-qa100-plan-v1.2-run-20260929, commit 345148b7fce2482349828f897abbc0d7d12fe7fa (Run B, section 4)
earlier_execution: branch qa/hde-epic040-qa100-plan-v1.2, commit e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c (Run A, section 4; preserved, non-canonical)
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d (both runs)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919)
observed_revision: 0b1487084562f5700628df97c60246b22ac1a7a3 (origin/main at review; pull request amthorn78/glow-hdengine-v2#546, which carries the QA-100 records, is merged)
routing: QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23), for Plan checks 11 and 12, which are unissued and have no Product Owner selection recorded
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-110 (QA-110 is not an addendum producer)
---

# HDE-EPIC040 — QA Evidence Review v1.0 (QA-110): tasks T01 to T10 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Members reviewed | T01 to T10 (Plan v1.2 checks 1 to 10), matched one to one with the ten `QA_EXECUTION_RESULT` records of the QA-100 results v1.1 §4 |
| Decision per member | 10 × `ACCEPT` (§5) |
| QA-110 per-task result | 10 × `PASS`: the execution layer (step-log `PASS`, every [E] predicate re-verified against the captured output) and the [K] layer (every [K] predicate evaluated here) both pass (Plan §12, two result layers) |
| Attempt lineage | Two stored executions of the same collection exist. Ruling LR-01 (§4): both are preserved; Run B is the evidence of record; Run B's executions of T01, T02 and T04 to T10 are second executions made without the QA-110 decision that attempt 2 requires, recorded as a process deviation; the one ordinary rerun of those checks is consumed |
| Collection defects found | Four in my QA-90 collection v1.1, all syntax-origin or procedural, none affecting a proof target (§6, K-01 to K-04) |
| Escalation | None. No behavior defect, no invalid Plan, no scope, code or Ops remediation |
| Run state | Incomplete. Plan checks 11 `open-rails-showcompat-vendor` and 12 `qa-closeout-deliverables` are unissued, and no Product Owner selection is recorded for them. No already-authored task remains |
| Next stage | QA-90 — Create Bounded QA Execution Task — 091426.1, for checks 11 and 12, on the Product Owner's selection (§8) |
| Not established | Whole-change QA PASS, acceptance, closure, PF09 movement, the QA-120 Report, or any claim for checks 11 and 12 (§12) |

## Canon relied on

Read from `docs/pfcanon/` on `main` at `0b14870`. `docs/pfcanon/` there is identical to `53449c9`, where the collection read it.

- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`, the version read): searched at this invocation for `QA-110`, `duplicate execution`, `second execution`, `execution of record`, `current-state`, `attempt lineage`, `unauthorized rerun` and `per-task result`, with no hit. PF10 sets no rule for evidence review or for two executions of one task collection, so the Glow QA Guide and Plan Templates govern. Relied on as the Plan records them: the addenda of Plan v1.2 §1 and §2.2 (2.5, 2.12, 2.19, 2.20, 2.22 to 2.25, 2.27 for the check anchors) and 2.29 (canon location; change documents in `docs/ephemeral/`).
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`), each read in full at this invocation: §3.1.2 (Kronos reviews evidence and retains per-task results, deviations and retry lineage); §3.4.8 (tracked entrypoints; `/tmp` glue helpers allowed and never evidence); §4.3 (mechanical evidence; no hand editing); §4.4.1 to §4.4.7 (current state is canonical; one manifest and one primary log per check; old run logs are non-canonical; the primary log must let a reviewer reconstruct the run); §10.8 (tested state distinct from the evidence-storage commit; preserve the original result and record later assessment separately; inadequate execution authority remains actionable). Read in full earlier in this session and relied on: §3.4.7, §3.4.9, §3.4.10 (syntax-origin defects, including shell grammar, tokenization and command-wrapper form, are normalizable and never verdict-bearing), §3.5.5, §3.5.6, §9.2.15.5 (preserve actual attempt counts; reconcile an uncertain earlier execution to its native record, or retain the uncertainty and route recovery), §10.6 (a first eligible fault needs Kronos's QA-110 decision before QA-90 attempt 2; a second failure goes to ESC-10), §11.1.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Step-log header schema expectations (required; v2)", including the closed status set, the exact status predicates and the causal precedence.
- **Technical Writing Best Practices** (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`): "Truth and source fidelity" (unknown stays unknown).

## 2. Inputs and matches

| Item | Identity | Match |
| --- | --- | --- |
| Approved base | Plan v1.2, SHA-256 `330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010` | Equal to the pins in the collection and in the QA-100 results |
| Approving review | Review v1.4, APPROVE, 2026-09-28T00:26:24Z | Equal |
| QA Audit | v1.0 | Equal |
| Task collection | v1.1, `TASK_READY`, T01 to T10 at attempt 1 | Executed as issued, with the normalizations its §4.9 lists and executor normalization E-01 (§6, D-01) |
| Selection | Product Owner "Tasks: 1-10" = Plan checks 1 to 10 | Ten tasks, ten results, same order |
| Execution results | QA-100 results v1.1, ten records, all `COMPLETE` | One record per task; the task, check, attempt label and Plan identity in each record match its task |
| Environment | Closed posture on every command; venue per §4 | Matches Plan §5.2 and collection §4.4 in both runs (R3 lines in every task) |
| Tested source | `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d` | The collection observed `53449c9`; `git diff --name-only 53449c9 0db3f0e` lists only the three QA-90 files under `docs/ephemeral/`, so the tested code, tests and evidence are those the collection observed |

## 3. Evidence integrity of the evidence of record (Run B)

- The 19 files on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `345148b7fce2482349828f897abbc0d7d12fe7fa` were read from `origin` and hashed: 19 of 19 equal the digests and sizes of the QA-100 results v1.1 §7 (§7 below repeats them). The commit's diff against the tested source adds exactly these 19 paths, all on the collection §4.7 permitted list.
- Manifest `audit/qa/hde-epic040/qa_step_logs_manifest.json`: valid JSON, an object keyed by `check_id`, 10 unique keys, each entry with `check_id`, the full `log_path` of that check's `primary.log`, and a `status` equal to the header status of that log (Glow QA Guide §4.4.3).
- Primary logs: each is non-empty, LF-terminated, starts with one `pf27.step_log_header.v2` line with the 14 keys, `status` `PASS`, empty `status_reason`, `exit_code` 0 equal to the final decisive command's recorded exit code, `captured_env` the six closed-posture values, empty `intended_tokens` and `claimed_tokens`, `evidence_artifacts` listing its own primary log and the task's supplementary files, and `pf_refs` as the collection directs. Each body has the five sections of Plan §8 (Glow QA Guide §4.4.4 to §4.4.6).
- No path proofs exist yet. They are produced by check 12 (Plan §12, check 12), which is unissued.
- A secret-pattern scan of both runs' evidence files (credential URLs, bearer and vendor key headers, key assignments, private-key blocks) found no hit. Every task in both runs records all nine secret-bearing and drift names as `UNSET` under the closed posture (R3).

## 4. Attempt lineage: two stored executions (ruling LR-01)

### 4.1 Facts, from the stored bytes

| Fact | Run A | Run B |
| --- | --- | --- |
| Branch and commit | `qa/hde-epic040-qa100-plan-v1.2`, `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c`, committed 2026-09-28T01:55:32Z, parent `0db3f0e` | `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, `345148b7fce2482349828f897abbc0d7d12fe7fa`, committed 2026-09-29T02:27:33Z, parent `0db3f0e` |
| Executor, as its T01 log records | "amthorn78 (authorized QA Codespace operator session; GitHub Copilot execution agent)" | Claude Code local VS Code session `fd43ebfd-1614-44e1-8ee5-6d03da21b70a`, QA-100 operator session delegated by the Product Owner |
| Venue and checkout | GitHub Codespace, `/workspaces/hde-epic040-qa`, umask 0022, Python 3.12.14 | Product Owner-controlled Linux shell, `/home/nathan/hde-epic040-qa`, umask 0022, Python 3.12.3 |
| Console environment before any change | `DATABASE_URL`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` SET; unset for every command by the closed prefix | All secret-bearing names UNSET |
| Recorded checks | 8: T01, T02, T04 to T09, all `PASS`, finalized 2026-09-28T01:28:15Z to 01:44:19Z | 10: T01 to T10, all `PASS`, finalized 2026-09-29T01:31:42Z to 02:00:29Z |
| T03 `ac040-08-evidence-validators` | No primary log, no manifest entry, no other file | Recorded `PASS` |
| T10 `sec-reader-http-live` | Executed: `http_probes.jsonl` (22 lines) and `gunicorn_server.log` (server 01:51:04Z to 01:52:02Z, clean shutdown) are stored. No primary log and no manifest entry | Recorded `PASS` |
| Log completeness | Four primary logs (T05, T07, T08, T09) have no OUTPUT section; their test summaries appear elsewhere in the body | Every log has all five sections |
| Own operator repeats | T01 command 22 first ran with a stray backtick and full stop copied from the collection and exited 2, then was repeated; commands 26 and 27 were repeated after a wrong stdout target. Both recorded in its T01 body | T10 commands 11 and 12 repeated after an operator error before the server started (D-02) |
| Returned to QA-110 | No `QA_EXECUTION_RESULT` exists | QA-100 results v1.1 |

Agreement between the runs, checked here: every summary Run A recorded equals Run B's (2,092 collected; 304, 371, 153 and 191 passed; 144 passed and 3 skipped; 339 passed); the doc-delta surfaces and the four golden-comparison files are byte-identical; Run A's 22 probe captures equal Run B's in every field except the `date` header; all 18 [K] evaluations of §5 give the same result on both runs' files.

### 4.2 Ruling LR-01

1. **Both executions stand as records.** Each is an actual execution of collection v1.1 at the same tested source. Neither is deleted, rewritten or reconstructed (Glow QA Guide §9.2.15.5, §10.8).
2. **Execution counts.** T01, T02 and T04 to T10: two executions each, Run A first. T03: one recorded execution (Run B); whether Run A executed T03 is unknown, because it left no trace.
3. **Attempt labels.** Run A's executions are the attempt-1 executions of the tasks it executed (Plan §7.3: attempt 1 is the task's first execution). Run B's executions of T01, T02 and T04 to T10 are second executions made without the QA-110 decision that attempt 2 requires (Plan §7.3; Glow QA Guide §10.6; collection §4.2, §4.8). They are not an authorized attempt 2, and that is recorded as a process deviation with its causes in §6 (D-12, D-13, K-03). If Run A never executed T03, Run B's T03 execution is its attempt 1; this stays unknown.
4. **Evidence of record: Run B, for all ten checks.** Reasons, none of which depends on a result:
   - current state is canonical, and an epic QA root holds one manifest and one primary log per check, with older logs non-canonical (Glow QA Guide §4.4.1, §4.4.3, §4.4.7). Run B is the later execution and the only single stream that holds all ten checks;
   - Run A has no receipt for T03 or T10, and four of its logs do not let a reviewer reconstruct the run from the primary log alone (Glow QA Guide §4.4.6);
   - Run B's results were returned through the QA-100 contract, and Run A's were not.
   The choice changes no outcome: wherever Run A recorded or captured a result, it equals Run B's (§4.1).
5. **Rerun consequence.** For T01, T02 and T04 to T10, the one ordinary rerun of Plan §7.3 is consumed; any later fault in those checks goes to ESC-10 (Plan §7.3; Glow QA Guide §10.6). For T03 it depends on the unknown of item 2; the point is moot while T03 stands accepted.
6. **Storage consequence.** Run A's branch is a preserved, non-canonical execution record. Merging it into `main` would place a second manifest for the same checks at the canonical QA root and must not happen (Glow QA Guide §4.4.3, §4.4.7). Checks 11 and 12 run in the Run B checkout and store on the Run B branch, so that one QA root and one manifest hold all twelve checks (Plan §7.1). Any merge is the Product Owner's.
7. **Unresolved, non-gating.** Why Run A left no T03 trace and no T10 receipt is not recorded anywhere I can read. The probable T10 cause is K-01 (§6), an inference, not established. Owner: the Product Owner, who holds the Run A Codespace. Recovery: a read-only look at that Codespace's scratch root, `/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/` and `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/`, if it still exists. If it shows a non-`PASS` T03 outcome, T03 is reopened for focused review (Glow QA Guide §10.8); otherwise the uncertainty is carried to the QA-120 RCA (Glow QA Guide §9.2.15.5).

## 5. Per-task reviews

Evidence of record for every task: Run B (§4.2 item 4). "[E] re-verified" means Kronos read the captured output in the primary log and compared it with the literal expectation of the task; "[K]" means evaluated here from the named artifacts. Where the task has supplementary files, their SHA-256 values are in §7.

### T01 `d0-discovery` — ACCEPT; per-task result PASS

- Result mapped: QA-100 results v1.1 §4 T01, `COMPLETE`, step-log `PASS`, finalized 2026-09-29T01:31:42Z, 28 recorded commands, final decisive command 24 exit 0.
- [E] re-verified: command 1 exit 1 (QA root absent before any write); commands 6, 7, 8 exit 0; command 9 `Python 3.12.3`; command 10 `harness_ready`, exit 0; command 22 exit 0 and command 23 `2092 tests collected in 3.99s`; commands 13 to 17 exit 0; all 14 flag counts of commands 18 to 21 at least 1; command 24 `AdmittedMechanicsBundle 1.3.0 2026-08-24T18:04:49Z 45 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96 m10-channel-state-v1.0.0`; command 27 printed 1; command 28 correctly not run; no `BLOCKER:` line.
- Count difference: 2,092 against the Audit reference 2,090. Verified here: `git diff a6002d2 0db3f0e -- tests/evidence/test_rails_ci_workflow_integration.py` adds exactly two parametrize cases. Recorded and explained; not a failure (Plan §11).
- [K]: none.

### T02 `step-0b-doc-delta-capture` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:33:05Z, final decisive command 9 (`cmp`) exit 0.
- [E] re-verified: gate exit 0; commands 3 and 4 exit 1 (both surfaces absent); writer exit 0; commands 6 and 7 exit 0; both digests `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2`; `cmp` exit 0.
- [K] K1 PASS: both surfaces LF-terminated, no BOM, no CR, 2,867 bytes each, identical. K2 PASS: DD-01 to DD-12 each exactly once. K3 PASS: `## BLOCKERS` and `## CAVEATS` present. K4 PASS: T01 recorded no `BLOCKER:` line and BLOCKERS reads `none`. Also verified: the twelve rows equal the Plan v1.2 §9.1 rows at the tested source followed by the `Drives decision: No` cell.

### T03 `ac040-08-evidence-validators` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:46:26Z, final decisive command 18 (group G) exit 0.
- [E] re-verified: gate showed `d0-discovery` `PASS`; venue evidence `0022` and `644 docs/evidence/INDEX.sha256`, so the venue rule of Plan check 3 did not apply; the nine validators (commands 9 to 17) exit 0; group G `587 passed in 659.57s`, no failure, error or skip; the governed-graph digest before and after is `29b7d9cbc557bc855d25b55b6cee9a562ef1f01840b788b1dad56ad7a4045150`, `cmp` exit 0.
- [K]: none. Lineage: Run A left no T03 trace (§4.2 item 7).

### T04 `ac040-02-03-catalog-config` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:48:22Z, final decisive command 4 (group A) exit 0, `304 passed in 41.82s`.
- Binding: the digests in the body, `catalog/channels_v1.json` `3a4ea9194121e48cc95848fd34a2903de413260b35bce9800b83f67a8bc3d3e9` and `catalog/magic10_mechanics_v1.json` `fff779980bdd6985dd0640d1b90ddc0e90046675a3b6cb7c17a08b9a70500eaf`, equal the SHA-256 of those files at the tested source.
- [K] K1 PASS: key `channels` with 36 rows; every row has exactly the keys `centers`, `circuit_primary`, `domains`, `flags`, `gates`, `id`, `primary_domain`, `substream`; all 36 `gates` pairs ascending and unique; no null value. K2 PASS: `config_id` `m10-channel-state-v1.0.0`; `schema` `magic10_mechanics_config.v1`; 20 signals with unique `signal_id`; profiles `activation_bp_v1`, `coherence_bp_v1`, `expression_bp_v1`; 10 `category_weights`; `equilibrium_score` uses `twice_min_owner_mass_v1`, `counterweight_ratio` uses `companionship_em_mass_v1`, the other 18 use `weighted_state_sum_v1`.

### T05 `ac040-04-05-admission-identity` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:50:07Z, final decisive command 6 (group B) exit 0, `371 passed in 57.21s`.
- [E] re-verified: command 3 (`--check-manifest-only`) exit 0; command 4 digest `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; command 5, 7 of 7 lines `OK`.
- [K] binding: `audit/ops/hde-epic040/ops01/attestation.json` at the tested source hashes to its `SHA256SUMS` line (`9ffd1929875cd8d7485d13b5bd15a9452e32f2b9e08c033a517df58213986dff`). K1 PASS: `release_id` and `manifest_sha256` both equal the command 4 digest. K2 PASS: `validation_result` `PASS`, `release_admission` `PR06R_B_FINAL_PASS`. Recorded as the Plan requires: `source_commit` `6f53d828a30101bb7cd6638f3695eb82c2b10979`, `validation_result` `PASS`, `release_admission` `PR06R_B_FINAL_PASS`. OPS01 evidence is corroboration, not QA evidence; the attestation was not rebuilt.

### T06 `ac040-06-golden-comparison` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:52:28Z, final decisive command 24 (group C) exit 0, `153 passed in 40.03s`.
- [E] re-verified: match runs exit 0 and byte-identical; mismatch run exit 1 with stderr exactly `GOLDEN_COMPARISON_MISMATCH:2`; command 13 printed 1; the report copy `cmp` exit 0; tree digest before and after equal; `cmp` exit 0.
- [K] K1 PASS: the match report has `ok` true, empty `mismatches`, cases `M10-G001` to `M10-G008` each `match`, `config_id` `m10-channel-state-v1.0.0`, `candidate_release_id` equal to the manifest SHA-256. K2 PASS: the mismatch report has `ok` false; its two rows are both `M10-G001`, `expected.signals[0].q` (actual 0, expected 1) and `transcription.expected`; cases `M10-G002` to `M10-G008` `match`. K3 PASS: a structural comparison of `tmp_goldens_altered.json` with the fixture at the tested source finds exactly one difference, `cases[0].expected.signals[0].q` (case `M10-G001`), 0 to 1.

### T07 `ac040-07-gate-ingress-offline` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:53:21Z, final decisive command 13 (group D) exit 0, `191 passed in 1.22s`.
- [E] re-verified: commands 4, 5, 6 exit 5 with stderr `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`; commands 7 to 9 printed 1; stdout of commands 4 to 6 empty (commands 10 to 12 exit 1).
- [K]: none.

### T08 `ac040-04-09-compat-cli-offline` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:54:22Z, final decisive command 3 (group E) exit 0, `144 passed, 3 skipped in 17.04s`.
- [E] re-verified: the three skip lines, all "showcompat vendor calls require open rails", are copied into PREDICATES with their reasons. Skips contribute no proof and are not vendor coverage; check 11 alone carries vendor-backed behavior (Plan check 8).
- [K]: none.

### T09 `ac040-09-reader-http-in-process` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 01:55:14Z, final decisive command 3 (group F) exit 0, `339 passed in 18.85s`, no skip.
- [K]: none. Proof class: in-process Flask test client with injected rows; this includes the production gating of the dev routes that T10 does not probe.

### T10 `sec-reader-http-live` — ACCEPT; per-task result PASS

- Result mapped: `COMPLETE`, step-log `PASS`, finalized 02:00:29Z, 47 recorded commands, final decisive command 44 exit 0, `22`.
- [E] re-verified: gate showed `d0-discovery` and `ac040-09-reader-http-in-process` `PASS`; port free before start (`000`, exit 7); request-body sizes 93, 8, 96, 99, 93, 0, 32,769 after the D-02 repeat; readiness polls `01:58:23 000` then `01:58:24 200`, exit 0, before any probe; all 22 probe curl exits 0; server ended (command 39 exit 0) and port closed (`000`, exit 7); assembler printed 22; `wc -l` printed 22. The server log shows a clean start and shutdown.
- [K] K1 PASS, all 22: S-01 200 with `release_id` equal to the manifest SHA-256 (its `build_commit` is a static literal, not source identity); S-02 and S-03 503 `ERR_M10_RESOLVER_UNAVAILABLE`; S-04 to S-06 400 `ERR_READER_INVALID_VERSION`; S-07 to S-13 422 `ERR_READER_INVALID_INPUT` (S-12 and S-13 each with a 32,769-byte request body whose digest is the corrected file's); S-14 to S-21 405 with `Allow: POST` and the body `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` plus LF, and no body for HEAD; S-26 404 HTML (known limitation O-P06a-22, observed, not failed). K2 PASS, 20 of 20: S-02 to S-21 carry `content-type: application/json; charset=utf-8`, `cache-control: no-store` and no `etag`; every body except HEAD's has exactly `code`, `error`, `ok` false and `schema` `v1`, is canonical and ends with one LF. K3 PASS, 22 of 22: no `Traceback`, `File "`, `psycopg`, `postgresql`, `gates` key, or number in a Reader error body.
- Lineage: Run A executed T10 with identical responses and left no receipt (§4.1).

## 6. Deviations and defects

### 6.1 Dispositions of the QA-100 deviations

| ID | Disposition |
| --- | --- |
| D-01 | Confirmed, and it is my defect (K-01). The executor's E-01 (one-space final argument) is a faithful syntax-origin normalization: the output is byte-identical, the proof target and predicates are unchanged, and it is recorded in the T10 header and provenance (Glow QA Guide §3.4.10). Accepted |
| D-02 | Operator-error repeat inside Run B's T10, before the server started, recorded in `argv.txt` (corrected form) and the body (both executions). The erroneous 65,446-byte file was used by no probe: the JSONL digests for S-12 and S-13 are those of the corrected 32,769-byte file. Not an attempt. Accepted |
| D-03 | Verified (T01 above). Accepted |
| D-04 | Verified: the tested source differs from the collection's observed revision only in the three QA-90 files (Glow QA Guide §10.8). Accepted |
| D-05 | The "other venue" the Plan front matter allows; the recorded 644 mode made group G verdictable. Accepted |
| D-06 | Correct reading: the recording invocation is the recording mechanism, not a check command (Plan §12). Accepted; the next collection says so explicitly (K-04) |
| D-07 | An inline shell capture wrapper that records and runs the literal command text is `/tmp`-level glue and a command-wrapper form (Glow QA Guide §3.4.8, §3.4.10); commands are recorded verbatim; no script file. Accepted |
| D-08 | Read-only observations outside the task lists; none is used as evidence here. Accepted |
| D-09 | As the Plan declares (PF07 §10.1 declaration), closed posture, no secret or database, about 33 seconds. Accepted |
| D-10 | The storage lane is named by the QA-90 task or the Product Owner (Plan §7.2); the Product Owner chose the new branch name after §4.7's stop condition. Accepted. The commit holds exactly the 19 permitted files (§3) |
| D-11 | Versions preserved; v1.1 supersedes v1.0 without editing it. Accepted |
| D-12 | Ruled in §4 (LR-01) |
| D-13 | A process miss, shared with my collection design (K-03). Carried to the QA-120 RCA |
| D-14 | One body line ends with a space. Not material; governed bytes are not edited (Glow QA Guide §4.3). Accepted |

### 6.2 Defects found in my QA-90 collection v1.1

| ID | Defect | Class | Effect | Correction |
| --- | --- | --- | --- | --- |
| K-01 | T10 command 11 ends with an empty-string argument (`''`). Its literal cannot be recorded: `tools.qa.qa_harness.CheckResult` rejects an empty argv part (reproduced here). It is the only command in the collection with an empty argument | Syntax-origin (tokenization); normalizable in flight (Glow QA Guide §3.4.10) | Run B normalized it (E-01). Probable cause of Run A's missing T10 receipt (inference) | Any reuse of that command uses a one-space final argument; issued v1.1 is not edited |
| K-02 | Long commands were printed as inline code followed by a full stop, and Run A's operator copied a stray backtick and full stop into command 22 (exit 2, then repeated) | Presentation (Glow QA Guide §3.4.7: avoid markup that breaks copy and paste) | One operator-error repeat in Run A; no evidence effect | Future collections put each command in its own fenced block with nothing after it |
| K-03 | The collection checked for an existing QA root only in the fresh clone (§4.3) and checked `origin` for the evidence branch only at storage time (§4.7). A second operator session therefore executed all ten tasks before the earlier stored execution was found | Procedural gap | Duplicate executions; the rerun allowance of nine checks consumed without a decision (§4.2) | Future collections check `origin` for an existing evidence branch before the first task and stop if one exists |
| K-04 | My QA-90 authoring dry-run validated the recording invocations with synthetic argv lines, not with the task's real command lines, so K-01 was not caught. The collection also left implicit whether the recording invocation belongs in `argv.txt` | Authoring verification gap | K-01 reached execution | Future collections are dry-run by passing every task's real command lines through `CheckResult`, and state that the recording invocation is not a check command |

None of K-01 to K-04 changes a Plan objective, proof target, rails posture, evidence identity or predicate, so none is a substantive Plan defect and none needs a Plan revision or escalation. All four are carried to the QA-120 RCA as lessons.

## 7. Evidence surfaces of the accepted checks (Glow QA Guide §4.4.1)

Common to every row: manifest entry present with `status` `PASS` and the full `log_path`; header `pf27.step_log_header.v2`, `status` `PASS`, `exit_code` 0, `captured_env` `{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"}`, `intended_tokens` `[]`, `claimed_tokens` `[]`; path-proof binding not yet produced (check 12).

| Check | Primary log SHA-256 | `evidence_artifacts` beyond its own log | Supplementary SHA-256 |
| --- | --- | --- | --- |
| `d0-discovery` | `f5b0f82c7974307bc52efac98232947726f534441fe07992ce384321aa7d5c1d` | the manifest | manifest `003878cbe3dc1d6107240e8e315ec0cfdbde5acc89451b9973ceb27f8f05eda8` |
| `step-0b-doc-delta-capture` | `a64483b5460b75fbc4ce7028f238ff9e72a3f62c617c8e3361ab3d3c163d2c4b` | both doc-delta surfaces | both `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2` |
| `ac040-08-evidence-validators` | `170171e1bbdb61b45c5650207425eabb63fea83597a2d0088023096ef1f11aed` | none | none |
| `ac040-02-03-catalog-config` | `6e622d117b9cbb9dc96845e61b34572c9d667bf62ed9d900a9cbebfaef65b5f6` | none | none |
| `ac040-04-05-admission-identity` | `ffa2a4629db34c415554f32ed88365641471f2995ac440c5b688b8b7262a45cc` | none | none |
| `ac040-06-golden-comparison` | `0b8cda3488141932d45205c9285620ac1545b78c93a6a5a322f218890a6c2e73` | the four comparison files | match runs `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8`; altered input `b8624a02bcc1f24aa689389fc976a5e4939f34a91e080748367e1d155824322f`; mismatch report `54d567373300a7d4a86ca44cb31a61db62d8c39493efc85d06496d2d17ae0026` |
| `ac040-07-gate-ingress-offline` | `fea547063e4b5f2476736e0b0e1f9f35bb6b2a1ad51cab97de4db6c4e3b2758e` | none | none |
| `ac040-04-09-compat-cli-offline` | `2c69c50a0520ab0f5b2a5e7d7ed94fa745ff10120bade979f127fec6a682ac87` | none | none |
| `ac040-09-reader-http-in-process` | `6e53c15e3e0b496c62457887ccc39b9629c1305dfcd830bc9b6964e315452854` | none | none |
| `sec-reader-http-live` | `97e37e38b75d793bef7b57d47bb024070bc7366df718edb1303d0c378022d960` | probes and server log | `http_probes.jsonl` `0c09bf7fdcb265acabc0e125621d69582365f5190728f4613f9375db04e3a008`; `gunicorn_server.log` `1af474e20796fd4be6fe58cf890802b8fd8897805ca07d80f12345ee0708c5db` |

## 8. Run state and routing

- Every member is `ACCEPT`, but the approved run is not complete: Plan v1.2 has twelve checks and checks 11 and 12 have no task. No already-authored task remains, so there is nothing to reuse through QA-100, and the run cannot go to QA-120 yet.
- The lawful branch for unissued steps is QA-90, and QA-90 converts only Product Owner-selected steps. No selection is recorded for checks 11 and 12, as none was recorded for checks 1 to 10 when the QA-70 handoff first routed to QA-90 (`docs/ephemeral/HDE-EPIC040-QA70-handoff-to-qa90-v1.1.md`). The Product Owner supplies the selection when invoking QA-90.
- Dependencies of the remaining checks, both satisfied by this review: check 11 needs checks 1 and 8 `PASS`; check 12 needs every other check recorded, so it runs after check 11.
- Constraints QA-90 must apply to those tasks:
  - both run in the Run B checkout and store on the Run B branch (LR-01 item 6);
  - review v1.4 notes N-101 and N-102 (check 11's `/tmp` files and the standard-input secret scan);
  - the lessons K-01 to K-04;
  - check 12's manifest verification counts the ten checks accepted here plus check 11.

## 9. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from Plan v1.2 §2.3 through the collection v1.1 §6. QA-110 adds no entry and changes no field: this review found no new conflict (PF10 is silent on the topics reviewed, and the Glow QA Guide governs them). PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 keeps for 2.2 to 2.28. A proposal here is not approval.

| ID | Classification | Sources and clauses | Decision and status | Reviewer, artifact, time | Interim treatment | Drainage target and owner | Full history |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION | Pinned source/scope predicate | APPROVED exactly as proposed | Thoth-17, Specification v1.0 (represented by approved v1.1), 2026-09-08T13:23:24Z | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 v13.3.9 §2.2, §2.4 |
| C040-02 | CANON_RECONCILIATION | PF12 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-03 | CANON_RECONCILIATION | PF14 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-04 | CANON_RECONCILIATION | PF19 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-05 | CANON_RECONCILIATION | PF14 §6.7 superseded precomputed-score test instructions | APPROVED, alternative A | Isis-49, Plan v1.0 review, 2026-09-09T03:57:16Z | PF10 §2.3 governs | PF14 §6.7; PF14 maintainer; pending, non-gating | Plan v2.1 §11.2; PF10 §2.3 |
| C040-06 | NEW_CANON | 36-row Channel taxonomy and 16-case existing-state conformance | APPROVED, alternative A | Isis-50, Implementation Plan Review v2.0, 2026-09-09T11:48:08Z | PF10 §2.5 governs | PF12 §2.1, PF01 §§6.1–6.2; their maintainers; pending | Plan v2.1 §11.3; `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`; PF10 §2.5 |
| C040-07 | NEW_CANON | Full Magic-10 exposure via Reader v2 versus Specification line 265 and PF01, PF04, PF05, PF12 statements | PO decision 2026-09-26; delivered by PR06a | Product Owner; PF10 §2.23 | PF10 §2.23 governs; QA tests `?v=2` | PF01, PF04, PF05, PF12, with PF14 and PF29 consequences; their maintainers; pending | PF10 §2.23, §2.24 |
| C040-08 | CANON_RECONCILIATION | Reader v1 error envelope versus schema | Alternative A; delivered by PR06b | PF10 §2.25 decision record | PF10 §2.25 governs; QA asserts the four-key envelope | PF01 §2.3, PF04 §8.1.2; their maintainers; pending | PF10 §2.25, §2.26 |
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks"; QA-only harness scaffolding permitted) | `APPROVED_AS_CHANGED`. Proposed: alternative (a), PF19 and PF27 govern the execution rail and plan shape; alternative (b), forbid all git reads and embedded helpers, which loses the tested-source attribution PF19 §10.8 requires, was not adopted. Change: the approval covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; it does not cover newly written decisive evaluators, which Glow QA Guide §3.4.8 governs. Rationale: Glow Infrastructure §2.1 is names-only ("No procedures or policy here") and §2.8 routes the Live QA execution rail to the Glow QA Guide, so Glow QA Guide §3.4.9 (read-only repository observation for attribution, never a PASS predicate) and Plan Templates govern | Isis, continuing QA Plan reviewer (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq); reviewed QA Plan v1.0 and QA Audit v1.0; decision in `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md` §3, "Decisions carried to this review"; 2026-09-27 | Applied in this Plan: read-only git observations for attribution only, never a PASS gate; no script file is created; tracked harness APIs through `python -c`; no decisive evaluator written at run time (§12). Unresolved risk: a reader who applies PF07 §2.8 literally until its wording is drained | PF07 §2.8 wording; PF07 maintainer; documentation drainage only | Original proposal: QA Audit v1.0 §11 (`PROPOSED`, 2026-09-27). QA-70 review v1.0 §4: APPROVED as proposed; that review was rejected by the Product Owner on 2026-09-27 and is history only (RCA v1.1, C2). QA-70 review v1.1 §3: `APPROVED_AS_CHANGED` (current) |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013).

## 10. Unresolved items and owners

| Item | Owner | Status |
| --- | --- | --- |
| Selection of Plan checks 11 and 12 | Product Owner, at the QA-90 invocation | Open; the run cannot complete without it |
| Run A's T03 outcome and why its T10 went unrecorded (LR-01 item 7) | Product Owner (holds the Run A Codespace) | Open, non-gating; reopens T03 only if a non-`PASS` outcome is found |
| Run A branch `qa/hde-epic040-qa100-plan-v1.2`: preserved, non-canonical, never merged into `main` as the QA root | Product Owner (merge authority) | Standing |
| Run B branch: the one evidence stream to which checks 11 and 12 append; any pull request and merge | Product Owner | Open |
| Lessons K-01 to K-04, D-13 and the duplicate-execution deviation | Kronos-23, in the QA-120 RCA; K-01 to K-04 also applied at QA-90 | Carried |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING: no such procedure at `0b14870` |

## 11. Working state

| Field | Value |
| --- | --- |
| Stage | QA-110 complete for T01 to T10 |
| Review | This file, v1.0 |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-QA110-checkpoint-v1.0.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA110-handoff-to-qa90-v1.0.md` |
| Resume point | QA-90 for Plan checks 11 and 12, on the Product Owner's selection |

## 12. Nonclaims

An `ACCEPT` here covers one bounded check each and is not whole-change QA PASS. This review establishes no acceptance, closure, PF09 status movement, PF-Canon drainage, PF10 addendum, deployment, release activation, token satisfaction, Index or Mirror publication, or ledger-bound manifest. It makes no claim for check 11 (vendor-backed behavior) or check 12 (close-out deliverables), which are unissued and NOT RUN, or for the deferred live Gate readiness and live DB Reader success requirements (Plan §2). QA-110 executed no task, changed no approved artifact and repaired nothing.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-110-20260929-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: K040-REQ-003 to K040-REQ-013 as mapped by Plan v1.2 checks 1 to 10
  - prompt: QA-110 — Review QA Evidence and Route the Next Action — 091426.1; Notion 3db4590a05eb816984d1d34da0e08f40; page as of 2026-09-24T15:52:32.947Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-110
  - capture_time: 2026-09-29T02:58:28Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_EVIDENCE_REVIEW v1.0; T01 to T10 each ACCEPT with per-task result PASS; lineage ruling LR-01; run incomplete; routed to QA-90 for checks 11 and 12
  - task_and_attempt_mapping: T01 to T10 of the collection v1.1, each mapped to its QA-100 results v1.1 record; executions per LR-01 (Run A first for T01, T02 and T04 to T10; Run B the evidence of record for all ten)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `0b14870`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (QA-100 execution results v1.1); GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (QA task collection v1.1).
