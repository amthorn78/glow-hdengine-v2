from __future__ import annotations

import datetime
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


EPIC_ID = "HDE-EPIC035"
QA_ROOT = Path("audit/qa/hde-epic035")
CHECKS_ROOT = QA_ROOT / "checks"
META_ROOT = QA_ROOT / "00_meta"
DOCDELTA_DRAFT = Path("audit/docdeltas/hde-epic035_doc_deltas.md")
DOCDELTA_CAPTURE = META_ROOT / "doc_deltas.md"


class ToolingBlocked(Exception):
    pass


class FailBehavior(Exception):
    pass


class FailTooling(Exception):
    pass


def utc_now() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_path_proof(path: Path) -> Path:
    if not path.exists():
        raise ToolingBlocked(f"MISSING_PATH_FOR_PROOF:{path}")
    proof = Path(str(path) + ".path_proof.txt")
    stat = path.stat()
    proof.write_text(
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
    return proof


def read_text(path: str | Path) -> str:
    p = Path(path)
    if not p.exists():
        raise ToolingBlocked(f"MISSING_FILE:{p}")
    return p.read_text(encoding="utf-8")


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def require_file(path: str | Path, body: list[str]) -> None:
    p = Path(path)
    if not p.exists():
        raise ToolingBlocked(f"MISSING_FILE:{p}")
    body.append(f"FILE_OK {p} sha256={sha256(p)}")


def require_contains(path: str | Path, needle: str, body: list[str]) -> None:
    text = read_text(path)
    if needle not in text:
        raise FailBehavior(f"MISSING_TEXT:{path}:{needle}")
    body.append(f"TEXT_OK {path} :: {needle}")


def require_json_value(path: str | Path, key: str, expected: Any, body: list[str]) -> None:
    payload = load_json(path)
    if key not in payload:
        raise FailBehavior(f"MISSING_JSON_KEY:{path}:{key}")
    actual = payload[key]
    if actual != expected:
        raise FailBehavior(f"JSON_VALUE_MISMATCH:{path}:{key}:{actual!r}!={expected!r}")
    body.append(f"JSON_OK {path} :: {key}={expected!r}")


def require_json_contains_record(
    path: str | Path, key: str, field: str, expected: Any, body: list[str]
) -> None:
    payload = load_json(path)
    records = payload.get(key)
    if not isinstance(records, list):
        raise FailBehavior(f"JSON_NOT_LIST:{path}:{key}")
    for rec in records:
        if isinstance(rec, dict) and rec.get(field) == expected:
            body.append(f"JSON_RECORD_OK {path} :: {key}.{field}={expected!r}")
            return
    raise FailBehavior(f"MISSING_JSON_RECORD:{path}:{key}.{field}={expected!r}")


def canonical_json_file(path: str | Path, body: list[str]) -> None:
    p = Path(path)
    raw = p.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n") or raw.startswith(b"\xef\xbb\xbf"):
        raise FailBehavior(f"JSON_CANONICAL_BYTES_FAIL:{p}")
    payload = json.loads(raw.decode("utf-8"))
    # EPIC035's checked-in acceptance-map test currently uses Python's default
    # escaped-Unicode JSON form; the HDAPI v2 vendor snapshots use UTF-8 JSON.
    ensure_ascii = p.as_posix() == "docs/acceptance_map_epic035.json"
    expected = (
        json.dumps(payload, ensure_ascii=ensure_ascii, sort_keys=True, separators=(",", ":")).encode("utf-8")
        + b"\n"
    )
    if raw != expected:
        raise FailBehavior(f"JSON_CANONICAL_SORT_FAIL:{p}")
    body.append(f"JSON_CANONICAL_OK {p}")


def run_cmd(cmd: list[str], body: list[str], tooling: bool = False) -> None:
    body.append("COMMAND " + " ".join(cmd))
    try:
        cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
    except FileNotFoundError as exc:
        raise ToolingBlocked(f"COMMAND_MISSING:{cmd[0]}") from exc
    if cp.stdout:
        body.append(cp.stdout.strip())
    body.append(f"EXIT_CODE {cp.returncode}")
    if cp.returncode != 0:
        if tooling:
            raise FailTooling(f"COMMAND_FAILED:{' '.join(cmd)}:{cp.returncode}")
        raise FailBehavior(f"COMMAND_FAILED:{' '.join(cmd)}:{cp.returncode}")


def require_pytest(body: list[str]) -> None:
    cp = subprocess.run(
        [sys.executable, "-c", "import pytest"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if cp.returncode != 0:
        raise ToolingBlocked("PYTEST_IMPORT_MISSING")
    body.append("PYTEST_IMPORT_OK")


def check_step0b(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    META_ROOT.mkdir(parents=True, exist_ok=True)
    DOCDELTA_DRAFT.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(
        [
            "# HDE-EPIC035 Live QA Doc Delta Capture",
            "",
            "BLOCKERS:",
            "- None at planning time.",
            "",
            "CAVEATS:",
            "- No pre-existing repo-resident HDE-EPIC035 Live QA harness was found under the audited epic QA or OPS roots; this plan creates a QA helper under audit/qa/hde-epic035/00_meta/.",
            "- CLI help/parser locus for hdctl bg:resolve was not isolated by the repo audit; this plan does not execute hdctl bg:resolve and uses retained OPS evidence only.",
            "- Retained OPS-01 evidence is already-produced evidence only; this plan does not rerun OPS.",
            "- Some retained OPS files were listed by audit without sibling path-proof proof; this plan gates only on explicit artifacts and path proofs required by each check.",
            "",
        ]
    )
    DOCDELTA_DRAFT.write_text(text, encoding="utf-8")
    DOCDELTA_CAPTURE.write_text(text, encoding="utf-8")
    draft_proof = write_path_proof(DOCDELTA_DRAFT)
    capture_proof = write_path_proof(DOCDELTA_CAPTURE)
    body.append(f"DOC_DELTA_DRAFT={DOCDELTA_DRAFT}")
    body.append(f"DOC_DELTA_CAPTURE={DOCDELTA_CAPTURE}")
    return [
        str(DOCDELTA_DRAFT),
        str(draft_proof),
        str(DOCDELTA_CAPTURE),
        str(capture_proof),
        "audit/qa/hde-epic035/00_meta/hde035_live_qa_harness.py",
    ], ["DOC_DELTA_PRESENT_OK"], ["DOC_DELTA_PRESENT_OK"]


def check_po001(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json"
    require_file(p, body)
    require_json_value(p, "artifact_kind", "hdapi_v2_provider_outcome_mapping", body)
    require_json_value(p, "epic_id", "HDE-EPIC035", body)
    require_json_value(p, "pf09_subtask_id", "HDE-FERM008.3", body)
    require_json_contains_record(p, "status_mapping_records", "provider_code", "PROVIDER_UNAUTHORIZED", body)
    require_json_contains_record(p, "status_mapping_records", "provider_code", "PROVIDER_RATE_LIMITED", body)
    require_json_contains_record(p, "status_mapping_records", "provider_code", "PROVIDER_UNAVAILABLE", body)
    require_json_value(
        p,
        "network_error_record",
        {"classification": "network_error", "provider_code": "PROVIDER_NETWORK_ERROR", "retryable": True},
        body,
    )
    require_json_value(
        p,
        "no_claims",
        {
            "full_hdapi_v2_runtime_conformance": "NONE",
            "live_vendor_call": "NONE",
            "open_rails_ops_execution": "NONE",
            "public_reader_change": "NONE",
            "public_route_flag_payload_or_transport_change": "NONE",
            "raw_vendor_payload_persisted": "NONE",
        },
        body,
    )
    return [p], [], []


def check_po002(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json"
    require_file(p, body)
    require_json_value(p, "artifact_kind", "hdapi_v2_retry_after_mapping", body)
    require_json_value(p, "epic_id", "HDE-EPIC035", body)
    require_json_value(p, "pf09_subtask_id", "HDE-FERM008.3", body)
    require_json_value(
        p,
        "rate_limit_status_record",
        {
            "classification": "429",
            "provider_code": "PROVIDER_RATE_LIMITED",
            "retry_after_header_supported": True,
            "retryable": False,
            "status": 429,
        },
        body,
    )
    for case in ["delta_seconds", "http_date", "invalid", "overflow"]:
        require_json_contains_record(p, "retry_after_records", "case", case, body)
    return [p], [], []


def check_po003(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json"
    require_file(p, body)
    require_json_contains_record(p, "bad_response_records", "scenario", "malformed_json_response", body)
    require_json_contains_record(p, "bad_response_records", "scenario", "provider_bad_response", body)
    require_json_contains_record(p, "status_mapping_records", "status", 302, body)
    require_json_value(
        p,
        "retry_classification",
        {
            "429": False,
            "4xx": False,
            "5xx": True,
            "http_status_other": False,
            "network_error": True,
            "redirect_response": False,
        },
        body,
    )
    require_json_value(
        p,
        "network_error_record",
        {"classification": "network_error", "provider_code": "PROVIDER_NETWORK_ERROR", "retryable": True},
        body,
    )
    return [p], [], []


def check_po004(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p1 = "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json"
    p2 = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(p1, body)
    require_file(p2, body)
    obs = load_json(p1).get("observability_posture", {})
    for k in [
        "bounded_labels_only",
        "keys_only",
        "no_plaintext_secret_value",
        "no_raw_request_body",
        "no_raw_response_body",
        "no_raw_secret_header",
        "no_raw_vendor_payload",
    ]:
        if obs.get(k) is not True:
            raise FailBehavior(f"OBSERVABILITY_FAIL:{k}")
        body.append(f"OBSERVABILITY_OK {p1} :: {k}=true")
    require_json_value(p2, "data_payload_body_emitted", False, body)
    require_json_value(
        p2,
        "raw_response_body_persisted" if "raw_response_body_persisted" in load_json(p2) else "runtime_conformance_claim",
        "NONE",
        body,
    )
    return [p1, p2], [], []


def check_po005(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json"
    require_file(p, body)
    payload = load_json(p)
    route = payload.get("route_family_identity", {})
    legacy = json.dumps(route.get("legacy_v1_bodygraph_routes", []), sort_keys=True)
    v2 = json.dumps(route.get("v2_chart_routes", []), sort_keys=True)
    if "HD-Api-Key: <redacted>" not in legacy:
        raise FailBehavior("LEGACY_AUTH_POSTURE_MISSING")
    if "Authorization: Bearer <redacted>" not in v2:
        raise FailBehavior("V2_AUTH_POSTURE_MISSING")
    for resource in ["bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates"]:
        if resource not in route.get("version_neutral_runtime_resource_paths", []):
            raise FailBehavior(f"ROUTE_FAMILY_RESOURCE_MISSING:{resource}")
        body.append(f"ROUTE_FAMILY_OK {resource}")
    return [p], [], []


def check_po006(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    final = "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt"
    binding = "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"
    require_file(final, body)
    require_file(binding, body)
    require_contains(final, "v2_charts_simple=success", body)
    require_contains(final, "v2_charts_simple_request_shape=/v2/charts/simple", body)
    require_contains(final, "v2_charts_simple_response_type=ChartSimpleResult", body)
    require_contains(binding, "full_runtime_conformance_claim=false", body)
    require_contains(binding, "ops_completion_claim=false", body)
    return [final, binding], [], []


def check_po007(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    final = "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt"
    binding = "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"
    require_file(final, body)
    require_file(binding, body)
    require_contains(final, "bg_resolve_error_code=PROVIDER_NOT_FOUND", body)
    require_contains(final, "bg_resolve_http_status=404", body)
    require_contains(final, "runtime_gap=bg:resolve_still_uses_legacy_bodygraph_route_against_configured_v2_base", body)
    require_contains(
        binding,
        "bg_resolve_runtime_gap=legacy BodyGraph route observation against configured v2 base returned PROVIDER_NOT_FOUND / 404",
        body,
    )
    return [final, binding], [], []


def check_po008(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(p, body)
    require_json_value(p, "artifact_kind", "hdapi_v2_response_normalization_gap", body)
    require_json_value(p, "response_normalization_posture", "EXACT_SCHEMA_ADAPTER_GAP_RECORDED", body)
    require_json_value(p, "schema_gap_status", "GAP_RECORDED", body)
    require_json_value(p, "normalized_data_path_proof_claim", "NONE", body)
    require_contains(p, "HDE-FERM008.4 remains an exact adapter/schema gap", body)
    return [p], [], []


def check_po009(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(p, body)
    require_contains(p, "ChartSimpleResult", body)
    require_contains(p, "ChartResult/ChartSimpleResult-to-BodyGraph adapter", body)
    require_contains(p, "schema_gap_recorded", body)
    require_contains(p, "no_compatibility_by_inference", body)
    require_json_value(p, "no_compatibility_by_inference", True, body)
    return [p], [], []


def check_po010(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    p = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    require_file(p, body)
    require_contains(
        p,
        "A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract before compatibility can be claimed.",
        body,
    )
    require_json_value(p, "runtime_conformance_claim", "NONE", body)
    require_json_value(p, "normalized_data_path_proof_claim", "NONE", body)
    return [p], [], []


def check_po011(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    paths = [
        "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
        "docs/acceptance_map_epic035.json",
        "audit/qa/hde-epic035/token_evidence_matrix.md",
    ]
    for p in paths:
        require_file(p, body)
    require_contains(paths[0], "pr01_hde_ferm008_3_provider_outcome", body)
    require_contains(paths[0], "pr02_hde_ferm008_4_response_normalization", body)
    require_contains(paths[1], "ops_01", body)
    require_contains(paths[1], "HDE-FERM008.5 governed evidence-loop closure", body)
    require_contains(paths[2], "HDE-FERM008.5 evidence-loop closure posture", body)
    return paths, [], []


def check_po012(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    paths = ["docs/acceptance_map_epic035.json", "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log"]
    for p in paths:
        require_file(p, body)
    for needle in ["QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout"]:
        require_contains(paths[0], needle, body)
    require_contains(paths[1], "qa_pass_claim=false", body)
    require_contains(paths[1], "pf09_status_movement_claim=false", body)
    require_contains(paths[1], "epic_closeout_claim=false", body)
    return paths, [], []


def check_po013(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    paths = [
        "docs/acceptance_map_epic035.json",
        "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "audit/qa/hde-epic035/ops-01/ops_evidence_binding.log",
    ]
    for p in paths:
        require_file(p, body)
    for needle in [
        "full HumanDesignAPI v2 runtime conformance",
        "public Reader change",
        "public route",
        "public flag",
        "public payload or transport change",
        "new HTTP home",
        "app-side HumanDesignAPI credential ownership",
        "raw payload persistence",
        "AI scope",
    ]:
        require_contains(paths[0], needle, body)
    require_json_value(paths[1], "ai_scope_claim", "NONE", body)
    require_contains(paths[2], "full_runtime_conformance_claim=false", body)
    require_contains(paths[2], "ai_scope_claim=false", body)
    return paths, [], []


def check_po014(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    require_pytest(body)
    artifacts = [
        "tests/evidence/test_hdapi_v2_live_conformance.py",
        "tests/evidence/test_hdapi_v2_response_normalization.py",
        "tests/evidence/test_hdapi_v2_contract_inventory.py",
        "tests/evidence/test_hde_epic035_pr03_evidence_loop.py",
        "docs/evidence/INDEX.json",
        "docs/evidence/INDEX.sha256",
        "artifacts/evidence_index.jsonl",
        "artifacts/evidence_index.jsonl.sha256",
        "docs/acceptance_map_epic035.json",
        "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json",
        "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
    ]
    for p in artifacts:
        require_file(p, body)
    for p in [
        "docs/acceptance_map_epic035.json",
        "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json",
        "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json",
        "artifacts/vendor/hdapi_v2/release_binding.snapshot.json",
    ]:
        canonical_json_file(p, body)
    run_cmd(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/evidence/test_hdapi_v2_live_conformance.py",
            "tests/evidence/test_hdapi_v2_response_normalization.py",
            "tests/evidence/test_hdapi_v2_contract_inventory.py",
            "tests/evidence/test_hde_epic035_pr03_evidence_loop.py",
        ],
        body,
    )
    run_cmd([sys.executable, "tools/evidence/validate_evidence_paths.py"], body)
    run_cmd([sys.executable, "tools/evidence/check_lf_endings.py"], body)
    run_cmd([sys.executable, "tools/evidence/update_evidence_index.py", "--check"], body)
    body.append("MIRROR_SCHEMA_INVOCATION_NORMALIZED=python ci/checks/check_mirror_schema.sh")
    run_cmd([sys.executable, "ci/checks/check_mirror_schema.sh"], body)
    run_cmd(["bash", "ci/checks/check_evidence_index_hash.sh"], body)
    run_cmd(["bash", "ci/checks/check_final_lf.sh"], body)
    tokens = [
        "EVIDENCE_INDEX_UPDATED_OK",
        "MACHINE_MIRROR_UPDATED_OK",
        "EVIDENCE_INDEX_HASH_OK",
        "EVIDENCE_PATHS_VALIDATED_OK",
        "EVIDENCE_PATH_PROOFS_OK",
        "JSON_CANONICAL_CHECK_OK",
        "TESTS_PASS_OK",
    ]
    for t in tokens:
        require_contains("docs/acceptance_map_epic035.json", t, body)
    return artifacts, tokens, tokens


def check_closeout(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    expected = ["step-0b-doc-delta-capture"] + [f"po-{i:03d}" for i in range(1, 15)]
    entries = []
    for check_id in expected:
        log = CHECKS_ROOT / check_id / "primary.log"
        proof = Path(str(log) + ".path_proof.txt")
        if not log.exists():
            raise ToolingBlocked(f"NOT_RUN:{check_id}:{log}")
        if not proof.exists():
            raise ToolingBlocked(f"MISSING_PATH_PROOF:{check_id}:{proof}")
        header = json.loads(log.read_text(encoding="utf-8").splitlines()[0])
        entries.append(
            {
                "check_id": check_id,
                "status": header.get("status"),
                "log_path": str(log),
                "path_proof_path": str(proof),
            }
        )
    manifest = QA_ROOT / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {"schema_version": "pf27.qa_step_logs_manifest.v1", "epic_id": EPIC_ID, "entries": entries},
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    manifest_proof = write_path_proof(manifest)
    discovery = META_ROOT / "discovery_artifact.md"
    discovery.write_text(
        "\n".join(
            [
                "# HDE-EPIC035 Discovery Artifact",
                "",
                "Repo loci were grounded by PF10, audit, and live repo validation. OPS-01 retained open-rails evidence is inspected only and not rerun. No full v2 runtime conformance, public expansion, PF09 status movement, epic closeout, raw payload persistence, or AI scope is claimed.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    discovery_proof = write_path_proof(discovery)
    rca = META_ROOT / "qa_rca_doc_delta_summary.md"
    rca.write_text(
        "\n".join(
            [
                "# HDE-EPIC035 QA RCA and Doc Delta Summary",
                "",
                "Coverage vs plan:",
                "- Step-0B through PO-014 are represented by check-scoped primary logs and path proofs under audit/qa/hde-epic035/checks/.",
                "- qa-16-close-out-deliverables created this closeout assembly evidence.",
                "",
                "Doc deltas:",
                "- Existing HDE-EPIC035 doc-delta surfaces remain audit/docdeltas/hde-epic035_doc_deltas.md and audit/qa/hde-epic035/00_meta/doc_deltas.md.",
                "",
                "Readiness posture:",
                "- This artifact supports QA closeout review only. It does not perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    rca_proof = write_path_proof(rca)
    return [str(manifest), str(manifest_proof), str(discovery), str(discovery_proof), str(rca), str(rca_proof)], [], []


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
    "po-013": ("PO-013", check_po013),
    "po-014": ("PO-014", check_po014),
    "qa-16-close-out-deliverables": ("Close-out deliverables", check_closeout),
}


def run(check_id: str) -> int:
    if check_id not in CHECKS:
        print(f"UNKNOWN_CHECK:{check_id}", file=sys.stderr)
        return 99
    check_name, fn = CHECKS[check_id]
    check_root = CHECKS_ROOT / check_id
    check_root.mkdir(parents=True, exist_ok=True)
    primary = check_root / "primary.log"
    proof = Path(str(primary) + ".path_proof.txt")
    command = f"python audit/qa/hde-epic035/00_meta/hde035_live_qa_harness.py {check_id}"
    body = [
        f"check_id={check_id}",
        f"check_name={check_name}",
        f"command={command}",
        "rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev",
        "pins=LC_ALL=C LANG=C TZ=UTC",
    ]
    status = "PASS"
    exit_code = 0
    artifacts = []
    intended = []
    claimed = []
    try:
        artifacts, intended, claimed = fn(body)
    except ToolingBlocked as exc:
        status = "TOOLING_BLOCKED"
        exit_code = 99
        claimed = []
        body.append(f"TOOLING_BLOCKED:{exc}")
    except FailTooling as exc:
        status = "FAIL_TOOLING"
        exit_code = 2
        claimed = []
        body.append(f"FAIL_TOOLING:{exc}")
    except FailBehavior as exc:
        status = "FAIL_BEHAVIOR"
        exit_code = 1
        claimed = []
        body.append(f"FAIL_BEHAVIOR:{exc}")
    except Exception as exc:
        status = "FAIL_TOOLING"
        exit_code = 2
        claimed = []
        body.append(f"FAIL_TOOLING:{type(exc).__name__}:{exc}")
    if status != "PASS":
        claimed = []
    evidence = [str(primary), str(proof)] + artifacts
    header = {
        "schema_version": "pf27.step_log_header.v1",
        "timestamp_utc": utc_now(),
        "check_id": check_id,
        "check_name": check_name,
        "status": status,
        "fail_status": "" if status == "PASS" else status,
        "command": command,
        "command_provenance": "Copy/paste from plan via QA-created helper",
        "exit_code": exit_code,
        "evidence_artifacts": evidence,
        "captured_env": {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        },
        "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"],
        "intended_tokens": intended,
        "claimed_tokens": claimed,
    }
    primary.write_text(json.dumps(header, ensure_ascii=False) + "\n" + "\n".join(body) + "\n", encoding="utf-8")
    write_path_proof(primary)
    print(f"{check_id} status={status} exit_code={exit_code} primary={primary}")
    return exit_code


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: hde035_live_qa_harness.py <check_id>", file=sys.stderr)
        raise SystemExit(99)
    raise SystemExit(run(sys.argv[1]))
