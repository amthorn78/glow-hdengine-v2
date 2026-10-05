1

GTWPE-TW-REPOSITORY-IO-PLAN-A: full PLAN review 1 of 2 (D26-A) of MODIFICATION-20261005-gtwpe-tw-repository-io, at 29fe34144d6c9f25ab921f1d583a166f33bc1fdc. I found one required defect: two of the three current-release notes do not say what Nathan's Q-1 answer directs. It is not in text the last repair added. The 94 prompt edits hold up. They map one for one onto §A's 72 passages and 12 identity lines, they keep GTWPE-D1 whole in the three bound prompts, and the readback would catch an edit that is partial, misplaced or sent to the wrong member.

**The brief's hash matches.** `PLAN-REVIEW-BRIEF.md` at a34cf0f has sha256 `920face887a95f32541384cf92faa6401c7ea54647d11de19d8397edf2147872` (11,651 bytes), the value I was given. a34cf0f changes only the brief's commit pointer, and the working tree equals 29fe341 for the record and its evidence.

**Checks I ran:**
- `edits.json` has sha256 `768d9255…aa84d542` (44,233 bytes), which equals «H».
- `ctl_check.py` has sha256 `4e968007…1720923c5`, the same as the model-advice copy.
- `PYTHONDONTWRITEBYTECODE=1 edits_check.py` returns PASS and exits 0. It reports 94 edits, 8 GTWPE-D1 items read from the decision record, and OUT-A as the longest anchor at 220 characters. Its counts after equal §P's table in all 78 cells, and its check phrases equal §P's table.
- All ten `--inject` faults exit 1, each caught by its own check.
- §A at 29fe341 equals §A at 8cd6fcc except for one trailing blank line.

REQUIRED

R-1: R3, a silent breach of a Product Owner ruling (also R2, a silent wrong edit to two control pages). Normal path; certain.
- **Text.** HDE-NEW (record line 1041, written by W22 at X4.5) and HUB-NEW (line 1049, written by W23 at X4.6) each say only "TW Flowmaster 1.3.0 does not run this release."
- **Evidence:**
  - Nathan's words in `analyze_approved_by`: "Q-1: option (a). Select the new release in this Modification; the selection page and the notes say that tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run it, and TW runs by Nathan's direct invocations until the Flow Manager (C4)."
  - The option he chose, §A Q-1 (a) at line 582 (unchanged since 8cd6fcc), says "the three notes". §A's A3 table identifies them as the current-release notes on *Alpha 1*, *HDE TW* and the Operations Hub.
  - §P says the same at lines 733–735: "The selection page and the three notes say that `tw-flowmaster` 1.3.0 and `flowmaster-validate` 3.3.2 do not run it, and that TW runs by Nathan's direct invocations until the Flow Manager (C4)".
  - The override reason at line 17 says "The selection page and the three notes say so". Brief claim C5 says the notes carry out Q-1's direction.
  - Only SECTION (line 1002) and A1-NEW (line 1028) carry both halves. HDE-NEW and HUB-NEW leave out flowmaster-validate 3.3.2 and the sentence about direct invocations.
  - No readback can see the gap:
    - X4.5 compares HDE-NEW with the plan's own text.
    - X4.6 checks only `--has` '**«R» is selected.**', 'Every member is at «V»', '«PA»' and 'six-member catalog'.
    - Both pass on the texts as written.
- **Consequence.** Two of the four pages that name TW's current release would not say what Nathan directed, and the record would report that they do. A reader of *HDE TW* or the Hub learns that TW Flowmaster does not run the release. They do not learn that flowmaster-validate 3.3.2 does not run it either, or that TW runs only by Nathan's direct invocations until C4.
- **Smallest correction:**
  - In HDE-NEW and HUB-NEW, replace the sentence with A1-NEW's: "TW Flowmaster 1.3.0 and flowmaster-validate 3.3.2 do not run this release: TW runs by Nathan's direct invocations until the Flow Manager (C4)."
  - Add that sentence as a `--has` to X4.4 and X4.6, and name it in the readbacks of X4.3 and X4.5.
- **In text the last repair added:** no. The repair changed only `edits.json`'s new texts.

LISTED (each line gives the attack item, the path, the likelihood, the consequence, and whether it is in text the last repair added)

- L1 (A3, the waiver's wording): The override reason (line 17) and SECTION (W20, "Nathan waived … for them") extend Nathan's waiver to flowmaster-validate 3.3.2. His words waive §9.1.6's interacting-skill readiness "for tw-flowmaster", and §A's option (a) says "for the skill". Normal; certain. The record and the selection page attribute to him a wider waiver than he gave. No behaviour changes, because flowmaster-validate reaches the release only through tw-flowmaster, which is unchanged. It is a cheap fix in R-1's pass. Not in repair text.
- L2 (A2, D26-E): R3 reverses the bodies' PR ban. OUT-B removes "create a PR", and C1's §A A.1 says every TW prompt "forbids a PR or repository change". Yet the readback looks for the old rule only by the exact phrase "create a PR", and none of the 13 broad terms covers PR, pull request, commit, push, merge or repository. A ban elsewhere in a body would survive beside OUT-A's "opened if none is" and pass every check. Normal; low, and not measurable from committed text. The result would be a silently self-contradicting selected body. Cheap fix: a broad-match readback of those terms on the five document prompts, each hit recorded with its exception, and a contradicting hit as a stop. Not in repair text.
- L3 (A2): R3's "never merges" appears in no new text (no `new` in `edits.json` contains "merge") and in no check phrase. Yet §P's rule table (line 852) says OUT-A and OUT-B leave a prompt that "never merges". The ban rests on kept text after OUT-B's anchor, which no committed file shows. Normal; unknown, likely low. If that text has no merge ban, a prompt that now opens pull requests has none of its own; AGENTS.md's rule that the PO merges still binds an agent here. Not in repair text.
- L4 (A1, C6): Line 746 says §P quotes bodies "only in its first line, its headings and its last words". The repair note for PL-C (lines 1150–1152) also quotes a kept drain sentence of 57 characters, which is not an anchor. That is shorter than the longest anchor, so Q-2's limit holds as the plan reads it, but the statement is untrue. Normal; certain; low. In text the last repair added: yes.
- L5 (A6, C6): X5's ITEM-01 check (paths only under `docs/ephemeral/modifications/`, and `edits_check.py` exits 0) tests where files are, not what they quote. A body passage quoted in §E would leave ITEM-01 marked VERIFIED, though 100526.2's own rule on reading bodies still binds the session. Normal; low; silent. Not in repair text.
- L6 (A3): No readback names SECTION's release paragraph or the Q-1 sentence on any of the four pages. X4.3 names «S», «PA», the rows and *Current operation*; X4.4 and X4.6 check only their `--has` values and rows. A dropped or garbled sentence would pass; R-1's correction covers the Q-1 sentence. Normal; low; silent. Not in repair text.
- L7 (A3): The pre-reads of X4.4 and X4.6 follow X4.3's selection write. The last TW change moved them ahead of it at Nathan's opt-in (DL-1). X1.0 (5) has already run `ctl_check.py pre` on real saves, so only a page change after X1.0 reaches this case, and it then fails after the switch while the notes still name 20261004.1. Failure path; low; loud (D26-B). Not in repair text.
- L8 (A3): The «PA» checks (`--has '«PA»'` in X4.4 and X4.6, and X4.3 (2)) are also met by «S» when approval and selection fall on the same UTC day, as the last change's DL-3 found. Normal; medium; a missing «PA» would pass. Not in repair text.
- L9 (A4): X1.0 (3) counts in "each member's fetch" without (g)(5)'s exclusion of the title property. Read literally, "— 100426.1" and "100426.1" then occur once more, in the title, and the precondition fails. Normal; low; loud, with nothing written. Not in repair text.
- L10 (A6): X1.3 (g), X4.2, X4.3 and X4.5 verify by reading, not by a committed command. D26-A rule 1 asks the dry run to confirm a committed command, but P8 checked only that each check could fail. The plan discloses this as K-5, and the last TW change did the same. Normal; procedural. Not in repair text.
- L11 (A1, K-4): PL-B and PL-F are the first TW edits that split a paragraph into list items. The rest of the paragraph follows the eighth item on a plain line. If Notion folds that line into the item, (g)(4) fails. Normal; low; loud. The structure predates the repair; the wording of the trailing line is the repair's.
- L12 (A6): «V» is fixed from X1.1's date. A run that crosses 00:00Z creates pages one day after the date their version carries. Normal; low; cosmetic. Not in repair text.
- L13 (A6): Each «ID» reaches the record only at X2. A crash between Write 1 and Write 2 leaves an unselected duplicate titled "… — 100426.1 (1)" that (h)'s count of new titles does not see, and a rerun makes another. Failure path; low; clutter that the sweep would list. Not in repair text.
- L14 (A6): X1.0 (7) does not look at the watched paths. X4.1 runs after W1 to W18 and does not stop X4.3, so a change to GTWPE-D1 or PF10 between approval and EXECUTE is recorded and returned, but only after selection. Likewise X1.0 (0) checks 100526.2's edit time, not that the catalog still selects it. Normal; very low; recorded, not silent. Not in repair text.
- L15 (A6): PO-1 authorizes W1 to W23 "made from this session". K-14's remedy may restart EXECUTE in a fresh session, which that wording does not cover. Failure path; low; a careful session asks. Not in repair text.
- L16 (A1, C6): Six anchors are 100 characters or more: OUT-A 220, PL-F 190, IN-C 150, OUT-E 130, RUN-C 121 and PL-A 100. Each is wholly replaced text, so Q-2 holds as the plan reads it. The ends of a span, the last TW change's form for long passages, would commit less of each body. Normal; certain; low. Not in repair text.

Attack items, answered:
- **A1.** No proof-log text weakens GTWPE-D1:
  - Each bound prompt gets a "separate proof log" with all eight items word for word; the PROOF check confirms this against the decision record.
  - The link is the name, the place and item 8.
  - TW-APPLY-10's basis for each operation (ID, rationale, source-ledger reference, "not only a pointer") is what ITEM-04 asks.
  - K-9 is rightly listed.
  - The four dry-run repairs are right and complete, and they added no required defect (see L4 and L11).
- **A2.** OUT-A and OUT-B carry every R3 property except no-merge: the path under `docs/ephemeral/`, the branch, one pull request "opened if none is", a missing path or branch as a stop, and the bans on Drive, Library and `docs/pfcanon/`. No-merge is L3. I could not reproduce from committed text any contradiction with the save-recovery rules or the documentation-work sentence; see L2 for the unchecked surface.
- **A3.**
  - Sending SEL-1 before SEL-2 is sound: each old text matches once whichever order the call applies them, and exactly one *Current operation* heading results.
  - F-1 and K-3 are rightly listed.
  - `ctl_check.py`'s arguments match A1-NEW and HUB-NEW: the headings, the `--has` strings and the row form.
  - The defects are R-1 and L1.
- **A4.** The readback is strong:
  - Every edit has at least one absent phrase, so a partial edit fails at (5). Unique anchors and (4) catch a misplaced edit. A second send cannot match.
  - I traced edits sent to the wrong member. RECORD-20's edits on RECORD-10's page, or DRAIN-10's on DRAIN-20's, are caught at (5) and (6); every other case fails at the call.
  - The counts after follow exactly from §A's counts before.
  - The ten checks test what they say.
- **A5.** K-12, K-13 and K-14 are each rightly listed:
  - K-12 would add a passage beyond §A's 72, and it is disclosed.
  - K-13 is §A's R1 and harmless either way.
  - K-14 stops loudly before any write, with PO-4 as the remedy.
- **A6.** These all hold: the rules for «V» and «R», X2 going straight on to X4, X4.1's range from 20d0dd8, the failure path (D26-B, with the failure-record exception that the second repair's E7 put into *Boundaries*), and the stops at 7 h and 6 h (twice 3.5 h and twice 3 h).

Method and disclosure:
- **Read-only throughout.** I used `git show`, `git diff` between commits, `git log`, `git grep`, `git cat-file`, `git rev-parse` and `git status`; `grep`, `sed`, `awk`, `cat`, `wc`, `sha256sum`, `ls`, `find` and `date`; and Python one-liners that parse piped text and write nothing. I ran `edits_check.py` and its injections with `PYTHONDONTWRITEBYTECODE=1`. There was no fetch: `origin/main` as known locally is 20d0dd8. There was no Notion, Drive, GitHub, session or agent action. The working tree is clean, with nothing untracked or ignored and no `__pycache__`.
- **Two harness side effects, neither mine:**
  - The harness saved one oversized output on its own, a slice of MODIFICATION-20260930-gtwpe-tw-model-advice.md (repository text, no prompt body), to `/root/.claude/projects/-home-user-glow-hdengine-v2/00019a4f-7a96-5dbc-8134-627fcf409934/tool-results/bi3b40puc.txt`. I did not read or delete it.
  - The repository's PostToolUse hook (`.claude/settings.json`, running `check_canon_relied_on.py`) ran after my Bash calls and updated `.git/canon_relied_on_hook.json` (modified 2026-10-05T23:45:42Z).
- **No TW body or Notion page was read** (D22, the brief). What I say about kept text rests on §A, §P, `edits.json` and earlier evidence. I cite the one kept sentence I mention (L4) by line rather than quote it.
- **Canon relied on**, read on main at 20d0dd8 after a `git grep` for the task's terms:
  - HDE Build Notes (PF10) 2.29 PF10-CANON-001 and 2.38 PF10-AINEUTRAL-001, each read in full.
  - HDE Governance (PF04) §9.1.6, read in full.
  - Canon names no TW prompt and sets no rule for TW proof logs, and nothing in it contradicts the plan's routes.
- **Rulings relied on:** GTWPE-D1; `gcfpe.decision-record.md` D20 to D22, D25 and D26; `modification-template.md`; `ecosystem-change-management.md`; the reviewer template; `notion-write-boundary.md`; `prompt-body-content-policy.md`. The calibration precedents were the last three PLAN reviews.
- **Not exercised:** any Notion write, the duplication and its polling, Notion's rendering (K-4), and `git fetch` (K-14).
- **Scope of this review:** it is the D26-A PLAN review Nathan directed, not an automated code review, so AGENTS.md's line on CI-exempt paths does not apply.

IN FLIGHT: R-1 goes to repair. Then, as Nathan directed, a second reviewer or a check of the repair's diff follows. The listed findings go to Nathan with the plan. If he opts in to any, I would put L1, L2 and L3 first.
