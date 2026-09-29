---
artifact_type: QA_EVIDENCE_REVIEW
artifact_id: HDE-EPIC040-QA110-QA-EVIDENCE-REVIEW-T11
artifact_version: "1.0"
predecessor: none for task T11. docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md holds the review of tasks T01 to T10 (SHA-256 2d45e7f0d252a3009ffb9cc0fe3d51b9652a7929eeb798bd618f2c497ab34ac3) and is not superseded
state: MEMBER_ACCEPT_RUN_INCOMPLETE
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-110 / QA task collection v1.3 task T11 against QA-100 execution result T11 v1.0
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-110 — Review QA Evidence and Route the Next Action — 091426.1 (Notion 3db4590a05eb816984d1d34da0e08f40; page as of 2026-09-24T15:52:32.947Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (APPROVE by Isis-52; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df)
task_collection: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md (task T11, attempt 1; SHA-256 c4ae999f9a38b7bcfabb66ac92ae542a1754682debd17fbd87c18fcc936de16b)
execution_result: docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-t11-v1.0.md (T11 COMPLETE, step-log PASS; SHA-256 0c884e8f6e56fdf959c68ec77860faef60ac1d2899494231745a3594e0dfe397)
execution_checkpoint: docs/ephemeral/HDE-EPIC040-QA100-checkpoint-t11-v1.0.md (SHA-256 60855b9aaf0c2162a2a6c469d665394d9efd524dcd4dee0f7f804c45d0374f2a)
evidence_of_record: branch qa/hde-epic040-qa100-plan-v1.2-run-20260929, commit 380cf46fda95686ccf71f256521e63ca0eb5c9e1 on 345148b7fce2482349828f897abbc0d7d12fe7fa (the Run B stream of ruling LR-01)
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.5.md on main at 633ca5d (SHA-256 aa5ef8812c68b2b107e3da2bbc0c566f399559ab74de076728d350c4fa7860d7; addendum 2.34 read in full)
observed_revision: 633ca5d340110d8058b795c366f6041bd0747929 (origin/main at review; pull request amthorn78/glow-hdengine-v2#551, which carries the QA-100 records for T11, is merged)
routing: QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23), for Plan check 12, which is unissued and has no Product Owner selection recorded
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-110 (QA-110 is not an addendum producer)
---

# HDE-EPIC040 — QA Evidence Review (QA-110): task T11 of QA Plan v1.2, v1.0

## 1. Result

| Field | Value |
| --- | --- |
| Member | T11 `open-rails-showcompat-vendor` (Plan v1.2 check 11), attempt 1, against QA-100 result T11 v1.0 |
| Decision | `ACCEPT`; per-task result `PASS`. Execution layer: step-log `PASS`, every [E] predicate re-verified against the captured output. [K] layer: K1, K2 and K3 evaluated here, all `PASS` (Plan §12, two result layers) |
| Authority for the delegated execution | HDE Build Notes addendum 2.34, PF10-VENDOR-001 (v13.4.5): a directed agent executes live vendor calls, including open-rails HumanDesignAPI calls in QA checks. It names T11, "records the authority for that execution" and leaves the per-task result to this review (§4.3) |
| Escalation | None. No behavior defect, no invalid Plan, no open authority boundary once 2.34 governs, and no code or Ops remediation |
| Scope of the decision | One bounded check. It is not whole-change QA PASS |
| Run state | Checks 1 to 11 `ACCEPT` (review v1.0 for checks 1 to 10; this review for check 11). Check 12 `qa-closeout-deliverables` is unissued and has no Product Owner selection: NOT RUN. The run is incomplete |
| Route | QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23), for check 12 on the Product Owner's selection (§6) |
| Lessons | K-05 and K-06, defects in my collection v1.3 (§5.2). Neither changes this decision |

## Canon relied on

Read from `docs/pfcanon/` on `main` at `633ca5d`. There `docs/pfcanon/` differs from `f4be532`, where the QA-100 session read it, only in that PF10 v13.4.5 replaces v13.4.4.

- **HDE Build Notes v13.4.5** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.5.md`). Its complete difference from v13.4.4 was read at this invocation: the version line; in the index, a line break after the 2.32 entry and new entries for 2.33 and 2.34; and the new addendum 2.34, inserted before the unchanged end marker. So v13.4.5 is v13.4.4 plus addendum 2.34.
  - 2.34 "PF10-VENDOR-001 — Agents Run Live Vendor Calls When the Product Owner Directs; Vendor Configuration Comes from Environment Variables" was read in full: rules 1 to 7, superseded passages, epic and task effects (T11 named), deferred obligations and nonclaims.
  - Whole-document search at this invocation for `QA-110`, `T11`, `check 11`, `open-rails-showcompat-vendor`, `directed agent`, `delegat`, `vendor call`, `evidence review`, `two executions`, `attempt 2`, `per-task result`, `QA-120`, `check 12`, `qa-closeout-deliverables` and `environment variable`. The governing hits are 2.32, 2.33 and 2.34. The other hits set no rule for this review: timestamps containing `T11` in 2.5 to 2.19, an unrelated implementation-task row `T11` in 2.6, a product-code "delegate" in 2.19, a CI attempt in 2.11, a dev capture without a vendor call in 2.23, the OPS01 delegation record in 2.27, and a triage row in 2.28.
  - Relied on: 2.34 (§4.3); 2.33 (synthetic data only, and the retained open-rails conditions); 2.32 (ruling LR-01 item 6, lessons K-01 to K-04, and routing unissued checks to QA-90 on the Product Owner's selection); 2.29 (canon location and change-document storage).
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`), unchanged on `main` since each read:
  - as read at QA-110 v1.0 in this session: §3.1.2, §3.4.7 to §3.4.10, §4.3, §4.4.1 to §4.4.7, §9.2.15.5, §10.6, §10.8, §11.1;
  - as read at QA-90 v1.3 in this session: §3.3 and §3.5.5 to §3.5.7. Their bar on an agent executing the vendor call is superseded for this scope by 2.34.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`):
  - "Execution authority (normative)", read in full at this invocation;
  - "Step-log header schema expectations (required; v2)" and "Proof-class and controlled vendor-smoke boundary (required when applicable)", as read at QA-90 v1.3 in this session. The latter is superseded in part by 2.34.
- **HDE Governance** (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`): §3.4, as read at QA-90 v1.3; §9.1 "Ops tasks", items 1 to 6, read at this invocation.
- **Change Process Guide** (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md`): the "Ops tasks" passage (execution authority, delegation contract, permitted stops, "Ops tasks are not QA tasks"), read in full at this invocation.
- **HDE CLI/API Vendor Ref** (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`): §3.7 and §7.3.9, as read at QA-90 v1.3. §3.7's agent bar is superseded for this scope by 2.34.
- **Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §2.7, as read at QA-90 v1.3.
- **Technical Writing Best Practices** (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`): "Truth and source fidelity", as read at QA-90 v1.1.
- **In-flight documents**:
  - Plan v1.2: front matter, §1 to §8, §10, §11, the §12 common rules and check block 11, as read at QA-90 v1.3 in this session.
  - Review v1.4: execution notes N-101 to N-104.
  - Collection v1.3: authored and read in full in this session, and equal to the pin the QA-100 result verified.
  - QA-100 result T11 v1.0 and checkpoint T11 v1.0: read in full at this invocation.
  - QA-110 review v1.0.
- **Product code read at this invocation for K3**: `engine/cli/main.py` (`showcompat`, `_resolve_party`) and `engine/bodygraph/resolver.py` (`resolve_compat_chart`, `_resolve_stored`, `_acquire_dry_run`).

## 2. Inputs and matches

| Item | Finding |
| --- | --- |
| Task to result | The result names task T11 of collection v1.3, attempt 1, Plan v1.2 check 11. Its pins equal the files on `main`: collection, Plan, review, Audit, QA-110 review v1.0 and PF10 v13.4.4 as read then |
| Environment | The Run B venue that ruling LR-01 item 6 requires: the Product Owner-controlled Linux shell, checkout `/home/nathan/hde-epic040-qa`, virtual environment `/tmp/hde-epic040-qa-v1.2/venv` (Python 3.12.3). Tested source `0db3f0ef`: command 2 lists only the 19 QA evidence files of checks 1 to 10 |
| Dependencies | `d0-discovery` and `ac040-04-09-compat-cli-offline` are `PASS` in the manifest (commands 9 and 10: 10 of 10 `PASS`), and each is `ACCEPT` in review v1.0 |
| Attempt | Attempt 1. No execution of check 11 existed on `origin` before this one (result §3 item 2). The evidence commit is the first commit touching the check 11 directory. No rerun and no operator-error repeat |
| Selected members | Plan v1.2 has 12 checks. Checks 1 to 10 were reviewed in v1.0; check 11 is reviewed here; check 12 is unissued |
| PF10 | The QA-100 session read v13.4.4. This review applies v13.4.5, which adds addendum 2.34 |

## 3. Evidence integrity of commit `380cf46`

The commit and every file were read from `origin` at this invocation.

- **Commit.** `380cf46fda95686ccf71f256521e63ca0eb5c9e1` on parent `345148b7fce2482349828f897abbc0d7d12fe7fa`, 2026-09-29T05:54:18Z. Its message names check 11, attempt 1 and the tested source. It adds 6 paths and modifies the manifest, 7 paths in all, every one on collection v1.3 §4.8's permitted list.
- **Digests.** SHA-256 and byte size of each file equal the result's §7 table:

  | Path | Bytes | SHA-256 |
  | --- | --- | --- |
  | `audit/qa/hde-epic040/qa_step_logs_manifest.json` | 1,836 | `f11fbdbc5a978772cd8ad0847a4341320939fbd17505843ef6426ed2d623bc96` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log` | 64,998 | `1e4341e27e1ce47fe172546581ac4737e2dcb9745f82bac42f0001ac6f5f4674` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt` | 2,312 | `328508d8a020e84d6d74078331c7221233556ee69b389893160057073e92c4a9` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json` | 3,303 | `e33377d7eab26ed1693b6ebbe5166b88cca5c38f300999c94a30db057c1fa564` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json` | 3,303 | `e33377d7eab26ed1693b6ebbe5166b88cca5c38f300999c94a30db057c1fa564` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json` | 330 | `103df389283c7e577ebd78d377eb49fe6b7d014b732389577ea9efbbe1de32d0` |
  | `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json` | 330 | `103df389283c7e577ebd78d377eb49fe6b7d014b732389577ea9efbbe1de32d0` |

- **Manifest.** Valid JSON with sorted keys and 11 entries. The 10 earlier entries are unchanged from `345148b`. The new entry has `check_id` `open-rails-showcompat-vendor`, the full `log_path` of its primary log and `status` `PASS`, equal to the header status (Glow QA Guide §4.4.3).
- **Primary log.** 64,998 bytes, one final LF, no CR (Glow QA Guide §4.4.4 to §4.4.6).
  - Header: `pf27.step_log_header.v2` with 14 keys.
    - `status` `PASS`, empty `status_reason`, `exit_code` 0, which is the exit code of command 26.
    - `command`: 28 argv lists with no empty part.
    - `command_provenance`: names the actual executor of commands 4 to 28, and E-01.
    - `captured_env`: the six vendor-posture values (`SAFE_MODE` 0, `ALLOW_NETWORK` 1, `APP_ENV` dev, `LC_ALL` C, `LANG` C, `TZ` UTC).
    - `evidence_artifacts`: the primary log and the five deliverables.
    - `pf_refs`: the PF05, PF19 and PF07 titles.
    - Both token arrays empty; timestamp 2026-09-29T05:53:32Z.
  - Body: the five sections of Plan §8, in order (CONTEXT, COMMANDS, OUTPUT, PREDICATES, LIMITS). PREDICATES carries an `EXECUTION DEVIATION:` line.
- **Commands.** The 28 recorded argv lists and the 28 COMMANDS lines equal the command lines of collection v1.3 byte for byte, which verifies E-01.
- **`vendor_request.txt`.** 29 lines, equal to its copy in the body. It was written at 05:51:11Z, before the vendor commands started (05:52:14Z, result §1). It records presence only (`SET` or `UNSET`).
- **Secret safety.**
  - Commands 21 and 22 exited 1, with 89 and 93 `path:count` lines, every count 0. D2 printed `1`, `1`, `END`; Q1 and Q2 were not run; no quarantine directory exists.
  - A sweep of the 7 files for token-shaped strings of 32 or more characters (hex digests excluded) found only identifiers.
  - Supplementary check: the values of `HD_API_KEY` and `GEO_API_KEY` held in this Kronos session's own environment were searched in the 7 files through standard input, with counts only. Each was found in 0 of 7 files. This adds assurance only if those are the same keys the QA-100 run used, which is unknown.

## 4. Per-task review: T11 `open-rails-showcompat-vendor` — ACCEPT; per-task result PASS

### 4.1 Execution layer ([E], re-verified against the OUTPUT section)

| Predicate | Observed | Result |
| --- | --- | --- |
| E1 recording and readiness preflight | Command 3 exit 0, printed `/home/nathan/hde-epic040-qa/audit/qa/hde-epic040`; command 4 printed `2` | PASS |
| E2 readiness line | Command 5 `Python 3.12.3`; command 6 exit 0, `/tmp/hde-epic040-qa-v1.2/venv/bin/python` | PASS |
| E3 preflight matrix | Command 8 printed `15` (the posture, and the keys `SET` or `UNSET` as required); command 10 printed `10`; commands 11, 12 and 13 exit 0; command 11 printed `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96  catalog/manifest.json`, the SHA-256 of `catalog/manifest.json` at the tested source | PASS |
| E4 exact commands | Command 16 printed `2` | PASS |
| E5 both vendor runs | Commands 14 and 15 exit 0 with empty stderr; command 17 printed `vendor_run_ab.json 3303`, `vendor_run_ba.json 3303`, `reader_v1_ab.json 330`, `reader_v1_ba.json 330` | PASS |
| E6 byte identity | Commands 18 and 19 exit 0 | PASS |
| E7 secret scan | Commands 21 and 22 exit 1; every count 0 (§3) | PASS |
| E8 parse | Commands 23 to 26 exit 0 | PASS |
| R restore (does not change the status) | Command 28 printed `HD_API_KEY=UNSET`, `GEO_API_KEY=UNSET`, `HD_API_BASE_URL=UNSET` | PASS |

No stop rule was triggered: display D1 matched every expectation, D2 printed `1`, `1`, `END`, W2 printed `W2_WRITTEN`, and C1 printed `c14.rc=0`, `c15.rc=0`, `c21.rc=1`, `c22.rc=1`, `2`, `END`. The request limit held: commands 14 and 15 each ran once, two CLI invocations in all (collection §5). The inputs were the synthetic L-51 tuples (QA50-S01; HDE Build Notes 2.33).

### 4.2 [K] layer (evaluated here, from the four JSON files, the command 11 digest and the body)

- **K1: PASS.** Both `vendor_run_ab.json` and `vendor_run_ba.json` meet every condition:
  - They are canonical JSON: sorted keys, compact separators, one final LF and no CR. Re-serializing with those rules reproduces the stored bytes exactly.
  - They have exactly the keys `categories`, `config_id`, `pair_key`, `release_id`, `schema` and `signals`, with `schema` `magic10_compat_result.v1` and `config_id` `m10-channel-state-v1.0.0`.
  - `release_id` equals the command 11 digest, which is the SHA-256 of `catalog/manifest.json` at the tested source, recomputed here.
  - `pair_key` is a string, `signals` has 20 items, and `categories` has 10 items whose `category_id` values follow the order harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance.
  - The two files are byte-identical (E6).
- **K2: PASS.** Both `reader_v1_ab.json` and `reader_v1_ba.json`:
  - have exactly six keys (`categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version`, `release_id`), with `reader_version` `v1`;
  - have `categories` `[{"band":"Cool","id":"harmony"}]`, one `harmony` item;
  - contain no JSON number at any depth;
  - are 330 bytes, end with one LF and are canonical.
- **K3: PASS.**
  - The captured stderr of commands 14 and 15 is empty. So the LIMITS statement that the exact vendor resource path, auth-header family and adapter status are "inferred, not exercised, unless the captured stderr shows it" is true of this run.
  - The "Exercised" statement also holds. With `--source vendor`, `showcompat` resolves each birth-only party through `resolve_compat_chart` with no local lookup. `_resolve_stored` then reaches `_acquire_dry_run`, the live acquisition through the vendor client (`engine/cli/main.py`; `engine/bodygraph/resolver.py`). Exit 0 under open rails therefore means both tuples were resolved through HumanDesignAPI, the pair was evaluated, and the canonical output and Reader v1 dumps were emitted.

### 4.3 Authority of the delegated execution (D-01)

- **Facts.** Commands 4 to 28, the displays and W2 were executed by the QA-100 session as the Product Owner's delegated agent, on the Product Owner's direction during the session. Plan v1.2 §7.1 and collection v1.3 §4.1 assign them to the Product Owner in person. The vendor configuration came from the environment the Product Owner set (D-02). The command text was taken mechanically from the collection (E-01).
- **Canon at execution (v13.4.4).**
  - Against delegation: Glow QA Guide §3.5.7 and HDE CLI/API Vendor Ref §3.7 barred an automated agent from executing the vendor call.
  - For delegation: HDE Governance §3.4 and §9.1, the Change Process Guide "Ops tasks" passage and Plan Templates "Execution authority (normative)" provide for Product Owner-delegated execution. But they are written for Ops tasks, and the Change Process Guide states "Delegation does not convert Ops into PR work or QA work".
  - Collection v1.3 §7 recorded this tension. No text then in canon authorized a directed agent in a QA check.
- **Canon now (v13.4.5, addendum 2.34).**
  - Scope: 2.34 covers "open-rails HumanDesignAPI calls in QA checks". Under it, an automated session agent executes a live vendor call when the Product Owner directs it, and "PO-only" names the authorizing and accountable principal.
  - Supersession: it supersedes the bars of Glow QA Guide §3.3 and §3.5.7, HDE CLI/API Vendor Ref §3.7 and the other listed passages for that scope.
  - Existing plans: a plan that assigns vendor commands to the Product Owner in person "remains a valid record", and under a Product Owner direction a directed agent executes its commands unchanged.
  - T11: it names T11 and "records the authority for that execution", leaving the per-task result to this review.
  - Reliance on this delta rests on the fresh read of current PF10 recorded under "Canon relied on".
- **Same controls (2.34 rule 3), verified from the evidence:**
  - the exact commands (byte-identical to the collection, §3);
  - the rails per command (VENDOR prefix for commands 4 to 26; CLOSED prefix for commands 1 to 3 and the recording);
  - the request limit (§4.1) and the stop checks (D1, D2, W2's gate, C1);
  - synthetic inputs, secret scan and quarantine (zero findings), presence-only redaction, and the evidence contract (7 files, §3).
- **Secret posture (2.34 rule 6).** Passing the environment to the product process is not handling a plaintext secret. No value was printed, recorded or persisted (§3; result D-01 and D-02).
- **Conclusion.** The delegated execution of T11 is authorized under current PF10, so no scope or authority boundary remains open and no escalation arises. Two fixed-text lines in the evidence still name the Product Owner as executor; that is lesson K-06 (§5.2). The accurate executor is recorded in the header's `command_provenance`, the `EXECUTION DEVIATION:` line, the result's D-01 and addendum 2.34. Governed bytes are not edited (Glow QA Guide §4.3).

### 4.4 Decision

`ACCEPT`, per-task result `PASS`. Both result layers pass, and every task, result, Plan, step, attempt and environment match holds (QA-110 decision rule 2). The decision covers one bounded check: the live vendor-backed CLI resolution of Plan check 11 and its nonclaims (collection v1.3 §5). It is not whole-change QA PASS.

## 5. Deviations and defects

### 5.1 Dispositions of the QA-100 deviations

| ID | Disposition |
| --- | --- |
| D-01 | Accepted under HDE Build Notes 2.34 (§4.3). The same controls were applied unchanged |
| D-02 | Accepted. The environment held `HD_API_KEY`, `GEO_API_KEY` and `HD_API_BASE_URL` once the Product Owner set them, and `HDAPI_BASE_URL` was unset. The `read -rs` lines were skipped, as collection §5 Part B allows. This matches 2.34 rules 4 and 5: vendor configuration comes from the environment, and the Product Owner does not re-enter values. `DATABASE_URL` was removed from every vendor command by the VENDOR prefix (command 7) |
| D-03 | Accepted. Command 27 unset the keys in the shell that ran commands 23 to 28, and command 28 confirmed it. Later shells regain them from the environment the Product Owner configured. The closed posture of every later command comes from the CLOSED prefix, which unsets the nine names per command (Plan §5.2, §7.5). Constraint carried to check 12 (§6) |
| D-04 | Accepted. Evidence storage is not a check (Plan §7.2). The identity of the Run B commit was passed with `git -c` for one command, and no configuration was changed |
| D-05 | Accepted. These are `/tmp` helper files (Glow QA Guide §3.4.8), not evidence and not committed; `.c13_src` was present during the scans and scanned 0 |
| D-06 | Confirmed as a defect of my collection v1.3: K-05 (§5.2). No effect on the execution |
| D-07 | Noted. Plan v1.2 §5.2 unsets `HDAPI_BASE_URL` in the CLI-local vendor posture. Addendum 2.34 rule 5 now says "A rails posture does not remove the only base URL the environment holds", so for any later vendor task under Plan v1.2 whose environment holds only the alias, 2.34 governs. No effect on T11, where `HD_API_BASE_URL` was set. No vendor task remains in Plan v1.2. Carried to the QA-120 RCA |
| D-08 | Noted. `.env.example` lacks `GEO_API_KEY`. This is documentation drift, recorded by 2.34 as a deferred obligation owned by the implementation lane. It is not a `DOC_DELTA:` line in T11's primary log, so check 12's doc-delta append will not collect it; it is carried to QA-120 (§8) |
| D-09 | Noted. A model switch during the session did not change the session's identity, its scratch state or the evidence |
| E-01 | Accepted as a syntax-origin normalization (Glow QA Guide §3.4.10). The executed bytes equal the collection's bytes (§3) |

### 5.2 Defects found in my QA-90 collection v1.3

| ID | Defect and class | Effect | Correction for future collections |
| --- | --- | --- | --- |
| K-05 | Part B told the Product Owner to "Set the three vendor keys", and §4.1 treated `HD_API_BASE_URL` as a secret, entered with `read -rs`. The base URL is configuration, not an API key: the product reads two credentials (`HD_API_KEY`, `GEO_API_KEY`) and takes the base URL from `HD_API_BASE_URL` or its alias (HDE Build Notes 2.34 rule 4; result D-06). Class: task content, conservative, not a safety defect | None. The lines were skipped because the environment held the values (D-02) | Treat the base URL as configuration, use the environment's vendor configuration with a presence preflight, and never ask for values to be typed (2.34 rules 4, 5 and 7) |
| K-06 | The executor of the vendor commands was fixed text: W1's CONTEXT line `VENDOR_COMMAND_EXECUTOR: Nathan (Product Owner), PO-only, commands 4 to 28`, and the `executor:` and `authorization:` lines that command 13 writes into `vendor_request.txt`. When the Product Owner directed an agent to execute, these three stored lines misstated the executor. Class: evidence design | Three stored lines misstate the executor. The header's `command_provenance`, the `EXECUTION DEVIATION:` line, result D-01 and 2.34 state it accurately. Governed bytes are not edited (Glow QA Guide §4.3); the evidence stays reconstructible from the primary log (Glow QA Guide §4.4.6) | Record the executor of each part from a captured identity file, as `recorder_identity.txt` already does, not as fixed text |

Carried from review v1.0: K-01 to K-04 were applied in collection v1.3, and none recurred in T11. The collection's own repairs V-01 to V-05 were exercised: the scans ran before the restore, D2 printed the three-line summary, W2's gate held, and C1's gate read was mechanical. None of K-01 to K-06 changes a Plan objective, proof target, rails posture, evidence identity or predicate. All six are carried to the QA-120 RCA.

## 6. Run state and routing

- **Run state.** Plan v1.2 has 12 checks. Checks 1 to 10 are `ACCEPT` (review v1.0), and check 11 is `ACCEPT` (this review). Check 12 `qa-closeout-deliverables` is unissued, has no task and has no Product Owner selection recorded: NOT RUN. No already-authored task remains, so nothing is reusable through QA-100, and the run cannot go to QA-120.
- **Route.** QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23), for check 12 on the Product Owner's selection. QA-90 converts only Product Owner-selected steps. This follows the routing that review v1.0 used and HDE Build Notes 2.32 records for unissued checks.
- **Dependency.** Check 12 needs every other check recorded (Plan §11). That now holds: the manifest has 11 entries.
- **Constraints on the QA-90 task for check 12:**
  - It runs in the Run B checkout and stores on the Run B branch, whose head is now `380cf46` (LR-01 item 6).
  - Its [K] manifest predicate counts exactly one entry for each of checks 1 to 11.
  - Its doc-delta append collects T11's `DOC_DELTA:` line (primary log line 488: the base-URL variable name in HDE CLI/API Vendor Ref §3.7). It is the only `DOC_DELTA:` line in the primary logs of checks 3 to 11 at `380cf46`, so it becomes DD-13 (Plan check 12 step 2).
  - Its path proofs cover T11's primary log together with the ten earlier ones (Plan check 12 step 3).
  - Every command runs under the closed posture with the CLOSED prefix, because the vendor configuration is held in the QA console's environment (D-03; 2.34 rule 4).
  - Lessons K-01 to K-06 apply.

## 7. CANON_CONFLICT_REGISTER (carried, with one entry added)

C040-01 to C040-09 are carried unchanged from Plan v1.2 §2.3, through collection v1.3 §6 and review v1.0 §9. This review adds C040-10. The conflict it records decided a matter of this change, the authority for T11's execution, and its actual owner has decided it in PF10; the entry records that decision, not a local resolution. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 to v13.4.5 keep for 2.2 to 2.28. A proposal here is not approval.

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
| C040-10 | CANON_CONFLICT (vendor execution authority) | Barring an automated agent from the vendor call or requiring the Product Owner as executor: Glow QA Guide §3.3 and §3.5.7; HDE CLI/API Vendor Ref §3.7 and §7.1.8a; HDE Governance §3.4 ("Controlled vendor-backed no-user validation") and §11.1; HDE Mechanics Guide §1.1 and §17.9.4; Plan Templates "Artifact execution boundary" and "Proof-class and controlled vendor-smoke boundary"; HDE Build Checklist Fermentation, HDE-FERM008 and HDE-FERM008.2. Versus Product Owner-delegated execution: HDE Governance §3.4 ("HDAPI v2 open-rails vendor proof posture") and §9.1; Change Process Guide "Ops tasks"; Plan Templates "Execution authority (normative)", which are written for Ops tasks | Product Owner decision, 2026-09-29, recorded as HDE Build Notes addendum 2.34 PF10-VENDOR-001 (v13.4.5). A directed agent executes live vendor calls, including open-rails HumanDesignAPI calls in QA checks; "PO-only" names the authorizing principal; vendor configuration comes from environment variables. The listed bars are superseded for that scope | Product Owner; HDE Build Notes v13.4.5 addendum 2.34 (Timestamp 092926 06:04 UTC); direction given in the QA-100 session that executed T11 | PF10 2.34 governs; T11's delegated execution is authorized (§4.3) | The passages in 2.34's superseded-passage table; their maintainers; pending (2.34: "Drainage into the listed documents is unperformed") | Observed as a canon tension in collection v1.3 §7 on 2026-09-29, and not entered then because no decision of the change depended on it. It became decisive when the Product Owner directed the QA-100 session to execute T11's vendor commands (result D-01), and was decided the same day by addendum 2.34. Entered by this review |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013). Affected requirements for C040-10: the vendor-backed part of AC040-04 and AC040-09 (Plan check 11) and PO Q-2.

## 8. Unresolved items and owners

| Item | Owner | Status |
| --- | --- | --- |
| Selection of Plan check 12 `qa-closeout-deliverables` | Product Owner, at the QA-90 invocation | Open; the run cannot complete without it |
| Drainage of the passages that addendum 2.34 supersedes (C040-10) | Their maintainers | Pending, per 2.34 |
| Which execution environments hold the vendor configuration | Product Owner (2.34 deferred obligation) | Open, non-gating for check 12, which makes no vendor call |
| `.env.example` lacks `GEO_API_KEY` (D-08) | Implementation lane (2.34 deferred obligation) | Documentation drift; carried to QA-120 |
| D-07: 2.34 rule 5 against the Plan v1.2 posture that unsets `HDAPI_BASE_URL` | Kronos-23, QA-120 RCA | No vendor task remains in Plan v1.2; carried |
| Lessons K-01 to K-06, D-13 and the duplicate-execution deviation of review v1.0 | Kronos-23, QA-120 RCA; K-01 to K-06 also applied at QA-90 for check 12 | Carried |
| Run A's T03 outcome and T10 receipt (LR-01 item 7) | Product Owner | Open, non-gating; unchanged |
| Run A branch `qa/hde-epic040-qa100-plan-v1.2`: preserved, non-canonical, never merged into `main` as the QA root | Product Owner (merge authority) | Standing |
| Run B branch: the one evidence stream, now checks 1 to 11, to which check 12 appends; any pull request and merge | Product Owner | Open |
| PF10 v13.4.5 formatting: in addendum 2.28, row RA-06 is still split at `dev \| test \| local`; the file ends with the `<eof>` marker and no final newline. The index now also lists 2.33 and 2.34 | Product Owner (PF10 publication) | Observed; non-gating; Kronos does not edit PF-Canon |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING; no such procedure at `633ca5d` |

Path proofs remain unproduced until check 12. The QA-120 Report and the two deferred requirements of Plan §2 (live Gate readiness; live DB Reader success) remain outstanding.

## 9. Working state

| Field | Value |
| --- | --- |
| Stage | QA-110 complete for T11; next QA-90 for check 12 on the Product Owner's selection |
| Review | This file, `ACCEPT` for T11 |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-QA110-checkpoint-t11-v1.0.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA110-handoff-to-qa90-t11-v1.0.md` |
| Resume point | QA-90 — Create Bounded QA Execution Task — 091426.1, for Plan check 12 |

## 10. Nonclaims

- The `ACCEPT` covers one bounded check. It is not whole-change QA PASS.
- The review establishes none of the following: acceptance, closure, PF09 status movement, PF-Canon drainage, deployment, release activation, token satisfaction, Index or Mirror publication, or broad HumanDesignAPI v2 conformance.
- The vendor calls prove only what check 11 exercises (collection v1.3 §5): live vendor-backed CLI resolution, canonical stdout, AB↔BA identity, a bands-only Reader v1 dump and the binding to the admitted release. They do not prove the exact vendor resource path, auth-header family, rate-limit or error handling, mapped-cache persistence, Reader v2 over HTTP or any deployed service.
- QA-110 executed no task, made no vendor call, changed no approved artifact, repaired nothing and produced no PF10 addendum. Addendum 2.34 is the Product Owner's canon action.
- The review makes no claim for check 12, which is unissued and NOT RUN.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-110-20260929-02
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-04 and AC040-09 (vendor-backed part), PO Q-2, as mapped by Plan v1.2 check 11
  - prompt: QA-110 — Review QA Evidence and Route the Next Action — 091426.1; Notion 3db4590a05eb816984d1d34da0e08f40; page as of 2026-09-24T15:52:32.947Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-110
  - capture_time: 2026-09-29T06:41:04Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_EVIDENCE_REVIEW T11 v1.0, T11 `ACCEPT`, per-task result `PASS`; run incomplete; routed to QA-90 for check 12
  - task_and_attempt_mapping: T11 `open-rails-showcompat-vendor`, attempt 1; result HDE-EPIC040-QA100-qa-execution-results-t11-v1.0; evidence commit 380cf46fda95686ccf71f256521e63ca0eb5c9e1
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `633ca5d`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-100-20260929-02 (QA-100 result T11 v1.0); GCFPE-USE-HDE-EPIC040-QA-90-20260929-02 (collection v1.3); GCFPE-USE-HDE-EPIC040-QA-90-20260929-01 (collection v1.2); GCFPE-USE-HDE-EPIC040-QA-110-20260929-01 (review v1.0); GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (results v1.1); GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (collection v1.1).
