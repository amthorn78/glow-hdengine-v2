# 0\. Document Control \[Required-Now\]

## 0.1 Header

**Title:** PF12-Canon-HDE-Schemas-and-Artifacts

**Version:** v2.8.3

**Status:** Canon

**Effective date:** 2026-08-08

**Last Update Gate:** 080826 Doc Refresh 2

**Invocation tag:** INV-f2ac55d77ce9aacc

## 0.2 Scope & single homes \[Required-Now\]

### Supersession by HDE Build Notes addenda

Consult the complete latest active HDE Build Notes base version, whether it is one unlettered document or a complete verified lettered set. Documents in a lettered set are equally authoritative containers of independently scoped addenda. A later document letter supersedes nothing by itself. A higher-numbered addendum controls only overlapping scope or scope it explicitly supersedes; lower-numbered guidance remains authoritative for distinct scope. HDE Build Notes governs a PF12-owned point only when an active, non-superseded addendum explicitly addresses that point. When the complete active HDE Build Notes version is silent on the point, PF12 governs.

PF12 integrates applicable HDE Build Notes guidance and routes cross-document references by title only. Cite HDE Build Notes by addendum number and addendum title, not by document version, document letter, or section number.

### Ownership

This document is the single home for:

- Engine catalogs under `catalog/`, including the current catalog homes defined in §2.  
- The Freeze-Pack Manifest at `catalog/manifest.json`.  
- Checksum sidecars only for families whose owning contract explicitly requires one. A Freeze-Pack Manifest entry, Human Index/Mirror hash-and-size binding, or path-proof does not create an unstated sibling-sidecar requirement.  
- Closed domains and canonical artifact rules, including the Freeze-Pack Manifest to `release_id` contract.  
- Canonical JSON schemas and Evidence Catalog families for stateless or no-database BodyGraph exports, compatibility exports, and optional run-bundle aggregates under §8.13.

`CANON_CHECKSUMS.json` is deprecated. `catalog/manifest.json` is authoritative for frozen inputs and pack identity.

### Human Evidence Index

The canonical Human Evidence Index is `docs/evidence/INDEX.json`. It is a records-only pointer and metadata ledger; it does not contain governed payload bytes. Its canonical JSON, record shape, legacy-row treatment, and parity join are governed by §8.3.

Each current parity row binds at least `artifact_key` and `discovered_physical_path`. The exact allowed metadata remains governed by §8.3. The index MUST maintain 1:1 key/path parity with `artifacts/evidence_index.jsonl`.

`docs/evidence/INDEX.sha256` is the hash sentinel over the canonical bytes of `docs/evidence/INDEX.json`. Acceptance-token semantics remain owned by HDE-Governance.

### Historical minimal Human Index rows

An older governed evidence artifact MAY retain a Human Evidence Index row containing only key/path-style pointer data when that row predates the current richer evidence shape.

Such a row MAY support closed-task revalidation only when all of the following are true:

- The governed artifact bytes and path are unchanged.  
- The minimal row is not used by itself to support evidence regeneration, schema migration, a new acceptance claim, QA PASS, OPS completion, HDE Build Checklist status movement, closeout, or a runtime-behavior claim.  
- The Human Evidence Index preserves the expected key/path binding.  
- The Machine Evidence Mirror contains the matching artifact record with coherent `sha256`, `size_bytes`, and `proof_anchor` values.  
- `proof_anchor` identifies the matching sibling path-proof transcript.  
- The path-proof records the same governed path, hash, and size.  
- The revalidation artifact discloses the minimal-row caveat.

Do not downgrade a historical evidence family solely because an older Human Index row is minimal when the Machine Mirror record and sibling path-proof provide coherent path, hash, size, and proof-anchor linkage. Treat that condition as a historical evidence-shape caveat unless a later PO-governed migration requires richer historical rows.

If artifact bytes or paths change, the family is regenerated, a new acceptance claim is made, or a migration changes the Human Index shape, the current Human Index, Machine Mirror, hash-sentinel, and path-proof rules apply in full.

### Machine Evidence Mirror

The canonical Machine Evidence Mirror is `artifacts/evidence_index.jsonl`. It is a governed, records-only JSONL artifact. §8.3 is the single home for its complete schema, optional metadata extension, ordering, self-record, timestamp, parity, and path-proof rules.

Every non-self record MUST bind the referenced artifact through `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor`. Unknown keys outside the §8.3 extension are rejected. Every present key is serialized in ASCII order, records are sorted by `(artifact_key, discovered_physical_path)`, and each record has exactly one terminating LF.

Each governed artifact has a sibling `<artifact-path>.path_proof.txt` transcript unless its owning family expressly defines another PF12-governed companion relationship. `proof_anchor` MUST point to the governed companion. `artifacts/evidence_index.jsonl` is the only Machine Mirror path.

### Dual-home layouts

The Evidence Catalog defines governed payload paths, normally under `audit/` or `artifacts/`. Human-facing navigation under `docs/` MAY point to those paths but MUST NOT create a surrogate payload home.

- Governed payload bytes remain at their Evidence Catalog paths.  
- A `docs/` pointer or index MAY reference governed bytes by repository-relative path.  
- A derived rendering or records-only catalog under `docs/` MUST state whether it is authoritative or points to another authoritative path and MUST be updated with the governed source when its owning contract requires synchronized change.  
- `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` are a paired pointer-ledger surface and MUST maintain strict parity.  
- A truth-like root is non-authoritative unless PF12 or another owning canon explicitly catalogs its artifact family.

Evidence may span multiple governed roots. Single-home means that the Human Evidence Index and Machine Evidence Mirror provide the authoritative artifact-key/path bindings and that each governed artifact has the required companion proof. Root count alone does not establish drift. A root becomes drift when it is treated as an independent authority outside the Evidence Catalog, Human Index, Machine Mirror, and path-proof contract.

`tools/` and `scripts/` are code and tooling roots by default. Their outputs are non-governed unless an owning Evidence Catalog entry expressly promotes them and binds them through the normal evidence discipline. Test fixtures and snapshots are governed evidence only when an owning PF section or Evidence Catalog family explicitly catalogs their path family.

### External evidence-package caveats

An external closeout package, uploaded archive, rendered-deliverables package, zip manifest, or review-package listing is not a PF12 evidence home unless PF12 catalogs the package and binds it through the Human Index, Machine Mirror, hash, and path-proof rules.

A zero-byte, missing, unreadable, or malformed package copy MAY be recorded as an evidence-package caveat instead of a PF12 evidence failure only when all of the following are true:

- The owning QA, closeout, or HDE Build Notes record explicitly records the caveat.  
- Current governed repository evidence supplies the same proof target.  
- The governed artifact is non-empty unless its family permits a cataloged sentinel.  
- The governed artifact has every required Human Index, Machine Mirror, hash, and sibling path-proof binding.  
- The caveat does not conceal a missing QA step, required deliverable, unresolved behavior or tooling failure, tooling blocker, missing close-gate artifact, or untrusted evidence source.

The caveat MUST NOT make the package authoritative, bypass a governed non-empty requirement, create another evidence home, or replace the Human Index, Machine Mirror, hash sentinel, or path-proof. A package promoted as evidence becomes an explicit governed family and is subject to the same rules as any other governed artifact.

### Mirror self-record semantics

Normative Machine Evidence Mirror self-record construction, hash, size, path-proof, canonical-path, and validation semantics are defined once in §8.3. Implementations, validators, and regression tests MUST use that section. This Document Control section does not restate a parallel rule set.

### Evidence-schema validation dependencies

Evidence tooling that validates governed JSON against JSON Schema MUST use one of these postures:

- Declare the validation dependency as required and ensure the applicable CI environment installs it.  
- Treat the dependency as optional and skip cleanly with an explicit reason when it is unavailable.

A schema-validation test MUST reflect the selected posture. It MUST NOT fail solely because an optional dependency is unavailable unless current canon declares that dependency required.

### Governed locations and operational summaries

Governed evidence MUST use a cataloged repository-relative path. A transient generator path such as `codex/out/` is not authoritative and MUST NOT be indexed.

Bounded OPS discovery and open-rails evidence MAY be promoted only as a text-first artifact under a governed root. It MAY record key names, provider or environment labels, endpoint or route-family labels, credential-binding names, base-URL posture, account or tier posture, authorization and task identity, safe status or error classes, redacted excerpts when approved, decisions, and bounded non-secret outcomes. It MUST NOT record raw secrets, bearer tokens, API keys, database passwords, uncontrolled production data, or private payload bodies.

Open-rails evidence MUST NOT establish QA PASS, checklist status movement, epic closure, public Reader expansion, new public routes, new acceptance tokens, or broad runtime conformance unless the owning canon and separately governed evidence support that claim. Candidate evidence is non-authoritative until its exact path is indexed, mirrored, and path-proved.

### Directory naming

Repository and application directory names MUST use lower-case ASCII. This rule applies to directory segments under governed roots, including `artifacts/`, `docs/`, `audit/`, `catalog/`, and `schemas/`.

The rule does not independently constrain filenames. An uppercase character in a canon-defined close-pack filename is not directory-case drift when every directory segment is lower-case and the filename satisfies its owning pattern.

Evaluate path identity from raw repository bytes, governed records, or canonical bindings. Rendering escapes in chat, Markdown, previews, or review prose are not source defects. A claimed escape-character blocker MUST identify the raw source, the read-only inspection method, the exact raw line, the identity or semantic change, and why the character is not display-layer escaping. Without that source-level proof, the blocker is invalid.

A governed directory rename requires synchronized updates to every affected Human Index row, hash sentinel, Machine Mirror row, and path-proof under §§8.3 and 8.6.

### Evidence bundles and manifests

A governed evidence family MAY use a textual JSON or JSONL bundle instead of many separately governed member files. Each bundle has a textual manifest that records, for every logical member, at least a logical identity or `artifact_key`, lowercase 64-hex `sha256`, and `size_bytes`, plus any descriptors required by its owning schema.

The bundle and manifest are separate governed artifacts. Each receives its own Human Index row, Machine Mirror row, and path-proof. Internal members MAY remain manifest-addressed instead of receiving separate ledger rows when the family contract so specifies. A bundle or its manifest MUST NOT include itself as a logical member.

Evidence used for agent-evaluated acceptance remains inspectable through text artifacts, including the Human Index, Machine Mirror, bundle manifests, and required QA logs. Binary or compressed files MAY be supplementary but MUST NOT be the sole governed proof for such acceptance.

### HDE-EPIC020 Candidate 1 transition

The HDE-EPIC020 Candidate 1 bundle producer MUST accept both structured artifact entries and legacy path-string entries from `docs/acceptance_map_epic020.json` without requiring the acceptance map to be rewritten.

For a legacy string entry, the producer MAY infer transitional logical keys from the token and path. This exception is limited to HDE-EPIC020 Candidate 1\. Canonical artifact and bundle identities remain governed by PF12 and may be pinned by a later Doc-Delta.

Bundle generation MUST exclude its own bundle and manifest outputs from membership even when those paths appear in an acceptance map. Membership is restricted to underlying evidence files. This prevents self-reference and does not authorize bundles to contain themselves or other governed bundle outputs.

### Evidence Catalog

§8.3 and §8.6 together form the Evidence Catalog and are the single home for governed evidence families, record shapes, and artifact paths. Other PF documents reference those families by name and MUST NOT maintain parallel path lists. HDE-Phased Epics is historical and planning context; it MUST NOT define current evidence paths, evidence shapes, or remediation predicate targets.

### HDE Build Checklist accountability

Task-like future PF12 work involving evidence families, artifact gaps, ledger or path-proof gaps, schema gaps, evidence-loop gaps, governed-output remediation, implementation, QA, OPS, runtime, vendor, architecture, or product behavior MUST resolve to exactly one of:

- A mapped phased HDE Build Checklist task or subtask.  
- A phased HDE Build Checklist gap.  
- Work outside the phased HDE build scope.  
- Documentation or status drainage only.

When both a relevant parent and subtask exist, use the subtask. PF12 does not create checklist rows, assign checklist status, or transform an evidence note into an implementation obligation.

### Planning observations

A read-only repository audit MAY identify existing governed artifacts, evidence helpers, ledger files, path-proofs, and candidate loci for planning. That observation is planning input only. It does not replace a governed artifact, ledger row, path-proof, QA artifact, OPS completion record, acceptance proof, checklist status, or closeout record. Later work relying on the observation MUST verify the locus at its pinned repository state and bind any promoted artifact through PF12.

### Routing and process ownership

Scoring, thresholds, deterministic preimage arithmetic, Reader and CLI transport bytes, vendor shaping, architecture boundaries, and governance-token semantics are routed by title to HDE-Math-Spec, HDE-CLI-API-Vendor-Ref, HDE Architecture, and HDE-Governance. PF12 does not restate their owned bytes.

HDE-Governance owns the Token Registry and acceptance-token semantics. PF12 binds token names to artifact families and paths through names-only acceptance hints. The phased HDE Build Checklist consumes established token names and does not create them.

Epic-Process-Guide owns PR workflow. PF12 defines which catalogs, manifests, ledgers, proofs, and companions must remain synchronized, not the mechanics for managing the PR.

### Magic-10 seed metadata

`catalog/magic10_seeds.json` is the governed Magic-10 seed-metadata catalog under §2.7. It is a frozen input. A byte change requires the release-identity and evidence treatment defined by §§5–6 and 8\.

## 0.3 Tagging

Section labels distinguish contract state:

- `[Implemented]` means the named behavior is verified in repository bytes and enforced by the referenced current validation surface.  
- `[Required-Now]` means the contract is required for the current build or release discipline; the label does not by itself claim repository conformance.  
- `[Future-Promotion]` means design intent is retained but excluded from current implementation, manifest, validation, or acceptance scope until promoted by Doc-Delta.  
- `[Speculative]` means a proposal is retained for later review and is not an accepted current contract.  
- `[OPEN]` identifies an unresolved decision or toggle awaiting the named decision path.  
- `[Tracking]` identifies a status ledger that may contain both resolved and open entries.

## 0.4 Change policy \[Required-Now\]

### Single homes

PF12 owns:

- The catalogs named under §2.  
- The Freeze-Pack Manifest at `catalog/manifest.json`.  
- Checksum sidecars only for families whose owning contract expressly requires one.  
- The schema, artifact, Evidence Catalog, and release-identity contracts assigned to PF12.

Bytes owned elsewhere are routed by title and are not restated here:

- HDE-Math-Spec owns scoring, thresholds, deterministic preimage, and idempotence arithmetic.  
- HDE Architecture owns architecture boundaries and single-home routing.  
- HDE-CLI-API-Vendor-Ref owns transport and vendor shaping.  
- HDE-Governance owns acceptance gates, token semantics, and Reader transport policy.

### Doc-Delta triggers

A Doc-Delta is required for a change to:

- A current catalog closed domain, identity, enum, or normative order.  
- A catalog schema or executable validation contract.  
- Canonical JSON serialization rules.  
- `catalog/manifest.json` structure, path semantics, or entries.  
- A frozen input, including the order in `catalog/magic10.json`, caps in `catalog/magic10_caps.json`, topology bytes in `catalog/gates_v1.json` and `catalog/channels_v1.json`, seed metadata in `catalog/magic10_seeds.json`, threshold inputs in `math/thresholds.json`, and the narratives inputs governed by §2.8.  
- The Machine Evidence Mirror path, required or optional record schema, parity rule, timestamp semantics, self-record semantics, or path-proof relationship.  
- Promotion of an Authorities, Profiles, Presets, enriched UMS, full-ten seed, governed seed-body, or hash-only/index-only evidence surface from Future-Promotion into the current contract.

Each Doc-Delta states its scope, targets, acceptance impact, evidence updates, and release-identity impact.

### Governed records-only artifacts

Governed records-only families under §8 include:

- `docs/ENDPOINTS_CATALOG.json` and its explicitly required checksum.  
- `artifacts/proofs/reader_success_get_head_304.json`.  
- Historical bridge-era runtime records, including `artifacts/runtime/env_connectivity.snapshot.json`, only under the historical nonclaims defined by §8.7.  
- CLI parity, help, and installability families cataloged under §8.6.  
- `/internal/version` proof families cataloged under §8.6.  
- Registry report, database fingerprint, start-command capture, environment inventory, and validator-output families cataloged under §8.6.  
- BodyGraph release bindings, refresh policy, metrics, and sanitized keys-only sample families cataloged under §8.6.

This list routes families to §8; §8.6 remains the authoritative artifact-key/path catalog.

### Synchronized evidence updates

When a governed artifact, snapshot, script, or path changes, update every affected surface in the same change:

- `docs/evidence/INDEX.json`.  
- `docs/evidence/INDEX.sha256`.  
- `artifacts/evidence_index.jsonl`.  
- `artifacts/evidence_index.jsonl.sha256` when required by the Machine Mirror family.  
- Every affected sibling path-proof.

Add the applicable change record and Doc-Delta hook under §9. Epic-Process-Guide owns the PR procedure.

### Release identity

A byte-level change to a manifest-listed frozen input or to the canonical bytes of `catalog/manifest.json` MUST produce a new `release_id` and record it in the Doc-Delta. The narratives pack manifest and its governed members are frozen inputs under §2.8. `catalog/magic10_seeds.json` is also a frozen input.

An editorial rearrangement that changes no governed catalog, schema, canonical-byte rule, artifact identity, or normative contract does not require a Doc-Delta. A normative change does.

### Required enforcement behavior

The applicable validation workflow MUST fail when:

- A catalog fails its schema or closed-domain contract.  
- A governed JSON artifact fails its canonical-byte contract.  
- A required Human Index, Machine Mirror, sentinel, checksum, or path-proof update is absent or incoherent.  
- A Machine Mirror record violates its required/optional key set, canonical JSONL form, ASCII key order, record sort order, final-LF rule, path-proof relationship, or single-file rule.  
- An explicitly required family checksum sidecar is missing or invalid.  
- `docs/evidence/INDEX.sha256` does not match the canonical Human Index bytes.  
- `artifacts/runtime/env_matrix.snapshot.json` is missing or invalid where its schema-v3 singleton contract applies.

This subsection defines required behavior, not current workflow, test, deployment, or PASS state.

## 0.5 Tracked decisions \[Tracking\]

This section records tracked decisions and their current status. Entries marked `[OPEN]` require confirmation from the named owner; entries marked `RESOLVED` record confirmed decisions. Changes affecting frozen inputs, schemas, closed domains, canonical bytes, or current/future scope require the applicable Doc-Delta.

### CH-PRIMARY

- Status: RESOLVED (current repository)  
- Decision: The canonical Human Design Channel Catalog is `catalog/channels_v1.json`; its owning schema is `schemas/channels_v1.schema.json`. `catalog/channels_catalog_v1.json` is an unrelated generic catalog and MUST NOT be substituted.  
- Owner: Isis  
- Severity: critical  
- Affects: §§2.1, 3.2, 5, 6, 8.1–8.2  
- Next: Synchronize current references, validators, tests, manifest entries, and evidence to `catalog/channels_v1.json`. Preserve an earlier path only when it is explicitly historical.

### CHANNEL-IDENTITY

- Status: RESOLVED  
- Decision: `channel_id` is `NN-NN`, with two distinct Gates zero-padded to `01..64` and ordered min-first. Collections of Channel IDs treated as sets are deduplicated and ASCII-sorted by `channel_id`.  
- Owner: Isis  
- Severity: high  
- Affects: §§2.1, 3.2.1, 4.2  
- Next: Enforce the identity, distinctness, membership, and ordering contract in the owning schemas, executable validation, and tests.

### CHECKSUMS-NAMING

- Status: RESOLVED (family-specific sidecars)  
- Decision: `catalog/manifest.json` is the Freeze-Pack checksum ledger; each entry binds exact path, hash, and size. A sibling `.sha256` is required only when the owning family explicitly says so. Narratives retain their HDE-Narratives-Guide-required sidecars; the Human Index sentinel and Machine Mirror checksum retain their named homes. No blanket sidecar is inferred for every catalog, schema, manifest member, or registry report.  
- Owner: Isis  
- Severity: high  
- Affects: §§1.1, 2.8, 5–6, 8.3–8.6  
- Next: Validate every expressly required sidecar and remove only false blanket wording. Do not remove an existing family-owned sidecar.

### MAGIC10-HOME

- Status: RESOLVED (split current homes)  
- Decision: Closed Magic-10 IDs and frozen order live in `catalog/magic10.json`; per-category input lists and inclusive caps live in `catalog/magic10_caps.json`; clamp, band-edge, rounding, and version inputs live in `math/thresholds.json`; seed metadata lives in `catalog/magic10_seeds.json`. No consumer or future Presets catalog may embed an alternate copy.  
- Owner: Isis  
- Severity: high  
- Affects: §§2.3–2.7, 6.1, 8.14–8.15  
- Next: Remove the conflicting hard-coded order in `engine/compat/categories.py` by deriving it from the canonical registry/order home, then refresh affected tests and evidence.

### PACK-ROOT

- Status: RESOLVED (current repository-relative path model)  
- Decision: `catalog/manifest.json` is stored under `catalog/`. Its exact `root` value remains `"catalog/"` as the current pack-namespace label, but every `files[].path` is a repository-relative POSIX path and catalog entries retain the `catalog/` prefix. Current release tooling resolves each entry from the repository root. PF12 MUST NOT describe `root` as the path-resolution base.  
- Owner: Isis  
- Severity: critical  
- Affects: §§5.1–5.3, 6.1–6.4  
- Next: Align §§5–6, manifest validation, and tests to the current model. A future operative path-base or field-name change requires a versioned manifest migration and Doc-Delta.

### SELF-LISTING

- Status: RESOLVED  
- Decision: `catalog/manifest.json` MUST NOT list itself in `files`.  
- Owner: Isis  
- Severity: low  
- Affects: §§5.2, 5.3, 6.1  
- Next: Keep manifest entries limited to governed frozen inputs and validate the finalized manifest as a governed canonical artifact.

### AUTH-PROFILES-USAGE

- Status: RESOLVED (excluded from current v1 catalogs; Future-Promotion retained)  
- Decision: No separate Authorities or Profiles catalog is present or consumed by the current engine. These domains are outside current catalog-validation and Freeze-Pack scope. The Human Design concepts remain reserved for governed Future-Promotion under §2.2.  
- Owner: Isis  
- Severity: medium  
- Affects: §§2.2, 3.3, 8.1–8.2  
- Next: Introduce either catalog only with a governed path, schema or executable validator, consumer, manifest treatment, tests, evidence, and Doc-Delta in the same change.

### ID-CHARSET

- Status: RESOLVED  
- Decision: Simple catalog IDs use `^[a-z0-9_]+$`, case-sensitive. Schema-defined composite IDs are explicit exceptions and MUST match their owning canonical projection; `channel_id` uses the `NN-NN` projection in §3.2.1.  
- Owner: Isis  
- Severity: medium  
- Affects: §3.3 and owning schemas  
- Next: Enforce each simple or composite identity through its owning schema and executable validation.

### PATH-CHARSET

- Status: RESOLVED  
- Decision: Manifest paths are repository-relative POSIX paths, case-sensitive, no more than 256 bytes, with no absolute form, backslash, `..`, `.`, empty segment, or doubled separator.  
- Owner: Isis  
- Severity: low  
- Affects: §5.1  
- Next: Enforce the path contract before resolving or opening a manifest member.

### SCHEMA-DRAFT

- Status: RESOLVED (current and future boundaries)  
- Decision: Catalog schemas use JSON Schema 2020-12. Current topology schema homes are `schemas/gates_v1.schema.json` and `schemas/channels_v1.schema.json`; both require stable repository-path `$id` values in the refresh change. Archived `schemas/ums.*` drafts are reference-only and are not current validators. A future enriched UMS schema requires a Doc-Delta and synchronized loader, test, manifest, and evidence changes.  
- Owner: Isis  
- Severity: medium  
- Affects: §§2.1, 3.1, 8.1 and Appendix A  
- Next: Add stable `$id` values to the two current schemas and prove that they validate the current catalog bytes. Preserve future UMS intent in the designated reference-only archive.

### ALIASES-POLICY

- Status: RESOLVED  
- Decision: Aliases are input-only and must be explicitly governed. Canonical outputs use canonical Center, planet, line, and other domain IDs.  
- Owner: Isis  
- Severity: medium  
- Affects: §3.3 and request rules in HDE-CLI-API-Vendor-Ref  
- Next: Keep alias input handling synchronized with the canonical domain and fail closed outside the allow-list.

### SERIALIZATION-SCOPE

- Status: RESOLVED  
- Decision: Canonical JSON rules apply to governed JSON artifacts in PF12 scope. Operational text logs remain subject to their owning format and keys-only rules and are not required to be canonical JSON.  
- Owner: Isis  
- Severity: low  
- Affects: §§4–5  
- Next: None; §4 owns the current distinction.

### EVIDENCE-PATHS

- Status: RESOLVED (updated)  
- Decision: The only Machine Evidence Mirror path is `artifacts/evidence_index.jsonl`. It is records-only, canonical JSONL, paired 1:1 with the Human Evidence Index by `artifact_key` and `discovered_physical_path`, and bound to sibling path-proofs.  
- Owner: audit  
- Severity: low  
- Affects: §§4, 8.3, 8.6  
- Next: Enforce canonical form, key/path parity, companion linkage, and the single-file rule.

### MTIME-UTC-SEMANTICS

- Status: RESOLVED (updated)  
- Decision: `mtime_utc` in a governed path-proof is capture-time provenance encoded as a valid UTC ISO-8601 timestamp. Portable validity is determined by the governed path, SHA-256, size, required companion fields, canonical field structure, timestamp shape, and linkage. A later checkout's filesystem mtime is not evidence and MUST NOT be compared with `mtime_utc`. An unchanged valid proof MUST NOT be rewritten or re-timestamped merely to make a clone, cache restore, or CI checkout pass. `produced_at_utc` remains the logical evidence-production timestamp.  
- Owner: Isis  
- Severity: medium  
- Affects: §8.3, Glow QA Guide, HDE Build Notes, evidence tooling, and tests  
- Next: Any semantic change requires a PF12 Doc-Delta and synchronized updates to Glow QA Guide, HDE Build Notes, `tools/evidence/update_evidence_index.py`, `ci/checks/check_mirror_schema.sh`, and relevant tests.

### MIRROR-RECORD-SCHEMA

- Status: RESOLVED (updated)  
- Decision: Required Mirror keys are `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor`. Optional metadata is limited to the §8.3 extension. All other keys are rejected.  
- Owner: audit  
- Severity: low  
- Affects: §8.3  
- Next: Validate required and optional keys, canonical serialization, and the Human Index join by `artifact_key` and `discovered_physical_path`.

### SEEDS-CATALOGIZE

- Status: RESOLVED (current subset semantics; full-ten Future-Promotion)  
- Decision: `catalog/magic10_seeds.json` is a manifest-listed metadata map whose keys are a subset of the closed Magic-10 set. Current rows are `harmony` and `heat`; the implemented row shape has no `admin_only` field. Unknown category keys fail closed. Full-ten coverage or governed seed-body bytes require a future Doc-Delta and implementation migration.  
- Owner: Isis  
- Severity: medium  
- Affects: §§2.7, 3, 6, 8.14–8.15 and Appendix C  
- Next: Enforce exact row keys, UTC timestamp shape, lowercase-64-hex checksum shape, canonical bytes, and subset closure. Do not invent eight rows or an `admin_only` field.

### EVIDENCE-BUNDLES-HASH-MODELS

- Status: RESOLVED for current architecture; Candidate 4 retained as Future-Promotion  
- Decision: Candidate 1, governed on-disk textual bundles plus textual manifests, is the current baseline. Each governed bundle and manifest remains subject to the applicable Human Index, Machine Mirror, explicitly required checksum, and path-proof rules. Hash-only or index-only families with absent governed payloads are not currently permitted.  
- Owner: audit  
- Severity: medium  
- Affects: §8.3, HDE-Mechanics Guide evidence tooling, phased HDE Build Checklist evidence gates, Glow QA Guide, and Reality Audits  
- Next: Candidate 4 remains a future design track. Promotion requires a Doc-Delta that reconciles path-proof semantics, Mirror schema, dependent canon, migration, and validation before implementation.

* 

# 1\. Purpose & Single-Home Rule \[Required-Now\]

## 1.1 What lives here

This document is the single home for the engine’s pack inputs and pack artifacts.

Closed catalogs (IDs, enums). Canonical lists and enums used by the engine (e.g., centers, gates, channels, Magic-10 category IDs, viewer-preference keys). Catalogs MUST be schema-validated, closed-domain, and locale-neutral.

Artifact serialization policy. Canonical JSON for all pack files: UTF-8, ASCII-sorted keys, compact separators (,/:), exactly one LF, no BOM/ANSI. Arrays treated as sets are deduped then ASCII-sorted; value conflicts fail-closed.

Freeze-Pack Manifest (single home). The authoritative manifest lives at catalog/manifest.json.

Entry shape (normative): each item contains exactly three fields: `path` (a repository-relative POSIX path string), `sha256` (a lowercase 64-hex digest of the file’s exact governed on-disk bytes after its format-specific validation passes), and `size` (the non-negative integer byte length of those same exact bytes).

Sidecars. Governed files carry sibling `.sha256` sidecars only where the owning artifact family explicitly requires them. Otherwise the manifest, Index/Mirror, and path-proof hash-and-size bindings remain authoritative without inventing a sidecar.

Release identity: release\_id \= sha256(canonical\_manifest\_bytes) (lowercase 64-hex). Any byte change to frozen inputs or to the manifest’s canonical bytes requires a new release\_id.

Deprecation note: CANON\_CHECKSUMS.json is deprecated; use catalog/manifest.json.

Stateless QA export artifacts (no-DB mode).

PF12 also governs the schemas and Evidence Catalog families for stateless QA exports produced directly by the engine and CLI from birth data or vendor JSON, without requiring database user records:

BodyGraph export JSON — a canonical JSON object that records:

- raw birth inputs used for the computation (date, time, location as normalized fields)  
- the resolved BodyGraph topology (centers, gates, channels, profile, authority, definition, type) as IDs and structures only  
- any internal registry IDs required for downstream compat or narratives

It MUST NOT embed app-level user identifiers or database primary keys. It is a pure engine result over frozen catalogs and math inputs (titles-only to HDE-Math-Spec and HDE-Schemas & Artifacts).

Compat export JSON (stateless mode) — a canonical JSON object that records compat results computed either from two BodyGraph export files or two birth tuples:

- the pair of inputs (referenced by birth data and/or BodyGraph export identity)  
- the internal compat result (closed Magic-10 IDs and bands only; numbers remain admin/internal)  
- the Reader v1 public envelope (six-key object per PF01/PF05) as a nested structure for parity checks

This artifact is a QA/admin surface only; it remains numeric-free at the public Reader layer.

Optional “run bundle” JSON — a composite QA artifact that aggregates, for a single compat run:

- the originating birth inputs or vendor JSON  
- the resulting BodyGraph export JSON for each chart  
- the compat export JSON for the pair

It exists to support reproducible QA runs and audits; concrete schema and usage live under §8.x Evidence Catalog.

All three stateless QA artifact types MUST follow the canonical JSON policy defined in this document (UTF-8, sorted keys, compact separators, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted) and MUST be admissible to the Evidence Index/Mirror under governed paths (artifacts/**, audit/**) when used as part of QA. They are not public app payloads; transport bytes and CLI flags live in HDE-CLI-API-Vendor-Ref and HDE-Governance (titles-only).

By design, math arithmetic (scoring, thresholds, preimage recipe) and transport bytes (Reader/CLI/vendor) are not duplicated here and are referenced by title only in their owning documents.

## 1.2 Titles-only routing \[Required-Now\]

Artifact binding rules (paths-of-record; normative)

PF12 is the single home for governed artifact families and their canonical paths-of-record. Plans and acceptance artifacts MUST bind to these canonical surfaces and MUST NOT invent alternates.

**Authority order (explicit; titles-only).**

1. HDE-Schemas and Artifacts is the source of truth for canonical artifact paths and sibling `.path_proof.txt` transcript naming for governed evidence families.  
2. HDE-Mechanics Guide may define how artifacts are generated or validated, but MUST NOT introduce alternate canonical paths that conflict with PF12.  
3. Glow QA Guide defines check execution semantics and status reporting posture, but does not override PF12 canonical paths-of-record.  
4. HDE-Build Checklist defines which checks are required for closure, but required checks MUST bind to PF12 canonical surfaces when a PF12-governed family exists.

**Evidence path binding authority order (artifact sources; normative).**

Authority order: repo manifests → audit manifests → rendered reports → QA Plan.

When multiple sources disagree on the bound path for a required artifact, the higher-authority source wins and the mismatch is treated as drift to remediate, not a license to invent alternate paths.

Guard proofs are evidence-only by default (promotion discipline)

Guard proof artifacts MAY be required deliverables, but they do not create new acceptance token obligations.

If a guard proof artifact is used for closure wiring (for example referenced by an acceptance map, token↔evidence matrix, or close-pack), it MUST be treated as governed evidence like other PF12 families:

- stable path under governed roots  
- updated in the Human Evidence Index and Machine Evidence Mirror in the same PR when bytes change  
- sibling \*.path\_proof.txt transcripts when required by the Evidence Catalog posture

Canonical JSON gate artifacts (primary family plus legacy coexistence)

Canonical JSON gate artifacts MUST use the canonical family under: audit/gates/json\_gate/canonical/

Canonical family (authoritative):

- audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson (required)  
    
- audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson (required)  
    
- audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json (optional by default; may be required by an explicit plan)

Legacy family (produced and evidence-indexed; non-authoritative for new bindings):

- audit/gates/canonical\_json/canonical\_json.gate.json  
    
- audit/gates/canonical\_json/canonical\_json.gate.json.path\_proof.txt  
    
- audit/gates/canonical\_json\_gate.json (optional legacy single-file canonical JSON gate summary referenced by some closeout and review flows; governed when present, but it MUST NOT replace the authoritative audit/gates/json\_gate/canonical/ family or the audit/gates/canonical\_json/ legacy pair as the binding surface for new plans)

This legacy family may remain present and evidence-indexed until an explicit canon migration removes it. During that period, it remains a governed output, but it MUST NOT be required by new plans or used as the sole binding for acceptance claims unless canon explicitly reinstates it (via PF12).

Canonical JSON gate target artifacts (minimum required keys)

The canonical JSON gate target set MUST include the conjunction-related CLI artifacts:

- cli.conjunction.pair\_ab (path: artifacts/audit/cli/pair.json)  
    
- cli.conjunction.pair\_ba (path: artifacts/audit/cli/pair\_ba.json)  
    
- cli.conjunction.showcompat\_ab (path: artifacts/audit/cli/showcompat\_ab.json)  
    
- cli.conjunction.showcompat\_ba (path: artifacts/audit/cli/showcompat\_ba.json)  
    
- cli.conjunction.output\_ab (path: artifacts/cli/out.json)  
    
- cli.conjunction.output\_ba (path: artifacts/cli/out\_ba.json)  
    
- cli.conjunction.abba\_sidecar (path: artifacts/cli/abba\_sidecar.json)

Implementation note: the target set is enforced by tools/evidence/run\_canonical\_json\_gate.py and MUST remain synchronized with this canon list.

EPIC-029 bounded conjunction route-probe current-state.

- The current EPIC029 canonical JSON gate lane MAY truthfully operate as a bounded route-probe over the conjunction JSON surface family recorded in `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`.  
- The required bounded minimum loci for that route-probe family are `/reader`, `/dev/writer/conjunction`, and `/internal/dev/sampler`.  
- Additional same-family loci MAY be probed only when they remain inside the same bounded conjunction JSON family and do not widen the proof surface, specifically `/dev/reader/conjunction` and `/dev/sampler/conjunction`.  
- When the canonical JSON gate is used as a route-probe family, governed gate outputs MUST fail closed on unexpected HTTP status. Canonical-byte equality alone is insufficient for acceptance.  
- When `audit/gates/json_gate/canonical/json_gate_structured_record.json` is emitted for this family, each probed locus MUST record both `expected_http_status` and `http_status`.  
- After any fix to route-probe status logic, the authoritative canonical JSON gate family, the Human Evidence Index, the Machine Evidence Mirror, and the required sibling path-proofs for changed governed artifacts MUST be regenerated coherently in the same change.

Acceptance bindings MUST cite audit/gates/json\_gate/canonical/ as the authoritative family. The legacy family under audit/gates/canonical\_json/ and the optional legacy artifact audit/gates/canonical\_json\_gate.json MAY be present and tracked during migration, but they MUST NOT be treated as independent acceptance bindings.

Evidence index snapshot artifacts (single home; remove EPIC-local variant)

Canonical evidence index snapshot artifacts MUST use the gate-family path:

- audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json  
- audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt

Deprecated snapshot files (MUST NOT use):

- `artifacts/INDEX_SNAPSHOT.json`  
    
- `audit/evidence_index_snapshot/evidence_index_snapshot.json`

Generator (titles-only).

The canonical generator invocation is python tools/evidence/generate\_evidence\_index\_snapshot.py. Plans and runbooks MUST NOT reference python tools/evidence/run\_evidence\_index\_snapshot.py.

Minimum snapshot JSON contract (records-only).

The snapshot JSON MUST include the following top-level keys: `schema_version`, `generated_at_utc`, `inputs`, `parity`.

`generated_at_utc` MUST be a RFC3339 UTC timestamp.

`parity` MUST include `artifact_keys_match` as a boolean.

The EPIC-local variant under `audit/qa/<epic-id>/evidence_index_snapshot.json` is non-authoritative and is not a closure-required canonical surface. Plans and acceptance artifacts MUST NOT bind to EPIC-local variants when the PF12 canonical gate-family surface exists.

Canonical compare artifacts (no epic-local compare paths)

Canonical compare evidence for canonical JSON gate checks MUST reuse the canon-defined surface under audit/gates/json\_gate/canonical/ (see json\_gate\_compare\_log.ndjson above).

Epics MUST NOT introduce new compare artifact paths as “the canonical compare proof” without an explicit canon change routed through a Doc-Delta and drained into the owning PF-Canon homes.

Close-pack artifacts (deterministic path-of-record; baseline artifacts)

The close-pack baseline artifacts MUST be located under audit/ using the EPIC-\#\#\# pattern (3 digits):

- audit/EPIC-\#\#\#\_close\_report.md  
- audit/EPIC-\#\#\#\_close\_report.md.path\_proof.txt  
- audit/EPIC-\#\#\#\_MANIFEST.json  
- audit/EPIC-\#\#\#\_MANIFEST.json.path\_proof.txt  
- audit/EPIC-\#\#\#\_QA\_RCA.md only when the QA RCA & Doc Delta summary is externalized as a separate governed artifact.

If the QA RCA & Doc Delta summary is embedded directly inside audit/EPIC-\#\#\#\_close\_report.md, the separate audit/EPIC-\#\#\#\_QA\_RCA.md artifact is not required. If a separate QA RCA artifact is used, the close report MUST reference it by exact repo-relative path.

When a QA RCA & Doc Delta summary is embedded in the close report or externalized as a separate governed QA RCA artifact, the RCA content SHOULD include, at minimum:

- what was reviewed and which source posture governed the review  
- coverage versus the QA plan or review plan  
- findings classification  
- outcome meaning  
- evidence support  
- root causes  
- remediation-loop assessment  
- evidence-hygiene assessment  
- recurrence-prevention follow-ups  
- canon follow-up posture  
- closeout-readiness recommendation

The QA RCA content MUST preserve proof-class separation among implementation support, QA result, close-pack packaging, PF-canon drainage, formal closeout, and deferred future work.

The close report at `audit/EPIC-###_close_report.md` MUST:

- Summarize shipped deliverables and the closure-minimum evidence artifacts produced by the epic.  
- Enumerate explicit deferrals (if any) by ID (for example, `TI-002`) in a dedicated section.  
- When the close-pack is intended to support a later PF-canon update, include a dedicated later-drain PF-canon update statement for each claimed supported update.  
- Each later-drain PF-canon update statement MUST include:  
  - affected PF canon home(s)  
  - exact affected locator(s)  
  - current canon posture  
  - supported later-drain action, using exactly one of: `change to Done`, `change to Partial`, `change to Not done`, `change to Consolidation pending`, `change to Optional`, `No status change recommended`  
  - drain readiness classification, using exactly one of: `Supportable from repo evidence`, `Not yet supportable from repo evidence`, `Already drained into PF-canon`  
  - evidence basis  
  - epic-close expectation  
- When current PF09 recorded status is cited, the close report MUST treat it as the current drained record only. The close report MUST distinguish current PF09 recorded status, supported later-drain status, actual implemented state, actual OPS state, and actual governed evidence state.  
- When a close report, QA RCA, closure review, or close-pack-adjacent governed artifact records a closure-trace decision such as `SATISFIED`, `READY`, `READY WITH CAVEATS`, or equivalent language, it MUST state whether that decision is review-trace-only, PO closeout, formal close-pack completion, or another explicitly named posture.  
- Review-trace satisfaction MUST NOT be presented as a PO closeout action, PF09 drain, or epic closure unless the governing close-pack artifact and approval process bind that claim.  
- The current PF09 recorded status text alone MUST NOT be used as the closure gate inside the close-pack narrative.  
- Later-drain PF-canon update statements are support records for future canon maintenance. They MUST NOT be treated as execution prerequisites, required deliverables, required checks, acceptance conditions, blockers, or close-pack readiness gates by themselves.  
- When the live truth for an undrained update is already recorded in PF10 or the owning PF canon home, otherwise-proven work remains valid without waiting for later drainage.  
- Point to the corresponding close-pack manifest’s `key_outputs` map as the binding authority for primary artifacts and their canonical paths-of-record.

In addition to the EPIC-\#\#\# baseline artifacts above, a closure pack MUST include the following supporting ledgers and QA harness outputs (repo-relative, governed):

- `audit/docdeltas/<epic-id>_doc_deltas.md` (doc delta ledger; MUST explicitly indicate when empty)  
    
- `audit/docdeltas/<epic-id>_drain_targets.md` (drain targets ledger; MUST explicitly indicate when empty)  
    
- `audit/qa/<epic-id>/qa_step_logs_manifest.json` (QA step logs manifest; titles-only index)

If `audit/qa/<epic-id>/00_meta/doc_deltas.md` is present as a QA-root copy, it MUST be byte-identical to `audit/docdeltas/<epic-id>_doc_deltas.md`.

In the close report’s dedicated deferrals section, each deferral MUST include its ID (e.g., TI-002) and its drain target pointer (PF09 pointer) when available. If a PF09 pointer is not yet available, the close report MUST declare the ADR status and rationale and ensure the deferral is represented in `audit/docdeltas/<epic-id>_drain_targets.md` as a canon pointer record.

These are baseline closure artifacts (required artifacts), not acceptance tokens by default. They MUST NOT be relocated into alternate directory trees (for example audit/qa/\*\* or artifacts/\*\*) without an explicit canon change.

Acceptance-binding family coherence (normative).

- Any governed evidence family that participates in acceptance or close-pack binding MUST present exactly one authoritative posture for each claimed closure dimension.  
- A mixed-state governed evidence family is invalid. If one governed artifact says `closed` and another governed artifact in the same family says `not yet closed`, `deferred`, `partial`, or equivalent contradictory meaning for the same closure dimension, the family MUST be treated as non-acceptable until normalized.  
- Consolidation or review artifacts MUST NOT summarize contradictory governed source bytes as if they formed a valid authoritative family state. When governed source bytes disagree, the issue MUST be classified as a documentation/evidence failure rather than a new runtime failure unless runtime facts are missing, changed, or contradicted.  
- A documentation/evidence normalization pass MAY be used instead of a new runtime rerun only when the underlying runtime facts are unchanged and already evidenced, no new runtime or ops behavior is being claimed, every governed artifact in the affected family is rewritten or refreshed to the same authoritative posture, and the Human Evidence Index, the Machine Evidence Mirror, any required checksum sidecars, and the required sibling path-proofs are refreshed coherently in the same change.  
- When equivalence or substitution is used for closure, the governed family MUST state the closure mode explicitly.

Evidence generator PASS coupling.

- A governed evidence generator MUST NOT emit or preserve a PASS posture for a family unless every decisive predicate recorded by that family has been evaluated and passed.  
- A top-level PASS MUST be derived from the artifact's predicate checks, not from stale local state, omitted comparisons, or partial binding checks.  
- After generator logic changes, final governed artifacts produced by that generator MUST be regenerated from the final logic before path-proofs, Human Index rows, Machine Mirror rows, and checksum sidecars are refreshed.  
- If an artifact's recorded PASS cannot be coupled to final generator logic and current predicate checks, the artifact is stale for acceptance and MUST NOT satisfy the evidence family until regenerated and rebound.

EPIC-028 OPS closeout evidence bundles (current-state).

- `audit/ops/hde-epic028/ops-01/commands.txt`: Optional OPS-01 action ledger for the packaging/evidence-only close-pack surfacing run. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-01/stdout.log`: Optional OPS-01 stdout capture for the packaging/evidence-only close-pack surfacing run. If present, it MUST be UTF-8 text.  
- `audit/ops/hde-epic028/ops-01/stderr.log`: Optional OPS-01 stderr capture for the packaging/evidence-only close-pack surfacing run. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic028/ops-01/exit_codes.txt`: Optional OPS-01 exit-code ledger for the packaging/evidence-only close-pack surfacing run. If present, it MUST contain only the final integer exit codes plus trailing LF.  
- `audit/ops/hde-epic028/ops-01/created_files_sha256.txt`: Optional OPS-01 checksum ledger for the surfaced close-pack outputs. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-02/commands.txt`: Optional OPS-02 action ledger for the provenance-only closeout binding run. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-02/repo_root.txt`: Optional OPS-02 repo-root capture. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-02/repo_head.txt`: Optional OPS-02 repo-head capture. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-02/python_version.txt`: Optional OPS-02 Python-version capture. LF-terminated text when present.  
- `audit/ops/hde-epic028/ops-02/stdout.log`: Optional OPS-02 stdout capture for the provenance-only closeout binding run. If present, it MUST be UTF-8 text.  
- `audit/ops/hde-epic028/ops-02/stderr.log`: Optional OPS-02 stderr capture for the provenance-only closeout binding run. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic028/ops-02/exit_codes.txt`: Optional OPS-02 exit-code ledger for the provenance-only closeout binding run. If present, it MUST contain only the final integer exit codes plus trailing LF.  
- `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md`: Optional OPS-02 governed provenance artifact used to bind one executed QA artifact family to a Codespaces execution context using presence-only venue details. Non-empty UTF-8 markdown when present.  
- `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md.path_proof.txt`: Required sibling path-proof transcript whenever `codespaces_harness_binding.md` is treated as governed closeout evidence.

When the OPS-02 provenance bundle uses a single closure-relevant governed QA artifact as its binding target, the allowed current-state target is either `audit/qa/hde-epic028/qa_step_logs_manifest.json` or `audit/qa/hde-epic028/checks/po-010/final_summary.txt`. The currently surfaced EPIC028 OPS-02 bundle binds `audit/qa/hde-epic028/checks/po-010/final_summary.txt`.

EPIC-029 OPS closeout evidence bundle (current-state).

- `audit/ops/hde-epic029/ops-01/commands.txt`: Optional OPS-01 action ledger for the EPIC029 dev-harness validation rerun. LF-terminated text when present.  
- `audit/ops/hde-epic029/ops-01/stdout.log`: Optional OPS-01 stdout capture for the EPIC029 dev-harness validation rerun. If present, it MUST be UTF-8 text.  
- `audit/ops/hde-epic029/ops-01/stderr.log`: Optional OPS-01 stderr capture for the EPIC029 dev-harness validation rerun. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`: Optional OPS-01 exit-code ledger for the EPIC029 dev-harness validation rerun. If present, it MUST contain only the final integer exit codes plus trailing LF.  
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`: Optional OPS-01 Codespaces binding note recording the effective EPIC029 Codespaces dev-harness URL and, when Codespaces is closed, the direct runtime-validation closure posture. Non-empty UTF-8 markdown when present.  
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`: Optional OPS-01 local-dev binding note recording the authoritative local-dev publication state and closure posture for the same dev-only sampler harness. Non-empty UTF-8 markdown when present. When `local_dev` is closed by binding-equivalence for HDE-EPIC029 W-004, this artifact MUST record at least `environment: local_dev`, `dev_sampler_url: http://127.0.0.1:8000/internal/dev/sampler`, `closure_mode: binding-equivalence`, `basis: approved same published DEV_SAMPLER_URL value as Codespaces for the same dev-only sampler harness`, and `note: no separate local-dev runtime was executed in this evidence pass`.  
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`: Optional OPS-01 per-environment disposition ledger for the EPIC029 dev-harness validation rerun. Non-empty UTF-8 markdown when present. It is the authoritative family summary when EPIC029 W-004 closure is normalized.  
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`: Optional OPS-01 checksum ledger for the surfaced OPS-01 bundle outputs. LF-terminated text when present.

When this EPIC029 OPS-01 bundle is bound into close-pack evidence, it is a governed closure-support OPS family for the EPIC029 dev-harness closure dimension. The family MAY preserve `codespaces` and `local_dev` as `not yet closed` only when that is the single authoritative posture for the current run.

For HDE-EPIC029 W-004 only, `local_dev` MAY be closed by binding-equivalence without a second independent local-dev runtime rerun when all of the following are true:

- the approved `DEV_SAMPLER_URL` value for `local_dev` is exactly `http://127.0.0.1:8000/internal/dev/sampler`  
- that value matches the approved Codespaces client-access value for the same dev-only sampler harness  
- the equivalence claim is limited to the client access binding for that same route  
- the underlying runtime facts already evidenced for Codespaces remain unchanged  
- no new local-dev-only behavior is being claimed

When `local_dev` is closed by binding-equivalence in this family, the authoritative OPS-01 posture MUST state all of the following:

- `codespaces` — closed by direct runtime validation  
- `local_dev` — closed by binding-equivalence  
- no separate local-dev runtime was executed in this evidence pass

The minimum OPS-01 artifacts that MUST be normalized together for that closure posture are:

- `audit/ops/hde-epic029/ops-01/commands.txt`  
    
- `audit/ops/hde-epic029/ops-01/stdout.log`  
    
- `audit/ops/hde-epic029/ops-01/stderr.log`  
    
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`  
    
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`  
    
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`  
    
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`  
    
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

If indexed governed bytes change during that normalization, the Human Evidence Index, the Machine Evidence Mirror, any required checksum sidecars, and the required sibling path-proofs MUST be refreshed coherently in the same change.

EPIC-029 OPS validation evidence bundle (current-state).

- `audit/ops/hde-epic029/ops-02/W-001_action_log_and_evidence_output_run2.md`: Optional OPS-02 read-only validation bundle for Work Item W-001. Non-empty UTF-8 markdown when present.  
- `audit/ops/hde-epic029/ops-02/W-001_classification_run2.md`: Optional OPS-02 classification artifact recording the bounded blocker-classification result for `HDE-CONJ009.1` and `HDE-CONJ008.1`. Non-empty UTF-8 markdown when present.  
- `audit/ops/hde-epic029/ops-02/commands_w001_run2.txt`: Optional OPS-02 command ledger for the W-001 read-only validation run. LF-terminated text when present.  
- `audit/ops/hde-epic029/ops-02/exit_codes_w001_run2.txt`: Optional OPS-02 exit-code ledger for the W-001 read-only validation run. If present, it MUST contain only the final integer exit codes plus trailing LF.  
- `audit/ops/hde-epic029/ops-02/stdout_w001_run2.log`: Optional OPS-02 stdout capture for the W-001 read-only validation run. If present, it MUST be UTF-8 text.  
- `audit/ops/hde-epic029/ops-02/stderr_w001_run2.log`: Optional OPS-02 stderr capture for the W-001 read-only validation run. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.

HDE-EPIC030 po-006 remediation OPS adoption evidence bundle.

Purpose. Govern the OPS-01 and OPS-02 adoption evidence paths for HDE-EPIC030 po-006 remediation discovery and controlled vendor-smoke validation. These artifacts may support remediation verification only. They do not by themselves claim QA PASS, Live QA completion, PF09 status change, epic closure, a new public route, a new public flag, or a new acceptance token.

OPS-01 artifact paths and content.

- `audit/ops/hde-epic030/ops-01/commands.txt`: Optional OPS-01 command ledger for discovery commands, remediation edit actions, and checksum regeneration. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/python_version.txt`: Optional OPS-01 Python-version stdout capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/python_version.stderr`: Optional OPS-01 Python-version stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/pytest_version.txt`: Optional OPS-01 pytest-version stdout capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/pytest_version.stderr`: Optional OPS-01 pytest-version stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/grep_path.txt`: Optional OPS-01 grep-path capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/grep_path.stderr`: Optional OPS-01 grep-path stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/hdctl_path.txt`: Optional OPS-01 hdctl-path capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/hdctl_path.stderr`: Optional OPS-01 hdctl-path stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/hdctl_help.txt`: Optional OPS-01 hdctl help capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/hdctl_help.stderr`: Optional OPS-01 hdctl help stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/showcompat_help.txt`: Optional OPS-01 showcompat help capture. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-01/showcompat_help.stderr`: Optional OPS-01 showcompat help stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-01/env_presence.json`: Optional OPS-01 environment-presence snapshot. Canonical JSON when present. It MUST contain key names and boolean values only and MUST NOT persist secret values.  
- `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`: Optional OPS-01 command-candidate record for the vendor-backed no-user command discovery posture. LF-terminated text when present. If command proof is unresolved, it MAY record the approved unresolved sentinel.  
- `audit/ops/hde-epic030/ops-01/discovery_summary.md`: Optional OPS-01 discovery summary recording command-proof posture, vendor-smoke block posture, and result posture. Non-empty UTF-8 markdown when present.  
- `audit/ops/hde-epic030/ops-01/files_sha256.txt`: Optional OPS-01 checksum ledger for the captured OPS-01 evidence files. LF-terminated text when present. It SHOULD include hashes for all OPS-01 captured files except itself.

OPS-02 artifact paths and content.

- `audit/ops/hde-epic030/ops-02/vendor_command.txt`: Required when OPS-02 completion is claimed. LF-terminated text containing the exact executable command used for the controlled vendor-backed birth-only no-user smoke. It MUST contain no unresolved placeholders and no caller user identity inputs.  
- `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`: Required when OPS-02 completion is claimed. Canonical JSON containing the birth values substituted into the command and constraints proving no app user IDs, no `person_uid`, no `user_id`, and vendor-call execution posture.  
- `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`: Required when OPS-02 completion is claimed. Canonical JSON containing key names and boolean values only. It MUST NOT persist secret values.  
- `audit/ops/hde-epic030/ops-02/target_disposition.md`: Required when OPS-02 completion is claimed. Non-empty UTF-8 markdown recording the target classification, including `CLI_LOCAL_VENDOR_SMOKE` when the run is a local CLI vendor-source smoke rather than a hosted HD Engine HTTP service smoke.  
- `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`: Required when OPS-02 completion is claimed. Non-empty UTF-8 markdown proving the PR-02 remediation is present in the runtime used for OPS-02, including the birth-only boundary and no caller `user_id` or `person_uid` posture.  
- `audit/ops/hde-epic030/ops-02/request_summary.txt`: Required when OPS-02 completion is claimed. LF-terminated text recording command source, input shape, target classification, no-user facts, no-secret facts, explicit vendor source use, and PO proceed authorization posture.  
- `audit/ops/hde-epic030/ops-02/stdout.json`: Required when OPS-02 execution is attempted. Canonical JSON when the command emits JSON stdout; otherwise UTF-8 stdout capture if the documented success output differs.  
- `audit/ops/hde-epic030/ops-02/stderr.log`: Required when OPS-02 execution is attempted. UTF-8 stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-02/exit_code.txt`: Required when OPS-02 execution is attempted. It MUST contain only the final integer exit code plus trailing LF.  
- `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`: Required when OPS-02 execution is attempted. Non-empty UTF-8 markdown recording whether stdout is non-empty, parseable, secret-free, and coupled to the recorded command exit code.  
- `audit/ops/hde-epic030/ops-02/stdout.json.sha256`: Required when OPS-02 execution is attempted and `stdout.json` is present. LF-terminated checksum sidecar containing the sha256 for `audit/ops/hde-epic030/ops-02/stdout.json`.  
- `audit/ops/hde-epic030/ops-02/execution_classification.md`: Required when OPS-02 execution is attempted. Non-empty UTF-8 markdown recording exactly one final execution classification and whether the command ran and vendor call executed.  
- `audit/ops/hde-epic030/ops-02/result_summary.md`: Required when OPS-02 completion is claimed. Non-empty UTF-8 markdown. It MUST record the outcome classification and state that the evidence is implementation-validation evidence only, not QA PASS, Live QA completion, PF09 status change, or epic closure.  
- `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`: Required when OPS-02 completion is claimed. Non-empty UTF-8 markdown mapping each OPS-02 prerequisite to its PF canon or PF10 basis and evidence status.  
- `audit/ops/hde-epic030/ops-02/files_sha256.txt`: Required when OPS-02 completion is claimed. LF-terminated checksum ledger. It MUST include hashes for the decisive OPS-02 evidence files. For po-006 validation, the final ledger MUST include the deterministic self-reference row for `audit/ops/hde-epic030/ops-02/files_sha256.txt` recorded by the accepted Moon Loop remediation.  
- `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`: Required when OPS-02 completion is claimed. Non-empty UTF-8 markdown exposing the decisive command, birth inputs, target disposition, PR-02 runtime binding, request summary, result summary, runtime outputs, execution classification, and checksum ledger contents for review.

Path-proofs and indexing.

- Each concrete artifact above MUST have a sibling .path\_proof.txt transcript if it is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence.  
- The Human Evidence Index and Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules.  
- The corresponding Mirror records MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact.  
- Non-path labels such as PR-01 boundary report and PR-02 targeted test report are not cataloged by this entry unless a later governed evidence record supplies concrete repo-relative paths for them.

HDE-EPIC030 close-pack and OPS-03 evidence-packaging bundle.

Purpose. Govern the HDE-EPIC030 close-pack surfacing artifacts and the OPS-03 evidence-packaging bundle. OPS-03 evidence packaging is close-pack surfacing only. It does not by itself claim QA rerun, vendor call execution, implementation change, PF-Canon edit, PF09.2 drainage, a new acceptance claim, a new public route, a new public flag, or a new acceptance token.

Close-pack and QA RCA artifact paths.

- `audit/EPIC-030_close_report.md`: HDE-EPIC030 close report. Non-empty UTF-8 markdown when present.  
- `audit/EPIC-030_close_report.md.path_proof.txt`: Required sibling path-proof transcript when the close report is treated as governed close-pack evidence.  
- `audit/EPIC-030_MANIFEST.json`: HDE-EPIC030 close-pack manifest. Canonical JSON when present. It MUST use a named `key_outputs` map.  
- `audit/EPIC-030_MANIFEST.json.path_proof.txt`: Required sibling path-proof transcript when the close-pack manifest is treated as governed close-pack evidence.  
- `audit/EPIC-030_QA_RCA.md`: HDE-EPIC030 QA RCA and closeout interpretation artifact. Non-empty UTF-8 markdown when present. It SHOULD include coverage versus QA plan, findings classification, outcome meaning, evidence support, RCA root causes, remediation-loop assessment, evidence hygiene assessment, recurrence-prevention follow-ups, canon follow-up, and closeout-readiness recommendation.  
- `docs/acceptance_map_epic030.json`: HDE-EPIC030 acceptance map. Canonical JSON when present.  
- `audit/qa/hde-epic030/token_evidence_matrix.md`: HDE-EPIC030 token-to-evidence matrix. Non-empty UTF-8 markdown when present.  
- `audit/qa/hde-epic030/qa_step_logs_manifest.json`: HDE-EPIC030 QA step logs manifest. Canonical JSON when present.  
- `audit/docdeltas/hde-epic030_doc_deltas.md`: HDE-EPIC030 doc-delta ledger. Non-empty UTF-8 markdown when present unless the ledger explicitly records that it is empty.  
- `audit/docdeltas/hde-epic030_drain_targets.md`: HDE-EPIC030 drain-targets ledger. Non-empty UTF-8 markdown when present unless the ledger explicitly records that it is empty.

HDE-EPIC030 close-pack manifest key\_outputs bindings.

When `audit/EPIC-030_MANIFEST.json` is used as the close-pack binding authority, its `key_outputs` map SHOULD include stable bindings for the following governed artifacts when those artifacts are present:

- `close_report`: `audit/EPIC-030_close_report.md`  
- `close_manifest`: `audit/EPIC-030_MANIFEST.json`  
- `qa_rca`: `audit/EPIC-030_QA_RCA.md`  
- `acceptance_map`: `docs/acceptance_map_epic030.json`  
- `token_matrix`: `audit/qa/hde-epic030/token_evidence_matrix.md`  
- `qa_step_manifest`: `audit/qa/hde-epic030/qa_step_logs_manifest.json`  
- `doc_deltas`: `audit/docdeltas/hde-epic030_doc_deltas.md`  
- `drain_targets`: `audit/docdeltas/hde-epic030_drain_targets.md`  
- `final_evidence_inventory`: `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md`  
- `ops03_created_files_sha256`: `audit/ops/hde-epic030/ops-03/created_files_sha256.txt`

OPS-03 artifact paths and content.

- `audit/ops/hde-epic030/ops-03/commands.txt`: Required when OPS-03 completion is claimed. LF-terminated text containing the corrected, replayable, task-labeled command transcript.  
- `audit/ops/hde-epic030/ops-03/commands_prev_invalid.txt`: Optional OPS-03 audit-trail artifact preserving the prior invalid command transcript. LF-terminated text when present.  
- `audit/ops/hde-epic030/ops-03/stdout.log`: Required when OPS-03 completion is claimed. UTF-8 text containing labeled stdout sections for manifest validation, close-report validation, path-proof validation, inventory generation, checksum generation, and final validation.  
- `audit/ops/hde-epic030/ops-03/stderr.log`: Required when OPS-03 completion is claimed. UTF-8 stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `audit/ops/hde-epic030/ops-03/exit_codes.txt`: Required when OPS-03 completion is claimed. LF-terminated ledger mapping task labels to integer exit codes.  
- `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md`: Required when OPS-03 completion is claimed. Non-empty UTF-8 markdown inventory of the surfaced close-pack and supporting evidence family.  
- `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md.path_proof.txt`: Required sibling path-proof transcript for the final evidence inventory when it is treated as governed evidence.  
- `audit/ops/hde-epic030/ops-03/final_validation.log`: Required when OPS-03 completion is claimed. LF-terminated text recording PASS lines for file existence, manifest validation, close-report validation, path-proof validation, final inventory validation, and OPS-03 evidence bundle validation.  
- `audit/ops/hde-epic030/ops-03/created_files_sha256.txt`: Required when OPS-03 completion is claimed. LF-terminated checksum ledger for created or refreshed OPS-03 files.  
- Non-path R3 report labels are not cataloged by this entry unless a later governed evidence record supplies a concrete repo-relative path for that report.

Path-proofs and indexing.

- Each concrete artifact above MUST have a sibling .path\_proof.txt transcript if it is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence.  
- The Human Evidence Index and Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules.  
- The corresponding Mirror records MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact.  
- The OPS-03 family MUST preserve the separation between close-pack surfacing, PF09.2 later-drain support, QA PASS, Live QA completion, PF09 status change, and epic closure.

HDE-EPIC032 OPS-01 DB provider parity evidence (historical-only).

The retained `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` remains non-claiming OPS evidence under its current record identity; it is not a current bridge gate. Its governed bytes, ledger binding, and sibling path-proof remain subject to §8.7. It MUST NOT prove current bridge availability, runtime support, direct-versus-bridge parity, bridge consistency, bridge fallback, current OPS PASS, release admission, PF09 status movement, epic closure, or acceptance-token satisfaction, and it MUST NOT be regenerated through retired transport.

HDAPI v2 open-rails OPS smoke evidence bundle.

Purpose. Govern the file-set shape for a PO-only HDAPI v2 open-rails smoke evidence bundle after a concrete epic-specific OPS audit root is assigned. This family is HDAPI vendor-conformance evidence only. It does not by itself claim runtime v2 conformance, QA PASS, Live QA completion, PF09 status change, epic closure, a new public Reader route, a Reader v1 contract change, a new public flag, a new acceptance token, app-side vendor credential ownership, raw payload persistence, or any AI enablement.

Concrete path-binding rule.

- The exact OPS smoke root MUST be a lowercase ASCII repo-relative path under `audit/ops/`. The root is assigned by the epic or OPS plan and MUST be bound by exact repo-relative path before the family is indexed, mirrored, or used as acceptance-support evidence.  
- A retained OPS smoke bundle MAY use a nested evidence root when the evidence was produced that way, provided a manifest maps approved deliverable names to retained evidence paths without moving or deleting current evidence.  
- For HDE-EPIC035 OPS-01, the assigned OPS root is `audit/ops/hde-epic035/ops-01/`, the retained nested smoke root is `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/`, and the manifest is `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt`.  
- Once the concrete root is assigned, PF12 path binding, the Human Evidence Index, the Machine Evidence Mirror, checksum ledgers, and sibling path-proofs MUST use the exact resulting repo-relative paths.  
- PR work MAY bind already-produced OPS evidence into governed evidence without rerunning the live vendor action when the binding artifact states that posture and preserves nonclaims.

Artifact filenames for retained OPS smoke evidence.

- `ops_evidence_manifest.txt`: Required when approved deliverable names differ from retained paths or formats. LF-terminated manifest mapping planned deliverables to retained evidence paths and status classifications.  
- `files_sha256.txt`: Required when open-rails smoke completion or retained evidence binding is claimed. LF-terminated checksum ledger for the OPS smoke evidence files in the assigned root or retained nested smoke root.  
- `commands.txt`: Required when the open-rails smoke is executed. LF-terminated command ledger for the controlled PO-run HDAPI v2 vendor smoke.  
- `stdout.log`: Required when the open-rails smoke is executed. UTF-8 stdout capture. It MUST NOT persist plaintext secrets.  
- `stderr.log`: Required when the open-rails smoke is executed. UTF-8 stderr capture. It MAY be empty only when the underlying command produced no stderr and the run still requires the file.  
- `exit_codes.txt`: Required when the open-rails smoke is executed. LF-terminated ledger mapping executed command labels to integer exit codes.  
- `redacted_env_presence.json`: Required when the open-rails smoke is executed. Canonical JSON containing exact key names and presence-only or redacted values only. It MUST NOT persist secret values.  
- `request_summary.txt` or `request_summary.json`: Required when the open-rails smoke is executed. The retained artifact MUST record the HDAPI-only target, route family, request-shaping basis, secret-handling posture, and PO authorization posture. Canonical JSON is preferred for new evidence; LF-terminated text remains governed when retained and manifest-bound.  
- `result_summary.md`, `result_summary.txt`, or `result_summary.json`: Required when open-rails smoke completion or retained evidence binding is claimed. The retained artifact MUST record outcome classification, vendor-only scope, secret-free posture, conformance claim boundary, and whether the result supports bounded conformance evidence.  
- `final_classification.txt`: Required when retained evidence distinguishes multiple live observations, such as `bg:resolve` versus a v2 chart route. It MUST record final safe classifications and nonclaims.  
- Route-specific command, stdout, stderr, and result-summary files MAY be retained when needed to distinguish a successful v2 chart/geokey observation from a legacy BodyGraph-route observation. If promoted, each retained file MUST have a sibling path-proof transcript and MUST be included in the Human Evidence Index and Machine Evidence Mirror.  
* `moon_loop_rerun_transcript.txt`: Optional but governed when retained. LF-terminated transcript preserving command-to-output provenance. If promoted, it MUST have a sibling path-proof transcript.  
* `ops02_full_action_log_and_evidence_output.md`: Optional but governed when retained. UTF-8 action log and evidence-output summary. If promoted, it MUST have a sibling path-proof transcript.  
* `ops02_open_rails_smoke_procedure.py`: Optional but governed when retained. UTF-8 repo-resident smoke procedure used for provenance or review. If promoted, it MUST have a sibling path-proof transcript and MUST NOT be treated as product runtime code.

PR binding artifacts for already-produced OPS smoke evidence.

- `audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log`: HDE-EPIC034 PR-06 LF-terminated binding log for already-produced OPS-02 open-rails smoke evidence. It supports HDE-FERM008.2 only and MUST preserve no full v2 runtime conformance, no HDE-FERM008 parent completion, no public Reader, and no AI scope claims.  
- `docs/acceptance_map_epic034.json`: HDE-EPIC034 acceptance map when used to bind PR-06 evidence. It MUST use existing registered acceptance posture only and MUST NOT mint a vendor-specific acceptance token by itself.  
- `audit/docdeltas/hde-epic034_doc_deltas.md` and `audit/qa/hde-epic034/00_meta/doc_deltas.md`: HDE-EPIC034 PR-06 doc-delta surfaces when used to record OPS-02 support and nonclaims. They are governed only when indexed, mirrored, and path-proven.

Path-proofs and indexing.

- Each concrete artifact above MUST have a sibling `.path_proof.txt` transcript when it is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence.  
- The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted concrete path under the normal PF12 parity rules.  
- The corresponding Mirror records MUST set proof\_anchor to the sibling `.path_proof.txt` transcript for that artifact.  
- If the assigned OPS smoke root changes, every affected artifact path, path-proof transcript, Human Index entry, Machine Mirror record, and checksum sidecar MUST be refreshed coherently in the same change.

No-AI evidence boundary.

- This OPS bundle MUST be limited to HumanDesignAPI v2 vendor-conformance evidence.  
- It MUST NOT include OpenAI, LLM, AI-agent, chatbot, prompt, embedding, model-call, or AI-provider calls.  
- It MUST NOT introduce AI-provider config keys, credentials, rails, acceptance tokens, evidence families, QA obligations, public or admin runtime surfaces, or product scope.  
- Vendor AI or LLM documentation, if inspected, is documentation-discovery context only and MUST NOT be captured as runtime evidence.

Generator contract (titles-only; EPIC-025). `tools/qa/generate_epic025_close_pack.py` is the governed generator. Its output set MUST include:

- `audit/EPIC-025_MANIFEST.json`  
    
- `audit/EPIC-025_MANIFEST.json.path_proof.txt`  
    
- `audit/EPIC-025_close_report.md`  
    
- `audit/EPIC-025_close_report.md.path_proof.txt`  
    
- `audit/docdeltas/hde-epic025_doc_deltas.md`  
    
- `audit/qa/hde-epic025/qa_step_logs_manifest.json`  
    
- `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`

Generator contract (titles-only; EPIC-026). `tools/qa/generate_epic026_close_pack.py` is the governed generator. Its output set MUST include:

- `audit/EPIC-026_MANIFEST.json`  
    
- `audit/EPIC-026_MANIFEST.json.path_proof.txt`  
    
- `audit/EPIC-026_close_report.md`  
    
- `audit/EPIC-026_close_report.md.path_proof.txt`  
    
- `audit/docdeltas/hde-epic026_doc_deltas.md`  
    
- `audit/docdeltas/hde-epic026_drain_targets.md`  
    
- `audit/qa/hde-epic026/00_meta/doc_deltas.md`  
    
- `audit/qa/hde-epic026/qa_step_logs_manifest.json`  
    
- `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt`  
    
1. `audit/EPIC-026_close_pack.md` (optional EPIC026 close-pack bundle summary; governed when present, but it MUST NOT replace `audit/EPIC-026_MANIFEST.json` as the binding surface)  
     
2. `audit/qa/hde-epic026/close_pack/` (optional EPIC026 QA-root close-pack working directory; child artifacts under this directory are non-authoritative unless a specific child path is separately cataloged here)

Close-pack manifest key\_outputs (named binding map; normative)

The close-pack manifest (audit/EPIC-\#\#\#\_MANIFEST.json) MUST include key\_outputs as a JSON object (map) where:

- each key is a stable pointer name (snake\_case), suitable for use as a binding label in the close report  
    
- each value is either:  
    
  - a repo-relative artifact path string, intended to be a canonical pointer to a governed artifact, or  
      
  - a non-empty list of repo-relative artifact path strings when the key intentionally binds multiple governed artifacts


- when a value is a list, list order MUST be stable and SHOULD be deterministic to preserve diff integrity

EPIC023 required bindings (normative)

For EPIC023, key\_outputs MUST include these keys and exact values:

- acceptance\_map: docs/acceptance\_map\_epic023.json  
- token\_matrix: audit/qa/hde-epic023/token\_evidence\_matrix.md  
- acceptance\_map\_viability: audit/qa/hde-epic023/acceptance\_map\_viability.log  
- qa\_step\_manifest: audit/qa/hde-epic023/qa\_step\_logs\_manifest.json  
- doc\_deltas: audit/docdeltas/hde-epic023\_doc\_deltas.md  
- close\_report: audit/EPIC-023\_close\_report.md  
- close\_manifest: audit/EPIC-023\_MANIFEST.json

EPIC024 required bindings (normative)

For EPIC024, key\_outputs MUST include at least these keys and exact values:

- close\_manifest: audit/EPIC-024\_MANIFEST.json  
    
- acceptance\_map: docs/acceptance\_map\_epic024.json  
    
- token\_matrix: audit/qa/hde-epic024/token\_evidence\_matrix.md  
    
- qa\_step\_manifest: audit/qa/hde-epic024/qa\_step\_logs\_manifest.json  
    
- doc\_deltas: audit/docdeltas/hde-epic024\_doc\_deltas.md

Additional key\_outputs entries are allowed, but these bindings are the closure minimum.

EPIC-025 binding authority note.

- The authoritative binding set for EPIC-025 is recorded in `audit/EPIC-025_MANIFEST.json`.  
- For EPIC-025, the close-pack manifest’s `key_outputs` map is the primary binding index for closure artifacts (what ships) and their evidence locations (where the evidence lives).

EPIC-027 binding authority note.

- The authoritative binding set for EPIC-027 is recorded in `audit/EPIC-027_MANIFEST.json`.  
    
- For EPIC-027, the close-pack manifest’s `key_outputs` map is the primary binding index for closure artifacts, their canonical paths-of-record, and the canonical EPIC027 QA root linkage.  
    
- For EPIC-027, `key_outputs` MUST include at least these keys and exact values:  
    
  - `acceptance_map`: `docs/acceptance_map_epic027.json`  
      
  - `token_matrix`: `audit/qa/hde-epic027/token_evidence_matrix.md`  
      
  - `acceptance_map_viability`: `audit/qa/hde-epic027/acceptance_map_viability.log`  
      
  - `qa_step_manifest`: `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
      
  - `close_report`: `audit/EPIC-027_close_report.md`  
      
  - `close_manifest`: `audit/EPIC-027_MANIFEST.json`


- For EPIC-027, the `qa_step_manifest` binding is closure-required and MUST identify the governed QA-root manifest at `audit/qa/hde-epic027/qa_step_logs_manifest.json`, not merely an unbound file present on disk.  
    
- For EPIC-027, the token matrix is the governed ledger that binds the EPIC027 acceptance roster to the reused D1, D3, and D4 evidence families and to the relevant EPIC027 QA-root step logs.  
    
- For EPIC-027, the acceptance-map viability log is the governed viability ledger for the EPIC027 acceptance map and token matrix.  
    
- The Machine Evidence Mirror bindings for the EPIC027 close-pack acceptance-ledger family are:  
    
  - `epic027.acceptance_map` — `docs/acceptance_map_epic027.json`  
  - `epic027.token_matrix` — `audit/qa/hde-epic027/token_evidence_matrix.md`  
  - `epic027.acceptance_map_viability` — `audit/qa/hde-epic027/acceptance_map_viability.log`  
  - `epic027.qa_step_logs_manifest` — `audit/qa/hde-epic027/qa_step_logs_manifest.json`  
  - `epic027.close_report` — `audit/EPIC-027_close_report.md`  
  - `epic027.manifest` — `audit/EPIC-027_MANIFEST.json`

EPIC-028 acceptance-ledger bindings (current-state).

- The governed acceptance-ledger set evidenced for EPIC-028 is:  
  - `docs/acceptance_map_epic028.json`  
  - `audit/qa/hde-epic028/token_evidence_matrix.md`  
  - `audit/qa/hde-epic028/acceptance_map_viability.log`  
- For EPIC-028, the token matrix is the governed ledger that binds the EPIC028 acceptance roster to the corresponding governed evidence families used by the epic.  
- For EPIC-028, the acceptance-map viability log is the governed viability ledger for the EPIC028 acceptance map and token matrix.  
- The Machine Evidence Mirror bindings for this EPIC028 acceptance-ledger set are:  
  - `epic028.acceptance_map` — `docs/acceptance_map_epic028.json`  
  - `epic028.token_matrix` — `audit/qa/hde-epic028/token_evidence_matrix.md`  
  - `epic028.acceptance_map_viability` — `audit/qa/hde-epic028/acceptance_map_viability.log`

EPIC-028 surfaced close-pack binding authority (current-state).

- The surfaced EPIC028 close-pack authoritative pair is `audit/EPIC-028_close_report.md` and `audit/EPIC-028_MANIFEST.json`.  
- For EPIC-028, the surfaced close-pack manifest’s `key_outputs` map is the primary binding index for the already-governed EPIC028 acceptance and QA evidence family.  
- The current surfaced EPIC028 `key_outputs` binding set includes at minimum these governed paths:  
  - `docs/acceptance_map_epic028.json`  
  - `audit/qa/hde-epic028/token_evidence_matrix.md`  
  - `audit/qa/hde-epic028/acceptance_map_viability.log`  
  - `audit/qa/hde-epic028/qa_step_logs_manifest.json`  
  - `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`  
  - `audit/qa/hde-epic028/checks/po-010/final_summary.txt`  
- For EPIC-028, the close-pack MAY use `audit/qa/hde-epic028/checks/po-010/final_summary.txt` as the closure-relevant repo-supported completion anchor when that artifact is the governed QA artifact bound by the surfaced provenance bundle for the run.  
- The current EPIC028 qa-step manifest pair remains a governed closure-support artifact and, when surfaced in the close-pack binding set, MUST remain discoverable in both the Human Evidence Index and the Machine Evidence Mirror.

EPIC-029 acceptance-ledger and surfaced close-pack bindings (current-state).

- The governed acceptance-ledger set evidenced for EPIC-029 is:  
  - `docs/acceptance_map_epic029.json`  
  - `audit/qa/hde-epic029/token_evidence_matrix.md`  
  - `audit/qa/hde-epic029/acceptance_map_viability.log`  
  - `audit/qa/hde-epic029/qa_step_logs_manifest.json`  
- The surfaced EPIC029 close-pack authoritative pair is `audit/EPIC-029_close_report.md` and `audit/EPIC-029_MANIFEST.json`.  
- For EPIC-029, the surfaced close-pack manifest’s `key_outputs` map is the primary binding index for the already-governed EPIC029 acceptance and QA evidence family.  
- The current surfaced EPIC029 binding set includes at minimum:  
  - `docs/acceptance_map_epic029.json`  
  - `audit/qa/hde-epic029/token_evidence_matrix.md`  
  - `audit/qa/hde-epic029/acceptance_map_viability.log`  
  - `audit/qa/hde-epic029/qa_step_logs_manifest.json`  
  - `audit/EPIC-029_close_report.md`  
  - `audit/EPIC-029_MANIFEST.json`  
- For EPIC-029, the current `qa_step_manifest` binding is the closure-support index for the canonical epic-close QA checks captured under the EPIC029 QA root, including:  
  - `audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log`  
  - `audit/qa/hde-epic029/checks/po-precommit/primary.log`  
  - `audit/qa/hde-epic029/checks/po-postcommit/primary.log`

EPIC-029 surfaced close-pack posture (current-state).

- For EPIC-029, `docs/acceptance_map_epic029.json`, `audit/qa/hde-epic029/token_evidence_matrix.md`, `audit/qa/hde-epic029/acceptance_map_viability.log`, `audit/EPIC-029_close_report.md`, and `audit/EPIC-029_MANIFEST.json` now operate as the surfaced close-pack authoritative pair and closure-support ledger set for a final in-epic closure decision.  
- Close-binding readiness for EPIC-029 is supportable from repo evidence when the surfaced evidence family binds all of the following current-state proofs together:  
  - explicit PF09 row-closure proof for `HDE-CONJ009.1`  
  - explicit PF09 row-closure proof for `HDE-CONJ008.1`  
  - environment-closure proof for `HDE-CONJ001.4`  
- For the current EPIC-029 environment-closure proof, `codespaces` is closed by direct runtime validation and `local_dev` is closed by binding-equivalence. No separate local-dev runtime is executed in that evidence pass.  
- The `qa_step_manifest` binding and the canonical epic-close QA checks above remain the governed closure-support index for the EPIC029 acceptance and QA evidence family, but they are no longer sequencing-only once the bound evidence family truthfully records the row-closure and environment-closure proofs above.

HDE-EPIC033 PR-01 acceptance-ledger baseline (current-state).

- The governed PR-01 acceptance-ledger set evidenced for HDE-EPIC033 is:  
  - `docs/acceptance_map_epic033.json`  
  - `audit/qa/hde-epic033/token_evidence_matrix.md`  
  - `audit/qa/hde-epic033/acceptance_map_viability.log`  
  - `audit/docdeltas/hde-epic033_doc_deltas.md`  
  - `audit/qa/hde-epic033/00_meta/doc_deltas.md`  
- The HDE-EPIC033 PR-01 token evidence matrix is a baseline ledger only. It may bind existing registry-valid tokens such as `TESTS_PASS_OK`, `DOC_DELTA_PRESENT_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, and `JSON_CANONICAL_CHECK_OK` when those tokens are already admitted by Governance.  
- The HDE-EPIC033 PR-01 token evidence matrix MUST NOT mint or claim a vendor-v2-specific token by itself.  
- `docs/acceptance_map_epic033.json` may record that HDE-FERM006.1 through HDE-FERM006.4 are completed by the PR and that HDE-FERM007 and HDE-FERM008 are not completed by the PR. That record is acceptance-ledger evidence only and does not itself edit PF09 status rows.  
- If `audit/qa/hde-epic033/00_meta/doc_deltas.md` is present, it MUST remain byte-identical to `audit/docdeltas/hde-epic033_doc_deltas.md` unless a later PF12 entry explicitly permits divergence.  
- Each concrete artifact above MUST have a sibling `.path_proof.txt` transcript when it is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence.  
- The HDE-EPIC033 PR-01 acceptance-ledger baseline is not a close-pack authoritative pair, not formal closeout, not a runtime v2 conformance claim, not an open-rails vendor smoke claim, not a public Reader change, and not AI scope.

HDE-EPIC035 PR-03 acceptance-boundary and evidence-loop current-state artifacts.

These artifacts are governed current-state evidence for HDE-EPIC035 PR-03 evidence-loop closure posture only. They do not by themselves claim QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, or AI scope.

- `docs/acceptance_map_epic035.json`: HDE-EPIC035 PR-03 acceptance map. Canonical JSON. It binds existing registered baseline tokens only and MUST preserve `pf09_scope_not_completed_by_this_pr` or equivalent nonclaim posture when the PR does not complete HDE-FERM008 parent, PF09 status drainage, or epic closeout.  
- `docs/acceptance_map_epic035.json.path_proof.txt`: Required sibling path-proof transcript when the acceptance map is treated as governed evidence.  
- `audit/qa/hde-epic035/token_evidence_matrix.md`: HDE-EPIC035 token-to-evidence matrix. UTF-8 markdown. It MUST distinguish token evidence binding from QA PASS, OPS completion, closeout review, and PF09 drainage.  
- `audit/qa/hde-epic035/token_evidence_matrix.md.path_proof.txt`: Required sibling path-proof transcript when the token-evidence matrix is treated as governed evidence.  
- `audit/qa/hde-epic035/acceptance_map_viability.log`: LF-terminated acceptance-map viability log for the PR-03 evidence-loop closure family.  
- `audit/qa/hde-epic035/acceptance_map_viability.log.path_proof.txt`: Required sibling path-proof transcript when the viability log is treated as governed evidence.  
- `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`: LF-terminated binding log for already-produced OPS-01 evidence. It MUST state that the live vendor action was not rerun by the PR when that is the posture, and MUST preserve no OPS completion, no QA PASS, no PF09 status movement, no epic closeout, no full runtime conformance, no public surface change, no app-side credential ownership, no raw payload persistence, and no AI-scope claims.  
- `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log.path_proof.txt`: Required sibling path-proof transcript when the OPS evidence binding log is treated as governed evidence.  
- `audit/docdeltas/hde-epic035_doc_deltas.md`: HDE-EPIC035 doc-delta surface. UTF-8 markdown. It records later-drain targets and MUST NOT be treated as the PF-canon drain itself.  
- `audit/docdeltas/hde-epic035_doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the doc-delta surface is treated as governed evidence.  
- `audit/qa/hde-epic035/00_meta/doc_deltas.md`: HDE-EPIC035 QA meta doc-delta surface. UTF-8 markdown. It records QA-root doc-delta context and MUST NOT be treated as the PF-canon drain itself.  
- `audit/qa/hde-epic035/00_meta/doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the QA meta doc-delta surface is treated as governed evidence.

HDE-EPIC035 Live QA Pass 1 and qa-16 closeout current-state artifacts.

These artifacts are governed current-state QA evidence for HDE-EPIC035 Live QA Pass 1 and qa-16 closeout-deliverables posture. They do not by themselves perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full HumanDesignAPI v2 runtime conformance, public expansion, raw payload persistence, or AI scope.

- `audit/qa/hde-epic035/qa_step_logs_manifest.json`: HDE-EPIC035 QA step-logs manifest. Canonical JSON. It records check IDs, statuses, primary-log paths, and primary-log path-proof paths when those fields are produced by the plan or harness.  
- `audit/qa/hde-epic035/qa_step_logs_manifest.json.path_proof.txt`: Required sibling path-proof transcript when the QA step-logs manifest is treated as governed evidence.  
- `audit/qa/hde-epic035/checks/<check_id>/primary.log`: Check-scoped primary log pattern for HDE-EPIC035 selected checks, including `step-0b-doc-delta-capture` and `po-001` through `po-014` when those checks are executed. Each concrete primary log MUST follow the normal PF12 primary-log and path-proof rules.  
- `audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log`: HDE-EPIC035 qa-16 closeout-deliverables primary log. Non-empty UTF-8 text. It records closeout assembly evidence and MUST preserve nonclaims when it is treated as governed evidence.  
- `audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt`: Required sibling path-proof transcript when the qa-16 primary log is treated as governed evidence.  
- `audit/qa/hde-epic035/00_meta/discovery_artifact.md`: HDE-EPIC035 discovery artifact. Non-empty UTF-8 markdown when present. It records repo-locus grounding and retained OPS-evidence inspection posture.  
- `audit/qa/hde-epic035/00_meta/discovery_artifact.md.path_proof.txt`: Required sibling path-proof transcript when the discovery artifact is treated as governed evidence.  
- `audit/qa/hde-epic035/00_meta/qa_rca_doc_delta_summary.md`: HDE-EPIC035 QA RCA and Doc Delta summary artifact. Non-empty UTF-8 markdown when present. It supports QA closeout review only and MUST NOT be treated as PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.  
- `audit/qa/hde-epic035/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`: Required sibling path-proof transcript when the QA RCA and Doc Delta summary is treated as governed evidence.

HDE-EPIC036 PR-02, Live QA, governed evidence, and closeout-support current-state artifacts.

These artifacts are governed current-state evidence for HDE-EPIC036 route-policy, evidence-loop binding, Live QA, governed-evidence-gate, and closeout-support posture. They do not by themselves claim OPS completion, PF09 status movement, HDE-FERM008 parent Done, PO closeout, board update, merge action, PF edit, full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, or AI scope.

PR-02 evidence-loop artifacts.

- `docs/acceptance_map_epic036.json`: HDE-EPIC036 PR-02 acceptance map. Canonical JSON. It binds existing registered baseline tokens only and MUST preserve HDE-FERM008.6 route-policy and evidence-loop scope, no OPS execution for PR-02, no QA PASS claim unless separately proven, no PF09 status movement, no HDE-FERM008 parent Done, no epic closeout, no full runtime conformance, and no public or AI scope claims.  
- `docs/acceptance_map_epic036.json.path_proof.txt`: Required sibling path-proof transcript when the acceptance map is treated as governed evidence.  
- `audit/qa/hde-epic036/token_evidence_matrix.md`: HDE-EPIC036 token-to-evidence matrix. UTF-8 markdown. It MUST distinguish token evidence binding from QA PASS, OPS completion, closeout review, and PF09 drainage.  
- `audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt`: Required sibling path-proof transcript when the token-evidence matrix is treated as governed evidence.  
- `audit/qa/hde-epic036/acceptance_map_viability.log`: LF-terminated acceptance-map viability log for the PR-02 evidence-loop family.  
- `audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt`: Required sibling path-proof transcript when the viability log is treated as governed evidence.  
- `audit/docdeltas/hde-epic036_doc_deltas.md`: HDE-EPIC036 doc-delta surface. UTF-8 markdown. It records later-drain targets and MUST NOT be treated as the PF-canon drain itself.  
- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the doc-delta surface is treated as governed evidence.  
- `audit/qa/hde-epic036/00_meta/doc_deltas.md`: HDE-EPIC036 QA meta doc-delta surface. UTF-8 markdown. It records QA-root doc-delta context and MUST NOT be treated as the PF-canon drain itself.  
- `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the QA meta doc-delta surface is treated as governed evidence.

Live QA and route-policy check artifacts.

- `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`: LF-terminated open-rails route-policy log. It records the bounded open-rails QA observation for the `bg:resolve --source vendor` route-policy surface and MUST preserve unsupported-runtime nonclaim, redacted base URL, redacted auth posture, no raw payload persistence, and no full runtime conformance claims.  
- `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`: Required sibling path-proof transcript when the live-route-policy log is treated as governed evidence.  
- `audit/qa/hde-epic036/qa_step_logs_manifest.json`: HDE-EPIC036 QA step-logs manifest. Canonical JSON. It records check IDs, statuses, primary-log paths, and primary-log path-proof paths when those fields are produced by the plan or harness.  
- `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt`: Required sibling path-proof transcript when the QA step-logs manifest is treated as governed evidence.  
- `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log`: HDE-EPIC036 governed-evidence-gates primary log. Non-empty UTF-8 text. It records governed evidence checks, canonical JSON checks, targeted tests, evidence-index checks, mirror checks, hash checks, LF checks, and token-support posture when those checks are executed.  
- `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.path_proof.txt`: Required sibling path-proof transcript when the qa-13 primary log is treated as governed evidence.  
- `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`: HDE-EPIC036 closeout-deliverables primary log. Non-empty UTF-8 text. It records closeout assembly evidence and MUST preserve nonclaims when it is treated as governed evidence.  
- `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.path_proof.txt`: Required sibling path-proof transcript when the qa-14 primary log is treated as governed evidence.

Closeout-support and remediation-routing artifacts.

- `audit/qa/hde-epic036/00_meta/discovery_artifact.md`: HDE-EPIC036 discovery artifact. Non-empty UTF-8 markdown when present. It records repo-locus grounding and retained evidence inspection posture.  
- `audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt`: Required sibling path-proof transcript when the discovery artifact is treated as governed evidence.  
- `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`: HDE-EPIC036 QA RCA and Doc Delta summary artifact. Non-empty UTF-8 markdown when present. It supports QA closeout review only and MUST NOT be treated as PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.  
- `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`: Required sibling path-proof transcript when the QA RCA and Doc Delta summary is treated as governed evidence.  
- `audit/qa/hde-epic036/00_meta/hde_epic036_po011_po012_qa13_qa14_remediation_evidence_addendum.md`: HDE-EPIC036 remediation evidence addendum. Non-empty UTF-8 markdown when present. It records routing receipt posture for non-QA-root governed evidence refreshes used by final PASS-grade QA evidence and MUST distinguish PR routing from Moon Loop, OPS execution, PF09 movement, PO closeout, full runtime conformance, public expansion, raw payload persistence, and AI scope.  
- `audit/qa/hde-epic036/00_meta/hde_epic036_po011_po012_qa13_qa14_remediation_evidence_addendum.md.path_proof.txt`: Required sibling path-proof transcript when the remediation evidence addendum is treated as governed evidence.

Titles-only routing rule

Rule. References are by title only. Do not include version numbers in prose. Do not restate bytes owned by other specs.

Math: scoring and thresholds; deterministic preimage (idempotence) recipe.

Referenced by title only in HDE-Math-Spec. No arithmetic or preimage bytes are restated here.

Governance / CLI: Reader transport (headers, conditional delivery, error model), writers and errors posture, and vendor request shaping plus typed mapping.

Referenced by title only in HDE-Governance and HDE-CLI-API-Vendor-Ref. No transport or vendor bytes are restated here.

Architecture: component boundaries (engine, adapter, presenter) and single-homes/single-emitter boundary.

Referenced by title only in HDE-Architecture. No architectural prose is duplicated here.

Narratives routing reminder: narratives transport and example payload bytes are out of scope for this document and are routed by title to HDE-Governance (A7) and HDE-CLI-API-Vendor-Ref.

## **3\. Catalog Validation & Integrity \[Required-Now\]**

## **3.1 JSON Schema validation**

Every catalog file MUST pass its owning JSON Schema. No extra keys. No missing required fields.

### **Scope**

“Catalog file” means any JSON artifact that enumerates a closed or structured domain used by the engine.

“Owning JSON Schema” is the single schema that defines the structure, types, and constraints for that catalog. Reference it by title and path only.

### **Normative rules**

* Each catalog MUST validate against its owning schema with no errors.  
* All required properties defined by the schema MUST be present. None may be omitted.  
* No additional properties are allowed unless the schema explicitly permits them at that object level.  
* Property types MUST match exactly (e.g., integer ≠ number; strings are not numeric).  
* All enums define closed sets. Values outside the set are invalid.  
* Arrays that represent sets MUST contain no duplicates. If uniqueness cannot be expressed in JSON Schema, a companion check MUST enforce it.  
* For arrays of objects used as sets, the schema MUST declare an identity key for deduplication and ordering. If an object-array is declared a set without an identity rule, that is a schema error; enforce via a companion check until the schema is corrected.  
* String identifier fields such as id MUST be non-empty. Charset and maximum length are governed in §0.5; until formally pinned, use the default guidance ^\[a-z0-9\_\]+$ (case-sensitive).  
* Numeric ranges, if present, MUST be enforced exactly as defined in the schema.  
* Seeds checksum (catalog/magic10\_seeds.json): checksum\_sha256 MUST equal the sha256 of the seed’s canonical serialized body; enforce via a companion check (see §2.7, §4).

Schema validation concerns data shape and values. Serialization rules (canonical JSON, key ordering, single trailing LF) are handled by the Artifact Serialization Policy (§4).

Identity-code constraints: where IDs must be normalized (e.g., channel identity), the schema SHOULD encode the constraint (min→max, zero-padded NN-NN, ASCII). Example (informative): channel\_id matches the min-first zero-padded pattern and domain 01..64-01..64; arrays-as-sets are ASCII-sorted by channel\_id.

### **Schema hygiene**

* Each schema MUST include $schema and SHOULD include $id.  
* Draft: 2020-12; $schema MUST be [https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema). $id MUST be a stable repo title-path for the catalog (e.g., schemas/ums.channel.v1.json) \- not an external URL.  
* Schemas SHOULD set additionalProperties: false at closed object levels, and allow additional properties only where intended.  
* Cross-catalog references that a schema cannot express (e.g., membership in another catalog’s closed set, degree/multiplicity invariants) MUST be enforced by companion checks (see §3.2–§3.3 and Integrity CI in §8.2).  
* Where identity codes are constrained by format (e.g., zero-padded numeric identifiers and min-first orientation), the schema SHOULD encode that constraint (pattern/range); otherwise a companion check MUST enforce it.

### **CI enforcement**

* Validation MUST run for every catalog locally and in CI. Any failure is a hard stop.  
* When a catalog or its schema changes, validation MUST re-run and succeed in the same change.  
* Uniqueness, cross-reference, ordering, and arrays-as-sets rules that exceed JSON Schema’s native capabilities MUST be enforced by companion checks.  
* Run checks under LC\_ALL=C per §4.3.

### **Acceptance hints**

* CATALOG\_SCHEMA\_OK  
* CATALOG\_NO\_ADDITIONAL\_PROPS\_OK  
* CATALOG\_ENUM\_DOMAIN\_CLOSED\_OK  
* ARR\_SET\_NO\_DUPLICATES\_OK  
* ARR\_SET\_IDENTITY\_DECLARED\_OK (when arrays of objects are used as sets)  
* SCHEMA\_HYGIENE\_OK  
* SCHEMA\_ID\_STABLE\_OK (repo title-path in $id)

## **3.2 Graph coherence checks (topology)**

Topology-level integrity rules across Centers, Gates, and Channels.

### **Scope**

Inputs. The Centers catalog, Gates catalog, and Channels catalog from §2.1.

Derived maps used by checks.

* center\_of\_gate\[g\] from the Gates catalog (each gate’s center)  
* gates\_of\_channel\[ch\] \= \[g\_a, g\_b\] from the Channels catalog  
* centers\_of\_channel\_derived\[ch\] \= { center\_of\_gate\[g\_a\], center\_of\_gate\[g\_b\] }

### **3.2.1 Channel degree and identity (channel ↔ exactly two gates)**

#### **Cardinality**

* Each channel MUST reference exactly two gate IDs.  
* The two gate IDs MUST be present in the Gates catalog and MUST be distinct. A channel MUST NOT list the same gate twice.

#### **Identity and uniqueness \[RESOLVED\]**

Canonical identity. A channel’s identity is the ASCII-ascending, zero-padded gate pair encoded as "-", where lowGate/highGate are the two referenced gate IDs normalized to two digits (01..64) and ordered lexicographically as strings (see §2.1, Channels). (Schema pattern reference: ^(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])$.)

Uniqueness. No two channels may share the same canonical identity. If the same identity appears with different element bytes, fail closed.

#### **Arrays-as-sets coupling**

Any array that lists channels as a set (for example, a top-level channels list) MUST be deduplicated by the canonical identity above and MUST be ASCII-sorted by that identity (see §4.2). Any duplicate identity or out-of-order identity is a validation error.

#### **CI acceptance hints**

* TOPOLOGY\_CHANNEL\_DEGREE\_2\_OK  
* ARR\_SET\_NO\_CONFLICTS\_OK  
* ARR\_SET\_ASCII\_SORT\_OK  
* CATALOG\_ORIENTATION\_CANON\_OK  
* TOPOLOGY\_COHERENCE\_OK

### **3.2.2 Gate↔center and channel↔center consistency**

* Every gate MUST reference exactly one valid center ID from the Centers catalog (domain closure).  
* For each channel, compute centers\_of\_channel\_derived\[ch\] \= { center\_of\_gate\[g\_a\], center\_of\_gate\[g\_b\] }.  
* If the Channels catalog stores an explicit center field (or fields), those values MUST equal centers\_of\_channel\_derived\[ch\].  
* There is no inherent requirement that the two centers of a channel differ; enforce distinctness only if a separate rule in this document or the owning schema declares it.

#### **CI acceptance hints**

* TOPOLOGY\_CENTER\_CONSISTENCY\_OK  
* TOPOLOGY\_DOMAIN\_CLOSED\_OK  
* XREF\_MEMBERSHIP\_OK

### **3.2.3 No orphans: every referenced ID exists**

* Every center ID referenced by any gate MUST exist in the Centers catalog.  
* Every gate ID referenced by any channel MUST exist in the Gates catalog.  
* There MUST be zero dangling references across all three catalogs. Any missing target is a hard validation error.

#### **CI acceptance hints**

* TOPOLOGY\_NO\_ORPHANS\_OK

### **3.2.4 Degree vectors (optional)**

Optional invariants that assert expected degree counts; enforce only when explicitly declared by the owning spec or a referenced proof artifact.

#### **Scope**

Inputs: Centers, Gates, Channels catalogs from §2.1.

Graph model: gate\_degree\[g\] \= count of channels that reference gate g.

Source of truth. If degree expectations are provided (e.g., in a field in the Gates schema or a separate declared artifact listed in the pack), they govern the checks below; otherwise this subsection is not applicable.

#### **Normative rules (apply only when expectations are declared)**

* Build the observed vector: for each gate g, compute gate\_degree\[g\].  
* Compare to the declared expected vector.  
* Every gate that appears in the expected vector MUST appear in the observed vector with the same integer value.  
* If the expected vector declares a closed key set, the observed vector MUST have exactly that key set.  
* All degree values MUST be non-negative integers. Any mismatch is a validation error.

#### **Notes**

* You may declare only a subset of gates; in that case, enforce equality only for the declared subset.  
* Encode any special-case adjustments (e.g., temporary exclusions) in the declared artifact rather than prose.

#### **CI enforcement**

Run this check whenever Centers, Gates, Channels, or the declared degree-vector artifact changes. Fail on first mismatch.

#### **Acceptance hints**

* DEGREE\_VECTORS\_DECLARED\_OK  
* DEGREE\_VECTORS\_MATCH\_OK  
* DEGREE\_VECTORS\_NONNEG\_INT\_OK

### **3.2.5 Distinguished sets (optional)**

Optional invariants that declare named, frozen subsets of channels or gates. Enforce only when a set is declared.

#### **Scope**

Inputs: Centers, Gates, Channels catalogs from §2.1.

“Distinguished set” means a named subset, e.g., Talk Ladder, Narrative Throat, or Direct Motor→Throat.

Source of truth. The set definition MUST be provided by a declared source (e.g., a dedicated catalog, a section in a proof artifact, or a field in a governed catalog) and referenced by title/path in §8.3.

#### **Declaration requirements — each distinguished set MUST declare:**

* name (string)  
* type with value "channels" or "gates"  
* members (array treated as a set per §4.2)  
* optional metadata (e.g., rationale, provenance), if needed

#### **Identity**

* For type: "gates", identity is the gate ID.  
* For type: "channels", identity is the canonical channel identity "-" (§3.2.1).

#### **Normative rules (apply only when a set is declared)**

* Domain closure: every member MUST belong to the relevant closed domain (see §3.3).  
* No duplicates: members MUST be deduplicated by identity; if the same identity appears with different element bytes, fail closed.  
* Ordering: members MUST be ASCII-ascending by identity (arrays-as-sets, §4.2).  
* Cross-consistency: for type: "channels", both gate IDs MUST resolve to valid gates; derived centers MUST be consistent with §3.2.2.  
* Closed vs partial sets: If a set is declared closed, the members list is authoritative and MUST be complete; otherwise, validate membership and set semantics only.

#### **CI enforcement**

Validate domain closure, deduplication, ordering, and topology cross-checks for every declared set; fail on the first violation.

#### **Acceptance hints**

* DISTINGUISHED\_DECLARED\_OK  
* DISTINGUISHED\_DOMAIN\_CLOSED\_OK  
* DISTINGUISHED\_NO\_CONFLICTS\_OK  
* DISTINGUISHED\_ASCII\_SORT\_OK  
* DISTINGUISHED\_TOPOLOGY\_CONSISTENT\_OK

### **3.2.6 Integration & multiplicity invariants (loader checks) \[NEW | NORMATIVE\]**

#### **Scope**

Inputs: Centers, Gates, Channels catalogs from §2.1; the graph model defined at the top of §3.2.

#### **Normative rules**

* Integration degree test (gate graph). Only gates 10, 20, 34, 57 have degree \= 3 (each participates in three distinct channels). All other gates have degree \= 1\. Fail closed if violated.  
* Center-pair multiplicity. When channels are reduced to unordered center pairs, the per-pair counts MUST sum to 36 across the wheel. The expected multiplicities MUST be encoded in a governed artifact or inlined as a closed list in catalog/channels.json and listed in the Evidence Index/machine mirror. Fail closed on mismatch.  
* Simple vs multigraph. At channel level, the graph is simple (no duplicate edges after canonical NN-NN normalization). At center level, it is a multigraph (parallel edges allowed) and is used for analytics only; mechanics remain per channel.

#### **Evidence hooks (titles/paths only)**

* audit/gates/topology/degree\_check.log — observed degree map and pass/fail  
* audit/gates/topology/multiplicity\_vector.log — observed center-pair multiplicities and pass/fail

#### **CI acceptance hints**

* TOPOLOGY\_INTEGRATION\_DEGREE\_OK  
* TOPOLOGY\_CENTER\_MULTIPLICITY\_OK  
* TOPOLOGY\_SIMPLE\_GRAPH\_OK

## **3.3 Domain closure & enums**

All IDs and enum values MUST come from the catalog’s closed domain. Unknowns are rejected.

### **Scope**

Applies to all closed-domain catalogs in §2 (for example, Centers, Gates, Channels, Authorities, Profiles) and to any artifact that references them (for example, presets, invariants).

Also applies to the Magic-10 category IDs and the viewer preferences key set from §§2.3–2.4.

### **Normative rules**

* Closed domain per release. For a given release, each catalog defines the complete set of valid IDs or enum values.  
* Exact membership. Every referenced ID or enum value MUST be a member of the owning catalog’s set. Any value not present is invalid.  
* No coercion. Do not coerce, normalize, or substitute unknown values. Treat them as hard validation errors.  
* Case & charset (RESOLVED). IDs are case-sensitive, ASCII, and MUST match the regex ^\[a-z0-9\_\]+$ (no spaces).  
* Aliases policy (RESOLVED). Input-only aliases may be accepted at ingestion (per alias catalogs); all outputs are canonical. Alias catalogs, when present, live separately and are validated independently.  
* Append/retire policy. Renames and deletions are discouraged; additions require explicit review and may require a release\_id bump and catalog version note.  
* Normative order. When order is consumed, it is defined by the owning catalog. Otherwise, treat sets as unordered; programmatic lists MUST sort in ASCII ascending for reproducibility.

### **Specific applications**

Magic-10 categories (§2.3). Only the ten category IDs listed are valid. If any consumer treats order as normative, do not reorder without a Doc-Delta.

Viewer preferences (§2.4). The preferences object key set MUST equal the ten category IDs. Unknown keys are invalid.

Magic-10 seeds (§2.7). Exactly ten entries (one per category); key set MUST match the ten category IDs; admin\_only MUST be true for all entries; checksum\_sha256 MUST match the canonical serialized seed body (see §3.1); any change is a frozen-input change and may require a release\_id bump (see §6).

#### **Topology catalogs (§2.1).**

* Centers. Closed set: head, ajna, throat, g\_center, ego, spleen, solar\_plexus, sacral, root.  
* Gates. A gate’s center MUST be a member of the Centers set.  
* Channels. Each channel MUST reference two gate IDs from Gates and use the canonical identity NN-NN (zero-padded, min-first). Any other format is invalid.

### **Validation mechanics**

* Prefer JSON Schema enum for explicit closed sets where feasible.  
* When values are references to another catalog, implement a cross-reference check that builds the owner set and validates membership for every reference.  
* Where JSON Schema cannot express the constraint, add a companion validation step that fails on the first unknown.

### **CI enforcement**

* Run domain-closure checks on every change to a catalog or any artifact that references it.  
* Treat any unknown ID or enum value as a hard failure.  
* When a closed set changes, re-run all dependent validations in the same change.  
* Execute under LC\_ALL=C per §4.3.

### **Acceptance hints**

* CATALOG\_DOMAIN\_CLOSED\_OK  
* CATALOG\_NO\_UNKNOWN\_IDS\_OK  
* PREFS\_KEYSET\_10\_OK  
* MAGIC10\_DOMAIN\_CLOSED\_OK  
* XREF\_MEMBERSHIP\_OK  
* ALIASES\_INPUT\_ONLY\_OK  
* ID\_CHARSET\_POLICY\_OK

## **3.4 Narratives composer response schema \[Required-Now\]**

Schema path: schemas/narratives.composer.response.v1.json

Valid shapes (reject unknown keys).

### **Text variant**

* composition\_id (ASCII, 8..128)  
* fragment\_ids (array, minItems: 1\)  
* pack\_sha (lowercase 64-hex)  
* policy\_reason (enum: "conflict")  
* text (string, maxLength: 300, MUST NOT contain "\\r")

### **Suppressed variant**

Same as Text variant without text (suppression \= missing body text)

### **Serialization & validation**

Canonical JSON applies to any stored artifacts (UTF-8, sorted keys, compact, exactly one LF; no BOM). The schema must reject any fields not listed above and any CR characters ("\\r") inside text.

### **Routing (titles-only)**

Transport headers, A7 rules, and suppression policy semantics: PF04/PF05.

### **Persistence profile (titles-only)**

Any admin persistence of narrative text MUST honor the ≤300/no-CR limits and identity fields (composition\_id, fragment\_ids, pack\_sha, release\_id). Storage/retention is routed to Glow Infrastructure (names-only). Logging/privacy posture (keys-only; never log text) is routed to PF04.

## **4\. Artifact Serialization Policy**

Canonical bytes for all pack files and for the manifest.

### **Scope**

Applies to all pack files listed in this document and to the pack manifest. The rules below define the exact byte form used for hashing and equality checks. These rules also apply to JSON evidence artifacts listed in Appendix D (so evidence is reproducibly comparable). Operational logs are out of scope for canonicalization; they must remain keys-only per Governance §7.1 and are not required to be canonical JSON.

### **Non-goals**

This section does not restate any schema content, arithmetic, or transport behavior. It only defines how valid JSON is serialized to bytes.

### **Canonical JSON rules (normative)**

* Encoding: UTF-8 without BOM.

* Whitespace: compact (no pretty/indent), no trailing spaces, exactly one trailing newline LF (\\n) at end of file.

* Objects: keys are emitted in ASCII ascending order at every object level.

* Numbers: encoded as JSON numbers (not strings). NaN/Infinity disallowed.

* Booleans/null: lowercase JSON literals.

* Arrays:

  * If the array represents a set, it MUST be de-duplicated and ASCII-sorted by its identity rule (see §3.2/§3.3).

  * If the array is ordered by spec, preserve the schema-declared order; do not re-sort.

* JSONL artifacts (records-only): one canonical JSON object per line; no blank lines; each line obeys all canonical JSON rules above (sorted keys, compact); the file ends with exactly one trailing LF.

* Escapes: JSON string escaping per RFC 8259; no non-canonical escape variants.

* Locale: all canonicalization and comparisons run under LC\_ALL=C, LANG=C, TZ=UTC.

* Capture env pins: header/body snapshot jobs and canonicalization checks MUST run with the same env pins: LC\_ALL=C, LANG=C, TZ=UTC.

### **Determinism & hashing**

* All governed pack files’ sha256 values in the manifest are computed over their canonical bytes.

* The release\_id is the sha256 of the canonical bytes of catalog/manifest.json (see §6.1).

* Any byte that violates the rules above invalidates the stored digest and must fail checks.

### **CI enforcement**

* Canonicalization check must re-serialize each governed JSON and byte-compare to the on-disk file.

* Two-run identity: two consecutive canonical dumps of the same object graph must produce identical bytes.

* Fail closed on: unsorted keys, missing LF, extra whitespace, BOM, duplicated set entries, locale drift, or number/string mismatches.

### **Acceptance hints (titles-only)**

* DET\_SERIALIZER\_OK

* TWO\_RUN\_IDENTITY\_OK

* JSON\_CANONICAL\_CHECK\_OK

* MANIFEST\_FILE\_EQ\_CANON\_OK

* JSONL\_RECORDS\_CANON\_OK

* ENV\_LC\_ALL\_C\_OK

§§5–8 reference this policy without redefining it.

## **4.1 Canonical JSON rules**

All artifacts covered by §4 MUST be encoded as canonical JSON. The same semantic content MUST always yield identical bytes.

### **Encoding and file boundary**

* Text encoding: UTF-8.

* No BOM.

* File terminator: exactly one line feed at end of file (LF, byte 0x0A).

* No carriage returns (0x0D) and no trailing spaces or tabs.

### **Object key ordering**

For every JSON object, keys MUST be emitted in strict ASCII ascending order. Ordering is recursive: apply the same rule to all nested objects. Arrays preserve their input order; only object member order is canonicalized.

### **Whitespace and separators**

* Compact form only. No pretty printing.

* Object member separator is a comma , with no surrounding spaces.

* Name–value separator is a colon : with no surrounding spaces.

* Example shape:

  * {"a":1,"b":\[true,false\],"c":{"d":2}}

### **Strings**

* Delimiter: double quotes.

* Content MUST be valid UTF-8.

* Escape only what JSON requires: ", , and control characters U+0000..U+001F (use the shortest legal escape such as \\n, \\t, or \\u00XX).

* Do not escape non-ASCII letters; emit them as UTF-8.

* Disallow unpaired surrogates; strings MUST be well-formed Unicode.

### **Numbers**

* Follow the owning schema’s types.

* Integers: base-10, no leading zeros, no plus sign, no decimal point, no exponent.

* Non-integers: not permitted in pack artifacts. If a future schema requires non-integer quantities, they MUST be represented as exact strings (or exact integer encodings) with a Math-defined rounding/precision policy (see §4.3).

### **Booleans and null**

* Booleans are true or false (lowercase).

* null only where explicitly allowed by the schema.

### **Field names**

Field names follow the schema. If unspecified, prefer lower\_snake ASCII for new fields to keep key ordering unambiguous.

### **Determinism checks (normative)**

* Re-serializing the same in-memory value MUST produce byte-for-byte identical output.

* Canonicalization MUST NOT reorder arrays or change values.

* Any byte that violates the rules above invalidates the artifact.

### **JSONL artifacts (records-only)**

* Structure: exactly one JSON object per line; no array wrapper.

* Line canon: each line is canonical JSON (sorted keys, compact separators).

* File boundary: end with exactly one LF; no blank lines before EOF.

* Purpose: used by the machine Evidence Index and other records-only evidence; see §8.

### **Acceptance hints**

* CANON\_JSON\_UTF8\_OK

* CANON\_JSON\_SORTED\_KEYS\_OK

* CANON\_JSON\_COMPACT\_OK

* CANON\_JSON\_SINGLE\_LF\_OK

* CANON\_JSON\_NO\_BOM\_OK

* CANON\_JSON\_IDENTITY\_OK

## **4.2 Arrays-as-sets discipline**

Deduplicate by identity. Sort ASCII. On value conflict, fail closed.

### **When this applies**

Any array that a schema defines as a set rather than an ordered list.

Typical cases include top-level catalog entries, lists of IDs, and composite references declared as sets.

The owning schema MUST explicitly mark which arrays are treated as sets (and, where possible, encode the identity rule).

### **Identity**

* Scalars: identity is the scalar value itself.

* Objects: identity is the value of the field the schema designates as the identity key (for example id).

* Composite identities: if identity is a tuple, the schema MUST define a canonical projection to a single string (e.g., normalize field order and join with a fixed delimiter).

* If no identity rule is defined for an object array that is treated as a set, that is a schema error to resolve (enforce via a companion check until corrected).

### **Normalization pins (identity projection)**

The projected identity string MUST be canonical and exactly match on-disk bytes for comparison/sort (no trimming, case changes, or locale transforms).

Where the schema mandates a normalized representation, the catalog MUST store that form.

Example (channels): channel\_id \= `"<a>-<b>"` with zero-padded 01..64, min-first (e.g., 31-07, 57-20/57-34/10-57).

### **Deduplication**

* Build a map identity → element.

* If the same identity appears multiple times with byte-identical elements, keep a single instance.

* If the same identity appears with different element values, that is a conflict → fail closed (companion check should point to the first divergent field).

### **Ordering**

After deduplication, arrays-as-sets MUST be ASCII ascending by the identity string (byte-wise, case-sensitive, locale-independent; treat LC\_ALL=C as the reference).

Producers MUST write arrays in this order; validators reject out-of-order sets.

### **Acceptance hints**

* ARR\_SET\_IDENTITY\_DECLARED\_OK

* ARR\_SET\_NO\_DUPLICATES\_OK

* ARR\_SET\_NO\_CONFLICTS\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* ARR\_SET\_PROJECTION\_CANON\_OK

## **4.3 Locale & determinism pins**

LC\_ALL=C. No wall clock. No randomness. No floats in artifact generation.

### **Scope**

Applies to every step that produces canonical pack files or the pack manifest.

### **Locale and environment**

* Set LC\_ALL=C for all generation and verification steps.

* Recommended pins: LANG=C and TZ=UTC to avoid host variance.

* Any collation, case-folding, or string comparison used during generation MUST be performed under this locale.

### **Time sources**

Artifact generation MUST NOT read the wall clock.

No timestamps, date strings, or time-derived fields may be computed during generation.

If a timestamp appears in surrounding evidence, it MUST come from release metadata or CI context and MUST NOT influence artifact bytes.

### **Randomness and process nondeterminism**

No calls to RNGs or seed-dependent libraries.

Do not depend on memory addresses, iteration order of non-deterministic structures, or any nondeterministic API.

Hash-order or interpreter randomization MUST NOT affect outputs; canonical JSON ordering applies.

### **Floating point prohibition**

Artifact generation MUST NOT use floating-point arithmetic.

Outputs MUST NOT contain floating-point numbers.

If a future schema requires non-integer quantities, represent them as exact integers or exact strings with a Math-defined encoding and rounding policy.

### **Determinism requirements**

Two runs over the same inputs and code MUST produce byte-for-byte identical artifacts.

Generation MUST be pure with respect to inputs declared by this document and the owning schemas.

### **CI enforcement**

* Assert LC\_ALL=C in the environment at generation and at checks.

* Run a two-run identity check over the full pack and manifest.

* Grep/audit for wall-clock calls, RNG usage, and float emission in the generation path. Any hit is a hard failure.

### **Acceptance hints**

* ENV\_LC\_ALL\_C\_OK

* NO\_WALL\_CLOCK\_OK

* NO\_RANDOMNESS\_OK

* NO\_FLOATS\_IN\_GEN\_OK

* TWO\_RUN\_IDENTITY\_OK

# 5\. Freeze-Pack Manifest (catalog/manifest.json) \[Required-Now\]

## **5.1 Manifest file shape \[Required-Now\]**

Purpose. Canonical JSON document that lists every frozen input with {path, sha256, size} and top-level metadata. The canonical bytes of this file determine release\_id (see §6).

Top-level object (no extras).

* root — string. Fixed: "catalog/".

* version — string. Semver for the catalog pack (not app version).

* built\_at\_utc — string. UTC ISO-8601 timestamp (YYYY-MM-DDThh:mm:ssZ).

* files — array of entry objects.

No other top-level members are allowed. Self-exclusion: the root manifest MUST NOT list itself (catalog/manifest.json). Listing catalog/narratives/manifest.json is required (see “Frozen inputs completeness” and §2.8).

Files\[\] as a set (arrays-as-sets policy).

Treat files as a set keyed by path. Deduplicate by path, ASCII-sort by path (byte-wise, locale-independent), and fail closed on conflicting duplicates. Producers MUST emit files in ASCII ascending path order. Canonical JSON applies everywhere (UTF-8, no BOM; sorted keys; compact separators; exactly one trailing LF).

Frozen inputs completeness (normative).

files\[\] MUST enumerate all frozen inputs for the release. This includes, at minimum, the four narratives pack members under catalog/narratives/\* and the narratives pack manifest at catalog/narratives/manifest.json (see §2.8 Narratives pack). Missing any required narratives entry is an error.

Entry object (exactly three fields).

* path — string. POSIX path relative to the pack root (root \== "catalog/"). Do not include the "catalog/" prefix. No absolute paths; no ..; no //. Case-sensitive. Path charset/length limits per §0.5 (default: ^\[a-z0-9\_./-\]+$, max 256 bytes).

* sha256 — string. 64-char lowercase hex of the file’s canonical bytes (per §4 policy).

* size — integer. Byte length of the same canonical bytes (non-negative; fits in signed 64-bit).

Additional properties. Not allowed. Each entry MUST contain exactly path, sha256, size.

Ordering (producer requirement).

files\[\] MUST be ASCII ascending by path (byte-wise; locale-independent). Producers MUST emit in this order.

Validation rules (summary).

* Every listed path MUST resolve to an existing file under the pack root (catalog/).

* For each entry, recompute SHA-256 over the file’s canonical bytes; it must match sha256.

* Recompute byte length; it must match size.

* Unknown fields or missing required fields are errors.

* Duplicate path values with differing sha256 or size are conflicts → error.

* Narratives completeness: catalog/narratives/manifest.json and the four narratives members under catalog/narratives/\* MUST be present (see §2.8); omission is an error.

* The manifest itself MUST be canonical JSON on disk (UTF-8, sorted keys, compact, exactly one LF).

Example (illustrative only).

{"root":"catalog/","version":"1.0.0","built\_at\_utc":"2025-10-28T00:00:00Z","files":\[{"path":"centers.json","sha256":"0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef","size":1234},{"path":"gates.json","sha256":"abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789","size":5678},{"path":"narratives/manifest.json","sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","size":321},{"path":"narratives/templates.json","sha256":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","size":654}\]}

(The example is non-normative and abbreviated; real catalogs will contain additional governed files.)

CI enforcement (minimum).

* PACK\_ROOT\_PINNED\_OK

* MANIFEST\_TOP\_LEVEL\_OBJECT\_OK

* MANIFEST\_FILES\_ARRAY\_OK

* MANIFEST\_ENTRY\_FIELDS\_OK

* MANIFEST\_SHA256\_HEX64\_OK

* MANIFEST\_SIZE\_MATCH\_OK

* MANIFEST\_PATH\_ASCII\_SORT\_OK

* MANIFEST\_NO\_DUP\_PATHS\_OK

* MANIFEST\_FILE\_EXISTS\_OK

* MANIFEST\_CANON\_JSON\_OK

* PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK

(Narratives pack-specific acceptance lives in §2.8: NARR\_PACKS\_IN\_MANIFEST\_OK, NARR\_PACK\_MANIFEST\_OK, NARR\_PACK\_IDENTITY\_OK, and NARR\_PACKS\_CANONICAL\_JSON\_OK.)

## **5.2 Hash input**

Arrays-as-sets report (governed proof artifact).

The arrays-as-sets canonicalization report is a governed proof artifact at `artifacts/canonical/arrays_as_sets_report.log`.

The canonical generator entrypoint is `tools/evidence/generate_arrays_as_sets_report.py` (titles-only; no runbook).

The report may explicitly record the already-canonical case (for example, a note stating that raw equals normalized). The already-canonical case is conforming and must not be treated as an error by consumers of the report.

Canonical bytes of the artifact (per §4), not raw editor formatting.

Normative rule.

Compute sha256 over the artifact’s canonical bytes as defined in §4 (UTF-8, sorted keys, compact, exactly one LF, no BOM). Do not hash whatever an editor wrote if it is non-canonical.

Required procedure (JSON artifacts).

* Read the file in binary mode.

* Parse as JSON and re-serialize with the canonical JSON rules from §4 to obtain canonical\_bytes.

* Compare canonical\_bytes to the on-disk bytes. They MUST match exactly.

* If they differ (pretty print, CRLF, extra spaces, unsorted keys, missing LF, BOM), fail closed. Do not “fix up” during hashing.

* Compute SHA-256 over canonical\_bytes.

* Encode the digest as 64 lowercase hex; record it as sha256.

* Set size to the byte length of canonical\_bytes.

What not to hash.

* Not compressed or transport encodings (no gzip, no br).

* Not editor or IDE previews with altered line endings or encodings.

* Not a “normalized-only-for-hashing” variant while leaving a non-canonical file on disk. The file itself must already be canonical.

Arrays-as-sets interaction.

* If an array is declared a set (§4), the file must already be deduplicated and ASCII-sorted by identity.

* Any duplicate-with-different-value or out-of-order identity makes the artifact non-canonical → fail closed.

Locale and environment.

Run under LC\_ALL=C (§4). Do not allow locale or timezone to affect bytes or hashing.

Self-listing.

RESOLVED: the manifest does not self-list. If this policy changes, compute any self-entry after the file is finalized and canonical, then validate it like any other entry (avoid recursion by hashing the canonical bytes as they exist on disk at that moment).

Acceptance hints.

* HASH\_INPUT\_CANON\_BYTES\_OK

* HASH\_SHA256\_HEX64\_OK

* HASH\_SIZE\_MATCH\_OK

* HASH\_FILE\_EQ\_CANON\_OK

* HASH\_ENV\_LC\_ALL\_C\_OK

## **5.3 Validation**

Hex64 lowercase; size matches canonical bytes; every referenced artifact appears exactly once.

Procedure (normative).

Schema pass. Validate catalog/manifest.json against its owning schema (top-level object with root, version, built\_at\_utc, and a single files array of {path, sha256, size}, no additional top-level members or entry fields).

Entry fields. For each files entry:

* sha256 matches regex ^\[0-9a-f\]{64}$ (lowercase hex).

* size is an integer ≥ 0 (fits in 64-bit signed).

* path is a relative POSIX path (no absolute paths, no .., no //).

File presence. Each path resolves to an existing file under the pack root (root="catalog/"). Missing files are errors.

Canonical bytes check. For each path:

* Read in binary, parse JSON, re-serialize with §4 canonical rules to obtain canonical\_bytes.

* The on-disk bytes MUST equal canonical\_bytes. If not, fail closed (do not “fix up” during hashing).

Digest and length. Recompute SHA-256 over canonical\_bytes; compare to sha256. Recompute byte length; compare to size. Both MUST match.

Uniqueness & order. Treat files as a set keyed by path:

* No duplicate path entries.

* ASCII-ascending order by path. Any out-of-order pair is an error.

Completeness. The set of entries MUST include every frozen input exactly once. No missing entries. No extraneous entries for non-inputs.

Arrays-as-sets interaction. Where any governed artifact contains arrays treated as sets (§4), that artifact MUST already be deduplicated and ASCII-sorted by identity. Any conflict/out-of-order identity makes the artifact non-canonical → error.

Locale & purity. Perform validation under LC\_ALL=C (§4); no wall clock, randomness, or floats in any step.

Self-listing. Not used. If re-enabled by policy, verify the computed self-entry like any other entry.

CI enforcement (minimum checks).

* MANIFEST\_TOP\_LEVEL\_OBJECT\_OK

* MANIFEST\_FILES\_ARRAY\_OK

* MANIFEST\_ENTRY\_FIELDS\_OK

* MANIFEST\_SHA256\_HEX64\_OK

* MANIFEST\_SIZE\_MATCH\_OK

* MANIFEST\_NO\_DUP\_PATHS\_OK

* MANIFEST\_PATH\_ASCII\_SORT\_OK

* MANIFEST\_FILE\_EXISTS\_OK

* MANIFEST\_FILE\_EQ\_CANON\_OK

* MANIFEST\_LISTS\_ALL\_INPUTS\_OK

* MANIFEST\_CANON\_JSON\_OK

* ENV\_LC\_ALL\_C\_OK

* PACK\_ROOT\_PINNED\_OK

* PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK

# 6\. Freeze-Pack Manifest → release\_id \[Required-Now\]

## **6.1 Manifest construction**

Purpose. Canonical JSON document listing every frozen input (path, sha256, size) with top-level metadata. This file’s canonical bytes are the exact bytes hashed to derive release\_id and it captures a closed set of frozen inputs for the release.

Single home.

The Freeze-Pack Manifest file is catalog/manifest.json — the single source of truth for the input list. Any prior name (for example, CANON\_CHECKSUMS.json) is deprecated.

Top-level shape (normative).

The manifest is a JSON object with the following properties (no others allowed):

* root — string. Pack root, fixed to "catalog/".

* version — string. Semver for the catalog pack (not the app version).

* built\_at\_utc — string. UTC ISO-8601 timestamp (YYYY-MM-DDThh:mm:ssZ).

* files — array of entry objects.

Self-exclusion. The root manifest MUST NOT list itself (catalog/manifest.json). Listing catalog/narratives/manifest.json is required (see Content requirements and §2.8).

Entry objects (see §5.1).

Exactly: {"path": "\<string\>", "sha256": "\<lowercase 64-hex\>", "size": \<non-negative integer\>}

path values are relative to the pack root (root \== "catalog/"). Do not include the "catalog/" prefix. Path constraints: repo-relative POSIX; no .., no //; maximum 256 bytes. Case-sensitive. (Default path charset guidance ^\[a-z0-9\_./-\]+$.)

Arrays-as-sets policy.

files is treated as a set keyed by path. Apply §4 arrays-as-sets rules: dedupe by identity (path), ASCII-sort by path, fail closed on conflicts.

Canonical bytes.

Apply §4 canonical JSON rules to the entire file: UTF-8 (no BOM); sorted keys (ASCII) for every object; compact separators; exactly one trailing LF.

Content requirements.

Include every catalog/artifact consumed as a frozen input in this document’s scope (for example: centers.json, gates.json, channels.json, presets.json, magic10.json, magic10\_seeds.json when present, and other denominators where applicable).

Include narratives pack members under catalog/narratives/\* (keys.json, templates.json, optional palettes.json, suppression\_map.json) and the narratives pack manifest at catalog/narratives/manifest.json (see §2.8).

Do not include logs, evidence reports, JSONL mirrors, or other non-inputs.

Narratives completeness check: the items above must be present exactly once; omission is an error.

Runtime (titles-only). Sealed narratives packs are served from /narratives/\<pack\_sha\>/\<PACK\_MEMBER\>. Identity binding is to the canonical bytes of catalog/narratives/manifest.json (see pack\_sha rule above). Loader/mount behavior is referenced here by title only; detailed runtime policy lives outside this document.

Ordering & duplicates.

files entries MUST be ASCII ascending by path.

No duplicate path. Conflicting duplicates (same path, different sha256/size) ⇒ error.

Example (illustrative only).

{"root":"catalog/","version":"1.0.0","built\_at\_utc":"2025-10-28T00:00:00Z","files":\[{"path":"centers.json","sha256":"0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef","size":1234},{"path":"gates.json","sha256":"abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789","size":5678},{"path":"narratives/manifest.json","sha256":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","size":321},{"path":"narratives/templates.json","sha256":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","size":654}\]}

CI enforcement (minimum).

MANIFEST\_TOP\_LEVEL\_OBJECT\_OK, MANIFEST\_FILES\_ARRAY\_OK, MANIFEST\_ENTRY\_FIELDS\_OK, MANIFEST\_SHA256\_HEX64\_OK, MANIFEST\_SIZE\_MATCH\_OK, MANIFEST\_PATH\_ASCII\_SORT\_OK, MANIFEST\_NO\_DUP\_PATHS\_OK, MANIFEST\_FILE\_EXISTS\_OK, MANIFEST\_CANON\_JSON\_OK, PACK\_ROOT\_PINNED\_OK, PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK.

## **6.2 release\_id computation**

release\_id \= sha256(canonical\_manifest\_bytes) where the digest is lowercase 64-hex.

Normative rule.

Compute release\_id by hashing the canonical bytes of the Freeze-Pack Manifest defined in §6.1. Canonical bytes follow §4: UTF-8, sorted keys (ASCII), compact, exactly one LF, no BOM. Output is a 64-character lowercase hex SHA-256 string. No prefixes, no uppercase.

Procedure.

* Read the finalized manifest in binary.

* Parse JSON and re-serialize using §4 rules to obtain canonical\_manifest\_bytes.

* Verify on-disk bytes equal canonical\_manifest\_bytes. If not, fail closed.

* Compute SHA-256 over canonical\_manifest\_bytes.

* Encode as 64 lowercase hex; record as release\_id.

Determinism pins.

Run with LC\_ALL=C, LANG=C, TZ=UTC (§4). No wall clock, no randomness, no floats.

Two runs over identical inputs MUST produce identical release\_id.

Validation.

To validate a claimed release\_id, recompute from the on-disk manifest as above and compare for exact equality.

If the manifest is non-canonical, do not compute. Treat as an error until canonicalization is fixed.

Acceptance hints (titles only; tokens live in HDE-Governance §2.0).

RELEASE\_ID\_RECOMPUTE\_OK, RELEASE\_ID\_FROM\_MANIFEST\_OK, JSON\_CANONICAL\_CHECK\_OK, PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK.

### **6.2.1 External release attestation**

The release dependency direction is:

`tracked source → canonical manifest → release_id → external attestation`

Runtime derives `release_id` only from the packaged canonical bytes of `catalog/manifest.json`. Runtime MUST NOT consume evidence paths, release-identity environment variables, generated source constants, or mutable attestation files as release-identity inputs.

Current release-bound derivatives are generated with:

`python tools/evidence/build_release_attestation.py --output <external-empty-directory> --require-clean`

The tracked contract schemas are:

* success: `hde.release_attestation.v1` at `schemas/hde_release_attestation.v1.json`; and  
* failure: `hde.release_attestation.failure.v1` at `schemas/hde_release_attestation_failure.v1.json`.

A successful final attestation requires an exact clean source commit, `source_commit_exact: true`, `release_admission: "PR06R_B_FINAL_PASS"`, and `pipeline_stop: null`. It binds the exact source commit, deterministic tracked-tree digest, canonical manifest and release identity, sorted file inventory, deterministic transcript facts, canonical checksums, and final release-admission posture.

`tools/evidence/build_release_attestation.py` MUST refuse output inside the source repository, a non-empty destination, and overwrite of existing output. Success and failure outputs remain external. They are not governed checked-in release primaries, do not create Human Evidence Index or Machine Evidence Mirror bindings for emitted bundles, and do not create acceptance-token satisfaction by implication.

Existing checked-in EPIC022 release evidence and its companions remain frozen capture-time records. They are not runtime identity inputs, are not regenerated for later release cuts, and MUST NOT be relabeled as current release attestations.

`artifacts/registry/registry_report.json` remains configuration evidence rather than release-identity or release-provenance evidence. It and derived config bundles MUST NOT embed incidental manifest digests, release IDs, or manifest-listed source-file identities, and an otherwise unchanged registry/configuration family MUST NOT churn solely because of a release cut.

## **6.3 Change ⇒ new release\_id**

Any byte change to a frozen input or to the manifest produces a new release\_id.

Scope.

“Frozen input” means any file listed in the Freeze-Pack Manifest (§6.1).

“Manifest structure” means the set of entries and their canonical JSON form in catalog/manifest.json.

Normative rules.

If any listed artifact’s canonical bytes change, the entry (sha256, size) changes ⇒ manifest bytes change ⇒ new release\_id.

If the manifest’s entries set changes in any way, manifest bytes change ⇒ new release\_id:

* Adding/removing an entry.

* Renaming a path.

* Introducing or resolving a duplicate path.

* Reordering so files is not ASCII-ascending by path.

* Changing any field value (path, sha256, size).

If an artifact violates canonical rules and is then corrected to canonical, the artifact bytes change ⇒ new release\_id.

Non-canonical manifest: do not compute (see §6.2 Validation). Fix canonicalization first; then compute.

Examples that produce a new release\_id.

Edit to catalog/gates.json that changes any value.

Fixing key order or line endings in catalog/centers.json to meet §4.

Adding catalog/presets.json to the pack.

Adding catalog/magic10\_seeds.json to the pack (when introduced).

Adding catalog/narratives/manifest.json to the pack.

Adding any catalog/narratives/\* member (keys/templates/palettes/suppression\_map) to the pack.

Renaming a path in the manifest.

Correcting an out-of-order files array to ASCII order.

Examples that do not produce a new release\_id.

Editor settings that do not alter canonical bytes.

Changes to logs, evidence reports, JSONL mirrors, or files not listed in the manifest.

Runtime or transport settings outside the pack (for example, gzip delivery).

CI enforcement.

Recompute release\_id from the finalized manifest and compare to the recorded value.

Fail the build if any listed artifact’s recomputed sha256 or size differs from the manifest.

Fail the build if the manifest is not canonical JSON or not ASCII-sorted by path.

Acceptance hints (titles only; tokens live in HDE-Governance §2.0).

RELEASE\_ID\_RECOMPUTE\_OK, RELEASE\_ID\_FROM\_MANIFEST\_OK, MANIFEST\_PATH\_ASCII\_SORT\_OK, MANIFEST\_NO\_DUP\_PATHS\_OK, MANIFEST\_FILE\_EXISTS\_OK, JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK.

## **6.4 Evidence and CI hooks**

Purpose. Prove the manifest is canonical, that each entry’s digest and size match the artifact’s canonical bytes, and that the release\_id equals the SHA-256 of the canonical manifest bytes.

Required artifacts.

Freeze-Pack Manifest evidence copy (no alternate semantics).

* path: artifacts/math/freeze\_pack\_manifest.json

* MUST be a byte-identical copy of the canonical on-disk catalog/manifest.json (identity is on canonical bytes; no derived schemas or alternate contracts).

* MUST NOT be repurposed for any other manifest-like payload (see “no branching semantics” posture in Build Notes by title only).

Recompute script — reads the finalized manifest, verifies canonical form, recomputes release\_id, and proves the freeze-pack identity surfaces are coherent.

* path: scripts/release\_id\_recompute.py

* recompute log (evidence): artifacts/math/release\_id\_recompute.log

Mode semantics (normative).

* \--check MUST be fail-closed (non-zero on any mismatch) and MUST NOT “self-heal” or rewrite governed artifacts.

* Non---check mode MAY rewrite governed artifacts to the canonical state and MUST exit 0 when the post-write state is clean.

* A regression test MUST cover both modes using an isolated temp workspace (so the repo working tree is not mutated).

Release ID file (canonical) — one-line release\_id \+ LF; must be treated as the canonical recorded value for tooling and closeout wiring.

* path: artifacts/math/release\_id.txt

* audit/gates/release/release\_id.txt is deprecated and MUST NOT be used.

Checksum verification report — per-entry results for path, recomputed sha256, size, and any failures.

* path: artifacts/math/checksums\_audit.log

Manifest snapshot — small JSON with release\_id, manifest file path, manifest sha256, entry count, CI timestamp. Evidence only, not an input.

* path: artifacts/math/manifest\_snapshot.json

Environment pins — text file recording LC\_ALL=C, LANG=C, TZ=UTC used during checks.

* path: artifacts/proofs/env\_pins.txt

Normative behavior.

Recompute release\_id.

* Read catalog/manifest.json in binary; parse; re-serialize with §4 rules to canonical bytes; verify on-disk file equals canonical.

* Compute SHA-256 over canonical bytes; compare to the recorded release\_id (must match).

* Assert manifest is UTF-8 (no BOM), sorted keys, compact, exactly one LF; files\[\] is ASCII-sorted by path, has no duplicates, and does not list the manifest itself.

Verify checksums.

* For each entry {path, sha256, size}: open the file; compute canonical bytes; verify on-disk equals canonical; recompute sha256 and size; both must match the manifest.

* Fail if any entry path is not repo-relative POSIX or any hash is not lowercase 64-hex.

Completeness.

* The manifest lists every frozen input exactly once (closed sets, denominators, catalogs, constants, thresholds, seeds if catalogized). No extras for non-inputs.

* Narratives completeness: catalog/narratives/manifest.json and the four catalog/narratives/\* members must be present exactly once (see §2.8).

Locale and determinism.

* Run under LC\_ALL=C, LANG=C, TZ=UTC with no wall-clock dependence, no randomness, and no floating-point nondeterminism (§4).

* Prove two-run identity of the recompute step (same inputs → identical outputs).

CI hooks (minimum).

Release identity gate (fail-closed, closed rails) — CI MUST run the dedicated identity gate entrypoint:

* path: ci/checks/check\_release\_identity.sh

invocation posture (names-only): invoke as a Python entrypoint (for example python ci/checks/check\_release\_identity.sh).

minimum behavior (normative):

* enforce closed rails

* run python scripts/release\_id\_recompute.py \--check

* assert manifest schema \+ canonical bytes posture

* assert byte-equality between catalog/manifest.json (canonical bytes) and artifacts/math/freeze\_pack\_manifest.json

* assert the governed recompute evidence outputs exist and are non-empty

operator note (non-blocking): running the gate may rewrite artifacts/math/release\_id\_recompute.log even in \--check mode in ephemeral CI workspaces; local operators MUST treat this as tool-driven churn and avoid committing unintended log rewrites.

Pre-merge job runs the recompute script and checksum verification; any failure is a hard stop.

Manifest-change gate requires updating, in the same commit/PR:

* the human Evidence Index: docs/evidence/INDEX.json

* the Evidence Index hash sentinel: docs/evidence/INDEX.sha256

* the machine mirror: artifacts/evidence\_index.jsonl

Two-run identity job ensures stable bytes across two executions on the same inputs.

Sentinel check: CI fails if docs/evidence/INDEX.sha256 does not match the current INDEX.json bytes.

Evidence Index entries (titles and paths only).

* Freeze-Pack Manifest (bytes copied for evidence) — artifacts/math/freeze\_pack\_manifest.json

* Release ID file (canonical) — artifacts/math/release\_id.txt

* Recompute release\_id script — scripts/release\_id\_recompute.py

* Recompute release\_id log — artifacts/math/release\_id\_recompute.log

* Checksum verification report — artifacts/math/checksums\_audit.log

* Manifest snapshot (release\_id, manifest sha256, count) — artifacts/math/manifest\_snapshot.json

* Environment pins (LC\_ALL, LANG, TZ) — artifacts/proofs/env\_pins.txt

* Evidence Index hash sentinel — docs/evidence/INDEX.sha256

Acceptance hints (titles only; acceptance token names live in PF04; semantics in HDE-Governance).

RELEASE\_ID\_RECOMPUTE\_OK, RELEASE\_ID\_FROM\_MANIFEST\_OK, PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK, MANIFEST\_SHA256\_HEX64\_OK, JSON\_CANONICAL\_CHECK\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, TWO\_RUN\_IDENTITY\_OK.

## **7\. Interfaces to Other Specs (titles-only) \[Required-Now\]**

This document routes by title only. Do not restate or duplicate content from other specs. Do not include version numbers in prose.

## **7.1 Math (by title)**

Reference: PF-Canon-HDE-Math-Spec

Defers to Math for:

* Scoring and thresholds

* Deterministic preimage and idempotence recipe

* Any arithmetic, weighting, tie-break, or precedence logic

## **7.2 Governance/CLI (by title)**

References: PF-Canon-HDE-Governance; PF-Canon-HDE-CLI-API-Vendor-Ref

Defers to Governance/CLI for:

* Public success and error shapes

* Headers and conditional delivery behavior

* Vendor request shaping and typed field mapping

## **7.3 Architecture (by title)**

Reference: PF-Canon-HDE-Architecture

Defers to Architecture for:

* System boundaries and single-homes

* Contract-free overview of components and responsibility lines

## **CI & Evidence \[Required-Now\]**

# 8\. CI & Evidence \[Required-Now\]

## **8.1 Catalog schema CI**

Jobs to validate all catalogs against their schemas. Fail on unknown keys or IDs. These jobs enforce §§3–6; they do not redefine rules.

### **Purpose**

Prove that every catalog conforms to its owning JSON Schema and that all referenced IDs belong to closed domains.

### **Scope**

Catalogs from §2: Centers, Gates, Channels, Presets, Magic-10 (catalog/magic10.json), Magic-10 seeds (catalog/magic10\_seeds.json), Authorities \[OPEN\], Profiles \[OPEN\].

Validation rules from §3.1 (schema), §3.2 (topology), §3.3 (domain closure), and serialization pins from §4.

### **Inputs**

Catalog file list from §2 with titles and paths only. Paths that are not yet confirmed remain \[OPEN\] and must be wired before CI runs.

### **Normative jobs**

#### **catalog\_schema\_validate**

Validate each catalog against its owning JSON Schema.

Reject additional properties unless the schema allows them at that object level.

Reject missing required fields and wrong types.

Arrays declared as sets must declare identity rules or be flagged \[OPEN\] to fix in schema.

#### **catalog\_domain\_closure**

Build owner sets for each closed domain.

Check all references for membership in the owner set.

Fail on any unknown ID or enum value. No coercion. No aliases in v1.

#### **catalog\_topology\_coherence**

Apply graph checks from §3.2 across Centers, Gates, Channels.

Channel has exactly two distinct gate IDs.

Gate references exactly one valid center.

Channel center derivation matches any stored center fields.

No orphaned references.

#### **catalog\_arrays\_as\_sets**

For arrays that function as sets, verify deduplication by identity, no conflicts on identical identities, and ASCII ascending order by identity, per §4.2.

#### **catalog\_canonical\_json**

Verify each catalog is already in canonical JSON form per §4.

Check UTF-8, sorted keys, compact separators, exactly one trailing LF, no BOM.

Do not auto-rewrite. Treat non-canonical bytes as an error.

### **Failure policy**

Any schema error, unknown key, unknown ID, orphan, set-order violation, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

### **Artifacts (titles and paths only)**

* Catalog Schema Validation Report — artifacts/catalog/catalog\_schema\_validation.log

* Domain Closure Report — artifacts/catalog/domain\_closure\_report.log

* Topology Coherence Report — artifacts/topology/topology\_coherence\_report.log

* Canonical JSON Check Report — audit/gates/canonical\_json/json\_canonical\_check.log

### **Indexing**

Add the above to Appendix D (human) and append records to artifacts/evidence\_index.jsonl (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a proof\_anchor to a path-proof stored alongside the artifact).

### **Environment and determinism**

Run with LC\_ALL=C, LANG=C, TZ=UTC per §4.3.

No wall clock, no randomness, no floats.

### **Acceptance hints (names-only)**

* UMS\_AJV\_PASS

* CATALOG\_SCHEMA\_OK

* CATALOG\_NO\_ADDITIONAL\_PROPS\_OK

* CATALOG\_NO\_UNKNOWN\_KEYS\_OK

* CATALOG\_DOMAIN\_CLOSED\_OK

* CATALOG\_TOPOLOGY\_OK

* ARR\_SET\_IDENTITY\_DECLARED\_OK

* ARR\_SET\_NO\_DUPLICATES\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* JSON\_CANONICAL\_CHECK\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

## **8.2 Integrity CI**

Degree-vector and orphan checks. Arrays-as-sets enforcement. Canonicalization compare.

### **Purpose**

Assert pack-level integrity beyond schema shape: graph soundness, set semantics, and byte determinism.

### **Scope**

Applies to all catalogs in §2 that participate in topology or set semantics (Centers, Gates, Channels, Presets, Magic-10, Magic-10 seeds, Authorities \[OPEN\], Profiles \[OPEN\]).

Uses rules from §3.2 (topology), §3.3 (domain closure), §4 (canonical JSON and arrays-as-sets).

### **Normative jobs**

#### **integrity\_topology**

Orphans. Every referenced ID exists (gate→center, channel→gates). Zero dangling references.

Channel degree. Each channel references exactly two distinct gate IDs.

Gate↔center consistency. Each gate references exactly one valid center; any stored center fields on channels must match the set derived from member gates.

Degree vectors (optional). If catalogs declare expected degree counts (for centers or gates), compute observed degrees from the graph and assert equality. If undeclared, skip with PASS; if declared, mismatches are errors. (Confirm degree-vector home in §3; leave \[OPEN\] only if not declared in schemas.)

#### **integrity\_arrays\_as\_sets**

For arrays designated as sets in their schemas, enforce §4.2:

* Identity declared & computable (\[OPEN\] where missing in schema).

* No duplicate identities with different element values (conflict).

* After deduplication, ASCII ascending order by identity.

* Fail closed on any conflict or ordering violation.

#### **integrity\_canonicalization\_compare**

For each catalog: parse JSON, re-serialize with §4 canonical rules, and compare bytes to the on-disk file.

Files must already be canonical (UTF-8, sorted keys, compact, one LF, no BOM).

Do not auto-rewrite. Any difference is an error.

### **Failure policy**

Any orphan, degree violation, set conflict, out-of-order identity, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

### **Artifacts (titles and paths only)**

* Topology Integrity Report — artifacts/topology/topology\_coherence\_report.log

* Arrays-as-Sets Report — artifacts/canonical/arrays\_as\_sets\_report.log

* Canonical JSON Gate Compare Log — audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

### **Indexing**

Add these to Appendix D (human) and append records to artifacts/evidence\_index.jsonl (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a proof\_anchor to a path-proof stored alongside the artifact).

### **Environment and determinism**

Run with LC\_ALL=C, LANG=C, TZ=UTC per §4.3.

No wall clock, no randomness, no floats.

### **Acceptance hints (names-only)**

* TOPOLOGY\_NO\_ORPHANS\_OK

* TOPOLOGY\_CHANNEL\_DEGREE\_2\_OK

* TOPOLOGY\_GATE\_CENTER\_OK

* DEGREE\_VECTORS\_MATCH\_OK (when declared)

* ARR\_SET\_IDENTITY\_DECLARED\_OK

* ARR\_SET\_NO\_CONFLICTS\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* FILE\_EQ\_CANON\_BYTES\_OK

* ENV\_LC\_ALL\_C\_OK

## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**

### **Single home and path**

#### **Path (fixed)**

* artifacts/evidence\_index.jsonl (there must be exactly one mirror file in the repo).

The mirror has a governed checksum sidecar at `artifacts/evidence_index.jsonl.sha256`. The mirror file and its checksum sidecar MUST each have a sibling `.path_proof.txt` transcript (co-located), including `artifacts/evidence_index.jsonl.path_proof.txt` and `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.

#### **Governed locations only.**

Every evidence file referenced by the mirror MUST live under governed repo paths (for example, artifacts/, docs/). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI.

#### **Evidence-path safety invariants (mirror discovered\_physical\_path).**

For every mirror record:

* `discovered_physical_path` MUST be a repo-relative path (no absolute paths).  
* `discovered_physical_path` MUST NOT contain parent-directory segments (`..`) and MUST NOT escape the repository root after normalization and resolution.  
* `discovered_physical_path` MUST resolve to an existing file at validation time.  
* Mirror entries that violate these invariants MUST fail CI.

Implementation notes (titles-only; mechanics live outside PF12).

* Evidence path validation: `tools/evidence/validate_evidence_paths.py`  
* Final-LF endings check wrapper: `tools/evidence/check_lf_endings.py`

#### **Tracked files (no .gitignore for governed artifacts).**

Governed evidence artifacts and their sibling path-proof transcripts (\<artifact\>.path\_proof.txt) MUST NOT be ignored by .gitignore. Governed locations are expected to be tracked; using .gitignore to hide governed artifacts or their path-proofs is invalid and should be treated as a QA failure.

### **Format (canonical JSONL)**

One JSON object per line.

Canonical JSON per §4 for each line:

* UTF-8 (no BOM).

* Sorted keys.

* Compact separators.

* Exactly one trailing \\n per line.

* No blank lines; no trailing spaces.

* Unknown keys are rejected (CI-blocking).

### **Minimum record schema (reject unknown keys)**

Each line in the mirror uses at least the following schema; unknown keys are rejected:

* {

* "artifact\_key": ""

* "role": "\<proof|golden|snapshot|script|log\>"

* "sha256": "\<lowercase 64-hex\>"

* "size\_bytes":

* "produced\_at\_utc": ""

* "discovered\_physical\_path": ""

* "proof\_anchor": ""

* }

### **Bundle-aware extension (evidence bundles, manifests, and epic metadata)**

The minimum record schema above remains normative for all Mirror records. This section extends it to cover bundle artifacts, their manifests, and per-epic metadata without changing the core field set or canonical JSONL discipline.

#### **Allowed top-level keys and unknown-key rejection**

The Mirror still rejects unknown keys. The only allowed top-level keys for any record are:

Core keys (required for every record):

* artifact\_key

* role

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor

Metadata keys (optional; may appear on any record):

* epic\_id — a short identifier for the owning epic (for example, "HDE-EPIC020"); semantics live in HDE-Phased Epics and Glow QA Guide (titles-only).

* record\_type — a short type label for this record (for example, "epic020\_bundle" or "epic020\_bundle\_manifest"); names are governed by local schemas and tests.

* schema\_version — a version string for the record schema (for example, "1.0").

* notes — free-form, names-only commentary to aid audits; contents are out of scope for PF12 beyond canonical JSON constraints.

* tokens — an array-as-set of acceptance token names (strings) associated with this record; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide. Arrays treated as sets MUST be deduped and ASCII-sorted.

tokens is a non-empty array of token names tied to the EPIC020 acceptance roster; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide.

Bundle-specific keys (optional; bundle rows only):

* bundle\_key — a stable logical identifier for the bundle’s member family (for example, "ordering\_evidence", "sampler\_pool\_snapshots", "config\_bundles", or an epic-specific family such as "epic020\_bundles"); names are governed by local schemas and tests, not by PF12.

* bundle\_manifest\_path — the repo-relative path to the bundle’s manifest JSON/JSONL file if the current record represents the bundle file (the manifest itself is a separate governed artifact with its own Mirror record).

* bundle\_member\_count — an integer counting the number of logical members recorded in the manifest for this bundle.

Non-bundle artifacts (most rows) MUST NOT include any bundle-specific keys.

For those rows, the allowed key set is exactly the core keys plus any applicable metadata keys above; the minimum record schema from the preceding block applies unchanged.

#### **Bundle artifacts and manifests**

A bundle artifact is a textual file (JSON/JSONL) that groups multiple logical evidence members. Its Mirror record’s artifact\_key identifies the governed bundle family (for example, "config\_bundle.fe" or a future bundle family defined in §8.6), and discovered\_physical\_path points to the bundle file under artifacts/\*\* or docs/evidence/\*\*.

A bundle manifest is a textual file (JSON/JSONL) that enumerates the bundle’s members (logical artifact\_key, member sha256, size\_bytes, and optional descriptors) and is treated as a separate governed artifact. The manifest has its own Mirror record with its own artifact\_key and discovered\_physical\_path; it MAY use bundle\_key to associate itself with the corresponding bundle artifact.

For selected bundle-based families (as defined in §8.6 and in their per-family subsections), the Human Evidence Index and Machine Evidence Mirror track the bundle file and its manifest as the governed artifacts instead of listing every internal member file as a separate row. Internal member content is addressed by the manifest, not directly by additional Mirror rows.

#### **EPIC-scale example (EPIC020 Candidate 1 bundles)**

EPIC020 Candidate 1 evidence bundles follow this pattern:

* Each EPIC020 bundle and manifest has a Mirror record whose artifact\_key is the relevant EPIC020 token (for example, "EPIC020.D1.HTTP\_COMPAT\_MALFORMED\_JSON" or CLI\_SHOWCOMPAT\_CANON\_OK).

* record\_type is "epic020\_bundle" for bundle artifacts and "epic020\_bundle\_manifest" for manifests.

* epic\_id is "HDE-EPIC020".

* tokens is a non-empty array of token names tied to the EPIC020 acceptance roster; schema and ownership of token names live in HDE-Governance and Glow QA Guide.

Other epics may introduce similar patterns with different record\_type and epic\_id values; PF12 remains the single home for the allowed key set and canonical JSONL constraints, while per-epic meaning is defined by PF04/PF19/PF20.

#### **Path-proof semantics for bundles**

Each bundle artifact and its manifest MUST have governed sibling path-proof transcripts (\<bundle\_file\>.path\_proof.txt and \<manifest\_file\>.path\_proof.txt) stored alongside each file, whose path, sha256, and size\_bytes match the bundle/manifest file and the corresponding Mirror record values.

For bundle-based families, “per-artifact path proofs” in PF12 are interpreted as “per governed artifact,” where a governed artifact may be either:

* a single artifact file (e.g., a log or JSON snapshot), or

* a bundle artifact or bundle manifest file.

This extension does not introduce hash-only or index-only families. Any future move toward hash-only evidence (no on-disk member payloads) remains out of scope here and requires an explicit reconciliation Doc-Delta (tracked as an OPEN decision in §0.5).

All other Mirror rules remain unchanged: canonical JSONL per §4, single mirror file at artifacts/evidence\_index.jsonl, sort-before-write by (artifact\_key, discovered\_physical\_path), uniqueness of that pair, strict governed-paths rule, and 1:1 parity with the Human Evidence Index.

### **Self-record semantics (index.machine\_mirror)**

The mirror MAY include a single record whose artifact\_key identifies the Machine Evidence Mirror itself (for example, "index.machine\_mirror"). This is the self-record for artifacts/evidence\_index.jsonl.

For this self-record:

* sha256 MUST equal the SHA-256 digest of the mirror’s canonical JSONL body excluding the self-record line.

* size\_bytes MUST equal the byte length of the complete artifacts/evidence\_index.jsonl file including the self-record line.

The associated path-proof transcript for artifacts/evidence\_index.jsonl MUST contain exactly one sha256/size\_bytes pair and those values MUST match the self-record’s sha256 and size\_bytes.

All other mirror records (non self-records) follow the normal mirror discipline: sha256 and size\_bytes are for the referenced artifact at discovered\_physical\_path, and their path-proof transcripts must match those values (see “Path-proof transcript schema”).

### **Field order and write discipline (merge-blocking)**

ASCII field order (exact):

* artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes.

Sort-before-write by the tuple (artifact\_key, discovered\_physical\_path).

Uniqueness: the pair (artifact\_key, discovered\_physical\_path) is unique; duplicates fail CI.

Single mirror file: only one artifacts/evidence\_index.jsonl may exist in the repo.

### **produced\_at\_utc vs mtime\_utc**

produced\_at\_utc records when the evidence was logically produced (the event time). It is part of the mirror record and is used to reason about when posture snapshots and QA runs occurred.

mtime\_utc is recorded in the per-artifact sibling path-proof transcript (\<artifact\>.path\_proof.txt) as the filesystem modification time for the artifact.

Differences between produced\_at\_utc and mtime\_utc are allowed but must be truthful — no “backdating” or forward-dating to distort ordering. QA may rely on produced\_at\_utc as the primary ordering key for evidence; disagreements should be rare and explainable in the PR.

### **Path-proof transcript schema (governed artifacts)**

Naming (MUST). The sibling path-proof transcript for a governed artifact MUST be named \<artifact\>.path\_proof.txt, where \<artifact\> includes the artifact’s full filename including extension. Example: audit/gates/determinism/env\_pins.log → audit/gates/determinism/env\_pins.log.path\_proof.txt (not env\_pins.path\_proof.txt).

For every governed artifact in §8.6, the path-proof transcript MUST be a co-located sibling file named \<artifact\>.path\_proof.txt. It MUST describe exactly one artifact and follow a stable, line-oriented schema.

#### **Required fields (exactly one record per file)**

Each path-proof MUST contain exactly one record for the artifact it describes, with the following required fields:

* path — repo-relative path to the artifact (for example artifacts/engine/order/channels\_sorted.snapshot.json).

* sha256 — lowercase 64-hex SHA-256 digest of the artifact’s canonical bytes.

* size\_bytes — non-negative integer byte length of the artifact’s canonical bytes.

* mtime\_utc — UTC ISO-8601 timestamp (e.g. YYYY-MM-DDThh:mm:ssZ) representing the artifact’s refresh-time mtime (see “mtime\_utc semantics” below).

* produced\_at\_utc — UTC ISO-8601 time when the evidence for this artifact was logically produced.

These fields MUST appear exactly once per file; path-proofs MUST NOT contain multiple or conflicting sha256/size\_bytes pairs, nor multiple mtime\_utc or produced\_at\_utc values for the same artifact.

#### **Optional fields**

Path-proof transcripts MAY include additional informational fields beyond the required set above, but those fields:

* MUST NOT change acceptance semantics, and

* MUST NOT conflict with the required record for path, sha256, size\_bytes, mtime\_utc, or produced\_at\_utc.

The authoritative truth remains the match between:

* the artifact’s canonical bytes,

* the mirror record’s sha256 and size\_bytes, and

* the path-proof’s single sha256/size\_bytes triple for that artifact.

#### **Relationship to proof\_anchor**

Each mirror record’s proof\_anchor field MUST equal the path to the corresponding .path\_proof.txt for that artifact.

CI MUST verify that:

* the file referenced by proof\_anchor exists under governed paths,

* its path matches the mirror’s discovered\_physical\_path,

* its sha256/size\_bytes match the mirror record’s sha256/size\_bytes, and

* there are no duplicate or conflicting sha256/size\_bytes entries within the path-proof.

Failure of any of these conditions is a hard error under the mirror/index tokens declared in §8.3 and §0.2.

### **mtime\_utc semantics (normative)**

#### **Refresh-time mtime**

mtime\_utc records the artifact’s refresh-time mtime: the filesystem modification time observed when the evidence job refreshed that artifact, encoded as a UTC ISO-8601 timestamp (YYYY-MM-DDThh:mm:ssZ) with no fractional seconds (microsecond component MUST be zero).

#### **Monotone vs filesystem stat()**

On any run that writes or checks a path-proof, the evidence tooling MUST verify that mtime\_utc parses as UTC (with microsecond \== 0\) and that parsed\_mtime \<= current\_fs\_mtime, where current\_fs\_mtime is the artifact’s stat().st\_mtime observed at check time.

mtime\_utc is not required to be exactly equal to stat().st\_mtime; it is permitted to be earlier (for example, when a proof is refreshed without the underlying file changing) but MUST NOT lie in the future relative to the current filesystem mtime.

#### **Interaction with produced\_at\_utc**

produced\_at\_utc captures when the evidence for the artifact was logically produced (the evidence refresh event). It is also a UTC ISO-8601 timestamp and may be updated on each refresh or left unchanged when appropriate.

It is expected, but not strictly required, that produced\_at\_utc be greater than or equal to prior produced\_at\_utc values for the same artifact; any non-monotone behavior should be rare and explained in the PR.

#### **Integrity semantics**

The primary integrity check for governed evidence remains the equality of sha256 and size\_bytes between:

* the artifact’s canonical bytes on disk,

* the Machine Mirror record (§8.3), and

* the single record in the path-proof transcript.

mtime\_utc and produced\_at\_utc provide temporal context and are enforced for format and monotone constraints as described above; they do not replace the sha/size equality as the core integrity proof.

#### **Alignment with tools and QA**

Evidence tooling (tools/evidence/update\_evidence\_index.py) and CI checks (ci/checks/check\_mirror\_schema.sh) MUST implement these semantics:

* when writing path-proofs, always recompute size\_bytes and sha256 from the artifact’s canonical bytes

* set or carry forward mtime\_utc as the refresh-time mtime, and validate that it is a UTC ISO timestamp with microsecond \== 0 and mtime\_utc \<= current\_fs\_mtime

* set or carry forward produced\_at\_utc as the evidence refresh time.

Evidence tests (for example, tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py) MUST assert these same semantics (format \+ monotone \<= stat\_mtime) and MUST be kept in sync with this section.

#### **Change control**

Any change to the definition or validation of mtime\_utc or produced\_at\_utc semantics is a normative change and requires:

* a PF12 Doc-Delta (§9),

* synchronized updates to PF19 (Glow QA Guide) and PF10 Build Notes, and

* updates to the evidence tooling and tests that enforce these semantics.

### **Join to the human index (parity, proofs, same-PR rule)**

#### **1:1 parity.**

Every §8.6 Evidence Index entry has exactly one mirror record, and every mirror record has a corresponding human entry:

* artifact\_key equals the Human Index title.

* discovered\_physical\_path equals the Human Index path.

#### **Path-proofs.**

Each artifact’s directory contains a stored path-proof (for example, path\_proof.txt with a stat transcript). The mirror record’s proof\_anchor must exactly match the stored path-proof for that artifact.

#### **Same-PR rule.**

For every governed artifact in §8.6, any change to the artifact MUST update, in the same PR:

* The artifact bytes on disk under a governed path.

* Its sibling \<artifact\>.path\_proof.txt path-proof transcript (the proof\_anchor target).

* The corresponding machine mirror record in artifacts/evidence\_index.jsonl.

* The Human Evidence Index entry in docs/evidence/INDEX.json and its hash sentinel docs/evidence/INDEX.sha256.

Mirror or index entries that refer to non-existent artifacts or stale path-proofs are invalid and must be corrected, not ignored.

#### **Troubleshooting (common failure mode): governed artifact drift**

A governed artifact is considered drifted when any of the following disagree:

* the artifact’s on-disk bytes

* its sibling \*.path\_proof.txt (sha256 and size\_bytes)

* the corresponding Machine Mirror record (sha256 and size\_bytes for the same discovered\_physical\_path)

This is a hard evidence integrity failure. Do not hand-edit proofs or mirror records to “make the check pass”.

Correct remediation (single writer):

Re-generate the evidence skeleton using the canonical evidence tooling so all three surfaces realign:

* Ensure docs/evidence/INDEX.json reflects the intended titles and paths.

* Run tools/evidence/update\_evidence\_index.py in write mode to regenerate:

  * docs/evidence/INDEX.sha256

  * artifacts/evidence\_index.jsonl

  * all governed \*.path\_proof.txt transcripts

* Re-run the tool in \--check mode and fix any remaining mismatches before merge.

### **Determinism**

All checks run with LC\_ALL=C, LANG=C, TZ=UTC.

JSONL records are canonical and LF-terminated (exactly one \\n per record).

### **Header snapshots in artifacts (normative)**

For artifacts that capture headers, header names MUST be lower-case and values MUST be verbatim; exact checks apply to values.

#### **Capture hygiene (normative).**

Header snapshot artifacts MUST contain header lines only.

Tool warnings or stderr output (for example, curl warnings) MUST NOT be mixed into header snapshot bytes.

If the capture command can emit warnings, capture stderr separately (for example, to a sibling \*.stderr.txt or a step log) or filter non-header lines before writing the governed artifact.

Wire casing may differ and is validated by transport owners.

Acceptance hint (names-only): SNAPSHOT\_HEADER\_LOWERCASE\_OK.

### **Refusal proofs (policy note)**

Refusal proofs are error/ops evidence (not JSON success). They must:

* Not set ETag, Vary, or compression headers.

* Use Content-Type: application/json; charset=utf-8.

The refusal log allow-list for JSON body fields is exactly:

* {at, route, status, duration\_ms, idempotence\_hash, release\_id}

Records with any additional fields fail policy checks.

Rate-limit (429) evidence uses a different allow-list and is governed by HDE-Governance. Do not mix refusal and 429 fields in the mirror.

### **Refresh sequence (normative)**

When governed evidence artifacts change, the canonical refresh sequence is:

* Update docs/evidence/INDEX.json with the new or changed titles and paths.

* Run python tools/evidence/update\_evidence\_index.py in write mode to regenerate:

  * docs/evidence/INDEX.sha256

  * artifacts/evidence\_index.jsonl

  * all governed \*.path\_proof.txt transcripts

* Run the mirror schema/shape check job (canonical CI invocation: ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl) and fix any discrepancies before merge.

#### **Operator note (invocation; avoid bash drift).**

ci/checks/check\_mirror\_schema.sh is a Python entrypoint (script file with a Python shebang) and CI invokes it directly. When an acceptance artifact or runbook needs an explicit command, the canonical invocation is:

* ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl

Acceptance artifacts may list either:

* the script path (ci/checks/check\_mirror\_schema.sh) as a tool reference, or

* the explicit direct command above as an invocation.

bash ci/checks/check\_mirror\_schema.sh is invalid and MUST NOT appear in approved acceptance artifacts or operator instructions.

Process and PR workflow (who runs which command and when) remains single-homed in Epic-Process-Guide; this section pins file-level ordering and artifacts that MUST be updated together.

### **Role usage notes (non-normative examples)**

* proof → artifacts/db/ddl\_fingerprint.json, artifacts/proofs/endpoints\_env\_gate\_proof.log, artifacts/bodygraph/source\_invariance/ab.json, /ba.json, /summary.json

* golden → catalog/manifest.json, catalog/schemas/\*.json

* snapshot → artifacts/runtime/env\_matrix.snapshot.json, artifacts/reader/endpoints\_snapshot.json, artifacts/bodygraph/refresh\_policy.snapshot.json, artifacts/bodygraph/metrics.snapshot.json

* script → scripts/card\_close.sh, scripts/migration\_runner.sh

* log → artifacts/db/migration\_runner.log, artifacts/proofs/headers\_probe.log, artifacts/bodygraph/keys\_only.logs.sample (sanitized; keys-only, no PII per Governance)

### **Artifacts with generated\_at\_utc (provenance discipline, including sampler and Engine Core evidence)**

Some governed artifacts (for example, sampler evidence artifacts under artifacts/sampler/\*\* and Engine Core evidence artifacts under artifacts/core/\*\*) include a generated\_at\_utc field in their own JSON payloads. For these artifact families, provenance discipline tightens the relationship between the payload timestamp and the evidence timestamps recorded in the Machine Mirror and path-proofs.

#### **Normative rules (in addition to the general rules in this section)**

When an artifact carries a generated\_at\_utc field in its payload, the evidence tooling MUST treat that field as the artifact’s self-reported generation time for the current refresh and enforce all of the following:

* produced\_at\_utc in the Machine Evidence Mirror record for that artifact MUST NOT be earlier than the artifact’s generated\_at\_utc value. Backdating Mirror produced\_at\_utc relative to generated\_at\_utc is not allowed.

* produced\_at\_utc in the Machine Evidence Mirror record and produced\_at\_utc in the artifact’s path-proof transcript MUST be identical strings (same UTC ISO-8601 representation). Mirror and path-proof timestamps MUST stay in lockstep for a given artifact.

* mtime\_utc in the path-proof remains the refresh-time filesystem mtime (see “mtime\_utc semantics” above) and MUST NOT be later than the artifact’s current filesystem stat().st\_mtime at check time. mtime\_utc may be earlier than generated\_at\_utc (for example, when an artifact’s content has not changed between runs but evidence is refreshed), but sha256 and size\_bytes MUST still match.

For governed families that include both generated\_at\_utc and produced\_at\_utc (including the sampler families registered in §8.6.3 and the Engine Core families engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, and engine\_core\_json\_compare\_logs), provenance correctness for a given refresh requires:

* the artifact’s payload generated\_at\_utc and the Mirror produced\_at\_utc to describe the same refresh window (produced\_at\_utc ≥ generated\_at\_utc in UTC time), and

* the path-proof produced\_at\_utc to match the Mirror produced\_at\_utc exactly.

Integrity gates for these artifacts continue to rely primarily on sha256 and size\_bytes equality across artifact, Mirror record, and path-proof. Timestamp checks are additive: format, monotonicity (per “mtime\_utc semantics”), and the non-backdating rule relative to payload generated\_at\_utc are enforced in addition to the existing sha/size equality rules.

#### **Example — sampler and Engine Core evidence fixes (HDE-EPIC019)**

In earlier EPIC019 work, sampler Mirror records and path-proofs for sampler\_pool\_snapshots, sampler\_two\_run\_logs, sampler\_abba\_logs, sampler\_diversity\_artifacts, and sampler\_seed\_replay\_logs carried produced\_at\_utc values copied from an older skeleton baseline even after the artifacts themselves were regenerated with later generated\_at\_utc timestamps. Engine Core evidence families added in PR7 (engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, engine\_core\_json\_compare\_logs) were wired with generated\_at\_utc and closed-rails env metadata from the start.

The EPIC019 bugfix refreshed Mirror records and path-proofs so that:

* sampler artifacts under artifacts/sampler/\*\* and Engine Core artifacts under artifacts/core/\*\* retain canonical bytes (sha256 and size\_bytes unchanged when content is unchanged)

* their payload generated\_at\_utc values reflect the actual regeneration time for the latest evidence run, and

* produced\_at\_utc in both Mirror and path-proofs is updated to the later refresh time, satisfying the non-backdating rule above and restoring consistency between payload generation timestamps and evidence timestamps for all families that carry generated\_at\_utc.

#### **Tools and tests**

Evidence tooling (for example, tools/evidence/update\_evidence\_index.py and any Engine Core/sampler-specific generators) and Mirror schema checks MUST implement these provenance rules whenever an artifact family introduces a payload-level generated\_at\_utc field.

Tests that exercise those families (for example, sampler evidence tests under tests/evidence/ and Engine Core evidence tests under tests/evidence/test\_engine\_core\_evidence.py) SHOULD assert that:

* produced\_at\_utc in Mirror and path-proofs matches for each artifact instance, and

* where generated\_at\_utc is present, Mirror produced\_at\_utc is not earlier than payload generated\_at\_utc.

#### **Change control**

Any change to the relationship between payload generated\_at\_utc and evidence produced\_at\_utc semantics is a normative change and MUST land with:

* a PF12 Doc-Delta (§9),

* synchronized updates to the relevant Mechanics/QA specs that describe Engine Core and sampler evidence behavior, and

* synchronized changes to the evidence tools and tests that enforce these semantics before the change is considered accepted.

## **8.3.1 Refusal proof (single-file canonical) \[Required-Now\]**

### **Path (fixed)**

artifacts/proofs/ops\_refusal\_proof.txt — single-file refusal:

* Header block.  
* One blank line.  
* LF-terminated JSON body.

Index this file in both docs/evidence/INDEX.json (human) and artifacts/evidence\_index.jsonl (machine) in the same PR.

Include a co-located path\_proof.txt and reference it via proof\_anchor in the mirror.

Policy and tokens live in HDE-Governance (titles only).

### **Purpose**

Capture a refusal response verbatim (headers \+ JSON body) for ops/evidence.

This is not a JSON success route.

### **File format (exact)**

The file consists of:

* A header block.  
* Exactly one blank line.  
* A JSON body.

The file ends with exactly one \\n.

#### **Header block**

One header per line, format: : .

Required header:

* content-type: application/json; charset=utf-8

Forbidden headers: etag, vary, content-encoding.

Other headers may appear as governed elsewhere (for example, date).

Header names are lower-case; values are verbatim. Order is preserved as captured.

#### **Separator**

Exactly one blank line (a single \\n) between headers and body.

#### **Body (JSON, single line)**

Canonical JSON per §4:

* UTF-8.  
* Sorted keys.  
* Compact separators.  
* One trailing \\n.

Fields must conform to the refusal allow-list:  
{at, route, status, duration\_ms, idempotence\_hash, release\_id}

Unknown keys fail policy checks.

### **Mirror linkage**

The mirror record uses role:"log" and must point to this file via discovered\_physical\_path.

The artifact directory also contains a path\_proof.txt stat transcript; the mirror proof\_anchor must exactly match that path-proof entry.

### **Validation checks (CI)**

* File ends with exactly one \\n.  
* Headers lower-case; required header present; forbidden headers absent.  
* Exactly one blank line between headers and body.  
* Body is single-line canonical JSON with the refusal allow-list only.  
* Determinism: checks run with LC\_ALL=C, TZ=UTC.

### **Example (illustrative)**

content-type: application/json; charset=utf-8

date: 2025-11-07T21:00:00Z

{"at":"2025-11-07T21:00:00Z","route":"/ops/rails/refusal","status":503,"duration\_ms":12,"idempotence\_hash":"\<64-hex\>","release\_id":"\<64-hex\>"}

### **Acceptance hints (titles-only; tokens live in HDE-Governance)**

OPS\_REFUSAL\_FILE\_FORMAT\_OK  
OPS\_REFUSAL\_HEADERS\_OK  
OPS\_REFUSAL\_BODY\_OK  
OPS\_REFUSAL\_MIRROR\_LINK\_OK

# 7\. Interfaces to Other Specs (titles-only) \[Required-Now\]

This document routes by title only. Do not restate or duplicate content from other specs. Do not include version numbers in prose.

## **7.1 Math (by title)**

Reference: PF-Canon-HDE-Math-Spec

Defers to Math for:

* Scoring and thresholds

* Deterministic preimage and idempotence recipe

* Any arithmetic, weighting, tie-break, or precedence logic

## **7.2 Governance/CLI (by title)**

References: PF-Canon-HDE-Governance; PF-Canon-HDE-CLI-API-Vendor-Ref

Defers to Governance/CLI for:

* Public success and error shapes

* Headers and conditional delivery behavior

* Vendor request shaping and typed field mapping

## **7.3 Architecture (by title)**

Reference: PF-Canon-HDE-Architecture

Defers to Architecture for:

* System boundaries and single-homes

* Contract-free overview of components and responsibility lines

CI & Evidence \[Required-Now\]

# 8\. CI & Evidence \[Required-Now\]

## **8.1 Catalog schema CI**

Jobs to validate all catalogs against their schemas. Fail on unknown keys or IDs. These jobs enforce §§3–6; they do not redefine rules.

### **Purpose**

Prove that every catalog conforms to its owning JSON Schema and that all referenced IDs belong to closed domains.

### **Scope**

Catalogs from §2: Centers, Gates, Channels, Presets, Magic-10 (catalog/magic10.json), Magic-10 seeds (catalog/magic10\_seeds.json), Authorities \[OPEN\], Profiles \[OPEN\].

Validation rules from §3.1 (schema), §3.2 (topology), §3.3 (domain closure), and serialization pins from §4.

### **Inputs**

Catalog file list from §2 with titles and paths only. Paths that are not yet confirmed remain \[OPEN\] and must be wired before CI runs.

### **Normative jobs**

catalog\_schema\_validate

* Validate each catalog against its owning JSON Schema.

* Reject additional properties unless the schema allows them at that object level.

* Reject missing required fields and wrong types.

* Arrays declared as sets must declare identity rules or be flagged \[OPEN\] to fix in schema.

catalog\_domain\_closure

* Build owner sets for each closed domain.

* Check all references for membership in the owner set.

* Fail on any unknown ID or enum value. No coercion. No aliases in v1.

catalog\_topology\_coherence

* Apply graph checks from §3.2 across Centers, Gates, Channels.

* Channel has exactly two distinct gate IDs.

* Gate references exactly one valid center.

* Channel center derivation matches any stored center fields.

* No orphaned references.

catalog\_arrays\_as\_sets

For arrays that function as sets, verify deduplication by identity, no conflicts on identical identities, and ASCII ascending order by identity, per §4.2.

catalog\_canonical\_json

* Verify each catalog is already in canonical JSON form per §4.

* Check UTF-8, sorted keys, compact separators, exactly one trailing LF, no BOM.

* Do not auto-rewrite. Treat non-canonical bytes as an error.

### **Failure policy**

Any schema error, unknown key, unknown ID, orphan, set-order violation, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

### **Artifacts (titles and paths only)**

* Catalog Schema Validation Report — artifacts/catalog/catalog\_schema\_validation.log

* Domain Closure Report — artifacts/catalog/domain\_closure\_report.log

* Topology Coherence Report — artifacts/topology/topology\_coherence\_report.log

* Canonical JSON Check Report — audit/gates/canonical\_json/json\_canonical\_check.log

### **Indexing**

Add the above to Appendix D (human) and append records to artifacts/evidence\_index.jsonl (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a proof\_anchor to a path-proof stored alongside the artifact).

### **Environment and determinism**

Run with LC\_ALL=C, LANG=C, TZ=UTC per §4.3.

No wall clock, no randomness, no floats.

### **Acceptance hints (names-only)**

* UMS\_AJV\_PASS

* CATALOG\_SCHEMA\_OK

* CATALOG\_NO\_ADDITIONAL\_PROPS\_OK

* CATALOG\_NO\_UNKNOWN\_KEYS\_OK

* CATALOG\_DOMAIN\_CLOSED\_OK

* CATALOG\_TOPOLOGY\_OK

* ARR\_SET\_IDENTITY\_DECLARED\_OK

* ARR\_SET\_NO\_DUPLICATES\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* JSON\_CANONICAL\_CHECK\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

## **8.2 Integrity CI**

Degree-vector and orphan checks. Arrays-as-sets enforcement. Canonicalization compare.

### **Purpose**

Assert pack-level integrity beyond schema shape: graph soundness, set semantics, and byte determinism.

### **Scope**

Applies to all catalogs in §2 that participate in topology or set semantics (Centers, Gates, Channels, Presets, Magic-10, Magic-10 seeds, Authorities \[OPEN\], Profiles \[OPEN\]).

Uses rules from §3.2 (topology), §3.3 (domain closure), §4 (canonical JSON and arrays-as-sets).

### **Normative jobs**

integrity\_topology

* Orphans. Every referenced ID exists (gate→center, channel→gates). Zero dangling references.

* Channel degree. Each channel references exactly two distinct gate IDs.

* Gate↔center consistency. Each gate references exactly one valid center; any stored center fields on channels must match the set derived from member gates.

* Degree vectors (optional). If catalogs declare expected degree counts (for centers or gates), compute observed degrees from the graph and assert equality. If undeclared, skip with PASS; if declared, mismatches are errors. (Confirm degree-vector home in §3; leave \[OPEN\] only if not declared in schemas.)

integrity\_arrays\_as\_sets

For arrays designated as sets in their schemas, enforce §4.2:

* Identity declared & computable (\[OPEN\] where missing in schema).

* No duplicate identities with different element values (conflict).

* After deduplication, ASCII ascending order by identity.

* Fail closed on any conflict or ordering violation.

integrity\_canonicalization\_compare

* For each catalog: parse JSON, re-serialize with §4 canonical rules, and compare bytes to the on-disk file.

* Files must already be canonical (UTF-8, sorted keys, compact, one LF, no BOM).

* Do not auto-rewrite. Any difference is an error.

### **Failure policy**

Any orphan, degree violation, set conflict, out-of-order identity, or non-canonical bytes is a hard failure; CI returns non-zero and blocks the merge.

### **Artifacts (titles and paths only)**

* Topology Integrity Report — artifacts/topology/topology\_coherence\_report.log

* Arrays-as-Sets Report — artifacts/canonical/arrays\_as\_sets\_report.log

* Canonical JSON Gate Compare Log — audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

### **Indexing**

Add these to Appendix D (human) and append records to artifacts/evidence\_index.jsonl (machine) in the same PR (records-only, canonical JSONL, one LF, unknown-keys rejected, each with a proof\_anchor to a path-proof stored alongside the artifact).

### **Environment and determinism**

Run with LC\_ALL=C, LANG=C, TZ=UTC per §4.3.

No wall clock, no randomness, no floats.

### **Acceptance hints (names-only)**

* TOPOLOGY\_NO\_ORPHANS\_OK

* TOPOLOGY\_CHANNEL\_DEGREE\_2\_OK

* TOPOLOGY\_GATE\_CENTER\_OK

* DEGREE\_VECTORS\_MATCH\_OK (when declared)

* ARR\_SET\_IDENTITY\_DECLARED\_OK

* ARR\_SET\_NO\_CONFLICTS\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* FILE\_EQ\_CANON\_BYTES\_OK

* ENV\_LC\_ALL\_C\_OK

## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**

Single home and path

Path (fixed)

* artifacts/evidence\_index.jsonl (there must be exactly one mirror file in the repo).

The mirror has a governed checksum sidecar at `artifacts/evidence_index.jsonl.sha256`. The mirror file and its checksum sidecar MUST each have a sibling `.path_proof.txt` transcript (co-located), including `artifacts/evidence_index.jsonl.path_proof.txt` and `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.

Governed locations only.

Every evidence file referenced by the mirror MUST live under governed repo paths (for example, artifacts/, docs/). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI.

Tracked files (no .gitignore for governed artifacts).

Governed evidence artifacts and their sibling path-proof transcripts (\<artifact\>.path\_proof.txt) MUST NOT be ignored by .gitignore. Governed locations are expected to be tracked; using .gitignore to hide governed artifacts or their path-proofs is invalid and should be treated as a QA failure.

Format (canonical JSONL)

One JSON object per line.

Canonical JSON per §4 for each line:

* UTF-8 (no BOM).

* Sorted keys.

* Compact separators.

* Exactly one trailing \\n per line.

* No blank lines.

* No trailing spaces.

* Unknown keys are rejected (CI-blocking).

Minimum record schema (reject unknown keys)

Each line in the mirror uses at least the following schema; unknown keys are rejected.

{  
 "artifact\_key": "",  
 "role": "\<proof|golden|snapshot|script|log\>",  
 "sha256": "\<lowercase 64-hex\>",  
 "size\_bytes": ,  
 "produced\_at\_utc": "",  
 "discovered\_physical\_path": "",  
 "proof\_anchor": ""  
 }

Bundle-aware extension (evidence bundles, manifests, and epic metadata)

The minimum record schema above remains normative for all Mirror records. This section extends it to cover bundle artifacts, their manifests, and per-epic metadata without changing the core field set or canonical JSONL discipline.

Allowed top-level keys and unknown-key rejection

The Mirror still rejects unknown keys. The only allowed top-level keys for any record are:

Core keys (required for every record):

* artifact\_key

* role

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor

Metadata keys (optional; may appear on any record):

* epic\_id — a short identifier for the owning epic (for example, "HDE-EPIC020"); semantics live in HDE-Phased Epics and Glow QA Guide (titles-only).

* record\_type — a short type label for this record (for example, "epic020\_bundle" or "epic020\_bundle\_manifest"); names are governed by local schemas and tests.

* schema\_version — a version string for the record schema (for example, "1.0").

* notes — free-form, names-only commentary to aid audits; contents are out of scope for PF12 beyond canonical JSON constraints.

* tokens — an array-as-set of acceptance token names (strings) associated with this record; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide. Arrays treated as sets MUST be deduped and ASCII-sorted.

tokens is a non-empty array of token names tied to the EPIC020 acceptance roster; acceptance token names (titles-only) are defined in PF04, while token semantics and gate meaning remain in HDE-Governance and Glow QA Guide.

Bundle-specific keys (optional; bundle rows only):

* bundle\_key — a stable logical identifier for the bundle’s member family (for example, "ordering\_evidence", "sampler\_pool\_snapshots", "config\_bundles", or an epic-specific family such as "epic020\_bundles"); names are governed by local schemas and tests, not by PF12.

* bundle\_manifest\_path — the repo-relative path to the bundle’s manifest JSON/JSONL file if the current record represents the bundle file (the manifest itself is a separate governed artifact with its own Mirror record).

* bundle\_member\_count — an integer counting the number of logical members recorded in the manifest for this bundle.

Non-bundle artifacts (most rows) MUST NOT include any bundle-specific keys.

For those rows, the allowed key set is exactly the core keys plus any applicable metadata keys above; the minimum record schema from the preceding block applies unchanged.

Bundle artifacts and manifests

A bundle artifact is a textual file (JSON/JSONL) that groups multiple logical evidence members. Its Mirror record’s artifact\_key identifies the governed bundle family (for example, "config\_bundle.fe" or a future bundle family defined in §8.6), and discovered\_physical\_path points to the bundle file under artifacts/\*\* or docs/evidence/\*\*.

A bundle manifest is a textual file (JSON/JSONL) that enumerates the bundle’s members (logical artifact\_key, member sha256, size\_bytes, and optional descriptors) and is treated as a separate governed artifact. The manifest has its own Mirror record with its own artifact\_key and discovered\_physical\_path; it MAY use bundle\_key to associate itself with the corresponding bundle artifact.

For selected bundle-based families (as defined in §8.6 and in their per-family subsections), the Human Evidence Index and Machine Evidence Mirror track the bundle file and its manifest as the governed artifacts instead of listing every internal member file as a separate row. Internal member content is addressed by the manifest, not directly by additional Mirror rows.

EPIC-scale example (EPIC020 Candidate 1 bundles)

EPIC020 Candidate 1 evidence bundles follow this pattern:

* Each EPIC020 bundle and manifest has a Mirror record whose artifact\_key is the relevant EPIC020 token (for example, "EPIC020.D1.HTTP\_COMPAT\_MALFORMED\_JSON" or CLI\_SHOWCOMPAT\_CANON\_OK).

* record\_type is "epic020\_bundle" for bundle artifacts and "epic020\_bundle\_manifest" for manifests.

* epic\_id is "HDE-EPIC020".

* tokens is a non-empty array of token names tied to the EPIC020 acceptance roster; schema and ownership of token names live in HDE-Governance and Glow QA Guide.

Other epics may introduce similar patterns with different record\_type and epic\_id values; PF12 remains the single home for the allowed key set and canonical JSONL constraints, while per-epic meaning is defined by PF04/PF19/PF20.

Path-proof semantics for bundles

Each bundle artifact and its manifest MUST have governed sibling path-proof transcripts (\<bundle\_file\>.path\_proof.txt and \<manifest\_file\>.path\_proof.txt) stored alongside each file, whose path, sha256, and size\_bytes match the bundle/manifest file and the corresponding Mirror record values.

For bundle-based families, “per-artifact path proofs” in PF12 are interpreted as “per governed artifact,” where a governed artifact may be either:

* a single artifact file (e.g., a log or JSON snapshot), or

* a bundle artifact or bundle manifest file.

This extension does not introduce hash-only or index-only families. Any future move toward hash-only evidence (no on-disk member payloads) remains out of scope here and requires an explicit reconciliation Doc-Delta (tracked as an OPEN decision in §0.5).

All other Mirror rules remain unchanged: canonical JSONL per §4, single mirror file at artifacts/evidence\_index.jsonl, sort-before-write by (artifact\_key, discovered\_physical\_path), uniqueness of that pair, strict governed-paths rule, and 1:1 parity with the Human Evidence Index.

Self-record semantics (index.machine\_mirror)

The mirror MAY include a single record whose artifact\_key identifies the Machine Evidence Mirror itself (for example, "index.machine\_mirror"). This is the self-record for artifacts/evidence\_index.jsonl.

For this self-record:

* sha256 MUST equal the SHA-256 digest of the mirror’s canonical JSONL body excluding the self-record line.

* size\_bytes MUST equal the byte length of the complete artifacts/evidence\_index.jsonl file including the self-record line.

The associated path-proof transcript for artifacts/evidence\_index.jsonl MUST contain exactly one sha256/size\_bytes pair and those values MUST match the self-record’s sha256 and size\_bytes.

All other mirror records (non self-records) follow the normal mirror discipline: sha256 and size\_bytes are for the referenced artifact at discovered\_physical\_path, and their path-proof transcripts must match those values (see “Path-proof transcript schema”).

Field order and write discipline (merge-blocking)

ASCII field order (exact):

* artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes.

Sort-before-write by the tuple (artifact\_key, discovered\_physical\_path).

Uniqueness: the pair (artifact\_key, discovered\_physical\_path) is unique; duplicates fail CI.

Single mirror file: only one artifacts/evidence\_index.jsonl may exist in the repo.

produced\_at\_utc vs mtime\_utc

produced\_at\_utc records when the evidence was logically produced (the event time). It is part of the mirror record and is used to reason about when posture snapshots and QA runs occurred.

mtime\_utc is recorded in the per-artifact sibling path-proof transcript (\<artifact\>.path\_proof.txt) as the filesystem modification time for the artifact.

Differences between produced\_at\_utc and mtime\_utc are allowed but must be truthful \- no “backdating” or forward-dating to distort ordering. QA may rely on produced\_at\_utc as the primary ordering key for evidence; disagreements should be rare and explainable in the PR.

Path-proof transcript schema (governed artifacts)

Naming (MUST). The sibling path-proof transcript for a governed artifact MUST be named \<artifact\>.path\_proof.txt, where \<artifact\> includes the artifact’s full filename including extension. Example: audit/gates/determinism/env\_pins.log → audit/gates/determinism/env\_pins.log.path\_proof.txt (not env\_pins.path\_proof.txt).

For every governed artifact in §8.6, the path-proof transcript MUST be a co-located sibling file named \<artifact\>.path\_proof.txt. It MUST describe exactly one artifact and follow a stable, line-oriented schema.

Required fields (exactly one record per file)

Each path-proof MUST contain exactly one record for the artifact it describes, with the following required fields:

* path — repo-relative path to the artifact (for example artifacts/engine/order/channels\_sorted.snapshot.json).

* sha256 — lowercase 64-hex SHA-256 digest of the artifact’s canonical bytes.

* size\_bytes — non-negative integer byte length of the artifact’s canonical bytes.

* mtime\_utc — UTC ISO-8601 timestamp (e.g. YYYY-MM-DDThh:mm:ssZ) representing the artifact’s refresh-time mtime (see “mtime\_utc semantics” below).

* produced\_at\_utc — UTC ISO-8601 time when the evidence for this artifact was logically produced.

These fields MUST appear exactly once per file; path-proofs MUST NOT contain multiple or conflicting sha256/size\_bytes pairs, nor multiple mtime\_utc or produced\_at\_utc values for the same artifact.

Optional fields

Path-proof transcripts MAY include additional informational fields beyond the required set above, but those fields:

* MUST NOT change acceptance semantics, and

* MUST NOT conflict with the required record for path, sha256, size\_bytes, mtime\_utc, or produced\_at\_utc.

The authoritative truth remains the match between:

* the artifact’s canonical bytes,

* the mirror record’s sha256 and size\_bytes, and

* the path-proof’s single sha256/size\_bytes triple for that artifact.

Relationship to proof\_anchor

Each mirror record’s proof\_anchor field MUST equal the path to the corresponding .path\_proof.txt for that artifact.

CI MUST verify that:

* the file referenced by proof\_anchor exists under governed paths,

* its path matches the mirror’s discovered\_physical\_path,

* its sha256/size\_bytes match the mirror record’s sha256/size\_bytes, and

* there are no duplicate or conflicting sha256/size\_bytes entries within the path-proof.

Failure of any of these conditions is a hard error under the mirror/index tokens declared in §8.3 and §0.2.

mtime\_utc semantics (normative)

Refresh-time mtime

mtime\_utc records the artifact’s refresh-time mtime: the filesystem modification time observed when the evidence job refreshed that artifact, encoded as a UTC ISO-8601 timestamp (YYYY-MM-DDThh:mm:ssZ) with no fractional seconds (microsecond component MUST be zero).

Monotone vs filesystem stat()

On any run that writes or checks a path-proof, the evidence tooling MUST verify that mtime\_utc parses as UTC (with microsecond \== 0\) and that parsed\_mtime \<= current\_fs\_mtime, where current\_fs\_mtime is the artifact’s stat().st\_mtime observed at check time.

mtime\_utc is not required to be exactly equal to stat().st\_mtime; it is permitted to be earlier (for example, when a proof is refreshed without the underlying file changing) but MUST NOT lie in the future relative to the current filesystem mtime.

Interaction with produced\_at\_utc

produced\_at\_utc captures when the evidence for the artifact was logically produced (the evidence refresh event). It is also a UTC ISO-8601 timestamp and may be updated on each refresh or left unchanged when appropriate.

It is expected, but not strictly required, that produced\_at\_utc be greater than or equal to prior produced\_at\_utc values for the same artifact; any non-monotone behavior should be rare and explained in the PR.

Integrity semantics

The primary integrity check for governed evidence remains the equality of sha256 and size\_bytes between:

* the artifact’s canonical bytes on disk,

* the Machine Mirror record (§8.3), and

* the single record in the path-proof transcript.

mtime\_utc and produced\_at\_utc provide temporal context and are enforced for format and monotone constraints as described above; they do not replace the sha/size equality as the core integrity proof.

Alignment with tools and QA

Evidence tooling (tools/evidence/update\_evidence\_index.py) and CI checks (ci/checks/check\_mirror\_schema.sh) MUST implement these semantics:

* when writing path-proofs, always recompute size\_bytes and sha256 from the artifact’s canonical bytes

* set or carry forward mtime\_utc as the refresh-time mtime, and validate that it is a UTC ISO timestamp with microsecond \== 0 and mtime\_utc \<= current\_fs\_mtime

* set or carry forward produced\_at\_utc as the evidence refresh time.

Evidence tests (for example, tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py) MUST assert these same semantics (format \+ monotone \<= stat\_mtime) and MUST be kept in sync with this section.

Change control

Any change to the definition or validation of mtime\_utc or produced\_at\_utc semantics is a normative change and requires:

* a PF12 Doc-Delta (§9),

* synchronized updates to PF19 (Glow QA Guide) and PF10 Build Notes, and

* updates to the evidence tooling and tests that enforce these semantics.

Join to the human index (parity, proofs, same-PR rule)

1:1 parity.

Every §8.6 Evidence Index entry has exactly one mirror record, and every mirror record has a corresponding human entry:

* artifact\_key equals the Human Index title.

* discovered\_physical\_path equals the Human Index path.

Path-proofs.

Each artifact’s directory contains a stored path-proof (for example, path\_proof.txt with a stat transcript). The mirror record’s proof\_anchor must exactly match the stored path-proof for that artifact.

Same-PR rule.

For every governed artifact in §8.6, any change to the artifact MUST update, in the same PR:

* The artifact bytes on disk under a governed path.

* Its sibling \<artifact\>.path\_proof.txt path-proof transcript (the proof\_anchor target).

* The corresponding machine mirror record in artifacts/evidence\_index.jsonl.

* The Human Evidence Index entry in docs/evidence/INDEX.json and its hash sentinel docs/evidence/INDEX.sha256.

Mirror or index entries that refer to non-existent artifacts or stale path-proofs are invalid and must be corrected, not ignored.

Troubleshooting (common failure mode): governed artifact drift

A governed artifact is considered drifted when any of the following disagree:

* the artifact’s on-disk bytes

* its sibling \*.path\_proof.txt (sha256 and size\_bytes)

* the corresponding Machine Mirror record (sha256 and size\_bytes for the same discovered\_physical\_path)

This is a hard evidence integrity failure. Do not hand-edit proofs or mirror records to “make the check pass”.

Correct remediation (single writer):

* Ensure docs/evidence/INDEX.json reflects the intended titles and paths.

* Run tools/evidence/update\_evidence\_index.py in write mode to regenerate:

  * docs/evidence/INDEX.sha256

  * artifacts/evidence\_index.jsonl

  * all governed \*.path\_proof.txt transcripts

* Re-run the tool in \--check mode and fix any remaining mismatches before merge.

Determinism

All checks run with LC\_ALL=C, LANG=C, TZ=UTC.

JSONL records are canonical and LF-terminated (exactly one \\n per record).

Header snapshots in artifacts (normative)

For artifacts that capture headers, header names MUST be lower-case and values MUST be verbatim; exact checks apply to values.

Capture hygiene (normative).

Header snapshot artifacts MUST contain header lines only.

Tool warnings or stderr output (for example, curl warnings) MUST NOT be mixed into header snapshot bytes.

If the capture command can emit warnings, capture stderr separately (for example, to a sibling \*.stderr.txt or a step log) or filter non-header lines before writing the governed artifact.

Wire casing may differ and is validated by transport owners.

Acceptance hint (names-only): SNAPSHOT\_HEADER\_LOWERCASE\_OK.

Refusal proofs (policy note)

Refusal proofs are error/ops evidence (not JSON success). They must:

* Not set ETag, Vary, or compression headers.

* Use Content-Type: application/json; charset=utf-8.

The refusal log allow-list for JSON body fields is exactly:

* {at, route, status, duration\_ms, idempotence\_hash, release\_id}

Records with any additional fields fail policy checks.

Rate-limit (429) evidence uses a different allow-list and is governed by HDE-Governance. Do not mix refusal and 429 fields in the mirror.

Refresh sequence (normative)

When governed evidence artifacts change, the canonical refresh sequence is:

* Update docs/evidence/INDEX.json with the new or changed titles and paths.

* Run python tools/evidence/update\_evidence\_index.py in write mode to regenerate:

  * docs/evidence/INDEX.sha256

  * artifacts/evidence\_index.jsonl

  * all governed \*.path\_proof.txt transcripts

* Run the mirror schema/shape check job (canonical CI invocation: ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl) and fix any discrepancies before merge.

Operator note (invocation; avoid bash drift).

ci/checks/check\_mirror\_schema.sh is a Python entrypoint (script file with a Python shebang) and CI invokes it directly. When an acceptance artifact or runbook needs an explicit command, the canonical invocation is:

* ci/checks/check\_mirror\_schema.sh artifacts/evidence\_index.jsonl

Acceptance artifacts may list either:

* the script path (ci/checks/check\_mirror\_schema.sh) as a tool reference, or

* the explicit direct command above as an invocation.

bash ci/checks/check\_mirror\_schema.sh is invalid and MUST NOT appear in approved acceptance artifacts or operator instructions.

Process and PR workflow (who runs which command and when) remains single-homed in Epic-Process-Guide; this section pins file-level ordering and artifacts that MUST be updated together.

Role usage notes (non-normative examples)

* proof → artifacts/db/ddl\_fingerprint.json, artifacts/proofs/endpoints\_env\_gate\_proof.log, artifacts/bodygraph/source\_invariance/ab.json, /ba.json, /summary.json

* golden → catalog/manifest.json, catalog/schemas/\*.json

* snapshot → artifacts/runtime/env\_matrix.snapshot.json, artifacts/reader/endpoints\_snapshot.json, artifacts/bodygraph/refresh\_policy.snapshot.json, artifacts/bodygraph/metrics.snapshot.json

* script → scripts/card\_close.sh, scripts/migration\_runner.sh

* log → artifacts/db/migration\_runner.log, artifacts/proofs/headers\_probe.log, artifacts/bodygraph/keys\_only.logs.sample (sanitized; keys-only, no PII per Governance)

Artifacts with generated\_at\_utc (provenance discipline, including sampler and Engine Core evidence)

Some governed artifacts (for example, sampler evidence artifacts under artifacts/sampler/\*\* and Engine Core evidence artifacts under artifacts/core/\*\*) include a generated\_at\_utc field in their own JSON payloads. For these artifact families, provenance discipline tightens the relationship between the payload timestamp and the evidence timestamps recorded in the Machine Mirror and path-proofs.

Normative rules (in addition to the general rules in this section)

When an artifact carries a generated\_at\_utc field in its payload, the evidence tooling MUST treat that field as the artifact’s self-reported generation time for the current refresh and enforce all of the following:

* produced\_at\_utc in the Machine Evidence Mirror record for that artifact MUST NOT be earlier than the artifact’s generated\_at\_utc value. Backdating Mirror produced\_at\_utc relative to generated\_at\_utc is not allowed.

* produced\_at\_utc in the Machine Evidence Mirror record and produced\_at\_utc in the artifact’s path-proof transcript MUST be identical strings (same UTC ISO-8601 representation). Mirror and path-proof timestamps MUST stay in lockstep for a given artifact.

* mtime\_utc in the path-proof remains the refresh-time filesystem mtime (see “mtime\_utc semantics” above) and MUST NOT be later than the artifact’s current filesystem stat().st\_mtime at check time. mtime\_utc may be earlier than generated\_at\_utc (for example, when an artifact’s content has not changed between runs but evidence is refreshed), but sha256 and size\_bytes MUST still match.

For governed families that include both generated\_at\_utc and produced\_at\_utc (including the sampler families registered in §8.6.3 and the Engine Core families engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, and engine\_core\_json\_compare\_logs), provenance correctness for a given refresh requires:

* the artifact’s payload generated\_at\_utc and the Mirror produced\_at\_utc to describe the same refresh window (produced\_at\_utc ≥ generated\_at\_utc in UTC time), and

* the path-proof produced\_at\_utc to match the Mirror produced\_at\_utc exactly.

Integrity gates for these artifacts continue to rely primarily on sha256 and size\_bytes equality across artifact, Mirror record, and path-proof. Timestamp checks are additive: format, monotonicity (per “mtime\_utc semantics”), and the non-backdating rule relative to payload generated\_at\_utc are enforced in addition to the existing sha/size equality rules.

Example — sampler and Engine Core evidence fixes (HDE-EPIC019)

In earlier EPIC019 work, sampler Mirror records and path-proofs for sampler\_pool\_snapshots, sampler\_two\_run\_logs, sampler\_abba\_logs, sampler\_diversity\_artifacts, and sampler\_seed\_replay\_logs carried produced\_at\_utc values copied from an older skeleton baseline even after the artifacts themselves were regenerated with later generated\_at\_utc timestamps. Engine Core evidence families added in PR7 (engine\_core\_purity\_report, engine\_core\_two\_run\_logs, engine\_core\_abba\_logs, engine\_core\_json\_compare\_logs) were wired with generated\_at\_utc and closed-rails env metadata from the start.

The EPIC019 bugfix refreshed Mirror records and path-proofs so that:

* sampler artifacts under artifacts/sampler/\*\* and Engine Core artifacts under artifacts/core/\*\* retain canonical bytes (sha256 and size\_bytes unchanged when content is unchanged)

* their payload generated\_at\_utc values reflect the actual regeneration time for the latest evidence run, and

* produced\_at\_utc in both Mirror and path-proofs is updated to the later refresh time, satisfying the non-backdating rule above and restoring consistency between payload generation timestamps and evidence timestamps for all families that carry generated\_at\_utc.

Tools and tests

Evidence tooling (for example, tools/evidence/update\_evidence\_index.py and any Engine Core/sampler-specific generators) and Mirror schema checks MUST implement these provenance rules whenever an artifact family introduces a payload-level generated\_at\_utc field.

Tests that exercise those families (for example, sampler evidence tests under tests/evidence/ and Engine Core evidence tests under tests/evidence/test\_engine\_core\_evidence.py) SHOULD assert that:

* produced\_at\_utc in Mirror and path-proofs matches for each artifact instance, and

* where generated\_at\_utc is present, Mirror produced\_at\_utc is not earlier than payload generated\_at\_utc.

Change control

Any change to the relationship between payload generated\_at\_utc and evidence produced\_at\_utc semantics is a normative change and MUST land with:

* a PF12 Doc-Delta (§9),

* synchronized updates to the relevant Mechanics/QA specs that describe Engine Core and sampler evidence behavior, and

* synchronized changes to the evidence tools and tests that enforce these semantics before the change is considered accepted.

## **8.6 Evidence Index entries (titles/paths only) \[Required-Now\]**

## **8.6.1 Discipline**

Update both the Human Index and the Machine Mirror in the same PR:

* Human Index: docs/evidence/INDEX.json

* Machine Mirror: artifacts/evidence\_index.jsonl

Governed path-proof transcripts (required). The Human Index and its hash sentinel MUST each have a sibling `.path_proof.txt` transcript:

* `docs/evidence/INDEX.json.path_proof.txt`

* `docs/evidence/INDEX.sha256.path_proof.txt`

Machine Mirror discipline:

* Records-only JSONL

* Canonical JSONL

* Exactly one LF per record

* Unknown-key rejection

* ASCII field order

* Sort-before-write

* Single mirror file

* proof\_anchor present and valid for every record

Process and CI posture:

* Detailed PR/workflow process is defined in Epic-Process-Guide (titles-only).

* Acceptance sentinel gating behavior is defined in PF12 front-matter and Governance (titles-only).

Canonical evidence-path binding validation (MUST).

When any acceptance token is claimed as satisfied (in an Epic Plan, acceptance map/manifest, or token\_evidence\_matrix), every token→evidence binding MUST be validated against PF12’s Evidence Catalog and any fixed canonical paths it defines.

If the Evidence Catalog defines a fixed canonical path for a token’s evidence surface, then the Plan/matrix/acceptance artifacts MUST bind to that exact path.

Any binding to a non-canonical path is a mechanical blocker and MUST be corrected before approval/merge. If a non-canonical path is truly required, it MUST be routed via an explicit decision process and drained into the correct canonical home; do not silently substitute paths.

Primary evidence vs path-proof transcripts (clarification).

Acceptance artifacts (Epic Plans, acceptance maps/manifests, token/evidence matrices) MUST bind tokens to the primary governed artifact paths listed in the Evidence Catalog.

\*.path\_proof.txt files are required integrity transcripts. They MUST exist and stay in sync, but they are not primary evidence targets.

Therefore, acceptance artifacts MUST NOT bind tokens directly to \*.path\_proof.txt as their evidence surface. The only approved linkage to a path-proof is via the Machine Mirror proof\_anchor for the primary artifact.

Minimum required artifacts that MUST agree when a token is claimed

For every claimed token, the following MUST be mutually consistent (same artifact\_key / same discovered\_physical\_path, and the same bytes-hash and size at the Index/Mirror/proof level):

* The Epic Plan’s required-evidence list entry (titles/paths only, per deliverable).

* The token\_evidence\_matrix row for the token.

* The Human Evidence Index entry in docs/evidence/INDEX.json.

* The Machine Evidence Mirror record in artifacts/evidence\_index.jsonl for the same (artifact\_key, discovered\_physical\_path).

* The governed path-proof referenced by the mirror record’s proof\_anchor.

Shared/global evidence dependencies (do not assume implicit).

Some governed evidence surfaces are shared across many deliverables and may live outside a deliverable’s “local bundle” directory. When a deliverable’s acceptance depends on shared/global evidence surfaces, they must be explicitly listed and bound by canonical path rather than assumed to be “implicitly available.” PF12’s role is to define canonical paths and evidence families; workflow enforcement and review gates are routed by title to the Epic-Process-Guide and Glow QA Guide.

Remediation-only artifacts (MUST).

Remediation-only diagnostics and manifests MUST NOT be introduced under governed Evidence Index / Machine Mirror surfaces unless explicitly adopted via a PF12 Doc-Delta into the Evidence Catalog. Default posture: remediation-only artifacts live under remediation audit paths (for example, audit/qa/\<epic-id\>/remediation/) and do not enter the Human Evidence Index or Machine Evidence Mirror.

Example remediation subtree (current-state; EPIC024 dev acceptance artifacts):

* `audit/qa/<epic-id>/remediation/s2_dev_acceptance_artifacts/acceptance_map_viability.json`: Remediation JSON report (current-state EPIC024 schema: `epic024.acceptance_map_viability.v1`).

* `audit/qa/<epic-id>/remediation/s2_dev_acceptance_artifacts/token_evidence_matrix_scope.md`: Remediation markdown scope note containing a canonicalized acceptance tokens table.

Index and mirror fixed filenames (for plans/tasks that touch governed indices/mirrors).

Evidence index (human-readable):

* docs/evidence/INDEX.json

* docs/evidence/INDEX.sha256

* docs/evidence/INDEX.json.path\_proof.txt

* docs/evidence/INDEX.sha256.path\_proof.txt

Evidence index mirror (machine-readable):

* artifacts/evidence\_index.jsonl

* artifacts/evidence\_index.jsonl.sha256

* artifacts/evidence\_index.jsonl.path\_proof.txt

* artifacts/evidence\_index.jsonl.sha256.path\_proof.txt

Plans and tasks that touch any file above MUST treat the mirror checksum sidecar and both sibling .path\_proof.txt transcripts as first-class deliverables. If a plan proposes a new file under governed roots, it MUST state whether the file is intended to appear in the indices/mirror; absence of that statement is a mechanical blocker.

Evidence-output naming discipline (plans and token claims; normative).

Plans and acceptance artifacts MUST name the primary governed evidence outputs that will be committed and indexed for the epic or PR.

Token-claim evidence outputs MUST be concrete, filename-specific, and indexable. Therefore, acceptance artifacts MUST NOT bind tokens to directory families, wildcard patterns, or vague family phrases such as “plus step logs”.

Plans SHOULD avoid wildcards in required-evidence lines even when a canon-defined path-pattern exists for discovery. If a path-pattern exists for discovery or enumeration, the plan SHOULD still bind the token to the concrete primary artifact instance(s) (exact path and filename) that will appear as records in the Human Evidence Index and Machine Evidence Mirror for the PR or QA run.

If a tool produces a high-churn set of member logs, the plan MAY treat the governed output as a single primary artifact (for example, a manifest or bundle) and state that member files are referenced by that primary artifact, provided the plan names the primary governed artifact by exact path and filename and keeps evidence binding deterministic. Member files SHOULD be referenced by the manifest/bundle rather than being individually required in the plan’s evidence-output lines unless the Evidence Catalog explicitly promotes them as primary governed evidence surfaces.

Acceptance map — token identity and shape (clarification).

This section clarifies how acceptance tokens are identified inside acceptance-map artifacts. This prevents token identity drift when acceptance maps are rendered as tables.

Rule (normative).

In acceptance maps, tokens are identified by the tokens\[\].name field (case-sensitive, exact-match), not by any display label or table header text.

Acceptance-map artifacts MUST include a top-level tokens array.

Each tokens\[\] entry MUST be an object.

Each tokens\[\] entry MUST include a name field whose value is a non-empty string.

tokens\[\].token\_name MAY be present as an alias/display label for compatibility, but it is non-authoritative; downstream validators MUST NOT require token\_name and MUST NOT use it as the token’s identity.

Implications for QA validators and plans.

QA plans and validators MUST derive token identity from tokens\[\].name.

QA plans and validators MUST NOT guess field keys or treat matrix/table header labels (for example token\_name) as tokens.

---

### **8.6.2 Parity rule (MUST)**

In any PR that changes governed evidence artifacts or their indexing, you MUST update all of the following together:

* docs/evidence/INDEX.json (Human Index)

* docs/evidence/INDEX.sha256 (hash sentinel)

* artifacts/evidence\_index.jsonl (Machine Evidence Mirror)

* artifacts/evidence\_index.jsonl.sha256 (Machine Evidence Mirror checksum sidecar)

* The governed sibling \*.path\_proof.txt transcripts for every changed index/mirror file above

And you MUST assert the mirror/index tokens named in §8.3 (for example, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, etc.) on every change.

Whole-family same-change closeout rule (MUST).

For evidence-indexing closeout claims, success MUST be evaluated across the whole set of governed evidence families whose bytes changed in the scoped run.

If the same scoped run changes more than one governed evidence family, closeout is satisfied only when every changed family is refreshed in that same run, indexed and mirrored coherently, and backed by current sibling `.path_proof.txt` transcripts where PF12 requires them.

A green result for one changed subfamily MUST NOT be used as a proxy for whole-family coherence. “Authoritative family fixed” is not equivalent to “whole changed family coherent.”

Path-proof churn review grouping.

Broad path-proof churn across governed artifacts is review load, not scope drift by itself.

When a scoped run refreshes many path-proof companions or mirror rows, review SHOULD group the changes by governed evidence family and verify:

* the changed payload artifact  
* the changed path-proof companion  
* the Human Evidence Index entry  
* the Machine Evidence Mirror row  
* any required checksum sidecar  
* the cause of the refresh

A broad refresh MAY be classified as non-blocking scope churn only when every changed governed artifact remains cataloged in PF12 or another owning PF home, every changed path-proof validates against its target artifact, and the Human Index, Machine Mirror, checksum sidecars, and path-proof records remain coherent for the same change.

Duplicate or repeated evidence-refresh hunks SHOULD be consolidated or summarized for review, but consolidation MUST NOT hide any changed governed artifact, proof anchor, sha256, size\_bytes, or discovered\_physical\_path.

### 8.6.3 Entries (authoritative list; titles/paths only)

#### 8.6.3.1 Catalog governance and root discipline

**Multi-root evidence catalog rule (normative).** The Evidence Catalog is intentionally multi-root: governed evidence artifacts are expected to exist under multiple repo roots, for example `audit/`, `artifacts/`, `docs/`, `catalog/`, and `narratives/`. In evidence terms, the single-home constraint means PF12 is the single authoritative home for evidence family naming, canonical path bindings, and the Index and Mirror discipline that binds those paths. It does not mean evidence must live under a single directory.

Multi-root storage is not, by itself, evidence drift. Drift occurs when a root or artifact is treated as governed evidence or a truth-home output but is not cataloged here and is not indexed and mirrored with exactly one governed `*.path_proof.txt` transcript.

**Root classification rule (normative).** If any additional top-level root is treated as governed evidence, for example `scripts/` or `tools/`, its evidence outputs MUST either:

* be cataloged in §8.6 as explicit evidence families with titles and canonical paths, and indexed and mirrored per §8.3; or  
* be treated as non-governed tooling outputs and excluded from truth-home claims, meaning not indexed, not mirrored, and not accepted as evidence.

Observed multi-root distribution across existing governed roots does not, by itself, expand the Evidence Catalog or create a new governed root.

Revisit evidence-root classification or root proliferation only when future work proposes either:

* a new governed root; or  
* a second truth home for an existing governed evidence family.

Absent one of those proposals, observed multi-root distribution is handled under the classification rule above and is not, by itself, a canon-change trigger.

Human Index entries are titles and paths only. Machine Mirror records include at least `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor`. Unless a family-specific note narrows the rule, every artifact listed below MUST have exactly one Human Index entry, one Machine Mirror record, and one governed sibling `*.path_proof.txt` transcript, all kept in lockstep.

#### 8.6.3.2 Core pack, canonical JSON, topology, and deterministic order

##### Freeze-pack and math

* `artifacts/math/freeze_pack_manifest.json`  
* `artifacts/math/release_id.txt`  
* `artifacts/math/release_id_recompute.log`  
* `artifacts/math/checksums_audit.log`  
* `artifacts/math/manifest_snapshot.json`

##### Canonical JSON and topology

* `artifacts/canonical/arrays_as_sets_report.log`  
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
* `audit/gates/json_gate/canonical/json_gate_structured_record.json` (optional)  
* `audit/gates/canonical_json/canonical_json.gate.json`  
* `audit/gates/canonical_json/json_canon_compare.log`  
* `audit/gates/canonical_json/json_canonical_check.log` The audit/gates/canonical\_json/ family is a supplemental legacy canonical-JSON gate family. While this family is still produced by the repo, it remains governed evidence under PF12. If any member of this family changes in a run, each changed member and its sibling .path\_proof.txt transcript MUST be refreshed in that same run, and the broader same-change requirement applies alongside the authoritative audit/gates/json\_gate/canonical/ family.  
* `artifacts/topology/topology_coherence.log`

##### Evidence Index snapshot (gate family)

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

##### Topology orientation demo

* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/degree_check.log`  
* `audit/gates/topology/multiplicity_vector.log` Each artifact above MUST have a co-located sibling path-proof transcript named .path\_proof.txt, for example audit/gates/topology/orientation\_demo.txt.path\_proof.txt. Canonical predicate targets (D16) are audit/gates/topology/orientation\_demo.txt and audit/gates/topology/orientation\_demo.txt.path\_proof.txt. These artifacts form the topology.orientation\_demo family and serve as the exemplar for path-proof validation and topology invariants. Each MUST be indexed in both the Human Evidence Index and the Machine Evidence Mirror with matching path-proofs.

##### Deterministic order and comparators \[Required-Now\]

* `artifacts/engine/order/props_total_order.log`: log of ordering properties and invariants, including antisymmetry, transitivity, and totality, for the canonical comparators.  
* `artifacts/engine/order/channels_sorted.snapshot.json`: canonical JSON snapshot of channels in comparator order.  
* `artifacts/engine/order/categories_iter.snapshot.json`: canonical JSON snapshot of categories in comparator order.  
* `artifacts/engine/order/abba_identity.bytes`: binary AB↔BA identity sample for comparator behavior, governed by the same Mirror and path-proof discipline as other artifacts in this section, including abba\_identity.bytes.path\_proof.txt.

#### 8.6.3.3 Reader, CLI, compat, and conjunction evidence

##### Endpoint Catalog and A7 proofs

* `artifacts/reader/endpoints_snapshot.json`  
* `artifacts/proofs/endpoints_env_gate_proof.log`  
* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`  
* `artifacts/proofs/success_encoding_invariance.txt` (optional)  
* `artifacts/proofs/reader_success_get_head_304.json`: composite proof; schema owned by the Endpoint Catalog evidence section (§8.12).

##### Aux Narrative (text) — header snapshots

* `tests/transport/headers/aux_text_200.snap`  
* `tests/transport/headers/aux_suppression_200.snap`

##### CLI Admin Preview (narrative) — evidence

* `artifacts/cli/narrative/stdout.txt`: LF-terminated narrative text; no ANSI.  
* `artifacts/cli/narrative/sidecar.json`: IDs-only payload with composition\_id, fragment\_ids\[\], pack\_sha, and optional release\_id; canonical JSON.

##### Conjunction writer evidence (EPIC027)

**Purpose.** Govern the explicit conjunction writer proof artifacts for the existing /dev/writer/conjunction proof path without turning that writer proof path into an A7 proof family.

**Artifact paths.**

* `artifacts/writer/conjunction_write_readback.log`: Governed writer log for the /dev/writer/conjunction proof family. When refreshed, it records writer\_invalid\_status, writer\_success\_type, and writer\_error\_type for the current family state.  
* `artifacts/writer/conjunction_writer_summary.json`: Governed writer summary snapshot for the same family. Canonical JSON when present. When refreshed, it records writer\_success\_typed\_envelope and writer\_error\_typed\_envelope for the current family state.

**Artifact-key bindings.**

* `conjunction.writer.write_readback` — `artifacts/writer/conjunction_write_readback.log`.  
* `conjunction.writer.summary` — `artifacts/writer/conjunction_writer_summary.json`.

**Path-proofs and indexing.**

Each artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. For EPIC-027, close-pack claims about executed closure workflow are governed truthfulness claims. If the EPIC027 close report, manifest, or generator output says that same-run evidence-refresh or validation lanes ran, that claim MUST be backed by same-run QA gate logs under the EPIC027 QA root. The current EPIC027 truthfulness-anchor log set is:

* `audit/qa/hde-epic027/checks/gate_update_evidence_index_write/primary.log`  
* `audit/qa/hde-epic027/checks/gate_update_evidence_index_check/primary.log`  
* `audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log`  
* `audit/qa/hde-epic027/checks/gate_evidence_paths_validation/primary.log`  
* `audit/qa/hde-epic027/checks/gate_lf_endings/primary.log`  
* `audit/qa/hde-epic027/checks/gate_orientation_demo_write/primary.log` The EPIC027 token matrix and close-pack bindings MUST treat the relevant log paths above as the backing execution anchors when they claim the corresponding closure lanes ran.

**Chronology posture.**

When this family changes, the writer artifacts, their sibling path-proofs, and any changed index or mirror companion proofs MUST be refreshed with current chronology under the existing PF12 mtime\_utc and produced\_at\_utc integrity rules.

##### CLI showcompat (deterministic capture) — evidence (EPIC022 D2)

* `artifacts/cli/showcompat/stdout.json`: deterministic capture of hdctl showcompat stdout bytes; LF-terminated; success has empty stderr; emitted via the canonical serializer required by CLI evidence posture.  
* `artifacts/cli/showcompat/stdout.json.sha256`: SHA-256 sidecar for stdout.json capture bytes.  
* `artifacts/cli/showcompat/stdout.sha256`: allowed legacy alias of stdout.json.sha256 for EPIC022 D2. Evidence wiring MUST normalize this alias to stdout.json.sha256. New producers MUST NOT emit stdout.sha256. If both are present they MUST match.  
* `artifacts/cli/showcompat/args.json`: names-only arguments and environment snapshot used for deterministic capture; no secrets; canonical JSON.  
* `tools/cli/generate_showcompat_artifacts.py`: deterministic producer tool used to generate the EPIC022 D2 showcompat capture artifacts under closed rails.

**Functional showcompat QA posture (vendor dependency; current limitation).**

The deterministic showcompat capture artifacts above are byte-determinism evidence and do not imply that functional showcompat runs can be executed under closed rails. Until BodyGraph storage or replay exists for QA, functional showcompat runs cannot rely on precomputed BodyGraph inputs being available locally. Any Live QA step that executes showcompat in a context where BodyGraph data is not already available MUST run that step with vendor rails open. Closed rails, meaning network disabled, MUST be treated as an expected blocker for functional showcompat runs under this limitation. The rails change MUST be explicit and step-scoped. After the showcompat step, restore the default rails posture. showcompat MUST NOT be executed as a zero-argument command in QA plans or QA runs. The authoritative command and argument contract is owned by HDE-CLI-API-Vendor-Ref. If showcompat is attempted under closed rails or without required arguments, classify the outcome as a tooling, environment, or usage defect for that step, not a product behavior failure. Record the rails posture used, names-only, and the failure signature in the step log.

##### Compat closure artifacts

* `artifacts/compat/AB.json`: governed compat proof artifact for canonical AB ordering bytes; canonical single-line JSON.  
* `artifacts/compat/BA.json`: governed compat proof artifact for canonical BA ordering bytes; canonical single-line JSON; matches the AB proof family bytes for the same pair.  
* `artifacts/compat/identity_hash.txt`: primary governed compat-closure artifact for explicit conjunction identity-hash capture. Its bytes MUST match the canonical AB compat bytes for the same pair. Family-scoped compat closure checks MAY target artifacts/compat/identity\_hash.txt directly when a compat-only slice is being validated, but those targeted checks MUST NOT narrow or replace same-PR updates and validations for docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, artifacts/evidence\_index.jsonl.sha256, or the governed sibling .path\_proof.txt transcripts required elsewhere in PF12 when governed evidence bytes change.

##### HDE-EPIC030 PR-01 normalization evidence

**Purpose.** Govern the direct PR-01 normalization evidence family for the existing viewer-preference normalization and compat surfaces. This family is slice evidence only. It does not create a new public route, new public surface, serializer path, or close-stage artifact family.

**Primary artifact paths.**

* `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log`: Direct PR-01 log artifact for invalid viewer-preference cases. When refreshed, it records invalid-shape and invalid-ID checks for normalization evidence.  
* `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log`: Direct PR-01 log artifact for normalization canonicalization comparison. When refreshed, it records normalized SHA-256 reparse comparison and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json`: Direct PR-01 canonical JSON artifact for zero-weight handoff from normalized viewer preferences into sampler exclusion evidence. When refreshed, it records the sampler handoff entrypoint and excluded or retained candidate IDs.

**Artifact-key bindings.**

* `epic030.pr01.invalid_viewer_prefs` maps to `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log`.  
* `epic030.pr01.normalization_canonical_compare` maps to `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log`.  
* `epic030.pr01.zero_weight_handoff` maps to `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json`.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the three primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC030 PR-02 dev-sampler evidence

**Purpose.** Govern the direct PR-02 dev-sampler evidence family for the existing internal/dev sampler harness. This family is slice evidence only. It does not create a new public route, new public surface, serializer path, endpoint-catalog success route, or close-stage artifact family.

**Primary artifact paths.**

* `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt`: Direct PR-02 text snapshot for the dev-sampler HTTP response headers. When refreshed, it records route, method, status, content type, Cache-Control, ETag presence, and APP\_ENV posture for the existing internal/dev sampler surface.  
* `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json`: Direct PR-02 canonical JSON snapshot for the dev-sampler HTTP response body. When refreshed, it records the viewer ID, ordered candidate IDs, and meta.seed only for the existing sampler harness output proof.  
* `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json`: Direct PR-02 canonical JSON proof artifact for byte-stable two-run identity on the same dev-sampler request.  
* `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json`: Direct PR-02 canonical JSON proof artifact showing that seed changes remain metadata-only for the dev-sampler harness and do not alter candidate IDs.

**Artifact-key bindings.**

* `epic030.pr02.dev_sampler_http_headers` maps to `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt`.  
* `epic030.pr02.dev_sampler_http_body` maps to `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json`.  
* `epic030.pr02.dev_sampler_two_run_identity` maps to `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json`.  
* `epic030.pr02.dev_sampler_seed_only` maps to `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json`.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the four primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC030 PR-03 compat evidence and indexing evidence

**Purpose.** Govern the direct PR-03 compat evidence family and the reused compat-family bindings for the existing compat evidence and narrative-key linkage surfaces. This family is slice evidence only. It does not create a new public route, new public surface, serializer path, endpoint-catalog success route, or close-stage artifact family.

**Primary artifact paths.**

* `audit/qa/hde-epic030/pr-03/category_order_binding.log`: Direct PR-03 log artifact for Magic-10 category-order binding. When refreshed, it records the binding family, frozen order source, category order, task/subtask binding, and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-03/compat_identity_binding.log`: Direct PR-03 log artifact for compat identity-hash binding. When refreshed, it records identity-hash comparison against AB and BA compat artifacts and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-03/compat_parity_binding.log`: Direct PR-03 log artifact for compat AB↔BA parity binding. When refreshed, it records AB and BA SHA-256 values, byte-level equality, structural equality, and PASS/FAIL status.  
* `artifacts/narratives/key_table_10x2.snapshot.json`: Governed PR-03 narrative key-table linkage snapshot for the compat evidence family. When refreshed, it materializes the ten-category by two-key linkage used by the compat evidence slice. Reused compat-family paths.  
* `artifacts/compat/AB.json`: Existing governed compat proof artifact for canonical AB ordering bytes. When refreshed for this family, it MUST have a sibling .path\_proof.txt transcript and a matching Human Index and Machine Mirror binding.  
* `artifacts/compat/BA.json`: Existing governed compat proof artifact for canonical BA ordering bytes. When refreshed for this family, it MUST have a sibling .path\_proof.txt transcript and a matching Human Index and Machine Mirror binding.

**Artifact-key bindings.**

* `epic030.pr03.category_order_binding` maps to `audit/qa/hde-epic030/pr-03/category_order_binding.log`.  
* `epic030.pr03.compat_identity_binding` maps to `audit/qa/hde-epic030/pr-03/compat_identity_binding.log`.  
* `epic030.pr03.compat_parity_binding` maps to `audit/qa/hde-epic030/pr-03/compat_parity_binding.log`.  
* `compat.narratives.key_table_10x2` maps to `artifacts/narratives/key_table_10x2.snapshot.json`.  
* `compat.conjunction.ab` maps to `artifacts/compat/AB.json`.  
* `compat.conjunction.ba` maps to `artifacts/compat/BA.json`.

**Path-proofs and indexing.**

Each primary artifact path above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. Reused compat-family paths listed above MUST follow the same sibling path-proof, Human Index, and Machine Mirror parity discipline when this PR-03 family changes them. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the three PR-03 binding logs, the narrative key-table linkage snapshot, any changed reused compat-family payload or proof companion, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC030 PR-04 band-threshold evidence

**Purpose.** Govern the direct PR-04 band-threshold and tuning evidence family for the existing compat threshold and constants-pack-backed threshold surfaces. This family is slice evidence only. It does not create a new public route, new public surface, flag, serializer path, second threshold home, endpoint-catalog success route, or close-stage artifact family.

**Primary artifact paths.**

* `audit/qa/hde-epic030/pr-04/band_edges_binding.log`: Direct PR-04 log artifact for constants-pack band-edge binding. When refreshed, it records constants-pack source, compat threshold binding, band names, inclusive edge values, resolved THRESHOLDS\_V1 maxima, and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json`: Direct PR-04 canonical JSON artifact for compact band-threshold and tuning diffs. When refreshed, it records compact diff values for cool\_max, open\_max, warm\_max, band order, expected values, and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt`: Direct PR-04 text artifact for threshold and tuning identity-hash evidence. When refreshed, it records LF-terminated AB and BA compat body hashes, ab\_ba\_identity\_match, and PASS/FAIL status. PASS requires current AB and BA identity hashes to match.

**Artifact-key bindings.**

* `epic030.pr04.band_edges_binding` maps to `audit/qa/hde-epic030/pr-04/band_edges_binding.log`.  
* `epic030.pr04.band_thresholds_diff` maps to `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json`.  
* `epic030.pr04.band_thresholds_identity_hash` maps to `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt`.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. If the producing generator semantics change for this family, the primary artifacts MUST be regenerated from the final generator behavior before their path-proofs, Human Index rows, and Machine Mirror rows are refreshed. When this family changes, the three primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC030 PR-05 category-framework evidence

**Purpose.** Govern the direct PR-05 category-framework evidence family for the existing category-framework, per-channel mechanics, canonical JSON compare, and evidence-indexing surfaces. This family is slice evidence only. It does not create a new public route, new public surface, flag, serializer path, endpoint-catalog success route, close-pack path, QA-ledger path, Live QA runbook path, or PF-canon edit path.

**Primary artifact paths.**

* `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json`: Direct PR-05 canonical JSON artifact for category-framework per-channel mechanics evidence. When refreshed, it records canonical channel edges, compromise direction and gate, channel-scoped circuit metadata, subtask binding, and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-05/category_canonical_compare.log`: Direct PR-05 log artifact for category-framework canonical JSON compare evidence. When refreshed, it records canonical compare outcome and PASS/FAIL status.  
* `audit/qa/hde-epic030/pr-05/category_framework_binding.log`: Direct PR-05 log artifact for category-framework binding and aggregate status. When refreshed, it records per-channel mechanics binding, canonical\_compare\_status, index binding, mirror binding, and PASS/FAIL status. PASS requires canonical\_compare\_status to be PASS and required bindings to be present.

**Artifact-key bindings.**

* `epic030.pr05.per_channel_mechanics` maps to `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json`.  
* `epic030.pr05.category_canonical_compare` maps to `audit/qa/hde-epic030/pr-05/category_canonical_compare.log`.  
* `epic030.pr05.category_framework_binding` maps to `audit/qa/hde-epic030/pr-05/category_framework_binding.log`.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. If the producing generator semantics change for this family, the primary artifacts MUST be regenerated from the final generator behavior before their path-proofs, Human Index rows, and Machine Mirror rows are refreshed. When this family changes, the three primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC030 implementation-slice evidence posture

The HDE-EPIC030 PR-01 through PR-05 families above are governed implementation-slice evidence families. They are not the HDE-EPIC030 close-pack authoritative pair, not a close-stage substitute, and not a QA-ledger path by themselves. When an HDE-EPIC030 close-pack is produced, it MUST use the close-pack baseline artifacts and key\_outputs binding rules in this section. The PR-slice evidence families may be referenced from that close-pack only through the normal governed artifact binding posture.

##### HDE-EPIC031 PR-01 SAFE rails provider-gate evidence

**Purpose.** Govern the direct PR-01 SAFE rails provider-gate evidence family for pinned provider timeout, retry, backoff, typed 429, Retry-After parsing, closed SAFE rails refusal, local no-live-call posture, and no-live-vendor provider behavior. This family is implementation-slice evidence only. It does not create a live vendor-call claim, public Reader change, HDAPI v2 runtime conformance claim, PO-only open-rails v2 smoke, close-pack path, QA-ledger path, or PF-canon edit path.

**Primary artifact paths.**

* `artifacts/vendor/policies_pinned.md`: Direct PR-01 policy evidence artifact for pinned timeout, retry, backoff, and non-200 classification posture. When refreshed, it records that non-200 HTTP statuses outside 4xx and 5xx are typed as PROVIDER\_ERROR and are not retried.  
* `artifacts/vendor/retry_after_parse.log`: Direct PR-01 Retry-After parse evidence log. When refreshed, it records deterministic delta-seconds and HTTP-date parsing posture and invalid, unsupported, or overflow omission posture.  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json`: Direct PR-01 governed proof JSON for open-rails policy posture without live vendor execution. Canonical JSON when present. When refreshed, it records no live vendor call, local mocked or fixture-backed proof posture, non-4xx and non-5xx http\_status\_other behavior, and classified side-effect families.  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json`: Direct PR-01 governed proof JSON for retry and backoff posture. Canonical JSON when present. When refreshed, it records 429, 4xx, 5xx, network-error, and other non-200 classification behavior and retry posture.  
* `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json`: Direct PR-01 governed proof JSON for closed default and open exception rails posture. Canonical JSON when present. When refreshed, it records that provider access is allowed only for local mocked or fixture-backed proof.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. Mirror records for this PR-01 family MUST use the exact artifact\_key values emitted by the governed single-writer evidence updater for these paths. This entry does not mint unsourced artifact\_key spellings for PR-01 paths whose exact keys are not surfaced here. When this family changes, the changed primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC031 PR-02 SAFE rails observability and keys-only log evidence

**Purpose.** Govern the direct PR-02 SAFE rails observability and keys-only log posture evidence family for bounded vendor log keys, bounded label domains, success and failure class observability, keys-only sample evidence, redaction proof artifacts, secret-redaction scan output, and PR-specific rails-scope evidence. This family is implementation-slice evidence only. It does not create a live vendor-call claim, public Reader change, close-pack path, QA-ledger path, or PF-canon edit path.

**Primary artifact paths.**

* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json`: Direct PR-02 governed evidence JSON for bounded label and observability posture. Canonical JSON when present. When refreshed, it records observed failure classes, route observability, timeout-profile observability, and PASS/FAIL status.  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`: Direct PR-02 governed evidence JSON for keys-only log redaction posture. Canonical JSON when present. When refreshed, it records forbidden hits, key violations, payload-body absence, plaintext-secret absence, raw-secret-header absence, and PASS/FAIL status.  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`: Direct PR-02 governed redaction scan log. LF-terminated text when present. When refreshed, it records records scanned, forbidden-hit count, and PASS/FAIL status.  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`: Direct PR-02 governed keys-only JSONL sample for vendor SAFE rails log records. Canonical JSONL when present. When refreshed, it records bounded key-only sample records across success and failure classes without payload or secret leakage.  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`: Direct PR-02 governed rails-scope text artifact. LF-terminated text when present. When refreshed, it records local deterministic scope, live vendor-call prohibition, SAFE rails pins, and vendor route detection posture.

**Current surfaced artifact-key bindings.**

* `epic031.pr02.vendor_keys_only_sample` maps to `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`.  
* `epic031.pr02.vendor_rails_scope` maps to `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`.  
* `epic031.pr02.keys_only_log_redaction` maps to `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`.  
* `epic031.pr02.secret_redaction_scan` maps to `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`. audit/qa/hde-epic031/pr-02/bounded\_label\_observability.json is a governed path in this family; when indexed or mirrored, its Mirror record MUST use the exact artifact\_key emitted by the governed single-writer evidence updater for that path.

**PR-specific path-collision posture.**

Vendor-specific PR-02 sample and rails-scope evidence MUST stay under audit/qa/hde-epic031/pr-02/ unless a later PF12 change explicitly re-homes the family. This family MUST NOT overwrite or substitute for shared DB-bridge or generic rails artifacts such as artifacts/logs/keys\_only.sample.jsonl or artifacts/ops/rails\_open\_scope.txt. Those shared artifacts remain separate governed families when cataloged, indexed, mirrored, and path-proven under their own bindings. If a PR-specific vendor artifact and a shared artifact both change in the same evidence-refresh pass, the run evidence MUST keep their paths, artifact roles, and proof anchors distinct.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings surfaced above where supplied, and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the changed primary artifacts, their sibling path-proofs, the Human Index, the Human Index hash sentinel, the Machine Mirror, the Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC031 PR-03 SAFE rails evidence and indexing coherence

**Purpose.** Govern the direct PR-03 SAFE rails evidence and indexing coherence family for binding PR-01, PR-02, and PR-03 SAFE rails artifacts through the Human Evidence Index, Human Index hash sentinel, Machine Evidence Mirror, Machine Mirror checksum sidecar, co-located path proofs, side-effect classification, and closed-rails validation checks. This family is implementation-slice evidence only. It does not create a live vendor-call claim, public Reader change, HDAPI v2 runtime conformance claim, PO-only open-rails v2 smoke, close-pack path, QA-ledger path, Live QA runbook path, token-matrix claim, or PF-canon edit path.

**Primary artifact paths.**

* `audit/qa/hde-epic031/pr-03/evidence_family_map.json`: Direct PR-03 governed evidence-family map. Canonical JSON when present. When refreshed, it records the PR-03 proof families, bounded side-effect refreshes, affected Machine Mirror rows, proof-validity posture, and sha256 or size matching posture.  
* `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`: Direct PR-03 governed coherence artifact. Canonical JSON when present. PASS requires the PR-03 evidence family, Human Index binding, Machine Mirror binding, path-proof binding, hash checks, and side-effect validation to be current and valid.  
* `audit/qa/hde-epic031/pr-03/evidence_refresh.log`: Direct PR-03 governed refresh log. LF-terminated text when present. When refreshed, it records closed-rails posture, refresh commands, check commands, side-effect classifications, live-vendor-call posture, and secret-recording posture.

**Bounded side-effect classification.**

When the PR-03 evidence generator or updater refreshes governed proof companions outside the direct PR-03 family, the PR-03 run evidence MUST name each refreshed family and classify it as exactly one of: expected updater convergence, required dependency refresh, or unexpected drift. The bounded side-effect set for this PR-03 family MAY include writer proof companions, topology orientation refreshes, and HDE-EPIC030 PR-03, PR-04, or PR-05 proof-companion refreshes when those are caused by the same governed evidence refresh. Side-effect classification MUST include both proof-companion paths and the affected Machine Mirror artifact keys or discovered paths when mirror rows change. A PR-03 coherence artifact MUST NOT report PASS if any classified side-effect path is missing, any classified side-effect proof companion fails validation, or any classified Machine Mirror row fails to match artifact key, proof anchor, sha256, or size. Classified outside-family side effects do not re-home those artifacts. The referenced writer, topology, and HDE-EPIC030 artifacts remain governed by their existing Evidence Catalog families and proof anchors.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The Human Index hash sentinel, Machine Mirror checksum sidecar, and their required sibling path-proofs MUST be refreshed coherently when this family changes governed evidence bytes. The corresponding Mirror records MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. Mirror records for this PR-03 family MUST use the exact artifact\_key values emitted by the governed single-writer evidence updater for these paths. This entry does not mint unsourced artifact\_key spellings for PR-03 paths whose exact keys are not surfaced here. When this family changes, the three primary artifacts, their sibling path-proofs, classified side-effect proof companions, Human Index rows, Human Index hash sentinel, Machine Mirror rows, Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC031 implementation-slice evidence posture

The HDE-EPIC031 PR-01 through PR-03 families above are governed implementation-slice evidence families. They are not a close-pack authoritative pair, not a close-stage substitute, and not QA-ledger paths by themselves. PR-slice evidence MAY support a later close-pack only through the normal governed artifact binding posture. It MUST NOT be used by itself to claim close-pack production, Live QA completion, PF09 drain, token-matrix completion, or epic closure. If HDE-EPIC031 close-pack artifacts are produced, they MUST use the close-pack baseline artifacts and key\_outputs binding rules in this section. Expected close-pack paths named by the current evidence posture include audit/EPIC-031\_close\_report.md, audit/EPIC-031\_MANIFEST.json, and docs/acceptance\_map\_epic031.json; those paths remain unclaimed until the actual governed artifacts, path proofs, and required Index or Mirror bindings exist.

HDE-EPIC031 close-pack, Live QA, acceptance-map, token-matrix, and close-stage review artifacts remain separate governed surfaces from the PR-01 through PR-03 implementation-slice families.

##### Showcompat artifacts (EPIC024 D03)

* `artifacts/showcompat/epic024/showcompat_manifest.json`: deterministic showcompat manifest for EPIC024, produced by the D03 runner.  
* `artifacts/showcompat/epic024/showcompat_symbols.json`: deterministic showcompat symbols table for EPIC024, produced by the D03 runner.  
* `tools/evidence/run_showcompat_artifacts.py`: EPIC024 D03 showcompat runner, wrapper around scripts/hdctl.py showcompat.

##### Sampler evidence (EPIC024 D04)

* `artifacts/sampler/epic024/sampler_evidence.json`: EPIC024 D04 sampler evidence summary artifact, meta-evidence over sampler families.  
* `artifacts/sampler/epic024/manifest.json`: EPIC024 D04 sampler evidence manifest with pointers and metadata for sampler\_evidence.json.  
* `tools/evidence/run_sampler_evidence.py`: EPIC024 D04 sampler evidence runner that produces sampler\_evidence.json and manifest.json.

##### CLI guardrail artifacts (EPIC024 D08)

* `artifacts/cli/guards/serializer_grep_guard.log`: serializer grep guard output log for the CLI serialization guardrail.  
* `tools/cli/serializer_grep_guard.py`: serializer grep guard producer tool that generates serializer\_grep\_guard.log. CLI serializer-coupling proof artifacts (EPIC028 PR01)  
* `artifacts/cli/guards/emitter_symbol_proof.txt`: governed emitter allow-list proof artifact for the CLI serializer-coupling surface.  
* `artifacts/cli/reader_cli_parity.bytes`: governed Reader↔CLI parity bytes artifact for the CLI serializer-coupling surface.  
* `tools/cli/emitter_symbol_proof.py`: emitter allow-list proof producer tool that generates emitter\_symbol\_proof.txt. Whenever the governed proof artifacts above change, their sibling .path\_proof.txt transcripts and their Human Index/Machine Mirror bindings MUST be refreshed in the same change.

#### 8.6.3.4 Gates, runtime, DB, and ops evidence

##### Narratives coverage (router)

##### HDE-EPIC032 PR-01 narrative-router evidence

**Purpose.** Govern the direct PR-01 narrative-router evidence family for router matrix coverage, missing-key fail-closed behavior, two-run identity, AB↔BA coherence where applicable, CLI/HTTP parity where defined, canonical JSON proof, and Evidence Index / Machine Mirror / path-proof binding. This family is implementation-slice evidence only. It does not create a public Reader contract change, PR-02 registry work, PR-03 or PR-04 DB work, HDAPI v2 work, OPS work, close-pack path, QA-ledger path, or PF-canon edit path.

**Primary artifact paths.**

* `audit/gates/narratives/keys_10x4.table.json`: HDE-EPIC032 PR-01 router coverage snapshot for the 10-category by 4-band supported matrix. Canonical JSON when present. It records personal and shared narrative keys, including missing\_narrative\_key cases for supported (category, band, perspective) coverage.  
* `artifacts/narratives/router/parity_abba.log`: HDE-EPIC032 PR-01 AB↔BA and two-run identity log for router outputs. LF-terminated text when present. It is keys-only and no-prose evidence.  
* `artifacts/narratives/router/cli_http_parity.log`: HDE-EPIC032 PR-01 CLI/HTTP parity log for router responses where parity is defined. LF-terminated text when present.

**Token posture for this family.**

The key-table row for this family MUST NOT claim NARR\_REGISTRY\_CLOSURE\_OK unless that token name is admitted by HDE-Governance or a later live Build Notes addendum. The current key-table posture for epic032.pr01.router\_key\_table\_10x4 carries JSON\_CANONICAL\_CHECK\_OK only. The parity rows may retain the approved parity token posture for CLI\_READER\_PARITY\_OK, TWO\_RUN\_IDENTITY\_OK, and COMPOSITE\_ABBA\_IDENTITY\_OK where those tokens are applicable to the governed parity artifacts.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The Human Index hash sentinel, Machine Mirror checksum sidecar, and their required sibling path-proofs MUST be refreshed coherently when this family changes governed evidence bytes. The corresponding Mirror records MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the three primary artifacts, their sibling path-proofs, Human Index rows, Human Index hash sentinel, Machine Mirror rows, Machine Mirror checksum sidecar, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### HDE-EPIC032 PR-02 narrative registry diff, Doc-Delta identity, and indexing evidence

**Purpose.** Govern the direct PR-02 evidence family for narrative registry diff generation, Doc-Delta posture binding, pack identity from canonical manifest bytes, same-bytes two-run identity, keys-only/no-prose registry evidence, Human Evidence Index binding, Machine Evidence Mirror binding, hash sentinels, path-proofs, sanity-pipeline generator ordering, and topology orientation evidence remediation. This family is implementation-slice evidence only. It does not create a public Reader contract change, PR-03 or PR-04 DB work, HDAPI v2 work, OPS work, close-pack path, QA-ledger path, token-matrix claim, or PF-canon edit path.

**Primary artifact paths.**

* `audit/gates/narratives/registry.diff.json`: Direct PR-02 canonical registry diff artifact. Canonical JSON when present. When refreshed, it records manifest identity, keys-only registry counts, no-prior-baseline diff state, and HDE-FERM003.2 scope.  
* `audit/gates/narratives/pack_identity.txt`: Direct PR-02 pack identity evidence artifact. LF-terminated text when present. When refreshed, it records pack\_sha, manifest canonical SHA, canonical manifest size, two-run identity values, two-run match, and SHA/size values for narrative manifest files.  
* `audit/docdeltas/hde-epic032_doc_deltas.md`: Direct PR-02 Doc-Delta posture artifact. Non-empty UTF-8 markdown when present. When refreshed, it records that HDE-FERM003.2 PR-02 adds repo evidence and tooling for narrative registry diffing, Doc-Delta binding, pack identity, and evidence indexing.

**Artifact-key bindings.**

* `epic032.pr02.registry_diff` maps to `audit/gates/narratives/registry.diff.json`.  
* `epic032.pr02.pack_identity` maps to `audit/gates/narratives/pack_identity.txt`.  
* `epic032.pr02.doc_deltas` maps to `audit/docdeltas/hde-epic032_doc_deltas.md`.

**Token posture for this family.**

epic032.pr02.registry\_diff may carry JSON\_CANONICAL\_CHECK\_OK. epic032.pr02.pack\_identity may carry TWO\_RUN\_IDENTITY\_OK. epic032.pr02.doc\_deltas may carry DOC\_DELTA\_PRESENT\_OK. This PR-02 family MUST NOT introduce NARR\_REGISTRY\_CLOSURE\_OK or any new acceptance token unless the token is registered by HDE-Governance or minted by a live Build Notes addendum before use.

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The Human Index hash sentinel, Machine Mirror checksum sidecar, and their required sibling path-proofs MUST be refreshed coherently when this family changes governed evidence bytes. The corresponding Mirror records MUST use the artifact-key bindings above and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the three primary artifacts, their sibling path-proofs, Human Index rows, Human Index hash sentinel, Machine Mirror rows, Machine Mirror checksum sidecar, topology orientation evidence and path-proof companions if refreshed by the same run, and the required index and mirror sibling path-proofs MUST be refreshed coherently in the same change.

##### Determinism env pins (gate)

* `audit/gates/determinism/env_pins.log`: determinism env pins gate output; structured log; current-state schema determinism\_env\_pins.v1.  
* `tools/evidence/run_env_pins_gate.py`: determinism env pins gate runner, wrapping ci/checks/check\_env\_pins.sh with proper environment setup.

##### Sanity pipeline (gate)

* `audit/gates/sanity_pipeline/sanity_pipeline.log`: sanity pipeline gate stable log; single canonical evidence surface.  
* `tools/evidence/run_sanity_pipeline.py`: sanity pipeline runner that produces sanity\_pipeline.log.  
* `tools/evidence/run_sanity_pipeline_gate.py`: sanity pipeline gate wrapper; gate-style invocation entrypoint.

##### Rails proofs (ops)

* `artifacts/proofs/ops_refusal_proof.txt`: single-file refusal proof with headers, then a blank line, then LF-terminated JSON. **Record type.** ops\_refusal\_proof. Policy and tokens are owned by HDE-Governance.  
* `ci/jobs/logs_keys_only_redaction.yml`  
* `ci/jobs/rails_open_conformance.yml`

##### DB posture and runtime

* `artifacts/db/ddl_fingerprint.json`  
* `artifacts/db/grants.txt`  
* `artifacts/db/check_schema.txt`  
* `artifacts/db/check_constraints.txt`  
* `artifacts/db/partition_plan.txt`  
* `artifacts/db/db_rw_smoke.log` (optional)

  ##### **Runtime and environment**

* `artifacts/runtime/env_matrix.snapshot.json`: singleton snapshot with `schema_version: 3`, default rails and determinism pins, and presence booleans only for DB, bridge, and guard configuration. Secret values MUST NOT appear. `tools/evidence/generate_env_matrix_snapshot.py` is the sole primary producer. Its check mode is read-only and MUST reject missing, noncanonical, non-v3, or drifted bytes.  
* `artifacts/runtime/env_connectivity.snapshot.json`: retained historical bridge and OPS evidence. Its governed bytes, path proof, Human Evidence Index binding, and Machine Evidence Mirror binding remain intact, but it MUST NOT prove current bridge availability, runtime support, fallback, provider parity, consistency, current OPS PASS, or token satisfaction.

##### **HDE-EPIC038 direct-only database selection and historical bridge evidence**

**DDL identity projection.** `engine/db/ddl_identity_projection.py` is the sole shared implementation of schema `hde.ddl_identity_projection.v1`. Its projection-only result MUST NOT be interpreted as full DDL semantic parity; the only passing comparison label is `projection_match`, with `full_ddl_semantic_parity_claimed: false`.

**Current direct-selection family.**

* `epic038.pr06r.direct_db_selection` → `artifacts/runtime/direct_db_selection.snapshot.json`; schema `hde_epic038.direct_db_selection.v1`; record type `epic038_pr06r_direct_db_selection`; sole primary producer `tools/evidence/generate_hde_epic038_direct_db_selection.py`.  
* `epic038.pr06r.direct_db_selection_schema` → `schemas/hde_epic038_direct_db_selection.v1.json`; record type `epic038_pr06r_schema`.

The primary has exactly `schema`, `retired_keys`, `cases`, `predicates`, `result`, and `failure`. Its four ordered cases are `healthy_direct`, `missing_database_url`, `unavailable_database_url`, and `retired_keys_present`. Its predicates are exactly `direct_only_provider`, `missing_direct_fails_closed`, `unavailable_direct_fails_closed`, `retired_keys_fail_before_provider_attempt`, `alternate_transport_attempts_zero`, and `secret_values_absent`.

**Historical bridge evidence.** Retained bridge-era primaries under `artifacts/db_bridge/**`, `artifacts/db/provider_parity/**`, bridge-era runtime-connectivity paths, bridge Presenter comparisons and schemas, and `audit/ops/hde-epic038/ops-01/**` use record type `historical_bridge_evidence` where bound by the current ledgers. Their bytes, checksums, path proofs, and Index/Mirror identities remain historical records; they MUST NOT prove current service availability, runtime support, direct-versus-bridge parity, bridge consistency, bridge fallback, current OPS PASS, release admission, or token satisfaction.

`tools/evidence/update_evidence_index.py` is the sole owner of direct-selection companions and historical row classification. Feature producers MUST NOT write Index, Mirror, path-proof, checksum, or orientation companions.

##### **HDE-EPIC038 PR-01 production identity and provenance evidence**

The accepted capture family consists of these exact key/path bindings:

* `epic038.pr01.service_identity` → `artifacts/identity/service_identity.json`. The artifact is canonical JSON with exactly `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, and `release_id`, and no extra fields.  
* `epic038.pr01.emitter_sha256` → `artifacts/identity/emitter_sha256.txt`.  
* `epic038.pr01.invocation_sha256` → `artifacts/identity/invocation_sha256.txt`.  
* `epic038.pr01.identity_release_id` → `artifacts/identity/release_id.json`.  
* `epic038.pr01.identity_release_id_recompute` → `artifacts/identity/release_id_recompute.log`.  
* `epic038.pr01.two_run_identity` → `artifacts/identity/two_run_identity.log`.

`tools/evidence/generate_identity_provenance.py` owns deterministic materialization and read-only checking of this six-artifact family. The service-identity artifact MUST satisfy the six-field contract, and the two-run artifact MUST be based on independently collected runs rather than one captured value reused twice.

`artifacts/identity/release_id.json` and `artifacts/identity/release_id_recompute.log` are frozen historical capture evidence. They MUST NOT be refreshed or relabeled as current release equality or current attestation. Current runtime release identity is derived directly from the canonical packaged bytes of `catalog/manifest.json`; current release provenance belongs to external attestation.

The bounded-development identity proof surfaces are:

* `conjunction.writer.write_readback` → `artifacts/writer/conjunction_write_readback.log`; and  
* `conjunction.writer.summary` → `artifacts/writer/conjunction_writer_summary.json`.

Their `writer_dev_identity` and `reader_dev_identity` predicates are development evidence only. They do not create a second production identity authority.

Every promoted primary in this family MUST retain exactly one Human Evidence Index binding, one matching Machine Evidence Mirror binding, a sibling path proof, and coherent checksum companions under the updater-owned evidence workflow.

##### **HDE-EPIC038 OPS-03 direct read-only posture packet**

The tracked success root is exactly `audit/ops/hde-epic038/ops-03/`. Its ten current primary bindings are:

* `epic038.ops03.commands` → `commands.txt`; record type `epic038_ops03_text`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.stdout` → `stdout.log`; record type `epic038_ops03_log`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.stderr` → `stderr.log`; record type `epic038_ops03_log`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.exit_code` → `exit_code.txt`; record type `epic038_ops03_text`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.env_presence` → `env_presence.json`; record type `epic038_ops03_env_presence`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.db_posture_summary` → `db_posture_summary.json`; record type `epic038_ops03_db_posture`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.nonclaims` → `nonclaims.json`; record type `epic038_ops03_nonclaims`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.result_summary` → `result_summary.json`; record type `epic038_ops03_result`; producer `scripts/ops/hde_epic038_ops03.py`.  
* `epic038.ops03.validation_receipt` → `validation_receipt.json`; record type `epic038_ops03_validation`; producer `tools/evidence/hde_epic038_ops03.py --emit-receipt`.  
* `epic038.ops03.checksums` → `checksums.sha256`; record type `epic038_ops03_checksum`; producer `scripts/ops/hde_epic038_ops03.py`.

The seven tracked schema bindings, each with record type `epic038_ops03_schema`, are:

* `epic038.ops03.schema.hde_epic038_ops03_authorization.v1` → `schemas/hde_epic038_ops03_authorization.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_env_presence.v1` → `schemas/hde_epic038_ops03_env_presence.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_db_posture_summary.v1` → `schemas/hde_epic038_ops03_db_posture_summary.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_nonclaims.v1` → `schemas/hde_epic038_ops03_nonclaims.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_result_summary.v1` → `schemas/hde_epic038_ops03_result_summary.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_validation_receipt.v1` → `schemas/hde_epic038_ops03_validation_receipt.v1.json`  
* `epic038.ops03.schema.hde_epic038_ops03_failure_receipt.v1` → `schemas/hde_epic038_ops03_failure_receipt.v1.json`

`tools/evidence/update_evidence_index.py` alone creates the seventeen sibling path proofs and updates the Human Evidence Index, Machine Evidence Mirror, hash sentinels, checksums, and orientation companions. Exact-byte admission does not make PR-06R-B a primary producer. OPS-03 does not mint an acceptance token or establish QA PASS, PF09 status movement, deployment, migration, production-write authorization, or epic closeout.

##### Ops and refusal (closed-rails)

* `artifacts/proofs/ops_refusal_proof.txt`: same governed artifact as above, viewed here specifically as the closed-rails refusal proof. It carries headers, then a blank line, then LF-terminated JSON. Policy and tokens are routed by title to Governance.

##### Internal-ops surface — `/internal/version` identity artifacts (`INTVER_*`)

These entries register the /internal/version identity artifacts required by Governance as governed Evidence Catalog families. /internal/version is an ops-only identity surface, non-A7. PF12 records its evidence artifacts, artifact\_keys, and Index/Mirror discipline, while transport bytes and token semantics remain in HDE-Governance and HDE-CLI-API-Vendor-Ref by title. Auth posture (not canonized; discovery evidence required) PF-Canon defines the /internal/version transport and content contract and its governed identity artifacts, but does not canonize the auth posture, meaning public vs operator-network gated vs auth-header required, or the expected failure mode when access is missing or invalid. Until canonized, remediation guides and operational tooling MUST NOT state auth requirements for /internal/version as canon. Any statement about auth posture MUST be explicitly labeled as Observed Evidence, non-PF. Until an auth-gated posture is both implemented and canonized, runbooks MUST NOT require an auth header for /internal/version. If an auth header is used in a probe, it MUST be treated as optional and recorded as presence-only, never the raw value, in any associated request-chain or run logs. Canonization of auth posture requires OPS discovery evidence that captures status line and headers for the canonical deployment context or contexts under two conditions: with no auth header with the expected auth header present, with value redacted or presence-only noted This discovery evidence MUST be secret-free and stored in-repo under a lowercase audit path, titles-only: HDE-Build Notes OPS posture. PF12 governs only that any such evidence, when promoted, must live under governed roots and follow the Evidence Index and Machine Mirror discipline. Checksum sidecars in this family, INTVER\_SHA256, are optional unless explicitly required by an acceptance roster. If present, each checksum file MUST be the sha256 hex plus LF of the corresponding artifact bytes. /internal/version invariant checklist (minimum set; MUST be explicit) Any remediation guide, QA step, or probe tool that produces governed /internal/version evidence artifacts, INTVER\_\*, MUST explicitly enumerate and verify the canon-critical invariants below. It is not acceptable to imply these checks by referencing PF sections only.

###### *Internal-version transport*

GET MUST return 200\. HEAD MUST return 200 and satisfy parity expectations. Conditional requests using If-None-Match and If-Modified-Since MUST NOT yield 304\. They MUST return 200\.

###### *Internal-version headers*

Cache-Control: no-store MUST be present. Content-Type: application/json; charset=utf-8 MUST be present. ETag MUST be absent. Absence is literal. The captured header set MUST NOT contain an ETag: header line at all. Do not emit placeholder lines such as ETag: . Last-Modified MUST be absent.

###### *Internal-version body identity payload*

Body MUST be fixed-schema JSON with exactly these keys and no extras: engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id. Body bytes MUST satisfy the canon identity-bytes posture where applicable: canonical JSON per §4, including LF termination.

###### *Internal-version coupling and fail-closed behavior*

Verification MUST be performed against the same captured bytes that are written as governed artifacts for that run, including headers snapshots, body snapshot, and any two-run identity digest or log. If coupling cannot be established, for example mixed target or redirect drift, or verification cannot be completed, for example tooling failure, the run MUST fail closed for evidence purposes and MUST NOT be recorded as satisfying the corresponding invariants. This checklist does not canonize auth posture. Auth posture remains not canonized until OPS discovery evidence is captured, as described above. INTVER artifact families

* `INTVER_BODY_GET_V1` — `GET body snapshot`. Artifact path, example: artifacts/ops/internal\_version/body\_get.json. Canonical JSON body for a successful GET /internal/version with six provenance fields and no extras; LF-terminated.  
* Schema path: a JSON Schema under docs/schemas/\*\* that captures the frozen six-field identity envelope for /internal/version. Mirror: artifact\_key:"INTVER\_BODY\_GET\_V1", role:"snapshot". Human Index: same artifact\_key and the body\_get.json path as discovered\_physical\_path.  
* `INTVER_BODY_GET_SHA256_V1` — `GET body hash record`. Artifact path, example: artifacts/ops/internal\_version/body\_get.sha256. Small JSON or text artifact recording the sha256 and size of body\_get.json as governed in Governance. Mirror: artifact\_key:"INTVER\_BODY\_GET\_SHA256\_V1", role:"snapshot". Human Index: same artifact\_key and the hash file path.  
* `INTVER_HEADERS_GET_V1` — `GET headers snapshot`. Artifact path, example: artifacts/ops/internal\_version/headers\_get.txt. Raw GET /internal/version response headers proving Cache-Control: no-store, absence of ETag and Last-Modified, and correct Content-Type. Mirror: artifact\_key:"INTVER\_HEADERS\_GET\_V1", role:"snapshot". Human Index: same artifact\_key and the headers file path.  
* `INTVER_HEADERS_COND_IF_NONE_MATCH_V1` — `conditional headers snapshot, If-None-Match`. Artifact path, canonical: artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt. Raw response headers captured from a conditional request to /internal/version with If-None-Match present. **Purpose.** provide governed evidence that /internal/version ignores conditional delivery for its ops-only identity contract, names-only and no body bytes in this artifact. Mirror: artifact\_key:"INTVER\_HEADERS\_COND\_IF\_NONE\_MATCH\_V1", role:"snapshot". Human Index: same artifact\_key and the conditional headers file path.  
* `INTVER_HEADERS_COND_IF_MODIFIED_SINCE_V1` — `conditional headers snapshot, If-Modified-Since`. Artifact path, canonical: artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt. Raw response headers captured from a conditional request to /internal/version with If-Modified-Since present. **Purpose.** provide governed evidence that /internal/version ignores conditional delivery for its ops-only identity contract, names-only and no body bytes in this artifact. Mirror: artifact\_key:"INTVER\_HEADERS\_COND\_IF\_MODIFIED\_SINCE\_V1", role:"snapshot". Human Index: same artifact\_key and the conditional headers file path. Conditional artifact-key posture (normative). Conditional header capture artifacts for /internal/version MUST use dedicated INTVER\_HEADERS\_COND\_\* artifact keys as listed above. They MUST NOT be indexed under INTVER\_HEADERS\_GET\_V1 or INTVER\_HEADERS\_HEAD\_V1. Evidence Index and Machine Mirror entries for these files MUST be consistent with this dedicated-key posture.  
* `INTVER_HEADERS_HEAD_V1` — `HEAD headers snapshot`. Artifact path, example: artifacts/ops/internal\_version/headers\_head.txt. Raw HEAD /internal/version response headers proving 200, Content-Length equal to the length of the identity GET body, Content-Type equal to GET, and no body. Mirror: artifact\_key:"INTVER\_HEADERS\_HEAD\_V1", role:"snapshot". Human Index: same artifact\_key and the headers file path.  
* `INTVER_TWO_RUN_IDENTITY_V1` — `coupling and two-run identity log, single governed proof`. Artifact path, example: artifacts/ops/internal\_version/two\_run\_identity.log. Single governed log proving /internal/version coupling and two-run identity under closed rails. Minimum required content, names-only and no secrets: two-run identity result: explicit pass or fail that two consecutive GET /internal/version captures are byte-identical, including recorded digests or byte identifiers for both runs coupling verification result: explicit pass or fail that the six /internal/version fields match their governing identity sources, recording the governing artifact paths by name and the check outcome, including release\_id coupling rails posture reference: names-only reference to closed-rails posture and the determinism pins evidence surface, audit/gates/determinism/env\_pins.log Mirror: artifact\_key:"INTVER\_TWO\_RUN\_IDENTITY\_V1", role:"log". Human Index: same artifact\_key and the log path.  
* `INTVER_REQUEST_CHAIN_MANIFEST_V1` — `request-chain manifest, deterministic`. Artifact path, canonical: artifacts/ops/internal\_version/request\_chain\_manifest.json. Deterministic request-chain manifest associated with /internal/version evidence capture runs. Requirements (normative): MUST be secret-free. If an auth header is used by a probe or harness, the manifest MUST NOT record the raw value; presence-only or redacted placeholder only. MUST have a co-located sibling path-proof transcript at artifacts/ops/internal\_version/request\_chain\_manifest.json.path\_proof.txt. Mirror and Human Index linkage, names-only: Mirror: artifact\_key:"INTVER\_REQUEST\_CHAIN\_MANIFEST\_V1", role:"snapshot" Human Index: same artifact\_key and the manifest path as discovered\_physical\_path proof\_anchor MUST point to artifacts/ops/internal\_version/request\_chain\_manifest.json`.path_proof.txt` Indexing and Mirror discipline For each INTVER\_\* family above, the Human Evidence Index, docs/evidence/INDEX.json, MUST contain at least one entry with the appropriate artifact\_key and a discovered\_physical\_path pointing to the governed artifact under artifacts/ops/internal\_version/\*\*. docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any /internal/version artifact. The Machine Evidence Mirror, artifacts/evidence\_index.jsonl, MUST contain canonical JSONL records for each governed /internal/version artifact and schema, using the artifact\_key names exactly as above and the minimum Mirror record schema in §8.3: artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor.

##### Acceptance hints (names-only)

These INTVER\_\* families are the governed surfaces for the /internal/version identity token titles defined in PF04 and the relevant epic acceptance roster, for example INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK, INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_NOTOK, INTERNAL\_VERSION\_200\_CTYPE\_HTML\_NOTOK, and INTERNAL\_VERSION\_404\_NOTOK.

#### 8.6.3.5 Presenter evidence

These entries register the presenter evidence families introduced by HDE-EPIC020 D2 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section: UTF-8, sorted keys, compact separators, exactly one trailing LF for JSON artifacts, governed paths only, and path-proofs plus Index/Mirror parity per §8.3 to §8.6. PF12 binds these families to D2 tokens by artifact\_key and path only. Token semantics remain in HDE-Governance and Glow QA Guide by title. Shared family rule. For each presenter family below, the Human Evidence Index MUST contain at least one entry per artifact\_key with discovered\_physical\_path pointing to the governed artifact path under artifacts/presenter/\*\*. docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any presenter artifact. The Machine Evidence Mirror MUST contain canonical JSONL records for each governed presenter artifact and schema using the exact artifact\_key names below and the minimum Mirror record schema in §8.3.

**HDE-EPIC038 PR-04 Presenter evidence.**

Shared Presenter history:

* Primary: `presenter.bodygraph.json_canon_compare` → `artifacts/presenter/json_canon_compare.log`.  
* Immutable source fixture: `tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json`, schema `presenter.history_source.v1`. The fixture is generator input and has no Machine Evidence Mirror key.  
* Sole primary producer: `tools/evidence/generate_presenter_history.py`.  
* Ordered record IDs: `epic011_s10_rails_closed_match`, `epic011_s10_diff`, `epic011_live_match_a`, and `epic011_live_match_b`.  
* Canonical output: exactly four LF-terminated JSONL rows, 1559 bytes, SHA-256 `64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c`.

Materialization MUST validate the closed fixture shape, exact record count and order, unique IDs, row hashes, output length, and output hash before replacing the destination atomically. Check mode is read-only and MUST reject missing, extra, changed, noncanonical, provisional, replay-constant, wall-clock-derived, or wrong-order rows.

Historical DB/bridge Presenter receipt:

* Primary: `epic038.pr04.presenter_db_bridge_compare` → `artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json`.  
* Schema ID: `presenter.db_bridge_compare.v1`.  
* Schema: `epic038.pr04.presenter_db_bridge_compare_schema` → `schemas/presenter_db_bridge_compare.v1.json`.  
* Historical producer provenance: `tools/evidence/generate_db_bridge_parity.py`.

The receipt and its schema are retained historical bridge evidence. Their bytes, hashes, path proofs, Human Evidence Index bindings, and Machine Evidence Mirror bindings MUST be preserved, but they MUST NOT be regenerated through a retired bridge or used to prove current bridge availability, fallback, provider parity, consistency, current OPS PASS, or token satisfaction. The receipt is not BodyGraph source-invariance truth and is not a BodyGraph release-binding input.

Each Presenter primary and governed schema MUST have exactly one current key/path binding. PR-specific duplicate aliases are prohibited. Sibling path proofs, the Human Evidence Index, its hash sentinel, the Machine Evidence Mirror, its checksum, orientation/index companions, and their proofs remain solely updater-owned.

The HDE-EPIC020 Presenter families below remain governed as written.

* `PRESENTER_IDENTITY_SUMMARY_V1` — `presenter identity summary`. Canonical JSON summary for showcompat identity. Example path: a JSON file under artifacts/presenter/, for example artifacts/presenter/showcompat\_identity\_summary.json. Schema: an engine/presenter evidence schema under docs/schemas/\*\*. Mirror role: snapshot.  
* `PRESENTER_PREIMAGE_RECOMPUTE_V1` — `presenter preimage recompute log`. Preimage recompute evidence for presenter and Reader envelopes. Example path: a log file under artifacts/presenter/, for example artifacts/presenter/preimage\_recompute.log. Mirror role: log.  
* `PRESENTER_READER_CLI_PARITY_V1` — `presenter Reader and CLI parity bytes`. Reader vs CLI presenter parity sample. Example path: a bytes or JSON artifact under artifacts/presenter/, for example artifacts/presenter/reader\_cli\_parity.bytes. Mirror role: snapshot or log, depending on implementation. PRESENTER\_SHOWCOMPAT\_AB\_BYTES\_V1 and PRESENTER\_SHOWCOMPAT\_BA\_BYTES\_V1 — presenter AB and BA identity bytes Showcompat presenter bytes for AB and BA. Example paths: artifacts/presenter/showcompat\_ab.bytes and artifacts/presenter/showcompat\_ba.bytes. Mirror role: snapshot. Acceptance hints (names-only). These families support the EPIC020 D2 presenter tokens, for example CLI\_SHOWCOMPAT\_CANON\_OK, TWO\_RUN\_IDENTITY\_OK, COMPOSITE\_ABBA\_IDENTITY\_OK, and PREIMAGE\_RECOMPUTE\_OK, by providing governed artifacts and Index/Mirror records. PF12 binds tokens to artifacts by name and path only and does not redefine token semantics.

#### 8.6.3.6 Error evidence

These entries register the error evidence families introduced by HDE-EPIC020 D1 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section: UTF-8, sorted keys, compact separators, exactly one trailing LF where JSON is used, governed paths only, and path-proofs plus Index/Mirror parity per §8.3 to §8.6.

* `ERRORS_READER_CLI_PARITY_V1` — `Reader↔CLI parity artifacts`. Paths: parity/errors\_reader\_cli.*.http.json parity/errors\_reader\_cli.*.cli.txt Closed-rails error parity artifacts for EPIC020 D1. Each scenario captures a typed error envelope from the HTTP surface and a matching CLI stderr or text log, used together to prove Reader↔CLI parity for error codes and messages under closed rails. Mirror: artifact\_key:"ERRORS\_READER\_CLI\_PARITY\_V1", role:"log". Human Index: same artifact\_key and the concrete parity file paths as discovered\_physical\_path values. Token semantics, for example CLI\_READER\_PARITY\_OK and related parity tokens, remain owned by HDE-Governance and Glow QA Guide. PF12 binds them to this family by name and path only.  
* `ERROR_SCHEMA_CHECK_V1` — `error-envelope schema-check logs`. Path: errors/schema\_check/error\_envelope\_\*.log Error-envelope schema-check logs for selected scenarios, for example invalid\_json, invalid\_viewer\_prefs, db\_unavailable, or vendor\_attempt\_closed\_rails. Each log records at minimum the scenario name, HTTP status, canonical error code, and schema validation result under the governed error-envelope schema. Mirror: artifact\_key:"ERROR\_SCHEMA\_CHECK\_V1", role:"log". Human Index: same artifact\_key and the concrete log paths under errors/schema\_check/. These artifacts support error-envelope schema tokens such as ERROR\_JSON\_CANON\_OK and JSON\_CANONICAL\_CHECK\_OK, names-only; semantics live in Governance.  
* `ERROR_TOKEN_MAP_V1` — `token-map snapshot`. Path: errors/token\_map/token\_map.json Canonical JSON snapshot of the typed error token map, listing each error code with its aliases and message text for the current error-envelope set. Mirror: artifact\_key:"ERROR\_TOKEN\_MAP\_V1", role:"snapshot". Human Index: same artifact\_key and discovered\_physical\_path:"errors/token\_map/token\_map.json". This artifact underpins ERROR\_TOKEN\_MAP\_OK, names-only, ensuring the runtime error token map matches the governed snapshot used in tests and CLI/HTTP error behavior. Indexing and path-proofs. All three error evidence families MUST participate in the standard Evidence Index and Machine Mirror discipline. Human Index, docs/evidence/INDEX.json: For every concrete parity artifact, parity/errors\_reader\_cli..http.json or parity/errors\_reader\_cli..cli.txt, there MUST be an entry whose artifact\_key is ERRORS\_READER\_CLI\_PARITY\_V1 and whose discovered\_physical\_path equals that file’s repo-relative path. For every schema-check log under errors/schema\_check/error\_envelope\_\*.log, there MUST be an entry whose artifact\_key is ERROR\_SCHEMA\_CHECK\_V1 and whose discovered\_physical\_path equals that log’s path. For the token-map snapshot, there MUST be an entry with artifact\_key:"ERROR\_TOKEN\_MAP\_V1" and discovered\_physical\_path:"errors/token\_map/token\_map.json". docs/evidence/INDEX.sha256 MUST be updated in the same PR as any change to these artifacts or their indexing. Machine Mirror, artifacts/evidence\_index.jsonl: MUST contain canonical JSONL records for each governed error artifact above. artifact\_key MUST be ERRORS\_READER\_CLI\_PARITY\_V1, ERROR\_SCHEMA\_CHECK\_V1, or ERROR\_TOKEN\_MAP\_V1 as appropriate. role MUST be log for parity and schema-check artifacts and snapshot for the token map. discovered\_physical\_path MUST equal the path recorded in the Human Index. sha256 and size\_bytes MUST match the artifact’s canonical bytes. produced\_at\_utc MUST reflect the evidence refresh time. proof\_anchor MUST point to the matching .path\_proof.txt transcript alongside each artifact. Mirror records MUST obey all §8.3 rules: field set, ASCII field order, sort-before-write, single mirror file, and unknown-key rejection. Path-proofs: Each concrete parity artifact and schema-check log MUST have a sibling path-proof transcript, .path\_proof.txt, stored alongside the artifact, whose path, sha256, size\_bytes, mtime\_utc, and produced\_at\_utc match the artifact’s canonical bytes and its Mirror record. errors/token\_map/token\_map.json MUST have a sibling errors/token\_map/token\_map.json.path\_proof.txt transcript with the same constraints. Acceptance hints for these families are names-only and include error/parity and schema tokens such as CLI\_READER\_PARITY\_OK, including its legacy alias CLI\_READER\_EMITTER\_PARITY\_OK, ERROR\_JSON\_CANON\_OK, JSON\_CANONICAL\_CHECK\_OK, and ERROR\_TOKEN\_MAP\_OK. PF12 does not change token semantics; it binds these tokens to the governed error evidence families by artifact\_key and path so Governance, QA, and PF09 can route by title only.

#### 8.6.3.7 Sampler evidence

These entries register the sampler and ranker evidence families introduced by HDE-EPIC019 D4 as governed members of the Evidence Catalog. They follow the same canonical JSON and Evidence Index/Mirror discipline as other families in this section: UTF-8, sorted keys, compact, exactly one trailing LF, governed paths only, and path-proofs plus Index/Mirror parity per §8.3 to §8.6.

* `sampler_pool_snapshots` — `sampler pool and eligibility snapshots`. **Purpose.** canonical JSON snapshots of sampler candidate pools, including viewer ID, candidate IDs, bands, compat scores, weights, and eligibility flags, used to prove sampler pool composition and eligibility filters. Artifact path, example: artifacts/sampler/pool\_snapshots/baseline.json, and siblings under artifacts/sampler/pool\_snapshots/.  
* Schema path: docs/schemas/sampler/pool\_snapshots.schema.json. PII posture: artifacts omit PII beyond IDs, bands, compat labels, and QA-necessary metadata. No app-level user identifiers or raw personal data are permitted.  
* `sampler_two_run_logs` — `sampler two-run identity logs`. **Purpose.** logs demonstrating two-run identity for sampler output, same inputs implying identical ordering, used to prove sampler determinism under closed rails.  
* Artifact path: artifacts/sampler/two\_run/identity.json.  
* Schema path: docs/schemas/sampler/two\_run\_logs.schema.json. **Notes.** canonical JSON; array fields that represent sets follow arrays-as-sets rules in §4.2.  
* `sampler_abba_logs` — `AB, BA, and ABBA parity logs`. **Purpose.** AB, BA, and ABBA sampler runs for parity checks, used to show sampler ranking is invariant under label order when inputs are normalized.  
* Artifact path: artifacts/sampler/abba/ab\_ba\_parity.json.  
* Schema path: docs/schemas/sampler/abba\_logs.schema.json.  
* `sampler_diversity_artifacts` — `diversity and window evidence`. **Purpose.** evidence for diversity, window, and recent-selection constraints in the sampler, used to show the sampler respects configured spread and recency rules.  
* Artifact path: artifacts/sampler/diversity/diversity\_requirements.json.  
* Schema path: docs/schemas/sampler/diversity\_artifacts.schema.json.  
* `sampler_seed_replay_logs` — `seed replay logs for CLI and HTTP harnesses`. **Purpose.** seed replay logs from dev sampler CLI and HTTP harnesses, capturing repeated seeded runs and proving seed-echo semantics and candidate-set stability across surfaces.  
* Artifact path: artifacts/sampler/seed\_replay/cli\_http\_seed\_replay.json.  
* Schema path: docs/schemas/sampler/seed\_replay\_logs.schema.json. Canonical JSON policy and governed locations, sampler family. All sampler artifacts listed above MUST use the canonical JSON emitter governed by §4: UTF-8, ASCII-sorted keys, compact separators, exactly one trailing LF; arrays treated as sets are deduped and ASCII-sorted by identity. All sampler artifacts and schemas MUST live under governed locations:  
* `artifacts/sampler/**`  
* `docs/schemas/sampler/**` Sampler evidence summary and manifest (EPIC024 D04).  
* `artifacts/sampler/epic024/sampler_evidence.json`: summary artifact. Current-state output reports counts for existing\_artifacts, missing\_artifacts, and total\_artifacts.  
* `artifacts/sampler/epic024/manifest.json`: manifest artifact. Current-state output includes: artifacts: object with concrete paths for manifest and sampler\_evidence epic: epic identifier string generated\_at\_utc: UTC timestamp string, example 2026-01-21T20:55:39Z generator: generator script path, example tools/evidence/run\_sampler\_evidence.py referenced\_artifacts: list of referenced sampler evidence categories Generator: tools/evidence/run\_sampler\_evidence.py. Transient generator paths, for example codex/out/\*\* and temp directories, MUST NOT be indexed or mirrored.

**Evidence Index, Machine Mirror, and path-proofs.**

For each sampler family, the Human Evidence Index MUST contain an entry with the appropriate artifact\_key, for example sampler\_pool\_snapshots, and discovered\_physical\_path pointing to the governed artifact path. docs/evidence/INDEX.sha256 MUST be updated in the same PR. The Machine Evidence Mirror MUST contain a canonical JSONL record for each governed sampler artifact and schema using artifact\_key names exactly as above and the minimum Mirror record schema in §8.3. Each sampler artifact and schema MUST have a sibling path-proof transcript, for example artifacts/sampler/pool\_snapshots/baseline.json.path\_proof.txt and docs/schemas/sampler/pool\_snapshots.schema.json.path\_proof.txt, that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via proof\_anchor. Acceptance hints (names-only; sampler). Sampler evidence families participate in the existing mirror and index tokens referenced in §0.2 and §8.3, for example EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, and JSON\_CANONICAL\_CHECK\_OK. PF12 binds these tokens to sampler artifacts by name and path only. Token semantics remain owned by Governance and Glow QA Guide.

#### 8.6.3.8 Engine Core evidence

These entries register the Engine Core evidence families introduced by HDE-EPIC019 PR7 as governed members of the Evidence Catalog. They mirror the sampler evidence pattern: canonical JSON artifacts under artifacts/core/, schemas under docs/schemas/core/, and full Index/Mirror plus path-proof discipline under §8.3 to §8.6.

##### engine\_core\_purity\_report — Engine Core purity report

**Purpose.** canonical JSON report summarizing Engine Core purity checks over compute\_core scenarios, for example invariants that must hold for all core calls under closed rails. Each report instance is produced under closed rails and records environment posture and provenance alongside result data.

* Artifact path: artifacts/core/purity/purity\_report.json, and siblings under artifacts/core/purity/ if multiple reports are captured.  
* Schema path: docs/schemas/core/engine\_core\_purity\_report.schema.json. Generated-at and environment metadata: each artifact MUST include a payload-level generated\_at\_utc field, UTC ISO-8601, and closed-rails environment metadata sufficient to reconstruct the determinism posture used for the run. Provenance semantics and timestamp constraints follow §8.3, Artifacts with generated\_at\_utc, for all Engine Core families.

##### engine\_core\_two\_run\_logs — Engine Core two-run identity logs

**Purpose.** canonical JSON logs demonstrating two-run identity for Engine Core output, same inputs implying identical outputs, under closed rails. These logs are used to prove TWO\_RUN\_IDENTITY\_OK and related determinism tokens for the core engine.

* Artifact path: artifacts/core/two\_run/identity.json.  
* Schema path: docs/schemas/core/engine\_core\_two\_run\_logs.schema.json. **Notes.** arrays that function as sets, for example lists of tested scenarios, MUST follow arrays-as-sets rules in §4.2, deduped and ASCII-sorted.

##### engine\_core\_abba\_logs — Engine Core AB, BA, and ABBA parity logs

**Purpose.** canonical JSON logs for AB, BA, and ABBA runs over Engine Core, for example swapping label order where appropriate, used to demonstrate core behavior is invariant under symmetry-preserving input permutations after normalization.

* Artifact path: artifacts/core/abba/ab\_ba\_parity.json.  
* Schema path: docs/schemas/core/engine\_core\_abba\_logs.schema.json. **Notes.** these logs complement engine\_core\_two\_run\_logs by proving parity properties. The same canonical JSON and path-proof discipline applies.

##### engine\_core\_json\_compare\_logs — Engine Core JSON-compare logs

**Purpose.** canonical JSON logs produced by comparing Engine Core result JSON across two runs or two surfaces, for example CLI vs internal harness, and recording equality or inequality at the structured JSON level. These artifacts support JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK, and related core evidence tokens.

* Artifact path: artifacts/core/json\_compare/core\_result\_json\_compare.json.  
* Schema path: docs/schemas/core/engine\_core\_json\_compare\_logs.schema.json. **Notes.** logs MUST NOT include raw payloads beyond what the schema requires for comparison. They remain names-only and structural, and rely on canonical JSON for reproducible diffs.

**Canonical JSON policy and governed locations, Engine Core family.**

All Engine Core artifacts listed above MUST use the canonical JSON emitter governed by §4: UTF-8, ASCII-sorted keys, compact separators, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted by identity. All Engine Core artifacts and schemas MUST live under governed locations:

* `artifacts/core/**`  
* `docs/schemas/core/**` Transient generator paths, for example scratch or codex/out/\*\*, MUST NOT be indexed or mirrored.

**Evidence Index, Machine Mirror, and path-proofs.**

For each Engine Core family, the Human Evidence Index MUST contain at least one entry with the appropriate artifact\_key, for example engine\_core\_purity\_report, and a discovered\_physical\_path pointing to the governed artifact path. docs/evidence/INDEX.sha256 MUST be updated in the same PR when adding or changing any Engine Core artifact. The Machine Evidence Mirror MUST contain canonical JSONL records for each governed Engine Core artifact and schema, using artifact\_key names exactly as above and the minimum Mirror record schema in §8.3. Each Engine Core artifact and schema MUST have a sibling path-proof transcript, for example artifacts/core/purity/purity\_report.json.path\_proof.txt and docs/schemas/core/engine\_core\_purity\_report.schema.json.path\_proof.txt, that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via proof\_anchor. Path-proof sha256 and size\_bytes MUST match both the artifact’s canonical bytes and the Mirror record values.

**Acceptance hints (names-only; Engine Core skeleton).**

Engine Core evidence families participate in the existing Mirror and Index tokens referenced in §0.2 and §8.3, for example EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, JSON\_CANONICAL\_CHECK\_OK, and TWO\_RUN\_IDENTITY\_OK. Together with the sampler evidence families, they form the governed Engine Core and sampler evidence skeleton for DISS003/DISS004. PF12 binds these tokens to Engine Core artifacts by name and path only. Token semantics remain owned by Governance and Glow QA Guide.

#### 8.6.3.9 SBOM, registry, configuration, and BodyGraph evidence

##### SBOM

* `sbom/cyclonedx.json`  
* `sbom/cyclonedx.json.sha256`

##### Registry, reporting, and config

* `artifacts/registry/registry_report.json`  
* `config.magic10` — `Magic-10 configuration snapshot`. Names-only summary of Magic-10 order, caps, and seed metadata; canonical JSON.  
* Path: artifacts/thresholds/magic10\_config.json  
* Path-proof: artifacts/thresholds/magic10\_config.json.path\_proof.txt **Mirror record.** artifact\_key:"config.magic10", role:"snapshot", discovered\_physical\_path:"artifacts/thresholds/magic10\_config.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.1.

##### config.band\_edges — band-edges configuration snapshot

Names-only summary of band names, edges, clamp, rounding mode, and version linked to math/thresholds.json; canonical JSON.

* Path: artifacts/thresholds/band\_edges.json  
* Path-proof: artifacts/thresholds/band\_edges.json.path\_proof.txt **Mirror record.** artifact\_key:"config.band\_edges", role:"snapshot", discovered\_physical\_path:"artifacts/thresholds/band\_edges.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.2.

##### epic018.config.acceptance\_map — HDE-EPIC018 config acceptance map

PF09-style mapping from config tasks to artifact keys to tokens and tests; canonical JSON.

* Path: audit/EPIC-018\_config\_acceptance\_map.json  
* Path-proof: audit/EPIC-018\_config\_acceptance\_map.json.path\_proof.txt **Mirror record.** artifact\_key:"epic018.config.acceptance\_map", role:"snapshot", discovered\_physical\_path:"audit/EPIC-018\_config\_acceptance\_map.json", with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the artifact’s canonical bytes and path-proof as required by §8.3 and §8.14.3.

##### epic024.qa\_rca — EPIC024 QA RCA narrative file, close-pack companion

* Path: audit/EPIC-024\_QA\_RCA.md

##### config\_bundle.fe — typed frontend config bundle

Names-only projection of governed Magic-10 config, band-edges config, and registry topology or alias policy for client consumption; canonical JSON; includes a sources block keyed to the underlying config artifacts and registry report.

* Path: JSON file under artifacts/config\_bundles/, exact filename pinned by the bundle generator and tests.  
* Path-proof: sibling .path\_proof.txt transcript under artifacts/path\_proofs/ for the same path. **Mirror record.** artifact\_key:"config\_bundle.fe", role:"snapshot", discovered\_physical\_path equal to the bundle path, with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the bundle’s canonical bytes and path-proof as required by §8.3 and §8.15.

##### config\_bundle.be — typed backend config bundle

Names-only projection of governed Magic-10 config, band-edges config, full channels, centers, domains, alias policy, and registry-derived topology for engine and internal use; canonical JSON; includes a sources block keyed to the underlying config artifacts and registry report.

* Path: JSON file under artifacts/config\_bundles/, exact filename pinned by the bundle generator and tests.  
* Path-proof: a sibling \<bundle\_file\>.path\_proof.txt transcript stored alongside the bundle file in the same directory. **Mirror record.** artifact\_key:"config\_bundle.be", role:"snapshot", discovered\_physical\_path equal to the bundle path, with sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the bundle’s canonical bytes and path-proof as required by §8.3 and §8.15.

##### **BodyGraph adapter data-source and invariance**

**Governed primaries and schemas.**

* `artifacts/bodygraph/source_selection.snapshot.json`  
* `bodygraph.source_invariance.ab` → `artifacts/bodygraph/source_invariance/ab.json`; validates against `bodygraph.source_invariance.run.v2`.  
* `bodygraph.source_invariance.ba` → `artifacts/bodygraph/source_invariance/ba.json`; validates against `bodygraph.source_invariance.run.v2`.  
* `bodygraph.source_invariance.summary` → `artifacts/bodygraph/source_invariance/summary.json`; validates against `bodygraph.source_invariance.summary.v2`.  
* `bodygraph.source_invariance.schema.run.v2` → `schemas/bodygraph_source_invariance.run.v2.json`; JSON Schema 2020-12.  
* `bodygraph.source_invariance.schema.summary.v2` → `schemas/bodygraph_source_invariance.summary.v2.json`; JSON Schema 2020-12.  
* `epic038.pr01.bodygraph_release_bindings` → `artifacts/bodygraph/release_bindings.json`.  
* `artifacts/bodygraph/refresh_policy.snapshot.json`  
* `artifacts/bodygraph/metrics.snapshot.json`  
* `artifacts/bodygraph/keys_only.logs.sample`

`tools/evidence/generate_bodygraph_policy_proofs.py` is the sole primary producer. The three established source-invariance paths above are the current family. Duplicate PR-specific keys and v1 records MUST NOT be retained as current alternatives.

**Decisive source-invariance contract.**

A valid PASS requires all of the following:

* distinct DB and vendor sources;  
* distinct canonical source-representation hashes;  
* the same canonical normalized-input SHA-256;  
* two independently materialized runs per source, each reopening, deserializing, mapping or projecting, and emitting independently;  
* stable projected hashes and Presenter-emitted hashes across both runs;  
* equal source-neutral projections;  
* byte-identical output from the shared Presenter;  
* unsafe-field absence;  
* reversed AB and BA source order;  
* closed JSON Schema validation with `additionalProperties: false` at every object level;  
* canonical UTF-8 JSON with sorted keys, compact separators, no BOM, and exactly one trailing LF; and  
* a negative mutation receipt proving that a DB `bodygraph.profile` mutation produces `BODYGRAPH_SOURCE_DIVERGENCE` without embedding raw values.

`top_level_pass` and every run status MUST be derived from the current predicates. Constants, copied claims, label comparisons, parsed-object equality, or one materialization hashed twice do not satisfy this contract. `BG_SOURCE_INVARIANCE_OK` remains a `non_token`; this family does not mint or satisfy an acceptance token.

**Release binding.**

`artifacts/bodygraph/release_bindings.json` retains schema version 1 and its established key. Its binding set MUST contain exactly these ASCII-sorted paths:

* `artifacts/bodygraph/refresh_policy.snapshot.json`  
* `artifacts/bodygraph/source_invariance/summary.json`  
* `artifacts/bodygraph/source_selection.snapshot.json`

The historical DB/bridge Presenter receipt is not BodyGraph source-invariance truth and MUST NOT be included in this release binding.

All sibling path proofs, Human Evidence Index rows, Machine Evidence Mirror rows, checksum sentinels, mirror checksum, orientation/index companions, and their proofs remain owned by `tools/evidence/update_evidence_index.py`. Primary producers MUST NOT write those companions. Missing sources, reused acquisition, v1 records, duplicate current keys, missing negative evidence, noncanonical bytes, unknown fields, stale release bindings, or stale companions fail closed.

#### 8.6.3.10 HDAPI v2 vendor contract and adapter-conformance evidence

**Purpose.** Govern the HDAPI v2 contract inventory, validation, source-selection, request-shaping, response-mapping, adapter-boundary, closed-rails refusal, error-mapping, rate-limit, and release-binding evidence families. These artifacts are vendor-contract and adapter-conformance evidence only. They do not claim HDE runtime v2 conformance until implementation, tests, rails proof, governed evidence, and required open-rails OPS evidence are complete. They do not create:

* a new public Reader route  
* a change to Reader v1 bands-only posture  
* a second HTTP home  
* a serializer path  
* any OpenAI, LLM, AI-agent, chatbot, prompt, embedding, model-call, or AI-enablement evidence family

**Reusable-pattern posture.**

The HDE-EPIC033 contract-inventory evidence family MAY be reused as a pattern for later vendor-contract inventory work only when the new work preserves the same PF12 boundaries: source inventory, source-cache grounding, validation and quarantine posture, endpoint reference, contract map, Human Evidence Index, Machine Evidence Mirror, and path-proof binding. Reuse of this pattern MUST NOT claim runtime adapter conformance, open-rails vendor smoke, public Reader changes, new HTTP homes, AI scope, or closure of later tasks unless those claims are separately planned, implemented, evidenced, indexed, mirrored, and closed by their owning PF homes.

**Primary artifact paths.**

* `artifacts/vendor/hdapi_v2/source_inventory.json`: Canonical JSON inventory of public same-origin HumanDesignAPI documentation sources used for vendor-contract conformance. When refreshed, it records source URL, final URL, content type, fetch status, sha256, discovered\_from, last\_seen\_utc, source classification, source\_mode, cache path, and cache checksum posture when a cached source body or spec backs closed-rails replay.  
* `artifacts/vendor/hdapi_v2/source_inventory.md`: UTF-8 markdown summary of the vendor documentation source inventory, including documentation-discovery-only classification for llms.txt, llms-full.txt, and AI or LLM-oriented vendor documentation when those sources are inspected. When refreshed for HDE-EPIC033 PR-01, it MUST state that public same-origin HumanDesignAPI documentation sources are used only for contract inventory and do not call credentialed runtime vendor endpoints or claim runtime v2 conformance.  
* `artifacts/vendor/hdapi_v2/openapi_validation.log`: LF-terminated validation log for v2-routes.yaml, v1-routes.yaml, and any quarantined or suspect OpenAPI artifact.  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv`: LF-terminated endpoint reference for v2 and v1 route families, auth model, geocode-key requirement, tier, request content type, request fields, success envelope, error codes, and source\_spec.  
* `artifacts/vendor/hdapi_v2/known_anomalies.md`: UTF-8 markdown anomaly ledger. It MUST quarantine api-reference/openapi.json unless validation proves HumanDesignAPI domain, title, server, and path-family ownership.  
* `artifacts/vendor/hdapi_v2/contract_map.json`: Canonical JSON contract map binding validated vendor sources to the required v2 and v1 route families, including POST /v2/charts, POST /v2/charts/simple, POST /v2/charts/coordinates, POST /v1/bodygraphs, and POST /v1/bodygraphs/simple.  
* `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`: Canonical JSON snapshot of v2 source-selection policy and v1 legacy isolation.  
* `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`: Canonical JSON snapshot of v2 request-shaping posture for the v2 chart endpoints. It MUST be derived from the governed contract map and MUST NOT guess credential names, base URLs, or request bytes not pinned by the owning contract and infrastructure homes. It MUST preserve HD\_API\_BASE\_URL as the configured base-url owner when that posture is being proven, and it MAY record HDAPI\_BASE\_URL only as deprecated alias, compatibility, observed drift, or migration evidence. It MUST distinguish vendor endpoint provenance such as /v2/charts from active runtime resource paths such as charts, charts/simple, and charts/coordinates; active runtime resource paths MUST be version-neutral when that is the implementation posture being evidenced. It MUST preserve auth-header family as redacted shape, including Authorization: Bearer for current v2 chart-style routes, HD-Api-Key: for legacy v1 BodyGraph routes when intentionally preserved, and HD-Geocode-Key: where geocoding is required. Auth-header source SHOULD be route or contract metadata rather than vendor API version-string inference when asserted. Raw header values and vendor payload bodies MUST NOT be persisted in this artifact.  
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`: Canonical JSON snapshot of v2 response-envelope mapping into HDE internal inputs. It MUST preserve response type, success status, errorCode, data payload identity posture, route variant, route family, response-envelope fields, and no-claim posture. If v2 ChartResult or ChartSimpleResult response data cannot truthfully feed existing BodyGraph, person, cache, compat, sampler, or admin paths without schema or adapter changes, this artifact MUST record the exact adapter/schema gap and MUST NOT claim normalized data-path proof, BodyGraph cache compatibility, compat-input compatibility, runtime v2 conformance, public Reader change, app-side HumanDesignAPI call path, raw vendor payload persistence, or compatibility by inference. A later runtime compatibility claim requires a bounded adapter/schema proof or implementation that maps the selected vendor payload family into the existing BodyGraph/person/cache contract.  
* `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`: LF-terminated guard log proving v1 BodyGraph routes remain explicitly legacy behavior and are not silently collapsed into v2 chart routes.  
* `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`: LF-terminated architecture proof log showing that the vendor seam does not create a new HTTP home, bypass adapter guards, or introduce ad-hoc serialization.  
* `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt`: LF-terminated closed-rails refusal artifact proving deterministic no-external-I/O behavior for v2 vendor paths when rails are closed.  
* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`: Canonical JSON snapshot of v2 vendor HTTP outcomes, error-envelope mapping, malformed-response handling, retry classification, malformed-response classification, network-error posture, redirect-response posture, route/auth posture, and HDE typed-error mapping. It MUST be generated and checked under closed rails when used as closed-rails provider-outcome evidence. It MUST avoid vendor payload echo, raw request bodies, raw response bodies, raw vendor payloads, raw secret headers, plaintext secret values, public Reader changes, public route/flag/payload/transport changes, open-rails execution claims, live vendor claims, full runtime conformance claims, and AI scope claims.  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`: Canonical JSON snapshot of v2 429, rate-limit, Retry-After, retryability, and Retry-After parsing posture. It MUST remain keys-only and secret-free. It MUST distinguish retryable and non-retryable status families, record bounded Retry-After cases without preserving sensitive provider payloads, and preserve the same no-claim posture as the provider-outcome evidence family when used for HDE-EPIC035 PR-01 or later equivalent evidence.  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`: Canonical JSON snapshot binding HDAPI v2 provider-outcome, response-normalization, schema-gap, release, pack, or BodyGraph-cache compatibility evidence when that binding is claimed. It MUST name the evidence families being bound, preserve SHA linkage to the referenced artifacts, preserve chronology where required by the evidence family, fail closed on stale or mismatched source artifacts, and preserve explicit nonclaims for full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, HDE-FERM008.5 closure, public Reader change, new public routes, raw payload persistence, and AI scope unless those claims are separately proven and governed. Future adapter/schema proof for v2 chart-to-BodyGraph compatibility. A future proof or implementation that claims v2 chart data feeds existing BodyGraph, person, cache, compatibility, sampler, or compute flows MUST be a governed, secret-safe evidence family. It MUST show:  
* which vendor payload family is used, including whether the evidence uses ChartResult, ChartSimpleResult, another v2 response family, or an explicit legacy fallback  
* which vendor response fields are required for the HD Engine contract  
* which internal BodyGraph, person, cache, compatibility, sampler, or compute fields are populated  
* which required fields are absent, unsupported, summarized, redacted, or intentionally excluded  
* whether the adapter is lossless enough for HD Engine compute  
* whether any legacy fallback remains  
* whether raw vendor payloads are persisted, redacted, summarized, excluded, or represented only by digest or field-coverage evidence  
* what normalized internal output contract is produced  
* what nonclaims remain after the proof. ChartSimpleResult MAY support bounded live smoke, authentication proof, geocode-key proof, provider availability proof, or minimal route-family confirmation. It MUST NOT be treated as sufficient for full BodyGraph, person, cache, compatibility, or compute input unless a governed adapter/schema proof demonstrates that it contains every required field for that contract. The preferred future v2 payload candidate is the richest relevant v2 chart response, currently the full chart route / ChartResult family, unless a future vendor-route policy or ADR proves another source. If full ChartResult does not contain all required BodyGraph details, the proof MUST record the exact field gap and either define a sanctioned adapter strategy, identify the correct vendor route for full BodyGraph detail, retain explicit legacy fallback, or route a new ADR before runtime compatibility is claimed. The proof MUST NOT persist raw secrets, uncontrolled raw vendor payloads, public Reader payload changes, new HTTP-home claims, app-side vendor credential ownership, or AI scope. Recording an adapter/schema gap is acceptable as gap evidence only; it MUST NOT be reused as proof of runtime compatibility. **Future `bg:resolve --source vendor` route-policy evidence.** A future proof or implementation that claims bg:resolve \--source vendor resolves BodyGraph detail MUST be a governed, secret-safe evidence family. It MUST distinguish the selected route policy as exactly one of: v2 chart-backed BodyGraph resolution, explicit legacy BodyGraph fallback, dual-route policy, or unsupported runtime nonclaim. The evidence MUST record:  
* the configured base-url posture  
* the selected runtime resource path family  
* the request shape used by bg:resolve \--source vendor  
* whether the route is v2 chart-backed, legacy BodyGraph, dual-route, or unsupported  
* the redacted auth-header family and geocode-key posture where applicable  
* whether the selected response contains the required BodyGraph detail  
* the normalized internal BodyGraph/person/cache output contract when compatibility is claimed  
* any legacy fallback or vendor-route gap that remains  
* the nonclaims preserved by the proof. The evidence MUST distinguish simple route availability from full BodyGraph-detail resolution. A successful charts/simple observation MAY prove provider availability, auth posture, geocode-key posture, or route-family availability. It MUST NOT prove that bg:resolve \--source vendor resolves complete BodyGraph detail unless the route-policy and adapter/schema proof also establish the required internal contract. The evidence MUST NOT treat accidental /v2/bodygraphs composition, route-family mismatch, or a wrong-shape 404 as generic provider unavailability. It MUST classify route-shape mismatch separately from provider unavailability when that distinction is visible.

**Current bounded configured-v2 mapped-cache persistence evidence family.**

This family governs bounded non-production persistence of adapter-mapped HDE BodyGraph/cache payloads. Its current primary bindings are:

* `epic038.pr05.v2_mapped_cache.write_transcript` → `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`  
* `epic038.pr05.v2_mapped_cache.read_back_transcript` → `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`  
* `epic038.pr05.v2_mapped_cache.canonical_parity` → `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`  
* `epic038.pr05.v2_mapped_cache.no_raw_vendor_payload` → `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`  
* `epic038.pr05.v2_mapped_cache.idempotence` → `artifacts/bodygraph/v2_mapped_cache/idempotence.log`  
* `epic038.pr05.v2_mapped_cache.closed_rails_refusal` → `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`  
* `epic038.pr05.v2_mapped_cache.legacy_fallback` → `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`  
* `epic038.pr05.v2_mapped_cache.manifest` → `artifacts/bodygraph/v2_mapped_cache/manifest.json`

These primaries use record type `epic038_pr05_mapped_cache_evidence`. The governed schema bindings are:

* `epic038.pr05.v2_mapped_cache.transcript_schema` → `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`, schema `bodygraph.v2_mapped_cache.transcript.v1`; and  
* `epic038.pr05.v2_mapped_cache.manifest_schema` → `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`, schema `bodygraph.v2_mapped_cache.manifest.v1`.

The schemas use record type `epic038_pr05_schema`. `tools/evidence/generate_v2_mapped_cache_evidence.py` is the sole primary producer. `tools/evidence/update_evidence_index.py` owns sibling path proofs, Human Evidence Index rows, Machine Evidence Mirror rows, hash sentinels, checksums, and orientation companions.

The family MUST prove canonical write/read-back parity, absence of raw vendor-envelope persistence, idempotence, closed-rails refusal, adapter-mapped payload use, cache-compatible identity types, and legacy non-v2 fallback preservation. It does not authorize production-like writes and does not create a public Reader change, new public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI ownership, raw secret or request/response persistence, AI scope, QA PASS, PF09 status movement, OPS completion, PO closeout, board update, production deployment, acceptance-token satisfaction, or epic closeout.

##### HDE-EPIC036 bg\_resolve\_\* route-policy evidence family

These artifacts are governed HDAPI v2 BodyGraph route-policy evidence for HDE-EPIC036. They do not by themselves claim QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, or AI scope.

* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`: Canonical JSON snapshot of the selected bg:resolve \--source vendor route policy. It MUST record configured-v2 unsupported-runtime nonclaim, non-v2 explicit legacy fallback, dual-route policy nonimplementation unless later implemented, selected route family, redacted auth posture, geocode posture, and no-claim boundaries.  
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the route-policy snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`: Canonical JSON proof of BodyGraph-detail sufficiency or explicit unsupported-runtime nonclaim. It MUST NOT treat charts/simple success, route availability, provider availability, or wrong-shape legacy BodyGraph behavior as proof that v2 chart data feeds existing BodyGraph, person, cache, or compatibility flows.  
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`: Required sibling path-proof transcript when the BodyGraph-detail proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`: Canonical JSON nonclaim ledger for bg:resolve \--source vendor route-policy work. It MUST preserve no full runtime conformance, no public Reader change, no public route, no public flag, no public payload change, no new HTTP home, no app-side vendor credential ownership, no raw request or response body persistence, no raw payload persistence, and no AI scope claims unless later evidence explicitly changes those claims.  
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`: Required sibling path-proof transcript when the runtime nonclaims artifact is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`: Canonical JSON request-shape snapshot for bg:resolve \--source vendor. It MUST distinguish configured-v2 unsupported-runtime posture from explicit legacy fallback and MUST record whether a request is constructed or blocked before request construction.  
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the request-shape snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`: Canonical JSON policy-binding snapshot that ties route-policy evidence, BodyGraph-detail evidence, request-shape evidence, runtime nonclaims, and follow-up boundaries together. It MUST distinguish PR implementation proof from later evidence-loop binding, QA proof, OPS execution, PF09 drainage, and closeout.  
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the policy-binding snapshot is treated as governed evidence.  
* `audit/qa/hde-epic036/route_policy_decision.log`: LF-terminated route-policy decision log for HDE-EPIC036 PR-01. It records the selected classification, request-shape posture, explicit legacy fallback posture, dual-route posture, BodyGraph-detail sufficiency posture, and no-claim boundaries.  
* `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`: Required sibling path-proof transcript when the route-policy decision log is treated as governed evidence.

##### HDE-EPIC037 v2 BodyGraph-detail runtime-conformance evidence chain

These artifacts are governed HDE-EPIC037 evidence for the HDE-FERM008.7 through HDE-FERM008.12 BodyGraph-detail runtime-conformance chain. They record field sufficiency, pure adapter mapping, configured-v2 bg:resolve \--source vendor route policy, v2-to-compat proof, PO-produced OPS runtime smoke, and parent evidence binding. They do not by themselves claim QA PASS, OPS completion by PR work, PF09 status movement, PF09 status drainage, PO closeout, board update, merge action, PF-Canon edit, epic closeout, production deployment, full HumanDesignAPI v2 platform conformance beyond the bounded HDE-FERM008.7 through HDE-FERM008.11 evidence chain, public Reader change, public route, public flag, public payload or transport change, new HTTP home, app-side HumanDesignAPI ownership, raw secret persistence, raw request body persistence, raw response body persistence, uncontrolled raw vendor payload persistence, or AI scope.

**PR-01 field-sufficiency artifacts.**

* `artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json`: Canonical JSON proof for HDE-FERM008.7. It records candidate payload-family evaluations, typed insufficient classification, missing internal contract fields, fail-closed posture, and no compute-ready/runtime-conformance claim.  
* `artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json.path_proof.txt`: Required sibling path-proof transcript when the field-sufficiency proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json`: Canonical JSON snapshot of the internal HDE BodyGraph/person/cache/compat adapter contract used to evaluate v2 ChartResult and ChartSimpleResult readiness.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the adapter-contract snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json`: Canonical JSON nonclaim ledger for PR-01 field-sufficiency evidence. It MUST preserve unsupported vendor-field, unsupported HDE-path, no-public-surface, no-live-vendor, no-runtime-conformance, no-raw-payload-persistence, no-QA-PASS, no-OPS, no-closeout, and no-AI posture.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json.path_proof.txt`: Required sibling path-proof transcript when the adapter-contract nonclaims artifact is treated as governed evidence.

**PR-02 adapter-mapping artifacts.**

* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json`: Canonical JSON snapshot for HDE-FERM008.8. It records pure context-backed ChartResult adapter mapping, adapter purity, ADAPTER\_MAPPED posture, cache-compatible metadata, adapter-mapped no-raw-vendor-payload posture, and explicit nonclaims.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the adapter-mapping snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json`: Canonical JSON negative-fixture evidence for missing context, missing detail fields, malformed data, unsupported payloads, and wrong-route failures.  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json.path_proof.txt`: Required sibling path-proof transcript when the adapter negative fixtures are treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json`: Canonical JSON no-raw-payload-persistence evidence for PR-02 adapter scope. It MUST NOT claim generic log/privacy tokens unless those claims are separately registered and proven.  
* `artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json.path_proof.txt`: Required sibling path-proof transcript when the no-raw-payload-persistence artifact is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json`: Canonical JSON public Reader no-change evidence. It records no public route, flag, payload, transport, or HTTP-home claim.  
* `artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json.path_proof.txt`: Required sibling path-proof transcript when the public Reader no-change artifact is treated as governed evidence.

**PR-03 bg:resolve \--source vendor route-policy artifacts.**

* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json`: Canonical JSON snapshot for HDE-FERM008.9. It records configured-v2 bg:resolve \--source vendor route policy selecting the version-neutral charts resource path and deterministic v2 ChartResult adapter, with redacted Bearer auth posture and explicit nonclaims.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the v2 route-policy snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json`: Canonical JSON request-shape proof for version-neutral charts construction, v2 Bearer auth posture, geocode posture, and no v2 legacy bodygraphs request.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the request-shape snapshot is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json`: Canonical JSON closed-rails no-external-I/O proof for bg:resolve \--source vendor route-policy work.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json.path_proof.txt`: Required sibling path-proof transcript when the closed-rails no-I/O proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json`: Canonical JSON snapshot of explicit non-v2 legacy BodyGraph fallback behavior.  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json.path_proof.txt`: Required sibling path-proof transcript when the legacy-fallback snapshot is treated as governed evidence.

**PR-04 v2-to-compat artifacts.**

* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json`: Canonical JSON proof for HDE-FERM008.10. It records mapped v2 ChartResult adapter outputs accepted by the existing compatibility compute path, category-count posture, output hash posture, raw request/response vendor body absence, and explicit nonclaims.  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json.path_proof.txt`: Required sibling path-proof transcript when the v2-to-compat proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json`: Canonical JSON two-run identity proof for the v2-to-compat evidence family.  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json.path_proof.txt`: Required sibling path-proof transcript when the two-run proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json`: Canonical JSON AB/BA pair-order identity proof for the v2-to-compat evidence family.  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json.path_proof.txt`: Required sibling path-proof transcript when the pair-order proof is treated as governed evidence.  
* `artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json`: Canonical JSON admin/public boundary proof showing mapped v2 adapter output does not create public Reader drift or admin-only leakage.  
* `artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json.path_proof.txt`: Required sibling path-proof transcript when the admin/public boundary artifact is treated as governed evidence.

**OPS-01 PO-produced runtime-smoke evidence.**

* `audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt`: LF-terminated command transcript for the PO-produced OPS-01 runtime smoke.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log`: UTF-8 stdout capture for OPS-01.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/stderr.log`: UTF-8 stderr capture for OPS-01.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt`: LF-terminated exit-code ledger for OPS-01.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json`: Canonical JSON redacted environment-presence evidence for OPS-01. It MUST remain presence-only or redacted for secret-bearing values.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json`: Canonical JSON request summary for OPS-01. It MUST preserve configured base URL redaction, route posture, request/response body non-persistence posture, and secret-safe header posture.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json`: Canonical JSON result summary for OPS-01. It records adapter status, adapter payload family, mapped no-raw-vendor-payload cache posture, exit code, runtime-smoke support posture, and explicit nonclaims.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json`: Canonical JSON adapter-mapping result summary for OPS-01.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json`: Canonical JSON compatibility-path result summary for OPS-01.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json`: Canonical JSON failure-classification artifact for OPS-01 when retained.  
* `audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt`: LF-terminated checksum ledger for OPS-01 retained evidence files. Each promoted OPS-01 file above MUST have a sibling .path\_proof.txt transcript when indexed, mirrored, or used as acceptance-support evidence.  
* `audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md`: UTF-8 markdown QA pointer to the PO-produced OPS-01 evidence root. It is a pointer only and MUST NOT be treated as OPS execution, QA PASS, PF09 status movement, or closeout.

**PR-05 parent evidence binding artifacts.**

* `docs/acceptance_map_epic037.json`: Canonical JSON HDE-EPIC037 parent acceptance map. It may record parent\_posture=supportable\_to\_done only as later-drain support and MUST preserve that it does not move PF09 status.  
* `docs/acceptance_map_epic037.json.path_proof.txt`: Required sibling path-proof transcript when the acceptance map is treated as governed evidence.  
* `audit/qa/hde-epic037/token_evidence_matrix.md`: UTF-8 markdown token-to-evidence matrix for HDE-EPIC037. It MUST distinguish evidence binding from QA PASS, OPS completion by PR work, PF09 status movement, PF09 drainage, PO closeout, board update, merge action, PF-canon edit, and epic closeout.  
* `audit/qa/hde-epic037/token_evidence_matrix.md.path_proof.txt`: Required sibling path-proof transcript when the token evidence matrix is treated as governed evidence.  
* `audit/qa/hde-epic037/acceptance_map_viability.log`: LF-terminated acceptance-map viability log for HDE-EPIC037 PR-05.  
* `audit/qa/hde-epic037/acceptance_map_viability.log.path_proof.txt`: Required sibling path-proof transcript when the viability log is treated as governed evidence.  
* `audit/qa/hde-epic037/parent_evidence_binding.log`: LF-terminated parent evidence-binding log for HDE-FERM008.12. It records HDE-FERM008.7 through HDE-FERM008.12 evidence families, index/mirror/hash/path-proof posture, parent support posture, and nonclaims.  
* `audit/qa/hde-epic037/parent_evidence_binding.log.path_proof.txt`: Required sibling path-proof transcript when the parent evidence-binding log is treated as governed evidence.  
* `audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md`: UTF-8 markdown PR-05 doc-delta surface. It records later-drain targets and MUST NOT be treated as the PF-canon drain itself.  
* `audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the PR-05 doc-delta surface is treated as governed evidence.  
* `audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md`: UTF-8 markdown QA-meta PR-05 doc-delta surface. It records QA-root doc-delta context and MUST NOT be treated as the PF-canon drain itself.  
* `audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md.path_proof.txt`: Required sibling path-proof transcript when the QA-meta PR-05 doc-delta surface is treated as governed evidence.

##### HDAPI v2 source-cache inputs

* `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`: Source-cache route-spec input for validated v2 routes. UTF-8 YAML text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`: Source-cache route-spec input for validated legacy v1 routes. UTF-8 YAML text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/api-reference.openapi.json`: Source-cache suspect OpenAPI input. Canonical JSON when present. It remains quarantined unless validation proves HumanDesignAPI domain, title, server, and path-family ownership.  
* `artifacts/vendor/hdapi_v2/source_cache/authentication.body`: Source-cache rendered public documentation body for authentication context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/coordinates_guide.body`: Source-cache rendered public documentation body for coordinates guidance. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`: Bounded source-cache endpoint-tier excerpt used for source-backed tier parsing. LF-terminated text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`: Source-cache public documentation-discovery body for llms.txt. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/migration_v1_to_v2.body`: Source-cache rendered public documentation body for v1-to-v2 migration context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/rate_limiting.body`: Source-cache rendered public documentation body for rate-limiting context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/response_format.body`: Source-cache rendered public documentation body for response-format context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/robots_preflight.body`: Source-cache rendered public documentation body for robots-preflight context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`: Canonical JSON metadata ledger for cached public documentation and route-spec inputs.  
* `artifacts/vendor/hdapi_v2/source_cache/v1_overview.body`: Source-cache rendered public documentation body for v1 overview context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_coordinates_chart_page.body`: Source-cache rendered public documentation body for the v2 coordinates chart page. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_full_chart_page.body`: Source-cache rendered public documentation body for the v2 full chart page. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_overview.body`: Source-cache rendered public documentation body for v2 overview context. UTF-8 text when present.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_simple_chart_page.body`: Source-cache rendered public documentation body for the v2 simple chart page. UTF-8 text when present.

**Source-cache posture.**

Closed-rails replay for source-inventory rows MUST be backed by cached bodies or route specs and matching checksums. Metadata-only replay for rendered endpoint or contract pages is not sufficient when those rows are promoted as governed contract-inventory evidence. The suspect api-reference/openapi.json source-cache body MAY be absent or unavailable without blocking promoted inventory generation when the validated v1 and v2 route YAML specs remain usable and the suspect OpenAPI artifact is recorded as quarantined. Tier handling MUST be parsed from actual endpoint table cells in the bounded cached endpoint-tier excerpt and MUST NOT rely on fixed substring defaults. Source-cache inputs are governed support inputs for the HDAPI v2 contract-inventory family. When a source-cache input is indexed, mirrored, or used as acceptance-support evidence, it MUST have a sibling .path\_proof.txt transcript and MUST use the exact artifact\_key emitted by the governed evidence updater for that path.

**Artifact-key bindings.**

* `hdapi_v2.source_inventory_json` maps to `artifacts/vendor/hdapi_v2/source_inventory.json`.  
* `hdapi_v2.source_inventory_md` maps to `artifacts/vendor/hdapi_v2/source_inventory.md`.  
* `hdapi_v2.openapi_validation` maps to `artifacts/vendor/hdapi_v2/openapi_validation.log`.  
* `hdapi_v2.endpoint_reference` maps to `artifacts/vendor/hdapi_v2/endpoint_reference.csv`.  
* `hdapi_v2.known_anomalies` maps to `artifacts/vendor/hdapi_v2/known_anomalies.md`.  
* `hdapi_v2.contract_map` maps to `artifacts/vendor/hdapi_v2/contract_map.json`.  
* `hdapi_v2.source_selection` maps to `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`.  
* `hdapi_v2.request_shaping` maps to `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`.  
* `hdapi_v2.response_mapping` maps to `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`.  
* `hdapi_v2.response_mapping_pr02` maps to `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json when the shared response-mapping snapshot is promoted as HDE-EPIC035 PR-02 evidence. The binding MUST validate that the payload is the expected PR-02 response-normalization or adapter/schema-gap payload before emitting the PR-02 artifact key. If an earlier epic also used the shared path, the updater MUST preserve distinct non-shared evidence rows and skip only the promoted shared-snapshot row required to prevent duplicate conflicting semantics`.  
* `hdapi_v2.v1_legacy_guard` maps to `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`.  
* `hdapi_v2.adapter_boundary_proof` maps to `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`.  
* `hdapi_v2.closed_rails_refusal` maps to `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt`.  
* `hdapi_v2.error_mapping` maps to `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`.  
* `hdapi_v2.rate_limit_headers` maps to `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`.  
* `hdapi_v2.release_binding` maps to `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`.  
* `hdapi_v2.bg_resolve_route_policy` maps to `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`.  
* `hdapi_v2.bg_resolve_bodygraph_detail_proof` maps to `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`.  
* `hdapi_v2.bg_resolve_runtime_nonclaims` maps to `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`.  
* `hdapi_v2.bg_resolve_request_shape` maps to `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`.  
* `hdapi_v2.bg_resolve_policy_binding` maps to `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`.  
* `epic036.pr01.route_policy_decision` maps to `audit/qa/hde-epic036/route_policy_decision.log`.  
* `epic036.pr02.acceptance_map` maps to `docs/acceptance_map_epic036.json`.  
* `epic036.pr02.token_matrix` maps to `audit/qa/hde-epic036/token_evidence_matrix.md`.  
* `epic036.pr02.acceptance_map_viability` maps to `audit/qa/hde-epic036/acceptance_map_viability.log`.  
* `epic036.pr02.doc_deltas` maps to `audit/docdeltas/hde-epic036_doc_deltas.md`.  
* `epic036.pr02.qa_meta_doc_deltas` maps to `audit/qa/hde-epic036/00_meta/doc_deltas.md`.  
* `hdapi_v2.hde_epic037_field_sufficiency_proof` maps to `artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json`.  
* `hdapi_v2.hde_epic037_adapter_contract` maps to `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json`.  
* `hdapi_v2.hde_epic037_adapter_contract_nonclaims` maps to `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json`.  
* `epic037.pr01.doc_deltas` maps to `audit/docdeltas/hde-epic037_doc_deltas.md`.  
* `epic037.pr01.qa_meta_doc_deltas` maps to `audit/qa/hde-epic037/00_meta/doc_deltas.md`.  
* `hdapi_v2.hde_epic037_adapter_mapping` maps to `artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json`.  
* `hdapi_v2.hde_epic037_adapter_negative_fixtures` maps to `artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json`.  
* `hdapi_v2.hde_epic037_public_reader_no_change` maps to `artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json`.  
* `hdapi_v2.hde_epic037_no_raw_payload_persistence` maps to `artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json`.  
* `hdapi_v2.hde_epic037_bg_resolve_v2_route_policy` maps to `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json`.  
* `hdapi_v2.hde_epic037_bg_resolve_request_shape` maps to `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json`.  
* `hdapi_v2.hde_epic037_bg_resolve_closed_rails_no_io` maps to `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json`.  
* `hdapi_v2.hde_epic037_bg_resolve_legacy_fallback` maps to `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json`.  
* `hdapi_v2.hde_epic037_v2_to_compat_proof` maps to `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json`.  
* `hdapi_v2.hde_epic037_v2_to_compat_two_run` maps to `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json`.  
* `hdapi_v2.hde_epic037_v2_to_compat_pair_order` maps to `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json`.  
* `hdapi_v2.hde_epic037_admin_public_boundary` maps to `artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json`.  
* `epic037.ops01.commands` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt`.  
* `epic037.ops01.stdout` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log`.  
* `epic037.ops01.stderr` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/stderr.log`.  
* `epic037.ops01.exit_codes` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt`.  
* `epic037.ops01.env_presence_redacted` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json`.  
* `epic037.ops01.request_summary` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json`.  
* `epic037.ops01.result_summary` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json`.  
* `epic037.ops01.adapter_mapping_result_summary` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json`.  
* `epic037.ops01.compat_path_result_summary` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json`.  
* `epic037.ops01.failure_classification` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json`.  
* `epic037.ops01.files_sha256` maps to `audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt`.  
* `epic037.ops01.qa_pointer` maps to `audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md`.  
* `epic037.pr05.acceptance_map` maps to `docs/acceptance_map_epic037.json`.  
* `epic037.pr05.token_matrix` maps to `audit/qa/hde-epic037/token_evidence_matrix.md`.  
* `epic037.pr05.acceptance_map_viability` maps to `audit/qa/hde-epic037/acceptance_map_viability.log`.  
* `epic037.pr05.parent_evidence_binding` maps to `audit/qa/hde-epic037/parent_evidence_binding.log`.  
* `epic037.pr05.parent_binding_doc_deltas` maps to `audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md`.  
* `epic037.pr05.qa_meta_parent_binding_doc_deltas` maps to `audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md`.

##### Source precedence and quarantine

The source-precedence posture for this family is:

* validated v2 and v1 YAML specs first  
* rendered endpoint pages second  
* high-level guide pages third  
* suspect artifacts quarantined until validated api-reference/openapi.json MUST NOT define vendor bytes, schemas, endpoint routes, request shaping, response mapping, or architecture conformance unless its HumanDesignAPI domain, title, server, and path-family ownership are validated and recorded in the governed validation artifacts. Vendor documentation-discovery files such as llms.txt and llms-full.txt MAY be recorded only as documentation-source inventory entries. They MUST NOT create:  
* AI product scope  
* AI runtime scope  
* AI evidence families  
* AI-provider config keys  
* AI rails  
* AI tokens  
* AI QA obligations

**Path-proofs and indexing.**

Each primary artifact above MUST have a sibling .path\_proof.txt transcript stored alongside the artifact when the artifact is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. Each source-cache support input above MUST have a sibling .path\_proof.txt transcript when the source-cache input is promoted into governed evidence, indexed, mirrored, or used as acceptance-support evidence. Canonical JSON artifacts in this family MUST follow PF12 canonical JSON rules:

* UTF-8  
* no BOM  
* ASCII-sorted keys  
* compact separators  
* exactly one trailing LF YAML, text, markdown, CSV, body, and log artifacts in this family MUST be UTF-8 and LF-terminated. The Human Evidence Index and the Machine Evidence Mirror MUST each carry exactly one binding for each promoted artifact path above under the normal PF12 parity rules. The corresponding Mirror records MUST use the artifact\_key bindings above where defined and MUST set proof\_anchor to the sibling .path\_proof.txt transcript for that artifact. When this family changes, the following MUST be refreshed coherently in the same change:  
* changed primary artifacts  
* promoted source-cache inputs  
* sibling path-proofs  
* Human Index  
* Human Index hash sentinel  
* Machine Mirror  
* Machine Mirror checksum sidecar  
* required Index and Mirror sibling path-proofs

#### 8.6.3.11 Lifecycle, admin QA, and runbooks

* `artifacts/db/backup_manifest.json`  
* `artifacts/db/restore_verify.log`  
* `artifacts/db/retention_run.log`

##### Admin QA and runbooks

* `docs/run/PROD_ENDPOINTS.json`  
* `docs/run/RUN_PROD_QA.md`  
* `docs/run/EPIC011_TEST_IDENTITIES.md`  
* `artifacts/ops/admin_vendor_calls.jsonl`

#### 8.6.3.12 Epic QA harness ledger artifacts

These entries register QA harness ledger files that summarize Live QA results as current-state evidence, while keeping per-run retention optional and non-canon unless explicitly promoted. The invariant required outputs for a Live QA run are the per-check primary log and the step-logs manifest; additional ledger artifacts may exist but MUST NOT be required for closure by default.

**Production-affecting open-rails Live QA evidence.**

When a Live QA plan includes a bounded open-rails step for production-affecting behavior, the evidence MUST remain redacted, bounded, and governed. It MAY record header names, redacted header-shape posture, endpoint or route family, environment label, rails posture, request class, result class, and safe status or error classification. It MUST NOT record raw secrets, raw bearer tokens, raw API keys, uncontrolled production data, full private payloads, or full vendor payload bodies unless a later owning canon explicitly permits that payload and the evidence is still secret-safe. Open-rails Live QA evidence proves only the behavior actually exercised. It MUST preserve nonclaim boundaries for full runtime conformance, parent-task completion, public Reader expansion, new public routes, new public flags, public payload changes, new HTTP homes, AI scope, PO closeout, and epic closure unless those claims are separately bound by their owning canon and governed evidence.

**Open-rails QA evidence-family distinction.**

When an epic requires open-rails QA, PF12-governed artifacts MUST keep the open-rails QA proof family distinguishable from closed-rails proof, OPS evidence, implementation evidence, repo inspection, static validation, schema validation, Evidence Index validation, Machine Mirror validation, and path-proof validation. The Human Evidence Index and Machine Evidence Mirror SHOULD preserve the distinction through artifact keys, roles, paths, notes, record types, or equivalent governed metadata emitted by the evidence tooling. A prior OPS observation may be referenced only when it is explicitly bound into QA evidence or accepted under QA posture by the owning QA plan and evidence artifacts.

**QA\_PLAN\_UPDATE routing for non-QA-root governed evidence.**

When final PASS-grade QA proof relies on a refreshed or newly bound governed evidence surface outside the QA root, the QA package MUST include a QA\_PLAN\_UPDATE routing receipt before the post-routing proof is accepted. The receipt MUST be a governed QA evidence artifact under the QA checks root, MUST have a sibling path-proof transcript when promoted, and MUST name the routing type, source or trigger, affected check or closeout proof, non-QA-root artifacts being bound, allowed action, required post-routing receipt, rails posture, and nonclaims. A QA\_PLAN\_UPDATE routing receipt does not by itself claim product behavior, token satisfaction, PF09 drainage, PO closeout, or epic closure. It records the provenance route that allows the later proof to rely on the named non-QA-root governed evidence.

##### Canonical epic QA root

* `audit/qa/<epic-id>/`

##### Invariant required outputs (current-state; canonical paths)

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`: Required per-check canonical step receipt and primary evidence log. Non-empty UTF-8 text. When a Live QA step reaches a governed verdict, this file is the decisive per-check receipt of record.  
* `audit/qa/<epic-id>/checks/<check_id>/primary.log.path_proof.txt`: Required sibling path-proof transcript whenever the per-check primary log exists as governed evidence for the run.  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json`: Per-epic manifest acting as a current-state index keyed by check\_id, pointing to (at minimum) each check’s status and the canonical path to its primary log. Records-only canonical JSON (UTF-8, ASCII-sorted keys, compact, exactly one trailing LF).  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`: Required sibling path-proof transcript whenever the root-level current-state manifest is created, refreshed, or indexed as governed evidence for the run.  
* `audit/qa/<epic-id>/checks/po-000/qa_step_logs_manifest.json`: Optional step-0, check-scoped current-state copy of the QA step logs manifest. When a Live QA plan explicitly names this check-scoped manifest as a required deliverable, it is the binding surface for that run.  
* `audit/qa/<epic-id>/checks/po-000/qa_step_logs_manifest.json.path_proof.txt`: Required sibling path-proof transcript whenever the step-0 check-scoped manifest copy exists. Legacy/root-level continuity note. A root-level pair at audit/qa//qa\_step\_logs\_manifest.json and audit/qa//qa\_step\_logs\_manifest.json.path\_proof.txt MAY remain for continuity, but it is non-decisive for a run when the Live QA plan explicitly binds the step-0 check-scoped pair.

##### Optional per-check outputs (check-owned; current-state if present)

* `audit/qa/<epic-id>/checks/<check_id>/transcript.txt`: Optional per-check execution transcript (non-empty UTF-8 text). If treated as governed evidence, it MUST have a sibling transcript.txt.path\_proof.txt.  
* `audit/qa/<epic-id>/checks/<check_id>/deliverables_report.md`: Optional per-check deliverables report summarizing step-scoped planned outputs and observed artifacts. When used as QA proof, it is admissible only if it lands under the canonical epic QA root and the canonical check directory for that step. It MUST NOT rely on per-run nesting as a correctness key.  
* `audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md`: Optional CHECK po-001 bounded-scope inventory snapshot used to preserve the approved conjunction surface inventory in the canonical check directory. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json`: Optional CHECK po-001 catalog snapshot used to preserve the compatible Endpoint Catalog anchors for the bounded conjunction slice. Canonical JSON when present.  
* `audit/qa/hde-epic029/checks/po-001/route_snapshot.txt`: Optional CHECK po-001 plain-text route slice snapshot used to show the in-scope conjunction family in adapter routing. LF-terminated text when present.  
* `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.output.log`: Optional CHECK po-002 command output capture for the canonical JSON gate runner. UTF-8 text when present. It MAY be empty only when the underlying command produced no stdout/stderr and the approved step posture explicitly accepts an empty output log for that exact artifact.  
* `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.rc.txt`: Optional CHECK po-002 exit-code capture for the canonical JSON gate runner. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.output.log`: Optional CHECK po-003 command output capture for the conjunction writer evidence generator. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.rc.txt`: Optional CHECK po-003 exit-code capture for the conjunction writer evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.output.log`: Optional CHECK po-003 test output capture for the dev conjunction HTTP tests. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.rc.txt`: Optional CHECK po-003 exit-code capture for the dev conjunction HTTP tests. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-003/conjunction_write_readback.snapshot.log`: Optional CHECK po-003 writer readback snapshot used to preserve the reviewed dev writer readback surface. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-003/conjunction_writer_summary.snapshot.json`: Optional CHECK po-003 writer summary snapshot used to preserve the reviewed typed-envelope writer summary. Canonical JSON when present. Command-scoped output logs and exit-code captures under the canonical check directory are admissible current-state evidence when a Live QA plan names them as required deliverables. The rc capture remains authoritative for success or failure. If a required command-scoped output log would otherwise be zero-byte because the underlying command succeeded with no stdout/stderr, the preferred governed remedy is a one-line text sentinel that states that the command produced no stdout/stderr and names the authoritative rc artifact. Path-proofs and Machine Mirror records MUST reflect the committed sentinel bytes.  
* `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.output.log`: Optional CHECK po-004 test output capture for the dev sampler HTTP harness tests. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.rc.txt`: Optional CHECK po-004 exit-code capture for the dev sampler HTTP harness tests. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-004/dev_start_reader.snapshot.sh`: Optional CHECK po-004 start-helper snapshot used to preserve the governed script bytes reviewed by the step. UTF-8 shell text when present.  
* `audit/qa/hde-epic029/checks/po-004/dev_sampler_healthcheck.snapshot.py`: Optional CHECK po-004 healthcheck snapshot used to preserve the governed script bytes reviewed by the step. UTF-8 Python source text when present.  
* `audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt`: Optional CHECK po-005 commands snapshot used to preserve the OPS-01 command family copied into the canonical check directory. LF-terminated text when present.  
* `audit/qa/hde-epic029/checks/po-005/exit_codes.snapshot.txt`: Optional CHECK po-005 exit-code snapshot used to preserve the OPS-01 disposition family copied into the canonical check directory. LF-terminated text when present.  
* `audit/qa/hde-epic029/checks/po-005/codespaces_dev_sampler_url.snapshot.md`: Optional CHECK po-005 Codespaces URL snapshot used to preserve the published sampler binding value reviewed by the step. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-005/local_dev_sampler_url.snapshot.md`: Optional CHECK po-005 local-dev URL snapshot used to preserve the published sampler binding value reviewed by the step. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-005/binding_disposition.snapshot.md`: Optional CHECK po-005 binding-disposition snapshot used to preserve the reviewed closure posture copied from the OPS-01 family. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.output.log`: Optional CHECK po-006 output capture for the endpoint-catalog validation lane. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.rc.txt`: Optional CHECK po-006 exit-code capture for the endpoint-catalog validation lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-006/endpoints_catalog.snapshot.json`: Optional CHECK po-006 catalog snapshot used to preserve the current proof-boundary classification for the bounded transport-proof step. Canonical JSON when present. It MUST preserve /reader as the formal A7 success surface and MUST NOT promote dev or internal surfaces into the formal proof family.  
* `audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log`: Optional CHECK po-007 combined functional-bundle output capture for the bounded sampler, dev conjunction, and endpoint-catalog pytest lane. UTF-8 text when present. When the accepted step posture records a dependency preflight in the same governed log, that preflight output MAY precede the bundle output in this file.  
* `audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt`: Optional CHECK po-007 exit-code capture for the combined functional-bundle lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic029/checks/po-008/acceptance_map.snapshot.json`: Optional CHECK po-008 snapshot of docs/acceptance\_map\_epic029.json used to preserve the current bounded close-binding state for the step, including ready\_for\_close\_binding when present. Canonical JSON when present.  
* `audit/qa/hde-epic029/checks/po-008/token_evidence_matrix.snapshot.md`: Optional CHECK po-008 snapshot of audit/qa/hde-epic029/token\_evidence\_matrix.md used to preserve the current bounded token-to-evidence binding ledger for the step. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-008/acceptance_map_viability.snapshot.log`: Optional CHECK po-008 snapshot of audit/qa/hde-epic029/acceptance\_map\_viability.log used to preserve the current close-binding viability summary for the step, including the current COVERED and PLANNED and MISSING summary when present. LF-terminated text when present.  
* `audit/qa/hde-epic029/checks/po-008/qa_step_logs_manifest.snapshot.json`: Optional CHECK po-008 snapshot of audit/qa/hde-epic029/qa\_step\_logs\_manifest.json used to preserve the current canonical QA-step manifest view for the bounded closeout step. Canonical JSON when present.  
* `audit/qa/hde-epic029/checks/po-008/close_report.snapshot.md`: Optional CHECK po-008 snapshot of audit/EPIC-029\_close\_report.md used to preserve the bounded repo-side closeout posture reviewed by the step, including any closure-mode statement recorded in the reviewed close report. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic029/checks/po-008/close_manifest.snapshot.json`: Optional CHECK po-008 snapshot of audit/EPIC-029\_MANIFEST.json used to preserve the bounded close-pack manifest posture reviewed by the step, including any closeout-scope or closure-mode fields reviewed by the step. Canonical JSON when present.  
* `audit/qa/hde-epic029/checks/po-008/po_epic_close_live_qa.snapshot.log`: Optional CHECK po-008 QA bridge snapshot used to preserve the current epic-close Live QA log reviewed by the step. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-008/po_precommit.snapshot.log`: Optional CHECK po-008 QA bridge snapshot used to preserve the current precommit QA checklist log reviewed by the step. UTF-8 text when present.  
* `audit/qa/hde-epic029/checks/po-008/po_postcommit.snapshot.log`: Optional CHECK po-008 QA bridge snapshot used to preserve the current postcommit QA checklist log reviewed by the step. UTF-8 text when present. For EPIC029 CHECK po-008, the snapshot family above is admissible only as a bounded review copy of the current EPIC029 acceptance ledger and close-pack authoritative pair. It MUST NOT become a second authoritative home for those artifacts.

##### HDE-EPIC030 CHECK po-001 through po-005 check-local current-state outputs

* `audit/qa/hde-epic030/checks/po-001/surface_inventory.txt`: Optional CHECK po-001 surface-inventory proof used to record seeded route families and the no-public-widening result. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-001/exit_code.txt`: Optional CHECK po-001 exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-001/stderr.log`: Optional CHECK po-001 stderr capture. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic030/checks/po-002/pytest_stdout.log`: Optional CHECK po-002 pytest stdout capture for the zero-weight normalization and sampler-core test lane. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-002/generator_stdout.log`: Optional CHECK po-002 stdout capture for the PR-01 normalization evidence generator. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-002/generator_rc.txt`: Optional CHECK po-002 exit-code capture for the PR-01 normalization evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-002/exit_code.txt`: Optional CHECK po-002 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-003/preflight_stdout.log`: Optional CHECK po-003 preflight stdout capture for dependency and repo-locus readiness checks. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-003/pytest_stdout.log`: Optional CHECK po-003 pytest stdout capture for the viewer-preference normalization lane. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-003/generator_rc.txt`: Optional CHECK po-003 exit-code capture for the PR-01 normalization evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-004/preflight_stdout.log`: Optional CHECK po-004 preflight stdout capture for dependency and repo-locus readiness checks. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-004/pytest_stdout.log`: Optional CHECK po-004 pytest stdout capture for the dev sampler adapter and CLI test lane. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-004/generator_rc.txt`: Optional CHECK po-004 exit-code capture for the PR-02 sampler harness evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-005/preflight_stdout.log`: Optional CHECK po-005 preflight stdout capture for dependency and repo-locus readiness checks. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-005/pytest_stdout.log`: Optional CHECK po-005 pytest stdout capture for the compat AB/BA identity lane. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-005/generator_rc.txt`: Optional CHECK po-005 exit-code capture for the PR-03 compat evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-005/exit_code.txt`: Optional CHECK po-005 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF. CHECK po-002 through po-005 MAY reference the already governed PR-slice artifacts under audit/qa/hde-epic030/pr-01/, audit/qa/hde-epic030/pr-02/, and audit/qa/hde-epic030/pr-03/. Those PR-slice artifacts remain governed by their PR-slice evidence families and are not re-homed into the check-local directories by this ledger entry.

##### HDE-EPIC030 CHECK po-006 through po-012 check-local current-state outputs

* `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`: Optional CHECK po-006 numeric-free public compatibility proof. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json`: Optional CHECK po-006 OPS-02 evidence validator output. Canonical JSON when present.  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.stderr`: Optional CHECK po-006 OPS-02 evidence validator stderr capture. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation_rc.txt`: Optional CHECK po-006 OPS-02 evidence validator exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-006/pytest_rc.txt`: Optional CHECK po-006 pytest exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-006/grep_rc.txt`: Optional CHECK po-006 numeric-free grep exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-006/preflight_rc.txt`: Optional CHECK po-006 preflight exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-006/exit_code.txt`: Optional CHECK po-006 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF. CHECK po-006 MAY reference the already governed PR-05 category-framework artifact audit/qa/hde-epic030/pr-05/category\_framework\_binding.log and the already governed OPS-02 artifact audit/ops/hde-epic030/ops-02/ops02\_complete\_action\_log\_and\_evidence\_final.md. Those artifacts remain governed by their PR-slice and OPS evidence families and are not re-homed into the check-local directory by this ledger entry.  
* `audit/qa/hde-epic030/checks/po-007/threshold_ownership.txt`: Optional CHECK po-007 threshold-ownership proof used to record the current existing threshold source files and no-duplicate-threshold-home posture. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-007/generator_stdout.log`: Optional CHECK po-007 generator stdout capture. UTF-8 text when present. It MAY be empty only when the underlying command produced no stdout and the plan still requires the file.  
* `audit/qa/hde-epic030/checks/po-007/generator_stderr.log`: Optional CHECK po-007 generator stderr capture. UTF-8 text when present. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic030/checks/po-007/generator_rc.txt`: Optional CHECK po-007 generator exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-007/preflight.log`: Optional CHECK po-007 preflight log recording threshold source and generator/test presence. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-007/exit_code.txt`: Optional CHECK po-007 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF. CHECK po-007 MAY reference the already governed PR-04 artifact audit/qa/hde-epic030/pr-04/band\_edges\_binding.log; that artifact remains governed by the PR-04 evidence family.  
* `audit/qa/hde-epic030/checks/po-008/status_gate.log`: Optional CHECK po-008 status-gate log recording generator, pytest, artifact-presence, status, and final exit-code values. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-008/preflight.log`: Optional CHECK po-008 preflight log recording prerequisite discovery, generator, test-file, and pytest availability. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-008/pytest_stdout.log`: Optional CHECK po-008 pytest stdout capture for the PR-04 band-threshold evidence test. UTF-8 text when present. CHECK po-008 MAY reference the already governed PR-04 artifacts audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json and audit/qa/hde-epic030/pr-04/band\_thresholds\_identity\_hash.txt; those artifacts remain governed by the PR-04 evidence family. The stale planned path audit/qa/hde-epic030/pr-04/band\_thresholds\_identity.log is not the governed current-state identity artifact unless a later PF12 entry explicitly catalogs it.  
* `audit/qa/hde-epic030/checks/po-009/generator_rc.txt`: Optional CHECK po-009 generator exit-code capture for the PR-05 category-framework evidence generator. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-009/pytest_rc.txt`: Optional CHECK po-009 pytest exit-code capture for the category-framework binding lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-009/pytest_stdout.log`: Optional CHECK po-009 pytest stdout capture for the category-framework binding lane. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-009/exit_code.txt`: Optional CHECK po-009 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF. CHECK po-009 MAY reference the already governed PR-05 artifacts audit/qa/hde-epic030/pr-05/category\_framework\_binding.log, audit/qa/hde-epic030/pr-05/category\_canonical\_compare.log, and audit/qa/hde-epic030/pr-05/per\_channel\_mechanics.json; those artifacts remain governed by the PR-05 evidence family.  
* `audit/qa/hde-epic030/checks/po-010/fail_closed_visibility.txt`: Optional CHECK po-010 fail-closed visibility proof recording generated proof-family coverage and final PASS or blocked classification. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-010/pytest_rc.txt`: Optional CHECK po-010 pytest exit-code capture for the fail-closed suite. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-010/pytest_stdout.log`: Optional CHECK po-010 pytest stdout capture for the fail-closed suite. UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-010/exit_code.txt`: Optional CHECK po-010 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF. tests/evidence/test\_epic030\_pr01\_pr03\_fail\_closed\_evidence.py is test support for CHECK po-010. It is not a governed evidence artifact under this ledger unless later promoted and cataloged with a concrete artifact key, Human Index entry, Machine Mirror record, and path-proof discipline.  
* `audit/qa/hde-epic030/checks/po-011/traceability_summary.json`: Optional CHECK po-011 traceability summary proving required PR-slice artifacts are present, indexed, and mirrored. Canonical JSON when present.  
* `audit/qa/hde-epic030/checks/po-011/exit_code.txt`: Optional CHECK po-011 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-012/reused_history_classification.txt`: Optional CHECK po-012 reused-history classification proof separating reused history rows from active HDE-EPIC030 scope rows and preserving the no-new-implementation claim for reused-history rows. LF-terminated text when present.  
* `audit/qa/hde-epic030/00_meta/doc_deltas.md`: Optional HDE-EPIC030 Step-0B QA-root doc-delta copy used as a precondition artifact for later checks. If present, it MUST remain byte-identical to audit/docdeltas/hde-epic030\_doc\_deltas.md.  
* `audit/qa/hde-epic030/00_meta/step_0b_primary.log`: Optional HDE-EPIC030 Step-0B primary log recording the governed doc-delta capture precondition run. Non-empty UTF-8 text when present.  
* `audit/docdeltas/hde-epic030_doc_deltas.md`: Optional HDE-EPIC030 doc-delta ledger used by Step-0B and close-pack adjacency. Non-empty UTF-8 markdown when present unless the ledger explicitly records that it is empty. CHECK po-011 and po-012 MAY reference PR-slice artifacts and Step-0B precondition artifacts by path, but those referenced artifacts remain in their owning PR-slice, doc-delta, or QA-meta families and are not re-homed into the check-local directories by this ledger entry.

##### HDE-EPIC030 CHECK po-013 through po-017 check-local current-state outputs

* `audit/qa/hde-epic030/checks/po-013/primary.log`: Optional CHECK po-013 primary log for source-of-truth separation validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-013/source_of_truth_posture.txt`: Optional CHECK po-013 source-of-truth posture artifact. LF-terminated text when present. It SHOULD preserve the fixed posture fields for repo-supported completion, canon-drain completion, and formal close-pack completion, and it MUST NOT overclaim PF09.2 drainage or formal close-pack completion. CHECK po-013 MAY reference audit/qa/hde-epic030/00\_meta/doc\_deltas.md as a Step-0B precondition artifact. That referenced artifact remains governed by its QA-meta family and is not re-homed into the check-local directory by this ledger entry.  
* `audit/qa/hde-epic030/checks/po-014/primary.log`: Optional CHECK po-014 primary log for all-slice coherence validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-014/all_slice_coherence.json`: Optional CHECK po-014 all-slice coherence artifact proving prior primary logs, required PR-slice artifacts, and final coherence status. Canonical JSON when present.  
* `audit/qa/hde-epic030/checks/po-014/exit_code.txt`: Optional CHECK po-014 final step exit-code capture. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic030/checks/po-015/primary.log`: Optional CHECK po-015 primary log for baseline execution context, reachable surfaces, and tool-health posture. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-015/discovery.json`: Optional CHECK po-015 discovery artifact for rails, paths, and surfaces. Canonical JSON when present.  
* `audit/qa/hde-epic030/checks/po-015/discovery_validation.txt`: Optional CHECK po-015 discovery-validation artifact recording discovery parseability and required rails, paths, and surfaces checks. LF-terminated text when present.  
* `audit/qa/hde-epic030/checks/po-016/primary.log`: Optional CHECK po-016 primary log for final QA interpretation and evidence-backed meaning. Non-empty UTF-8 text when present. CHECK po-016 MAY reference audit/EPIC-030\_QA\_RCA.md as the governed QA RCA artifact. That artifact remains governed by the EPIC030 closeout and QA RCA family and is not re-homed into the check-local directory by this ledger entry.  
* `audit/qa/hde-epic030/checks/po-017/primary.log`: Optional CHECK po-017 primary log for documentation-drainage non-blocker posture. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic030/checks/po-017/documentation_drainage_posture.txt`: Optional CHECK po-017 documentation-drainage posture artifact. LF-terminated text when present. It SHOULD preserve that documentation drainage is not a blocker by itself while real truth-and-proof blocker classes remain explicit. CHECK po-013 through po-017 artifacts are check-level current-state evidence. They do not by themselves claim PF09.2 drainage, formal close-pack completion, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC031 Step-0A and Step-0B check-local current-state outputs

* `audit/qa/hde-epic031/00_meta/live_qa_harness.py`: Optional HDE-EPIC031 QA harness helper used by current-state QA checks. UTF-8 source text when present. It is QA harness evidence only and MUST NOT be treated as product behavior evidence by itself.  
* `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log`: Optional Step-0A primary log for discovery posture and harness setup. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json`: Optional Step-0A discovery artifact recording rails, paths, surfaces, and required seed-path presence. Canonical JSON when present.  
* `audit/docdeltas/hde-epic031_doc_deltas.md`: Optional HDE-EPIC031 doc-delta ledger used by Step-0B and close-pack adjacency. Non-empty UTF-8 markdown when present unless the ledger explicitly records that it is empty.  
* `audit/qa/hde-epic031/00_meta/doc_deltas.md`: Optional HDE-EPIC031 QA-root doc-delta copy used as a Step-0B precondition artifact for later checks. If present, it MUST remain byte-identical to audit/docdeltas/hde-epic031\_doc\_deltas.md unless a later PF12 entry explicitly permits divergence.  
* `audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log`: Optional Step-0B primary log recording the governed doc-delta capture precondition run. Non-empty UTF-8 text when present. audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json is the accepted current-state Step-0A discovery path for this ledger entry. The conflicting action-line reference to audit/qa/hde-epic031/00\_meta/discovery.json is not cataloged as a governed Step-0A deliverable by this entry unless a later PF12 entry explicitly promotes it.

##### HDE-EPIC031 CHECK po-001 through po-006 check-local current-state outputs

* `audit/qa/hde-epic031/checks/po-001/primary.log`: Optional CHECK po-001 primary log for Fermentation first-slice scope-boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-001/result.json`: Optional CHECK po-001 result artifact recording scope-boundary posture, no public-surface widening, and excluded later-scope work. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-002/primary.log`: Optional CHECK po-002 primary log for closed-by-default provider access and explicit bounded-opening validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-002/result.json`: Optional CHECK po-002 result artifact recording provider-test, closed-default refusal, bounded-opening, and no-live-vendor policy posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-003/primary.log`: Optional CHECK po-003 primary log for deterministic typed provider refusal when external access is not allowed. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-003/result.json`: Optional CHECK po-003 result artifact recording typed refusal markers, provider-test posture, and refusal-before-input or refusal-before-ingest ordering facts. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-004/primary.log`: Optional CHECK po-004 primary log for retry, backoff, and non-success classification validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-004/result.json`: Optional CHECK po-004 result artifact recording non-success classification, pinned-attempt, and retry-backoff evidence facts. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-005/primary.log`: Optional CHECK po-005 primary log for typed 429 and Retry-After parsing validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-005/result.json`: Optional CHECK po-005 result artifact recording Retry-After delta parsing, 429 source mapping, and typed 429 evidence facts. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-006/primary.log`: Optional CHECK po-006 primary log for keys-only redaction and observability validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-006/result.json`: Optional CHECK po-006 result artifact recording allowed-key presence, payload-body absence, plaintext-secret absence, raw-secret-header absence, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`: Optional Moon Loop remediation patch artifact for in-session QA harness remediation. UTF-8 diff text when present.  
* `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`: Optional Moon Loop changed-files artifact recording changed paths and sha256 values for in-session remediation. LF-terminated text when present. CHECK po-006 MAY reference audit/qa/hde-epic031/00\_meta/doc\_deltas.md for the recorded remediation note, but that artifact remains governed by the QA-meta doc-delta family and is not re-homed into the po-006 check directory by this ledger entry. CHECK po-001 through po-006 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09 drain, token-matrix completion, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC031 CHECK po-007 through po-018 check-local current-state outputs

* `audit/qa/hde-epic031/checks/po-007/primary.log`: Optional CHECK po-007 primary log for sensitive-provider-material absence and live-vendor-call prohibition validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-007/result.json`: Optional CHECK po-007 result artifact recording redaction-scan presence, scope-live-forbidden posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-008/primary.log`: Optional CHECK po-008 primary log for governed evidence coherence, hash-sentinel, validator-command, and PR-03 coherence validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-008/result.json`: Optional CHECK po-008 result artifact recording command-green posture, coherence status, and final PASS or failure posture. Canonical JSON when present. CHECK po-008 MAY reference audit/qa/hde-epic031/remediation/moon\_loop/patch.diff and audit/qa/hde-epic031/remediation/moon\_loop/changed\_files.txt for the auditable Moon Loop remediation stream, including changed coherence, index, mirror, path-proof, and compat artifacts. Those remediation artifacts remain governed by the HDE-EPIC031 remediation family and are not re-homed into the po-008 check directory by this ledger entry.  
* `audit/qa/hde-epic031/checks/po-009/primary.log`: Optional CHECK po-009 primary log for machine-mirror and evidence-family-map alignment validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-009/result.json`: Optional CHECK po-009 result artifact recording family-map presence, machine-mirror presence, mirror EPIC031 linkage, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-010/primary.log`: Optional CHECK po-010 primary log for generated-proof fail-closed posture validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-010/result.json`: Optional CHECK po-010 result artifact recording PR-01 generator check-mode presence, PR-02 and PR-03 generator-check posture, blocked-reason posture, and final PASS or failure posture. Canonical JSON when present. CHECK po-010 MAY reference check-mode validation labels such as PR-01 check-mode validation only as command or evidence labels. Non-path labels are not cataloged as governed artifacts by this entry unless a later PF12 entry supplies concrete repo-relative paths for them.  
* `audit/qa/hde-epic031/checks/po-011/primary.log`: Optional CHECK po-011 primary log for acceptance-claim boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-011/result.json`: Optional CHECK po-011 result artifact recording no claimed tokens, evidence-scope-limited claims, acceptance-map or token-matrix close-stage posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-012/primary.log`: Optional CHECK po-012 primary log for active Fermentation subtask supportability validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-012/result.json`: Optional CHECK po-012 result artifact recording HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4 supportability, PF09.5 drainage non-claim posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-013/primary.log`: Optional CHECK po-013 primary log for reused-foundation and active-scope classification validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-013/result.json`: Optional CHECK po-013 result artifact recording reused-foundation history-only classification, no new implementation claim for reused foundation, active-slice limitation posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-014/primary.log`: Optional CHECK po-014 primary log for prior-log presence and implementation-readiness interpretation validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-014/result.json`: Optional CHECK po-014 result artifact recording all-prior-logs-present posture, implementation-readiness not-final-QA-outcome posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-015/primary.log`: Optional CHECK po-015 primary log for implementation-readiness, QA-readiness, final-QA-outcome, and documentation-drainage truth-class separation validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-015/result.json`: Optional CHECK po-015 result artifact recording documentation-drainage separation, final-QA-outcome separation, PF09.5 drainage not-required-before-QA-PASS posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-016/primary.log`: Optional CHECK po-016 primary log for vendor-version runtime-conformance non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-016/result.json`: Optional CHECK po-016 result artifact recording vendor-version runtime conformance non-claim, no-live-vendor policy posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-017/primary.log`: Optional CHECK po-017 primary log for live-vendor-behavior non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-017/result.json`: Optional CHECK po-017 result artifact recording live-vendor-behavior non-claim, live-vendor-calls-forbidden posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic031/checks/po-018/primary.log`: Optional CHECK po-018 primary log for Live QA proof-only boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic031/checks/po-018/result.json`: Optional CHECK po-018 result artifact recording no implementation by Live QA, no remediation by Live QA, no closeout action by Live QA, Live QA proof-only role, and final PASS or failure posture. Canonical JSON when present. CHECK po-007 through po-018 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, vendor-version runtime conformance, live vendor behavior, formal close-pack completion, PO closeout, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC032 Step-0A and Step-0B check-local current-state outputs

* `audit/qa/hde-epic032/00_meta/live_qa_harness.py`: Optional HDE-EPIC032 QA harness helper used by current-state QA checks. UTF-8 source text when present. It is QA harness evidence only and MUST NOT be treated as product behavior evidence by itself.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`: Optional Step-0A primary log for discovery posture and Live QA harness setup. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log.path_proof.txt`: Optional Step-0A sibling path-proof transcript for the Step-0A primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`: Optional Step-0A result artifact recording QA-root creation, repo-locus discovery, discovery posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/remediation_provenance.md`: Optional Step-0A remediation provenance artifact for bounded Moon Loop correction of the QA-created harness. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic032/00_meta/delta/changed_files.txt`: Optional Step-0A Moon Loop changed-files ledger. LF-terminated text when present.  
* `audit/qa/hde-epic032/00_meta/delta/changed_files.sha256`: Optional Step-0A Moon Loop changed-files hash capture. LF-terminated text when present.  
* `audit/qa/hde-epic032/00_meta/delta/remediation_note.txt`: Optional Step-0A Moon Loop remediation note naming what changed and why. LF-terminated text when present.  
* `audit/qa/hde-epic032/00_meta/delta/failure_signature.txt`: Optional Step-0A Moon Loop failure-signature capture. LF-terminated text when present.  
* `audit/docdeltas/hde-epic032_doc_deltas.md`: Optional HDE-EPIC032 doc-delta ledger used by Step-0B and close-pack adjacency. Non-empty UTF-8 markdown when present unless the ledger explicitly records that it is empty.  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md`: Optional HDE-EPIC032 QA-root doc-delta copy used as a Step-0B precondition artifact for later checks. If present, it MUST remain byte-identical to audit/docdeltas/hde-epic032\_doc\_deltas.md unless a later PF12 entry explicitly permits divergence.  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`: Optional Step-0B primary log recording the governed doc-delta capture precondition run. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log.path_proof.txt`: Optional Step-0B sibling path-proof transcript for the Step-0B primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`: Optional Step-0B result artifact recording doc-delta surface creation, heading presence, and final PASS or failure posture. Canonical JSON when present.

##### HDE-EPIC032 CHECK po-001 through po-006 check-local current-state outputs

* `audit/qa/hde-epic032/checks/po-001/primary.log`: Optional CHECK po-001 primary log for Fermentation Pass 3 scope-boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-001/primary.log.path_proof.txt`: Optional CHECK po-001 sibling path-proof transcript for the po-001 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-001/result.json`: Optional CHECK po-001 result artifact recording Reader and dev Reader catalog surfaces, OPS-evidence non-conversion, DB proof-label non-token posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-002/primary.log`: Optional CHECK po-002 primary log for narrative-router deterministic key-selection validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-002/primary.log.path_proof.txt`: Optional CHECK po-002 sibling path-proof transcript for the po-002 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-002/result.json`: Optional CHECK po-002 result artifact recording router test posture, key-table evidence presence, AB and BA parity evidence presence, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-003/primary.log`: Optional CHECK po-003 primary log for keys-only router evidence and Reader non-expansion validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-003/primary.log.path_proof.txt`: Optional CHECK po-003 sibling path-proof transcript for the po-003 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-003/result.json`: Optional CHECK po-003 result artifact recording keys-only router evidence posture, no new Reader proof route posture, APP\_ENV gating visibility, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-004/primary.log`: Optional CHECK po-004 primary log for narrative-router identity validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-004/primary.log.path_proof.txt`: Optional CHECK po-004 sibling path-proof transcript for the po-004 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-004/result.json`: Optional CHECK po-004 result artifact recording router pytest return code, AB and BA identity-marker evidence, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-005/primary.log`: Optional CHECK po-005 primary log for registry diff and pack identity validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-005/primary.log.path_proof.txt`: Optional CHECK po-005 sibling path-proof transcript for the po-005 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-005/result.json`: Optional CHECK po-005 result artifact recording registry generator check posture, registry diff HDE-EPIC032 binding, pack identity posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-006/primary.log`: Optional CHECK po-006 primary log for registry non-overclaim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-006/primary.log.path_proof.txt`: Optional CHECK po-006 sibling path-proof transcript for the po-006 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-006/result.json`: Optional CHECK po-006 result artifact recording unsupported-registry-token absence, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json`: Optional HDE-EPIC032 QA step logs manifest for Step-0A, Step-0B, and CHECK po-001 through po-006 current-state evidence. Canonical JSON when present. It MUST record check IDs, statuses, primary-log paths, and primary-log path-proof paths when those fields are produced by the plan or harness.  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`: Optional sibling path-proof transcript for the HDE-EPIC032 QA step logs manifest when treated as governed QA evidence. CHECK po-001 through po-006 primary headers MAY record intended\_tokens and claimed\_tokens as empty arrays to preserve tokenless evidence posture. Empty token arrays are non-claim posture only and MUST NOT be treated as token satisfaction. CHECK po-004 MAY reference artifacts/narratives/router/parity\_abba.log; that artifact remains governed by the HDE-EPIC032 PR-01 narrative-router evidence family and is not re-homed into the check-local directory by this ledger entry. CHECK po-005 MAY reference audit/gates/narratives/registry.diff.json and audit/gates/narratives/pack\_identity.txt; those artifacts remain governed by the HDE-EPIC032 PR-02 narrative registry diff, Doc-Delta identity, and indexing evidence family and are not re-homed into the check-local directory by this ledger entry. CHECK po-006 MAY reference audit/gates/narratives/keys\_10x4.table.json; that artifact remains governed by the HDE-EPIC032 PR-01 narrative-router evidence family and is not re-homed into the check-local directory by this ledger entry. Step-0A, Step-0B, and CHECK po-001 through po-006 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, formal close-pack completion, PO closeout, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC032 CHECK po-007 through po-015 check-local current-state outputs

* `audit/qa/hde-epic032/checks/po-007/primary.log`: Optional CHECK po-007 primary log for registry and Doc-Delta identity validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-007/primary.log.path_proof.txt`: Optional CHECK po-007 sibling path-proof transcript for the po-007 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-007/result.json`: Optional CHECK po-007 result artifact recording registry-diff binding, Doc-Delta surface availability, no ungoverned Doc-Delta claim, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-008/primary.log`: Optional CHECK po-008 primary log for DB bridge and provider-parity proof-chain validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-008/primary.log.path_proof.txt`: Optional CHECK po-008 sibling path-proof transcript for the po-008 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-008/result.json`: Optional CHECK po-008 result artifact recording DB bridge parity generator check posture, provider-parity proof presence, adapter-selection evidence presence, OPS closure-status visibility, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-009/primary.log`: Optional CHECK po-009 primary log for OPS evidence non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-009/primary.log.path_proof.txt`: Optional CHECK po-009 sibling path-proof transcript for the po-009 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-009/result.json`: Optional CHECK po-009 result artifact recording OPS support-evidence visibility, OPS QA PASS non-claim posture, no standalone checklist-completion or epic-closure claim, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-010/primary.log`: Optional CHECK po-010 primary log for structural adapter-selection selection\_order validation after PR-routed remediation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-010/primary.log.path_proof.txt`: Optional CHECK po-010 sibling path-proof transcript for the po-010 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-010/result.json`: Optional CHECK po-010 result artifact recording structural selection\_order evidence, required-missing posture, behavior-failure posture, tokenless primary-header posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-011/primary.log`: Optional CHECK po-011 primary log for current-state evidence proof posture after PR-routed DB bridge remediation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-011/primary.log.path_proof.txt`: Optional CHECK po-011 sibling path-proof transcript for the po-011 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-011/result.json`: Optional CHECK po-011 result artifact recording required-missing posture, behavior-failure posture, tokenless primary-header posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-012/primary.log`: Optional CHECK po-012 primary log for DB bridge evidence regeneration and current-state evidence restoration. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-012/primary.log.path_proof.txt`: Optional CHECK po-012 sibling path-proof transcript for the po-012 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-012/result.json`: Optional CHECK po-012 result artifact recording governed DB bridge evidence regeneration posture, required-missing posture, behavior-failure posture, tokenless primary-header posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-013/primary.log`: Optional CHECK po-013 primary log for evidence-index coherence validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt`: Optional CHECK po-013 sibling path-proof transcript for the po-013 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-013/result.json`: Optional CHECK po-013 result artifact recording Human Evidence Index presence, Machine Evidence Mirror presence, command-check posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-014/primary.log`: Optional CHECK po-014 primary log for Human Index and Machine Mirror alignment validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt`: Optional CHECK po-014 sibling path-proof transcript for the po-014 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-014/result.json`: Optional CHECK po-014 result artifact recording Human/Machine evidence loci presence, command-check posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-015/primary.log`: Optional CHECK po-015 primary log for generated-proof fail-closed check validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt`: Optional CHECK po-015 sibling path-proof transcript for the po-015 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-015/result.json`: Optional CHECK po-015 result artifact recording generated-proof command-check posture, all-commands-green posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/remediation/moon_loop/patch.diff`: Optional remediation patch artifact for the QA evidence remediation package. UTF-8 diff text when present.  
* `audit/qa/hde-epic032/remediation/moon_loop/changed_files.txt`: Optional remediation changed-files ledger for the QA evidence remediation package. LF-terminated text when present.  
* `audit/qa/hde-epic032/remediation/moon_loop/boundary_classification.md`: Optional remediation boundary-classification artifact recording why a remediation path is QA-root evidence assembly, PR-routed remediation, or non-QA-root work. Non-empty UTF-8 markdown when present. For CHECK po-007 through po-015, audit/qa/hde-epic032/qa\_step\_logs\_manifest.json remains the current-state manifest and audit/qa/hde-epic032/qa\_step\_logs\_manifest.json.path\_proof.txt remains its sibling path-proof when the manifest is treated as governed QA evidence. CHECK po-007 MAY reference audit/gates/narratives/registry.diff.json, audit/gates/narratives/pack\_identity.txt, and audit/docdeltas/hde-epic032\_doc\_deltas.md; those artifacts remain governed by their narrative registry and Doc-Delta families and are not re-homed into the po-007 check directory by this ledger entry. CHECK po-008 and CHECK po-010 through po-012 MAY reference artifacts/db\_bridge/adapter\_selection.snapshot.json, artifacts/db\_bridge/provider\_parity.proof.json, and artifacts/runtime/env\_connectivity.snapshot.json; those artifacts remain governed by their DB bridge and runtime evidence families and are not re-homed into the check-local directories by this ledger entry. CHECK po-009 MAY reference audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json; that artifact remains governed by the OPS-01 DB provider parity closure evidence bundle and is not re-homed into the po-009 check directory by this ledger entry. CHECK po-013 through po-015 MAY reference docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, tools/evidence/generate\_narrative\_registry\_diff.py, and tools/evidence/generate\_db\_bridge\_parity.py as checked loci or command sources. Those referenced files are not re-homed into the check-local directories by this ledger entry. CHECK po-007 through po-015 primary headers MAY record intended\_tokens and claimed\_tokens as empty arrays to preserve tokenless evidence posture. Empty token arrays are non-claim posture only and MUST NOT be treated as token satisfaction. CHECK po-007 through po-015 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, formal close-pack completion, PO closeout, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC032 CHECK po-016 through po-024 check-local current-state outputs

* `audit/qa/hde-epic032/checks/po-016/primary.log`: Optional CHECK po-016 primary log for DB proof-label token-boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-016/primary.log.path_proof.txt`: Optional CHECK po-016 sibling path-proof transcript for the po-016 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-016/result.json`: Optional CHECK po-016 result artifact recording DB label token-overclaim posture, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-017/primary.log`: Optional CHECK po-017 primary log for bridge fallback scope-boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-017/primary.log.path_proof.txt`: Optional CHECK po-017 sibling path-proof transcript for the po-017 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-017/result.json`: Optional CHECK po-017 result artifact recording fallback-scope checking, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-018/primary.log`: Optional CHECK po-018 primary log for active evidence-family supportability and PF09.5 drainage non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-018/primary.log.path_proof.txt`: Optional CHECK po-018 sibling path-proof transcript for the po-018 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-018/result.json`: Optional CHECK po-018 result artifact recording active evidence-family presence, PF09.5 drainage non-claim posture, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-019/primary.log`: Optional CHECK po-019 primary log for reused-foundation and active implementation-scope validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-019/primary.log.path_proof.txt`: Optional CHECK po-019 sibling path-proof transcript for the po-019 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-019/result.json`: Optional CHECK po-019 result artifact recording reused-foundation repo-doc checking, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-020/primary.log`: Optional CHECK po-020 primary log for truth-class separation validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-020/primary.log.path_proof.txt`: Optional CHECK po-020 sibling path-proof transcript for the po-020 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-020/result.json`: Optional CHECK po-020 result artifact recording truth-class separation, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-021/primary.log`: Optional CHECK po-021 primary log for vendor-version runtime conformance non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-021/primary.log.path_proof.txt`: Optional CHECK po-021 sibling path-proof transcript for the po-021 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-021/result.json`: Optional CHECK po-021 result artifact recording vendor-version runtime conformance non-claim posture, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-022/primary.log`: Optional CHECK po-022 primary log for live-provider behavior non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-022/primary.log.path_proof.txt`: Optional CHECK po-022 sibling path-proof transcript for the po-022 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-022/result.json`: Optional CHECK po-022 result artifact recording live-provider behavior non-claim posture, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-023/primary.log`: Optional CHECK po-023 primary log for public Reader non-expansion validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-023/primary.log.path_proof.txt`: Optional CHECK po-023 sibling path-proof transcript for the po-023 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-023/result.json`: Optional CHECK po-023 result artifact recording Reader route visibility, invented proof-route absence, required-missing posture, behavior-failure posture, and final PASS or failure posture. Canonical JSON when present.  
* `audit/qa/hde-epic032/checks/po-024/primary.log`: Optional CHECK po-024 primary log for proof-only Live QA role-boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic032/checks/po-024/primary.log.path_proof.txt`: Optional CHECK po-024 sibling path-proof transcript for the po-024 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic032/checks/po-024/result.json`: Optional CHECK po-024 result artifact recording Live QA proof-only role, no implementation action, no PF edit, no closeout action, and final PASS or failure posture. Canonical JSON when present. For CHECK po-016 through po-024, audit/qa/hde-epic032/qa\_step\_logs\_manifest.json remains the current-state manifest and audit/qa/hde-epic032/qa\_step\_logs\_manifest.json.path\_proof.txt remains its sibling path-proof when the manifest is treated as governed QA evidence. CHECK po-016 through po-024 MAY reference already governed evidence loci such as artifacts/db\_bridge/provider\_parity.proof.json, docs/evidence/INDEX.json, audit/gates/narratives/keys\_10x4.table.json, and audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json. Those referenced artifacts remain governed by their owning evidence families and are not re-homed into the check-local directories by this ledger entry. CHECK po-016 through po-024 primary headers MAY record intended\_tokens and claimed\_tokens as empty arrays to preserve tokenless evidence posture. Empty token arrays are non-claim posture only and MUST NOT be treated as token satisfaction. CHECK po-016 through po-024 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, vendor-version runtime conformance, live vendor behavior, public Reader expansion, formal close-pack completion, PO closeout, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC033 Step-0B check-local current-state outputs

* `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log`: Optional Step-0B primary log for doc-delta capture validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`: Optional Step-0B sibling path-proof transcript for the Step-0B primary log when treated as governed QA evidence. Step-0B MAY reference audit/docdeltas/hde-epic033\_doc\_deltas.md, audit/docdeltas/hde-epic033\_doc\_deltas.md.path\_proof.txt, audit/qa/hde-epic033/00\_meta/doc\_deltas.md, and audit/qa/hde-epic033/00\_meta/doc\_deltas.md.path\_proof.txt. Those artifacts remain governed by the HDE-EPIC033 acceptance-ledger and doc-delta baseline families and are not re-homed into the Step-0B check directory by this ledger entry.

##### HDE-EPIC033 CHECK po-001 through po-003 check-local current-state outputs

* `audit/qa/hde-epic033/checks/po-001/primary.log`: Optional CHECK po-001 primary log for closed-rails source-inventory grounding validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-001/primary.log.path_proof.txt`: Optional CHECK po-001 sibling path-proof transcript for the po-001 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-002/primary.log`: Optional CHECK po-002 primary log for AI and LLM documentation-discovery boundary validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-002/primary.log.path_proof.txt`: Optional CHECK po-002 sibling path-proof transcript for the po-002 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-003/primary.log`: Optional CHECK po-003 primary log for v2 and legacy v1 route-validation evidence. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-003/primary.log.path_proof.txt`: Optional CHECK po-003 sibling path-proof transcript for the po-003 primary log when treated as governed QA evidence. CHECK po-001 through po-003 MAY reference already governed HDAPI v2 contract-inventory and source-cache artifacts, including artifacts/vendor/hdapi\_v2/source\_inventory.json, artifacts/vendor/hdapi\_v2/source\_inventory.md, artifacts/vendor/hdapi\_v2/source\_cache/v1-routes.yaml, artifacts/vendor/hdapi\_v2/source\_cache/v2-routes.yaml, artifacts/vendor/hdapi\_v2/source\_cache/source\_metadata.json, artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body, artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt, artifacts/vendor/hdapi\_v2/known\_anomalies.md, and artifacts/vendor/hdapi\_v2/openapi\_validation.log. Those artifacts remain governed by the HDAPI v2 vendor contract and adapter-conformance evidence family and are not re-homed into the check-local directories by this ledger entry. CHECK po-003 MAY reference tests/evidence/test\_hdapi\_v2\_contract\_inventory.py as a checked test locus. That test file is not re-homed into the po-003 check directory by this ledger entry.

##### HDE-EPIC033 CHECK po-004 through po-006 check-local current-state outputs

* `audit/qa/hde-epic033/checks/po-004/primary.log`: Optional CHECK po-004 primary log for suspect OpenAPI quarantine and validated route-spec posture. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-004/primary.log.path_proof.txt`: Optional CHECK po-004 sibling path-proof transcript for the po-004 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-005/primary.log`: Optional CHECK po-005 primary log for endpoint reference and contract-map validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-005/primary.log.path_proof.txt`: Optional CHECK po-005 sibling path-proof transcript for the po-005 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-006/primary.log`: Optional CHECK po-006 primary log for contract-map canonical JSON and non-conformance-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`: Optional CHECK po-006 sibling path-proof transcript for the po-006 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log`: Optional CHECK po-006 remediation-r3 primary log used when bounded Moon Loop remediation supersedes the original po-006 receipt. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log.path_proof.txt`: Optional CHECK po-006 remediation-r3 sibling path-proof transcript for the remediation-r3 primary log when treated as governed QA evidence. CHECK po-004 through po-006 MAY reference already governed HDAPI v2 contract-inventory artifacts, including artifacts/vendor/hdapi\_v2/openapi\_validation.log, artifacts/vendor/hdapi\_v2/known\_anomalies.md, artifacts/vendor/hdapi\_v2/endpoint\_reference.csv, and artifacts/vendor/hdapi\_v2/contract\_map.json. Those artifacts remain governed by the HDAPI v2 vendor contract and adapter-conformance evidence family and are not re-homed into the check-local directories by this ledger entry. CHECK po-006 remediation-r3 artifacts are QA-root remediation receipts only. They do not change the governed HDAPI v2 vendor contract artifact family unless separately cataloged payload artifacts outside the QA root are changed and indexed.

##### HDE-EPIC033 CHECK po-007 through po-009 check-local current-state outputs

* `audit/qa/hde-epic033/checks/po-007/primary.log`: Optional CHECK po-007 primary log for Human Evidence Index, Machine Evidence Mirror, hash, LF, and path-proof binding validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-007/primary.log.path_proof.txt`: Optional CHECK po-007 sibling path-proof transcript for the po-007 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-008/primary.log`: Optional CHECK po-008 primary log for baseline existing-token posture and no vendor-v2-specific acceptance-token minting. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-008/primary.log.path_proof.txt`: Optional CHECK po-008 sibling path-proof transcript for the po-008 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-009/primary.log`: Optional CHECK po-009 primary log for HDE-FERM006 supportability, no runtime v2 conformance claim, and no PF09.5 drainage overclaim. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-009/primary.log.path_proof.txt`: Optional CHECK po-009 sibling path-proof transcript for the po-009 primary log when treated as governed QA evidence. CHECK po-007 through po-009 MAY reference already governed index, mirror, acceptance-ledger, and token-matrix artifacts, including docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, artifacts/evidence\_index.jsonl.sha256, docs/evidence/INDEX.json.path\_proof.txt, docs/evidence/INDEX.sha256.path\_proof.txt, artifacts/evidence\_index.jsonl.path\_proof.txt, artifacts/evidence\_index.jsonl.sha256.path\_proof.txt, docs/acceptance\_map\_epic033.json, audit/qa/hde-epic033/token\_evidence\_matrix.md, and audit/qa/hde-epic033/acceptance\_map\_viability.log. Those artifacts remain governed by their owning evidence, mirror, and acceptance-ledger families and are not re-homed into the check-local directories by this ledger entry. CHECK po-001 through po-009 primary headers MAY record claimed\_tokens as empty or limited to the token posture supported by the governed artifact family under review. Empty token arrays are non-claim posture only and MUST NOT be treated as token satisfaction. Step-0B and CHECK po-001 through po-009 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, formal close-pack completion, PO closeout, runtime v2 conformance, open-rails vendor smoke completion, public Reader change, or epic closure unless a separately cataloged close-pack artifact binds that claim.

##### HDE-EPIC033 CHECK po-010 through po-012 check-local current-state outputs

* `audit/qa/hde-epic033/checks/po-010/primary.log`: Optional CHECK po-010 primary log for later adapter architecture, runtime request-shaping, live vendor smoke, and runtime v2 conformance non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt`: Optional CHECK po-010 sibling path-proof transcript for the po-010 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`: Optional CHECK po-010 accepted Moon Loop remediation receipt when a QA evidence-harness phrase-match defect supersedes the initial po-010 receipt. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt`: Optional CHECK po-010 remediation-r1 sibling path-proof transcript for the remediation-r1 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-011/primary.log`: Optional CHECK po-011 primary log for inventory-only runtime-conformance non-claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt`: Optional CHECK po-011 sibling path-proof transcript for the po-011 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-012/primary.log`: Optional CHECK po-012 primary log for no live vendor smoke, no public Reader change, no new HTTP home, and no AI runtime or evidence-scope expansion validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt`: Optional CHECK po-012 sibling path-proof transcript for the po-012 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`: Optional CHECK po-012 accepted Moon Loop remediation receipt when a QA evidence-harness phrase-match defect supersedes the initial po-012 receipt. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt`: Optional CHECK po-012 remediation-r1 sibling path-proof transcript for the remediation-r1 primary log when treated as governed QA evidence. CHECK po-010 and CHECK po-012 remediation-r1 artifacts are QA-root remediation receipts only. They do not change product code, repo tests, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multi-subsystem implementation surfaces. CHECK po-010 MAY reference artifacts/vendor/hdapi\_v2/known\_anomalies.md, artifacts/vendor/hdapi\_v2/contract\_map.json, and audit/qa/hde-epic033/acceptance\_map\_viability.log; those artifacts remain governed by their owning HDAPI v2 and acceptance-ledger families and are not re-homed into the po-010 check directory by this ledger entry. CHECK po-011 MAY reference artifacts/vendor/hdapi\_v2/source\_inventory.md, artifacts/vendor/hdapi\_v2/contract\_map.json, and audit/qa/hde-epic033/acceptance\_map\_viability.log; those artifacts remain governed by their owning HDAPI v2 and acceptance-ledger families and are not re-homed into the po-011 check directory by this ledger entry. CHECK po-012 MAY reference artifacts/vendor/hdapi\_v2/known\_anomalies.md, docs/acceptance\_map\_epic033.json, and audit/qa/hde-epic033/acceptance\_map\_viability.log; those artifacts remain governed by their owning HDAPI v2 and acceptance-ledger families and are not re-homed into the po-012 check directory by this ledger entry.

##### HDE-EPIC033 CHECK po-013 through po-014 and qa-16 closeout-deliverables check-local current-state outputs

* `audit/qa/hde-epic033/checks/po-013/primary.log`: Optional CHECK po-013 primary log for evidence-index and Machine Mirror proof validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-013/primary.log.path_proof.txt`: Optional CHECK po-013 sibling path-proof transcript for the po-013 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log`: Optional CHECK po-013 QA\_PLAN\_UPDATE routing receipt used when final PASS-grade proof relies on non-QA-root governed evidence refresh. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log.path_proof.txt`: Optional CHECK po-013 QA\_PLAN\_UPDATE routing sibling path-proof transcript for the routing receipt when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log`: Optional CHECK po-013 accepted R3 remediation proof receipt after QA\_PLAN\_UPDATE routing. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log.path_proof.txt`: Optional CHECK po-013 remediation-r3 sibling path-proof transcript for the remediation-r3 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/po-014/primary.log`: Optional CHECK po-014 primary log for baseline token, evidence-path, and no-runtime-conformance claim validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/po-014/primary.log.path_proof.txt`: Optional CHECK po-014 sibling path-proof transcript for the po-014 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log`: Optional qa-16 closeout-deliverables primary log for manifest, discovery artifact, QA RCA / Doc Delta summary, and non-PO-closeout posture validation. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt`: Optional qa-16 closeout-deliverables sibling path-proof transcript for the qa-16 primary log when treated as governed QA evidence.  
* `audit/qa/hde-epic033/qa_step_logs_manifest.json`: Optional HDE-EPIC033 QA step logs manifest produced or refreshed by qa-16 closeout-deliverables. Canonical JSON when present. It records expected checks, statuses, log paths, original planned receipts, accepted remediation receipts, and check coverage posture when those fields are produced by the plan or harness.  
* `audit/qa/hde-epic033/qa_step_logs_manifest.json.path_proof.txt`: Optional sibling path-proof transcript for the HDE-EPIC033 QA step logs manifest when treated as governed QA evidence.  
* `audit/qa/hde-epic033/00_meta/discovery_artifact.md`: Optional qa-16 discovery artifact for closeout-deliverables evidence. Non-empty UTF-8 markdown when present.  
* `audit/qa/hde-epic033/00_meta/discovery_artifact.md.path_proof.txt`: Optional sibling path-proof transcript for the qa-16 discovery artifact when treated as governed QA evidence.  
* `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md`: Optional qa-16 QA RCA / Doc Delta summary artifact. Non-empty UTF-8 markdown when present. It is closeout-support evidence only and does not by itself claim PO closeout, formal close-pack completion, PF09 drainage, or epic closure.  
* `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`: Optional sibling path-proof transcript for the qa-16 QA RCA / Doc Delta summary when treated as governed QA evidence. qa-16 MAY reference audit/qa/hde-epic033/checks/\*/primary.log for checks already executed as a plan-level inventory pattern only. Concrete primary logs remain governed by their check-specific entries. CHECK po-013 MAY reference already governed index, mirror, topology, and HDAPI v2 artifacts, including docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, audit/gates/topology/orientation\_demo.txt, and artifacts/vendor/hdapi\_v2/source\_inventory.json. Those artifacts remain governed by their owning evidence families and are not re-homed into the po-013 check directory by this ledger entry. CHECK po-014 MAY reference already governed acceptance-ledger, token-matrix, and HDAPI v2 artifacts, including docs/acceptance\_map\_epic033.json, audit/qa/hde-epic033/token\_evidence\_matrix.md, and artifacts/vendor/hdapi\_v2/source\_inventory.md. Those artifacts remain governed by their owning evidence families and are not re-homed into the po-014 check directory by this ledger entry. CHECK po-010 through po-014 and qa-16 primary headers MAY record claimed\_tokens as empty or limited to the token posture supported by the governed artifact family under review. Empty token arrays are non-claim posture only and MUST NOT be treated as token satisfaction. CHECK po-010 through po-014 and qa-16 artifacts are check-level current-state evidence. They do not by themselves claim close-pack production, Live QA completion beyond the named checks, PF09.5 drainage, token-matrix completion, formal close-pack completion, PO closeout, runtime v2 conformance, open-rails vendor smoke completion, public Reader change, new HTTP home, AI runtime or evidence scope, or epic closure unless a separately cataloged close-pack artifact binds that claim. Per-check dependency-preflight, activation/remediation, and ready/not-ready evidence MAY be carried in primary.log or in additional check-scoped command output and rc artifacts beneath the same canonical check directory. When separate artifacts are used, they are governed QA evidence under this ledger family and MUST NOT rely on per-run nesting as a correctness key.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_stdout.log`: Optional CHECK po-009 stdout capturefor a closed-rails lane. Produced only when that lane executes. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-009/catalog_surface_inventory.txt`: Optional CHECK po-009 plain-text catalog-surface inventory used to demonstrate that no unexpected public success surface appears in the current EPIC027 catalog family. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-009/token_inventory.txt`: Optional CHECK po-009 plain-text token inventory used to demonstrate that no non-canonical token names are introduced in the current EPIC027 token family. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_stderr.log`: Optional CHECK po-009 stderr capture for a closed-rails lane. Produced only when that lane executes. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_rc.txt`: Optional CHECK po-009 exit-code capture for a closed-rails lane. Produced only when that lane executes. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_classification.txt`: Optional CHECK po-009 text classification of the closed-rails outcome. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_stdout.log`: Optional CHECK po-009 stdout capture for an open-rails lane. Produced only when that lane executes. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_stderr.log`: Optional CHECK po-009 stderr capture for an open-rails lane. Produced only when that lane executes. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_rc.txt`: Optional CHECK po-009 exit-code capture for an open-rails lane. Produced only when that lane executes. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_ab_rc.txt`: Optional CHECK po-009 exit-code capture for the AB directional open-rails lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_ba_rc.txt`: Optional CHECK po-009 exit-code capture for the BA directional open-rails lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_ab_canonical_json_check.txt`: Optional CHECK po-009 text verification that the AB directional open-rails output satisfies canonical JSON checks. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_ba_canonical_json_check.txt`: Optional CHECK po-009 text verification that the BA directional open-rails output satisfies canonical JSON checks. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/abba_identity_check.txt`: Optional CHECK po-009 text verification that the AB and BA open-rails outputs satisfy the ABBA identity requirement. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_note.txt`: Optional CHECK po-009 blocking note used when the open-rails lane does not execute because required product inputs are unavailable. Non-empty UTF-8 text when present.  
* `audit/qa/<epic-id>/checks/po-009/po-009_input_constraint.log`: Optional CHECK po-009 text record explaining the input-availability constraint that blocked the planned lane. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/<check_id>/success_head.txt`: Optional per-check copy of artifacts/proofs/success\_head.txt (HTTP A7 proof snapshot). If present, it MUST be byte-identical to artifacts/proofs/success\_head.txt and MUST have a sibling success\_head.txt.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/success_get.txt`: Optional per-check copy of artifacts/proofs/success\_get.txt (HTTP A7 proof snapshot). If present, it MUST be byte-identical to artifacts/proofs/success\_get.txt and MUST have a sibling success\_get.txt.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/canonical_json_gate_stdout.txt`: Optional per-check stdout capture for a canonical-JSON gate runner. If present, it MUST have a sibling canonical\_json\_gate\_stdout.txt.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/env_pins.log`: Optional per-check copy of audit/gates/determinism/env\_pins.log. If present, it MUST be byte-identical to audit/gates/determinism/env\_pins.log and MUST have a sibling env\_pins.log.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/env_pins_check_stdout.txt`: Optional per-check stdout capture for an env pins check runner. If present, it MUST have a sibling env\_pins\_check\_stdout.txt.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/sanity_pipeline_stdout.txt`: Optional per-check stdout capture for ci/pipeline/run\_sanity\_pipeline.py. If present, it MUST have a sibling sanity\_pipeline\_stdout.txt.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/endpoints_catalog.json`: Optional per-check endpoint catalog snapshot used for the step’s validation. If present, it MUST have a sibling endpoints\_catalog.json.sha256.  
* `audit/qa/<epic-id>/checks/<check_id>/route_proof.txt`: Optional per-check plain-text route proof used to demonstrate route existence and gating. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-007/catalog_sha256_check.txt`: Optional CHECK po-007 text capture of a baseline-versus-current endpoint catalog hash comparison. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-007/catalog_extract_dev_endpoints.json`: Optional CHECK po-007 extracted dev-endpoints proof file used to verify the /dev/\*/conjunction endpoint set. Canonical JSON when present.  
* `audit/qa/hde-epic027/checks/po-007/update_evidence_index_write.txt`: Optional CHECK po-007 stdout capture for the evidence-index write lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/update_evidence_index_check.txt`: Optional CHECK po-007 stdout capture for the evidence-index check lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/orientation_demo_write.txt`: Optional CHECK po-007 stdout capture for the topology orientation-demo write lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/orientation_demo_check.txt`: Optional CHECK po-007 stdout capture for the topology orientation-demo check lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/validate_evidence_paths.txt`: Optional CHECK po-007 stdout capture for the evidence-path validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/check_lf_endings.txt`: Optional CHECK po-007 stdout capture for the final-LF validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/check_mirror_schema.txt`: Optional CHECK po-007 stdout capture for the mirror-schema validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-007/qa_step_manifest_lookup.txt`: Optional CHECK po-007 plain-text lookup proof used to demonstrate EPIC027 qa-step manifest coverage in the updater source and governed ledgers. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json`: Optional CHECK po-007 snapshot of docs/acceptance\_map\_epic028.json used to capture the current epic acceptance-map home for the step. Canonical JSON when present.  
* `audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt`: Optional CHECK po-007 plain-text snapshot of audit/qa/hde-epic028/token\_evidence\_matrix.md used to capture the current epic token-matrix home for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt`: Optional CHECK po-007 plain-text snapshot of audit/qa/hde-epic028/acceptance\_map\_viability.log used to capture the current epic viability home for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl`: Optional CHECK po-007 records-only JSONL snapshot of the current EPIC028 acceptance-binding rows from the Machine Evidence Mirror. Canonical JSONL when present.  
* `audit/qa/<epic-id>/checks/<check_id>/pytest_stdout.log`: Optional per-check stdout capture for a pytest lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/<check_id>/pytest_stderr.log`: Optional per-check stderr capture for a pytest lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/<check_id>/pytest_rc.txt`: Optional per-check exit-code capture for a pytest lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/<check_id>/catalog_api_compat_entry.json`: Optional per-check extracted compat-catalog proof file used to demonstrate /api/compat/v1 presence for that step. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-001/route_inventory.txt`: Optional CHECK po-001 plain-text route inventory proof used to demonstrate the dev conjunction trio and the related blueprint registration state. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-001/dev_conjunction_http.txt`: Optional CHECK po-001 pytest stdout capture for the dev conjunction HTTP validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-001/endpoint_catalog.txt`: Optional CHECK po-001 pytest stdout capture for the endpoint catalog validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt`: Optional CHECK po-001 plain-text source snapshot used to capture normalize\_pair and pair\_key loci for internal compat ordering. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt`: Optional CHECK po-001 plain-text source snapshot used to capture compat\_public ordering flow and pair-key use. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt`: Optional CHECK po-001 plain-text source snapshot used to capture canonical emitter loci used by the internal compat path. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-002/compat_surface.txt`: Optional CHECK po-002 plain-text compat surface proof used to demonstrate /api/compat/v1 mount posture and compat blueprint root behavior for that step. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-003/cli_emitter_proof.txt`: Optional CHECK po-003 plain-text emitter proof used to show shared emit\_public usage and the CLI LF or CRLF guard posture for that step. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-003/showcompat_parity.txt`: Optional CHECK po-003 pytest stdout capture for the showcompat parity and identity lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-003/showcompat_help.txt`: Optional CHECK po-003 stdout capture for hdctl showcompat \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.txt`: Optional CHECK po-003 stdout capture for hdctl \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt`: Optional CHECK po-003 stderr capture for hdctl \--help. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt`: Optional CHECK po-003 exit-code capture for hdctl \--help. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt`: Optional CHECK po-003 plain-text help-surface probe used to demonstrate that showcompat is present in the CLI help output. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt`: Optional CHECK po-003 snapshot of the governed emitter-symbol proof artifact. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt`: Optional CHECK po-003 snapshot of the governed serializer-grep guard artifact. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt`: Optional CHECK po-003 plain-text probe used to demonstrate that the governed Reader↔CLI parity bytes artifact exists and is non-zero for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-004/success_encoding_invariance_snapshot.txt`: Optional CHECK po-004 plain-text snapshot of artifacts/proofs/success\_encoding\_invariance.txt used to verify the preserved encoding-invariance proof surface for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.txt`: Optional CHECK po-003 stdout capture for hdctl \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt`: Optional CHECK po-003 stderr capture for hdctl \--help. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt`: Optional CHECK po-003 exit-code capture for hdctl \--help. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt`: Optional CHECK po-003 plain-text help-surface probe used to demonstrate that showcompat is present in the CLI help output. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt`: Optional CHECK po-003 snapshot of the governed emitter-symbol proof artifact. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt`: Optional CHECK po-003 snapshot of the governed serializer-grep guard artifact. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt`: Optional CHECK po-003 plain-text probe used to demonstrate that the governed Reader↔CLI parity bytes artifact exists and is non-zero for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-004/success_encoding_invariance_snapshot.txt`: Optional CHECK po-004 plain-text snapshot of artifacts/proofs/success\_encoding\_invariance.txt used to verify the preserved encoding-invariance proof surface for the step. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-004/entrypoint_proof.txt`: Optional CHECK po-004 plain-text entrypoint proof used to demonstrate explicit pyproject console binding for that step. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-004/cli_install_help.txt`: Optional CHECK po-004 pytest stdout capture for the CLI install-help validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-004/bg_resolve_test.txt`: Optional CHECK po-004 pytest stdout capture for the bg-resolve validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt`: Optional CHECK po-005 plain-text catalog snapshot used to identify the current governed Reader success-proof surface for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt`: Optional CHECK po-005 plain-text source snapshot of adapter/http\_reader.py used to demonstrate Reader route ownership and co-located surface classification for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-005/blocked_note.txt`: Optional CHECK po-005 plain-text context note preserving blocked-branch or lookup-note reasoning for the step. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-005/catalog_routes.txt`: Optional CHECK po-005 plain-text catalog route inventory proof used to show /reader A7 eligibility and /internal/version non-A7 posture for that step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt`: Optional CHECK po-006 plain-text imported lookup artifact used to carry the decisive PO-005 governed proof-surface resolution into the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-006/blocked_note.txt`: Optional CHECK po-006 plain-text branch note or blocked-reason note recording the resolved or blocked lane for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-005/context_note_pre_po010_moonloop.txt`: Optional immutable context-note capture used to preserve historical PO-005 blocked-note or lookup-note text when a bounded PO-010 Moon Loop remediation re-homes that text out of the current-state trigger filename. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-006/context_note_pre_po010_moonloop.txt`: Optional immutable context-note capture used to preserve historical PO-006 blocked-note or branch-note text when a bounded PO-010 Moon Loop remediation re-homes that text out of the current-state trigger filename. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-006/dev_conjunction_http.txt`: Optional CHECK po-006 pytest stdout capture for the dev conjunction HTTP validation lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-006/writer_index_rows.txt`: Optional CHECK po-006 plain-text mirror row proof used to show discoverability of conjunction.writer.summary and conjunction.writer.write\_readback for that step. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-008/generate_close_pack.txt`: Optional CHECK po-008 stdout capture for the EPIC027 close-pack generator lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic027/checks/po-008/close_pack_bindings.txt`: Optional CHECK po-008 plain-text binding proof used to demonstrate that close-pack bindings point to the EPIC027 QA root and current canonical ledger files. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-008/qa_step_manifest_lookup.txt`: Optional CHECK po-008 plain-text lookup proof used to demonstrate that the EPIC027 qa-step manifest is ledger-bound and not merely present on disk. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-008/cli_help.txt`: Optional CHECK po-008 stdout capture for hdctl \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-008/showcompat_help.txt`: Optional CHECK po-008 stdout capture for hdctl showcompat \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-008/reject_nonjson_stdout.log`: Optional CHECK po-008 stdout capture for a non-JSON conjunction-modifier rejection lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-008/reject_nonjson_stderr.log`: Optional CHECK po-008 stderr capture for a non-JSON conjunction-modifier rejection lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-008/reject_nonjson_rc.txt`: Optional CHECK po-008 exit-code capture for a non-JSON conjunction-modifier rejection lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/<check_id>/cli_ab.json`: Optional per-check directional D2-lane capture (AB ordering). Canonical JSON when present and only produced if that conditional lane executes.  
* `audit/qa/<epic-id>/checks/<check_id>/cli_ba.json`: Optional per-check directional D2-lane capture (BA ordering). Canonical JSON when present and only produced if that conditional lane executes.  
* `audit/qa/<epic-id>/checks/po-008/concat_output.json`: Optional CHECK po-008 conjunction output artifact produced only when the run provides both USER\_A\_ID and USER\_B\_ID. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-008/concat_output_order_check.txt`: Optional CHECK po-008 text verification of conjunction output order; produced only when concat\_output.json is produced.  
* `audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt`: Optional CHECK po-008 plain-text inventory of the authoritative audit/gates/json\_gate/canonical family captured before the canonical gate writer runs. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt`: Optional CHECK po-008 plain-text inventory of the supplemental audit/gates/canonical\_json family captured before the canonical gate writer runs. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log`: Optional CHECK po-008 stdout capture for the canonical gate-writer lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log`: Optional CHECK po-008 stderr capture for the canonical gate-writer lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt`: Optional CHECK po-008 exit-code capture for the canonical gate-writer lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt`: Optional CHECK po-008 plain-text inventory of the authoritative audit/gates/json\_gate/canonical family captured after the canonical gate writer runs. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt`: Optional CHECK po-008 plain-text inventory of the supplemental audit/gates/canonical\_json family captured after the canonical gate writer runs. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_stdout.log`: Optional CHECK po-009 stdout capture for a closed-rails lane. Produced only when that lane executes. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_stderr.log`: Optional CHECK po-009 stderr capture for a closed-rails lane. Produced only when that lane executes. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-009/closed_rails_rc.txt`: Optional CHECK po-009 exit-code capture for a closed-rails lane. Produced only when that lane executes. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_stdout.log`: Optional CHECK po-009 stdout capture for an open-rails lane. Produced only when that lane executes. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_stderr.log`: Optional CHECK po-009 stderr capture for an open-rails lane. Produced only when that lane executes. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_rc.txt`: Optional CHECK po-009 exit-code capture for an open-rails lane. Produced only when that lane executes. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-009/open_rails_note.txt`: Optional CHECK po-009 blocking note used when the open-rails lane does not execute because required product inputs are unavailable. Non-empty UTF-8 text when present.  
* `audit/qa/<epic-id>/checks/po-009/po-009_input_constraint.log`: Optional CHECK po-009 text record explaining the input-availability constraint that blocked the planned lane. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stdout.log`: Optional CHECK po-009 stdout capture for the evidence-index refresh lane. If present, it MUST be UTF-8 text.  
* `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stderr.log`: Optional CHECK po-009 stderr capture for the evidence-index refresh lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/hde-epic028/checks/po-009/update_evidence_index.rc.txt`: Optional CHECK po-009 exit-code capture for the evidence-index refresh lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/hde-epic028/checks/po-009/index_snapshot.json`: Optional CHECK po-009 snapshot of docs/evidence/INDEX.json used to capture the current human-ledger body for the step. Canonical JSON when present.  
* `audit/qa/hde-epic028/checks/po-009/index_sha_snapshot.txt`: Optional CHECK po-009 plain-text snapshot of docs/evidence/INDEX.sha256 used to capture the current human-ledger hash sentinel for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-009/mirror_path_proof_snapshot.txt`: Optional CHECK po-009 plain-text snapshot of artifacts/evidence\_index.jsonl.path\_proof.txt used to capture the current machine-ledger companion proof for the step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-009/manifest_updater_lookup.txt`: Optional CHECK po-009 plain-text lookup proof used to show that audit/qa/hde-epic028/qa\_step\_logs\_manifest.json is referenced by the evidence-index updater source. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-009/manifest_human_index_lookup.txt`: Optional CHECK po-009 plain-text lookup proof used to show that audit/qa/hde-epic028/qa\_step\_logs\_manifest.json is discoverable in docs/evidence/INDEX.json. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-009/manifest_mirror_lookup.txt`: Optional CHECK po-009 plain-text lookup proof used to show that audit/qa/hde-epic028/qa\_step\_logs\_manifest.json is discoverable in artifacts/evidence\_index.jsonl. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt`: Optional CHECK po-010 plain-text runtime-log presence proof used to show that no prerequisite same-run runtime logs are missing for that step. LF-terminated text when present.  
* `audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt`: Optional CHECK po-010 plain-text runtime-surface inventory used to demonstrate same-run execution across the required runtime proof families for that step. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/po-010/final_summary.txt`: Optional CHECK po-010 repo-supported completion summary. When present, it MUST explicitly distinguish recorded, blocked, and no-claim step outcomes and MUST NOT over-claim canon drain or formal close-pack completion for the run. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-010/showcompat_help.txt`: Optional CHECK po-010 stdout capture for hdctl showcompat \--help. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-010/catalog_extract_dev_endpoints.json`: Optional CHECK po-010 extracted dev-endpoints proof file used to verify conjunction endpoint presence under the dev scope. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-011/canonical_json_gate_stdout.log`: Optional CHECK po-011 stdout capture for a canonical JSON gate lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-011/canonical_json_gate_stderr.log`: Optional CHECK po-011 stderr capture for a canonical JSON gate lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-011/canonical_json_gate_rc.txt`: Optional CHECK po-011 exit-code capture for a canonical JSON gate lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-011/update_evidence_index_stdout.log`: Optional CHECK po-011 stdout capture for an evidence-index update lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-011/update_evidence_index_stderr.log`: Optional CHECK po-011 stderr capture for an evidence-index update lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-011/update_evidence_index_rc.txt`: Optional CHECK po-011 exit-code capture for an evidence-index update lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-011/check_evidence_bindings_stdout.log`: Optional CHECK po-011 stdout capture for tools/evidence/check\_evidence\_bindings.py \--strict when that auxiliary lane is executed. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-011/check_evidence_bindings_stderr.log`: Optional CHECK po-011 stderr capture for tools/evidence/check\_evidence\_bindings.py \--strict when that auxiliary lane is executed. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-011/check_evidence_bindings_rc.txt`: Optional CHECK po-011 exit-code capture for tools/evidence/check\_evidence\_bindings.py \--strict when that auxiliary lane is executed. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-012/generator_stdout.log`: Optional CHECK po-012 stdout capture for the close-pack generator lane. If present, it MUST be UTF-8 text.  
* `audit/qa/<epic-id>/checks/po-012/generator_stderr.log`: Optional CHECK po-012 stderr capture for the close-pack generator lane. It MAY be empty only when the underlying command produced no stderr and the plan still requires the file.  
* `audit/qa/<epic-id>/checks/po-012/generator_rc.txt`: Optional CHECK po-012 exit-code capture for the close-pack generator lane. If present, it MUST contain only the final integer exit code plus trailing LF.  
* `audit/qa/<epic-id>/checks/po-012/close_pack_copy/epic-026_manifest.json`: Optional CHECK po-012 copied close-pack manifest used for generator verification. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-012/close_pack_copy/epic-026_evidence_index.json`: Optional CHECK po-012 copied evidence-index snapshot used for generator verification. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-012/close_pack_copy/endpoints_catalog.json`: Optional CHECK po-012 copied endpoint catalog snapshot used for generator verification. Canonical JSON when present.  
* `audit/qa/<epic-id>/checks/po-012/close_pack_copy/endpoints_catalog.json.sha256`: Optional CHECK po-012 copied checksum sidecar for close\_pack\_copy/endpoints\_catalog.json. LF-terminated text when present.  
* `audit/qa/<epic-id>/checks/po-000/doc_deltas.md`: Optional step-0, check-scoped doc-delta capture for the run. Non-empty UTF-8 markdown.  
* `audit/qa/<epic-id>/checks/po-000/qa_helpers.sh`: Optional step-0, check-scoped helper copy created or pinned by the plan/run. If a plan uses this file, it MUST be treated as a run-local helper surface, not as a pre-existing repo-resident source outside the run.  
* `audit/qa/hde-epic028/checks/d0/runtime_context.txt`: Optional D0 runtime-context snapshot recording the effective rails and runtime context for the run. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/d0/cli_health.txt`: Optional D0 CLI-health baseline recording the initial CLI-help return code and stdout/stderr line counts for the run. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/d0/services_surfaces.txt`: Optional D0 services/surfaces baseline recording the expected compat, Reader, internal, and dev surfaces for the run. LF-terminated text when present.  
* `audit/qa/hde-epic028/checks/d0/d0_exact_commands.sh`: Optional D0 executed shell-script capture used when the bootstrap commands are consolidated into one explicit runtime sequence. If present, it MUST be treated as a run-local helper surface, not as a pre-existing repo-resident source outside the run.

##### Optional ledger artifacts (non-required for closure; current-state if present)

* `audit/qa/<epic-id>/topology/topology_conjunction_demo.json`: Optional, per-epic topology demo output. If present, audit/qa//topology/README.md may accompany the JSON to describe the scenario and expected interpretation.  
* `audit/qa/<epic-id>/acceptance_map_viability.log`: Per-epic text log summarizing acceptance-map viability results for the current-state (and optionally noting any retained history). Produced mechanically by the epic QA harness entrypoint (titles-only). LF-terminated text.  
* `audit/qa/<epic-id>/epic_closure_record.md`: Optional per-epic closure record (non-empty UTF-8 markdown). If present, it MUST have a sibling epic\_closure\_record.md.sha256. Deferred and Not Run listing constraint (normative). If epic\_closure\_record.md is present and it lists any checks as Deferred or Not Run for the current run, it MUST NOT present those checks’ artifact paths (including primary.log paths) as required primary evidence paths for the current run. Deferred or Not Run artifacts MAY be listed only under an explicitly labeled Deferred or Not Run section and MUST be clearly marked non-binding.  
* `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`: Optional Step-0 Codespaces environment snapshot (tool versions, rails pins, presence-only env context). Canonical JSON; schema and indexing posture are defined in §8.17.5. Live QA Plans MUST NOT require this artifact for closure by default.  
* `audit/qa/hde-epic028/00_meta/delta/patch.diff`: Optional Step-0B patch capture for a bounded Moon Loop remediation or equivalent controlled delta repair within the stable EPIC028 QA root. Non-empty UTF-8 text when present.  
* `audit/qa/hde-epic028/00_meta/delta/changed_files.txt`: Optional Step-0B changed-files ledger paired with audit/qa/hde-epic028/00\_meta/delta/patch.diff. LF-terminated text when present.  
* `audit/qa/<epic-id>/00_meta/deferred_scope_posture.md`: Optional per-epic deferred scope posture record (non-empty UTF-8 markdown).  
* `audit/qa/<epic-id>/checks/<check_id>/deferred_scope_posture.md.sha256`: Optional integrity proof for audit/qa//00\_meta/deferred\_scope\_posture.md produced by the check that generated the posture record.  
* `audit/docdeltas/<epic-id>_doc_deltas.md`: Mechanically produced doc delta draft/capture (names-only; no secrets). If no deltas exist, the artifact MUST explicitly say so (produced output, not an instruction). This artifact may be referenced by QA ledger artifacts and or close-pack key\_outputs pointers, but it is not required to live under the epic QA root.  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`: Optional EPIC029 bounded conjunction JSON surface inventory. Non-empty UTF-8 markdown when present. It records the bounded conjunction JSON surface family and the emit\_public \-\> sercanon single-emitter verification for each included locus. The required bounded minimum loci for this artifact are /reader, /dev/writer/conjunction, and /internal/dev/sampler. Additional same-family loci MAY be listed only when they remain inside the same bounded conjunction JSON family and do not widen the proof surface, for example /dev/reader/conjunction and /dev/sampler/conjunction.  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`: Optional EPIC029 dev-harness binding coverage artifact. Non-empty UTF-8 markdown when present. It records the closure-support binding posture for the EPIC029 dev-harness family and MUST preserve any accepted environment state that remains not yet closed while separately recording QA-log coverage as present and bound.

##### Per-run retention and appendix copies (non-canonical; not binding)

Retained copies under run-scoped or appendix-only paths MUST NOT be introduced or required for Live QA evidence. run\_id (or RUN\_ID) MUST NOT be used as an operator input, a step-log header field, a governed manifest field, a correctness key, or an evidence-root selector. If historical or earlier-attempt materials are kept outside the canonical audit/qa check directories for audit visibility, they are non-canonical. They MUST NOT be plan-required deliverables, MUST NOT be used for manifest keying or PASS/FAIL binding, and MUST NOT be indexed or mirrored unless a later canon change explicitly promotes them.

##### Indexing discipline (governed artifacts)

Indexing follows the standard §8.6 rule set: exactly one Human Evidence Index entry per concrete file path, exactly one Machine Evidence Mirror record per concrete file path, and exactly one governed path-proof transcript per concrete file path, kept in lockstep. Acceptance hints (titles-only; evidence is via per-check primary.log under the epic QA root). EVIDENCE\_INDEX\_UPDATED\_OK EVIDENCE\_INDEX\_HASH\_OK EVIDENCE\_INDEX\_MIRROR\_OK EVIDENCE\_PATHS\_VALIDATED\_OK CI\_CHECK\_MIRROR\_SCHEMA\_OK CI\_CHECK\_FINAL\_LF\_OK JSON\_CANONICAL\_CHECK\_OK

#### 8.6.3.13 Epic token/evidence matrix

These entries register per-epic Token/Evidence Matrix artifacts as governed members of the Evidence Catalog. Each matrix provides a single, reviewable ledger mapping QA tokens to evidence and execution surfaces for one epic.

##### Family description

Each epic MAY define exactly one Token/Evidence Matrix artifact under its epic QA root. The matrix is current-state; it is updated in place as the epic’s closure posture evolves.

##### Path pattern (single home per epic; choose exactly one format per epic)

Markdown: audit/qa//token\_evidence\_matrix.md JSON: audit/qa//token\_evidence\_matrix.json JSONL: audit/qa//token\_evidence\_matrix.jsonl is the canonical epic identifier used in §8.17 (lower-case ASCII, hyphenated; for example hde-epic021). If a semantic epic identifier differs (for example HDE-EPIC021), it MAY be recorded in Machine Mirror metadata via epic\_id (see §8.3 allowed metadata keys). The matrix is a textual artifact (Markdown or JSON or JSONL) intended to be read by humans and QA agents; it must carry no secrets.

##### Row set (binding discipline; names-only)

Matrix rows are reserved for the set of QA tokens that this epic explicitly claims as in-scope. Tokens explicitly deferred or out of scope for this epic MUST NOT appear as matrix rows.

##### Minimum content (names-only)

For each token row in the matrix, the artifact MUST record at least: token\_name: the QA token’s canonical name, as defined in HDE-Governance and or Glow QA Guide or an approved doc delta (titles-only). owner\_pf: the PF document (and optionally section) that owns the token’s semantics (titles-only). evidence\_artifacts: one or more governed artifacts associated with the token (artifact\_keys and or discovered\_physical\_path entries), drawn from families listed in §8.6 and other PF12 sections. qa\_root\_logs: QA log paths under audit/qa// that demonstrate QA harness runs relevant to this token (current-state preferred; retained history optional). ci\_tests\_jobs: CI test modules and or jobs that enforce this token under closed rails (names only). Additional columns such as Status or Notes MAY be present for human use; their contents are not governed by PF12 beyond canonical text formatting and governed-path rules.

##### Canonical format

When the matrix is Markdown, it MUST remain plain UTF-8 text with LF line endings and no ANSI sequences. When JSON or JSONL is used instead of Markdown, canonical JSON rules from §4 apply (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted when treated as sets).

##### Indexing (titles/paths only)

Let MATRIX\_PATH be the chosen single-home Token/Evidence Matrix path for this epic (one of the three paths listed above). Human Evidence Index (docs/evidence/INDEX.json). For each epic that defines a Token/Evidence Matrix, there MUST be exactly one Index entry with artifact\_key set to a stable, epic-scoped key (for example epic021.token\_matrix) and discovered\_physical\_path pointing to MATRIX\_PATH. docs/evidence/INDEX.sha256 MUST be updated in the same change-set whenever a new epic matrix is added or its path changes. Machine Evidence Mirror (artifacts/evidence\_index.jsonl). Each epic Token/Evidence Matrix MUST have a corresponding Mirror record with artifact\_key equal to the key used in the Human Index entry, role: "snapshot", discovered\_physical\_path pointing to MATRIX\_PATH, and sha256, size\_bytes, produced\_at\_utc, and proof\_anchor matching the governed path-proof transcript for this artifact. If additional labeling is needed, use §8.3 metadata keys (for example epic\_id and record\_type:"token\_evidence\_matrix"). Unknown keys remain rejected. Exactly one Mirror record per epic is allowed for this family; additional QA tables or notes under the same directory are separate artifacts and MUST NOT reuse the same artifact\_key. Path-proofs. Each matrix artifact MUST have a sibling path-proof transcript (for example token\_evidence\_matrix.md.path\_proof.txt) that satisfies the path-proof schema in §8.3 and is referenced from the Mirror record via proof\_anchor.

##### Acceptance hints (names-only)

PF12 does not own token semantics. For epic Token/Evidence Matrices, PF12 binds the matrix family to existing QA tokens by name and path only. Epics and QA plans use the matrix as a ledger; PF12 governs only its existence, location, and indexing.

### 

### **8.6.4 Discipline reminder (current-state; unchanged)**

Every entry above must have:

* Exactly one Human Index entry in docs/evidence/INDEX.json.

* Exactly one Mirror record in artifacts/evidence\_index.jsonl.

* Exactly one governed path-proof transcript (\*.path\_proof.txt), referenced by proof\_anchor.

Mirror records must follow §8.3:

* Canonical JSONL

* Single mirror file

* Sorted field order and sorted records

* LF-terminated

* Unknown-key rejection

* proof\_anchor pointing to a stored path-proof transcript for the same artifact

### **8.6.5 Acceptance impact**

This section is a names-only catalog of governed artifact families and their paths. It does not introduce new acceptance tokens. Enforcement remains via existing mirror and index tokens (for example EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, CI\_CHECK\_MIRROR\_SCHEMA\_OK), plus the specific domain tokens referenced by Governance and QA.

## **8.7 DB fingerprint & smoke artifacts \[Required-Now\]**

Purpose. Capture database posture and minimal activity proofs as records-only governed evidence for EPIC-011 and future epics.

### **Artifacts (titles and paths only)**

* DB fingerprint — normalized DDL \+ sha256: `artifacts/db/ddl_fingerprint.json`

* Roles and grants snapshot: `artifacts/db/grants.txt`

* Schema/search\_path echo: `artifacts/db/check_schema.txt`

* Constraints check: `artifacts/db/check_constraints.txt`

* Partition plan (summary): `artifacts/db/partition_plan.txt`

* RW smoke (optional): `artifacts/db/db_rw_smoke.log`  
* Retained historical runtime-connectivity snapshot: `artifacts/runtime/env_connectivity.snapshot.json`  
* Env posture (names-only): `artifacts/runtime/env_matrix.snapshot.json`  
* Current direct-selection snapshot: `artifacts/runtime/direct_db_selection.snapshot.json`  
* Current direct-selection schema: `schemas/hde_epic038_direct_db_selection.v1.json`  
* Current direct read-only OPS packet: `audit/ops/hde-epic038/ops-03/`

### **Shared DDL identity projection**

`engine/db/ddl_identity_projection.py` is the sole shared implementation of `hde.ddl_identity_projection.v1`.

The included projection fields are exactly:

* `projection[].kind`  
* `projection[].name`  
* `projection[].columns[].name`  
* `projection[].columns[].type`

The explicitly unexamined fields are:

* `source[].columns[].nullable`  
* `source[].columns[].default`  
* `source[].constraints`  
* `source[kind=view].definition`

The projector accepts only `table` and `view`, rejects malformed or duplicate objects and columns, sorts objects by `(kind, name)`, sorts columns by `(name, type)`, and emits only the governed projection fields. Equality proves only `projection_match`; it MUST be accompanied by `full_ddl_semantic_parity_claimed: false` and MUST NOT be represented as full DDL semantic parity.

### **Current direct-only selection evidence**

The current family is `epic038.pr06r.direct_db_selection` at `artifacts/runtime/direct_db_selection.snapshot.json`, validated by `hde_epic038.direct_db_selection.v1` at `schemas/hde_epic038_direct_db_selection.v1.json`.

The primary contains exactly `schema`, `retired_keys`, `cases`, `predicates`, `result`, and `failure`. Its ordered cases are `healthy_direct`, `missing_database_url`, `unavailable_database_url`, and `retired_keys_present`. Its exact predicates are `direct_only_provider`, `missing_direct_fails_closed`, `unavailable_direct_fails_closed`, `retired_keys_fail_before_provider_attempt`, `alternate_transport_attempts_zero`, and `secret_values_absent`.

PASS requires every predicate and case invariant to hold. Missing or unavailable direct access fails closed. Retired bridge keys fail before provider construction or I/O. No alternate transport attempt is permitted.

### **OPS-03 direct read-only evidence**

The tracked success root is `audit/ops/hde-epic038/ops-03/`. It contains the ten primaries and uses the seven schemas registered in §8.6.3.4. The runner-owned primaries are produced by `scripts/ops/hde_epic038_ops03.py`; `tools/evidence/hde_epic038_ops03.py --emit-receipt` produces `validation_receipt.json`.

Failure receipts are diagnostic, non-admissible, and excluded from the success root. The tracked failure-receipt schema does not make a failure receipt a governed PASS primary.

`tools/evidence/update_evidence_index.py` alone creates sibling path proofs and refreshes Index, Mirror, checksum, sentinel, and orientation companions for the ten primaries and seven schemas.

### **Historical bridge evidence**

Bridge-era primaries remain preserved historical records. Current historical roots and loci include:

* `artifacts/db_bridge/**`  
* `artifacts/db/provider_parity/**`  
* `artifacts/runtime/env_connectivity.snapshot.json`  
* `artifacts/runtime/env_connectivity.nondev_failure.json`  
* bridge Presenter comparisons and schemas  
* `audit/ops/hde-epic038/ops-01/**`

Where bound by the current ledgers, these rows use record type `historical_bridge_evidence`. Their primary bytes, historical producer provenance, checksums, sibling path proofs, and Human/Machine ledger identities remain intact.

Historical bridge evidence MUST NOT be regenerated through retired transport or used to prove current service availability, runtime support, direct-versus-bridge parity, bridge consistency, bridge fallback, current OPS PASS, release admission, or token satisfaction. Accurate historical token fields remain historical only.

`audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` remains non-claiming OPS evidence under its current record identity; it is not a current bridge gate.

### **Indexing**

List every current direct-selection and OPS-03 artifact and every retained historical binding in `docs/evidence/INDEX.json`, and update `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl` coherently with the required sibling path proofs and checksums. The Machine Evidence Mirror remains canonical JSONL and follows §8.3.

Feature producers MUST NOT write Index, Mirror, path-proof, checksum, sentinel, or orientation companions. Those companions remain owned by `tools/evidence/update_evidence_index.py`.

### **Primary key posture (current EPIC-011 reality)**

The canonical fingerprint schema for EPIC-011 includes a primary\_key array and constraints list for each table. In the current captured posture for hde.body\_graphs, both primary\_key and constraints are empty; this accurately reflects the production database at the time of capture (no primary key is defined on hde.body\_graphs).

For EPIC-011, tokens such as DB\_SCHEMA\_FINGERPRINT\_OK and DB\_ROLE\_OK are defined as “posture is captured and indexed as-is,” so this no-PK state is sufficient for those tokens once fingerprint, grants, mirror, and path-proofs are in sync.

The missing PK on hde.body\_graphs is recorded technical debt: a future DB/infra migration epic must introduce and enforce an appropriate primary key on (user\_id, vendor, vendor\_version, input\_fingerprint), re-capture ddl\_fingerprint.json and grants.txt, and update PF12 and PF10 accordingly. Until that epic lands, PF12’s role is to document the current posture truthfully, not to prescribe the eventual PK.

Acceptance (titles-only; tokens live in HDE-Governance). DB\_SCHEMA\_FINGERPRINT\_OK, DB\_ROLE\_OK, DB\_RUNTIME\_SEARCH\_PATH\_OK, DB\_CONN\_ENV\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK. Historical bridge labels and stored historical token occurrences create no current acceptance claim. OPS-03 creates no acceptance token by implication.

## **8.8 Reader JSON Success Endpoint Catalog snapshot (records-only)**

Purpose. Support Governance proofs for success routes (A7) beyond /internal/version. A7 proofs run only on cataloged JSON success routes; /internal/version is ops-only and excluded. The Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod (pair with an env-gate proof artifact).

Path. `artifacts/reader/endpoints_snapshot.json` (fixed).

Content (titles only). Canonical JSON snapshot that lists success endpoints by title and the names of response envelope keys. No URLs, no example payloads, no bytes beyond names.

Format. Records-only, canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF). An empty endpoints array is allowed until a route ships.

Suggested minimal schema (example).

* {"generated\_at\_utc":"YYYY-MM-DDThh:mm:ssZ","endpoints":\["\<title-1\>","\<title-2\>"\],"envelope\_keys":\["reader\_version","eligible","categories","meta","release\_id","idempotence\_hash"\]}

Related governed files (titles only). The authoritative Catalog file lives at `docs/ENDPOINTS_CATALOG.json` with checksum sidecar `docs/ENDPOINTS_CATALOG.json.sha256` and MUST be indexed like other records-only artifacts (see §8.6, Appendix C).

### **Authoritative Endpoint Catalog file (records-only; names-only fields)**

The authoritative Catalog file lives at:

* `docs/ENDPOINTS_CATALOG.json` (records-only; canonical JSON)  
* docs/ENDPOINTS\_CATALOG.json.sha256 (checksum sidecar; sha256sum \-c compatible; MUST reference docs/ENDPOINTS\_CATALOG.json)  
* docs/ENDPOINTS\_CATALOG.json.path\_proof.txt (path proof transcript for the catalog file)

Checksum verification expectation. `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256` MUST succeed when run from repo root.

Some workflows also emit an audit copy of the catalog under `artifacts/audit/ENDPOINTS_CATALOG.json`.

Audit mirror checksum sidecar (names-only; governed when present).

* If `artifacts/audit/ENDPOINTS_CATALOG.json` exists, a checksum sidecar MUST exist at `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`.

* When the endpoint catalog bytes change, regenerate `docs/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.path_proof.txt`, `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`, and (when present) `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`.

This Catalog is a machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints) used to support QA, audits, and transport reasoning. It contains names-only metadata and MUST NOT embed secrets or example payload bytes.

Reader surface canonical routes (normative).

Canonical Reader route: GET /reader. Reader v1 is selected via query parameter v=1 on this route (the route path does not change).

API-mount alias posture: when the Reader blueprint is mounted under an /api prefix, /api/reader is an alias of the same Reader surface. It is not a distinct contract or a separate proof surface.

Forbidden invented route: /api/reader-proof/v1 MUST NOT appear in the Endpoint Catalog, in endpoint snapshot artifacts, or in any proof-surface references. Proofs that depend on a Reader success route MUST target the actual reachable mounted Reader route for the target environment. When this Catalog is used for selection, select only from Catalog entries that correspond to real mounted routes (no invented proof routes).

Governed Reader success-proof designation (normative).

The authoritative Endpoint Catalog MUST explicitly designate the governed Reader success-proof surface within the Catalog’s own machine-readable structure.

For the current HD Engine Reader success surface, that designation resolves to `GET /reader`.

When an `/api` blueprint mount exists, `/api/reader` is an alias of the same Reader surface and MUST NOT be treated as a second governed proof surface.

This designation MUST NOT be inferred solely from route existence, env-gate posture, or `a7_eligible:true` on a catalog row.

The designation MUST remain inside the existing single-home Catalog posture and MUST NOT be carried by a second designation mechanism, a second inventory home, a new route, or a flag created solely to carry proof-surface authority.

Minimum required fields (per endpoint record). Each endpoint entry in `docs/ENDPOINTS_CATALOG.json` MUST include at least:

* `path`: HTTP path as a string (e.g., /api/compat/v1).

* `method`: HTTP method as a string (e.g., GET, POST).

* `internal`: Boolean. True indicates the endpoint is non-public (internal/ops/dev surface).

* `classification`: One of public\_reader, public\_compat, internal\_identity, internal\_admin, ops, dev\_harness.

* `env_gate`: Env-gate metadata for non-public endpoints. Value MUST be either (a) a string expression (example: `APP_ENV!=prod`) or (b) an object mapping env var names to required values (example: `{"APP_ENV":"dev"}`).

* `a7_eligible`: Boolean. True indicates the endpoint is eligible to be selected by the A7 proof harness.

* `blueprint_module`: The owning blueprint module (names-only).

* `rails_profile`: A names-only summary of rails mode. Use a short string, no secrets.

Additional key for writer surfaces (conditional).

* `route_id`: Stable route identifier string (names-only). Required for endpoint catalog entries referenced by writer-envelope idempotence behavior (example: dev.writer.conjunction.v1).

Minimum schema (records-only):

* {"generated\_at\_utc":"YYYY-MM-DDThh:mm:ssZ","endpoints":\[{"path":"\<route-path\>","method":"\<METHOD\>","internal":true,"classification":"\<one-of: public\_reader|public\_compat|internal\_identity|internal\_admin|ops|dev\_harness\>","env\_gate":"\<string-or-map\>","a7\_eligible":false,"blueprint\_module":"\<module-path\>","rails\_profile":"\<names-only rails summary\>"}\]}

### **Indexing**

Human Index: add a titles/paths-only entry in docs/evidence/INDEX.json and update the hash sentinel docs/evidence/INDEX.sha256 in the same PR.

Machine mirror: add a matching records-only line to artifacts/evidence\_index.jsonl (see §8.3). The mirror record MUST include artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, and a proof\_anchor to a path\_proof.txt stored alongside the artifact.

Mirror hygiene (merge-blocking): canonical JSONL, unknown-key rejection, ASCII field order and sort-before-write as pinned in §8.3; exactly one mirror file in the repo.

Env-gate pairing: pair this entry with `artifacts/proofs/endpoints_env_gate_proof.log` to prove env-gating (headers-only, LF-terminated; header names lower-case, values verbatim).

Acceptance hints (titles only; tokens live in HDE-Governance §2.0). ENDPOINTS\_CATALOG\_OK, ENDPOINTS\_CATALOG\_INTERNAL\_OK, ENDPOINTS\_CATALOG\_ENV\_GATE\_OK, A7\_TRANSPORT\_PROOF\_OK.

## **8.9 Start-command capture (records-only)**

Content: effective start command as bytes with sha256; path discovered post-emission.

Indexing: list in machine mirror and human index (titles/paths only).

Acceptance hints. START\_COMMAND\_CAPTURE\_OK.

## **8.10 Environment inventories, redacted environment snapshots, and validator outputs (names-only)**

Inventories: canonical JSON listing of environment variables consulted by the service; unknown keys flagged.

Redacted environment snapshots: governed evidence that records exact environment-variable key names, provider/context labels, environment labels, redacted value posture, requiredness, and whether each key is rails-related, vendor-related, DB-related, dev-harness-related, vendor-related, or secret-bearing. Secret values MUST remain redacted or presence-only. Snapshots MAY record non-secret base URLs, URL hostnames and ports provided by PO or infrastructure canon, redacted database URL forms, and exact key-spelling differences across environments.

Secret-safe header-shape evidence: governed evidence MAY record outbound header names, header family, and redacted header shape when those facts prove request-shaping posture. It MUST NOT record raw header values, raw bearer tokens, raw API keys, raw geocode keys, database credentials, or plaintext secrets. Acceptable redacted shapes include `Authorization: Bearer <redacted>`, `HD-Api-Key: <redacted>`, and `HD-Geocode-Key: <redacted>` when those shapes are required by the owning vendor contract and byte homes.

HumanDesignAPI vendor environment evidence MUST preserve `HD_API_BASE_URL` as the canonical base-url key when that posture is being proven. `HDAPI_BASE_URL` MAY appear only as deprecated alias, compatibility, observed drift, or migration evidence. If both spellings are present and differ, the evidence MUST record configuration ambiguity and fail-closed posture rather than silently normalizing the keys.

Validator outputs: records-only outputs to prove config sanity.

Indexing: list in machine mirror and human index (titles/paths only), with sibling path-proof transcripts when promoted into governed evidence.

Acceptance hints. ENV\_INVENTORY\_OK, VALIDATOR\_OUTPUTS\_OK.

## **8.11 SBOM (records-only) \[Optional\]**

Purpose. Provide a build-time Software Bill of Materials to support provenance, audit, and supply-chain review. This artifact is records-only and does not change release\_id or the Freeze-Pack manifest contents.

### **Artifacts (titles/paths only)**

* SBOM (CycloneDX JSON): `sbom/cyclonedx.json`

* SBOM hash (sha256): `sbom/cyclonedx.json.sha256`

### **Format & scope**

Format: CycloneDX JSON (v1.x). Titles-only here; bytes live at the path above.

Scope: Enumerates runtime and package components for the shipped artifact; no secrets/tokens, no PII.

Stability: Generated from the finalized dependency graph of the release build; the tool version and preset is pinned in CI (names-only).

### **Indexing (required)**

Appendix D (human index): add a titles/paths-only entry for `sbom/cyclonedx.json` and `sbom/cyclonedx.json.sha256` in the same PR that adds or changes them.

Machine mirror (artifacts/evidence\_index.jsonl): add one record per artifact with artifact\_key, role, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor.

Mirror hygiene (merge-blocking): canonical JSONL (one LF), unknown-key rejection, ASCII field order, sort-before-write (see §8.3); exactly one mirror file in the repo.

Path-proof: store a path\_proof (stat transcript) alongside each SBOM artifact and reference it via proof\_anchor in the mirror record.

### **Determinism & environment**

Generate and verify under LC\_ALL=C, LANG=C, TZ=UTC.

SBOM bytes are canonical JSON (UTF-8, no BOM; sorted keys where the tool allows; compact; exactly one trailing LF).

### **Retention & release identity**

SBOM is not part of catalog/manifest.json and does not affect release\_id.

Ship under sbom/ in the release bundle; treat as a governed, records-only artifact.

Acceptance hints (titles only; tokens live in HDE-Governance §2.0). SBOM\_PRESENT\_OK, SBOM\_HASH\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, CI\_CHECK\_FINAL\_LF\_OK, CI\_CHECK\_MIRROR\_SCHEMA\_OK.

Routing (titles-only). Provenance policy and release workflow: Epic-Process-Guide; HDE-Governance §2.0 tokens and evidence rules.

## **8.12 Reader A7 composite proof — schema & validation (records-only) \[Required-Now\]**

Purpose. Provide a single, machine-checkable JSON artifact that proves the A7 suite on a cataloged JSON success route (GET, HEAD, 304; quoted strong ETag; Vary; encoding-invariance). The /internal/version ops surface is excluded.

Alternate artifact example (same schema): `artifacts/proofs/reader_route_proof.json`.

Schema (single home). Schema path: `schemas/proofs.reader_success.v1.json` (owned by PF12). Artifact (example): `artifacts/proofs/reader_success_get_head_304.json` (records-only). Routing: Tokens live in Governance; transport bytes live in Vendor Ref. This section governs only the artifact’s shape and validation. Always pair this artifact with the Catalog snapshot and the env-gate proof (see Indexing).

Minimum required fields (reject unknown keys).

* {"route\_path":"\<Catalog title or identifier of the success route\>","env\_gate":{"proof\_path":"artifacts/proofs/endpoints\_env\_gate\_proof.log","gated\_ok":true},"get\_200":{"content\_type":"application/json; charset=utf-8","etag":""\<strong-etag\>"","body\_sha256":"\<64-hex\>","captured\_at\_utc":"YYYY-MM-DDThh:mm:ssZ"},"head\_200":{"content\_type\_equals\_get":true,"content\_length\_equals\_identity":true,"no\_body":true},"after\_304":{"seen\_after\_prior\_get":true,"no\_body":true,"omits\_content\_type":true,"omits\_content\_length":true},"vary\_flags":{"authorization":true,"accept\_encoding":true},"etag":{"identity\_etag":""\<strong-etag\>"","encoding\_invariance\_ok":true,"tested\_encodings":\["identity","gzip","br"\]}}

Field notes (normative): route\_path references the Catalog route by title (no URL). env\_gate.proof\_path points to the headers-only env-gate artifact; gated\_ok: true asserts non-prod entries are unreachable in prod. get\_200.body\_sha256 is the SHA-256 of the LF-terminated canonical body used for identity. head\_200.content\_length\_equals\_identity compares to the GET identity body length (pre-compression). after\_304 proves the 304 invariants (only after prior 200; omits both Content-Type and Content-Length; no body). vary\_flags must assert both authorization and accept\_encoding. etag.encoding\_invariance\_ok: true affirms identity (ETag) and effective length are stable across accepted encodings.

Validation & CI (merge-blocking). The proof JSON MUST validate against `schemas/proofs.reader_success.v1.json` before indexing. Unknown keys are rejected (mirror enforces). Canonical JSON: UTF-8 (no BOM), sorted keys, compact, exactly one trailing \\n. Determinism: all captures and derivations run with LC\_ALL=C, TZ=UTC. Governed locations only: artifact under artifacts/; schema under schemas/.

Artifact write gating (normative). Proof artifacts under `artifacts/proofs/` MUST be written only when `HDE_WRITE_A7_PROOFS=1` is set. Default test runs MUST NOT create or modify these files.

When proof artifacts are updated, check in the governed proof artifacts plus their sibling `.path_proof.txt` transcripts in the same PR.

Indexing (titles/paths only). Human Index: add a titles/paths entry in docs/evidence/INDEX.json and update docs/evidence/INDEX.sha256 in the same PR. Machine mirror: add a records-only line to artifacts/evidence\_index.jsonl (see §8.3) with artifact\_key, role:"proof", discovered\_physical\_path, sha256, size\_bytes, produced\_at\_utc, and a proof\_anchor to a path\_proof.txt stored alongside the JSON file. Pair with `artifacts/reader/endpoints_snapshot.json` (Catalog snapshot) and `artifacts/proofs/endpoints_env_gate_proof.log` (env-gate headers).

Acceptance hints (titles-only; tokens live in HDE-Governance §2.0). A7\_GET\_QUOTED\_ETAG\_OK, A7\_HEAD\_PARITY\_OK, A7\_304\_OMITS\_CT\_CL\_OK, A7\_VARY\_AUTH\_AE\_OK, A7\_ENCODING\_INVARIANCE\_OK, A7\_TRANSPORT\_PROOF\_OK, ENDPOINTS\_CATALOG\_OK, ENDPOINTS\_CATALOG\_INTERNAL\_OK, ENDPOINTS\_CATALOG\_ENV\_GATE\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_INDEX\_MIRROR\_OK.

## **8.13 Stateless QA export families (no-DB JSON mode) \[Required-Now\]**

Purpose. Record the governed evidence families used to exercise the engine in a stateless/no-DB QA mode, using only CLI \+ files. These families do not replace existing DB-bound evidence; they provide a complementary way to prove engine math and Reader/CLI parity when no app user model or persistent BodyGraph records are available.

HD Engine ownership posture. HumanDesignAPI vendor acquisition evidence, raw vendor BodyGraph or chart acquisition evidence, BodyGraph persistence evidence, BodyGraph retrieval evidence, HD computation evidence, and normalized app-facing export evidence belong to HD Engine governed evidence families unless future canon explicitly moves that responsibility. App-facing or stateless outputs MUST be normalized and governed artifacts; they MUST NOT make raw unbounded vendor payload ownership an app-layer, public payload, or direct app-to-vendor contract by inference.

### **Family: qa.bodygraph\_export.stateless**

Role. Captures a single BodyGraph export JSON object produced directly from birth data or vendor JSON via CLI, without reading or writing app/user tables.

Minimum content (names-only):

* schema: a string tag (e.g. "hdctl\_bodygraph\_export.v1") governed by this document.

* input: a birth tuple or vendor JSON descriptor (names-only; schema pinned in PF12 §3.x).

* bodygraph: a structure containing centers, channels, gates, profile, authority, definition, and type as IDs (titles-only to HDE-Math-Spec and HDE-Schemas & Artifacts catalogs).

* meta: engine/build identity fields (e.g. engine\_tag, release\_id, invocation\_tag) routed to HDE-Math-Spec/HDE-Governance by title.

Canonical JSON. Artifact bytes MUST obey PF12 canonical JSON rules: UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF; arrays used as sets deduped and ASCII-sorted.

Stateless posture. No app-level user IDs or DB row identifiers are permitted in this artifact; provenance is via input and catalog IDs only.

Indexing. When used as governed evidence, each artifact MUST be indexed in docs/evidence/INDEX.json and mirrored in artifacts/evidence\_index.jsonl with a proof\_anchor to a co-located path-proof transcript (see §8.3).

### **Family: qa.compat\_export.stateless**

Role. Captures a compat run in stateless mode, using two BodyGraph exports or two birth tuples as inputs, and emits compat \+ Reader envelope JSON without DB users.

Minimum content (names-only):

* schema: a string tag (e.g. "hdctl\_compat\_export.v1") governed here.

* inputs: references to the two charts (by birth data and or BodyGraph export identity).

* compat: internal compat result (Magic-10 IDs and bands only; numbers remain admin/internal; arithmetic lives in HDE-Math-Spec).

* reader\_envelope: nested copy of the six-key Reader v1 success body for this pair (see PF01/PF05 by title), used for Reader↔CLI parity checks; this is not a separate public transport surface.

* meta: identity fields as above (engine\_tag, release\_id, invocation\_tag).

Canonical JSON. Same canonical JSON requirements as qa.bodygraph\_export.stateless.

Stateless posture. No DB user IDs; only birth and BodyGraph identities and catalog IDs.

Indexing. Governed uses MUST be indexed and mirrored under the Evidence Index discipline, with path-proofs, like other PF12 evidence families.

### **Family: qa.run\_bundle.stateless (optional)**

Role. Provides a single-file “bundle” tying together inputs, BodyGraph exports, and compat exports for a QA run, to simplify reproduction and auditing.

Minimum content (names-only):

* schema: bundle schema tag (e.g. "hdctl\_run\_bundle.v1").

* inputs: original birth tuples or vendor descriptors.

* artifacts: references (by artifact\_key and or file path) to the BodyGraph export and compat export artifacts produced in this run.

* meta: minimal identity fields (engine\_tag, release\_id, invocation\_tag, run\_id).

Canonical JSON. Same canonical JSON posture as other QA families; arrays-as-sets semantics apply to any list of artifact references.

Indexing. When used as governed evidence, bundles are indexed and mirrored like other artifacts; they do not replace indexing of the underlying BodyGraph and compat exports.

No transport bytes here. These families define artifact shapes and governance, not CLI flags or HTTP contracts. CLI command names, flags (for example, a future hdctl bg:export-json or pure-mode showcompat), and any QA scripts that produce these artifacts are specified in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide; PF12 remains contract-free and schema-first.

Acceptance (names-only). When these families are adopted by a future epic, PF12 and PF09 may attach the following hints to them (token semantics live in HDE-Governance): JSON\_CANONICAL\_CHECK\_OK, TWO\_RUN\_IDENTITY\_OK, CLI\_SHOWCOMPAT\_CANON\_OK, CLI\_STDOUT\_LF\_OK, CLI\_READER\_PARITY\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK.

Governance and QA docs (PF04, PF09, PF19, PF20) refer to these families by name (qa.bodygraph\_export.stateless, qa.compat\_export.stateless, qa.run\_bundle.stateless) and must not define parallel path lists.

## **8.14 Config artifacts & acceptance map (D5) \[Required−Now\]**

Purpose. Record the governed config artifact families and the config acceptance map introduced in D5 of HDE-EPIC018 and tie them into the Evidence Catalog and Machine Mirror. These artifacts are generated under closed rails using the hardened registry loader and canonical serializer, and they provide the concrete evidence surfaces for config-related acceptance tokens (names-only; semantics live in Glow QA Guide and HDE-Governance).

Scope. This section covers:

* artifacts/thresholds/magic10\_config.json — governed Magic-10 config snapshot.

* artifacts/thresholds/band\_edges.json — governed band-edges config snapshot.

* audit/EPIC-018\_config\_acceptance\_map.json — governed PF09-style config acceptance map for HDE-EPIC018.

The registry report at artifacts/registry/registry\_report.json is governed separately in §8.5; this section only cross-references it where needed.

### **8.14.1 Magic-10 config artifact (config.magic10)**

Path (fixed): artifacts/thresholds/magic10\_config.json

Role and artifact\_key:

* Mirror artifact\_key: "config.magic10" (names-only).

* Mirror role: "snapshot".

Generation and env rails (titles-only):

* Generated by tools/config/generate\_config\_artifacts.py under closed rails: LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0.

* Uses the hardened registry loader and the shared canonical serializer (per §4) to ensure deterministic bytes and two-run identity.

Canonical JSON and schema tag:

* MUST be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* MUST contain a top-level schema field whose value MUST equal "magic10\_config.v1".

* MUST use field shapes and types pinned by the owning JSON Schema for this artifact (names-only; the schema file is referenced here by title, not path).

Content (names-only, from Addendum 6):

At minimum, the Magic-10 config JSON MUST:

* Capture the normative Magic-10 order as a closed list matching the Magic-10 catalog (§2.6): ten category IDs in the pinned order.

* Record per-category caps as integer bounds for all categories (inputs \+ integer limits); details of the cap object shape are governed by the config schema and tests, not restated here.

* Include seed metadata for each Magic-10 category with at least the fields:

  * template\_id — string.

  * seed\_version — integer or string version identifier.

  * updated\_at\_utc — UTC ISO-8601 timestamp string.

  * checksum\_sha256 — lowercase 64-hex digest of the seed’s canonical bytes.

The config MUST NOT introduce new Magic-10 IDs; all IDs must belong to the closed domain defined in the Magic-10 catalog (§2.6, §3.3). Any unknown ID is a hard error.

### **8.14.2 Band-edges config artifact (config.band\_edges)**

Path (fixed): artifacts/thresholds/band\_edges.json

Role and artifact\_key:

* Mirror artifact\_key: "config.band\_edges" (names-only).

* Mirror role: "snapshot".

Generation and env rails (titles-only):

* Generated by tools/config/generate\_config\_artifacts.py under the same closed-rails profile as config.magic10 (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0).

* Uses the shared canonical serializer; two-run identity must hold for this artifact as well.

Canonical JSON and schema tag:

* MUST be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* MUST contain a top-level schema field whose value MUST equal "band\_edges.v1".

* MUST include top-level fields for band names and edges, clamp policy, rounding mode, and version \+ a source pointer back to math/thresholds.json, with exact field names and types pinned by the owning JSON Schema; PF12 does not restate the full schema.

Content (names-only, from Addendum 6):

At minimum, the band-edges config JSON MUST:

* Enumerate the band names and the numeric edges used for banding, in a form consistent with the engine’s band constants (names-only; arithmetic remains in Math).

* Encode clamp behavior and rounding mode (for example, how values at or beyond the defined edges are handled and how intermediate values are rounded) in explicit fields governed by the schema.

* Include a version identifier for the band-edges config itself and a pointer back to math/thresholds.json indicating which thresholds source this config was derived from.

Any mismatch between band edges and math/thresholds.json (for example, missing bands, unsorted edges, or incompatible ranges) is a hard error in the config tests and should be treated as a spec violation.

### **8.14.3 EPIC-018 config acceptance map (epic018.config.acceptance\_map)**

Path (fixed): audit/EPIC-018\_config\_acceptance\_map.json

Role and artifact\_key:

* Mirror artifact\_key: "epic018.config.acceptance\_map" (names-only).

* Mirror role: "snapshot".

Purpose. Record, in canonical JSON, the mapping between PF09 config tasks, governed config artifacts, config-related acceptance tokens, and the tests that uphold them for HDE-EPIC018 D5.

Canonical JSON and shape:

audit/EPIC-018\_config\_acceptance\_map.json MUST:

* Be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* Use a top-level JSON object where each property name is a PF09 task ID string (for example, "HDE-CALC004", "HDE-CALC004.3", "HDE-CALC004.7").

* Map each task ID to an object with at least the following fields:

  * artifact\_key — string; MUST be one of the governed config or registry artifact keys (for example "registry.registry\_report", "config.magic10", "config.band\_edges").

  * tokens — array of strings; acceptance token names (names-only) relevant to the task (for example, CONFIG\_REGISTRY\_OK, CONFIG\_MAGIC10\_OK); array-as-set semantics apply (dedupe \+ ASCII sort).

  * test\_names — array of strings; names or paths of tests that uphold the mapping (for example, tests/config/test\_config\_artifacts.py::test\_magic10\_config\_snapshot); array-as-set semantics apply.

The exact set of allowed task IDs, artifact keys, token names, and test names is constrained by PF09, PF19, PF04, and the test suite. Config acceptance-map tests enforce that:

* Every task ID named in the map is a known PF09 task ID.

* Every artifact\_key corresponds to an artifact listed in the Evidence Index (§8.6) and Appendix C.

* Every tokens\[\] entry is a known token name (semantics live in Governance and QA).

* Every test\_names\[\] entry refers to an existing test artifact (file and, when encoded, node).

Indexing and parity:

All three config families in this section MUST participate in the standard Evidence Index and Machine Mirror discipline.

Human Index. docs/evidence/INDEX.json MUST include entries with the following (artifact\_key, discovered\_physical\_path) pairs:

* ("config.magic10", "artifacts/thresholds/magic10\_config.json")

* ("config.band\_edges", "artifacts/thresholds/band\_edges.json")

* ("epic018.config.acceptance\_map", "audit/EPIC-018\_config\_acceptance\_map.json")

docs/evidence/INDEX.sha256 MUST be updated in the same PR as any change to these artifacts or their paths.

Machine mirror. artifacts/evidence\_index.jsonl MUST contain canonical JSONL records for each of the above artifact keys with:

* artifact\_key

* role ("snapshot" for all three)

* discovered\_physical\_path equal to the paths above

* sha256 and size\_bytes matching the artifact’s canonical bytes

* produced\_at\_utc reflecting the evidence refresh time

* proof\_anchor pointing to the matching .path\_proof.txt transcript alongside each artifact

Mirror records MUST obey §8.3’s schema, field order, sort-before-write, and single-mirror-file rules.

Path-proof requirements. Each of the three artifacts MUST have a sibling path-proof transcript:

* artifacts/thresholds/magic10\_config.json.path\_proof.txt

* artifacts/thresholds/band\_edges.json.path\_proof.txt

* audit/EPIC-018\_config\_acceptance\_map.json.path\_proof.txt

Each transcript MUST follow the path-proof schema in §8.3 (exactly one record with path, sha256, size\_bytes, mtime\_utc, produced\_at\_utc) and MUST match the mirror record and the artifact bytes exactly.

## **8.15 Config bundles (typed FE/BE) \[Required−Now\]**

Purpose. Record the governed typed config bundles introduced in D6 of HDE-EPIC018 and tie them into the Evidence Catalog and Machine Mirror. These bundles are deterministic, canonical JSON projections of already-governed config artifacts and registry state, and serve as typed configuration payloads for backend and frontend consumers. They are generated under closed rails and provide the evidence surface for bundle-related acceptance tokens (names-only; semantics live in Glow QA Guide and HDE-Governance).

Scope. This section covers two new governed artifact families:

* config\_bundle.fe — typed frontend config bundle.

* config\_bundle.be — typed backend config bundle.

Concrete bundle files live under artifacts/config\_bundles/ (names-only). Exact filenames are owned by the bundle generator and tests; PF12 governs the family, not per-file naming.

### **8.15.1 Backend config bundle (config\_bundle.be)**

Artifact family:

* Artifact key (mirror / Evidence Index): "config\_bundle.be".

* Role: "snapshot" (typed backend bundle).

* Directory: artifacts/config\_bundles/ (filenames owned by the generator; tests and Evidence Index entries pin the exact paths).

Generation and env rails (titles-only):

* Generated by engine/config/bundles.py and tools/config/generate\_bundles.py.

* Generation MUST run under the same closed-rails profile used for D5 config artifacts: LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0.

* Bundles are built exclusively from:

  * governed Magic-10 config (config.magic10)

  * governed band-edges config (config.band\_edges)

  * the registry report (registry.registry\_report)

* via the hardened registry loader (titles-only to Mechanics/Registry).

Canonical JSON and schema tag:

* Each backend bundle JSON MUST be canonical JSON per §4 (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF).

* MUST contain a top-level schema field whose value MUST equal "config\_bundle.be.v1".

* MUST use field shapes and types pinned by the local JSON Schema used in tests (titles-only; schema files live under docs/schemas/ and are not PF12-canonical yet).

Content (names-only, from Addendum 7):

At minimum, the backend bundle MUST contain:

* A Magic-10 section that matches the governed config.magic10 artifact semantically:

  * normative Magic-10 order

  * per-category caps for all ten categories

  * seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256)

* A band-edges section that matches config.band\_edges semantically:

  * band names and edges

  * clamp policy

  * rounding mode

  * version and a pointer to the source thresholds (names-only)

* Full topology slices aligned with the registry report:

  * channel objects with at least the fields id, gates, centers, circuit\_primary, substream, primary\_domain, domains, flags (exact field set pinned by schema/tests), where:

    * id MUST be a canonical channel ID (NN-NN or multi-pair string) consistent with the Channels catalog

    * center/domain/circuit values MUST be consistent with the registry report and catalogs (titles-only to §2.1/§3.2)

  * center records and domain lists consistent with the registry report

  * an alias\_policy block whose semantics match the registry’s alias policy (titles-only; details governed by Mechanics/Registry)

PF12 does not restate the full JSON shape; concrete field definitions are owned by the bundle schemas and tests. The requirements above are names-only semantic constraints.

Sources block:

Each backend bundle MUST include a sources object that records, for each upstream governed artifact:

* an entry for the Magic-10 config (config.magic10)

* an entry for the band-edges config (config.band\_edges)

* an entry for the registry report (registry.registry\_report)

Each sources entry MUST contain at least:

* path — the artifact’s repo-relative path (for example, artifacts/thresholds/magic10\_config.json).

* sha256 — lowercase 64-hex digest of the artifact’s canonical bytes.

* size\_bytes — integer byte length of the artifact’s canonical bytes.

Tests MUST assert that these path/sha256/size\_bytes triples match the current governed artifacts; any mismatch is an error.

Two-run identity. Generating the backend bundle twice over the same inputs and code under closed rails MUST produce identical bytes. Bundle tests (names-only) MUST assert two-run identity and canonical JSON for this artifact.

### **8.15.2 Frontend config bundle (config\_bundle.fe)**

Artifact family:

* Artifact key (mirror / Evidence Index): "config\_bundle.fe".

* Role: "snapshot" (typed frontend bundle).

* Directory: artifacts/config\_bundles/ (filenames owned by the generator; tests and Evidence Index entries pin the exact paths).

Generation and env rails:

* Generated by the same bundle generator (engine/config/bundles.py \+ tools/config/generate\_bundles.py) under the same closed-rails profile as the backend bundle.

* Derived exclusively from the same governed config artifacts and registry report as the backend bundle; no additional config sources.

Canonical JSON and schema tag:

* Each frontend bundle JSON MUST be canonical JSON per §4.

* MUST contain a top-level schema field whose value MUST equal "config\_bundle.fe.v1".

* MUST conform structurally to the local frontend bundle JSON Schema used in tests (titles-only; schema lives under docs/schemas/).

Content (names-only, from Addendum 7):

At minimum, the frontend bundle MUST contain:

* Magic-10 content sufficient for client usage:

  * Magic-10 order and per-category caps consistent with the backend bundle and config.magic10

* Band-edges content sufficient for client usage:

  * band names, edges, clamp behavior, rounding mode, version, and a pointer to the thresholds source, consistent with config.band\_edges

* A trimmed topology view:

  * channel identifiers (IDs) with associated center/domain information such that:

    * the set of channel IDs MUST equal the channel\_ids recorded in the registry report’s artifacts.registry section

    * centers/domains/alias policy information is consistent with the backend bundle and registry report

* An alias\_policy section aligned with the registry report

* A sources object with the same structure and constraints as the backend bundle’s sources block (entries for Magic-10 config, band-edges config, and registry report, each with path, sha256, size\_bytes matching the governed artifacts)

Two-run identity. Generating the frontend bundle twice over the same inputs and code under closed rails MUST produce identical bytes. Bundle tests MUST assert two-run identity and canonical JSON for this artifact.

### **8.15.3 Indexing, path-proofs, and tokens**

Both bundle families MUST participate in the standard Evidence Index/Mirror discipline.

Human Index (docs/evidence/INDEX.json):

* For each concrete frontend bundle file under artifacts/config\_bundles/, there MUST be an entry with artifact\_key: "config\_bundle.fe" and discovered\_physical\_path equal to that file’s repo-relative path.

* For each concrete backend bundle file under artifacts/config\_bundles/, there MUST be an entry with artifact\_key: "config\_bundle.be" and discovered\_physical\_path equal to that file’s repo-relative path.

* docs/evidence/INDEX.sha256 MUST be updated in the same PR as any change to bundle paths or bytes.

Machine mirror (artifacts/evidence\_index.jsonl):

MUST contain canonical JSONL records for config\_bundle.fe and config\_bundle.be with:

* artifact\_key set to "config\_bundle.fe" or "config\_bundle.be" as appropriate

* role: "snapshot"

* discovered\_physical\_path equal to the bundle path recorded in the Human Index

* sha256 and size\_bytes computed from the bundle’s canonical bytes

* produced\_at\_utc reflecting the evidence refresh time

* proof\_anchor pointing to the bundle’s .path\_proof.txt

Mirror records MUST obey all §8.3 rules (field set, ASCII field order, sort-before-write, single mirror file, unknown-key rejection).

Path-proofs:

* Each concrete frontend bundle file MUST have a sibling path-proof transcript named \<bundle\_file\>.path\_proof.txt stored alongside the bundle file, whose path, sha256, size\_bytes, mtime\_utc, and produced\_at\_utc match the bundle’s canonical bytes and mirror record.

* The same requirement applies to backend bundle files.

Acceptance hints (names-only):

PF12 does not own token semantics, but these bundles are the governed surface for bundle-related tokens, including:

* CONFIG\_BUNDLES\_DETERMINISTIC\_OK — typed frontend and backend bundles are generated under closed rails from governed config artifacts and registry report, are canonical JSON, satisfy two-run identity, and contain a sources block whose path/sha256/size\_bytes entries match the current governed artifacts.

Tokens and detailed CI policy live in Glow QA Guide and HDE-Governance; PF12 binds these tokens to the config\_bundle.fe and config\_bundle.be families by artifact key, directory, and sources linkage, not by test names.

## **8.16 Repo implementation docs (non-canonical) \[Required−Now\]**

Purpose. Record the role and limits of repo-level implementation documents that describe PF12-owned artifacts and rails (for example, README, AGENTS, and selected ./docs/\*\* files) so that they remain consistent with this document without becoming parallel sources of truth. These docs are not canon. They exist to help humans run and reason about the EPIC018 engine and evidence harness; PF12 remains the single home for schemas, governed artifact families, and Evidence Catalog entries.

### **8.16.1 Non-canonical implementation docs (titles/paths only)**

The repository contains implementation-level docs that describe PF12-governed behavior for EPIC018:

Top-level docs:

* README.md — EPIC018-centric engine overview; lists D1–D7 outcomes and gives a closed-rails “quickstart” and evidence-harness workflow.

* CHANGELOG.md — includes an EPIC018 entry summarizing deterministic rails, CLI guards, evidence skeleton and sanity pipeline, governed config artifacts, typed bundles, and the manifest/close report.

* AGENTS.md — operational guidance for Codex/dev agents under EPIC018 rails (closed env, single emitter/serializer, CLI guards, evidence tools, and close-out workflow).

Evidence posture crib:

* docs/evidence/EPIC018\_evidence.md — implementation-level view of the EPIC018 evidence skeleton, orientation demo, sanity pipeline, and evidence-update commands. It explains how to run the harness and where artifacts live, but must not redefine schemas, canonical JSON rules, or token semantics already owned by PF12, Glow QA Guide, or Governance.

Config and bundles crib:

* docs/config\_and\_bundles.md — implementation-level view of:

  * D5 governed config artifacts (config.magic10, config.band\_edges, registry.registry\_report) and the EPIC018 config acceptance map (epic018.config.acceptance\_map)

  * D6 typed FE/BE config bundles (config\_bundle.fe, config\_bundle.be) and their local JSON Schemas under docs/schemas/

* This doc explains how to generate and inspect these artifacts using the canonical tools, but PF12 §8.5, §8.14, and §8.15 remain the single homes for their families, canonical JSON posture, and Evidence Index/Mirror behavior.

Runbook and index cribs:

* docs/INDEX.md — repo-level index that points to EPIC018 close-out artifacts (manifest, close report, config acceptance map) and the evidence/tooling surfaces described in §8 (Evidence Index, orientation demo, sanity pipeline, CLI guards, config/bundle generators, determinism helper).

* docs/RUN.md — EPIC018-aligned developer flight checks (env pins, serializer parity, evidence & guard workflow, config and bundle generation), expressed as operational steps that must remain consistent with PF12 §4, §6, and §8 but never override them.

Other architecture and CLI docs under docs/architecture/\*\* and docs/CLI\_\*.md reference PF12-governed artifacts (for example, emitter/serializer guardrails, CLI guards, evidence coupling) by title only and must defer to PF12 and PF-Canon for normative rules.

### **8.16.2 Constraints on repo docs (must follow PF12)**

These implementation docs MUST obey the following constraints:

Non-canonical status:

* Repo docs (README.md, AGENTS.md, CHANGELOG.md, docs/INDEX.md, docs/RUN.md, docs/config\_and\_bundles.md, docs/evidence/EPIC018\_evidence.md, and related ./docs/\*\* files) are not part of PF-Canon.

* When they conflict with PF12 or other PF documents, the PF documents win; the drift is a bug in the repo docs and must be fixed there.

Titles-only routing:

* Repo docs MUST reference PF documents by title only (for example, “HDE-Schemas and Artifacts”, “Glow QA Guide”, “HDE-Phased Epics”, “Epic-Process-Guide”) and MUST NOT inline or restate canonical schemas, Evidence Index field sets, or acceptance token definitions.

* Any normative claim about schemas, canonical JSON rules, Evidence Index/Mirror behavior, or token semantics must appear in PF-Canon, not in repo docs.

No parallel Evidence Catalog:

* Repo docs MUST NOT maintain independent, authoritative lists of governed evidence paths or artifact families.

* The single home for governed artifact families and titles/paths is PF12 §8.x and §8.6; any lists in repo docs must explicitly be framed as summaries or cribs and must be kept in sync with PF12 or removed.

No token ownership:

* Repo docs MUST NOT introduce new acceptance token names, redefine token semantics, or change which artifacts a token covers.

* Token names and meanings remain owned by HDE-Governance and Glow QA Guide; PF12 provides names-only hints and bindings to artifacts (§0.2, §8), not token semantics.

Path lists are illustrative only:

* Where repo docs list specific artifact paths (for example, config artifacts under artifacts/thresholds/, bundles under artifacts/config\_bundles/, or evidence reports under artifacts/ and audit/), those lists are illustrative and must match the authoritative lists in PF12 §8.5, §8.6, §8.14, §8.15 and Appendix C.

* If a path appears in repo docs but not in PF12’s Evidence Catalog, treat it as non-governed until a PF12 Doc-Delta adds it.

### **8.16.3 Doc-Delta expectations**

Repo docs themselves do not require a Doc-Delta when they change wording or flow, but:

* Any change to governed artifacts, Evidence Index entries, Machine Mirror records, config artifacts, or typed bundles still requires a Doc-Delta per §9, regardless of whether a repo doc mentions those artifacts.

* If a change relies on a new repo doc (for example, adding docs/config\_and\_bundles.md as the implementation crib for D5/D6 config/bundles) and that change also adjusts governed artifacts or Evidence Index entries, the Doc-Delta MUST name both:

  * the PF12 sections it affects (for example, §8.5, §8.14, §8.15, §8.6, Appendix C)

  * the new or updated repo docs (by path) as implementation references only.

## **8.17 Live QA evidence layout (audit/qa/\<epic-id\>/) \[Required−Now\]**

Purpose.

Standardize the layout and naming of Live QA evidence under the governed audit/\*\* root so that:

* Live QA artifacts are easy to locate and reason about across epics and attempts.

* Evidence promoted to governed status can be indexed and mirrored consistently.

* The QA process can rely on predictable naming without re-specifying it per epic.

Path provenance (normative).

Live QA plans and runbooks MUST NOT list a file path as “required” unless the path is one of:

* Canon-defined — the path (or path-pattern) is explicitly defined by PF canon (including this section and the Evidence Index entries catalog).

* Audit-proven — the path’s existence is already proven by an existing governed artifact family.

* QA-created — the plan includes inline creation instructions and validation for the path.

Proven or created, otherwise forbidden (MUST).

If a path is not canon-defined and not audit-proven, it MUST either be created under QA with explicit instructions and justification, or it MUST NOT appear in the plan.

QA-created path requirements (MUST).

When a plan requires QA to create a file that has no prior canonical existence, the relevant step MUST include:

* exact mkdir / write instructions (no placeholders)

* a one-line purpose (what the file proves and why it exists)

* explicit PASS and FAIL predicates tied to the file’s contents

QA write scope (MUST).

QA MAY create folders/files only under audit/\*\* or artifacts/\*\*.

Pre-existing vs QA-run artifacts (MUST).

Plans MUST separate pre-existing artifacts (expected to exist before execution) from QA-run artifacts (created during execution).

Preflight presence gating (MUST).

Preflight “presence” checks MUST only gate on pre-existing artifacts. A QA-run artifact MUST NOT be required in preflight unless the plan also creates it in that same preflight step.

New standardized evidence families (MUST).

If a new recurring QA evidence family/path is needed, it MUST be introduced via Glow HD Engine Build Notes addendum (or the owning PF canon home) before plans may require it.

If the live truth is introduced first via Glow HD Engine Build Notes addendum, drain into the owning PF document later under the normal canon-maintenance workflow. The absence of later drainage is not, by itself, an execution, acceptance, or closeout blocker once the live truth is recorded.

Epic Plan evidence-family reference posture.

* A high-level evidence-family reference in an Epic Plan is a planning reference only unless the plan or an owning PF section also defines concrete QA evidence production requirements.  
* A high-level evidence-family reference MUST NOT be treated as a required QA evidence artifact, close-pack evidence inventory item, Human Index entry, Machine Mirror row, path-proof obligation, or close-stage deliverable by itself.  
* QA evidence production requirements require concrete paths, creation or discovery posture, PASS/FAIL predicates, and the applicable Evidence Index / Machine Mirror / path-proof posture.  
* Close-pack evidence inventories require the close-pack baseline artifacts and key\_outputs binding posture defined in this section or a later owning PF canon update.

Live QA Plan approval evidence identity vs later byte-shape validation.

* Live QA Plan approval requires evidence identity: proof target, governed evidence family or class, decisive receipt, PASS and FAIL predicate, rails posture, and token non-claim posture when applicable.  
* Live QA Plan approval does not require every final byte-shape detail to be specified in advance when evidence identity, safe execution, and verdictability are clear.  
* Byte-shape details may still fail QA execution, evidence indexing, or closeout validation. Closeout-time validation remains responsible for canonical JSON compactness, field order, path-proof transcript shape, step-log header shape, mirror-record shape, checksum sidecars, zero-byte prohibition, and Human Index / Machine Mirror parity.  
* Plan approval MUST NOT be treated as a waiver of later PF12 evidence-discipline failures.

Governed evidence planning posture.

* Evidence family identity and governed proof intent matter at plan approval.  
* Byte-perfect generation mechanics, helper syntax, and command literalness are execution details unless they change evidence identity.  
* Path-proof or evidence-index planning MUST NOT be blocked because a plan’s helper syntax is not paste-ready.  
* Plan approval MUST distinguish evidence identity from execution syntax.  
* These plan-approval rules do not waive execution-time or closeout-time PF12 evidence discipline.

Scope / root.

The canonical root for Live QA evidence is:

* EPIC\_QA\_ROOT \= audit/qa/\<epic-id\>/

Within EPIC\_QA\_ROOT, evidence is organized primarily by check\_id (current-state), with a stable epic-level manifest at:

* `audit/qa/<epic-id>/qa_step_logs_manifest.json`: Per-epic manifest acting as a current-state index keyed by check\_id. Each manifest entry MUST carry, at minimum, `check_id`, `status`, and `log_path`; `log_path` MUST point to that check’s canonical primary log under the epic QA root. Additional fields such as `check_name`, `fail_status`, and `timestamp_utc` MAY appear when the producing plan or harness records them. Records-only canonical JSON (UTF-8, ASCII-sorted keys, compact, exactly one trailing LF).  
* `audit/qa/<epic-id>/checks/po-000/qa_step_logs_manifest.json`: Optional step-0, check-scoped current-state copy of the QA step logs manifest. When a Live QA plan explicitly names this check-scoped manifest as a required deliverable, it is the binding surface for that run.

This section does not define:

* Live QA rails posture, D-goal semantics, or QA tokens (titles-only routing to Glow QA Guide, HDE-Phased Epics, HDE-Governance, and HDE-Build Checklist).

* Which specific Live QA artifacts must be indexed in the Evidence Index/Mirror; that remains governed by the QA source-of-truth documents and epic-specific plans.

Current-state evidence (normative).

Under audit/qa/\<epic-id\>/:

* Current-state evidence is the set of artifacts referenced by qa\_step\_logs\_manifest.json as the latest authoritative results for each check\_id.

* Re-running a check MUST reuse stable check-scoped paths under audit/qa/\<epic-id\>/checks/\<check\_id\>/ and MUST NOT create a new run root.

Tools MUST NOT infer run state by enumerating subdirectories under audit/qa/\<epic-id\>/. The manifest is the authoritative index of current-state step evidence.

### **8.17.1 Root and step directories**

Epic QA root (per epic).

Each epic’s Live QA area lives under:

EPIC\_QA\_ROOT \= audit/qa/\<epic-id\>/

EPIC\_QA\_ROOT MUST use lower-case ASCII directory names for fixed directory slugs (for example 00\_meta/, checks/, results/). Per-check directories under checks/ are named by the check\_id token and are exempt from the lower-case rule (see Directory name rules).

EPIC\_QA\_ROOT MAY contain:

* 00\_meta/ — stable, mechanically produced epic-level QA metadata (for example, baseline rails/env pins capture, optional debugging captures).

* checks/ — current-state per-check directories (one directory per check\_id). Each check directory contains primary.log and MAY contain auxiliary tmp\_\* supporting files or plan-owned outputs.

* results/ — current-state step outputs and verdict artifacts (names-only; plan-owned).

* snapshots/ — run-local convenience copies of governed artifacts and headers (names-only; non-canon).

* closeout/ — current-state closeout summaries (names-only; plan-owned).

* remediation/ — remediation-only staging (if present); excluded from governed Evidence Index/Mirror unless explicitly governed elsewhere.

Planning-trace deliverables (hard rule).

Live QA Plans MUST NOT include any required deliverable whose sole purpose is “PF23 consult capture.” Planning consult capture is planning-time only and is not a governed member of the audit/qa/\<epic-id\>/ evidence layout.

Checks-only evidence layout (hard rule).

Per-run directory nesting is disallowed for Live QA evidence. Live QA Plans, QA prompts, and QA reviews MUST NOT introduce or depend on run-id directories, timestamped run roots, or operator-selected fresh evidence roots.

Plan-created Live QA deliverables are allowed, but they MUST live under stable `audit/qa/<epic-id>/checks/<check_id>/` directories. Re-running a check MUST reuse the same check-scoped path rather than creating a new root for that run.

Directory name rules.

* The EPIC\_QA\_ROOT directory name and its fixed structural children MUST use lower-case ASCII: 00\_meta/, checks/, results/, and tmp/.

* Per-check directories under checks/ MUST be named by the check\_id slug used for manifest keying, and that slug MUST be lower-case ASCII.

* Use `-` as the default separator for new plan-owned directory slugs. Use `_` only if matching an existing canon slug (example: po-017\_lowercase\_naming).

Scope note (directory-only).

* This rail applies to directory names only. Filenames MAY contain uppercase characters unless separately forbidden by canon.

* When validating this rail mechanically, scan directories, not file paths. Example: `find <root> -type d -print | grep -n -E '[A-Z]'`.

### **8.17.2 Primary step logs and emptiness rules**

Mechanical, not hand-edited (governed evidence rule).

Any Live QA artifact treated as QA evidence (for example: indexed, mirrored, or referenced as acceptance evidence) MUST be produced by commands (shell/scripts/CLI tools). Manual editing in an editor is prohibited for artifacts treated as evidence.

Placeholders that imply later human fill (for example, (fill PASS/FAIL) or “fill manually as run proceeds”) are non-conforming in approved QA evidence templates.

If a Live QA run requires summary or RCA artifacts, they MUST be generated mechanically from machine-readable inputs (for example: step exit codes, step logs, existence checks), not by human fill.

Primary log per check\_id (current-state).

Each Live QA check that produces evidence MUST have exactly one current-state primary log file referenced by qa\_step\_logs\_manifest.json for that check\_id.

Primary log location (canonical).

Primary logs MUST live at:

audit/qa/\<epic-id\>/checks/\<check\_id\>/primary.log

The directory checks/\<check\_id\>/ is the check-scoped home for the check. The \<check\_id\> directory name MUST match the check\_id used for manifest keying (see §8.17.1).

Primary log filename (normative constraints).

The primary log filename is fixed: primary.log.

The log’s header (format owned by QA source-of-truth documents) MUST include the true check\_id used for manifest keying.

JSON header posture (current-state).

* `audit/qa/<epic-id>/checks/<check_id>/primary.log` MUST begin with exactly one machine-readable JSON object header line (first line), followed by the transcript body.

* Header regeneration or Moon Loop header repair MUST result in exactly one header line. If a prior header line exists, it MUST be removed before writing the corrected header.

* The header line SHOULD include a schema\_version value to support validation and downstream parsing.

Plan-scoped header writer inputs (names-only).

If a Live QA plan uses a step-log header writer that reads per-check metadata from environment variables, the plan MUST export the complete required set immediately before header generation for each check and MUST NOT rely on prior step state. Minimum per-check exports (names must match the header writer contract):

* CHECK\_ID

* CHECK\_NAME

* PASS\_FAIL

* COMMANDS\_JSON

* ARTIFACTS\_JSON

* PF\_REFS\_JSON

Artifact list invariants (normative).

* The per-check artifacts list (exported via `ARTIFACTS_JSON` and recorded in the `primary.log` JSON header) MUST include the canonical primary log path for the current `check_id`: `audit/qa/<epic-id>/checks/<check_id>/primary.log`.

* For PASS results (`PASS_FAIL=PASS`), omission of the primary log path from that artifacts list is an evidence hygiene defect and MUST be remediated (header repair or rerun) before the step can be treated as closed PASS.

Live QA handling (discovered mid-run).

If a check ran successfully but primary.log is missing or has a wrong JSON header due to missing exports, a minimal header-only remediation MAY:

* export the required header env vars for the check, and

* regenerate the JSON header and reassemble primary.log by writing the corrected header plus the existing body bytes verbatim

This remediation is evidence-capture only and MUST NOT modify product behavior, test assertions, or acceptance criteria.

Non-empty requirement.

The primary log for a check MUST be a non-empty, LF-terminated text file. It MUST NOT be zero bytes.

If a step fails to complete or tooling fails, the primary log MUST STILL be written and MUST contain at least:

* a short summary of what the check attempted

* a terse failure description and/or final status line consistent with Live QA status semantics (for example, PASS/FAIL\_BEHAVIOR/FAIL\_TOOLING/TOOLING\_BLOCKED)

It is an error for a planned check to have no primary log at all.

Minimum command transcript capture (current-state).

Each per-check primary log MUST include an execution transcript sufficient to reconstruct what actually ran. At minimum, it MUST capture:

* the exact command line(s) invoked (as executed)

* an explicit exit code (per-command or final)

* stdout/stderr output, or explicit references to captured output files

If a Live QA executor corrects a plan-command syntax defect during execution while preserving the approved command identity and proof target, the per-check primary log or equivalent governed evidence MUST also record:

* the command provenance, such as `Plan + QA syntax correction`  
* a brief reason for the correction  
* the produced evidence artifacts  
* the final PASS, FAIL, or TOOLING classification

The correction MUST NOT silently alter the acceptance target, command identity, artifact output, or PASS/FAIL predicate.

Discovery-resolved loci (runtime evidence).

If a check first discovers a repo-resident locus during execution and then uses it, the primary log MUST record the discovered locus string verbatim before the first command that depends on it.

The primary log SHOULD also record the discovery proof used (for example, an existence check, file listing, or route probe) so the executor’s locus choice remains auditable without guesswork.

Governed Live QA evidence files under audit/qa/\<epic-id\>/ MUST NOT be empty:

* If a planned artifact is not produced, the file MUST be absent rather than present with size 0\.

* Path-proofs and Machine Mirror records MUST NOT point to zero-byte QA artifacts.

Exception: Sentinel files MAY be empty if clearly marked as sentinel and MUST NOT be referenced by the Human Evidence Index, Machine Mirror, or acceptance binding surfaces.

### **8.17.3 Supporting files and tmp\_\* naming**

Supporting files (auxiliary; not canonical per-step).

A Live QA check MAY produce additional supporting files (for example, JSON request bodies, sorted ID lists, raw CLI outputs). These files are auxiliary and do not replace the primary log.

Any supporting file SHOULD:

* live under audit/qa/\<epic-id\>/results/ or a check-scoped subdirectory

* use a tmp\_ prefix (for example, tmp\_http\_request.json, tmp\_sorted\_ids.txt, tmp\_cli\_output.txt)

Where a supporting file materially contributes to proof, the primary log SHOULD:

* mention the filename explicitly

* briefly describe how it is used

Canonical per-check surface.

For acceptance and audit purposes, the primary log remains the canonical per-check artifact. Supporting files are auxiliary unless separately promoted to governed evidence by the owning evidence catalog and indexed/mirrored accordingly.

### **8.17.4 Env/rails snapshots and D-goal linkage**

Env/rails snapshots (current-state).

Env/rails snapshot data MUST be captured mechanically for the Live QA run. To preserve a minimal required output set, the required capture surface is the per-check primary.log (see §8.17.2): the primary log SHOULD include the relevant rails/env pins in a machine-grep-friendly header block.

Separate snapshot files under audit/qa/\<epic-id\>/ MAY be produced (recommended: under 00\_meta/ for baseline and under results/ for per-check snapshots), but they are optional and MUST NOT be required for closure unless explicitly promoted as acceptance-decisive governed evidence.

Each snapshot (whether embedded in a primary log header or stored as a standalone text artifact) MUST clearly record, at minimum, values of:

* SAFE\_MODE

* ALLOW\_NETWORK

* APP\_ENV

* LC\_ALL

* LANG

* TZ

in a machine-parsable form consistent with the QA rails pins.

Environment variable discipline (governed interface; QA-time minting prohibited).

* Environment variable names used in Live QA plans and Live QA evidence artifacts are governed interface surfaces, not free text.

* The list above is the minimum required env/rails snapshot set. Plans MAY capture additional environment variables, but MUST NOT treat additional names as required correctness gates unless the names are explicitly canon-approved.

* No QA-time env var minting: new environment variable names MUST NOT be introduced during Live QA execution (including Moon Loop execution). If a plan/tooling flow would require a new environment variable name to function, that is a development change and the name MUST be defined and documented in canon before any plan relies on it.

* MODO\_\* variables are non-canonical and meaningless for Glow/HDE. Any environment variable name beginning with MODO\_ MUST NOT be introduced, required, or depended on for PASS/FAIL or for required evidence structure (including required header fields, required manifest fields, or required evidence schema keys).

* EPIC025 exception (grandfathered; non-binding only): existing approved EPIC025 plan materials may contain MODO\_\* references due to iteration churn. These placeholders MUST be treated as inert and MUST NOT be replicated.

D-goal/token references (titles-only).

When a Live QA artifact is intended to satisfy or inform a specific D-goal or token:

* the corresponding primary log SHOULD include a short, machine-grep-friendly header line stating the D-goal and token names (names-only)

* acceptance wiring documents SHOULD reference the check\_id and primary log path by title only (titles-only routing)

Ownership of semantics.

PF12 standardizes layout and naming only. Semantics for:

* rails posture and env pins

* D-goals and QA tokens

* Live QA workflows and status classifications (for example, PASS/FAIL\_BEHAVIOR/FAIL\_TOOLING/TOOLING\_BLOCKED)

remain owned by the QA source-of-truth documents and are referenced here by title only.

### **8.17.5 Codespaces snapshot (Step-0; current-state) \[Optional\]**

Status (normative).

This artifact is OPTIONAL. Live QA Plans MUST NOT require it for closure by default.

If it is produced and treated as governed evidence, it MUST be generated by commands and MUST NOT be hand-edited (see §8.17.2), and it MUST conform to the canonical bytes and schema rules below.

Purpose.

If produced, provide a single, mechanically generated snapshot of the Codespaces execution context at the start of Live QA so later review can see:

* determinism and rails posture (pins and rails variables)

* tooling versions used for the run

* presence-only status for required secrets and env keys

without leaking secret values.

Canonical path (current-state; epic-level).

audit/qa/\<epic-id\>/00\_meta/codespaces\_snapshot.json

Optional per-run copy (non-canon; allowed).

A run-scoped copy MAY exist at:

audit/qa/\<epic-id\>/runs/\<run\_id\>/snapshots/codespaces\_snapshot.json

If both exist for a given attempt, they MUST be byte-identical.

Run-id discipline note (normative).

run\_id is optional metadata and MUST NOT be used as a governance key. The epic-level current-state snapshot is authoritative; run directories are optional retention only.

Canonical JSON (required).

* UTF-8, no BOM.

* ASCII-sorted keys at every object level.

* Compact separators.

* Exactly one trailing LF.

* No ANSI sequences.

Schema (minimum; reject unknown keys).

codespaces\_snapshot.json MUST be a JSON object with exactly the keys below:

* schema — string, MUST equal "codespaces\_snapshot.v1".

* captured\_at\_utc — string, UTC ISO-8601 (YYYY-MM-DDThh:mm:ssZ).

* epic\_id — string (for example hde-epic022).

* run\_id — string or null.

  * If present as a string, it MUST be a UTC timestamp label (for example 20251221T031045Z).

  * It MUST NOT be required for correctness and MUST NOT be used for keying.

* rails — object with exactly:

  * SAFE\_MODE — integer or boolean (effective value).

  * ALLOW\_NETWORK — integer or boolean (effective value).

  * APP\_ENV — string or null (names-only).

  * LC\_ALL — string.

  * LANG — string.

  * TZ — string.

* tool\_versions — array of objects treated as a set (dedupe \+ ASCII-sort by tool):

  * each item MUST be { "tool": \<string\>, "version": \<string\> }

  * examples (non-normative): "python", "pip", "poetry", "os"

  * tool versions MUST be collected without invoking repository state (no VCS-derived identity).

* env\_presence — array of objects treated as a set (dedupe \+ ASCII-sort by name):

  * each item MUST be { "name": \<string\>, "present": \<boolean\> }

  * Values MUST NOT be recorded. Only name and presence boolean.

  * The list of names to include is owned by the Live QA plan (titles-only routing to the QA source-of-truth).

* notes — array of strings (optional; names-only; no secrets).

Indexing (when used as governed evidence).

When the Codespaces snapshot is used as governed evidence (for example, referenced by acceptance artifacts), the indexed artifact MUST be the epic-level current-state snapshot:

audit/qa/\<epic-id\>/00\_meta/codespaces\_snapshot.json

Optional per-run copies are history retention and do not need separate indexing unless explicitly promoted by acceptance wiring.

# 9\) Change Log & Doc-Delta Hooks \[Required-Now\]

## **9.1 What requires a Doc-Delta**

A Doc-Delta is required whenever a change affects frozen inputs, closed domains, validation rules, or canonical bytes. The Doc-Delta must accompany the change that introduces the effect, and the Evidence Index must be updated in the same PR/commit.

Changes that require a Doc-Delta (normative)

Catalog set changes

Adding a new catalog file  
 Removing a catalog file  
 Renaming or moving a catalog file path

Schema and validation changes

Any edit to an owning JSON Schema  
 Any change to arrays-as-sets identity or ordering rules  
 Any change to topology or cross-reference constraints  
 Pinning or changing JSON Schema draft / $schema / $id conventions (pin to JSON Schema 2020-12)  
 Introducing or revising companion checks for constraints that exceed JSON Schema’s native power (uniqueness, cross-catalog membership, ASCII sort)

Closed domain changes

Adding, removing, or renaming IDs in a closed enum (Centers, Gates, Channels, Authorities, Profiles, Magic-10)  
 Reordering IDs where order is normative

Frozen math inputs changes

Any byte change to catalog/magic10.json (Magic-10 IDs, preset-specific inclusive maxima, caps)  
 Adding or removing a preset entry inside magic10.maxima  
 Changing the prefs key set in the Preset catalog

Manifest and checksums changes

Any edit that changes catalog/manifest.json entries, ordering, or content  
 Adding or removing governed files in the manifest  
 Changing canonical bytes of any governed file (content, key order, whitespace, line endings, encoding)  
 Introducing or changing required checksum sidecars (\*.sha256)  
 Toggling manifest self-listing policy

Machine Evidence Mirror & parity

Changing the Machine Evidence Mirror path or record schema (artifacts/evidence\_index.jsonl) or its parity rule with the human Evidence Index (§8.3)  
 Changing mirror field order or sort-before-write rules; altering the single-mirror-file posture  
 Changing the human-index hash sentinel posture or acceptance (merge-gating)

Governed records-only artifacts in §8

Endpoint-Catalog snapshot and env-gate proof  
 Registry report  
 DB fingerprint / grants / schema / constraints / partition plan / RW smoke  
 Start-command capture and Environment inventories/validator outputs  
 Runtime environment matrix capture

What the Doc-Delta must include

Short summary of the change and its rationale  
 Titles and paths of affected catalogs and schemas  
 Statement of impact on release\_id with the new value if it changes  
 Evidence Index updates (reports, recompute logs, snapshots) updated in the same PR/commit  
 Any new or updated acceptance tokens relevant to the change  
 (Optional but recommended) PR link and commit hash for traceability

CI coupling

The Doc-Delta must land with passing schema, topology, domain-closure, arrays-as-sets, canonicalization, and manifest checks.  
 Recompute release\_id and update snapshots and reports in the same change (enforced by tokens such as EVIDENCE\_INDEX\_UPDATED\_OK).  
 Mirror hygiene must pass: canonical JSONL, unknown-key rejection, ASCII field order, sort-before-write, one mirror file, path-proofs present and joined correctly.

---

## **9.2 Doc-Delta template**

ID/date/scope/targets; summary; acceptance impact; evidence updates; freeze-pack impact; routing (titles-only).

### **How to use**

Fill the template below and attach it to the same change that introduces the edits.

Reference other specs by title only (no version numbers in prose).

Update §8.6 Evidence Index entries where you add or move evidence.

Keep human Appendix D and the machine mirror in §8.3 in the same PR.

### **Fill-in template (paste and complete)**

`doc_delta:`

  `id: "DOCDELTA-YYYYMMDD-<slug>"`

  `date: "YYYY-MM-DD"`

  `author: "<name>"`

  `scope:`

    `catalogs: [true|false]`

    `schemas: [true|false]`

    `manifest_checksums: [true|false]`

    `ci_jobs: [true|false]`

    `evidence_index: [true|false]`

    `routing_only: [true|false]`

  `targets:        # titles and paths only`

    `catalogs_changed:`

      `- title: "Centers"           # §2 reference title`

        `path: "<relative/path>"`

      `- title: "Gates"`

        `path: "<relative/path>"`

    `schemas_changed:`

      `- title: "Centers Schema"`

        `path: "<relative/path>"`

    `other_artifacts_changed:`

      `- title: "catalog/manifest.json"`

        `path: "catalog/manifest.json"`

      `- title: "Endpoint Catalog env-gate proof"`

        `path: "artifacts/proofs/endpoints_env_gate_proof.log"`

      `- title: "Registry report"`

        `path: "artifacts/registry/registry_report.json"`

      `- title: "EPIC close-pack report"`

        `path: "audit/EPIC-009_close_report.md"`

      `- title: "EPIC close-pack manifest"`

        `path: "audit/EPIC-009_MANIFEST.json"`

      `- title: "Evidence Index hash sentinel"`

        `path: "docs/evidence/INDEX.sha256"`

  `summary: |`

    `<short description of what changed and why, one or two paragraphs>`

  `acceptance_impact:            # list tokens that matter`

    `tokens_added: ["<TOKEN_A>", "<TOKEN_B>"]`

    `tokens_removed: []`

    `tokens_unchanged:`

      `- "JSON_CANONICAL_CHECK_OK"`

      `- "UMS_AJV_PASS"`

      `- "CATALOG_DOMAIN_CLOSED_OK"`

      `- "TOPOLOGY_NO_ORPHANS_OK"`

      `- "ARR_SET_ASCII_SORT_OK"`

      `- "EVIDENCE_INDEX_MIRROR_OK"`

      `- "EVIDENCE_INDEX_UPDATED_OK"`

      `- "EVIDENCE_INDEX_HASH_OK"`

      `- "CI_CHECK_MIRROR_SCHEMA_OK"`

      `- "CI_CHECK_FINAL_LF_OK"`

  `freeze_pack_impact:`

    `manifest_changed: [true|false]`

    `release_id_expected_change: [true|false]`

    `computed_release_id: "[OPEN]"          # fill after recompute`

  `notes: |`

    `routing_titles_only:`

      `math: "HDE-Math-Spec"`

      `governance: "HDE-Governance"`

      `cli_api_vendor: "HDE-CLI-API-Vendor-Ref"`

      `architecture: "HDE Architecture"`

  `open_decisions:`

    `- id: "OPEN-CH-PRIMARY"`

      `description: "Choose canonical Channels catalog"`

      `owner: "Isis"`

      `status: "open"`

  `ci_status:                     # pass/fail at time of landing`

    `catalog_schema: "pass|fail"`

    `domain_closure: "pass|fail"`

    `topology: "pass|fail"`

    `arrays_as_sets: "pass|fail"`

    `canonical_json: "pass|fail"`

    `manifest: "pass|fail"`

    `recompute_release_id: "pass|fail"`

    `mirror_schema: "pass|fail"   # CI_CHECK_MIRROR_SCHEMA_OK`

    `final_lf: "pass|fail"        # CI_CHECK_FINAL_LF_OK`

    `env_pins: "pass|fail"        # LC_ALL=C, LANG=C, TZ=UTC`

  `evidence_updates:              # titles and paths only`

    `- title: "Checksum Verification Report"`

      `path: "artifacts/math/checksums_audit.log"`

    `- title: "Manifest Snapshot"`

      `path: "artifacts/math/manifest_snapshot.json"`

    `- title: "Recompute release_id log"`

      `path: "artifacts/math/release_id_recompute.log"`

    `- title: "Environment Pins"`

      `path: "artifacts/proofs/env_pins.txt"`

    `- title: "EPIC close-pack report"`

      `path: "audit/EPIC-009_close_report.md"`

    `- title: "EPIC close-pack manifest"`

      `path: "audit/EPIC-009_MANIFEST.json"`

    `- title: "Evidence Index (human)"`

      `path: "docs/evidence/INDEX.json"`

    `- title: "Evidence Index hash sentinel"`

      `path: "docs/evidence/INDEX.sha256"`

  `change_log_entry: |`

    `<one paragraph for §9 Change Log summarizing the change, listing affected catalogs/schemas by title, stating release_id impact, and confirming human/machine index parity + hash sentinel status>`

### **Submission checklist**

* All targets listed by title and path.

* Update §8.6 Evidence Index and §8.3 machine mirror.

* CI jobs pass with updated artifacts.

* release\_id recomputed if the manifest changed.

* Any unresolved items marked \[OPEN\] with owner and next step.

* Close-pack artifacts listed when applicable.

* Evidence Index hash sentinel updated alongside the human index.

  ## **9.3 Acceptance to land**

All catalog and schema CI green. Evidence Index updated in the same change. New release\_id recorded if the pack changed.

### **Preconditions (normative)**

CI status: All jobs required by §§8.1–8.2 pass on the same change set:

* catalog\_schema\_validate

* catalog\_domain\_closure

* catalog\_topology\_coherence

* catalog\_arrays\_as\_sets

* catalog\_canonical\_json

* integrity\_topology

* integrity\_arrays\_as\_sets

* integrity\_canonicalization\_compare

Manifest integrity: §6 checks pass in the same change:

* MANIFEST\_FILE\_EQ\_CANON\_OK

* MANIFEST\_PATH\_ASCII\_SORT\_OK

* MANIFEST\_NO\_DUP\_PATHS\_OK

* RELEASE\_ID\_FROM\_MANIFEST\_OK

Evidence Index: Update §8.6 (human) and §8.3 (machine) in the same PR; mirror record has proof\_anchor and obeys field-order/sort rules.

Doc-Delta: If any condition in §9.1 applies, a completed §9.2 Doc-Delta is included in the same change.

### **Release handling (normative)**

If any frozen input or the manifest changed, recompute release\_id per §6.2 and record it:

* In the Manifest Snapshot evidence file.

* In the Change Log entry for this change.

If no frozen input or manifest bytes changed, confirm that the prior release\_id remains valid and record that fact in the Change Log entry.

### **Environment and determinism**

All generation and checks run with LC\_ALL=C, LANG=C, TZ=UTC per §4.3.

Two-run identity proof over the pack and manifest passes on the same inputs.

### **Failure policy**

Any CI failure, missing Evidence Index entry, missing required Doc-Delta, or inconsistent release\_id blocks the change from landing.

### **Acceptance tokens (minimum)**

* UMS\_AJV\_PASS

* CATALOG\_DOMAIN\_CLOSED\_OK

* CATALOG\_TOPOLOGY\_OK

* ARR\_SET\_ASCII\_SORT\_OK

* JSON\_CANONICAL\_CHECK\_OK

* MANIFEST\_FILE\_EQ\_CANON\_OK

* RELEASE\_ID\_FROM\_MANIFEST\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* DOC\_DELTA\_PRESENT\_OK

* ENV\_LC\_ALL\_C\_OK

* TWO\_RUN\_IDENTITY\_OK

* CI\_CHECK\_FINAL\_LF\_OK

* CI\_CHECK\_MIRROR\_SCHEMA\_OK

* EVIDENCE\_INDEX\_HASH\_OK

# Appendix A: UMS Schemas

## Ums.catalog.channels

{"meta":{"built\_at\_utc":"2025-10-28T18:04:04.331512Z","sources":\["PF08-Reference-Human Design System.md","PF11-Reference-The Rave I Ching.md"\],"assumptions":\["Channel circuits set only when explicitly confirmed by PF11 gate headers; others use well-known stream inference or marked 'Tribal/Ego' where PF08 text implies Ego/Tribal circuitry.","Astrologic spans copied where visible on PF11 headers; no extrapolation performed for missing gates."\]},"channels":\[{"id":"02-14","name":"The Beat","keynote":"A design of being the keeper of keys","from\_center":"g\_center","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"03-60","name":"Mutation","keynote":"Energy which fluctuates and initiates, pulse","from\_center":"sacral","to\_center":"root","circuit":"Knowing","notes":null},{"id":"08-01","name":"Inspiration","keynote":"The creative role model","from\_center":"throat","to\_center":"g\_center","circuit":"Knowing","notes":null},{"id":"09-52","name":"Concentration","keynote":"A design of determination, focused","from\_center":"sacral","to\_center":"root","circuit":"Understanding","notes":null},{"id":"10-34","name":"Exploration","keynote":"A design of following one's convictions","from\_center":"g\_center","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"10-57","name":"Perfected Form","keynote":"A design of survival","from\_center":"g\_center","to\_center":"spleen","circuit":"Knowing","notes":null},{"id":"11-56","name":"Curiosity","keynote":"A design of a searcher","from\_center":"ajna","to\_center":"throat","circuit":"Sensing","notes":null},{"id":"12-22","name":"Openness","keynote":"A design of a social being","from\_center":"throat","to\_center":"solar\_plexus","circuit":"Sensing","notes":null},{"id":"15-05","name":"Rhythm","keynote":"A design of being in the flow","from\_center":"g\_center","to\_center":"sacral","circuit":"Understanding","notes":null},{"id":"16-48","name":"The Wave Length","keynote":"A design of talent","from\_center":"throat","to\_center":"spleen","circuit":"Understanding","notes":null},{"id":"17-62","name":"Acceptance","keynote":"A design of an organizational being","from\_center":"ajna","to\_center":"throat","circuit":"Understanding","notes":null},{"id":"18-58","name":"Judgment","keynote":"A design of insatiability","from\_center":"spleen","to\_center":"root","circuit":"Understanding","notes":null},{"id":"20-10","name":"Awakening","keynote":"A design of commitment to higher principles","from\_center":"throat","to\_center":"g\_center","circuit":"Knowing","notes":null},{"id":"20-34","name":"Charisma","keynote":"A design where thoughts must become deeds","from\_center":"throat","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"20-57","name":"The Brain Wave","keynote":"A design of penetrating awareness","from\_center":"throat","to\_center":"spleen","circuit":"Knowing","notes":null},{"id":"25-51","name":"Initiation","keynote":"A design of needing to be first","from\_center":"g\_center","to\_center":"ego\_heart","circuit":"Tribal/Ego","notes":null},{"id":"26-44","name":"Surrender","keynote":"A design of a transmitter","from\_center":"ego\_heart","to\_center":"spleen","circuit":"Tribal/Ego","notes":null},{"id":"28-38","name":"Struggle","keynote":"A design of stubbornness","from\_center":"spleen","to\_center":"root","circuit":"Knowing","notes":null},{"id":"30-41","name":"Recognition","keynote":"A design of focused energy","from\_center":"solar\_plexus","to\_center":"root","circuit":null,"notes":null},{"id":"31-07","name":"The Alpha","keynote":"For 'good' or 'bad', a design of leadership","from\_center":"throat","to\_center":"g\_center","circuit":"Understanding","notes":null},{"id":"32-54","name":"Transformation","keynote":"A design of being driven","from\_center":"spleen","to\_center":"root","circuit":"Tribal/Ego","notes":null},{"id":"33-13","name":"The Prodigal","keynote":"The design of the witness","from\_center":"throat","to\_center":"g\_center","circuit":"Sensing","notes":null},{"id":"35-36","name":"Transitoriness","keynote":"A design of a 'Jack of all Trades'","from\_center":"throat","to\_center":"solar\_plexus","circuit":"Sensing","notes":null},{"id":"40-37","name":"Community","keynote":"A design of being a part, seeking a whole","from\_center":"ego\_heart","to\_center":"solar\_plexus","circuit":"Tribal/Ego","notes":null},{"id":"42-53","name":"Maturation","keynote":"A design of balanced development, cyclical","from\_center":"sacral","to\_center":"root","circuit":"Sensing","notes":null},{"id":"43-23","name":"Structuring","keynote":"A design of individuality","from\_center":"ajna","to\_center":"throat","circuit":"Knowing","notes":null},{"id":"45-21","name":"Money","keynote":"A design of a materialist","from\_center":"throat","to\_center":"ego\_heart","circuit":"Tribal/Ego","notes":null},{"id":"46-29","name":"Discovery","keynote":"A design of succeeding where others fail","from\_center":"g\_center","to\_center":"sacral","circuit":"Sensing","notes":null},{"id":"49-19","name":"Synthesis","keynote":"A design of being sensitive","from\_center":"solar\_plexus","to\_center":"root","circuit":"Tribal/Ego","notes":null},{"id":"50-27","name":"Preservation","keynote":"A design of custodianship","from\_center":"spleen","to\_center":"sacral","circuit":"Tribal/Ego","notes":null},{"id":"55-39","name":"Emoting","keynote":"A design of moodiness","from\_center":"solar\_plexus","to\_center":"root","circuit":null,"notes":null},{"id":"57-34","name":"Power","keynote":"A design of an archetype","from\_center":"spleen","to\_center":"sacral","circuit":"Knowing","notes":null},{"id":"59-06","name":"Mating","keynote":"A design focused on reproduction","from\_center":"sacral","to\_center":"solar\_plexus","circuit":"Defense","notes":null},{"id":"61-24","name":"Awareness","keynote":"A design of a thinker","from\_center":"head","to\_center":"ajna","circuit":"Knowing","notes":null},{"id":"63-04","name":"Logic","keynote":"A design of mental ease mixed with doubt","from\_center":"head","to\_center":"ajna","circuit":"Understanding","notes":null},{"id":"64-47","name":"Abstraction","keynote":"A design of mental activity and clarity","from\_center":"head","to\_center":"ajna","circuit":null,"notes":null}\],"count":36}

## Ums.catalog.gates.json

{  
"meta": {  
"built\_at\_utc": "2025-10-28T18:04:04.331512Z",  
"sources": \[  
"PF08-Reference-Human Design System.md",  
"PF11-Reference-The Rave I Ching.md"  
\],  
"assumptions": \[  
"Channel circuits set only when explicitly confirmed by PF11 gate headers; others use well-known stream inference or marked 'Tribal/Ego' where PF08 text implies Ego/Tribal circuitry.",  
"Astrologic spans copied where visible on PF11 headers; no extrapolation performed for missing gates."  
\]  
},  
"gates": \[  
{  
"gate": 1,  
"rave\_title": "The Gate of Self-Expression",  
"i\_ching\_name": "The Creative",  
"channel\_id": "01-08",  
"harmonic\_gate": 8,  
"center": "g\_center",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Scorpio", "deg": 13, "min": 15, "sec": 0 },  
"end": { "sign": "Scorpio", "deg": 18, "min": 52, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 2,  
"rave\_title": "The Gate of the Direction of the Self",  
"i\_ching\_name": "The Receptive",  
"channel\_id": "02-14",  
"harmonic\_gate": 14,  
"center": "g\_center",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Taurus", "deg": 13, "min": 15, "sec": 0 },  
"end": { "sign": "Taurus", "deg": 18, "min": 52, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 3,  
"rave\_title": "The Gate of Ordering",  
"i\_ching\_name": "Difficulty at the Beginning",  
"channel\_id": "03-60",  
"harmonic\_gate": 60,  
"center": "sacral",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Aries", "deg": 26, "min": 22, "sec": 30 },  
"end": { "sign": "Taurus", "deg": 2, "min": 0, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 4,  
"rave\_title": "The Gate of Formulization",  
"i\_ching\_name": "Youthful Folly",  
"channel\_id": "04-63",  
"harmonic\_gate": 63,  
"center": "ajna",  
"circuit": "Understanding",  
"astro\_span": {  
"start": { "sign": "Leo", "deg": 18, "min": 52, "sec": 30 },  
"end": { "sign": "Leo", "deg": 24, "min": 30, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 5,  
"rave\_title": "The Gate of Fixed Rhythms",  
"i\_ching\_name": "Waiting",  
"channel\_id": "05-15",  
"harmonic\_gate": 15,  
"center": "sacral",  
"circuit": "Understanding",  
"astro\_span": {  
"start": { "sign": "Sagittarius", "deg": 11, "min": 22, "sec": 30 },  
"end": { "sign": "Sagittarius", "deg": 17, "min": 0, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 6,  
"rave\_title": "The Gate of Friction",  
"i\_ching\_name": "Conflict",  
"channel\_id": "06-59",  
"harmonic\_gate": 59,  
"center": "solar\_plexus",  
"circuit": "Defense",  
"astro\_span": {  
"start": { "sign": "Virgo", "deg": 22, "min": 37, "sec": 30 },  
"end": { "sign": "Virgo", "deg": 28, "min": 15, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 7,  
"rave\_title": "The Gate of the Role of the Self",  
"i\_ching\_name": "The Army",  
"channel\_id": "07-31",  
"harmonic\_gate": 31,  
"center": "g\_center",  
"circuit": "Understanding",  
"astro\_span": {  
"start": { "sign": "Leo", "deg": 13, "min": 15, "sec": 0 },  
"end": { "sign": "Leo", "deg": 18, "min": 52, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 8,  
"rave\_title": "The Gate of Contribution",  
"i\_ching\_name": "Holding Together",  
"channel\_id": "01-08",  
"harmonic\_gate": 1,  
"center": "throat",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Capricorn", "deg": 24, "min": 30, "sec": 0 },  
"end": { "sign": "Aquarius", "deg": 0, "min": 7, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 9, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 10, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 11,  
"rave\_title": "The Gate of Ideas",  
"i\_ching\_name": "Peace",  
"channel\_id": "11-56",  
"harmonic\_gate": 56,  
"center": "ajna",  
"circuit": "Sensing",  
"astro\_span": {  
"start": { "sign": "Sagittarius", "deg": 22, "min": 37, "sec": 30 },  
"end": { "sign": "Sagittarius", "deg": 28, "min": 15, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 12, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 13, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 14,  
"rave\_title": "The Gate of Power Skills",  
"i\_ching\_name": "Possession in Great Measure",  
"channel\_id": "02-14",  
"harmonic\_gate": 2,  
"center": "sacral",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Scorpio", "deg": 24, "min": 30, "sec": 0 },  
"end": { "sign": "Sagittarius", "deg": 0, "min": 7, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 15,  
"rave\_title": "The Gate of Extremes",  
"i\_ching\_name": "Modesty",  
"channel\_id": "05-15",  
"harmonic\_gate": 5,  
"center": "g\_center",  
"circuit": "Understanding",  
"astro\_span": {  
"start": { "sign": "Gemini", "deg": 28, "min": 15, "sec": 0 },  
"end": { "sign": "Cancer", "deg": 3, "min": 52, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 16, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 17, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 18, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 19,  
"rave\_title": "The Gate of Wanting",  
"i\_ching\_name": "Approach",  
"channel\_id": "19-49",  
"harmonic\_gate": 49,  
"center": "root",  
"circuit": "Tribal/Ego",  
"astro\_span": {  
"start": { "sign": "Aquarius", "deg": 7, "min": 37, "sec": 30 },  
"end": { "sign": "Aquarius", "deg": 13, "min": 15, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 20, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 21, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 22, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 23,  
"rave\_title": "The Gate of Assimilation",  
"i\_ching\_name": "Splitting Apart",  
"channel\_id": "23-43",  
"harmonic\_gate": 43,  
"center": "throat",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Taurus", "deg": 18, "min": 52, "sec": 30 },  
"end": { "sign": "Taurus", "deg": 24, "min": 30, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 24, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 25, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 26, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 27, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 28, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 29,  
"rave\_title": "The Gate of Saying Yes",  
"i\_ching\_name": "The Abysmal",  
"channel\_id": "29-46",  
"harmonic\_gate": 46,  
"center": "sacral",  
"circuit": "Sensing",  
"astro\_span": {  
"start": { "sign": "Leo", "deg": 24, "min": 30, "sec": 0 },  
"end": { "sign": "Virgo", "deg": 0, "min": 7, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 30, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 31,  
"rave\_title": "The Gate of Leading",  
"i\_ching\_name": "Influence",  
"channel\_id": "07-31",  
"harmonic\_gate": 7,  
"center": "throat",  
"circuit": "Understanding",  
"astro\_span": {  
"start": { "sign": "Leo", "deg": 2, "min": 0, "sec": 0 },  
"end": { "sign": "Leo", "deg": 7, "min": 37, "sec": 30 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 32, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 33, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 34, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 35, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 36, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 37, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 38, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 39, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 40, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 41, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 42, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 43,  
"rave\_title": "The Gate of Insight",  
"i\_ching\_name": "Breakthrough",  
"channel\_id": "23-43",  
"harmonic\_gate": 23,  
"center": "ajna",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Scorpio", "deg": 18, "min": 52, "sec": 30 },  
"end": { "sign": "Scorpio", "deg": 24, "min": 30, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{ "gate": 44, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 45, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 46, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 47, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 48, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 49, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 50, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 51, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 52, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 53, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 54, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 55, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{  
"gate": 56,  
"rave\_title": "The Gate of Stimulation",  
"i\_ching\_name": "The Wanderer",  
"channel\_id": "11-56",  
"harmonic\_gate": 11,  
"center": "throat",  
"circuit": "Sensing",  
"astro\_span": {  
"start": { "sign": "Aquarius", "deg": 26, "min": 22, "sec": 30 },  
"end": { "sign": "Pisces", "deg": 2, "min": 0, "sec": 0 }  
},  
"crosses": \[\],  
"notes": null  
},  
{  
"gate": 57,  
"rave\_title": "The Gate of Intuitive Insight",  
"i\_ching\_name": "The Gentle",  
"channel\_id": "10-57/20-57/34-57",  
"harmonic\_gate": null,  
"center": "spleen",  
"circuit": "Knowing",  
"astro\_span": {  
"start": { "sign": "Libra", "deg": 15, "min": 7, "sec": 30 },  
"end": { "sign": "Libra", "deg": 20, "min": 45, "sec": 0 }  
},  
"crosses": \[\],  
"notes": "Gate 57 participates in three channels: 10-57, 20-57, 34-57."  
},  
{ "gate": 58, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 59, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 60, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 61, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 62, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 63, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." },  
{ "gate": 64, "status": "TODO", "notes": "Header metadata pending extraction from PF11; do not infer center/circuit/astro without source." }  
\],  
"count": 64  
}

## Ums.schema.channel.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.channel.v1.json","title":"UMS Channel (v1)","type":"object","additionalProperties":false,"required":\["id","name","keynote","from\_center","to\_center"\],"properties":{"id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))\*$","description":"Gate-pair identifier (zero-padded NN-NN), e.g. '31-07'. Multiple pairs allowed with '/': '20-57/34-57/10-57'."},"name":{"type":"string","minLength":1},"keynote":{"type":"string","minLength":1},"from\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"to\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"notes":{"type":\["string","null"\]}}}

## Ums.schema.gate.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.gate.v1.json","title":"UMS Gate (v1)","oneOf":\[{"type":"object","additionalProperties":false,"required":\["gate","status"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"status":{"type":"string","const":"TODO"},"notes":{"type":"string"}}},{"type":"object","additionalProperties":false,"required":\["gate","rave\_title","i\_ching\_name","center","astro\_span"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"rave\_title":{"type":"string","minLength":1},"i\_ching\_name":{"type":"string","minLength":1},"channel\_id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))\*$","description":"Primary channel id(s) for the gate; hyphenated, zero-padded NN-NN; multiple allowed when a gate participates in multiple channels."},"harmonic\_gate":{"description":"Harmonic partner gate; null or string allowed when multiple partners exist.","oneOf":\[{"type":"integer","minimum":1,"maximum":64},{"type":"string"},{"type":"null"}\]},"center":{"description":"Center label (snake\_case canonical).","type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"astro\_span":{"type":"object","additionalProperties":false,"required":\["start","end"\],"properties":{"start":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}},"end":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}}}},"crosses":{"type":"array","items":{"type":"string"},"uniqueItems":true},"notes":{"type":\["string","null"\]}}}\]}

## ums.schema.ums.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.v1.json","title":"Unified Master Schema (UMS v1)","type":"object","additionalProperties":false,"required":\["version","wheel","gates","channels"\],"properties":{"version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+(-\[A-Za-z0-9.\_-\]+)?$"},"wheel":{"type":"object","additionalProperties":false,"required":\["zodiac","hexagrams"\],"properties":{"zodiac":{"type":"object","additionalProperties":false,"required":\["segments","segment\_size\_deg"\],"properties":{"segments":{"const":12},"segment\_size\_deg":{"const":30}}},"hexagrams":{"type":"object","additionalProperties":false,"required":\["segments","segment\_size\_deg"\],"properties":{"segments":{"const":64},"segment\_size\_deg":{"const":5.625}}}}},"gates":{"type":"array","minItems":64,"maxItems":64,"items":{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.gate.v1.json","title":"UMS Gate (v1)","oneOf":\[{"type":"object","additionalProperties":false,"required":\["gate","status"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"status":{"type":"string","const":"TODO"},"notes":{"type":"string"}}},{"type":"object","additionalProperties":false,"required":\["gate","rave\_title","i\_ching\_name","center","astro\_span"\],"properties":{"gate":{"type":"integer","minimum":1,"maximum":64},"rave\_title":{"type":"string","minLength":1},"i\_ching\_name":{"type":"string","minLength":1},"channel\_id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))$","description":"Primary channel id(s) for the gate; hyphenated, zero-padded NN-NN; multiple allowed when a gate participates in multiple channels."},"harmonic\_gate":{"description":"Harmonic partner gate; null or string allowed when multiple partners exist.","oneOf":\[{"type":"integer","minimum":1,"maximum":64},{"type":"string"},{"type":"null"}\]},"center":{"description":"Center label (snake\_case canonical).","type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"astro\_span":{"type":"object","additionalProperties":false,"required":\["start","end"\],"properties":{"start":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}},"end":{"type":"object","additionalProperties":false,"required":\["sign","deg","min","sec"\],"properties":{"sign":{"type":"string","enum":\["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"\]},"deg":{"type":"integer","minimum":0,"maximum":29},"min":{"type":"integer","minimum":0,"maximum":59},"sec":{"type":"integer","minimum":0,"maximum":59}}}}},"crosses":{"type":"array","items":{"type":"string"},"uniqueItems":true},"notes":{"type":\["string","null"\]}}}\]}},"channels":{"type":"array","minItems":36,"maxItems":36,"items":{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"schemas/ums.channel.v1.json","title":"UMS Channel (v1)","type":"object","additionalProperties":false,"required":\["id","name","keynote","from\_center","to\_center"\],"properties":{"id":{"type":"string","pattern":"^(?:(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))(?:/(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\])-(?:0\[1-9\]|\[1-5\]\[0-9\]|6\[0-4\]))$","description":"Gate-pair identifier, e.g. '31-07'. Multiple pairs allowed with '/': '20-57/34-57/10-57'."},"name":{"type":"string","minLength":1},"keynote":{"type":"string","minLength":1},"from\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"to\_center":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"circuit":{"type":\["string","null"\],"enum":\["Knowing","Understanding","Sensing","Defense","Defence","Tribal/Ego","Ego/Tribal",null\]},"notes":{"type":\["string","null"\]}}}},"centers":{"type":"array","items":{"type":"object","additionalProperties":false,"required":\["id"\],"properties":{"id":{"type":"string","enum":\["head","ajna","throat","g\_center","ego","spleen","sacral","solar\_plexus","root"\]},"color":{"type":"string"}}}}}}

## ums.schemas.README

UMS JSON Schemas (JSON Schema 2020-12)

Artifacts:

* ums.schema.channel.json — schema for channel catalog entries  
* ums.schema.gate.json — schema for gate catalog entries (supports full header and TODO placeholder variants)  
* ums.schema.ums.json — umbrella schema for a full UMS bundle (gates \+ channels \+ wheel)

Schema hygiene:

* Each schema sets $schema: [https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema) and a stable $id URL.  
* Title/IDs are aligned to the artifact’s role (e.g., ums.channel.v1.json, ums.gate.v1.json, ums.v1.json).

Validation notes:

* Zero-padded channel IDs. id (and gate channel\_id) require two-digit gate numbers 01..64 in NN-NN form; multiple pairs are allowed with /, e.g., 57-20/57-34/10-57.  
* Angles are modeled inside a sign; deg 0–29, min/sec 0–59.  
* Circuits permit both spellings Defense/Defence and the tribal label Tribal/Ego (also Ego/Tribal) as seen in the sources.

Reference math (grounded by the books you provided):

* 64 equal hexagrams tile 360° → 5° 37′ 30″ per gate; 6 lines per gate → 56′ 15″ per line.

Wheel constants appear in ums.schema.ums.json as: {"zodiac":{"segments":12,"segment\_size\_deg":30},"hexagrams":{"segments":64,"segment\_size\_deg":5.625}}.

How to use (AJV example):

* ajv \-s ums.schema.gate.json \-d ums.catalog.gates.json  
* ajv \-s ums.schema.channel.json \-d ums.catalog.channels.json

— Generated: 2025-10-28T18:38:46.050554Z

# Appendix B — Channel ID normalization (informative)

Purpose. QA aid for catalog builders and vendor normalization tests. This appendix illustrates the identity rule and sorting discipline for channel IDs. The normative home for channel identity is §2.1 (Channels), and topology invariants are defined in §3.2. No schemas or payload bytes live here.

Rule (titles-only restatement)

* Channels are unordered edges between two gates.  
* Store the ID in min→max, zero-padded NN-NN form with gates in 01..64.  
* Arrays treated as sets MUST be deduplicated and ASCII-sorted by channel\_id.

  ## B.1 Before → After (normalization examples)

| Input (as received) | Normalized channel\_id |
| ----- | ----- |
| 57-20 | 20-57 |
| 8-1 | 01-08 |
| 34-10 | 10-34 |
| 43-23 | 23-43 |
| 3-60 | 03-60 |
| 12-22 | 12-22 (already canonical) |
| 10-10 | invalid (same gate twice is not a channel) |

  ## B.2 Sorting examples (arrays-as-sets)

Before (unordered, duplicates possible): \["57-20","01-08","10-34","23-43","10-34"\]

Normalize \+ dedupe \+ ASCII-sort → After: \["01-08","10-34","20-57","23-43"\]

Notes

* Normalization is performed before any catalog or evidence emission.  
* Duplicates or malformed identities fail closed (see §3.1 JSON Schema validation and §3.2 Graph coherence checks).

  ## B.3 Evidence hooks (Index titles/paths only)

Register the following artifacts in the Evidence Index (Governance, Appendix D) to demonstrate orientation and topology invariants:

* audit/gates/topology/orientation\_demo.txt — before/after normalization examples  
* audit/gates/topology/degree\_check.log — observed gate degrees \+ pass/fail  
* audit/gates/topology/multiplicity\_vector.log — observed center-pair multiplicities \+ pass/fail

  # Appendix C — Governed artifact record types (records-only)

Titles and paths only. One-line purpose each. Bytes live outside PF12; this appendix governs names and paths only.

manifest — Freeze-Pack manifest; frozen inputs (path, sha256, size); sole source for release identity. (path: catalog/manifest.json)

freeze\_pack\_manifest — Evidence copy of the Freeze-Pack manifest for audits. (path: artifacts/math/freeze\_pack\_manifest.json)

release\_id — Canonical release\_id derived from manifest bytes. (path: artifacts/math/release\_id.txt)

release\_id\_recompute — Recompute log proving sha256(canonical\_manifest\_bytes) equals release\_id. (path: artifacts/math/release\_id\_recompute.log)

checksums\_audit — Per-entry sha256/size/presence verification report. (path: artifacts/math/checksums\_audit.log)

manifest\_snapshot — Names-only snapshot (release\_id, manifest sha256, entry count, CI timestamp). (path: artifacts/math/manifest\_snapshot.json)

human\_index — Human Evidence Index; titles/paths only; 1:1 with machine mirror. (path: docs/evidence/INDEX.json)

human\_index\_hash — Hash sentinel for the Human Evidence Index (sha256 of INDEX.json). (path: docs/evidence/INDEX.sha256)

mirror\_jsonl — Machine Evidence Index; JSONL; 1:1 parity with the human index. (path: artifacts/evidence\_index.jsonl)

seeds — Magic-10 seeds catalog; admin-only; exactly 10 entries; manifest-listed frozen input. (path: catalog/magic10\_seeds.json)

db\_fingerprint — Normalized database DDL snapshot with sha256; proves schema identity. (path: artifacts/db/ddl\_fingerprint.json)

db\_grants\_snapshot — Least-privilege grants snapshot for runtime principal. (path: artifacts/db/grants.txt)

db\_schema\_check — Search\_path/schema echo (names-only posture). (path: artifacts/db/check\_schema.txt)

db\_constraints\_check — Constraints posture snapshot. (path: artifacts/db/check\_constraints.txt)

db\_partition\_plan — Partition plan definition/proof. (path: artifacts/db/partition\_plan.txt)

db\_conn\_env\_selection — Connection env selection order proof. (path: artifacts/db/conn\_env\_selection.log)

db\_rw\_smoke\_log (optional) — Minimal read/write smoke probe. (path: artifacts/db/db\_rw\_smoke.log)

registry\_report — Names-only configuration registry proof (no secrets). (path: artifacts/registry/registry\_report.json)

config.magic10 — Magic-10 configuration snapshot; governed config artifact capturing Magic-10 order, per-category caps (integer bounds), and seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256) under closed rails; canonical JSON; manifest-listed as evidence only (not a pack input). (path: artifacts/thresholds/magic10\_config.json)

config.band\_edges — Band-edges configuration snapshot; governed config artifact capturing band names, edges, clamp behavior, rounding mode, version, and a source pointer back to math/thresholds.json; canonical JSON; generated under closed rails. (path: artifacts/thresholds/band\_edges.json)

epic018.config.acceptance\_map — HDE-EPIC018 config acceptance map; PF09-style mapping from config tasks (e.g., HDE-CALC004, HDE-CALC004.3, HDE-CALC004.7) to artifact keys, config-related tokens, and tests; canonical JSON; used to prove that each config task is wired to existing artifacts and real tests only. (path: audit/EPIC-018\_config\_acceptance\_map.json)

config\_bundle.fe — Typed frontend config bundle; governed config artifact produced under closed rails from the Magic-10 and band-edges config artifacts plus the registry report; canonical JSON; includes a sources block that records path/sha256/size\_bytes for each upstream governed artifact; used by client-facing components as a read-only projection. (path: JSON file under artifacts/config\_bundles/)

config\_bundle.be — Typed backend config bundle; governed config artifact produced under closed rails from the same governed config artifacts and registry report; canonical JSON; includes full topology slices (channels/centers/domains/alias\_policy) and a sources block with path/sha256/size\_bytes for each upstream governed artifact; used by internal engine/adapter code as a read-only projection. (path: JSON file under artifacts/config\_bundles/)

endpoint\_catalog\_file — Authoritative Endpoint Catalog (records-only) plus checksum. (paths: docs/ENDPOINTS\_CATALOG.json, docs/ENDPOINTS\_CATALOG.json.sha256)

endpoint\_catalog\_snapshot — Reader JSON success-endpoints snapshot; proves success envelopes. (path: artifacts/reader/endpoints\_snapshot.json)

endpoint\_env\_gate\_proof — Env-gating proof (headers-only); shows non-prod entries unreachable in prod. (path: artifacts/proofs/endpoints\_env\_gate\_proof.log)

a7\_headers\_get — A7 GET (200) headers snapshot (headers-only). (path: artifacts/proofs/success\_get.txt)

a7\_headers\_head — A7 HEAD (200) headers snapshot (headers-only). (path: artifacts/proofs/success\_head.txt)

a7\_headers\_304 — A7 304 headers snapshot (headers-only; omits Content-Type and Content-Length). (path: artifacts/proofs/success\_304.txt)

a7\_headers\_writers\_errors — Writers/errors posture headers snapshot (no-store, no ETag). (path: artifacts/proofs/success\_writers\_errors.txt)

reader\_success\_proof — Composite proof JSON for GET/HEAD/304 on Catalog route. (path: artifacts/proofs/reader\_success\_get\_head\_304.json)

artifacts/proofs/ops\_refusal\_proof.txt — ops refusal proof capturing why rails were closed and how the system declined a run under closed-rails posture.

a7.success\_encoding\_invariance — Reader A7 encoding-invariance proof that identity (ETag) and effective length are stable across accepted Accept-Encoding values. (path: artifacts/proofs/success\_encoding\_invariance.txt)

start\_command\_capture — Effective start command captured as bytes \+ sha256. (path: artifacts/proofs/start\_command\_capture.txt)

env\_inventory — Environment inventory (names-only) proving consulted keys. (path: artifacts/proofs/env\_inventory.json)

env\_pins — Environment pins snapshot used for specific runs (LC\_ALL, LANG, TZ). Does not satisfy DETERMINISM\_ENV\_PINS\_OK; the canonical determinism env pins surface is audit/gates/determinism/env\_pins.log (see §8.3.3). (path: artifacts/proofs/env\_pins.txt)

validator\_outputs — Validator outputs proving config sanity. (path: artifacts/proofs/validator\_outputs.json)

internal\_version\_get\_head — /internal/version ops identity proof (headers/body/conditionals). (path: artifacts/proofs/internal\_version\_get\_head.json)

compat.conjunction.identity\_hash — Primary governed compat-closure artifact for explicit conjunction identity-hash capture; bytes MUST match the canonical AB compat bytes for the same pair. (path: artifacts/compat/identity\_hash.txt)

conjunction.writer.write\_readback — Governed writer log for explicit conjunction writer readback proof. Records `writer_invalid_status`, `writer_success_type`, and `writer_error_type` for the current family state. (path: artifacts/writer/conjunction\_write\_readback.log)

conjunction.writer.summary — Governed writer summary snapshot for explicit conjunction writer typed-envelope posture. Records `writer_success_typed_envelope` and `writer_error_typed_envelope` for the current family state. (path: artifacts/writer/conjunction\_writer\_summary.json)

cli.showcompat.stdout — Canonical stdout capture for `hde showcompat` (LF-terminated; no CRLF; non-empty on success; success has empty stderr). (path: artifacts/cli/showcompat/stdout.json)

cli.showcompat.stdout\_sha256 — SHA-256 sidecar for the showcompat stdout capture bytes. (path: artifacts/cli/showcompat/stdout.json.sha256)

cli\_showcompat\_args — Names-only capture arguments/env snapshot used by the deterministic generator (no secrets). (path: artifacts/cli/showcompat/args.json)

cli\_showcompat\_generator — Deterministic producer tool for EPIC022 D2 showcompat capture artifacts. (path: tools/cli/generate\_showcompat\_artifacts.py)

cli.conjunction.pair\_ab — Conjunction-mode pair artifact (AB ordering). (path: artifacts/audit/cli/pair.json)

cli.conjunction.pair\_ba — Conjunction-mode pair artifact (BA ordering). (path: artifacts/audit/cli/pair\_ba.json)

cli.conjunction.showcompat\_ab — Conjunction-mode showcompat artifact (AB ordering). (path: artifacts/audit/cli/showcompat\_ab.json)

cli.conjunction.showcompat\_ba — Conjunction-mode showcompat artifact (BA ordering). (path: artifacts/audit/cli/showcompat\_ba.json)

cli.conjunction.output\_ab — Conjunction-mode showcompat output artifact (AB ordering). (path: artifacts/cli/out.json)

cli.conjunction.output\_ba — Conjunction-mode showcompat output artifact (BA ordering). (path: artifacts/cli/out\_ba.json)

cli.conjunction.abba\_sidecar — Conjunction-mode ABBA sidecar proof artifact tying AB and BA outputs. (path: artifacts/cli/abba\_sidecar.json)

cli.guard.emitter\_symbol\_proof — Governed emitter allow-list proof artifact for the CLI serializer-coupling surface. (path: artifacts/cli/guards/emitter\_symbol\_proof.txt)

cli.guard.serializer\_grep — Serializer grep guard output log for the CLI serialization guardrail. (path: artifacts/cli/guards/serializer\_grep\_guard.log)

cli\_showcompat\_two\_run — Two-run identity log for showcompat. (path: artifacts/cli/showcompat/two\_run\_identity.log)

cli\_showcompat\_abba — AB↔BA byte-diff for showcompat (expected empty). (path: artifacts/cli/showcompat/abba.diff)

cli.showcompat.reader\_cli\_parity — Governed Reader↔CLI parity bytes artifact for the CLI serializer-coupling surface. (path: artifacts/cli/reader\_cli\_parity.bytes)

preimage\_recompute — Log proving sha256(preimage\_bytes) equals idempotence\_hash. (path: artifacts/cli/showcompat/preimage\_recompute.log)

cli\_parity\_ab — CLI/SDK parity artifact (A→B). (path: artifacts/cli/ab.json)

cli\_parity\_ba — CLI/SDK parity artifact (B→A). (path: artifacts/cli/ba.json)

cli\_parity\_summary — CLI/SDK parity summary. (path: artifacts/cli/summary.json)

catalog\_schema\_validation — Catalog schema validation report. (path: artifacts/catalog/catalog\_schema\_validation.log)

domain\_closure\_report — Domain closure report. (path: artifacts/catalog/domain\_closure\_report.log)

topology\_coherence\_report — Topology coherence report. (path: artifacts/topology/topology\_coherence\_report.log)

arrays\_as\_sets\_report — Arrays-as-sets canonicalization report. (path: artifacts/canonical/arrays\_as\_sets\_report.log)

canonical\_json\_check — Canonical JSON gate check log. (path: audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson)

canonicalization\_compare — Canonical JSON gate compare log. (path: audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson)

json\_gate\_structured\_record (optional) — Canonical JSON gate structured record (canonical JSON). (path: audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json)

evidence\_index\_snapshot — Evidence index snapshot artifact (single-home gate-family surface). (path: audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json)

topology\_orientation\_demo — Orientation demo transcript and helper reports used as the exemplar for path-proof validation and topology invariants. (paths: audit/gates/topology/orientation\_demo.txt, audit/gates/topology/degree\_check.log, audit/gates/topology/multiplicity\_vector.log)

env\_matrix\_snapshot — Runtime environment matrix (names-only; capture). (path: artifacts/runtime/env\_matrix.snapshot.json)

env\_matrix\_failure — Runtime environment matrix failure envelope (frozen failure). (path: artifacts/runtime/env\_matrix.failure.json)

runtime.env\_connectivity — Retained bridge-era runtime-connectivity snapshot; record type `historical_bridge_evidence`; historical integrity and nonclaims only. (path: artifacts/runtime/env\_connectivity.snapshot.json)

db\_bridge.adapter\_selection.snapshot — Retained bridge-era adapter-selection snapshot; record type `historical_bridge_evidence`; not current fallback or provider-selection evidence. (path: artifacts/db\_bridge/adapter\_selection.snapshot.json)

db\_bridge.provider\_parity — Retained bridge-era provider-parity proof; record type `historical_bridge_evidence`; not current parity or bridge-availability evidence. (path: artifacts/db\_bridge/provider\_parity.proof.json)

epic032.pr04.env\_connectivity\_nondev\_failure — Retained bridge-era non-dev failure capture; record type `historical_bridge_evidence`; not current transport evidence. (path: artifacts/runtime/env\_connectivity.nondev\_failure.json)

epic032.pr04.ops01.provider\_parity\_closure\_decision — Retained non-claiming EPIC032 OPS evidence; record type `epic032_pr04_ops_evidence`. It MUST NOT establish current bridge support, QA PASS, PF09 status movement, epic closure, or acceptance-token satisfaction. (path: audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json)

bodygraph\_source\_selection — Source selection snapshot (names-only; no PII). (path: artifacts/bodygraph/source\_selection.snapshot.json)

bodygraph\_invariance\_ab — Current source-invariance v2 A→B primary; key `bodygraph.source_invariance.ab`; schema `bodygraph.source_invariance.run.v2`. (path: artifacts/bodygraph/source\_invariance/ab.json)

bodygraph\_invariance\_ba — Current source-invariance v2 B→A primary; key `bodygraph.source_invariance.ba`; schema `bodygraph.source_invariance.run.v2`. (path: artifacts/bodygraph/source\_invariance/ba.json)

bodygraph\_invariance\_summary — Current source-invariance v2 summary; key `bodygraph.source_invariance.summary`; schema `bodygraph.source_invariance.summary.v2`. (path: artifacts/bodygraph/source\_invariance/summary.json)

bodygraph\_invariance\_run\_schema — Closed JSON Schema 2020-12 for source-invariance run primaries; key `bodygraph.source_invariance.schema.run.v2`. (path: schemas/bodygraph\_source\_invariance.run.v2.json)

bodygraph\_invariance\_summary\_schema — Closed JSON Schema 2020-12 for the source-invariance summary; key `bodygraph.source_invariance.schema.summary.v2`. (path: schemas/bodygraph\_source\_invariance.summary.v2.json)

bodygraph\_release\_bindings — Schema-version-1 BodyGraph release binding with the exact source-selection, source-invariance-summary, and refresh-policy binding set; key `epic038.pr01.bodygraph_release_bindings`. (path: artifacts/bodygraph/release\_bindings.json)

presenter.bodygraph.json\_canon\_compare — Canonical four-row shared Presenter-history JSONL; sole current key for this path. (path: artifacts/presenter/json\_canon\_compare.log)

epic038.pr04.presenter\_db\_bridge\_compare — Retained historical DB/bridge Presenter receipt; not current bridge or BodyGraph release-binding evidence. (path: artifacts/presenter/hde\_epic038\_pr04\_db\_bridge\_compare.json)

epic038.pr04.presenter\_db\_bridge\_compare\_schema — Retained historical schema for the DB/bridge Presenter receipt; schema ID `presenter.db_bridge_compare.v1`. (path: schemas/presenter\_db\_bridge\_compare.v1.json)

epic038\_pr05\_mapped\_cache\_evidence — Bounded configured-v2 mapped-cache primary record type for the eight `epic038.pr05.v2_mapped_cache.*` evidence keys. (paths: artifacts/bodygraph/v2\_mapped\_cache/\*)

epic038\_pr05\_schema — Mapped-cache transcript and manifest schema record type. (paths: schemas/bodygraph\_v2\_mapped\_cache\_transcript.v1.json, schemas/bodygraph\_v2\_mapped\_cache\_manifest.v1.json)

hde.ddl\_identity\_projection.v1 — Shared projection-only DDL identity contract. (path: engine/db/ddl\_identity\_projection.py)

epic038\_pr06r\_direct\_db\_selection — Current direct-only selection record type; key `epic038.pr06r.direct_db_selection`. (path: artifacts/runtime/direct\_db\_selection.snapshot.json)

epic038\_pr06r\_schema — Direct-selection schema record type; key `epic038.pr06r.direct_db_selection_schema`. (path: schemas/hde\_epic038\_direct\_db\_selection.v1.json)

epic038\_ops03\_text — OPS-03 command and exit-code record type. (paths: audit/ops/hde-epic038/ops-03/commands.txt, audit/ops/hde-epic038/ops-03/exit\_code.txt)

epic038\_ops03\_log — OPS-03 stdout and stderr record type. (paths: audit/ops/hde-epic038/ops-03/stdout.log, audit/ops/hde-epic038/ops-03/stderr.log)

epic038\_ops03\_env\_presence — OPS-03 environment-presence record type. (path: audit/ops/hde-epic038/ops-03/env\_presence.json)

epic038\_ops03\_db\_posture — OPS-03 direct read-only database-posture record type. (path: audit/ops/hde-epic038/ops-03/db\_posture\_summary.json)

epic038\_ops03\_nonclaims — OPS-03 nonclaims record type. (path: audit/ops/hde-epic038/ops-03/nonclaims.json)

epic038\_ops03\_result — OPS-03 result-summary record type. (path: audit/ops/hde-epic038/ops-03/result\_summary.json)

epic038\_ops03\_validation — OPS-03 validation-receipt record type. (path: audit/ops/hde-epic038/ops-03/validation\_receipt.json)

epic038\_ops03\_checksum — OPS-03 checksum-ledger record type. (path: audit/ops/hde-epic038/ops-03/checksums.sha256)

epic038\_ops03\_schema — OPS-03 schema record type for authorization, environment-presence, database-posture, nonclaims, result-summary, validation-receipt, and failure-receipt contracts. (paths: schemas/hde\_epic038\_ops03\_\*.v1.json)

historical\_bridge\_evidence — Historical-integrity record type for retained bridge-era and HDE-EPIC038 OPS-01 rows; not current transport, parity, fallback, OPS PASS, or token evidence. (paths include artifacts/db\_bridge/\*\*, bridge-era runtime and Presenter loci, and audit/ops/hde-epic038/ops-01/\*\*)

hde.release\_attestation.v1 — Tracked success-contract schema for externally emitted final release attestations. (path: schemas/hde\_release\_attestation.v1.json)

hde.release\_attestation.failure.v1 — Tracked failure-contract schema for externally emitted release-attestation failures. (path: schemas/hde\_release\_attestation\_failure.v1.json)

close\_pack\_report — EPIC close-out report (scope, tokens PASS roster, merged SHAs). (path pattern: audit/EPIC-\<NNN\>\_close\_report.md)

close\_pack\_manifest — Close-pack manifest (artifact keys, sha256, size). (path pattern: audit/EPIC-\<NNN\>\_MANIFEST.json)

sbom\_cyclonedx (optional) — Software Bill of Materials (CycloneDX) with hash. (paths: sbom/cyclonedx.json, sbom/cyclonedx.json.sha256)

cli\_preview\_stdout — Admin preview stdout (LF-terminated narrative text; no ANSI). (path: artifacts/cli/narrative/stdout.txt)

cli\_preview\_sidecar — Admin preview sidecar (ids-only; canonical JSON; no prose). (path: artifacts/cli/narrative/sidecar.json)

narratives\_coverage\_10x4 — Router coverage table (10 categories × 4 bands). (path: audit/gates/narratives/keys\_10x4.table.json)

epic032.pr01.router\_key\_table\_10x4 — HDE-EPIC032 PR-01 router coverage table for the 10-category by 4-band supported matrix. Current token posture carries `JSON_CANONICAL_CHECK_OK` only unless `NARR_REGISTRY_CLOSURE_OK` is later admitted by HDE-Governance or a live Build Notes addendum. (path: audit/gates/narratives/keys\_10x4.table.json)

epic032.pr02.registry\_diff — HDE-EPIC032 PR-02 canonical registry diff artifact for narrative manifest changes. Current token posture may carry `JSON_CANONICAL_CHECK_OK`. (path: audit/gates/narratives/registry.diff.json)

epic032.pr02.pack\_identity — HDE-EPIC032 PR-02 pack identity evidence proving `pack_sha = sha256(canonical manifest bytes)` and same-bytes two-run identity. Current token posture may carry `TWO_RUN_IDENTITY_OK`. (path: audit/gates/narratives/pack\_identity.txt)

epic032.pr02.doc\_deltas — HDE-EPIC032 PR-02 Doc-Delta posture artifact for narrative registry diffing, Doc-Delta binding, pack identity, and evidence indexing. Current token posture may carry `DOC_DELTA_PRESENT_OK`. (path: audit/docdeltas/hde-epic032\_doc\_deltas.md)

# Appendix D — Stateless JSON QA artifacts \[Speculative\]

Status: Speculative — accepted future design, not yet wired.

This appendix canonically defines stateless JSON artifact families for a future no-DB QA mode, as described in HDE-Build Notes Addendum 11\.

These artifacts are not required for current acceptance until a dedicated epic defines concrete paths and schemas.

## D.1 Scope

This appendix describes the intended artifact families for a stateless (no-DB) QA mode:

* A canonical BodyGraph export JSON for single-chart QA.  
* A canonical compat export JSON for compatibility QA.  
* An optional composite run-bundle artifact that groups per-run JSON exports and proof metadata.

This appendix does not fix concrete paths or full JSON schemas.

Those will be defined by a future epic and then drained into this appendix as normative detail.

Process, CLI surfaces, and CI flows for stateless QA remain single-homed in:

* HDE-CLI-API-Vendor-Ref  
* HDE-Mechanics Guide  
* Glow QA Guide  
* HDE-Phased Epics

  ## D.2 Artifact families (design, not yet wired)

  ### D.2.1 BodyGraph export JSON

A canonical JSON document representing a single BodyGraph, suitable for round-trip QA without access to the backing database.

Informal expectations:

* Includes the birth/event inputs needed to reconstruct the chart.  
* Encodes the derived BodyGraph topology (centers, gates, channels, splits).  
* Uses stable identifiers consistent with the catalogs defined elsewhere in PF canon.

Exact field names, nesting, and allowed value ranges are intentionally deferred to a future epic.

### D.2.2 Compat export JSON

A canonical JSON document representing the compatibility view for one or more charts (for example, relationships or composites) in a form that can be evaluated by stateless tools.

Informal expectations:

* Mirrors the compat structures already used by the engine.  
* Is sufficient to replay compat scoring and bands in a stateless QA harness.

No precise JSON shape is fixed in this appendix.

### D.2.3 Run-bundle artifact

An optional composite artifact that groups:

* One or more BodyGraph export JSON documents.  
* Any corresponding compat export JSON documents.  
* Minimal metadata required to replay a QA run (for example: tool/version identifiers, rails posture, references to evidence artifacts).

This concept is recorded here to give future work a canonical home for its schema.

Current PF canon does not require this artifact for acceptance.

## D.3 Normative status and gating

Until a dedicated epic defines concrete JSON schemas and paths:

* These artifact families are not referenced by any acceptance token.  
* No CI job, QA checklist, or governance rule may treat their presence or absence as a gate.  
* Any prototype implementation MUST be clearly marked as experimental and SHOULD reference:  
  * this appendix  
  * the corresponding entry in HDE-Build Notes

Once schemas and paths are finalized in a future epic:

* This appendix will be updated with full canonical detail (paths and schemas).  
* Relevant PF documents will reference this appendix as the single home for stateless JSON QA artifact definitions.

