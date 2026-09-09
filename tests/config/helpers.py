import os


_CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def closed_rails_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(_CLOSED_RAILS)
    return env


from pathlib import Path
import shutil
from engine.serializer import canon


def write_canonical(path: Path, payload: object) -> None:
    """Write one owning test input; malformed-byte tests write bytes explicitly."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canon.sercanon(payload, sort_keys=True))


def catalog_root(tmp_path: Path, *, source_root: Path | None = None) -> Path:
    """Copy complete selected local inputs; generated primaries need their owners."""
    source = source_root or Path(__file__).resolve().parents[2]
    paths = (
        "catalog/channels_v1.json", "catalog/gates_v1.json", "catalog/magic10.json",
        "catalog/magic10_caps.json", "catalog/magic10_seeds.json", "catalog/manifest.json",
        "catalog/magic10_mechanics_v1.json", "math/thresholds.json",
        "schemas/channels_v1.schema.json", "schemas/gates_v1.schema.json",
        "schemas/magic10_mechanics_v1.schema.json", "schemas/magic10_result_v1.schema.json",
        "schemas/magic10_compat_result_v1.schema.json",
        "docs/schemas/config_bundle_be.json", "docs/schemas/config_bundle_fe.json",
    )
    for name in paths:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / name, target)
    return tmp_path
