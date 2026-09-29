5 distinct confirmed REQUIRED findings

GTWPE-FIRST-REPAIR-PLAN-B, PLAN full review 1 of MODIFICATION-20260929-gtwpe-first-repair, commit e7e4d4cab7450d8574c1cc5066c47812005f84bb. I read the commit with git show only. I made one Notion fetch, of the GTWPE parent page. I wrote nothing and ran no script.

REQUIRED

RB-1. R1, normal path. Step X5.
Text: "restart the branch from `origin/main` (`git checkout -B docs/20260929-modification-gtwpe-first-repair origin/main`), write the saved record back, commit, `git push --force-with-lease`".
Evidence:
- This checkout runs git 2.43.0, with `push.default` and `branch.autoSetupMerge` both unset, so git's defaults apply. Under those defaults, `checkout -B <branch> origin/main` makes `origin/main` the branch's upstream. A plain push under `push.default=simple` then refuses, because the upstream's name differs from the branch's.
- Separately, if GitHub deletes the head branch when Nathan merges (§A *Consult*: the pilot's branch "was deleted after its merge"), the tracking ref is left stale, because X3 fetches only `main`. The lease is then refused.
- This repository has met both. closeout-residuals `plan/DECISIONS.md`, P-106: "`checkout -B … origin/main` made `origin/main` the upstream, so a plain `git push` could fail or target `main` (executability#11)". P-97 and `rca-20260924/defects-by-round.csv` R5-06: "force-with-lease push stale after remote branch deleted". It was fixed there as `git fetch --prune origin`, then `checkout --no-track -f -B … origin/main`, then `git push --force-with-lease origin <branch>`.
Likelihood: high, on every run with a merge at X2.
Consequence: the last step fails after W1 to W4 have landed and been verified. The plan then takes `D26-B` and returns `IMPLEMENTATION_BLOCKED`. Its *Failure path* step 4 and PO-5 would have Nathan reverse W4, undoing a correct selection because of a push error. The record at `COMPLETE` never reaches `main`.
Smallest correction: X5 runs `git fetch --prune origin && git checkout --no-track -B docs/20260929-modification-gtwpe-first-repair origin/main`, then later `git push --force-with-lease origin docs/20260929-modification-gtwpe-first-repair`. A failure at X5 is recorded and returned without reversing any Notion write.
In text the last repair added: no.

RB-2. R1, normal path. Step X2, and *How the plan runs*, X2.
Text: "push the branch; open its pull request", verified by "the branch's blob of the record equals the local file; the pull request lists the tool, the record and the evidence files".
Evidence:
- X1.5 is the last commit before X2. After it the record changes locally: X1.6 fixes «NEW», which *Values, fixed once and recorded in §E* puts in §E, and each step's disposition is added.
- X1.12 writes `EXEC-READBACK.md` and says to "commit nothing new".
- No step between X1.5 and X2 commits either change, so X2 as written pushes only X1.5's commit, and its own blob check fails.
Likelihood: certain as written. An executor that adds a commit is interpreting the step, against C1.
Consequence:
- As written, a loud `D26-B` stop after W1 to W3, with «NEW» archived.
- If the check were passed over, `main` at the X3 resume point would lack «NEW», «V», the clock and the readback capture. K-13 relies on all of them.
Smallest correction: X2 begins "commit the record and `EXEC-READBACK.md` (when written)", and its check names that commit.
In text the last repair added: no.

RB-3. R3, failure path. *Failure path* step 4 and the paragraph after it; PO-5; X2's rollback.
Text: the failure record reaches `main` only "in the branch's pull request … X2 opens it; a failure before X2 opens it then". Yet on a failure:
- step 4 has Nathan close that pull request unmerged "if PART-02 failed";
- PO-5 says, with no condition, "close the pull request unmerged";
- X2's rollback is "the pull request is closed unmerged".
After Nathan merges X2's pull request, a failure at X3, X4 or X5 has no pull request left, and no step restarts a branch to carry the failure record.
Evidence: this breaches `D26-B` step 1, "commit a failure record that reaches main, in a record pull request", and the template's §P, "a failure record committed to `main` in a record pull request".
Likelihood: low for a given run, since it needs a failure after W1. Once such a failure happens, it is certain.
Consequence: the failure record stays on a closed or merged branch and never reaches `main`. Nothing tells Nathan that closing the pull request drops it.
Smallest correction: every stop after W1 sends the failure record to `main` in a record-only pull request, from a branch restarted from `origin/main` with the RB-1 commands. X2's pull request is closed unmerged only when the tool must not land. Step 4 and PO-5 say which pull request Nathan merges and which he closes.
In text the last repair added: no.

RB-4. R3, a silent breach of Nathan's Q1 ruling, on the normal path of later runs. E11 (ITEM-02 with ITEM-01), A3's step.
Text: "and for a TW-ALPHA member every page that names TW's current release: search on the member's ID, title and version, fetch each page found and each page the member's own text names as holding its selection". This is the only new text that says how `ANALYZE` finds those pages. E7 writes only to pages "found by `ANALYZE`", and E6's check reads back only pages whose note changed.
Evidence:
- The pilot's texts now current on *HDE TW* and the *Glow Operations Hub* (pilot §P, HDE-NEW and HUB-NEW) name the release and TW-MGMT-10 only. Neither names or links any other member.
- Only TW-MGMT-10's own text names the selection pages (PF-4).
- Notion search misses pages (PF-26).
- Nothing in E11 searches on TW's current release name.
- So a later repair of any member other than TW-MGMT-10 reaches those two pages only by chance, for example if search happens to match an older section.
- Nathan's ruling: "when a TW prompt is repaired, the change prompt updates every page that names TW's current release".
Likelihood: plausible, for any repair of a TW-ALPHA member other than TW-MGMT-10 before G5.
Consequence: silent. Those pages go on naming a superseded release. That is PF-4, the defect ITEM-01 was approved to fix.
Smallest correction: E11 reads "search on the member's ID, title and version and on TW's current release name; fetch each page found, each page the member's own text names as holding its selection, and each page TW's last selection wrote".
In text the last repair added: no.

RB-5. R4, failure path. *How the plan runs*, "Waiting for each write", and *Failure path* step 2.
Text: a returned task is polled to `succeeded` "and only then makes the step's check". The sweep reads each page "once". Nothing waits for a pending task before the sweep.
Evidence:
- The pilot's full review made exactly this required (RA-1, PLB-1: "a failure sweep could record a write as not landed that lands later").
- Its repair read "before the step's check, and before any sweep". The pilot's §P says: "On the failure path, every pending task is polled to its end before the sweep". That clause is gone here.
- D9 records that `allow_async: false` "may still return a task".
Path: W4 returns a task, and polling ends in a tool error, so the run stops. The sweep reads the parent page before W4 lands and records the catalog as unchanged. Nathan follows "Before X4, he archives «NEW»". W4 then lands.
Likelihood: low.
Consequence: silent. The catalog selects an archived page, and the failure record says it does not.
Smallest correction: restore the pilot's sentence. A task whose state cannot be read is recorded as possibly landed, and the page is fetched again before Nathan acts.
In text the last repair added: no.

LISTED
Each gives path, likelihood and consequence. None is in text the last repair added.

- LB-1. E12, ITEM-03.
  - The body's new meter is elapsed time since the mode started, with no allowance for a wait on Nathan. §P's own stop rule does exclude the merge wait.
  - So any later `EXECUTE` that waits at X2 for longer than about its estimate passes twice the estimate when it resumes at X3.
  - Normal path of later runs; likely; a spurious stop and a re-pricing round trip (loud).
  - `ANALYZE` has no estimate to meter against at all.
- LB-2. E36 contains its own anchor, and its only check phrase spans that anchor.
  - Applied twice, it reads "subsection in each mode's subsection in each mode's section names each one.", and P58 still counts 1 in both X1.10 and X1.12.
  - Every other edit that contains its anchor (E8, E11, E12, E23, E24, E28, E29, E32, E34, E38, E41, E42) doubles its check phrase when doubled, so it is caught.
  - Failure path (a resend of W3); low; a duplicated clause in the body goes unseen.
  - Fix: add the absent phrase "mode's subsection in each", expected count 0.
- LB-3. X1.10 (4) checks one phrase from each new text. Design §11.5 asks for "its new text present" for each approved edit.
  - The unchecked parts of long texts (E7, E9, E11, E12, E15, E17, E18, E24, E25, E28, E29, E32, E34, E38, E40, E41) could be changed by Notion's Markdown round trip without either readback noticing. K-5 rates only the check phrases.
  - Normal path; low; silent.
- LB-4. K-14's mitigation, "X1.10 reads it in place", is not one of X1.10's seven checks.
  - Nothing checks that each new text reads correctly where it lands. Examples: E4 drops its anchor's leading "and "; E29 cites *Capturing a reviewer's or worker's return*, a label that no anchor or new text shows exists.
  - Normal path; unknown; silent.
  - Fix: add a check that each new text reads correctly in its sentence or cell, and that each label it cites is present.
- LB-5. E24 and E25 say more than ITEM-07.
  - The extra sentences are E24's "checked by a second reading", E24's limit on what a script over a save prints, and E25's "A save is deleted once its check is done". E25's rule does match `D22` condition 4.
  - C3 does not hold as written.
  - Normal path; certain; approved scope widened without naming it to Nathan (template rule 3).
  - Fix: drop the extra sentences, or name them in PO-1.
- LB-6. The selftest omits a case §A promised.
  - §A's PART-02 says the selftest holds "the pilot's record as a real must-pass case". It does not; only X1.4 (3)'s directory run reads the pilot's record.
  - §P does not record this departure from the frozen §A.
  - Normal path; certain; low.
- LB-7. X3 re-runs gates (3) and (4) with fixed counts: "2/2 GTWPE records pass, 4 others" and "the directory 6/6".
  - A Modification record that lands on `main` during the merge wait changes those counts, or may fail the validator.
  - After W1 to W3; low to medium; a loud `D26-B` stop caused by an unrelated file.
  - Fix: require exit 0 and record the counts rather than fixing them.
- LB-8. X4.2's readback wording would fail a correct W4.
  - C3-NEW reads back with the page's title (PF-27), not as sent.
  - 092926.1 stays a child page whose `<page>` block still links `3ea4590a05eb817093b3feea624aa24a`.
  - Read literally, "C1-NEW to C4-NEW present" and "C3's link … absent" both fail. The failure path then asks Nathan to reverse W4.
  - Normal path; low; loud.
  - Fix: state C3-NEW's rendered form, and confine the absence check to the members table.
- LB-9. C4-NEW dates the drift examination «D», which is X1.1's date. X4.1 examines after the merge, possibly days later.
  - Normal path; medium; a wrong date on a control page (the commit hash itself is exact).
  - Fix: use X4.1's UTC date.
- LB-10. «M» is called "the first commit … that holds the tool" but computed with `git log -1`, which gives the latest.
  - With a true merge commit this returns the branch's own commit, so X4.1's `fffadb5..«M»` skips main-only commits. The next A0 still sees them.
  - Normal path; low, since the repository squash-merges.
- LB-11. W4 leaves the catalog's lineage-pins note unchanged ("from a search that fetched no body … to the minute", "2026-09-24T15:38, to the minute").
  - E18 and E22 now make the drift check fetch exact edit times.
  - Later runs; medium; a false trigger finding recorded for Nathan (loud).
- LB-12. E32 says the branch's pull request "gates nothing", yet X2 waits on that same pull request whenever a part changes a repository file.
  - A pull request open from A1 onward invites a merge mid-flow. After that, the body's X5 "otherwise keep it" (and this run's X2, if a pull request from the branch merges before `EXECUTE`) pushes onto a squash-merged branch, and the new pull request conflicts.
  - Low to medium; loud.
  - Fix: X1.0 could check that the record is not already on `origin/main`.
- LB-13. E31's "a directory named for the Modification's slug" is ambiguous.
  - The body's `<slug>` excludes `gtwpe-`, yet this Modification's evidence directory is `gtwpe-first-repair`.
  - A GTWPE and a GCFPE Modification with the same slug would share a directory.
  - Low.
- LB-14. E7's "naming the new release and its changed members" differs from what the pilot wrote on *Alpha 1*: the whole eight-member section, which HDE TW and the Operations Hub cite as the exact rows.
  - Later plans; low. The approved plan names each text, so Nathan would see it.
- LB-15. E17 says a control page's rollback is "the reverse replacement". For TW-ALPHA, the route also gives "a newer release selecting the prior version" (E10).
  - Imprecise, not contradictory; low.
- LB-16. The tool copies the validator's threshold (`MIN_CONTENT = 40`) and its status-to-section map (`REACHED`) instead of reading `SECTION_FOR`.
  - If the validator changes either, the two checks diverge silently.
  - Low. Otherwise C5 holds: the shared rules run from the validator itself.
- LB-17. The tool's dry-run rule fires as soon as a `DRY_RUN` round is in `reviews`, and a dry run's first gate runs with that round already recorded.
  - So the *Dry run* subsection must be written before its own first gate.
  - Later runs; certain; a loud first failure.
- LB-18. E15 and "Waiting for each write" poll a pending task with no bound.
  - Failure path; low; waits until the 4 h stop (loud).
- LB-19. X1.7's "wait of about 20 seconds" may be unavailable where the harness blocks a foreground sleep. The six fetches could then run back to back.
  - Normal path; low; a loud stop after W1.
- LB-20. X2's pull request carries both the tool and records.
  - AGENTS.md gives records "Merging preserves the record and approves nothing (D21-C)", and gives other changes "what becomes current on main". Merging this pull request lands PART-02 (PO-2), and the plan does not say which statement it carries.
  - Low.
- LB-21. Trivial:
  - X1.3's `git status --porcelain` lists the untracked directory `docs/prompt_ecosystem_management/gtwpe/`, not the file.
  - «P» is fixed but used in no text.

A6, the catalog texts against the live GTWPE parent page, fetched in this review (last edited 2026-09-29T20:11:58.508Z; content stamped as of 21:58:10Z):
- C1, C2, C3 and C4 each occur exactly once.
- Each replacement stays inside its table cell or paragraph, so the members table keeps its four columns.
- C3-NEW's self-closing mention is the form the pilot used successfully.
- C4-NEW chains correctly into the existing "Before it, `0db3f0e`…".
- No required finding.

A7, authority:
- W1 to W4 rest correctly on the plan's approval (`notion-write-boundary.md`). PF10-AINEUTRAL-001 rule 3 keeps every authorization requirement and lets the surface confer none.
- X1.12's worker is a kind the body lets an approval name, and it is isolated from the counts as `execution-and-delegation-model.md` §7 requires.
- PO-1 names the pull requests at X2 and X5, but not X5's force-push. That rests on the body's X5 restart. With RB-1's explicit refspec it can rewrite only this Modification's own branch.

A8, the risk list: K-1 to K-14 are rated consistently, but they miss RB-1 to RB-5, LB-1, LB-2, LB-7 and LB-8. K-14's mitigation is overstated (LB-4). No entry in K-1 to K-14 is itself REQUIRED.

The claims:
- C1 fails (RB-1, RB-2).
- C2 holds.
- C3 holds except LB-5.
- C4 holds except LB-2 and LB-3.
- C5 holds (see LB-6 and LB-16).
- C6 fails in part (RB-3, RB-5).
- C7 holds.
- C8 holds except Q1 (RB-4).

Canon relied on
- AGENTS.md, read first: the canon-first rule; PF canon is read-only; operating routes; the pull-request description rules.
- HDE Governance (PF04) §9.1.6, read in full on `main` at `fffadb5`.
- HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, read in full on `main` at `fffadb5`.
- In flight, at e7e4d4c:
  - the record: its front matter, §A whole and §P whole;
  - `edits.json`, `phrases.json`, `gtwpe_record_check.py`, `guard_proof.py` and `EXEC-READBACK-BRIEF.md`, each whole;
  - my block of `PLAN-REVIEW-BRIEF.md` at eb36e70.
- On `main`:
  - design v1.2 §11 (11.1 to 11.10);
  - `gcfpe.decision-record.md` D20, D21, D22 and D26 in full, and D25 in part (D23 and D24 not read);
  - `notion-write-boundary.md` in full;
  - `prompt-body-content-policy.md`, the rule and its enforcement;
  - `execution-and-delegation-model.md` §7;
  - `ecosystem-change-management.md` §2 steps 3 to 5, §4 (CHK-001, DISP-001, GUARD-001, DERIV-001, PAIR-001, SCOPE-002), §5 and §6;
  - `modification_validate.py`, its constants, `split_frontmatter` and `check()` (blob 0cd1e5c);
  - `modification-template.md`, rules 1 to 8 and the §P guidance (blob 8fc21ab);
  - the pilot's record: §A findings PF-1 to PF-20, §P's steps, texts and full review, and PF-21 to PF-28;
  - closeout-residuals `plan/DECISIONS.md` P-83, P-97 and P-106, and `defects-by-round.csv` row R5-06, as evidence only.
- Not read: GTWPE-MGMT-10's body (by instruction), `reviewer-prompt-template.md` and `session-working-rules.md`.

Harness files: the harness auto-saved one oversized `git show` of the pilot's record, repository text with no prompt body, to `tool-results/b8quwqa0g.txt`. I did not read it. I did not delete it, because I write nothing, so it is left to teardown. My one Notion fetch was of the GTWPE parent page, a control page, and came back inline. I fetched no prompt page.

DECISION NEEDED
