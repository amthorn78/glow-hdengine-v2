#!/usr/bin/env python3
"""Record a value in EX/run.json once, and never overwrite it (P-96, P-104).

  runjson.py <run.json> <key> [<value>]

Without <value>, the value is today's UTC date (YYYY-MM-DD). If <key> already holds a value, it is kept and printed
unchanged: a step resumed in a new session, on another day, fills its tokens with the value it recorded the first
time, so an edit already on a page is recognized as landed and is not written again. Prints
{"key", "value", "kept"}; `kept` is true when the value was already recorded. Creates the file (as {}) if it does not
exist. EXECUTE commits and pushes the file before the write that uses the value.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def main():
    if len(sys.argv) not in (3, 4):
        raise SystemExit("usage: runjson.py <run.json> <key> [<value>]")
    path, key = Path(sys.argv[1]), sys.argv[2]
    run = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if run.get(key) not in (None, ""):
        print(json.dumps({"key": key, "value": run[key], "kept": True}))
        return
    value = sys.argv[3] if len(sys.argv) == 4 else datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run[key] = value
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(run, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"key": key, "value": value, "kept": False}))


if __name__ == "__main__":
    main()
