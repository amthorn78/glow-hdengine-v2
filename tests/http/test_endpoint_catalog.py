import json
from pathlib import Path


def _catalog_entries():
    catalog = json.loads(Path("docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))
    return catalog.get("endpoints", [])


def test_compat_endpoint_catalog_entry_is_internal_post_only():
    entry = next(
        (item for item in _catalog_entries() if item.get("path") == "/api/compat/v1"),
        None,
    )
    assert entry is not None
    method = entry.get("method")
    if isinstance(method, list):
        assert "POST" in method
        assert "GET" not in method
    else:
        assert method == "POST"
    assert entry.get("classification") == "internal_admin"
    assert entry.get("a7_eligible") is False
    assert isinstance(entry.get("env_gate"), str)
    assert entry.get("env_gate")


def test_dev_conjunction_endpoints_catalog_entries_are_dev_only():
    entries = _catalog_entries()
    for endpoint in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        entry = next((item for item in entries if item.get("path") == endpoint), None)
        assert entry is not None
        method = entry.get("method")
        if isinstance(method, list):
            assert method == ["GET"]
        else:
            assert method == "GET"
        assert entry.get("classification") == "dev_harness"
        assert entry.get("a7_eligible") is False
        assert isinstance(entry.get("env_gate"), str)
        assert entry.get("env_gate")
