---
artifact_type: RS20_HANDOFF
artifact_id: HDE-EPIC040-PR04-F01-RS20-HANDOFF
artifact_version: "1.0"
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
decision: REVISION_REQUIRED
decision_ref: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v1.0
receiver_prompt: RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1
receiver_prompt_url: https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204
addendum_created: NONE
pr_return_phase: NOT_APPLICABLE
created_at_utc: 2026-09-22T06:48:06Z
---

# HDE-EPIC040-PR04-F01 — RS-20 Handoff v1.0

## Outcome

`RS-20` decided **`REVISION_REQUIRED`** on `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0`.

The finding is real and its classification is settled: `HDE-EPIC040-PR04-F01` is a **bounded implementation rescope**, and candidate **D** is the correct disposition. The proposal's enumerated bounded delta is **provably incomplete** — it names six files and cannot achieve its own stated purpose without a seventh, `tools/evidence/run_sanity_pipeline_gate.py`. Because the overlay is deliberately stated as an exhaustive file list in order to bound its precedent, that omission is a defect in the artifact.

**No `PF10_BUILD_NOTES_ADDENDUM` was created.** Only `APPROVE` creates one.

## Repository references

| Artifact | Repository path in `amthorn78/glow-hdengine-v2` |
| --- | --- |
| Decision | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-checkpoint-v1.0.md` |
| This handoff | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v1.0.md` |
| Reviewed proposal v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` (merged in PR #457) |
| PR04 instruction v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md` (merged in PR #452) |
| PR04 implementation plan v1.0 `DRAFT` | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md` (merged in PR #453) |
| Immutable base Plan v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` |
| Approving Plan Review v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| Specification v1.1 | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` |
| Implementation Audit v2.0 | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` |
| Current controlled PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md` (read-only) |

Storage pull request for this stage's three artifacts: **PR #459**, branch `claude/nice-mayer-tf9l4c`. **Nathan alone merges.**

## What Nathan does next

Paste the block below into the **same session that authored the rescope proposal** — the retained whole-change HDE-EPIC040 Implementation Architect. It is complete and requires no editing.

```text
NEXT_PROMPT_HANDOFF

Run RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1
https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204

=== RECEIVING ROLE AND SESSION ===
Actor: the retained whole-change HDE-EPIC040 Implementation Architect — the same session that
authored HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0. session_disposition: RETAIN_EXISTING.
role_session_ref: that same RS-10 proposal author session; the operator selects it. Do not create,
restart or replace a session and do not invent a platform session ID. The dedicated PR-development
session PR04-HDE-EPIC040-1 is retained separately for HDE-EPIC040-PR04 and is not replaced or
addressed by this invocation. The RS-20 decision owner remains Isis-50, the continuing independent
Lead Developer reviewer, and the artifact type remains RESCOPE_PROPOSAL. No new approval owner is
created. invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-30 (GCF-17.RESCOPE).
context_conflict: NONE established. EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION.
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS.

=== CHANGE, WORK UNIT AND FINDING ===
CHANGE_CLASS: EPIC. CHANGE_ID: HDE-EPIC040 — Separation Pass 3.
WORK_UNIT_ID: HDE-EPIC040-PR04 — Bounded application, identity and consumer integration.
FINDING_REF: HDE-EPIC040-PR04-F01 — PR04's approved completion condition (its proofs pass CI)
cannot be met inside PR04's approved loci.
Originating stage: PR-20 planning in session PR04-HDE-EPIC040-1, before any Proceed, workspace,
worktree, branch, commit, open PR or CI run. No PR_RETURN_PHASE applies and none is asserted; those
vehicle facts are truthfully not yet produced, not missing prerequisites. RS-40 is ineligible and
is not invoked. Product Owner PR-30 Proceed: NOT REQUESTED, NOT EXECUTED.

=== THE DECISION YOU ARE ACTING ON ===
RS-20 decided REVISION_REQUIRED on 2026-09-22T06:48:06Z, by Isis-50, against
HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0. No PF10 addendum was created and none may be drafted,
numbered or implied by this invocation.
Decision artifact: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md in
amthorn78/glow-hdengine-v2, stored through PR #459 on branch claude/nice-mayer-tf9l4c. Read it
completely from that branch if #459 has not merged when you run, otherwise from main at the same
path. Its §6 carries the exact redlines, §2 the independent verification, §4 the proof that the
submitted delta is incomplete, §5 the confirmation of candidate D, §7 the PR05 answer, §9 the
evidence against each excluded decision, §10 the carried register and §11 the unresolved facts.

=== WHAT IS SETTLED AND MUST NOT BE RELITIGATED ===
- Classification: HDE-EPIC040-PR04-F01 is a bounded implementation rescope. Not IN_SCOPE_REPAIR,
  not SPECIFICATION_CHANGE_REQUIRED, not a defect in PR01-PR03. Decided; do not reopen it.
- The suspended boundary is confirmed, and RS-20 reproduced it by execution rather than inference:
  a change confined to PR04's own approved loci, implementing exactly PR04's approved behavior,
  turns all three selected gates red (review §2.3, observations V-05 through V-08).
- Candidate D remains the correct disposition. Do not re-argue A, B or C.
- Proposal §6.1's narrowing holds and is confirmed: schemas/hde_release_attestation_failure.v1.json
  exists, _write_failure already emits it, and its code and stage fields are open ^[a-z0-9_]+$
  tokens, so a truthful release_not_admitted outcome needs no PF12 schema or wire-value change.

=== BLOCKING REDLINES ===
R-1. The enumerated file set is incomplete. Add tools/evidence/run_sanity_pipeline_gate.py to §4.4,
§6.2, §6.3 candidate D and §10, and correct §4.4's closing sentence and the §6.3 cost cell to the
corrected count. Proof to carry: build_release_attestation.py:669 invokes the gate wrapper, not
run_sanity_pipeline.py directly; run_sanity_pipeline_gate.py::_expected_log() builds a byte-exact
log in which all fifteen stages read ":OK" with first_failed_stage:NONE and summary:PASS, and
_valid_log() requires data == _expected_log() byte equality; run_sanity_pipeline.py::_render_log at
line 220 collapses every stage status to exactly "OK" or "FAIL", so no third token exists today;
build_release_attestation.py:757-766 independently requires that same tail. A truthful third state
must therefore be expressible in run_sanity_pipeline.py and accepted by run_sanity_pipeline_gate.py
before it can reach the attestation's failure receipt at all.
R-2. State the method by which the enumerated set was derived, and its stopping condition — an
explicit, reproducible trace of every PASS pin reachable from the rails lane and from the release
lane through build_release_attestation.py. An exhaustive enumeration is what risk R-01 relies on to
bound the precedent, so it must be derived exhaustively rather than by inspection. RS-20 proved six
is insufficient; it did not prove seven is sufficient, and declined to substitute its own
unverified enumeration. That proof is yours to supply.

=== REQUIRED CORRECTIONS THAT DO NOT CHANGE THE DISPOSITION ===
R-3. §6.1 third bullet and §10 E-13: schemas/hde_release_attestation.v1.json pins pipeline_stop as
{"type": "null"}, not const null. validation_result and release_admission are const as stated.
R-4. §7 Dependencies and §11 R-03: replace the assertion that PR05 inherits the condition with its
proof, supplied in review §7.
R-5. §6.3 candidate D cost cell: record that widening PR04's loci to the named CI and evidence files
selects no additional CI lane, because PR04's candidate already runs full validation and all seven
lanes through its planned change to ci/checks/classify_ci_changes.py, a member of
_FULL_VALIDATION_PATHS. This materially lowers D's stated cost and should be visible to the reader.
R-6. §5 second bullet: qualify "every truthful treatment lies outside the work unit's approved
loci". PR04's plan §6.2 and §6.5 already change several paths outside instruction §7.1 as necessary
dependents, including ci/checks/classify_ci_changes.py, tools/evidence/run_canonical_json_gate.py
and tools/cli/generate_showcompat_artifacts.py, without a rescope. State the distinguishing
criterion the overlay rests on: these six or seven files change gate semantics and acceptance,
whereas the plan's dependents change coherence registration and frozen-byte validation.
R-7. §6.2 item 2 and §7 Downstream: state explicitly that PR04's bounded touch on
tools/evidence/build_release_attestation.py transfers no attestation ownership from PR06. Plan §4.2
maps complete release and external attestation to cut_release_manifest.py, release_id_recompute.py
and build_release_attestation.py, and Plan §6.6 gives PR06 the owning attestation validator only
where current contract gaps are evidenced. Bound PR04's touch to the non-admitted outcome and its
failure receipt.

=== CONDITIONS TO CARRY FORWARD UNCHANGED ===
RS-20 confirms these as correct; they are not open for revision.
- The explicit outcome is never PASS, never top_level_pass: true, and never a frozen-byte
  substitute presented as a live result. Frozen captures stay frozen with their existing nonclaims.
- The ordinary-CI acceptance keys on that one explicit outcome only, and on the observed
  non-admitted state of the active release — never on a generic failure, a lane name or a time
  window. This is risk R-02's mitigation and it is binding.
- Because the acceptance is conditioned on a runtime-observable fact rather than a hardcoded
  window, it is self-extinguishing by construction: once PR06 admits the complete 44-member roster
  the branch is never taken, and its continued presence is truthful and inert. No later removal is
  owed, no unit is allocated scope for one, and no cleanup PR is required.
- No change to the hde.release_attestation.v1 success schema or to the PR06R_B_FINAL_PASS wire
  value is authorized. If implementation nonetheless requires one, that portion is a separate PF12
  canon decision routed to the governed PF12 maintainer as a new finding, and is not pre-authorized.

=== PR05 — ANSWERED BY RS-20 ===
Yes. An overlay approved on the corrected delta covers PR05's inherited condition, and PR05 requires
no separate overlay and receives no new loci. Proven: PR05's Plan §6.5 owned loci classify to the
lane union {evidence, product, release}; the release lane is exactly where sanity stages 04 and 05
run; PR05 owns none of the affected files; PR05 runs before PR06 under the order PF10 §2.13 fixes.
PR05 inherits through the release lane only, not the rails lane. Because the condition keys on the
non-admitted state of the active release rather than on PR04's candidate, it covers every candidate
in the interval and extinguishes for all of them when PR06 lands. Carry this at §7 and §11 R-03.

=== REPOSITORY BASELINE, RE-VERIFIED BY RS-20 ===
main head a07340965c1dabbe0205135e321ecd6e76687d68, tree 9ab2c9a9c3ed1dfb9aba127ee19c87fce8d98702,
committed 2026-09-22T07:35:39+01:00; working tree clean. git diff
6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612..main excluding docs/ is still empty, so the plan's
verification remains exactly valid. The only post-PR03 commits touching ci/ or .github/ are 3c0b1fa
and c683255, both ancestors of 6ecacafb; fe65a3b and 28612bc touch AGENTS.md only. The executable
baseline is still the accepted PR03 state 9cda1b49a972da874021e8820997fab1ebaff153. No PR04 product
branch, commit, pull request, Proceed, implementation, review, CI result or merge exists.
Correction to the earlier record: PRs #452, #453 and #457 have all merged, so the instruction, the
PR04 plan and the proposal are all on main. Re-verify the head yourself.

=== PF10 AND APPLICABLE ACTIVE OVERLAYS ===
Resolve and completely read the unique current controlled PF10 Markdown from docs/pfcanon/ yourself
and read every applicable active addendum by its repository path, then carry that lineage into your
revision. At RS-20 decision time PF10 resolved to docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md,
SHA-256 1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f, 1649 lines / 181316 bytes,
recomputed and matched. Applicable overlays and their retained source artifacts are unchanged from
proposal §2: §2.2 (PF10 body only); §2.3 HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md;
§2.4 HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md;
§2.5 HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md;
§2.6 PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md;
§2.7 HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md and -v2.0.md; §2.8 PF10-FORM-001;
§2.9 HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md;
§2.10 HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md; §2.11 (PF10 body; review body
HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md);
§2.12 HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md;
§2.13 HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md. PF10 §2.14 exists in the body and is not
applicable. §2.12 places the executing-mechanics admission boundary in
engine/config/registry_loader.py and §2.13 fixes the order PR01 → PR02 → PR03 → PR04 → PR05 → PR06 →
PR07 → OPS01; both remain load-bearing. PF10 §2.13 also independently corroborates the cause: it
records that the actual repository release remains the incomplete 15-member manifest and that PR06
alone owns the 44-member materialization. Resolve every PF source only from docs/pfcanon/, which is
read-only; never open, compare, cite or fall back to a Google Doc, .doc, .docx, export, archive
result or search hit as PFCanon authority. Record the PF10 version actually read as provenance.

=== CARRIED REGISTER AND UNRESOLVED FACTS ===
CANON_CONFLICT_REGISTER C040-01 through C040-06 is carried unchanged in review §10 with no entry
reopened, relabeled, omitted, newly decided or resolved. HDE-EPIC040-PR04-F01 is not a register
entry. Unresolved facts, all non-gating: U-01 resolved — the baseline advanced and #453 and #457
merged; U-02 carried — plan §14.2 decision D-03 remains a deliberately unbundled potential second
boundary, not raised here; U-03 resolved — the Specification v1.1 SHA-256 was independently
recomputed as 43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df and matches, so
close it at v1.1; U-04 carried — repository-resolved PF12 v2.9.5 against the register's v2.9.6,
owned by the governed PF12 maintainer; U-05 new — PF10's §1.1 Addendum Index lists through 2.13
while the body carries 2.14, an observation for the PF10 drain owner; U-06 new — repository prompt
provenance persistence remains PENDING with no installed GCFPE_PROMPT_PROVENANCE.md procedure,
schema, writer or destination in docs/changes.

=== CONSTRAINTS ===
Preserve proposal v1.0 intact; v1.1 supersedes it without deletion or rewriting. Preserve all
completed valid work: PR04 plan §§5-8 in full, §9 checkpoints C1-C3 executable as written, and
§§10-12; only §9 item 15 and §4.2 condition 4 remain dependent on a disposition. Preserve the
immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1, every active PF10 overlay,
and accepted-final PR01, PR02 and PR03, which are historical evidence and are never rerun. Do not
implement, create a product branch or PR, request or fabricate a Proceed, rewrite the immutable
Plan, restart IA-30 or IA-40, edit PF10, allocate a PF10 number, claim canonical adoption, draft an
addendum, merge, enable auto-merge, or invoke or route to PR-50 — PR-50 is Nathan-only and merge is
a Product Owner action. Repository paths outside docs/ephemeral/ and docs/graph/ are not written;
docs/pfcanon/ is read-only. Google Drive is not a source, store or authority for this work.
Manual prerequisites: none beyond the operator selecting the RS-10 proposal author session. PR #459
is open and unmerged; the RS-20 decision is readable on branch claude/nice-mayer-tf9l4c either way.

=== GCFPE_PROMPT_USES (carried) ===
GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01 — prompt RS-20 — Review Bounded Work-Unit Rescope —
091426.1, page https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204, retrieved revision
2026-09-21T22:57:36.541Z; ecosystem GCFPE-20260914.1 / 091426.1 / 55; role and stage continuing
independent Lead Developer reviewer Isis-50 / RS-20 decision owner; MANUAL_PROMPT_EXECUTION; capture
2026-09-22T06:48:06Z; result HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v1.0, REVISION_REQUIRED, no
addendum. Preserved earlier entries by exact reference:
GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01 in proposal §13,
GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01 in plan §16 and
GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01 in instruction §15. Repository provenance persistence
remains PENDING / NON_GATING.

=== NEXT ACTION AND EXPECTED OUTPUT ===
Apply redlines R-1 through R-7 to HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0 and produce one
complete successor, HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1, in state
RESCOPE_PROPOSAL_PENDING_REVIEW, as complete Markdown under docs/ephemeral/, committed and pushed on
a working branch, read back completely and referenced by repository path, with one pull request;
Nathan alone merges. Carry the settled classification and candidate D forward rather than
re-deriving them, and record the RS-20 decision and this revision in its lineage. The successor
returns to the same Isis-50 reviewer session for a second RS-20 decision. This invocation supplies
no implementation authority, no Product Owner Proceed, no merge permission, no PF10 addendum, no
PF09 movement, no QA verdict and no closure.
```
