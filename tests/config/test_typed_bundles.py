import hashlib
import json
import subprocess
import sys
from pathlib import Path

import jsonschema
import pytest

from tests.config.helpers import closed_rails_env


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


def _run_generators(env: dict[str, str]) -> tuple[bytes, bytes]:
    subprocess.run([sys.executable, "tools/config/generate_config_artifacts.py"], check=True, env=env)
    subprocess.run([sys.executable, "tools/config/generate_bundles.py"], check=True, env=env)
    return FE_BUNDLE_PATH.read_bytes(), BE_BUNDLE_PATH.read_bytes()


@pytest.fixture(scope="module")
def rails_env() -> dict[str, str]:
    return closed_rails_env()


def test_two_run_identity(rails_env: dict[str, str]) -> None:
    fe_first, be_first = _run_generators(rails_env)
    fe_second, be_second = _run_generators(rails_env)
    assert fe_first == fe_second
    assert be_first == be_second


def test_frontend_bundle_schema_and_sources(rails_env: dict[str, str]) -> None:
    _run_generators(rails_env)
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


def test_backend_bundle_schema_and_sources(rails_env: dict[str, str]) -> None:
    _run_generators(rails_env)
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
