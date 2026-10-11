# PLAN review brief, round 1, reviewer B

Filled from the canonical *ANALYZE and PLAN review brief* in `docs/prompt_ecosystem_management/reviewer-prompt-template.md` (sections 3, 5 and 6 copied verbatim). Committed before the reviewer is spawned (D24 condition 2, D26-A). The two briefs differ only in the reviewer id, the record path and the order of the attack list.

```plain text
You are REVIEWER-PLAN-1-B, reviewing PLAN of MODIFICATION-20261011-gcfpe-mb008-to-promotion. You did not author it.
This is full review 1 of at most 2 for this mode (D26-A).

=== 1. WHAT YOU ARE REVIEWING ===
Repository amthorn78/glow-hdengine-v2, local checkout /home/user/glow-hdengine-v2, branch
claude/mb-008-modification-promotion-fdz2sn, commit 1b742bb84e42b5fdceb63eebcc2ba3b7cce0b15d. Read that commit (git show /
git cat-file), not the working tree or branch head.
The record: docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md, section §P and frontmatter
(§A is approved and frozen; read it for context; §A.12 records the six decisions DN-A to DN-F).
Its evidence: docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md (the plan's detail)
and plan/ (edits.json, guards.json, body_check.py, graph_assemble.py, release-values-100926.1.json,
make_profile_20261009.py, package-redlines.json, package_apply.py, patches/, dry_run.py, dry-run.json). ANALYZE evidence
in the same directory (scope-measurement.md, source-identities.md, body-scan.json, contract-probe.json).
Its governing documents: AGENTS.md first (canon-first rule); docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D17 and D20-D27, modification-template.md, ecosystem-change-management.md,
skill-packaging-and-delivery.md, postflight-procedure.md, notion-write-boundary.md, authoritative-surfaces.md,
prompt-corpus-policy.md; docs/ephemeral/gcfpe.promotion-20260921/PROMOTION-RECORD-20260921.md; and canon on main in
docs/pfcanon/: PF10-HDE-Build-Notes-v13.5.2.md (addendum 2.1, complete), PF04 §9.1.2, §9.1.3, §9.1.6, PF06 §0.1A,
PF27 "Canon precedence for template use".
The parent: docs/ephemeral/modifications/MODIFICATION-20261010-gcfpe-candidate-skill-analysis.md and its evidence
(findings.md, plan-successor-2/, execute/candidate-graph-parts/). The grandparent's non-derived registry proposal:
docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/execute/candidate-registry-nonderived.json.
Notion (read-only for you): the 55 candidate pages (ids in plan/edits.json), the MGMT-10 testing body
3e34590a05eb811b93d2da9b4ef8106d, the register 3d24590a05eb81ce942ad994cfca9fa1, the candidate inventory
3f44590a05eb8110aa69fe4189ad9abc, the 091426.1 Flow Index 3db4590a05eb81de9736ea69bac61016 and the five hubs named in
PLAN §7. D22 applies to your reads: no copies on disk beyond a transient read for one check, no hashes of bodies.
Installed skills (read-only; copy to scratch before running anything):
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/
The dry run that preceded you: plan/dry-run.json at 93bb9e36, nine gates all passing (identities; guards; 82 of 82 body
operations and 210 of 210 guard rows after on 55 fresh reads; audit-engine agreement; graph builds; the patched
regenerator reproduces the shipped 091426.1 contract byte for byte; the derived 100926.1 profile; 54 bodies pass its body
checks after the edits; 46 package redlines land). You can rerun it: the command is in plan/dry_run.py's docstring; it
reads the fetch records of the session that ran it, so in your session fetch the 55 pages first and pass your own time.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
C1. The 82 body operations, with the canonical text C-TYPESAFE (PLAN §3, PART-02), apply PF10 2.1 rules 2-4 and PF04
    §9.1.3's surface advice inside D23's C-PLACE, C-ART and D23-B and DN-B option 2: afterwards no candidate body forbids the
    reading or the surface advice, and nothing about either goes inside the NEXT_PROMPT_HANDOFF block.
C2. The 14 guards catch surviving old text (broad match minus named exceptions) and prove each repair present; the insertion
    support added to the parent's body_check.py is correct (landing, batch safety, a re-send refused or caught).
C3. PART-03 completes F05 in the bodies; the ESC-25 and ESC-30 "Never ... allocate PF10 numbering" sentences are the
    permitted nonproducer exception.
C4. The 46 package redlines apply D27 (F01, F02), F04, F05, F07 under PF10 2.1, F08 and MB-003 without breaking ruled
    behaviour; the immutable R1 oracle stays byte-identical and mapping its Kronos token like its revision token is lawful.
C5. F06: the glow-graph-contract patch derives release identity from the graph and leaves the 091426.1 contract unchanged
    (byte equality); release-values-100926.1.json holds only true literals; make_profile_20261009.py changes only release
    pins plus the F05 format check and the PF10 2.1 body check.
C6. Bundling the production build (lifecycle literals flipped, nothing else) is correct and avoids the 2026-09-21 open
    activation delta; the candidate and production contracts differ only in lifecycle fields and the graph digest.
C7. PART-05: the MGMT-10 successor's body operations, graph part (four results, one terminal-return edge), registry row,
    parent placement under the 091426.1 Flow Index, and DN-D's bounded rescope are correct.
C8. PLAN §7 follows D17's order and the register's own rules; updating the hubs and Flow Index in place and creating a new
    selected catalog are right; the 57-page archive set is complete and moves nothing a successor depends on; PLAN §8 lists
    every Notion write EXECUTE makes, as notion-write-boundary.md requires.
C9. EXECUTE's normal path is mechanical, each step with a verification that can fail; the dry run reproduces.
C10. The open findings and disclosed deviations are complete, and nothing outside the frozen nine items is added.

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
A1. C5: reproduce the byte equality yourself (scratch copies, PYTHONDONTWRITEBYTECODE=1: apply
    plan/patches/glow-graph-contract-mb008.patch with patch -p2 to a copy of glow-graph-contract, build docs/graph/parts,
    run contract_recipe.py with --check against both bundled 091426.1 contracts). Then test the derived 100926.1 values:
    page ids from URLs, staged parents against the pages' actual Notion parents, the named prompts, the lifecycle values in
    candidate and production mode, and each literal in release-values-100926.1.json against its stated source.
A2. C6: whether the validator's own rules (release_semantic_view, CONTRACT_LIFECYCLE_KEYS, PRODUCTION_SELECTION_EVIDENCE,
    the production-mode bundle comparison in validate_package) accept the production build and still check what matters;
    whether shipping SELECTED_PRODUCTION bytes before the register selects them breaches D17 or any other ruling.
A3. C8: PLAN §7 against D17, the register's text (read it), the 20260914.1 register entry, authoritative-surfaces.md's sweep
    rule and notion-write-boundary.md. Is anything a successor depends on in the 57-page archive set? Does any EXECUTE or
    PART-08 write lack its line in PLAN §8?
A4. C5 and C9: the validator change list V1-V7 and the PR-development validator changes. Search the six packages for
    anything else pinned to 091426.1, 3.3.1, 3.3.2, 1.3.1, 3.2.0 or 1.13.0, or to the redlined phrases, that the plan does
    not name and that would make X9's gates fail.
A5. graph_assemble.py: the measured proofs, the carried observed_pf10_producers, the flip, and whether check() could pass a
    wrong part.
A6. C9: any EXECUTE step whose verification cannot fail, or whose failure is not a stop.
Not exercised by the dry run: the Notion writes themselves; the MGMT-10 duplicate (the dry run used the testing page's URL as a stand-in) and its M-HEAD/M-TS; the PLAN document's own digest (stood in by edits.json's); the package build beyond the redlines, the patch and the derived profile (the 100926.1 fixtures, the derived fixtures runner and change-flow validator, V1-V7, the docs); the D24 review; the candidate registry assembly; the post-flight; the promotion transaction. Questions about them are questions, not findings, unless the plan as written would make one of them fail or go silently wrong.

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/REVIEW-PLAN-1-B.md. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
