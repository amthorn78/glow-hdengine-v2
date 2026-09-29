2 distinct confirmed REQUIRED findings

GTWPE-FIRST-REPAIR-PLAN-DC. This is the PLAN diff check of MODIFICATION-20260929-gtwpe-first-repair: e7e4d4c..bba16f9, under docs/ephemeral/modifications/. I followed the fenced block of DIFFCHECK-BRIEF.md at 602abcb. That block is 5,544 bytes without its final newline, sha256 af41f422…4317a, which matches the file's own statement.

What I did and did not do:
- I wrote nothing and ran no script.
- I changed no git state and made no Notion, GitHub or agent call.
- I read with git show, git diff, git log, git grep and `git config --get`, and I measured with grep, sed -n, wc and sha256sum.
- I did not re-run P2. My answer to A2 is reasoned from git's push and lease rules.

Both required findings are in text the last repair added. Both were refuted first and still stand.

## REQUIRED

**DC-1 (R3). Failure path, before the merge: the "record-only" pull request is X2's own pull request, and the plan has Nathan close it.**
- **Text:**
  - Step 4: "If PART-02 must not land, he says so; the session then restarts the branch from `origin/main` with X5's commands, commits the failure record alone, and opens a record-only pull request, and only then does he close the branch's first pull request unmerged."
  - PO-5: "merge the pull request that carries the failure record; if PART-02 must not land, close X2's pull request unmerged once the record-only one exists".
  - X2's rollback points to step 4.
- **Evidence:**
  - X5's commands name this Modification's own branch: `git checkout --no-track -B docs/20260929-modification-gtwpe-first-repair origin/main` and `git push --force-with-lease origin docs/20260929-modification-gtwpe-first-repair`.
  - On this path, X2's pull request is open on that branch. Step 1 says: "before X3, the branch's own pull request carries it, opened then if X2 has not opened it".
  - A pull request follows its head branch. The force-push therefore makes X2's pull request itself the record-only one.
  - GitHub allows one open pull request per head and base, so a second cannot be opened. That refusal is loud.
  - The plan then orders Nathan to close "the branch's first pull request unmerged". That pull request is now the only one carrying the failure record, so "merge" and "close" name the same pull request.
  - P2 tested git in scratch repositories, not pull requests.
- **Refutation tried:** the record would survive if a different branch were used, or if Nathan closed X2's pull request first. But the text names X5's commands, which name this branch, and it puts the close after the new pull request exists.
- **Path, likelihood:** failure path. It needs a stop after W1 and before the merge, and Nathan ruling that PART-02 must not land. Low likelihood, but certain once on that path.
- **Consequence:** if Nathan follows the order given, the failure record never reaches `main`, and nothing tells him. This silently breaches `D26-B` step 1 and the plan's "in every case". It is the outcome RB-3 was required for.
- **Smallest correction:** in step 4 and PO-5, say that the restart makes X2's pull request carry the failure record alone (its title and body updated), and that Nathan merges it. Drop "close the branch's first pull request unmerged". Alternatively, Nathan closes X2's pull request first, and then the session restarts the branch and opens the new pull request.
- **In text the last repair added:** yes (repair 6).

**DC-2 (R4). After W4 has landed, PO-5 still has Nathan archive «NEW», although nothing reverses W4.**
- **Text:** PO-5 reads "Only after a failure: archive «NEW»; … have W4 reversed from its readback only if X4.2 or X4.3 failed". Three new texts say otherwise:
  - step 4: "Before X4, he archives «NEW»" and "A failure at X5 reverses no Notion write";
  - X5: "it reverses no Notion write";
  - step 4: "W4 is reversed only when X4.2's or X4.3's own check failed".
- **Evidence:**
  - Take a failure at X5, or a stop at X4.2 or X4.3 on a tool error rather than its own check (RB-5's path). If W4 has landed, it stays, and the catalog selects «NEW».
  - PO-5 is the plan's list of Nathan's actions. It conditions its other clauses but not the archive, so it tells him to archive the selected page. Step 4 tells him not to.
  - Before the repair the two agreed, because every failure after W4 reversed W4 before «NEW» was archived.
- **Refutation tried:** the session's return follows step 4, which asks for no archive after X4. But PO-5 is the standing, approved list of his actions.
- **Path, likelihood:** failure path; low.
- **Consequence:** the selected GTWPE-MGMT-10 version is archived while the catalog still links it. Nothing says so. This is RB-5's outcome, reached again through PO-5.
- **Smallest correction:** PO-5 reads "archive «NEW» if the failure came before X4, or once W4 has been reversed".
- **In text the last repair added:** yes. PO-5 was rewritten by repair 6, and the no-reversal sentences were added by repair 1.

## LISTED
Each line gives: path | likelihood | consequence | in new text?

- **DL-1.** Step 4's restart before the merge "commits the failure record alone". The evidence files the record cites do not reach `main` with it: PLAN-REVIEW-A.md, PLAN-REVIEW-B.md, PLAN-REVIEW-BRIEF.md, edits.json, phrases.json and EXEC-READBACK*.md. Only the tool needs leaving out. | failure | low | the evidence stays on abandoned commits | yes
- **DL-2.** W4 is reversed "only when X4.2's or X4.3's own check failed". A tool error at X4.2 (RB-5's path, where K-3 allows a partial W4) therefore has no reversal instruction. This is also more than RB-1's X5-only correction asked for. | failure | low | loud: the sweep records the catalog | yes
- **DL-3.** Step 1 has two cases, "before X3" and "after the merge X3 detects". Neither covers a failure at X3's own blob check after a real merge, and a failure record pushed to a merged branch reaches no `main`. | failure | low | loud | yes
- **DL-4.** A failure in X5's own push or pull-request step is handled by rerunning "X5's commands". | failure | low | loud repeat | yes
- **DL-5.** The 4-hour stop after W1 is not a failure-path stop, and no step commits or pushes the record at it (LA-11, still in K-15). | failure | low | loud | no
- **DL-6.** E11's second check phrase covers RB-4's addition only. RA-4's own clause, "and for a TW-ALPHA member on TW's current release", has no check phrase (LA-3/LB-3's class). | normal | low | missed only if W3 altered that clause | yes
- **DL-7.** E11's "and each page the record of TW's latest selection says it wrote" sits in the clause that governs every prompt change, and it does not say where that record is found. | future normal | low | extra fetches for changes to prompts outside TW-ALPHA, or reliance on search | yes
- **DL-8.** E12 excludes waits for "Nathan's approval, a merge or an install". §A's estimate and K-12 name only the merge, and PO-1 does not name the widening (as LB-5). | normal | certain | a wider exclusion than the analysis proposed, visible to Nathan | yes
- **DL-9.** X4.1 still uses 092926.1 "as fetched at the start of EXECUTE", although X3 now fetches it whole. A compaction, or a fresh session at X3, leaves only X3's fetch. The body is identical, since X3 checks its edit time. | resume | low | interpretation only | yes
- **DL-10.** P5 says D2's counts stand, but D2's check that no check phrase occurs in 092926.1 did not cover P20 or P22. | normal | very low | a loud stop at X1.10 | yes
- **DL-11.** K-15 imports LA-4 (P73), LA-23 (P69), LB-2 (P58) and RA-3 (P20) with e7e4d4c's phrase numbers. After the renumbering those numbers name other phrases (the intended ones are now P75, P71, P60 and P21), and K-15 does not say so. | normal | certain | a misleading reference if Nathan opts in to one | yes
- **DL-12.** Take a failure before X3 with PART-02 intact. PO-5's "merge the pull request that carries the failure record" then lands the tool without X3's gates being run from `main`. | failure | low | the tool is checked only on the branch (X1.4) | yes

## The seven, and the trend

| # | Finding | Disposition |
|---|---|---|
| 1 | RA-1, RB-1 | Fixed. PO-5 contradicts its new no-reversal sentence (DC-2) |
| 2 | RA-2, RB-2 | Fixed |
| 3 | RA-3 (LB-1) | Fixed (DL-8) |
| 4 | RA-4, RB-4 | Fixed (DL-6, DL-7) |
| 5 | RA-5 | Fixed (DL-9) |
| 6 | RB-3 (LA-9) | Fixed with a new defect: DC-1, and DC-2 in PO-5 |
| 7 | RB-5 | Fixed in its own text; its outcome is reachable again through PO-5 (DC-2) |

- **Trend:** 7 distinct required findings fell to 2, which is at least a halving.
- **D26-A rule 5's second stop signal is met:** both required findings, and 11 of the 12 listed ones, sit in text the last repair added.
- **Next:** under D26-A rule 2 no further round follows. The plan goes to Nathan with DC-1, DC-2, DL-1 to DL-12, and K-15 to K-17 still open.

## The claims
- **C1:** met for repairs 1 to 5 and 7. Repair 6 introduced new defects (DC-1, DC-2).
- **C2:** not met (DC-1, DC-2).
- **C3:** holds, except DL-2's narrowing of when W4 is reversed. K-15 to K-17 keep every listed finding, and every other change is a count or ledger entry the repairs imply.

## A1 to A5
- **A1: every stop after W1, and contradictory instructions.**
  - Every failure-path stop after W1 now sends a record to `main`, with one exception: the stop before the merge where PART-02 must not land (DC-1).
  - Two stops remain uncovered, both loud: the time stop (LA-11) and a failure at X3's blob check after a merge (DL-3).
  - Nathan is given contradictory instructions on two paths: DC-1 and DC-2.
- **A2: X5's new commands.** They work whether the remote branch was deleted or kept:
  - Deleted: the prune removes the tracking ref, so the lease expects the branch to be absent, and the push creates it.
  - Kept: the lease equals the freshly fetched value.
  - Here the local branch tracks `origin/docs/20260929-modification-gtwpe-first-repair`, and `push.default` and `autoSetupMerge` are unset. The push names its remote and branch explicitly, so any upstream the local branch still tracks is irrelevant. The check fetches the branch by name.
  - The checkout keeps the modified record because HEAD and `main` hold the same record blob, which X3 established. The save and write-back cover it anyway.
  - The same commands, reused by step 4 before the merge, collide with X2's open pull request (DC-1).
- **A3: E11 and E12.**
  - E11 fixes RA-4 and RB-4, and E12 fixes RA-3.
  - The two new check phrases, P20 and P22, each occur in their own new text and in no other new text or phrase. edits.json holds each twice: in the new text and in check2.
  - Remaining listed points: DL-6, DL-7, DL-8, DL-10.
- **A4: X2's commit and X4.1's search.**
  - X2 now commits the record and EXEC-READBACK.md ("when written") before its checks. It verifies with `git show --stat HEAD` and the pushed blobs.
  - This is consistent with X1.12: its "commit nothing new" belongs to its own step, and its refusal branch writes no file. It is also consistent with X3's blob comparison.
  - X4.1 searches «NEW» as X3 fetches it, after X3 confirms «NEW» is unedited since X1.10 (DL-9).
- **A5: phrases.json and EXEC-READBACK-BRIEF.md.**
  - phrases.json holds 75 phrases: 44 expected once, 1 expected four times and 30 expected absent (45 present, 30 absent).
  - P20 and P22 are inserted. The old P20 to P73 are renumbered P21 to P75 with their texts unchanged.
  - The brief lists 75 lines and holds no count.
  - §P's counts are updated in the evidence table, X1.10 and X1.12. D8 keeps 73 as the dry run's history (DL-11).

## Canon relied on
- **`AGENTS.md`, read first:** the canon-first rule; PF canon is read-only; the rule on truncated reads (the brief block was verified by byte count and hash).
- **HDE Governance (PF04) v2.8.6 §9.1.6:** read in full on `origin/main` at `fffadb5`.
- **HDE Build Notes (PF10) v13.5, 2.38 PF10-AINEUTRAL-001:** read in full at `fffadb5`. I also searched PF10's list of addenda for related rules; none bears on this diff.
- **In flight, at bba16f9:**
  - the record's front matter, §A (items, scope, risks, Q1, readiness) and §P, whole;
  - the diffs of edits.json, phrases.json and EXEC-READBACK-BRIEF.md;
  - EXEC-READBACK-BRIEF.md, PLAN-REVIEW-A.md and PLAN-REVIEW-B.md, whole;
  - DIFFCHECK-BRIEF.md at 602abcb.
- **Governing documents:**
  - `gcfpe.decision-record.md`: D26 in full and D21's rulings;
  - `modification-template.md`: rules 1 to 8 and the §P guidance;
  - `ecosystem-change-management.md`: EVID-001, DISP-001, §5 and part of §6.
- **Not read:**
  - D20 and D22 to D25;
  - `reviewer-prompt-template.md`;
  - the tool and guard_proof.py, which the diff leaves unchanged;
  - GTWPE-MGMT-10's body, by instruction; no Notion access was made.

DECISION NEEDED
