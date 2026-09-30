3

GTWPE-TW-ADVICE-PLAN-A: full PLAN review 1 of MODIFICATION-20260930-gtwpe-tw-model-advice, at cc08e2a78711ba34cc6874f3dc07108690010e75. There are three required defects, all in §P's X2 and X4 rows. None of them is in text a repair added, because no repair has run on §P yet. As far as the committed text lets me check, the prompt edits, the skill edits and the guard proof hold.

REQUIRED

R-1: R1, normal path. X4.2, X4.3 and X4.5 check their result against a "pre-read" that no step makes.
- Text:
  - X4.2: "the rest of the page as the pre-read showed it".
  - X4.3 and X4.5: "every other heading and child page as the pre-read showed them".
  - X4.4: "32 headings, the old list with one added and one renamed".
  - X4.6: "139 headings, the old list with one added and one renamed".
- Evidence:
  - None of the edit cells in X4.2 to X4.6 includes a pre-read. The only read of these pages that §P defines is X1.0 (5), and it checks only anchors and edit times; it records no headings and no child pages.
  - X1.0 (5) also runs before X1.5 creates seven child pages: six under *HDE TW*, and TW-MGMT-10 «V» under the selection page. Checked against that read, X4.3 and X4.5 fail even when the write is correct.
  - In the S-3 resume, a fresh session has no pre-read at all.
  - X1.0 (5) accepts "a later edit" of *Alpha 1* or the Hub, yet X4.4 and X4.6 hard-code 32 and 139, which are the dry run's 31 and 138 plus one.
  - Both precedents put a "Pre-read: …" inside the step and compared against it: the pilot's X4.3 to X4.6, and the first repair's X4.2.
  - modification-template.md §P requires a plan that can be "executed mechanically with no interpretation on its normal path". C1 is refuted here.
- Likelihood and consequence: the missing pre-read affects every run. Read literally, the readback fails after X4.3 has already switched the selection page. The selection page then names «R» while *Alpha 1*, *HDE TW* and the Hub still name TW-ALPHA-20260929.1, and the freeze holds that state until Nathan acts. Read loosely, the executor has to improvise the check.
- Smallest correction: add a pre-read to the edit cell of each step from X4.2 to X4.6, as the precedents do: fetch the page, confirm its anchor occurs once, and record its headings and child pages (for *Alpha 1* and the Hub, by the script over the harness's save). Then state the X4.4 and X4.6 checks relative to it ("the pre-read's heading list with one added and one renamed") instead of 32 and 139.
- In text the last repair added: no.

R-2: R2, a silent wrong edit to a control page. The X4.4 and X4.6 readbacks cannot see the content they write.
- Text:
  - X4.4: "the page begins with *SECTION*'s heading, then the renamed heading; 32 headings…".
  - X4.6: "*HUB-NEW*'s heading once, directly above …; 139 headings…".
  - Both run "by a script over the harness's save".
- Evidence:
  - On *Alpha 1*, *SECTION* carries the seven «ID» links, «V», «R», «S» and «PA». *HUB-NEW* carries «R», «V» and «ID:MGMT-10». Both readbacks check headings only.
  - X4.3 checks the rows, but only on the selection page. X4.4 is a separate call, composed separately.
  - *HDE-NEW* sends readers to *Alpha 1* for the "Exact rows".
  - The pilot's X4.4 checked "rows as in X4.3", and its X4.6 checked that "the new section holds «R», «V» and «NEW»".
  - The script is not committed: the PLAN harness list names only scratch scripts. So D26-A rule 1 ("every step's verification names a committed command") is not met for these two steps.
- Path, likelihood and consequence: failure path, from an execution slip in the X4.4 or X4.6 call (a mistyped or swapped 32-hex «ID», or a value left unsubstituted). Likelihood is low. The consequence is silent: a wrong or broken row link lands on the page that holds TW's exact rows, or a wrong maintenance link lands on the Hub.
- Smallest correction: add to the X4.4 readback "*SECTION* as sent, its seven rows linking the seven «ID»s at «V»". Add to the X4.6 readback "*HUB-NEW*'s paragraph holding «R», «V» and «ID:MGMT-10»". Commit the script that checks both, and name it in the two rows.
- In text the last repair added: no.

R-3: R3, a silent breach of a Product Owner ruling (D24). X2's delivery to Nathan is incomplete.
- Text: X2 says "send Nathan the two archives, then `CHANGE-NOTE.md`, by `SendUserFile`". *CHANGE-NOTE.md* holds "the two archives' names and sha256; what changed …; the two reviewers' verdicts; …".
- Evidence:
  - D24's own guard: "A delivery is incomplete unless it carries the committed brief and two verdict files, each bound to the delivered digests … checked by reading the delivery."
  - skill-packaging-and-delivery.md, a BINDING convention from Nathan's direction of 2026-09-21, adds: caption each `.skill` file with its digest, leading with the sha256; send one `.skill` file per message; give every non-`.skill` file a unique name; and state where each package installs and what Nathan should see afterwards.
  - X2 sends neither `D24-BRIEF.md` nor the two `SECTION-10-REVIEW-tw1-<n>.md` files, and does not name them. *CHANGE-NOTE.md* is a bare, non-unique name, and X2 sets no captions.
  - X2's verification checks none of this.
  - The alpha-feedback precedent delivered "the brief and both verdict files".
- Path, likelihood and consequence: normal path, certain. Nathan installs from a delivery that D24 defines as incomplete, and nothing in the plan flags it.
- Smallest correction: X2 sends `D24-BRIEF.md` and both verdict files with the archives, or *CHANGE-NOTE* names each of them by repository path at the pushed commit, bound to the digests in `packages.json`. Send one archive per message, with the caption leading with its sha256, and give *CHANGE-NOTE* a unique name.
- In text the last repair added: no.

LISTED (each gives path; likelihood; consequence. None is in text a repair added.)

- L1 (A1): DRAIN-10.07 and DRAIN-20.07 turn "The two required assessment checkpoints do not require…" into "Preflight does not require…". That widens the kept rule from the checkpoints to all of preflight, which is more than a removal. Normal; certain; low.
- L2 (A1): MGMT-10.13 keeps "Missing decisive input is incomplete." as a rule of its own. Its twin in tw-flowmaster line 338, "missing decisive input makes assessment incomplete", suggests the clause qualified the advice passage being removed. Normal; cannot be checked without the body; low.
- L3 (A1): APPLY-10.08's new text drops "separate audit", which the drains' parallel sentence keeps, and adds "Preserve run identity and verified work.". The shared new step 5 adds "source selection, package identities where present". Without the body (D22) I cannot check any of this against the removed span, and X1.5 checks only that the new text is present (K-5). Normal; likelihood unknown; low.
- L4 (A2): Composing a span from the fetch is mechanical, and the single retry covers only the tags' backslashes; any other escape fails loudly (K-2). But nothing checks that a span removes only §A's passage. X1.5 checks new text, absent phrases, counts and headings, so a span that also removes kept text containing none of the counted terms passes. Failure path; low; silent loss of kept prompt text.
- L5 (A2, D26-E): `absent_after` does not say whether it is case-sensitive (`counts_after` is). It is also narrower than §A's broad search terms: it lacks the other forms of `recommend` and `assess`, `Strength` on its own, `profile`, `Max`, `Sol`, and a bare `eight`. Normal; low; a missed in-scope passage would survive.
- L6 (A3): `counts_after` matches §A's exception list.
  - TRIAGE: model 3, advice 2, assessment 2. These are its two model-advice bans, "model-assessment" and "complete supported assessment".
  - workload is 1 in exactly the five members whose step 4 has "verification workload".
  - RECORD-10 and RECORD-20: model 1, advice 1 each.
  - MGMT: model 3, advice 1, from its three model exceptions.
  - However, no dry-run row runs X1.5's absence and count checks on the text as it would land (D26-A rule 1); the counts rest on the author's own derivation. Normal; low; a wrong count stops the run loudly after the page already exists.
- L7 (A4): Three wording issues in the control texts. Normal; certain; low.
  - *SECTION*'s "except where they run or name TW-ASSESS-10 or give model or effort advice" leaves open a step that names TW-ASSESS-10 and also carries another instruction.
  - The historical *Verification and runtime limits*, which *SECTION* says "still apply", hold the stale Flowmaster revisions that §P leaves out of scope. They sit beside *SECTION*'s claim that "TW Flowmaster 1.3.0 … match this release".
  - *HDE-NEW* and *HUB-NEW* say "model advice" where *SECTION* says "model or effort advice".
  - The +1 arithmetic behind 32 and 139 is correct.
- L8 (A5): The edit to line 393 leaves "Configure the GCFPE target under …, and only the capabilities required by the pinned identification prompt", so the capability limit now reads as applying only to GCFPE targets on legacy runs. Selected-catalog TW keeps its own "Require only capabilities needed by the pinned stage". These all read correctly: the rewritten profile condition (with K-1 accepted), line 339's kept rule, the GCFPE sentences on lines 351 and 352, and "Validate the manifest and fixed policies" (two fixed policies remain). Normal; certain; low.
- L9 (K-1): K-1's likelihood reasoning, "the window is X3 to X4.3 in one session", understates S-1 as §A stated it. The window opens at Nathan's install, extends into a new session under S-3, and stays open after a failed X3 until rollback. Failure path; low; Flowmaster runs silently skip assessments that the selected release requires.
- L10 (A6): No rollback archives are built from the installed trees, although X3, PO-4 and *CHANGE-NOTE* all rely on "the prior archives". The alpha-feedback precedent delivered rollback packages. Failure path; low; rollback may be impossible, which prolongs L9.
- L11 (A6): X3 compares only the two changed skills, using skill_tree_digest. skill-identity-and-freeze.md names freeze.py and also asks to check "every skill it deliberately did not" touch. For tw-flowmaster the two recipes agree, and for flowmaster-validate the self-identity check covers the declaration line. Failure path; low; a stray change to another skill would go unseen. X3 otherwise stops loudly if the install never shows (S-3). The synced tree does refresh within a session (docx was rewritten at 2026-09-30T02:07:46Z and `manifest.json` at 02:17), so the check "exits 0 with X1.2's results" can differ for reasons unrelated to this change.
- L12 (A6): X3's "stop and record it" does not say to commit and push the record before the session ends, which the resuming session needs. Failure path; low; loud.
- L13 (A7): P-F2's fourth site is required, because `validate_gcfpe_20260914.load_profile` compares the profile's `validator_revision` under PROFILE_IDENTITY. Normal; low; the worst case is a voided GCFPE review. Consequences beyond S-4:
  - the profile's sha256 changes (it is 1690c91d… now); it is pinned only in the historical closeout-residuals `plan/skills/manifest.json`;
  - no other installed skill pins `validator_revision` or the profile;
  - §A searched only the repository, so any GCFPE record in Notion of flowmaster-validate's revision or digest is unchecked;
  - the plan does not ask Nathan to confirm that no GCFPE review is running before he installs the shared validator (the freeze rule), as the alpha-feedback A1-4 did.
- L14: X1.3 gives no packaging command, no quick_validate step and no PYTHONDONTWRITEBYTECODE=1. The convention runs package_skill from the skill-creator directory, so running it from the synced skill-creator would write `__pycache__` into the synced tree, which X1.0 (3) says is only read. Normal; plausible; low and silent.
- L15: Dropping the isolated readback departs from ecosystem-change-management.md, where class B verification is "Isolated readback of everything changed" and item 2 of the definition of done requires it. The plan discloses this under Nathan's directions but does not list it as an accepted risk, as the pilot did with its K-3. Normal; certain; a misread by the session goes unseen.
- L16: P-F1 and P-F2 carry on past findings against §A, whereas modification-template.md rule 1 says to return DECISION NEEDED and not carry on past such a finding. Both are disclosed with the plan. Normal; certain; procedural.
- L17: The failure path does not say that the failure record is committed and pushed (D26-B rule 1, in the branch-only form Nathan allowed on 2026-09-28). It also does not say who makes a reverse replacement, when PO-1 authorizes no other Notion write. Failure path; low; loud.
- L18: "Before X1.5's first write … nothing written" is no longer true once X1.4 has pushed `D24-BRIEF.md`; restarting the mode would re-commit it. Failure path; low; loud.
- L19: CAT-OLD is only the start of the live line, which continues "Before it, `74f6cc9`, examined by MODIFICATION-20260929-gtwpe-pilot.". With CAT-NEW the result is a two-step "Before it" chain that still reads coherently. Normal; certain; cosmetic.
- L20: S-OLD and the block spans each cross Notion block boundaries in a single `old_str`, which no earlier run has tried. Normal; likelihood unknown; loud (K-2).
- L21: The front matter's `estimate.plan` still says "one full review by two reviewers with its repair", and X1.0 (5) says "four control pages" but lists five. Normal; certain; cosmetic.

Claims:
- C1 is refuted in part (R-1, R-2).
- C2 and C3 hold as far as the committed text shows (L1 to L6).
- C4 holds by reading; I did not run the scripts. The 21 tw-flowmaster edits and 11 flowmaster-validate edits each match once. Every forbidden identifier in the installed tw-flowmaster (lines 258, 266, 268, 337, 340 and 341) sits on a line an edit removes, and none sits in the Primary core. The guard proof's disabled case is meaningful, because the validator checks self-identity after the skill checks. P-F2 is required.
- C5 holds for the 21 + 5 writes, and the selection waits for X3.
- C6 holds: the lean review, K-1, the aim of about 2 h with the stop rule at twice the recorded estimate, and C5 recorded.

Canon relied on:
- AGENTS.md.
- HDE Governance (PF04) §9.1.6, read in full.
- HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, its rule, on origin/main at f83c755.
- Governing documents read: gcfpe.decision-record.md D20 to D26, modification-template.md, ecosystem-change-management.md §2 and §5, reviewer-prompt-template.md, notion-write-boundary.md, skill-identity-and-freeze.md and skill-packaging-and-delivery.md. The pilot's and first repair's records were used for precedent.

Method and disclosure:
- Read-only throughout: git show, grep, log, ls-tree and rev-parse; grep, sed, cat, ls and find; and one sha256sum of the installed validation profile. No fetch, no script or Python run, no Notion access, no agent.
- The harness saved one oversized grep output on its own (validator source lines and a docs search, no prompt body) to /root/.claude/projects/-home-user-glow-hdengine-v2/2ccc3813-37ac-5060-a437-a15e0e1ad7a0/tool-results/bs5h0tx3z.txt. I did not read or delete it, since deleting would be a write; it is left for teardown.

IN FLIGHT: the three required defects go to repair, followed by a second review or a diff check, as Nathan directed. The listed findings go to Nathan with the plan.
