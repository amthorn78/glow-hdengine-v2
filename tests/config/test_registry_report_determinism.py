import hashlib
import json
from dataclasses import replace

from engine.config.registry_loader import load_registry_config
from engine.serializer.canon import sercanon
from tools.generate_registry_report import _build_registry_inputs, build_registry_report


def _render_current_report() -> bytes:
    return sercanon(build_registry_report(), sort_keys=True)


def test_registry_report_two_run_identity() -> None:
    first = _render_current_report()
    second = _render_current_report()
    assert first == second
    data = json.loads(first.decode("utf-8"))
    assert data["schema"] == "registry_report.v1"
    assert first.endswith(b"\n")
    assert hashlib.sha256(first).hexdigest() == hashlib.sha256(second).hexdigest()


def test_registry_report_is_independent_of_release_manifest_identity() -> None:
    config = load_registry_config()
    changed_manifest = replace(
        config.manifest,
        version="999.0.0",
        built_at_utc="2099-01-01T00:00:00Z",
    )
    changed = replace(config, manifest=changed_manifest)

    expected = _build_registry_inputs(config)
    assert _build_registry_inputs(changed) == expected
    assert set(expected) == {"catalogs"}
