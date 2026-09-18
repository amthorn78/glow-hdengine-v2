---
artifact_type: GCFPE_CROSS_CUTTING_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-18
status: COMPLETE_AND_VERIFIED
release: GCFPE-20260914.1 / 091426.1 / 55
authority: Product Owner ruling D7; executed by PE31
baseline: main @ 3c0b1fa; branch docs/20260918-pe31-transition
---

# Drive → repository storage pass — repair report

The second cross-cutting repair of this candidate, after drainage removal. It applies
D7 to prompt behaviour: the repository is the storage and versioning authority, Notion
is the operational layer, and Google Drive is not a storage authority at all.

Executed and verified 2026-09-18. **No graph change and no change to the selected
release `091326.2`.**

## Result

| | |
|---|---|
| Prompts edited | **44 of 55** |
| Passages rewritten | **333** |
| Apply failures | **0** |
| Blind-readback verification | **44 / 44 clean** |
| Live byte-identical to expected post-state | **41 / 44** (3 explained in §5) |
| Registry entries recomputed | **44**; all 55 reproduce from source |

Every edited prompt now writes artifacts to `docs/ephemeral/` by repository path and
resolves PFCanon from `docs/pfcanon/`. Zero surviving occurrences of
`Glow / Core Docs / PFCanon`, `Glow / Ephemeral Planning Files`, `drive.google.com`,
`docs.google.com`, or `EPHEMERAL_DRIVE`.

**Preserved intact:** the single conditional sentence *"Google Drive is used only where
Nathan directs a specific file there."*; the Google Docs / `.doc` / `.docx` prohibition;
`SOURCE_RESOLUTION_ERROR` with its failed-predicate and recovery-owner payload; every
PF09 row, canon-conflict and ADR record, `NEW_CANON`, `CANON_RECONCILIATION`, and the
permanent Canon drainage target and owner.

## 1. Measured scope — and a correction to the inherited figure

| Measure | Succession record | Measured against live bodies |
|---|---|---|
| Name Drive as artifact destination | 44 | **44** — confirmed |
| Resolve PFCanon through Drive | 39 | **42** |
| Occurrences | 310 | **333** |

The partition is clean: **11 converted, 44 unconverted, 0 partially converted.** The 11
are `CF-C-10/20/30/40`, `CF-E-10/20/30/40`, `CF-PO-10`, `GCFPE-MGMT-10`, `MGR-10`, and
their wording was the convergence target. No new phrasing was invented.

**Discovery was got wrong once, by this session.** A first pass enumerated Drive
*phrasings* already seen and found 236 lines. Two classification workers independently
reported unassigned Drive lines inside their own prompts. Re-measuring by matching the
word and subtracting the one permitted sentence found **97 further occurrences across 38
of the 44 prompts** — a 29% undercount. The missed lines were the enforcement
counterparts of lines the first pass had already repaired (*"Use only the verified Drive
location…"*, *"…its complete Drive readback…"*). Applying the first pass alone would have
left twelve prompts instructing an agent to write to `docs/ephemeral/` and, two lines
later, to use only a verified Drive location.

This is the same failure the drainage repair recorded. **Measure by reading, not by
pattern, and treat a worker's out-of-scope observation as a signal about the scope.**

## 2. Method

Discovery was precomputed centrally so coverage was arithmetic. Four classification
workers each received an exact hit list (59 hits apiece), the settled rules, and the
target wording; a second pass covered the 97 missed lines, carrying the first pass's
proposals as fixed context so paragraphs stayed coherent. Every return was validated
centrally: membership exact, coverage complete, and **every `evidence_quote` matched
character-for-character against source** before acceptance.

The full edit was simulated against local copies and scanned before anything was
written to Notion.

## 3. Coordinator decisions applied under D7

Three passages could not be resolved by substitution. They were decided centrally and
applied uniformly rather than per prompt. These are implementation decisions under D7,
not new Product Owner rulings.

**`EPHEMERAL_DRIVE` is retired.** The destination-class token appeared once each in
`OPS-10/20/30`, `PR-10/20/30/40`, `QA-10` — one byte-identical sentence in all eight.
Under D7 the class it names no longer exists, and it overlapped its sibling
`REPOSITORY_CONTROLLED` in the adjacent sentence. Replaced by `REPOSITORY_CONTROLLED`
rather than renamed: the sibling already covers the case, and minting a replacement
would create a token nothing validates. It appears in no graph part and no registry
field, so retiring it touched prompt bodies only.

Four workers had handled this one shared token three different ways — two dropped it,
three kept it, three escalated. That is the D4 failure mode exactly: *several producers
using different values for one concept because nothing authoritative defined it.*

**`QA-10` line 55 and `QA-50` line 29 were rewritten, not deleted.** Both prohibited
using a repository file as PFCanon authority — written when Drive was authority, and
under D7 they forbade the correct behaviour. `QA-10`'s named `docs/pfcanon` explicitly.

They were narrowed rather than removed because **the hazard they guard is real and
present**: `audit/docdeltas/` contains `PF10_EPIC017_addendum.md`,
`PF12_EPIC017_registry_and_mirror.md`, `PF14_EPIC017_mechanics_and_CI.md` and
`PF19_EPIC017_evidence_CI_rails.md` — PF-named repository files that are not controlled
canon. `docs/pfcanon/` is now carved out as the authority; the prohibition still covers
every other repository file.

> **Open, not resolved here.** Those `audit/docdeltas/` files sit outside the four open
> paths and were not touched. A session resolving canon by filename search would find
> them. This needs a Product Owner decision at some point.

## 4. Scope boundaries confirmed by inspection

**The graph required no change.** The 55 per-prompt parts carry zero Drive signals.
`global.json` carries 11 Drive URLs, but they are `binding_scope:
REPAIR_BASELINE_EVIDENCE_ONLY_NOT_A_RUNTIME_CURRENT_PF10_ALIAS`, with a `runtime_rule`
stating the pins "never replace that lookup" — pinned historical captures with SHA-256.
**They are provenance, not storage authority, and must survive.** Interpret Drive
references by function, exactly as "drain" must be.

Graph parts cite only routing sections (`Required result and routing`, 264 citations),
never the storage or canon sections, so no `source_evidence` citation was invalidated.

The assembled graph still rebuilds from `docs/graph/parts/` to
**55 nodes · 227 edges · 55 state_routes · 571,493 bytes · sha256 `3b54d620…`**.

**Topology was not changed.** The 11 converted prompts consolidated storage and canon
into one section; the 44 keep them separate. This pass converged the *wording*, not the
structure. Restructuring 44 prompts exceeds what D7 requires and would invalidate
section-level citations for no architectural gain.

## 5. Verification, and two transcription defects it caught

Verification was isolated: workers fetched the live pages and saved them verbatim with
no sight of the expected text, the edit list, or the pre-edit corpus; comparison happened
centrally afterward. Per §7 of the execution model.

It caught two defects, **both in working artifacts, neither in Notion**:

1. **Quote flattening.** One readback worker transcribed curly quotation marks (U+201C /
   U+201D) as straight ASCII in three captures (`PR-40`, `QA-90`, `QA-100`). A direct
   fetch confirmed the live pages retained the curly characters. Re-read with mandatory
   programmatic extraction — file → Python → file, never through a model's hands — and
   all three reproduced exactly.
2. **Dropped content in the pre-edit corpus.** `ESC-40` and `PR-30` were each missing a
   whole line, and `CL-20` had one altered sentence, relative to live. Live Notion held
   the correct fuller text in every case; only the local copy was lossy.

Both would have passed a "looks right" review. Byte comparison caught them; worker
self-reports did not. **Where byte fidelity matters, extraction must be programmatic by
an exact documented slice, never retyped.**

Consequently the registry hashes were computed **only from live post-edit readbacks** —
never from the pre-edit corpus and never from the constructed expected state.

## 6. Registry refresh

All 44 edited entries recomputed; the 11 untouched keep their existing values. The
refresh **proves its extraction convention before writing**: it must reproduce the 11
untouched prompts' existing byte counts and hashes exactly, or it refuses to run. It
reproduced 11/11. All 55 resulting entries were then re-verified against source.

**Inherited drift found:** the registry's evidence was already stale for **29 of 55**
prompts before this pass. All five prompts carrying the renamed CL-20 title were in the
drifted set and none in the matching set, indicating the last refresh preceded those
title updates. The succession record described the evidence as current; against live
bodies it was current for 26. Corrected here.

## 7. What this pass did not touch

- Drainage and PF10 addendum lifecycle language — that repair is complete and separate.
- `HDE-EPIC040` material.
- The selected live release `GCFPE-20260913.1` / `091326.2`.
- `docs/pfcanon/`, which remains read-only.
- Prompt IDs, routing targets, receiver names, and handoff block structure.
