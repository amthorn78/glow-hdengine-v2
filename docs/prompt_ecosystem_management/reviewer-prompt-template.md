---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.2"
created_date: 2026-09-21
revised_date: 2026-09-24 — D26, a second template for ANALYZE and PLAN reviews (1.1, 2026-09-23: D24, delivered to reviewer subagents rather than pasted by Nathan)
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Standard skill reviewer prompt — canonical template — 2026-09-21*
---

# Standard skill reviewer prompt — canonical template

This file holds two canonical templates. **The first, below, is for skill reviews** (`D24`). **The
second, *ANALYZE and PLAN review brief*, is for reviews of a Modification's analysis or plan**
(`D26`). Both are filled, committed under `docs/ephemeral/` before any reviewer is spawned, and given
to fresh-context reviewer subagents as their only brief. Both run under `D26`'s bounds: a dry run
first, at most two full reviews and one check of the repair's diff per mode.

Every skill handover uses this template. Do not compose a reviewer prompt from scratch. Fill the
slots, delete nothing. Filled instances are release-scoped and belong in `docs/ephemeral/`.

Standing rule, Product Owner direction 2026-09-21. **Every skill handover uses this template.** Do not compose a reviewer prompt from scratch, and do not re-derive the mandatory elements from `Skill packaging and installation` each round — they are already built into the sections below. Fill the slots, delete nothing.
Added after a session wrote a bespoke reviewer prompt without reading the rules that govern one, and shipped it missing five mandatory elements. A template removes the opportunity.
**How to use it.** Copy the fenced block, replace every `<SLOT>`, and write `NONE` in any section that is genuinely empty. Commit the filled instance under `docs/ephemeral/` beside the round's report **before** the review starts. Then spawn two reviewer subagents with fresh context — never forked or context-inheriting. Give each this filled prompt as its only brief, with its own `<REVIEWER_ID>` and its own record path (`D24`). Each writes its verdict to that file, and the author never edits it.
**Verdict vocabulary is fixed.** `SKILL_FIT_CONFIRMED` or `SKILL_REPAIR_REQUIRED`. Never invent a verdict set; a reviewer's words have to match the record they land in.
```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
<for each package: NAME.skill, N files, N bytes, sha256 ...>
<state whether the packages install together or independently>

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
<prior verdict, its date, and the exact digests it was issued against — or NONE, first review>
<which digests have changed, and therefore what carries and what is void>
<any finding carried forward, by ID, with its current disposition>

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline the diff was taken against: <N files>, digest <VALUE>, by the recipe at <PATH>.
Repaired tree: <N files>, digest <VALUE>.
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.
<any superseded or unreproducible identity value, named so it is not chased>

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository <OWNER/REPO>. Branch <BRANCH> — read its HEAD, not a pinned commit.
<MERGED or NOT MERGED — if not merged, say so explicitly, or the reviewer will look on main and
find nothing.>
**If that branch does not exist when you look, it merged and was deleted.** Read the same paths on
main. <name the pull request the branch is expected to merge as, if it is open, so the reviewer can
confirm rather than guess.>
<each artifact by path: report, diff, digest recipe, predecessor records>
Read <governing file, e.g. AGENTS.md> first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
<C1..Cn, in the author's own words, phrased as claims to be tested rather than conclusions to be
accepted. Include the authority the change rests on, quoted where it was given verbatim.>

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
<A1..An, weakest first. Name the author's least-confident reasoning, the checks the author
constructed to test their own work, and anything the author checked partially and stopped. A
reviewer pointed at the soft parts finds more than one left to browse.>
<Any question the round deliberately did not settle, marked as a question, not a finding.>

=== 7. KNOWN LIMITS, VOLUNTEERED ===
<L1..Ln. Anything the reviewer cannot reproduce — corpora living outside the repository above all,
with how to obtain them. State these up front rather than leaving them to be discovered.>

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm `name:` in each SKILL.md frontmatter is unchanged.
  b. Extract into a clean tree, restore the untouched sibling skills the tooling needs, and run the
     gates FROM THE EXTRACTED CONTENTS, not from any working copy:
       <exact commands, one per line, with required arguments>
     Read each tool's own top-level flag by name. A green section count beside a false suite flag
     means the suite failed.
  c. Confirm the extracted trees differ from the installed tree only in the files listed here, and
     that the list accounts for every difference:
       <every changed file, DERIVED by `diff -rq` or `git diff --name-only` against the baseline
       tree and pasted, never typed from memory. A revision bump touches every revision site, so a
       file whose only change is the version string still belongs on this list.>
  d. <change-specific structural checks: rosters, contracts, pins, counts>
  e. <recompute every hash pin from its artifact and confirm each consumer agrees with it>
  f. <recount every versioned site by grep, independently of the author's list>
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  <each gate and its expected result>

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation as carrying to these bytes. <project-specific
prohibitions: read-only paths, sources that must not be edited, prompt bodies>

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
<On a re-review: the disposition of every prior finding — fixed, declined with reasoning, or
deferred — and any defect found while fixing them.>
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
## Why each section is there
Each maps to a mandatory element in `Skill packaging and installation`, so filling the template satisfies that rule by construction: §1 the scoped digests, §2 the prior verdict and what carries, §3 the baseline, §4 the repository evidence, §5 the claims in the author's words, §6 the attack priority, §7 the volunteered limits, §10 the deliverable and its vocabulary. §8 and §9 carry the packaging procedure's own step 4 and the freeze rule.
**A reviewer that has to ask for any of this has already lost a round.**

---

# ANALYZE and PLAN review brief — canonical template

For a review of a Modification's `§A` or `§P` (`D26-A`). Replaces the three-lenses-plus-verifiers
pattern whose rounds ran eight times on `MODIFICATION-20260923-closeout-residuals`.

**How to use it.** Run the dry run first and record it in the Modification's `reviews` ledger
(`kind: DRY_RUN`). Then copy the fenced block, replace every `<SLOT>`, write `NONE` in any section
that is genuinely empty, and commit the filled instance under `docs/ephemeral/` **before** spawning
the reviewers. Spawn two reviewer subagents with fresh context, never forked or
context-inheriting, each with its own `<REVIEWER_ID>` and record path. Each writes its own record,
and the author never edits it (`AUTH-001`). The author then enters the round in the `reviews`
ledger with its count of distinct confirmed required defects.

**The author fills in the attack list, not the rubric.** §3, §5 and §6 are fixed text: the
required-finding rubric, the cap and the exit are not the author's to widen or tighten.

```plain text
You are <REVIEWER_ID>, reviewing <MODE: ANALYZE or PLAN> of <MODIFICATION_ID>. You did not author it.
This is full review <1 or 2> of at most 2 for this mode (D26-A). <For review 2: the prior round's
record path, and the repair diff you are reviewing against it.>

=== 1. WHAT YOU ARE REVIEWING ===
Repository <OWNER/REPO>, branch <BRANCH>, commit <SHA>. Read that commit, not the branch head.
The record: docs/ephemeral/modifications/<MODIFICATION_ID>.md, section <§A or §P>.
Its evidence: <paths>. Its governing documents: docs/prompt_ecosystem_management/ — read
gcfpe.decision-record.md D20-D26, modification-template.md and ecosystem-change-management.md.
The dry run that preceded you: <path to its output>, <its result, one line>.

=== 2. WHAT IT CLAIMS, AS CLAIMS ===
<C1..Cn in the author's own words, to be tested rather than accepted.>

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
<A1..An, the author's least-confident reasoning first. Name what the dry run did not exercise.
No instruction to "try hard", "be exhaustive" or "find everything": the list is the attack.>

=== 5. THE CAP AND THE EXIT — FIXED TEXT, DO NOT EDIT ===
After at most two full reviews and one check of the repair's diff, the output goes to Nathan with
every open finding listed by path, likelihood and consequence, however many there are. The session
stops early and returns to Nathan if distinct confirmed required defects do not at least halve from
the previous round, or if most of this round's findings sit in text the last repair added. Zero
findings is not the exit, and no session may make it one. LISTED findings are not repaired unless
Nathan opts in.

=== 6. THE DELIVERABLE — FIXED TEXT, DO NOT EDIT ===
Write your record to <RECORD_PATH>. First line: the count of distinct confirmed REQUIRED findings.
Then each REQUIRED finding: rubric class (R1-R4), the exact text or step, the evidence, the smallest
correction, and whether it is in text the last repair added. Then each LISTED finding, one line
each. On review 2: the disposition of every prior REQUIRED finding (fixed, not fixed, or fixed with
a new defect), and the trend in the count.
Do not edit the record under review, merge, install, write to Notion, or edit a prompt body.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

**Why it is shaped this way.** The eight PLAN rounds had no likelihood test for "required", no cap,
"clean" as the only exit, an attack list the author widened each round, and 25–33% duplicate
reports across three lenses and three verifiers. §3 and §5 are fixed so none of that can be brought
back by filling the slots (`D26-A`; recovery analysis §7; RCA §7 actions 1–3).
