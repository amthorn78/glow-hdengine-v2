import json

import pytest

from engine.cli.main import cli


def test_showcompat_vendor_dry_run(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    called: list[dict] = []

    def _fake_ingest(inputs, **kwargs):
        called.append({"inputs": inputs, "kwargs": kwargs})
        return type("Outcome", (), {
            "vendor": "hdapi",
            "vendor_version": 1,
            "input_fingerprint": "fingerprint",
            "idempotency_key": "idem",
            "rows_written": 0,
            "duration_ms": 1.0,
            "payload_sha256": "p",
            "db_emitted_sha256": "p",
            "parity_match": True,
            "db_rows_after": 0,
            "payload": {"type": "Projector", "birth": {"date": "1990-01-01", "time": "12:00", "location": "A"}},
        })()

    monkeypatch.setattr("engine.cli.main.ingest_vendor_bodygraph", _fake_ingest)
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")

    exit_code = cli(
        [
            "showcompat",
            "--source",
            "vendor",
            "--birthdate-a",
            "1990-01-01",
            "--birthtime-a",
            "12:00",
            "--location-a",
            "Amsterdam",
            "--birthdate-b",
            "1991-02-02",
            "--birthtime-b",
            "13:00",
            "--location-b",
            "Berlin",
        ]
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    payload = json.loads(captured.out)
    assert payload["compat"]["meta"]["engine_tag"]
    assert called and called[0]["kwargs"]["dry_run"] is True


def test_showcompat_db_source(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    class _DB:
        def query(self, sql: str, params):
            assert "body_graphs_current" in sql
            return [(json.dumps({"type": "Generator", "birth": {"date": "1990-01-01", "time": "12:00"}}),)]

    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda: _DB())
    monkeypatch.setattr("engine.cli.main.ingest_vendor_bodygraph", lambda *_, **__: (_ for _ in ()).throw(AssertionError("no vendor")))

    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])

    captured = capsys.readouterr()
    assert exit_code == 0
    payload = json.loads(captured.out)
    compat = payload["compat"]
    assert compat["categories"]
    assert compat["meta"]["release_id"]
