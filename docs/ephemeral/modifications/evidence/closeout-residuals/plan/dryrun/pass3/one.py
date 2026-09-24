#!/usr/bin/env python3
"""Pass 3 (landing rehearsal) wrapper: runs one engine command on the newest fetch and records its JSON output.

  one.py plan|check <PID> <PAGE> <BATCH>        land.py plan --no-ops (or check) with the new registry and $PKG
  one.py graph QA-110 <QA110_PAGE> <BATCH> <QA80_PAGE>   graph_check.py --simulate
Writes EV/dryrun/pass3/<BATCH>/<PID>.json ({mode, pid, page, exit, result}); prints one summary line. The engine
prints no body text (D22), so neither does this.
"""
import json, subprocess, sys, os
from pathlib import Path
sys.dont_write_bytecode = True
EV = Path("/home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/closeout-residuals/plan")
P3 = Path(__file__).resolve().parent
mode, pid, page, batch = sys.argv[1:5]
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
if mode == "graph":
    cmd = ["python3", str(EV / "engine/graph_check.py"), "--qa110", page, "--qa80", sys.argv[5], "--simulate"]
    pid = "graph_check"
else:
    cmd = ["python3", str(EV / "engine/land.py"), mode, pid, page, "--registry", str(P3 / "registry.new.md"),
           "--guards", str(EV / "registry/row_assertions.json"), "--skills", str(P3 / "pkg-root")]
    if mode == "plan":
        cmd += ["--no-ops", "--candidate-url", "https://app.notion.com/p/" + "0" * 32]
r = subprocess.run(cmd, capture_output=True, text=True, env=env)
try:
    res = json.loads(r.stdout)
except Exception:
    res = {"unparsed_stdout_head": r.stdout[:400], "stderr_tail": r.stderr[-800:]}
out = EV / "dryrun/pass3" / batch
out.mkdir(parents=True, exist_ok=True)
rec = {"mode": mode, "pid": pid, "page": page, "exit": r.returncode,
       "cmd": " ".join(c.replace(str(P3), "$P3").replace(str(EV), "EV") for c in cmd), "result": res}
(out / f"{pid}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
pre = res.get("precheck", res) if isinstance(res, dict) else {}
print(json.dumps({"pid": pid, "mode": mode, "exit": r.returncode, "refused": res.get("refused") if isinstance(res, dict) else None,
                  "pass": (pre.get("pass") if isinstance(pre, dict) else None), "fetched": res.get("fetched") if isinstance(res, dict) else None,
                  "source_file": res.get("source_file") if isinstance(res, dict) else None}))
