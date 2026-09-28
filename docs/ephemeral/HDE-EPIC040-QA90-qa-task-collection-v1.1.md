---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-EPIC040-QA90-QA-TASK-COLLECTION
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.0.md (tasks for QA Plan v1.0 under the rejected QA-70 review v1.0; not carried forward per the Alpha state record v1.0; preserved unchanged; SHA-256 a973f7f59499497c746074d2a912e5b17c720ff71fa98c85dbeaee9385c66698)
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-90 / QA_PLAN v1.2 checks 1 to 10
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 091426.1 (Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; 938 lines, 129,319 bytes; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (QA_PLAN_REVIEW v1.4, APPROVE by Isis-52, 2026-09-28T00:26:24Z; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0; SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df)
selection: Product Owner, "Tasks: 1-10" in the QA-90 handoff of 2026-09-28 = QA Plan v1.2 checks 1 to 10
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919)
observed_revision: 53449c96a42a6fdbc61ab272ff248394b58df62c (origin/main at authoring; no file outside `docs/ephemeral/` changed since `8eb4ce0`, the revision the approving review observed)
routing: QA-100 — Execute Bounded QA Task — 091426.1, in the authorized environment/operator session
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
---

# HDE-EPIC040 — QA Task Collection v1.1 (QA-90): checks 1 to 10 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Tasks | T01 to T10, one per selected check, each at attempt 1 (§4.2) |
| Selection | Product Owner "Tasks: 1-10" = Plan v1.2 checks 1 to 10; checks 11 and 12 are not selected (§3) |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING`: every selected block is complete and resolves to current repository loci (§2.5) |
| Normalizations | N-01 to N-19 (§4.9). Each keeps the Plan's objective, target, rails, evidence identity and predicates |
| Evidence storage | Branch `qa/hde-epic040-qa100-plan-v1.2`, evidence files only, pushed, no pull request by the executor (§4.7) |
| Next stage | QA-100 — Execute Bounded QA Task — 091426.1, in the operator session the Product Owner opens with the handoff of this collection |
| Not done by QA-90 | Execution, evidence acceptance, a PASS declaration, selection of any step, a rerun, merge, PF-Canon or PF10 edits, addendum production |

## Canon relied on

Read from `docs/pfcanon/` on `main` at `53449c9`. `docs/pfcanon/` at `53449c9` is identical to `e1ab8ba`, where Plan v1.2 read it (empty `git diff`).

- **HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`, the version read): the addenda listed in Plan v1.2 §1 and §2.2, relied on as the Plan records them; 2.27 "HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.4", section "Evidence storage" (an evidence branch published without merge, the precedent for §4.7); 2.29 "PF10-CANON-001" (canon location; change documents in `docs/ephemeral/`). A search at this invocation for `QA-90`, `QA_TASK`, `bounded QA task`, `attempt 2`, `evidence branch`, `evidence storage` and `QA-100` found no rule for QA task packaging, attempt numbering or QA evidence storage, so the Glow QA Guide and Plan Templates govern them.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`), each read in full at this invocation: §3.4.7 (objective-first steps; in-flight syntax normalization; exact executed command recorded); §3.4.9 (Plans confer no commit, push or pull-request authority; storage uses separately authorized lanes; tested state distinct from a later evidence-storage commit); §3.4.10 (plan validity lint; operation normalization; QA-created evidence-capture harnesses); §9.2.15.5 (complete selected membership; attempt counts; task-authoring normalization is not an attempt); §10.6 (a first eligible fault needs Kronos's QA-110 decision before QA-90 attempt 2; a second failure, behavior defect or invalid Plan goes to ESC-10). Relied on as read in full at QA-80: §3.3; §3.4.8; §3.5.5 to §3.5.7; §4.3; §4.4.1 to §4.4.7; §10.8; §11.1.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Step-log header schema expectations (required; v2)", including the closed status set, the exact status predicates and the causal precedence (re-read at this invocation); "Check Blocks" and "Template-safe placeholders and omission syntax", as read at QA-80.
- **Technical Writing Best Practices** (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`): "Truth and source fidelity" (read every relied-on source completely; unknown stays unknown; no invented paths, commands, flags or identities).

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, QA_PLAN v1.2, approved by `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`. Read in full at this invocation. This collection packages checks 1 to 10 of that Plan; it rewrites none of its content.

### 2.2 Overlays

| Overlay | Repository path | Effect on these tasks |
| --- | --- | --- |
| PF10 addenda | `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md` | The addenda that Plan v1.2 §1 and §2.2 list. No addendum was added after the Plan's approval |
| QA-70 review v1.4 execution notes | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md` §6, §7 | N-103: the delegation record names the executor and states that it runs in the PO's QA console (§4.1). N-104: each task states its attempt number and the treatment of the `06b04a9` attempts (§4.2). N-101 and N-102 concern check 11, which is not selected; they are carried to the task for check 11 (§7). N-105: none |
| Alpha state record v1.0 | `docs/ephemeral/HDE-EPIC040-alpha-state-stopped-failed-at-qa-v1.0.md` | The QA-90 task collection v1.0 and the checks 1 to 10 evidence of `06b04a9` are not carried forward (§4.2) |
| Approval revocation v1.0 | `docs/ephemeral/HDE-EPIC040-QA70-approval-revocation-v1.0.md` | The QA-70 review v1.2 approval is revoked and its QA-90 handoff is void; nothing here derives from them |

### 2.3 Aids (not overlays)

- `docs/ephemeral/HDE-EPIC040-QA80-redline-application-report-v1.1.md` (SHA-256 f05fc1fed20245c2281482013e70a42ee1c17d667923d3475bb32baf9a78dcc2): the v1.1 to v1.2 renumbering, used to confirm that checks 1 to 10 keep their v1.1 identities.
- `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`: loci L-07, L-09, L-13, L-20 to L-28, L-41, L-42, L-50, L-51, L-53, L-54, as Plan v1.2 cites them.
- `docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md` (SHA-256 713e8c1f8c913ec13a59d18a17bb5a697b7cc4fc7ab3ff7635783012da204682): Q-1 (the security step, check 10 here) and Q-2 (the vendor step, check 11, not selected).
- `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.0.md`: format lineage only. No task, normalization, path or result of v1.0 is reused by reference; every instruction below is derived from Plan v1.2.

### 2.4 Read-only repository observations at `53449c9` (authoring aids, not QA evidence)

- The 70 test files of pytest groups A to G, every tool, script and CI check that checks 1 to 10 invoke, `audit/ops/hde-epic040/ops01/SHA256SUMS` (7 lines), `audit/ops/hde-epic040/ops01/attestation.json` and `tests/fixtures/magic10/v1/goldens.json` exist. `audit/qa/hde-epic040/` does not exist on `main`.
- `catalog/manifest.json` SHA-256 is 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96 (as review v1.4 §5 records).
- `requirements.txt` pins `gunicorn>=21,<22`; `pyproject.toml` declares `hdctl = "engine.cli.main:cli"`.
- The `showcompat` flags `--source`, `--birthdate-a`, `--birthtime-a`, `--location-a`, `--birthdate-b`, `--birthtime-b`, `--location-b`, `--dump-reader` are defined in `engine/cli/main.py`; `--compare-goldens`, `--goldens`, `--report` in `tools/config/generate_config_artifacts.py`; `--user-id`, `--selection-file` in `tools/bodygraph/check_magic10_gate_readiness.py`; `--check-manifest-only` in `scripts/release_id_recompute.py`.
- `adapter/http_reader.py` sets `_READER_MAX_BODY_BYTES = 32_768`, reads at most one byte past it, and accepts an identity only through `strict_canonical_uuid`, whose pattern is lower-case hexadecimal only (`engine/bodygraph/projection.py`).
- The readiness tool writes its refusal code as one line on standard error and exits 5; an empty selection file gives `READINESS_EMPTY_SELECTION`.
- The comparator writes `GOLDEN_COMPARISON_MISMATCH:<n>` on standard error and exits 1 on a completed mismatch. `tests/fixtures/magic10/v1/goldens.json` is canonical JSON (sorted keys, compact separators, non-ASCII characters unescaped, one trailing LF), and case `M10-G001` `expected.signals[0]` is `{"q": 0, "signal_id": "rapport_delta"}`.
- `tools/qa/qa_harness.py`: `CheckResult` requires `exit_code` exactly when a command is recorded, a non-empty reason for every non-PASS status, `exit_code` 0 for PASS, `pf_refs` matching the in-document PF title pattern, and `captured_env` keys among `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`.

Authoring dry-runs (Kronos, in a scratch copy of the tree outside the repository, with no product code executed and no QA evidence produced): the ten recording invocations of §5 published primary logs and a manifest for the PASS, FAIL_BEHAVIOR and not-executed TOOLING_BLOCKED shapes; the Step-0B writer of T02 produced two byte-identical surfaces with twelve DD rows; the altered-input writer of T06 produced a file that differs from the fixture in exactly one byte; the probe-body commands of T10 produced the stated byte counts; and the JSONL assembler of T10 wrote 22 LF-terminated lines from synthetic captures. These dry-runs test instruction syntax only. They are not executions of any check.

### 2.5 Pre-execution assessment

Isis-52 approved exactly Plan v1.2 (review v1.4 front matter, `reviewed_plan` SHA-256 equal to the base above). Every selected check is inside the Plan's scope (Plan §2, §10). Every command, test file, flag and entrypoint the ten blocks use exists at `53449c9` (§2.4). No selected block has a substantive defect that survives faithful normalization; the normalizations of §4.9 change no objective, target, rails, evidence identity or predicate.

### 2.6 Carried lineage

- Attempt lineage: §4.2.
- `CANON_CONFLICT_REGISTER`: §6, carried unchanged from Plan v1.2 §2.3; QA-90 adds no entry.
- PR lineage: Plan v1.2 carries no `PR_RETURN_PHASE`; none is created here.
- Deferred requirements (live Gate readiness; live DB Reader success): Plan v1.2 §2. They are not checks and have no task.

## 3. Selection reconciliation

The Product Owner's selection "Tasks: 1-10" names members by the only numbering the approved Plan defines: its check numbers 1 to 12 (Plan §10, §11). Tasks T01 to T10 are Plan checks 1 to 10 in Plan order.

| Plan # | `check_id` | Selected | Task | Attempt | Executor | Depends on (must be PASS unless stated) | Ready at authoring |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Yes | T01 | 1 | Q | none | Yes |
| 2 | `step-0b-doc-delta-capture` | Yes | T02 | 1 | Q | `d0-discovery` executed, any status, with a primary log | Waits on T01 |
| 3 | `ac040-08-evidence-validators` | Yes | T03 | 1 | Q | `d0-discovery` | Waits on T01 |
| 4 | `ac040-02-03-catalog-config` | Yes | T04 | 1 | Q | `d0-discovery` | Waits on T01 |
| 5 | `ac040-04-05-admission-identity` | Yes | T05 | 1 | Q | `d0-discovery` | Waits on T01 |
| 6 | `ac040-06-golden-comparison` | Yes | T06 | 1 | Q | `d0-discovery` | Waits on T01 |
| 7 | `ac040-07-gate-ingress-offline` | Yes | T07 | 1 | Q | `d0-discovery` | Waits on T01 |
| 8 | `ac040-04-09-compat-cli-offline` | Yes | T08 | 1 | Q | `d0-discovery` | Waits on T01 |
| 9 | `ac040-09-reader-http-in-process` | Yes | T09 | 1 | Q | `d0-discovery` | Waits on T01 |
| 10 | `sec-reader-http-live` | Yes | T10 | 1 | Q | `d0-discovery`, `ac040-09-reader-http-in-process` | Waits on T01 and T09 |
| 11 | `open-rails-showcompat-vendor` | No | none | not started | P, with Q recording | `d0-discovery`, `ac040-04-09-compat-cli-offline` | Not selected: NOT RUN |
| 12 | `qa-closeout-deliverables` | No | none | not started | Q | every other check recorded, any status | Not selected: NOT RUN |

Counts: 12 Plan checks; 10 selected; 10 tasks, all attempt 1; 0 conditional; 2 not selected. The deferred requirements of Plan §2 are not checks and are not counted.

Consequences of the partial selection, for QA-110 and the Product Owner: check 11 depends on checks 1 and 8 of this collection, and check 12 runs only after checks 1 to 11 are recorded. Until both are selected and executed, the QA-120 coverage accounting cannot mark them COVERED (Glow QA Guide §9.2.15.5), and the QA console checkout of §4.3 must be kept, because Plan §7.1 requires all twelve checks in one checkout.

## 4. Common execution contract

### 4.1 Executor, delegation and venue (Plan §6, §7.1; review v1.4 N-103)

Delegation record:

- Executor: the operator session in which the Product Owner runs QA-100 — Execute Bounded QA Task — 091426.1 with the handoff of this collection. QA-100 names that operator "the authorized environment or DevOps operator, not Kronos". It is the Plan's QA/infra executor for T01 to T10, acting in the repository's QA/Verifier role (`AGENTS.md`). It is neither the Product Owner nor Kronos.
- Delegating act: the Product Owner's selection "Tasks: 1-10" and the Product Owner opening that QA-100 session with this handoff. This record states that delegation; it creates no authority beyond it.
- Execution identity: PENDING at QA-90, because the session does not exist yet. T01 records it as the first line of its `=== CONTEXT ===` section (the session URL, or the operator's name), and the QA-100 result records it. If no identity can be recorded, no task runs (Plan §6).
- Venue: the executor runs in the Product Owner's QA console: the GitHub Codespace for `amthorn78/glow-hdengine-v2` (preferred), or the Product Owner-controlled Linux shell of the Plan front matter. It works in the one QA checkout of §4.3, where check 11's recording will later read the PO's `/tmp` files and write into the same QA root.
- Capability: none of T01 to T10 makes a vendor call, handles a secret value or connects to a database, so an automated execution agent may be the executor (Plan §7.1). Secret-bearing variables are only reported SET or UNSET and are unset for every command (§4.4).

### 4.2 Attempts and the `06b04a9` attempts (Plan §7.3; review v1.4 N-104)

- Every task in this collection is attempt 1 under Plan v1.2 (Plan §7.3: "Attempt 1 is the QA-90 task's first execution of a check").
- Treatment of the `06b04a9` attempts (Kronos, at QA-90, as N-104 requires): checks 1 to 10 were executed under Plan v1.0 in commit `06b04a9` on branch `qa/hde-epic040-qa100-checks-1-10`, from the task collection v1.0, under the QA-70 review v1.0 that the Product Owner rejected. The Alpha state record v1.0 does not carry that collection or that evidence forward. They are therefore not attempts of these tasks: they are not counted toward the one-rerun limit, not reused as evidence, not copied as `attempt1_primary.log`, and not deleted. They remain historical records on their own branch. Kronos records this treatment again in the QA-110 result.
- Attempt 2 of any task exists only through Kronos's QA-110 decision and a new QA-90 task (Plan §7.3; Glow QA Guide §10.6). Task authoring and syntax normalization are not attempts (Glow QA Guide §9.2.15.5).

### 4.3 Setup before T01 (not a check)

1. Scratch root: `test -e /tmp/hde-epic040-qa-v1.2` must exit 1 (absent). If it exists, stop and report it; do not delete it. Then `mkdir -p` these eleven directories: `/tmp/hde-epic040-qa-v1.2/d0-discovery`, `/tmp/hde-epic040-qa-v1.2/step-0b-doc-delta-capture`, `/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators`, `/tmp/hde-epic040-qa-v1.2/ac040-02-03-catalog-config`, `/tmp/hde-epic040-qa-v1.2/ac040-04-05-admission-identity`, `/tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison`, `/tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline`, `/tmp/hde-epic040-qa-v1.2/ac040-04-09-compat-cli-offline`, `/tmp/hde-epic040-qa-v1.2/ac040-09-reader-http-in-process`, `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes`, `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies`. The scratch root is outside the repository and is never committed.
2. QA checkout: a fresh clone of `main`, made with umask 022 so that tracked files are created with mode 644, in a new directory. In Codespaces: `sh -c 'umask 022 && git clone https://github.com/amthorn78/glow-hdengine-v2.git /workspaces/hde-epic040-qa'`. In the other venue: the same command with the target `$HOME/hde-epic040-qa`. Reason: the Plan front matter shows that group G's file-mode assertion depends on the checkout mode of `docs/evidence/INDEX.sha256`, and a mode of 644 makes that assertion verdictable at attempt 1 instead of `TOOLING_BLOCKED`. The mode is still recorded as venue evidence in T03. Do not reuse an existing checkout, and do not check out branch `qa/hde-epic040-qa100-checks-1-10`.
3. Work from the root of that checkout for every command of §5. Do not switch branches, pull, rebase, stash, restore or clean the checkout at any time before §4.7. The tested source is the checkout's `HEAD`, expected to be `53449c96a42a6fdbc61ab272ff248394b58df62c` or a later `main` commit; T01 records it, and a later commit is recorded, not refused (Plan §5.3).
4. Keep the checkout, the virtual environment and the scratch root after T10: check 11 and check 12 must run in this checkout (Plan §7.1).

### 4.4 Rails prefixes (Plan §5.2; normalization N-01)

Two literal prefixes, defined once here and written in full in each command as run. They apply the closed posture per command, so a shell that does not keep exported variables still runs every command under the same rails.

- CLOSED prefix, for every command marked [C]: `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`
- PYTEST prefix, for every command marked [P]: the CLOSED prefix followed by `PYTHONDONTWRITEBYTECODE=1` (Plan §5.2, the CI lane posture).
- Commands marked [N] run without a prefix; only T01 commands 1 and 2 are [N], because they record the console's state before any change.

With the virtual environment first on `PATH`, `python` and `hdctl` resolve to it (N-02). No other variable is introduced. Rails never change inside a task, and T01 to T10 all use the closed posture.

### 4.5 Readiness line and dependency gate (Plan §11, §12 common rules)

Dependency gate (T03 to T10), before anything else in the task: [C] `python -m json.tool audit/qa/hde-epic040/qa_step_logs_manifest.json`, stdout to `gate.out`. Read the `status` of each dependency the task names. If any is not `PASS`, run nothing else: record the check `TOOLING_BLOCKED` with a reason naming the dependency and its recorded status (for example `dependency d0-discovery is FAIL_TOOLING`), `argv.txt` holding only the gate command and `final.rc` its exit code (N-05). T02's gate is `test -s audit/qa/hde-epic040/checks/d0-discovery/primary.log` (T01 executed, any status).

Readiness line (T02 to T10), after the gate and before the behavior commands:

- R1 [C] `python --version`. Expected: `Python 3.12.` followed by the patch number.
- R2 [C] `python -c "import sys, tools.qa.qa_harness, engine; print(sys.executable)"`. Expected: exit 0 and `/tmp/hde-epic040-qa-v1.2/venv/bin/python` (N-03).
- R3 [C] `sh -c 'for k in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do echo "$k=$(printenv "$k")"; done; for k in DATABASE_URL HD_API_KEY GEO_API_KEY HD_API_BASE_URL HDAPI_BASE_URL DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV; do if printenv "$k" > /dev/null; then echo "$k=SET"; else echo "$k=UNSET"; fi; done'`. Expected: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, and nine `UNSET` lines.

If R1, R2 or R3 differs from its expectation, the check is `TOOLING_BLOCKED` (or `FAIL_TOOLING` when the harness import fails after a good install) and no behavior command runs. In T01 the readiness line is part of the task's own commands (the virtual environment does not exist before them).

### 4.6 Captures, body, status and recording

Per-task scratch directory: `/tmp/hde-epic040-qa-v1.2/<check_id>/`, for example `/tmp/hde-epic040-qa-v1.2/d0-discovery/`.

- Capture (N-04): each command k of a task runs with stdout to `ck.out`, stderr to `ck.err` and its exit code to `ck.rc` in that directory, unless the task names another stdout target. The exit code is taken immediately from the command itself, never through a pipe. Example for T01 command 3: `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git rev-parse HEAD > /tmp/hde-epic040-qa-v1.2/d0-discovery/c3.out 2> /tmp/hde-epic040-qa-v1.2/d0-discovery/c3.err; echo $? > /tmp/hde-epic040-qa-v1.2/d0-discovery/c3.rc`.
- `argv.txt`: every command executed for the check, gate and readiness lines included, one per line in execution order, exactly as run with its prefix and without the capture redirections. A compound command is a single `sh -c` argv (N-06).
- `body.txt`: the Plan §8 sections in order: `=== CONTEXT ===` (for T01, the executor identity, venue, checkout path and clone umask first; then the tested source, interpreter and environment presence as captured), `=== COMMANDS ===` (each command line from `argv.txt` with its exit code from its `.rc` file), `=== OUTPUT ===` (the captured stdout and stderr of each command), `=== PREDICATES ===` (each [E] predicate as `PASS` or `FAIL` with the observed value; each [K] predicate as `pending QA-110`; and the line `Step-log status attests the execution layer only; [K] predicates are evaluated by Kronos at QA-110.`), `=== LIMITS ===` (the task's proof class and nonclaims). The body is composed by shell redirection (`printf` for headings and labels, `cat` for captured files) from the actual captures, never retyped. It also holds a `sha256sum` line for every supplementary file the task names (Plan §8), `BLOCKER:` lines for Plan-to-repository gaps found by T01 (numbered `B-01` onward), and `DOC_DELTA:` lines for any documentation mismatch a task observes (Plan §12 markers).
- `status.txt`: line 1 is the status the executor determines from the task's [E] predicates and prerequisites under Plan Templates causal precedence (`FAIL_TOOLING`, then `TOOLING_BLOCKED`, then `FAIL_BEHAVIOR`, then `PASS`); line 2 is the causal reason, absent for `PASS`.
- `final.rc`: the exit code of the task's final decisive command, copied from its `.rc` file.
- `provenance.txt`: one line, in this order: `QA Plan v1.2 CHECK`, the check number and `check_id`, and the Plan path in parentheses; `QA-90 collection v1.1 task`, the task ID and this collection's path in parentheses; `attempt 1`; `executed by` and the executor identity recorded in T01; `normalizations:` and the IDs of §4.9 the task applied. For T04 the line begins `QA Plan v1.2 CHECK 4 ac040-02-03-catalog-config (docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md); QA-90 collection v1.1 task T04 (docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md); attempt 1; executed by ` and continues with the real identity and the applied IDs.
- Recording (Plan §8, §12; C040-09 as approved as changed): each task ends with its recording invocation, run [C] from the checkout root. It reads the five files above and calls the tracked `tools.qa.qa_harness.record_check` once, which publishes the primary log and the manifest entry together and rolls both back on any error. The executor composes nothing else: status, reason and exit code come from the files. Expected: exit 0 and two printed paths, the primary log and `audit/qa/hde-epic040/qa_step_logs_manifest.json`. If it exits non-zero, keep every scratch file, stop the task, and report the failure signature; Kronos classifies it at QA-110.

### 4.7 Evidence files and commit boundary (Plan §7.2; separately authorized storage lane)

Evidence storage is not a check and is not part of any PASS predicate. This collection names the storage lane Plan §6 and §7.2 leave to the QA-90 task:

- When: once, after the last task of this collection has been recorded or has stopped.
- Where: branch `qa/hde-epic040-qa100-plan-v1.2`, created at the tested source in the QA checkout. It must not exist on `origin` beforehand (`git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2` prints nothing); if it exists, stop and report.
- Permitted files, and nothing else: `audit/qa/hde-epic040/qa_step_logs_manifest.json`; `audit/qa/hde-epic040/00_meta/doc_deltas.md`; `audit/docdeltas/hde-epic040_doc_deltas.md`; `audit/qa/hde-epic040/checks/d0-discovery/primary.log`; `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log`; `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log`; `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log`; `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log`; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log`; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json`; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json`; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`; `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json`; `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log`; `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log`; `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log`; `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log`; `audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl`; `audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`. Only those that exist are added; a missing one is reported, not created.
- Steps, from the checkout root: (1) `git status --porcelain --untracked-files=all` into the scratch root as `storage_status_before.txt`, and compare its untracked paths under `audit/` with the permitted list; any other path under `audit/qa/hde-epic040/` or `audit/docdeltas/` is reported and not added. (2) `git switch -c qa/hde-epic040-qa100-plan-v1.2`. (3) `git add --` followed by the permitted paths that exist, named one by one. (4) `git diff --cached --name-only` must list exactly those paths. (5) `git commit -m` with the message `HDE-EPIC040 QA-100: evidence for QA Plan v1.2 checks 1 to 10, attempt 1; tested source ` followed by the full 40-character SHA that T01 command 3 printed. (6) `git push -u origin qa/hde-epic040-qa100-plan-v1.2`, retried on a network error only. (7) `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2` must print the local `HEAD`.
- Never committed: any product, test, tool, schema, catalog, manifest, CI, Index, Mirror, PF or `docs/` file; any tracked file a test run changed (it stays uncommitted in the checkout, and check 12 later records it); anything from the scratch root; any file holding a secret value, a non-synthetic user identifier or a BodyGraph payload.
- Not done: no force-push, rebase, merge or amend; no pull request is opened by the executor (QA-100 cannot open one). The Product Owner decides any pull request and merge for that branch.
- The QA-100 result record under `docs/ephemeral/` is QA-100's own output. It is never committed to the evidence branch; QA-100 stores it under its own working-branch rule, from a checkout other than the QA checkout (for example the Codespace's default `/workspaces/glow-hdengine-v2`), so that the QA checkout stays as check 11 needs it.

### 4.8 Stop, rerun, recovery and cleanup (Plan §7.3 to §7.5)

- Run the tasks in order T01 to T10. A task whose dependency is not PASS is still recorded, as `TOOLING_BLOCKED` through its gate (§4.5); independent tasks continue.
- If T01 command 1 finds `audit/qa/hde-epic040` already present, stop before recording anything: the checkout is not the one §4.3 requires. Report every task as not executed with that observation.
- If a recording invocation fails (§4.6), stop that task, keep its scratch files, continue with independent tasks, and report.
- No rerun, Moon Loop or repeated command is authorized by this collection. A command repeated because of an operator error is recorded with both executions in `argv.txt` and the body, and the reason. A QA-created evidence-assembly defect (T02 writer, T06 altered input, T10 assembler) is recorded as `FAIL_TOOLING` and returned to QA-110, where Kronos decides any Moon Loop or attempt 2 (Plan §7.3, §7.4; Glow QA Guide §10.6).
- T10: stop the server and confirm port 8000 is closed before recording T10 (Plan §7.5). If T10 stops early, stop the server first.
- No task connects to a database, so no database recovery exists. No secret value is handled; if one is nevertheless found in any evidence file, move that file out of the repository into the scratch root, do not commit it, record the check `FAIL_TOOLING`, and report (Plan §7.5).
- Temporary files stay in the scratch root and are not committed (Plan §7.5). Nothing is deleted after the run (§4.3 item 4).

### 4.9 Normalizations (Plan §12; Glow QA Guide §3.4.7, §3.4.10; QA-90 Execute step 5)

Each normalization clarifies an unchanged Plan operation. None changes the objective, proof target, rails, evidence identity or predicate. The executor lists those applied in `provenance.txt`.

| ID | Plan locus | Normalization | Reason |
| --- | --- | --- | --- |
| N-01 | §5.2; §12 readiness ("the posture of §5.2 is applied and recorded") | The closed posture is applied per command through the CLOSED and PYTEST prefixes of §4.4 | Identical rails in every command, including in shells that do not keep exported variables |
| N-02 | Check 1 step 4 ("a fresh venv outside the repository") | The virtual environment is `/tmp/hde-epic040-qa-v1.2/venv`, first on `PATH` through the prefixes | A concrete location; `python` and `hdctl` resolve to the tested install |
| N-03 | §12 readiness (`python -c "import tools.qa.qa_harness, engine"`) | R2 also imports `sys` and prints `sys.executable` | Records the interpreter actually used (Glow QA Guide §3.4.10 execution record) |
| N-04 | §12 ("exit codes are captured from the producer itself") | Per-command capture files `ck.out`, `ck.err`, `ck.rc` (§4.6) | The body and recording are composed from actual captures |
| N-05 | §11 ("Dependencies read the step-log status") | The dependency status is read from `python -m json.tool` of the manifest | A baseline read of the recorded status |
| N-06 | Check 5 step 3 `(cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS)`; check 1 step 2; check 3 `umask`; check 10 loops | Each compound command runs as one `sh -c` argv from the checkout root | One argv per command for `argv.txt` and the header `command` list |
| N-07 | Check 3 commands 5 and 8 | `./ci/checks/check_evidence_index_hash.sh` and `./ci/checks/check_env_pins.sh` are invoked directly, as command 4 is | Both files are executable; direct invocation runs their own interpreter line |
| N-08 | Check 1 predicate ("help lists" the named flags) | Presence is counted with `grep -c -F -e` on the captured help output | A baseline count compared with the literal expectation (at least 1) |
| N-09 | Check 1 predicate (`release_id` equal to the manifest SHA-256) | The digest is cut from the `sha256sum` output into a file and counted in the admission output with `grep -c -F -f` | A baseline comparison of two printed values |
| N-10 | Check 6 steps 1 and 6; check 3 supplementary digest | `find` with `-prune` exclusions and `-print0`, `sort -z`, `xargs -0 -a` with `sha256sum` into a list file; the digest is the SHA-256 of that list; equality is `cmp` of the two lists | The Plan's digest over the sorted paths and file digests, built without pipes |
| N-11 | Check 6 predicate (stderr `GOLDEN_COMPARISON_MISMATCH:<n>` with n at least 2) | `grep -c -x -E` on the captured stderr, with the pattern that T06 command 13 gives in full (it matches the token followed by an integer of at least 2) | A baseline match of the printed value, including the bound on n |
| N-12 | Check 7 command 1 ("an empty file created outside the repository"); "empty stdout" | `touch` in the task's scratch directory; empty stdout verified by `test -s` exiting 1 | Baseline commands |
| N-13 | Check 10 probe table | S-04 to S-06 carry the valid body (the version is selected before the body is read). S-10's `a_id` is `00000000-0000-0000-0000-00000000000A`, because the upper-case form of `00000000-0000-0000-0000-000000000001` is identical to its lower-case form and would not exercise the refusal. S-12 and S-13 carry the valid body followed by 32,676 spaces, 32,769 bytes of valid JSON, so that size is the only defect. S-08 is the bytes EF BB BF followed by the valid body | Each probe isolates the one defect its row names |
| N-14 | Check 10 command 2 (`curl`) | Every probe uses `--noproxy '*'`, `-s -S`, `--max-time 10` and `-H 'Expect:'`; S-15 uses `--head`; S-13 adds `-H 'Transfer-Encoding: chunked'`; POST probes send `Content-Type: application/json; charset=utf-8` | Loopback must bypass any console proxy; no 100-continue interim response; `curl -X HEAD` would wait for a body; the chunked header makes curl omit `Content-Length` |
| N-15 | Check 10 command 2 ("append one JSON object per probe") | Each probe's status, headers and body go to scratch files; after S-26, one embedded `python -c` assembler writes all 22 lines at once. `headers` is an array of `[name, value]` pairs in received order, names lower-cased, values after the colon with leading blanks and the CR terminator removed | The Plan's command requires JSON assembly. The assembler is QA-created evidence assembly, the same class as the three writers Plan §12 names; it evaluates no predicate, and the [E] line count and the [K] malformed-capture predicate verify it |
| N-16 | Check 10 commands 1 and 3 (readiness poll; port closed) | Bounded `sh -c` loops over `curl` with a 30-second limit, each poll's time and HTTP code recorded | The Plan's poll and stop confirmation as baseline commands |
| N-17 | Check 2 command 2 (the doc-delta writer) | The writer takes the twelve DD rows byte for byte from the Plan's §9.1 table in the checkout and appends the cell `Drives decision: No`; `BLOCKER:` lines are copied verbatim from the T01 primary log | The rows cannot drift from the approved Plan |
| N-18 | Check 1 step 4 ("Python 3.12") | The virtual environment is created with `python3.12`; if that command is absent but another command reports 3.12, that command is used and recorded | The Plan names the version, not the command |
| N-19 | Check 1 step 3 (`git status --porcelain` line count) | The porcelain output is captured to a file and counted with `wc -l` on that file | No pipe |

### 4.10 Return to QA-110

QA-100 returns one `QA_EXECUTION_RESULT` per task T01 to T10 to QA-110 — Review QA Evidence and Route the Next Action — 091426.1, in the continuing Kronos-23 session. Each result gives: task, `check_id`, attempt 1, the step-log status and reason as recorded, the final decisive command's exit code, the primary-log path, the supplementary files with their SHA-256 values, the normalizations applied, deviations, residual state (server stopped, checkout kept) and the resume point; plus, once, the executor identity, the tested source SHA, the evidence branch and its pushed commit. QA-110 evaluates every [K] predicate, forms the per-task results (Plan §12 two result layers), dispositions any fault, and decides any attempt 2.

## 5. Tasks

Every task: change HDE-EPIC040 (Epic); approved Plan `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`; approving review `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`; QA Audit `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`; attempt 1 (§4.2); executor Q (§4.1); environment: the QA console checkout of §4.3 under the closed posture (§4.4); target: the tested source tree, locally; tokens `[]`; evidence storage and commit boundary §4.7; cleanup §4.8; return §4.10. Nonclaims for every task: no QA PASS for the change, acceptance, closure, PF09 status change, deployment, token, new public route or flag, or PF edit follows from a task result (Plan §12).

### T01 `d0-discovery` — Discovery and tooling bootstrap

- Plan block: CHECK 1 (Plan v1.2 L461 to L499). Class 1, pre-flight / internal. D0; all criteria as prerequisite. PF anchors: PF06-Canon-Change-Process-Guide §0.4.1.1; PF19-Canon-Glow-QA-Guide §3.6, §3.4.9.
- Dependencies: none. Setup §4.3 complete.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/d0-discovery/`.
- Inputs: the checkout; `requirements.txt`, `requirements-dev.txt`, `pyproject.toml`; `catalog/manifest.json`; the 70 test files listed in command 22.
- Outputs: `audit/qa/hde-epic040/checks/d0-discovery/primary.log` and `audit/qa/hde-epic040/qa_step_logs_manifest.json`, both created by the recording.

Commands, in order:

1. [N] `test -e audit/qa/hde-epic040`. Expected exit 1 (absent). If exit 0, stop under §4.8.
2. [N] `sh -c 'for k in DATABASE_URL HD_API_BASE_URL HDAPI_BASE_URL HD_API_KEY GEO_API_KEY DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV PORT; do if printenv "$k" > /dev/null; then echo "$k=SET"; else echo "$k=UNSET"; fi; done; for k in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do if printenv "$k" > /dev/null; then echo "$k=$(printenv "$k")"; else echo "$k=UNSET"; fi; done'`. Records presence before any change; prints no secret value.
3. [C] `git rev-parse HEAD` (attribution only; Plan §5.3).
4. [C] `git status --porcelain` (stdout to `c4.out`).
5. [C] `wc -l /tmp/hde-epic040-qa-v1.2/d0-discovery/c4.out` (N-19; attribution only).
6. [C] `python3.12 -m venv /tmp/hde-epic040-qa-v1.2/venv` (N-18).
7. [C] `python -m pip install -r requirements.txt -r requirements-dev.txt -e .` (dependency installation from the package index; `ALLOW_NETWORK` governs the product's I/O, not the installer).
8. [C] `python -m pytest --version`.
9. [C] `python --version` (R1).
10. [C] `python -c "from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check, run_pytest_check; from tools.evidence.update_evidence_index import _refresh_path_proof; print('harness_ready')"`.
11. [C] `python -c "import sys, tools.qa.qa_harness, engine; print(sys.executable)"` (R2).
12. [C] R3 of §4.5 (the closed posture as applied).
13. [C] `hdctl --help`.
14. [C] `hdctl showcompat --help`.
15. [C] `python tools/config/generate_config_artifacts.py --help`.
16. [C] `python tools/bodygraph/check_magic10_gate_readiness.py --help`.
17. [C] `python scripts/release_id_recompute.py --help`.
18. [C] `sh -c 'for f in --source --birthdate-a --birthtime-a --location-a --birthdate-b --birthtime-b --location-b --dump-reader; do printf "%s " "$f"; grep -c -F -e "$f" /tmp/hde-epic040-qa-v1.2/d0-discovery/c14.out; done'` (N-08).
19. [C] `sh -c 'for f in --compare-goldens --goldens --report; do printf "%s " "$f"; grep -c -F -e "$f" /tmp/hde-epic040-qa-v1.2/d0-discovery/c15.out; done'`.
20. [C] `sh -c 'for f in --user-id --selection-file; do printf "%s " "$f"; grep -c -F -e "$f" /tmp/hde-epic040-qa-v1.2/d0-discovery/c16.out; done'`.
21. [C] `sh -c 'for f in --check-manifest-only; do printf "%s " "$f"; grep -c -F -e "$f" /tmp/hde-epic040-qa-v1.2/d0-discovery/c17.out; done'`.
22. [P] Collection test (Plan check 1 step 7; groups G, A, B, C, D, E, F in check order, 70 files, one invocation): `python -m pytest --collect-only -q -p no:cacheprovider tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_cli_conformance_artifacts.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_engine_core_evidence.py tests/evidence/test_epic030_pr05_category_framework_evidence.py tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_sanity_pipeline.py tests/qa/test_qa_tool_ownership.py tests/config/test_registry_catalog_contract.py tests/config/test_magic10_contracts.py tests/config/test_manifest_schema.py tests/config/test_typed_bundles.py tests/config/test_alias_policy_enforcement.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_registry_report.py tests/config/test_registry_report_determinism.py tests/config/test_registry_report_indexing.py tests/compare/test_arrays_as_sets.py tests/m10/test_defs_order.py tests/m10/test_thresholds_rounding.py tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/core/test_engine_core_purity.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_m10_symmetry_identity.py tests/runtime/test_identity.py tests/scripts/test_cut_release_manifest.py tests/reader_v1/test_release_pack.py tests/config/test_config_artifacts.py tests/bodygraph/test_gates.py tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py tests/bodygraph/test_check_magic10_gate_readiness.py tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_ab_ba_identity.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_abba_parity.py tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/cli/test_showcompat_sources.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py tests/artifacts/test_cli_text_artifacts_bom_lf.py tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py tests/runtime/test_emit_public_legacy_helper.py tests/epic003/test_meta_invocation_ok.py tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_writer_transport.py tests/reader_v1/test_emitter.py tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/transport/test_a7_transport_proofs.py tests/compliance/test_log_shape_snapshot.py tests/compliance/test_logging_filter_keys_only_and_redactions.py`.
23. [C] `tail -n 1 /tmp/hde-epic040-qa-v1.2/d0-discovery/c22.out` (the collected-count line).
24. [C] Admission: `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as f; b=f(); print(type(b).__name__, b.manifest.version, b.manifest.built_at_utc, len(b.manifest.files), b.release_id, b.mechanics['config_id'])"`.
25. [C] `sha256sum catalog/manifest.json`.
26. [C] `cut -d ' ' -f 1 /tmp/hde-epic040-qa-v1.2/d0-discovery/c25.out`, stdout to `/tmp/hde-epic040-qa-v1.2/d0-discovery/manifest_sha256.txt` (N-09).
27. [C] `grep -c -F -f /tmp/hde-epic040-qa-v1.2/d0-discovery/manifest_sha256.txt /tmp/hde-epic040-qa-v1.2/d0-discovery/c24.out` (N-09).
28. [C] Only if command 24 exits non-zero or command 27 does not print 1: `python scripts/release_id_recompute.py --check-manifest-only`. Never run this script in any other mode.
29. [C] `git check-ignore -v audit/qa/hde-epic040/checks/d0-discovery/primary.log audit/qa/hde-epic040/qa_step_logs_manifest.json audit/docdeltas/hde-epic040_doc_deltas.md` (informative; exit 1 means no path is ignored).
30. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/d0-discovery'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='d0-discovery', check_name='Discovery and tooling bootstrap', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=('audit/qa/hde-epic040/qa_step_logs_manifest.json',), intended_tokens=(), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

Final decisive command: command 24 (admission); `final.rc` is its exit code.

Body additions: the `=== CONTEXT ===` section opens with `EXECUTOR:`, `VENUE:`, `CHECKOUT:` (absolute path) and `CLONE_UMASK: 0022` lines, then the outputs of commands 2, 3, 5, 9, 11 and 12. A missing entrypoint or flag found by commands 13 to 21 is written as `BLOCKER: B-01` (and onward) with the missing item.

[E] predicates (Plan check 1 PASS conditions):

1. Command 1 exits 1.
2. Commands 6, 7 and 8 exit 0; command 9 prints `Python 3.12.` followed by the patch number; command 10 prints `harness_ready` and exits 0.
3. Command 22 exits 0; command 23's collected count is recorded. The QA Audit §4.4 reference is 2,090 tests; a different count is recorded with its explanation, and is not a failure by itself (Plan §11).
4. Commands 13 to 17 exit 0; every count printed by commands 18 to 21 is at least 1.
5. Command 24 prints `AdmittedMechanicsBundle 1.3.0 2026-08-24T18:04:49Z 45`, then a `release_id`, then `m10-channel-state-v1.0.0`; command 27 prints 1 (the `release_id` equals the `catalog/manifest.json` SHA-256).

Status (Plan check 1, causal precedence):

- `FAIL_TOOLING`: command 10 fails although command 7 exited 0; a help command crashes with a traceback; or command 22 exits non-zero for a reason `TOOLING_BLOCKED` does not name (for example 2). No collection result is `FAIL_BEHAVIOR`.
- `TOOLING_BLOCKED`: Python 3.12 is unavailable; command 7 fails; an entrypoint or Plan-used flag is missing (with its `BLOCKER:` line); command 22 exits 5 or reports a listed file as not found; command 28 exits 1 (member bytes differ: source contamination).
- `FAIL_BEHAVIOR`: admission refuses, or command 27 does not print 1, while command 28 exits 0.
- `PASS`: every [E] predicate holds.

[K] predicates: none.

### T02 `step-0b-doc-delta-capture` — Step-0B doc-delta capture

- Plan block: CHECK 2 (L501 to L524). Class 1, pre-flight / internal. D1. PF anchors: PF27-Canon-Plan-Templates (Step-0B); PF19-Canon-Glow-QA-Guide §3.4.3.
- Dependencies: T01 executed, any status, with its primary log present.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/step-0b-doc-delta-capture/`.
- Inputs: Plan v1.2 §9.1 in the checkout (`docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`); the T01 primary log.
- Outputs: `audit/docdeltas/hde-epic040_doc_deltas.md` (draft or staging surface), `audit/qa/hde-epic040/00_meta/doc_deltas.md` (authoritative epic capture), the primary log and its manifest entry.

Commands, in order:

1. [C] Gate: `test -s audit/qa/hde-epic040/checks/d0-discovery/primary.log`. If exit 1: record `TOOLING_BLOCKED` ("d0-discovery produced no primary log") and stop.
2. R1, R2, R3 of §4.5.
3. [C] `test -e audit/docdeltas/hde-epic040_doc_deltas.md` (expected exit 1).
4. [C] `test -e audit/qa/hde-epic040/00_meta/doc_deltas.md` (expected exit 1). If command 3 or 4 exits 0: run [C] `sha256sum` on the existing file, write nothing, and record `FAIL_TOOLING` ("existing doc-delta surface; not overwritten").
5. [C] Writer (N-17): `python -c "import re; from pathlib import Path; plan=Path('docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md').read_text(encoding='utf-8').splitlines(); rows=[l.rstrip() + ' Drives decision: No |' for l in plan if re.match(r'\| DD-[0-9]{2} \|', l)]; blk=[l for l in Path('audit/qa/hde-epic040/checks/d0-discovery/primary.log').read_text(encoding='utf-8').splitlines() if l.startswith('BLOCKER:')]; t='# HDE-EPIC040 doc deltas (Step-0B)\n\nSource: QA Plan v1.2, docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md, section 9.1. Written by check step-0b-doc-delta-capture (QA-90 collection v1.1, task T02).\n\n## BLOCKERS\n\n' + ('\n'.join(blk) if blk else 'none') + '\n\n## CAVEATS\n\n| ID | Class | Delta | Drain target (title) | Owner | Decision |\n| --- | --- | --- | --- | --- | --- |\n' + '\n'.join(rows) + '\n'; [(Path(p).parent.mkdir(parents=True, exist_ok=True), Path(p).write_bytes(t.encode('utf-8'))) for p in ('audit/docdeltas/hde-epic040_doc_deltas.md', 'audit/qa/hde-epic040/00_meta/doc_deltas.md')]"`.
6. [C] `test -s audit/docdeltas/hde-epic040_doc_deltas.md`.
7. [C] `test -s audit/qa/hde-epic040/00_meta/doc_deltas.md`.
8. [C] `sha256sum audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`.
9. [C] `cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md`.
10. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/step-0b-doc-delta-capture'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='step-0b-doc-delta-capture', check_name='Step-0B doc-delta capture', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=('audit/docdeltas/hde-epic040_doc_deltas.md', 'audit/qa/hde-epic040/00_meta/doc_deltas.md',), intended_tokens=(), pf_refs=('PF27-Canon-Plan-Templates', 'PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

Final decisive command: command 9 (`cmp`).

[E] predicates: commands 3 and 4 exit 1; command 5 exits 0; commands 6 and 7 exit 0; command 9 exits 0.

Status: `FAIL_TOOLING` if command 5 fails, a surface is empty, the surfaces differ, or an existing surface would be overwritten; `TOOLING_BLOCKED` if the gate fails; `PASS` if every [E] predicate holds.

[K] predicates (Kronos, from the two files): LF-terminated and without BOM; each of DD-01 to DD-12 appears exactly once; both sections are present; every T01 `BLOCKER:` line appears under BLOCKERS. A false [K] predicate makes the per-task result `FAIL_TOOLING` (Plan check 2).

### T03 `ac040-08-evidence-validators` — Owner evidence coherence and evidence tests

- Plan block: CHECK 3 (L526 to L560). Class 2, local/offline (no vendor). D2; AC040-08; K040-REQ-012. PF anchors: PF12-Canon-HDE-Schemas-and-Artifacts §8.3, §8.6; PF19-Canon-Glow-QA-Guide §2.2.7, §2.2.11, §14.1.
- Dependencies: `d0-discovery` PASS (gate §4.5).
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/`.
- Inputs: the governed evidence graph in the checkout (`docs/evidence/`, `artifacts/`, `audit/gates/`), the nine validators, the 12 group G files.
- Outputs: the primary log and its manifest entry. No other file.

Commands, in order:

1. [C] Gate: the manifest read of §4.5; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [C] Venue evidence: `sh -c umask`.
4. [C] Venue evidence: `stat -c '%a %n' docs/evidence/INDEX.sha256`.
5. [C] Supplementary digest, before (N-10; non-gating): `find docs/evidence artifacts audit/gates -type f -print0`, stdout to `/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_before.z`.
6. [C] `sort -z /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_before.z`, stdout to `graph_before.sorted.z` in the scratch directory.
7. [C] `xargs -0 -a /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_before.sorted.z sha256sum`, stdout to `graph_before.txt` in the scratch directory.
8. [C] `sha256sum /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_before.txt`.
9. [C] `python tools/evidence/update_evidence_index.py --check`
10. [C] `python tools/evidence/orientation_demo.py --check`
11. [C] `python tools/evidence/validate_evidence_paths.py`
12. [C] `./ci/checks/check_mirror_schema.sh`
13. [C] `./ci/checks/check_evidence_index_hash.sh` (N-07)
14. [C] `python tools/evidence/run_canonical_json_gate.py --check-only`
15. [C] `python tools/evidence/check_lf_endings.py`
16. [C] `./ci/checks/check_env_pins.sh` (N-07)
17. [C] `python tools/config/generate_config_artifacts.py --check`
18. [P] Pytest group G: `python -m pytest -q -p no:cacheprovider -rs tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_cli_conformance_artifacts.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_engine_core_evidence.py tests/evidence/test_epic030_pr05_category_framework_evidence.py tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_sanity_pipeline.py tests/qa/test_qa_tool_ownership.py`
19. [C] Supplementary digest, after: `find docs/evidence artifacts audit/gates -type f -print0`, stdout to `/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_after.z`.
20. [C] `sort -z /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_after.z`, stdout to `graph_after.sorted.z` in the scratch directory.
21. [C] `xargs -0 -a /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_after.sorted.z sha256sum`, stdout to `graph_after.txt` in the scratch directory.
22. [C] `sha256sum /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_after.txt`.
23. [C] `cmp /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_before.txt /tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators/graph_after.txt` (non-gating; a difference is reported to Kronos in the body, and is not a predicate).
24. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-08-evidence-validators'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-08-evidence-validators', check_name='Owner evidence coherence and evidence tests', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF12-Canon-HDE-Schemas-and-Artifacts', 'PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

Final decisive command: command 18 (group G). Commands 19 to 23 run after it, are supplementary and non-gating, and do not change `final.rc`.

[E] predicates: commands 9 to 17 exit 0; command 18 exits 0 and its summary reports no failure or error; skips are listed with their reasons.

Status (Plan check 3):

- `FAIL_TOOLING`: a validator crashes with a traceback; command 18 exits 2, 3, 4 or negative.
- `TOOLING_BLOCKED`: the gate fails; an entrypoint is missing; command 18 exits 5. Also the venue rule: command 18 exits 1, every failure it reports is in `tests/evidence/test_evidence_index_missing_state.py` at its file-mode equality assertion, and command 4 does not print `644` (or was not recorded). AC040-08 then relies for that test on the exact-head CI evidence of Plan §10.2; Kronos confirms the attribution at QA-110.
- `FAIL_BEHAVIOR`: a validator runs normally and reports incoherent delivered evidence (a governed error token); or command 18 exits 1 outside the venue rule, including a file-mode failure when command 4 printed `644`.
- `PASS`: every [E] predicate holds.

[K] predicates: none. Kronos confirms any venue-rule attribution from the pytest output and commands 3 and 4.

### T04 `ac040-02-03-catalog-config` — Catalog, configuration and schemas

- Plan block: CHECK 4 (L562 to L589). Class 2, local/offline (no vendor). D3; AC040-02, AC040-03; K040-REQ-003 to K040-REQ-006; PF09.3 HDE-SEPA005.1, HDE-SEPA005.2. PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation; PF10 Addendum 2.5 (written in the body, since the harness pattern does not admit the PF10 title).
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-02-03-catalog-config/`.
- Inputs: `catalog/channels_v1.json`, `catalog/magic10_mechanics_v1.json`, the 12 group A files.
- Outputs: the primary log and its manifest entry.

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [C] `sha256sum catalog/channels_v1.json catalog/magic10_mechanics_v1.json`.
4. [P] Pytest group A (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_registry_catalog_contract.py tests/config/test_magic10_contracts.py tests/config/test_manifest_schema.py tests/config/test_typed_bundles.py tests/config/test_alias_policy_enforcement.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_registry_report.py tests/config/test_registry_report_determinism.py tests/config/test_registry_report_indexing.py tests/compare/test_arrays_as_sets.py tests/m10/test_defs_order.py tests/m10/test_thresholds_rounding.py`
5. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-02-03-catalog-config'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-02-03-catalog-config', check_name='Catalog, configuration and schemas', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF09.3-Canon-HDE-Build-Checklist-Separation',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

[E] predicates: command 3 prints both digests; command 4 exits 0.

Status: `FAIL_TOOLING` if command 4 exits 2, 3, 4 or negative; `TOOLING_BLOCKED` if the gate fails, a listed file is missing, or command 4 exits 5; `FAIL_BEHAVIOR` if command 4 exits 1; `PASS` otherwise when every [E] predicate holds.

[K] predicates (Kronos, from the two catalog files at the tested source whose SHA-256 equals command 3's digests): the structural predicates of Plan check 4 (36 channel rows with exactly the eight keys, ascending and unique gate pairs, no null; the mechanics `config_id`, `schema`, 20 unique signals, the three profiles, 10 category weights and the three aggregation assignments). A false one makes the per-task result `FAIL_BEHAVIOR`.

### T05 `ac040-04-05-admission-identity` — Admission, pure core and release identity

- Plan block: CHECK 5 (L591 to L618). Class 2, local/offline (no vendor). D4; AC040-04, AC040-05; K040-REQ-007 to K040-REQ-009; PF09.3 HDE-SEPA005.3, HDE-SEPA005.4. PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation; PF10 Addenda 2.12, 2.22, 2.27 (in the body).
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-04-05-admission-identity/`.
- Inputs: the 45 release members; `catalog/manifest.json`; `audit/ops/hde-epic040/ops01/SHA256SUMS` and the files it lists; the 9 group B files.
- Outputs: the primary log and its manifest entry. OPS01 files are read, never written.

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [C] `python scripts/release_id_recompute.py --check-manifest-only` (expected exit 0). Never in any other mode.
4. [C] `sha256sum catalog/manifest.json`.
5. [C] `sh -c 'cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS'` (N-06; expected 7 lines ending `OK`, exit 0; read-only).
6. [P] Pytest group B (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/core/test_engine_core_purity.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_m10_symmetry_identity.py tests/runtime/test_identity.py tests/scripts/test_cut_release_manifest.py tests/reader_v1/test_release_pack.py`
7. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-04-05-admission-identity'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-04-05-admission-identity', check_name='Admission, pure core and release identity', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF09.3-Canon-HDE-Build-Checklist-Separation',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

The Plan's step 4 (binding) has no command: Kronos reads `audit/ops/hde-epic040/ops01/attestation.json` at QA-110.

[E] predicates: commands 3, 5 and 6 exit 0; command 4 prints the digest.

Status: `FAIL_TOOLING` if a command crashes or command 6 exits 2, 3, 4 or negative; `TOOLING_BLOCKED` if the gate fails, an OPS01 file is missing or command 6 exits 5; `FAIL_BEHAVIOR` if command 3 reports `MANIFEST_ERROR` or command 6 exits 1; `PASS` when every [E] predicate holds.

[K] predicates (Kronos, from `attestation.json` and command 4's digest): `release_id` and `manifest_sha256` both equal that digest; `validation_result` is `PASS` and `release_admission` is `PR06R_B_FINAL_PASS`; `source_commit`, `validation_result` and `release_admission` are recorded in the QA-110 result. A false one makes the per-task result `FAIL_BEHAVIOR`. OPS01 evidence is corroboration, not QA evidence, and the attestation is not rebuilt.

### T06 `ac040-06-golden-comparison` — Read-only golden comparison

- Plan block: CHECK 6 (L620 to L661). Class 2, local/offline (no vendor). D5; AC040-06; K040-REQ-010; PF09.3 HDE-SEPA005.4. PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation; PF01-Canon-HDE-Math-Spec §9.5; PF10 Addendum 2.20 (in the body).
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/`.
- Inputs: the checkout; `tests/fixtures/magic10/v1/goldens.json`.
- Outputs (QA-created, in `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/`): `compare_match_run1.json`, `compare_match_run2.json`, `tmp_goldens_altered.json`, `compare_mismatch_report.json`; the primary log and its manifest entry.

Never run `tools/config/generate_config_artifacts.py` without `--compare-goldens` or `--check` (write paths; QA Audit L-07).

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [C] Before-digest (N-10): `find . -path ./.git -prune -o -path ./audit/qa/hde-epic040 -prune -o -name __pycache__ -prune -o -name .pytest_cache -prune -o -type f -print0`, stdout to `/tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_before.z`.
4. [C] `sort -z /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_before.z`, stdout to `tree_before.sorted.z` in the scratch directory.
5. [C] `xargs -0 -a /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_before.sorted.z sha256sum`, stdout to `tree_before.txt` in the scratch directory.
6. [C] `sha256sum /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_before.txt`.
7. [C] `mkdir -p audit/qa/hde-epic040/checks/ac040-06-golden-comparison`.
8. [C] Match run 1: `python tools/config/generate_config_artifacts.py --compare-goldens .`, stdout to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json` (expected exit 0).
9. [C] Match run 2: the same command, stdout to `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json` (expected exit 0).
10. [C] Altered input (QA-created input writer, Plan §12): `python -c "import json; from pathlib import Path; d=json.loads(Path('tests/fixtures/magic10/v1/goldens.json').read_bytes()); s=[x for x in d['cases'] if x['case_id'] == 'M10-G001'][0]['expected']['signals'][0]; print('M10-G001 expected.signals[0]', s['signal_id'], 'q', s['q'], 'to', 1); s['q']=1; Path('audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json').write_bytes(json.dumps(d, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8') + b'\n')"`. It prints the one changed leaf.
11. [C] `sha256sum tests/fixtures/magic10/v1/goldens.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json`.
12. [C] Mismatch run: `python tools/config/generate_config_artifacts.py --compare-goldens . --goldens audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json --report /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/mismatch_report.json` (expected exit 1).
13. [C] `grep -c -x -E 'GOLDEN_COMPARISON_MISMATCH:([2-9]|[1-9][0-9]+)' /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/c12.err` (N-11; expected 1).
14. [C] `cp /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/mismatch_report.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json`.
15. [C] `cmp /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/mismatch_report.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json`.
16. [C] `sha256sum /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/mismatch_report.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json`.
17. [C] After-digest, before any test runs: `find . -path ./.git -prune -o -path ./audit/qa/hde-epic040 -prune -o -name __pycache__ -prune -o -name .pytest_cache -prune -o -type f -print0`, stdout to `/tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_after.z`.
18. [C] `sort -z /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_after.z`, stdout to `tree_after.sorted.z` in the scratch directory.
19. [C] `xargs -0 -a /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_after.sorted.z sha256sum`, stdout to `tree_after.txt` in the scratch directory.
20. [C] `sha256sum /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_after.txt`.
21. [C] `cmp /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_before.txt /tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison/tree_after.txt`.
22. [C] Byte identity: `cmp audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json`.
23. [C] `sha256sum audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json` (binding lines, Plan §8).
24. [P] Pytest group C (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/config/test_config_artifacts.py`.
25. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-06-golden-comparison'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-06-golden-comparison', check_name='Read-only golden comparison', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=('audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json', 'audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json', 'audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json', 'audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json',), intended_tokens=(), pf_refs=('PF09.3-Canon-HDE-Build-Checklist-Separation', 'PF01-Canon-HDE-Math-Spec',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

[E] predicates: commands 8 and 9 exit 0 and command 22 exits 0; command 12 exits 1 and command 13 prints 1; command 15 exits 0; command 21 exits 0; command 24 exits 0.

Status (Plan check 6):

- `FAIL_TOOLING`: command 10 fails; command 12 refuses the altered file with `GOLDENS_INVALID` (a QA input defect); command 15 exits non-zero (the report copy differs); command 24 exits 2, 3, 4 or negative.
- `TOOLING_BLOCKED`: the gate fails; a run refuses with `RAILS_CLOSED_REQUIRED`; a run refuses on admission and [C] `python scripts/release_id_recompute.py --check-manifest-only` then exits 1; command 24 exits 5.
- `FAIL_BEHAVIOR`: command 8 or 9 mismatches or refuses on the tested source (when `--check-manifest-only` exits 0); command 12 reports a match (exit 0); command 22 or 21 exits 1; command 24 exits 1.
- `PASS`: every [E] predicate holds.

[K] predicates (Kronos, from `compare_match_run1.json`, `compare_mismatch_report.json`, `tmp_goldens_altered.json`, the fixture at the tested source and T01's manifest digest): the match report has `ok` true, empty `mismatches`, `cases` exactly `M10-G001` to `M10-G008` each with `outcome` `match`, `config_id` `m10-channel-state-v1.0.0` and `candidate_release_id` equal to the manifest SHA-256; the mismatch report has `ok` false, every mismatch row has `case_id` `M10-G001`, one row has `path` `transcription.expected`, and cases `M10-G002` to `M10-G008` have `outcome` `match`; `tmp_goldens_altered.json` differs from the fixture only in case `M10-G001` `expected.signals[0].q`, changed from `0` to `1`. A false report predicate makes the per-task result `FAIL_BEHAVIOR`; a false altered-file predicate makes it `FAIL_TOOLING`.

### T07 `ac040-07-gate-ingress-offline` — Gate ingress and readiness, offline

- Plan block: CHECK 7 (L663 to L689). Class 2, local/offline (no vendor). D6; AC040-07 (offline part); K040-REQ-007, K040-REQ-011; PF09.3 HDE-SEPA005.3, HDE-SEPA005.5. PF anchors: PF09.3-Canon-HDE-Build-Checklist-Separation; PF10 Addendum 2.20 (in the body).
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/`.
- Inputs: an empty selection file in the scratch directory; the synthetic identifiers `00000000-0000-0000-0000-00000000000G` (invalid) and `00000000-0000-0000-0000-000000000001`; the 4 group D files. `DATABASE_URL` is unset by the prefix.
- Outputs: the primary log and its manifest entry.

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [C] `touch /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/empty_selection.txt` (N-12).
4. [C] `python tools/bodygraph/check_magic10_gate_readiness.py --selection-file /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/empty_selection.txt` (expected exit 5).
5. [C] `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-00000000000G` (expected exit 5).
6. [C] `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-000000000001` (expected exit 5; no report on stdout).
7. [C] `grep -c -x -F READINESS_EMPTY_SELECTION /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c4.err` (expected 1).
8. [C] `grep -c -x -F READINESS_SELECTION_INVALID /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c5.err` (expected 1).
9. [C] `grep -c -x -F READINESS_UNAVAILABLE /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c6.err` (expected 1).
10. [C] `test -s /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c4.out` (expected exit 1: empty stdout).
11. [C] `test -s /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c5.out` (expected exit 1).
12. [C] `test -s /tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline/c6.out` (expected exit 1).
13. [P] Pytest group D (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/bodygraph/test_gates.py tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py tests/bodygraph/test_check_magic10_gate_readiness.py`
14. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-07-gate-ingress-offline'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-07-gate-ingress-offline', check_name='Gate ingress and readiness, offline', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF09.3-Canon-HDE-Build-Checklist-Separation',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

The open-rails refusal of the readiness command is not re-run: group D proves it, and rails never change inside a task (Plan check 7).

[E] predicates: commands 4, 5 and 6 exit 5; commands 7, 8 and 9 print 1; commands 10, 11 and 12 exit 1; command 13 exits 0.

Status: `FAIL_TOOLING` if a readiness command crashes with a traceback or command 13 exits 2, 3, 4 or negative; `TOOLING_BLOCKED` if the gate fails or command 13 exits 5; `FAIL_BEHAVIOR` if a refusal is missing or wrong, any command emits a report on stdout, or command 13 exits 1; `PASS` when every [E] predicate holds.

[K] predicates: none.

### T08 `ac040-04-09-compat-cli-offline` — Compat and CLI, local/offline

- Plan block: CHECK 8 (L691 to L706). Class 2, local/offline (no vendor). D7; AC040-04 (application boundary), AC040-09; K040-REQ-004, K040-REQ-008. PF anchors: PF19-Canon-Glow-QA-Guide §3.3.
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-04-09-compat-cli-offline/`.
- Inputs: the 17 group E files.
- Outputs: the primary log and its manifest entry.

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [P] Pytest group E (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_ab_ba_identity.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_abba_parity.py tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/cli/test_showcompat_sources.py tests/cli/test_errors_parity.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py tests/artifacts/test_cli_text_artifacts_bom_lf.py tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py tests/runtime/test_emit_public_legacy_helper.py tests/epic003/test_meta_invocation_ok.py`
4. [C] `grep -F SKIPPED /tmp/hde-epic040-qa-v1.2/ac040-04-09-compat-cli-offline/c3.out` (exit 1 when there is no skip line). Its output is copied into `=== PREDICATES ===`, each skip with its reason (Plan RL-12).
5. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-04-09-compat-cli-offline'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-04-09-compat-cli-offline', check_name='Compat and CLI, local/offline', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

Final decisive command: command 3.

[E] predicates: command 3 exits 0. Skips contribute no proof and are not counted as passes; the three `tests/cli/test_showcompat_parity_and_identity.py` tests that skip with "showcompat vendor calls require open rails" are not vendor coverage (Glow QA Guide §2.3), which check 11 alone carries.

Status: `PASS` if command 3 exits 0; `FAIL_BEHAVIOR` if 1; `FAIL_TOOLING` if 2, 3, 4 or negative; `TOOLING_BLOCKED` if 5, a file is missing, or the gate fails.

[K] predicates: none.

### T09 `ac040-09-reader-http-in-process` — Reader, HTTP and transport, in-process

- Plan block: CHECK 9 (L708 to L721). Class 2, local/offline (no vendor), in-process. D8; AC040-09; Reader v1 and v2 contracts. PF anchors: PF05-Canon-HDE-CLI-API-Vendor-Ref §5 as overridden by PF10 Addenda 2.23 and 2.25 (in the body); PF19-Canon-Glow-QA-Guide §3.2.
- Dependencies: `d0-discovery` PASS.
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/ac040-09-reader-http-in-process/`.
- Inputs: the 15 group F files. They include `tests/http/test_reader_post_v1.py` and `tests/http/test_dev_conjunction_http.py`, which carry the production gating of the dev routes that T10 does not probe over HTTP.
- Outputs: the primary log and its manifest entry.

Commands, in order:

1. [C] Gate; dependency `d0-discovery`.
2. R1, R2, R3 of §4.5.
3. [P] Pytest group F (final decisive command): `python -m pytest -q -p no:cacheprovider -rs tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_writer_transport.py tests/reader_v1/test_emitter.py tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/transport/test_a7_transport_proofs.py tests/compliance/test_log_shape_snapshot.py tests/compliance/test_logging_filter_keys_only_and_redactions.py`
4. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/ac040-09-reader-http-in-process'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='ac040-09-reader-http-in-process', check_name='Reader, HTTP and transport, in-process', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=(), intended_tokens=(), pf_refs=('PF05-Canon-HDE-CLI-API-Vendor-Ref', 'PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

[E] predicates: command 3 exits 0.

Status: `PASS` if command 3 exits 0; `FAIL_BEHAVIOR` if 1; `FAIL_TOOLING` if 2, 3, 4 or negative; `TOOLING_BLOCKED` if 5, a file is missing, or the gate fails.

[K] predicates: none. Proof class: in-process Flask test client with injected current rows; not live transport and not a live database.

### T10 `sec-reader-http-live` — Reader route security over loopback HTTP (closed posture)

- Plan block: CHECK 10 (L723 to L781). Class 2, local/offline (no vendor), loopback HTTP. D9; PO Q-1; AC040-09 (closed-rails part); K040-REQ-008, K040-REQ-013. PF anchors: PF19-Canon-Glow-QA-Guide §3.2, §3.5.10, §14.4.2; PF10 Addenda 2.19, 2.23, 2.24, 2.25 (in the body).
- Dependencies: `d0-discovery` PASS and `ac040-09-reader-http-in-process` PASS.
- Target: `adapter.factory:create_app()` from the tested tree, served by gunicorn on the console's loopback, under the closed posture with `APP_ENV=dev` and `PORT=8000`. Not production and not the deployed service (Glow QA Guide §3.5.5, §14.4.2).
- Scratch directory: `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/`, with `bodies/` and `probes/`.
- Inputs: the seven request-body files of commands 5 to 11 (N-13), built from the synthetic identifiers `00000000-0000-0000-0000-000000000001` and `00000000-0000-0000-0000-000000000002` (QA Audit L-50).
- Outputs (QA-created, in `audit/qa/hde-epic040/checks/sec-reader-http-live/`): `http_probes.jsonl` (decisive captures) and `gunicorn_server.log` (supplementary, non-gating); the primary log and its manifest entry.

Commands, in order:

1. [C] Gate; dependencies `d0-discovery` and `ac040-09-reader-http-in-process`.
2. R1, R2, R3 of §4.5.
3. [C] Port free: `curl --noproxy '*' -s -o /dev/null -w '%{http_code}' --max-time 2 http://127.0.0.1:8000/internal/version` (expected stdout `000` and exit 7). Anything else means port 8000 is unavailable: record `TOOLING_BLOCKED` and stop.
4. [C] `mkdir -p audit/qa/hde-epic040/checks/sec-reader-http-live`.
5. [C] `printf '%s' '{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002"}'`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json` (93 bytes).
6. [C] `printf '%s' '{"a_id":'`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/truncated.json` (8 bytes).
7. [C] `printf '\357\273\277%s' '{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002"}'`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/bom.json` (96 bytes; first bytes EF BB BF).
8. [C] `printf '%s' '{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002","c":1}'`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/extra_key.json` (99 bytes).
9. [C] `printf '%s' '{"a_id":"00000000-0000-0000-0000-00000000000A","b_id":"00000000-0000-0000-0000-000000000002"}'`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/upper_a_id.json` (93 bytes).
10. [C] `touch /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/empty.json` (0 bytes).
11. [C] `printf '%s%32676s' '{"a_id":"00000000-0000-0000-0000-000000000001","b_id":"00000000-0000-0000-0000-000000000002"}' ''`, stdout to `/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/oversize.json` (32,769 bytes).
12. [C] `wc -c /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/truncated.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/bom.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/extra_key.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/upper_a_id.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/empty.json /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/oversize.json` (expected 93, 8, 96, 99, 93, 0, 32769).
13. [C] `touch /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-15.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.body /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.body` (a zero-length response body then leaves an empty file rather than a missing one).
14. Start the server in the background, so that it keeps running across the probe commands, and record its process ID: `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PORT=8000 python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8000 --workers 2 --threads 4 --timeout 30 > audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log 2>&1 & echo $! > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/server.pid`. In `argv.txt` this is recorded as the server command without the redirections, `&` and the PID capture.
15. [C] Service readiness (N-16): `sh -c 's=$(date +%s); while :; do c=$(curl --noproxy "*" -s -o /dev/null -w "%{http_code}" --max-time 2 http://127.0.0.1:8000/internal/version); printf "%s %s\n" "$(date -u +%H:%M:%S)" "$c"; [ "$c" = 200 ] && exit 0; [ $(($(date +%s) - s)) -ge 30 ] && exit 1; sleep 1; done'` (expected exit 0; stdout lists every poll). If it exits 1, stop the server (commands 38 to 40) and record `TOOLING_BLOCKED`; no probe is sent.

Commands 16 to 37 are the 22 probes, in this order (N-13, N-14). Each is shown with its capture: the HTTP status to `.status`, curl's stderr to `.err` and curl's exit code to `.rc`, beside the `.headers` and `.body` files curl writes. Each runs with the CLOSED prefix.

16. [C] S-01 `GET /internal/version`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.headers -w '%{http_code}' 'http://127.0.0.1:8000/internal/version' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-01.rc`
17. [C] S-02 `POST /api/reader?v=1`, body `valid.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-02.rc`
18. [C] S-03 `POST /api/reader?v=2`, body `valid.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-03.rc`
19. [C] S-04 `POST /api/reader`, body `valid.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json 'http://127.0.0.1:8000/api/reader' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-04.rc`
20. [C] S-05 `POST /api/reader?v=3`, body `valid.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json 'http://127.0.0.1:8000/api/reader?v=3' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-05.rc`
21. [C] S-06 `POST /api/reader?v=1&v=2`, body `valid.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/valid.json 'http://127.0.0.1:8000/api/reader?v=1&v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-06.rc`
22. [C] S-07 `POST /api/reader?v=1`, body `truncated.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/truncated.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-07.rc`
23. [C] S-08 `POST /api/reader?v=1`, body `bom.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/bom.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-08.rc`
24. [C] S-09 `POST /api/reader?v=1`, body `extra_key.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/extra_key.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-09.rc`
25. [C] S-10 `POST /api/reader?v=1`, body `upper_a_id.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/upper_a_id.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-10.rc`
26. [C] S-11 `POST /api/reader?v=1`, body `empty.json`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/empty.json 'http://127.0.0.1:8000/api/reader?v=1' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-11.rc`
27. [C] S-12 `POST /api/reader?v=2`, body `oversize.json`, sent with `Content-Length`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/oversize.json 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-12.rc`
28. [C] S-13 `POST /api/reader?v=2`, body `oversize.json`, sent chunked, no `Content-Length`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.headers -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' -H 'Transfer-Encoding: chunked' --data-binary @/tmp/hde-epic040-qa-v1.2/sec-reader-http-live/bodies/oversize.json 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-13.rc`
29. [C] S-14 `GET /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.headers -w '%{http_code}' 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-14.rc`
30. [C] S-15 `HEAD /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' --head -o /dev/null -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-15.headers -w '%{http_code}' 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-15.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-15.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-15.rc`
31. [C] S-16 `OPTIONS /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.headers -w '%{http_code}' -X OPTIONS 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-16.rc`
32. [C] S-17 `PUT /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.headers -w '%{http_code}' -X PUT 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-17.rc`
33. [C] S-18 `PATCH /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.headers -w '%{http_code}' -X PATCH 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-18.rc`
34. [C] S-19 `DELETE /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.headers -w '%{http_code}' -X DELETE 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-19.rc`
35. [C] S-20 `TRACE /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.headers -w '%{http_code}' -X TRACE 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-20.rc`
36. [C] S-21 `PROPFIND /api/reader?v=2`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.headers -w '%{http_code}' -X PROPFIND 'http://127.0.0.1:8000/api/reader?v=2' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-21.rc`
37. [C] S-26 `GET /api/reader/missing`: `curl --noproxy '*' -s -S --max-time 10 -H 'Expect:' -o /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.body -D /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.headers -w '%{http_code}' 'http://127.0.0.1:8000/api/reader/missing' > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.status 2> /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.err; echo $? > /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/probes/S-26.rc`

38. [C] Stop: `sh -c 'kill -TERM "$(cat /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/server.pid)"'`.
39. [C] `sh -c 'p=$(cat /tmp/hde-epic040-qa-v1.2/sec-reader-http-live/server.pid); s=$(date +%s); while kill -0 "$p" 2> /dev/null; do [ $(($(date +%s) - s)) -ge 30 ] && exit 1; sleep 1; done; exit 0'` (expected exit 0: the server process has ended).
40. [C] Port closed: `curl --noproxy '*' -s -o /dev/null -w '%{http_code}' --max-time 2 http://127.0.0.1:8000/internal/version` (expected stdout `000`, exit 7).
41. [C] `test -s audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`. If it exits 1: [C] `printf 'no server output\n'`, stdout to that log (Plan §12 non-empty capture rule).
42. [C] JSONL assembly (N-15): `python -c "import hashlib, json; from pathlib import Path; r=Path('/tmp/hde-epic040-qa-v1.2/sec-reader-http-live'); P=(('S-01', 'GET', '/internal/version', ''), ('S-02', 'POST', '/api/reader?v=1', 'valid.json'), ('S-03', 'POST', '/api/reader?v=2', 'valid.json'), ('S-04', 'POST', '/api/reader', 'valid.json'), ('S-05', 'POST', '/api/reader?v=3', 'valid.json'), ('S-06', 'POST', '/api/reader?v=1&v=2', 'valid.json'), ('S-07', 'POST', '/api/reader?v=1', 'truncated.json'), ('S-08', 'POST', '/api/reader?v=1', 'bom.json'), ('S-09', 'POST', '/api/reader?v=1', 'extra_key.json'), ('S-10', 'POST', '/api/reader?v=1', 'upper_a_id.json'), ('S-11', 'POST', '/api/reader?v=1', 'empty.json'), ('S-12', 'POST', '/api/reader?v=2', 'oversize.json'), ('S-13', 'POST', '/api/reader?v=2', 'oversize.json'), ('S-14', 'GET', '/api/reader?v=2', ''), ('S-15', 'HEAD', '/api/reader?v=2', ''), ('S-16', 'OPTIONS', '/api/reader?v=2', ''), ('S-17', 'PUT', '/api/reader?v=2', ''), ('S-18', 'PATCH', '/api/reader?v=2', ''), ('S-19', 'DELETE', '/api/reader?v=2', ''), ('S-20', 'TRACE', '/api/reader?v=2', ''), ('S-21', 'PROPFIND', '/api/reader?v=2', ''), ('S-26', 'GET', '/api/reader/missing', '')); H=lambda i: [x for x in (r / 'probes' / (i + '.headers')).read_bytes().decode('iso-8859-1').split('\r\n\r\n') if x.strip()][-1].split('\r\n')[1:]; B=lambda f: (r / 'bodies' / f).read_bytes() if f else b''; L=[json.dumps({'probe_id': i, 'method': m, 'target': t, 'request_body_bytes': len(B(f)), 'request_body_sha256': hashlib.sha256(B(f)).hexdigest(), 'status': int((r / 'probes' / (i + '.status')).read_text(encoding='ascii').strip() or '0'), 'headers': [[h.split(':', 1)[0].lower(), h.split(':', 1)[1].lstrip(' \t')] for h in H(i) if ':' in h], 'body': (r / 'probes' / (i + '.body')).read_bytes().decode('utf-8')}, sort_keys=True, separators=(',', ':')) + '\n' for i, m, t, f in P]; Path('audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl').write_bytes(''.join(L).encode('utf-8')); print(len(L))"`. Expected: exit 0 and `22` printed.
43. [C] `sha256sum audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log`.
44. [C] Capture check (final decisive command): `wc -l audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl` (expected `22`).
45. [C] Recording: `python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s=Path('/tmp/hde-epic040-qa-v1.2/sec-reader-http-live'); st=(s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd=tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r=CheckResult(check_id='sec-reader-http-live', check_name='Reader route security over loopback HTTP (closed posture)', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=('audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl', 'audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log',), intended_tokens=(), pf_refs=('PF19-Canon-Glow-QA-Guide',), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"`.

Body additions: in `=== OUTPUT ===`, command 15's poll lines, and for each probe its curl exit code and stderr (the JSONL holds status, headers and body). The probe table of Plan check 10 is not repeated here; the expected status and code of each probe are Kronos's [K] predicates.

[E] predicates (Plan check 10): command 3 printed `000`; command 15 exited 0 before command 16 ran; each of commands 16 to 37 ran (an exit code recorded for each); command 39 exited 0 and command 40 printed `000`; command 42 exited 0; command 44 printed 22.

Status:

- `FAIL_TOOLING`: a probe's capture is missing after it ran; command 42 fails; command 44 does not print 22.
- `TOOLING_BLOCKED`: the gate fails (including `ac040-09-reader-http-in-process` not PASS); port 8000 is unavailable (command 3); the server never becomes ready (command 15 exits 1: connection refused, HTTP 000 or a non-HTTP response).
- `PASS`: every [E] predicate holds. `FAIL_BEHAVIOR` is decided only at QA-110 from the [K] predicates.

[K] predicates (Kronos, from `http_probes.jsonl` and T01's manifest digest): each probe returns the status and code of the Plan check 10 table; every JSON response from S-02 to S-21 has `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store` and no `ETag`; every Reader error body from S-02 to S-21 except the bodiless HEAD probe has exactly the keys `code`, `error`, `ok` (false) and `schema` (`"v1"`), is canonical and ends with exactly one LF; no response body or header from S-01 to S-21 and S-26 contains `Traceback`, `File "`, `psycopg`, `postgresql`, a `gates` key, or a JSON number in a Reader error body. A false predicate makes the per-task result `FAIL_BEHAVIOR` (the server was reachable), or `FAIL_TOOLING` for a malformed capture.

Nonclaims (Plan check 10): no deployed-service, production-environment, live-database or admission-refusal-over-live-HTTP claim; no HTTP claim about the dev routes.

## 6. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from Plan v1.2 §2.3, which carries C040-01 to C040-08 from the QA Audit v1.0 §11 and C040-09's decision from the QA-70 review v1.1. QA-90 adds no entry and changes no field: packaging checks 1 to 10 raised no new conflict. The evidence-storage lane of §4.7 is outside the checks and is named under Glow QA Guide §3.4.9 and Plan §7.2; C040-09's interim treatment (read-only git observations for attribution only, never a PASS gate; tracked harness APIs through `python -c`; no script file; no decisive evaluator written at run time) applies to every task. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 keeps for 2.2 to 2.28. A proposal here is not approval.

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
| Executor identity (§4.1) | The QA-100 operator session; recorded in T01 | PENDING until that session exists |
| Tested source SHA | Recorded by T01 command 3 | PENDING until execution |
| Evidence branch `qa/hde-epic040-qa100-plan-v1.2` and its commit | The QA-100 executor under §4.7 | PENDING until execution; any pull request and merge are the Product Owner's |
| Selection of checks 11 and 12 | Product Owner, through a later QA-90 | Not selected; NOT RUN |
| Review v1.4 N-101 (check 11 `/tmp` files absent before the recording preflight) and N-102 (secret scan by standard input) | Kronos-23, in the QA-90 task for check 11 | Carried |
| QA console checkout, virtual environment and scratch root kept for checks 11 and 12 (§4.3 item 4) | The QA-100 executor and the Product Owner | Required by Plan §7.1 |
| Per-task results, every [K] predicate, disposition of any fault, any attempt 2 | Kronos-23 at QA-110 | After QA-100 |
| Treatment of the `06b04a9` attempts (§4.2) | Kronos-23; restated in the QA-110 result | Decided here for task numbering |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING: no such procedure exists at `53449c9` |

## 8. Working state

| Field | Value |
| --- | --- |
| Stage | QA-90 complete for the selection; next QA-100 |
| Collection | This file, v1.1, `TASK_READY` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.1.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.1.md` |
| Resume point for QA-100 | §4.3 setup, then T01 |

## 9. Nonclaims

This collection executes nothing and produces no evidence. It establishes no QA PASS, acceptance, closure, PF09 status movement, PF-Canon drainage, PF10 addendum, deployment, release activation, token satisfaction or Index/Mirror publication. Every artifact named in §5 is NOT RUN until its task executes.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-90-20260928-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: K040-REQ-003 to K040-REQ-013 as mapped by Plan v1.2 checks 1 to 10
  - prompt: QA-90 — Create Bounded QA Execution Task — 091426.1; Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-90
  - capture_time: 2026-09-28T00:58:31Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_TASK_COLLECTION v1.1, TASK_READY, tasks T01 to T10 at attempt 1, routed to QA-100
  - task_and_attempt_mapping: T01 `d0-discovery`, T02 `step-0b-doc-delta-capture`, T03 `ac040-08-evidence-validators`, T04 `ac040-02-03-catalog-config`, T05 `ac040-04-05-admission-identity`, T06 `ac040-06-golden-comparison`, T07 `ac040-07-gate-ingress-offline`, T08 `ac040-04-09-compat-cli-offline`, T09 `ac040-09-reader-http-in-process`, T10 `sec-reader-http-live`; each attempt 1; result mapping PENDING until QA-100
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `53449c9`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-90-20260927-01 (QA task collection v1.0, not carried forward); GCFPE-USE-HDE-EPIC040-QA-80-20260928-01 (QA Plan v1.2); GCFPE-USE-HDE-EPIC040-QA-70-20260927-04 (QA Plan Review v1.3, DENY); GCFPE-USE-HDE-EPIC040-QA-70-20260928-01 (QA Plan Review v1.4, APPROVE).
