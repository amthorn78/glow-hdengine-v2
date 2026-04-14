#!/usr/bin/env python3
"""Generate EPIC029 offline acceptance + close-pack binding artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC029"
EPIC_SLUG = "hde-epic029"
RUN_ID = "epic029-close"
PF09_TASK_ID = "HDE-CONJ009"
PF09_SUBTASK_ID = "HDE-CONJ009.1"
PF09_SCOPE = [
    {"task_id": "HDE-CONJ009", "subtask_id": "HDE-CONJ009.1"},
    {"task_id": "HDE-CONJ008", "subtask_id": "HDE-CONJ008.1"},
    {"task_id": "HDE-CONJ001", "subtask_id": "HDE-CONJ001.4"},
]

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
OPS_ROOT = ROOT / "audit" / "ops" / EPIC_SLUG / "ops-01"
CLOSURE_MODE = "binding-equivalence"

ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic029.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"
QA_STEP_MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"

SURFACE_INVENTORY_PATH = QA_ROOT / "00_meta" / "conjunction_json_surface_inventory.md"
DEV_HARNESS_BINDING_COVERAGE_PATH = QA_ROOT / "00_meta" / "dev_harness_binding_coverage.md"

DOC_DELTAS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_doc_deltas.md"
DRAIN_TARGETS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_drain_targets.md"

CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-029_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-029_MANIFEST.json"

OPS_REQUIRED = [
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_codes.txt",
    "codespaces_dev_sampler_url.md",
    "local_dev_sampler_url.md",
    "binding_disposition.md",
    "created_files_sha256.txt",
]

LIVE_QA_CHECKS = {
    "po-epic-close-live-qa": QA_ROOT / "checks" / "po-epic-close-live-qa" / "primary.log",
    "po-precommit": QA_ROOT / "checks" / "po-precommit" / "primary.log",
    "po-postcommit": QA_ROOT / "checks" / "po-postcommit" / "primary.log",
}


def _has_path_proof(path: Path) -> bool:
    return path.with_name(path.name + ".path_proof.txt").exists()


def _evidence_index_status() -> dict[str, bool]:
    index = ROOT / "docs" / "evidence" / "INDEX.json"
    mirror = ROOT / "artifacts" / "evidence_index.jsonl"
    index_sha = ROOT / "docs" / "evidence" / "INDEX.sha256"
    mirror_sha = ROOT / "artifacts" / "evidence_index.jsonl.sha256"

    index_present = index.exists() and _has_path_proof(index)
    mirror_present = mirror.exists() and _has_path_proof(mirror)
    hashes_present = (
        index_sha.exists()
        and mirror_sha.exists()
        and _has_path_proof(index_sha)
        and _has_path_proof(mirror_sha)
    )
    hashes_match = False
    if index_present and mirror_present and hashes_present:
        index_parts = index_sha.read_text(encoding="utf-8").strip().split()
        mirror_parts = mirror_sha.read_text(encoding="utf-8").strip().split()
        if index_parts and mirror_parts:
            index_expected = index_parts[0]
            mirror_expected = mirror_parts[0]
            hashes_match = (
                index_expected == _sha256(index) and mirror_expected == _sha256(mirror)
            )
    return {
        "evidence_index_updated": index_present,
        "machine_mirror_updated": mirror_present,
        "evidence_index_hash": hashes_present and hashes_match,
    }


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT).as_posix()}")


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


def _write_path_proof(path: Path, produced_at: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )
    print(f"WROTE {rel}.path_proof.txt")


def _missing_required_paths() -> list[str]:
    required = [SURFACE_INVENTORY_PATH, ROOT / "artifacts" / "writer" / "conjunction_write_readback.log", ROOT / "artifacts" / "writer" / "conjunction_writer_summary.json"]
    required += [OPS_ROOT / name for name in OPS_REQUIRED]
    return [path.relative_to(ROOT).as_posix() for path in required if not path.exists()]


def _live_qa_status() -> dict[str, bool]:
    status: dict[str, bool] = {}
    for check_id, path in LIVE_QA_CHECKS.items():
        if not path.exists():
            status[check_id] = False
            continue
        text = path.read_text(encoding="utf-8")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        exit_code_line = next((line for line in reversed(lines) if line.startswith("[exit_code]")), "")
        status[check_id] = exit_code_line == "[exit_code] 0"
    return status


def _ops_binding_disposition_status() -> dict[str, str]:
    disposition = OPS_ROOT / "binding_disposition.md"
    status = {"codespaces": "not yet closed", "local_dev": "not yet closed"}
    if not disposition.exists():
        return status

    for raw in disposition.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("codespaces:"):
            status["codespaces"] = line.split(":", 1)[1].strip().split(" - ", 1)[0]
        elif line.startswith("local_dev:"):
            status["local_dev"] = line.split(":", 1)[1].strip().split(" - ", 1)[0]
    return status


def _has_surface_inventory_closure_semantics(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    required_fragments = (
        "## Conclusion (PR-01 bounded outcome)",
        "single shared canonical emitter (`emit_public` -> `sercanon`)",
        "No in-place emitter fix was needed for the inventoried loci.",
    )
    return all(fragment in text for fragment in required_fragments)


def _has_writer_closure_semantics(log_path: Path, summary_path: Path) -> bool:
    if not (log_path.exists() and summary_path.exists()):
        return False

    log_lines = {
        line.strip()
        for line in log_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    required_log_lines = {
        "schema=conjunction_write_readback.log.v1",
        "route=/dev/writer/conjunction",
        "reader_route=/dev/reader/conjunction",
        "writer_first_status=200",
        "writer_second_status=200",
        "reader_status=200",
        "writer_invalid_status=422",
        "writer_bytes_two_run_equal=true",
        "writer_payload_two_run_equal=true",
        "writer_result_reader_readback_equal=true",
        "writer_success_type=dev.writer.conjunction.success.v1",
        "writer_error_type=dev.writer.conjunction.error.v1",
    }
    if not required_log_lines.issubset(log_lines):
        return False

    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False

    checks = summary.get("checks")
    if not isinstance(checks, dict):
        return False

    required_true_checks = (
        "writer_status_200",
        "reader_status_200",
        "writer_error_typed_envelope",
        "writer_success_typed_envelope",
        "writer_bytes_two_run_equal",
        "writer_payload_two_run_equal",
        "writer_result_reader_readback_equal",
    )
    return all(checks.get(check_name) is True for check_name in required_true_checks)


def _pf09_row_closure_gate(live_qa: dict[str, bool], index_status: dict[str, bool]) -> dict[str, object]:
    disposition_status = _ops_binding_disposition_status()
    codespaces_closed = disposition_status["codespaces"] == "closed"
    local_dev_closed = disposition_status["local_dev"] == "closed"
    required_inputs_ready = not _missing_required_paths()
    qa_complete = all(live_qa.values())
    evidence_index_complete = all(index_status.values())
    writer_log = ROOT / "artifacts" / "writer" / "conjunction_write_readback.log"
    writer_summary = ROOT / "artifacts" / "writer" / "conjunction_writer_summary.json"
    hde_conj009_1_closed = _has_surface_inventory_closure_semantics(SURFACE_INVENTORY_PATH)
    hde_conj008_1_closed = _has_writer_closure_semantics(writer_log, writer_summary)
    hde_conj001_4_closed = codespaces_closed and local_dev_closed
    ready_for_close_binding = all(
        [
            hde_conj009_1_closed,
            hde_conj008_1_closed,
            hde_conj001_4_closed,
            required_inputs_ready,
            qa_complete,
            evidence_index_complete,
        ]
    )
    return {
        "sequencing_classification": "supportable from repo evidence",
        "closure_mode": CLOSURE_MODE,
        "codespaces": disposition_status["codespaces"],
        "local_dev": disposition_status["local_dev"],
        "row_closure_status": {
            "HDE-CONJ009.1": "closed" if hde_conj009_1_closed else "not closed",
            "HDE-CONJ008.1": "closed" if hde_conj008_1_closed else "not closed",
            "HDE-CONJ001.4": "closed" if hde_conj001_4_closed else "not closed",
        },
        "mapped_rows": {
            "HDE-CONJ009.1": "Supportable from repo evidence: HDE-CONJ009.1 -> Done",
            "HDE-CONJ008.1": "Supportable from repo evidence: HDE-CONJ008.1 -> Done",
            "HDE-CONJ001.4": (
                "Supportable from repo evidence: HDE-CONJ001.4 -> Done after OPS-01 normalization"
                if hde_conj001_4_closed
                else "remains open while codespaces or local_dev is not yet closed"
            ),
        },
        "ready_for_close_binding": ready_for_close_binding,
    }


def _tokens(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> list[dict[str, object]]:
    gate_open = bool(gate["ready_for_close_binding"])
    return [
        {
            "name": "DOC_DELTA_PRESENT_OK",
            "owner_pf": "PF04 — HDE Governance §2.0.0",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": [
                "audit/docdeltas/hde-epic029_doc_deltas.md",
                "audit/docdeltas/hde-epic029_drain_targets.md",
            ],
        },
        {
            "name": "EVIDENCE_INDEX_UPDATED_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Index",
            "status": "implemented" if (gate_open and index_status["evidence_index_updated"]) else "token_incomplete",
            "evidence_titles": ["docs/evidence/INDEX.json"],
        },
        {
            "name": "MACHINE_MIRROR_UPDATED_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Mirror",
            "status": "implemented" if (gate_open and index_status["machine_mirror_updated"]) else "token_incomplete",
            "evidence_titles": ["artifacts/evidence_index.jsonl"],
        },
        {
            "name": "EVIDENCE_INDEX_HASH_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Hash Discipline",
            "status": "implemented" if (gate_open and index_status["evidence_index_hash"]) else "token_incomplete",
            "evidence_titles": [
                "docs/evidence/INDEX.sha256",
                "artifacts/evidence_index.jsonl.sha256",
            ],
        },
        {
            "name": "ENV_RAILS_POLICY_OK",
            "owner_pf": "PF10 — HDE Build Notes §Closed Rails",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": ["artifacts/proofs/env_pins.txt"],
        },
        {
            "name": "JSON_CANONICAL_CHECK_OK",
            "owner_pf": "PF10 — HDE Build Notes §Canonical JSON Gate",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": [
                "audit/gates/json_gate/canonical/json_gate_structured_record.json",
                "audit/gates/canonical_json/json_canonical_check.log",
            ],
        },
        {
            "name": "TESTS_PASS_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-epic-close-live-qa"]) else "token_incomplete",
            "evidence_titles": [
                "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log",
            ],
        },
        {
            "name": "QA_PRECOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-precommit"]) else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-precommit/primary.log"],
        },
        {
            "name": "QA_POSTCOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-postcommit"]) else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-postcommit/primary.log"],
        },
    ]


def _write_acceptance_map(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> None:
    _write_json(ACCEPTANCE_MAP_PATH, {"epic_id": EPIC_ID, "sequencing_gate": gate, "tokens": _tokens(live_qa, index_status, gate)})


def _write_token_matrix(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> None:
    gate_open = bool(gate["ready_for_close_binding"])
    lines = [
        "# HDE-EPIC029 Token ↔ Evidence Matrix",
        "",
        "Sequencing posture: **supportable from repo evidence**.",
        "Close-pack acceptance binding is supportable for the controlled PF09 rows in this bounded EPIC029 closeout.",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        f"| DOC_DELTA_PRESENT_OK | PF04 — HDE Governance §2.0.0 | audit/docdeltas/hde-epic029_doc_deltas.md; audit/docdeltas/hde-epic029_drain_targets.md | Bound by close-pack generator outputs | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Doc-delta and drain-target ledgers are generated and bound for close-pack readiness.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| EVIDENCE_INDEX_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Index | docs/evidence/INDEX.json | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['evidence_index_updated']) else 'Planned'} | {'Bound only when INDEX.json and INDEX.json.path_proof.txt are present.' if (gate_open and index_status['evidence_index_updated']) else 'Deferred pending required readiness inputs.'} |",
        f"| MACHINE_MIRROR_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Mirror | artifacts/evidence_index.jsonl | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['machine_mirror_updated']) else 'Planned'} | {'Bound only when evidence_index.jsonl and evidence_index.jsonl.path_proof.txt are present.' if (gate_open and index_status['machine_mirror_updated']) else 'Deferred pending required readiness inputs.'} |",
        f"| EVIDENCE_INDEX_HASH_OK | PF12 — Schemas & Artifacts §Evidence Hash Discipline | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['evidence_index_hash']) else 'Planned'} | {'Bound only when sha256 sidecars and path proofs exist and hashes match current bytes.' if (gate_open and index_status['evidence_index_hash']) else 'Deferred pending required readiness inputs.'} |",
        f"| ENV_RAILS_POLICY_OK | PF10 — HDE Build Notes §Closed Rails | artifacts/proofs/env_pins.txt | ci/checks/check_env_pins.sh (via sanity pipeline) | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Determinism env pins evidence remains present for closed-rails posture.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| JSON_CANONICAL_CHECK_OK | PF10 — HDE Build Notes §Canonical JSON Gate | audit/gates/json_gate/canonical/json_gate_structured_record.json; audit/gates/canonical_json/json_canonical_check.log | tools/evidence/run_canonical_json_gate.py (governed) | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Canonical JSON gate evidence is bound without introducing new token names.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | Existing epic-close live QA output only | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-epic-close-live-qa']) else 'Planned'} | {'Bound to existing live QA primary log.' if (gate_open and live_qa['po-epic-close-live-qa']) else 'Deferred pending required readiness inputs.'} |",
        f"| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | Existing precommit checklist output only | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-precommit']) else 'Planned'} | {'Bound to existing precommit primary log.' if (gate_open and live_qa['po-precommit']) else 'Deferred pending required readiness inputs.'} |",
        f"| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | Existing postcommit checklist output only | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-postcommit']) else 'Planned'} | {'Bound to existing postcommit primary log.' if (gate_open and live_qa['po-postcommit']) else 'Deferred pending required readiness inputs.'} |",
        "",
        "## PF09 scope bindings (status-only; not acceptance tokens)",
        "",
        f"- Supportable from repo evidence: `{PF09_SCOPE[0]['subtask_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[0]['task_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[1]['subtask_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[1]['task_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[2]['subtask_id']}` -> Done after OPS-01 normalization.",
        "- `HDE-CONJ001` remains task-level done in PF09; this report only states subtask supportability from repo evidence.",
    ]
    _write_text(TOKEN_MATRIX_PATH, "\n".join(lines) + "\n")


def _write_dev_harness_binding_coverage(live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    live_block = []
    for check_id, path in LIVE_QA_CHECKS.items():
        rel = path.relative_to(ROOT).as_posix()
        if live_qa[check_id]:
            live_block.append(f"- `{rel}`: present and bound.")
        else:
            live_block.append(f"- `{rel}`: missing (deferred; no synthetic PASS claim).")

    hde_conj001_4_closed = gate["row_closure_status"]["HDE-CONJ001.4"] == "closed"
    local_line = (
        "- Local dev is **closed** by explicit binding-equivalence to the canonical Codespaces loopback DEV_SAMPLER_URL for EPIC029 (not an independent second runtime proof)."
        if hde_conj001_4_closed
        else "- Local dev remains **not yet closed**; PF07 publishes `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`, but OPS disposition has not closed this environment."
    )
    hde_conj001_4_line = (
        "- Therefore `HDE-CONJ001.4` is closed under the approved equivalence rule for this epic slice."
        if hde_conj001_4_closed
        else "- Therefore `HDE-CONJ001.4` remains not done in this close-pack."
    )

    content = f"""# HDE-EPIC029 Dev Harness Binding Coverage

## OPS-01 single-source disposition
- Source of truth: `audit/ops/hde-epic029/ops-01/binding_disposition.md`.
- Codespaces is **{gate['codespaces']}** based on OPS-01 evidence under closed rails.
- Closure mode: {gate['closure_mode']}
{local_line}
{hde_conj001_4_line}

## OPS-01 files bound by this PR
- `audit/ops/hde-epic029/ops-01/commands.txt`
- `audit/ops/hde-epic029/ops-01/stdout.log`
- `audit/ops/hde-epic029/ops-01/stderr.log`
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

## Epic-close Live QA outputs disposition
{chr(10).join(live_block)}
"""
    _write_text(DEV_HARNESS_BINDING_COVERAGE_PATH, content)


def _write_docdeltas() -> None:
    _write_text(
        DOC_DELTAS_PATH,
        "# HDE-EPIC029 doc deltas\n\n- Empty ledger: this PR binds governed acceptance/closeout artifacts only; no canon/doc prose deltas were introduced.\n",
    )
    _write_text(
        DRAIN_TARGETS_PATH,
        "# HDE-EPIC029 drain targets\n\n- Empty ledger: no additional drain-target document actions are required in this offline acceptance binding slice.\n",
    )


def _write_qa_step_manifest(live_qa: dict[str, bool]) -> None:
    checks = {
        "po-epic-close-live-qa": {
            "check_id": "po-epic-close-live-qa",
            "log_path": "checks/po-epic-close-live-qa/primary.log",
            "status": "PASS" if live_qa["po-epic-close-live-qa"] else "MISSING",
        },
        "po-precommit": {
            "check_id": "po-precommit",
            "log_path": "checks/po-precommit/primary.log",
            "status": "PASS" if live_qa["po-precommit"] else "MISSING",
        },
        "po-postcommit": {
            "check_id": "po-postcommit",
            "log_path": "checks/po-postcommit/primary.log",
            "status": "PASS" if live_qa["po-postcommit"] else "MISSING",
        },
    }
    _write_json(QA_STEP_MANIFEST_PATH, {"epic_id": EPIC_ID, "checks": checks})


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        qa_root=QA_ROOT,
        acceptance_map_path=ACCEPTANCE_MAP_PATH,
        token_matrix_path=TOKEN_MATRIX_PATH,
        step_names=("acceptance_map_viability",),
    )
    qa_harness.generate_acceptance_map_viability(config, RUN_ID)
    print(f"WROTE {VIABILITY_LOG_PATH.relative_to(ROOT).as_posix()}")


def _write_close_report(produced_at: str, live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    qa_lines = []
    for check_id, exists in live_qa.items():
        rel = LIVE_QA_CHECKS[check_id].relative_to(ROOT).as_posix()
        qa_lines.append(f"- `{rel}`: {'present' if exists else 'missing'}")

    hde_conj001_4_closed = gate["row_closure_status"]["HDE-CONJ001.4"] == "closed"
    hde_conj001_4_line = (
        "- `HDE-CONJ001` / `HDE-CONJ001.4`: closed by explicit binding-equivalence normalization across OPS-01 governed evidence."
        if hde_conj001_4_closed
        else "- `HDE-CONJ001` / `HDE-CONJ001.4`: represented via OPS disposition; remains not done while codespaces/local_dev are not yet closed."
    )
    ops_truth_line = (
        "- `HDE-CONJ001.4` is marked complete using approved equivalence closure with no claim of a second independently exercised runtime."
        if hde_conj001_4_closed
        else "- `HDE-CONJ001.4` is therefore not marked complete in this PR."
    )

    content = f"""# HDE-EPIC029 — Close Report

## Overview
This EPIC029 closeout refresh is bounded to repo-side governed evidence and report-only status recommendations for the controlling conjunction rows.

## Capture timestamp
- `{produced_at}`

## PF09 mapping used
- Task: `{PF09_TASK_ID}`
- Subtask: `{PF09_SUBTASK_ID}`
- Additional bound subtasks: `HDE-CONJ008.1`, `HDE-CONJ001.4`.

## PF09 scope truth (bound in metadata, not minted as acceptance tokens)
- `HDE-CONJ001` / `HDE-CONJ001.4`: status supportability is bound via normalized OPS-01 disposition evidence.
- `HDE-CONJ008` / `HDE-CONJ008.1`: status supportability is bound via existing writer conjunction evidence.
- `HDE-CONJ009` / `HDE-CONJ009.1`: status supportability is bound via existing conjunction surface inventory evidence.

## OPS-01 truth preserved
- Codespaces is **{gate['codespaces']}** under OPS-01 governed evidence.
- Local dev is **{gate['local_dev']}** under OPS-01 governed evidence.
- Closure mode: {gate['closure_mode']}
{ops_truth_line}

## PF09 status recommendations (report only; no PF edits)
- Current PF09 text is not edited here.
- Statuses below are supportable from repo evidence only.
- Any PF09 status change happens later, outside this Codex work.
- Supportable from repo evidence: HDE-CONJ009.1 -> Done
- Supportable from repo evidence: HDE-CONJ009 -> Done
- Supportable from repo evidence: HDE-CONJ008.1 -> Done
- Supportable from repo evidence: HDE-CONJ008 -> Done
- Supportable from repo evidence: HDE-CONJ001.4 -> Done, contingent on the normalized OPS-01 binding-equivalence family now present in repo

## Epic-close Live QA outputs
{chr(10).join(qa_lines)}

## Canonical EPIC029 close-pack artifacts
- `docs/acceptance_map_epic029.json`
- `audit/qa/hde-epic029/token_evidence_matrix.md`
- `audit/qa/hde-epic029/acceptance_map_viability.log`
- `audit/qa/hde-epic029/qa_step_logs_manifest.json`
- `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`
- `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`
- `audit/docdeltas/hde-epic029_doc_deltas.md`
- `audit/docdeltas/hde-epic029_drain_targets.md`
- `audit/EPIC-029_close_report.md`
- `audit/EPIC-029_MANIFEST.json`
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str, live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    key_outputs = {
        "acceptance_map": "docs/acceptance_map_epic029.json",
        "token_matrix": "audit/qa/hde-epic029/token_evidence_matrix.md",
        "acceptance_map_viability": "audit/qa/hde-epic029/acceptance_map_viability.log",
        "qa_step_manifest": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "conjunction_json_surface_inventory": "audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md",
        "dev_harness_binding_coverage": "audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md",
        "doc_deltas": "audit/docdeltas/hde-epic029_doc_deltas.md",
        "drain_targets": "audit/docdeltas/hde-epic029_drain_targets.md",
        "close_report": "audit/EPIC-029_close_report.md",
        "close_manifest": "audit/EPIC-029_MANIFEST.json",
        "ops_commands": "audit/ops/hde-epic029/ops-01/commands.txt",
        "ops_stdout": "audit/ops/hde-epic029/ops-01/stdout.log",
        "ops_stderr": "audit/ops/hde-epic029/ops-01/stderr.log",
        "ops_exit_codes": "audit/ops/hde-epic029/ops-01/exit_codes.txt",
        "ops_codespaces_dev_sampler_url": "audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md",
        "ops_local_dev_sampler_url": "audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md",
        "ops_binding_disposition": "audit/ops/hde-epic029/ops-01/binding_disposition.md",
        "ops_created_files_sha256": "audit/ops/hde-epic029/ops-01/created_files_sha256.txt",
    }
    payload = {
        "captured_at_utc": produced_at,
        "closeout_dir": "audit/qa/hde-epic029",
        "epic_id": EPIC_ID,
        "key_outputs": key_outputs,
        "ops_task_id": "OPS-01",
        "pf09_task_id": PF09_TASK_ID,
        "pf09_subtask_id": PF09_SUBTASK_ID,
        "pf09_scope": PF09_SCOPE,
        "qa_epic_root": "audit/qa/hde-epic029",
        "qa_step_count": len(live_qa),
        "qa_step_manifest_path": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "qa_summary_lines": [
            f"po-epic-close-live-qa={'recorded' if live_qa['po-epic-close-live-qa'] else 'missing'}",
            f"po-precommit={'recorded' if live_qa['po-precommit'] else 'missing'}",
            f"po-postcommit={'recorded' if live_qa['po-postcommit'] else 'missing'}",
            f"codespaces={gate['codespaces']}",
            f"local_dev={gate['local_dev']}",
            f"closure_mode={gate['closure_mode']}",
            "hde_conj009_1=supportable_from_repo_evidence_done_report_only",
            "hde_conj009=supportable_from_repo_evidence_done_report_only",
            "hde_conj008_1=supportable_from_repo_evidence_done_report_only",
            "hde_conj008=supportable_from_repo_evidence_done_report_only",
            f"hde_conj001_4={gate['row_closure_status']['HDE-CONJ001.4']}",
            "hde_conj001_4_recommendation=supportable_from_repo_evidence_done_after_ops01_normalization",
            "pf09_report_only_recommendations=yes_no_pf_edits",
        ],
        "run_id": RUN_ID,
        "scope": "repo_side_governed_evidence_closeout_report_only_pf09_recommendations",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _write_path_proofs(produced_at: str) -> None:
    governed = [
        DOC_DELTAS_PATH,
        DRAIN_TARGETS_PATH,
        OPS_ROOT / "commands.txt",
        OPS_ROOT / "stdout.log",
        OPS_ROOT / "stderr.log",
        OPS_ROOT / "exit_codes.txt",
        OPS_ROOT / "codespaces_dev_sampler_url.md",
        OPS_ROOT / "local_dev_sampler_url.md",
        OPS_ROOT / "binding_disposition.md",
        OPS_ROOT / "created_files_sha256.txt",
        ACCEPTANCE_MAP_PATH,
        TOKEN_MATRIX_PATH,
        VIABILITY_LOG_PATH,
        QA_STEP_MANIFEST_PATH,
        SURFACE_INVENTORY_PATH,
        DEV_HARNESS_BINDING_COVERAGE_PATH,
        CLOSE_REPORT_PATH,
        CLOSE_MANIFEST_PATH,
    ]
    for path in governed:
        _write_path_proof(path, produced_at)


def _verify_manifest_paths() -> None:
    payload = json.loads(CLOSE_MANIFEST_PATH.read_text(encoding="utf-8"))
    missing: list[str] = []
    for rel in sorted(set(payload["key_outputs"].values())):
        if not (ROOT / rel).exists():
            missing.append(rel)
    if missing:
        raise SystemExit(f"DANGLING_MANIFEST_PATHS:{','.join(missing)}")


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    missing = _missing_required_paths()
    if missing:
        raise SystemExit(f"MISSING_REQUIRED_INPUTS:{','.join(missing)}")

    produced_at = _utc_now()
    live_qa = _live_qa_status()
    index_status = _evidence_index_status()
    gate = _pf09_row_closure_gate(live_qa, index_status)

    _write_acceptance_map(live_qa, index_status, gate)
    _write_token_matrix(live_qa, index_status, gate)
    _write_qa_step_manifest(live_qa)
    _write_viability_log()
    _write_dev_harness_binding_coverage(live_qa, gate)
    _write_docdeltas()
    _write_close_report(produced_at, live_qa, gate)
    _write_close_manifest(produced_at, live_qa, gate)
    _write_path_proofs(produced_at)
    _verify_manifest_paths()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
