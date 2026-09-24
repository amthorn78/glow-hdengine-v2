#!/usr/bin/env python3
"""Pass 5 (repair round 5, P-88) wrapper: runs one engine command on the newest fetch and records its JSON output under
this directory (the PLAN scratchpad). No body text is printed or written (D22): counts, rule ids and booleans only.

  one.py plan|check <PID> <PAGE> <BATCH>        land.py plan --no-ops (or check) with the new registry and $PKG; for
                                                plan, also the in-memory landing-state proof on the same fetch:
                                                - re-planning the fully landed text reads every edit LANDED;
                                                - each partial landing (every operation left out alone, and every
                                                  operation applied alone) is either repaired to exactly the fully
                                                  landed text or refused; none is repaired to anything else;
                                                - no insertion is doubled in the landed text.
  one.py graph QA-110 <QA110_PAGE> <BATCH> <QA80_PAGE>   graph_check.py --simulate
"""
import json, subprocess, sys, os
from pathlib import Path
sys.dont_write_bytecode = True
EV = Path("/home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/closeout-residuals/plan")
HERE = Path(__file__).resolve().parent
P4 = HERE.parent.parent / "r4/pass4"
URL = "https://app.notion.com/p/" + "0" * 32
mode, pid, page, batch = sys.argv[1:5]
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
if mode == "graph":
    cmd = ["python3", str(EV / "engine/graph_check.py"), "--qa110", page, "--qa80", sys.argv[5], "--simulate"]
    pid = "graph_check"
else:
    cmd = ["python3", str(EV / "engine/land.py"), mode, pid, page, "--registry", str(P4 / "registry.new.md"),
           "--guards", str(EV / "registry/row_assertions.json"), "--skills", str(P4 / "pkg-root")]
    if pid == "CL-40":
        cmd += ["--candidate-url", URL]
    if mode == "plan":
        cmd += ["--no-ops"]
r = subprocess.run(cmd, capture_output=True, text=True, env=env)
try:
    res = json.loads(r.stdout)
except Exception:
    res = {"unparsed_stdout_head": r.stdout[:400], "stderr_tail": r.stderr[-800:]}
proof = None
if mode == "plan":
    sys.path.insert(0, str(EV / "engine"))
    import land as L, dryrun as D  # noqa: E402
    if pid == "CL-40":
        L.fill(URL)
    _, body = D.latest_body(page)
    post, rep, states = L.edit_states(pid, body)
    ops = D.ops_for(body, post)
    full = D.simulate(body, ops)
    _, rep_f, st_f = L.edit_states(pid, full)
    live = [k for k in st_f if rep_f[k]["expected"] > 0]
    subsets = [[j for j in range(len(ops)) if j != i] for i in range(len(ops))]
    if len(ops) > 1:
        subsets += [[i] for i in range(len(ops))]
    rows = []
    for sub in subsets:
        text = D.simulate(body, [ops[j] for j in sub])
        p2, r2, s2 = L.edit_states(pid, text)
        if any(not v["ok"] for v in r2.values()):
            rows.append({"applied": sub, "outcome": "REFUSED_COUNT_MISMATCH"})
            continue
        o2 = D.ops_for(text, p2)
        fixed = D.simulate(text, o2) if o2 is not None else None
        rows.append({"applied": sub, "outcome": "REPAIRED_EXACT" if fixed == full else "REPAIRED_WRONG",
                     "repair": sorted(k for k, s in s2.items() if s == "LANDED")})
    proof = {"pristine_states": sorted({s for k, s in states.items() if rep[k]["expected"] > 0}),
             "ops": len(ops),
             "relanded_all_LANDED": bool(live) and all(st_f[k] == "LANDED" for k in live),
             "relanded_not_LANDED": sorted(k for k in live if st_f[k] != "LANDED"),
             "landed_fn": L.landed(pid, full),
             "doubled_in_landed": L.doubled(pid, L.C.collapse(full)),
             "partials": len(rows),
             "partials_repaired_exact": sum(1 for x in rows if x["outcome"] == "REPAIRED_EXACT"),
             "partials_refused": sum(1 for x in rows if x["outcome"].startswith("REFUSED")),
             "partials_repaired_wrong": sum(1 for x in rows if x["outcome"] == "REPAIRED_WRONG"),
             "rows": rows}
    proof["pass"] = (proof["pristine_states"] == ["NOT_LANDED"] and proof["relanded_all_LANDED"] and proof["landed_fn"]
                     and not proof["doubled_in_landed"] and proof["partials_repaired_wrong"] == 0)
out = HERE / "results" / batch
out.mkdir(parents=True, exist_ok=True)
rec = {"mode": mode, "pid": pid, "page": page, "exit": r.returncode,
       "cmd": " ".join(c.replace(str(P4), "$P4").replace(str(EV), "EV") for c in cmd), "result": res, "state_proof": proof}
(out / f"{pid}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
if isinstance(res, dict) and mode == "plan":
    ok = (bool((res.get("precheck") or {}).get("pass")) and bool((res.get("landed_check") or {}).get("pass"))
          and res.get("repair") == [] and bool(proof and proof["pass"]))
elif isinstance(res, dict):
    ok = res.get("pass")
else:
    ok = None
print(json.dumps({"pid": pid, "mode": mode, "exit": r.returncode, "refused": res.get("refused") if isinstance(res, dict) else None,
                  "pass": ok, "fetched": res.get("fetched") if isinstance(res, dict) else None,
                  "proof": {k: v for k, v in (proof or {}).items() if k != "rows"} or None}))
