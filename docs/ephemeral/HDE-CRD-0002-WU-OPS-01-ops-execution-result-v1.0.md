---
artifact_type: OPS_EXECUTION_RESULT
artifact_id: HDE-CRD-0002-WU-OPS-01-OPS-EXECUTION-RESULT
artifact_version: "1.0"
result_state: COMPLETE (attempt 1 PASS, exit 0; evidence published as an open pull request). SC-3 and task completion wait on the Product Owner's merge and OPS-30's acceptance
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
OPS_UNIT_ID: WU-OPS-01
OPS_TASK_ID: HDE-CRD-0002-WU-OPS-01-OPS-TASK v1.0 (docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: OPS-20 — Execute Bounded Ops Task — 100926.1 (https://app.notion.com/p/3f44590a05eb8155aebacd56f469643e; page state of 2026-10-12T02:29:42.649Z as read)
prompt_release: GCFPE-20261009.1 / 100926.1
executor: PO-delegated-agent (Claude Code, Sonnet 5.5, VS Code extension, local session)
delegation_ref: "claude-code-vscode-session 4b626dac-628b-40e4-9f68-31528cc344bc (no URL exists for a local session)"
creator_ia_and_acceptance_owner: the continuing whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
receipt_destination: OPS-30 — Review Ops Execution Receipt — 100926.1; receipt file docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md
return_owner: the creator IA above; Product Owner for the merge
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_OPS-20
created_at: 2026-10-23T13:34:00Z
---

# HDE-CRD-0002 WU-OPS-01 — Ops Execution Result v1.0

## 1. Result

- **Attempt 1 exited 0, class `PASS`.**
  - Read 1 of `GET /internal/version` on `https://glow-hdengine-v2-production.up.railway.app` returned HTTP 200 and reported `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, the candidate's.
  - All seven named variables were recorded `SET`.
  - The script stopped at the first match, so the 300 s and 600 s reads did not run.
- **No production configuration change was made.** The rollback condition (exit 5) did not arise.
- **Evidence:** six unedited files under `audit/ops/hde-crd-0002/wu-ops-01/` (§7), in the pull request named in §10. They are not on `main` until the Product Owner merges it.
- **Six deviations from the task's expected path are recorded for OPS-30** (§8). None changes the script, its bytes or its output. D-2 and D-3 limit how far SC-2 reaches.
- This result is an executor's report. It is not creator acceptance, QA, deployment approval or closure.

## 2. Binding and identity

| Item | Value |
| :- | :- |
| CHANGE_CLASS / CHANGE_ID / OPS_UNIT_ID | CRD / HDE-CRD-0002 / WU-OPS-01 |
| OPS_TASK_ID | HDE-CRD-0002-WU-OPS-01-OPS-TASK v1.0 |
| Target classification | Hosted-service operation (read-only here: no redeploy, no vendor call, no database access) |
| Target | Railway project `ample-illumination`, service `glow-hdengine-v2`, base URL above (PF07-derived; Glow Infrastructure v2.3.3) |
| Named operator | `PO-delegated-agent`, acting on the Product Owner's direct instruction (the OPS-20 handoff pasted into this session) and three in-session Product Owner directions (§3) |
| Session | Local Claude Code VS Code session `4b626dac-628b-40e4-9f68-31528cc344bc`. No session URL exists (D-1) |
| Tested state | Candidate: `main` HEAD `45f045ba4164c4e13fa5e807b10a4dc803c362e6` (#703), which contains `f508dcf` (#700). Its `catalog/manifest.json` is `1.3.0`, built `2026-08-24T18:04:49Z`, 45 members, sha256 = the pinned `release_id` |
| Evidence-storage commit | `8d7424c5` on branch `docs/20261023-hde-crd-0002-wu-ops-01-execution`. It is later than, and distinct from, the tested state. The run did not test it |
| Repeat-invocation check | In the `main` checkout, no WU-OPS-01 result or receipt exists in `docs/ephemeral/` and no `audit/ops/hde-crd-0002/` path exists. The only remote branch with a WU-OPS-01 name is #703's, which carries the task. This is attempt 1 and the first task version |

## 3. Authority, dependencies and lineage

- **Authority:** the Product Owner's OPS-20 invocation of this task (task record §2). It covers the HTTPS read, the variable-presence observation and the evidence pull request.
- **In-session Product Owner directions** (this session, the Product Owner's answers to my questions; no secret content):
  1. Observe variable presence with the Railway CLI ("Try to use the railway CLI").
  2. Publish both the `audit/ops` evidence and this result in one pull request ("Yes, publish both").
  3. Use the local session ID as `DELEGATION_REF` ("Use the local session ID").
- **The Product Owner also approved the Railway CLI sign-in** (a device-code approval, second flow, §5).
- **Dependencies:** WU-PR-08 accepted (PR-40 ACCEPT, #688); WU-DOC-01 COMPLETE (DOC-20 v1.1, #702); business case adopted (#702); task record and script merged (#703). All met.
- **Plan lineage:** Specification v1.1 with delta 01; Implementation Audit v1.0; Implementation Plan v1.1 §7 WU-OPS-01 with Plan delta 01 v1.1 (P-9, P-18, P-19, P-20); Plan review v1.1 INITIAL_APPROVE and delta review DELTA_APPROVE; PF10 addenda 2.18, 2.19, 2.20. No rescope or remediation re-entry.
- **Product Owner execution authority is bounded by** PF27 §3 (Execution authority) and PF04 §9.1 (Ops tasks, item 1). The delegate is executor and evidence producer, not approver.

## 4. Environment

| Item | Value |
| :- | :- |
| Shell | GNU bash 5.2.21 on Linux 6.8.0-147-generic; `curl` 8.5.0; Python 3.12.3 (`python3`; `python` is not on `PATH`); `git`, `sha256sum` present |
| Script run | Unedited, from the checkout root on `main` at `45f045ba`, clean tree, `WORK_DIR` outside the checkout |
| Egress | HTTPS to the base URL worked (a TCP connect check to port 443 before the run; no HTTP request outside the script) |
| Railway CLI | `@railway/cli` 5.70.0, installed with `npm` into an empty scratch directory outside the repository, from the official npm package (repository `railwayapp/cli`). It is not installed globally |

## 5. Ordered actions

| Step | Action | Outcome |
| :- | :- | :- |
| O-1 | Clean checkout of current `main` containing #703; P-0 | `origin/main` = HEAD = `45f045ba`, clean. P-0: `sha256sum` of the script printed `960eabe59b6cc4abda69cf90320fb91abd3f10520830e2fb2fd346f2df7ad0d9`, matching the pin. Re-checked immediately before the run: match |
| (ahead of O-2) | Egress and tool check | `bash`, `curl`, `python3`, `git`, `sha256sum` present; DNS resolved and TCP 443 connected. No HTTP read made outside the script |
| O-2 | Open the variable list (§6) | Done through the Railway CLI, after a CLI sign-in. Confirmed: confirmed complete |
| O-3 | Run the script once, `EXECUTOR=PO-delegated-agent`, `ATTEMPT=1` | Exit 0. Started and finished `2026-10-23T13:30:06Z` |
| O-4 | Act on the exit status | Exit 0: continue |
| O-5 | Verify outputs | `sha256sum -c SHA256SUMS.attempt1` in the work directory and again in the repository path: five of five `OK` |
| O-6 | Publish the evidence (task §8.3) | Steps 1 to 4 done: new branch from `origin/main`, byte-for-byte copy (`cmp` identical), ledger check `OK`, result written. Step 5, the read-only check: §10. Step 6, pull request opened; not merged by me |
| O-7 | Return | This record, read back after saving (§10) |

**Railway CLI sign-in (an extra step the task record does not name; Product Owner directed, direction 1):**

- The CLI reported its saved login from 19 October invalid. A first device-code flow was never approved, and I stopped it. A second flow was approved by the Product Owner.
- Only read-only CLI commands ran: `--version`, `whoami`, `list --json`, and `variable list --json`. No `link`, `up`, `redeploy`, `variable set`, `variable delete` or `variable edit` was run.

## 6. Binding-presence observation (SC-2)

- **Command:** `railway variable list --project <ample-illumination project ID> --service glow-hdengine-v2 --environment production --json`.
  - The project ID was resolved from `railway list --json`. No `railway link` was used, so the CLI's local project link is unchanged.
  - The CLI's `--json` output includes raw values (the CLI help says so). The output was piped straight into a small filter script held in the session's scratch directory. The filter read the names, printed `SET` or `UNSET` for the seven task names plus a total count, and discarded the rest. Standard error went to a scratch file, which was empty.
  - No variable value was displayed, written to a file, copied, typed or persisted anywhere.
- **Result:** all seven names (`APP_ENV`, `SAFE_MODE`, `ALLOW_NETWORK`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`) `SET`. The listing held 22 variables in total (a count only). Observed between `13:29:32Z` and `13:30:06Z`; the session did not timestamp the listing separately.
- **The agent typed the answers.** I typed `SET` seven times at the script's prompts, from the CLI observation above. The Product Owner typed none (D-2).

## 7. Evidence and checks

Files, all under `audit/ops/hde-crd-0002/wu-ops-01/`. The pull request adds them unedited. The ledger `SHA256SUMS.attempt1` was written last by the script.

| File | sha256 |
| :- | :- |
| `binding_presence.attempt1.tsv` | `a7789c68b0dadf426337e5f5022c6772597f2f747228bdcf246d762b003ef133` |
| `expected_identity.attempt1.txt` | `1f60bf93121c8fe7f2f72747fcfbb926199825fc60fdeca650dd06e6928c4c52` |
| `identity_reads.attempt1.tsv` | `2e8706fdf578faed07d26772e788539fcc94efb5493043e97fd321991be34acc` |
| `result.attempt1.txt` | `eb67faccebab0c677e2d53535f1a5eef71f479850c78bb699473729d513bb629` |
| `run.attempt1.log` | `019a6ec6bb20134c69447e56dda467d6402f82f11267945fcf2f764b12db1d1e` |
| `SHA256SUMS.attempt1` | (the ledger itself; it lists the five above) |

- **The one read:** read 1 at `2026-10-23T13:30:06Z`, HTTP 200, `curl` exit 0, class `MATCH`. The body's keys, in order: `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`. Size 347 bytes, sha256 `c9302e70…06a`. The task record §10 reports the same size and body hash for the rehearsal app factory on loopback. This is an observation of consistency, not a proof (task record §11).
- **Redaction:** no variable value, response body, header value or credential appears in any file. The script's own secret scan ran and found nothing, and its output files were kept. I also read the five output files and the log in full after the run.
- **Not written, per CR-9's interim treatment:** no path proof, no Evidence Index row, no Mirror row, no checksum sidecar other than the script's ledger.

## 8. Deviations and limitations (for OPS-30)

| ID | What differs | Effect |
| :- | :- | :- |
| D-1 | `DELEGATION_REF` is a local session ID, not a session URL. A local VS Code session has no URL, and I did not invent one. The Product Owner agreed to this form | Form only. The reference is secret-free and printable ASCII, and the script accepted it |
| D-2 | The presence answers came from the Railway CLI listing, at the Product Owner's direction, not from the Railway dashboard. The task record names no command for the view (PF07 gap); the CLI command is the vendor's own documented one. The agent, not the Product Owner, typed the answers | SC-2 rests on the CLI's account of the variable names. Values are not verified (presence only, by design) |
| D-3 | I queried the environment named `production` (PF07 §2.4 heading "Production — Railway"). I did not verify that this environment is the one serving the base URL, because that would mean inspecting the service's domain settings, which the task's Constraints exclude | The identity match shows the service at the base URL runs the candidate. It does not by itself prove the `production` listing belongs to that same service instance. OPS-30 or the Product Owner may want to confirm |
| D-4 | TypeSafe not read (§12) | None on the Ops outcome |
| D-5 | Local effects on the Product Owner's machine, outside the repository and production: the CLI rewrote `~/.railway/config.json` on its first failed call (the file went from 783 to 695 bytes, consistent with clearing the stale login; I did not read its contents), and a fresh login is now stored there. The CLI package sits in a scratch directory | See §9 |
| D-6 | `python` is not on `PATH`; the pre-push `lanes` check ran with `python3` and without the CI install. The `replay` mode was not run | See §10 |

## 9. Before and after state, side effects

- **Production (Railway service, variables, deployment):** no change. Actions on it were one `GET` of `/internal/version` (no credential header, no override header, no other endpoint) and read-only CLI queries. Before and after: not applicable, no mutation.
- **Repository:** the run wrote nothing in the checkout. The checkout was clean immediately after it. Publication is the branch in §10.
- **Product Owner's machine:** D-5. The valid Railway login now in `~/.railway/config.json` was created by the sign-in the Product Owner approved. It stays until the Product Owner runs `railway logout` or revokes the session at railway.com. I did not log out.
- **Temporary files:** work directory and scratch files under the session's scratchpad (outside the repository), including the filter script and the CLI package. They hold no value.

## 10. Success criteria and publication

| ID | Executor's observation | State |
| :- | :- | :- |
| SC-1 | Read 1 class `MATCH`; `expected_identity.attempt1.txt` shows `pinned_equal yes` | Met on attempt 1 |
| SC-2 | Seven names recorded, all `SET`, none `NOT_OBSERVED`. Environment disposition under PF04 §9.1 "Ops tasks" item 4: `validated` for the one intended environment (production), within D-2 and D-3. This bounded slice implies nothing about PF09 scope or closeout | Recorded |
| SC-3 | Files copied byte for byte; ledger verifies five of five `OK` in the work directory and in the repository path; no path proof, Index or Mirror row written | Pending the Product Owner's merge. Path-proof coverage follows CR-9's interim treatment |
| SC-4 | No production configuration change. The rollback condition did not arise. Before and after: no mutation | Met |

**Publication facts:**

- **Branch:** `docs/20261023-hde-crd-0002-wu-ops-01-execution`, from `origin/main` at `45f045ba`.
- **Commits:** `8d7424c5` (the six evidence files only); this record in the next commit.
- **Pull request:** [#704](https://github.com/amthorn78/glow-hdengine-v2/pull/704). I opened it and did not merge it. The Product Owner merges. The number was added by a follow-up commit on the same branch, after the pull request opened.
- **Read-only check (task §8.3 step 5):** `python3 tools/ci/prepush_check.py lanes` under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`) on commit `8d7424c5`: `evidence=true`, every other lane `false`, `path_count=6`, `PREPUSH_CHECK_RESULT: PASS lanes=PASS`. It ran without the CI install (no pytest, no `-e .`), so `replay` was **NOT RUN** for that reason. The hosted `evidence` lane on the pull request is the check of record. The pre-push result is not CI's result, not QA and not governed evidence.
- **Read-back:** this record was read back once after saving; see the pull request for the final blob.

## 11. Recovery, residual state and unresolved items

- **Recovery:** none needed. The task changed nothing in production.
- **Residual state:** the machine-side effects in D-5 and §9; the unmerged pull request; the unreviewed CR-9.
- **Unresolved items and owners:**
  - CR-9 disposition: Isis (PROPOSED, unchanged).
  - Merge: the Product Owner.
  - Receipt (OPS-30): the creator IA.
  - Whether the Railway sign-in should be revoked, and whether D-3 needs a dashboard check: the Product Owner.
- **Not done and not claimed:** no second or third read (not needed; the first matched); no second attempt; no rollback; no path proof.

## 12. TypeSafe reading and surface advice (for OPS-30)

Run once, with the installed TypeSafe scoring skill (request v8.2), on an action text describing OPS-30's work, session kind `review`:

> TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-23T13:30:54Z). Do not fill in a reading by hand.

- **TypeSafe: not read.** Reason: the service refused both attempts with HTTP 403. The skill says the `Glow app` environment attaches the credential, and this local session is not that environment. That is the probable cause; I did not verify it.
- No Notion row was written. Nathan's pick for OPS-20 is not stated.
- **Surface advice for OPS-30:**
  - A repository-only review. It needs read access to this branch or the merged files, and to the task record. It does not need Railway access, network access to production, or any credential.
  - It writes one file, the receipt, through the creator IA's own pull request.
  - Merge this pull request first, or read the branch directly.

## 13. Carried CANON_CONFLICT_REGISTER

CR-1 to CR-8 are carried unchanged from the task record, all decided. CR-9 is carried unchanged: PROPOSED, decision owner Isis, not yet reviewed (path proofs under the WU-OPS-01 Ops root). Execution found no new conflict and silently resolved none. Interim treatment applied: canon governs; no path proof, Index row or Mirror row was written.

## 14. Nonclaims

No QA PASS, Live QA completion, final acceptance, public-surface change, CLI flag change, PF09 or PF30 status change, change completion, PF-canon drainage or closeout. No claim of `/internal/version` tokens (HDE Governance §2.0.2) and no INTVER family artifact. The read proves the release running at the base URL at `2026-10-23T13:30:06Z`. It does not prove reachability from another network, any behaviour, or the deployed commit (`build_commit` is a fixed source value; deployment is judged by `release_id` alone, Plan delta 01 P-9). Presence is not value correctness.

## 15. Prompt-use provenance

`GCFPE_PROMPT_USES`:

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-OPS-20-20261023-WU-OPS-01-01` |
| Change identity | CRD HDE-CRD-0002 |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| Work unit | WU-OPS-01 |
| Ecosystem release | GCFPE-20261009.1 / 100926.1 |
| Prompt | OPS-20 — Execute Bounded Ops Task — 100926.1, page state of 2026-10-12T02:29:42.649Z |
| Role and stage | PO-delegated target-environment operator, Ops execution |
| Capture time | 2026-10-23T13:34:00Z |
| Execution identity | local Claude Code session `4b626dac-628b-40e4-9f68-31528cc344bc` |

- **Repository persistence: PENDING / NON_GATING.** `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main` (`docs/changes` holds `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`), so the usage stays in this record's metadata. Owner: the authorized repository writer, when the procedure is installed.

## 16. Canon relied on

Read on `main` at `45f045ba` from `docs/pfcanon/`. PF10 is v13.7.4 (433,368 bytes, sha256 `8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff`, matching the task record's pin).

| Topic | Sections read in this session |
| :- | :- |
| Ops task record, delegated execution, evidence posture | PF27-Canon-Plan-Templates v2.0.5 §3 (Definition; Execution authority; IA facilitation; Ops Task record fields; Controlled execution contract; Evidence posture) |
| Ops tasks: delegation predicates, evidence, environment-validation disposition, no governance drift; QA/Ops sources and currentness | PF04-Canon-HDE-Governance v2.8.7 §9.1 "Ops tasks" items 1 to 5; §9.1.4 |
| `/internal/version`: no auth header, status, six-field body | PF04-Canon-HDE-Governance v2.8.7 §10.5 (intent, interim auth posture, methods, payload) |
| Target facts | PF07-Canon-Glow-Infrastructure v2.3.3: the HD Engine row (project, service, base URL) and the production block, by search; the task record carries the rest |
| WU-OPS-01 scope | PF10 addendum 2.19 (approved delta header and decision; P-9, P-18, P-19, P-20) |
| Taken from the task record and not re-read here | PF12 §8.3 and §8.6.3 (path-proof writer), PF19 §11.1 (Ops evidence consumed by QA), PF10 addenda 2.11, 2.18 and 2.20, and PF07 sections other than those above. This record relies on the task record's reading of them and does not claim to have verified them again |
