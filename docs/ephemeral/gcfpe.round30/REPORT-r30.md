---
artifact_type: GCFPE_REPAIR_ROUND_REPORT
artifact_version: "1.0"
created_date: 2026-09-22
round: 30
release: GCFPE-20260914.1 / 091426.1 / 55 (SELECTED)
authority: SFR-01 §10 verdict on round 29 — SKILL_REPAIR_REQUIRED
supersedes_packages: rounds 28 and 29
status: PACKAGED_AWAITING_INDEPENDENT_SECTION_10
---

# Round 30 — a rule I broke in the file that states it

`SFR-01` confirmed both round-28 findings fixed, then returned **`SKILL_REPAIR_REQUIRED`** on a new
blocking finding. It is a repeat of round 24's `F1`, and round 24's `F1` is written in
`flowmaster-validate/SKILL.md` four paragraphs above the round-28 narrative I added to that same
file, in both rounds, without applying it.

## R29-F1 — changed behaviour, unchanged identity

Rounds 28 and 29 are **different packages that advertise the same identity**:

| | package sha256 | `FLOWMASTER_VALIDATE_REVISION` | `validator_revision` | tree hash |
|---|---|---|---|---|
| round 28 | `b5f5d3a3…` | 3.2.15 | 3.2.13 | `8ed6d8b0…` |
| round 29 | `423458d9…` | **3.2.15** | **3.2.13** | `740844f0…` |
| **round 30** | `0e00084e…` | **3.2.16** | **3.2.14** | `eb9634d6…` |

They are not merely different, they are **mutually incompatible**: each validator rejects the
other's profile with `PROFILE_CONTRACT_PIN`, because round 29 renamed the field one requires and
the other forbids. Their governance checks additionally differ on fifteen vectors.

**Nothing downstream could tell them apart.** No report emits the tree hash; all three emit
`validator_revision: "3.2.13"` and `self_identity: "OK"`, byte-identical between packages. And
3.2.15 / 3.2.13 is the identity a **published §10 verdict on `main`** — `SFR-01`'s round-28
`SKILL_REPAIR_REQUIRED` — records its measurements against.

The rule, from `SKILL.md`, raised by the §10 review of round 23 and *"accepted without argument"*:

> round 23 shipped `SF10-09`'s validation behaviour while still emitting `validator_revision:
> 3.2.8` … **The counts coincided and that coincidence was the hazard** … Because 3.2.10 is
> installed and bound to a published §10 verdict, **corrected bytes must not reuse it.**

Both clauses violated. `validator_revision` moves to **3.2.14** at its four sites;
`FLOWMASTER_VALIDATE_REVISION` to **3.2.16**; and a round-29/30 narrative paragraph is added,
which round 29 also omitted.

**§8f asked the reviewer to confirm the revisions were unchanged. They were. The confirmation is
what surfaced it** — an instruction to check that a thing did not move, answered honestly, found
the defect.

## R29-F2 — what the prefix strip still let through

Round 29 stripped a *lead-in prefix*. That caught `- **Lifecycle:** X` but not
**`**Lifecycle**: X`** — bolding the *label* rather than the *field* moves the colon outside the
emphasis, and which form an editor produces depends on nothing but where the selection ended.
`SFR-01` flagged it in round 29's own §6 A1 as suspected-and-unfixed; it is fixed here, with the
neighbours it travels with.

Emphasis and code marks are now removed from the whole line **before** the list, quote and heading
lead-in is stripped.

| now caught, previously not | |
|---|---|
| `**Lifecycle**: X` | bold label, colon outside |
| `*Selection status*: X` · `***Lifecycle***: X` · `~~Lifecycle~~: X` | italic, nested, strikethrough |
| `1. Lifecycle: X` · `2) Selection status: X` | ordered lists |
| `## Lifecycle: X` | headings |
| `` `Lifecycle:` X `` | code spans |
| `\| Lifecycle: \| X \|` | table cells |
| `> > Selection status: X` | nested quotes |
| `Note: <authority line>` | authority line mid-sentence |

**21 of 21 vectors caught. 7 of 7 false-positive controls still pass**, including
`## Selection and authority`, `- Resolve selection only from the … Register.` and
`The register determines selected lifecycle for every member.`

**The fixtures were the reason this survived twice.** Round 28's suite tested only undecorated
input; round 29's tested only the shapes I had already thought of. Eight cases are added for the
shapes above, and the prose control gains three lines. **172 cases**, up from 164.

## Identities

`change-flow` is **byte-identical to rounds 28 and 29** — `ed7041c0…`, verified by `cmp`. Every
change in this round is in `flowmaster-validate`.

| artifact | round 29 | round 30 |
|---|---|---|
| `flowmaster-validate.skill` | `423458d9…` / 286739 | `0e00084e…` / 288056 |
| `flowmaster-validate` freeze | `5da1c46b…` | `b9ca212a…` |
| `SKILL_TREE_SHA256` | `740844f0…` | `eb9634d6…` |
| `FLOWMASTER_VALIDATE_REVISION` | 3.2.15 | **3.2.16** |
| `validator_revision` | 3.2.13 | **3.2.14** |
| fixture cases | 164 | **172** |

Contracts, graph, `change-flow` and `CHANGE_FLOW_SPECIALIZATION_REVISION` (3.2.9) are untouched:
contract `2b78f877…` / 606657, graph `90021eb7…` / 569835.

## Gates, from the extracted package contents, full sibling tree

| gate | flag | result |
|---|---|---|
| `validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, **172 cases** |
| `validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK` |
| `validate_gcfpe_current.py` | `ok` | `true`, `errors: []` |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` |

Zero `.pyc` in the synced directory.

## What `SFR-01` confirmed, and what it found that I had not claimed

Both round-28 findings verified fixed by falsification in both directions. Two results were
better than my report claimed, and I did not know either:

- **F2** — I asserted the rename made the claim true as history. `SFR-01` additionally added
  `selection_status_current: "SELECTED_PRODUCTION"` and the gate **accepted** it. In round 28,
  stating that same truth broke the gate. The trap is gone, not merely relabelled.
- **F1** — the correction catches six vectors neither of us listed: NBSP, `***`, italics,
  combined decorations, nested quotes, four-space indent.

It also answered `A2` by looking: **twelve real lines from seven bodies, including
`## Selection and authority`, zero false positives.** That is direct corpus evidence I had asked
for and not obtained.

## Still open, unchanged

`AF-004` — 42 of 55 bodies have never been scanned for a decorated governance line — remains
deferred to the next `GCFPE-MGMT-10` run by Product Owner decision, 2026-09-21. Round 30 widens
what such a scan would catch, which makes the deferred item more valuable, not less.
