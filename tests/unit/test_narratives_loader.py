import hashlib
import json
from pathlib import Path

from engine.narratives import get_pack


def _canonical_sha(path: Path) -> str:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        canonical = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_pack_loads_and_mounts():
    pack = get_pack()
    manifest_path = Path("catalog/narratives/manifest.json")
    assert pack.pack_sha == _canonical_sha(manifest_path)
    assert pack.mount_path.exists()
    # Ensure mount contains the sealed files
    for name in [
        "keys.json",
        "templates.json",
        "palettes.json",
        "suppression_map.json",
        "manifest.json",
    ]:
        assert (pack.mount_path / name).exists()
        assert (pack.mount_path / f"{name}.sha256").exists()
