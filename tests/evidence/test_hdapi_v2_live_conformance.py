from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import generate_hdapi_v2_live_conformance as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED_ARTIFACTS = [
    VENDOR_DIR / "error_mapping.snapshot.json",
    VENDOR_DIR / "rate_limit_headers.snapshot.json",
]


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    assert not raw.startswith(b"\xef\xbb\xbf")
    payload = json.loads(raw.decode("utf-8"))
    expected = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    assert raw == expected
    return payload


def test_generator_rendered_outputs_are_canonical_and_scoped() -> None:
    outputs = generator.render_outputs()
    assert set(outputs) == set(REQUIRED_ARTIFACTS)
    for body in outputs.values():
        assert body.endswith(b"\n")
        assert not body.endswith(b"\n\n")
        payload = json.loads(body.decode("utf-8"))
        assert payload["epic_id"] == "HDE-EPIC035"
        assert payload["pf09_document"] == "PF09.5 — HDE Build Checklist Fermentation"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.3"
        assert payload["no_claims"]["live_vendor_call"] == "NONE"
        assert payload["no_claims"]["full_hdapi_v2_runtime_conformance"] == "NONE"
        assert b"Bearer redacted" not in body
        assert b"HD-Api-Key: redacted" not in body


def test_error_mapping_artifact_covers_provider_codes_retry_and_observability() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "error_mapping.snapshot.json")
    records = {record["status"]: record for record in payload["status_mapping_records"]}
    assert records[401]["provider_code"] == "PROVIDER_UNAUTHORIZED"
    assert records[403]["provider_code"] == "PROVIDER_FORBIDDEN"
    assert records[404]["provider_code"] == "PROVIDER_NOT_FOUND"
    assert records[429]["provider_code"] == "PROVIDER_RATE_LIMITED"
    assert records[500]["provider_code"] == "PROVIDER_UNAVAILABLE"
    assert records[302]["provider_code"] == "PROVIDER_ERROR"
    assert records[302]["classification"] == "http_status_other"
    retry = payload["retry_classification"]
    assert retry["network_error"] is True
    assert retry["5xx"] is True
    assert retry["429"] is False
    assert retry["4xx"] is False
    assert retry["http_status_other"] is False
    assert retry["redirect_response"] is False
    assert payload["network_error_record"]["provider_code"] == "PROVIDER_NETWORK_ERROR"
    assert {item["provider_code"] for item in payload["bad_response_records"]} == {"PROVIDER_BAD_RESPONSE"}
    observability = payload["observability_posture"]
    assert observability["keys_only"] is True
    assert observability["no_raw_request_body"] is True
    assert observability["no_raw_response_body"] is True
    assert observability["no_raw_secret_header"] is True
    assert observability["no_plaintext_secret_value"] is True


def test_rate_limit_artifact_covers_retry_after_forms() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "rate_limit_headers.snapshot.json")
    assert payload["rate_limit_status_record"] == {
        "classification": "429",
        "provider_code": "PROVIDER_RATE_LIMITED",
        "retry_after_header_supported": True,
        "retryable": False,
        "status": 429,
    }
    records = {record["case"]: record for record in payload["retry_after_records"]}
    assert records["delta_seconds"]["parsed_retry_after_ms"] == 7000
    assert records["http_date"]["parsed_retry_after_ms"] == 5000
    assert records["invalid"]["parsed_retry_after_ms"] is None
    assert records["overflow"]["parsed_retry_after_ms"] is None


def test_live_conformance_index_and_path_proof_bindings_when_promoted() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    mirror_lines = [json.loads(line) for line in (ROOT / "artifacts" / "evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    index_paths = {entry["discovered_physical_path"] for entry in index}
    mirror_paths = {entry["discovered_physical_path"] for entry in mirror_lines}
    for path in REQUIRED_ARTIFACTS:
        rel = path.relative_to(ROOT).as_posix()
        assert rel in index_paths
        assert rel in mirror_paths
        proof = ROOT / f"{rel}.path_proof.txt"
        assert proof.exists(), proof
        proof_text = proof.read_text(encoding="utf-8")
        assert f"path: {rel}" in proof_text
        assert "sha256: " in proof_text
