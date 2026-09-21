---
artifact_type: PROMPT_ECOSYSTEM_POST_INSTALL_RECORD
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: INSTALLED_AND_VALIDATED_TWO_FINDINGS_OPEN
subject: Round 23 — §10 verdict, installation, post-install validation, and the two findings
supersedes: nothing; this is a successor record to REPORT.md, which is not corrected in place
---

# Round 23 — successor record: installed, validated, two findings

`REPORT.md` is a dated record and is not edited. This is its successor, per `AUTH-001`. Every
claim in `REPORT.md` stands as written except the two the §10 review corrected, both named below.

## 1. §10 verdict — `SKILL_FIT_CONFIRMED` with findings

`SFR-01`, independent, scoped to exactly these digests:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242412 | `52d77d970c5eca5dbc89f39a49bcd1b178deeee0ca3d0d8869e1b9193805e337` |
| `flowmaster-validate.skill` | 29 | 277974 | `26a8d4766eb839c86c73df02a59f30395a3036a335a23f35afbd9edb4678a6ab` |

Verdict: **the repair is sound and faithful to the Product Owner's ruling.** Two findings, neither
blocking installation.

Reproduced by the reviewer from the bytes, not from the report: package digests, counts and sizes;
single skill root with no traversal and no absolute entries; scope — installed tree plus
`round23.patch` is byte-identical to both packages, 50 files, nothing unaccounted, and the 307
untouched files identical base against work; the ten-writer roster equal to `active_addenda_required`
with `authoring_context_required` at twelve and `evaluated_prompt_ids` at fourteen, both bundled
contract copies byte-identical and canonical-JSON round-tripping; the validator constants agreeing
with the contract on all three obligations; the hash-pin chain agreeing at file, validator and
profile on `1c3c7969b7b93356…` / 610549; six mutable revision sites plus the profile map, with the
two remaining `3.2.7` occurrences confirmed as preserved dated prose rather than missed sites; and
the repointed fixture's falsification reproduced in both directions.

**Gate coverage, stated exactly.** `SFR-01` did not run the end-to-end 55-body gate or the 179 body
fixtures and did not rebuild the corpus. It established the substantive claim by a different route —
loading the shipped validator and running `states_current_pf10_markdown` against writer bodies read
from Notion returns `False` for all four CF authors and `True` for all ten non-CF writers. That
independently confirms the roster change has exactly the claimed effect; it is **not** confirmation
of the full run's exit code. `REPORT.md`'s "end-to-end 0 errors" therefore rested on PE35's
measurement alone at the time of review. It is now confirmed post-install in §3 below.

## 2. Installation

Both packages were installed by the Product Owner after the verdict. Verified from the installed
tree rather than reported:

| | |
|---|---|
| installed skill content | **317 files, `2fa5b8489acd0b7363199ee552157867de2b8c30371f35992b55fb6220b14d07`** |
| identical to | the work tree the packages were built from — same digest |
| `CHANGE_FLOW_SPECIALIZATION_REVISION` | 3.2.8 |
| `FLOWMASTER_VALIDATE_REVISION` | 3.2.10 |
| candidate contract | `1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` / 610549 bytes |
| `validator_revision` | 3.2.8 — **F1 applies here; see §4** |

`REPORT.md` says "Nothing has been installed, merged, or auto-merged." That was true when written
and is now superseded by this section. Nothing was merged and no auto-merge was enabled; the change
reached the installed tree by the Product Owner's own install action, which is the only permitted
route.

## 3. Post-install validation — PASS

Run against the **final installed snapshot**, per the Ops Hub GCFPE tie-in, from a scratch copy with
`PYTHONDONTWRITEBYTECODE=1`. The synced directory was never written to and still holds 318 files
with zero `.pyc`.

| gate | result |
|---|---|
| end-to-end, 55 bodies | exit 0 — **0 errors** |
| candidate validator | exit 0 — 0 errors |
| contract fixtures | exit 0 — 155 cases, 0 failed |
| body fixtures | exit 0 — 179 cases, 0 failed |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current change-flow` | exit 0 |
| `change-flow` self-validator | exit 0 |

This closes the coverage gap in §1: the end-to-end gate the reviewer could not run is now measured
at 0 errors against the installed bytes.

## 4. F1 — `validator_revision` should be 3.2.9 — ACCEPTED, NOT YET APPLIED

The reviewer ruled on the question this round deliberately put to it. **The ruling is accepted
without argument.**

A recorded identity denotes a *behaviour*, not whatever happened to be installed. Round 22's report
is on `main` and asserts 155/179 against `validator_revision: 3.2.8` produced by SF10-09-only bytes;
the installed bytes have different validation behaviour. The counts coincide, and that coincidence
is the hazard — a later reader reconciling the two records finds agreement and concludes the bytes
match. PE35 applied "two repairs, two recorded increments" to `FLOWMASTER_VALIDATE_REVISION` and
then declined to apply the same rule one line later. That inconsistency was PE35's.

**Scope, measured:** four sites, all inside `flowmaster-validate`, none in the candidate contract.

| site | change |
|---|---|
| `references/gcfpe-20260914.1-091426.1-validation-profile.json:45` | `3.2.8` → `3.2.9` |
| `scripts/run_gcfpe_20260914_fixtures.py:629` | `3.2.8` → `3.2.9` |
| `scripts/validate_gcfpe_20260914.py:1063` | `3.2.8` → `3.2.9` |
| `scripts/validate_flowmaster.py:1223` | `3.2.8` → `3.2.9` |

All four move together — the validator checks the profile's value for equality. The hash-pin chain
does **not** move again, because `validator_revision` is not in the contract. `change-flow` is
untouched, so `change-flow.skill` stays byte-identical at `52d77d97…` and its confirmation carries;
only `flowmaster-validate.skill` would need fresh bytes and a fresh §10.

**Consequence now that 3.2.10 is installed.** `FLOWMASTER_VALIDATE_REVISION` must move to **3.2.11**
in the same change. 3.2.10 is installed and is bound to a published §10 verdict naming
`26a8d476…`; corrected bytes that still called themselves 3.2.10 would put two behaviours behind one
installed identity, which is the exact hazard F1 names. When PE35 raised this question it was
genuinely open because nothing was installed; installation settles it.

**Not applied in this round, deliberately.** F1 is non-blocking and costs a full cycle — new
package, Product Owner install, fresh independent §10 — to correct one recorded string. The Ops Hub
rule is explicit that separate one-line fixes each cost an independent review while one change
carrying several costs one. F1 is therefore **carried to the next substantive round**, with its
exact edit already specified above so no analysis is repeated. Owner: the next PE session. It
blocks nothing.

## 5. F2 — the freeze recipe was not reproducible — ACCEPTED AND FIXED

**The finding is correct and is the more serious of the two.** `freeze.py` was introduced in this
round to end the unreproducible-digest problem, and reproduced that problem exactly: rooted at the
skill tree, it hashed `manifest.json`, which carries a `lastUpdated` epoch the sync layer rewrites.
The digests `REPORT.md` publishes — 318-file `3e84e5cc…` and `ca9bdd1e…` — are therefore
per-container, per-sync values, not identities.

Falsified here, not merely accepted on report. `manifest.json`'s `lastUpdated` moved three times
inside this one session — `1789960888158`, `1789962416175` when the reviewer read it, `1789964477235`
— and the installed tree under the published recipe now returns `2c05251d…`, which is neither value
`REPORT.md` printed.

**Correction applied:** `freeze.py` now excludes sync-layer bookkeeping from the walk. The digest
covers skill content and never the machinery that delivers it.

| tree | files hashed | digest |
|---|---|---|
| base, pre-round-23 | 317 | `66a0b5504166416b0386b591e65c4e277ea62de7e5c7d9a81343fa9adb2e4a2f` |
| round-23 repaired, and the installed tree | 317 | `2fa5b8489acd0b7363199ee552157867de2b8c30371f35992b55fb6220b14d07` |

Both reproduce the reviewer's independently computed values exactly, and both are stable across
re-runs. The tree is still 318 files; the digest covers 317, excluding `manifest.json`.

Every substantive baseline fact in `REPORT.md` verified unchanged under the corrected recipe and was
independently confirmed by the reviewer: 318 files, `change-flow` 3.2.7, `flowmaster-validate` 3.2.8,
`validator_revision` 3.2.7 at exactly four sites, contract `5d871b5d…` / 610625 byte-identical in
both copies.

This fix touches the repository only. No skill byte changes, so no package and no review cycle.

## 6. Standing

Round 23 is **installed and post-install validated**. F2 is closed. F1 is accepted, specified, and
carried to the next substantive round as a non-blocking correction. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` is untouched, prompt bodies and registry rows are unchanged, and
nothing has been merged.
