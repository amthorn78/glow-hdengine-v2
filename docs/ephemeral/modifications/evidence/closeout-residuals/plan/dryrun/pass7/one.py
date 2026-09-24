#!/usr/bin/env python3
"""Pass 7 (repair round 7, P-103) wrapper: runs one engine command on the newest fetch and records its JSON output
under this directory (the PLAN scratchpad). No body text is printed or written (D22): counts, rule ids, refusals and
booleans only.

  one.py plan|check <PID> <PAGE> <BATCH>        land.py plan --no-ops (or check) with the new registry and $PKG, as a
                                                subprocess; for plan, also the in-process landing proof on the same
                                                fetch, through land.py's own main() (the real refusal chain):
                                                - `state` reads UNTOUCHED on the fetch and LANDED on the landed text;
                                                - `plan` on the landed text refuses ALREADY_LANDED (exit 3);
                                                - each DISTINCT partial landing (every operation left out alone, and
                                                  every operation applied alone; the empty and the full set and
                                                  duplicates dropped) is planned by main(): its operations reproduce
                                                  exactly the landed text, or it is refused; `state` reads PARTIAL;
                                                - no insertion is doubled in the landed text;
                                                - P-103: every operation's old_str is absent from the landed text
                                                  (sent again on a stale read it matches nothing), except those
                                                  reapply_unsafe names, each of which is listed.
  one.py graph QA-110 <QA110_PAGE> <BATCH> <QA80_PAGE>   graph_check.py --simulate
"""
import contextlib
import hashlib
import io
import json
import os
import subprocess
import sys
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
    _, body = D.latest_body(page)
    src = D.SOURCE
    extra = ["--candidate-url", URL] if pid == "CL-40" else []
    base = ["--registry", str(P4 / "registry.new.md"), "--guards", str(EV / "registry/row_assertions.json"),
            "--skills", str(P4 / "pkg-root")]
    # checks() runs the body validator in a subprocess; the same text gives the same verdict, so it is memoized
    _orig_checks, _memo = L.checks, {}

    def _checks(pid_, text_, a_, mode_):
        k = (hashlib.sha256(text_.encode()).hexdigest(), mode_)
        if k not in _memo:
            _memo[k] = _orig_checks(pid_, text_, a_, mode_)
        return _memo[k]
    L.checks = _checks

    def main_on(text, m, no_ops=False):
        D.latest_body = lambda p: ("in-memory", text)
        D.SOURCE = "in-memory"
        sys.argv = ["land.py", m, pid, page] + base + extra + (["--no-ops"] if no_ops else [])
        out, code = io.StringIO(), 0
        with contextlib.redirect_stdout(out):
            try:
                L.main()
            except SystemExit as e:
                code = e.code or 0
        try:
            return code, json.loads(out.getvalue())
        except Exception:
            return code, {"raw_head": out.getvalue()[:200]}

    if pid == "CL-40":
        L.fill(URL)
    post, rep, states = L.edit_states(pid, body)
    ops = D.ops_for(body, post)
    full = D.simulate(body, ops)
    c0, s0 = main_on(body, "state")
    c1, s1 = main_on(full, "state")
    c2, p2 = main_on(full, "plan", no_ops=True)
    n = len(ops)
    subsets, seen = [], set()
    for sub in [[j for j in range(n) if j != i] for i in range(n)] + [[i] for i in range(n)]:
        key = tuple(sub)
        if 0 < len(sub) < n and key not in seen:
            seen.add(key)
            subsets.append(sub)
    rows = []
    for sub in subsets:
        text = D.simulate(body, [ops[j] for j in sub])
        cs, ss = main_on(text, "state")
        cp, jp = main_on(text, "plan")
        if cp == 0:
            fixed = D.simulate(text, jp["ops"])
            outcome = "REPAIRED_EXACT" if fixed == full else "REPAIRED_WRONG"
        else:
            outcome = "REFUSED"
        rows.append({"applied": sub, "state": ss.get("verdict"), "plan_exit": cp,
                     "refused": (jp.get("refused") or "")[:40] or None, "repair": jp.get("repair"), "outcome": outcome})
    unsafe = D.reapply_unsafe(body, ops)
    proof = {"ops": n, "reapply_unsafe": unsafe,
             "reapply_unsafe_old_str_words": [len(ops[i]["old_str"].split()) for i in unsafe],
             "state_fetch": s0.get("verdict"), "state_landed": s1.get("verdict"),
             "plan_on_landed_exit": c2, "plan_on_landed_refused": (p2.get("refused") or "")[:40] or None,
             "doubled_in_landed": L.doubled(pid, L.C.collapse(full)),
             "partials": len(rows),
             "partials_state_partial": sum(1 for x in rows if x["state"] == "PARTIAL"),
             "partials_repaired_exact": sum(1 for x in rows if x["outcome"] == "REPAIRED_EXACT"),
             "partials_refused": sum(1 for x in rows if x["outcome"] == "REFUSED"),
             "partials_repaired_wrong": sum(1 for x in rows if x["outcome"] == "REPAIRED_WRONG"),
             "refusals": sorted({x["refused"] for x in rows if x["refused"]}),
             "rows": rows}
    proof["pass"] = (proof["state_fetch"] == "UNTOUCHED" and proof["state_landed"] == "LANDED"
                     and c2 == 3 and (p2.get("refused") or "").startswith("ALREADY_LANDED")
                     and not proof["doubled_in_landed"] and proof["partials_repaired_wrong"] == 0
                     and proof["partials_state_partial"] == len(rows))
    D.SOURCE = src
out = HERE / "results" / batch
out.mkdir(parents=True, exist_ok=True)
rec = {"mode": mode, "pid": pid, "page": page, "exit": r.returncode,
       "cmd": " ".join(c.replace(str(P4), "$P4").replace(str(EV), "EV") for c in cmd), "result": res, "proof": proof}
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
