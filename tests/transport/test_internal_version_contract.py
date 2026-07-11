import hashlib
import json
import os
from pathlib import Path

import pytest

from engine.serializer import canon
from tools.evidence import update_evidence_index
from tools.ops.internal_version_artifacts import MANIFEST_NAME, ensure_request_chain_manifest

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


def _write_two_run_log(
    path: Path,
    *,
    digest: str,
    digest_run2: str,
    stored_digest: str,
    payload: dict[str, str],
    coupling_sources: dict[str, tuple[str, str]],
    release_id_manifest: tuple[str, str],
) -> None:
    lines = [
        "TWO_RUN_IDENTITY",
        f"run1_sha256={digest}",
        f"run2_sha256={digest_run2}",
        f"artifact_sha256={stored_digest}",
        f"identical={str(digest == digest_run2 == stored_digest).lower()}",
        "",
        "COUPLING_CHECKS",
    ]

    for key in _REQUIRED_KEYS:
        source_path, expected = coupling_sources[key]
        observed = payload.get(key, "")
        status = "PASS" if observed == expected else "FAIL"
        lines.append(f"{key}.source={source_path}")
        lines.append(f"{key}.expected={expected}")
        lines.append(f"{key}.observed={observed}")
        lines.append(f"{key}.status={status}")

    manifest_path, manifest_release_id = release_id_manifest
    manifest_status = "PASS" if manifest_release_id == payload.get("release_id", "") else "FAIL"
    lines.extend(
        [
            f"release_id_manifest.source={manifest_path}",
            f"release_id_manifest.expected={manifest_release_id}",
            f"release_id_manifest.observed={payload.get('release_id', '')}",
            f"release_id_manifest.status={manifest_status}",
        ]
    )

    lines.extend(
        [
            "",
            "RAILS_PINS",
            "audit/gates/determinism/env_pins.log (names-only reference)",
        ]
    )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_internal_version_invariants_and_artifacts(monkeypatch):
    monkeypatch.setenv("APP_ENV", "prod")
    monkeypatch.setenv("ENGINE_SERVICE_TOKEN", "must-not-be-required")
    client = app.test_client()
    get_resp1 = client.get("/internal/version")
    head_resp = client.head("/internal/version")
    get_resp2 = client.get("/internal/version")
    cond_resp_inm = client.get("/internal/version", headers={"If-None-Match": "xyz"})
    cond_resp_ims = client.get(
        "/internal/version", headers={"If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT"}
    )

    assert (
        get_resp1.status_code
        == head_resp.status_code
        == get_resp2.status_code
        == cond_resp_inm.status_code
        == cond_resp_ims.status_code
        == 200
    )
    assert "no-store" in get_resp1.headers.get("Cache-Control", "")
    assert "ETag" not in get_resp1.headers
    assert "ETag" not in head_resp.headers
    assert "ETag" not in cond_resp_inm.headers
    assert "ETag" not in cond_resp_ims.headers
    assert head_resp.headers.get("Content-Type") == get_resp1.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert head_resp.headers.get("Content-Length") == str(len(get_resp1.data))
    assert get_resp1.headers.get("Cache-Control") == head_resp.headers.get("Cache-Control")
    assert cond_resp_inm.headers.get("Content-Length") == str(len(get_resp1.data))
    assert cond_resp_ims.headers.get("Content-Length") == str(len(get_resp1.data))
    assert cond_resp_inm.headers.get("Content-Type") == cond_resp_ims.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert cond_resp_inm.headers.get("Cache-Control") == cond_resp_ims.headers.get("Cache-Control") == get_resp1.headers.get("Cache-Control")

    payload1 = json.loads(get_resp1.data.decode("utf-8"))
    payload2 = json.loads(get_resp2.data.decode("utf-8"))
    payload_cond_inm = json.loads(cond_resp_inm.data.decode("utf-8"))
    payload_cond_ims = json.loads(cond_resp_ims.data.decode("utf-8"))
    assert list(payload1.keys()) == _REQUIRED_KEYS
    assert payload1 == payload2 == payload_cond_inm == payload_cond_ims

    service_identity = json.loads(Path("artifacts/identity/service_identity.json").read_text(encoding="utf-8"))
    invocation = json.loads(Path("artifacts/invocation.json").read_text(encoding="utf-8")).get("invocation", {})
    release_id_file = Path("artifacts/math/release_id.txt").read_text(encoding="utf-8").strip()
    manifest_bytes = Path("catalog/manifest.json").read_bytes()
    manifest_obj = json.loads(manifest_bytes.decode("utf-8"))
    canonical_manifest_bytes = canon.sercanon(manifest_obj, sort_keys=True)
    expected_release_id = hashlib.sha256(canonical_manifest_bytes).hexdigest()
    freeze_manifest_path = Path("artifacts/math/freeze_pack_manifest.json")
    freeze_manifest = json.loads(freeze_manifest_path.read_text(encoding="utf-8"))
    assert freeze_manifest_path.read_bytes() == canonical_manifest_bytes
    emitter_sha256 = Path("artifacts/identity/emitter_sha256.txt").read_text(encoding="utf-8").strip()

    assert payload1["engine_tag"] == service_identity.get("engine_tag")
    assert payload1["build_commit"] == service_identity.get("build_commit")
    assert payload1["invocation_tag"] == invocation.get("tag")
    assert payload1["invocation_sha256"] == invocation.get("sha256")
    assert payload1["emitter_sha256"] == emitter_sha256
    assert payload1["release_id"] == release_id_file == service_identity.get("release_id") == expected_release_id

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
    _write_headers_artifact(
        _ARTIFACT_DIR / "headers_cond_if_none_match.txt",
        cond_resp_inm,
        body_len=len(cond_resp_inm.data),
    )
    _write_headers_artifact(
        _ARTIFACT_DIR / "headers_cond_if_modified_since.txt",
        cond_resp_ims,
        body_len=len(cond_resp_ims.data),
    )
    _write_two_run_log(
        _ARTIFACT_DIR / "two_run_identity.log",
        digest=digest1,
        digest_run2=digest2,
        stored_digest=stored_digest,
        payload=payload1,
        coupling_sources={
            "engine_tag": ("artifacts/identity/service_identity.json", service_identity.get("engine_tag", "")),
            "build_commit": ("artifacts/identity/service_identity.json", service_identity.get("build_commit", "")),
            "invocation_tag": ("artifacts/invocation.json", invocation.get("tag", "")),
            "invocation_sha256": ("artifacts/invocation.json", invocation.get("sha256", "")),
            "emitter_sha256": ("artifacts/identity/emitter_sha256.txt", emitter_sha256),
            "release_id": ("artifacts/math/release_id.txt", release_id_file),
        },
        release_id_manifest=("catalog/manifest.json", expected_release_id),
    )

    manifest_path, proof_path, manifest_sha = ensure_request_chain_manifest(_ARTIFACT_DIR, allow_create=True)
    manifest_rel = manifest_path.relative_to(Path(".").resolve()).as_posix()
    manifest_obj = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest_obj.get("artifact_root") == _ARTIFACT_DIR.as_posix()
    assert manifest_obj.get("manifest_version") == 1
    expected_steps = ["get", "head", "conditional_if_none_match", "conditional_if_modified_since"]
    steps = manifest_obj.get("steps", [])
    assert [step.get("name") for step in steps] == expected_steps
    for step in steps:
        artifacts = step.get("artifacts", {})
        for filename in artifacts.values():
            path = _ARTIFACT_DIR / filename
            assert path.is_file(), f"Manifest references missing artifact: {path}"
    two_run_entry = manifest_obj.get("two_run_identity", {})
    assert two_run_entry == {"log": "two_run_identity.log"}

    manifest_bytes = canon.sercanon(manifest_obj, sort_keys=True)
    assert manifest_path.read_bytes() == manifest_bytes
    assert hashlib.sha256(manifest_bytes).hexdigest() == manifest_sha

    proof_data = update_evidence_index._load_existing_proof(proof_path)
    assert proof_data.get("path") == manifest_rel
    assert proof_data.get("sha256") == manifest_sha
    assert int(proof_data.get("size_bytes", "-1")) == manifest_path.stat().st_size
