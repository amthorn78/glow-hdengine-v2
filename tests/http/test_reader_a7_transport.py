import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

from adapter import http_reader
from engine.serializer.canon import sercanon


def _client():
    app = http_reader.create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _reader_query_params() -> dict[str, str]:
    alice = Path("fixtures/charts/alice.json").resolve()
    bob = Path("fixtures/charts/bob.json").resolve()
    return {
        "v": "1",
        "a": str(alice),
        "b": str(bob),
        "a_tz": "UTC",
        "b_tz": "UTC",
    }


def _assert_canonical_lf_bytes(raw: bytes) -> None:
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    assert b"\r" not in raw
    assert sercanon(json.loads(raw)) == raw


def test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    repo_root = Path(__file__).resolve().parents[2]
    pair_path = tmp_path / "pair.json"
    pair_path.write_text(
        json.dumps(
            {
                "left": {
                    "birthdate": "1990-01-10",
                    "birthtime": "14:05",
                    "location": "Chicago, US",
                },
                "right": {
                    "birthdate": "1992-03-04",
                    "birthtime": "08:15",
                    "location": "Berlin, DE",
                },
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    cli_reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"
    rails = {
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    for name, value in rails.items():
        monkeypatch.setenv(name, value)
    cli_env = os.environ.copy()
    cli_env.update(rails)

    result = subprocess.run(
        [
            sys.executable,
            "scripts/hdctl.py",
            "showcompat",
            "--pair-file",
            str(pair_path),
            "--dump-reader",
            str(cli_reader_path),
            "--dump-admin-dir",
            str(admin_dir),
        ],
        cwd=repo_root,
        env=cli_env,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr.decode("utf-8", errors="replace")
    assert result.stderr == b""

    cli_reader = cli_reader_path.read_bytes()
    _assert_canonical_lf_bytes(cli_reader)

    # The CLI's governed admin sidecars are its normalized chart pair. Point the
    # HTTP path guard at only that private directory, then ask /reader to emit
    # the same pair through the current HTTP adapter.
    left_chart = admin_dir / "pair.left.bodygraph.json"
    right_chart = admin_dir / "pair.right.bodygraph.json"
    assert left_chart.is_file()
    assert right_chart.is_file()
    monkeypatch.setattr(http_reader, "ALLOWED_ROOT", admin_dir.resolve())

    response = _client().get(
        "/reader",
        query_string={
            "v": "1",
            "a": str(left_chart),
            "b": str(right_chart),
            "a_tz": "UTC",
            "b_tz": "UTC",
        },
        headers={"Accept-Encoding": "identity"},
    )

    assert response.status_code == 200
    _assert_canonical_lf_bytes(response.data)
    assert response.data == cli_reader


@pytest.mark.epic025
def test_reader_a7_transport_invariants(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("ENGINE_TAG", "hdengine-a7")
    monkeypatch.setenv("PRODUCT_INVOCATION_TAG", "INV-A7")
    monkeypatch.setenv("RELEASE_ID", "a" * 64)

    client = _client()
    params = _reader_query_params()

    get_resp_identity = client.get(
        "/reader",
        query_string=params,
        headers={"Accept-Encoding": "identity"},
    )
    get_resp_gzip = client.get(
        "/reader",
        query_string=params,
        headers={"Accept-Encoding": "gzip"},
    )

    assert get_resp_identity.status_code == 200
    assert get_resp_gzip.status_code == 200
    assert get_resp_identity.data.endswith(b"\n")
    assert get_resp_identity.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert get_resp_identity.headers.get("Cache-Control") == "private, max-age=0, must-revalidate"
    assert get_resp_identity.headers.get("Vary") == "Authorization, Accept-Encoding"
    assert get_resp_identity.headers.get("Content-Length") == str(len(get_resp_identity.data))
    payload = get_resp_identity.get_json()
    assert list(payload.keys()) == ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
    etag = get_resp_identity.headers.get("ETag")
    assert isinstance(etag, str)
    assert etag.startswith('"') and etag.endswith('"')
    assert not etag.startswith("W/")
    assert get_resp_gzip.headers.get("ETag") == etag
    assert get_resp_gzip.headers.get("Content-Length") == str(len(get_resp_gzip.data))

    head_resp = client.head("/reader", query_string=params)
    assert head_resp.status_code == 200
    assert head_resp.data == b""
    assert head_resp.headers.get("Content-Type") == get_resp_identity.headers.get("Content-Type")
    assert head_resp.headers.get("Cache-Control") == get_resp_identity.headers.get("Cache-Control")
    assert head_resp.headers.get("Vary") == get_resp_identity.headers.get("Vary")
    assert head_resp.headers.get("ETag") == etag
    assert head_resp.headers.get("Content-Length") == str(len(get_resp_identity.data))

    cond_resp = client.get("/reader", query_string=params, headers={"If-None-Match": etag})
    assert cond_resp.status_code == 304
    assert cond_resp.data == b""
    assert "Content-Type" not in cond_resp.headers
    assert "Content-Length" not in cond_resp.headers
    assert cond_resp.headers.get("ETag") == etag
    assert cond_resp.headers.get("Vary") == get_resp_identity.headers.get("Vary")

    post_resp = client.post("/reader", query_string=params)
    assert post_resp.status_code == 405
    assert "ETag" not in post_resp.headers
    assert post_resp.headers.get("Cache-Control") == "no-store"
