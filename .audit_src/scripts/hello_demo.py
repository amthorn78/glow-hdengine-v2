#!/usr/bin/env python3
import sys, json
print("hello from python", sys.version.split()[0])
print(json.dumps({"ok": True}, sort_keys=True, separators=(",", ":")))
