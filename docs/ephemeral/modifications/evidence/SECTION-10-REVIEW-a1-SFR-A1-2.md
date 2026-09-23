---
artifact_type: SKILL_REVIEW_VERDICT
round: a1 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries)
reviewer: SFR-A1-2
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a1.md (branch HEAD 4cb0b77d1a35330e950a72add8083eba51a8eaf1)
written: 2026-09-23
verdict: SKILL_REPAIR_REQUIRED
---

# §10 review, round a1 — SFR-A1-2

## Verdict

**SKILL_REPAIR_REQUIRED**

This verdict applies to these six packages, reviewed together as one set, and only to these bytes. It is
void for any other bytes.

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54344 | db6c4807c2c552114b816c9e720825b0faa07317ed797e199b05a2cd31ad8999 |
| change-flow.skill | 22 | 257847 | a1170af8d953dcd06aa750b6dd4adf1a29f8ca1ed74e4a14c7f444c3507e73c6 |
| flowmaster-validate.skill | 31 | 313930 | 3ebce735eeb88d3dfc028c94df49ba30f4f24ece110caf274e9be5b267665688 |
| glow-hde-pr-development.skill | 4 | 22191 | c77f624f9903c8c4849d963dc2c57dac139ddd2833b4a0f13e6d6051552cb316 |
| session-relay-flowmaster.skill | 5 | 56281 | bfe6b8c6f94f67144953a96c4e037fe010281aa76e0ca27200fb9b1f1d883d89 |
| tw-flowmaster.skill | 2 | 20318 | bdb73141cfabae14a6305eaa24002e61930d5b54752a24e821fd886126741556 |

There is **one required finding (F1)**. It is in `flowmaster-validate` only: the spec calls for a check
that the package does not contain. I found no required finding in the other five packages. The
current bytes of the successor oracle, matrix, map and contract are correct as measured. F1 is a
missing guard, not a wrong value.

## What I measured (derived from the artifacts in front of me, not taken from the report)

- **Packages (§8a).** All six files match the §1 sizes and sha256 values. Each zip holds the stated
  number of entries, all regular files under its own skill root. There is no `..`, no absolute
  path, no backslash, no symlink and no duplicate entry. The frontmatter `name:` in each `SKILL.md`
  is unchanged.
- **Baseline (§3).** `freeze.py` on the installed synced tree reproduced all six baseline digests
  in full: `b9ca212a…`/29, `80e877c2…`/21, `e109d47a…`/4, `4ef8daa3…`/5, `6cd088a0…`/15 and
  `fa3fac85…`/2. I re-measured them at the end of the review and got the same values. The tree did
  not move. Branch HEAD was `4cb0b77` at both the start and the end.
- **Extracted trees.** They gave `d2d98c69…`/31, `880c4284…`/22, `c075226e…`/4, `fb70af77…`/5,
  `46d22b2d…`/15 and `1875015f…`/2, all matching the brief.
- **Diff (§8c, derived with `diff -rq`).** It lists 29 entries:
  - 26 changed files;
  - 3 new files: the successor oracle, the successor matrix and the successor runtime map.

  Every change maps to a §8a/§8b/§5/§6 site in spec v2. The historical oracle (`52807e58…`), the
  historical map (`5574666e…`), the 091326.2 alias and the correction layers are byte-unchanged.
- **Graph.** `graph_parts.py build` of the branch's `docs/graph/parts` gave 55 nodes, 229 edges and
  575 074 B, sha256 `ae2bd159…`. This is byte-identical to the graph bundled in both skills. It is
  also the `<root>` I used.
- **Contract (C2).** I ran `regenerate_contract.py acceptance` myself:
  - The template was today's contract, the parts were at `0084183` (pre-E1), and I used the baseline
    validator scripts.
  - Regenerating from the stripped template (61 859 B, so not a no-op) reproduced `2b78f877…` at
    606 657 B.
  - The negative control passed, and no mirrored path fell out under leave-one-out.

  `generate` from the final build reproduced the shipped contract byte for byte: 613 162 B,
  `7a7fd028…`. The copies in both skills are identical. `validate_graph_contract` returns `[]`,
  `validate_contract` returns `[]`, and the routing surface is `fecc319bdd4ce7ee6201cb77d7231861`/284.
  - With the *new* validator against the pre-E1 build, the negative control reads False. That is
    expected, because the new validator rejects the old graph.
- **Routing diff (C3).** I diffed the old and new contracts route row by route row. I found 13
  changed or added route rows (the PR-40 → PR-30 row became PR-40 → PR-20) plus 2
  boundary_transitions: 15 in all. Every condition string matches the A1-7 table verbatim.
- **Oracle (C6).** 46 rows, in the historical order. Exactly GCF-14 (`consumes`), GCF-17 (`name`,
  `actor`, `session`, `failure_stop_condition`) and GCF-17.LINEAGE (`next`,
  `failure_stop_condition`) differ, along with their `source_row_sha256`. The other 43 rows are
  equal to the historical rows in all 12 fields.
  - The top-level keys that differ are only `profile_id`, `authority` (the 3 appended keys) and
    `required_global_tokens` (the profile token).
  - I recomputed the row-digest formula for all three rows. Each equals the oracle value, the matrix
    `source_row_sha256:` line and the matrix block.
  - Each `supersedes_source_row_sha256` equals the historical digest. The formula does not reproduce
    the historical digests, as the spec states.
  - Matrix: 3 653 B, `8b443eb1…`, byte-equal to the repository copy. Oracle `ede635b1…`. Map
    `aa6ed8e3…`, which equals the §5.6 projection.
- **Hash pins (§8e).** Every 64-hex value added by the diff resolves to an artifact in the set:
  - `ede635b1` oracle ×11 sites;
  - `aa6ed8e3` map ×6;
  - `8b443eb1` matrix ×3;
  - `7a7fd028` contract ×2;
  - `ae2bd159` graph ×5;
  - `c433aa09` fixtures ×2;
  - `08979501` `SKILL_TREE_SHA256`, which equals the measured `skill_tree_digest`, with self-identity `[]`.

  No live site still carries `2b78f877`, `90021eb7`, `a1a73062`, `eb9634d6` or `7380cd14`.
- **Revisions (§8f, by grep).** pr-dev 1.3.0 at 4 sites; change-flow 3.3.0 at 6; relay 3.1.0 at 2;
  tw 1.2.0 at 2; amthor 1.12.0 at 2; `validator_revision` / `FLOWMASTER_VALIDATE_REVISION` 3.3.0 at 5;
  contract `primary_skill_revision` 1.3.0 in both copies. The remaining older values are historical
  changelog prose, historical contracts, or the v3 alias path (S-5, §8a O25).

## Gates actually run

All runs were on a full scratch copy of the synced tree with the six skills replaced, under
`PYTHONDONTWRITEBYTECODE=1` and with `TMPDIR` in scratch. I read each tool's own top-level flag.

| command | result |
|---|---|
| `validate_flowmaster.py --skills-root <copy>` | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, exit 0 |
| same, with `--strict-warnings --gcfpe-contract … --gcfpe-candidate-root <root>` | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, exit 0 |
| `validate_gcfpe_20260914.py <cf> --contract …` | `"ok": true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py <cf> --contract …` | `fixture_suite_ok: true`, **228 cases, 0 failed**, section-13 37/37 and 38/38 variants |
| `validate_gcfpe_current.py <cf>` | `"ok": true` (output byte-equal to the v4 run; S-5 delegates) |
| `run_gcfpe_current_fixtures.py <cf>` | `fixture_suite_ok: true`, 228/0 |
| `run_change_flow_fixtures.py` | `fixture_suite_ok: true`, 32/32, profile `…R1_20260923_1` |
| `<cf>/scripts/validate_gcfpe_20260914.py` | `PASS`, exit 0 |
| `validate_glow_hde_pr_development.py` | `PASS` |
| `validate_relay_manifest.py --self-test` | `status: PASS`, 230 cases, 0 failed |
| `run_fixture_suite.py` (amthor) | 34 tests OK |
| `validate_project_prompt_registry.py` on the branch registry | `{"valid": true, "problems": []}` |
| 12 historical-layer commands of spec v2 §2 | all exit 0; each output **byte-equal** to the same command on an unmodified baseline copy (0 B for the four no-output validators) |
| `validate_gcfpe_current.py --contract <alias 091326.2>` (extra) | `ok: true` on both the baseline and the new copy |
| `regenerate_contract.py acceptance` and `generate` | as above |
| My own mutation runs (about 25 cases, below) | as reported under each finding |

**Not run, plainly:**
- `route_sim_final.py`. Its hard-coded scratch path lies outside my permitted scratch directory, and
  it reads the post-E1 parts. I verified its product, `fecc319b…`/284 and the 15-row diff, directly
  from the contract instead.
- `e1_registry_apply.py`, `e1_graph_transform.py`, `g16_graph.py`, `build_r1_successor.py`. They
  write to the repository or to skill paths. I read `build_r1_successor.py` and reproduced its
  outputs' digests independently.
- `body_rules.py` / `run_e4.py`. This is optional under L1, and it needs live Notion bodies.
- `closure.py`, `modification_validate.py`, and the author's `regress_*` scripts.

**A procedural slip of mine.** One import without `PYTHONDONTWRITEBYTECODE` wrote a `__pycache__` into
my extracted `ext/` tree (not into the synced tree or the copy the gates ran on).
- I found it, deleted it, and confirmed `ext == copy` with `diff -rq`.
- `freeze.py` again gave `d2d98c69…`, and self-identity is `[]`.

## Findings

### F1 (required) — the matrix digest-line check that spec v2 requires is missing

- **Artifact.** `flowmaster-validate/scripts/validate_flowmaster.py`, `successor_oracle_findings`
  (package `3ebce735…`).
- **Defect.** Spec v2, §12 *Addendum, v2*, §5, *"The matrix bytes"*, states: *"A check reads each
  `source_row_sha256:` line and compares it with the oracle's digest."* No shipped code reads those
  lines:
  - `MATRIX_BLOCK_RE` parses only the JSON fences;
  - N7 (FMV-ORACLE-013) recomputes the oracle row's digest, not the matrix line;
  - `grep` finds no reader in any of the six packages;
  - the builder (`build_r1_successor.py`) writes the lines from computed values but never reads them
    back.
- **Evidence.** Mutation `restamp_matrix_digest_line_lies`:
  - Replace the GCF-14 line with `source_row_sha256: abab…ab`.
  - Write the new matrix digest into `authority.successor_source_matrix_sha256`.
  - Re-serialize the oracle and re-derive the map.
  - Re-stamp `EXPECTED_ORACLE_SHA256`, the map constants, the v4 R1 literals, the profile and
    `SKILL_TREE_SHA256`. This is the spec's own re-stamp set.

  No FMV-ORACLE-00x finding fires. The only findings are the contract and graph
  `PROTECTED_IDENTITIES` pins I did not re-stamp. That is the same finding set produced by a benign
  change to `generated_for_run`, so it is not a provenance catch.

  The matrix is the human-readable authority for the three changed rows (A1-1 "Provenance"). Its
  displayed digest can therefore disagree with the oracle, and nothing notices. The current bytes
  agree, as I measured.
- **Smallest correction.**
  1. In `successor_oracle_findings`, read `^source_row_sha256: ([0-9a-f]{64})$` lines, one directly
     after each JSON fence.
  2. Require exactly three such lines, paired with the blocks in order.
  3. Require each to equal the oracle row's `source_row_sha256`. N7 already ties that value to the
     formula.
  4. Emit a new code, for example `FMV-ORACLE-018`, or extend FMV-ORACLE-011.
  5. Add a must-fail regression: tamper one line, re-stamp, and expect exactly that finding.
  6. Re-stamp `SKILL_TREE_SHA256`.

  Only the `flowmaster-validate` package's bytes change. No other package pins them. The set then needs
  re-review against the new `flowmaster-validate` digest.

### Advisory findings (not required for fit; recorded so they are not lost)

- **V1 — oracle keys that are not rows are not tied to history.**
  - Artifact: `validate_flowmaster.py`, N1–N10.
  - Defect: nothing ships that compares these keys with the historical oracle:
    `prohibited_active_patterns`, `special_destinations`, `external_inputs`, `terminal_outputs`,
    `coverage`, `schema_version`, `generated_for_run`, and `required_global_tokens` (beyond the
    profile token).
  - Evidence: under the same re-stamp, dropping `prohibited_active_patterns[0]` fired no provenance
    finding. That list drives the obsolete-pattern scan at `validate_flowmaster.py:1007`, so the scan
    would silently narrow. `build_r1_successor.py` asserts this property only at build time
    (`top == [authority, profile_id, required_global_tokens, runtime_rows]`). Dropping an
    `external_inputs` entry is caught incidentally by FMV-GCF-INPUT-001.
  - Correction: an N11 check in the same edit as F1, with a regression. The spec does not require it,
    and it would strengthen C6.
- **V2 — the fallback predicate has no guard in skill text.**
  - Artifact: `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py`, and
    `CONTRACT_REQUIRED` for the relay and tw.
  - Defect: A1-5's predicate "only where no `MERGE_OBSERVED` result was returned for this merge" is
    guarded in the contract (`event_2`, `pr40_entry`, `entry_fact` and the boundary condition). No
    skill validator requires it.
  - Evidence: deleting every occurrence from `glow-hde-pr-development/SKILL.md` passes every suite.
    In `change-flow` the deletion fails only by accident, because the shortened text matches a
    retired clause.
  - The §8a.3 list is implemented as specified, so this is a gap in the spec, not an implementation
    deviation. A required literal and a deletion regression would close it.
- **V3 — stale prose around the re-pointed alias (S-5).**
  - `flowmaster-validate/SKILL.md:157` ends "while the selected alias remains
    `GCFPE-20260913.1 / 091326.2 / 54` until promotion".
  - The re-pointed paragraph at `:382` keeps "the candidate validator proves the predecessor alias
    remains selected during staging" beside "the alias is validated only when passed explicitly".
  - The FMV-GCF-CURRENT-FIXTURE-001 evidence text still says "selected-alias fixture suite" for what
    is now the 091426.1 default overlay.
  - These are wording only, with no check effect. They are candidates for the next Modification.

## Answers to §6

- **A1 — could a third row change pass unnoticed?** No. An independent run edited GCF-15 `session`,
  set its digest by the formula and re-stamped. FMV-ORACLE-015 fired on GCF-15.
  - The pinned `SUCCESSOR_ROWS`, N4 and N9 (with order) together make the 43-row count exact.
  - N10 pins the four historical attestations.
  - The digest formula is sound, and I recomputed it.
  - The authority block matches §5.5 verbatim.
  - The provenance gaps are F1 (the displayed digest lines) and V1 (keys that are not rows), not
    rows.
- **A2 — the regenerator's contract-only value table.** Every table value equals §12 V-3 to V-8 and
  W-8 as settled. Each is read by an exact-value check: `HANDOFF_CONTRACT` (exact keys),
  `RECEIVER_CONTRACT:*` (all seven), `ROUTE_GRAPH_SEMANTICS`, `ROUTE_GRAPH_SHORTHAND`,
  `EXPECTED_EVENT_2`, `EXPECTED_OBSERVED_MERGE_EDGES`, `PR_DEVELOPMENT_CONTRACT`, `RESCOPE_CONTRACT`
  and `PROTECTED_IDENTITIES`.
  - Values that nothing checks and that could fall stale: `historical_non_executable_references`
    appears in no exact-value check I found. It is correct now.
  - The unchanged `route_graph_semantics.rs40` ("…only after for PR-30_POSTPUBLICATION or PR-35.")
    is ungrammatical, but it predates this change and has an exact check.
  - The "same-session" strings left in the contract (PR-30 role, edges 156 and 161, RS-20 rows
    215/216) are mirrored graph text inside the diff Nathan read. Each refers to the phase's own
    session.
  - `boundary_transitions.NATHAN_PROCEED` keeps `branch_id: original_proceed` under a condition that
    no longer says "original". That is cosmetic, and it is part of the diff Nathan read.
- **A3 — the reversed literals.** Each reversed literal has a replacement that still guards the kept
  rule, and its old text is forbidden. My injections:
  - "same-session PR-35 handoff" into the relay and tw fails;
  - "supplies merge approval" into tw fails;
  - removing the override from change-flow, the relay or tw fails;
  - removing the A1-8 top-level sentence from tw fails;
  - replacing the no-agent-merge sentence in pr-dev fails in four suites;
  - `r1_oracle_changed: false` fails (author fixture);
  - the old ten-field list and "one dedicated PR-development session" are forbidden in pr-dev,
    change-flow and amthor.
  - Not guarded in pr-dev and change-flow: injecting "launched as a new session" (forbidden only for
    the relay and tw, per §12 §8b O4), and deleting "stay subscribed and do not poll" (the kept
    no-poll rule is still required through "never … keep polling for that manual action").
  - The PR-40 independent-verification rule is still required, through "PR-40's duty to
    independently verify actual merged state and landed lineage".
- **A4 — the PART-11 fallback.**
  - No-dispatch path: none. If the subscription is inactive, is held by a PR Steward, or the session
    is gone, no `MERGE_OBSERVED` is returned, so the conditional block stays usable.
  - Double dispatch: a race window exists.
    - Nathan merges and pastes the conditional block *before* the subscription delivers the event.
      The predicate is then true, because no `MERGE_OBSERVED` has been returned yet.
    - When the event arrives, the PR-35 session returns `MERGE_OBSERVED` with a second PR-40
      handoff.
    - Nothing in the wording or the behaviour cases makes that second handoff conditional on the
      first not having been used.
    - Both are paste actions that Nathan performs, and PR-40 is read-only, so the harm is a duplicate
      review.
  - The packages carry C-DISPATCH exactly as Nathan approved it. This is therefore **a question for
    Nathan, not a package finding**. One remedy for a later Modification: the `MERGE_OBSERVED`
    handoff is usable only if no PR-40 session was already started from the conditional block for
    this merge.
- **A5 — the override.**
  - The override text is identical in change-flow `:265`, relay `:257` and tw `:302`. Each is held by
    `CONTRACT_REQUIRED`, and deleting it fails.
  - The Flowmaster core is still byte-identical: `core_sync: true` for all five skills.
  - The relay's provisioning lines `:255` and `:717` are scoped "Outside a GCFPE main-ecosystem
    stage". The W-9 sentence follows the override, per addendum U-6.
- **A6 — §12 and its addendum, and G11.** The settlements I checked are all implemented: S-5, S-6,
  S-7, S-8, W-1 to W-10, V-1 to V-12, OQ-1 to OQ-14, O-series and U-1 to U-8b.
  - The exception is F1: the addendum's digest-line check is missing.
  - G11's expected set of four departs from §12's "two wrapper codes". The departure is recorded in
    §E as the author's choice, and I find it sound:
    - under S-5 the default overlay runs the v4 checks;
    - so FMV-GCF-CURRENT-001 and FMV-GCF-CURRENT-FIXTURE-001 are genuine consequences of the same
      single profile mutation;
    - no finding is dropped.
- **A7 — contradictions with kept rules.** None found.
  - No agent merge: kept and required everywhere.
  - No polling for the manual merge: kept. The new "where no subscription delivers it, poll only
    when…" covers review/CI evidence, not the merge.
  - One handoff block per result: kept. `MERGE_PENDING` and `MERGE_OBSERVED` are separate results.
  - PR-40's independent verification: kept.
  - Single Proceed within a plan: "One Proceed per approved per-PR plan"; a continuation never
    creates a second Proceed, and only a re-plan gets a new one.
- **C5.** Outside the shared Flowmaster core, which the override neutralises for GCFPE, no text in
  the six skills instructs creating, launching or scheduling a session, or running a main-ecosystem
  prompt as a subagent.
  - Out-of-scope lines I noted: the TW flow's own session creation (tw `:281`, `:425`, `:427`), which
    §12 records as outside the main ecosystem.
  - `amthor` SKILL `:77` ("Run BASELINE, FINAL_VALIDATION, and high-risk independent reviews in fresh
    sessions") is governance-audit procedure, not a main-ecosystem prompt.
- **Question — anything outside Amendment 1's scope?** Nothing I found. Every changed line traces to
  a numbered step, a child step, an A1 ruling, or a §12/addendum settlement. That includes the C-D22
  wording (step 45 / W-7) and amthor `:32` (A1-3).

## DECISION NEEDED

- **F1 blocks this set.** Nathan chooses between two routes (§P step 47): have the author fix F1 in
  `flowmaster-validate` and re-review the set against the new digest, or ship without the rejected
  part.
- **V1 and V2** can ride along with the F1 fix, at the author's discretion.
- **A4's double-dispatch window** is a wording question for Nathan, not for this package set.
