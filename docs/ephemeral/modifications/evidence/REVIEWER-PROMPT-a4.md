---
artifact_type: SKILL_REVIEWER_PROMPT
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1
round: a4 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after hardening round a3)
committed_before_review: true (D24)
predecessor: REVIEWER-PROMPT-a3.md (round a3, SKILL_FIT_CONFIRMED from both reviewers, for other bytes)
---

# Reviewer prompt, round a4

The same brief goes to both reviewers. Only the reviewer id and the record path differ. Both are fresh:
neither took part in rounds a1 to a3.
- **SFR-A4-1** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a4-SFR-A4-1.md`
- **SFR-A4-2** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a4-SFR-A4-2.md`

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Six packages, installed together as one set, in /tmp/claude-0/pkg4/new/:
- amthor-workspace-governance-audit.skill, 15 files, 54899 bytes, sha256 0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7
- change-flow.skill, 22 files, 257990 bytes, sha256 af8cff939b1b94ced1c487dbcb6b87a6ccb9904304b3ca7cc621fd0798c34902
- flowmaster-validate.skill, 31 files, 318773 bytes, sha256 b1f9184b88eff82dfbe49044509626dba7863bc080e93008491061758e56eef6
- glow-hde-pr-development.skill, 4 files, 22494 bytes, sha256 dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913
- session-relay-flowmaster.skill, 5 files, 56330 bytes, sha256 30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b
- tw-flowmaster.skill, 2 files, 20368 bytes, sha256 db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf
Rollback packages, built from today's installed trees, are in /tmp/claude-0/pkg/rollback/. They
are not under review. Earlier packages in /tmp/claude-0/pkg/new/, pkg2/new/ and pkg3/new/ are superseded
and are not under review either. amthor, glow-hde-pr-development, session-relay-flowmaster and tw-flowmaster
are byte-identical to their round-a3 packages; change-flow changed only in its copy of the contract.

=== 2. THE PRIOR VERDICTS, AND WHAT DOES NOT CARRY ===
Rounds a1 and a2: SKILL_REPAIR_REQUIRED from both reviewers each; their findings were repaired (see
REVIEWER-PROMPT-a2.md §2 and REVIEWER-PROMPT-a3.md §2). Round a3: SKILL_FIT_CONFIRMED from SFR-A3-1 and
SFR-A3-2, bound to the a3 digests (amthor 0070d61c…, change-flow 97bf899c…, flowmaster-validate e8eeda44…,
PR skill dadf64b2…, relay 30fdce6a…, tw db4cde53…). Nathan then chose to fold the round-a3 non-blocking
findings in before installing, so these are new bytes and nothing carries: not those confirmations, and
not any measurement in SECTION-10-REVIEW-a1/a2/a3-*.md. Read those records for the findings, not the
results.
What each round-a3 finding became (repair-a3/apply_repairs_a3.py, pin_repairs_a3.py; must-fail
regressions repair-a3/regress_repair_a3.py):
- SFR-A3-2 A3-1 / SFR-A3-1 F1 (a fourth code block inside a block quote, list item or <pre> escapes the
  fence count) -> H1: FMV-ORACLE-022 counts fence lines after stripping block-quote and list-item
  prefixes, and rejects <pre>. Regressions Q1-Q3.
- SFR-A3-2 A3-2 / SFR-A3-1 limit (counts, not positions; text moved into an HTML comment) -> H2:
  FMV-GCF-DISPATCH-001 pins the whole C-DISPATCH passage (identical at the seven carrying sites, ending
  with the D23-E sentence) once per carrying site. Every other fallback predicate, and the fixture texts'
  D23-E sentence, is pinned by its own sentence context. HTML comments are removed before counting.
  Regressions Q8-Q11.
- SFR-A3-1 V1 (a missing carrying skill is skipped) -> H3: reported as FMV-GCF-DISPATCH-001. Regression V1.
- SFR-A3-1 V2 (an extra top-level key in the successor map passes) -> H4: FMV-GCF-MAP-005 requires
  exactly the projection keys, in order. Regression V2.
- SFR-A3-2 A3-3 / SFR-A3-1 limit (the contract does not carry the D23-E void rule) -> H5: the
  contract-only value route_graph_semantics.pr40_entry gains the D23-E sentence, and validate_contract
  expects it. route_graph_semantics lies outside the graph and outside the routing surface. The graph
  stays ae2bd159…, the routing surface stays fecc319b…/284 (the diff Nathan read), and the contract
  becomes 6902924a…, 613326 B. Provenance: the E2 regenerator still produces 7a7fd028…; H5 asserts that
  input and changes that one value only. Regressions K0-K2.
No earlier regression expectation changed: all 191 are exact on the new tree. Control: every new case
except K0, K2 and Q2 fails on the round-a3 reviewed tree (repair-a3/outputs/regress_repair_a3_on_pre.out).
Q2 was already caught there, as SFR-A3-1 found.
E3/E4 revision 6 (evidence/e3/E3-E4-report.md) re-ran E4 in memory: unchanged from revision 4.
Known limits that stay: a contradicting sentence added after a pinned sentence, and an author who edits
a pinned constant in the same validator and re-stamps. No literal check can catch either.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
The baseline is the installed synced tree
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502.
Its freeze.py digests (docs/prompt_ecosystem_management/freeze.py <dir>):
  flowmaster-validate 29 b9ca212a…, change-flow 21 80e877c2…, glow-hde-pr-development 4 e109d47a…,
  session-relay-flowmaster 5 4ef8daa3…, amthor-workspace-governance-audit 15 6cd088a0…, tw-flowmaster 2 fa3fac85…
  (full values: execution spec v2 §2).
Hardened a4 trees, once extracted: flowmaster-validate 31 95d8469d…, change-flow 22 ee546df5…,
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
  reproduces the whole E2 stage), repair-a1/, repair-a2/ and repair-a3/ (run_repair_a3.sh reproduces
  the a3 hardening from the round-a3 tree and runs every gate), e3/ (body_rules.py, run_e4.py, E3-E4-report.md), and preflight-2026-09-23.md.
- The successor matrix: docs/prompt_ecosystem_management/r1-successor-source-20260923.md.
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. The six packages carry, exactly, the §8a/§8b edits, the §5 successor oracle, map and matrix,
    the §6 contract 4.1.0 and the pins of spec v2, plus the round-a1 and round-a2 repairs and the
    round-a3 hardening, and nothing else. Historical files are byte-unchanged.
C2. The regenerated contract equals graph parity. It reproduces today's contract (2b78f877…) from a
    template stripped of the mirrored keys, so it is not a no-op. Its output (7a7fd028…) differs from the
    shipped contract (6902924a…) only in route_graph_semantics.pr40_entry (H5).
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
C7. The gate passes (spec §9; §E rows E1–E4 and E5's repair records; E3-E4-report.md revision 6).
C8. Each round-a3 finding is closed as §2 states. At each of the nine files, deleting or moving the
    D23-E sentence or a fallback predicate, or hiding it in an HTML comment, fails the suites. The
    contract carries the D23-E sentence, and the graph and routing surface are unchanged.
Authority: Nathan's approval of Amendment 1 ("yes", 2026-09-23), his G06 ruling ("yes"), his
approval of the once-per-merge sentence ("ok"), his approval of the a2 repair set ("yes, run the
repair set as listed"), his choice to fold the round-a3 findings in ("we may as well do it now"),
and the D23 notes quoted there.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The round-a3 hardening: the fence counter, the pinned C-DISPATCH passage and sentence contexts,
    comment stripping, the missing-skill report, the map key check, and the pr40_entry value. Can a
    re-stamped or text-only change still pass? Try what the a1 to a3 reviewers did not.
A2. Whether a3 weakened or over-reached: is any pinned context wrong or too wide? Does H5 change anything
    beyond the one contract value? Do the graph and routing surface really stay as Nathan read them?
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
repairs, the a3 hardening, or D23-E?

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
  g. Write must-fail probes of your own against the round-a3 hardening (FMV-GCF-DISPATCH-001 positions
     and comments, the FMV-ORACLE-022 fence count, FMV-GCF-MAP-005 keys, pr40_entry) under the full
     re-stamp that regress_oracle.py uses, and report each result.
  h. Confirm the contract differs from the regenerator's output only in route_graph_semantics.pr40_entry,
     and that the graph build and routing surface are unchanged.
Derive every digest from the artifact in front of you. Never transcribe one from the report.
The author's measurements, for you to contradict rather than confirm: every suite above passes;
the fixtures give 228 cases with 0 failed; the historical outputs are byte-equal to baseline; the
routing surface is fecc319b…/284; the regressions are exact: oracle 15, skills 70, contract 53 + 35 + 3,
fixtures 2, a1 17, a2 34, a3 13 (repair-a3/outputs/).

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
explicitly; a question is not a finding. State for each round-a3 finding whether §2's disposition
closes it on these bytes.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
