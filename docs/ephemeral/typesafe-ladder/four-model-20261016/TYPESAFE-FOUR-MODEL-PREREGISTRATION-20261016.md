---
artifact_type: SCORER_PREREGISTRATION
artifact_version: "1.0"
created_date: 2026-10-16
status: "PRE-REGISTERED, AWAITING NATHAN'S REVIEW (no v8 or hd-v3 reading has been sent)"
authority: Nathan (Product Owner), 2026-10-16, quoted in §1
applies_to: the TypeSafe reasoning-strength scorer — request v8 (Glow app and repository sessions, replacing v6) and hd-v3 (Human Design report-production jobs, replacing hd-v1)
---

# TypeSafe scorer: Sonnet 5.5 and Haiku 5.5 added (v8 and hd-v3)

This record fixes the two requests, the rule and the acceptance test before any reading is sent.
The results will go in a separate file. This file is not changed after the first reading.

## 1. Why

Nathan, 2026-10-16:

- "I want you to analyze all of the type-safe skills that I have in place and cross-reference them to their Notion tables I want to add Haiku and Sonnet rungs for all reasoning levels from low all the way up to ultra."
- The active models are Claude Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 and Opus 4.8, and the reasoning levels are `low`, `medium`, `high`, `xhigh`, `max` and `ultra`.
- "recommended for all", which settled these decisions:
  - D1: one four-way model question, with the most probable model winning;
  - D2: all five models have all six levels;
  - D3: a research workflow;
  - D4: both scorers;
  - D5: Opus 4.8 not added.
- "I need installable claude skills, not just repo skills."

## 2. What changes and what does not

| | v6 / hd-v1 (in force) | v8 / hd-v3 (this record) |
|---|---|---|
| Effort question | Score over six rungs: low, medium, high, extra high, max, ultracode | **Unchanged.** `build_v8.py` asserts that it is identical. |
| Model question | Choice between 2 options | Choice between 4 options with neutral names (below) |
| Rule | rung nearest the score, halves up; Fable 5.1 if P(most capable) is 0.5 or more, else Opus 5.5 | rung unchanged; model = the most probable of the four, an exact tie going to the higher-priced model |
| Cells | 12 | 24 (4 models × 6 rungs) |
| Flags | boundary; model near tie when P(most capable) is between 0.40 and 0.60 | boundary unchanged; model near tie when the top two model probabilities are within 0.20 |

The effort question is kept byte for byte. TypeSafe answers each question independently, so v8 and hd-v3 rung readings stay comparable with every recorded v6 and hd-v1 row. Part B checks this.

Model options. No product names appear in either request, and `build_v8.py` asserts this.

| Option | Model | List price (input / output per million tokens) |
|---|---|---|
| `most_capable_model` | Fable 5.1 | $10 / $50 |
| `strong_model` | Opus 5.5 | $4 / $20 |
| `balanced_model` | Sonnet 5.5 | $2 / $10 |
| `small_fast_model` | Haiku 5.5 | $0.10 / $0.50 for prompts up to 100,000 tokens; $0.50 / $2.50 above |

**Where the model texts come from.**

- **Fable 5.1 and Opus 5.5:** their criteria keep v6's and hd-v1's accepted text. The only changes are that "the lower-cost model" now reads "the strong model", and the work that now belongs to the two cheaper options is moved to them.
- **Facts added:** every new figure is a third-party or vendor figure from `evidence-20261016.json`.
  - That file holds 329 claims, each re-opened by an independent skeptic agent on 2026-10-16, and all 329 were confirmed.
  - Vendor figures are marked `third_party: false` there.
  - The Artificial Analysis figures for all four models come from the same Intelligence Index, v4.3.2, which is the version v6 and hd-v1 already cite.
- **Rung coverage:** both Sonnet 5.5 and Haiku 5.5 support all five single-session levels (low to max). Because both support `xhigh`, Claude Code also offers ultracode for both. Sources: Claude Code model-configuration page and Claude Platform effort page, accessed 2026-10-16.

## 3. The rule (applied by `score_v8.py`, never by hand)

- **Rung:** the rung nearest the effort score, with exact halves going up (cuts at 0.5, 1.5, 2.5, 3.5 and 4.5).
- **Model:** the option with the highest probability. An exact tie goes to the higher-priced model.
- **Cell:** "<model> at <rung>".
- **Recorded, never used by the rule:**
  - every probability and both confidences;
  - all 24 cell probabilities, each the product of the two independent answers;
  - two flags: boundary, and model near tie.
- **Status:** the reading is advisory. Nathan picks the cell, and the reading gates nothing (PF10 addendum 2.1, rule 2).
- **What the script refuses:** it sends nothing unless the request file's SHA-256 matches its pin. By default it sends no Authorization header. With `--key-from-env` (the HD Reader environment) it reads `TYPESAFE_API_KEY` once, removes it from the environment and redacts it from any error text.

## 4. Files

All are in this directory.

| File | SHA-256 |
|---|---|
| `request-v8.json` | `e19f4e328bd2ec0d6099dcf9b89e668065c77127d4895acf949de6f5d211d236` |
| `request-hd-v3.json` | `c548868d3c5a45c530474cf2de4b739b96699c2227459ee7e5db4e9c2af2ec8f` |
| `score_v8.py`, `evaluate_v8.py`, `build_v8.py`, `acceptance-v8.json`, `acceptance-hd-v3.json` | hashed at the commit that lands this record |

**Sources of the two requests:**

| Request | Built from | SHA-256 of the source | Where the source lives |
|---|---|---|---|
| v8 | `request-v6.json` | `72beaafa4a03f4d74f5f9ff9a58c8e36e3a75c77d1c77d02c8e835a74345593a` | Nathan's installed `typesafe-scoring` skill |
| hd-v3 | `request-hd-v1.json` | `ffa7af75bb6f305430a2113d21e642e36260af4d4a45ea22498b3d6848ce9ba0` | the Notion page *TypeSafe effort scorer — HD readings usage log*; downloaded and checked against the skill's pin on 2026-10-16 |

**Part B texts.** As for v7, Part B's 31 texts are Nathan's private uses-table rows and are not published here. Each row of `acceptance-v8.json` carries the SHA-256 of its exact text, and all 31 were matched to their rows on 2026-10-16.

## 5. Acceptance test (fixed before any reading)

The expectations come from each case's plain stakes and from the positioning that the evidence and the vendor give each model, not from anyone's pick. Nathan reviews them in this record's pull request before any reading is sent.

### v8

**Part A: 16 cases.** A1 to A12 are v7's Part A texts, unchanged; A13 to A16 are new. No case copies an example from the request. A15 has the same shape as one balanced-model example (a named bug fixed with a test), but it is not a copy of it.

| Case | Rung expected | Model expected |
|---|---|---|
| A1 Record given results | low | Haiku |
| A2 One documented setting | low, medium | Haiku, Sonnet |
| A3 Listed repairs on a reviewed client | high, extra high | Opus, Sonnet |
| A4 Check of a follow-up commit | high, extra high | Opus |
| A5 First look at a large new system | max | Fable |
| A6 First live run on real cards | max | Fable |
| A7 Endpoint-by-endpoint check of 62 endpoints | extra high, max, ultracode | none stated |
| A8 Mechanical conversion of 240 modules | none stated | Haiku, Sonnet |
| A9 A cause that two fixes missed | max | Fable |
| A10 Licence survey of 180 packages | none stated | Haiku, Sonnet |
| A11 Conflicting legal sources (out of frame) | extra high, max | none stated |
| A12 Name suggestions (out of frame) | low, medium | Haiku, Sonnet |
| A13 Locate definitions for a larger session | low, medium | Haiku |
| A14 Route 300 support emails | low, medium | Haiku |
| A15 Named date-picker bug | medium, high | Sonnet |
| A16 Help article for a shipped feature | low, medium, high | Sonnet |

**Gate A** passes when all four hold:
- at least 14 of the 16 cases meet every stated expectation;
- A5, A6 and A9 read Fable 5.1;
- at least 2 of A1, A13 and A14 read Haiku 5.5;
- at least 1 of A15 and A16 reads Sonnet 5.5.

**Part B: Nathan's 31 recorded Glow app picks.**

| Gate | Passes when |
|---|---|
| B_effort | the rung equals his pick on at least 24 of 31, and is within one rung on at least 30 (v6 on the same texts: 26 and 31) |
| B_model | at least 6 of his 9 Fable 5.1 picks read Fable 5.1 (v6: 8); at least 18 of his 22 Opus 5.5 picks read Opus 5.5 or Sonnet 5.5 (v6 read Opus on 19); Haiku 5.5 is read on at most 1 of the 31 |

**Reported, not gated:**
- how many Opus 5.5 picks read Sonnet 5.5. Those picks were made when only two models were offered, so a Sonnet reading is not counted as a disagreement;
- the 9 texts where Nathan overrode the v6 reading he saw.

**Part C:** Part A is read twice, and the differences between runs are reported, not gated.

**Outcome.** v8 is accepted when gates A, B_effort and B_model all pass on run 1. If any fails, one revision (v8.1) is allowed, run on the same cases and marked as fitted to them. If v8.1 also fails, Nathan decides.

### hd-v3

There are eight cases, and all eight must pass, as with hd-v1.

| Case | Rung expected (hd-v1's, unchanged) | Model expected |
|---|---|---|
| HA1 Record a delivered report | low | Haiku, Sonnet |
| HA2 Two named one-line fixes | medium | Sonnet, Opus |
| HA3 Repair four named defects | high, extra high | Opus |
| HA4 First parent-child composite | max | Fable |
| HA5 Claim audit of the first six reports | ultracode | none stated |
| HA6 Standard single-person reading | high, extra high | Opus |
| HA7 Check a run folder against the naming plan (new) | low, medium | Haiku (required) |
| HA8 Handover note from open run items (new) | low, medium | Sonnet, Haiku |

- HA1 to HA6 keep hd-v1's texts and rung expectations. HA3's and HA5's texts share phrases with hd-v1's effort criteria, as they did when hd-v1 was accepted.
- Jobs J0 to J6 are re-read and reported against hd-v1, not gated.
- One revision (hd-v3.1) is allowed, on the same terms as for v8.

## 6. After acceptance

Each step happens only if acceptance passes:

1. **Installable skills.** Build `typesafe-scoring.skill` (v8) and `hd-typesafe-scoring.skill` (hd-v3) and give them to Nathan to install. They are not committed to the repository.
2. **Notion tables.** Add these options to both uses tables (`collection://e1d83c6d-23b7-447f-8bc6-dcbb4829f24e` and `collection://6d7a823b-eb6c-42ed-9d97-93ec1c5306ae`):
   - the 12 Sonnet 5.5 and Haiku 5.5 cells, to *TypeSafe cell* and *Nathan's pick*;
   - "Sonnet 5.5" and "Haiku 5.5", to *TypeSafe model*;
   - v8 or hd-v3, to *Version*.
3. **Notion log pages.** Record the result at the top of both log pages, and mark v6 and hd-v1 as superseded.
4. **HD skill files.** Upload `request-hd-v3.json` and `score_v8.py` to the HD log page, as hd-v1's files were, so that the HD skill can pin and download them.

If acceptance fails, v6 and hd-v1 stay in force, and nothing is changed in Notion or in the skills.

## 7. Limits

- **Model readings are untested against real outcomes.** Nathan's picks never had Sonnet 5.5 or Haiku 5.5 available, so Part B can show no regression but cannot show that the new options are chosen correctly. Part A tests that they are reachable and behave as described.
- **Unequal evidence.** Several new figures are single practitioner tests (CodeRabbit, Bito, AI Dive, Aivio Labs, The SEO Agent), not benchmarks. The texts state their sizes.
- **Mixed measurement points.** Some of the strong and most-capable figures carried over from v6 and hd-v1 (cost per task at the lower rungs, writing tests) were measured in September. The new four-way comparisons use the tables as read on 2026-10-16.
- **Ultracode is unmeasured.** No third-party measurement exists for any of the four models, as recorded for v6.
- **The glow-dating-app record is not updated.** Its reasoning-strength matrix (§6) is outside this session's reach, as recorded for v7.

## Canon relied on

- `AGENTS.md`: the canon-first rule; the closed-rails and evidence-attribution rules.
- HDE Build Notes (PF10) v13.5.8, addendum 2.1, read in full from `main`:
  - the model and reasoning-level guidance is the reading of the installed TypeSafe scoring skill;
  - no agent gives its own recommendation;
  - the Product Owner picks.
  This record changes the scorer at Nathan's direction. It adds no recommendation beside a reading.
- HDE Governance §9.1.3: provider neutrality continues to apply to the model that performs work, per PF10 addendum 2.1, rule 5.
