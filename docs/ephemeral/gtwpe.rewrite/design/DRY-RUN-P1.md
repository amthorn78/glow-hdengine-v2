---
artifact_type: GTWPE_DRY_RUN_RECORD
subject: design/GTWPE-DESIGN-v1.0.md at commit 9548251, as authored
rule: D26-A rule 1 — "run every normal-path gate and readback on the text as it would land, read-only against the live pages, and check that every step's verification names a committed command"
mode: PLAN (P1's design package; plan §5 fixes one dry run, then at most one diff check)
run_by: W1, 2026-09-28
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# P1 dry run of the GTWPE design package

**Result: 8 distinct required defects, 4 listed.** Every required defect is on the normal path
(R1), except DR-4, which is a silent breach of a Product Owner ruling (R3). The repair is the
commit after this record's own. The one diff check reviews that repair.

## 1. What was run

All checks were read-only. The design lands as a repository record only: no page, tool, prompt or
canon file.

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Every PF section the design cites exists on `main` | A Python heading scan over the cited PF files | 62 of 64 matched directly. PF04 §9.3.1 and §9.4 sit on blockquote lines (`> ###`, `> ##`, lines 2558 and 2577) and exist. **"PF27 §1" is wrong**: PF27 §1 is *Live QA Plan*; the rules cited sit under the H2 *Review guardrails* (line 988): *Hard blockers for plan approval/execution*, *Materiality-based blocker discipline…*, and *QA planning QoS guardrails…* with *Redline bundle construction discipline* and *Review stability and no-moving-target discipline* (DR-6) |
| 2 | Each cited PF06 passage sits in its cited section | `grep -n -F` of the quoted words, mapped to the enclosing heading | All hold: *Post-QA documentation drainage ordering* is inside §3.5.2.8 (line 3209); `ASK OK?` in §1.1.11 (2346); "The final historical record is archived in PF20 only at epic close" in §1.1.2; "once, at epic close" in §3.5.1 (2913); §6.3 (4158); §1.0.3 (1447); §1.0.6 (1465) |
| 3 | Each repository path the design names exists, or is a later deliverable | A regex over backticked paths; `os.path.exists` | Present: the ten procedure files, `modification_validate.py`, `closure.py`, `docs/ephemeral/modifications/`, the subagent transcript directory. Absent as expected: `docs/prompt_ecosystem_management/gtwpe/` and `readers.lock` (P2), `.claude/agents/` (§14 D-6). A branch name and two glob patterns matched the regex and are not paths |
| 4 | Live: the P3 target area | `notion-fetch` of HDE TW `3c74590a05eb8176baf8cb59f1631f3c` | `page_last_edited_at` 2026-09-23T17:44:08.540Z, equal to P0's probe; 20 child pages, matching `CHECKPOINT.md` §4.6; no GTWPE page; the page says Glow Technical Writing Ecosystem selects TW-ALPHA-20260908.1 |
| 5 | Live: the PE Metaprompt is unchanged since P0 | `notion-search` (no body fetched, so no `D22` transient) | `timestamp` 2026-09-23T17:17:00.000Z, consistent at minute resolution with P0's 2026-09-23T17:17:22.217Z |
| 6 | Filename and in-document title agree for every file in `docs/pfcanon/` | `grep` of each `Title`, `Name` or first H1 line | All 34 agree on "canon"; PF16's title is its H1 |
| 7 | Capture is feasible | A JSON parse of the P0 probe's transcript, `…/subagents/agent-acdc66a7d5db676cf.jsonl` | Its final 1,111-character answer extracted |
| 8 | Normal-path walkthrough: Path A on one small target | The design's text, stage by stage | DR-1, DR-2, DR-3, DR-5 |
| 9 | Normal-path walkthrough: Path B with PF10 | The same | DR-1, DR-2, DR-3 |
| 10 | Normal-path walkthrough: GTWPE-RECORD-20 and GTWPE-RECORD-10 | The same | DR-2, DR-7 |
| 11 | Coverage: plan §2, plan §8's failure rows, the relay's items, and the PE design-package contents each have a home | A trace table, §3 below | DR-1, DR-7, DR-8 |
| 12 | Every stage's verification names a command | §2 below | DR-2 |

## 2. Commands behind each stage's check

A check "names a committed command" when its command is in the repository. At P1 none of the GTWPE
tools exists yet: they are P2's deliverables. This check therefore asks whether each stage's check
names a command, and whether P2's list builds it.

| Stage | Check | Command | In P2's list |
|---|---|---|---|
| S0 | inputs resolve | `git cat-file -e origin/main:<path>`; the Notion or Drive read | git: yes |
| S1 | record complete | `gtwpe_read.py` | yes |
| S2 | each target cites a source unit and passes eligibility | none named | **no (DR-2)** |
| S3 | the return is captured and parses | `gtwpe_redline.py capture` | yes |
| S4 | exit 0 | `gtwpe_redline.py validate` | yes |
| S5 | the reply names the run and each file | none named | **no (DR-2)** |
| S6 | the diff check | `gtwpe_redline.py apply` | yes |
| S7 | zero differences, compared centrally | none named | **no (DR-2)** |
| S8 | the PR's paths and diff equal the approval | none named | **no (DR-2)** |
| S9 | files on `main` equal S6's output | `gtwpe_redline.py detect-merge` | yes |
| post-check | nothing written | `gtwpe_redline.py postcheck` | yes |

## 3. Coverage trace

| Requirement | Home in the design | Gap |
|---|---|---|
| Plan §2.1, the two paths | §4.1 inputs | — |
| Plan §2.2, row "A document only" | §4.1 (a); §5.1 S2 | — |
| Row "A specification and PF10" | §4.1 (b) | the invocation cannot say whether PF10 is included (DR-1) |
| Row "A specification, a document, and PF10" | §4.1 "and/or" | as above |
| Row "A specification without PF10" | none | **DR-1** |
| Row "PF10 only" | none | **DR-1** |
| Row "Nothing usable" | §5.1 S0 | — |
| Plan §2.2, an unsure target goes to G3 | §5.1 S2 | — |
| Plan §2.3, the types and readers | §9.2 | "A prompt body stays out of the record (`D22`)" is not stated for a Notion input (**DR-4**) |
| Plan §2.4, S0 to S9 and their checks | §5.1 | four checks without a command (DR-2) |
| Plan §2.5, membership | §2, with the three rulings | — |
| Plan §3, §4, §8, §11, §12 | §7.2, §5.2, §5.1 and §9.1, §13, §12.5 | — |
| Relay: E-003, E-004, E-006, E-007, Q1 to Q3, S2 and S3 prices | §9.1 to §9.5, §7.6 | — |
| PE package: per-prompt purpose, owner, inputs, outputs, writes, approval effects, dependencies, exclusions, completion | §4.1 complete | §4.2 and §4.3 lack dependencies, exclusions and completion; §4.4 has no contract table (**DR-7**) |
| PE package: "New Glow prompts need a complete PF03, PF06 and PF10 check" | cited throughout | no stated check result (**DR-8**) |
| PE package: Mermaid, producer-consumer contracts, maintenance scope, change plan, decisions, `AWAITING_APPROVAL`, identity lines, lineage, no effort fields | §3, §6, §11, §12, §14, front matter, §4, §11, §7.6 | — |

## 4. Required defects

| ID | Class | Finding | Where | Smallest correction |
|---|---|---|---|---|
| DR-1 | R1 | The invocation forms cannot express two of plan §2.2's rows, "A specification without PF10" and "PF10 only", and never say whether PF10 is included | §4.1 Inputs | Make PF10 an explicit input, `PF10` optionally narrowed to named addenda, and map the six rows to invocations |
| DR-2 | R1 | S2, S5, S7 and S8 name no command for their checks (`D26-A` rule 1) | §5.1; §12.1 P2 | Name `targets-check`, `approval-check`, `verify-check` and `pr-check`, and add them to P2's list |
| DR-3 | R1 | S1 writes every input into a record, so a Path B run copies PF10 (316 KB) and the specification into the run directory: a committed copy of source material (`STALE-001`) | §5.1 S1; §6 H2 | Record a repository input by path, blob SHA and unit index; copy only inputs from outside the repository |
| DR-4 | R3 | A Notion prompt body used as a Path A input is not kept out of the record: the design only exempts it from hashing. Plan §2.3 and `D22` keep it out | §5.1 S1 | Record a prompt-body page by identity only; its drafter reads it live; with §14 D-6's reader agents it is `UNSUPPORTED_INPUT notion-prompt-body` |
| DR-5 | R1 | S2 says candidates are "precomputed mechanically" but gives no method for Path A | §5.1 S2 | Candidates are the eligible PFs the source names by number or title, plus those whose purpose-and-scope sections the manager finds the source bears on, each with its reason |
| DR-6 | R1 | "PF27 §1" is cited six times for the review rules; §1 is *Live QA Plan*. A brief citing it would send a drafter to the wrong section | §1, §7.2, §8.1, §8.6 (twice), §11 | Cite PF27 *Review guardrails* and the named sub-headings |
| DR-7 | R1 | The PE's contract fields are incomplete for GTWPE-RECORD-10, GTWPE-RECORD-20 and GTWPE-MGMT-10 | §4.2, §4.3, §4.4 | Add dependencies, exclusions and completion to §4.2 and §4.3; give §4.4 a contract table |
| DR-8 | R1 | The PE's "complete PF03, PF06 and PF10 check" for new prompts has no stated result | none | Add the check: each rule the four prompts must meet, and where the design meets it |

## 5. Listed, not repaired (`D26-A` rule 4)

| ID | Finding | Path | Likelihood | Consequence | Why listed |
|---|---|---|---|---|---|
| DL-1 | §9.1 says merges are never detected "by commit subjects or PR state", then reads the PR's state to tell "still open" from "closed unmerged" when the files are absent | normal | certain | none: detection itself is by files; the wording overstates | wording only |
| DL-2 | §7.4's capture is proved on a background subagent's transcript; a foreground call's layout is unverified | normal | low | `CAPTURE_UNAVAILABLE`, a loud stop | P2 tests both |
| DL-3 | S2's classifier for PF27 is not named; B-CLASSIFY covers it by its general contract | normal | low | none | covered |
| DL-4 | A post-check watch on HDE TW's `page_last_edited_at` would also move with any unrelated edit to HDE TW | failure | low | a false stop, loud | loud |

§17 of the design receives each round's ledger row after the round, as a Modification record's
`reviews` ledger does (`modification-template.md` rule 8). That is record-keeping, not a change to
the reviewed design.
