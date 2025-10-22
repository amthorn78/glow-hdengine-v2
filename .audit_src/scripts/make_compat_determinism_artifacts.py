#!/usr/bin/env python3
from __future__ import annotations
import importlib, hashlib, pathlib, sys
from engine.stable.sercanon import serialize
from engine.charts.loader import load_chart

def main():
    mod = importlib.import_module("engine.compat.compute")
    fn = getattr(mod, "compat_public", None)
    if fn is None:
        print("compat_public not implemented", file=sys.stderr)
        sys.exit(2)

    # Use tz from pinned IANA list.
    A = {"birthdate":"1990-05-04","birthtime":"14:22","place":"Austin, US","tz":"Europe/Amsterdam"}
    B = {"birthdate":"1992-07-19","birthtime":"08:05","place":"New York, US","tz":"Europe/Amsterdam"}

    ca, cb = load_chart(**A), load_chart(**B)
    pab, pba = fn(ca, cb), fn(cb, ca)

    outdir = pathlib.Path("artifacts/compat"); outdir.mkdir(parents=True, exist_ok=True)
    ab = serialize(pab); ba = serialize(pba)

    (outdir/"AB.json").write_bytes(ab)
    (outdir/"BA.json").write_bytes(ba)

    assert ab == ba, "AB and BA public bytes must be identical"
    assert ab.endswith(b"\n") and not ab.startswith(b"\xef\xbb\xbf")

    h = hashlib.sha256(ab).hexdigest()
    (outdir/"hash.txt").write_text(h + "\n", encoding="utf-8")

    print("AB_BA_IDENTITY=OK")
    print("PUBLIC_SHA256=", h)

if __name__ == "__main__":
    main()
