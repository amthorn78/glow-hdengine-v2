# HDE-EPIC040-PR05 — Conditional PR-40 Handoff v1.2

Issued by the dedicated PR-35 session together with PR-35 result v1.3 (`MERGE_PENDING`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.3.md`).
- It supersedes handoff v1.1, which is void because it names result v1.2; handoff v1.0 was already void. Both are unchanged as issued.
- It is usable only after Nathan / Product Owner's actual manual merge of PR #492, and only where no `MERGE_OBSERVED` result was returned for that merge.
- The PR-35 return carries this block with one line added: the final head read back after the push.
- It neither creates nor dispatches a session.

```text
NEXT_PROMPT_HANDOFF

Run PR-40 — Review PR Work-Unit Lineage — 091426.1:
https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204

Use this block only after Nathan / Product Owner has actually merged PR #492 by hand, and only if no MERGE_OBSERVED result was returned for that merge.

Continue as the retained whole-change HDE-EPIC040 Implementation Architect, in its established read-only PR lineage-review role, as HDE-EPIC040-PR05-PR-INSTRUCTION v1.0 §14 designates. Do not repurpose the PR05 PR-20, PR-30 or PR-35 sessions, or Isis-50. This handoff neither creates nor dispatches a session.

EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: the retained whole-change HDE-EPIC040 Implementation Architect session, in its established read-only lineage-review role (no platform ID invented)
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR05 / PR-40
context_conflict: NONE
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR05
engineering_state: MERGE_PENDING
PR05_lineage_review: NOT_EXECUTED
manual_merge_at_handoff: NOT_EXECUTED
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect

Read the complete package by repository path on main after the merge. Every file is under docs/ephemeral/ unless stated otherwise, and none was edited after issue:

- PR_INSTRUCTION: docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md. HDE-EPIC040-PR05-PR-INSTRUCTION v1.0, INSTRUCTION_READY. SHA-256 adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7
- PR_IMPLEMENTATION_PLAN: docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-plan-v1.0.md. HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN v1.0; the original PR-30 Proceed covers it together with the instruction. SHA-256 d50a6f1f8215124ee04fbce00538480352cf2513159b8df5030956b565675709
- PR_IMPLEMENTATION_RESULT (PR-35): docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.3.md. v1.3, MERGE_PENDING. SHA-256 1fb7cac9ee65e5fd4f403637c22b4b0722311b510d2974b2e5c9f0ad7ffb0e7f
- Superseded, kept as lineage, all unchanged as issued:
  - results v1.1 and v1.2 (docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.1.md and -v1.2.md), whose MERGE_PENDING no longer stands because Codex findings arrived on their records heads (CR-17; CR-18 and CR-19);
  - handoffs v1.0 and v1.1 (docs/ephemeral/HDE-EPIC040-PR05-conditional-PR40-handoff-v1.0.md and -v1.1.md), which are void.
- PR_IMPLEMENTATION_RESULT (PR-30): docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md. v1.0, PR_CANDIDATE_PUBLISHED. SHA-256 2eae5c052623abb885edbfeac1d7dc08fce7324dc328aac7f1ff78c78da8b128
- PR_REMOTE_ACTION_LEDGER: docs/ephemeral/HDE-EPIC040-PR05-pr-remote-action-ledger-v1.12.md (L-01 to L-195; v1.0 to v1.11 unchanged). SHA-256 744834f975c6abe540a7bbd610b7086302dbb86e344713ecfb36ac30a447407f
- Checkpoints: docs/ephemeral/HDE-EPIC040-PR05-pr30-checkpoint-v1.0.md, and docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md through v1.11. v1.11 is the final one: SHA-256 5367e6c1fac84121e8f48ccc86933e50fad4c0552c301daf21e7e7232ddcb24b
- Specification v1.1, SPECIFICATION_APPROVED: docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md. SHA-256 43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df
- Implementation Audit v2.0, AUDIT_COMPLETE: docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md. SHA-256 9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b
- Immutable whole-change Implementation Plan v2.1: docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md. SHA-256 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be
- Plan Review v2.1, Isis-50 APPROVE: docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md. SHA-256 47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3
- Approved F01 overlay, drained as PF10 §2.15:
  - docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md. SHA-256 7700796fedcbd5847146f8e47c611aec662f67ec9ae99e4e8ed97279edbf5b20
  - docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md. SHA-256 86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1
- Accepted predecessors (lineage reviews):
  - PR01 v1.1: docs/ephemeral/HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md. SHA-256 f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273
  - PR02 v1.0: docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md. SHA-256 4b8d638c3f0e9232c8c2143fbce9593296f89c5dcc3d6b6da82293f21d5ab5c3
  - PR03 v1.0: docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md. SHA-256 07647f68bb5f5a705d8d2196f2aaaca9c17cb2b1c9f8774f8fd2b8268ae7dffa
  - PR04 v1.0: docs/ephemeral/HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md. SHA-256 08bff31889c9c76b65cf788826f2a602a388e64c4247eaef7e5ca89df086dba4
- Current controlled PF10, read-only: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md. SHA-256 d79e41102a88ded2cf9823787925c0ac243622cf2a3e59a3e5c1da28387e6f91

Repository and the complete ordered PR lineage:

- Repository: amthorn78/glow-hdengine-v2. Target: main.
- Base: main 25b2c87baa9298956e4cb62f53b9e2acfa95fc1a, unchanged from PR-30 to the final records.
- PR_REFS, the sole PR of this work unit: https://github.com/amthorn78/glow-hdengine-v2/pull/492
- Branch: claude/beautiful-ritchie-6uvevf
- Ordered commits:
  - PR-30: 96b54dd870c6abe855af55140e13094ef896bbb6, 229d1f7bab7c70f16022c190da77f6622899d702.
  - PR-35, round by round (corrective, then records):
    - 1: 2dad33c889260ab13f1de8aa8e0f81c972e1b067, d677f5d6fd8885267c5cff4fad3949591de3e68f
    - 2: ab5e6e7e23787bff59138468d989dadfd89ee40e, fe5f35c5bfd4b269ae788a69c568355e8f315177
    - 3: 88016e4812515363903c608a08c8773bbdd3a9b1, 9d9558d62d190aad27f5eb818afba4050ab52467
    - 4: 145d8a1f02b2d2bbfd7b1282a070e299d391d46a, 4c178efc6ab8aa39c5011c306a13f440ff2d81e3
    - 5: 26b760a8728137380acd456596bf29419e1ff3ea, 78b84f989a9bb98d932e31c6e9e2a45d651d329e
    - 6: daa2110af8f1ff46b667fff399ed1c49bd10071a, 8f5921ca0367a9d1620e48865a6802f6af600584
    - 7: af3bc83d9fd515afa18a86f0dfd334ad98eb76dc, 8d92ec9bbc1a79526338cfc2cac213195cfb2b98
    - 8: 130f78c6513c8df6cdb11a48ed2ef909a5197000, 98f75d6ef711df8d597e3129c7e85da373da01e9
    - 9: 511827f7dbdea2ad86bc325b3b09f1d1fec61e48, dcb2716ed6007bf23d86a157345b540cbc6b9f61
  - Final records of result v1.1: 0e3a9c1818b83c4112614a200d2fae397e5ef212.
  - PR-35 round 10: d47a7cbed7ef70b2a0ce342c96ed4ed8521e42e4 (corrective), e4e9d38deb4d37208d5ac79b4bf2bd0a0c9ccfc9 (records of result v1.2).
  - PR-35 round 11: 2842282e82b8e3bea5631b32ebfb2088e2cd91e4 (corrective), then the records commit that adds this handoff. The PR #492 body and the PR-35 return record that commit's SHA as read back after the push.
- Final code commit: 2842282e82b8e3bea5631b32ebfb2088e2cd91e4 (tree c5eae5c7c32fa7adf0313cb68d1dec4d8292dcf8). The records commit above it changes only docs/ephemeral/.
- Scope against main: 42 changed paths.
  - 9 code, test or documentation paths: ci/checks/classify_ci_changes.py, docs/config_and_bundles.md, tests/bodygraph/test_check_magic10_gate_readiness.py, tests/config/helpers.py, tests/config/test_config_artifacts.py, tests/fixtures/magic10/v1/goldens.json, tools/bodygraph/check_magic10_gate_readiness.py, tools/config/artifacts.py and tools/config/generate_config_artifacts.py.
  - 33 records under docs/ephemeral/.
  - No change to engine/**, catalog/**, schemas/**, migrations/**, adapter/**, presenter/**, goldens/**, .github/workflows/ci.yml, ci/jobs/**, tools/evidence/** or docs/pfcanon/**, and no governed evidence written.

Engineering evidence and decisions (result v1.3 §§4–11):

- Review findings. Eleven corrective rounds dispositioned twenty-five findings: CR-01 to CR-19 from Codex, and SR-01 to SR-06 from PR-35's own review.
  - Twenty-four were fixed in scope. Each fix has tests that fail on the head before it and pass after it.
  - CR-06 (P1: the golden runners execute the executing installation's application modules) was routed to the admission owner and PR06 as observation O-17. Its thread, PRRT_kwDOP103ks6l0Pn2, is left open by design.
  - No rescope was raised. Fifteen in-flight decisions, IF-02 to IF-16, are recorded (result v1.3 §5).
- Local validation at 2842282, under closed rails, with the CI install:
  - Owner modules 201. Focused and guard suites 1,203. Changed-test isolation 2,499.
  - Lanes: product 20; compat 101 (+3 skipped, 2 xfailed); db 249; rails 133; evidence 111; qa 488; release 63.
  - Roster 2,063 passed, 3 skipped. The base-vs-head sweep of the 129 uncovered test files is identical, with zero regressions.
- Hosted CI passed on three earlier heads: dcb2716 and 0e3a9c1 (both with the code of 511827f), and e4e9d38 (with the code of d47a7cb). The runs were 36091521703 (#3625), 36092693372 (#3626) and 36095483387 (#3627).
  - All seven lanes succeeded.
  - The rails and release lanes ended in the accepted RAILS_LANE:RELEASE_NOT_ADMITTED and RELEASE_LANE:RELEASE_NOT_ADMITTED outcomes.
  - Each run ended with CI_APPLICABILITY_AND_EXACT_HEAD_OK.
  - https://github.com/amthorn78/glow-hdengine-v2/actions/runs/36095483387
- Codex Code Review: automatic, and clean on dcb2716. Its review of 0e3a9c1 raised CR-17, fixed in d47a7cb. Its review of e4e9d38 raised CR-18 and CR-19, fixed in 2842282. Of nineteen threads, eighteen are resolved (CR-18's and CR-19's after the push, as the PR-35 return confirms), and CR-06's is open by design. On the pushed round-11 head, CI and the Code Review are verified after the push, and the PR #492 body and the PR-35 return record them.
- Stated limitation L-10: no current-head security review.
  - Codex's Security Review ran only on 96b54dd, the PR-open head, and found nothing.
  - The one @codex security review request (comment 5826076458) was routed to the Code Review track, and the connector reports mergeGateEnabled false.
  - Whether to merge without a current-head security review is the Product Owner's call.
- F01 posture (PF10 §2.15).
  - The rails and release lanes end RELEASE_NOT_ADMITTED.
  - The comparator refuses the repository root with CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER until PR06. Its success is proven only against the labeled synthetic fixture root.
  - No synthetic release was fed to a governed gate or to the attestation. There is no PR06R_B_FINAL_PASS, and neither tool exits 3.
- The readiness tool was exercised only against fake current-view rows and a missing DATABASE_URL. No live readiness observation exists.

Carry C040-01 through C040-06 unchanged (plan §13.1, result v1.3 §12). The PF01 §4.5 versus PF05 §5.2.3 token-naming tension remains plan observation O-01 / PR04 result O-16. Observations O-13 to O-23 (result v1.3 §11) and O-09 to O-12 (result v1.0) stay with their named owners; O-17 is CR-06.

Manual prerequisite and required action:

After Nathan's actual manual merge, verify the merge and the landed commit and tree through authorized repository evidence. Do not infer the merge from this handoff, from green CI or from MERGE_PENDING.

Review the complete PR05 work unit against its immutable bases and the approved F01 overlay. Cover:
- requirement coverage: K040-REQ-010 and K040-REQ-011 principal, and portions of K040-REQ-001, -008, -012 and -013 (AC040-06 to AC040-09);
- interfaces and tests;
- evidence ownership;
- the corrected-source review and the actual CI;
- attribution;
- limitations L-01 to L-12.

Distinguish landed PR05 work from later repository divergence, and preserve result v1.3 as a truthful pre-merge checkpoint.

Remain read-only. Do not:
- implement, merge, enable auto-merge, rewrite a Plan or edit PF10 or Canon;
- create another branch, PR or Proceed;
- enter PR06, PR07 or OPS01, or operate QA, Ops or deployment;
- contact live vendors or databases;
- materialize or promote a release, or close the Epic.

Non-gating prompt-use repository persistence stays with its authorized writer.

Expected output:

Save and read back exactly one complete PR_WORK_UNIT_LINEAGE_REVIEW under docs/ephemeral/, landed by pull request. Its decision is ACCEPT, REJECT or PENDING, and it records:
- exact merge and commit attribution;
- full requirement coverage;
- the actual review and CI evidence, including limitation L-10;
- conflict-register lineage;
- findings, limitations and the native return.

ACCEPT returns the result to the same whole-change IA for its current Plan progression. A precise defect or missing fact follows PR-40's native bounded owner route. Do not create another acceptance receipt, and do not claim independent QA or Ops, release activation or Epic closure.
```
