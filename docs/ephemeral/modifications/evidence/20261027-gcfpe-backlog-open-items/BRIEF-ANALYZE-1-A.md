# ANALYZE review brief, round 1, reviewer A

Filled from the canonical *ANALYZE and PLAN review brief* in `docs/prompt_ecosystem_management/reviewer-prompt-template.md`. Sections 3, 5 and 6 are copied byte for byte by script. Committed before the reviewer is spawned (D24 condition 2, D26-A).

**Supplement outside the fixed text (MB-006):**
- Also read `AGENTS.md` (the canon-first rule; the code review guidelines) and decision record D27 to D29.
- Resolve canon from `docs/pfcanon/` at that commit, which equals `main` @ `44dba78`.
- PF10 front matter §6 forbids reading any PF10 base version older than v13.8.9, including through git history.
- Read prompt bodies live in Notion, read-only: the member URLs are in `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`.
- Keep no body on disk beyond the read in hand (D22), and say in your record which pages you read.

```plain text
You are REVIEWER-ANALYZE-1-A, reviewing ANALYZE of MODIFICATION-20261027-gcfpe-backlog-open-items. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A).

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, local checkout /home/user/glow-hdengine-v2, branch
claude/cool-bardeen-zwduzl, commit 4780f64aa2909d40fb3e8c4e77165567f6e23342. Read that commit, not the branch head.
The record: docs/ephemeral/modifications/MODIFICATION-20261027-gcfpe-backlog-open-items.md, section §A.
Its evidence: docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/
(closure.md, scope-measurement.md, findings.md, worker-brief.md, typesafe-plan.md). Its governing documents: docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md.
The dry run that preceded you: the record's reviews ledger, entry 1, and §A.10; it passed with no
defect in the analysis open.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1  All 28 open backlog entries are still live in GCFPE-20261009.1 / 100926.1, wholly or in part; none is
    refuted outright. MB-028 already holds in practice for TW (§A.3).
C2  PF10 v13.8.9 carries no addenda. Each rule the entries cite now lives in permanent canon (PF04 v2.8.8
    §9.7.7 and §9.1.3; PF06 v2.5.5 §1.1.4 and §3.5.1; PF19 v3.0.7 §3.1.3 and §3.4.3; PF27 v2.0.6), or reached
    no permanent home (2.3; parts of 2.11; 2.27 and 2.28; 2.31's interim route; 2.34) (§A.2, §A.3).
C3  Scope is measured by broad match minus exceptions: MB-010 is 95 lines on 23 pages; 0 of 56 pages carry
    the drained finding or business-case rules; 0 pages name Codex; the provenance clause is on 55 pages
    (§A.5, scope-measurement.md).
C4  The 32 items sit in 25 parts, each part one rule across its surfaces, with the classes in §A.4. A-1's
    reading: edits land on candidate successor pages under D23-G, so each part is classed by the rule it
    applies, not as Class A for touching a selected member; Nathan's promotion touches the selected release.
C5  The gate tier is 2 (the prompt parts reach 50 of 55 members; PART-13 changes the shared contract).
C6  CD-1 to CD-15 are evidence-determined applications of existing rulings or canon, which ecosystem-change-
    management.md §6 gives the coordinator; none decides a policy question.
C7  Exactly twelve decisions are Nathan's (DN-1 to DN-12), each with options and a recommendation.
C8  Readiness is SPLIT_RECOMMENDED for PART-23 alone (unmeasured scope); there is no sequential discovery;
    interaction cost 23, range 21 to 28; the estimate is PLAN 10-16 h, EXECUTE 24-40 h.
C9  J-1 to J-14 are outside every taken entry's rule, so leaving them out splits no rule (D12).
C10 The PLAN session's TypeSafe reading is recorded as the skill printed it, with no Notion row and no agent
    recommendation (PF04 §9.1.3; GCFPE-MGMT-10 Result routing).

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
A1  A-1 and DN-1. Does anything in D23-G, its successors, D27, D29, the register's Release rule or the
    GCFPE-MGMT-10 body let a selected member be edited in place, which would make the successor-release
    reading wrong? Is classing each part by its rule, rather than as Class A, a silent breach of the
    MGMT-10 body's PLAN rule ("if it is a selected release member the change is Class A")?
A2  PART-04 and DN-3: can PF06 v2.5.5 §1.1.4's Real input bullet bear the reading offered in option (a)?
    And PART-03/CD-14: are PF04 v2.8.8 §9.7.7's gates quoted and applied correctly?
A3  CD-1: is DOC-20 -> PR-40 always a second entry for the same merge? Read DOC-20.json, PR-40.json and the
    DOC-20 body. Does removing the edge leave the missing-acceptance case a lawful route?
A4  CD-4: may a Product Owner direction recorded in a closed change's records (MB-024, 2026-10-13) be
    applied as an existing ruling, with no D-number?
A5  MB-010's count: the stated test and the 13 lines read in context (scope-measurement.md §2). Re-run the
    test on two or three bodies you fetch yourself.
A6  PART-13: are the CL-05 installation surfaces complete (graph, global.json, R1, both packages' pins,
    controls, the Flow Map under PF04 §9.1.6)? Can an ANALYZE approval authorize R1 successor rows, as DN-2
    option (b) says (precedent: D23's Amendment 1 successor)?
A7  ITEM-31 and ITEM-32 are derived, not taken from an entry. Do they breach ANALYZE's "Must not ... widen
    the request into adjacent work"?
A8  The interaction-cost arithmetic and the split table (§A.8).
A9  Is any J-item in fact the same rule as a taken item, so that leaving it out splits a rule?
Not exercised by the dry run: 114 of 166 Notion quotes rest on the verifiers' capture alone; PART-03's
seven author prompts were not read; no body was fetched fresh for MB-007, MB-009 or MB-011.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/REVIEW-ANALYZE-1-A.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
