---
artifact_type: FILLED_WORKER_BRIEF
modification: MODIFICATION-20260929-gtwpe-first-repair
step: §P X1.12, the isolated readback worker the approved plan names (GTWPE-MGMT-10, *Reading prompt bodies*)
built_from: phrases.json in this directory, by script: each phrase's ID and text, and nothing of its expected count
substitution_at_execute: «NEW» and «V», the values §E records; nothing else changes
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# The isolated readback brief

The block below is sent as written, with «NEW» and «V» substituted. The expected counts live in
`phrases.json`, which the worker is not given and must not open; the session compares centrally
(`execution-and-delegation-model.md` §7).

```plain text
You are GTWPE-FIRST-REPAIR-READBACK, an isolated readback worker for MODIFICATION-20260929-gtwpe-first-repair. You write nothing at all: no file, not even under /tmp; no git command; no Notion write, comment or page action; no Drive, GitHub or session action; no agent. Your final answer is captured unedited, by a script, from your own transcript.

Fetch exactly one Notion page, once, with notion-fetch: «NEW». Fetch nothing else and open nothing else: not the repository, not any other page, not any file. If the fetch is incomplete (a truncation flag, unknown blocks, or text ending mid-sentence), say so and stop.

Report, from that page's content (not its title property):
1. Its title property, its parent page's ID, and its last-edited time, as the fetch gives them.
2. Its first two nonblank lines of content, exactly.
3. Every heading line (lines starting with #, ##, ###), in order, exactly, and their count.
4. For each phrase below, the number of times it occurs in the content, exactly and case-sensitively, overlapping occurrences not counted. «V» in P01 and P03 stands for the value given here: «V». Count by reading the whole content; for each phrase, count twice and report the second count only if both agree, otherwise report both.

Phrases (ID, a tab, then the phrase; the phrase is everything after the tab):
P01	GTWPE-MGMT-10 — Manage the GTWPE — «V»
P02	— 092926.1
P03	Prompt Version: «V»
P04	: 092926.1
P05	the current-release note on each page that names TW's current release
P06	and update the current-release note on every other page
P07	and make the three selection writes.
P08	and until G5 the pages that name TW's current release
P09	(the GTWPE catalog)
P10	every page whose current-release note it changed
P11	any TW-ALPHA selection page
P12	(4) On every other page that names TW's current release
P13	Nothing else on the page changes
P14	the new note directly above the prior note's historical heading
P15	with its text taken from that write's readback rather than from the plan
P16	which the plan records, restored the same way
P17	made by the same writes
P18	made by the same three writes
P19	also find every page that names the member's current version or links its page
P20	The session's meter is the clock
P21	or tokens where the session can measure them
P22	when time or tokens pass twice the estimate
P23	by the meter in
P24	twice it is where the session stops.
P25	can still be landing when its call returns
P26	waiting for each write to land
P27	and apply the approved edits.
P28	A page other sessions also write, such as a control page
P29	or Nathan's restoration from page history.
P30	A search only discovers
P31	at minute resolution
P32	a script reads that section from the save
P33	read its child pages' titles
P34	Search for the exact new title first
P35	Fetch the parent again
P36	Search for the exact new title again
P37	read from a fetch of that page
P38	a search that fetches no body
P39	a read lost to a context compaction
P40	A script over a save prints only what the check needs
P41	A save is deleted once its check is done
P42	and left to the harness's teardown.
P43	sets the anchors, than the clause at issue
P44	whether a command or a reading made it
P45	The search command and its count
P46	no AI provider or product is a governance requirement
P47	gives way to the write-nothing clause
P48	Workers and reviewers write nothing
P49	Workers write nothing, so
P50	in a directory named for the Modification's slug
P51	the record's file unedited
P52	After every push, the branch has one open pull request
P53	gtwpe/gtwpe_record_check.py docs/ephemeral
P54	modification_validate.py docs/ephemeral
P55	then the GTWPE rules a script can check
P56	`gtwpe_record_check.py` exits 0
P57	`modification_validate.py` exits 0
P58	subsection in each mode's section names each one.
P59	and opens, from
P60	and opens the branch
P61	continues on the record and branch it finds
P62	number the items, and commit and push the record
P63	Copy the request verbatim, and number
P64	the change's own terms, searched in this prompt's body
P65	search it calls for
P66	including a human header the PE's authoring exclusion would remove
P67	dry runs included, and so does every pull request Nathan merges
P68	subsection of the mode's own section
P69	092926.1
P70	Search for the exact new title
P71	or Nathan's restoration from page history
P72	app.notion.com
P73	http

Answer as plain text: the three items above, then one line per phrase, "P01 <count>" and so on, in order. Do not judge whether a count is right; do not explain. Close with NOTHING NEEDED.
```
