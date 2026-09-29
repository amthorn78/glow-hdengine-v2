---
artifact_type: QA_EXECUTION_RESULTS
artifact_id: HDE-EPIC040-QA100-QA-EXECUTION-RESULTS-T11
artifact_version: "1.0"
predecessor: none for task T11. docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.1.md holds the results of tasks T01 to T10 and is not superseded by this record
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
stage: QA-100 — Execute Bounded QA Task — 091426.1
state: RESULTS_RETURNED_TO_QA110
author: QA-100 QA/infra executor, Claude Code (model claude-sonnet-5-5, then claude-opus-5-5 after the Product Owner's /model switch during the session), delegated by the Product Owner; not Kronos, not the Product Owner
session_disposition: not a continuing session; the operator session the Product Owner opened with the QA-90 v1.3 handoff
role_session_ref: Claude Code local VS Code session f0edea78-3120-4040-92a1-020776ba5a6f (id taken from the session transcript and scratchpad path; no claude.ai session URL is available to this session)
invocation_binding: EPIC / HDE-EPIC040 / QA-100 / QA_PLAN v1.2 check 11 (task T11, attempt 1)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-100 — Execute Bounded QA Task — 091426.1 (Notion 3db4590a05eb811a8d13c0bbbf77a848; page as of 2026-09-24T15:52:02.330Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
task_collection: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md (QA_TASK_COLLECTION v1.3, TASK_READY; SHA-256 c4ae999f9a38b7bcfabb66ac92ae542a1754682debd17fbd87c18fcc936de16b as read at this invocation)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010, verified equal to the collection's pin)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025, verified)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df, verified)
qa_evidence_review: docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md (SHA-256 2d45e7f0d252a3009ffb9cc0fe3d51b9652a7929eeb798bd618f2c497ab34ac3, verified)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.4.md on main at f4be532 (SHA-256 8f3edd03dea4badd36933ef23bb726e35d7a40840277413128bf4ccaf91c0e55, verified equal to the collection's pin)
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d (product tree of the QA checkout; command 2 lists only the 19 QA evidence files of checks 1 to 10 against it)
checkout_head_at_execution: 345148b7fce2482349828f897abbc0d7d12fe7fa (branch qa/hde-epic040-qa100-plan-v1.2-run-20260929)
evidence_branch: qa/hde-epic040-qa100-plan-v1.2-run-20260929, commit 380cf46fda95686ccf71f256521e63ca0eb5c9e1 on parent 345148b7fce2482349828f897abbc0d7d12fe7fa; pushed; exactly the 7 files of section 7; no pull request
observed_revision: f4be5329220ab6e75db85b2eb19ba20f71c8d775 (origin/main when this record was written)
routing: QA-110 — Review QA Evidence and Route the Next Action — 091426.1, in the continuing Kronos-23 session
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-100 (QA-100 is not an addendum producer; the Product Owner separately directed a PF10 addendum in this session, produced after this record as its own change, section 5)
---

# HDE-EPIC040 — QA-100 execution result v1.0: task T11 `open-rails-showcompat-vendor` (QA Plan v1.2 check 11), attempt 1

## 1. Result

| Field | Value |
| --- | --- |
| Task | T11 `open-rails-showcompat-vendor` of `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md`, attempt 1 (collection §4.2) |
| Result state | `COMPLETE`. No state is an acceptance or a QA PASS |
| Step-log status recorded | `PASS`, empty reason. It attests the execution layer only (Plan §12, two result layers) |
| [K] predicates | K1 to K3 not evaluated by QA-100; pending QA-110 |
| Final decisive command | Command 26 (`python -m json.tool` on `reader_v1_ba.json`), exit 0 |
| Vendor calls | Commands 14 (AB) and 15 (BA), each run once, exactly as written, both exit 0 with empty stderr; started 2026-09-29T05:52:14Z. The request limit of collection §5 held (two CLI invocations) |
| Primary log | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`, finalized 2026-09-29T05:53:32Z |
| Main deviation | Commands 4 to 28 and the Part B displays and writer were executed by this session as the Product Owner's delegated agent, not by the Product Owner in person (§4, D-01) |
| Evidence storage | PERFORMED on the Product Owner's instruction given at the start of the session: commit `380cf46fda95686ccf71f256521e63ca0eb5c9e1` on the Run B branch, pushed, 7 of 7 remote blobs equal to their recorded SHA-256 (§7) |
| Not selected, not run | Plan check 12 `qa-closeout-deliverables`: NOT RUN (collection §3) |
| Next stage | QA-110 — Review QA Evidence and Route the Next Action — 091426.1 (Kronos-23) |

## 2. Identity, venue and environment

| Field | Value |
| --- | --- |
| Executor | Claude Code local VS Code session `f0edea78-3120-4040-92a1-020776ba5a6f`, the QA/infra executor of collection §4.1, written to `recorder_identity.txt` in Part A and to the CONTEXT section of the primary log. Commands 1 to 3, Part C and the recording, as the collection assigns; and, on the Product Owner's direction, commands 4 to 28 (D-01) |
| Venue | The Run B venue of ruling LR-01 item 6: Product Owner-controlled Linux shell, host `glow-devops-vps`, Linux 6.8.0-142-generic; QA checkout `/home/nathan/hde-epic040-qa`; virtual environment `/tmp/hde-epic040-qa-v1.2/venv` (Python 3.12.3, editable install of the checkout, `hdctl` entry point `engine.cli.main:cli`) |
| Rails | Commands 1 to 3 and the recording: CLOSED prefix of collection §4.4 (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, nine keys unset per command). Commands 4 to 26: VENDOR prefix (`SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, pins; `HDAPI_BASE_URL`, `DATABASE_URL`, the three retired bridge keys and `ENGINE_ENV` unset per command). Commands 27 and 28 without a prefix. No shell had its own rails opened |
| Vendor posture under the VENDOR prefix | Command 7: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` SET; `HDAPI_BASE_URL`, `DATABASE_URL`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, `ENGINE_ENV` UNSET. No value was printed, recorded or persisted |
| Inputs | Synthetic tuples A (`1999-10-16`, `04:37`, `Santiago, Chile`) and B (`1978-06-17`, `02:35`, `Tallinn, Estonia`), QA Audit L-51 default (QA50-S01) |
| Delegation | See §4, D-01 |

## 3. Setup observations (collection §4.3)

| Item | Observation |
| --- | --- |
| 1 | `HEAD` `345148b7fce2482349828f897abbc0d7d12fe7fa`; branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`; `git status --porcelain --untracked-files=all` empty |
| 2 | `git fetch origin` exit 0; `git ls-remote --heads origin 'qa/*'` listed `qa/hde-epic040-qa100-checks-1-10` (`06b04a9`), `qa/hde-epic040-qa100-plan-v1.2` (`e5b671c`) and the Run B branch at `345148b7fce2482349828f897abbc0d7d12fe7fa`. `git ls-tree -r --name-only` of the check 11 directory printed nothing on all three branches, exit 0. No earlier execution of check 11 exists on origin; no open pull request (`gh pr list`: empty) |
| 3 | `test -e` of the check 11 directory exit 1; the manifest had 10 entries |
| 4 | `/tmp/hde-epic040-open-rails-showcompat-vendor` and its `-quarantine` sibling both absent (exit 1) |
| 5 | `/tmp/hde-epic040-qa-v1.2/venv/bin/python --version` printed `Python 3.12.3`; not re-created |
| 6 | Storage authorization asked before Part A. The Product Owner's answer: "Yes, store it" (branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, files under `audit/qa/hde-epic040/` only, pushed, no pull request). For this record: "Push a new docs/ branch and open the PR" |
| 7 | `mkdir -p /tmp/hde-epic040-open-rails-showcompat-vendor` exit 0 |

The pins of the collection were verified before Part A: Plan v1.2, review v1.4, QA Audit v1.0, QA-110 review v1.0, QA-100 results v1.1, PF10 v13.4.4, collections v1.1 and v1.2, all equal.

## 4. QA_EXECUTION_RESULT — T11 `open-rails-showcompat-vendor` — COMPLETE, step-log `PASS`

Change HDE-EPIC040 (Epic); Plan `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md` check 11; review v1.4; QA Audit v1.0; attempt 1; tokens `[]`, `[]`. `[E]` lines give observed values, as the primary log's PREDICATES section records them.

| Command or step | Observed |
| --- | --- |
| 1 | exit 0, `345148b7fce2482349828f897abbc0d7d12fe7fa` |
| 2 | exit 0, 19 paths, all under `audit/` |
| 3 (recording preflight) | exit 0, `/home/nathan/hde-epic040-qa/audit/qa/hde-epic040` |
| W1 | CONTEXT written |
| 4 | exit 0, `2` |
| 5, 6 | `Python 3.12.3`; exit 0, `/tmp/hde-epic040-qa-v1.2/venv/bin/python` |
| 7, 8 | exit 0; `15` |
| 9, 10 | manifest printed; `10` |
| 11 | `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96  catalog/manifest.json` |
| 12, 13 | exit 0, exit 0 (`vendor_request.txt` written, `time_utc: 2026-09-29T05:51:11Z`) |
| D1 | every line equal to its expectation |
| 14, 15 | exit 0 and exit 0; stderr 0 bytes each |
| 16 | `2` |
| 17 | `vendor_run_ab.json 3303`, `vendor_run_ba.json 3303`, `reader_v1_ab.json 330`, `reader_v1_ba.json 330` |
| 18, 19 | `cmp` exit 0 and exit 0 |
| 20 | digests of the five deliverables (§7) |
| 21, 22 | exit 1 and exit 1; 89 and 93 `path:count` lines, every count 0 |
| D2 | `1`, `1`, `END`. Q1 and Q2 not run; nothing quarantined; no quarantine directory exists |
| 23 to 26 | exit 0 each |
| 27, 28 | exit 0; `HD_API_KEY=UNSET`, `GEO_API_KEY=UNSET`, `HD_API_BASE_URL=UNSET` in the executing shell |
| W2 | `W2_WRITTEN` |
| C1 | `c14.rc=0`, `c15.rc=0`, `c21.rc=1`, `c22.rc=1`, no `path:count` line, `2`, `END` |
| C2, E lines, W4 | written; E1 to E8 `PASS`; R `PASS`; K1 to K3 `pending QA-110`; LIMITS with the `DOC_DELTA:` line of collection §2.5 |
| C3 | `status.txt` `PASS`; `final.rc` `0`; `captured_env.txt` the six vendor-posture lines of command 7 |
| Pre-record re-scan (observation, not a check command) | the values of `HD_API_KEY`, `GEO_API_KEY` and `HD_API_BASE_URL` searched in the finished `body.txt`, `argv.txt`, `provenance.txt` and the check directory: 0 files with a hit for each |
| C4 | exit 0; printed the primary log and the manifest paths |
| C5 | manifest valid JSON, 11 unique keys; entry `open-rails-showcompat-vendor` with the full `log_path` and status `PASS` equal to the header status; header `pf27.step_log_header.v2`, 14 keys, empty `status_reason`, `exit_code` 0, 28 commands, `captured_env` `{"ALLOW_NETWORK":"1","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"0","TZ":"UTC"}`, `evidence_artifacts` the primary log and the five deliverables, `pf_refs` PF05, PF19, PF07 titles, both token arrays empty; 64,998 bytes, one final LF, no CR |

Normalizations: N-02, N-03, N-05, N-06, N-20 to N-35 (collection §4.10), and executor normalization E-01 (§5). Residual state and resume point: §6.

### Deviations and observations

| ID | Kind | Statement |
| --- | --- | --- |
| D-01 | Executor of commands 4 to 28 | Collection §4.1 and Plan v1.2 §7.1 assign commands 4 to 28, the displays D1 and D2, the quarantine commands and W2 to the Product Owner in person, and Plan §7.1 states "No automated agent executes a vendor call, handles a plaintext secret or connects to the shared database". After Part A the Product Owner directed: "you need to execute all the steps as my agent", and then "yes agents can run live vendor calls when directed, and the environmental variables hold the vendor information". This session executed them as the Product Owner's delegated agent. Canon basis relied on: HDE Governance §3.4 ("A PO-delegated automated session agent MAY execute the exact authorized vendor call only within the task-specific scope, rails, request limit, stop checks, redaction, and evidence contract") and §9.1, Change Process Guide "Ops tasks" execution authority and delegation contract, and Plan Templates "Execution authority (normative)" ("PO-only" does not require the Product Owner to be the physical keystroke actor). Contrary canon: Glow QA Guide §3.5.7 ("Automated agents may define intent, safety rails, success criteria, evidence requirements, and rollback intent, but MUST NOT execute the vendor call, handle plaintext secrets, or claim completion without PO-run evidence") and HDE CLI/API Vendor Ref §3.7 ("Automated agents MUST NOT run the vendor call"); collection v1.3 §7 had recorded this conflict as not affecting T11 while the Product Owner ran the calls. Every command, rail, input, stop rule, scan and predicate was applied unchanged; no value was printed, recorded or persisted. `vendor_request.txt` (command 13, whose text is fixed by the collection) and the primary log's CONTEXT line `VENDOR_COMMAND_EXECUTOR` therefore still name the Product Owner as executor of the vendor commands; the primary log's PREDICATES section carries an `EXECUTION DEVIATION:` line and the header's `command_provenance` states the actual executor. QA-110 decides the effect on this attempt (Plan §7.3 routes authority issues through QA-110) |
| D-02 | Vendor configuration availability | At the Product Owner's direction, a presence check (SET or UNSET only) in this session's shell first showed `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL` and `DATABASE_URL` all UNSET (an earlier attempt at the same check was refused by the harness permission classifier and did not run). A search of this machine's shell profiles, `.env` files and VS Code and Claude settings files for those names (file, line and name only) found them only in the tracked template `.env.example`. The Product Owner then set them; a re-check showed `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL` SET and `HDAPI_BASE_URL` UNSET. The session-setup `read -rs` lines of Part B were therefore skipped as the collection allows ("Skip a line if that key is already set in this terminal"). `DATABASE_URL` was removed from every vendor command by the VENDOR prefix (command 7 recorded it UNSET) |
| D-03 | Restore scope | Command 27 unset the three keys in the shell that ran commands 23 to 28, and command 28 confirmed it. Each of this session's shells starts from the environment the Product Owner configured, so the keys are present again in later shells. The recording (C4) ran under the CLOSED prefix, which unsets them per command |
| D-04 | Evidence commit identity | The first `git commit` in the QA checkout failed with "Author identity unknown"; nothing was committed or pushed. The commit was then made with the identity of the Run B commit `345148b7` (`amthorn78 <146120956+amthorn78@users.noreply.github.com>`), passed with `git -c` on that one command; no git configuration was changed |
| D-05 | Scratch helper files | For E-01 the session wrote command-text copies `.c13_src`, `.c2_src`, `.c27_src`, `.c28_src`, `.w2_src`, `.w4_src`, `.c4_src` and a timestamp `.vendor_start_utc` into the scratch directory. `.c13_src` existed when commands 21 and 22 ran and scanned 0; the others hold only collection text or a time. `/tmp` glue (Glow QA Guide §3.4.8); not evidence; not committed |
| D-06 | Collection defect: "three vendor keys" | Collection v1.3 Part B tells the Product Owner to "Set the three vendor keys from your own store", and §4.1 treats `HD_API_BASE_URL` as a secret. The product code reads two credentials, `HD_API_KEY` and `GEO_API_KEY` (`engine/bodygraph/vendor_client.py` L333 to L335; `engine/providers/vendor_http_hdapi.py` L60 to L67), and takes the base URL as configuration from `HD_API_BASE_URL`, or from `HDAPI_BASE_URL` when that is absent, failing closed on conflicting values (`engine/bodygraph/vendor_client.py` L196 to L201; `engine/bodygraph/resolver.py` L410 to L420). The Product Owner stated that there are two API keys, held in the environment variables. No effect on this execution; for QA-110 and the QA-120 RCA |
| D-07 | Plan posture versus a held environment | The VENDOR posture (Plan §5.2; collection §4.4) removes `HDAPI_BASE_URL` from every vendor command and requires `HD_API_BASE_URL` SET. QA-90 checkpoint v1.3 recorded that the Kronos cloud environment holds `HDAPI_BASE_URL`, not `HD_API_BASE_URL`; in such an environment D1 would fail and the check would be `TOOLING_BLOCKED` although the code accepts that key. Not the case here (`HD_API_BASE_URL` SET). For QA-110 |
| D-08 | `.env.example` | The tracked template lists `HD_API_BASE_URL`, `HD_API_KEY` and `HD_API_SECRET` but not `GEO_API_KEY`, which the vendor path requires; unchanged since `a4652dc6` (2025-09-25). Repository documentation drift; owner: the implementation lane. Not corrected here |
| D-09 | Model switch | The Product Owner switched this session's model from claude-sonnet-5-5 to claude-opus-5-5 before the vendor commands ran. The session, its identity and its scratch state are unchanged |

## 5. Executor normalization and the Product Owner's canon direction

- **E-01.** Command lines 13 to 28 and the writers C2, W4, W2 and C4 were fed to the capture function, or to `bash`, from the collection file by line number (`sed -n '<line>p'`), each line first checked against its expected prefix, instead of being retyped; commands 4 to 12 were entered as the collection's quoted here-document blocks. The bytes executed are the collection's bytes, and `argv.txt` holds the 28 check commands as run. Proof target, rails, evidence identity and predicates are unchanged (Glow QA Guide §3.4.10; Plan §12).
- **Stored vendor-run environments (from governed evidence, read-only).** Every earlier stored HumanDesignAPI vendor run found both keys and a base URL in the operator environment: HDE-EPIC028 OPS-02 (`GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL` SET, Codespace), HDE-EPIC034 OPS-02 (`HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` SET; executed by "Codex acting as PO tooling per user authorization"), HDE-EPIC035 OPS-01, HDE-EPIC037 OPS-01 and HDE-EPIC038 OPS-02 (base URL and keys present). Paths are under `audit/ops/` for those changes.
- **Repository history of the conflicting canon text (read-only, `git log -S` over `docs/pfcanon/`).** The agent bar in Glow QA Guide §3.5.7 and HDE CLI/API Vendor Ref §3.7 first appears in commit `94c9291a` (2026-05-09); the delegated-agent permission in HDE Governance §3.4 first appears in `489f9c66` (2026-08-05, PF04 v2.7.4). The two texts have coexisted since then.
- **PF10 addendum.** The Product Owner directed in this session: "at the end of this create a PF10 build notes addendum, for 2 reasons, yes agents can run live vendor calls when directed, and the environmental variables hold the vendor information, and always have". That canon change is the Product Owner's direction, not a QA-100 output; it is produced after this record as a separate pull request that the Product Owner merges. Nothing in this result depends on it.

## 6. Residual state and resume point

- QA checkout `/home/nathan/hde-epic040-qa`: branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `380cf46fda95686ccf71f256521e63ca0eb5c9e1`, equal to origin; working tree clean. Kept for check 12 (Plan §7.1).
- Scratch `/tmp/hde-epic040-open-rails-showcompat-vendor/`: every `c<k>.*` capture, `argv.txt` (28 lines), `cmds.txt`, `body.txt`, `recorder_identity.txt`, `status.txt`, `final.rc`, `provenance.txt`, `captured_env.txt` and the D-05 helper files. Kept, never committed. No quarantine directory exists.
- Virtual environment `/tmp/hde-epic040-qa-v1.2/venv`: kept.
- No database connection was made. No server was started. The vendor keys remain in the environment the Product Owner configured (D-03).
- Resume point: QA-110 (Kronos-23) evaluates K1 to K3 from the four JSON files, the command 11 digest and the body; forms the per-task result; dispositions D-01 to D-09; classifies nothing as a vendor failure (none occurred). Check 12 `qa-closeout-deliverables` needs the Product Owner's selection through QA-90 and then runs in the same checkout.

## 7. Evidence inventory (branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, commit `380cf46fda95686ccf71f256521e63ca0eb5c9e1`)

SHA-256 over the file bytes; sizes in bytes. After the push each remote blob was hashed from `origin`: 7 of 7 equal. The commit's diff against its parent lists exactly these 7 paths, all on the collection §4.8 permitted list.

| Path | Bytes | SHA-256 |
| --- | --- | --- |
| `audit/qa/hde-epic040/qa_step_logs_manifest.json` | 1,836 | `f11fbdbc5a978772cd8ad0847a4341320939fbd17505843ef6426ed2d623bc96` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log` | 64,998 | `1e4341e27e1ce47fe172546581ac4737e2dcb9745f82bac42f0001ac6f5f4674` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt` | 2,312 | `328508d8a020e84d6d74078331c7221233556ee69b389893160057073e92c4a9` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json` | 3,303 | `e33377d7eab26ed1693b6ebbe5166b88cca5c38f300999c94a30db057c1fa564` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json` | 3,303 | `e33377d7eab26ed1693b6ebbe5166b88cca5c38f300999c94a30db057c1fa564` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json` | 330 | `103df389283c7e577ebd78d377eb49fe6b7d014b732389577ea9efbbe1de32d0` |
| `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json` | 330 | `103df389283c7e577ebd78d377eb49fe6b7d014b732389577ea9efbbe1de32d0` |

## 8. Carried lineage

- Attempts: T11 attempt 1 (collection §4.2). No earlier execution of check 11 exists on origin (§3 item 2). No Moon Loop, no rerun, no operator-error repeat.
- `CANON_CONFLICT_REGISTER`: carried unchanged in collection v1.3 §6 (C040-01 to C040-09). QA-100 adds no entry. The executor conflict of D-01 was already recorded outside the register in collection v1.3 §7.
- PR lineage: Plan v1.2 carries no `PR_RETURN_PHASE`. The only pull request this session opens for QA records is the one carrying this file.
- Repository persistence of `GCFPE_PROMPT_USES`: PENDING / NON_GATING; `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent at `f4be532`.

## 9. Canon relied on, and sources read at this invocation

Canon resolved from `docs/pfcanon/` on `main` (`f4be532`; the working tree's `docs/pfcanon/` equals `origin/main`).

- **HDE Build Notes v13.4.4**: 2.27, 2.28 (RA-10, Q-2), 2.29 (canon location and change-document storage), 2.32 and 2.33, read in full; searched for executor and delegation terms, with no rule on who executes a vendor call.
- **Glow QA Guide**: §3.3, §3.4.7, §3.4.8, §3.4.9, §3.4.10, §3.5.5, §3.5.6, §3.5.7, §4.4.1 to §4.4.7, §9.2.15.5, §10.6, §10.8, §11.1, read in full.
- **HDE Governance**: §3.4 "Open rails (controlled)" and §9.1 "Ops tasks", read in full.
- **HDE CLI/API Vendor Ref**: §3.7 and §7.3.9, read in full.
- **Glow Infrastructure**: §2.7, read in full.
- **Plan Templates**: "Step-log header schema expectations (required; v2)", "Vendor-dependent steps (rails-scoped)", "Proof-class and controlled vendor-smoke boundary (required when applicable)" and "Execution authority (normative)", read in full.
- **Change Process Guide**: the "Ops tasks" passage (execution authority, delegation contract, permitted stops), read in full.
- **In-flight documents**: collection v1.3 (read in full), Plan v1.2 (§7, §12 common rules, check block 11), QA-70 review v1.4 §6 to §8, QA-110 review v1.0 (via PF10 2.32), QA-100 results v1.1, QA-90 checkpoint v1.3 and handoff v1.3.
- **Prompt**: QA-100 — Execute Bounded QA Task — 091426.1, read in full from Notion.

## 10. Nonclaims

This record establishes no QA PASS for the change, acceptance, closure, PF09 status change, deployment, release activation, token satisfaction, Index or Mirror publication, or broad HumanDesignAPI v2 conformance. The step-log `PASS` attests the execution layer only; K1 to K3 and the per-task result are Kronos's at QA-110. Check 12 is NOT RUN. The vendor calls prove only what check 11 exercises (collection §5 nonclaims). Evidence storage is not a check and is part of no PASS predicate. Merging the pull request that carries this record preserves the record and approves nothing (D21-C).

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-100-20260929-02
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-04 and AC040-09 (vendor-backed part), PO Q-2, as mapped by Plan v1.2 check 11
  - prompt: QA-100 — Execute Bounded QA Task — 091426.1; Notion 3db4590a05eb811a8d13c0bbbf77a848; page as of 2026-09-24T15:52:02.330Z; release GCFPE-20260914.1
  - role_stage: QA-100 QA/infra executor and, on the Product Owner's direction, delegated executor of the vendor commands
  - capture_time: 2026-09-29T05:55:08Z
  - execution_identity: Claude Code local VS Code session f0edea78-3120-4040-92a1-020776ba5a6f
  - result: T11 COMPLETE, step-log PASS; evidence commit 380cf46fda95686ccf71f256521e63ca0eb5c9e1
  - task_and_attempt_mapping: T11 `open-rails-showcompat-vendor`, attempt 1
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md`)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-90-20260929-02 (collection v1.3); GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (results v1.1, T01 to T10).
