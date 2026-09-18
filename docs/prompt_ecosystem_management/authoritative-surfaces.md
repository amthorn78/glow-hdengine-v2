---
artifact_type: PROMPT_ECOSYSTEM_AUTHORITATIVE_SURFACES
artifact_version: "1.0"
created_date: 2026-09-18
status: BINDING
authority: Product Owner instruction, 2026-09-18
baseline: main @ 3c0b1fa (PR #415, squash-merged)
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
| Candidate release under repair | `GCFPE-20260914.1` / `091426.1` / **55 prompts** |
| Candidate selection status | `UNSELECTED_CANDIDATE` |
| Selected (live) release | `GCFPE-20260913.1` / `091326.2` / 54 — **never modified** |
| Repository baseline | `main` @ `3c0b1fa` |
| Graph proof token | `55 nodes · 227 edges · 55 state_routes · 571,479 bytes · sha256 021058dd…` |

The graph proof token is reproduced by building from the committed parts. A session that
builds and gets the same token has proved agreement; nothing needs a stored copy.

**How to rebuild — this is the whole procedure, do not go looking for it.**

```
python3 scripts/graph_parts.py build docs/graph/parts "$SCRATCH/graph.md"
```

`graph_parts.py` ships with the **`glow-graph-contract` skill**, not as a tracked file in this
repository. That is deliberate: reusable behaviour lives in skills, maintained data lives in
the repository. Verified working 2026-09-18, output:

```
build: 55 nodes, 227 edges, 55 state_routes
       embedded JSON 571479 bytes  sha256 021058ddf8795124c34a38d53ac9245b7718b1b9e095f02fb82fc4ef41102bb6
       validation PASS
```

Build to the scratchpad, never into `docs/graph/`. The assembled graph is derived output and is
never committed. **A session that cannot find the builder has not lost it — it is in the skill.**

## Repository — persistent authority

| Path | Role | Status |
|---|---|---|
| `docs/prompt_ecosystem_management/README.md` | Architecture of this directory; what belongs here and what does not; validation posture | Current |
| `docs/prompt_ecosystem_management/gcfpe.decision-record.md` | Product Owner rulings governing the ecosystem, with consequences. **Binding.** | Current |
| `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` | Approved machine-readable per-prompt contract registry, all 55 prompts, with `evidence_contract` byte count and SHA-256 per prompt | `APPROVED` 2026-09-17; evidence refreshed 2026-09-18 |
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
| Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | `3db4590a05eb81de9736ea69bac61016` | Operational mapping index: families, actors, artifacts, lifecycle, candidate topology |
| GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1 | `3dc4590a05eb81a9adf1d8f800863937` | The live repair plan and batch checklists |
| GCFPE Membership and Release Register | `3d24590a05eb81ce942ad994cfca9fa1` | **Sole selection authority.** Selection is resolved only here |
| Register entry — GCFPE-20260914.1 | `3db4590a05eb816f925ef3b0659de3b8` | Candidate register entry |
| Glow HDE Complete Prompt Set — 091426.1 | `3db4590a05eb81738ef1d846e3c0df8c` | The 55-member catalog |
| GCFPE Alpha Establishment and Change Management Checklist — 091426.1 | `3db4590a05eb812f87caed515836687f` | Alpha establishment items |
| GCFPE Repair Completion Checklist — 20260914.1 | `3db4590a05eb8104b04cc01ed90ec39f` | Completion criteria |
| Glow HDE Prompt Repair Plan (parent) | `3cb4590a05eb81bdaeb3e6a097f0a3a6` | Historical append-only receipt log. Read as history, not instruction |

Lane hubs: Change Flow `3db4590a05eb81d59059eb6b95ed5fcf` · IA `3db4590a05eb8195a2ccf7c0959a8b6e` ·
QA `3db4590a05eb814d96d3dcfa8835f96d` · Escalation `3db4590a05eb81cd938de84cfffead9c` ·
TW `3db4590a05eb811b9c14f2ae89c28df7`

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
