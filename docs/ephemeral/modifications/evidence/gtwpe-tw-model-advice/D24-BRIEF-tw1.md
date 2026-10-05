---
artifact_type: FILLED_SKILL_REVIEW_BRIEF
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.2, first template (skill reviews, D24)
modification: MODIFICATION-20260930-gtwpe-tw-model-advice
round: tw1, the first D24 skill review of PART-02 (X1.4)
reviewers: two, SFR-TW1-1 and SFR-TW1-2, each a fresh general-purpose subagent, neither forked nor context-inheriting
committed_before_spawn: true (D24 condition 2)
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# D24 skill-review brief, round tw1, filled

The same brief goes to both reviewers; only the reviewer ID and the capture path differ. Under
GTWPE-MGMT-10 092926.2 (*Reviews are bounded*) a reviewer writes nothing: its final message is its
record, captured unedited from its own transcript by the authoring session.

- **SFR-TW1-1**: its final message is captured to
  `docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/SECTION-10-REVIEW-tw1-1.md`
- **SFR-TW1-2**: its final message is captured to
  `docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/SECTION-10-REVIEW-tw1-2.md`

## Canon relied on

- `AGENTS.md`: the canon-first rule; PF canon is read-only.
- HDE Governance (PF04) §9.1.6, on interacting skills ("An edited subgroup is not ready while an
  affected counterpart remains incompatible"), and §9.1.3; HDE Build Notes (PF10) 2.31
  PF10-HDR-001 and 2.38 PF10-AINEUTRAL-001; all on `main` at `f83c755`.
- In flight: the record's §A (approved), §P (approved, with its successor of 2026-10-04) and §E;
  `gcfpe.decision-record.md` D22, D24 and D26; `reviewer-prompt-template.md`;
  `skill-packaging-and-delivery.md`; `skill-identity-and-freeze.md`.

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Two packages, installed together as one set, in
/tmp/claude-0/-home-user-glow-hdengine-v2/48e35780-fb1c-5213-a75c-f5af8b1fdc6c/scratchpad/pkg-tw1/
(the directory and both files are read-only):
- tw-flowmaster.skill, 2 entries, 19193 bytes, sha256 88166c3d48fee16900e125f1cf2fe15cf2b46a2e0a6ac05ea0fdd5ef3c1a4b89
  Extracted tree: 2 files, 55131 bytes, tree digest 0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c;
  TW_FLOWMASTER_SPECIALIZATION_REVISION 1.3.0; SKILL.md 54711 bytes, sha256
  21c632e1b92a6096bb521d990fde1d7aee383af029e7f0e99fce68eac09b1575.
- flowmaster-validate.skill, 31 entries, 322860 bytes, sha256 e1f495b3f40f9a75c713433236391763505cb3895364076f71eb771a72710f3f
  Extracted tree: 31 files, 1915296 bytes, tree digest and declared SKILL_TREE_SHA256
  284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733; FLOWMASTER_VALIDATE_REVISION 3.3.2;
  validator_revision 3.3.2.
They install together: the new validator requires tw-flowmaster 1.3.0, and the installed validator
3.3.1 requires 1.2.0, so either one installed alone fails the suite.
The same digests are in docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/packages-tw1.json.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
NONE, first review of these changes. The installed trees (§3) were last reviewed under earlier
Modifications; no verdict on them carries to these bytes. No finding is carried forward.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline the diff was taken against: the installed skills in the synced directory
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/
(read only):
- tw-flowmaster: 2 files, 58775 bytes, tree digest fd6c344befd9ce9e89648e6e404dd39f02e50bfaef2ca13d4e56ab84f5576617, revision 1.2.0.
- flowmaster-validate: 31 files, 1914948 bytes, tree digest ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af (its declared SKILL_TREE_SHA256), revision 3.3.1.
Repaired trees: the extracted trees in §1.
The tree digest recipe is skill_tree_digest in flowmaster-validate/scripts/validate_gcfpe_20260914.py,
run with PYTHONDONTWRITEBYTECODE=1 (import the module from the tree you are measuring; see
docs/prompt_ecosystem_management/skill-identity-and-freeze.md for the freeze convention).
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.
Superseded values, not to be chased: the trial archives in the record's §P *Dry run (PL3)* row P10 had
the same byte sizes but other sha256 values (a zip carries timestamps); the tree digests are the identity.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2, cloned at /home/user/glow-hdengine-v2. Branch
docs/20260930-modification-gtwpe-tw-model-advice — read its HEAD, not a pinned commit, through the
remote-tracking ref, without touching the working tree:
  git -C /home/user/glow-hdengine-v2 show origin/docs/20260930-modification-gtwpe-tw-model-advice:<path>
NOT MERGED. It carries pull request amthorn78/glow-hdengine-v2#568, which stays open until the record
is COMPLETE.
**If that branch does not exist when you look, it merged and was deleted.** Read the same paths on
main.
- The record: docs/ephemeral/modifications/MODIFICATION-20260930-gtwpe-tw-model-advice.md. Read §A's
  *Revision of 2026-09-30* (the skill part's scope, F-2, F-3, S-1 to S-5, C4), §P's *Values*, *The
  skill edits*, *The D24 brief*, *Open findings, accepted as risks* (K-1), the listed findings L8 to
  L14, and §P's successor of 2026-10-04; and §E's X1.2 and X1.3 rows once present.
- The edit script: docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/skill_edits.py (32
  literal edits; the diff is defined by it).
- The guard proof: docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/guard_proof.py.
- The digests: docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/packages-tw1.json.
- The prompt edits PART-01 makes, for "matching the new prompts":
  docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/edits.json (its `new` texts).
- The packaging and identity conventions: docs/prompt_ecosystem_management/skill-packaging-and-delivery.md,
  skill-identity-and-freeze.md, and gcfpe.decision-record.md D22, D24 and D26.
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. The extracted trees differ from the installed trees only as skill_edits.py says: 32 literal
    edits, each matching once, in six files, and flowmaster-validate's SKILL_TREE_SHA256 recomputed
    after them. Rebuilding from the installed trees with skill_edits.py reproduces the extracted trees
    byte for byte.
C2. tw-flowmaster's embedded Primary core, from `<!-- FLOWMASTER_CORE_BEGIN -->` to
    `<!-- FLOWMASTER_CORE_END -->`, is byte-identical to the installed tw-flowmaster's and to
    flowmaster-primary's.
C3. No stage, input or rule of tw-flowmaster runs, requires or names TW-ASSESS-10, and no fixed model
    or effort policy remains, outside §A's kept exceptions: the GCFPE binding and the GCFPE sentences
    (§A's candidate C4), the stall bullet's prohibitions, `/model`, the composer checksum's
    model/reasoning, the report row's application model/reasoning, and the rule to record actual
    configuration only when directly verified. The selected-catalog TW profile now applies when the
    selected prompts "carry the exact no-redlines contract", and READY creator output points to
    TW-APPLY-10, as the new prompts say.
C4. With the two built skills in an isolated root, flowmaster-validate passes strict
    (FLOWMASTER_SUITE_PASS, exit 0, self_identity OK, validator_revision 3.3.2, no skill error or
    warning), and each of the six new CONTRACT_FORBIDDEN identifiers for tw-flowmaster fires when
    injected and is silent with its own line removed (guard proof 12/12).
C5. The authority is Nathan's direction of 2026-09-30, quoted in §A's *Revision of 2026-09-30*:
    "Q1: option (b), plus the skill update — Nathan: "we should update the skill" ... 1. Add a skill
    part: an updated tw-flowmaster package with TW-ASSESS-10's stages and its fixed model policy
    removed, matching the new prompts, and any flowmaster-validate assertions that pin the old wording
    updated to match. Nathan's direction is the explicit skill-update scope the body requires; Nathan
    alone installs." His approval of the analysis (analyze_approved_by) narrowed it: "Keep scope to
    removal: drop the new guard that makes tw-flowmaster refuse the old release (selection already
    waits for Nathan's install). Keep the validator guard against the removed wording returning." His
    plan approval of 2026-10-04 is in plan_approved_by.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The rewritten profile condition and what now governs a selected-catalog run. With the
    assessment contract gone from the condition, does any legacy clause (a fixed model, a page-count
    rule, direct creation-to-application) still govern a selected-catalog TW run, or does some text
    still route through an assessment? The profile now also matches the currently selected
    release, TW-ALPHA-20260929.1, whose prompts still require TW-ASSESS-10, until the new release is
    selected; that window is the accepted risk K-1 (Nathan dropped the refusing guard). Treat K-1
    itself as known; report anything beyond it.
A2. The kept GCFPE clauses (§A's C4: the GCFPE binding and the GCFPE sentences of the old lines 351,
    352, 393 and 451) and the old line 339's kept rule. Are the edited sentences coherent after
    removal, and does anything kept still impose a fixed model or effort policy on a non-GCFPE (TW)
    stage? The listed finding L8 says the old line 393's capability limit now reads as GCFPE-only on
    legacy runs; confirm or refute its consequence.
A3. The fourth validator_revision site (§P's P-F2), in the GCFPE reference
    references/gcfpe-20260914.1-091426.1-validation-profile.json. Its sha256 changes (installed
    1690c91de5ab5d606ac7fffc8b4e26a0f791f0e5fb39e4c5d30fb34689e2bfb1, built
    3f35e35c130040a65fd3e9cb4164e39b77f9f206f0deb35cc36c60ad4a68ff3a). Does change-flow's GCFPE check,
    or any other consumer, pin that file's bytes or hash, and does every pin still agree? Is GCFPE
    validation otherwise unchanged?
A4. Whether any fixture, reference or other skill's list still expects the old terms
    (PRE_CREATION_ASSESSMENT, PRE_APPLY_ASSESSMENT, ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN,
    TW-ASSESS-10, revision 1.2.0 or validator revision 3.3.1).
No question is deliberately left unsettled by this round.

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. The installed tree cannot be validated in place: flowmaster-validate stops fatally (exit 2) on
    canva-drive-facebook-workflow/SKILL.md, whose quoted `name:` its front-matter check rejects,
    before it checks any Flowmaster skill (§A's F-3). Validate on an isolated root that copies every
    installed skill directory except canva-drive-facebook-workflow; the validator's documentation
    allows an isolated test root. The fix belongs to that skill's owner.
L2. The synced directory now holds 30 skill directories (29 besides the canva skill); §A counted 28
    besides it on 2026-09-30. The additions are unrelated skills; include them in the root as found.
L3. No prompt body is available to you (D22): check "matching the new prompts" against edits.json's
    new texts and the record, never by fetching a Notion page.
L4. No rollback archives were built from the installed trees (the accepted risk L10); the prior
    digests in §3 identify what a rollback must restore.
L5. The author ran the gates from the built trees, which the extracted trees equal (diff -r, no
    output); the author did not run them from a fresh extraction.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1.
Use your own scratch directory,
/tmp/claude-0/-home-user-glow-hdengine-v2/48e35780-fb1c-5213-a75c-f5af8b1fdc6c/scratchpad/review-<REVIEWER_ID>/,
and write nothing anywhere else.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm `name:` in each SKILL.md frontmatter is unchanged.
  b. Extract into a clean tree, restore the untouched sibling skills the tooling needs, and run the
     gates FROM THE EXTRACTED CONTENTS, not from any working copy:
       R=<scratch>/root; mkdir $R; copy every directory of the synced root into $R except
         canva-drive-facebook-workflow, tw-flowmaster and flowmaster-validate; copy the two
         extracted skills into $R
       PYTHONDONTWRITEBYTECODE=1 python3 $R/flowmaster-validate/scripts/validate_flowmaster.py --skills-root $R --strict-warnings
       git -C /home/user/glow-hdengine-v2 show origin/docs/20260930-modification-gtwpe-tw-model-advice:docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/guard_proof.py > <scratch>/guard_proof.py
       PYTHONDONTWRITEBYTECODE=1 python3 <scratch>/guard_proof.py $R <scratch>/guard
       git -C /home/user/glow-hdengine-v2 show origin/docs/20260930-modification-gtwpe-tw-model-advice:docs/ephemeral/modifications/evidence/gtwpe-tw-model-advice/skill_edits.py > <scratch>/skill_edits.py
       PYTHONDONTWRITEBYTECODE=1 python3 <scratch>/skill_edits.py <synced root> <scratch>/rebuilt
       diff -r <scratch>/rebuilt/tw-flowmaster <extracted>/tw-flowmaster
       diff -r <scratch>/rebuilt/flowmaster-validate <extracted>/flowmaster-validate
     Read each tool's own top-level flag by name. A green section count beside a false suite flag
     means the suite failed. In the guard proof, a "guard disabled" case exits 1 on the validator's
     own changed digest with no tw-flowmaster error; that is its expected result.
  c. Confirm the extracted trees differ from the installed tree only in the files listed here, and
     that the list accounts for every difference:
       tw-flowmaster/SKILL.md
       flowmaster-validate/SKILL.md
       flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json
       flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py
       flowmaster-validate/scripts/validate_flowmaster.py
       flowmaster-validate/scripts/validate_gcfpe_20260914.py
     (derived by `diff -rq` of each installed tree against its built tree, and pasted.)
  d. Check: the Primary core block identity (C2); CONTRACT_REQUIRED["tw-flowmaster"] requires
     revision 1.3.0 and no longer PRE_CREATION_ASSESSMENT, PRE_APPLY_ASSESSMENT or
     ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN; CONTRACT_FORBIDDEN["tw-flowmaster"] adds exactly
     TW-ASSESS-10, PRE_CREATION_ASSESSMENT, PRE_APPLY_ASSESSMENT, STRENGTH_ANALYZER_PROMPT_ID,
     APPLICATION_REASONING_POLICY and PF_RENDERED_PAGE_COUNTS; the profile condition and READY's
     route (C3); a broad search of tw-flowmaster's specialization (between
     `<!-- FLOWMASTER_SPECIALIZATION_BEGIN -->` and `<!-- FLOWMASTER_SPECIALIZATION_END -->`) for
     assess, analyzer, strength, model, effort, reasoning, surface, workload, profile, advice,
     recommend, appraisal, openai-docs, Ultra, Max, Astra, Sol, GPT, rendered, page count and
     checkpoint, each hit read in context and classified against C3's exceptions.
  e. Recompute flowmaster-validate's SKILL_TREE_SHA256 from its extracted tree and confirm the
     declaration equals it; recompute both tree digests; find every pin of the validation profile
     (by path or hash) in the root and confirm each consumer agrees (A3).
  f. Recount by grep, independently of the author's list: `validator_revision` "3.3.2" at its four
     sites and no "3.3.1" left as a current revision; FLOWMASTER_VALIDATE_REVISION 3.3.2;
     TW_FLOWMASTER_SPECIALIZATION_REVISION 1.3.0.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  - skill_edits.py on the installed trees: exit 0, 32 edits; SKILL_TREE_SHA256 284b3ac1…d1fd733.
  - validate_flowmaster.py --strict-warnings on the isolated root (29 skills): exit 0,
    verdict FLOWMASTER_SUITE_PASS, suite_ok true, self_identity OK, validator_revision 3.3.2,
    finding_counts all 0, warnings []; skills change-flow, flowmaster-primary, flowmaster-validate,
    session-branch-flowmaster, session-relay-flowmaster and tw-flowmaster each PASS with 0 errors and
    0 warnings; change-flow fixtures 32 passed, 0 failed (13 positive, 19 negative).
  - guard_proof.py: 12 of 12 PASS, exit 0.
  - Primary core block: 18255 bytes, identical in installed tw-flowmaster, built tw-flowmaster and
    flowmaster-primary.
  - Each archive extracted equals its built tree (diff -r, no output); 2 and 31 entries, none
    outside its root.

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation as carrying to these bytes. Write nothing in the
repository at /home/user/glow-hdengine-v2: no file, commit, branch, checkout, fetch, push or pull
request, and no change to its working tree; read it only through `git show`. Do not read, write or
fetch anything in Notion, and fetch no prompt body (D22). Do not edit or delete the archives. Do not
spawn agents or start sessions. Write nothing outside your own scratch directory.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Your final message is your record: the authoring session captures it unedited from your transcript
to the capture path named for your REVIEWER_ID, and you write no file yourself. Give it a
"## Canon relied on" section listing the PF titles and sections, and the repository documents, you
relied on (AGENTS.md requires that in every artifact; the repository's hook checks for it).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
