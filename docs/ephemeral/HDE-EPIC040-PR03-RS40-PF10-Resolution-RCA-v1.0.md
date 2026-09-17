# RCA: Incorrect `MANUAL_DRAIN_REQUIRED` Decision

## Conclusion

The approved §2.12 addendum is present in the current controlled PF10: [PF10-HDE-Build-Notes-v13.2.5.md](https://drive.google.com/file/d/1evxWB8tdxeFstNtMzT-MD0kjuRGtaILq/view?usp=drivesdk).

It appears as:

> `## 2.12 HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release`

The section is substantively equal to `HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md`. The differences are formatting-only, including bolded headings, bullet characters, Markdown escaping, and PF10’s final `<eof>` marker.

The `MANUAL_DRAIN_REQUIRED` response was incorrect.

## Primary root cause

The session failed to resolve the current PF10 independently.

The handoff identified:

> `Current controlled PF10 before this drain: PF10-HDE-Build-Notes-v13.2.4.md`

The phrase **“before this drain”** explicitly classified v13.2.4 as the pre-drain source. Nevertheless, the session opened and relied on that file. Because v13.2.4 ends at §2.11, it treated the lack of §2.12 there as unresolved drainage.

It should instead have searched the authoritative `Glow / Core Docs / PFCanon` location for the successor controlled Markdown. That search finds v13.2.5, which contains §2.12.

This was a stale-source selection error.

## Failure sequence

1. The handoff supplied the pre-drain PF10 v13.2.4 as historical context.
2. It supplied the approved standalone §2.12 addendum.
3. It instructed the session to run RS-40 after Nathan had manually drained and verified that addendum.
4. RS-40 itself required independent resolution of the current PF10 Markdown.
5. The session retrieved v13.2.4 but did not perform the required current-file search.
6. It saw that v13.2.4 lacked §2.12.
7. It converted that incomplete observation into `MANUAL_DRAIN_REQUIRED`.
8. It then asked Nathan to confirm work that the current PF10 already demonstrated had occurred.

The mistake occurred between steps 5 and 7: an explicitly pre-drain file was substituted for the current authority.

## Contributing errors

### 1. A decisive qualifier was ignored

“Before this drain” was not incidental wording. It meant v13.2.4 could not establish the post-drain state. The filename was preserved but its stated role was not.

### 2. RS-40’s source-resolution requirement was not completed

RS-40 says to:

> “Resolve the current PF10 Markdown independently.”

The session did not complete that instruction. It inspected a supplied predecessor instead.

### 3. Three different questions were conflated

The following should have remained separate:

- Is §2.12 present in the standalone approved addendum?
- Is §2.12 present in the current controlled PF10?
- Has Nathan asserted that manual drainage and verification are complete?

The first was already established. A proper current-source lookup established the second. The invocation, combined with the matching post-drain PF10, supplied the operational basis for the third. The session instead treated all three as unresolved because the old PF10 lacked the section.

### 4. Read-only verification stopped too early

No write or implementation action was necessary to resolve the question. Drive search and file inspection were available. The session stopped at the first apparent blocker rather than finishing the mandatory verification.

### 5. The terminal state contradicted the stated uncertainty

The session wrote:

> “I have not determined whether §2.12 is present in PF10.”

But it returned:

> `MANUAL_DRAIN_REQUIRED`

Those statements do not support each other. If presence had genuinely remained undetermined, the defensible conclusion would have been a source-resolution problem, not a factual determination that drainage was still required.

### 6. The attachment-routing statement was not a valid basis for stopping

The session also said that the sources could not be safely routed. That statement cannot be substantiated from the available evidence. More importantly, any attachment-routing issue would not have prevented an independent search of the authoritative PFCanon directory. It was therefore irrelevant to determining the current PF10 state.

## Verified evidence

| Evidence | Finding |
| --- | --- |
| PF10 v13.2.4 | Ends at §2.11 and is explicitly identified in the handoff as the PF10 **before** this drain. |
| Current PFCanon Markdown | PF10 v13.2.5 exists in the authoritative PFCanon parent. |
| PF10 v13.2.5 table of contents | Lists §2.12 for `HDE-EPIC040-PR03-R02`. |
| PF10 v13.2.5 body | Contains the complete §2.12 section. |
| Standalone addendum comparison | The §2.12 wording is substantively equal; observed differences are Markdown presentation and the PF10 EOF marker. |
| RS-40 invocation | States that RS-40 is being run only after Nathan manually drained and verified the approved addendum. |

Drive reports v13.2.5 with a modification timestamp of `2026-09-14T10:47:58Z` and a Drive creation timestamp of `2026-09-14T11:00:45.842Z`. A reliable timestamp for the previous final response is not available, so the exact availability of v13.2.5 at that instant cannot be reconstructed. That uncertainty does not excuse the error: the session did not perform a fresh current-PF10 resolution before issuing the terminal decision.

## Classification

This was primarily an **incorrect authority-resolution and source-selection decision**.

The session did not invent supposed text from PF10, because it explicitly admitted that it had not determined whether §2.12 was present. However, it issued an unsupported blocker from that incomplete determination. Functionally, the result was incorrect and presented an unresolved lookup as though it proved missing Product Owner action.

## Impact

- RS-40 was stopped incorrectly.
- Approved PR03 correction work was delayed.
- Nathan was asked to repeat or confirm an already completed prerequisite.
- The response created the false impression that the authoritative material was unavailable.
- It wasted time and reduced confidence in the session’s ability to resolve current authority.

No repository mutation, PF10 edit, implementation work, merge, or other external change was performed during the incorrect stop.

## Required prevention

1. Treat any file described as “before this drain” as historical evidence only.
2. Independently search the authoritative PFCanon directory for the current Markdown.
3. Reject Google Doc, DOC, and DOCX counterparts as authority.
4. Confirm the current file’s title, MIME type, parent, and version.
5. Locate the exact expected section heading.
6. Compare its substance with the approved standalone addendum.
7. Keep source presence, substantive equality, and Product Owner assertion as separate recorded checks.
8. Return `MANUAL_DRAIN_REQUIRED` only after the current authoritative PF10 has been resolved and shown not to contain the required drained material.
9. Never issue a definitive missing-drain state while simultaneously stating that presence was not determined.
10. Perform one final source-freshness check immediately before returning a terminal blocker.
