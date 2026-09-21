---
artifact_type: GCFPE_PROMOTION_AND_ARCHIVAL_RECORD
artifact_version: "1.0"
created_date: 2026-09-21
release: GCFPE-20260914.1 / 091426.1 / 55
predecessor: GCFPE-20260913.1 / 091326.2 / 54
authority: Nathan / Product Owner — "I approve promotion. Promote, document thoroughly, and move all predecessors to archive."
decision: D17
status: EXECUTED
---

# Promotion and archival record — GCFPE-20260914.1 / 091426.1 / 55

`GCFPE-20260914.1` / `091426.1` / **55** is the selected release as of 2026-09-21.
`GCFPE-20260913.1` / `091326.2` / 54 is superseded and archived intact.

## The three predicates, met before anything was written

| predicate | evidence | result |
|---|---|---|
| complete behaviour validation of the exact pinned snapshot | five installed gates; 55 of 55 bodies through the shipped validator; 831 registry assertions; 9 QA-closure + 17 artifact-timing fixture cases against live bodies | zero failures |
| independent governance post-flight, no mandatory unresolved finding | `docs/ephemeral/gcfpe.round27/POSTFLIGHT-REPORT-r27.md` | `PASS WITH WARNINGS` — **zero findings against the release**; all three warnings against controls and instruments |
| Product Owner approval of that exact snapshot | 2026-09-21, after reading the post-flight verdict | granted |

The §10 independent skill review had already returned `SKILL_FIT_CONFIRMED` for the installed
`change-flow` and `flowmaster-validate` bytes.

## Frozen identities, reproduced before the transaction began

| identity | value |
|---|---|
| `change-flow` | 21 files · `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` |
| `flowmaster-validate` | 29 files · `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` |
| direct-handoff contract | `1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` · 610549 bytes, byte-identical in both bundled copies |
| candidate graph contract | `1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7` · 569902 bytes, byte-identical in both bundled copies |
| graph proof token | 55 nodes · 227 edges · 55 state_routes |

Digest recipe: `docs/prompt_ecosystem_management/freeze.py`, rooted at the skill directory.
Zero `.pyc` in the synced directory before and after. Every run used `PYTHONDONTWRITEBYTECODE=1`
from a scratch copy; the synced directory was never written to.

## Transaction order — the safety property

The register entry specified the order and it was followed exactly. There is no cross-system
atomic rollback, so **the ordering is the control**:

1. **Every successor binding prepared, activated and read back.** Ten control pages moved to
   `status: REGISTER_CONTROLLED`.
2. **The stable selection register updated last.**
3. **Production validation rerun against the activated state.**
4. **Archival only after that.**

No write failed, none was ambiguous, and no receipt was inferred.

### The ten bindings

| binding | page id |
|---|---|
| Complete Prompt Set — 091426.1 (catalog) | `3db4590a05eb81738ef1d846e3c0df8c` |
| Prompt Flow Index — 091426.1 | `3db4590a05eb81de9736ea69bac61016` |
| Register entry — GCFPE-20260914.1 | `3db4590a05eb816f925ef3b0659de3b8` |
| PE Metaprompt 091426.1 | `3db4590a05eb8174be35d9e35acb3f77` |
| Alpha Establishment and Change Management Checklist — 091426.1 | `3db4590a05eb812f87caed515836687f` |
| Change Flow hub | `3db4590a05eb81d59059eb6b95ed5fcf` |
| IA hub | `3db4590a05eb8195a2ccf7c0959a8b6e` |
| QA hub | `3db4590a05eb814d96d3dcfa8835f96d` |
| Escalation hub | `3db4590a05eb81cd938de84cfffead9c` |
| TW hub | `3db4590a05eb811b9c14f2ae89c28df7` |

**No page asserts its own selection.** Each carries the register's URL and the rule that it is
operative if and only if the register selects this release. This follows the pattern already
designed in `GCFPE-20260914.1-Production-Activation-Delta-Manifest.md`
(`selection_authority.page_or_file_self_selection: false`), adopted as standing by `D17`.

## Production validation, rerun against the activated state

| gate | flag read by name | result |
|---|---|---|
| `validate_gcfpe_20260914.py change-flow --contract <C>` | `ok` | `true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py change-flow --contract <C>` | `fixture_suite_ok` | `true`, 155 cases, §13 33/33 and 28/28 variants |
| `validate_flowmaster.py` | `suite_ok` | `true` — `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current.py change-flow` | `ok` | `true`, `errors: []` |
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit + text | `PASS` |

`<C>` is the **direct-handoff** contract, not the graph contract. Passing the graph contract
raises `TypeError: 'NoneType' object is not iterable` at `validate_contract`, which reads as a
crash rather than as "wrong file" — recorded here so the next session does not diagnose it twice.

## Archival receipt — 56 of 56 moved intact

| what | count |
|---|---|
| `091326.2` member prompts | 54 |
| PE Metaprompt 091326.2 | 1 |
| Complete Prompt Set — 091326.2 (predecessor catalog) | 1 |
| **total** | **56** |

Destination: *04 Archived Prompt Versions*, `3c94590a05eb811cb145cd010e3b3fcf`, which now holds
298 child pages. All 56 IDs were confirmed present under the destination after the move.

**Moved, never copied.** A move preserves the page, its ID and its body; nothing was deleted,
overwritten or reconstructed.

The un-versioned *Glow HDE Prompt Flow Index* (`3cc4590a05eb8101b5ded32c12616eb6`) was
deliberately **not** moved: it is the parent of the stable register, and archiving it would have
carried the selection authority into the archive with it.

## What promotion did not change

Alpha remains `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR`. Selection is governance maintenance,
not Alpha execution. `HDE-EPIC040` PR01–PR03 remain accepted-final; PR04 has not started and its
PR-10 handoff remains `NOT_YET_APPROVED` until Nathan's manual decision. Merge and abort remain
Nathan-only actions.

## Open — the activation delta beyond the register

Promotion recorded the selection. It did **not** rewrite the `UNSELECTED_CANDIDATE` literals that
still sit inside the release's own content:

| where | occurrences | consequence of changing it |
|---|---|---|
| 55 prompt bodies — `Lifecycle: ``UNSELECTED_CANDIDATE``` | 55, one per body | edits bodies an independent post-flight was scoped to |
| `gcfpe-20260914.1-091426.1-direct-handoff-contract.json` | 173 | new skill bytes → new `SKILL_TREE_SHA256` → a fresh §10 review before install |
| `gcfpe-20260914.1-091426.1-candidate-graph-contract.json` | 57 | rebuilt from `docs/graph/parts/`, so regenerable by script |

Both contracts are bundled in **both** skills, so the file count is four.

This was left open deliberately. A promotion that silently edited 55 validated bodies and both
machine contracts would have voided the post-flight verdict that authorised it — *"a verdict is
scoped to exact bytes, and does not carry."* The predecessor release shows the intended end
state: `091326.2` bodies carry **no** lifecycle line at all, and the activation manifest's
intended value is `REGISTER_CONTROLLED`, not `SELECTED`.

Until it is done, a reader of any selected prompt sees `Lifecycle: UNSELECTED_CANDIDATE` while
the register says the release is selected. The register governs — that is the rule, and it is now
recorded in both places — but the contradiction is real and it is the Product Owner's call how to
close it.

## Corrections made while promoting

**The registry's `SELECTED_CATALOG` authority row pointed at the wrong catalog.** It declared
`version_family: '091426.1'` and `member_count: 55` while its URL resolved to
`3da4590a05eb81bcbc5deb2d2cec4f1f` — the **091326.2** catalog, which holds 54 members of a
different release. The identifiers were right and the URL was wrong. Corrected to
`3db4590a05eb81738ef1d846e3c0df8c` with the correction stated in place rather than silently
swapped.

**The pre-written activation manifest no longer matched the live pages.** Its anchors
(`mutation_posture: LOCAL_DRAFT_ONLY`, `Selection status: UNSELECTED_CANDIDATE`) were written
2026-09-14/15 and the pages moved since; live values were `LIVE_UNSELECTED_CANDIDATE` and
`Lifecycle: ``UNSELECTED_CANDIDATE```. Its **design** was adopted; its **anchors** were not
usable as written. It remains `posture: LOCAL_PREPARED_NOT_APPLIED`,
`external_mutation_performed: false`, which is still true of its prompt payloads.
