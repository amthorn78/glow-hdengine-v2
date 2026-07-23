import hashlib
import json
from pathlib import Path

import pytest

from tools.config.generate_bundles import expected_bundles


jsonschema = pytest.importorskip(
    "jsonschema",
    reason="jsonschema is required for config bundle schema validation; install from requirements-dev.txt",
)


ROOT = Path(__file__).resolve().parents[1].parent
FE_BUNDLE_PATH = ROOT / "artifacts" / "config_bundles" / "fe_bundle.json"
BE_BUNDLE_PATH = ROOT / "artifacts" / "config_bundles" / "be_bundle.json"


def _read_canonical(path: Path) -> dict:
    payload = path.read_text(encoding="utf-8")
    obj = json.loads(payload)
    expected = json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    assert payload == expected
    return obj


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _expected_bundle_bytes() -> tuple[bytes, bytes]:
    expected = expected_bundles()
    return expected[FE_BUNDLE_PATH], expected[BE_BUNDLE_PATH]


def test_two_run_identity() -> None:
    fe_first, be_first = _expected_bundle_bytes()
    fe_second, be_second = _expected_bundle_bytes()
    assert fe_first == fe_second
    assert be_first == be_second


def test_bundle_check_mode_is_read_only() -> None:
    fe_before = FE_BUNDLE_PATH.read_bytes()
    be_before = BE_BUNDLE_PATH.read_bytes()
    fe_expected, be_expected = _expected_bundle_bytes()
    assert (fe_expected, be_expected) == (fe_before, be_before)
    assert FE_BUNDLE_PATH.read_bytes() == fe_before
    assert BE_BUNDLE_PATH.read_bytes() == be_before


def test_frontend_bundle_schema_and_sources() -> None:
    fe_bundle = _read_canonical(FE_BUNDLE_PATH)
    fe_schema = json.loads((ROOT / "docs" / "schemas" / "config_bundle_fe.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=fe_bundle, schema=fe_schema)

    magic10_config = _read_canonical(ROOT / "artifacts" / "thresholds" / "magic10_config.json")
    band_edges = _read_canonical(ROOT / "artifacts" / "thresholds" / "band_edges.json")
    registry_report = _read_canonical(ROOT / "artifacts" / "registry" / "registry_report.json")

    assert fe_bundle["magic10"]["order"] == magic10_config["order"]
    assert fe_bundle["magic10"]["caps"] == magic10_config["caps"]
    assert fe_bundle["bands"]["edges"] == band_edges["edges"]
    assert fe_bundle["bands"]["bands"] == band_edges["bands"]
    assert fe_bundle["channels"]["ids"] == registry_report["artifacts"]["registry"]["channel_ids"]

    for key, src in fe_bundle["sources"].items():
        artifact_path = ROOT / src["path"]
        assert artifact_path.exists()
        assert src["sha256"] == _sha256(artifact_path)
        assert src["size_bytes"] == artifact_path.stat().st_size


def test_backend_bundle_schema_and_sources() -> None:
    be_bundle = _read_canonical(BE_BUNDLE_PATH)
    be_schema = json.loads((ROOT / "docs" / "schemas" / "config_bundle_be.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=be_bundle, schema=be_schema)

    magic10_config = _read_canonical(ROOT / "artifacts" / "thresholds" / "magic10_config.json")
    band_edges = _read_canonical(ROOT / "artifacts" / "thresholds" / "band_edges.json")
    registry_report = _read_canonical(ROOT / "artifacts" / "registry" / "registry_report.json")

    assert be_bundle["magic10"] == magic10_config
    assert be_bundle["bands"] == band_edges

    registry_channels = registry_report["artifacts"]["registry"]["channel_ids"]
    assert [entry["id"] for entry in be_bundle["channels"]] == registry_channels
    assert be_bundle["domains"] == registry_report["artifacts"]["registry"]["domains"]
    assert be_bundle["centers"] == registry_report["artifacts"]["registry"]["centers"]
    assert be_bundle["alias_policy"] == registry_report["artifacts"]["registry"]["alias_policy"]

    for key, src in be_bundle["sources"].items():
        artifact_path = ROOT / src["path"]
        assert artifact_path.exists()
        assert src["sha256"] == _sha256(artifact_path)
        assert src["size_bytes"] == artifact_path.stat().st_size
