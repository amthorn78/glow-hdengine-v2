import hashlib
import json
import os
from pathlib import Path

import pytest

os.environ.setdefault("DATABASE_URL", "postgresql://example")
os.environ.setdefault("SAFE_MODE", "1")
os.environ.setdefault("ALLOW_NETWORK", "0")
os.environ.setdefault("LC_ALL", "C")
os.environ.setdefault("LANG", "C")
os.environ.setdefault("TZ", "UTC")

from adapter.http_reader import app

pytestmark = pytest.mark.epic020


_REQUIRED_KEYS = [
    "engine_tag",
    "build_commit",
    "invocation_tag",
    "invocation_sha256",
    "emitter_sha256",
    "release_id",
]
_ARTIFACT_DIR = Path("artifacts/ops/internal_version")


def _write_headers_artifact(path: Path, resp, *, body_len: int) -> None:
    status_suffix = resp.status.split(" ", 1)[1] if " " in resp.status else ""
    lines = [f"HTTP/1.0 {resp.status_code} {status_suffix}".rstrip()]
    for key, value in sorted(resp.headers.items()):
        lines.append(f"{key}: {value}")
    if "ETag" not in resp.headers:
        lines.append("ETag: <absent>")
    lines.append(f"Body-Length: {body_len} bytes")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_two_run_log(path: Path, *, digest: str, digest_run2: str, stored_digest: str) -> None:
    lines = [
        "Two-run identity for /internal/version (closed rails)",
        f"run1.sha256={digest}",
        f"run2.sha256={digest_run2}",
        f"artifact.sha256={stored_digest}",
        f"hash_match={digest == digest_run2 == stored_digest}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_internal_version_invariants_and_artifacts():
    client = app.test_client()
    get_resp1 = client.get("/internal/version")
    head_resp = client.head("/internal/version")
    get_resp2 = client.get("/internal/version")
    cond_resp = client.get("/internal/version", headers={"If-None-Match": "xyz"})

    assert get_resp1.status_code == head_resp.status_code == get_resp2.status_code == cond_resp.status_code == 200
    assert "no-store" in get_resp1.headers.get("Cache-Control", "")
    assert "ETag" not in get_resp1.headers
    assert "ETag" not in head_resp.headers
    assert "ETag" not in cond_resp.headers
    assert head_resp.headers.get("Content-Type") == get_resp1.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert head_resp.headers.get("Content-Length") == str(len(get_resp1.data))
    assert get_resp1.headers.get("Cache-Control") == head_resp.headers.get("Cache-Control")
    assert cond_resp.headers.get("Content-Length") == str(len(get_resp1.data))

    payload1 = json.loads(get_resp1.data.decode("utf-8"))
    payload2 = json.loads(get_resp2.data.decode("utf-8"))
    assert list(payload1.keys()) == _REQUIRED_KEYS
    assert payload1 == payload2

    service_identity = json.loads(Path("artifacts/identity/service_identity.json").read_text(encoding="utf-8"))
    invocation = json.loads(Path("artifacts/invocation.json").read_text(encoding="utf-8")).get("invocation", {})
    release_id_file = Path("artifacts/math/release_id.txt").read_text(encoding="utf-8").strip()
    freeze_manifest = json.loads(Path("artifacts/math/freeze_pack_manifest.json").read_text(encoding="utf-8"))
    emitter_sha256 = Path("artifacts/identity/emitter_sha256.txt").read_text(encoding="utf-8").strip()

    assert payload1["engine_tag"] == service_identity.get("engine_tag")
    assert payload1["build_commit"] == service_identity.get("build_commit")
    assert payload1["invocation_tag"] == invocation.get("tag")
    assert payload1["invocation_sha256"] == invocation.get("sha256")
    assert payload1["emitter_sha256"] == emitter_sha256
    assert payload1["release_id"] == release_id_file == service_identity.get("release_id") == freeze_manifest.get("release_id")

    computed_invocation_hash = hashlib.sha256(invocation.get("tag", "").encode("utf-8")).hexdigest()
    assert computed_invocation_hash == payload1["invocation_sha256"]

    digest1 = hashlib.sha256(get_resp1.data).hexdigest()
    digest2 = hashlib.sha256(get_resp2.data).hexdigest()
    assert digest1 == digest2

    _ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    body_path = _ARTIFACT_DIR / "body_get.json"
    body_path.write_bytes(get_resp1.data)
    digest_path = _ARTIFACT_DIR / "body_get.sha256"
    digest_path.write_text(digest1 + "\n", encoding="utf-8")
    stored_digest = digest_path.read_text(encoding="utf-8").strip()
    assert stored_digest == digest1

    _write_headers_artifact(_ARTIFACT_DIR / "headers_get.txt", get_resp1, body_len=len(get_resp1.data))
    _write_headers_artifact(_ARTIFACT_DIR / "headers_head.txt", head_resp, body_len=0)
    _write_two_run_log(
        _ARTIFACT_DIR / "two_run_identity.log",
        digest=digest1,
        digest_run2=digest2,
        stored_digest=stored_digest,
    )
