---
artifact_type: SKILL_PACKAGE_CHANGE_NOTE
modification: MODIFICATION-20260930-gtwpe-tw-model-advice
round: tw1
part: PART-02
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# Change note, round tw1: tw-flowmaster 1.3.0 and flowmaster-validate 3.3.2

**Install both archives together, in one install.** Neither works alone: the new validator requires
`tw-flowmaster` 1.3.0, and the installed validator 3.3.1 requires 1.2.0.

## The two archives

| Archive | sha256 | Bytes | Replaces | Revision after install |
|---|---|---|---|---|
| `tw-flowmaster.skill` | `88166c3d48fee16900e125f1cf2fe15cf2b46a2e0a6ac05ea0fdd5ef3c1a4b89` | 19,193 | installed `tw-flowmaster` 1.2.0 | `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.3.0` |
| `flowmaster-validate.skill` | `e1f495b3f40f9a75c713433236391763505cb3895364076f71eb771a72710f3f` | 322,860 | installed `flowmaster-validate` 3.3.1 | `FLOWMASTER_VALIDATE_REVISION: 3.3.2` |

Both update the installed skills in place: the directory names and `name:` fields are unchanged.
`packages-tw1.json` holds the same values and each tree's digest.

## What changed

**`tw-flowmaster`**, 21 edits in `SKILL.md`, and nothing in the embedded Primary core, which stays
byte-identical to `flowmaster-primary`'s. TW-ASSESS-10's two assessment stages
(`PRE_CREATION_ASSESSMENT`, `PRE_APPLY_ASSESSMENT`), its inputs (`STRENGTH_ANALYZER_PROMPT_ID`) and its
research rules are removed, and so is every fixed model or effort policy (the Ultra/Max page-count
rule, `PF_RENDERED_PAGE_COUNTS`, the fixed Sol models for non-GCFPE stages). The selected-catalog TW
profile now applies when the selected prompts "carry the exact no-redlines contract", and READY
creator output points straight to TW-APPLY-10, as the new prompts say. The GCFPE's own clauses, the
stall prohibitions and the rule to record actual configuration only when directly verified are kept.

**`flowmaster-validate`**, 11 edits: it requires the TW revision 1.3.0, no longer requires the three
removed TW terms, and forbids six identifiers (`TW-ASSESS-10`, `PRE_CREATION_ASSESSMENT`,
`PRE_APPLY_ASSESSMENT`, `STRENGTH_ANALYZER_PROMPT_ID`, `APPLICATION_REASONING_POLICY`,
`PF_RENDERED_PAGE_COUNTS`) from coming back. Its revision moves from 3.3.1 to 3.3.2 at all four
`validator_revision` sites, including the GCFPE validation profile, and its self-digest
`SKILL_TREE_SHA256` is recomputed. The GCFPE's checks are otherwise unchanged.

## Review

Both reviewers returned **`SKILL_FIT_CONFIRMED`**, bound to the digests above, under the brief
`D24-BRIEF-tw1.md`:

- `SECTION-10-REVIEW-tw1-1.md` (SFR-TW1-1)
- `SECTION-10-REVIEW-tw1-2.md` (SFR-TW1-2)

They listed five non-blocking findings, which are not repaired, since any byte change would void both
verdicts. Three concern these bytes: a leftover sentence, "Non-GCFPE runs retain their existing
scoped defaults." (SFR-TW1-1 LF-1); a capability limit that now reads as GCFPE-only on legacy runs
(LF-2); and the guard catching only identifiers, not reworded text such as "Sol Max" (SFR-TW1-2 L1).
The other two are the record's HDE Governance §9.1.3 point (§E's E-F2).

## After installing

- The installed `tw-flowmaster/SKILL.md` shows `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.3.0`, and
  `flowmaster-validate/SKILL.md` shows `FLOWMASTER_VALIDATE_REVISION: 3.3.2`.
- X3 then compares the installed tree digests with these and runs the validator on an isolated root:
  `tw-flowmaster` `0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c` (2 files) and
  `flowmaster-validate` `284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733` (31 files).
- **The selection waits for this install.** The seven new TW prompt pages exist but are unselected;
  X4 selects the new release only after X3 passes. Between the install and X4, the installed profile
  also matches the old release (the accepted risk K-1), so start no TW Flowmaster run in that window.
- Do not install while a skill review is running (`D24`'s freeze). No review is running now.

## Rollback

Reinstall the prior versions, whose tree digests are `fd6c344befd9ce9e89648e6e404dd39f02e50bfaef2ca13d4e56ab84f5576617`
(`tw-flowmaster` 1.2.0) and `ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af`
(`flowmaster-validate` 3.3.1). This run did not build archives of them (the accepted risk L10).
