---
artifact_type: QA_RCA
artifact_id: HDE-CRD-0002-QA120-QA-RCA
artifact_version: "1.0"
predecessor: none. This is the first QA RCA for the HDE-CRD-0002 QA run
companion_report: docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md (QA_REPORT_ID HDE-CRD-0002-QA120-QA-REPORT, v1.0; verdict PASS)
run_verdict: PASS
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002
role_session_ref: the continuing Kronos session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: CRD / HDE-CRD-0002 / QA-120 / complete run of approved QA Plan v1.3 (checks 1 to 21; S01 removed, S02 to S22)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-120 — Create Final QA Report and RCA — 100926.1 (https://app.notion.com/p/3f44590a05eb81a4a3fbc0fae65d153e; page state 2026-10-12T02:29:51.614Z, re-read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a)
evidence_of_record: audit/qa/hde-crd-0002/ on main at 48cdc25e5856773375fe703ecffc01a6f753cc34 (manifest SHA-256 203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874; 21 checks, all PASS)
observed_revision: 48cdc25e5856773375fe703ecffc01a6f753cc34 (origin/main at this invocation)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-120 (QA-120 is not an addendum producer)
created_at: 2026-10-26T00:50:00Z
---

# HDE-CRD-0002 — QA RCA and Doc Delta summary (QA-120), v1.0

## 1. Summary

- **Outcome.** The QA run passed: all 21 checks of approved QA Plan v1.3 are `PASS` in the manifest and in their step-log headers, and each was accepted at QA-110 (companion Report §1 and §4).
- **One product defect.** The run found one product-behavior failure, QA110-F01. In check 13 attempt 1, the pre-push check's read-only guard tripped on a full-history checkout although every report passed. The cause is evidenced (§6.1). The defect was remedied by WU-REM-02 and verified at state (b) by check 13's remediation verification `RV-1`.
- **What else this RCA records:**
  - two `TOOLING_BLOCKED` executions, each superseded by an accepted Moon Loop rerun (checks 3 and 21);
  - one independent repository-test portability defect (O-1);
  - five QA Plan reviews, three of them `DENY`, and a prompt-route gap;
  - process deviations, an assembly gap (G-1) and a session incident (I-1).

  None of them changed a predicate outcome of the accepted run.
- **Not invented.** No incident is invented for the passing run (Glow QA Guide §3.1.2). Where the record does not establish a cause, §8.5 says so.
- **Canon updates.**
  - The product change is already recorded in HDE Build Notes 2.27 and the repository `README.md`. QA identifies no further PF-Canon delta for product behavior.
  - Two Product Owner drainages stay pending (PO-2, PO-5).
  - §9.2 proposes one process delta (D-1) and records two non-canon carriers. None is a blocker.
- **Closeout readiness.** The QA outcome supports `CLOSE` (§11). The decision is Isis's, through CL-C-10.

## 2. What ran and what the outcomes mean

- **What ran.**
  - Checks 1 to 12, 14 and 15: executed under approved Plan v1.2, whose text for them Plan v1.3 keeps, at state (a).
  - Check 13: attempt 1 under Plan v1.2 at state (a), then `RV-1` under Plan v1.3 at state (b).
  - Checks 16 to 20: against the deployed service at `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`. Check 20 includes one live vendor call.
  - Check 21: on the published family.
- **Outcome classes in this run** (Plan Templates "Exact status predicates"; Plan v1.3 §7 rule B):

| Class | Where it occurred | Meaning here |
| :- | :- | :- |
| `PASS` | All 21 current statuses | The check's decisive predicates hold on captured output, re-read at QA-110 |
| `FAIL_BEHAVIOR` | Check 13 attempt 1 (QA110-F01) | The delivered surface (`tools/ci/prepush_check.py`, S20) contradicted an explicit predicate with readiness held and the QA tooling trustworthy. A product defect, not an environment fault |
| `TOOLING_BLOCKED` | Check 3 attempt 1; check 21's first run | A readiness read failed, so the check could not reach its predicates. Neither was a behavior result. Each was superseded by an accepted rerun inside the same attempt (§7) |
| `FAIL_TOOLING` | None | — |

- **Hosted CI and the pre-push tool's result** are cited evidence, not QA verdicts (Report §7, §16).

## 3. Source-of-truth posture

- **Primary execution sources:**
  - the governed primaries under `audit/qa/hde-crd-0002/checks/<check_id>/primary.log` and the manifest `audit/qa/hde-crd-0002/qa_step_logs_manifest.json`, on `main` at `48cdc25`;
  - the QA-100 results v1.0 to v1.3 and the QA-110 reviews v1.0 to v1.2, which carry the per-check decisions.
- **Change-specific guidance records:** HDE Build Notes 2.27 (the QA110-F01 remedy) and 2.28 (the QA-110 review of checks 1 to 15).
  - Both carry direct evidence pointers (commit and blob identities, file paths, run numbers), not only prose.
  - Neither is evidence-light for the facts this RCA uses.
- **Canon homes for interpretation:**
  - Glow QA Guide §3.1.2, §3.4.8, §3.5.7 and §10.6;
  - Plan Templates "Moon Loop allowed (bounded)" and "Bounded step-level rerun posture";
  - Change Process Guide §0.4.1.2 and HDE-Schemas & Artifacts' QA RCA content list, applied for their content to this CRD (§12).
- **Used only for framing:**
  - Live QA Guide v1.0 (IR-1 to IR-11);
  - QA Audit v1.0 and readiness v1.1;
  - the Specification's S-rows.

## 4. Coverage vs QA Plan, in plan order

Every check is **Fully evidenced**: its governed primary exists, is indexed in the Human Evidence Index and the Machine Mirror, and matches its path proof (Report §7). The Report's §4 gives the primary SHA-256 values and the evidence commits. "Deviation" names any accepted divergence between the planned and the executed step, even where the status is `PASS`.

| # | `check_id` | Req. | Coverage | Deviation from the approved step | Closeout impact |
| -: | :- | :- | :- | :- | :- |
| 1 | `qa-01-preflight` | Step-0 | Fully evidenced | None | None |
| 2 | `qa-02-ci-coverage` | S03 to S05 | Fully evidenced | None | None |
| 3 | `qa-03-attestation-debian` | S06 | Fully evidenced | Attempt 1 `TOOLING_BLOCKED`; Moon Loop (PO-1) wired E-D from uv CPython 3.13.17 with the system `dist-packages`, two reruns inside attempt 1 (R-1, R-2) | Caveat carried: S06 is proven under the venue's patched setuptools 78.1.1 as wired |
| 4 | `qa-04-showcompat-help` | S07 | Fully evidenced | None | None |
| 5 | `qa-05-aux-preview-band` | S08 | Fully evidenced | None | None |
| 6 | `qa-06-dev-harness-retired` | S09 | Fully evidenced | None | None |
| 7 | `qa-07-dev-reader-gate` | S10 | Fully evidenced | None | None |
| 8 | `qa-08-release-evidence-tooling` | S11 to S13 | Fully evidenced | None | None |
| 9 | `qa-09-override-matrix` | S14 | Fully evidenced | None | None |
| 10 | `qa-10-endpoint-catalog` | S15 | Fully evidenced | None | None |
| 11 | `qa-11-template-and-documents` | S16 to S18 | Fully evidenced | None | None |
| 12 | `qa-12-security-review` | S19 | Fully evidenced | None | None |
| 13 | `qa-13-prepush-check` | S20 | Fully evidenced | Attempt 1 `FAIL_BEHAVIOR` (QA110-F01) after an in-session Moon Loop (PO-3, R-2). `RV-1` ran under Plan v1.3's amended step 3 count (141) at state (b) | None remaining; the defect is remedied and verified (§6.1) |
| 14 | `qa-14-close-pack-writer` | S21 | Fully evidenced | None | None |
| 15 | `qa-15-s01-removal` | S01 (removed) | Fully evidenced | None | Evidence for S01's removal; its close representation is a close-stage point (§11) |
| 16 | `qa-16-deployed-identity` | Step-0C | Fully evidenced | Header `timestamp_utc` typed during assembly (G-1, R-3) | None; no predicate depends on it |
| 17 | `qa-17-deployed-not-found` | S02 | Fully evidenced | None | None |
| 18 | `qa-18-deployed-dev-surfaces` | S10, S19 | Fully evidenced | None | None |
| 19 | `qa-19-deployed-reader-input` | S19 | Fully evidenced | None | None |
| 20 | `qa-20-live-vendor-override` | S14, S19 | Fully evidenced | None; venue V-B and the Product Owner as initiator were the Plan's options, chosen by the Product Owner (PO-QA100-2) | None |
| 21 | `qa-21-evidence-admission` | S22 | Fully evidenced | First run `TOOLING_BLOCKED`; Moon Loop (PO-QA100-6) restored one Markdown file in the throwaway copy only; republished (R-4) | None; an independent run on unmodified `main` gave the same counts |

**Execution order and selection.** Collections v1.2 and v1.3 were executed before their pull request merged, by the Product Owner's direction (PO-QA100-3). Check 21 ran after the Product Owner closed the rails (PO-QA100-5). The union of selections equals all 21 checks (Report §4).

## 5. Same-run runtime proof

The changed runtime surfaces that the Plan requires proven on the deployed service each have same-run proof against one deployed identity, judged by `release_id` (HDE Build Notes 2.19). Check 16 read it live, and check 20's P1 matched it.

| Surface (requirement) | Governed proof |
| :- | :- |
| Unknown non-compat paths answer not-found (S02) | `checks/qa-17-deployed-not-found/primary.log` |
| Dev surfaces refused in production (S10, S19 F03) | `checks/qa-18-deployed-dev-surfaces/primary.log` |
| Reader input handling (S19 F01) | `checks/qa-19-deployed-reader-input/primary.log` |
| Production vendor override, refused and then one bounded call (S14, S19 F05 and F06) | `checks/qa-20-live-vendor-override/primary.log` |

Operator-CLI and tooling surfaces (S07, S08, S11 to S13, S20 to S22) are proven local/offline, as the Plan classes them (Report §5). No deployed surface is claimed beyond these rows.

## 6. Failures, anomalies and their causes

### 6.1 QA110-F01 — product behavior (`FAIL_BEHAVIOR`; check 13 attempt 1; S20)

- **Observed.**
  - Two executions on the Product Owner's workstation (Ubuntu 26.04.1, git 2.53.0) at state (a): step 1 exited 4 with `PREPUSH_CHECK_READ_ONLY_VIOLATION`, although all five reports passed.
  - The second execution followed an in-session Moon Loop that removed a venue cause (`TMPDIR` on another filesystem; O-1). That rerun's replay passed, but the violation stayed (QA-110 v1.0 §6).
- **Cause (evidenced; HDE Build Notes 2.27 "Cause").**
  - `make_copy` in `tools/ci/prepush_check.py` made every throwaway copy with `git clone --shared`, so each copy borrowed the source checkout's object store.
  - In replay step 08, the tool's own owner test commits in `--shared` fixture clones of the replay copy. Writing an object that already exists in a reachable store freshens the file that holds it, here the source checkout's pack.
  - The guard compares the lstat identity of every file under the source's `.git`, so it correctly reported the change.
  - The defect was in the copy mechanism; the guard's precision was correct.
- **Why earlier runs passed.**
  - The earlier passing runs used shallow sources, and a shallow source disables `--shared`, so the copies held their own packs (2.27).
  - Those runs were the WU-PR-06 PR-40 lineage review on `fc51620` and the QA Audit's item 9 rehearsal on `0b15328d`.
  - Plan v1.2's E-L is a full-history clone, which is the operator's real environment, and it engages the mechanism. Git's version is not the factor: the escalation report's H-2 was answered at `RV-1` (O-8), when the remedy held under git 2.53.0 as it did under 2.43.0.
- **Remedy and verification.**
  - WU-REM-02 (amthorn78/glow-hdengine-v2#734, squash `22a3bc0`): the copies own their objects (R-1) and a violation names what changed (R-2). It was accepted at PR-40.
  - Plan v1.3 changed check 13's step 3 count to 141 (C-1, through the Product Owner's route D-1 to D-3, CR-12).
  - `RV-1` passed under git 2.53.0 in the venue class that failed, which meets 2.27 V-6 (QA-110 v1.1).
- **Contributing conditions.**
  1. The recorded validation venues before QA, the PR-40 lineage review and the QA Audit's rehearsal, used shallow sources (2.27). QA's E-L was the first full-history source. Hosted CI's checkout depth is not established here (§8.5).
  2. The owner test's own `--shared` fixtures are what write. Their effect on a developer's checkout (O-A) stays with the Product Owner as a later-change candidate.
  3. Check 13's first execution also met an independent venue fault (O-1), which made the first signal noisier. The Moon Loop separated the two.
- **Detection.**
  - The defect was found by the approved QA environment, as designed: Plan v1.2 bound E-L to a full-history clone, and the Plan did not restrict the venue's git version.
  - It was not found earlier because both earlier recorded venues used shallow sources, which disable the mechanism.

### 6.2 Check 3 attempt 1 — `TOOLING_BLOCKED` (venue interpreters)

- **Observed:** "No interpreter meets step 1 in this venue: /usr/bin/python3 (3.14.4) makes _distutils_system_mod importable; /usr/bin/python3.13, 3.12 and 3.11 are absent". The bytes are preserved at `docs/ephemeral/HDE-CRD-0002-QA100-t03-attempt1-primary-v1.0.log`, 12,380 bytes, SHA-256 `f67c2274cb9288f464616b5db503846b36dacd6f245b03521af9b2e4872961e3`.
- **Cause (evidenced):**
  - Collection v1.0's NZ-02 listed only system interpreters (`/usr/bin/python3*`). It was written against an Ubuntu 24.04 container, where `/usr/bin/python3.13` met E-D.
  - The executor's venue, an Ubuntu 26.04 workstation chosen by the Product Owner, had none that met it. This is Kronos's collection defect O-4.
- **Correction:** the Product Owner directed a Moon Loop (PO-1). E-D was wired from uv CPython 3.13.17 with the system `dist-packages`, with a reinstall after rerun 1's `rpds.rpds` import error. No repository file, predicate or expected value changed (R-1).
- **Residual:** R-1's caveat. S06 is proven under Ubuntu 26.04's patched setuptools 78.1.1 as wired, not under the Plan's literal construction or under other distributions. PO-2 ("Do not pin tool versions") is the context.

### 6.3 Check 21's first run — `TOOLING_BLOCKED` (Plan guard too narrow)

- **Observed.** Readiness (i), the code-identity diff against `22a3bc0` excluding Plan v1.3's storage prefixes, printed `docs/prompt_ecosystem_management/authoritative-surfaces.md | 6 +++---`. That file changed on `main` in `63335e66` (amthorn78/glow-hdengine-v2#737), after `da5735eb`.
  - Plan v1.3 §7 rule A maps a non-empty diff to `TOOLING_BLOCKED`.
  - Every other read and predicate held.
  - The first run was published at `d639772d` (blob `3e1562ea1175`).
- **Cause (evidenced; O-11).** Plan v1.3's state-(b) guards exclude only `docs/ephemeral` and `docs/pfcanon`, two of the eight CI-exempt storage prefixes that `AGENTS.md` and `ci/checks/classify_ci_changes.py` define. A change confined to a third prefix is not code, but the guard counted it.
  - This is Kronos's planning defect (the Plan's author).
  - QA-70 reviews v1.3 and v1.4 did not catch it either.
- **Correction:** the Product Owner directed a Moon Loop (PO-QA100-6). In the throwaway copy only, the Markdown file was restored to its state (b) bytes; the rerun passed and was republished at `7974e2c7`. An independent run on unmodified `main` gave the same counts (31, 1, 81, 1 passed), so the restored file bears on no predicate (R-4).

### 6.4 O-1 — independent repository-test portability defect (outside S20)

- **Observed:** in check 13's first execution, the replay failed two tests in `tests/ops/test_hde_epic038_ops03.py` with `EXDEV`.
- **Cause (evidenced; QA-110 v1.0 §6.6):** the OPS03 tool's fixed `RUN_ROOT` `/tmp/hde-epic038-ops03` (tmpfs) and pytest's `tmp_path` under `TMPDIR` (ext4) were on different filesystems, so a link or rename between them failed. With `TMPDIR` unset, as on hosted CI, both are under `/tmp`.
- **Handling:** later runs avoided it with NZ-08 (`TMPDIR` unset). It is not a CRD-0002 requirement. It stays open with Thoth, and with the Product Owner if independent (HDE Build Notes 2.28).

### 6.5 QA planning and review cycles

| Round | Decision | What it found | Cause class |
| :- | :- | :- | :- |
| QA-70 review v1.0 of Plan v1.0 | `DENY` | Three blockers (FND-001 to FND-003) and eight caveats | Author defects in Plan v1.0 |
| QA-70 review v1.1 of Plan v1.1 | `DENY` | FND-101: common rule A made check 21's test copy unexecutable in every run | Introduced by the revision; partly the reviewer's own, since review v1.0's RL-05 omitted the coupled constraint for check 21 ("Non-author penalty rule": not author churn) |
| QA-70 review v1.2 of Plan v1.2 | `APPROVE` | — | — |
| QA-70 review v1.3 of Plan v1.2, after the remedy | `DENY` | FND-201 to FND-203: no commit had both the Plan's tested code and the remedy | FND-202 and FND-203 are Review Drift, the reviewer's: the coupled constraint was visible at ESC-40, when C-1 named the change |
| QA-70 review v1.4 of Plan v1.3 | `APPROVE` | — | — |

- **Route gap.** HDE Build Notes 2.27 C-1 required a Kronos-authored approved-Plan delta with a QA-70 delta-mode decision and no QA-80, but no prompt in release 100926.1 authors such a delta.
  - The Product Owner decided the route instead: QA-70, then QA-80 if needed, then QA-90 (direction v1.1, D-1 to D-3; CR-12 `APPROVED`).
  - The gap is MB-021 on the GCFPE Modification Backlog, with the GCFPE-MGMT-10 maintenance owner.
  - Unresolved risk (CR-12): no PF10 addendum records the Plan v1.3 change; the QA-70 reviews v1.3 and v1.4 and the redline application report v1.2 do.

### 6.6 Process deviations and gaps

| Item | What happened | Cause | Effect |
| :- | :- | :- | :- |
| R-2 | Checks 3 and 13 (and later check 21) re-executed inside attempt 1 at the Product Owner's in-session direction, although Plan §9 lets only Kronos allow an attempt 2 | The Product Owner directed the reruns in the executing session (PO-1, PO-3, PO-QA100-6) | Each check's one ordinary rerun is consumed. No outcome changed: two reruns were accepted Moon Loops, and check 13 went through escalation |
| PO-4 | The evidence of checks 1 to 15 was first left uncommitted in a scratch clone | QA-100 Execute step 4 commits evidence only under an explicit grant, and collection v1.0 §4.8 left the grant to the Product Owner | The Product Owner's direction, recorded through amthorn78/glow-hdengine-v2#727, persisted it in amthorn78/glow-hdengine-v2#726. The QA-100 prompt defect is reported to the GCFPE-MGMT-10 maintenance owner; PO-5 drainage is pending |
| PO-QA100-3 | Collections v1.2 and v1.3 were executed from the open amthorn78/glow-hdengine-v2#743, before it merged | Product Owner direction ("just proceed") | A sequencing deviation only: the bytes on `main` equal the executed pins, whose SHA-256 values QA-110 v1.2 recomputed |
| G-1 (QA-100 gap; not Live QA Guide §8's G-1) | Check 16's header `timestamp_utc` reads 23:40:00Z. The value was typed during assembly; the requests ran at 23:18:11Z to 23:18:12Z, and the primary was written at 23:23:10Z | A hand-typed `captured_at_utc` in the task spec, instead of `date -u` at assembly | Kept as a recorded deviation (R-3). Checks 17 to 20 carry their real finalization times (QA-100 results v1.2), and collection v1.3 had check 21's read from `date -u` at assembly |

### 6.7 I-1 — session incident (not an evidence defect)

- **What happened.** At about 2026-10-25T23:20Z, during check 16's local secret scan in the executing session, a malformed shell line printed the workstation environment into that session's transcript. The line was an `export $(<command>)` substitution that reduced to a bare `export`. The values printed included `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL`.
- **What it contradicts.** Glow QA Guide §3.5.7: keep values "out of conversations, logs, files and commits".
- **What it did not reach.** No repository file, commit or published primary holds a value; every primary scanned `NO_HIT` (QA-100 results v1.2 §7; QA-110 v1.2).
- **Cause (evidenced).** A command-construction error by the executing session: an empty substitution turned a scoped export into a full environment dump. Nothing between the session and the shell stopped a bare `export`.
- **Decision and prevention.**
  - The Product Owner decided not to rotate (PO-QA100-4) and asked that it not recur.
  - The executing session installed a PreToolUse hook on the workstation, `~/.claude/hooks/block-env-dump.py`. Before they run, it denies bare `export`, `env`, `printenv`, `set` and `declare -x`, `export $(<command>)`, reads of `/proc/*/environ` and `echo $<secret>`. The hook was proven to fire (QA-100 results v1.2 §7).
  - The workstation's values are not shown to be production's, and the production service's values were never printed (same record).
- **Open.** The transcript's handling stays with the Product Owner. The hook is local to the workstation and is not a repository control.

### 6.8 Other anomalies (recorded, not causes of any outcome)

- **O-2, O-5, O-12:** every HDE-CRD-0002 path proof carries `produced_at_utc` `2026-09-22T14:25:29Z`, and republication keeps an earlier `mtime_utc`. The validators accept both. `AGENTS.md` "Path-proof portability" treats `mtime_utc` as provenance. Check 21 recorded them.
- **O-9:** the deployed identity's `build_commit` `9479d28` is an older commit. It is recorded and not judged, since the identity is judged by `release_id`.
- **O-10:** the "final LF no" label in the bodies of checks 16 to 19 is a display flag; the bytes end with one LF.
- **TypeSafe 403:** readings could not be taken in the executors' local venue (HTTP 403), so those records state "TypeSafe: not read". This session's readings were taken.

## 7. Accepted deviations

| Deviation | Check | Basis of acceptance | Changes a proof target |
| :- | :- | :- | :- |
| E-D wired from uv CPython with the system `dist-packages` (R-1) | 3 | Plan Templates "Bounded step-level rerun posture"; Glow QA Guide §3.4.8 (environment wiring) | No; caveat on S06's venue |
| In-session reruns consume the ordinary rerun (R-2) | 3, 13, 21 | Precedent HDE-EPIC040 QA-110 review v1.0 LR-01; Plan §9 | No |
| `TMPDIR` unset, leftover OPS03 directories removed (PO-3) | 13 | Moon Loop, environment only | No; it removed a venue cause and did not resolve the check |
| `RV-1` as remediation verification, not attempt 2 (QA-110 v1.1) | 13 | Plan §9; Glow QA Guide §10.6 | No |
| Typed header timestamp kept (R-3) | 16 | Recorded assembly deviation; no predicate depends on it | No |
| One Markdown file restored in the throwaway copy (R-4) | 21 | Moon Loop; independent run on unmodified `main` | No |
| Normalizations NZ-01 to NZ-08, NZ-20 to NZ-25, NZ-30 to NZ-32 | Several | Each keeps objective, target, rails, evidence identity and predicates (Report §9) | No |

**Pre-remediation context** (Glow QA Guide §9.2.15.6). Each Moon Loop's failure signature, minimal change set and rerun basis are recorded in the same governed primary, and the earlier bytes are preserved (Report §7):
- check 3: the attempt-1 receipt and the "Moon Loop E-D setup" block;
- check 21: the "FIRST RUN (failure signature)" and "MOON LOOP" blocks.

**Execution venue** (same section). A Codespaces venue is `NOT APPLICABLE`: no claim concerns a Codespaces-specific property. The venues material to a proof are the ones the Plan's checks name: E-D for check 3, E-P for checks 16 to 19, and V-B for check 20 (Report §3, §6).

## 8. Root cause analysis

### 8.1 Patterns

Two patterns account for every failure and friction item in §6:
1. **Venue assumptions not tested against the real operating environment.** QA110-F01 (shallow validation venues), check 3 attempt 1 (a container's interpreters assumed on a workstation) and O-1 (`TMPDIR` on another filesystem).
2. **Coupled constraints missed while writing or reviewing guards.** FND-101, FND-202 and FND-203, and O-11 (a storage-prefix list narrower than the repository's).

### 8.2 Primary root cause (product)

The pre-push check's throwaway copies shared the source checkout's object store, while its read-only guard watched that store. Under a full-history source, a write inside a copy is therefore visible to the guard as a change to the operator's checkout. The defect is in the copy mechanism (HDE Build Notes 2.27), and WU-REM-02 removed it.

### 8.3 Contributing factors

- The recorded validation runs before QA used shallow sources, which disable `--shared` (2.27).
- The owner test's own `--shared` fixtures perform the writes (O-A, unchanged).
- QA collections were authored in a cloud container and executed on a workstation with different interpreters and filesystems (O-4, O-1).
- Plan guards and review redlines were written per check, without a whole-plan list of coupled constraints (FND-101, FND-202, FND-203, O-11).
- Executions were directed in-session, outside the Plan §9 rerun gate (R-2).

### 8.4 What made the failures hard to detect earlier

- **QA110-F01.** The same code passed in two earlier recorded venues. The depth of the source checkout was the difference, but QA-110 v1.0's venue comparison (§6.4) did not list depth; ESC-30 and ESC-40 identified it (2.27).
- **O-11.** The guard's two excluded prefixes covered every change on `main` until amthorn78/glow-hdengine-v2#737 touched a third prefix between state (b) and check 21.

### 8.5 Causal limits

- **Which file changed in attempt 1.** The post-run inspection followed step 3 and could not show which `.git` file changed in attempt 1, or which step wrote it.
  - The mechanism is established by reproduction instead: QA-110 v1.0's scratch-repository verification under git 2.43.0, ESC-30 and ESC-40, and the remedy's V-3 negative control, which names the pack's (mtime, ctime).
  - That attempt 1 was this mechanism and nothing else is the strongest supported reading, not a direct observation.
  - `RV-1` passing in the same venue class supports it.
- **Hosted CI's checkout depth.** This RCA does not establish the depth on any hosted run. It relies on 2.27's statement that "the earlier passing runs used shallow sources".
- **I-1's exposure.** No exposure beyond the transcript is evidenced, and none is ruled out beyond what the scans cover. The Product Owner holds that risk (PO-QA100-4).

### 8.6 Remediation-loop assessment

- **Route.** QA110-F01 took the canonical route of Glow QA Guide §10.6: QA-110 `ESCALATION_REQUIRED`, ESC-10, ESC-30, ESC-40 (`APPROVE_AS_CHANGED`, C-1), WU-REM-02 through PR-30, PR-35 and PR-40, the Plan route of CR-12, and QA-90/QA-100/QA-110 for `RV-1`.
- **One deviation.** C-1's delta route had no author prompt, and the Product Owner's direction replaced it (CR-12).
- **No reopening.** No accepted check was reopened. Checks 1 to 12, 14 and 15 stood at state (a), and the remedy changed no release member.
- **Bounded reruns.** Each Moon Loop was bounded to the QA venue or a throwaway copy, and each superseded attempt is preserved byte for byte (Report §7).

### 8.7 Evidence-hygiene assessment

- **Integrity.**
  - Every primary was published through the canonical writer and validated by the five read-only validators and `validate_crd_check_family`.
  - The Index and Mirror hold every key.
  - The evidence pull requests' hosted CI passed (Report §7).
- **Secrets.** No primary holds a secret value. I-1 is a transcript incident, outside the evidence.
- **Failure history.** Preserved (Report §7). The one assembly inaccuracy (G-1) is recorded rather than rewritten.
- **Timestamps.** Path-proof timestamps behave as provenance only (O-2, O-5, O-12).

## 9. Doc deltas

### 9.1 Carried from the run

| Item | Target | Owner | State |
| :- | :- | :- | :- |
| PO-5: evidence persistence | Glow QA Guide §3.4.3 | Product Owner | `PENDING_DRAINAGE` (HDE Build Notes 2.28) |
| PO-2: do not pin tool versions | Owner's choice of home | Product Owner | `PENDING_DRAINAGE` |
| QA110-F01 remedy's limits (copies own their objects; a borrowing source costs a repack) | Recorded in HDE Build Notes 2.27 and `README.md` "Pre-push check (HDE-CRD-0002)" | — | Recorded; no further QA delta |
| LR5-O1 doc-delta candidate (IR-3 observation: `GET //reader?v=1` answered `403`) | As the Product Owner decides | Product Owner | Recorded, no predicate |
| Check 1's doc-delta surface under CR-11 | — | — | Check 1 found none |
| Undrained HDE-CRD-0002 records, HDE Build Notes 2.19 to 2.28 | Their stated owning homes | Their stated owners | Not QA's; no claim |

### 9.2 Proposed by this RCA

| ID | Finding | Proposed delta (by title) | Owner | Blocker |
| :- | :- | :- | :- | :- |
| D-1 | O-11 | Plan Templates: a code-identity guard that excludes storage paths uses the repository's whole set of CI-exempt storage prefixes, as its change classifier defines them, rather than a hand-written subset | Product Owner (canon owner) | No |

**Recorded outside PF-Canon:**
- the approved-Plan delta route is a prompt-ecosystem matter (MB-021, GCFPE-MGMT-10 maintenance owner);
- the QA-100 evidence-commit default is a prompt defect (PO-4 record §6, same owner).

**Considered, no delta proposed:**
- For I-1, Glow QA Guide §3.5.7 already states the rule, and the prevention is a workstation control.
- For QA110-F01's venue lesson, the Plan's full-history E-L already worked as designed.

## 10. Lessons

| ID | Lesson | Owner |
| :- | :- | :- |
| L-1 | A tool that inspects `.git` must be validated on a full-history source as well as a shallow one, because a shallow source disables object borrowing | Implementation Agent and PR reviewers for later tooling work |
| L-2 | A QA task's interpreter selection names a fallback that the executor's venue can supply, not only system paths, and the collection records the venue it was authored against (O-4) | Kronos, for later QA-90 tasks |
| L-3 | Guards that exclude paths take the classifier's prefix list, not a subset (O-11; D-1) | Kronos (Plan author) and QA-70 reviewers |
| L-4 | When a remedy changes an approved Plan's tested source, list every guard and coupled constraint it touches in one pass (FND-202, FND-203) | QA-70 reviewers; Kronos |
| L-5 | Timestamps in task specs are read from `date -u` at assembly, never typed (G-1); collection v1.3 already does this | Kronos |
| L-6 | Shell lines that touch credentials are built without substitutions that can collapse to bare `export`, `env` or `set`; a deny hook backs this (I-1) | Executing sessions; Product Owner for workstation controls |
| L-7 | The evidence-commit grant is settled before execution (PO-4) | Kronos in collections; GCFPE-MGMT-10 maintenance owner for QA-100 |

## 11. Closeout-readiness recommendation and completion states

- **Recommendation.** The QA outcome supports `CLOSE`: the run is complete, every §11 criterion of Plan v1.3 holds, and no acceptance-critical QA defect remains open.
  - This is a closure-oriented review result and not the closure decision. Isis decides `CLOSE` or `DO_NOT_CLOSE` through CL-C-10.
  - It is not a `SATISFIED` close-pack decision.
- **Points the closure owner weighs** (QA blocks on none of them):
  - The close representation of S01 (Live QA Guide §8 G-1; IR-11): the close writer requires S01 among the requirement IDs, and check 15 supplies the removal evidence.
  - CR-9: `PROPOSED`, unreviewed.
  - Measure (2) of the FND-001 remedy belongs to the close-pack pull request.
  - O-1, O-A, D-1/LR6-O1, FND-028 and the S19-R01 to R07 routed items stay with their owners.
  - I-1's transcript handling.
- **Completion states.** Each is stated separately; no state implies another.

| State | Posture |
| :- | :- |
| Repo-supported completion (QA) | The QA run is complete with `verdict: PASS`, supported by governed evidence on `main` |
| Canon-drain completion | No claim. PO-2 and PO-5 are pending, and HDE Build Notes 2.19 to 2.28 are undrained |
| Formal close-pack completion | No claim. No HDE-CRD-0002 close pack or candidate source exists |
| Acceptance and closure; Product Owner closeout action | No claim. Isis decides closure through CL-C-10 |
| Merge provenance | The evidence reached `main` through amthorn78/glow-hdengine-v2#726, amthorn78/glow-hdengine-v2#741 and amthorn78/glow-hdengine-v2#744 as the Report's §7 records; no other merge is claimed |
| Board state, formal Ops action | No claim. QA moved no board or register row and performed no Ops action |

## 12. Location and applicability

- **Where this file lives.** It is the change-process QA RCA, stored in `docs/ephemeral/` as Glow QA Guide §3.1.2 and the QA-120 prompt require.
- **How the canon content lists apply.** Change Process Guide §0.4.1.2 states its contents for "Every Live QA epic". HDE-Schemas & Artifacts lists what a QA RCA should include. This CRD's RCA applies both lists for their content only.
- **The close-pack RCA is a different artifact.**
  - The v2 close writer binds a separate QA RCA only at `audit/HDE-CRD-0002_QA_RCA.md`, or embeds summary lines in the close report (`tools/qa/generate_epic_close_pack.py`; HDE Build Notes PO-35-15).
  - That artifact belongs to the close mutation set, if one is authorized. QA-120 writes nothing under `audit/`.

## 13. Nonclaims

This RCA establishes none of the following:
- acceptance, closure or a close pack;
- PF09 or PF30 movement;
- deployment or release activation;
- canon drainage or a PF canon edit;
- a decision on any routed Product Owner item.

It proposes one doc delta (D-1) and decides none. Its causal statements are bounded by §8.5.

## Canon relied on

Read on `main` at `48cdc25`. `docs/pfcanon/` was last changed by `21141b39`, and this branch edits no `docs/pfcanon/` file.

| Decision topic | Sources read | Applied in |
| :- | :- | :- |
| RCA obligation; do not invent a failure | PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.2 (read in full at this invocation); QA-120 prompt, Execute steps 3 and 4 (read in full at this invocation) | §1 |
| RCA contents | PF06-Canon-Change-Process-Guide v2.5.4 §0.4.1.2 "Mandatory QA RCA & Doc Delta summary" (read in full at this invocation); PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6, the QA RCA content list under the close-pack baseline artifacts (read at this invocation) | §2 to §11 |
| Final closeout elements; Moon Loop context; venue posture; completion axes | PF19 v3.0.6 §9.2.15.6 (read in full at this invocation) | §7, §11 |
| Moon Loops, reruns, escalation | PF19 v3.0.6 §3.4.8 and §10.6; PF27-Canon-Plan-Templates v2.0.5 "Moon Loop allowed (bounded)" and "Bounded step-level rerun posture" (read in full earlier in this session, at QA-110 v1.0 and v1.2) | §6, §7, §8.6 |
| Cause, remedy and verification of QA110-F01 | HDE Build Notes v13.8 addendum 2.27 "Cause", "Approved delta", "Verification", "Unresolved obligations and owners" (read in full at QA-80 and re-read here) | §6.1, §8 |
| Carried drainage and deferred items | HDE Build Notes v13.8 addendum 2.28 "Required canon drainage", "Deferred obligations and unresolved work" (re-read here) | §9.1, §11 |
| Close-pack RCA location | HDE Build Notes v13.8 decision row PO-35-15 (read); `tools/qa/generate_epic_close_pack.py` `qa_rca` binding (read) | §12 |
| Secrets | PF19 v3.0.6 §3.5.7 (read in full at QA-110 v1.2); `AGENTS.md` redaction rule | §6.7 |
| Evidence attribution | `AGENTS.md` "Evidence attribution, currentness and distinct decisions", "Path-proof portability", and the CI-exempt prefix list in "Code review scope" | §6.3, §6.8, §8.7 |

**In-flight documents relied on:**
- QA-70 reviews v1.0 to v1.4 (decision lines and the findings cited);
- the ESC-10 report v1.0 (H-1 to H-4);
- the QA-110 reviews v1.0 to v1.2;
- the QA-100 results v1.0 to v1.3;
- collections v1.0 (NZ-02) and v1.3;
- the PO direction records for QA110-F01 (v1.1, CR-12) and for evidence persistence (v1.0);
- the companion Report.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-120-20261026-01 (shared with the companion Report) |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | Whole QA run: Plan v1.3 checks 1 to 21 |
| prompt | QA-120 — Create Final QA Report and RCA — 100926.1, page state of 2026-10-12T02:29:51.614Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-120 (RCA; run verdict `PASS`) |
| capture time | 2026-10-26T00:50:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
