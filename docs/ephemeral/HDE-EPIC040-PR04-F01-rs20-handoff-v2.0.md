---
artifact_type: RS20_HANDOFF
artifact_id: HDE-EPIC040-PR04-F01-RS20-HANDOFF
artifact_version: "2.0"
predecessor_version: "1.0"
predecessor_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v1.0.md
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
decision: APPROVE
decision_ref: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v2.0
receiver_prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1
receiver_prompt_url: https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204
addendum_created: docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md
pr_return_phase: NOT_APPLICABLE
rs40_eligible: false
created_at_utc: 2026-09-22T07:27:55Z
---

# HDE-EPIC040-PR04-F01 — RS-20 Handoff v2.0

## Outcome

`RS-20` decided **`APPROVE`** on `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1`, and emitted **exactly one** `PF10_BUILD_NOTES_ADDENDUM`.

Redlines R-1 through R-7 are applied exactly once each and were verified against the repository. The R-2 derivation method was tested by execution across all three chains; every failure fell inside the approved enumeration or inside loci PR04 already owns. The approved set is **nine production and CI-configuration files plus four test homes** — one more than the proposal's eight, because `tools/evidence/run_canonical_json_gate.py` is admitted.

## Repository references

| Artifact | Repository path in `amthorn78/glow-hdengine-v2` |
| --- | --- |
| Decision | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` |
| **PF10 addendum overlay** | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-checkpoint-v2.0.md` |
| This handoff | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v2.0.md` |
| Approved proposal v1.1 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md` (merged in PR #463) |
| RS-30 application report | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs30-redline-application-report-v1.0.md` (merged in PR #463) |
| Prior decision v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` (merged in PR #462) |
| Proposal v1.0, preserved | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` (merged in PR #457) |
| PR04 instruction v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md` (merged in PR #452) |
| PR04 implementation plan v1.0 `DRAFT` | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md` (merged in PR #453) |
| Immutable base Plan v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` |
| Approving Plan Review v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| Current controlled PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md` (read-only) |

Storage pull request for this stage's four artifacts: **PR #465**, branch `claude/nice-mayer-tf9l4c`. **Nathan alone merges.**

## What Nathan does next

Paste the block below into the **dedicated PR04 development session `PR04-HDE-EPIC040-1`**. It is complete and requires no editing.

Separately, and not part of that block: the review records a candidate finding, `HDE-EPIC040-PR04-F02`, for the same session to raise through `RS-10` in the ordinary way. It is independent of this overlay and does not gate it.

```text
NEXT_PROMPT_HANDOFF

Run PR-20 — Create Detailed PR Implementation Plan — 091426.1
https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204

=== RECEIVING ROLE AND SESSION ===
Actor: the dedicated HDE-EPIC040-PR04 development session PR04-HDE-EPIC040-1 — the same session
that produced PR04 detailed Implementation Plan v1.0 and raised finding HDE-EPIC040-PR04-F01 at its
§14.1. session_disposition: RETAIN_EXISTING. role_session_ref: that same dedicated PR04 session; the
operator selects it. Do not create, restart or replace a session and do not invent a platform
session ID. The retained whole-change HDE-EPIC040 Implementation Architect session and the Isis-50
reviewer session are separate and are not addressed here. No new approval owner is created.
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / PR-20, successor plan after an approved
bounded rescope. context_conflict: NONE established. EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION.
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS.

=== CHANGE, WORK UNIT AND STATE ===
CHANGE_CLASS: EPIC. CHANGE_ID: HDE-EPIC040 — Separation Pass 3.
WORK_UNIT_ID: HDE-EPIC040-PR04 — Bounded application, identity and consumer integration.
No Proceed, workspace, worktree, branch, commit, open PR or CI run exists for PR04. Those vehicle
facts are truthfully not yet produced, not missing prerequisites. No PR_RETURN_PHASE applies and
none is asserted; RS-40 is ineligible and is not invoked. Product Owner PR-30 Proceed: NOT
REQUESTED, NOT EXECUTED. This invocation does not request one.

=== THE APPROVED DISPOSITION YOU ARE ACTING ON ===
RS-20 decided APPROVE on 2026-09-22T07:27:55Z, by Isis-50, against
HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1, and emitted exactly one PF10 build-notes addendum
overlay. Finding HDE-EPIC040-PR04-F01 is an approved bounded implementation rescope.
Decision: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md
Overlay: docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md
Both are in amthorn78/glow-hdengine-v2, stored through PR #465 on branch claude/nice-mayer-tf9l4c.
Read both completely from that branch if #465 has not merged when you run, otherwise from main at
the same paths. The overlay is the operative authority for the delta; the review carries the
reasoning, the verification and the two recorded items below.
The overlay is page-ready under PF10-FORM-001 with its addendum number deliberately NOT allocated:
RS-20 never edits PF10, allocates PF10 numbering, or claims canonical adoption. Drainage into PF10
is Nathan's manual action and is not a prerequisite for your work.

=== THE APPROVED DELTA, IN BRIEF ===
PR04's approved loci extend to the files below, for one purpose only: the affected gates express a
truthful, explicit RELEASE_NOT_ADMITTED outcome instead of an ambiguous failure, and ordinary CI
accepts that one outcome while the active release is not admitted. Read the overlay for the
authoritative statement; this is orientation, not a substitute.
Production and CI configuration, nine files: tools/evidence/generate_open_rails_abba_proof.py;
tools/evidence/generate_a7_transport_proofs.py; tools/evidence/generate_determinism_gate_proofs.py;
tools/evidence/run_sanity_pipeline.py; tools/evidence/run_sanity_pipeline_gate.py;
tools/evidence/build_release_attestation.py; tools/evidence/run_canonical_json_gate.py;
.github/workflows/ci.yml; ci/jobs/rails_open_conformance.yml.
Test homes, four files: tests/evidence/test_sanity_pipeline.py;
tests/evidence/test_open_rails_abba_proof.py; tests/evidence/test_rails_ci_workflow_integration.py;
tests/transport/test_a7_transport_proofs.py.
Four binding conditions, not open to interpretation: (1) the outcome is never PASS, never
top_level_pass: true, and never a frozen-byte substitute presented as a live result; (2) the CI
acceptance keys on that one explicit outcome and on the observed non-admitted state of the active
release, never on a generic failure, a lane name or a time window; (3) the acceptance is
self-extinguishing by construction, so no removal is owed and no cleanup PR is created; (4) no
change to the hde.release_attestation.v1 success schema or the PR06R_B_FINAL_PASS wire value is
authorized — any such need is a separate PF12 canon decision for the governed PF12 maintainer.
Ownership limit: PR04's touch on build_release_attestation.py transfers no attestation ownership
from PR06 and is bounded to emitting the distinct non-admitted code on the existing failure-receipt
path and the withholding the builder already performs.
Governed evidence affected by the corrected renders is regenerated by its existing owning writers
and never hand-edited, including audit/gates/sanity_pipeline/sanity_pipeline.log with its path-proof
companion and the SIX outputs of the determinism builder: audit/gates/parity/reader_cli/ab.json,
ba.json and summary.json, audit/gates/determinism/abba.bytes,
audit/gates/determinism/tworun_identity.sha256, and artifacts/cards/a3/IDENTITY_OK.txt. The
proposal listed five and omitted the last; the overlay names all six.

=== TWO ITEMS RS-20 DECIDED THAT CHANGE YOUR PLAN ===
1. run_canonical_json_gate.py is IN the set. The proposal excluded it as X-8, reachable only through
   sanity stage 03. That understates it: generate_open_rails_abba_proof.py::canonical_gate() runs it
   as a subprocess and canonical_gate_success is a predicate of top_level_pass, so its result is a
   direct input to the rails-lane gate; generate_determinism_gate_proofs.py invokes it the same way.
   Under a PR04-shaped simulation it returns rc=1. Its existing treatment as a plan §6.2 necessary
   dependent — dropping removed imports, validating against _FROZEN_GENERATED_SHA256 — is unchanged
   and unaffected. The overlay adds only the permission to express the non-admitted outcome in that
   file where implementation establishes it must live there. Both treatments are stated so the dual
   role is visible rather than ambiguous.
2. tests/evidence/test_release_attestation.py stays OUT, on execution: it is fully green under the
   simulation. Its wire-contract test pins PR06R_B_FINAL_PASS, which condition 4 forbids changing,
   and its failure-receipt test constructs its own code value, so the open code token is not pinned.

=== A SEPARATE FINDING TO RAISE, NOT PART OF THIS OVERLAY ===
Candidate HDE-EPIC040-PR04-F02 — manifest binding refresh for adapter/http_reader.py.
adapter/http_reader.py is simultaneously an approved PR04 locus that instruction §6.5 requires PR04
to change, and one of the fifteen committed members of catalog/manifest.json — the first entry.
tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes
asserts every committed entry's sha256 and size equal the repository bytes; it runs in the release
lane at .github/workflows/ci.yml:251 and FAILS under a PR04-shaped change, while PR04 plan §6.6
lists catalog/manifest.json as explicitly unchanged and instruction §9 excludes manifest expansion
or promotion.
This is the class PF10 §2.10 settled for HDE-EPIC040-PR02 and engine/serializer/canon.py: a single
existing-row rebind through the canonical manifest writer, the roster held at fifteen, release
identity recomputed from actual bytes. That overlay is scoped "For HDE-EPIC040-PR02 only" and its
item 8 reserves complete member refresh and final identity recomputation to PR06, so it does not
extend to PR04.
It is independent of release admission — it would fail with a fully admitted release — so it is
outside F01 by the proposal's own §6.3 definition and is NOT covered by the approved overlay. RS-20
decided nothing about it, scoped no remedy and pre-approved nothing. Raise it through RS-10 in the
ordinary way, on the PF10 §2.10 precedent. It does not gate F01 and the two proceed independently.
Also still carried and not raised: plan §14.2 decision D-03, the valid self-pair exit-0 carrier.

=== WHAT IS SETTLED AND MUST NOT BE REOPENED ===
The classification (bounded implementation rescope, not IN_SCOPE_REPAIR, not
SPECIFICATION_CHANGE_REQUIRED, not a defect in PR01-PR03) and candidate D as the disposition were
decided at review v1.0 §3 and §5 and confirmed at v2.0. The §6.1 canon narrowing holds: the failure
receipt contract already exists and its code and stage fields are open ^[a-z0-9_]+$ tokens, so a
truthful release_not_admitted outcome needs no PF12 schema or wire-value change. PR05 is covered by
this overlay, needs no separate overlay and receives no new loci, on the proof at review v2.0 §7.

=== PRESERVED WORK AND UNCHANGED AUTHORITY ===
PR04 plan v1.0 §§5-8 in full (designed interfaces, invariants, contracts, the exact file and
component plan, the requirement-to-change-and-test mapping and the complete test design), §9
checkpoints C1-C3 executable exactly as written, and §§10-12 are preserved and valid. Only §9 item
15 and §4.2 condition 4 depended on this disposition and are now dispositioned. The immutable
Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1, every active PF10 overlay, and
accepted-final PR01, PR02 and PR03 are unchanged; accepted-final PRs are historical evidence and are
never rerun. Proposal v1.0, review v1.0 and proposal v1.1 are preserved unchanged at their paths.

=== PF10 AND APPLICABLE ACTIVE OVERLAYS ===
Resolve and completely read the unique current controlled PF10 Markdown from docs/pfcanon/ yourself
and read every applicable active addendum by its repository path, then carry that lineage into your
plan. At RS-20 decision time PF10 resolved to docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md, SHA-256
1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f, 1649 lines / 181316 bytes,
recomputed and matched. Applicable overlays and their retained source artifacts: §2.2 (PF10 body
only); §2.3 HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md;
§2.4 HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md;
§2.5 HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md;
§2.6 PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md;
§2.7 HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md and -v2.0.md; §2.8 PF10-FORM-001;
§2.9 HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md;
§2.10 HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md — load-bearing for the F02 candidate
above, and scoped to PR02 alone; §2.11 (PF10 body; review body
HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md);
§2.12 HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md — the executing-mechanics admission
boundary in engine/config/registry_loader.py; §2.13 HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md
— the order PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01, and the record that the actual
repository release remains the incomplete 15-member manifest with PR06 alone owning the 44-member
materialization. PF10 §2.14 exists in the body and is not applicable. The new F01 overlay above is
additional to all of these. Resolve every PF source only from docs/pfcanon/, which is read-only;
never open, compare, cite or fall back to a Google Doc, .doc, .docx, export, archive result or
search hit as PFCanon authority. Record the PF10 version actually read as provenance.

=== REPOSITORY BASELINE, RE-VERIFIED AT THE DECISION ===
main head 0f47079f24834424c4a4cfaba6a8d44d94286ad2, tree 0865ef1814d238910b7da1e935d04124980aba34,
committed 2026-09-22T08:19:44+01:00; working tree clean. git diff
6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612..main excluding docs/ is still empty, so the PR04 plan's
verification point remains exactly valid. The executable baseline is still the accepted PR03 state
9cda1b49a972da874021e8820997fab1ebaff153. PRs #452, #453, #457, #462 and #463 have merged. No PR04
product branch, commit, pull request, Proceed, implementation, review, CI result or merge exists.
Re-verify the head yourself before planning against it.

=== EXECUTED EVIDENCE RS-20 PRODUCED, FOR YOUR PLAN TO BUILD ON ===
A PR04-shaped change was applied in an isolated scratch worktree — engine/runtime/public.py banding
through the admission owner instead of ts_v0, and adapter/http_reader.py implementing the §6.5
Reader POST success path — and all three chains were executed. The worktree was removed; the
repository was clean before and after and no governed artifact was written.
Rails chain: run_rails_job_definitions.py over all three job files returned rc=1 with 18 failures in
tests/evidence/test_open_rails_abba_proof.py; tests/bodygraph/test_vendor_client.py passed. The
workflow integration test failed once, at test_open_rails_producer_check_mode_has_no_repo_residue,
on INCOMPLETE_RELEASE_ROSTER.
Release chain: the lane's four-file pytest set returned 2 failed, 50 passed —
tests/runtime/test_identity.py and tests/evidence/test_release_manifest_content_binding.py;
tests/evidence/test_release_attestation.py was fully green.
Full-validation chain: the complete 40-member supplemental roster returned 14 failed, 1207 passed,
across five files — tests/cli/test_showcompat_sources.py, tests/cli/test_cli_file_inputs.py,
tests/cli/test_cli_install_help.py, tests/qa/test_cli_admin_dumps.py, tests/qa/test_cli_admin_parity.py
and tests/transport/test_a7_transport_proofs.py. Every one is inside the enumeration or inside loci
PR04 already owns; the tests/qa pair are registered engine/cli/main.py owners under plan §6.5.
tools/evidence/run_canonical_json_gate.py --check-only returned rc=1.
All runs used LC_ALL=C LANG=C TZ=UTC with requirements.txt and requirements-dev.txt installed and
pytest 8.4.2 as readiness proof. These are engineering observations, not a QA verdict.

=== CARRIED REGISTER AND UNRESOLVED FACTS ===
CANON_CONFLICT_REGISTER C040-01 through C040-06 is carried unchanged with no entry reopened,
relabeled, omitted, newly decided or resolved. Neither HDE-EPIC040-PR04-F01 nor the F02 candidate is
a register entry. Decision history is preserved in full: REVISION_REQUIRED, Isis-50,
2026-09-22T06:48:06Z, no addendum, against proposal v1.0; APPROVE, Isis-50, 2026-09-22T07:27:55Z,
one addendum, against proposal v1.1. Unresolved facts: U-01 and U-03 resolved; U-07 resolved (X-8
admitted, X-10 upheld); U-02 carried (D-03); U-04 carried (PF12 v2.9.5 against the register's
v2.9.6, governed PF12 maintainer); U-05 carried (PF10 Addendum Index lists through 2.13 while the
body carries 2.14, PF10 drain owner); U-06 carried (repository prompt-provenance persistence
PENDING); U-08 new (the F02 candidate above); U-09 new (the sixth determinism-builder output).

=== CONSTRAINTS AND MANUAL PREREQUISITES ===
Produce PR04 detailed Implementation Plan v1.1 as a complete successor to v1.0, carrying the
approved overlay, in state AWAITING_PO_PROCEED. Preserve v1.0 unchanged at its path. Do not
implement, create a product branch, worktree or pull request, request or fabricate a Proceed, write
or assume CI results, rewrite the immutable whole-change Plan, restart IA-30 or IA-40, rerun
accepted-final PR01-PR03, edit PF10, allocate a PF10 number, claim canonical adoption, draft an
addendum, merge, enable auto-merge, or invoke or route to PR-50 — PR-50 is Nathan-only and merge is
a Product Owner action. AWAITING_PO_PROCEED is a plan state, not an authorization: implementation
begins only on Nathan's separate exact PR-30 invocation against this plan version. Repository paths
outside docs/ephemeral/ and docs/graph/ are not written; docs/pfcanon/ is read-only. Google Drive is
not a source, store or authority for this work. Manual prerequisites: none beyond the operator
selecting session PR04-HDE-EPIC040-1. PR #465 is open and unmerged; the decision and the overlay are
readable on branch claude/nice-mayer-tf9l4c either way.

=== GCFPE_PROMPT_USES (carried) ===
GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-02 — prompt RS-20 — Review Bounded Work-Unit Rescope —
091426.1, page https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204, retrieved revision
2026-09-21T22:57:36.541Z; ecosystem GCFPE-20260914.1 / 091426.1 / 55; role and stage continuing
independent Lead Developer reviewer Isis-50 / RS-20 decision owner, second decision;
MANUAL_PROMPT_EXECUTION; capture 2026-09-22T07:27:55Z; result
HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v2.0, APPROVE, with exactly one PF10 addendum overlay. Preserved
earlier entries by exact reference: GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01 in proposal
v1.1 §13, GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01 in review v1.0 §13,
GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01 in proposal v1.0 §13,
GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01 in plan §16 and
GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01 in instruction §15. Repository provenance persistence
remains PENDING / NON_GATING.

=== NEXT ACTION AND EXPECTED OUTPUT ===
Re-verify the repository head; resolve and completely read current controlled PF10 and every
applicable active overlay including the new F01 overlay; then issue HDE-EPIC040-PR04 detailed
Implementation Plan v1.1 as a complete successor in state AWAITING_PO_PROCEED, written as complete
Markdown under docs/ephemeral/, committed and pushed on a working branch, read back completely and
referenced by repository path, with one pull request; Nathan alone merges. Carry the approved delta
into §6's file and component plan, §9's ordered procedure — item 15 is now dispositioned — and
§4.2's completion conditions, and record the overlay in the plan's lineage. Preserve every section
v1.0 already carries that this disposition does not touch. Raise HDE-EPIC040-PR04-F02 separately
through RS-10; do not fold it into the plan as though it were approved. This invocation supplies no
implementation authority, no Product Owner Proceed, no merge permission, no PF09 movement, no QA
verdict and no closure.
```
