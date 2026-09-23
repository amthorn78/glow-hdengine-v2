---
artifact_type: SKILL_FIT_REVIEW
reviewer: SFR-A2-1
round: a2 (after repair round a1)
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a2.md, commit 9c49a65, 14883 B, sha256 67b7215e6db6e355caa7c0fa8d084099e75bd43079d6b9390b8b8ad4cd1d00d3 (verified at the working tree and at the commit)
repository_head_reviewed: 9c49a65e8c44e36f90eac0d988b0a3b34c06d8c9 (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged)
date: 2026-09-23 (UTC)
supersedes: nothing. This is a successor record. It does not edit the round-a1 records (AUTH-001).
---

# Section 10 review, round a2 — SFR-A2-1

## Verdict

**SKILL_REPAIR_REQUIRED**

The verdict applies only to these six packages, by these digests, in /tmp/claude-0/pkg2/new/:

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54461 | 9d5308e67ac91535c6b3184a0e13dd8cc5fca278ec66e660aceaab6bfae7b079 |
| change-flow.skill | 22 | 257909 | 97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0 |
| flowmaster-validate.skill | 31 | 315534 | 5ffa13f101db9108cdec356ce638ee0d67fa4c8a5eb2f7952bc13a2e220d3db4 |
| glow-hde-pr-development.skill | 4 | 22414 | 3292e348febe0136f1d4b6768238be95e2b7b3e529c00595fcf14366016b1d6a |
| session-relay-flowmaster.skill | 5 | 56330 | 30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b |
| tw-flowmaster.skill | 2 | 20368 | db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf |

It is void for any other bytes. I measured every value in the table myself from the archives.

**Why the verdict is repair.** Two findings block the set.
- **R2-1:** the round-a1 V2 disposition that §2 of the brief records is not in these bytes. §2 says the fallback predicate became a required literal "in validate_glow_hde_pr_development.py and the relay/tw CONTRACT_REQUIRED lists". The relay and tw lists do not carry it. The same gap applies to the once-per-merge sentence: deleting it passes every suite at six of its seven sites.
- **R2-2:** a re-stamped change to the *value* of an allowed successor field still passes. For example, GCF-17 `session` can be rewritten to allow a subagent PR-35 and every suite stays green.

Everything else the brief claims reproduced on these bytes: the pins, parity, the routing surface, the historical layer, and all 32 of the author's regressions.

## Stability and baseline

- **Baseline.** freeze.py on the installed synced tree gave exactly the six spec v2 §2 values at the start of the review, and again at the end: flowmaster-validate 29 b9ca212a…, change-flow 21 80e877c2…, PR skill 4 e109d47a…, relay 5 4ef8daa3…, amthor 15 6cd088a0…, tw 2 fa3fac85…, and glow-graph-contract 6 4e671ddc…. The package digests and the repository HEAD were also unchanged at the end. The tree did not move while I reviewed.
- **Extracted a2 trees.** freeze.py gave flowmaster-validate 31 a00cccbf…, change-flow 22 1186283d…, PR skill 4 6382ead5…, relay 5 15aef989…, amthor 15 87201ab5… and tw 2 fd6c344b…. All six match §3.
- **Archive hygiene.** Every entry sits under its skill root. There are no directory entries, `..` segments, absolute paths, backslashes or symlinks. The file counts match §1. The `name:` line of every SKILL.md is unchanged.

## Gates I ran

All runs used a full scratch copy of the synced tree with the six skills replaced (`/tmp/claude-0/review-SFR-A2-1/copy`), with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside my scratch. `<root>` holds only the embedded JSON of a graph_parts.py build of the branch's docs/graph/parts: 575074 B, sha256 ae2bd159…, 55 nodes, 229 edges, 55 state_routes. That build is byte-identical to the graph bundled in both packages.

| command | result |
|---|---|
| validate_flowmaster.py --skills-root | exit 0, suite_ok true, FLOWMASTER_SUITE_PASS, 0 findings, self_identity OK |
| the same with --strict-warnings, the contract and the candidate root | exit 0, suite_ok true, FLOWMASTER_SUITE_PASS, 0 findings |
| validate_gcfpe_20260914.py (fv) with the contract | ok true, errors [], contract 7a7fd028…, frozen graph ae2bd159… |
| run_gcfpe_20260914_fixtures.py | fixture_suite_ok true, 228 cases, 0 failed, §13 37/37 and 38/38 |
| validate_gcfpe_current.py | ok true |
| run_gcfpe_current_fixtures.py | fixture_suite_ok true, 228 cases |
| run_change_flow_fixtures.py | fixture_suite_ok true, 32/32, 0 expectation failures |
| change-flow/scripts/validate_gcfpe_20260914.py | exit 0, PASS |
| validate_glow_hde_pr_development.py | exit 0, PASS |
| validate_relay_manifest.py --self-test | status PASS, 230 cases, 0 not ok |
| amthor run_fixture_suite.py | 34 tests OK |
| amthor validate_project_prompt_registry.py on the branch registry | valid true, problems [] |
| the 12 historical-layer commands of spec v2 §2, on the baseline copy and on the a2 copy | all exit 0. stdout, stderr and exit code are byte-equal after normalizing the two scratch root paths |

**Regenerator.**
- `regenerate_contract.py acceptance` on the parts at merge-base a63bf801 reproduces today's contract byte for byte, 2b78f877…/606657 B. The stripped template's digest differs from the target, so the test is not a no-op. The negative control passes and leave-one-out is empty.
- One condition: acceptance must be run with the *baseline* validator scripts. With the a2 scripts, the negative control reports false, because the new validator expects the successor pins. That is expected, but the script does not say so.
- `generate` from my graph build reproduces the shipped contract exactly: 613162 B, 7a7fd028…. On it, validate_graph_contract returns [], validate_contract returns [], and routing_surface returns fecc319bdd4ce7ee6201cb77d7231861/284.

**Pins.** I recomputed each one from its artifact.
- **Successor oracle:** 53402 B, ede635b1…. It is pinned at validate_flowmaster.py:38, at three literals in validate_gcfpe_20260914.py, in the profile, and in both the graph and the contract `protected_identities`.
- **Successor map:** 46326 B, aa6ed8e3…, pinned at five sites.
- **Matrix:** 3653 B, 8b443eb1…. It equals `authority.successor_source_matrix_sha256`, and the repository copy is byte-identical.
- **Contract:** 7a7fd028…/613162 B, matching the profile and EXPECTED_CANDIDATE_CONTRACT_BYTES.
- **Graph:** ae2bd159…/575074 B, matching the profile, EXPECTED_GRAPH_SHA and the contract's source_snapshot.
- **Fixtures:** c433aa09…, 37 cases.
- **SKILL_TREE_SHA256:** 9c48d9f4…, equal to skill_tree_digest.
- **Historical files:** the oracle 52807e58… and the map 5574666e… are unchanged.

**Oracle content.** The successor oracle has 46 rows in the historical order. The only differences from the historical oracle are `profile_id`, the in-place token replacement, the three appended authority keys, and the ten A1-1 row fields. The row values equal spec §5.3, and each `source_row_sha256` follows the formula. The map equals the §5.6 projection of the oracle.

**Changed files.** Derived with diff -rq: 26 files differ and 3 files are new. Every one is named by spec v2 §5, §6, §8a or §8b, or by the a1 repair script. No historical file differs.

**The author's regressions, re-run on these bytes.** I copied the scripts into my scratch and changed only their path constants.
- regress_repair_a1.py: `A1_REPAIR_REGRESSIONS 17 of 17 exact`.
- regress_oracle.py: `ORACLE_REGRESSIONS 15 of 15 exact`. This includes G2 and G3 with 018 and G11's four-finding set.

**Gates I did not run.**
- run_e4.py (E3/E4). The bodies live in Notion, and the brief marks it optional.
- run_e2.sh and run_repair_a1.sh as whole scripts, because they write outside my scratch. I ran their regression components instead.
- Any post-install check. Nothing is installed.

## My own probes

The oracle probes (`probes/oracle_probes.py`) use the full re-stamp of regress_repair_a1.py: oracle and map, graph and contract `protected_identities`, the validator literals, the profile, SKILL_TREE_SHA256, and the matrix digest in `authority`. Each probe runs both suites.

**Must-fail probes, all caught:**
- **M1:** GCF-14 `produces` changed in both the oracle and the matrix, with the digest recomputed. Caught by FMV-ORACLE-019 on row GCF-14. FMV-GCF-OUTPUT-001 also fired, because of the artifact name I chose.
- **M2:** an entry added to `special_destinations`. Caught by FMV-ORACLE-020.
- **M3:** a fourth `source_row_sha256:` line in the matrix header. Caught by FMV-ORACLE-018.
- **M4:** a blank line between a block and its digest line. Caught by FMV-ORACLE-018.
- **M5:** authority keys reordered. Caught by FMV-ORACLE-020.
- **M6:** the new profile id moved to the end of `required_global_tokens`. Caught by FMV-ORACLE-020.
- **M7:** GCF-17 and GCF-17.LINEAGE swapped. Caught by FMV-ORACLE-019.

**Gap probes: each passed both suites with 0 findings.**
- **P1:** GCF-17.LINEAGE `next` gains GCF-16, consistently in the oracle and the matrix.
- **P2:** GCF-17 `session` changed to "…or a subagent of the PR-30 session.", consistently.
- **P3:** the matrix blocks reordered, with GCF-17 first.
- **P4:** a fourth fence, tagged ```` ```JSON ````, holding a fake GCF-16 block.
- **P5:** the key order reversed inside kept row GCF-16.

**Text probes** (`probes/textprobe.py`, `probes/inject.py`). Each probe deletes or injects one literal, re-stamps SKILL_TREE_SHA256 where needed, and runs all ten live suites.

Once-per-merge sentence deleted:

| site | result |
|---|---|
| glow-hde-pr-development/SKILL.md | caught |
| change-flow/SKILL.md | passes every suite |
| session-relay-flowmaster/SKILL.md | passes every suite |
| tw-flowmaster/SKILL.md | passes every suite |
| flowmaster-validate/SKILL.md | passes every suite |
| amthor-workspace-governance-audit/SKILL.md | passes every suite |
| amthor-workspace-governance-audit/references/interoperability-contracts.md | passes every suite |

The fallback predicate "only where no `MERGE_OBSERVED` result was returned for this merge", deleted:
- **Caught:** glow-hde-pr-development/SKILL.md.
- **Passes every suite:** change-flow, relay, tw, flowmaster-validate/SKILL.md, amthor SKILL.md, interoperability-contracts.md, behavior-cases.md and behavioral-fixtures.md.

Other text probes:
- **Retired phrases injected, 14 cases, all caught.** Four phrases each in tw and the relay; three PR-skill phrases; three change-flow phrases.
- **Override edited:** removing "schedules" from the override is caught in all three skills.
- **Relay scope phrase deleted:** "Outside a GCFPE main-ecosystem stage," deleted at relay :255 or at :717 passes every suite.

## Findings

### R2-1 (blocking): the round-a1 V2 disposition is not implemented beyond the PR skill; the once-per-merge sentence is guarded at one of seven sites
- **Artifacts:** flowmaster-validate/scripts/validate_flowmaster.py (`CONTRACT_REQUIRED` for "session-relay-flowmaster", "tw-flowmaster" and "change-flow"); claims C8 and §2 (V2, F3).
- **Defect.** §2 records V2's disposition as "required literals in validate_glow_hde_pr_development.py and the relay/tw CONTRACT_REQUIRED lists".
  - Neither the relay nor the tw list contains the predicate. `grep MERGE_OBSERVED validate_flowmaster.py` returns nothing.
  - apply_repairs_a1.py edits only the PR-skill validator.
  - C8 says the once-per-merge sentence "is a required literal". It is required only in glow-hde-pr-development.
- **Evidence.** See the text probes above. Deleting the predicate, or the whole once-per-merge sentence, from the relay, tw, change-flow, flowmaster-validate or amthor texts passes all ten live suites. R5-SITES checks only that the sentence is present on these bytes; nothing requires it to stay.
- **Smallest correction.**
  - Add both literals to `CONTRACT_REQUIRED["session-relay-flowmaster"]` and `["tw-flowmaster"]`, which is what §2 already states. Add them to `["change-flow"]` or to the change-flow validator's required skill clauses.
  - Add one deletion regression per skill.
  - For the flowmaster-validate and amthor texts, either add equivalent literals or record in §2 that those sites are unguarded.
  - The alternative, correcting §2 and C8 to say only the PR skill is guarded, would leave four of the seven C-DISPATCH sites free to lose the D23-E rule silently.

### R2-2 (blocking): the values of the allowed successor fields are not pinned under the full re-stamp
- **Artifacts:** validate_flowmaster.py, `successor_oracle_findings` (FMV-ORACLE-012/013/018/019); claim C6; attack items A1 and A2.
- **Defect.** FMV-ORACLE-019 restricts *which* fields of GCF-14, GCF-17 and GCF-17.LINEAGE may differ from history. The *values* of those fields are bound only by a chain the re-stamp moves: the matrix block, its digest line, the matrix digest in `authority`, and then the oracle pins. Nothing independent of the re-stamp holds the approved A1-1 values.
- **Evidence.**
  - P2 passes both suites with 0 findings. That rewrite of GCF-17 `session` contradicts C-SESSION and the kept rule that PR-35 is never a subagent.
  - P1 passes too. It adds an unapproved re-plan destination to GCF-17.LINEAGE `next`.
  - The historical comparison survives the re-stamp only because HISTORICAL_ORACLE_SHA256 is not among regress_oracle's substituted pairs. The successor values have no pin like that.
- **Smallest correction.**
  - Add a constant mapping the three row ids to their approved digests in validate_flowmaster.py: GCF-14 42db7a9e…, GCF-17 67745290…, GCF-17.LINEAGE 73a133c1…. Require each oracle row's `source_row_sha256` to equal it, under a new code or FMV-ORACLE-019.
  - The re-stamp model substitutes only file digests, so this pin holds.
  - Add P1 and P2 as must-fail regressions.

### R2-3 (minor, non-blocking): the matrix and row layout rules of §5.3/§5.4 are not enforced
- **Artifacts:** FMV-ORACLE-011 and FMV-ORACLE-015/019.
- **Defect:** three layout rules are unchecked:
  - blocks "in oracle row order" (P3 passes; 011 compares sorted ids);
  - "the file has no other JSON fence" (P4 passes; only lower-case ```` ```json ```` fences are counted);
  - "the key order in every object" is copied verbatim (P5 passes; row comparison is dict equality).
- **Effect:** none on the shipped bytes, which conform. The rules are unguarded under re-stamp.
- **Smallest correction:**
  - compare the block id list to `SUCCESSOR_ROWS` in order;
  - count every line that opens a code fence;
  - compare `list(row)` with `list(history_row)`.

### R2-4 (minor, non-blocking): the contract-only value `historical_non_executable_references` is unchecked
- **Artifact:** the §6.3 value table, and validate_gcfpe_20260914.py (both copies).
- **Defect:** 25 of the 26 value-table entries are guarded by validate_contract or validate_graph_contract. I tested this by mutating every leaf. This entry is checked only for key presence.
- **Evidence:** each of the following returns [] from both functions on the regenerated contract:
  - removing either new historical filename;
  - appending the *live* successor oracle's filename to the list.
- **Smallest correction:** an exact-value check in validate_contract.

### R2-5 (minor, non-blocking): the relay's GCFPE scoping of SESSION_PROVISIONING_REQUIRED is unguarded
- **Artifact:** session-relay-flowmaster/SKILL.md :255 and :717; `CONTRACT_REQUIRED["session-relay-flowmaster"]`.
- **Defect:** deleting "Outside a GCFPE main-ecosystem stage," at either line passes every suite. The unscoped sentence would send a GCFPE stage to Session Branch Flowmaster, against the override that follows it.
- **Smallest correction:** a required literal and one deletion regression.

A code-reading note, not measured, so not a finding: `FMV-GCF-MAP-005` compares only `profile_id`, `authority` and `coverage` besides the rows. An extra top-level key in the successor map would be caught only by the re-stampable digest, MAP-006. That logic predates this change.

## Answers to §6

- **A1.** 018, 019 and 020 hold against everything I tried outside the allowed field sets (M1–M7). A re-stamped unauthorized change can still pass through the values of the allowed fields (R2-2), and through layout (R2-3).
- **A2.** Provenance reproduces:
  - The matrix bytes and header match the §12 addendum.
  - The formula reproduces all three digests, and the `supersedes` values equal the historical digests.
  - The authority block is §5.5 exactly.
  - N10 and FMV-ORACLE-017 behave as specified (G14, G15).

  A third row cannot change unnoticed: G1 is caught by 015, G7 by 010, and M7 by 019. A change to a value inside the three rows can, as R2-2 shows.
- **A3.**
  - **Presence:** the once-per-merge sentence and the predicate are present at every site that carries the full C-DISPATCH text. I found seven such sites by grepping for "The observed merge event is the fact PR-40 is entered on"; they match the author's list. The fallback-only sites carry the predicate without the sentence: PR SKILL :176, behavior-cases :87/:123, change-flow :355/:457, and amthor behavioral-fixtures. That is consistent with "sites that carry C-DISPATCH".
  - **Deletion:** deleting either fails only in the PR skill (R2-1).
  - **Double or no dispatch:** I see no double-dispatch path left in the text. "Once either has been pasted, the other is void" closes the race between a late `MERGE_OBSERVED` and an already-pasted fallback. I also see no no-dispatch path: without an active subscription, the fallback remains.
- **A4.** The regenerator's table is correct against spec §6.3. `generate` reproduces the shipped contract, and acceptance reproduces 2b78f877 with the baseline validator. One value is read by no check (R2-4).
- **A5.** Every retired phrase I injected is caught: 14 cases across tw, the relay, the PR skill and change-flow. The replacement literals exist, and the author's regress_skills set passes. I did not re-inject every reversed literal of §8b.7 individually.
- **A6.**
  - **Override text:** the override is present verbatim in change-flow :265, relay :257 and tw :302, outside the byte-identical core.
  - **Override guard:** it is held by `CONTRACT_REQUIRED` in all three skills. Deleting "schedules" is caught.
  - **Relay provisioning lines:** :255 and :717 are scoped outside GCFPE stages. The scoping phrase itself is unguarded (R2-5).
- **A7.**
  - **G2/G3:** the expected sets gain 018 because the untouched matrix line no longer equals the recomputed or altered oracle digest. That reasoning is correct, and both runs reproduce it.
  - **G11:** its four-finding set reproduces.
  - **§12 and the addendum:** the choices I checked are applied as written: the matrix header and spacing, U-6's ordering, U-8b-1's wording, and the S-7 placement. I found no conflict with a kept rule. Not every §12 line was re-derived.
- **A8.** I found no edited line that contradicts a kept rule. No agent merges; it is required in the PR skill and the contract. There is no polling: "stay subscribed and do not poll". The one-handoff-block rule, PR-40's independent verification, and one Proceed per plan are required literals in the PR skill and the change-flow validator.

  The one way to *introduce* such a contradiction without a failing check is R2-2's field rewrite, or the deletions in R2-1 and R2-5.
- **Scope question.** Every changed file traces to spec v2 §5, §6, §8a or §8b, the a1 repairs, or D23-E. I saw nothing outside them.

## Round-a1 findings on these bytes

- **F1 (both reviewers), missing matrix digest-line check:** closed. FMV-ORACLE-018 is present, T6, T6b and T7 reproduce, and my M3 and M4 are caught.
- **SFR-A1-1 F2 and SFR-A1-2 V1, re-stamped changes to non-allowed fields, positions and non-row keys:** closed for that scope. T1, T3, T3b, T3c and T5 reproduce, and M1, M2 and M5–M7 are caught. The residual on allowed-field values is new finding R2-2, not a reopening.
- **SFR-A1-2 V2, fallback predicate without a skill-text guard:** not closed as §2 states. It is closed in glow-hde-pr-development only; the relay and tw lists were not changed (R2-1).
- **SFR-A1-2 V3, stale alias prose:** closed. The three stale phrases are absent from flowmaster-validate SKILL.md and validate_flowmaster.py, and the evidence text reads "current-overlay fixture suite failed".
- **SFR-A1-1 F3, double PR-40 dispatch:** closed in text at all seven C-DISPATCH sites, with the sentence verbatim from the D23-E record. Its guard exists only in the PR skill (R2-1).

## Scratch

All work is under /tmp/claude-0/review-SFR-A2-1/: pkg/ holds the archive copies, ext/, base/ and copy/ the trees, root/ the candidate root, out/ and hist/ the suite outputs, regen/ the regenerator runs, and probes/ my probe scripts. This record is the only repository write. Nothing was installed, committed or pushed, and the synced skills directory was not written.

DECISION NEEDED
