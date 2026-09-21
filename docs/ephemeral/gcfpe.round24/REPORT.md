---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
subject: F1 and SF10-11 — the validator's recorded identity, and the class-map branches nothing fired
---

# Round 24 — `F1` and `SF10-11`, one package

**Two carried corrections, shipped together because separate one-line fixes each cost an
independent review.** `change-flow` is byte-identical to the installed tree, so
`change-flow.skill` at `52d77d97…` keeps its round-23 confirmation and only
`flowmaster-validate` needs fresh bytes and a fresh §10.

Nothing is installed. No prompt body, registry row, graph part or contract changed. The
hash-pin chain does not move.

## `F1` — the validator was advertising an identity that was not its own

Raised by `SFR-01`'s §10 review of round 23 and accepted without argument. Round 23 shipped
`SF10-09`'s validation behaviour while still emitting `validator_revision: 3.2.8` — the identity
round 22's report, already on `main`, records measurements against, produced by `SF10-09`-only
bytes. The fixture counts coincided, and that coincidence was the hazard: a later reader
reconciling the two records finds agreement and concludes the bytes match.

| site | change |
|---|---|
| `references/gcfpe-20260914.1-091426.1-validation-profile.json` | `3.2.8` → **3.2.9** |
| `scripts/run_gcfpe_20260914_fixtures.py` | `3.2.8` → **3.2.9** |
| `scripts/validate_gcfpe_20260914.py` | `3.2.8` → **3.2.9** |
| `scripts/validate_flowmaster.py` | `3.2.8` → **3.2.9** |

All four move together — the validator checks the profile's value for equality. Counted by grep,
not from the round-23 list: `validator_revision` appears at exactly four sites and all four are
inside `flowmaster-validate`.

`FLOWMASTER_VALIDATE_REVISION` **3.2.10 → 3.2.11** in the same change, at its one mutable site.
3.2.10 is installed and bound to a published §10 verdict naming `26a8d476…`; corrected bytes that
still called themselves 3.2.10 would put two behaviours behind one installed identity, which is
the exact hazard `F1` names. The prose recording round 23's increment to 3.2.10 is preserved and a
successor paragraph added beside it (`AUTH-001`).

`CHANGE_FLOW_SPECIALIZATION_REVISION` stays at **3.2.8** at all six mutable sites and in the
profile's revision map, because `change-flow` does not change.

## `SF10-11` — both halves of the class-map guard now have a fixture that uniquely fires them

`D5`'s closure note recorded that no fixture exercised an **absent** CRD branch in `QA-120`'s
PASS class map: the fixture renamed in round 21 tests a *retargeted* destination, and the old
name advertised coverage that did not exist. Closing that gap by measurement found a second,
sharper one.

The guard is `if len(rows) != 2 or {r[0]: r[1] for r in rows} != expected`. Two fixtures are
added, and falsification on throwaway copies decides what each one is worth:

| the guard, with… | cases that stop firing |
|---|---|
| the **mapping** half removed | `reject-source-epic-to-crd` — the only one |
| the **length** half removed | `reject-source-duplicate-crd-class-branch` — the only one |
| the whole guard removed | all four class-map cases, including both new ones |

**The absence case alone was not enough, and that is the finding.** With only
`reject-source-absent-crd-class-branch` added, removing the length half broke nothing: absence
drops the row count to one *and* breaks the mapping, so the mapping half catches it on its own.
The length half still had nothing firing it — the same shape as the contract-side duplicate case
round 23 repointed, and the same reason round 21 added a length check there in the first place.

A **duplicated** CRD row is the case only length can catch: the mapping stays exactly equal
because the dict collapses the repeat, and the count moves to three. That fixture is added too.

Two design choices, stated because a reviewer should test them:

- **The absence case deletes only the class cell, not the whole row.** Deleting the row also
  trips `PROMPT_HANDOFF_RECEIVER:QA-120:CL-C-10` in the end-to-end validator, and a fixture that
  fires two guards cannot prove which one caught it. Removing the cell leaves the `CL-C-10`
  mention in place, so the observed error is exactly `['QA_PASS_BODY_CLASS_MAP']`.
- **The duplicate case locates the row by line scan, not by `QA_PASS_ROW_HTML_RE`.** A fixture
  that builds its mutation with the same regex the check uses cannot fail when that regex is
  wrong — which is precisely the failure this suite has already hit once, recorded in the comment
  above the fixture list.

## Measured

Every run from a scratch copy, `PYTHONDONTWRITEBYTECODE=1`. Base is the installed tree.

| run | base (installed) | work (repaired) |
|---|---|---|
| end-to-end, 55 bodies | exit 0 — 0 errors | exit 0 — 0 errors |
| candidate validator | exit 0 — 0 errors | exit 0 — 0 errors |
| contract fixtures | exit 0 — 155 cases, 0 failed | exit 0 — 155 cases, 0 failed |
| body fixtures | exit 0 — 179 cases, 0 failed | exit 0 — **181 cases**, 0 failed |
| `qa_closure_source_case_count` | 7 | **9** |
| `validator_revision` emitted | 3.2.8 | **3.2.9** |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current change-flow` | exit 0 | exit 0 |
| `change-flow` self-validator | exit 0 | exit 0 |

Zero `.pyc` written into either tree. The synced skills directory was never written to.

**The hash-pin chain is unmoved and was re-derived, not copied:** the candidate contract is
`1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` / 610549 bytes, byte-identical
in both bundled copies, and the validator's `EXPECTED_CANDIDATE_CONTRACT_SHA256` / `_BYTES` and
the profile's `candidate_contract.sha256` / `byte_count` all agree with the file itself.
`validator_revision` is not in the contract, so nothing downstream of it moves.

## Scope

Five files, all inside `flowmaster-validate`:

    SKILL.md
    references/gcfpe-20260914.1-091426.1-validation-profile.json
    scripts/run_gcfpe_20260914_fixtures.py
    scripts/validate_flowmaster.py
    scripts/validate_gcfpe_20260914.py

`change-flow` is byte-identical base to work — 21 files,
`14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` — and equal to the installed
copy. The complete diff is `round24.patch`, 135 lines across those five files.

## Package

| package | files | bytes | sha256 |
|---|---|---|---|
| `flowmaster-validate.skill` | 29 | 279481 | `e8f30b9a798ce12b0616d54ee6fb99af296bab9f1986cfa6158088a8c3bff872` |

Built with the canonical `skill-creator/scripts/package_skill.py` from a scratch copy with
`PYTHONDONTWRITEBYTECODE=1`. The archive was extracted and compared **path-by-path and
digest-by-digest** against the tested tree: 29 entries, every one identical, none outside the
skill root, no traversal sequences, nothing on disk left unpackaged.

**This package installs alone.** `change-flow` does not move, so `change-flow.skill` at
`52d77d970c5eca5dbc89f39a49bcd1b178deeee0ca3d0d8869e1b9193805e337` stays installed as it is.

## A correction to the freeze recipe's scope, found by using it

`freeze.py` was introduced in round 23 rooted at the **synced tree**, and round 23's records
publish whole-tree digests. Between round 23 and this round the tree's digest moved from
`2fa5b848…` to `c607cedc…` with nothing of ours touched: the sync layer updated
`built-in-browser/SKILL.md`, an unrelated Anthropic skill.

A whole-tree digest is therefore a **tree** identity, not a per-skill one, and it is hostage to
skills this project does not own. The claim a repair round needs is per-skill, and the recipe
produces it unchanged when rooted at a skill directory:

| tree | files | digest |
|---|---|---|
| `change-flow` — base, work and installed, all three | 21 | `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` |
| `flowmaster-validate` — base, equal to installed | 29 | `5dcb95a992263cc2255c9e324ec3ea28fe2768f97ac7d0bf3f6204c0b50c6220` |
| `flowmaster-validate` — repaired | 29 | `f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd` |

**Round 23's whole-tree values are not wrong; they are scoped to a tree that includes skills this
project does not control.** Per-skill digests are what later rounds should quote, and the script
needs no change to produce them — only the root does.

## What this does not claim

No QA verdict, no acceptance, no closure, no PF09 movement. Round 23's `SKILL_FIT_CONFIRMED` is
scoped to the digests it named and **does not carry to these bytes**. Nothing has been installed,
merged, or auto-merged. The selected release `GCFPE-20260913.1 / 091326.2 / 54` is untouched,
prompt bodies and registry rows are unchanged, and nothing here names `HDE-EPIC040`.
