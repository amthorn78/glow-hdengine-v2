---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-EPIC040-QA90-QA-TASK-COLLECTION
artifact_version: "1.0"
predecessor: none (first QA-90 invocation for this change)
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
specification: docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md (Specification v1.1)
author: Kronos, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-90 / QA_PLAN v1.0 checks 1 to 10
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 091426.1 (Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z; read in full; registry lifecycle ACTIVE, session_class ROLE_CONTINUING, no trial restriction recorded)
ecosystem_release: GCFPE-20260914.1 (091426.1)
qa_plan_id: HDE-EPIC040-QA50-QA-PLAN v1.0 (approved base)
qa_plan_review_id: HDE-EPIC040-QA70-QA-PLAN-REVIEW v1.0 (APPROVE)
qa_audit_id: HDE-EPIC040-QA50-QA-AUDIT v1.0 (AUDIT_COMPLETE)
qa_step_ids: d0-discovery, step-0b-doc-delta-capture, ac040-08-evidence-validators, ac040-02-03-catalog-config, ac040-04-05-admission-identity, ac040-06-golden-comparison, ac040-07-gate-ingress-offline, ac040-04-09-compat-cli-offline, ac040-09-reader-http-in-process, sec-reader-http-live
selection_source: Product Owner task selection in the QA-90 handoff of 2026-09-27 (checks 1 to 10)
qa_task_ids: HDE-EPIC040-QA90-T01 to HDE-EPIC040-QA90-T10 (attempt 1 each)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md (SHA-256 54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d; provenance of what was read, not a gate)
observed_revision: 295722ed8b77468e94fdfc29b86145c30ff5e0cc (origin/main after amthorn78/glow-hdengine-v2#536)
observation_time_utc: 2026-09-27T10:51:17Z
next_prompt: QA-100 — Execute Bounded QA Task — 091426.1
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90
---

# HDE-EPIC040 — QA Task Collection v1.0 (QA-90): checks 1 to 10

## 1. Result

**`TASK_READY`.** This collection issues ten complete QA tasks, `HDE-EPIC040-QA90-T01` to `HDE-EPIC040-QA90-T10`, one for each check the Product Owner selected from the approved QA Plan v1.0 (checks 1 to 10), each at attempt 1, in Plan order. Checks 11 to 15 were not selected and have no task (§3).

- **Approval is for this exact Plan.** The QA-70 review names `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` at 86,589 characters. The file has 86,589 characters (86,864 bytes, SHA-256 `f3500c4952d4ee4f2080c2eaeb7b50c3b9fd77bb404d4287fd8806ec048403f3`) and was last changed by `efbe874`, the revision the review observed.
- **Every selected check fits the Plan's scope** (Plan §10, §11). T02 to T10 wait on T01, and T10 also waits on T09; Plan order satisfies both.
- **No material pre-execution defect remains.** One latent input problem, probe S-10's upper-case UUID, is resolved by faithful normalization N-05 (§4.6) without changing the objective, target, rails or predicate.
- This collection executes nothing, accepts no evidence, fixes nothing and declares no PASS. Every evidence file it names is NOT RUN until its task executes under QA-100.

## 2. Sources and lineage

### 2.1 Approved base (immutable)

| Artifact | Identity | Path | SHA-256 |
| --- | --- | --- | --- |
| QA Plan | `HDE-EPIC040-QA50-QA-PLAN` v1.0, approved at QA-70 | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` | `f3500c4952d4ee4f2080c2eaeb7b50c3b9fd77bb404d4287fd8806ec048403f3` |

The Plan's §12 check blocks govern every task. A task restates the Plan's commands and predicates to make them executable; if any restatement differs from the Plan, the Plan governs and the executor reports the difference in the QA-100 result instead of resolving it.

### 2.2 Overlays

| ID | Overlay | Path | What it adds |
| --- | --- | --- | --- |
| O-1 | QA Plan Review v1.0 (APPROVE; Isis-50; 2026-09-27) | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (SHA-256 `d5639bebb7905722f810b7809db1f273f9f1d9b55776286b4beeb0cb2649a083`) | §4: C040-09 APPROVED for this Plan and its tasks. §5: QA50-S01 resolution (check 11 only). §6: three QA-90 constraints (§7 here) |
| O-2 | PF10 v13.3.9 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` (SHA-256 `54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d`) | Addenda 2.2 to 2.28 as the Plan applies them (Plan §1, §2.2). Each task names the addenda it relies on. No PF10 addendum was produced for this change after v13.3.9 (QA-50: not produced; QA-70: none) |

### 2.3 Operational aids and instructions (not overlays)

| Source | Use |
| --- | --- |
| QA-90 handoff RCA v1.0, `docs/ephemeral/HDE-EPIC040-QA90-handoff-rca-v1.0.md` (SHA-256 `9421232c1af3be123a4a52ecc7c7dbc180dd0e6096665a95c053c1955acd05f5`), §5 | Prefixes C and S and the execution-order rules. They restate Plan §5.2 and §11 and change no predicate |
| Product Owner environment-handling instruction (QA-90 handoff, 2026-09-27) | Apply each check's "Must be UNSET" variables per command with `env -u`, never by changing the Codespaces configuration or secrets. Recorded as normalization N-01 |
| QA Audit v1.0, `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md` (SHA-256 `1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df`) | Audit-proven loci that tasks cite by L-number |
| Live QA Guide v1.0, `docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md` (GUIDE_READY; SHA-256 `5a61d77b8301dcee750eedb2916ecae1ec231d540b85028c022fa6d7883a9818`) | Lineage. Its obligations reach the tasks through Plan §2.1 |
| Product Owner disposition v1.0, `docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md` (SHA-256 `713e8c1f8c913ec13a59d18a17bb5a697b7cc4fc7ab3ff7635783012da204682`) | Q-1 reaches T10 through the Plan. Q-2 is check 11, not selected |

### 2.4 Controlled PF sources read

Each is the unique controlled Markdown file for its title in `docs/pfcanon/`, read by this Kronos session.

| Title | Path | SHA-256 | Used for |
| --- | --- | --- | --- |
| PF03-Reference-Technical-Writing-Best-Practices | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` | `cb123d2134b634c64589c1e193ef41a0bb5045f5d0b3fc85a8ff2cd3336399f3` | Source fidelity, task writing, syntax normalization, security (§3, §12, §13) |
| PF19-Canon-Glow-QA-Guide | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md` | `2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0` | §3.3, §3.4.3, §3.4.9, §3.4.10, §3.5.10, §4.4.4, §4.4.6, §10.6, §10.8 |
| PF27-Canon-Plan-Templates | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md` | `aa4ac7201e83beb46d43be80999049edcb43a2d24798a8b51ca6c2cce67b5248` | Step-log header v2, the five statuses and their causal precedence, Step-0B |
| PF10-HDE-Build-Notes | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` | `54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d` | Overlay O-2 |
| PF07-Canon-Glow-Infrastructure | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md` | `c4c2505ef3bda71bd4268b098faa03607aaa84c12f0c1f190f1f4ab82e880c4a` | Venue (§2.6 to §2.8), loopback (§2.2), server declaration (§10.1) |
| PF06-Canon-Change-Process-Guide | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md` | `ee51f4cc9e78709f7fbf5868c2891ad3a109c0ed9d87b367250738dc3d55d7e0` | Discovery artifact (§0.4.1.1) |
| PF12-Canon-HDE-Schemas-and-Artifacts | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md` | `d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d` | Evidence graph (§8.3, §8.6) |
| PF09.3-Canon-HDE-Build-Checklist-Separation | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md` | `0e3415e62e92f9d18c0d6ac1e513c1d8999efcacf2f71f4e1bda495fdbadec65` | HDE-SEPA005.1 to HDE-SEPA005.5 |
| PF05-Canon-HDE-CLI-API-Vendor-Ref | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` | `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e` | Reader transport (§5) as overlaid by PF10 Addenda 2.23 and 2.25 |
| PF01-Canon-HDE-Math-Spec | `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md` | `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a` | §9.5 goldens |

### 2.5 Carried lineage

- PR-30, PR-35 and `PR_RETURN_PHASE`: the approved Plan carries none.
- Earlier prompt uses: `GCFPE-USE-HDE-EPIC040-QA-50-20260927-01` (QA Plan and QA Audit provenance) and `GCFPE-USE-HDE-EPIC040-QA-70-20260927-01` (QA Plan Review provenance).
- Previous QA-90 result: none. At `295722e` no QA task exists for HDE-EPIC040 and the QA root `audit/qa/hde-epic040/` is absent, so there is no attempt history to reuse or preserve.
- Source state: between the planning basis `a6002d2` and `295722e` the only changed paths are under `docs/ephemeral/` (read-only `git diff`). The product source the Plan was written against is unchanged at the observed revision.

## 3. Selection reconciliation

| # | QA_STEP_ID | Selected | QA_TASK_ID | Attempt | Depends on | State at issue | Executor class (Plan §10) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Yes | `HDE-EPIC040-QA90-T01` | 1 | none | Issued; NOT RUN | E |
| 2 | `step-0b-doc-delta-capture` | Yes | `HDE-EPIC040-QA90-T02` | 1 | T01 recorded, any status | Issued; NOT RUN | E |
| 3 | `ac040-08-evidence-validators` | Yes | `HDE-EPIC040-QA90-T03` | 1 | T01 PASS | Issued; NOT RUN | E |
| 4 | `ac040-02-03-catalog-config` | Yes | `HDE-EPIC040-QA90-T04` | 1 | T01 PASS | Issued; NOT RUN | E |
| 5 | `ac040-04-05-admission-identity` | Yes | `HDE-EPIC040-QA90-T05` | 1 | T01 PASS | Issued; NOT RUN | E |
| 6 | `ac040-06-golden-comparison` | Yes | `HDE-EPIC040-QA90-T06` | 1 | T01 PASS | Issued; NOT RUN | E |
| 7 | `ac040-07-gate-ingress-offline` | Yes | `HDE-EPIC040-QA90-T07` | 1 | T01 PASS | Issued; NOT RUN | E |
| 8 | `ac040-04-09-compat-cli-offline` | Yes | `HDE-EPIC040-QA90-T08` | 1 | T01 PASS | Issued; NOT RUN | E |
| 9 | `ac040-09-reader-http-in-process` | Yes | `HDE-EPIC040-QA90-T09` | 1 | T01 PASS | Issued; NOT RUN | E |
| 10 | `sec-reader-http-live` | Yes | `HDE-EPIC040-QA90-T10` | 1 | T01 PASS and T09 PASS | Issued; dependency-waiting; NOT RUN | E |
| 11 | `open-rails-showcompat-vendor` | No | none | none | checks 1 and 8 PASS | Not selected; NOT RUN | P |
| 12 | `live-db-gate-readiness` | No | none | none | checks 1 and 7 PASS | Not selected; NOT RUN | P |
| 13 | `live-db-reader-refusal` | No | none | none | checks 1 and 10 PASS | Not selected; NOT RUN | P |
| 14 | `live-db-reader-success` | No | none | none | check 12 PASS with `READY` and `requested` at least 2; check 13 PASS | Not selected; NOT RUN | P |
| 15 | `qa-closeout-deliverables` | No | none | none | every other check recorded, any status; runs last | Not selected; NOT RUN | E |

Counts: 15 Plan checks; 10 selected, 10 tasks issued at attempt 1, all NOT RUN; 5 not selected; 1 issued task waits on another issued task (T10 on T09); 0 PARKED; no rerun issued.

Order: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10. This is the Product Owner's order and Plan order, and it satisfies every dependency.

Effects of the selection. These are limitations, not defects:

1. **Check 15 is not selected.** This batch therefore produces no path proofs (PF19 §3.4.3), no manifest verification, no append of `DOC_DELTA:` lines to the Step-0B surfaces, no governed-graph non-interference observation and no coverage accounting. They stay owed to check 15, which runs after every selected check is recorded. Until then the committed evidence of this batch is primary logs, supplementary files, the manifest and the two Step-0B surfaces.
2. **Checks 11 to 14 are not selected.** The Q-2 vendor step, live Gate readiness and both live-database Reader checks stay NOT RUN. QA-70 §6 items 1 and 3 carry to their future tasks (§7).
3. **The Plan expects one checkout for all fifteen checks** (Plan §7.1). If a later selection runs in a different checkout, T01's discovery record does not describe that checkout, and QA-110 decides how that selection establishes the `d0-discovery` prerequisite.

## 4. Common execution contract

Every task applies this section. A task's own text adds to it and never relaxes it.

### 4.1 Executor, venue and session

- **Session.** QA-100 runs in a new dedicated top-level session that Nathan creates (registry: QA-100 `session_class` DEDICATED_ONE_OFF; `session_disposition: NEW_DEDICATED`). Its operator is the authorized environment operator, not Kronos.
- **Authorized environment executor.** Nathan (Product Owner), for T01 to T10 (Plan §7.1).
- **Delegation (Plan §6; QA-70 §6 item 2).** The Product Owner's selection names no execution agent, so none is recorded here. Under Plan §6, Nathan therefore executes T01 to T10. If Nathan delegates instead, the binding is:
  - Nathan names one repository-capable execution agent, in Nathan's own words, when opening the QA-100 session;
  - that agent works in the same checkout, on T01 to T10 only, under closed rails, with no plaintext secret, vendor call or database contact;
  - before T01's first command, the executor copies Nathan's instruction verbatim into T01's `=== CONTEXT ===` with the agent's session identity, as the Plan §6 delegation record.

  The delegate's identity does not exist yet, so it is bound then and not invented here. This collection grants no authority by itself.
- **Venue.** Nathan's GitHub Codespace for `amthorn78/glow-hdengine-v2` (the Plan's preferred venue), or another Product Owner-controlled Linux shell that satisfies every T01 prerequisite. All ten tasks run in one checkout, in one session, in order. No deployed service is a target.
- **Tested source.** The checkout's HEAD as T01 records it, expected `295722e` or a later `main` commit (Plan §5.3). Source identity is attribution only and never a predicate (PF19 §3.4.9; C040-09).
- **Interpreter precondition.** CPython 3.12 must be available outside the repository before T01. The repository devcontainer (`.devcontainer/devcontainer.json`) uses the image `mcr.microsoft.com/devcontainers/python:3.11`, and its post-create script builds `.venv` inside the checkout on that interpreter; neither satisfies T01 (QA Audit QA50-F08). Providing Python 3.12 is an environment action outside the repository, not a QA step. If it is absent when T01 runs, T01 records `TOOLING_BLOCKED` (Plan CHECK 1).
- **Scratch root.** `/tmp/hde-epic040-qa/` holds the venv, the captures and temporary inputs. It is outside the repository and is never committed.
- **Forbidden throughout** (Plan §2, §7.2, §7.5; QA Audit L-07, L-12):
  - any command a task does not list;
  - `tools/config/generate_config_artifacts.py` in any mode other than `--help`, `--check` or `--compare-goldens` (without a mode flag it writes);
  - `scripts/release_id_recompute.py` in any mode other than `--help` and `--check-manifest-only`;
  - `hdctl bg:resolve`, any `hdctl showcompat` run other than `--help`, writer routes, upserts, database access, vendor or AI-provider calls, and any network service other than T10's loopback server;
  - editing any product, test, tool, schema, catalog, manifest, CI, Index, Mirror or PF file;
  - any Git write other than the evidence commit and push of §4.4.

### 4.2 Rails prefixes (normalization N-01)

The Plan's "Must be UNSET" variables are removed per command with `env -u`. The shell's own environment, the Codespaces configuration and its secrets are never changed, and no value is ever printed; T01 records presence as SET or UNSET only.

Prefix `[C]`, ENV-C (Plan §5.2):

```text
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
```

Prefix `[CP]`, ENV-C in the pytest posture of Plan §5.2 and CI:

```text
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
```

Prefix `[C7]`, for T07 command 4 only (Plan §5.2, "Rails change inside a check"):

```text
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=0 ALLOW_NETWORK=0 APP_ENV=dev
```

Prefix `[S]`, ENV-S, for T10's server command and T10's recording only:

```text
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=prod PORT=8000
```

`[none]` means no prefix. It applies to T01 commands 1 and 2, which observe the ambient environment before ENV-C is applied, and to shell actions such as venv activation and stopping the server.

Rules:

- A command written as `[C]` followed by `python X` is executed as the prefix's words followed by `python X`. The executed argv, and therefore the recorded `command`, includes the prefix.
- After T01 command 6, the venv must be active in every shell that runs a task command. A persistent shell runs `. /tmp/hde-epic040-qa/venv/bin/activate` once. A tool whose shell state does not persist between invocations runs it at the start of every invocation. `python`, `python3` and `hdctl` then resolve to `/tmp/hde-epic040-qa/venv/bin/`, and in this collection `python` always means that interpreter.
- Every command runs from the repository root.

### 4.3 Commands, captures and recording

**Step-local readiness.** In T02 to T10, commands 1 and 2 are the readiness line of Plan §12:

1. `[C]` `python --version`, expected `Python 3.12.` followed by the patch number;
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`, expected exit 0.

If either fails, the task is `TOOLING_BLOCKED`, or `FAIL_TOOLING` if the harness itself malfunctions after a good install (Plan §12).

**Captures.** Before a task's first command, create its capture directory with `mkdir -p` (setup outside the repository, noted in CONTEXT, not listed in `command`). Keep each numbered command's stdout, stderr and exit status in that directory, named after the command number: for command 3, `c3.out`, `c3.err` and `c3.rc`. The only exceptions are commands whose stdout the task sends to an evidence file, and T10's probes, which the task names. Use the form `command > c3.out 2> c3.err; echo $? > c3.rc` with the capture directory's paths, so the status is the producer's own. Never take a status through a pipe (Plan §12).

**Embedded Python (N-02).** Evaluators, writers and probes run as `python -c` or as `python -` reading a shell heredoc. No script file is created (C040-09). Each one's exact code goes verbatim into the task's primary log.

**Tree digest (N-04).** Given root directories and exclusions: list every path under the roots that is not a directory, meaning regular files and symbolic links (a link to a directory counts as a link and is not followed), and skip excluded directories entirely. For each path write one line of three tab-separated fields: the path relative to the repository root with `/` separators; `f` for a regular file or `l` for a link; and the SHA-256 of the file's bytes, or of the link's target text in UTF-8. Sort the lines by path in byte order, join them with LF and end with LF. The digest is the SHA-256 of that text. Record the digest and the line count in OUTPUT, and keep the listing in the capture directory so that any difference can be itemized.

**Recording.** Each task is recorded by one call from an embedded Python recorder, run under `[C]` (under `[S]` in T10, N-08). The recorder imports `from pathlib import Path` and `from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, classify_pytest_returncode, record_check`, builds one `CheckResult` from the captures, and calls `record_check(HarnessConfig("HDE-EPIC040", Path.cwd()), result)`. The recorder is not itself listed in `command`.

| `CheckResult` field | Value (Plan §8; QA Audit L-41, L-42; PF27 required v2 keys) |
| --- | --- |
| `check_id` | The task's QA_STEP_ID |
| `status` | The `Status` member that the task's rules select, under PF27 causal precedence: untrustworthy tooling or evidence selects `FAIL_TOOLING`; otherwise a missing prerequisite selects `TOOLING_BLOCKED`; otherwise a proven false behavior predicate selects `FAIL_BEHAVIOR`; `PASS` only when every predicate holds |
| `status_reason` | Empty for `PASS`; otherwise one sentence naming the deciding predicate or stop point |
| `check_name` | The Plan §10 check name the task gives |
| `command` | Every executed argv, in order, each a tuple of strings that begins with its prefix words. Empty only when nothing ran |
| `command_provenance` | `QA_PLAN v1.0 §12 CHECK` with the check number, the task ID and `attempt 1`, then the normalizations used (§4.6) and any in-flight normalization with its reason. Exactly `Not executed` when nothing ran |
| `exit_code` | Exit status of the task's final decisive command. If the task stopped before that command, the status of the last command executed. `None` only when nothing ran |
| `output` | The body described below |
| `evidence_artifacts` | The task's evidence files, repository-relative. The harness adds the task's own `primary.log` |
| `intended_tokens` | Empty. The harness always writes `claimed_tokens` as empty |
| `pf_refs` | The titles the task lists: the Plan check block's PF anchors (N-09). PF10 is cited in the body (QA50-F07) |
| `captured_env` | Left empty, so the harness records the recorder's actual `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK` and `APP_ENV` |

Body sections (PF19 §4.4.6; Plan §8):

- `=== CONTEXT ===`: task ID and attempt; Plan step; tested source (T01 command 3); executor and session identity; the delegation record in T01 when one exists; interpreter and venv path; the prefixes used; capture directory; UTC start time.
- `=== COMMANDS ===`: each numbered command as executed, prefix included, with its exit status and where its stdout and stderr went. Shell actions such as venv activation and stopping the server appear as text.
- `=== OUTPUT ===`: every command's stdout and stderr verbatim, and every piece of embedded code verbatim. Each supplementary evidence file gets one line in `sha256sum` format, the 64-character digest, two spaces, then the repository-relative path. Only T01's pip output may be shortened, and only with an explicit `[SNIP: n lines omitted]` marker (PF19 §3.4.10).
- `=== PREDICATES ===`: each predicate of the task with PASS or FAIL and the observed value.
- `=== LIMITS ===`: proof class, nonclaims and the PF10 addenda relied on.

Markers: a line starting `BLOCKER:` records a prerequisite gap found by T01, and T02 copies it. A line starting `DOC_DELTA:` records any documentation mismatch a task observes; check 15 collects those later.

Other recording rules:

- **Dependency not PASS.** Record the task `TOOLING_BLOCKED` with no command, `exit_code` `None`, `command_provenance` `Not executed`, and a reason naming the dependency and its status. Run nothing else (Plan §11).
- **Harness unavailable.** If the recorder cannot import the harness, no primary log can be written. Never write one by hand. Report the task as `BLOCKED` in the QA-100 result with the actual error.
- **Record once.** If `record_check` raises, keep the error text, do not retry by guesswork, and report it.

### 4.4 Evidence files and commit boundary (Plan §7.2; QA-70 §6 item 2)

**Evidence branch:** `qa/hde-epic040-qa100-checks-1-10`, created from the tested commit. If the QA-100 session's platform binds its work to a different branch name, use that branch and record its name in the QA-100 result. Branch names are storage, not predicates (Plan §7.2; PF19 §3.4.9).

Files that may be committed. Each is NOT RUN until its task produces it. Commit only files that exist, and never create one by hand:

1. `audit/qa/hde-epic040/qa_step_logs_manifest.json`
2. `audit/qa/hde-epic040/checks/d0-discovery/primary.log`
3. `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log`
4. `audit/docdeltas/hde-epic040_doc_deltas.md`
5. `audit/qa/hde-epic040/00_meta/doc_deltas.md`
6. `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log`
7. `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`
8. `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log`
9. `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log`
10. `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json`
11. `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json`
12. `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`
13. `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json`
14. `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log`
15. `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log`
16. `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log`
17. `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log`
18. `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl`
19. `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`

QA-100 also commits its own result document under `docs/ephemeral/` on the same branch (QA-100 contract). Not expected under this collection: `attempt1_primary.log` and `rerun_note.md` (attempt 2 only), files under `audit/qa/hde-epic040/00_meta/delta/` (Moon Loop, §4.5) and `.path_proof.txt` files (check 15).

Procedure, after the last task is recorded and T10's server is stopped:

1. Run `git status --porcelain`. List every changed path outside the permitted list for the QA-100 result; never stage or revert it.
2. Switch to the evidence branch, creating it with `git checkout -b qa/hde-epic040-qa100-checks-1-10` if it does not exist.
3. Stage the permitted files that exist by explicit path (`git add --` followed by the paths), never by directory, `-A` or `.`.
4. Confirm with `git diff --cached --name-only` that exactly those paths are staged.
5. Commit. The message names HDE-EPIC040, checks 1 to 10, attempt 1 and the tested source commit from T01 command 3 (Plan §7.2).
6. Push with `git push -u origin qa/hde-epic040-qa100-checks-1-10`.

Boundaries:

- Never commit a secret value, a real user identifier or a BodyGraph payload. The synthetic UUIDs of QA Audit L-50 (`00000000-0000-0000-0000-000000000001`, `00000000-0000-0000-0000-000000000002`) and the derived test values of T07 and T10 are fixture-class values and may appear.
- No pull request. QA-100 cannot open or merge one, so the Plan §7.2 permission to open one evidence pull request is not exercised; Nathan opens and merges it. CI runs on that pull request, not on the branch push (`.github/workflows/ci.yml` triggers), and its outcome is not a predicate of any task.
- No force-push, rebase or merge (Plan §7.2). Evidence storage is not a check and not part of any predicate.

### 4.5 Stop, rerun, recovery and cleanup

- **Independent work continues.** T02 to T09 depend only on T01, and T10 also on T09. A failure in one of T03 to T09 does not stop the others.
- **Attempt 1 only.** A task that ends `FAIL_TOOLING` or `TOOLING_BLOCKED` from an execution or evidence fault is recorded as it is; only Kronos's QA-110 decision can route attempt 2 through QA-90 (Plan §7.3; PF19 §10.6). A `FAIL_BEHAVIOR` goes through QA-110 to ESC-10. Never re-run a command to obtain a different result, and never change an expected value.
- **Moon Loop** (Plan §7.4) is not self-initiated under this collection, because QA-100 may not select a rerun. Record the defect and its failure signature, and return it to QA-110, which can route the bounded correction.
- **Preserve attempt-1 bytes.** Never delete or overwrite a recorded primary log or supplementary file.
- **Secret found in an evidence file:** quarantine the file outside the repository, do not commit it, and record the task `FAIL_TOOLING` (Plan §7.5).
- **Cleanup.** T10 stops its server and confirms port 8000 is closed on every path, including early stops. `/tmp/hde-epic040-qa/` stays in place; it is not evidence and is never committed. No database or vendor state is touched, so there is nothing to roll back.
- **Residual state for the QA-100 result:** server stopped and port closed (T10), the `git status --porcelain` summary, the branch, and the pushed commit.

### 4.6 Normalizations (Plan §12; PF19 §3.4.10; QA-90 Execute step 5)

Each keeps the Plan's objective, target, rails, evidence identity and predicates unchanged.

| ID | Normalization | Reason |
| --- | --- | --- |
| N-01 | "Must be UNSET" is applied per command with `env -u` through the §4.2 prefixes; the ambient environment is untouched | Product Owner instruction; the names are exactly Plan §5.2's; RCA §5 |
| N-02 | Embedded Python runs as `python -c` or as `python -` with a heredoc; shell built-ins run as `bash -c` with their exact text so that the recorded argv is exact | C040-09 forbids a script file; Plan §12 requires the exact command |
| N-03 | The Plan's outside-repository temporaries get concrete paths under `/tmp/hde-epic040-qa/` | Plan §7.5; CHECK 6 step 5; CHECK 7 step 2 |
| N-04 | The digest algorithm is made exact (§4.3) | Plan CHECK 3 supplementary digest; CHECK 6 steps 1 and 6 |
| N-05 | Probe S-10 sends `a_id` `00000000-0000-0000-0000-00000000000A` | The Plan's synthetic UUIDs contain only digits, so their upper-case form equals the valid body and would reach the resolver (503) instead of testing the upper-case refusal. `_parse_reader_post_body` in `adapter/http_reader.py` refuses a UUID that is not lowercase canonical with 422 (`strict_canonical_uuid`) |
| N-06 | Probes S-04 to S-06 carry the valid body. S-12 and S-13 carry the valid body followed by space characters to exactly 32,769 bytes | So that only the version rule or only the size limit can refuse. JSON permits trailing whitespace, so without the size limit that body would parse and reach the resolver |
| N-07 | curl specifics: `--head` for HEAD; `-H 'Expect:'` on POST probes; `-H 'Transfer-Encoding: chunked'` for S-13; one assembly command writes all 26 JSONL lines after the probes | HEAD without waiting for a body; no interim 100 response in the capture; chunked without `Content-Length` (Plan CHECK 10 step 2) |
| N-08 | T10's recorder runs under `[S]`, so `captured_env` records the server posture (`APP_ENV=prod`); the client posture goes in CONTEXT | Plan §8 `captured_env` for a check with two postures |
| N-09 | `pf_refs` are the Plan check block's PF anchors as exact titles | Harness `PF_TITLE_RE`; QA50-F07 |
| N-10 | Every pytest status comes from the harness's `classify_pytest_returncode`; `run_pytest_check` is not used | The Plan says "may"; one body layout and provenance for every task |
| N-11 | T01 adds two read-only observations: `command -v python3.12` and `command -v python python3 hdctl` | Record the interpreter and entrypoint resolution that Plan CHECK 1 intends; no predicate added |

### 4.7 Return to QA-110

- QA-100 writes one result document under `docs/ephemeral/` (suggested name: `docs/ephemeral/HDE-EPIC040-QA100-qa-execution-result-v1.0.md`) with one `QA_EXECUTION_RESULT` per task T01 to T10, then hands off to QA-110 — Review QA Evidence and Route the Next Action — 091426.1 in the continuing Kronos session.
- Each result carries: task, step, attempt, Plan and environment identity; the harness status and reason recorded in the primary log; evidence paths; commit reference once observed; cleanup and residual state; criterion observations; `BLOCKER:` and `DOC_DELTA:` lines; any supplementary-digest difference from T03; and the resume point.
- The QA-100 execution state and the harness status are separate facts. Neither is acceptance or QA PASS.

## 5. Tasks

Every evidence path below is NOT RUN until its task executes. Every task returns through the QA-100 result to QA-110 (§4.7).

### T01 `d0-discovery` — Discovery and tooling bootstrap

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T01`, attempt 1 |
| QA_STEP_ID | `d0-discovery` (Plan §10 row 1; D0; prerequisite for all criteria) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 1 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` §4 (C040-09) and §6 item 2; `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addenda 2.12, 2.15, 2.22 |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-01, L-03, L-06, L-09, L-11, L-12, L-41, L-43; EPIC / HDE-EPIC040 |
| Objective | Before any behavior check, establish and record this checkout's tested source, interpreter, dependencies, harness, CLI and tool entrypoints, rails, environment presence and admission, and the initial absence of the QA root |
| Environment and target | ENV-C. Commands 1 and 2 `[none]`, then `[C]`. Target: the local checkout; no service |
| Dependencies | None. T02 to T10 depend on it |
| Setup and data | Python 3.12 available (§4.1). `mkdir -p /tmp/hde-epic040-qa/t01` and note in CONTEXT whether `/tmp/hde-epic040-qa` existed before. If Nathan delegates, the delegation record goes into CONTEXT before command 1 (§4.1) |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 17 |
| `check_name` | `Discovery and tooling bootstrap` |
| `pf_refs` | `PF06-Canon-Change-Process-Guide`, `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/d0-discovery/primary.log`. The recording also creates `audit/qa/hde-epic040/` and `audit/qa/hde-epic040/qa_step_logs_manifest.json`. `evidence_artifacts` stays empty (the harness adds the primary log) |

Commands, in order. Plan step numbers are in brackets.

1. `[none]` `bash -c 'test -e audit/qa/hde-epic040'`. Expected exit 1 (absent). Runs before anything is written in the checkout. [Plan 1]
2. `[none]` The presence record. It prints SET or UNSET for ten names (a set but empty variable counts as SET) and the values of the six rail names, which are not secrets. [Plan 2]

   ```bash
   bash -c 'for n in DATABASE_URL HD_API_BASE_URL HDAPI_BASE_URL HD_API_KEY GEO_API_KEY DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV PORT; do if [ -n "${!n+x}" ]; then echo "$n=SET"; else echo "$n=UNSET"; fi; done; for n in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do if [ -n "${!n+x}" ]; then echo "$n=${!n}"; else echo "$n=UNSET"; fi; done'
   ```

   From here on, ENV-C is applied per command.
3. `[C]` `git rev-parse HEAD`. The tested source, for attribution only. [Plan 3]
4. `[C]` `git status --porcelain`. The body records the line count only. [Plan 3]
5. `[C]` `bash -c 'command -v python3.12'`. Interpreter discovery (N-11). If `python3.12` is not on `PATH` but Nathan has provided a CPython 3.12 at another path outside the repository, command 6 uses that absolute path and CONTEXT records it. [Plan 4]
6. `[C]` `python3.12 -m venv --clear /tmp/hde-epic040-qa/venv`. Expected exit 0. Then the shell action `. /tmp/hde-epic040-qa/venv/bin/activate` (§4.2). [Plan 4]
7. `[C]` `python --version`. Expected `Python 3.12.` followed by the patch number. [Plan 4]
8. `[C]` `python -m pip install -r requirements.txt -r requirements-dev.txt -e .`. Expected exit 0. [Plan 4]
9. `[C]` `python -m pytest --version`. Expected exit 0. [Plan 4]
10. `[C]` `bash -c 'command -v python python3 hdctl'`. Expected three paths under `/tmp/hde-epic040-qa/venv/bin/` (N-11). [Plan 4]
11. `[C]` The harness registration preflight. Expected exit 0 and `harness_ready` on stdout. [Plan 5]

    ```bash
    python -c "from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check, run_pytest_check; from tools.evidence.update_evidence_index import _refresh_path_proof; print('harness_ready')"
    ```

12. `[C]` `hdctl --help`. [Plan 6]
13. `[C]` `hdctl showcompat --help`. [Plan 6]
14. `[C]` `python tools/config/generate_config_artifacts.py --help`. [Plan 6]
15. `[C]` `python tools/bodygraph/check_magic10_gate_readiness.py --help`. [Plan 6]
16. `[C]` `python scripts/release_id_recompute.py --help`. [Plan 6]
17. `[C]` Admission, the final decisive command. [Plan 7]

    ```bash
    python -c "from engine.config.registry_loader import load_active_mechanics_bundle as f; b=f(); print(type(b).__name__, b.manifest.version, b.manifest.built_at_utc, len(b.manifest.files), b.release_id, b.mechanics['config_id'])"
    ```

18. `[C]` `sha256sum catalog/manifest.json`. [Plan 7]
19. `[C]` `python scripts/release_id_recompute.py --check-manifest-only`, run only if command 17 exits non-zero or its `release_id` differs from command 18's digest. It classifies the failure. [Plan CHECK 1 FAIL_BEHAVIOR and TOOLING_BLOCKED rules]
20. `[C]` `git check-ignore -v audit/qa/hde-epic040/checks/d0-discovery/primary.log audit/qa/hde-epic040/qa_step_logs_manifest.json audit/docdeltas/hde-epic040_doc_deltas.md`. Informative; exit 1 means none is ignored. [Plan 8]
21. Recording (§4.3), which creates the QA root and the manifest. [Plan 9]

Inputs and outputs: inputs are the checkout, the ambient environment's presence, the interpreter and the two requirements files. Outputs are the recorded facts and the admission line; the only repository writes are the recording's.

Predicates:

- **P1.** Command 1 exited 1: the QA root was absent before anything was written.
- **P2.** Command 7 printed `Python 3.12.` with a patch number. Commands 8 and 9 exited 0. Command 11 exited 0 and printed `harness_ready`.
- **P3.** Commands 12 to 16 exited 0. The stdout of 13 contains `--source`, `--birthdate-a`, `--birthtime-a`, `--location-a`, `--birthdate-b`, `--birthtime-b`, `--location-b` and `--dump-reader`. The stdout of 14 contains `--compare-goldens`, `--goldens` and `--report`. The stdout of 15 contains `--user-id` and `--selection-file`. The stdout of 16 contains `--check-manifest-only`.
- **P4.** Command 17 exited 0 and printed one line of six space-separated fields: `AdmittedMechanicsBundle`, `1.3.0`, `2026-08-24T18:04:49Z`, `45`, a `release_id` equal to the digest command 18 printed, and `m10-channel-state-v1.0.0`.
- Commands 2, 3, 4, 5, 10 and 20 are observations, not predicates.

Status (Plan CHECK 1, under PF27 precedence):

- **PASS:** P1 to P4 hold.
- **FAIL_TOOLING:** command 11 fails after commands 8 and 9 succeeded, or a help command ends with a traceback.
- **TOOLING_BLOCKED:** P1 fails (the QA root pre-exists at attempt 1); no Python 3.12 is available; command 6, 8 or 9 fails; an entrypoint or a Plan-used flag is missing (P3); or command 17 refuses and command 19 exits 1 (modified members: source contamination, not behavior). Write one `BLOCKER:` line naming each gap.
- **FAIL_BEHAVIOR:** command 17 refuses, or its `release_id` differs from command 18's digest, while command 19 exits 0.

Limits: source identity is attribution only. PF10 Addendum 2.15: release 1.3.0 is admitted, so `RELEASE_NOT_ADMITTED` is not an expected outcome. Addendum 2.22: installs are editable from the source tree because a wheel install refuses admission.

Cleanup and recovery: none; the venv stays for T02 to T10. If the venv could not be built, the recorder may run under any available interpreter that imports the harness under `[C]`, and CONTEXT names that interpreter. If no interpreter can import the harness, follow §4.3 ("Harness unavailable").

### T02 `step-0b-doc-delta-capture` — Step-0B doc-delta capture

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T02`, attempt 1 |
| QA_STEP_ID | `step-0b-doc-delta-capture` (Plan §10 row 2; D1) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 2 and §9.1 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` §4 (DD-02 is C040-09's drainage row) and §7; `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` (rows DD-07 and DD-12 refer to it; the writer copies them unchanged) |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) findings behind DD-01 to DD-06 (QA50-F11 to F14, B01) and locus L-41; EPIC / HDE-EPIC040 |
| Objective | Mechanically record the Plan's §9.1 doc deltas and every `BLOCKER:` line of T01's primary log on both Step-0B surfaces, byte-identical |
| Environment and target | ENV-C, `[C]`. Target: the local checkout |
| Dependencies | T01 recorded, any status. If T01's primary log does not exist: `TOOLING_BLOCKED`, nothing run |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t02`. The rows come from the approved Plan file itself |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 6 |
| `check_name` | `Step-0B doc-delta capture` |
| `pf_refs` | `PF27-Canon-Plan-Templates`, `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log`; `audit/docdeltas/hde-epic040_doc_deltas.md`; `audit/qa/hde-epic040/00_meta/doc_deltas.md`. The two surfaces are listed in `evidence_artifacts` and bound by SHA-256 lines |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` `bash -c 'test -e audit/docdeltas/hde-epic040_doc_deltas.md'`. Expected exit 1. [Plan 1]
4. `[C]` `bash -c 'test -e audit/qa/hde-epic040/00_meta/doc_deltas.md'`. Expected exit 1. If command 3 or 4 exits 0, run `[C]` `sha256sum` on the existing file (captures `c4a.out`, `c4a.err`, `c4a.rc`), write nothing, and record `FAIL_TOOLING`; nothing is overwritten. [Plan 1]
5. `[C]` The writer, embedded Python. [Plan 2] It:
   1. checks that `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` has SHA-256 `f3500c4952d4ee4f2080c2eaeb7b50c3b9fd77bb404d4287fd8806ec048403f3`, and otherwise writes nothing and stops (`FAIL_TOOLING`, input mismatch);
   2. takes from that file, between the line `### 9.1 Step-0B doc-delta rows` and the line `## 10. Runbook Check Matrix`, the twelve lines that start with `| DD-`, and checks that they are DD-01 to DD-12 in order;
   3. takes from `audit/qa/hde-epic040/checks/d0-discovery/primary.log`, after its first (header) line, every line that starts with `BLOCKER:`, in order;
   4. renders UTF-8 text without BOM, with LF line ends and exactly one final LF, made of: the title line `# HDE-EPIC040 Step-0B doc deltas (QA_PLAN v1.0, docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md)`; a blank line; `## BLOCKERS`; a blank line; either the single line `none` or one line per blocker, `- BL-01: ` followed by the text after `BLOCKER:` with leading spaces removed, numbered BL-01, BL-02 and so on in order; a blank line; `## CAVEATS`; a blank line; the header line `| ID | Class | Delta | Drain target (title) | Owner | Drives decision |`; the line `| --- | --- | --- | --- | --- | --- |`; and the twelve Plan rows, each with ` No |` appended;
   5. creates `audit/qa/hde-epic040/00_meta/` if needed and writes the same bytes to both surfaces.
6. `[C]` `cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`. Final decisive; expected exit 0. [Plan 3]
7. `[C]` `sha256sum audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`. [Plan 3]
8. Recording (§4.3).

Inputs and outputs: inputs are the Plan's §9.1 rows and T01's `BLOCKER:` lines. Outputs are the two identical Markdown surfaces.

Predicates (Plan CHECK 2): both files exist, are non-empty, end with LF, have no BOM and are byte-identical (command 6 exits 0); each of DD-01 to DD-12 appears exactly once as a line starting with its row cell (for DD-01, `| DD-01 |`); `## BLOCKERS` and `## CAVEATS` are both present; and the text of every T01 `BLOCKER:` line appears under BLOCKERS.

Status:

- **PASS:** every predicate holds.
- **FAIL_TOOLING:** the files differ, are empty or miss a row; existing content would be overwritten (command 3 or 4 exits 0); or the Plan file's digest differs.
- **TOOLING_BLOCKED:** T01 produced no primary log.
- **FAIL_BEHAVIOR:** not applicable; this task makes no behavior claim.

Cleanup and recovery: none. Only check 15 appends to these surfaces later; nothing in this collection edits them after this task.

### T03 `ac040-08-evidence-validators` — Owner evidence coherence and evidence tests

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T03`, attempt 1 |
| QA_STEP_ID | `ac040-08-evidence-validators` (Plan §10 row 3; D2; AC040-08; K040-REQ-012) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 3 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (approval; §4 C040-09); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addenda 2.12 and 2.21 (admission and canonical-JSON-gate identity) |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-13, L-44, L-45 and test group G (§4.4); EPIC / HDE-EPIC040 |
| Objective | Re-verify, read-only, that the owner-generated evidence graph and governed families are coherent at the tested source, and run the evidence and QA-tooling test group |
| Environment and target | ENV-C, `[C]`; the pytest run `[CP]`. Target: the local checkout |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t03` |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 13 |
| `check_name` | `Owner evidence coherence and evidence tests` |
| `pf_refs` | `PF12-Canon-HDE-Schemas-and-Artifacts`, `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` Supplementary digest before (embedded Python; tree digest of §4.3 with roots `docs/evidence`, `artifacts` and `audit/gates` and no exclusions). Non-gating. [Plan supplementary]
4. `[C]` `python tools/evidence/update_evidence_index.py --check` [Plan 1]
5. `[C]` `python tools/evidence/orientation_demo.py --check` [Plan 2]
6. `[C]` `python tools/evidence/validate_evidence_paths.py` [Plan 3]
7. `[C]` `./ci/checks/check_mirror_schema.sh` (a Python script, invoked directly) [Plan 4]
8. `[C]` `ci/checks/check_evidence_index_hash.sh` [Plan 5]
9. `[C]` `python tools/evidence/run_canonical_json_gate.py --check-only` [Plan 6]
10. `[C]` `python tools/evidence/check_lf_endings.py` [Plan 7]
11. `[C]` `ci/checks/check_env_pins.sh` [Plan 8]
12. `[C]` `python tools/config/generate_config_artifacts.py --check` [Plan 9]
13. `[CP]` Pytest group G, the final decisive command. [Plan 10]

    ```bash
    python -m pytest -q -p no:cacheprovider -rs tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_cli_conformance_artifacts.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_engine_core_evidence.py tests/evidence/test_epic030_pr05_category_framework_evidence.py tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_sanity_pipeline.py tests/qa/test_qa_tool_ownership.py
    ```

14. `[C]` Supplementary digest after, with the same code as command 3. [Plan supplementary]
15. Recording (§4.3).

Inputs and outputs: inputs are the governed evidence graph and families at the tested source. Outputs are validator exit statuses and messages, the pytest summary with skip reasons, and the two supplementary digests.

Predicates (Plan CHECK 3): commands 4 to 13 exit 0; the pytest summary reports no failure and no error; skips are listed with their reasons.

Supplementary, non-gating: if the digests of commands 3 and 14 differ, write the added, removed and changed paths in OUTPUT and report the difference in the QA-100 result. It does not change the status.

Status:

- **PASS:** every predicate holds.
- **FAIL_TOOLING:** a validator ends with a traceback (`Traceback (most recent call last)` in its stderr), or pytest exits 2, 3, 4 or a negative status.
- **TOOLING_BLOCKED:** T01 is not PASS; an entrypoint is missing; or pytest exits 5.
- **FAIL_BEHAVIOR:** a validator runs to completion and reports incoherent delivered evidence (a non-zero exit with a governed error token and no traceback), or pytest exits 1. The QA RCA classifies an evidence-coherence failure as a documentation or evidence failure, not a runtime failure (Plan CHECK 3).

Authoring note, a static reading and not a predicate: the QA files that T01 and T02 have already written are not inputs to these validators. The updater's check mode renders only explicitly listed entries and walks no directory (`_run_once` in `tools/evidence/update_evidence_index.py`); `check_lf_endings.py` delegates to `ci/checks/check_final_lf.sh`, which checks a fixed file list; and `validate_evidence_paths.py` reads only the Mirror (QA Audit L-44). A failure here is therefore not explained by the new QA files.

Cleanup and recovery: none. Tracked files changed by the tests are listed at storage time (§4.4) and never committed.

### T04 `ac040-02-03-catalog-config` — Catalog, configuration and schemas

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T04`, attempt 1 |
| QA_STEP_ID | `ac040-02-03-catalog-config` (Plan §10 row 4; D3; AC040-02, AC040-03; K040-REQ-003 to K040-REQ-006; PF09.3 HDE-SEPA005.1, HDE-SEPA005.2) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 4 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (approval); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addendum 2.5 (Channel taxonomy) and Addenda 2.2 to 2.4 (C040-01 to C040-06 decisions) |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-53, L-54 and test group A (§4.4); EPIC / HDE-EPIC040 |
| Objective | Prove that the delivered catalog and mechanics configuration have the approved structure, and run the catalog, configuration and schema test group |
| Environment and target | ENV-C, `[C]`; the pytest run `[CP]`. Target: the local checkout |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t04`. Inputs: `catalog/channels_v1.json`, `catalog/magic10_mechanics_v1.json` |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 4 |
| `check_name` | `Catalog, configuration and schemas` |
| `pf_refs` | `PF09.3-Canon-HDE-Build-Checklist-Separation` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` Structural probe, embedded Python, a read-only JSON parse of the two files. It prints one line per structural predicate below with PASS or FAIL and the observed value, and exits 0 only if all hold. It reads fields defensively, so a shape difference prints a FAIL line rather than raising; a traceback is a probe malfunction. [Plan 1]
4. `[CP]` Pytest group A, the final decisive command. [Plan 2]

   ```bash
   python -m pytest -q -p no:cacheprovider -rs tests/config/test_registry_catalog_contract.py tests/config/test_magic10_contracts.py tests/config/test_manifest_schema.py tests/config/test_typed_bundles.py tests/config/test_alias_policy_enforcement.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_registry_report.py tests/config/test_registry_report_determinism.py tests/config/test_registry_report_indexing.py tests/compare/test_arrays_as_sets.py tests/m10/test_defs_order.py tests/m10/test_thresholds_rounding.py
   ```

5. Recording (§4.3).

Inputs and outputs: inputs are the two catalog files. Outputs are the probe's predicate lines and the pytest summary.

Predicates (Plan CHECK 4):

- `catalog/channels_v1.json` is an object whose key `channels` holds 36 rows. Each row has exactly the keys `centers`, `circuit_primary`, `domains`, `flags`, `gates`, `id`, `primary_domain` and `substream`. Each `gates` value is a pair whose first element is less than its second. The 36 pairs are unique. No value at any depth is null.
- `catalog/magic10_mechanics_v1.json` has `config_id` `m10-channel-state-v1.0.0` and `schema` `magic10_mechanics_config.v1`; 20 `signals` with unique `signal_id`; 3 `profiles` whose `profile_id` values are `activation_bp_v1`, `coherence_bp_v1` and `expression_bp_v1`; and 10 `category_weights`. Signal `equilibrium_score` has `operation` `twice_min_owner_mass_v1`, `counterweight_ratio` has `companionship_em_mass_v1`, and the other 18 signals have `weighted_state_sum_v1`.
- Command 4 exits 0.

Status:

- **PASS:** every predicate holds.
- **FAIL_TOOLING:** the probe ends with a traceback, or pytest exits 2, 3, 4 or a negative status.
- **TOOLING_BLOCKED:** T01 is not PASS; a listed file is missing; or pytest exits 5.
- **FAIL_BEHAVIOR:** a structural predicate is false, or pytest exits 1.

Cleanup and recovery: none.

### T05 `ac040-04-05-admission-identity` — Admission, pure core and release identity

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T05`, attempt 1 |
| QA_STEP_ID | `ac040-04-05-admission-identity` (Plan §10 row 5; D4; AC040-04, AC040-05; K040-REQ-007 to K040-REQ-009; PF09.3 HDE-SEPA005.3, HDE-SEPA005.4) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 5 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (approval); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addenda 2.12, 2.22, 2.27 |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-11, L-12 and test group B (§4.4); EPIC / HDE-EPIC040 |
| Objective | Prove that the complete release is intact and bound to the accepted OPS01 attestation, and run the admission, refusal-class, pure-core, determinism and identity test group |
| Environment and target | ENV-C, `[C]`; the pytest run `[CP]`. Target: the local checkout |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t05`. Inputs: `catalog/manifest.json`, `audit/ops/hde-epic040/ops01/SHA256SUMS`, `audit/ops/hde-epic040/ops01/attestation.json` (Plan §8 pre-existing inputs) |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 7 |
| `check_name` | `Admission, pure core and release identity` |
| `pf_refs` | `PF09.3-Canon-HDE-Build-Checklist-Separation` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` `python scripts/release_id_recompute.py --check-manifest-only`. Expected exit 0; it audits the bytes and size of all 45 members. Never run this script in any other mode. [Plan 1]
4. `[C]` `sha256sum catalog/manifest.json` [Plan 2]
5. `[C]` `bash -c 'cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS'`. Expected exit 0 with seven lines ending `: OK`; read-only. [Plan 3]
6. `[C]` Binding probe, embedded Python. [Plan 4] It reads `audit/ops/hde-epic040/ops01/attestation.json`, computes the SHA-256 of `catalog/manifest.json`, prints `release_id`, `manifest_sha256`, `source_commit`, `validation_result` and `release_admission`, and prints one PASS or FAIL line for each of four checks: `release_id` equals the digest; `manifest_sha256` equals the digest; `validation_result` is `PASS`; `release_admission` is `PR06R_B_FINAL_PASS`. It exits 0 only if all four hold.
7. `[CP]` Pytest group B, the final decisive command. [Plan 5]

   ```bash
   python -m pytest -q -p no:cacheprovider -rs tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/core/test_engine_core_purity.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_m10_symmetry_identity.py tests/runtime/test_identity.py tests/scripts/test_cut_release_manifest.py tests/reader_v1/test_release_pack.py
   ```

8. Recording (§4.3).

Inputs and outputs: inputs are the manifest, its 45 members and the OPS01 ledger. Outputs are the audit result, the digest, the ledger check, the binding lines and the pytest summary.

Predicates (Plan CHECK 5): commands 3, 5 and 7 exit 0; command 5 prints seven `OK` lines; command 6's four checks hold; and the digest command 6 computed equals command 4's.

Status:

- **PASS:** every predicate holds.
- **FAIL_TOOLING:** a command ends with a traceback, or pytest exits 2, 3, 4 or a negative status.
- **TOOLING_BLOCKED:** T01 is not PASS; an OPS01 file is missing (command 5 reports a missing file, or command 6 cannot open the attestation); or pytest exits 5 (N-10).
- **FAIL_BEHAVIOR:** command 3 prints `MANIFEST_ERROR:` and exits 1; the binding fails, including command 5 reporting `FAILED` for a file that is present; or pytest exits 1. Kronos confirms the classification of a ledger mismatch at QA-110.

Limits: OPS01 evidence is corroboration, not QA evidence, and the attestation is not rebuilt (Plan §2).

Cleanup and recovery: none.

### T06 `ac040-06-golden-comparison` — Read-only golden comparison

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T06`, attempt 1 |
| QA_STEP_ID | `ac040-06-golden-comparison` (Plan §10 row 6; D5; AC040-06; K040-REQ-010; PF09.3 HDE-SEPA005.4) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 6 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` §3 (mismatch mechanics verified against the code); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addendum 2.20 |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-06, L-07, L-08, L-15, L-50 and test group C (§4.4); EPIC / HDE-EPIC040 |
| Objective | Prove that the complete eight-case collection matches at the repository root through the canonical code, that the result repeats byte for byte, that a deliberate expected-value change is reported as a mismatch, and that nothing in the checkout changes |
| Environment and target | ENV-C, `[C]`; the pytest run `[CP]`. Target: the local checkout |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t06`. Input: `tests/fixtures/magic10/v1/goldens.json`. Between commands 4 and 11 nothing else may write inside the checkout (no editor saves, no other session and no QA-100 note); anything that does invalidates the non-mutation proof |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 13 |
| `check_name` | `Read-only golden comparison` |
| `pf_refs` | `PF09.3-Canon-HDE-Build-Checklist-Separation`, `PF01-Canon-HDE-Math-Spec` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log`; in the same directory `compare_match_run1.json`, `compare_match_run2.json`, `tmp_goldens_altered.json` and `compare_mismatch_report.json`. The four files are listed in `evidence_artifacts` and bound by SHA-256 lines |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` `mkdir -p audit/qa/hde-epic040/checks/ac040-06-golden-comparison` (Plan §12: a check creates its own directory before its first write).
4. `[C]` Before-digest, embedded Python: the tree digest of §4.3 with root `.` (the repository root), excluding the top-level `.git` directory, `audit/qa/hde-epic040`, and every directory named `__pycache__` or `.pytest_cache`. [Plan 1]
5. `[C]` `python tools/config/generate_config_artifacts.py --compare-goldens .`, with stdout sent to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json`. Expected exit 0. [Plan 2]
6. `[C]` The same command, with stdout sent to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json`. Expected exit 0. [Plan 3]
7. `[C]` Altered-input writer, embedded Python. [Plan 4] It loads `tests/fixtures/magic10/v1/goldens.json`; finds the case whose `case_id` is `M10-G001`; checks that its `expected.signals[0]` is `{"q": 0, "signal_id": "rapport_delta"}` and otherwise writes nothing and stops (`FAIL_TOOLING`); sets that `q` to `1`; and writes the document as JSON with sorted keys, compact separators and non-ASCII characters kept, plus one LF, to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`. It prints the SHA-256 of the original and the altered file and the one changed leaf.
8. `[C]` The mismatch run. Expected exit 1 and stderr `GOLDEN_COMPARISON_MISMATCH:` followed by the count. [Plan 5]

   ```bash
   python tools/config/generate_config_artifacts.py --compare-goldens . --goldens audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json --report /tmp/hde-epic040-qa/t06/compare_mismatch_report.json
   ```

9. `[C]` `cp /tmp/hde-epic040-qa/t06/compare_mismatch_report.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json` [Plan 5]
10. `[C]` `sha256sum /tmp/hde-epic040-qa/t06/compare_mismatch_report.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json` [Plan 5]
11. `[C]` After-digest, with the same code and scope as command 4, taken before any test runs so that only the comparator runs fall between the two digests. [Plan 6]
12. `[CP]` `python -m pytest -q -p no:cacheprovider -rs tests/config/test_config_artifacts.py` [Plan 7]
13. `[C]` Evaluator, embedded Python, the final decisive command. It reads the three repository JSON files, the captures of commands 4, 5, 6, 8, 10, 11 and 12, and `catalog/manifest.json`; prints one line per predicate below; and exits 0 only if all hold. [Plan 8]
14. `[C]` `python scripts/release_id_recompute.py --check-manifest-only`, run only when command 5, 6 or 8 refuses (exit 5) with a token other than `RAILS_CLOSED_REQUIRED` and `GOLDENS_INVALID`, to attribute the refusal. [Plan CHECK 6 TOOLING_BLOCKED rule]
15. Recording (§4.3).

If a comparator run exits 5, record its stderr token, run command 14 when it applies, complete the remaining commands so that the digests and the tests are still recorded, and classify by the status rules.

Inputs and outputs: inputs are the goldens fixture, the altered copy and the checkout. Outputs are two match reports, one mismatch report, two tree digests, the pytest summary and the evaluator's predicate lines.

Predicates (Plan CHECK 6):

- Commands 5 and 6 exit 0. Both reports have `ok` true, empty `mismatches`, and `cases` listing exactly `M10-G001` to `M10-G008`, each with `outcome` `match`; `config_id` is `m10-channel-state-v1.0.0` and `candidate_release_id` equals the SHA-256 of `catalog/manifest.json`. The two report files are byte-identical.
- Command 8 exits 1 and its stderr is `GOLDEN_COMPARISON_MISMATCH:` followed by a count of at least 2. The report has `ok` false; every row of `mismatches` has `case_id` `M10-G001`; one row has `path` `transcription.expected`; and cases `M10-G002` to `M10-G008` have `outcome` `match`.
- Command 12 exits 0.
- The digests of commands 4 and 11 are equal.
- Evidence integrity: the two digests command 10 prints are equal, and command 7 found the expected original value before its change.

Status:

- **PASS:** every predicate holds and the evaluator exits 0.
- **FAIL_TOOLING:** command 8 refuses with `GOLDENS_INVALID` (a QA input defect, eligible for a Moon Loop through QA-110); the report copy differs; command 7 finds a different original value; the evaluator malfunctions; or pytest exits 2, 3, 4 or a negative status.
- **TOOLING_BLOCKED:** T01 is not PASS; a comparator run refuses with `RAILS_CLOSED_REQUIRED`; a run refuses and command 14 exits 1 (modified members); or pytest exits 5.
- **FAIL_BEHAVIOR:** the root comparison mismatches, or refuses while command 14 exits 0; the altered collection is reported as a match; runs 1 and 2 differ; the mismatch names another case; the digests differ; or pytest exits 1.

Never run the comparator without `--compare-goldens` or `--check`; without a mode flag it writes (QA Audit L-07).

Cleanup and recovery: `/tmp/hde-epic040-qa/t06/` stays outside the repository. The four supplementary files are evidence and are not removed.

### T07 `ac040-07-gate-ingress-offline` — Gate ingress and readiness, offline

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T07`, attempt 1 |
| QA_STEP_ID | `ac040-07-gate-ingress-offline` (Plan §10 row 7; D6; AC040-07 offline part; K040-REQ-007, K040-REQ-011; PF09.3 HDE-SEPA005.3, HDE-SEPA005.5) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 7 and §5.2 ("Rails change inside a check") |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` §3 (refusal order verified against the code); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addendum 2.20 |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-09, L-10, L-50 and test group D (§4.4); EPIC / HDE-EPIC040 |
| Objective | Run the Gate normalization and rejection corpus and the readiness tool's tests, and prove the readiness command's typed refusals at runtime without a database, including that an unavailable dataset is never reported ready |
| Environment and target | ENV-C, `[C]`, with `DATABASE_URL` unset by the prefix; command 4 alone under `[C7]`; the pytest run `[CP]`. Target: the local checkout; no database or network is reachable |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t07`. The synthetic UUID `00000000-0000-0000-0000-000000000001` (QA Audit L-50) and the invalid value `00000000-0000-0000-0000-00000000000G` |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 8 |
| `check_name` | `Gate ingress and readiness, offline` |
| `pf_refs` | `PF09.3-Canon-HDE-Build-Checklist-Separation` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` `bash -c ': > /tmp/hde-epic040-qa/t07/empty_selection.txt'`. Creates the empty selection file outside the repository. [Plan 2 input]
4. `[C7]` `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-000000000001`. Expected exit 5, empty stdout, and a first stderr line that starts `RAILS_CLOSED_REQUIRED:`. [Plan 1]
5. `[C]` `python tools/bodygraph/check_magic10_gate_readiness.py --selection-file /tmp/hde-epic040-qa/t07/empty_selection.txt`. Expected exit 5, empty stdout, and first stderr line `READINESS_EMPTY_SELECTION`. [Plan 2]
6. `[C]` `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-00000000000G`. Expected exit 5, empty stdout, and first stderr line `READINESS_SELECTION_INVALID`. [Plan 3]
7. `[C]` `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-000000000001`. Expected exit 5, empty stdout, and first stderr line `READINESS_UNAVAILABLE`; the prefix leaves `DATABASE_URL` unset, so no report is possible. [Plan 4]
8. `[CP]` Pytest group D, the final decisive command. [Plan 5]

   ```bash
   python -m pytest -q -p no:cacheprovider -rs tests/bodygraph/test_gates.py tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py tests/bodygraph/test_check_magic10_gate_readiness.py
   ```

9. Recording (§4.3).

Rails: command 4 alone runs with `SAFE_MODE=0`; `ALLOW_NETWORK=0` stays and `DATABASE_URL` stays unset, so no live service is reachable. The header's `captured_env` shows the recorder's closed rails, and the body records command 4's posture, exit status and stderr token (Plan §5.2).

Inputs and outputs: inputs are the readiness tool, its four refusal inputs and the Gate test corpus. Outputs are four exit statuses with their stderr tokens and the pytest summary.

Predicates (Plan CHECK 7): commands 4 to 7 return the stated exit status and token with empty stdout; none prints a report; command 8 exits 0.

Status:

- **PASS:** every predicate holds.
- **FAIL_TOOLING:** a command ends with a traceback, or pytest exits 2, 3, 4 or a negative status.
- **TOOLING_BLOCKED:** T01 is not PASS, or pytest exits 5.
- **FAIL_BEHAVIOR:** a refusal is missing or wrong; any command prints a readiness report (`READY` or `NOT_READY`); or pytest exits 1.

Cleanup and recovery: the empty selection file stays in `/tmp/hde-epic040-qa/t07/`.

### T08 `ac040-04-09-compat-cli-offline` — Compat and CLI, local/offline

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T08`, attempt 1 |
| QA_STEP_ID | `ac040-04-09-compat-cli-offline` (Plan §10 row 8; D7; AC040-04 application boundary, AC040-09; K040-REQ-004, K040-REQ-008) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 8 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (approval); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` (no addendum beyond the Plan's own application) |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) test group E (§4.4); EPIC / HDE-EPIC040 |
| Objective | Run the eligibility, no-user boundary, AB/BA identity, CLI source, error parity, canonical-bytes and file-input tests |
| Environment and target | ENV-C; the pytest run `[CP]`. Target: the local checkout; no vendor |
| Dependencies | T01 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t08` |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 3 |
| `check_name` | `Compat and CLI, local/offline` |
| `pf_refs` | `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[CP]` Pytest group E, the final decisive command. [Plan CHECK 8]

   ```bash
   python -m pytest -q -p no:cacheprovider -rs tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_ab_ba_identity.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_abba_parity.py tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/cli/test_showcompat_sources.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py tests/artifacts/test_cli_text_artifacts_bom_lf.py tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py tests/runtime/test_emit_public_legacy_helper.py tests/epic003/test_meta_invocation_ok.py
   ```

4. Recording (§4.3).

Inputs and outputs: inputs are the 17 test files. Output is the pytest summary with skip reasons.

Status by the exit status of command 3 (Plan CHECK 8): 0 **PASS**; 1 **FAIL_BEHAVIOR**; 2, 3, 4 or negative **FAIL_TOOLING**; 5 **TOOLING_BLOCKED**. Also **TOOLING_BLOCKED** if a listed file is missing or T01 is not PASS.

Limits: proof class local/offline (PF19 §3.3). It does not prove live vendor behavior.

Cleanup and recovery: none.

### T09 `ac040-09-reader-http-in-process` — Reader, HTTP and transport, in-process

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T09`, attempt 1 |
| QA_STEP_ID | `ac040-09-reader-http-in-process` (Plan §10 row 9; D8; AC040-09; Reader v1 and v2 contracts) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 9 |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` (approval); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addenda 2.23 (Reader v2) and 2.25 (Reader v1 error envelope) |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-20 to L-23, L-25 and test group F (§4.4); EPIC / HDE-EPIC040 |
| Objective | Run the Reader v1 and v2 route tests (success, eligibility, refusal classes, admission refusal as 503 `ERR_M10_MANIFEST_MISMATCH`, and every non-POST method including CONNECT and QUERY on all three factories), the emitter and schema tests, transport proofs and keys-only logging tests |
| Environment and target | ENV-C; the pytest run `[CP]`. Target: in-process Flask test clients; no server, no database |
| Dependencies | T01 PASS. T10 depends on this task |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t09` |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 3 |
| `check_name` | `Reader, HTTP and transport, in-process` |
| `pf_refs` | `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log` only |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[CP]` Pytest group F, the final decisive command. [Plan CHECK 9]

   ```bash
   python -m pytest -q -p no:cacheprovider -rs tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_writer_transport.py tests/reader_v1/test_emitter.py tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/transport/test_a7_transport_proofs.py tests/compliance/test_log_shape_snapshot.py tests/compliance/test_logging_filter_keys_only_and_redactions.py
   ```

4. Recording (§4.3).

Inputs and outputs: inputs are the 15 test files. Output is the pytest summary with skip reasons.

Status by the exit status of command 3 (Plan CHECK 9): 0 **PASS**; 1 **FAIL_BEHAVIOR**; 2, 3, 4 or negative **FAIL_TOOLING**; 5 **TOOLING_BLOCKED**. Also **TOOLING_BLOCKED** if a listed file is missing or T01 is not PASS.

Limits: proof class in-process, a Flask test client with injected current rows. It is not live transport and not a live database. It supplies the admission-refusal and CONNECT/QUERY coverage that T10 cites.

Cleanup and recovery: none.

### T10 `sec-reader-http-live` — Security of the live production Reader route

| Field | Value |
| --- | --- |
| QA_TASK_ID | `HDE-EPIC040-QA90-T10`, attempt 1 |
| QA_STEP_ID | `sec-reader-http-live` (Plan §10 row 10; D9; Product Owner Q-1; AC040-09; K040-REQ-008, K040-REQ-013) |
| Base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md` §12 CHECK 10, §5.2 (ENV-S and the server declaration) |
| Overlays | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md` §3 (probe expectations verified against the code); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` Addenda 2.19, 2.23, 2.24, 2.25 |
| Review, audit, change | QA_PLAN_REVIEW v1.0 (APPROVE); QA_AUDIT v1.0 (`docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`) loci L-14, L-20 to L-28, L-50; EPIC / HDE-EPIC040 |
| Objective | Over real HTTP against the production factory `adapter.factory:create_app()`, prove that every request-shape, version, size and method refusal on `POST /api/reader` returns its governed envelope and headers, that dev routes refuse in production posture, and that no public response carries a secret, stack trace, Gate payload or internal diagnostic |
| Environment and target | ENV-S: the server under `[S]` (`APP_ENV=prod`, `PORT=8000`, closed rails, no `DATABASE_URL`, no vendor keys); every client command under `[C]`; the recording under `[S]` (N-08). Target: a loopback server on port 8000 built from the tested checkout; clients use `http://127.0.0.1:8000` (PF07 §2.2) |
| Dependencies | T01 PASS and T09 PASS |
| Setup and data | `mkdir -p /tmp/hde-epic040-qa/t10/req`. The request bodies below; the synthetic UUIDs of QA Audit L-50 |
| Executor | Nathan, or the delegated agent (§4.1) |
| Final decisive command | 38 |
| `check_name` | `Security of the live production Reader route` |
| `pf_refs` | `PF19-Canon-Glow-QA-Guide` |
| Evidence (NOT RUN) | `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log`; `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` (decisive captures); `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log` (supplementary, non-gating). Both files are listed in `evidence_artifacts` and bound by SHA-256 lines |

Request bodies, written by command 4 to `/tmp/hde-epic040-qa/t10/req/` (N-05, N-06). None ends with LF. The writer prints each file's size and SHA-256, which must equal this table.

| File | Bytes | Content | SHA-256 |
| --- | --- | --- | --- |
| `valid.json` | 93 | `{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002"}` | `b401dcb879a2153aa69229e4c119a11d647f52f0cc26ec1ae5ca3aee71bacd32` |
| `s07.json` | 8 | `{"a_id":` | `255bdd70c7fe12faa8d88b6aab14e571260c1bb24b02327e0411de25774173fc` |
| `s08.json` | 96 | The three bytes EF BB BF (a UTF-8 BOM), then the bytes of `valid.json` | `939730e29bfe84c60ca741ce009a5c34a7adfc9433b33d1185405c4e3d54c17a` |
| `s09.json` | 99 | `{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002","c":1}` | `9c895e6b83a83ad2ceb8533ff378f80d0a6fe017d487c6c017994c10c9db64c2` |
| `s10.json` | 93 | `{"a_id":"00000000-0000-0000-0000-00000000000A","b_id":"00000000-0000-0000-0000-000000000002"}` | `1b3fb4341182567b84d3634a5d2b28d1986fa9f8dd91bd4868e4a5317542f86d` |
| `empty.json` | 0 | No bytes | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `big.json` | 32,769 | The bytes of `valid.json`, then 32,676 space characters (0x20) | `45e66f1c25d1fc33ca1a6699013efe201cdc76f5591c394c9d05c7fc7e0191c8` |

Commands:

1. `[C]` `python --version`. Step-local readiness (§4.3).
2. `[C]` `python -c "import tools.qa.qa_harness, engine"`. Step-local readiness (§4.3).
3. `[C]` `mkdir -p audit/qa/hde-epic040/checks/sec-reader-http-live` (Plan §12).
4. `[C]` Request-body writer, embedded Python: writes the seven files of the table above and prints each name, size and SHA-256.
5. `[C]` Port check: `curl -sS -o /dev/null -w '%{http_code}' --max-time 5 http://127.0.0.1:8000/internal/version`. Expected exit 7 (nothing listening). Any HTTP status means port 8000 is in use: stop and record `TOOLING_BLOCKED` (port unavailable).
6. `[S]` Start the server in the background, with stdout and stderr to the server log, and write its PID to `/tmp/hde-epic040-qa/t10/server.pid`. Start it so that it keeps running across the following commands; in a tool whose shell ends after each invocation, start it detached (for example with `nohup`). [Plan 1; PF07 §10.1]

   ```bash
   python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 30 > audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log 2>&1 &
   ```

7. `[C]` Service readiness: `curl -sS -o /dev/null -w '%{http_code}' --max-time 2 http://127.0.0.1:8000/internal/version`, repeated at one-second intervals, at most 30 times, until it prints `200`. Record the number of attempts and the last result. If it never prints `200`, stop the server (commands 35 and 36) and record `TOOLING_BLOCKED`. [Plan 1]

**Commands 8 to 33.** `[C]` Probes S-01 to S-26, one curl command each, in the order of the probe table below: S-01 is command 8 and S-26 is command 33. [Plan 2] Every probe uses these common options, shown here for S-01:

```bash
curl -sS --max-time 20 -D /tmp/hde-epic040-qa/t10/S-01.hdr -o /tmp/hde-epic040-qa/t10/S-01.body -w '%{http_code}' 'http://127.0.0.1:8000/internal/version'
```

Each probe uses its own ID in the two file names and keeps curl's stdout (the status code), stderr and exit status as `S-01.code`, `S-01.err` and `S-01.rc`, and likewise for every probe. "POST options with" a file means `-H 'Content-Type: application/json; charset=utf-8' -H 'Expect:' --data-binary @/tmp/hde-epic040-qa/t10/req/` followed by the file name.

34. `[C]` JSONL assembly, embedded Python: writes `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` with one line per probe, in probe order. [Plan 2] Each line is an object with exactly the keys `probe_id`, `method`, `target`, `request_body_bytes`, `request_body_sha256`, `status`, `headers` and `body`:
    - `method`: the HTTP method sent;
    - `target`: the path and query string;
    - `request_body_bytes` and `request_body_sha256`: the size and SHA-256 of the body file sent, or 0 and the SHA-256 of empty input when no body was sent;
    - `status`: the integer status curl printed;
    - `headers`: the final response's header lines, in order, as two-item lists of the name in lower case and the value verbatim, without the line end and the separating space;
    - `body`: the response body decoded as UTF-8, or `""` when empty.

    Each line is JSON with sorted keys and compact separators, followed by LF.
35. `[none]` Stop the server: `kill -TERM` the PID in `/tmp/hde-epic040-qa/t10/server.pid`. Record its exit status where the shell can observe it (`wait`); otherwise record it as not observable. [Plan 3]
36. `[C]` Port closed: command 5's curl command again. Expected exit 7. [Plan 3]
37. `[C]` Non-empty rule (Plan §12): `bash -c 'test -s audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log || printf "no server output\n" > audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log'`
38. `[C]` Evaluator, embedded Python, the final decisive command. It reads `http_probes.jsonl` and `catalog/manifest.json`, prints one line per predicate, and exits 0 only if all hold. [Plan 4]
39. Recording under `[S]` (§4.3, N-08).

Probes (Plan CHECK 10; expected results unchanged):

| Probe | Method | curl request options besides the common ones | URL | Expected |
| --- | --- | --- | --- | --- |
| S-01 | GET | none | `http://127.0.0.1:8000/internal/version` | 200; `release_id` equals the SHA-256 of `catalog/manifest.json` (`build_commit` is a static literal, not source identity) |
| S-02 | POST | POST options with `valid.json` | `http://127.0.0.1:8000/api/reader?v=1` | 503 `ERR_M10_RESOLVER_UNAVAILABLE` |
| S-03 | POST | POST options with `valid.json` | `http://127.0.0.1:8000/api/reader?v=2` | 503 `ERR_M10_RESOLVER_UNAVAILABLE` |
| S-04 | POST | POST options with `valid.json` | `http://127.0.0.1:8000/api/reader` | 400 `ERR_READER_INVALID_VERSION` |
| S-05 | POST | POST options with `valid.json` | `http://127.0.0.1:8000/api/reader?v=3` | 400 `ERR_READER_INVALID_VERSION` |
| S-06 | POST | POST options with `valid.json` | `http://127.0.0.1:8000/api/reader?v=1&v=2` | 400 `ERR_READER_INVALID_VERSION` |
| S-07 | POST | POST options with `s07.json` | `http://127.0.0.1:8000/api/reader?v=1` | 422 `ERR_READER_INVALID_INPUT` |
| S-08 | POST | POST options with `s08.json` | `http://127.0.0.1:8000/api/reader?v=1` | 422 `ERR_READER_INVALID_INPUT` |
| S-09 | POST | POST options with `s09.json` | `http://127.0.0.1:8000/api/reader?v=1` | 422 `ERR_READER_INVALID_INPUT` |
| S-10 | POST | POST options with `s10.json` | `http://127.0.0.1:8000/api/reader?v=1` | 422 `ERR_READER_INVALID_INPUT` |
| S-11 | POST | POST options with `empty.json` | `http://127.0.0.1:8000/api/reader?v=1` | 422 `ERR_READER_INVALID_INPUT` |
| S-12 | POST | POST options with `big.json` | `http://127.0.0.1:8000/api/reader?v=2` | 422 `ERR_READER_INVALID_INPUT` |
| S-13 | POST | `-H 'Transfer-Encoding: chunked'` and POST options with `big.json` | `http://127.0.0.1:8000/api/reader?v=2` | 422 `ERR_READER_INVALID_INPUT` |
| S-14 | GET | none | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-15 | HEAD | `--head` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; no body |
| S-16 | OPTIONS | `-X OPTIONS` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-17 | PUT | `-X PUT` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-18 | PATCH | `-X PATCH` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-19 | DELETE | `-X DELETE` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-20 | TRACE | `-X TRACE` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-21 | PROPFIND | `-X PROPFIND` | `http://127.0.0.1:8000/api/reader?v=2` | 405; `Allow: POST`; the ERR_NOT_FOUND body below |
| S-22 | GET | none | `http://127.0.0.1:8000/reader?v=1&a=x&b=y` | 403 `ERR_READER_FORBIDDEN` |
| S-23 | GET | none | `http://127.0.0.1:8000/dev/reader/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-24 | GET | none | `http://127.0.0.1:8000/dev/sampler/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-25 | GET | none | `http://127.0.0.1:8000/dev/writer/conjunction` | 403 `ERR_WRITER_FORBIDDEN` |
| S-26 | GET | none | `http://127.0.0.1:8000/api/reader/missing` | 404 HTML (known limitation O-P06a-22; observed, not failed) |

URLs are passed in single quotes. The ERR_NOT_FOUND body is exactly `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` followed by one LF. The `code` of S-02 to S-25 is the body's top-level `code`.

Predicates, checked by the evaluator (Plan CHECK 10):

- **E1.** The server became ready at command 7, and every probe S-01 to S-26 appears exactly once in `http_probes.jsonl` with a non-zero status.
- **E2.** Each probe returns its expected status and code from the probe table. S-14 to S-21 have header `allow` equal to `POST`; S-14 and S-16 to S-21 have the ERR_NOT_FOUND body exactly; S-15 has an empty body.
- **E3.** For S-02 to S-25, `content-type` is `application/json; charset=utf-8`, `cache-control` is `no-store`, and there is no `etag` header.
- **E4.** For S-02 to S-22 except S-15, the body is a JSON object with exactly the keys `code`, `error`, `ok` and `schema`, with `ok` false and `schema` `"v1"`, and the body equals its canonical form (sorted keys, compact separators) followed by exactly one LF.
- **E5.** Across S-01 to S-26, no body and no header value contains `Traceback`, `File "`, `psycopg` or `postgresql`; no JSON body has a key `gates` at any depth, and no other body contains the text `"gates"`; and no Reader error body (S-02 to S-22) contains a JSON number, meaning an integer or float that is not a boolean.

Status:

- **PASS:** the server became ready, every probe was captured, E1 to E5 hold, and the evaluator exits 0.
- **FAIL_TOOLING:** a capture is malformed or missing after its probe ran (no status code, an unreadable header block, or an absent body file); the JSONL cannot be assembled; or the evaluator malfunctions. A non-zero curl exit status with a complete capture is written in the body and does not by itself change the status.
- **TOOLING_BLOCKED:** T01 or T09 is not PASS; port 8000 is in use (command 5); or the server never becomes ready (command 7: connection refused, HTTP 000 or a non-HTTP response).
- **FAIL_BEHAVIOR:** the server is reachable and a probe contradicts its expected status, code, envelope, header or leak predicate (PF19 §3.5.10).

Limits and nonclaims: no deployed-service, live-database or admission-refusal-over-live-HTTP claim. Admission-refusal propagation and CONNECT and QUERY coverage come from T09 and are cited, not repeated.

Cleanup and recovery: commands 35 and 36 run on every path, including early stops, so that the server is stopped and port 8000 is closed. The request bodies stay in `/tmp/hde-epic040-qa/t10/`.

## 6. CANON_CONFLICT_REGISTER (carried)

One register, carried from QA Audit v1.0 §11. C040-01 to C040-08 are copied unchanged. C040-09 is updated with its QA-70 decision; its full history is the proposal in QA Audit v1.0 §11 and the decision in QA Plan Review v1.0 §4. QA-90 decides nothing in this register.

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
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks") | **APPROVED**, alternative (a) as proposed: PF19 and PF27 govern the execution rail and plan shape. Rejected alternative: (b) forbid all git reads and embedded helpers, which loses the tested-source attribution PF19 §10.8 requires. Scope: this QA Plan and its tasks only | Isis-50 at QA-70; reviewed QA_PLAN v1.0 and QA_AUDIT v1.0; 2026-09-27. Rationale: PF07 §2.8 itself routes the execution rail to PF19, and PF19 §10.8 requires tested-source attribution | Read-only git observations for attribution only, never a PASS gate; no script file; existing harness APIs through embedded Python. T01 to T10 follow it (N-02). Residual risk: a reader applying PF07 §2.8 literally until it is drained | PF07 §2.8 wording; PF07 maintainer; documentation drainage, non-gating (Plan DD-02) | Proposal: QA Audit v1.0 §11, 2026-09-27, PROPOSED. Decision: QA Plan Review v1.0 §4, 2026-09-27, APPROVED |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013).

## 7. Constraints, open inputs and unresolved items

| Item | Source | State in this collection | Owner |
| --- | --- | --- | --- |
| Check 11 carries the Product Owner's synthetic-tuple confirmation | QA-70 §5, §6 item 1 | Not applicable here (check 11 not selected); carried to check 11's future task | Product Owner; Kronos at a later QA-90 |
| The QA-90 task names the evidence branch and any execution-agent delegation | QA-70 §6 item 2 | Branch named (§4.4). Delegation: none supplied, so Nathan executes (Plan §6); the binding for a later delegation is in §4.1 | Kronos (done); Product Owner (delegation choice) |
| Checks 11 to 14 stay Product Owner-executed | QA-70 §6 item 3; Plan §7.1 | Carried; no task issued here | Product Owner |
| Python 3.12 in the venue | §4.1; QA Audit QA50-F08 | Open environment precondition for T01 | Nathan (environment) |
| Check 15 outputs: path proofs, doc-delta append, manifest verification, governed-graph non-interference, coverage accounting | §3 effect 1 | Owed until check 15 is selected | Product Owner selection; Kronos |
| One checkout for all fifteen checks | §3 effect 3; Plan §7.1 | Open for later selections | QA-110 |
| QA50-F01, Index and Mirror registration of QA evidence | QA-70 §7 | Unchanged; blocks only a ledger-bound manifest claim | Evidence owner, through the whole-change IA PR route |
| QA50-F05, selection of existing current rows | QA-70 §7 | Unchanged; needed by checks 12 and 14 | Product Owner |
| QA50-B01, `--allow-prod-vendor` gap | QA-70 §7 | Unchanged; non-blocking | PF05 and CLI owners |
| DD-01 to DD-12 | Plan §9.1 | Recorded by T02; non-blocking | Named owners |
| N-05, probe S-10 input | §4.6 | Informational for QA-110; no Plan change needed | Kronos |

## 8. Working state

```text
QA-90 working state, HDE-EPIC040, 2026-09-27
- Selection: checks 1 to 10 (Product Owner). Issued: T01 to T10, attempt 1, all NOT RUN.
- Not selected: checks 11 to 15. No task, no attempt.
- Dependencies: T02 on T01 recorded (any status); T03 to T09 on T01 PASS; T10 on T01 PASS and T09 PASS.
- Reruns issued: none. Material findings: none. Normalizations: N-01 to N-11.
- Next: QA-100 in a new dedicated session, then QA-110 in the continuing Kronos session.
```

## 9. Nonclaims

This collection establishes no QA PASS, acceptance, closure, PF09 status movement, PF-Canon or PF10 edit, deployment, release activation, token, Index or Mirror publication, or ledger-bound manifest. Issuing a task is not executing it, and a task's evidence paths are not evidence until QA-100 produces them.

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-90-20260927-01
  change: EPIC / HDE-EPIC040 (Specification v1.1, docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md)
  work_units: QA_TASK HDE-EPIC040-QA90-T01 to HDE-EPIC040-QA90-T10 for QA_PLAN v1.0 checks 1 to 10
  prompt: QA-90 — Create Bounded QA Execution Task — 091426.1; Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z; release GCFPE-20260914.1; registry lifecycle ACTIVE
  role_stage: continuing Kronos, QA-90
  capture_time: 2026-09-27T10:51:17Z
  execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  result: QA_TASK collection v1.0, TASK_READY, routed to QA-100
  task_and_attempt_mapping: T01 to T10 map to checks 1 to 10 at attempt 1; result mapping pending until QA-100 runs
  earlier_uses: GCFPE-USE-HDE-EPIC040-QA-50-20260927-01 (QA Plan v1.0 and QA Audit v1.0); GCFPE-USE-HDE-EPIC040-QA-70-20260927-01 (QA Plan Review v1.0)
  repository_persistence: PENDING / NON_GATING (docs/changes/GCFPE_PROMPT_PROVENANCE.md is not installed; owner: the authorized repository writer once that procedure is installed)
```

## Handoff

```text
NEXT_PROMPT_HANDOFF

Run QA-100 — Execute Bounded QA Task — 091426.1
https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848

Receiver: the authorized environment operator for HDE-EPIC040 QA, in a new dedicated QA-100 session that Nathan creates (session_disposition: NEW_DEDICATED). Executor authority and delegation are set in the task collection §4.1.
Change: EPIC / HDE-EPIC040 / Separation Pass 3. Execution posture: MANUAL_PROMPT_EXECUTION.
Tasks: HDE-EPIC040-QA90-T01 to HDE-EPIC040-QA90-T10 (QA_PLAN v1.0 checks 1 to 10, attempt 1), in that order.

Inputs:
- docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.0.md — QA_TASK collection v1.0, TASK_READY: execution instructions, evidence boundary and return
- docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md — QA_PLAN v1.0, the approved base (immutable)
- docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md — QA_PLAN_REVIEW v1.0, APPROVE; overlay with the C040-09 decision and QA-90 constraints
- docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md — QA_AUDIT v1.0, the audit-proven loci the tasks cite
- docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md — LIVE_QA_GUIDE v1.0, GUIDE_READY lineage
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md — current PF10; overlay addenda cited per task
```
