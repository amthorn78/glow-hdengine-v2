from __future__ import annotations
from typing import Dict, Optional, Tuple, Iterable

# Public constants (used by adapter routes & tests)
VARY_VAL = "Authorization, Accept-Encoding"
READER_CACHE = "private, no-cache, must-revalidate"
NO_STORE = "no-store"

def _parse_if_none_match(header: Optional[str]) -> Iterable[str]:
    """
    Return a set of strong, quoted tokens from If-None-Match.
    - Ignore weak validators (W/...) entirely.
    - Split CSV tokens; strip whitespace; drop empties.
    """
    if not header:
        return set()
    out = set()
    for part in header.split(","):
        t = part.strip()
        if not t or t.startswith("W/"):
            continue
        out.add(t)
    return out

def reader_response(
    public_bytes: bytes,
    id_hash_hex: str,
    if_none_match: Optional[str],
    method: str = "GET",
) -> Tuple[int, Dict[str, str], bytes]:
    """
    Adapter response builder for Reader:
    - ETag is the strong, quoted engine id hash (lowercase hex), derived upstream.
    - 304 on exact strong match; empty body; Content-Length: 0; parity headers.
    - HEAD mirrors GET logic; always empty body.
    - Wildcard '*' treated as miss; compression invariance handled by not touching bytes.
    """
    etag = f"\"{id_hash_hex}\""
    tokens = _parse_if_none_match(if_none_match)
    wildcard = "*" in tokens
    matched = (etag in tokens) and not wildcard

    base_headers: Dict[str, str] = {
        "ETag": etag,
        "Cache-Control": READER_CACHE,
        "Vary": VARY_VAL,
    }

    is_head = method.upper() == "HEAD"

    if matched:
        headers = dict(base_headers)
        headers["Content-Length"] = "0"
        return 304, headers, b""

    if is_head:
        headers = dict(base_headers)
        headers["Content-Length"] = "0"
        return 200, headers, b""

    # GET miss → 200 with literal engine bytes (unchanged)
    return 200, base_headers, public_bytes

def writer_headers() -> Dict[str, str]:
    """Headers for writers and any non-200 error branch."""
    return {"Cache-Control": NO_STORE}
