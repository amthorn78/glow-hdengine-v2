---
artifact_type: PROMPT_ECOSYSTEM_AUTHORITATIVE_SURFACES
artifact_version: "1.0"
created_date: 2026-09-18
status: BINDING
authority: Product Owner instruction, 2026-09-18; release baseline updated by decision D17, 2026-09-21; repository baseline and graph proof token updated 2026-09-23 after D23 (close-out of MODIFICATION-20260923-alpha-feedback-open-entries)
baseline: main @ aeb256e
---

# Authoritative surfaces

Where the persistent truth of this prompt ecosystem lives. A session should be able to
orient from this page alone, without reading a predecessor's transcript.

**Rule of precedence.** The repository is the persistent versioned authority. Notion is
the operational and indexing layer. Google Drive is not a storage authority for this
ecosystem. Where a Notion page and a repository document disagree about implementation,
the repository wins and the Notion page is the thing to correct.

## Release baseline

| Field | Value |
|---|---|
| **Selected (live) release** | `GCFPE-20260914.1` / `091426.1` / **55 prompts** |
| Selection status | `SELECTED` — promoted 2026-09-21 by Product Owner decision `D17` |
| Selection authority | The **GCFPE Membership and Release Register** in Notion, and nothing else. Every control page reads `REGISTER_CONTROLLED` and asserts no selection of its own |
| Predecessor | `GCFPE-20260913.1` / `091326.2` / 54 — superseded, **archived intact** (56 pages moved, never copied or rewritten) |
| Repository baseline | `main` @ `aeb256e` |
| Graph proof token | `55 nodes · 229 edges · 55 state_routes · 575,074 bytes · sha256 ae2bd159…`, as measured after `D23` |

The graph proof token is reproduced by building from the committed parts. A session that
builds and gets the same token has proved agreement; nothing needs a stored copy.

**How to rebuild — this is the whole procedure, do not go looking for it.**

```
python3 scripts/graph_parts.py build docs/graph/parts "$SCRATCH/graph.md"
```

`graph_parts.py` ships with the **`glow-graph-contract` skill**, not as a tracked file in this
repository. That is deliberate: reusable behaviour lives in skills, maintained data lives in
the repository. Verified working 2026-09-18, output, as measured before `D23`:

```
build: 55 nodes, 227 edges, 55 state_routes
       embedded JSON 569902 bytes  sha256 1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7
       validation PASS
```

Build to the scratchpad, never into `docs/graph/`. The assembled graph is derived output and is
never committed. **A session that cannot find the builder has not lost it — it is in the skill.**

## Repository — persistent authority

| Path | Role | Status |
|---|---|---|
| `docs/prompt_ecosystem_management/README.md` | Architecture of this directory; what belongs here and what does not; validation posture | Current |
| `docs/prompt_ecosystem_management/gcfpe.decision-record.md` | Product Owner rulings governing the ecosystem, with consequences. **Binding.** | Current |
| `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` | Approved machine-readable per-prompt contract registry, all 55 prompts. Its per-prompt `evidence_contract` and `source_snapshot` identities describe the bodies before `D23` (2026-09-23) and no longer identify them | `APPROVED` 2026-09-17; evidence refreshed 2026-09-18 |
| `docs/prompt_ecosystem_management/authoritative-surfaces.md` | This page | Current |
| `docs/prompt_ecosystem_management/pe-succession/` | Session succession records | Current |
| `docs/graph/parts/global.json` | Shared graph contract — boundary nodes, vocabularies, PF10 addendum contract | Current |
| `docs/graph/parts/prompts/*.json` | 55 per-prompt graph parts. **The graph source.** | Current |
| `docs/pfcanon/` | PF Canon, controlled Markdown, **read-only** | Authority for canon |
| `docs/ephemeral/` | Release-scoped run evidence, batch reports, ledgers | Working store |
| `ci/checks/classify_ci_changes.py` | CI lane sorter. Must know every documentation path `ci.yml` ignores | Current |
| `ci/checks/check_direct_db_contract.py` | Source contract scan. Must exclude documentation paths | Current |

### Skills that carry binding rules

| Skill | Role |
|---|---|
| `glow-write-boundary` | The only repository paths that may be written, and the prohibition on every other write |
| `glow-artifact-storage` | Where each artifact belongs and how it is authored |
| `glow-graph-contract` | Never hand-edit the graph; hold it as parts and rebuild by script |
| `glow-workspace-currency` | Open and close every task against the record, not conversation memory |
| `amthor-workspace-governance-audit` | Read-only prompt-ecosystem validation; the mechanism that covers material excluded from application CI |

## Notion — operational and indexing layer

| Page | ID | Role |
|---|---|---|
| Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | `3db4590a05eb81de9736ea69bac61016` | Operational mapping index: families, actors, artifacts, lifecycle, selected topology. `REGISTER_CONTROLLED` |
| GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1 | `3dc4590a05eb81a9adf1d8f800863937` | **Closed 2026-09-23** (Product Owner): historical repair plan and batch checklists. Parent of the live Alpha Feedback page |
| GCFPE Modification Backlog | `3e54590a05eb81eb818fd0f42045167a` | Created 2026-09-24 (Product Owner). Defects a maintenance run finds outside its Modification's frozen scope, each with a severity S1–S4; beside the Alpha Feedback list, which holds the Product Owner's own feedback and deferrals. Written by `GCFPE-MGMT-10` runs under the maintenance destination rule |
| GCFPE Membership and Release Register | `3d24590a05eb81ce942ad994cfca9fa1` | **Sole selection authority.** Selection is resolved only here |
| Register entry — GCFPE-20260914.1 | `3db4590a05eb816f925ef3b0659de3b8` | The promotion transaction and its archival receipt |
| Glow HDE Complete Prompt Set — 091426.1 | `3db4590a05eb81738ef1d846e3c0df8c` | The 55-member selected catalog. `REGISTER_CONTROLLED` |
| GCFPE Alpha Establishment and Change Management Checklist — 091426.1 | `3db4590a05eb812f87caed515836687f` | Alpha establishment items |
| GCFPE Repair Completion Checklist — 20260914.1 | `3db4590a05eb8104b04cc01ed90ec39f` | Completion criteria |
| Glow HDE Prompt Repair Plan (parent) | `3cb4590a05eb81bdaeb3e6a097f0a3a6` | Historical append-only receipt log. Read as history, not instruction |
| PE Metaprompt 091426.1 | `3db4590a05eb8174be35d9e35acb3f77` | Prompt-authoring control. `REGISTER_CONTROLLED` |
| 04 Archived Prompt Versions | `3c94590a05eb811cb145cd010e3b3fcf` | Where superseded prompts and controls are **moved** intact. Never a copy, never a rewrite |
| Glow HDE Prompt Flow Index (un-versioned) | `3cc4590a05eb8101b5ded32c12616eb6` | Historical index, and the **parent of the release register** — never archive it |

Lane hubs, all `091426.1` and all `REGISTER_CONTROLLED`: Change Flow `3db4590a05eb81d59059eb6b95ed5fcf` ·
IA `3db4590a05eb8195a2ccf7c0959a8b6e` · QA `3db4590a05eb814d96d3dcfa8835f96d` ·
Escalation `3db4590a05eb81cd938de84cfffead9c` · TW `3db4590a05eb811b9c14f2ae89c28df7`

**No page asserts its own selection.** Every control above reads `REGISTER_CONTROLLED` and carries
the register's URL plus the rule that it is operative if and only if the register selects this
release. The PE Metaprompt is the one exception: it is operative while the register binds it as the
selected release's prompt-authoring control, and when unchanged it is bound again in the next
release (`D23-G`, AF-012). If a page ever says `SELECTED` on its own, that is the defect, not the evidence.

**The 55 prompt bodies live in Notion and are authored and revised there in place.** They
are never mirrored into the repository. The repository holds their *contracts* (registry)
and their *machine-readable restatement* (graph parts), not their text.

## Not authoritative

| Thing | Why |
|---|---|
| Google Drive | Not a storage authority for this ecosystem. A file lives there only where Nathan directs that specific file |
| The assembled graph contract | Derived output. Built on demand to a scratchpad, represented downstream by its proof token, **never committed** |
| Any pre-merge report, ledger or plan copy | Superseded by the merged baseline. Dated records are history, not instruction |
| Conversation context from any prior session | Not a system of record. If it matters, it is written here |

## Stale-state sweep — 2026-09-22

The Product Owner found the **Epic Alpha Run Notes — 20260914.1** still reading
`ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR`, a day after `D18` resumed Alpha. A sweep for the
same literal across the workspace found it was not alone.

| surface | what it said | disposition |
|---|---|---|
| Epic Alpha Run Notes — 20260914.1 | `ALPHA_STOPPED_…`, `NOT_YET_APPROVED`, and frontmatter `status: UNSELECTED_CANDIDATE_DRAFT` / `promotion_authorized: false` | **corrected** — points at the Flow Index, frontmatter `REGISTER_CONTROLLED` |
| **HDE Change Flow Overview** | declared `GCFPE-20260913.1` / `091326.2` / **54** the current selection, Alpha stopped, and navigated to archived `091326.2` pages | **corrected** — worse than the reported page, and a top-level surface |
| ⛔ Epic Alpha Run Notes (predecessor) | first section not labelled historical, read as current | **bannered**, body untouched |
| ⛔ Alpha Establishment Checklist (predecessor) | "Current GCFPE contract maintenance — 091326.2" | **bannered**, body untouched |
| Membership and Release Register | correct | verified, unchanged |
| Glow Operations Hub | correct | verified, unchanged |

**The register and the hub were right; the navigation was wrong.** That is the more dangerous
arrangement of the two, because an agent reaches navigation first and has no reason to distrust it.

### The rule this establishes

**A release transaction is not complete until every page that *names* the release has been swept,
not only every page the transaction *touched*.** Promotion on 2026-09-21 updated ten bindings and
archived 56 pages, all read back — and still left a top-level navigation page asserting the
superseded release, because that page was not in the binding set and not a member.

Sweep by literal, not by inventory: search the workspace for the **predecessor's** release id,
version family and member count, and for every Alpha-state token. A page that restates state it
does not own is a defect even when the owning authority is correct.

### Restating is allowed; asserting is not

Several pages legitimately restate the Alpha state for convenience. Each must say, in the same
breath, that the Flow Index holds it and governs any disagreement. A heading that calls itself
"Sole operative Alpha state" on a page that is not the Flow Index is the defect — two pages made
that claim, and one of them was stale.

**Superseded for Alpha state, 2026-09-23 (`D18` successor).** No Notion page holds or restates the
Alpha state now. The Flow Index section *Alpha state — recorded in the repository, not here* points
to the Epic's artifacts under `docs/ephemeral/`, and the other pages point to that section. The
restating rule above still applies to other state.

Predecessor pages are **bannered, never rewritten**. Their bodies are dated evidence under
`AUTH-001`; the banner states what superseded them and points at the current authority.
