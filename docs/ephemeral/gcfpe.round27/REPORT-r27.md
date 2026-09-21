---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
authority: Product Owner authorisation 2026-09-21, on SFR-01's four blocking findings against round 26
subject: Round 26's four findings repaired, and the test that would have caught three of them
---

# Round 27 — the corpus requirement actually leaves this time

**Same real prompt body, same command, two packages:**

| package | result |
|---|---|
| round 26 (`2495b235…`, rejected) | `ok: false` — `['ARTIFACT_AVAILABILITY_BODY_SET']` |
| **round 27 (this one)** | **`ok: true` — `validated: ['IA-10']`, `not_evaluated: ['QA_PASS_CLASS_MAP_AND_INTAKES']`** |

`IA-10` was read from Notion, piped in exactly as the Operations Hub procedure prescribes, and
deleted in the same command. That single test demonstrates `F1` and `F2` fixed on real text, and it
is the test round 26 should have run before packaging.

## The four findings, each repaired and falsified

### `F1` — the all-55 requirement had moved, not gone

`validate_artifact_timing_bodies(bodies, *, require_complete=True)` still demanded every
stage-category body, and `require_complete` was passed **nowhere in the package** — two grep hits,
the definition and its own default. Round 26 removed the corpus gate from `validate_prompt_bodies`
and left an identical one a single call away, converting *"the gate will not run"* into *"the run
fails on one body"*, which is worse.

**Repair:** `ARTIFACT_AVAILABILITY_BODY_SET` and the `require_complete` parameter are deleted, for
the same reason `PROMPT_BODY_MEMBER_SET` was. Nothing depended on it: emitted in one place,
expected by no fixture.

### `F2` — the coverage report was silent exactly when coverage was zero

`if bodies:` treated `{}` and `None` alike, though `main()` deliberately distinguishes them. A run
that validated nothing reported `not_evaluated: []` — an assertion that nothing had been skipped.

**Repair:** `None` now reports `ALL_BODY_LEVEL_CHECKS`; `{}` and partial sets report the specific
set-scoped checks. Measured from the extracted package with no bodies offered:
`not_evaluated: ['ALL_BODY_LEVEL_CHECKS']`.

### `F3` — `SKILL.md` still documented the removed flag

Lines 148, 156 and 162 still described a *"required recursively scanned 55-member prompt corpus"*
and `--prompt-dir /exact/.../prompts`, unchanged from the installed tree — the prohibited
instruction, verbatim, in the round that removed the flag.

**Repair:** all three rewritten, and the replacement procedure documented in the same place an
operator looks, including *"a run that validated nothing is not a pass — read those two fields,
never `ok` alone."* The only surviving `--prompt-dir` mentions are the dated prose recording its
removal, which `AUTH-001` preserves.

### `F4` — the post-install gates never checked self-identity

Round 26 put `SKILL_TREE_SHA256` only in the candidate validator. The gates an operator actually
runs after installing both certified a tampered tree.

**Repair and falsification** — one comment appended to one unrelated script:

| gate | round 26 | round 27 |
|---|---|---|
| `validate_flowmaster` | `FLOWMASTER_SUITE_PASS` | **exit 1, `FLOWMASTER_SUITE_FAIL`** |
| `validate_gcfpe_current` | `ok: true` | **exit 1** |
| `validate_gcfpe_20260914` | exit 1 | exit 1 |

All three name the mismatch: `SKILL_SELF_IDENTITY:DECLARED_6f682315a943_MEASURED_5475f5e24c5d`.

### Non-blocking — duplicate declaration lines

The exclusion was a global substitution, so any number of `SKILL_TREE_SHA256:` lines was invisible
to the digest; twenty-one identical lines were accepted silently. Exactly one is now permitted:
`SKILL_SELF_IDENTITY:MULTIPLE_DECLARATIONS:21`.

### `Q1` — the two dormant snapshot validators

`validate_epic_alpha.py` and `validate_strength_middleware.py` each globbed a prompt directory and
gated on `SNAPSHOT_MEMBER_SET` for other prompt sets. **Retired**, per `SFR-01`'s recommendation and
Product Owner authorisation: `--prompts` now returns `PROMPT_SNAPSHOT_DIRECTORY_RETIRED`. Dormant is
not conformant, and leaving them guaranteed a later reviewer would find them.

## A correction to round 26's report

> *"the package is SMALLER than the tree it replaces"*

**False.** Measured 1,764,361 against 1,756,991 — round 26's tree was 7,370 bytes larger, and round
27's is 1,769,023, larger still. `SFR-01`'s figures match this re-measurement exactly. The claim
compared two different things and was not checked before it was published.

## Measured

Scratch copies, `PYTHONDONTWRITEBYTECODE=1`. Base is the installed tree.

| gate | base | work | from the extracted package |
|---|---|---|---|
| candidate validator | exit 0 | exit 0 | exit 0, `ok: true` |
| contract fixtures | 155, 0 failed | 155, 0 failed | 155, 0 failed |
| flowmaster suite | `PASS` | `PASS` | `PASS` |
| `validate_gcfpe_current`, `change-flow` self | exit 0 | exit 0 | exit 0 |
| `validator_revision` | 3.2.9 | **3.2.12** | 3.2.12 |
| self-identity | n/a | OK | **OK** |
| `.pyc` | 0 | 0 | 0 |

## Scope and package

Nine files, all inside `flowmaster-validate`; `change-flow` byte-identical at `14981ba7…`. Diff:
`round27.patch`, 666 lines.

| | files | bytes | sha256 |
|---|---|---|---|
| `flowmaster-validate.skill` | 29 | 284588 | `cb3c628662a19b77b235634c77e2eac0e24e6d304debb8bb15ef573f1c727bfd` |
| baseline — the installed tree | 29 | — | `f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd` |
| repaired tree | 29 | — | `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` |
| `SKILL_TREE_SHA256` | — | — | `6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93` |

Verified path-by-path and digest-by-digest: 29 entries, all identical to the tested tree, none
outside the skill root, nothing unpackaged.

`validator_revision` 3.2.11 → **3.2.12**; `FLOWMASTER_VALIDATE_REVISION` 3.2.13 → **3.2.14**.
`CHANGE_FLOW_SPECIALIZATION_REVISION` stays 3.2.8; the candidate contract stays `1c3c7969…` /
610549 in both copies.

**This package supersedes round 26's `2495b235…`, which was rejected and never installed.** The
installed tree remains round 24's `e8f30b9a…` until the Product Owner installs after §10.

## The process change this round carries

Round 26's report named *"no full per-prompt run against a complete real body"* as its largest
unverified claim and handed that run to the reviewer. The reviewer ran it and it failed
immediately. **Naming a limit is not closing it.** Three of four findings — `F1`, `F2` and `F3` —
would all have surfaced from that one command.

**Standing consequence: the documented procedure is executed end-to-end against real content before
a package is built, not after.** A round that has not run its own published instructions has not
been tested.

## What this does not claim

No QA verdict, no acceptance, no closure, no PF09 movement. Nothing installed, merged or
auto-merged. The selected release `GCFPE-20260913.1 / 091326.2 / 54` is untouched; no prompt body,
registry row or graph part changed; no prompt corpus was written to disk, and the single body used
for the end-to-end test was deleted in the command that used it.
