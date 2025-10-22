from __future__ import annotations
from typing import Tuple, Dict, Any
from pathlib import Path
import os, json, copy, hashlib

from core.stable.sercanon import stable_dumps

class OverridesNotAllowedInProd(Exception): ...
class UnknownOverrideKey(Exception): ...

_FROZEN = Path("config/toggles_v1.json")
_OVR = Path("config/runtime_overrides.json")

def _load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))

def _dot_set(d: Dict[str, Any], dotted: str, val: Any) -> None:
    cur = d
    parts = dotted.split(".")
    for i, k in enumerate(parts):
        last = (i == len(parts) - 1)
        if k not in cur or (not isinstance(cur[k], dict) and not last):
            raise UnknownOverrideKey(dotted)
        if last:
            if k not in cur:
                raise UnknownOverrideKey(dotted)
            cur[k] = val
        else:
            cur = cur[k]  # descend

def resolve_toggles() -> Tuple[Dict[str, Any], str, bool]:
    """Return (resolved, frozen_sha, override_applied). No I/O at import."""
    frozen = _load_json(_FROZEN)
    frozen_sha = hashlib.sha256(stable_dumps(frozen)).hexdigest()
    resolved = copy.deepcopy(frozen)
    applied = False

    env = os.environ.get("ENGINE_ENV", "dev")
    if env == "prod":
        if _OVR.exists():
            raise OverridesNotAllowedInProd("override file present in prod")
        return (resolved, frozen_sha, False)

    if not frozen.get("experiment", {}).get("allow_runtime_overrides", False):
        return (resolved, frozen_sha, False)

    if _OVR.exists():
        ov = _load_json(_OVR)
        patch = ov.get("experiment", {}).get("patch", {})
        for key in sorted(patch.keys()):
            _dot_set(resolved, key, patch[key])
        applied = True

    return (resolved, frozen_sha, applied)
