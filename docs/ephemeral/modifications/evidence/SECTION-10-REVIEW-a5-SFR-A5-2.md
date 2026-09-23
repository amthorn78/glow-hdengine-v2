---
artifact_type: SKILL_FIT_REVIEW
reviewer: SFR-A5-2
round: a5 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a4)
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a5.md, commit b65f754, 16561 B, sha256 80a7ce77fab20fc4e046df97a5bc04770150ecf1f82532d7d9cf9257b2ca5aee (verified in the working tree and in the commit's blob)
repository_head_reviewed: b65f7545b1d5e47eec55839ce02f61922e25002c (branch docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged). HEAD was the same at the start and at the end.
reviewed_at_utc: 2026-09-23T12:08Z
scratch: /tmp/claude-0/review-SFR-A5-2/
supersedes: nothing. This is a successor record. It does not edit any a1 to a4 record (AUTH-001).
---

# Section 10 review, round a5: SFR-A5-2

## Verdict

**SKILL_FIT_CONFIRMED**

This verdict applies only to the six packages below, installed together as one set, as they sat in
`/tmp/claude-0/pkg5/new/`. I measured every value from those archives. **The verdict is void for any
other bytes.** No earlier confirmation or measurement carries to these bytes, and none was used.

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54899 | `0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7` |
| change-flow.skill | 22 | 257990 | `af8cff939b1b94ced1c487dbcb6b87a6ccb9904304b3ca7cc621fd0798c34902` |
| flowmaster-validate.skill | 31 | 319235 | `394bb1ae208607f46170b481153e4e00b7f93fe65150c872bc401c1406f59d22` |
| glow-hde-pr-development.skill | 4 | 22494 | `dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913` |
| session-relay-flowmaster.skill | 5 | 56330 | `30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b` |
| tw-flowmaster.skill | 2 | 20368 | `db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf` |

**Why.**
- Every gate in brief §8 passes on these bytes.
- All 12 historical-layer outputs are byte-equal to the baseline.
- Every regression the author lists in §8 is exact when I re-run it in my scratch: 253 cases across eight harnesses, 242 of them from before round a4.
  - §2's "all 204" is a count I could not reproduce from these harness totals. It may be defined differently. It is noted, not a finding: every case is exact either way.
- The round-a4 control holds: 9 of the 11 a4 cases fail on the round-a4 tree. The two that pass are `clean` and K3.
- C1 to C8 hold as stated. That includes C8's comment clause: every comment I added other than a marker failed.

My own probes found four residuals. All are minor, and none changes a value that any consumer reads:
- **F1:** indented code inside a block quote or list item.
- **F2:** a marker-shaped comment.
- **F3:** hidden-text constructs that are not comments.
- **F4:** an ASCII arrow falsely rejected.

F1 is the only one that falls under a stated repair claim. §2 says R3 rejects "indented code lines outside the fenced blocks", and a container-prefixed indented line escapes it. It is the same display-only class that SFR-A4-2 rated minor (their F3), so it does not block. Each finding can be fixed with a small code edit, or listed as a known limit.

What I did not do:
- install anything;
- write to the synced skills directory;
- commit, merge or enable auto-merge;
- edit PF-Canon, the registry, the graph parts, Notion or any prompt body;
- write to any repository path except this record.

## Stability and baseline

- **Brief.** `REVIEWER-PROMPT-a5.md`: 16561 B, sha256 `80a7ce77…`. It is equal in the working tree and in `git show b65f754:`.
- **Baseline.** `freeze.py` on the installed synced tree reproduced spec v2 §2 exactly, at the start and at the end:
  - flowmaster-validate 29 `b9ca212a…`
  - change-flow 21 `80e877c2…`
  - glow-hde-pr-development 4 `e109d47a…`
  - session-relay-flowmaster 5 `4ef8daa3…`
  - amthor-workspace-governance-audit 15 `6cd088a0…`
  - tw-flowmaster 2 `fa3fac85…`
  - glow-graph-contract 6 `4e671ddc…`
- **Packages.** The package sha256 values were unchanged at the end.
- **Repository.** HEAD `b65f754` did not move. `git status` is clean apart from this record.
- **Relation to round a4.** Against `/tmp/claude-0/pkg4/new/`, five packages are byte-identical. Only flowmaster-validate differs. Inside it, the only differences are:
  - `SKILL.md`: the `SKILL_TREE_SHA256` line, `d6fa3c03…` → `be70787a…`;
  - `scripts/validate_flowmaster.py`: R1, R2 and R3, exactly as §2 describes.

## §8a: archives

- **Counts, bytes and sha256.** All six match §1, measured from the archive bytes.
- **Entry paths.** Every entry sits under its own `<skill>/` root. No entry contains `..` or an absolute path, and there are no symlinks.
- **Frontmatter.** `name:` in each SKILL.md is unchanged from the installed tree.
- **Freeze digests of the extracted trees.** All six match §3:
  - flowmaster-validate 31 `a79401deaabe35ce1393d91e8d333e86c26a71500b3c5abd89ff5fdbaa7f8f48`
  - change-flow 22 `ee546df57f3d5f0f0dc29c514376e64ca0fa830fe03e64ff7acd8645648bcb73`
  - glow-hde-pr-development 4 `68077fa6620992997c8bb3949b1135ba47b1c5bd275610eb49c3b7d8d04ecf22`
  - session-relay-flowmaster 5 `15aef9890ebfa286bf56272e64cc9880d6dc57701d4e8b45e15fa6f45c3f2121`
  - amthor-workspace-governance-audit 15 `819915e4a57184fd3af0c783f13e102892eb7182d0c951727869655d11ae078d`
  - tw-flowmaster 2 `fd6c344befd9ce9e89648e6e404dd39f02e50bfaef2ca13d4e56ab84f5576617`

## §8b: gates I ran

**Setup.**
- I ran everything from a full copy of the synced tree with the six skills replaced (`/tmp/claude-0/review-SFR-A5-2/copy`), with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside my scratch.
- `<root>` holds only `graph/GCFPE-20260914.1-Candidate-Graph-Contract.json`. That file is the embedded JSON of `graph_parts.py build` over the branch's `docs/graph/parts`:
  - 55 nodes, 229 edges, 55 state_routes;
  - 575074 B, sha256 `ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d`, validation PASS;
  - it is byte-equal to the graph bundled in both change-flow and flowmaster-validate.

**Live suites.** Each result below is read from the tool's own top-level flag.

| command | result |
|---|---|
| `validate_flowmaster.py --skills-root <copy>` | exit 0, `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, 0 findings of any severity, fixtures 32/32 |
| same, with `--strict-warnings --gcfpe-contract … --gcfpe-candidate-root <root>` | exit 0, `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, 0 findings, every `warnings` array empty |
| `validate_gcfpe_20260914.py <cf> --contract …` | `"ok": true`, `errors: []`, contract `6902924a…`, frozen graph `ae2bd159…` 55/229 |
| `run_gcfpe_20260914_fixtures.py <cf> --contract …` | `fixture_suite_ok: true`, 228 cases, 0 failed, §13 37/37 fixtures and 38/38 variants |
| `validate_gcfpe_current.py <cf>` | `"ok": true`, `errors: []` |
| `run_gcfpe_current_fixtures.py <cf>` | `fixture_suite_ok: true`, 228 cases, 0 failed |
| `run_change_flow_fixtures.py` | `fixture_suite_ok: true`, 32 passed, 0 failed |
| `<cf>/scripts/validate_gcfpe_20260914.py` | exit 0, `PASS` |
| `validate_glow_hde_pr_development.py` | `PASS` |
| `validate_relay_manifest.py --self-test` | `status: PASS`, 230 cases, 0 not ok |
| amthor `run_fixture_suite.py` | 35 tests OK (34 on the baseline; one was added) |
| amthor `validate_project_prompt_registry.py <repo registry>` | `{"valid": true, "problems": []}` |

**Historical layer.**
- I ran all 12 commands of spec v2 §2 on the new copy and on a fresh baseline copy. Every command exited 0 on both.
- Each output was byte-equal to its baseline, compared on the raw stdout and stderr bytes.
- Output sizes: 122, 66, 7922, 49255, 41317, 0, 0, 0, 0, 9269, 3521 and 6557 B.

**Regressions.** I derived every harness with `derive_regressions_a4.py`, re-pathed it into my scratch, and ran it against a copy of the reviewed tree:
- oracle 15/15;
- skills 70/70;
- contract 53/53, 35/35 and 3/3;
- fixtures 2/2;
- a1 17/17;
- a2 34/34;
- a3 13/13;
- a4 11/11.

That is exactly the author's set. `regress_repair_a4.py` against the round-a4 tree (`b1f9184b…`) gives 2 of 11. P1–P4 and M1–M5 fail there, as the author's control says.

**Not run.**
- `run_e4.py` over Notion bodies (L1; optional). The prompt-body side (E3/E4) therefore rests on `E3-E4-report.md` and is not re-measured by me.
- `closure.py`.
- Any post-install check (L2).

## §8c: diff list, derived with `diff -rq` against the installed tree

**flowmaster-validate**
- Changed:
  - `SKILL.md`
  - `fixtures/change-flow/scenarios.json`
  - `fixtures/gcfpe-20260914.1-091426.1/scenarios.json`
  - `references/…candidate-graph-contract.json`
  - `references/…direct-handoff-contract.json`
  - `references/…validation-profile.json`
  - `scripts/run_change_flow_fixtures.py`
  - `scripts/run_gcfpe_20260914_fixtures.py`
  - `scripts/run_gcfpe_current_fixtures.py`
  - `scripts/validate_flowmaster.py`
  - `scripts/validate_gcfpe_20260914.py`
  - `scripts/validate_gcfpe_current.py`
- Added:
  - `references/glow-hde-canonical-change-flow-r1-20260923.json`
  - `references/r1-successor-source-20260923.md`

**change-flow**
- Changed:
  - `SKILL.md`
  - the 091426.1 graph
  - the 091426.1 contract
  - `scripts/validate_gcfpe_20260914.py`
- Added: `references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json`.

**glow-hde-pr-development**
- Changed: `SKILL.md`, `references/behavior-cases.md` and the validator.

**session-relay-flowmaster** and **tw-flowmaster**
- Changed: `SKILL.md` only.

**amthor-workspace-governance-audit**
- Changed:
  - `SKILL.md`
  - `behavioral-fixtures.md`
  - `interoperability-contracts.md`
  - `project-prompt-registry-schema.md`
  - `run_fixture_suite.py`

**Checks on the list.**
- Every path is named in spec v2 or in a repair script.
- Every historical file is byte-unchanged: the historical oracle (`52807e58…`), the historical map (`5574666e…`), and the earlier contracts and corrections.
- Of the SKILL.md diffs, flowmaster-validate's is the only one that moved in round a4.

## §8d–f: rosters, contracts, pins and sites

**Oracle.**
- The successor oracle has 46 rows, in the historical order.
- Only GCF-14 (`consumes`), GCF-17 (`name`, `actor`, `session`, `failure_stop_condition`) and GCF-17.LINEAGE (`next`, `failure_stop_condition`) differ, each with its `source_row_sha256`. Each row keeps its historical key order.
- The other 43 rows equal the historical rows.
- The non-row keys differ only in:
  - `profile_id` (`…_20260831_1` → `…_20260923_1`);
  - the matching token in `required_global_tokens`;
  - `authority`, which adds the three successor keys and keeps the historical values.

**Matrix.**
- The matrix is 3 blocks. Its sha256 `8b443eb1…` equals `authority.successor_source_matrix_sha256` and the repository copy.
- I recomputed each row digest with the §5.4 formula:
  - GCF-14 `42db7a9e…`
  - GCF-17 `67745290…`
  - GCF-17.LINEAGE `73a133c1…`
- Each equals, all three ways:
  - the oracle row;
  - the matrix line;
  - `SUCCESSOR_ROW_SHA256`.
- Each block equals its oracle row on all 11 content fields. Each `supersedes_source_row_sha256` equals the historical row digest.
- The formula does not reproduce the historical digests. Spec §5.4 records that, and it is why the 43 kept rows are checked by equality.

**Map.**
- sha256 `aa6ed8e3…`.
- It equals the four-key projection `profile_id, authority, coverage, runtime_rows`, in that order.

**Contract.** `validate_graph_contract(contract, graph)` returns `[]`.

**Pins.** I recomputed each pin from its artifact and found every consumer by grep. All consumers agree.

| artifact | sha256 | consumers |
|---|---|---|
| graph | `ae2bd159…` | both contracts, profile, both `validate_gcfpe_20260914.py` |
| contract | `6902924a…` | profile, fv `validate_gcfpe_20260914.py` |
| successor oracle | `ede635b1…` | both graphs, both contracts, profile, fv SKILL.md, `validate_flowmaster.py`, fv `validate_gcfpe_20260914.py` |
| successor map | `aa6ed8e3…` | profile, `validate_flowmaster.py`, `validate_gcfpe_current.py`, fv `validate_gcfpe_20260914.py`, change-flow SKILL.md |
| matrix | `8b443eb1…` | oracle, map, fv SKILL.md |
| `SKILL_TREE_SHA256` | `be70787a…` | fv SKILL.md; recomputed with `skill_tree_digest` |

- No stale value remains anywhere in the six trees: none of `2b78f877`, `90021eb7`, `7a7fd028`, `b1911cf5`, `d6fa3c03` or `eb9634d6`.

**Sites, recounted by grep.**
- The D23-E sentence occurs exactly once in each of the nine carrying files.
- The backticked fallback predicate occurs at those files 2, 4, 2, 2, 1, 1, 2, 2 and 2 times, in the order: PR SKILL.md, change-flow, flowmaster-validate SKILL.md, behavior-cases, relay, tw, amthor SKILL.md, interoperability-contracts, behavioral-fixtures. Those are exactly the counts pinned in `DISPATCH_SITES`.
- The contract carries the D23-E sentence once, in `route_graph_semantics.pr40_entry`, with the unbackticked predicate. The graph does not carry it (H5, as §2 states).

## §8g: my own must-fail probes, under a full re-stamp

**Harness.**
- I used `regress_repair_a4.py`'s own `fresh`, `move`, `restamp` and `restamp_map_only`, re-pathed to my scratch.
- Each probe ran both `validate_flowmaster.py` runs, plus the PR skill validator, change-flow's own validator and the relay self-test.
- The scripts are `/tmp/claude-0/review-SFR-A5-2/probe/probes.py` and `probes2.py`. Their outputs are `probes.out` and `probes2.out`.

| probe | edit | result |
|---|---|---|
| CLEAN | none | pass |
| Q8 | comment inside the C-DISPATCH passage, interoperability-contracts.md | **caught**, FMV-GCF-DISPATCH-001 (comment and passage count) |
| Q9 | unclosed `<!--` before the passage, tw-flowmaster | **caught** |
| Q12 | abrupt `<!-->` at the end of change-flow SKILL.md | **caught** |
| M1s | two top-level map keys swapped (not a full reversal), map-only re-stamp | **caught**, FMV-GCF-MAP-005 |
| M4d | duplicate top-level `profile_id` in the map | **caught**, FMV-GCF-MAP-003 |
| A3a | a fourth row (GCF-15) changed, with its digest recomputed | **caught**, FMV-ORACLE-015 |
| A3b | GCF-15 added to `authority.successor_rows` | **caught**, FMV-ORACLE-010 |
| O2 | multi-line indented block under a list item (continuation at 6 spaces) | **caught**, FMV-ORACLE-022 |
| O4 | `<PRE class="x">` | **caught**, FMV-ORACLE-022 |
| O5 | `<plaintext>` | **caught**, FMV-ORACLE-022 |
| **O1** | a fourth JSON "row" as `>     ` indented code inside a block quote in the matrix | **passes every gate** (F1) |
| **O2b / O2c** | the same as a one-line `-     {…}` or `1.     {…}` list item | **pass every gate** (F1) |
| **O3** | the same with each line prefixed ` \t` (one space, then a tab) | **passes** (F1, renderer-dependent) |
| O9 | `<p><code>{…}</code></p>` | passes. Inline code, not a code block; noted only |
| **Q3** | whole-line `<!-- FLOWMASTER_AFTER_MERGE_OBSERVED_ALSO_PASTE_THE_FALLBACK_BLOCK -->` after the D23-E sentence, change-flow | **passes every gate** (F2) |
| **Q1** | unclosed `<style>` line before the passage, PR skill | **passes every gate** (F3) |
| **Q2** | unclosed `<?x` line before the passage, amthor SKILL.md | **passes every gate** (F3) |
| **Q2b** | `<template>` line, tw-flowmaster | **passes every gate** (F3) |
| **Q4** | `[//]: # (Exception: when both arrive, paste both and enter PR-40 twice.)` after the D23-E sentence, relay | **passes every gate** (F3) |
| **Q5** | legitimate text `Route: PR-35 --> PR-40 (once per merge).` in tw-flowmaster | **fails**, FMV-GCF-DISPATCH-001 "an HTML comment … is present" (F4) |
| M2n / M3r | reordered keys inside the map's `authority`, or inside one map row | pass. A JSON no-op; H4 and R2 claim top-level order only; noted |

**Rendering evidence.**
- There is no CommonMark renderer in this container, and I installed nothing.
- I parsed the O1, O2b, O2c, Q1 and Q2 snippets with the Markdown parser bundled in the installed prettier (remark), using `prettier.__debug.parse`:
  - O1, O2b and O2c are `code` nodes.
  - Q1 and Q2 are one `html` node that runs to the end of the input.
- For O3, remark gives a paragraph. The CommonMark spec's tab rules (Example 2: `  \tfoo` is an indented code block) give code. So O3 depends on the renderer.

## §8h: regenerator, graph and routing surface

- **Contract recipe.** `contract_recipe.py <graph.md> <installed contract> <successor oracle> <out> --check <fv contract> <cf contract>`:
  - the E2 regenerator output is `7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675`, 613162 B;
  - the recipe output is `6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718`, 613326 B;
  - it prints EQUAL for both shipped contracts, and exits 0.
- **E2 regenerator.** `regenerate_contract.py generate` on its own also gives `7a7fd028…`.
- **Structural diff.** A diff of E2 against the shipped contract finds one difference only: `route_graph_semantics.pr40_entry`, which gains the D23-E sentence.
- **Graph build.**
  - The build from the branch parts is `ae2bd159…`, 55/229/55.
  - `docs/graph/parts` is unchanged between `76912a4` and `b65f754`.
- **Routing surface** (`routing_surface`):
  - graph: `fecc319bdd4ce7ee6201cb77d7231861`/284;
  - shipped contract: the same;
  - installed contract: `7380cd14…`/282, which is spec §2's baseline.

## Findings

### F1 (minor): FMV-ORACLE-022's indentation check misses indented code inside a block quote or list item

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `matrix_indented_code_lines`, in package `394bb1ae…`.
- **Defect:** the check counts a line only when the raw line starts with four spaces or a tab. A line whose indentation follows a container marker therefore escapes it, although it renders as an indented code block inside the container:
  - `>     …` inside a block quote;
  - `-     …` or `1.     …`, where the marker is followed by five or more spaces.

  The fence counter already strips these prefixes (a3 H1), but the indentation counter does not. Separately, one to three spaces followed by a tab reach column 4. That is indented code under the CommonMark tab rule, but it is renderer-dependent (remark disagrees).
- **Evidence:** probes O1, O2b and O2c pass both suites and every other gate, under the full re-stamp with `matrix_changed=True`. remark parses each as a `code` node. O3 also passes.
- **Scope:**
  - The defect is display-only. FMV-ORACLE-011, -012 and -021 pin every parsed value, and no consumer reads a decoy block.
  - It still means §2's R3 wording ("indented code lines outside the fenced blocks") and the rule's own message ("only the three JSON blocks may render as code") hold only for unprefixed lines.
- **Smallest correction:**
  - In `matrix_indented_code_lines`, remove each container marker together with at most one following space or tab, rather than with all trailing whitespace.
  - Then count the line when the remainder begins with four spaces, a tab, or one to three spaces followed by a tab.
  - Add O1, O2b and O3 as must-fail regressions.
- **Alternative:** narrow R3's wording to "unprefixed indented code lines", and list container-prefixed indentation as a known limit.

### F2 (minor): the allowed-marker pattern admits any `FLOWMASTER_*` name, so a marker can carry an instruction

- **Artifact:** `DISPATCH_ALLOWED_COMMENT_RE = re.compile(r"(?m)^<!-- FLOWMASTER_[A-Z_]+ -->$")`.
- **Defect:** any upper-case underscore name passes. Such a name can itself be an instruction, and it is invisible in rendered Markdown.
- **Evidence:** probe Q3 passes every gate. The carrying files use only six marker names:
  - `FLOWMASTER_CORE_BEGIN` and `FLOWMASTER_CORE_END`;
  - `FLOWMASTER_SPECIALIZATION_BEGIN` and `FLOWMASTER_SPECIALIZATION_END`;
  - `FLOWMASTER_PROHIBITIONS_BEGIN` and `FLOWMASTER_PROHIBITIONS_END`.
- **Scope:** this is within the volunteered limit "a contradicting sentence added outside a pinned sentence or passage". The difference is that it is hidden rather than visible, and it is exactly the channel the a4 rule's rationale names ("a comment can hide text").
- **Smallest correction:** enumerate the six names, for example
  `^<!-- FLOWMASTER_(?:CORE|SPECIALIZATION|PROHIBITIONS)_(?:BEGIN|END) -->$`, and add Q3 as a regression.

### F3 (minor, limit class): constructs other than comments still hide text in a rendered carrying file

- **Artifact:** `dispatch_contract_findings`, whose residue test looks only for `<!--`, `-->` and `--!>`.
- **Defect:** CommonMark HTML blocks that begin with any of the following hide what follows when unclosed:
  - `<style>`, `<script>` or `<textarea>` (type 1);
  - `<?` (type 3);
  - `<!` followed by a letter (type 4);
  - `<![CDATA[` (type 5).

  The same applies to `<template>` in a browser. A link-reference definition `[//]: # (…)` is the common Markdown idiom for a hidden comment. None of these is caught.
- **Evidence:** probes Q1, Q2, Q2b and Q4 pass every gate. remark parses Q1 and Q2 as one `html` node to the end of the input.
- **Scope:**
  - C8 holds as worded, since it names HTML comments.
  - A model reading the raw SKILL.md sees all of this text, and the pinned passage is still counted on the raw file.
  - The risk is to a human reading the rendered file, which is the risk SFR-A4-2 F1's defect 2 raised.
- **Smallest correction, either of:**
  - (a) add these openers (`<?`, `<!` followed by a letter, `<![CDATA[`, `<style`, `<script`, `<template`) and a `^\[[^\]]*\]:\s*#` line to the residue test;
  - (b) add "text hidden by raw-HTML blocks or reference definitions other than comments" to §2's known limits.

### F4 (minor, over-reach): an ASCII arrow `-->` in a carrying file is rejected as an HTML comment

- **Artifact:** the same token list.
- **Defect:** a bare `-->` cannot open or hide anything. Every hiding comment needs `<!--`, which the rule already rejects. Yet the rule rejects a legitimate arrow, and its message then misdescribes the text as an HTML comment.
- **Evidence:** probe Q5. No carrying file uses `-->` today, so there is no present effect. `-->` does occur in other installed skills, including flowmaster-primary and deep-research, so an author may reach for it.
- **Smallest correction:** drop `-->` from the token list, keeping `<!--` and `--!>`. Or accept the strictness and say so in the message.

## Round-a4 findings: does §2's disposition close each one on these bytes?

| round-a4 finding | disposition | closed on these bytes? |
|---|---|---|
| SFR-A4-2 F1 (required) / SFR-A4-1 A4-2: comment stripping; comment inside the passage; unterminated `<!--`; `--!>` | R1 | **Yes.** Counts read the raw file. P1–P4 are exact, and they fail on the a4 tree. My Q8, Q9 and Q12 are caught. Residuals outside comments are F2 and F3. |
| SFR-A4-1 A4-1 / SFR-A4-2 F2: map key order unreachable | R2 | **Yes.** M1 is exact, and my M1s (a swap of two keys) is caught. The check is now outside the equality guard. |
| SFR-A4-1 A4-3 / SFR-A4-2 F3: indented code, `<xmp>`, `<listing>`, `<textarea>` | R3 | **Yes for the named elements, `<plaintext>` and unprefixed indentation** (M2–M5 exact; my O2, O4 and O5). **Partly** for indentation in general: container-prefixed indented code passes (F1). |
| SFR-A4-1 A4-O1: regenerator lacks the new `pr40_entry` | R4, `contract_recipe.py` | **Yes.** K3 is exact, and my own run of the recipe reproduces `6902924a…` for both copies. `regenerate_contract.py` is unchanged and still gives `7a7fd028…`. |
| SFR-A4-2 F4: the whole passage moved intact passes | known limit, C8 narrowed | **Yes, as a limit.** C8 now says "out of its pinned passage or sentence", and §2 lists the move. |

## Answers to the §6 questions

**A1. Can a re-stamped or text-only change still pass the round-a4 repairs?**
- The comment rule catches every comment I added, closed or unclosed, inside or outside the passage.
- The map order check catches a partial swap as well as a reversal.
- Under a full re-stamp, three text-only changes still pass:
  - container-prefixed indented code in the matrix (F1);
  - a marker-shaped hidden instruction (F2);
  - non-comment hiding constructs (F3).
- `contract_recipe.py` is correct as a recipe. It asserts that the E2 output's `pr40_entry` equals `W4` before appending, so a changed regenerator fails loudly.

**A2. Did a4, or the a3 hardening beneath it, weaken or over-reach anything?**
- **Weakened:** no. Returning to raw counts restores the a3-tree behaviour that SFR-A4-2 found lost, and the control shows P1–P4 fail on the a4 tree.
- **Over-reach:** one case, F4 (`-->` as an arrow). The pinned sentence contexts are narrow (≤ ~200 characters) and occur once each. None is wider than its sentence.
- **Graph and routing surface:** they stay as Nathan read them:
  - graph `ae2bd159…`, 55/229/55;
  - routing surface `fecc319b…`/284, which is Amendment 1 A1-7's value;
  - the graph parts are unchanged since a4.

**A3. Could a third row change pass unnoticed?** No, in what I tried:
- A3a, a changed kept row with its digest recomputed, gives FMV-ORACLE-015.
- A3b, a fourth id in `successor_rows`, gives FMV-ORACLE-010.

The rest of the provenance checks out:
- The matrix bytes equal the repository copy. The digest formula reproduces all three pinned row digests. The authority block keeps the historical values and adds exactly three keys.
- FMV-ORACLE-021 pins the approved digests independently of any re-stamp.
- The earlier rounds' N1–N10 and FMV-ORACLE-017 cases are in the author's oracle, a1 and a2 harnesses, and they are exact on these bytes.

**A4. Is there a double-dispatch or no-dispatch path left?** None that I found.
- The sentence is identical at all nine sites and in the contract.
- The fallback is usable only where no `MERGE_OBSERVED` was returned. Whichever block is pasted first voids the other.
- Both fixture texts also carry it. behavior-cases.md does so with "stays usable only after Nathan merges and only where no …". behavioral-fixtures.md adds "Reject a second PR-40 entry for the same merge".
- If the fallback is pasted and `MERGE_OBSERVED` arrives later, the sentence voids the late handoff.

**A5. Are there wrong or stale values in the regenerator's contract-only table that no check reads?**
- Every contract-only key in the value table is read by `validate_gcfpe_20260914.py` (flowmaster-validate), and most also by the fixture runner. I grepped all 22 keys and sub-keys.
- `primary_skill_revision` `1.3.0` equals the PR skill's `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION`.
- The only stale value is `W4` without D23-E. That is by design, and the recipe (R4) supersedes it.

**A6. Does every reversed validator literal still guard the kept rule?**
- Yes, as far as the author's skills regressions (70 exact) and contract regressions (91 exact) show, and I re-ran both.
- In my own probes, every carrying-site edit that touched a pinned literal failed.

**A7. The GCFPE override of the core's session-creation option, and the relay's provisioning lines.**
- change-flow, the relay and tw-flowmaster each carry the same override: for every GCFPE main-ecosystem stage, the skill "never creates, spawns, launches or schedules a session" and returns the handoff for Nathan.
- The relay's two `SESSION_PROVISIONING_REQUIRED` lines both begin "Outside a GCFPE main-ecosystem stage".
- The core blocks are unchanged, so the flowmaster suite's core-identity checks pass.

**A8. The author's choices in spec §12 and its addendum, and G11's four-finding set.**
- I found nothing that contradicts a ruling.
- G11's four-finding set reproduces exactly: two candidate wrappers plus FMV-GCF-CURRENT-001 and -FIXTURE-001, all `PROFILE_PROTECTED_IDENTITIES`. The reason is the one the harness states (§12 S-5: the default overlay runs the same v4 checks on the same profile).
- I did not re-audit every §12 settlement line by line.

**A9. Does any edited line contradict a kept rule?** None found.
- **No agent merge:** stated at every carrying site.
- **No polling:** "stay subscribed and do not poll". The PR skill's `:124` is qualified "where no subscription delivers it" (U-1). The relay's `:606` "short read-only polls" is unchanged baseline text about session monitoring.
- **One handoff block:** C-PLACE.
- **PR-40's independent verification:** stated in C-DISPATCH.
- **Single Proceed within a plan:** the PR skill's line 9; only a PR-40 `REJECT` re-plan gets a new Proceed.

**Question: is anything outside the stated scope?**
- No. Every changed path is named by spec v2 or a repair script.
- The only round-a5 byte changes are R1–R3 and the tree digest.

## Claims C1–C8

| claim | holds on these bytes? |
|---|---|
| C1 | Yes (§8c; the historical files are byte-unchanged). |
| C2 | Yes (§8h). |
| C3 | Yes: `fecc319b…`/284 in the graph and in the contract. |
| C4 | Yes, per the author's regressions, which I re-ran exactly. |
| C5 | Yes, in the edited lines I read (A7, A9). |
| C6 | Yes (§8d–f; A3a and A3b). |
| C7 | Yes for every gate I ran. E3/E4 is not re-measured (L1). |
| C8 | Yes as worded. Deletions, moves out of a passage, and every non-marker comment fail. The residuals F1–F3 lie outside its wording. |

## Scratch and writes

- Scratch: `/tmp/claude-0/review-SFR-A5-2/`. It holds the extracted trees, `copy/`, `base/`, `k/` and `k4/`, and `root/`, `out/`, `hist/`, `regs/`, `regout/` and `probe/`.
- Repository writes: this record only. No `__pycache__` was created in the repository or in the synced tree.

## DECISION NEEDED

The verdict is **SKILL_FIT_CONFIRMED** on the §1 digests. Nathan chooses one of these, and this verdict does not depend on which:
- **(a) Install as reviewed.** Record F1–F4 as known limits: F1 and F3 widen §2's list, and F2 and F4 are noted.
- **(b) Fold F1, F2 and F4 into flowmaster-validate** (small edits to `matrix_indented_code_lines`, `DISPATCH_ALLOWED_COMMENT_RE` and the token list), with or without F3(a). That changes `394bb1ae…`, so this verdict would be void and a fresh review needed.
