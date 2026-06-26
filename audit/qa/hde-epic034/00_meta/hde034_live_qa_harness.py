from __future__ import annotations

import datetime
import hashlib
import json
import os
import sys
from pathlib import Path

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


CHECKS = {
    "step-0b-doc-delta-capture": ("Step-0B - Doc Delta Capture", check_step0b),
    "po-001": ("PO-001", check_po001),
    "po-002": ("PO-002", check_po002),
    "po-003": ("PO-003", check_po003),
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
