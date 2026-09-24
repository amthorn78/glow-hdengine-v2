#!/usr/bin/env python3
"""Pass 4 (landing rehearsal with the readback, P-76) wrapper: runs one engine command on the newest fetch and records
its JSON output under this directory (the PLAN scratchpad). The engine prints no body text (D22), so neither does this.

  one.py plan|check <PID> <PAGE> <BATCH>        land.py plan --no-ops (or check) with the new registry and $PKG
  one.py graph QA-110 <QA110_PAGE> <BATCH> <QA80_PAGE>   graph_check.py --simulate
"""
import json, subprocess, sys, os
from pathlib import Path
sys.dont_write_bytecode = True
EV = Path("/home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/closeout-residuals/plan")
HERE = Path(__file__).resolve().parent
mode, pid, page, batch = sys.argv[1:5]
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
if mode == "graph":
    cmd = ["python3", str(EV / "engine/graph_check.py"), "--qa110", page, "--qa80", sys.argv[5], "--simulate"]
    pid = "graph_check"
else:
    cmd = ["python3", str(EV / "engine/land.py"), mode, pid, page, "--registry", str(HERE / "registry.new.md"),
           "--guards", str(EV / "registry/row_assertions.json"), "--skills", str(HERE / "pkg-root")]
    if pid == "CL-40":
        cmd += ["--candidate-url", "https://app.notion.com/p/" + "0" * 32]
    if mode == "plan":
        cmd += ["--no-ops"]
r = subprocess.run(cmd, capture_output=True, text=True, env=env)
try:
    res = json.loads(r.stdout)
except Exception:
    res = {"unparsed_stdout_head": r.stdout[:400], "stderr_tail": r.stderr[-800:]}
out = HERE / "results" / batch
out.mkdir(parents=True, exist_ok=True)
rec = {"mode": mode, "pid": pid, "page": page, "exit": r.returncode,
       "cmd": " ".join(c.replace(str(HERE), "$P4").replace(str(EV), "EV") for c in cmd), "result": res}
(out / f"{pid}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
if isinstance(res, dict) and mode == "plan":
    ok = bool((res.get("precheck") or {}).get("pass")) and bool((res.get("landed_check") or {}).get("pass"))
elif isinstance(res, dict):
    ok = res.get("pass")
else:
    ok = None
print(json.dumps({"pid": pid, "mode": mode, "exit": r.returncode, "refused": res.get("refused") if isinstance(res, dict) else None,
                  "pass": ok, "fetched": res.get("fetched") if isinstance(res, dict) else None,
                  "source_file": res.get("source_file") if isinstance(res, dict) else None}))
