from __future__ import annotations

import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

EPIC_ID = "HDE-EPIC034"
EPIC_QA_ROOT = Path("audit/qa/hde-epic034")
CHECKS_ROOT = EPIC_QA_ROOT / "checks"


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


CHECKS = {
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
