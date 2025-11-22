"""Scan for direct JSON emission on governed paths."""
from __future__ import annotations

import subprocess
from pathlib import Path

ALLOWED = {
    "engine/serializer/canon.py",
    "engine/stable/sercanon.py",
    "engine/cli/_admin_dump.py",
}


def main() -> int:
    target_paths = ["engine", "adapter", "presenter"]
    result = subprocess.run(
        ["rg", "json.dumps", *target_paths], capture_output=True, text=True, check=False
    )
    lines = []
    for line in result.stdout.splitlines():
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        path = parts[0]
        if any(path.startswith(ok) for ok in ALLOWED):
            continue
        lines.append(line)

    out_dir = Path("artifacts/cli/guards")
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "serializer_grep_guard.log"
    if lines:
        body = "\n".join(lines) + "\n"
    else:
        body = "no disallowed json.dumps occurrences found\n"
    log_path.write_text(body, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
