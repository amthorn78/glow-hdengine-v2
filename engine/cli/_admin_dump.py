"""Admin proof dump helpers for the hdctl CLI."""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import stat


def canon_dump(path: str | pathlib.Path, obj: object) -> str:
    """Write canonical JSON plus a .sha256 sidecar, enforcing 0600 perms."""
    target = pathlib.Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(obj, separators=(",", ":"), ensure_ascii=False, sort_keys=True) + "\n"
    target.write_text(data, encoding="utf-8")
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    sidecar = target.parent / f"{target.name}.sha256"
    sidecar.write_text(digest + "\n", encoding="utf-8")
    os.chmod(sidecar, stat.S_IRUSR | stat.S_IWUSR)
    return digest
