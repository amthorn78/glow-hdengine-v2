from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path

from tools.evidence import generate_hdapi_v2_live_conformance as generator
from tools.evidence import update_evidence_index

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


def _parse_utc_iso8601(raw: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    assert parsed.tzinfo == dt.timezone.utc
    assert parsed.microsecond == 0
    return parsed


def _load_path_proof(path: Path) -> dict[str, str]:
    proof = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            proof[key] = value
    return proof


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


def test_live_conformance_evidence_chronology_is_not_backdated() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    mirror_lines = [json.loads(line) for line in (ROOT / "artifacts" / "evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    index_by_path = {entry["discovered_physical_path"]: entry for entry in index}
    mirror_by_path = {entry["discovered_physical_path"]: entry for entry in mirror_lines}

    for path in REQUIRED_ARTIFACTS:
        rel = path.relative_to(ROOT).as_posix()
        payload_produced = _parse_utc_iso8601(_assert_canonical_json(path)["generated_at_utc"])
        proof = _load_path_proof(ROOT / f"{rel}.path_proof.txt")
        proof_mtime = _parse_utc_iso8601(proof["mtime_utc"])
        proof_produced = _parse_utc_iso8601(proof["produced_at_utc"])
        index_produced = _parse_utc_iso8601(index_by_path[rel]["produced_at_utc"])
        mirror_produced = _parse_utc_iso8601(mirror_by_path[rel]["produced_at_utc"])

        assert proof_produced >= proof_mtime
        assert index_produced == payload_produced
        assert mirror_produced == payload_produced


def test_epic035_index_entries_use_payload_timestamp_not_checkout_mtime(monkeypatch, tmp_path) -> None:
    vendor_dir = tmp_path / "artifacts" / "vendor" / "hdapi_v2"
    vendor_dir.mkdir(parents=True)
    generated_at = "2026-06-28T07:46:52Z"
    future = dt.datetime(2026, 6, 29, 12, 0, tzinfo=dt.timezone.utc).timestamp()
    for name in ["error_mapping.snapshot.json", "rate_limit_headers.snapshot.json"]:
        path = vendor_dir / name
        path.write_text(json.dumps({"generated_at_utc": generated_at}) + "\n", encoding="utf-8")
        path.touch()
        os.utime(path, (future, future))

    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    entries = update_evidence_index._load_epic035_pr01_entries()

    assert entries
    assert {entry["produced_at_utc"] for entry in entries} == {generated_at}


def test_machine_mirror_path_proofs_are_not_backdated() -> None:
    for rel in ["artifacts/evidence_index.jsonl", "artifacts/evidence_index.jsonl.sha256"]:
        proof = _load_path_proof(ROOT / f"{rel}.path_proof.txt")
        proof_mtime = _parse_utc_iso8601(proof["mtime_utc"])
        proof_produced = _parse_utc_iso8601(proof["produced_at_utc"])
        assert proof_produced >= proof_mtime


def test_generator_refuses_non_closed_rails_without_writing(monkeypatch) -> None:
    before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in REQUIRED_ARTIFACTS}
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")

    try:
        generator.main([])
    except SystemExit as exc:
        assert "HDAPI_V2_LIVE_CONFORMANCE_CLOSED_RAILS_REQUIRED" in str(exc)
    else:  # pragma: no cover - explicit failure path
        raise AssertionError("generator accepted non-closed rails")

    for path, (body, mtime_ns) in before.items():
        assert path.read_bytes() == body
        assert path.stat().st_mtime_ns == mtime_ns


def test_generator_refuses_network_enabled_check_without_certifying(monkeypatch) -> None:
    before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in REQUIRED_ARTIFACTS}
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")

    try:
        generator.main(["--check"])
    except SystemExit as exc:
        assert "HDAPI_V2_LIVE_CONFORMANCE_CLOSED_RAILS_REQUIRED" in str(exc)
    else:  # pragma: no cover - explicit failure path
        raise AssertionError("generator check accepted network-enabled rails")

    for path, (body, mtime_ns) in before.items():
        assert path.read_bytes() == body
        assert path.stat().st_mtime_ns == mtime_ns
