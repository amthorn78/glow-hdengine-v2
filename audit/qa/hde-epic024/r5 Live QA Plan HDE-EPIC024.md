Front matter
Epic ID: HDE-EPIC024
Plan type: Live QA Plan (PF27)
Plan revision: r5
Date: 2026-01-17 (UTC)
Execution venue: Codespaces (repo-local)
Target environment: dev (repo-local, no prod handshake)
Roles:
PO (executor; runs steps in Codespaces)
QA reviewer (reviews governed evidence artifacts and step logs)
Canon precedence statement (required)
PF10 supersedes where it speaks.
Where PF10 is silent, PF19 governs QA work (evidence posture, step logs, rails discipline).
PF27 governs this plan format and required headings.
Repo reality is determined by the current repo state in Codespaces (files/paths present; repo-local commands available). If a referenced path or command is missing at execution time, the affected step is marked TOOLING_BLOCKED per plan rules and the missing-surface proof is captured in that step’s primary.log.
Canon set (explicit; stable references only)
PF10 — HDE-Build Notes
Addendum 2.1 Acceptance token registry authority + legacy spellings + unregistered tokens
Addendum 2.2 Evidence path binding authority order + Machine Evidence Index mirror home + path-proof naming
Addendum 2.3 Acceptance map path-of-record
Addendum 2.4 Evidence Index snapshot mechanical contract (PASS/FAIL)
Addendum 2.5 Ellipsis Prohibition (template syntax)
Addendum 2.6 PR01: HDE-EPIC024 Review
Addendum 2.7 PR02: HDE-EPIC024 Review
Addendum 2.8 PR03: HDE-EPIC024 Review
Addendum 2.9 PR04: HDE-EPIC024 Review
Addendum 2.10 Docs PR: HDE-EPIC024
PF19 — Glow QA Guide
§3.4.2 Tooling discipline
§3.4.3 Evidence layout
§3.4.6 Step-level Deliverables
§3.4.8 Rails posture
§4.4.4 Step log headers (required fields)
§4.4.5 Status field vocabulary (noting PF27 ownership statement)
PF23 — Reality Audits
§3. Evidence, Indices, and Catalogs (repo surfaces and evidence loci)
PF27 — Canon Plan Templates
§1 Live QA Plan template (this document’s structure)

Scope statement
Epic intent and boundaries (names-only; PF-anchored)
This Live QA Plan verifies EPIC024’s governed QA deliverables and gates across these repo surfaces (names-only):
Epic QA root for EPIC024: audit/qa/hde-epic024


Acceptance map and viability evaluation: docs/acceptance_map_epic024.json and audit/qa/hde-epic024/acceptance_map_viability.log


Canonical JSON gate log: audit/gates/json_gate/canonical/json_gate_check_log.ndjson


Evidence index snapshot: audit/gates/evidence_index_snapshot/evidence_index_snapshot.json


Harness selftest and acceptance ledger outputs: reports/qa_acceptance_tokens.json and audit/qa/hde-epic024/token_evidence_matrix.md


Step logs and step log manifest: audit/qa/hde-epic024/checks/*/primary.log and audit/qa/hde-epic024/qa_step_logs_manifest.json


Close pack artifacts: audit/EPIC-024_MANIFEST.json, audit/EPIC-024_close_report.md, audit/EPIC-024_QA_RCA.md


Doc delta captures: audit/docdeltas/hde-epic024_doc_deltas.md and audit/qa/hde-epic024/00_meta/doc_deltas.md


This plan:
does not modify governed artifacts under docs/ except where explicitly required by the epic and only in governed, reviewed paths;


produces step logs in audit/qa/hde-epic024/checks/ per PF19; and


uses only deterministic command runners explicitly listed in the check blocks; if a runner is not present, the step is marked TOOLING_BLOCKED with an evidence note in the step log.


PF10 Addendum 2.5 prohibits ellipsis tokens in governed outputs. This plan contains no ellipsis tokens.
PF23 anchors
Components and loci this plan touches (names-only; anchored to PF23 evidence loci and repo surfaces):
audit/qa/ epic QA root locus (EPIC024 uses audit/qa/hde-epic024)
audit/gates/* gate loci (canonical JSON, determinism env pins, evidence index snapshot, sanity pipeline)
docs/acceptance_map_epic024.json (acceptance map locus)
docs/evidence/INDEX.json and docs/evidence/INDEX.sha256 (human index and sentinel)
artifacts/evidence_index.jsonl (machine mirror)
artifacts/showcompat/epic024 (showcompat artifacts locus)
artifacts/sampler/epic024 (sampler evidence locus)
artifacts/compare (arrays-as-sets evidence locus)
reports/qa_acceptance_tokens.json (token registry locus)
Environment and rails posture
Determinism pins (canonical pins only)
Pins expected for governed outputs:
LC_ALL=C
LANG=C
TZ=UTC
Primary enforcement and proof for this epic is via the determinism env pins gate evidence (see PO-012 step).
Rails posture (explicit)
Rails posture for this plan:
SAFE_MODE=1
ALLOW_NETWORK=0
APP_ENV=dev
No step in this plan requires network calls.
No VCS workflow content (hard)
This plan contains no git commands and no branch/merge workflow instructions.
PO inputs needed
Codespaces access to the repo workspace.


Ability to open and read files in the Codespaces editor and terminal.


Ability to create governed QA step-log captures under audit/qa/hde-epic024/ (for posture-only steps in this plan).


Evidence posture and directory structure
Epic QA root normalization (required)
Canonical epic QA root (current-state evidence locations):
audit/qa/hde-epic024/ — canonical epic QA root


audit/qa/hde-epic024/checks/ — canonical per-check step logs (PF19) and any per-check capture files referenced by those logs


audit/qa/hde-epic024/qa_step_logs_manifest.json — step log manifest (PF19)


audit/qa/hde-epic024/token_evidence_matrix.md — token ↔ evidence mapping (PF10/PF19)


audit/qa/hde-epic024/acceptance_map_viability.log — acceptance map viability evaluation output


Optional run-local convenience folder (not acceptance binding):
audit/qa/hde-epic024/runs/20260117T000000Z_po/ — optional scratch copies only; do not treat as required deliverables


Step log header expectations (PF19-aligned)
Each check has a primary step log at:
audit/qa/hde-epic024/checks/<check_id>/primary.log


The first line of primary.log MUST be a single-line JSON object with:
check_id (string)


status (PASS / FAIL_BEHAVIOR / FAIL_TOOLING / TOOLING_BLOCKED)


fail_status (string; MUST be "" when status == PASS; else MUST equal status)


command (string; exact command string executed, or N/A if no command applies)


command_provenance (string; describe how the command string was obtained)


captured_env (object)


pf_refs (array of strings)


intended_tokens (array of strings)


claimed_tokens (array of strings)


Note: log_path is a manifest field (audit/qa/hde-epic024/qa_step_logs_manifest.json), not a required field in the primary.log header.
Posture-only steps (PO-006, PO-008, PO-011, PO-017) capture their required evidence into canonical governed locations under audit/qa/hde-epic024/checks/ as specified in their check blocks.
The step log manifest audit/qa/hde-epic024/qa_step_logs_manifest.json references primary step logs via each entry’s log_path.
Mandatory Step‑0 artifacts
Step‑0A — Evidence Root + Session Header (mechanical; no narrative)
Goal:
Confirm the EPIC024 canonical QA root exists and contains the required root artifacts.


Optionally create a run-local convenience folder (not acceptance binding).


Preconditions:
You are in Codespaces at the repo root.


PO actions:
Confirm the canonical EPIC024 QA root exists and contains the required root artifacts:


audit/qa/hde-epic024/qa_step_logs_manifest.json


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt


audit/qa/hde-epic024/acceptance_map_viability.log


audit/qa/hde-epic024/token_evidence_matrix.md


What to look for:
The required root artifacts exist at the canonical paths above.


Required deliverables:
audit/qa/hde-epic024/qa_step_logs_manifest.json


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt


audit/qa/hde-epic024/acceptance_map_viability.log


audit/qa/hde-epic024/token_evidence_matrix.md


Note: If audit/qa/hde-epic024/qa_step_logs_manifest.json bytes change for any reason, audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt must be refreshed after the final write.
PASS criteria:
All required root artifacts exist at their canonical paths.


FAIL criteria:
Any required root artifact missing (FAIL_TOOLING).


Determine rails posture (JSON gate + env pins) (required)
Goal
Determine whether the plan can execute D-check runners.
Preconditions
Step-0A completed.
Ability to run python command runners.
PO actions (commands)
Run the canonical JSON gate:
python tools/evidence/run_canonical_json_gate.py
Run env pins capture:
python tools/evidence/run_env_pins_gate.py
Required outputs (must be produced even if status ultimately FAIL_BEHAVIOR)
audit/gates/json_gate/canonical/json_gate_check_log.ndjson — written by python tools/evidence/run_canonical_json_gate.py
audit/gates/determinism/env_pins.log — written by python tools/evidence/run_env_pins_gate.py
audit/gates/determinism/env_pins.log.path_proof.txt — written by python tools/evidence/run_env_pins_gate.py
Required deliverables (files that must exist)
audit/gates/json_gate/canonical/json_gate_check_log.ndjson
audit/gates/determinism/env_pins.log
audit/gates/determinism/env_pins.log.path_proof.txt
audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log
audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
Verification (confirm outputs exist)
audit/gates/json_gate/canonical/json_gate_check_log.ndjson
audit/gates/determinism/env_pins.log
PASS criteria
Both commands exit 0, and all required deliverables exist at fixed paths.
FAIL criteria
Either command missing or exits nonzero.
Any required deliverable is missing.
Either primary.log missing or header not PASS.
Status vocabulary and gating rules (PF19)
Status vocabulary (must be used verbatim in primary.log header status field):
PASS
FAIL_BEHAVIOR
FAIL_TOOLING
TOOLING_BLOCKED
Gating rules
A D-check runner missing or failing due to environment is FAIL_TOOLING (if command exists and executed).
A plan-defined deterministic runner not available (no command/path exists) is TOOLING_BLOCKED.
A content/logic mismatch (acceptance token mismatch, invalid schema, etc.) is FAIL_BEHAVIOR.

Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)
Goal: Confirm doc-delta capture artifacts exist before executing proof obligations that rely on them.
PO actions:
Confirm the following doc-delta artifacts exist:
audit/docdeltas/hde-epic024_doc_deltas.md
audit/qa/hde-epic024/00_meta/doc_deltas.md
Required deliverables:
audit/docdeltas/hde-epic024_doc_deltas.md (fixed location; governed candidate)
audit/qa/hde-epic024/00_meta/doc_deltas.md (fixed location; governed under epic QA root)
PASS criteria:
Both doc-delta files exist.
FAIL criteria:
Either doc-delta file is missing (capture failure; record as FAIL_TOOLING for PO-011 later).
Step‑0C — Prod handshake (identity-only) when target is prod-like
Not applicable: target environment is dev repo-local; no prod-like handshake is required.

Runbook Check Matrix

Every check_id is unique and is also the directory name under audit/qa/hde-epic024/checks/.
 This is the canonical mapping from guide steps to repo-local evidence artifacts.
PO vs CI/QA-only execution:
PO executes every check_id listed in this matrix during Live QA.


CI/QA-only preconditions (not executed by the PO in this run): none.


Class 2 steps are PO-executed because Live QA is a PO-run runbook in a repo-local dev environment; safety constraints: SAFE_MODE=1 and ALLOW_NETWORK=0 (see Step‑0A).

check_id
step name (guide)
step type
step_class
expected status semantics
PO command(s)
primary evidence path
minimal deliverables set
PASS criteria
FAIL criteria
PF anchors
D02_canonical_json_gate
PO-001
D-check
class 2 — internal functional/determinism
PASS iff canonical JSON gate passes and emits a stable log at a fixed path; FAIL_TOOLING otherwise
Run python tools/evidence/run_canonical_json_gate.py
audit/gates/json_gate/canonical/json_gate_check_log.ndjson
python tools/evidence/run_canonical_json_gate.py; audit/gates/json_gate/canonical/json_gate_check_log.ndjson; audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log
Exit 0; gate log exists; PASS header
Missing runner/log; nonzero exit; FAIL_TOOLING or FAIL_BEHAVIOR header
PF19 §3.4.1
D05_arrays_as_sets
PO-002
D-check
class 2 — internal functional/determinism
PASS iff arrays-as-sets check passes and emits a stable report at a fixed path; FAIL_TOOLING otherwise
Run python tools/evidence/run_arrays_as_sets_check.py
audit/gates/arrays_as_sets/arrays_as_sets_report.md
python tools/evidence/run_arrays_as_sets_check.py; audit/gates/arrays_as_sets/arrays_as_sets_report.md; audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log
Exit 0; report exists; PASS header
Missing runner/report; nonzero exit; FAIL_TOOLING or FAIL_BEHAVIOR header
PF19 §3.4.3
D09_generate_evidence_index_snapshot
PO-003
D-check
class 2 — internal functional/determinism
PASS iff evidence index snapshot is generated and stored at a fixed path; FAIL_TOOLING otherwise
Run python tools/evidence/run_evidence_index_snapshot.py
audit/gates/evidence_index_snapshot/evidence_index_snapshot.json
python tools/evidence/run_evidence_index_snapshot.py; audit/gates/evidence_index_snapshot/evidence_index_snapshot.json; audit/qa/hde-epic024/checks/D09_generate_evidence_index_snapshot/primary.log
Exit 0; snapshot exists; PASS header
Missing runner/snapshot; nonzero exit; FAIL_TOOLING or FAIL_BEHAVIOR header
PF19 §3.4.4
D13_acceptance_map_viability
PO-004
D-check
class 2 — internal functional/determinism
PASS iff acceptance map viability check passes and emits a stable log at a fixed path; FAIL_TOOLING otherwise
Run python tools/evidence/run_acceptance_map_viability_check.py
audit/qa/hde-epic024/acceptance_map_viability.log
python tools/evidence/run_acceptance_map_viability_check.py; docs/acceptance_map_epic024.json; audit/qa/hde-epic024/acceptance_map_viability.log; audit/qa/hde-epic024/checks/D13_acceptance_map_viability/primary.log
Exit 0; viability log exists; PASS header
Missing runner/log; nonzero exit; FAIL_TOOLING or FAIL_BEHAVIOR header
PF19 §3.4.5
D14_harness_selftest
PO-005
D-check
class 2 — internal functional/determinism
PASS iff harness selftest passes and required artifacts exist at fixed paths; FAIL_TOOLING otherwise
Run python tools/evidence/run_harness_selftest.py
audit/gates/harness_selftest/harness_selftest.log
python tools/evidence/run_harness_selftest.py; audit/gates/harness_selftest/harness_selftest.log; audit/qa/hde-epic024/token_evidence_matrix.md; audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log
Exit 0; artifacts exist; PASS header
Missing runner/artifacts; nonzero exit; FAIL_TOOLING or FAIL_BEHAVIOR header
PF19 §3.4.6
po-006_token_registry_validity
PO-006
posture-only
class 1 — ops-only
PASS iff every token in acceptance map appears in registry; FAIL_BEHAVIOR on mismatch; FAIL_TOOLING on missing inputs
Run rg captures per check block; compare token sets; write primary.log header
audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log
docs/acceptance_map_epic024.json; reports/qa_acceptance_tokens.json; audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt; audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt; audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log
Token sets match; PASS header
Missing inputs/evidence ⇒ FAIL_TOOLING; missing token ⇒ FAIL_BEHAVIOR
PF10 Addendum 2.8; PF19 §3.4.6
D19_step_logs_manifest
PO-007
D-check
class 2 — internal functional/determinism
PASS iff qa step logs manifest exists, is path-proven, and referenced logs exist; FAIL_TOOLING otherwise
None required (review fixed artifacts and referenced paths)
audit/qa/hde-epic024/qa_step_logs_manifest.json
audit/qa/hde-epic024/qa_step_logs_manifest.json; audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt; audit/qa/hde-epic024/checks/; audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log
Manifest+path_proof exist; referenced logs exist; PASS header
Missing manifest/path_proof; missing referenced logs ⇒ FAIL_TOOLING
PF19 §3.4.2
po-008_bootstrap_status_classification
PO-008
posture-only
class 1 — ops-only
PASS iff bootstrap status classification test passes; FAIL_BEHAVIOR if test fails; FAIL_TOOLING if runner/test missing
Run python -m pytest -q tests/test_bootstrap_status_classification.py and record outcome
audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
tests/test_bootstrap_status_classification.py; audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
pytest exit 0; PASS header
Missing test/pytest ⇒ FAIL_TOOLING; failing test ⇒ FAIL_BEHAVIOR
PF19 §3.4.8
D16_close_pack
PO-009
D-check
class 2 — internal functional/determinism
PASS iff close pack artifacts exist and are internally consistent, and QA RCA exists
Run python tools/evidence/run_close_pack.py; verify audit/EPIC-024_QA_RCA.md exists
audit/EPIC-024_MANIFEST.json
audit/EPIC-024_MANIFEST.json; audit/EPIC-024_close_report.md; audit/EPIC-024_QA_RCA.md; audit/qa/hde-epic024/checks/D16_close_pack/primary.log
Close pack artifacts exist; PASS header; QA RCA exists
Missing artifacts/log ⇒ FAIL_TOOLING; inconsistency ⇒ FAIL_BEHAVIOR
PF19 §3.4.9; PF19 §3.4.10
po-011_doc_delta_capture
PO-011
posture-only
class 1 — ops-only
PASS iff doc delta capture is consistent across loci and content is complete; FAIL_BEHAVIOR on mismatch/incomplete; FAIL_TOOLING on missing files
Validate audit/docdeltas/hde-epic024_doc_deltas.md vs audit/qa/hde-epic024/00_meta/doc_deltas.md; record PASS/FAIL_BEHAVIOR
audit/docdeltas/hde-epic024_doc_deltas.md
audit/docdeltas/hde-epic024_doc_deltas.md; audit/qa/hde-epic024/00_meta/doc_deltas.md; audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
Files exist and match; content complete; PASS header
Missing files ⇒ FAIL_TOOLING; mismatch/incomplete ⇒ FAIL_BEHAVIOR
PF27 §4.2; PF19 §3.4.11
D01_env_pins_gate
PO-012
D-check
class 2 — internal functional/determinism
PASS iff determinism env pins gate passes and required outputs exist at fixed paths; FAIL_TOOLING otherwise
Run python tools/evidence/run_env_pins_gate.py
audit/gates/determinism/env_pins.log
python tools/evidence/run_env_pins_gate.py; audit/gates/determinism/env_pins.log; audit/gates/determinism/env_pins.log.path_proof.txt; audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
Exit 0; log+path_proof exist; PASS header
Missing runner/log/path_proof; nonzero exit ⇒ FAIL_TOOLING or FAIL_BEHAVIOR
PF19 §3.4.11
D03_showcompat_artifacts
PO-013
D-check
class 2 — internal functional/determinism
PASS iff showcompat artifacts are present at fixed paths; FAIL_TOOLING otherwise
Run python tools/evidence/run_showcompat_artifacts.py
artifacts/showcompat/epic024/showcompat_manifest.json
python tools/evidence/run_showcompat_artifacts.py; artifacts/showcompat/epic024/showcompat_manifest.json; artifacts/showcompat/epic024/showcompat_symbols.json; audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log
Exit 0; manifest+symbols exist; PASS header
Missing runner/artifacts; nonzero exit ⇒ FAIL_TOOLING or FAIL_BEHAVIOR
PF19 §3.4.12
D08_cli_guardrail
PO-014
D-check
class 2 — internal functional/determinism
PASS iff CLI guardrail finds 0 hits; FAIL_BEHAVIOR on any hit; FAIL_TOOLING on missing inputs/log
Run python tools/cli/serializer_grep_guard.py
audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log
python tools/cli/serializer_grep_guard.py; cli/main.py; audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log
0 hits; PASS header
Any hit ⇒ FAIL_BEHAVIOR; missing target/log ⇒ FAIL_TOOLING
PF19 §3.4.13
D04_sampler_evidence
PO-015
D-check
class 2 — internal functional/determinism
PASS iff sampler evidence artifacts exist at fixed paths and are internally consistent; FAIL_TOOLING otherwise
None required (review fixed artifacts and primary log)
artifacts/sampler/epic024/sampler_evidence.json
artifacts/sampler/epic024/sampler_evidence.json; artifacts/sampler/epic024/manifest.json; audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log
Evidence+manifest exist; PASS header
Missing artifacts ⇒ FAIL_TOOLING
PF10 Addendum 2.9
D07_sanity_pipeline
PO-016
D-check
class 2 — internal functional/determinism
PASS iff sanity pipeline passes and required outputs exist at fixed paths; FAIL_TOOLING otherwise
Run python tools/evidence/run_sanity_pipeline.py
artifacts/sanity/sanity.log
python tools/evidence/run_sanity_pipeline.py; artifacts/sanity/sanity.log; artifacts/sanity/sanity.log.path_proof.txt; audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log
Exit 0; log+path_proof exist; PASS header
Missing runner/log/path_proof; nonzero exit ⇒ FAIL_TOOLING or FAIL_BEHAVIOR
PF19 §3.4.8
po-017_lowercase_naming
PO-017
posture-only
class 1 — ops-only
PASS iff no non-allowlisted uppercase paths were created by QA steps; FAIL_BEHAVIOR otherwise
Run find scans per check block and record outputs; allowlist out-of-scope docs scan
audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt; audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt; audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt; audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
No uppercase hits; PASS header
Any uppercase hit ⇒ FAIL_BEHAVIOR
PF19 §3.4.17


Check Blocks
CHECK D02_canonical_json_gate: PO-001
Proof obligation: Canonical JSON rules are enforced for all governed records.
Goal:
Execute the canonical JSON gate and verify all governed JSON outputs meet canonical format requirements.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run the canonical JSON gate runner.


Confirm the canonical JSON gate log exists.


Open the D02 primary log and confirm header status PASS.


Commands:
python tools/evidence/run_canonical_json_gate.py
What to look for:
Command exits successfully (exit code 0).


audit/gates/json_gate/canonical/json_gate_check_log.ndjson exists.


D02 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_canonical_json_gate.py (command entrypoint)


audit/gates/json_gate/canonical/json_gate_check_log.ndjson


audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log


PASS criteria:
run_canonical_json_gate.py exits 0.


json_gate_check_log.ndjson exists at audit/gates/json_gate/canonical/json_gate_check_log.ndjson.


D02 primary.log header contains "status":"PASS".


FAIL criteria:
Command missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR depending on error).


json gate log missing (FAIL_TOOLING).


D02 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.1


CHECK D05_arrays_as_sets: PO-002
step_class: class 2 — internal functional/determinism

Proof obligation: Arrays-as-sets logic produces stable diff and report artifacts; drift is detectable.
Goal:
Execute arrays-as-sets check and verify stable report artifact exists and primary log indicates PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run arrays-as-sets check runner.


Confirm arrays-as-sets report exists.


Open D05 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_arrays_as_sets_check.py
What to look for:
Command exits successfully (exit code 0).


audit/gates/arrays_as_sets/arrays_as_sets_report.md exists.


D05 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_arrays_as_sets_check.py (command entrypoint)


audit/gates/arrays_as_sets/arrays_as_sets_report.md


audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log


PASS criteria:
runner exits 0.


arrays_as_sets_report.md exists at audit/gates/arrays_as_sets/arrays_as_sets_report.md.


D05 primary.log header contains "status":"PASS".


FAIL criteria:
runner missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR).


report missing (FAIL_TOOLING).


D05 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.3


CHECK D09_generate_evidence_index_snapshot: PO-003

step_class: class 2 — internal functional/determinism
Proof obligation: Evidence index snapshot exists, is stable, and includes all governed artifacts required for audit reconstruction.
Goal:
Execute evidence index snapshot runner and verify snapshot exists and primary log indicates PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run evidence index snapshot runner.


Confirm evidence_index_snapshot.json exists.


Open D09 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_evidence_index_snapshot.py
What to look for:
Command exits successfully (exit code 0).


audit/gates/evidence_index_snapshot/evidence_index_snapshot.json exists.


D09 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_evidence_index_snapshot.py (command entrypoint)


audit/gates/evidence_index_snapshot/evidence_index_snapshot.json


audit/qa/hde-epic024/checks/D09_generate_evidence_index_snapshot/primary.log


PASS criteria:
runner exits 0.


evidence index snapshot exists at audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.


D09 primary.log header contains "status":"PASS".


FAIL criteria:
runner missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR).


evidence index snapshot missing (FAIL_TOOLING).


D09 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.4


CHECK D13_acceptance_map_viability: PO-004

step_class: class 2 — internal functional/determinism
Proof obligation: Acceptance map is viable and binds correctly to governed evidence outputs.
Goal:
Execute acceptance map viability check and verify viability log exists and primary log indicates PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run acceptance map viability runner.


Confirm acceptance_map_viability.log exists.


Open D13 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_acceptance_map_viability_check.py
What to look for:
Command exits successfully (exit code 0).


audit/qa/hde-epic024/acceptance_map_viability.log exists.


D13 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_acceptance_map_viability_check.py (command entrypoint)


docs/acceptance_map_epic024.json


audit/qa/hde-epic024/acceptance_map_viability.log


audit/qa/hde-epic024/checks/D13_acceptance_map_viability/primary.log


PASS criteria:
runner exits 0.


viability log exists at audit/qa/hde-epic024/acceptance_map_viability.log.


D13 primary.log header contains "status":"PASS".


FAIL criteria:
runner missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR).


viability log missing (FAIL_TOOLING).


D13 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.5


CHECK D14_harness_selftest: PO-005

step_class: class 2 — internal functional/determinism
Proof obligation: Acceptance ledger artifacts exist and are coherent with harness outputs (token matrix, manifest, acceptance map).
Goal:
Execute harness selftest runner and verify harness selftest log exists, token matrix is present, and primary log indicates PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run harness selftest runner.


Confirm harness selftest log exists.


Confirm token evidence matrix exists.


Open D14 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_harness_selftest.py
What to look for:
Command exits successfully (exit code 0).


audit/gates/harness_selftest/harness_selftest.log exists.


audit/qa/hde-epic024/token_evidence_matrix.md exists.


D14 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_harness_selftest.py (command entrypoint)


audit/gates/harness_selftest/harness_selftest.log


audit/qa/hde-epic024/token_evidence_matrix.md


audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log


PASS criteria:
runner exits 0.


harness selftest log exists at audit/gates/harness_selftest/harness_selftest.log.


token evidence matrix exists at audit/qa/hde-epic024/token_evidence_matrix.md.


D14 primary.log header contains "status":"PASS".


FAIL criteria:
runner missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR).


harness selftest log missing (FAIL_TOOLING).


token evidence matrix missing (FAIL_TOOLING).


D14 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.6


CHECK po-008_bootstrap_status_classification: PO-008
step_class: class 1 — ops-only
Proof obligation: Bootstrap status classification is deterministic and produces the same outcome under the plan’s pinned environment posture.
Goal: Prove the bootstrap status classification test can be executed and yields a stable PASS or FAIL_BEHAVIOR result (not TOOLING_BLOCKED).
Preconditions:
Step-0A completed.
Setup:
Ensure the governed output directory exists:
audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/
PO actions:
Confirm the test file exists.
Confirm pytest is available in the current python environment.
Execute the test deterministically and capture its output.
Write or overwrite primary.log so line 1 is a PF27-compliant JSON header reflecting PASS / FAIL_BEHAVIOR / FAIL_TOOLING, and include captured_env keys.
Append an ls -la proof line and a pointer to the captured pytest output in the log body.
Manifest + path_proof rule: after final writes to this step’s primary.log and captures, re-run PO-007 (D19_step_logs_manifest) so the manifest and path_proof reflect the final bytes.
Commands:
mkdir -p audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification
Preconditions (file + pytest availability)
if ! test -f tests/test_bootstrap_status_classification.py; then
python -c 'import json, os; print(json.dumps({"check_id":"po-008_bootstrap_status_classification","status":"FAIL_TOOLING","fail_status":"FAIL_TOOLING","command":"python -m pytest -q tests/test_bootstrap_status_classification.py","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF19 §3.4.8"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
ls -la tests/test_bootstrap_status_classification.py >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log 2>&1 || true
exit 0
fi
python -c 'import pytest' > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_import_check.txt 2>&1
PYTEST_IMPORT_RC="$?"
if test "$PYTEST_IMPORT_RC" -ne 0; then
python -c 'import json, os; print(json.dumps({"check_id":"po-008_bootstrap_status_classification","status":"FAIL_TOOLING","fail_status":"FAIL_TOOLING","command":"python -m pytest -q tests/test_bootstrap_status_classification.py","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF19 §3.4.8"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
printf '%s\n' 'captures:' >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
printf '%s\n' '- audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_import_check.txt' >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
ls -la tests/test_bootstrap_status_classification.py >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log 2>&1 || true
exit 0
fi
Execute proof
python -m pytest -q tests/test_bootstrap_status_classification.py > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_output.txt 2>&1
PYTEST_RC="$?"
if test "$PYTEST_RC" -eq 0; then
python -c 'import json, os; print(json.dumps({"check_id":"po-008_bootstrap_status_classification","status":"PASS","fail_status":"","command":"python -m pytest -q tests/test_bootstrap_status_classification.py","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF19 §3.4.8"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
else
python -c 'import json, os; print(json.dumps({"check_id":"po-008_bootstrap_status_classification","status":"FAIL_BEHAVIOR","fail_status":"FAIL_BEHAVIOR","command":"python -m pytest -q tests/test_bootstrap_status_classification.py","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF19 §3.4.8"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
fi
printf '%s\n' 'captures:' >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
printf '%s\n' '- audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_output.txt' >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
printf '%s\n' '- audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_import_check.txt' >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
ls -la tests/test_bootstrap_status_classification.py >> audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log 2>&1 || true
Required deliverables:
tests/test_bootstrap_status_classification.py
audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log
audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_output.txt
audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/pytest_import_check.txt
What to look for:
pytest_output.txt exists and reflects the executed test run.
primary.log line 1 is valid single-line JSON with status PASS / FAIL_BEHAVIOR / FAIL_TOOLING and captured_env keys present.
PASS criteria:
pytest exits 0 and primary.log header status is PASS.
FAIL criteria:
FAIL_TOOLING: test file missing or pytest import fails.
FAIL_BEHAVIOR: pytest executes and returns nonzero.
PF anchors:
PF19 §3.4.8

CHECK D19_step_logs_manifest: PO-007
step_class: class 2 — internal functional/determinism
Proof obligation: QA step logs exist per step; a manifest reconstructs the event stream and is kept in audit/qa.
Goal:
Confirm the QA step logs manifest exists at canonical location and that step logs are present per manifest entries.


Preconditions:
None beyond Step-0 completion.


Setup:
None.


PO actions:
Confirm audit/qa/hde-epic024/qa_step_logs_manifest.json exists.


Confirm audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt exists.


For each entry, confirm referenced log file exists at audit/qa/hde-epic024/<log_path>.


Commands:
None required (review file existence and referenced paths).


What to look for:
Manifest exists at canonical path and references existing step logs.


Required deliverables:
audit/qa/hde-epic024/qa_step_logs_manifest.json


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt


audit/qa/hde-epic024/checks/ (primary logs referenced by the manifest)


audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log


Note: If audit/qa/hde-epic024/qa_step_logs_manifest.json bytes change for any reason, audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt must be refreshed after the final write.
PASS criteria:
qa_step_logs_manifest.json exists and all referenced logs exist.


FAIL criteria:
manifest missing or any referenced log missing (FAIL_TOOLING).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.2


CHECK po-006_token_registry_validity: PO-006
step_class: class 1 — ops-only
Proof obligation: Acceptance tokens in docs/acceptance_map_epic024.json are registry-valid in reports/qa_acceptance_tokens.json.
Goal: Ensure every acceptance token used in the acceptance map is a known, registry-defined token and is spelled exactly, to avoid phantom passes.
Preconditions
Step-0A completed.
Setup
Ensure the governed output directory exists:
audit/qa/hde-epic024/checks/po-006_token_registry_validity/
PO actions
Run the capture commands below (they write outputs directly to fixed governed paths).
Compare the sets. Every acceptance token used in the map must appear in the registry list.
Write / overwrite audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log so that:
line 1 is a PF27-compliant JSON header (see “Step log header expectations”)
status is PASS if sets match; FAIL_BEHAVIOR if mismatch; TOOLING_BLOCKED if required inputs missing.
Manifest + path_proof rule: after final writes to this step’s governed files, ensure PO-007 (D19_step_logs_manifest) is re-run so the manifest and path_proof reflect the final bytes.
Commands
mkdir -p audit/qa/hde-epic024/checks/po-006_token_registry_validity


rg -n '"acceptance_tokens"' docs/acceptance_map_epic024.json > audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt 2>&1 || true
rg -n '"token"' reports/qa_acceptance_tokens.json > audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt 2>&1 || true

Primary.log header write (choose ONE):
python -c 'import json, os; print(json.dumps({"check_id":"po-006_token_registry_validity","status":"PASS","fail_status":"","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF10 Addendum 2.8","PF19 §3.4.6"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log


python -c 'import json, os; print(json.dumps({"check_id":"po-006_token_registry_validity","status":"FAIL_BEHAVIOR","fail_status":"FAIL_BEHAVIOR","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF10 Addendum 2.8","PF19 §3.4.6"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log


python -c 'import json, os; print(json.dumps({"check_id":"po-006_token_registry_validity","status":"TOOLING_BLOCKED","fail_status":"TOOLING_BLOCKED","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF10 Addendum 2.8","PF19 §3.4.6"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log

After the chosen header write, append capture pointers:
printf '%s\n' 'captures:' >> audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log
printf '%s\n' '- audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt' >> audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log
printf '%s\n' '- audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt' >> audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log

Required deliverables
docs/acceptance_map_epic024.json
reports/qa_acceptance_tokens.json
audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt
audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt
audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log
What to look for
The capture files show all acceptance tokens used in the map and all tokens defined in the registry.
PASS criteria
All acceptance tokens found in docs/acceptance_map_epic024.json appear in reports/qa_acceptance_tokens.json.
FAIL criteria
Any acceptance token in the map is absent from the registry list.
Status tokens
intended_tokens: []
claimed_tokens:
PF anchors
PF10 Addendum 2.8 (acceptance token registry)
PF19 §3.4.6
CHECK D16_close_pack: PO-009
step_class: class 2 — internal functional/determinism
Proof obligation: Produce the PF10 “close pack” artifacts at fixed paths, with internal consistency, and ensure audit/EPIC-024_QA_RCA.md exists.
Goal: Provide a fixed-location close pack suitable for review.
Preconditions:
Step-0A completed.


Steps PO-001 through PO-008 have been executed and logs exist.


Setup:
None.


PO actions:
Run the close pack builder:

 python tools/evidence/run_close_pack.py


Verify that the close pack artifacts exist at fixed paths.


Verify audit/EPIC-024_QA_RCA.md exists (this satisfies the guide’s PO-010 completeness requirement without reusing D16_close_pack as a second row).


Confirm audit/qa/hde-epic024/checks/D16_close_pack/primary.log header status is PASS.


Commands:
python tools/evidence/run_close_pack.py
Required deliverables:
audit/EPIC-024_MANIFEST.json


audit/EPIC-024_close_report.md


audit/EPIC-024_QA_RCA.md


audit/qa/hde-epic024/checks/D16_close_pack/primary.log


What to look for:
The close pack artifacts exist at fixed paths and are internally consistent.


audit/EPIC-024_QA_RCA.md exists.


D16 primary.log header status is PASS.


PASS criteria:
All required deliverables exist and D16 primary.log header status is PASS.


FAIL criteria:
Any close pack artifact is missing, or audit/EPIC-024_QA_RCA.md is missing, or D16 primary.log is not PASS.


Status tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 §3.4.9


PF19 §3.4.10
CHECK po-011_doc_delta_capture: PO-011
Goal: Ensure doc delta capture exists, matches across loci, and is content-complete (not file-presence only).
Step class: class 1 — ops-only (posture-only).
Proof obligation: PASS iff both doc delta files exist, are identical across loci, and the content reflects all canon deltas raised by EPIC-024 work; FAIL_BEHAVIOR on mismatch/incomplete content; FAIL_TOOLING on missing/unreadable files.
PO actions:
Confirm both doc delta capture copies exist:
audit/docdeltas/hde-epic024_doc_deltas.md
audit/qa/hde-epic024/00_meta/doc_deltas.md
Validate the two files are identical:
diff -u audit/docdeltas/hde-epic024_doc_deltas.md audit/qa/hde-epic024/00_meta/doc_deltas.md
Content validation (manual proof obligation):
Open audit/docdeltas/hde-epic024_doc_deltas.md and confirm it includes every canon delta raised by EPIC-024 work (each entry includes PF ref + concise description).
If no canon deltas were raised, the file must explicitly state that.
Write primary.log header reflecting outcome and append evidence:
mkdir -p audit/qa/hde-epic024/checks/po-011_doc_delta_capture


if test -f audit/docdeltas/hde-epic024_doc_deltas.md && test -f audit/qa/hde-epic024/00_meta/doc_deltas.md; then
  DIFF_OUT="$(diff -u audit/docdeltas/hde-epic024_doc_deltas.md audit/qa/hde-epic024/00_meta/doc_deltas.md 2>&1)"
  DIFF_RC="$?"
  if test "$DIFF_RC" -eq 0; then
    python -c 'import json, os; print(json.dumps({"check_id":"po-011_doc_delta_capture","status":"PASS","fail_status":"","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF27 §4.2","PF19 §3.4.11"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
  else
    python -c 'import json, os; print(json.dumps({"check_id":"po-011_doc_delta_capture","status":"FAIL_BEHAVIOR","fail_status":"FAIL_BEHAVIOR","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF27 §4.2","PF19 §3.4.11"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
  fi
  ls -la audit/docdeltas/hde-epic024_doc_deltas.md audit/qa/hde-epic024/00_meta/doc_deltas.md >> audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
  printf '%s\n' "$DIFF_OUT" >> audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
else
  python -c 'import json, os; print(json.dumps({"check_id":"po-011_doc_delta_capture","status":"FAIL_TOOLING","fail_status":"FAIL_TOOLING","command":"N/A","command_provenance":"Copy/paste from plan","captured_env":{"MODO_AI_BUNDLE":os.environ.get("MODO_AI_BUNDLE",""),"MODO_AI_VERBOSE":os.environ.get("MODO_AI_VERBOSE",""),"MODO_RAILS":os.environ.get("MODO_RAILS",""),"LC_ALL":os.environ.get("LC_ALL",""),"LANG":os.environ.get("LANG",""),"TZ":os.environ.get("TZ","")},"pf_refs":["PF27 §4.2","PF19 §3.4.11"],"intended_tokens":[],"claimed_tokens":[]}, separators=(",",":")))' > audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
  ls -la audit/docdeltas/hde-epic024_doc_deltas.md audit/qa/hde-epic024/00_meta/doc_deltas.md >> audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log 2>&1 || true
fi

Commands:
diff -u audit/docdeltas/hde-epic024_doc_deltas.md audit/qa/hde-epic024/00_meta/doc_deltas.md
Required deliverables:
audit/docdeltas/hde-epic024_doc_deltas.md
audit/qa/hde-epic024/00_meta/doc_deltas.md
audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log
What to look for:
diff exit 0 indicates both loci match.
manual review confirms completeness of canon delta content.
primary.log header is PASS only when both match and content is complete.
PASS criteria:
Both files exist.
diff exit code 0.
content complete per manual validation.
primary.log header is PASS.
FAIL criteria:
Missing files ⇒ FAIL_TOOLING.
diff nonzero or incomplete content ⇒ FAIL_BEHAVIOR.
PF anchors:
PF27 — Plan Templates, §4.2
PF19 — Glow QA Guide, §3.4.11
CHECK D01_env_pins_gate: PO-012
Goal: Prove determinism env pins gate ran and outputs exist at fixed paths.
Step class: class 2 — internal functional/determinism.
Proof obligation: PASS iff determinism env pins gate passes and required outputs exist at fixed paths; FAIL_TOOLING otherwise.
PO actions:
Run the env pins gate runner:
python tools/evidence/run_env_pins_gate.py
Confirm:
Command exits successfully (exit code 0).
audit/gates/determinism/env_pins.log exists.
audit/gates/determinism/env_pins.log.path_proof.txt exists.
D01 primary.log header contains "status":"PASS".
Store the primary log at:
audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
Required deliverables:
python tools/evidence/run_env_pins_gate.py (command entrypoint)
audit/gates/determinism/env_pins.log
audit/gates/determinism/env_pins.log.path_proof.txt
audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
PASS criteria:
Command exits 0.
audit/gates/determinism/env_pins.log exists at fixed path.
audit/gates/determinism/env_pins.log.path_proof.txt exists at fixed path.
D01 primary.log header is PASS.
FAIL criteria:
Command missing or exits nonzero.
Required artifacts (env pins log and/or path_proof) missing.
D01 primary.log missing or header not PASS.
PF anchors:
PF19 — Glow QA Guide, §3.4.11
CHECK D03_showcompat_artifacts: PO-013
step_class: class 2 — internal functional/determinism
Proof obligation: Showcompat artifacts exist and are deterministic; emitter symbol proof exists.
Goal:
Execute showcompat artifacts runner and verify showcompat artifacts exist and primary log indicates PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run showcompat artifacts runner.


Confirm showcompat manifest and symbols exist.


Open D03 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_showcompat_artifacts.py
What to look for:
Command exits successfully (exit code 0).


artifacts/showcompat/epic024/showcompat_manifest.json exists.


artifacts/showcompat/epic024/showcompat_symbols.json exists.


D03 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_showcompat_artifacts.py (command entrypoint)


artifacts/showcompat/epic024/showcompat_manifest.json


artifacts/showcompat/epic024/showcompat_symbols.json


audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log


PASS criteria:
runner exits 0.


showcompat artifacts exist at fixed paths.


D03 primary log header contains "status":"PASS".


FAIL criteria:
runner missing or exits nonzero (FAIL_TOOLING or FAIL_BEHAVIOR).


showcompat artifacts missing (FAIL_TOOLING).


D03 primary log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.12


CHECK D08_cli_guardrail: PO-014


step_class: class 2 — internal functional/determinism
Proof obligation: CLI output discipline is enforced; serializer guard prevents accidental leakage into non-governed output.
Goal:
Execute serializer grep guard and verify it passes (exit=0) and cli/main.py exists, with primary log indicating PASS.


Preconditions:
Codespaces running.


Setup:
None.


PO actions:
Run serializer grep guard.


Confirm cli/main.py exists.


Open D08 primary.log and confirm header status PASS.


Commands:
python tools/cli/serializer_grep_guard.py
What to look for:
Command exits successfully (exit code 0).


cli/main.py exists.


D08 primary.log header contains "status":"PASS".


Required deliverables:
python tools/cli/serializer_grep_guard.py (command entrypoint)


cli/main.py


audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log


PASS criteria:
serializer_grep_guard.py exits 0.


cli/main.py exists.


D08 primary.log header contains "status":"PASS".


FAIL criteria:
Command exits nonzero (FAIL_BEHAVIOR or FAIL_TOOLING depending on error).


cli/main.py missing (FAIL_TOOLING).


D08 primary.log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.13


CHECK D04_sampler_evidence: PO-015

step_class: class 2 — internal functional/determinism
Proof obligation: Sampler evidence is generated and stored as governed artifacts with deterministic output.
Goal:
Confirm sampler evidence artifacts exist and the corresponding EPIC024 QA check indicates PASS.


Preconditions:
None beyond Step-0 completion.


Setup:
None.


PO actions:
Confirm sampler evidence artifacts exist:


artifacts/sampler/epic024/sampler_evidence.json


artifacts/sampler/epic024/manifest.json


Open D04 primary.log and confirm header status PASS.


Commands:
None required (review fixed artifacts and D04 primary log).


What to look for:
Sampler evidence files exist at the paths above.


D04 primary.log header contains "status":"PASS".


Required deliverables:
artifacts/sampler/epic024/sampler_evidence.json


artifacts/sampler/epic024/manifest.json


audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log


PASS criteria:
Both sampler evidence files exist.


D04 primary.log header contains "status":"PASS".


FAIL criteria:
Any sampler evidence file missing (FAIL_TOOLING).


D04 primary.log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF10 — HDE-Build Notes, Addendum 2.9


CHECK D01_env_pins_gate: PO-012
Goal: Prove determinism env pins gate ran and outputs exist at fixed paths.
Step class: class 2 — internal functional/determinism.
Proof obligation: PASS iff determinism env pins gate passes and required outputs exist at fixed paths; FAIL_TOOLING otherwise.
PO actions:
Run the env pins gate runner:
python tools/evidence/run_env_pins_gate.py
Confirm:
Command exits successfully (exit code 0).
audit/gates/determinism/env_pins.log exists.
audit/gates/determinism/env_pins.log.path_proof.txt exists.
D01 primary.log header contains "status":"PASS".
Store the primary log at:
audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
Required deliverables:
python tools/evidence/run_env_pins_gate.py (command entrypoint)
audit/gates/determinism/env_pins.log
audit/gates/determinism/env_pins.log.path_proof.txt
audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log
PASS criteria:
Command exits 0.
audit/gates/determinism/env_pins.log exists at fixed path.
audit/gates/determinism/env_pins.log.path_proof.txt exists at fixed path.
D01 primary.log header is PASS.
FAIL criteria:
Command missing or exits nonzero.
Required artifacts (env pins log and/or path_proof) missing.
D01 primary.log missing or header not PASS.
PF anchors:
PF19 — Glow QA Guide, §3.4.11
CHECK D07_sanity_pipeline: PO-016
Proof obligation: Sanity pipeline gate runs and produces a stable log; failures are actionable.
Goal:
Execute the sanity pipeline gate and verify the EPIC024 QA sanity pipeline check indicates PASS and the gate log exists.


Preconditions:
None beyond Step-0 completion.


Setup:
None.


PO actions:
Run the sanity pipeline command (CI-proven).


Confirm sanity pipeline log exists at fixed location.


Open D07 primary.log and confirm header status PASS.


Commands:
python tools/evidence/run_sanity_pipeline.py
What to look for:
Command exits successfully (exit code 0).


audit/gates/sanity_pipeline/sanity_pipeline.log exists.


D07 primary.log header contains "status":"PASS".


Required deliverables:
python tools/evidence/run_sanity_pipeline.py (command entrypoint)


audit/gates/sanity_pipeline/sanity_pipeline.log


audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log


PASS criteria:
run_sanity_pipeline.py exits 0.


sanity_pipeline.log exists at audit/gates/sanity_pipeline/sanity_pipeline.log.


D07 primary.log header contains "status":"PASS".


FAIL criteria:
Command exits nonzero (FAIL_BEHAVIOR or FAIL_TOOLING depending on error).


sanity_pipeline.log missing (FAIL_TOOLING).


D07 primary.log missing or header status not PASS (FAIL_BEHAVIOR).


Tokens:
intended_tokens:


claimed_tokens:


PF anchors:
PF19 — Glow QA Guide, §3.4.8


CHECK po-017_lowercase_naming: PO-017
step_class: class 1 — ops-only
Proof obligation: All QA-created artifacts are under lowercase-governed paths only.
Goal: Ensure no new uppercase-governed files are created under QA-created loci.
Preconditions:
Step-0A completed.


Setup:
Ensure the governed output directory exists:


audit/qa/hde-epic024/checks/po-017_lowercase_naming/


PO actions:
Scan only QA-created loci for uppercase-governed paths:


audit/qa/hde-epic024/**


artifacts/** (if present)


Explicit allowlist: fixed-location close pack artifacts under audit/EPIC-024_* are permitted and are out of scope for this check.


Write scan outputs directly to fixed governed paths (see Required deliverables).


Create/update audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log with a PF27-compliant JSON header (line 1), PASS iff scans are empty; otherwise FAIL_BEHAVIOR.


Manifest + path_proof rule: after final writes to this step’s governed files, ensure PO-007 (D19_step_logs_manifest) is re-run so the manifest and path_proof reflect the final bytes.


Commands:
mkdir -p audit/qa/hde-epic024/checks/po-017_lowercase_naming
find audit/qa/hde-epic024 -type f -print | grep -n -E '[A-Z]' > audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt || true
printf '%s\n' 'OUT OF SCOPE: docs/ is not scanned by PO-017 in this plan (QA-created files under docs/ are forbidden by this plan).' > audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt
if test -d artifacts; then
 find artifacts -type f -print | grep -n -E '[A-Z]' > audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt || true
 else
 : > audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt
 fi
if test -s audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt || test -s audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt; then
 printf '%s\n' '{"check_id":"po-017_lowercase_naming","status":"FAIL_BEHAVIOR","fail_status":"FAIL_BEHAVIOR","command":"N/A","command_provenance":"PO posture-only scan; see find_* outputs","captured_env":{},"pf_refs":["PF19 §3.4.17"],"intended_tokens":[],"claimed_tokens":[]}' > audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
 else
 printf '%s\n' '{"check_id":"po-017_lowercase_naming","status":"PASS","fail_status":"","command":"N/A","command_provenance":"PO posture-only scan; see find_* outputs","captured_env":{},"pf_refs":["PF19 §3.4.17"],"intended_tokens":[],"claimed_tokens":[]}' > audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
 fi
printf '%s\n' 'captures:' >> audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
 printf '%s\n' '- audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt' >> audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
 printf '%s\n' '- audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt' >> audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
 printf '%s\n' '- audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt' >> audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log
Required deliverables:
audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt


What to look for:
find_audit_uppercase.txt is empty.


find_artifacts_uppercase.txt is empty (or artifacts/ does not exist).


find_docs_uppercase.txt is an out-of-scope note (docs/ not scanned by this check).


PASS criteria:
No uppercase-governed paths found in QA-created loci (audit/qa/hde-epic024/** and artifacts/**).


FAIL criteria:
Any uppercase-governed path is present in find_audit_uppercase.txt or find_artifacts_uppercase.txt.


PF anchors:
PF19 §3.4.17

Close-out deliverables
At end of the run, the PO must provide governed deliverables at their fixed locations (no run-local acceptance surface):
Fixed-location governed deliverables:
audit/qa/hde-epic024/qa_step_logs_manifest.json


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt


audit/qa/hde-epic024/token_evidence_matrix.md


docs/acceptance_map_epic024.json


audit/qa/hde-epic024/acceptance_map_viability.log


audit/EPIC-024_MANIFEST.json


audit/EPIC-024_close_report.md


audit/EPIC-024_QA_RCA.md


audit/docdeltas/hde-epic024_doc_deltas.md


audit/qa/hde-epic024/00_meta/doc_deltas.md


audit/qa/hde-epic024/checks/ (primary logs referenced by audit/qa/hde-epic024/qa_step_logs_manifest.json)


Posture-only step log deliverables (fixed governed locations):
audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log


audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_acceptance_map_output.txt


audit/qa/hde-epic024/checks/po-006_token_registry_validity/rg_registry_output.txt


audit/qa/hde-epic024/checks/po-008_bootstrap_status_classification/primary.log


audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log


audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt


audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt


Note: audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt must be refreshed whenever audit/qa/hde-epic024/qa_step_logs_manifest.json bytes change.
Review guardrails
Reviewer checklist:
Every step in the Check Matrix has:


a clear status (PASS / FAIL_BEHAVIOR / FAIL_TOOLING / TOOLING_BLOCKED), and


required deliverables present at their fixed paths.


Step log manifest integrity:


audit/qa/hde-epic024/qa_step_logs_manifest.json exists, and


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt exists.


For each entry in audit/qa/hde-epic024/qa_step_logs_manifest.json:


the referenced log_path exists under audit/qa/hde-epic024/, and


the referenced log’s first line is a JSON object that includes at least check_id, status, fail_status, command, command_provenance, captured_env, pf_refs, intended_tokens, claimed_tokens


Posture-only steps captured by this plan:


the per-check governed logs exist at the fixed paths listed in “Posture-only step log deliverables”, and


any step marked TOOLING_BLOCKED includes a one-line missing-capability note in its primary.log.


Canonical path hygiene: no QA-created files were written under docs/.
Review guardrails (second)
A reviewer must be able to validate this run without re-running steps and without relying on external audit inventories:
Sources of truth for review are limited to:


primary step logs under audit/qa/hde-epic024/checks/<check_id>/primary.log


the step log manifest + path proof:


audit/qa/hde-epic024/qa_step_logs_manifest.json


audit/qa/hde-epic024/qa_step_logs_manifest.json.path_proof.txt


fixed-location deliverables referenced by the Check Matrix and “Close-out deliverables set”.


PF canon referenced via each check’s pf_refs.


Posture-only checks (PO-006 / PO-008 / PO-011 / PO-017) store their capture outputs at the fixed governed paths specified in their check blocks.


Command provenance is established by the step logs (primary.log header command and command_provenance) and the fixed-path capture outputs; no external inventory (e.g., CoDex audits) is required.

ASK OK?

