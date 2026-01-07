# Live QA Planning Guide — HDE-EPIC023

## Scope recap

QA must be able to prove (with evidence artifacts) that:

* **EPIC023 acceptance scaffolds are present and structurally coherent**: `docs/acceptance_map_epic023.json` and `audit/qa/hde-epic023/token_evidence_matrix.md` exist at canonical paths, parse cleanly, and do not contain placeholder bindings.
* **EPIC023 uses only the canonical token roster** (no aliases, no “non-token” promoted to token), and token names match the governance registry exactly.
* **Acceptance artifacts do not bind tokens to `*.path_proof.txt` files as primary evidence** (path-proofs may exist but must be referenced via Mirror `proof_anchor`, not treated as primary evidence).
* **Acceptance-map viability and alignment are proven by artifacts**: the EPIC023 viability log exists and is non-empty, and the EPIC023 acceptance-alignment validator passes.
* **Evidence Index/Mirror integrity is intact**: Index ↔ Mirror parity holds, mirror schema check passes, and the topology orientation demo is coherent with the current Index/Mirror state.
* **The governed evidence surfaces referenced by EPIC023’s tokens exist and are valid**, including determinism env pins, sanity pipeline log, canonical JSON gate logs, and internal `/internal/version` two-run identity evidence family.
* **Doc-delta posture and closure posture are satisfied**: the EPIC023 doc-delta draft exists (non-placeholder), the PF23 consult capture exists, and the EPIC close-pack artifacts exist with the required QA rails section and correct key-output pointers.

## Clarifying questions

1. **Does `audit/qa/hde-epic023/evidence_index_snapshot.json` exist in-repo, and if not, what artifact replaced it?** (Required by the Implementation Plan; not established in PF-canon and not found in PF10.)
2. **Does `audit/gates/canonical_json/canonical_json.gate.json` exist in-repo, and is it intended to be indexed/mirrored as governed evidence?** (Required by the Implementation Plan; not established in PF-canon and not found in PF10.)

## Deliverables inventory

### D01 — EPIC023 Acceptance Map

* **Purpose:** Defines which acceptance tokens apply to EPIC023 and what primary evidence artifacts they bind to.
* **Classification:** Proven-existing
* **Path/name:**

  * `docs/acceptance_map_epic023.json`
  * `docs/acceptance_map_epic023.json.path_proof.txt`
    **Basis:** PF14 canonizes the acceptance-map location; PF10 records EPIC023 acceptance-map wiring.
* **Content requirements:**

  * Parseable JSON (canonical JSON discipline).
  * Contains **only** governance-valid token names.
  * Includes the **EPIC023 token roster** (the 8 tokens listed in PF10’s EPIC023 roster note).
  * Evidence bindings reference **primary evidence artifacts** (not `*.path_proof.txt`).
  * No placeholder / “TBD” evidence bindings once concrete governed evidence exists.
* **PASS proof facts:**

  * No token entry uses an evidence path ending in `.path_proof.txt`.
  * No token name `REALITY_AUDIT_OK` appears anywhere.
  * The eight EPIC023 tokens are all present (names must match governance registry exactly).
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §37.2 (acceptance scaffold locations; “no path-proof as primary evidence”).
  * PF04 — HDE-Governance (token registry; names-only validity rule).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.13 (token binding + acceptance map), Addendum 2.14 (close-pack manifest key_outputs include acceptance map).

---

### D02 — EPIC023 Token-to-Evidence Matrix

* **Purpose:** Provides a reviewable matrix mapping each acceptance token to its owning PF canon and the evidence artifacts / QA logs / CI checks used to prove it.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/qa/hde-epic023/token_evidence_matrix.md`
  * `audit/qa/hde-epic023/token_evidence_matrix.md.path_proof.txt`
    **Basis:** PF14 canonizes the matrix location; PF12 specifies minimum columns; PF10 records EPIC023 matrix wiring.
* **Content requirements:**

  * Markdown table with **at least** these columns (in this order):
    `token_name | owner_pf | evidence_artifacts | qa_root_logs | ci_tests_jobs`
  * One row per EPIC023 token (no duplicates).
  * `owner_pf` uses PF titles-only references (not filenames).
  * `evidence_artifacts` lists **primary** artifact paths (not path-proof paths).
  * No placeholder strings remain for implemented tokens.
* **PASS proof facts:**

  * Header row includes all required columns.
  * Exactly the EPIC023 token roster is present (no extra token rows; no missing token rows).
  * No row lists a `*.path_proof.txt` file under `evidence_artifacts`.
* **Canon touchpoints:**

  * PF12 — HDE-Schemas and Artifacts, §8.17.4 (minimum columns for `token_evidence_matrix.md`).
  * PF14 — HDE-Mechanics Guide, §37.2 (acceptance scaffolds; token name validity; no path-proof as primary evidence).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.13 (final token bindings + matrix), Addendum 2.3 (EPIC023 canonical token roster note).

---

### D03 — EPIC023 Acceptance Map Viability Log

* **Purpose:** Machine-produced viability report proving the acceptance map + matrix are usable and not empty / broken.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/qa/hde-epic023/acceptance_map_viability.log`
  * `audit/qa/hde-epic023/acceptance_map_viability.log.path_proof.txt`
    **Basis:** PF12 defines this ledger artifact; PF10 records it as implemented for EPIC023.
* **Content requirements:**

  * Plaintext log (no ANSI).
  * Non-empty.
  * Contains a clear end-of-log summary (unambiguous overall result for viability).
  * References (at minimum) the acceptance map path and token matrix path as inputs or context.
* **PASS proof facts:**

  * File exists and is non-empty.
  * The final ~10 lines include a clear viability summary line (human reviewer can interpret PASS vs FAIL without inference).
* **Canon touchpoints:**

  * PF12 — HDE-Schemas and Artifacts, §8.17.4 (viability log is a required QA ledger artifact).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.13 (adds viability log + path-proof + mirror update).

---

### D04 — EPIC023 Acceptance Alignment Validator Test

* **Purpose:** CI-safe validator proving acceptance artifacts are aligned (token names valid, no path-proof-as-primary, evidence paths governed and index/mirror-resolved).
* **Classification:** Proven-existing
* **Path/name:**

  * `tests/qa/test_epic023_acceptance_alignment.py`
    **Basis:** PF10 records this validator as implemented and tied to EPIC023 acceptance posture.
* **Content requirements:**

  * Pytest test module that loads EPIC023 acceptance map and token matrix.
  * Enforces (at minimum):

    * no evidence binding points to `*.path_proof.txt`
    * token names match governance registry exactly
    * governed evidence paths resolve through Index/Mirror with proof anchors as applicable
  * Must be CI-safe (deterministic, import-safe; no environment-only behavior).
* **PASS proof facts:**

  * The QA run captures a step log showing pytest completion with **exit code 0** for this test module.
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §37.2 (CI-safe scaffold checks; no path-proof as primary evidence; token name validity).
  * PF19 — Glow QA Guide, §4.4.5 (step log header + PASS semantics for recording the run).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.11 (adds validator), Addendum 2.12 (implements alignment and closes spec holes).

---

### D05 — QA Step Logs Manifest

* **Purpose:** Single manifest enumerating QA step logs for the run, with strict status semantics and traceability.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/qa/hde-epic023/qa_step_logs_manifest.json`
  * `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt`
    **Basis:** PF12 and PF19 define the manifest location and schema requirements.
* **Content requirements:**

  * Canonical JSON (compact; one trailing LF).
  * Required top-level fields: `schema`, `epic_id`, `run_id`, `steps`.
  * Each `steps[]` entry includes: `check_id`, `status`, `path`, `started_at_utc`, `ended_at_utc`, `tool` (with optional `notes`).
  * `status` uses only the allowed vocabulary.
* **PASS proof facts:**

  * JSON parses; `schema == "hde.qa.step_logs_manifest.v1"`.
  * Every `steps[].path` points to an existing non-empty primary step log.
  * No unknown top-level keys; no unknown per-step keys.
* **Canon touchpoints:**

  * PF19 — Glow QA Guide, §4.4.3 (manifest schema + status vocabulary), §4.4.5 (status semantics).
  * PF12 — HDE-Schemas and Artifacts, §8.17.2 (manifest location), §8.17.4 (canonical JSON discipline for ledger artifacts).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.13 (acceptance artifact set includes step log manifest), Addendum 2.14 (manifest referenced as key output).

---

### D06 — Primary QA Step Logs

* **Purpose:** Per-check step logs that prove each QA check ran and provide decisive PASS vs FAIL evidence.
* **Classification:** QA-created
* **Path/name:** QA-created under **audit/** (must live under `audit/qa/hde-epic023/` and be referenced by D05’s `steps[].path`).
* **Content requirements:**

  * Non-empty plaintext.
  * Begins with the required step-log header fields:
    `check_id`, `started_at_utc`, `ended_at_utc`, `status`, `tool`, `source_paths`, `notes`
  * Records enough output to justify the status (e.g., exit codes, decisive result lines).
  * Does not contain secrets.
* **PASS proof facts:**

  * Header `status: PASS` for each required check.
  * Header timestamps present and UTC format.
  * The body includes a decisive success indicator for that check (human reviewer can decide PASS without inference).
* **Canon touchpoints:**

  * PF19 — Glow QA Guide, §4.4.4 (primary step logs required), §4.4.5 (header fields + statuses).
  * PF12 — HDE-Schemas and Artifacts, §8.17.3 (primary step logs location rules and non-empty requirement).
* **PF10 linkage:** PF10 linkage: Not found.

---

### D07 — Codespaces Snapshot

* **Purpose:** Reproducibility record for the QA environment (required for Codespaces runs).
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json`
  * `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt`
    **Basis:** PF12 defines this artifact and schema; PF19 requires it for Step-0 in Codespaces.
* **Content requirements:**

  * JSON with required keys: `schema`, `created_at_utc`, `git_ref`, `git_sha`, `repo_dirty`, `os`, `python`.
  * Optional keys allowed: `pip_freeze`, `poetry_lock_hash`, `pipfile_lock_hash`, `requirements_hash`, `tool_versions`, `notes`.
  * Rejects unknown keys (no extras).
* **PASS proof facts:**

  * `schema == "hde.qa.codespaces_snapshot.v1"`.
  * `git_sha` present and non-empty; `repo_dirty` is `true|false` (boolean).
  * No unknown keys in the object.
* **Canon touchpoints:**

  * PF12 — HDE-Schemas and Artifacts, §8.17.5 (codespaces snapshot schema).
  * PF19 — Glow QA Guide, §14.4.3 (Step-0 codespaces snapshot required).
* **PF10 linkage:** PF10 linkage: Not found.

---

### D08 — QA Doc Deltas Capture

* **Purpose:** QA ledger capture explicitly stating doc deltas (or explicitly stating none).
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/qa/hde-epic023/00_meta/doc_deltas.md`
  * `audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt`
    **Basis:** PF12 defines this ledger artifact under epic QA meta.
* **Content requirements:**

  * Non-empty markdown.
  * Explicitly lists doc deltas, or explicitly states there are no doc deltas.
  * Uses titles-only PF references when citing canon.
  * Secret-free.
* **PASS proof facts:**

  * Reviewer can determine “doc deltas present” vs “no doc deltas” without interpreting intent.
* **Canon touchpoints:**

  * PF12 — HDE-Schemas and Artifacts, §8.17.4 (doc_deltas.md is a required QA ledger artifact).
  * PF10 — HDE-Build Notes, Addendum 2.5 (doc-delta surfaces discipline for EPIC023 posture).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.9 (mentions QA meta doc deltas).

---

### D09 — PF23 Consult Capture

* **Purpose:** Captures the PF23 consult used to ensure “reality audit” posture is handled correctly (non-token unless governance says otherwise).
* **Classification:** Proven-existing
* **Path/name:** `audit/qa/hde-epic023/00_meta/pf23_consult.md`
* **Content requirements:**

  * Non-empty markdown.
  * Includes which PF23 sections were consulted (titles-only + section anchors).
  * Records the consult conclusions that affect EPIC023 artifacts (tokens remain governance-only; consult note is evidence-only).
  * Secret-free.
* **PASS proof facts:**

  * The consult note clearly distinguishes “token” vs “evidence-only” posture.
* **Canon touchpoints:**

  * PF23 — Reality Audits (consult source).
  * PF10 — HDE-Build Notes, Addendum 2.10 (adds consult capture note for EPIC023).
  * PF10 — HDE-Build Notes, Addendum 2.3 (EPIC023 token roster excludes `REALITY_AUDIT_OK`).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.10.

---

### D10 — EPIC023 Doc-Delta Draft

* **Purpose:** Staging document enumerating required doc updates for EPIC023 (non-placeholder; used in closure posture).
* **Classification:** Proven-existing
* **Path/name:** `audit/docdeltas/hde-epic023_doc_deltas.md`
* **Content requirements:**

  * Non-empty markdown.
  * Contains concrete deltas (no “TBD/placeholder” deltas).
  * References target PF docs by title and section anchors.
  * Secret-free.
* **PASS proof facts:**

  * At least one concrete doc delta is present, *or* an explicit statement that no doc deltas are required (no ambiguity).
* **Canon touchpoints:**

  * PF10 — HDE-Build Notes, Addendum 2.5 (doc-delta surfaces; staging under `audit/docdeltas/`).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.9 (adds doc-delta draft), Addendum 2.14 (close report points to doc-delta draft).

---

### D11 — EPIC023 Close Report

* **Purpose:** Human-readable closure artifact proving QA rails and acceptance posture were satisfied for the epic.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/EPIC-023_close_report.md`
  * `audit/EPIC-023_close_report.md.path_proof.txt`
* **Content requirements:**

  * Includes the required section header: **`QA Rails — Open/Close (Final PR)`**.
  * Includes an “Acceptance tokens (names-only)” section listing the EPIC023 token roster.
  * References the EPIC023 acceptance scaffolds and viability log by exact path.
  * References the EPIC023 doc-delta draft by exact path.
* **PASS proof facts:**

  * The string `QA Rails — Open/Close (Final PR)` appears exactly.
  * The eight-token roster appears as names-only (no aliases; no extra tokens).
  * The close report includes the canonical paths for: acceptance map, token matrix, viability log, doc delta draft.
* **Canon touchpoints:**

  * PF06 — Epic Process Guide, §5.1.2 (close report required sections/posture).
  * PF14 — HDE-Mechanics Guide, §37.2 (canonical close-pack paths).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.14 (close report added with required header and token list).

---

### D12 — EPIC023 Close Pack Manifest

* **Purpose:** Machine-readable close-pack manifest listing key outputs (paths) used for closure and review.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/EPIC-023_MANIFEST.json`
  * `audit/EPIC-023_MANIFEST.json.path_proof.txt`
* **Content requirements:**

  * Canonical JSON (compact; one trailing LF).
  * Includes `epic_id`.
  * Includes `key_outputs` and lists the EPIC023 key-output paths (at minimum: acceptance map, token matrix, viability log, QA step logs manifest, doc-delta draft).
* **PASS proof facts:**

  * `key_outputs` contains the canonical paths for the EPIC023 acceptance scaffold set.
  * JSON parses with no unknown keys (reviewer can locate key outputs unambiguously).
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §37.2 (canonical close-pack paths).
  * PF10 — HDE-Build Notes, Addendum 2.14 (manifest `key_outputs` pointers included).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.14.

---

### D13 — Human Evidence Index

* **Purpose:** Titles/paths registry of governed evidence artifacts; must include EPIC023 governed artifacts.
* **Classification:** Proven-existing
* **Path/name:**

  * `docs/evidence/INDEX.json`
  * `docs/evidence/INDEX.json.path_proof.txt`
* **Content requirements:**

  * Parseable JSON.
  * Includes entries for EPIC023 governed artifacts (acceptance map, token matrix, viability log, close pack artifacts).
  * No payload bytes (titles/paths only).
* **PASS proof facts:**

  * Index contains references (string match is sufficient) to:
    `docs/acceptance_map_epic023.json`, `audit/qa/hde-epic023/token_evidence_matrix.md`, `audit/qa/hde-epic023/acceptance_map_viability.log`, `audit/EPIC-023_close_report.md`, `audit/EPIC-023_MANIFEST.json`.
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §37.2 (Human Index home).
  * PF12 — HDE-Schemas and Artifacts, §8.3.1 (index + sentinel + mirror core artifacts).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.16 (evidence index/mirror/path proofs updated in revalidation sweep).

---

### D14 — Evidence Index Hash Sentinel

* **Purpose:** Hash sentinel proving `INDEX.json` bytes are stable and checkable.
* **Classification:** Proven-existing
* **Path/name:**

  * `docs/evidence/INDEX.sha256`
  * `docs/evidence/INDEX.sha256.path_proof.txt`
* **Content requirements:**

  * Single-line sha256 format (no extra lines).
  * References `INDEX.json` on the same line.
* **PASS proof facts:**

  * Contains a 64-hex sha and includes `INDEX.json` on the line.
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §37.2 (sentinel home).
  * PF12 — HDE-Schemas and Artifacts, §8.3.2 (sentinel artifact).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.16.

---

### D15 — Machine Evidence Mirror

* **Purpose:** Records-only mirror of all governed artifacts, including proof anchors to path-proofs (schema-enforced).
* **Classification:** Proven-existing
* **Path/name:**

  * `artifacts/evidence_index.jsonl`
  * `artifacts/evidence_index.jsonl.path_proof.txt`
* **Content requirements:**

  * JSONL; one JSON object per line; no blank lines.
  * Fixed field set/order; rejects unknown keys.
  * Contains a record for each governed artifact referenced in the Human Index.
  * Each record includes a valid `proof_anchor` pointing to a sibling `*.path_proof.txt` transcript.
* **PASS proof facts:**

  * Mirror contains entries for EPIC023 governed artifacts (as in D13).
  * For each such entry, `proof_anchor` points to an existing path-proof transcript.
* **Canon touchpoints:**

  * PF12 — HDE-Schemas and Artifacts, §8.3 (mirror schema), §8.6 (path-proof transcripts).
  * PF14 — HDE-Mechanics Guide, §37.4 (mirror discipline + required fields/order).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.16.

---

### D16 — Topology Orientation Demo Report

* **Purpose:** Gate report proving orientation coherence against current Index/Mirror state.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/gates/topology/orientation_demo.txt`
  * `audit/gates/topology/orientation_demo.txt.path_proof.txt`
* **Content requirements:**

  * Plaintext, no ANSI.
  * Contains a clear summary indicating whether orientation is coherent (stale vs current).
* **PASS proof facts:**

  * Report contains an unambiguous “OK”/pass result line.
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §1.3 (orientation demo check posture; report path).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.16 (orientation demo + path-proof updated).

---

### D17 — Determinism Environment Pins Log

* **Purpose:** Proves determinism pins are set and recorded under canonical evidence surfaces.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/gates/determinism/env_pins.log`
  * `audit/gates/determinism/env_pins.log.path_proof.txt`
* **Content requirements:**

  * Plaintext, no ANSI.
  * Includes the required pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
  * Secret-free.
* **PASS proof facts:**

  * Those three pins appear explicitly in the file.
* **Canon touchpoints:**

  * PF09 — HDE-Build Checklist, §0.5.2 (env pins file + required lines + indexing/mirroring requirements).
  * PF14 — HDE-Mechanics Guide, §9.4 (requires pins for `/internal/version` evidence captures).
* **PF10 linkage:** PF10 linkage: Not found.

---

### D18 — Sanity Pipeline Log

* **Purpose:** Proves the sanity pipeline executed and passed with required metadata.
* **Classification:** Proven-existing
* **Path/name:**

  * `artifacts/sanity/sanity.log`
  * `artifacts/sanity/sanity.log.path_proof.txt`
* **Content requirements:**

  * Plaintext, no ANSI.
  * Contains: `PASS`, `checker_version:`, `started_at_utc:`, `finished_at_utc:`, `target_commit_sha:`.
* **PASS proof facts:**

  * All required fields appear and the status is `PASS`.
* **Canon touchpoints:**

  * PF09 — HDE-Build Checklist, §0.2.5 (sanity log requirements + indexing/mirroring requirements).
* **PF10 linkage:** PF10 linkage: Not found.

---

### D19 — Canonical JSON Gate Check Log

* **Purpose:** Proves canonical JSON checks ran and passed, stored at the canonical path.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/gates/canonical_json/json_canonical_check.log`
  * `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`
* **Content requirements:**

  * Plaintext, no ANSI.
  * Contains PASS result and identifies checked scope (at least at a summary level).
* **PASS proof facts:**

  * Contains an unambiguous PASS result line.
  * Located under the canonical directory `audit/gates/canonical_json/` (not a legacy/mistyped path).
* **Canon touchpoints:**

  * PF09 — HDE-Build Checklist, §0.3.1 (canonical JSON gate outputs + path proofs + indexing/mirroring).
  * PF10 — HDE-Build Notes, Addendum 2.2 (canonical JSON gate directory naming rule).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.2.

---

### D20 — Canonical JSON Gate Compare Log

* **Purpose:** Proves canonicalization compare report exists at the canonical surface and is indexed/mirrored consistently.
* **Classification:** Proven-existing
* **Path/name:**

  * `audit/gates/canonical_json/json_canon_compare.log`
  * `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`
* **Content requirements:**

  * Plaintext; one-line report posture (LF-terminated).
  * No ANSI; secret-free.
* **PASS proof facts:**

  * File exists, is non-empty, and ends with exactly one trailing LF.
* **Canon touchpoints:**

  * PF09 — HDE-Build Checklist, §0.3.1 (compare log requirements).
  * PF10 — HDE-Build Notes, Addendum 2.4 (canonical compare artifacts must reuse canon surfaces).
* **PF10 linkage:** PF10 — HDE-Build Notes, Addendum 2.4; Addendum 2.16 (compare log + path-proof + mirror/index updated).

---

### D21 — `/internal/version` Evidence Family for Two-Run Identity

* **Purpose:** Proves two-run identity (and required transport/body posture) for `/internal/version`, satisfying EPIC023’s two-run identity acceptance requirement.
* **Classification:** Proven-existing
* **Path/name:**
  Directory `artifacts/ops/internal_version/` containing (at minimum):

  * `headers_get.txt`
  * `headers_head.txt`
  * `body_get.json` and `body_get.sha256`
  * `headers_cond_if_none_match.txt`
  * `headers_cond_if_modified_since.txt`
  * `request_chain_manifest.json`
  * `two_run_identity.log`
    *(Each file should have a sibling `*.path_proof.txt` transcript if governed/indexed.)*
* **Content requirements:**

  * Captures demonstrate GET/HEAD posture (no-store; no ETag; `Content-Type` correct; HEAD parity).
  * `body_get.json` is LF-terminated and conforms to the fixed six-key identity body posture.
  * `two_run_identity.log` records two-run identity and includes coupling proof (release_id match) and env pins reference.
  * `request_chain_manifest.json` is deterministic and secret-free.
* **PASS proof facts:**

  * `headers_get.txt` demonstrates **no-store** and **no ETag**.
  * `two_run_identity.log` contains an explicit two-run identity assertion (byte-equality) and references env pins.
* **Canon touchpoints:**

  * PF14 — HDE-Mechanics Guide, §9.4 (required `/internal/version` evidence files and posture).
  * PF09 — HDE-Build Checklist, §0.5.2 (env pins required evidence surface referenced by captures).
* **PF10 linkage:** PF10 linkage: Not found.

---

### D22 — Canonical JSON Gate Record

* **Purpose:** Structured gate record for canonical JSON checks (required by the Implementation Plan).
* **Classification:** **Unproven — Requires repo/tooling confirmation before QA plan finalization.**
* **Path/name:**

  * `audit/gates/canonical_json/canonical_json.gate.json`
  * `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`
* **Content requirements:**

  * Parseable canonical JSON.
  * Contains an unambiguous overall status and references the corresponding canonical JSON gate logs.
* **PASS proof facts:**

  * Status indicates PASS and points to the canonical check/compare log paths.
* **Canon touchpoints:** PF10/canon basis not found for this filename.
* **PF10 linkage:** PF10 linkage: Not found.

---

### D23 — EPIC023 Evidence Index Snapshot Artifact

* **Purpose:** Snapshot artifact intended to capture Index/Mirror identity state for EPIC023 (required by the Implementation Plan).
* **Classification:** **Unproven — Requires repo/tooling confirmation before QA plan finalization.**
* **Path/name:** `audit/qa/hde-epic023/evidence_index_snapshot.json`
* **Content requirements:**

  * Parseable JSON.
  * Captures enough identity facts to let a reviewer compare Index/Mirror state deterministically (e.g., sha256/size/timestamps for Index/Mirror and/or proof transcripts).
* **PASS proof facts:**

  * Snapshot contains unambiguous hashes/identity fields for the evidence index and mirror.
* **Canon touchpoints:** PF10/canon basis not found for this artifact.
* **PF10 linkage:** PF10 linkage: Not found.

---

## Evidence posture notes

* QA Plan and QA step reviews must be able to decide **PASS vs REMEDIATION NEEDED** using only:
  **the approved QA Plan + step artifacts (logs/manifests/snapshots) + PF canon**, with **PF10 as the implementation record** (superseding where it speaks).
* **Evidence print is required at acceptance time:** reviewers must list (names-only where tokens are involved) the deliverables produced/verified, the **exact paths used in that run**, and the decisive **PASS proof facts** observed for each deliverable.
