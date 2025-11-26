"""Admin proof dump helpers for the hdctl CLI."""
from __future__ import annotations

import hashlib
import os
import pathlib
import stat

from engine.serializer.canon import sercanon


def canon_dump(path: str | pathlib.Path, obj: object) -> str:
    """Write canonical JSON plus a .sha256 sidecar, enforcing 0600 perms."""
    target = pathlib.Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data_bytes = sercanon(obj)
    target.write_bytes(data_bytes)
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
    digest = hashlib.sha256(data_bytes).hexdigest()
    sidecar = target.parent / f"{target.name}.sha256"
    sidecar.write_text(digest + "\n", encoding="utf-8")
    os.chmod(sidecar, stat.S_IRUSR | stat.S_IWUSR)
    return digest
