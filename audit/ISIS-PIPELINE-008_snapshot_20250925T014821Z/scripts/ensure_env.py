#!/usr/bin/env python3
import os, sys
NEEDED = ["HD_API_BASE_URL","HD_API_KEY","HD_API_SECRET"]
missing = [k for k in NEEDED if not os.environ.get(k)]
print("SECRETS_OK", not missing, "MISSING", ",".join(missing) or "none")
sys.exit(0)  # informational only in 008
