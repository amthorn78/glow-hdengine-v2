---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE34
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
subject: SF10-09 — re-encode CURRENT_PF10_MARKDOWN as the two claims it makes; the four errors survive
---

# Round 22 — `SF10-09`, and the four errors are now attributable

`SFR-01` carried one item forward from the round-21 §10: `CURRENT_PF10_MARKDOWN` was **narrower than
the obligation it encodes**, so the four remaining end-to-end errors could not be attributed to the
prompt bodies on that check's word. This round re-encodes the predicate and re-measures.

**The four errors survive, and they are now attributable.** The count is unchanged at 4 — but it is
unchanged for a principled reason rather than a string match, which is the whole point of the round.

## The defect was in both directions at once

The old predicate tested two hard-coded contiguous strings:

```python
"current controlled pf10 markdown" in lower
or ("current controlled pf10" in lower and "controlled markdown" in lower)
```

**Too strict.** Any word between "PF10" and "Markdown" defeated the first form. `SFR-01` showed
"the current controlled PF10 build notes in Markdown" raising; re-measured here, so does the
document's own title:

| phrasing | old |
|---|---|
| "Read the current controlled PF10 Markdown before authoring." | accepts |
| "the current controlled PF10 build notes in Markdown" | **raises** |
| "Resolve the current controlled PF10 — HDE Build Notes in Markdown." | **raises** |
| "Work from the Markdown copy of the current controlled PF10." | **raises** |

**Too loose, and this half was not in the finding.** The second form accepted its two substrings
from *anywhere* in a body. A prompt could satisfy it with "current controlled PF10" in one section
and an unrelated "controlled Markdown" many paragraphs away — components from sentences that never
meet.

## The encoding

The obligation is now tested as the **two claims it actually makes**, each in proximity:

- **identity** — the PF10 object is identified as current and controlled: `pf10`, `current`,
  `controlled` within 30 words of one another.
- **source** — the controlled-Markdown source rule is stated: `controlled` and `markdown` within
  the same span, anywhere in the body.

The source rule is checked body-wide on purpose. A body may legitimately **factor** it into its
general PFCanon-resolution sentence instead of restating it beside PF10 — and `IA-40` does exactly
that. My first attempt required all four components in one window, which **raised on `IA-40`**: a
regression found by measurement before shipping, not by reading. The two-claim form keeps it.

This is **not** a widening of the predicate until bodies pass. That act was refused in round 21 and
stays refused. The evidence that it is not: **no body verdict changes.**

| | old | new |
|---|---|---|
| writers raising, 55-body corpus | 4 | **4** |
| which writers | CF-C-20, CF-C-40, CF-E-20, CF-E-40 | **the same four** |
| other ten writers | pass | **pass** |

Span sensitivity: identical verdicts for all fourteen writers at **every span from 10 to 200 words**,
so the window does not drive the result. 30 is about one long sentence in this corpus.

## Why the four raise — attribution on evidence

All four bodies carry the same source-rule sentence, and it is not the problem:

> "When a PFCanon source is necessary, resolve and read only the **unique controlled Markdown**
> source from `docs/pfcanon/`"

The **identity** claim is what is missing. Their PF10 mentions never place `current` and `controlled`
near `PF10`:

- `CF-C-40` / `CF-E-40`: "retain **current PF10**/overlay evidence only when the branch relies on
  it" — current, but not controlled, and conditional.
- `CF-C-20` / `CF-E-20`: "Initial authoring does not make **PF10** a universal prerequisite."

So the four raise because their bodies do not state the obligation, not because a string failed to
match. **`SFR-01`'s carried-forward item is discharged: the attribution to bodies is established.**

## The falsification that mattered, and the one that failed first

A synthetic phrasing table is not proof on real bodies, so I mutated `IA-10` — a passing writer —
into the lawful interposed form and ran both trees.

**The first attempt did not discriminate: both trees accepted.** The reason is worth recording. The
old check's strictness defect is **masked by its own looseness defect**: `IA-10` still carried the
generic "controlled Markdown" sentence, which satisfies the loose second form. **53 of the 55 bodies
carry that sentence**, so on this corpus the old predicate could not actually produce a false raise.
F1 was a real predicate defect with **no active effect today** — latent, not firing.

Removing that escape hatch as well produces a genuine corpus-level falsification:

| tree | errors | `IA-10` |
|---|---|---|
| base | **5** | `PROMPT_WRITER:IA-10:CURRENT_PF10_MARKDOWN` |
| work | **4** | accepted |

A real body that lawfully states the obligation raises on the old code and passes on the new.

## Fixtures — ten cases, and an honest account of which ones fire

The predicate is a pure function of body text, so the cases run **without the corpus**, in the
contract suite rather than only under `--prompt-dir`.

| | cases | fails on old code |
|---|---|---|
| accepts a lawful phrasing | 6 | **3** — interposed word, document title, Markdown-before-identity |
| raises on a defective one | 4 | 0 |

**Three of ten discriminate**; the other seven agree under both encodings. The four negatives are
kept deliberately: they pin the predicate's ability to **still fail** — missing currency, missing
control, missing source rule, and identity terms dispersed beyond the span. A repair that quietly
became a check accepting anything would pass a suite of positives alone, and a guard that cannot
fire is the defect class this series exists to remove.

## Measured

| run | base (installed) | work (repaired) |
|---|---|---|
| E2E, 55 bodies | exit 1 — 4 errors | exit 1 — **4 errors, same four** |
| contract fixtures | exit 0 — 145 cases | exit 0 — **155 cases**, 0 failed |
| body fixtures | exit 0 — 169 cases | exit 0 — **179 cases**, 0 failed |
| candidate validator | exit 0, 0 errors | exit 0, 0 errors |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current change-flow` | exit 0 | exit 0 |
| `change-flow` validator | exit 0 | exit 0 |

Zero `.pyc` written into either tree. Every run from a scratch copy; the installed tree was never
written to.

## Scope and revisions

**Only `flowmaster-validate` changes** — 5 files. `change-flow` is **byte-identical**, as are the
other 24 skills and `manifest.json`, so **one package installs this round** and `change-flow` stays
at `3.2.7`. The candidate contract is **unchanged**, so no hash-pin chain moves: `5d871b5d052f3eba…`
/ 610625 bytes still agrees with the validator pin, the profile pin and the file.

`FLOWMASTER_VALIDATE_REVISION` **3.2.8 → 3.2.9**, one site. The sentence recording why 3.2.8 was
incremented is **not rewritten**; a successor sentence is added beside it, per `AUTH-001`.
`validator_revision` **3.2.7 → 3.2.8** at its four sites — three scripts and the validation profile —
because the validator's behaviour changes and two behaviours must not advertise one validator
identity. Nothing reads that field for equality; it is a recorded value, and all four move together.

## Package

| package | files | bytes | sha256 |
|---|---|---|---|
| `flowmaster-validate.skill` | 29 | 277007 | `d5228e093dc871dae30a5f6d94afc36dc3aeeff6cc74fff9af6ef3e9283e3ee4` |

Extracted and compared path-by-path and digest-by-digest against the tested tree: **identical, 29
entries, none outside the skill root, no traversal sequences.**

## What this does not claim

No QA verdict, no acceptance, no closure, no PF09 movement. The round-21 `SKILL_FIT_CONFIRMED` is
scoped to the two digests it named and **does not carry to these bytes** — this package needs its own
§10. The complete diff is `sf10-09.patch`, 216 lines.

Prompt bodies are untouched: no body, registry row, or Notion page changed. The corpus mutations
above were made to throwaway scratch copies. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` is untouched.

## Carried forward — a roster question, not a predicate question

Reading the four bodies for this round surfaced something the predicate work does not settle, and it
is recorded rather than acted on. **`CF-C-20` and `CF-E-20` state "Initial authoring does not make
PF10 a universal prerequisite."** That is a body-level declaration that they do not owe the
obligation — the substantiated exemption that round 21's R1 correctly rejected for lack of evidence.

It is deliberately **not** applied here. Changing a roster on the strength of bodies only I can read
is precisely the pattern R1 raised, and this round is scoped to the predicate. It is put to the
Product Owner and to independent review as the next decision, with the quotation attached. The
`-40` pair is a different case and stays on the roster: their bodies consume current PF10
conditionally.
