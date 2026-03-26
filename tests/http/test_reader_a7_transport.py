import hashlib
import os
from pathlib import Path

import pytest

from adapter.http_reader import create_app


def _client():
    app = create_app()
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


def _format_status(resp) -> str:
    status_text = resp.status.split(" ", 1)[1] if " " in resp.status else ""
    return f"HTTP/1.0 {resp.status_code} {status_text}".rstrip()


def _write_headers_proof(path: Path, resp, header_order: list[str]) -> None:
    lines = [_format_status(resp)]
    headers = {key.lower(): value for key, value in resp.headers.items()}
    for key in header_order:
        if key in headers:
            lines.append(f"{key}: {headers[key]}")
        else:
            lines.append(f"{key}: <absent>")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_encoding_proof(path: Path, *, etag_identity: str, etag_gzip: str) -> None:
    lines = [
        "ENCODING_INVARIANCE",
        f"etag_identity={etag_identity}",
        f"etag_gzip={etag_gzip}",
        f"match={str(etag_identity == etag_gzip).lower()}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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

    write_proofs = os.environ.get("HDE_WRITE_A7_PROOFS") == "1"
    if not write_proofs:
        return

    proof_dir = Path("artifacts/proofs")
    proof_dir.mkdir(parents=True, exist_ok=True)

    with monkeypatch.context() as gate_ctx:
        gate_ctx.setenv("APP_ENV", "prod")
        blocked_resp = client.get("/reader", query_string=params)

    _write_headers_proof(
        proof_dir / "endpoints_env_gate_proof.log",
        blocked_resp,
        ["cache-control", "content-type", "etag"],
    )

    _write_headers_proof(
        proof_dir / "success_get.txt",
        get_resp_identity,
        ["etag", "content-type", "cache-control", "vary", "content-length"],
    )
    _write_headers_proof(
        proof_dir / "success_head.txt",
        head_resp,
        ["etag", "content-type", "cache-control", "vary", "content-length"],
    )
    _write_headers_proof(
        proof_dir / "success_304.txt",
        cond_resp,
        ["etag", "cache-control", "vary", "content-type", "content-length"],
    )
    _write_headers_proof(
        proof_dir / "success_writers_errors.txt",
        post_resp,
        ["cache-control", "etag"],
    )
    etag_gzip = get_resp_gzip.headers.get("ETag", "")
    _write_encoding_proof(
        proof_dir / "encoding_invariance.txt",
        etag_identity=etag,
        etag_gzip=etag_gzip,
    )
    _write_encoding_proof(
        proof_dir / "success_encoding_invariance.txt",
        etag_identity=etag,
        etag_gzip=etag_gzip,
    )
