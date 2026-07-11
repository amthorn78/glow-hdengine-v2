import ast
import json
from pathlib import Path

import pytest

from engine.runtime.identity import _initialize_identity_for_tests, identity_admin, identity_meta
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
