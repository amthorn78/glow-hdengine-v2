---
artifact_type: SKILL_REVIEWER_PROMPT
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1
round: a3 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a2)
committed_before_review: true (D24)
predecessor: REVIEWER-PROMPT-a2.md (round a2, SKILL_REPAIR_REQUIRED from both reviewers)
---

# Reviewer prompt, round a3

The same brief goes to both reviewers. Only the reviewer id and the record path differ. Both are fresh:
neither took part in round a1 or a2.
- **SFR-A3-1** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a3-SFR-A3-1.md`
- **SFR-A3-2** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a3-SFR-A3-2.md`

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Six packages, installed together as one set, in /tmp/claude-0/pkg3/new/:
- amthor-workspace-governance-audit.skill, 15 files, 54899 bytes, sha256 0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7
- change-flow.skill, 22 files, 257909 bytes, sha256 97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0
- flowmaster-validate.skill, 31 files, 317639 bytes, sha256 e8eeda442162081257e6a75e08813d7f4707213c5acbb2fa171505b8544ae766
- glow-hde-pr-development.skill, 4 files, 22494 bytes, sha256 dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913
- session-relay-flowmaster.skill, 5 files, 56330 bytes, sha256 30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b
- tw-flowmaster.skill, 2 files, 20368 bytes, sha256 db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf
Rollback packages, built from today's installed trees, are in /tmp/claude-0/pkg/rollback/. They
are not under review. The round-a1 and round-a2 packages in /tmp/claude-0/pkg/new/ and /tmp/claude-0/pkg2/new/ are
superseded and are not under review either. change-flow, session-relay-flowmaster and tw-flowmaster are
byte-identical to their round-a2 packages: repair a2 changed none of their files.

=== 2. THE PRIOR VERDICTS, AND WHAT DOES NOT CARRY ===
Round a1: SKILL_REPAIR_REQUIRED from SFR-A1-1 and SFR-A1-2, bound to the a1 digests. Round a2:
SKILL_REPAIR_REQUIRED from SFR-A2-1 and SFR-A2-2, bound to the a2 digests (amthor 9d5308e6…,
change-flow 97bf899c…, flowmaster-validate 5ffa13f1…, PR skill 3292e348…, relay 30fdce6a…, tw
db4cde53…). Their records are SECTION-10-REVIEW-a1-*.md and SECTION-10-REVIEW-a2-*.md in the evidence
directory. Nothing in them carries to these bytes, not even for the three packages whose bytes did not
change: this verdict is over the set. Read them for the findings, not the results.
The round-a1 dispositions are listed in REVIEWER-PROMPT-a2.md §2. One of them was wrong: that brief said
the a1 V2 repair put the fallback predicate into the relay and tw CONTRACT_REQUIRED lists. It did not;
only the PR skill guarded the predicate and the D23-E sentence. Both a2 reviewers found this.
What each round-a2 finding became (repair-a2/apply_repairs_a2.py, pin_repairs_a2.py; must-fail
regressions repair-a2/regress_repair_a2.py; Nathan approved the repair set as listed, 2026-09-23):
- SFR-A2-1 R2-1 / SFR-A2-2 F1 (predicate and D23-E sentence guarded only in the PR skill) -> S1:
  FMV-GCF-DISPATCH-001 in validate_flowmaster.py over nine files: the seven C-DISPATCH sites (PR skill,
  change-flow, relay, tw, flowmaster-validate SKILL.md, amthor SKILL.md and interoperability-contracts.md)
  and the two fixture texts. It checks exact predicate counts, the C-DISPATCH fallback clause and the
  anchored D23-E sentence. The amthor suite gains test_pr40_once_per_merge_parity. The PR-skill literal for
  the sentence is now its C-DISPATCH anchor form, so that the new copy in behavior-cases.md cannot satisfy
  it for SKILL.md. Regressions: 18 D-* cases.
- SFR-A2-1 R2-2 (an allowed successor field can take an unapproved value) -> S2: FMV-ORACLE-021, the three
  approved row digests as constants. Regressions U1, U2.
- SFR-A2-2 F2 (duplicate JSON keys) -> S3: strict_json_loads rejects duplicates for the successor and
  historical oracles, the matrix blocks and the successor map. U3 exposed a baseline defect: an
  unreadable oracle raised KeyError in the runtime-map projection, so the suite printed a traceback. That
  line now reads oracle.get(key). Regressions U3, U4.
- SFR-A2-1 R2-3 (layout) -> S4(a): FMV-ORACLE-022, matrix blocks in oracle row order, block key order, no
  other code fence, and every oracle row's key order equal to its historical row. Regressions U5-U8.
- SFR-A2-1 R2-4 / SFR-A2-2 advisory (historical_non_executable_references unchecked) -> S4(b): the exact
  set in validate_contract. Regressions C0-C3.
- SFR-A2-1 R2-5 (relay qualifier unguarded) -> S4(c): both "Outside a GCFPE main-ecosystem stage,"
  sentences in CONTRACT_REQUIRED for the relay. Regressions R-RELAY-255, R-RELAY-717.
- SFR-A2-2 advisory (fixture texts without the void clause) -> S4(d): the D23-E sentence added verbatim
  to behavior-cases.md "Observed merge" and to the amthor behavioral-fixtures.md PR-40 entry fixture, with
  "Reject a second PR-40 entry for the same merge."
Expectations of the earlier regressions that changed, each as a consequence of a2 and listed with its
reason in repair-a2/derive_regressions_a2.py, which derives re-pathed copies and leaves the originals
alone: G2 and G3 gain FMV-ORACLE-021; T1 gains FMV-ORACLE-022; T5 gains FMV-ORACLE-021; the amthor
suite runs 35 tests; R-DISP fails two PR-skill literals.
E3/E4 revision 5 (evidence/e3/E3-E4-report.md) re-ran E4 in memory: unchanged from revision 4.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
The baseline is the installed synced tree
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502.
Its freeze.py digests (docs/prompt_ecosystem_management/freeze.py <dir>):
  flowmaster-validate 29 b9ca212a…, change-flow 21 80e877c2…, glow-hde-pr-development 4 e109d47a…,
  session-relay-flowmaster 5 4ef8daa3…, amthor-workspace-governance-audit 15 6cd088a0…, tw-flowmaster 2 fa3fac85…
  (full values: execution spec v2 §2).
Repaired a3 trees, once extracted: flowmaster-validate 31 cb7e1693…, change-flow 22 1186283d…,
glow-hde-pr-development 4 68077fa6…, session-relay-flowmaster 5 15aef989…, amthor 15 819915e4…,
tw-flowmaster 2 fd6c344b….
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2, local clone /home/user/glow-hdengine-v2. Branch
docs/20260923-modification-intake-alpha-feedback-open-entries — read its HEAD. NOT MERGED; it is
PR #474.
- The plan: docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md
  (§P, Amendment 1, which Nathan approved; §E), and MODIFICATION-20260923-pr40-reject-replans.md.
- The rulings: docs/prompt_ecosystem_management/gcfpe.decision-record.md, D23 with its successor
  notes (including D23-E, once per merge), and D24.
- The execution specification: docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md.
  §12 and its addendum list every choice the plan's author made.
- Evidence and scripts, all under docs/ephemeral/modifications/evidence/:
  build_r1_successor.py, regenerate_contract.py, route_sim_final.py, e1_*.py, e2/ (run_e2.sh
  reproduces the whole E2 stage), repair-a1/ and repair-a2/ (run_repair_a2.sh reproduces the a2
  repair from the round-a2 tree and runs every gate), e3/ (body_rules.py, run_e4.py, E3-E4-report.md), and preflight-2026-09-23.md.
- The successor matrix: docs/prompt_ecosystem_management/r1-successor-source-20260923.md.
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. The six packages carry, exactly, the §8a/§8b edits, the §5 successor oracle, map and matrix,
    the §6 contract 4.1.0 and the pins of spec v2, plus the round-a1 and round-a2 repairs, and
    nothing else. Historical files are byte-unchanged.
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
    and binds them to the successor matrix by recomputable digests. The other 43 rows, the three
    rows' unchanged fields and positions, and the non-row keys equal the historical oracle, and
    FMV-ORACLE-018 to -022 enforce that, and the approved row values, under a full re-stamp.
C7. The gate passes (spec §9; §E rows E1–E4 and E5's repair-a2 record; E3-E4-report.md revision 5).
C8. Each round-a1 and round-a2 finding is closed as §2 states. At each of the nine files, deleting
    the D23-E sentence or a fallback predicate fails the suites.
Authority: Nathan's approval of Amendment 1 ("yes", 2026-09-23), his G06 ruling ("yes"), his
approval of the once-per-merge sentence ("ok"), his approval of the a2 repair set ("yes, run the
repair set as listed"), and the D23 notes quoted there.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The round-a2 repairs: FMV-GCF-DISPATCH-001, FMV-ORACLE-021/022, strict_json_loads, the contract
    value check and the relay literals. Can a re-stamped or text-only change still pass? Try what the a1
    and a2 reviewers did not. Is any of the nine files a site that should not be pinned, or is a
    carrying file missing?
A2. Whether a2 weakened anything: the PR-skill literal change, the .get() in the runtime-map
    projection, and every changed regression expectation in derive_regressions_a2.py. Is each change a
    consequence, not a relaxation?
A3. The successor oracle's provenance (§5): matrix bytes, the digest formula, the authority block,
    N1-N10 and FMV-ORACLE-017. Could a third row change pass unnoticed?
A4. The once-per-merge sentence and the fallback predicate: any double-dispatch or no-dispatch path
    left, including in the two fixture texts?
A5. The regenerator's contract-only value table (§6): wrong or stale values that no check reads.
A6. Every reversed validator literal. Does its replacement still guard the kept rule?
A7. The GCFPE override of the Flowmaster core option to create a session, in change-flow, the relay
    and tw-flowmaster; and the relay's provisioning lines scoped outside GCFPE stages.
A8. The author's own choices in spec §12 and its addendum, and G11's four-finding expected set.
A9. Whether any edited skill line now contradicts a kept rule: no agent merge, no polling, one
    handoff block, PR-40's independent verification, single Proceed within a plan.
Question, not a finding: is anything in these packages outside Amendment 1's scope, the a1 and a2
repairs, or D23-E?

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
     and the a1 repairs name. Derive the list with diff -rq; never type it from memory.
  d. Rosters and contracts: the 46-row oracle, with only the three changed rows differing from the
     historical oracle; the contract equals graph parity (validate_graph_contract returns []).
  e. Recompute every hash pin from its artifact and confirm each consumer agrees with it.
  f. Recount every revision site by grep, independently of the author's list, including every
     site of the once-per-merge sentence and the fallback predicate.
  g. Write must-fail probes of your own against the round-a2 checks (FMV-GCF-DISPATCH-001,
     FMV-ORACLE-021/022, duplicate keys) under the full re-stamp that regress_oracle.py uses, and report
     each result.
Derive every digest from the artifact in front of you. Never transcribe one from the report.
The author's measurements, for you to contradict rather than confirm: every suite above passes;
the fixtures give 228 cases with 0 failed; the historical outputs are byte-equal to baseline; the
routing surface is fecc319b…/284; the regressions are exact: oracle 15, skills 70, contract 53 + 35 + 3,
fixtures 2, a1 17, a2 34 (repair-a2/outputs/).

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation or a prior measurement as carrying to these
bytes. Do not edit docs/pfcanon, the registry, the graph parts, Notion or any prompt body. Write
only your own record file (and scratch files under /tmp/claude-0/review-<REVIEWER_ID>/). Do not
commit; the author commits your record.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding. State for each round-a2 finding whether §2's disposition
closes it on these bytes.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
