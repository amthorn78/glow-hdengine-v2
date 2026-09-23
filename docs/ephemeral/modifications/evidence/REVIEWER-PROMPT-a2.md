---
artifact_type: SKILL_REVIEWER_PROMPT
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1
round: a2 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a1)
committed_before_review: true (D24)
predecessor: REVIEWER-PROMPT-a1.md (round a1, SKILL_REPAIR_REQUIRED from both reviewers)
---

# Reviewer prompt, round a2

The same brief goes to both reviewers. Only the reviewer id and the record path differ. Both are fresh:
neither took part in round a1.
- **SFR-A2-1** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a2-SFR-A2-1.md`
- **SFR-A2-2** writes `docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a2-SFR-A2-2.md`

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Six packages, installed together as one set, in /tmp/claude-0/pkg2/new/:
- amthor-workspace-governance-audit.skill, 15 files, 54461 bytes, sha256 9d5308e67ac91535c6b3184a0e13dd8cc5fca278ec66e660aceaab6bfae7b079
- change-flow.skill, 22 files, 257909 bytes, sha256 97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0
- flowmaster-validate.skill, 31 files, 315534 bytes, sha256 5ffa13f101db9108cdec356ce638ee0d67fa4c8a5eb2f7952bc13a2e220d3db4
- glow-hde-pr-development.skill, 4 files, 22414 bytes, sha256 3292e348febe0136f1d4b6768238be95e2b7b3e529c00595fcf14366016b1d6a
- session-relay-flowmaster.skill, 5 files, 56330 bytes, sha256 30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b
- tw-flowmaster.skill, 2 files, 20368 bytes, sha256 db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf
Rollback packages, built from today's installed trees, are in /tmp/claude-0/pkg/rollback/. They
are not under review. The round-a1 packages in /tmp/claude-0/pkg/new/ are superseded and are not
under review either.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Round a1: SKILL_REPAIR_REQUIRED from both reviewers (SFR-A1-1, SFR-A1-2), bound to the a1 digests
(amthor db6c4807…, change-flow a1170af8…, flowmaster-validate 3ebce735…, PR skill c77f624f…,
relay bfe6b8c6…, tw bdb73141…). Their records are SECTION-10-REVIEW-a1-SFR-A1-1.md and
SECTION-10-REVIEW-a1-SFR-A1-2.md in the evidence directory. Nothing in them carries to these bytes:
every measurement they report was made on other bytes. Read them for the findings, not the results.
What each finding became (repair script repair-a1/apply_repairs_a1.py and pin_repairs_a1.py;
must-fail regressions repair-a1/regress_repair_a1.py; commit 32e04d4):
- F1 (both reviewers; missing matrix digest-line check) -> new check FMV-ORACLE-018: the matrix must
  carry exactly three `source_row_sha256:` lines, one directly after each JSON block, each equal to
  that block's oracle row digest. Regressions T6, T6b, T7.
- SFR-A1-1 F2 and SFR-A1-2 V1 (re-stamped changes to successor-row fields, row positions, and
  non-row oracle keys) -> FMV-ORACLE-019 (per-row allowed-change field sets and historical
  positions) and FMV-ORACLE-020 (non-row top-level keys equal history; required_global_tokens
  differs only by the profile id in place; authority adds only the three successor keys).
  Regressions T1, T3, T3b, T3c, T5.
- SFR-A1-2 V2 (fallback predicate has no skill-text guard) -> required literals in
  validate_glow_hde_pr_development.py and the relay/tw CONTRACT_REQUIRED lists. Regressions
  R-FB-SKILL, R-FB-ALL, R-FB-DISPATCH, R-FB-CONDITIONAL.
- SFR-A1-2 V3 (stale alias prose, S-5) -> prose corrected in flowmaster-validate/SKILL.md and the
  FMV-GCF-CURRENT-FIXTURE-001 evidence text. Wording only.
- SFR-A1-1 F3 (Nathan-mediated double PR-40 dispatch) -> Nathan approved ("ok") the D23 successor
  "PR-40 is entered once per merge (D23-E)" in gcfpe.decision-record.md. Its sentence, "PR-40 is
  entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise the
  fallback block. Once either has been pasted, the other is void.", is appended to C-DISPATCH at
  every skill site that carries it, and is a required literal. Regressions R-ONCE, R-ONCE-VOID,
  R5-SITES.
Consequential expected-set changes in the E2 regressions (e2/regress_oracle.py): G2 and G3 now
expect FMV-ORACLE-018 beside FMV-ORACLE-012 / 013, because the mutated row digest no longer
matches its matrix line. G11 keeps the settled four-finding set both a1 reviewers accepted.
The E3/E4 gate was re-run on the repaired text: evidence/e3/E3-E4-report.md revision 4 (commit
7572af0).

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
The baseline is the installed synced tree
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502.
Its freeze.py digests (docs/prompt_ecosystem_management/freeze.py <dir>):
  flowmaster-validate 29 b9ca212a…, change-flow 21 80e877c2…, glow-hde-pr-development 4 e109d47a…,
  session-relay-flowmaster 5 4ef8daa3…, amthor-workspace-governance-audit 15 6cd088a0…, tw-flowmaster 2 fa3fac85…
  (full values: execution spec v2 §2).
Repaired a2 trees, once extracted: flowmaster-validate 31 a00cccbf…, change-flow 22 1186283d…,
glow-hde-pr-development 4 6382ead5…, session-relay-flowmaster 5 15aef989…, amthor 15 87201ab5…,
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
  reproduces the whole E2 stage), repair-a1/ (run_repair_a1.sh reproduces the repair and its
  regressions), e3/ (body_rules.py, run_e4.py, E3-E4-report.md), and preflight-2026-09-23.md.
- The successor matrix: docs/prompt_ecosystem_management/r1-successor-source-20260923.md.
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. The six packages carry, exactly, the §8a/§8b edits, the §5 successor oracle, map and matrix,
    the §6 contract 4.1.0 and the pins of spec v2, plus the round-a1 repairs of §2 above, and
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
    FMV-ORACLE-018/019/020 enforce that under a full re-stamp.
C7. The gate passes (spec §9; §E rows E1–E4; E3-E4-report.md revision 4).
C8. Each round-a1 finding is closed as §2 states, and PR-40 is entered at most once per merge in
    every skill text that carries C-DISPATCH.
Authority: Nathan's approval of Amendment 1 ("yes", 2026-09-23), his G06 ruling ("yes"), his
approval of the once-per-merge sentence ("ok"), and the D23 notes quoted there.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The round-a1 repairs themselves: FMV-ORACLE-018/019/020. Can you still pass a re-stamped
    unauthorized change to the oracle or matrix? Try what the a1 reviewers did not.
A2. The successor oracle's provenance (§5): matrix bytes, the digest formula, the authority block,
    N1–N10 and FMV-ORACLE-017. Could a third row change pass unnoticed?
A3. The once-per-merge sentence and the fallback-predicate literals: is either missing at a site
    that carries C-DISPATCH or the fallback, and does deleting either fail? Is any double-dispatch
    or no-dispatch path left?
A4. The regenerator's contract-only value table (§6): wrong or stale values that no check reads.
A5. Every reversed validator literal. Does its replacement still guard the kept rule? Is the
    old text forbidden, and does injecting it fail?
A6. The GCFPE override of the Flowmaster core option to create a session, in change-flow, the
    relay and tw-flowmaster; and the relay's provisioning line scoped outside GCFPE stages.
A7. The author's own choices in spec §12 and its addendum, the G2/G3 expected-set change, and
    G11's four-finding expected set.
A8. Whether any edited skill line now contradicts a kept rule: no agent merge, no polling, one
    handoff block, PR-40's independent verification, single Proceed within a plan.
Question, not a finding: is anything in these packages outside Amendment 1's scope, the a1
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
     site of the once-per-merge sentence.
  g. Write at least one must-fail probe of your own against FMV-ORACLE-018/019/020 under the full
     re-stamp that regress_oracle.py uses, and report its result.
Derive every digest from the artifact in front of you. Never transcribe one from the report.
The author's measurements, for you to contradict rather than confirm: every suite above passes;
the fixtures give 228 cases with 0 failed; the historical outputs are byte-equal to baseline; the
routing surface is fecc319b…/284; the repair regressions are 17 of 17 exact.

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
explicitly; a question is not a finding. State for each round-a1 finding whether §2's disposition
closes it on these bytes.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
