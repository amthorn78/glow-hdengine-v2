# HDE-EPIC024 Remediation S1 — Token Registry Discovery (PR-01)

## 1. Registry locations and schema summary

**Registry sources located (authoritative vs derived):**

1) **Canonical token registry (authority):**
   - `docs/pfcanon/PF04-Canon-HDE-Governance-v1.8.6.md` — HDE-Governance §2.0 Acceptance Tokens is described as the single-home Token Registry. This is the canonical authority for acceptance token names and semantics. (See PF10 addendum summary in §2.1 for authority rules.)
   - **Format:** Markdown; registry content appears as a text roster in §2.0. (No machine schema in repo; registry is human-readable canon.)

2) **Registry export used in repo QA (derived/consumer):**
   - `reports/qa_acceptance_tokens.json`
   - **Format/schema shape:** JSON object with top-level `tokens` array. Each token entry is an object with:
     - `name` (string token name)
     - `scope` (string)
     - `feature_label` (string)
     - `code_locations` (array of `{path, summary}` objects)
     - `tests_and_ci` (array of `{path, summary}` objects)
     - `evidence_artifacts` (array of `{path, summary}` objects)
     - `notes` (string, optional)
   - **Status:** Used as a local registry export; not the canonical authority but explicitly referenced as the registry locus in EPIC024 QA planning and checks.

**Acceptance artifacts (not registries, but token consumers):**
- `docs/acceptance_map_epic024.json` (JSON object with `epic_id` and `tokens[]` entries containing `name`, `owner_pf`, `status`, `evidence_titles`).
- `audit/qa/hde-epic024/token_evidence_matrix.md` (Markdown table with token rows and columns like `token_name`, `owner_pf`, `evidence_artifacts`, `ci_tests_jobs`, `qa_root_logs`, `status`, `notes`).

## 2. Authority mapping (what is authoritative for acceptance evidence)

- **Canonical authority:** PF04 (HDE-Governance) is the single-home registry for acceptance tokens; PF10 §2.1 reiterates that acceptance artifacts must use canonical names from PF04.
- **Repo validation logic:** `tests/qa/test_epic023_acceptance_alignment.py` loads tokens from PF04 (via regex extraction) and merges in tokens from `reports/qa_acceptance_tokens.json` if present; it then validates that acceptance map and token matrix tokens are registry-valid.
- **Acceptance-map generation (EPIC024):** `tools/qa/run_hde_epic024_harness.py` is the harness that writes `docs/acceptance_map_epic024.json` and the token matrix as governed outputs.

**Authority chain summary:** PF04 defines canonical names → acceptance maps/token matrices must use those names (PF10 §2.1) → repo QA validations (e.g., EPIC023 acceptance alignment test) treat PF04 + `reports/qa_acceptance_tokens.json` as registry sources for validation.

## 3. Canonical tokens and deprecated spellings (and alias mappings)

**Canonical token universe (registry export / repo-local registry list):**
```
AB_BA_PARITY_OK
BYTES_OK
CI_CHECK_FINAL_LF_OK
CI_CHECK_MIRROR_SCHEMA_OK
CLI_HELP_OK
CLI_NO_ALT_JSON_OK
CLI_READER_PARITY_OK
CLI_SHOWCOMPAT_CANON_OK
CLI_STDOUT_LF_OK
COMPOSITE_ABBA_IDENTITY_OK
CONFIG_GEN_OK
DOC_DELTA_PRESENT_OK
EMIT_PATH_NO_JSON_DUMPS_OK
ENV_GUARD_IMPORT_OK
EVIDENCE_INDEX_HASH_OK
EVIDENCE_INDEX_UPDATED_OK
EVIDENCE_PATHS_VALIDATED_OK
EVIDENCE_PATH_PROOFS_OK
FILE_EQ_CANON_BYTES_OK
INGEST_IDEMPOTENT_OK
INGEST_OK
JSON_CANONICAL_CHECK_OK
LF_OK
MACHINE_MIRROR_UPDATED_OK
MODULE_HELP_OK
PARTITION_PLAN_OK
READER_CLI_BYTE_IDENTITY_OK
SECRETS_OK
SIDE_OK
SINGLE_EMITTER_OK
SIX_KEY_SUCCESS_ENVELOPE_OK
TESTS_PASS_OK
TIEBREAK_TOTAL_ORDER_OK
TWO_RUN_IDENTITY_OK
UNKNOWN_IDS_FAIL_CLOSED_OK
VENDOR_NO_PAYLOAD_LOGGING_OK
VENDOR_RETRY_BACKOFF_OK
```
Source: `reports/qa_acceptance_tokens.json`.

**Deprecated / alternate spellings (explicit from PF10 §2.1):**
- `QA_STEP_LOGS_CONSOLIDATED_OK` (deprecated doc-only alias) → canonical `QA_HARNESS_DISCIPLINE_OK`.

**Alias mappings (deprecated → canonical):**
- `QA_STEP_LOGS_CONSOLIDATED_OK` → `QA_HARNESS_DISCIPLINE_OK`.

> Note: No other alias mapping is determinable from repo-local registry export; only PF10’s explicit alias rule is recorded.

## 4. QA_STEP_LOGS_CONSOLIDATED_OK presence and alias treatment

**Presence in repo artifacts:**
- `docs/acceptance_map_epic021.json` includes the token `QA_STEP_LOGS_CONSOLIDATED_OK`.
- `audit/qa/hde-epic021/token_evidence_matrix.md` includes the same token in the matrix.

**Alias treatment (per PF10 §2.1):**
- `QA_STEP_LOGS_CONSOLIDATED_OK` is explicitly called a deprecated doc-only alias for `QA_HARNESS_DISCIPLINE_OK` and must not be claimed in acceptance artifacts.

## 5. reports/qa_acceptance_tokens.json trace (producers/consumers)

**Existence:**
- File exists at `reports/qa_acceptance_tokens.json` and contains a `tokens` array of token definitions.

**Producer(s):**
- **No explicit in-repo generator or writer found** via searches in `tools/`, `scripts/`, and `tests/` beyond references (see Section 8 for search commands). The file appears to be a checked-in registry export, but the repo does not document a generator in code.

**Consumer(s):**
- `tests/qa/test_epic023_acceptance_alignment.py` loads the file (if present) and merges its token names with PF04 tokens for registry validation.
- `audit/qa/hde-epic024/r5 Live QA Plan HDE-EPIC024.md` uses it as the registry locus for po-006_token_registry_validity.
- `audit/qa/hde-epic024/checks/po-006_token_registry_validity/*` uses it for the po-006 check (inputs and evidence reports).

## 6. po-006_token_registry_validity procedure/spec + runner loci

**Procedure/spec documents located:**
- `audit/qa/hde-epic024/r5 Live QA Plan HDE-EPIC024.md` — PO-006 specifies:
  - Proof obligation: acceptance map tokens must be registry-valid in `reports/qa_acceptance_tokens.json`.
  - Commands to capture tokens using `rg` on the acceptance map and registry export.
  - Primary log header requirements (PASS/FAIL_BEHAVIOR/TOOLING_BLOCKED) and capture pointer append.
  - Requirement to re-run D19_step_logs_manifest after final writes.

- `audit/qa/hde-epic024/checks/po-006_token_registry_validity/HDE-EPIC024_PO-006_FULL_EVIDENCE_REPORT.md` — execution record with token comparison logic, outputs, and final status.

**Runner/implementation loci:**
- **No dedicated script or module found** that implements po-006. The procedure is specified in the QA plan and executed via ad hoc shell/python commands captured in the step log.

## 7. CI entrypoint for po-006_token_registry_validity (file + step name + invoked command + expected outputs + manifest posture)

**CI entrypoint search result:**
- **No CI step found** in `.github/workflows/ci.yml` (or other CI config locations searched) that runs `po-006_token_registry_validity`.

**Expected outputs (per QA plan / step reports):**
- Primary log: `audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log`
- Transcript outputs:
  - `audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt`
  - `audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt`
- Manifest posture:
  - After final writes, D19_step_logs_manifest must be re-run so `audit/qa/hde-epic024/qa_step_logs_manifest.json` and its `.path_proof.txt` reflect the updated check list.

**Unresolved (no CI step name):**
- Because no CI entrypoint is declared in `.github/workflows/ci.yml`, the CI step name and CI command are **unresolved**. See Section 8 for the negative search commands used.

## 8. Search commands used (verbatim, so negatives are auditable)

```
rg -n "token" docs audit reports tools ci scripts
rg -n "epic024|EPIC024|token_evidence_matrix" audit docs reports tools ci scripts
rg -n "token registry|acceptance token|token roster|tokens" docs audit schemas tools reports ci | head -n 200
rg -n "token|alias|deprecated|registry" docs/pfcanon/PF04-Canon-HDE-Governance-v1.8.6.md
rg -n "po-006_token_registry_validity|token_registry_validity|registry_validity" -S .
rg -n "po-006_token_registry_validity" -n audit/qa/hde-epic024/r5\ Live\ QA\ Plan\ HDE-EPIC024.md
rg -n "qa_acceptance_tokens.json" -S .
rg -n "QA_STEP_LOGS_CONSOLIDATED_OK" -S .
rg -n "po-006_token_registry_validity" ci .github .gitlab .circleci -S
rg -n "qa_acceptance_tokens" -S tools scripts tests reports docs audit
rg -n "acceptance_map_epic024.json" tools/qa/run_hde_epic024_harness.py
find audit -name AGENTS.md -print
```
