#!/usr/bin/env python3
"""E6 step 5 (spec v2 §11): re-scan all 55 live bodies together, from their most recent fetch (the landing readbacks),
in memory. Checks: the installed validate_gcfpe_20260914.py with --bodies-stdin on all 55 at once (so the cross-body
checks run), the registry assertions of every row, and every canonical text placed once (blank-line runs collapsed, as
Notion stores paragraphs). Prints no body text.
usage: PYTHONDONTWRITEBYTECODE=1 python3 rescan.py <PID PAGE_ID lines on stdin>
"""
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import land as L  # noqa: E402

pages = [line.split()[:2] for line in sys.stdin if line.strip()]
bodies, fetched = {}, {}
for pid, page in pages:
    fetched[pid], bodies[pid] = L.latest_body(page)
contract = L.SKILLS / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
p = subprocess.run([sys.executable, str(L.SKILLS / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"),
                    str(L.SKILLS / "change-flow"), "--contract", str(contract), "--bodies-stdin"],
                   input=json.dumps(bodies), capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
v = json.loads(p.stdout)
reg = L.A.load_data(L.REG)
rows = {r["prompt_key"]: r for r in reg["prompts"]}
nph, _ = L.R.nph_from_registry(str(L.REG))
collapse = lambda x: re.sub(r"\n{2,}", "\n", x)  # noqa: E731
saved = dict(L.R.T)
L.R.T.update({k: collapse(t) for k, t in saved.items() if isinstance(t, str)})
findings, placement = {}, {}
for pid, body in bodies.items():
    f = sorted({(x["rule_id"], x["observed"]["summary"]) for x in L.A._evaluate_assertions(rows[pid], body, "e6-rescan")})
    if f:
        findings[pid] = f
    bad = {k: n for k, n in L.R.placement_counts(pid, collapse(body), nph).items() if n != 1}
    if bad:
        placement[pid] = bad
L.R.T.clear(); L.R.T.update(saved)
out = {"bodies": len(bodies), "rows": len(rows), "validator_exit": p.returncode, "validator_ok": v.get("ok"),
       "validated": len(v.get("prompt_bodies_validated") or []), "not_evaluated": v.get("prompt_body_checks_not_evaluated"),
       "validator_errors": v.get("errors"), "registry_findings": findings, "placement_not_once": placement,
       "fetched_before_landing": sorted(k for k, t in fetched.items() if t < "2026-09-23T13:"),
       "assertions": sum(len(x) for r in reg["prompts"] for x in (r["audit_assertions"] or {}).values() if isinstance(x, list))}
out["pass"] = (p.returncode == 0 and v.get("ok") is True and out["validated"] == 55 and not out["not_evaluated"]
               and not findings and not placement)
print(json.dumps(out, indent=1, ensure_ascii=False))
