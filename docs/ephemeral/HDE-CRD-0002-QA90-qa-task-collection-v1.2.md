---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-CRD-0002-QA90-QA-TASK-COLLECTION
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.1.md (TASK_READY; task T13-RV1, executed and accepted by QA-110 review v1.1; blob 5a0fb12af755; unchanged). Collection v1.0 (T01 to T15) is unchanged too.
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002 (role and artifact continuity with the author of QA Plan v1.0 to v1.3 and collections v1.0 and v1.1; this invocation runs in a Claude Code CLI session on the Product Owner's workstation, local session 5c9c7c47-41bd-437a-a9ee-63879dec618b, no URL)
session_disposition: continuing Kronos context by artifact lineage, re-entered by the Product Owner pasting the QA-110 handoff to QA-90 v1.0
invocation_binding: CRD / HDE-CRD-0002 / QA-90 / approved QA_PLAN v1.3 checks 16 to 20, attempt 1 each
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8; page state 2026-10-12T02:30:51.327Z; read in full at this invocation, unchanged since collection v1.0)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (QA_PLAN v1.3; blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; 119,368 bytes; immutable)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md (QA_PLAN_REVIEW v1.4, APPROVE by Isis, 2026-10-25T16:38:19Z; blob 10adabfe9fce)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE)
selection: Product Owner SEL-110-1 (QA-110 review v1.1 §5, "Select checks 16 to 21"), narrowed by the Product Owner in this session on 2026-10-25 ("run checks 16-20"; "do not do 21, you won't be able to with open rails") = QA Plan v1.3 checks 16 to 20
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; unchanged since the approval; no addendum after 2.28)
observed_revision: 463cbbef (origin/main at authoring; amthorn78/glow-hdengine-v2#742 merged)
routing: QA-100 — Execute Bounded QA Task — 100926.1, under the Product Owner's execution arrangement of §4.1
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
created_at: 2026-10-25T23:10:00Z
---

# HDE-CRD-0002 — QA Task Collection v1.2 (QA-90): checks 16 to 20 under QA Plan v1.3

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Tasks | T16 `qa-16-deployed-identity`, T17 `qa-17-deployed-not-found`, T18 `qa-18-deployed-dev-surfaces`, T19 `qa-19-deployed-reader-input`, T20 `qa-20-live-vendor-override`; attempt 1 each (§5) |
| Selection | SEL-110-1 (checks 16 to 21), narrowed by the Product Owner to checks 16 to 20. Check 21 is not issued here (§3) |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING` (§2.5) |
| Execution arrangement | Product Owner, 2026-10-25: Kronos executes T16 to T19, and T20's preflight, gate reads and evidence assembly. The Product Owner is check 20's human initiator and types V1 and V2. Check 20's venue is **V-B**, the production service shell, reached with the Railway CLI from the Product Owner's workstation (§4.1) |
| Evidence-only commit grant | Granted by the Product Owner, 2026-10-25, in this session: the Plan §2 grant, bounded as §4.8 states |
| Normalizations | NZ-01, NZ-06, NZ-20 to NZ-25 (§4.10). Each keeps the Plan's objective, target, rails, evidence identity and predicates |
| Publication | One `publish_crd_check_family` call per check through the helper of §4.7. A first publication of each new `check_id` was smoke-validated at `main` (§2.4 row 6) |

This collection is preparation, not an execution result. It executes no check, accepts no evidence and declares no PASS. Collections v1.0 and v1.1 are not reissued.

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md`, blob `3aea6033e3c0`, approved by the QA-70 review v1.4. Governing text: §2 (state (b), execution arrangement, the evidence-only commit permission), §3 (rails by check; E-P and E-V), §4, §5.1 to §5.6, §7 rules A and B, CHECK 16 to CHECK 20, §8, §9.

### 2.2 Overlays

None. HDE Build Notes v13.8 is unchanged since the approval and carries no addendum after 2.28. The Product Owner choices of §4.1 and §4.8 are Plan §2 and §4 inputs, not overlays.

### 2.3 Aids (not overlays)

- The QA-70 review v1.2 N-201 (P4 directory mode `0700`), carried by reviews v1.3 and v1.4; review v1.4 N-303.
- The QA-110 review v1.1 §5 (SEL-110-1; order) and §9 surface advice.
- `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13 (CR-9, interim (a)), applied by T16.
- Collection v1.1 §4: the contract pattern and the helper this collection reuses.

### 2.4 Authoring observations (planning validation, not QA evidence)

Observed by Kronos on 2026-10-25 between 21:40Z and 23:05Z from the Product Owner's workstation (git 2.53.0; CPython 3.12 at `/home/nathan/.local/bin/python3.12`; `curl` at `/usr/bin/curl`). Nothing below is evidence, and nothing was committed or pushed from it.

| # | Object | What ran | Result (observed) |
| :- | :- | :- | :- |
| 1 | Deployed identity | One `curl -sS --http1.1 -m 20` GET of `https://glow-hdengine-v2-production.up.railway.app/internal/version` (QA-110 review v1.1 §9 optional read) | `200 1.1`; six keys in the frozen order; `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; `build_commit` `9479d28` (O-9) |
| 2 | Railway CLI for V-B | Installed by the Product Owner's instruction: Railway CLI 5.71.0 at `~/.local/bin/railway`; `railway login` by the Product Owner (device code); project `ample-illumination` `ce01529f-679f-4f52-a979-23113299a59b`, environment `production` `a06b149a-2876-40bf-84a0-7880feaf8b67`, service `glow-hdengine-v2` `62e7b993-6d30-48b4-9059-c1884b16e90b`; an ed25519 key `glow-workstation` (`SHA256:dD8Nz5fNjfhowDKLHOSYpGO8EObrkOr8IFdxVcFrBlI`) registered on the Product Owner's Railway account; the `ssh.railway.com` host key trusted on first use (`SHA256:+S1xg92FrnHz6pY3bpkmh1OGtWQGNANXilPzlxA7B1g`; Railway publishes no fingerprint) | `railway ssh` connects |
| 3 | Service-shell posture | Read-only `railway ssh` reads, names and rails only | `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`; `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `DATABASE_URL` `SET`; `HDAPI_BASE_URL`, `ENGINE_ENV`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `XDG_STATE_HOME` `UNSET`; `HOME=/root`; effective user `root`; `/app/.venv/bin/python` is Python 3.13.16; default working directory `/app`; `/app/.git` absent; `/root/.local/state/glow-hdengine` absent |
| 4 | V-B P1 reads | From `/app`: `/app/.venv/bin/python -c "import engine; print(engine.__file__)"`; `/app/.venv/bin/python -m engine.cli --version`. From `/tmp`: the same import | From `/app`: `/app/engine/__init__.py`; `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)`, exit 0. From `/tmp`: `ModuleNotFoundError: No module named 'engine'` (NZ-21) |
| 5 | `railway ssh` transport | `printf '[%s]\n' "a b" 'c d'`; a script on stdin exiting 3; the remote wrapper shape of §5 T20 with `--version` | Arguments arrive intact (`[a b]`, `[Amsterdam, NL]`); the remote exit status is returned; stdin is forwarded; the CLI writes one transport line (`Using SSH key from file <path>: <key comment>`) to local stderr, kept apart from the product's streams by NZ-22 |
| 6 | First publication of new check IDs | In a full-history clone of `main` at `463cbbef`, branch `qa/smoke`, CPython 3.12 venv with CI's install, closed rails: the §4.7 helper with stand-in specs for `qa-16-deployed-identity` (PASS stand-in, `evidence_artifacts` the six WU-OPS-01 paths) and `qa-20-live-vendor-override` (`TOOLING_BLOCKED` stand-in); then §4.7's six validators | Both `PUBLISHED`; every validator exits 0; `validate_crd_check_family` lists 17 checks. Changed: the manifest and its proof, the ten updater-owned graph files, and two new check directories. All lie inside the §4.8 grant. The clone was reset afterwards |
| 7 | Consumed Ops evidence | `sha256sum -c SHA256SUMS.attempt1` in `audit/ops/hde-crd-0002/wu-ops-01/` on `main` | 5 of 5 `OK`; `result.attempt1.txt` `classification PASS`; `identity_reads.attempt1.tsv` class `MATCH`, the candidate `release_id` |
| 8 | Delivered sink rule | `engine/bodygraph/vendor_audit.py` `resolve_sink_path` (lines 85 to 106) | As Plan P4 states. With V-B's posture the sink resolves to `/root/.local/state/glow-hdengine/vendor_prod_override.jsonl`, outside `/app` |

### 2.5 Pre-execution assessment

Checks 16 to 20 are complete under Plan v1.3: environment, readiness (rule A, E-P bullet; check 20's P1 to P5), actions, PASS predicates, Outcomes lines, deliverables and publication (§5). Every locus resolves on `main` or in the deployed service (§2.4). There is no `QA_PREEXECUTION_FINDING`.

Execution-time conditions, recorded and not defects:
- **V-B needs the working directory `/app`.** The service image does not install `engine` into its venv; `import engine` resolves through the working directory, as it does for the service's own `gunicorn` process. P1 then holds (§2.4 row 4). NZ-21 runs every V-B command from `/app`, the shell's default.
- **One container.** The sink lives in the container that runs V1 and V2. A redeploy or a second replica between P4 and the after-reads would split or drop the sink. T20 records the container hostname in every remote read and in V1 and V2 (NZ-23); a mismatch is `TOOLING_BLOCKED` before V2, or a recorded gap after it.
- **`build_commit` is not the deployed code identity** (O-9). Plan §2 and HDE Build Notes 2.19 judge the deployed candidate by `release_id` alone. V-B executes the deployed code, which T16 and P1 tie to that `release_id`.

### 2.6 Carried lineage

- Plan v1.2 → checks 1 to 15 executed (collection v1.0) → QA-110 v1.0: 14 `ACCEPT`, check 13 escalated (QA110-F01) → ESC route → WU-REM-02 → Plan v1.3 (QA-80) → QA-70 v1.4 `APPROVE` → collection v1.1 (T13-RV1) → QA-100 v1.1 `PASS` → QA-110 v1.1 `ACCEPT`, SEL-110-1 → this collection.
- Checks 16 to 20 have no earlier attempt. Each task here is attempt 1.

## 3. Selection reconciliation

| Plan check | `check_id` | Selected | Task | Attempt | Depends on | State |
| :- | :- | :- | :- | :- | :- | :- |
| 1 to 12, 14, 15 | `qa-01-preflight` to `qa-15-s01-removal` (not 13) | No | collection v1.0 | 1 | — | Accepted (QA-110 v1.0) |
| 13 | `qa-13-prepush-check` | No | collection v1.1 T13-RV1 | `RV-1` | — | Accepted (QA-110 v1.1) |
| 16 | `qa-16-deployed-identity` | Yes | T16 | 1 | check 1 published (done) | Issued |
| 17 | `qa-17-deployed-not-found` | Yes | T17 | 1 | T16 `PASS` | Issued |
| 18 | `qa-18-deployed-dev-surfaces` | Yes | T18 | 1 | T16 `PASS` | Issued |
| 19 | `qa-19-deployed-reader-input` | Yes | T19 | 1 | T16 `PASS` | Issued |
| 20 | `qa-20-live-vendor-override` | Yes | T20 | 1 | T16 `PASS` in the same session window (V-B) | Issued |
| 21 | `qa-21-evidence-admission` | Selected by SEL-110-1; withdrawn from this run by the Product Owner | none | none | checks 1 to 20 published (Plan §8) | Not issued. Plan §11 needs it before QA-120; a later QA-90 issues it on the Product Owner's selection (§7) |

Order (Plan §8): T16, then T17 to T19 in any order, then T20.

## 4. Common execution contract

### 4.1 Executor, venue and authority (Plan §2; QA-90 "Product Owner execution choice")

- **Product Owner arrangement (2026-10-25, this session).**
  - T16 to T19: Kronos, from the Product Owner's workstation (E-P).
  - T20: venue V-B, the production service shell of `glow-hdengine-v2` (project `ample-illumination`, environment `production`), reached with the Railway CLI from the same workstation. The Product Owner is the human initiator and types and runs V1 and V2, each as one short command (§5 T20, NZ-20). Kronos runs P1 to P5, the gate reads, the after-reads, the secret scan and the evidence assembly. None of those makes vendor I/O.
- Execution authority is not acceptance authority. Evidence returns to Kronos at QA-110; Isis keeps closure.
- QA-100 records the actual executor, venue, tool versions (`curl`, `python3`, `railway`, `git`) and times.

### 4.2 Attempt identity

Attempt 1 for each of the five checks. The executor never reruns on its own. Any outcome other than `PASS` goes to Kronos at QA-110 with its evidence (Plan §9). Check 20 makes at most one allowed invocation (V2) in this attempt.

### 4.3 Setup (not a check)

Fixed scratch locations, all outside every repository (NZ-01):

```text
/tmp/hde-crd-0002-evidence           evidence checkout (full history), branch qa/hde-crd-0002-t16-t20-evidence
/tmp/hde-crd-0002-evid-venv          its venv (CPython 3.12, CI's full install from the evidence checkout)
/tmp/hde-crd-0002-qa                 helper, specs and bodies
/tmp/hde-crd-0002-qa16 to -qa19      T16 to T19 captures
/tmp/hde-crd-0002-qa/qa-20           T20 scripts and captures
```

1. `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-evidence` (no `--depth`); `git -C /tmp/hde-crd-0002-evidence checkout -b qa/hde-crd-0002-t16-t20-evidence origin/main`. Record HEAD. Its history holds `22a3bc0` and its code equals state (b) (Plan §5.4). It holds the published family of checks 1 to 15.
2. `python3.12 -m venv /tmp/hde-crd-0002-evid-venv`; from `/tmp/hde-crd-0002-evidence`: `/tmp/hde-crd-0002-evid-venv/bin/python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; then `python -c "import engine, flask; print(engine.__file__)"` from the checkout prints a path inside it. Tests never run here.
3. `mkdir -p /tmp/hde-crd-0002-qa/qa-20`; write the §4.7 helper to `/tmp/hde-crd-0002-qa/publish_check.py` and record its SHA-256.
4. **E-P shell** (T16 to T19), recorded before the first request:

```text
export SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1
curl --version | head -1; python3 --version
```

5. **Railway prefix** (T20; every V-B read, and the V1 and V2 scripts, use exactly this project, environment and service):

```text
R=(railway ssh -p ce01529f-679f-4f52-a979-23113299a59b -e a06b149a-2876-40bf-84a0-7880feaf8b67 -s 62e7b993-6d30-48b4-9059-c1884b16e90b --)
```

6. **Publication shell** (all five checks): from `/tmp/hde-crd-0002-evidence`, `export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 PATH=/tmp/hde-crd-0002-evid-venv/bin:$PATH`. Publication always runs under the default closed rails (Plan §3.1).

### 4.4 Rails and `captured_env`

- T16 to T19 run under the Production binding set in the E-P shell (§4.3 step 4). Their `captured_env` is `{"LC_ALL":"C","LANG":"C","TZ":"UTC","SAFE_MODE":"0","ALLOW_NETWORK":"1","APP_ENV":"prod"}`, read from that shell when the step ran (Plan §5.3 rule 2).
- T20 runs under the service shell's inherited Production binding; P3 reads it. Its `captured_env` is P3's six values as read.
- A value that differs from the planned one is recorded as read, and the check is `TOOLING_BLOCKED`, rails not as planned.

### 4.5 Step-local readiness (Plan §7 rule A)

- **E-P (T16 to T19):** `curl --version` prints a version; `python3 --version` prints one (the captures are read in the same shell); the six Production binding values are recorded. A failed read is `TOOLING_BLOCKED`.
- **T17 to T19** also record T16's published status and time. If T16 is not `PASS`, they do not start (Plan §8; CHECK 16 Outcomes).
- **E-V (T20):** P1 to P5 are its readiness (§5 T20).
- No installation happens inside a check. The environment is repaired outside it, and the case goes to Kronos.

### 4.6 Capture, body and status

- **HTTP captures** (T16 to T19): every request uses `curl -sS --http1.1`, never `-L`, with headers (`-D`), body (`-o`) and curl's stderr in separate files, and `-w '%{http_code} %{http_version}\n'` on stdout (Glow QA Guide §3.5.10, capture hygiene). Each request is sent once.
- **Header reading.** A header file holds one status line and its headers (no redirect is followed). Header names compare case-insensitively. The status line must start `HTTP/1.1 `.
- **Body comparison** is byte-exact, against the expected bytes plus one LF where the Plan says so.
- **Body** (Plan §5.2), in order: `=== CONTEXT ===` (tested target and candidate; environment class; interpreter and tool versions; rails; a `SET`/`UNSET` table for `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV`; the actor; start and end times; the readiness reads); `=== COMMANDS ===` (each request or command, its curl or process exit code, the `-w` line, the header capture, the body or its length and SHA-256 where the Plan says so, curl's stderr, each separated); `=== PREDICATES ===` (each predicate, its observed value, PASS or FAIL); `=== NOTES ===` (normalizations, observations, nonclaims; for a non-PASS outcome, the cause and the follow-up).
- **LF only** (Plan §5.3 rule 1): normalize CRLF with `sed 's/\r$//'` before any capture enters the body, and note "CRLF normalized to LF". Predicates are judged on the raw captured bytes before normalization.
- **Secret scan** (Plan §5.3 rule 3). For T16 to T19, in the E-P shell, on the body file; the workstation holds `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL`, so the comparison is real:

```text
python3 -I -c "import os,re,sys; t=open(sys.argv[1],encoding='utf-8').read(); v=[os.environ[n] for n in ('HD_API_KEY','GEO_API_KEY','HD_API_BASE_URL','HDAPI_BASE_URL','DATABASE_URL') if os.environ.get(n)]; raw=re.search(r'(Authorization: Bearer|HD-Api-Key:|HD-Geocode-Key:)[ \t]*(?!<redacted>)\S', t); print('HIT' if any(x in t for x in v) or raw else 'NO_HIT')" <body file>
```

  For T20 the same comparison runs inside the service shell, against the service's own values (§5 T20 step A3). A `HIT` quarantines the capture outside the repository and makes the check `FAIL_TOOLING`. Only `HIT` or `NO_HIT` is printed, never a value.
- **`command` and `exit_code`** (Plan §5.2): `command` lists each executed argv in order. T16 to T19 expect every child to exit 0, so `exit_code` is the last decisive child's actual status. T20 follows NZ-20.
- **Status:** each task's PASS predicate and Outcomes line, else Plan §7 rule B in its order. A non-PASS status carries a one-line `status_reason`.

### 4.7 Publication and indexing (Plan §5.4 and §5.5)

**Helper:** collection v1.1 §4.7's helper, unchanged (SHA-256 `8bfbde7cdddfa79cdcbc568096c1f4e8acff23e45c28ee665de12e8ba016b0ae` as extracted from that collection), at `/tmp/hde-crd-0002-qa/publish_check.py`.

**Spec** (`/tmp/hde-crd-0002-qa/<check_id>/spec.json`), one JSON object per check:
- `check_id` and `check_name` (the Plan heading after the ID);
- `status`; `status_reason` (`""` for PASS);
- `command`; `command_provenance` `"QA Plan v1.3 check <N>; QA-90 collection v1.2 task T<N>, attempt 1; normalizations: <those applied>"` (`"Not executed"` when nothing ran);
- `exit_code` (§4.6, or `null` when nothing ran);
- `output_file` the body path;
- `evidence_artifacts`: T16 the six WU-OPS-01 paths of §5 T16; the others `[]`;
- `pf_refs`: T16 `["PF19-Canon-Glow-QA-Guide","PF07-Canon-Glow-Infrastructure","PF04-Canon-HDE-Governance"]`; T17 to T19 `["PF05-Canon-HDE-CLI-API-Vendor-Ref"]`; T20 `["PF05-Canon-HDE-CLI-API-Vendor-Ref","PF19-Canon-Glow-QA-Guide","PF27-Canon-Plan-Templates"]`;
- `captured_env` (§4.4); `captured_at_utc` (the check's finalization time).

**Call**, one per check, in the publication shell (§4.3 step 6):

```text
python -c "exec(open('/tmp/hde-crd-0002-qa/publish_check.py').read())" /tmp/hde-crd-0002-qa/<check_id>/spec.json
```

STOP if the output does not start with `PUBLISHED`. A refused publication changes nothing: correct the assembly from the preserved transcript and publish again; that is not a rerun. A second refusal of the same check goes to Kronos.

**Then, read-only, from `/tmp/hde-crd-0002-evidence`**, after each call, each exit status and output recorded in the QA-100 result:

```text
python tools/evidence/update_evidence_index.py --check
python tools/evidence/orientation_demo.py --check
python tools/evidence/validate_evidence_paths.py
python ci/checks/check_mirror_schema.sh
python tools/evidence/check_lf_endings.py
python -c "import pathlib; from tools.qa.qa_harness import HarnessConfig, validate_crd_check_family as v; print(v(HarnessConfig(crd_id='HDE-CRD-0002', repo_root=pathlib.Path.cwd())))"
```

Expected: each exits 0; `validate_crd_check_family` lists 16, 17, 18, 19, then 20 checks as each is added.

**Registration set** (Plan §5.5), per check: `audit/qa/hde-crd-0002/checks/<check_id>/primary.log` and its `.path_proof.txt`; its manifest entry in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and that file's `.path_proof.txt`; Index keys `audit.qa.hde_crd_0002.checks.<check_id>.primary.log` and `audit.qa.hde_crd_0002.qa_step_logs_manifest` with their Mirror rows; and the ten updater-owned graph files of Plan §2. Never hand-edit any of them; never run the updater in write mode separately.

### 4.8 Evidence files and commit boundary (Plan §2, §5.6)

- Only the writer of §4.7 writes in the evidence checkout. Nothing else is written under `audit/qa/hde-crd-0002/`. Scratch captures, scripts and the WU-OPS-01 files stay where they are.
- **Evidence-only commit grant: granted** (Product Owner, 2026-10-25, this session). The executor may commit and push, on the one branch `qa/hde-crd-0002-t16-t20-evidence`, only `audit/qa/hde-crd-0002/**`, the ten graph files of Plan §2, and its own QA-100 result record (with its checkpoint and handoff) under `docs/ephemeral/`, and open one pull request. No other path, no merge, no force-push.
- Commit after each published check, or at least after T16 and after T20, so that attempt 1's bytes stay in history if a later attempt republishes (Plan §9).
- Expected CI selection for the evidence pull request: lanes `evidence` and `release`. Named risks: FND-024 (PR35-C1) and IR-7. A red run is classified from its log before any re-run.

### 4.9 Stop, recovery and cleanup (Plan §9)

- T16 not `PASS` → T17 to T20 do not start. Publish T16 and route to Kronos.
- T20: any P1 to P5 failure → V1 does not run. Any V1 deviation → V2 does not run. After V2, stop whatever its result.
- An interrupted check restarts from its readiness reads, never from a half-captured state; a request already sent is never re-sent within the attempt. Record the interruption.
- Cleanup after publication and commit: delete `/tmp/hde-crd-0002-qa16` to `-qa19`; in the service shell, delete `/tmp/hde-crd-0002-qa20` (the captures there). The sink file keeps its three events (append-only by design; under V-B it lives on the service host until the container is replaced). Keep `/tmp/hde-crd-0002-evidence` and `/tmp/hde-crd-0002-qa` until QA-110 has read the QA-100 result.
- The Railway key and host key of §2.4 row 2 stay; removing them is the Product Owner's choice (`railway ssh keys remove`).

### 4.10 Normalizations (Glow QA Guide §3.4.7; QA-90 Execute step 5)

| ID | Normalization | Basis |
| :- | :- | :- |
| NZ-01 | The fixed scratch paths of §4.3 instantiate the Plan's scratch directories; another location may be used if recorded | Plan §3.2, CHECK 16 actions |
| NZ-06 | Publication runs the helper file through `python -c "exec(open(<helper path>).read())"` from the evidence checkout's root | Plan §5.4; collection v1.0 NZ-06 |
| NZ-20 | Check 20's V1 and V2 each run as one short script, `/tmp/hde-crd-0002-qa/qa-20/v1.sh` and `v2.sh`, whose exact text is in §5 T20. The Product Owner types `bash <script>` with the `!` prefix of the Claude Code prompt, so the command runs as the Product Owner's own action in the session's shell. Each script runs the Plan's unchanged command in the service shell and asserts its expected status (V1: 1; V2: 0). This is Plan §5.2's "one `bash -c` invocation that asserts each child's expected status", applied per step so that the gate between V1 and V2 stays a separate decision. `command` lists the P reads, `bash /tmp/hde-crd-0002-qa/qa-20/v1.sh`, the gate reads, `bash /tmp/hde-crd-0002-qa/qa-20/v2.sh` and the after-reads; `exit_code` is `v2.sh`'s status, or `v1.sh`'s when V2 did not run | Plan §5.2; CHECK 20 "Initiator"; the Product Owner cannot paste in this environment |
| NZ-21 | Every V-B command runs from `/app`, the service shell's default directory, where `import engine` resolves to `/app/engine/__init__.py` as for the service's own process | Plan §3.2 E-V V-B; §2.4 row 4 |
| NZ-22 | V-B outputs are captured into files by the scripts and reads, not copied by hand. The product's stderr is written to a file inside the container and read back; the Railway CLI's own transport line goes to a separate local file. The Plan's "copied by the initiator, CRLF normalized" is met with the same bytes | Plan CHECK 20 "Evidence"; §2.4 row 5 |
| NZ-23 | Every V-B read, V1 and V2 record the container hostname (`cat /proc/sys/kernel/hostname`) so that one container is shown to hold P4's count, both steps and the after-reads | Plan CHECK 20 P4 and after-reads; §2.5 |
| NZ-24 | P4 creates the sink's directory with mode `0700` (`p.parent.mkdir(mode=0o700, parents=True, exist_ok=True)`), as the QA-70 review v1.2 N-201 cautions; no proof target changes | Review v1.2 N-201 |
| NZ-25 | T17 to T19's request lines, which the Plan names by method, path and body, are written as `curl --http1.1` commands in §5; `HEAD` uses `-I`; `OPTIONS` and `DELETE` use `-X`; a body is sent with `--data-binary`; `//reader?v=1` uses `--path-as-is` so curl keeps the doubled slash | Plan CHECK 16 "Protocol", CHECK 17 to 19 |

### 4.11 Return to QA-110

QA-100 returns, per check: the state (`COMPLETE`, `PARTIAL`, `BLOCKED`, `FAILED` or `NOT_EXECUTED`); the status; attempt 1; the target and the `release_id` read; the primary's path, size and SHA-256; its manifest entry; the two Index keys present; the path proofs validating; §4.7's six validator results; the evidence commit and pull request; the executor, venue and tool versions; every normalization and gap. For T20 also: the venue class (V-B), the initiator attestation as recorded, the container hostnames, P4's sink and count, and the three new sink lines. Missing indexing is incomplete work, never PASS.

## 5. Tasks

Base `B=https://glow-hdengine-v2-production.up.railway.app`. Every request below is sent once, with no auth header.

### T16 `qa-16-deployed-identity` — Service readiness and the deployed candidate's identity (Plan v1.3 check 16; Step-0C; FND-032; FND-031)

- **Binding:** approved Plan v1.3 check 16; review v1.4; Audit v1.0; attempt 1; Production binding; E-P; publication by §4.7; class 1, pre-flight / internal, handled by QA outside the Product Owner's Live QA time (Glow QA Guide §3.5.6).
- **Readiness:** §4.5 E-P. **Depends on:** check 1 published (done).
- **Actions** (Plan check 16, unchanged; scratch `/tmp/hde-crd-0002-qa16`; curl stderr to `<name>.err` beside each capture):
  1. `mkdir -p /tmp/hde-crd-0002-qa16 && curl -sS --http1.1 -D /tmp/hde-crd-0002-qa16/get.hdr -o /tmp/hde-crd-0002-qa16/get.body -w '%{http_code} %{http_version}\n' $B/internal/version 2>/tmp/hde-crd-0002-qa16/get.err`
  2. `curl -sS --http1.1 -I -D /tmp/hde-crd-0002-qa16/head.hdr -o /dev/null -w '%{http_code} %{http_version}\n' $B/internal/version 2>/tmp/hde-crd-0002-qa16/head.err`
  3. `curl -sS --http1.1 -H 'If-None-Match: "qa-hde-crd-0002"' -D /tmp/hde-crd-0002-qa16/inm.hdr -o /tmp/hde-crd-0002-qa16/inm.body -w '%{http_code} %{http_version}\n' $B/internal/version 2>/tmp/hde-crd-0002-qa16/inm.err`
  4. `curl -sS --http1.1 -H 'If-Modified-Since: Sat, 24 Oct 2026 00:00:00 GMT' -D /tmp/hde-crd-0002-qa16/ims.hdr -o /tmp/hde-crd-0002-qa16/ims.body -w '%{http_code} %{http_version}\n' $B/internal/version 2>/tmp/hde-crd-0002-qa16/ims.err`
  5. Step 5 of the Plan, verbatim: the `python3 -I -c` body-form read on `get.body`; then `cmp get.body inm.body` and `cmp get.body ims.body`.
  6. From `/tmp/hde-crd-0002-evidence`: `python -c "import json; [print(e['method'], e['path'], e['a7_eligible']) for e in json.load(open('docs/ENDPOINTS_CATALOG.json'))['endpoints'] if e['path']=='/internal/version']"`.
  7. From `/tmp/hde-crd-0002-evidence/audit/ops/hde-crd-0002/wu-ops-01`: `sha256sum -c SHA256SUMS.attempt1`; read `result.attempt1.txt` and `identity_reads.attempt1.tsv`.
- **PASS:** the Plan's predicate, unchanged: transport (`200` for steps 1 to 4, never `304`, HTTP `1.1`); headers in each of steps 1 to 4 (`Cache-Control: no-store`; `Content-Type: application/json; charset=utf-8`; no `ETag`; no `Last-Modified`); HEAD parity (status, `Content-Type`, `Cache-Control` equal step 1's; `Content-Length` equals step 1's body length; HEAD's empty body not observable with `curl -I`, recorded as a limit); step 5 prints `True True True True True <length>` with `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` and both `cmp` silent; step 6 prints exactly `GET /internal/version False` and `HEAD /internal/version False`; step 7 "5 of 5 OK", result `PASS`, class `MATCH` with the same `release_id`. `build_commit` recorded, never judged.
- **Outcomes:** Plan check 16, unchanged: unreachable or no status line → `TOOLING_BLOCKED` (ops gap, curl exit and stderr kept apart); a different `release_id` → `TOOLING_BLOCKED` ("deployed candidate differs"), routed to the Product Owner; a valid HTTP/1.1 answer contradicting an invariant → `FAIL_BEHAVIOR`. Any non-PASS stops T17 to T20.
- **Consumed Ops evidence** (CR-9 interim (a)): the body lists, and `evidence_artifacts` names, these six paths with their SHA-256 values:

```text
a1c3ba4b61710bf3b19d6dccc297df84d77a48b6ed8a7c9dbbfc05780555ebb8  audit/ops/hde-crd-0002/wu-ops-01/SHA256SUMS.attempt1
a7789c68b0dadf426337e5f5022c6772597f2f747228bdcf246d762b003ef133  audit/ops/hde-crd-0002/wu-ops-01/binding_presence.attempt1.tsv
1f60bf93121c8fe7f2f72747fcfbb926199825fc60fdeca650dd06e6928c4c52  audit/ops/hde-crd-0002/wu-ops-01/expected_identity.attempt1.txt
2e8706fdf578faed07d26772e788539fcc94efb5493043e97fd321991be34acc  audit/ops/hde-crd-0002/wu-ops-01/identity_reads.attempt1.tsv
eb67faccebab0c677e2d53535f1a5eef71f479850c78bb699473729d513bb629  audit/ops/hde-crd-0002/wu-ops-01/result.attempt1.txt
019a6ec6bb20134c69447e56dda467d6402f82f11267945fcf2f764b12db1d1e  audit/ops/hde-crd-0002/wu-ops-01/run.attempt1.log
```

  The executor recomputes each value in the evidence checkout; a difference is `FAIL_TOOLING` (untrustworthy consumed evidence).
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-16-deployed-identity/primary.log`.
- **Nonclaims:** Step-0C identity only; no Reader success, no deployment by QA, no OPS completion.

### T17 `qa-17-deployed-not-found` — Unknown paths answer the governed envelope in the deployed service (Plan v1.3 check 17; S02)

- **Binding:** Plan v1.3 check 17 (FND-004 statement unchanged); attempt 1; Production binding; E-P. **Depends on:** T16 `PASS`. **Readiness:** §4.5.
- **Requests** (scratch `/tmp/hde-crd-0002-qa17`; each `curl -sS --http1.1 -D <n>.hdr -o <n>.body -w '%{http_code} %{http_version}\n' <request> 2><n>.err`):

| n | Request | curl form (NZ-25) |
| :- | :- | :- |
| r1 | `GET /qa-hde-crd-0002-unknown` | `$B/qa-hde-crd-0002-unknown` |
| r2 | `HEAD /qa-hde-crd-0002-unknown` | `-I $B/qa-hde-crd-0002-unknown` (body file not written) |
| r3 | `POST /qa-hde-crd-0002-unknown`, body `{}` | `-X POST -H 'Content-Type: application/json; charset=utf-8' --data-binary '{}' $B/qa-hde-crd-0002-unknown` |
| r4 | `OPTIONS /qa-hde-crd-0002-unknown` | `-X OPTIONS $B/qa-hde-crd-0002-unknown` |
| r5 | `GET /api/qa-hde-crd-0002-unknown` | `$B/api/qa-hde-crd-0002-unknown` |
| r6 | `GET /internal/qa-hde-crd-0002-unknown` | `$B/internal/qa-hde-crd-0002-unknown` |
| r7 | `GET /api/compat/v1` | `$B/api/compat/v1` |
| r8 | `DELETE /internal/version` | `-X DELETE $B/internal/version` |

- **PASS:** Plan check 17, unchanged: r1 to r7 `404`, r8 `405` with `Allow: GET, HEAD, OPTIONS`; every answer `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, no `ETag`, HTTP `1.1`; every body except r2's is exactly `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` plus one LF; r2's body is empty (r2 uses `curl -I`, so its empty body is recorded as not observable, as in T16); no answer `text/html`.
- **Outcomes:** a reachable answer that contradicts a predicate → `FAIL_BEHAVIOR`; transport failure → `TOOLING_BLOCKED`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-17-deployed-not-found/primary.log`. **Nonclaims:** the Reader's unknown-person 404 is excluded (Plan §1).

### T18 `qa-18-deployed-dev-surfaces` — Dev and retired routes refuse in the deployed service (Plan v1.3 check 18; S10, S19)

- **Binding:** Plan v1.3 check 18; attempt 1; Production binding; E-P. **Depends on:** T16 `PASS`. **Readiness:** §4.5.
- **Requests** (scratch `/tmp/hde-crd-0002-qa18`; same capture form as T17):

| n | Request | curl form (NZ-25) | Expected |
| :- | :- | :- | :- |
| d1 | `GET /reader?v=1` | `"$B/reader?v=1"` | 403, `{"code":"ERR_READER_FORBIDDEN","error":"reader endpoint disabled","ok":false,"schema":"v1"}` + LF |
| d2 | `HEAD /reader?v=1` | `-I "$B/reader?v=1"` | 403, empty body (not observable with `-I`; recorded) |
| d3 | `POST /internal/dev/sampler`, body `{}` | `-X POST -H 'Content-Type: application/json; charset=utf-8' --data-binary '{}' $B/internal/dev/sampler` | 403, `{"code":"ERR_WRITER_FORBIDDEN","error":"insufficient scope","ok":false,"schema":"v1"}` + LF |
| d4 | `GET /dev/sampler/conjunction` | `$B/dev/sampler/conjunction` | as d3 |
| d5 | `GET /dev/reader/conjunction` | `$B/dev/reader/conjunction` | as d3 |
| d6 | `GET /dev/writer/conjunction` | `$B/dev/writer/conjunction` | as d3 |
| d7 | `GET /ops/probe/env` | `$B/ops/probe/env` | 404, the `ERR_NOT_FOUND` envelope + LF |
| d8 | `GET /ops/db/unavailable` | `$B/ops/db/unavailable` | as d7 |
| d9 | `POST /ops/writer/diagnostic`, body `{}` | `-X POST -H 'Content-Type: application/json; charset=utf-8' --data-binary '{}' $B/ops/writer/diagnostic` | as d7 |
| o1 | `OPTIONS /dev/sampler/conjunction` (observation) | `-X OPTIONS $B/dev/sampler/conjunction` | none; status, `Allow`, `Location` recorded |
| o2 | `GET //reader?v=1` (observation) | `--path-as-is "$B//reader?v=1"` | none; status, `Allow`, `Location` recorded |

- **PASS:** Plan check 18, unchanged: d1 to d9 as the table states; all nine `application/json; charset=utf-8`, `no-store`, no `ETag`, HTTP `1.1`. o1 and o2 carry no predicate (IR-3; LR5-O1).
- **Outcomes:** a `200` or a handler response on d1 to d9 → `FAIL_BEHAVIOR`; transport failure → `TOOLING_BLOCKED`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-18-deployed-dev-surfaces/primary.log`. **Nonclaims:** no claim from the env guard (IR-4) or the dead `after_request` hook (IR-5).

### T19 `qa-19-deployed-reader-input` — Deeply nested JSON is a typed 422 in the deployed Reader (Plan v1.3 check 19; S19)

- **Binding:** Plan v1.3 check 19; attempt 1; Production binding; E-P. **Depends on:** T16 `PASS`. **Readiness:** §4.5.
- **Inputs** (attacker-suppliable through the public route; HDE Build Notes 2.11 rule 4(c)), written to scratch `/tmp/hde-crd-0002-qa19`:

```text
python3 -I -c "import sys; sys.stdout.buffer.write(b'['*32768)" > /tmp/hde-crd-0002-qa19/b1.json
python3 -I -c "import sys; sys.stdout.buffer.write(b'{\"a_id\":'+b'['*20000)" > /tmp/hde-crd-0002-qa19/b2.json
wc -c /tmp/hde-crd-0002-qa19/b1.json /tmp/hde-crd-0002-qa19/b2.json; sha256sum /tmp/hde-crd-0002-qa19/b1.json /tmp/hde-crd-0002-qa19/b2.json
```

  Expected lengths 32,768 and 20,008 bytes. The bodies are recorded by length and SHA-256 only, never inline.
- **Requests** (same capture form as T17; each `-X POST -H 'Content-Type: application/json; charset=utf-8' --data-binary @<file>`): q1 `"$B/api/reader?v=1"` with `b1.json`; q2 `"$B/api/reader?v=2"` with `b1.json`; q3 `"$B/api/reader?v=1"` with `b2.json`.
- **PASS:** Plan check 19, unchanged: each `422`, `application/json; charset=utf-8`, `no-store`, no `ETag`, HTTP `1.1`, body exactly `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}` plus LF. A `500` or `text/html` fails.
- **Outcomes:** Plan rule B; a reachable contradicting answer → `FAIL_BEHAVIOR`; transport failure → `TOOLING_BLOCKED`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-19-deployed-reader-input/primary.log`.

### T20 `qa-20-live-vendor-override` — The mandatory live vendor call through the production override (Plan v1.3 check 20; S14, S19)

- **Binding:** Plan v1.3 check 20; attempt 1; class 3, vendor, the Product Owner's Live QA workload (Glow QA Guide §3.5.5, §3.5.6); venue **V-B** (§4.1); initiator: **the Product Owner**; authorization reference `HDE-CRD-0002/qa/qa-20-live-vendor-override`; synthetic inputs as the Plan states; request limit: at most one allowed invocation (V2); no `--upsert`; no other vendor command.
- **Depends on:** T16 `PASS` in the same QA-100 session window (record T16's finalization time and P1's time).
- **Script files** (written by the executor from this text, before P1; their SHA-256 values recorded in the body; the Product Owner may read them with `! cat <file>` before running them):

`/tmp/hde-crd-0002-qa/qa-20/v1.sh`

```bash
#!/usr/bin/env bash
# HDE-CRD-0002, QA Plan v1.3 check 20, step V1 (QA-90 collection v1.2, task T20).
# Typed and run by the initiator: ! bash /tmp/hde-crd-0002-qa/qa-20/v1.sh
# Runs the Plan's unchanged V1 command in the production service shell (V-B) and asserts its expected exit status 1.
set -u
D=/tmp/hde-crd-0002-qa/qa-20
date -u +%Y-%m-%dT%H:%M:%SZ >"$D/v1.started_at_utc"
railway ssh -p ce01529f-679f-4f52-a979-23113299a59b -e a06b149a-2876-40bf-84a0-7880feaf8b67 -s 62e7b993-6d30-48b4-9059-c1884b16e90b -- \
  sh -c 'mkdir -p /tmp/hde-crd-0002-qa20 && cat /proc/sys/kernel/hostname >/tmp/hde-crd-0002-qa20/v1.host && cd /app && exec /app/.venv/bin/python -m engine.cli "$@" 2>/tmp/hde-crd-0002-qa20/v1.stderr' sh \
  bg:resolve --user qa-hde-crd-0002-vendor1 --source vendor --dry-run --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL" \
  >"$D/v1.stdout" 2>"$D/v1.transport.stderr"
rc=$?
printf '%s\n' "$rc" >"$D/v1.rc"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D/v1.finished_at_utc"
echo "V1 exit status $rc (expected 1)"
test "$rc" -eq 1
```

`/tmp/hde-crd-0002-qa/qa-20/v2.sh`

```bash
#!/usr/bin/env bash
# HDE-CRD-0002, QA Plan v1.3 check 20, step V2 (QA-90 collection v1.2, task T20).
# Typed and run by the initiator, only after the executor reports that V1 held: ! bash /tmp/hde-crd-0002-qa/qa-20/v2.sh
# Runs the Plan's V2 command (V1 plus the authorization reference) in the production service shell and asserts exit status 0.
set -u
D=/tmp/hde-crd-0002-qa/qa-20
date -u +%Y-%m-%dT%H:%M:%SZ >"$D/v2.started_at_utc"
railway ssh -p ce01529f-679f-4f52-a979-23113299a59b -e a06b149a-2876-40bf-84a0-7880feaf8b67 -s 62e7b993-6d30-48b4-9059-c1884b16e90b -- \
  sh -c 'mkdir -p /tmp/hde-crd-0002-qa20 && cat /proc/sys/kernel/hostname >/tmp/hde-crd-0002-qa20/v2.host && cd /app && exec /app/.venv/bin/python -m engine.cli "$@" 2>/tmp/hde-crd-0002-qa20/v2.stderr' sh \
  bg:resolve --user qa-hde-crd-0002-vendor1 --source vendor --dry-run --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL" --allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override \
  >"$D/v2.stdout" 2>"$D/v2.transport.stderr"
rc=$?
printf '%s\n' "$rc" >"$D/v2.rc"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D/v2.finished_at_utc"
echo "V2 exit status $rc (expected 0)"
test "$rc" -eq 0
```

  No vendor value appears on any argument list; the service process inherits them (Glow QA Guide §3.5.7).
- **Preflight** (executor; no vendor I/O; each through `"${R[@]}"` of §4.3 step 5, from `/app` (NZ-21); each output saved under `/tmp/hde-crd-0002-qa/qa-20/` with the transport stderr apart):
  - **P0 venue:** `railway --version`; `"${R[@]}" cat /proc/sys/kernel/hostname` (the container, NZ-23).
  - **P1 candidate (V-B):** T16 `PASS` with its time; `"${R[@]}" sh -c 'test -x /app/.venv/bin/python && echo P1_EXECUTABLE=OK'`; `"${R[@]}" /app/.venv/bin/python -c "import engine; print(engine.__file__)"` (expected `/app/engine/__init__.py`); `"${R[@]}" /app/.venv/bin/python -m engine.cli --version` (contains `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`).
  - **P2 presence:** `"${R[@]}" sh -c 'for n in HD_API_BASE_URL HD_API_KEY GEO_API_KEY HDAPI_BASE_URL HDE_VENDOR_OVERRIDE_AUDIT_PATH DATABASE_URL ENGINE_ENV; do eval "s=\${$n+SET}"; echo "$n=${s:-UNSET}"; done; if [ -n "${HDAPI_BASE_URL+x}" ]; then [ "$HDAPI_BASE_URL" = "${HD_API_BASE_URL-}" ] && echo HDAPI_BASE_URL_EQUAL=YES || echo HDAPI_BASE_URL_EQUAL=NO; fi'`; then the Plan's `ENGINE_ENV` read, verbatim, as `"${R[@]}" /app/.venv/bin/python -c "<Plan P2 code>"`, printing `P2_ENGINE_ENV=OK`.
  - **P3 rails:** `"${R[@]}" sh -c 'for n in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do eval "v=\${$n-UNSET}"; echo "$n=$v"; done'`; exactly `0`, `1`, `prod`, `C`, `C`, `UTC`.
  - **P4 sink:** `"${R[@]}" /app/.venv/bin/python -c "<Plan P4 code>"` with the single change of NZ-24; holds when it prints `ABSOLUTE_AS_CONFIGURED=True`, `IN_REPOSITORY=False`, `DIR_WRITABLE=True`, `FILE_WRITABLE=True`. Record `ENGINE_ROOT`, `SINK` and `LINES` (P4's count, `L0`).
  - **P5 actor:** `"${R[@]}" /app/.venv/bin/python -c "import os, pwd; print(pwd.getpwuid(os.geteuid()).pw_name)"`, non-empty (expected `root`; IR-1: the account is not proof of a person, the attestation is).
  - Any P row failing → `TOOLING_BLOCKED`; V1 is not run; tell the Product Owner not to run the scripts.
- **Steps:**
  - **V1** (the Product Owner): `! bash /tmp/hde-crd-0002-qa/qa-20/v1.sh`.
  - **A1, V1 gate** (executor; no vendor I/O): `"${R[@]}" sh -c 'wc -c </tmp/hde-crd-0002-qa20/v1.stderr; cat /tmp/hde-crd-0002-qa20/v1.stderr; cat /tmp/hde-crd-0002-qa20/v1.host'`; `"${R[@]}" sh -c 'tail -n +"$(( $1 + 1 ))" "$2"' sh <L0> <SINK>`; parse `v1.stdout` with `python3 -I`. V2 may follow only when every V1 predicate below holds, the V1 host equals P0's, and the new-line count is exactly 1. Otherwise the executor stops and tells the Product Owner not to run V2.
  - **V2** (the Product Owner, after the executor reports A1 held): `! bash /tmp/hde-crd-0002-qa/qa-20/v2.sh`.
  - **A2, after-reads** (executor): `"${R[@]}" sh -c 'wc -c </tmp/hde-crd-0002-qa20/v2.stderr; cat /tmp/hde-crd-0002-qa20/v2.stderr; cat /tmp/hde-crd-0002-qa20/v2.host'`; `"${R[@]}" sh -c 'tail -n +"$(( $1 + 1 ))" "$2"' sh <L0> <SINK>` (all lines after P4's count, three expected); `"${R[@]}" cat /proc/sys/kernel/hostname`.
  - **A3, secret scan in the service** (Plan §5.3 rule 3, against the service's values): `cat v1.stdout v1.product.stderr v2.stdout v2.product.stderr sink_new_lines.txt | "${R[@]}" /app/.venv/bin/python -c "<§4.6 scan, reading sys.stdin instead of a file>"`, printing only `HIT` or `NO_HIT`. The same scan also runs locally on the assembled body (§4.6).
  - **Attestation:** after V2 (or after V1 when V2 does not run), the executor asks the initiator for one line naming their role and stating that they typed and ran V1 and V2 themselves, and records it verbatim.
  - V-A's `git status --porcelain` is not applicable under V-B; recorded with the reason (no tracked checkout in the container; `/app/.git` absent).
- **PASS:** Plan check 20, unchanged:
  - V1 exits 1; stdout is a `status` `error` envelope with code `PROVIDER_PROD_OVERRIDE_REQUIRED` and `error.details.outbound_attempted` `false`; the product's stderr is empty (0 bytes in `v1.stderr`); exactly one new sink line: event `vendor_prod_override`, outcome `refused`, `error_code` `PROVIDER_PROD_OVERRIDE_REQUIRED`, `authorization_ref` `null`, `outbound_attempted` `false`.
  - V2 exits 0; stdout `status` `ok`; `resolver.route_policy.route_family` `recommended_v2_chart` and `resource_path` `charts`; `adapter.status` `mapped` with `payload_family` `ChartResult`; `cache.payload_posture` `adapter_mapped_no_raw_vendor_payload`; `ingest.rows_written` 0; the request posture lists `Authorization: Bearer <redacted>` and `HD-Geocode-Key: <redacted>` and no `HD-Api-Key`.
  - Exactly two further sink lines with one shared `correlation_id`: first outcome `allowed` (`authorization_ref` the reference, `outbound_attempted` `false`, `route_family` `null`), then `completed` (`outbound_attempted` `true`, `route_family` `recommended_v2_chart`, `resource_path` `charts`, `error_code` `null`).
  - Every new sink line has the sixteen keys of HDE CLI/API/Vendor Ref §7.1.11f, `actor_principal` equal to P5's account, and no user key, birth data, location, URL, header, key or raw provider text.
  - V-A git status: not applicable (V-B). Secret scans `NO_HIT`. All hostnames equal (NZ-23).
- **Outcomes and classification:** Plan check 20, unchanged (P-row failure → `TOOLING_BLOCKED`, V1 not run; configuration or tooling codes → `TOOLING_BLOCKED`; `FAIL_BEHAVIOR` only when P1 to P5 hold and the output or events contradict §7.1.11c to §7.1.11f; any V1 deviation → V2 not run; a secret hit → `FAIL_TOOLING` and quarantine). Added by NZ-23 and NZ-22, as tooling: a hostname mismatch before V2 → `TOOLING_BLOCKED`, V2 not run; a transport failure of `railway ssh` (no product output, a CLI error on the transport stderr) → `TOOLING_BLOCKED`, classified from the transport stderr before any action. `v1.sh`'s exit status alone never decides V1: an exit 1 with no envelope on stdout is a transport failure.
- **Evidence** (all in the primary; no sidecar; IR-6): venue class V-B and its Railway identifiers; the initiator attestation; the script texts' SHA-256 values; P0 to P5; V1 and V2 argv as run in the container; their stdout (canonical JSON; the mapped record of the synthetic input, no raw vendor payload), the product's stderr and the transport stderr, kept apart, and exit codes; the three new sink lines verbatim; the hostnames; the secret-scan results; the classification; the nonclaims.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-20-live-vendor-override/primary.log`.
- **Nonclaims:** Plan check 20, unchanged: no broad HumanDesignAPI v2 conformance, mapped-cache write, database write, deployment, QA PASS for the change or closure. V-B is a call inside the deployed service's container, through the CLI, not a request to the service's HTTP surface.

## 6. CANON_CONFLICT_REGISTER (carried)

Held in full in the approved Plan v1.3 §13; carried unchanged:

| ID | Status | Decision owner | Bearing on these tasks |
| :- | :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth | None |
| CR-4 | `APPROVED` | Product Owner | None |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner | None |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20 | None |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner | None |
| CR-9 | `PROPOSED`, unreviewed | Isis, IA-30 boundary | T16: interim (a), the consuming primary names the six WU-OPS-01 paths |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40 | §4.7 publication (the `crd_id` key) |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis, QA-70 review v1.0 | T20: vendor evidence lives in the primary only |
| CR-12 | `APPROVED`, alternative (a) | Product Owner, 2026-10-25 | None |

QA-90 proposes no new conflict.

## 7. Constraints, open inputs and unresolved items

| Item | Owner | State |
| :- | :- | :- |
| Check 21 `qa-21-evidence-admission` | Product Owner (selection); Kronos at a later QA-90 | Withdrawn from this run by the Product Owner; Plan §11 needs it before QA-120 |
| O-9: `/internal/version` reports `build_commit` `9479d28` (an EPIC-005 commit, an ancestor of `22a3bc0`), not the deployed code's commit | Recorded; Plan judges by `release_id` | Observation for QA-110; never judged (Plan check 16) |
| Railway access added for V-B (CLI 5.71.0, the `glow-workstation` key, the trusted host key) | Product Owner | In place; removal is the Product Owner's choice |
| A redeploy between P4 and A2 would replace the container and its sink | Executor | Detected by NZ-23; T16 to T20 run in one window |
| O-1, O-2, O-5, O-7 | As QA-110 review v1.1 §8 records them | Unchanged |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| G-1; PO-2 and PO-5 drainage; O-A, D-1/LR6-O1, FND-028 | As HDE Build Notes 2.28 and review v1.1 §8 record them | Unchanged |

## 8. Working state

QA-90 for checks 16 to 20 is complete at `TASK_READY`. No task has run. Next: QA-100 under §4.1's arrangement, after this collection reaches `main`. On a repeated QA-90 invocation for this selection, reuse T16 to T20 unchanged unless a QA-110 decision says otherwise; issue check 21 only on the Product Owner's selection.

## 9. TypeSafe reading for the receiving session (QA-100)

Action sent (v8.2): "Execute five existing, already-reviewed bounded QA tasks for one change request, following their written commands: four read-only HTTP probe tasks against the deployed production service (about twenty-five requests in all, with an identity preflight that gates the other three), and one mandatory live vendor call against a provider under open rails in the production service shell, whose preflight the executor runs and whose two vendor commands the Product Owner types in person, each judged against written pass predicates and published as one evidence log per task through the repository's canonical evidence writer with read-only validation, recorded in a Markdown result record. No new code runs; an independent evidence review follows."

- **TypeSafe: not read.** As printed: "TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-25T23:02:50Z). Do not fill in a reading by hand."
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, session kind `review`, label "QA-100 HDE-CRD-0002 tasks T16 to T20 (QA Plan v1.3 checks 16 to 20)". A first send at 2026-10-25T23:02:39Z, on a text that differed only in the wording of who types the two commands, also returned HTTP 403; the wording was corrected and the text re-sent once. Neither send produced a reading.
- **Records:** the Notion row was not written.
- **Picks:** QA-100: Nathan's pick is not stated. This QA-90: Nathan's pick is not stated; its reading is in the QA-110 review v1.1 §9 (Opus 5.5 at high, score 2.03).

**Surface advice.**
- **Session.** QA-100 runs where the Product Owner runs the Railway CLI: this workstation session, which holds `railway` 5.71.0 signed in to the Product Owner's account, the registered key and the trusted host key, and lets the Product Owner type V1 and V2 with the `!` prefix. A cloud session would need its own Railway sign-in and key, and could not let the Product Owner type into its shell.
- **Time.** Setup about 5 minutes; T16 to T19 a few minutes each; T20's preflight about 3 minutes (each `railway ssh` call takes a few seconds), then two typed commands with a gate read between them; publication and validation a few minutes per check.
- **Access.** GitHub read and push (evidence branch only); HTTPS to the production service; Railway SSH to the production service. The vendor is reached only by V2, from inside the service.
- **Writes.** The canonical writer's paths in the evidence checkout (§4.7, §4.8); the QA-100 result record, checkpoint and handoff under `docs/ephemeral/`; scratch under `/tmp`; one directory in the container's `/tmp` and the sink's directory and file under `/root/.local/state/glow-hdengine/`.
- **Reads.** This collection; Plan v1.3 checks 16 to 20, §3, §5, §7 rules A and B, §8, §9.

## 10. Nonclaims

This collection is preparation. It executes no check, publishes no evidence, makes no QA verdict, accepts nothing, and establishes no S-requirement, deployment, release activation, Live QA completion or closure. The authoring observations of §2.4 are not evidence.

## Canon relied on

Read on `main` at `463cbbef` (`docs/pfcanon/` last changed by `21141b39`; this branch edits no `docs/pfcanon/` file).
- QA-90 — Create Bounded QA Execution Task — 100926.1 (page state 2026-10-12T02:30:51.327Z), read in full at this invocation.
- PF19-Canon-Glow-QA-Guide v3.0.6: §3.5.5 (vendor-first rails; production-affecting minimum; the mandatory live vendor test), §3.5.6 (class labels), §3.5.7 (vendor evidence; environment-held configuration; presence-only; secret scan), §3.5.10 (TOOLING_BLOCKED for HTTP surfaces; capture hygiene), read in full at this invocation; §3.4.7, §3.4.8 and §11.1 (read at collection v1.0; unchanged).
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11e (the authorized initiator: an authenticated human Product Owner or a delegated human operations executor; actor identity from the authenticated environment), read at this invocation; §7.1.11 to §7.1.11f as the Plan and the QA-70 reviews read them.
- PF27-Canon-Plan-Templates v2.0.5 "Exact status predicates", "Causal precedence", "Bounded step-level rerun posture" (read at QA-80; unchanged).
- HDE Build Notes v13.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md`): addenda 2.27 and 2.28 (read in full at QA-80 and QA-110 in this role's lineage), 2.19 (deployment by commits on `main`; judged by `release_id`), 2.11 rules 4 to 6 (real inputs). No addendum post-dates the approval.
- In-flight: approved Plan v1.3 checks 16 to 20, §2 to §5, §7, §8, §9 (re-read here); the QA-70 reviews v1.4 (N-301 to N-303) and v1.2 (N-201); the QA-110 review v1.1 §5 to §9; the WU-OPS-01 Ops task §13 (CR-9); collection v1.1 §4.

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-90-20261025-03 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | S02, S10, S14, S19 and Step-0C; QA Plan v1.3 checks 16 to 20; tasks T16 to T20, attempt 1 |
| prompt | QA-90 — Create Bounded QA Execution Task — 100926.1, page state of 2026-10-12T02:30:51.327Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-90 (`TASK_READY`) |
| capture time | 2026-10-25T23:10:00Z |
| execution identity | Claude Code CLI session on the Product Owner's workstation, local session 5c9c7c47-41bd-437a-a9ee-63879dec618b (no URL; no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-90-20261024-01 (collection v1.0); GCFPE-USE-HDE-CRD-0002-QA-90-20261025-02 (collection v1.1); each in its artifact |
| task/result mapping | T16 to T20 → Plan v1.3 checks 16 to 20 → QA-100 result pending |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
