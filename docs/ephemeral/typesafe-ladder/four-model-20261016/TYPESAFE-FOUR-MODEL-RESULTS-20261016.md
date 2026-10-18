---
artifact_type: SCORER_ACCEPTANCE_RESULTS
artifact_version: "1.0"
created_date: 2026-10-18
status: "hd-v3 ACCEPTED; v8 NOT ACCEPTED on run 1 (B_model); v8.1 pre-registered in section 4, not yet read"
pre_registration: TYPESAFE-FOUR-MODEL-PREREGISTRATION-20261016.md, commit 5438f38, approved by Nathan on 2026-10-18 ("proceed")
---

# TypeSafe four-model ladder: acceptance results for v8 and hd-v3

## 1. Outcome

- **hd-v3 (Human Design jobs): accepted.** All 8 cases pass, including HA7, which reads Haiku 5.5 as required. Run 2 gave the same cell on 8 of 8 cases. hd-v3 replaces hd-v1 for HD production jobs.
- **v8 (Glow app and repository sessions): not accepted on run 1.**
  - Gates A and B_effort pass. Gate B_model fails: 4 of Nathan's 9 Fable 5.1 picks read Fable 5.1, where 6 were needed.
  - The pre-registration allows one revision, v8.1, run on the same cases and marked as fitted to them. Section 4 fixes v8.1 before any reading of it is sent.
  - v6 stays in force until v8.1 is accepted or Nathan decides.

## 2. Readings

| Item | Value |
|---|---|
| Readings sent | 2026-10-16, from 17:06:39 to 17:07:05 UTC |
| Requests | `request-v8.json` (`e19f4e32…`) and `request-hd-v3.json` (`c548868d…`), both matching their pins |
| Response | every reading returned HTTP 200 from `jev-1.13.0`; none was missing |
| Credential | the environment's proxy attached it; the script sent no Authorization header |
| Readings in all | 16 + 16 for v8 Part A, 31 for Part B, 8 + 8 for the hd-v3 cases, 7 for the hd-v3 jobs |

Raw readings are in `results/`. The Part B readings carry each text's SHA-256 in place of the text. The evaluator's full output is in `results/evaluation-v8.txt` and `results/evaluation-hd-v3.txt`.

## 3. v8, run 1

### Gate A: pass

- 16 of 16 cases meet every expectation (14 required).
- A5, A6 and A9 read Fable 5.1.
- A1, A13 and A14 all read Haiku 5.5 (2 required).
- A15 and A16 both read Sonnet 5.5 (1 required).

| Case | Cell | Highest model probability |
|---|---|---|
| A1 Record given results | Haiku 5.5 at low | Haiku 0.94 |
| A2 One documented setting | Sonnet 5.5 at medium | Sonnet 0.79 |
| A3 Listed repairs on a reviewed client | Opus 5.5 at high | Opus 0.99 |
| A4 Check of a follow-up commit | Opus 5.5 at high | Opus 1.00 |
| A5 First look at a large new system | Fable 5.1 at max | Fable 0.88 |
| A6 First live run on real cards | Fable 5.1 at max | Fable 0.89 |
| A7 Endpoint-by-endpoint check | Opus 5.5 at max | Opus 0.55 (Sonnet 0.36) |
| A8 Mechanical conversion of many modules | Sonnet 5.5 at high | Sonnet 0.53 (Opus 0.45) |
| A9 Cause that two fixes missed | Fable 5.1 at max | Fable 0.94 |
| A10 Licence survey of many packages | Haiku 5.5 at extra high | Haiku 0.46 (Opus 0.29) |
| A11 Conflicting legal sources | Sonnet 5.5 at extra high | Sonnet 0.65 |
| A12 Name suggestions | Haiku 5.5 at low | Haiku 0.50 (Sonnet 0.49) |
| A13 Locate definitions for a larger session | Haiku 5.5 at low | Haiku 1.00 |
| A14 Route support emails | Haiku 5.5 at medium | Haiku 0.82 |
| A15 Named date-picker bug | Sonnet 5.5 at medium | Sonnet 0.99 |
| A16 Help article for a shipped feature | Sonnet 5.5 at medium | Sonnet 0.99 |

**Part C (reported):**
- Run 2 gave the same cell on 15 of 16 cases. The one change was A12, a near tie, which moved to Sonnet 5.5 at low.
- The largest run-to-run changes were 0.04 in effort score and 0.07 in a model probability.

### B_effort: pass

The rung equals Nathan's pick on 25 of 31 (24 required) and is within one rung on 31 of 31. v6 read 26 on the same texts. The effort question is v6's, unchanged; the difference of one is within the noise recorded for v6.

### B_model: fail

| Condition | Result | Needed | v6 |
|---|---|---|---|
| Fable 5.1 picks read Fable 5.1 | **4 of 9** | 6 | 8 |
| Opus 5.5 picks read Opus 5.5 or Sonnet 5.5 | 21 of 22 (none read Sonnet) | 18 | 19 Opus |
| Haiku 5.5 read on | 0 of 31 | at most 1 | — |

These five Fable picks moved to Opus 5.5:

| Text | P(Fable 5.1) under v7 | P(Fable 5.1) under v8 |
|---|---|---|
| P06.1-I2a exact-head review | 0.69 | 0.18 |
| P06.1-I2b exact-head review | 0.54 | 0.12 |
| App Manager 4 | 0.30 (v6 already read Opus) | 0.02 |
| P06.2 Stage B1 implementation | 0.55 | 0.00 |
| P06.2 Stage B1 exact-head review | 0.96 | 0.11 |

v7's model question was v6's, with only its ladder wording changed.

**Diagnosis.** v8 rewrote the strong model's "what". Three phrases in it match these texts directly, and none of them is in v6's text:
- "the exact-head review that gates a merge", which also appears in the third example. Three of the moved texts are exact-head reviews.
- "where a miss would reach a merge, a live system or later work". The B1 implementation text says its miss "would carry into the later live Stream stage".
- "across a large or security-sensitive codebase".

**Reported, not gated.**
- On two texts where Nathan had overridden v6's Fable reading with Opus, v8 reads Opus: the P06.1-I1 exact-head review and P06.1-I2a live.
- No Opus pick reads Sonnet 5.5.

## 4. v8.1: the one allowed revision (pre-registered before any v8.1 reading)

- **Status:** fitted to v8's run-1 Part B miss, and recorded as such.
- **Built by:** `build_v8_1.py`, from `request-v8.json`.
- **File:** `request-v8.1.json`, SHA-256 `55b835dac95da6bc092ec61235f9b4eb33d46633643849509383227d4b82ba8f`, pinned in `score_v8.py` as version `v8.1`.
- **What changes:** only the strong model's "what" and examples.
  - The "what" returns to v6's accepted text, less the three kinds of work v8 hands to the cheaper options: checking results against a list, recording decisions, and writing or updating documents.
  - Its measurement sentence is restated for four models: "first of the four on the general and work-task indexes at max, at a quarter to a sixth of the most capable model's cost per task and 2 to 3 times faster per task".
  - The three phrases named in section 3 and the exact-head review example are removed.
  - `build_v8_1.py` asserts that everything else in the request is identical to v8.
- **What stays the same:** the cases, gates and rule are v8's (`acceptance-v8.json`, section 5 of the pre-registration). v8.1 is read on Part A twice and on Part B once.
- **Outcome rule:** v8.1 is accepted when gates A, B_effort and B_model all pass on its run 1. If any fails, Nathan decides, and v6 stays in force until he does.

v8.1's results are added below this line after its readings. Nothing above this line changes.

## Canon relied on

- `AGENTS.md`: the canon-first rule, and evidence attribution (tested state, time and limitations recorded).
- HDE Build Notes (PF10) v13.5.8, addendum 2.1: the reading is the installed TypeSafe skill's output; no agent gives its own recommendation; the Product Owner picks.
