
from __future__ import annotations
import os, tempfile
from pathlib import Path
from adapter.env_guard import validate_or_fail

ARTIFACT = Path("artifacts/hotfix/env_guard_import_ok.txt")

def _write_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".tmp.")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
        dirfd = os.open(path.parent, os.O_DIRECTORY)
        try: os.fsync(dirfd)
        finally: os.close(dirfd)
        os.chmod(path, 0o600)
    finally:
        try:
            if os.path.exists(tmp): os.remove(tmp)
        except Exception:
            pass

def main() -> None:
    # Non-prod mapping so this never throws here
    validate_or_fail({"APP_ENV": "dev"})
    _write_atomic(ARTIFACT, b"ENV_GUARD_IMPORT_OK\n")

if __name__ == "__main__":
    main()
