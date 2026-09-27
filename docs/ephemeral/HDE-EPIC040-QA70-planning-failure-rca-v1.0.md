---
artifact_type: RCA
artifact_id: HDE-EPIC040-QA70-PLANNING-FAILURE-RCA
artifact_version: "1.0"
change_class: EPIC
change_id: HDE-EPIC040
subject: QA_PLAN_REVIEW v1.0 approved a QA Plan with an invalid rails model
author: Isis (Isis-50 session), reviewer who issued the approval and author of the Live QA Guide
requested_by: Nathan / Product Owner, 2026-09-27 ("your approval is rejected. The plan needs revision. But only produce the RCA now.")
rejected_decision: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md (APPROVE), rejected by the Product Owner 2026-09-27
plan_under_review: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md
evidence_read:
  - commit 06b04a9 on qa/hde-epic040-qa100-checks-1-10 ("QA Planning Failure HDE-EPIC040"), all 13 files read in full
  - docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.0.md (§4.2, T01, T07)
  - docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md §2.3, §3.4.8; docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md "Environment and rails posture"; docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md §2.2 Production table and §2.6
  - engine/runtime/determinism_env.py; engine/bodygraph/vendor_client.py L762–765; tests/bodygraph/test_check_magic10_gate_readiness.py L384
scope: RCA only. No revised review, redline, Plan change or task disposition is produced here
---

# HDE-EPIC040 — RCA: approval of a QA Plan with an invalid rails model

## 1. Summary

I approved QA Plan v1.0 even though its rails model contradicts canon in three ways:
- it uses a rails state that canon does not define;
- it switches rails, and `APP_ENV`, per command instead of per check;
- it runs checks against the production database under closed rails.

I also originated part of that model myself, in the Live QA Guide, and then spread it into the QA-90 tasks through my handoff RCA brief.

The review failed for one main reason. I verified that each command would produce its expected output in the code. I never verified that each command's operating posture was legitimate under canon. The approval is rejected and the Plan needs revision.

## 2. What is wrong in the Plan

### D1. A rails state canon does not define (check 7, command 1)

| | Evidence |
| --- | --- |
| Plan | §5.2 "Rails change inside a check": check 7 command 1 runs with `SAFE_MODE=0` while `ALLOW_NETWORK=0` "stays". QA-90 made this prefix `[C7]` (`SAFE_MODE=0 ALLOW_NETWORK=0`) |
| Canon | PF19 §2.3 defines exactly two postures: open (`SAFE_MODE=0; ALLOW_NETWORK=1`) and closed (`SAFE_MODE=1; ALLOW_NETWORK=0`), and makes the epic's posture "non-negotiable". AGENTS.md: "open rails require both `SAFE_MODE=0` and `ALLOW_NETWORK=1`". The pair `SAFE_MODE=0, ALLOW_NETWORK=0` is neither |
| Code | `engine/runtime/determinism_env.py` pins closed rails as `SAFE_MODE=1`, `ALLOW_NETWORK=0`; the vendor gate (`vendor_client.py` L762–765) requires both open values. No component treats the mixed pair as a posture |
| Value of the step | None. `tests/bodygraph/test_check_magic10_gate_readiness.py` L384 already asserts `RAILS_CLOSED_REQUIRED`, and it ran in the same check (pytest group D, 191 passed) |
| Executed | T07 recorded `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]` twice, the second time in a rerun on Python 3.13.5, outside the Plan's 3.12 requirement |

### D2. Rails and `APP_ENV` switched per command, not per check

| | Evidence |
| --- | --- |
| Canon | PF27 "Rails posture (explicit)" sets one default posture for the runbook, and "If rails change by check, list it". PF27 L755 sets vendor-step rails "for this step only" and restores them after the step. Neither permits a change inside a check |
| Plan | §5.2 cites "PF27 'Rails posture'" for a change *inside* check 7. ENV-S runs the server at `APP_ENV=prod` with clients at `dev`. ENV-D runs the readiness tool at `APP_ENV=dev` and the server at `prod`, inside one check |
| My contribution | My RCA brief v1.0 §5 turned every environment class into a per-command `env -u … VAR=…` prefix and listed row 7 as "Closed (command 1 only: `SAFE_MODE=0`…)". QA-90 adopted that as normalization N-01 with prefixes `[C]`, `[CP]`, `[C7]` and `[S]` (task collection §4.2). I also called the scheme "syntax normalization". PF27 L1151 tests whether a normalization changes the rails posture; this one does |

### D3. The production database under closed rails (checks 12–14)

| | Evidence |
| --- | --- |
| Plan | ENV-D: `SAFE_MODE=1`, `ALLOW_NETWORK=0` with a real `DATABASE_URL`, for live reads of `public.hde_body_graphs_current` |
| Target | PF07 §2.2 Production table and §2.6: the HD Engine database is `ample-illumination/production/postgres`. That is a production network endpoint |
| Canon | PF19 §3.4.8: "Manual Live QA steps that touch production endpoints run with open rails as required by the command." `ALLOW_NETWORK=0` with a live remote connection contradicts the posture's own meaning |
| How it got in | The QA Audit found that closed rails do not gate database access (QA50-F03). The Plan treated that gap as permission. **I originated the pattern:** my Guide §4.3 required the live readiness run "under the tool's closed rails, with a real `DATABASE_URL`" |

### D4. The epic's acceptance rails posture was never obtained from you

| | Evidence |
| --- | --- |
| Canon | PF19 §2.3: "Every EPIC's PO specifies what rails posture must be used to accept the epic … This posture is non-negotiable" |
| What happened | My QA-10 triage Q-2 asked only whether one open-rails step applied. My Guide §5 then set "Default rails are closed … Open rails only for the step in §4.1" on my own authority. The Plan's ENV-C/S/V/D classes rest on that default. The one decision canon reserves to you, and the one you later called the most important determiner, was never put to you |

### D5. The PASS predicate hides skipped open-rails coverage

| | Evidence |
| --- | --- |
| Plan | Check 8 passes on pytest rc 0 under closed rails |
| Executed | T08 recorded "143 passed, 3 skipped"; each skip says "showcompat vendor calls require open rails" (`tests/cli/test_showcompat_parity_and_identity.py` L108, L128, L150) |
| Canon | PF19 §2.3: a closed-rails run cannot be used as open-rails evidence, and the step log must say so explicitly. The Plan has no predicate or note for this. Rc 0 would have counted as PASS |

### D6. Environment facts measured in the wrong place

| | Evidence |
| --- | --- |
| Plan basis | QA Audit §7 recorded the *planning container* (`DATABASE_URL`, `HD_API_KEY` and `GEO_API_KEY` SET). The whole "Must be UNSET" design responds to that container |
| Executed | T01 command 2 was the ambient record, run with no prefix (task collection L338). The QA console recorded every secret key and retired key UNSET, and rails already closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`) |
| Consequence | The unset scheme you objected to guarded against a condition the execution venue did not have. Checks 11–14 need values *supplied*, the opposite problem, and the Plan does not describe that as a setup step |

### D7. Venue sensitivity declared impossible

| | Evidence |
| --- | --- |
| Plan header | "Why venue can affect the result: NOT APPLICABLE" |
| Executed | T03: `test_updater_recovers_complete_missing_state_in_one_write` failed on file mode, expected `438` (0o666), got `420` (0o644) in the Codespace. The run was then interrupted (`KeyboardInterrupt`), ending at 1 failed, 141 passed. A venue property changed the result |

### D8. A Plan that could not be executed as written by a manual operator

| Plan requirement | Executed evidence |
| --- | --- |
| Every primary log written by `record_check` with a `pf27.step_log_header.v2` header, plus a manifest | No log has a header; no `qa_step_logs_manifest.json` exists; T03's log carries VS Code shell-integration trace lines |
| T06: two match runs, a deliberate mismatch run, before/after tree digests | One match run and pytest group C only |
| T07: four refusals | Two recorded (open-pin and unavailable). Empty and invalid selection absent |
| T10: 26 probes with JSON capture and an evaluator | Two version probes. The first returned `000` (server not yet ready), the second `200`; recorded `RC=0` |
| T01 command 1 expects exit 1 (QA root absent) | Recorded `rc=0`. The log does not show whether the root existed or the status capture was wrong |

These are execution deviations, not plan defects in themselves. But their pattern matches the Plan's weight: embedded `python -c` recorders, evaluators and multi-file captures for a person running commands by hand. I judged the Plan "executable" by reading it, never by walking an operator through one check.

## 3. Why my review failed

| # | Cause | What I did | What the review needed |
| --- | --- | --- | --- |
| R1 | I verified outputs, not postures | My review §3 table checked 12 expectations against the code, for example that command 1 returns `RAILS_CLOSED_REQUIRED`. It does, so I passed it | Validate every rails state against PF19 §2.3 before checking any output |
| R2 | I reviewed my own premise | Guide §4.3 (live DB under closed rails) and §5 (default closed rails, set by me) are the foundation of ENV-C and ENV-D. I approved a Plan built on my own unverified assumption | Treat my own prior artifacts as inputs to challenge, and re-derive rails from canon |
| R3 | I accepted an implementation gap as a planning fact | I wrote "closed rails do not gate DB access (Audit QA50-F03, confirmed…)" as a reason the environment classes were *sound*, and repeated it to you as the reason for unsetting variables | Raise it as a rails-semantics conflict. A live production connection under `ALLOW_NETWORK=0` is invalid whatever the code allows |
| R4 | I treated rails as environment plumbing, not an operating posture you decide | When you said rails disposition was the most important determiner, I regrouped the checks and wrote per-command prefixes. That made the defect more concrete, and QA-90 copied it | Recognise that rails are a per-epic, PO-owned posture (PF19 §2.3) with two states, changed only at check boundaries (PF27) |
| R5 | No rails validity criteria in my QA-70 method | I marked "Environments: Sound" on internal consistency alone (DSN unset, so no DB) | Explicit criteria: only the two canon states; changes only between checks; production-touching steps open; acceptance posture from the PO; closed-rails skips of open-rails coverage declared |
| R6 | Executability judged on paper | I read the checks and judged them executable | Walk one check through as the actual operator would, in the actual venue |
| R7 | I did not open the sources the Plan cited for its exception | The Plan cited "PF27 'Rails posture'" for the in-check change. I did not read that section, which permits only per-check changes | Verify every canon citation that authorizes an exception |

## 4. Impact

- **Evidence not valid for acceptance:** the evidence committed in `06b04a9` is not valid acceptance evidence for the checks the defects touch. That covers T07 command 1 (meaningless posture), T08 (open-rails coverage silently skipped) and the planned design of checks 10–14, plus the recording and completeness gaps across T01–T10.
- **Defect propagated:** it spread from the Guide into the Plan, the approval, the QA-90 task collection (N-01, `[C7]`) and a QA-100 run, in that order.
- **Your time:** you spent effort on an unset scheme that the execution venue did not need, and on rails questions the Plan should have put to you before planning.

## 5. Corrective actions (identified, not executed in this RCA)

| Action | Owner | Route |
| --- | --- | --- |
| Obtain the epic's acceptance rails posture from you (PF19 §2.3) before any revision | Isis → you | Decision below |
| QA_PLAN_REVIEW v1.1: `DENY` with redlines for D1–D8, replacing the rejected v1.0 | Isis | QA-70, then QA-80 to Kronos |
| Remove the per-command rails prefixes of my RCA brief v1.0 §5 and QA-90 N-01/`[C7]`; one posture per check, set once for the shell | Kronos, in the revised Plan and tasks | QA-80, QA-90 |
| Decide the disposition of the T01–T10 attempts in `06b04a9` (evidence, attempt lineage, rerun eligibility) | Kronos | QA-110 after the Plan is revised |
| Record QA50-F03 (database not gated by rails) as a rails-semantics finding for its owner, not a planning convenience | Isis | Triage carry to the whole-change IA; possible Canon or code question |
| Add rails-validity and operator walk-through criteria to my own QA-70 reviews | Isis | Adopted now |

## 6. Limits of this RCA

- The QA-100 logs are headerless, so exit codes come from the operator's `RC=` lines, not the harness.
- Why T07 was rerun, why T03 was interrupted, and whether the QA root pre-existed at T01 are not established from the stored evidence.
- No test, tool or network call was run for this RCA.
