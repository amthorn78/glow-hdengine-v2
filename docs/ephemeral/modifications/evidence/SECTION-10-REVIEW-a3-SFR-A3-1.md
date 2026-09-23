---
artifact_type: SKILL_REVIEW_RECORD
reviewer: SFR-A3-1
round: a3 (Amendment 1 of MODIFICATION-20260923-alpha-feedback-open-entries, after repair round a2)
brief: docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a3.md (commit c22bc64, 16580 bytes, sha256 c29a5a8b09fbbb297d4ffd86eddbde01aa0aa3374e8c69b52bd14cdc2e1d7af5, verified before reading)
reviewed_at: 2026-09-23, ending 10:30Z
branch_head_at_start: c22bc64280000d6cf4ca68d5348636a79f91896a
branch_head_at_end: 72bd27cdcbe80cff2046b8697c968f49e3cac877 (adds only SECTION-10-REVIEW-a3-SFR-A3-2.md; I did not read it)
---

# §10 review, round a3 — SFR-A3-1

## Verdict

**SKILL_FIT_CONFIRMED.**

It is bound to exactly these six packages, which I read from `/tmp/claude-0/pkg3/new/`:

| package | files | bytes | sha256 |
|---|---|---|---|
| amthor-workspace-governance-audit.skill | 15 | 54899 | 0070d61c90dd6877ebf5aa3b71ce2a35e9c921b47b19129fabbf6847b2f7cfe7 |
| change-flow.skill | 22 | 257909 | 97bf899c6135cdafea9ff5b34a4ac6c00c68fe402266598e05b91dcc675990a0 |
| flowmaster-validate.skill | 31 | 317639 | e8eeda442162081257e6a75e08813d7f4707213c5acbb2fa171505b8544ae766 |
| glow-hde-pr-development.skill | 4 | 22494 | dadf64b24b2a0c08931d5afb59123bb72e4a1cab85e738d05bffa91dafba2913 |
| session-relay-flowmaster.skill | 5 | 56330 | 30fdce6af87f350950fc11fdd0a2ef96412c31311bd4b2d1194248fec2c9952b |
| tw-flowmaster.skill | 2 | 20368 | db4cde530883f790a2f6118090cbb71661eac3902585b8e411cbc66ec025dabf |

**The verdict is void for any other bytes**, and for any subset of the set.

I found no blocking defect:
- Every round-a2 finding is closed on these bytes, with one minor residual (F1 below).
- Every gate the brief names passes on my own run.
- Every claimed regression count reproduces exactly.
- My own must-fail probes against the round-a2 checks fail where they should, except for the residual and the limits listed below.

I raise one minor finding and two advisories. None is a runtime or routing defect. None blocks installation. Each can go into the next revision.

## Findings

### F1 (minor, non-blocking): FMV-ORACLE-022's "no other code fence" rule misses container-prefixed fences
- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `MATRIX_FENCE_RE = re.compile(r"(?m)^ {0,3}(?:`{3,}|~{3,})")` and the FMV-ORACLE-022 fence count.
- **Defect.** Repair S4(a) and claim C6 say the matrix has "no other code fence" besides the three JSON blocks. The regex counts only fences that start in columns 0 to 3. A fence inside a block quote (`> ```json`) is a real CommonMark fenced block, and the regex does not count it.
- **Evidence.** In probe P9b I appended a block-quoted `json` fence to the matrix prose, holding a fake `{"id": "GCF-16"}` block. I moved `authority.successor_source_matrix_sha256` and re-stamped every pin with the `regress_oracle.py` recipe. Both suites returned `FLOWMASTER_SUITE_PASS` with `[]`.
  - Controls that are caught: P9 (a `~~~` fence) and P20 (a list-item `- ```json` fence whose closing line is indented 2). Both fail FMV-ORACLE-022.
  - This is the residual of SFR-A2-1 R2-3, and of SFR-A2-2 V-d, whose `json5` form is now caught.
  - **Effect:** readability and provenance only. The machine parser `MATRIX_BLOCK_RE` ignores the quoted block, and the matrix bytes stay pinned by FMV-ORACLE-009.
- **Smallest correction.** Count fence openers after stripping container prefixes, for example `(?m)^(?:[ \t]*>[ \t]?)*[ \t]*(?:(?:[-*+]|\d+[.)])[ \t]+)?(?:`{3,}|~{3,})`. Add P9b as a must-fail regression. Alternatively, narrow the claim to "no top-level code fence".

### Advisory V1: FMV-GCF-DISPATCH-001 silently skips a site whose skill is absent, and its comment misstates who reports that
- **Artifact:** `validate_flowmaster.py`, `dispatch_contract_findings`. The line reads `if skill not in skills:  # absence is FMV-SKILL-STRUCTURE-001's to report`.
- **Evidence.**
  - FMV-SKILL-STRUCTURE-001 covers only `EXPECTED` and the marked specializations. `amthor-workspace-governance-audit` is neither.
  - P18 (amthor removed from the skills root) passes both flowmaster suites.
  - P14 (amthor's frontmatter `name:` changed, and the D23-E sentence broken in `interoperability-contracts.md`) passes both flowmaster suites. Only the amthor suite fails it (rc 1).
  - For the PR skill, P13 (removed) is caught, but by FMV-GCF-CURRENT-001 `SKILL_MISSING`, not by FMV-SKILL-STRUCTURE-001.
- **Why it does not block:** the brief's full gate runs amthor's own suite, which catches P14 through `test_pr40_once_per_merge_parity`, and cannot run at all in P18.
- **Smallest correction:** in `dispatch_contract_findings`, emit an FMV-GCF-DISPATCH-001 finding when a `DISPATCH_SITES` skill is absent, or fix the comment.

### Advisory V2: the new successor runtime map can carry an extra top-level key under re-stamp
- **Artifact:** the `validate_flowmaster.py` runtime-map projection check (FMV-GCF-MAP-004/005/006).
- **Evidence.** In P19 I added `"notes": "PR-35 may run as a subagent"` to `glow-hde-canonical-change-flow-r1-runtime-map-20260923.json` and moved the map pins. Every suite passes: both flowmaster suites, the PR validator, amthor, both 20260914 validators and the current validator.
  - The map should be exactly the oracle projection (`profile_id`, `authority`, `coverage`, `runtime_rows`).
  - The comparison logic predates this change, and SFR-A2-1 noted it as unmeasured. It applies here to a file this change creates.
  - No consumer reads the extra key.
- **Smallest correction:** require `set(contract_map) == {"profile_id", "authority", "coverage", "runtime_rows"}` under FMV-GCF-MAP-005, plus a regression.

### Limits (stated so they are not mistaken for passes)
- **L-a, in-package pins.** In P2b, GCF-14 `consumes` drops `pr_work_unit_lineage_review`, consistently across the oracle, matrix, digest line and authority, under a full re-stamp.
  - With the constant kept, FMV-ORACLE-021 fires alone: this is the R2-2 closure.
  - If the `SUCCESSOR_ROW_SHA256` constant is also edited and the tree re-stamped, every suite passes.
  - This is inherent: the approved digests are a literal in the same validator. They are also recorded outside the package, in the repository's `r1-successor-source-20260923.md` (byte-equal to the bundled copy, 8b443eb1…) and in spec v2.
- **L-b, literal guards count occurrences, not placement or meaning.**
  - P11: the anchored D23-E sentence was moved out of change-flow's C-DISPATCH paragraph into a trailing HTML comment. It passes.
  - P12: "If both arrive, paste both." was appended after it. It passes.
  - No forbidden-literal check covers a contradiction of D23-E. This is the ordinary limit of required-literal validation, not a regression.

## Answers to §6

- **A1 (round-a2 repairs).**
  - **FMV-GCF-DISPATCH-001** holds at all nine files.
    - My independent recount matches `DISPATCH_SITES` exactly, with predicate counts PR 2, change-flow 4, relay 1, tw 1, fv 2, amthor SKILL 2, interop 2, behavior-cases 2 and behavioral-fixtures 2. The once-per-merge sentence occurs exactly once per file, in the anchored form at the seven C-DISPATCH sites.
    - No other prose file in the six trees carries either text. The bundled graph and contract carry `MERGE_OBSERVED` only as data.
    - Nine is the right set: no carrying file is missing, and none should not be pinned.
    - P16 (tw predicate deleted) and P17 (behavior-cases sentence deleted) fail FMV-GCF-DISPATCH-001.
  - **FMV-ORACLE-021** fired on P1 (an unapproved value in GCF-17.LINEAGE `next`, consistent everywhere and re-stamped) and on P2b.
  - **FMV-ORACLE-022** fired on P8 (GCF-16 key order), P9 and P20. The residual is F1.
  - **strict_json_loads:**
    - Duplicates in the oracle (P3 top-level, P4 inside GCF-16) give FMV-ORACLE-001.
    - A duplicate in the successor map (P5) gives FMV-GCF-MAP-003.
    - A duplicate in a matrix block (P6) gives FMV-ORACLE-011.
    - A duplicate in the contract, which is outside S3's scope (P7), is still caught (PROFILE_BUNDLED_CONTRACT_HASH, and validate_gcfpe_20260914/current rc 1).
  - **The contract value check:** mutating every value-table leaf, and re-adding each deleted key, changes the output of `validate_contract` together with `validate_graph_contract` in every case (see A5).
  - **The relay literals:** P15 (qualifier deleted) fails with FMV-SKILL-STRUCTURE-001.
  - Re-stamped or text-only changes that still pass are F1, V1, V2, L-a and L-b.
- **A2 (did a2 weaken anything?).** No.
  - **The PR-skill literal** is now `"No agent merges, and no session is created by an agent. " + ONCE`. That string contains the old one, so it is strictly stronger on SKILL.md. The copy in behavior-cases.md is guarded by FMV-GCF-DISPATCH-001.
  - **`oracle.get(key)`** is safe:
    - With a readable oracle, it equals the old `oracle[key]`.
    - With an unreadable oracle, it turns a traceback into FMV-ORACLE-001 plus MAP-005/ROW-001 findings (P3, P4).
    - With a key missing from both the oracle and the map (P10), FMV-ORACLE-004 and -020 still fire.
  - **The changed expectations in derive_regressions_a2.py** only add rule ids (G2, G3 and T5 gain -021; T1 gains -022), raise a test count (34 to 35), or raise a literal count (R-DISP 1 to 2). Each follows from S1, S2 or S4(a). Every original expected id stays. The T1 row-mapping change (None to "") keeps the comparison exact.
- **A3 (provenance).**
  - The oracle has 46 rows, with ids in historical order. Only GCF-14 (`consumes`), GCF-17 (`name`, `actor`, `session`, `failure_stop_condition`) and GCF-17.LINEAGE (`next`, `failure_stop_condition`) differ, each with its `source_row_sha256`. Key order equals history.
  - I recomputed the three digests with the formula: 42db7a9e…, 67745290… and 73a133c1…. They equal the oracle, the matrix digest lines and `SUCCESSOR_ROW_SHA256`.
  - Each new value appears verbatim in the approved plan (Amendment 1) and in spec v2.
  - Non-row keys differ only in `profile_id`, `required_global_tokens` (the profile id replaced in place) and `authority` (three successor keys appended). This is exactly `SUCCESSOR_CHANGED_TOP_LEVEL`, which FMV-ORACLE-020 enforces. C6's phrase "the non-row keys equal the historical oracle" should be read with that exception.
  - The matrix bytes match the §12 addendum: exact header, one blank line between blocks, one final LF, no CR.
  - A third row cannot change unnoticed. Content changes give -015 (G1), key-order changes give -022 (P8), and position changes give -019.
- **A4 (once per merge and the fallback predicate).**
  - I found no double-dispatch or no-dispatch path in the skill text. With no MERGE_OBSERVED, the fallback applies. If MERGE_OBSERVED arrives after the fallback was pasted, it is void. Both fixture texts carry the sentence, and amthor's fixture adds "Reject a second PR-40 entry for the same merge."
  - Observation, not a finding: the graph and contract (the MERGE_OBSERVED edges, and W-4 `pr40_entry`) encode the forward predicate but not the reverse void. D23-E's successor note places the sentence in C-DISPATCH only, and the routing surface Nathan read is fecc319b/284. So this is within the recorded scope.
- **A5 (value table).** The table is correct and live.
  - `generate` reproduces the shipped 4.1.0 contract byte for byte (613162 B, 7a7fd028…, with both copies equal).
  - Every set leaf, when mutated, and every deleted key, when re-added, changes the output of validate_contract together with validate_graph_contract. None is unread, which closes R2-4 and V-a.
  - `primary_skill_revision` 1.3.0 equals the PR skill's revision. The overlay contract's 1.2.0 predates this change.
- **A6 (reversed literals).** Every validator literal present at baseline and absent now is one of these:
  - a revision bump;
  - a re-pin (graph, contract, oracle, map, fixtures, routing surface);
  - a spec-directed replacement: `PROMPT_VERSION_HEADER_RE` became the key tuple (spec v2 :6060); the four transition_contract keys follow V-6; the GCF-17 ten-field sentence became `EXPECTED_PHASE_CONTINUITY`, which rejects "dedicated PR-development session"; EXPECTED_EVENT_2's fact became `product_owner_manual_merge_observed_or_asserted` with the predicate;
  - the selected-alias rewording (§12 S-5 / a1 V3), with FMV-GCF-CURRENT-001 still running against the 091426.1 contract.
  - Each kept rule stays guarded.
- **A7 (GCFPE override).** The override sentence is verbatim in change-flow :265, relay :257 and tw :302, and is in `CONTRACT_REQUIRED` for all three.
  - The core's "fresh spawned session" option stays byte-identical in the core block, as core sync requires. The override outside the block limits it for GCFPE stages.
  - The relay provisioning lines :255 and :717 are scoped "Outside a GCFPE main-ecosystem stage" and guarded (P15).
  - C5 holds on my grep: no main-ecosystem skill text instructs creating, launching or scheduling a session, or running a main-ecosystem prompt as a subagent.
- **A8 (author's choices).**
  - The §12 addendum items I checked hold: the matrix bytes, FMV code placement, the -017 tie check and G25B.
  - G11 reproduces its four findings: CANDIDATE-CONTRACT-001, CANDIDATE-FIXTURE-PROFILE-001 and CURRENT-001, all `PROFILE_PROTECTED_IDENTITIES`, plus CURRENT-FIXTURE-001. Each follows from the one unmoved profile pin, so the set is correct and not padded.
- **A9 (contradictions with kept rules).** None found. No agent merge stays at every site. "stay subscribed and do not poll" keeps no-polling. The MERGE_PENDING and MERGE_OBSERVED turns each end in one handoff block. PR-40 still verifies independently. A re-plan takes a new Proceed (GCF-17.LINEAGE, GCF-14).
- **Out of scope?** No. `diff -rq` against the installed tree lists 26 changed files and 3 new files, and each is named by spec v2 §5/§6/§8 or by the a1/a2 repair scripts. The bundled graph is spec §2's "bundled graph (both skills)". The a2-to-a3 delta is 7 files, exactly S1–S4. The change-flow, relay and tw packages are byte-identical to round a2.

## Round-a2 findings on these bytes

| finding | closed? | basis |
|---|---|---|
| SFR-A2-1 R2-1 / SFR-A2-2 F1 (predicate and D23-E guarded only in the PR skill) | **Yes** | FMV-GCF-DISPATCH-001 over the nine files, with counts equal to my recount. P16 and P17 fail. The amthor test exists (35 tests). V1 is an absent-skill edge only. |
| SFR-A2-1 R2-2 (allowed field takes an unapproved value) | **Yes**, subject to L-a | FMV-ORACLE-021 fires on P1 and P2b. |
| SFR-A2-2 F2 (duplicate keys) | **Yes** | P3–P6 fail, and so does P7, which is outside scope. |
| SFR-A2-1 R2-3 (layout) | **Yes, with minor residual F1** | Block order, block key order and row key order are enforced (T1, P8). The fence count misses block-quoted fences. |
| SFR-A2-1 R2-4 / SFR-A2-2 V-a (historical_non_executable_references) | **Yes** | Exact set in validate_contract. My leaf mutation shows nothing unread. |
| SFR-A2-1 R2-5 (relay qualifier) | **Yes** | P15 fails. |
| SFR-A2-2 V-b (fixture texts without void clause) | **Yes** | The sentence is in both fixtures and guarded. |

## Gates I actually ran

All runs used a scratch copy under `/tmp/claude-0/review-SFR-A3-1/`, with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside the scratch.

- **Brief identity.** I verified the brief's hash first: 16580 B, c29a5a8b…, equal to `git show c22bc64:`.
- **Baseline.** I reproduced it from a copy of the synced tree: fv 29 b9ca212a…, cf 21 80e877c2…, PR 4 e109d47a…, relay 5 4ef8daa3…, amthor 15 6cd088a0…, tw 2 fa3fac85….
  - I re-copied the tree at the end: identical, so the tree did not move.
  - The package hashes were unchanged at the end.
- **§8a.** All six package hashes, sizes and file counts match §1.
  - Every entry sits under its skill root, with no `..`, absolute path, backslash, symlink or duplicate.
  - `name:` is unchanged in every SKILL.md.
  - The extracted trees give freeze digests cb7e1693…, 1186283d…, 68077fa6…, 15aef989…, 819915e4… and fd6c344b…, matching §3.
- **§8b, the twelve live commands.** All exit 0:
  - FLOWMASTER_SUITE_PASS twice (`suite_ok` true, 0 findings, 0 warnings);
  - validate_gcfpe_20260914 `"ok": true` with errors [];
  - both 20260914 and current fixture runners: 228 cases, `fixture_suite_ok` true, 228 passed;
  - validate_gcfpe_current `"ok": true`;
  - change-flow fixtures 32/32;
  - the cf validator PASS;
  - the PR validator PASS;
  - relay self-test PASS, 230 cases, 0 failed;
  - amthor `Ran 35 tests … OK`;
  - the registry validator `{"valid": true}`.
  - `<root>` held only the graph JSON from a `graph_parts.py` build of the branch's `docs/graph/parts`: 575074 B, ae2bd159…, equal to both bundled graphs.
- **§8b, the historical layer.** 12 of 12 exit 0, and the outputs are byte-equal to the baseline tree's after normalizing the scratch root path. The four `validate_*` commands produce empty output.
- **§8c.** I derived the differing files with `diff -rq` and traced each to the spec or a repair script.
- **§8d.** 46 rows, with only the three rows differing from history. `validate_graph_contract` returns []. The routing surface is fecc319bdd4ce7ee6201cb77d7231861 / 284 from both the contract and the graph.
  - `regenerate_contract.py acceptance`, on baseline parts exported from merge-base a63bf80, reproduced 2b78f877…/606657 from a stripped template (61859 B, not a no-op). The negative control passes, and no mirrored path is non-load-bearing.
- **§8e.** Every 64-hex value in the six trees that names a file in them recomputes, with every consumer agreeing. No digest of a baseline or round-a2 version of a changed file remains cited anywhere. `SKILL_TREE_SHA256` 82505ca8… recomputes.
- **§8f.** Recounted by grep, as in A1.
- **§8g.** My probes P1–P20 and P2b, with results as reported above. Script: `probes.py` in my scratch.
- **Author regressions.** I re-ran them from `derive_regressions_a2.py` copies re-pathed into my scratch, against a separate tree copy that I confirmed unchanged afterwards. All are exact: oracle 15/15, skills 70/70, contract 53/53 + 35/35 + 3/3, fixtures 2/2, a1 17/17, a2 34/34.

## Not run
- `run_e4.py` / E3–E4 over the Notion bodies. It is optional (L1) and I did not fetch any body.
- `run_e2.sh` and `run_repair_a2.sh` as written. They write to `/tmp/claude-0/e2` and `/tmp/claude-0/repair2`, outside my permitted scratch. I ran their regression harnesses re-pathed instead, as above.
- `closure.py`.
- No install and no post-install check (L2).

## DECISION NEEDED

Nathan decides whether to install the six packages under this confirmation, which is bound to the digests above. The alternative is to fold F1, V1 and V2 into a further revision first. That revision would need a new review round, because this verdict does not carry to other bytes.
