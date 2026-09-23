---
artifact_type: SKILL_REVIEW_RECORD
round: a5
reviewer: SFR-A5-1
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a5.md (committed at b65f754; 16561 bytes; sha256 80a7ce77fab20fc4e046df97a5bc04770150ecf1f82532d7d9cf9257b2ca5aee, verified against the working file and the b65f754 blob)
branch_head_read: b65f7545b1d5e47eec55839ce02f61922e25002c (docs/20260923-modification-intake-alpha-feedback-open-entries, PR #474, not merged)
date: 2026-09-23
successor_of: none (a new record; no earlier record is edited, AUTH-001)
---

# Section 10 review, round a5 — SFR-A5-1

## Verdict

**SKILL_FIT_CONFIRMED**

This verdict applies only to these six packages, as I measured them from the bytes in `/tmp/claude-0/pkg5/new/`:

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54899 | `0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7` |
| change-flow.skill | 22 | 257990 | `af8cff939b1b94ced1c487dbcb6b87a6ccb9904304b3ca7cc621fd0798c34902` |
| flowmaster-validate.skill | 31 | 319235 | `394bb1ae208607f46170b481153e4e00b7f93fe65150c872bc401c1406f59d22` |
| glow-hde-pr-development.skill | 4 | 22494 | `dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913` |
| session-relay-flowmaster.skill | 5 | 56330 | `30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b` |
| tw-flowmaster.skill | 2 | 20368 | `db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf` |

**It is void for any other bytes.** It carries no confirmation from an earlier round.

**Why it passes:**
- Every gate in brief §8 passes on these bytes.
- The historical layer is byte-equal to baseline.
- Every one of the author's regressions reproduces on my re-pathed copies of the harnesses. The only exception is a4's K3, and that is an artifact of how I re-pathed it: run directly, the same recipe gives EQUAL.
- Each round-a4 finding is closed as §2 says.

**What my own probes found.** They found no path by which a re-stamped change alters any **value** that a consumer reads. Three residuals remain, all in the same category as the volunteered limits:
- **N1:** at the nine dispatch sites, text can be hidden in rendered Markdown without using `<!--`.
- **N2:** an indented code block inside a block quote still passes FMV-ORACLE-022.
- **N3:** row order in the runtime map is not checked.

All three are display-only or semantic no-ops. Each can be closed either by a one-line code change or by narrowing a claim, so none blocks installation. N1 makes C8's phrase "any HTML comment" too broad, so it should be narrowed or fixed before the claim is relied on.

## Stability

- Baseline freeze digests reproduce exactly, measured both before and after the review:
  - flowmaster-validate 29 `b9ca212a…`
  - change-flow 21 `80e877c2…`
  - glow-hde-pr-development 4 `e109d47a…`
  - session-relay-flowmaster 5 `4ef8daa3…`
  - amthor-workspace-governance-audit 15 `6cd088a0…`
  - tw-flowmaster 2 `fa3fac85…`
  - glow-graph-contract 6 `4e671ddc…`
- The tree did not move during the review.
- The branch HEAD stayed at `b65f754` and the working tree stayed clean.
- The package digests were unchanged at the end.

## §8a Archives

- **Contents:** the entry counts equal the file counts (15/22/31/4/5/2). No archive has a directory entry, a symlink, an absolute path, a `..` component or a backslash. Every entry sits under its own skill root.
- **Names:** the `name:` line in each SKILL.md is unchanged from the installed tree.
- **Freeze digests of the extracted trees:**
  - flowmaster-validate 31 `a79401deaabe35ce…`
  - change-flow 22 `ee546df57f3d5f0f…`
  - glow-hde-pr-development 4 `68077fa6620992…`
  - session-relay-flowmaster 5 `15aef9890ebfa286…`
  - amthor 15 `819915e4a57184fd…`
  - tw-flowmaster 2 `fd6c344befd9ce9e…`

  All six equal §3.
- **Against round a4:** five packages are byte-identical to `/tmp/claude-0/pkg4/new/`. The a4→a5 difference is exactly `flowmaster-validate/SKILL.md` (SKILL_TREE_SHA256 moves from `d6fa3c03…` to `be70787a…`) and `scripts/validate_flowmaster.py` (R1, R2 and R3 as §2 describes). Nothing else changed.

## §8b Gates I ran

I ran these from a full scratch copy of the synced tree with the six skills replaced, using `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` in scratch.

`<root>` holds only `graph/GCFPE-20260914.1-Candidate-Graph-Contract.json`. It is the embedded JSON of my own `graph_parts.py build` of the branch's `docs/graph/parts`: 55/229/55, 575074 B, `ae2bd159f0ba947c…`. That graph is byte-equal to the bundled graph in both skills.

| gate | result (the tool's own flag) |
|---|---|
| validate_flowmaster.py --skills-root | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, findings [] |
| same, --strict-warnings --gcfpe-contract … --gcfpe-candidate-root | `suite_ok: true`, `FLOWMASTER_SUITE_PASS`, findings [], every nested `ok`/`fixture_suite_ok` true |
| validate_gcfpe_20260914.py <cf> --contract | `"ok": true`, errors [], contract `6902924a…`, graph `ae2bd159…` 55/229 |
| run_gcfpe_20260914_fixtures.py | `fixture_suite_ok: true`, 228 cases, 228 `passed: true` |
| validate_gcfpe_current.py | `"ok": true` |
| run_gcfpe_current_fixtures.py | `fixture_suite_ok: true`, 228/228 |
| run_change_flow_fixtures.py | `fixture_suite_ok: true`, 32 expectations, 0 failed |
| <cf>/scripts/validate_gcfpe_20260914.py | PASS, exit 0 |
| validate_glow_hde_pr_development.py | PASS |
| validate_relay_manifest.py --self-test | `status: PASS`, 230 cases, 230 ok |
| amthor run_fixture_suite.py | 35 tests OK. Baseline is 34; the added test is `test_pr40_once_per_merge_parity`. |
| amthor validate_project_prompt_registry.py (registry on the branch) | `{"valid": true, "problems": []}` |

**Historical layer (the 12 commands of spec v2 §2).** I ran each command on a fresh baseline copy and on the new copy. All 12 give exit 0 on both, and every output is **byte-equal** to baseline, both raw and after path normalisation. Every flag is `ok`/`PASS`/`fixture_suite_ok` true, and commands 6–9 produce empty output.

**The author's regressions.** Their harness scripts write to fixed paths in `/tmp/claude-0/repair4` and `/tmp/claude-0/e2`, which my brief does not let me write to. So I derived them with `derive_regressions_a4.py` into my scratch, re-pathed them with `sed` to `/tmp/claude-0/review-SFR-A5-1/rr`, and ran them against a disposable copy of the tree.

| suite | result | author's value |
|---|---|---|
| oracle | 15 of 15 exact | 15 |
| skills | 70 of 70 exact | 70 |
| contract | 53 + 35 + 3 exact | 53 + 35 + 3 |
| fixtures | 2 of 2 exact | 2 |
| a1 | 17 of 17 exact | 17 |
| a2 | 34 of 34 exact | 34 |
| a3 | 13 of 13 exact | 13 |
| a4 | 10 of 11 exact | 11 |

**The one non-exact case is a4's K3.** It calls `contract_recipe.py` next to the harness file, and in my re-pathed copy that file is not there. The recipe also has to run from the repository, because it resolves the repository from its own location. So this is an artifact of my re-pathing, not a defect in the change.

I ran the recipe itself from the repository (§8h below): exit 0, and both shipped contracts are EQUAL. P1–P4 and M1–M5 are exact on these bytes.

**Not run:**
- Brief §7 L1: E3/E4 (`run_e4.py` over the Notion bodies). This is optional and I did not fetch the bodies, so I make no claim about E3/E4 beyond the report existing.
- The author's control run `regress_repair_a4_on_pre.out` on the round-a4 tree. I did not re-run it.
- No post-install check exists (L2).

## §8c Diff against the installed tree (derived with `diff -rq`)

**Changed (26 files):**
- **amthor:** SKILL.md, references/behavioral-fixtures.md, references/interoperability-contracts.md, references/project-prompt-registry-schema.md, scripts/run_fixture_suite.py.
- **change-flow:** SKILL.md, references/…candidate-graph-contract.json, references/…direct-handoff-contract.json, scripts/validate_gcfpe_20260914.py.
- **flowmaster-validate:** SKILL.md; fixtures/change-flow/scenarios.json and fixtures/gcfpe-20260914.1-091426.1/scenarios.json; references/…candidate-graph-contract.json, …direct-handoff-contract.json and …validation-profile.json; scripts/run_change_flow_fixtures.py, run_gcfpe_20260914_fixtures.py, run_gcfpe_current_fixtures.py, validate_flowmaster.py, validate_gcfpe_20260914.py and validate_gcfpe_current.py.
- **glow-hde-pr-development:** SKILL.md, references/behavior-cases.md, scripts/validate_glow_hde_pr_development.py.
- **session-relay-flowmaster:** SKILL.md.
- **tw-flowmaster:** SKILL.md.

**Added (3):**
- change-flow references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json
- flowmaster-validate references/glow-hde-canonical-change-flow-r1-20260923.json
- flowmaster-validate references/r1-successor-source-20260923.md

**Unchanged:**
- the historical oracle (`52807e58…`) and historical map (`5574666e…`);
- the older contracts;
- every historical-layer validator and runner;
- the relay's validator.

**Scope.** I traced the non-obvious prose edits to spec v2 wording: the relay's Notion/`docs/ephemeral` line, "provisioning does not apply", and the usage-record "never to the handoff". I did not re-derive the full §8a/§8b/§5/§6 file list from the spec text. The set above is consistent with it and with the author's a4 list.

## §8d Rosters and contracts

**Successor oracle** (`ede635b1…`):
- **Rows:** 46 rows in historical order. Exactly GCF-14 (`consumes`), GCF-17 (`name`, `actor`, `session`, `failure_stop_condition`) and GCF-17.LINEAGE (`next`, `failure_stop_condition`) differ, each also in `source_row_sha256`. Each keeps its position and key order.
- **Top-level keys:** only `profile_id`, `required_global_tokens` (the in-place profile token swap) and `authority` differ.
- **Authority block:** it keeps the four historical attestation fields plus `r1_contract_matrix_sha256`. It adds `successor_source_matrix_sha256` = `8b443eb1…`, `successor_rows` (the three ids) and `successor_authority` "D23-D, D23-F; Product Owner 2026-09-23".

**Successor matrix** (`8b443eb17180f85e…`):
- It is byte-equal to `docs/prompt_ecosystem_management/r1-successor-source-20260923.md` on the branch.
- It has three `json` blocks, each with the key order `R1_ROW_CONTENT_FIELDS + supersedes_source_row_sha256`.
- Each block equals its oracle row on all eleven content fields.
- Each block's recomputed digest (sorted-key compact JSON of the eleven fields) equals the row's `source_row_sha256`, the `source_row_sha256:` line, and `SUCCESSOR_ROW_SHA256` in the validator: `42db7a9e…`, `6774529…`, `73a133c1…`.
- Each `supersedes_source_row_sha256` equals the historical row's digest.
- The 43 historical rows keep the original R1 digests. Those are not recomputable by the successor formula, which is expected because they attest the original R1 matrix.

**Successor map** (`aa6ed8e3…`): it equals the projection `{profile_id, authority, coverage, runtime_rows}` of the successor oracle, in that key order.

**Contract and graph:**
- `validate_graph_contract(contract, graph)` returns `[]`.
- The routing surface is `fecc319bdd4ce7ee6201cb77d7231861`/284 on both the shipped contract and my graph build. Baseline is `7380cd14…`/282.
- The graph has 55 nodes and 229 edges (baseline 227).
- The contract and graph both pin `r1_oracle_sha256` = `ede635b1…`. The contract's `frozen_candidate_graph.sha256` = `ae2bd159…`.

## §8e Hash pins, recomputed

I extracted every 64-hex literal in each changed file. Each one resolves to one of:
- the sha256 of a file in the new tree;
- the flowmaster-validate tree digest (`SKILL_TREE_SHA256` `be70787a…` = `skill_tree_digest`);
- a verified row digest; or
- an external identity (`faa7fb7d…` R1 contract matrix, `5a6d89ed…` frozen snapshot, `4d8bb9bf…` Primary core, `4b2b0d19…`, `e14c9fa0…`, `252fbc9a…`, `a8f3351c…`, `94562065…`, `4a254519…`, `94478a23…`).

Each external identity occurs in exactly as many files as it did in the baseline tree.

None of these stale identities appears anywhere in the new tree: `2b78f877…`, `90021eb7…`, `eb9634d6…`, `7380cd14…`, `b1911cf5…`, `d6fa3c03…`, `7a7fd028…`.

## §8f Revision sites, recounted by grep

- **The once-per-merge sentence** occurs once in each of the nine carrying files:
  - PR skill SKILL.md and behavior-cases.md
  - change-flow, relay, tw-flowmaster and flowmaster-validate SKILL.md
  - amthor SKILL.md, interoperability-contracts.md and behavioral-fixtures.md

  It also occurs once in each of the two contracts, in `flowmaster-validate/scripts/validate_gcfpe_20260914.py`, in the PR-skill validator and in the amthor suite, and three times in `validate_flowmaster.py` (its pins). It is not in the graph.
- **The C-DISPATCH passage** opens once at each of the seven carrying SKILL/interop sites.
- **The fallback predicate occurrences** equal `DISPATCH_SITES` (2, 4, 1, 1, 2, 2, 2, 2, 2). The suite's own raw count agrees, and grep line counts are consistent with it.

## §8g My own must-fail probes, under the full re-stamp

**Harness.** I used `regress_repair_a4.py`'s `fresh`, `move`, `restamp`, `restamp_map_only` and `tree_stamp`, re-pathed to my scratch. `restamp` is the same full re-stamp that `regress_oracle.py` uses. Each probe ran both the default suite and the candidate suite. My scripts are `/tmp/claude-0/review-SFR-A5-1/probes.py` and `probes2.py`. The control C0 (a clean re-stamped copy) passes both suites.

**FMV-GCF-DISPATCH-001, comment rule (R1):**

| id | mutation | result |
|---|---|---|
| D1 | change-flow: `<!x … paste both.>` (HTML bogus comment) after the passage | **passes** (N1) |
| D2 | PR skill: `<?PR-40 may be entered twice…?>` after the passage | **passes** (N1) |
| D3 | relay: unclosed `<script type="text/plain">` line before the passage | **passes** (N1) |
| D4 | tw-flowmaster: unclosed `<![CDATA[` before the passage | **passes** (N1) |
| D5 | amthor SKILL.md: `[//]: # (Paste both …)` link-reference comment idiom | **passes** (N1) |
| D6 | flowmaster-validate: `<details>` before the passage (in place) | passes. This is the volunteered limit. |
| D7 | change-flow: unclosed `<div hidden>` before the passage | **passes** (N1) |
| D8 | behavior-cases: `<template>Paste both blocks.</template>` | **passes** (N1) |
| D9 | an extra whole-line `<!-- FLOWMASTER_NOTE -->` | passes, by design (closed, identifier-only) |
| D10 | legitimate prose `PR-35 --> PR-40` in interoperability-contracts.md | **fails** FMV-GCF-DISPATCH-001 (over-reach, see N4) |
| D11 | a marker with a double space | fails FMV-GCF-DISPATCH-001 + FMV-SKILL-STRUCTURE-001 (correct) |

The a4 regressions P1–P4 (a comment inside the passage, an unclosed `<!--`, `--!>`, a closed comment after the sentence) are exact on these bytes.

**FMV-ORACLE-022, matrix elements and indentation (R3).** In each probe a fourth JSON "row" is appended to the matrix, followed by the full re-stamp with `matrix_changed=True`.

| id | mutation | result |
|---|---|---|
| X1 | `>     {…}`, a 4-space indented code block inside a block quote | **passes** (N2) |
| X2 | indented code under a list item (8 spaces) | fails FMV-ORACLE-022 |
| X3 | `<code>` element | passes (inline code element, not a code block; see N2) |
| X4 | `<script type="application/json">` | passes (hidden, not rendered as code) |
| X5 | a list item whose content begins with 4+ spaces | fails FMV-ORACLE-022 |
| X6 | `<PRE` + newline | fails FMV-ORACLE-022 |
| X7 | whitespace-only indented line | passes (correct; not code) |

**FMV-GCF-MAP-005 and the map (R2):**

| id | mutation | result |
|---|---|---|
| K1 | the map's `authority` keys reversed, map pin re-stamped | passes (nested key order is not claimed) |
| K2 | the map re-serialised with indent 4 | passes (a semantic no-op) |
| K3 | the map's `runtime_rows` reversed | **passes** (N3) |
| K4 | the top-level `authority` and `coverage` swapped | fails FMV-GCF-MAP-005 (R2 works) |

**The oracle (A3):**

| id | mutation | result |
|---|---|---|
| A1b | GCF-15 `next` += GCF-17 | fails FMV-ORACLE-015 |
| A1c | GCF-15 `failure_stop_condition` edited | fails FMV-ORACLE-015 |
| A1d | as A1c, with the row digest recomputed by the successor formula | fails FMV-ORACLE-015 |
| A2 | GCF-17 `session` edited, digest recomputed, matrix untouched | fails -012, -018, -021 |
| A3 | the same edit in both oracle and matrix, every digest re-stamped | fails FMV-ORACLE-021 (the approved-digest constant) |
| A4 | GCF-14 swapped with its neighbour | fails FMV-ORACLE-019 |
| A5 | a fourth id added to `successor_rows` | fails FMV-ORACLE-010 |
| A6 | historical `authority.r1_verdict` changed | fails FMV-ORACLE-016 |
| A7 | one historical row removed | fails -005, -015, -019 and others |

My first A1 was a no-op: it concatenated a string onto a list, which left the value unchanged. I discarded it and re-ran it as A1b–A1d.

**Rendering.** No Markdown renderer is installed here, and I may not install one. The claims about what D1–D8 and X1 **render** as come from the CommonMark and HTML parsing specifications (HTML block types 1, 3, 4, 5 and 6; bogus-comment state; indented code inside a block-quote container). I did not execute a renderer, and a hosting sanitizer may strip some of these constructs.

## §8h Regenerator, recipe, graph and routing surface

I ran `repair-a4/contract_recipe.py <my graph.md> <installed contract 2b78f877…> <new oracle> <scratch out> --check <both shipped contracts>`:
- E2 regenerator output: `7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675`, 613162 B.
- Recipe output: `6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718`, 613326 B.
- Both shipped contracts are **EQUAL**, and the exit code is 0.

A structural diff of the E2 output against the shipped contract shows exactly one difference: `route_graph_semantics.pr40_entry`, which is W4 with the D23-E sentence appended.

The graph build and routing surface are unchanged from what Nathan read: `ae2bd159…`, 55/229/55, `fecc319b…`/284.

Not re-run: C2's non-no-op half, which reproduces `2b78f877…` from a stripped template.

## Findings

### N1 (minor, non-blocking; claim-level): the comment rule covers only `<!--` syntax, so C8's "any HTML comment" is too broad, and rendered hiding remains possible

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `dispatch_contract_findings`. The residue test is `any(token in residue for token in ("<!--", "-->", "--!>"))`.
- **Defect:**
  - Other constructs that an HTML parser turns into comment nodes pass every gate at the carrying sites: a bogus comment `<!x …>`, a processing instruction `<?…?>`, and an unclosed `<![CDATA[`.
  - So do elements that hide content from a rendered view: unclosed `<script>`, `<template>`, `<div hidden>`, and the Markdown `[//]: # (…)` idiom.
  - Some of these can hide the whole passage in place (D3, D4, D7), which is the rendered-view effect behind SFR-A4-2 F1 defect 2.
- **Evidence:** probes D1–D5, D7 and D8 above. All pass both suites.
- **Why it is not blocking:**
  - Raw counting (R1) closes the substantive half of F1, where text is inserted inside the passage.
  - A model reads the raw file, so hidden text is no stronger for it than a visible contradicting sentence outside the passage, which is a volunteered limit.
  - Every value pin still holds.
- **Smallest correction (choose one):**
  - (a) Add `"<!"` and `"<?"` to the residue tokens. This closes D1, D2 and D4. Then list "text hidden by raw-HTML elements (`<script>`, `<template>`, `hidden`, `<details>`) or the `[//]: #` idiom" as a known limit, and narrow C8 to `<!`/`<?`-introduced markup.
  - (b) Keep the code, and narrow C8 to "`<!--`-delimited comments", with the same limit entry.

### N2 (minor, non-blocking; display-only): FMV-ORACLE-022 misses indented code inside a block-quote container

- **Artifact:** `matrix_indented_code_lines`. It tests `line.startswith("    ")` on the raw line, while `MATRIX_CONTAINER_PREFIX_RE` is applied only for fence detection.
- **Defect:** `>     {…}` (block-quote marker, then 4+ spaces) is an indented code block inside a block quote. It renders as code, and it passes. The list-item form (X2, X5) is caught, only because those lines start with spaces.
- **Evidence:** probe X1 passes both suites. X3 (`<code>`) also passes, but that is an inline element rather than a code block, so I record it only as context.
- **Impact:** display only. FMV-ORACLE-011, -012 and -021 pin the parsed values, as for SFR-A4-2 F3.
- **Smallest correction:** in `matrix_indented_code_lines`, strip `^[ \t]{0,3}>[ \t]?` block-quote markers repeatedly before the indentation test, and add X1 as a must-fail regression. Alternatively, record block-quote-nested indented code as a limit of R3.

### N3 (minor, non-blocking; semantic no-op, pre-existing): row order in the runtime map is not checked

- **Artifact:** `validate_flowmaster.py`, the `contract_map != expected_projection` branch. It compares rows by `id` only, and R2's order test covers top-level keys only.
- **Evidence:** K3 (rows reversed, map pin re-stamped) passes. The oracle's own row order is enforced (A4 fails FMV-ORACLE-019), but the map's is not. The baseline validator had the same row-by-id logic, so this is not a regression introduced by a1–a4.
- **Smallest correction:** add `[r.get("id") for r in contract_map["runtime_rows"]] == [r["id"] for r in oracle["runtime_rows"]]` as FMV-GCF-MAP-005. Alternatively, leave the code and state that map row order is not pinned.

### N4 (observation; over-reach, no current effect): the comment rule rejects a legitimate `-->` arrow

- **Artifact:** the same residue test.
- **Evidence:** D10. Prose `PR-35 --> PR-40` in a carrying file fails FMV-GCF-DISPATCH-001. None of the nine files uses `-->` today, so there is no current false positive.
- **Correction:** none needed. Optionally, name the constraint in the rule's message or in the SKILL text, so a later author writes `->` or `→`.

## Round-a4 findings: does §2's disposition close each one on these bytes?

| finding | disposition | closed? |
|---|---|---|
| SFR-A4-2 F1 (required) / SFR-A4-1 A4-2: comment stripping | R1: raw counts plus the comment rule | **Yes, for `<!--`-syntax comments.** P1–P4 are exact, and a comment inside the passage fails again. The residual non-`<!--` hiding is N1 (claim-level). |
| SFR-A4-1 A4-1 / SFR-A4-2 F2: map key order unreachable | R2 | **Yes.** M1 and my K4 fail FMV-GCF-MAP-005. The row-order residue is N3, which is outside F2's scope. |
| SFR-A4-1 A4-3 / SFR-A4-2 F3: indented code, `<xmp>`, `<listing>`, `<textarea>` | R3 | **Yes, as stated.** M2–M5, X2, X5 and X6 fail. The block-quote-nested residue is N2. |
| SFR-A4-1 A4-O1: the regenerator table lacks the pr40_entry value | R4, contract_recipe.py | **Yes.** It reproduces both shipped contracts byte for byte, and E2's output differs only in pr40_entry. |
| SFR-A4-2 F4: moving the whole passage intact | limit, with C8 narrowed | **Yes, as a limit.** D6 confirms that `<details>` in place passes, which is the volunteered limit. |

## Answers to §6

- **A1 (the a4 repairs).** Can a re-stamped or text-only change still pass?
  - No value change passes. Every oracle, matrix and map value mutation I tried fails.
  - Text-only display changes do pass: N1 at the dispatch sites and N2 in the matrix.
  - contract_recipe.py is correct.
- **A2 (weakening or over-reach).**
  - Nothing is weaker than on the a3 tree. Raw counting restores the a3 behaviour for insertions inside the passage.
  - The marker allowance `^<!-- FLOWMASTER_[A-Z_]+ -->$` admits only closed, identifier-only lines. The only markers present today are the six real section markers.
  - The comment rule can reject legitimate `-->` prose (N4).
  - The pinned sentence contexts are narrow, single-sentence contexts. I found none that is wrong.
  - The graph (`ae2bd159…`) and routing surface (`fecc319b…`/284) are as Nathan read them.
- **A3 (successor oracle provenance).**
  - The matrix bytes equal the branch copy (`8b443eb1…`), which the oracle's authority pins.
  - The digest formula recomputes all three rows.
  - The authority block is as §5.5 describes.
  - A third-row change fails FMV-ORACLE-015 (A1b–d), as do a successor-row reorder (-019), a fourth id in `successor_rows` (-010), a historical authority edit (-016) and an in-both-files re-stamp (-021).
  - I did not audit N1–N10 individually beyond the oracle regressions (15/15 exact).
- **A4 (once-per-merge and the fallback predicate).** I found no double-dispatch or no-dispatch path.
  - If Nathan pastes the fallback before a late MERGE_OBSERVED arrives, "Once either has been pasted, the other is void" voids the late handoff.
  - If MERGE_OBSERVED is returned, the predicate voids the fallback, and the MERGE_OBSERVED handoff stays usable.
  - If the MERGE_OBSERVED session is lost, RS-40 can resume the PR-35 phase and return its lawful result.
  - The two fixture texts each carry the sentence once and the predicate twice, pinned by contexts.
- **A5 (the regenerator's value table).**
  - Every After block in spec v2 §6.3 (contract-only and mirrored) is a subset match for the shipped contract, except `route_graph_semantics.pr40_entry`. That key carries the H5 append, which contract_recipe.py reproduces.
  - The regenerator's W4 is stale on its own. The recipe is the documented successor step, and validate_gcfpe_20260914.py pins the final value.
  - I found no wrong value that no check reads.
- **A6 (reversed validator literals).** Every reversed literal I read in the PR-skill validator and the amthor suite has a forbidden counterpart for the retired text:
  - "one dedicated PR-development session"
  - "same-session `PR-35` handoff"
  - the old vocabulary
  - the ten-field continuity list

  So the kept rule is still guarded. The skills regressions are 70/70 exact.
- **A7 (the GCFPE override of the core option to create a session).**
  - change-flow, the relay and tw-flowmaster each carry the override sentence once. The relay scopes `SESSION_PROVISIONING_REQUIRED` to "Outside a GCFPE main-ecosystem stage" at both provisioning lines, and adds "provisioning does not apply" for GCFPE stages. That wording repeats the override without contradicting it.
  - A sweep of every SKILL.md found no affirmative instruction to create, spawn, launch or schedule a session, or to run a main-ecosystem prompt as a subagent (C5).
- **A8 (spec §12, its addendum, and G11).**
  - §12 sets G11's expected set at two wrapper codes. §E records the four measured findings, with the mechanism: under S-5 the default overlay runs the same profile checks, adding FMV-GCF-CURRENT-001 and its fixture finding.
  - That explanation is consistent with the code, and the oracle regressions reproduce it exactly.
  - I did not re-litigate the other §12 choices.
- **A9 (contradictions with kept rules).** I found none.
  - No agent merges, and "no session is created by an agent" appears inside C-DISPATCH.
  - No polling: "stay subscribed and do not poll"; "Subscribing is not polling".
  - One handoff block: "exactly one complete `PR-35` handoff".
  - PR-40's independent verification is kept.
  - One Proceed per approved per-PR plan is pinned.
- **Question: is anything outside scope?** The edits I sampled trace to spec v2 texts (§3.6, §8b O2(b), the §8a revisions). I found nothing outside Amendment 1, the a1/a2 repairs, the a3 hardening, the a4 repairs or D23-E. This was not an exhaustive line-by-line audit of every prose edit.

## Claims C1–C8

| claim | holds? |
|---|---|
| C1 | Holds on what I checked: the diff set, historical files byte-unchanged, and the a4 delta confined to two files. |
| C2 | Holds, except the non-no-op half, which I did not re-run. |
| C3 | Holds. |
| C4 | Holds on the regressions and A6. |
| C5 | Holds on my sweep. |
| C6 | Holds. |
| C7 | Holds for everything I ran. E3/E4 were not re-run. |
| C8 | **Holds except for its "any HTML comment" wording** (N1). Deletions and moves out of pinned passages or sentences fail, and so does any `<!--` comment other than a marker. The contract carries the D23-E sentence, and the graph and routing surface are unchanged. |

## Writes

- **Scratch only:** `/tmp/claude-0/review-SFR-A5-1/`.
- **Repository:** this record only.
- I did not install anything, write to the synced skills directory, commit, merge, or touch pfcanon, the registry, the graph parts, Notion or any prompt body.
- No `__pycache__` was created.

**NOTHING NEEDED.** The verdict does not depend on any correction. Nathan may optionally choose (a) or (b) for N1, and code or limit wording for N2 and N3, in a later round.
