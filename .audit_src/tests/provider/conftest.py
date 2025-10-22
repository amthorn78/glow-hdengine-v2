from __future__ import annotations

import json
import logging
import os
import pathlib
import subprocess
import tempfile
from hashlib import sha256
from typing import Optional

from adapter.env_guard import EnvGuardError
from engine.provider.base import Provider
from engine.provider.fixtures import FixturesProvider
from engine.provider.internal_engine import InternalEngineProvider
from engine.provider.vendor_http import VendorHttpProvider


"""
Provider resolver (Python-first, no import-time I/O)

Precedence:
  SECRETS -> ENV -> DEFAULT(fixtures)

Guards:
  - Prod: any override (ENGINE_SECRETS_DIR or ENV) -> CANON_TOGGLES_OVERRIDE_IN_PROD
  - SAFE_MODE: non-fixtures may refuse to construct; vendor may raise on call-time use.

Artifacts:
  - artifacts/provider/decision.txt (0600, single trailing LF), written only after *successful* resolve.

Logging (keys-only):
  - Success:  {route:"provider.resolve", provider, source, safe_mode, correlation_id}
  - Error:    {route:"provider.resolve.error", code, source, correlation_id}
  - Startup:  {route:"provider.startup", provider, source, safe_mode, correlation_id}  # once per process
"""

# ---------------- Canonical pins ----------------
DEFAULT_PROVIDER = "fixtures"
_ALLOWED = {"fixtures", "internal_engine", "vendor_http"}

# One-time guards (process-local)
_decision_written = False
_startup_logged = False

_log = logging.getLogger("engine.provider")


# ---------------- Helpers ----------------
def _is_prod() -> bool:
    env = (os.environ.get("ENGINE_ENV") or os.environ.get("APP_ENV") or "").lower()
    return env == "prod"


def _repo_root() -> pathlib.Path:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        return pathlib.Path(out)
    except Exception:
        return pathlib.Path.cwd()


def _is_under(path: pathlib.Path, base: pathlib.Path) -> bool:
    path = path.resolve()
    base = base.resolve()
    return path == base or base in path.parents


def _validate_secrets_dir(raw: str) -> pathlib.Path:
    rp = pathlib.Path(raw).resolve()
    if not rp.exists() or not rp.is_dir():
        raise EnvGuardError(
            "PROVIDER_SECRETS_DIR_INVALID",
            "secrets dir invalid",
            {"path": str(rp)},
        )
    allow_repo = _repo_root()
    allow_tmp = pathlib.Path(tempfile.gettempdir()).resolve()
    if not (_is_under(rp, allow_repo) or _is_under(rp, allow_tmp)):
        raise EnvGuardError(
            "PROVIDER_SECRETS_DIR_INVALID",
            "secrets dir invalid",
            {"path": str(rp)},
        )
    return rp


def _secrets_dir() -> pathlib.Path:
    override = os.environ.get("ENGINE_SECRETS_DIR")
    if override:
        if _is_prod():
            raise EnvGuardError(
                "CANON_TOGGLES_OVERRIDE_IN_PROD",
                "ENGINE_SECRETS_DIR is forbidden in prod",
                {"var": "ENGINE_SECRETS_DIR"},
            )
        return _validate_secrets_dir(override)
    return pathlib.Path("secrets")


def _secrets_path() -> pathlib.Path:
    return _secrets_dir() / "provider.json"


def _normalize_name(name: str) -> str:
    return name.strip().lower()


def _ensure_cid(correlation_id: Optional[str], seed: str) -> str:
    """Synthesize CID-<8hex> if not supplied; deterministic on seed."""
    if correlation_id:
        return correlation_id
    h = sha256(seed.encode("utf-8")).hexdigest()[:8]
    return f"CID-{h}"


def _atomic_write(path: pathlib.Path, data: bytes) -> None:
    """
    Write bytes atomically with perms 0600 and a single trailing LF (caller-provided).
    fsync file and directory. No import-time I/O—only call from resolve().
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    dir_fd = os.open(path.parent, os.O_DIRECTORY)
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as tmp:
            tmp_path = pathlib.Path(tmp.name)
            tmp.write(data)
            tmp.flush()
            os.fchmod(tmp.fileno(), 0o600)
            os.fsync(tmp.fileno())
        os.replace(tmp_path, path)
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)


def _write_decision(name: str, source: str) -> None:
    """Write decision artifact atomically (0600) with a single trailing LF.
    Safe if called multiple times; writes once per process, and only recreates if missing."""
    global _decision_written
    d = pathlib.Path("artifacts/provider")
    path = d / "decision.txt"
    if _decision_written and path.exists():
        return
    content = f"provider={name} source={source}\n".encode("utf-8")
    _atomic_write(path, content)
    _decision_written = True


# ---------------- Public API ----------------
def resolve_provider(correlation_id: Optional[str] = None) -> Provider:
    """
    Resolve and instantiate a provider with pinned precedence:
      SECRETS -> ENV -> DEFAULT(fixtures).

    Guards:
      * Prod: any override (ENGINE_SECRETS_DIR or ENV) -> CANON_TOGGLES_OVERRIDE_IN_PROD
      * SAFE_MODE: non-fixtures may refuse to construct; vendor may raise on call-time network use.

    Logging:
      keys-only JSON lines. Startup line is emitted once per process on the first success.
    """
    name: Optional[str] = None
    source = "default"

    # 1) SECRETS (if present)
    p = _secrets_path()
    if p.exists():
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:
            cid = _ensure_cid(correlation_id, "error:PROVIDER_SECRETS_UNREADABLE|secrets")
            _log.info(
                json.dumps(
                    {
                        "route": "provider.resolve.error",
                        "code": "PROVIDER_SECRETS_UNREADABLE",
                        "source": "secrets",
                        "correlation_id": cid,
                    }
                )
            )
            raise EnvGuardError(
                "PROVIDER_SECRETS_UNREADABLE",
                "secrets file unreadable",
                {"source": "secrets", "path": str(p)},
            )
        try:
            obj = json.loads(txt)
        except Exception:
            cid = _ensure_cid(correlation_id, "error:PROVIDER_SECRETS_PARSE_ERROR|secrets")
            _log.info(
                json.dumps(
                    {
                        "route": "provider.resolve.error",
                        "code": "PROVIDER_SECRETS_PARSE_ERROR",
                        "source": "secrets",
                        "correlation_id": cid,
                    }
                )
            )
            raise EnvGuardError(
                "PROVIDER_SECRETS_PARSE_ERROR",
                "secrets JSON invalid",
                {"source": "secrets", "path": str(p)},
            )
        prov = obj.get("provider")
        if not isinstance(prov, str) or not prov:
            raise EnvGuardError(
                "PROVIDER_MISCONFIGURED",
                "provider value missing/invalid",
                {"source": "secrets", "path": str(p)},
            )
        name, source = _normalize_name(prov), "secrets"

    # 2) ENV
    if name is None:
        env_val = os.environ.get("ENGINE_PROVIDER")
        if env_val:
            name, source = _normalize_name(env_val), "env"

    # 3) DEFAULT
    if name is None:
        name, source = DEFAULT_PROVIDER, "default"

    # Prod guard
    if _is_prod() and source != "default":
        cid = _ensure_cid(correlation_id, f"error:CANON_TOGGLES_OVERRIDE_IN_PROD|{source}")
        _log.info(
            json.dumps(
                {
                    "route": "provider.resolve.error",
                    "code": "CANON_TOGGLES_OVERRIDE_IN_PROD",
                    "source": source,
                    "correlation_id": cid,
                }
            )
        )
        raise EnvGuardError(
            "CANON_TOGGLES_OVERRIDE_IN_PROD",
            f"provider override via {source} forbidden in prod",
            {"source": source, "provider": name},
        )

    # Validate name
    if name not in _ALLOWED:
        cid = _ensure_cid(correlation_id, f"error:PROVIDER_MISCONFIGURED|{source}")
        _log.info(
            json.dumps(
                {
                    "route": "provider.resolve.error",
                    "code": "PROVIDER_MISCONFIGURED",
                    "source": source,
                    "correlation_id": cid,
                }
            )
        )
        raise EnvGuardError(
            "PROVIDER_MISCONFIGURED",
            f"unknown provider '{name}'",
            {"provider": name, "source": source},
        )

    # SAFE_MODE rails
    safe_mode = os.environ.get("SAFE_MODE", "1") == "1"

    # Construct
    if name == "fixtures":
        prov: Provider = FixturesProvider()
    elif name == "internal_engine":
        if safe_mode:
            cid = _ensure_cid(correlation_id, "error:PROVIDER_UNAVAILABLE|internal_engine")
            _log.info(
                json.dumps(
                    {
                        "route": "provider.resolve.error",
                        "code": "PROVIDER_UNAVAILABLE",
                        "source": source,
                        "correlation_id": cid,
                    }
                )
            )
            raise EnvGuardError(
                "PROVIDER_UNAVAILABLE",
                "internal_engine refused under SAFE_MODE",
                {"safe_mode": True},
            )
        prov = InternalEngineProvider()
    elif name == "vendor_http":
        try:
            prov = VendorHttpProvider(safe_mode=safe_mode)
        except EnvGuardError as e:
            cid = _ensure_cid(correlation_id, f"error:{getattr(e, 'code', 'ERR')}|vendor_http")
            _log.info(
                json.dumps(
                    {
                        "route": "provider.resolve.error",
                        "code": getattr(e, "code", "ERR"),
                        "source": source,
                        "correlation_id": cid,
                    }
                )
            )
            raise
    else:
        # Unreachable due to _ALLOWED
        raise EnvGuardError(
            "PROVIDER_MISCONFIGURED",
            f"unknown provider '{name}'",
            {"provider": name},
        )

    # One-time startup line (first successful resolve only)
    global _startup_logged
    if not _startup_logged:
        cid = _ensure_cid(correlation_id, f"{name}|{source}")
        _log.info(
            json.dumps(
                {
                    "route": "provider.startup",
                    "provider": name,
                    "source": source,
                    "safe_mode": safe_mode,
                    "correlation_id": cid,
                }
            )
        )
        _startup_logged = True

    # Success: write decision and log
    _write_decision(name, source)
    cid = _ensure_cid(correlation_id, f"{name}|{source}")
    _log.info(
        json.dumps(
            {
                "route": "provider.resolve",
                "provider": name,
                "source": source,
                "safe_mode": safe_mode,
                "correlation_id": cid,
            }
        )
    )
    return prov