import hashlib, json, pathlib

import pytest

pytestmark = pytest.mark.epic006


def test_service_identity_is_canonical():
    p = pathlib.Path("artifacts/identity/service_identity.json")
    raw = p.read_text(encoding="utf-8")
    assert raw.endswith("\n") and "\n\n" not in raw
    # Re-canonicalize and compare hash (sorted keys, compact)
    obj = json.loads(raw)
    recanon = json.dumps(obj, separators=(",", ":"), ensure_ascii=False) + "\n"
    assert hashlib.sha256(raw.encode("utf-8")).hexdigest() == hashlib.sha256(recanon.encode("utf-8")).hexdigest()
