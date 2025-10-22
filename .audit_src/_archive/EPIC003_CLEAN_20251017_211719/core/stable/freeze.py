from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List
import hashlib, json

INCLUDE = [
    "freeze/*.json",
    "catalog/*.json",
    "config/bands_*.json",
    "schemas/*catalog*_v*.schema.json",
]
EXCLUDE_SUBSTR = (".backup.", "~", ".bak", ".tmp", "#")
EXCLUDE_DIRS = (".venv", "__pycache__", "node_modules")

@dataclass(frozen=True)
class Record:
    path: str   # POSIX repo-relative
    sha256: str # sha of stable JSON bytes (via sercanon)
    size: int   # raw file size in bytes

def _posix(p: Path) -> str:
    return p.as_posix()

def _should_include(p: Path) -> bool:
    s = _posix(p)
    return not any(x in s for x in EXCLUDE_SUBSTR)

def _stable_json_bytes(raw: bytes) -> bytes:
    # Parse JSON, then canonicalize using the 006 serializer canon.
    # If NaN/Inf appear, sercanon normalization will raise ValueError.
    from core.stable.sercanon import stable_dumps
    data = json.loads(raw.decode("utf-8"))
    return stable_dumps(data)

def iter_records(root: str = ".") -> Iterator[Record]:
    base = Path(root)
    paths: List[Path] = []
    for pat in INCLUDE:
        paths.extend(base.glob(pat))
    seen = set()
    for p in sorted(paths, key=lambda q: q.as_posix()):
        if not p.is_file(): 
            continue
        posix = _posix(p)
        if any(d in p.parts for d in EXCLUDE_DIRS):
            continue
        if posix in seen or not _should_include(p):
            continue
        seen.add(posix)
        raw = p.read_bytes()
        sb = _stable_json_bytes(raw)
        h = hashlib.sha256(sb).hexdigest()
        yield Record(path=posix, sha256=h, size=len(raw))
