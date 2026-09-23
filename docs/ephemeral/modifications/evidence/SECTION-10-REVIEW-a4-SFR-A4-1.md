---
artifact_type: SKILL_FIT_REVIEW
reviewer: SFR-A4-1
round: a4 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after hardening round a3)
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a4.md, commit 76912a4, 16473 B, sha256 a3faac9b32c48559993a5db0d5643c3a2854541b3bbbd477dfea0a721c06587c (verified at the working tree and at the commit's blob, at the start and the end)
repository_head_reviewed: 76912a491d12ca26fb5a10788c4bb9ad67e2669c (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged), the same at the start and the end
reviewed_at_utc: 2026-09-23T11:20Z
scratch: /tmp/claude-0/review-SFR-A4-1/
supersedes: nothing. This is a successor record. It does not edit the round-a1, a2 or a3 records (AUTH-001).
---

# Section 10 review, round a4 — SFR-A4-1

## Verdict

**SKILL_FIT_CONFIRMED**

The verdict applies only to these six packages, installed together as one set, as they sat in
`/tmp/claude-0/pkg4/new/`. I measured every value in the table myself from those archives. **The
verdict is void for any other bytes.** No earlier confirmation or measurement carries to these bytes.

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54899 | `0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7` |
| change-flow.skill | 22 | 257990 | `af8cff939b1b94ced1c487dbcb6b87a6ccb9904304b3ca7cc621fd0798c34902` |
| flowmaster-validate.skill | 31 | 318773 | `b1f9184b88eff82dfbe49044509626dba7863bc080e93008491061758e56eef6` |
| glow-hde-pr-development.skill | 4 | 22494 | `dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913` |
| session-relay-flowmaster.skill | 5 | 56330 | `30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b` |
| tw-flowmaster.skill | 2 | 20368 | `db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf` |

**Why fit.**
- Every gate in brief §8 passes when run from these bytes.
- The historical layer is byte-equal to baseline, 12 of 12.
- All 191 earlier regressions and the 13 round-a3 regressions reproduce exactly.
- The contract differs from the regenerator's output only in `route_graph_semantics.pr40_entry`.
- The graph (`ae2bd159…`) and the routing surface (`fecc319b…`/284) are unchanged.
- Each round-a3 finding is closed on these bytes, as §2 states.

**Three residuals, none blocking.** Each is in a validator's completeness at a corner. None
changes a bound value, a routing edge or a skill instruction:
- **A4-1:** H4's "in order" half cannot fire.
- **A4-2:** H2's comment stripping misses an unterminated `<!--` and a `--!>` close.
- **A4-3:** H1 misses an indented code block and the `<xmp>`/`<textarea>` elements.

I also record one advisory, A4-O1: the regenerator's value table does not carry H5.

## Stability and baseline

- **Brief.** The file is 16473 B, sha256 `a3faac9b…`, equal to the blob at `76912a4`.
- **HEAD.** `76912a491d12…` at the start and at the end. The working tree was clean apart from this
  record.
- **Baseline reproduced first.** The synced tree `b25b7d44-…_bb1d0f6b-…` gives, from `freeze.py`:
  - flowmaster-validate 29 `b9ca212ac1275f16…`
  - change-flow 21 `80e877c20fa9be5b…`
  - glow-hde-pr-development 4 `e109d47ac9410a77…`
  - session-relay-flowmaster 5 `4ef8daa3faabc085…`
  - amthor 15 `6cd088a00c5bbcb3…`
  - tw-flowmaster 2 `fa3fac85b69c0f58…`

  All six equal spec v2 §2 in full. I re-measured them at the end: unchanged. The tree did not move.
- **Extracted a4 trees.** Their freeze digests equal brief §3:
  - flowmaster-validate 31 `95d8469d99abaf2c…`
  - change-flow 22 `ee546df57f3d5f0f…`
  - glow-hde-pr-development 4 `68077fa6620992997…`
  - session-relay-flowmaster 5 `15aef9890ebfa286…`
  - amthor 15 `819915e4a57184fd…`
  - tw-flowmaster 2 `fd6c344befd9ce9e…`

## §8a — archives

- File counts, byte sizes and sha256 equal §1 for all six. I measured each from the archive bytes.
- Every entry sits under its own skill root:
  - no entry lies outside the root;
  - no entry is absolute;
  - no entry contains `..` or a backslash;
  - no entry is a symlink.
- Each SKILL.md `name:` is unchanged from the installed tree.

## §8b — gates I ran

I built the scratch copy from the whole synced tree, then replaced the six skills with the
extracted contents. Every command below ran from that copy, with `PYTHONDONTWRITEBYTECODE=1` and
`TMPDIR` inside the scratch.

For `<root>`, I built `graph_parts.py build` over the branch's `docs/graph/parts`:
- 55 nodes, 229 edges and 55 state_routes;
- the embedded JSON is 575074 B, `ae2bd159f0ba947c…`;
- `validation PASS`.

That JSON is byte-equal to the graph bundled in both change-flow and flowmaster-validate.

| command | result (top-level flag read by name) |
|---|---|
| validate_flowmaster.py (default) | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`; 0 findings, 0 warnings, 0 advisories |
| validate_flowmaster.py --strict-warnings --gcfpe-contract … --gcfpe-candidate-root <root> | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`; 0 findings |
| validate_gcfpe_20260914.py <cf> --contract … | `ok: true`; `errors []`; contract `6902924a…`; graph `ae2bd159…`, 55/229 |
| run_gcfpe_20260914_fixtures.py | `fixture_suite_ok: true`; 228 cases, 0 failed; `profile_errors []` |
| validate_gcfpe_current.py | `ok: true`; `errors []` |
| run_gcfpe_current_fixtures.py | `fixture_suite_ok: true`; 228 cases, 0 failed |
| run_change_flow_fixtures.py | `fixture_suite_ok: true`; 32/32 expectations, 0 failed |
| <cf>/scripts/validate_gcfpe_20260914.py | exit 0, `PASS` |
| validate_glow_hde_pr_development.py | exit 0, `PASS` |
| validate_relay_manifest.py --self-test | `status: PASS`; 230 cases, 0 not ok |
| amthor run_fixture_suite.py | `Ran 35 tests … OK` |
| amthor validate_project_prompt_registry.py (repo registry) | `valid: true`, `problems []` |

amthor's suite runs 35 tests. Spec v2 §2's baseline listed 34. The 35th is one of the listed
amthor edits (run_fixture_suite.py is in the diff list), not an unlisted change.

**The 12 historical-layer commands of spec v2 §2.** I ran each on my copy and on a fresh baseline
copy of the synced tree. For every command, stdout, stderr and the exit code are byte-equal: 12 of
12, all exit 0.

## §8c — diff list

I derived the list with `diff -rq` against the installed tree. It holds 25 changed files and 3 added
files. Every one falls in a section that names it:
- **amthor** (§8a.7–8a.9): SKILL.md; references behavioral-fixtures, interoperability-contracts and
  project-prompt-registry-schema; scripts/run_fixture_suite.py.
- **glow-hde-pr-development** (§8a.1–8a.3): SKILL.md, references/behavior-cases.md and the validator.
- **change-flow** (§8b.2, §8b.3, §5, §6, graph): SKILL.md, the graph, the contract,
  scripts/validate_gcfpe_20260914.py, and the added runtime map `-20260923`.
- **flowmaster-validate** (§8b.6–8b.9, §5, §5.8, §6):
  - SKILL.md;
  - both scenarios.json files;
  - the graph, the contract and the profile;
  - run_change_flow_fixtures.py, run_gcfpe_20260914_fixtures.py and run_gcfpe_current_fixtures.py;
  - validate_flowmaster.py, validate_gcfpe_20260914.py and validate_gcfpe_current.py;
  - two added files: the oracle `-20260923` and `r1-successor-source-20260923.md`.
- **session-relay-flowmaster, tw-flowmaster:** SKILL.md only (§8b.4, §8b.5).

The historical oracle, the historical map and the older contracts do not appear in the list, so
they are byte-unchanged.

## §8d–f — rosters, contracts, pins, sites

- **Oracle.** 46 rows, with ids in historical order. Only GCF-14 (`consumes`), GCF-17 (`name`,
  `actor`, `session`, `failure_stop_condition`) and GCF-17.LINEAGE (`next`,
  `failure_stop_condition`) differ, each with its `source_row_sha256`.
  - Each digest recomputes by the formula: `42db7a9e…`, `67745290…` and `73a133c1…`.
  - The top-level key order is historical. Only `profile_id`, `required_global_tokens`, `authority`
    and `runtime_rows` differ.
  - The matrix digest equals `authority.successor_source_matrix_sha256` (`8b443eb1…`). The
    repository copy of the matrix is byte-equal to the bundled one.
- **Contract.** It equals graph parity: `validate_graph_contract(contract, graph) == []` and
  `validate_contract(contract) == []`.
- **Pins.** I recomputed each pinned artifact and grepped every consumer:
  - graph `ae2bd159…`, 575074 B; both copies are equal;
  - contract `6902924a…`, 613326 B; both copies are equal; its consumers are the profile and fv
    `validate_gcfpe_20260914.py`;
  - successor oracle `ede635b1…`;
  - successor map `aa6ed8e3…`;
  - matrix `8b443eb1…`;
  - fixtures `c433aa09…`;
  - historical oracle `52807e58…` and historical map `5574666e…`, each kept at its historical
    consumers.

  Every consumer carries the recomputed value. None of the stale values appears anywhere in the six
  trees: `7a7fd028`, `2b78f877`, `90021eb7`, `b1911cf5`, `613162`, `7380cd14`.
  - `SKILL_TREE_SHA256` is `d6fa3c03…`, equal to `skill_tree_digest` recomputed.
  - The routing surface, computed by `routing_surface()` from both the shipped contract and my graph
    build, is `fecc319bdd4ce7ee6201cb77d7231861`/284.
- **Sites, by grep over all six trees, independent of the author's list.**
  - The D23-E sentence occurs once in each of 9 skill-text files: 7 carrying sites plus 2 fixture
    texts.
  - The whole C-DISPATCH passage occurs once at each of the 7 carrying sites.
  - Backticked fallback predicate counts:

    | file | count |
    |---|---|
    | PR SKILL.md | 2 |
    | change-flow SKILL.md | 4 |
    | relay SKILL.md | 1 |
    | tw SKILL.md | 1 |
    | fv SKILL.md | 2 |
    | amthor SKILL.md | 2 |
    | amthor interoperability-contracts.md | 2 |
    | PR behavior-cases.md | 2 |
    | amthor behavioral-fixtures.md | 2 |

    These equal `DISPATCH_SITES` exactly.
  - Outside skill text, the D23-E sentence also sits in both contract copies (`pr40_entry`, once),
    in validators and in fixture scripts. The graph carries the unbackticked predicate 5 times and
    no D23-E sentence, as H5 intends.
  - No guarded text sits in an HTML comment at any site.

## §8g — my own must-fail probes, under a full re-stamp

`probes.py` is in my scratch. Its re-stamp follows `regress_oracle.py`:
- it re-writes the oracle and map;
- it moves the graph and contract `protected_identities` and `frozen_candidate_graph`;
- it moves both contract copies, the profile, the byte-count pins and every validator literal;
- it re-stamps `SKILL_TREE_SHA256` last.

Each probe then runs six checks: the default suite, the candidate suite, fv
`validate_gcfpe_20260914`, the change-flow validator, the PR validator and the amthor suite. Before
any mutation, all six are clean.

| id | mutation | result |
|---|---|---|
| D3 | C-DISPATCH wrapped in `<!-- … -->` (control) | caught, FMV-GCF-DISPATCH-001 |
| D6 | one space in C-DISPATCH replaced by U+00A0 (control) | caught, DISPATCH-001 |
| D7 | fixture D23-E sentence put in an HTML comment (control) | caught, DISPATCH-001 |
| D8 | relay skill absent from the root (H3 control) | caught, DISPATCH-001 |
| **D1** | **a lone `<!--` line before C-DISPATCH, never closed (hides the rest of the file in CommonMark/HTML)** | **passes: A4-2** |
| **D2** | **C-DISPATCH wrapped in `<!-- … --!>` (a comment close under the HTML spec)** | **passes: A4-2** |
| D4 | a pinned change-flow context sentence moved under a new "Superseded wording (not in force)" heading | passes: the volunteered limit |
| D5 | tw's C-DISPATCH put inside a fenced block labelled "Superseded example, not in force" | passes: the volunteered limit |
| M3 | fence in `> 1. - ```json` (H1 control) | caught, FMV-ORACLE-022 |
| M4 | `<PRE>` block (H1 control) | caught, ORACLE-022 |
| M5 | tab-indented fence in a list item (control) | caught, ORACLE-022 |
| **M1** | **a fourth block as a 4-space indented code block** | **passes: A4-3** |
| **M2** | **a fourth block in `<xmp>`** | **passes: A4-3** |
| **M6** | **a fourth block in `<textarea>`** | **passes: A4-3** |
| P1 | extra top-level key in the successor map (H4 control) | caught, FMV-GCF-MAP-005 |
| **P2** | **successor-map projection keys reordered, same content** | **passes: A4-1** |
| K1 | D23-E sentence removed from `pr40_entry` (H5 control) | caught: ROUTE_GRAPH_SEMANTICS; CURRENT-001, CANDIDATE-CONTRACT-001 and fixtures |
| K2 | "the other is void" changed to "also valid" in `pr40_entry` | caught, as K1 |
| K3 | new sibling `route_graph_semantics.pr40_reentry` contradicting D23-E | caught, ROUTE_GRAPH_SEMANTICS |
| K4 | new top-level contract key contradicting D23-E | caught: CONTRACT_TOP_LEVEL_KEY_DRIFT, and the cf validator fails |

- **D4 and D5** add text that contradicts a pinned sentence. That is the §2 "known limit that
  stays", so I do not raise them as findings. Note one consequence: H2's pins hold a predicate to
  its local context of about 70 characters, not to its section.
- **K3 and K4** show that `route_graph_semantics` is exact-valued and that the contract's
  top-level keys are closed. The contract side of D23-E is therefore stronger than the skill-text
  side.

**The author's regressions, re-pathed into my scratch** (from `derive_regressions_a3.py` and
`regress_repair_a3.py`):

| harness | result |
|---|---|
| oracle | 15/15 exact; G11 gives its four findings |
| skills | 70/70 |
| contract | 53/53, 35/35 and 3/3 |
| fixtures | 2/2 |
| a1 | 17/17 |
| a2 | 34/34 |
| a3 | 13/13 |

## §8h — regenerator, graph and routing surface

- **`regenerate_contract.py generate`.** Inputs: my graph build, the installed contract
  (`2b78f877…`) as template, and the bundled successor oracle. It writes 613162 B, `7a7fd028…`.
  - A recursive JSON diff against the shipped contract gives exactly one path,
    `.route_graph_semantics.pr40_entry`. The shipped value is the regenerated value plus
    ` PR-40 is entered once per merge: …, the other is void.`
- **`regenerate_contract.py acceptance`.** Inputs: the parts at the merge base
  `a63bf80` (= `origin/main`), and the installed builder, template and validator.
  - The stripped template is not a no-op.
  - The regenerated contract is 606657 B, `2b78f877…`: `ACCEPTANCE_PASS`.
  - `validate_graph_contract` and `validate_contract` both return `[]`.
  - The routing surface is `7380cd14…`/282.
  - Leave-one-out finds nothing that is not load-bearing.
  - `NEGATIVE_CONTROL_PASS`.
- The graph build and the routing surface are unchanged from round a3.

## Findings

### A4-1 (minor, non-blocking): H4's key-order clause cannot fire

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, the FMV-GCF-MAP-005 block
  (about lines 1290–1323).
- **Defect:** the new check `list(contract_map) != list(expected_projection)` sits inside
  `if contract_map and contract_map != expected_projection:`. Python dict equality ignores key
  order. A map with the same content and reordered keys therefore never reaches the check. §2 says
  H4 requires "exactly the projection keys, in order". The "in order" half does not hold.
- **Evidence:** probe P2 (keys reordered, every pin re-stamped) gives 0 findings in all six checks.
  P1 (an extra key) is caught.
- **Why it does not block:**
  - SFR-A3-1 V2 (an extra key passes) is closed.
  - Content equality is fully enforced.
  - No consumer reads the map's key order.
- **Smallest correction:** move the order comparison outside the inequality guard, as
  `if contract_map and list(contract_map) != list(expected_projection):`. Then add a
  reordered-keys must-fail case beside V2.

### A4-2 (minor, non-blocking): comment stripping misses an unterminated or `--!>`-closed comment

- **Artifact:** `validate_flowmaster.py`, `HTML_COMMENT_RE = re.compile(r"(?s)<!--.*?-->")`, as
  used by FMV-GCF-DISPATCH-001.
- **Defect:** H2 states that "moving text into a comment is a deletion". Two cases escape it:
  - A `<!--` that is never closed is not stripped. In CommonMark and HTML it hides everything after
    it.
  - A comment closed by `--!>` is not stripped. The HTML parser accepts `--!>` as a close.
- **Evidence:** probes D1 and D2, each at the PR skill's C-DISPATCH, pass all six checks. The
  well-formed control D3 is caught.
- **Smallest correction:** strip with `r"(?s)<!--.*?(?:-->|--!>)"`. Then report DISPATCH-001 when
  `<!--` remains in the stripped text. Add D1 and D2 as must-fail cases.

### A4-3 (minor, non-blocking): FMV-ORACLE-022 misses code rendered without a fence

- **Artifact:** `validate_flowmaster.py`, `matrix_fence_lines` and `MATRIX_PRE_RE`.
- **Defect:** H1 says "no fourth block can render in the matrix unchecked", but three forms escape:
  - a 4-space indented code block renders as code with no fence line;
  - `<xmp>` renders preformatted;
  - `<textarea>` does too.
- **Evidence:** probes M1, M2 and M6. Each adds a fake GCF-16 row block and re-stamps the matrix
  digest, and each passes all six checks. The container and `<PRE>` controls (M3–M5) are caught.
- **Why it does not block:**
  - The matrix's JSON blocks are bound by FMV-ORACLE-009, -011, -012, -018 and -021.
  - A fourth block is display only; no check or consumer reads it.
  - Free prose in the matrix can already say anything under a re-stamp.
- **Smallest correction:** outside the three JSON blocks, report FMV-ORACLE-022 for any line
  beginning with 4 spaces or a tab, and widen `MATRIX_PRE_RE` to
  `(?i)<(?:pre|xmp|listing|plaintext|textarea)[\s>]`. Alternatively, pin the matrix prose outside
  the blocks and digest lines to its current skeleton.

### A4-O1 (advisory): the regenerator's value table does not carry H5

- **Artifact:** `docs/ephemeral/modifications/evidence/regenerate_contract.py`, `VALUE_TABLE`.
- **Observation:** `generate` still yields `7a7fd028…`. `validate_contract` rejects that output
  with `ROUTE_GRAPH_SEMANTICS`. The shipped `6902924a…` exists only by way of
  `apply_repairs_a3.py`'s one-value patch.
- **Why it is only advisory:** brief §2 and C2 declare this, and a check does read the value. It
  is a provenance two-step rather than a stale value, but whoever next runs the recipe will get a
  contract that fails.
- **Smallest correction:** set `pr40_entry` in `VALUE_TABLE` to the H5 value. `generate` then
  reproduces `6902924a…` directly.

## Round-a3 findings: does §2's disposition close each one on these bytes?

| round-a3 finding | closed? | evidence |
|---|---|---|
| SFR-A3-2 A3-1 / SFR-A3-1 F1 (fence in a block quote, list item or `<pre>`) | **Yes** | M3, M4 and M5 are caught; Q1–Q3 reproduce. The residual A4-3 concerns forms without a fence, which were not the reported vector. |
| SFR-A3-2 A3-2 / SFR-A3-1 limit (counts, not positions; text moved into a comment) | **Yes, with residual A4-2** | The whole passage is pinned once per carrying site, and contexts are pinned. D3, D6 and D7 are caught; Q8–Q11 reproduce. Unterminated and `--!>` comments escape (A4-2). Moving a whole sentence to another section with a contradicting heading remains the volunteered limit (D4). |
| SFR-A3-1 V1 (a missing carrying skill is skipped) | **Yes** | D8 and V1 are caught as FMV-GCF-DISPATCH-001. |
| SFR-A3-1 V2 (an extra top-level map key passes) | **Yes** | P1 and V2 are caught. The added "in order" claim is inert (A4-1). |
| SFR-A3-2 A3-3 / SFR-A3-1 limit (the contract lacks D23-E) | **Yes** | `pr40_entry` carries the sentence, and `validate_contract` pins it (K1, K2, K3). Graph and routing surface are unchanged. |

## Answers to §6

- **A1: the round-a3 hardening.**
  - A re-stamped, text-only change can still pass in three narrow ways: A4-1 (key order), A4-2
    (malformed comments) and A4-3 (fence-less code in the matrix).
  - Every other probe I tried against H1–H5 fails as it should.
  - The known limits (added contradicting text, and a re-stamped validator constant) remain, as
    volunteered.
- **A2: weakened or over-reached?**
  - Nothing is weakened: the 191 earlier expectations are exact.
  - Some pinned contexts reach back into the previous sentence, e.g. `permission. PR-35's …`. An edit
    to that sentence's last word would fail DISPATCH-001. This is slightly wide but fails closed, so
    I do not count it as a defect.
  - H5 changes exactly one contract value, confirmed by a recursive diff against the regenerator
    output.
  - The graph (`ae2bd159…`) and the routing surface (`fecc319b…`/284) are as Nathan read them.
- **A3: the successor oracle's provenance.**
  - The matrix bytes, the digest formula, the authority block (historical keys followed by the three
    successor keys, `successor_authority` pinned) and FMV-ORACLE-017 all check.
  - A third row change cannot pass unnoticed. `SUCCESSOR_ROWS` is a validator constant (-010), the
    other 43 rows are equal and in historical order (-015), and each changed row's field set (-019)
    and digest (-021) are pinned. Only a re-stamp of the validator constants themselves could pass,
    which is the volunteered limit.
  - `oracle` 15/15 reproduces.
- **A4: once-per-merge.** I found no double-dispatch or no-dispatch path.
  - All 7 carrying sites have the same passage. It says the conditional block is usable "only after
    he merges and only where no `MERGE_OBSERVED` result was returned", and "Once either has been
    pasted, the other is void".
  - Both fixture texts carry the sentence in context.
  - The contract's `pr40_entry` now says the same.
  - The graph edge predicates keep the "only where no MERGE_OBSERVED" guard. The void rule lives in
    the contract, not the graph, by design.
- **A5: the regenerator's value table.** With the H5 value applied, the regenerator's output equals
  the shipped contract, and `validate_contract` passes. No other stale value exists. The table
  itself lacks H5 (A4-O1), and `validate_contract` does read that value.
- **A6: reversed validator literals.** I did not audit each literal by hand. I relied on the 191
  regressions, which I re-ran and found exact, and on my own probes. I state this as a limit of my
  review rather than a finding.
- **A7: the GCFPE override of the Flowmaster core option to create a session.**
  - change-flow SKILL.md:265 and tw SKILL.md:302 each say: "For every GCFPE main-ecosystem stage,
    the core's option to create a fresh session does not apply … returns the paste-ready
    `NEXT_PROMPT_HANDOFF` and stops for Nathan".
  - The core text stays byte-pinned.
  - The relay scopes provisioning outside GCFPE stages: SKILL.md:255 (`SESSION_PROVISIONING_REQUIRED`
    only "Outside a GCFPE main-ecosystem stage"), :259 (GCFPE returns the handoff; "provisioning does
    not apply") and :717.
  - A grep of the six trees for create, launch, schedule, spawn and subagent finds only the pinned
    core lines, negations, and prohibitions on PR-35 running as a subagent.
- **A8: the author's choices in spec §12 and its addendum, and G11.**
  - The settlements I sampled are implemented: N9 order, the historical non-executable references,
    and full paths.
  - G11 reproduces its four findings: CANDIDATE-CONTRACT-001 and CANDIDATE-FIXTURE-PROFILE-001
    (both `PROFILE_PROTECTED_IDENTITIES`), CURRENT-001 (`PROFILE_PROTECTED_IDENTITIES`) and
    CURRENT-FIXTURE-001. All four follow from the one unmoved profile pin under S-5. The set is
    correct and not padded, and I accept it.
- **A9: contradictions with kept rules.** I found none.
  - No agent merge: "No agent merges".
  - No polling: "stay subscribed and do not poll".
  - One handoff block: at `MERGE_PENDING`, the conditional PR-40 block is the single routed handoff.
  - PR-40's independent verification is kept: "`PR-40` still verifies the merged state and landed
    lineage independently".
  - Single Proceed within a plan: "retaining Proceed for the unchanged Plan".
- **Question: anything out of scope?** No. Every changed file maps to §8a, §8b, §5, §6, the a1/a2
  repairs, the a3 hardening or D23-E.

## Claims C1–C8

| claim | holds on these bytes? |
|---|---|
| C1 | Yes. The diff list is confined as in §8c, and historical files are byte-unchanged. |
| C2 | Yes. Acceptance reproduces `2b78f877…`, not a no-op; `generate` gives `7a7fd028…`; the only difference from shipped is `pr40_entry`. |
| C3 | Yes. `fecc319b…`/284, from both the contract and the graph. |
| C4 | Yes, as far as the 191 regressions and my probes reach (see A6). |
| C5 | Yes (A7). |
| C6 | Yes (§8d). FMV-ORACLE-018 to -022 hold under re-stamp, apart from the display-only residual A4-3. |
| C7 | The gates of §8 pass as I ran them. I did not re-run E3/E4 (L1, optional). |
| C8 | Yes, with residuals A4-1 and A4-2. Deleting a D23-E sentence or a fallback predicate, moving it (within the context limit), or hiding it in a well-formed comment fails the suites at each of the 9 files. The contract carries D23-E, and the graph and routing surface are unchanged. |

## Gates I could not run

- **E3/E4 over the Notion prompt bodies.** Optional under L1. I did not fetch any body.
- **A post-install check.** Nothing is installed (L2).

## Scratch and writes

All work is under `/tmp/claude-0/review-SFR-A4-1/`:
- `ext/`, `copy/` and `base/`: the trees;
- `graph.md` and `root/`: the candidate root;
- `out/` and `hist/`: suite outputs;
- `regen/` and `baseparts/`: the regenerator runs;
- `regs/` and `r3/`: the re-pathed regressions;
- `probes.py` and `probes.out`: my probes.

This record is my only repository write. Nothing was installed, committed or pushed, and the synced
skills directory was not written.

One `__pycache__` appeared inside my scratch copy's `glow-graph-contract/scripts`. An ad hoc import
of mine ran without `PYTHONDONTWRITEBYTECODE`. That skill is not one of the six. The directory was
outside the synced tree and the repository, and I deleted it. At the end, `find` shows none in the
scratch, the synced tree or `docs/`.

NOTHING NEEDED. A4-1 to A4-3 and A4-O1 are optional hardening for a later change and do not
condition this verdict.
