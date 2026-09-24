---
artifact_type: SKILL_REVIEW_RECORD
round: cr1 (MODIFICATION-20260923-closeout-residuals)
reviewer: SFR-CR1-1
brief: docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-PROMPT-cr1.md (committed at 6a643d6; 18944 bytes; sha256 e48d773782fa062f9adf02b4ec2263cd1897bac4dcb03e2d1b0585e15cbb29a9, the same for the working file and the 6a643d6 blob)
branch_head_read: 6a643d6ec4a379c8c8d6585c6c87ae9c98ac8059 (docs/20260924-closeout-residuals-execute, not merged; see B1)
date: 2026-09-24
successor_of: none. This is the first review of these bytes, and no earlier record is edited (AUTH-001)
---

# Section 10 review, round cr1: SFR-CR1-1

## Verdict

**SKILL_FIT_CONFIRMED**

This verdict covers only the seven archives below. I measured each one from the bytes in
`/tmp/claude-0/-home-user-glow-hdengine-v2/219095eb-5889-516e-828c-322c5d5d5b5c/scratchpad/skills-out/`:

| archive | entries | bytes | sha256 | extracted freeze |
|---|---|---|---|---|
| flowmaster-validate.skill | 31 | 322703 | `ecdb49ff38c937d12332dd4ab99978fa6c0f6d33c77db06bfd758af17eb5bed0` | `31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626` |
| change-flow.skill | 22 | 258193 | `aa11c933a99b0ca590ed54a8fae4f7a1c5a1946a0754374f2183ce84800ca13b` | `22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47` |
| glow-graph-contract.skill | 9 | 55695 | `a908cde3adc4f15a3454589b42141734a9119ac4fe917d2159e86e4218bd3b49` | `9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c` |
| session-relay-flowmaster.skill | 5 | 56250 | `54d272867892e596cda9d54b2bd2c8e005f34f3ea799692c30672191526746a8` | `5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4` |
| glow-hde-pr-development.skill | 4 | 22605 | `59b42809024807f81eac7ba766617ba9cec0cf96ee85b07da68b7ec8dfcdacf2` | `4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a` |
| amthor-workspace-governance-audit.skill | 15 | 56629 | `87c59a6cef700ee7dd2c32f0a378225319b5837d49af52a239cd1a4c007615e7` | `15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab` |
| glow-po-reporting.skill | 1 | 3776 | `bb7d7967f05443fda739918e1ce6e636658501443f03e39caafafa149015906c` | `1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1` |

**It is void for any other bytes.** No earlier confirmation carries to these bytes: this is the first review (§2).
The seven packages install together. I confirmed it both ways: the new flowmaster-validate against the six
installed skills, and the installed flowmaster-validate against the six new ones, each give `FLOWMASTER_SUITE_FAIL`.

**Why it passes:**
- The baseline reproduces exactly, before the review and after it.
- Every package is its installed skill with exactly `EV/skills/diffs/<skill>.diff` applied. `patch -p1 -F0`
  reproduces all seven trees byte for byte: 27 files changed and 3 added.
- `run_gate.py --set pkg` exits 0 from the extracted archives with 34 of 34 rows `ok`. Every row's observed values
  equal `EX/gate_pkg.json`.
- The contract regenerates byte for byte: `6902924a…` at 4.1.0/1.3.0 and `dbae180b…` at 4.1.1/1.3.1. The two
  contracts differ in exactly the two revision lines.
- The protected core is byte-identical, `4d8bb9bf…`, in all five carriers. ITEM-08's sentence stands once outside the
  core in each of its two sites.
- Every hash pin agrees with its recomputed artifact.
- Every exact-phrase guard, revision pin and ITEM-11/12/14/36 regression I injected fires.

**What my own probes found:** four non-blocking findings (F1 to F4), one pre-existing residue outside this
change (F5), six observations, and one defect in the brief itself (B1). No finding shows a regression against the
installed baseline, and none needs a correction before install. **F2 is the one to read.** It is the D22 answer to
A1: two script paths in the governance audit still carry a prompt-body digest, and they pass every suite.

## Stability

- **The installed tree did not move.** I measured the seven baseline freeze lines before the review and again at
  the end, and each time they equalled brief §3 exactly. The whole synced root measured `320 420705ec…` at the end,
  the value in `EX/run.json` `root_x0.3`.
- **The archives did not change.** Their sha256s at the end equal the table above.
- **One commit was added to the branch during the review.** It is `69932d0` ("verdict SFR-CR1-2") and adds only the
  other reviewer's record. I did not read that record, and this review does not rely on it. Everything else I read
  is at `6a643d6`.

## §8a Archives

- All seven archives match brief §1 on entry count, bytes and sha256.
- `testzip` is clean for each one.
- No archive has a directory entry, an absolute path, a `..` component, a backslash, a symlink, a duplicate
  entry, `__pycache__` or `manifest.json`.
- Every entry sits under its own `<skill>/` root.
- `name:` is unchanged in all seven SKILL.md frontmatters. The `description:` changes in glow-graph-contract
  (ITEM-09 and ITEM-13) and in the governance audit (ITEM-05).
- File modes are 644, the same as the installed tree.
- skill-creator's `quick_validate`, run from my scratch copy of the root, reports "Skill is valid!" for all seven.

## §8b Gates I ran

- I ran the extraction and root build exactly as in the brief, with `R=…/scratchpad/sfr1`, the scratch
  directory my caller assigned. I used `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR=$R/tmp` throughout.
- **freeze.py on the extracted trees:** the seven lines equal `EV/skills/expected_after_patch.txt`, and `diff`
  exits 0.
- **`run_gate.py --set pkg --pkg-root $R/root --out $R/gate`:** exit 0; `rows_total` 34, `rows_ok` 34,
  `rows_not_ok` [], `not_run` [], `ok` true. I read `ok` row by row:
  - `validate_flowmaster.default` and `validate_flowmaster.candidate` both give `FLOWMASTER_SUITE_PASS` and
    `suite_ok` true; the candidate run gives 236/236 fixtures.
  - `run_change_flow_fixtures`: 32/32. `run_gcfpe_current_fixtures`: 236/236.
  - The historical alias gives 84/84, and both ITEM-11 cases are true.
  - `run_gcfpe_20260914_fixtures`: 236/236.
  - Relay self-test: 232 cases, `PASS`.
  - The PR validator, change-flow's own validator and the audit fixture suite all pass.
  - The pre-reindex build exits 1 with exactly the nine expected stderr lines.
  - The deriver finds 0 drift with the 1.13.0 audit and with the installed 1.12.0 audit.
  - `freeze.skills_root` is `323 047ca742…` at the start and at the end, the PLAN-time value.
- **`core_sync` is true** for change-flow, flowmaster-primary, session-branch-flowmaster, session-relay-flowmaster
  and tw-flowmaster.
- **My own suite harness** (`$R/suites.py`) runs 11 suites on a skills root, adding the historical-alias,
  current-overlay and Change Flow fixture runs. All 11 pass on the clean root, and it is the harness for §8g.

**Not run, and why:**
- `--set pre` is X1.3-only and needs the pre-reindex working tree.
- `--set post` comes after the install.
- The registry corpus gate over live bodies is excluded: bodies are out of scope (L1, D22).
- The author's PLAN-scratchpad regressions are not in the repository (L4). I wrote my own probes instead.

I read no Notion page and no prompt body. Every body in my probes is synthetic text I wrote, such as
`IA-10 synthetic body — not a real prompt` and `Step n: act.`

## §8c Diff against the installed tree

`diff -rq -x __pycache__ <installed>/<skill> $R/ext/<skill>/<skill>` lists exactly the files in brief §8c, and
nothing else, for all seven skills: 27 files differ, and 3 files are only in the new glow-graph-contract
(`scripts/contract_recipe.py`, `scripts/regenerate_contract.py` and `scripts/registry_deriver.py`).

I also applied each committed diff to a copy of the installed skill with `patch -p1 --no-backup-if-mismatch -F0`.
Every patch exits 0, and `diff -r` against the extracted tree is empty for all seven. Each diff's sha256 and byte
count equal `EV/skills/manifest.json`.

## §8d The contract and the graph

- **Both bundled copies are byte-identical:** 613326 B, sha256 `dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c`.
- **The graph builds from the branch's parts.** `graph_parts.py build docs/graph/parts` (new builder) gives:
  - 55 nodes, 229 edges, 55 `state_routes` keys and 282 `state_route` rows;
  - embedded JSON of 575074 B, sha256 `ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d`;
  - graph.md of 575672 B, sha256 `a70a93263f2943be45450a210f62a82a2a27abfd49a259d04f838e469ba0cc24`.

  The header's `complete_source_*` values equal the block, and the block equals the bundled
  `…-candidate-graph-contract.json` byte for byte.
- **The contract regenerates.** I ran `contract_recipe.py` with spec §5.4 execute.4's arguments, the kept template
  (606657 B, `2b78f877…`) and the bundled successor oracle:
  - At 4.1.0/1.3.0, E2 is `7a7fd028…` and the recipe gives `6902924a…`, 613326 B, EQUAL to both installed copies,
    exit 0.
  - At 4.1.1/1.3.1, E2 is `5ad52062…` and the recipe gives `dbae180b…`, EQUAL to both packaged copies, exit 0.
- **The 4.1.0 and 4.1.1 outputs differ in exactly two lines:** `contract_revision` 4.1.0 → 4.1.1 and
  `.pr_development_contract.primary_skill_revision` 1.3.0 → 1.3.1. A structural JSON diff between the installed and
  packaged contracts finds only those two paths.

## §8e Hash pins, recomputed

| pin | recomputed from | consumers that agree |
|---|---|---|
| `SKILL_TREE_SHA256 ed52208f…` | my own implementation (sorted paths, per-file sha256, the declaration line removed from SKILL.md) and the validator's `skill_tree_digest` both measure `ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af` | `flowmaster-validate/SKILL.md:9` (exactly one declaration); `validate_self_identity` passes |
| contract `dbae180b…` / 613326 | both bundled copies | `validate_gcfpe_20260914.py:1012–1013`; profile `candidate_contract.sha256` and `byte_count` |
| graph `ae2bd159…` / 575074 | built graph block; both bundled graph files; `$R/gate/cand/graph/…` | FV `:1010–1011`, change-flow `:21`, profile `frozen_graph`, both contracts' `source_snapshot.frozen_candidate_graph.sha256`, glow-graph-contract `SKILL.md:203` and `contract_recipe.py:17` |
| fixtures `c433aa09…` | `fixtures/gcfpe-20260914.1-091426.1/scenarios.json` (37 scenarios) | FV `:1014`, profile |
| core `4d8bb9bf…` | the marked core in all five carriers | change-flow `:26`, FV `validate_gcfpe_current.py:79`, profile, contracts |
| Primary file `06655077…`, R1 oracle `ede635b1…`, R1 runtime map `aa6ed8e3…`, historical map `5574666e…`, historical R1 `52807e58…`, URL map `af03c353…`, topology `705f5acf…` | the files themselves | every pin site I grepped |
| template `2b78f877…` / 606657 | `docs/graph/contract-template/…-4.0.6.json` | glow-graph-contract `SKILL.md:112`, `regenerate_contract.py:289` (acceptance only) |

## §8f Revision sites, recounted by grep

- **3.3.1 (flowmaster-validate):** `FLOWMASTER_VALIDATE_REVISION` at `SKILL.md:8`.
- **3.3.1 (change-flow):** `SKILL.md:8`; change-flow `validate_gcfpe_20260914.py:746`; FV `validate_flowmaster.py:149`
  and `:1329`; `validate_gcfpe_current.py:640–641`; profile `installed_skill_revisions`.
- **`validator_revision` 3.3.1, at exactly four sites:** profile `:45`, `run_gcfpe_20260914_fixtures.py:828`,
  `validate_gcfpe_20260914.py:1166` and `validate_flowmaster.py:1903`. No other emitter exists.
- **3.2.0 (relay):** `SKILL.md:8` and `validate_flowmaster.py:186`.
- **1.3.1 (PR skill):** `SKILL.md:8`; its validator `:26`; both contracts `:3026`; FV `:1821`, `:2710` and
  `validate_gcfpe_current.py:657`; the profile.
- **1.13.0 (audit):** `SKILL.md:10` and `run_fixture_suite.py:344`.
- **4.1.1 (contract):** both contracts `:356`, change-flow `:751`, FV `:1482` and FV `SKILL.md:155`.
- **Leftovers:** no 3.3.0, 1.12.0 or relay-3.1.0 revision string is left. The remaining 3.1.0, 4.1.0 and 1.3.0 hits
  are the historical 091326.2 contracts and the regenerator's documented 4.1.0/1.3.0 reproduction.

## §8g My own must-fail probes

Each probe mutates a scratch copy of `$R/root`. Where a probe touches flowmaster-validate, I re-declare
`SKILL_TREE_SHA256` so that only the guard under test can fail. Each probe then runs all 11 suites.

| # | probe | expected | result |
|---|---|---|---|
| A1-01/02 | ITEM-08 sentence removed from change-flow / relay | fail | fail (`missing specialization contract`) |
| A1-03 | `source revision/content identity` restored in change-flow's active text | fail | fail (FV and change-flow's own validator) |
| A1-04 | same phrase inside change-flow's prohibition block | FV passes by design | FV passes; change-flow's own validator fails (stricter, as `regress_final_p25` records) |
| A1-05 | relay `optional digest` restored | fail | fail |
| A1-09/10 | FV `its recursively loaded corpus` in SKILL.md; `complete 55-member prompt corpus` in the profile | fail | fail (`retired D22 phrase present`) |
| A1-11 | audit `Place retrieved representations in a local run snapshot` | fail | fail (`test_retired_d22_phrases_absent`) |
| A1-12 | audit `build_snapshot_manifest` hashes prompt kinds again | fail | fail (3 subtests) |
| A1-06/07/13/14/15/18 | paraphrases: a "checksum of the prompt text" kept in provenance (relay); "save the prompt's Notion text to a local file and record its SHA-256" (change-flow); "record a SHA-256 of every prompt page's text" (audit); "keep a reference copy under docs/ephemeral/prompts/" (PR skill); "keep a mirror of every prompt body under docs/graph/prompts/" (glow-graph-contract); "attach a copy of its Notion body and its hash" (po-reporting) | pass (the volunteered limit) | all pass every suite |
| A1-08/16/17 | an **exact** retired phrase with a line break inside it (FV, relay) or a doubled space (change-flow) | should fail | all pass every suite (F3) |
| P1 | `build_snapshot_manifest.py` without `--source-index` on a dir holding a synthetic prompt body | no body digest | the body is `local_text` with a sha256 (F2) |
| P2 | snapshot whose `notion_prompt` source carries a body sha256, fed to `audit_governance` | refused or stripped | no finding, verdict `PASS`, and the digest is written to `WGA-fixture-Evidence.json` (F2) |
| A2-01 | ITEM-08 sentence moved inside change-flow's core markers | fail | fail (`embedded Primary core is not byte-identical`; `protected Primary core SHA`) |
| A2-02 | one byte of the relay's core changed | fail | fail |
| M1–M16 | builder with bookkeeping errors on a copy of the branch parts | reject | see A3 below: 14 rejected by name, a string index rejected by traceback, a float index accepted |
| M1–M16 + `reindex` | repair | build passes | passes, except M3 (global list short): `KeyError` (F1) |
| R0–R9 | `contract_recipe.py` with bad inputs | fail when it should | see A3 below: all as expected |
| D0–D6 | `registry_deriver.py` with drift or bad inputs | exit 1 or 2 as documented | drift exits 1; a missing part exits 2; an unusable registry or audit dir exits 1, not 2 (F4) |
| A4-01 | `PROMPT_BODY_RELEASE_HEADER` window restored to `nonblank[:8]` | fail | fail (current and 20260914 fixture suites) |
| A5-01/02/04 | relay validator without `REPOSITORY`; enum line reverted; "preferred artifact plane" restored | fail | fail |
| A5-03/05 | examples back to `GOOGLE_DRIVE`; paraphrase "keep exchange artifacts in a shared Drive folder" | (unguarded) | pass (O4) |
| A6-01 | `paths[prompt_id]` restored in `validate_gcfpe_current.py` | fail | fail (both ITEM-11 alias cases) |
| A7-01..04 | change-flow 3.3.0, PR skill 1.3.0, audit 1.12.0, relay 3.1.0 | fail | all fail |

## Findings

### F1 (non-blocking): `reindex` cannot repair a short `_other_edge_indices`, and it can move an edge

- **Artifact:** `glow-graph-contract/scripts/graph_parts.py`, `ordered_edges` and `reindex` (ITEM-12), and
  `glow-graph-contract/SKILL.md` ("`reindex` … The order is the builder's own, so the built graph does not change").
- **Defect:**
  1. When `global.json` carries fewer `_other_edge_indices` than `_other_edges`, `build` rejects it by name and says
     "run `graph_parts.py reindex <parts-dir>`". `reindex` then exits 1 with an unhandled
     `KeyError: ('global.json', 2)`: `ordered_edges` zips the short list with the edges and drops the unindexed
     global edge. Nothing is written, and `build` stays fail-closed.
  2. When an existing edge's index is lost, out of range or negative, `reindex` moves that edge to the end, so the
     rebuilt proof token changes. My probes gave `18c0bbf3`, `ab287748`, `8e4d25d1`, `4cae5afa` and `b9e0429e`, none
     of them `ae2bd159`. "the built graph does not change" is true only against the lenient builder's order.
- **Evidence:** probes M3, M1, M5, M6, M7, M13, M15 and M16 on a copy of the branch parts. On the real parts, reindex
  rewrites 27 files and then 0, and the reindexed pre-parts equal the branch parts, with the graph unchanged
  (`a70a9326…`).
- **Smallest correction:** in `ordered_edges`, give global edges beyond the index list the part rule
  (`other_eidx[j] if j < len(other_eidx) else nxt`). In SKILL.md, say that `reindex` can reorder an edge whose
  index was lost, and that the tokens must be compared before committing.

### F2 (non-blocking, claim-level; D22): two audit script paths still carry a prompt-body digest

- **Artifact:** `amthor-workspace-governance-audit/scripts/audit_workspace_governance.py` (`build_snapshot_manifest`,
  `audit_governance`, `write_audit_artifacts`) and `SKILL.md` step 6 (ITEM-05, ITEM-16).
- **Defect:**
  1. Without `--source-index`, `build_snapshot_manifest` records every file under the source dir as `local_text`,
     with `sha256`, `structural_sha256` and `size_bytes`. The audit reads prompt text only from under
     `snapshot_root`, so step 5's transient prompt file has to sit in that directory. Step 6 tells the agent to run
     `build_snapshot_manifest.py`, but it never mentions `--source-index` or how a source's `kind` is declared. Run as
     documented, it therefore hashes the prompt body into the Snapshot-Manifest.
  2. `audit_governance` accepts a prompt-kind source that already carries `sha256` and `size_bytes`, as every prompt
     source in a 1.12.0-built manifest does. It raises nothing, returns `PASS`, and `write_audit_artifacts` writes the
     digest into the Evidence artifact.

  The ITEM-16 fixture tests only the builder with an index that declares the kind. Both paths pass every suite. So
  ITEM-05's claim, and the new description's "prompt bodies are … never snapshotted or hashed", hold only when an
  undocumented index is used and the manifest is fresh.
- **Evidence:** probes P1 and P2 in §8g.
- **Smallest correction:** in `audit_governance`, raise `SRC-003` (or strip with a warning) for a prompt-kind source
  that carries `sha256`, `structural_sha256` or `size_bytes`. In step 6, name `--source-index` and the three `kind`
  values. Add one must-fail fixture for each.
- **Why non-blocking:** the installed 1.12.0 hashes every prompt source by design, so installing 1.13.0 improves on
  it. Holding it back would keep the worse state. D22's directive allows the limitation to be reported instead.

### F3 (non-blocking): the exact-phrase D22 guards miss a phrase broken by whitespace

- **Artifact:** `validate_flowmaster.py` `CONTRACT_FORBIDDEN` and `SELF_FORBIDDEN`, change-flow's retired-clause list,
  and the audit's `RETIRED_D22_PHRASES` test (ITEM-16).
- **Defect:** all four checks match lower-cased raw substrings. A retired phrase re-inserted with a line break inside
  it, or with a doubled space, renders identically and passes every suite. flowmaster-validate's SKILL.md is
  hard-wrapped, so a phrase restored there would naturally be split. The `D14` note records only "prose paraphrase"
  as the residual limit, and this is not a paraphrase.
- **Evidence:** probes A1-08, A1-16 and A1-17.
- **Smallest correction:** compare `" ".join(text.split()).lower()` against each phrase in the four checks, with one
  line-wrapped must-fail regression. Or add the whitespace variant to the recorded limit.

### F4 (non-blocking): `registry_deriver.py`'s exit codes differ from its docstring

- **Artifact:** `glow-graph-contract/scripts/registry_deriver.py` (ITEM-13).
- **Defect:** the docstring says "1 when any [row drifts], 2 on unusable input". A missing registry file exits 1 with a
  `FileNotFoundError` traceback, and a wrong audit directory exits 1 through `sys.exit(message)`, the same code as
  drift. Only a missing part returns 2.
- **Evidence:** probes D4 and D5. The gate checks only exit 0, so it cannot see this.
- **Smallest correction:** catch the load failures and the missing-script case, and return 2.

### F5 (pre-existing; outside this change's items): D22-contrary code left in unchanged scripts

- **Artifacts:**
  - change-flow `scripts/validate_gcfpe_artifact_timing.py` keeps `run_artifact_timing_cases(prompt_dir, contract)`,
    which reads a directory of prompt `.md` files with `rglob`. Nothing in change-flow calls it; its validator imports
    only `validate_artifact_timing_contract`. flowmaster-validate's copy takes supplied bodies.
  - flowmaster-validate `scripts/validate_epic_alpha.py` and `validate_strength_middleware.py` keep two
    snapshot-directory functions, `validate_snapshot` and `validate_prompt_snapshot`, which are unreachable. They also
    keep a reachable `--publication` check. It requires and compares prompt-body SHA-256 fields
    (`source_body_sha256`, `candidate_content_sha256`, `readback_content_sha256` and `archived_body_sha256`) for the
    retired GCFPE-20260908.2 release. SKILL.md classes these as provenance that the active runner must not execute.
- **Smallest correction, in a later change:** delete change-flow's `run_artifact_timing_cases`, or give it supplied
  bodies as flowmaster-validate's copy has. Retire the `--publication` body-digest checks, as `--prompts` was retired.

### Observations (not findings)

- **O1 (ITEM-15, beyond a5 N1's list):** `DISPATCH_HIDING_RE` matches `[//]: #` only. Other link reference
  definitions also render as nothing and pass: `[//]: <> (text)`, `[comment]: <> (text)` and `[note]: /x "text"`.
  Either match `^[ \t]{0,3}\[[^\]\n]+\]:`, or name these beside `<div hidden>` and `<details>` as a limit.
- **O2 (ITEM-36):** the window is gone, and a label line is rejected at any depth. The normaliser, which predates this
  change, still passes these forms:
  - `Ecosystem Release:`, `PROMPT VERSION:` and `prompt version:`;
  - `Prompt version : x`;
  - `<b>Prompt version:</b>`;
  - `a. Prompt version:`.

  The registry's pattern rejects `Prompt version : x` but accepts `10) Set:`, and this check does the opposite, so
  the two checks disagree on those two forms. None of my ten legitimate-prose probes was wrongly rejected, among
  them `Settings:`, `Set up the run:` and `Prompt versions: …`.
- **O3 (ITEM-11):** with `--bodies-stdin` and empty input or `{}`, the historical alias now returns `ok: true` and
  `prompt_bodies_validated: []`, where the installed code raised `NameError`. The v4 path does the same, and
  `prompt-validation-procedure.md` step 4 calls it correct ("it found no fault in nothing"). A list or a non-string
  body still raises `AttributeError`, as it did before the change.
- **O4 (ITEM-14):** `manifest-v2-examples.md` agrees with the enum, and its manifest validates `PASS` with
  `REPOSITORY`. Nothing guards the examples, though: probe A5-03 reverted them and every suite passed.
- **O5 (ITEM-13):** `contract_recipe.py` does not check the template's `2b78f877…` digest; only `--check` against a
  shipped contract does. Its preconditions are `assert`s, which `python -O` strips.
- **O6 (a policy reading, not ruled here):** in every project-registry mode, each non-archived registry prompt must
  exist as a file under the snapshot root; otherwise the audit reports `INV-001` ERROR. A BASELINE audit therefore
  needs every body as a local file for the run. Step 5 calls those files D22 transient reads.
  `prompt-validation-procedure.md` step 3 gives the validator no path option because "a path option invites a
  standing directory". Whether the audit's path-keyed design meets D22 is Nathan's reading to make if he wants it
  settled.

### B1 (the brief, not the packages): §4 names a branch that is not the execution branch

- **Defect:** brief §4 says to read `claude/epic-tesla-17406z`, and that if it is missing, "it merged and was
  deleted; read the same paths on main". That branch does not exist, locally or at `origin`. `main` (`7028bea`) has
  none of this attempt's commits: `EX/gate_pkg.json` is not on `origin/main`.
- **Where the work is:** the approved §P successor's checkpoint 1 (`D26-C`) moved EXECUTE to
  `docs/<yyyymmdd>-closeout-residuals-execute`. That branch holds `2729f88` and `6a643d6`, and it is what I read.
- **Cause:** the stale name comes from `EV/skills/REVIEWER-PROMPT-cr.draft.md:86–91`, which `fill_brief.py` does not
  fill. A reviewer who followed the fallback literally would have read `main` and found none of §4's `execute/`
  files.
- **Smallest correction:** replace the draft's branch sentences with the checkpoint-1 branch, or with a token that
  `fill_brief.py` fills from `git branch --show-current`.

## Answers to §6

- **A1:** yes.
  - Exact re-injections of every retired phrase and of the override sentence fire.
  - Paraphrases pass every suite in six of the seven skills, as the volunteered limit says. glow-graph-contract and
    glow-po-reporting have no text guard at all.
  - Beyond paraphrase, exact phrases split by whitespace pass (F3).
  - Two audit script paths carry a prompt-body digest (F2).
  - Pre-existing, unchanged scripts keep a prompt-directory scan and a body-digest publication check (F5).
  - I found no live instruction in the seven packages' active text that tells an agent to copy, hash or snapshot a
    prompt body. My search terms were hash, sha, digest, snapshot, mirror, copy, export, cache, corpus and persist
    near "prompt". The hits are prohibitions or history.
- **A2:** yes on both counts.
  - The marked core hashes to `4d8bb9bf…` in change-flow, the relay, flowmaster-primary, session-branch-flowmaster and
    tw-flowmaster.
  - The sentence occurs exactly once in change-flow and once in the relay. Each time it sits inside the specialization
    block, after the core's end marker, and outside change-flow's prohibition block.
  - `CONTRACT_REQUIRED` names exactly those two sites. Removing the sentence, or moving it into the core, fails.
- **A3:** yes, with F1 and O5.
  - **The builder** rejects, each by name: a dropped index; a duplicate; an out-of-range or negative index; an extra
    or short global list; an absent or null list; an added edge; and a removed edge that leaves a gap.
  - It rejects a string index only with a `TypeError` traceback. That still fails closed, before any write.
  - It accepts a float index `1.0`, which leaves the output unchanged.
  - It accepts the reindexed parts, and the pre-reindex parts fail exactly as `gate_pre` expects.
  - **The recipe** reproduces `dbae180b…` and `6902924a…`. It fails on each of these: a wrong oracle; a doubled D23-E
    heading; a third quoted line; a changed quoted line; a wrong revision or a malformed one; a changed template
    under `--check`; and a missing argument.
  - A quoted line under the next heading does not change the output (P-21).
  - **The deriver** detects edge and state drift. Its exit codes are F4.
- **A4:** yes.
  - A label line is rejected at depth 40 and past the old window, plain or decorated. Restoring the window fails the
    fixture suites.
  - No legitimate line I tried was rejected. The variant forms in O2 pass, which is the limit of the existing matcher.
- **A5:** no.
  - Nothing in the seven packages expects a Drive artifact plane. The self-test base uses `NONE`. The new cases accept
    `REPOSITORY` and reject `DROPBOX`, and the example validates.
  - The remaining Drive items are the `DRIVE_LINK` reference method and its fixtures. They are still lawful outside
    GCFPE or where Nathan directs a file (D7).
  - The one contract with `DIRECT_GOOGLE_DRIVE_LINK` is the historical 091326.2 contract.
- **A6:** yes, on every path that raised `NameError`.
  - The installed code raised it for every dict input, `{}` included, because the loop always reached `paths`.
  - A non-empty dict now returns named results: `PROMPT_BODY_IDENTITY`, `PROMPT_ROUTE_SEMANTICS:*` and
    `PROMPT_BODY_UNEXPECTED_ID`.
  - An empty supply now returns `ok: true` with nothing validated (O3).
  - A static undefined-name scan over every script in the seven packages finds nothing. The same scan finds the
    installed `paths`.
- **A7:** every site agrees (§8e and §8f). `validator_revision` is 3.3.1 at exactly four sites, and every hash pin
  equals its recomputed artifact.
- **A8:** I reproduced the recorded counts: 36/36, 20/20, 33/33 and 11/11, with 32 base controls.
  - **Mostly the author's own construction.** They re-inject exactly the phrases the author removed and exactly the
    sentence the author wrote. The ITEM-12 cases are three chosen mutations and one reindex. D1–Q5, O1–O3 and K3
    reproduce the a5 reviewers' probes.
  - **What they do not reach:** paraphrase (volunteered), whitespace splits (F3), the audit consumer and the
    index-less build (F2), a short global index list (F1), the deriver's error exits (F4), other reference definitions
    (O1), label variants (O2), the empty supply (O3), the examples (O4), and any text in glow-graph-contract or
    glow-po-reporting. They also cannot be re-run from the repository (L4).
- **Question (outside the items?):** no. Each hunk maps to an ITEM, PART-01, RULING-5-Q3-A or a REVISION line, as
  spec §5.2 counts them. Three changes go wider than their item's one-line statement, and each is still within it:
  - validate_flowmaster now enforces change-flow's whole `CONTRACT_FORBIDDEN` list outside the prohibition block,
    where it used to skip change-flow (ITEM-16).
  - The relay's replacement paragraph also forbids requesting, creating or routing through an assessment, an Analyzer
    or a configuration gate (ITEM-02). That matches the 091426.1 contract's `transition_contract.prohibited_references`.
  - glow-graph-contract gains a run-hygiene sentence: `PYTHONDONTWRITEBYTECODE`, `TMPDIR` and scratch output
    (ITEM-12 and ITEM-13).

## Claims C1–C5

| claim | holds? |
|---|---|
| C1 | Holds exactly: the patch round trip gives 27 changed files and 3 added. |
| C2 | Holds for every item. Carry F2 (ITEM-05/16), F1 (ITEM-12), F3 (ITEM-16) and F4 (ITEM-13) as non-blocking. |
| C3 | Holds. |
| C4 | Holds on my own run: exit 0, 34/34 `ok`. |
| C5 | Holds on my sweep. The fresh-session option at change-flow `:158` and relay `:148` is in the protected core, and each skill's specialization overrides it. The audit's "fresh sessions" line (`SKILL.md:77`) is maintenance work, which D23 excepts. |

## Writes

- **Scratch only:** `/tmp/claude-0/-home-user-glow-hdengine-v2/219095eb-5889-516e-828c-322c5d5d5b5c/scratchpad/sfr1/`
  holds the extracted trees, `root/`, `baseline/`, `gate/` and the probe harnesses.
- **Repository:** this record only.
- **Nothing else was written.** I installed nothing and wrote nothing to the synced skills directory. I made no
  commit or push and no git operation that changes the branch. I did not touch `docs/pfcanon`, the registry, the
  graph parts, the Modification record, Notion, Drive or GitHub. I did not read the other reviewer's record.

**NOTHING NEEDED.** The verdict does not depend on any correction. F1 to F5 and B1 are for the author to carry into a
later change.
