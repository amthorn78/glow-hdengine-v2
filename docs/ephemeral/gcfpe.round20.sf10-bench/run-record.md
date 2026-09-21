---
artifact_type: GCFPE_RUN_RECORD
artifact_version: "1.0"
created_date: 2026-09-20
release: GCFPE-20260914.1 / 091426.1 / 55
author: PE34
records: 'The round-20 SF10-03/05/06/08 bench and regression runs, with input identities, commands and outputs'
status: RUN_RECORD_LANDED
generated_by: 'Emitted programmatically from the run artefacts; no value in this file was transcribed by hand.'
---

# Round 20 run record — inputs, commands, outputs

> **Regenerated at `210bb8f`+1 from the final artefacts.** The first version of this file was
> emitted before the last validator change and then not refreshed, so it named the previous
> validator digest, the previous package size and an 18-case bench run — sending a reviewer to
> verify bytes that were not the bytes under review. `make_run_record.py --check` now recomputes
> every identity below from the artefacts and fails if any record has drifted; re-reading the
> summaries by hand was tried and failed three times in one round.

Review asked for this, correctly, and cited the repository's own standard against the earlier
version of the report. The registry's `corroboration_not_reproducible_here` key says a review whose
report, inputs and command are not checked in "cannot be reproduced and it is recorded here as
corroboration, never as evidence," and that it "is promoted to evidence only by landing the run."
The bench and regression numbers in the repair report were in exactly that position: asserted counts
with no landed run.

This file lands the run. It is generated from the artefacts themselves, so every digest and count
below was read from a file rather than typed.

**What this file does and does not make reproducible**, in the registry's own vocabulary:

| claim | status |
|---|---|
| the commands that were run, verbatim | **evidence** — listed below |
| the identity of every input | **evidence** — digests below |
| the outputs those commands produced | **evidence** — reproduced below |
| that re-running them yields the same outputs **in a clean checkout** | **not reproducible here** — the inputs cannot be landed, see below |

**Why the inputs cannot be landed, and this is a constraint rather than a choice.** The 55 prompt
bodies are authored in Notion in place and are never mirrored into this repository. The two skill
trees live in a one-way synced directory that is not a git checkout and that only the Product Owner
installs into. Neither is mine to commit. So a clean checkout has the commands and the input
identities but not the inputs, and anyone holding the inputs can verify they are the same ones by
the digests below. That is the strongest form available here, and it is weaker than a self-contained
harness; the report should not be read as claiming otherwise.

## Input identities

### The frozen installed tree (the `--base` source)

- root: `synced/<bucket-id>/` (the freeze is rooted here, not at `~/.claude/skills`)
- files: **321**, of which **320** excluding `manifest.json`
- `.pyc` files: **0**
- recorded freeze digest: `c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb`

### The 55-body corpus (the `--prompt-dir` / `--bodies` source)

- bodies: **55**
- total bytes: **1,060,573**
- every body's SHA-256 is checked against its `evidence_contract` digest in
  `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` before any case runs;
  the bench exits 1 if the set is not exactly those 55 with exactly those digests.

| prompt | sha256 | bytes |
|---|---|---|
| `CF-C-10` | `41dce73a62735927d291bd8f7342654d314d38de47070fe37f8a6c9318fd1702` | 7203 |
| `CF-C-20` | `4570e718530316c018b18dcb15848f061e938e268ae4ec163630b310c14c67c7` | 5888 |
| `CF-C-30` | `b56d218a4f5d2a08f4f12af99fe097b001925dd1a1a445c2375edf4d3cd894e7` | 9420 |
| `CF-C-40` | `9b62004b93aa3a1e93fb5cf325bb6e78ea460ed78f49c523a654be6fd5a0c95f` | 7518 |
| `CF-E-10` | `5cdfce4d502c5b5b564b562b18e108cc38b1ffa85b3b655edd6706d0e76e80fe` | 7307 |
| `CF-E-20` | `5add38939d7e920b90c4031846e51f0fdb29b1bf50ec3574dcb72eaddc134108` | 5900 |
| `CF-E-30` | `6e92232ba58cc4e8c53004af7176ae2422863f2e1bcf1c6e209dc3a257066e76` | 9428 |
| `CF-E-40` | `e5e297ebcf0585c4114d30311535089ea16bad4ea679120a8e0e8d08050987ce` | 7533 |
| `CF-PO-10` | `ba98c011ec3607c25618d2dfe8409c4a1f6232dbf0323812b80f551a8a277b79` | 6091 |
| `CL-20` | `6c7860c0b23210e7a4f58938b134c0f80ba1f2ec69d4c4bfe567d2b83608660e` | 32573 |
| `CL-30` | `dc0a967032467707c738c465069b0cc3c042b1b1cbcdadb3389356e1d7b7d2c1` | 29622 |
| `CL-40` | `a3fd6cd79929c91829672faee9c5129e3f0ca80b9eef38360a6c1f80dc898e06` | 29401 |
| `CL-C-10` | `794b9bf3bed9278386379f898039bfde22e1831a92bdf40942fe74ca4d7b1b91` | 35878 |
| `CL-E-10` | `0c2b669d5833dcfb4c60d11fe5afe3851343c2f866251bffeb8f1af952b00753` | 36353 |
| `CL-E-20` | `10698a09852b296886f36d4df4ae0250285f8b13741c122ba9fcb90f54659689` | 14832 |
| `CL-E-30` | `7e1524159e9f6b00f5b4ffb8d33a90b3cd78e4115b526313322d7a0f5f8b99ae` | 13629 |
| `CL-E-40` | `582b6476d38e45bc9733c5d5d3e599281178a1a9f0cadb99aaf451dcbddd3b8c` | 15457 |
| `DOC-10` | `c858901a70cf0532395fda643841b9de2ea55b236b48f12bb24cac77661218ac` | 19787 |
| `DOC-20` | `e37624c24c349aff20324721fd2c9ae3d9b23e33b7261d6e49884805fafd4194` | 20217 |
| `ESC-10` | `93b05f42c6c18c4a1bc67bac767efc36c8d84f075a90292384a7be64e7e6e75c` | 16683 |
| `ESC-25` | `7766e52f3da17ee56e3ff4b60edb2a264215503e53fa7ed286a097769c6c09e2` | 17279 |
| `ESC-30` | `459ed2988a3fe000e70079a02967a1f47a8644498f54fc6199586c16a428ac6a` | 17751 |
| `ESC-40` | `9159ec0d9b52a52a58b1cf654547f31089381c331f5d10d133c1f619cea2bd08` | 17786 |
| `GCFPE-MGMT-10` | `e5b77f9c5c9939b2234146b106360b06fe73101b6ec50459ada16b18f6d25b12` | 8015 |
| `IA-10` | `5b7980fe30e9fced15b3c88133f834236d0309dc1f8966db9d0a9430b4fe8659` | 10301 |
| `IA-20` | `802ccd490feb83f6c4df3c73c325342e0202a02935579ffbf33c74feb35451be` | 6411 |
| `IA-30` | `a07e8933a00a4979298fabb703a0c2226aaf96eb870f1109a2c71b1252d14ebc` | 9729 |
| `IA-40` | `8c9bb2273f3e54ba8b1422a6f8d1c3bd1132497faa0ffd561038342a0c268326` | 5712 |
| `IA-50` | `42ce029be426cd3d745b3e9f7099439a091d3ee915c1f4c0dcd660cf5cf0afef` | 6668 |
| `IA-60` | `5addd33093e4c794e609829bba434275f06e798d313eda8ed29d63ffdba3e8c6` | 5633 |
| `MGR-10` | `5c8aebc68f7f7f6aa708851e0464e5793b27df158af1e37537ab450efbd86f6a` | 7276 |
| `OPS-10` | `4a30d7342f4a71e314b7962c2f7eb2ab6b313d9323044a1fcc8e6cbc6bc41563` | 42826 |
| `OPS-20` | `429c6ccca8c1602b3457433b85f3c91f96d7c21bb4891ee921dd56decd8b2c0c` | 36912 |
| `OPS-30` | `321e626fc72fb71dddf865860193b9d66fb36eae30b6a43c7d713e27443ff45f` | 57532 |
| `PR-10` | `d1e2458c39037c9aa1dfbc3f97641e2e6b2c1dd2143447f40c142dacb6a8b623` | 49351 |
| `PR-20` | `d64997b20867063089a23b42d44f6744a6537f158844e0a13f84670fd5f41110` | 51725 |
| `PR-30` | `482ca2a7657058154147acf3768334dfb956246c45a400a80e6c6f0138004a9d` | 39791 |
| `PR-35` | `51e8a5e85ca3b66ce755e979d0a1ac61540c7f06e58237f516f3a28148570e79` | 17908 |
| `PR-40` | `042255564c9916c4a933f0986ad8f98e36a495bdf1e35a956cdc0704a87991dc` | 54043 |
| `PR-50` | `ac910fe9e1374a4206179c58b8fba187b6c0e62e66e9c0cc1ffab85de93a91c8` | 6887 |
| `QA-10` | `9aeaeff42ad12f44f0e6036e922cb14c9da16457128a07159a8ee4331b152b99` | 82485 |
| `QA-100` | `373907a43557e87e46892fb35c683228a779765fb388cfff9dc98389d0c3fb7c` | 13317 |
| `QA-110` | `698c44f0c57d7294eed8a9a34049ee729b4a334eda81d6da0da8ad2dfb287718` | 14305 |
| `QA-120` | `94d6abb95dc8c637f91e2cb16d5a68323addc416bb961cef32c27477fb6a53d4` | 13731 |
| `QA-20` | `927b57745409bb99c4a83013a84f86ba7a375f2811b03d5a8beb46dcaba453a2` | 13217 |
| `QA-50` | `6fee14353c20e21d8ae1d38df31d3be2fc93a73161606fc17a7e45bd385881ff` | 16351 |
| `QA-60` | `f523e6354696e5ba637181f1ad7f1b60b54f11bb421ea39ac55cf7b9ede965a3` | 14012 |
| `QA-70` | `ed4ee3adca15bf2a3e91525eca413d6aba0d2ef1819ce81640f9b4cbd2505881` | 14014 |
| `QA-80` | `3c0080857a39aa14cf8e8e93f80674858e906a5e30e58d44dfdc944abfa8a02d` | 10163 |
| `QA-90` | `b77124fc789087f297fb668547617c3d6d82f3b0e4c8fcaff93686684c62d097` | 13892 |
| `RS-10` | `93905c67c008c31d829ad1cf3b3b621ff699a84228df61cb2268a6d0cbfc83c1` | 12732 |
| `RS-20` | `e6ccd013f8b390fc39069bbd3f87508cf630d3c1d267fda5feada00184ec5659` | 14818 |
| `RS-30` | `4c5f96f002762200a18fc8eff864d85157ef5d12487e6b044adc51e3fef5641a` | 12113 |
| `RS-40` | `ddef768be169c6eb41660433ff7557d72b3ebc5dd3ba8f617bdeb113b4732630` | 8233 |
| `UTIL-10` | `9234ff70454e2cd12f2d98e40a9ce103f9a27c87d51e7ded78aae5352cd96de4` | 6934 |

### The nine files that differ between `--base` and `--work`

| file | base sha256 | work sha256 |
|---|---|---|
| `change-flow/SKILL.md` | `e6bd29d59ca0152254c9f234e79b7fe146152bc20898e6e621c58904b6aa4f93` | `b26332af385b7c169739d7635c381a75dfa658c8d967fb9168634458f3592d2c` |
| `change-flow/scripts/validate_gcfpe_20260914.py` | `660d61fe619c9dd9aa2b5646a7344084af3c8c333fc044e2e91f51e941363c63` | `8e7cbe435a6e99385c98881ea95b1c9e7525506315172098b5e88672fbd288da` |
| `flowmaster-validate/SKILL.md` | `f2729ba39de4f46ba32a6d5d5a232b54038c685644835d700f308020f7dca4e3` | `3166ed867125758473aaf702ee85a1c594eccdd808c13bcd74368a01f9d5c667` |
| `flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json` | `fac89991c5c4e5a1064054f82e1e6d921fc5c5b3e079595fd8068b5e989015a7` | `39c44ad84ca05d5e2c02f9cd188506e472a34e7e97211981e2f0b7624e285479` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `433d2a1611e5671aca628ff2cd3d2ea312b9efab064e5a5c67c95c8417d96f4b` | `7523947d952b1372fd1786d5088ad7c92bee77fd5b5a250a58a93b2f98a36cf0` |
| `flowmaster-validate/scripts/validate_flowmaster.py` | `0e4c964c0dbf3701ade4e02551e0ef6ae9d923f756f28c84dc641f1ade6dcbe3` | `0460116f1a57e78db5183c74eb6624d56f9f5ba0a00551839fb0d50d2034cdd2` |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `535a3b161ef0996249540b46607b855c8d17d841fdd24ce3b615f97e6199bc2e` | `b0456a27816c47dea31382a55e3bc9070c329d140a8dcbec76c0e56ef0195094` |
| `flowmaster-validate/scripts/validate_gcfpe_artifact_timing.py` | `b5716af7882223d599812498e015fa7dfa88c095a899be80464a394d14d727e5` | `8cff6c7ef685c0a008dc5ea6290a379368723c46d14b184912a1971fd67dd43b` |
| `flowmaster-validate/scripts/validate_gcfpe_current.py` | `00c8b2035263ed0f172ef4107b084a1b6151bcb056944504572e3e3e245fb7fb` | `272d7b81fa091ce2f03dcf3fcc68c62134a5426bfa26214b0af50e03e5b17f91` |

### The packages built from `--work`

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 241886 | `07864f2b1315aca01c7c0d0fba9278a31afb64f3df5587c55303f5ffd7fddf7b` |
| `flowmaster-validate.skill` | 29 | 272724 | `43075084f00515f12a3a88bfd61e585054697106c416d8dfef89ab942207d7a0` |

Each archive was verified by extracting it and running a full recursive diff against the
working copy; both are identical. `zip -X` is used so a rebuild from unchanged content
reproduces the same digest, which was confirmed by building twice.

## Commands

**Corrected after review.** The first version of this section was headed "Commands, verbatim" and
then wrote the corpus as `<55-body corpus>` — a placeholder, not a path — and gave **no extraction
command at all**, while invoking the registry key that requires exactly that. Both are fixed below:
the extraction step is named and its script is committed, and the corpus argument is the real path.

`$B` below is the corpus directory, session-local at
`<scratchpad>/s10/bodies` — the path is not portable, but the **identity** of what it held is pinned
by the 55 digests above, which is the part a reader can check. All runs used a scratch copy of the
whole tree, never the installed tree, with `LC_ALL=C LANG=C TZ=UTC`. `$T` is `base` or `work`; `$C`
is `references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`.

### 0. Extraction — how the corpus was produced

```sh
# once per prompt, from a persisted Notion fetch result
python3 docs/ephemeral/gcfpe.round20.sf10-bench/extract_body.py <fetch-result.json> $B/<PROMPT>.md
```

`extract_body.py` **is committed with this record**. It implements the **strip-both** convention the
registry's recorded digests depend on: the body is the text between the first `<content>` and the
last `</content>`, with exactly one leading and one trailing newline removed if present. Any other
variant yields different bytes and a different SHA-256, which is why the registry names the
convention rather than assuming it.

**Round-trip verified, not asserted.** Of the persisted fetch results retained in this session, **26
have a counterpart in the corpus, and the committed extractor reproduces all 26 byte-identically.**
That checks the script against the corpus it is claimed to have produced. It does not cover the other
29, whose fetch results were not retained; those rest on the registry digest check the bench performs
before every run.

**Still not reproducible in a clean checkout**, and this is the honest limit: the persisted fetch
results are per-session artifacts of a Notion read, and prompt bodies are authored in Notion in place
and never mirrored here. The extractor plus the digests let a holder of the bodies confirm identical
bytes; they do not let a clean checkout obtain the bodies.

```sh
# 1. the bench, and the record.  The recorder RUNS the bench and observes its stdout and
#    its exit status, so neither can be asserted by the caller; --write regenerates the
#    generated sections of this file and --check recomputes every identity and fails on drift.
# regenerate this file's generated sections from the artefacts
python3 docs/ephemeral/gcfpe.round20.sf10-bench/make_run_record.py \
    --base prep/base --work prep/work --bodies $B --pkg prep/pkg --write

# verify every identity against the artefacts and fail on drift (this is the run recorded below)
python3 docs/ephemeral/gcfpe.round20.sf10-bench/make_run_record.py \
    --base prep/base --work prep/work --bodies $B --pkg prep/pkg --check

#    the bench can also be run directly; no env var is needed, since it sets
#    sys.dont_write_bytecode itself
python3 docs/ephemeral/gcfpe.round20.sf10-bench/bench.py \
    --base  prep/base  --work prep/work \
    --bodies $B \
    --registry docs/prompt_ecosystem_management/project-prompt-contract-registry.md

# 2. end-to-end, body-level, on the 55-body corpus
python3 prep/$T/flowmaster-validate/scripts/validate_gcfpe_20260914.py prep/$T/change-flow \
    --contract prep/$T/flowmaster-validate/$C --prompt-dir $B

# 3. the body-level fixture suite
python3 prep/$T/flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py prep/$T/change-flow \
    --contract prep/$T/flowmaster-validate/$C --prompt-dir $B

# 4. the contract-only fixture suite
python3 prep/$T/flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py prep/$T/change-flow \
    --contract prep/$T/flowmaster-validate/$C

# 5. the change-flow contract validator
python3 prep/$T/change-flow/scripts/validate_gcfpe_20260914.py prep/$T/change-flow \
    --contract prep/$T/change-flow/$C

# 6. the whole-ecosystem validator
python3 prep/$T/flowmaster-validate/scripts/validate_flowmaster.py
```

Exit codes below are each command's own, read directly rather than after a pipeline or a command
substitution -- both of which produced a false `exit=0` earlier in this session and are recorded as
void in the repair report.

## Outputs

### End-to-end on the 55-body corpus

**`--base`** (base) — `ok: False`, exit 1, **12 errors**, stdout 6179 bytes, stderr empty:

```
PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10
PROMPT_WRITER:CF-C-20:ACTIVE_ADDENDA
PROMPT_WRITER:CF-C-20:AUTHORING_CONTEXT
PROMPT_WRITER:CF-C-20:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-C-40:ACTIVE_ADDENDA
PROMPT_WRITER:CF-C-40:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-E-20:ACTIVE_ADDENDA
PROMPT_WRITER:CF-E-20:AUTHORING_CONTEXT
PROMPT_WRITER:CF-E-20:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-E-40:ACTIVE_ADDENDA
PROMPT_WRITER:CF-E-40:CURRENT_PF10_MARKDOWN
QA_PASS_BODY_CLASS_MAP
```

**`--work`** (work) — `ok: False`, exit 1, **10 errors**, stdout 6104 bytes, stderr empty:

```
PROMPT_WRITER:CF-C-20:ACTIVE_ADDENDA
PROMPT_WRITER:CF-C-20:AUTHORING_CONTEXT
PROMPT_WRITER:CF-C-20:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-C-40:ACTIVE_ADDENDA
PROMPT_WRITER:CF-C-40:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-E-20:ACTIVE_ADDENDA
PROMPT_WRITER:CF-E-20:AUTHORING_CONTEXT
PROMPT_WRITER:CF-E-20:CURRENT_PF10_MARKDOWN
PROMPT_WRITER:CF-E-40:ACTIVE_ADDENDA
PROMPT_WRITER:CF-E-40:CURRENT_PF10_MARKDOWN
```

The difference is exactly two errors: `PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10` and
`QA_PASS_BODY_CLASS_MAP` are gone, and the ten that remain are all `PROMPT_WRITER` —
`SF10-07`, which is the Product Owner's open decision and is untouched by this package.
Every other field of the two JSON documents, including the frozen-graph digest and all 55
body digests, is identical.

### Fixture suites

| suite | `--base` | `--work` |
|---|---|---|
| body-level (`--prompt-dir`) | **exit 1 — crash**: `ValueError: Mutation anchor absent: reject-source-epic-to-crd` | exit 0 — 164 cases, 0 failed |
| contract-only | exit 0 — 140 cases, 0 failed | exit 0 — 140 cases, 0 failed |

The body-level suite **cannot run at all** on the installed build. Its last line is the
crash above: a fixture mutation anchor that no longer matches, so the suite raises before
scoring any case. That is the `SF10-08` family — a harness returning no verdict rather than
a wrong one — and it is why the 164/0 on the repaired build is a restoration, not an
improvement in score.

### The other three validators

| run | `--base` | `--work` |
|---|---|---|
| `change-flow` contract validator | exit 0 — `PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy` | exit 0 — **byte-identical stdout** |
| `validate_flowmaster.py` | exit 0 | exit 0 — the difference is reproduced below |

**This was a prose summary and it went stale, which is why it is now generated.** It read "the
whole report differs in 2 line(s) … its `fixture_source` absolute path and its
`validator_revision`", and the `SF10-04` roster retirement landed later in the same round and
removed a six-line `flowmaster-propagate` block from the work-side report. The summary was then
false in both documents, with the commit that falsified it recorded a few hundred lines away in
one of them. The recorder now runs each tree's own copy of the validator and embeds the
difference itself, so `--check` fails if it moves.

Each tree's own `flowmaster-validate/scripts/validate_flowmaster.py` is used, because its
`DEFAULT_ROOT` is the tree holding the script — that is what makes a scratch copy validate
itself. The two tree roots are normalised to `<tree>`: the report prints `fixture_source` as an
absolute path, and where the copies live is not a behavioural difference. Both copies exit 0;
the recorder refuses to record a difference count for a nonzero run.

<!-- generated: flowmaster-diff -->
```diff
--- base
+++ work
@@ -1530,8 +1530,2 @@
     },
-    "flowmaster-propagate": {
-      "core_sync": null,
-      "errors": [],
-      "status": "PASS",
-      "warnings": []
-    },
     "flowmaster-validate": {
@@ -1562,3 +1556,3 @@
   "suite_ok": true,
-  "validator_revision": "3.2.6",
+  "validator_revision": "3.2.7",
   "verdict": "FLOWMASTER_SUITE_PASS",
```
<!-- /generated: flowmaster-diff -->

### Guard-block parity — D8/D15

| copy | chars | md5 |
|---|---|---|
| `base/change-flow` | 7355 | `46c69eaf8f00672e44f8502bbf43c721` |
| `base/flowmaster-validate` | 7355 | `46c69eaf8f00672e44f8502bbf43c721` |
| `work/change-flow` | 7355 | `46c69eaf8f00672e44f8502bbf43c721` |
| `work/flowmaster-validate` | 7355 | `46c69eaf8f00672e44f8502bbf43c721` |

**1 distinct value across all four copies.** The block is the four functions
`_addendum_paths`, `_ambiguous_addendum_keys`, `pf10_addendum_contract_key_drift`, `addendum_list_value_drift`.
The guard is the part that must stay byte-identical between the two validator copies, and it
is untouched by this package.

### The bench

Exit 0. **19 cases, 0 not as expected.** Full stdout:

```
corpus gate: 55 registry digests loaded from /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md
corpus gate: all 55 bodies match their recorded evidence_contract digest

=== SF10-03 — QA-120 class map (validate_qa_closure_bodies) ===
  [PASS] installed build reports a defect on the real body
        expected ['QA_PASS_BODY_CLASS_MAP']
        got      ['QA_PASS_BODY_CLASS_MAP']
  [PASS] repaired build reads the real HTML body
        expected []
        got      []
  [PASS] repaired build also reads the pipe rendering
        expected []
        got      []
  [PASS] repaired build still rejects a wrong receiver
        expected ['QA_PASS_BODY_CLASS_MAP']
        got      ['QA_PASS_BODY_CLASS_MAP']
  [PASS] repaired build still rejects a wrong page id
        expected ['QA_PASS_BODY_CLASS_MAP']
        got      ['QA_PASS_BODY_CLASS_MAP']

=== SF10-06 — handoff obligation (validate_prompt_bodies) ===
  [PASS] installed build reports GCFPE-MGMT-10
        expected ['PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10']
        got      ['PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10']
  [PASS] repaired build clears the corpus, GCFPE-MGMT-10 and PR-50 included
        expected []
        got      []
  [PASS] repaired build catches a dropped receiver (PR-30 -> PR-35)
        expected ['PROMPT_HANDOFF_RECEIVER:PR-30:PR-35']
        got      ['PROMPT_HANDOFF_RECEIVER:PR-30:PR-35']
  [PASS] repaired build catches GCFPE-MGMT-10 dropping PR-10
        expected ['PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10']
        got      ['PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10']

=== SF10-06 — the registry's handoff literal, kept alongside the receiver check ===
  The approved registry requires NEXT_PROMPT_HANDOFF on 53 of its 55 rows and exempts
  exactly GCFPE-MGMT-10 and PR-50. The clean-corpus case above passes while both of
  those bodies lack the token, which is the exemption working; the case below proves
  the requirement still bites everywhere else. The installed build is not contrasted
  here: it also catches a dropped literal on PR-30, because PR-30 has a non-terminal
  public branch. The two builds differ only on GCFPE-MGMT-10, which is the case above.
  [PASS] repaired build catches a dropped handoff literal (PR-30)
        expected ['PROMPT_HANDOFF_LITERAL:PR-30']
        got      ['PROMPT_HANDOFF_LITERAL:PR-30']

=== SF10-06 — receiver ids match as complete tokens ===
  QA-10 is a prefix of QA-100, the one such collision among the 55 ids. MGR-10 routes
  to QA-10 and names it once; swapping that token for QA-100 leaves the substring
  present, so a substring test would pass and boundary matching must not.
  [PASS] repaired build catches a prefix-collision receiver (MGR-10 -> QA-10)
        expected ['PROMPT_HANDOFF_RECEIVER:MGR-10:QA-10']
        got      ['PROMPT_HANDOFF_RECEIVER:MGR-10:QA-10']

=== SF10-06 — `_` is an identifier character too ===
  Review asked whether `_` belongs in the boundary class. It does, and the corpus
  proves it rather than a hypothetical: `PR_RETURN_PHASE` values are written
  `PR-30_PREPUBLICATION` and `PR-30_POSTPUBLICATION`, and OPS-20 writes
  `NOT_PRODUCED_BY_OPS-20` -- 54 underscore-adjacent prompt-id occurrences in all.
  Those are enum tokens, not routing mentions. ESC-40 is the subject because it is
  real on both halves: it declares PR-30 as a receiver AND already carries six
  `PR-30_` enum tokens beside its five complete mentions. Burying those five leaves
  a body that discusses `PR-30_PREPUBLICATION` constantly and never names PR-30 --
  the exact shape of the hazard, not an invented one. Adding `_` to the class flips
  none of the 166 declared receiver checks on the clean corpus, so this closes a
  reachable hole without moving a single current verdict.
  [PASS] repaired build catches a receiver buried in an enum token (ESC-40 -> PR-30)
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:PR-30']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:PR-30']

=== SF10-06 — malformed route data fails closed through the structured path ===
  The container was validated; the elements were not. Review found the gap and
  understated it: an int element is silently absent from EXPECTED_MEMBERS and
  skipped without a word, and BOTH a dict and a list element raise
  `TypeError: unhashable type` from the membership test -- which aborts body
  validation entirely rather than reporting a contract defect. That is the same
  crash-instead-of-verdict shape as the installed build's fixture-suite failure.
  All three now surface as MALFORMED_DESTINATIONS, which is what the code already
  promised. The subject is a real ESC-40 public row, not a synthetic contract.
  [PASS] repaired build reports MALFORMED_DESTINATIONS for a non-string scalar
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
  [PASS] repaired build reports MALFORMED_DESTINATIONS for an unhashable dict
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
  [PASS] repaired build reports MALFORMED_DESTINATIONS for an unhashable list
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
  Null and absent are rejected too, and for a reason the shape states: a
  non-terminal public row's whole meaning is that the invocation continues
  somewhere, so declaring no route at all is malformed. The old guard read
  `destinations is not None and not isinstance(..., list)`, so both slipped
  through and the loop iterated nothing -- silence where a verdict belonged.
  The contract-level STATE_DESTINATION check already required a list here, so
  the lax body-level guard also disagreed with the stricter one in the same
  file. Measured on the real contract first: all 208 non-terminal public rows
  carry a non-empty list, so requiring one costs nothing. An EMPTY list is
  deliberately NOT flagged, because STATE_DESTINATION does not flag it either
  and this check must not be quietly stricter than the rule it mirrors.
  [PASS] repaired build reports MALFORMED_DESTINATIONS for a null destinations value
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
  [PASS] repaired build reports MALFORMED_DESTINATIONS for an absent destinations key
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']

=== SF10-06 — an unknown destination string is malformed, not a symbol ===
  The contract declares five non-prompt destinations -- NATHAN_TERMINAL_RETURN (54
  rows), ORIGINAL_NATIVE_STAGE (39), ACTUAL_OWNER_TERMINAL_RETURN (18),
  NATHAN_MANUAL_MERGE_ASSERTION (2), NATHAN_PROCEED (1) -- counted from the contract,
  not recalled. Skipping everything merely absent from EXPECTED_MEMBERS made a typo
  indistinguishable from a symbol: `PR-300` was ignored exactly as NATHAN_PROCEED is,
  and the receiver that row meant to name was never checked. With the roster named in
  SYMBOLIC_DESTINATIONS, anything else fails closed.
  [PASS] repaired build reports MALFORMED_DESTINATIONS for an unknown destination (ESC-40)
        expected ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
        got      ['PROMPT_HANDOFF_RECEIVER:ESC-40:MALFORMED_DESTINATIONS']
  And the five declared symbols must still be skipped rather than flagged -- the
  clean-corpus case above is that control: all 42 symbolic destinations on
  non-terminal public rows pass through it without an error.

=== SF10-06 — the predicate's remaining limit, asserted rather than hidden ===
  The check asserts that each declared receiver is NAMED in the body. It does not
  bind that name to the operative handoff, so retargeting PR-30's last mention of
  PR-35 to PR-40 -- while its earlier mentions stay -- is NOT caught. The case
  below asserts that blind spot so it cannot be mistaken for coverage.
  Review asked for the stronger check: parse the operative handoff and validate
  its receiver. It is not implementable against this input, and the reason is
  categorical rather than a tuning problem. Measured over the 55 bodies: all 68
  NEXT_PROMPT_HANDOFF occurrences are PROSE, and zero are inside a fenced block.
  The bodies are prompts -- they instruct a runtime to EMIT a handoff block; the
  block does not exist until the prompt runs, and this validator never sees a run.
  There is no operative binding in the artifact to parse. An earlier note here
  justified the limit by a 17-of-166 false-failure count from one scoped variant;
  that was a symptom, and this is the cause.
  [PASS] retargeting the last mention is NOT caught (known limit)
        expected []
        got      []

ALL CASES AS EXPECTED
```
