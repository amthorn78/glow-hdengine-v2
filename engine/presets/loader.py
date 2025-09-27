from __future__ import annotations
import os, json
from pathlib import Path
from typing import Iterator, Tuple, Dict, Any

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

from engine.presets.validator import validate_preset
try:
    from engine.errors import PresetSchemaError
except Exception:
    class PresetSchemaError(Exception):
        pass

def _dirs() -> Iterator[Path]:
    # Highest precedence: ENGINE_PRESETS_DIRS (os.pathsep-delimited)
    env = os.getenv("ENGINE_PRESETS_DIRS", "")
    if env:
        for raw in env.split(os.pathsep):
            p = Path(raw.strip())
            if p.exists() and p.is_dir():
                yield p
    # Repo defaults
    for p in (Path("presets"), Path("config/presets")):
        if p.exists() and p.is_dir():
            yield p

def _iter_paths() -> Iterator[Path]:
    for d in _dirs():
        # JSON first; YAML second
        for ext in ("*.json", "*.yml", "*.yaml"):
            yield from d.glob(ext)

def _read(path: Path) -> Dict[str, Any]:
    suf = path.suffix.lower()
    if suf == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    if suf in (".yml", ".yaml"):
        if yaml is None:
            raise PresetSchemaError(f"YAML support not available to load {path}")
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raise PresetSchemaError(f"Unsupported preset file type: {path}")

def load_all_presets() -> Iterator[Tuple[Path, Dict[str, Any]]]:
    for p in _iter_paths():
        yield p, _read(p)

def ensure_presets_validated() -> None:
    """
    Load every active preset and validate schema. Raise PresetSchemaError on first failure.
    Used at app startup to fail pre-serve.
    """
    for path, data in load_all_presets():
        validate_preset(data, source=str(path))
