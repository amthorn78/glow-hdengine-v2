from __future__ import annotations

from pathlib import Path
from typing import Any
import datetime as _dt
import hashlib

from engine.db import (
    DBAccess,
    Statement,
    BridgeUnavailable,
    BridgeUnsupported,
    IntrospectionError,
    PrimaryUnavailable,
    SqlExecError,
    TxError,
)

ADAPTER_SNAPSHOT = "artifacts/db_bridge/adapter_selection.snapshot.json"

# Backwards-compatible alias used by legacy scripts/tests.
MissingDbConfigError = PrimaryUnavailable


def db_access() -> DBAccess:
    return DBAccess.for_current_env(snapshot_path=ADAPTER_SNAPSHOT)


def ensure_artifact(path: str) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def write_text(path: str, content: str) -> None:
    target = ensure_artifact(path)
    target.write_text(content, encoding="utf-8")


def write_json(path: str, payload: Any) -> None:
    import json

    target = ensure_artifact(path)
    target.write_text(json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")


def write_path_proof(path: str) -> None:
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"artifact not found: {path}")
    proof_path = Path(f"{path}.path_proof.txt")
    proof_path.parent.mkdir(parents=True, exist_ok=True)
    data = target.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    stat = target.stat()
    mtime = _dt.datetime.fromtimestamp(stat.st_mtime, tz=_dt.timezone.utc).replace(microsecond=0)
    proof = "\n".join(
        [
            f"path: {path}",
            f"sha256: {sha}",
            f"size_bytes: {stat.st_size}",
            f"mtime_utc: {mtime.isoformat().replace('+00:00', 'Z')}",
            "",
        ]
    )
    proof_path.write_text(proof, encoding="utf-8")


__all__ = [
    "ADAPTER_SNAPSHOT",
    "DBAccess",
    "Statement",
    "db_access",
    "ensure_artifact",
    "write_text",
    "write_json",
    "write_path_proof",
    "MissingDbConfigError",
    "BridgeUnavailable",
    "BridgeUnsupported",
    "IntrospectionError",
    "PrimaryUnavailable",
    "SqlExecError",
    "TxError",
]
