from __future__ import annotations
import re
from pathlib import Path
from typing import Iterable
from tests._helpers.app_import import get_app_factory
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams

_HEX64 = re.compile(r'^"[0-9a-f]{64}"$')  # quoted, lowercase hex

def _has_all(h: str, parts: Iterable[str]) -> bool:
    hv = [x.strip().lower() for x in h.split(",")] if h else []
    return all(p.lower() in hv for p in parts)

def _params() -> dict[str, str]:
    # Dev GET /reader requires exactly v=1 and a complete fixture pair (PF05 5.4).
    return {
        "v": "1",
        "a": str(Path("fixtures/charts/alice.json").resolve()),
        "b": str(Path("fixtures/charts/bob.json").resolve()),
        "a_tz": "UTC",
        "b_tz": "UTC",
    }

def test_reader_200_304_head_and_vary(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_ENV", "dev")
    # An eligible pair is served only against an admitted release.
    inject_seams(monkeypatch, build_bundle(tmp_path), build_pack(tmp_path))
    create_app = get_app_factory()
    app = create_app()
    q = _params()
    with app.test_client() as c:
        r200 = c.get("/reader", query_string=q)
        assert r200.status_code == 200
        etag = r200.headers.get("ETag")
        assert etag and _HEX64.match(etag), f"bad ETag: {etag}"
        vary = r200.headers.get("Vary", "")
        assert _has_all(vary, ["Authorization", "Accept-Encoding"])

        # Conditional GET hit → 304 with empty body
        r304 = c.get("/reader", query_string=q, headers={"If-None-Match": etag})
        assert r304.status_code == 304
        assert r304.data == b""

        # Header parity on 304
        assert r304.headers.get("ETag") == etag
        assert _has_all(r304.headers.get("Vary",""), ["Authorization","Accept-Encoding"])

        # HEAD mirrors logic, empty body
        rhead = c.head("/reader", query_string=q, headers={"If-None-Match": etag})
        assert rhead.status_code in (200, 304)
        assert rhead.get_data() == b""

        # Wildcard is treated as miss
        rwild = c.get("/reader", query_string=q, headers={"If-None-Match": "*"})
        assert rwild.status_code == 200
