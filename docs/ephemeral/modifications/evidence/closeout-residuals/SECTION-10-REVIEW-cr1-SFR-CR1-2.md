---
artifact_type: SKILL_FIT_REVIEW
reviewer: SFR-CR1-2
round: cr1 (MODIFICATION-20260923-closeout-residuals, first review of its packages)
brief: docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-PROMPT-cr1.md, commit 6a643d6, 18944 B, sha256 e48d773782fa062f9adf02b4ec2263cd1897bac4dcb03e2d1b0585e15cbb29a9 (working tree and commit blob agree)
repository_head_reviewed: 6a643d6ec4a379c8c8d6585c6c87ae9c98ac8059 on branch docs/20260924-closeout-residuals-execute (local and origin agree; not merged; origin/main is 7028bea). HEAD was the same at the start and at the end.
reviewed_at_utc: 2026-09-24T14:16Z
scratch: /tmp/claude-0/-home-user-glow-hdengine-v2/219095eb-5889-516e-828c-322c5d5d5b5c/scratchpad/sfr2/ (my caller directed this location, in place of the brief's /tmp/claude-0/review-SFR-CR1-2)
supersedes: nothing. First review; successor record to no earlier record (AUTH-001).
---

# Section 10 review, round cr1: SFR-CR1-2

## Verdict

**SKILL_FIT_CONFIRMED**

This verdict covers only the seven packages below, installed together in one sitting, as they sat in
`/tmp/claude-0/-home-user-glow-hdengine-v2/219095eb-5889-516e-828c-322c5d5d5b5c/scratchpad/skills-out/`.
I measured every value from those archives. **The verdict is void for any other bytes.** No earlier
confirmation or measurement carries to these bytes, and I relied on none.

| package | files | bytes | archive sha256 | extracted freeze (freeze.py) |
|---|---|---|---|---|
| flowmaster-validate.skill | 31 | 322703 | `ecdb49ff38c937d12332dd4ab99978fa6c0f6d33c77db06bfd758af17eb5bed0` | `31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626` |
| change-flow.skill | 22 | 258193 | `aa11c933a99b0ca590ed54a8fae4f7a1c5a1946a0754374f2183ce84800ca13b` | `22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47` |
| glow-graph-contract.skill | 9 | 55695 | `a908cde3adc4f15a3454589b42141734a9119ac4fe917d2159e86e4218bd3b49` | `9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c` |
| session-relay-flowmaster.skill | 5 | 56250 | `54d272867892e596cda9d54b2bd2c8e005f34f3ea799692c30672191526746a8` | `5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4` |
| glow-hde-pr-development.skill | 4 | 22605 | `59b42809024807f81eac7ba766617ba9cec0cf96ee85b07da68b7ec8dfcdacf2` | `4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a` |
| amthor-workspace-governance-audit.skill | 15 | 56629 | `87c59a6cef700ee7dd2c32f0a378225319b5837d49af52a239cd1a4c007615e7` | `15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab` |
| glow-po-reporting.skill | 1 | 3776 | `bb7d7967f05443fda739918e1ce6e636658501443f03e39caafafa149015906c` | `1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1` |

Every claim C1 to C5 holds on these bytes, except one scoped gap in ITEM-05 that I list rather than
block on (L-1): the governance audit's snapshot script still hashes a prompt-body file when no source
index declares it as a prompt, and the skill text never names the index. It fails loudly on the only path
that can run a prompt audit, and it hashes less than the installed baseline, which hashed every source. I
found no required defect. Eleven listed findings follow, each with a smallest correction. None needs to be
repaired before install unless Nathan opts in.

## What I ran, and what I could not

Everything ran with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` in my scratch, from a scratch copy.

| step | result |
|---|---|
| §3 baseline, `freeze.py` on the seven installed skills | all seven reproduce the brief's §3 digests exactly. The tree did not move: the same seven digests, the same archive sha256s and the same repository HEAD at the end. Only the synced root's `manifest.json` mtime changed (L3) |
| §8a archives | sizes and sha256 as §1. Each zip has exactly its file count of entries, no directory entries, no duplicates, no symlinks, no `..`, no absolute path, and every entry under `<skill>/`. `testzip` is clean. Frontmatter `name:` is unchanged in all seven (the audit and graph-contract `description:` lines change) |
| §8b freeze of the extracted trees | the seven lines equal `EV/skills/expected_after_patch.txt` byte for byte (`diff` exit 0) |
| §8b `run_gate.py --set pkg --pkg-root <my root built from the extracted archives>` | **exit 0; 34 rows, 34 ok, `not_run` empty, top-level `ok: true`**. I read each row's `ok` and the suites' own flags (`suite_ok: true`, `fixture_suite_ok: true`, relay `status: PASS`, audit `OK`). Every row's `observed` equals EX/gate_pkg.json's |
| §8c `diff -rq -x __pycache__` installed vs extracted | exactly the 27 changed and 3 added files §8c lists, and nothing else |
| C1, independently | I applied each `EV/skills/diffs/<skill>.diff` with `patch -p1` to a copy of the installed skill: all seven equal the extracted packages (`diff -r` silent). I also rebuilt all seven from the installed tree plus `results/edits_final.json` (113 text edits and 3 pin edits, each old string found exactly once), my own regenerated 4.1.1 contract and the 3 new files: all seven reproduce, so every changed byte carries an item label |
| §8d contract | both bundled copies are byte-identical, 613326 B, `dbae180b…`. `contract_recipe.py` with 4.1.0 / 1.3.0 gives E2 `7a7fd028…` and `6902924a…`, EQUAL to both *installed* copies. With 4.1.1 / 1.3.1 it gives E2 `5ad52062…` and `dbae180b…`, EQUAL to both *packaged* copies. `diff` of the two outputs is exactly two lines: `contract_revision` and `.pr_development_contract.primary_skill_revision`. A structural walk of installed against packaged contract finds the same two paths and nothing else |
| §8d graph | the branch's `docs/graph/parts` build to 55 nodes, 229 edges, 55 state_routes keys and 282 rows, all with `source_evidence`. Embedded JSON 575074 B `ae2bd159…`, byte-equal to both bundled graphs; graph.md 575672 B `a70a9326…` |
| §8e hash pins | recomputed: `SKILL_TREE_SHA256` = `ed52208f…`, equal to the declaration. The contract `dbae180b…` equals the profile `candidate_contract.sha256` and `EXPECTED_CANDIDATE_CONTRACT_SHA256`. The graph `ae2bd159…` equals the profile, fv `EXPECTED_FROZEN_GRAPH_SHA256`, cf `EXPECTED_GRAPH_SHA`, both contracts' `source_snapshot.frozen_candidate_graph.sha256` and the gate's candidate root. The oracle is `ede635b1…` and the fixtures `c433aa09…`. Unchanged pins (URL map, topology readback, runtime maps, R1 oracle, `flowmaster-primary` file `06655077…`) also agree |
| §8f revisions by grep | 3.3.1 in both skills' markers. `validator_revision` 3.3.1 at exactly four sites: profile `:45`, `run_gcfpe_20260914_fixtures.py:828`, `validate_gcfpe_20260914.py:1166`, `validate_flowmaster.py:1903`. Relay 3.2.0 at 2 sites, PR skill 1.3.1 at 8, audit 1.13.0 at 2, contract 4.1.1 at 5. No 3.3.0, 1.12.0 or stale 4.1.0 / 1.3.0 remains outside explanatory docstrings, a historical comment (`validate_gcfpe_20260914.py:1464`) and historical 3.1.0 contract content |
| reindex claim | on the pre-reindex parts from `git archive 77d98dd` (freeze `56 980af73e…`): `reindex` rewrites 27 files, a second reindex rewrites 0, and the result is byte-identical to the branch's parts. The *installed* builder gives `ae2bd159…` on both the pre-reindex and the reindexed parts, so the reindex did not change the build |
| §8g own probes | 104 must-fail and control probes, below. None is copied from the author's regressions |
| extra | historical fixture runners (alpha-feedback, epic-alpha, final-scan, integrated-readiness, strength-middleware) give the same results on the baseline and the packages. All package scripts compile. A symbol-table scan finds no undefined global name in any package script (the baseline's `paths` in `validate_gcfpe_current.py` is gone) |

**Not run:** the author's PLAN regression scripts (L4: not in the repository; I read their recorded
outcomes, which total 36/36, 20/20, 33/33 and 11/11 plus a 32-case baseline control set, and wrote my own
probes). The `post` gate set, which comes after install (L2). Anything touching Notion or a prompt body
(L1, D22): I fetched, read, copied and hashed no prompt body. My probe bodies are synthetic strings I wrote,
not Notion content, so no D22 transient file arose.

## §6, answered

**A1. Can a body-copying, body-hashing or corpus-snapshot instruction survive and pass every suite?**
Yes, in the forms the record already volunteers (D14 note: prose paraphrase) and in one script path it
does not (L-1). Exact-phrase regressions all fire: 10 of 10 probes. They are the retired phrase in
change-flow's specialization, the same phrase in Title Case and inside the prohibition block (caught by
change-flow's own validator), each override sentence removed, relay `optional digest`, and fv
`its recursively loaded corpus` and the profile's `complete 55-member prompt corpus`, both with
`SKILL_TREE_SHA256` re-stamped, as an author would re-stamp it, so the phrase guard fires rather than the
identity check. They also cover the audit's `Use complete pinned snapshots` and the audit script hashing
prompt-kind sources again. Nine probes passed every suite:
- whitespace variants of a guarded phrase: `source revision / content identity`, and `optional` then
  `digest` split across a line break;
- a paraphrased copy-hash-byte-compare instruction in change-flow and in the relay;
- a paraphrased local-corpus requirement in fv (re-stamped), and a paraphrased prompt snapshot in the audit
  SKILL.md;
- a script-level paraphrase, where the audit stores `sha256_text(text)` of each prompt body in its output;
- body-hash or corpus-export instructions in the PR skill and glow-graph-contract, which ITEM-16 leaves
  unguarded by scope.

On a read of every changed file and the D22-sensitive terms in all seven packages, the one live residual
is L-1. L-2 is a presumption carried in unchanged text.

**A2. Is the protected core byte-identical, with the ITEM-08 sentence outside it?** Yes. The
`FLOWMASTER_CORE_BEGIN…END` block is byte-identical (`4d8bb9bf…`, the contract's
`flowmaster_primary_core_sha256`) in flowmaster-primary, change-flow, session-relay-flowmaster,
session-branch-flowmaster and tw-flowmaster. Each file has exactly one marker pair. The sentence occurs
once in change-flow (line 267) and once in the relay (line 259), both inside
`FLOWMASTER_SPECIALIZATION_BEGIN`. It is absent from the three skills ITEM-08 excludes. Removing it at
either site fails `CONTRACT_REQUIRED`.

**A3. Builder, reindex, recipe, deriver.** The builder rejects each of these and reindex repairs them:
- a dropped, extra, duplicate, out-of-range, negative or null index;
- missing `_other_edge_indices`;
- an edge moved to another part, or added, without a reindex.

It accepts the reindexed parts with token `ae2bd159…`, and a second reindex is idempotent. It does not
reject JSON `true` for index 1 or `N.0` floats, and reindex leaves them in place (L-3). A string index
crashes both commands with `TypeError`, fail-closed but unnamed (L-3). The recipe reproduces `6902924a…`
from the kept template and `dbae180b…` with the new revisions. It failed on all 11 of my must-fail inputs:
- a wrong or malformed revision, or the wrong oracle;
- the D23-E heading duplicated or missing, or its section holding three `> ` lines, holding a changed line,
  or ending the file;
- a changed template, or a graph built from mutated parts.

It stayed EQUAL where it should: a later D23 successor with its own quotes, the extracted-JSON input form,
and a stale header hash. Under `python -O` it cannot run at all (L-9). The deriver catches drift (exit 1)
and a row without a part (exit 2). A part without a row exits 0 (L-8).

**A4. Whole-body release-line check.** It rejects a plain, bold, backticked, numbered, `1)`, `+`,
blockquote, table or heading label line at any depth. One case was checked at nonblank line 24, past the
old 8-line window. It does not reject a label mentioned mid-sentence, `Settings:`, `Set_up:` or the
`Prompt ID:` line. It wrongly rejects no legitimate line I could construct, with one ruling-consistent
edge: a label line inside a fenced template is rejected, as P-31's "anywhere, line-anchored" says. It
misses case and spacing variants (L-6).

**A5. Does anything still expect a Drive artifact plane?** No consumer, fixture or example expects
Drive as the GCFPE artifact plane. The relay SKILL.md, the enum, the validator, the self-test cases
`artifact_plane_repository` (PASS) and `artifact_plane_unknown_token` (FAIL) and the example agree.
`google-drive` has left the example's skills. No other skill in the root reads `ARTIFACT_PLANE`. The
generic Drive fixtures in `behavioral-test-fixtures.md` concern non-GCFPE file references. The D7
restriction is text only (L-7).

**A6. Is the named result reached on every path that raised NameError?** Yes. In the baseline every
`--bodies-stdin` JSON object reached `paths[...]`, including `{}` and `{"ZZ-99": 5}`, and each raised
NameError (confirmed on the installed tree). On the packages:
- a supplied body gives named `PROMPT_BODY_*` and `PROMPT_ROUTE_SEMANTICS:*` errors, exit 1;
- an unexpected ID gives `PROMPT_BODY_UNEXPECTED_ID`;
- `{}` gives `ok: true` with nothing evaluated, as the item's fixture intends.

Non-object JSON, a non-string value and malformed JSON still end in tracebacks, as they did before the
NameError point in the baseline (L-5).

**A7. Revision sites and pins,** recounted above. All agree. The contract changes in exactly its two
revision paths.

**A8. The recorded regressions.** Each group tests the author's own construction:
- 36/36 re-inject the exact phrases the author removed and the a5 probes the a5 reviewers named;
- 33/33 restore the old text item by item;
- 11/11 are P-25's own marker cases;
- 20/20 are function-level before/after pairs on the author's chosen inputs.

They do not reach:
- paraphrase (declared);
- whitespace or line-wrap variants of a guarded phrase;
- the audit's unindexed snapshot path (L-1);
- non-integer or string edge indices (L-3);
- reference definitions other than `[//]: #` (L-4);
- malformed `--bodies-stdin` in `validate_gcfpe_current.py` (L-5);
- release-label case and spacing variants (L-6);
- a part without a registry row (L-8).

**Question: is anything outside the items, PART-01 and RULING-5-Q3-A?** No. Every one of the 113 text
edits, 3 pin edits, 2 contract copies and 3 new files carries a label. Each label is an item, PART-01,
RULING-5-Q3-A, or REVISION (revision strings and re-declared pins). P-16 rides with ITEM-36, as spec §5.2
lists it. The per-package counts match spec §5.2.

## Findings (all listed, none required)

**L-1 (A1, ITEM-05): the snapshot script hashes a prompt-body file unless an index declares it a prompt.**
- *Artifact:* `amthor-workspace-governance-audit/scripts/audit_workspace_governance.py`,
  `build_snapshot_manifest` (`:458`, `:469`, `:473`), and SKILL.md "Acquire and pin sources" step 6.
- *Defect:* without `--source-index`, every file in the snapshot root becomes `kind: local_text` and gets
  `sha256`, `structural_sha256` and `size_bytes`. So does any source whose kind is not exactly
  `prompt`, `notion_prompt` or `notion_page`. The audit reads prompt text only from a file under the
  snapshot root, so the transient body file sits there. SKILL.md never names `--source-index`.
- *Evidence:* unindexed, a synthetic `IA-10.md` gets `sha256`. Indexed as `prompt`, it gets none. Indexed
  as `gcfpe_prompt`, it gets one again. The ITEM-05 fixture covers only the indexed path.
- *Why listed:* a project prompt audit succeeds only with prompt kinds; unindexed it fails loudly with
  INV-001 for every expected prompt. The baseline hashed every source.
- *Smallest correction:* step 6 names `--source-index`, with each prompt body file declared as `prompt`,
  `notion_prompt` or `notion_page`, and says an unindexed run hashes every file. Optionally, the script
  refuses an unindexed run whose root holds a `Prompt ID:` header, and a fixture covers it.

**L-2 (A1, unchanged text in a changed package): "Working a batch" step 2 cites a corpus path.**
- *Artifact:* glow-graph-contract SKILL.md `:157-159`.
- *Defect:* it still says to derive each field from "that prompt's persisted Notion body", with the
  example `source_evidence` `{"path": "candidate/prompts/b/IA-30.md", …}`. The example reads as a local
  corpus path. The parts use that form in 282 rows as a legacy citation key.
- *Smallest correction:* one sentence saying the path is a legacy citation key naming the body, and that
  fields are derived from the Notion page read live (D22).

**L-3 (A3, ITEM-12): non-integer indices are accepted, and a string index crashes.**
- *Artifact:* `graph_parts.py` `index_bookkeeping_errors` (`:152`) and `reindex`.
- *Defect:* `true` for 1 and `12.0` for 12 pass the build, with the token unchanged, and reindex leaves
  them, because Python equality treats them as the integers. A string index raises `TypeError` in both
  commands.
- *Smallest correction:* require `type(i) is int` for every index, reported as a named bookkeeping
  error, and compare index lists type-exactly in `reindex`.

**L-4 (ITEM-15 residual): other link-reference definitions hide text and pass every gate.**
- *Artifact:* `validate_flowmaster.py` `DISPATCH_HIDING_RE` (`:758-760`).
- *Defect:* only `[..]: #` reference definitions are matched. `[comment]: <> (text)` and a titled
  definition `[n]: https://… "text"` also hide their text in rendered Markdown. Both passed every suite
  when appended to a carrying file. The limit note names only `<div hidden>` and `<details>` (and P-33
  names type-6 blocks). The a5 finding's own correction (a) asked only for `#`, so this is a residual, not
  a failed repair.
- *Smallest correction:* match any link-reference-definition line (`^[ \t]{0,3}\[[^\]\n]+\]:`), or add
  "reference definitions other than `[//]: #`" to the limit note.

**L-5 (A6): `validate_gcfpe_current.py` does not check the shape of its stdin.**
- *Artifact:* `validate_gcfpe_current.py` `main` (`:692`).
- *Defect:* it parses `--bodies-stdin` without the shape check its sibling `validate_gcfpe_20260914.py`
  has (`BODIES_STDIN_MALFORMED`, `BODIES_STDIN_NOT_ID_TO_TEXT_MAP`). `[]`, `"x"`, `{"RS-10": 5}` and
  non-JSON exit 1 with a traceback, on both the alias path and the v4 path. This is fail-closed and was
  present before the change.
- *Smallest correction:* reuse the sibling's check.

**L-6 (A4): case and spacing variants of the release labels pass.**
- *Artifact:* `validate_gcfpe_20260914.py` `RELEASE_HEADER_KEYS` (`:979`).
- *Defect:* `Ecosystem Release:`, `SET:`, `PROMPT VERSION:`, `Prompt version :`, a double space and a
  non-breaking space are not rejected. The registry's patterns share the limit. No such variant occurs in
  the repository today.
- *Smallest correction (optional):* case-fold and collapse whitespace before the `startswith`.

**L-7 (A5, ITEM-14): the validator cannot enforce the GCFPE artifact-plane rule.**
- *Artifact:* `validate_relay_manifest.py`.
- *Defect:* "A GCFPE run's `ARTIFACT_PLANE` is `REPOSITORY` or `NONE`" (SKILL.md `:378`) is prose only.
  The shipped example, which names the Glow repository, validates PASS with `GOOGLE_DRIVE`, because a
  manifest carries no GCFPE marker. ITEM-14 claims agreement, not enforcement.
- *Correction:* none needed. Record it as a limit.

**L-8 (A3, ITEM-13): the deriver checks rows against parts, but not parts against rows.**
- *Artifact:* `registry_deriver.py` `drift` (`:58`).
- *Defect:* a part with no registry row exits 0. The gate compensates by asserting `parts: 55`.
- *Smallest correction:* report `parts_without_row` and exit non-zero on it.

**L-9 (A3, ITEM-13): the recipe's guards are `assert`s, and the generate call sits inside one.**
- *Artifact:* `contract_recipe.py:55`, and the guards in `regenerate_contract.py`.
- *Defect:* all of their guards are `assert` statements, and the side-effecting `rc.generate(...)` call is
  itself inside one. Under `python -O` or `PYTHONOPTIMIZE`, the recipe cannot produce output and fails with
  `FileNotFoundError`. It fails closed, but the message is misleading.
- *Smallest correction:* call `generate` outside the `assert`, and raise `SystemExit` for the checks.

**L-10 (brief, not a package): §4 names a branch that does not exist.**
- *Artifact:* REVIEWER-PROMPT-cr1.md §4, from `REVIEWER-PROMPT-cr.draft.md:86-91` and `fill_brief.py`.
- *Defect:* §4 names branch `claude/epic-tesla-17406z`, which does not exist locally or on origin. Its
  fallback ("it merged … read main") would send a reviewer to `main`, which holds none of this attempt's
  commits. The attempt runs on `docs/20260924-closeout-residuals-execute`, which the resumed plan's
  `docs/*-closeout-residuals-execute*` pattern names. I read that branch's HEAD `6a643d6`, whose parent is
  the `2729f88` the brief states.
- *Smallest correction:* `fill_brief.py` fills the branch from `git rev-parse --abbrev-ref HEAD`.

**L-11 (observation): the candidate root's contents are not enforced.**
- *Artifact:* `validate_gcfpe_20260914.py:2650-2672`.
- *Defect:* fv SKILL.md now says the candidate root "holds only" the graph file "and never prompt bodies".
  The validator reads only that file and ignores anything else in the root, so a stale snapshot root with
  `prompts/` would still pass. It reads and hashes nothing extra, so D22 is not breached.
- *Smallest correction (optional):* reject any other file in the root.

## Compliance

I installed nothing, and wrote nothing to the synced skills tree, to the repository other than this file,
to Notion, Drive or GitHub. I made no commit and no push. I ran no git command that changes a branch. All
extraction, gate output and probes are under my scratch directory.

NOTHING NEEDED. The verdict lets the attempt continue. L-1 is the one listed finding I would repair before
install if Nathan opts in; it costs one SKILL.md sentence and a re-cut of the audit package.
