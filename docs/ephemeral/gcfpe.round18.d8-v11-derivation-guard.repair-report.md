---
artifact_type: GCFPE_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-20
round: 18
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
authority: Product Owner instruction, 2026-09-20
guard_version: v11
supersedes_guard_version: v10
installed_guard_version_at_time_of_writing: v6
change_flow_package_sha256: 72d1da48e1619f365b100761f0e41aeef43123d66ab0b9953efc4ec2fbe4ab01
flowmaster_validate_package_sha256: 9e7e79c87db78bc81dc38299dfc5cdab4213cf2b70a7ddd756be2ca0d65f319f
---

# Round 18 — D8/D15 guard v11, the tenth defeat, and a lossy key function

**Packaged, not installed, and not yet cleared by independent review.** Skills live in a
one-way synced directory; only the Product Owner installs. The installed build at the time of
writing is **v6** — the round-17 package, whose own status line belongs to that package and not
to this one. Three files change from v10.

This report exists so the measurements below are auditable from the repository rather than
asserted in a decision record. It records the tested state, not a later HEAD.

## Environment and method, stated so the run can be repeated

| Item | Value |
|---|---|
| Actor | PE34 (prompt-engineer session), acting on Product Owner instruction |
| Date | 2026-09-20 |
| Reviewer whose findings prompted it | SFR-01, independent reviewer session, v10 attack round |
| Rig | a scratch copy of the frozen synced skills tree with v10's two skills replaced by the packaged copies; nothing executed inside the synced tree |
| Environment pins | `PYTHONDONTWRITEBYTECODE=1`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` |
| Contract edits | applied identically to both contract copies, with the byte pins re-stamped — `EXPECTED_CANDIDATE_CONTRACT_SHA256`, `EXPECTED_CANDIDATE_CONTRACT_BYTES`, and the profile's `candidate_contract.sha256`/`byte_count` — which is the minimum any lawful contract edit requires |
| Synced tree, before and after | 321 files; 320 files and `7a15a24656c380223e5dd72d8dd59a4d3a37303384ea8b799f21c04cca5c0cf4` excluding `manifest.json`, which carries a per-container sync epoch; `.pyc` count 0 |

## The tenth defeat — a failure class the record did not name

v10 was defeated twice by SFR-01, and both defeats were reproduced here before being accepted.
Both sit inside `pf10_addendum_contract`, the one object the guard enumerates exactly.

The root of both is neither a selector nor a waiver but a **lossy key function**: layer 3
compared derived dotted path strings, and the derivation was not injective, so two different
contracts produced the same observed set.

| Placement | Layers | Gates |
|---|---|---|
| top-level key `producers.RS-20` inside the addendum | all silent | all four green |
| `producers.CF-C-30` | all silent | all four green |
| `native_outcome_normalization.PENDING` | all silent | all four green |
| control — same value under `post_approval_divergence_check` | `L3 added:post_approval_divergence_check` | G1 exit 1, G2 `PF10_ADDENDUM_CONTRACT_KEY_DRIFT` |
| prohibited gate appended to `forbidden_fields` | all silent | all four green |

There were 22 dotted paths in the enumeration, so 22 free slots. The only difference between
the caught case and the uncaught one was the dot.

The second placement has the same root: a path was recorded for a list element only when that
element was itself a dict or a list. Every list in the addendum is a list of scalars, so none
of their elements was covered at any depth. Three of the four lists were caught anyway, each
by exactly one unrelated value check — `exact_producer_set` by `PF10_PRODUCER_SET`,
`never_for` by `PF10_NONQUALIFYING_OUTCOMES`, `required_fields` by
`PF10_ADDENDUM_SCHEMA` — which D8's own rule counts as incidental coverage, not enforcement.
`forbidden_fields` had nothing behind it, because its only reader is a superset test.

## What v11 changes — three things

1. A path is a **tuple of typed segments**: dict keys as strings, list indices as integers.
   Injective by construction, with no rejection rule and no vocabulary. The expected
   enumeration stays dotted and greppable and is read into segments at import under an
   assertion that the reading does not collide. A key carrying `.` or `[` is additionally
   reported as `AMBIGUOUS_KEY` — the diagnosis, not the mechanism — and messages render paths
   as JSON arrays so an added and a removed path can never read as the same text.
2. Every list inside the addendum is pinned to its **exact element sequence**, order included,
   under the new code `PF10_ADDENDUM_LIST_VALUE_DRIFT`. `UNENUMERATED_LIST`,
   `MISSING_LIST` and `LIST_VALUE_DRIFT` report distinctly.
3. Both changed checks return `contract:NOT_AN_OBJECT` on a non-dict contract, matching their
   sibling rather than raising.

### A shape rule was proposed, measured, and rejected

SFR-01 recommended requiring every addendum list element to match the bare single-token form
already used for lifecycle values. **Refuted by measurement:** two elements of the *lawful*
`forbidden_fields` are prose — *"any pinned PF document version"* and *"any field describing
this addendum's own drainage state — not a Canon destination, Canon target, or PF09 row"*. That
list describes prohibited content in English, not field names, so the rule fails on the
contract as it stands. That is the ninth defeat's mistake and the removed PF10-token rule's
mistake. Shape is unavailable on this axis, so the values are enumerated instead.

## Measurements — each read from the tool's own top-level flag

| Check | Result |
|---|---|
| Attack placements caught | **13 of 13** |
| — SFR-01's two defeats | `AMBIGUOUS_KEY` + `added:[…]`; `PF10_ADDENDUM_LIST_VALUE_DRIFT` |
| — shapes added this round | nested dotted key, bracket-shaped key, index-collision dict, list reversal, dict-in-list — all caught |
| Earlier defeats still caught | v8 object `NOT_SCALAR:dict` and v9 prose `NOT_TOKEN` on all four lifecycle names; nested addendum clause by layer 3 |
| Lawful promotion control | clean — `L3`, `L4`, `L5` all `[]` with the real lifecycle key names |
| Fail-open sweep | `contract:NOT_AN_OBJECT` on list / None / str / int; `pf10_addendum_contract:NOT_AN_OBJECT` for the inner object |
| Cross-copy parity of the guard block | byte-identical, 8836 chars, `e80529aac5653adfce29fe4c40227fce` |
| Fixture cost | **1 amended expectation in 140** |

## Gates from the packaged tree, each read from the tool's own top-level flag

| Tool | Flag | Result |
|---|---|---|
| `change-flow/validate_gcfpe_20260914.py` | process exit + PASS line | PASS, exit 0 |
| `flowmaster-validate/validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, 140 cases, 0 failing |
| `validate_flowmaster.py` | `verdict` | `FLOWMASTER_SUITE_PASS` |

Re-run from the **extracted** `.skill` packages rather than the build tree: all four green.

## Fixture change — one expectation

`reject-second-pf10-producer` appends to `exact_producer_set`, which now also drifts that
list's element pin, so the case expects `["PF10_ADDENDUM_LIST_VALUE_DRIFT",
"PF10_PRODUCER_SET"]`. The runner already documents and supports an exact multi-code
expectation and has precedent in `reject-pr30-direct-pr40`. Comparison stays exact equality,
so `PF10_PRODUCER_SET` is still required to fire; the case is not weakened. This is the first
change to the runner since v8.

## Swept and deliberately not changed

- The layer-2 branch scan builds paths with the same dotted derivation, but nothing selects on
  that path — it is a label in a report whose emptiness is the only thing tested — so a
  collision there is cosmetic.
- A non-scalar element appended to an addendum list is caught by layer 3 and then reaches the
  pre-existing `TypeError: unhashable type: 'dict'`. Fail-closed, and already recorded.
- Lifecycle values of type `bool`, `int`, `float` or `None` receive no form check. **No
  change:** that value space cannot express a directive, so a rule there buys nothing.

## Files changed — three

| File | sha256 (first 16) |
|---|---|
| `change-flow/scripts/validate_gcfpe_20260914.py` | `660d61fe619c9dd9` |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `535a3b161ef09962` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `433d2a1611e5671a` |

## Limitations

- The validator sources and the fixture runner are **not** in this repository and must not be:
  prompts and skills are never mirrored here. The three sha256 values above are the identity by
  which the packaged copies can be checked against this report.
- Every measurement above was produced on the scratch rig described, in an ephemeral session
  container. The rig is not preserved. What is reproducible from this report is the method, the
  pins, and the identities — not the container.
- v11 has **not** been cleared by independent review. Round 18 does not close the §10 gate; it
  supplies the artifact a tenth review would judge, and only after installation.
- §10 requires an approved skill edit to be made with `skill-creator` and the review to be
  re-run against the final installed snapshot. These edits were authored as working copies
  against a frozen tree because this session cannot install.

## On installation

Only the Product Owner installs, and no skill may be installed while a review is running. If
independent review returns `GUARD_HOLDS`, the packages above are the ones to install; the
installed build until then is v6.
