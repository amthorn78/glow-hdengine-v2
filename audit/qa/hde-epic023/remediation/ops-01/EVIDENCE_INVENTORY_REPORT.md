# Evidence Files Inventory Report
**Generated:** 2026-01-10T22:56:05Z  
**Repository:** glow-hdengine-v2  
**Branch:** main

---

## Executive Summary

This report catalogs all evidence artifacts in the HDE repository, organized by category and governed by the Evidence Index/Mirror system described in AGENTS.md and PF-Canon documentation.

**Total Evidence Artifacts:**
- **322** Path Proof Files (`.path_proof.txt`)
- **107** SHA256 Sidecar Files (`.sha256`)
- **62** Evidence-related files
- **4** INDEX.json files

---

## I. Canonical Evidence Index System

### Primary Artifacts (SoT)

| File | Size | Status | Description |
|------|------|--------|-------------|
| `docs/evidence/INDEX.json` | 44K | ✅ Present | Human-readable evidence index |
| `docs/evidence/INDEX.sha256` | 91B | ✅ Present | INDEX.json integrity proof |
| `artifacts/evidence_index.jsonl` | 95K | ✅ Present | Machine-readable evidence mirror |

**Governance:** These artifacts are maintained by `tools/evidence/update_evidence_index.py` and must never be hand-edited. All governed artifacts require `.path_proof.txt` siblings.

---

## II. EPIC-Specific Evidence

### EPIC-018 (Config Management)
**Location:** `audit/`

| Artifact | Size | Status |
|----------|------|--------|
| `EPIC-018_MANIFEST.json` | - | ✅ + path proof |
| `EPIC-018_close_report.md` | - | ✅ + path proof |
| `EPIC-018_config_acceptance_map.json` | - | ✅ + path proof |

### EPIC-022 (Release Identity)
**Location:** `audit/`, `artifacts/math/`

| Artifact | Size | Status |
|----------|------|--------|
| `EPIC-022_MANIFEST.json` | - | ✅ + path proof |
| `EPIC-022_close_report.md` | - | ✅ + path proof |
| Release identity artifacts | See § Math Artifacts | ✅ |

**Key Evidence:** Freeze-pack manifest (`catalog/manifest.json`), release ID recompute logs, checksums audit.

### EPIC-023 (Remediation 2 - Current)
**Location:** `audit/qa/hde-epic023/`, `docs/`

**Acceptance Artifacts:**
- `docs/acceptance_map_epic023.json` (3.9K) + path proof
- `audit/EPIC-023_MANIFEST.json` (787B) + path proof
- `audit/EPIC-023_close_report.md` (1.6K) + path proof

**Token Evidence:**
- `token_evidence_matrix.md` (3.8K) + path proof
- `acceptance_map_viability.log` + path proof

**QA Check Logs (D01-D18):**
Structure: `audit/qa/hde-epic023/checks/{D##_check_name}/primary.log`

Present checks:
- D01: Acceptance Map
- D02: Token Evidence Matrix
- D03: Acceptance Viability
- D04: Acceptance Alignment Validator
- D05: Step Logs Manifest
- D06: Primary Step Logs
- D07: Codespaces Snapshot
- D08: QA Doc Deltas Capture
- D09: PF23 Consult Capture
- D10: Doc Delta Draft
- D11: Close Report
- D12: Close Pack Manifest
- D13: Human Index
- D14: Index Hash Sentinel
- D15: Machine Mirror
- D16: Orientation Demo ⚠️ (check module missing)
- D17: Env Pins ⚠️ (check module missing)
- D18: Sanity Log ⚠️ (check module missing)

**Meta Artifacts:**
- Codespaces snapshot + path proof
- Doc deltas + path proof
- PF23 consult + path proof

**Remediation Evidence:**
- `remediation/ops-01/ops_transcript.log` (OPS-01 failure capture)

### EPIC-017, EPIC-019, EPIC-020, EPIC-021
**Acceptance Maps:** Present in `docs/` with path proofs  
**QA Evidence:** Segregated in `audit/qa/hde-epic0{17,18,19,20,21}/`

---

## III. Gates Evidence

### Canonical JSON Gate
**Location:** `audit/gates/canonical_json/`

- `canonical_json.gate.json` + path proof (606B)
- `cli_surfaces.log` + path proof (154B)
- `json_canon_compare.log` + path proof (2.3K)
- `json_canonical_check.log` + path proof (2.3K)

### Determinism Gate (D17 target)
**Location:** `audit/gates/determinism/`

- `env_pins.log` + path proof (240B)

### Topology Gate (D16 target)
**Location:** `audit/gates/topology/`

- `orientation_demo.txt` + path proof (115B)

### Auxiliary Gates
**Location:** `audit/gates/aux/`

- Suppression snapshot check + path proof
- Text snapshot check + path proof
- Headers style check
- Provenance echo check
- Route alias check
- Determinism check

---

## IV. Artifact Categories (by top-level directory)

### High-Density Evidence Categories

| Category | Path Proofs | Description |
|----------|-------------|-------------|
| `audit/` | 44 | EPIC manifests, close reports, acceptance maps |
| `epic020/` | 40 | Determinism bundles and manifests |
| `db/` | 21 | Database migrations, partitions, introspection |
| `cli/` | 14 | CLI guards, showcompat captures, parity proofs |
| `ops/` | 14 | /internal/version bundles, rails refusal proofs |
| `bodygraph/` | 9 | Source invariance, AB/BA parity |
| `engine/` | 7 | DB adapter fingerprints, order proofs |
| `presenter/` | 6 | JSON canon compare, preimage recompute |
| `db_bridge/` | 6 | Provider parity, health checks |
| `sampler/` | 5 | ABBA, diversity, two-run identity |

### Zero-Evidence Categories
These categories exist but contain no path proofs:
- `admin/`, `canon/`, `cards/`, `constants/`, `db_discovery/`, `ddl/`, `epic003/`, `epic004/`, `epic007/`, `errors/`, `goldens/`, `hdapi/`, `headers/`, `hotfix/`, `idempotence/`, `identity/`, `live_vendor/`, `m10/`, `math/`, `mech/`, `mvp/`, `prod/`, `provider/`, `reader/`, `redaction/`, `reports/`, `serializer/`, `validation/`

---

## V. Math Artifacts (EPIC-022 Release Identity)

**Location:** `artifacts/math/`

| Artifact | Size | SHA256 Sidecar | Path Proof | Description |
|----------|------|----------------|------------|-------------|
| `release_id.txt` | - | ✅ | ❌ | Single-line release identity hash |
| `release_id_recompute.log` | - | ✅ | ❌ | Recompute validation log |
| `checksums_audit.log` | - | ✅ | ❌ | Checksums audit output |
| `freeze_pack_manifest.json` | - | ✅ | ❌ | Evidence copy of catalog/manifest.json |

**Canonical SoT:** `catalog/manifest.json` (no self-listing, canonical bytes)

**Governed Commands:**
- `python scripts/release_id_recompute.py --check`
- `python ci/checks/check_release_identity.sh`
- `python tools/evidence/run_sanity_pipeline.py`

---

## VI. Sanity Pipeline (D18 target)

**Location:** `artifacts/sanity/`

- `sanity.log` (1.1K) + path proof

**Invocation:** `python tools/evidence/run_sanity_pipeline.py`

---

## VII. QA Evidence by Epic

| Epic Directory | Evidence Count | Key Artifacts |
|----------------|----------------|---------------|
| `hde-epic017/` | - | Step logs, admin artifacts |
| `hde-epic018/` | - | Config QA artifacts |
| `hde-epic019/` | - | Vendor live QA, dev sampler HTTP |
| `hde-epic020/` | - | Determinism bundles (40 path proofs) |
| `hde-epic021/` | - | Token matrix, dedupe runs |
| `hde-epic022/` | - | D3.2 evidence updates, showcompat captures |
| `hde-epic023/` | **54 files** | D01-D18 check logs, token matrix, remediation |
| `compat/` | - | ABBA parity, lints, coverage sweeps |
| `premerge/` | - | Premerge QA checks |

---

## VIII. Notable Evidence Patterns

### Path Proof Siblings
All governed artifacts require a `.path_proof.txt` sibling containing:
- Relative path from repo root
- SHA256 hash
- UTC timestamp
- For mirrors: `mirror_body_sha256` for the self-record

**Convention:** Never hand-edit path proofs. Generated by evidence tooling only.

### SHA256 Sidecars
107 SHA256 sidecars exist for:
- Goldens (reader v1)
- Fixtures (HDAPI normalized/raw)
- Canon checksums
- Narratives catalog
- Admin QA artifacts
- EPIC-specific captures

### Evidence Index Updates
**Workflow (governed):**
1. Run `update_evidence_index.py` (write mode)
2. Run `orientation_demo.py` (write mode)
3. Run `update_evidence_index.py --check`
4. Run `orientation_demo.py --check`
5. Run `ci/checks/check_mirror_schema.sh`

---

## IX. Tools and Scripts

### Evidence Generation
- `tools/evidence/update_evidence_index.py` — Index/Mirror updater
- `tools/evidence/orientation_demo.py` — Topology gate
- `tools/evidence/run_sanity_pipeline.py` — Determinism checks
- `tools/generate_registry_report.py` — Registry report
- `tools/cli/generate_showcompat_artifacts.py` — Showcompat D2 captures

### Evidence Validation
- `ci/checks/check_mirror_schema.sh` — Mirror schema validation
- `ci/checks/check_release_identity.sh` — Release identity gate
- `ci/checks/check_env_pins.sh` — Env pins gate
- `tools/evidence/run_canonical_json_gate.py` — JSON canon gate

### QA Harnesses
- `tools/qa/epic021_qa.py` — EPIC021 QA harness
- `tools/qa/qa_harness.py` — Generic QA framework
- `tools/qa/token_roster_validate.py` — Token validation

---

## X. Current Issues / Blockers

### OPS-01 Failure (HDE-EPIC023 Remediation 2)
**Status:** ❌ FAILED AT S1  
**Root Cause:** Missing check modules
- `hde.qa.check_d16_orientation_demo`
- `hde.qa.check_d17_env_pins`
- `hde.qa.check_d18_sanity_log`

**Evidence Captured:**
- `audit/qa/hde-epic023/remediation/ops-01/ops_transcript.log` (1.5K)

**Next Steps:** DEV must provide check modules before OPS-01 can proceed.

---

## XI. Compliance Status

### AGENTS.md Compliance
- ✅ Evidence Index/Mirror present and governed
- ✅ Path proofs present for governed artifacts
- ✅ No hand-edited evidence detected
- ✅ Canonical tools used for evidence generation
- ⚠️ EPIC023 D16/D17/D18 checks pending (modules missing)

### PF-Canon Compliance
- ✅ PF10 precedence respected (release identity, HDE-Build Notes)
- ✅ PF12 schemas and artifacts aligned
- ✅ PF19 QA guide followed (evidence-first, closed rails)
- ✅ PF20 phased epics tracked with acceptance maps

---

## XII. Evidence Directories

```
./audit/codex/epic011_r17c/evidence
./audit/docs_snapshot/docs/evidence
./codex/out/docs_snapshots/docs/evidence
./docs/evidence (canonical)
./tests/evidence
./tools/evidence
```

---

## XIII. Recommendations

1. **DEV Priority:** Create missing check modules for EPIC023 D16/D17/D18
2. **Evidence Hygiene:** Run `update_evidence_index.py --check` in CI
3. **Path Proof Coverage:** Audit zero-evidence categories for missing proofs
4. **Documentation:** Update evidence generation procedures in PF-Canon
5. **Automation:** Add evidence presence checks to precommit hooks

---

**Report End**
