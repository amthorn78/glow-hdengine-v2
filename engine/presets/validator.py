from __future__ import annotations
import os, json, pathlib
from typing import Dict, Any, Iterable

# Tests expect this class to exist in engine.errors
try:
    from engine.errors import PresetSchemaError  # type: ignore
except Exception:  # fallback, just in case
    class PresetSchemaError(Exception):  # type: ignore
        pass

_REQUIRED = ("electromagnetic_scoring_enabled", "emotional_scoring_enabled")
_LEGACY   = "em_scoring_enabled"

def _raise(code: str, message: str, source: str, missing: Iterable[str] | None = None):
    # Make the exception "typed" without assuming constructor signature
    e = PresetSchemaError(message)
    try:
        setattr(e, "code", code)
        details: Dict[str, Any] = {"source": source}
        if missing:
            details["missing"] = list(missing)
        setattr(e, "details", details)
    except Exception:
        pass
    raise e

def _iter_search_dirs() -> list[pathlib.Path]:
    dirs: list[pathlib.Path] = []
    env = os.getenv("ENGINE_PRESETS_DIRS", "")
    if env:
        for part in env.split(os.pathsep):
            part = part.strip()
            if part:
                dirs.append(pathlib.Path(part))
    # Default repo/runtime locations (these come after explicit ENV so ENV wins)
    dirs += [pathlib.Path("presets"), pathlib.Path("config/presets")]
    # De-dup while preserving order
    out: list[pathlib.Path] = []
    seen: set[str] = set()
    for d in dirs:
        try:
            r = str(d.resolve())
        except Exception:
            r = str(d)
        if r not in seen:
            out.append(d)
            seen.add(r)
    return out

def _iter_json_files(base: pathlib.Path) -> Iterable[pathlib.Path]:
    if not base.exists():
        return []
    return sorted(base.glob("*.json"))

def _load_json(p: pathlib.Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def _validate_constraints(obj: Dict[str, Any], source: str) -> None:
    constraints = obj.get("constraints", {})
    if isinstance(constraints, dict):
        # Legacy key is forbidden regardless of presence of new keys
        if _LEGACY in constraints:
            _raise(
                "PRESET_SCHEMA_LEGACY_FIELD",
                "legacy key 'constraints.em_scoring_enabled' is forbidden; "
                "use 'constraints.electromagnetic_scoring_enabled' and "
                "'constraints.emotional_scoring_enabled'",
                source,
            )
        # Require both new booleans to be present (values can be True/False)
        missing = [f"constraints.{k}" for k in _REQUIRED if k not in constraints]
        if missing:
            _raise(
                "PRESET_SCHEMA_MISSING_FIELD",
                "missing required key(s): " + ", ".join(missing),
                source,
                missing=missing,
            )
    else:
        _raise(
            "PRESET_SCHEMA_MISSING_FIELD",
            "missing required key(s): constraints.electromagnetic_scoring_enabled, constraints.emotional_scoring_enabled",
            source,
            missing=[f"constraints.{k}" for k in _REQUIRED],
        )

def validate_all_presets() -> None:
    """
    Load every active preset we might run with and validate constraints.
    Called from app factory (pre-serve). Raises PresetSchemaError on first failure.
    """
    for d in _iter_search_dirs():
        for p in _iter_json_files(d):
            obj = _load_json(p)
            _validate_constraints(obj, str(p))

# ---- FIX: typed raise helper (constructor: (code, message, details)) ----
from engine.errors import PresetSchemaError  # type: ignore

def _raise(code: str, message: str, source: str, missing: list[str] | None = None):
    """Raise typed preset schema error with deterministic details payload."""
    details = {"source": source}
    if missing:
        details["missing"] = list(missing)
    # Correct constructor usage:
    raise PresetSchemaError(code, message, details)
