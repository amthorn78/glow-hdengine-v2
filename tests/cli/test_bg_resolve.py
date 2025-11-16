from __future__ import annotations

import json

import pytest

from engine.bodygraph.ingest import IngestOutcome, resolve_db_user_id
from engine.cli.main import cli


pytestmark = pytest.mark.epic011


def _set_safe_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")


def _set_open_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")


def test_bg_resolve_db_under_safe_rails(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_safe_rails(monkeypatch)
    monkeypatch.delenv("APP_ENV", raising=False)

    exit_code = cli(["bg:resolve", "--user", "user-123", "--source", "db"])
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = json.loads(captured.out)
    assert payload["status"] == "ok"
    assert payload["resolver"]["resolved_source"] == "db"
    assert payload["resolver"]["requested_source"] == "db"
    assert payload["resolver"]["safe_mode"] is True


def test_bg_resolve_vendor_refused_under_safe_rails(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _set_safe_rails(monkeypatch)

    exit_code = cli(["bg:resolve", "--user", "user-123", "--source", "vendor"])
    captured = capsys.readouterr()

    assert exit_code != 0
    payload = json.loads(captured.out)
    assert payload["status"] == "error"
    assert payload["error"]["code"] == "PROVIDER_REFUSED"
    assert payload["resolver"]["resolved_source"] == "vendor"
    assert payload["resolver"]["safe_mode"] is True


def test_bg_resolve_defaults_to_auto(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_safe_rails(monkeypatch)

    exit_code = cli(["bg:resolve", "--user", "example"])
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = json.loads(captured.out)
    assert payload["resolver"]["requested_source"] == "auto"
    assert payload["resolver"]["resolved_source"] == "db"


def test_bg_resolve_vendor_open_rails_success(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_open_rails(monkeypatch)
    monkeypatch.setenv("APP_ENV", "dev")

    normalized_user_id = resolve_db_user_id("open-rails")

    fake_outcome = IngestOutcome(
        vendor="hdapi",
        vendor_version=1,
        input_fingerprint="abc123",
        idempotency_key=f"{normalized_user_id}:hdapi:1:abc123",
        rows_written=1,
        duration_ms=25.0,
        payload_sha256="p",
        db_emitted_sha256="p",
        parity_match=True,
        db_rows_after=1,
    )

    def _fake_ingest(inputs, **kwargs):
        assert inputs.user_id == normalized_user_id
        return fake_outcome

    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", _fake_ingest)

    exit_code = cli(
        [
            "bg:resolve",
            "--user",
            "open-rails",
            "--source",
            "vendor",
            "--birthdate",
            "1990-01-01",
            "--birthtime",
            "12:34",
            "--location",
            "Amsterdam, NL",
        ]
    )
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = json.loads(captured.out)
    assert payload["status"] == "ok"
    ingest = payload["ingest"]
    assert ingest["provider"] == fake_outcome.vendor
    assert ingest["vendor_version"] == fake_outcome.vendor_version
    assert ingest["input_fingerprint"] == fake_outcome.input_fingerprint
    assert ingest["idempotency_key"] == fake_outcome.idempotency_key
    assert ingest["rows_written"] == fake_outcome.rows_written
    assert ingest["db_rows_after"] == fake_outcome.db_rows_after
    assert ingest["duration_ms"] == round(fake_outcome.duration_ms, 3)
    assert ingest["payload_sha256"] == fake_outcome.payload_sha256
    assert ingest["db_emitted_sha256"] == fake_outcome.db_emitted_sha256
    assert ingest["parity_match"] == fake_outcome.parity_match
