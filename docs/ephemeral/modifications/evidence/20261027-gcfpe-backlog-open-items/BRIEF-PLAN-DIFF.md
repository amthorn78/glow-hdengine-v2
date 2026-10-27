# PLAN repair DIFF_CHECK brief — reviewer C

You are REVIEWER-PLAN-DIFF-C, checking the repair of MODIFICATION-20261027-gcfpe-backlog-open-items's PLAN after full review 1. You did not author it, and you were not reviewer A or B.

This is the one bounded check of the repair's diff that D26-A allows after a FULL round. It is not another FULL review. The rubric and the cap are the fixed text in the committed `BRIEF-PLAN-1-A.md` (§3 and §5) in this evidence directory. Apply them as written.

**What to check.** The repository is at `/home/user/glow-hdengine-v2`. Check only this diff, using these commits and not the branch head:

    git diff f2346b2 885638d

The diff also carries two files that are not the repair: `typesafe-execute.md` (the EXECUTE session's TypeSafe reading) and the ledger entry for round 1 in the record's frontmatter. Read them only for contradictions with the repair.

- **Canon:** `docs/pfcanon/` at those commits, which equals `main` @ `91925e9`. PF10 is v13.9; read no older PF10 base version, including through git history. Read PF06-Canon-Change-Process-Guide v2.5.5 §0.1A where the repair touches the register's or the Hub's PF10 boundary text.
- **Governing:** `AGENTS.md` (the canon-first rule); `docs/prompt_ecosystem_management/modification-template.md` (rules 1, 4 and 8, and §P); D26 and D30 in `gcfpe.decision-record.md`; the record's §A.13 (L-C1) and §A.14 (Nathan's approval: "All other listed findings are accepted as risks"); `plan/coordinator-decisions.md` C-15, C-22 and C-23 to C-26.
- **Tools:** you may run the plan's tools from a scratch copy of the commit (`git worktree add` or `git archive` into `/tmp/...`), with `PYTHONDONTWRITEBYTECODE=1`. Never apply an edit to the real tree, and write nothing to Notion. Read Notion pages read-only if you need them (Hub `3ce4590a05eb814f8892f88ff8539308`, register `3d24590a05eb81ce942ad994cfca9fa1`, IA-30 `3f44590a05eb81c6bfb5f36f7df8f464`); keep no body on disk beyond the read in hand (D22).

**The four required findings being repaired.** They are in `REVIEW-PLAN-1-A.md` (R-1, R-2) and `REVIEW-PLAN-1-B.md` (R-B1, R-B2).

- **R-1 (R1, R4).**
  - **Finding:** X1's and X26's repository edits had no committed applier; W1's PART-02 note was stored anchored before D30; the `repository` and `notion-control` guards ran only on fixtures, so X8 would pass with a surviving retired line.
  - **Repair (C-23):** `plan/repo_edits_102726.py` (apply, check, selftest); `activation_render_102726.py`'s part17 phase runs the notion-control guards on the reads; dry-run gates N10 part17, N11 and N12; X1, X8 and X26 name the commands.
- **R-2 (R3).**
  - **Finding:** L-C1, which Nathan accepted as a risk, was repaired without his opt-in in W2-IA-30-BC-2, D30-A and G-W2-EM-2, and D30 stated it as his ruling.
  - **Repair (C-24):** reverted to the frozen per-work-unit cut through the assemblers; D30-A's delta bullet and its tested-guard description corrected in place on the unmerged branch, disclosed in §P. G-W2-BC-4 followed BC-2.
- **R-B1 (R1).**
  - **Finding:** the X17 post-flight would pipe raw fetches to the shipped validator and the registry assertions, outside C-15's normalized form.
  - **Repair (C-25):** X17 names `plan/normalize_fetch.py` as the form, and the reviewers run `x12_qualify_102726.py` and `registry_assemble_102726.py assertions` on their own reads.
- **R-B2 (R2).**
  - **Finding:** C-REG wrote "pull request #768" on the register.
  - **Repair (C-26):** the link is `@CONTROLS_PR`, recorded at X1 and filled at X9; unfilled, it is refused.

**Questions to answer.**
1. Is each of the four fixed?
2. Did the repair add a new required defect (R1 to R4)? Look above all for:
   - a check the repair added that cannot fail, or that fails on a correct result (the new X8 refusal when a guard's before-count differs from W6's measurement on a volatile page);
   - an edit applier that could write the wrong span silently, or apply to the real tree;
   - D30's in-place correction: does D30 now state exactly Nathan's DN-3 (b) for ITEM-15 and ITEM-17 and nothing wider, and is the correction disclosed?
   - `@CONTROLS_PR` and the existing `@PROCEDURE_PR`: two markers for one pull request.
3. Does any changed text contradict unchanged text elsewhere: §P's step table, PLAN §5, §10's accepted risks, or the ledger entry?

**Deliverable.**
- Write a new record to `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/REVIEW-PLAN-DIFF.md`.
- First line: the count of distinct confirmed REQUIRED findings.
- Then:
  - the disposition of R-1, R-2, R-B1 and R-B2 (fixed, not fixed, or fixed with a new defect);
  - each new REQUIRED finding, with its rubric class, exact text, evidence, smallest correction and whether it is in repaired text;
  - each LISTED finding, one line each;
  - the trend in the count (round 1: 4);
  - a short *Canon relied on* block.
- Do not edit the record under review, merge, install, write to Notion, or edit a prompt body. Write no other file.
- Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
