---
artifact_type: SKILL_FIT_REVIEW
round: a1 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries)
reviewer: SFR-A1-1
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a1.md (10 968 B, sha256 5e33dff4034b7dbbf2c6228472a95614f440e1777ae676b0ab44c973e2bbca13)
repository_head_read: 4cb0b77d1a35330e950a72add8083eba51a8eaf1 (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged)
reviewed_at_utc: 2026-09-23T08:50Z
scratch: /tmp/claude-0/review-SFR-A1-1/
---

# §10 review, round a1 — SFR-A1-1

## Verdict

**SKILL_REPAIR_REQUIRED**

This verdict applies only to these six packages, as they sat in `/tmp/claude-0/pkg/new/`. I recomputed each value from those bytes:

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54 344 | `db6c4807c2c552114b816c9e720825b0faa07317ed797e199b05a2cd31ad8999` |
| change-flow.skill | 22 | 257 847 | `a1170af8d953dcd06aa750b6dd4adf1a29f8ca1ed74e4a14c7f444c3507e73c6` |
| flowmaster-validate.skill | 31 | 313 930 | `3ebce735eeb88d3dfc028c94df49ba30f4f24ece110caf274e9be5b267665688` |
| glow-hde-pr-development.skill | 4 | 22 191 | `c77f624f9903c8c4849d963dc2c57dac139ddd2833b4a0f13e6d6051552cb316` |
| session-relay-flowmaster.skill | 5 | 56 281 | `bfe6b8c6f94f67144953a96c4e037fe010281aa76e0ca27200fb9b1f1d883d89` |
| tw-flowmaster.skill | 2 | 20 318 | `bdb73141cfabae14a6305eaa24002e61930d5b54752a24e821fd886126741556` |

The verdict is void for any other bytes. No prior confirmation carries to these bytes.

The tree did not move during the review. The six baseline freeze digests were the same at the start and at the end (08:50Z). Nothing was installed. I wrote nothing to the synced skills directory, and I made no commit, merge or auto-merge. The only repository file I wrote is this record.

**Reason, in one line:** one check that the plan's author settled in the spec v2 addendum is missing from `validate_flowmaster.py` (F1). The fix is small. Everything else I measured reproduces. F2 is a hardening gap that I recommend fixing in the same repair. F3 needs a decision from Nathan.

## Findings

### F1 — the settled matrix digest-line check is missing (blocking)

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, in `successor_oracle_findings` (package `flowmaster-validate.skill`).
- **Defect:** spec v2 §12 *Addendum, v2*, §5, settles §5.14 item 6 as follows: "A check reads each `source_row_sha256:` line and compares it with the oracle's digest." No validator reads those lines.
  - `MATRIX_BLOCK_RE` captures only the JSON fences.
  - N5–N8 (FMV-ORACLE-011 to -014) never parse the `source_row_sha256: <hex>` lines.
  - `grep -rn 'source_row_sha256:' --include=*.py` over the package returns nothing.
  - No regression covers the check.
  - C1 claims the packages carry exactly the §5 settlement, so C1 does not hold.
- **Evidence:** I ran two must-fail probes on a scratch copy, using the author's own re-stamp helper (`regress_oracle.py` `restamp`, re-pathed into my scratch).
  - **T6:** set GCF-14's matrix line to `source_row_sha256: 000…0`, then write the new matrix digest into `authority`. Both the default and candidate suites returned `FLOWMASTER_SUITE_PASS` with `[]`.
  - **T7:** delete all three digest lines, then re-stamp. The result was the same: both suites pass with `[]`.
  - Today the matrix's three digest lines do equal the oracle rows and the formula; I recomputed all three. So the bytes are correct, but no check enforces them.
- **Smallest correction:**
  1. Extend the matrix parse to capture the `^source_row_sha256: ([0-9a-f]{64})$` line after each fence.
  2. Require exactly one such line per block, equal to that oracle row's `source_row_sha256`.
  3. Emit a new code in the series, FMV-ORACLE-018, or report it under FMV-ORACLE-011.
  4. Add T6 and T7 as must-fail regressions.
  5. Re-stamp `SKILL_TREE_SHA256` and rebuild the package.

### F2 — re-stamped changes to successor-row fields and non-row oracle keys pass (recommended with F1)

- **Artifacts:** the same function; claims C4 and C6; attack items A1 and A3.
- **Defect:** N9 replaces `protected_r1_46_rows_unchanged: true`, but it guards only the 43 rows outside the successor set. Nothing independent of the re-stampable whole-file pins guards four other things against the historical oracle:
  - the content fields that A1-1 did **not** change inside the three successor rows;
  - the positions of the successor rows;
  - the non-row top-level keys: `prohibited_active_patterns`, `special_destinations`, `external_inputs`, and the other entries of `required_global_tokens`;
  - `terminal_outputs`, which is guarded only indirectly, through FMV-GCF-OUTPUT-001.
- **Evidence:** I ran each probe under the full re-stamp, then ran both suites.
  - **T5:** change GCF-17 `approval_contract` in both the oracle and the matrix to "…The PR session may merge after review.", recompute its row digest, re-stamp. Both suites: `FLOWMASTER_SUITE_PASS`, `[]`. That field carries a kept rule: no new PO approval binding, and no agent merge.
  - **T1:** move GCF-14 to the end of `runtime_rows`. Pass, `[]`.
  - **T3:** drop one `prohibited_active_patterns` entry. Pass, `[]`.
  - **T2:** drop one `terminal_outputs` entry. Caught by FMV-GCF-OUTPUT-001.
- **Scope:** this conforms to the spec as written. §5.7 defines N9 over the 43 rows only. The gap does not contradict the bytes shipped: I diffed the successor oracle against the historical oracle, and the only differences are the authorized ones. I report it because the spec measures its guards against this same re-stamp model, and A1 asks exactly whether an unauthorized change can pass.
- **Smallest correction:**
  1. Pin, per successor row, the set of fields allowed to change: GCF-14 `consumes`; GCF-17 `name`, `actor`, `session`, `failure_stop_condition`; GCF-17.LINEAGE `next`, `failure_stop_condition`. Each row's `source_row_sha256` may also change.
  2. Require every other content field of those rows to equal the historical row.
  3. Require the successor rows to sit at their historical indices.
  4. Require the remaining top-level keys to equal the historical ones. `required_global_tokens` may differ only in the one profile-id entry. `authority` may add only the three successor keys (N10 and FMV-ORACLE-003 already pin the other five).
  5. Add T1, T3 and T5 as regressions.

### F3 — a Nathan-mediated double PR-40 dispatch path exists in the canonical wording (decision for Nathan; not a skill-text defect)

- **Artifacts:** C-DISPATCH and `{FALLBACK}`, carried verbatim in:
  - `glow-hde-pr-development/SKILL.md:110`, and behavior-cases.md "Observed merge";
  - `change-flow/SKILL.md:333` and `:457`;
  - the relay (`:287`) and tw (`:321`);
  - `flowmaster-validate/SKILL.md:173`;
  - `amthor` SKILL.md and references.
- **Defect (A4):** the conditional PR-40 block is lawful "only where no `MERGE_OBSERVED` result was returned for this merge". That condition is judged when Nathan pastes the block. The sequence below yields two PR-40 entries for one merge, and no text says the second is void:
  1. Nathan merges.
  2. He pastes the conditional block at once, lawfully, because no `MERGE_OBSERVED` has been returned yet.
  3. The subscribed PR-35 session then receives the merge event.
  4. It returns `MERGE_OBSERVED` with a second paste-ready PR-40 handoff, which the text calls "the fact PR-40 is entered on".

  No agent creates a session here, because Nathan must paste twice. So this does not breach D23, but it can produce two lineage reviews of one merge.
- **No-dispatch path:** none found. When no `MERGE_OBSERVED` is ever returned, for example because the subscription is inactive or the session has ended, the fallback stays usable.
- **Smallest correction (needs Nathan, because A1-5's wording is approved canonical text):** add one clause to C-DISPATCH, applied everywhere it is carried: "the `MERGE_OBSERVED` handoff is not used where PR-40 was already entered for this merge through the conditional block." Alternatively, record that PR-40 is entered at most once per merge.

## Answers to §6

- **A1 (successor-oracle provenance). A third row cannot change unnoticed, but field-level changes inside the successor rows can.**
  - Matrix bytes: 3 653 B, `8b443eb17180f85e8d615ba56ed6e1d1d78802fcd1a49aa3be3b5dd638bc4d04`. The repository copy is byte-identical.
  - Each of the three blocks has exactly 12 keys, in oracle key order, and equals its oracle row. Each `supersedes_source_row_sha256` equals the historical row digest.
  - Recomputed row digests: `42db7a9e…`, `67745290…`, `73a133c1…`.
  - The authority block is exactly as §5.5 specifies.
  - N1–N10 and FMV-ORACLE-017 each fire on their author regressions.
  - **Any row outside the pinned set:** N4 (pinned set) together with N9 (43 rows compared whole, and in order) catches it.
  - **What is not caught:**
    - the matrix digest lines are unread (F1);
    - under re-stamp, unlisted fields inside the three successor rows, the positions of those rows, and several top-level keys are unguarded (F2).
- **A2 (contract-only value table). No stale or unread value found.**
  - I diffed old against new contract by key path: 56 changed paths, 42 of them outside `route_edges`, `state_routes` and `member_registry`.
  - Every changed contract-only key is read by `validate_gcfpe_20260914.py` as an exact expected literal: `receiver_compatibility.*`, `route_graph.*`, `route_graph_semantics.*`, `transition_contract.*`, `pr30_ownership`, `primary_skill_revision`, `preserved_lineage`, `historical_non_executable_references`, `contract_revision`, `graph_proofs`, `protected_identities`.
  - Remaining "same-session" text is mirrored and still true: PR-30 and PR-35 each re-enter their own session.
- **A3 (reversed literals). Each reversed literal is still guarded, and injecting the old text fails.**
  - I reproduced the author's regressions on my copy: skills 70/70, contract 88/88, fixtures 2/2.
  - Independent injections all failed as they should:
    - "one dedicated PR-development session": PR-skill validator FAIL;
    - the backticked "same-session `PR-35` handoff": FAIL;
    - `protected_r1_46_rows_unchanged` set true: GRAPH_PROOFS;
    - `r1_oracle_changed` set false: PROTECTED_IDENTITIES;
    - `nathan_manual_merge_assertion_required` restored: RECEIVER_CONTRACT:PR-40;
    - `same_session_phase_continuation` restored: ROUTE_GRAPH_SEMANTICS;
    - the ten-field `shared_exactly_one`: PR_PHASE_CONTINUITY.
  - Limits:
    - N9 does not cover all that the old 46-row flag covered (F2).
    - The PR-skill validator forbids only the backticked form. The plain "same-session PR-35 handoff", which base `SKILL.md:22` also carried, passes when injected. This is not a finding: that form was never a validator literal, and the relay/tw validators do forbid it.
- **A4 (PART-11 fallback).**
  - No no-dispatch path.
  - One double-dispatch path, Nathan-mediated (F3).
  - The contract, graph and fixtures carry the edges consistently: `merge_observed` from PR-35 and RS-40, non-automatic, COMPLETE_NEXT_PROMPT_HANDOFF; and `pr35_merge_pending_fallback` through NATHAN_MANUAL_MERGE_ASSERTION.
- **A5 (GCFPE override). Confirmed.**
  - The override paragraph is byte-identical in change-flow `:265`, relay `:257` and tw `:302`, and each skill holds it as a `CONTRACT_REQUIRED` literal (R-OV-1…3 fire).
  - The Flowmaster core block is unchanged in all three skills: sha256 `4d8bb9bf1c9c85ae…`, equal to the baseline.
  - The relay provisioning lines `:255` and `:717` are scoped "Outside a GCFPE main-ecosystem stage". The W-9 sentence follows the override (U-6). It is redundant with the override but does not contradict it.
- **A6 (author's choices in §12 and the addendum, and G11). All acceptable except F1.**
  - G11 yields four findings (the two candidate wrappers plus FMV-GCF-CURRENT-001 and FMV-GCF-CURRENT-FIXTURE-001), because under S-5 the default overlay runs the v4 checks. I reproduced exactly these four. They are one defect reported twice, and nothing is masked. I accept the four-finding set.
  - A minor evidence note, not a package defect: `evidence/e2/regress_oracle.py:159` still expects two findings, so both its committed output and my re-run print "BAD G11" and "14 of 15 exact". §E records the settlement, but the script does not.
  - Other addendum items: the matrix header is read literally; `change-flow:563` names the historical map as provenance; U-6 order; tie check FMV-ORACLE-017; codes 008–016 and MAP-007; ROUTE_GRAPH_SEMANTICS, GRAPH_HANDOFF_PROHIBITED_REFERENCES and PR35_TOP_LEVEL_ROLE present.
  - The one addendum item not implemented is the digest-line check (F1).
- **A7 (contradictions with kept rules). None found in the edited text.**
  - No agent merge: kept everywhere.
  - No polling: "stay subscribed and do not poll". Polling is allowed only "where no subscription delivers it".
  - One handoff block per response: C-HANDOFF, and "The final response ends with the `NEXT_PROMPT_HANDOFF` block".
  - PR-40's independent verification: "`PR-40` still verifies… independently".
  - Single Proceed within a plan: C-PROCEED, with a new Proceed only for a PR-40 REJECT re-plan.
  - The dropped PR-30 "review corrections" bundling (`:79`) is spec step 27. PR-35's correction bundling survives at `:93` and in "group related corrections". The dropped lineage clause at `:22` is §12 §8a O4 (a).
- **Question, out of Amendment 1's scope? No.** Every changed file and hunk I read traces to a §P step, an A1 ruling, or a §12 or addendum settlement. Examples: C-D22 at flowmaster-validate `:60`/`:231` (step 45); C-HANDOFF (step 14); the S-5 default-overlay move; the W-8 renames. I found no hunk without a source.

## Claims C1–C7

- **C1 — does not hold, because of F1.**
  - What does hold: `diff -rq` against the installed tree shows 22 differing files and 3 added files (the successor oracle, matrix and map), all named by §5, §6, §8a and §8b.
  - The 13 §5.9 historical references, the 12 historical-layer scripts and `flowmaster-primary` are byte-identical.
  - The author's `check_spec_blocks.py` reports one "MISSING" and three "STALE" items. The MISSING one is the relay `:255` block, reordered by U-6. The three STALE ones are old literals that now sit inside forbidden lists.
- **C2 — holds.** I re-ran `regenerate_contract.py acceptance` against the pre-E1 parts (`git archive 0084183`):
  - the stripped template (61 859 B) regenerates `2b78f877…` / 606 657 B;
  - `noop_on_stripped_equals_target` is false;
  - the negative control passes;
  - `generate` reproduces the package contract `7a7fd028…` byte for byte;
  - `validate_graph_contract` against the branch build returns `[]`, and `validate_contract` returns `[]`.
- **C3 — holds.** The package's `routing_surface`, unchanged from baseline, gives `fecc319bdd4ce7ee6201cb77d7231861` / 284.
- **C4 — holds, except for the gap in F2.**
- **C5 — holds on package text.**
  - The only session-creating lines are in the untouched core (change-flow `:145`, `:158`), which the override disables.
  - tw `:281`, `:425` and `:427` are TW ecosystem lines, recorded as out of scope.
- **C6 — holds on bytes.**
  - 46 rows: 26 CORE and 20 MATERIAL.
  - Exactly the ten row fields, the one token and the authority additions differ.
  - The 43 other rows are equal to the historical rows and in historical order.
  - The map equals the projection (`aa6ed8e3…`, 46 326 B).
  - The binding is enforced incompletely (F1).
- **C7 — E1–E4 are not re-run in full.** My results for the gate items I ran are listed below.

## Gates run

All runs were from the extracted trees, in a full copy of the synced tree, with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` in scratch.

**§8a**
- Recomputed counts, bytes and sha256 from the bytes: all equal §1.
- Every archive entry sits under its own skill root: no `..`, no absolute paths, no symlinks.
- `name:` in each SKILL.md is unchanged.
- The freeze digests of the extracted trees equal the brief's "repaired" values:

  | skill | files | freeze digest |
  |---|---|---|
  | flowmaster-validate | 31 | `d2d98c69…` |
  | change-flow | 22 | `880c4284…` |
  | glow-hde-pr-development | 4 | `c075226e…` |
  | session-relay-flowmaster | 5 | `fb70af77…` |
  | amthor-workspace-governance-audit | 15 | `46d22b2d…` |
  | tw-flowmaster | 2 | `1875015f…` |

**Baseline.** It reproduced before the review (all seven freeze digests in spec §2) and was unchanged after it.

**§8b.** Every live suite passes; each tool's top-level flag is as listed:

| suite | result |
|---|---|
| `validate_flowmaster.py` (default) | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, 0 findings |
| `validate_flowmaster.py` (candidate; `<root>` = embedded JSON of `graph_parts.py build` over branch parts, 575 074 B, `ae2bd159…`, equal to both bundled graphs) | `suite_ok: true`, `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_20260914.py` | `ok: true`, errors `[]` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok: true`, 228 cases, 0 failed; section-13 37/37, variants 38/38 |
| `validate_gcfpe_current.py` | `ok: true` (output byte-equal to the v4 validator's) |
| `run_gcfpe_current_fixtures.py` | `true`, 228 |
| `run_change_flow_fixtures.py` | `true`, 32/32 |
| change-flow `validate_gcfpe_20260914.py` | PASS, exit 0 |
| PR-skill validator | PASS |
| relay self-test | `status: PASS`, 230 cases, 0 not ok |
| `amthor` `run_fixture_suite.py` | 34 tests OK |
| registry validator | `{"valid": true, "problems": []}` |

The 12 historical-layer commands all exited 0, and each output is byte-identical to a baseline run on an unmodified copy (raw bytes; no paths embedded).

**§8c.** The `diff -rq` list, derived as described under C1.

**§8d.** 46-row oracle diff: see C6. Contract graph parity: `validate_graph_contract` returns `[]`.

**§8e.** Every hash literal added or removed in a changed file resolves to the artifact it pins:

| pin | artifact |
|---|---|
| `ede635b1…` | successor oracle, in profile `:35`, both contracts, both graphs, the 3 v4 literals, `EXPECTED_ORACLE_SHA256`, and SKILL.md `:149`/`:245` |
| `aa6ed8e3…` | successor map, in profile, v4 ×2, `validate_gcfpe_current`, `EXPECTED_CHANGE_RUNTIME_MAP_SHA256`, and change-flow `:559` |
| `8b443eb1…` | matrix, in authority and SKILL.md |
| `ae2bd159…` | graph, in contract `source_snapshot`, profile, and both v4 validators |
| `7a7fd028…` | contract, in profile and v4 |
| `c433aa09…` | 091426.1 fixtures, in profile and `EXPECTED_FIXTURE_SHA256` |
| `089795017f…` | `SKILL_TREE_SHA256`, which equals the package's `skill_tree_digest` |

The §5.12 residual grep hits only the expected sites, plus the `change-flow:563` provenance line settled in §E. The old profile id appears only in the two historical files.

**§8f.** Revision sites recounted by grep, base against new:

| revision | old → new | sites |
|---|---|---|
| change-flow | 3.2.9 → 3.3.0 | 6 live |
| relay | 3.0.0 → 3.1.0 | 2 |
| tw | 1.1.6 → 1.2.0 | 2 |
| PR skill | 1.2.5 → 1.3.0 | 4, plus `primary_skill_revision` ×3 |
| contract | 4.0.6 → 4.1.0 | 3 |
| `validator_revision` | 3.2.14 → 3.3.0 | 3 JSON sites and one fixture runner |
| FLOWMASTER_VALIDATE | 3.2.16 → 3.3.0 | — |
| amthor | 1.11.3 → 1.12.0 | 2 |

No stale live pin remains. The old values that are left are change-history prose.

**Additional runs**
- The author's regressions, re-pathed into my scratch: oracle 14/15 (G11 settled as four findings), skills 70/70, contract 88/88, fixtures 2/2.
- My own probes: T1–T7 (above) and seven independent injections (A3).

**Not run**
- E3/E4 over the prompt bodies (L1, optional). I did not fetch any Notion body. I did not re-run `body_rules.py`, `run_e4.py` or the G06 registry guards, and I make no claim about them.
- `run_e2.sh` as committed. It writes two repository paths, which §9 of the brief forbids; I reproduced its contract stage with `regenerate_contract.py` into scratch instead.
- No post-install check exists (L2).

## Required before installation

1. Fix F1 (blocking): add the digest-line check and its T6/T7 regressions.
2. Recommended in the same repair: F2's field-level and top-level guards, with the T1/T3/T5 regressions.
3. Rebuild the packages, then run a fresh review against the new digests. This verdict does not carry.
4. Nathan decides F3: whether C-DISPATCH gains the clause that rules out a second PR-40 entry per merge.

DECISION NEEDED
