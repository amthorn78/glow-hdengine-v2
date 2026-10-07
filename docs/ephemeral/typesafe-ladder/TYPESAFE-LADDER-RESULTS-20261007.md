---
artifact_type: SCORER_ACCEPTANCE_RESULTS
artifact_version: "1.0"
created_date: 2026-10-07
status: "WITHDRAWN 2026-10-07 (does not match the cloud interface); as tested: v7 passed its gates, hd-v2 6 of 7"
author: PE39 (`session_01CHFdeCiw98MgmvoYznRE76`)
pre_registration: TYPESAFE-LADDER-PREREGISTRATION-20261007.md, commit 3041eed
---

# TypeSafe reasoning-strength ladder: acceptance results for v7 and hd-v2

> **Withdrawn, 2026-10-07: v7 and hd-v2 do not match the cloud interface.** Nathan's screenshot of the cloud interface shows effort as one slider per model, from Faster to Smarter, with Ultracode as its top stop, above Max. This record took the Claude Code documentation's line that ultracode is a switch combining with every level, and built both requests on it. As a result they read cells, such as "medium with ultracode", that the cloud interface cannot select. The results below stand as a record of what was tested; they do not put either request in force. v6 and hd-v1 stay in force until a corrected request is accepted. The installed Claude Code's fallback cloud picker (surface `ccr`) lists Low, Medium, High, Extra and Max for both models, and the interface adds Ultracode above Max.

## Outcome

- **v7 (Glow app and repository sessions): accepted.** All four pre-registered gates pass. v7 is now the request in force for these sessions, replacing v6.
- **hd-v2 (Human Design jobs): not accepted under its gate.** It scored 6 of 7, where 7 of 7 was required. Six cases pass, and HA5 now reads max with ultracode. The miss is HA7, a case added at the pre-registration review. Its ultracode reading was right (on), but its level read high where extra high or max was expected. hd-v2 reproduces hd-v1's readings on all seven real jobs (table below).

  The pre-registered rule allows one revision, marked as fitted, and leaves the decision to Nathan if that also fails. No revision has been run. hd-v1 stays in force until Nathan decides.

## Timeline (UTC, 2026-10-07)

| Time | Event |
|---|---|
| 03:31:09 | Pre-registration committed (`3041eed`); pushed by 03:31:12 |
| 03:31:27 | Pre-registration note added to the HD scorer's Notion page (its own procedure requires it) |
| 03:31:47 | First reading sent |
| 03:33:19 | Last reading sent: the first Flow Manager run, under v7 |

There were 77 readings in all. Every one returned HTTP 200 from `jev-1.13.0`, with no errors. The
raw readings are in `results/`. Part B's readings carry each text's SHA-256 in place of the text.

## v7, Part A: 12 cases, run 1 (run 2 shown where its cell differs)

| Case | Expected | Read | Effort | P(ultracode) | P(Fable) | Run 2 |
|---|---|---|---|---|---|---|
| A1 Record given results | low; ultracode off; Opus 5.5 | Opus 5.5 at low | 0.01 | 0.03 | 0.00 | same |
| A2 One documented setting | low or medium; ultracode off; Opus 5.5 | Opus 5.5 at medium | 0.97 | 0.04 | 0.01 | same |
| A3 Listed repairs on a reviewed client | high or extra high; ultracode off; Opus 5.5 | Opus 5.5 at high | 1.90 | 0.09 | 0.00 | same |
| A4 Check of a follow-up commit | high or extra high; ultracode off; Opus 5.5 | Opus 5.5 at high | 2.02 | 0.09 | 0.00 | same |
| A5 First look at a large new system | max; ultracode either; Fable 5.1 | Fable 5.1 at max | 3.99 | 0.39 | 0.97 | same |
| A6 First live run on real cards | max; ultracode off; Fable 5.1 | Fable 5.1 at max | 4.00 | 0.10 | 0.99 | same |
| A7 Endpoint-by-endpoint check | high or extra high or max; ultracode on; either model | Opus 5.5 at extra high with ultracode | 2.96 | 0.77 | 0.09 | same |
| A8 Mechanical conversion of many modules | low or medium or high; ultracode on; Opus 5.5 | Opus 5.5 at high with ultracode | 1.80 | 0.75 | 0.03 | same |
| A9 Cause that two fixes missed | max; ultracode off; Fable 5.1 | Fable 5.1 at max | 3.96 | 0.15 | 0.99 | same |
| A10 Licence survey of many packages | low or medium or high; ultracode on; Opus 5.5 | Opus 5.5 at high with ultracode | 2.43 | 0.83 | 0.05 | Opus 5.5 at extra high with ultracode |
| A11 Conflicting legal sources | extra high or max; ultracode off; either model | Opus 5.5 at extra high | 3.25 | 0.12 | 0.33 | same |
| A12 Name suggestions | low or medium; ultracode off; Opus 5.5 | Opus 5.5 at low | 0.16 | 0.10 | 0.04 | same |

**Gate A passes.** All three conditions hold:
- 12 of 12 cases pass, against 11 required;
- A7, A8 and A10 read ultracode on. A8 reads "high with ultracode", which shows that ultracode is read below the top levels;
- A5, A6 and A9 read Fable 5.1.

**Part C, noise (reported):**
- The same cell came back on 11 of 12 cases.
- The largest changes between runs were 0.23 in effort score, 0.01 in P(ultracode) and 0.03 in P(Fable 5.1).
- The one change was A10: its effort score moved from 2.43 to 2.66, across the cut between high and extra high, so its run-2 cell is outside its expected set.

## v7, Part B: 31 recorded Glow app texts, with Nathan's picks as labels

| Gate | Result | Needed | v6 on the same texts |
|---|---|---|---|
| B_effort | level equal to the pick on 26; within one level on 31 | 24 and 30 | 26 and 31 |
| B_model | model equal to the pick on 27 (Fable picks 8 of 9; Opus picks 19 of 22) | 26 (6 and 18) | 27 (8 and 19) |
| B_ultracode | off on 20 of the 20 plainly single-thread texts | 19 | v6 could not read ultracode as a separate setting |

All three gates pass. Two findings, reported and not gated:

- **Ultracode stays off on all 31 real texts.** The highest P(on) is 0.31, on the P06.DB exact-head review. That includes P06.DB's implementation, which Nathan ran as "Fable Max Ultracode": v7 reads it "Fable 5.1 at max" with ultracode off (P 0.13), as the pre-registration predicted, since its text describes a plan-driven implementation. v7 can express his cell but did not choose ultracode for that text. Ultracode fires on broad work that splits into many separate parts (A7, A8, A10).
- **On the 9 texts where Nathan overrode the v6 reading,** v7 reads the same cell as v6 on all 9, not his override. On these texts the fix changed nothing; their disagreement with Nathan is about level and model, which v7 inherits unchanged from v6.

| Text | Nathan's pick | v6 | v7 | P(ultracode) |
|---|---|---|---|---|
| M02-C1 correction session (PR18 review findings) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.09 |
| M02-I1 implementation session (PR18) | Opus 5.5 at extra high | Opus 5.5 at high | Opus 5.5 at high | 0.10 |
| M02 delta review of PR18's final head (5e3fb2f against ccebd1b) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.15 |
| M02 exact-head code and security review (PR18 @ ccebd1b) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.20 |
| P06.1-I1 exact-head code and security review (code head 9ff600f) | Opus 5.5 at max | Fable 5.1 at max | Fable 5.1 at max | 0.23 |
| P06.1-I1 implementation session (Stream sandbox harness and bypass matrix) | Opus 5.5 at extra high | Fable 5.1 at max | Fable 5.1 at max | 0.15 |
| P06.1-I2a revocation and safety, live | Opus 5.5 at max | Fable 5.1 at max | Fable 5.1 at max | 0.13 |
| P06.1-C2 second offline correction pass on the harness | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.06 |
| P06.1 flake fix exact-head review (code head 8b8b1bd) | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.06 |
| P06.1-C3 third offline correction pass on the harness | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.07 |
| P06.1-C2 exact-head review (merge commit 63e922f) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.08 |
| P06.1-C3 exact-head review (merge commit 8c1a8c0) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.07 |
| P06.1-C1 offline correction pass on the I1 harness | Opus 5.5 at extra high | Opus 5.5 at high | Opus 5.5 at high | 0.08 |
| P06.1-I2a exact-head review (merge commit 6a51dae) | Fable 5.1 at extra high | Fable 5.1 at max | Fable 5.1 at max | 0.12 |
| P06.1-C1 exact-head review (merge commit e85bba0) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.10 |
| P06.1-I2b implementation (revision 2; revision 1 read by DM-05) | Fable 5.1 at extra high | Fable 5.1 at max | Fable 5.1 at max | 0.12 |
| P06.1-I2b exact-head review (merge commit 55b2238) | Fable 5.1 at max | Fable 5.1 at max | Fable 5.1 at max | 0.12 |
| App Manager 4 (manager session, created by App Manager 3) | Fable 5.1 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.12 |
| P06.1-C4 fourth offline correction pass on the harness | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.09 |
| P06.1-C5 fifth offline correction pass on the harness | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.06 |
| P06.1-C5 exact-head review (C5's head 1a5f58a) | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.09 |
| P06.DB implementation (revision 1) | Fable 5.1 at ultracode | Fable 5.1 at max | Fable 5.1 at max | 0.13 |
| P06.DB exact-head review | Fable 5.1 at max | Fable 5.1 at max | Fable 5.1 at max | 0.31 |
| P06.DB-C1 correction pass | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.07 |
| P06.DB-C1 exact-head review, revision 2 | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.08 |
| P06.DB-C2 exact-head review | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.10 |
| P06.2 Stage A implementation | Opus 5.5 at extra high | Opus 5.5 at extra high | Opus 5.5 at extra high | 0.11 |
| P06.2 Stage A exact-head review | Fable 5.1 at max | Fable 5.1 at max | Fable 5.1 at max | 0.12 |
| P06.2 Stage B1 implementation | Fable 5.1 at extra high | Fable 5.1 at extra high | Fable 5.1 at extra high | 0.09 |
| P06.2 Stage B1 exact-head review | Fable 5.1 at max | Fable 5.1 at max | Fable 5.1 at max | 0.12 |
| P06.2 Stage B1-C1 correction | Opus 5.5 at high | Opus 5.5 at high | Opus 5.5 at high | 0.07 |

## hd-v2: seven cases, run 1

| Case | Expected | Read | Effort | P(ultracode) | P(Fable) | Result |
|---|---|---|---|---|---|---|
| HA1 Record a delivered report | low; ultracode off; Opus 5.5 | Opus 5.5 at low | 0.00 | 0.05 | 0.01 | pass |
| HA2 Two named one-line fixes | medium; ultracode off; Opus 5.5 | Opus 5.5 at medium | 1.00 | 0.12 | 0.00 | pass |
| HA3 Repair four named defects | high or extra high; ultracode off; Opus 5.5 | Opus 5.5 at high | 1.99 | 0.16 | 0.00 | pass |
| HA4 First parent-child composite | max; ultracode off; Fable 5.1 | Fable 5.1 at max | 3.99 | 0.17 | 0.99 | pass |
| HA5 Claim audit of the first six reports | extra high or max; ultracode on; either model | Opus 5.5 at max with ultracode | 3.60 | 0.79 | 0.15 | pass |
| HA6 Standard single-person reading | high or extra high; ultracode off; Opus 5.5 | Opus 5.5 at extra high | 3.00 | 0.15 | 0.01 | pass |
| HA7 Entry-by-entry glossary check | extra high or max; ultracode on; either model | Opus 5.5 at high with ultracode | 1.80 | 0.62 | 0.02 | fail: level |

Run 2 gave the same cell on 7 of 7 cases. The largest changes between runs were 0.16 in effort score and 0.02 in P(ultracode).

### Why HA7 missed

- **Its effort reading:** medium 0.54, high 0.20, extra high 0.16, max 0.10.
- **Its text** says only "Before the new 64-gate glossary replaces the old one, check each gate entry against the three reference works it cites, entry by entry". It does not say that later reports depend on the glossary, or whether any check follows.
- **The levels it was read against:** hd-v2's effort level texts are hd-v1's accepted texts, which place checking a document against its sources at medium.
- **Ultracode:** the reading was right (on, P 0.62).

The expectation was added at review, and it is not changed after the reading.

### hd-v2 against hd-v1 on the seven real jobs (reported)

| Job | hd-v1 (00:03 UTC) | hd-v2 | P(ultracode) |
|---|---|---|---|
| J0 General: a typical three-report request | Opus 5.5 at extra high (3.03) | Opus 5.5 at extra high (3.00) | 0.33 |
| J1 Controller: routine production run | Opus 5.5 at extra high (2.96) | Opus 5.5 at extra high (2.96) | 0.12 |
| J2 Controller: first live production run here | Opus 5.5 at max (4.00) | Opus 5.5 at max (3.99) | 0.14 |
| J3 Author: romantic composite, type already produced | Opus 5.5 at extra high (3.00) | Opus 5.5 at extra high (3.00) | 0.16 |
| J4 Author: first single-person reading on this platform | Opus 5.5 at max (3.60) | Opus 5.5 at max (3.58) | 0.13 |
| J5 Author: focused answer to two questions | Opus 5.5 at high (2.04) | Opus 5.5 at high (2.04) | 0.12 |
| J6 QA: formatting check by the same author | Opus 5.5 at medium (1.01) | Opus 5.5 at medium (1.00) | 0.12 |

## The reading Nathan asked for: the first Flow Manager run (HDE-EPIC040 drain)

The action text is the one sent to v6 at 02:25:11 UTC, unchanged (SHA-256
`9e850d865a19b4556242f981dfebde255bec8779a5e9cd53766e08c92d0a1624`).

> **TypeSafe v7: Opus 5.5 at extra high.** Effort score 3.07 (confidence 0.49): low 0.00, medium 0.01, high 0.25, extra high 0.40, max 0.34. Ultracode P(on) 0.46. Model probabilities Fable 5.1 0.32, Opus 5.5 0.68 (confidence 0.36). Ten rungs, computed: low 0.00, low with ultracode 0.00, medium 0.01, medium with ultracode 0.00, high 0.14, high with ultracode 0.12, extra high 0.22, extra high with ultracode 0.18, max 0.18, max with ultracode 0.16. Flags: effort boundary between max and extra high; ultracode near tie. Sent 2026-10-07T03:33:19Z.

The v6 reading of the same text was "Opus 5.5, extra high" (score 2.87). It could not express
ultracode at any level other than the top, or max with ultracode.

## What changes where

| Place | State |
|---|---|
| Nathan's `typesafe-scoring` skill | v7 package built (request, script and SKILL.md), for Nathan to install. Until it is installed, sessions still produce v6 readings |
| Nathan's `hd-typesafe-scoring` skill | hd-v2 package drafted and held, pending Nathan's decision |
| Notion: Glow app usage log | v7 accepted, recorded at the top; v6 marked superseded |
| Notion: HD readings usage log | hd-v2 result recorded at the top; hd-v1 stays in force |
| Notion: the original usage log (v4) | not edited: a frozen history page (E-031) |
| glow-dating-app: `docs/planning/reasoning-level-matrix.md` §6-7, `manager-workflow.md` step 3, `docs/continuity/owner-directions.md` (a new OD row), `reasoning-level-evidence.md` | not reachable from this session (access was refused); Nathan or a Glow app session updates them |
| Notion copies of those files (*Implementation Control*, *Owner-direction register*) | they follow the repository; left until the repository changes |

## Canon relied on

- `AGENTS.md`: the canon-first rule.
- HDE Build Notes (PF10) v13.5, §2.38 PF10-AINEUTRAL-001: no governance rule requires a specific AI provider, product, model or effort level. Canon sets no ladder.
- Ledger E-031: no TypeSafe reading is taken or logged for GTWPE steps; Nathan asked for this one by name. The reading is recorded here, not in a Notion uses table.
