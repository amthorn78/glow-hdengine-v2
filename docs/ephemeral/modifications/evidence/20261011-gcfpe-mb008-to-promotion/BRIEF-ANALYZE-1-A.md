# ANALYZE review brief, round 1, reviewer A

Filled from the canonical *ANALYZE and PLAN review brief* in `docs/prompt_ecosystem_management/reviewer-prompt-template.md` (sections 3, 5 and 6 copied verbatim). Committed before the reviewer is spawned (D24 condition 2, D26-A).

```plain text
You are REVIEWER-ANALYZE-1-A, reviewing ANALYZE of MODIFICATION-20261011-gcfpe-mb008-to-promotion. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A).

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, local checkout /home/user/glow-hdengine-v2, branch
claude/mb-008-modification-promotion-fdz2sn, commit 978d233e228bc88c77bbc8148117da7c2613c02d. Read that commit
(git show / git cat-file), not the working tree or branch head.
The record: docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md, section §A and frontmatter.
Its evidence: docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/ (scope-measurement.md,
body-scan.json, closure-candidate.md, contract-probe.json, source-identities.md, worker-brief.md).
The parent it starts from: docs/ephemeral/modifications/MODIFICATION-20261010-gcfpe-candidate-skill-analysis.md and its
evidence directory (findings.md, PLAN-SUCCESSOR-1-20261011.md, PLAN-SUCCESSOR-2-20261011.md, plan-redlines.md).
Its governing documents: AGENTS.md first (it governs; canon-first rule); docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D20-D27, modification-template.md and ecosystem-change-management.md; and canon on main in
docs/pfcanon/: PF10-HDE-Build-Notes-v13.5.2.md (addendum 2.1, complete), PF04 §9.1.2, §9.1.3, §9.1.6, PF06 §0.1A,
PF27 "Canon precedence for template use".
The GCFPE-MGMT-10 testing body that governs this run: Notion page 3e34590a05eb811b93d2da9b4ef8106d (MODE = ANALYZE section
and the spine). The GCFPE Modification Backlog: Notion page 3e54590a05eb81eb818fd0f42045167a (MB-008).
Installed skills (read-only): /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/
The dry run that preceded you: the record's reviews ledger, DRY_RUN entry, 2026-10-11: 55 closure calls exit 0, both builds
reproduce, contract probe control 0/0 and candidate 62 in 8 classes, 13 digests reproduce, 8 of 8 sampled quotes verified,
validator 16/16.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. PF10 addendum 2.1 governs F07 and supersedes the parent's F07 redline; its rule 1 reaches every candidate member that
    emits a handoff (53 bodies), PE's authoring rules and five skills (change-flow, flowmaster-validate,
    glow-hde-pr-development, session-relay-flowmaster, amthor-workspace-governance-audit), not only the three MB-008 packages.
C2. Printing the reading beside the NEXT_PROMPT_HANDOFF block, not inside it, applies D23-B and PF10 2.1 together and needs
    no new ruling; the 23 in-block prohibitions stay valid; PR-50's two general prohibitions need no change.
C3. The body scan is complete for its classes: no page names TypeSafe or gives AI model advice; general prohibitions sit on
    PR-10, PR-20, PR-30, PR-35, PR-40, PR-50 and PE; the universal F05 numbering text sits on 9 + 5 member pages and PE.
C4. ITEM-04 (F05 surviving text) and ITEM-09 (MB-003) are within this Modification's request, not adjacent work it must
    not widen into; MB-010 (the D23-B sentence) is correctly kept out.
C5. F06 is measured: the shipped regenerator produces a candidate contract unchanged; the 091426.1 validator then reports
    62 release-bound expectations in 8 classes (control 0); glow-graph-contract probably changes because of the
    contract-only value table.
C6. Classes, tiers (gate_tier 2), parts, item statements and the interaction cost 19 are correct; readiness NEEDS_RULING
    with six decisions, and no split predicate holds.
C7. The six decisions DN-A to DN-F are genuinely the Product Owner's (canon searched and silent, or a ruling or policy is
    needed), and none of the recommendations would breach a ruling if adopted.
C8. Evidence retention complies with prompt-corpus-policy.md and D22.

=== 3. WHAT COUNTS AS A REQUIRED FINDING — FIXED TEXT, DO NOT EDIT ===
Only these are REQUIRED:
  R1  a defect on the normal success path;
  R2  a silent wrong edit to a prompt body, governed document or control page;
  R3  a silent breach of a Product Owner ruling, however unlikely;
  R4  a plausible path with a silent or destructive outcome.
A failure that ends in a loud stop and a return to Nathan is NOT required: list it as LISTED.
Everything else is LISTED. For each finding give its path (normal or failure), its likelihood, its
consequence, and whether it sits in text the last repair added. Refute your own findings first: a
finding you cannot reproduce from the committed text is not a finding.


=== 4. WHAT TO ATTACK, WEAKEST FIRST ===
A1. C3's completeness. Workers classified inline pages by reading, not by a mechanical count. Re-read a sample of
    candidate pages fresh from Notion (page ids are in body-scan.json) and look for a general model/reasoning/effort
    prohibition, an AI recommendation, a TypeSafe mention, or "no agent/the producer ... numbering" text the scan missed.
    Pages outside the PR lane and PE are the least examined. D22 applies to your reads: no copies, no hashes.
A2. C1 and C2: whether rule 1's scope really reaches every handoff-emitting member, whether "beside the block" satisfies
    rule 2 ("reported as the skill prints it") without contradicting D23-B or session-working-rules' "the block comes last",
    and whether PR-50's exception is right.
A3. C4: the line between this Modification's scope and adjacent work the MGMT-10 body forbids ANALYZE to widen into.
A4. C5: reproduce the probe if you can (scratch copies of the installed skills, PYTHONDONTWRITEBYTECODE=1); test whether the
    value-table claim (receiver_compatibility, EXPECTED_RECEIVERS) holds.
A5. C7: DN-D option D2 waives an MGMT-10 body boundary on Nathan's explicit authorization; DN-B option B2 needs a new
    destination rule. Check each recommendation against the rulings and policies it touches.
A6. C6: the cost arithmetic, the tier reasoning for skill-only parts, PART-05's class.
Not exercised by the dry run: the typesafe-scoring skill's fit to a GCFPE handoff; the promotion transaction; any package
build. These are PLAN's; a question about them is a question, not a finding.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.


=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/REVIEW-ANALYZE-1-A.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

Supplement outside the fixed text (MB-006): `AGENTS.md` asks every artifact to record the PF titles and sections relied on. Add a short *Canon relied on* line to your record after the deliverable it fixes.
