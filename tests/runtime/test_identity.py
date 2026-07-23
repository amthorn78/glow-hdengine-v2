import ast
import hashlib
import json
from pathlib import Path

import pytest

from engine.runtime.identity import (
    _initialize_identity_for_tests,
    _manifest_release_id_from_bytes,
    identity_admin,
    identity_meta,
)
from engine.serializer import canon
from engine.runtime.public import emit_reader_public_envelope
from engine.cli.main import _engine_identity

FIELDS = ["engine_tag","build_commit","invocation_tag","invocation_sha256","emitter_sha256","release_id"]

def test_identity_shapes_and_reader_cli_shared_identity():
    admin = identity_admin()
    assert list(admin) == FIELDS
    assert set(identity_meta()) == {"engine_tag","invocation_tag","release_id"}
    assert _engine_identity() == (admin["engine_tag"], admin["release_id"], admin["invocation_tag"])
    body, payload = emit_reader_public_envelope({"person_uid":"a","mechanics":{"type":"Generator"}},{"person_uid":"b","mechanics":{"type":"Projector"}})
    assert payload["meta"] == {"engine_tag": admin["engine_tag"], "invocation_tag": admin["invocation_tag"]}
    assert payload["release_id"] == admin["release_id"]
    assert body.endswith(b"\n")


def test_release_identity_is_derived_from_the_packaged_manifest():
    manifest_path = Path("catalog/manifest.json")
    raw = manifest_path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    canonical = canon.sercanon(payload, sort_keys=True)

    assert raw == canonical
    assert identity_admin()["release_id"] == hashlib.sha256(canonical).hexdigest()
    source = Path("engine/runtime/identity.py").read_text(encoding="utf-8")
    assert "_CUT_TIME_IDENTITY" not in source
    assert "artifacts/math/release_id.txt" not in source


def test_runtime_manifest_identity_rejects_canonical_contract_mutations():
    payload = json.loads(Path("catalog/manifest.json").read_bytes())
    payload["unknown"] = True
    with pytest.raises(ValueError, match="release_manifest_contract_invalid"):
        _manifest_release_id_from_bytes(canon.sercanon(payload, sort_keys=True))

    payload.pop("unknown")
    payload["files"][0]["path"] = "catalog/manifest.json"
    with pytest.raises(ValueError, match="release_manifest_contract_invalid"):
        _manifest_release_id_from_bytes(canon.sercanon(payload, sort_keys=True))

    payload = json.loads(Path("catalog/manifest.json").read_bytes())
    payload["version"] = "01.0.0"
    with pytest.raises(ValueError, match="release_manifest_contract_invalid"):
        _manifest_release_id_from_bytes(canon.sercanon(payload, sort_keys=True))

    payload["version"] = "1.0.0"
    payload["built_at_utc"] = "2026-02-30T00:00:00Z"
    with pytest.raises(ValueError, match="release_manifest_contract_invalid"):
        _manifest_release_id_from_bytes(canon.sercanon(payload, sort_keys=True))

    raw = Path("catalog/manifest.json").read_bytes().replace(b'{"built', b'{ "built', 1)
    with pytest.raises(ValueError, match="release_manifest_not_canonical"):
        _manifest_release_id_from_bytes(raw)

def test_identity_rejects_missing_extra_and_conflicting_reinit():
    admin = identity_admin()
    assert _initialize_identity_for_tests(admin) == _initialize_identity_for_tests(dict(admin))
    missing = dict(admin); missing.pop("release_id")
    with pytest.raises(ValueError): _initialize_identity_for_tests(missing)
    extra = dict(admin); extra["extra"] = "x"
    with pytest.raises(ValueError): _initialize_identity_for_tests(extra)
    changed = dict(admin); changed["release_id"] = "a"*64
    with pytest.raises(RuntimeError): _initialize_identity_for_tests(changed)

def test_runtime_identity_paths_do_not_read_artifacts_or_identity_env():
    files = [Path("adapter/http_reader.py"), Path("engine/cli/main.py"), Path("engine/http/compat_handler.py")]
    banned_paths = ["service_identity.json", "artifacts/invocation.json", "artifacts/math/release_id.txt", "emitter_sha256.txt"]
    banned_env = ["ENGINE_TAG", "BUILD_COMMIT", "PRODUCT_INVOCATION_TAG", "EMITTER_SHA256"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        for token in banned_paths:
            assert token not in text
        for token in banned_env:
            assert token not in text


def test_reader_injected_emitter_receives_identity_kwargs(tmp_path, monkeypatch):
    from flask import Flask
    import adapter.http_reader as http_reader
    from adapter.http_reader import get_reader_bp

    a_path = tmp_path / "a.json"
    b_path = tmp_path / "b.json"
    a_path.write_text('{"person_uid":"a","mechanics":{"type":"Generator"}}', encoding="utf-8")
    b_path.write_text('{"person_uid":"b","mechanics":{"type":"Projector"}}', encoding="utf-8")
    seen = {}

    def injected(a, b, *, engine_tag, invocation_tag, release_id):
        seen.update({"engine_tag": engine_tag, "invocation_tag": invocation_tag, "release_id": release_id})
        return b'{"ok":true}\n'

    monkeypatch.setattr(http_reader, "ALLOWED_ROOT", tmp_path.resolve())
    app = Flask(__name__)
    app.register_blueprint(get_reader_bp(emit_fn=injected))
    monkeypatch.setenv("APP_ENV", "dev")
    resp = app.test_client().get(f"/reader?v=1&a={a_path}&b={b_path}&a_tz=UTC&b_tz=UTC")
    assert resp.status_code == 200
    assert seen == identity_meta()
