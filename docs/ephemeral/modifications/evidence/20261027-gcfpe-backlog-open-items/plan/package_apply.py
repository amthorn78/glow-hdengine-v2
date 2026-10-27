#!/usr/bin/env python3
"""Apply package-redlines.json to copies of the installed skills (MODIFICATION-20261011-gcfpe-mb008-to-promotion).

  package_apply.py <skills-dir> [--check]
      <skills-dir> holds copies of the skills named in the redlines (never the synced install directory). Each op's
      `old` must occur exactly `count` times before it is replaced; any mismatch stops before anything is written.
      --check reports, without writing, whether every op is untouched (applicable) or landed (its `new` present and
      its `old` gone, or `old` still present only inside `new`).

Writes only <skills-dir>. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OPS = json.loads((HERE / "package-redlines.json").read_text(encoding="utf-8"))["ops"]


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve()
    if "/skills/synced/" in str(root):
        print(json.dumps({"error": "refusing the synced install directory"}))
        return 2
    check = "--check" in argv
    texts: dict[Path, str] = {}
    rows, ok = [], True
    for op in OPS:
        path = root / op["skill"] / op["file"]
        text = texts.setdefault(path, path.read_text(encoding="utf-8"))
        n_old = text.count(op["old"])
        landed = op["new"] != "" and text.count(op["new"]) >= 1 and n_old == op["new"].count(op["old"])
        landed = landed or (op["new"] == "" and n_old == 0)
        state = "UNTOUCHED" if n_old == op["count"] and not (op["new"] and op["new"] in text) else (
            "LANDED" if landed else "CONFLICT")
        rows.append({"id": op["id"], "state": state})
        if state == "CONFLICT" or (not check and state != "UNTOUCHED"):
            ok = False
            continue
        if not check:
            texts[path] = text.replace(op["old"], op["new"])
    if not check and ok:
        for path, text in texts.items():
            path.write_text(text, encoding="utf-8")
    print(json.dumps({"mode": "check" if check else "apply", "ok": ok, "written": (not check and ok),
                      "rows": rows}, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main(sys.argv))
