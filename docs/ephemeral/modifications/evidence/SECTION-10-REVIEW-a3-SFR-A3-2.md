---
artifact_type: SKILL_FIT_REVIEW
reviewer: SFR-A3-2
round: a3 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a2)
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a3.md, commit c22bc64, 16580 B, sha256 c29a5a8b09fbbb297d4ffd86eddbde01aa0aa3374e8c69b52bd14cdc2e1d7af5 (verified at the working tree and at the commit's blob)
repository_head_reviewed: c22bc64280000d6cf4ca68d5348636a79f91896a (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged), the same at the start and the end
reviewed_at_utc: 2026-09-23T10:22Z
scratch: /tmp/claude-0/review-SFR-A3-2/
supersedes: nothing. This is a successor record. It does not edit the round-a1 or round-a2 records (AUTH-001).
---

# Section 10 review, round a3 — SFR-A3-2

## Verdict

**SKILL_FIT_CONFIRMED**

The verdict applies only to these six packages, installed together as one set, as they sat in
`/tmp/claude-0/pkg3/new/`. I measured every value in the table myself from those archives. **The
verdict is void for any other bytes.** No earlier confirmation or measurement carries to these bytes.

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54899 | `0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7` |
| change-flow.skill | 22 | 257909 | `97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0` |
| flowmaster-validate.skill | 31 | 317639 | `e8eeda442162081257e6a75e08813d7f4707213c5acbb2fa171505b8544ae766` |
| glow-hde-pr-development.skill | 4 | 22494 | `dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913` |
| session-relay-flowmaster.skill | 5 | 56330 | `30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b` |
| tw-flowmaster.skill | 2 | 20368 | `db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf` |

**Why fit.** Every round-a2 finding is closed on these bytes as brief §2 states, and I found no
blocking defect.
- All the gates of brief §8 pass. The historical layer is byte-equal to baseline.
- All 191 of the author's regressions reproduce exactly.
- My own must-fail probes against FMV-ORACLE-021, the duplicate-key rule and the runtime-map
  `.get()` fail as they should.

**Three residuals, none blocking.** I record them as minor findings so they are not lost:
- **A3-1:** the "no other code fence" half of FMV-ORACLE-022 misses container-nested fences.
- **A3-2:** FMV-GCF-DISPATCH-001 pins counts, not positions.
- **A3-3:** the contract's routing edges do not carry the D23-E void clause.

None of them changes a bound value or a runtime route. None contradicts a claim in brief §5, except
the one word "no other code fence" in §2's S4(a), which A3-1 qualifies.

## Stability and baseline

- **Baseline.** I ran freeze.py on the installed synced tree at the start and at the end (10:22Z).
  Both times it gave exactly the spec v2 §2 values:

  | skill | files | digest |
  |---|---|---|
  | flowmaster-validate | 29 | `b9ca212a…` |
  | change-flow | 21 | `80e877c2…` |
  | glow-hde-pr-development | 4 | `e109d47a…` |
  | session-relay-flowmaster | 5 | `4ef8daa3…` |
  | amthor-workspace-governance-audit | 15 | `6cd088a0…` |
  | tw-flowmaster | 2 | `fa3fac85…` |

  The package digests and the repository HEAD were also unchanged at the end. The tree did not move.
- **Extracted a3 trees.** freeze.py gives exactly the values in brief §3:

  | skill | files | digest |
  |---|---|---|
  | flowmaster-validate | 31 | `cb7e1693…` |
  | change-flow | 22 | `1186283d…` |
  | glow-hde-pr-development | 4 | `68077fa6…` |
  | session-relay-flowmaster | 5 | `15aef989…` |
  | amthor-workspace-governance-audit | 15 | `819915e4…` |
  | tw-flowmaster | 2 | `fd6c344b…` |

- **Archive hygiene.**
  - Every entry sits under its own skill root.
  - There is no `..` segment, no absolute path and no symlink entry. No symlink was created on
    extraction.
  - The file counts match §1.
  - `name:` in every SKILL.md frontmatter is unchanged from the installed tree.

## Gates I ran

**Setup.** Every run used a full scratch copy of the synced tree with the six skills replaced
(`copy/`), with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside my scratch. `<root>` holds only the
embedded JSON of a `graph_parts.py build` of the branch's `docs/graph/parts`:
- 55 nodes, 229 edges, 55 state_routes;
- 575074 B, `ae2bd159…`;
- byte-identical to the graph bundled in both change-flow and flowmaster-validate.

I read each tool's own top-level flag by name.

| command | result |
|---|---|
| `validate_flowmaster.py --skills-root` | exit 0, `suite_ok` true, `FLOWMASTER_SUITE_PASS`, 0 findings of any severity, `self_identity` OK, oracle profile `GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1` |
| the same with `--strict-warnings`, the contract and `<root>` | exit 0, `suite_ok` true, `FLOWMASTER_SUITE_PASS`, 0 findings, 0 warnings |
| `validate_gcfpe_20260914.py <cf> --contract …` | `ok` true, `errors` [] |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` true, 228 cases, §13 37/37 and 38/38, validator_revision 3.3.0 |
| `validate_gcfpe_current.py` | `ok` true, `errors` [] |
| `run_gcfpe_current_fixtures.py` | `fixture_suite_ok` true, 228 cases |
| `run_change_flow_fixtures.py` | `fixture_suite_ok` true, 32/32, 0 failed expectations |
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit 0, PASS |
| `validate_glow_hde_pr_development.py` | exit 0, PASS |
| `validate_relay_manifest.py --self-test` | `status` PASS, 230 cases |
| amthor `run_fixture_suite.py` | 35 tests, OK |
| amthor `validate_project_prompt_registry.py` on the branch registry | `{"valid": true, "problems": []}` |
| the 12 historical-layer commands of spec v2 §2, on a baseline copy and on the a3 copy | all exit 0. stdout and stderr are byte-equal after normalising the two scratch roots. The flags are `ok`/PASS/`fixture_suite_ok` true |

**Regenerator (§6).**
- `regenerate_contract.py generate` from my graph build reproduces the shipped contract byte for
  byte: 613162 B, `7a7fd028…`. The template was the installed contract.
- `acceptance` on the parts at merge-base `a63bf801`, with the baseline validator, gives:
  - the stripped template: 61859 B, `8e49c365…`, not the target (so the test is not a no-op);
  - the regenerated contract: `2b78f877…`/606657 B;
  - `validate_graph_contract` [] and `validate_contract` [];
  - negative control PASS, and leave-one-out empty.
- On the shipped contract, with the a3 validator:
  - `validate_graph_contract(contract, graph)` returns [];
  - `validate_contract` returns [];
  - `routing_surface` returns `fecc319bdd4ce7ee6201cb77d7231861`/284.

**The author's regressions, re-run on these bytes.** I derived them with `derive_regressions_a2.py`
into my scratch, re-pathed only the `/tmp/claude-0/repair2` constants, and ran them against `copy/`
and `<root>`:

| harness | result |
|---|---|
| oracle | `ORACLE_REGRESSIONS 15 of 15 exact` |
| skills | `SKILL_REGRESSIONS 70 of 70 exact` |
| contract | `53 of 53`, `35 of 35`, `3 of 3` exact |
| fixtures | `2 of 2` |
| a1 repair | `A1_REPAIR_REGRESSIONS 17 of 17 exact` |
| a2 repair | `A2_REPAIR_REGRESSIONS 34 of 34 exact`: U1–U8 with U7b, C0–C3, R-RELAY-255/717, and all 18 D-* cases |

This agrees with the author's measurements; I found nothing to contradict them.

**Not run, plainly.**
- `run_e4.py` and `body_rules.py` (E3/E4). They are optional under L1 and need Notion bodies. I read
  only the header of E3-E4-report.md revision 5. I did not re-verify C7's E3/E4 items.
- `run_repair_a2.sh`, `run_e2.sh`, `build_r1_successor.py`, `e1_*.py`, `route_sim_final.py`,
  `closure.py`. They write outside my scratch, or their product I verified directly: the routing
  surface from the contract, and the oracle and matrix from their bytes.
- Any post-install check. Nothing is installed (L2).

## Content checks (§8 c–f)

- **(c) Changed files.** I derived the list with `diff -rq` against the installed tree:
  - 26 files differ and 3 are new: the successor oracle, the successor map and the matrix.
  - The list is identical to the base→a2 list. Repair a2 touched only files already in it.
  - Every file traces to spec v2 §5, §6, §8a or §8b, or to the a1/a2 repair scripts.
  - The a2→a3 delta is exactly seven files:
    - flowmaster-validate `SKILL.md` (only `SKILL_TREE_SHA256`), `validate_flowmaster.py` and
      `validate_gcfpe_20260914.py`;
    - the PR skill's `behavior-cases.md` and its validator;
    - amthor `behavioral-fixtures.md` and `run_fixture_suite.py`.
  - change-flow, the relay and tw are byte-identical to a2, as §1 states.
- **(d) Rosters.**
  - The successor oracle has 46 rows, in the historical id order.
  - Only GCF-14 (`consumes`), GCF-17 (`name`, `actor`, `session`, `failure_stop_condition`) and
    GCF-17.LINEAGE (`next`, `failure_stop_condition`) differ from the historical rows, each also in
    `source_row_sha256`.
  - The top-level keys that differ are exactly `profile_id`, `authority` and
    `required_global_tokens`.
  - The map equals the projection of the oracle, and parity holds (above).
- **(e) Pins, recomputed from each artifact.**

  | artifact | size | sha256 | consumers |
  |---|---|---|---|
  | successor oracle | 53402 B | `ede635b1…` | validate_flowmaster.py, validate_gcfpe_20260914.py (fv), the profile, flowmaster-validate SKILL.md, and `protected_identities` in the graph and contract of both skills |
  | successor map | 46326 B | `aa6ed8e3…` | five sites, including the profile and change-flow SKILL.md |
  | matrix | 3653 B | `8b443eb1…` | equals `authority.successor_source_matrix_sha256`; byte-equal to `docs/prompt_ecosystem_management/r1-successor-source-20260923.md` |
  | contract | 613162 B | `7a7fd028…` | the profile and `EXPECTED_CANDIDATE_CONTRACT_*` |
  | graph | 575074 B | `ae2bd159…` | the profile, `EXPECTED_FROZEN_GRAPH_*`, both validators and the contract's snapshot |
  | fixtures | — | `c433aa09…` | the profile and `EXPECTED_FIXTURE_SHA256` |
  | historical oracle | — | `52807e58…` | unchanged |
  | historical map | — | `5574666e…` | unchanged |

  - `SKILL_TREE_SHA256` `82505ca8…` measures equal: `self_identity` OK.
  - No live site carries `2b78f877`, `90021eb7`, `eb9634d6` or the a2 tree stamp `9c48d9f4`.
  - **Row digests.** I recomputed the three successor row digests with the §5.4 formula from three
    sources: the oracle rows, the matrix blocks, and the spec v2 §5.4 blocks. All three agree with
    each other and with the matrix digest lines and `SUCCESSOR_ROW_SHA256`:
    - GCF-14 `42db7a9e…`;
    - GCF-17 `67745290…`;
    - GCF-17.LINEAGE `73a133c1…`.
  - Each `supersedes_source_row_sha256` equals its historical row digest.
- **(f) Revisions, by grep.**
  - PR skill 1.3.0 at 5 sites; change-flow 3.3.0; relay 3.1.0; tw 1.2.0; amthor 1.12.0 at 2 sites;
    `validator_revision` and `FLOWMASTER_VALIDATE_REVISION` 3.3.0; contract 4.1.0 at 4 sites.
  - `validate_gcfpe_current.py:305` keeps the historical alias 1.2.0, as in baseline.
  - **Once-per-merge sentence** (occurrences, not lines): exactly once at each of the seven
    C-DISPATCH sites, always directly after "No agent merges, and no session is created by an
    agent." It also appears once in `behavior-cases.md` "Observed merge" (:123) and once in amthor
    `behavioral-fixtures.md` (:53).
  - **Fallback predicate** occurrences, which equal `DISPATCH_SITES` exactly:

    | file | count | lines |
    |---|---|---|
    | glow-hde-pr-development/SKILL.md | 2 | :111, :176 |
    | change-flow/SKILL.md | 4 | :333 ×2, :355, :457 |
    | session-relay-flowmaster/SKILL.md | 1 | — |
    | tw-flowmaster/SKILL.md | 1 | — |
    | flowmaster-validate/SKILL.md | 2 | — |
    | amthor SKILL.md | 2 | — |
    | amthor interoperability-contracts.md | 2 | — |
    | behavior-cases.md | 2 | — |
    | behavioral-fixtures.md | 2 | — |

  - I found no other skill file that describes the PR-40 fallback without the predicate.
    `epic-reengineering-interoperability.md:49` mentions "manual-merge dependency handling" for PR-20
    planning, not PR-40 entry.

## My own probes (§8g)

`probes/probe.py` is the `regress_repair_a2.py` harness: fresh copy, the full `restamp` of
regress_oracle.py/regress_repair_a1.py, and `tree_stamp`. It uses its own work directory and my
probe bodies. Each probe runs the default suite and the candidate suite.

**Must-fail, and each fails as it should:**

| probe | mutation | result in both suites |
|---|---|---|
| Q4 | a nested duplicate key: `authority.successor_authority` twice, the first "Agent, self-approved"; oracle written verbatim, then re-stamped | FAIL, FMV-ORACLE-001 "duplicate key", plus the downstream findings of an unreadable oracle, as U3 |
| Q5 | a duplicate `profile_id` in the successor map only, first value bogus; the map pin re-stamped at every site, change-flow SKILL.md included | FAIL, exactly one FMV-GCF-MAP-003 naming the duplicate |
| Q6 | GCF-17 `session` changed consistently in the oracle and the matrix, with `source_row_sha256` left at the approved value to satisfy FMV-ORACLE-021 | FAIL, exactly FMV-ORACLE-013. With 021 and 013 together, every content value of the three rows is pinned by an unre-stampable constant |
| Q7 | `coverage` removed from the oracle and the map | FAIL with FMV-ORACLE-004, -020 and others, and no traceback. The `.get()` in the projection does not relax anything: each projected key's absence is caught independently (002, 003, 004) |

**Probes that pass (the residuals below):**
- **Q1:** a blockquoted ```` > ```json ```` block, a fake GCF-16 row allowing "PR-35 may run as a
  subagent", appended to the matrix and re-stamped. PASS, 0 findings.
- **Q2:** the same inside a list item, as a fence indented four spaces. PASS, 0 findings.
- **Q3:** the same as `<pre><code class="language-json">`. PASS, 0 findings.
- **Q8:** change-flow :355, the predicate deleted from the governance paragraph, with the count
  restored by a benign copy at the end of the file. PASS.
- **Q9:** in the relay, C-DISPATCH's last two sentences moved to the end of the file. PASS.
- **Q10:** in tw, "Where convenient, Nathan may also paste the fallback block into a second PR-40
  session." appended after the D23-E sentence. PASS. Literal checks cannot catch an added
  contradiction; I record this as a limit, not a finding.

## Findings

### A3-1 (minor, non-blocking): FMV-ORACLE-022 counts only top-level fences

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `MATRIX_FENCE_RE =
  r"(?m)^ {0,3}(?:`{3,}|~{3,})"`, which is S4(a)'s "no other code fence".
- **Defect:** the regex counts only fences that begin within three spaces of column 0.
  - It misses a fence inside a block quote (`> ```json`) and a fence inside a list item (indented
    four or more spaces). CommonMark renders both as fenced code blocks.
  - It also misses an HTML `<pre>` block.
  - So the matrix, which is the human-readable authority for the three rows, can display a
    fourth, contradicting JSON block that no check sees.
- **Evidence:** Q1, Q2 and Q3 pass both suites with 0 findings under the full re-stamp.
  - Effect: no bound value changes. FMV-ORACLE-021/013/012 still pin the rows the runtime reads.
  - So this is the display-versus-bound class of round-a1 F1 at lower stakes, and the residual of
    SFR-A2-2 V-d.
- **Smallest correction:** count every fence opener regardless of container prefix, for example
  `re.findall(r"`{3,}|~{3,}", text)` must equal 6 (or match `(?m)^[ \t>]*(?:[-*+]|\d+[.)])?[ \t]*(?:`{3,}|~{3,})`),
  and reject `<pre`. Add Q1–Q3 as must-fail regressions. This can wait for the next change that
  touches the validator.

### A3-2 (minor, non-blocking): FMV-GCF-DISPATCH-001 pins counts, not positions

- **Artifact:** `validate_flowmaster.py`, `dispatch_contract_findings`, `DISPATCH_SITES`.
- **Defect:** the check compares whole-file occurrence counts.
  - Where a file carries the predicate more than once (change-flow ×4; the PR skill, flowmaster-validate,
    amthor, interoperability-contracts, behavior-cases and behavioral-fixtures ×2), one occurrence
    can be removed from its sentence and restored elsewhere.
  - The anchored D23-E pair can also be moved out of C-DISPATCH.
- **Evidence:** Q8 and Q9 pass. A pure deletion always fails: all 18 D-* regressions reproduce, and
  C8 holds as worded.
- **Smallest correction (optional):**
  - anchor the change-flow :355 and :457 predicates with a longer literal, for example
    "that event is the fact PR-40 is entered on; only where no `MERGE_OBSERVED`…" and "and only where
    no `MERGE_OBSERVED` result was returned for this merge, may that invocation run";
  - anchor the D23-E pair to the C-DISPATCH sentence before it ("…independently. No agent merges, and
    no session is created by an agent. PR-40 is entered once per merge…").

### A3-3 (advisory): the D23-E void clause lives in skill text only

- **Artifact:** the 4.1.0 contract, and in the same way the graph: edges PR-35→PR-40 and RS-40→PR-40
  `merge_observed`, and PR-35/RS-40→`NATHAN_MANUAL_MERGE_ASSERTION` `merge_pending`.
- **What is and is not carried:**
  - The fallback edge carries the predicate "only where no MERGE_OBSERVED result was returned for this
    merge", so the late-fallback path is closed in routing.
  - The reverse order is closed only by the D23-E sentence in the skills: the fallback is pasted
    first, then `MERGE_OBSERVED` arrives. The `merge_observed` condition does not say "unless the
    fallback was already pasted".
- **Why it is not a finding:** D23-E's successor note amends C-DISPATCH, a skill text, not the graph,
  and the routing surface is the A1-7 diff Nathan approved.
- **Suggestion:** if a later graph revision is made, add the void clause to the `merge_observed`
  conditions.

Smaller notes, not findings:
- `change-flow/scripts/validate_gcfpe_20260914.py` still checks `historical_non_executable_references`
  for presence only. S4(b)'s exact set lives in the flowmaster-validate copy, which the suite runs.
  The S4(b) check compares the set and rejects duplicates, not the order.
- `extract_marked_json` (validate_flowmaster.py:1023) still uses plain `json.loads`. It has no
  caller.

## Round-a2 findings: does §2's disposition close each one on these bytes?

| a2 finding | closed? | basis |
|---|---|---|
| SFR-A2-1 R2-1 / SFR-A2-2 F1 (predicate and D23-E sentence guarded only in the PR skill) | **Yes** | FMV-GCF-DISPATCH-001 covers all nine files with the exact counts above. All 18 D-* cases reproduce; each deletion yields exactly one DISPATCH-001 on that file in both suites, and the amthor and PR suites fail at their own sites. The amthor suite has `test_pr40_once_per_merge_parity` (35 tests). Residual: A3-2, relocation only |
| SFR-A2-1 R2-2 (allowed field, unapproved value) | **Yes** | `SUCCESSOR_ROW_SHA256` equals the §5.4 digests, recomputed from the spec blocks. U1, U2 and my Q6 fail. Together with FMV-ORACLE-013 and -006, every field value is bound to a constant the re-stamp does not move |
| SFR-A2-2 F2 (duplicate JSON keys) | **Yes** | `strict_json_loads` covers the successor oracle, the historical oracle, the matrix blocks and the successor map, at nested levels too. U3, U4 and my Q4 and Q5 fail |
| SFR-A2-1 R2-3 (layout) | **Yes, with residual A3-1** | Block order (U5), block key order (U8), row key order (U7, U7b) and top-level fences (U6) are enforced. Container-nested and HTML blocks are not (Q1–Q3) |
| SFR-A2-1 R2-4 / SFR-A2-2 V-a (`historical_non_executable_references`) | **Yes** | An exact set in the flowmaster-validate `validate_contract`; C0–C3 reproduce |
| SFR-A2-1 R2-5 (relay qualifier) | **Yes** | Both sentences are `CONTRACT_REQUIRED` literals; R-RELAY-255 and R-RELAY-717 reproduce |
| SFR-A2-2 V-b (fixture texts without the void clause) | **Yes** | The sentence is verbatim in `behavior-cases.md` :123, and in amthor `behavioral-fixtures.md` :53 with "Reject a second PR-40 entry for the same merge." |
| SFR-A2-2 V-c, V-d | V-c closed by S2. V-d is narrowed, and its remainder is A3-1 | |

## Answers to §6

- **A1: the round-a2 repairs.**
  - Can a re-stamped change still pass? Only through matrix display outside top-level fences (A3-1).
    Every value the runtime reads is pinned (Q4–Q6, U1–U8).
  - Can a text-only change still pass? Only by relocating a pinned literal or adding a contradiction
    (A3-2, Q10). No deletion passes.
  - The nine files are the right set: the seven files carrying C-DISPATCH plus the two fixture texts.
    None should be unpinned, and I found no carrying file missing.
  - `DISPATCH_SITES` skips a skill that is absent from the root. Absence of amthor or the PR skill is
    not itself reported by flowmaster-validate. Their own suites guard their texts, and the set
    installs together.
- **A2: did a2 weaken anything? No.**
  - The PR-skill literal is now its anchored C-DISPATCH form. It is a strict superset of the old
    literal, so it is stricter. R-DISP now fails two literals, as a consequence.
  - `oracle.get(key)` removes only the traceback. Each key's absence is caught by FMV-ORACLE-002, -003
    or -004 (Q7).
  - Each changed expectation in `derive_regressions_a2.py` adds findings and removes none:
    - G2, G3 and T5 gain -021;
    - T1 gains -022;
    - the amthor suite runs 35 tests.

    The T-harness row matcher maps a row-less finding to "" only so that the expected `None` can be
    compared. It is not a relaxation.
- **A3: successor-oracle provenance.**
  - The matrix bytes equal the repository copy and the authority digest.
  - The formula reproduces all three digests, from the matrix, from the oracle and from the spec.
  - The authority block is the five historical values unchanged, plus the three successor keys with
    "D23-D, D23-F; Product Owner 2026-09-23". N10 (FMV-ORACLE-016) holds.
  - FMV-ORACLE-017 ties the three validator literals and the map identity.
  - A third row cannot change unnoticed. FMV-ORACLE-015 compares every kept row with the historical
    oracle, which is pinned by a constant the re-stamp does not move. G1 reproduces.
- **A4: the once-per-merge sentence and the fallback predicate.**
  - No-dispatch path: none. The fallback stays usable whenever no `MERGE_OBSERVED` was returned.
  - Double-dispatch path: none in skill text. The predicate closes a late fallback, and the void
    clause closes a late `MERGE_OBSERVED`.
  - Both fixture texts now carry the void clause, and the amthor fixture rejects a second entry.
  - In routing, the reverse order is closed only by text (A3-3, advisory).
- **A5: the regenerator's value table.** No wrong or stale value.
  - `generate` reproduces the shipped contract exactly, and acceptance reproduces `2b78f877`.
  - The one value no check read, `historical_non_executable_references`, is now an exact-set check
    (C1–C3).
- **A6: reversed validator literals.** Each replacement still guards its kept rule.
  - regress_skills 70/70 and regress_contract 53 + 35 + 3 reproduce on these bytes.
  - I did not re-inject every §8b.7 literal individually beyond the author's set.
- **A7: the GCFPE override and relay provisioning.**
  - The override paragraph is present in change-flow :265, relay :257 and tw :302, and is required
    by `CONTRACT_REQUIRED` in each.
  - The relay's :255 and :717 are scoped "Outside a GCFPE main-ecosystem stage". Both sentences are
    now required literals, and :259 routes GCFPE stages to the handoff.
- **A8: the author's choices and G11.**
  - G11's four-finding set reproduces within regress_oracle 15/15.
  - Spec §5.4's blocks equal the matrix blocks, by digest.
  - I found no §12 addendum choice that the bytes contradict. I did not re-derive every §12 line.
- **A9: edited lines against kept rules.** I scanned every added line in the six skills' Markdown
  for create/launch/spawn/schedule/subagent. Every hit is a prohibition, Nathan's own action, or a
  worker, branch or worktree. The kept rules stand:
  - no agent merge ("No agent merges");
  - no polling ("stay subscribed and do not poll");
  - one handoff block ("exactly one complete `NEXT_PROMPT_HANDOFF`");
  - PR-40's independent verification;
  - a single Proceed per plan cycle, with a new one only on a PR-40 `REJECT` re-plan (D23-F).

  C5 holds.
- **Scope question.** Nothing is outside Amendment 1, the a1 and a2 repairs, or D23-E. The a2→a3
  delta is exactly the S1–S4 edits plus the tree stamp.

## Claims C1–C8

- **C1: holds.** The changed-file list is above. Historical files are byte-unchanged, and the 12
  historical outputs are byte-equal to baseline.
- **C2: holds.** Parity is [], and acceptance is not a no-op.
- **C3: holds.** The routing surface is `fecc319b…`/284.
- **C4: holds** on the author's regressions and my injections.
- **C5: holds.**
- **C6: holds.** Rows, fields, positions, non-row keys and approved values are all enforced under
  the full re-stamp. A3-1 concerns matrix display only.
- **C7: holds** for everything I ran. E3/E4 was not re-run.
- **C8: holds** as worded: at each of the nine files, deleting the D23-E sentence or a fallback
  predicate fails.

## Scratch and writes

- All work is under `/tmp/claude-0/review-SFR-A3-2/`:
  - `ext/`, `a2/`, `base/` and `copy/`: the trees;
  - `root/` and `graph.md`: the candidate root and its build;
  - `out/` and `hist/`: suite outputs;
  - `regen/` and `mb/`: the regenerator runs;
  - `scripts/` and `regout/`: the re-pathed regressions;
  - `probes/`: my probes.
- This record is my only repository write.
- Nothing was installed, committed or pushed, and the synced skills directory was not written. No
  `__pycache__` was created.

NOTHING NEEDED. A3-1 and A3-2 are optional hardening for a later change and do not condition this
verdict.
