#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import pathlib

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public
from engine.presenter import emit_public

def _build_conjunction(left_uid: str, right_uid: str) -> bytes:
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    payload = conjunction_public(
        {"person_uid": left_uid},
        {"person_uid": right_uid},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
    )
    return emit_public(payload)


def main():
    outdir = pathlib.Path("artifacts/compat")
    outdir.mkdir(parents=True, exist_ok=True)

    ab = _build_conjunction("alice", "bob")
    ba = _build_conjunction("bob", "alice")
    assert ab == ba, "AB and BA conjunction bytes must be identical"
    assert ab.endswith(b"\n") and not ab.startswith(b"\xef\xbb\xbf")

    (outdir / "AB.json").write_bytes(ab)
    (outdir / "BA.json").write_bytes(ba)

    identity_hash = hashlib.sha256(ab).hexdigest()
    (outdir / "identity_hash.txt").write_text(identity_hash + "\n", encoding="utf-8")

    print("AB_BA_IDENTITY=OK")
    print("CONJUNCTION_PUBLIC_SHA256=", identity_hash)

if __name__ == "__main__":
    main()
