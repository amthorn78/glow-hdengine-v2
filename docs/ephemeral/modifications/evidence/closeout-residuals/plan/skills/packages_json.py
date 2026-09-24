#!/usr/bin/env python3
"""X4.3 (execute.4b, P-100): write EX/packages.json from the seven archives and their extracted freeze lines.

  packages_json.py <skills-out dir> <skills-ext/freeze.txt> <EX/packages.json>

For each package: the archive's file name, its number of file entries, its size in bytes and its sha256 (read from
the archive), and the freeze line of the tree it extracts to (from freeze.txt, which execute.4b has already compared
with EV/skills/expected_after_patch.txt). Refuses unless there are exactly the seven archives and seven freeze lines.
Writes only the output file. No archive content is printed or copied.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

SEVEN = ["flowmaster-validate", "change-flow", "glow-graph-contract", "session-relay-flowmaster",
         "glow-hde-pr-development", "amthor-workspace-governance-audit", "glow-po-reporting"]


def main():
    out_dir, freeze_txt, dest = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
    freeze = {}
    for line in freeze_txt.read_text(encoding="utf-8").splitlines():
        name, files, digest = line.split()
        freeze[name] = f"{files} {digest}"
    archives = sorted(p.name for p in out_dir.glob("*.skill"))
    if archives != sorted(f"{s}.skill" for s in SEVEN) or sorted(freeze) != sorted(SEVEN):
        raise SystemExit(json.dumps({"refused": "NOT_THE_SEVEN", "archives": archives, "freeze": sorted(freeze)}))
    rows = []
    for s in SEVEN:
        p = out_dir / f"{s}.skill"
        data = p.read_bytes()
        with zipfile.ZipFile(p) as z:
            files = sum(1 for i in z.infolist() if not i.is_dir())
        rows.append({"skill": s, "file": p.name, "files": files, "bytes": len(data),
                     "sha256": hashlib.sha256(data).hexdigest(), "freeze": freeze[s]})
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps({"out_dir": str(out_dir), "archives": rows}, indent=1) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r['file']} {r['files']} {r['bytes']} {r['sha256']} {r['freeze']}")


if __name__ == "__main__":
    main()
