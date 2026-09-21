---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
supersedes: the round-24 package e8f30b9a…, which was confirmed but never installed
subject: SF10-12 — the body hashes were already recorded; nothing checked them
---

# Round 25 — `SF10-12`, and the round-24 comment correction

**Before this round a corrupted prompt body passed the entire end-to-end gate in silence.**
Measured, not argued: with the new check removed and one byte appended to `IA-30`, the validator
returns **0 errors**. With the check in place it returns exactly one — `PROMPT_BODY_IDENTITY:IA-30`.

That is the limit the independent §10 review of round 24 reported rather than papered over. It
declined to run the 55-body gate because no body hashes were pinned anywhere, so a rebuilt corpus
could be verified by nobody but the session that built it. The reviewer was right, and the fix was
cheaper than anyone had assumed.

## The hashes already existed

The validator computed `prompt_body_sha256`, put it in the output, and **compared it with
nothing**. Meanwhile the approved registry has carried a byte count and a SHA-256 for every one of
the 55 bodies since the consolidated pass recomputed them, under a documented extraction
convention. Two halves of a check that had never been introduced to each other.

| | |
|---|---|
| registry rows carrying both a byte count and a sha256 | **55 of 55** |
| of those, reproducing against the corpus on disk | **55 of 55** |
| cost of deriving the pins | **no prompt body was read into context** — registry on disk → script → profile on disk |

The last line is a constraint the Product Owner set before authorising this work: pin the hashes
only if doing so does not require pulling all 55 bodies through a session. It did not, because the
values were already written down. The verification that they reproduce was a script printing six
numbers.

## What was added

The 55 pins live in `flowmaster-validate/references/…-validation-profile.json` under
`prompt_bodies`, beside `candidate_contract.sha256` — which is already the place where the
validator's expected artifact identities live. **Nothing was added to the candidate contract**, so
the hash-pin chain does not move and `change-flow` does not move with it.

`validate_prompt_bodies` now takes the profile and compares. Three deliberate choices:

- **The profile parameter is required, not optional.** A check that can be skipped is a check that
  will not run.
- **Absent pins are an error**, `PROMPT_BODY_PINS_ABSENT`, not a quiet skip. An unpinned corpus is
  unverifiable and the run should say so.
- **Exactly one trailing newline is stripped before hashing, and nothing else is normalised.** The
  pin is a property of the Notion page, not of the file that happens to hold it: the recorded
  convention is the exact slice between the fetch result's `<content>` markers with no trailing
  newline added, while a file written from that slice normally ends in one. CRLF, stripped
  whitespace and a second blank line are real corruption and still fail. Getting this wrong in the
  other direction is not hypothetical — 24 of 55 `evidence_contract` entries once reproduced only
  with a trailing newline the page does not contain, because the corpus had been assembled by two
  different methods.

## Falsified four ways, on throwaway copies

| experiment | result |
|---|---|
| one byte appended to `IA-30` | `PROMPT_BODY_IDENTITY:IA-30` — **the only error** |
| `QA-120` given a **second** trailing newline | `PROMPT_BODY_IDENTITY:QA-120` — one newline is tolerated, two are not |
| `prompt_bodies` stripped from the profile | `PROMPT_BODY_PINS_ABSENT` — not silence |
| **the check removed, `IA-30` still corrupted** | **0 errors** — which is what the ecosystem did before this round |

The last row is the justification for the whole change, and it is a measurement rather than an
argument.

## The round-24 finding, corrected

`SFR-01` confirmed the round-24 package with one non-blocking finding: the shipped comment on
`reject-source-absent-crd-class-branch` claimed that deleting the row "also trips
`PROMPT_HANDOFF_RECEIVER`" and that the case "isolates the arity branch". Both are false of that
fixture. `PROMPT_HANDOFF_RECEIVER` is emitted only in `validate_prompt_bodies`; the fixture calls
`validate_qa_closure_bodies`, which never emits it. And the case does not isolate the arity branch —
round 24's own falsification showed the mapping half catches absence unaided.

**The cause was carrying a true measurement across contexts.** The `PROMPT_HANDOFF_RECEIVER`
observation came from the end-to-end validator in the `D5` note and was written into a comment
about a different checker, and a conclusion was then drawn from it that the same round's experiment
disproved. `REPORT.md` for round 24 states both correctly; only the shipped bytes were wrong. The
comment now says which checker emits what, and points at
`reject-source-duplicate-crd-class-branch` as the case that does isolate the length half.

## Revisions, and why both move

`validator_revision` **3.2.9 → 3.2.10** at its four sites; `FLOWMASTER_VALIDATE_REVISION`
**3.2.11 → 3.2.12**. Validation behaviour changes, and 3.2.9 and 3.2.11 are bound to the published
§10 verdict naming `e8f30b9a…`. `F1`'s rule was that corrected bytes must not reuse an identity an
installed build already claims; the same hazard applies to an identity a **published verdict**
already describes, which is why both move here although nothing was installed.

`CHANGE_FLOW_SPECIALIZATION_REVISION` stays **3.2.8** and the candidate contract stays
`1c3c7969…` / 610549 bytes in both bundled copies.

## Round 24's package is withdrawn

`e8f30b9a798ce12b0616d54ee6fb99af296bab9f1986cfa6158088a8c3bff872` was confirmed by §10 and
**never installed**. This package supersedes it against the same baseline and carries everything it
carried, with the comment corrected. **Do not install `e8f30b9a…`.** Its §10 verdict stands as the
record of what was reviewed; those bytes are now history.

## Measured

Every run from a scratch copy, `PYTHONDONTWRITEBYTECODE=1`. Base is the installed tree.

| run | base (installed) | work (repaired) |
|---|---|---|
| end-to-end, 55 bodies | exit 0 — 0 errors | exit 0 — **0 errors, now including 55 body-identity comparisons** |
| candidate validator | exit 0 — 0 errors | exit 0 — 0 errors |
| contract fixtures | exit 0 — 155 cases, 0 failed | exit 0 — 155 cases, 0 failed |
| body fixtures | exit 0 — 179 cases, 0 failed | exit 0 — **181 cases**, 0 failed |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current`, `change-flow` self-validator | exit 0 | exit 0 |
| `.pyc` written | 0 | 0 |

The synced skills directory was never written to. The validation profile round-trips under the
canonical convention it already used — `indent=2`, `sort_keys=True`, `ensure_ascii=False`, trailing
newline.

## Scope and package

Five files, all inside `flowmaster-validate`; `change-flow` byte-identical to the installed copy at
`14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2`. Diff: `round25.patch`, 451
lines. This package installs alone.

| | files | bytes | sha256 |
|---|---|---|---|
| `flowmaster-validate.skill` | 29 | 284004 | `7cf4298c43d515c33c8d9fc4b4dc5892e421d39c740b495f8ae42356f3cd231a` |
| baseline — installed `flowmaster-validate` | 29 | — | `5dcb95a992263cc2255c9e324ec3ea28fe2768f97ac7d0bf3f6204c0b50c6220` |
| repaired tree | 29 | — | `90e9d405061c3975884056d067ec595e533c6c35dcc9702bd67bcd4cd58410dc` |

Extracted and compared path-by-path and digest-by-digest against the tested tree: 29 entries, every
one identical, none outside the skill root, no traversal, nothing left unpackaged.

## What the pins do not claim

They record the bodies as extracted on **2026-09-18 and 2026-09-19**, which is what the approved
registry recorded and what this session's corpus reproduces. They are not a fresh fetch. If a body
has changed in Notion since, the check will fire — correctly, as drift — and the profile records
the dates and the convention so the mismatch is diagnosable rather than mysterious. Re-pinning
after an authorised body change is a normal part of that change, not an exception to this check.

No QA verdict, no acceptance, no closure, no PF09 movement. Nothing installed, merged or
auto-merged. The selected release `GCFPE-20260913.1 / 091326.2 / 54` is untouched and no prompt
body, registry row or graph part changed.
