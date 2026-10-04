SFR-TW1-1, D24 skill review, round tw1: **SKILL_FIT_CONFIRMED**

This verdict covers exactly these two packages, installed together, and is void for any other bytes:
- `tw-flowmaster.skill`: 19,193 bytes, 2 entries, sha256 `88166c3d48fee16900e125f1cf2fe15cf2b46a2e0a6ac05ea0fdd5ef3c1a4b89`. Extracted tree: 2 files, 55,131 bytes, digest `0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c`. `SKILL.md` is 54,711 bytes, sha256 `21c632e1b92a6096bb521d990fde1d7aee383af029e7f0e99fce68eac09b1575`.
- `flowmaster-validate.skill`: 322,860 bytes, 31 entries, sha256 `e1f495b3f40f9a75c713433236391763505cb3895364076f71eb771a72710f3f`. Extracted tree: 31 files, 1,915,296 bytes, digest `284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733`, which equals the declared `SKILL_TREE_SHA256`.

No required defect was found (`D26-A` rule 3). There are three listed findings (LF-1 to LF-3) and none of them blocks the packages. This is the first review of these bytes and corrects no earlier record (`AUTH-001`). I ran it from 2026-10-04T13:38Z to about 13:52Z against branch head `80d226c` (main is at `f83c755`).

## Freeze
- **Start:** both archives matched §1 byte for byte. I also took a content snapshot of the synced directory: 338 files, `manifest.json` excluded.
- **End (13:50:31Z):** both archives were unchanged, still read-only, with modification time 13:34:01. The synced skill content was identical to the start snapshot. No `__pycache__` was written anywhere.
- Only the sync layer's `manifest.json` was rewritten (at 13:34 and 13:44). The freeze convention excludes that file, and no skill content moved.
- Branch head stayed at `80d226c`. The repository working tree stayed clean. Nothing moved, so the review stands.

## Gates I ran myself
Everything below was run with `PYTHONDONTWRITEBYTECODE=1`, in `review-SFR-TW1-1/` only.

**§3, baseline:** it reproduced before I reviewed anything.
- Installed `tw-flowmaster`: 2 files, 58,775 bytes, digest `fd6c344b…f5576617`, revision 1.2.0.
- Installed `flowmaster-validate`: 31 files, 1,914,948 bytes, digest `ed52208f…3cc572af`, equal to its declared digest, revision 3.3.1.

**§8a, the archives:**
- Each archive's sha256, size and entry count match §1.
- No directory entries, no symbolic links, no traversal sequences, and no entry outside its skill root.
- The `name:` frontmatter is unchanged in both `SKILL.md` files.
- Extracted, both trees match the §1 tree digests.
- `skill-creator`'s `quick_validate`, run from my root's copy of it, reports "Skill is valid!" for both skills.

**§8b, the gates, run from a fresh extraction:**
- **Isolated root:** 29 skill directories. That is the 30 synced directories, without canva, with the two extracted skills in place of the installed ones.
- **`validate_flowmaster.py --strict-warnings`:**
  - Exit 0.
  - `verdict` FLOWMASTER_SUITE_PASS, `suite_ok` true, `self_identity` OK, `validator_revision` 3.3.2.
  - `finding_counts` all 0. `warnings`, `advisories` and `findings` all empty.
  - Six skills each PASS with 0 errors and 0 warnings: change-flow, flowmaster-primary, flowmaster-validate, session-branch-flowmaster, session-relay-flowmaster and tw-flowmaster.
  - Change-flow fixtures: 32 of 32 pass (13 positive, 19 negative), and `fixture_suite_ok` is true.
  - GCFPE current fixtures: 236 cases, `fixture_suite_ok` true. Section 13: 37 of 37, and 38 of 38 variants.
- **`guard_proof.py`:** 12 of 12 PASS, exit 0.
  - I reproduced one "guard disabled" case by hand. Its only failure is `SKILL_SELF_IDENTITY:DECLARED_284b3ac150be_MEASURED_76e22e7bc4c1`, reported under change-flow as `FMV-GCF-CURRENT-001`. It has no tw-flowmaster error, which is the expected result.
- **`skill_edits.py` on the synced root:** exit 0, 32 edits, `SKILL_TREE_SHA256 284b3ac1…d1fd733`. Both `diff -r` comparisons of the rebuilt trees against the extracted trees produce no output, so C1 holds.

**§8c, the difference list:** `diff -rq` of the installed trees against the extracted trees lists exactly the six files the brief names, and nothing else. The diff bodies are exactly the 32 edits.

**§8d, the contracts and the search:**
- **Primary core (C2):** the `FLOWMASTER_CORE_BEGIN` to `_END` block is 18,255 bytes, sha256 `4d8bb9bf…f9d409`. It is identical in installed `tw-flowmaster`, built `tw-flowmaster` and `flowmaster-primary`. Lines 9 to 229 are identical between the old and new file.
- **`CONTRACT_REQUIRED["tw-flowmaster"]`:** it requires `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.3.0`. It no longer requires `PRE_CREATION_ASSESSMENT`, `PRE_APPLY_ASSESSMENT` or `ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN`.
- **`CONTRACT_FORBIDDEN["tw-flowmaster"]`:** it adds exactly the six identifiers.
  - The match is case-insensitive over the whole file. A lowercase `tw-assess-10` I injected was reported.
- **Broad-term search (C3):** hits in the specialization are on lines 239, 280, 310, 312, 314, 318, 326, 328, 330, 339, 345, 346, 348, 386, 434, 444, 459 and 474. I read each in context, and each falls within one of C3's exceptions:
  - GCFPE binding and GCFPE sentences: 310, 312, 314, 345, 346, 386 and 444.
  - Stall prohibitions: 339.
  - `/model`: 348.
  - Composer checksum: 434.
  - Report row: 474.
  - Ledger checkpoints: 239, 280, 318, 386 and 459.
  - The profile's own name: 326, 328 and 330.
  - No hits for analyzer, strength, workload, appraisal, openai-docs, Ultra, Sol, GPT, Astra, rendered or page count.

**§8e, digests and profile pins:** all three digests were recomputed from the extracted bytes and match. The profile pins are covered under A3.

**§8f, the revision recount:**
- `"validator_revision": "3.3.2"` appears at exactly four sites: the validation profile, and three scripts (line 1908 of `validate_flowmaster.py`, line 1166 of `validate_gcfpe_20260914.py`, line 828 of `run_gcfpe_20260914_fixtures.py`).
- No "3.3.1" is left as a current validator revision. The 3.3.1 values that remain are `CHANGE_FLOW_SPECIALIZATION_REVISION`, which is change-flow's own revision and correctly unchanged.
- `FLOWMASTER_VALIDATE_REVISION` is 3.3.2. `TW_FLOWMASTER_SPECIALIZATION_REVISION` is 1.3.0.

**Extra checks, beyond the brief:**
- **"Install together" claim:** I tried both mixed installs. New validator with old tw-flowmaster: suite fails with 1 missing-contract error plus all 6 guards firing. Old validator with new tw-flowmaster: suite fails with 4 missing-contract errors. So the claim holds, and the new guard fires on the real 1.2.0 file.
- **Identities are unspent:** a diff of the advertised identities between installed and extracted shows every identity moved. No record on `main` or the branch, outside this Modification's own files, names 3.3.2 or 1.3.0.
- **freeze.py digests**, the install-verification recipe in `skill-identity-and-freeze.md`, recorded for the post-install check (L11):
  - `tw-flowmaster`: `2 0581205ba29f…722c`.
  - `flowmaster-validate`: `31 90c15e985a0c4b78d24298fe8187e8a50576689ddfc509d09fa11187ab97fcc2`. This differs from the skill-tree digest because `skill_tree_digest` strips the self-identity line.

## Gates I could not run
- No live TW Flowmaster run. None is possible from here.
- No post-install validation, because nothing is installed (that is X3).
- No prompt-body comparison (`D22`). "Matching the new prompts" was checked only against `edits.json`'s `new` texts and the record.

## Answers to §6
**A1. What governs a selected-catalog run now: no legacy fixed-model or page-count clause can govern any run.**
- The old fixed-model and page-count clauses were deleted outright: old lines 258, 266, 351, 352 and 353, line 393's Sol Max, and line 451's Sol Ultra and Max.
- The profile now applies when the selected drain and apply prompts "carry the exact no-redlines contract". It now supersedes only the repository-source and all-targets-must-apply clauses.
- Direct creation-to-application now governs a selected-catalog run, which matches the new prompts:
  - "As soon as one target's creation is terminal and validated successful…"
  - "READY creator output points to TW-APPLY-10."
  - The new prompt texts say the same: DRAIN-10.04 "For a complete READY package, Nathan invokes TW-APPLY-10", DRAIN-10.09 "the immediate next prompt is TW-APPLY-10", and APPLY-10.12.
- No text routes a non-GCFPE stage through an assessment:
  - "assess" appears only at lines 312 and 314 (the GCFPE binding) and 444 ("For a GCFPE application").
  - Neither the flow states nor the per-target states contain an assessment stage.
  - Neither bundled GCFPE contract contains a TW member (0 TW IDs), so the GCFPE clauses cannot reach a TW stage.
- Nothing found goes beyond K-1. One clarification of K-1: in that window, an old-release READY handoff names TW-ASSESS-10, while the new profile checks that READY points to TW-APPLY-10. So the pre-Apply half would probably fail creation validation loudly. The pre-creation assessment would still be skipped silently, as K-1 records.
- Outside this change, and the same in 1.2.0: the profile's first bullet resolves PF targets from `docs/pfcanon`, while lines 277, 404 and 430 say Drive.

**A2. The kept GCFPE clauses and the old line 339's rule: coherent, with one leftover sentence (LF-1).**
- Each edited sentence reads as a complete rule:
  - 334: "Record actual configuration only when directly verified."
  - 345 and 346, the two GCFPE configuration bullets. "above" resolves to lines 312 to 314.
  - 386, the target-identification configuration sentence.
  - 444, step 3 of redline application.
- Nothing kept imposes a fixed model or effort on a non-GCFPE stage:
  - `/model` is a preference for how to configure, not a model choice.
  - Line 339 contains only prohibitions.
  - Lines 434 and 474 record the observed configuration.
- **L8 is confirmed in part.** Line 386 now reads: "Configure the GCFPE target under the actual-work recommendation policy above, and only the capabilities required by the pinned identification prompt."
  - For selected-catalog TW runs, the consequence is refuted: the profile's second bullet restates "Require only capabilities needed by the pinned stage".
  - For legacy non-GCFPE runs outside the profile, it is confirmed: no sentence still limits that identification session to the capabilities its prompt requires. The core's capability-state rule governs how a capability is invoked, not which ones.
  - The consequence is low and not destructive, and no model is imposed. Listed as LF-2.

**A3. The fourth `validator_revision` site: no consumer pins the profile's bytes or hash, and every pin agrees.**
- The profile's sha256 moves from `1690c91d…bfb1` to `3f35e35c…ff3a`, and only line 45 changes.
- Within the root, only flowmaster-validate's own scripts name the file:
  - `load_profile` runs a field subset check (`PROFILE_IDENTITY`) that expects "3.3.2", which agrees.
  - `REQUIRED_SCRIPTS` checks that the file is present.
  - `SELF_FORBIDDEN` checks that a retired phrase is absent.
- change-flow names neither the file nor its hash. It reaches the check through `validate_gcfpe_current`, which is where P8's `PROFILE_IDENTITY` failure appeared.
- The file's bytes are covered by the recomputed `SKILL_TREE_SHA256`.
- In the repository, no file outside `docs/ephemeral` names the path or either hash. The hits inside `docs/ephemeral` are frozen historical captures from 2026-09-14/15 and 2026-09-23/24, not current consumers.
- GCFPE validation is otherwise unchanged:
  - The three script diffs change only the revision strings.
  - I ran the installed 3.3.1 validator on a baseline root (also FLOWMASTER_SUITE_PASS). Its contract coverage, fixtures, oracle and primary sections are identical to 3.3.2's on the new root, except for the revision label and the root path.

**A4. Leftover expectations of the old terms: none.**
- Across all 29 directories, and canva, the six removed identifiers and `ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN` appear only in the new forbidden list and in `SKILL.md` line 184's history clause.
- The "1.2.0" hits are other skills' own revisions: glow-merged-change-attribution-lock, and glow-hde-pr-development as named in the GCFPE contracts.
- The "3.3.1" hits are change-flow's own revision.
- No fixture names the TW contract.
- amthor-workspace-governance-audit mentions tw-flowmaster only in prose.

## Findings
**Required: none.**

**LF-1 (listed): a leftover sentence about non-GCFPE runs**
- **Where:** `tw-flowmaster/SKILL.md`, line 312, the last sentence: "Non-GCFPE runs retain their existing scoped defaults."
- **Defect:** the defaults it referred to have been removed. Those were the non-GCFPE model defaults on the old lines 351 to 353, and selected-catalog TW's two-checkpoint policy.
- **Evidence:** no non-GCFPE model or effort default remains anywhere in the file. The only other "defaults" are the filename-composition defaults on line 301.
- **Risk:** normal path, low likelihood. Nothing silent can happen, since there is no default left to apply.
- **Smallest correction:** replace it with "Non-GCFPE runs carry no model or effort recommendation", or delete it.
  - §A kept this paragraph under its candidate C4, but this sentence speaks only of non-GCFPE runs.

**LF-2 (listed): L8, confirmed in part**
- **Where:** `tw-flowmaster/SKILL.md`, line 386, the target-identification configuration sentence quoted under A2.
- **Defect:** the clause "and only the capabilities required by the pinned identification prompt" now attaches only to a GCFPE target. On a legacy non-GCFPE run, no sentence limits the identification session's capabilities.
- **Evidence:** the A2 reading above. The profile's second bullet restates the limit, so selected-catalog TW runs are covered.
- **Risk:** affects legacy runs only, low likelihood, not destructive.
- **Smallest correction:** "Configure the target with only the capabilities required by the pinned identification prompt and, for a GCFPE target, under the actual-work recommendation policy above."

**LF-3 (listed): the record's canon basis, not the package bytes**
- **Where:** §A's *Consult* and *Canon and rulings relied on*, and §P's canon list.
- **Defect:** they cite PF10 2.38 as making "no model or effort level a governance requirement… canon requires none". But 2.38's *Deferred obligations* keeps HDE Governance §9.1.3's requirement that every downstream-session prompt receive task-specific human advice on surface, model and reasoning level, and says whether it continues "is open for Product Owner determination".
- **Why it matters here:** TW Flowmaster sends prompts to downstream sessions, and TW-ASSESS-10 was where that advice came from.
- **Why it does not block the bytes:**
  - Nathan's direction of 2026-09-29 reads as that determination for TW: "no hard coded model recommendations or strength assessments at all", "In the tw prompts I mean", "Nathan chooses the model and effort for each session", and no addendum.
  - Under `AGENTS.md`, a formally approved, bounded Product Owner decision governs the exact decision it settles.
- **Smallest correction:** a dated successor note in §E that cites §9.1.3 and 2.38's deferred obligation, and names Nathan's direction as the determination for TW.

**Not a defect, a limit:** the six guards catch identifiers only. A reworded passage such as "Sol Max" or "pre-Apply assessment" would not fire. That is the set the plan fixed.

## Disclosures
- **One write outside my directory.** Before my directory existed, a shell redirect created `review-SFR-TW1-1-record.tmp` in the shared scratchpad root. It held the record's repository text, no prompt body. I deleted it in the next command. Nothing else was written outside `review-SFR-TW1-1/`.
- **No prompt body** was read or fetched (`D22`), and nothing in Notion was accessed.
- **The repository** was read only through `git show`, `git grep`, `ls-tree`, `rev-parse` and `status`. No fetch, checkout or write.

## Canon relied on
- **`AGENTS.md`:** the canon-first rule, PF canon is read-only, review scope, evidence attribution, and the truncation guardrail.
- **HDE Governance (PF04):** §9.1.3, the advice sentence and the local-eligibility paragraph; and §9.1.6, interacting skills, "An edited subgroup is not ready while an affected counterpart remains incompatible", and human model headers. Read on `main` at `f83c755`.
- **HDE Build Notes (PF10):** 2.31 PF10-HDR-001 and 2.38 PF10-AINEUTRAL-001, each read in full on `main` at `f83c755`.
- **In flight, at `80d226c`:** `MODIFICATION-20260930-gtwpe-tw-model-advice.md`, including:
  - its front matter;
  - §A: *Consult*, *Contradictions and risks*, Q1, *Revision of 2026-09-30* and *Canon*;
  - §P: directions, P-F1 and P-F2, *Values*, *Evidence files*, *Steps*, *The skill edits*, *The D24 brief*, K-1 to K-6, L1 to L21 and DL-1 to DL-9, and the successor of 2026-10-04;
  - §E: *Values*, and the X1.0 to X1.3 rows.
- **Also at `80d226c`:** `skill_edits.py`, `guard_proof.py`, `packages-tw1.json` and `edits.json`.
- **`docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D22, D24 and D26;
  - `reviewer-prompt-template.md` 1.2;
  - `skill-packaging-and-delivery.md` 1.1;
  - `skill-identity-and-freeze.md` 1.0, with `freeze.py`.
- **Background for the §9.1.3 reading:** `GTWPE-TARGET-ARCHITECTURE-20260929.md` on `main`, and the GTWPE design v1.2 row D7 and `P1-SOURCE-NOTES.md`.

IN FLIGHT. This record asks Nathan for nothing beyond the install the plan already names (PO-2). LF-1 to LF-3 are listed, not required. If Nathan opts in to repairing LF-1 or LF-2, the bytes change and this verdict is void for them. LF-3 touches only the record.
