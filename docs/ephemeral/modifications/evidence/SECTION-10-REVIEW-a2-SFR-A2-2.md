---
artifact_type: SKILL_FIT_REVIEW
round: a2 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a1)
reviewer: SFR-A2-2
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a2.md (14 883 B, sha256 67b7215e6db6e355caa7c0fa8d084099e75bd43079d6b9390b8b8ad4cd1d00d3, equal to its blob at 9c49a65)
repository_head_read: 9c49a65e8c44e36f90eac0d988b0a3b34c06d8c9 (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged), the same at start and end
reviewed_at_utc: 2026-09-23T09:43Z
scratch: /tmp/claude-0/review-SFR-A2-2/
predecessors: SECTION-10-REVIEW-a1-SFR-A1-1.md, SECTION-10-REVIEW-a1-SFR-A1-2.md (other bytes; not corrected here, AUTH-001)
---

# §10 review, round a2 — SFR-A2-2

## Verdict

**SKILL_REPAIR_REQUIRED**

This verdict applies only to the six packages below, installed together as one set, as they sat in
`/tmp/claude-0/pkg2/new/`. I recomputed every value from those bytes. The verdict is void for any
other bytes. No earlier confirmation or measurement carries to these bytes.

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54 461 | `9d5308e67ac91535c6b3184a0e13dd8cc5fca278ec66e660aceaab6bfae7b079` |
| change-flow.skill | 22 | 257 909 | `97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0` |
| flowmaster-validate.skill | 31 | 315 534 | `5ffa13f101db9108cdec356ce638ee0d67fa4c8a5eb2f7952bc13a2e220d3db4` |
| glow-hde-pr-development.skill | 4 | 22 414 | `3292e348febe0136f1d4b6768238be95e2b7b3e529c00595fcf14366016b1d6a` |
| session-relay-flowmaster.skill | 5 | 56 330 | `30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b` |
| tw-flowmaster.skill | 2 | 20 368 | `db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf` |

**Why, in one line.** Brief §2 says the round-a1 V2 repair added the fallback-predicate literals to
"the relay/tw `CONTRACT_REQUIRED` lists". Those lists carry no such literal. The D23-E once-per-merge
sentence is also guarded only in `glow-hde-pr-development`. At the other six sites that carry
C-DISPATCH, I deleted the sentence, its "void" clause, or the fallback predicate. Every gate still
passed, all 18 times (F1). So C8 does not hold as stated. Everything else I measured reproduces.

- F1 is small and confined to `flowmaster-validate`.
- F2 is a new re-stamp gap in the FMV-ORACLE family (duplicate JSON keys). I recommend fixing it in
  the same repair.

The tree did not move. The six baseline freeze digests were the same at the start and at the end. The
end measurement was at 09:43Z, on a fresh byte copy.

What I did not do:
- install anything;
- write to the synced skills directory;
- commit, merge or enable auto-merge;
- write to any repository path except this record.

## Findings

### F1 (required): the V2 disposition in §2 is not in the bytes, and the D23-E sentence is guarded at one of seven sites

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `CONTRACT_REQUIRED` (from
  line 113), in package `5ffa13f1…`. The texts it would guard are in `change-flow`, the relay and `tw`,
  plus two further sites in `amthor-workspace-governance-audit` and `flowmaster-validate/SKILL.md`.
- **Defect:**
  - Brief §2, line 50 of the prompt, disposes of SFR-A1-2 V2 as "required literals in
    validate_glow_hde_pr_development.py and the relay/tw CONTRACT_REQUIRED lists".
  - `grep MERGE_OBSERVED validate_flowmaster.py` returns nothing. The relay and `tw` lists hold only
    the A1-6 override paragraph and the PR-35 top-level sentence.
  - The repair script agrees with the bytes, not with §2. `repair-a1/apply_repairs_a1.py`'s docstring
    says R3 adds literals to the PR-skill validator only. All four R-FB regressions exercise only
    `glow-hde-pr-development`.
  - The same holds for the D23-E sentence Nathan approved ("PR-40 is entered once per merge: …
    Once either has been pasted, the other is void."). It is present, exactly once, at all seven
    C-DISPATCH sites. But only `validate_glow_hde_pr_development.py:94` requires it.
- **Evidence (`probe2.py`, in scratch):**
  - Setup: a full copy of the synced tree with the six skills replaced, and `SKILL_TREE_SHA256`
    re-stamped. No other pin needs to move, because none of these SKILL.md files is hash-pinned.
  - Six sites:
    1. `change-flow/SKILL.md:333` (the predicate deletion also removes it at `:457`);
    2. `session-relay-flowmaster/SKILL.md:287`;
    3. `tw-flowmaster/SKILL.md:321`;
    4. `flowmaster-validate/SKILL.md:173`;
    5. `amthor-workspace-governance-audit/SKILL.md:51`;
    6. `amthor…/references/interoperability-contracts.md:74`.
  - Three deletions at each site: (a) the whole once-per-merge sentence, (b) only "Once either has
    been pasted, the other is void.", and (c) the predicate " and only where no `MERGE_OBSERVED`
    result was returned for this merge".
  - Gates run after each deletion:
    - default suite;
    - candidate suite (`--strict-warnings --gcfpe-contract … --gcfpe-candidate-root`);
    - `change-flow/scripts/validate_gcfpe_20260914.py`;
    - the PR-skill validator;
    - the relay `--self-test`;
    - the amthor `run_fixture_suite.py`.
  - Result: all 18 mutations give `FLOWMASTER_SUITE_PASS` with `[]` in both suites, and every other
    gate passes.
  - On these bytes, the change-flow deletion of the predicate no longer fails even by the accident
    SFR-A1-2 recorded.
- **Smallest correction:**
  1. Add both literals to `CONTRACT_REQUIRED["change-flow"]`, `["session-relay-flowmaster"]` and
     `["tw-flowmaster"]` in `validate_flowmaster.py`:
     - "which is usable only after he merges and only where no `MERGE_OBSERVED` result was returned
       for this merge";
     - the D23-E sentence verbatim.
  2. Optionally, add an `assertIn` for the same two strings on the amthor SKILL.md and
     `interoperability-contracts.md` in `run_fixture_suite.py`. `flowmaster-validate/SKILL.md:173`
     would then be the only site left without a guard.
  3. Add one deletion regression per guarded site.
  4. Re-stamp `SKILL_TREE_SHA256`, then rebuild `flowmaster-validate`, and `amthor` if it was touched.

  Alternative: the author may hold that PR-skill-only guarding was intended. In that case §2 must be
  restated in a successor brief, and C8 re-scoped. Either way, the set then needs review against its
  new digests.

### F2 (recommended with F1): duplicate JSON keys pass FMV-ORACLE-011/012/018/019/020 under the full re-stamp

- **Artifact:** `validate_flowmaster.py`, `load_change_oracle_core` and `successor_oracle_findings`.
  Both parse with plain `json.loads`, which keeps the last duplicate key. `set(block)` and `set(row)`
  then hide the duplicate.
- **Defect:** a matrix block, or an oracle row, can display a second value for a field. That value
  differs from the parsed value and from the authorized one. Every provenance check compares only the
  parsed, last value.

  The matrix is the human-readable authority for the three changed rows (A1-1). This is the same
  class as round-a1 F1: what is displayed disagrees with what is bound, and nothing notices.
- **Evidence (`probe.py`, using the `regress_oracle.py` `restamp` helper re-pathed into my scratch,
  plus a raw-bytes variant for the oracle):**
  - **P1.** I inserted `"approval_contract": "The PR session may merge after review; no PR-40 review
    is needed."` before the real `approval_contract` in the matrix's GCF-17 block. Then I wrote the
    matrix digest into `authority` and re-stamped. Both suites: `FLOWMASTER_SUITE_PASS`, `[]`.
  - **P2.** I inserted the same kind of duplicate into the oracle's GCF-17 row as raw bytes, then
    re-stamped every pin in `restamp`'s set. Both suites: `FLOWMASTER_SUITE_PASS`, `[]`.
  - Runtime behaviour does not change, because every consumer parses last-wins. The defect is in
    provenance and readability only, which is why I rank it below F1.
- **Smallest correction:**
  1. Parse the successor oracle, the historical oracle, each matrix block and the successor map with
     an `object_pairs_hook` that rejects duplicate keys.
  2. Report a duplicate under FMV-ORACLE-011 (matrix), FMV-ORACLE-001 (oracle) and FMV-GCF-MAP-003
     (map), or under a new code.
  3. Add P1 and P2 as must-fail regressions.

### Advisories (not required for fit; recorded so they are not lost)

- **V-a, A4: one contract-only value is not read by any check.**
  - The claim this answers: SFR-A1-1 wrote that every changed contract-only key is read by
    `validate_gcfpe_20260914.py` as an exact literal. I tested that claim.
  - Method: I reverted each of the 31 changed contract paths that are not mirrored to its baseline
    value, one at a time. Then I ran `validate_contract` together with `validate_graph_contract`.
  - Result: 30 of the 31 reverts fail. One passes: `historical_non_executable_references` without
    its two new filenames (§12 OQ-14). That key appears only in a required-keys tuple, at
    `validate_gcfpe_20260914.py:357` and `change-flow/scripts/validate_gcfpe_20260914.py:226`.
  - Its value is correct. Only the re-stampable whole-contract pins guard it.
  - Optional fix: an exact expected-value check.
- **V-b, A3: the "void" clause is missing from two scenario and fixture texts.**
  - `glow-hde-pr-development/references/behavior-cases.md` "Observed merge" (`:123`) and
    `amthor…/references/behavioral-fixtures.md:52-53` describe both PR-40 entries without the void
    clause.
  - Neither contradicts its skill's SKILL.md, which carries the sentence. But the amthor acceptance
    fixture does not reject a second PR-40 entry after the fallback was pasted.
  - Optional fix: add "reject a second PR-40 entry for the same merge" to that fixture line.
- **V-c, A1: an allowed field can take an unauthorized value (a limit, not a finding).**
  - Probe P4b: set GCF-17 `session` to "PR-35 may run as a subagent of the PR-30 session." in both
    the oracle and the matrix, recompute the digests, and re-stamp. It passes.
  - FMV-ORACLE-019 correctly allows `session` to change. The value of an allowed field is bound only by
    re-stampable hashes and by A1-1's text. This is inherent to the re-stamp model: under it, only a
    literal of the value could catch the change.
  - P4 (an added `consumes` input) was caught, incidentally, by FMV-GCF-INPUT-001.
- **V-d: matrix text outside the three blocks is bound only by the matrix digest.**
  - Probe P5: a fourth pseudo-block fenced as ` ```json5 `, for GCF-16, plus an off-format digest
    line. After re-stamping it passes.
  - This is consistent with the author's G4 design: prose is covered by FMV-ORACLE-009 only.
- **Wording:** `flowmaster-validate/SKILL.md:212` ("leave the selected alias untouched") and the
  `--gcfpe-contract` help text at `validate_flowmaster.py:1528` still mention a "selected alias".
  They remain true statements and have no effect on any check.

## Round-a1 findings: does §2's disposition close each one on these bytes?

| a1 finding | closed? | basis |
|---|---|---|
| F1 (both reviewers; matrix digest lines) | **Yes** | FMV-ORACLE-018 reads exactly three `^source_row_sha256:` lines, each directly after a block, and compares each with its oracle row. T6, T6b and T7 reproduce exactly. Each of the three lines equals the row digest I recomputed with the formula (`42db7a9e…`, `67745290…`, `73a133c1…`). |
| SFR-A1-1 F2 and SFR-A1-2 V1 (successor fields, positions, non-row keys) | **Yes, as asked** | T1, T3, T3b, T3c and T5 reproduce. My own probes P6 (historical profile id re-listed in `required_global_tokens`) and P7 (successor authority keys reordered) fire FMV-ORACLE-020. P3 (all three rows reverted to history in both oracle and matrix, digests recomputed) is caught by FMV-FIXTURE-SUITE-001. Residual: F2 (duplicate keys) and V-c. |
| SFR-A1-2 V2 (fallback predicate has no skill-text guard) | **Partly** | Closed for `glow-hde-pr-development` (R-FB-SKILL, R-FB-ALL, R-FB-DISPATCH and R-FB-CONDITIONAL reproduce). Not closed for the relay and `tw`, where §2 says literals were added; they were not (F1). |
| SFR-A1-2 V3 (stale alias prose) | **Yes** | `:157`, `:212` and `:382` are reworded. The FMV-GCF-CURRENT-FIXTURE-001 evidence now reads "current-overlay fixture suite failed". The two residual mentions are listed under Wording above. |
| SFR-A1-1 F3 (double PR-40 dispatch) | **Text yes; guard partly** | The D23-E sentence equals the decision-record successor note verbatim. It appears exactly once at each of the 7 C-DISPATCH sites (R5-SITES reproduces, and my grep agrees). Deleting it fails only in the PR skill (F1). |

## Answers to §6

- **A1 (FMV-ORACLE-018/019/020). One new unauthorized change passes: duplicate keys (F2).**
  - FMV-ORACLE-018 reads each digest line anchored directly after its fence, and requires exactly
    three lines starting `source_row_sha256:`. Trailing text, uppercase hex, 65 hex characters, a
    swapped line (T6b) and a deleted line (T7) all fail.
  - FMV-ORACLE-019 checks each successor row's fields against its allowed set, and its neighbours.
    It falls back to the full id list, so any reordering is caught.
  - FMV-ORACLE-020 checks the key order, verbatim equality of the non-row keys, the in-place token
    replacement, and the exact authority key list plus the `successor_authority` literal.
  - Beyond F2, what passes is the inherent limit V-c and the prose limit V-d.
- **A2 (successor-oracle provenance). A third row cannot change unnoticed.**
  - Oracle `ede635b1…` (53 402 B), 46 rows, in the historical order. The 43 rows outside the set
    equal the historical rows in all 12 fields.
  - Exactly these fields differ, besides each row's `source_row_sha256`:
    - GCF-14: `consumes`;
    - GCF-17: `name`, `actor`, `session`, `failure_stop_condition`;
    - GCF-17.LINEAGE: `next`, `failure_stop_condition`.
  - The top-level keys that differ are exactly `authority`, `profile_id` and
    `required_global_tokens`.
  - The authority block is the five historical values unchanged, plus `successor_source_matrix_sha256`
    `8b443eb1…`, which equals the matrix bytes (3 653 B, byte-equal to the repository copy),
    `successor_rows` for the three ids, and `D23-D, D23-F; Product Owner 2026-09-23`.
  - Each `supersedes_source_row_sha256` equals the historical row digest.
  - Map `aa6ed8e3…` equals the projection of the oracle.
  - FMV-ORACLE-017: the regressions reproduce (G15).
  - The oracle regressions reproduce 15 of 15, including G1, the rule that catches a third-row change.
- **A3 (once-per-merge sentence and fallback literals).**
  - Missing at a C-DISPATCH site: none. Present once at each of the 7 sites.
  - Does deleting either fail? Only in `glow-hde-pr-development`; at the other 6 sites, no (F1).
  - No-dispatch path: none. The fallback stays usable whenever no `MERGE_OBSERVED` was returned.
  - Double-dispatch path: none left in any SKILL.md. Every C-DISPATCH site now voids the second
    entry. V-b notes two scenario and fixture texts that do not repeat the void clause.
- **A4 (the regenerator's contract-only value table). No wrong or stale value.**
  - `regenerate_contract.py acceptance` on the parts at `008418336` (before E1), with the baseline
    validator:
    - the stripped template (61 859 B, not a no-op) regenerates `2b78f877…`/606 657 B;
    - the negative control passes;
    - leave-one-out finds nothing that is not load-bearing.
  - `generate` from my own build of the branch parts reproduces the shipped contract byte for byte:
    613 162 B, `7a7fd028…`, revision 4.1.0. The copies in both skills are identical.
  - One value is unread (V-a).
- **A5 (reversed validator literals).**
  - `regress_skills` reproduces 70 of 70, `regress_contract` 53/53, 35/35 and 3/3, and
    `regress_fixtures` 2 of 2.
  - My own injections fail:
    - "same-session PR-35 handoff" in change-flow fails in the change-flow validator (retired
      clause), and in the relay fails as FMV-SKILL-STRUCTURE-001;
    - "launched as a new session" in `tw` fails as FMV-SKILL-STRUCTURE-001;
    - "one dedicated PR-development session" in the PR skill fails in the PR-skill validator.
  - Two phrases the relay and `tw` forbid are not forbidden in change-flow: "launched as a new
    session" and "The Product Owner's PR-40 invocation supplies merge approval". Injected there, they
    pass. The spec places those phrases only where the old text lived, so this is not a finding.
- **A6 (the GCFPE override and relay provisioning). Confirmed.**
  - The override paragraph is byte-identical at `change-flow:265`, relay `:257` and `tw:302`, and it
    is a `CONTRACT_REQUIRED` literal for each.
  - The embedded Flowmaster core block is identical to baseline in all three skills and to
    `flowmaster-primary`.
  - The relay's provisioning lines `:255` and `:717` are both scoped "Outside a GCFPE main-ecosystem
    stage".
- **A7 (the author's choices).**
  - G2 and G3 now expect FMV-ORACLE-018 beside 012 and 013. That follows necessarily: each mutates
    only the oracle row, so its digest no longer equals the untouched matrix line.
  - G11's four-finding set reproduces, and I accept it for the reasons SFR-A1-1 gave.
  - I found nothing in the §12 addendum items I checked that the bytes contradict, apart from the §2
    statement in F1.
- **A8 (contradictions with kept rules). None in the edited lines.**
  - The a1→a2 delta is the D23-E sentence, the alias prose and validator code.
  - That delta keeps: no agent merge ("No agent merges"), no polling ("stay subscribed and do not
    poll"), one handoff block, PR-40's independent verification, and one Proceed per plan.
- **Question, is anything outside the scope? No.**
  - `diff -rq` of the a1 extracts against the a2 extracts touches exactly the repair sites: the
    D23-E sentence at 7 sites, `flowmaster-validate/SKILL.md` lines 9, 157, 173, 212 and 382,
    `validate_flowmaster.py` (FMV-ORACLE-018/019/020 and the fixture message), and the PR validator's
    three literals.

## Claims C1–C8

- **C1 holds.**
  - `diff -rq` of the installed tree against the extracts gives 26 changed files and 3 new ones (the
    successor oracle, map and matrix). All are §5, §6, §8a or §8b sites or a1 repair sites.
  - The historical oracle `52807e58…`, the historical map `5574666e…`, the correction layers and the
    alias contracts are byte-unchanged.
  - The 12 historical-layer outputs are byte-equal to baseline.
- **C2 holds** (see A4). `validate_graph_contract` returns `[]` and `validate_contract` returns `[]`.
- **C3 holds.** The routing surface is `fecc319bdd4ce7ee6201cb77d7231861`/284 (baseline
  `7380cd14…`/282).
- **C4 holds**, subject to F1 for guards added by a1.
- **C5 holds.** No line added to any of the six skills instructs creating, launching or scheduling a
  session, or running a prompt as a subagent. Every match is a prohibition or a Nathan-created
  session.
- **C6 holds for rows, fields, positions and keys** (A2), except for F2.
- **C7:** partly verified. See "Gates" below.
- **C8 does not hold as stated** (F1).

## Measurements

- **Baseline (§3).** Measured at start and end on byte copies (`cp -a`) of the synced tree:
  `b9ca212a…`/29, `80e877c2…`/21, `e109d47a…`/4, `4ef8daa3…`/5, `6cd088a0…`/15, `fa3fac85…`/2, all
  equal to spec v2 §2 in full. The harness refused to run `freeze.py` directly against the synced
  directory, so I measured copies of it.
- **Packages (§8a).**
  - All sizes, sha256 values and entry counts match §1.
  - Every entry is a regular file under its own skill root: no `..`, no absolute path, no backslash,
    no symlink, no duplicate.
  - `name:` is unchanged in all six SKILL.md files.
  - Extracted freeze digests: `a00cccbf…`/31, `1186283d…`/22, `6382ead5…`/4, `15aef989…`/5,
    `87201ab5…`/15, `fd6c344b…`/2, all as the brief states.
- **Graph.** `graph_parts.py build` of the branch parts gives 55 nodes, 229 edges and 575 074 B,
  `ae2bd159…`. This is byte-identical to the graph bundled in both skills, and it is the `<root>` I
  used.
- **Hash pins (§8e).** Every 64-hex value the diff adds resolves to an artifact in the set:
  - oracle `ede635b1` ×8 files;
  - map `aa6ed8e3` ×5;
  - graph `ae2bd159` ×5;
  - matrix `8b443eb1` ×3;
  - contract `7a7fd028` ×2;
  - fixtures `c433aa09` ×2;
  - row digests;
  - `SKILL_TREE_SHA256` `9c48d9f4…`, which equals `skill_tree_digest`, with `self_identity` OK.

  Two values are carried unchanged from the historical authority (`faa7fb7d`, `5a6d89ed`).
  No live site carries `2b78f877`, `90021eb7`, `a1a73062` or `eb9634d6`. `52807e58` and `5574666e`
  remain only at historical sites.
- **Revisions (§8f, counted by grep):**
  - PR skill 1.3.0: SKILL.md, its validator, the contract's `primary_skill_revision` in both copies,
    the profile, and two validator sites;
  - change-flow 3.3.0: SKILL.md, its validator, the profile, `validate_gcfpe_current` ×2, and
    `validate_flowmaster` ×2;
  - relay 3.1.0 ×2;
  - `tw` 1.2.0 ×2;
  - amthor 1.12.0 ×2;
  - `validator_revision` 3.3.0 ×4, plus `FLOWMASTER_VALIDATE_REVISION`.

  `validate_gcfpe_current.py:305` keeps the historical 1.2.0 of the v3 alias, as in baseline.
- **Once-per-merge sites (independent grep):** the 7 C-DISPATCH sites listed under F1, plus
  `glow-hde-pr-development/SKILL.md:111`, each exactly once.

## Gates actually run

Every run used a full scratch copy of the synced tree with the six skills replaced, with
`PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside my scratch. I read each tool's own top-level flag.

| command | result |
|---|---|
| `validate_flowmaster.py --skills-root <copy>` | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, 0 findings, 46/46 rows exact |
| same, with `--strict-warnings --gcfpe-contract … --gcfpe-candidate-root <root>` | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, 0 findings of any severity |
| `validate_gcfpe_20260914.py <cf> --contract …` | `"ok": true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py <cf> --contract …` | `fixture_suite_ok: true`, 228 cases, 0 failing, section 13 37/37 and 38/38 |
| `validate_gcfpe_current.py <cf>` | `"ok": true` |
| `run_gcfpe_current_fixtures.py <cf>` | `fixture_suite_ok: true`, 228 |
| `run_change_flow_fixtures.py` | `fixture_suite_ok: true`, 32/32, 0 failed |
| `<cf>/scripts/validate_gcfpe_20260914.py` | PASS, exit 0 |
| `validate_glow_hde_pr_development.py` | PASS |
| `validate_relay_manifest.py --self-test` | `status: PASS`, 230 cases, 0 failed |
| amthor `run_fixture_suite.py` | 34 tests OK |
| `validate_project_prompt_registry.py` on the branch registry | `{"valid": true, "problems": []}` |
| the 12 historical-layer commands of spec v2 §2 | all exit 0; stdout and stderr byte-equal to the same commands on an unmodified baseline copy |
| the author's regressions, re-pathed into my scratch | oracle 15/15; a1 repair 17/17; skills 70/70; contract 53/53, 35/35, 3/3; fixtures 2/2 |
| `regenerate_contract.py acceptance` and `generate` | as under A4 |
| my probes: `probe.py` (P1–P7), `probe2.py` (18 deletions), `probe3.py` (9 injections), a contract-revert sweep (31 paths) | as reported above |

**Not run, plainly:**
- `run_e4.py` and `body_rules.py`. These are optional under L1 and need Notion bodies. I did not
  re-verify C7's E3/E4 items; I read `E3-E4-report.md` revision 4 only.
- `route_sim_final.py`. I verified its product, `fecc319b…`/284, from the contract and the graph
  build directly.
- `build_r1_successor.py`, `e1_*.py`, `g16_graph.py`, and the `run_e2.sh` and `run_repair_a1.sh`
  wrappers. These write to repository or fixed `/tmp` paths. I ran re-pathed copies of the regression
  scripts they call instead.
- `closure.py`.

## DECISION NEEDED

F1 needs a choice before repair:
- **(a)** Add the two literals to the change-flow, relay and `tw` `CONTRACT_REQUIRED` lists, as §2
  states. This is my recommendation, and it can take F2 in the same edit.
- **(b)** Accept PR-skill-only guarding and restate §2 and C8 in a successor brief.

Either way, the changed packages need a fresh review against their new digests.
