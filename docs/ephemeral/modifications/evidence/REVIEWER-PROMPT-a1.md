---
artifact_type: SKILL_REVIEWER_PROMPT
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1
round: a1 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries)
committed_before_review: true (D24)
---

# Reviewer prompt, round a1

The same brief goes to both reviewers. Only the reviewer id and the record path differ:
- **SFR-A1-1** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a1-SFR-A1-1.md`
- **SFR-A1-2** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a1-SFR-A1-2.md`

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Six packages, installed together as one set, in /tmp/claude-0/pkg/new/:
- amthor-workspace-governance-audit.skill, 15 files, 54344 bytes, sha256 db6c4807c2c552114b816c9e720825b0faa07317ed797e199b05a2cd31ad8999
- change-flow.skill, 22 files, 257847 bytes, sha256 a1170af8d953dcd06aa750b6dd4adf1a29f8ca1ed74e4a14c7f444c3507e73c6
- flowmaster-validate.skill, 31 files, 313930 bytes, sha256 3ebce735eeb88d3dfc028c94df49ba30f4f24ece110caf274e9be5b267665688
- glow-hde-pr-development.skill, 4 files, 22191 bytes, sha256 c77f624f9903c8c4849d963dc2c57dac139ddd2833b4a0f13e6d6051552cb316
- session-relay-flowmaster.skill, 5 files, 56281 bytes, sha256 bfe6b8c6f94f67144953a96c4e037fe010281aa76e0ca27200fb9b1f1d883d89
- tw-flowmaster.skill, 2 files, 20318 bytes, sha256 bdb73141cfabae14a6305eaa24002e61930d5b54752a24e821fd886126741556
Rollback packages, built from today's installed trees, are in /tmp/claude-0/pkg/rollback/. They
are not under review.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
NONE: first review of these bytes. Earlier verdicts on these skills, from rounds 23–30, were issued
against other digests and do not carry.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
The baseline is the installed synced tree
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502.
Its freeze.py digests (docs/prompt_ecosystem_management/freeze.py <dir>):
  flowmaster-validate 29 b9ca212a…, change-flow 21 80e877c2…, glow-hde-pr-development 4 e109d47a…,
  session-relay-flowmaster 5 4ef8daa3…, amthor-workspace-governance-audit 15 6cd088a0…, tw-flowmaster 2 fa3fac85…
  (full values: execution spec v2 §2).
Repaired trees, once extracted: flowmaster-validate 31 d2d98c69…, change-flow 22 880c4284…,
glow-hde-pr-development 4 c075226e…, session-relay-flowmaster 5 fb70af77…, amthor 15 46d22b2d…,
tw-flowmaster 2 1875015f….
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2, local clone /home/user/glow-hdengine-v2. Branch
docs/20260923-modification-intake-alpha-feedback-open-entries — read its HEAD. NOT MERGED; it is
PR #474.
- The plan: docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md
  (§P, Amendment 1, which Nathan approved; §E), and MODIFICATION-20260923-pr40-reject-replans.md.
- The rulings: docs/prompt_ecosystem_management/gcfpe.decision-record.md, D23 with its successor
  notes, and D24.
- The execution specification: docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md.
  §12 and its addendum list every choice the plan's author made.
- Evidence and scripts, all under docs/ephemeral/modifications/evidence/:
  build_r1_successor.py, regenerate_contract.py, route_sim_final.py, e1_*.py, e2/ (run_e2.sh
  reproduces the whole E2 stage), e3/ (body_rules.py, run_e4.py, E3-E4-report.md), and
  preflight-2026-09-23.md.
- The successor matrix: docs/prompt_ecosystem_management/r1-successor-source-20260923.md.
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. The six packages carry, exactly, the §8a/§8b edits, the §5 successor oracle, map and matrix,
    the §6 contract 4.1.0 and the pins of spec v2, and nothing else. Historical files are
    byte-unchanged.
C2. The regenerated contract equals graph parity. It reproduces today's contract (2b78f877…) from a
    template stripped of the mirrored keys, so it is not a no-op.
C3. The routing surface is fecc319bdd4ce7ee6201cb77d7231861/284, the diff Nathan read (Amendment 1,
    A1-7).
C4. Every reversed check has a replacement that still guards what is kept, and a must-fail
    regression proves it. No check is weakened except where the record says so (G06 option (b),
    approved by Nathan).
C5. No main-ecosystem skill text instructs creating, launching or scheduling a session, or running
    a main-ecosystem prompt as a subagent. Workers inside a task are allowed. GCFPE-MGMT-10 and the
    triage prompt are excepted (D23 clarification).
C6. The successor R1 oracle changes exactly three rows (GCF-14, GCF-17, GCF-17.LINEAGE), keeps 46,
    and binds them to the successor matrix by recomputable digests. The other 43 rows equal the
    historical rows.
C7. The gate passes (spec §9; §E rows E1–E4).
Authority: Nathan's approval of Amendment 1 ("yes", 2026-09-23), his G06 ruling ("yes"), and the
D23 notes quoted there.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The successor oracle's provenance (§5): matrix bytes, the digest formula, the authority block,
    N1–N10 and FMV-ORACLE-017. Could a third row change pass unnoticed?
A2. The regenerator's contract-only value table (§6): wrong or stale values that no check reads.
A3. Every reversed validator literal. Does its replacement still guard the kept rule? Is the
    old text forbidden, and does injecting it fail?
A4. The PART-11 fallback path: MERGE_OBSERVED, and the fallback condition "only where no
    MERGE_OBSERVED result was returned for this merge". Is there a double-dispatch or a no-dispatch
    path?
A5. The GCFPE override of the Flowmaster core option to create a session, in change-flow, the
    relay and tw-flowmaster; and the relay's provisioning line scoped outside GCFPE stages.
A6. The author's own choices in spec §12 and its addendum, and G11's four-finding expected set.
A7. Whether any edited skill line now contradicts a kept rule: no agent merge, no polling, one
    handoff block, PR-40's independent verification, single Proceed within a plan.
Question, not a finding: is anything in these packages outside Amendment 1's scope?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. The prompt bodies live in Notion and must not be copied. E3/E4 (body edits and the gate over
    them) are reported in evidence/e3/E3-E4-report.md. You may re-run run_e4.py only by fetching
    bodies into memory, never writing them; this is optional, and you need not do it.
L2. Nothing has been installed; no post-install check exists yet.
L3. The installed tree's manifest.json mtime changes on the host's periodic sync. That is not a
    content change.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy under /tmp/claude-0/review-<REVIEWER_ID>/. Never write to the synced
skills directory. Run everything with PYTHONDONTWRITEBYTECODE=1 and TMPDIR inside your scratch.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm name: in each SKILL.md frontmatter is unchanged.
  b. Copy the whole synced tree to scratch, replace the six skills with the extracted contents, and
     run FROM THEM:
       python3 <fv>/validate_flowmaster.py --skills-root <copy>
       python3 <fv>/validate_flowmaster.py --skills-root <copy> --strict-warnings --gcfpe-contract <cf>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json --gcfpe-candidate-root <root>
       python3 <fv>/validate_gcfpe_20260914.py <cf> --contract <cf>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 <fv>/run_gcfpe_20260914_fixtures.py <cf> --contract <same>
       python3 <fv>/validate_gcfpe_current.py <cf> ; python3 <fv>/run_gcfpe_current_fixtures.py <cf> ; python3 <fv>/run_change_flow_fixtures.py
       python3 <cf>/scripts/validate_gcfpe_20260914.py
       python3 <copy>/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py
       python3 <copy>/session-relay-flowmaster/scripts/validate_relay_manifest.py --self-test
       (cd <copy>/amthor-workspace-governance-audit/scripts && python3 run_fixture_suite.py)
       plus the 12 historical-layer commands of spec v2 §2.
     <root> is a scratch directory holding only graph/GCFPE-20260914.1-Candidate-Graph-Contract.json,
     the embedded JSON of a graph_parts.py build of the branch's docs/graph/parts.
     Read each tool's own top-level flag by name. A green section count beside a false suite flag
     means the suite failed.
  c. Confirm the extracted trees differ from the installed tree only in the files spec v2 §8a/§8b/§5/§6
     name. Derive the list with diff -rq; never type it from memory.
  d. Rosters and contracts: the 46-row oracle, with only the three changed rows differing from the
     historical oracle; the contract equals graph parity (validate_graph_contract returns []).
  e. Recompute every hash pin from its artifact and confirm each consumer agrees with it.
  f. Recount every revision site by grep, independently of the author's list.
Derive every digest from the artifact in front of you. Never transcribe one from the report.
The author's measurements, for you to contradict rather than confirm: every suite above passes;
the fixtures give 228 cases with 0 failed; the historical outputs are byte-equal to baseline; the
routing surface is fecc319b…/284.

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation as carrying to these bytes. Do not edit
docs/pfcanon, the registry, the graph parts, Notion or any prompt body. Write only your own record
file (and scratch files under /tmp/claude-0/review-<REVIEWER_ID>/).

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
