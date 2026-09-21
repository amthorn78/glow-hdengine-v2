---
artifact_type: GCFPE_REPAIR_ROUND_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
round: 29
release: GCFPE-20260914.1 / 091426.1 / 55 (SELECTED)
authority: SFR-01 §10 verdict on round 28 — SKILL_REPAIR_REQUIRED
supersedes_packages: round 28 (ed7041c0… / b5f5d3a3…)
status: PACKAGED_AWAITING_INDEPENDENT_SECTION_10
---

# Round 29 — the two blocking findings from `SFR-01`

`SFR-01` returned **`SKILL_REPAIR_REQUIRED`** against the round-28 packages with two blocking
findings. Both were mine. Both are fixed here, by the corrections the reviewer specified and
verified.

Nothing from round 28 was installed.

## F1 — decoration walked through the check

`prompt_body_governance_state` matched `startswith` against lines that were filtered for blankness
but never **stripped**, and matched the authority line by exact list membership. So every one of
these said the same thing to a reader and nothing to the check:

| vector | round 28 | round 29 |
|---|---|---|
| `Lifecycle: …` | caught | caught |
| `   Lifecycle: …` (leading spaces) | **evades** | caught |
| `\tSelection status: …` (tab) | **evades** | caught |
| `**Lifecycle:** …` (bold) | **evades** | caught |
| `- Selection status: …` (bullet) | **evades** | caught |
| `> Lifecycle: …` (block quote) | **evades** | caught |
| `  - **Selection status:** …` | **evades** | caught |
| `**<authority line>**` | **evades** | caught |

Bold and bullets are not exotic in this corpus — Notion's editor produces them from ordinary use.

**The sharper half, and the reason this was blocking.** The *old* validator's
`len(status_lines) == 1` collected lines the same unstripped way. That count was the sole support
for round 28's A1 proof that all 55 bodies are clean. **A blind spot in the evidence, not just in
the new check.** The proof holds only for undecorated, unindented lines — and I presented it
without that qualification.

Fixed by stripping leading whitespace and Markdown lead-in before matching, and by testing the
authority line as a substring of the stripped line rather than by equality. Nine vectors verified
caught; a control confirms ordinary prose that merely *discusses* lifecycle or selection is not a
false positive, which matters because several bodies instruct the reader to resolve lifecycle from
the register — the policy being obeyed, not broken.

**The fixtures were part of the defect.** Every case in the round-28 suite used undecorated input,
which is why they all passed while the check was porous. Seven decorated vectors and one prose
control are added: **164 cases**, up from 156.

## F2 — the profile asserted a falsehood about the contract it pins

`candidate_contract` in the validation profile pins the **promoted** contract — `sha256`
`2b78f877…`, `byte_count` 606657, both updated in round 28 — while still declaring
`"selection_status": "UNSELECTED_CANDIDATE"`. The contract it pins declares `SELECTED_PRODUCTION`.
And `load_profile` did not merely tolerate the stale value: it **required** it, so correcting the
profile to the truth failed the gate.

**This is the same trap as coupled defects 1 and 3 — a selection value pinned to a literal with no
production branch — surviving in a fourth site.** I fixed three instances, disclosed three
cosmetic leftovers as Q1/Q2/Q3, and missed the one that was load-bearing.

Fixed by renaming to `selection_status_during_staging` in the profile and in `load_profile`'s
required subset, matching the file's three existing `_during_staging` siblings. The claim becomes
true as history, and the assertion moves rather than disappearing: reverting to the bare name now
fails `PROFILE_CONTRACT_PIN`, verified by falsification.

## Identities

`change-flow` did not change. Both fixes are in `flowmaster-validate`.

| artifact | round 28 | round 29 |
|---|---|---|
| `change-flow.skill` | `ed7041c0…` / 242827 | **unchanged** |
| `flowmaster-validate.skill` | `b5f5d3a3…` / 285630 | `423458d9…` / 286739 |
| `change-flow` freeze | `80e877c2…` / 21 files | **unchanged** |
| `flowmaster-validate` freeze | `13353ffe…` / 29 files | `5da1c46b…` / 29 files |
| `SKILL_TREE_SHA256` | `8ed6d8b0…` | `740844f0…` |
| fixture cases | 156 | 164 |

Contracts, graph and revisions are untouched by this round: contract `2b78f877…` / 606657, graph
`90021eb7…` / 569835, 3.2.9 / 3.2.15 / 3.2.13.

## Gates, from the extracted package contents, full sibling tree

| gate | flag | result |
|---|---|---|
| `validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []`, `SELECTED_PRODUCTION` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, **164 cases** |
| `validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK` |
| `validate_gcfpe_current.py` | `ok` | `true`, `errors: []` |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` |

Zero `.pyc` in the synced directory; it was never written to.

## The delivery defect, separately

`SFR-01` was handed a **stale copy** of the round-28 reviewer prompt — byte-identical to commit
`24dfe87`, pinning evidence at `b83bd107`, while the branch had moved two commits further. Those
two commits rewrote A1, L2 and §9: the delivered copy said reading the corpus was forbidden; the
branch said the opposite. **The reviewer resolved it correctly against the policy and read bodies
anyway.** Following the copy as handed would have reproduced the exact misreading the branch
existed to correct.

Cause: I corrected the repository copy and never re-delivered the file. The round-29 prompt is
delivered after its final push and says plainly which commit it was delivered at, and that a later
head only ever corrects it.

## Open — A1's residual, unchanged by this round

`SFR-01` read **6 bodies from the 48 I had not read**, one per lane, all clean in every form.
Direct confirmation now stands at **13 of 55**. The other 42 rest on the inferential argument whose
blind spot is F1 itself.

**F1's correction plus one sweep with `--bodies-stdin` closes it**, and that sweep has not been
run. Neither `SFR-01` nor I assert any body is dirty; this is the honest residual, stated as one.
