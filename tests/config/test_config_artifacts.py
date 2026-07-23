import json
import subprocess
import sys
from pathlib import Path

import pytest

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.magic10.thresholds import BANDS
from tests.config.helpers import closed_rails_env


@pytest.fixture(scope="module", autouse=True)
def _generate_artifacts() -> None:
    subprocess.run([sys.executable, "tools/config/generate_config_artifacts.py"], check=True, env=closed_rails_env())


def _read_canonical(path: Path) -> tuple[str, dict]:
    payload = path.read_text(encoding="utf-8")
    obj = json.loads(payload)
    expected = json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    assert payload == expected
    return payload, obj


def test_magic10_config_snapshot() -> None:
    _, obj = _read_canonical(Path("artifacts/thresholds/magic10_config.json"))
    assert obj["schema"] == "magic10_config.v1"
    assert tuple(obj["order"]) == FROZEN_MAGIC10_ORDER
    caps = obj["caps"]
    assert set(caps) == set(FROZEN_MAGIC10_ORDER)
    for key, entry in caps.items():
        assert entry["inputs"], f"missing inputs for {key}"
        bounds = entry["bounds"]
        assert isinstance(bounds["min"], int) and isinstance(bounds["max"], int)
        assert bounds["min"] <= bounds["max"]
    seeds = obj["seeds"]
    assert set(seeds).issubset(set(FROZEN_MAGIC10_ORDER))
    for seed_key, seed in seeds.items():
        assert seed["template_id"]
        assert seed["seed_version"]
        assert seed["updated_at_utc"]
        assert seed["checksum_sha256"]


def test_band_edges_config() -> None:
    _, obj = _read_canonical(Path("artifacts/thresholds/band_edges.json"))
    assert obj["schema"] == "band_edges.v1"
    assert obj["bands"] == list(BANDS)
    edges = obj["edges"]
    assert edges == sorted(edges)
    assert len(edges) == len(obj["bands"])
    clamp = obj["clamp"]
    assert len(clamp) == 2
    assert clamp[0] <= clamp[1]
    assert edges[-1] == clamp[1]
    assert obj["rounding"] == "ROUND_HALF_UP"


def test_config_artifact_check_mode_is_read_only() -> None:
    paths = (
        Path("artifacts/registry/registry_report.json"),
        Path("artifacts/thresholds/magic10_config.json"),
        Path("artifacts/thresholds/band_edges.json"),
    )
    before = {path: path.read_bytes() for path in paths}
    subprocess.run(
        [sys.executable, "tools/config/generate_config_artifacts.py", "--check"],
        check=True,
        env=closed_rails_env(),
    )
    assert {path: path.read_bytes() for path in paths} == before
