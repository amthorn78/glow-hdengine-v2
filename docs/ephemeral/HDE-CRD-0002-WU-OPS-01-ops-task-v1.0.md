---
artifact_type: OPS_TASK
artifact_id: HDE-CRD-0002-WU-OPS-01-OPS-TASK
artifact_version: "1.0"
task_state: READY
execution_state: NOT_EXECUTED (this record creates the task; nothing in it has run against production)
template: PF27-Canon-Plan-Templates v2.0.5, §3 Ops Task Record (Template), including its controlled execution contract
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
OPS_UNIT_ID: WU-OPS-01
task_id: WU-OPS-01
work_unit_title: "Place the QA candidate and record the deployment facts (Ops; Coagulation; PO-only execution, IA-guided)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
IMMUTABLE_APPROVED_BASE:
  - docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (Specification v1.1, approved; blob c4802a5a7fa3)
  - docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (Implementation Plan v1.1; blob abffa2ccbd44), approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
overlays: (1) Specification delta 01, docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md), PF10 addendum 2.20; (2) Implementation Plan delta 01 v1.1, docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (blob 5103fe29d588; DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md), PF10 addendum 2.19, whose P-9, P-18, P-19 and P-20 set this unit; (3) PF10 addendum 2.18 (no cost ceiling); (4) the business case, docs/ephemeral/HDE-CRD-0002-WU-OPS-01-po-disposition-business-case-v1.0.md §2 (blob a2ece720ff42; #702). Overlay scope: WU-OPS-01's Intent, PF07 posture, External execution classification, Success criteria and Constraints, and R-9's removal. The bases are not edited
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, with Specification delta 01
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (blob b39ac9f276db)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md §7 WU-OPS-01, with Plan delta 01 v1.1 P-9, P-18, P-19, P-20
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (INITIAL_APPROVE), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (DELTA_APPROVE)
dependency_receipts: WU-PR-08 accepted (docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-work-unit-lineage-review-v1.0.md, PR-40 ACCEPT; #688); WU-DOC-01 COMPLETE (docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.1.md, DOC-20; blob aed23f6577a3; #702)
rescope_or_remediation_reentry: none
CURRENT_PF10_MARKDOWN_LINK: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff)
ACTIVE_PF10_ADDENDA_LINKS:
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.11 (business case; real inputs only), as §2.18 narrows it
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.18 (no cost ceiling); record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-no-cost-ceiling-v1.0.md
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.19 (Plan delta 01; WU-OPS-01 proves deployment by release_id); record docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-PF10-build-notes-addendum-v1.0.md
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.20 (Specification delta 01; release stays 1.3.0); record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md
pf10_addendum_created: none (OPS-10 is not an addendum producer)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
creator_ia: the continuing whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N); task author and future task-acceptance owner at OPS-30
receipt_destination: OPS-30 — Review Ops Execution Receipt — 100926.1 (AI Prompts / HDE IA), run by the creator IA; the receipt is saved as docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md
executable: docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh (12,531 bytes, 237 lines; sha256 960eabe59b6cc4abda69cf90320fb91abd3f10520830e2fb2fd346f2df7ad0d9)
prompt: OPS-10 — Create Bounded Ops Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81509957c43992c03625; page state of 2026-10-12T02:29:29.013Z, read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_head_read: origin/main 8e6f238 (#702). Every repository fact below was measured at this head
created_at: 2026-10-22T05:15:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; CR-9 new, PROPOSED (§13)
---

# HDE-CRD-0002 WU-OPS-01 — Ops Task Record v1.0

## 1. Result

**READY. Not executed.** This record creates the task. Nothing in it has run against production.

- **What the task does:**
  - reads `GET /internal/version` on the production HD Engine base URL;
  - confirms the candidate's `release_id`, `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, at version `1.3.0`;
  - records whether the seven named production variables are set, without any value;
  - stores the outputs under `audit/ops/hde-crd-0002/wu-ops-01/`.
- **Executable:** one versioned script, `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh`. These bytes were rehearsed on 19 cases against loopback targets, and every case behaved as designed (§10).
- **One Plan conflict, CR-9 (§13).** The Plan asks for path proofs under the Ops root. No canonical writer can write them there, and canon forbids anyone else from writing them.
  - Interim treatment: canon governs. The executor writes no path proof, and path-proof coverage comes when QA consumes the evidence.
  - It does not block execution. It needs Isis's disposition.
- **Owner and executor:** the Product Owner, or an agent the Product Owner delegates. Any rollback is the Product Owner's alone (§9).

## 2. Authority, Plan location and dependencies

- **Plan location:** Implementation Plan v1.1 §7, block "WU-OPS-01". It is read with Plan delta 01 v1.1:
  - P-9: Intent, Success criteria and Constraints;
  - P-18: PF07 posture;
  - P-19: External execution classification;
  - P-20: R-9 removed.
  - The other fields are unchanged: Task ID, Owner, Facilitator, Executor, Secret posture, Dependencies and Nonclaims.
- **Authority:**
  - The Product Owner authorizes Ops tasks and owns accountability and acceptance (Plan Templates §3, "Execution authority"; HDE Governance §9.1, "Ops tasks", item 1).
  - The approved Plan names the Product Owner as owner and executor, or "a PO-delegated automated session agent under the same controls".
  - The Product Owner gives the action authority by invoking OPS-20 on this record. That authority covers:
    - the HTTPS read;
    - the variable-presence observation;
    - the evidence pull request.
  - A rollback needs a separate, explicit Product Owner action (§9).
  - No production configuration change is authorized.
- **Dependencies:**
  - **"After WU-DOC-01": met.** DOC-20 v1.1 is `COMPLETE` (#702).
  - **WU-PR-08: accepted** (PR-40 v1.0 `ACCEPT`, #688).
  - **Business case: adopted** (#702).
  - **"Before the QA Plan's live steps":** no QA Plan exists yet.
- **The candidate:**
  - "The `main` head after WU-PR-08 and WU-DOC-01 merge" is any `main` commit containing `f508dcf`, WU-DOC-01's last merge (#700).
  - Its release is `1.3.0`, built `2026-08-24T18:04:49Z`, with 45 members and `release_id` `77204764…c51e` (§12).
- **Repeat-invocation check:** no earlier WU-OPS-01 task, result or receipt exists in `docs/ephemeral/` or `audit/ops/`. Only the business-case record does. This is the first task version.

## 3. Ops Task record fields (Plan Templates §3)

| Field | Value |
| :- | :- |
| **Task ID** | `WU-OPS-01` (HDE-CRD-0002) |
| **Owner** | `PO` |
| **Facilitator** | `IA` (the creator IA above) |
| **Executor** | `PO`, or `PO-delegated automated session agent` |
| **PO delegation record, when delegated** | The Product Owner's direct instruction is the OPS-20 handoff the Product Owner pastes into the executing session. It names Task ID `WU-OPS-01`, this record (v1.0), the objective (§1), the target (§4) and the approved scope (§6, operations O-1 to O-7). The delegated executor records that session's URL as `DELEGATION_REF`, a secret-free reference. The Product Owner writes no delegation text |
| **Task-specific authorization identity and dispatch-boundary validity** | None. There is no credential, token or time-bound authorization; the read sends no credential header (HDE Governance §10.5). STOP CHECK before dispatch: P-0 and the script's preflight P-1 to P-8 pass (§5) |
| **Objective blocker and resume posture** | No blocker is known. If an executor lacks HTTPS egress to the base URL, or cannot see the Railway variable list, the affected step is `TOOLING_BLOCKED`; the executor preserves the outputs and the Product Owner supplies the access. A delegate without Railway access answers `NOT_OBSERVED` and does not guess |
| **PF07 posture** | `PF07-derived`: provider Railway; project `ample-illumination`; service `glow-hdengine-v2`; base URL `https://glow-hdengine-v2-production.up.railway.app` (Glow Infrastructure §2.2, §2.6, §3.1, §4.1); repository `amthorn78/glow-hdengine-v2`, default branch `main` (§3.3); the production variable names (§2.4); `/internal/version`, ops-only and identity-only (§2.3.3, §4.1). The deploy source is a Product Owner-provided fact (Plan delta 01 P-18): the candidate reaches the service when its commit lands on `main`. `PF07-gap`, for the conditional rollback only: PF07 does not state how a previous Railway deployment is redeployed (§9) |
| **Infra/ops fact inventory** | Target provider: Railway. Target project: `ample-illumination`. Target service: `glow-hdengine-v2`. Target repository: `amthorn78/glow-hdengine-v2`. Target base URL: `https://glow-hdengine-v2-production.up.railway.app`. Target database instance or schema: not applicable (no database access). Exact config key names: `APP_ENV`, `SAFE_MODE`, `ALLOW_NETWORK`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`. Governed evidence root: `audit/ops/hde-crd-0002/wu-ops-01/` (Plan v1.1 §4 invariant 6). Expected value: `release_id` `77204764…c51e`, from `catalog/manifest.json` on `main` (§12); PF07 records the variable values, but this task records presence only (Plan Secret posture) |
| **PF07 gap statement** | (1) The Railway procedure for redeploying a previous deployment is not in PF07, and no other canon gives it. Only the conditional rollback is affected (§9). (2) PF07 does not label the Railway environment that serves the base URL. The task calls it "production" (PF07 §2.4 heading "Production — Railway"; database instance `ample-illumination/production/postgres`, §2.2). The operator observes the environment that serves the base URL. Neither gap blocks the read or the probe |
| **External execution classification** | Hosted-service operation (Plan delta 01 P-19): a read of `/internal/version`, a presence-only probe of the bindings, and a redeploy of the previously deployed commit only under the rollback intent. No vendor call and no database write |
| **Exact command proof** | §4 and §6. The executable is the rehearsed script; the evidence steps are standard `git` and `sha256sum` commands |
| **Input identity boundary** | No app user IDs, no `person_uid`, no `user_id`, no chart or birth data. The task reads only the service's identity |
| **Secret persistence posture** | `presence-only`. No variable value, no response body, no response header value and no credential appears in any output |
| **Non-claims preserved** | Delegation does not turn Ops into PR or QA work. No QA PASS, Live QA completion, acceptance-token satisfaction, PF09 or PF30 status change, change completion, deployment success beyond the evidenced target, or closeout |
| **Completion-claim boundary** | WU-OPS-01 is complete only when its secret-free evidence is in the repository, meets §7's success criteria, and OPS-30 accepts it |
| **Intent / desired end state** | The Railway production service runs the accepted candidate, so that the QA Plan's bounded open-rails live steps exercise it: S02 and S10 in the deployed target, and S14's live vendor call from the operator shell against the production rails (Plan delta 01 P-9). This task proves that state; it does not create it. The candidate is deployed by its commit landing on `main` |
| **Constraints / safety rails** | No production configuration change. No discovery or recording of the deployment trigger, build command or start command, and no inspection of the deploy pipeline or the service settings (Plan delta 01 P-9). The presence probe the Plan requires reads variable names only. No vendor call and no database access. No credential header and no other endpoint. Nothing is written in the repository until the script has exited |
| **Success criteria** | §7: SC-1 to SC-4 |
| **Closure dimension** | Supports QA readiness only (Plan v1.1 §9 item 1, "WU-OPS-01 is planned (OPS-10) or executed"). It is the deployed-candidate identity for the QA Plan's live steps |
| **Closure mode** | `direct runtime validation` of the running service's release identity |
| **Unchanged runtime facts already evidenced** | Not applicable |
| **Governed evidence family to normalize** | Not applicable. The task creates Ops evidence and no Index, Mirror or INTVER family entry (§8, CR-9) |
| **Superseded contradictory artifacts** | None for this task. Plan v1.1's original WU-OPS-01 text (deployment trigger, build command, `1.4.0`) is superseded by Plan delta 01 |
| **Evidence to capture** | §8 |
| **Rollback intent** | Redeploy the previously deployed commit, only when the service did not answer any read (§9) |
| **Secret handling note** | No plaintext secret in any document or evidence. The script records variable names and SET or UNSET only. It deletes all of its output if its secret scan finds a credential pattern |
| **Canon-grounded instructions** | Carried into §4 to §9: HDE Governance §10.5 (no auth header may be required; the six-field identity body; 200 on success); HDE Governance §9.1, "Ops tasks", items 1 and 4 (delegation predicates; text-first evidence under a lowercase audit path; presence-only; the environment-validation disposition rule); Plan Templates §0, "Exact technical facts and secret safety" (record presence only as `SET` or `UNSET`; scan output before it enters evidence; no guessed values); HDE Schemas and Artifacts §8.3, "Join to the human index (parity, proofs, same-PR rule)" (a path proof belongs to an Evidence Index entry; `tools/evidence/update_evidence_index.py`, the single writer, regenerates all governed path proofs; proofs are never hand-edited), and the §8.6.3 family entries that repeat it ("Feature producers MUST NOT write Index, Mirror, path-proof, checksum, sentinel, or orientation companions"); Glow QA Guide §11.1, the paragraph after the roles table ("Ops evidence remains distinct under `audit/ops/<change-id>/<task_id>/`"). Canon gives no command for listing Railway variables or for redeploying a Railway deployment; those steps are stated as requirements, not invented commands (§6, §9) |

## 4. Controlled execution contract

| Item | Value |
| :- | :- |
| **Command source** | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh`, sha256 `960eabe59b6cc4abda69cf90320fb91abd3f10520830e2fb2fd346f2df7ad0d9`, 12,531 bytes, run unedited |
| **Command substitution source** | Four environment parameters, all validated by the script: `EXECUTOR` (`PO` or `PO-delegated-agent`); `DELEGATION_REF` (delegated only: the executing session's URL, printable ASCII, at most 256 characters); `WORK_DIR` (an absolute path outside the checkout, absent or empty); `ATTEMPT` (a positive integer, `1` for the first run). The seven presence answers are typed at the script's prompts: `SET`, `UNSET` or `NOT_OBSERVED` |
| **Executable command artifact** | The script file above. The executor runs it from the checkout, `bash docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh` |
| **Placeholder rule** | The script holds no placeholder. A missing or invalid parameter stops it at preflight with `PREFLIGHT_FAIL` and exit 3 (`TOOLING_BLOCKED`) |
| **Target classification** | Hosted-service operation |
| **Required target facts** | Command target: `GET https://glow-hdengine-v2-production.up.railway.app/internal/version`, HTTPS only (`curl --proto =https`), 30-second limit per read. The request sets one header, `Accept: application/json`, beside curl's own `Host` and `User-Agent`; it carries no credential or override header. Data sources: the service's identity response, and `catalog/manifest.json` in the checkout. Execution context: a shell with bash 4 or later, `curl`, `python3` (standard library only), `git` and `sha256sum`; a clean checkout of `amthorn78/glow-hdengine-v2` `main` containing `f508dcf`, run from its root; HTTPS egress to the base URL; sight of the variable list of the Railway service in the production environment. Config keys and credential keys in the operator shell: none; the script reads no environment value but its four parameters. Deterministic pins: the script sets `LC_ALL=C LANG=C TZ=UTC`. Rails: the script runs no product code, so `SAFE_MODE` and `ALLOW_NETWORK` are not consulted; the only network action is the Plan-authorized HTTPS read of one host. Application environment: the target's values are not read; presence only |
| **Target facts not required for this classification** | The database instance and schema (no database access); variable values (presence only, Plan Secret posture); the deployment trigger, build and start commands (excluded by P-9 and P-18); the Railway region and project ID (PF07 TBD, not used); vendor facts (no vendor call); the repository package install (no product code runs) |
| **Target-change rule** | A different base URL, candidate `release_id`, endpoint or classification returns the task to the creator IA (OPS-10) before execution. Glow Infrastructure owns a replacement base URL. The script refuses a checkout whose release differs from the pin |
| **Prerequisite proof** | WU-PR-08 accepted (#688); DOC-20 v1.1 `COMPLETE` (#702); this record and its script merged on `main` |
| **Preflight matrix** | §5 |
| **Execution wrapper or operator command** | §6, O-3 |
| **Run rules** | §7.3 |
| **Required evidence outputs** | §8.2 |
| **Required content for evidence outputs** | §8.2 |
| **Outcome classification map** | §7.2 |
| **Non-claims** | No QA PASS, Live QA completion, final acceptance, public-surface change, CLI flag change, PF09 or PF30 status change, change closure or PF-canon drainage. The task claims none of HDE Governance §2.0.2's `/internal/version` tokens and produces no INTVER family artifact |

## 5. Preflight matrix

P-0 is the executor's step. P-1 to P-8 run inside the script, before any read.

| ID | Requirement | Required proof | Status rule |
| :- | :- | :- | :- |
| P-0 | Script identity | `sha256sum docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh` prints `960eabe59b6cc4abda69cf90320fb91abd3f10520830e2fb2fd346f2df7ad0d9` | Otherwise do not run; `TOOLING_BLOCKED`, return to the creator IA |
| P-1 | Parameters valid | `ATTEMPT` a positive integer; `WORK_DIR` absolute, outside the checkout, absent or empty; `EXECUTOR` `PO` or `PO-delegated-agent`; `DELEGATION_REF` present when delegated; no rehearsal variable in execution | `PREFLIGHT_FAIL`, exit 3 |
| P-2 | Tools present | bash 4 or later; `curl`, `python3`, `git`, `sha256sum` on `PATH` | `PREFLIGHT_FAIL`, exit 3 |
| P-3 | Run from a repository root | `git rev-parse --show-toplevel` equals the working directory | `PREFLIGHT_FAIL`, exit 3 |
| P-4 | Candidate included | `f508dcf` exists and is an ancestor of `HEAD` | `PREFLIGHT_FAIL`, exit 3 |
| P-5 | Clean tree | `git status --porcelain` prints nothing | `PREFLIGHT_FAIL`, exit 3 |
| P-6 | Attempt number unused | No `audit/ops/hde-crd-0002/wu-ops-01/*.attempt<N>.*` exists in the checkout | `PREFLIGHT_FAIL`, exit 3 |
| P-7 | Candidate release | `sha256(catalog/manifest.json)` equals `77204764…c51e`, with version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z` and 45 members | `PREFLIGHT_FAIL`, exit 3; return to OPS-10 |
| P-8 | Mode | Execution mode targets only the PF07 base URL over HTTPS. Rehearsal mode accepts only `http://127.0.0.1:<port>` and is never evidence | `PREFLIGHT_FAIL`, exit 3 |

## 6. Bounded ordered operations

- **O-1. Prepare the checkout.**
  - Use a clean checkout of `amthorn78/glow-hdengine-v2` at current `main`, for example `git fetch origin main` and `git switch --detach origin/main`.
  - It must contain this record's merge.
  - Run P-0.
  - Choose a `WORK_DIR` outside the checkout, for example under the system temporary directory.
- **O-2. Open the variable list.**
  - Open the variables of the Railway service `glow-hdengine-v2`, project `ample-illumination`, in the environment that serves the base URL.
  - Do not reveal, copy or type any value.
  - Canon gives no procedure for this view (PF07 gap). The requirement is only that the observer sees the variable names for that service and environment.
- **O-3. Run the script once**, from the checkout root:
  - Product Owner: `EXECUTOR=PO WORK_DIR=<absolute path> ATTEMPT=1 bash docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh`
  - Delegated agent: `EXECUTOR=PO-delegated-agent DELEGATION_REF='<this session's URL>' WORK_DIR=<absolute path> ATTEMPT=1 bash docs/ephemeral/HDE-CRD-0002-WU-OPS-01-run-v1.0.sh`
  - The script runs in this order:
    1. preflight;
    2. the seven presence prompts. Answer each with `SET` if a variable of exactly that name is listed, `UNSET` if it is not, or `NOT_OBSERVED` if the list cannot be seen. An invalid answer is not recorded and is asked again, up to three times, then recorded as `NOT_OBSERVED`;
    3. up to three reads: the first at once, the second 300 s later, the third 600 s after that. The reads stop at the first match. This schedule is the task author's bound for "after the service has had time to deploy" (P-9); it is not a PF07 fact;
    4. classification;
    5. the secret scan;
    6. the checksum ledger.
- **O-4. Act on the exit status** (§7.2). Exit 0 continues to O-5. Every other status stops the operations, except as §7.2 and §9 state.
- **O-5. Verify the outputs.**
  - Run `cd "$WORK_DIR" && sha256sum -c SHA256SUMS.attempt<N>`; every line must print `OK`.
  - Exit 4 leaves nothing to verify.
- **O-6. Publish the evidence** (§8.3), for every attempt except one that exited 4.
- **O-7. Return.** Write the OPS-20 result (§8.2) and hand it to OPS-30.

## 7. Success criteria, outcome map and run rules

### 7.1 Success criteria (from Plan delta 01 P-9)

| ID | Criterion | Evidence |
| :- | :- | :- |
| SC-1 | `GET /internal/version` on the base URL reports the candidate's `release_id`, `77204764…c51e`. The candidate's release is version `1.3.0`: its `catalog/manifest.json` hashes to that value | A read of class `MATCH` in `identity_reads.attempt<N>.tsv`, and `pinned_equal yes` in `expected_identity.attempt<N>.txt` |
| SC-2 | The presence-only binding probe is recorded: each of the seven names `SET` or `UNSET`, none `NOT_OBSERVED`. The environment disposition is `validated` when all seven are `SET`; otherwise it is "not yet closed", with the `UNSET` names as the reason (HDE Governance §9.1, "Ops tasks", item 4) | `binding_presence.attempt<N>.tsv`; `result.attempt<N>.txt` line `binding_presence` |
| SC-3 | Every output is stored under `audit/ops/hde-crd-0002/wu-ops-01/`, byte for byte, through a pull request the Product Owner merges. Each attempt's ledger verifies. The executor writes no path proof and no Index or Mirror row; path-proof coverage follows CR-9's interim treatment | The merged files; `sha256sum -c` on each ledger; OPS-30's check |
| SC-4 | No production configuration change was made. If the rollback condition arose, the redeploy is recorded (§9) | The OPS-20 result's before and after statement |

The task's PASS is SC-1 to SC-4 met on an attempt that exits 0. The business-case measure is the same test.

### 7.2 Outcome classification map and stop conditions

| Exit | Class | Condition | Next action |
| :- | :- | :- | :- |
| 0 | `PASS` | A read matched, and all seven variables are `SET` | O-5 to O-7 |
| 2 | `FAIL_BEHAVIOR` | The service answered without the candidate's `release_id` on every read: another `release_id` (`OTHER_RELEASE`), or any other answer (`NO_IDENTITY`), such as 401, 403, 404, 500 or a body without an identity | **Stop.** No redeploy and no configuration change. Publish the outputs (O-5, O-6); the Product Owner decides the next step |
| 5 | `FAIL_BEHAVIOR` | The service did not answer any read: no HTTP response (`NO_RESPONSE`), or a gateway 502, 503 or 504 reporting that the application did not answer (`GATEWAY_NO_ANSWER`). The task author defines this as P-9's "the service did not answer at all" | **Stop.** The rollback condition is met (§9). Publish the outputs |
| 6 | `FAIL_BEHAVIOR` | A read matched, but at least one variable is `UNSET`. The environment is not yet closed | **Stop.** Publish the outputs; the Product Owner decides before the QA Plan relies on the bindings |
| 3 | `TOOLING_BLOCKED` | A preflight row failed, or a variable's presence was `NOT_OBSERVED` | Fix the stated cause (for example, a clean checkout or Railway access), then run again with the next `ATTEMPT`. Publish the blocked attempt's outputs too |
| 4 | `FAIL_TOOLING` | A step failed unexpectedly, or the secret scan found a credential pattern; on a scan hit the script deletes all of its output | Copy nothing into the repository. One run again with the next `ATTEMPT` is allowed if the failure came before any read. Otherwise return to the creator IA |

### 7.3 Run rules

- **The script and its inputs:**
  - The script is not edited, and is used only with the parameters in §4.
  - The request carries no credential header and no identity-override header (`/internal/version` refuses an override), and goes to no other endpoint.
- **Results are not altered:**
  - No forced PASS.
  - No edit, reorder, rename or deletion of an output file.
  - A failed attempt is kept, never replaced.
- **When the script runs again.** Only in these cases, each with the next `ATTEMPT` number:
  - after a fixed `TOOLING_BLOCKED` cause;
  - after an early exit 4;
  - once after a rollback (§9);
  - as the Product Owner directs in writing in the OPS-20 session.
- **Out of scope:**
  - no Railway setting or variable change;
  - no deploy;
  - no vendor call;
  - no database access;
  - no hand-written path proof, Index, Mirror or checksum sidecar;
  - no merge by the executor.
- **A delegated agent:**
  - follows the same rules (HDE Governance §9.1, "Ops tasks", item 1);
  - stops at an objective blocker and names the smallest Product Owner input needed;
  - performs no rollback.

## 8. Evidence

### 8.1 Temporary outputs and controlled evidence

- **Temporary (`TRANSIENT_SCRATCH`):** `WORK_DIR`, outside the repository.
  - The script writes only there, apart from one response-body file in the system temporary directory. It empties that file after each read and deletes it after the last.
  - Nothing is written in the checkout while the script runs.
- **Controlled (`REPOSITORY_CONTROLLED`):** `audit/ops/hde-crd-0002/wu-ops-01/` and the OPS-20 result record.
  - Both are added through one pull request per publication, which the Product Owner merges.
  - The path class `audit/ops/` selects only the CI `evidence` lane.

### 8.2 Required outputs and content

Each attempt `N` produces these files. They are copied byte for byte into `audit/ops/hde-crd-0002/wu-ops-01/`.

| File | Content |
| :- | :- |
| `identity_reads.attempt<N>.tsv` | A header line, then one row per read: read number, UTC time, HTTP status, `curl` exit code, class, `release_id` reported (or `-`), the body's top-level key names in order, and the body's SHA-256 and size. No body and no header value |
| `binding_presence.attempt<N>.tsv` | A header line, then the seven names, each `SET`, `UNSET` or `NOT_OBSERVED`, with the UTC time of the answer |
| `expected_identity.attempt<N>.txt` | Candidate `HEAD` SHA, the included commit `f508dcf`, the manifest's SHA-256, version, `built_at_utc` and member count, the pinned `release_id`, and `pinned_equal yes` |
| `result.attempt<N>.txt` | Mode, attempt, classification, exit status, reason, read and presence states, base URL, endpoint, executor, delegation reference, candidate head, script SHA-256, start and finish times, nonclaims |
| `run.attempt<N>.log` | The script's log, including any `curl` error message. No value, body or typed answer other than the three accepted words |
| `SHA256SUMS.attempt<N>` | The checksum ledger over the five files above, written last |

**The OPS-20 result record**, `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-execution-result-v1.0.md`, is written by OPS-20. It records:

- the executor;
- the delegation reference or the personal-execution statement;
- the environment (shell kind, `curl` and Python versions);
- every attempt, with its exit status and class;
- P-0's output;
- the before and after state: no configuration change, or the rollback facts of §9;
- the evidence paths;
- the pull request;
- residual state;
- the nonclaims;
- the truthful `COMPLETE`, `PARTIAL` or `BLOCKED` state.

### 8.3 Publication steps

1. From a clean checkout of current `main`, create a new branch. Then run `mkdir -p audit/ops/hde-crd-0002/wu-ops-01`, and `cp "$WORK_DIR"/*.attempt<N>.* "$WORK_DIR"/SHA256SUMS.attempt<N> audit/ops/hde-crd-0002/wu-ops-01/`.
2. Run `(cd audit/ops/hde-crd-0002/wu-ops-01 && sha256sum -c SHA256SUMS.attempt<N>)`. Every line must print `OK`.
3. Write the OPS-20 result record.
4. Commit only those paths.
5. Read-only check, if the checkout has the repository's CI install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`):
   - `python tools/ci/prepush_check.py lanes` under closed rails (default refs `origin/main` and `HEAD`). It is expected to report `lanes=evidence` and `PASS`.
   - Without that install, record the check as `NOT RUN` with the reason. The hosted `evidence` lane on the pull request is the check of record.
6. Push and open a pull request. Do not merge it.

An attempt that stopped at a parameter check before creating its log (`ATTEMPT`, `WORK_DIR` or the rehearsal variables) has no files to publish; the OPS-20 result records it.

**Path proofs (CR-9).**
- No path proof, Index row, Mirror row or checksum sidecar is written by the executor or by hand. Path proofs are the canonical updater's alone (HDE Schemas and Artifacts §8.3, "Join to the human index"; the same rule in the §8.6.3 family entries).
- The canonical updater has no registration for this root. It indexes Ops roots only where its source names them, and names none for HDE-CRD-0002 (§12).
- When QA consumes this evidence, the QA check's governed `primary.log` and its sibling path proof point to these files without re-homing them (Glow QA Guide §11.1). The updater publishes that QA family for HDE-CRD-0002.

## 9. Recovery and escalation

- **Rollback (exit 5 only).**
  - **Condition:** the service did not answer any read. This is Plan delta 01 P-9's "the service did not answer at all".
  - **Action:** the Product Owner redeploys the previously deployed commit under the rollback intent, using Railway's own deployment controls for `glow-hdengine-v2`.
  - **Procedure gap:** the exact Railway procedure is not in Glow Infrastructure or any other canon (PF07 gap). So a delegated agent does not perform it: it would have to invent the procedure.
  - **The Product Owner records, in the OPS-20 result:**
    - the time;
    - the deployment and commit identity Railway shows for the redeployed deployment;
    - who performed it.
  - **Then:** the script runs once more with the next `ATTEMPT`, to record the state after the rollback, and the Product Owner decides any next step.
  - **Not authorized:** no other redeploy, setting change or restart.
- **Recovery of a run.**
  - Delete `WORK_DIR`.
  - The task changes nothing in production unless the rollback runs.
  - An unmerged evidence pull request can be closed; a merged one stays as history, and a later attempt adds files.
- **Escalation:**
  - a changed target, release or classification, or a defect in this record or its script: to the creator IA (OPS-10, a successor version);
  - a failed identity, an `UNSET` variable, or the rollback decision: to the Product Owner;
  - a material scope change: to the Product Owner, then the Plan's author and reviewer (IA-40 and IA-30).

## 10. Rehearsal record

Rehearsal is not production execution and created no evidence. It ran in this IA session's scratch area, outside the repository, on 2026-10-22, against these exact script bytes (`960eabe5…ad0d9`), from a clean throwaway clone at `main` `8e6f238`. The production service was not contacted.

- **Targets:**
  - the production app factory, `adapter.factory:create_app()` under gunicorn 21.2.0, on `127.0.0.1:18080`, with `APP_ENV=prod SAFE_MODE=1 ALLOW_NETWORK=0` and no secret. Its `/internal/version` reported `release_id` `77204764…c51e`, a 347-byte body with SHA-256 `c9302e7072138482c1363f66c58606b45faac476a07235772d06ca581bc0f06a`, and the six keys in HDE Governance §10.5's order;
  - stub servers answering with another `release_id`, a 502, or a 404;
  - a closed port.

| Case | Expected exit | Result |
| :- | :- | :- |
| r01 match, PO | 0 | 0; ledger verifies |
| r02 match, delegated | 0 | 0; ledger verifies |
| r03 no response (closed port) | 5 | 5 (three `NO_RESPONSE`) |
| r04 gateway 502 | 5 | 5 (three `GATEWAY_NO_ANSWER`) |
| r05 other `release_id` | 2 | 2 (three `OTHER_RELEASE`) |
| r06 404 | 2 | 2 (three `NO_IDENTITY`) |
| r07 one `UNSET` | 6 | 6 |
| r08 one `NOT_OBSERVED` | 3 | 3 |
| r09 invalid answers, one of them a typed value | 3 | 3. The typed value appears in no output file |
| r10 credential pattern in `DELEGATION_REF` | 4 | 4. `SECRET_SCAN_HIT`; every output deleted |
| p01 to p08 preflight: `WORK_DIR` in the repository, `WORK_DIR` not empty, bad `EXECUTOR`, missing `DELEGATION_REF`, non-loopback rehearsal URL, a rehearsal delay in execution mode, `ATTEMPT=0`, a dirty tree | 3 each | 3 each, with the matching `PREFLIGHT_FAIL` |
| p09 an old checkout without `f508dcf` (`892feeb`) | 3 | 3, `PREFLIGHT_FAIL: HEAD … does not contain f508dcf` |

- The checkout was clean after every case.
- **Publication path:** two commits under `audit/ops/hde-crd-0002/wu-ops-01/` were each run through `tools/ci/prepush_check.py` (`lanes` and `replay`) in a throwaway clone, under closed rails, with CPython 3.12.3 and CI's full install. One commit held stand-in files; the other held r01's actual output.
  - Both classified to `evidence` only.
  - The stand-in commit's replay ran the evidence lane: 134 passed in 671.86 s, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, `PASS`. The second replay's result is in §16.
  - These pre-push results are not CI's result.
- **Limitations:**
  - The HTTPS path was not exercised end to end; production may not be contacted from this session. `curl --proto =https` was confirmed to refuse a plain-HTTP URL (curl 8.5.0, exit 1).
  - The 300 s and 600 s delays were exercised as 1 s each; the loop is the same code.
  - The Railway variable list was not observed.
  - A delegated agent with real Railway access was not rehearsed.

## 11. `/internal/version` posture

- **Governing source:** HDE Governance §10.5. The route is ops-only, identity-only and not A7. Its interim posture has no application-layer auth and is "operator-network-only".
  - Runbooks must not require an auth header, and the script sends none.
  - A 401 or 403 is recorded as status only, as Observed Evidence. It is `NO_IDENTITY`: exit 2, and the Product Owner decides.
- **Earlier reads (Observed Evidence, non-PF):** `audit/preflight/intver_headers.txt` (2025-11-02) and `audit/qa/hde-epic022/remediation/s1_host_matrix/host_matrix.md` record HTTP 200 from this base URL with no auth header.
- **What this task does not claim:**
  - It produces no INTVER family artifact (HDE Schemas and Artifacts §8.6.3, "Internal-ops surface — `/internal/version` identity artifacts") and claims no `/internal/version` token.
  - The recorded key names are an observation, not a header or body-invariant proof.
  - The read proves the release running on the target. It does not prove reachability from another environment, or any behaviour (Glow QA Guide §3.5.2: an identity anchor, "not a substitute for real behavior tests").
- **`build_commit`:** it is the fixed source value `9479d28` (`engine/runtime/identity.py`, `_STATIC_IDENTITY`). It does not identify the running commit, so deployment is judged by `release_id` alone (Plan delta 01 P-9).

## 12. Repository facts measured for this task (at `8e6f238`)

- **`catalog/manifest.json`:**
  - version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`, 45 members;
  - SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`.
- **When that `release_id` appeared:** first at `822ce15` (#656, WU-PR-05, 2026-10-18). The commit before it, `5892538`, had `2f18a5eb…`. It is unchanged on every later `main` commit.
- **Served code since `822ce15`:**
  - Outside `docs/`, `tests/`, `audit/` and `artifacts/`, the files changed are `.env.example`, `.github/workflows/epic-closeout-validation.yml`, `AGENTS.md`, `CHANGELOG.md`, `README.md`, `ci/checks/classify_ci_changes.py`, `pytest.ini`, `schemas/close_candidate_source.v2.json`, `tools/ci/prepush_check.py`, `tools/evidence/update_evidence_index.py`, `tools/qa/generate_epic_close_pack.py` and `tools/qa/qa_harness.py`.
  - No file under `adapter/`, `engine/` or `catalog/` changed, and neither did `requirements*.txt`, `pyproject.toml` or `Procfile`.
  - So a service reporting `77204764…` from a deploy of `main` serves the candidate's application code. S02 (#643), S10 (#643, #646) and S14 (#651) precede `822ce15`.
  - This rests on the Product Owner's deploy-source fact (P-18).
- **The identity body:** `/internal/version` returns `identity_admin()`, six fields, through `emit_public` (`adapter/http_reader.py` lines 1164 to 1196). There is no `version` field, so version `1.3.0` is established through the manifest (SC-1). The handler refuses `X-Identity-Override` with 400.
- **The canonical updater:**
  - `tools/evidence/update_evidence_index.py` names Ops evidence paths only for HDE-EPIC028, 032, 034, 035, 037 and 038.
  - It has no directory discovery under `audit/ops/`.
  - Its CRD admission (`ADMITTED_CRD_QA`) covers only `audit/qa/hde-crd-0001` and `audit/qa/hde-crd-0002`.
- **CI classification:** `audit/ops/` is in the classifier's `_HISTORICAL_PREFIXES`, which selects the `evidence` lane (`ci/checks/classify_ci_changes.py`).

## 13. Canon-conflict register

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | WU-PR-01 rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | addendum 2.7 |
| CR-9 | PROPOSED | Isis (not yet reviewed) | this record, below |

### CR-9 — Path proofs under the WU-OPS-01 Ops root

**Classification and sources**

- **Classification:** CANON_RECONCILIATION. An in-flight Plan text conflicts with canon.
- **Conflicting sources:**
  - **The Plan:** Plan delta 01 v1.1 P-9, Success criteria: "all captured under `audit/ops/hde-crd-0002/wu-ops-01/` with path proofs (Plan Templates §3 evidence posture; lower-case directory names)". It is recorded in HDE Build Notes addendum 2.19 and repeated in the business-case measure (#702).
  - **HDE Schemas and Artifacts v2.9.6 §8.3, "Join to the human index (parity, proofs, same-PR rule)":** a path proof belongs to an Evidence Index entry; the single-writer remediation runs `tools/evidence/update_evidence_index.py` to regenerate "all governed \*.path\_proof.txt transcripts"; "Do not hand-edit proofs". The §8.6.3 family entries repeat the rule ("Feature producers MUST NOT write Index, Mirror, path-proof … companions") and require a path proof when an artifact is "promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence".
  - **Plan Templates v2.0.5 §3, "Evidence posture":** path proofs "for any governed artifact path included in acceptance or close-pack".
  - **Glow QA Guide v3.0.6 §11.1, after the roles table:** "Ops evidence remains distinct under `audit/ops/<change-id>/<task_id>/`. When QA consumes it, the QA check's governed … `primary.log` and required sibling path proof point to that evidence rather than re-homing it."
- **Evidence:** §12. The updater has no registration for this root and no directory discovery, so no canonical writer can produce a path proof there today.

**The conflict and its effect**

- **Conflict:** read literally, the Plan requires path proofs at capture time under a root no canonical writer covers. Canon forbids anyone else from writing them, and places the path proof for consumed Ops evidence on the consuming QA check.
- **Affected:** WU-OPS-01's success criterion (SC-3); the business-case measure; no Specification requirement.

**Alternatives**

- **(a) Canon route.** The Ops evidence carries a SHA-256 ledger. Its path-proof coverage comes from the QA check that consumes it, published by the updater's existing HDE-CRD-0002 QA admission. No new unit and no code change.
- **(b) Registration unit.** A PR unit registers `audit/ops/hde-crd-0002/wu-ops-01/` in the updater, so it indexes these files and writes their sibling path proofs. This is new code, owner tests and a full PR cycle.
- **(c) No promotion at all.** Like HDE-EPIC040 OPS01, leave the evidence unpromoted with a nonclaim. QA would still have to consume it, as in (a).

**Proposed disposition, interim treatment and remaining risk**

- **Proposed disposition:** (a). The Plan text can be aligned by a one-item bounded delta when the Plan's author and reviewer next meet (IA-40, then IA-30).
- **Interim treatment:** canon governs (AGENTS.md "Canon-first rule"; the sources above).
  - OPS-20 writes no path proof, Index row or Mirror row.
  - SC-3 is judged as §7.1 states it.
  - Execution is not blocked.
- **Unresolved risk:** if Isis rejects (a) and the Product Owner chooses (b), the captured bytes stay valid. The updater would add their path proofs later, with no re-execution.
- **Drainage target and owner:** none in permanent canon, which is consistent. The Plan text and the measure wording belong to the Plan's author (this IA) and reviewer (Isis), and to the Product Owner for the measure.

**Review fields:** reviewer, session, reviewed artifact, decision time and rationale are not yet reviewed.

**Note:** this IA drafted the business-case measure with the Plan's wording without checking the writer's coverage. The conflict was found while authoring this task.

## 14. Build Checklist tracking (Plan Templates §3)

| Field | Value |
| :- | :- |
| Work item ID | HDE-CRD-0002 WU-OPS-01 |
| PF09 disposition | Out of HDE phased-build scope. The Specification records "No PF09 mapping of this work (Plan Templates §2A)" |
| Phased PF09 document | N/A (non-mapping posture) |
| Task ID | N/A (non-mapping posture) |
| Subtask ID | N/A (non-mapping posture) |
| Exact source heading | Specification v1.1, the exclusion "No PF09 mapping of this work" |
| Contribution | documents (the deployed-candidate identity for QA) |
| Status nonclaim | This artifact does not itself move PF09 or PF30 status |

## 15. Recipient-completeness check

- **What the executor needs, and all of it is named here:**
  - this record;
  - its script, with its hash;
  - a clean checkout of `main`;
  - HTTPS egress to the base URL;
  - sight of the Railway variable list;
  - the Product Owner's OPS-20 invocation.
- **Nothing is left to invent:**
  - The only operator inputs are the four parameters, which the script validates, and the seven one-word answers.
  - No command, endpoint, credential or value has to be supplied or guessed.
- **Isolated gaps:**
  - The Railway rollback procedure affects the exit-5 path only. The Product Owner performs that path.
  - The variable view's navigation affects SC-2 only. A failure there is `NOT_OBSERVED`, which is `TOOLING_BLOCKED`, not a guess.
- **Access:** no production credential is needed for the read. No unrelated credential is required.

## 16. Validation of this record

- **Read back after push:** the record and the script, by their blobs on the branch (pull request below).
- **Second publication replay** (r01's actual output committed under the root): see the line below, filled before push.

REPLAY-2: running when this record was first committed; its result is added by a follow-up commit on this branch before the pull request opens.

## 17. Next stage and return

- **Next:** OPS-20 — Execute Bounded Ops Task — 100926.1 (AI Prompts / HDE IA), run by the Product Owner or a delegate the Product Owner names, after this record's pull request merges.
- **Then:** OPS-30 — Review Ops Execution Receipt — 100926.1, run by the creator IA. It compares SC-1 to SC-4 with the evidence and returns `ACCEPT` or `REJECT`.
- **QA-10:** Plan v1.1 §9 item 1 lets QA-10 begin once WU-OPS-01 is "planned (OPS-10) or executed". That holds when this record merges, with WU-PR-08 and WU-DOC-01 accepted and AQ-1 decided (addendum 2.15). QA-10's own readiness intake decides; this record routes only to OPS-20. The QA Plan's live steps still follow WU-OPS-01's execution (Plan v1.1 §7, "before the QA Plan's live steps").
- **Not decided here:** CR-9's disposition (Isis), any rollback (Product Owner), QA, acceptance or closure.

## 18. TypeSafe reading for the receiving session (OPS-20, WU-OPS-01)

Action sent (v8.2): "Execute, as the Product Owner or an agent the Product Owner delegates, one new operations task record for an approved change, not yet executed: run its rehearsed 250-line shell script once from a clean checkout to read the production service's identity endpoint over HTTPS (one endpoint, up to three reads over about fifteen minutes), compare the reported release identity with the candidate's, and enter the operator's presence-only observation of seven named service variables from the hosting dashboard; then copy the six secret-free output files unchanged into a fixed audit directory, write a short execution result record, commit both and open a pull request for the Product Owner to merge. The task record fixes every command, expected output, stop condition and recovery step; no code is written, nothing in production changes unless the service does not answer at all, and the task author's receipt review follows."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 1.80 (confidence 0.29). Rung probabilities: low 0.13, medium 0.34, high 0.25, extra high 0.15, max 0.13, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.11, Opus 5.5 0.81, Sonnet 5.5 0.04, Haiku 5.5 0.04 (confidence 0.75).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.014, Fable 5.1 at medium 0.037, Fable 5.1 at high 0.028, Fable 5.1 at extra high 0.017, Fable 5.1 at max 0.014, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.105, Opus 5.5 at medium 0.275, Opus 5.5 at high 0.203, Opus 5.5 at extra high 0.121, Opus 5.5 at max 0.105, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.005, Sonnet 5.5 at medium 0.014, Sonnet 5.5 at high 0.010, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.005, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.005, Haiku 5.5 at medium 0.014, Haiku 5.5 at high 0.010, Haiku 5.5 at extra high 0.006, Haiku 5.5 at max 0.005, Haiku 5.5 at ultracode 0.000.
  - Flags: boundary between high and medium.
  - Sent 2026-10-22T05:09:53Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T05:09:53Z; HTTP 200 in 0.62 s; 5513 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `operations`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for OPS-20 is not stated.

**Surface advice:** run OPS-20 where all of the following hold:

- **Shell:** a shell with HTTPS egress to `glow-hdengine-v2-production.up.railway.app`, bash, `curl`, `python3` and `git`, and a clean checkout of `amthorn78/glow-hdengine-v2` `main`. GitHub Codespaces for the repository is the QA console Glow Infrastructure §2.6 names; the Product Owner's own terminal also qualifies.
- **Railway:** the Railway variable list of `glow-hdengine-v2` must be visible to whoever answers the seven prompts. A delegated agent without Railway access needs the Product Owner to answer them.
- **Pull request:** the session must be able to push a branch and open a pull request on `amthorn78/glow-hdengine-v2`.
- **Not needed:** no production credential, vendor key or database access.
- **Order:** this record's pull request is merged first.

## 19. Prompt-use provenance

`GCFPE_PROMPT_USES`:

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-OPS-10-20261022-WU-OPS-01-01` |
| Change identity | CRD HDE-CRD-0002 |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| Work unit | WU-OPS-01 |
| Ecosystem release | GCFPE-20261009.1 / 100926.1 |
| Prompt | OPS-10 — Create Bounded Ops Task — 100926.1, page state of 2026-10-12T02:29:29.013Z |
| Role and stage | whole-change IA, task author |
| Capture time | 2026-10-22T05:15:00Z |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |

- **Repository persistence: PENDING / NON_GATING.** `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`, so the usage stays in this record's metadata.
- **Owner:** the authorized repository writer, when the procedure is installed.

## 20. Canon relied on

Read on `main` at `8e6f238`; PF10 is v13.7.4.

| Topic | Sources and sections |
| :- | :- |
| Ops Task Record fields; controlled execution contract; evidence posture; Build Checklist tracking; no governance drift | PF27-Canon-Plan-Templates v2.0.5 §3, read in full; §0 "Exact technical facts and secret safety" and "Repository loci and file minting"; §1 "Step-0C — Prod handshake"; §4 "/internal/version conditional proof binding" |
| Infrastructure facts and gaps | PF07-Canon-Glow-Infrastructure v2.3.3 §2.2, §2.3.3, §2.4, §2.6, §3.1, §3.3, §4.1, §8.1 (opening entries), §10, read in full |
| Ops task authority, delegation, evidence and environment validation | PF04-Canon-HDE-Governance v2.8.7 §9.1 "Ops tasks" items 1 to 5 |
| `/internal/version` posture, payload and tokens | PF04-Canon-HDE-Governance v2.8.7 §10.5 (intent, interim auth posture, methods, headers, payload, acceptance checklist) and §2.0.2 (token names, not claimed); PF02-Canon-HDE-Architecture v2.4.6 (non-A7, ops-only, identity-only); PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 (ops endpoint, excluded from A7) |
| Path-proof writer and INTVER families | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.3 "Join to the human index (parity, proofs, same-PR rule)", including its single-writer remediation; §8.6.3 family entries (the promotion rule; the companion-ownership rule; "Internal-ops surface — `/internal/version` identity artifacts (`INTVER_*`)"; the Ops evidence entries of earlier epics) |
| Ops evidence consumed by QA; identity anchor | PF19-Canon-Glow-QA-Guide v3.0.6 §11.1 "QA roles", the roles table and the paragraph after it; §3.5.2 "Step 0 — prod handshake (identity-only, not behavior)" |
| Business case, real inputs, no ceiling; WU-OPS-01 delta | PF10 — HDE Build Notes v13.7.4 addenda 2.11 (as narrowed), 2.18 and 2.19, read in full; 2.20 by its title and effects |
| WU-OPS-01 scope | Implementation Plan v1.1 §3, §4, §7 WU-OPS-01 and §9; Plan delta 01 v1.1 P-9, P-17 to P-20; the business-case disposition §2 |
| Precedent | `docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.3.md` and `docs/ephemeral/HDE-EPIC040-OPS01-RCA-v1.0.md` (CA-1: rehearse before READY; CA-2: the controlled execution contract; CA-3: state the environment exactly; CA-4: the Product Owner writes no delegation text) |
| Stage rules | OPS-10 — Create Bounded Ops Task — 100926.1, read in full |
