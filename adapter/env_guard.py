#!/usr/bin/env python3
from __future__ import annotations

from typing import Mapping, Optional, Dict, List, Any
import os

class EnvGuardError(Exception):
    def __init__(self, code: str, message: str, details: Dict[str, Any]):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details
    def __str__(self) -> str:
        return self.message

# --- Constants (no env reads at import) ---
_PROD_ALIASES = {"prod", "production", "live"}
_FORBIDDEN_IN_PROD = (
    "ENGINE_SECRETS_DIR",
    "ENGINE_PROVIDER",
    "KEEP_REAL_SECRETS",
    "FEATURE_TOGGLES",
    "PRESET_OVERRIDE",
    "COPY_OVERRIDE",
    "ALLOW_NETWORK",
    "HD_ADMIN",
)

def _norm(s: Optional[str]) -> str:
    return (s or "").strip().lower()

def _compute_env_mode(env: Mapping[str, str]) -> str:
    """
    APP_ENV precedence:
      - If APP_ENV is non-empty -> decide solely from APP_ENV.
      - Else fallback to ENGINE_ENV.
      - If neither set -> dev.
    Normalize to:
      - 'prod' if in aliases
      - otherwise the lowercased value (e.g., 'dev', 'staging', etc.)
    """
    app = env.get("APP_ENV")
    if app is not None and app.strip() != "":
        v = _norm(app)
        return "prod" if v in _PROD_ALIASES else v

    eng = env.get("ENGINE_ENV")
    if eng is not None and eng.strip() != "":
        v = _norm(eng)
        return "prod" if v in _PROD_ALIASES else v

    return "dev"

def validate_or_fail(environ: Optional[Mapping[str, str]] = None) -> None:
    """
    Pure, silent guard. Reads env ONLY when called.
    In 'prod' mode, forbids any of the known override keys when value is present after .strip().
    Returns None if allowed; raises EnvGuardError otherwise.
    """
    env = os.environ if environ is None else environ
    mode = _compute_env_mode(env)
    if mode == "prod":
        offending: List[str] = []
        for key in _FORBIDDEN_IN_PROD:
            val = env.get(key)
            # 'present' means non-empty after .strip(); '0'/'false' count as present
            if val is not None and val.strip() != "":
                offending.append(key)
        if offending:
            offending.sort()
            raise EnvGuardError(
                code="CANON_TOGGLES_OVERRIDE_IN_PROD",
                message="forbidden config present in prod; remove overrides or use non-prod",
                details={"env_mode": "prod", "forbidden_keys": offending},
            )
    return None


# --- hotfix: accept Flask app or any object; coerce to Mapping before core ---
from collections.abc import Mapping as _Mapping

def _as_mapping(obj):
    if obj is None:
        import os as _os
        return _os.environ
    if isinstance(obj, _Mapping):
        return obj
    cfg = getattr(obj, "config", None)
    if isinstance(cfg, _Mapping):
        return cfg
    env = getattr(obj, "environ", None)
    if isinstance(env, _Mapping):
        return env
    import os as _os
    return _os.environ

try:
    _orig_validate_or_fail  # type: ignore[name-defined]
except Exception:
    _orig_validate_or_fail = validate_or_fail  # type: ignore[misc]

def validate_or_fail(environ=None):  # wrapper keeps API but coerces to Mapping
    env = _as_mapping(environ)
    return _orig_validate_or_fail(env)
# --- end hotfix ---
