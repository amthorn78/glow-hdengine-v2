from __future__ import annotations
import datetime
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

EPIC_ID = "HDE-EPIC036"
QA_ROOT = Path("audit/qa/hde-epic036")
CHECKS_ROOT = QA_ROOT / "checks"
META_ROOT = QA_ROOT / "00_meta"
DOCDELTA_DRAFT = Path("audit/docdeltas/hde-epic036_doc_deltas.md")
DOCDELTA_CAPTURE = META_ROOT / "doc_deltas.md"

class ToolingBlocked(Exception): pass
class FailBehavior(Exception): pass
class FailTooling(Exception): pass

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
        "\n".join([
            f"path: {path}",
            f"size_bytes: {stat.st_size}",
            f"sha256: {sha256(path)}",
            f"mtime_utc: {datetime.datetime.utcfromtimestamp(stat.st_mtime).replace(microsecond=0).isoformat()}Z",
            f"produced_at_utc: {utc_now()}",
            "",
        ]),
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

def require_json_value(path: str | Path, dotted_key: str, expected: Any, body: list[str]) -> None:
    payload: Any = load_json(path)
    for key in dotted_key.split("."):
        if not isinstance(payload, dict) or key not in payload:
            raise FailBehavior(f"MISSING_JSON_KEY:{path}:{dotted_key}")
        payload = payload[key]
    if payload != expected:
        raise FailBehavior(f"JSON_VALUE_MISMATCH:{path}:{dotted_key}:{payload!r}!={expected!r}")
    body.append(f"JSON_OK {path} :: {dotted_key}={expected!r}")

def require_json_list_contains(path: str | Path, dotted_key: str, expected: Any, body: list[str]) -> None:
    payload: Any = load_json(path)
    for key in dotted_key.split("."):
        if not isinstance(payload, dict) or key not in payload:
            raise FailBehavior(f"MISSING_JSON_KEY:{path}:{dotted_key}")
        payload = payload[key]
    if not isinstance(payload, list) or expected not in payload:
        raise FailBehavior(f"JSON_LIST_MISSING:{path}:{dotted_key}:{expected!r}")
    body.append(f"JSON_LIST_OK {path} :: {dotted_key} contains {expected!r}")

def check_step0b(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    META_ROOT.mkdir(parents=True, exist_ok=True)
    DOCDELTA_DRAFT.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join([
        "# HDE-EPIC036 Live QA Doc Delta Capture",
        "",
        "BLOCKERS:",
        "- None at planning time.",
        "",
        "CAVEATS:",
        "- Existing audit reported no repo-resident HDE-EPIC036 OPS-01 evidence root.",
        "- Bounded live production-like route-policy proof is required by this plan and is executed as PO-010 under the QA root.",
        "- PO-010 uses a PO-approved live v2 base value and expects configured-v2 refusal before legacy BodyGraph request construction.",
        "- This plan does not claim OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, public Reader change, new HTTP home, AI scope, raw payload persistence, or full HumanDesignAPI v2 runtime conformance.",
        "",
    ])
    DOCDELTA_DRAFT.write_text(text, encoding="utf-8")
    DOCDELTA_CAPTURE.write_text(text, encoding="utf-8")
    draft_proof = write_path_proof(DOCDELTA_DRAFT)
    capture_proof = write_path_proof(DOCDELTA_CAPTURE)
    helper = Path("audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py")
    helper_proof = write_path_proof(helper)
    body.append(f"DOC_DELTA_DRAFT={DOCDELTA_DRAFT}")
    body.append(f"DOC_DELTA_CAPTURE={DOCDELTA_CAPTURE}")
    body.append(f"QA_HELPER={helper}")
    return [str(DOCDELTA_DRAFT), str(draft_proof), str(DOCDELTA_CAPTURE), str(capture_proof), str(helper), str(helper_proof)], ["DOC_DELTA_PRESENT_OK"], ["DOC_DELTA_PRESENT_OK"]

def check_po001(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
    shape = "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json"
    test = "tests/bodygraph/test_bg_resolve_route_policy.py"
    for p in [route, shape, test]:
        require_file(p, body)
    require_json_value(route, "epic_id", EPIC_ID, body)
    require_json_value(route, "configured_v2_policy.classification", "unsupported_runtime_nonclaim", body)
    require_json_value(route, "configured_v2_policy.supported", False, body)
    require_json_value(route, "configured_v2_policy.error_code", "PROVIDER_ROUTE_UNSUPPORTED", body)
    require_json_value(shape, "configured_v2_bg_resolve_request_shape", "NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM", body)
    require_contains(test, "assert calls == []", body)
    return [route, shape, test], ["NO_EXTERNAL_IO_ON_REFUSAL_OK"], ["NO_EXTERNAL_IO_ON_REFUSAL_OK"]

def check_po002(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
    decision = "audit/qa/hde-epic036/route_policy_decision.log"
    for p in [route, decision]:
        require_file(p, body)
    require_json_value(route, "selected_posture", "unsupported_runtime_nonclaim", body)
    require_json_value(route, "supported_postures.unsupported_runtime_nonclaim", "SELECTED_FOR_CONFIGURED_V2_BASE", body)
    require_json_value(route, "supported_postures.explicit_legacy_fallback", "PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE", body)
    require_json_value(route, "legacy_fallback_policy.classification", "explicit_legacy_fallback", body)
    require_contains(decision, "explicit_legacy_fallback=PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE", body)
    return [route, decision], ["ENV_RAILS_POLICY_OK"], ["ENV_RAILS_POLICY_OK"]

def check_po003(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
    route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
    response = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    for p in [bodygraph, route, response]:
        require_file(p, body)
    require_json_value(bodygraph, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
    require_json_value(route, "route_family_identity.v2_chart_candidate.bodygraph_detail_sufficiency", "NOT_CLAIMED", body)
    require_contains(response, "ChartSimpleResult", body)
    require_contains(bodygraph, "NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI", body)
    return [bodygraph, route, response], [], []

def check_po004(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
    response = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
    for p in [bodygraph, response]:
        require_file(p, body)
    require_json_value(bodygraph, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
    require_json_value(bodygraph, "adapter_sufficiency", "NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI", body)
    require_json_value(response, "normalized_data_path_proof_claim", "NONE", body)
    require_json_value(response, "schema_gap_status", "GAP_RECORDED", body)
    return [bodygraph, response], [], []

def check_po005(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
    test = "tests/bodygraph/test_bg_resolve_route_policy.py"
    for p in [route, test]:
        require_file(p, body)
    require_json_value(route, "legacy_fallback_policy.classification", "explicit_legacy_fallback", body)
    require_json_value(route, "legacy_fallback_policy.supported", True, body)
    require_json_value(route, "legacy_fallback_policy.configured_base_version", "v1", body)
    require_json_value(route, "configured_v2_policy.supported", False, body)
    require_contains(test, "test_explicit_legacy_fallback_remains_available_for_non_v2_configured_base", body)
    return [route, test], [], []

def check_po006(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
    shape = "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json"
    for p in [nonclaims, shape]:
        require_file(p, body)
    for key in ["raw_payload_persistence", "raw_request_body_persisted", "raw_response_body_persisted", "app_side_humandesignapi_credential_ownership"]:
        require_json_value(nonclaims, f"no_claims.{key}", "NONE", body)
    require_json_value(shape, "raw_request_body_persisted", False, body)
    require_json_value(shape, "raw_response_body_persisted", False, body)
    require_json_value(shape, "raw_vendor_payload_persisted", False, body)
    return [nonclaims, shape], [], []

def check_po007(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    acceptance = "docs/acceptance_map_epic036.json"
    binding = "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json"
    decision = "audit/qa/hde-epic036/route_policy_decision.log"
    for p in [acceptance, binding, decision]:
        require_file(p, body)
    for nonclaim in ["QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout"]:
        require_json_list_contains(acceptance, "nonclaims", nonclaim, body)
    require_json_value(binding, "policy_binding.ops_01_requirement", "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.", body)
    require_contains(decision, "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.", body)
    return [acceptance, binding, decision], [], []

def check_po008(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    paths = [
        "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
        "audit/qa/hde-epic036/route_policy_decision.log",
    ]
    for p in paths:
        require_file(p, body)
        require_file(p + ".path_proof.txt", body)
    require_json_value(paths[4], "policy_binding.selected_classification", "unsupported_runtime_nonclaim", body)
    require_json_value(paths[4], "policy_binding.hde_ferm008_6_completion_role", "Complete in this epic for route-policy classification only", body)
    return paths + [p + ".path_proof.txt" for p in paths], [], []

def check_po009(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
    acceptance = "docs/acceptance_map_epic036.json"
    decision = "audit/qa/hde-epic036/route_policy_decision.log"
    for p in [nonclaims, acceptance, decision]:
        require_file(p, body)
    for key in ["public_reader_change", "public_route", "public_flag", "public_payload_change", "new_http_home", "app_side_humandesignapi_credential_ownership", "full_hdapi_v2_runtime_conformance", "raw_payload_persistence", "ai_scope"]:
        require_json_value(nonclaims, f"no_claims.{key}", "NONE", body)
    for needle in ["no_public_reader_change=true", "no_public_route=true", "no_ai_scope=true", "no_full_hdapi_v2_runtime_conformance=true"]:
        require_contains(decision, needle, body)
    return [nonclaims, acceptance, decision], [], []

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
    command = f"python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py {check_id}"
    body = [f"check_id={check_id}", f"check_name={check_name}", f"command={command}", "pins=LC_ALL=C LANG=C TZ=UTC"]
    status = "PASS"
    exit_code = 0
    artifacts: list[str] = []
    intended: list[str] = []
    claimed: list[str] = []
    try:
        artifacts, intended, claimed = fn(body)
    except ToolingBlocked as exc:
        status = "TOOLING_BLOCKED"; exit_code = 99; claimed = []; body.append(f"TOOLING_BLOCKED:{exc}")
    except FailTooling as exc:
        status = "FAIL_TOOLING"; exit_code = 2; claimed = []; body.append(f"FAIL_TOOLING:{exc}")
    except FailBehavior as exc:
        status = "FAIL_BEHAVIOR"; exit_code = 1; claimed = []; body.append(f"FAIL_BEHAVIOR:{exc}")
    except Exception as exc:
        status = "FAIL_TOOLING"; exit_code = 2; claimed = []; body.append(f"FAIL_TOOLING:{type(exc).__name__}:{exc}")
    if status != "PASS":
        claimed = []
    captured_env = {
        "SAFE_MODE": os.environ.get("SAFE_MODE", ""),
        "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", ""),
        "APP_ENV": os.environ.get("APP_ENV", ""),
        "LC_ALL": os.environ.get("LC_ALL", ""),
        "LANG": os.environ.get("LANG", ""),
        "TZ": os.environ.get("TZ", ""),
    }
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
        "captured_env": captured_env,
        "pf_refs": ["PF10 — HDE-Build Notes", "PF19 — Glow QA Guide", "PF27 — Canon Plan Templates", "PF05 — HDE CLI/API Vendor Reference", "PF02 — HDE Architecture"],
        "intended_tokens": intended,
        "claimed_tokens": claimed,
    }
    primary.write_text(json.dumps(header, ensure_ascii=False) + "\n" + "\n".join(body) + "\n", encoding="utf-8")
    write_path_proof(primary)
    print(f"{check_id} status={status} exit_code={exit_code} primary={primary}")
    return exit_code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: hde036_live_qa_harness.py <check_id>", file=sys.stderr)
        raise SystemExit(99)
    raise SystemExit(run(sys.argv[1]))
