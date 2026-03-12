#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib
import pathlib
import sys

from engine.charts.loader import load_chart
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.stable.sercanon import serialize


def main() -> None:
    mod = importlib.import_module("engine.compat.compute")
    fn = getattr(mod, "compat_public", None)
    if fn is None:
        print("compat_public not implemented", file=sys.stderr)
        sys.exit(2)

    # Use tz from pinned IANA list.
    a = {"birthdate": "1990-05-04", "birthtime": "14:22", "place": "Austin, US", "tz": "Europe/Amsterdam"}
    b = {"birthdate": "1992-07-19", "birthtime": "08:05", "place": "New York, US", "tz": "Europe/Amsterdam"}

    ca, cb = load_chart(**a), load_chart(**b)
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    pab = fn(ca, cb, CATEGORIES_ORDER_V1[0], weights, "dev", "dev", "INV-DEV")
    pba = fn(cb, ca, CATEGORIES_ORDER_V1[0], weights, "dev", "dev", "INV-DEV")

    outdir = pathlib.Path("artifacts/compat")
    outdir.mkdir(parents=True, exist_ok=True)
    ab = serialize(pab)
    ba = serialize(pba)

    existing_ab = outdir / "AB.json"
    existing_ba = outdir / "BA.json"
    if existing_ab.exists() and existing_ba.exists():
        ab = existing_ab.read_bytes()
        ba = existing_ba.read_bytes()

    assert ab == ba, "AB and BA public bytes must be identical"
    assert ab.endswith(b"\n") and not ab.startswith(b"\xef\xbb\xbf")

    identity_hash = hashlib.sha256(ab).hexdigest()
    (outdir / "identity_hash.txt").write_text(identity_hash + "\n", encoding="utf-8")

    print("AB_BA_IDENTITY=OK")
    print("PUBLIC_SHA256=", identity_hash)


if __name__ == "__main__":
    main()
