---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.2.md
artifact_version: "1.2"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review resolution and merge readiness); this record is the checkpoint for PR-35's second corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.1.md (v1.1, PR-35 checkpoint for the first corrective push; blob 8c002e3e20bf05bc09361523f08d7022a2a3c179). Preserved unchanged; v1.0 (PR-30) likewise
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d92f90b3389d56d498f12964a91a9)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5804a88bcf861f45ea24d8846288f)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain), as planned by PR_IMPLEMENTATION_PLAN_ID v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112da05bbcc9fae7316f64d1657824ff; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this PR-35 session; unchanged on main 0cd7b84 and on the branch)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (reviewer chain) and § 2.1 (TypeSafe reading)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-02 PR-35 session, https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK; session_disposition NEW_DEDICATED; role_session_ref NOT_YET_ASSIGNED (Nathan assigns). The session's worker process restarted once between the CX-2/CX-3 reads and the Product Owner decision; the checkout, scratchpad environment and branch were intact and nothing was lost
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/intelligent-cannon-32u7tl; pull request amthorn78/glow-hdengine-v2#634 (open, not draft, base main 0cd7b84)
step_entry_head: b6fe37d4a353c74bdb7783b18f81bec99e89dfe5 (v1.1 checkpoint commit; parent c0ca923)
correction_commit: 489bc17eaeae173c6ee835b1a85e5defb3fadbb1 ("fix(evidence): HDE-CRD-0002 WU-PR-02 — validate the manifest fully before minting a release label (S12)"; parent b6fe37d; tree 44fa30af273fa8ca61da1d17b22b6fe5ec40246c, the exact tree every §5 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.3.md (PR-35, written after the remote evidence below arrives)
created_at: 2026-10-13T19:43:00Z
---

# HDE-CRD-0002 WU-PR-02 — PR implementation result v1.2 (PR-35 checkpoint)

## 1. State

PR-35 checkpoint after the second corrective push. The Codex code review of `b6fe37d` raised two findings. CX-3 (P2) is corrected by `489bc17`, locally validated (§5) and pushed together with this record. CX-2 (P1) is not changed in code: the Product Owner decided to accept its residual and record it for the IA at PR-40 (§3). Hosted CI and the Codex code review on the pushed head are pending and arrive through this session's pull-request subscription. Nothing here merges, claims merge readiness, QA, acceptance or closure.

## 2. Finding identifiers

PR-35 names Codex findings `CX-<n>` in order of appearance. HDE-CRD-0002's canon-conflict register already uses CR-1 to CR-5 (CR-2 is Thoth's), so a `CR-` label for a review finding would collide in PR-40's reading. **v1.1's "CR-1" is CX-1**; v1.1 is preserved unchanged, and this mapping is its only reading correction. The Product Owner directed this relabelling (§3).

## 3. Review matrix

| ID | Reviewer / location / head | Finding | Classification | Disposition | Evidence |
| :- | :- | :- | :- | :- | :- |
| CX-1 | Codex code review 5508104545, thread `PRRT_kwDOP103ks6sAH60`, `tools/evidence/update_evidence_index.py` L3855–3857, `c27c5e8` | P1 "Verify captures before relabeling them as current" | substantive, in scope (v1.1 §3) | corrected by `c0ca923` (v1.1 ID-35-1); thread answered (comment 4262732644) and resolved 2026-10-13 ~18:54Z; GitHub now marks it outdated | v1.1 §4 |
| CX-2 | Codex code review 5508508117, thread `PRRT_kwDOP103ks6sA712` (comment 4262770376), `update_evidence_index.py` L3907–3909, `b6fe37d` | P1 "Require producer proof before advancing capture labels": a byte difference is not proof that the owning producer regenerated the capture; a stale restore, truncation or manual edit after a manifest change would take the new label; "bind the transition to owner-produced release identity or an authenticated publication transaction" | Product Owner decision required: full owner proof needs producer checks or publication transactions across the owner families, outside WU-PR-02's bounded files, and changes the relabel procedure D-1 hands to WU-PR-03/04/05/08 | **Accepted residual, by Product Owner decision** (below). No code change. The thread is answered with the traced path and the decision and resolved after the push (v1.3 records it); the residual is recorded for the IA at PR-40 (§8) | §3.1 |
| CX-3 | Codex code review 5508508117, thread `PRRT_kwDOP103ks6sA719` (comment 4262770388), `update_evidence_index.py` L3827–3831, `b6fe37d` | P2 "Validate the manifest before minting a release label": a canonical manifest with a plausible `version` but bad fields, timestamps or member hashes/sizes would yield a label for an identity the repository's validation rejects | substantive, in scope (S12 label derivation; HDE Schemas & Artifacts §6.2 "Do not compute an identity from a noncanonical or otherwise invalid manifest") | corrected by `489bc17` (§6 ID-35-4); thread answered and resolved after the push | §5 |
| — | Codex review summary (issue comment 6152304678) | Code Review completed 2026-10-13T18:57:17Z on `b6fe37d`, trigger "New commits" | — | read | — |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not requested or waited on | — |

### 3.1 CX-2: Product Owner decision

This session put three options to the Product Owner (2026-10-13, after the CX-2/CX-3 reads): (A) accept the residual and fix CX-3; (B) partial owner proof for the nine captures that embed `release_id`; (C) a rescope to the IA through RS-20. The question form was dismissed; Nathan then directed in this session: **"Choose option A: accept the residual, fix CR-3, answer the thread and record the residual for the IA at PR-40."** ("CR-3" in that sentence is CX-3 under §2.)

Rationale as Nathan gave it, recorded:
- The label is not meant to prove owner regeneration. IF-7 and S12 ask that "a reader of the Mirror can tell a current-release capture from a frozen one without opening the file." `AGENTS.md` says hashes, path proofs and Index/Mirror facts never substitute for the substantive predicate; a reader who treats the label as proof that the producer ran is already breaking that rule.
- Owner proof would contradict the binding contract. The WU-PR-02 instruction §8 D-1 requires that later re-cuts "relabel rows through the updater alone"; owner-certified labels change that procedure for WU-PR-03, WU-PR-04, WU-PR-05 and WU-PR-08, which makes the rescope option a Plan change, not a correction within PR-35.
- Codex's three failure paths are mostly covered elsewhere: a hand edit is already forbidden by `AGENTS.md` (the lines Codex cites); a stale restore that embeds the old `release_id` is caught for at least some families by existing checks (the engine-core payloads must match the admitted `release_id` under S11's test; the identity closure's check graph lists the reader_cli parity files). Nathan did not confirm owner-side checks for every family.

Repository facts this session read for the last point, without extending the claim: `tools/evidence/regenerate_identity_closure.py` `CLOSURE_STEPS` gives a read-only owner `--check` for the canonical-JSON family (4 roster paths), the reader/CLI determinism family (5), the open-rails fixture proof (1) and the A7 transport family (5 of the roster's 23 paths); `tests/evidence/test_engine_core_evidence.py` (S11) binds three of the four engine-core payloads to the admitted `release_id`; `tools/evidence/generate_conjunction_writer_evidence.py` has a `--check` mode not listed in the closure graph; the two catalog logs are written by the config-family publication inside the updater's transaction; the purity report carries no release binding. Whether a stale tracked capture fails the hosted release lane was not verified (the isolated closure repairs derived outputs in its copy before checking).

## 4. Hosted CI read

| Run / job | Head | Result | Status as gate |
| :- | :- | :- | :- |
| 38446041858 / 115465311140 | `4d11089` | success 18:22:50Z–18:34:58Z; EVIDENCE, RELEASE success; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | stale (CX-1) |
| 38450463942 / 115479729750 | `b6fe37d` | success 18:53:53Z–19:06:27Z | stale (CX-3 required a further change) |

## 5. Local validation of `489bc17`

Environment E-CI exactly as v1.1 §4 (CPython 3.12.3, CI's install, setuptools 84.0.0, pytest 8.4.2; closed rails; detached worktree or clean clone; clean tree after each). The E-DEB rehearsal was not rerun: the correction does not touch `build_release_attestation.py` or `regenerate_identity_closure.py`.

Run 2026-10-13T19:26:09Z–19:41:47Z, tested commit `489bc17` (base `0cd7b84`).

| # | Check (plan §11 numbering) | Result |
| :- | :- | :- |
| 1 | `ci/checks/check_env_pins.sh`; `python3 ci/checks/check_agents_md_citations.py` | 0; 0 |
| 3 | Updater write twice in the worktree | 0, 0; `git diff --exit-code` 0, 0 untracked (governed companions byte-unchanged) |
| 4 | `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, `check_lf_endings.py`, `release_id_recompute.py --check-manifest-only` | all 0 |
| 5 | Classifier `--base 0cd7b84… --head 489bc17… --event-name pull_request` | exit 0; `lanes=evidence,release`; `product/compat/db/rails/qa=false`; `changed_tests=true`; `path_count=17`; the same five targets |
| 6 | Changed-test step (detached worktree, `PYTHONPATH` = worktree) | **198 passed**; tree clean |
| 7 | Evidence lane as `ci.yml` runs it | checks 0; **130 passed** (622.2 s; 129 at `c0ca923` + the CX-3 case) |
| 7b | `tests/config/test_config_artifacts.py`, `tests/evidence/test_engine_core_evidence.py` | **165 passed**; tree clean |
| 8 | Release-lane tests (four files) | **75 passed**; tree clean |
| 11 | qa lane, seven files (prudence) | **488 passed**; tree clean |
| 9 | Release-lane build: clean clone at `489bc17`, E-CI, `release_id_recompute.py --check-manifest-only`, build `--require-clean`, `--verify --require-clean` | 0, 0, 0; no `build_backend_compat` line; `attestation.json` 28,163 bytes, SHA-256 `2080f75e76789a0870b28bffc3125de1f13a7de6f910b9da661de26eed68a750`, `source_commit 489bc17…`, `source_commit_exact true`, `pipeline_stop null`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean. The isolated closure ran the updater with the new manifest validation |
| — | Narrow run before commit (label and config-family selection, including the CX-3 case) | 9 passed |

Negative control: `test_release_label_refuses_a_manifest_that_fails_full_validation` against the `b6fe37d` updater (detached worktree, new test file) **fails** (the old updater exits 0 with a drifted member); with the correction it passes.

## 6. In-flight decisions

| ID | Decision | Why necessary to deliver the approved scope | Tested by (identity → outcome) |
| :- | :- | :- | :- |
| ID-35-4 | CX-3 correction: `_current_release_label` first runs the repository's shared full manifest validation, `scripts/release_id_recompute.py` `manifest_only_problems(ROOT/catalog/manifest.json)` (canonical bytes; schema through `load_manifest`; every member's bytes and size), and refuses with the existing `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` before any write, in write and `--check` modes. The existing canonical and version-character checks stay | S12's label names a release_id; HDE Schemas & Artifacts §6.2 forbids computing an identity from an invalid manifest, and `AGENTS.md` names `release_id_recompute.py --check-manifest-only` as the source validation. The function requires closed rails, which the updater already enforces | `test_release_label_refuses_a_manifest_that_fails_full_validation` (pass; fails against `b6fe37d`); the full §5 set |

ID-35-1 to ID-35-3 (v1.1 §5) stand unchanged.

## 7. PR_REMOTE_ACTION_LEDGER (PR-35, continued from v1.1 §6)

| Time (UTC) | Action | Fact |
| :- | :- | :- |
| 18:53:44 | Push 1 | `4d11089..b6fe37d` (`c0ca923` + v1.1), no force; remote head read back `b6fe37d4a353c74bdb7783b18f81bec99e89dfe5` |
| ~18:54 | CX-1 thread | reply 4262732644; thread `PRRT_kwDOP103ks6sAH60` resolved |
| ~18:54 | PR description | updated: PR-35 correction under "What changed", `c0ca923` checks under "Checks run", headings kept |
| 18:54:54 | Safety-net check-in | `send_later` trigger `trig_01CpnpgvUJVYBvVhwSz1KSqQ`, fire 19:45Z |
| 18:57:17–20 | Codex review on `b6fe37d` | review 5508508117: CX-2 (P1), CX-3 (P2); summary completed |
| 18:57–19:20 | Investigation; worker restart; question to the Product Owner | CX-2 options A/B/C; the question form was dismissed and Nathan directed option A in this session (§3.1) |
| ~19:20–19:25 | CX-3 correction and narrow tests | label/config selection 9 passed; negative control failed as intended |
| 19:26:01 | Commit `489bc17` (local) | updater +7/−1, test +13/−0 |
| ~19:27 | Hosted CI read | run 38450463942 on `b6fe37d` success; stale |
| 19:26:09–19:41:47 | Local validation | §5, all 0 / passed |
| after this record's commit | Push 2 | `489bc17` and this record, one push; read back in v1.3 |
| after push | CX-2 and CX-3 thread replies and resolution; PR description update | recorded in v1.3 |

**Remaining useful local action:** none. **Next evidence action:** hosted CI and the Codex code review on the pushed head, received through the subscription; then v1.3.

## 8. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Hosted CI and Codex code review on the pushed head | this PR-35 session |
| **CX-2 residual (accepted by Product Owner decision, §3.1):** a capture changed after a manifest cut by something other than its owner (stale restore, truncation, forbidden hand edit) takes the new label at the next updater run; owner-certified labels would change D-1 for WU-PR-03/04/05/08 | recorded for the IA at PR-40 |
| v1.1 §5 residual (regeneration under the previous release with no updater run before the cut) | recorded for the IA at PR-40 (subsumed by the CX-2 residual) |
| PD-10 superseded by ID-35-2; PD-11 stands | Nathan / IA (PR-40) |
| OBS-W2-1, OBS-W2-2, OBS-W2-3; OBS-17 | plan §17 owners; QA tool and test owner through the IA |
| Prompt-use provenance writer absent | pending, non-gating |

## Canon relied on

Read on `main` at `0cd7b84` (the branch changes no file under `docs/pfcanon/`):
- **Review chain and decision authority:** PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 ("Material rescope boundary"; "Other lawful results"); PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 2 and 3; HDE Governance §9.1.1 (Product Owner authority; PR merges remain Product Owner actions); PR instruction v1.0 §8 D-1 and §14.
- **CX-2 and CX-3:** HDE Schemas & Artifacts §6.2 ("Do not compute an identity from a noncanonical or otherwise invalid manifest"; the identity table's Human Index / Machine Mirror row) and §6.4 (`release_id_recompute.py --check-manifest-only` as the read-only current manifest/member validation); §8.3 "Allowed top-level keys and unknown-key rejection" (`notes` encoding unchanged). In-flight: Implementation Plan v1.1 §5 IF-7, §7 WU-PR-02 acceptance (4), §10.
- **Operative documentation:** `AGENTS.md` (release identity: source validation through `release_id_recompute.py --check-manifest-only`; hashes, path proofs and Index/Mirror facts never substitute for the substantive predicate; no hand edits of governed artifacts; closed rails; evidence attribution).

## Nonclaims

No merge readiness, QA evidence, QA verdict, acceptance, PF09/PF30 movement, deployment, canon change or closure. Local green is not hosted CI; CI green is not QA.
