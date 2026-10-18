---
artifact_type: SCORER_ACCEPTANCE_RESULTS
artifact_version: "1.0"
created_date: 2026-10-18
status: "hd-v3 ACCEPTED; v8 and v8.1 NOT ACCEPTED (B_model); v8.2 ACCEPTED on its run 1 (section 8), at the gate thresholds; v8.2 replaces v6 for Glow app and repository sessions"
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

## 5. v8.1, run 1 (results)

Readings were sent on 2026-10-18 from 08:36:12 to 08:36:24 UTC: 16 + 16 for Part A and 31 for Part B. Every reading returned HTTP 200 from `jev-1.13.0`, from `request-v8.1.json` matching its pin. The evaluator's output is in `results/evaluation-v8.1.txt`; its last line says "(v8)" because v8.1 is read against v8's cases.

| Gate | Result | Needed |
|---|---|---|
| A | pass: 15 of 16 meet every expectation; Fable on A5, A6, A9; Haiku on 3 of A1, A13, A14; Sonnet on 2 of A15, A16 | 14; all three; 2; 1 |
| B_effort | pass: rung equal to the pick on 25 of 31, within one rung on 31 | 24 and 30 |
| B_model | **fail: Fable 5.1 picks read Fable 5.1 on 5 of 9**; Opus 5.5 picks read Opus or Sonnet on 20 of 22; Haiku on 0 | 6; 18; at most 1 |

- **The A8 miss.** A8 (mechanical conversion of 240 modules) is a near tie, Opus 5.5 0.50 against Sonnet 5.5 0.49, and it read Opus. Gate A still passes.
- **Part C.** Run 2 gave the same cell on 16 of 16. The largest changes were 0.09 in effort score and 0.05 in a model probability.
- **Model agreement with Nathan's picks.** 25 of 31 for v8.1, as for v8, against 27 for v6.

The Fable 5.1 picks, P(Fable 5.1):

| Text | v7 | v8 | v8.1 | v8.1 cell |
|---|---|---|---|---|
| P06.1-I2a exact-head review | 0.69 | 0.18 | 0.45 (Opus 0.54) | Opus 5.5 at max |
| P06.1-I2b implementation | 0.99 | 0.60 | 0.72 | Fable 5.1 at max |
| P06.1-I2b exact-head review | 0.54 | 0.12 | 0.40 (Opus 0.59) | Opus 5.5 at max |
| App Manager 4 (v6 also read Opus) | 0.30 | 0.02 | 0.04 | Opus 5.5 at extra high |
| P06.DB implementation | 0.88 | 0.50 | 0.59 | Fable 5.1 at max |
| P06.DB exact-head review | 0.95 | 0.81 | 0.84 | Fable 5.1 at max |
| P06.2 Stage A exact-head review | 0.98 | 0.83 | 0.91 | Fable 5.1 at max |
| P06.2 Stage B1 implementation | 0.55 | 0.00 | 0.08 | Opus 5.5 at extra high |
| P06.2 Stage B1 exact-head review | 0.96 | 0.11 | 0.76 | Fable 5.1 at max |

**What the two runs show.**
- Removing v8's three strong-model phrases recovered P(Fable 5.1) on every Fable pick, most on the B1 exact-head review (0.11 to 0.76).
- It did not recover v6's level. P(Fable 5.1) stays below v7's on all nine picks.
- The remaining differences from v6's model question are its rewritten tradeoff (four-model facts in place of v6's two-model comparison) and the split of probability across four options.
- This is an observation from two fitted runs, not a tested cause.

**Outcome.** Under the pre-registration, v8.1 failing means Nathan decides. v6 stays in force for Glow app and repository sessions until he does. hd-v3 is unaffected: it was accepted in its own right in section 1.

## Canon relied on

- `AGENTS.md`: the canon-first rule, and evidence attribution (tested state, time and limitations recorded).
- HDE Build Notes (PF10) v13.5.8, addendum 2.1: the reading is the installed TypeSafe skill's output; no agent gives its own recommendation; the Product Owner picks.

## 6. hd-v3 deliverables (pre-registration section 6), 18 October 2026

Every step was read back after it was written.

| Step | What was done | Read-back |
|---|---|---|
| Uses table `collection://6d7a823b-eb6c-42ed-9d97-93ec1c5306ae` | Options added: the 12 Sonnet 5.5 and Haiku 5.5 cells to *TypeSafe cell* and *Nathan's pick*; "Sonnet 5.5" and "Haiku 5.5" to *TypeSafe model*; "hd-v3" to *Version*. | All 26 earlier options kept their IDs |
| hd-v3 rows | 15 rows added: HA1 to HA8 as `acceptance` and J0 to J6 as `live`, each with *Run* "hd-v3 setup, 16 Oct 2026" and *Nathan's pick* "pending". The hd-v1 rows are unchanged. | *TypeSafe cell*, *Rung probabilities* and *Model probabilities* identical to the script output on all 15 |
| Log page 3f24590a-05eb-8151-b4a0-ee4ff3f1612a | A callout at the top marks hd-v3 in force and hd-v1 superseded, followed by an hd-v3 section with three file blocks. The earlier record is kept as written. | Page re-fetched |
| hd-v3 files on the log page | `request-hd-v3.json`, `score_v8.py` (`822a80cb…`, the committed script with the v8.1 pin) and `acceptance-hd-v3.json` uploaded | Downloaded back; all three match their SHA-256 |
| Installable skill | `hd-typesafe-scoring.skill`, packaged with skill-creator's `package_skill.py` and passing its validator. It contains `hd-typesafe-scoring/SKILL.md` (8,152 bytes). The package's SHA-256 is `53f42b3d85243c6bfc243ac99294d45429b9dd33c1f0ba670d1faa6c0a662495`. | Handed to Nathan to install; not committed to the repository |

**Not done, per the pre-registration:** because v8 and v8.1 were not accepted, nothing changed in the Glow app uses table, on the Glow app log page, or in the `typesafe-scoring` skill. v6 stays in force for Glow app and repository sessions.

## 7. v8.2: Nathan's option (c) (pre-registered before any v8.2 reading)

**Authority.** Nathan, 2026-10-18, chose option (c) of the three put to him after v8.1 failed: "c, go ahead". The option as put to him: "Keep v6's Fable and Opus text word for word, and add only the Sonnet and Haiku options with their own figures. Same test, re-run on the same cases."

**Status.** This is the second revision fitted to the same cases, and it is recorded as such; a pass is weaker evidence than a first-run pass.

**File.** `request-v8.2.json`, SHA-256 `62486fcc4357e5917c3e9ba3e1ba9e2709364f0338dde70d4a88b116022b22ec`, built by `build_v8_2.py` from `request-v6.json` (`72beaafa…`) and `request-v8.json`.

**What it keeps from v6, word for word:**
- the effort Score;
- the model question's wording;
- v6's two-model tradeoff;
- v6's two options, with their keys (`most_capable_model`, `strong_lower_cost_model`), texts and examples.

**What it adds:**
- one sentence before the tradeoff, scoping it to the first two options;
- one paragraph after it, giving the two new options' prices and figures from `evidence-20261016.json`;
- v8's `balanced_model` and `small_fast_model` options, with "the strong model" renamed to "the strong lower-cost model".

`build_v8_2.py` asserts each of these.

**Script.** `score_v8.py`, SHA-256 `d8435c16fc96ed0055f9857bc3b0a2f1c25e1a9a1f1c33206bce33a03cfd6e86`, pins the new request as version `v8.2`. It also maps v6's key `strong_lower_cost_model` to Opus 5.5. It refuses an answer whose four options do not name the four models exactly once each. The rule is unchanged. The HD skill keeps its own pinned copy, `822a80cb…`, on the HD log page; that copy needs no change, because its hd-v3 pin is the same.

**Cases and gates.** The same as v8's (`acceptance-v8.json`; pre-registration section 5). v8.2 is read on Part A twice and on Part B once.

**Outcome rule.**
- If gates A, B_effort and B_model all pass on v8.2's run 1, v8.2 is accepted, and the pre-registration's section 6 steps follow for the Glow app.
- If any gate fails, v6 stays in force for Glow app and repository sessions (option (a)).

v8.2's results are added below this line after its readings. Nothing above this line changes.

## 8. v8.2, run 1 (results)

**The readings.**
- Sent on 2026-10-18, from 09:01:53 to 09:02:07 UTC: 16 + 16 for Part A and 31 for Part B.
- Every reading returned HTTP 200 from `jev-1.13.0`, from `request-v8.2.json` matching its pin.
- The evaluator's output is in `results/evaluation-v8.2.txt`.

| Gate | Result | Needed |
|---|---|---|
| A | **pass at the threshold:** 14 of 16 cases meet every expectation; A5, A6 and A9 read Fable; Haiku on all 3 of A1, A13 and A14; Sonnet on both A15 and A16 | 14 of 16; all three Fable; 2 of 3 Haiku; 1 of 2 Sonnet |
| B_effort | **pass:** the rung equals the pick on 25 of 31 and is within one rung on 31 | 24 and 30 |
| B_model | **pass at the threshold:** Fable 5.1 picks read Fable 5.1 on 6 of 9; Opus 5.5 picks read Opus or Sonnet on 19 of 22; Haiku on 0 of 31 | 6; 18; at most 1 |

**The two Part A misses.**
- **A8**, mechanical conversion of 240 modules: read Opus 5.5 at high (Opus 0.91, Sonnet 0.08); expected Haiku or Sonnet.
- **A10**, licence survey of 180 packages: read Opus 5.5 at extra high (Opus 0.69, Haiku 0.27); expected Haiku or Sonnet.
- Under v8.2, both broad mechanical sweeps go to the strong model.

**Part C.** Run 2 gave the same cell on all 16 cases. The largest run-to-run changes were 0.06 in effort score and 0.05 in a model probability.

**Agreement with Nathan's picks.** The model equals his pick on 25 of 31 (v6: 27) and the rung on 25 of 31 (v6: 26). No Opus pick reads Sonnet 5.5.

P(Fable 5.1) on the Fable picks, and on the Opus picks that read Fable:

| Text | Pick | v6 | v7 | v8 | v8.1 | v8.2 | v8.2 cell |
|---|---|---|---|---|---|---|---|
| P06.1-I1 exact-head review | Opus | Fable | 0.97 | 0.47 | 0.78 | 0.92 | Fable 5.1 at max |
| P06.1-I1 implementation | Opus | Fable | 0.97 | 0.74 | 0.75 | 0.95 | Fable 5.1 at max |
| P06.1-I2a revocation and safety, live | Opus | Fable | 0.93 | 0.32 | 0.46 | 0.85 | Fable 5.1 at max |
| P06.1-I2a exact-head review | Fable | Fable | 0.69 | 0.18 | 0.45 | 0.58 | Fable 5.1 at max |
| P06.1-I2b implementation | Fable | Fable | 0.99 | 0.60 | 0.72 | 0.96 | Fable 5.1 at max |
| P06.1-I2b exact-head review | Fable | Fable | 0.54 | 0.12 | 0.40 | 0.47 | Opus 5.5 at max |
| App Manager 4 | Fable | Opus | 0.30 | 0.02 | 0.04 | 0.15 | Opus 5.5 at extra high |
| P06.DB implementation | Fable | Fable | 0.88 | 0.50 | 0.59 | 0.87 | Fable 5.1 at max |
| P06.DB exact-head review | Fable | Fable | 0.95 | 0.81 | 0.84 | 0.94 | Fable 5.1 at max |
| P06.2 Stage A exact-head review | Fable | Fable | 0.98 | 0.83 | 0.91 | 0.98 | Fable 5.1 at max |
| P06.2 Stage B1 implementation | Fable | Fable | 0.55 | 0.00 | 0.08 | 0.42 | Opus 5.5 at extra high |
| P06.2 Stage B1 exact-head review | Fable | Fable | 0.96 | 0.11 | 0.76 | 0.95 | Fable 5.1 at max |

**What it shows.** Restoring v6's two-model text recovers most of v6's Fable signal. The three misses are:
- I2b's review and B1's implementation, which were already near ties under v7 (0.54 and 0.55);
- App Manager 4, which v6 also read as Opus.

The three Opus picks that read Fable are the same three that v6 read Fable and Nathan overrode.

**Outcome.** v8.2 is accepted under section 7's rule. It replaces v6 for Glow app and repository sessions. The pre-registration's section 6 steps for the Glow app follow; they are recorded in section 9.

**Limits of this pass.**
- Two gates passed exactly at their thresholds.
- It is the second fitted revision.
- On the two broad mechanical sweeps (A8, A10), the strong model wins where the cheaper options were expected.

## 9. v8.2 deliverables (pre-registration section 6 for the Glow app), 18 October 2026

Every step was read back after it was written.

| Step | What was done | Read-back |
|---|---|---|
| Uses table `collection://e1d83c6d-23b7-447f-8bc6-dcbb4829f24e` | Options added: the 12 Sonnet 5.5 and Haiku 5.5 cells to *TypeSafe cell* and *Nathan's pick*; "Sonnet 5.5" and "Haiku 5.5" to *TypeSafe model*; "v8.2" to *Version*. Earlier rows are unchanged. | Every earlier option kept its ID. *Manager model* is unchanged. |
| Log page 3e54590a-05eb-81a5-845b-f0a52f7c1cea | A callout at the top marks v8.2 in force and v6 superseded, with the history of v8 and v8.1 and the threshold passes. The earlier record is kept as written. | Page re-fetched |
| Installable skill | `typesafe-scoring.skill`, packaged with skill-creator's `package_skill.py` and passing its validator. It contains `SKILL.md`, `request-v8.2.json` (`62486fcc…`) and `scripts/score_v8.py` (`d8435c16…`, this directory's script). The package's SHA-256 is `2b79a57bcc1a5de7d81ac09ef56d9df8a735a1f31df3427c935e298fbdc423e8`. | Handed to Nathan to install; not committed to the repository |

**Two copies of the script.** The HD skill keeps its own pinned copy, `822a80cb…`, from commit `d91cb14`. The Glow skill carries `d8435c16…`, which adds the v8.2 pin. Both serve hd-v3 the same way.
