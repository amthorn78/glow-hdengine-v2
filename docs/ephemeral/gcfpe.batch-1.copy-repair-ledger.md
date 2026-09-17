# GCFPE Batch 1 Copy/Repair Ledger — repository-first re-run

```yaml
artifact_type: GCFPE_BATCH_1_COPY_REPAIR_LEDGER
artifact_version: "2.0"
ledger_date: 2026-09-17
authority: "Nathan / Product Owner, Batch 1 repair re-run authorization, 2026-09-17"
scope: BATCH_1_ONLY
contract_ledger: docs/ephemeral/gcfpe.batch-1.contract-ledger.md
prompts_in_batch: 11
prompts_edited_pass_1: 11
prompts_edited_pass_2: 6
prompts_reverified_pass_2: 11
prompts_confirmed_no_change: 0
complete_readback: 11
readback_failures: 0
```

Every body was fetched fresh from Notion immediately before editing and read
back completely afterwards. In each readback the target clauses are present,
and no other section moved. All eleven changed in this re-run, which is why no
row reads `CONFIRMED_NO_CHANGE`: the storage boilerplate was in every body.

## Per-prompt record

| # | Prompt | Notion page ID | Clauses changed | Finding IDs | Disposition | Readback |
|---|---|---|---|---|---|---|
| 1.01 | GCFPE-MGMT-10 | `3db4590a05eb81d1bb64ebcb3ca8eb54` | 3 | `B1-SA-01`…`03` | **REPAIRED** | COMPLETE |
| 1.02 | MGR-10 | `3db4590a05eb8108ad2dd4d0e20bd6c4` | 3 | `B1-SA-04`…`06` | **REPAIRED** | COMPLETE |
| 1.03 | CF-PO-10 | `3db4590a05eb8161b4d7cb6d07f5101c` | 4 | `B1-SA-07`…`10` | **REPAIRED** | COMPLETE |
| 1.04 | CF-C-10 | `3db4590a05eb8119a5a8e4d083fcf360` | 4 | `B1-SA-11`…`14` | **REPAIRED** | COMPLETE |
| 1.05 | CF-C-20 | `3db4590a05eb8173a73edc73f302a90a` | 4 | `B1-SA-15`…`18` | **REPAIRED** | COMPLETE |
| 1.06 | CF-C-30 | `3db4590a05eb8149a8d2ed42c9c01ffd` | 9 | `B1-SA-19`…`27` | **REPAIRED** | COMPLETE |
| 1.07 | CF-C-40 | `3db4590a05eb81269931cee342ce8a0e` | 3 + R1 | `B1-SA-28`…`30`, `B1-SDF-01` | **REPAIRED** | COMPLETE |
| 1.08 | CF-E-10 | `3db4590a05eb815b84a5c5a5ace85fe1` | 4 | `B1-SA-31`…`34` | **REPAIRED** | COMPLETE |
| 1.09 | CF-E-20 | `3db4590a05eb810eb177f7dced41bc8f` | 4 | `B1-SA-35`…`38` | **REPAIRED** | COMPLETE |
| 1.10 | CF-E-30 | `3db4590a05eb81b4be79f405566da9a7` | 9 | `B1-SA-39`…`47` | **REPAIRED** | COMPLETE |
| 1.11 | CF-E-40 | `3db4590a05eb8101b655ed223b11a85e` | 3 + R1 | `B1-SA-48`…`50`, `B1-SDF-01` | **REPAIRED** | COMPLETE |

**50 clauses across eleven bodies.** The distribution is not arbitrary: the
`-30` review prompts carry 9 each because the PF10 addendum field list names a
storage reference twice more, and the `-40` revision prompts carry only 3
because they hand their artifact to `-30` rather than referencing one.

## Copy quality of the replacement text

The same replacement was used wherever the same clause appeared, so the eleven
bodies stay consistent with each other and with the graph. Three forms:

**Artifact and source boundaries** — one paragraph, present in all eleven:

> Every artifact produced by this prompt is complete efficient machine-readable
> Markdown written at a path under `docs/ephemeral/` in the repository,
> committed and pushed on the working branch, read back completely, and
> referenced by its repository path. Nathan alone merges; an open pull request
> is a complete outcome. Repository paths outside `docs/ephemeral/` and
> `docs/graph/` are not written, and `docs/pfcanon/` is read-only. Google Drive
> is used only where Nathan directs a specific file there. Do not use ChatGPT
> Library artifacts or Library IDs. When a PFCanon source is necessary, resolve
> and read only the unique controlled Markdown source from `docs/pfcanon/`; do
> not open, compare, cite, or fall back to Google Docs, `.doc`, or `.docx`
> variants.

GCFPE-MGMT-10 reads "the batch branch" rather than "the working branch", which
is its own native vocabulary.

**Handoff rule** — present in all eleven:

> carry every required artifact that already exists by exact identity/version
> and its repository path, or its direct Notion URL for a Notion-resident
> artifact

**Artifact-specific references** — repaired in place to "repository path",
keeping each sentence's existing shape.

Three properties a reviewer can check directly:

1. **Markdown-only survived.** The `.doc` / `.docx` / Google Docs prohibition is
   the same sentence it always was, now reading from `docs/pfcanon/`.
2. **Drive is conditional, not absent.** Exactly one `Drive` occurrence remains
   per body, and it is the narrowing clause.
3. **The open-path statement replaces a false implication.** The old text let a
   reader infer repository writes were forbidden outright. The new text names
   the two writable paths, the read-only one, and who merges.

## What was deliberately not touched

- **No section was added, removed or reordered** in any body. Every edit
  replaced text inside an existing sentence or paragraph.
- **`Save/read back …` phrasings that name no destination** were left as
  written — for example CF-C-20 and CF-E-20 step 4, CF-C-40 and CF-E-40 step 5.
  They are governed by the repaired Artifact-and-source-boundaries paragraph and
  carry no contradicting clause of their own. Rewriting them would be
  re-authoring beyond a recorded defect.
- **No lineage was removed**, because none of the eleven bodies contained any.
  The only `drive.google.com` URL in each was the destination folder.
- **The five historical Batch 1 artifacts** are untouched and unrenamed.

## Second pass — `SPECIFICATION_FORMAT_AUTHORITY`, 2026-09-17

After PR #409 merged, the Product Owner mandated that specification formatting
comes from referenced canon. Six bodies were edited; all eleven were re-fetched
and re-read against the mandate.

| # | Prompt | Pass-2 change | Finding IDs | Disposition | Readback |
|---|---|---|---|---|---|
| 1.01 | GCFPE-MGMT-10 | none | — | **CONFIRMED_NO_CHANGE** | COMPLETE |
| 1.02 | MGR-10 | none | — | **CONFIRMED_NO_CHANGE** | COMPLETE |
| 1.03 | CF-PO-10 | none | — | **CONFIRMED_NO_CHANGE** | COMPLETE |
| 1.04 | CF-C-10 | kickoff schema token removed; field list kept | `B1-SFA-05` | **REPAIRED** | COMPLETE |
| 1.05 | CF-C-20 | schema token removed; 13-section list replaced by canon resolution | `B1-SFA-01`, `B1-SFA-02` | **REPAIRED** | COMPLETE |
| 1.06 | CF-C-30 | none | — | **CONFIRMED_NO_CHANGE** | COMPLETE |
| 1.07 | CF-C-40 | delta inherits the base's canon; no schema of its own | `B1-SFA-07` | **REPAIRED** | COMPLETE |
| 1.08 | CF-E-10 | kickoff schema token removed; field list kept | `B1-SFA-06` | **REPAIRED** | COMPLETE |
| 1.09 | CF-E-20 | schema token removed; 13-section list replaced by canon resolution | `B1-SFA-03`, `B1-SFA-04` | **REPAIRED** | COMPLETE |
| 1.10 | CF-E-30 | none | — | **CONFIRMED_NO_CHANGE** | COMPLETE |
| 1.11 | CF-E-40 | delta inherits the base's canon; no schema of its own | `B1-SFA-08` | **REPAIRED** | COMPLETE |

**Zero `glow-*` tokens remain across the eleven.** The CRD and Epic lanes stay
exact mirrors: 2 clauses each on the `-20` pair, 1 each on the `-10` pair, 1 each
on the `-40` pair.

### The replacement text

**Specification authors** (`CF-C-20`, `CF-E-20`), Execute step 2, identical but
for the class word:

> Resolve the CRD Specification format from the canon referenced for this change,
> through this prompt's PFCanon source contract below, and cite the exact canon
> and section resolved. Write one complete pending Specification in that format,
> covering every field that canon requires. The format is canon's and not this
> prompt's: a CRD Specification becomes a permanent governed record and must seat
> in the register that governs it. Do not author against an assumed structure, do
> not reuse a neighbouring artifact's schema token, and do not mint one. If that
> canon cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR` with the
> failed predicate and recovery owner rather than authoring against a guess.

**Kickoff preparers** (`CF-C-10`, `CF-E-10`) — the field list is retained and the
permission is stated rather than assumed:

> The kickoff is transient scaffolding between two stages and does not become a
> permanent governed record, so this prompt states its format and it carries no
> canon schema token. This does not extend to the Specification itself, whose
> format CF-C-20 resolves from canon.

**Delta authors** (`CF-C-40`, `CF-E-40`):

> The `SPECIFICATION_DELTA` format … is governed by the same canon that governs
> the base CRD Specification it modifies … A delta has no schema of its own: do
> not mint one and do not carry a schema version token.

### What pass 2 deliberately did not touch

- **No section was added, removed or reordered** beyond replacing the
  thirteen-section list with its canon-resolution clause in the two `-20` bodies.
- **The `-30` addendum field lists stand.** PF10 2.14 is silent on addendum
  structure and PF10 §8 returns that authority to permanent canon, which defines
  none. Recorded as `B1-OBS-02` where the prompts lack a drain transition.
- **`CF-PO-10`'s `CHANGE_CLASS_SELECTION` field list stands.** Not a Specification.
- **No `docs/pfcanon/` write.** `B1-OBS-01` and `B1-OBS-03` are canon defects
  this pass found and could not fix.

### Ordering fault, recorded

The six edits were made before PF10 2.14 was drained, inverting the correct
order — canon first, then prompts — and going beyond the instruction given. The
Product Owner elected to keep them. Between the edits and the drain the CRD and
Epic Specification lanes would have returned `SOURCE_RESOLUTION_ERROR`; after
the drain they resolve. No artifact was produced in that window.
