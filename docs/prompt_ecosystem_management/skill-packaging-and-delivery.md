---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Skill packaging and installation — 2026-09-20* and *Delivered artifacts must be identifiable from their filename — 2026-09-21*
---

# Skill packaging, delivery and identification

How a skill is packaged and handed over, and why the handover needs a digest rather than a filename.
Install verification and the digest recipe are in `skill-identity-and-freeze.md`.

## Skill packaging and installation

How a worker session hands Nathan an installable skill. Added after a session wasted a turn delivering a `.tgz` and then loose `.py` files, neither of which can be installed.
### The constraint
Installed skills live in a **one-way synced directory** (`/root/.claude/skills/synced/<bucket>/`). A worker session **cannot install or update a skill** and must never write into that directory. **Nathan alone installs.** A worker edits a copy, packages it, and hands over the package.
### The deliverable is a `.skill` file — never anything else
A `.skill` file is a zipped skill folder. When delivered with `SendUserFile`, its file card shows a **Save skill** button that installs it. Nothing else installs:
| Do not hand over | Why |
|---|---|
| `.tgz` / `.zip` / tarball | Not installable; Nathan cannot open it |
| Loose `.py` / `.md` files | A diff, not a skill; destination is ambiguous |
| A list of edits or a patch | Requires manual reconstruction |
| Renamed files encoding a path | Still not installable |
One `.skill` per skill changed. Two skills changed means two `.skill` files.
### Procedure
`skill-creator` is the governed packaging mechanism. Its scripts must be run **from the ****`skill-creator`**** directory** so `scripts` resolves as a package.
**1. Copy before editing.** The installed path is read-only. Copy the whole skill folder to a writeable location and edit there.
**2. Keep the name.** For an update, the directory name and the `name:` field in `SKILL.md` frontmatter must stay **unchanged** — that is what makes it update the existing skill in place rather than create a variant. Never `-v2`, never a new name.
**3. Validate, then package:**
```bash
cd <skills-root>/skill-creator
python3 -m scripts.quick_validate <path/to/skill-folder>
python3 -m scripts.package_skill <path/to/skill-folder> <output-dir>
```
Expect `Skill is valid!` then `✅ Successfully packaged skill to: <output-dir>/<name>.skill`. The packager automatically excludes `__pycache__`, `node_modules`, `*.pyc`, `.DS_Store`, and a root-level `evals/`.
**4. Verify by installing it yourself — do not skip this.** Extract the `.skill` into a clean directory, add back any untouched sibling skills the tooling needs to resolve, and run that skill's own gates **from the extracted contents**, not from the working copy. This is what catches a reference file dropped during packaging. Confirm `name:` survived and the intended change is present.
**5. Deliver** the `.skill` file(s) with `SendUserFile`, and state what changed, where each file installs, and what Nathan should see after installing.
### Reading a validator's result
Read each tool's **own top-level flag** by name — `ok`, `fixture_suite_ok`, `suite_ok`/`verdict`, and the suite result. A green subsidiary section flag while the overall flag is false is meaningless, and a green section count (for example "33/33 passed") next to `fixture_suite_ok: false` means the suite failed.
### Independent validation is mandatory — for every skill change, not only GCFPE
Standing rule, Product Owner direction 2026-09-21: **no skill change is trusted until a party that did not author it has validated it.** The author's own gates passing is necessary and never sufficient — an author validates what they thought they built.
**Independent means a different session or reviewer**, one that did not write the change, working from the package and the repository rather than from the author's summary. Its finding is what makes a package installable-with-confidence; a green run by the author alone is corroboration.
**A verdict is scoped to exact bytes, and does not carry.** Bind every confirmation to the `.skill` digests it was issued against. If any byte changes afterwards — a one-line fixture rename included — the confirmation is void for the new bytes and the change needs its own pass. This is the rule that keeps "we already reviewed that skill" from covering something nobody reviewed.
**Every handover includes a paste-ready reviewer prompt.** Standing rule, Product Owner direction 2026-09-21: a `.skill` delivered without one is an incomplete handover. Nathan is the courier between the worker session and the reviewer, and he should never have to compose the brief himself or reconstruct it from the report. The prompt is delivered in the same message as the package, in a single copyable block.
What the prompt must carry, because a reviewer that has to ask for any of these has already lost a round:
- **The exact digests, file counts and byte sizes** the verdict is to be scoped to, and the prior verdict with the digests it was issued against, so the reviewer can see what does and does not carry.
- **Where the repository evidence is** — branch, commit, and the paths of the report and the diff.
- **The baseline** the diff was taken against, by digest and file count, so identity can be reproduced before anything else.
- **What the change claims**, in the author's own words, stated as claims rather than as conclusions.
- **What to attack, in priority order.** Name the weakest parts. A reviewer pointed at the author's least-confident reasoning finds more than one left to browse.
- **Known limits, volunteered.** Anything the reviewer cannot reproduce — corpora that live outside the repository above all — stated up front rather than left as a discovery.
- **The deliverable and its vocabulary**: the exact verdict set, the scoping instruction, and for a re-review, the instruction to write a successor record rather than correct the earlier one (`AUTH-001`).
On a **re-review**, add the disposition of every prior finding — fixed, declined with reasoning, or deferred — and any defect found while fixing them. A reviewer re-reading a package deserves to know what moved.
**Practical consequence, learned the expensive way:** batch small corrections into one change rather than shipping them one at a time. Three separate one-line fixes cost three independent reviews; one change carrying all three costs one.
**Prevent bytecode rather than excluding it.** Run every validator with `PYTHONDONTWRITEBYTECODE=1`. The Freeze rule below is right that `__pycache__` is not a content change, but a stray `.pyc` has been packaged into a `.skill` before and was caught only by a file count — preventing it is cheaper than reasoning about it.
### GCFPE tie-in
The GCFPE plan's §10 requires that any approved skill edit be made with `skill-creator`, preserve unrelated behaviour, be committed and read back, and then have the dedicated skill review re-run against the **final installed snapshot**. Packaging is not the end of the gate — the review still has to run after Nathan installs.
### Freeze rule
No skill may be installed while a review is running. A review that judges a moving snapshot is void. Freeze the tree, hash it, review, then re-hash and confirm nothing moved. Note that merely *running* a bundled Python validator writes `__pycache__/*.pyc` into the tree; that is expected, is not a content change, and should be compared with `__pycache__` excluded.

## Delivered artifacts must be identifiable from their filename


Product Owner direction, 2026-09-21: *"it is difficult for me to identify skill packages and prompts because they are not uniquely identified in the file names."*
**It has already cost two rounds.** Both failures are the same root cause and neither was caught by any gate.
| incident | what happened |
|---|---|
| **wrong package installed** | Two `.skill` files delivered four hours apart, both named `flowmaster-validate.skill`. The withdrawn round-24 package was installed instead of round 25's, and ran for a full round behind green gates |
| **wrong reviewer prompt pasted** | Four reviewer prompts delivered across rounds 23–26, all named `REVIEWER-PROMPT.md`. `SFR-01` was handed the round-24 text with the round-26 package, caught it at the §3 baseline check, and stopped |
The second one only ended well because the reviewer verifies the baseline before reviewing. That is a control working, not a reason to keep producing the collision.
### The `.skill` filename cannot carry a version, and that is not negotiable
`skill-creator`'s own instructions are explicit: *"Preserve the original name. Note the skill's directory name and **`name`** frontmatter field — use them unchanged. E.g., if the installed skill is **`research-helper`**, output **`research-helper.skill`** (not **`research-helper-v2`**)."* The packager derives the filename from the skill directory name, and the install path depends on it.
**So every version of a skill will always arrive looking identical.** The fix cannot be the filename. It has to be the delivery and the verification:
1. **Lead the caption with the sha256**, not the round number. The digest is the identity; the round is a label.
2. **One ****`.skill`**** per message.** Never two packages of the same skill in one message, and say explicitly which earlier delivery is superseded.
3. **Verify after installing** — the post-install digest comparison is mandatory and is the only control that catches this. See `skill-identity-and-freeze.md`.
### Everything that is NOT a `.skill` file must be uniquely named
There is no constraint on these and no excuse for the collision. From now on:
| artifact | name it |
|---|---|
| reviewer prompt | `REVIEWER-PROMPT-r26.md` — round in the filename, never bare |
| repair report | `REPORT-r26.md` |
| §10 review record | `SECTION-10-REVIEW-r26.md` |
| patch | `round26.patch` — already correct, keep it |
| any successor or correction | the round it belongs to, plus `-v2` where it supersedes a sibling |
The round directory is not sufficient. A file gets detached from its directory the moment it is delivered as a card, pasted into a session, or downloaded — and that is precisely when the identification matters.
### The standing rule
**An artifact that leaves the repository must be identifiable from what travels with it.** For a file that can be renamed, that is the filename. For a `.skill`, which cannot, that is the digest in the caption and the digest check after installing. Deciding which artifact you are holding must never require reading its contents and inferring.
