"""Current-state HDE-EPIC021 QA and acceptance-input generator."""

from __future__ import annotations

import json
import os
import re
import shutil
import stat as _stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import orientation_demo, update_evidence_index
from tools.evidence.run_sanity_pipeline import STAGE_NAMES as SANITY_STAGE_NAMES
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC021"
EPIC_SLUG = "hde-epic021"
BOOTSTRAP_CHECK_ID = "d00-bootstrap"
LEGACY_BOOTSTRAP_CHECK_ID = "D00_bootstrap"
BOOTSTRAP_TEST = "tests/qa/test_epic021_scaffolding.py"
QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic021.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"
DOC_DELTA_PATH = ROOT / "audit/docdeltas/hde-epic021_doc_deltas.md"
DOC_DELTA_CAPTURE_PATH = QA_ROOT / "00_meta/doc_deltas.md"
README_PATH = QA_ROOT / "README.md"
CLOSE_REPORT_PATH = ROOT / "audit/EPIC-021_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit/EPIC-021_MANIFEST.json"

REQUIRED_CLOSE_OUTPUTS = {
    "acceptance_map": "docs/acceptance_map_epic021.json",
    "token_matrix": "audit/qa/hde-epic021/token_evidence_matrix.md",
    "acceptance_viability": (
        "audit/qa/hde-epic021/acceptance_map_viability.log"
    ),
    "step_logs_manifest": (
        "audit/qa/hde-epic021/qa_step_logs_manifest.json"
    ),
    "doc_deltas": "audit/docdeltas/hde-epic021_doc_deltas.md",
    "close_report": "audit/EPIC-021_close_report.md",
    "close_manifest": "audit/EPIC-021_MANIFEST.json",
}
RETIRED_CLOSE_OUTPUT_KEYS = frozenset(
    {"acceptance_map_viability", "qa_step_manifest"}
)

LIVE_QA_TESTS = (
    "tests/qa/test_generic_qa_harness.py",
    "tests/qa/test_qa_harness_followup.py",
    "tests/qa/test_epic021_harness_entrypoint.py",
    "tests/qa/test_epic021_acceptance_alignment.py",
    "tests/qa/test_tooling_bootstrap.py",
    "tests/qa/test_epic021_scaffolding.py",
    "tests/cli/test_cli_canonical_bytes.py",
    "tests/cli/test_bg_resolve.py",
    "tests/cli/test_errors_parity.py",
    "tests/cli/test_aux_preview.py",
    "tests/cli/test_showcompat_parity_and_identity.py",
    "tests/cli/test_serializer_guards.py",
    "tests/evidence/test_sanity_pipeline.py",
    "tests/evidence/test_sanity_evidence_index.py",
    "tests/config/test_registry_report_indexing.py",
    "tests/evidence/test_evidence_index_env.py",
    "tests/invariance/test_determinism_env_helper.py",
    "tests/ops/test_evidence_index.py",
)
PRECOMMIT_COMMANDS = (
    ("ci/checks/check_env_pins.sh",),
    ("ci/checks/check_cli_help.sh",),
    ("ci/checks/check_final_lf.sh",),
)
TOOLING_CLASSIFICATION_FIXTURE = (
    "tests/qa/fixtures/epic021_missing_dependency.py"
)
CONTROLLED_TOOLING_FAILURE_CONTENT = (
    "run:epic021-controlled-bootstrap\n"
    "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC\n"
    "check import:FAIL_TOOLING controlled missing dependency\n"
    "pytest_returncode:2\n"
    "summary:FAIL_TOOLING\n"
)
PYTEST_PASS_RE = re.compile(r"(?m)^\s*(?P<count>[0-9]+) passed(?:[, ]|$)")
PYTEST_TERMINAL_RE = re.compile(
    r"(?P<count>[0-9]+) (?P<outcome>passed|skipped|xfailed|xpassed)"
)

FINAL_COMMANDS = (
    (sys.executable, "tools/evidence/validate_evidence_paths.py"),
    ("ci/checks/check_mirror_schema.sh",),
    ("ci/checks/check_evidence_index_hash.sh",),
    ("ci/checks/check_final_lf.sh",),
)


def _token(
    name: str,
    owner_pf: str,
    evidence_artifacts: str,
    ci_tests_jobs: str,
    qa_root_logs: str,
    notes: str,
) -> dict[str, str]:
    return {
        "name": name,
        "owner_pf": owner_pf,
        "evidence_artifacts": evidence_artifacts,
        "ci_tests_jobs": ci_tests_jobs,
        "qa_root_logs": qa_root_logs,
        "status": "Implemented",
        "notes": notes,
    }


TOKENS = (
    _token(
        "TESTS_PASS_OK",
        "PF19 — Glow QA Guide §QA Rails",
        "audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log",
        "python -m pytest -q -p no:cacheprovider " + " ".join(LIVE_QA_TESTS),
        "checks/po-epic021-live-qa/primary.log",
        "A fresh exact-collection test family proves the current EPIC021 QA and CLI surface.",
    ),
    _token(
        "DOC_DELTA_PRESENT_OK",
        "PF03 — Technical Writing §Single-home",
        "audit/docdeltas/hde-epic021_doc_deltas.md",
        "python -m pytest -q -p no:cacheprovider tests/qa/test_epic021_acceptance_alignment.py",
        "00_meta/doc_deltas.md; checks/po-epic021-live-qa/primary.log",
        "The deterministic current-state migration delta is bound by an alignment guard.",
    ),
    _token(
        "EVIDENCE_INDEX_UPDATED_OK",
        "PF12 — HDE-Schemas and Artifacts §Evidence Index",
        "docs/evidence/INDEX.json; docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl",
        "python tools/evidence/update_evidence_index.py --check",
        "checks/po-postcommit/primary.log",
        "The canonical updater owns the Human Index and its hash sentinel.",
    ),
    _token(
        "MACHINE_MIRROR_UPDATED_OK",
        "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
        "artifacts/evidence_index.jsonl",
        "python tools/evidence/update_evidence_index.py --check; python tools/evidence/orientation_demo.py --check",
        "checks/po-postcommit/primary.log",
        "The canonical updater owns the machine mirror and its self-proof.",
    ),
    _token(
        "EVIDENCE_INDEX_HASH_OK",
        "PF12 — HDE-Schemas and Artifacts §Evidence Hashing",
        "docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl",
        "ci/checks/check_evidence_index_hash.sh",
        "checks/po-postcommit/primary.log",
        "The Human Index sentinel and Machine Mirror body digest are validated by the canonical hash gate.",
    ),
    _token(
        "QA_PRECOMMIT_CHECKLIST_OK",
        "PF19 — Glow QA Guide §QA Rails",
        "audit/qa/hde-epic021/checks/po-precommit/primary.log",
        "ci/checks/check_env_pins.sh; ci/checks/check_cli_help.sh; ci/checks/check_final_lf.sh",
        "checks/po-precommit/primary.log",
        "Concrete precommit gates replace the historical prose-only binding.",
    ),
    _token(
        "QA_POSTCOMMIT_CHECKLIST_OK",
        "PF19 — Glow QA Guide §QA Rails",
        "audit/EPIC-021_close_report.md; audit/EPIC-021_MANIFEST.json; audit/qa/hde-epic021/checks/po-postcommit/primary.log",
        "python tools/qa/epic021_qa.py; python tools/evidence/run_sanity_pipeline.py; python tools/evidence/update_evidence_index.py --check; ci/checks/check_mirror_schema.sh; ci/checks/check_evidence_index_hash.sh",
        "checks/po-postcommit/primary.log",
        "Concrete postcommit entrypoints replace the historical run-id binding.",
    ),
    _token(
        "ENV_RAILS_POLICY_OK",
        "PF19 — Glow QA Guide §Env Pins",
        "audit/gates/determinism/env_pins.log; docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
        "ci/checks/check_env_pins.sh; python -m pytest -q -p no:cacheprovider tests/invariance/test_determinism_env_helper.py",
        "checks/po-epic021-live-qa/primary.log; checks/po-precommit/primary.log",
        "The bootstrap and evidence gates share the closed-rails policy.",
    ),
    _token(
        "EVIDENCE_INDEX_MIRROR_OK",
        "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
        "artifacts/evidence_index.jsonl",
        "python tools/evidence/update_evidence_index.py --check; ci/checks/check_mirror_schema.sh",
        "checks/po-postcommit/primary.log",
        "The updater check and mirror-schema gate validate one machine-readable surface.",
    ),
    _token(
        "EVIDENCE_PATHS_VALIDATED_OK",
        "PF12 — HDE-Schemas and Artifacts §Path Proofs",
        "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl; audit/qa/hde-epic021/checks/po-postcommit/primary.log",
        "python tools/evidence/validate_evidence_paths.py",
        "checks/po-postcommit/primary.log",
        "The canonical path validator covers indexed proof anchors.",
    ),
    _token(
        "DETERMINISM_ENV_PINS_OK",
        "PF19 — Glow QA Guide §Env Pins",
        "audit/gates/determinism/env_pins.log",
        "ci/checks/check_env_pins.sh",
        "checks/po-precommit/primary.log",
        "The current bootstrap receipt captures the required closed-rails environment.",
    ),
    _token(
        "SANITY_PIPELINE_OK",
        "PF19 — Glow QA Guide §Sanity Pipeline",
        "audit/gates/sanity_pipeline/sanity_pipeline.log",
        "python tools/evidence/run_sanity_pipeline.py",
        "checks/po-postcommit/primary.log",
        "The current canonical fifteen-stage sanity receipt is resolvable and indexed.",
    ),
    _token(
        "CLI_NO_ALT_JSON_OK",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "artifacts/cli/guards/serializer_grep_guard.log; audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log",
        "python -m pytest -q -p no:cacheprovider tests/cli/test_cli_canonical_bytes.py tests/cli/test_bg_resolve.py tests/cli/test_aux_preview.py tests/cli/test_serializer_guards.py",
        "checks/po-epic021-live-qa/primary.log",
        "Current CLI canonical-byte tests replace the historical serializer-step placeholder.",
    ),
    _token(
        "JSON_CANONICAL_CHECK_OK",
        "PF19 — Glow QA Guide §Emitter Canon",
        "audit/gates/json_gate/canonical/json_gate_structured_record.json",
        "python tools/evidence/run_canonical_json_gate.py --check-only",
        "checks/po-postcommit/primary.log",
        "The canonical JSON gate exposes a concrete read-only verifier and governed record.",
    ),
    _token(
        "ERROR_JSON_CANON_OK",
        "PF19 — Glow QA Guide §Emitter Canon",
        "parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt; parity/errors_reader_cli.vendor_attempt_closed_rails.http.json",
        "python -m pytest -q -p no:cacheprovider tests/cli/test_errors_parity.py",
        "checks/po-epic021-live-qa/primary.log",
        "Vendor-error nodes are selected through a concrete current pytest locator.",
    ),
    _token(
        "CI_CHECK_MIRROR_SCHEMA_OK",
        "PF12 — HDE-Schemas and Artifacts §Evidence Mirror",
        "artifacts/evidence_index.jsonl; docs/evidence/INDEX.json; audit/qa/hde-epic021/checks/po-postcommit/primary.log",
        "ci/checks/check_mirror_schema.sh",
        "checks/po-postcommit/primary.log",
        "The exact executable mirror-schema gate is bound without prose or shell composition.",
    ),
    _token(
        "CLI_READER_PARITY_OK",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "artifacts/cli/reader_cli_parity.bytes",
        "python tools/evidence/run_canonical_json_gate.py --check-only",
        "checks/po-postcommit/primary.log",
        "The deprecated CLI_READER_EMITTER_PARITY_OK name is normalized to its canonical token.",
    ),
    _token(
        "QA_HARNESS_DISCIPLINE_OK",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "audit/qa/hde-epic021/README.md; audit/qa/hde-epic021/qa_step_logs_manifest.json; audit/qa/hde-epic021/checks/po-postcommit/primary.log",
        "python tools/qa/epic021_qa.py; python -m pytest -q -p no:cacheprovider tests/qa/test_epic021_harness_entrypoint.py tests/qa/test_generic_qa_harness.py",
        "checks/d00-bootstrap/primary.log; checks/po-epic021-live-qa/primary.log; checks/po-postcommit/primary.log; checks/acceptance-map-viability/primary.log",
        "The responsible tools/qa/epic021_qa.py entrypoint and stable current-state receipts replace run consolidation and placeholders.",
    ),
    _token(
        "QA_BOOTSTRAP_OK",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log; audit/qa/hde-epic021/qa_step_logs_manifest.json",
        "python -m pytest -q -p no:cacheprovider tests/qa/test_epic021_scaffolding.py",
        "checks/d00-bootstrap/primary.log",
        "The current PF27 bootstrap receipt replaces the noncanonical PR_OPENED_OK label.",
    ),
    _token(
        "QA_BOOTSTRAP_TOOLING_FAIL",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "audit/qa/hde-epic021/00_meta/bootstrap_tooling_failure.log; audit/qa/hde-epic021/checks/bootstrap-tooling-classification/primary.log",
        "python -m pytest -q -p no:cacheprovider tests/qa/test_generic_qa_harness.py",
        "checks/bootstrap-tooling-classification/primary.log",
        "A fresh controlled missing-dependency probe proves tooling failure is distinct from behavior failure.",
    ),
    _token(
        "QA_ACCEPTANCE_MAP_VIABILITY_OK",
        "PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens",
        "docs/acceptance_map_epic021.json; audit/qa/hde-epic021/token_evidence_matrix.md; audit/qa/hde-epic021/acceptance_map_viability.log",
        "python -m pytest -q -p no:cacheprovider tests/qa/test_generic_qa_harness.py tests/qa/test_qa_harness_followup.py",
        "acceptance_map_viability.log",
        "The PF04/PF19 placeholder is replaced by the canonical viability token and dual receipt.",
    ),
)


@dataclass(frozen=True)
class _TokenRecord:
    owner_pf: str
    evidence_artifacts: tuple[str, ...]
    ci_tests_jobs: tuple[str, ...]
    qa_root_logs: tuple[str, ...]
    status: str


def _sorted_unique(
    values: Sequence[str], *, field: str, token_name: str
) -> tuple[str, ...]:
    if not values or any(
        not isinstance(value, str) or not value.strip() for value in values
    ):
        raise ValueError(f"token {token_name} has malformed {field}")
    stripped = tuple(value.strip() for value in values)
    if len(stripped) != len(set(stripped)):
        raise ValueError(f"token {token_name} has duplicate {field}")
    return tuple(sorted(stripped))


def _defined_token_rows() -> dict[str, _TokenRecord]:
    rows: dict[str, _TokenRecord] = {}
    for token in TOKENS:
        name = token["name"]
        if name in rows:
            raise ValueError(f"duplicate EPIC021 token definition: {name}")
        rows[name] = _TokenRecord(
            token["owner_pf"],
            _sorted_unique(
                token["evidence_artifacts"].split(";"),
                field="evidence_artifacts",
                token_name=name,
            ),
            _sorted_unique(
                token["ci_tests_jobs"].split(";"),
                field="ci_tests_jobs",
                token_name=name,
            ),
            _sorted_unique(
                token["qa_root_logs"].split(";"),
                field="qa_root_logs",
                token_name=name,
            ),
            token["status"].lower(),
        )
    return rows


def _manifest_token_records() -> list[dict[str, object]]:
    return [
        {
            "ci_tests_jobs": list(row.ci_tests_jobs),
            "evidence_artifacts": list(row.evidence_artifacts),
            "name": name,
            "owner_pf": row.owner_pf,
            "qa_root_logs": list(row.qa_root_logs),
            "status": row.status,
        }
        for name, row in sorted(_defined_token_rows().items())
    ]


def _acceptance_map_content() -> str:
    payload = {
        "epic_id": EPIC_ID,
        "tokens": [
            {
                "evidence_titles": token["evidence_artifacts"].split("; "),
                "name": token["name"],
                "owner_pf": token["owner_pf"],
                "status": token["status"].lower(),
            }
            for token in TOKENS
        ],
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def _token_matrix_content() -> str:
    lines = [
        "# HDE-EPIC021 Token ↔ Evidence Matrix",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for token in TOKENS:
        lines.append(
            "| {name} | {owner_pf} | {evidence_artifacts} | {ci_tests_jobs} | "
            "{qa_root_logs} | {status} | {notes} |".format(**token)
        )
    return "\n".join(lines) + "\n"


def _readme_content() -> str:
    return """# HDE-EPIC021 current-state QA harness

This directory is the governed QA_ROOT for EPIC021. Run the canonical entrypoint
from the repository root under already-closed rails:

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC APP_ENV=dev \\
  python tools/qa/epic021_qa.py
```

The entrypoint validates the supplied rails without modifying them. A successful
transaction publishes one flat, check-keyed `qa_step_logs_manifest.json` whose
current receipts are:

- `checks/d00-bootstrap/primary.log`
- `checks/bootstrap-tooling-classification/primary.log`
- `checks/po-epic021-live-qa/primary.log`
- `checks/po-precommit/primary.log`
- `checks/po-postcommit/primary.log`
- `checks/acceptance-map-viability/primary.log`

`acceptance_map_viability.log` is the governed epic-level viability ledger. The
QA_ROOT-owned binding artifacts are:

- `token_evidence_matrix.md`
- `checks/d00-bootstrap/primary.log`
- `qa_step_logs_manifest.json`
- `acceptance_map_viability.log`

The PF12 evidence graph remains outside QA_ROOT at these exact paths:

- `docs/evidence/INDEX.json`
- `docs/evidence/INDEX.sha256`
- `artifacts/evidence_index.jsonl`

The acceptance map, QA_ROOT artifacts, primary receipts, path proofs, PF12
evidence graph, and orientation receipt are refreshed and verified as one
recoverable transaction.

Historical run-id directories and `step_*` logs remain immutable historical
records. They are not imported into current correctness and are not executable
inputs to this harness.
"""


def _doc_delta_content() -> str:
    return """# HDE-EPIC021 Current-State Acceptance Migration — Doc Deltas

This QA slice records later PF-Canon drainage targets only. It does not edit PF-Canon,
move a PF09/PF20 status, claim token satisfaction, or rewrite historical EPIC021 run evidence.

- Normalize `CLI_READER_EMITTER_PARITY_OK` to `CLI_READER_PARITY_OK`, and retire
  `CLI_SERIALIZER_GUARD_OK` while retaining its guard evidence under
  `CLI_NO_ALT_JSON_OK`. (PF04 — HDE Governance, §2.0.)
- Normalize `QA_STEP_LOGS_CONSOLIDATED_OK` to `QA_HARNESS_DISCIPLINE_OK`, and
  retire `SANITY_PIPELINE_LOGGED_OK` while binding its intent through
  `SANITY_PIPELINE_OK` and `QA_HARNESS_DISCIPLINE_OK`. (PF04 — HDE Governance, §2.0.)
- Replace active run identity and `step_*` acceptance mechanics with stable
  `checks/<check_id>/primary.log` receipts, a flat check-keyed manifest, and the
  governed root viability ledger. (PF14 — HDE Mechanics Guide, §1.6.3.)
- Keep only the plan-owned lowercase `d00-bootstrap` receipt in the current
  canonical checks namespace; immutable historical run directories remain unchanged
  and non-gating. (PF14 — HDE Mechanics Guide, §1.6.3.)
- Publish this exact document at both the draft and epic-scoped capture paths.
  (PF06 — Epic Process Guide, §0.5.)
"""


def _doc_delta_capture_content() -> str:
    return _doc_delta_content()


def _close_manifest_content(captured_at_utc: str) -> str:
    payload = {
        "captured_at_utc": qa_harness._validate_timestamp(captured_at_utc),
        "closeout_dir": f"audit/qa/{EPIC_SLUG}",
        "epic_id": EPIC_ID,
        "key_outputs": {
            **REQUIRED_CLOSE_OUTPUTS,
            "qa_log_acceptance_map_viability": (
                "audit/qa/hde-epic021/checks/acceptance-map-viability/primary.log"
            ),
            "qa_log_bootstrap": (
                "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log"
            ),
            "qa_log_bootstrap_tooling_classification": (
                "audit/qa/hde-epic021/checks/"
                "bootstrap-tooling-classification/primary.log"
            ),
            "qa_log_live_qa": (
                "audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log"
            ),
            "qa_log_postcommit": (
                "audit/qa/hde-epic021/checks/po-postcommit/primary.log"
            ),
            "qa_log_precommit": (
                "audit/qa/hde-epic021/checks/po-precommit/primary.log"
            ),
        },
        "qa_epic_root": f"audit/qa/{EPIC_SLUG}",
        "qa_step_count": 6,
        "qa_step_manifest_path": (
            "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ),
        "scope": (
            "current_state_qa_requalification;"
            "historical_close_event_not_rewritten"
        ),
        "tokens": _manifest_token_records(),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def _close_report_content(captured_at_utc: str) -> str:
    return f"""# HDE-EPIC021 — Current-State QA Close Report

## Scope

This report closes the current-state QA requalification required by PR-03. It
does not rewrite EPIC021's historical close event, historical run directories,
or PF20 Done posture.

## Capture timestamp

- `{qa_harness._validate_timestamp(captured_at_utc)}`

## Acceptance and evidence pointers

- `docs/acceptance_map_epic021.json`
- `audit/qa/hde-epic021/token_evidence_matrix.md`
- `audit/qa/hde-epic021/acceptance_map_viability.log`
- `audit/docdeltas/hde-epic021_doc_deltas.md`
- `audit/qa/hde-epic021/qa_step_logs_manifest.json`
- `audit/EPIC-021_MANIFEST.json`
- `audit/EPIC-021_close_report.md`

## QA Rails — Open/Close (Final PR)

- Default posture: closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`,
  `LANG=C`, `TZ=UTC`).
- Opened-rails exceptions required for this current-state requalification: none.

## Mechanical result

- Six PF27 current-state checks are present and PASS.
- The acceptance map and matrix contain the same 21 canonical tokens.
- Acceptance-map viability is PASS with no broken references.
- Human Index, Machine Mirror, path proofs, hashes, orientation, and final-LF
  validation are coherent under closed rails.

Historical run-id and `step_*` evidence remains historical and non-gating.
"""


def _write_close_pack(captured_at_utc: str) -> None:
    qa_harness._atomic_write(
        CLOSE_MANIFEST_PATH, _close_manifest_content(captured_at_utc)
    )
    qa_harness._atomic_write(
        CLOSE_REPORT_PATH, _close_report_content(captured_at_utc)
    )


def _acceptance_map_token_rows(
    captured_bytes: bytes,
) -> tuple[tuple[str, ...], dict[str, _TokenRecord]]:
    try:
        payload = qa_harness._loads_json_strict(captured_bytes.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"acceptance map cannot be parsed: {exc}") from exc
    if not isinstance(payload, dict) or payload.get("epic_id") != EPIC_ID:
        raise ValueError("acceptance map epic identity is malformed or mismatched")
    tokens = payload.get("tokens")
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("acceptance map tokens must be a non-empty list")

    roster: list[str] = []
    rows: dict[str, _TokenRecord] = {}
    for index, item in enumerate(tokens, start=1):
        if not isinstance(item, dict):
            raise TypeError(f"acceptance token entry {index} is not an object")
        name = item.get("name")
        owner_pf = item.get("owner_pf")
        evidence = item.get("evidence_titles")
        status = qa_harness._normalized_acceptance_posture(item.get("status"))
        if not isinstance(name, str) or not qa_harness.TOKEN_RE.fullmatch(name):
            raise ValueError(f"acceptance token entry {index} has an invalid name")
        if name in rows:
            raise ValueError(f"duplicate acceptance token: {name}")
        if not isinstance(owner_pf, str) or not owner_pf.strip():
            raise ValueError(f"acceptance token {name} has an invalid owner_pf")
        if (
            not isinstance(evidence, list)
            or not evidence
            or any(
                not isinstance(value, str) or not value.strip() for value in evidence
            )
        ):
            raise ValueError(f"acceptance token {name} has invalid evidence_titles")
        if status is None:
            raise ValueError(f"acceptance token {name} has an invalid status")
        roster.append(name)
        rows[name] = _TokenRecord(
            owner_pf.strip(),
            _sorted_unique(
                evidence,
                field="evidence_titles",
                token_name=name,
            ),
            (),
            (),
            status,
        )
    return tuple(roster), rows


def _token_matrix_rows(
    path: Path, captured_bytes: bytes
) -> tuple[tuple[str, ...], dict[str, _TokenRecord]]:
    matrix, error = qa_harness._matrix_rows(path, captured_bytes=captured_bytes)
    if error:
        raise ValueError(f"token matrix cannot be parsed: {error}")
    rows: dict[str, _TokenRecord] = {}
    for name, row in matrix.items():
        status = qa_harness._normalized_acceptance_posture(row.status)
        if status is None:
            raise ValueError(f"matrix token {name} has an invalid status")
        rows[name] = _TokenRecord(
            row.owner_pf.strip(),
            _sorted_unique(
                row.evidence_artifacts,
                field="evidence_artifacts",
                token_name=name,
            ),
            _sorted_unique(
                row.ci_tests_jobs,
                field="ci_tests_jobs",
                token_name=name,
            ),
            _sorted_unique(
                row.qa_root_logs,
                field="qa_root_logs",
                token_name=name,
            ),
            status,
        )
    return tuple(matrix), rows


def _manifest_token_rows(
    manifest: Mapping[str, object],
) -> tuple[tuple[str, ...], dict[str, _TokenRecord]]:
    tokens = manifest.get("tokens")
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("close manifest tokens must be a non-empty list")
    roster: list[str] = []
    rows: dict[str, _TokenRecord] = {}
    required_fields = {
        "ci_tests_jobs",
        "evidence_artifacts",
        "name",
        "owner_pf",
        "qa_root_logs",
        "status",
    }
    for index, item in enumerate(tokens, start=1):
        if not isinstance(item, dict) or set(item) != required_fields:
            raise ValueError(
                f"close manifest token entry {index} has a malformed schema"
            )
        name = item.get("name")
        owner_pf = item.get("owner_pf")
        status = qa_harness._normalized_acceptance_posture(item.get("status"))
        if (
            not isinstance(name, str)
            or not qa_harness.TOKEN_RE.fullmatch(name)
            or name in rows
        ):
            raise ValueError(f"close manifest token entry {index} has an invalid name")
        if not isinstance(owner_pf, str) or not owner_pf.strip():
            raise ValueError(f"close manifest token {name} has an invalid owner_pf")
        if status is None:
            raise ValueError(f"close manifest token {name} has an invalid status")
        roster.append(name)
        rows[name] = _TokenRecord(
            owner_pf.strip(),
            _manifest_reference_list(item, "evidence_artifacts", name),
            _manifest_reference_list(item, "ci_tests_jobs", name),
            _manifest_reference_list(item, "qa_root_logs", name),
            status,
        )
    if tuple(roster) != tuple(sorted(roster)):
        raise ValueError("close manifest token roster is not ASCII-sorted")
    return tuple(roster), rows


def _manifest_reference_list(
    item: Mapping[str, object], field: str, token_name: str
) -> tuple[str, ...]:
    values = item.get(field)
    if not isinstance(values, list):
        raise TypeError(f"close manifest token {token_name} has malformed {field}")
    normalized = _sorted_unique(values, field=field, token_name=token_name)
    if tuple(values) != normalized:
        raise ValueError(
            f"close manifest token {token_name} {field} is not ASCII-sorted"
        )
    return normalized


def _validate_acceptance_lockstep(
    manifest: Mapping[str, object],
    viability: Mapping[str, object],
    *,
    acceptance_map_bytes: bytes,
    token_matrix_bytes: bytes,
    token_matrix_path: Path = TOKEN_MATRIX_PATH,
) -> None:
    expected_rows = _defined_token_rows()
    map_roster, map_rows = _acceptance_map_token_rows(acceptance_map_bytes)
    matrix_roster, matrix_rows = _token_matrix_rows(
        token_matrix_path, token_matrix_bytes
    )
    manifest_roster, manifest_rows = _manifest_token_rows(manifest)

    rosters = (set(map_roster), set(matrix_roster), set(manifest_roster))
    if not (rosters[0] == rosters[1] == rosters[2]):
        raise ValueError("map, matrix, and close manifest token rosters disagree")
    for name in sorted(rosters[0]):
        map_row = map_rows[name]
        matrix_row = matrix_rows[name]
        manifest_row = manifest_rows[name]
        if (
            map_row.owner_pf != matrix_row.owner_pf
            or map_row.evidence_artifacts != matrix_row.evidence_artifacts
            or map_row.status != matrix_row.status
        ):
            raise ValueError(
                f"acceptance map and token matrix bindings disagree for {name}"
            )
        if matrix_row != manifest_row:
            raise ValueError(
                f"token matrix and close manifest records disagree for {name}"
            )
    if matrix_rows != expected_rows:
        raise ValueError("acceptance records disagree with current token definitions")

    expected_disposition = {name: "VALID" for name in sorted(rosters[0])}
    if viability.get("epic_id") != EPIC_ID:
        raise ValueError("close viability epic identity is malformed or mismatched")
    if viability.get("acceptance_map_path") != REQUIRED_CLOSE_OUTPUTS["acceptance_map"]:
        raise ValueError("close viability acceptance_map_path is not canonical")
    if viability.get("token_status") != expected_disposition:
        raise ValueError("close viability token_status is not the exact current roster")
    if viability.get("token_reference_disposition") != expected_disposition:
        raise ValueError(
            "close viability token_reference_disposition is not the exact current roster"
        )


def _capture_close_input(path: Path, *, subject: str) -> bytes:
    status, reason, payload = qa_harness._read_stable_repo_file_bytes(
        ROOT, path, subject=subject
    )
    if status is not qa_harness.Status.PASS or payload is None:
        raise ValueError(
            f"{subject} cannot be captured safely: {status.value}: {reason}"
        )
    return payload


def _validate_close_pack() -> None:
    try:
        manifest_bytes = _capture_close_input(
            CLOSE_MANIFEST_PATH, subject="EPIC021 close manifest"
        )
        acceptance_map_bytes = _capture_close_input(
            ACCEPTANCE_MAP_PATH, subject="EPIC021 acceptance map"
        )
        token_matrix_bytes = _capture_close_input(
            TOKEN_MATRIX_PATH, subject="EPIC021 token matrix"
        )
        viability_bytes = _capture_close_input(
            VIABILITY_LOG_PATH, subject="EPIC021 viability ledger"
        )
        close_report_bytes = _capture_close_input(
            CLOSE_REPORT_PATH, subject="EPIC021 close report"
        )
        manifest = qa_harness._loads_json_strict(manifest_bytes.decode("utf-8"))
        if not isinstance(manifest, dict):
            raise TypeError("close manifest is not an object")
        captured_at_utc = manifest["captured_at_utc"]
        viability = qa_harness._loads_json_strict(viability_bytes.decode("utf-8"))
        if not isinstance(viability, dict):
            raise TypeError("close viability is not an object")
        _validate_acceptance_lockstep(
            manifest,
            viability,
            acceptance_map_bytes=acceptance_map_bytes,
            token_matrix_bytes=token_matrix_bytes,
        )
        if manifest_bytes.decode("utf-8") != _close_manifest_content(captured_at_utc):
            raise ValueError("close manifest is not canonical")
        if close_report_bytes.decode("utf-8") != _close_report_content(captured_at_utc):
            raise ValueError("close report is not canonical")
        key_outputs = manifest["key_outputs"]
        if not isinstance(key_outputs, dict):
            raise ValueError("close key_outputs is not a named object")
        for key, relative_path in REQUIRED_CLOSE_OUTPUTS.items():
            if key_outputs.get(key) != relative_path:
                raise ValueError(f"close output binding mismatch: {key}")
        retired_keys = RETIRED_CLOSE_OUTPUT_KEYS.intersection(key_outputs)
        if retired_keys:
            raise ValueError(
                "retired close output binding present: "
                + ",".join(sorted(retired_keys))
            )
        for relative_path in key_outputs.values():
            output = ROOT / relative_path
            if not output.is_file() or output.stat().st_size == 0:
                raise ValueError(f"close output unavailable: {relative_path}")
        if (
            viability.get("status") != qa_harness.Status.PASS.value
            or viability.get("broken_references") != []
        ):
            raise ValueError("close viability is not exact PASS")
        step_manifest = json.loads(
            (QA_ROOT / "qa_step_logs_manifest.json").read_text(encoding="utf-8")
        )
        expected_checks = {
            BOOTSTRAP_CHECK_ID,
            "bootstrap-tooling-classification",
            "po-epic021-live-qa",
            "po-precommit",
            "po-postcommit",
            "acceptance-map-viability",
        }
        if set(step_manifest) != expected_checks or any(
            entry.get("status") != qa_harness.Status.PASS.value
            for entry in step_manifest.values()
        ):
            raise ValueError("close step manifest is not exact six-check PASS")
    except (
        KeyError,
        OSError,
        TypeError,
        UnicodeError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        raise RuntimeError(f"EPIC021_CLOSE_PACK_INVALID:{exc}") from exc


@dataclass(frozen=True)
class _CommandReceipt:
    argv: tuple[str, ...]
    returncode: int | None
    stdout: str
    stderr: str
    process_error: str = ""
    semantic_artifact: bytes | None = None


class _TransientNarrativeMounts:
    """Remove only sealed narrative mounts created by the fresh test process."""

    _PACK_ID_RE = re.compile(r"[0-9a-f]{64}")

    def __init__(self, root: Path) -> None:
        self._root = root
        self._mount_root = root / "narratives"
        self._before: set[str] = set()

    def __enter__(self) -> _TransientNarrativeMounts:
        if self._mount_root.is_symlink():
            raise RuntimeError("EPIC021_NARRATIVE_MOUNT_ROOT_SYMLINK")
        if self._mount_root.exists() and not self._mount_root.is_dir():
            raise RuntimeError("EPIC021_NARRATIVE_MOUNT_ROOT_INVALID")
        self._before = (
            {path.name for path in self._mount_root.iterdir()}
            if self._mount_root.exists()
            else set()
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if not self._mount_root.exists():
            return False
        expected_members = {
            path.name
            for pattern in ("*.json", "*.sha256")
            for path in (self._root / "catalog/narratives").glob(pattern)
        }
        created = sorted(
            (
                path
                for path in self._mount_root.iterdir()
                if path.name not in self._before
            ),
            key=lambda path: path.name,
        )
        for path in created:
            if (
                self._PACK_ID_RE.fullmatch(path.name) is None
                or path.is_symlink()
                or not path.is_dir()
            ):
                raise RuntimeError(f"EPIC021_UNSAFE_TRANSIENT_MOUNT:{path}")
            members = tuple(path.iterdir())
            if {member.name for member in members} != expected_members or any(
                member.is_symlink() or not member.is_file() for member in members
            ):
                raise RuntimeError(f"EPIC021_INVALID_TRANSIENT_MOUNT:{path}")
            shutil.rmtree(path)
        return False


def _closed_execution_env(
    environ: Mapping[str, str] | None = None,
) -> dict[str, str]:
    source = os.environ if environ is None else environ
    runtime_bin = str(Path(sys.executable).parent)
    inherited_path = source.get("PATH", "")
    return {
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": runtime_bin
        + (os.pathsep + inherited_path if inherited_path else ""),
        "PYTHONDONTWRITEBYTECODE": "1",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }


def _execute_command(
    argv: Sequence[str],
    *,
    root: Path = ROOT,
    environ: Mapping[str, str] | None = None,
) -> _CommandReceipt:
    command = tuple(argv)
    try:
        completed = subprocess.run(
            command,
            cwd=root,
            env=_closed_execution_env(environ),
            capture_output=True,
            text=True,
            check=False,
            shell=False,
            timeout=1800,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return _CommandReceipt(
            command, None, "", "", f"{type(exc).__name__}: {exc}"
        )
    semantic_artifact = None
    if command[-1:] == ("tools/evidence/run_sanity_pipeline.py",):
        try:
            semantic_artifact = (
                root / "audit/gates/sanity_pipeline/sanity_pipeline.log"
            ).read_bytes()
        except OSError:
            semantic_artifact = None
    return _CommandReceipt(
        command,
        completed.returncode,
        completed.stdout or "",
        completed.stderr or "",
        semantic_artifact=semantic_artifact,
    )


def _run_commands(
    commands: Sequence[Sequence[str]], *, root: Path = ROOT
) -> tuple[_CommandReceipt, ...]:
    receipts: list[_CommandReceipt] = []
    for command in commands:
        receipt = _execute_command(command, root=root)
        receipts.append(receipt)
        if receipt.process_error or receipt.returncode != 0:
            break
    return tuple(receipts)


def _render_receipts(receipts: Sequence[_CommandReceipt]) -> str:
    blocks: list[str] = [qa_harness.NONCLAIM_EXPLANATION]
    for index, receipt in enumerate(receipts, start=1):
        blocks.append(
            json.dumps(
                {
                    "argv": list(receipt.argv),
                    "command_index": index,
                    "process_error": receipt.process_error,
                    "returncode": receipt.returncode,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        blocks.extend(
            (
                "[stdout]",
                receipt.stdout.rstrip("\n"),
                "[stderr]",
                receipt.stderr.rstrip("\n"),
            )
        )
        if receipt.semantic_artifact is not None:
            blocks.extend(
                (
                    "[semantic_artifact]",
                    receipt.semantic_artifact.decode(
                        "utf-8", errors="replace"
                    ).rstrip("\n"),
                )
            )
    return "\n".join(blocks).rstrip("\n") + "\n"


def _check_result(
    check_id: str,
    check_name: str,
    receipts: Sequence[_CommandReceipt],
    status: qa_harness.Status,
    reason: str,
    intended_tokens: Sequence[str],
) -> qa_harness.CheckResult:
    executed = tuple(
        receipt
        for receipt in receipts
        if not receipt.process_error and receipt.returncode is not None
    )
    command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    if len(executed) == 1:
        command = executed[0].argv
    elif executed:
        command = tuple(receipt.argv for receipt in executed)
    else:
        command = ()
    return qa_harness.CheckResult(
        check_id=check_id,
        status=status,
        status_reason=reason,
        check_name=check_name,
        command=command,
        command_provenance=(
            "EPIC021 exact executed non-shell argv receipts"
            if executed
            else "Not executed"
        ),
        exit_code=executed[-1].returncode if executed else None,
        output=_render_receipts(receipts),
        evidence_artifacts=(
            f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log",
        ),
        intended_tokens=(
            ()
            if status is qa_harness.Status.TOOLING_BLOCKED
            else tuple(intended_tokens)
        ),
        pf_refs=(
            "PF04-Canon-HDE-Governance",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
        captured_env=tuple(
            sorted((*qa_harness.DETERMINISM_ENV_PINS.items(), ("APP_ENV", "dev")))
        ),
    )


def _live_qa_result(*, root: Path = ROOT) -> qa_harness.CheckResult:
    commands = (
        (sys.executable, "-m", "pytest", "--version"),
        (
            sys.executable,
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            "-p",
            "no:cacheprovider",
            *LIVE_QA_TESTS,
        ),
        (
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            *LIVE_QA_TESTS,
        ),
    )
    with _TransientNarrativeMounts(root):
        receipts = _run_commands(commands, root=root)
    status = qa_harness.Status.PASS
    reason = ""
    if not receipts or receipts[0].process_error:
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "pytest readiness process malfunction",
        )
    elif receipts[0].returncode != 0:
        status, reason = (
            qa_harness.Status.TOOLING_BLOCKED,
            "pytest readiness check failed",
        )
    elif len(receipts) != 3:
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "EPIC021 current test family was not executed completely",
        )
    else:
        collected_nodes = {
            line.strip()
            for line in receipts[1].stdout.splitlines()
            if "::" in line
        }
        if receipts[1].returncode != 0 or any(
            not any(node.startswith(f"{path}::") for node in collected_nodes)
            for path in LIVE_QA_TESTS
        ):
            status, reason = (
                qa_harness.Status.FAIL_TOOLING,
                "EPIC021 collection omitted a required test module",
            )
        elif receipts[2].returncode != 0:
            status, reason = (
                qa_harness.Status.FAIL_BEHAVIOR
                if receipts[2].returncode == 1
                else qa_harness.Status.FAIL_TOOLING,
                "EPIC021 current test family failed",
            )
        else:
            summary_text = receipts[2].stdout + receipts[2].stderr
            summary = PYTEST_PASS_RE.search(summary_text)
            terminal_count = sum(
                int(match.group("count"))
                for match in PYTEST_TERMINAL_RE.finditer(summary_text)
            )
            if summary is None or terminal_count != len(collected_nodes):
                status, reason = (
                    qa_harness.Status.FAIL_TOOLING,
                    "pytest PASS count disagrees with exact collection",
                )
    return _check_result(
        "po-epic021-live-qa",
        "EPIC021 current QA and CLI family",
        receipts,
        status,
        reason,
        (
            "TESTS_PASS_OK",
            "CLI_NO_ALT_JSON_OK",
            "ERROR_JSON_CANON_OK",
            "ENV_RAILS_POLICY_OK",
            "DOC_DELTA_PRESENT_OK",
            "QA_HARNESS_DISCIPLINE_OK",
        ),
    )


def _tooling_classification_result(*, root: Path = ROOT) -> qa_harness.CheckResult:
    controlled = _execute_command(
        (
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            TOOLING_CLASSIFICATION_FIXTURE,
        ),
        root=root,
    )
    controlled_output = controlled.stdout + controlled.stderr
    causal_markers = (
        "ModuleNotFoundError" in controlled_output
        and "_epic021_deliberately_missing_dependency" in controlled_output
        and "ERROR collecting" in controlled_output
    )
    classified = (
        qa_harness.classify_pytest_returncode(controlled.returncode)
        if controlled.returncode is not None
        and not controlled.process_error
        and causal_markers
        else qa_harness.Status.FAIL_TOOLING
    )
    verifier = _execute_command(
        (
            sys.executable,
            "-c",
            "from tools.qa.qa_harness import Status,classify_pytest_returncode;"
            f"raise SystemExit(0 if classify_pytest_returncode({controlled.returncode!r}) "
            "is Status.FAIL_TOOLING else 1)",
        ),
        root=root,
    )
    receipts = (controlled, verifier)
    if (
        causal_markers
        and classified is qa_harness.Status.FAIL_TOOLING
        and verifier.returncode == 0
    ):
        status, reason = qa_harness.Status.PASS, ""
    else:
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "controlled bootstrap tooling-failure classification disagreed",
        )
    return _check_result(
        "bootstrap-tooling-classification",
        "EPIC021 controlled bootstrap tooling classification",
        receipts,
        status,
        reason,
        ("QA_BOOTSTRAP_TOOLING_FAIL",),
    )


def _precommit_result(*, root: Path = ROOT) -> qa_harness.CheckResult:
    receipts = _run_commands(PRECOMMIT_COMMANDS, root=root)
    if any(receipt.process_error for receipt in receipts):
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "precommit checklist process malfunction",
        )
    elif receipts and receipts[-1].returncode != 0:
        if receipts[-1].argv == PRECOMMIT_COMMANDS[0]:
            status, reason = (
                qa_harness.Status.FAIL_TOOLING,
                "environment-pins gate failed",
            )
        else:
            status, reason = (
                qa_harness.Status.FAIL_BEHAVIOR,
                "precommit checklist gate failed",
            )
    elif len(receipts) != len(PRECOMMIT_COMMANDS):
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "precommit checklist family is incomplete",
        )
    elif "[env-pins] OK:" not in receipts[0].stdout:
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "environment-pins receipt lacks its success predicate",
        )
    else:
        status, reason = qa_harness.Status.PASS, ""
    return _check_result(
        "po-precommit",
        "EPIC021 current precommit checklist",
        receipts,
        status,
        reason,
        (
            "QA_PRECOMMIT_CHECKLIST_OK",
            "ENV_RAILS_POLICY_OK",
            "DETERMINISM_ENV_PINS_OK",
        ),
    )


def _sanity_status(payload: bytes | None) -> tuple[qa_harness.Status, str]:
    if payload is None:
        return (
            qa_harness.Status.FAIL_TOOLING,
            "sanity pipeline did not produce its governed result",
        )
    try:
        lines = payload.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        return qa_harness.Status.FAIL_TOOLING, "sanity pipeline result is not UTF-8"
    prefix = (
        "run:sanity-pipeline",
        "pipeline_identity:hde-release-sanity-v1",
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC",
        "env_pins:audit/gates/determinism/env_pins.log",
    )
    expected = list(prefix)
    for name in SANITY_STAGE_NAMES:
        expected.append(f"check {name}:OK")
    expected.extend(("first_failed_stage:NONE", "summary:PASS"))
    if lines == expected:
        return qa_harness.Status.PASS, ""
    if len(lines) >= 2 and lines[-1] == "summary:FAIL":
        first_failed_prefix = "first_failed_stage:"
        if lines[-2].startswith(first_failed_prefix):
            first_failure = lines[-2][len(first_failed_prefix) :]
            if first_failure in SANITY_STAGE_NAMES:
                failure_index = SANITY_STAGE_NAMES.index(first_failure)
                failed_expected = list(prefix)
                for index, name in enumerate(SANITY_STAGE_NAMES):
                    status = "OK" if index < failure_index else "FAIL"
                    failed_expected.append(f"check {name}:{status}")
                    if index > failure_index:
                        failed_expected.append(
                            f"not_executed {name}:"
                            f"earlier_mandatory_failure={first_failure}"
                        )
                failed_expected.extend(
                    (f"first_failed_stage:{first_failure}", "summary:FAIL")
                )
                if lines == failed_expected:
                    return (
                        qa_harness.Status.FAIL_BEHAVIOR,
                        f"sanity pipeline predicate failed: {first_failure}",
                    )
    return qa_harness.Status.FAIL_TOOLING, "sanity pipeline result is not exact PASS"


def _postcommit_result(
    *, root: Path = ROOT
) -> tuple[qa_harness.CheckResult, bytes | None]:
    receipts = _run_commands(
        ((sys.executable, "tools/evidence/run_sanity_pipeline.py"),), root=root
    )
    if len(receipts) != 1 or receipts[0].process_error:
        status, reason = (
            qa_harness.Status.FAIL_TOOLING,
            "release-sanity process malfunction",
        )
    else:
        status, reason = _sanity_status(receipts[0].semantic_artifact)
        if receipts[0].returncode != 0 and status is qa_harness.Status.PASS:
            status, reason = (
                qa_harness.Status.FAIL_TOOLING,
                "release-sanity exit/result disagreement",
            )
    result = _check_result(
        "po-postcommit",
        "EPIC021 current postcommit release-sanity checklist",
        receipts,
        status,
        reason,
        (
            "QA_POSTCOMMIT_CHECKLIST_OK",
            "SANITY_PIPELINE_OK",
            "JSON_CANONICAL_CHECK_OK",
            "CLI_READER_PARITY_OK",
            "EVIDENCE_INDEX_UPDATED_OK",
            "MACHINE_MIRROR_UPDATED_OK",
            "EVIDENCE_INDEX_HASH_OK",
            "EVIDENCE_INDEX_MIRROR_OK",
            "EVIDENCE_PATHS_VALIDATED_OK",
            "CI_CHECK_MIRROR_SCHEMA_OK",
        ),
    )
    artifact = receipts[0].semantic_artifact if len(receipts) == 1 else None
    return result, artifact


def _require_pass(result: qa_harness.CheckResult) -> None:
    if result.status is not qa_harness.Status.PASS:
        raise RuntimeError(
            f"{result.check_id}_{result.status.value}:{result.status_reason}"
        )


def _provisional_result(check_id: str, reason: str) -> qa_harness.CheckResult:
    return qa_harness.CheckResult(
        check_id=check_id,
        status=qa_harness.Status.TOOLING_BLOCKED,
        status_reason=reason,
        check_name=f"EPIC021 {check_id} graph preseal",
        command=(),
        command_provenance="Not executed",
        exit_code=None,
        output=qa_harness.NONCLAIM_EXPLANATION + "\n",
        evidence_artifacts=(
            f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log",
        ),
        intended_tokens=(),
        pf_refs=(
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )


def _path_proof_path(path: Path) -> Path:
    return path.with_name(f"{path.name}.path_proof.txt")


def _updater_graph_paths() -> tuple[Path, ...]:
    primaries = (
        ROOT / "docs/evidence/INDEX.json",
        ROOT / "docs/evidence/INDEX.sha256",
        ROOT / "artifacts/evidence_index.jsonl",
        ROOT / "artifacts/evidence_index.jsonl.sha256",
        ROOT / "audit/gates/topology/orientation_demo.txt",
    )
    registered_proofs = tuple(
        ROOT / f"{entry['discovered_physical_path']}.path_proof.txt"
        for entry in update_evidence_index._load_human_index()
    )
    return (
        *primaries,
        *(_path_proof_path(path) for path in primaries),
        *registered_proofs,
    )


def _wrapper_write_paths() -> tuple[Path, ...]:
    governed = (
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        DOC_DELTA_PATH,
        DOC_DELTA_CAPTURE_PATH,
        README_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
        VIABILITY_LOG_PATH,
        QA_ROOT / "qa_step_logs_manifest.json",
        QA_ROOT / "checks/d00-bootstrap/primary.log",
        QA_ROOT / "checks/po-epic021-live-qa/primary.log",
        QA_ROOT / "checks/bootstrap-tooling-classification/primary.log",
        QA_ROOT / "00_meta/bootstrap_tooling_failure.log",
        QA_ROOT / "checks/po-precommit/primary.log",
        QA_ROOT / "checks/po-postcommit/primary.log",
        QA_ROOT / "checks/acceptance-map-viability/primary.log",
        ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log",
    )
    paths = {
        *governed,
        *(_path_proof_path(path) for path in governed),
        *_updater_graph_paths(),
    }
    return tuple(sorted(paths, key=lambda path: path.as_posix()))


class _WrapperWriteTransaction:
    """Restore the entire wrapper and updater family after any failure."""

    def __init__(self) -> None:
        self._preimages: dict[Path, tuple[bytes, int] | None] = {}
        self._new_directories: set[Path] = set()

    @staticmethod
    def _relative(path: Path) -> None:
        try:
            path.absolute().relative_to(ROOT.absolute())
        except ValueError as exc:
            raise RuntimeError(f"WRAPPER_TRANSACTION_PATH_OUTSIDE_ROOT:{path}") from exc

    def _inspect_parent_chain(self, path: Path) -> None:
        parents: list[Path] = []
        parent = path.parent
        while parent != ROOT:
            self._relative(parent)
            parents.append(parent)
            parent = parent.parent
        for candidate in reversed(parents):
            if candidate.is_symlink():
                raise RuntimeError(
                    f"WRAPPER_TRANSACTION_PARENT_SYMLINK:{candidate}"
                )
            if candidate.exists():
                if not candidate.is_dir():
                    raise RuntimeError(
                        f"WRAPPER_TRANSACTION_PARENT_NOT_DIRECTORY:{candidate}"
                    )
            else:
                self._new_directories.add(candidate)

    def __enter__(self) -> _WrapperWriteTransaction:
        if ROOT.is_symlink() or not ROOT.is_dir():
            raise RuntimeError("WRAPPER_TRANSACTION_ROOT_INVALID")
        for path in _wrapper_write_paths():
            self._relative(path)
            self._inspect_parent_chain(path)
            if path.is_symlink():
                raise RuntimeError(f"WRAPPER_TRANSACTION_TARGET_SYMLINK:{path}")
            if path.exists():
                if not path.is_file():
                    raise RuntimeError(
                        f"WRAPPER_TRANSACTION_TARGET_NOT_REGULAR:{path}"
                    )
                self._preimages[path] = (
                    path.read_bytes(),
                    _stat.S_IMODE(path.stat().st_mode),
                )
            else:
                self._preimages[path] = None
        return self

    @staticmethod
    def _restore_file(path: Path, content: bytes, mode: int) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.rollback.", dir=path.parent
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(temporary, mode)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)

    @staticmethod
    def _remove_new_target(path: Path) -> None:
        if path.is_symlink() or path.is_file():
            path.unlink(missing_ok=True)
        elif path.exists():
            path.rmdir()

    def _rollback(self) -> None:
        for path, preimage in self._preimages.items():
            if preimage is None:
                self._remove_new_target(path)
                continue
            if path.is_symlink():
                path.unlink()
            elif path.exists() and not path.is_file():
                path.rmdir()
            content, mode = preimage
            self._restore_file(path, content, mode)
        for directory in sorted(
            self._new_directories,
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            if directory.is_symlink():
                directory.unlink()
            elif directory.exists():
                directory.rmdir()

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_value is None:
            return False
        try:
            self._rollback()
        except BaseException as rollback_error:  # noqa: BLE001
            raise RuntimeError("EPIC021_WRAPPER_ROLLBACK_FAILED") from rollback_error
        return False


def _write_acceptance_inputs() -> None:
    qa_harness._atomic_write(ACCEPTANCE_MAP_PATH, _acceptance_map_content())
    qa_harness._atomic_write(TOKEN_MATRIX_PATH, _token_matrix_content())
    qa_harness._atomic_write(DOC_DELTA_PATH, _doc_delta_content())
    qa_harness._atomic_write(DOC_DELTA_CAPTURE_PATH, _doc_delta_capture_content())
    qa_harness._atomic_write(README_PATH, _readme_content())


def run_epic021_qa(*, repo_root: Path | None = None) -> dict[str, object]:
    """Execute EPIC021's concrete bootstrap and governed viability definitions."""
    ensure_determinism_env()
    config = qa_harness.HarnessConfig(
        EPIC_ID,
        repo_root=repo_root,
        step_names=(BOOTSTRAP_CHECK_ID,),
    )
    bootstrap = qa_harness.run_pytest_check(
        config,
        BOOTSTRAP_CHECK_ID,
        ("-q", BOOTSTRAP_TEST),
        check_name="EPIC021 tooling bootstrap",
    )
    bootstrap_log, manifest = qa_harness.record_check(
        config, bootstrap, supersede_check_ids=(LEGACY_BOOTSTRAP_CHECK_ID,)
    )
    viability = qa_harness.generate_acceptance_map_viability(
        config, publish_governed_ledger=True
    )
    governed_ledger = qa_harness.require_governed_viability(
        viability, config.viability_ledger_path
    )
    return {
        "bootstrap": bootstrap,
        "bootstrap_log": bootstrap_log,
        "manifest": manifest,
        "viability": viability,
        "governed_ledger": governed_ledger,
    }


def _provisional_ledger(reason: str) -> str:
    return (
        json.dumps(
            {
                "epic_id": EPIC_ID,
                "status": qa_harness.Status.TOOLING_BLOCKED.value,
                "status_reason": reason,
                "token_status": {},
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    )


def _write_graph() -> None:
    update_evidence_index.main([])
    orientation_demo.main([])


def _verify_graph() -> None:
    update_evidence_index.main(["--check"])
    orientation_demo.main(["--check"])
    for command in FINAL_COMMANDS:
        _run_final_command(command)


def _execute_current_family() -> dict[str, object]:
    """Execute, publish, and seal the complete EPIC021 current-state family."""
    config = qa_harness.HarnessConfig(EPIC_ID, repo_root=ROOT)

    bootstrap = qa_harness.run_pytest_check(
        config,
        BOOTSTRAP_CHECK_ID,
        ("-q", BOOTSTRAP_TEST),
        check_name="EPIC021 tooling bootstrap",
        intended_tokens=("QA_BOOTSTRAP_OK",),
    )
    qa_harness.record_check(
        config, bootstrap, supersede_check_ids=(LEGACY_BOOTSTRAP_CHECK_ID,)
    )
    _require_pass(bootstrap)

    tooling_classification = _tooling_classification_result(root=ROOT)
    qa_harness.record_check(
        config,
        tooling_classification,
        additional_files=(
            (
                QA_ROOT / "00_meta/bootstrap_tooling_failure.log",
                CONTROLLED_TOOLING_FAILURE_CONTENT,
            ),
        ),
    )
    _require_pass(tooling_classification)

    precommit = _precommit_result(root=ROOT)
    qa_harness.record_check(config, precommit)
    _require_pass(precommit)

    live_reason = "current test family awaits the updater-bound evidence-graph preseal"
    qa_harness.record_check(
        config, _provisional_result("po-epic021-live-qa", live_reason)
    )
    post_reason = "postcommit awaits the updater-bound evidence-graph preseal"
    qa_harness.record_check(
        config, _provisional_result("po-postcommit", post_reason)
    )
    viability_reason = "viability awaits current postcommit requalification"
    qa_harness.record_check(
        config,
        _provisional_result("acceptance-map-viability", viability_reason),
        additional_files=(
            (VIABILITY_LOG_PATH, _provisional_ledger(viability_reason)),
        ),
    )

    _write_graph()
    _verify_graph()

    live_qa = _live_qa_result(root=ROOT)
    qa_harness.record_check(config, live_qa)
    _require_pass(live_qa)

    # The live receipt and manifest entry are indexed inputs to the canonical
    # sanity pipeline.  Seal them before Stage 15 validates the graph.
    _write_graph()
    _verify_graph()

    postcommit, first_sanity = _postcommit_result(root=ROOT)
    qa_harness.record_check(config, postcommit)
    _require_pass(postcommit)

    # The fresh postcommit receipt and manifest entry are viability evidence.
    # Seal and verify those exact bytes before evaluating their governance.
    _write_graph()
    _verify_graph()

    viability = qa_harness.generate_acceptance_map_viability(
        config, publish_governed_ledger=True
    )
    governed_ledger = qa_harness.require_governed_viability(
        viability, VIABILITY_LOG_PATH
    )
    _validate_close_pack()

    _write_graph()
    second_postcommit, second_sanity = _postcommit_result(root=ROOT)
    _require_pass(second_postcommit)
    if first_sanity is None or first_sanity != second_sanity:
        raise RuntimeError("EPIC021_POSTCOMMIT_NOT_FIXED_POINT")
    _validate_close_pack()
    _verify_graph()

    return {
        "bootstrap": bootstrap,
        "live_qa": live_qa,
        "tooling_classification": tooling_classification,
        "precommit": precommit,
        "postcommit": postcommit,
        "viability": viability,
        "governed_ledger": governed_ledger,
    }


def _run_final_command(command: tuple[str, ...]) -> None:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=_closed_execution_env(),
            capture_output=True,
            text=True,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"EPIC021_FINAL_GATE_FAIL_TOOLING:{command[0]}:{exc}") from exc
    if completed.returncode != 0:
        raise RuntimeError(
            f"EPIC021_FINAL_GATE_FAILED:{command[0]}:{completed.returncode}:"
            f"{completed.stdout}{completed.stderr}"
        )


def main() -> int:
    try:
        ensure_determinism_env()
        captured_at_utc = qa_harness._utc_now()
        with _WrapperWriteTransaction():
            _write_acceptance_inputs()
            _write_close_pack(captured_at_utc)
            with _TransientNarrativeMounts(ROOT):
                _execute_current_family()
    except (DeterminismEnvError, OSError, ValueError, RuntimeError) as exc:
        sys.stderr.write(f"EPIC021_QA_ERROR: {exc}\n")
        return 1
    except SystemExit as exc:
        sys.stderr.write(f"EPIC021_QA_ERROR: {exc}\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
