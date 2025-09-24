from __future__ import annotations
from typing import Iterable, Tuple
import hashlib

def compute_release_id(records: Iterable[Tuple[str, str]]) -> str:
    """Pure composer: records = iterable of (posix_path, per_file_sha).
    Returns hex sha256 of the ordered fold over "path\\nsha" bytes.
    """
    items = sorted(((p, s) for p, s in records), key=lambda t: t[0])
    h = hashlib.sha256()
    for path, sha in items:
        h.update(path.encode("utf-8")); h.update(b"\n"); h.update(sha.encode("ascii"))
    return h.hexdigest()
