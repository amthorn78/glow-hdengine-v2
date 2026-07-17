from argparse import Namespace
import hashlib

import pytest

from scripts.ops.hde_epic038_mapped_cache_smoke import (
    PACKET_NAMES,
    SINGLE_REQUEST_RETRY,
    _preflight,
    _success_files,
    _write_packet,
    main,
)


def args():
    return Namespace(
        synthetic_user_id="00000000-0000-4000-8000-000000000039",
        synthetic_person_uid="fixture-person",
        birthdate="fixture-date",
        birthtime="fixture-time",
        location="fixture-location",
        evidence_dir=None,
        retention_decision=None,
    )


def configure(monkeypatch, base_url):
    for key, value in {
        "SAFE_MODE":"0", "ALLOW_NETWORK":"1", "APP_ENV":"test",
        "HD_API_BASE_URL":base_url, "HD_API_KEY":"set", "GEO_API_KEY":"set", "DATABASE_URL":"set",
    }.items():
        monkeypatch.setenv(key, value)


def test_preflight_accepts_only_configured_v2_chart_base(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    _preflight(args())


@pytest.mark.parametrize("base_url", ["https://fixture.invalid/v1", "https://fixture.invalid", "https://fixture.invalid/v3"])
def test_preflight_refuses_non_v2_base_before_io(monkeypatch, base_url):
    configure(monkeypatch, base_url)
    with pytest.raises(SystemExit, match="configured-v2 charts route"):
        _preflight(args())


@pytest.mark.parametrize("user_id", ["00000000000040008000000000000039", "{00000000-0000-4000-8000-000000000039}", "AAAAAAAA-AAAA-4AAA-8AAA-AAAAAAAAAAAA"])
def test_preflight_refuses_noncanonical_uuid_before_io(monkeypatch, user_id):
    configure(monkeypatch, "https://fixture.invalid/v2")
    value = args()
    value.synthetic_user_id = user_id
    with pytest.raises(SystemExit, match="canonical UUID form"):
        _preflight(value)


def test_database_is_health_checked_before_vendor_fetch(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    calls = []
    class DB:
        def health(self):
            calls.append("db_health")
            raise RuntimeError("unavailable")
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.DBAccess.for_current_env", lambda **kwargs: DB())
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.HdApiClient.from_env", lambda **kwargs: calls.append("vendor") or None)
    with pytest.raises(RuntimeError, match="unavailable"):
        main(["--synthetic-user-id", args().synthetic_user_id, "--synthetic-person-uid", "fixture", "--birthdate", "fixture", "--birthtime", "fixture", "--location", "fixture"])
    assert calls == ["db_health"]


def test_vendor_client_is_pinned_to_one_attempt_and_result_is_verified(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    captured = {}

    class DB:
        def health(self):
            return None

    class Client:
        def build_contract_route_request(self, **kwargs):
            return object()

        def fetch(self, request):
            return type("VendorResult", (), {"attempts": 2, "payload": {}})()

    def client_from_env(**kwargs):
        captured.update(kwargs)
        return Client()

    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.DBAccess.for_current_env", lambda **kwargs: DB())
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.HdApiClient.from_env", client_from_env)

    with pytest.raises(SystemExit, match="attempt count must equal one"):
        main(["--synthetic-user-id", args().synthetic_user_id, "--synthetic-person-uid", "fixture", "--birthdate", "fixture", "--birthtime", "fixture", "--location", "fixture"])

    assert captured["retry"] == SINGLE_REQUEST_RETRY


def test_packet_arguments_must_be_supplied_together(monkeypatch, tmp_path):
    configure(monkeypatch, "https://fixture.invalid/v2")
    value = args()
    value.evidence_dir = tmp_path / "ops-02"
    with pytest.raises(SystemExit, match="evidence directory and retention decision"):
        _preflight(value)


def test_secret_safe_packet_has_exact_file_set_and_valid_checksums(monkeypatch, tmp_path):
    configure(monkeypatch, "https://fixture.invalid/v2")
    value = args()
    value.retention_decision = "retain"
    observation = {
        "adapter_code": "ADAPTER_MAPPED",
        "adapter_status": "mapped",
        "canonical_sha256": "a" * 64,
        "first": {
            "provider": "postgres",
            "canonical_sha256": "a" * 64,
            "rows_before": 0,
            "rows_after": 1,
            "rows_written": 1,
            "read_back_match": True,
            "idempotent": False,
        },
        "input_fingerprint": "b" * 64,
        "payload_family": "ChartResult",
        "payload_posture": "adapter_mapped_no_raw_vendor_payload",
        "projected_keys": ["bodygraph", "person", "person_uid"],
        "provider": "postgres",
        "request_route": "vendor.hdapi.post:/charts",
        "second": {
            "provider": "postgres",
            "canonical_sha256": "a" * 64,
            "rows_before": 1,
            "rows_after": 1,
            "rows_written": 0,
            "read_back_match": True,
            "idempotent": True,
        },
        "vendor_requests": 1,
    }
    repository = {
        "branch": "main",
        "head": "c" * 40,
        "pre_execution_worktree": "clean",
        "root": "/workspace/repo",
    }
    legacy = {
        "classification": "explicit_legacy_fallback",
        "resource_path": "bodygraphs",
        "route_family": "legacy_bodygraph",
    }
    files = _success_files(
        value,
        observation,
        repository,
        captured_at="2026-07-17T00:00:00Z",
        production_refused=True,
        legacy=legacy,
    )
    output = tmp_path / "packet"
    _write_packet(output, files, value)

    assert tuple(sorted(path.name for path in output.iterdir())) == tuple(sorted(PACKET_NAMES))
    assert (output / "stderr.log").read_text() == "OPS_STDERR_EMPTY\n"
    combined = b"".join(path.read_bytes() for path in output.iterdir())
    for forbidden in ("fixture-date", "fixture-time", "fixture-location", "fixture-person", "set"):
        assert forbidden.encode() not in combined

    ledger = (output / "checksums.sha256").read_text().splitlines()
    assert len(ledger) == len(PACKET_NAMES) - 1
    for row in ledger:
        digest, name = row.split("  ", 1)
        assert hashlib.sha256((output / name).read_bytes()).hexdigest() == digest
