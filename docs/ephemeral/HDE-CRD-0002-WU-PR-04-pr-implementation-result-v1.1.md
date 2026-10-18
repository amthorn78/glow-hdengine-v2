---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-04-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.1.md
artifact_version: "1.1"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review resolution and merge readiness), plan cycle 1; this record is the checkpoint for PR-35's first corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; 47,967 bytes; sha256 c78b62f79e83d279c77b49c24811d4855fed868884898fc3137ef7cc57d1221e; read in full). Preserved unchanged; this v1.1 is its PR-35 successor in the same lineage
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-04
work_unit_title: "Provider gate and Aux preview (PR; Fermentation; S08, S14)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md (v1.0; Proceeded); companion docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; not edited)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.3, 2.5, 2.6, 2.7 and 2.8 as plan v1.0 applies them (unchanged)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md (v13.5.9; the only PF10 file under docs/pfcanon/ on origin/main 6b5b3f3; blob a125fd4eefbfd70715bd131e763f130fc1fe7cd9; 135,146 bytes; 975 lines; sha256 361274ddcb0e04e1d8986e2bfff4529912b5bba06a9c57820b8bc12a1adbff1e; docs/pfcanon/ last changed by b9edb0c; resolved afresh and read in full by this session, front matter §§1–9, index and addenda 2.1 to 2.8 to <eof>). Provenance, not a gate
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md §2.3 (review chain), §2.5, §2.6, §2.7, §2.8 (carried items), §2.1 (TypeSafe reading, at the final record)
pf10_addendum_created: none (PR-35 is not a qualifying approval prompt)
proceed: the original Product Owner Proceed recorded in result v1.0 (Nathan's PR-30 invocation naming plan v1.0). PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: the dedicated HDE-CRD-0002 WU-PR-04 PR-35 session, https://claude.ai/code/session_01L3975UmX1MJFVcHhQqKv5F; session_disposition NEW_DEDICATED (top-level session Nathan created from PR-30's handoff)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full at entry); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container; a fresh clone, not PR-30's container)
vehicle: branch claude/dreamy-hawking-yz6hnr; pull request amthorn78/glow-hdengine-v2#651 (open, not draft, base main 6b5b3f30c008c4c95b575ac508a9e594894eb9bc)
pr_subscription: active (subscribe_pr_activity confirmed delivery of #651 events to this session at entry)
entry_head: c6df96f3b2e9c06ecc882b1b500dae6221ecfe84 (PR-30 result commit; parents 2336a0c convergence, a00cb8b source)
correction_commit: 90ec0ca30614f82c08235beb2f328cbba848c674 ("HDE-CRD-0002 WU-PR-04: persist the audit sink's directory entries before vendor I/O"; parent c6df96f; tree 1e96c20dbdd27410d7558ede906b4ccb622576bf, the tree every §5 check ran on)
checkpoint_commit: the commit that adds this file, on top of 90ec0ca; it changes only docs/ephemeral/; its own identity is not written into itself
release_id: 2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76 (1.3.0, 45 members; unchanged by this phase)
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.2.md (PR-35, written after the remote evidence of §7 arrives)
created_at: 2026-10-18T13:33Z
---

# HDE-CRD-0002 WU-PR-04 — PR Implementation Result v1.1 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex code review of [amthorn78/glow-hdengine-v2#651](https://github.com/amthorn78/glow-hdengine-v2/pull/651) raised one P1 finding, CX-1, on the audit sink's durability. CX-1 is corrected by `90ec0ca` and verified locally (§4, §5). This record rides the same push. The Codex re-review of the corrected head, its hosted CI, the thread resolution and the readiness decision follow in v1.2.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Entry recovery

| Check | Observation |
| :- | :- |
| Pull request | #651 open, not draft, not merged; head `claude/dreamy-hawking-yz6hnr` at `c6df96f`; base `main` at `6b5b3f3` = `origin/main`; 3 commits (`a00cb8b`, `2336a0c`, `c6df96f`); 66 files (+1,738/−124); `mergeable_state: unstable` at entry (checks running) |
| Local and remote | Fresh clone; one worktree, on the session's default branch `claude/exciting-fermi-xlgs46` at `6b5b3f3` (no commits of its own; absent on the remote). The PR branch existed only on the remote; a tracking branch was created from it at `c6df96f`, clean |
| Artifact lineage | result v1.0 (PR-30) on the branch, read in full; plan v1.0 (§§1–22 headings; §§6.7, 11–14, 19–21 read in full), instruction v1.0 and the Specification on `main`; no PR-35 record for WU-PR-04 existed |
| Tree identity | `git diff --name-only 2336a0c c6df96f` is result v1.0 only: the entry head's code tree is the one PR-30 validated |
| Earlier cycles | none: this is plan cycle 1 of WU-PR-04 |
| Subscription | active at entry for #651 |
| Repository skills | `.claude/skills/steward/` and `.claude/skills/babysit/` are absent on the head branch |

## 3. Review matrix

| ID | Reviewer, location, head | Finding | Classification | Disposition | Evidence |
| :- | :- | :- | :- | :- | :- |
| — | Codex code review, `2336a0c`, trigger "PR opened" | none: the review **failed** at 12:56:53Z; Codex posted "You have reached your Codex usage limits for code reviews" (comment 6250183766) | evidence unavailable | Product Owner decision PO-1 (§6): request a review | summary comment 6250183424 |
| CX-1 | Codex code review 5563130407 (`COMMENTED`, 13:12:55Z), thread `PRRT_kwDOP103ks6tqvyR` (r4307154022), `engine/bodygraph/vendor_audit.py` line 174, head `c6df96f`, trigger "Manual request" | P1 "Persist the audit directory entry before vendor I/O": `os.fsync(fd)` makes the file's bytes durable but not the directory entries that `mkdir` and `O_CREAT` create. On the first audited invocation, or after the sink is recreated, the vendor call follows at once, so a crash can leave no pre-I/O event although HTTP occurred, against HDE-CLI-API-Vendor-Ref §7.1.11f | substantive, in scope (S14; instruction ID-6 and §7.1.11f "locally durable … before I/O"; plan §6.7 "Writing") | corrected by `90ec0ca` (§4); reproduced by the negative control (§5); thread answered before the push, resolved after the re-review | §4, §5 |
| — | Codex security review | not applicable | deprecated (PF10 addendum 2.3 Rule 2) | not obtained or waited on; not a gap | PF10 HDE Build Notes 2.3 |
| — | Human reviewers | none requested or present | — | — | formal reviews: only Codex's |

**Path traced for CX-1.** Production-like `bg:resolve --source vendor --allow-prod-vendor <REF>` with the default sink and no existing state directory → step 6: `mkdir` creates `~/.local/state/glow-hdengine`, `os.open(O_CREAT)` creates the file, the line is written and the file is fsynced → step 7 builds the client and performs the HTTP read. On Linux, `fsync(2)` on a file does not ensure that its entry in the containing directory has reached disk (the manual names an explicit `fsync` on the directory's descriptor). A power loss between step 7's request and a later writeback leaves a directory without the file, or without the new directory: the pre-I/O event that §7.1.11f requires to be "locally durable" before I/O is lost although the vendor was contacted. The path is real for every first invocation on a host and after any rotation or removal of the sink. The fix is about 25 lines in one non-member module.

No finding raised a boundary (plan RK-7): the correction stays inside plan §6.7's module and its owner test, changes no member, no governed artifact, no interface field and no refusal code.

## 4. Correction CX-1 (`90ec0ca`)

| Path | Change |
| :- | :- |
| `engine/bodygraph/vendor_audit.py` (not a release member) | `append_event` records, before `mkdir`, every missing directory from the sink's parent up to the first existing ancestor. After the file is written and fsynced, it fsyncs the directory holding the file and the parent of every directory it created, deepest first, through a new private `_fsync_directory` (`os.open(O_RDONLY \| O_DIRECTORY \| O_CLOEXEC)`, `os.fsync`, close). Any `OSError` is `AuditUnavailable`, so step 6 refuses `PROVIDER_AUDIT_UNAVAILABLE` and step 7 does not start (§7.1.11f: "Failure to persist the pre-I/O event is `PROVIDER_AUDIT_UNAVAILABLE` and blocks the call"). The docstring names the new guarantee; one comment cites §7.1.11f |
| `tests/bodygraph/test_vendor_prod_override.py` (owner test, 96 → 99 cases) | `test_append_persists_the_line_and_every_new_directory_entry`: on a new sink two levels below an existing directory, the fsync sequence is exactly the file, its directory, the created parent, then the existing ancestor; on the second append it is the file and its directory only (identities by `st_dev`, `st_ino`). `test_directory_fsync_failure_is_unavailable`: a directory fsync failure raises `AuditUnavailable`. `test_o6_unpersisted_directory_entry_blocks_step_seven`: with the real `append_event` and a failing directory fsync, a valid production override refuses `PROVIDER_AUDIT_UNAVAILABLE` with `outbound_attempted: false` under the I/O guards (no client, DNS, socket or database) |

Unchanged: every refusal code and message, the 16-field record and its bytes, the sink path rule, the file's `0600` and the created parent's `0700` modes, the event order and outcomes, the state events' best-effort rule (an `AuditUnavailable` from them still changes nothing), the release roster and every governed artifact. The flag-absent event and the post-step-7 state event use the same `append_event`, so they gain the same durability; their failure rule is unchanged.

**Restart rules (result v1.0 §15).** `engine/bodygraph/vendor_audit.py` is not one of the 45 members (`catalog/manifest.json` and `engine/config/registry_loader.py` do not name it) and no governed artifact binds its bytes (`git grep vendor_audit -- artifacts audit docs/evidence schemas`: no hit; its only non-engine references are the classifier's owner key and the mapped-cache evidence generator's actor seam). No member and no evidence primary changed, so neither restart point (step 2 or step 3b) applies; the `--check` forms and the attestation below show the converged state is still current.

## 5. Local validation of `90ec0ca`

Environment: CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`), `python -m pytest --version` → pytest 8.4.2; `ruby` 3.3.6 at `/usr/local/bin/ruby`, `bash`, `curl`. Closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; unset by name `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `ENGINE_ENV`. Every run that can write tracked files ran in a detached worktree of `90ec0ca` with `PYTHONPATH` set to it, and ended with `git diff --exit-code` 0 and an empty `git status --short --untracked-files=all`.

| # | Check | Result |
| :- | :- | :- |
| 1 | Entry confirmation on `c6df96f`: the six files of result v1.0 §10 #10 (four changed test files, the mapped-cache file, `tests/evidence/test_v2_mapped_cache_evidence.py`) | 212 passed, exit 0; clean tree |
| 2 | `tests/bodygraph/test_vendor_prod_override.py` with the correction | 99 passed, exit 0 |
| 3 | Negative control: the same file with `engine/bodygraph/vendor_audit.py` at `c6df96f` (correction removed; restored afterwards, diff verified) | 3 failed (the three new cases), 96 passed, exit 1 |
| 4 | Read-only checks: `scripts/release_id_recompute.py --check-manifest-only`; `tools/evidence/update_evidence_index.py --check`; `tools/evidence/orientation_demo.py --check`; `tools/evidence/validate_evidence_paths.py`; `tools/evidence/generate_v2_mapped_cache_evidence.py --check` (`V2_MAPPED_CACHE_EVIDENCE_OK`; its production scenario writes the real sink in a temporary directory); `tools/evidence/generate_bodygraph_policy_proofs.py --check`; `tools/evidence/run_canonical_json_gate.py --check-only`; `tools/evidence/check_lf_endings.py`; `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `ci/checks/check_final_lf.sh`, `ci/checks/check_cli_help.sh` (each invoked by path, plan F-2) | 12 of 12 exit 0; clean tree |
| 5 | Attestation: `tools/evidence/build_release_attestation.py --output <external empty directory> --require-clean`, then `--verify` (13:16:47Z to 13:18:33Z) | build exit 0; verify exit 0; `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `release_id` and `manifest_sha256` `2f18a5ebbf19…`, `source_commit` `90ec0ca30614…`, `source_commit_exact` true; clean tree |
| 6 | Classifier, base `6b5b3f3` → head `90ec0ca`, event `pull_request` | `reason=selected_lanes`; 66 paths; all seven lanes; `needs_python=true`, `changed_tests=true`; 166 changed-test targets, `tests/bodygraph/test_vendor_prod_override.py` among them |
| 7 | Full `tests/` sweep (`python -m pytest -q -p no:cacheprovider tests/`; `ruby`, `bash`, `curl` on `PATH`) | **4,918 passed, 3 skipped, 2 xfailed, 0 failed** (1,007.2 s; 13:16:17Z to 13:33:05Z), exit 0, then `git diff --exit-code` 0 and an empty status. Result v1.0's 4,915 plus the three new cases, with the same skips and xfails; the 5 warnings are the pre-existing `datetime.utcnow()` deprecation in `engine/ops/http_log.py` |

A full sweep started on `c6df96f` at entry was stopped at about 35% (no failure up to then) when CX-1 made that head stale; it is not evidence.

## 6. Product Owner decisions and in-flight decisions

**Product Owner decision in this phase.**

| ID | Question | Decision | Effect |
| :- | :- | :- | :- |
| PO-1 (2026-10-18, about 13:09Z) | The Codex code review of #651 failed on its usage limit; PF10 addendum 2.3 Rule 3 keeps the Codex code review in the chain. Request a review, waive it for #651, or pause | "Request review" | one `@codex review` comment (6250299904, 13:09:10Z); the review ran on `c6df96f` (§3) |

**In-flight decisions** (taken without a rescope):

| ID | What changed | Why it was necessary to deliver the approved scope | Tested by (outcome) |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits are pushed to the pull request's branch `claude/dreamy-hawking-yz6hnr`, not to the session's default branch `claude/exciting-fermi-xlgs46` | The handoff continues #651; the work unit keeps one branch and one pull request (GCF-17 continuity). Same decision as WU-PR-03 result v2.1 IF-35-1 | remote head read back after the push (§7) |
| IF-35-2 | `append_event` also fsyncs the directory holding the sink and the parent of every directory it creates (§4). Plan §6.7 "Writing" listed only the file's `os.fsync` | §7.1.11f requires the pre-I/O event to be "locally durable" before I/O, and the instruction's ID-6 requires it durable before step 7; the file fsync alone does not persist a new entry (CX-1). Fail-closed, inside the plan's module, no interface change | §5 #2, #3 (the three new cases fail without it), #4, #5, #7 |
| IF-35-3 | The hosted run 39129482681 on `c6df96f`, already in its evidence lane when CX-1 arrived, was left to finish rather than cancelled; it is recorded as stale and is not a gate | Its remaining lanes covered the 54 evidence paths and the attestation, which the correction does not touch, so its result could reveal a hosted-only failure to fold into the same corrective push. It ended `success` (12:57:51Z to 13:18:03Z) | §7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.0 §14)

| Time (UTC, 2026-10-18) | Action | Fact |
| :- | :- | :- |
| 12:56:53 | Codex code review on `2336a0c` (trigger "PR opened") | failed: usage limit (comment 6250183766) |
| 12:56:53–12:58:09 | CI run 39129417131 on `2336a0c` | cancelled by pull-request concurrency when `c6df96f` was pushed (result v1.0 D-3); not a gate |
| entry (about 13:00) | `subscribe_pr_activity` #651 | confirmed |
| entry | Reads: PR, commits, formal reviews (0), review threads (0), issue comments (2), check runs, workflow runs | §2, §3 |
| 13:09:10 | Comment `@codex review` on #651 (6250299904), on PO-1 | Codex reacted 👀; review running from 13:09:24Z |
| 13:12:53 | Codex code review on `c6df96f` (trigger "Manual request") | completed; one P1 finding, CX-1 (review 5563130407; thread `PRRT_kwDOP103ks6tqvyR`); summary `has_unresolved_findings: true` |
| 12:57:51–13:18:03 | CI run 39129482681 on `c6df96f` (job 117681580184) | success; stale after CX-1 (IF-35-3); not a gate |
| 13:13–13:15:44 | Local correction and negative control; local commit `90ec0ca` at 13:15:44Z | §4, §5 #2, #3 |
| 13:16–13:33:05 | Validation of `90ec0ca` in two detached worktrees (§5 #4 to #7) | all pass |
| before the push | Reply on `PRRT_kwDOP103ks6tqvyR` naming `90ec0ca` as not yet pushed and what it changes | GitHub |
| this push | `90ec0ca` and this record's commit, one fast-forward push to `claude/dreamy-hawking-yz6hnr` (no force) | read back by `git ls-remote` and a PR read after the push; recorded in v1.2 |
| next | Evidence actions | the Codex re-review of the new head (trigger "New commits", as on earlier HDE-CRD-0002 pull requests), CI on the new head (seven lanes, the changed-test step, the attestation, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), then the thread's resolution; the subscription delivers them |

No `[skip ci]` or other CI suppression was used. No CI run was retriggered or cancelled by this session.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the corrected head; CX-1 thread resolution | this PR-35 session | pending (§7) |
| Hosted CI on the new head: seven lanes, changed-test step, attestation, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; OBS-17 and O-6 if they occur | this PR-35 session | pending |
| Mergeability and readiness (`MERGE_PENDING`) | this PR-35 session | pending; v1.2 |
| Merge | Nathan only | — |
| Lineage review and WU-PR-04 acceptance | the whole-change IA (PR-40) | after the merge |
| Stale documents, OBS-P4-1 to OBS-P4-7, carried items, canon doc-delta candidates | result v1.0 §12 owners | unchanged |
| Persistence of prompt-use provenance (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) | Product Owner | pending, non-gating |

Constraints preserved: closed rails; no live vendor, production or database call; no secret in any log, record or comment; no audit sink in the repository (tests used temporary sinks); no hand edit of a governed artifact; no member change, re-cut or convergence; no skipped, deselected, `xfail`-marked or quarantined test; no canon, Specification, instruction or plan edit; no PF10 addendum.

## Canon relied on

Read on `origin/main` `6b5b3f3` (`docs/pfcanon/` last changed by `b9edb0c`; the branch does not change `docs/pfcanon/`).

| Decision topic | Sources and sections read | Effect |
| :- | :- | :- |
| PF10 authority and resolution | PF10-HDE-Build-Notes v13.5.9 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md`), front matter §§1–9, cross-references, index, addenda 2.1 to 2.8 (read in full to `<eof>`) | the unique unlettered current PF10; addenda applied by scope |
| Review chain; the failed review; no security review | PF10 addendum 2.3, Rules 1 to 5 and "Passages read under this rule" | the Codex code review is required and read; its absence could not be treated as clean, so PO-1 was asked; the security review is not applicable and not a gap |
| CX-1 validity and its fix | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §7.1.11 preamble and §7.1.11a to §7.1.11f (read in full): §7.1.11d step 6 "durably write the pre-I/O audit event", §7.1.11f "one append-only, locally durable, keys-only event before I/O" and "Failure to persist the pre-I/O event is `PROVIDER_AUDIT_UNAVAILABLE` and blocks the call"; instruction v1.0 IF-2 and ID-6 ("durable (append, flush, `fsync`) before step 7 starts"); plan v1.0 §6.7 | CX-1 is substantive and in scope; the fix fails closed with the existing code |
| Restart rules | plan v1.0 §6.13 and §14 (RK-2, RK-7); result v1.0 §15; PF10 addenda 2.6 (step 3b) and 2.7 AD-5 (restart points); `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" | the corrected module is not a member and binds no evidence; no restart |
| Change authority | HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (the PR implementation row: "Normal substantive code/security/review and evidence chain"; merges are Product Owner actions) | correction under the original Proceed; no merge |
| Phase authority, checkpoint and ledger | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (read in full); skill glow-hde-pr-development 1.4.0 | this checkpoint after the corrective push; review before CI; no CI suppression |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; pytest readiness; no hand edits; "Code review guidelines"; "Evidence attribution, currentness and distinct decisions"; truncation guardrail) | §5 profile; tested state `90ec0ca` distinguished from this record's commit |
| Precedent | WU-PR-02 result v1.1 and WU-PR-03 result v2.1 (PR-35 checkpoint and record-head patterns); PF10 addendum 2.5 (Codex re-review trigger "New commits" on #637) | record layout; expected re-review |

## Nonclaims

- Local green is not QA. No QA artifact was created; `audit/qa/hde-crd-0002/` is untouched.
- This checkpoint is not a PR-35 result. It claims no merge readiness, merge, acceptance of WU-PR-04 or HDE-CRD-0002, Ops, deployment, PF09 or PF30 movement, release activation or closure.
- The `--allow-prod-vendor` flag was not exercised live; durability was tested by fsync-order and failure injection, not by a power-loss experiment.
- No canon, Specification, instruction, plan or PF10 edit; no PF10 addendum.
