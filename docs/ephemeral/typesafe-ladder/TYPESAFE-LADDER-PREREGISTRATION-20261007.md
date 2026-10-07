---
artifact_type: SCORER_PREREGISTRATION
artifact_version: "1.0"
created_date: 2026-10-07
status: PRE-REGISTERED (no v7 or hd-v2 reading has been sent)
authority: Nathan (Product Owner), 2026-10-07, quoted in §1
author: PE39 (`session_01CHFdeCiw98MgmvoYznRE76`)
applies_to: the TypeSafe reasoning-strength scorer — request v7 (Glow app and repository sessions) and hd-v2 (Human Design report-production jobs)
---

# TypeSafe reasoning-strength ladder: pre-registration of v7 and hd-v2

This record fixes the requests, the rule and the acceptance test before any reading is sent.
The results are added afterwards in a separate file, `TYPESAFE-LADDER-RESULTS-20261007.md`. This
file is not changed after the first reading.

## 1. Why

Nathan, 2026-10-07, after PE39 gave him a v6 reading for the first Flow Manager run:

- "hmmm there should be 10 rungs"
- "I tried to fix this multiple times. Your current score is meaningless. I want whatever made you think there were only 6 rungs fixed across the board. of course ultracode and max need to be in there"
- "If you have to ask mne these questions, then that means the solution is not well researched"

## 2. What the research found

Sources were read on 2026-10-07. The Claude Code CLI installed in this environment is 2.1.292.

**Every model has five effort levels.** Claude Code's model configuration page lists `low`,
`medium`, `high`, `xhigh` and `max` for both Fable 5.1 and Opus 5.5. It adds: "The effort scale
is calibrated per model, so the same level name does not represent the same underlying value
across models." (`code.claude.com/docs/en/model-config.md`, 114,798 bytes, SHA-256
`66f827e0568361a36228d18a7fab5f2bd2786ee7d4f6e5523193440ae1c8b343`, lines 586-590 and 660.)

**Ultracode is a switch, not a sixth level.** The same page says:

- line 620: "Ultracode is a Claude Code setting rather than a model effort level: with it on, Claude orchestrates dynamic workflows for substantive tasks, at whichever effort level the session runs at."
- line 622: "Turning ultracode on or off with `/effort` or the `ultracode` setting leaves the effort level unchanged. … Picking a level in the `/effort` slider or the `/model` picker leaves ultracode as it was."
- line 630: "… keeping ultracode on at effort levels other than `xhigh` require Claude Code v2.1.284 or later. Before v2.1.284, turning on ultracode set the session to `xhigh` effort, picking another level turned it off …"
- lines 638-641: ultracode is unavailable only when workflows are turned off or the model does not support `xhigh`. Both models support `xhigh`.

**So each model has ten rungs:** five effort levels, each with ultracode off or on. Max and
ultracode are both in, and ultracode can sit at any level, including max. Across the two models
there are twenty cells.

## 3. Root cause of the six-rung ladder

Every request so far put ultracode on the effort scale as a sixth level "above max", beside a
separate model choice:

- the HDE stream's v4 (2026-09-24);
- the Glow app's v5 and v6 (2026-09-27);
- hd-v1 (2026-10-07).

That matched Claude Code before v2.1.284, when ultracode forced `xhigh` and choosing another level
turned it off. Since v2.1.284 ultracode combines with every level, but the requests were never
updated. The result:

- ultracode and max were mutually exclusive;
- four of each model's five ultracode settings could not be read at all;
- one signal on the effort Score (can one reader hold the work?) was really the ultracode
  question.

Nathan's recorded pick for P06.DB, "Fable Max Ultracode", is a cell the old ladder could not
express.

## 4. The design

One request per reading, with three independent questions:

| Question | TypeSafe type | What it reads |
|---|---|---|
| `effort` | Score, five levels | low, medium, high, extra high, max |
| `ultracode` | Noul | whether the work splits into many separate parts that independent agents can each take on in parallel |
| `model` | Choice | `most_capable_model` (Fable 5.1) or `strong_lower_cost_model` (Opus 5.5) |

**Where each question's text comes from.** `build_requests.py` builds both new requests from the
old ones and asserts every edit, so the derivation can be re-run.

- **`effort`:** v6's and hd-v1's accepted level texts are kept, with four changes:
  - "rung" becomes "level";
  - max's "the deepest single-session reasoning" becomes "the deepest reasoning level", since max can now run with ultracode;
  - the instruction loses signal (4) (can one reader hold the work?) and the "sixth rung" sentence;
  - the instruction ends: "Place the session (job) by these three signals only, not by whether the work should be split across many (several) independent agents."
- **`ultracode`:** new. Its true condition is one breadth condition; its false condition is one connected object followed as a whole, even when large or consequential.
  - Its evidence is v6's and hd-v1's ultracode evidence, moved into it. One source is added: Google Research, arXiv 2512.08296, +80.9% on tasks that split into parallel parts and −39 to 70% on sequential ones.
  - Two v6 harness statements are removed as outdated: "every request runs at extra high" and the 471,480-token pre-check.
  - v6's two ultracode examples (a first live run with real money, and a first review of a very large new system) are not carried into the true condition.
- **`model`:** v6's and hd-v1's text is kept. Only the ladder wording changes, and v6's outdated claim about which models support the many-agent setting is corrected.

**Why three questions, not one ten-level Score.** TypeSafe's Score page says to keep each Score
to one dimension and to split a judgment into one question per thing, combined in code
(`docs.typesafe.ai/primitives/score.md`, "Keep each Score question to one dimension" and the next
section). Its Noul page says to ask one yes/no question per Noul. Ultracode is a separate axis
from effort, per the documentation in §2. A single ladder across both models is not supported
either: the documentation says the same level name means different things on each model, and the
third-party measurements interleave the two models in no consistent order (research report,
2026-10-07).

## 5. The rule (applied by the script, never by hand)

- **Level:** the level nearest the effort score, with exact halves going up (cuts at 0.5, 1.5, 2.5 and 3.5).
- **Ultracode:** on when P(yes) is 0.5 or more.
- **Model:** Fable 5.1 when P(`most_capable_model`) is 0.5 or more; otherwise Opus 5.5.
- **Cell:** "<model> at <level>", with " with ultracode" added when ultracode is on. Example: "Fable 5.1 at max with ultracode".

**Recorded, never used by the rule:**
- every probability and both confidences;
- the ten rung probabilities and all twenty cell probabilities, computed as products of the three answers (TypeSafe evaluates them separately; their product is a summary, not a joint judgment);
- three flags:
  - effort boundary: the score is within 0.10 of a cut, or the top two levels are within 0.20 of each other;
  - ultracode near tie: P is between 0.40 and 0.60;
  - model near tie: P is between 0.40 and 0.60.

The reading is advisory. Nathan picks the cell, and the reading gates nothing.

**What the script enforces:**
- It refuses to send unless the request file's SHA-256 matches its pin, and it takes the version from the pinned file.
- By default it sends no Authorization header and reads no environment value.
- With `--key-from-env` (the HD Reader environment only), it reads `TYPESAFE_API_KEY` once, removes it from the environment and redacts it from any error text.

## 6. Files

All are in this directory.

| File | SHA-256 |
|---|---|
| `request-v7.json` | `834e43ea17fb0743bc12fd93cf2af2fe4ef1c89d066ecd6d59208cb8200c4dbb` |
| `request-hd-v2.json` | `39709aac99baaa4a6481bd6371fca503f6c6f63706d649aea7a77df12f7b792c` |
| `score_ladder.py` (record copy of the scoring script) | `4f4215dad8a91017065a69885fee2bf49bab05aebf07b751e8254bc8c3790d1f` |
| `evaluate_ladder.py` (applies the gates in §7) | `4d74b231f7223b83a8604ee59b1528a13b5cfb12b35c4791ff8d5701f2f1daa5` |
| `acceptance-v7.json` | `a081772d81a2cf967f0b99b2b3c03fe8afc00cd1ed90387c2f25219bf19ffa1b` |
| `acceptance-hd-v2.json` | `ef3398255eeddbdebabddf639631b0d4c6078e7307619bb6a1611fe10ffb1e55` |
| `build_requests.py` (derivation of both requests) | `94705049bcb8823b0a4c3dd770764e3061680fc5f0c84e6bd992af04b2f7662b` |

**Part B texts are kept out of this public repository.** v7's 31 Part B texts come from Nathan's
private Notion uses table (`collection://e1d83c6d-23b7-447f-8bc6-dcbb4829f24e`), so they are
not published here. Each row of `acceptance-v7.json` carries the SHA-256 of its exact text, and
the run checks every text against it before sending.

## 7. Acceptance test (fixed before any reading)

### v7

**Part A: 12 cases.** None copies an example from the request:

| Case | Level | Ultracode | Model |
|---|---|---|---|
| A1 record given results | low | off | Opus |
| A2 one documented setting | low or medium | off | Opus |
| A3 listed repairs on a reviewed client | high or extra high | off | Opus |
| A4 check of a follow-up commit | high or extra high | off | Opus |
| A5 first look at a 9,000-line new system | max | undecided | Fable |
| A6 first live run on real cards | max | off | Fable |
| A7 endpoint-by-endpoint check of 62 endpoints | high, extra high or max | on | not stated |
| A8 mechanical conversion of 240 modules | low, medium or high | on | Opus |
| A9 a cause that two fixes missed | max | off | Fable |
| A10 licence survey of 180 packages | low, medium or high | on | Opus |
| A11 conflicting legal sources | extra high or max | off | not stated |
| A12 name suggestions | low or medium | off | Opus |

A11 and A12 are out-of-frame cases (not coding sessions).

**Gate A** passes when all three hold:
- at least 11 of the 12 cases meet every stated expectation;
- A7, A8 and A10 read ultracode on;
- A5, A6 and A9 read Fable 5.1.

**Part B: 31 recorded Glow app texts.** Nathan's picks are the labels. His P06.DB pick, "Fable Max
Ultracode", maps to Fable 5.1, max, ultracode on. For that row, extra high also counts as the same
level: a launch with `--effort ultracode`, or a version before v2.1.284, runs at `xhigh`.

| Gate | Passes when |
|---|---|
| B_effort | the level equals his pick on at least 24 of 31 (v6 managed 26), and is within one level on at least 30 |
| B_model | the model equals his pick on at least 26 of 31 (v6: 27), including at least 6 of his 9 Fable 5.1 picks and 18 of his 22 Opus 5.5 picks |
| B_ultracode | ultracode reads off on at least 19 of the 20 texts the request's false condition plainly covers: listed correction passes, reviews of one correction or change, and plan-driven implementations |

**Reported, not gated:**
- ultracode on the other 11 Part B texts, which include large first reviews and live runs;
- the 9 texts where Nathan overrode the v6 reading he saw.

Part B tests agreement with picks Nathan made after seeing v6 readings. It is a no-regression
check, not proof of correctness.

**Part C:** Part A is read twice. Run-to-run differences are reported, not gated.

**Outcome.** v7 is accepted when gates A, B_effort, B_model and B_ultracode all pass on run 1. If
any fails, one revision (v7.1) is allowed, run on the same cases and marked as fitted to them. If
v7.1 also fails, Nathan decides.

### hd-v2

There are seven cases, and all seven must pass, as with hd-v1.

| Case | Level | Ultracode | Model | Basis |
|---|---|---|---|---|
| HA1 | low | off | Opus | hd-v1's accepted expectation |
| HA2 | medium | off | Opus | hd-v1's accepted expectation |
| HA3 | high or extra high | off | Opus | hd-v1's accepted expectation |
| HA4 | max | off | Fable | hd-v1's accepted expectation |
| HA5 (claim audit of the first six reports) | extra high or max | on | not stated | in hd-v1 this case sat above max |
| HA6 | high or extra high | off | Opus | hd-v1's accepted expectation |
| HA7 (entry-by-entry glossary check, new) | extra high or max | on | not stated | added at review |

The job texts J0 to J6 are re-read and reported, not gated. One revision (hd-v2.1) is allowed on
the same terms as for v7.

## 8. Pre-registration review (2026-10-07)

Three independent reviewers read the drafts before this record was fixed. None sent a request to
TypeSafe. They found six blocking defects, all fixed above:

1. The ultracode true condition mixed in the effort question's stakes signal. It is now one breadth condition.
2. Every ultracode-on case copied an example from the request. The cases were reworded, and the examples were removed from the true conditions.
3. B_effort could be passed by always answering "extra high". It now requires exact agreement on 24 or more.
4. B_ultracode treated off-picks made under the old ladder as ground truth. It is now gated only on the 20 texts the false condition plainly covers.
5. A widened figure ("orchestration neither helped nor hurt") had lost its scope. "The lower-cost model" is restored.
6. Fable 5.1 was tested by one case only. A5 and A6 now expect Fable, and Gate A requires all three Fable cases.

The minor findings were also applied:
- the script's error handling, per-reading output, per-job session, `--kind`, Notes field, hash pin, key handling and twenty-cell output;
- the evaluator's label alignment;
- the effort instruction's last sentence;
- the max wording;
- the ultracode harness sentence;
- the HD model sentence's source;
- widened sets for A12 and HA5;
- a new hd-v2 ultracode case (HA7).

## 9. Limits

- **Ultracode is unmeasured.** No third-party measurement of ultracode exists for either model, so the Noul's evidence comes from older multi-agent studies.
- **Part B labels are anchored.** Nathan saw a v6 reading before picking each cell.
- **Unchanged text carries its old limits.** The level texts and model criteria are v6's and hd-v1's, so any limit they had remains.
- **The glow-dating-app record is not updated.** That repository holds v6's record but was not reachable from this session. Its matrix, owner-direction register and manager workflow still describe the six-rung ladder until they are updated there.

## Canon relied on

- `AGENTS.md`: the canon-first rule.
- HDE Build Notes (PF10) v13.5, §2.38 PF10-AINEUTRAL-001, read in full from `main`: "No governance rule requires a specific AI provider, product, model or effort level." Canon sets no ladder, and no canon change is needed.
- Ledger E-031 (`docs/ephemeral/gtwpe.rewrite/ERRORS.md`): no TypeSafe reading is taken or logged for GTWPE steps. Nathan's request of 2026-10-07 asks for this reading by name.
