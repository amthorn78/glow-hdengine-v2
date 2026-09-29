---
artifact_type: QA_EXECUTION_RESULTS
artifact_id: HDE-EPIC040-QA100-QA-EXECUTION-RESULTS
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.0.md (QA_EXECUTION_RESULTS v1.0, committed and pushed on the pull request; preserved unchanged; SHA-256 c5425f8ad888a98f05f8cd54c9e44df02ae0ea2d2827974b0a907001bd5964b0). Superseded by this version because, after v1.0, the Product Owner clarified that the evidence files are to be stored in the repository and an earlier stored execution of the same collection was found at the storage step; that made the storage and attempt statements of v1.0 (sections 1, 5 and 8) incomplete
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
stage: QA-100 — Execute Bounded QA Task — 091426.1
state: RESULTS_RETURNED_TO_QA110
author: QA-100 QA/infra executor, Claude Code (model claude-sonnet-5-5), delegated by the Product Owner; not Kronos, not the Product Owner
session_disposition: not a continuing session; the operator session the Product Owner opened for this collection (the handoff supplies no disposition value)
role_session_ref: Claude Code local VS Code session fd43ebfd-1614-44e1-8ee5-6d03da21b70a (id taken from the session scratchpad path; no claude.ai session URL is available to this session)
invocation_binding: EPIC / HDE-EPIC040 / QA-100 / QA_PLAN v1.2 checks 1 to 10 (tasks T01 to T10, attempt 1)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-100 — Execute Bounded QA Task — 091426.1 (Notion 3db4590a05eb811a8d13c0bbbf77a848; page as of 2026-09-24T15:52:02.330Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
task_collection: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md (QA_TASK_COLLECTION v1.1, TASK_READY; SHA-256 4d498d91382a16df3a73653172fa00d427402a9c12ad85e6d2589d699415f836)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010, verified equal to the collection's pin)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025, verified equal to the collection's pin)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df, verified equal to the collection's pin)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919, verified equal to the collection's pin; see "Canon relied on" for what was and was not read)
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d (origin/main at clone time; identical to the local main HEAD)
evidence_branch: qa/hde-epic040-qa100-plan-v1.2-run-20260929 (commit 345148b7fce2482349828f897abbc0d7d12fe7fa on parent 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d; pushed; exactly the 19 files of section 7; no pull request)
earlier_stored_execution: branch qa/hde-epic040-qa100-plan-v1.2, commit e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c (authored 2026-09-28T01:55:32Z by a Codespace operator session; 8 of 10 checks; not touched by this session; see section 5, D-12)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/546 (open, not merged)
routing: QA-110 — Review QA Evidence and Route the Next Action — 091426.1, in the continuing Kronos-23 session
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-100 (QA-100 is not an addendum producer)
---

# HDE-EPIC040 — QA-100 execution results v1.1: tasks T01 to T10 (QA Plan v1.2 checks 1 to 10), as labeled attempt 1

## 1. Result

| Field | Value |
| --- | --- |
| Collection executed | T01 to T10 of `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md`, in order, each labeled attempt 1 by the collection. No task was skipped or narrowed; within this session nothing was repeated except commands 11 and 12 of T10 (§5 D-02). This session did not know, while executing, that an earlier stored execution of the same collection existed (§5 D-12, D-13) |
| Result states | 10 × `COMPLETE` (§3). No state is an acceptance or a QA PASS |
| Step-log status recorded | `PASS` for all ten checks, with an empty reason. This attests the execution layer only (Plan §12 two result layers) |
| [K] predicates | Not evaluated by QA-100. Pending QA-110 for T02, T04, T05, T06 and T10; none exist for T01, T03, T07, T08, T09 |
| Not selected, not run | Plan checks 11 `open-rails-showcompat-vendor` and 12 `qa-closeout-deliverables` (collection §3): NOT RUN |
| Deviations | In T10 command 11, a collection defect with an executor normalization (E-01) and one operator error (§5, D-01 and D-02); a stored earlier execution of the same collection (D-12) and my missed check for it before executing (D-13). Whether this execution is attempt 1, a rerun or corroboration is for QA-110 |
| Evidence storage (collection §4.7) | PERFORMED after the Product Owner's clarification. Branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, one commit `345148b7fce2482349828f897abbc0d7d12fe7fa` on the tested source, exactly the 19 files of §7, pushed to origin and verified with `git ls-remote` and by comparing every remote blob with its recorded SHA-256 (19 of 19 equal). No pull request, no force-push, no merge. Collection §4.7 names `qa/hde-epic040-qa100-plan-v1.2`, but that branch already existed, so §4.7's stop condition applied and the Product Owner chose this new branch. The earlier branch was not touched (§5 D-10) |
| Earlier stored execution | Found at the storage step: branch `qa/hde-epic040-qa100-plan-v1.2` at `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c`, one commit authored 2026-09-28T01:55:32Z, executor recorded as "amthorn78 (authorized QA Codespace operator session; GitHub Copilot execution agent)", same tested source. It holds primary logs for 8 of the 10 checks (all `PASS`; T03 and T10 have none, though T10's two supplementary files are present) and agrees with this session on every check that has a summary line. Attempt lineage is for QA-110 (§5 D-12) |
| This record | Version 1.1, superseding v1.0. Submitted for merge as pull request #546 (https://github.com/amthorn78/glow-hdengine-v2/pull/546) from branch `docs/20260929-hde-epic040-qa100-results`, on the Product Owner's instruction "you may create a PR now and update the handoff". v1.0 stays on that pull request unchanged (§5 D-11). Not merged; merging preserves the record and approves nothing (D21-C) |
| Next stage | QA-110 — Review QA Evidence and Route the Next Action — 091426.1 (Kronos-23) |

## 2. Identity, venue and environment

| Field | Value |
| --- | --- |
| Executor identity | Claude Code (model claude-sonnet-5-5), local VS Code session `fd43ebfd-1614-44e1-8ee5-6d03da21b70a`, acting for the Product Owner (Nathan) as the QA/infra executor of Plan v1.2 (collection §4.1). No claude.ai session URL exists for it. T01 recorded this identity as the first CONTEXT line of every primary log |
| Venue | The "other venue" of Plan front matter: a Product Owner-controlled Linux shell, host Linux 6.8.0-142-generic. Not a GitHub Codespace. Python 3.12.3; 1 CPU, about 3.9 GB memory |
| QA checkout | `/home/nathan/hde-epic040-qa`, a fresh clone of `main` made with `sh -c 'umask 022 && git clone …'` (collection §4.3 item 2). Recorded `umask` 0022; `docs/evidence/INDEX.sha256` mode `644` |
| Tested source | `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`, branch `main`, clean at clone time. The collection observed `53449c96a42a6fdbc61ab272ff248394b58df62c`; `git log 53449c96..0db3f0ef` is one commit (#544, the QA-90 collection itself) and `git diff --name-only` between them lists no file outside `docs/ephemeral/` (read-only observation for attribution only, Plan §5.3). A later commit is recorded, not refused |
| Virtual environment | `/tmp/hde-epic040-qa-v1.2/venv` (Python 3.12.3; Flask 2.3.3, gunicorn 21.2.0, pytest 8.4.2, jsonschema 4.23.0, psycopg 3.2.13, editable `glow-hdengine`), first on `PATH` through the CLOSED and PYTEST prefixes (N-01, N-02) |
| Rails | Closed posture on every command: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`; `DATABASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` unset per command with `env -u` (readiness R3 recorded nine `UNSET` lines in every task). Environment presence before any change (T01 command 2): all secret-bearing and drift names UNSET; pins UNSET except `LANG=C.UTF-8`. No secret value, database, vendor call or network I/O by the product was involved. The only network use was the dependency install (PyPI) and the clone and fetch of the repository (GitHub) |
| Delegation | Product Owner's selection "Tasks: 1-10" and the Product Owner opening this session with the QA-100 handoff (collection §4.1). Nothing beyond it was assumed |

## 3. Task-to-result map

`Final cmd` is the final decisive command and its exit code (its `final.rc`). All finalization times are 2026-09-29 UTC from each primary-log header. The Attempt column is the label the collection gives every task; the lineage question raised by D-12 is open.

| Task | `check_id` | Attempt | State | Step-log status | Final cmd | Finalized | Primary log | [K] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | `d0-discovery` | 1 | COMPLETE | PASS | 24 → 0 | 01:31:42Z | `audit/qa/hde-epic040/checks/d0-discovery/primary.log` | none |
| T02 | `step-0b-doc-delta-capture` | 1 | COMPLETE | PASS | 9 → 0 | 01:33:05Z | `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log` | 4, pending |
| T03 | `ac040-08-evidence-validators` | 1 | COMPLETE | PASS | 18 → 0 | 01:46:26Z | `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` | none |
| T04 | `ac040-02-03-catalog-config` | 1 | COMPLETE | PASS | 4 → 0 | 01:48:22Z | `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log` | 2, pending |
| T05 | `ac040-04-05-admission-identity` | 1 | COMPLETE | PASS | 6 → 0 | 01:50:07Z | `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log` | 2, pending |
| T06 | `ac040-06-golden-comparison` | 1 | COMPLETE | PASS | 24 → 0 | 01:52:28Z | `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log` | 3, pending |
| T07 | `ac040-07-gate-ingress-offline` | 1 | COMPLETE | PASS | 13 → 0 | 01:53:21Z | `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log` | none |
| T08 | `ac040-04-09-compat-cli-offline` | 1 | COMPLETE | PASS | 3 → 0 | 01:54:22Z | `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log` | none |
| T09 | `ac040-09-reader-http-in-process` | 1 | COMPLETE | PASS | 3 → 0 | 01:55:14Z | `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log` | none |
| T10 | `sec-reader-http-live` | 1 | COMPLETE | PASS | 44 → 0 | 02:00:29Z | `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log` | 3, pending |

The manifest `audit/qa/hde-epic040/qa_step_logs_manifest.json` lists these ten `check_id` values, each `PASS`. Every header is `pf27.step_log_header.v2` with `status_reason` empty, `claimed_tokens` and `intended_tokens` empty, and `captured_env` the six admitted values. Header `command` entry counts (one argv per line of `argv.txt`): T01 28, T02 11, T03 25, T04 6, T05 8, T06 26, T07 15, T08 6, T09 5, T10 47.

## 4. QA_EXECUTION_RESULT records

Common to every record: change HDE-EPIC040 (Epic); Plan `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`; review v1.4; QA Audit v1.0; environment per §2; attempt 1 as labeled by the collection (lineage note in §5 D-12); tokens `[]`; residual state and resume point per §6; nonclaims per §10. Digests and sizes of every file are in §7. "Normalizations" are the IDs of collection §4.9 recorded in the task's `provenance.txt`. `[E]` lines give observed values only.

### T01 `d0-discovery` — COMPLETE, step-log `PASS`

- Final decisive command: 24 (admission), exit 0. No `BLOCKER:` line. Command 28 (conditional) was not executed: command 24 exited 0 and command 27 printed 1.
- Normalizations: N-01, N-02, N-03, N-04, N-06, N-08, N-09, N-18, N-19.
- [E] observed: command 1 exit 1 (QA root absent before any write); commands 6, 7, 8 exit 0; command 9 `Python 3.12.3`; command 10 `harness_ready`; command 22 exit 0 with 70 files and **2,092 tests collected in 3.99 s** (QA Audit §4.4 reference 2,090; difference +2, explained in §5 D-03); commands 13 to 17 exit 0; flag counts from commands 18 to 21 all at least 1 (`--source` and the seven other `showcompat` flags 2 each; `--compare-goldens` 4, `--goldens` 2, `--report` 2; `--user-id` 2, `--selection-file` 2; `--check-manifest-only` 2); command 24 printed `AdmittedMechanicsBundle 1.3.0 2026-08-24T18:04:49Z 45 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96 m10-channel-state-v1.0.0`; command 27 printed 1 (`release_id` equals the `catalog/manifest.json` SHA-256); command 29 exit 1 (no planned path is ignored).
- [K]: none.

### T02 `step-0b-doc-delta-capture` — COMPLETE, step-log `PASS`

- Final decisive command: 9 (`cmp` of the two surfaces), exit 0.
- Supplementary files: `audit/docdeltas/hde-epic040_doc_deltas.md` and `audit/qa/hde-epic040/00_meta/doc_deltas.md`, byte-identical, SHA-256 `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2`, 2,867 bytes each.
- Normalizations: N-01, N-02, N-03, N-04, N-06, N-17.
- [E] observed: gate `test -s` on the T01 primary log exit 0; commands 3 and 4 exit 1 (both surfaces absent); writer (command 5) exit 0; commands 6 and 7 exit 0; command 9 exit 0. The writer is QA-created evidence assembly under Plan §12 and evaluates no predicate.
- [K] pending QA-110: LF-terminated and without BOM; each of DD-01 to DD-12 exactly once; both sections present; every T01 `BLOCKER:` line under BLOCKERS (T01 recorded none).

### T03 `ac040-08-evidence-validators` — COMPLETE, step-log `PASS`

- Final decisive command: 18 (pytest group G, 12 files), exit 0. Commands 19 to 23 ran after it and are non-gating.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06, N-07, N-10.
- Venue evidence (required before the validators): `umask` 0022 (command 3); `stat -c '%a %n' docs/evidence/INDEX.sha256` → `644 docs/evidence/INDEX.sha256` (command 4). The venue rule of Plan check 3 did not apply.
- [E] observed: dependency gate `d0-discovery` `PASS`; commands 9 to 17 (the nine validators) each exit 0; command 18: **587 passed in 659.57 s (0:10:59)**, no failure, error or skip.
- Supplementary, non-gating: digest of the sorted path and SHA-256 list of `docs/evidence`, `artifacts` and `audit/gates` (1,098 files) before command 9 and after command 18: both `29b7d9cbc557bc855d25b55b6cee9a562ef1f01840b788b1dad56ad7a4045150`; `cmp` exit 0. Nothing to report.
- [K]: none.

### T04 `ac040-02-03-catalog-config` — COMPLETE, step-log `PASS`

- Final decisive command: 4 (pytest group A, 12 files), exit 0.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06.
- [E] observed: gate `d0-discovery` `PASS`; command 3 digests `catalog/channels_v1.json` `3a4ea9194121e48cc95848fd34a2903de413260b35bce9800b83f67a8bc3d3e9` and `catalog/magic10_mechanics_v1.json` `fff779980bdd6985dd0640d1b90ddc0e90046675a3b6cb7c17a08b9a70500eaf`; command 4: **304 passed in 41.82 s**, no failure, error or skip.
- [K] pending QA-110: the structural predicates of Plan check 4 on the two catalog files whose SHA-256 equals the digests above (K1 channels; K2 mechanics). PF10 Addendum 2.5 is cited in the body.

### T05 `ac040-04-05-admission-identity` — COMPLETE, step-log `PASS`

- Final decisive command: 6 (pytest group B, 9 files), exit 0.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06.
- [E] observed: gate `d0-discovery` `PASS`; command 3 (`release_id_recompute.py --check-manifest-only`, the only mode used) exit 0, no output; command 4 digest `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; command 5 (OPS01 ledger, read-only) exit 0, 7 of 7 lines `OK`; command 6: **371 passed in 57.21 s**, no failure, error or skip.
- [K] pending QA-110: `audit/ops/hde-epic040/ops01/attestation.json` fields `release_id` and `manifest_sha256` equal the command 4 digest; `validation_result` `PASS`; `release_admission` `PR06R_B_FINAL_PASS`; record `source_commit`, `validation_result` and `release_admission`. QA-100 did not read `attestation.json` and did not rebuild it. PF10 Addenda 2.12, 2.22 and 2.27 are cited in the body.

### T06 `ac040-06-golden-comparison` — COMPLETE, step-log `PASS`

- Final decisive command: 24 (pytest group C, 1 file), exit 0.
- Supplementary files (QA-created, in `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/`): `compare_match_run1.json` and `compare_match_run2.json` (byte-identical, SHA-256 `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8`, 1,051 bytes each); `tmp_goldens_altered.json` (SHA-256 `b8624a02bcc1f24aa689389fc976a5e4939f34a91e080748367e1d155824322f`, 26,030 bytes); `compare_mismatch_report.json` (SHA-256 `54d567373300a7d4a86ca44cb31a61db62d8c39493efc85d06496d2d17ae0026`, 1,382 bytes, byte-identical to the comparator's report at the scratch path).
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06, N-10, N-11.
- [E] observed: gate `PASS`; commands 8 and 9 (match runs) exit 0; command 22 (`cmp` of the two reports) exit 0; command 10 (input writer) exit 0 and printed `M10-G001 expected.signals[0] rapport_delta q 0 to 1`; command 12 (mismatch run) exit 1 with stderr `GOLDEN_COMPARISON_MISMATCH:2`; command 13 printed 1; command 15 (`cmp` of report copy) exit 0; tree digest before command 8 (commands 3 to 6) and after command 16, before any test ran (commands 17 to 20), both `0e9a98a597b85902da0b1ca251813ad0b3d2190fdd08dbaae4330365a711246b` over 7,299 files (excluding `.git`, `audit/qa/hde-epic040`, `__pycache__`, `.pytest_cache`); command 21 (`cmp`) exit 0; command 24: **153 passed in 40.03 s**, no failure, error or skip. Fixture `tests/fixtures/magic10/v1/goldens.json` SHA-256 `9f99c6aa633cf4713c3de9d37a1d70157fe632e08740ec1c505ecc202486ace5`. `generate_config_artifacts.py` ran only with `--compare-goldens`.
- [K] pending QA-110: K1 match reports; K2 mismatch report; K3 the altered file differs from the fixture only in case `M10-G001` `expected.signals[0].q` (0 → 1). QA-100 displayed the first 300 bytes of `compare_match_run1.json` once while checking that it was written (§5 D-08); it made no evaluation. PF01 §9.5 and PF10 Addendum 2.20 are cited in the body.

### T07 `ac040-07-gate-ingress-offline` — COMPLETE, step-log `PASS`

- Final decisive command: 13 (pytest group D, 4 files), exit 0.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06, N-12.
- [E] observed: gate `PASS`; commands 4, 5, 6 exit 5 with stderr `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE` respectively; commands 7, 8, 9 (`grep -c -x -F`) printed 1, 1, 1; commands 10, 11, 12 (`test -s` on the stdout captures) exit 1, 1, 1 (empty stdout, no report); command 13: **191 passed in 1.22 s**, no failure, error or skip. The open-rails refusal was not re-run (Plan check 7).
- [K]: none.

### T08 `ac040-04-09-compat-cli-offline` — COMPLETE, step-log `PASS`

- Final decisive command: 3 (pytest group E, 17 files), exit 0.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06.
- [E] observed: gate `PASS`; command 3: **144 passed, 3 skipped in 17.04 s**; command 4 (`grep -F SKIPPED`) exit 0, three lines, each recorded in the body's PREDICATES section with its reason (Plan RL-12): `tests/cli/test_showcompat_parity_and_identity.py` lines 108, 128 and 150, "showcompat vendor calls require open rails". Skips contribute no proof and are not vendor coverage (Glow QA Guide §2.3); check 11 alone carries vendor-backed behavior and is NOT RUN.
- [K]: none.

### T09 `ac040-09-reader-http-in-process` — COMPLETE, step-log `PASS`

- Final decisive command: 3 (pytest group F, 15 files), exit 0.
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06.
- [E] observed: gate `PASS`; command 3: **339 passed in 18.85 s**, no failure, error or skip. Proof class: in-process Flask test client with injected rows; not live transport and not a live database. PF05 §5 as overridden by PF10 Addenda 2.23 and 2.25 is cited in the body.
- [K]: none.

### T10 `sec-reader-http-live` — COMPLETE, step-log `PASS` (FAIL_BEHAVIOR is decided only at QA-110 from the [K] predicates)

- Final decisive command: 44 (`wc -l` of `http_probes.jsonl`), exit 0, printed `22`.
- Supplementary files: `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` (SHA-256 `0c09bf7fdcb265acabc0e125621d69582365f5190728f4613f9375db04e3a008`, 11,575 bytes, 22 lines) and `gunicorn_server.log` (SHA-256 `1af474e20796fd4be6fe58cf890802b8fd8897805ca07d80f12345ee0708c5db`, 638 bytes, non-empty).
- Normalizations: N-01, N-02, N-03, N-04, N-05, N-06, N-13, N-14, N-15, N-16, plus executor in-flight normalization **E-01** on command 11 (§5 D-01).
- [E] observed: gate (both dependencies `PASS`); command 3 printed `000` with exit 7 (port 8000 free); request bodies as expected after the repeat of commands 11 and 12 (sizes 93, 8, 96, 99, 93, 0, 32,769; §5 D-02); server started as PID 78820 (gunicorn 21.2.0, gthread, 2 workers, `0.0.0.0:8000`, `APP_ENV=dev`, `PORT=8000`); readiness poll `01:58:23 000`, `01:58:24 200`, exit 0, before any probe; commands 16 to 37 (probes S-01 to S-21 and S-26) all ran, every curl exit code 0 and every curl stderr empty; command 38 exit 0; command 39 exit 0 (server ended after `Handling signal: term`, both workers exited, master shut down); command 40 printed `000` with exit 7 (port closed); command 41 exit 0 (log non-empty); command 42 exit 0 and printed `22`; command 44 printed `22`. The server ran about 33 seconds.
- Request bodies for S-12 and S-13 are recorded in `http_probes.jsonl` with `request_body_bytes` 32769 and `request_body_sha256` `45e66f1c25d1fc33ca1a6699013efe201cdc76f5591c394c9d05c7fc7e0191c8` (the corrected `oversize.json`).
- [K] pending QA-110: K1 each probe's expected status and code per the Plan check 10 table (S-01 also `release_id` equals the manifest SHA-256 `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`); K2 header and envelope predicates; K3 leak predicates. QA-100 printed each probe's HTTP status, header-line count and body size once to confirm the captures exist (§5 D-08) and made no comparison with the Plan table.

## 5. Deviations, defects and observations for QA-110

None of these changes an objective, proof target, rails posture, evidence identity or predicate. Each is recorded where it happened.

| ID | Kind | Statement |
| --- | --- | --- |
| D-01 | Collection defect and executor normalization E-01 (T10 command 11) | The collection text of command 11 ends with an empty-string argument to `printf '%s%32676s'`. `tools.qa.qa_harness.CheckResult` rejects an empty argv part (`ValueError: every command argv must contain only non-empty strings`), so a T10 `argv.txt` holding the command as written cannot be recorded. A read-only dry check before T10's first command (tokenizing every T10 command line and constructing a `CheckResult` in memory; nothing written) found this and no other empty part in T10. QA-100 ran command 11 with a one-space argument instead: `printf` pads `%32676s` to the same width, so the output is byte-identical (compared with a one-character first argument before the task: identical, 32,677 bytes each). Recorded in T10's body (DEVIATION E-01) and `provenance.txt`, outside the N-01 to N-19 list because it is executor-originated (Plan §12: the executor records the normalization in `command_provenance`). Kronos decides whether the collection needs correction for any later attempt or task. T01 to T09 contain no empty argv part; all recorded normally |
| D-02 | Operator error (T10 command 11, first execution) | While applying E-01 my driver code did not strip the trailing empty-string argument (parameter expansion `${cmd11% ''}` treated the empty quotes as quoting), so the first execution ran with three `printf` arguments and wrote a 65,446-byte `oversize.json` (SHA-256 `c3ea59e2775bfc36a6445a6d66fc3150cad36455b80a47c40853d70a796e8e4d`); command 12's first execution printed `65446`. The server had not been started and no probe used the file. Per collection §4.8 the commands were repeated (command 11 corrected as `c11b`, command 12 as `c12b`), both executions of command 12 and the corrected command 11 are in T10's `argv.txt` and body, and the erroneous first execution of command 11 is recorded in the body's COMMANDS and CONTEXT sections but is not in `argv.txt`, because its text also ends with an empty-string argument the harness rejects. Its exact text, the erroneous file and its digest are preserved in the scratch directory. This is an operator-error repeat inside attempt 1, not an attempt 2 (collection §4.2, §4.8; Glow QA Guide §9.2.15.5). The corrected file is 32,769 bytes, SHA-256 `45e66f1c25d1fc33ca1a6699013efe201cdc76f5591c394c9d05c7fc7e0191c8`; its first 93 bytes equal `valid.json` and the rest are spaces (operator diagnostics, D-08) |
| D-03 | Test-count difference (T01) | 2,092 collected against the Audit reference 2,090. A read-only `git diff a6002d2 HEAD` of `tests/evidence/test_rails_ci_workflow_integration.py` shows exactly two added parametrize cases (`.claude/settings.json` and `ci/checks/check_agents_md_citations.py`); the `def test_` count of that file is 59 at both commits and no other of the 70 files changed since `a6002d2`. The difference is explained and is not a failure (Plan §11). T01's body records the count and the lineage note; the verification above was made outside the task record |
| D-04 | Tested source | `0db3f0ef…` differs from the collection's observed `53449c96…` by one docs-only commit (§2). The tested state is the clone-time `HEAD`; it is distinct from the later evidence-storage commit `345148b7…` (D-10) and from review-time `HEAD` (Glow QA Guide §3.4.9, §10.8) |
| D-05 | Venue | Executed in the "other venue" (Product Owner-controlled Linux shell), not a Codespace. The recorded checkout mode `644` made group G's file-mode assertion verdictable at attempt 1 |
| D-06 | Recording invocation | The recording invocation (last numbered command of each task) is not listed in `argv.txt`, so it is not in the header `command` list; each body's COMMANDS section states this. Collection §4.6 says `argv.txt` holds "every command executed for the check"; QA-100 read that as the check's own commands because the recording reads `argv.txt` |
| D-07 | Capture mechanics | Each command ran through an inline shell function that appended the literal command text to `argv.txt` and evaluated that same text with stdout, stderr and exit code captured to `c<k>.out`, `c<k>.err`, `c<k>.rc` (N-04). Long command lines (collection lines for the collection test, admission, the Step-0B writer, every pytest group, the input writer, the probes, the JSONL assembler and every recording invocation) were taken mechanically from the collection file with `sed`, not retyped. Readiness R1 to R3 in T02 to T10 reuse T01's exact command text. T06 command 9 ("the same command") was typed with the CLOSED prefix. Long pytest runs (T03 to T09) ran as detached or harness-background jobs with the same captures; T10's server was started with the collection command and detached with `disown`. No script file was created (C040-09 interim treatment) |
| D-08 | Operator observations outside the task command lists | Read-only, none changed a status: before setup, tool and PyPI reachability probes, disk and memory, `git fetch origin main`; the D-03 git history check; in T02, `wc`, `grep -c`, `od` and a CR count on the written surface (12 `DD-` rows, no BOM, no CR seen; not a [K] evaluation); in T06, the first 300 bytes of `compare_match_run1.json`; before T10, the in-memory harness and tokenization dry checks (D-01) and a `ps`/`ss`/`pgrep` check after the server stopped (no gunicorn process, no listener on 8000); a per-probe rc/status/size listing in T10 (D-01); `git status` snapshots of the QA checkout (taken after T01, after T02, after T03's group G and after T10; no tracked file was modified in any of them, and none was taken after T04 to T09 individually); a read of only the `request_body_bytes` and `request_body_sha256` fields of probes S-12 and S-13 in `http_probes.jsonl` to verify a statement in this record (32769 and the corrected body's digest in both); and before any storage decision, a secret-pattern scan over the 19 evidence files (credential URLs, bearer tokens, key material, set values of `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`) with no hit; and, in the storage steps, read-only checks of the two evidence branch names on origin, `sha256sum -c` of the 19 files before staging, a comparison of the staged list with the collection's permitted list, a fetch into a second clone to compare the remote blobs with the recorded digests, and a read-only comparison with the earlier branch (its manifest, log headers, pytest summary lines and byte-identical files) |
| D-09 | Server exposure | The Plan's PF07 declaration binds gunicorn to `0.0.0.0:8000`. The server therefore listened on all interfaces for about 33 seconds, with no database, no vendor keys and `APP_ENV=dev`. Followed as written |
| D-10 | Evidence storage: decision sequence and stop condition | Collection §4.7 names an evidence branch `qa/hde-epic040-qa100-plan-v1.2`. Its files lie under `audit/`, outside the repository paths this operator may write without the Product Owner's explicit instruction for that change (the workspace write boundary opens only `docs/ephemeral/`, `docs/graph/` and `docs/prompt_ecosystem_management/`; Glow QA Guide §3.4.9 and §10.8 likewise keep publication a separately authorized lane). Sequence in this conversation: (1) I asked whether to push and the Product Owner answered "No, keep evidence local" (v1.0 recorded storage as not performed); (2) the Product Owner then said "No I do want the evidence files in the repo. That is a misunderstanding."; (3) the first check of the storage lane found that `qa/hde-epic040-qa100-plan-v1.2` already existed on origin (D-12), and §4.7 says to stop and report if it does, so nothing was pushed; (4) the Product Owner chose to push to a new branch, `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, with no pull request and the earlier branch untouched; (5) steps 1 to 7 of §4.7 then ran with that name: the status capture and its comparison with the permitted list, `git switch -c` at the tested source, `git add --` of the 19 named paths, the staged list equal to the permitted list, a commit whose subject is the §4.7 message with the tested-source SHA (its body states that it is a second stored execution and does not replace the earlier branch), a push, and `git ls-remote` printing the local head `345148b7fce2482349828f897abbc0d7d12fe7fa`. The branch name is the only departure from §4.7 and was the Product Owner's choice |
| D-11 | Record storage sequence and this version | These records were first written as local files ("Write local files only"), then the Product Owner instructed "you may create a PR now and update the handoff". No version had been committed or given to another reader, so the three files were edited in place before their first commit, and v1.0 of each was committed to pull request #546 (results and checkpoint first, the handoff after the pull request number existed). After that, the evidence storage (D-10) and the earlier stored execution (D-12) made v1.0's statements that storage was not performed and that every task was attempt 1 with no rerun incomplete. Because a committed version is never edited, v1.0 is preserved unchanged and this v1.1 (with a v1.1 checkpoint and handoff) supersedes it on the same pull request |
| D-12 | Earlier stored execution of the same collection | Branch `qa/hde-epic040-qa100-plan-v1.2` on origin at commit `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c` (parent `0db3f0ef…`, the same tested source), one commit authored 2026-09-28T01:55:32Z, 45 minutes after `0db3f0ef` (2026-09-28T01:10:02Z). Its subject is the §4.7 message. Facts read from it (read-only): the T01 log names the executor as "amthorn78 (authorized QA Codespace operator session; GitHub Copilot execution agent)" in a GitHub Codespace, checkout `/workspaces/hde-epic040-qa`, `umask` 0022; its manifest and 17 files cover 8 recorded checks, all `PASS` with exit code 0: `d0-discovery` (finalized 01:28:15Z), `step-0b-doc-delta-capture` (01:29:06Z), `ac040-02-03-catalog-config` (01:39:14Z), `ac040-04-05-admission-identity` (01:41:09Z), `ac040-06-golden-comparison` (01:42:26Z), `ac040-07-gate-ingress-offline` (01:43:03Z), `ac040-04-09-compat-cli-offline` (01:43:41Z), `ac040-09-reader-http-in-process` (01:44:19Z); there is no primary log or manifest entry for `ac040-08-evidence-validators` (T03) or `sec-reader-http-live` (T10) and no other T03 file; the branch does hold T10's two supplementary files (`http_probes.jsonl`, 22 lines, and `gunicorn_server.log`, 9 lines), so T10's probes appear to have run without being recorded. The reasons are not recorded there; one possible link, an inference and not established, is that T10 command 11 has the empty-argument defect of D-01, which would make its recording invocation fail. Its pytest and collection summaries equal this session's for every check that has one: 2,092 collected; 304, 371, 153 and 191 passed; 144 passed and 3 skipped; 339 passed. Six deterministic files are byte-identical between the two runs (both doc-delta surfaces and the four golden-comparison files); the primary logs differ as expected (executor, venue, times, durations), and the header `command` counts differ for `d0-discovery` (32 there, 28 here) and `ac040-04-05-admission-identity` (9 there, 8 here). Consequence: for T01, T02 and T04 to T09 this session's execution duplicates an execution that was already recorded and stored, and the collection authorizes no rerun (§4.2, §4.8). QA-100 did not know of it while executing. QA-100 does not decide whether this session's execution is attempt 1, an unauthorized rerun or corroboration, or how the two stored runs are reconciled for T03 and T10 (one QA root and one manifest per checkout, Plan §7.1); that is Kronos's decision at QA-110 (Glow QA Guide §10.6; collection §4.2) |
| D-13 | Process miss | This session checked for an existing evidence branch only at the storage step, after executing all ten tasks, because §4.3 and §4.8 test only the fresh clone for a pre-existing QA root. Checking origin for an earlier stored execution before starting would have exposed D-12 before any task ran |
| D-14 | Trailing whitespace in stored evidence | `git diff --cached --check` on the staged evidence flagged one line: the `E5` predicate line in the T10 primary log body ends with a space. Governed evidence bytes are not hand-edited and the file's digest is recorded, so it was left as written |

## 6. Residual state and resume point

- Server: stopped. `SIGTERM` handled, both workers exited, master shut down; PID 78820 gone; no listener on port 8000; `curl` to `http://127.0.0.1:8000/internal/version` printed `000` with exit 7 after the stop.
- QA checkout `/home/nathan/hde-epic040-qa`: now on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at commit `345148b7fce2482349828f897abbc0d7d12fe7fa`, which holds the 19 evidence files (§7). Until the storage steps it was on `main` at `0db3f0ef…` with the 19 files untracked, no tracked file modified, and nothing switched, pulled, rebased, stashed, restored or cleaned (collection §4.3 item 3); the switch was §4.7 step 2. Ignored caches (`.pytest_cache/`, `__pycache__/`) remain. The checkout is kept for checks 11 and 12 (Plan §7.1); it is now on the evidence branch.
- Virtual environment `/tmp/hde-epic040-qa-v1.2/venv` and scratch root `/tmp/hde-epic040-qa-v1.2` (63 MB in total, of which the venv is 57 MB) are kept and uncommitted. The scratch root holds every `c<k>.*` capture, `argv.txt`, `body.txt`, `status.txt`, `final.rc`, `provenance.txt` per task, the digest listings, the operator-error files of D-02, `executor_identity.txt` and `evidence_sha256.txt`.
- No secret value was handled; no database or vendor call was made.
- Resume point: QA-110 (Kronos-23) rules on the lineage of the two stored executions (D-12), evaluates the [K] predicates from the evidence it accepts (this session's files are on the evidence branch named in §1 and inventoried in §7), forms the per-task results, dispositions D-01, D-02 and D-12, and decides any attempt 2. The Product Owner decides any pull request or merge for either evidence branch and the merge of pull request #546. Checks 11 and 12 are not selected and NOT RUN.

## 7. Evidence inventory (stored on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, commit `345148b7fce2482349828f897abbc0d7d12fe7fa`)

Digests are SHA-256 over the file bytes as recorded before storage; sizes in bytes. After the push every remote blob was compared with its digest: 19 of 19 equal. All 19 paths are on the collection §4.7 permitted list, the commit's own diff against its parent lists exactly these 19 paths, and `git status --porcelain --untracked-files=all` in the QA checkout after T10 (before storage) listed no untracked path other than these 19 and no modified tracked file.

| Path | Bytes | SHA-256 |
| --- | --- | --- |
| `audit/qa/hde-epic040/qa_step_logs_manifest.json` | 1,663 | `003878cbe3dc1d6107240e8e315ec0cfdbde5acc89451b9973ceb27f8f05eda8` |
| `audit/qa/hde-epic040/00_meta/doc_deltas.md` | 2,867 | `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2` |
| `audit/docdeltas/hde-epic040_doc_deltas.md` | 2,867 | `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2` |
| `audit/qa/hde-epic040/checks/d0-discovery/primary.log` | 329,498 | `f5b0f82c7974307bc52efac98232947726f534441fe07992ce384321aa7d5c1d` |
| `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log` | 15,951 | `a64483b5460b75fbc4ce7028f238ff9e72a3f62c617c8e3361ab3d3c163d2c4b` |
| `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` | 28,542 | `170171e1bbdb61b45c5650207425eabb63fea83597a2d0088023096ef1f11aed` |
| `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log` | 12,806 | `6e622d117b9cbb9dc96845e61b34572c9d667bf62ed9d900a9cbebfaef65b5f6` |
| `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log` | 14,284 | `ffa2a4629db34c415554f32ed88365641471f2995ac440c5b688b8b7262a45cc` |
| `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log` | 36,195 | `0b8cda3488141932d45205c9285620ac1545b78c93a6a5a322f218890a6c2e73` |
| `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json` | 1,051 | `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8` |
| `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json` | 1,051 | `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8` |
| `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json` | 26,030 | `b8624a02bcc1f24aa689389fc976a5e4939f34a91e080748367e1d155824322f` |
| `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json` | 1,382 | `54d567373300a7d4a86ca44cb31a61db62d8c39493efc85d06496d2d17ae0026` |
| `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log` | 19,946 | `fea547063e4b5f2476736e0b0e1f9f35bb6b2a1ad51cab97de4db6c4e3b2758e` |
| `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log` | 14,003 | `2c69c50a0520ab0f5b2a5e7d7ed94fa745ff10120bade979f127fec6a682ac87` |
| `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log` | 12,737 | `6e53c15e3e0b496c62457887ccc39b9629c1305dfcd830bc9b6964e315452854` |
| `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log` | 73,940 | `97e37e38b75d793bef7b57d47bb024070bc7366df718edb1303d0c378022d960` |
| `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` | 11,575 | `0c09bf7fdcb265acabc0e125621d69582365f5190728f4613f9375db04e3a008` |
| `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log` | 638 | `1af474e20796fd4be6fe58cf890802b8fd8897805ca07d80f12345ee0708c5db` |

The same list, one line per file in `sha256sum` format, is in the scratch root as `evidence_sha256.txt` (not committed).

## 8. Carried lineage

- Attempts: every task carries the label attempt 1 that the collection gives it. The `06b04a9` executions of Plan v1.0 are not attempts of these tasks and were neither reused nor touched (collection §4.2; review v1.4 N-104). This session performed no Moon Loop and requested no attempt 2. An earlier stored execution of the same collection exists (D-12), so this session's execution of T01, T02 and T04 to T09 duplicates a recorded execution; whether that is attempt 1, a rerun or corroboration is for QA-110. Attempt 2 exists only through Kronos's QA-110 decision and a new QA-90 task (Plan §7.3; Glow QA Guide §10.6).
- `CANON_CONFLICT_REGISTER`: carried unchanged in the QA task collection v1.1 §6 (C040-01 to C040-09, from Plan v1.2 §2.3). QA-100 adds no entry, decides none and creates no second register.
- PR lineage: Plan v1.2 carries no `PR_RETURN_PHASE`; none exists here. The only pull request is #546, which carries these records (v1.0 and v1.1), opened by this operator session on the Product Owner's instruction. No pull request for product work or for either evidence branch was opened or continued.
- Deferred requirements (live Gate readiness; live DB Reader success): Plan §2. Not checks; no task; not run.
- Repository provenance persistence for `GCFPE_PROMPT_USES`: PENDING / NON_GATING. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent at `0db3f0ef`; the authorized repository writer owns persistence once that procedure is installed.

## 9. Canon relied on, and sources read at this invocation

Canon was resolved from `docs/pfcanon/` on `main` (`0db3f0ef`), unique controlled Markdown only.

- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.4.7 (read in full: commands are intent carriers; correctable syntax is in-flight normalization; the executed command, exit code and output belong in execution evidence); §3.4.8 (opening paragraphs read: rails posture, Moon Loop, entrypoint preflight; not read to its end); §3.4.9 (read in full: Plans confer no commit, push or pull-request authority; repository publication and evidence storage use separately authorized lanes; tested state is distinct from a later evidence-storage commit); §3.4.10 (the blocker list and the non-blocking review constraints read through the syntax-origin bullets; not read to its end); §9.2.15.5 (read in full: complete membership, actual attempt counts, record material deviations); §10.6 (read through the QA execution/evidence fault limit); §10.8 subsections "Claim separation, CI and integrity" and "Owner and authorization continuity" (read in full: QA evidence returns to Kronos; capture, synchronization and approval metadata grant no omitted action class).
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Step-log header schema expectations (required; v2)" (read in full: closed status set, exact status predicates, causal precedence, required keys, token-claim rules, template and correction boundaries, executable helper boundary).
- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`): identity checked by SHA-256 against the collection's pin. Searched at this invocation for `QA-100`, `QA_EXECUTION_RESULT` and `execute bounded`: one hit, an OPS-20 line about the OPS01 evidence branch (line 2770), which sets no rule for this stage. The addenda the tasks cite (2.5, 2.12, 2.19, 2.20, 2.22, 2.23, 2.24, 2.25, 2.27) are relied on as Plan v1.2 §1 and §2.2 and the collection record them; QA-100 did not re-read PF10 in full, and produces no addendum.
- **Documents named as task anchors by the collection** (PF01, PF05, PF06, PF09.3, PF12): cited by title in the primary-log headers as the collection directs; not read by QA-100 at this invocation.
- **In-flight documents**: the QA task collection v1.1 (read in full); Plan v1.2 (front matter, sections 1 to 12 and the check blocks 1 to 10, read; check blocks 11 and 12 and sections 13 and 14 not read); QA-70 review v1.4 (sections 1, 5, 6, 7, 8, "Canon relied on" and Provenance read); the QA-90 handoff to QA-100 (`docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.1.md`), the QA-90 checkpoint v1.1 and the QA-90 handoff RCA v1.0 (read in full); the QA Audit v1.0 (identity checked by SHA-256; not read in full).
- **Prompt**: QA-100 — Execute Bounded QA Task — 091426.1, read in full from Notion at this invocation.
- **Repository rules**: `AGENTS.md` (canon-first rule; QA output placement; redaction; governed evidence never hand-edited). No governed artifact was hand-edited: every primary log and the manifest were written by the tracked `tools.qa.qa_harness.record_check`; the Index, Mirror and path proofs were not touched. Evidence storage followed collection §4.7 on the Product Owner's explicit instruction in this session ("No I do want the evidence files in the repo. That is a misunderstanding."), stopped at §4.7's branch-exists condition, and continued only after the Product Owner chose a new branch name.

## 10. Nonclaims

This record executes no further check and establishes no QA PASS for the change, acceptance, closure, PF09 status change, deployment, release activation, token satisfaction or Index/Mirror publication. A step-log `PASS` attests the execution layer only; every [K] predicate is Kronos's at QA-110. Vendor-backed behavior (check 11), close-out deliverables (check 12), the live Gate readiness and the live DB Reader success path are NOT RUN or deferred. Nothing here edits PF-Canon or PF10 or produces an addendum. Merging any file that carries this record would preserve it and approve nothing (D21-C). This record does not decide whether this session's execution is attempt 1, a rerun or corroboration of the earlier stored execution, or how the two runs are reconciled; that is Kronos's decision at QA-110. Evidence storage is not a check and is part of no PASS predicate (Plan §7.2).

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-100-20260929-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: K040-REQ-003 to K040-REQ-013 as mapped by Plan v1.2 checks 1 to 10
  - prompt: QA-100 — Execute Bounded QA Task — 091426.1; Notion 3db4590a05eb811a8d13c0bbbf77a848; page as of 2026-09-24T15:52:02.330Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: QA-100 QA/infra executor (Claude Code operator session opened by the Product Owner)
  - capture_time: 2026-09-29T02:04:46Z
  - execution_identity: Claude Code local session fd43ebfd-1614-44e1-8ee5-6d03da21b70a (no session URL available)
  - result: QA_EXECUTION_RESULTS v1.1 (supersedes v1.0), T01 to T10 each COMPLETE, each labeled attempt 1 by the collection with the lineage open (D-12), routed to QA-110
  - task_and_attempt_mapping: T01 `d0-discovery`, T02 `step-0b-doc-delta-capture`, T03 `ac040-08-evidence-validators`, T04 `ac040-02-03-catalog-config`, T05 `ac040-04-05-admission-identity`, T06 `ac040-06-golden-comparison`, T07 `ac040-07-gate-ingress-offline`, T08 `ac040-04-09-compat-cli-offline`, T09 `ac040-09-reader-http-in-process`, T10 `sec-reader-http-live`; each attempt 1; each result COMPLETE
  - evidence_branch_and_commit: qa/hde-epic040-qa100-plan-v1.2-run-20260929 at 345148b7fce2482349828f897abbc0d7d12fe7fa
  - pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/546 (open, not merged)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `0db3f0ef`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (QA task collection v1.1, the input of this stage).
