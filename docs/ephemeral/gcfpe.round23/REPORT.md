---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
subject: SF10-10 — the PF10 roster on the Product Owner's ruling, shipped with SF10-09
---

# Round 23 — `SF10-10`, and the end-to-end validator reaches zero

**The end-to-end validator goes from 4 errors to 0.** Measured on both trees against the complete
55-body corpus, not assumed. Every other gate exits 0 on both trees, no fixture fails, and the
installed tree is byte-identical before and after.

`SF10-09` and `SF10-10` ship together as one round, in two packages that install together.

## The authority for SF10-10 is the Product Owner's ruling

Verbatim, 2026-09-21:

> "no, initial authoring does not require a PF10 built in this addendum. It is an input only, like
> all other pfcanon, but should not be a named input or output for an authoring prompt."

PF10 is one PFCanon source among others, reached through the general PFCanon-resolution rule that
every body already carries. **An authoring prompt must not be required to name PF10 as an input or
an output.** Requiring a CF Specification author's body to state "current controlled PF10 Markdown"
is therefore requiring the wrong thing.

**This is not the exemption `SFR-01`'s R1 rejected.** R1 rejected it because `SF10-07` asserted it
from body quotations without evidence, and the bodies contradicted the assertion. What has changed
is not the reading but the **authority**: the owning authority has settled what an authoring prompt
should *say*. The roster moves on that ruling. It is deliberately **not** re-derived from prompt
bodies, and the error count falling to zero is the consequence of the change, not its justification.

## What changed

| | before | after |
|---|---|---|
| `current_pf10_markdown_required` | 14 writers | **10** — the non-CF writers, matching `active_addenda_required` exactly |
| `authoring_context_required` | 12 | 12 — unchanged |
| `active_addenda_required` | 10 | 10 — unchanged |
| `evaluated_prompt_ids` (`EXPECTED_WRITERS`) | 14 | 14 — unchanged |

The four — `CF-C-20`, `CF-C-40`, `CF-E-20`, `CF-E-40` — keep every other obligation, including
`approved_base_live_reauthoring_refused`, which is the central rule of the `-40` pair's
approved-base mode. This is per-obligation scope, not a smaller writer set.

The roster lives in the **contract**, so unlike `SF10-09` this is a contract change and the hash-pin
chain fires.

| pin | before | after |
|---|---|---|
| candidate contract bytes | 610625 | **610549** |
| candidate contract sha256 | `5d871b5d052f3eba…` | **`1c3c7969b7b93356…`** |

`CONTRACT_HASH` → `PROFILE_BUNDLED_CONTRACT_HASH` → `PROFILE_CONTRACT_PIN`: the file itself, the
validator's `EXPECTED_CANDIDATE_CONTRACT_SHA256` / `_BYTES`, and the validation profile's
`candidate_contract.sha256` / `byte_count`. Both bundled copies of the contract remain
byte-identical to each other — verified, not assumed.

### Revision sites, counted by grep rather than trusted

`CHANGE_FLOW_SPECIALIZATION_REVISION` **3.2.7 → 3.2.8**. The literal `3.2.7` appeared **8** times in
the tree; **6** are mutable sites and **2** are dated prose records that `AUTH-001` forbids
rewriting:

| site | disposition |
|---|---|
| `change-flow/SKILL.md` declaration | → 3.2.8 |
| `change-flow/scripts/validate_gcfpe_20260914.py` | → 3.2.8 |
| `flowmaster-validate/scripts/validate_gcfpe_current.py` ×2 | → 3.2.8 |
| `flowmaster-validate/scripts/validate_flowmaster.py` ×2 | → 3.2.8 |
| `change-flow/SKILL.md` — "…is incremented to 3.2.7." | **preserved**; successor sentence added beside it |
| `flowmaster-validate/SKILL.md` — "`change-flow` … stays at 3.2.7." | **preserved**; successor paragraph added beside it |

Plus the profile's `installed_skill_revisions.change-flow` → `3.2.8`, which a plain digest grep does
not find. That is six mutable sites plus the revision map, and exactly two `3.2.7` occurrences
remain in the tree, both historical.

`FLOWMASTER_VALIDATE_REVISION` **3.2.8 → 3.2.10**, folding in `SF10-09`'s 3.2.9: two repairs, two
recorded increments, one package.

## A fixture stopped testing what it was named for, and the roster change is why

`SFR-01`'s carried question was whether the roster-drift and duplicate-id cases still fire once
`current_pf10_markdown_required` is no longer all fourteen. They still **pass**. One of them had
stopped **discriminating**.

`reject-body-obligation-duplicate-id` appended `"CF-C-20"` to that roster. While the roster held all
fourteen, that produced a genuine duplicate, caught by the length half of the check — the half round
21 added precisely because set equality alone accepted a duplicated id. With the four CF authors
exempt, `"CF-C-20"` is an id from **outside** the roster, so the case now rejects through set
inequality instead, exactly like the drift case beside it. The length branch had no fixture left
firing it.

Measured, not read:

| appended id | set equal after mutation | length differs | what the case tests |
|---|---|---|---|
| `CF-C-20` (old) | **False** | True | set drift — duplicate branch not reached |
| `IA-10` (new) | **True** | True | **duplicate — the length-only branch** |

Falsified on a throwaway copy by removing the length half of the check and re-running the suite:

| fixture points at | cases failing with the length check removed |
|---|---|
| `IA-10` (repaired) | **`reject-body-obligation-duplicate-id`** — the only one |
| `CF-C-20` (as inherited) | **none** |

A guard nobody fires is the defect class this series exists to remove, so the fixture is repointed
at an id the new roster actually holds. `reject-body-obligation-roster-drift` and
`reject-body-obligation-foreign-id` target `active_addenda_required` and `authoring_context_required`,
whose rosters `SF10-10` does not touch; both still fire.

## Measured

Every run from a scratch copy, `PYTHONDONTWRITEBYTECODE=1`. Base is the installed tree; work is base
plus `SF10-09` reapplied from `sf10-09.patch` plus `SF10-10`.

| run | base (installed) | work (repaired) |
|---|---|---|
| **end-to-end, 55 bodies** | exit 1 — **4 errors** | exit 0 — **0 errors** |
| candidate validator | exit 0 — 0 errors | exit 0 — 0 errors |
| contract fixtures | exit 0 — 145 cases, 0 failed | exit 0 — **155 cases**, 0 failed |
| body fixtures | exit 0 — 169 cases, 0 failed | exit 0 — **179 cases**, 0 failed |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current change-flow` | exit 0 | exit 0 |
| `change-flow` self-validator | exit 0 | exit 0 |

The four base errors are exactly `PROMPT_WRITER:{CF-C-20,CF-C-40,CF-E-20,CF-E-40}:CURRENT_PF10_MARKDOWN`
— the same four the handoff records, which is independent confirmation that the re-fetched corpus
reproduces the predecessor's measurement.

Zero `.pyc` written into either tree. The synced skills directory was never written to and is
byte-identical to `base` after every run.

## The corpus was re-fetched, and how

The 55 prompt bodies are authored in Notion in place and are never mirrored into the repository. All
55 were re-fetched from the Notion page ids in the contract's own `notion_page_manifest`, then
written to disk by reading the recorded fetch results back off disk rather than by retyping them, so
the bytes validated are the bytes Notion returned. The extractor is small and is not shipped in
either package; it exists only to rebuild the corpus. One body was transcribed by hand first as a
control and compared byte-for-byte against the extracted copy: identical.

## Two things to flag rather than bury

**1. The handoff's baseline digest is not reproducible, because its recipe was never recorded.**
The installed tree is **318 files**, which matches. The digest `2f5d14a6…` does not reproduce under
ten distinct recipes tried here (path+hash lines sorted several ways, hashes-only, null-separated,
content concatenation, reproducible tar, and two Python hashlib variants). No recipe was recorded in
round 21, round 22, or the handoff, so the value cannot be checked and is **not** claimed as
verified. The baseline was instead confirmed on the substantive facts, each independently
checkable: 318 files; `change-flow` at 3.2.7; `flowmaster-validate` at 3.2.8; `validator_revision`
3.2.7 at exactly four sites; candidate contract `5d871b5d052f3eba…` / 610625 bytes, byte-identical
in both bundled copies; end-to-end exit 1 with those four errors. To end this for the next round,
the recipe is now written down as `freeze.py` beside this report, and its values are:

| tree | files | freeze digest |
|---|---|---|
| installed / base | 318 | `3e84e5cc789578d3690e38fc330b66c45d4a46e2b3c5d9505bb89f8597712945` |
| work | 318 | `ca9bdd1e443c6c094a49b7316c88968088593da7a809e5d7cb2c917bfb6f59b1` |

**2. `validator_revision` stays at 3.2.8, and that is a judgment call worth a reviewer's eye.**
`SF10-09` moved it 3.2.7 → 3.2.8 at its four sites, and the handoff specifies 3.2.7 → 3.2.8 for the
combined round, so this round adds no further bump: one installed validator, one identity. The
counter-argument is real and is not hidden here. Round 22's own rule is that "two behaviours must
not advertise one validator identity", and round 22's report — already on `main` — records fixture
counts of 155/179 against `validator_revision: 3.2.8` produced by `SF10-09`-only bytes, which are
not the bytes shipped now. Those numbers happen to coincide, but the behaviour does not. A reviewer
may reasonably rule that this round should emit **3.2.9** instead. Nothing outside the profile pin
reads the field, all four sites move together, and the change is one line in four places.

## Packages

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242412 | `52d77d970c5eca5dbc89f39a49bcd1b178deeee0ca3d0d8869e1b9193805e337` |
| `flowmaster-validate.skill` | 29 | 277974 | `26a8d4766eb839c86c73df02a59f30395a3036a335a23f35afbd9edb4678a6ab` |

Built with the canonical `skill-creator/scripts/package_skill.py`, copied to scratch and run with
`PYTHONDONTWRITEBYTECODE=1`. Each archive was extracted and compared **path-by-path and
digest-by-digest** against the tested tree: every entry identical, no entry outside the skill root,
no traversal sequences, and no on-disk file left unpackaged.

**Both packages install together.** The revision and the contract move across both, so either alone
leaves a 3.2.8 assertion pointed at a 3.2.7 declaration, or a validator pin pointed at the wrong
contract bytes.

## What this does not claim

No QA verdict, no acceptance, no closure, no PF09 movement. Round 21's `SKILL_FIT_CONFIRMED` is
scoped to the digests it named and **does not carry to these bytes**; this round needs its own §10
from `SFR-01` before anything is installed. Nothing has been installed, merged, or auto-merged.

Prompt bodies are untouched: no body, registry row, or Notion page content changed. The corpus
mutations used for falsification were made to throwaway scratch copies. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` is untouched, and nothing here names `HDE-EPIC040`.

The complete diff from the installed tree is `round23.patch`, 395 lines across 10 files: five from
`SF10-09`, reproduced from `sf10-09.patch`, and the rest from `SF10-10`.
