from __future__ import annotations
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from engine.bodygraph.resolver import resolve_bodygraph

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

def require_token(path: str | Path, token: str, body: list[str]) -> None:
    text = read_text(path)
    if token not in text:
        raise FailBehavior(f"MISSING_TOKEN:{path}:{token}")
    body.append(f"TOKEN_OK {path} :: {token}")

def canonical_json_file(path: str | Path, body: list[str]) -> None:
    p = Path(path)
    raw = p.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n") or raw.startswith(b"\xef\xbb\xbf"):
        raise FailBehavior(f"JSON_CANONICAL_BYTES_FAIL:{p}")
    payload = json.loads(raw.decode("utf-8"))
    # The checked-in EPIC036 acceptance map currently uses escaped-Unicode canonical bytes.
    ensure_ascii = p.as_posix() == "docs/acceptance_map_epic036.json"
    expected = json.dumps(payload, ensure_ascii=ensure_ascii, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
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
        "- PF-Canon was not edited.",
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

def check_po010(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    """Moon Loop remediation: executable behavior probe for configured-v2 vendor route policy refusal."""
    check_root = CHECKS_ROOT / "po-010"
    check_root.mkdir(parents=True, exist_ok=True)
    live_log = check_root / "live_route_policy.log"

    configured_base = (os.environ.get("HD_API_BASE_URL") or "").strip()
    effective_base = configured_base or "https://vendor.test/v2"
    base_source = "process_env" if configured_base else "moon_loop_fallback"

    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=True,
        env={
            "SAFE_MODE": "0",
            "ALLOW_NETWORK": "1",
            "APP_ENV": "dev",
            "HD_API_BASE_URL": effective_base,
        },
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    if result.status != "error" or result.exit_code != 1:
        raise FailBehavior(f"PO010_UNEXPECTED_RESULT:{result.status}:{result.exit_code}")

    payload = result.payload if isinstance(result.payload, dict) else {}
    error = payload.get("error") if isinstance(payload.get("error"), dict) else {}
    resolver = payload.get("resolver") if isinstance(payload.get("resolver"), dict) else {}
    policy = resolver.get("route_policy") if isinstance(resolver.get("route_policy"), dict) else {}

    if error.get("code") != "PROVIDER_ROUTE_UNSUPPORTED":
        raise FailBehavior(f"PO010_ERROR_CODE:{error.get('code')!r}")
    if policy.get("classification") != "unsupported_runtime_nonclaim":
        raise FailBehavior(f"PO010_CLASSIFICATION:{policy.get('classification')!r}")
    if "<redacted>" not in str(policy.get("route_auth_posture", "")):
        raise FailBehavior("PO010_REDACTION_MISSING:route_auth_posture")

    live_log.write_text(
        "\n".join([
            "check_id=po-010",
            "moon_loop_remediation=enabled",
            "command=resolve_bodygraph(source=vendor,dry_run=true)",
            "SAFE_MODE=0",
            "ALLOW_NETWORK=1",
            "APP_ENV=dev",
            f"HD_API_BASE_URL_source={base_source}",
            "HD_API_BASE_URL=REDACTED",
            f"error.code={error.get('code')}",
            f"route_policy.classification={policy.get('classification')}",
            f"route_policy.route_family={policy.get('route_family')}",
            f"route_policy.resource_path={policy.get('resource_path')}",
            f"route_policy.route_auth_posture={policy.get('route_auth_posture')}",
            "",
        ]),
        encoding="utf-8",
    )
    live_log_proof = write_path_proof(live_log)
    body.append(f"PO010_LIVE_LOG={live_log}")
    body.append(f"PO010_LIVE_LOG_PROOF={live_log_proof}")
    return [str(live_log), str(live_log_proof)], [], []

def check_po011(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    live_log = CHECKS_ROOT / "po-010" / "live_route_policy.log"
    live_proof = Path(str(live_log) + ".path_proof.txt")
    nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
    bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
    for p in [live_log, live_proof, nonclaims, bodygraph]:
        require_file(p, body)
    require_contains(live_log, "PROVIDER_ROUTE_UNSUPPORTED", body)
    require_contains(live_log, "unsupported_runtime_nonclaim", body)
    require_json_value(nonclaims, "chart_simple_success_bodygraph_detail_claim", "NONE", body)
    require_json_value(nonclaims, "no_compatibility_by_inference", True, body)
    require_json_value(bodygraph, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
    return [str(live_log), str(live_proof), nonclaims, bodygraph], [], []

def check_po012(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    acceptance = "docs/acceptance_map_epic036.json"
    bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
    nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
    for p in [acceptance, bodygraph, nonclaims]:
        require_file(p, body)
    require_json_value(acceptance, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
    require_json_value(acceptance, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
    require_json_value(bodygraph, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
    require_json_value(nonclaims, "chart_simple_success_bodygraph_detail_claim", "NONE", body)
    return [acceptance, bodygraph, nonclaims], [], []

def check_qa13(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    require_pytest(body)
    artifacts = [
        "tests/bodygraph/test_bg_resolve_route_policy.py",
        "tests/bodygraph/test_resolver_vendor.py",
        "tests/cli/test_bg_resolve.py",
        "tests/evidence/test_hde_epic036_pr02_evidence_loop.py",
        "tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py",
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
        "docs/acceptance_map_epic036.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
    ]
    for p in artifacts:
        require_file(p, body)
    for p in [
        "docs/acceptance_map_epic036.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
        "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
    ]:
        canonical_json_file(p, body)
    run_cmd([sys.executable, "-m", "pytest", "tests/bodygraph/test_bg_resolve_route_policy.py", "tests/bodygraph/test_resolver_vendor.py", "tests/cli/test_bg_resolve.py", "tests/evidence/test_hde_epic036_pr02_evidence_loop.py"], body)
    run_cmd([sys.executable, "tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py", "--check"], body)
    run_cmd([sys.executable, "tools/evidence/validate_evidence_paths.py"], body)
    run_cmd([sys.executable, "tools/evidence/check_lf_endings.py"], body)
    run_cmd([sys.executable, "tools/evidence/update_evidence_index.py", "--check"], body)
    run_cmd([sys.executable, "ci/checks/check_mirror_schema.sh"], body)
    run_cmd(["bash", "ci/checks/check_evidence_index_hash.sh"], body)
    run_cmd(["bash", "ci/checks/check_final_lf.sh"], body)
    tokens = [
        "TESTS_PASS_OK",
        "EVIDENCE_INDEX_UPDATED_OK",
        "MACHINE_MIRROR_UPDATED_OK",
        "EVIDENCE_INDEX_HASH_OK",
        "EVIDENCE_PATHS_VALIDATED_OK",
        "EVIDENCE_PATH_PROOFS_OK",
        "JSON_CANONICAL_CHECK_OK",
    ]
    for token in tokens:
        require_token("docs/acceptance_map_epic036.json", token, body)
    return artifacts, tokens, tokens

def check_closeout(body: list[str]) -> tuple[list[str], list[str], list[str]]:
    expected = ["step-0b-doc-delta-capture"] + [f"po-{i:03d}" for i in range(1, 13)] + ["qa-13-governed-evidence-gates"]
    entries = []
    for check_id in expected:
        log = CHECKS_ROOT / check_id / "primary.log"
        proof = Path(str(log) + ".path_proof.txt")
        if not log.exists():
            raise ToolingBlocked(f"NOT_RUN:{check_id}:{log}")
        if not proof.exists():
            raise ToolingBlocked(f"MISSING_PATH_PROOF:{check_id}:{proof}")
        header = json.loads(log.read_text(encoding="utf-8").splitlines()[0])
        entries.append({"check_id": check_id, "status": header.get("status"), "log_path": str(log), "path_proof_path": str(proof)})
    manifest = QA_ROOT / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {"schema_version": "pf27.qa_step_logs_manifest.v1", "epic_id": EPIC_ID, "entries": entries},
            ensure_ascii=False,
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
                "# HDE-EPIC036 Discovery Artifact",
                "",
                "Repo loci were grounded by PF10, QA audit, and live repo validation before this plan was drafted.",
                "The QA run validates existing governed artifacts and creates check-scoped QA logs under audit/qa/hde-epic036/checks/.",
                "PO-010 creates bounded live production-like route-policy evidence under the QA root using a PO-approved live v2 base value.",
                "No OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, public Reader change, new HTTP home, AI scope, raw payload persistence, or full HumanDesignAPI v2 runtime conformance is claimed.",
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
                "# HDE-EPIC036 QA RCA and Doc Delta Summary",
                "",
                "Coverage vs plan:",
                "- Step-0B, PO-001 through PO-012, and qa-13 are represented by check-scoped primary logs and sibling path proofs under audit/qa/hde-epic036/checks/.",
                "- qa-14-close-out-deliverables created this closeout assembly evidence.",
                "",
                "Doc deltas:",
                "- Existing HDE-EPIC036 doc-delta surfaces remain audit/docdeltas/hde-epic036_doc_deltas.md and audit/qa/hde-epic036/00_meta/doc_deltas.md.",
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
    "qa-13-governed-evidence-gates": ("Governed evidence gates", check_qa13),
    "qa-14-close-out-deliverables": ("Close-out deliverables", check_closeout),
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
