#!/usr/bin/env python3
"""P-108 proof: `land.py state CL-40` with no --candidate-url fills X4.5's stand-in URL. On CL-40's newest fetch it
reads UNTOUCHED (exit 0); on the same fetch landed in memory with a real-form URL (as X5.4 would land it) it does not
read UNTOUCHED, so a landed page is still listed by the stop sweep. Runs land.py's own main() in-process; prints
verdicts and counts only (D22).

  cl40_state.py [--since-minutes N]
"""
import contextlib
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
EV = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(EV / "engine"))
import dryrun as D  # noqa: E402
import land as L  # noqa: E402

PAGE = "3db4590a05eb81db9c88cde6027e07bf"
REAL = "https://app.notion.com/p/" + "1234abcd" * 4
since = int(sys.argv[sys.argv.index("--since-minutes") + 1]) if "--since-minutes" in sys.argv else 30
D.SINCE = since * 60
_, body = D.latest_body(PAGE)
src = D.SOURCE
rules0 = list(L.R.RULES)


def state_on(text, url=None):
    L.R.RULES[:] = rules0
    D.latest_body = lambda p: ("in-memory", text)
    sys.argv = ["land.py", "state", "CL-40", PAGE] + (["--candidate-url", url] if url else [])
    out, code = io.StringIO(), 0
    with contextlib.redirect_stdout(out):
        try:
            L.main()
        except SystemExit as e:
            code = e.code or 0
    return code, json.loads(out.getvalue())


L.fill(REAL)
post, rep, states = L.edit_states("CL-40", body)
landed = D.simulate(body, D.ops_for(body, post))
L.R.RULES[:] = rules0
rows = {}
for name, text, url in [("fetch, no url", body, None), ("landed with a real url, no url", landed, None),
                        ("landed with a real url, that url", landed, REAL)]:
    code, out = state_on(text, url)
    rows[name] = {"exit": code, "verdict": out.get("verdict"), "candidate_url": out.get("candidate_url"),
                  "refused": out.get("refused")}
ok = (rows["fetch, no url"] == {"exit": 0, "verdict": "UNTOUCHED", "candidate_url": "stand-in", "refused": None}
      and rows["landed with a real url, no url"]["verdict"] not in ("UNTOUCHED", None)
      and rows["landed with a real url, that url"]["verdict"] == "LANDED")
print(json.dumps({"source_file": src, "all_ok": ok, "cases": rows}, indent=1))
