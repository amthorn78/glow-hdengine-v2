---
artifact_type: PE_SESSION_TASK_REPORT
artifact_version: "1.0"
created_date: 2026-09-22
session: PE36
task: docs/ephemeral/pe36.task-01/TASK-01-skill-write-boundary-revision.md
authority_document: docs/prompt_ecosystem_management/notion-write-boundary.md
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
change_class: "B — rule application (ecosystem-change-management.md §2 Step 1)"
installed_by_pe36: false
---

# PE36 Task 01 — three skills brought into line with the Notion write boundary

Three `.skill` packages are built and validated and **nothing is installed.** The independent
§10 review has not run. Only Nathan installs.

## What the packages are scoped to

| package | files | package bytes | sha256 of the `.skill` |
|---|---|---|---|
| `glow-workspace-currency.skill` | 3 | 13,536 | `6491301202e7d310ff9785bb1fc36a8c45d6b704ad8d6e65a3fa37c52885eecb` |
| `glow-artifact-storage.skill` | 1 | 4,850 | `8a7c074e39dc30a436b0c330290c0f60048f9842d6dbb80324b889edc5c69cfd` |
| `glow-write-boundary.skill` | 1 | 4,199 | `cfe2d7a900c36ea67a413282cff758c66c181a3e85cc543aeaba2425619ad494` |

They install **independently**. No package depends on another; each is a prose-only skill.

## Identity — baseline and repaired

`freeze.py` rooted at the **skill directory**, never the synced tree
(`skill-identity-and-freeze.md`). Format is `<file count> <sha256>`.

| skill | baseline (installed, measured this session) | repaired |
|---|---|---|
| `glow-workspace-currency` | `3 0beffb2a3bf14274c7088ab260eb5f44c6842ca02400cc3de22de2e7be226dbe` | `3 5f2b4ae0d43f0609ae3c3b88409a2578791b008cf6908bd6516181688e06dd93` |
| `glow-artifact-storage` | `1 895488910744a108e193ab8cb76d4f9fa3e02e8903323bfea3009e70c2d5e6a7` | `1 502b4ecf11cea156702207ddb829b2d51064fe9eaa8678ac5db05c04375cba1c` |
| `glow-write-boundary` | `1 c0e3875b4e932e516b75962d37c5bafaf57664eef9de1e036009c96c03e50a27` | `1 662f9647ccfd996aa72e3d80ac70edc3d06a4310805ef14207b1340c69e93fc4` |

Each repaired digest was reproduced **from the extracted `.skill` contents**, not from the
working copy, and matched. The unrelated installed skills were measured too and are unchanged:
`change-flow` `21 80e877c2…`, `flowmaster-validate` `29 b9ca212a…` — the two digests the
succession record names. **The round-30 baseline reproduces.**

## Every file that changed — four, derived by `diff -rq`, not typed

```
glow-workspace-currency/SKILL.md
glow-workspace-currency/references/notion-operations.md
glow-artifact-storage/SKILL.md
glow-write-boundary/SKILL.md
```

`glow-workspace-currency/references/drive-retrieval.md` is byte-identical to the installed
copy and is listed here so its absence from the change set is a measurement, not an omission.

The full unified diff is `pe36-task01.diff` beside this report, 192 lines.

## The design principle applied

> **The obligation stays absolute. Only the destination becomes conditional.**

The six triggers in `glow-workspace-currency` §2 — what counts as a state change — are
**byte-identical to the baseline**, verified by hashing that block in both trees. Nothing was
removed. What changed is where the record lands, and the destination table is copied from
`session-working-rules.md`'s *Tracking is part of the work*, so the three surfaces converge on
one wording rather than three (`ecosystem-change-management.md` §2 Step 3).

### `glow-workspace-currency` — 5 edits

1. **Description**, one clause: *"writing any state change back to Notion"* → *"recording any
   state change at the destination that holds it - Notion for ecosystem-maintenance surfaces,
   docs/ephemeral otherwise -"*. Every trigger term is preserved verbatim: the whole
   *"Glow, GCFPE, HDE, Change Flow, prompt repair, batches, ledgers, reports, verdicts, plans,
   checklists, releases, PF10, or Alpha"* list, *"Open every task by searching BOTH Notion and
   the repository"*, *"reading it back before reporting it"*, and both closing sentences.
2. **Opening**, one paragraph: the read-only default stated before the framing can be read as
   an obligation, ending *"This never relaxes the obligation to record."*
3. **The three obligations**: *"Any state change goes to Notion"* → *"is recorded … at the
   destination that already holds it"*. *Consult* and *Verify* untouched.
4. **§2 "Where it lands"**: the session-kind table, the safe default, and a pointer to the
   policy's not-an-authorization list. Placed after the six triggers, which stand unchanged.
5. **§3 Verify**: read back *"from wherever it landed"*, with *"This obligation does not vary
   by destination"* stated explicitly so the scoping cannot be read as a weakening. The worked
   example is labelled an ecosystem-maintenance session, since that is why Notion is right in it.

### `glow-artifact-storage` — 3 edits

Description: *"Prompts are authored and revised directly in Notion."* → *"Only durable,
Notion-managed prompts are authored and revised directly in Notion."* The routing table gains
a second row for the five excluded categories, and the *Notion: author in place* section is
scoped to durable members with the policy cited.

### `glow-write-boundary` — 3 edits

The destination table's Notion row is qualified; a Notion paragraph is added to *The open
paths*, parallel to the existing Drive paragraph; and *"A prompt, plan, or state? Notion."*
becomes three routed questions that give the excluded categories somewhere to go.
**Its description was not changed** — it lists allowed destinations and states no Notion-write
obligation, so no edit was required and none was made.

## A fourth instance of the same conflict, found by reading the artifact

The brief quotes three conflicts and its quotations were checked against the installed bytes:
**all three are accurate.** They are not exhaustive. Reading the skills in full surfaced the
same unqualified sentence in a fourth place:

`glow-workspace-currency/references/notion-operations.md`, *What not to do*:

> Don't author a prompt as a local file and transfer it in. Prompts are authored
> and revised directly in Notion — see `glow-artifact-storage`.

This is the `glow-artifact-storage` conflict verbatim, inside an in-scope skill's reference
file. It was corrected in the same change. It is **not** the out-of-scope case the brief
describes — that case is a *fourth skill*, and no fourth skill was touched.

Two further unquoted instances were inside the in-scope SKILL.md files and are covered above:
`glow-artifact-storage`'s routing row and *Notion: author in place* section, and
`glow-write-boundary`'s destination-table row.

## Gates actually run — and what they are not

These are **prose skills with no validator of their own.** There is no fixture suite, no
hash-pin chain, no self-identity check. Saying otherwise would be the overstatement the
succession record warns about.

| check | result |
|---|---|
| `scripts.quick_validate` on each working tree | `Skill is valid!` ×3 |
| `scripts.quick_validate` **from the extracted `.skill` contents** | `Skill is valid!` ×3 |
| archive layout — every entry under its skill root, no traversal | confirmed, 5 entries total |
| `name:` frontmatter unchanged | confirmed against the installed tree ×3 |
| repaired digest reproduced from extracted contents | matched ×3 |
| reference files survived packaging | both present in `glow-workspace-currency.skill` |
| `diff -rq` extracted vs installed | exactly the four files listed above |
| six state-change triggers vs baseline | `sha256` of the block equal, `fd571777…` |
| every baseline heading still present | 11 / 13 / 8, none missing |
| bytecode written anywhere | none — `PYTHONDONTWRITEBYTECODE=1` throughout |

Everything else is a careful read and the diff. That is the whole check.

### One gate did fail, and caught a real defect

The first `glow-artifact-storage` description ran to **1,069 characters against a 1,024
limit** and `quick_validate` rejected it. The baseline description is 966 characters, so the
headroom was 58. The replacement clause was cut to the minimal form that carries the
carve-out, landing at 995 with 29 characters of margin; a 110-character candidate that landed
at exactly 1,024 was rejected as too fragile to survive any later edit.

## A departure from the brief's procedure, stated plainly

The brief's step 4 says *"Bump each skill's own version."* **These three skills have no
version to bump**, and this was measured rather than assumed:

```
grep -rnE 'SKILL_TREE_SHA256|_REVISION|validator_revision|^version:' <the three skills>
→ no matches
frontmatter keys, all three: name, description
```

No skill in this workspace carries a `version:` field. The `FLOWMASTER_VALIDATE_REVISION` /
`validator_revision` mechanism that *"advertised identity must be unspent"* governs belongs to
`flowmaster-validate` and `change-flow`; the set of advertised identity values in these three
is empty, so the mandated diff against the previous package is vacuous rather than passing.

**No version field was invented.** `prompt-body-content-policy.md` settles which authority
owns the fact: *"Skill identity belongs to the skill's own digest."* Adding a `version:` line
to three skills that load their frontmatter into every session would create a second identity
surface that can disagree with the digest — the exact shape that document forbids. The
distinguishing identity for these packages is the `.skill` sha256, delivered first in the
caption, one package per line, and confirmed after install by digest comparison.

This is a coordinator-level implementation consequence of a ruling already made
(`ecosystem-change-management.md` §6), not a policy question. It is recorded here because it
departs from a literal line in an authorized brief, and that should not be found by a reviewer.

## Notion

**No Notion write was made, and none is authorized for this task.**

Searched: `glow-workspace-currency`, the Notion write-boundary policy by name, and the round
tracking page. The Glow Operations Hub carries only a *brief* pointing at
`notion-write-boundary.md`; no Notion page records these three conflicts as open. The only
record that claims they are open is the conflicts table in `notion-write-boundary.md`, in this
repository, and this change updates it.

So nothing in Notion goes stale, nothing there needs correcting, and the task instruction
directs no Notion write — which is `notion-write-boundary.md` applied to its own repair.

## What is not done

- **The independent §10 review has not run.** `REVIEWER-PROMPT-pe36-task01.md` is filled and
  delivered with the packages. A prior verdict does not exist for these skills; this is a
  first review.
- **Nothing is installed.** Only Nathan installs. An install is complete when the installed
  tree measures the repaired digest the verdict names — not when anything returns green.
- **Nothing is merged.** Nathan merges. The branch is
  `docs/20260922-pe36-task01-skill-write-boundary` and the pull request is **#461**, open, four
  changed files, read back from the API rather than inferred from having pushed.

## Out of scope, untouched

`AF-001`–`AF-004`, the reconciliation backlog, `HDE-EPIC040`, PR #457, the selected release's
55 prompt bodies, the contract, the graph, the registry, and every other skill.
