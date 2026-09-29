---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-EPIC040-QA90-QA-TASK-COLLECTION
artifact_version: "1.3"
predecessor: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.2.md (TASK_READY; task T11 at attempt 1, never executed; SHA-256 6dec3bae15580fe88ee8994368ef2fa6dfb95d0b4dc20478f7c54810b717c9b3; preserved unchanged and superseded for T11 by this version, which repairs it as §1.1 records). docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md (SHA-256 4d498d91382a16df3a73653172fa00d427402a9c12ad85e6d2589d699415f836) remains the issued source of T01 to T10
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-90 / QA_PLAN v1.2 check 11 (repeated invocation)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 091426.1 (Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (APPROVE by Isis-52, 2026-09-28T00:26:24Z; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df)
qa_evidence_review: docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md (T01 to T10 ACCEPT; ruling LR-01; lessons K-01 to K-04; SHA-256 2d45e7f0d252a3009ffb9cc0fe3d51b9652a7929eeb798bd618f2c497ab34ac3)
execution_results: docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.1.md (executor, venue, checkout and evidence branch that check 11 continues; SHA-256 afcb8df263c1e2295caa63e0fb213a3f1c48da8a8dca6ea0470eb1199944e041)
selection: Product Owner, "Task: 11" at this QA-90 invocation on 2026-09-29, the same selection as the "Task to run: 11" that collection v1.2 packaged = QA Plan v1.2 check 11 `open-rails-showcompat-vendor`
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.4.md on main since 4ad12fe (SHA-256 8f3edd03dea4badd36933ef23bb726e35d7a40840277413128bf4ccaf91c0e55, byte-identical to the working-tree copy that collection v1.2 read; v13.4.2 is no longer on main)
observed_revision: 4ad12fe4be4c8149b9159adb1abe7812a8b5da50 (origin/main at authoring; `git diff --name-only` from the tested source 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d lists only files under `docs/ephemeral/`, `docs/pfcanon/` and `docs/prompt_ecosystem_management/`)
routing: QA-100 — Execute Bounded QA Task — 091426.1, in the operator session the Product Owner opens with this collection's handoff
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
---

# HDE-EPIC040 — QA Task Collection v1.3 (QA-90): check 11 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Task | T11 `open-rails-showcompat-vendor`, Plan v1.2 check 11, attempt 1 (§4.2) |
| Selection | Product Owner "Task: 11" = Plan check 11 only, the selection that collection v1.2 packaged. Check 12 is not selected (§3) |
| Repeated invocation | Collection v1.2 was inspected in full and its command blocks were dry-run (§2.4). This version reuses it unchanged except for the repairs of §1.1. Its T11 was never executed, so T11 stays attempt 1 |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING`: the Plan's check 11 block is complete and every locus it uses exists at the tested source (§2.4, §2.5). The defects repaired in §1.1 are in collection v1.2, not in the Plan |
| Normalizations | N-20 to N-35 (§4.10), plus N-02, N-03, N-05 and N-06 carried from collection v1.1. None changes the Plan's objective, target, rails, evidence identity or predicates |
| Applied from QA-70 review v1.4 | N-101 (scratch files absent before the recording preflight), N-102 (secret values read from standard input), N-103 (delegation record), N-104 (attempt statement) |
| Applied from QA-110 review v1.0 | LR-01 item 6 (Run B checkout and branch); K-01 (no empty argument), K-02 (one command per fenced block), K-03 (origin checked before the first command), K-04 (dry-run through `CheckResult`; recording is not a check command) |
| Evidence storage | Branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, one fast-forward commit of the check 11 evidence files and the manifest, pushed, no pull request by the executor (§4.8) |
| Next stage | QA-100 — Execute Bounded QA Task — 091426.1, in the operator session the Product Owner opens with the handoff of this collection. The Product Owner runs the vendor commands in that session's QA console. Collection v1.2 and its handoff are not used |
| Not done by QA-90 | Execution, a vendor call, evidence acceptance, a PASS declaration, selection of any step, a rerun, merge, PF-Canon or PF10 edits, addendum production |

### 1.1 Repairs to collection v1.2

This invocation's inspection and dry run of collection v1.2 (§2.4) found the defects below. Each is a defect of the QA-90 task packaging, which is Kronos-23's own, not of the Plan. Each repair carries out Plan check 11 command 6 ("Expected 0 everywhere. The stderr text of both runs is then added to the body"), the check's `FAIL_TOOLING` and `TOOLING_BLOCKED` conditions, and HDE Governance §3.4 ("Any secret-bearing artifact MUST be quarantined, named in the result summary, and excluded from proof") more strictly than v1.2 did. No repair changes a Plan objective, proof target, rails posture, evidence identity or predicate. The repairs also reach §4.1 (the executor's reading rule), §4.3 item 4 (the quarantine directory must be absent too) and §4.5 (the list of non-check commands and W2's gate). The front matter, §1, "Canon relied on", §2, §3, the delegating act in §4.1, §4.2, §6 to §8 and Provenance record this invocation. Every other rule and command is carried from v1.2 unchanged.

| ID | v1.2 locus | Defect and evidence | Harm | Repair (v1.3 locus) |
| --- | --- | --- | --- | --- |
| V-01 | §4.6, the rule for commands 14 and 15; Part C, C1 | If a vendor command could not be run as written, the PO was sent to commands 27, 28 and W2. When command 14 had already run, that skipped the secret scan (commands 21 and 22), which cannot run once command 27 has unset the keys. C1 then read the missing scan files as "no vendor command ran" | Command 14's stdout, stderr and Reader dump would reach `body.txt` through W2, the primary log through C4 and the evidence commit through §4.8, all unscanned | §4.6: once command 14 has run, every remaining command runs in order, so the scan comes before the restore (N-34). C1 reports the vendor and scan exit files mechanically (N-35) |
| V-02 | Display D2; writer W2 | D2 printed every `path:count` line of both scans for the PO to check by eye before W2; the dry run printed 87 and 91 lines. W2 then copied both vendor stderr captures into `body.txt` with nothing to stop it if a named file was still in place. No rule covered a scan that exited 2 | One missed line puts a secret-bearing capture into the primary log and the pushed evidence branch | D2 prints only the two exit codes, any line whose count is not 0, and `END`; Q1 and Q2 quarantine mechanically (N-32). W2 writes nothing and prints `W2_NOT_WRITTEN` while a named file is in place, while any vendor-run file is in place after a failed or missing scan, or while `body.txt` is absent (N-33) |
| V-03 | §4.7 | No status covered a vendor command that was not run because it could not be run as written while E1 to E3 hold | The executor would have had to choose a status the task does not give | §4.7 item 2: `TOOLING_BLOCKED` (Glow QA Guide §3.3; Plan Templates "Exact status predicates"), below `FAIL_TOOLING` in precedence. §4.7 item 1 now names each vendor command's own two files, because the dry run showed "one of its two deliverables" could be read across both commands |
| V-04 | §5, "Request limit" | Said the vendor client retries on 429. `engine/bodygraph/vendor_client.py` retries only after a 5xx response or a transport failure (`_is_retryable_error_class`) | None on the bound: at most 3 attempts per request and 12 requests in total still hold | Wording corrected |
| V-05 | Front matter; "Canon relied on"; §2.2; §7 | Written while PF10 v13.4.4 was a working-tree copy. `main` now carries it (`4ad12fe`) and no longer carries v13.4.2 | The PF10 overlay path in §2.2 named a file no longer on `main` | Paths and currency updated; §7 items resolved or carried |

Editorial changes: the Part A example identity is shortened to the session identity, and every reference to this task inside the commands names v1.3.

## Canon relied on

Read from `docs/pfcanon/` on `main` at `4ad12fe`. There `docs/pfcanon/` differs from `3c29ef4`, where collection v1.2 read it, only in that PF10 v13.4.4 replaces v13.4.2.

- **HDE Build Notes, v13.4.4** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.4.md`, on `main` since `4ad12fe`, byte-identical to the working-tree copy that collection v1.2 reviewed). Its difference from v13.4.2, compared with whitespace ignored, was read in full at this invocation: the version and date, an index entry for 2.32 and none for 2.33, table alignment rows, one link form, the RA-06 row of 2.28, the removed end marker, and the two new addenda. 2.32 "HDE-EPIC040-QA110 — QA Evidence Review v1.0 (tasks T01 to T10 of QA Plan v1.2)" and 2.33 "PF10-OPENRAILS-001 — Mandatory Live Vendor Open-Rails Test in Every QA Plan Touching Production-Functional Surfaces" were read in full. 2.32 records the QA-110 review this collection follows (LR-01 item 6; K-01 to K-04; checks 11 and 12 on the Product Owner's selection). 2.33: the open-rails test is a live vendor call under `SAFE_MODE=0`, `ALLOW_NETWORK=1`, with synthetic data only; closed-rails tests, mocks, fake services and generated artifacts do not substitute for it; the existing conditions of PO authorization, secret-safe evidence, redaction, a defined request limit and classification of failures before any is treated as a product failure are unchanged. T11 meets 2.33 (§2.5). Searched at this invocation for `QA-90`, `QA_TASK`, `bounded QA task`, `attempt 2`, `open-rails`, `open rails`, `showcompat`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `evidence branch`, `PO Live QA`, `vendor smoke`, `PO-only`, `quarantin`, `secret scan`, `secret-bearing`, `physical executor` and `PO-delegated`. The hits are in 2.11, 2.14, 2.18 and 2.22 (records of other work), 2.27, 2.28, 2.32 and 2.33. No addendum sets a rule for packaging a vendor QA task, the scan-and-quarantine sequence of a vendor step, recording a PO-run check or the base-URL key, so HDE Governance, the Glow QA Guide, Plan Templates, the HDE CLI/API Vendor Ref and Glow Infrastructure govern. 2.27 "Evidence storage", 2.28 (RA-10: the bounded open-rails step is required) and 2.29 "PF10-CANON-001" are relied on as collection v1.2 records them; the other addenda as Plan v1.2 §1 and §2.2 record them.
- **HDE Governance** (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`): §3.4 "Open rails (controlled)", read at this invocation from "PR-specific bounded development-proof exception" through the `PASS` rule of the controlled vendor-backed no-user smoke. Persisted secret-bearing output is `FAIL_TOOLING`; "Any secret-bearing artifact MUST be quarantined, named in the result summary, and excluded from proof"; the controlled no-user smoke is PO-only and IA-guided; missing preflight facts are `TOOLING_BLOCKED` and the vendor call does not run.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`): §3.3 and §3.5.5 to §3.5.7, each read in full at this invocation (vendor-backed `showcompat` with birth-only inputs and an explicit vendor source; controlled smoke preflight, evidence and outcome predicates; `TOOLING_BLOCKED` when the smoke cannot run; secret-bearing artifacts quarantined and excluded from proof; PO-only execution; the production-affecting open-rails minimum; `HD_API_BASE_URL` canonical; automated agents do not execute the vendor call or handle plaintext secrets). §3.4.7 to §3.4.10, §4.4.1 to §4.4.7, §9.2.15.5, §10.6, §10.8 and §11.1 as read at QA-110 in this session, unchanged on `main` since.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Step-log header schema expectations (required; v2)" (closed status set, exact status predicates, causal precedence, required keys), "Vendor-dependent steps (rails-scoped)" and "Proof-class and controlled vendor-smoke boundary (required when applicable)", each read in full at this invocation.
- **HDE CLI/API Vendor Ref** (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`): §3.7 "Interim “no-user” QA mode (pre-Glow prod)" (allowed and forbidden inputs; birth values from `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`; PO-only; automated agents do not run the vendor call; outcome classes) and §7.3.9 "HumanDesignAPI v2 live conformance pending" (bounded open-rails step; exercised versus inferred route behavior), each read in full at this invocation; §1, "Base-URL, API-version, and credential posture" (`HD_API_BASE_URL` canonical), read at this invocation.
- **Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §2.7 "Terminal CLI access as admin surface", including "CLI-local vendor smoke target distinction (names-only)", read in full at this invocation.
- **Technical Writing Best Practices** (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`): "Truth and source fidelity", as read at QA-90 v1.1 (unknown stays unknown; no invented paths, commands, flags or identities).

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, QA_PLAN v1.2, approved by `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`. Read at this invocation: the front matter, §1 to §8, §10 (the check 11 row and §10.1), §11, the §12 common rules and check block 11; the register of §2.3 was compared row for row with §6 below and is identical. §9, §13 and §14 are relied on only as collection v1.2 records them. This collection packages check 11; it rewrites none of the Plan's content.

### 2.2 Overlays

| Overlay | Repository path | Effect on T11 |
| --- | --- | --- |
| PF10 addenda | `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.4.md` | The addenda that Plan v1.2 §1 and §2.2 list; 2.28 RA-10 requires this step. Added after the Plan's approval: 2.32, which records QA-110 review v1.0 (two rows below), and 2.33, which requires a live vendor open-rails test with synthetic data only; T11 is that test (§2.5). Neither changes the Plan's content |
| QA-70 review v1.4 execution notes | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md` §6 | N-101: §4.3 item 4 and the preflight order. N-102: commands 21 and 22. N-103: §4.1. N-104: §4.2 |
| QA-110 review v1.0 | `docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md` §4.2, §6.2, §8 | LR-01 item 6: T11 runs in the Run B checkout and stores on the Run B branch. K-01 to K-04 applied (§1). T01 to T10 each `ACCEPT` |
| PO disposition v1.0 | `docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md` | Q-2: the PF05 §7.3.9 open-rails step applies, with no exemption. It grants no execution authority by itself; this task defines that authority |

### 2.3 Aids (not overlays)

- `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`: loci L-01, L-03, L-05, L-33, L-41, L-42, L-51, L-52; findings QA50-F07, QA50-F10, QA50-S01, QA50-B01.
- `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md`: decision QA50-S01 ("Synthetic QA tuples, recorded verbatim as Glow QA Guide §3.3's substituted birth-input record, satisfy both that section and Plan v2.1 §7.4. Default: the L-51 tuples"), carried unchanged by review v1.4 §7.
- `docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.1.md` §2, §6, §7: the QA console, checkout, virtual environment and evidence branch that T11 continues.
- `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md` §4: format lineage and the closed-posture prefix. No task of v1.1 is re-issued here.
- `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.2.md`, with its checkpoint and handoff: the predecessor this version reuses, except for §1.1.

### 2.4 Read-only repository observations (authoring aids, not QA evidence)

At `4ad12fe` (`main`), whose product code equals the tested source `0db3f0ef` (re-read at this invocation):

- `engine/cli/main.py`: `showcompat` defines `--source {db,vendor,auto}`, the six birth flags and `--dump-reader`. With `--source vendor`, both parties resolve with `source_policy="vendor"`; the Reader dump is written only after the pair is evaluated, so a failed run leaves no dump; stdout passes the `STDOUT_MISSING_LF` and `STDOUT_CRLF` guards. A failure writes one line to standard error: a `VendorError` code, a compat-boundary token, an admission refusal code, or `CLI_UNEXPECTED:` followed by the exception text, each with exit 1; or a `CliError` code (default exit 64; an argument error prints the usage instead). A successful run writes nothing to standard error; no module on the vendor path logs to it.
- `engine/bodygraph/resolver.py` `_acquire_dry_run`: refuses `PROVIDER_REFUSED` when `SAFE_MODE` is true and `PROVIDER_NETWORK_BLOCKED` when `ALLOW_NETWORK` is not; reads `HD_API_BASE_URL` (refusing `PROVIDER_CONFIG_INVALID` when it and `HDAPI_BASE_URL` conflict, `PROVIDER_CONFIG_MISSING` when both are absent); takes the v2 `charts` path or the explicit legacy fallback by the configured base; never persists. The v2 dry-run client is built without a log path, so a vendor run writes no file into the checkout.
- `engine/bodygraph/vendor_client.py`: HTTP 401 → `PROVIDER_UNAUTHORIZED`, 403 → `PROVIDER_FORBIDDEN`, 404 → `PROVIDER_NOT_FOUND`, 429 → `PROVIDER_RATE_LIMITED`, 5xx → `PROVIDER_UNAVAILABLE`, other → `PROVIDER_ERROR`; malformed JSON → `PROVIDER_BAD_RESPONSE`; transport failure → `PROVIDER_NETWORK_ERROR`; a non-https base → `PROVIDER_CONFIG_MISSING`. At most 3 attempts per request (`max_attempts=3`), with a retry only after a 5xx response or a transport failure (`_is_retryable_error_class`), so a 429 is not retried. The per-attempt log is written only to a configured log path, and the dry-run client has none.
- `tools/qa/qa_harness.py`: `CheckResult` rejects an empty argv part, a non-admitted `captured_env` key and a `pf_refs` value outside `PF_TITLE_RE`; `record_check` publishes the primary log and the manifest together, verifies both and rolls back on error; an empty `captured_env` falls back to the recording process's own environment.
- `audit/ops/hde-epic030/ops-02/vendor_command.txt` (L-51) and `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json` hold the same tuples: A `1999-10-16`, `04:37`, `Santiago, Chile`; B `1978-06-17`, `02:35`, `Tallinn, Estonia`.

On `origin`, observed again at this invocation (2026-09-29, `main` at `4ad12fe`):

- Branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` is still at `345148b7fce2482349828f897abbc0d7d12fe7fa`; its manifest has 10 entries, all `PASS`; `git diff --name-only 0db3f0ef 345148b` lists only the 19 QA evidence files of checks 1 to 10.
- No remote branch holds any file under `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/`, and no pull request carries a QA-100 result for T11. Collection v1.2's T11 has no stored execution.

In the QA console, as collection v1.2 recorded at its authoring. This Kronos session cannot reach the console, and §4.3 checks each item again before anything runs:

- The QA checkout `/home/nathan/hde-epic040-qa` is on that branch at that commit with a clean working tree; its check 11 directory is absent; `/tmp/hde-epic040-open-rails-showcompat-vendor` is absent; `/tmp/hde-epic040-qa-v1.2/venv` has Python 3.12.3 and an editable install of that checkout.
- `git diff --name-only 0db3f0ef HEAD` in that checkout lists only the 19 QA evidence files of checks 1 to 10, so the product tree there is the tested source `0db3f0ef`.

Collection v1.2 recorded its own authoring dry-run in its §2.4: the PASS path, secret detection, an empty capture and an early stop before the vendor commands. It did not exercise a stop after command 14 had run, or the length of D2's output as the PO would read it.

Dry run of this version (Kronos-23, 2026-09-29; K-04). It tests instruction syntax and flow only. It is not an execution of check 11 and produced no QA evidence, and Kronos made no vendor call, because Glow QA Guide §3.5.7 and HDE CLI/API Vendor Ref §3.7 bar an automated agent from running it.

- Exact vendor argument lists: the text of commands 14 and 15, with only the virtual-environment path changed and the rails closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`), was run through the real `hdctl` of a scratch clone at `345148b7`. Both exited 1 with standard error `PROVIDER_REFUSED` and empty stdout, and wrote no dump: both argument lists parse, and the closed-rails refusal comes before any vendor configuration is read.
- Command blocks: the 45 bash blocks of §5 were extracted mechanically from this file and run in order, in that scratch clone with a Python 3.12.3 virtual environment. Each shell started with an empty environment. The scratch, virtual-environment and checkout paths were substituted; fake key values and a fake base URL replaced `read -rs`; and a stub `hdctl` first on `PATH` emitted only the output shape and logged how it was called. The stub saw `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, the three pins, the three vendor keys `SET`, and `HDAPI_BASE_URL`, `DATABASE_URL`, the three retired bridge keys and `ENGINE_ENV` `UNSET`.
- Seven scenarios, each recorded through C4 with the real `tools.qa.qa_harness`:

| Scenario | What happened | Recorded status |
| --- | --- | --- |
| Clean run | D2 printed `1`, `1`, `END`; W2 printed `W2_WRITTEN` | `PASS`, exit 0, 28 commands, 6 evidence artifacts |
| A key value in command 14's stderr, quarantined at D2 | D2 named `c14.err`; Q1 moved it | `FAIL_TOOLING`, 28 commands, 6 evidence artifacts |
| The same, with Q1 missed at D2 | W2 printed `NOT QUARANTINED` and `W2_NOT_WRITTEN` and wrote nothing; after Q1 it wrote | `FAIL_TOOLING`, 28 commands, 6 evidence artifacts |
| Typed refusal `PROVIDER_UNAUTHORIZED` from both vendor commands | Command 17 moved the two empty stdout files | `TOOLING_BLOCKED`, exit 2, 28 commands, 2 evidence artifacts |
| A D1 row wrong (`GEO_API_KEY` unset), stop before any vendor command | Commands 1 to 13, 27 and 28 ran; C1 printed four `absent` lines | `TOOLING_BLOCKED`, exit 0, 15 commands, 2 evidence artifacts |
| Command 15 not run after command 14 | Commands 16 to 28 ran, so the scan covered command 14's output | `TOOLING_BLOCKED`, exit 2, 27 commands, 4 evidence artifacts |
| Scan failure (command 21's exit file set to 2) | W2 listed the six vendor-run files and wrote nothing; Q2 moved them; W2 wrote | `FAIL_TOOLING`, exit 0, 28 commands, 2 evidence artifacts |

- In every scenario the primary log had a 14-key `pf27.step_log_header.v2` header with no empty argv part and all five body sections, and the manifest had 11 entries. No fake key value or base URL appeared in any file outside the quarantine directory, and `git status --porcelain --untracked-files=all` listed only paths on the §4.8 list. In the clean run the two scans printed 87 and 91 `path:count` lines, all of which v1.2's D2 would have shown the PO.
- The scenario with command 15 not run first came out `FAIL_TOOLING` in Kronos's own status evaluator, which had read "one of its two deliverables" across both vendor commands. §4.7 item 1 now names each command's own files, and the scenario gives `TOOLING_BLOCKED`.

### 2.5 Pre-execution assessment

Isis-52 approved exactly Plan v1.2 (review v1.4 `reviewed_plan` SHA-256 equal to the base above). Check 11 is inside the Plan's scope (Plan §2 D10, §3, §10). Its dependencies are satisfied: `d0-discovery` and `ac040-04-09-compat-cli-offline` are recorded `PASS` on the Run B branch and each was `ACCEPT` at QA-110. Every command, flag, entrypoint and input file it uses exists at the tested source (§2.4). No part of the block has a substantive defect that survives faithful normalization.

T11 meets HDE Build Notes 2.33 (v13.4.4): commands 14 and 15 are live HumanDesignAPI calls under `SAFE_MODE=0` and `ALLOW_NETWORK=1`; the inputs are synthetic QA birth tuples only; nothing in the task substitutes a closed-rails, mocked or generated result for them (the authoring dry-run of §2.4 tests instruction syntax only and is not evidence); the retained conditions hold: the Product Owner runs and authorizes the calls, the evidence is secret-safe and presence-only, the request limit is stated in §5, and failures are classified before any is treated as a product failure (§4.7; QA-110).

The repairs of §1.1 leave this assessment unchanged: they correct collection v1.2's packaging of the check, not the check.

One documentation mismatch was observed, which drives no decision: HDE CLI/API Vendor Ref §3.7 lists `HDAPI_BASE_URL` among the CLI vendor smoke's target facts, while the same document's §1, Glow Infrastructure §2.7 and Glow QA Guide §3.5.7 make `HD_API_BASE_URL` canonical and `HDAPI_BASE_URL` a deprecated alias. The Plan already follows the canonical key (Plan §5.2; QA50-F10). T11 records the mismatch as a `DOC_DELTA:` line so that check 12 collects it (Plan §12 markers).

### 2.6 Carried lineage

- Attempt lineage: §4.2.
- `CANON_CONFLICT_REGISTER`: §6, carried unchanged; QA-90 adds no entry.
- PR lineage: Plan v1.2 carries no `PR_RETURN_PHASE`; none is created here.
- Deferred requirements (live Gate readiness; live DB Reader success): Plan §2. They are not checks and have no task.

## 3. Selection reconciliation

The Product Owner's selection "Task: 11" names Plan check 11 by the only numbering the approved Plan defines (Plan §10, §11). It is the selection "Task to run: 11" that collection v1.2 packaged; T11 is the same member, re-issued here only to carry the repairs of §1.1.

| Plan # | `check_id` | Selected | Task | Attempt | Executor | Depends on | State at authoring |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 to 10 | checks 1 to 10 | Earlier selection "Tasks: 1-10" | T01 to T10 in collection v1.1 | 1 each (ruling LR-01) | Q | per Plan §11 | Executed; each `ACCEPT` at QA-110; not re-issued |
| 11 | `open-rails-showcompat-vendor` | Yes | T11 (this version; v1.2's T11 superseded, never executed) | 1 | P runs the commands; Q runs the recording preflight and records | `d0-discovery` PASS, `ac040-04-09-compat-cli-offline` PASS | Ready: both dependencies recorded PASS |
| 12 | `qa-closeout-deliverables` | No | none | not started | Q | every other check recorded | Not selected: NOT RUN |

Counts: 12 Plan checks; 1 selected here; 1 task, attempt 1; 0 conditional; check 12 not selected. The deferred requirements of Plan §2 are not checks and are not counted.

Consequence for the Product Owner and QA-110: check 12 runs only after check 11 is recorded (Plan §11), and QA-120 cannot mark it COVERED until it is selected and executed (Glow QA Guide §9.2.15.5). The QA checkout, the virtual environment and the Run B branch must be kept for it.

## 4. Common execution contract

### 4.1 Executors, delegation and venue (Plan §6, §7.1, §12; review v1.4 N-103)

Delegation record:

- **Vendor commands (commands 4 to 28): Nathan, the Product Owner, in person.** Plan §7.1 assigns check 11 to the PO only, and Glow QA Guide §3.5.7 bars an automated agent from executing the vendor call or handling a plaintext secret. The PO runs these commands in a bash terminal on the QA console and composes no program: every command is given below.
- **Recording preflight, check commands 1 to 3, and the recording (Plan §12 items 1, 3 and 4): the QA/infra executor.** It is the operator session in which the Product Owner runs QA-100 — Execute Bounded QA Task — 091426.1 with the handoff of this collection. It acts in the repository's QA/Verifier role (`AGENTS.md`). It is neither the Product Owner nor Kronos. Its execution identity is PENDING at QA-90, because the session does not exist yet; it writes that identity to `/tmp/hde-epic040-open-rails-showcompat-vendor/recorder_identity.txt` (§5 Part A) and the QA-100 result records it. If no identity can be recorded, T11 does not run (Plan §6).
- The executor never runs a vendor command, never reads, sets or prints `HD_API_KEY`, `GEO_API_KEY` or `HD_API_BASE_URL`, and reads no file the PO produced until C1 shows that W2 wrote the body, which W2 does only after commands 21 and 22 found no key value or every file they named was quarantined (§5 Part C, C1; N-33). It never reads a quarantined file. Its own commands run under the closed posture.
- Delegating act: the Product Owner's selection of check 11 ("Task to run: 11", repeated as "Task: 11") and the Product Owner opening that QA-100 session with this collection's handoff. This record creates no authority beyond it.
- **Venue (LR-01 item 6):** the Product Owner-controlled Linux shell where checks 1 to 10 ran (Run B). Both the PO's terminal and the executor work in the one QA checkout `/home/nathan/hde-epic040-qa`, from its root, and share the scratch directory `/tmp/hde-epic040-open-rails-showcompat-vendor`. This is not production and not a deployed service (Glow QA Guide §3.5.5; Plan front matter "Target environment").

### 4.2 Attempts (Plan §7.3; review v1.4 N-104; ruling LR-01)

- T11 is attempt 1 of check 11 under Plan v1.2: no execution of check 11 is recorded or stored on any branch (§2.4), and the `06b04a9` executions of Plan v1.0 hold no vendor check. The `06b04a9` attempts are not attempts of T11, as collection v1.1 §4.2 decided for checks 1 to 10.
- Whether an unrecorded execution of check 11 ever took place outside the stored branches is unknown; none is known.
- Collection v1.2 issued T11, which was never executed (§2.4). Issuing this version in its place is authoring, not an attempt (Glow QA Guide §9.2.15.5). If an execution of v1.2's T11 has nevertheless started, §4.3 items 2 and 4 detect it: stop, run nothing from this version, and report to Kronos.
- One ordinary rerun (attempt 2) exists only through Kronos's QA-110 decision and a new QA-90 task, after an attempt 1 that ends `FAIL_TOOLING` or `TOOLING_BLOCKED` from an execution or evidence fault (Plan §7.3; Glow QA Guide §10.6). Task authoring and syntax normalization are not attempts (Glow QA Guide §9.2.15.5). This collection authorizes no rerun and no repeated vendor command.

### 4.3 Setup (executor, before Part A; not check commands)

These read-only checks establish the starting state (K-03). Record each output in the QA-100 result. If any expectation fails, stop, run nothing else, and report.

1. From `/home/nathan/hde-epic040-qa`: `git rev-parse HEAD` prints `345148b7fce2482349828f897abbc0d7d12fe7fa`; `git branch --show-current` prints `qa/hde-epic040-qa100-plan-v1.2-run-20260929`; `git status --porcelain --untracked-files=all` prints nothing.
2. `git fetch origin`, then `git ls-remote --heads origin 'qa/*'`: the branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` is at `345148b7fce2482349828f897abbc0d7d12fe7fa`. Then, for every remote `qa/` branch, `git ls-tree -r --name-only` of `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor` prints nothing. If check 11 evidence exists on any branch, stop and report: another execution exists.
3. `test -e audit/qa/hde-epic040/checks/open-rails-showcompat-vendor` exits 1, and the manifest `audit/qa/hde-epic040/qa_step_logs_manifest.json` has exactly 10 entries.
4. `test -e /tmp/hde-epic040-open-rails-showcompat-vendor` exits 1 (N-101: `body.txt` and `argv.txt` from an earlier attempt must not exist), and so does `test -e /tmp/hde-epic040-open-rails-showcompat-vendor-quarantine`. If either exists, for example from a started execution of collection v1.2's T11, stop and report; do not delete it.
5. `/tmp/hde-epic040-qa-v1.2/venv/bin/python --version` prints `Python 3.12.` and a patch number. If the virtual environment is missing, re-create it exactly as collection v1.1 T01 commands 6 and 7 did (`python3.12 -m venv /tmp/hde-epic040-qa-v1.2/venv`, then its `python -m pip install -r requirements.txt -r requirements-dev.txt -e .` from the checkout root) and record the installed versions of Flask, gunicorn, pytest, jsonschema and psycopg. That is setup, not a check command.
6. Storage authorization: ask the Product Owner now, before Part A, for the instruction to store the evidence of §4.8 (branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, files under `audit/`, one pushed commit, no pull request). Record the answer in the QA-100 result.
7. `mkdir -p /tmp/hde-epic040-open-rails-showcompat-vendor` (Plan §12 item 1).

### 4.4 Rails prefixes (Plan §5.2; N-21)

Two literal prefixes, written in full in each command:

- CLOSED prefix, the executor's check commands 1 to 3 and the recording: `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`
- VENDOR prefix, the PO's commands 4 to 26 (the CLI-local vendor posture for the whole check): `env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`

The VENDOR prefix opens rails for its own command only; the PO's shell keeps its own settings, so no command outside check 11 can run with open rails. `HD_API_BASE_URL`, `HD_API_KEY` and `GEO_API_KEY` reach the vendor commands from the PO's shell, where the PO sets them in Part B without printing them. Commands 27 and 28 run without a prefix, because they act on and observe the PO's shell.

### 4.5 Capture function and body (Plan §12 items 1 to 3; N-20)

Scratch directory: `/tmp/hde-epic040-open-rails-showcompat-vendor/`, outside the repository and never committed.

Both the PO and the executor record every check command with one shell function, `q11`. Definition (the same text for both; §5 gives it as its own block):

```bash
q11() { Q=/tmp/hde-epic040-open-rails-showcompat-vendor; c=$(cat); printf '%s\n' "$c" >> "$Q/argv.txt"; printf '%s\n' "$c" > "$Q/c$1.argv"; eval "$c" > "${2:-$Q/c$1.out}" 2> "$Q/c$1.err"; echo $? > "$Q/c$1.rc"; printf '[%s] exit=%s :: %s\n' "$1" "$(cat "$Q/c$1.rc")" "$c" >> "$Q/cmds.txt"; printf '[%s] exit=%s\n' "$1" "$(cat "$Q/c$1.rc")"; }
```

`q11 K [stdout-target]` reads one command line from a quoted here-document, appends it to `argv.txt` and writes it to `cK.argv`, runs it with stdout to the target (default `cK.out`), stderr to `cK.err` and its exit code to `cK.rc`, appends `[K] exit=N :: command` to `cmds.txt`, and prints `[K] exit=N` on the terminal. Because the here-document delimiter is quoted, the command line is recorded exactly as run, with no expansion. The function evaluates no predicate; it is `/tmp`-level capture glue (Glow QA Guide §3.4.8, §3.4.10), the form QA-110 accepted as D-07. An executor whose shell does not keep functions between invocations defines `q11` in the same invocation as each of its commands.

`argv.txt` holds the check commands actually run, in order, and only those: 28 when none is skipped. The following are not check commands and are not in `argv.txt` (K-04): the setup of §4.3, the PO's session setup in Part B, the display commands D1 and D2, the quarantine commands Q1 and Q2, the body writers W1 to W4, the executor's gate read C1, the status and provenance files of C3, the recording invocation C4, the verification C5 and the storage steps of §4.8.

`body.txt` receives the Plan §8 sections in order, each by redirection from captures, never typed: `=== CONTEXT ===` (W1, executor, before the PO starts: it records the recording preflight's exit code and output, Plan §12 item 1); `=== COMMANDS ===` and `=== OUTPUT ===` (W2, PO, after command 28: every command with its exit code, stdout and stderr, and `vendor_request.txt`, written only when the scan gate holds, N-33); `=== PREDICATES ===` (W3, executor: observed values; then the executor's result line for each [E] predicate, the [K] predicates as `pending QA-110`, and the two-layer statement); `=== LIMITS ===` (W4, executor: proof class, exercised versus inferred, nonclaims and the `DOC_DELTA:` line). The stderr of the two vendor runs enters the body only in W2, after the secret scan and any quarantine (Plan check 11 command 6). W2 refuses to write while a file a scan named is still in place, or while any vendor-run file is in place after a failed or missing scan (N-33).

### 4.6 Stop rules (Plan check 11; Plan §7.5, §12 item 5)

- **Before any vendor command:** after command 13, the PO runs display D1. If any value differs from its expectation, or the executor reported that the recording preflight failed, the PO runs no vendor command: skip commands 14 to 26, run 27 and 28, then W2, and tell the executor where the check stopped. The check is then `TOOLING_BLOCKED` (Plan: "If the preflight fails, the check is TOOLING_BLOCKED and no behavior command runs").
- **The vendor commands 14 and 15 run exactly once each, exactly as written, whatever the exit code of command 14.** A vendor command that cannot be run as written is not changed and not run (Glow QA Guide §3.3: no command changed by guesswork):
  - If command 14 cannot be run as written, run neither vendor command. No vendor output exists: go to command 27, as for a stop before any vendor command.
  - If command 15 cannot be run as written after command 14 has run, do not run it; continue with command 16 and run every remaining command in order. The secret scan (commands 21 and 22) must cover command 14's output while the keys are still set, before command 27 unsets them (N-34).
  - Tell the executor which vendor command was not run and why. The check is then `TOOLING_BLOCKED` (§4.7), unless the scan finds a key value.
- **Secret found or scan failed (commands 21 and 22).** After command 22 the PO runs display D2 (N-32). It prints the two scan exit codes, any `path:count` line whose count is not 0, and `END`. Expected exactly `1`, `1`, `END`. Anything else is dealt with before any other command runs:
  - For any `path:count` line, run Q1 (Part B). It moves every file the scans named into `/tmp/hde-epic040-open-rails-showcompat-vendor-quarantine/` and prints each one.
  - For an exit code of 2 (the scan failed, so its counts cannot be trusted), run Q2 (Part B). It moves the six vendor-run files, `c14.err` and `c15.err` in the scratch directory and the four JSON deliverables, into the same directory.

  Then continue with command 23. The check is `FAIL_TOOLING`, recorded from the files that remain (Plan §12 item 5). A quarantined file is never committed. If `body.txt` or `argv.txt` is named, Q1 quarantines it too, and the executor does not record: it reports the failure signature to Kronos, who records the check at QA-110. W2 enforces this gate (N-33): if it prints `W2_NOT_WRITTEN`, it has written nothing; run Q1 or Q2 for the files it lists, then run W2 again.
- **Operator error:** if a command other than 14 or 15 is mistyped, tell the executor. The repeat is recorded with both executions in `argv.txt` and `cmds.txt` and the reason in the QA-100 result. It is not an attempt.
- **Recording failure:** if the recording invocation C4 exits non-zero, the executor keeps every file, stops, and reports the failure signature to Kronos, who records the check `FAIL_TOOLING` at QA-110 (Plan §12 item 4). No status is inferred.
- **Restore always:** whatever happens, commands 27 and 28 end the PO's check commands, after the secret scan whenever a vendor command has run (Plan check 11 command 9; Plan §7.5).

### 4.7 Status (Plan check 11; Plan Templates causal precedence; N-31)

The executor determines the step-log status from the [E] predicates of §5 Part C, C2, in this precedence:

1. `FAIL_TOOLING`: a secret value was found (E7 count not 0), or a scan exited 2 (scan malfunction), or a vendor command ran and a scan did not; the executed vendor argv differs from the command recorded before execution (E4 after commands 14 and 15 ran: a command changed); a vendor command exited 0 but its own stdout file or Reader dump is absent or was moved as empty (an evidence file missing after an attempted run; the files of a vendor command that did not run do not count); or the recording fails after its preflight passed (then Kronos records it, §4.6).
2. `TOOLING_BLOCKED`: E1, E2 or E3 does not hold (the PO then ran no vendor command); a vendor command was not run because it could not be run as written (§4.6; Glow QA Guide §3.3; Plan Templates "Exact status predicates": the check cannot reach its behavior-decisive point); or a vendor command exited non-zero and its standard error is a typed refusal caused by rails, configuration, credentials, account or vendor availability: `PROVIDER_REFUSED`, `PROVIDER_NETWORK_BLOCKED` (rails); `PROVIDER_CONFIG_MISSING`, `PROVIDER_CONFIG_INVALID`, `PROVIDER_MISCONFIGURED` (configuration); `PROVIDER_UNAUTHORIZED`, `PROVIDER_FORBIDDEN`, `PROVIDER_SECRETS_UNREADABLE`, `PROVIDER_SECRETS_PARSE_ERROR`, `PROVIDER_SECRETS_DIR_INVALID` (credentials); `PROVIDER_RATE_LIMITED`, `PROVIDER_UNAVAILABLE`, `PROVIDER_NETWORK_ERROR` (account or vendor availability).
3. `FAIL_BEHAVIOR`: E1 to E4 hold, both vendor commands ran, no tooling or secret fault occurred, and E5, E6 or E8 is false: a vendor command exited non-zero with any other standard error (for example `PROVIDER_BAD_RESPONSE`, `PROVIDER_NOT_FOUND`, `PROVIDER_ERROR`, `PROVIDER_INPUT_INVALID`, a compat-boundary token, `STDOUT_MISSING_LF`, `STDOUT_CRLF` or `CLI_UNEXPECTED:`), the two stdout files or the two dumps differ, or a file does not parse. The reason names the command, its exit code and its standard-error line, and states that the cause classification of Glow QA Guide §3.5.7 (vendor contract mismatch, request shaping, response mapping, product implementation defect or QA expectation mismatch) is left to QA-110.
4. `PASS`: E1 to E8 all hold.

The restore line R does not change the status; if it fails, the executor reports it as a deviation. `status_reason` is empty only for `PASS`. The [K] predicates are Kronos's at QA-110 and do not enter the step-log status (Plan §12 two result layers).

### 4.8 Evidence files and commit boundary (Plan §7.2; ruling LR-01 item 6; storage authorization §4.3 item 6)

Evidence storage is not a check and is part of no PASS predicate.

- Where: the existing branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, checked out in the QA checkout, as one new commit on `345148b7fce2482349828f897abbc0d7d12fe7fa`, so that one QA root and one manifest hold checks 1 to 11.
- Permitted files, and nothing else; only those that exist are added, and a missing one is reported, not created: `audit/qa/hde-epic040/qa_step_logs_manifest.json`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json`; `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json`.
- Steps, from the checkout root, after C5:
  1. `git status --porcelain --untracked-files=all` lists exactly the modified manifest and the new files of the check directory. Any other path is reported and not added.
  2. `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` still prints `345148b7fce2482349828f897abbc0d7d12fe7fa`. If not, stop and report.
  3. `git add --` followed by the permitted paths that exist, named one by one.
  4. `git diff --cached --name-only` lists exactly those paths.
  5. `git commit -m "HDE-EPIC040 QA-100: evidence for QA Plan v1.2 check 11, attempt 1; tested source 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d"`, plus any attribution lines the session's own rules require.
  6. `git push origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` (a fast-forward), retried on a network error only.
  7. `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` prints the local `HEAD`; each pushed blob's SHA-256 equals the digest recorded by command 20 or C5.
- Never committed: anything in the scratch or quarantine directories; any file holding a secret value, a non-synthetic identifier or a BodyGraph payload; any product, test, tool, schema, catalog, CI, Index, Mirror, PF or `docs/` file.
- Not done: no force-push, rebase, merge or amend; no pull request by the executor. The Product Owner decides any pull request and merge. Run A's branch stays untouched and is never merged as the QA root (LR-01 item 6).
- The QA-100 result record under `docs/ephemeral/` is QA-100's own output, stored under its own working-branch rule from a checkout other than the QA checkout, so that the QA checkout stays as check 12 needs it.

### 4.9 Cleanup and recovery (Plan §7.5)

- Commands 27 and 28 unset the vendor keys in the PO's shell and confirm it. The PO may also close that terminal.
- Keep the QA checkout, the virtual environment, the scratch directory and any quarantine directory after T11. Check 12 runs in this checkout (Plan §7.1). Nothing is deleted.
- No command connects to a database or changes database state, so no database recovery exists.

### 4.10 Normalizations (Plan §12; Glow QA Guide §3.4.7, §3.4.10; QA-90 Execute step 5)

Each clarifies an unchanged Plan operation and changes no objective, proof target, rails posture, evidence identity or predicate. `provenance.txt` lists them.

| ID | Plan locus | Normalization | Reason |
| --- | --- | --- | --- |
| N-02, N-03, N-05, N-06 | As in collection v1.1 §4.9 | Virtual environment `/tmp/hde-epic040-qa-v1.2/venv` first on `PATH`; R2 prints `sys.executable`; the dependency status is read from `python -m json.tool` of the manifest; a compound command is one `sh -c` argv | Carried unchanged |
| N-20 | §12 item 2 (`body.txt` and `argv.txt` kept by redirection) | The capture function `q11` and the writers W1 to W4 (§4.5) | Every executed argv is recorded exactly as run, and the body is composed only from captures |
| N-21 | §5.2 postures; §12 items 1 and 3 (the executor's invocations under the closed posture) | The CLOSED and VENDOR prefixes of §4.4, applied per command | Identical rails on every command, and no open rails outside check 11 |
| N-22 | Check 11 command 0 ("confirm that `body.txt` records the QA/infra executor's recording preflight") | Command 4 counts the two CONTEXT lines W1 wrote from command 3's captures (expected 2) | A baseline count of a recorded value |
| N-23 | Check 11 command 0 (readiness line) | Commands 5 to 7; command 7 reports a key as `SET` only when it is set and non-empty | An empty key value would make the secret scan match every line |
| N-24 | Check 11 command 1 (preflight matrix) | Commands 7 to 11 and the content of `vendor_request.txt` (command 13): posture and presence counted with `grep -c -x -F` (expected 15); the ten recorded statuses counted in the manifest (expected 10, which includes `d0-discovery` and `ac040-04-09-compat-cli-offline`); the manifest digest; the Plan and task identity, authorization reference, tuple provenance and exact commands in `vendor_request.txt` | Each row becomes a baseline value compared with a literal expectation |
| N-25 | Check 11 command 1 ("the exact two commands") and `FAIL_TOOLING` ("a command was changed by guesswork") | Command 16 counts how many of the two executed vendor argv lines appear exactly in `vendor_request.txt`, written before they ran (expected 2) | Proves "the exact command runs" (Glow QA Guide §3.3) mechanically |
| N-26 | Glow QA Guide §4.4.4 (a planned artifact that is not produced is absent, not zero bytes) | Command 17 moves a zero-byte deliverable to the scratch directory, never deletes it, and prints each deliverable's size | A failed run leaves an empty stdout file behind its redirection |
| N-27 | Check 11 command 6 (secret scan) | The value is read from standard input (review v1.4 N-102); the scan is recursive over the check directory and the whole scratch directory, a superset of the Plan's list (every check-directory file, both stderr captures, `body.txt` as it stands), and excludes only the scan's own capture files; one command per key; expected every count 0 and exit 1 | Keeps the value off every process argument list while covering every file that can enter the evidence |
| N-28 | Check 11 command 9 ("restore the closed posture and unset the vendor keys") | Command 27 unsets the keys in the PO's shell; command 28 confirms them `UNSET`. The shell's own rails were never opened (N-21) | The restore is recorded, not assumed |
| N-29 | §12 item 3 (`captured_env` "given explicitly with the values the body file records for the check's decisive commands") | `captured_env.txt` holds command 7's six posture lines; if command 7 did not run, the closed values of commands 1 to 3 | The harness would otherwise record the recording process's closed posture |
| N-30 | §12 item 3 (`evidence_artifacts` "the block's deliverable paths") | Only the deliverables that exist at recording; the harness adds the primary log itself | A missing deliverable is reported in the status, never listed as present |
| N-31 | Check 11 status conditions | The status rules of §4.7, with the typed refusal codes the CLI actually emits (§2.4) | Makes the rails, configuration, credential and availability classes of `TOOLING_BLOCKED` mechanical |
| N-32 | Check 11 command 6 ("Expected 0 everywhere") | D2 prints only the two scan exit codes, the `path:count` lines whose count is not 0, and `END`. Q1 quarantines exactly the files the scans named; Q2 quarantines the six vendor-run files after a failed scan | The PO checks three expected lines instead of every scanned file, and quarantine moves exactly the named files |
| N-33 | Check 11 command 6 ("The stderr text of both runs is then added to the body") | W2 writes only when no file a scan named is still in place, no vendor-run file is in place after a failed or missing scan, and `body.txt` exists. Otherwise it writes nothing and prints `W2_NOT_WRITTEN` with the files concerned | The stderr enters the body only after a clean scan or a quarantine, checked mechanically |
| N-34 | Check 11 command 9 ("This ends the check"); the check's `FAIL_TOOLING` and `TOOLING_BLOCKED` conditions | Once command 14 has run, commands 16 to 28 all run in order, so the scan comes before the restore (§4.6). A vendor command not run because it could not be run as written is `TOOLING_BLOCKED` (§4.7) | The restore unsets the keys the scan reads; the status follows Glow QA Guide §3.3 and Plan Templates "Exact status predicates" |
| N-35 | Part C, the executor's first read (§4.1) | C1 prints the exit files of both vendor commands and both scans, the `path:count` lines whose count is not 0, and the number of W2 section lines in `body.txt`, and states when the executor stops without recording | The executor's first read is mechanical and never reads a file that a scan named |

### 4.11 Return to QA-110

QA-100 returns one `QA_EXECUTION_RESULT` for T11 to QA-110 — Review QA Evidence and Route the Next Action — 091426.1, in the continuing Kronos-23 session. It gives: task, `check_id`, attempt 1, the step-log status and reason as recorded, the final decisive command's exit code, the primary-log path, the deliverables with their SHA-256 values, the normalizations applied, deviations (including any operator-error repeat, quarantine or recording failure), the setup observations of §4.3, the storage authorization, residual state and the resume point; plus the executor identity, the checkout `HEAD` at execution, the evidence branch and its pushed commit. QA-110 evaluates K1 to K3, forms the per-task result, classifies any vendor failure under Glow QA Guide §3.5.7, dispositions any fault and decides any attempt 2.

## 5. Task T11 `open-rails-showcompat-vendor` — Bounded open-rails vendor step

- Plan block: CHECK 11 (Plan v1.2 L783 to L823). Class 3, vendor-focused; the whole PO Live QA subset. D10; PO Q-2; PF05 §7.3.9; AC040-04 and AC040-09 (vendor-backed functional proof of the CLI, resolver, core and emitter). PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §7.3.9; PF19-Canon-Glow-QA-Guide §3.3, §3.5.7; PF07-Canon-Glow-Infrastructure §2.7.
- Change HDE-EPIC040 (Epic); approved Plan `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`; approving review `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`; QA Audit `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`; attempt 1 (§4.2); tokens `[]`.
- Dependencies: `d0-discovery` PASS and `ac040-04-09-compat-cli-offline` PASS, both recorded on the Run B branch.
- Environment and target: the QA console of §4.1, checkout `/home/nathan/hde-epic040-qa`; the CLI-local vendor smoke target of Glow Infrastructure §2.7 (`hdctl showcompat`, `--source vendor`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `APP_ENV=dev`); HumanDesignAPI through `HD_API_BASE_URL`. No database, no deployed service, not production.
- Proof class: vendor-backed no-user behavior (birth-only). Allowed inputs: `--source vendor` and the six birth flags. Forbidden: `--user-a`, `--user-b`, `--source db`, `--source auto`, any app user identifier or `person_uid`, DB-backed BodyGraphs as input, inline secret values, `--dump-admin-dir`, `--conjunction`.
- Inputs: birth tuples A (`1999-10-16`, `04:37`, `Santiago, Chile`) and B (`1978-06-17`, `02:35`, `Tallinn, Estonia`), the QA Audit L-51 default, synthetic QA tuples as decided by the QA-70 review v1.1 (QA50-S01). The Product Owner named no other tuples. The PO's three vendor keys, set in Part B.
- Outputs (QA-created, in `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/`): `vendor_request.txt`, `vendor_run_ab.json`, `vendor_run_ba.json`, `reader_v1_ab.json`, `reader_v1_ba.json`; the primary log `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log` and its manifest entry, written by the recording.
- Final decisive command: command 26 (`python -m json.tool` on `reader_v1_ba.json`); `final.rc` is its exit code.
- Request limit (HDE Build Notes 2.33; Glow QA Guide §3.5.7): exactly two CLI invocations, commands 14 and 15, each run once. Each resolves two birth tuples, one vendor chart request per tuple, and the vendor client makes at most 3 attempts per request, retrying only after a 5xx response or a transport failure, so a 429 is not retried (`engine/bodygraph/vendor_client.py`, `max_attempts=3`, `_is_retryable_error_class`). At most 12 HTTP requests to HumanDesignAPI in total; normally 4. No load, stress or repeated call.

Each command below is complete in its own block (K-02). A block that starts `q11` is three lines: the `q11` line, the command, and `EOF`; paste all three together. After each `q11` block the terminal shows `[K] exit=N`.

### Part A — executor, before the PO starts

After §4.3 setup. The executor records its identity, one line, in the form of this example (the QA-100 Run B identity), with its own values:

```bash
printf '%s\n' 'Claude Code local VS Code session fd43ebfd-1614-44e1-8ee5-6d03da21b70a, QA/infra executor delegated by the Product Owner' > /tmp/hde-epic040-open-rails-showcompat-vendor/recorder_identity.txt
```

Define the capture function:

```bash
q11() { Q=/tmp/hde-epic040-open-rails-showcompat-vendor; c=$(cat); printf '%s\n' "$c" >> "$Q/argv.txt"; printf '%s\n' "$c" > "$Q/c$1.argv"; eval "$c" > "${2:-$Q/c$1.out}" 2> "$Q/c$1.err"; echo $? > "$Q/c$1.rc"; printf '[%s] exit=%s :: %s\n' "$1" "$(cat "$Q/c$1.rc")" "$c" >> "$Q/cmds.txt"; printf '[%s] exit=%s\n' "$1" "$(cat "$Q/c$1.rc")"; }
```

**1.** Checkout `HEAD`, for attribution only (Glow QA Guide §3.4.9). Expected `345148b7fce2482349828f897abbc0d7d12fe7fa`.

```bash
q11 1 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git rev-parse HEAD
EOF
```

**2.** Files that differ from the tested source, for attribution only. Expected: the 19 QA evidence files of checks 1 to 10, all under `audit/`, so the product tree is `0db3f0ef`.

```bash
q11 2 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git diff --name-only 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d HEAD
EOF
```

**3.** Recording preflight (Plan §12 item 1): imports the recording API, constructs the configuration and a not-executed `TOOLING_BLOCKED` result for this check, and prints the QA root. It writes nothing. Expected: exit 0 and `/home/nathan/hde-epic040-qa/audit/qa/hde-epic040`.

```bash
q11 3 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; c=HarnessConfig('HDE-EPIC040', Path.cwd()); r=CheckResult(check_id='open-rails-showcompat-vendor', check_name='Bounded open-rails vendor step', status=Status.TOOLING_BLOCKED, status_reason='recording preflight only, nothing is recorded', command=(), command_provenance='Not executed', exit_code=None, output='recording preflight', evidence_artifacts=(), intended_tokens=(), pf_refs=('PF05-Canon-HDE-CLI-API-Vendor-Ref', 'PF19-Canon-Glow-QA-Guide', 'PF07-Canon-Glow-Infrastructure'), captured_env=()); print(c.qa_root)"
EOF
```

**W1.** CONTEXT section (writer, not a check command):

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; { printf "=== CONTEXT ===\n"; printf "TASK: T11 of docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md; QA Plan v1.2 CHECK 11 open-rails-showcompat-vendor (docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md); attempt 1\n"; printf "VENDOR_COMMAND_EXECUTOR: Nathan (Product Owner), PO-only, commands 4 to 28\n"; printf "RECORDER: "; cat "$Q/recorder_identity.txt"; printf "VENUE: Product Owner-controlled Linux shell, the venue of checks 1 to 10 (Run B)\n"; printf "CHECKOUT: %s\n" "$(pwd)"; printf "CHECKOUT_HEAD: "; cat "$Q/c1.out"; printf "RECORDING_PREFLIGHT_EXIT: "; cat "$Q/c3.rc"; printf "RECORDING_PREFLIGHT_OUTPUT: "; cat "$Q/c3.out"; } >> "$Q/body.txt"'
```

If command 3 did not exit 0 or did not print the QA root, the check is `TOOLING_BLOCKED` and no behavior command runs: tell the PO not to start Part B and go to Part C. If the harness import itself failed, recording cannot run: report the failure signature to Kronos instead (§4.6). Otherwise tell the PO that Part B may start.

### Part B — the Product Owner

Session setup (not check commands). Open a bash terminal on the QA console and go to the checkout:

```bash
cd /home/nathan/hde-epic040-qa
```

Set the three vendor keys from your own store without printing them. Each `read -rs` waits silently for one pasted value and Enter; nothing is echoed or saved in the history. Skip a line if that key is already set in this terminal.

```bash
read -rs HD_API_BASE_URL && export HD_API_BASE_URL
```

```bash
read -rs HD_API_KEY && export HD_API_KEY
```

```bash
read -rs GEO_API_KEY && export GEO_API_KEY
```

Define the capture function:

```bash
q11() { Q=/tmp/hde-epic040-open-rails-showcompat-vendor; c=$(cat); printf '%s\n' "$c" >> "$Q/argv.txt"; printf '%s\n' "$c" > "$Q/c$1.argv"; eval "$c" > "${2:-$Q/c$1.out}" 2> "$Q/c$1.err"; echo $? > "$Q/c$1.rc"; printf '[%s] exit=%s :: %s\n' "$1" "$(cat "$Q/c$1.rc")" "$c" >> "$Q/cmds.txt"; printf '[%s] exit=%s\n' "$1" "$(cat "$Q/c$1.rc")"; }
```

**4.** Confirm that `body.txt` records the executor's recording preflight (Plan check 11 command 0; N-22). Expected stdout `2`.

```bash
q11 4 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -E '^RECORDING_PREFLIGHT_(EXIT: 0|OUTPUT: /.*/audit/qa/hde-epic040)$' /tmp/hde-epic040-open-rails-showcompat-vendor/body.txt
EOF
```

**5.** Readiness R1. Expected `Python 3.12.` and a patch number.

```bash
q11 5 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python --version
EOF
```

**6.** Readiness R2. Expected exit 0 and `/tmp/hde-epic040-qa-v1.2/venv/bin/python`.

```bash
q11 6 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import sys, tools.qa.qa_harness, engine; print(sys.executable)"
EOF
```

**7.** Readiness R3 under the vendor posture: the six posture values, and each key as `SET`, `EMPTY` or `UNSET`, never its value (N-23).

```bash
q11 7 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'for k in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do echo "$k=$(printenv "$k")"; done; for k in HD_API_BASE_URL HD_API_KEY GEO_API_KEY HDAPI_BASE_URL DATABASE_URL DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV; do if [ -n "$(printenv "$k")" ]; then echo "$k=SET"; elif printenv "$k" > /dev/null; then echo "$k=EMPTY"; else echo "$k=UNSET"; fi; done'
EOF
```

**8.** Preflight rows for posture and presence (N-24). Expected stdout `15`.

```bash
q11 8 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -x -F -e SAFE_MODE=0 -e ALLOW_NETWORK=1 -e APP_ENV=dev -e LC_ALL=C -e LANG=C -e TZ=UTC -e HD_API_BASE_URL=SET -e HD_API_KEY=SET -e GEO_API_KEY=SET -e HDAPI_BASE_URL=UNSET -e DATABASE_URL=UNSET -e DB_BRIDGE_URL=UNSET -e DB_FORCE_BRIDGE=UNSET -e DB_ALLOW_BRIDGE_IN_PROD=UNSET -e ENGINE_ENV=UNSET /tmp/hde-epic040-open-rails-showcompat-vendor/c7.out
EOF
```

**9.** Dependency statuses: the manifest as recorded (N-05).

```bash
q11 9 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/qa_step_logs_manifest.json
EOF
```

**10.** Every recorded check is `PASS`, including `d0-discovery` and `ac040-04-09-compat-cli-offline` (N-24). Expected stdout `10`.

```bash
q11 10 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -F '"status": "PASS"' /tmp/hde-epic040-open-rails-showcompat-vendor/c9.out
EOF
```

**11.** Release binding for QA-110 (Plan check 11 command 1). Expected exit 0 and `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96  catalog/manifest.json`.

```bash
q11 11 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sha256sum catalog/manifest.json
EOF
```

**12.** Create the check directory (Plan check 11 command 2). Expected exit 0.

```bash
q11 12 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC mkdir -p audit/qa/hde-epic040/checks/open-rails-showcompat-vendor
EOF
```

**13.** Write `vendor_request.txt` (Plan check 11 command 2): identity, authorization reference, target, tuples, posture and presence, time, and the exact two vendor commands, with no secret value. Expected exit 0.

```bash
q11 13 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c '{ printf "check_id: open-rails-showcompat-vendor\n"; printf "plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md, CHECK 11\n"; printf "task: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md, T11, attempt 1\n"; printf "executor: Nathan (Product Owner), PO-only execution of the vendor commands\n"; printf "authorization: Product Owner selection of QA Plan v1.2 check 11 at the QA-90 invocation of 2026-09-29, and the Product Owner running this task; PO disposition Q-2 (docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md)\n"; printf "target: CLI-local vendor smoke, hdctl showcompat --source vendor, local process, APP_ENV=dev, not production\n"; printf "tuple_provenance: QA Audit L-51 default, audit/ops/hde-epic030/ops-02/vendor_command.txt, equal to audit/ops/hde-epic030/ops-02/sample_birth_inputs.json; synthetic QA tuples (QA50-S01, QA-70 review v1.1)\n"; printf "tuple_a: birthdate 1999-10-16, birthtime 04:37, location Santiago, Chile\n"; printf "tuple_b: birthdate 1978-06-17, birthtime 02:35, location Tallinn, Estonia\n"; for k in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do printf "%s=%s\n" "$k" "$(printenv "$k")"; done; for k in HD_API_BASE_URL HD_API_KEY GEO_API_KEY HDAPI_BASE_URL DATABASE_URL DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV; do if [ -n "$(printenv "$k")" ]; then printf "%s=SET\n" "$k"; else printf "%s=UNSET\n" "$k"; fi; done; printf "time_utc: %s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf "exact_commands, one per line, as they are run (AB, then BA):\n"; printf "%s\n" "$1" "$2"; printf "No secret value is recorded in this file.\n"; } > audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt' sh 'env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC hdctl showcompat --source vendor --birthdate-a 1999-10-16 --birthtime-a 04:37 --location-a "Santiago, Chile" --birthdate-b 1978-06-17 --birthtime-b 02:35 --location-b "Tallinn, Estonia" --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json' 'env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC hdctl showcompat --source vendor --birthdate-a 1978-06-17 --birthtime-a 02:35 --location-a "Tallinn, Estonia" --birthdate-b 1999-10-16 --birthtime-b 04:37 --location-b "Santiago, Chile" --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json'
EOF
```

**D1.** Display (not a check command). Compare every line with the expectation below. If any line differs, follow the stop rule of §4.6: run no vendor command, go to command 27.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; for k in 4 5 6 8 10 11 12 13; do printf "[%s] exit=%s stdout=%s\n" "$k" "$(cat "$Q/c$k.rc")" "$(cat "$Q/c$k.out")"; done'
```

Expected:

- `[4] exit=0 stdout=2`
- `[5] exit=0 stdout=Python 3.12.` followed by a patch number
- `[6] exit=0 stdout=/tmp/hde-epic040-qa-v1.2/venv/bin/python`
- `[8] exit=0 stdout=15`
- `[10] exit=0 stdout=10`
- `[11] exit=0 stdout=52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96  catalog/manifest.json`
- `[12] exit=0 stdout=`
- `[13] exit=0 stdout=`

**14.** AB vendor run (Plan check 11 command 3), stdout to `vendor_run_ab.json`. This calls HumanDesignAPI. Expected exit 0. Run it exactly once, exactly as written.

```bash
q11 14 audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC hdctl showcompat --source vendor --birthdate-a 1999-10-16 --birthtime-a 04:37 --location-a "Santiago, Chile" --birthdate-b 1978-06-17 --birthtime-b 02:35 --location-b "Tallinn, Estonia" --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json
EOF
```

**15.** BA vendor run (Plan check 11 command 4), tuples swapped, stdout to `vendor_run_ba.json`. This calls HumanDesignAPI. Expected exit 0. Run it exactly once, exactly as written, whatever command 14 returned.

```bash
q11 15 audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC hdctl showcompat --source vendor --birthdate-a 1978-06-17 --birthtime-a 02:35 --location-a "Tallinn, Estonia" --birthdate-b 1999-10-16 --birthtime-b 04:37 --location-b "Santiago, Chile" --dump-reader audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json
EOF
```

**16.** The two executed vendor commands equal the lines recorded before they ran (N-25). Expected stdout `2`.

```bash
q11 16 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -x -F -f /tmp/hde-epic040-open-rails-showcompat-vendor/c14.argv -f /tmp/hde-epic040-open-rails-showcompat-vendor/c15.argv audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt
EOF
```

**17.** Capture guard (N-26): prints each deliverable with its size in bytes, and moves a zero-byte one to the scratch directory. Expected four lines, each a file name and a size greater than 0.

```bash
q11 17 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'cd audit/qa/hde-epic040/checks/open-rails-showcompat-vendor && for f in vendor_run_ab.json vendor_run_ba.json reader_v1_ab.json reader_v1_ba.json; do if [ -s "$f" ]; then printf "%s %s\n" "$f" "$(wc -c < "$f")"; elif [ -e "$f" ]; then mv "$f" "/tmp/hde-epic040-open-rails-showcompat-vendor/$f.empty" && printf "%s EMPTY_MOVED\n" "$f"; else printf "%s ABSENT\n" "$f"; fi; done'
EOF
```

**18.** Byte identity of the two stdout files (Plan check 11 command 5). Expected exit 0.

```bash
q11 18 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cmp audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json
EOF
```

**19.** Byte identity of the two Reader dumps (Plan check 11 command 5). Expected exit 0.

```bash
q11 19 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cmp audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json
EOF
```

**20.** SHA-256 of the five deliverables, which binds them to the primary log (Plan §8).

```bash
q11 20 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sha256sum audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json
EOF
```

**21.** Secret scan for the `HD_API_KEY` value (Plan check 11 command 6; N-27). Prints one `path:count` line per file and never the value. Expected: every count `0`, exit 1.

```bash
q11 21 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'printf "%s\n" "$HD_API_KEY" | grep -r -c -F -f - --exclude="c21.*" /tmp/hde-epic040-open-rails-showcompat-vendor audit/qa/hde-epic040/checks/open-rails-showcompat-vendor'
EOF
```

**22.** Secret scan for the `GEO_API_KEY` value. Expected: every count `0`, exit 1.

```bash
q11 22 <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'printf "%s\n" "$GEO_API_KEY" | grep -r -c -F -f - --exclude="c22.*" /tmp/hde-epic040-open-rails-showcompat-vendor audit/qa/hde-epic040/checks/open-rails-showcompat-vendor'
EOF
```

**D2.** Display (not a check command; N-32): the two scan exit codes, then any `path:count` line whose count is not 0, then `END`. It shows paths and numbers only. Expected exactly three lines: `1`, `1`, `END`.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; cat "$Q/c21.rc" "$Q/c22.rc"; grep -h -v -E ":0$" "$Q/c21.out" "$Q/c22.out"; echo END'
```

If D2 shows anything else, act before running any other command (§4.6). A `path:count` line names a file that holds a key value: run Q1, which quarantines every file the scans named and prints `QUARANTINED` and the path for each, then `END`.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; mkdir -p "$Q-quarantine"; for f in $(grep -h -v -E ":0$" "$Q/c21.out" "$Q/c22.out" | sed -e "s/:[0-9]*\$//"); do if [ -e "$f" ]; then mv "$f" "$Q-quarantine/" && printf "QUARANTINED %s\n" "$f"; fi; done; echo END'
```

An exit code of 2 means the scan failed: run Q2, which quarantines the six vendor-run files and prints each one it moves, then `END`.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; D=audit/qa/hde-epic040/checks/open-rails-showcompat-vendor; mkdir -p "$Q-quarantine"; for f in "$Q/c14.err" "$Q/c15.err" "$D/vendor_run_ab.json" "$D/vendor_run_ba.json" "$D/reader_v1_ab.json" "$D/reader_v1_ba.json"; do if [ -e "$f" ]; then mv "$f" "$Q-quarantine/" && printf "QUARANTINED %s\n" "$f"; fi; done; echo END'
```

Q1 and Q2 are not check commands. After either, continue with command 23, and tell the executor what was quarantined.

**23.** Parse check (Plan check 11 command 7), output discarded. Expected exit 0.

```bash
q11 23 /dev/null <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json
EOF
```

**24.** Expected exit 0.

```bash
q11 24 /dev/null <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json
EOF
```

**25.** Expected exit 0.

```bash
q11 25 /dev/null <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json
EOF
```

**26.** Final decisive command. Expected exit 0.

```bash
q11 26 /dev/null <<'EOF'
env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json
EOF
```

**27.** Restore: unset the vendor keys in this shell (Plan check 11 command 9; N-28). Expected exit 0.

```bash
q11 27 <<'EOF'
unset HD_API_KEY GEO_API_KEY HD_API_BASE_URL
EOF
```

**28.** Confirm the restore. Expected `HD_API_KEY=UNSET`, `GEO_API_KEY=UNSET`, `HD_API_BASE_URL=UNSET`.

```bash
q11 28 <<'EOF'
sh -c 'for k in HD_API_KEY GEO_API_KEY HD_API_BASE_URL; do if printenv "$k" > /dev/null; then echo "$k=SET"; else echo "$k=UNSET"; fi; done'
EOF
```

**W2.** COMMANDS and OUTPUT sections (writer, not a check command; N-33). Run it after command 28, as your last step. Expected last line: `W2_WRITTEN`. If it prints `W2_NOT_WRITTEN`, it has written nothing: for a `NOT QUARANTINED:` line run Q1, for a `NOT QUARANTINED (scan` line run Q2, then run W2 again. If it prints `BODY ABSENT`, stop and tell the executor. Then tell the executor that Part B is done, and whether you stopped early, skipped a vendor command or quarantined anything.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; D=audit/qa/hde-epic040/checks/open-rails-showcompat-vendor; ok=1; if [ ! -e "$Q/body.txt" ]; then ok=0; printf "BODY ABSENT\n"; fi; for f in $(grep -h -v -E ":0$" "$Q/c21.out" "$Q/c22.out" 2> /dev/null | sed -e "s/:[0-9]*\$//"); do if [ -e "$f" ]; then ok=0; printf "NOT QUARANTINED: %s\n" "$f"; fi; done; if [ -e "$Q/c14.rc" ] || [ -e "$Q/c15.rc" ]; then for k in 21 22; do s=$(cat "$Q/c$k.rc" 2> /dev/null); if [ "$s" != 0 ] && [ "$s" != 1 ]; then for f in "$Q/c14.err" "$Q/c15.err" "$D/vendor_run_ab.json" "$D/vendor_run_ba.json" "$D/reader_v1_ab.json" "$D/reader_v1_ba.json"; do if [ -e "$f" ]; then ok=0; printf "NOT QUARANTINED (scan %s exit %s): %s\n" "$k" "${s:-missing}" "$f"; fi; done; fi; done; fi; if [ "$ok" = 1 ]; then { printf "=== COMMANDS ===\n"; cat "$Q/cmds.txt"; printf "=== OUTPUT ===\n"; for k in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28; do if [ -e "$Q/c$k.rc" ]; then printf "[%s] exit=%s\n" "$k" "$(cat "$Q/c$k.rc")"; if [ -e "$Q/c$k.out" ]; then printf "[%s] stdout:\n" "$k"; cat "$Q/c$k.out"; else printf "[%s] stdout: written to the file the command names, or discarded\n" "$k"; fi; if [ -e "$Q/c$k.err" ]; then printf "[%s] stderr:\n" "$k"; cat "$Q/c$k.err"; else printf "[%s] stderr: capture absent (quarantined)\n" "$k"; fi; fi; done; printf "vendor_request.txt:\n"; cat audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt 2> /dev/null || printf "(absent)\n"; } >> "$Q/body.txt"; echo W2_WRITTEN; else echo W2_NOT_WRITTEN; fi'
```

### Part C — executor, after the PO

**C1.** Gate, read first and alone (§4.1; N-35). It prints the exit files of both vendor commands and both scans, any `path:count` line whose count is not 0, the number of W2 section lines in `body.txt`, and `END`: names and numbers only.

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; for k in 14 15 21 22; do if [ -e "$Q/c$k.rc" ]; then printf "c%s.rc=%s\n" "$k" "$(cat "$Q/c$k.rc")"; else printf "c%s.rc=absent\n" "$k"; fi; done; grep -h -v -E ":0$" "$Q/c21.out" "$Q/c22.out" 2> /dev/null; grep -c -x -F -e "=== COMMANDS ===" -e "=== OUTPUT ===" "$Q/body.txt"; echo END'
```

Expected after both vendor commands and a clean scan: `c14.rc` and `c15.rc` with the two exit codes, `c21.rc=1`, `c22.rc=1`, `2`, `END`. Expected after a stop before any vendor command: four `absent` lines, `2`, `END`. Then:

- If the line before `END` is not `2`, W2 has not written the body: stop, read nothing else, do not record, and report the failure signature to Kronos, who records the check at QA-110.
- Otherwise W2 has confirmed that no file a scan named, and after a failed or missing scan no vendor-run file, is still in place. A `path:count` line, or a present `c14.rc` or `c15.rc` with `c21.rc` or `c22.rc` absent or neither `0` nor `1`, makes the check `FAIL_TOOLING` (§4.7): confirm with the PO what Q1 or Q2 moved, read nothing that was named, and continue with C2.

**C2.** PREDICATES, observed values (writer W3, first half; not a check command):

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; o() { if [ -e "$Q/c$1.rc" ]; then printf "command %s: exit=%s stdout=%s\n" "$1" "$(cat "$Q/c$1.rc")" "$(if [ -e "$Q/c$1.out" ]; then tr "\n" " " < "$Q/c$1.out"; fi)"; else printf "command %s: not executed\n" "$1"; fi; }; { printf "=== PREDICATES ===\n"; printf "Observed values, from the capture files:\n"; for k in 3 4 5 6 8 10 11 12 13 14 15 16 17 18 19 21 22 23 24 25 26 28; do o "$k"; done; } >> "$Q/body.txt"'
```

Then append one result line per [E] predicate, `PASS` or `FAIL` with the observed value, by `printf` into `body.txt`, in this form and order:

| Line | Predicate (Plan check 11 PASS conditions) | Holds when |
| --- | --- | --- |
| `E1 recording and readiness preflight` | Recording preflight passed and is recorded | command 3 exit 0 and printed a path ending in `/audit/qa/hde-epic040`; command 4 printed `2` |
| `E2 readiness line` | Python 3.12 and the tested install | command 5 printed `Python 3.12.`; command 6 exit 0 and printed `/tmp/hde-epic040-qa-v1.2/venv/bin/python` |
| `E3 preflight matrix` | Every preflight row holds | command 8 printed `15`; command 10 printed `10`; commands 11, 12 and 13 exit 0 |
| `E4 exact commands` | The exact recorded commands ran | command 16 printed `2` |
| `E5 both vendor runs` | Both exit 0 with non-empty stdout and a dump | commands 14 and 15 exit 0; command 17 printed four lines, each a file name and a size greater than 0 |
| `E6 byte identity` | Stdout files identical; dumps identical | commands 18 and 19 exit 0 |
| `E7 secret scan` | Zero occurrences | commands 21 and 22 exit 1 and every count is 0 |
| `E8 parse` | All four files parse | commands 23 to 26 exit 0 |
| `R restore (does not change the status)` | Keys unset in the PO shell | command 28 printed the three `UNSET` lines |

**W4.** The [K] predicates, the two-layer statement and LIMITS (writer; not a check command):

```bash
sh -c 'Q=/tmp/hde-epic040-open-rails-showcompat-vendor; { printf "[K] K1 each stdout is canonical JSON with one final LF and no CR, exactly the keys schema (magic10_compat_result.v1), config_id (m10-channel-state-v1.0.0), release_id (equal to the command 11 digest), pair_key, signals (20) and categories (10, in the order harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance): pending QA-110\n"; printf "[K] K2 each Reader dump has exactly six keys, reader_version v1, categories of one harmony item or empty, no JSON number, and one final LF: pending QA-110\n"; printf "[K] K3 the exercised-versus-inferred statement below matches the captured stderr of commands 14 and 15: pending QA-110\n"; printf "Step-log status attests the execution layer only; [K] predicates are evaluated by Kronos at QA-110.\n"; printf "=== LIMITS ===\n"; printf "Proof class: vendor-backed no-user behavior (birth-only); CLI-local vendor smoke in a local process with APP_ENV=dev; not production and not a deployed service.\n"; printf "Exercised: both birth tuples resolved through HumanDesignAPI, pair evaluated, canonical output and Reader v1 dump emitted.\n"; printf "Inferred, not exercised, unless the captured stderr shows it: the exact vendor resource path, auth-header family and adapter status.\n"; printf "Not exercised: rate-limit and Retry-After handling, typed vendor error mapping, malformed-response handling, v1 legacy guard, mapped-cache persistence, Reader v2 and any deployed service.\n"; printf "Nonclaims: no QA PASS for the change, acceptance, closure, PF09 status change, deployment, token, new public route or flag, broad HumanDesignAPI v2 conformance, or PF edit follows from this result.\n"; printf "DOC_DELTA: PF05-Canon-HDE-CLI-API-Vendor-Ref section 3.7 lists HDAPI_BASE_URL among the target facts of the CLI vendor smoke, while its section 1, PF07-Canon-Glow-Infrastructure section 2.7 and PF19-Canon-Glow-QA-Guide section 3.5.7 make HD_API_BASE_URL canonical and HDAPI_BASE_URL a deprecated alias; this check used HD_API_BASE_URL with HDAPI_BASE_URL unset (QA Plan v1.2 section 5.2). Owner: PF05 maintainer. Documentation drainage only; drives no decision.\n"; } >> "$Q/body.txt"'
```

**C3.** Recording inputs, each written by `printf` or `cp` from the captures:

- `status.txt`: line 1 the status of §4.7; line 2 the causal reason, absent for `PASS`.
- `final.rc`: a copy of `c26.rc`; if command 26 did not run, a copy of the `.rc` file of the last check command that ran.
- `provenance.txt`, one line: `QA Plan v1.2 CHECK 11 open-rails-showcompat-vendor (docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md); QA-90 collection v1.3 task T11 (docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md); attempt 1; commands 4 to 28 executed by Nathan (Product Owner); commands 1 to 3 executed and the check recorded by ` followed by the identity in `recorder_identity.txt`, then `; normalizations: N-02, N-03, N-05, N-06, N-20 to N-35` and any executor normalization, with its reason.
- `captured_env.txt` (N-29): if `c7.out` exists, `grep -E '^(LC_ALL|LANG|TZ|SAFE_MODE|ALLOW_NETWORK|APP_ENV)=' /tmp/hde-epic040-open-rails-showcompat-vendor/c7.out`, stdout to `/tmp/hde-epic040-open-rails-showcompat-vendor/captured_env.txt`; otherwise the six closed values `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, one per line.

**C4.** Recording (Plan §12 items 3 and 4; not a check command and not in `argv.txt`). Expected: exit 0 and two printed paths, the primary log and `audit/qa/hde-epic040/qa_step_logs_manifest.json`.

```bash
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-open-rails-showcompat-vendor'); d='audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/'; st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); env=tuple(tuple(x.split('=', 1)) for x in (s / 'captured_env.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='open-rails-showcompat-vendor', check_name='Bounded open-rails vendor step', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=tuple(d + f for f in ('vendor_request.txt', 'vendor_run_ab.json', 'vendor_run_ba.json', 'reader_v1_ab.json', 'reader_v1_ba.json') if Path(d + f).is_file()), intended_tokens=(), pf_refs=('PF05-Canon-HDE-CLI-API-Vendor-Ref', 'PF19-Canon-Glow-QA-Guide', 'PF07-Canon-Glow-Infrastructure'), captured_env=env); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"
```

**C5.** Verification (not a check command): the manifest parses and has 11 entries; the `open-rails-showcompat-vendor` entry's `status` equals the primary-log header status; the primary log is non-empty, starts with one `pf27.step_log_header.v2` line and ends with one LF; `sha256sum` of the primary log and the manifest, for the QA-100 result. Then store the evidence under §4.8.

**[K] predicates (Kronos at QA-110, from the four JSON files, the command 11 digest and the body; Plan check 11):** K1, K2 and K3 exactly as W4 writes them. A false [K] predicate makes the per-task result `FAIL_BEHAVIOR`, or `FAIL_TOOLING` when a capture is malformed; the cause is classified under Glow QA Guide §3.5.7 before a `FAIL_BEHAVIOR` result stands.

**Nonclaims (Plan check 11, §3):** the step proves live vendor-backed CLI resolution through the HDE-EPIC040 core and emitter, canonical stdout, AB↔BA identity, a bands-only Reader v1 dump and the binding to the admitted release. It does not prove the exact vendor resource path or auth-header family unless the captured stderr shows them, rate-limit, `Retry-After`, typed vendor error, malformed-response or v1-legacy-guard handling, mapped-cache persistence, Reader v2 over HTTP, deployed-service behavior or broad HumanDesignAPI v2 conformance.

## 6. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from Plan v1.2 §2.3, through collection v1.1 §6, QA-110 review v1.0 §9 and collection v1.2 §6. QA-90 adds no entry and changes no field. The PF05 §3.7 key-name mismatch of §2.5 is a documentation delta within one PF title, which the Plan already resolves by following the canonical key; it is not a canon conflict affecting this change's work. C040-09's interim treatment applies to T11: read-only git observations for attribution only, never a PASS gate; the tracked harness API through `python -c`; no script file; no decisive evaluator written at run time. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 and v13.4.4 keep for 2.2 to 2.28. A proposal here is not approval.

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

## 7. Constraints, open inputs and unresolved items

| Item | Owner | Status |
| --- | --- | --- |
| Executor identity (§4.1) | The QA-100 operator session; recorded in Part A | PENDING until that session exists |
| Storage authorization (§4.3 item 6) | Product Owner, asked at the start of the QA-100 session | PENDING |
| The three vendor keys in the PO's terminal | Product Owner | Supplied at execution; never recorded |
| Evidence commit on `qa/hde-epic040-qa100-plan-v1.2-run-20260929` | The QA-100 executor under §4.8 | PENDING until execution; any pull request and merge are the Product Owner's |
| Per-task result, K1 to K3, cause classification of any vendor failure, any attempt 2 | Kronos-23 at QA-110 | After QA-100 |
| Selection of check 12 `qa-closeout-deliverables` | Product Owner, through a later QA-90 | Not selected; NOT RUN; runs after check 11 is recorded |
| `DOC_DELTA` on PF05 §3.7 key name (§2.5) | PF05 maintainer, through check 12's doc-delta append and QA-120 | Documentation only; drives no decision |
| Run A's T03 outcome and T10 receipt (QA-110 review v1.0 LR-01 item 7) | Product Owner | Open, non-gating; unchanged |
| PF10 v13.4.4 on `main` (`4ad12fe`): in addendum 2.28, row RA-06 lost its last two cells (the proposed doc delta and `NO`) because the text `dev\|test\|local` was split into table cells; and the addendum index lists 2.32 but not 2.33 | Product Owner (PF10 publication) | Observed by collection v1.2 in the working-tree copy and confirmed on `main` at this invocation. Neither affects T11; Kronos does not edit the file |
| PF10 v13.4.4 landing on `main` | Product Owner (canon transfer) | Resolved: it landed at `4ad12fe`, byte-identical to the copy collection v1.2 read. T11 needed no change for it beyond the paths of §1.1 V-05 |
| Collection v1.2 and its handoff `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.2.md` | Product Owner | Superseded for T11 by this collection and its handoff; v1.2's T11 is not executed. If an execution under v1.2 has started, §4.2 applies |
| Who may run the vendor call: HDE Governance §3.4 lets a PO-delegated automated session agent execute an authorized HDAPI v2 open-rails call, while Glow QA Guide §3.5.7 and HDE CLI/API Vendor Ref §3.7 bar automated agents from running the vendor call | PF04, PF05 and PF19 maintainers; Product Owner | Observed at this invocation. It does not affect T11: the approved Plan has the Product Owner run the vendor commands, which satisfies every one of these passages. Not entered in the register, because no decision of this change depends on it |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING: no such procedure at `4ad12fe` |

## 8. Working state

| Field | Value |
| --- | --- |
| Stage | QA-90 complete for the selection "Task: 11" (repeated invocation); next QA-100 |
| Collection | This file, v1.3, `TASK_READY` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.3.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.3.md` |
| Resume point for QA-100 | §4.3 setup, then §5 Part A |

## 9. Nonclaims

This collection executes nothing, makes no vendor call and produces no evidence. It establishes no QA PASS, acceptance, closure, PF09 status movement, PF-Canon drainage, PF10 addendum, deployment, release activation, token satisfaction or Index/Mirror publication. Every artifact named in §5 is NOT RUN until T11 executes. It makes no claim for check 12, which is not selected.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-90-20260929-02
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-04 and AC040-09 (vendor-backed part), PO Q-2, as mapped by Plan v1.2 check 11
  - prompt: QA-90 — Create Bounded QA Execution Task — 091426.1; Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-90 (repeated invocation for the selection "Task: 11")
  - capture_time: 2026-09-29T04:51:30Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_TASK_COLLECTION v1.3, TASK_READY, task T11 at attempt 1, repairing collection v1.2 (V-01 to V-05), routed to QA-100
  - task_and_attempt_mapping: T11 `open-rails-showcompat-vendor`, attempt 1; collection v1.2's T11 superseded and never executed; result mapping PENDING until QA-100
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `4ad12fe`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-90-20260929-01 (QA task collection v1.2); GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (QA task collection v1.1); GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (QA-100 execution results v1.1); GCFPE-USE-HDE-EPIC040-QA-110-20260929-01 (QA-110 evidence review v1.0).
