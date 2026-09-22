---
artifact_type: SKILL_REVIEWER_PROMPT
artifact_version: "1.0"
created_date: 2026-09-22
task: PE36 Task 01 — Notion write-boundary skill revision
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md
---

# Reviewer prompt — PE36 Task 01

Paste the block below to the reviewing session, together with the three `.skill` files.

```plain text
You are SFR-PE36-T01, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
glow-workspace-currency.skill   3 files   13,536 bytes
  sha256 6491301202e7d310ff9785bb1fc36a8c45d6b704ad8d6e65a3fa37c52885eecb
glow-artifact-storage.skill     1 file     4,850 bytes
  sha256 8a7c074e39dc30a436b0c330290c0f60048f9842d6dbb80324b889edc5c69cfd
glow-write-boundary.skill       1 file     4,199 bytes
  sha256 cfe2d7a900c36ea67a413282cff758c66c181a3e85cc543aeaba2425619ad494

These three install INDEPENDENTLY. No package depends on another; each is a prose-only skill with
no bundled scripts. You may confirm or reject them individually, but give one verdict per package.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
NONE. This is the FIRST independent review of any of these three skills. The repository was
searched for a prior SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED naming them and there is none.

The round-30 verdict SKILL_FIT_CONFIRMED is bound to ed7041c0… and 0e00084e… and covers
change-flow and flowmaster-validate only. It is void for these bytes and does not carry. Those two
skills are NOT part of this change and their installed digests are unchanged — confirm that:
  change-flow          21 80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8
  flowmaster-validate  29 b9ca212ac1275f16af12d34ad15d3df6e95fc71a95f2ce1ab56ee7245a3317af
An unchanged skill proving unchanged is evidence; assuming it is not.

No findings are carried forward — there are none to carry.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Recipe: docs/prompt_ecosystem_management/freeze.py, rooted at the SKILL DIRECTORY, never at the
synced tree. Format below is "<file count> <sha256>".

Baseline the diff was taken against — the currently installed trees:
  glow-workspace-currency  3 0beffb2a3bf14274c7088ab260eb5f44c6842ca02400cc3de22de2e7be226dbe
  glow-artifact-storage    1 895488910744a108e193ab8cb76d4f9fa3e02e8903323bfea3009e70c2d5e6a7
  glow-write-boundary      1 c0e3875b4e932e516b75962d37c5bafaf57664eef9de1e036009c96c03e50a27

Repaired trees, as extracted from the .skill files:
  glow-workspace-currency  3 5f2b4ae0d43f0609ae3c3b88409a2578791b008cf6908bd6516181688e06dd93
  glow-artifact-storage    1 502b4ecf11cea156702207ddb829b2d51064fe9eaa8678ac5db05c04375cba1c
  glow-write-boundary      1 662f9647ccfd996aa72e3d80ac70edc3d06a4310805ef14207b1340c69e93fc4

Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.

Superseded or unreproducible identity values, named so you do not chase them:
  - These three skills carry NO advertised identity value — no SKILL_TREE_SHA256, no
    *_REVISION constant, no version: frontmatter key. Frontmatter is exactly `name` and
    `description`. There is nothing to diff for the "advertised identity must be unspent" rule
    and nothing was added. See A1 below — this is a deliberate decision you should attack.
  - Do NOT compare against the synced-tree whole-directory digest. It is hostage to unrelated
    Anthropic skills the sync layer updates.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2.
Branch docs/20260922-pe36-task01-skill-write-boundary — read its HEAD, not a pinned commit.
NOT MERGED at the time this prompt was written. Nathan merges; PE36 never does.
If that branch does not exist when you look, it merged and was deleted — read the same paths on
main. If a pull request is open for it, confirm the branch HEAD against the PR rather than
guessing; PE36 could not open the PR itself (no GitHub CLI or PR tool in its session), so the PR
may have been opened by Nathan under a number PE36 never saw. Do not treat a missing PR as a
finding about the change.

Artifacts, by path:
  docs/ephemeral/pe36.task-01/TASK-01-skill-write-boundary-revision.md  the authorizing brief
  docs/ephemeral/pe36.task-01/REPORT-pe36-task01.md                      the report
  docs/ephemeral/pe36.task-01/pe36-task01.diff                           the full unified diff
  docs/ephemeral/pe36.task-01/REVIEWER-PROMPT-pe36-task01.md             this prompt
  docs/prompt_ecosystem_management/notion-write-boundary.md              the governing policy
  docs/prompt_ecosystem_management/session-working-rules.md              the wording converged on
  docs/prompt_ecosystem_management/skill-identity-and-freeze.md          the digest recipe
  docs/prompt_ecosystem_management/prompt-body-content-policy.md         "skill identity belongs
                                                                          to the skill's own digest"
  docs/prompt_ecosystem_management/pe-succession/pe35-to-pe36.md         predecessor record

Read docs/prompt_ecosystem_management/authoritative-surfaces.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
The authority, quoted verbatim from notion-write-boundary.md's record of the Product Owner's
policy: "a development prompt that is executing the ecosystem flow may read the required Notion
prompt pages and operational records, but it must not write anything to Notion unless the
instruction for that specific task explicitly directs a Notion write." And, authorizing this
round: "I do want a skill revision then. Pass that over to the new session as the first task".

C1. The obligation to record every state change, in the session that produced it, and to read it
    back before claiming it, is UNCHANGED in glow-workspace-currency. Only the destination is now
    conditional on session kind.
C2. The six triggers in glow-workspace-currency's "Record — what counts as a state change" are
    byte-identical to the baseline. Nothing was removed from them.
C3. The destination table added to that skill is converged wording, copied from
    session-working-rules.md's "Tracking is part of the work", not newly invented phrasing.
C4. glow-artifact-storage's description now carries the durable-asset carve-out the policy asked
    for, and remains within the 1,024-character limit at 995 characters.
C5. glow-write-boundary now routes the five excluded prompt categories somewhere other than
    Notion, and its description was not changed because it states no Notion-write obligation.
C6. Exactly four files differ from the installed trees. drive-retrieval.md is unchanged.
C7. A fourth instance of the same conflicting sentence was found in
    glow-workspace-currency/references/notion-operations.md and corrected in the same change.
    This is an in-scope skill's reference file, not a fourth skill.
C8. No advertised identity value was bumped because these three skills have none, and inventing
    a version: field was judged to create a second identity surface that could disagree with the
    digest.
C9. No Notion write was made and none was authorized for this task.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. C8 is the author's least-confident reasoning and it departs from a literal line in the
    authorizing brief, which says "Bump each skill's own version." Decide whether the digest
    alone is sufficient identity for these packages, or whether the brief meant something the
    author has read away. This is the finding most likely to be real.
A2. glow-workspace-currency's DESCRIPTION is permanently in every session's context, so a
    triggering regression is the most expensive possible defect here and no gate tests for it.
    AF-003 records that skill triggering is probabilistic and that four very different
    descriptions scored 1-2/10, possibly selecting on noise. The author deliberately did not
    measure a trigger rate. Read the old and new descriptions side by side and judge whether the
    trigger surface actually survived, or whether "recording ... at the destination that holds it"
    reads as weaker instruction than "writing ... back to Notion" and will fire less often or
    be obeyed less.
A3. Test C1 adversarially: does the revised skill still force a session to record a blocked
    verdict, an abandoned task, and an UNCHANGED verdict? Those are the three cases the skill was
    written for, and the plan-page failure it cites is exactly the unchanged-verdict case. If a
    reader could now conclude "I am a development session, so I need not record this at all",
    the change has gutted the skill and the correct verdict is SKILL_REPAIR_REQUIRED.
A4. The "Where it lands" table asks a session to classify itself as maintaining vs executing.
    Attack that boundary. Find a real session kind that fits neither cleanly, and check whether
    the stated default ("treat yourself as executing") is actually safe for it.
A5. The author checked the brief's three quotations against the installed bytes and found a
    fourth instance, but stopped at the three named skills plus their reference files. The author
    did NOT audit any other installed skill for the same conflict. Treat that as a known
    incompleteness, not a finding, unless you find an instance.
A6. C6 says exactly four files. Derive that yourself with diff -rq and contradict it.
A7. glow-artifact-storage's description sits 29 characters below a hard 1,024 limit. Confirm the
    count yourself. A first attempt at this edit ran to 1,069 and was rejected by the validator.

Questions the round deliberately did not settle — these are questions, not findings:
Q1. Should these three prose skills acquire a durable advertised identity (a version: key, or a
    revision constant) as a standing convention, so future packages are distinguishable without
    the digest? PE36 says no and gives its reason; the question is open for the Product Owner.
Q2. Should the remaining installed skills be swept for the same unqualified "prompts are
    authored in Notion" sentence? PE36 did not, because the brief scoped this to three.

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. These are PROSE skills. They bundle no scripts, no fixtures, no validator, no hash-pin chain
    and no self-identity check. The only executable gate is skill-creator's quick_validate, which
    checks frontmatter and structure — NOT meaning. Everything substantive here is a careful read
    and a diff. Do not expect a suite to run, and do not accept a green quick_validate as
    evidence that the prose is correct.
L2. The 55 prompt bodies live in Notion and are never mirrored to disk
    (prompt-corpus-policy.md). Reading them is unrestricted and requires no authorization;
    copying, hashing or byte-comparing them is absolutely prohibited. No prompt body was touched
    by this change and none needs to be read to review it.
L3. PE36's session had no GitHub CLI and no PR tool, so it could not open a pull request. The
    branch is pushed. If you cannot find a PR, that is an environment limit, not a defect.
L4. PE35's transcript is not available and is not a system of record. Neither is PE36's.
L5. The author cannot measure skill trigger rates from its own session, so A2 cannot be settled
    empirically by either of us. Judge it by reading.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm `name:` in each SKILL.md frontmatter is unchanged against the
     installed tree.
  b. Extract into a clean tree and run the gates FROM THE EXTRACTED CONTENTS, not from any working
     copy. There are no sibling skills to restore; these three have no cross-skill tooling.
       cd <skills-root>/skill-creator
       python3 -m scripts.quick_validate <extracted>/glow-workspace-currency
       python3 -m scripts.quick_validate <extracted>/glow-artifact-storage
       python3 -m scripts.quick_validate <extracted>/glow-write-boundary
       python3 <repo>/docs/prompt_ecosystem_management/freeze.py <extracted>/<each skill>
     Read each tool's own top-level flag by name. A green section count beside a false suite flag
     means the suite failed.
  c. Confirm the extracted trees differ from the installed tree only in these files, and that the
     list accounts for every difference. Derive it with diff -rq; do not type it from memory:
       glow-workspace-currency/SKILL.md
       glow-workspace-currency/references/notion-operations.md
       glow-artifact-storage/SKILL.md
       glow-write-boundary/SKILL.md
     glow-workspace-currency/references/drive-retrieval.md must be byte-identical. Exclude
     manifest.json — it is sync-layer bookkeeping, not skill content.
  d. Structural checks specific to this change:
       - hash the six-trigger block in both the baseline and the extracted
         glow-workspace-currency/SKILL.md and confirm they are equal (author measured fd571777…)
       - confirm every heading present in each baseline SKILL.md is still present
         (11 / 13 / 8 headings respectively)
       - confirm "Consult before you act." and "Verify before you claim." both survive verbatim
       - confirm "An unverified write described as done is the exact failure this skill exists to
         prevent." survives — it is line-wrapped, so match across the newline
  e. Recount the description lengths yourself, per skill, and confirm each is at or under 1,024:
     author measured 898 / 995 / 723.
  f. grep the three extracted trees for any remaining unqualified instruction to write to Notion.
     The author claims four were found and four were fixed. Find a fifth.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  quick_validate, working trees                  Skill is valid! x3
  quick_validate, extracted contents             Skill is valid! x3
  freeze.py, extracted == working tree           match x3
  diff -rq extracted vs installed                exactly 4 files
  six-trigger block, baseline vs revised         sha256 equal
  description lengths                            898 / 995 / 723, limit 1024
  change-flow, flowmaster-validate installed     unchanged, 80e877c2… and b9ca212a…
  bytecode written                               none

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation as carrying to these bytes.
Do not write anything to Notion — reading it is unrestricted, writing it is not authorized for
this review, and this change is itself about that rule.
Do not copy, mirror, hash or byte-compare any prompt body (prompt-corpus-policy.md).
Do not write to docs/pfcanon/ — it is read-only.
Do not touch HDE-EPIC040, PR #457, AF-001 through AF-004, or the reconciliation backlog.
Do not fold a fourth skill's conflict into this change if you find one. Report it.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the three digests in §1 and state that it is void for any other bytes. For each
finding give the artifact, the exact defect, the evidence, and the smallest correction. Answer
every §6 question (Q1, Q2) explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a
result. Given L1, say plainly how much of your verdict rests on reading rather than on a gate.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
