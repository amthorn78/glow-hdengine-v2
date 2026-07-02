from __future__ import annotations

import json

import pytest

from engine.bodygraph.resolver import IngestOutcome, resolve_db_user_id
from engine.cli.main import cli
from engine.presenter import emitter
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon


pytestmark = pytest.mark.epic011


DETERMINISM_PINS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


@pytest.fixture(autouse=True)
def _rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_PINS.items():
        monkeypatch.setenv(key, value)


def _set_safe_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")


def _set_open_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")


def _assert_canonical_output(text: str) -> dict[str, object]:
    assert text.endswith("\n")
    payload = json.loads(text)
    emitted = emitter.emit_public(payload)
    assert emitted.decode("utf-8") == text
    assert sercanon(payload) == emitted
    return payload


def test_bg_resolve_db_under_safe_rails(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_safe_rails(monkeypatch)
    monkeypatch.delenv("APP_ENV", raising=False)
    ensure_determinism_env()

    exit_code = cli(["bg:resolve", "--user", "user-123", "--source", "db"])
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = _assert_canonical_output(captured.out)
    assert payload["status"] == "ok"
    assert payload["resolver"]["resolved_source"] == "db"
    assert payload["resolver"]["requested_source"] == "db"
    assert payload["resolver"]["safe_mode"] is True


def test_bg_resolve_two_run_identity(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_safe_rails(monkeypatch)
    first_code = cli(["bg:resolve", "--user", "user-123", "--source", "db"])
    first = capsys.readouterr()

    second_code = cli(["bg:resolve", "--user", "user-123", "--source", "db"])
    second = capsys.readouterr()

    assert first_code == second_code == 0
    assert first.out == second.out
    _assert_canonical_output(first.out)


def test_bg_resolve_vendor_refused_under_safe_rails(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _set_safe_rails(monkeypatch)

    exit_code = cli(
        [
            "bg:resolve",
            "--user",
            "user-123",
            "--source",
            "vendor",
            "--birthdate",
            "1990-01-01",
            "--birthtime",
            "12:00",
            "--location",
            "Amsterdam, Netherlands",
        ]
    )
    captured = capsys.readouterr()

    assert exit_code != 0
    payload = _assert_canonical_output(captured.out)
    assert payload["status"] == "error"
    assert payload["error"]["code"] == "PROVIDER_REFUSED"
    assert payload["resolver"]["resolved_source"] == "vendor"
    assert payload["resolver"]["safe_mode"] is True


def test_bg_resolve_defaults_to_auto(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_safe_rails(monkeypatch)

    exit_code = cli(["bg:resolve", "--user", "example"])
    captured = capsys.readouterr()

    assert exit_code == 0
    payload = _assert_canonical_output(captured.out)
    assert payload["resolver"]["requested_source"] == "auto"
    assert payload["resolver"]["resolved_source"] == "db"


def test_bg_resolve_vendor_open_rails_success(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_open_rails(monkeypatch)
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v1")
    monkeypatch.delenv("HDAPI_BASE_URL", raising=False)

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
        payload={"ok": True},
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
    payload = _assert_canonical_output(captured.out)
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


def test_bg_resolve_vendor_missing_inputs(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _set_open_rails(monkeypatch)

    exit_code = cli(["bg:resolve", "--user", "open-rails", "--source", "vendor"])
    captured = capsys.readouterr()

    assert exit_code == 64
    if captured.out:
        payload = _assert_canonical_output(captured.out)
        assert payload["status"] == "error"
    else:
        assert captured.err
