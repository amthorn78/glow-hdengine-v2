---
artifact_type: GTWPE_DRY_RUN_RECORD
subject: design/GTWPE-DESIGN-v1.1.md at commit d087e4d, as authored
rule: D26-A rule 1 — "run every normal-path gate and readback on the text as it would land, read-only against the live pages, and check that every step's verification names a committed command"
mode: PLAN (plan v1.2 §16.1 gives P1r one dry run, then one fresh full review)
run_by: W1, 2026-09-28, 20:30Z to 20:45Z
status: RECORD. Merging preserves the record and approves nothing (D21-C)
---

# P1r dry run of design v1.1

**Result: 6 distinct required defects, all on the normal path (R1), and 3 listed.** Four of the six
are in the change prompt's own steps (§11). DRr-1 is proved mechanically: a pilot record written as
v1.1 says fails the real validator from `PLANNED` on, and passes at all four mode boundaries once it
carries the scope-freeze count. The repair is the commit after this record's own. The full review
then reads the repaired text.

## 1. What was run

All checks were read-only. Scratch files went only to the session scratchpad, and none holds a
prompt body.

| # | Check | Method | Result |
|---|---|---|---|
| 1 | A pilot record in v1.1's shape passes `modification_validate.py` at each mode boundary | Four synthetic records, `ANALYZED`, `PLANNED`, `EXECUTING` and `COMPLETE`, written exactly as §11.3 and §11.4 say (`artifact_type: GCFPE_MODIFICATION_RECORD`, `ecosystem: GTWPE`, `targets: [tool]`, `gate_tier: 1`, closure from §6). Run against a scratch copy of the real validator, and against a scratch copy with `tool` added to `TARGETS`, as P2(a) will | Real validator: 0 of 4 pass, exit 1, on `tool` (expected until P2(a)) and on `SCOPE FREEZE: status PLANNED requires item_count_at_approval` at `PLANNED`, `EXECUTING` and `COMPLETE` (**DRr-1**). With `tool` added: 1 of 4, the same scope-freeze failures. With `tool` added and `item_count_at_approval` set: **4 of 4, exit 0**. The copy with `tool` added still passes its own selftest, 64 of 64. The extra `ecosystem` key and the GCFPE type are accepted, and `closure` is never read |
| 2 | Each quotation v1.1 adds matches its source | Exact search, whitespace-normalized for wrapped lines | All hold: Nathan's G0 words (plan v1.2 §16.4; `CHECKPOINT.md` §8); "PF27 and PF30 are updated only when a specification exists" (plan §1); three HDE Governance §9.1.6 phrases, on `main`; v1.0's D-10 wording; the PE rule carried from v1.0 |
| 3 | Each repository path v1.1 adds exists | `git cat-file -e` on `origin/main` | All eight present |
| 4 | Live: the source pin still holds | A Notion search with highlights off, so no body was fetched | The proposed body is still "PROPOSED BODY (D20 redesign)", last edited 2026-09-24T11:00; no later versioned GCFPE-MGMT-10 page. The live `091426.1` page was last edited 2026-09-24T15:38 |
| 5 | Live: the PE Metaprompt pin | The same | "PE Metaprompt 091426.1", last edited 2026-09-23T17:17, as at P0 |
| 6 | Live: P2(b)'s target area | `notion-fetch` of HDE TW `3c74590a05eb8176baf8cb59f1631f3c`, a navigation page, not a prompt body | `page_last_edited_at` 2026-09-23T17:44:08.540Z, as at P0; 20 child pages; no GTWPE page. A search for "GTWPE" finds none either |
| 7 | Can S1 classify a Notion page from its ID without fetching it? | A Notion search whose query is a page ID (HDE TW's) | **No.** The page itself is not among the results: they are three other pages that mention it (**DRr-5**) |
| 8 | A0's drift check runs as written | `git log 8eb4ce0..origin/main` over §11.7's watched paths, with the glob pathspecs quoted | Exit 0, no commits: nothing watched changed since P1's base. The globs match: `docs/pfcanon/PF10-*` finds the three 2026-09-27 PF10 commits |
| 9 | Walkthrough: P2(b) | The text, write by write | DRr-2 |
| 10 | Walkthrough: P3, the pilot, mode by mode | The text, against the validator and the second review template | DRr-1, DRr-2, DRr-3, DRr-4; and the branch question in §5 |
| 11 | Walkthrough: a later prompt change through GTWPE-MGMT-10 | §11.5 against HDE Governance §9.1.6 | DRr-6 |
| 12 | Coverage of plan v1.2 §16.1 and §16.2 | A trace, §3 below | Every item has a home |

## 2. The check behind each change-prompt step

| Step | Check in v1.1 | Command | Gap |
|---|---|---|---|
| P2(b) writes | "each read back completely before the next" | none named | **DRr-2** |
| A0 | trigger findings recorded | Notion search; `git log` over §11.7 | — |
| A1 | "The record exists on its branch" | none named | **DRr-2** |
| A2, A4 | "—" | none; the validator at A7 would check what they write | **DRr-2** |
| A3 | the search and its count in §A | the search itself | — |
| A5, A7 | `modification_validate.py` | yes | — |
| A6, PL3 | the validator's cap and dry-run checks | yes; the reviewers' records need capture, and P3 has no capture command (**DRr-3**) | DRr-3 |
| On `ANALYZE` approval | none | — | **DRr-1**: `item_count_at_approval` is never set |
| PL1, PL2 | "—" | none; the validator at PL4 would check them | **DRr-2** |
| PL4, X2 | `modification_validate.py` | yes | — |
| X1 | each step's own verification | from §P | — |
| X3 | `git rev-parse origin/main:<path>` equals the branch's blob | yes | — |
| X4 | the catalog block, read back | for prompt pages; §11.7's rows assume every member has a page ID | **DRr-4** |
| X5 | validator; the catalog pin "once the record has merged" | no step returns for, or resumes after, that second merge | **DRr-4** |
| §11.5, a prompt page | edit by edit | named, but short of HDE Governance §9.1.6 | **DRr-6** |

## 3. Coverage of plan v1.2 §16

| Item | Home in v1.1 |
|---|---|
| §16.1 phase order P1r to P6, with gates and checks | §12.1; §3's third diagram |
| §16.1 "From P3 on, every repair runs through GTWPE-MGMT-10" | §2.2; §12.1; §12.4 |
| §16.2 the validator's `tool` class (E-017) | §11.3; §12.1 P2(a); §14 D-8 |
| §16.2 the `closure` risk removed (E-018) | §16; §11.3 |
| §16.2 *Writes* against *Boundaries* (listed #10) | §4; §4.4 |
| §16.2 the source pinned, and added to the triggers (E-019) | §11.1; §11.4 A0; §11.7; §11.9 |
| §16.2 RQ-1 to RQ-3 carried into P3 and P4 (E-020 to E-022) | §0.1; §4.1; §4.1.1; §5.1; §6 H2; §9.2; §13.2; §13.3; §16 |
| §16.2 the post-check's two directories (E-016) | §7.5; §13.3 |
| §16.3 estimates and the measure | §7.6; §12.5; §14 D-11 |

## 4. Required defects

| ID | Class | Finding | Where | Smallest correction |
|---|---|---|---|---|
| DRr-1 | R1 | No step sets `item_count_at_approval`, which the validator requires from `PLANNING` on (its scope-freeze check). Every pilot record past `ANALYZED` fails, as check 1 shows | §11.4, "On Nathan's approval" after A7 | On `ANALYZE` approval, also set `item_count_at_approval` to the number of items (template rule 3) |
| DRr-2 | R1 | Six checks name no command or criteria: P2(b)'s readback ("read back completely"), A1, A2, A4, PL1 and PL2 | §11.4; §12.1 P2; §12.2 | Name each. P2(b): in context, title, parent, identity lines, every approved section heading in order, and the catalog rows. A1: `git cat-file -e <branch>:<record>`. A2, A4, PL1, PL2: checked by the validator at A7 or PL4 |
| DRr-3 | R1 | The pilot's `PLAN` review captures its reviewers' records "by script", but `gtwpe_redline.py capture` is built only in P4. The cold run's brief is also unstated | §11.4 A6; §13.2 | Until P4, capture as P1 did: a JSON parse of the reviewer's own transcript for its final handback message, written unedited, with its byte count and sha256 recorded. Brief the cold run with §7.2's write-nothing clause |
| DRr-4 | R1 | X5 sets the catalog's last-close commit "once the record has merged", but no step returns for or resumes after that second merge, and a squash-merged branch cannot simply take the `COMPLETE` record. §11.7 also gives every member a page ID, which a tool does not have | §11.4 X4, X5; §11.7 | The last-close commit is X3's merge commit. X5 restarts the branch from `origin/main`, commits the `COMPLETE` record and pushes it; Nathan merges it when he chooses, and nothing waits on it. The catalog has a row per prompt; the tools and the procedure are identified by their paths on `main` |
| DRr-5 | R1 | S1 refuses a prompt-body page "before it is fetched", from a search result. A search by page ID does not return that page (check 7), so a page given by ID cannot be classified without fetching it | §5.1 S1 | Nathan names a Notion page input by title and page ID. S1 searches the title, takes the result whose ID matches, and applies the rule to its title and path. No match is `UNSUPPORTED_INPUT notion-page-unidentified` |
| DRr-6 | R1 | A prompt change's readback checks each edit, while HDE Governance §9.1.6 asks to "read back complete changed published bodies and required links" and to "Record actual author, checker and acceptor". v1.1 also lists the edit-by-edit check as an accepted risk | §11.5; §11.4 X5; §16 | Read the new page back whole, in context: identity lines, each approved edit present, section headings as planned, and the catalog's link to it. Record author, checker and acceptor in §E. Drop the listed risk |

## 5. Listed, not repaired (`D26-A` rule 4), and one decision

| ID | Finding | Path | Likelihood | Consequence | Why listed |
|---|---|---|---|---|---|
| DLr-1 | The pilot record cannot validate before P2(a) adds `tool` | normal | certain before P2(a) | A loud validator failure | Plan v1.2 orders P2 before P3 |
| DLr-2 | S1's rule refuses every page under `AI Prompts`, including navigation pages that are not prompt bodies | normal, Path A | low | A loud `UNSUPPORTED_INPUT`; Nathan can supply the page as an upload | Loud, and conservative by design |
| DLr-3 | The cold run's capture reads a transcript that holds the change prompt's body | normal, P3 | certain for the cold run | A second read under `D22`, disclosed | Already listed in §16 |

**A decision the walkthrough exposed, for §14.** GTWPE-MGMT-10 opens its own branch for each
Modification (§11.3). The kickoff tells W1 to "Work on one branch, docs/20260925-gtwpe-w1". When W1
runs the pilot, the two conflict. The repair adds it as D-14, with the default that the pilot uses
its own branch, as the prompt specifies, and W1's records stay on `docs/20260925-gtwpe-w1`.

**A second decision, where canon is silent.** HDE Governance §9.1.6 introduces the *Glow HDE Living
Prompt Flow Map* within its GCFPE governance text. It says the map is updated "when a prompt is
proposed, contracted, authored, independently reviewed, repaired, published", and so on, but not
whether a non-GCFPE ecosystem's prompts belong on it. No procedure document names the map. The
repair adds it as D-15, with the default that GTWPE-MGMT-10 does not write the map: the GTWPE's
catalog is its navigation, and D-10's destination rule does not reach the map.

§17 of the design receives this round's ledger row with the repair.

## Canon relied on

PF04 — HDE Governance §9.1.6, read in full on `main` at `0db3f0e`. `AGENTS.md`, the canon-first
rule. In-flight and governing documents: plan v1.2 §16; `modification-template.md` rule 3;
`modification_validate.py`, the checks at lines 330 to 420 and 466 to 484; `reviewer-prompt-template.md`,
the second template; `gcfpe.decision-record.md` D22 and D26.
