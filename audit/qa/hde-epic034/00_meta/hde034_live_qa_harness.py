from __future__ import annotations

import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

EPIC_ID = "HDE-EPIC034"
EPIC_QA_ROOT = Path("audit/qa/hde-epic034")
CHECKS_ROOT = EPIC_QA_ROOT / "checks"
META_ROOT = EPIC_QA_ROOT / "00_meta"


class ToolingBlocked(Exception):
    pass


class FailBehavior(Exception):
    pass


def utc_now() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_path_proof(path: Path) -> Path:
    if not path.exists():
        raise ToolingBlocked(f"MISSING_PATH_FOR_PROOF:{path}")
    proof_path = Path(str(path) + ".path_proof.txt")
    stat = path.stat()
    proof_path.write_text(
        "\n".join(
            [
                f"path: {path}",
                f"size_bytes: {stat.st_size}",
                f"sha256: {sha256(path)}",
                f"mtime_utc: {datetime.datetime.utcfromtimestamp(stat.st_mtime).replace(microsecond=0).isoformat()}Z",
                f"produced_at_utc: {utc_now()}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return proof_path


def read_text(path: str | Path) -> str:
    target = Path(path)
    if not target.exists():
        raise ToolingBlocked(f"MISSING_FILE:{target}")
    return target.read_text(encoding="utf-8")


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def require_file(path: str | Path, body: list[str]) -> None:
    target = Path(path)
    if not target.exists():
        raise ToolingBlocked(f"MISSING_FILE:{target}")
    body.append(f"FILE_OK {target} sha256={sha256(target)}")


def require_contains(path: str | Path, needle: str, body: list[str]) -> None:
    text = read_text(path)
    if needle not in text:
        raise FailBehavior(f"MISSING_TEXT:{path}:{needle}")
    body.append(f"TEXT_OK {path} :: {needle}")


def require_regex(path: str | Path, pattern: str, body: list[str]) -> None:
    text = read_text(path)
    if not re.search(pattern, text):
        raise FailBehavior(f"MISSING_REGEX:{path}:{pattern}")
    body.append(f"REGEX_OK {path} :: {pattern}")


def require_json_value(path: str | Path, key: str, expected: Any, body: list[str]) -> None:
    payload = load_json(path)
    if key not in payload:
        raise FailBehavior(f"MISSING_JSON_KEY:{path}:{key}")
    actual = payload[key]
    if actual != expected:
        raise FailBehavior(f"JSON_VALUE_MISMATCH:{path}:{key}:{actual!r}!={expected!r}")
    body.append(f"JSON_OK {path} :: {key}={expected!r}")


def classify_ops_result(path: str | Path, body: list[str]) -> None:
    payload = load_json(path)
    classification = payload.get("classification")
    if classification == "TOOLING_BLOCKED":
        raise ToolingBlocked(f"OPS02_TOOLING_BLOCKED:{payload.get('exit_code')!r}")
    if classification != "PASS":
        raise FailBehavior(f"OPS02_CLASSIFICATION:{classification!r}")


def readonly_subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    for key in ["HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY"]:
        env.pop(key, None)
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        }
    )
    return env


def run_readonly(
    cmd: list[str], body: list[str], *, behavior_failure: bool = True
) -> None:
    body.append("COMMAND " + " ".join(cmd))
    try:
        completed = subprocess.run(
            cmd,
            cwd=Path("."),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            env=readonly_subprocess_env(),
        )
    except FileNotFoundError as exc:
        raise ToolingBlocked(f"COMMAND_MISSING:{cmd[0]}") from exc
    output = completed.stdout.strip()
    if output:
        body.append(output)
    body.append(f"EXIT_CODE {completed.returncode}")
    if completed.returncode != 0:
        if behavior_failure:
            raise FailBehavior(f"COMMAND_FAILED:{' '.join(cmd)}:{completed.returncode}")
        raise ToolingBlocked(f"COMMAND_FAILED:{' '.join(cmd)}:{completed.returncode}")


def require_pytest(body: list[str]) -> None:
    completed = subprocess.run(
        [sys.executable, "-c", "import pytest"],
        cwd=Path("."),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        env=readonly_subprocess_env(),
    )
    if completed.returncode != 0:
        raise ToolingBlocked("PYTEST_MISSING")
    body.append("PYTEST_IMPORT_OK")


def check_step0b(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifacts = [
        "audit/docdeltas/hde-epic034_doc_deltas.md",
        "audit/qa/hde-epic034/00_meta/doc_deltas.md",
    ]
    for artifact in artifacts:
        require_file(artifact, body)
    body.append("DOC_DELTA_PRESENT_OK")
    return artifacts, ["DOC_DELTA_PRESENT_OK"], ["DOC_DELTA_PRESENT_OK"]


def check_po001(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/source_selection.snapshot.json"
    require_file(artifact, body)
    require_contains(
        artifact, '"recommended_internal_vendor_route_family":"recommended_v2_chart"', body
    )
    require_contains(artifact, '"route_family":"recommended_v2_chart"', body)
    require_contains(artifact, '"route_variant":"coordinates_chart"', body)
    require_contains(artifact, '"runtime_conformance_claim":"NONE"', body)
    return [artifact], [], []


def check_po002(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    source = "artifacts/vendor/hdapi_v2/source_selection.snapshot.json"
    guard = "artifacts/vendor/hdapi_v2/v1_legacy_guard.log"
    require_file(source, body)
    require_file(guard, body)
    require_contains(source, '"legacy_v1_bodygraph_route_family":"legacy_v1_bodygraph"', body)
    require_contains(guard, "legacy_v1_bodygraph", body)
    require_contains(guard, "status=PASS", body)
    return [source, guard], [], []


def check_po003(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    snapshot = "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"
    client = "engine/bodygraph/vendor_client.py"
    require_file(snapshot, body)
    require_file(client, body)
    require_contains(snapshot, '"version_owner":"HD_API_BASE_URL"', body)
    require_contains(snapshot, '"resource_path":"charts/coordinates"', body)
    require_contains(snapshot, '"no_double_prefix_posture":true', body)
    require_contains(client, "def join_vendor_resource_url", body)
    require_contains(client, "HD_API_BASE_URL", body)
    return [snapshot, client], [], []


def check_po004(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"
    require_file(artifact, body)
    require_contains(
        artifact, '"v2_auth_header_posture":"Authorization: Bearer <redacted>"', body
    )
    require_contains(
        artifact, '"v1_legacy_auth_header_posture":"HD-Api-Key: <redacted>"', body
    )
    require_contains(artifact, '"credential_env_var":"HD_API_KEY"', body)
    require_contains(artifact, "<redacted>", body)
    return [artifact], [], []


def check_po005(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"
    require_file(artifact, body)
    require_contains(artifact, '"geocode_env_var":"GEO_API_KEY"', body)
    require_contains(artifact, '"geocode_header_posture":"HD-Geocode-Key: <redacted>"', body)
    require_contains(artifact, '"geocode_key_requirement":"required"', body)
    require_contains(artifact, '"geocode_key_requirement":"not needed"', body)
    require_contains(artifact, '"geocode_env_var":"not applicable"', body)
    return [artifact], [], []


def check_po006(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(artifact, body)
    require_contains(
        artifact,
        '"response_envelope_fields":["timestamp","success","message","errorCode","type","data"]',
        body,
    )
    require_contains(artifact, '"success_status_handling"', body)
    require_contains(artifact, '"errorCode_handling"', body)
    require_contains(artifact, '"data_payload_body_emitted":false', body)
    require_contains(artifact, '"route_variant":"coordinates_chart"', body)
    return [artifact], [], []


def check_po007(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(artifact, body)
    require_contains(artifact, '"schema_gap_status":"GAP_RECORDED"', body)
    require_contains(artifact, '"no_compatibility_by_inference":true', body)
    require_contains(artifact, '"normalized_data_path_proof_claim":"NONE"', body)
    return [artifact], [], []


def check_po008(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"
    require_file(artifact, body)
    require_contains(artifact, "adapter/presenter boundary taxonomy proof", body)
    require_contains(
        artifact, "adapter routes resolve to sanctioned presenter/emitter calls", body
    )
    require_contains(artifact, "bounded_static_grammar_posture", body)
    return [artifact], [], []


def check_po009(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"
    require_file(artifact, body)
    require_regex(artifact, r"fail[- ]closed", body)
    require_contains(artifact, "unproven route-shaped forms fail closed", body)
    require_contains(artifact, "unknown_current_categories_fail_closed", body)
    return [artifact], [], []


def check_po010(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"
    require_file(artifact, body)
    require_contains(artifact, "public_route_drift_proof_repair", body)
    require_contains(
        artifact, "typed analyzer-owned route records replace string-first drift proof", body
    )
    require_contains(artifact, "route_proof_contract_required_fields", body)
    return [artifact], [], []


def check_po011(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "artifacts/vendor/hdapi_v2/closed_rails_refusal.txt"
    require_file(artifact, body)
    require_contains(
        artifact,
        "typed_refusal_posture=PROVIDER_REFUSED before outbound transport under closed rails",
        body,
    )
    require_contains(artifact, "no_dns_socket_http_external_io_posture", body)
    require_contains(artifact, "no_live_vendor_call_claim=NONE", body)
    require_contains(artifact, "status=PASS", body)
    return [artifact], [], []


def check_po012(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifacts = [
        "audit/ops/hde-epic034/ops-02/commands.txt",
        "audit/ops/hde-epic034/ops-02/stdout.log",
        "audit/ops/hde-epic034/ops-02/files_sha256.txt",
        "audit/ops/hde-epic034/ops-02/env_presence_redacted.json",
        "audit/ops/hde-epic034/ops-02/request_summary.json",
        "audit/ops/hde-epic034/ops-02/result_summary.json",
    ]
    for artifact in artifacts:
        require_file(artifact, body)

    result = "audit/ops/hde-epic034/ops-02/result_summary.json"
    request = "audit/ops/hde-epic034/ops-02/request_summary.json"
    env_presence = "audit/ops/hde-epic034/ops-02/env_presence_redacted.json"
    commands = "audit/ops/hde-epic034/ops-02/commands.txt"

    classify_ops_result(result, body)
    require_json_value(result, "classification", "PASS", body)
    require_json_value(result, "exit_code", 0, body)
    require_json_value(result, "vendor_attempted", True, body)
    require_json_value(result, "full_v2_conformance_claim", False, body)
    require_json_value(result, "hde_ferm008_parent_completion_claim", False, body)
    require_json_value(result, "pf09_subtask_id", "HDE-FERM008.2", body)
    require_json_value(result, "raw_secret_persisted", False, body)
    require_json_value(result, "full_vendor_payload_persisted", False, body)

    require_json_value(request, "resource_path", "charts/coordinates", body)
    require_json_value(request, "configured_base_url_key", "HD_API_BASE_URL", body)
    require_json_value(request, "auth_header_posture", "Authorization: Bearer <redacted>", body)
    require_json_value(request, "geocode_key_requirement", "not needed", body)
    require_json_value(
        request,
        "legacy_v2_auth_header_posture",
        "HD-Api-Key not used for v2 chart routes",
        body,
    )

    require_json_value(env_presence, "SAFE_MODE", "0", body)
    require_json_value(env_presence, "ALLOW_NETWORK", "1", body)
    require_json_value(env_presence, "HD_API_BASE_URL", "SET", body)
    require_json_value(env_presence, "HD_API_KEY", "SET", body)
    require_json_value(env_presence, "GEO_API_KEY", "SET", body)

    expected_command = (
        "actual_pass_producing_command=SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev "
        "LC_ALL=C LANG=C TZ=UTC .venv/bin/python "
        "audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py"
    )
    command_text = read_text(commands)
    if expected_command not in command_text:
        raise FailBehavior("MISSING_ACTUAL_PASS_PRODUCING_COMMAND")
    body.append(
        "TEXT_OK audit/ops/hde-epic034/ops-02/commands.txt :: actual_pass_producing_command"
    )
    return artifacts, [], []


def check_po013(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifacts = [
        "audit/ops/hde-epic034/ops-02/env_presence_redacted.json",
        "audit/ops/hde-epic034/ops-02/request_summary.json",
        "audit/ops/hde-epic034/ops-02/result_summary.json",
    ]
    for artifact in artifacts:
        require_file(artifact, body)

    result = "audit/ops/hde-epic034/ops-02/result_summary.json"
    request = "audit/ops/hde-epic034/ops-02/request_summary.json"
    env_presence = "audit/ops/hde-epic034/ops-02/env_presence_redacted.json"

    require_json_value(env_presence, "HD_API_KEY", "SET", body)
    require_json_value(env_presence, "GEO_API_KEY", "SET", body)
    require_json_value(env_presence, "HD_API_BASE_URL", "SET", body)
    require_json_value(result, "raw_secret_persisted", False, body)
    require_json_value(result, "full_vendor_payload_persisted", False, body)
    require_json_value(request, "auth_header_posture", "Authorization: Bearer <redacted>", body)
    require_json_value(
        request,
        "input_tuple_posture",
        "synthetic non-PII coordinates tuple; full request body not persisted",
        body,
    )
    require_json_value(
        request,
        "request_url_posture",
        "redacted base URL; version-neutral resource path joined by HdApiClient",
        body,
    )

    return artifacts, [], []


def check_po014(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"
    require_file(artifact, body)
    require_contains(artifact, "ops02_classification=PASS", body)
    require_contains(
        artifact,
        "validation_rails=closed rails for PR-06 binding; OPS-02 open-rails smoke not rerun",
        body,
    )
    require_contains(artifact, "final_classification=PASS_PR06_EVIDENCE_BINDING_ONLY", body)
    return [artifact], [], []


def check_po015(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"
    require_file(artifact, body)
    require_contains(
        artifact,
        "nonclaim_hde_ferm008_3_error_retry_rate_limit_mapping=true",
        body,
    )
    require_contains(
        artifact,
        "nonclaim_hde_ferm008_4_normalized_live_data_path_proof=true",
        body,
    )
    require_contains(
        artifact,
        "nonclaim_hde_ferm008_5_full_live_conformance_evidence_loop=true",
        body,
    )
    require_contains(
        artifact,
        "nonclaim_full_humandesignapi_v2_runtime_conformance=true",
        body,
    )
    return [artifact], [], []


def check_po016(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"
    require_file(artifact, body)
    require_contains(artifact, "nonclaim_public_reader_change=true", body)
    require_contains(artifact, "nonclaim_public_route=true", body)
    require_contains(artifact, "nonclaim_public_flag=true", body)
    require_contains(artifact, "nonclaim_public_payload_change=true", body)
    require_contains(artifact, "nonclaim_new_http_home=true", body)
    require_contains(artifact, "nonclaim_ai_scope=true", body)
    return [artifact], [], []


def check_po017(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    require_pytest(body)
    artifacts = [
        "tests/bodygraph/test_vendor_client.py",
        "tests/evidence/test_hdapi_v2_contract_inventory.py",
        "tools/evidence/validate_evidence_paths.py",
        "tools/evidence/check_lf_endings.py",
        "tools/evidence/update_evidence_index.py",
        "ci/checks/check_mirror_schema.sh",
        "ci/checks/check_evidence_index_hash.sh",
        "ci/checks/check_final_lf.sh",
        "docs/evidence/INDEX.json",
        "docs/evidence/INDEX.sha256",
        "artifacts/evidence_index.jsonl",
        "artifacts/evidence_index.jsonl.sha256",
        "docs/acceptance_map_epic034.json",
    ]
    for artifact in artifacts:
        require_file(artifact, body)

    run_readonly(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/bodygraph/test_vendor_client.py",
            "tests/evidence/test_hdapi_v2_contract_inventory.py",
        ],
        body,
    )
    run_readonly([sys.executable, "tools/evidence/validate_evidence_paths.py"], body)
    run_readonly([sys.executable, "tools/evidence/check_lf_endings.py"], body)
    run_readonly([sys.executable, "tools/evidence/update_evidence_index.py", "--check"], body)
    run_readonly([sys.executable, "ci/checks/check_mirror_schema.sh"], body)
    run_readonly(["bash", "ci/checks/check_evidence_index_hash.sh"], body)
    run_readonly(["bash", "ci/checks/check_final_lf.sh"], body)

    acceptance = "docs/acceptance_map_epic034.json"
    require_contains(acceptance, '"EVIDENCE_INDEX_UPDATED_OK"', body)
    require_contains(acceptance, '"MACHINE_MIRROR_UPDATED_OK"', body)
    require_contains(acceptance, '"TESTS_PASS_OK"', body)

    intended = [
        "EVIDENCE_INDEX_UPDATED_OK",
        "MACHINE_MIRROR_UPDATED_OK",
        "EVIDENCE_INDEX_HASH_OK",
        "EVIDENCE_PATHS_VALIDATED_OK",
        "EVIDENCE_PATH_PROOFS_OK",
        "TESTS_PASS_OK",
    ]
    return artifacts, intended, intended


def check_po018(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    artifact = "docs/acceptance_map_epic034.json"
    require_file(artifact, body)
    require_contains(artifact, '"acceptance_claims_mode":"baseline_existing_tokens_only"', body)
    require_contains(
        artifact,
        "No vendor-v2-specific acceptance token is minted or claimed.",
        body,
    )
    text = read_text(artifact)
    if "VENDOR_V2_" in text or "HDAPI_V2_ACCEPTANCE" in text:
        raise FailBehavior("VENDOR_SPECIFIC_TOKEN_PRESENT")
    body.append("NO_VENDOR_SPECIFIC_ACCEPTANCE_MARKER_OK")
    return [artifact], [], []


def check_closeout(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    expected = ["step-0b-doc-delta-capture"] + [f"po-{i:03d}" for i in range(1, 19)]
    entries = []
    for check_id in expected:
        log_path = CHECKS_ROOT / check_id / "primary.log"
        proof_path = Path(str(log_path) + ".path_proof.txt")
        if not log_path.exists():
            raise ToolingBlocked(f"NOT_RUN:{check_id}:{log_path}")
        if not proof_path.exists():
            raise ToolingBlocked(f"MISSING_PATH_PROOF:{check_id}:{proof_path}")
        try:
            first_line = log_path.read_text(encoding="utf-8").splitlines()[0]
            header = json.loads(first_line)
        except Exception as exc:
            raise ToolingBlocked(f"UNREADABLE_HEADER:{check_id}") from exc
        entries.append(
            {
                "check_id": check_id,
                "status": header.get("status", "UNKNOWN"),
                "log_path": str(log_path),
                "path_proof_path": str(proof_path),
            }
        )

    manifest = EPIC_QA_ROOT / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": "pf27.qa_step_logs_manifest.v1",
                "epic_id": EPIC_ID,
                "entries": entries,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    write_path_proof(manifest)

    META_ROOT.mkdir(parents=True, exist_ok=True)

    discovery = META_ROOT / "discovery_artifact.md"
    discovery.write_text(
        "\n".join(
            [
                "# HDE-EPIC034 Live QA Discovery Artifact",
                "",
                "Discovery posture: repo loci used by this Live QA plan were prechecked from current repo reality, structured repo audit, or QA-created output posture.",
                "Rails posture: PO-012 is the bounded PO-authorized open-rails Live QA step. All other checks in this closeout run are closed rails.",
                "Out-of-scope boundaries: no public Reader expansion, no public route/flag/payload expansion, no new HTTP home, no AI scope, no full HumanDesignAPI v2 runtime conformance, and no HDE-FERM008 parent completion.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    write_path_proof(discovery)

    rca = META_ROOT / "qa_rca_doc_delta_summary.md"
    rca.write_text(
        "\n".join(
            [
                "# HDE-EPIC034 QA RCA and Doc Delta Summary",
                "",
                "Coverage vs plan:",
                *[
                    f"* {entry['check_id']}: {entry['status']} - {entry['log_path']}"
                    for entry in entries
                ],
                "",
                "Doc-delta posture:",
                "Step-0B records the current HDE-EPIC034 doc-delta surfaces. No PF document edit is performed by this runbook.",
                "",
                "Known non-claims:",
                "No full HumanDesignAPI v2 runtime conformance, no later HDE-FERM008.3/8.4/8.5 completion, no public Reader change, no public route/flag/payload expansion, no new HTTP home, and no AI scope is claimed by this Live QA run.",
                "",
                "Closeout posture:",
                "This closeout assembly check creates QA evidence deliverables only. It does not perform PO closeout, board update, merge, or canon drain.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    write_path_proof(rca)

    body.append(f"manifest={manifest}")
    body.append(f"discovery_artifact={discovery}")
    body.append(f"qa_rca_doc_delta_summary={rca}")

    return [
        str(manifest),
        str(Path(str(manifest) + ".path_proof.txt")),
        str(discovery),
        str(Path(str(discovery) + ".path_proof.txt")),
        str(rca),
        str(Path(str(rca) + ".path_proof.txt")),
    ], [], []


CHECKS: dict[str, tuple[str, Callable[[list[str]], tuple[list[str], list[str], list[str]]]]] = {
    "step-0b-doc-delta-capture": ("Step-0B - Doc Delta Capture", check_step0b),
    "po-001": ("PO-001", check_po001),
    "po-002": ("PO-002", check_po002),
    "po-003": ("PO-003", check_po003),
    "po-004": ("PO-004", check_po004),
    "po-005": ("PO-005", check_po005),
    "po-006": ("PO-006", check_po006),
    "po-007": ("PO-007", check_po007),
    "po-008": ("PO-008", check_po008),
    "po-009": ("PO-009", check_po009),
    "po-010": ("PO-010", check_po010),
    "po-011": ("PO-011", check_po011),
    "po-012": ("PO-012", check_po012),
    "po-013": ("PO-013", check_po013),
    "po-014": ("PO-014", check_po014),
    "po-015": ("PO-015", check_po015),
    "po-016": ("PO-016", check_po016),
    "po-017": ("PO-017", check_po017),
    "po-018": ("PO-018", check_po018),
    "qa-19-close-out-deliverables": ("Close-out deliverables", check_closeout),
}


def run(check_id: str) -> int:
    if check_id not in CHECKS:
        print(f"UNKNOWN_CHECK:{check_id}", file=sys.stderr)
        return 99

    check_name, check_func = CHECKS[check_id]
    check_root = CHECKS_ROOT / check_id
    check_root.mkdir(parents=True, exist_ok=True)

    primary_log = check_root / "primary.log"
    primary_proof = Path(str(primary_log) + ".path_proof.txt")
    command_text = f"python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py {check_id}"

    body = [
        f"check_id={check_id}",
        f"check_name={check_name}",
        f"command={command_text}",
        "rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev",
        "pins=LC_ALL=C LANG=C TZ=UTC",
    ]

    status = "PASS"
    exit_code = 0
    evidence_artifacts: list[str] = []
    intended_tokens: list[str] = []
    claimed_tokens: list[str] = []

    try:
        evidence_artifacts, intended_tokens, claimed_on_pass = check_func(body)
        claimed_tokens = claimed_on_pass
    except ToolingBlocked as exc:
        status = "TOOLING_BLOCKED"
        exit_code = 99
        body.append(f"TOOLING_BLOCKED:{exc}")
    except FailBehavior as exc:
        status = "FAIL_BEHAVIOR"
        exit_code = 1
        body.append(f"FAIL_BEHAVIOR:{exc}")
    except Exception as exc:
        status = "FAIL_TOOLING"
        exit_code = 2
        body.append(f"FAIL_TOOLING:{type(exc).__name__}:{exc}")

    if status != "PASS":
        claimed_tokens = []

    artifacts = [str(primary_log), str(primary_proof), *evidence_artifacts]

    header = {
        "schema_version": "pf27.step_log_header.v1",
        "timestamp_utc": utc_now(),
        "check_id": check_id,
        "check_name": check_name,
        "status": status,
        "fail_status": "" if status == "PASS" else status,
        "command": command_text,
        "command_provenance": "Copy/paste from PO instructions via QA-created harness",
        "exit_code": exit_code,
        "evidence_artifacts": artifacts,
        "captured_env": {
            "SAFE_MODE": os.environ.get("SAFE_MODE", ""),
            "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", ""),
            "APP_ENV": os.environ.get("APP_ENV", ""),
            "LC_ALL": os.environ.get("LC_ALL", ""),
            "LANG": os.environ.get("LANG", ""),
            "TZ": os.environ.get("TZ", ""),
        },
        "pf_refs": [
            "PF10 - HDE-Build Notes",
            "PF19 - Glow QA Guide",
            "PF27 - Canon Plan Templates",
        ],
        "intended_tokens": intended_tokens,
        "claimed_tokens": claimed_tokens,
    }

    primary_log.write_text(
        json.dumps(header, ensure_ascii=False) + "\n" + "\n".join(body) + "\n",
        encoding="utf-8",
    )
    write_path_proof(primary_log)

    print(f"{check_id} status={status} exit_code={exit_code} primary={primary_log}")
    return exit_code


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: hde034_live_qa_harness.py <check_id>", file=sys.stderr)
        raise SystemExit(99)
    raise SystemExit(run(sys.argv[1]))
